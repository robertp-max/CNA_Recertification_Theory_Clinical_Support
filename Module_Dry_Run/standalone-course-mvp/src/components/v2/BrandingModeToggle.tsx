import { Moon, Sun } from "lucide-react";
import { useUiState } from "../../lib/uiState";

export function BrandingModeToggle({ className = "" }: { className?: string }) {
  const { brandingMode, setBrandingMode } = useUiState();
  const isDark = brandingMode === "dark";

  return (
    <button
      type="button"
      onClick={() => setBrandingMode(isDark ? "normal" : "dark")}
      aria-label="Toggle dark and normal mode"
      title={isDark ? "Switch to normal mode" : "Switch to dark mode"}
      className={`inline-flex items-center justify-center w-9 h-9 rounded-lg border transition-colors shrink-0 ${
        isDark
          ? "border-[#3a2120] bg-[#120909] text-amber-400 hover:bg-[#1a0e0e]"
          : "border-[#DEE2E6] bg-white text-[#8B1515] hover:bg-stone-50 shadow-sm"
      } ${className}`}
    >
      {isDark ? <Sun size={16} /> : <Moon size={16} />}
    </button>
  );
}
