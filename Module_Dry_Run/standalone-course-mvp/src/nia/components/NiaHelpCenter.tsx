import { BookOpen } from "lucide-react";

const SECTIONS: { title: string; body: string }[] = [
  {
    title: "What is Nia?",
    body:
      "Nia is a course-grounded student success coach for this CNA recertification course. Nia helps you understand where you are in the course, what to review next, why a gate may be locked, and how course topics connect to safe CNA practice.",
  },
  {
    title: "What Nia can help with",
    body:
      "Course navigation, module and lesson summaries, key terms, quiz and final-exam study readiness, the certificate gate, optional clinical support, the no-PHI rules, and CNA scope of practice.",
  },
  {
    title: "What Nia cannot do",
    body:
      "Nia cannot provide final exam answer keys, certify completion, issue certificates, grant clinical-hour credit, review real patient information, diagnose conditions, recommend treatment, or replace your instructor, employer, supervisor, licensed nurse, legal counsel, or CDPH guidance.",
  },
  {
    title: "No PHI",
    body:
      "Do not type real patient, resident, family, facility, chart, medical record, DOB, room number, or identifying details. Use fictional examples only (for example, \"Ms. Johnson\" or \"Mr. Park\").",
  },
  {
    title: "Certificate gate help",
    body:
      "A certificate can stay locked for required modules incomplete, final exam not passed, active-time/completion checks pending, or affidavit/approval metadata pending. Production certificate issuance remains disabled in this preview. Open the Certificate Gate for your specific status.",
  },
  {
    title: "Final exam study support",
    body:
      "Nia helps you study by topic: review the related modules, focus on weak areas, and use the module knowledge checks. Nia never reveals the answer key.",
  },
  {
    title: "Optional Clinical Support boundaries",
    body:
      "Optional Clinical Support is separate, optional, non-credit, and non-gating. It is not clinical-hour credit and does not validate hands-on competency. It is useful for skills refresh and confidence support.",
  },
  {
    title: "CNA scope reminders",
    body:
      "Observe, report, document, follow the care plan, communicate to licensed staff or a supervisor, and escalate concerns. Do not diagnose, treat, change medications, or stage pressure injuries as independent CNA authority.",
  },
  {
    title: "Example questions",
    body:
      "\"What should I do next?\" · \"What does Module 1 cover?\" · \"Does Clinical Support count for clinical hours?\" · \"Why is my certificate locked?\" · \"What should I review for vital signs?\" · \"What is CNA scope?\"",
  },
];

export function NiaHelpCenter() {
  return (
    <div className="space-y-3">
      <div className="flex items-center gap-1.5 text-[9px] font-mono uppercase tracking-wider text-amber-500/80">
        <BookOpen size={11} /> Nia Help Center
      </div>
      {SECTIONS.map((section) => (
        <div key={section.title} className="bg-[#0c0606] border border-stone-800/80 rounded-lg p-3">
          <h4 className="text-xs font-semibold text-stone-100">{section.title}</h4>
          <p className="text-[11px] text-stone-400 mt-1 leading-relaxed">{section.body}</p>
        </div>
      ))}
    </div>
  );
}
