import { useNavigate } from "react-router-dom";
import { CheckCircle2, Lock, Shield } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { requiredProgressPct } from "../lib/progress";
import { isModuleComplete, isModuleUnlocked, moduleProgressPct, requiredTheoryComplete } from "../lib/moduleProgress";
import { useUiState } from "../lib/uiState";
import { paths } from "../app/routes";
import { StatusBadge } from "../components/v2/primitives";
import { courseModules } from "../data/courseModules";
import type { ModuleDef } from "../data/lessonModel";

function routeForModule(module: ModuleDef): string | null {
  if (module.id === "m0") return paths.module0;
  if (module.kind === "lesson") return paths.module(module.id);
  return paths.module(module.id);
}

function badgeForModule(module: ModuleDef, complete: boolean, unlocked: boolean) {
  if (complete) return <StatusBadge tone="complete">Complete</StatusBadge>;
  if (module.status === "source-repair") return <StatusBadge tone="remediation">Source Repair</StatusBadge>;
  if (!unlocked) return <StatusBadge tone="locked">Sequential Lock</StatusBadge>;
  if (module.status === "sme-review") return <StatusBadge tone="action">SME Review</StatusBadge>;
  return <StatusBadge tone="pending">ContentV2 Loaded</StatusBadge>;
}

export function ModulesPage() {
  const navigate = useNavigate();
  const { state } = useLearner();
  const { brandingMode } = useUiState();
  const isDark = brandingMode === "dark";

  const theoryDone = requiredTheoryComplete(state);
  const finalPassed = state.finalExamPassed;
  const progress = requiredProgressPct(state);
  const styles = {
    sideCard: isDark ? "bg-[#120909] border-stone-800/80" : "bg-white border-stone-200 shadow-sm",
    title: isDark ? "text-stone-100" : "text-stone-900",
    body: isDark ? "text-stone-400" : "text-stone-600",
    muted: isDark ? "text-stone-500" : "text-stone-500",
    divider: isDark ? "border-stone-800/80" : "border-stone-200",
    value: isDark ? "text-stone-200" : "text-stone-800",
    accentText: isDark ? "text-amber-500" : "text-[#8B1515]",
    progressTrack: isDark ? "bg-stone-900" : "bg-stone-200",
    progressFill: isDark ? "bg-amber-500" : "bg-[#8B1515]",
    secondaryButton: isDark
      ? "bg-stone-900 hover:bg-stone-850 border-stone-800 text-stone-200"
      : "bg-white hover:bg-stone-50 border-stone-300 text-stone-700",
    primaryButton: isDark
      ? "bg-[#5c1111] text-stone-100 hover:bg-[#781616]"
      : "bg-[#8B1515] text-white hover:bg-[#741111]",
    openCard: isDark ? "bg-[#120909] border-stone-800/80 hover:border-stone-700/80" : "bg-white border-stone-200 hover:border-[#8B1515]/25 shadow-sm",
    lockedCard: isDark ? "bg-[#0a0505]/60 border-stone-950 opacity-75" : "bg-stone-50 border-stone-200 opacity-90",
    cardDivider: isDark ? "border-stone-900" : "border-stone-200",
  };

  return (
    <div className="flex flex-col lg:flex-row gap-8">
      <div className="w-full lg:w-80 shrink-0">
        <div className={`border rounded-xl p-6 lg:sticky lg:top-8 ${styles.sideCard}`}>
          <div className={`text-[10px] uppercase tracking-widest font-bold mb-3 flex items-center gap-1.5 ${styles.accentText}`}>
            <Shield size={12} /> Theory CE Requirements
          </div>
          <h2 className={`text-2xl font-normal mb-3 leading-tight ${styles.title}`}>Curriculum</h2>
          <p className={`text-xs mb-6 leading-relaxed ${styles.body}`}>
            ContentV2 supplies the complete 720-minute required theory package across NATP Modules 10-17.
          </p>

          <div className={`space-y-2 mb-6 border-t pt-4 ${styles.divider}`}>
            <div className={`flex justify-between text-[11px] ${styles.body}`}>
              <span>Legal Name</span>
              <span className={`font-mono ${styles.value}`}>{state.legalFirstName} {state.legalLastName}</span>
            </div>
            <div className={`flex justify-between text-[11px] ${styles.body}`}>
              <span>CNA Certificate #</span>
              <span className={`font-mono ${styles.value}`}>{state.cnaNumber || "-"}</span>
            </div>
          </div>

          <div className="space-y-2 mb-6">
            <div className="flex justify-between text-[11px] font-semibold">
              <span className={isDark ? "text-stone-300" : "text-stone-700"}>Required Progress</span>
              <span className={`font-mono ${styles.accentText}`}>{progress}%</span>
            </div>
            <div className={`w-full h-1 rounded-full overflow-hidden ${styles.progressTrack}`}>
              <div className={`h-full transition-all ${styles.progressFill}`} style={{ width: `${progress}%` }} />
            </div>
          </div>

          <button
            onClick={() => navigate(paths.certificate)}
            className={`w-full py-2.5 rounded border font-semibold text-xs uppercase tracking-wider transition-colors ${styles.secondaryButton}`}
          >
            Review Gate Checklist
          </button>
        </div>
      </div>

      <div className="flex-1 space-y-6">
        <div>
          <h2 className={`text-2xl font-normal mb-1 ${styles.title}`}>Theory Recertification Modules</h2>
          <p className={`text-xs ${styles.body}`}>ContentV2 data is loaded for Orientation plus NATP Modules 10 through 17.</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {courseModules.map((module) => {
            const route = routeForModule(module);
            const complete = isModuleComplete(state, module.id);
            const unlocked = isModuleUnlocked(state, module.id);
            const pct = moduleProgressPct(state, module.id);
            const isRouteReady = Boolean(route) && (unlocked || state.unlockMode || module.id === "m0");
            const canOpenFinal = false;

            return (
              <div
                key={module.id}
                className={`p-5 rounded-xl border transition-all flex flex-col justify-between ${
                  unlocked || module.id === "m0"
                    ? styles.openCard
                    : styles.lockedCard
                }`}
              >
                <div>
                  <div className="flex items-center justify-between mb-3">
                    <span className={`text-[10px] font-bold uppercase tracking-wider font-mono ${styles.accentText}`}>{module.code}</span>
                    <span className={`text-[10px] font-mono ${styles.muted}`}>{module.time}</span>
                  </div>
                  <h3 className={`text-base font-semibold mb-2 ${isDark ? "text-stone-200" : "text-stone-800"}`}>{module.shortTitle}</h3>
                  <p className={`text-xs leading-relaxed mb-4 line-clamp-3 ${styles.body}`}>{module.summary}</p>
                  {module.reviewerNote && (
                    <p className={`text-[10px] font-mono leading-relaxed mb-4 line-clamp-2 ${styles.muted}`}>{module.reviewerNote}</p>
                  )}
                </div>

                <div className={`space-y-3 pt-3 border-t ${styles.cardDivider}`}>
                  <div className="flex items-center justify-between gap-3">
                    {badgeForModule(module, complete, unlocked)}
                    <span className={`text-[10px] font-mono ${styles.muted}`}>{pct}%</span>
                  </div>
                  <div className={`w-full h-1 rounded-full overflow-hidden ${styles.progressTrack}`}>
                    <div className={`h-full transition-all ${styles.progressFill}`} style={{ width: `${pct}%` }} />
                  </div>
                  {route && (isRouteReady || canOpenFinal) ? (
                    <button
                      onClick={() => navigate(route)}
                      className={`w-full px-3 py-1.5 rounded text-xs transition-colors font-semibold ${styles.primaryButton}`}
                    >
                      {complete ? "Review" : "Open Module"}
                    </button>
                  ) : (
                    <div className={`flex items-center justify-between text-[10px] font-mono ${isDark ? "text-stone-600" : "text-stone-500"}`}>
                      <span className="inline-flex items-center gap-1">
                        <Lock size={10} /> {unlocked ? "Route Pending" : "Locked"}
                      </span>
                      <span className="inline-flex items-center gap-1">
                        <CheckCircle2 size={10} /> ContentV2 Data Loaded
                      </span>
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>

        <div className={`p-6 rounded-xl border transition-all ${
          theoryDone
            ? isDark
              ? "bg-[#1c0808] border-[#5c1111]/80"
              : "bg-[#8B1515]/5 border-[#8B1515]/25"
            : isDark
              ? "bg-stone-950/20 border-stone-900/60 opacity-75"
              : "bg-white border-stone-200 opacity-90 shadow-sm"
        }`}>
          <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
            <div>
              <div className={`inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-[10px] font-bold tracking-widest uppercase border mb-3 font-mono ${
                isDark ? "text-amber-500 bg-amber-950/40 border-amber-500/20" : "text-[#8B1515] bg-[#8B1515]/5 border-[#8B1515]/20"
              }`}>
                Course-Wide Final Examination
              </div>
              <h3 className={`text-lg font-semibold mb-2 ${isDark ? "text-stone-200" : "text-stone-800"}`}>Theory Final Assessment Gate</h3>
              <p className={`text-xs max-w-xl leading-relaxed ${styles.body}`}>
                ContentV2 includes the 50-question final pool. The learner-facing result never exposes the full answer key.
              </p>
            </div>
            <div className="shrink-0">
              {finalPassed ? (
                <StatusBadge tone="complete">Passed</StatusBadge>
              ) : theoryDone ? (
                <button onClick={() => navigate(paths.finalSplash)} className={`border font-semibold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors ${
                  isDark ? "bg-[#5c1111] hover:bg-[#781616] text-stone-100 border-[#8a1d1d]" : "bg-[#8B1515] hover:bg-[#741111] text-white border-[#8B1515]"
                }`}>
                  Enter Final Assessment
                </button>
              ) : (
                <div className={`flex items-center gap-2 border px-4 py-2 rounded text-xs font-semibold font-mono ${
                  isDark ? "bg-stone-900 border-stone-800 text-stone-500" : "bg-stone-100 border-stone-200 text-stone-500"
                }`}>
                  <Lock size={12} /> Locked
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

