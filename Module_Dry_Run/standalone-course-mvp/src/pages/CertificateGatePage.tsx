import { useState } from "react";
import { CheckCircle2, Circle, Lock, ShieldCheck } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { useUiState, formatHoursAndMins } from "../lib/uiState";
import { activeTimeMet, requiredTheoryComplete } from "../lib/moduleProgress";
import { summarizeGates, type GateStatus } from "../lib/gates";
import { MockCertificate } from "../components/v2/MockCertificate";
import { appCopy } from "../data/contentV2Adapter";

function GateRow({ done, locked, title, detail }: { done: boolean; locked?: boolean; title: string; detail: React.ReactNode }) {
  const { brandingMode } = useUiState();
  const isDark = brandingMode === "dark";
  return (
    <div className={`flex items-start gap-3 p-3 border rounded ${isDark ? "bg-[#080404] border-stone-900" : "bg-stone-50 border-stone-200"}`}>
      <div className="mt-0.5 shrink-0">
        {done ? <CheckCircle2 size={16} className={isDark ? "text-amber-400" : "text-[#8B1515]"} /> : locked ? <Lock size={16} className="text-stone-500" /> : <Circle size={16} className="text-stone-500" />}
      </div>
      <div>
        <span className={`text-[11px] font-bold block uppercase font-mono ${isDark ? "text-stone-300" : "text-stone-800"}`}>{title}</span>
        <span className="text-[10px] text-stone-500">{detail}</span>
      </div>
    </div>
  );
}

const statusLabel: Record<GateStatus, string> = {
  complete: "Met",
  pending: "Pending",
  blocked: "Blocked",
  "needs-review": "Needs review",
  "not-started": "Not started",
};

export function CertificateGatePage() {
  const { state, update } = useLearner();
  const { demoSeconds, brandingMode } = useUiState();
  const isDark = brandingMode === "dark";
  const [viewingMock, setViewingMock] = useState(false);

  const legalReady = Boolean(state.legalFirstName.trim() && state.legalLastName.trim() && state.cnaNumber.trim());
  const hoursMet = activeTimeMet(state);
  const competency = requiredTheoryComplete(state) && state.finalExamPassed;
  const affidavit = state.affidavitComplete;
  const coreReady = legalReady && hoursMet && competency;
  const allReady = coreReady && affidavit;

  const summary = summarizeGates(state);
  const styles = {
    card: isDark ? "bg-[#120909] border-stone-800/80" : "bg-white border-stone-200 shadow-sm",
    title: isDark ? "text-stone-200" : "text-stone-900",
    body: isDark ? "text-stone-400" : "text-stone-600",
    muted: isDark ? "text-stone-500" : "text-stone-500",
    divider: isDark ? "border-stone-800/60" : "border-stone-200",
    accent: isDark ? "text-amber-500" : "text-[#8B1515]",
    accentIcon: isDark ? "text-amber-400" : "text-[#8B1515]",
    primaryButton: isDark ? "bg-[#5c1111] hover:bg-[#781616] text-stone-100 border-[#8a1d1d]" : "bg-[#8B1515] hover:bg-[#741111] text-white border-[#8B1515]",
    secondaryButton: isDark ? "bg-stone-900 border-stone-800 text-stone-400" : "bg-white border-stone-300 text-stone-600",
  };

  if (viewingMock) {
    return (
      <MockCertificate
        firstName={state.legalFirstName}
        lastName={state.legalLastName}
        cnaNumber={state.cnaNumber}
        onClose={() => setViewingMock(false)}
      />
    );
  }

  return (
    <div className="space-y-8">
      <div className="flex flex-col lg:flex-row gap-8">
        {/* Left: required audit checklist */}
        <div className="w-full lg:w-[400px] shrink-0 space-y-6">
          <div className={`border rounded-xl p-6 ${styles.card}`}>
            <h2 className={`text-lg font-semibold mb-2 uppercase tracking-wider ${styles.title}`}>{appCopy.certificate.checklist_title}</h2>
            <p className={`text-xs leading-relaxed mb-6 ${styles.body}`}>
              {appCopy.certificate.intro}
            </p>

            <div className="space-y-4">
              <GateRow done={legalReady} title="01. Legal Identity Verified" detail="Legal first/last name and CNA certificate number entered in Module 0." />
              <GateRow done={hoursMet} title="02. 12-Hour Study Time / Active-Time" detail={<>Active-time (demo / MVP — not CDPH-validated): <strong className={`font-mono font-normal ${styles.accent}`}>{hoursMet ? "12h 00m (demo)" : formatHoursAndMins(demoSeconds)}</strong></>} />
              <GateRow done={competency} title="03. Competency Achieved" detail="Required ContentV2 theory modules complete and final assessment passed." />

              {/* Affidavit (interactive once 1–3 met) */}
              <div className={`p-4 rounded border transition-colors ${
                affidavit
                  ? isDark
                    ? "bg-stone-900/40 border-amber-500/20 text-stone-200"
                    : "bg-[#8B1515]/5 border-[#8B1515]/20 text-stone-800"
                  : isDark
                    ? "bg-[#1c0c0c]/40 border-[#5c1111]/30 text-stone-400"
                    : "bg-stone-50 border-stone-200 text-stone-700"
              }`}>
                <div className="flex items-start gap-3">
                  <div className="mt-0.5 shrink-0">
                    {affidavit ? <CheckCircle2 size={16} className={styles.accentIcon} /> : <Circle size={16} className={isDark ? "text-[#5c1111]" : "text-stone-500"} />}
                  </div>
                  <div className="w-full">
                    <span className="text-[11px] font-bold block uppercase font-mono">04. Professional Affidavit</span>
                    <p className={`text-[10px] mt-1 mb-3 ${styles.muted}`}>{appCopy.certificate.affidavit_text}</p>
                    {coreReady ? (
                      <button
                        onClick={() => update("affidavitComplete", !affidavit)}
                        className={`w-full py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-colors border ${affidavit ? styles.secondaryButton : styles.primaryButton}`}
                      >
                        {affidavit ? "Revoke Signature" : "Sign Draft Affidavit"}
                      </button>
                    ) : (
                      <span className="text-[9px] text-stone-500 uppercase font-mono font-bold block">Locked (Complete Steps 1–3 first)</span>
                    )}
                  </div>
                </div>
              </div>
            </div>

            {/* Deeper compliance gate detail (preserved engine) */}
            <details className="mt-6 group">
              <summary className={`cursor-pointer text-[10px] uppercase font-bold font-mono tracking-wider transition-colors ${isDark ? "text-stone-400 hover:text-stone-200" : "text-stone-600 hover:text-[#8B1515]"}`}>
                Full compliance gate detail ({summary.passingCount}/{summary.totalCount} certificate gates met)
              </summary>
              <div className="mt-3 space-y-1.5">
                {summary.gates.map((g) => (
                  <div key={g.key} className={`flex items-center justify-between gap-3 text-[10px] border-b pb-1.5 ${isDark ? "border-stone-900/80" : "border-stone-200"}`}>
                    <span className={styles.body}>
                      {g.label}
                      {g.simulated ? <span className={isDark ? "text-amber-500/70" : "text-[#8B1515]/70"}> (simulated)</span> : null}
                      {!g.affectsCertificate ? <span className="text-stone-500"> · non-gating</span> : null}
                    </span>
                    <span className={`font-mono shrink-0 ${g.status === "complete" ? styles.accentIcon : g.status === "blocked" ? "text-red-500" : "text-stone-500"}`}>
                      {statusLabel[g.status]}
                    </span>
                  </div>
                ))}
              </div>
            </details>
          </div>
        </div>

        {/* Right: preview engine */}
        <div className="flex-1 space-y-6">
          <div className={`border rounded-xl p-6 relative overflow-hidden ${styles.card}`}>
            <div className={`flex items-center justify-between mb-4 pb-3 border-b ${styles.divider}`}>
              <h3 className={`font-semibold text-xs uppercase tracking-wider ${isDark ? "text-stone-300" : "text-stone-800"}`}>Preview Engine</h3>
              <span className="text-[10px] font-bold font-mono text-red-400 bg-red-950/40 px-2 py-0.5 rounded border border-red-500/20">MOCK ONLY • PRODUCTION DISABLED</span>
            </div>

            {allReady ? (
              <div className={`p-8 text-center space-y-6 rounded-lg border ${isDark ? "bg-stone-950 border-stone-900" : "bg-stone-50 border-stone-200"}`}>
                <div className={`w-16 h-16 rounded-full border flex items-center justify-center mx-auto ${isDark ? "bg-stone-900 border-amber-500/40 text-amber-400" : "bg-white border-[#8B1515]/25 text-[#8B1515]"}`}>
                  <ShieldCheck size={32} />
                </div>
                <div>
                  <h2 className={`text-2xl font-light ${styles.title}`}>Compliance Gates Cleared</h2>
                  <p className={`text-xs mt-2 max-w-md mx-auto leading-relaxed ${styles.body}`}>{appCopy.certificate.ready_body}</p>
                </div>
                <div className="pt-2">
                  <button onClick={() => setViewingMock(true)} className={`border font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-all ${styles.primaryButton}`}>
                    View Mock Certificate Preview
                  </button>
                </div>
              </div>
            ) : (
              <div className={`p-12 text-center space-y-6 rounded-lg border ${isDark ? "bg-stone-950 border-stone-900" : "bg-stone-50 border-stone-200"}`}>
                <div className={`w-12 h-12 rounded-full border flex items-center justify-center mx-auto ${isDark ? "bg-stone-900 border-stone-800 text-stone-600" : "bg-white border-stone-200 text-stone-500"}`}>
                  <Lock size={20} />
                </div>
                <div>
                  <h2 className={`text-lg font-semibold ${isDark ? "text-stone-300" : "text-stone-800"}`}>Certificate Status Locked</h2>
                  <p className="text-xs text-stone-500 max-w-sm mx-auto leading-relaxed mt-1">{appCopy.certificate.locked_body}</p>
                </div>
              </div>
            )}

            <div className={`mt-4 p-4 rounded border ${isDark ? "bg-[#0c0505] border-stone-900/60" : "bg-[#8B1515]/5 border-[#8B1515]/20"}`}>
              <p className={`text-xs leading-relaxed ${isDark ? "text-stone-400" : "text-stone-700"}`}>
                <strong>Legal Restriction:</strong> {appCopy.certificate.restriction}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
