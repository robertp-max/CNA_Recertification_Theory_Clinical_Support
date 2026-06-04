import React, { useState } from 'react';
import { 
  ArrowLeft, Download, Printer, Share2, ShieldCheck, 
  CheckCircle2, Lock, AlertTriangle, Clock, AlertCircle, 
  FileCheck, Shield, FileText, Ban, Eye, XCircle, Info, ArrowRight,
  ShieldAlert, Check, Circle
} from 'lucide-react';

export default function App() {
  const [readinessState, setReadinessState] = useState('review'); 
  // States: 'locked', 'review', 'ready'
  
  const [viewingCertificate, setViewingCertificate] = useState(false);

  return (
    <div className="min-h-screen bg-[#0a0505] text-stone-200 font-sans selection:bg-amber-500/30 flex flex-col">
      {/* Global Scrollbar Override & Print Styles */}
      <style dangerouslySetInnerHTML={{__html: `
        ::-webkit-scrollbar { width: 4px; height: 4px; background: transparent; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background-color: #3b0b0b; border-radius: 0px; }
        ::-webkit-scrollbar-thumb:hover { background-color: #5c1212; }
        ::-webkit-scrollbar-button { display: none; }
        * { scrollbar-width: thin; scrollbar-color: #3b0b0b transparent; }
        
        @media print {
          body { background: #000; -webkit-print-color-adjust: exact; }
          .no-print { display: none !important; }
          .print-only { display: block; }
        }
      `}} />
      
      <div className="fixed inset-0 pointer-events-none bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#4a0f0f]/20 via-[#0a0505] to-[#0a0505] z-0 no-print"></div>

      {/* DEV NAVIGATION - For Reviewing States */}
      {!viewingCertificate && (
        <div className="bg-amber-500/10 border-b border-amber-500/20 px-4 py-2 flex items-center justify-center gap-4 relative z-50 text-xs overflow-x-auto whitespace-nowrap no-print">
          <span className="font-bold text-amber-500 uppercase tracking-widest mr-2">Dev Toggle:</span>
          <button onClick={() => setReadinessState('locked')} className={readinessState === 'locked' ? 'text-white font-bold' : 'text-stone-400 hover:text-stone-200'}>STATE 1: Locked</button>
          <span className="text-stone-700">|</span>
          <button onClick={() => setReadinessState('review')} className={readinessState === 'review' ? 'text-white font-bold' : 'text-stone-400 hover:text-stone-200'}>STATE 2: Gate Review</button>
          <span className="text-stone-700">|</span>
          <button onClick={() => setReadinessState('ready')} className={readinessState === 'ready' ? 'text-white font-bold' : 'text-stone-400 hover:text-stone-200'}>STATE 3: Preview Ready</button>
        </div>
      )}

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
          <button className="text-white bg-white/5 px-3 py-1.5 rounded-lg border border-white/10">Certificate</button>
          <div className="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-500 flex items-center justify-center border border-amber-500/30 ml-2 md:ml-4">
            <span className="text-xs font-bold">JD</span>
          </div>
        </div>
      </header>

      {/* Main Content Router */}
      <main className="flex-1 w-full max-w-7xl mx-auto relative z-10 overflow-y-auto">
        {viewingCertificate ? (
          <CertificatePreview onClose={() => setViewingCertificate(false)} readinessState={readinessState} />
        ) : (
          <CertificateHub 
            readinessState={readinessState} 
            onOpenPreview={() => setViewingCertificate(true)} 
          />
        )}
      </main>
    </div>
  );
}

// ==========================================
// MAIN HUB: STATUS & GATE REVIEW
// ==========================================
function CertificateHub({ readinessState, onOpenPreview }) {
  return (
    <div className="p-4 md:p-8 lg:p-12 animate-in fade-in slide-in-from-bottom-4 duration-500 pb-24">
      <div className="mb-8">
        <button className="text-stone-400 hover:text-white flex items-center gap-2 text-sm transition-colors mb-6">
          <ArrowLeft size={16} /> Return to Dashboard
        </button>
        <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-2">Compliance Hub</div>
        <h1 className="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-2">
          {readinessState === 'locked' && 'Certificate Status'}
          {readinessState === 'review' && 'Certificate Gate Review'}
          {readinessState === 'ready' && 'Certificate Preview Ready'}
        </h1>
        <p className="text-sm text-stone-400 max-w-2xl">
          {readinessState === 'locked' && 'Your online CE certificate preview is locked until all required certificate steps are complete.'}
          {readinessState === 'review' && 'Review your required completion gates. The certificate preview remains locked until all learner steps are complete.'}
          {readinessState === 'ready' && 'Your required learner steps are complete. Production certificate issuance remains disabled until approval metadata and active-time validation are approved.'}
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        {/* LEFT COLUMN: Main Gates */}
        <div className="lg:col-span-8 space-y-6">
          
          {/* Hero Status Card based on State */}
          {readinessState === 'locked' && (
            <div className="bg-[#120a0a] border border-white/5 rounded-xl p-8 shadow-xl flex items-start gap-6">
              <div className="w-16 h-16 rounded-full bg-black/40 border border-white/10 flex items-center justify-center shrink-0">
                <Lock size={32} className="text-stone-500" />
              </div>
              <div>
                <h2 className="text-2xl font-semibold text-stone-200 mb-2">Certificate Locked</h2>
                <p className="text-stone-400 text-sm leading-relaxed mb-6">
                  Your certificate cannot be released yet because required certificate gates are incomplete or approval metadata is pending.
                </p>
                <div className="flex flex-wrap gap-4">
                  <button className="px-6 py-3 rounded-xl font-semibold text-sm transition-all bg-[#7a1212] hover:bg-[#5c0d0d] text-stone-100 border border-[#8f1818] shadow-lg">
                    Review Certificate Gates
                  </button>
                  <button className="px-6 py-3 rounded-xl font-medium text-sm transition-all bg-white/5 hover:bg-white/10 text-white border border-white/10">
                    Return to Dashboard
                  </button>
                </div>
              </div>
            </div>
          )}

          {readinessState === 'ready' && (
            <div className="bg-[#120a0a] border border-amber-500/20 rounded-xl p-8 shadow-xl flex items-start gap-6">
              <div className="w-16 h-16 rounded-full bg-amber-500/10 border border-amber-500/20 flex items-center justify-center shrink-0">
                <ShieldCheck size={32} className="text-amber-500" />
              </div>
              <div>
                <h2 className="text-2xl font-semibold text-stone-200 mb-2">Preview Available</h2>
                <p className="text-stone-400 text-sm leading-relaxed mb-6">
                  All learner steps are complete. Production certificate issuance is disabled pending administrative review. You may view a mock preview of your certificate.
                </p>
                <div className="flex flex-wrap gap-4">
                  <button 
                    onClick={onOpenPreview}
                    className="px-6 py-3 rounded-xl font-semibold text-sm transition-all bg-[#7a1212] hover:bg-[#5c0d0d] text-stone-100 border border-[#8f1818] shadow-lg flex items-center gap-2"
                  >
                    <Eye size={16} /> Preview Certificate
                  </button>
                  <button disabled className="px-6 py-3 rounded-xl font-medium text-sm transition-all bg-black/40 text-stone-600 border border-white/5 cursor-not-allowed">
                    Issue Production Certificate
                  </button>
                </div>
                <div className="mt-4 text-[10px] uppercase tracking-widest text-amber-500/80 font-bold flex items-center gap-1.5">
                  <AlertTriangle size={12} /> Production Issuance Disabled
                </div>
              </div>
            </div>
          )}

          {/* Gate Review Checklist */}
          <div className="bg-[#120a0a] border border-white/5 rounded-xl shadow-xl overflow-hidden">
            <div className="px-6 py-4 border-b border-white/5 bg-black/20 flex items-center justify-between">
              <h3 className="text-xs font-bold uppercase tracking-widest text-stone-500">Certificate Readiness Gates</h3>
            </div>
            
            <div className="divide-y divide-white/5">
              <GateRow 
                name="Approval Metadata"
                explanation="Provider/course approval, NAC#, approved course list, certificate wording, and affidavit method must be documented before production issuance."
                status={readinessState === 'ready' ? 'pending' : 'blocked'}
                evidence="Admin approval archive"
                adminNote={readinessState === 'ready' ? "Pending CDPH letter upload." : null}
              />
              <GateRow 
                name="Legal Name"
                explanation="Legal name must be present for certificate identity."
                status="complete"
                evidence="Learner profile"
              />
              <GateRow 
                name="CNA Certificate Number"
                explanation="CNA certificate number must be present before certificate release."
                status="complete"
                evidence="Learner profile"
              />
              <GateRow 
                name="Online CE Cap Acknowledgement"
                explanation="Learner must acknowledge the California online CE cap."
                status="complete"
                evidence="Orientation acknowledgement"
              />
              <GateRow 
                name="Required Online CE Theory Completion"
                explanation="Required theory modules and required lesson interactions must be complete."
                status={readinessState === 'locked' ? 'pending' : 'complete'}
                evidence="Module and lesson completion records"
                actionText={readinessState === 'locked' ? "Continue Modules" : null}
              />
              <GateRow 
                name="Required Interaction and Feedback Completion"
                explanation="Required knowledge checks, scenario checks, or equivalent interactions must be complete."
                status={readinessState === 'locked' ? 'pending' : 'complete'}
                evidence="Interaction attempt records"
              />
              <GateRow 
                name="Active-Time Requirement"
                explanation="Active participation time must meet the required threshold."
                status={readinessState === 'locked' ? 'pending' : 'complete'}
                evidence="Active-time engine/report"
                truthLabel="MVP active-time engine — demo threshold, not CDPH-validated."
              />
              <GateRow 
                name="Final Course Assessment"
                explanation="Final assessment must be passed before final statement and certificate preview."
                status={readinessState === 'locked' ? 'locked' : readinessState === 'review' ? 'pending' : 'complete'}
                evidence="Final assessment attempt and score summary"
                actionText={readinessState === 'review' ? "Begin Assessment" : null}
              />
              <GateRow 
                name="Final Statement / Affidavit"
                explanation="Learner must complete the final signed statement before certificate release."
                status={readinessState === 'ready' ? 'complete' : 'locked'}
                evidence="Final statement/affidavit record"
                truthLabel="E-signature method pending legal/CDPH confirmation unless approved."
              />
              <GateRow 
                name="Certificate Fields"
                explanation="Required certificate fields must be available and mapped correctly."
                status="complete"
                evidence="Certificate template field map and learner profile"
              />
              <GateRow 
                name="Admin Hold"
                explanation="Certificate cannot release if an admin hold is active."
                status="complete"
                evidence="Restricted admin hold record"
              />
              <GateRow 
                name="Manual Override"
                explanation="Any override must be authorized and fully documented."
                status="na"
                evidence="Manual override log"
              />
            </div>
          </div>

          <div className="bg-[#1a0f0f] border border-white/5 rounded-xl p-5 flex items-start gap-4 shadow-sm">
            <Info size={20} className="text-stone-500 shrink-0 mt-0.5" />
            <div>
              <h4 className="text-xs font-bold uppercase tracking-widest text-stone-400 mb-1">Optional Clinical Support</h4>
              <p className="text-xs text-stone-500 leading-relaxed">
                Optional Clinical Support is separate from the online CE certificate. Skipping optional clinical support does not block certificate readiness if all required online CE certificate gates are complete.
              </p>
            </div>
          </div>
        </div>

        {/* RIGHT COLUMN: Sidebar (Audit & Mini Preview) */}
        <div className="lg:col-span-4 space-y-6">
          
          {/* Mini Certificate Preview */}
          <div className="bg-[#120a0a] border border-white/5 rounded-xl overflow-hidden shadow-xl">
             <div className="px-5 py-4 border-b border-white/5 bg-black/20 flex items-center justify-between">
              <h3 className="text-xs font-bold uppercase tracking-widest text-stone-500">Preview</h3>
            </div>
            <div className="p-5">
              <div className="aspect-[11/8.5] border border-white/10 rounded bg-[#0c0606] relative overflow-hidden flex flex-col items-center justify-center group cursor-pointer" onClick={readinessState === 'ready' ? onOpenPreview : undefined}>
                <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-[#2a0808]/20 via-transparent to-transparent pointer-events-none"></div>
                {readinessState === 'ready' ? (
                  <>
                    <img src="https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg" alt="Logo" className="w-8 h-8 opacity-50 mb-2" />
                    <span className="text-[8px] uppercase tracking-[0.2em] text-amber-500 font-bold border-b border-amber-500/30 pb-1 mb-1">Certificate of Completion</span>
                    <span className="text-xs font-serif text-white">James Bond</span>
                    <div className="absolute inset-0 bg-black/60 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                      <span className="text-white text-xs font-medium flex items-center gap-2 bg-black/80 px-4 py-2 rounded-full border border-white/10"><Eye size={14} /> Open Preview</span>
                    </div>
                  </>
                ) : (
                  <>
                    <Lock size={32} className="text-stone-700 mb-3" />
                    <span className="text-[10px] uppercase tracking-widest text-stone-600 font-bold">Preview Locked</span>
                  </>
                )}
              </div>
            </div>
          </div>

          {/* Certificate Audit Evidence Panel */}
          <div className="bg-[#120a0a] border border-white/5 rounded-xl shadow-xl overflow-hidden">
            <div className="px-5 py-4 border-b border-white/5 bg-black/20 flex items-center gap-2">
              <FileCheck size={16} className="text-amber-500" />
              <h3 className="text-xs font-bold uppercase tracking-widest text-stone-300">Audit Evidence Panel</h3>
            </div>
            <div className="p-5 space-y-4">
              <EvidenceItem label="Learner profile fields" present />
              <EvidenceItem label="Identity confirmation" present />
              <EvidenceItem label="Online cap acknowledgement" present />
              <EvidenceItem label="Required theory completion" present={readinessState !== 'locked'} />
              <EvidenceItem label="Required interaction records" present={readinessState !== 'locked'} />
              <EvidenceItem label="Active-time report" present={readinessState !== 'locked'} />
              <EvidenceItem label="Final assessment attempt & score" present={readinessState === 'ready'} />
              <EvidenceItem label="Final statement / affidavit" present={readinessState === 'ready'} />
              <EvidenceItem label="Certificate preview PDF" present={readinessState === 'ready'} />
              <EvidenceItem label="Approval metadata" present={false} />
              
              <div className="pt-4 border-t border-white/5">
                <h4 className="text-[10px] uppercase tracking-widest text-stone-600 font-bold mb-2">Optional Records</h4>
                <EvidenceItem label="Optional clinical support records" present={false} mute />
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}

// Subcomponents for Hub
function GateRow({ name, explanation, status, evidence, actionText, adminNote, truthLabel }) {
  const getStatusConfig = () => {
    switch(status) {
      case 'complete': return { icon: <CheckCircle2 size={18} className="text-green-500" />, text: 'Complete', color: 'text-stone-300' };
      case 'pending': return { icon: <Clock size={18} className="text-amber-500" />, text: 'Needs Review', color: 'text-amber-500' };
      case 'blocked': return { icon: <ShieldAlert size={18} className="text-[#9E1A2F]" />, text: 'Blocked', color: 'text-[#9E1A2F]' };
      case 'locked': return { icon: <Lock size={18} className="text-stone-600" />, text: 'Locked', color: 'text-stone-500' };
      case 'na': return { icon: <Ban size={18} className="text-stone-700" />, text: 'Not Applicable', color: 'text-stone-600' };
      default: return { icon: <Circle size={18} className="text-stone-600" />, text: 'Unknown', color: 'text-stone-500' };
    }
  };

  const config = getStatusConfig();

  return (
    <div className="p-6 flex flex-col sm:flex-row gap-6 hover:bg-white/[0.02] transition-colors">
      <div className="flex-1 space-y-2">
        <div className="flex items-center gap-3">
          {config.icon}
          <h4 className="text-sm font-semibold text-stone-200">{name}</h4>
          <span className={`text-[10px] uppercase tracking-widest font-bold ${config.color} border border-current px-2 py-0.5 rounded-sm opacity-80`}>
            {config.text}
          </span>
        </div>
        <p className="text-sm text-stone-400 leading-relaxed pl-8">{explanation}</p>
        <div className="pl-8 pt-1 flex items-center gap-2">
          <FileText size={14} className="text-stone-600" />
          <span className="text-xs text-stone-500"><strong className="font-medium text-stone-400">Evidence:</strong> {evidence}</span>
        </div>
        {truthLabel && (
          <div className="pl-8 pt-1">
            <span className="inline-block bg-black/40 border border-white/5 text-[10px] text-stone-500 px-2 py-1 rounded italic">
              {truthLabel}
            </span>
          </div>
        )}
      </div>
      
      {(actionText || adminNote) && (
        <div className="sm:w-48 shrink-0 flex flex-col justify-center border-t sm:border-t-0 sm:border-l border-white/5 pt-4 sm:pt-0 sm:pl-6">
          {actionText && (
            <button className="w-full px-4 py-2 rounded-lg font-medium text-xs transition-all bg-[#7a1212] hover:bg-[#5c0d0d] text-stone-100 border border-[#8f1818] text-center shadow-sm">
              {actionText}
            </button>
          )}
          {adminNote && (
            <div className="bg-[#1a0f0f] border border-red-900/30 rounded p-2 mt-2">
              <span className="text-[9px] uppercase tracking-widest text-stone-500 font-bold block mb-0.5">Admin Note</span>
              <p className="text-[10px] text-red-300/80 leading-snug">{adminNote}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

function EvidenceItem({ label, present, mute }) {
  return (
    <div className={`flex items-start gap-3 ${mute ? 'opacity-50' : ''}`}>
      {present ? (
        <Check size={16} className="text-green-500 shrink-0 mt-0.5" />
      ) : (
        <Circle size={16} className="text-stone-700 shrink-0 mt-0.5" />
      )}
      <span className={`text-xs ${present ? 'text-stone-300' : 'text-stone-500'}`}>{label}</span>
    </div>
  );
}

// ==========================================
// FORMAL CERTIFICATE PREVIEW
// ==========================================
function CertificatePreview({ onClose, readinessState }) {
  return (
    <div className="min-h-screen bg-[#0a0505] p-4 md:p-8 animate-in fade-in duration-500 flex flex-col">
      
      {/* Top Bar */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-8 max-w-[1100px] mx-auto w-full no-print">
        <div className="flex items-center gap-4">
          <button onClick={onClose} className="p-2 bg-white/5 hover:bg-white/10 rounded-lg text-stone-400 hover:text-white transition-colors">
            <XCircle size={20} />
          </button>
          <div>
            <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-1">Formal Record of Completion</div>
            <h1 className="text-2xl font-semibold text-white tracking-tight">Certificate Preview</h1>
          </div>
        </div>
        <div className="flex items-center gap-3">
          <button className="px-5 py-2.5 rounded-xl text-stone-300 hover:text-white hover:bg-white/5 font-medium text-sm transition-all border border-white/10 flex items-center gap-2">
            <Download size={16} /> Download Mock Preview
          </button>
          <button disabled className="px-6 py-2.5 rounded-xl font-semibold text-sm flex items-center gap-2 transition-all bg-black/40 text-stone-600 border border-white/5 cursor-not-allowed">
            Issue Certificate
          </button>
        </div>
      </div>

      {/* Warning Banner */}
      <div className="max-w-[1100px] mx-auto w-full bg-[#1a0f0f] border border-red-900/30 rounded-xl p-4 mb-8 flex items-start gap-4 no-print shadow-sm">
        <AlertTriangle size={20} className="text-amber-500 shrink-0 mt-0.5" />
        <div>
          <h4 className="text-sm font-bold text-stone-200 mb-1">Not a Production Certificate</h4>
          <p className="text-xs text-stone-400 leading-relaxed">
            This is a mock preview only. Production issuance remains disabled until approval metadata (provider/course approval, NAC#, affidavit method) and active-time validation are finalized by administration.
          </p>
        </div>
      </div>

      {/* Certificate Container */}
      <div className="w-full overflow-x-auto custom-scrollbar pb-12 flex-1 flex items-start justify-center">
        <div className="min-w-[1000px] max-w-[1100px] w-full shrink-0 relative bg-white shadow-[0_20px_50px_rgba(0,0,0,0.5)]">
          
          {/* THE CERTIFICATE (Ivory/White Base) */}
          <div className="relative w-full aspect-[11/8.5] bg-[#fbfaf8] overflow-hidden flex flex-col text-stone-900">
            
            {/* Background Textures */}
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-amber-900/5 via-transparent to-transparent pointer-events-none"></div>
            <div className="absolute inset-0 opacity-[0.03] bg-[url('https://www.transparenttextures.com/patterns/stardust.png')] pointer-events-none"></div>

            {/* MOCK PREVIEW ONLY Overlay */}
            <div className="absolute inset-0 flex items-center justify-center pointer-events-none z-30 opacity-10">
              <span className="text-8xl font-black uppercase text-red-900 -rotate-12 tracking-widest outline-2 outline-white">
                MOCK PREVIEW ONLY
              </span>
            </div>

            {/* Subdued Watermark in Quadrant 3 (Bottom Left) */}
            <div className="absolute bottom-16 left-16 flex items-end justify-start pointer-events-none z-0">
              <img 
                src="https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg" 
                alt="Watermark" 
                className="w-64 h-auto opacity-[0.04] invert" 
              />
            </div>

            {/* Double Border Frame */}
            <div className="absolute inset-6 border-[3px] border-[#4a0f0f] rounded-sm pointer-events-none z-10"></div>
            <div className="absolute inset-8 border border-amber-600/40 rounded-sm pointer-events-none z-10"></div>

            {/* Corner Accents */}
            <div className="absolute top-7 left-7 w-4 h-4 border-t-2 border-l-2 border-[#4a0f0f] z-10"></div>
            <div className="absolute top-7 right-7 w-4 h-4 border-t-2 border-r-2 border-[#4a0f0f] z-10"></div>
            <div className="absolute bottom-7 left-7 w-4 h-4 border-b-2 border-l-2 border-[#4a0f0f] z-10"></div>
            <div className="absolute bottom-7 right-7 w-4 h-4 border-b-2 border-r-2 border-[#4a0f0f] z-10"></div>

            {/* Certificate Content */}
            <div className="relative z-20 flex-1 flex flex-col items-center justify-center p-16 text-center pt-20">
              
              {/* Top Header */}
              <div className="mb-6 flex flex-col items-center gap-3">
                <img 
                  src="https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg" 
                  alt="Logo" 
                  className="w-12 h-12 opacity-90 invert brightness-0"
                />
                <div className="tracking-[0.3em] text-[10px] uppercase text-[#4a0f0f] font-bold">
                  CI Institute of Nursing
                </div>
              </div>

              <h1 className="font-serif text-4xl md:text-5xl text-[#2a0808] mb-3 tracking-wide font-medium">
                Online Continuing Education Certificate
              </h1>
              
              <div className="w-32 h-0.5 bg-[#4a0f0f]/20 mb-8"></div>

              <p className="text-xs uppercase tracking-widest text-stone-500 mb-4 font-medium">
                This certifies that
              </p>

              <h2 className="font-serif text-5xl text-[#1a0505] mb-6 tracking-wide">
                James Bond
              </h2>
              
              <div className="text-sm font-medium text-stone-600 mb-8">
                CNA Certificate Number: <span className="font-mono bg-stone-100 px-2 py-0.5 rounded border border-stone-200">CNA_DEMO-007</span>
              </div>

              <p className="text-sm text-stone-700 max-w-2xl leading-relaxed mb-8">
                This certificate documents completion of the approved online CE course activities listed above, subject to provider/course approval and learner eligibility. Specifically, the <strong className="text-[#4a0f0f] font-semibold">24-Hour CNA Recertification Theory Pathway</strong>.
              </p>

              <div className="bg-stone-100 border border-stone-200 rounded p-4 text-[9px] text-stone-500 max-w-3xl leading-relaxed text-justify mb-auto">
                <strong className="text-stone-700 uppercase">Disclaimer:</strong> This course does not, by itself, complete all California CNA renewal requirements. Learners are responsible for meeting all renewal requirements, including total hours, annual minimums, online-hour limits, and any required work/practice documentation.
              </div>

              {/* Bottom Grid: Details & Signatures & Seal */}
              <div className="w-full px-12 grid grid-cols-3 items-end mt-12 pb-4">
                
                {/* Left: Course Details */}
                <div className="flex flex-col items-start text-left">
                  <div className="space-y-1.5 border-l-2 border-[#4a0f0f]/20 pl-3">
                    <div className="text-[10px] text-stone-500"><strong className="text-stone-700 w-16 inline-block">Date:</strong> [Pending Issuance]</div>
                    <div className="text-[10px] text-stone-500"><strong className="text-stone-700 w-16 inline-block">CE Hours:</strong> 24.0 (Online)</div>
                    <div className="text-[10px] text-stone-500"><strong className="text-stone-700 w-16 inline-block">NAC#:</strong> [Pending Metadata]</div>
                    <div className="text-[10px] text-stone-500"><strong className="text-stone-700 w-16 inline-block">Cert ID:</strong> [Pending Issuance]</div>
                  </div>
                </div>

                {/* Center: The Seal */}
                <div className="flex flex-col items-center justify-center">
                  <div className="relative flex items-center justify-center w-28 h-28 opacity-90">
                    <div className="absolute inset-0 bg-gradient-to-br from-amber-300 via-amber-500 to-amber-700 rotate-12 rounded opacity-30 mix-blend-multiply"></div>
                    <div className="absolute inset-0 bg-gradient-to-br from-amber-300 via-amber-500 to-amber-700 rotate-45 rounded opacity-30 mix-blend-multiply"></div>
                    <div className="absolute inset-2 border border-dashed border-amber-600 rounded-full"></div>
                    <div className="absolute inset-3 border border-[#4a0f0f] rounded-full bg-[#fdfbf7] flex flex-col items-center justify-center shadow-sm">
                       <ShieldCheck size={24} className="text-[#4a0f0f] mb-1" />
                       <span className="text-[6px] uppercase tracking-[0.2em] text-[#4a0f0f] font-bold font-serif text-center leading-tight">Mock<br/>Preview</span>
                    </div>
                  </div>
                </div>

                {/* Right: Signature Placeholder */}
                <div className="flex flex-col items-end text-right">
                  <div className="w-48 border-b border-stone-400 pb-2 mb-2 flex justify-end">
                    <span className="text-stone-400 text-sm italic">Authorized Signature Pending</span>
                  </div>
                  <span className="text-[9px] uppercase tracking-widest text-stone-600">Program Director</span>
                  <span className="text-[9px] text-stone-500 mt-1">CI Institute of Nursing<br/>123 Health Way, CA 90000</span>
                </div>

              </div>
            </div>

          </div>
          {/* END CERTIFICATE */}

        </div>
      </div>
    </div>
  );
}