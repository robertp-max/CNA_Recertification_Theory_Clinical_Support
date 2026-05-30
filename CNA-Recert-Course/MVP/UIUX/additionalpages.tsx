import React, { useState } from 'react';
import { 
  Play, Shield, BookOpen, CheckCircle2, 
  Lock, ArrowRight, AlertCircle, Clock, Info, AlertTriangle, 
  ShieldAlert, Circle, FileText, Check, LayoutDashboard, 
  FileCheck, Stethoscope as StethoscopeIcon, Database, 
  FileSignature, Search, ShieldQuestion, HelpCircle, StopCircle,
  ShieldCheck, Ban, ArrowLeft
} from 'lucide-react';

export default function App() {
  const [currentView, setCurrentView] = useState('dashboard'); 
  // Views: 'dashboard', 'certStatus', 'gateCenter', 'clinicalHub'

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
      `}} />
      
      {/* Intense, premium burgundy radial gradient */}
      <div className="fixed inset-0 pointer-events-none bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#4a0f0f]/40 via-[#0a0505] to-[#0a0505] z-0"></div>

      {/* DEV NAVIGATION - For Reviewing States */}
      <div className="bg-amber-500/10 border-b border-amber-500/20 px-4 py-2 flex items-center justify-center gap-4 relative z-50 text-xs overflow-x-auto whitespace-nowrap">
        <span className="font-bold text-amber-500 uppercase tracking-widest mr-2">Dev Toggle:</span>
        <button onClick={() => setCurrentView('dashboard')} className={currentView === 'dashboard' ? 'text-white font-bold' : 'text-stone-400 hover:text-stone-200'}>Course Dashboard</button>
        <span className="text-stone-700">|</span>
        <button onClick={() => setCurrentView('certStatus')} className={currentView === 'certStatus' ? 'text-white font-bold' : 'text-stone-400 hover:text-stone-200'}>Certificate Status</button>
        <span className="text-stone-700">|</span>
        <button onClick={() => setCurrentView('gateCenter')} className={currentView === 'gateCenter' ? 'text-white font-bold' : 'text-stone-400 hover:text-stone-200'}>Gate Center</button>
        <span className="text-stone-700">|</span>
        <button onClick={() => setCurrentView('clinicalHub')} className={currentView === 'clinicalHub' ? 'text-white font-bold' : 'text-stone-400 hover:text-stone-200'}>Clinical Hub</button>
      </div>

      {/* Global Navigation */}
      <header className="px-6 py-4 border-b border-white/5 bg-black/20 backdrop-blur-md relative z-20 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-white/10 flex items-center justify-center border border-white/20">
            <span className="text-white font-bold text-xs">CI</span>
          </div>
          <span className="font-semibold text-white tracking-widest text-[10px] uppercase hidden sm:block">Institute of Nursing</span>
        </div>
        <div className="flex items-center gap-2 md:gap-6 text-xs font-semibold uppercase tracking-wider text-stone-400">
          <button className={`flex items-center gap-2 transition-colors px-3 py-1.5 rounded-lg ${currentView === 'dashboard' ? 'text-white bg-white/5 border border-white/10' : 'hover:text-white'}`}>
            <LayoutDashboard size={14} /> Course
          </button>
          <button className={`flex items-center gap-2 transition-colors px-3 py-1.5 rounded-lg ${currentView === 'certStatus' ? 'text-white bg-white/5 border border-white/10' : 'hover:text-white'}`}>
            <FileCheck size={14} /> Certificate
          </button>
          <button className={`flex items-center gap-2 transition-colors px-3 py-1.5 rounded-lg ${currentView === 'gateCenter' ? 'text-white bg-white/5 border border-white/10' : 'hover:text-white'}`}>
            <Shield size={14} /> Gate Center
          </button>
          <button className={`flex items-center gap-2 transition-colors px-3 py-1.5 rounded-lg ${currentView === 'clinicalHub' ? 'text-white bg-white/5 border border-white/10' : 'hover:text-white'}`}>
            <StethoscopeIcon size={14} /> Clinical Hub
          </button>
          <div className="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-500 flex items-center justify-center border border-amber-500/30 ml-2 md:ml-4">
            <span className="text-xs font-bold">JD</span>
          </div>
        </div>
      </header>

      {/* Main Content Router */}
      <main className="flex-1 w-full max-w-6xl mx-auto p-4 md:p-8 relative z-10 overflow-y-auto">
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 pb-20">
          {currentView === 'dashboard' && <CourseDashboard />}
          {currentView === 'certStatus' && <CertificateStatus />}
          {currentView === 'gateCenter' && <GateCenter />}
          {currentView === 'clinicalHub' && <ClinicalHub />}
        </div>
      </main>
    </div>
  );
}

// ==========================================
// VIEW 1: COURSE DASHBOARD
// ==========================================
function CourseDashboard() {
  return (
    <div className="space-y-6 max-w-5xl mx-auto">
      {/* Hero Section */}
      <div className="bg-[#120a0a]/80 backdrop-blur-xl border border-white/5 rounded-xl p-8 md:p-12 shadow-2xl relative overflow-hidden flex flex-col lg:flex-row gap-12 lg:items-center">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-96 h-96 rounded-full bg-amber-500/10 blur-3xl"></div>

        <div className="flex-1 relative z-10">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-950/30 border border-red-500/20 text-xs font-semibold tracking-wide text-red-200 uppercase mb-6">
            CNA Recertification
          </div>
          <h1 className="text-3xl md:text-5xl font-semibold text-white tracking-tight mb-4 leading-tight">
            Theory + Clinical Support
          </h1>
          <p className="text-sm md:text-lg text-stone-400 mb-10 max-w-xl leading-relaxed">
            Complete the required online theory pathway, and use optional clinical support tools for practice and confidence. This online course provides partial CE credit only — it does not complete all California renewal requirements.
          </p>
          <div className="flex flex-col sm:flex-row items-center gap-4">
            <button className="w-full sm:w-auto bg-amber-500 hover:bg-amber-400 text-black font-semibold px-8 py-4 rounded-xl flex items-center justify-center gap-3 transition-all transform hover:-translate-y-0.5 shadow-[0_0_20px_rgba(245,158,11,0.15)]">
              Start Module 0 <Play size={18} className="fill-current" />
            </button>
            <button className="w-full sm:w-auto bg-white/5 hover:bg-white/10 text-white font-medium px-8 py-4 rounded-xl transition-all border border-white/5">
              Open Dashboard
            </button>
          </div>
          <div className="flex items-center gap-4 mt-8 text-[10px] uppercase tracking-widest text-stone-500 font-semibold">
            <span className="flex items-center gap-1.5"><ShieldCheck size={14} className="text-amber-500"/> Compliance First</span>
            <span className="flex items-center gap-1.5"><Lock size={14} className="text-amber-500"/> Approval Protected</span>
            <span className="flex items-center gap-1.5"><StethoscopeIcon size={14} className="text-amber-500"/> Support is Optional</span>
          </div>
        </div>

        {/* Certificate Status Mini-Card */}
        <div className="w-full lg:w-[340px] shrink-0 bg-white/[0.02] border border-white/10 rounded-xl p-6 backdrop-blur-md relative z-10">
          <div className="flex items-center justify-between mb-6">
            <h3 className="font-semibold text-white">Certificate Status Preview</h3>
            <Shield size={18} className="text-amber-500" />
          </div>
          <div className="bg-black/40 rounded-xl p-4 border border-white/5 mb-6">
            <div className="flex items-center justify-between text-xs mb-3">
              <span className="text-stone-400 uppercase tracking-wider font-semibold">Progress</span>
              <span className="text-amber-500 font-medium">11%</span>
            </div>
            <div className="w-full h-2 bg-white/10 rounded-full overflow-hidden">
              <div className="w-[11%] h-full bg-amber-500 rounded-full"></div>
            </div>
            <p className="text-[11px] text-stone-500 mt-3 flex items-center gap-1.5">
              <AlertCircle size={12} /> 6 requirements remaining
            </p>
          </div>
          <p className="text-xs text-stone-500 leading-relaxed">
            Preview only. No certificate is issued. CDPH approval is not claimed.
          </p>
        </div>
      </div>

      {/* 3 Pillars */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <PillarCard 
          tag="Required" 
          icon={<BookOpen size={18}/>} 
          title="12-Hour Required Online CE Theory" 
          desc="Orientation, six theory modules, required interactions, knowledge checks, a final exam, and a signed statement gate your certificate readiness."
          action="View modules"
        />
        <PillarCard 
          tag="Optional • Non-Credit" 
          icon={<StethoscopeIcon size={18}/>} 
          title="Optional Clinical Support" 
          desc="Skills refresh, scenario coaching, and documentation support. Helpful and separate — it is not for clinical-hour credit and does not affect your certificate."
          action="Open Clinical Hub"
        />
        <PillarCard 
          tag="Privacy" 
          icon={<ShieldAlert size={18}/>} 
          title="No PHI" 
          desc="Never enter protected health information, real patient names, or facility data anywhere in this course. Use simulated examples only."
        />
      </div>

      {/* Modules Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 pt-4">
        {[
          { id: 'M0', title: 'Orientation', progress: 35 },
          { id: 'M1', title: 'Infection Control & PPE' },
          { id: 'M2', title: 'Resident Rights & Abuse Prevention' },
          { id: 'M3', title: 'Dementia & Communication' },
          { id: 'M4', title: 'Mobility & Safety' },
          { id: 'M5', title: 'Nutrition, Skin & Vitals' },
          { id: 'M6', title: 'Documentation & Scope' },
          { id: 'Final', title: 'Review, Final Exam & Affidavit' }
        ].map((mod, i) => (
          <div key={i} className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-5 hover:border-white/10 hover:bg-[#150c0c] transition-colors flex flex-col">
            <div className="text-[10px] font-bold text-amber-500 mb-1">{mod.id}</div>
            <h4 className="text-xs font-semibold text-stone-200 mb-4">{mod.title}</h4>
            {mod.progress !== undefined ? (
              <div className="w-full h-1 bg-white/10 rounded-full overflow-hidden mt-auto">
                <div className="h-full bg-amber-500 rounded-full" style={{ width: `${mod.progress}%` }}></div>
              </div>
            ) : (
              <div className="w-8 h-1 bg-white/5 rounded-full mt-auto"></div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

function PillarCard({ tag, icon, title, desc, action }) {
  return (
    <div className="bg-[#120a0a]/80 hover:bg-[#120a0a] transition-colors border border-white/5 rounded-xl p-6 flex flex-col h-full shadow-xl">
      <div className="text-[10px] font-bold tracking-widest uppercase text-amber-500 flex items-center gap-2 mb-4">
        {icon} {tag}
      </div>
      <h3 className="text-sm font-semibold text-white mb-2">{title}</h3>
      <p className="text-xs text-stone-400 leading-relaxed mb-6 flex-1">{desc}</p>
      {action && (
        <button className="self-start px-4 py-2 rounded-lg border border-white/10 text-xs font-semibold text-stone-300 hover:text-white hover:bg-white/5 transition-colors">
          {action}
        </button>
      )}
    </div>
  );
}

// ==========================================
// VIEW 2: CERTIFICATE STATUS (Learner View)
// ==========================================
function CertificateStatus() {
  return (
    <div className="max-w-4xl mx-auto space-y-6">
      <div className="mb-8">
        <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-2">Certificate Readiness</div>
        <h1 className="text-3xl font-semibold text-white tracking-tight mb-2">Certificate Status</h1>
        <p className="text-sm text-stone-400">No certificate is issued here. This preview is locked until every required gate passes.</p>
      </div>

      <div className="grid md:grid-cols-3 gap-6">
        {/* Circular Progress Card */}
        <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-8 flex flex-col items-center justify-center shadow-xl">
          <div className="relative w-32 h-32 mb-6">
            <svg className="w-full h-full transform -rotate-90">
              <circle cx="64" cy="64" r="56" stroke="currentColor" strokeWidth="8" fill="transparent" className="text-white/5" />
              <circle cx="64" cy="64" r="56" stroke="currentColor" strokeWidth="8" fill="transparent" strokeDasharray="351.8" strokeDashoffset={351.8 * (1 - 0.55)} className="text-amber-500 transition-all duration-1000" />
            </svg>
            <div className="absolute inset-0 flex flex-col items-center justify-center">
              <span className="text-2xl font-bold text-white">55%</span>
              <span className="text-[8px] uppercase tracking-widest text-stone-500 font-bold">Required Gates</span>
            </div>
          </div>
          <div className="bg-amber-500/10 border border-amber-500/20 text-amber-500 text-[10px] uppercase tracking-widest font-bold px-4 py-1.5 rounded-full mb-3 flex items-center gap-1.5">
            <AlertTriangle size={12} /> 5 blocker(s)
          </div>
          <p className="text-xs text-stone-400">6 of 11 required gates complete.</p>
        </div>

        {/* What this means Card */}
        <div className="md:col-span-2 bg-[#120a0a]/80 border border-white/5 rounded-xl p-8 shadow-xl">
          <h2 className="text-lg font-semibold text-white mb-4">What this means</h2>
          <p className="text-sm text-stone-300 leading-relaxed mb-6">
            California CDPH regulations require these specific gates for renewal. Each must be complete before the certificate preview unlocks.
          </p>
          <div className="bg-[#1a0f0f] border border-red-900/30 rounded-lg p-4 mb-6">
            <p className="text-xs font-medium text-red-200/80">
              Optional clinical support does not affect this readiness score and is never counted toward online CE.
            </p>
          </div>
          <p className="text-xs text-stone-500 leading-relaxed">
            The certificate remains a mock preview only. Provider approval metadata (NAC#) and certificate wording are still pending, so no certificate can be issued.
          </p>
        </div>
      </div>

      {/* Gate Checklist */}
      <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl shadow-xl overflow-hidden">
        <div className="px-6 py-5 border-b border-white/5 bg-black/20">
          <h2 className="text-base font-semibold text-white">Required gate checklist</h2>
        </div>
        <div className="divide-y divide-white/5 p-2">
          <LearnerGateRow title="Legal name present" desc="Your legal first and last name are recorded for the certificate." status="Complete" />
          <LearnerGateRow title="CNA certificate number present" desc="Your CNA certificate number is recorded." status="Complete" />
          <LearnerGateRow title="Online cap acknowledgement" desc="You acknowledged the 24-hour online CE cap and partial-credit boundary." status="Complete" />
          <LearnerGateRow title="No-PHI acknowledgement" desc="You acknowledged the no-PHI policy for all course activities." status="Complete" />
          
          <LearnerGateRow 
            title="Required theory complete" 
            desc="All required theory modules (0-6) are complete." 
            status="Pending" 
            action="Finish all required theory modules." 
          />
          <LearnerGateRow 
            title="Required interaction/feedback complete" 
            desc="You completed the required lesson interactions and knowledge checks." 
            status="Pending" 
            action="Complete the required knowledge checks in the modules." 
          />
          <LearnerGateRow 
            title="Active-time threshold (MVP engine — not CDPH-validated)" 
            desc="Active-time is measured by a real MVP engine as a demo threshold (99s of 120s accrued across required lessons). It is not yet CDPH-validated." 
            status="Pending" 
            action="Active-time threshold not yet met (99s / 120s, demo scale)." 
            pill="Simulated in Phase 1"
          />
          <LearnerGateRow 
            title="Final exam/test passed (simulated)" 
            desc="The final exam must be passed at the required threshold. Simulated/locked in this preview." 
            status="Not Started" 
            action="Final exam not yet passed (simulated/locked in this preview)." 
            pill="Simulated in Phase 1"
          />
          <LearnerGateRow 
            title="Final statement/affidavit complete (simulated)" 
            desc="A signed final statement is required before release. Draft only: e-signature method is unresolved." 
            status="Not Started" 
            action="Final statement/affidavit not yet complete (draft only)." 
            pill="Simulated in Phase 1"
          />
          <LearnerGateRow title="Certificate fields populated" desc="Required certificate output fields are present." status="Complete" />
          <LearnerGateRow title="Admin hold clear" desc="No manual compliance hold is active on this record." status="Complete" />
        </div>
      </div>

      {/* Certificate Preview Locked Banner */}
      <div className="bg-[#1a0f0f] border border-[#3a1515] rounded-xl p-8 flex flex-col items-center justify-center text-center relative overflow-hidden mt-8 shadow-2xl">
        <div className="absolute top-4 right-4 bg-black/40 border border-white/10 text-[8px] uppercase tracking-widest text-stone-500 px-2 py-1 rounded">
          Mock Preview — Not for Issuance
        </div>
        <Lock size={32} className="text-red-500 mb-4" />
        <div className="text-[10px] uppercase tracking-widest text-red-500 font-bold mb-1">Continuing Education Certificate Preview</div>
        <h2 className="text-2xl font-semibold text-white mb-8">Certificate Preview Locked</h2>
        
        <div className="w-full max-w-md text-left space-y-4">
          <div className="border-b border-white/10 pb-2">
            <div className="text-[10px] uppercase tracking-widest text-stone-500 mb-1">Learner</div>
            <div className="text-sm font-semibold text-white">James Bond</div>
          </div>
          <div className="border-b border-white/10 pb-2">
            <div className="text-[10px] uppercase tracking-widest text-stone-500 mb-1">CNA Number</div>
            <div className="text-sm font-semibold text-white">CNA-DEMO-007</div>
          </div>
          <div className="border-b border-white/10 pb-2">
            <div className="text-[10px] uppercase tracking-widest text-stone-500 mb-1">Course</div>
            <div className="text-sm font-semibold text-white">CNA Recertification Online CE — 12 Hour Theory</div>
          </div>
          <div className="pt-2">
            <div className="text-[10px] uppercase tracking-widest text-stone-500 mb-1">Status</div>
            <div className="text-sm font-bold text-red-400">Required gates incomplete</div>
          </div>
        </div>

        <p className="text-[10px] text-stone-500 mt-8">Optional clinical support is not included in this online CE certificate preview.</p>
      </div>
    </div>
  );
}

function LearnerGateRow({ title, desc, status, action, pill }) {
  const getBadge = () => {
    if (status === 'Complete') return <span className="flex items-center gap-1.5 text-[10px] uppercase tracking-widest font-bold text-green-500 bg-green-500/10 border border-green-500/20 px-2.5 py-1 rounded-full"><CheckCircle2 size={12}/> Complete</span>;
    if (status === 'Pending') return <span className="flex items-center gap-1.5 text-[10px] uppercase tracking-widest font-bold text-amber-500 bg-amber-500/10 border border-amber-500/20 px-2.5 py-1 rounded-full"><Clock size={12}/> Pending</span>;
    return <span className="flex items-center gap-1.5 text-[10px] uppercase tracking-widest font-bold text-stone-400 bg-white/5 border border-white/10 px-2.5 py-1 rounded-full"><Circle size={12}/> Not Started</span>;
  };

  return (
    <div className="p-4 flex flex-col sm:flex-row sm:items-start justify-between gap-4 hover:bg-white/[0.02] transition-colors rounded-lg">
      <div className="space-y-1">
        <h4 className="text-sm font-bold text-stone-200">{title}</h4>
        <p className="text-xs text-stone-400">{desc}</p>
        {action && <p className="text-[11px] text-amber-500/90 pt-1">{action}</p>}
        {pill && <span className="inline-block mt-2 bg-[#1a0f0f] border border-amber-500/20 text-[9px] uppercase tracking-widest text-amber-500 px-2 py-0.5 rounded">{pill}</span>}
      </div>
      <div className="shrink-0">{getBadge()}</div>
    </div>
  );
}

// ==========================================
// VIEW 3: GATE CENTER (Admin / Detailed)
// ==========================================
function GateCenter() {
  return (
    <div className="max-w-4xl mx-auto space-y-6">
      <div className="mb-8">
        <div className="text-[10px] uppercase tracking-widest text-red-500 font-bold mb-2">Compliance Control Center</div>
        <h1 className="text-3xl font-semibold text-white tracking-tight mb-2">Certificate Gate Center</h1>
        <p className="text-sm text-stone-400">Every certificate requirement in plain English — for learners, admins, and auditors. Optional clinical support is excluded from gate computation.</p>
      </div>

      {/* Decision Box */}
      <div className="bg-[#1a0f0f] border border-red-900/30 rounded-xl p-6 shadow-xl flex items-center justify-between">
        <div>
          <div className="text-[10px] uppercase tracking-widest text-red-400 font-bold flex items-center gap-1.5 mb-2">
            <ShieldAlert size={14} /> Decision
          </div>
          <h2 className="text-2xl font-bold text-white mb-1">Certificate locked</h2>
          <p className="text-sm text-stone-400">Certificate cannot release because Required theory complete is incomplete.</p>
        </div>
        <div className="bg-red-500/10 border border-red-500/20 text-red-500 px-4 py-2 rounded-lg text-xs font-bold uppercase tracking-widest flex items-center gap-2">
          <Lock size={14} /> Blocked
        </div>
      </div>

      {/* Detailed Status List */}
      <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl shadow-xl overflow-hidden">
        <div className="px-6 py-5 border-b border-white/5 bg-black/20">
          <h2 className="text-base font-semibold text-white">Requirement status</h2>
        </div>
        <div className="divide-y divide-white/5 p-2">
          <AdminGateRow 
            title="Provider approval metadata (NAC#)" 
            desc="Provider approval number and certificate wording must be on file before any production certificate can be issued."
            status="Needs Review"
            adminNote="Approval metadata is pending. Certificate remains a mock preview only."
          />
          <AdminGateRow title="Legal name present" desc="Your legal first and last name are recorded for the certificate." status="Complete" />
          <AdminGateRow title="CNA certificate number present" desc="Your CNA certificate number is recorded." status="Complete" />
          <AdminGateRow title="Online cap acknowledgement" desc="You acknowledged the 24-hour online CE cap and partial-credit boundary." status="Complete" />
          <AdminGateRow title="No-PHI acknowledgement" desc="You acknowledged the no-PHI policy for all course activities." status="Complete" />
          
          <AdminGateRow 
            title="Required theory complete" 
            desc="All required theory modules (0-6) are complete." 
            status="Pending" 
            action="Finish all required theory modules." 
          />
          <AdminGateRow 
            title="Required interaction/feedback complete" 
            desc="You completed the required lesson interactions and knowledge checks." 
            status="Pending" 
            action="Complete the required knowledge checks in the modules." 
          />
          <AdminGateRow 
            title="Active-time threshold (MVP engine — not CDPH-validated)" 
            desc="Active-time is measured by a real MVP engine at a demo threshold (99s of 120s accrued across required lessons). It is not yet CDPH-validated." 
            status="Pending" 
            action="Active-time threshold not yet met (99s / 120s, demo scale)." 
            pill="Simulated in Phase 1"
          />
          <AdminGateRow 
            title="Final exam/test passed (simulated)" 
            desc="The final exam must be passed at the required threshold. Simulated/locked in this preview." 
            status="Not Started" 
            action="Final exam not yet passed (simulated/locked in this preview)." 
            pill="Simulated in Phase 1"
          />
          <AdminGateRow 
            title="Final statement/affidavit complete (simulated)" 
            desc="A signed final statement is required before release. Draft only: e-signature method is unresolved." 
            status="Not Started" 
            action="Final statement/affidavit not yet complete (draft only)." 
            pill="Simulated in Phase 1"
          />
          <AdminGateRow title="Certificate fields populated" desc="Required certificate output fields are present." status="Complete" />
          <AdminGateRow title="Admin hold clear" desc="No manual compliance hold is active on this record." status="Complete" />
        </div>
      </div>

      {/* Bottom Grid */}
      <div className="grid md:grid-cols-2 gap-6">
        {/* Optional Support Boundary */}
        <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-6 shadow-xl flex flex-col h-full">
          <div className="text-[10px] uppercase tracking-widest text-stone-500 font-bold mb-2">Excluded From Gate</div>
          <h3 className="text-lg font-bold text-white mb-2">Optional Clinical Support boundary</h3>
          <p className="text-xs text-stone-400 mb-6">Support activities help learners but never count as online CE requirements. Optional progress: 0% (informational only).</p>
          
          <div className="space-y-2 mb-6">
            {["Optional Clinical Support Hub", "Skills Refresh", "Confidence Checks", "Documentation Support", "Help / Contact"].map((item, i) => (
              <div key={i} className="flex justify-between items-center bg-black/20 border border-white/5 rounded-lg px-4 py-3">
                <span className="text-xs text-stone-300">{item}</span>
                <span className="text-[10px] font-bold uppercase text-stone-500">Skipped</span>
              </div>
            ))}
          </div>
          
          <div className="mt-auto bg-[#1a0f0f] border border-red-900/30 rounded-lg p-3">
            <p className="text-xs font-medium text-red-200/80 text-center">Optional clinical support is not inside certificate gate computation.</p>
          </div>
        </div>

        {/* Approval Metadata */}
        <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-6 shadow-xl">
          <div className="text-[10px] uppercase tracking-widest text-stone-500 font-bold mb-2">Approval Metadata</div>
          <h3 className="text-lg font-bold text-white mb-4">Provider NAC# & wording</h3>
          <div className="inline-flex items-center gap-1.5 text-[10px] uppercase tracking-widest font-bold text-amber-500 bg-amber-500/10 border border-amber-500/20 px-2.5 py-1 rounded-full mb-4">
            <AlertTriangle size={12} /> Needs Review
          </div>
          <p className="text-xs text-stone-400 leading-relaxed mb-4">
            Approval metadata is pending. Certificate remains a mock preview only.
          </p>
          <div className="border border-amber-500/30 border-dashed rounded-lg p-3 mb-6">
            <p className="text-[10px] text-amber-500/80 italic text-center">Active-time is simulated in Phase 1. The certificate stays a mock preview.</p>
          </div>
          <button className="px-5 py-2.5 rounded-xl border border-amber-500/30 text-amber-500 hover:bg-amber-500/10 text-xs font-semibold transition-colors">
            View audit evidence
          </button>
        </div>
      </div>
    </div>
  );
}

function AdminGateRow({ title, desc, status, action, pill, adminNote }) {
  const getBadge = () => {
    if (status === 'Complete') return <span className="flex items-center gap-1.5 text-[10px] uppercase tracking-widest font-bold text-green-500 border border-green-500/30 px-2.5 py-1 rounded-full"><CheckCircle2 size={12}/> Complete</span>;
    if (status === 'Needs Review') return <span className="flex items-center gap-1.5 text-[10px] uppercase tracking-widest font-bold text-red-400 border border-red-500/30 px-2.5 py-1 rounded-full"><AlertTriangle size={12}/> Needs Review</span>;
    if (status === 'Pending') return <span className="flex items-center gap-1.5 text-[10px] uppercase tracking-widest font-bold text-amber-500 border border-amber-500/30 px-2.5 py-1 rounded-full"><Clock size={12}/> Pending</span>;
    return <span className="flex items-center gap-1.5 text-[10px] uppercase tracking-widest font-bold text-stone-500 border border-stone-600 px-2.5 py-1 rounded-full"><Circle size={12}/> Not Started</span>;
  };

  return (
    <div className="p-5 flex flex-col sm:flex-row sm:items-start justify-between gap-4 hover:bg-white/[0.02] transition-colors rounded-lg">
      <div className="space-y-1">
        <h4 className="text-sm font-bold text-stone-200">{title}</h4>
        <p className="text-xs text-stone-400">{desc}</p>
        {action && <p className="text-xs text-stone-500 pt-1">{action}</p>}
        {adminNote && <p className="text-[11px] font-medium text-amber-500 pt-1">{adminNote}</p>}
        {pill && <span className="inline-block mt-2 bg-[#1a0f0f] border border-amber-500/20 text-[9px] uppercase tracking-widest text-amber-500 px-2 py-0.5 rounded">{pill}</span>}
      </div>
      <div className="shrink-0 mt-1">{getBadge()}</div>
    </div>
  );
}

// ==========================================
// VIEW 4: CLINICAL SUPPORT HUB
// ==========================================
function ClinicalHub() {
  const tools = [
    { id: 'CS-1', title: 'Clinical Orientation', desc: 'How optional support works and the non-credit boundary.', icon: ShieldQuestion },
    { id: 'CS-2', title: 'Skills Refresh', desc: 'Refresh PPE, transfers, vitals, and feeding technique.', icon: StethoscopeIcon },
    { id: 'CS-3', title: 'Scheduling Guidance', desc: 'Options for lab, workplace, or preceptor practice.', icon: Clock },
    { id: 'CS-4', title: 'Optional Confidence Checks', desc: 'Ungraded self-checks to find areas to practice.', icon: HelpCircle },
    { id: 'CS-5', title: 'Practice Documentation Support', desc: 'Practice objective notes with fictional, de-identified data.', icon: FileText },
    { id: 'CS-6', title: 'RN/Preceptor Signoff Support', desc: 'Optional signoff artifact (name/title/date only).', icon: FileSignature },
    { id: 'CS-7', title: 'Help / Support', desc: 'Ask for help without penalty; office-hours info.', icon: Info }
  ];

  return (
    <div className="max-w-5xl mx-auto space-y-6">
      
      {/* Banner */}
      <div className="bg-[#120a0a]/80 border border-cyan-900/30 rounded-xl p-4 flex items-center gap-4">
        <div className="w-10 h-10 rounded-full bg-cyan-950/50 flex items-center justify-center shrink-0 border border-cyan-900/50">
          <StethoscopeIcon size={20} className="text-cyan-400" />
        </div>
        <div>
          <h3 className="text-sm font-bold text-stone-200">Optional Clinical Support • Non-Credit</h3>
          <p className="text-xs text-stone-400">Support only — not a certificate gate. Not for clinical-hour credit. Skipping this never affects your online CE certificate.</p>
        </div>
      </div>

      <div className="pt-4 mb-8">
        <div className="text-[10px] uppercase tracking-widest text-stone-500 font-bold mb-2">Practice Support</div>
        <h1 className="text-3xl font-semibold text-white tracking-tight mb-2">Clinical Support Hub</h1>
        <p className="text-sm text-stone-400">Build confidence and refresh skills at your own pace. These resources are separate from the required online CE pathway.</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        {/* Left Column: Support Tools */}
        <div className="lg:col-span-7 space-y-4">
          <h2 className="text-lg font-bold text-white mb-4">Support tools</h2>
          
          <div className="space-y-3">
            {tools.map((tool, i) => {
              const Icon = tool.icon;
              return (
                <div key={i} className="bg-[#120a0a]/80 border border-white/5 hover:border-white/10 rounded-xl p-4 flex items-center gap-4 cursor-pointer transition-colors group">
                  <div className="w-10 h-10 rounded-lg bg-black/40 border border-white/5 flex items-center justify-center shrink-0 text-cyan-500 group-hover:text-cyan-400 transition-colors">
                    <Icon size={18} />
                  </div>
                  <div className="flex-1">
                    <div className="text-[9px] font-bold uppercase tracking-widest text-stone-500 mb-0.5">Optional • Non-Credit</div>
                    <h4 className="text-sm font-bold text-stone-200">{tool.id} - {tool.title}</h4>
                    <p className="text-xs text-stone-400">{tool.desc}</p>
                  </div>
                  <ArrowRight size={16} className="text-stone-600 group-hover:text-white transition-colors" />
                </div>
              );
            })}
          </div>

          <div className="bg-black/20 border border-white/5 rounded-xl p-4 flex items-center gap-3">
            <HelpCircle size={16} className="text-cyan-500 shrink-0" />
            <p className="text-xs text-stone-400">Need help? Asking for support never lowers a score and never affects certificate gates.</p>
          </div>
        </div>

        {/* Right Column: Info & Action */}
        <div className="lg:col-span-5 space-y-4">
          <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-6">
            <h3 className="text-sm font-bold text-white mb-2">Support boundaries</h3>
            <p className="text-xs text-stone-400 leading-relaxed">These resources are optional and do not count toward required CE hours or California renewal clinical-hour credit.</p>
          </div>

          <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-6">
            <h3 className="text-sm font-bold text-white mb-2">Reviewer-safe documentation</h3>
            <p className="text-xs text-stone-400 leading-relaxed">All examples and templates use fictional, de-identified details and are safe for practice.</p>
          </div>

          <div className="bg-[#120a0a]/80 border border-cyan-900/30 rounded-xl p-6 mt-4">
            <div className="text-[10px] font-bold uppercase tracking-widest text-cyan-500 mb-2">Practice Beyond The Screen</div>
            <h3 className="text-lg font-bold text-white mb-6 leading-tight">In-person practice and instructor feedback are separate from your online course.</h3>
            <button className="px-6 py-3 rounded-xl border border-cyan-800 text-cyan-400 hover:bg-cyan-900/30 hover:text-cyan-300 text-sm font-semibold transition-colors flex items-center gap-2">
              Find in-person options <ArrowRight size={16} />
            </button>
          </div>
        </div>

      </div>

      {/* Bottom Documentation Box */}
      <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-6 md:p-8 mt-8">
        <h2 className="text-xl font-bold text-white mb-6">Documentation support (practice)</h2>
        
        <div className="bg-[#1a0f0f] border border-red-900/50 rounded-lg p-4 flex items-start sm:items-center gap-3 mb-6">
          <StopCircle size={20} className="text-red-500 shrink-0" />
          <p className="text-sm font-bold text-red-200">STOP: <span className="font-normal text-red-100">Do not enter Protected Health Information (PHI), real patient names, or facility data. Use simulated case data only.</span></p>
        </div>

        <div className="space-y-2 mb-6">
          <label className="text-xs font-bold text-stone-300">Practice note — fictional / de-identified details only</label>
          <textarea 
            disabled
            rows={4}
            className="w-full bg-black/40 border border-white/10 rounded-lg p-4 text-sm text-stone-500 cursor-not-allowed resize-none"
            placeholder="Do not type patient or resident identifiers. Use fictional practice notes only."
          ></textarea>
        </div>

        <button disabled className="px-6 py-3 rounded-xl bg-black/40 text-stone-600 border border-white/5 font-semibold text-sm cursor-not-allowed transition-colors">
          Mock upload disabled
        </button>
      </div>

    </div>
  );
}