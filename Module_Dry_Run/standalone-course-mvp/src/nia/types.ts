// Nia (Nurse Instructor Assistant) — structured response contract.
//
// Nia is a course-grounded learner-support assistant for the standalone CNA
// recertification theory app. It is NOT "Brad", NOT "iAdministrator", NOT a
// surveyor/enforcement engine, and NOT a licensed clinician, evaluator,
// certifying authority, legal advisor, CDPH representative, or instructor of
// record. All contracts here are learner-oriented and grounded in ContentV2.

export type NiaIntent =
  | "course_navigation"
  | "lesson_explanation"
  | "module_summary"
  | "quiz_readiness"
  | "final_exam_readiness"
  | "certificate_gate"
  | "clinical_support"
  | "scope_safety"
  | "phi_safety"
  | "technical_help"
  | "general_course_question"
  | "out_of_scope";

export type NiaReferenceType =
  | "module"
  | "lesson"
  | "card"
  | "assessment"
  | "clinical_support"
  | "certificate_gate"
  | "course_policy"
  | "app_help";

export interface NiaCitation {
  id: string;
  referenceId: string;
  referenceType: NiaReferenceType;
  title: string;
  locationLabel: string;
  appLocation?: string;
  excerpt: string;
  relevance: "primary" | "secondary";
}

export interface NiaLinkedReference {
  id: string;
  type: NiaReferenceType;
  title: string;
  description: string;
  appLocation?: string;
  moduleId?: string;
  lessonId?: string;
  cardId?: string;
  required?: boolean;
}

export type NiaActionType =
  | "open_module"
  | "open_lesson"
  | "open_card"
  | "open_clinical_hub"
  | "open_certificate_gate"
  | "review_key_terms"
  | "practice_quiz_readiness"
  | "show_no_phi_guidance"
  | "show_scope_guidance";

export interface NiaAction {
  id: string;
  label: string;
  type: NiaActionType;
  targetId?: string;
  appLocation?: string;
  priority: "primary" | "secondary";
}

export type NiaBlockedReason = "phi" | "final_exam_key" | "clinical_advice" | "out_of_scope";

export type NiaProviderId = "deterministic" | "external";

export interface NiaStructuredResponse {
  id: string;
  intent: NiaIntent;
  directAnswer: string;
  learnerSummary: string;
  nextSteps: string[];
  safetyNotes: string[];
  scopeReminder?: string;
  confidence: "high" | "medium" | "low";
  citations: NiaCitation[];
  linkedReferences: NiaLinkedReference[];
  availableActions: NiaAction[];
  noAnswerFound: boolean;
  noAnswerReason?: string;
  blockedReason?: NiaBlockedReason;
  meta: {
    elapsedMs: number;
    provider: NiaProviderId;
    retrievedReferenceIds: string[];
    currentCourseLocation?: string;
  };
}

export interface NiaQueryRequest {
  input: string;
  currentRoute?: string;
  currentModuleId?: string;
  currentLessonId?: string;
  currentCardId?: string;
  learnerProgressSnapshot?: unknown;
  certificateGateSnapshot?: unknown;
}

// ---- Index record (built from ContentV2 — see niaIndex.ts) ----
export interface NiaIndexRecord {
  id: string;
  type: NiaReferenceType;
  title: string;
  body: string;
  keywords: string[];
  appLocation?: string;
  moduleId?: string;
  moduleTitle?: string;
  lessonId?: string;
  lessonTitle?: string;
  cardId?: string;
  sourceReference?: string;
  status?: string;
  safetyFlags?: string[];
}

// ---- Context snapshot (see niaContext.ts) ----
export interface NiaContextSnapshot {
  route: string | null;
  activeView: string | null;
  currentModuleId: string | null;
  currentLessonId: string | null;
  currentCardId: string | null;
  // Best-effort progress; null when unknown — never fabricated.
  progress: {
    requiredTheoryComplete: boolean | null;
    completedRequiredModuleIds: string[] | null;
    nextIncompleteModuleId: string | null;
    nextIncompleteModuleTitle: string | null;
  };
  certificateGate: {
    productionIssuable: boolean | null;
    previewReady: boolean | null;
    blockerLabels: string[] | null;
  };
  finalExam: {
    attempted: boolean | null;
    passed: boolean | null;
    bestScorePct: number | null;
  };
  clinicalHub: {
    available: boolean;
    appLocation: string | null;
  };
  courseCounts: {
    requiredTheoryMinutes: number;
    requiredTheoryHours: number;
    moduleCount: number;
  };
}

// ---- Guardrail result (see niaGuardrails.ts) ----
export interface NiaGuardrailResult {
  blocked: boolean;
  blockedReason?: NiaBlockedReason;
  // Learner-safe message to surface when blocked.
  message?: string;
  // Detected signals (for status/debugging surfaces — not shown to learner).
  signals: string[];
}

// ---- Provider boundary ----
export interface NiaProviderRequest {
  request: NiaQueryRequest;
  intent: NiaIntent;
  records: NiaIndexRecord[];
  context: NiaContextSnapshot;
  guardrail: NiaGuardrailResult;
  startedAt: number;
}

export interface NiaProvider {
  providerId: NiaProviderId;
  generate(request: NiaProviderRequest): Promise<NiaStructuredResponse>;
}

// ---- Health / status surface ----
export interface NiaHealthStatus {
  ok: boolean;
  provider: NiaProviderId;
  externalEnabled: boolean;
  indexRecordCount: number;
  builtAt: string;
  notes: string[];
}
