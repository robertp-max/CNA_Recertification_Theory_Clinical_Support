import { useLocation, useNavigate } from "react-router-dom";
import { CheckCircle2, AlertTriangle, Info } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { EXAM } from "../data/examPool";
import { paths } from "../app/routes";
import { appCopy } from "../data/contentV2Adapter";

export function FinalResultPage() {
  const navigate = useNavigate();
  const { state } = useLearner();
  const location = useLocation();
  const nav = location.state as { pct?: number; passed?: boolean } | null;

  const passed = nav?.passed ?? state.finalExamPassed;
  const pct = nav?.pct ?? state.finalExamBestScorePct ?? 0;

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
              <p className="text-xs text-stone-400 mt-2 max-w-md mx-auto leading-relaxed">
                {appCopy.final.fail_body} Required threshold: {EXAM.PASS_PCT}%.
              </p>
            </div>
            <div className="bg-stone-950 p-4 rounded border border-stone-900 max-w-sm mx-auto font-mono text-xs text-stone-400 flex justify-between">
              <span>Recorded Score:</span><strong className="text-red-500">{pct}% Correct</strong>
            </div>
            <div className="bg-red-950/10 border border-red-500/10 p-4 rounded text-left max-w-md mx-auto space-y-2">
              <h4 className="text-[10px] uppercase font-bold text-stone-300 font-mono flex items-center gap-1"><Info size={12} /> Directed Remediation</h4>
              <p className="text-[11px] text-stone-400 leading-relaxed">
                {appCopy.final.fail_body}
              </p>
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
