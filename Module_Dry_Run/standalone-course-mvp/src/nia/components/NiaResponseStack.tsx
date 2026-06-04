import { AlertTriangle, ArrowRight, ListChecks, ShieldAlert, Sparkles } from "lucide-react";
import type { NiaAction, NiaActionType, NiaLinkedReference, NiaStructuredResponse } from "../types";
import { resolveNiaActionRoute } from "../niaActions";
import { NiaCitationCards } from "./NiaCitationCards";
import { NiaReferencePreview } from "./NiaReferencePreview";

const INFORMATIONAL_ACTIONS: NiaActionType[] = [
  "show_no_phi_guidance",
  "show_scope_guidance",
  "review_key_terms",
];

function isInformational(type: NiaActionType): boolean {
  return INFORMATIONAL_ACTIONS.includes(type);
}

const CONFIDENCE_LABEL: Record<NiaStructuredResponse["confidence"], string> = {
  high: "High confidence",
  medium: "Medium confidence",
  low: "Low confidence",
};

export function NiaResponseStack({
  response,
  onAction,
  onOpenReference,
}: {
  response: NiaStructuredResponse;
  onAction: (action: NiaAction) => void;
  onOpenReference: (reference: NiaLinkedReference) => void;
}) {
  const blocked = Boolean(response.blockedReason);

  return (
    <div className="space-y-4">
      {/* Direct answer */}
      <div
        className={
          blocked
            ? "bg-[#1a0f0f] border border-red-900/50 rounded-lg p-4"
            : "bg-[#120909] border border-stone-800 rounded-lg p-4"
        }
      >
        <div className="flex items-center gap-1.5 text-[9px] font-mono uppercase tracking-wider text-stone-500 mb-2">
          {blocked ? <ShieldAlert size={11} className="text-red-400" /> : <Sparkles size={11} className="text-amber-400" />}
          {blocked ? "Safety boundary" : "Nia"} · {CONFIDENCE_LABEL[response.confidence]}
        </div>
        <p className={blocked ? "text-sm text-red-100 leading-relaxed" : "text-sm text-stone-100 leading-relaxed"}>
          {response.directAnswer}
        </p>
        {response.learnerSummary && (
          <p className="text-xs text-stone-400 leading-relaxed mt-2">{response.learnerSummary}</p>
        )}
      </div>

      {/* Next steps */}
      {response.nextSteps.length > 0 && (
        <div className="bg-[#0c0606] border border-stone-800/80 rounded-lg p-3">
          <div className="flex items-center gap-1.5 text-[9px] font-mono uppercase tracking-wider text-amber-500/80 mb-2">
            <ListChecks size={11} /> Next steps
          </div>
          <ul className="space-y-1.5">
            {response.nextSteps.map((step, i) => (
              <li key={i} className="flex gap-2 text-xs text-stone-300">
                <ArrowRight size={12} className="text-amber-500/70 shrink-0 mt-0.5" />
                <span>{step}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Scope reminder */}
      {response.scopeReminder && (
        <div className="bg-[#0c0606] border border-amber-500/20 rounded-lg p-3 text-xs text-amber-200/90 leading-relaxed">
          <span className="font-semibold">CNA scope: </span>
          {response.scopeReminder}
        </div>
      )}

      {/* Safety notes */}
      {response.safetyNotes.length > 0 && (
        <div className="space-y-1.5">
          {response.safetyNotes.map((note, i) => (
            <div key={i} className="flex gap-2 text-[11px] text-stone-400">
              <AlertTriangle size={11} className="text-amber-500/70 shrink-0 mt-0.5" />
              <span>{note}</span>
            </div>
          ))}
        </div>
      )}

      {/* Available actions */}
      {response.availableActions.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {response.availableActions.map((action) => {
            const informational = isInformational(action.type);
            const route = resolveNiaActionRoute(action);
            const disabled = !informational && route === null;
            const primary = action.priority === "primary" && !disabled;
            return (
              <button
                key={action.id}
                type="button"
                disabled={disabled}
                onClick={() => onAction(action)}
                title={disabled ? "Coming soon — no route available yet" : undefined}
                className={
                  "inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-[11px] font-semibold uppercase tracking-wider transition-colors " +
                  (disabled
                    ? "bg-stone-950 text-stone-600 border border-stone-900 cursor-not-allowed"
                    : primary
                      ? "bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d]"
                      : "bg-stone-900 hover:bg-stone-800 text-stone-300 border border-stone-800")
                }
              >
                {action.label}
                {disabled && <span className="text-[8px] normal-case tracking-normal">(soon)</span>}
              </button>
            );
          })}
        </div>
      )}

      {/* Citations */}
      <NiaCitationCards citations={response.citations} />

      {/* Linked references with open affordance */}
      {response.linkedReferences.length > 0 && (
        <div className="space-y-2">
          <div className="text-[9px] font-mono uppercase tracking-wider text-stone-500">Reference preview</div>
          {response.linkedReferences.map((ref) => {
            const canOpen = canOpenReference(ref);
            return (
              <NiaReferencePreview
                key={ref.id}
                reference={ref}
                canOpen={canOpen}
                onOpen={onOpenReference}
              />
            );
          })}
        </div>
      )}
    </div>
  );
}

// A reference is openable when it maps to an existing route.
function canOpenReference(ref: NiaLinkedReference): boolean {
  if (ref.type === "module") return ref.moduleId === "m0" || ref.moduleId === "m1" || ref.moduleId !== undefined;
  if (ref.type === "lesson") return ref.moduleId === "m1";
  if (ref.type === "clinical_support") return true;
  if (ref.type === "certificate_gate") return true;
  return false;
}
