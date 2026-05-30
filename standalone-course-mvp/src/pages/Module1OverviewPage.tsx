import { useNavigate } from "react-router-dom";
import { CheckCircle2, Lock, Play } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { lessonCompleted, moduleAssessmentPassed } from "../lib/v2state";
import { paths } from "../app/routes";
import { BackLink, StatusBadge } from "../components/v2/primitives";
import { appCopy, getModuleDef } from "../data/contentV2Adapter";

export function Module1OverviewPage() {
  const navigate = useNavigate();
  const { state } = useLearner();
  const module = getModuleDef("m1");
  const lesson = lessonCompleted(state);
  const m1Exam = moduleAssessmentPassed(state);

  if (!module) return null;

  return (
    <div className="max-w-3xl mx-auto space-y-6">
      <BackLink to={paths.modules}>Back to Modules</BackLink>

      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-stone-800/60">
          <div>
            <span className="text-[10px] uppercase font-bold text-amber-500 font-mono">
              {module.code} - {module.time} Theory
            </span>
            <h1 className="text-2xl font-normal text-stone-100 tracking-tight">{module.shortTitle}</h1>
          </div>
          <StatusBadge tone={m1Exam ? "complete" : module.status === "sme-review" ? "action" : "pending"}>
            {m1Exam ? "Complete" : module.status === "sme-review" ? "SME Review Flagged" : "Not Attempted"}
          </StatusBadge>
        </div>

        <div className="py-6 space-y-4">
          <h3 className="text-xs uppercase tracking-wider font-bold text-stone-300">Lesson Objectives</h3>
          <div className="grid grid-cols-1 gap-2.5">
            {module.learningObjectives.map((obj, idx) => (
              <div key={obj} className="flex gap-2.5 items-start text-xs text-stone-400 leading-relaxed">
                <span className="text-amber-500 font-bold font-mono">{String(idx + 1).padStart(2, "0")}.</span>
                <span>{obj}</span>
              </div>
            ))}
          </div>
          {module.reviewerNote && (
            <div className="bg-amber-950/20 border border-amber-500/20 rounded p-3 text-[11px] text-stone-400 font-mono leading-relaxed">
              {module.reviewerNote}
            </div>
          )}
        </div>

        <div className="space-y-3 pt-4 border-t border-stone-800/60">
          <h3 className="text-xs uppercase tracking-wider font-bold text-stone-300">Course Component Lessons</h3>

          {module.lessons.map((item, idx) => {
            const routeReady = idx === 0;
            return (
              <button
                key={item.id}
                type="button"
                onClick={() => routeReady && navigate(paths.lesson)}
                disabled={!routeReady}
                className={`w-full p-4 rounded border transition-all flex items-center justify-between text-left ${
                  routeReady
                    ? "bg-[#080404] border-stone-800 hover:border-[#5c1111]/80 hover:bg-[#120909]"
                    : "bg-[#080404]/40 border-stone-900 opacity-70 cursor-not-allowed"
                }`}
              >
                <div className="flex items-center gap-3 min-w-0">
                  <div className="w-8 h-8 rounded bg-[#1c0d0d] flex items-center justify-center border border-[#5c1111]/40 text-amber-500 font-bold font-mono text-xs shrink-0">
                    {item.index}
                  </div>
                  <div className="min-w-0">
                    <h4 className="text-xs font-semibold text-stone-200 truncate">{item.title}</h4>
                    <span className="text-[10px] text-stone-500 font-mono uppercase tracking-wide">
                      {item.estMinutes} min - ContentV2 4-card model
                    </span>
                  </div>
                </div>
                {routeReady ? (
                  lesson ? (
                    <span className="text-amber-400 flex items-center gap-1 text-[10px] font-bold shrink-0">
                      <CheckCircle2 size={12} /> Finished
                    </span>
                  ) : (
                    <span className="text-amber-500 flex items-center gap-1 text-[10px] font-bold shrink-0">
                      <Play size={12} className="fill-current" /> Play
                    </span>
                  )
                ) : (
                  <span className="text-[10px] text-stone-600 font-mono inline-flex items-center gap-1 shrink-0">
                    <Lock size={10} /> Route Pending
                  </span>
                )}
              </button>
            );
          })}
        </div>

        <div className="pt-8 border-t border-stone-800/60 flex flex-col sm:flex-row items-center gap-4 justify-between">
          <div className="text-xs text-stone-400">
            {lesson ? "ContentV2 lesson complete. Continue to the module assessment." : "Complete Lesson 1 to unlock the Module Assessment."}
          </div>
          <div className="flex gap-3 w-full sm:w-auto">
            {lesson && (
              <button
                onClick={() => navigate(paths.moduleAssessment)}
                className="w-full sm:w-auto bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors"
              >
                Start {appCopy.moduleAssessment.title}
              </button>
            )}
            <button
              onClick={() => navigate(paths.lesson)}
              className="w-full sm:w-auto bg-stone-900 hover:bg-stone-850 border border-stone-800 text-stone-300 font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors"
            >
              {lesson ? "Review Theory" : "Start Theory"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

