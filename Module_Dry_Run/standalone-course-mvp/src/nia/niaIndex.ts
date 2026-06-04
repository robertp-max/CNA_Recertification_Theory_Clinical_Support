// Builds a lightweight in-memory, learner-facing course index from ContentV2.
//
// SAFETY: This index is consumed by learner-facing retrieval. It MUST NOT
// contain final-exam correct answers, `correct_id_internal`, `rationale_internal`
// for final items, or any full answer key. We read only safe, learner-facing
// fields below and never copy answer-key fields into NiaIndexRecord.body.

import { contentV2 } from "../data/contentV2Adapter";
import type { NiaIndexRecord, NiaReferenceType } from "./types";

// ---- Narrow, read-only views of the generated ContentV2 shape ----
// We intentionally describe only the fields Nia is allowed to read.
interface RawKeyTerm {
  term: string;
  definition: string;
}

interface RawCard {
  card_id: string;
  card_type: string;
  app?: { location?: string };
  display_title?: string;
  learner_facing_content?: string;
  learning_goal?: string;
  cna_practice_example?: string;
  why_it_matters?: string[];
  key_terms?: RawKeyTerm[];
  transcript_text?: string;
  source_reference?: string;
  status?: string;
  sme_review_flag?: string;
}

interface RawLesson {
  lesson_id: string;
  lesson_title: string;
  estimated_minutes?: number;
  source_reference?: string;
  status?: string;
  cards: RawCard[];
}

interface RawModule {
  module_id: string;
  module_title: string;
  short_title?: string;
  estimated_minutes?: number;
  learning_objectives?: string[];
  status?: string;
  sme_review_flag?: string;
  compliance_review_flag?: string;
  source_status_flag?: string;
  lessons: RawLesson[];
}

interface RawModuleAssessment {
  module_id: string;
  title?: string;
  splash_app_location?: string;
  coverage_topics?: string[];
  remediation_rule?: string;
  source_reference?: string;
}

interface RawFinalAssessment {
  title?: string;
  splash_app_location?: string;
  attempt_size?: number;
  pass_percent?: number;
  answer_key_policy?: string;
  instructions?: string;
  remediation_map?: Record<string, string>;
}

interface RawClinicalUnit {
  unit_id: string;
  title: string;
  app_location?: string;
  content?: string;
  status?: string;
  source_reference?: string;
  sme_review_flag?: string;
}

interface RawConfidenceCheck {
  check_id: string;
  title: string;
  app_location?: string;
  prompt?: string;
  scenario?: string;
  recommended_response?: string;
  refresh_resource?: string;
  status?: string;
}

interface RawCourseContent {
  control_facts?: {
    theory_total_minutes?: number;
    module_minutes?: Record<string, number>;
    required_flags?: string[];
  };
  compliance_guardrails?: string[];
  modules: RawModule[];
  assessments?: {
    module_assessments?: Record<string, RawModuleAssessment>;
    final_assessment?: RawFinalAssessment;
  };
  clinical_support?: {
    overview_app_location?: string;
    units?: RawClinicalUnit[];
    confidence_checks?: RawConfidenceCheck[];
  };
  app_copy?: {
    dashboard?: Record<string, string>;
    certificate?: Record<string, string>;
    final?: Record<string, string>;
    clinicalHub?: Record<string, unknown>;
  };
}

const content = contentV2 as unknown as RawCourseContent;

// App module ids (m0..m7) mirror src/data/contentV2Adapter.ts.
function appModuleId(canonicalModuleId: string): string {
  return `m${Number(canonicalModuleId.slice(1))}`;
}

function appLessonId(canonicalLessonId: string): string {
  return `l${Number(canonicalLessonId.slice(1))}`;
}

function isReviewFlag(flag?: string): boolean {
  return Boolean(flag && flag !== "None identified");
}

const STOPWORDS = new Set([
  "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "is", "are", "be",
  "this", "that", "with", "as", "at", "by", "it", "its", "do", "does", "not", "no",
  "you", "your", "i", "we", "they", "he", "she", "from", "if", "can", "will", "may",
  "must", "should", "what", "which", "how", "when", "where", "who", "about", "into",
  "any", "all", "but", "so", "than", "then", "their", "them", "these", "those",
  "have", "has", "had", "was", "were", "been", "being", "use", "used", "using",
  "during", "within", "while", "after", "before", "more", "most", "only", "also",
]);

function tokenize(text: string): string[] {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, " ")
    .split(/\s+/)
    .filter((w) => w.length > 2 && !STOPWORDS.has(w));
}

function deriveKeywords(parts: string[], extra: string[] = []): string[] {
  const out = new Set<string>(extra.map((k) => k.toLowerCase()));
  for (const part of parts) {
    for (const token of tokenize(part)) out.add(token);
  }
  return [...out];
}

function clip(text: string, max = 320): string {
  const clean = text.replace(/\s+/g, " ").trim();
  return clean.length <= max ? clean : `${clean.slice(0, max - 1).trimEnd()}…`;
}

function buildModuleVariants(canonicalModuleId: string): string[] {
  const n = Number(canonicalModuleId.slice(1));
  return [
    canonicalModuleId.toLowerCase(), // m00
    `m${n}`, // m0
    `m0${n}`, // m00 (single digit zero-pad)
    `module ${n}`,
    `module${n}`,
    `mod ${n}`,
  ];
}

let cachedIndex: NiaIndexRecord[] | null = null;

export function buildNiaIndex(): NiaIndexRecord[] {
  const records: NiaIndexRecord[] = [];

  // 1. Course overview / control facts.
  const minutes = content.control_facts?.theory_total_minutes ?? 720;
  const hours = Math.round((minutes / 60) * 10) / 10;
  records.push({
    id: "policy:course-overview",
    type: "course_policy",
    title: "Course overview and required theory hours",
    body:
      `This course contains ${minutes} minutes / ${hours} hours of required online theory across required modules M00 through M07. ` +
      `It provides partial online CE theory only and does not create clinical-hour credit or hands-on competency validation. ` +
      (content.app_copy?.dashboard?.compliance_notice ?? ""),
    keywords: deriveKeywords(
      ["course hours minutes theory total online ce partial credit recertification"],
      ["hours", "720", "12", "minutes", "course", "length", "long", "duration", "theory"],
    ),
    appLocation: "dashboard",
    status: "control-facts",
  });

  // Dashboard policy cards (theory / clinical / audit summaries).
  const dash = content.app_copy?.dashboard;
  if (dash) {
    for (const [key, label] of [
      ["theory_card", "Required theory summary"],
      ["clinical_card", "Optional clinical support summary"],
      ["audit_card", "No-PHI and audit summary"],
    ] as const) {
      const body = dash[key];
      if (!body) continue;
      records.push({
        id: `policy:dashboard-${key}`,
        type: "course_policy",
        title: label,
        body,
        keywords: deriveKeywords([label, body]),
        appLocation: "dashboard",
        status: "app-copy",
      });
    }
  }

  // Compliance guardrails as course policy.
  for (const [i, flag] of (content.control_facts?.required_flags ?? []).entries()) {
    records.push({
      id: `policy:flag-${i}`,
      type: "course_policy",
      title: "Course compliance fact",
      body: flag,
      keywords: deriveKeywords([flag], ["policy", "rule", "compliance"]),
      status: "control-facts",
    });
  }

  // 2-9. Modules, lessons, cards, key terms, goals, practice examples, why-it-matters.
  for (const mod of content.modules) {
    const appMod = appModuleId(mod.module_id);
    const moduleVariants = buildModuleVariants(mod.module_id);
    const moduleSafety: string[] = [];
    if (isReviewFlag(mod.sme_review_flag)) moduleSafety.push(mod.sme_review_flag as string);
    if (isReviewFlag(mod.source_status_flag)) moduleSafety.push(mod.source_status_flag as string);

    const lessonTitles = mod.lessons.map((l) => l.lesson_title).filter(Boolean);
    records.push({
      id: `module:${appMod}`,
      type: "module",
      title: `${mod.module_id} — ${mod.module_title}`,
      body:
        `Module ${Number(mod.module_id.slice(1))}: ${mod.module_title}. ` +
        `Estimated ${mod.estimated_minutes ?? 0} minutes. ` +
        (lessonTitles.length ? `Lessons: ${lessonTitles.join("; ")}. ` : "") +
        (mod.learning_objectives && mod.learning_objectives.length
          ? `Objectives: ${mod.learning_objectives.join(" ")}`
          : ""),
      keywords: deriveKeywords(
        [mod.module_title, mod.short_title ?? "", lessonTitles.join(" ")],
        [...moduleVariants, "module", "cover", "covers", "summary", "overview"],
      ),
      appLocation: `module.${mod.module_id.toLowerCase()}`,
      moduleId: appMod,
      moduleTitle: mod.module_title,
      sourceReference: `ContentV2 ${mod.module_id}`,
      status: mod.status,
      safetyFlags: moduleSafety.length ? moduleSafety : undefined,
    });

    for (const lesson of mod.lessons) {
      const appLesson = appLessonId(lesson.lesson_id);
      // Pick the richest learner-facing card for the lesson summary.
      const overview = lesson.cards.find((c) => c.card_type === "overview") ?? lesson.cards[0];
      const delivery = lesson.cards.find((c) => c.card_type === "delivery") ?? overview;
      const keyTerms = overview?.key_terms ?? [];
      const why = overview?.why_it_matters ?? [];

      records.push({
        id: `lesson:${appMod}:${appLesson}`,
        type: "lesson",
        title: `${mod.module_id} ${lesson.lesson_id} — ${lesson.lesson_title}`,
        body: clip(
          [
            overview?.learning_goal,
            delivery?.learner_facing_content ?? overview?.learner_facing_content,
            why.length ? `Why it matters: ${why.join(" ")}` : "",
            overview?.cna_practice_example ? `CNA practice example: ${overview.cna_practice_example}` : "",
          ]
            .filter(Boolean)
            .join(" "),
          600,
        ),
        keywords: deriveKeywords(
          [lesson.lesson_title, mod.module_title, overview?.learning_goal ?? "", keyTerms.map((t) => t.term).join(" ")],
          [...moduleVariants, lesson.lesson_id.toLowerCase(), appLesson],
        ),
        appLocation: overview?.app?.location,
        moduleId: appMod,
        moduleTitle: mod.module_title,
        lessonId: appLesson,
        lessonTitle: lesson.lesson_title,
        sourceReference: lesson.source_reference,
        status: lesson.status,
        safetyFlags: isReviewFlag(overview?.sme_review_flag) ? [overview!.sme_review_flag as string] : undefined,
      });

      // Index a focused card record for the delivery/teaching card, plus key terms.
      if (delivery?.learner_facing_content) {
        records.push({
          id: `card:${appMod}:${appLesson}:${delivery.card_id}`,
          type: "card",
          title: delivery.display_title || lesson.lesson_title,
          body: clip(delivery.learner_facing_content, 600),
          keywords: deriveKeywords(
            [delivery.display_title ?? "", lesson.lesson_title, delivery.learner_facing_content],
            [...moduleVariants, appLesson],
          ),
          appLocation: delivery.app?.location,
          moduleId: appMod,
          moduleTitle: mod.module_title,
          lessonId: appLesson,
          lessonTitle: lesson.lesson_title,
          cardId: delivery.card_id,
          sourceReference: delivery.source_reference,
          status: delivery.status,
        });
      }

      if (keyTerms.length) {
        records.push({
          id: `terms:${appMod}:${appLesson}`,
          type: "card",
          title: `Key terms — ${lesson.lesson_title}`,
          body: keyTerms.map((t) => `${t.term}: ${t.definition}`).join(" "),
          keywords: deriveKeywords(
            [keyTerms.map((t) => `${t.term} ${t.definition}`).join(" ")],
            [...moduleVariants, "key terms", "define", "definition", "term", "vocabulary", "glossary"],
          ),
          appLocation: overview?.app?.location,
          moduleId: appMod,
          moduleTitle: mod.module_title,
          lessonId: appLesson,
          lessonTitle: lesson.lesson_title,
          status: "key-terms",
        });
      }
    }
  }

  // 11. Assessment prompts only — module knowledge checks (NO answer keys).
  const moduleAssessments = content.assessments?.module_assessments ?? {};
  for (const [canonicalId, assessment] of Object.entries(moduleAssessments)) {
    const appMod = appModuleId(canonicalId);
    const topics = assessment.coverage_topics ?? [];
    records.push({
      id: `assessment:module:${appMod}`,
      type: "assessment",
      title: assessment.title || `${canonicalId} knowledge check`,
      body: clip(
        `Knowledge check for ${canonicalId}. Coverage topics: ${topics.join("; ")}. ` +
          (assessment.remediation_rule ? `To prepare: ${assessment.remediation_rule}` : ""),
        500,
      ),
      keywords: deriveKeywords(
        [assessment.title ?? "", topics.join(" "), assessment.remediation_rule ?? ""],
        [...buildModuleVariants(canonicalId), "quiz", "knowledge check", "practice", "study", "review", "readiness"],
      ),
      appLocation: assessment.splash_app_location,
      moduleId: appMod,
      sourceReference: assessment.source_reference,
      status: "assessment-overview",
    });
  }

  // Final assessment — policy + remediation topics ONLY. We deliberately do NOT
  // index individual final-exam question prompts, correct answers, or rationales.
  const final = content.assessments?.final_assessment;
  if (final) {
    const remediationTopics = Object.entries(final.remediation_map ?? {})
      .map(([mod, topic]) => `${mod}: ${topic}`)
      .join("; ");
    records.push({
      id: "assessment:final",
      type: "assessment",
      title: final.title || "Course final assessment",
      body: clip(
        `${final.instructions ?? ""} Pass threshold: ${final.pass_percent ?? 80}% across ${final.attempt_size ?? 25} drawn items. ` +
          `${final.answer_key_policy ?? "Correct answers are not revealed."} ` +
          (remediationTopics ? `Study by topic: ${remediationTopics}.` : ""),
        600,
      ),
      keywords: deriveKeywords(
        [final.title ?? "", final.instructions ?? "", remediationTopics],
        ["final", "final exam", "test", "exam", "pass", "score", "study", "readiness", "prepare", "review"],
      ),
      appLocation: final.splash_app_location,
      status: "final-overview",
    });
  }

  // 12. Clinical support — overview, units, confidence checks.
  const clinical = content.clinical_support;
  if (clinical) {
    records.push({
      id: "clinical:overview",
      type: "clinical_support",
      title: "Optional Clinical Support — overview",
      body:
        "Optional Clinical Support is separate, optional, non-credit, and non-gating. It does not count as clinical-hour credit and does not validate hands-on competency. " +
        "Use it for skills refresh and confidence support before, during, or after the required theory modules.",
      keywords: deriveKeywords(
        ["optional clinical support hub skills refresh confidence non credit non gating clinical hours competency"],
        ["clinical", "clinical hub", "clinical support", "clinical hours", "skills", "refresh", "confidence", "optional", "preceptor"],
      ),
      appLocation: clinical.overview_app_location ?? "clinical.hub.overview",
      status: "Optional - non-credit - non-gating",
    });

    for (const unit of clinical.units ?? []) {
      records.push({
        id: `clinical:unit:${unit.unit_id}`,
        type: "clinical_support",
        title: `Clinical Support — ${unit.title}`,
        body: clip(unit.content ?? unit.title, 500),
        keywords: deriveKeywords(
          [unit.title, unit.content ?? ""],
          ["clinical", "clinical hub", "clinical support", "optional", unit.unit_id.toLowerCase()],
        ),
        appLocation: unit.app_location,
        sourceReference: unit.source_reference,
        status: unit.status,
        safetyFlags: isReviewFlag(unit.sme_review_flag) ? [unit.sme_review_flag as string] : undefined,
      });
    }

    for (const check of clinical.confidence_checks ?? []) {
      records.push({
        id: `clinical:confidence:${check.check_id}`,
        type: "clinical_support",
        title: `Confidence check — ${check.title}`,
        body: clip(
          [check.prompt, check.recommended_response, check.refresh_resource ? `Refresh: ${check.refresh_resource}` : ""]
            .filter(Boolean)
            .join(" "),
          500,
        ),
        keywords: deriveKeywords(
          [check.title, check.prompt ?? "", check.refresh_resource ?? ""],
          ["clinical", "confidence", "confidence check", "skills", "optional", check.check_id.toLowerCase()],
        ),
        appLocation: check.app_location,
        status: check.status,
      });
    }
  }

  // 13. Certificate gate policy / app copy.
  const cert = content.app_copy?.certificate;
  if (cert) {
    records.push({
      id: "certificate:gate",
      type: "certificate_gate",
      title: "Certificate gate status",
      body: clip(
        [cert.intro, cert.locked_body, cert.ready_body, cert.restriction].filter(Boolean).join(" "),
        700,
      ),
      keywords: deriveKeywords(
        [cert.intro ?? "", cert.locked_body ?? "", cert.restriction ?? ""],
        ["certificate", "locked", "gate", "affidavit", "completion", "issue", "approval", "production", "unlock", "blocked"],
      ),
      appLocation: "certificate",
      status: "certificate-policy",
    });
  }

  // App help records (navigation orientation).
  records.push(
    {
      id: "help:navigation",
      type: "app_help",
      title: "Course navigation",
      body:
        "The course has four main areas: Dashboard (your status and what to do next), CE Modules (required theory modules and the final assessment), Certificate Gate (your completion requirements and certificate status), and Clinical Hub (optional clinical support).",
      keywords: deriveKeywords(
        ["navigation dashboard ce modules certificate gate clinical hub menu tabs where find next button"],
        ["navigate", "navigation", "where", "find", "menu", "tab", "button", "dashboard", "next", "resume", "login"],
      ),
      appLocation: "dashboard",
      status: "app-help",
    },
    {
      id: "help:phi",
      type: "course_policy",
      title: "No PHI policy",
      body:
        "No PHI (Protected Health Information) may be requested, typed, uploaded, shown, implied, stored, or used in examples. Do not enter real patient, resident, family, facility, chart, medical-record, date-of-birth, or room-number details. Use fictional examples only, such as \"Ms. Johnson\" or \"Mr. Park\".",
      keywords: deriveKeywords(
        ["phi protected health information resident patient name chart medical record dob room number fictional identifiers privacy"],
        ["phi", "resident name", "patient name", "medical record", "chart", "upload", "identifiers", "privacy"],
      ),
      status: "policy",
    },
    {
      id: "help:scope",
      type: "course_policy",
      title: "CNA scope of practice",
      body:
        "A CNA observes, reports, documents, follows the care plan, communicates to licensed staff or a supervisor, and escalates concerns. A CNA does not independently diagnose, treat, change medications, stage pressure injuries as independent authority, or make clinical judgments beyond CNA scope.",
      keywords: deriveKeywords(
        ["cna scope practice observe report document care plan escalate supervisor licensed nurse allowed cannot diagnose treat medication"],
        ["scope", "allowed", "cna can", "diagnose", "treat", "care plan", "escalate", "report", "observe", "document"],
      ),
      status: "policy",
    },
  );

  return records;
}

export function getNiaIndex(): NiaIndexRecord[] {
  if (!cachedIndex) cachedIndex = buildNiaIndex();
  return cachedIndex;
}
