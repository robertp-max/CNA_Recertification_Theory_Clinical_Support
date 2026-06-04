// Nia action helpers + safe route resolution. Nia actions are advisory: when a
// concrete route does not exist for an action, the UI renders a disabled
// "Coming soon" affordance instead of breaking.

import { paths } from "../app/routes";
import type { NiaAction, NiaActionType } from "./types";

export type NiaAppRoutes = typeof paths;

let counter = 0;
function nextActionId(type: NiaActionType): string {
  counter += 1;
  return `act-${type}-${counter}`;
}

export function makeAction(
  type: NiaActionType,
  label: string,
  opts: { targetId?: string; appLocation?: string; priority?: "primary" | "secondary" } = {},
): NiaAction {
  return {
    id: nextActionId(type),
    label,
    type,
    targetId: opts.targetId,
    appLocation: opts.appLocation,
    priority: opts.priority ?? "secondary",
  };
}

// Resolve an action to a concrete in-app route, or null if no route exists yet.
// Only m0 and m1 (plus the m1 lesson player) have dedicated routes today; other
// modules resolve to the CE Modules list rather than a dead link.
export function resolveNiaActionRoute(action: NiaAction, routes: NiaAppRoutes = paths): string | null {
  switch (action.type) {
    case "open_module": {
      if (action.targetId === "m0") return routes.module0;
      if (action.targetId === "m1") return routes.module1;
      return routes.modules;
    }
    case "open_lesson":
      // Only the Module 1 lesson player route exists in the current app.
      return action.targetId === "m1" ? routes.lesson : null;
    case "open_card":
      // No dedicated card route in the current app.
      return null;
    case "open_clinical_hub":
      return routes.clinicalHub;
    case "open_certificate_gate":
      return routes.certificate;
    case "practice_quiz_readiness":
      return routes.modules;
    case "review_key_terms":
    case "show_no_phi_guidance":
    case "show_scope_guidance":
      // Handled inline in the drawer (informational), no navigation.
      return null;
    default:
      return null;
  }
}
