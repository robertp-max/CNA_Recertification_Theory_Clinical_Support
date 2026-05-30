import { useNavigate } from "react-router-dom";
import { ShieldAlert } from "lucide-react";
import { paths } from "../app/routes";
import { BackLink } from "../components/v2/primitives";
import { moduleQuizItems, MODULE_QUIZ_PASS_PCT } from "../data/v2ModuleQuiz";
import { appCopy } from "../data/contentV2Adapter";

export function ModuleAssessmentSplashPage() {
  const navigate = useNavigate();
  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <BackLink to={paths.module1}>Back to Module 1</BackLink>

      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl text-center space-y-6">
        <div className="w-12 h-12 rounded bg-[#1c0c0c] border border-[#5c1111] flex items-center justify-center mx-auto text-amber-500">
          <ShieldAlert size={24} />
        </div>
        <div>
          <span className="text-[10px] uppercase font-bold text-stone-500 font-mono tracking-widest">Formal Assessment Portal</span>
          <h1 className="text-2xl font-normal text-stone-100 tracking-tight mt-1">{appCopy.moduleAssessment.title}</h1>
          <p className="text-xs text-stone-400 max-w-md mx-auto leading-relaxed mt-2">
            {appCopy.moduleAssessment.summary} You must score {MODULE_QUIZ_PASS_PCT}% or higher to advance.
          </p>
        </div>

        <div className="bg-stone-950 p-4 rounded border border-stone-900 text-left max-w-md mx-auto space-y-3 font-mono text-[11px] text-stone-400">
          <div className="flex justify-between"><span>Structured Questions:</span><span className="text-stone-200">{moduleQuizItems.length} Questions</span></div>
          <div className="flex justify-between"><span>Target Score:</span><span className="text-amber-500">{MODULE_QUIZ_PASS_PCT}% Minimum</span></div>
          <div className="flex justify-between"><span>Remediation Rules:</span><span className="text-stone-200">Unlimited Retakes</span></div>
        </div>

        <div className="pt-4 flex flex-col sm:flex-row justify-center gap-3">
          <button onClick={() => navigate(paths.moduleAssessmentQuiz)} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
            Begin Assessment Exam
          </button>
          <button onClick={() => navigate(paths.module1)} className="bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-300 font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
            Study Material Again
          </button>
        </div>
      </div>
    </div>
  );
}
