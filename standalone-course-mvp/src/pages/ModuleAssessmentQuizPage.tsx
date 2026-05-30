import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { CheckCircle2, AlertTriangle, Info } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { withModuleAssessment } from "../lib/v2state";
import { paths } from "../app/routes";
import { QuizRunner } from "../components/v2/QuizRunner";
import { moduleQuizItems, scoreModuleQuiz, MODULE_QUIZ_PASS_PCT } from "../data/v2ModuleQuiz";
import { appCopy } from "../data/contentV2Adapter";

export function ModuleAssessmentQuizPage() {
  const navigate = useNavigate();
  const { setState } = useLearner();
  const [result, setResult] = useState<{ pct: number; passed: boolean } | null>(null);

  if (!result) {
    return (
      <QuizRunner
        label="MODULE 1 ASSESSMENT"
        questions={moduleQuizItems}
        onSubmit={(answers) => {
          const scored = scoreModuleQuiz(answers);
          setState((s) => withModuleAssessment(s, scored.passed));
          setResult(scored);
        }}
      />
    );
  }

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl text-center space-y-6">
        {result.passed ? (
          <>
            <div className="w-16 h-16 rounded bg-stone-900 border border-amber-500/40 flex items-center justify-center mx-auto text-amber-400">
              <CheckCircle2 size={32} />
            </div>
            <div>
              <span className="text-[10px] uppercase font-bold text-amber-400 font-mono tracking-widest bg-amber-950/20 px-2 py-0.5 rounded border border-amber-500/20">Module 1 Passed</span>
              <h1 className="text-2xl font-normal text-stone-100 tracking-tight mt-3">Module Assessment Complete</h1>
              <p className="text-xs text-stone-400 mt-2">The course-wide Final Assessment gate is now available on the Modules page.</p>
            </div>
            <div className="bg-stone-950 p-4 rounded border border-stone-900 max-w-sm mx-auto font-mono text-xs text-stone-400 flex justify-between">
              <span>Recorded Score:</span><strong className="text-amber-400">{result.pct}%</strong>
            </div>
            <div className="pt-2">
              <button onClick={() => navigate(paths.modules)} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
                Continue to Modules &rarr;
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
              <h1 className="text-2xl font-normal text-stone-100 tracking-tight mt-3">Below Passing Threshold</h1>
              <p className="text-xs text-stone-400 mt-2 max-w-md mx-auto leading-relaxed">
                Your score fell below the {MODULE_QUIZ_PASS_PCT}% minimum. Answer keys remain hidden to preserve educational integrity.
              </p>
            </div>
            <div className="bg-stone-950 p-4 rounded border border-stone-900 max-w-sm mx-auto font-mono text-xs text-stone-400 flex justify-between">
              <span>Recorded Score:</span><strong className="text-red-400">{result.pct}%</strong>
            </div>
            <div className="bg-red-950/10 border border-red-500/10 p-4 rounded text-left max-w-md mx-auto space-y-2">
              <h4 className="text-[10px] uppercase font-bold text-stone-300 font-mono flex items-center gap-1"><Info size={12} /> Directed Remediation</h4>
              <p className="text-[11px] text-stone-400 leading-relaxed">{appCopy.moduleAssessment.remediation}</p>
            </div>
            <div className="pt-2 flex flex-col sm:flex-row justify-center gap-3">
              <button onClick={() => setResult(null)} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
                Retake Assessment
              </button>
              <button onClick={() => navigate(paths.module1)} className="bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-300 font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
                Study Material Again
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
