// Deterministic retrieval + intent classification over the Nia course index.
// No vector DB and no extra dependencies — lexical scoring is enough for the MVP.

import type { NiaContextSnapshot, NiaIndexRecord, NiaIntent } from "./types";
import { getNiaIndex } from "./niaIndex";

const STOPWORDS = new Set([
  "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "is", "are", "be",
  "this", "that", "with", "as", "at", "by", "it", "its", "do", "does", "not", "no",
  "you", "your", "i", "we", "my", "me", "from", "if", "can", "will", "may", "should",
  "what", "which", "how", "when", "where", "who", "about", "into", "any", "all",
  "but", "so", "than", "then", "have", "has", "had", "was", "were", "been", "help",
]);

export function normalizeQuery(input: string): string {
  return input.toLowerCase().replace(/\s+/g, " ").trim();
}

function tokenize(text: string): string[] {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, " ")
    .split(/\s+/)
    .filter((w) => w.length > 2 && !STOPWORDS.has(w));
}

// Detect an explicit app module id (m0..m7) from "M01", "module 1", "mod 5", etc.
export function detectModuleId(input: string): string | null {
  const q = input.toLowerCase();
  const explicit = q.match(/\bm0?([0-7])\b/);
  if (explicit) return `m${Number(explicit[1])}`;
  const worded = q.match(/\bmodule\s*0?([0-7])\b/);
  if (worded) return `m${Number(worded[1])}`;
  return null;
}

interface DetectedTargets {
  moduleId: string | null;
  mentionsCertificate: boolean;
  mentionsClinical: boolean;
  mentionsFinal: boolean;
  mentionsQuiz: boolean;
}

function detectTargets(input: string): DetectedTargets {
  const q = input.toLowerCase();
  return {
    moduleId: detectModuleId(input),
    mentionsCertificate: /\b(certificate|certification|gate|affidavit|completion|locked|unlock)\b/.test(q),
    mentionsClinical: /\b(clinical hub|clinical support|clinical hour|clinical|skills refresh|confidence check|preceptor)\b/.test(q),
    mentionsFinal: /\b(final exam|final|exam|test)\b/.test(q),
    mentionsQuiz: /\b(quiz|knowledge check|practice question|practice quiz)\b/.test(q),
  };
}

// ---- Intent classifier (deterministic, ordered) ----
export function classifyNiaIntent(input: string): NiaIntent {
  const q = input.toLowerCase();

  // PHI signals first (also caught by guardrails, but the intent stays phi_safety).
  if (/\b(phi|protected health|resident name|patient name|patient's name|resident's name|medical record|mrn|date of birth|\bdob\b|room number|upload|chart)\b/.test(q)) {
    return "phi_safety";
  }
  // Scope / "can I" safety.
  if (/\b(scope|allowed to|am i allowed|cna can|can i do|can a cna|diagnose|treat|out of scope|within scope)\b/.test(q)) {
    return "scope_safety";
  }
  if (/\b(certificate|certification|gate|affidavit|completion gate|locked|unlock)\b/.test(q)) {
    return "certificate_gate";
  }
  if (/\b(clinical hub|clinical support|clinical hour|skills refresh|confidence check|preceptor)\b/.test(q)) {
    return "clinical_support";
  }
  if (/\b(final exam|final|pass score|passing score|answer key|answers)\b/.test(q)) {
    return "final_exam_readiness";
  }
  if (/\b(quiz|knowledge check|practice question|practice quiz)\b/.test(q)) {
    return "quiz_readiness";
  }
  if (/\b(explain|summarize|summary|what does|what is|define|definition|key terms|cover|covers|tell me about)\b/.test(q)) {
    // Module-scoped explanation vs. lesson/term explanation.
    return detectModuleId(input) ? "module_summary" : "lesson_explanation";
  }
  if (/\b(next|where|resume|progress|module|lesson|card|navigate|go to|dashboard|menu)\b/.test(q)) {
    return "course_navigation";
  }
  if (/\b(login|log in|sign in|app|button|technical|broken|error|not working|page)\b/.test(q)) {
    return "technical_help";
  }
  return "general_course_question";
}

export interface RetrievalOptions {
  limit?: number;
  context?: NiaContextSnapshot;
  intent?: NiaIntent;
}

const INTENT_TYPE_BOOST: Partial<Record<NiaIntent, NiaIndexRecord["type"][]>> = {
  certificate_gate: ["certificate_gate"],
  clinical_support: ["clinical_support"],
  final_exam_readiness: ["assessment"],
  quiz_readiness: ["assessment"],
  module_summary: ["module", "lesson"],
  lesson_explanation: ["lesson", "card"],
  phi_safety: ["course_policy"],
  scope_safety: ["course_policy"],
  course_navigation: ["app_help", "module"],
  technical_help: ["app_help"],
};

export function retrieve(input: string, options: RetrievalOptions = {}): NiaIndexRecord[] {
  const { limit = 4, context, intent } = options;
  const index = getNiaIndex();
  const normalized = normalizeQuery(input);
  const tokens = tokenize(normalized);
  const tokenSet = new Set(tokens);
  const targets = detectTargets(input);
  const boostTypes = intent ? INTENT_TYPE_BOOST[intent] ?? [] : [];

  const scored = index.map((record) => {
    let score = 0;
    const keywordSet = new Set(record.keywords);

    // Keyword overlap.
    for (const token of tokenSet) {
      if (keywordSet.has(token)) score += 3;
    }

    // Phrase scoring against title + body.
    const haystack = `${record.title} ${record.body}`.toLowerCase();
    for (const token of tokenSet) {
      if (token.length > 3 && haystack.includes(token)) score += 1;
    }
    if (normalized.length > 6 && haystack.includes(normalized)) score += 6;

    // Title boost.
    const titleLower = record.title.toLowerCase();
    for (const token of tokenSet) {
      if (titleLower.includes(token)) score += 2;
    }

    // Explicit module id boost.
    if (targets.moduleId && record.moduleId === targets.moduleId) score += 12;

    // Reference-type targeting.
    if (targets.mentionsCertificate && record.type === "certificate_gate") score += 8;
    if (targets.mentionsClinical && record.type === "clinical_support") score += 8;
    if ((targets.mentionsFinal || targets.mentionsQuiz) && record.type === "assessment") score += 6;

    // Intent-type boost.
    if (boostTypes.includes(record.type)) score += 4;

    // Current-location boost.
    if (context?.currentModuleId && record.moduleId === context.currentModuleId) score += 3;

    return { record, score };
  });

  return scored
    .filter((s) => s.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, limit)
    .map((s) => s.record);
}
