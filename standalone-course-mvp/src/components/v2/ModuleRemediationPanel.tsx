import { useState } from "react";
import { BookOpenCheck, ListChecks, Repeat, Target } from "lucide-react";
import type { ModuleRemediation } from "../../data/remediation";

// Failed-module-assessment remediation, modeled as a REQUIRED THEORY EXTENSION.
// Not clinical support, not a clinical hour, not competency validation. No final
// assessment answer keys are exposed.
export function ModuleRemediationPanel({
  scorePct,
  passPct,
  remediation,
  onRetry,
  onStudyAgain,
}: {
  scorePct: number;
  passPct: number;
  remediation: ModuleRemediation;
  onRetry: () => void;
  onStudyAgain: () => void;
}) {
  const [checked, setChecked] = useState<boolean[]>(remediation.retryReadiness.map(() => false));
  const ready = checked.every(Boolean);

  return (
    <div className="max-w-2xl mx-auto space-y-5">
      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl space-y-6">
        <div className="text-center space-y-3">
          <span className="text-[10px] uppercase font-bold text-red-400 font-mono tracking-widest bg-red-950/20 px-2 py-0.5 rounded border border-red-500/20">
            Required Theory Remediation
          </span>
          <h1 className="text-2xl font-normal text-stone-100 tracking-tight">Module Review Before Retry</h1>
          <div className="inline-flex items-center gap-2 bg-stone-950 px-4 py-1.5 rounded border border-stone-900 font-mono text-xs text-stone-400">
            <span>Recorded score</span>
            <strong className="text-red-400">{scorePct}%</strong>
            <span className="text-stone-600">· need {passPct}%</span>
          </div>
        </div>

        {/* Remediation Overview */}
        <div className="space-y-1.5">
          <h4 className="text-[10px] uppercase font-bold text-stone-400 font-mono tracking-wider flex items-center gap-1.5">
            <Target size={12} className="text-amber-500" /> Remediation Overview
          </h4>
          <p className="text-xs text-stone-300 leading-relaxed">{remediation.overview}</p>
        </div>

        {/* Missed Topic Review Cards */}
        <div className="space-y-2.5">
          <h4 className="text-[10px] uppercase font-bold text-stone-400 font-mono tracking-wider flex items-center gap-1.5">
            <BookOpenCheck size={12} className="text-amber-500" /> Missed Topic Review
          </h4>
          <div className="grid grid-cols-1 gap-2.5">
            {remediation.missedTopics.map((topic) => (
              <div key={topic.title} className="p-4 rounded border border-stone-800 bg-[#080404]">
                <h5 className="text-xs font-semibold text-stone-200 mb-1">{topic.title}</h5>
                <p className="text-[11px] text-stone-400 leading-relaxed">{topic.review}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Practice Scenario */}
        <div className="rounded border border-amber-500/25 bg-amber-950/10 p-4 space-y-1.5">
          <h4 className="text-[10px] uppercase font-bold text-amber-400 font-mono tracking-wider">Practice Scenario</h4>
          <p className="text-xs text-stone-200 leading-relaxed">{remediation.practiceScenario.prompt}</p>
          <p className="text-[11px] text-stone-400 leading-relaxed">{remediation.practiceScenario.guidance}</p>
        </div>

        {/* Retry Readiness Check */}
        <div className="space-y-2.5">
          <h4 className="text-[10px] uppercase font-bold text-stone-400 font-mono tracking-wider flex items-center gap-1.5">
            <ListChecks size={12} className="text-amber-500" /> Retry Readiness Check
          </h4>
          <div className="space-y-2">
            {remediation.retryReadiness.map((item, idx) => (
              <label key={item} className="flex items-start gap-2.5 p-3 rounded border border-stone-800 bg-[#080404] cursor-pointer">
                <input
                  type="checkbox"
                  checked={checked[idx]}
                  onChange={() => setChecked((cur) => cur.map((v, i) => (i === idx ? !v : v)))}
                  className="mt-0.5 accent-amber-500"
                />
                <span className="text-[11px] text-stone-300 leading-relaxed">{item}</span>
              </label>
            ))}
          </div>
        </div>

        <div className="pt-2 flex flex-col sm:flex-row justify-center gap-3">
          <button
            onClick={onRetry}
            disabled={!ready}
            className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40 disabled:cursor-not-allowed inline-flex items-center justify-center gap-2"
          >
            <Repeat size={14} /> {remediation.retryLabel}
          </button>
          <button
            onClick={onStudyAgain}
            className="bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-300 font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors"
          >
            Reopen Module Lesson
          </button>
        </div>
        {!ready && (
          <p className="text-[11px] text-stone-500 font-mono text-center">Confirm each readiness item to unlock the retry.</p>
        )}
      </div>
    </div>
  );
}
