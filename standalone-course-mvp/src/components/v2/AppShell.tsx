import type { ReactNode } from "react";
import { TopNav } from "./TopNav";
import { ReviewerToolsPanel } from "./ReviewerToolsPanel";

const scrollbarCss = `
  .v2-root ::-webkit-scrollbar { width: 6px; height: 6px; background: transparent; }
  .v2-root ::-webkit-scrollbar-track { background: #080404; }
  .v2-root ::-webkit-scrollbar-thumb { background-color: #331212; border-radius: 3px; }
  .v2-root ::-webkit-scrollbar-thumb:hover { background-color: #5c1111; }
  .v2-root * { scrollbar-width: thin; scrollbar-color: #331212 #080404; }
`;

export function AppShell({ children }: { children: ReactNode }) {
  return (
    <div className="v2-root min-h-screen bg-[#080404] text-stone-100 font-sans flex flex-col relative overflow-x-hidden">
      <style dangerouslySetInnerHTML={{ __html: scrollbarCss }} />

      {/* Premium burgundy base gradient */}
      <div className="fixed inset-0 pointer-events-none bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#4a0d0d]/30 via-[#080404] to-[#080404] z-0" />

      <ReviewerToolsPanel />
      <TopNav />

      <main id="main-content" className="flex-1 w-full max-w-6xl mx-auto p-4 md:p-8 relative z-10 flex flex-col justify-start">
        {children}
      </main>

      <footer className="relative z-10 border-t border-stone-800/60 bg-[#0c0606]/70 px-6 py-4 text-[11px] text-stone-500 text-center no-print">
        No PHI. No CDPH approval claimed. Optional clinical support is non-gating and non-credit. Certificate surfaces are mock previews only.
      </footer>
    </div>
  );
}
