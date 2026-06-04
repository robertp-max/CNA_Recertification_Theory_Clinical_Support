// Deterministic, fully-local Nia provider. This is the permanent safe fallback
// and the entire Phase-1 MVP: it answers learner questions from the ContentV2
// index with NO external API. The external provider (when enabled) returns the
// same NiaStructuredResponse contract so the UI never changes.

import {
  type NiaAction,
  type NiaCitation,
  type NiaIndexRecord,
  type NiaIntent,
  type NiaLinkedReference,
  type NiaProvider,
  type NiaProviderRequest,
  type NiaReferenceType,
  type NiaStructuredResponse,
} from "../types";
import { getNiaIndex } from "../niaIndex";
import { detectModuleId } from "../niaRetrieval";
import { makeAction } from "../niaActions";
import { NIA_BLOCK_MESSAGES } from "../niaGuardrails";

let responseCounter = 0;
function nextId(): string {
  responseCounter += 1;
  return `nia-${Date.now().toString(36)}-${responseCounter}`;
}

function findRecord(id: string): NiaIndexRecord | undefined {
  return getNiaIndex().find((r) => r.id === id);
}

const SCOPE_REMINDER =
  "As a CNA: observe, report, document, follow the care plan, communicate to licensed staff or your supervisor, and escalate concerns. " +
  "Do not independently diagnose, treat, change medications, or stage pressure injuries as independent authority.";

function locationLabel(record: NiaIndexRecord): string {
  switch (record.type) {
    case "module":
    case "lesson":
    case "card":
      return record.moduleTitle ? `CE Modules · ${record.moduleTitle}` : "CE Modules";
    case "assessment":
      return "CE Modules · Assessment";
    case "clinical_support":
      return "Clinical Hub";
    case "certificate_gate":
      return "Certificate Gate";
    case "course_policy":
      return "Course policy";
    case "app_help":
      return "App help";
    default:
      return "Course";
  }
}

function toCitation(record: NiaIndexRecord, relevance: "primary" | "secondary"): NiaCitation {
  return {
    id: `cite-${record.id}`,
    referenceId: record.id,
    referenceType: record.type,
    title: record.title,
    locationLabel: locationLabel(record),
    appLocation: record.appLocation,
    excerpt: record.body.length > 240 ? `${record.body.slice(0, 239).trimEnd()}…` : record.body,
    relevance,
  };
}

function toLinked(record: NiaIndexRecord): NiaLinkedReference {
  return {
    id: `ref-${record.id}`,
    type: record.type,
    title: record.title,
    description: record.body.length > 160 ? `${record.body.slice(0, 159).trimEnd()}…` : record.body,
    appLocation: record.appLocation,
    moduleId: record.moduleId,
    lessonId: record.lessonId,
    cardId: record.cardId,
    required: record.type === "module" || record.type === "lesson",
  };
}

function citationsFrom(records: NiaIndexRecord[], max = 4): NiaCitation[] {
  return records.slice(0, max).map((r, i) => toCitation(r, i === 0 ? "primary" : "secondary"));
}

function actionForType(record: NiaIndexRecord): NiaAction | null {
  switch (record.type) {
    case "module":
      return record.moduleId
        ? makeAction("open_module", `Open ${record.moduleTitle ?? "module"}`, { targetId: record.moduleId })
        : null;
    case "lesson":
      return record.moduleId
        ? makeAction("open_lesson", `Open lesson: ${record.lessonTitle ?? "lesson"}`, { targetId: record.moduleId })
        : null;
    case "clinical_support":
      return makeAction("open_clinical_hub", "Open Clinical Hub", { appLocation: record.appLocation });
    case "certificate_gate":
      return makeAction("open_certificate_gate", "Open Certificate Gate");
    default:
      return null;
  }
}

interface Draft {
  intent: NiaIntent;
  directAnswer: string;
  learnerSummary: string;
  nextSteps: string[];
  safetyNotes?: string[];
  scopeReminder?: string;
  confidence?: "high" | "medium" | "low";
  records: NiaIndexRecord[];
  actions?: NiaAction[];
  noAnswerFound?: boolean;
  noAnswerReason?: string;
  blockedReason?: NiaStructuredResponse["blockedReason"];
}

function finalize(draft: Draft, req: NiaProviderRequest): NiaStructuredResponse {
  const records = draft.records;
  const actions = draft.actions ?? [];
  // Append record-derived actions, de-duplicated by (type+targetId).
  const seen = new Set(actions.map((a) => `${a.type}:${a.targetId ?? ""}`));
  for (const record of records) {
    const action = actionForType(record);
    if (action && !seen.has(`${action.type}:${action.targetId ?? ""}`)) {
      seen.add(`${action.type}:${action.targetId ?? ""}`);
      actions.push(action);
    }
  }

  return {
    id: nextId(),
    intent: draft.intent,
    directAnswer: draft.directAnswer,
    learnerSummary: draft.learnerSummary,
    nextSteps: draft.nextSteps,
    safetyNotes: draft.safetyNotes ?? [],
    scopeReminder: draft.scopeReminder,
    confidence: draft.confidence ?? (records.length ? "high" : "low"),
    citations: citationsFrom(records),
    linkedReferences: records.map(toLinked),
    availableActions: actions.slice(0, 5),
    noAnswerFound: draft.noAnswerFound ?? false,
    noAnswerReason: draft.noAnswerReason,
    blockedReason: draft.blockedReason,
    meta: {
      elapsedMs: Math.max(0, Math.round(performance.now() - req.startedAt)),
      provider: "deterministic",
      retrievedReferenceIds: records.map((r) => r.id),
      currentCourseLocation: req.context.activeView ?? req.context.route ?? undefined,
    },
  };
}

// ---- Blocked responses ----
function buildBlocked(req: NiaProviderRequest): NiaStructuredResponse {
  const reason = req.guardrail.blockedReason ?? "out_of_scope";
  const phiRef = findRecord("help:phi");
  const scopeRef = findRecord("help:scope");
  const finalRef = findRecord("assessment:final");

  // If a PHI-blocked message also describes an emergency/clinical situation,
  // add safe CNA-scope guidance (escalate / notify) without diagnosing.
  const emergencyContext = /\b(fell|fall|head|emergency|hit|injur|unrespons|choking|bleed|chest pain|stroke|seizure)\b/i.test(
    req.request.input,
  );
  const phiNextSteps = emergencyContext
    ? [
        "For a real emergency, follow your facility's protocol and notify licensed staff or your supervisor immediately.",
        "Replace any real names or details with a fictional example, then ask me about the general course concept.",
      ]
    : [
        "Replace any real names or details with a fictional example.",
        "Ask me to explain the general course concept instead.",
      ];

  const drafts: Record<string, Draft> = {
    phi: {
      intent: "phi_safety",
      directAnswer: req.guardrail.message ?? NIA_BLOCK_MESSAGES.phi,
      learnerSummary:
        "This course never uses real identifiers. Rewrite any scenario with a fictional name (for example, \"Ms. Johnson\" or \"Mr. Park\") and no real dates, room numbers, or record numbers, and I can help.",
      nextSteps: phiNextSteps,
      safetyNotes: emergencyContext
        ? [
            "No PHI may be entered, uploaded, shown, or implied anywhere in this course.",
            "Nia cannot make patient-specific clinical decisions; follow the care plan and notify licensed staff or your supervisor.",
          ]
        : ["No PHI may be entered, uploaded, shown, or implied anywhere in this course."],
      scopeReminder: emergencyContext ? SCOPE_REMINDER : undefined,
      records: phiRef ? [phiRef] : [],
      actions: [makeAction("show_no_phi_guidance", "Review the no-PHI rules", { priority: "primary" })],
      blockedReason: "phi",
      confidence: "high",
    },
    final_exam_key: {
      intent: "final_exam_readiness",
      directAnswer: req.guardrail.message ?? NIA_BLOCK_MESSAGES.final_exam_key,
      learnerSummary:
        "The final exam keeps correct answers internal so the assessment stays meaningful. I can still help you prepare by topic — review the related modules and use the knowledge checks.",
      nextSteps: [
        "Tell me a topic (for example, infection control or vital signs) and I will point you to the right module.",
        "Use the module knowledge checks to test yourself before the final.",
      ],
      safetyNotes: ["Final exam answers and answer keys are never shown to learners."],
      records: finalRef ? [finalRef] : [],
      actions: [makeAction("practice_quiz_readiness", "Go to CE Modules to study", { priority: "primary" })],
      blockedReason: "final_exam_key",
      confidence: "high",
    },
    clinical_advice: {
      intent: "scope_safety",
      directAnswer: req.guardrail.message ?? NIA_BLOCK_MESSAGES.clinical_advice,
      learnerSummary:
        "For any real situation, follow the care plan, observe and report objectively, notify licensed staff or your supervisor, and use your facility's emergency protocol when needed. I can explain the general course concept behind it.",
      nextSteps: [
        "Notify a licensed nurse or supervisor for patient-specific decisions.",
        "Ask me to explain the general course topic (no real patient details).",
      ],
      safetyNotes: ["Nia is not a clinician and cannot make patient-specific clinical decisions."],
      scopeReminder: SCOPE_REMINDER,
      records: scopeRef ? [scopeRef] : [],
      actions: [makeAction("show_scope_guidance", "Review CNA scope", { priority: "primary" })],
      blockedReason: "clinical_advice",
      confidence: "high",
    },
    out_of_scope: {
      intent: "out_of_scope",
      directAnswer: req.guardrail.message ?? NIA_BLOCK_MESSAGES.out_of_scope,
      learnerSummary:
        "I am a course-grounded study coach. I cannot guarantee renewals, issue or approve certificates, or grant clinical-hour credit, but I can help you understand and complete the course.",
      nextSteps: [
        "Ask me about a module, the certificate gate, or how to study for the final.",
        "Check the Certificate Gate to see your remaining requirements.",
      ],
      safetyNotes: ["Certificate production remains disabled until required approvals and gates are complete."],
      records: [],
      actions: [makeAction("open_certificate_gate", "Open Certificate Gate", { priority: "primary" })],
      blockedReason: "out_of_scope",
      confidence: "high",
    },
  };

  return finalize(drafts[reason] ?? drafts.out_of_scope, req);
}

const HOURS_RE = /\b(how many )?(hours?|how long|minutes|duration|length|long is)\b/i;

function answerHours(req: NiaProviderRequest): Draft {
  const minutes = req.context.courseCounts.requiredTheoryMinutes;
  const hours = req.context.courseCounts.requiredTheoryHours;
  const overview = findRecord("policy:course-overview");
  return {
    intent: "general_course_question",
    directAnswer: `This course contains ${minutes} minutes / ${hours} hours of required online theory across modules M00 through M07.`,
    learnerSummary:
      "This is partial online CE theory only. It does not create clinical-hour credit and does not, by itself, complete California CNA renewal — you remain responsible for your full renewal requirements.",
    nextSteps: [
      "Continue working through your required theory modules.",
      "Check the Certificate Gate to see what is still required.",
      "Never enter real patient or resident information (no PHI).",
    ],
    safetyNotes: ["Optional Clinical Support is separate and does not count toward these required theory hours."],
    records: overview ? [overview] : [],
    confidence: "high",
  };
}

function answerClinicalSupport(req: NiaProviderRequest): Draft {
  const overview = findRecord("clinical:overview");
  const records = [overview, ...req.records.filter((r) => r.type === "clinical_support" && r.id !== overview?.id)].filter(
    Boolean,
  ) as NiaIndexRecord[];
  return {
    intent: "clinical_support",
    directAnswer:
      "Optional Clinical Support is separate, optional, non-credit, and non-gating. It does not count as clinical-hour credit and does not validate hands-on competency.",
    learnerSummary:
      "You can use Clinical Support for skills refresh and confidence support before, during, or after the required theory modules. Nothing there is required for your certificate.",
    nextSteps: [
      "Open the Clinical Hub to browse optional skills-refresh topics and confidence checks.",
      "Continue your required theory modules — those are what affect your certificate.",
    ],
    safetyNotes: ["Optional Clinical Support is never a certificate gate and is not clinical-hour credit."],
    records: records.length ? records.slice(0, 4) : overview ? [overview] : [],
    actions: [makeAction("open_clinical_hub", "Open Clinical Hub", { priority: "primary" })],
    confidence: "high",
  };
}

function answerCertificateGate(req: NiaProviderRequest): Draft {
  const cert = findRecord("certificate:gate");
  const blockers = req.context.certificateGate.blockerLabels;
  const summaryLine =
    blockers && blockers.length
      ? `Based on your current status, these requirements still need attention: ${blockers.join("; ")}.`
      : blockers && blockers.length === 0
        ? "Your tracked certificate requirements currently look complete in this preview, but production issuance stays disabled until approval metadata is configured."
        : "I cannot read your exact progress right now, so check the Certificate Gate page for your specific status.";

  return {
    intent: "certificate_gate",
    directAnswer:
      "A certificate can stay locked for several reasons: required modules incomplete, the final exam not yet passed, active-time/completion checks not met, or affidavit/approval metadata still pending. Production certificate issuance is disabled in this preview.",
    learnerSummary: summaryLine,
    nextSteps: [
      "Open the Certificate Gate to see exactly which requirements are outstanding.",
      "Finish any incomplete required theory modules and the final assessment.",
    ],
    safetyNotes: [
      "Certificate production remains disabled until approval metadata, approved wording, affidavit method, and all gates are complete.",
    ],
    records: cert ? [cert] : [],
    actions: [makeAction("open_certificate_gate", "Open Certificate Gate", { priority: "primary" })],
    confidence: cert ? "high" : "medium",
  };
}

function answerFinalReadiness(req: NiaProviderRequest): Draft {
  const finalRef = findRecord("assessment:final");
  const records = [finalRef, ...req.records.filter((r) => r.id !== finalRef?.id)].filter(Boolean) as NiaIndexRecord[];
  return {
    intent: "final_exam_readiness",
    directAnswer:
      "To get ready for the final, review the required modules, focus on weaker topics, and use the module knowledge checks. I cannot reveal final exam answers or answer keys.",
    learnerSummary:
      "Study the underlying topics rather than memorizing answers. The final draws from required theory across infection control, resident rights, dementia/communication, mobility/safety, nutrition/skin/vitals, and documentation/scope.",
    nextSteps: [
      "Re-read the modules tied to topics you find hardest.",
      "Use the module knowledge checks to self-test.",
      "Review any remediation notes from earlier attempts.",
    ],
    safetyNotes: ["Final results never display the full answer key, and Nia will not provide it."],
    records: records.slice(0, 4),
    actions: [makeAction("practice_quiz_readiness", "Go to CE Modules", { priority: "primary" })],
    confidence: "high",
  };
}

function answerQuizReadiness(req: NiaProviderRequest): Draft {
  return {
    intent: "quiz_readiness",
    directAnswer:
      "Knowledge checks help you confirm understanding before moving on. Review the relevant lesson cards and key terms, then take the check.",
    learnerSummary:
      "Module knowledge checks are for learning, not for memorizing answers. If you miss one, use the Challenge Debrief and re-read the related lesson.",
    nextSteps: [
      "Open the module you are studying and review its lessons and key terms.",
      "Take the knowledge check, then review any remediation guidance.",
    ],
    safetyNotes: ["Answer keys for the final assessment are never shown."],
    records: req.records.slice(0, 4),
    confidence: req.records.length ? "high" : "medium",
  };
}

function answerModuleSummary(req: NiaProviderRequest): Draft {
  const moduleId = detectModuleId(req.request.input) ?? req.context.currentModuleId;
  const moduleRec = moduleId ? findRecord(`module:${moduleId}`) : undefined;
  const lessonRecs = moduleId
    ? getNiaIndex().filter((r) => r.type === "lesson" && r.moduleId === moduleId).slice(0, 3)
    : [];

  if (!moduleRec) {
    return answerGeneral(req);
  }

  const flagNote = moduleRec.safetyFlags?.length
    ? `Note: this module's content is flagged for SME/source review (${moduleRec.safetyFlags.join("; ")}), so treat it as draft/review-flagged rather than production-approved.`
    : undefined;

  return {
    intent: "module_summary",
    directAnswer: `${moduleRec.title}. ${moduleRec.body}`,
    learnerSummary: lessonRecs.length
      ? `Main lessons include: ${lessonRecs.map((l) => l.lessonTitle).filter(Boolean).join("; ")}.`
      : "Open the module to work through its lessons in order.",
    nextSteps: [
      `Open ${moduleRec.moduleTitle ?? "the module"} to start or resume its lessons.`,
      "Review the key terms in each lesson before the knowledge check.",
    ],
    safetyNotes: flagNote ? [flagNote] : [],
    records: [moduleRec, ...lessonRecs].slice(0, 4),
    actions: moduleRec.moduleId
      ? [makeAction("open_module", `Open ${moduleRec.moduleTitle ?? "module"}`, { targetId: moduleRec.moduleId, priority: "primary" })]
      : [],
    confidence: "high",
  };
}

function answerLessonExplanation(req: NiaProviderRequest): Draft {
  if (!req.records.length) return answerGeneral(req);
  const top = req.records[0];
  return {
    intent: "lesson_explanation",
    directAnswer: top.body.length > 360 ? `${top.body.slice(0, 359).trimEnd()}…` : top.body,
    learnerSummary: top.moduleTitle
      ? `This comes from ${top.moduleTitle}${top.lessonTitle ? ` · ${top.lessonTitle}` : ""}. Use the reference card below to open it in the course.`
      : "Use the reference card below to open the related course content.",
    nextSteps: [
      "Open the linked lesson to read the full content and key terms.",
      "Try the related knowledge check to confirm your understanding.",
    ],
    safetyNotes: top.safetyFlags?.length
      ? [`This content is flagged for SME/source review (${top.safetyFlags.join("; ")}); treat it as draft.`]
      : [],
    scopeReminder: /infection|skin|pressure|vital|wound|clinical/i.test(top.title + top.body) ? SCOPE_REMINDER : undefined,
    records: req.records.slice(0, 4),
    confidence: "high",
  };
}

function answerScope(req: NiaProviderRequest): Draft {
  const scopeRef = findRecord("help:scope");
  return {
    intent: "scope_safety",
    directAnswer:
      "CNA scope means you observe, report, document, follow the care plan, communicate to licensed staff or your supervisor, and escalate concerns.",
    learnerSummary:
      "Staying in scope keeps residents safe and keeps you within your role. Decisions like diagnosing, treating, or changing medications belong to licensed staff.",
    nextSteps: [
      "When unsure, observe and report to a licensed nurse or supervisor.",
      "Follow the care plan and your facility's policies.",
    ],
    safetyNotes: ["Do not independently diagnose, treat, change medications, or stage pressure injuries as independent CNA authority."],
    scopeReminder: SCOPE_REMINDER,
    records: [scopeRef, ...req.records.filter((r) => r.id !== "help:scope")].filter(Boolean).slice(0, 4) as NiaIndexRecord[],
    actions: [makeAction("show_scope_guidance", "Review CNA scope", { priority: "primary" })],
    confidence: "high",
  };
}

function answerPhi(req: NiaProviderRequest): Draft {
  const phiRef = findRecord("help:phi");
  return {
    intent: "phi_safety",
    directAnswer:
      "No. Never enter real patient or resident names, dates of birth, room numbers, medical-record numbers, or facility identifiers anywhere in this course.",
    learnerSummary:
      "PHI (Protected Health Information) must never be requested, typed, uploaded, shown, or implied here. Use fictional examples like \"Ms. Johnson\" or \"Mr. Park\" instead.",
    nextSteps: [
      "Use a fictional name and remove any real details.",
      "Ask me to explain the general course concept with no identifiers.",
    ],
    safetyNotes: ["This applies to every course activity, including practice documentation and scenarios."],
    records: phiRef ? [phiRef] : [],
    actions: [makeAction("show_no_phi_guidance", "Review the no-PHI rules", { priority: "primary" })],
    confidence: "high",
  };
}

function answerNavigation(req: NiaProviderRequest): Draft {
  const ctx = req.context;
  const nextId = ctx.progress.nextIncompleteModuleId;
  const nextTitle = ctx.progress.nextIncompleteModuleTitle;
  const help = findRecord("help:navigation");

  let directAnswer: string;
  const actions: NiaAction[] = [];
  if (ctx.progress.requiredTheoryComplete) {
    directAnswer =
      "You've completed the required theory modules. Next, head to the final assessment and then the Certificate Gate to review your status.";
    actions.push(makeAction("practice_quiz_readiness", "Go to CE Modules / Final", { priority: "primary" }));
    actions.push(makeAction("open_certificate_gate", "Open Certificate Gate"));
  } else if (nextId) {
    directAnswer = `Your next required step is ${nextTitle ?? nextId}. Open it from CE Modules and work through the lessons in order.`;
    actions.push(makeAction("open_module", `Open ${nextTitle ?? nextId}`, { targetId: nextId, priority: "primary" }));
  } else {
    directAnswer =
      "Start from the Dashboard to see your status, then open CE Modules to continue the next required module. I can't read your exact progress right now, so use the Dashboard for specifics.";
    actions.push(makeAction("open_module", "Open CE Modules", { targetId: "modules", priority: "primary" }));
  }

  return {
    intent: "course_navigation",
    directAnswer,
    learnerSummary:
      "The course has four areas: Dashboard, CE Modules, Certificate Gate, and Clinical Hub. The Dashboard always shows where you are and what to do next.",
    nextSteps: [
      "Use the Dashboard to confirm your current status.",
      "Open CE Modules to continue your required theory.",
    ],
    records: [help, ...req.records.filter((r) => r.id !== "help:navigation")].filter(Boolean).slice(0, 4) as NiaIndexRecord[],
    actions,
    confidence: nextId || ctx.progress.requiredTheoryComplete ? "high" : "medium",
  };
}

function answerTechnical(req: NiaProviderRequest): Draft {
  const help = findRecord("help:navigation");
  return {
    intent: "technical_help",
    directAnswer:
      "For app or navigation issues, use the top navigation to move between Dashboard, CE Modules, Certificate Gate, and Clinical Hub. Your progress is saved automatically in this browser.",
    learnerSummary:
      "If something looks stuck, try the Dashboard first. For account, login, or technical problems your facility administrator or course support can help.",
    nextSteps: [
      "Return to the Dashboard and reopen the area you need.",
      "Contact your course administrator for login or account issues.",
    ],
    records: help ? [help] : [],
    confidence: "medium",
  };
}

function answerGeneral(req: NiaProviderRequest): Draft {
  if (req.records.length) {
    const top = req.records[0];
    return {
      intent: "general_course_question",
      directAnswer: top.body.length > 360 ? `${top.body.slice(0, 359).trimEnd()}…` : top.body,
      learnerSummary: "Here's the most relevant course content I found. Open the reference below for the full details.",
      nextSteps: [
        "Open the linked reference to read more.",
        "Ask me about a specific module, the certificate gate, or how to study for the final.",
      ],
      records: req.records.slice(0, 4),
      confidence: "medium",
    };
  }
  return {
    intent: "general_course_question",
    directAnswer:
      "I couldn't find enough course-grounded information to answer that confidently, so I'd rather not guess.",
    learnerSummary:
      "I can help with things like: what to do next, what a module covers, how many hours the course is, whether Clinical Support counts for clinical hours, why a certificate is locked, how to study for the final, CNA scope, and the no-PHI rules.",
    nextSteps: [
      "Try asking about a specific module (for example, \"What does M01 cover?\").",
      "Ask \"What should I do next?\" or \"Why is my certificate locked?\".",
    ],
    records: [],
    noAnswerFound: true,
    noAnswerReason: "No course index records scored above the relevance threshold.",
    confidence: "low",
  };
}

export class DeterministicNiaProvider implements NiaProvider {
  readonly providerId = "deterministic" as const;

  async generate(req: NiaProviderRequest): Promise<NiaStructuredResponse> {
    if (req.guardrail.blocked) {
      return buildBlocked(req);
    }

    const input = req.request.input;
    let draft: Draft;

    switch (req.intent) {
      case "clinical_support":
        draft = answerClinicalSupport(req);
        break;
      case "certificate_gate":
        draft = answerCertificateGate(req);
        break;
      case "final_exam_readiness":
        draft = answerFinalReadiness(req);
        break;
      case "quiz_readiness":
        draft = answerQuizReadiness(req);
        break;
      case "module_summary":
        draft = answerModuleSummary(req);
        break;
      case "lesson_explanation":
        draft = answerLessonExplanation(req);
        break;
      case "scope_safety":
        draft = answerScope(req);
        break;
      case "phi_safety":
        draft = answerPhi(req);
        break;
      case "course_navigation":
        draft = HOURS_RE.test(input) && /\b(course|class|program|training|this)\b/i.test(input)
          ? answerHours(req)
          : answerNavigation(req);
        break;
      case "technical_help":
        draft = answerTechnical(req);
        break;
      case "general_course_question":
      default:
        draft = HOURS_RE.test(input) ? answerHours(req) : answerGeneral(req);
        break;
    }

    return finalize(draft, req);
  }
}

export const deterministicNiaProvider = new DeterministicNiaProvider();
