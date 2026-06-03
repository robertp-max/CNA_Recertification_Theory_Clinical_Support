import React, { useState, useEffect } from 'react';
import { 
  Play, Pause, FileText, CheckCircle2, Circle, 
  ArrowRight, ArrowLeft, Clock, ShieldAlert, Image as ImageIcon,
  AlertTriangle, Info, Check, X, Shield, Stethoscope, 
  BookOpen, Lock, AlertCircle, ChevronRight, CheckSquare, Square,
  Video, FileSignature, HelpCircle, Eye, RefreshCw, Award, Settings,
  Flag, LayoutDashboard, FileCheck, Database, Search, ShieldQuestion,
  StopCircle, ShieldCheck, Ban, Printer, Share2, Download, User,
  Sun, Moon
} from 'lucide-react';

// ==========================================
// THEME: dark (default) / normal branding modes
// ==========================================
const BRANDING_STORAGE_KEY = 'ciIonBrandingMode';

function readSavedBrandingMode() {
  try {
    const saved = window.localStorage.getItem(BRANDING_STORAGE_KEY);
    return saved === 'dark' || saved === 'normal' ? saved : 'dark';
  } catch {
    return 'dark';
  }
}

// Minimalist dark/normal toggle (Sun/Moon)
function ThemeToggle({ brandingMode, setBrandingMode, className = '' }) {
  const isDark = brandingMode === 'dark';
  return (
    <button
      type="button"
      onClick={() => setBrandingMode(isDark ? 'normal' : 'dark')}
      aria-label="Toggle dark and normal mode"
      title={isDark ? 'Switch to normal mode' : 'Switch to dark mode'}
      className={`inline-flex items-center justify-center w-8 h-8 rounded-lg border transition-colors shrink-0 ${
        isDark
          ? 'border-[#3a2120] text-[#e0a938] hover:bg-[#1a0e0e]'
          : 'border-[#DEE2E6] text-[#8B1515] hover:bg-stone-100'
      } ${className}`}
    >
      {isDark ? <Sun size={15} /> : <Moon size={15} />}
    </button>
  );
}

export default function App() {
  const [currentView, setCurrentView] = useState('signin'); 

  // Branding theme mode: 'dark' (default) | 'normal'. Persisted to localStorage.
  const [brandingMode, setBrandingMode] = useState(readSavedBrandingMode);
  const isDark = brandingMode === 'dark';

  useEffect(() => {
    try {
      window.localStorage.setItem(BRANDING_STORAGE_KEY, brandingMode);
    } catch {
      /* storage unavailable; keep in-memory mode */
    }
  }, [brandingMode]);
  
  // ==========================================
  // SHARED STATE MODEL (Audit & Compliance)
  // ==========================================
  const [module0Completed, setModule0Completed] = useState(false);
  const [module0Agreed, setModule0Agreed] = useState([false, false, false]);
  const [m0FirstName, setM0FirstName] = useState('James');
  const [m0LastName, setM0LastName] = useState('Bond');
  const [m0License, setM0License] = useState('CNA_DEMO-007');

  const [lessonCompleted, setLessonCompleted] = useState(false);
  
  const [m1AssessmentPassed, setM1AssessmentPassed] = useState(false);
  const [m1AssessmentScore, setM1AssessmentScore] = useState(null);

  const [finalAssessmentPassed, setFinalAssessmentPassed] = useState(false);
  const [finalAssessmentScore, setFinalAssessmentScore] = useState(null);
  
  const [affidavitSigned, setAffidavitSigned] = useState(false);
  const [activeTimeSecs, setActiveTimeSecs] = useState(43285); // Starts at 12.02 hours for realistic audit display
  const [isTimerRunning, setIsTimerRunning] = useState(true);

  // Clinical Hub State (separate non-gating credit)
  const [clinicalInteractions, setClinicalInteractions] = useState(0);

  // Reviewer Tools Panel Visibility
  const [showReviewerTools, setShowReviewerTools] = useState(false);

  // Track active study/CE time simulation
  useEffect(() => {
    let interval = null;
    if (isTimerRunning) {
      interval = setInterval(() => {
        setActiveTimeSecs(prev => prev + 1);
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [isTimerRunning]);

  const formatHoursAndMins = (totalSecs) => {
    const hrs = Math.floor(totalSecs / 3600);
    const mins = Math.floor((totalSecs % 3600) / 60);
    const secs = totalSecs % 60;
    return `${hrs}h ${mins}m ${secs}s`;
  };

  // Helper to force unlock everything for testing
  const forceCompleteAll = () => {
    setModule0Completed(true);
    setModule0Agreed([true, true, true]);
    setLessonCompleted(true);
    setM1AssessmentPassed(true);
    setM1AssessmentScore(100);
    setFinalAssessmentPassed(true);
    setFinalAssessmentScore(90);
    setAffidavitSigned(true);
    setActiveTimeSecs(43200); // exactly 12 hours
  };

  const resetAllProgress = () => {
    setModule0Completed(false);
    setModule0Agreed([false, false, false]);
    setLessonCompleted(false);
    setM1AssessmentPassed(false);
    setM1AssessmentScore(null);
    setFinalAssessmentPassed(false);
    setFinalAssessmentScore(null);
    setAffidavitSigned(false);
    setActiveTimeSecs(185); // Reset to 3 minutes
  };

  return (
    <div data-theme={brandingMode} className="ci-app-root min-h-screen bg-[#F8F9FA] text-[#212529] font-sans selection:bg-[#FFC107]/30 flex flex-col relative overflow-x-hidden">
      
      {/* Global Scrollbar & Focus Styles */}
      <style dangerouslySetInnerHTML={{__html: `
        ::-webkit-scrollbar { width: 6px; height: 6px; background: transparent; }
        ::-webkit-scrollbar-track { background: #F8F9FA; }
        ::-webkit-scrollbar-thumb { background-color: #DEE2E6; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background-color: #c8ccd0; }
        * { scrollbar-width: thin; scrollbar-color: #DEE2E6 #F8F9FA; }
        
        .editorial-headline {
          font-family: Georgia, Cambria, "Times New Roman", Times, serif;
          font-weight: 800;
          letter-spacing: -0.015em;
        }

        /* ==========================================================
           DARK MODE (default) — Gemini burgundy-black design system.
           Applied centrally via [data-theme="dark"] so that the
           existing normal-mode (CI brand kit light) styling is left
           untouched. Intentionally-dark blocks (reviewer tools,
           audit bars: stone-800/850/900, #120606, #180a0a, etc.)
           are deliberately NOT remapped so they stay dark in both
           modes for audit/prototype separation.
           ========================================================== */
        .ci-app-root[data-theme="dark"] {
          background-color: #080404;
          color: #ece4da;
        }
        [data-theme="dark"] ::-webkit-scrollbar-track { background: #080404; }
        [data-theme="dark"] ::-webkit-scrollbar-thumb { background-color: #3a2120; }
        [data-theme="dark"] ::-webkit-scrollbar-thumb:hover { background-color: #4a2c2a; }
        [data-theme="dark"] * { scrollbar-color: #3a2120 #080404; }

        /* Surfaces */
        [data-theme="dark"] .bg-white { background-color: #120909; }
        [data-theme="dark"] .bg-\\[\\#F8F9FA\\] { background-color: #1a0e0e; }
        [data-theme="dark"] .bg-\\[\\#faf8f5\\] { background-color: #1a0e0e; }
        [data-theme="dark"] .bg-stone-50 { background-color: #1a0e0e; }
        [data-theme="dark"] .bg-stone-100 { background-color: #20120f; }
        [data-theme="dark"] .bg-stone-200,
        [data-theme="dark"] .bg-stone-250,
        [data-theme="dark"] .bg-stone-300 { background-color: #2a1716; }
        [data-theme="dark"] .bg-\\[\\#DEE2E6\\] { background-color: #2e1a19; }
        [data-theme="dark"] .bg-white\\/40 { background-color: rgba(18,9,9,0.5); }
        [data-theme="dark"] .bg-\\[\\#F8F9FA\\]\\/60 { background-color: rgba(26,14,14,0.6); }
        [data-theme="dark"] .bg-\\[\\#F8F9FA\\]\\/40 { background-color: rgba(26,14,14,0.4); }

        /* Status tint surfaces (kept dark-friendly, not glaring pastels) */
        [data-theme="dark"] .bg-amber-50 { background-color: rgba(224,169,56,0.12); }
        [data-theme="dark"] .bg-amber-100 { background-color: rgba(224,169,56,0.18); }
        [data-theme="dark"] .bg-emerald-50 { background-color: rgba(16,185,129,0.10); }
        [data-theme="dark"] .bg-emerald-100 { background-color: rgba(16,185,129,0.16); }
        [data-theme="dark"] .bg-red-50\\/75 { background-color: rgba(220,38,38,0.10); }
        [data-theme="dark"] .bg-red-100 { background-color: rgba(220,38,38,0.16); }

        /* Borders */
        [data-theme="dark"] .border-\\[\\#DEE2E6\\],
        [data-theme="dark"] .border-stone-100,
        [data-theme="dark"] .border-stone-200 { border-color: #2e1a19; }
        [data-theme="dark"] .border-stone-300 { border-color: #3a2120; }
        [data-theme="dark"] .border-stone-400 { border-color: #4a2c2a; }
        [data-theme="dark"] .border-amber-200 { border-color: rgba(224,169,56,0.35); }
        [data-theme="dark"] .border-emerald-200 { border-color: rgba(16,185,129,0.30); }
        [data-theme="dark"] .border-emerald-300 { border-color: rgba(16,185,129,0.40); }
        [data-theme="dark"] .border-red-200 { border-color: rgba(220,38,38,0.30); }

        /* Text */
        [data-theme="dark"] .text-\\[\\#212529\\],
        [data-theme="dark"] .text-stone-900,
        [data-theme="dark"] .text-stone-800 { color: #ece4da; }
        [data-theme="dark"] .text-stone-700 { color: #ded6cc; }
        [data-theme="dark"] .text-stone-600 { color: #cabfb4; }
        [data-theme="dark"] .text-stone-500 { color: #a99f94; }
        [data-theme="dark"] .text-stone-400 { color: #877d72; }
        [data-theme="dark"] .text-\\[\\#8B1515\\],
        [data-theme="dark"] .text-\\[\\#a61a1a\\] { color: #e0a938; }
        [data-theme="dark"] .text-\\[\\#4a0f0f\\],
        [data-theme="dark"] .text-\\[\\#2a0808\\],
        [data-theme="dark"] .text-\\[\\#1a0505\\] { color: #edc987; }
        [data-theme="dark"] .text-amber-650 { color: #e0a938; }
        [data-theme="dark"] .text-amber-800 { color: #e7c074; }
        [data-theme="dark"] .text-emerald-600 { color: #34d399; }
        [data-theme="dark"] .text-emerald-800 { color: #6ee7b7; }
        [data-theme="dark"] .text-red-700 { color: #f87171; }
        [data-theme="dark"] .text-red-800 { color: #fca5a5; }
        [data-theme="dark"] .placeholder-stone-400::placeholder { color: #877d72; }

        /* Hover states for remapped light surfaces */
        [data-theme="dark"] .hover\\:bg-stone-50:hover,
        [data-theme="dark"] .hover\\:bg-\\[\\#F8F9FA\\]:hover { background-color: #20120f; }
        [data-theme="dark"] .hover\\:bg-stone-100:hover { background-color: #2a1716; }
        [data-theme="dark"] .hover\\:bg-stone-200:hover,
        [data-theme="dark"] .hover\\:bg-stone-250:hover { background-color: #34201e; }
        [data-theme="dark"] .hover\\:text-\\[\\#212529\\]:hover { color: #ece4da; }
        [data-theme="dark"] .hover\\:text-\\[\\#8B1515\\]:hover,
        [data-theme="dark"] .hover\\:text-\\[\\#a61a1a\\]:hover { color: #e0a938; }
        [data-theme="dark"] .hover\\:border-stone-300:hover { border-color: #3a2120; }
        [data-theme="dark"] .hover\\:border-stone-400:hover { border-color: #4a2c2a; }

        /* Sign-in card burgundy glow in dark mode */
        [data-theme="dark"] .ci-signin-card {
          box-shadow: 0 25px 60px rgba(0,0,0,0.55), 0 0 60px rgba(122,16,38,0.18);
        }
      `}} />
      
      {/* Dev/Reviewer Tools Drawer */}
      <div className="relative z-50">
        <div className="bg-[#180a0a] border-b border-[#FFC107]/20 text-xs py-1.5 px-4 flex items-center justify-between text-stone-400 no-print">
          <div className="flex items-center gap-2">
            <span className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></span>
            <span className="font-mono tracking-wide text-stone-300">CDPH CE Audit-Simulator Active: V2.1 (Light Mode)</span>
          </div>
          <button 
            onClick={() => setShowReviewerTools(!showReviewerTools)} 
            className="flex items-center gap-1.5 text-amber-500 hover:text-amber-400 font-semibold uppercase tracking-wider px-2 py-0.5 rounded bg-amber-955/40 border border-amber-500/20 transition-all"
          >
            <Settings size={12} />
            {showReviewerTools ? 'Close Review Panel' : 'Open Review Panel'}
          </button>
        </div>

        {showReviewerTools && (
          <div className="bg-[#120606] border-b border-[#8B1515] p-5 text-sm animate-in slide-in-from-top-4 duration-300 no-print">
            <div className="max-w-6xl mx-auto space-y-4">
              <div className="flex items-center justify-between border-b border-stone-800 pb-2">
                <span className="font-semibold text-stone-200 uppercase tracking-widest text-[11px] flex items-center gap-2">
                  <Shield size={14} className="text-[#FFC107]" /> Prototype State Override Panel
                </span>
                <span className="text-xs text-stone-500 italic">Select any specific view below to instantly verify its design</span>
              </div>

              {/* Quick View Switcher Grid */}
              <div className="bg-black/40 p-3 rounded-lg border border-stone-850">
                <div className="text-[10px] text-stone-400 uppercase tracking-wider font-mono font-bold mb-2">View Selector Jump:</div>
                <div className="flex flex-wrap gap-2">
                  {[
                    { id: 'signin', label: 'Sign-in Card', group: 'Auth' },
                    { id: 'dashboard', label: 'Dashboard', group: 'Portal' },
                    { id: 'modules', label: 'CE Modules Grid', group: 'Portal' },
                    { id: 'module0', label: 'Mod 0 Orientation', group: 'Portal' },
                    { id: 'module1', label: 'Mod 1 Overview', group: 'Portal' },
                    { id: 'lesson', label: '4-Card Player', group: 'Portal' },
                    { id: 'm1Assessment', label: 'Mod-Splash', group: 'Exams' },
                    { id: 'm1AssessmentQuiz', label: 'Mod-Test (Quiz)', group: 'Exams' },
                    { id: 'finalAssessmentSplash', label: 'Final-Splash', group: 'Exams' },
                    { id: 'finalAssessmentQuiz', label: 'Final-Test (Quiz)', group: 'Exams' },
                    { id: 'certificate', label: 'Cert Status / Gate Center', group: 'Compliance' },
                    { id: 'clinical', label: 'Clinical Hub', group: 'Compliance' }
                  ].map((btn) => (
                    <button
                      key={btn.id}
                      onClick={() => {
                        setCurrentView(btn.id);
                        window.scrollTo({ top: 0, behavior: 'smooth' });
                      }}
                      className={`px-2.5 py-1 rounded text-[10px] font-mono font-semibold transition-all border ${
                        currentView === btn.id 
                          ? 'bg-[#8B1515] text-stone-100 border-[#8B1515]' 
                          : 'bg-stone-900 text-stone-400 border-stone-800 hover:text-stone-200'
                      }`}
                    >
                      <span className="opacity-40 mr-1 text-[8px] uppercase">{btn.group}:</span>
                      {btn.label}
                    </button>
                  ))}
                </div>
              </div>

              {/* Simulation States */}
              <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
                <div>
                  <label className="block text-stone-400 text-[10px] uppercase font-bold mb-1">Module 0 Status</label>
                  <div className="flex gap-2">
                    <button 
                      onClick={() => { setModule0Completed(true); setModule0Agreed([true, true, true]); }} 
                      className={`px-3 py-1.5 rounded text-xs font-semibold w-full border ${module0Completed ? 'bg-amber-955/40 text-amber-400 border-amber-500/20' : 'bg-stone-900 text-stone-400 border-stone-800'}`}
                    >
                      Complete
                    </button>
                    <button 
                      onClick={() => { setModule0Completed(false); setModule0Agreed([false, false, false]); }} 
                      className="px-2 py-1.5 rounded text-xs bg-stone-900 border border-stone-800 text-stone-500 hover:text-stone-300"
                    >
                      Reset
                    </button>
                  </div>
                </div>

                <div>
                  <label className="block text-stone-400 text-[10px] uppercase font-bold mb-1">Lesson Completed</label>
                  <button 
                    onClick={() => setLessonCompleted(!lessonCompleted)} 
                    className={`px-3 py-1.5 rounded text-xs font-semibold w-full border ${lessonCompleted ? 'bg-amber-955/20 text-amber-400 border-amber-500/30' : 'bg-stone-900 text-stone-400 border-stone-800'}`}
                  >
                    {lessonCompleted ? 'Completed' : 'Not Started'}
                  </button>
                </div>

                <div>
                  <label className="block text-stone-400 text-[10px] uppercase font-bold mb-1">Module 1 Exam</label>
                  <div className="flex gap-1">
                    <button 
                      onClick={() => { setM1AssessmentPassed(true); setM1AssessmentScore(90); }} 
                      className={`px-2 py-1.5 rounded text-xs font-semibold flex-1 border ${m1AssessmentPassed ? 'bg-emerald-950/20 text-emerald-400 border-emerald-500/30' : 'bg-stone-900 text-stone-400 border-stone-800'}`}
                    >
                      Pass (90%)
                    </button>
                    <button 
                      onClick={() => { setM1AssessmentPassed(false); setM1AssessmentScore(50); }} 
                      className="px-2 py-1.5 rounded text-xs bg-stone-900 border border-stone-800 text-stone-400 font-semibold hover:bg-stone-850"
                    >
                      Fail
                    </button>
                  </div>
                </div>

                <div>
                  <label className="block text-stone-400 text-[10px] uppercase font-bold mb-1">Final Exam</label>
                  <div className="flex gap-1">
                    <button 
                      onClick={() => { setFinalAssessmentPassed(true); setFinalAssessmentScore(85); }} 
                      className={`px-2 py-1.5 rounded text-xs font-semibold flex-1 border ${finalAssessmentPassed ? 'bg-emerald-950/20 text-emerald-400 border-emerald-500/30' : 'bg-stone-900 text-stone-400 border-stone-800'}`}
                    >
                      Pass (85%)
                    </button>
                    <button 
                      onClick={() => { setFinalAssessmentPassed(false); setFinalAssessmentScore(40); }} 
                      className="px-2 py-1.5 rounded text-xs bg-stone-900 border border-stone-800 text-stone-400 font-semibold hover:bg-[#1f1212]"
                    >
                      Fail
                    </button>
                  </div>
                </div>

                <div className="flex flex-col justify-end">
                  <div className="flex gap-2">
                    <button 
                      onClick={forceCompleteAll} 
                      className="flex-1 bg-amber-500 hover:bg-amber-400 text-black text-xs font-bold py-1.5 px-2 rounded transition-all uppercase tracking-wider"
                    >
                      Unlock All
                    </button>
                    <button 
                      onClick={resetAllProgress} 
                      className="flex-1 bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-400 text-xs font-bold py-1.5 px-2 rounded transition-all uppercase tracking-wider"
                    >
                      Reset All
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Light Mode Navigation Header */}
      {currentView !== 'signin' && (
        <header className="px-6 py-4 border-b border-[#DEE2E6] bg-white relative z-40 flex items-center justify-between shrink-0 no-print shadow-sm">
          <div className="flex items-center gap-3 cursor-pointer" onClick={() => setCurrentView('dashboard')}>
            <div className="w-8 h-8 rounded bg-[#8B1515] flex items-center justify-center border border-[#8B1515]/20">
              <span className="text-white font-bold text-xs tracking-tight font-sans">CI</span>
            </div>
            <div>
              <span className="font-semibold text-[#212529] tracking-wider text-sm block">CI INSTITUTE OF NURSING</span>
              <span className="text-[9px] text-[#8B1515] block -mt-1 font-mono uppercase tracking-widest font-bold">CNA CE Program Preview</span>
            </div>
          </div>
          
          <div className="flex items-center gap-1 sm:gap-4 text-xs sm:text-sm font-medium text-stone-600">
            {[
              { id: 'dashboard', label: 'Dashboard' },
              { id: 'modules', label: 'CE Modules' },
              { id: 'certificate', label: 'Certificate Gate' },
              { id: 'clinical', label: 'Clinical Hub' },
            ].map(item => {
              const isActive = currentView === item.id || 
                (item.id === 'modules' && ['module0', 'module1', 'lesson', 'm1Assessment', 'm1AssessmentQuiz', 'finalAssessmentSplash', 'finalAssessmentQuiz', 'finalResult'].includes(currentView));
              return (
                <button 
                  key={item.id}
                  onClick={() => setCurrentView(item.id)}
                  className={`transition-all px-3 py-1.5 rounded-lg border uppercase tracking-wider text-[11px] font-bold ${
                    isActive 
                      ? 'text-[#8B1515] bg-[#8B1515]/5 border-[#8B1515]/25' 
                      : 'border-transparent text-stone-600 hover:text-[#212529] hover:bg-stone-100'
                  }`}
                >
                  {item.label}
                </button>
              );
            })}
            
            <ThemeToggle brandingMode={brandingMode} setBrandingMode={setBrandingMode} className="ml-1 sm:ml-4" />

            <div className="w-8 h-8 rounded bg-stone-100 text-[#8B1515] flex items-center justify-center border border-[#DEE2E6] ml-1 sm:ml-2">
              <span className="text-xs font-bold font-mono">JB</span>
            </div>
          </div>
        </header>
      )}

      {/* Main Content Area */}
      <main className="flex-1 w-full max-w-6xl mx-auto p-4 md:p-8 relative z-10 flex flex-col justify-start">
        <div className="transition-all duration-300 flex-1 flex flex-col justify-start">
          
          {/* VIEW: SIGN IN */}
          {currentView === 'signin' && (
            <SignInView 
              setView={setCurrentView}
              m0FirstName={m0FirstName}
              m0LastName={m0LastName}
              m0License={m0License}
              brandingMode={brandingMode}
              setBrandingMode={setBrandingMode}
            />
          )}
          
          {/* VIEW: DASHBOARD */}
          {currentView === 'dashboard' && (
            <div className="space-y-6 animate-in fade-in slide-in-from-bottom-2 duration-500">
              
              {/* Main Banner */}
              <div className="bg-white border border-[#DEE2E6] rounded-xl p-6 md:p-10 shadow-sm relative overflow-hidden flex flex-col lg:flex-row gap-8 lg:items-center">
                <div className="absolute top-0 right-0 -mr-32 -mt-32 w-96 h-96 rounded-full bg-[#FFC107]/5 blur-3xl pointer-events-none"></div>

                <div className="flex-1 relative z-10">
                  <div className="inline-flex items-center gap-2 px-3 py-1 rounded bg-[#8B1515]/5 border border-[#8B1515]/20 text-[11px] font-bold tracking-widest text-[#8B1515] uppercase mb-4">
                    <Shield size={12} /> CNA Theory Recertification Pathway
                  </div>
                  <h1 className="text-3xl md:text-5xl font-bold text-[#212529] tracking-tight mb-4 leading-tight">
                    CNA CE Theory Portal
                  </h1>
                  <p className="text-stone-600 text-sm md:text-base mb-6 max-w-xl leading-relaxed">
                    A secure 12-hour structured online theory program designed to meet professional continuing education guidelines. Features standard verification modules, assessments, and audit trails.
                  </p>
                  
                  {/* High priority regulatory guardrail clearly visible */}
                  <div className="bg-amber-50 p-4 rounded-lg border border-amber-200 max-w-xl mb-6">
                    <div className="flex items-start gap-2.5">
                      <AlertTriangle size={15} className="text-amber-650 shrink-0 mt-0.5" />
                      <p className="text-[11px] text-stone-700 leading-relaxed font-mono">
                        <strong>Regulatory Compliance Notice:</strong> This course provides 12 hours of online theory CE only. It does not constitute full CDPH CNA renewal on its own. Optional Clinical Support Hub does not count toward clinical hours.
                      </p>
                    </div>
                  </div>

                  <div className="flex flex-col sm:flex-row items-center gap-4">
                    {!module0Completed ? (
                      <button 
                        onClick={() => setCurrentView('module0')}
                        className="w-full sm:w-auto bg-[#8B1515] hover:bg-[#a61a1a] text-white border border-[#8B1515] font-semibold px-6 py-3 rounded-lg flex items-center justify-center gap-2 transition-colors uppercase tracking-wider text-xs shadow-sm"
                      >
                        Start Required Orientation <ArrowRight size={14} />
                      </button>
                    ) : (
                      <button 
                        onClick={() => setCurrentView('modules')}
                        className="w-full sm:w-auto bg-[#8B1515] hover:bg-[#a61a1a] text-white border border-[#8B1515] font-semibold px-6 py-3 rounded-lg flex items-center justify-center gap-2 transition-colors uppercase tracking-wider text-xs shadow-sm"
                      >
                        Resume Pathway <ArrowRight size={14} />
                      </button>
                    )}
                    <button 
                      onClick={() => setCurrentView('modules')}
                      className="w-full sm:w-auto bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-300 font-semibold px-6 py-3 rounded-lg transition-colors uppercase tracking-wider text-xs shadow-sm"
                    >
                      View All Modules
                    </button>
                  </div>
                </div>

                {/* Status Column */}
                <div className="w-full lg:w-[320px] shrink-0 bg-[#F8F9FA] border border-[#DEE2E6] rounded-xl p-5 relative z-10">
                  <div className="flex items-center justify-between mb-4 pb-3 border-b border-[#DEE2E6]">
                    <h3 className="font-semibold text-stone-700 text-xs uppercase tracking-wider">Gate Review Status</h3>
                    <div className="flex items-center gap-1.5 text-[#8B1515] text-xs">
                      <Shield size={14} />
                      <span className="font-mono text-[11px] font-bold">12-HOUR CAP</span>
                    </div>
                  </div>

                  <div className="space-y-3 mb-5 text-stone-700">
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-stone-500 font-medium">Orientation (Mod 0):</span>
                      <span className={`flex items-center gap-1 ${module0Completed ? 'text-emerald-600 font-semibold' : 'text-stone-500'}`}>
                        {module0Completed ? <CheckCircle2 size={12} /> : <Circle size={12} />}
                        {module0Completed ? 'Approved' : 'Pending'}
                      </span>
                    </div>
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-stone-500 font-medium">Active Timer Check:</span>
                      <span className={`font-mono text-[11px] font-bold ${activeTimeSecs >= 43200 ? 'text-emerald-600' : 'text-[#8B1515]'}`}>
                        {formatHoursAndMins(activeTimeSecs)}
                      </span>
                    </div>
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-stone-500 font-medium">Theory Lessons:</span>
                      <span className={`flex items-center gap-1 ${lessonCompleted ? 'text-emerald-600 font-semibold' : 'text-stone-500'}`}>
                        {lessonCompleted ? <CheckCircle2 size={12} /> : <Circle size={12} />}
                        {lessonCompleted ? 'Complete' : 'Pending'}
                      </span>
                    </div>
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-stone-500 font-medium">Final Assessment:</span>
                      <span className={`flex items-center gap-1 ${finalAssessmentPassed ? 'text-emerald-600 font-semibold' : 'text-stone-500'}`}>
                        {finalAssessmentPassed ? <CheckCircle2 size={12} /> : <Circle size={12} />}
                        {finalAssessmentPassed ? `Passed` : 'Unattempted'}
                      </span>
                    </div>
                  </div>

                  <div className="bg-white p-3 rounded border border-[#DEE2E6] mb-4">
                    <div className="flex items-center justify-between text-[11px] mb-2">
                      <span className="text-stone-500 uppercase font-bold">Overall Progress</span>
                      <span className="text-[#8B1515] font-bold font-mono">
                        {finalAssessmentPassed && affidavitSigned ? '100%' : module0Completed ? '15%' : '0%'}
                      </span>
                    </div>
                    <div className="w-full h-1.5 bg-stone-100 rounded-full overflow-hidden">
                      <div 
                        className="h-full bg-[#FFC107] transition-all duration-500" 
                        style={{ width: finalAssessmentPassed && affidavitSigned ? '100%' : module0Completed ? '15%' : '2%' }}
                      ></div>
                    </div>
                  </div>

                  <button 
                    onClick={() => setCurrentView('certificate')}
                    className="w-full py-2.5 rounded bg-white hover:bg-stone-50 text-stone-800 font-semibold text-xs border border-[#DEE2E6] transition-colors uppercase tracking-wider shadow-sm"
                  >
                    Review Auditing Gates
                  </button>
                </div>
              </div>

              {/* Grid Features */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="p-6 rounded-xl bg-white border border-[#DEE2E6] flex flex-col justify-between shadow-sm">
                  <div>
                    <div className="text-[#8B1515] mb-3"><BookOpen size={20} /></div>
                    <h4 className="text-sm font-semibold text-[#212529] uppercase tracking-wider mb-2">12-Hour Required Theory</h4>
                    <p className="text-xs text-stone-500 leading-relaxed">
                      Structured sequence covering Infection Control, Resident Rights, Dementia Care, Mobility, and Nutrition.
                    </p>
                  </div>
                  <div className="mt-4 pt-3 border-t border-[#DEE2E6]">
                    <span className="text-[10px] text-[#8B1515] font-bold uppercase font-mono">STATUS: SEQUENTIAL ONLY</span>
                  </div>
                </div>

                <div className="p-6 rounded-xl bg-white border border-[#DEE2E6] flex flex-col justify-between shadow-sm">
                  <div>
                    <div className="text-[#8B1515] mb-3"><Stethoscope size={20} /></div>
                    <h4 className="text-sm font-semibold text-[#212529] uppercase tracking-wider mb-2">Optional Clinical Support</h4>
                    <p className="text-xs text-stone-500 leading-relaxed">
                      Skills practice and simulated scenarios to gain professional confidence. Entirely optional, non-credit, and separate from certificate progress.
                    </p>
                  </div>
                  <div className="mt-4 pt-3 border-t border-[#DEE2E6] flex justify-between items-center">
                    <span className="text-[10px] text-[#8B1515] font-bold uppercase font-mono">STATUS: OPTIONAL CE</span>
                    <button 
                      onClick={() => setCurrentView('clinical')}
                      className="text-[10px] text-[#8B1515] hover:underline font-bold uppercase tracking-wider"
                    >
                      Enter Hub &rarr;
                    </button>
                  </div>
                </div>

                <div className="p-6 rounded-xl bg-white border border-[#DEE2E6] flex flex-col justify-between shadow-sm">
                  <div>
                    <div className="text-[#8B1515] mb-3"><ShieldAlert size={20} /></div>
                    <h4 className="text-sm font-semibold text-[#212529] uppercase tracking-wider mb-2">Audit Safety Guarantee</h4>
                    <p className="text-xs text-stone-500 leading-relaxed">
                      Strict HIPAA / PHI guardrails. Simulated patient personas are used exclusively. No actual resident healthcare identifiers are saved.
                    </p>
                  </div>
                  <div className="mt-4 pt-3 border-t border-[#DEE2E6]">
                    <span className="text-[10px] text-emerald-600 font-bold uppercase font-mono flex items-center gap-1">
                      <ShieldCheck size={12} /> No-PHI Safeguards Active
                    </span>
                  </div>
                </div>
              </div>

            </div>
          )}

          {/* VIEW: MODULES LIST */}
          {currentView === 'modules' && (
            <div className="flex flex-col lg:flex-row gap-8 animate-in fade-in duration-300 font-sans">
              
              {/* Left Sidebar */}
              <div className="w-full lg:w-80 shrink-0 space-y-6">
                <div className="bg-white border border-[#DEE2E6] rounded-xl p-6 sticky top-8 shadow-sm">
                  <div className="text-[10px] uppercase tracking-widest text-[#8B1515] font-bold mb-3 flex items-center gap-1.5 font-mono">
                    <Shield size={12} /> Theory CE Requirements
                  </div>
                  <h2 className="text-2xl font-normal text-[#212529] mb-3 leading-tight font-sans">Curriculum</h2>
                  <p className="text-xs text-stone-500 mb-6 leading-relaxed">
                    All required theory modules must be initiated and completed in order. Active study time is logged for CDPH compliance.
                  </p>

                  <div className="space-y-4 mb-6 border-t border-[#DEE2E6] pt-4">
                    <div>
                      <div className="flex justify-between text-[11px] mb-1 text-stone-600">
                        <span>Legal Name Verified</span>
                        <span className="font-mono text-[#212529] font-bold">{m0FirstName} {m0LastName}</span>
                      </div>
                      <div className="flex justify-between text-[11px] text-stone-600">
                        <span>License Key</span>
                        <span className="font-mono text-[#212529] font-bold">{m0License}</span>
                      </div>
                    </div>
                  </div>

                  <div className="space-y-2 mb-6">
                    <div className="flex justify-between text-[11px] font-semibold">
                      <span className="text-[#212529]">Course Verification</span>
                      <span className="text-[#8B1515] font-bold font-mono">
                        {finalAssessmentPassed ? "100%" : module0Completed ? "15%" : "0%"}
                      </span>
                    </div>
                    <div className="w-full h-1 bg-stone-100 rounded-full overflow-hidden">
                      <div 
                        className="h-full bg-[#8B1515] transition-all" 
                        style={{ width: finalAssessmentPassed ? '100%' : module0Completed ? '15%' : '0%' }}
                      ></div>
                    </div>
                  </div>

                  <button 
                    onClick={() => setCurrentView('certificate')}
                    className="w-full py-2.5 rounded bg-stone-100 hover:bg-stone-250 border border-stone-300 text-stone-800 font-semibold text-xs uppercase tracking-wider transition-colors shadow-sm"
                  >
                    Review Gate Checklist
                  </button>
                </div>
              </div>

              {/* Right Modules Grid */}
              <div className="flex-1 space-y-6">
                <div>
                  <h2 className="text-2xl font-normal text-[#212529] mb-1">Theory Recertification Modules</h2>
                  <p className="text-stone-500 text-xs">Verify your identification during Module 0 to unlock successive study units.</p>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  
                  {/* Module 0 Card */}
                  <div className="p-5 rounded-xl border bg-white border-[#DEE2E6] hover:border-stone-400 transition-all flex flex-col justify-between shadow-sm">
                    <div>
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-[10px] font-bold text-amber-500 uppercase tracking-wider font-mono">Module 0</span>
                        <span className="text-[10px] font-mono text-stone-500 font-bold">0.5 HR</span>
                      </div>
                      <h3 className="text-base font-semibold text-[#212529] mb-2">Orientation & Compliance Verification</h3>
                      <p className="text-xs text-stone-500 leading-relaxed mb-6">
                        Confirm CNA credentials, review regulatory guidelines, acknowledge HIPAA restrictions, and establish core active-time validation parameters.
                      </p>
                    </div>
                    <div className="flex items-center justify-between pt-3 border-t border-[#DEE2E6]">
                      <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded text-[10px] font-semibold ${
                        module0Completed ? 'bg-emerald-100 text-emerald-800 border border-emerald-200' : 'bg-amber-100 text-amber-800 border border-amber-200'
                      }`}>
                        {module0Completed ? <CheckCircle2 size={10} /> : <AlertCircle size={10} />}
                        {module0Completed ? 'Completed & Confirmed' : 'Action Required'}
                      </span>
                      <button 
                        onClick={() => setCurrentView('module0')}
                        className={`px-3 py-1 rounded text-xs font-semibold ${
                          module0Completed ? 'bg-stone-100 text-stone-300 hover:bg-[#8B1515]/5 hover:text-[#8B1515]' : 'bg-[#8B1515] text-white hover:bg-[#781616]'
                        } transition-colors border border-transparent hover:border-[#8B1515]/30`}
                      >
                        {module0Completed ? 'Review' : 'Begin'}
                      </button>
                    </div>
                  </div>

                  {/* Module 1 Card */}
                  <div className={`p-5 rounded-xl border transition-all flex flex-col justify-between shadow-sm ${
                    module0Completed ? 'bg-white border-[#DEE2E6] hover:border-stone-400' : 'bg-[#F8F9FA] border-stone-200 opacity-60'
                  }`}>
                    <div>
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-[10px] font-bold text-stone-500 uppercase tracking-wider font-mono">Module 1</span>
                        <span className="text-[10px] font-mono text-stone-500 font-bold">1.5 HR</span>
                      </div>
                      <h3 className="text-base font-semibold text-[#212529] mb-2">Infection Control & PPE</h3>
                      <p className="text-xs text-stone-500 leading-relaxed mb-6">
                        Examine infection chains, implement WHO hand hygiene protocols, and perform standard safety selections for CNA barrier protection.
                      </p>
                    </div>
                    <div className="flex items-center justify-between pt-3 border-t border-[#DEE2E6]">
                      <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded text-[10px] font-semibold ${
                        !module0Completed ? 'bg-stone-100 text-stone-500 border border-stone-200' :
                        m1AssessmentPassed ? 'bg-emerald-100 text-emerald-800 border border-emerald-200' :
                        lessonCompleted ? 'bg-amber-100 text-amber-800 border border-amber-200' : 'bg-stone-100 text-stone-500'
                      }`}>
                        {!module0Completed ? <Lock size={10} /> : m1AssessmentPassed ? <CheckCircle2 size={10} /> : <AlertCircle size={10} />}
                        {!module0Completed ? 'Locked (Complete Mod 0)' : m1AssessmentPassed ? 'Passed' : lessonCompleted ? 'Assessment Ready' : 'In Progress'}
                      </span>
                      {module0Completed && (
                        <button 
                          onClick={() => setCurrentView('module1')}
                          className="px-3 py-1 rounded text-xs bg-[#8B1515] text-white hover:bg-[#781616] transition-colors"
                        >
                          Open Module
                        </button>
                      )}
                    </div>
                  </div>

                  {/* Module 2 Card (Locked Demo) */}
                  <div className="p-5 rounded-xl border bg-white/40 border-[#DEE2E6] opacity-50 flex flex-col justify-between shadow-sm">
                    <div>
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-[10px] font-bold text-stone-500 uppercase tracking-wider font-mono">Module 2</span>
                        <span className="text-[10px] font-mono text-stone-500 font-bold">2.0 HR</span>
                      </div>
                      <h3 className="text-base font-semibold text-stone-500 mb-2">Resident Rights & Abuse Prevention</h3>
                      <p className="text-xs text-stone-500 leading-relaxed mb-6">
                        Required regulatory overview regarding legal rights, active advocacy, mandates, and CDPH reporting timelines.
                      </p>
                    </div>
                    <div className="flex items-center justify-between pt-3 border-t border-[#DEE2E6]">
                      <span className="inline-flex items-center gap-1 text-[10px] text-stone-500 font-mono font-bold">
                        <Lock size={10} /> Locked (Sequential Path)
                      </span>
                    </div>
                  </div>

                  {/* Module 3 Card (Locked Demo) */}
                  <div className="p-5 rounded-xl border bg-white/40 border-[#DEE2E6] opacity-50 flex flex-col justify-between shadow-sm">
                    <div>
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-[10px] font-bold text-stone-500 uppercase tracking-wider font-mono">Module 3</span>
                        <span className="text-[10px] font-mono text-stone-500 font-bold">2.0 HR</span>
                      </div>
                      <h3 className="text-base font-semibold text-stone-500 mb-2">Dementia Care & Communication</h3>
                      <p className="text-xs text-stone-500 leading-relaxed mb-6">
                        Cognitive decline, verbal and non-verbal adjustment methods, and behavioral de-escalation protocols.
                      </p>
                    </div>
                    <div className="flex items-center justify-between pt-3 border-t border-[#DEE2E6]">
                      <span className="inline-flex items-center gap-1 text-[10px] text-stone-500 font-mono font-bold">
                        <Lock size={10} /> Locked (Sequential Path)
                      </span>
                    </div>
                  </div>

                </div>

                {/* Course Final Assessment Panel */}
                <div className={`p-6 rounded-xl border transition-all shadow-sm ${
                  m1AssessmentPassed ? 'bg-white border-[#8B1515]/30' : 'bg-[#F8F9FA]/60 border-[#DEE2E6] opacity-60'
                }`}>
                  <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
                    <div>
                      <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-[10px] font-bold tracking-widest text-[#8B1515] uppercase bg-[#8B1515]/5 border border-[#8B1515]/20 mb-3 font-mono">
                        Course-Wide Final Examination
                      </div>
                      <h3 className="text-lg font-bold text-[#212529] mb-2 font-sans">Theory Final Assessment Gate</h3>
                      <p className="text-xs text-stone-500 max-w-xl leading-relaxed">
                        CDPH compliant multi-topic assessment. Minimum 80% score required. No correct answer keys are displayed following submission to preserve compliance integrity.
                      </p>
                    </div>
                    
                    <div className="shrink-0 font-sans">
                      {finalAssessmentPassed ? (
                        <div className="flex items-center gap-2 bg-emerald-50 border border-emerald-200 text-emerald-800 px-4 py-2 rounded-lg font-semibold text-xs shadow-sm">
                          <CheckCircle2 size={14} /> Passed ({finalAssessmentScore}%)
                        </div>
                      ) : m1AssessmentPassed ? (
                        <button 
                          onClick={() => setCurrentView('finalAssessmentSplash')}
                          className="bg-[#8B1515] hover:bg-[#a61a1a] text-white border border-[#8B1515] font-semibold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors shadow-sm"
                        >
                          Enter Final Assessment
                        </button>
                      ) : (
                        <div className="flex items-center gap-2 bg-stone-100 border border-stone-200 text-stone-500 px-4 py-2 rounded text-xs font-semibold font-mono">
                          <Lock size={12} /> Locked
                        </div>
                      )}
                    </div>
                  </div>
                </div>

              </div>
            </div>
          )}

          {/* VIEW: MODULE 0 ORIENTATION & COMPLIANCE */}
          {currentView === 'module0' && (
            <div className="max-w-3xl mx-auto space-y-6 animate-in fade-in duration-300 font-sans">
              <button 
                onClick={() => setCurrentView('modules')} 
                className="text-stone-600 hover:text-[#212529] flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider font-sans"
              >
                <ArrowLeft size={14} /> Back to Modules
              </button>

              <div className="bg-white border border-[#DEE2E6] rounded-xl p-6 md:p-10 shadow-sm space-y-6">
                <div>
                  <div className="text-[10px] uppercase tracking-widest text-[#8B1515] font-bold mb-1 font-mono">Required Step • Module 0</div>
                  <h1 className="text-3xl font-bold text-[#212529] tracking-tight">Identity & Compliance Orientation</h1>
                  <p className="text-xs text-stone-500 leading-relaxed mt-1">
                    Please audit and sign the mandatory compliance declarations. Accurate PHI warnings must be observed throughout the active session.
                  </p>
                </div>

                <div className="space-y-4 pt-4 border-t border-stone-200">
                  <h3 className="text-xs uppercase tracking-wider font-bold text-[#212529]">1. Verification of Legal CNA Identity</h3>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                      <label className="block text-[10px] uppercase font-bold text-stone-500 mb-1 font-mono">First Name (Legal)</label>
                      <input 
                        type="text" 
                        value={m0FirstName} 
                        onChange={(e) => setM0FirstName(e.target.value)}
                        className="w-full bg-[#F8F9FA] border border-[#DEE2E6] text-[#212529] text-xs px-3 py-2 rounded focus:outline-none focus:border-[#FFC107]"
                      />
                    </div>
                    <div>
                      <label className="block text-[10px] uppercase font-bold text-stone-500 mb-1 font-mono">Last Name (Legal)</label>
                      <input 
                        type="text" 
                        value={m0LastName} 
                        onChange={(e) => setM0LastName(e.target.value)}
                        className="w-full bg-[#F8F9FA] border border-[#DEE2E6] text-[#212529] text-xs px-3 py-2 rounded focus:outline-none focus:border-[#FFC107]"
                      />
                    </div>
                    <div>
                      <label className="block text-[10px] uppercase font-bold text-stone-500 mb-1 font-mono">CNA Certificate Number</label>
                      <input 
                        type="text" 
                        value={m0License} 
                        onChange={(e) => setM0License(e.target.value)}
                        className="w-full bg-[#F8F9FA] border border-[#DEE2E6] text-[#212529] text-xs px-3 py-2 rounded font-mono focus:outline-none focus:border-[#FFC107]"
                      />
                    </div>
                  </div>
                </div>

                <div className="space-y-3 pt-4 border-t border-stone-200">
                  <h3 className="text-xs uppercase tracking-wider font-bold text-[#212529]">2. Mandatory Declarations & Acknowledgements</h3>
                  
                  {[
                    "I certify that my legal CNA identity matches the credential entered above, and that I alone will complete this CE training program.",
                    "No-PHI Safeguards Active: I acknowledge that I will NEVER enter real Protected Health Information (PHI), client records, or actual identifier keys anywhere in this portal.",
                    "I understand this 12-hour CE program satisfies theory credit ONLY. It does not certify practical hours or complete California CNA licensing on its own."
                  ].map((text, i) => (
                    <div 
                      key={i} 
                      onClick={() => {
                        const next = [...module0Agreed];
                        next[i] = !next[i];
                        setModule0Agreed(next);
                      }}
                      className={`p-4 rounded border cursor-pointer flex items-start gap-3 transition-colors ${
                        module0Agreed[i] 
                          ? 'bg-[#8B1515]/5 border-[#8B1515]/30 text-[#212529]' 
                          : 'bg-white border-[#DEE2E6] hover:border-stone-400 text-stone-500'
                      }`}
                    >
                      <div className="mt-0.5 text-[#8B1515] shrink-0">
                        {module0Agreed[i] ? <CheckSquare size={16} /> : <Square size={16} />}
                      </div>
                      <p className="text-xs leading-relaxed">{text}</p>
                    </div>
                  ))}
                </div>

                <div className="pt-6 border-t border-stone-200 flex items-center justify-between">
                  <div className="text-xs text-stone-500">
                    {!module0Agreed.every(Boolean) && "Select all 3 agreements to proceed."}
                  </div>
                  <button 
                    onClick={() => {
                      setModule0Completed(true);
                      setCurrentView('modules');
                    }}
                    disabled={!module0Agreed.every(Boolean)}
                    className="bg-[#8B1515] hover:bg-[#a61a1a] text-white border border-[#8B1515] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-all disabled:opacity-40 disabled:cursor-not-allowed shadow-sm"
                  >
                    Confirm & Unlock Module 1
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* VIEW: MODULE 1 OVERVIEW */}
          {currentView === 'module1' && (
            <div className="max-w-3xl mx-auto space-y-6 animate-in fade-in duration-300 font-sans">
              <button 
                onClick={() => setCurrentView('modules')} 
                className="text-stone-600 hover:text-[#212529] flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider"
              >
                <ArrowLeft size={14} /> Back to Modules
              </button>

              <div className="bg-white border border-[#DEE2E6] rounded-xl p-6 md:p-8 shadow-sm">
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-[#DEE2E6]">
                  <div>
                    <span className="text-[10px] uppercase font-bold text-[#8B1515] font-mono">Module 1 • 1.5 Theory Hours</span>
                    <h1 className="text-2xl font-bold text-[#212529] tracking-tight">Infection Control & PPE</h1>
                  </div>
                  <div className="shrink-0 flex items-center gap-2">
                    <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded text-[10px] font-bold ${
                      m1AssessmentPassed ? 'bg-emerald-100 text-emerald-800 border border-emerald-200' : 'bg-amber-100 text-amber-800 border border-amber-200'
                    }`}>
                      {m1AssessmentPassed ? 'Complete' : 'Not Attempted'}
                    </span>
                  </div>
                </div>

                <div className="py-6 space-y-4">
                  <h3 className="text-xs uppercase tracking-wider font-bold text-stone-500 font-sans">Lesson Objectives</h3>
                  <div className="grid grid-cols-1 gap-2.5">
                    {[
                      "Recall the six distinct structural links in the chain of infection.",
                      "Formulate proper WHO handwashing strategies and determine active timings.",
                      "Acknowledge critical indications for Contact, Droplet, and Airborne barriers."
                    ].map((obj, idx) => (
                      <div key={idx} className="flex gap-2.5 items-start text-xs text-stone-500 leading-relaxed">
                        <span className="text-[#8B1515] font-bold font-mono">0{idx+1}.</span>
                        <span>{obj}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Lesson Track List */}
                <div className="space-y-3 pt-4 border-t border-[#DEE2E6]">
                  <h3 className="text-xs uppercase tracking-wider font-bold text-stone-500 font-sans">Course Component Lessons</h3>
                  
                  <div 
                    onClick={() => setCurrentView('lesson')}
                    className="p-4 rounded border bg-white border-[#DEE2E6] hover:border-[#8B1515] hover:bg-[#F8F9FA] transition-all cursor-pointer flex items-center justify-between shadow-sm"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded bg-[#8B1515]/5 flex items-center justify-center border border-[#8B1515]/20 text-[#8B1515] font-bold font-mono text-xs">
                        1
                      </div>
                      <div>
                        <h4 className="text-xs font-semibold text-[#212529]">The Chain of Infection & Standard Precautions</h4>
                        <span className="text-[10px] text-stone-400 font-mono uppercase tracking-wide">Structured Theory &bull; 4-Card Player</span>
                      </div>
                    </div>
                    <div className="flex items-center gap-2 text-xs text-[#8B1515] font-semibold uppercase tracking-wider">
                      {lessonCompleted ? (
                        <span className="text-emerald-600 flex items-center gap-1 text-[10px] font-bold">
                          <CheckCircle2 size={12} /> Finished
                        </span>
                      ) : (
                        <span className="text-[#8B1515] flex items-center gap-1 text-[10px] font-bold">
                          <Play size={12} className="fill-current" /> Play
                        </span>
                      )}
                    </div>
                  </div>

                  <div className="p-4 rounded border bg-[#F8F9FA]/40 border-[#DEE2E6] opacity-60 flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded bg-[#DEE2E6] flex items-center justify-center text-stone-500 font-bold font-mono text-xs">
                        2
                      </div>
                      <div>
                        <h4 className="text-xs font-semibold text-stone-400">Clinical Isolation & PPE Selection Sequence</h4>
                        <span className="text-[10px] text-stone-400 font-mono uppercase tracking-wide">Visual Demonstration</span>
                      </div>
                    </div>
                    <span className="text-[10px] text-stone-500 font-bold uppercase tracking-wider">SEQUENTIAL LOCK</span>
                  </div>

                </div>

                <div className="pt-8 border-t border-[#DEE2E6] flex flex-col sm:flex-row items-center gap-4 justify-between">
                  <div className="text-xs text-stone-500">
                    {lessonCompleted ? "Theory lessons complete. Complete the assessment." : "Complete Lesson 1 to unlock the Module Assessment."}
                  </div>
                  <div className="flex gap-3 w-full sm:w-auto">
                    {lessonCompleted && (
                      <button 
                        onClick={() => setCurrentView('m1Assessment')}
                        className="w-full sm:w-auto bg-[#8B1515] hover:bg-[#a61a1a] text-white border border-[#8B1515] font-semibold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors shadow-sm"
                      >
                        Start Module 1 Assessment
                      </button>
                    )}
                    <button 
                      onClick={() => setCurrentView('lesson')}
                      className="w-full sm:w-auto bg-stone-100 hover:bg-stone-200 border border-stone-300 text-stone-700 font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors shadow-sm"
                    >
                      {lessonCompleted ? 'Review Theory' : 'Start Theory'}
                    </button>
                  </div>
                </div>
              </div>
            </div>
          )}

        </div>
      </main>
    </div>
  );
}

// ==========================================
// COMPONENT: SIGN-IN VIEW (Light Mode Optimized)
// ==========================================
function SignInView({ setView, m0FirstName, m0LastName, m0License, brandingMode, setBrandingMode }) {
  const [username, setUsername] = useState('james.bond');
  const [password, setPassword] = useState('••••••••••••');
  const [showPassword, setShowPassword] = useState(false);
  const isDark = brandingMode === 'dark';

  const handleSignInSubmit = (e) => {
    e.preventDefault();
    setView('dashboard');
  };

  return (
    <div className="min-h-[82vh] flex items-center justify-center py-6 px-4 sm:px-6 lg:px-8 relative z-10 animate-in fade-in zoom-in-95 duration-500 no-print font-sans">
      <div className="ci-signin-card w-full max-w-[618px] space-y-8 bg-white border border-[#DEE2E6] rounded-2xl p-8 sm:p-12 shadow-[0_25px_60px_rgba(0,0,0,0.06),_0_0_50px_rgba(139,21,21,0.02)] relative overflow-hidden">

        {/* Minimalist Theme Toggle Top-Right */}
        <div className="absolute top-4 right-4 z-20">
          <ThemeToggle brandingMode={brandingMode} setBrandingMode={setBrandingMode} />
        </div>
        
        {/* top glowing maroon line indicator */}
        <div className="absolute top-0 inset-x-0 h-[3px] bg-gradient-to-r from-transparent via-[#8B1515] to-transparent"></div>

        {/* Branding header logo */}
        <div className="border-b border-[#DEE2E6] pb-6 flex flex-col items-start gap-4">
          <div className="relative">
            <img 
              src={isDark
                ? "https://ciinstituteofnursing.com/assets/logos/ci-ion-logo-white.svg"
                : "https://ciinstituteofnursing.com/assets/logos/ci-ion-logo-original.svg"} 
              className="h-20 sm:h-[84px] w-auto object-contain transition-all" 
              alt="CI Institute of Nursing"
              onError={(e) => {
                e.currentTarget.style.display = 'none';
                const parent = e.currentTarget.parentElement;
                if (parent) {
                  const fallbackSpan = document.createElement('span');
                  fallbackSpan.className = "text-[#8B1515] font-bold text-lg tracking-tighter";
                  fallbackSpan.innerText = "CI INSTITUTE OF NURSING";
                  parent.appendChild(fallbackSpan);
                }
              }}
            />
          </div>
          <span className="text-[10px] text-stone-500 font-sans uppercase tracking-[0.18em] block font-extrabold">
            NURSING EXCELLENCE. ELEVATING CARE.
          </span>
        </div>

        {/* Welcome titles */}
        <div className="space-y-4">
          <h2 className="text-3xl sm:text-[38px] leading-[1.12] text-[#212529] font-sans font-bold tracking-tight select-none">
            Welcome back.<br />
            Let's continue your<br />
            journey.
          </h2>
          <div className="text-xs uppercase tracking-wider text-[#FFC107] font-extrabold font-sans">
            CNA Recertification Theory + Clinical Support
          </div>
          <p className="text-xs sm:text-sm text-stone-500 leading-relaxed font-sans">
            Complete your required online theory and strengthen your skills through optional clinical support.
          </p>
        </div>

        {/* Form fields */}
        <form onSubmit={handleSignInSubmit} className="space-y-6 mt-4">
          <div className="space-y-4">
            
            {/* Username */}
            <div>
              <label className="block text-[10px] uppercase font-bold text-[#8B1515] font-mono tracking-widest mb-1.5 pl-0.5">
                Username
              </label>
              <div className="relative rounded-lg shadow-sm">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-stone-400">
                  <User size={15} />
                </div>
                <input
                  type="text"
                  required
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="block w-full pl-10 pr-3 py-3 border border-[#DEE2E6] bg-[#F8F9FA] text-[#212529] placeholder-stone-400 rounded-lg text-xs focus:outline-none focus:ring-1 focus:ring-[#FFC107] focus:border-[#FFC107] transition-all font-sans"
                  placeholder="Enter your username"
                />
              </div>
            </div>

            {/* Password */}
            <div>
              <label className="block text-[10px] uppercase font-bold text-[#8B1515] font-mono tracking-widest mb-1.5 pl-0.5">
                Password
              </label>
              <div className="relative rounded-lg shadow-sm">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-stone-400">
                  <Lock size={15} />
                </div>
                <input
                  type={showPassword ? "text" : "password"}
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="block w-full pl-10 pr-16 py-3 border border-[#DEE2E6] bg-[#F8F9FA] text-[#212529] placeholder-stone-400 rounded-lg text-xs focus:outline-none focus:ring-1 focus:ring-[#FFC107] focus:border-[#FFC107] transition-all font-sans"
                  placeholder="Enter your password"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute inset-y-0 right-0 pr-3 flex items-center text-[10px] font-mono font-bold text-[#8B1515] hover:text-[#a61a1a] transition-colors uppercase tracking-wider"
                >
                  {showPassword ? "Hide" : "Show"}
                </button>
              </div>
              <div className="flex justify-end mt-2">
                <a href="#forgot" className="text-[10px] uppercase tracking-wider font-bold text-stone-400 hover:text-[#8B1515] transition-colors">
                  Forgot password?
                </a>
              </div>
            </div>

          </div>

          {/* School Card */}
          <div className="p-4 rounded-xl border border-[#DEE2E6] bg-[#F8F9FA] hover:bg-stone-50 hover:border-stone-300 transition-all cursor-pointer flex items-center justify-between group">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded bg-[#8B1515]/5 flex items-center justify-center border border-[#8B1515]/10 text-[#8B1515] shrink-0">
                <svg className="w-4.5 h-4.5 text-[#8B1515]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3V6z" />
                  <path d="M9 3v15" />
                  <path d="M15 6v15" />
                </svg>
              </div>
              <div>
                <h4 className="text-xs font-bold text-[#212529] font-sans">Are you signing in at a facility or school?</h4>
                <p className="text-[9.5px] text-stone-500 font-sans mt-0.5">Access your organization's local portal</p>
              </div>
            </div>
            <ChevronRight size={14} className="text-stone-400 group-hover:text-[#8B1515] group-hover:translate-x-0.5 transition-all shrink-0" />
          </div>

          {/* Submit */}
          <div>
            <button
              type="submit"
              className="w-full py-3.5 px-4 rounded-lg font-bold text-xs uppercase tracking-wider text-white bg-[#8B1515] hover:bg-[#a61a1a] border border-[#8B1515] shadow-md hover:shadow-[0_4px_20px_rgba(139,21,21,0.2)] transition-all flex items-center justify-between group"
            >
              <span className="flex-1 text-center pl-4 font-sans">Sign in</span>
              <ChevronRight size={14} className="group-hover:translate-x-0.5 transition-transform text-white shrink-0" />
            </button>
          </div>

          {/* Monitoring disclaimer */}
          <div className="pt-4 border-t border-[#DEE2E6] flex items-start gap-2.5 text-[10px] text-stone-500 leading-relaxed font-sans">
            <ShieldCheck size={14} className="text-stone-400 shrink-0 mt-0.5" />
            <span>This is a reviewer and stakeholder access environment for CI Institute of Nursing. Use is monitored and logged.</span>
          </div>

        </form>

      </div>
    </div>
  );
}

// ==========================================
// COMPONENT: HIGH-FIDELITY 4-CARD PLAYER
// ==========================================
function LessonPlayerView({ setView, setLessonCompleted, activeTime, formatHoursAndMins }) {
  const [currentCard, setCurrentCard] = useState(1);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);
  const [showTranscript, setShowTranscript] = useState(false);
  const [clickedRationales, setClickedRationales] = useState([]);

  const handleNext = () => {
    if (currentCard < 4) {
      setCurrentCard(c => c + 1);
    } else {
      setLessonCompleted(true);
      setView('module1');
    }
  };

  const handlePrev = () => {
    if (currentCard > 1) {
      setCurrentCard(c => c - 1);
    }
  };

  const selectAnswer = (id) => {
    if (!submitted) setSelectedAnswer(id);
  };

  const handleRationaleClick = (id) => {
    if (!clickedRationales.includes(id)) {
      setClickedRationales([...clickedRationales, id]);
    }
  };

  return (
    <div className="space-y-6 animate-in zoom-in-95 duration-300 font-sans">
      
      {/* Header Info */}
      <div className="flex items-center justify-between pb-3 border-b border-stone-200">
        <button 
          onClick={() => setView('module1')}
          className="text-stone-600 hover:text-[#212529] flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider"
        >
          <ArrowLeft size={14} /> Close Player
        </button>
        <div className="flex items-center gap-4 text-xs font-mono text-stone-500">
          <span className="flex items-center gap-1"><Clock size={12} className="text-[#8B1515]" /> Lesson Session: 15m</span>
          <span>&bull;</span>
          <span className="text-[#8B1515] flex items-center gap-1 font-bold">
            <span className="w-1.5 h-1.5 rounded-full bg-[#8B1515] animate-pulse"></span>
            Simulated Time: {formatHoursAndMins(activeTime)}
          </span>
        </div>
      </div>

      {/* Steps indicators */}
      <div className="flex items-center justify-between bg-stone-100 p-3 rounded-lg border border-[#DEE2E6] overflow-x-auto">
        {[
          { num: 1, name: "Card 1: Overview" },
          { num: 2, name: "Card 2: Delivery" },
          { num: 3, name: "Card 3: Challenge" },
          { num: 4, name: "Card 4: Debrief & Remediation" },
        ].map((step) => (
          <div key={step.num} className="flex items-center gap-3 shrink-0 mx-2">
            <div className={`w-5 h-5 rounded-full border flex items-center justify-center text-[10px] font-mono font-bold ${
              currentCard === step.num 
                ? 'bg-[#8B1515] border-[#8B1515] text-white' 
                : currentCard > step.num 
                  ? 'bg-emerald-100 text-emerald-800 border-emerald-300' 
                  : 'bg-transparent border-stone-300 text-stone-400'
            }`}>
              {currentCard > step.num ? <Check size={10} /> : step.num}
            </div>
            <span className={`text-[11px] font-semibold uppercase tracking-wider ${
              currentCard === step.num ? 'text-[#8B1515]' : 'text-stone-500'
            }`}>
              {step.name}
            </span>
            {step.num < 4 && <div className="w-6 h-px bg-stone-300"></div>}
          </div>
        ))}
      </div>

      {/* Main card panel */}
      <div className="bg-white border border-[#DEE2E6] rounded-xl overflow-hidden shadow-sm flex flex-col min-h-[500px]">
        <div className="p-6 md:p-8 flex-1 space-y-6">
          
          {/* Card 1: Overview */}
          {currentCard === 1 && (
            <div className="space-y-6 animate-in fade-in duration-300">
              <span className="text-[10px] font-bold text-[#8B1515] uppercase tracking-widest font-mono">Module 1 • Lesson 1 • Card 1</span>
              <h2 className="text-2xl font-bold text-[#212529] tracking-tight">Scope of Infection Control in LTC</h2>

              {/* Blueprint */}
              <div className="w-full aspect-video md:h-64 bg-stone-50 border border-[#DEE2E6] rounded-lg flex flex-col items-center justify-center relative overflow-hidden group shadow-inner">
                <span className="absolute top-3 left-3 bg-white border border-[#DEE2E6] rounded px-2 py-0.5 text-[9px] font-mono text-stone-500 uppercase tracking-wider">
                  Visual Blueprint L1-1
                </span>
                <svg className="w-32 h-32 text-stone-300" viewBox="0 0 100 100" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <rect x="15" y="15" width="70" height="70" rx="3" />
                  <path d="M50 15v70M15 50h70" strokeDasharray="3 3" />
                  <circle cx="50" cy="50" r="10" stroke="#8B1515" strokeWidth="2" />
                  <circle cx="30" cy="35" r="5" fill="#DEE2E6" />
                  <circle cx="70" cy="35" r="5" fill="#DEE2E6" />
                  <circle cx="30" cy="65" r="5" fill="#DEE2E6" />
                  <circle cx="70" cy="65" r="5" fill="#DEE2E6" />
                </svg>
                <span className="text-[10px] font-mono text-stone-500 uppercase mt-2 tracking-widest">
                  Pathogen Proliferation Model
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <h4 className="text-xs uppercase font-bold text-stone-700 font-mono tracking-wider mb-2">Core Principle</h4>
                  <p className="text-xs text-stone-600 leading-relaxed">
                    Long-term care facilities house highly vulnerable populations. As a CNA, your hand sanitation and PPE execution are the frontline defenses against devastating healthcare-associated infections (HAIs).
                  </p>
                </div>
                <div>
                  <h4 className="text-xs uppercase font-bold text-stone-700 font-mono tracking-wider mb-2 font-semibold">Core Focus Metrics</h4>
                  <div className="space-y-1.5 font-mono text-[10px] text-stone-500">
                    <div className="flex justify-between border-b border-stone-100 pb-1">
                      <span>LTC Infection Rates:</span>
                      <span className="text-[#212529] font-bold">1:10 Active Residents</span>
                    </div>
                    <div className="flex justify-between border-b border-stone-100 pb-1">
                      <span>Primary Transmission:</span>
                      <span className="text-[#212529] font-bold">Transient Hand Contact</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Card 2: Delivery */}
          {currentCard === 2 && (
            <div className="space-y-6 animate-in fade-in duration-300">
              <span className="text-[10px] font-bold text-[#8B1515] uppercase tracking-widest font-mono">Module 1 • Lesson 1 • Card 2</span>
              <h2 className="text-2xl font-bold text-[#212529] tracking-tight">Understanding the Chain of Infection</h2>

              <div className="w-full aspect-video md:h-64 bg-stone-50 border border-[#DEE2E6] rounded-lg flex flex-col items-center justify-center relative overflow-hidden shadow-inner">
                <span className="absolute top-3 left-3 bg-white border border-[#DEE2E6] rounded px-2 py-0.5 text-[9px] font-mono text-stone-500 uppercase tracking-wider">
                  Visual Blueprint L1-2
                </span>
                <svg className="w-64 h-24 text-stone-300" viewBox="0 0 300 100" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <rect x="10" y="30" width="60" height="40" rx="20" stroke="#FFC107" strokeWidth="2" />
                  <rect x="50" y="30" width="60" height="40" rx="20" />
                  <rect x="90" y="30" width="60" height="40" rx="20" stroke="#FFC107" strokeWidth="2" />
                  <rect x="130" y="30" width="60" height="40" rx="20" />
                  <rect x="170" y="30" width="60" height="40" rx="20" stroke="#FFC107" strokeWidth="2" />
                  <rect x="210" y="30" width="60" height="40" rx="20" />
                </svg>
                <div className="text-[10px] font-mono text-stone-500 uppercase tracking-widest mt-2">
                  Chain Links representation
                </div>
              </div>

              <div className="space-y-3">
                <h4 className="text-xs uppercase font-bold text-stone-700 font-mono tracking-wider">Breaking the Pathogen Cycle</h4>
                <p className="text-xs text-stone-600 leading-relaxed">
                  The six active links are: (1) Causative Agent, (2) Reservoir, (3) Portal of Exit, (4) Mode of Transmission, (5) Portal of Entry, and (6) Susceptible Host. Interruption at any of these nodes instantly halts contamination spread.
                </p>
                <div className="p-3 bg-stone-50 border border-stone-200 rounded">
                  <p className="text-[11px] text-[#212529] leading-relaxed italic">
                    <strong>Critical CNA Link:</strong> Performing hand decontamination after client contact breaks the <em>Mode of Transmission</em> link.
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* Card 3: Challenge */}
          {currentCard === 3 && (
            <div className="space-y-6 animate-in fade-in duration-300">
              <span className="text-[10px] font-bold text-[#8B1515] uppercase tracking-widest font-mono">Module 1 • Lesson 1 • Card 3</span>
              <h2 className="text-2xl font-bold text-[#212529] tracking-tight">Interactive Challenge Simulation</h2>

              <div className="w-full aspect-video md:h-56 bg-stone-50 border border-[#DEE2E6] rounded-lg flex flex-col items-center justify-center relative overflow-hidden shadow-inner">
                <span className="absolute top-3 left-3 bg-white border border-[#DEE2E6] rounded px-2 py-0.5 text-[9px] font-mono text-stone-500 uppercase tracking-wider">
                  Simulation Scene L1-3
                </span>
                <svg className="w-24 h-24 text-stone-300" viewBox="0 0 100 100" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <path d="M20 80h60M30 80V40h40v40" />
                  <path d="M40 30h20M50 20v10" />
                  <circle cx="50" cy="55" r="8" stroke="#FFC107" />
                </svg>
                <div className="text-[10px] font-mono text-stone-500 uppercase tracking-widest mt-2">
                  Client Room Environment
                </div>
              </div>

              <div className="space-y-4">
                <p className="text-xs text-stone-700 leading-relaxed font-semibold">
                  SCENARIO: Mr. Henderson is on Contact Precautions for a suspected MRSA wound infection. As you prepare to deliver a fresh water pitcher, what is your safest procedural sequence?
                </p>

                <div className="grid grid-cols-1 gap-2.5">
                  {[
                    { id: 'A', text: "Sanitize hands, don clean gown and gloves before entering room, deliver water, doff PPE inside room, sanitize hands upon exit." },
                    { id: 'B', text: "Deliver water quickly using gloves only. No gown is required unless changing bed sheets." },
                    { id: 'C', text: "Don gown and gloves outside room, deliver water, walk out into the hallway in PPE, doff at nurse station." },
                  ].map((ans) => (
                    <button
                      key={ans.id}
                      onClick={() => selectAnswer(ans.id)}
                      disabled={submitted}
                      className={`w-full text-left p-4 rounded border text-xs flex items-start gap-3 transition-colors ${
                        selectedAnswer === ans.id 
                          ? 'bg-[#8B1515]/5 border-[#8B1515]/30 text-[#212529]' 
                          : 'bg-[#F8F9FA] border-stone-200 hover:border-stone-400 text-stone-700'
                      }`}
                    >
                      <div className={`mt-0.5 w-4 h-4 rounded border flex items-center justify-center text-[10px] font-bold shrink-0 ${
                        selectedAnswer === ans.id ? 'bg-[#8B1515] text-white border-[#8B1515]' : 'border-stone-400 text-stone-500'
                      }`}>
                        {ans.id}
                      </div>
                      <span>{ans.text}</span>
                    </button>
                  ))}
                </div>

                {!submitted && selectedAnswer && (
                  <button 
                    onClick={() => setSubmitted(true)}
                    className="bg-[#8B1515] hover:bg-[#a61a1a] text-white font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors shadow-sm"
                  >
                    Submit Decision Pattern
                  </button>
                )}
              </div>
            </div>
          )}

          {/* Card 4: Debrief */}
          {currentCard === 4 && (
            <div className="space-y-6 animate-in fade-in duration-300">
              <span className="text-[10px] font-bold text-[#8B1515] uppercase tracking-widest font-mono">Module 1 • Lesson 1 • Card 4</span>
              <h2 className="text-2xl font-bold text-[#212529] tracking-tight">Review & Rationale Matrix</h2>
              <p className="text-xs text-stone-500">
                Compliance review requires interacting with both the Correct (A) and your selected choice rationales to finalize the block.
              </p>

              <div className="space-y-3">
                {[
                  {
                    id: 'A',
                    type: 'CORRECT OPTION',
                    title: "Standard Contact Precautions Protocol",
                    text: "Putting on PPE BEFORE room entry stops contamination. Correct doffing inside prevents tracking pathogens into corridor hallways.",
                    correct: true
                  },
                  {
                    id: 'B',
                    type: 'INCORRECT OPTION',
                    title: "Limited Barrier Protective Assumption",
                    text: "Mr. Henderson's room handles (bedside, water pitcher) are high reservoirs. Gloves only are completely deficient.",
                    correct: false
                  },
                  {
                    id: 'C',
                    type: 'INCORRECT OPTION',
                    title: "PPE Leakage Mode",
                    text: "Walking outside the isolation area wearing active contaminated gloves creates a critical Mode of Transmission risk.",
                    correct: false
                  }
                ].map((item) => {
                  const isClicked = clickedRationales.includes(item.id);
                  return (
                    <div 
                      key={item.id} 
                      onClick={() => handleRationaleClick(item.id)}
                      className={`p-4 rounded border text-xs cursor-pointer transition-all ${
                        isClicked 
                          ? 'bg-[#F8F9FA] border-[#8B1515]/30' 
                          : 'bg-white border-[#DEE2E6] hover:bg-stone-50'
                      }`}
                    >
                      <div className="flex items-center justify-between mb-2">
                        <div className="flex items-center gap-2">
                          <span className={`px-2 py-0.5 rounded text-[9px] font-mono font-bold ${
                            item.correct ? 'bg-emerald-100 text-emerald-800' : 'bg-red-100 text-red-800'
                          }`}>
                            {item.id} &bull; {item.type}
                          </span>
                          <h4 className="font-semibold text-[#212529]">{item.title}</h4>
                        </div>
                        <span className="text-[10px] text-[#8B1515] font-mono font-bold">
                          {isClicked ? "✓ Verified" : "Click to Review"}
                        </span>
                      </div>
                      {isClicked && (
                        <p className="text-stone-600 leading-relaxed pl-1 animate-in slide-in-from-top-1">
                          {item.text}
                        </p>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>
          )}

        </div>

        {/* Audio controller */}
        <div className="px-6 py-4 bg-[#F8F9FA] border-t border-[#DEE2E6] flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <button 
              onClick={() => setIsPlaying(!isPlaying)}
              className="w-10 h-10 rounded-full bg-white border border-[#DEE2E6] flex items-center justify-center text-[#8B1515] hover:bg-stone-50 transition-colors shrink-0 shadow-sm"
            >
              {isPlaying ? <Pause size={16} className="fill-current" /> : <Play size={16} className="fill-current ml-0.5" />}
            </button>
            <div>
              <span className="text-xs font-semibold text-[#212529] block">Required Core Narration Audio</span>
              <span className="text-[10px] text-stone-500 font-mono block">
                {isPlaying ? "Active Playback Logged" : "Playback Standby"} (01:45)
              </span>
            </div>
          </div>

          <button 
            onClick={() => setShowTranscript(!showTranscript)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded border text-xs font-mono transition-all ${
              showTranscript 
                ? 'bg-[#8B1515]/5 text-[#8B1515] border-[#8B1515]/20 font-bold' 
                : 'bg-transparent border-stone-200 text-stone-500 hover:text-[#212529]'
            }`}
          >
            <FileText size={12} /> Transcript Text
          </button>
        </div>

        {showTranscript && (
          <div className="px-6 py-4 bg-stone-50 text-stone-600 text-xs italic leading-relaxed border-t border-[#DEE2E6] animate-in fade-in">
            &ldquo;In this nursing recertification system, standard precautions dictate treating all biological fluids as infectious. CNAs must construct physical barriers prior to touching potential host reservoirs like resident nightstands, catheters, or bed rails. Complete rationale review ensures clinical safety audit compliance.&rdquo;
          </div>
        )}

        {/* Navigation buttons */}
        <div className="px-6 py-4 bg-white border-t border-[#DEE2E6] flex items-center justify-between">
          <button 
            onClick={handlePrev}
            disabled={currentCard === 1}
            className="px-4 py-2 text-xs font-semibold text-stone-500 hover:text-[#212529] disabled:opacity-35 uppercase tracking-wider"
          >
            &larr; Previous Card
          </button>
          <button 
            onClick={handleNext}
            disabled={currentCard === 3 && !submitted}
            className="bg-[#8B1515] hover:bg-[#a61a1a] text-white font-bold px-6 py-2.5 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40"
          >
            {currentCard === 4 ? "Complete Theory Lesson" : "Continue"} &rarr;
          </button>
        </div>

      </div>
    </div>
  );
}

// ==========================================
// COMPONENT: CORE QUIZ FLOW (MODULAR)
// ==========================================
function QuizFlowView({ setView, isFinalExam, onPass, onFail }) {
  const [currentIdx, setCurrentIdx] = useState(0);
  const [answers, setAnswers] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  const questions = [
    {
      id: 1,
      q: "Which link inside the standard chain of infection does proper handwashing break?",
      options: [
        { id: 'A', text: "Reservoir Source" },
        { id: 'B', text: "Mode of Transmission" },
        { id: 'C', text: "Susceptible Host" },
        { id: 'D', text: "Portal of Entry" }
      ],
      correct: 'B'
    },
    {
      id: 2,
      q: "A resident has a suspected droplet-transmitted infection. What standard barriers are required prior to entry?",
      options: [
        { id: 'A', text: "Gown and N95 Mask only" },
        { id: 'B', text: "Standard Surgical Mask and eye protection shield if within 3 feet" },
        { id: 'C', text: "Standard gloves and shoe coverings only" }
      ],
      correct: 'B'
    },
    {
      id: 3,
      q: "What is the minimum active friction scrub duration required during standard handwashing under CDPH guidelines?",
      options: [
        { id: 'A', text: "10 Seconds" },
        { id: 'B', text: "20 Seconds" },
        { id: 'C', text: "5 Seconds" },
        { id: 'D', text: "60 Seconds" }
      ],
      correct: 'B'
    },
    {
      id: 4,
      q: "While performing standard catheter care, which safety measure stops retrograde contamination?",
      options: [
        { id: 'A', text: "Hanging the drainage bag higher than bladder level on the bed rail" },
        { id: 'B', text: "Always maintaining the drainage bag below bladder level" },
        { id: 'C', text: "Emptying the bag only once every 48 hours" }
      ],
      correct: 'B'
    },
    {
      id: 5,
      q: "HIPAA Rules: Which element represents a Protected Health Identifier that must never be entered in general study areas?",
      options: [
        { id: 'A', text: "Client medical record numbers" },
        { id: 'B', text: "General nursing scenario diagnosis" },
        { id: 'C', text: "CNA license number keys" }
      ],
      correct: 'A'
    }
  ];

  const handleSelect = (ansId) => {
    if (!isSubmitted) {
      setAnswers({ ...answers, [questions[currentIdx].id]: ansId });
    }
  };

  const handleNext = () => {
    if (currentIdx < questions.length - 1) {
      setCurrentIdx(currentIdx + 1);
    }
  };

  const handlePrev = () => {
    if (currentIdx > 0) {
      setCurrentIdx(currentIdx - 1);
    }
  };

  const handleSubmit = () => {
    setIsSubmitted(true);
    let correctCount = 0;
    questions.forEach(q => {
      if (answers[q.id] === q.correct) {
        correctCount++;
      }
    });

    const scorePct = Math.round((correctCount / questions.length) * 100);
    const passed = scorePct >= 80;

    if (passed) {
      onPass(scorePct);
    } else {
      onFail(scorePct);
    }
    setView('finalResult');
  };

  const currentQ = questions[currentIdx];
  const allAnswered = Object.keys(answers).length === questions.length;

  return (
    <div className="max-w-2xl mx-auto space-y-6 animate-in fade-in duration-300">
      <div className="flex justify-between items-center pb-3 border-b border-stone-200 font-mono text-xs text-stone-500">
        <span>Question {currentIdx + 1} of {questions.length}</span>
        <span>{isFinalExam ? "COURSE THEORY FINAL EXAM" : "MODULE 1 ASSESSMENT"}</span>
      </div>

      <div className="bg-white border border-[#DEE2E6] rounded-xl p-6 md:p-8 shadow-sm space-y-6">
        <div>
          <span className="text-[10px] font-bold text-[#8B1515] uppercase tracking-widest font-mono">Select One Response</span>
          <h2 className="text-base font-bold text-[#212529] mt-1 leading-relaxed">
            {currentQ.q}
          </h2>
        </div>

        <div className="grid grid-cols-1 gap-2.5">
          {currentQ.options.map((opt) => (
            <button
              key={opt.id}
              onClick={() => handleSelect(opt.id)}
              className={`w-full text-left p-4 rounded border text-xs flex items-start gap-3 transition-colors ${
                answers[currentQ.id] === opt.id 
                  ? 'bg-[#8B1515]/5 border-[#8B1515]/30 text-[#212529] font-semibold' 
                  : 'bg-[#F8F9FA] border-stone-200 hover:border-stone-400 text-stone-700'
              }`}
            >
              <div className={`mt-0.5 w-4 h-4 rounded border flex items-center justify-center text-[10px] font-bold shrink-0 ${
                answers[currentQ.id] === opt.id ? 'bg-[#8B1515] text-white border-[#8B1515]' : 'border-stone-400 text-stone-500'
              }`}>
                {opt.id}
              </div>
              <span>{opt.text}</span>
            </button>
          ))}
        </div>

        <div className="bg-stone-50 p-3 rounded border border-stone-200 text-[10px] text-stone-500 font-mono">
          CDPH Compliance Guardrail: Real-time validation checks enabled. Incorrect answers are simulated silently.
        </div>

        <div className="pt-4 border-t border-stone-200 flex justify-between">
          <button 
            onClick={handlePrev}
            disabled={currentIdx === 0}
            className="px-4 py-2 text-xs font-semibold text-[#8B1515] hover:underline disabled:opacity-35 disabled:no-underline uppercase tracking-wider"
          >
            Back
          </button>

          {currentIdx < questions.length - 1 ? (
            <button 
              onClick={handleNext}
              disabled={!answers[currentQ.id]}
              className="bg-[#8B1515] hover:bg-[#a61a1a] text-white font-bold px-5 py-2 rounded text-xs uppercase tracking-wider transition-colors shadow-sm"
            >
              Next
            </button>
          ) : (
            <button 
              onClick={handleSubmit}
              disabled={!allAnswered}
              className="bg-[#8B1515] hover:bg-[#a61a1a] text-white border border-[#8B1515] font-bold px-6 py-2.5 rounded text-xs uppercase tracking-wider transition-colors shadow-sm"
            >
              Submit Exam
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

// ==========================================
// COMPONENT: CERTIFICATE REVIEW & WATERMARK
// ==========================================
function CertificateGateView({ 
  setView, 
  module0Completed, 
  activeTime, 
  lessonCompleted, 
  finalAssessmentPassed, 
  affidavitSigned, 
  setAffidavitSigned,
  m0FirstName,
  m0LastName,
  m0License,
  formatHoursAndMins
}) {
  const [viewingMock, setViewingMock] = useState(false);

  const hoursCompleted = activeTime >= 43200; // 12 hours check
  const orientationReady = module0Completed;
  const theoryReady = lessonCompleted && finalAssessmentPassed;

  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      
      {!viewingMock ? (
        <div className="flex flex-col lg:flex-row gap-8">
          
          {/* Left: Audit Compliance Panel */}
          <div className="w-full lg:w-[400px] shrink-0 space-y-6">
            <div className="bg-white border border-[#DEE2E6] rounded-xl p-6 shadow-sm">
              <h2 className="text-lg font-bold text-[#212529] mb-2 uppercase tracking-wider">Required Audit Checklist</h2>
              <p className="text-xs text-stone-500 leading-relaxed mb-6">
                Official CDPH continuing education certificates remain locked unless all active gates are checked.
              </p>

              <div className="space-y-4">
                
                {/* Gate 1 */}
                <div className="flex items-start gap-3 p-3 bg-[#F8F9FA] border border-[#DEE2E6] rounded shadow-inner">
                  <div className="mt-0.5 shrink-0">
                    {orientationReady ? (
                      <CheckCircle2 size={16} className="text-emerald-600" />
                    ) : (
                      <Circle size={16} className="text-stone-400" />
                    )}
                  </div>
                  <div>
                    <span className="text-[11px] font-bold text-[#212529] block uppercase font-mono">01. Legal Identity Verified</span>
                    <span className="text-[10px] text-stone-500">First/Last name entered in Module 0.</span>
                  </div>
                </div>

                {/* Gate 2 */}
                <div className="flex items-start gap-3 p-3 bg-[#F8F9FA] border border-[#DEE2E6] rounded shadow-inner">
                  <div className="mt-0.5 shrink-0">
                    {hoursCompleted ? (
                      <CheckCircle2 size={16} className="text-emerald-600" />
                    ) : (
                      <Circle size={16} className="text-stone-400" />
                    )}
                  </div>
                  <div>
                    <span className="text-[11px] font-bold text-[#212529] block uppercase font-mono">02. 12-Hour Study Time</span>
                    <span className="text-[10px] text-stone-500">Logged session active: <strong className="text-[#8B1515] font-mono">{formatHoursAndMins(activeTime)}</strong></span>
                  </div>
                </div>

                {/* Gate 3 */}
                <div className="flex items-start gap-3 p-3 bg-[#F8F9FA] border border-[#DEE2E6] rounded shadow-inner">
                  <div className="mt-0.5 shrink-0">
                    {theoryReady ? (
                      <CheckCircle2 size={16} className="text-emerald-600" />
                    ) : (
                      <Circle size={16} className="text-stone-400" />
                    )}
                  </div>
                  <div>
                    <span className="text-[11px] font-bold text-[#212529] block uppercase font-mono">03. Competency Achieved</span>
                    <span className="text-[10px] text-stone-500">Modules Completed & Assessment Passed.</span>
                  </div>
                </div>

                {/* Gate 4 - Interactive Affidavit */}
                <div className={`p-4 rounded border transition-colors ${
                  affidavitSigned 
                    ? 'bg-emerald-50 border-emerald-200 text-emerald-800' 
                    : 'bg-[#8B1515]/5 border-[#8B1515]/20 text-[#8B1515]'
                }`}>
                  <div className="flex items-start gap-3">
                    <div className="mt-0.5 shrink-0">
                      {affidavitSigned ? (
                        <CheckCircle2 size={16} className="text-emerald-600" />
                      ) : (
                        <Circle size={16} className="text-[#8B1515]" />
                      )}
                    </div>
                    <div>
                      <span className="text-[11px] font-bold block uppercase font-mono">04. Professional Affidavit</span>
                      <p className="text-[10px] text-stone-500 mt-1 mb-3">
                        I swear under penalty of perjury that I completed all online continuing education hours in this portal myself.
                      </p>
                      {orientationReady && hoursCompleted && theoryReady ? (
                        <button 
                          onClick={() => setAffidavitSigned(!affidavitSigned)}
                          className={`w-full py-1.5 rounded text-[10px] font-bold uppercase tracking-wider transition-colors border ${
                            affidavitSigned 
                              ? 'bg-stone-200 border-stone-300 text-stone-700' 
                              : 'bg-[#8B1515] border-[#8B1515] hover:bg-[#a61a1a] text-white shadow-sm'
                          }`}
                        >
                          {affidavitSigned ? "Revoke Signature" : "Sign Digital Affidavit"}
                        </button>
                      ) : (
                        <span className="text-[9px] text-stone-400 uppercase font-mono font-bold block">
                          Locked (Complete Steps 1-3 first)
                        </span>
                      )}
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>

          {/* Right: Immersive Mock Certificate Preview */}
          <div className="flex-1 space-y-6">
            <div className="bg-white border border-[#DEE2E6] rounded-xl p-6 relative overflow-hidden shadow-sm">
              <div className="flex items-center justify-between mb-4 pb-3 border-b border-[#DEE2E6]">
                <h3 className="font-semibold text-stone-700 text-xs uppercase tracking-wider">Preview Engine</h3>
                <span className="text-[10px] font-bold font-mono text-red-700 bg-red-100 px-2 py-0.5 rounded border border-red-200">
                  MOCK ONLY &bull; PRODUCTION DISABLED
                </span>
              </div>

              {orientationReady && hoursCompleted && theoryReady && affidavitSigned ? (
                <div className="p-8 text-center space-y-6 bg-[#F8F9FA] rounded-lg border border-[#DEE2E6]">
                  <div className="w-16 h-16 rounded-full bg-emerald-100 border border-emerald-200 flex items-center justify-center mx-auto text-emerald-600 animate-bounce">
                    <ShieldCheck size={32} />
                  </div>
                  <div>
                    <h2 className="text-2xl font-bold text-[#212529]">Compliance Gates Cleared</h2>
                    <p className="text-xs text-stone-500 mt-2 max-w-md mx-auto leading-relaxed">
                      All required learner steps are complete. Production certificate issuance remains disabled until provider approval metadata is configured.
                    </p>
                  </div>
                  <div className="pt-2">
                    <button 
                      onClick={() => setViewingMock(true)}
                      className="bg-[#8B1515] hover:bg-[#a61a1a] text-white font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-all shadow-md"
                    >
                      View Mock Certificate Preview
                    </button>
                  </div>
                </div>
              ) : (
                <div className="p-12 text-center space-y-6 bg-[#F8F9FA] rounded-lg border border-[#DEE2E6]">
                  <div className="w-12 h-12 rounded-full bg-stone-200 border border-stone-300 flex items-center justify-center mx-auto text-stone-400">
                    <Lock size={20} />
                  </div>
                  <div>
                    <h2 className="text-lg font-semibold text-stone-700">Certificate Status Locked</h2>
                    <p className="text-xs text-stone-500 max-w-sm mx-auto leading-relaxed mt-1">
                      Complete legal verification, theoretical study modules, assessments, and the digital affidavit to unlock the mock certificate preview.
                    </p>
                  </div>
                </div>
              )}

              <div className="mt-4 p-4 rounded bg-stone-50 border border-[#DEE2E6]">
                <p className="text-xs text-stone-500 leading-relaxed font-sans">
                  <strong>Legal Action Restrictions:</strong> Official certificate downloading is permanently locked in preview environments. Real validation files are strictly generated on CDPH-audited production servers only.
                </p>
              </div>
            </div>
          </div>

        </div>
      ) : (
        <MockCertificateView 
          onClose={() => setViewingMock(false)}
          m0FirstName={m0FirstName}
          m0LastName={m0LastName}
          m0License={m0License}
          activeTime={activeTime}
          formatHoursAndMins={formatHoursAndMins}
        />
      )}

    </div>
  );
}

// ==========================================
// COMPONENT: MOCK CERTIFICATE DESIGN
// ==========================================
function MockCertificateView({ onClose, m0FirstName, m0LastName, m0License, activeTime, formatHoursAndMins }) {
  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      
      {/* Action panel above certificate */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 max-w-[1050px] mx-auto w-full no-print">
        <button 
          onClick={onClose}
          className="text-stone-600 hover:text-[#212529] flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider self-start"
        >
          <ArrowLeft size={14} /> Back to Gates
        </button>
        <div className="flex items-center gap-3">
          <span className="text-xs text-stone-500 italic">Production download disabled</span>
          <button disabled className="px-5 py-2 rounded bg-stone-100 text-stone-400 border border-[#DEE2E6] text-xs font-bold uppercase tracking-wider cursor-not-allowed">
            Print Certificate
          </button>
        </div>
      </div>

      {/* Certificate Frame Container */}
      <div className="w-full overflow-x-auto custom-scrollbar pb-12 flex justify-center">
        <div className="min-w-[950px] max-w-[1050px] w-full shrink-0 relative bg-white shadow-lg">
          
          <div className="relative w-full aspect-[11/8.5] bg-[#faf8f5] overflow-hidden flex flex-col text-stone-900 border-8 border-stone-800">
            
            {/* Ambient watermarking overlay */}
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-[#8B1515]/5 via-transparent to-transparent pointer-events-none"></div>

            {/* Large central watermarking text */}
            <div className="absolute inset-0 flex items-center justify-center rotate-[-15deg] select-none pointer-events-none opacity-5">
              <span className="text-7xl font-black font-mono tracking-widest text-stone-900">
                MOCK PREVIEW ONLY
              </span>
            </div>

            {/* QUADRANT 3 Floating Watermark (Specific compliance requested location) */}
            {/* Coordinates x:35-40% , y:62-68% */}
            <div 
              className="absolute select-none pointer-events-none z-30 opacity-25 border border-red-500 bg-red-50/75 px-3 py-1.5 text-center leading-none rounded"
              style={{ left: '38%', top: '65%', transform: 'translate(-50%, -50%) rotate(-12deg)' }}
            >
              <span className="text-[10px] font-bold text-red-700 tracking-wider font-mono block">
                MOCK PREVIEW ONLY
              </span>
              <span className="text-[7px] font-mono text-stone-600 block mt-0.5 uppercase">
                UNAUTHORIZED PRODUCTION
              </span>
            </div>

            {/* Outer border lines */}
            <div className="absolute inset-4 border-[3px] border-[#4a0f0f] pointer-events-none z-10"></div>
            <div className="absolute inset-6 border border-amber-600/40 pointer-events-none z-10"></div>

            {/* Gold Corner Accents */}
            <div className="absolute top-5 left-5 w-4 h-4 border-t-2 border-l-2 border-[#4a0f0f] z-10"></div>
            <div className="absolute top-5 right-5 w-4 h-4 border-t-2 border-r-2 border-[#4a0f0f] z-10"></div>
            <div className="absolute bottom-5 left-5 w-4 h-4 border-b-2 border-l-2 border-[#4a0f0f] z-10"></div>
            <div className="absolute bottom-5 right-5 w-4 h-4 border-b-2 border-r-2 border-[#4a0f0f] z-10"></div>

            {/* Main Template Content */}
            <div className="relative z-20 flex-1 flex flex-col items-center justify-center p-16 text-center">
              
              <div className="mb-6 flex flex-col items-center gap-2">
                <div className="w-10 h-10 rounded bg-[#4a0f0f] flex items-center justify-center text-amber-500 border border-amber-500/20">
                  <span className="font-serif font-bold text-sm">CI</span>
                </div>
                <div className="tracking-[0.25em] text-[10px] uppercase text-[#4a0f0f] font-bold">
                  CI Institute of Nursing
                </div>
              </div>

              <h1 className="font-serif text-4xl md:text-5xl text-[#2a0808] mb-2 tracking-wide font-medium">
                Certificate of Completion
              </h1>
              <div className="w-24 h-0.5 bg-[#4a0f0f]/20 mb-6"></div>

              <p className="text-xs uppercase tracking-widest text-stone-500 mb-3 font-semibold">
                This is to certify that
              </p>

              <h2 className="font-serif text-4xl text-[#1a0505] mb-5 tracking-wide">
                {m0FirstName} {m0LastName}
              </h2>
              
              <div className="text-xs font-semibold text-stone-600 mb-6 font-mono">
                CNA License Key: <span className="bg-stone-200/50 px-2 py-0.5 rounded border border-stone-300">{m0License}</span>
              </div>

              <p className="text-xs text-stone-700 max-w-2xl leading-relaxed mb-8">
                has completed the 12-hour online continuing education theory pathway, demonstrating comprehensive theoretical knowledge in Infection Control, Resident Rights, and Safety standards.
              </p>

              {/* Disclaimer block */}
              <div className="bg-stone-100/80 border border-stone-200 rounded p-3 text-[9px] text-stone-500 max-w-2xl leading-relaxed text-justify mb-8">
                <strong>Disclaimer:</strong> This preview does not constitute official certification of California CNA renewal. Learners remain responsible for satisfying overall CDPH renewal minimums, in-person clinical components, and license timelines.
              </div>

              {/* Bottom seals and signatures */}
              <div className="w-full px-6 grid grid-cols-3 items-end pt-2 text-[10px] font-mono text-stone-500">
                <div className="text-left space-y-1.5 border-l border-stone-300 pl-3">
                  <div><strong className="text-stone-700">Date Logged:</strong> {new Date().toLocaleDateString()}</div>
                  <div><strong className="text-stone-700">Active CE:</strong> 12.0 Hours</div>
                  <div><strong className="text-stone-700">Audit Status:</strong> MOCK PREVIEW</div>
                  <div><strong className="text-stone-700">NAC Key:</strong> [PENDING METADATA]</div>
                </div>

                <div className="flex flex-col items-center justify-center">
                  <div className="relative flex items-center justify-center w-24 h-24">
                    <div className="absolute inset-0 bg-gradient-to-br from-amber-500 to-amber-700 rotate-12 rounded opacity-25"></div>
                    <div className="absolute inset-0 bg-gradient-to-br from-amber-500 to-amber-700 rotate-45 rounded opacity-25"></div>
                    <div className="absolute inset-2 border border-dashed border-amber-600 rounded-full"></div>
                    <div className="absolute inset-3 border border-[#4a0f0f] rounded-full bg-white flex flex-col items-center justify-center shadow-sm">
                      <ShieldCheck size={20} className="text-[#4a0f0f] mb-0.5" />
                      <span className="text-[5px] uppercase tracking-[0.1em] text-[#4a0f0f] font-bold text-center leading-none">MOCK<br/>SEAL</span>
                    </div>
                  </div>
                </div>

                <div className="text-right space-y-1">
                  <div className="border-b border-stone-400 pb-1 italic font-serif text-stone-700 text-sm">
                    Sarah Jenkins, RN
                  </div>
                  <span className="block uppercase tracking-widest text-[8px] text-stone-500 font-bold">Program Director</span>
                  <span className="block text-[8px] text-stone-400 leading-none">CI Institute of Nursing</span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>

    </div>
  );
}