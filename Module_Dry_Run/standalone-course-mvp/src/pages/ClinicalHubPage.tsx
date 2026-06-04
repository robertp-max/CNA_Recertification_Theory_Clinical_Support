import { useState } from "react";
import { Stethoscope, AlertTriangle } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { useUiState } from "../lib/uiState";
import { PhiWarningBlock } from "../components/ui/PhiWarningBlock";
import { appCopy, contentV2 } from "../data/contentV2Adapter";

// Optional Clinical Support. Always optional, non-credit, and NON-GATING — none
// of this affects required CE / certificate readiness (enforced in gates.ts).
export function ClinicalHubPage() {
  const { state, setOptionalClinical } = useLearner();
  const { brandingMode } = useUiState();
  const isDark = brandingMode === "dark";
  const [inputText, setInputText] = useState("");

  const o = state.optionalClinical;
  const interactions = [o.hub, o.skills, o.confidence, o.documentation, o.help].filter(Boolean).length;
  const styles = {
    card: isDark ? "bg-[#120909] border-stone-850 shadow-xl" : "bg-white border-stone-200 shadow-sm",
    title: isDark ? "text-stone-100" : "text-stone-900",
    subtitle: isDark ? "text-stone-300" : "text-stone-800",
    body: isDark ? "text-stone-400" : "text-stone-600",
    muted: isDark ? "text-stone-500" : "text-stone-500",
    accent: isDark ? "text-amber-500" : "text-[#8B1515]",
    divider: isDark ? "border-stone-800/60" : "border-stone-200",
    primaryButton: isDark ? "bg-[#5c1111] hover:bg-[#781616] text-stone-100 border-[#8a1d1d]" : "bg-[#8B1515] hover:bg-[#741111] text-white border-[#8B1515]",
  };

  return (
    <div className="space-y-6">
      <div className={`border rounded-xl p-6 md:p-8 ${styles.card}`}>
        <div className={`flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b ${styles.divider}`}>
          <div>
            <span className={`text-[10px] uppercase font-bold font-mono flex items-center gap-1.5 ${styles.accent}`}>
              <Stethoscope size={12} /> {appCopy.clinicalHub.eyebrow}
            </span>
            <h1 className={`text-2xl font-normal mt-1 ${styles.title}`}>{appCopy.clinicalHub.title}</h1>
          </div>
          <span className={`inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-[10px] font-bold border font-mono shrink-0 ${
            isDark ? "bg-amber-950/40 text-amber-400 border-amber-500/20" : "bg-[#8B1515]/5 text-[#8B1515] border-[#8B1515]/20"
          }`}>
            {appCopy.clinicalHub.badge}
          </span>
        </div>

        <div className={`border rounded-lg p-4 my-6 ${isDark ? "bg-amber-950/20 border-amber-500/20" : "bg-[#8B1515]/5 border-[#8B1515]/20"}`}>
          <div className="flex items-start gap-2.5">
            <AlertTriangle size={16} className={`${styles.accent} shrink-0 mt-0.5`} />
            <p className={`text-[11px] leading-relaxed font-mono ${styles.body}`}>
              <strong>Regulatory Warning:</strong> {appCopy.clinicalHub.warning}
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4">
          {appCopy.clinicalHub.scenarios.map((scenario, index) => (
            <div key={scenario.title} className={`p-5 rounded-lg border transition-colors ${isDark ? "bg-[#080404] border-stone-800 hover:border-stone-700" : "bg-stone-50 border-stone-200 hover:border-[#8B1515]/25"}`}>
              <h3 className={`text-xs font-bold uppercase tracking-wider mb-2 font-mono ${styles.subtitle}`}>{scenario.title}</h3>
              <p className={`text-xs leading-relaxed mb-4 ${styles.body}`}>{scenario.body}</p>
              <div className="flex items-center justify-between gap-3">
                <span className={`text-[10px] font-mono ${styles.muted}`}>
                  {index === 0 ? `${contentV2.clinical_support.units.length} Units` : `${contentV2.clinical_support.confidence_checks.length} Checks`}
                </span>
                <button
                  onClick={() => setOptionalClinical(index === 0 ? "skills" : "confidence", true)}
                  className={`border font-bold px-4 py-1.5 rounded text-[10px] uppercase tracking-wider transition-colors ${styles.primaryButton}`}
                >
                  {scenario.action}
                </button>
              </div>
            </div>
          ))}
        </div>

        {interactions > 0 && (
          <div className={`mt-6 p-4 rounded border text-xs font-mono flex justify-between items-center ${
            isDark ? "border-stone-850 bg-stone-950 text-stone-400" : "border-stone-200 bg-stone-50 text-stone-600"
          }`}>
            <span>Optional practice engaged (does not affect certificate progress):</span>
            <strong className={styles.accent}>{interactions} session{interactions === 1 ? "" : "s"}</strong>
          </div>
        )}

        {/* Documentation support (practice) */}
        <div className={`border rounded-xl p-6 md:p-8 mt-8 ${isDark ? "bg-[#120a0a]/80 border-stone-800/60" : "bg-stone-50 border-stone-200"}`}>
          <h2 className={`text-xl font-bold mb-6 ${styles.title}`}>{appCopy.clinicalHub.documentation_title}</h2>

          <div className="mb-6">
            <PhiWarningBlock brandingMode={brandingMode} />
            <p className={`text-[11px] font-mono mt-3 ${styles.muted}`}>{appCopy.clinicalHub.documentation_warning}</p>
          </div>

          <div className="space-y-2 mb-6">
            <label className={`text-xs font-bold ${styles.subtitle}`}>Practice note — fictional / de-identified details only</label>
            <textarea
              rows={4}
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              className={`w-full border rounded-lg p-4 text-xs focus:outline-none resize-none ${
                isDark
                  ? "bg-[#080404] border-stone-800/80 text-stone-300 focus:border-amber-500/50 placeholder:text-stone-600"
                  : "bg-white border-stone-300 text-stone-800 focus:border-[#8B1515]/50 placeholder:text-stone-400"
              }`}
              placeholder="Do not type patient or resident identifiers. Use fictional practice notes only."
            />
          </div>

          <button disabled className={`px-6 py-3 rounded-xl border font-semibold text-sm cursor-not-allowed ${
            isDark ? "bg-black/40 text-stone-600 border-white/5" : "bg-stone-100 text-stone-500 border-stone-200"
          }`}>
            Mock upload disabled
          </button>
        </div>
      </div>
    </div>
  );
}
