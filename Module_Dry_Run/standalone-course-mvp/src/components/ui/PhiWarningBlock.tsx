import { StopCircle } from "lucide-react";
import type { BrandingMode } from "../../lib/uiState";

// Pinned, non-dismissible PHI warning. Must appear above every free-text / upload
// area. Copy is mandated and asserted by tests — do not change the wording.
export function PhiWarningBlock({ brandingMode = "dark" }: { brandingMode?: BrandingMode }) {
  const isDark = brandingMode === "dark";
  return (
    <div
      className={`border rounded-lg p-4 flex items-start sm:items-center gap-3 ${
        isDark ? "bg-[#1a0f0f] border-red-900/50" : "bg-red-50 border-red-200"
      }`}
      role="note"
      aria-label="No protected health information warning"
    >
      <StopCircle size={20} className="text-red-500 shrink-0" aria-hidden="true" />
      <p className={`text-sm font-bold ${isDark ? "text-red-200" : "text-red-800"}`}>
        STOP:{" "}
        <span className={`font-normal ${isDark ? "text-red-100" : "text-red-700"}`}>
          Do not enter Protected Health Information (PHI), real patient names, or facility data.
          Use simulated case data only.
        </span>
      </p>
    </div>
  );
}
