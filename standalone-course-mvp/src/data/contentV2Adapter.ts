import type { ModuleDef, ModuleLesson, KnowledgeCheck } from "./lessonModel";
import { courseContentV2 } from "./contentV2.generated";

type GeneratedModule = (typeof courseContentV2.modules)[number];
type GeneratedLesson = GeneratedModule["lessons"][number];
type GeneratedQuestion = (typeof courseContentV2.assessments.final_assessment.questions)[number];

function appModuleId(moduleId: string): string {
  return `m${Number(moduleId.slice(1))}`;
}

function appLessonId(lessonId: string): string {
  return `l${Number(lessonId.slice(1))}`;
}

function toKnowledgeCheck(question: GeneratedQuestion | null | undefined): KnowledgeCheck | undefined {
  if (!question) return undefined;
  // NOTE: learner-facing remediation is rendered via the course-extension model
  // in src/data/remediation.ts (Challenge Debrief). These fields are retained
  // only for internal scoring/back-compat and are NOT shown to learners. We do
  // not surface answer-key or internal phrases here.
  return {
    prompt: question.prompt,
    choices: question.choices.map((choice) => ({ id: choice.id, label: choice.label })),
    correctId: question.correct_id_internal,
    feedbackCorrect: "",
    feedbackIncorrect: "",
    remediation: undefined,
  };
}

function firstChallenge(lesson: GeneratedLesson): GeneratedQuestion | undefined {
  return lesson.cards.find((card) => card.card_type === "challenge")?.internal_challenge as GeneratedQuestion | undefined;
}

function toLesson(lesson: GeneratedLesson): ModuleLesson {
  const challenge = firstChallenge(lesson);
  const overview = lesson.cards.find((card) => card.card_type === "overview") ?? lesson.cards[0];
  const delivery = lesson.cards.find((card) => card.card_type === "delivery") ?? overview;
  return {
    id: appLessonId(lesson.lesson_id),
    index: Number(lesson.lesson_id.slice(1)),
    title: lesson.lesson_title,
    estMinutes: lesson.estimated_minutes,
    learningGoal: overview.learning_goal,
    scenario: challenge?.prompt ?? delivery.learner_facing_content.slice(0, 220),
    keyConcept: delivery.learner_facing_content,
    whyItMatters: [...overview.why_it_matters],
    practiceExample: overview.cna_practice_example,
    commonMistake: "Skipping required reporting, scope, no-PHI, or compliance steps.",
    knowledgeCheck: toKnowledgeCheck(challenge),
    keyTerms: overview.key_terms.map((term) => ({ term: term.term, definition: term.definition })),
    transcript: overview.transcript_text,
    summary: overview.learner_facing_content,
    smeFlag: overview.sme_review_flag !== "None identified" ? overview.sme_review_flag : undefined,
  };
}

function toModuleDef(module: GeneratedModule): ModuleDef {
  const n = Number(module.module_id.slice(1));
  return {
    id: appModuleId(module.module_id),
    code: module.module_id.replace(/^M0?/, "M"),
    title: `Module ${n}: ${module.module_title}`,
    shortTitle: module.short_title,
    time: `${(module.estimated_minutes / 60).toFixed(module.estimated_minutes % 60 ? 1 : 0)} hr`,
    summary: module.lessons.map((lesson) => lesson.lesson_title).join("; "),
    kind: module.module_id === "M00" ? "orientation" : module.module_id === "M07" ? "final" : module.status === "source-repair" ? "locked" : "lesson",
    status: module.status === "source-repair" ? "source-repair" : module.status === "sme-review" ? "sme-review" : "ready",
    countsTowardTheory: module.counts_toward_theory && module.status !== "source-repair",
    reviewerNote: [module.source_status_flag, module.sme_review_flag, module.compliance_review_flag].filter(Boolean).join(" "),
    learningObjectives: [...module.learning_objectives],
    lessons: module.module_id === "M00" || module.module_id === "M07" ? [] : module.lessons.map(toLesson),
  };
}

export const contentV2 = courseContentV2;
export const appCopy = courseContentV2.app_copy;
export const contentV2Modules = courseContentV2.modules;
export const courseModules: ModuleDef[] = courseContentV2.modules.map(toModuleDef);

export function getModuleDef(moduleId: string): ModuleDef | undefined {
  return courseModules.find((m) => m.id === moduleId);
}

export function getLessonDef(moduleId: string, lessonId: string) {
  return getModuleDef(moduleId)?.lessons.find((l) => l.id === lessonId);
}

export const requiredTheoryModuleIds = courseModules.filter((m) => m.countsTowardTheory).map((m) => m.id);
export const moduleSequence = courseModules.map((m) => m.id);

export function getGeneratedModule(moduleId: string) {
  const canonical = moduleId.toUpperCase().startsWith("M") && moduleId.length === 3 ? moduleId.toUpperCase() : `M${String(Number(moduleId.replace("m", ""))).padStart(2, "0")}`;
  return courseContentV2.modules.find((m) => m.module_id === canonical);
}

export function getGeneratedLesson(moduleId: string, lessonId: string) {
  const mod = getGeneratedModule(moduleId);
  const canonicalLesson = lessonId.toUpperCase().startsWith("L") && lessonId.length === 3 ? lessonId.toUpperCase() : `L${String(Number(lessonId.replace("l", ""))).padStart(2, "0")}`;
  return mod?.lessons.find((lesson) => lesson.lesson_id === canonicalLesson);
}

export const module1Assessment = courseContentV2.assessments.module_assessments.M01;
export const moduleQuizItems = module1Assessment.questions.map((question) => ({
  id: question.id,
  prompt: question.prompt,
  choices: question.choices.map((choice) => ({ id: choice.id, label: choice.label })),
  correctId: question.correct_id_internal,
}));
export const MODULE_QUIZ_PASS_PCT = module1Assessment.pass_percent ?? 80;
export function scoreModuleQuiz(answers: Record<string, string>): { pct: number; passed: boolean } {
  const correct = moduleQuizItems.filter((q) => answers[q.id] === q.correctId).length;
  const pct = Math.round((correct / moduleQuizItems.length) * 100);
  return { pct, passed: pct >= MODULE_QUIZ_PASS_PCT };
}

export type ExamItem = {
  id: string;
  moduleCode: string;
  prompt: string;
  choices: { id: string; label: string }[];
  correctId: string;
};

function moduleCodeFromQuestionId(id: string): string {
  const raw = courseContentV2.assessments.final_assessment.questions.find((q) => q.id === id);
  const match = raw?.source_reference.match(/Module\s+(\d+)/i);
  return match ? `M${match[1]}` : "M";
}

export const EXAM = {
  ATTEMPT_SIZE: courseContentV2.assessments.final_assessment.attempt_size,
  PASS_PCT: courseContentV2.assessments.final_assessment.pass_percent,
  NOTICE: courseContentV2.assessments.final_assessment.answer_key_policy,
};

export const examPool: ExamItem[] = courseContentV2.assessments.final_assessment.questions.map((question) => ({
  id: question.id,
  moduleCode: moduleCodeFromQuestionId(question.id),
  prompt: question.prompt,
  choices: question.choices.map((choice) => ({ id: choice.id, label: choice.label })),
  correctId: question.correct_id_internal,
}));

export function drawAttempt(size = EXAM.ATTEMPT_SIZE, seed = Date.now()): ExamItem[] {
  const arr = [...examPool];
  let s = seed % 2147483647;
  const rand = () => (s = (s * 48271) % 2147483647) / 2147483647;
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr.slice(0, Math.min(size, arr.length));
}

export function scoreAttempt(items: ExamItem[], answers: Record<string, string>) {
  const correct = items.filter((it) => answers[it.id] === it.correctId).length;
  const pct = items.length ? Math.round((correct / items.length) * 100) : 0;
  return { correct, total: items.length, pct, passed: pct >= EXAM.PASS_PCT };
}
