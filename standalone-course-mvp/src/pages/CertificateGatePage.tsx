import { useState } from "react";
import { CheckCircle2, Circle, Lock, ShieldCheck } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { useUiState, formatHoursAndMins } from "../lib/uiState";
import { activeTimeMet, requiredTheoryComplete } from "../lib/moduleProgress";
import { summarizeGates, type GateStatus } from "../lib/gates";
import { MockCertificate } from "../components/v2/MockCertificate";
import { appCopy } from "../data/contentV2Adapter";

function GateRow({ done, locked, title, detail }: { done: boolean; locked?: boolean; title: string; detail: React.ReactNode }) {
  return (
    <div className="flex items-start gap-3 p-3 bg-[#080404] border border-stone-900 rounded">
      <div className="mt-0.5 shrink-0">
        {done ? <CheckCircle2 size={16} className="text-amber-400" /> : locked ? <Lock size={16} className="text-stone-600" /> : <Circle size={16} className="text-stone-600" />}
      </div>
      <div>
        <span className="text-[11px] font-bold text-stone-300 block uppercase font-mono">{title}</span>
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
  const { demoSeconds } = useUiState();
  const [viewingMock, setViewingMock] = useState(false);

  const legalReady = Boolean(state.legalFirstName.trim() && state.legalLastName.trim() && state.cnaNumber.trim());
  const hoursMet = activeTimeMet(state);
  const competency = requiredTheoryComplete(state) && state.finalExamPassed;
  const affidavit = state.affidavitComplete;
  const coreReady = legalReady && hoursMet && competency;
  const allReady = coreReady && affidavit;

  const summary = summarizeGates(state);

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
          <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6">
            <h2 className="text-lg font-semibold text-stone-200 mb-2 uppercase tracking-wider">{appCopy.certificate.checklist_title}</h2>
            <p className="text-xs text-stone-400 leading-relaxed mb-6">
              {appCopy.certificate.intro}
            </p>

            <div className="space-y-4">
              <GateRow done={legalReady} title="01. Legal Identity Verified" detail="Legal first/last name and CNA certificate number entered in Module 0." />
              <GateRow done={hoursMet} title="02. 12-Hour Study Time / Active-Time" detail={<>Active-time (demo / MVP — not CDPH-validated): <strong className="text-amber-500 font-mono font-normal">{hoursMet ? "12h 00m (demo)" : formatHoursAndMins(demoSeconds)}</strong></>} />
              <GateRow done={competency} title="03. Competency Achieved" detail="Required ContentV2 theory modules complete and final assessment passed." />

              {/* Affidavit (interactive once 1–3 met) */}
              <div className={`p-4 rounded border transition-colors ${affidavit ? "bg-stone-900/40 border-amber-500/20 text-stone-200" : "bg-[#1c0c0c]/40 border-[#5c1111]/30 text-stone-400"}`}>
                <div className="flex items-start gap-3">
                  <div className="mt-0.5 shrink-0">
                    {affidavit ? <CheckCircle2 size={16} className="text-amber-400" /> : <Circle size={16} className="text-[#5c1111]" />}
                  </div>
                  <div className="w-full">
                    <span className="text-[11px] font-bold block uppercase font-mono">04. Professional Affidavit</span>
                    <p className="text-[10px] text-stone-500 mt-1 mb-3">{appCopy.certificate.affidavit_text}</p>
                    {coreReady ? (
                      <button
                        onClick={() => update("affidavitComplete", !affidavit)}
                        className={`w-full py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-colors border ${affidavit ? "bg-stone-900 border-stone-800 text-stone-400" : "bg-[#5c1111] border-[#8a1d1d] hover:bg-[#781616] text-stone-100"}`}
                      >
                        {affidavit ? "Revoke Signature" : "Sign Draft Affidavit"}
                      </button>
                    ) : (
                      <span className="text-[9px] text-stone-600 uppercase font-mono font-bold block">Locked (Complete Steps 1–3 first)</span>
                    )}
                  </div>
                </div>
              </div>
            </div>

            {/* Deeper compliance gate detail (preserved engine) */}
            <details className="mt-6 group">
              <summary className="cursor-pointer text-[10px] uppercase font-bold text-stone-400 font-mono tracking-wider hover:text-stone-200">
                Full compliance gate detail ({summary.passingCount}/{summary.totalCount} certificate gates met)
              </summary>
              <div className="mt-3 space-y-1.5">
                {summary.gates.map((g) => (
                  <div key={g.key} className="flex items-center justify-between gap-3 text-[10px] border-b border-stone-900/80 pb-1.5">
                    <span className="text-stone-400">
                      {g.label}
                      {g.simulated ? <span className="text-amber-500/70"> (simulated)</span> : null}
                      {!g.affectsCertificate ? <span className="text-stone-600"> · non-gating</span> : null}
                    </span>
                    <span className={`font-mono shrink-0 ${g.status === "complete" ? "text-amber-400" : g.status === "blocked" ? "text-red-400" : "text-stone-500"}`}>
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
          <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 relative overflow-hidden">
            <div className="flex items-center justify-between mb-4 pb-3 border-b border-stone-800/60">
              <h3 className="font-semibold text-stone-300 text-xs uppercase tracking-wider">Preview Engine</h3>
              <span className="text-[10px] font-bold font-mono text-red-400 bg-red-950/40 px-2 py-0.5 rounded border border-red-500/20">MOCK ONLY • PRODUCTION DISABLED</span>
            </div>

            {allReady ? (
              <div className="p-8 text-center space-y-6 bg-stone-950 rounded-lg border border-stone-900">
                <div className="w-16 h-16 rounded-full bg-stone-900 border border-amber-500/40 flex items-center justify-center mx-auto text-amber-400">
                  <ShieldCheck size={32} />
                </div>
                <div>
                  <h2 className="text-2xl font-light text-stone-200">Compliance Gates Cleared</h2>
                  <p className="text-xs text-stone-400 mt-2 max-w-md mx-auto leading-relaxed">{appCopy.certificate.ready_body}</p>
                </div>
                <div className="pt-2">
                  <button onClick={() => setViewingMock(true)} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-all">
                    View Mock Certificate Preview
                  </button>
                </div>
              </div>
            ) : (
              <div className="p-12 text-center space-y-6 bg-stone-950 rounded-lg border border-stone-900">
                <div className="w-12 h-12 rounded-full bg-stone-900 border border-stone-800 flex items-center justify-center mx-auto text-stone-600">
                  <Lock size={20} />
                </div>
                <div>
                  <h2 className="text-lg font-semibold text-stone-300">Certificate Status Locked</h2>
                  <p className="text-xs text-stone-500 max-w-sm mx-auto leading-relaxed mt-1">{appCopy.certificate.locked_body}</p>
                </div>
              </div>
            )}

            <div className="mt-4 p-4 rounded bg-[#0c0505] border border-stone-900/60">
              <p className="text-xs text-stone-400 leading-relaxed">
                <strong>Legal Restriction:</strong> {appCopy.certificate.restriction}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
