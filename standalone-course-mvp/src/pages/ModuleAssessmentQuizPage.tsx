import { useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import { CheckCircle2 } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { withModuleAssessment } from "../lib/v2state";
import { paths } from "../app/routes";
import { QuizRunner } from "../components/v2/QuizRunner";
import { ModuleRemediationPanel } from "../components/v2/ModuleRemediationPanel";
import { moduleQuizItems, scoreModuleQuiz, MODULE_QUIZ_PASS_PCT } from "../data/v2ModuleQuiz";
import { appCopy, getGeneratedModule } from "../data/contentV2Adapter";
import { buildModuleRemediation } from "../data/remediation";

export function ModuleAssessmentQuizPage() {
  const navigate = useNavigate();
  const { setState, recordRemediation } = useLearner();
  const [result, setResult] = useState<{ pct: number; passed: boolean } | null>(null);

  const remediation = useMemo(() => {
    const mod = getGeneratedModule("M01");
    return buildModuleRemediation(mod?.module_title ?? "Module 1", mod?.lessons ?? []);
  }, []);

  if (!result) {
    return (
      <QuizRunner
        label="MODULE 1 ASSESSMENT"
        questions={moduleQuizItems}
        onSubmit={(answers) => {
          const scored = scoreModuleQuiz(answers);
          setState((s) => withModuleAssessment(s, scored.passed));
          if (!scored.passed) recordRemediation("Module 1 assessment remediation (theory review)");
          setResult(scored);
        }}
      />
    );
  }

  if (!result.passed) {
    return (
      <ModuleRemediationPanel
        scorePct={result.pct}
        passPct={MODULE_QUIZ_PASS_PCT}
        remediation={remediation}
        onRetry={() => setResult(null)}
        onStudyAgain={() => navigate(paths.module1)}
      />
    );
  }

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl text-center space-y-6">
        <div className="w-16 h-16 rounded bg-stone-900 border border-amber-500/40 flex items-center justify-center mx-auto text-amber-400">
          <CheckCircle2 size={32} />
        </div>
        <div>
          <span className="text-[10px] uppercase font-bold text-amber-400 font-mono tracking-widest bg-amber-950/20 px-2 py-0.5 rounded border border-amber-500/20">Module 1 Passed</span>
          <h1 className="text-2xl font-normal text-stone-100 tracking-tight mt-3">Module Assessment Complete</h1>
          <p className="text-xs text-stone-400 mt-2">{appCopy.moduleAssessment.summary}</p>
          <p className="text-xs text-stone-400 mt-1">The course-wide Final Assessment gate is now available on the Modules page.</p>
        </div>
        <div className="bg-stone-950 p-4 rounded border border-stone-900 max-w-sm mx-auto font-mono text-xs text-stone-400 flex justify-between">
          <span>Recorded Score:</span><strong className="text-amber-400">{result.pct}%</strong>
        </div>
        <div className="pt-2">
          <button onClick={() => navigate(paths.modules)} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors">
            Continue to Modules &rarr;
          </button>
        </div>
      </div>
    </div>
  );
}
