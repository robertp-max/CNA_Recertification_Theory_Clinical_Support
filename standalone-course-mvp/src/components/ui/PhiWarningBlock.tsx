import { StopCircle } from "lucide-react";

// Pinned, non-dismissible PHI warning. Must appear above every free-text / upload
// area. Copy is mandated and asserted by tests — do not change the wording.
export function PhiWarningBlock() {
  return (
    <div
      className="bg-[#1a0f0f] border border-red-900/50 rounded-lg p-4 flex items-start sm:items-center gap-3"
      role="note"
      aria-label="No protected health information warning"
    >
      <StopCircle size={20} className="text-red-500 shrink-0" aria-hidden="true" />
      <p className="text-sm font-bold text-red-200">
        STOP:{" "}
        <span className="font-normal text-red-100">
          Do not enter Protected Health Information (PHI), real patient names, or facility data.
          Use simulated case data only.
        </span>
      </p>
    </div>
  );
}
