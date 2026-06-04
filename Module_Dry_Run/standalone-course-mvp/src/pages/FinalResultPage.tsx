import { useMemo } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { CheckCircle2, AlertTriangle, BookOpenCheck, ListChecks, Lock } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { EXAM } from "../data/examPool";
import { paths } from "../app/routes";
import { appCopy, courseModules } from "../data/contentV2Adapter";
import { buildFinalRemediation } from "../data/remediation";

export function FinalResultPage() {
  const navigate = useNavigate();
  const { state } = useLearner();
  const location = useLocation();
  const nav = location.state as { pct?: number; passed?: boolean } | null;

  const passed = nav?.passed ?? state.finalExamPassed;
  const pct = nav?.pct ?? state.finalExamBestScorePct ?? 0;
  const remediation = useMemo(() => buildFinalRemediation(courseModules), []);

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl text-center space-y-6">
        {passed ? (
          <>
            <div className="w-16 h-16 rounded bg-stone-900 border border-amber-500/40 flex items-center justify-center mx-auto text-amber-400">
              <CheckCircle2 size={32} />
            </div>
            <div>
              <span className="text-[10px] uppercase font-bold text-amber-400 font-mono tracking-widest bg-amber-950/20 px-2 py-0.5 rounded border border-amber-500/20">Passed Course Exam</span>
              <h1 className="text-3xl font-normal text-stone-100 tracking-tight mt-3">{appCopy.final.pass_title}</h1>
              <p className="text-xs text-stone-400 mt-2">{appCopy.final.pass_body}</p>
            </div>
            <div className="bg-stone-950 p-4 rounded border border-stone-900 max-w-sm mx-auto font-mono text-xs text-stone-400 flex justify-between">
              <span>Recorded Score:</span><strong className="text-amber-400">{pct}% Correct</strong>
            </div>
            <div className="pt-4 flex justify-center">
              <button onClick={() => navigate(paths.certificate)} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
                Proceed to Certificate Gate &rarr;
              </button>
            </div>
          </>
        ) : (
          <>
            <div className="w-16 h-16 rounded bg-red-950/40 border border-red-500/40 flex items-center justify-center mx-auto text-red-500">
              <AlertTriangle size={32} />
            </div>
            <div>
              <span className="text-[10px] uppercase font-bold text-red-400 font-mono tracking-widest bg-red-950/20 px-2 py-0.5 rounded border border-red-500/20">Requires Remediation</span>
              <h1 className="text-3xl font-normal text-stone-100 tracking-tight mt-3">{appCopy.final.fail_title}</h1>
              <p className="text-xs text-stone-400 mt-2 max-w-md mx-auto leading-relaxed">{remediation.overview}</p>
            </div>
            <div className="bg-stone-950 p-4 rounded border border-stone-900 max-w-sm mx-auto font-mono text-xs text-stone-400 flex justify-between">
              <span>Recorded Score:</span><strong className="text-red-500">{pct}% Correct · need {EXAM.PASS_PCT}%</strong>
            </div>

            {/* Topic areas to review (no answer keys, no rationales) */}
            <div className="text-left space-y-2.5">
              <h4 className="text-[10px] uppercase font-bold text-stone-400 font-mono tracking-wider flex items-center gap-1.5">
                <BookOpenCheck size={12} className="text-amber-500" /> Topic Areas to Review
              </h4>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                {remediation.topicAreas.map((topic) => (
                  <div key={topic.code} className="p-3 rounded border border-stone-800 bg-[#080404]">
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-[10px] font-mono font-bold text-amber-500 uppercase">{topic.code}</span>
                    </div>
                    <h5 className="text-xs font-semibold text-stone-200">{topic.title}</h5>
                    <p className="text-[11px] text-stone-400 leading-relaxed mt-1">{topic.revisit}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Remediation pathway */}
            <div className="text-left space-y-2">
              <h4 className="text-[10px] uppercase font-bold text-stone-400 font-mono tracking-wider flex items-center gap-1.5">
                <ListChecks size={12} className="text-amber-500" /> Remediation Pathway
              </h4>
              <ol className="space-y-1.5">
                {remediation.pathway.map((step, idx) => (
                  <li key={step} className="flex gap-2.5 items-start text-[11px] text-stone-400 leading-relaxed">
                    <span className="text-amber-500 font-bold font-mono">{idx + 1}.</span>
                    <span>{step}</span>
                  </li>
                ))}
              </ol>
            </div>

            <div className="bg-stone-950 border border-stone-900 p-3 rounded text-left max-w-xl mx-auto flex items-start gap-2">
              <Lock size={12} className="text-stone-500 shrink-0 mt-0.5" />
              <p className="text-[10px] text-stone-500 leading-relaxed font-mono">{remediation.retryInstructions}</p>
            </div>

            <div className="pt-4 flex flex-col sm:flex-row justify-center gap-3">
              <button onClick={() => navigate(paths.finalSplash)} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
                Retake Assessment Exam
              </button>
              <button onClick={() => navigate(paths.modules)} className="bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-300 font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
                Return to Modules
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
