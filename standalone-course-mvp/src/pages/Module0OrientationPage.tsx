import { useNavigate } from "react-router-dom";
import { CheckSquare, Square } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { paths } from "../app/routes";
import { BackLink, PrimaryButton } from "../components/v2/primitives";
import { appCopy } from "../data/contentV2Adapter";

type AckKey = "orientationFinalAck" | "phiAck" | "onlineCapAck";

const acks = appCopy.module0.acknowledgements as readonly { key: AckKey; text: string }[];

export function Module0OrientationPage() {
  const navigate = useNavigate();
  const { state, update } = useLearner();
  const allAgreed = acks.every((a) => state[a.key]);

  return (
    <div className="max-w-3xl mx-auto space-y-6">
      <BackLink to={paths.modules}>Back to Modules</BackLink>

      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-10 shadow-xl space-y-6">
        <div>
          <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-1 font-mono">{appCopy.module0.eyebrow}</div>
          <h1 className="text-3xl font-normal text-stone-100 tracking-tight">{appCopy.module0.title}</h1>
          <p className="text-xs text-stone-400 leading-relaxed mt-1">{appCopy.module0.intro}</p>
        </div>

        <div className="space-y-4 pt-4 border-t border-stone-800/60">
          <h3 className="text-xs uppercase tracking-wider font-bold text-stone-300">1. Verification of Legal CNA Identity</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <label className="block text-[10px] uppercase font-bold text-stone-500 mb-1 font-mono">First Name (Legal)</label>
              <input
                type="text"
                value={state.legalFirstName}
                onChange={(e) => update("legalFirstName", e.target.value)}
                className="w-full bg-[#080404] border border-stone-800 text-stone-100 text-xs px-3 py-2 rounded focus:outline-none focus:border-amber-500"
              />
            </div>
            <div>
              <label className="block text-[10px] uppercase font-bold text-stone-500 mb-1 font-mono">Last Name (Legal)</label>
              <input
                type="text"
                value={state.legalLastName}
                onChange={(e) => update("legalLastName", e.target.value)}
                className="w-full bg-[#080404] border border-stone-800 text-stone-100 text-xs px-3 py-2 rounded focus:outline-none focus:border-amber-500"
              />
            </div>
            <div>
              <label className="block text-[10px] uppercase font-bold text-stone-500 mb-1 font-mono">CNA Certificate Number</label>
              <input
                type="text"
                value={state.cnaNumber}
                onChange={(e) => update("cnaNumber", e.target.value)}
                className="w-full bg-[#080404] border border-stone-800 text-stone-100 text-xs px-3 py-2 rounded font-mono focus:outline-none focus:border-amber-500"
              />
            </div>
          </div>
        </div>

        <div className="space-y-3 pt-4 border-t border-stone-800/60">
          <h3 className="text-xs uppercase tracking-wider font-bold text-stone-300">2. Mandatory Declarations &amp; Acknowledgements</h3>
          {acks.map((ack) => {
            const checked = state[ack.key];
            return (
              <button
                key={ack.key}
                type="button"
                onClick={() => update(ack.key, !checked)}
                aria-pressed={checked}
                className={`w-full text-left p-4 rounded border flex items-start gap-3 transition-colors ${
                  checked ? "bg-[#1c0d0d] border-[#5c1111]/80 text-stone-100" : "bg-[#080404] border-stone-800 hover:border-stone-700 text-stone-400"
                }`}
              >
                <div className="mt-0.5 text-amber-500 shrink-0">{checked ? <CheckSquare size={16} /> : <Square size={16} />}</div>
                <p className="text-xs leading-relaxed">{ack.text}</p>
              </button>
            );
          })}
        </div>

        <div className="pt-6 border-t border-stone-800/60 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
          <div className="text-xs text-stone-500">{!allAgreed && "Select all 3 acknowledgements to proceed."}</div>
          <PrimaryButton
            disabled={!allAgreed}
            onClick={() => navigate(paths.modules)}
            className="font-bold"
          >
            Confirm &amp; Unlock Module 1
          </PrimaryButton>
        </div>
      </div>
    </div>
  );
}
