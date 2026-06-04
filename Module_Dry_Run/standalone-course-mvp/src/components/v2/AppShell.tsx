import type { ReactNode } from "react";
import { useLocation } from "react-router-dom";
import { paths } from "../../app/routes";
import { useUiState } from "../../lib/uiState";
import { TopNav } from "./TopNav";
import { ReviewerToolsPanel } from "./ReviewerToolsPanel";
import { NiaCoach } from "../../nia/components/NiaCoachButton";

const shellCss = `
  .v2-root ::-webkit-scrollbar { width: 6px; height: 6px; background: transparent; }
  .v2-root[data-theme="dark"] ::-webkit-scrollbar-track { background: #080404; }
  .v2-root[data-theme="dark"] ::-webkit-scrollbar-thumb { background-color: #331212; border-radius: 3px; }
  .v2-root[data-theme="dark"] ::-webkit-scrollbar-thumb:hover { background-color: #5c1111; }
  .v2-root[data-theme="dark"] * { scrollbar-width: thin; scrollbar-color: #331212 #080404; }

  .v2-root[data-theme="normal"] ::-webkit-scrollbar-track { background: #f8f9fa; }
  .v2-root[data-theme="normal"] ::-webkit-scrollbar-thumb { background-color: #dee2e6; border-radius: 3px; }
  .v2-root[data-theme="normal"] ::-webkit-scrollbar-thumb:hover { background-color: #c8ccd0; }
  .v2-root[data-theme="normal"] * { scrollbar-width: thin; scrollbar-color: #dee2e6 #f8f9fa; }

  .v2-root[data-theme="normal"] { background: #f8f9fa; color: #212529; }

  /* Centralized light-theme remap for the existing dark MVP surface. */
  .v2-root[data-theme="normal"] .bg-\\[\\#080404\\],
  .v2-root[data-theme="normal"] .bg-\\[\\#0c0606\\],
  .v2-root[data-theme="normal"] .bg-\\[\\#120909\\],
  .v2-root[data-theme="normal"] .bg-\\[\\#0e0707\\],
  .v2-root[data-theme="normal"] .bg-stone-950,
  .v2-root[data-theme="normal"] .bg-stone-900,
  .v2-root[data-theme="normal"] .bg-stone-850 {
    background-color: #ffffff;
  }

  .v2-root[data-theme="normal"] .bg-\\[\\#1b1212\\],
  .v2-root[data-theme="normal"] .bg-\\[\\#1f0d0d\\],
  .v2-root[data-theme="normal"] .bg-\\[\\#310c0c\\] {
    background-color: #f8f9fa;
  }

  .v2-root[data-theme="normal"] .border-stone-900,
  .v2-root[data-theme="normal"] .border-stone-800,
  .v2-root[data-theme="normal"] .border-stone-800\\/60,
  .v2-root[data-theme="normal"] .border-stone-800\\/80,
  .v2-root[data-theme="normal"] .border-\\[\\#5c1111\\],
  .v2-root[data-theme="normal"] .border-\\[\\#8a1d1d\\] {
    border-color: #dee2e6;
  }

  .v2-root[data-theme="normal"] .text-stone-100,
  .v2-root[data-theme="normal"] .text-stone-200,
  .v2-root[data-theme="normal"] .text-stone-300 {
    color: #212529;
  }

  .v2-root[data-theme="normal"] .text-stone-400 { color: #495057; }
  .v2-root[data-theme="normal"] .text-stone-500,
  .v2-root[data-theme="normal"] .text-stone-600 { color: #6c757d; }

  .v2-root[data-theme="normal"] .text-amber-300,
  .v2-root[data-theme="normal"] .text-amber-400,
  .v2-root[data-theme="normal"] .text-amber-500 { color: #8b1515; }

  .v2-root[data-theme="normal"] .border-amber-500\\/20,
  .v2-root[data-theme="normal"] .border-amber-500\\/25,
  .v2-root[data-theme="normal"] .border-amber-500\\/40 {
    border-color: rgba(139, 21, 21, 0.18);
  }

  .v2-root[data-theme="normal"] .bg-amber-950\\/20,
  .v2-root[data-theme="normal"] .bg-amber-950\\/40 {
    background-color: rgba(139, 21, 21, 0.05);
  }

  .v2-root[data-theme="normal"] .bg-amber-500 { background-color: #ffc107; }
  .v2-root[data-theme="normal"] .bg-amber-500\\/\\[0\\.02\\] { background-color: rgba(139, 21, 21, 0.04); }

  .v2-root[data-theme="normal"] .hover\\:bg-stone-850:hover,
  .v2-root[data-theme="normal"] .hover\\:bg-stone-900:hover,
  .v2-root[data-theme="normal"] .hover\\:bg-stone-900\\/40:hover {
    background-color: #f1f3f5;
  }

  .v2-root[data-theme="normal"] .hover\\:text-stone-200:hover { color: #212529; }

  .v2-root[data-theme="normal"] .bg-\\[\\#5c1111\\],
  .v2-root[data-theme="normal"] .hover\\:bg-\\[\\#781616\\]:hover {
    background-color: #8b1515;
  }

  .v2-root[data-theme="normal"] .bg-\\[\\#5c1111\\].text-stone-100,
  .v2-root[data-theme="normal"] .hover\\:bg-\\[\\#781616\\]:hover.text-stone-100 {
    color: #ffffff;
  }

  .v2-root[data-theme="normal"] .reviewer-tools-root,
  .v2-root[data-theme="normal"] .reviewer-tools-root * {
    color-scheme: light;
  }
`;

export function AppShell({ children }: { children: ReactNode }) {
  const { pathname } = useLocation();
  const { brandingMode } = useUiState();
  const isDark = brandingMode === "dark";
  const hideNiaOnRoute = pathname === paths.moduleAssessmentQuiz || pathname === paths.finalQuiz;

  return (
    <div
      data-theme={brandingMode}
      className={`v2-root min-h-screen font-sans flex flex-col relative overflow-x-hidden ${isDark ? "bg-[#080404] text-stone-100" : "bg-[#F8F9FA] text-[#212529]"}`}
    >
      <style dangerouslySetInnerHTML={{ __html: shellCss }} />

      {/* Premium burgundy base gradient */}
      <div
        className={`fixed inset-0 pointer-events-none z-0 ${
          isDark
            ? "bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#4a0d0d]/30 via-[#080404] to-[#080404]"
            : "bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#8B1515]/[0.06] via-[#F8F9FA] to-[#F8F9FA]"
        }`}
      />

      <ReviewerToolsPanel />
      <TopNav />

      <div className="flex-1 w-full max-w-[1680px] mx-auto px-4 md:px-8 py-4 md:py-8 relative z-10">
        <div className="flex flex-col">
          <main
            id="main-content"
            className="w-full max-w-6xl mx-auto flex flex-col justify-start"
          >
            {children}
          </main>
        </div>
      </div>

      <NiaCoach />

      <footer
        className={`relative z-10 pointer-events-none border-t px-6 py-4 text-[11px] text-center no-print ${
          isDark
            ? "border-stone-800/60 bg-[#0c0606]/70 text-stone-500"
            : "border-[#DEE2E6] bg-white/80 text-stone-600"
        }`}
      >
        No PHI. No CDPH approval claimed. Optional clinical support is non-gating and non-credit. Certificate surfaces are mock previews only.
      </footer>
    </div>
  );
}
