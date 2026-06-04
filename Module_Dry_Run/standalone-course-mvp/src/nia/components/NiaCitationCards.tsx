import { Quote } from "lucide-react";
import type { NiaCitation } from "../types";

// Compact citation/reference cards rendered under a Nia answer.
export function NiaCitationCards({ citations }: { citations: NiaCitation[] }) {
  if (!citations.length) return null;
  return (
    <div className="space-y-2">
      <div className="text-[9px] font-mono uppercase tracking-wider text-stone-500">Course references</div>
      {citations.map((cite) => (
        <div
          key={cite.id}
          className="bg-[#0c0606] border border-stone-800/80 rounded-lg p-3 flex gap-2.5"
        >
          <Quote size={13} className="text-amber-500/70 shrink-0 mt-0.5" />
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              <span className="text-xs font-semibold text-stone-100 truncate">{cite.title}</span>
              {cite.relevance === "primary" && (
                <span className="text-[8px] font-mono uppercase tracking-wider text-amber-400 border border-amber-500/25 rounded px-1">
                  primary
                </span>
              )}
            </div>
            <div className="text-[9px] font-mono uppercase tracking-wider text-stone-600 mt-0.5">{cite.locationLabel}</div>
            <p className="text-[11px] text-stone-400 mt-1 leading-relaxed">{cite.excerpt}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
