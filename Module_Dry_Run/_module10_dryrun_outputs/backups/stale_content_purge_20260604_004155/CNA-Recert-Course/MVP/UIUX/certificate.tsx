import React from 'react';
import { 
  ArrowLeft, Download, Printer, Share2, Award, 
  ShieldCheck, CheckCircle2
} from 'lucide-react';

export default function App() {
  return (
    <div className="min-h-screen bg-[#0a0505] text-stone-200 font-sans selection:bg-amber-500/30 flex flex-col">
      {/* Global Scrollbar Override */}
      <style dangerouslySetInnerHTML={{__html: `
        ::-webkit-scrollbar { width: 4px; height: 4px; background: transparent; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background-color: #3b0b0b; border-radius: 0px; }
        ::-webkit-scrollbar-thumb:hover { background-color: #5c1212; }
        ::-webkit-scrollbar-button { display: none; }
        * { scrollbar-width: thin; scrollbar-color: #3b0b0b transparent; }
        
        /* Certificate specific print styles */
        @media print {
          body { background: #000; -webkit-print-color-adjust: exact; }
          .no-print { display: none; }
          .print-only { display: block; }
        }
      `}} />
      
      {/* Intense, premium burgundy radial gradient */}
      <div className="fixed inset-0 pointer-events-none bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#4a0f0f]/30 via-[#0a0505] to-[#0a0505] z-0 no-print"></div>

      {/* Global Navigation */}
      <header className="px-6 py-4 border-b border-white/5 bg-[#0d0707] relative z-20 flex items-center justify-between no-print">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-white/10 flex items-center justify-center border border-white/20">
            <span className="text-white font-bold text-xs">CI</span>
          </div>
          <span className="font-medium text-white tracking-wide text-sm hidden sm:block">INSTITUTE OF NURSING</span>
        </div>
        <div className="flex items-center gap-2 md:gap-6 text-sm font-medium text-stone-400">
          <button className="hover:text-white transition-colors">Dashboard</button>
          <button className="hover:text-white transition-colors">Modules</button>
          <button className="text-white bg-white/5 px-3 py-1.5 rounded-lg">Certificate</button>
          <div className="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-500 flex items-center justify-center border border-amber-500/30 ml-2 md:ml-4">
            <span className="text-xs font-bold">JD</span>
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 w-full max-w-6xl mx-auto p-4 md:p-8 lg:p-12 relative z-10 overflow-y-auto">
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 space-y-8 pb-12">
          
          {/* Page Header & Toolbar */}
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 no-print">
            <div>
              <button className="text-stone-400 hover:text-white flex items-center gap-2 text-sm transition-colors mb-6">
                <ArrowLeft size={16} /> Return to Dashboard
              </button>
              <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-3 flex items-center gap-2">
                <CheckCircle2 size={14} /> Formal Record of Completion
              </div>
              <h1 className="text-4xl font-semibold text-white tracking-tight mb-2">Your Certificate</h1>
              <p className="text-sm text-stone-400">Congratulations on completing the CNA Recertification Theory Pathway.</p>
            </div>
            
            <div className="flex items-center gap-3">
              <button className="px-5 py-2.5 rounded-xl text-stone-300 hover:text-white hover:bg-white/5 font-medium text-sm transition-all border border-white/10 flex items-center gap-2">
                <Share2 size={16} /> Share
              </button>
              <button className="px-5 py-2.5 rounded-xl text-stone-300 hover:text-white hover:bg-white/5 font-medium text-sm transition-all border border-white/10 flex items-center gap-2">
                <Printer size={16} /> Print
              </button>
              <button className="px-6 py-2.5 rounded-xl font-semibold text-sm flex items-center gap-2 transition-all bg-[#7a1212] hover:bg-[#5c0d0d] text-stone-100 border border-[#8f1818] shadow-lg">
                <Download size={16} /> Download PDF
              </button>
            </div>
          </div>

          {/* Certificate Container (Scrollable on small screens to maintain aspect ratio) */}
          <div className="w-full overflow-x-auto custom-scrollbar pb-8">
            <div className="min-w-[900px] max-w-[1100px] mx-auto">
              
              {/* THE CERTIFICATE */}
              <div className="relative w-full aspect-[11/8.5] bg-[#0c0606] shadow-[0_20px_50px_rgba(0,0,0,0.5)] overflow-hidden flex flex-col">
                
                {/* Background Textures / Gradient */}
                <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-[#2a0808]/20 via-transparent to-transparent pointer-events-none"></div>
                <div className="absolute inset-0 opacity-[0.02] bg-[url('https://www.transparenttextures.com/patterns/stardust.png')] pointer-events-none"></div>

                {/* The Watermark (Provided by User) */}
                <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
                  <img 
                    src="https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg" 
                    alt="Watermark" 
                    className="w-[45%] h-auto opacity-[0.04] grayscale brightness-200"
                  />
                </div>

                {/* Double Border Frame */}
                <div className="absolute inset-6 border-[3px] border-[#7a1212] rounded-sm pointer-events-none z-10"></div>
                <div className="absolute inset-8 border border-amber-500/40 rounded-sm pointer-events-none z-10"></div>
                <div className="absolute inset-[34px] border border-white/5 rounded-sm pointer-events-none z-10"></div>

                {/* Corner Accents (Gold) */}
                <div className="absolute top-7 left-7 w-4 h-4 border-t-2 border-l-2 border-amber-500 z-10"></div>
                <div className="absolute top-7 right-7 w-4 h-4 border-t-2 border-r-2 border-amber-500 z-10"></div>
                <div className="absolute bottom-7 left-7 w-4 h-4 border-b-2 border-l-2 border-amber-500 z-10"></div>
                <div className="absolute bottom-7 right-7 w-4 h-4 border-b-2 border-r-2 border-amber-500 z-10"></div>

                {/* Certificate Content */}
                <div className="relative z-20 flex-1 flex flex-col items-center justify-center p-16 text-center">
                  
                  {/* Top Logo / Name */}
                  <div className="mb-8 flex flex-col items-center gap-3">
                    <img 
                      src="https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg" 
                      alt="Logo" 
                      className="w-10 h-10 opacity-90"
                    />
                    <div className="tracking-[0.3em] text-xs uppercase text-amber-500 font-bold">
                      CI Institute of Nursing
                    </div>
                  </div>

                  <h1 className="font-serif text-5xl md:text-6xl text-stone-100 mb-4 tracking-wide font-medium drop-shadow-md">
                    Certificate of Completion
                  </h1>
                  
                  <div className="w-24 h-0.5 bg-gradient-to-r from-transparent via-amber-500/50 to-transparent mb-8"></div>

                  <p className="text-sm uppercase tracking-widest text-stone-400 mb-4 font-medium">
                    This is to certify that
                  </p>

                  <h2 className="font-serif text-5xl text-white mb-8 tracking-wide drop-shadow-lg text-shadow-gold">
                    James Bond
                  </h2>

                  <p className="text-sm text-stone-300 max-w-2xl leading-relaxed mb-12">
                    Has successfully completed the requirements for the <strong className="text-amber-500 font-semibold">24-Hour CNA Recertification Theory Pathway</strong>, demonstrating comprehensive knowledge in infection control, resident rights, safety, and professional documentation as required by state guidelines.
                  </p>

                  {/* Bottom Grid: Signatures & Seal & Details */}
                  <div className="w-full px-12 grid grid-cols-3 items-end">
                    
                    {/* Left: Date & Details */}
                    <div className="flex flex-col items-start text-left">
                      <div className="w-40 border-b border-white/20 pb-2 mb-2">
                        <span className="text-stone-200 text-lg font-serif">May 29, 2026</span>
                      </div>
                      <span className="text-[10px] uppercase tracking-widest text-stone-500 mb-3">Date of Completion</span>
                      
                      <div className="space-y-1">
                        <div className="text-[10px] text-stone-400"><span className="text-stone-500">CE Hours:</span> 24.0</div>
                        <div className="text-[10px] text-stone-400"><span className="text-stone-500">Cert ID:</span> ION-2026-98432</div>
                        <div className="text-[10px] text-stone-400"><span className="text-stone-500">CDPH NAC:</span> NAC-7654321</div>
                      </div>
                    </div>

                    {/* Center: The Seal */}
                    <div className="flex flex-col items-center justify-center">
                      <div className="relative flex items-center justify-center w-32 h-32">
                        {/* Outer jagged edge effect via rotated squares */}
                        <div className="absolute inset-0 bg-gradient-to-br from-amber-400 via-amber-600 to-amber-700 rotate-12 rounded opacity-20"></div>
                        <div className="absolute inset-0 bg-gradient-to-br from-amber-400 via-amber-600 to-amber-700 rotate-45 rounded opacity-20"></div>
                        <div className="absolute inset-2 border border-dashed border-amber-500 rounded-full animate-[spin_60s_linear_infinite]"></div>
                        <div className="absolute inset-3 border-2 border-[#7a1212] rounded-full bg-[#120a0a] flex flex-col items-center justify-center shadow-inner">
                           <ShieldCheck size={28} className="text-amber-500 mb-1" />
                           <span className="text-[7px] uppercase tracking-[0.2em] text-amber-500/80 font-bold font-serif text-center leading-tight">Official<br/>Record</span>
                        </div>
                      </div>
                    </div>

                    {/* Right: Signature */}
                    <div className="flex flex-col items-end text-right">
                      <div className="w-48 border-b border-white/20 pb-2 mb-2 flex justify-end">
                        {/* A cursive-style font approximation for the signature */}
                        <span className="text-stone-200 text-2xl font-serif italic pr-4" style={{ fontFamily: "'Brush Script MT', cursive, serif" }}>
                          Sarah Jenkins, RN
                        </span>
                      </div>
                      <span className="text-[10px] uppercase tracking-widest text-stone-500">Program Director</span>
                    </div>

                  </div>
                </div>

              </div>
              {/* END CERTIFICATE */}

            </div>
          </div>

        </div>
      </main>
    </div>
  );
}