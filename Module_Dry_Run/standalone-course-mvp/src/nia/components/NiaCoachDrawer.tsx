import { useCallback, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { HelpCircle, MessageCircle, X } from "lucide-react";
import { useLearner } from "../../lib/learnerState";
import { buildNiaContext } from "../niaContext";
import { askNia } from "../niaClient";
import { resolveNiaActionRoute } from "../niaActions";
import type { NiaAction, NiaLinkedReference, NiaStructuredResponse } from "../types";
import { NiaCommandBar } from "./NiaCommandBar";
import { NiaResponseStack } from "./NiaResponseStack";
import { NiaHelpCenter } from "./NiaHelpCenter";
import { NiaStatusBadge } from "./NiaStatusBadge";
import { useUiState } from "../../lib/uiState";

interface Turn {
  id: string;
  question: string;
  response: NiaStructuredResponse;
}

function informationalPrompt(action: NiaAction): string | null {
  switch (action.type) {
    case "show_no_phi_guidance":
      return "What does no PHI mean in this course?";
    case "show_scope_guidance":
      return "What is CNA scope?";
    case "review_key_terms":
      return action.targetId ? `What are the key terms for ${action.targetId}?` : "Show me key terms to review";
    default:
      return null;
  }
}

function routeForReference(ref: NiaLinkedReference): string | null {
  if (ref.type === "module") {
    return resolveNiaActionRoute({ id: "x", label: "", type: "open_module", targetId: ref.moduleId, priority: "secondary" });
  }
  if (ref.type === "lesson") {
    return resolveNiaActionRoute({ id: "x", label: "", type: "open_lesson", targetId: ref.moduleId, priority: "secondary" });
  }
  if (ref.type === "clinical_support") {
    return resolveNiaActionRoute({ id: "x", label: "", type: "open_clinical_hub", priority: "secondary" });
  }
  if (ref.type === "certificate_gate") {
    return resolveNiaActionRoute({ id: "x", label: "", type: "open_certificate_gate", priority: "secondary" });
  }
  return null;
}

export function NiaCoachDrawer({ open, onClose }: { open: boolean; onClose: () => void }) {
  const { state } = useLearner();
  const { brandingMode } = useUiState();
  const isDark = brandingMode === "dark";
  const location = useLocation();
  const navigate = useNavigate();
  const [turns, setTurns] = useState<Turn[]>([]);
  const [busy, setBusy] = useState(false);
  const [showHelp, setShowHelp] = useState(false);

  const runQuery = useCallback(
    async (input: string) => {
      setBusy(true);
      try {
        const context = buildNiaContext({ route: location.pathname, learnerState: state });
        const response = await askNia({ input, currentRoute: location.pathname }, context);
        setTurns((prev) => [...prev, { id: response.id, question: input, response }]);
      } finally {
        setBusy(false);
      }
    },
    [location.pathname, state],
  );

  const handleAction = useCallback(
    (action: NiaAction) => {
      const prompt = informationalPrompt(action);
      if (prompt) {
        void runQuery(prompt);
        return;
      }
      const route = resolveNiaActionRoute(action);
      if (route) {
        navigate(route);
      }
    },
    [navigate, runQuery],
  );

  const handleOpenReference = useCallback(
    (ref: NiaLinkedReference) => {
      const route = routeForReference(ref);
      if (route) {
        navigate(route);
      }
    },
    [navigate],
  );

  if (!open) return null;

  return (
    <aside
      aria-label="Nia (Nurse Instructor Assistant)"
      className="fixed inset-x-3 bottom-3 top-auto z-50 w-auto sm:inset-x-auto sm:right-6 sm:bottom-6 sm:w-[390px] no-print"
    >
      <div className={`max-h-[calc(100vh-1.5rem)] sm:max-h-[calc(100vh-3rem)] border rounded-2xl shadow-2xl flex flex-col overflow-hidden ${
        isDark ? "bg-[#0c0606] border-stone-800 shadow-black/50" : "bg-white border-stone-200 shadow-stone-900/15"
      }`}>
        {/* Header */}
        <header className={`border-b p-4 ${isDark ? "border-stone-800 bg-[#120909]" : "border-stone-200 bg-[#FBF9F9]"}`}>
          <div className="flex items-start justify-between gap-3">
            <div className="flex items-center gap-2 min-w-0">
              <div className={`w-8 h-8 rounded-lg border flex items-center justify-center shrink-0 ${
                isDark ? "bg-[#5c1111] border-[#8a1d1d]" : "bg-[#8B1515] border-[#8B1515]"
              }`}>
                <MessageCircle size={16} className="text-white" />
              </div>
              <div className="min-w-0">
                <h2 className={`text-sm font-bold ${isDark ? "text-stone-100" : "text-stone-900"}`}>Nia (Nurse Instructor Assistant)</h2>
                <p className="text-[10px] text-stone-500">Course Guidance · CNA Recertification · Grounded Answers Only</p>
              </div>
            </div>
            <button
              type="button"
              onClick={onClose}
              className={`p-1 shrink-0 transition-colors ${isDark ? "text-stone-500 hover:text-stone-100" : "text-stone-500 hover:text-stone-900"}`}
              aria-label="Close Nia"
            >
              <X size={18} />
            </button>
          </div>
          <div className="flex items-center justify-between mt-3 gap-3">
            <NiaStatusBadge />
            <button
              type="button"
              onClick={() => setShowHelp((v) => !v)}
              className={`inline-flex items-center gap-1 text-[10px] font-semibold uppercase tracking-wider shrink-0 transition-colors ${isDark ? "text-stone-400 hover:text-stone-100" : "text-stone-600 hover:text-[#8B1515]"}`}
            >
              <HelpCircle size={12} /> {showHelp ? "Hide help" : "Help Center"}
            </button>
          </div>
        </header>

        {/* Body */}
        <div className="flex-1 overflow-y-auto p-4 space-y-5 min-h-[320px] max-h-[55vh] sm:min-h-[420px] sm:max-h-[calc(100vh-17rem)]">
          {showHelp && <NiaHelpCenter />}

          {turns.length === 0 && !showHelp && (
            <div className={`text-xs leading-relaxed border rounded-xl p-4 ${isDark ? "text-stone-400 bg-[#120909] border-stone-800" : "text-stone-700 bg-stone-50 border-stone-200"}`}>
              Hi — I'm Nia. I answer questions using this course's content only. Ask me what to do next, what a module
              covers, why your certificate is locked, how to study for the final, or about CNA scope and the no-PHI rules.
            </div>
          )}

          {turns.map((turn) => (
            <div key={turn.id} className="space-y-3">
              <div className="text-right">
                <span className={`inline-block border text-xs rounded-xl px-3 py-1.5 max-w-[85%] text-left ${
                  isDark ? "bg-[#5c1111]/40 border-[#8a1d1d]/40 text-stone-200" : "bg-[#8B1515]/10 border-[#8B1515]/20 text-stone-900"
                }`}>
                  {turn.question}
                </span>
              </div>
              <NiaResponseStack response={turn.response} onAction={handleAction} onOpenReference={handleOpenReference} />
            </div>
          ))}

          {busy && <div className="text-xs text-stone-500 animate-pulse">Nia is checking the course content…</div>}
        </div>

        {/* Command input */}
        <div className={`border-t p-4 ${isDark ? "border-stone-800 bg-[#120909]" : "border-stone-200 bg-[#FBF9F9]"}`}>
          <NiaCommandBar onSubmit={(input) => void runQuery(input)} busy={busy} />
        </div>
      </div>
    </aside>
  );
}
