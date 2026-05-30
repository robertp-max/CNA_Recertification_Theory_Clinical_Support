import { useState } from "react";
import { Stethoscope, AlertTriangle } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { PhiWarningBlock } from "../components/ui/PhiWarningBlock";
import { appCopy, contentV2 } from "../data/contentV2Adapter";

// Optional Clinical Support. Always optional, non-credit, and NON-GATING — none
// of this affects required CE / certificate readiness (enforced in gates.ts).
export function ClinicalHubPage() {
  const { state, setOptionalClinical } = useLearner();
  const [inputText, setInputText] = useState("");

  const o = state.optionalClinical;
  const interactions = [o.hub, o.skills, o.confidence, o.documentation, o.help].filter(Boolean).length;

  return (
    <div className="space-y-6">
      <div className="bg-[#120909] border border-stone-850 rounded-xl p-6 md:p-8 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-stone-800/60">
          <div>
            <span className="text-[10px] uppercase font-bold text-amber-500 font-mono flex items-center gap-1.5">
              <Stethoscope size={12} /> {appCopy.clinicalHub.eyebrow}
            </span>
            <h1 className="text-2xl font-normal text-stone-100 mt-1">{appCopy.clinicalHub.title}</h1>
          </div>
          <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-[10px] font-bold bg-amber-950/40 text-amber-400 border border-amber-500/20 font-mono shrink-0">
            {appCopy.clinicalHub.badge}
          </span>
        </div>

        <div className="bg-amber-950/20 border border-amber-500/20 rounded-lg p-4 my-6">
          <div className="flex items-start gap-2.5">
            <AlertTriangle size={16} className="text-amber-500 shrink-0 mt-0.5" />
            <p className="text-[11px] text-stone-400 leading-relaxed font-mono">
              <strong>Regulatory Warning:</strong> {appCopy.clinicalHub.warning}
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4">
          {appCopy.clinicalHub.scenarios.map((scenario, index) => (
            <div key={scenario.title} className="p-5 rounded-lg bg-[#080404] border border-stone-800 hover:border-stone-700 transition-colors">
              <h3 className="text-xs font-bold uppercase tracking-wider text-stone-300 mb-2 font-mono">{scenario.title}</h3>
              <p className="text-xs text-stone-400 leading-relaxed mb-4">{scenario.body}</p>
              <div className="flex items-center justify-between gap-3">
                <span className="text-[10px] text-stone-500 font-mono">
                  {index === 0 ? `${contentV2.clinical_support.units.length} Units` : `${contentV2.clinical_support.confidence_checks.length} Checks`}
                </span>
                <button
                  onClick={() => setOptionalClinical(index === 0 ? "skills" : "confidence", true)}
                  className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-4 py-1.5 rounded text-[10px] uppercase tracking-wider transition-colors"
                >
                  {scenario.action}
                </button>
              </div>
            </div>
          ))}
        </div>

        {interactions > 0 && (
          <div className="mt-6 p-4 rounded border border-stone-850 bg-stone-950 text-stone-400 text-xs font-mono flex justify-between items-center">
            <span>Optional practice engaged (does not affect certificate progress):</span>
            <strong className="text-amber-500">{interactions} session{interactions === 1 ? "" : "s"}</strong>
          </div>
        )}

        {/* Documentation support (practice) */}
        <div className="bg-[#120a0a]/80 border border-stone-800/60 rounded-xl p-6 md:p-8 mt-8">
          <h2 className="text-xl font-bold text-white mb-6">{appCopy.clinicalHub.documentation_title}</h2>

          <div className="mb-6">
            <PhiWarningBlock />
            <p className="text-[11px] text-stone-500 font-mono mt-3">{appCopy.clinicalHub.documentation_warning}</p>
          </div>

          <div className="space-y-2 mb-6">
            <label className="text-xs font-bold text-stone-300">Practice note — fictional / de-identified details only</label>
            <textarea
              rows={4}
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              className="w-full bg-[#080404] border border-stone-800/80 rounded-lg p-4 text-xs text-stone-300 focus:outline-none focus:border-amber-500/50 resize-none"
              placeholder="Do not type patient or resident identifiers. Use fictional practice notes only."
            />
          </div>

          <button disabled className="px-6 py-3 rounded-xl bg-black/40 text-stone-600 border border-white/5 font-semibold text-sm cursor-not-allowed">
            Mock upload disabled
          </button>
        </div>
      </div>
    </div>
  );
}
