import { ArrowUpRight, FileText, MapPin } from "lucide-react";
import type { NiaLinkedReference } from "../types";

const TYPE_LABELS: Record<NiaLinkedReference["type"], string> = {
  module: "Module",
  lesson: "Lesson",
  card: "Lesson card",
  assessment: "Assessment",
  clinical_support: "Clinical support (optional)",
  certificate_gate: "Certificate gate",
  course_policy: "Course policy",
  app_help: "App help",
};

// Expandable reference preview: title, type, app location, excerpt, and an
// optional open button when a route exists for the reference.
export function NiaReferencePreview({
  reference,
  onOpen,
  canOpen,
}: {
  reference: NiaLinkedReference;
  onOpen?: (reference: NiaLinkedReference) => void;
  canOpen?: boolean;
}) {
  return (
    <div className="bg-[#120909] border border-stone-800 rounded-lg p-3">
      <div className="flex items-start justify-between gap-2">
        <div className="min-w-0">
          <div className="flex items-center gap-1.5 text-[9px] font-mono uppercase tracking-wider text-amber-500/80">
            <FileText size={10} />
            {TYPE_LABELS[reference.type]}
            {reference.required && <span className="text-stone-500">· required</span>}
          </div>
          <h4 className="text-sm font-semibold text-stone-100 mt-1 truncate">{reference.title}</h4>
        </div>
        {canOpen && onOpen && (
          <button
            type="button"
            onClick={() => onOpen(reference)}
            className="shrink-0 inline-flex items-center gap-1 text-[10px] font-semibold uppercase tracking-wider text-amber-400 hover:text-amber-300 border border-amber-500/25 rounded px-2 py-1"
          >
            Open <ArrowUpRight size={11} />
          </button>
        )}
      </div>
      <p className="text-xs text-stone-400 mt-2 leading-relaxed">{reference.description}</p>
      {reference.appLocation && (
        <div className="flex items-center gap-1 text-[9px] font-mono text-stone-600 mt-2">
          <MapPin size={9} /> {reference.appLocation}
        </div>
      )}
    </div>
  );
}
