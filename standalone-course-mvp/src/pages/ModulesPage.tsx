import { useNavigate } from "react-router-dom";
import { CheckCircle2, Lock, Shield } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { requiredProgressPct } from "../lib/progress";
import { isModuleComplete, isModuleUnlocked, moduleProgressPct } from "../lib/moduleProgress";
import { moduleAssessmentPassed } from "../lib/v2state";
import { paths } from "../app/routes";
import { StatusBadge } from "../components/v2/primitives";
import { courseModules } from "../data/courseModules";
import type { ModuleDef } from "../data/lessonModel";

function routeForModule(module: ModuleDef): string | null {
  if (module.id === "m0") return paths.module0;
  if (module.id === "m1") return paths.module1;
  if (module.id === "m7") return paths.finalSplash;
  return null;
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

  const m1Exam = moduleAssessmentPassed(state);
  const finalPassed = state.finalExamPassed;
  const progress = requiredProgressPct(state);

  return (
    <div className="flex flex-col lg:flex-row gap-8">
      <div className="w-full lg:w-80 shrink-0">
        <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 lg:sticky lg:top-8">
          <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-3 flex items-center gap-1.5">
            <Shield size={12} /> Theory CE Requirements
          </div>
          <h2 className="text-2xl font-normal text-stone-100 mb-3 leading-tight">Curriculum</h2>
          <p className="text-xs text-stone-400 mb-6 leading-relaxed">
            ContentV2 supplies the complete 720-minute required theory package. Current learner routes demonstrate Module
            0, Module 1, and the assessment gates while later modules are loaded for future screens.
          </p>

          <div className="space-y-2 mb-6 border-t border-stone-800/80 pt-4">
            <div className="flex justify-between text-[11px] text-stone-400">
              <span>Legal Name</span>
              <span className="font-mono text-stone-200">{state.legalFirstName} {state.legalLastName}</span>
            </div>
            <div className="flex justify-between text-[11px] text-stone-400">
              <span>CNA Certificate #</span>
              <span className="font-mono text-stone-200">{state.cnaNumber || "-"}</span>
            </div>
          </div>

          <div className="space-y-2 mb-6">
            <div className="flex justify-between text-[11px] font-semibold">
              <span className="text-stone-300">Required Progress</span>
              <span className="text-amber-500 font-mono">{progress}%</span>
            </div>
            <div className="w-full h-1 bg-stone-900 rounded-full overflow-hidden">
              <div className="h-full bg-amber-500 transition-all" style={{ width: `${progress}%` }} />
            </div>
          </div>

          <button
            onClick={() => navigate(paths.certificate)}
            className="w-full py-2.5 rounded bg-stone-900 hover:bg-stone-850 border border-stone-800 text-stone-200 font-semibold text-xs uppercase tracking-wider transition-colors"
          >
            Review Gate Checklist
          </button>
        </div>
      </div>

      <div className="flex-1 space-y-6">
        <div>
          <h2 className="text-2xl font-normal text-stone-100 mb-1">Theory Recertification Modules</h2>
          <p className="text-stone-400 text-xs">ContentV2 data is loaded for Modules 0 through 7; route coverage remains prototype-scoped.</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {courseModules.map((module) => {
            const route = routeForModule(module);
            const complete = isModuleComplete(state, module.id);
            const unlocked = isModuleUnlocked(state, module.id);
            const pct = moduleProgressPct(state, module.id);
            const isRouteReady = Boolean(route) && (unlocked || state.unlockMode || module.id === "m0");
            const isFinal = module.id === "m7";
            const canOpenFinal = isFinal && (state.unlockMode || m1Exam || finalPassed);

            return (
              <div
                key={module.id}
                className={`p-5 rounded-xl border transition-all flex flex-col justify-between ${
                  unlocked || module.id === "m0"
                    ? "bg-[#120909] border-stone-800/80 hover:border-stone-700/80"
                    : "bg-[#0a0505]/60 border-stone-950 opacity-75"
                }`}
              >
                <div>
                  <div className="flex items-center justify-between mb-3">
                    <span className="text-[10px] font-bold text-amber-500 uppercase tracking-wider font-mono">{module.code}</span>
                    <span className="text-[10px] font-mono text-stone-500">{module.time}</span>
                  </div>
                  <h3 className="text-base font-semibold text-stone-200 mb-2">{module.shortTitle}</h3>
                  <p className="text-xs text-stone-400 leading-relaxed mb-4 line-clamp-3">{module.summary}</p>
                  {module.reviewerNote && (
                    <p className="text-[10px] text-stone-500 font-mono leading-relaxed mb-4 line-clamp-2">{module.reviewerNote}</p>
                  )}
                </div>

                <div className="space-y-3 pt-3 border-t border-stone-900">
                  <div className="flex items-center justify-between gap-3">
                    {badgeForModule(module, complete, unlocked)}
                    <span className="text-[10px] text-stone-500 font-mono">{pct}%</span>
                  </div>
                  <div className="w-full h-1 bg-stone-950 rounded-full overflow-hidden">
                    <div className="h-full bg-amber-500 transition-all" style={{ width: `${pct}%` }} />
                  </div>
                  {route && (isRouteReady || canOpenFinal) ? (
                    <button
                      onClick={() => navigate(route)}
                      className="w-full px-3 py-1.5 rounded text-xs bg-[#5c1111] text-stone-100 hover:bg-[#781616] transition-colors font-semibold"
                    >
                      {complete ? "Review" : isFinal ? "Enter Final Assessment" : "Open Module"}
                    </button>
                  ) : (
                    <div className="flex items-center justify-between text-[10px] text-stone-600 font-mono">
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

        <div className={`p-6 rounded-xl border transition-all ${m1Exam ? "bg-[#1c0808] border-[#5c1111]/80" : "bg-stone-950/20 border-stone-900/60 opacity-75"}`}>
          <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
            <div>
              <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-[10px] font-bold tracking-widest text-amber-500 uppercase bg-amber-950/40 border border-amber-500/20 mb-3 font-mono">
                Course-Wide Final Examination
              </div>
              <h3 className="text-lg font-semibold text-stone-200 mb-2">Theory Final Assessment Gate</h3>
              <p className="text-xs text-stone-400 max-w-xl leading-relaxed">
                ContentV2 includes the 50-question final pool. The learner-facing result never exposes the full answer key.
              </p>
            </div>
            <div className="shrink-0">
              {finalPassed ? (
                <StatusBadge tone="complete">Passed</StatusBadge>
              ) : m1Exam ? (
                <button onClick={() => navigate(paths.finalSplash)} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-semibold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors">
                  Enter Final Assessment
                </button>
              ) : (
                <div className="flex items-center gap-2 bg-stone-900 border border-stone-800 text-stone-500 px-4 py-2 rounded text-xs font-semibold font-mono">
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

