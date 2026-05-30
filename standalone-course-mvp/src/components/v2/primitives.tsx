// Shared V2 visual primitives. Burgundy/charcoal system, gold only as a small
// accent. NO bright-green success states — "complete" reads as warm ivory + a
// small gold check; "pending" is muted stone; "locked" is subdued neutral;
// "remediation/fail" uses red (danger, never used to signal success).

import type { ButtonHTMLAttributes, ReactNode } from "react";
import { Link } from "react-router-dom";
import { ArrowLeft, CheckCircle2, Circle, Lock, AlertCircle } from "lucide-react";

function cx(...parts: Array<string | false | undefined>): string {
  return parts.filter(Boolean).join(" ");
}

type BtnProps = ButtonHTMLAttributes<HTMLButtonElement>;

export function PrimaryButton({ className, children, ...rest }: BtnProps) {
  return (
    <button
      {...rest}
      className={cx(
        "inline-flex items-center justify-center gap-2 bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-semibold px-6 py-3 rounded-lg transition-colors uppercase tracking-wider text-xs disabled:opacity-40 disabled:cursor-not-allowed",
        className,
      )}
    >
      {children}
    </button>
  );
}

export function SecondaryButton({ className, children, ...rest }: BtnProps) {
  return (
    <button
      {...rest}
      className={cx(
        "inline-flex items-center justify-center gap-2 bg-stone-900 hover:bg-stone-850 text-stone-300 border border-stone-800 font-semibold px-6 py-3 rounded-lg transition-colors uppercase tracking-wider text-xs disabled:opacity-40 disabled:cursor-not-allowed",
        className,
      )}
    >
      {children}
    </button>
  );
}

export function BackLink({ to, children }: { to: string; children: ReactNode }) {
  return (
    <Link
      to={to}
      className="text-stone-400 hover:text-stone-100 inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider"
    >
      <ArrowLeft size={14} /> {children}
    </Link>
  );
}

export type BadgeTone = "complete" | "action" | "locked" | "pending" | "remediation";

const badgeStyles: Record<BadgeTone, string> = {
  complete: "bg-stone-800/70 text-stone-100 border border-amber-500/25",
  action: "bg-amber-950/40 text-amber-400 border border-amber-500/20",
  locked: "bg-stone-950 text-stone-600 border border-stone-900",
  pending: "bg-stone-900 text-stone-400 border border-stone-800",
  remediation: "bg-red-950/30 text-red-300 border border-red-500/20",
};

export function StatusBadge({ tone, children }: { tone: BadgeTone; children: ReactNode }) {
  const Icon = tone === "complete" ? CheckCircle2 : tone === "locked" ? Lock : tone === "action" ? AlertCircle : Circle;
  return (
    <span
      className={cx(
        "inline-flex items-center gap-1 px-2.5 py-0.5 rounded text-[10px] font-semibold",
        badgeStyles[tone],
      )}
    >
      <Icon size={10} className={tone === "complete" ? "text-amber-400" : undefined} />
      {children}
    </span>
  );
}

export function ProgressBar({ pct }: { pct: number }) {
  const safe = Math.max(0, Math.min(100, pct));
  return (
    <div className="w-full h-1.5 bg-stone-900 rounded-full overflow-hidden">
      <div className="h-full bg-amber-500 transition-all duration-500" style={{ width: `${safe}%` }} />
    </div>
  );
}

/** Schematic 16:9 media placeholder. Real assets are not generated for the MVP. */
export function MediaPanel({ label, caption, children, className }: { label: string; caption: string; children?: ReactNode; className?: string }) {
  return (
    <div className={cx("w-full aspect-video bg-stone-950 border border-stone-900 rounded-lg flex flex-col items-center justify-center relative overflow-hidden", className)}>
      <div className="absolute top-3 left-3 bg-[#120909] border border-stone-800 rounded px-2 py-0.5 text-[9px] font-mono text-stone-400 uppercase tracking-wider">
        {label}
      </div>
      {children}
      <div className="text-[10px] font-mono text-stone-500 uppercase mt-2 tracking-widest px-4 text-center">{caption}</div>
    </div>
  );
}

export { cx };
