import { ShieldCheck } from "lucide-react";
import { niaHealth } from "../niaClient";

// Small status/debug surface. Defaults to a learner-friendly "Course-grounded
// MVP" label; pass `detailed` for the debug variant (record count + provider).
export function NiaStatusBadge({ detailed = false }: { detailed?: boolean }) {
  const health = niaHealth();
  const label = health.externalEnabled ? "Course-grounded + model assist" : "Course-grounded MVP";
  return (
    <span
      className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-[10px] font-semibold bg-stone-800/70 text-stone-100 border border-amber-500/25"
      title={detailed ? `${health.indexRecordCount} indexed references · provider: ${health.provider}` : label}
    >
      <ShieldCheck size={11} className="text-amber-400" />
      {detailed ? `${label} · ${health.indexRecordCount} refs · ${health.provider}` : label}
    </span>
  );
}
