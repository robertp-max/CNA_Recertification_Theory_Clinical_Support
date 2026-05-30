import { useNavigate } from "react-router-dom";
import {
  Shield, ArrowRight, AlertTriangle, BookOpen, Stethoscope, ShieldAlert, CheckCircle2, Circle,
} from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { useUiState, formatHoursAndMins } from "../lib/uiState";
import { activeTimeMet, requiredTheoryComplete } from "../lib/moduleProgress";
import { requiredProgressPct } from "../lib/progress";
import { module0Complete } from "../lib/v2state";
import { paths } from "../app/routes";
import { PrimaryButton, SecondaryButton } from "../components/v2/primitives";
import { appCopy } from "../data/contentV2Adapter";

function StatusRow({ label, done, value }: { label: string; done?: boolean; value?: string }) {
  return (
    <div className="flex items-center justify-between text-xs">
      <span className="text-stone-500 font-medium">{label}</span>
      {value !== undefined ? (
        <span className="font-mono text-[11px] font-semibold text-amber-500">{value}</span>
      ) : (
        <span className={`flex items-center gap-1 ${done ? "text-amber-400" : "text-stone-600"}`}>
          {done ? <CheckCircle2 size={12} /> : <Circle size={12} />}
          {done ? "Complete" : "Pending"}
        </span>
      )}
    </div>
  );
}

export function DashboardPage() {
  const navigate = useNavigate();
  const { state } = useLearner();
  const { demoSeconds } = useUiState();

  const m0 = module0Complete(state);
  const theoryComplete = requiredTheoryComplete(state);
  const finalPassed = state.finalExamPassed;
  const timeMet = activeTimeMet(state);
  const overall = requiredProgressPct(state);

  return (
    <div className="space-y-6">
      {/* Hero banner */}
      <div className="bg-[#120909] border border-stone-800/60 rounded-xl p-6 md:p-10 shadow-xl relative overflow-hidden flex flex-col lg:flex-row gap-8 lg:items-center">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-96 h-96 rounded-full bg-amber-500/[0.02] blur-3xl pointer-events-none" />

        <div className="flex-1 relative z-10">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded bg-[#310c0c] border border-[#5c1111]/60 text-[11px] font-bold tracking-widest text-amber-500 uppercase mb-4">
            <Shield size={12} /> {appCopy.dashboard.badge}
          </div>
          <h1 className="text-3xl md:text-5xl font-normal text-stone-100 tracking-tight mb-4 leading-tight">{appCopy.dashboard.title}</h1>
          <p className="text-stone-400 text-sm md:text-base mb-6 max-w-xl leading-relaxed">
            {appCopy.dashboard.summary}
          </p>

          <div className="bg-amber-950/20 border border-amber-500/20 rounded-lg p-3.5 max-w-xl mb-6">
            <div className="flex items-start gap-2">
              <AlertTriangle size={14} className="text-amber-500 shrink-0 mt-0.5" />
              <p className="text-[11px] text-stone-400 leading-relaxed font-mono">
                <strong>Regulatory Compliance Notice:</strong> {appCopy.dashboard.compliance_notice}
              </p>
            </div>
          </div>

          <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
            {!m0 ? (
              <PrimaryButton onClick={() => navigate(paths.module0)}>
                Start Required Orientation <ArrowRight size={14} />
              </PrimaryButton>
            ) : (
              <PrimaryButton onClick={() => navigate(paths.modules)}>
                Resume Pathway <ArrowRight size={14} />
              </PrimaryButton>
            )}
            <SecondaryButton onClick={() => navigate(paths.modules)}>View All Modules</SecondaryButton>
          </div>
        </div>

        {/* Gate Review Status */}
        <div className="w-full lg:w-[320px] shrink-0 bg-[#0e0707] border border-stone-800/80 rounded-xl p-5 relative z-10">
          <div className="flex items-center justify-between mb-4 pb-3 border-b border-stone-800/60">
            <h3 className="font-semibold text-stone-300 text-xs uppercase tracking-wider">Gate Review Status</h3>
            <div className="flex items-center gap-1.5 text-amber-500 text-xs">
              <Shield size={14} />
              <span className="font-mono text-[11px] font-bold">12-HOUR CAP</span>
            </div>
          </div>

          <div className="space-y-3 mb-5">
            <StatusRow label="Orientation (Mod 0):" done={m0} />
            <StatusRow label="Active-Time (demo):" value={timeMet ? "12h 00m (demo)" : formatHoursAndMins(demoSeconds)} />
            <StatusRow label="Required Theory:" done={theoryComplete} />
            <StatusRow label="Final Assessment:" done={finalPassed} />
          </div>

          <div className="bg-stone-950 p-3 rounded border border-stone-900 mb-4">
            <div className="flex items-center justify-between text-[11px] mb-2">
              <span className="text-stone-500 uppercase font-bold">Required Progress</span>
              <span className="text-amber-500 font-bold font-mono">{overall}%</span>
            </div>
            <div className="w-full h-1.5 bg-stone-900 rounded-full overflow-hidden">
              <div className="h-full bg-amber-500 transition-all duration-500" style={{ width: `${overall}%` }} />
            </div>
            <p className="text-[10px] text-stone-600 mt-2 font-mono">Required CE only — optional clinical support excluded.</p>
          </div>

          <button
            onClick={() => navigate(paths.certificate)}
            className="w-full py-2 rounded bg-stone-900 hover:bg-stone-850 text-stone-200 font-semibold text-xs border border-stone-800 transition-colors uppercase tracking-wider"
          >
            Review Auditing Gates
          </button>
        </div>
      </div>

      {/* Three feature cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="p-6 rounded-xl bg-[#120909] border border-stone-800/80 flex flex-col justify-between">
          <div>
            <div className="text-amber-500 mb-3"><BookOpen size={20} /></div>
            <h4 className="text-sm font-semibold text-stone-200 uppercase tracking-wider mb-2">12-Hour Required Theory</h4>
            <p className="text-xs text-stone-400 leading-relaxed">
              {appCopy.dashboard.theory_card}
            </p>
          </div>
          <div className="mt-4 pt-3 border-t border-stone-900">
            <span className="text-[10px] text-stone-500 font-mono">STATUS: UNLOCKED SEQUENTIALLY</span>
          </div>
        </div>

        <div className="p-6 rounded-xl bg-[#120909] border border-stone-800/80 flex flex-col justify-between">
          <div>
            <div className="text-amber-500 mb-3"><Stethoscope size={20} /></div>
            <h4 className="text-sm font-semibold text-stone-200 uppercase tracking-wider mb-2">Optional Clinical Support</h4>
            <p className="text-xs text-stone-400 leading-relaxed">
              {appCopy.dashboard.clinical_card}
            </p>
          </div>
          <div className="mt-4 pt-3 border-t border-stone-900 flex justify-between items-center">
            <span className="text-[10px] text-stone-500 font-mono">STATUS: OPTIONAL · NON-GATING</span>
            <button onClick={() => navigate(paths.clinicalHub)} className="text-[10px] text-amber-500 hover:text-amber-400 font-bold uppercase tracking-wider">
              Enter Hub &rarr;
            </button>
          </div>
        </div>

        <div className="p-6 rounded-xl bg-[#120909] border border-stone-800/80 flex flex-col justify-between">
          <div>
            <div className="text-amber-500 mb-3"><ShieldAlert size={20} /></div>
            <h4 className="text-sm font-semibold text-stone-200 uppercase tracking-wider mb-2">Audit Safety Controls</h4>
            <p className="text-xs text-stone-400 leading-relaxed">
              {appCopy.dashboard.audit_card}
            </p>
          </div>
          <div className="mt-4 pt-3 border-t border-stone-900">
            <span className="text-[10px] text-red-500/80 font-mono font-semibold flex items-center gap-1">
              <ShieldAlert size={12} /> No-PHI Safeguards Active
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
