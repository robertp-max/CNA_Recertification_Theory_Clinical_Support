import React, { useState } from 'react';
import { 
  Play, FileText, CheckCircle2, Circle, 
  ArrowRight, ArrowLeft, Clock, ShieldAlert, Image as ImageIcon,
  AlertTriangle, Info, Check, Lock, AlertCircle, Shield, BookOpen,
  ListChecks, FileCheck, Search, Flag
} from 'lucide-react';

export default function App() {
  const [currentView, setCurrentView] = useState('moduleSplash'); 
  // Views: 'moduleSplash', 'finalSplash', 'activeTest', 'testResult'

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
      <div className="fixed inset-0 pointer-events-none bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#4a0f0f]/30 via-[#0a0505] to-[#0a0505] z-0"></div>

      {/* DEV NAVIGATION - For Reviewing Different States */}
      <div className="bg-amber-500/10 border-b border-amber-500/20 px-4 py-2 flex items-center justify-center gap-4 relative z-50 text-xs overflow-x-auto whitespace-nowrap">
        <span className="font-bold text-amber-500 uppercase tracking-widest mr-2">Preview Toggle:</span>
        <button onClick={() => setCurrentView('moduleSplash')} className={currentView === 'moduleSplash' ? 'text-white' : 'text-stone-400 hover:text-stone-200'}>Module Splash</button>
        <span className="text-stone-700">|</span>
        <button onClick={() => setCurrentView('finalSplash')} className={currentView === 'finalSplash' ? 'text-white' : 'text-stone-400 hover:text-stone-200'}>Final Splash</button>
        <span className="text-stone-700">|</span>
        <button onClick={() => setCurrentView('activeTest')} className={currentView === 'activeTest' ? 'text-white' : 'text-stone-400 hover:text-stone-200'}>Active Question</button>
        <span className="text-stone-700">|</span>
        <button onClick={() => setCurrentView('testResult')} className={currentView === 'testResult' ? 'text-white' : 'text-stone-400 hover:text-stone-200'}>Result View</button>
      </div>

      {/* Global Navigation */}
      <header className="px-6 py-4 border-b border-white/5 bg-[#0d0707] relative z-20 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-white/10 flex items-center justify-center border border-white/20">
            <span className="text-white font-bold text-xs">CI</span>
          </div>
          <span className="font-medium text-white tracking-wide text-sm hidden sm:block">INSTITUTE OF NURSING</span>
        </div>
        <div className="flex items-center gap-2 md:gap-6 text-sm font-medium text-stone-400">
          <button className="hover:text-white transition-colors">Dashboard</button>
          <button className="text-white bg-white/5 px-3 py-1.5 rounded-lg">Modules</button>
          <button className="hover:text-white transition-colors">Certificate</button>
          <div className="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-500 flex items-center justify-center border border-amber-500/30 ml-2 md:ml-4">
            <span className="text-xs font-bold">JD</span>
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 w-full max-w-5xl mx-auto p-4 md:p-8 lg:p-12 relative z-10 overflow-y-auto">
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
          {currentView === 'moduleSplash' && <ModuleAssessmentSplash onStart={() => setCurrentView('activeTest')} />}
          {currentView === 'finalSplash' && <FinalAssessmentSplash onStart={() => setCurrentView('activeTest')} />}
          {currentView === 'activeTest' && <ActiveAssessment onComplete={() => setCurrentView('testResult')} />}
          {currentView === 'testResult' && <AssessmentResult onReturn={() => setCurrentView('finalSplash')} />}
        </div>
      </main>
    </div>
  );
}

// ==========================================
// VIEW 1: MODULE ASSESSMENT SPLASH
// ==========================================
function ModuleAssessmentSplash({ onStart }) {
  // Toggle this to see locked state vs unlocked state
  const [isLocked, setIsLocked] = useState(false);

  const topics = [
    "Chain of Infection", "Hand Hygiene", "PPE Selection", 
    "Infection Signs", "Safe Cleaning Practices"
  ];

  return (
    <div className="max-w-3xl mx-auto space-y-8 pb-12">
      <div className="flex items-center justify-between">
        <button className="text-stone-400 hover:text-white flex items-center gap-2 text-sm transition-colors">
          <ArrowLeft size={16} /> Return to Module
        </button>
        <button 
          onClick={() => setIsLocked(!isLocked)} 
          className="text-[10px] uppercase tracking-widest text-stone-500 hover:text-stone-300 border border-white/10 px-3 py-1 rounded"
        >
          Dev: Toggle Locked State
        </button>
      </div>

      <div>
        <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-3">Module 1 Assessment</div>
        <h1 className="text-4xl font-semibold text-white tracking-tight mb-4 leading-tight">Infection Control and PPE</h1>
      </div>

      <div className="grid md:grid-cols-3 gap-4">
        {/* Main Info Card */}
        <div className="md:col-span-2 bg-[#120a0a] border border-white/5 rounded-xl p-6 md:p-8 shadow-xl">
          <h2 className="text-sm font-semibold uppercase tracking-widest text-stone-500 mb-3 flex items-center gap-2">
            <Info size={16} /> Assessment Purpose
          </h2>
          <p className="text-stone-300 text-sm leading-relaxed mb-8">
            This assessment checks your understanding of the required concepts from Module 1 before you continue in the online CE pathway.
          </p>

          <h2 className="text-sm font-semibold uppercase tracking-widest text-stone-500 mb-4">What This Covers</h2>
          <div className="flex flex-wrap gap-2 mb-8">
            {topics.map(topic => (
              <span key={topic} className="inline-flex bg-white/[0.02] border border-white/10 rounded-lg px-3 py-1.5 text-xs text-stone-300">
                {topic}
              </span>
            ))}
          </div>

          <div className="bg-[#1a0f0f] border border-[#2a1616] rounded-xl p-5 flex items-start gap-4">
            <ShieldAlert size={20} className="text-amber-500 shrink-0 mt-0.5" />
            <div>
              <h3 className="text-xs font-semibold uppercase tracking-widest text-stone-300 mb-1">Retake / Remediation Rule</h3>
              <p className="text-stone-400 text-xs leading-relaxed">
                If you do not pass, you will be guided back to the lesson topics that need review before trying again according to course rules.
              </p>
            </div>
          </div>
        </div>

        {/* Sidebar Info Cards */}
        <div className="space-y-4">
          <div className="bg-[#120a0a] border border-white/5 rounded-xl p-6 shadow-xl">
            <Clock size={20} className="text-stone-500 mb-3" />
            <div className="text-xs font-bold uppercase tracking-widest text-stone-500 mb-1">Estimated Time</div>
            <div className="text-stone-200 text-sm font-medium">10–15 minutes</div>
          </div>

          <div className="bg-[#120a0a] border border-white/5 rounded-xl p-6 shadow-xl">
            <ListChecks size={20} className="text-stone-500 mb-3" />
            <div className="text-xs font-bold uppercase tracking-widest text-stone-500 mb-2">Format</div>
            <ul className="text-stone-400 text-xs space-y-1.5">
              <li>• Multiple choice</li>
              <li>• Scenario-based questions</li>
              <li>• One question at a time</li>
            </ul>
          </div>

          <div className="bg-[#120a0a] border border-white/5 rounded-xl p-6 shadow-xl">
            <FileCheck size={20} className="text-stone-500 mb-3" />
            <div className="text-xs font-bold uppercase tracking-widest text-stone-500 mb-2">Evidence Created</div>
            <ul className="text-stone-400 text-xs space-y-1.5 mb-4">
              <li>• Assessment opened event</li>
              <li>• Attempt timestamp</li>
              <li>• Submitted answers & score</li>
              <li>• Module completion update</li>
            </ul>
            <div className="pt-3 border-t border-white/5">
              <p className="text-[10px] text-stone-500 italic leading-relaxed">
                Your assessment attempt is saved as part of your course completion record.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Lock/Unlock CTA Area */}
      <div className={`p-6 border rounded-xl flex flex-col sm:flex-row sm:items-center justify-between gap-6 transition-all ${
        isLocked ? 'bg-[#1a0f0f] border-red-900/30' : 'bg-[#120a0a] border-white/5 shadow-xl'
      }`}>
        <div className="flex-1">
          {isLocked ? (
            <div className="flex items-start gap-3">
              <Lock size={20} className="text-red-400 shrink-0 mt-1" />
              <div>
                <h3 className="text-sm font-bold text-red-200 mb-1">Module Assessment Locked</h3>
                <p className="text-xs text-red-300/70 leading-relaxed">
                  Complete all required lessons, interactions, and active-time requirements in this module before beginning the assessment.
                </p>
              </div>
            </div>
          ) : (
            <div className="flex items-start gap-3">
              <CheckCircle2 size={20} className="text-green-500 shrink-0 mt-1" />
              <div>
                <h3 className="text-sm font-bold text-stone-200 mb-1">Ready to Begin</h3>
                <p className="text-xs text-stone-500 leading-relaxed">
                  Module lessons completed. Required interactions completed. Active-time requirement met.
                </p>
              </div>
            </div>
          )}
        </div>
        <button 
          onClick={onStart}
          disabled={isLocked}
          className={`shrink-0 w-full sm:w-auto px-8 py-3.5 rounded-xl font-semibold text-sm transition-all ${
            isLocked 
              ? 'bg-black/40 text-stone-600 border border-white/5 cursor-not-allowed'
              : 'bg-[#7a1212] hover:bg-[#5c0d0d] text-stone-100 border border-[#8f1818] shadow-lg'
          }`}
        >
          Begin Module 1 Assessment
        </button>
      </div>

      <div className="text-center pt-4">
        <p className="text-[10px] text-stone-500">
          This module assessment supports your required online CE completion record. It does not replace the final course assessment or final signed statement.
        </p>
      </div>
    </div>
  );
}

// ==========================================
// VIEW 2: FINAL COURSE ASSESSMENT SPLASH
// ==========================================
function FinalAssessmentSplash({ onStart }) {
  const modules = [
    "Orientation and Compliance Boundaries",
    "Infection Control and PPE",
    "Resident Rights and Abuse Prevention",
    "Dementia and Communication",
    "Mobility, Falls, and Safety",
    "Nutrition, Skin Integrity, and Vital Signs",
    "Documentation, Reporting, and Scope"
  ];

  return (
    <div className="max-w-4xl mx-auto space-y-8 pb-12">
      <div>
        <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-3">Formal Course Requirement</div>
        <h1 className="text-4xl md:text-5xl font-semibold text-white tracking-tight mb-4 leading-tight">Final Course Assessment</h1>
        <p className="text-lg text-stone-400">Required final knowledge check for the online CE theory pathway.</p>
      </div>

      <div className="bg-[#120a0a] border border-white/5 rounded-xl p-6 md:p-8 shadow-2xl">
        <h2 className="text-sm font-semibold uppercase tracking-widest text-stone-500 mb-3">Final Assessment Purpose</h2>
        <p className="text-stone-300 text-sm leading-relaxed mb-0">
          This final assessment checks your understanding across the required online CE theory pathway before the final statement and certificate preview steps.
        </p>
      </div>

      <div className="grid md:grid-cols-12 gap-6">
        
        {/* Left Column: Topics & Integrity */}
        <div className="md:col-span-7 space-y-6">
          <div className="bg-[#120a0a] border border-white/5 rounded-xl p-6 shadow-xl">
            <h2 className="text-xs font-semibold uppercase tracking-widest text-stone-500 mb-4">What This Final Assessment Covers</h2>
            <div className="space-y-2">
              {modules.map((mod, i) => (
                <div key={i} className="flex items-center gap-3 p-3 rounded-lg bg-white/[0.02] border border-white/5">
                  <div className="w-6 h-6 rounded bg-black flex items-center justify-center text-[10px] font-bold text-stone-500 shrink-0">
                    M{i}
                  </div>
                  <span className="text-sm text-stone-300">{mod}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="bg-[#1a0f0f] border border-red-900/30 rounded-xl p-6">
            <h2 className="text-xs font-semibold uppercase tracking-widest text-red-300 mb-2 flex items-center gap-2">
              <ShieldAlert size={14} /> Integrity Notice
            </h2>
            <p className="text-stone-400 text-xs leading-relaxed">
              Do not use outside help during the final assessment. Do not enter or upload PHI. The final assessment is part of the online CE completion record.
            </p>
          </div>
        </div>

        {/* Right Column: Requirements & Evidence */}
        <div className="md:col-span-5 space-y-6">
          <div className="bg-[#120a0a] border border-white/5 rounded-xl p-6 shadow-xl">
            <div className="text-xs font-bold uppercase tracking-widest text-stone-500 mb-1 flex items-center gap-2">
              <Clock size={16} className="text-stone-400" /> Estimated Time
            </div>
            <div className="text-stone-200 text-sm font-medium mb-4">30–45 minutes</div>
            <p className="text-[10px] text-stone-500 italic">Final time limit and attempt policy pending compliance approval.</p>
          </div>

          <div className="bg-[#120a0a] border border-white/5 rounded-xl p-6 shadow-xl">
            <h2 className="text-xs font-semibold uppercase tracking-widest text-stone-500 mb-4">Required Before Starting</h2>
            <ul className="space-y-3">
              {[
                "Required theory modules complete",
                "Required interactions complete",
                "Active-time requirement met",
                "Identity fields complete",
                "Online CE cap acknowledgement complete",
                "No-PHI acknowledgement complete"
              ].map((item, i) => (
                <li key={i} className="flex items-start gap-2 text-xs text-stone-300">
                  <CheckCircle2 size={14} className="text-green-500 shrink-0 mt-0.5" /> {item}
                </li>
              ))}
            </ul>
          </div>

          <div className="bg-[#120a0a] border border-white/5 rounded-xl p-6 shadow-xl">
            <h2 className="text-xs font-semibold uppercase tracking-widest text-stone-500 mb-3">Evidence Created</h2>
            <p className="text-[10px] text-stone-500 italic leading-relaxed mb-3">
              This final assessment attempt becomes part of your course completion and certificate-readiness evidence.
            </p>
            <ul className="text-stone-400 text-[11px] space-y-1">
              <li>• Final assessment attempt timestamp</li>
              <li>• Question responses & score summary</li>
              <li>• Pass/fail status & attempt count</li>
              <li>• Remediation record if not passed</li>
            </ul>
          </div>
        </div>
      </div>

      {/* Footer CTA & Path */}
      <div className="border-t border-white/5 pt-8 flex flex-col items-center">
        <button 
          onClick={onStart}
          className="px-12 py-4 rounded-xl font-semibold text-base transition-all bg-[#7a1212] hover:bg-[#5c0d0d] text-stone-100 border border-[#8f1818] shadow-lg mb-8"
        >
          Begin Final Course Assessment
        </button>

        <div className="w-full max-w-2xl bg-[#120a0a] border border-white/5 rounded-xl p-6 text-center">
          <h3 className="text-[10px] font-bold uppercase tracking-widest text-stone-500 mb-3">Certificate Path Reminder</h3>
          <div className="flex items-center justify-center gap-3 text-xs text-stone-300 font-medium mb-4">
            <span>Pass Assessment</span>
            <ArrowRight size={12} className="text-stone-600" />
            <span>Final Statement</span>
            <ArrowRight size={12} className="text-stone-600" />
            <span className="text-amber-500">Certificate Preview</span>
          </div>
          <p className="text-[10px] text-stone-500 leading-relaxed max-w-xl mx-auto">
            Passing the final assessment does not automatically issue a production certificate. Certificate release remains controlled by required certificate gates and approval metadata.
          </p>
        </div>
        
        <p className="text-[10px] text-stone-600 mt-6 text-center max-w-lg">
          <strong className="text-stone-500">Optional Clinical Support Boundary:</strong> Optional Clinical Support is separate and does not affect final assessment eligibility or online CE certificate readiness unless written CDPH-approved instructions say otherwise.
        </p>
      </div>
    </div>
  );
}

// ==========================================
// VIEW 3: ACTIVE ASSESSMENT (SINGLE QUESTION)
// ==========================================
function ActiveAssessment({ onComplete }) {
  const [selected, setSelected] = useState(null);
  const [isFlagged, setIsFlagged] = useState(false);

  // Question Mock Data
  const choices = [
    { id: 'A', text: "Immediately request a mechanical lift and two staff members." },
    { id: 'B', text: "Attempt to pivot the resident yourself using a gait belt." },
    { id: 'C', text: "Leave the room to check the resident's care plan documentation." },
    { id: 'D', text: "Lower the bed to the lowest position and place a mat." }
  ];

  return (
    <div className="max-w-3xl mx-auto flex flex-col h-[75vh]">
      
      {/* Assessment Top Bar */}
      <div className="bg-[#120a0a] border border-white/5 rounded-t-xl p-4 flex items-center justify-between shrink-0">
        <div className="text-xs font-semibold text-stone-400">
          Question <span className="text-white">12</span> of 25
        </div>
        <button 
          onClick={() => setIsFlagged(!isFlagged)}
          className={`flex items-center gap-2 text-xs font-medium px-3 py-1.5 rounded-lg border transition-colors ${
            isFlagged ? 'bg-amber-500/10 text-amber-500 border-amber-500/30' : 'bg-transparent text-stone-500 border-white/10 hover:bg-white/5 hover:text-stone-300'
          }`}
        >
          <Flag size={14} className={isFlagged ? 'fill-current' : ''} /> 
          {isFlagged ? 'Flagged' : 'Flag for review'}
        </button>
      </div>

      {/* Active Question Content */}
      <div className="bg-[#0f0808] border-x border-white/5 p-6 md:p-10 flex-1 overflow-y-auto">
        <div className="max-w-2xl mx-auto">
          
          <div className="mb-8">
            <h2 className="text-lg md:text-xl font-medium text-stone-200 leading-relaxed">
              You are assigned to transfer a resident who is normally a one-person assist. However, upon entering the room, the resident appears unusually lethargic and states they feel extremely weak today. What is your <strong className="text-amber-500">FIRST</strong> appropriate action?
            </h2>
          </div>

          {/* 16:9 Media Panel ONLY if needed by question */}
          {/* <MediaPanel label="Resident Transfer Scenario" /> */}

          <div className="space-y-3">
            {choices.map((choice) => (
              <button
                key={choice.id}
                onClick={() => setSelected(choice.id)}
                className={`w-full text-left p-5 rounded-xl border transition-all flex items-center gap-4 ${
                  selected === choice.id
                    ? 'bg-[#1a0f0f] border-amber-500/50 shadow-[0_0_15px_rgba(245,158,11,0.05)]'
                    : 'bg-[#120a0a] border-white/5 hover:border-white/20'
                }`}
              >
                <div className={`w-6 h-6 shrink-0 rounded-full border flex items-center justify-center transition-colors ${
                  selected === choice.id ? 'border-amber-500 bg-amber-500/10' : 'border-stone-600 bg-black/40'
                }`}>
                  {selected === choice.id && <div className="w-2.5 h-2.5 rounded-full bg-amber-500"></div>}
                </div>
                <span className={`text-sm leading-relaxed ${selected === choice.id ? 'text-stone-100 font-medium' : 'text-stone-400'}`}>
                  {choice.text}
                </span>
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Assessment Bottom Bar */}
      <div className="bg-[#120a0a] border border-white/5 rounded-b-xl p-4 flex items-center justify-between shrink-0">
        <button className="px-6 py-2.5 rounded-xl text-stone-500 hover:text-stone-300 hover:bg-white/5 font-medium text-sm transition-all">
          Previous
        </button>
        <button 
          onClick={onComplete}
          className="px-8 py-2.5 rounded-xl font-semibold text-sm flex items-center gap-2 transition-all bg-[#7a1212] hover:bg-[#5c0d0d] text-stone-100 border border-[#8f1818]"
        >
          Next Question <ArrowRight size={16} />
        </button>
      </div>

    </div>
  );
}

// ==========================================
// VIEW 4: ASSESSMENT RESULT (PASS/FAIL)
// ==========================================
function AssessmentResult({ onReturn }) {
  // Toggle this state to view Pass vs Fail UX
  const [passed, setPassed] = useState(false);

  return (
    <div className="max-w-2xl mx-auto animate-in zoom-in-95 duration-500 space-y-8 pb-12">
      
      <div className="flex justify-end">
        <button 
          onClick={() => setPassed(!passed)} 
          className="text-[10px] uppercase tracking-widest text-stone-500 hover:text-stone-300 border border-white/10 px-3 py-1 rounded"
        >
          Dev: Toggle Pass/Fail State
        </button>
      </div>

      <div className="bg-[#120a0a] border border-white/5 rounded-xl p-8 md:p-12 shadow-2xl text-center relative overflow-hidden">
        {passed && <div className="absolute top-0 left-0 right-0 h-1 bg-green-500"></div>}
        {!passed && <div className="absolute top-0 left-0 right-0 h-1 bg-amber-500"></div>}

        <div className="flex justify-center mb-6">
          {passed ? (
            <div className="w-20 h-20 rounded-full bg-green-500/10 border border-green-500/20 flex items-center justify-center">
              <CheckCircle2 size={40} className="text-green-500" />
            </div>
          ) : (
            <div className="w-20 h-20 rounded-full bg-amber-500/10 border border-amber-500/20 flex items-center justify-center">
              <AlertTriangle size={40} className="text-amber-500" />
            </div>
          )}
        </div>

        <div className="text-[10px] uppercase tracking-widest text-stone-500 font-bold mb-2">Final Course Assessment</div>
        <h1 className="text-3xl font-semibold text-white mb-2">
          {passed ? "Assessment Passed" : "Assessment Not Passed"}
        </h1>
        
        <div className="text-5xl font-mono font-light text-stone-300 my-6">
          {passed ? "88%" : "64%"}
        </div>

        <p className="text-sm text-stone-400 max-w-md mx-auto leading-relaxed mb-8">
          {passed 
            ? "You have successfully demonstrated knowledge across the required theory pathway. Answer keys are not revealed for final assessments."
            : "You did not meet the passing threshold for this attempt. Answer keys are not revealed. Please review the recommended remediation topics below before attempting the assessment again."}
        </p>

        {passed ? (
          <div className="space-y-4">
            <button className="w-full px-8 py-4 rounded-xl font-semibold text-base transition-all bg-[#7a1212] hover:bg-[#5c0d0d] text-stone-100 border border-[#8f1818] shadow-lg">
              Continue to Final Statement
            </button>
            <p className="text-[10px] text-stone-500 italic">Certificate preview remains controlled by gates.</p>
          </div>
        ) : (
          <div className="text-left bg-black/40 border border-white/5 rounded-xl p-6">
            <h3 className="text-xs font-bold uppercase tracking-widest text-stone-400 mb-4">Recommended Remediation Topics</h3>
            <ul className="space-y-3 mb-6">
              <li className="flex items-center justify-between text-sm text-stone-300 p-3 rounded-lg bg-white/[0.02] border border-white/5">
                <span>Safe Transfers and Mobility</span>
                <button className="text-amber-500 text-xs font-semibold hover:text-amber-400">Review Lesson</button>
              </li>
              <li className="flex items-center justify-between text-sm text-stone-300 p-3 rounded-lg bg-white/[0.02] border border-white/5">
                <span>Recognizing Infection Signs</span>
                <button className="text-amber-500 text-xs font-semibold hover:text-amber-400">Review Lesson</button>
              </li>
            </ul>
            <button 
              onClick={onReturn}
              className="w-full px-6 py-3.5 rounded-xl font-semibold text-sm transition-all bg-white/5 hover:bg-white/10 text-white border border-white/10"
            >
              Return to Course Dashboard
            </button>
            <p className="text-center text-[10px] text-stone-500 mt-4">
              Retake permitted according to approved policy or demo-safe placeholder.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

// ==========================================
// UTILITY COMPONENTS
// ==========================================
function MediaPanel({ label, icon: Icon = ImageIcon }) {
  return (
    <div className="w-full aspect-video bg-[#0c0707] border border-white/5 rounded-xl flex flex-col items-center justify-center text-stone-600 mb-8 overflow-hidden relative group shadow-inner">
      <div className="absolute inset-0 bg-gradient-to-tr from-black/40 to-transparent pointer-events-none"></div>
      <Icon size={40} className="mb-4 opacity-30 group-hover:opacity-50 transition-opacity" />
      <span className="text-xs font-semibold uppercase tracking-widest text-stone-500">{label || "Visual coming soon"}</span>
    </div>
  );
}