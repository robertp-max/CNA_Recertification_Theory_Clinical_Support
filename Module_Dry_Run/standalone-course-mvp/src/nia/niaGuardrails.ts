// Nia guardrails — run BEFORE retrieval/generation (input screening) and AFTER
// generation (output screening). Nia never reveals final-exam answer keys,
// never invites PHI, never gives patient-specific clinical advice, and never
// claims certification/clinical-hour authority.

import type { NiaGuardrailResult, NiaStructuredResponse } from "./types";

export const NIA_BLOCK_MESSAGES = {
  phi:
    "Please do not enter real patient, resident, family, facility, or medical-record information here. " +
    "I can still help if you rewrite the situation as a fictional training scenario with no identifiers.",
  final_exam_key:
    "I can help you study the topic and explain the course content, but I cannot provide final exam answers or answer keys.",
  clinical_advice:
    "I cannot make patient-specific clinical decisions. For CNA practice, follow the care plan, observe and report, and notify " +
    "licensed staff or a supervisor. I can explain the general course concept instead.",
  out_of_scope:
    "That looks outside what this course coach can do. I cannot guarantee renewals, issue or approve certificates, or grant " +
    "clinical-hour credit. I can help you study the course content, navigate the modules, and understand the certificate gate.",
} as const;

// ---- Detectors ----
const PHI_PATTERNS: RegExp[] = [
  /\b(resident|patient|client)\s+(named|name is|is named)\b/i,
  /\b[Mm]y\s+(resident|patient|client)\b[^.?!]*\b[A-Z][a-z]+\b/, // "My resident Mary..."
  /\b(date of birth|d\.?o\.?b\.?)\b/i,
  /\b(mrn|medical record(\s*(number|#|no))?)\b/i,
  /\bssn\b|\bsocial security\b/i,
  /\broom\s*(number|#|\d+)\b/i,
  /\b(uploaded?|attach(ed)?|upload)\b[^.?!]*\b(chart|record|file)\b/i,
];

// "Ms./Mr./Mrs." + proper name is a likely real identifier in a non-fiction phrasing.
const NAMED_PERSON = /\b(mr|mrs|ms|miss|dr)\.?\s+[A-Z][a-z]+/;
const FICTION_HINT = /\b(fictional|fictitious|example|hypothetical|pretend|made up|imaginary|sample|practice)\b/i;

const FINAL_KEY_PATTERNS: RegExp[] = [
  /\b(answer key|answer keys)\b/i,
  /\b(give|tell|show|what('?s| is| are))\b[^.?!]*\b(answer|answers)\b/i,
  /\b(correct (option|answer|choice|id))\b/i,
  /\bfinal\b[^.?!]*\b(answer|answers|key)\b/i,
  /\bq0?\d+\b[^.?!]*\banswer\b/i,
  /\bcorrect_id_internal\b/i,
];

const CLINICAL_ADVICE_PATTERNS: RegExp[] = [
  /\b(diagnos(e|is)|what('?s| is) wrong with)\b/i,
  /\b(treat|treatment for|how (do|should) i treat)\b/i,
  /\b(change|adjust|give|administer|stop)\b[^.?!]*\bmedication|\bmeds?\b|\bdose\b/i,
  /\bstage\b[^.?!]*\b(wound|pressure (injury|ulcer|sore))\b/i,
  /\bwhat (should|do) i do for\b[^.?!]*\b(my|this)\b[^.?!]*\b(patient|resident|client)\b/i,
];

const UNSUPPORTED_CLAIM_PATTERNS: RegExp[] = [
  /\bguarantee\b[^.?!]*\b(renewal|recert|pass|certificate)\b/i,
  /\b(print|issue|generate|download)\b[^.?!]*\b(official|production|real)\b[^.?!]*\bcertificate\b/i,
  /\b(approve|approval of)\b[^.?!]*\b(cdph|certificate)\b/i,
  /\breplace\b[^.?!]*\bclinical hours?\b/i,
];

function anyMatch(patterns: RegExp[], text: string): boolean {
  return patterns.some((re) => re.test(text));
}

// PRE-generation screening of the raw learner input.
export function screenInput(input: string): NiaGuardrailResult {
  const signals: string[] = [];
  const text = input.trim();

  const phiMatched = anyMatch(PHI_PATTERNS, text) || (NAMED_PERSON.test(text) && !FICTION_HINT.test(text));
  const clinicalMatched = anyMatch(CLINICAL_ADVICE_PATTERNS, text);
  const finalKeyMatched = anyMatch(FINAL_KEY_PATTERNS, text);
  const unsupportedMatched = anyMatch(UNSUPPORTED_CLAIM_PATTERNS, text);

  if (phiMatched) signals.push("phi");
  if (clinicalMatched) signals.push("clinical_advice");
  if (finalKeyMatched) signals.push("final_exam_key");
  if (unsupportedMatched) signals.push("unsupported_claim");

  // Priority order: PHI > final-exam key > clinical advice > unsupported claim.
  if (phiMatched) {
    return { blocked: true, blockedReason: "phi", message: NIA_BLOCK_MESSAGES.phi, signals };
  }
  if (finalKeyMatched) {
    return { blocked: true, blockedReason: "final_exam_key", message: NIA_BLOCK_MESSAGES.final_exam_key, signals };
  }
  if (clinicalMatched) {
    return { blocked: true, blockedReason: "clinical_advice", message: NIA_BLOCK_MESSAGES.clinical_advice, signals };
  }
  if (unsupportedMatched) {
    return { blocked: true, blockedReason: "out_of_scope", message: NIA_BLOCK_MESSAGES.out_of_scope, signals };
  }

  return { blocked: false, signals };
}

// POST-generation screening: scrub disallowed content from any provider output
// (especially the external provider). Returns a sanitized response.
const FORBIDDEN_OUTPUT_PHRASES = [
  /correct_id_internal/gi,
  /rationale_internal/gi,
  /\bthe correct answer is\b/gi,
  /\banswer key\b/gi,
];

const FALSE_CREDIT_CLAIMS = [
  /\bclinical[-\s]?hour credit\b/gi,
  /\bcounts? (as|toward|for) clinical hours?\b/gi,
];

export function screenOutput(response: NiaStructuredResponse): NiaStructuredResponse {
  const scrub = (text: string): string => {
    let out = text;
    for (const re of FORBIDDEN_OUTPUT_PHRASES) out = out.replace(re, "[removed]");
    return out;
  };

  const scrubbed: NiaStructuredResponse = {
    ...response,
    directAnswer: scrub(response.directAnswer),
    learnerSummary: scrub(response.learnerSummary),
    nextSteps: response.nextSteps.map(scrub),
    safetyNotes: [...response.safetyNotes],
    citations: response.citations.map((c) => ({ ...c, excerpt: scrub(c.excerpt) })),
  };

  // Never imply certificate production is enabled.
  const combined = `${scrubbed.directAnswer} ${scrubbed.learnerSummary}`.toLowerCase();
  if (/certificate (is|are) (now )?(enabled|issued|available|ready to download|approved)/.test(combined)) {
    scrubbed.safetyNotes = [
      ...scrubbed.safetyNotes,
      "Certificate production remains disabled in this preview until required approvals and gates are complete.",
    ];
  }

  // Guard against false clinical-hour credit claims slipping through.
  for (const re of FALSE_CREDIT_CLAIMS) {
    if (re.test(`${scrubbed.directAnswer} ${scrubbed.learnerSummary}`)) {
      if (!scrubbed.safetyNotes.some((n) => /clinical-hour credit/i.test(n))) {
        scrubbed.safetyNotes = [
          ...scrubbed.safetyNotes,
          "Optional Clinical Support is non-credit and does not count as clinical-hour credit.",
        ];
      }
    }
  }

  return scrubbed;
}
