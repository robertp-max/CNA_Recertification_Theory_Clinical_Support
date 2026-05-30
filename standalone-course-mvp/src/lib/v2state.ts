// Adapters that map the V2 prototype's simplified state concepts onto the
// canonical, persisted LearnerState (single source of truth). No new gating
// state is introduced — these are derived getters plus typed mutators that
// write into LearnerState via the existing reducer helpers.

import type { LearnerState } from "./learnerState";
import { passAllRequiredState } from "./learnerState";
import { completeAllRequiredLessons } from "./moduleProgress";

export const M1_ID = "m1";
export const M1_LESSON_ID = "l1";
const M1_LESSON_KEY = `${M1_ID}:${M1_LESSON_ID}`;

/** Module 0 orientation complete (identity + all three acknowledgements). */
export function module0Complete(state: LearnerState): boolean {
  return Boolean(
    state.legalFirstName.trim() &&
      state.legalLastName.trim() &&
      state.cnaNumber.trim() &&
      state.orientationFinalAck &&
      state.phiAck &&
      state.onlineCapAck,
  );
}

/** Module 1 Lesson 1 (the 4-card lesson) viewed + practice challenge submitted. */
export function lessonCompleted(state: LearnerState): boolean {
  const p = state.lessonProgress[M1_LESSON_KEY];
  return Boolean(p?.viewed && p?.checkPassed);
}

export function moduleAssessmentPassed(state: LearnerState): boolean {
  return state.moduleQuizPassed[M1_ID] === true;
}

/** Mark the Module 1 lesson complete and write real active-time for that lesson. */
export function withLessonCompleted(state: LearnerState): LearnerState {
  const now = new Date().toISOString();
  return {
    ...state,
    lessonProgress: {
      ...state.lessonProgress,
      [M1_LESSON_KEY]: { viewed: true, checkPassed: true, completedAt: now },
    },
    lessonActiveSeconds: {
      ...state.lessonActiveSeconds,
      [M1_LESSON_KEY]: Math.max(state.lessonActiveSeconds[M1_LESSON_KEY] || 0, 20),
    },
  };
}

export function withLessonReset(state: LearnerState): LearnerState {
  const lessonProgress = { ...state.lessonProgress };
  delete lessonProgress[M1_LESSON_KEY];
  return { ...state, lessonProgress };
}

export function withModuleAssessment(state: LearnerState, passed: boolean): LearnerState {
  return { ...state, moduleQuizPassed: { ...state.moduleQuizPassed, [M1_ID]: passed } };
}

/** Reviewer "Unlock All": drive every certificate gate + V2 milestone to ready. */
export function withEverythingUnlocked(state: LearnerState): LearnerState {
  const base = completeAllRequiredLessons(passAllRequiredState(state));
  return withLessonCompleted(withModuleAssessment(base, true));
}
