// Best-effort course context snapshot for Nia. Pure + framework-agnostic so the
// deterministic provider and tests can use it without React. The UI passes the
// current route and the persisted LearnerState; everything unknown stays null
// (never fabricated).

import type { LearnerState } from "../lib/learnerState";
import { summarizeGates } from "../lib/gates";
import { isModuleComplete, requiredTheoryComplete } from "../lib/moduleProgress";
import { courseModules, requiredTheoryModuleIds, contentV2 } from "../data/contentV2Adapter";
import type { NiaContextSnapshot } from "./types";

export interface NiaContextInput {
  route?: string | null;
  moduleId?: string | null;
  lessonId?: string | null;
  cardId?: string | null;
  learnerState?: LearnerState | null;
}

function viewNameForRoute(route: string | null): string | null {
  if (!route) return null;
  if (route.startsWith("/dashboard")) return "Dashboard";
  if (route.startsWith("/final")) return "Final Assessment";
  if (route.startsWith("/modules")) return "CE Modules";
  if (route.startsWith("/certificate")) return "Certificate Gate";
  if (route.startsWith("/clinical")) return "Clinical Hub";
  return null;
}

function moduleFromRoute(route: string | null): string | null {
  if (!route) return null;
  const match = route.match(/\/modules\/(m\d+)/i);
  return match ? match[1].toLowerCase() : null;
}

export function buildNiaContext(input: NiaContextInput): NiaContextSnapshot {
  const route = input.route ?? null;
  const learner = input.learnerState ?? null;

  const minutes =
    (contentV2 as unknown as { control_facts?: { theory_total_minutes?: number } }).control_facts
      ?.theory_total_minutes ?? 720;

  let completedRequiredModuleIds: string[] | null = null;
  let nextIncompleteModuleId: string | null = null;
  let nextIncompleteModuleTitle: string | null = null;
  let theoryComplete: boolean | null = null;

  if (learner) {
    completedRequiredModuleIds = requiredTheoryModuleIds.filter((id) => isModuleComplete(learner, id));
    theoryComplete = requiredTheoryComplete(learner);
    const nextId = requiredTheoryModuleIds.find((id) => !isModuleComplete(learner, id)) ?? null;
    nextIncompleteModuleId = nextId;
    nextIncompleteModuleTitle = nextId ? courseModules.find((m) => m.id === nextId)?.title ?? null : null;
  }

  let gate: NiaContextSnapshot["certificateGate"] = {
    productionIssuable: null,
    previewReady: null,
    blockerLabels: null,
  };
  let finalExam: NiaContextSnapshot["finalExam"] = {
    attempted: null,
    passed: null,
    bestScorePct: null,
  };

  if (learner) {
    const summary = summarizeGates(learner);
    gate = {
      productionIssuable: summary.productionIssuable,
      previewReady: summary.certificatePreviewReady,
      blockerLabels: summary.blockers.map((b) => b.label),
    };
    finalExam = {
      attempted: learner.finalExamAttempted,
      passed: learner.finalExamPassed,
      bestScorePct: learner.finalExamBestScorePct,
    };
  }

  return {
    route,
    activeView: viewNameForRoute(route),
    currentModuleId: input.moduleId ?? moduleFromRoute(route),
    currentLessonId: input.lessonId ?? null,
    currentCardId: input.cardId ?? null,
    progress: {
      requiredTheoryComplete: theoryComplete,
      completedRequiredModuleIds,
      nextIncompleteModuleId,
      nextIncompleteModuleTitle,
    },
    certificateGate: gate,
    finalExam,
    clinicalHub: {
      available: true,
      appLocation: "clinical.hub.overview",
    },
    courseCounts: {
      requiredTheoryMinutes: minutes,
      requiredTheoryHours: Math.round((minutes / 60) * 10) / 10,
      moduleCount: courseModules.length,
    },
  };
}
