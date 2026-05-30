import { useNavigate } from "react-router-dom";
import { Award } from "lucide-react";
import { useUiState, formatHoursAndMins } from "../lib/uiState";
import { EXAM } from "../data/examPool";
import { paths } from "../app/routes";
import { BackLink } from "../components/v2/primitives";
import { appCopy } from "../data/contentV2Adapter";

export function FinalAssessmentSplashPage() {
  const navigate = useNavigate();
  const { demoSeconds } = useUiState();

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <BackLink to={paths.modules}>Back to Modules</BackLink>

      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-10 shadow-xl text-center space-y-6">
        <div className="w-14 h-14 rounded bg-[#1c0c0c] border border-[#5c1111] flex items-center justify-center mx-auto text-amber-500">
          <Award size={28} />
        </div>
        <div>
          <span className="text-[10px] uppercase font-bold text-stone-500 font-mono tracking-widest">Course-Wide Examination</span>
          <h1 className="text-3xl font-normal text-stone-100 tracking-tight mt-1">{appCopy.final.title}</h1>
          <p className="text-xs text-stone-400 max-w-md mx-auto leading-relaxed mt-2">
            {appCopy.final.summary}
          </p>
        </div>

        <div className="bg-[#0c0505] p-5 rounded border border-stone-900 text-left max-w-md mx-auto space-y-3 font-mono text-[11px] text-stone-400">
          <div className="flex justify-between"><span>Active Time Logged (demo):</span><span className="text-stone-200">{formatHoursAndMins(demoSeconds)}</span></div>
          <div className="flex justify-between"><span>Minimum Passing:</span><span className="text-amber-500">{EXAM.PASS_PCT}% Correct</span></div>
          <div className="flex justify-between"><span>Post-Exam Track:</span><span className="text-stone-200">Affidavit Validation</span></div>
        </div>

        <div className="bg-amber-950/20 border border-amber-500/20 p-4 rounded text-left max-w-md mx-auto">
          <p className="text-[10px] text-stone-400 leading-relaxed font-mono">
            <strong>No Answer Key Notice:</strong> {appCopy.final.no_key_notice}
          </p>
        </div>

        <div className="pt-4 flex flex-col sm:flex-row justify-center gap-3">
          <button onClick={() => navigate(paths.finalQuiz)} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
            Begin Course Final Exam
          </button>
          <button onClick={() => navigate(paths.modules)} className="bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-300 font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
            Go Back &amp; Study Modules
          </button>
        </div>
      </div>
    </div>
  );
}
