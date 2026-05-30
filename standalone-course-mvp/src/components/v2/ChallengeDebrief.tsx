import { BookOpenCheck, ChevronDown, HeartPulse, ShieldCheck, Sparkles, UserCheck } from "lucide-react";
import type { LessonRemediation } from "../../data/remediation";

// Polished, course-extension "Challenge Debrief". This is a mini re-teaching
// section — never an answer-key reveal. Amber = Safest Response; muted burgundy
// = Needs Review. No bright green, no internal/answer-key language.

function Section({ icon, title, children }: { icon: React.ReactNode; title: string; children: React.ReactNode }) {
  return (
    <div className="space-y-1.5">
      <h4 className="text-[10px] uppercase font-bold text-stone-400 font-mono tracking-wider flex items-center gap-1.5">
        <span className="text-amber-500">{icon}</span>
        {title}
      </h4>
      <p className="text-xs text-stone-300 leading-relaxed">{children}</p>
    </div>
  );
}

export function ChallengeDebrief({
  remediation,
  selectedId,
  openedIds,
  onOpen,
}: {
  remediation: LessonRemediation;
  selectedId: string | null;
  openedIds: string[];
  onOpen: (id: string) => void;
}) {
  return (
    <div className="space-y-6">
      <div className="space-y-1">
        <span className="text-[10px] font-bold text-amber-500 uppercase tracking-widest font-mono flex items-center gap-1.5">
          <Sparkles size={12} /> {remediation.title}
        </span>
        <p className="text-[11px] text-stone-500 font-mono">{remediation.submittedNote}</p>
      </div>

      <div className="rounded-lg border border-amber-500/25 bg-amber-950/10 p-4 space-y-4">
        <Section icon={<ShieldCheck size={12} />} title="Safety Principle">
          {remediation.safetyPrinciple}
        </Section>

        <div className="rounded border border-amber-500/40 bg-amber-950/20 p-4 space-y-2">
          <div className="flex items-center gap-2">
            <span className="px-2 py-0.5 rounded text-[9px] font-mono font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40 uppercase tracking-wider">
              Safest Response
            </span>
          </div>
          <p className="text-sm text-stone-100 font-medium leading-relaxed">{remediation.safestResponseLabel}</p>
          <div className="pt-1">
            <h5 className="text-[10px] uppercase font-bold text-amber-400/90 font-mono tracking-wider mb-1">Why This Is Safest</h5>
            <p className="text-xs text-stone-300 leading-relaxed">{remediation.whySafest}</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="rounded border border-stone-800 bg-[#080404] p-4">
          <Section icon={<UserCheck size={12} />} title="CNA Scope Note">{remediation.cnaScopeNote}</Section>
        </div>
        <div className="rounded border border-stone-800 bg-[#080404] p-4">
          <Section icon={<HeartPulse size={12} />} title="Resident Safety Note">{remediation.residentSafetyNote}</Section>
        </div>
      </div>

      <div className="rounded border border-stone-800 bg-[#080404] p-4">
        <Section icon={<BookOpenCheck size={12} />} title="What to Remember">{remediation.whatToRemember}</Section>
      </div>

      <div className="space-y-3">
        <h4 className="text-xs uppercase font-bold text-stone-300 font-mono tracking-wider">Option Review</h4>
        <p className="text-[11px] text-stone-500 leading-relaxed">
          Open the safest response and your own choice to finish the debrief. Each option is a teaching point, not a graded answer.
        </p>
        <div className="space-y-2.5">
          {remediation.options.map((opt) => {
            const open = openedIds.includes(opt.id);
            const isSafest = opt.status === "safest";
            const isYours = selectedId === opt.id;
            return (
              <button
                key={opt.id}
                type="button"
                onClick={() => onOpen(opt.id)}
                className={`w-full text-left p-4 rounded border text-xs transition-all ${
                  open
                    ? isSafest
                      ? "bg-amber-950/15 border-amber-500/40"
                      : "bg-[#1a0a0a] border-[#5c1111]/50"
                    : "bg-stone-950/40 border-stone-900/70 opacity-80 hover:opacity-100"
                }`}
              >
                <div className="flex items-center justify-between gap-3 mb-1.5">
                  <div className="flex items-center gap-2 min-w-0">
                    <span
                      className={`px-2 py-0.5 rounded text-[9px] font-mono font-bold uppercase tracking-wider shrink-0 ${
                        isSafest
                          ? "bg-amber-500/20 text-amber-300 border border-amber-500/40"
                          : "bg-[#5c1111]/30 text-red-300/90 border border-[#5c1111]/50"
                      }`}
                    >
                      {isSafest ? "Safest Response" : "Needs Review"}
                    </span>
                    <span className="font-semibold text-stone-200 truncate">
                      {opt.id}. {opt.label}
                    </span>
                  </div>
                  <span className="flex items-center gap-1 text-[10px] text-stone-500 font-mono shrink-0">
                    {isYours && <span className="text-amber-500/80">Your choice</span>}
                    <ChevronDown size={13} className={`transition-transform ${open ? "rotate-180 text-amber-500" : ""}`} />
                  </span>
                </div>
                {open && (
                  <div className="space-y-2 pt-1.5 pl-1">
                    <p className="text-stone-300 leading-relaxed">{opt.why}</p>
                    <p className="text-[11px] text-stone-500 leading-relaxed">
                      <span className="font-semibold text-stone-400">Remember:</span> {opt.remember}
                    </p>
                  </div>
                )}
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
