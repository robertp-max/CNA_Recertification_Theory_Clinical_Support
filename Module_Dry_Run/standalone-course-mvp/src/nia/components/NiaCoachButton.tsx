import { useLocation } from "react-router-dom";
import { Sparkles } from "lucide-react";
import { paths } from "../../app/routes";
import { useUiState } from "../../lib/uiState";
import { NiaCoachDrawer } from "./NiaCoachDrawer";

// Public feature toggle (non-secret). Nia is on by default for the MVP and can
// be disabled with VITE_NIA_ENABLED="false".
function niaEnabled(): boolean {
  return import.meta.env?.VITE_NIA_ENABLED !== "false";
}

export function NiaCoachButton({ onClick }: { onClick: () => void }) {
  const { brandingMode } = useUiState();
  const isDark = brandingMode === "dark";
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label="Open Nia (Nurse Instructor Assistant)"
      className={`fixed bottom-6 right-6 z-50 inline-flex items-center gap-2 border font-bold px-5 py-3 rounded-full transition-all tracking-[0.14em] text-xs uppercase no-print before:absolute before:inset-[-10px] before:rounded-full before:pointer-events-none before:blur-md before:content-[''] after:absolute after:inset-[-18px] after:rounded-full after:pointer-events-none after:content-[''] ${
        isDark
          ? "bg-[#5c1111] hover:bg-[#781616] text-stone-100 border-[#8a1d1d] shadow-lg shadow-black/40 before:bg-amber-400/20 after:border after:border-amber-400/20"
          : "bg-white hover:bg-[#FFF9E8] text-[#8B1515] border-[#8B1515]/25 shadow-xl shadow-[#8B1515]/15 before:bg-amber-300/35 after:border after:border-amber-300/35"
      }`}
    >
      <Sparkles size={16} className={`relative z-10 ${isDark ? "text-amber-300" : "text-amber-500"}`} />
      <span className="relative z-10">Nia</span>
    </button>
  );
}

// Mount: floating button + drawer. Rendered once inside the app shell.
export function NiaCoach() {
  const { pathname } = useLocation();
  const { niaOpen, setNiaOpen } = useUiState();
  const hideOnRoute = pathname === paths.moduleAssessmentQuiz || pathname === paths.finalQuiz;

  if (!niaEnabled()) return null;
  return (
    <>
      {!niaOpen && !hideOnRoute && <NiaCoachButton onClick={() => setNiaOpen(true)} />}
      <div className={hideOnRoute ? "hidden" : ""}>
        <NiaCoachDrawer open={niaOpen} onClose={() => setNiaOpen(false)} />
      </div>
    </>
  );
}
