import { useNavigate } from "react-router-dom";
import { Award } from "lucide-react";
import { useUiState, formatHoursAndMins } from "../lib/uiState";
import { EXAM } from "../data/examPool";
import { paths } from "../app/routes";
import { BackLink } from "../components/v2/primitives";
import { appCopy } from "../data/contentV2Adapter";

export function FinalAssessmentSplashPage() {
  const navigate = useNavigate();
  const { demoSeconds, brandingMode } = useUiState();
  const isDark = brandingMode === "dark";

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <BackLink to={paths.modules}>Back to Modules</BackLink>

      <div className={`border rounded-xl p-6 md:p-10 text-center space-y-6 ${isDark ? "bg-[#120909] border-stone-800/80 shadow-xl" : "bg-white border-stone-200 shadow-sm"}`}>
        <div className={`w-14 h-14 rounded border flex items-center justify-center mx-auto ${
          isDark ? "bg-[#1c0c0c] border-[#5c1111] text-amber-500" : "bg-[#8B1515]/5 border-[#8B1515]/20 text-[#8B1515]"
        }`}>
          <Award size={28} />
        </div>
        <div>
          <span className="text-[10px] uppercase font-bold text-stone-500 font-mono tracking-widest">Course-Wide Examination</span>
          <h1 className={`text-3xl font-normal tracking-tight mt-1 ${isDark ? "text-stone-100" : "text-stone-900"}`}>{appCopy.final.title}</h1>
          <p className={`text-xs max-w-md mx-auto leading-relaxed mt-2 ${isDark ? "text-stone-400" : "text-stone-600"}`}>
            {appCopy.final.summary}
          </p>
        </div>

        <div className={`p-5 rounded border text-left max-w-md mx-auto space-y-3 font-mono text-[11px] ${
          isDark ? "bg-[#0c0505] border-stone-900 text-stone-400" : "bg-stone-50 border-stone-200 text-stone-600"
        }`}>
          <div className="flex justify-between"><span>Active Time Logged (demo):</span><span className={isDark ? "text-stone-200" : "text-stone-800"}>{formatHoursAndMins(demoSeconds)}</span></div>
          <div className="flex justify-between"><span>Minimum Passing:</span><span className={isDark ? "text-amber-500" : "text-[#8B1515]"}>{EXAM.PASS_PCT}% Correct</span></div>
          <div className="flex justify-between"><span>Post-Exam Track:</span><span className={isDark ? "text-stone-200" : "text-stone-800"}>Affidavit Validation</span></div>
        </div>

        <div className={`border p-4 rounded text-left max-w-md mx-auto ${isDark ? "bg-amber-950/20 border-amber-500/20" : "bg-[#8B1515]/5 border-[#8B1515]/20"}`}>
          <p className={`text-[10px] leading-relaxed font-mono ${isDark ? "text-stone-400" : "text-stone-700"}`}>
            <strong>No Answer Key Notice:</strong> {appCopy.final.no_key_notice}
          </p>
        </div>

        <div className="pt-4 flex flex-col sm:flex-row justify-center gap-3">
          <button onClick={() => navigate(paths.finalQuiz)} className={`border font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors ${
            isDark ? "bg-[#5c1111] hover:bg-[#781616] text-stone-100 border-[#8a1d1d]" : "bg-[#8B1515] hover:bg-[#741111] text-white border-[#8B1515]"
          }`}>
            Begin Course Final Exam
          </button>
          <button onClick={() => navigate(paths.modules)} className={`border font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors ${
            isDark ? "bg-stone-900 border-stone-800 hover:bg-stone-850 text-stone-300" : "bg-white border-stone-300 hover:bg-stone-50 text-stone-700"
          }`}>
            Go Back &amp; Study Modules
          </button>
        </div>
      </div>
    </div>
  );
}
