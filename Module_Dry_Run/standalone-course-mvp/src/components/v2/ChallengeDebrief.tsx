import { BookOpenCheck, ChevronDown, HeartPulse, ShieldCheck, Sparkles, UserCheck } from "lucide-react";
import type { LessonRemediation } from "../../data/remediation";
import { useUiState } from "../../lib/uiState";

// Polished, course-extension "Challenge Debrief". This is a mini re-teaching
// section — never an answer-key reveal. Amber = Safest Response; muted burgundy
// = Needs Review. No bright green, no internal/answer-key language.

function Section({ icon, title, children }: { icon: React.ReactNode; title: string; children: React.ReactNode }) {
  const { brandingMode } = useUiState();
  const isDark = brandingMode === "dark";
  return (
    <div className="space-y-1.5">
      <h4 className={`text-[10px] uppercase font-bold font-mono tracking-wider flex items-center gap-1.5 ${isDark ? "text-stone-400" : "text-stone-600"}`}>
        <span className={isDark ? "text-amber-500" : "text-[#8B1515]"}>{icon}</span>
        {title}
      </h4>
      <p className={`text-xs leading-relaxed ${isDark ? "text-stone-300" : "text-stone-700"}`}>{children}</p>
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
  const { brandingMode } = useUiState();
  const isDark = brandingMode === "dark";
  const styles = {
    heading: isDark ? "text-stone-400" : "text-stone-600",
    body: isDark ? "text-stone-300" : "text-stone-700",
    muted: isDark ? "text-stone-500" : "text-stone-500",
    title: isDark ? "text-stone-300" : "text-stone-800",
    accent: isDark ? "text-amber-500" : "text-[#8B1515]",
    teachingPanel: isDark ? "border-amber-500/25 bg-amber-950/10" : "border-[#8B1515]/20 bg-[#8B1515]/5",
    safestPanel: isDark ? "border-amber-500/40 bg-amber-950/20" : "border-[#8B1515]/25 bg-white",
    notePanel: isDark ? "border-stone-800 bg-[#080404]" : "border-stone-200 bg-stone-50",
    safestBadge: isDark ? "bg-amber-500/20 text-amber-300 border-amber-500/40" : "bg-[#8B1515]/10 text-[#8B1515] border-[#8B1515]/25",
    reviewBadge: isDark ? "bg-[#5c1111]/30 text-red-300/90 border-[#5c1111]/50" : "bg-red-50 text-red-700 border-red-200",
  };
  return (
    <div className="space-y-6">
      <div className="space-y-1">
        <span className={`text-[10px] font-bold uppercase tracking-widest font-mono flex items-center gap-1.5 ${styles.accent}`}>
          <Sparkles size={12} /> {remediation.title}
        </span>
        <p className={`text-[11px] font-mono ${styles.muted}`}>{remediation.submittedNote}</p>
      </div>

      <div className={`rounded-lg border p-4 space-y-4 ${styles.teachingPanel}`}>
        <Section icon={<ShieldCheck size={12} />} title="Safety Principle">
          {remediation.safetyPrinciple}
        </Section>

        <div className={`rounded border p-4 space-y-2 ${styles.safestPanel}`}>
          <div className="flex items-center gap-2">
            <span className={`px-2 py-0.5 rounded text-[9px] font-mono font-bold border uppercase tracking-wider ${styles.safestBadge}`}>
              Safest Response
            </span>
          </div>
          <p className={`text-sm font-medium leading-relaxed ${isDark ? "text-stone-100" : "text-stone-900"}`}>{remediation.safestResponseLabel}</p>
          <div className="pt-1">
            <h5 className={`text-[10px] uppercase font-bold font-mono tracking-wider mb-1 ${styles.accent}`}>Why This Is Safest</h5>
            <p className={`text-xs leading-relaxed ${styles.body}`}>{remediation.whySafest}</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className={`rounded border p-4 ${styles.notePanel}`}>
          <Section icon={<UserCheck size={12} />} title="CNA Scope Note">{remediation.cnaScopeNote}</Section>
        </div>
        <div className={`rounded border p-4 ${styles.notePanel}`}>
          <Section icon={<HeartPulse size={12} />} title="Resident Safety Note">{remediation.residentSafetyNote}</Section>
        </div>
      </div>

      <div className={`rounded border p-4 ${styles.notePanel}`}>
        <Section icon={<BookOpenCheck size={12} />} title="What to Remember">{remediation.whatToRemember}</Section>
      </div>

      <div className="space-y-3">
        <h4 className={`text-xs uppercase font-bold font-mono tracking-wider ${styles.title}`}>Option Review</h4>
        <p className={`text-[11px] leading-relaxed ${styles.muted}`}>
          Open every option explanation to finish the debrief. Each plausible choice teaches either the safest reasoning path or a common trap.
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
                      ? isDark
                        ? "bg-amber-950/15 border-amber-500/40"
                        : "bg-[#8B1515]/5 border-[#8B1515]/25"
                      : isDark
                        ? "bg-[#1a0a0a] border-[#5c1111]/50"
                        : "bg-red-50/70 border-red-200"
                    : isDark
                      ? "bg-stone-950/40 border-stone-900/70 opacity-80 hover:opacity-100"
                      : "bg-white border-stone-200 opacity-90 hover:opacity-100 hover:border-stone-300"
                }`}
              >
                <div className="flex items-center justify-between gap-3 mb-1.5">
                  <div className="flex items-center gap-2 min-w-0">
                    <span
                      className={`px-2 py-0.5 rounded text-[9px] font-mono font-bold uppercase tracking-wider shrink-0 border ${
                        isSafest ? styles.safestBadge : styles.reviewBadge
                      }`}
                    >
                      {isSafest ? "Safest Response" : "Needs Review"}
                    </span>
                    <span className={`font-semibold truncate ${isDark ? "text-stone-200" : "text-stone-800"}`}>
                      {opt.id}. {opt.label}
                    </span>
                  </div>
                  <span className={`flex items-center gap-1 text-[10px] font-mono shrink-0 ${styles.muted}`}>
                    {isYours && <span className={isDark ? "text-amber-500/80" : "text-[#8B1515]/80"}>Your choice</span>}
                    <ChevronDown size={13} className={`transition-transform ${open ? `rotate-180 ${styles.accent}` : ""}`} />
                  </span>
                </div>
                {open && (
                  <div className="space-y-2 pt-1.5 pl-1">
                    <p className={`leading-relaxed ${styles.body}`}>{opt.why}</p>
                    <p className={`text-[11px] leading-relaxed ${styles.muted}`}>
                      <span className={`font-semibold ${styles.heading}`}>Remember:</span> {opt.remember}
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
