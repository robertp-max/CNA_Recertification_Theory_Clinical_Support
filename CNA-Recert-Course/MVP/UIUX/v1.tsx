import React, { useState, useEffect } from 'react';
import { 
  Play, Pause, FileText, CheckCircle2, Circle, 
  ArrowRight, ArrowLeft, Clock, ShieldAlert, Image as ImageIcon,
  AlertTriangle, Info, Check, X, Shield, Stethoscope, 
  BookOpen, Lock, AlertCircle, ChevronRight, CheckSquare, Square,
  Video, FileSignature, HelpCircle, Eye, RefreshCw, Award, Settings
} from 'lucide-react';

export default function App() {
  const [currentView, setCurrentView] = useState('dashboard'); 
  
  // Compliance & Demo States (controlled manually or via Reviewer Tools)
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
    <div className="min-h-screen bg-[#080404] text-stone-100 font-sans selection:bg-amber-500/30 flex flex-col relative overflow-x-hidden">
      
      {/* Global Scrollbar Customization */}
      <style dangerouslySetInnerHTML={{__html: `
        ::-webkit-scrollbar { width: 6px; height: 6px; background: transparent; }
        ::-webkit-scrollbar-track { background: #080404; }
        ::-webkit-scrollbar-thumb { background-color: #331212; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background-color: #5c1111; }
        * { scrollbar-width: thin; scrollbar-color: #331212 #080404; }
      `}} />
      
      {/* Premium Burgundy Base Gradients */}
      <div className="fixed inset-0 pointer-events-none bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#4a0d0d]/30 via-[#080404] to-[#080404] z-0"></div>

      {/* Admin/Reviewer Tools Drawer (Safe, clean dev utility simulating production admin mode) */}
      <div className="relative z-50">
        <div className="bg-[#180a0a] border-b border-amber-500/20 text-xs py-1 px-4 flex items-center justify-between text-stone-400">
          <div className="flex items-center gap-2">
            <span className="w-1.5 h-1.5 rounded-full bg-green-500"></span>
            <span className="font-mono tracking-wide">CDPH CE Audit-Simulator Active: V2.0</span>
          </div>
          <button 
            onClick={() => setShowReviewerTools(!showReviewerTools)} 
            className="flex items-center gap-1.5 text-amber-500 hover:text-amber-400 font-semibold uppercase tracking-wider px-2 py-0.5 rounded bg-amber-950/40 border border-amber-500/20"
          >
            <Settings size={12} />
            {showReviewerTools ? 'Close Reviewer Panel' : 'Open Reviewer Panel'}
          </button>
        </div>

        {showReviewerTools && (
          <div className="bg-[#120606] border-b border-[#5c1111] p-4 text-sm animate-in slide-in-from-top-4 duration-300">
            <div className="max-w-6xl mx-auto">
              <div className="flex items-center justify-between mb-3 border-b border-stone-800 pb-2">
                <span className="font-semibold text-stone-200 uppercase tracking-widest text-[11px] flex items-center gap-2">
                  <Shield size={14} className="text-amber-500" /> Prototype State Override Panel
                </span>
                <span className="text-xs text-stone-500 italic">Simulates user progress & compliance actions</span>
              </div>
              <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
                <div>
                  <label className="block text-stone-500 text-[10px] uppercase font-bold mb-1">Module 0 Status</label>
                  <div className="flex gap-2">
                    <button 
                      onClick={() => { setModule0Completed(true); setModule0Agreed([true, true, true]); }} 
                      className={`px-3 py-1.5 rounded text-xs font-semibold w-full border ${module0Completed ? 'bg-amber-950/20 text-amber-400 border-amber-500/30' : 'bg-stone-900 text-stone-400 border-stone-800'}`}
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
                  <label className="block text-stone-500 text-[10px] uppercase font-bold mb-1">Lesson Completed</label>
                  <button 
                    onClick={() => setLessonCompleted(!lessonCompleted)} 
                    className={`px-3 py-1.5 rounded text-xs font-semibold w-full border ${lessonCompleted ? 'bg-amber-950/20 text-amber-400 border-amber-500/30' : 'bg-stone-900 text-stone-400 border-stone-800'}`}
                  >
                    {lessonCompleted ? 'Completed' : 'Not Started'}
                  </button>
                </div>

                <div>
                  <label className="block text-stone-500 text-[10px] uppercase font-bold mb-1">Module 1 Exam</label>
                  <div className="flex gap-1">
                    <button 
                      onClick={() => { setM1AssessmentPassed(true); setM1AssessmentScore(90); }} 
                      className={`px-2 py-1.5 rounded text-xs font-semibold flex-1 border ${m1AssessmentPassed ? 'bg-emerald-950/20 text-emerald-400 border-emerald-500/30' : 'bg-stone-900 text-stone-400 border-stone-800'}`}
                    >
                      Pass (90%)
                    </button>
                    <button 
                      onClick={() => { setM1AssessmentPassed(false); setM1AssessmentScore(50); }} 
                      className="px-2 py-1.5 rounded text-xs bg-stone-900 border border-stone-800 text-red-500 font-semibold hover:bg-stone-850"
                    >
                      Fail
                    </button>
                  </div>
                </div>

                <div>
                  <label className="block text-stone-500 text-[10px] uppercase font-bold mb-1">Final Exam</label>
                  <div className="flex gap-1">
                    <button 
                      onClick={() => { setFinalAssessmentPassed(true); setFinalAssessmentScore(85); }} 
                      className={`px-2 py-1.5 rounded text-xs font-semibold flex-1 border ${finalAssessmentPassed ? 'bg-emerald-950/20 text-emerald-400 border-emerald-500/30' : 'bg-stone-900 text-stone-400 border-stone-800'}`}
                    >
                      Pass (85%)
                    </button>
                    <button 
                      onClick={() => { setFinalAssessmentPassed(false); setFinalAssessmentScore(40); }} 
                      className="px-2 py-1.5 rounded text-xs bg-stone-900 border border-stone-800 text-red-500 font-semibold hover:bg-stone-850"
                    >
                      Fail
                    </button>
                  </div>
                </div>

                <div className="flex flex-col justify-end">
                  <div className="flex gap-2">
                    <button 
                      onClick={forceCompleteAll} 
                      className="flex-1 bg-amber-500 hover:bg-amber-400 text-black text-xs font-bold py-1.5 px-2 rounded transition-colors uppercase tracking-wider"
                    >
                      Unlock All
                    </button>
                    <button 
                      onClick={resetAllProgress} 
                      className="flex-1 bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-400 text-xs font-bold py-1.5 px-2 rounded transition-colors uppercase tracking-wider"
                    >
                      Reset All
                    </button>
                  </div>
                </div>
              </div>
              <div className="mt-3 text-[11px] text-stone-500 flex gap-4">
                <span><strong>Simulated Active Study Time:</strong> {formatHoursAndMins(activeTimeSecs)}</span>
                <span>•</span>
                <span><strong>Affidavit Signed:</strong> {affidavitSigned ? "Yes" : "No"}</span>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Global Navigation */}
      <header className="px-6 py-4 border-b border-stone-800/60 bg-[#0c0606]/80 backdrop-blur-md relative z-40 flex items-center justify-between shrink-0">
        <div className="flex items-center gap-3 cursor-pointer" onClick={() => setCurrentView('dashboard')}>
          <div className="w-8 h-8 rounded bg-[#1f0909] flex items-center justify-center border border-[#5c1111]">
            <span className="text-stone-100 font-bold text-xs tracking-tight">CI</span>
          </div>
          <div>
            <span className="font-semibold text-stone-200 tracking-wider text-sm block">CI INSTITUTE OF NURSING</span>
            <span className="text-[9px] text-stone-500 block -mt-1 font-mono uppercase tracking-widest">CDPH CNA CE PROVIDER</span>
          </div>
        </div>
        
        <div className="flex items-center gap-1 sm:gap-4 text-xs sm:text-sm font-medium text-stone-400">
          {[
            { id: 'dashboard', label: 'Dashboard' },
            { id: 'modules', label: 'CE Modules' },
            { id: 'certificate', label: 'Certificate Gate' },
            { id: 'clinical', label: 'Clinical Hub' },
          ].map(item => {
            const isActive = currentView === item.id || 
              (item.id === 'modules' && ['module0', 'module1', 'lesson', 'm1Assessment', 'finalAssessment', 'finalResult'].includes(currentView));
            return (
              <button 
                key={item.id}
                onClick={() => setCurrentView(item.id)}
                className={`transition-all px-3 py-1.5 rounded-lg border uppercase tracking-wider text-[11px] font-semibold ${
                  isActive 
                    ? 'text-amber-500 bg-[#1f0d0d] border-[#5c1111]' 
                    : 'border-transparent text-stone-400 hover:text-stone-200 hover:bg-stone-900/40'
                }`}
              >
                {item.label}
              </button>
            );
          })}
          
          <div className="w-8 h-8 rounded bg-[#1b1212] text-amber-500 flex items-center justify-center border border-stone-800/80 ml-1 sm:ml-4">
            <span className="text-xs font-bold font-mono">JB</span>
          </div>
        </div>
      </header>

      {/* Main Content Container */}
      <main className="flex-1 w-full max-w-6xl mx-auto p-4 md:p-8 relative z-10 flex flex-col justify-start">
        <div className="transition-all duration-300 flex-1 flex flex-col justify-start">
          
          {/* VIEW: DASHBOARD */}
          {currentView === 'dashboard' && (
            <div className="space-y-6 animate-in fade-in slide-in-from-bottom-2 duration-500">
              
              {/* Main Banner */}
              <div className="bg-[#120909] border border-stone-800/60 rounded-xl p-6 md:p-10 shadow-xl relative overflow-hidden flex flex-col lg:flex-row gap-8 lg:items-center">
                <div className="absolute top-0 right-0 -mr-32 -mt-32 w-96 h-96 rounded-full bg-amber-500/[0.02] blur-3xl pointer-events-none"></div>

                <div className="flex-1 relative z-10">
                  <div className="inline-flex items-center gap-2 px-3 py-1 rounded bg-[#310c0c] border border-[#5c1111]/60 text-[11px] font-bold tracking-widest text-amber-500 uppercase mb-4">
                    <Shield size={12} /> CNA Theory Recertification Pathway
                  </div>
                  <h1 className="text-3xl md:text-5xl font-normal text-stone-100 tracking-tight mb-4 leading-tight">
                    CNA CE Theory Portal
                  </h1>
                  <p className="text-stone-400 text-sm md:text-base mb-6 max-w-xl leading-relaxed">
                    A secure 12-hour structured online theory program designed to meet professional continuing education guidelines. Features standard verification modules, assessments, and audit trails.
                  </p>
                  
                  {/* High priority regulatory guardrail clearly visible */}
                  <div className="bg-amber-950/20 border border-amber-500/20 rounded-lg p-3.5 max-w-xl mb-6">
                    <div className="flex items-start gap-2">
                      <AlertTriangle size={14} className="text-amber-500 shrink-0 mt-0.5" />
                      <p className="text-[11px] text-stone-400 leading-relaxed font-mono">
                        <strong>Regulatory Compliance Notice:</strong> This course provides 12 hours of online theory CE only. It does not constitute full CDPH CNA renewal on its own. Optional Clinical Support Hub does not count toward clinical hours.
                      </p>
                    </div>
                  </div>

                  <div className="flex flex-col sm:flex-row items-center gap-4">
                    {!module0Completed ? (
                      <button 
                        onClick={() => setCurrentView('module0')}
                        className="w-full sm:w-auto bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-semibold px-6 py-3 rounded-lg flex items-center justify-center gap-2 transition-colors uppercase tracking-wider text-xs"
                      >
                        Start Required Orientation <ArrowRight size={14} />
                      </button>
                    ) : (
                      <button 
                        onClick={() => setCurrentView('modules')}
                        className="w-full sm:w-auto bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-semibold px-6 py-3 rounded-lg flex items-center justify-center gap-2 transition-colors uppercase tracking-wider text-xs"
                      >
                        Resume Pathway <ArrowRight size={14} />
                      </button>
                    )}
                    <button 
                      onClick={() => setCurrentView('modules')}
                      className="w-full sm:w-auto bg-stone-900 hover:bg-stone-850 text-stone-300 border border-stone-800 font-semibold px-6 py-3 rounded-lg transition-colors uppercase tracking-wider text-xs"
                    >
                      View All Modules
                    </button>
                  </div>
                </div>

                {/* Status Column */}
                <div className="w-full lg:w-[320px] shrink-0 bg-[#0e0707] border border-stone-800/80 rounded-xl p-5 relative z-10">
                  <div className="flex items-center justify-between mb-4 pb-3 border-b border-stone-800/60">
                    <h3 className="font-semibold text-stone-300 text-xs uppercase tracking-wider">Gate Review Status</h3>
                    <div className="flex items-center gap-1.5 text-amber-500 text-xs">
                      <Shield size={14} />
                      <span className="font-mono text-[11px] font-bold">12-HOUR CAP</span>
                    </div>
                  </div>

                  <div className="space-y-3 mb-5">
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-stone-500 font-medium">Orientation (Mod 0):</span>
                      <span className={`flex items-center gap-1 ${module0Completed ? 'text-emerald-500' : 'text-stone-600'}`}>
                        {module0Completed ? <CheckCircle2 size={12} /> : <Circle size={12} />}
                        {module0Completed ? 'Approved' : 'Pending'}
                      </span>
                    </div>
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-stone-500 font-medium">Active Timer Check:</span>
                      <span className={`font-mono text-[11px] font-semibold ${activeTimeSecs >= 43200 ? 'text-emerald-500' : 'text-amber-500'}`}>
                        {formatHoursAndMins(activeTimeSecs)}
                      </span>
                    </div>
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-stone-500 font-medium">Theory Lessons:</span>
                      <span className={`flex items-center gap-1 ${lessonCompleted ? 'text-emerald-500' : 'text-stone-600'}`}>
                        {lessonCompleted ? <CheckCircle2 size={12} /> : <Circle size={12} />}
                        {lessonCompleted ? 'Complete' : 'Pending'}
                      </span>
                    </div>
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-stone-500 font-medium">Final Assessment:</span>
                      <span className={`flex items-center gap-1 ${finalAssessmentPassed ? 'text-emerald-500' : 'text-stone-600'}`}>
                        {finalAssessmentPassed ? <CheckCircle2 size={12} /> : <Circle size={12} />}
                        {finalAssessmentPassed ? `Passed` : 'Unattempted'}
                      </span>
                    </div>
                  </div>

                  <div className="bg-stone-950 p-3 rounded border border-stone-900 mb-4">
                    <div className="flex items-center justify-between text-[11px] mb-2">
                      <span className="text-stone-500 uppercase font-bold">Overall Progress</span>
                      <span className="text-amber-500 font-bold font-mono">
                        {finalAssessmentPassed && affidavitSigned ? '100%' : module0Completed ? '15%' : '0%'}
                      </span>
                    </div>
                    <div className="w-full h-1.5 bg-stone-900 rounded-full overflow-hidden">
                      <div 
                        className="h-full bg-amber-500 transition-all duration-500" 
                        style={{ width: finalAssessmentPassed && affidavitSigned ? '100%' : module0Completed ? '15%' : '2%' }}
                      ></div>
                    </div>
                  </div>

                  <button 
                    onClick={() => setCurrentView('certificate')}
                    className="w-full py-2 rounded bg-stone-900 hover:bg-stone-850 text-stone-200 font-semibold text-xs border border-stone-800 transition-colors uppercase tracking-wider"
                  >
                    Review Auditing Gates
                  </button>
                </div>
              </div>

              {/* Grid Features */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="p-6 rounded-xl bg-[#120909] border border-stone-800/80 flex flex-col justify-between">
                  <div>
                    <div className="text-amber-500 mb-3"><BookOpen size={20} /></div>
                    <h4 className="text-sm font-semibold text-stone-200 uppercase tracking-wider mb-2">12-Hour Required Theory</h4>
                    <p className="text-xs text-stone-400 leading-relaxed">
                      Structured sequence covering Infection Control, Resident Rights, Dementia Care, Mobility, and Nutrition.
                    </p>
                  </div>
                  <div className="mt-4 pt-3 border-t border-stone-900">
                    <span className="text-[10px] text-stone-500 font-mono">STATUS: UNLOCKED SEQUENTIALLY</span>
                  </div>
                </div>

                <div className="p-6 rounded-xl bg-[#120909] border border-stone-800/80 flex flex-col justify-between">
                  <div>
                    <div className="text-amber-500 mb-3"><Stethoscope size={20} /></div>
                    <h4 className="text-sm font-semibold text-stone-200 uppercase tracking-wider mb-2">Optional Clinical Support</h4>
                    <p className="text-xs text-stone-400 leading-relaxed">
                      Skills practice and simulated scenarios to gain professional confidence. Entirely optional, non-credit, and separate from certificate progress.
                    </p>
                  </div>
                  <div className="mt-4 pt-3 border-t border-stone-900 flex justify-between items-center">
                    <span className="text-[10px] text-stone-500 font-mono">STATUS: OPTIONAL CE</span>
                    <button 
                      onClick={() => setCurrentView('clinical')}
                      className="text-[10px] text-amber-500 hover:text-amber-400 font-bold uppercase tracking-wider"
                    >
                      Enter Hub &rarr;
                    </button>
                  </div>
                </div>

                <div className="p-6 rounded-xl bg-[#120909] border border-stone-800/80 flex flex-col justify-between">
                  <div>
                    <div className="text-amber-500 mb-3"><ShieldAlert size={20} /></div>
                    <h4 className="text-sm font-semibold text-stone-200 uppercase tracking-wider mb-2">Audit Safety Guarantee</h4>
                    <p className="text-xs text-stone-400 leading-relaxed">
                      Strict HIPAA / PHI guardrails. Simulated patient personas are used exclusively. No actual resident healthcare identifiers are saved.
                    </p>
                  </div>
                  <div className="mt-4 pt-3 border-t border-stone-900">
                    <span className="text-[10px] text-red-500/80 font-mono font-semibold flex items-center gap-1">
                      <ShieldAlert size={12} /> HIPAA COMPLIANT PRESETS
                    </span>
                  </div>
                </div>
              </div>

            </div>
          )}

          {/* VIEW: MODULES LIST */}
          {currentView === 'modules' && (
            <div className="flex flex-col lg:flex-row gap-8 animate-in fade-in duration-300">
              
              {/* Left Sidebar */}
              <div className="w-full lg:w-80 shrink-0 space-y-6">
                <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 sticky top-8">
                  <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-3 flex items-center gap-1.5">
                    <Shield size={12} /> Theory CE Requirements
                  </div>
                  <h2 className="text-2xl font-normal text-stone-100 mb-3 leading-tight">Curriculum</h2>
                  <p className="text-xs text-stone-400 mb-6 leading-relaxed">
                    All required theory modules must be initiated and completed in order. Active study time is logged for CDPH compliance.
                  </p>

                  <div className="space-y-4 mb-6 border-t border-stone-800/80 pt-4">
                    <div>
                      <div className="flex justify-between text-[11px] mb-1 text-stone-400">
                        <span>Legal Name Verified</span>
                        <span className="font-mono text-stone-200">{m0FirstName} {m0LastName}</span>
                      </div>
                      <div className="flex justify-between text-[11px] text-stone-400">
                        <span>License Key</span>
                        <span className="font-mono text-stone-200">{m0License}</span>
                      </div>
                    </div>
                  </div>

                  <div className="space-y-2 mb-6">
                    <div className="flex justify-between text-[11px] font-semibold">
                      <span className="text-stone-300">Course Verification</span>
                      <span className="text-amber-500 font-mono">
                        {finalAssessmentPassed ? "100%" : module0Completed ? "15%" : "0%"}
                      </span>
                    </div>
                    <div className="w-full h-1 bg-stone-900 rounded-full overflow-hidden">
                      <div 
                        className="h-full bg-amber-500 transition-all" 
                        style={{ width: finalAssessmentPassed ? '100%' : module0Completed ? '15%' : '0%' }}
                      ></div>
                    </div>
                  </div>

                  <button 
                    onClick={() => setCurrentView('certificate')}
                    className="w-full py-2.5 rounded bg-stone-900 hover:bg-stone-850 border border-stone-800 text-stone-200 font-semibold text-xs uppercase tracking-wider transition-colors"
                  >
                    Review Gate Checklist
                  </button>
                </div>
              </div>

              {/* Right Modules Grid */}
              <div className="flex-1 space-y-6">
                <div>
                  <h2 className="text-2xl font-normal text-stone-100 mb-1">Theory Recertification Modules</h2>
                  <p className="text-stone-400 text-xs">Verify your identification during Module 0 to unlock successive study units.</p>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  
                  {/* Module 0 Card */}
                  <div className="p-5 rounded-xl border bg-[#120909] border-stone-800/80 hover:border-stone-700/80 transition-all flex flex-col justify-between">
                    <div>
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-[10px] font-bold text-amber-500 uppercase tracking-wider font-mono">Module 0</span>
                        <span className="text-[10px] font-mono text-stone-500">0.5 HR</span>
                      </div>
                      <h3 className="text-base font-semibold text-stone-200 mb-2">Orientation & Compliance Verification</h3>
                      <p className="text-xs text-stone-400 leading-relaxed mb-6">
                        Confirm CNA credentials, review regulatory guidelines, acknowledge HIPAA restrictions, and establish core active-time validation parameters.
                      </p>
                    </div>
                    <div className="flex items-center justify-between pt-3 border-t border-stone-900">
                      <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded text-[10px] font-semibold ${
                        module0Completed ? 'bg-emerald-950/40 text-emerald-400 border border-emerald-500/20' : 'bg-amber-950/40 text-amber-400 border border-amber-500/20'
                      }`}>
                        {module0Completed ? <CheckCircle2 size={10} /> : <AlertCircle size={10} />}
                        {module0Completed ? 'Completed & Confirmed' : 'Action Required'}
                      </span>
                      <button 
                        onClick={() => setCurrentView('module0')}
                        className={`px-3 py-1 rounded text-xs font-semibold ${
                          module0Completed ? 'bg-stone-900 text-stone-300 hover:bg-stone-850' : 'bg-[#5c1111] text-stone-100 hover:bg-[#781616]'
                        } transition-colors`}
                      >
                        {module0Completed ? 'Review' : 'Begin'}
                      </button>
                    </div>
                  </div>

                  {/* Module 1 Card */}
                  <div className={`p-5 rounded-xl border transition-all flex flex-col justify-between ${
                    module0Completed ? 'bg-[#120909] border-stone-800/80 hover:border-stone-700/80' : 'bg-[#0a0505]/60 border-stone-950 opacity-60'
                  }`}>
                    <div>
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-[10px] font-bold text-stone-400 uppercase tracking-wider font-mono">Module 1</span>
                        <span className="text-[10px] font-mono text-stone-500">1.5 HR</span>
                      </div>
                      <h3 className="text-base font-semibold text-stone-200 mb-2">Infection Control & PPE</h3>
                      <p className="text-xs text-stone-400 leading-relaxed mb-6">
                        Examine infection chains, implement WHO hand hygiene protocols, and perform standard safety selections for CNA barrier protection.
                      </p>
                    </div>
                    <div className="flex items-center justify-between pt-3 border-t border-stone-900">
                      <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded text-[10px] font-semibold ${
                        !module0Completed ? 'bg-stone-950 text-stone-600 border border-stone-900' :
                        m1AssessmentPassed ? 'bg-emerald-950/40 text-emerald-400 border border-emerald-500/20' :
                        lessonCompleted ? 'bg-amber-950/40 text-amber-400 border border-amber-500/20' : 'bg-stone-900 text-stone-400'
                      }`}>
                        {!module0Completed ? <Lock size={10} /> : m1AssessmentPassed ? <CheckCircle2 size={10} /> : <AlertCircle size={10} />}
                        {!module0Completed ? 'Locked (Complete Mod 0)' : m1AssessmentPassed ? 'Passed' : lessonCompleted ? 'Assessment Ready' : 'In Progress'}
                      </span>
                      {module0Completed && (
                        <button 
                          onClick={() => setCurrentView('module1')}
                          className="px-3 py-1 rounded text-xs bg-[#5c1111] text-stone-100 hover:bg-[#781616] transition-colors"
                        >
                          Open Module
                        </button>
                      )}
                    </div>
                  </div>

                  {/* Module 2 Card (Locked Demo) */}
                  <div className="p-5 rounded-xl border bg-[#0a0505]/60 border-stone-950 opacity-50 flex flex-col justify-between">
                    <div>
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-[10px] font-bold text-stone-500 uppercase tracking-wider font-mono">Module 2</span>
                        <span className="text-[10px] font-mono text-stone-600">2.0 HR</span>
                      </div>
                      <h3 className="text-base font-semibold text-stone-500 mb-2">Resident Rights & Abuse Prevention</h3>
                      <p className="text-xs text-stone-600 leading-relaxed mb-6">
                        Required regulatory overview regarding legal rights, active advocacy, mandates, and CDPH reporting timelines.
                      </p>
                    </div>
                    <div className="flex items-center justify-between pt-3 border-t border-stone-950">
                      <span className="inline-flex items-center gap-1 text-[10px] text-stone-600 font-mono">
                        <Lock size={10} /> Locked (Sequential Path)
                      </span>
                    </div>
                  </div>

                  {/* Module 3 Card (Locked Demo) */}
                  <div className="p-5 rounded-xl border bg-[#0a0505]/60 border-stone-950 opacity-50 flex flex-col justify-between">
                    <div>
                      <div className="flex items-center justify-between mb-3">
                        <span className="text-[10px] font-bold text-stone-500 uppercase tracking-wider font-mono">Module 3</span>
                        <span className="text-[10px] font-mono text-stone-600">2.0 HR</span>
                      </div>
                      <h3 className="text-base font-semibold text-stone-500 mb-2">Dementia Care & Communication</h3>
                      <p className="text-xs text-stone-600 leading-relaxed mb-6">
                        Cognitive decline, verbal and non-verbal adjustment methods, and behavioral de-escalation protocols.
                      </p>
                    </div>
                    <div className="flex items-center justify-between pt-3 border-t border-stone-950">
                      <span className="inline-flex items-center gap-1 text-[10px] text-stone-600 font-mono">
                        <Lock size={10} /> Locked (Sequential Path)
                      </span>
                    </div>
                  </div>

                </div>

                {/* Course Final Assessment Panel (Unlocked once Mod 1-5 are theoretical or simulated passed) */}
                <div className={`p-6 rounded-xl border transition-all ${
                  m1AssessmentPassed ? 'bg-[#1c0808] border-[#5c1111]/80' : 'bg-stone-950/20 border-stone-900/60 opacity-60'
                }`}>
                  <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
                    <div>
                      <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-[10px] font-bold tracking-widest text-amber-500 uppercase bg-amber-950/40 border border-amber-500/20 mb-3 font-mono">
                        Course-Wide Final Examination
                      </div>
                      <h3 className="text-lg font-semibold text-stone-200 mb-2">Theory Final Assessment Gate</h3>
                      <p className="text-xs text-stone-400 max-w-xl leading-relaxed">
                        CDPH compliant multi-topic assessment. Minimum 80% score required. No correct answer keys are displayed following submission to preserve compliance integrity.
                      </p>
                    </div>
                    
                    <div className="shrink-0">
                      {finalAssessmentPassed ? (
                        <div className="flex items-center gap-2 bg-emerald-950/40 border border-emerald-500/30 text-emerald-400 px-4 py-2 rounded-lg font-semibold text-xs">
                          <CheckCircle2 size={14} /> Passed ({finalAssessmentScore}%)
                        </div>
                      ) : m1AssessmentPassed ? (
                        <button 
                          onClick={() => setCurrentView('finalAssessmentSplash')}
                          className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-semibold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors"
                        >
                          Enter Final Assessment
                        </button>
                      ) : (
                        <div className="flex items-center gap-2 bg-stone-900 border border-stone-800 text-stone-500 px-4 py-2 rounded text-xs font-semibold font-mono">
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
            <div className="max-w-3xl mx-auto space-y-6 animate-in fade-in duration-300">
              <button 
                onClick={() => setCurrentView('modules')} 
                className="text-stone-400 hover:text-stone-100 flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider"
              >
                <ArrowLeft size={14} /> Back to Modules
              </button>

              <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-10 shadow-xl space-y-6">
                <div>
                  <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-1 font-mono">Required Step • Module 0</div>
                  <h1 className="text-3xl font-normal text-stone-100 tracking-tight">Identity & Compliance Orientation</h1>
                  <p className="text-xs text-stone-400 leading-relaxed mt-1">
                    Please audit and sign the mandatory compliance declarations. Accurate PHI warnings must be observed throughout the active session.
                  </p>
                </div>

                <div className="space-y-4 pt-4 border-t border-stone-800/60">
                  <h3 className="text-xs uppercase tracking-wider font-bold text-stone-300">1. Verification of Legal CNA Identity</h3>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                      <label className="block text-[10px] uppercase font-bold text-stone-500 mb-1 font-mono">First Name (Legal)</label>
                      <input 
                        type="text" 
                        value={m0FirstName} 
                        onChange={(e) => setM0FirstName(e.target.value)}
                        className="w-full bg-[#080404] border border-stone-800 text-stone-100 text-xs px-3 py-2 rounded focus:outline-none focus:border-amber-500"
                      />
                    </div>
                    <div>
                      <label className="block text-[10px] uppercase font-bold text-stone-500 mb-1 font-mono">Last Name (Legal)</label>
                      <input 
                        type="text" 
                        value={m0LastName} 
                        onChange={(e) => setM0LastName(e.target.value)}
                        className="w-full bg-[#080404] border border-stone-800 text-stone-100 text-xs px-3 py-2 rounded focus:outline-none focus:border-amber-500"
                      />
                    </div>
                    <div>
                      <label className="block text-[10px] uppercase font-bold text-stone-500 mb-1 font-mono">CNA Certificate Number</label>
                      <input 
                        type="text" 
                        value={m0License} 
                        onChange={(e) => setM0License(e.target.value)}
                        className="w-full bg-[#080404] border border-stone-800 text-stone-100 text-xs px-3 py-2 rounded font-mono focus:outline-none focus:border-amber-500"
                      />
                    </div>
                  </div>
                </div>

                <div className="space-y-3 pt-4 border-t border-stone-800/60">
                  <h3 className="text-xs uppercase tracking-wider font-bold text-stone-300">2. Mandatory Declarations & Acknowledgements</h3>
                  
                  {[
                    "I certify that my legal CNA identity matches the credential entered above, and that I alone will complete this CE training program.",
                    "HIPAA STRICT: I acknowledge that I will NEVER enter real Protected Health Information (PHI), client records, or actual identifier keys anywhere in this portal.",
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
                          ? 'bg-[#1c0d0d] border-[#5c1111]/80 text-stone-100' 
                          : 'bg-[#080404] border-stone-800 hover:border-stone-700 text-stone-400'
                      }`}
                    >
                      <div className="mt-0.5 text-amber-500 shrink-0">
                        {module0Agreed[i] ? <CheckSquare size={16} /> : <Square size={16} />}
                      </div>
                      <p className="text-xs leading-relaxed">{text}</p>
                    </div>
                  ))}
                </div>

                <div className="pt-6 border-t border-stone-800/60 flex items-center justify-between">
                  <div className="text-xs text-stone-500">
                    {!module0Agreed.every(Boolean) && "Select all 3 agreements to proceed."}
                  </div>
                  <button 
                    onClick={() => {
                      setModule0Completed(true);
                      setCurrentView('modules');
                    }}
                    disabled={!module0Agreed.every(Boolean)}
                    className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-all disabled:opacity-40 disabled:cursor-not-allowed"
                  >
                    Confirm & Unlock Module 1
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* VIEW: MODULE 1 OVERVIEW */}
          {currentView === 'module1' && (
            <div className="max-w-3xl mx-auto space-y-6 animate-in fade-in duration-300">
              <button 
                onClick={() => setCurrentView('modules')} 
                className="text-stone-400 hover:text-stone-100 flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider"
              >
                <ArrowLeft size={14} /> Back to Modules
              </button>

              <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl">
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-stone-800/60">
                  <div>
                    <span className="text-[10px] uppercase font-bold text-amber-500 font-mono">Module 1 • 1.5 Theory Hours</span>
                    <h1 className="text-2xl font-normal text-stone-100 tracking-tight">Infection Control & PPE</h1>
                  </div>
                  <div className="shrink-0 flex items-center gap-2">
                    <span className={`inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-bold ${
                      m1AssessmentPassed ? 'bg-emerald-950 text-emerald-400 border border-emerald-500/20' : 'bg-amber-950 text-amber-400 border border-amber-500/20'
                    }`}>
                      {m1AssessmentPassed ? 'Complete' : 'Not Attempted'}
                    </span>
                  </div>
                </div>

                <div className="py-6 space-y-4">
                  <h3 className="text-xs uppercase tracking-wider font-bold text-stone-300">Lesson Objectives</h3>
                  <div className="grid grid-cols-1 gap-2.5">
                    {[
                      "Recall the six distinct structural links in the chain of infection.",
                      "Formulate proper WHO handwashing strategies and determine active timings.",
                      "Acknowledge critical indications for Contact, Droplet, and Airborne barriers."
                    ].map((obj, idx) => (
                      <div key={idx} className="flex gap-2.5 items-start text-xs text-stone-400 leading-relaxed">
                        <span className="text-amber-500 font-bold font-mono">0{idx+1}.</span>
                        <span>{obj}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Lesson Track List */}
                <div className="space-y-3 pt-4 border-t border-stone-800/60">
                  <h3 className="text-xs uppercase tracking-wider font-bold text-stone-300">Course Component Lessons</h3>
                  
                  <div 
                    onClick={() => setCurrentView('lesson')}
                    className="p-4 rounded border bg-[#080404] border-stone-800 hover:border-[#5c1111]/80 hover:bg-[#120909] transition-all cursor-pointer flex items-center justify-between"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded bg-[#1c0d0d] flex items-center justify-center border border-[#5c1111]/40 text-amber-500 font-bold font-mono text-xs">
                        1
                      </div>
                      <div>
                        <h4 className="text-xs font-semibold text-stone-200">The Chain of Infection & Standard Precautions</h4>
                        <span className="text-[10px] text-stone-500 font-mono uppercase tracking-wide">Structured Theory &bull; 4-Card Player</span>
                      </div>
                    </div>
                    <div className="flex items-center gap-2 text-xs text-stone-400 font-semibold uppercase tracking-wider">
                      {lessonCompleted ? (
                        <span className="text-emerald-500 flex items-center gap-1 text-[10px] font-bold">
                          <CheckCircle2 size={12} /> Finished
                        </span>
                      ) : (
                        <span className="text-amber-500 flex items-center gap-1 text-[10px] font-bold">
                          <Play size={12} className="fill-current" /> Play
                        </span>
                      )}
                    </div>
                  </div>

                  <div className="p-4 rounded border bg-[#080404]/40 border-stone-900 opacity-60 flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded bg-[#111] flex items-center justify-center border border-stone-850 text-stone-600 font-bold font-mono text-xs">
                        2
                      </div>
                      <div>
                        <h4 className="text-xs font-semibold text-stone-400">Clinical Isolation & PPE Selection Sequence</h4>
                        <span className="text-[10px] text-stone-600 font-mono uppercase tracking-wide">Visual Demonstration</span>
                      </div>
                    </div>
                    <span className="text-[10px] text-stone-600 font-mono">SEQUENTIAL LOCK</span>
                  </div>

                </div>

                <div className="pt-8 border-t border-stone-800/60 flex flex-col sm:flex-row items-center gap-4 justify-between">
                  <div className="text-xs text-stone-400">
                    {lessonCompleted ? "Theory lessons complete. Complete the assessment." : "Complete Lesson 1 to unlock the Module Assessment."}
                  </div>
                  <div className="flex gap-3 w-full sm:w-auto">
                    {lessonCompleted && (
                      <button 
                        onClick={() => setCurrentView('m1Assessment')}
                        className="w-full sm:w-auto bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors"
                      >
                        Start Module 1 Assessment
                      </button>
                    )}
                    <button 
                      onClick={() => setCurrentView('lesson')}
                      className="w-full sm:w-auto bg-stone-900 hover:bg-stone-850 border border-stone-800 text-stone-300 font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors"
                    >
                      {lessonCompleted ? 'Review Theory' : 'Start Theory'}
                    </button>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* VIEW: HIGH-FIDELITY 4-CARD LESSON PLAYER */}
          {currentView === 'lesson' && (
            <LessonPlayerView 
              setView={setCurrentView} 
              setLessonCompleted={setLessonCompleted} 
              activeTime={activeTimeSecs}
              formatHoursAndMins={formatHoursAndMins}
            />
          )}

          {/* VIEW: MODULE 1 ASSESSMENT SPLASH */}
          {currentView === 'm1Assessment' && (
            <div className="max-w-2xl mx-auto space-y-6 animate-in fade-in duration-300">
              <button 
                onClick={() => setCurrentView('module1')} 
                className="text-stone-400 hover:text-stone-100 flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider"
              >
                <ArrowLeft size={14} /> Back to Module 1
              </button>

              <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl text-center space-y-6">
                <div className="w-12 h-12 rounded bg-[#1c0c0c] border border-[#5c1111] flex items-center justify-center mx-auto text-amber-500">
                  <ShieldAlert size={24} />
                </div>
                
                <div>
                  <span className="text-[10px] uppercase font-bold text-stone-500 font-mono tracking-widest">Formal Assessment Portal</span>
                  <h1 className="text-2xl font-normal text-stone-100 tracking-tight mt-1">Module 1 Knowledge Exam</h1>
                  <p className="text-xs text-stone-400 max-w-md mx-auto leading-relaxed mt-2">
                    Verify compliance of key Infection Control concepts. You must score $80\%$ or higher to advance. Correct answer codes are hidden after completion.
                  </p>
                </div>

                <div className="bg-stone-950 p-4 rounded border border-stone-900 text-left max-w-md mx-auto space-y-3 font-mono text-[11px] text-stone-400">
                  <div className="flex justify-between">
                    <span>Structure Questions:</span>
                    <span className="text-stone-200">5 Questions</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Target Score Check:</span>
                    <span className="text-amber-500">80% Minimum (4 Correct)</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Remediation Rules:</span>
                    <span className="text-stone-200">Unlimited Retakes Required</span>
                  </div>
                </div>

                <div className="pt-4 flex flex-col sm:flex-row justify-center gap-3">
                  <button 
                    onClick={() => {
                      // Navigate to question flow
                      setCurrentView('m1AssessmentQuiz');
                    }}
                    className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors"
                  >
                    Begin Assessment Exam
                  </button>
                  <button 
                    onClick={() => setCurrentView('module1')}
                    className="bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-300 font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors"
                  >
                    Study Material Again
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* VIEW: MODULE 1 ASSESSMENT QUIZ FLOW */}
          {currentView === 'm1AssessmentQuiz' && (
            <QuizFlowView 
              setView={setCurrentView}
              isFinalExam={false}
              onPass={(score) => {
                setM1AssessmentPassed(true);
                setM1AssessmentScore(score);
              }}
              onFail={(score) => {
                setM1AssessmentPassed(false);
                setM1AssessmentScore(score);
              }}
            />
          )}

          {/* VIEW: COURSE FINAL EXAM SPLASH */}
          {currentView === 'finalAssessmentSplash' && (
            <div className="max-w-2xl mx-auto space-y-6 animate-in fade-in duration-300">
              <button 
                onClick={() => setCurrentView('modules')} 
                className="text-stone-400 hover:text-stone-100 flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider"
              >
                <ArrowLeft size={14} /> Back to Modules
              </button>

              <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-10 shadow-xl text-center space-y-6">
                <div className="w-14 h-14 rounded bg-[#1c0c0c] border border-[#5c1111] flex items-center justify-center mx-auto text-amber-500">
                  <Award size={28} />
                </div>
                
                <div>
                  <span className="text-[10px] uppercase font-bold text-stone-500 font-mono tracking-widest">CDPH Course-Wide Examination</span>
                  <h1 className="text-3xl font-normal text-stone-100 tracking-tight mt-1">Theory Competency Exam</h1>
                  <p className="text-xs text-stone-400 max-w-md mx-auto leading-relaxed mt-2">
                    A comprehensive validation of all modules in the 12-hour theory portal. Complete the exam under strict auditing guidelines. No correct answers will be reviewed post-submission.
                  </p>
                </div>

                <div className="bg-[#0c0505] p-5 rounded border border-stone-900 text-left max-w-md mx-auto space-y-3 font-mono text-[11px] text-stone-400">
                  <div className="flex justify-between">
                    <span>Audit Time Logged:</span>
                    <span className="text-stone-200">{formatHoursAndMins(activeTimeSecs)}</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Minimum Passing Criteria:</span>
                    <span className="text-amber-500">80% Correct Answers</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Regulatory Action Track:</span>
                    <span className="text-stone-200">Affidavit Validation Post-Exam</span>
                  </div>
                </div>

                {/* Direct PHI warning for audit defense */}
                <div className="bg-amber-950/20 border border-amber-500/20 p-4 rounded text-left max-w-md mx-auto">
                  <p className="text-[10px] text-stone-400 leading-relaxed font-mono">
                    <strong>Audit Integrity Rule:</strong> Any tab switching or idle status will temporarily pause active validation. Please ensure a stable network.
                  </p>
                </div>

                <div className="pt-4 flex flex-col sm:flex-row justify-center gap-3">
                  <button 
                    onClick={() => setCurrentView('finalAssessmentQuiz')}
                    className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors"
                  >
                    Begin Course Final Exam
                  </button>
                  <button 
                    onClick={() => setCurrentView('modules')}
                    className="bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-300 font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors"
                  >
                    Go Back & Study Modules
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* VIEW: FINAL QUIZ FLOW */}
          {currentView === 'finalAssessmentQuiz' && (
            <QuizFlowView 
              setView={setCurrentView}
              isFinalExam={true}
              onPass={(score) => {
                setFinalAssessmentPassed(true);
                setFinalAssessmentScore(score);
              }}
              onFail={(score) => {
                setFinalAssessmentPassed(false);
                setFinalAssessmentScore(score);
              }}
            />
          )}

          {/* VIEW: ASSESSMENT RESULT & REMEDIATION */}
          {currentView === 'finalResult' && (
            <div className="max-w-2xl mx-auto space-y-6 animate-in fade-in duration-300">
              <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl text-center space-y-6">
                
                {finalAssessmentPassed ? (
                  <>
                    <div className="w-16 h-16 rounded bg-emerald-950/40 border border-emerald-500/40 flex items-center justify-center mx-auto text-emerald-500">
                      <CheckCircle2 size={32} />
                    </div>
                    <div>
                      <span className="text-[10px] uppercase font-bold text-emerald-400 font-mono tracking-widest bg-emerald-950/20 px-2 py-0.5 rounded border border-emerald-500/10">Passed Course Exam</span>
                      <h1 className="text-3xl font-normal text-stone-100 tracking-tight mt-3">Competency Accomplished</h1>
                      <p className="text-xs text-stone-400 mt-2">
                        You have successfully proved theoretical mastery in all recertification criteria. 
                      </p>
                    </div>
                    <div className="bg-stone-950 p-4 rounded border border-stone-900 max-w-sm mx-auto font-mono text-xs text-stone-400 flex justify-between">
                      <span>Verified Score:</span>
                      <strong className="text-emerald-400">{finalAssessmentScore}% Correct</strong>
                    </div>
                    <div className="pt-4 flex flex-col sm:flex-row justify-center gap-3">
                      <button 
                        onClick={() => setCurrentView('certificate')}
                        className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors"
                      >
                        Proceed to Certificate Gate &rarr;
                      </button>
                    </div>
                  </>
                ) : (
                  <>
                    <div className="w-16 h-16 rounded bg-red-950/40 border border-red-500/40 flex items-center justify-center mx-auto text-red-500">
                      <AlertTriangle size={32} />
                    </div>
                    <div>
                      <span className="text-[10px] uppercase font-bold text-red-400 font-mono tracking-widest bg-red-950/20 px-2 py-0.5 rounded border border-red-500/10">Requires Remediation</span>
                      <h1 className="text-3xl font-normal text-stone-100 tracking-tight mt-3">Competency Not Achieved</h1>
                      <p className="text-xs text-stone-400 mt-2 max-w-md mx-auto leading-relaxed">
                        Your score fell below the required $80\%$ CDPH passing limit. In line with nursing recertification standards, correct answer keys remain locked to preserve educational integrity.
                      </p>
                    </div>

                    <div className="bg-stone-950 p-4 rounded border border-stone-900 max-w-sm mx-auto font-mono text-xs text-stone-400 flex justify-between">
                      <span>Achieved Score:</span>
                      <strong className="text-red-500">{finalAssessmentScore}% Correct</strong>
                    </div>

                    <div className="bg-red-950/10 border border-red-500/10 p-4 rounded text-left max-w-md mx-auto space-y-2">
                      <h4 className="text-[10px] uppercase font-bold text-stone-300 font-mono flex items-center gap-1">
                        <Info size={12} /> Directed Remediation Instructions
                      </h4>
                      <p className="text-[11px] text-stone-400 leading-relaxed">
                        Please review standard precautions, the six links of infection chain transmission, and proper PPE donning and doffing sequence inside Module 1 prior to initiating your next evaluation.
                      </p>
                    </div>

                    <div className="pt-4 flex flex-col sm:flex-row justify-center gap-3">
                      <button 
                        onClick={() => setCurrentView('finalAssessmentSplash')}
                        className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors"
                      >
                        Retake Assessment Exam
                      </button>
                      <button 
                        onClick={() => setCurrentView('modules')}
                        className="bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-300 font-bold px-6 py-3 rounded text-xs uppercase tracking-wider transition-colors"
                      >
                        Return to Modules
                      </button>
                    </div>
                  </>
                )}

              </div>
            </div>
          )}

          {/* VIEW: CERTIFICATE VIEW & GATES REVIEW */}
          {currentView === 'certificate' && (
            <CertificateGateView 
              setView={setCurrentView}
              module0Completed={module0Completed}
              activeTime={activeTimeSecs}
              lessonCompleted={lessonCompleted}
              finalAssessmentPassed={finalAssessmentPassed}
              affidavitSigned={affidavitSigned}
              setAffidavitSigned={setAffidavitSigned}
              m0FirstName={m0FirstName}
              m0LastName={m0LastName}
              m0License={m0License}
              formatHoursAndMins={formatHoursAndMins}
            />
          )}

          {/* VIEW: OPTIONAL CLINICAL SUPPORT HUB */}
          {currentView === 'clinical' && (
            <div className="space-y-6 animate-in fade-in duration-300">
              <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl">
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-stone-800/60">
                  <div>
                    <span className="text-[10px] uppercase font-bold text-amber-500 font-mono flex items-center gap-1.5">
                      <Stethoscope size={12} /> Optional Practical Enrichment
                    </span>
                    <h1 className="text-2xl font-normal text-stone-100 mt-1">Clinical Scenario Support Hub</h1>
                  </div>
                  <div className="shrink-0">
                    <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-[10px] font-bold bg-amber-950/40 text-amber-400 border border-amber-500/20 font-mono">
                      NON-GATING HOUR STUDY
                    </span>
                  </div>
                </div>

                <div className="bg-amber-950/10 border border-amber-500/20 rounded-lg p-4 my-6">
                  <div className="flex items-start gap-2.5">
                    <AlertTriangle size={16} className="text-amber-500 shrink-0 mt-0.5" />
                    <p className="text-[11px] text-stone-400 leading-relaxed font-mono">
                      <strong>Regulatory Warning:</strong> This module is entirely optional, for professional confidence only, and provides zero clinical CE hours. It does not gate nor count toward your required 12-hour theory CE, nor does it fulfill active hands-on CDPH clinical renewal requisites.
                    </p>
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4">
                  
                  {/* Scenario 1 */}
                  <div className="p-5 rounded-lg bg-[#080404] border border-stone-800 hover:border-stone-700 transition-colors">
                    <h3 className="text-xs font-bold uppercase tracking-wider text-stone-300 mb-2 font-mono">Scenario Demo A: Catheter Care</h3>
                    <p className="text-xs text-stone-400 leading-relaxed mb-4">
                      Review simulated sequence actions for cleaning and safety management of urinary drainage bags to prevent ascending UTIs.
                    </p>
                    <div className="flex items-center justify-between">
                      <span className="text-[10px] text-stone-500 font-mono">3 Interactive Cards</span>
                      <button 
                        onClick={() => setClinicalInteractions(prev => prev + 1)}
                        className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-4 py-1.5 rounded text-[10px] uppercase tracking-wider transition-colors"
                      >
                        Start Simulation
                      </button>
                    </div>
                  </div>

                  {/* Scenario 2 */}
                  <div className="p-5 rounded-lg bg-[#080404] border border-stone-800 hover:border-stone-700 transition-colors">
                    <h3 className="text-xs font-bold uppercase tracking-wider text-stone-300 mb-2 font-mono">Scenario Demo B: PPE Sequencer</h3>
                    <p className="text-xs text-stone-400 leading-relaxed mb-4">
                      Practice CDC ordering requirements for donning (putting on) and doffing (taking off) personal protective isolation suits safely.
                    </p>
                    <div className="flex items-center justify-between">
                      <span className="text-[10px] text-stone-500 font-mono">Don/Doff Selector</span>
                      <button 
                        onClick={() => setClinicalInteractions(prev => prev + 1)}
                        className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-4 py-1.5 rounded text-[10px] uppercase tracking-wider transition-colors"
                      >
                        Start Simulation
                      </button>
                    </div>
                  </div>

                </div>

                {clinicalInteractions > 0 && (
                  <div className="mt-6 p-4 rounded border border-stone-850 bg-stone-950 text-stone-400 text-xs font-mono flex justify-between items-center animate-in slide-in-from-bottom-2">
                    <span>Practiced Sessions in Portal:</span>
                    <strong className="text-amber-500">{clinicalInteractions} Simulations Verified</strong>
                  </div>
                )}
              </div>
            </div>
          )}

        </div>
      </main>
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
  
  // Track unique rationales clicked for remediation audit requirement
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
    <div className="space-y-6 animate-in zoom-in-95 duration-300">
      
      {/* Header Info */}
      <div className="flex items-center justify-between pb-3 border-b border-stone-800/60">
        <button 
          onClick={() => setView('module1')}
          className="text-stone-400 hover:text-stone-100 flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider"
        >
          <ArrowLeft size={14} /> Close Lesson Player
        </button>
        <div className="flex items-center gap-4 text-xs font-mono text-stone-400">
          <span className="flex items-center gap-1"><Clock size={12} className="text-amber-500" /> Lesson Session: 15m</span>
          <span>&bull;</span>
          <span className="text-amber-500 flex items-center gap-1">
            <span className="w-1.5 h-1.5 rounded-full bg-amber-500 animate-pulse"></span>
            Simulated Time: {formatHoursAndMins(activeTime)}
          </span>
        </div>
      </div>

      {/* Modern Horizontal Navigation Line */}
      <div className="flex items-center justify-between bg-stone-950/60 p-3 rounded-lg border border-stone-900 overflow-x-auto">
        {[
          { num: 1, name: "Card 1: Overview" },
          { num: 2, name: "Card 2: Delivery" },
          { num: 3, name: "Card 3: Challenge" },
          { num: 4, name: "Card 4: Debrief & Remediation" },
        ].map((step) => (
          <div key={step.num} className="flex items-center gap-3 shrink-0 mx-2">
            <div className={`w-5 h-5 rounded-full border flex items-center justify-center text-[10px] font-mono font-bold ${
              currentCard === step.num 
                ? 'bg-amber-500 border-amber-500 text-black' 
                : currentCard > step.num 
                  ? 'bg-emerald-950/40 text-emerald-400 border-emerald-500/20' 
                  : 'bg-transparent border-stone-800 text-stone-600'
            }`}>
              {currentCard > step.num ? <Check size={10} /> : step.num}
            </div>
            <span className={`text-[11px] font-semibold uppercase tracking-wider ${
              currentCard === step.num ? 'text-amber-500' : 'text-stone-500'
            }`}>
              {step.name}
            </span>
            {step.num < 4 && <div className="w-6 h-px bg-stone-900"></div>}
          </div>
        ))}
      </div>

      {/* Main Study Deck Card */}
      <div className="bg-[#120909] border border-stone-800/80 rounded-xl overflow-hidden shadow-2xl flex flex-col min-h-[500px]">
        
        <div className="p-6 md:p-8 flex-1 space-y-6">
          
          {/* CARD 1: OVERVIEW */}
          {currentCard === 1 && (
            <div className="space-y-6 animate-in fade-in duration-300">
              <div className="flex justify-between items-start">
                <div>
                  <span className="text-[10px] font-bold text-stone-500 uppercase tracking-widest font-mono">Module 1 • Lesson 1 • Card 1</span>
                  <h2 className="text-2xl font-normal text-stone-100 tracking-tight mt-1">Scope of Infection Control in LTC</h2>
                </div>
              </div>

              {/* High fidelity 16:9 media visual panel near top */}
              <div className="w-full aspect-video md:h-64 bg-stone-950 border border-stone-900 rounded-lg flex flex-col items-center justify-center relative overflow-hidden group">
                <div className="absolute top-3 left-3 bg-[#120909] border border-stone-800 rounded px-2 py-0.5 text-[9px] font-mono text-stone-400 uppercase tracking-wider">
                  Visual Blueprint L1-1
                </div>
                {/* SVG Schematic Blueprint */}
                <svg className="w-32 h-32 text-stone-800" viewBox="0 0 100 100" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <rect x="15" y="15" width="70" height="70" rx="3" />
                  <path d="M50 15v70M15 50h70" strokeDasharray="3 3" />
                  <circle cx="50" cy="50" r="10" stroke="#5c1111" strokeWidth="2" />
                  <circle cx="30" cy="35" r="5" />
                  <circle cx="70" cy="35" r="5" />
                  <circle cx="30" cy="65" r="5" />
                  <circle cx="70" cy="65" r="5" />
                </svg>
                <div className="text-[10px] font-mono text-stone-500 uppercase mt-2 tracking-widest">
                  Pathogen Proliferation & Contact Zone Model
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="space-y-2">
                  <h4 className="text-xs uppercase font-bold text-stone-400 font-mono tracking-wider">Core Principle</h4>
                  <p className="text-xs text-stone-400 leading-relaxed">
                    Long-term care facilities house highly vulnerable populations. As a CNA, your hand sanitation and PPE execution are the frontline defenses against devastating healthcare-associated infections (HAIs).
                  </p>
                </div>
                <div className="space-y-2">
                  <h4 className="text-xs uppercase font-bold text-stone-400 font-mono tracking-wider font-semibold">Core Focus Metrics</h4>
                  <div className="space-y-1.5 font-mono text-[10px] text-stone-500">
                    <div className="flex justify-between border-b border-stone-900 pb-1">
                      <span>LTC Infection Rates:</span>
                      <span className="text-stone-300">$1:10$ Active Residents</span>
                    </div>
                    <div className="flex justify-between border-b border-stone-900 pb-1">
                      <span>Primary Transmission:</span>
                      <span className="text-stone-300">Transient Hand Contact</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* CARD 2: DELIVERY */}
          {currentCard === 2 && (
            <div className="space-y-6 animate-in fade-in duration-300">
              <div className="flex justify-between items-start">
                <div>
                  <span className="text-[10px] font-bold text-stone-500 uppercase tracking-widest font-mono">Module 1 • Lesson 1 • Card 2</span>
                  <h2 className="text-2xl font-normal text-stone-100 tracking-tight mt-1">Understanding the Chain of Infection</h2>
                </div>
              </div>

              {/* 16:9 media visual panel near top */}
              <div className="w-full aspect-video md:h-64 bg-stone-950 border border-stone-900 rounded-lg flex flex-col items-center justify-center relative overflow-hidden">
                <div className="absolute top-3 left-3 bg-[#120909] border border-stone-800 rounded px-2 py-0.5 text-[9px] font-mono text-stone-400 uppercase tracking-wider">
                  Visual Blueprint L1-2
                </div>
                {/* SVG Schematic Chain */}
                <svg className="w-64 h-24 text-stone-800" viewBox="0 0 300 100" fill="none" stroke="currentColor" strokeWidth="1.5">
                  {/* Chain links */}
                  <rect x="10" y="30" width="60" height="40" rx="20" stroke="#d4af37" strokeWidth="2" />
                  <rect x="50" y="30" width="60" height="40" rx="20" />
                  <rect x="90" y="30" width="60" height="40" rx="20" stroke="#d4af37" strokeWidth="2" />
                  <rect x="130" y="30" width="60" height="40" rx="20" />
                  <rect x="170" y="30" width="60" height="40" rx="20" stroke="#d4af37" strokeWidth="2" />
                  <rect x="210" y="30" width="60" height="40" rx="20" />
                </svg>
                <div className="text-[10px] font-mono text-stone-500 uppercase tracking-widest mt-2">
                  Interactive Schematic: Six Links of Pathogen Transmission
                </div>
              </div>

              <div className="space-y-3">
                <h4 className="text-xs uppercase font-bold text-stone-400 font-mono tracking-wider">Breaking the Pathogen Cycle</h4>
                <p className="text-xs text-stone-400 leading-relaxed">
                  The six active links are: (1) Causative Agent, (2) Reservoir, (3) Portal of Exit, (4) Mode of Transmission, (5) Portal of Entry, and (6) Susceptible Host. Interruption at any of these nodes instantly halts contamination spread.
                </p>
                <div className="p-3 bg-[#1c0d0d] border border-[#5c1111]/30 rounded">
                  <p className="text-[11px] text-stone-300 leading-relaxed italic">
                    <strong>Critical CNA Link:</strong> Performing hand decontamination after client contact breaks the <em>Mode of Transmission</em> link.
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* CARD 3: CHALLENGE */}
          {currentCard === 3 && (
            <div className="space-y-6 animate-in fade-in duration-300">
              <div>
                <span className="text-[10px] font-bold text-stone-500 uppercase tracking-widest font-mono">Module 1 • Lesson 1 • Card 3</span>
                <h2 className="text-2xl font-normal text-stone-100 tracking-tight mt-1">Interactive Challenge Simulation</h2>
              </div>

              {/* 16:9 media visual panel near top */}
              <div className="w-full aspect-video md:h-56 bg-stone-950 border border-stone-900 rounded-lg flex flex-col items-center justify-center relative overflow-hidden">
                <div className="absolute top-3 left-3 bg-[#120909] border border-stone-800 rounded px-2 py-0.5 text-[9px] font-mono text-stone-400 uppercase tracking-wider">
                  Simulation Scene L1-3
                </div>
                <svg className="w-24 h-24 text-stone-800" viewBox="0 0 100 100" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <path d="M20 80h60M30 80V40h40v40" />
                  <path d="M40 30h20M50 20v10" />
                  <circle cx="50" cy="55" r="8" stroke="#d4af37" />
                </svg>
                <div className="text-[10px] font-mono text-stone-500 uppercase tracking-widest mt-2">
                  Client Room Environment & Contamination Map
                </div>
              </div>

              <div className="space-y-4">
                <p className="text-xs text-stone-300 leading-relaxed font-semibold">
                  SCENARIO: Resident Mr. Henderson is on Contact Precautions for a suspected MRSA wound infection. As you prepare to deliver a fresh water pitcher, what is your safest procedural sequence?
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
                          ? 'bg-[#1c0d0d] border-amber-500/50 text-stone-100' 
                          : 'bg-[#080404] border-stone-900 hover:border-stone-800 text-stone-400'
                      }`}
                    >
                      <div className={`mt-0.5 w-4 h-4 rounded border flex items-center justify-center text-[10px] font-bold shrink-0 ${
                        selectedAnswer === ans.id ? 'bg-amber-500 text-black border-amber-500' : 'border-stone-600 text-stone-500'
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
                    className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors"
                  >
                    Submit Decision Pattern
                  </button>
                )}
              </div>
            </div>
          )}

          {/* CARD 4: DEBRIEF & REMEDIATION */}
          {currentCard === 4 && (
            <div className="space-y-6 animate-in fade-in duration-300">
              <div>
                <span className="text-[10px] font-bold text-stone-500 uppercase tracking-widest font-mono">Module 1 • Lesson 1 • Card 4</span>
                <h2 className="text-2xl font-normal text-stone-100 tracking-tight mt-1">Review & Rationale Matrix</h2>
                <p className="text-xs text-stone-400 mt-1">
                  Compliance validation mandates clicking and reading both the Correct (A) and your selected choice rationales to finish the block.
                </p>
              </div>

              {/* 16:9 media visual panel near top */}
              <div className="w-full aspect-video md:h-52 bg-stone-950 border border-stone-900 rounded-lg flex flex-col items-center justify-center relative overflow-hidden">
                <div className="absolute top-3 left-3 bg-[#120909] border border-stone-800 rounded px-2 py-0.5 text-[9px] font-mono text-stone-400 uppercase tracking-wider">
                  Flow Schematic L1-4
                </div>
                <svg className="w-48 h-20 text-stone-800" viewBox="0 0 200 80" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <rect x="10" y="25" width="40" height="30" rx="3" />
                  <path d="M50 40h40" />
                  <polygon points="90,37 96,40 90,43" fill="currentColor" />
                  <rect x="100" y="25" width="40" height="30" rx="3" stroke="#d4af37" />
                  <path d="M140 40h40" />
                  <polygon points="180,37 186,40 180,43" fill="currentColor" />
                  <rect x="150" y="25" width="40" height="30" rx="3" />
                </svg>
                <div className="text-[10px] font-mono text-stone-500 uppercase tracking-widest mt-2">
                  Systematic Corrective Action Logic Loop
                </div>
              </div>

              {/* Rationale Matrix */}
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
                          ? 'bg-[#080404] border-[#5c1111]/60' 
                          : 'bg-stone-950/40 border-stone-900/60 opacity-75 hover:opacity-100'
                      }`}
                    >
                      <div className="flex items-center justify-between mb-2">
                        <div className="flex items-center gap-2">
                          <span className={`px-2 py-0.5 rounded text-[9px] font-mono font-bold ${
                            item.correct ? 'bg-emerald-950/60 text-emerald-400' : 'bg-red-950/60 text-red-400'
                          }`}>
                            {item.id} &bull; {item.type}
                          </span>
                          <h4 className="font-semibold text-stone-200">{item.title}</h4>
                        </div>
                        <span className="text-[10px] text-amber-500 font-mono font-semibold">
                          {isClicked ? "✓ Read" : "Click to Review"}
                        </span>
                      </div>
                      {isClicked && (
                        <p className="text-stone-400 leading-relaxed pl-1 animate-in slide-in-from-top-1">
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

        {/* Audio Narration Controller (Universal on all Cards) */}
        <div className="px-6 py-4 bg-[#0a0505] border-t border-stone-850 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <button 
              onClick={() => setIsPlaying(!isPlaying)}
              className="w-10 h-10 rounded-full bg-[#1c0d0d] border border-[#5c1111]/40 flex items-center justify-center text-amber-500 hover:bg-[#2c1212] transition-colors shrink-0"
            >
              {isPlaying ? <Pause size={16} className="fill-current" /> : <Play size={16} className="fill-current ml-0.5" />}
            </button>
            <div>
              <span className="text-xs font-semibold text-stone-200 block">Required Core Narration Audio</span>
              <span className="text-[10px] text-stone-500 font-mono block">
                {isPlaying ? "Active Playback Logged" : "Playback Standby"} (01:45)
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button 
              onClick={() => setShowTranscript(!showTranscript)}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded border text-xs font-mono transition-all ${
                showTranscript 
                  ? 'bg-amber-950/40 text-amber-400 border-amber-500/30' 
                  : 'bg-transparent border-stone-900 text-stone-500 hover:text-stone-300'
              }`}
            >
              <FileText size={12} /> Transcript Text
            </button>
          </div>
        </div>

        {showTranscript && (
          <div className="px-6 py-4 bg-stone-950 text-stone-400 text-xs italic leading-relaxed border-t border-stone-900 animate-in fade-in">
            &ldquo;In this nursing recertification system, standard precautions dictate treating all biological fluids as infectious. CNAs must construct physical barriers prior to touching potential host reservoirs like resident nightstands, catheters, or bed rails. Complete rationale review ensures clinical safety audit compliance.&rdquo;
          </div>
        )}

        {/* Course Card Navigation Bar */}
        <div className="px-6 py-4 bg-stone-950 border-t border-stone-850 flex items-center justify-between">
          <button 
            onClick={handlePrev}
            disabled={currentCard === 1}
            className="px-4 py-2 text-xs font-semibold text-stone-500 hover:text-stone-300 disabled:opacity-35 disabled:cursor-not-allowed uppercase tracking-wider"
          >
            &larr; Previous Card
          </button>
          
          <button 
            onClick={handleNext}
            disabled={currentCard === 3 && !submitted}
            className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-2.5 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
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

  // Simulated 5 Question Compliance Quiz
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
      <div className="flex justify-between items-center pb-3 border-b border-stone-800/60 font-mono text-xs text-stone-400">
        <span>Question {currentIdx + 1} of {questions.length}</span>
        <span>{isFinalExam ? "COURSE THEORY FINAL EXAM" : "MODULE 1 ASSESSMENT"}</span>
      </div>

      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl space-y-6">
        <div>
          <span className="text-[10px] font-bold text-amber-500 uppercase tracking-widest font-mono">Select One Response</span>
          <h2 className="text-base font-semibold text-stone-200 mt-1 leading-relaxed">
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
                  ? 'bg-[#1c0d0d] border-amber-500/50 text-stone-100' 
                  : 'bg-[#080404] border-stone-900 hover:border-stone-800 text-stone-400'
              }`}
            >
              <div className={`mt-0.5 w-4 h-4 rounded border flex items-center justify-center text-[10px] font-bold shrink-0 ${
                answers[currentQ.id] === opt.id ? 'bg-amber-500 text-black border-amber-500' : 'border-stone-600 text-stone-500'
              }`}>
                {opt.id}
              </div>
              <span>{opt.text}</span>
            </button>
          ))}
        </div>

        {/* Regulatory audit guardrail: strict lock on review keys */}
        <div className="bg-stone-950 p-3 rounded border border-stone-900/60 text-[10px] text-stone-500 font-mono">
          CDPH Compliance Guardrail: Real-time validation checks enabled. Incorrect answers are simulated silently.
        </div>

        <div className="pt-4 border-t border-stone-850 flex justify-between">
          <button 
            onClick={handlePrev}
            disabled={currentIdx === 0}
            className="px-4 py-2 text-xs font-semibold text-stone-500 hover:text-stone-300 disabled:opacity-35 uppercase tracking-wider"
          >
            Back
          </button>

          {currentIdx < questions.length - 1 ? (
            <button 
              onClick={handleNext}
              disabled={!answers[currentQ.id]}
              className="bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-200 font-bold px-5 py-2 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40"
            >
              Next
            </button>
          ) : (
            <button 
              onClick={handleSubmit}
              disabled={!allAnswered}
              className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-2.5 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40"
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

  // Check overall progress gating triggers
  const hoursCompleted = activeTime >= 43200; // 12 hours check
  const orientationReady = module0Completed;
  const theoryReady = lessonCompleted && finalAssessmentPassed;

  const allGatesPassed = orientationReady && hoursCompleted && theoryReady && affidavitSigned;

  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      
      <div className="flex flex-col lg:flex-row gap-8">
        
        {/* Left: Audit Compliance Panel */}
        <div className="w-full lg:w-[400px] shrink-0 space-y-6">
          <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6">
            <h2 className="text-lg font-semibold text-stone-200 mb-2 uppercase tracking-wider">Required Audit Checklist</h2>
            <p className="text-xs text-stone-400 leading-relaxed mb-6">
              Official CDPH continuing education certificates remain locked unless all active gates are checked.
            </p>

            <div className="space-y-4">
              
              {/* Gate 1 */}
              <div className="flex items-start gap-3 p-3 bg-[#080404] border border-stone-900 rounded">
                <div className="mt-0.5 shrink-0">
                  {orientationReady ? (
                    <CheckCircle2 size={16} className="text-emerald-500" />
                  ) : (
                    <Circle size={16} className="text-stone-600" />
                  )}
                </div>
                <div>
                  <span className="text-[11px] font-bold text-stone-300 block uppercase font-mono">01. Legal Identity Verified</span>
                  <span className="text-[10px] text-stone-500">First/Last name entered in Module 0.</span>
                </div>
              </div>

              {/* Gate 2 */}
              <div className="flex items-start gap-3 p-3 bg-[#080404] border border-stone-900 rounded">
                <div className="mt-0.5 shrink-0">
                  {hoursCompleted ? (
                    <CheckCircle2 size={16} className="text-emerald-500" />
                  ) : (
                    <Circle size={16} className="text-stone-600" />
                  )}
                </div>
                <div>
                  <span className="text-[11px] font-bold text-stone-300 block uppercase font-mono">02. 12-Hour Study Time</span>
                  <span className="text-[10px] text-stone-500">Logged session active: <strong className="text-amber-500 font-mono font-normal">{formatHoursAndMins(activeTime)}</strong></span>
                </div>
              </div>

              {/* Gate 3 */}
              <div className="flex items-start gap-3 p-3 bg-[#080404] border border-stone-900 rounded">
                <div className="mt-0.5 shrink-0">
                  {theoryReady ? (
                    <CheckCircle2 size={16} className="text-emerald-500" />
                  ) : (
                    <Circle size={16} className="text-stone-600" />
                  )}
                </div>
                <div>
                  <span className="text-[11px] font-bold text-stone-300 block uppercase font-mono">03. Competency Achieved</span>
                  <span className="text-[10px] text-stone-500">Modules Completed & Assessment Passed.</span>
                </div>
              </div>

              {/* Gate 4 - Interactive Affidavit */}
              <div className={`p-4 rounded border transition-colors ${
                affidavitSigned 
                  ? 'bg-emerald-950/10 border-emerald-500/20 text-stone-200' 
                  : 'bg-[#1c0c0c]/40 border-[#5c1111]/30 text-stone-400'
              }`}>
                <div className="flex items-start gap-3">
                  <div className="mt-0.5 shrink-0">
                    {affidavitSigned ? (
                      <CheckCircle2 size={16} className="text-emerald-500" />
                    ) : (
                      <Circle size={16} className="text-[#5c1111]" />
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
                            ? 'bg-stone-900 border-stone-800 text-stone-400' 
                            : 'bg-[#5c1111] border-[#8a1d1d] hover:bg-[#781616] text-stone-100'
                        }`}
                      >
                        {affidavitSigned ? "Revoke Signature" : "Sign Digital Affidavit"}
                      </button>
                    ) : (
                      <span className="text-[9px] text-stone-600 uppercase font-mono font-bold block">
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
          <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 relative overflow-hidden">
            <div className="flex items-center justify-between mb-4 pb-3 border-b border-stone-800/60">
              <h3 className="font-semibold text-stone-300 text-xs uppercase tracking-wider">Preview Engine</h3>
              <span className="text-[10px] font-bold font-mono text-red-500 bg-red-950/40 px-2 py-0.5 rounded border border-red-500/20">
                MOCK ONLY &bull; PRODUCTION DISABLED
              </span>
            </div>

            {/* MOCK CERTIFICATE CONTAINER */}
            <div className="w-full border-2 border-stone-800 bg-[#0c0505] p-8 md:p-12 rounded-lg relative overflow-hidden flex flex-col justify-between aspect-[1.414/1] shadow-2xl">
              
              {/* Outer border lines */}
              <div className="absolute inset-2 border border-stone-900 pointer-events-none"></div>

              {/* Diagonal Watermark Backdrop across the central zone */}
              <div className="absolute inset-0 flex items-center justify-center rotate-[-25deg] select-none pointer-events-none opacity-[0.03]">
                <span className="text-5xl md:text-8xl font-bold font-mono tracking-widest text-stone-200">
                  MOCK PREVIEW
                </span>
              </div>

              {/* QUADRANT 3 Floating Watermark (Specific compliance requested location) */}
              {/* Coordinates x:35-40% , y:62-68% */}
              <div 
                className="absolute select-none pointer-events-none z-30 opacity-20 border border-red-500/60 bg-red-950/20 px-3 py-1.5 text-center leading-none rounded"
                style={{ left: '38%', top: '65%', transform: 'translate(-50%, -50%) rotate(-10deg)' }}
              >
                <span className="text-[9px] md:text-[11px] font-bold text-red-500 tracking-wider font-mono block">
                  MOCK PREVIEW ONLY
                </span>
                <span className="text-[7px] md:text-[8px] font-mono text-stone-400 block mt-0.5 uppercase">
                  UNAUTHORIZED PRODUCTION
                </span>
              </div>

              {/* Certificate Content Header */}
              <div className="text-center space-y-3 relative z-10">
                <div className="w-12 h-12 mx-auto mb-2 opacity-55">
                  <svg viewBox="0 0 100 100" className="text-amber-500" stroke="currentColor" fill="none" strokeWidth="1.5">
                    <circle cx="50" cy="50" r="40" />
                    <path d="M50 10v80M10 50h80" strokeDasharray="2 2" />
                  </svg>
                </div>
                <h2 className="text-xl md:text-3xl font-serif text-stone-300 tracking-wide uppercase">Certificate of Completion</h2>
                <p className="text-[10px] md:text-xs text-stone-500 font-mono tracking-widest uppercase">CI Institute of Continuing Education</p>
              </div>

              {/* Recipient details */}
              <div className="text-center my-6 space-y-2 relative z-10">
                <span className="text-[10px] text-stone-500 italic block">This is to verify that</span>
                <h3 className="text-lg md:text-2xl font-serif text-amber-500 tracking-wide font-normal">
                  {m0FirstName ? `${m0FirstName} ${m0LastName}` : "[Verify Name in Module 0]"}
                </h3>
                <p className="text-[9px] md:text-[11px] text-stone-400 max-w-lg mx-auto leading-relaxed">
                  has successfully performed the 12-hour theoretical continuing education requirement for the Nursing Recertification Pathway under active log metrics.
                </p>
              </div>

              {/* Footer seals & Signatures */}
              <div className="flex justify-between items-end text-left relative z-10 border-t border-stone-900 pt-4 text-[9px] md:text-[10px] font-mono text-stone-500">
                <div>
                  <span className="block font-bold text-stone-400 uppercase">James Bond, CNA</span>
                  <span className="block">CNA LICENSE: {m0License || "UNVERIFIED"}</span>
                  <span className="block">ACTIVE HOURS: {formatHoursAndMins(activeTime)}</span>
                </div>
                <div className="text-center">
                  <span className="block border-b border-stone-800 pb-1 px-4 italic text-stone-400 font-serif">James Bond</span>
                  <span className="block pt-1 uppercase">Client Signature</span>
                </div>
                <div className="text-right">
                  <span className="block">CE PROVIDER #: CI-CE-99120</span>
                  <span className="block">CDPH COMPLIANCE VERIFIED</span>
                </div>
              </div>

            </div>

            <div className="mt-4 p-4 rounded bg-[#0c0505] border border-stone-900/60">
              <p className="text-xs text-stone-400 leading-relaxed">
                <strong>Legal Action Restrictions:</strong> Official certificate downloading is permanently locked in preview environments. Real validation files are strictly generated on CDPH-audited production servers only.
              </p>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}