import React, { useState, useEffect } from 'react';
import { 
  Play, Pause, FileText, CheckCircle2, Circle, 
  ArrowRight, ArrowLeft, Clock, ShieldAlert, Image as ImageIcon,
  AlertTriangle, Info, Check, X, Shield, Stethoscope, 
  BookOpen, Lock, AlertCircle, ChevronRight, CheckSquare, Square,
  Video
} from 'lucide-react';

export default function App() {
  const [currentView, setCurrentView] = useState('dashboard'); 
  // Views: 'dashboard', 'modules', 'module0', 'module1', 'lesson'

  return (
    <div className="min-h-screen bg-[#0a0505] text-slate-200 font-sans selection:bg-amber-500/30 flex flex-col">
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

      {/* Global Navigation */}
      <TopNav currentView={currentView} setView={setCurrentView} />

      {/* Main Content Area */}
      <main className="flex-1 w-full max-w-6xl mx-auto p-4 md:p-8 relative z-10">
        <div className="transition-all duration-500 ease-in-out h-full">
          {currentView === 'dashboard' && <DashboardView setView={setCurrentView} />}
          {currentView === 'modules' && <ModulesView setView={setCurrentView} />}
          {currentView === 'module0' && <ModuleZeroView setView={setCurrentView} />}
          {currentView === 'module1' && <ModuleOneOverview setView={setCurrentView} />}
          {currentView === 'lesson' && <LessonView setView={setCurrentView} />}
        </div>
      </main>
    </div>
  );
}

// ==========================================
// SHARED NAVIGATION
// ==========================================
function TopNav({ currentView, setView }) {
  const navItems = [
    { id: 'dashboard', label: 'Dashboard' },
    { id: 'modules', label: 'Modules' },
    { id: 'certificate', label: 'Certificate' },
    { id: 'clinical', label: 'Clinical Hub' },
  ];

  return (
    <header className="px-6 py-4 border-b border-white/5 bg-black/20 backdrop-blur-md relative z-20 flex items-center justify-between">
      <div className="flex items-center gap-3 cursor-pointer" onClick={() => setView('dashboard')}>
        <div className="w-8 h-8 rounded-lg bg-white/10 flex items-center justify-center border border-white/20">
          <span className="text-white font-bold text-xs">CI</span>
        </div>
        <span className="font-medium text-white tracking-wide text-sm hidden sm:block">INSTITUTE OF NURSING</span>
      </div>
      
      <div className="flex items-center gap-2 md:gap-6 text-sm font-medium text-slate-400">
        {navItems.map(item => (
          <button 
            key={item.id}
            onClick={() => setView(item.id === 'certificate' || item.id === 'clinical' ? currentView : item.id)}
            className={`transition-colors px-3 py-1.5 rounded-lg ${
              currentView === item.id || (currentView.startsWith('module') && item.id === 'modules') || (currentView === 'lesson' && item.id === 'modules')
                ? 'text-white bg-white/5' 
                : 'hover:text-white hover:bg-white/[0.02]'
            }`}
          >
            {item.label}
          </button>
        ))}
        <div className="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-500 flex items-center justify-center border border-amber-500/30 ml-2 md:ml-4">
          <span className="text-xs font-bold">JD</span>
        </div>
      </div>
    </header>
  );
}

// ==========================================
// FLOW 1 & 2 & 3 & 4: DASHBOARD / PATHWAY / OVERVIEWS
// ==========================================
function DashboardView({ setView }) {
  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div className="bg-[#120a0a]/80 backdrop-blur-xl border border-white/5 rounded-xl p-8 md:p-12 shadow-2xl relative overflow-hidden flex flex-col lg:flex-row gap-12 lg:items-center">
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-96 h-96 rounded-full bg-amber-500/10 blur-3xl"></div>

        <div className="flex-1 relative z-10">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-950/30 border border-red-500/20 text-xs font-semibold tracking-wide text-red-200 uppercase mb-6">
            CNA Recertification
          </div>
          <h1 className="text-3xl md:text-5xl font-semibold text-white tracking-tight mb-4 leading-tight">
            Theory + Clinical Support
          </h1>
          <p className="text-lg text-slate-400 mb-10 max-w-xl leading-relaxed">
            Complete the required online theory pathway, and use optional clinical support tools for practice and confidence.
          </p>
          <div className="flex flex-col sm:flex-row items-center gap-4">
            <button 
              onClick={() => setView('module0')}
              className="w-full sm:w-auto bg-amber-500 hover:bg-amber-400 text-black font-semibold px-8 py-4 rounded-xl flex items-center justify-center gap-3 transition-all transform hover:-translate-y-0.5 shadow-[0_0_20px_rgba(245,158,11,0.15)]"
            >
              Start Module 0 <Play size={18} className="fill-current" />
            </button>
            <button 
              onClick={() => setView('modules')}
              className="w-full sm:w-auto bg-white/5 hover:bg-white/10 text-white font-medium px-8 py-4 rounded-xl transition-all border border-white/5"
            >
              View Pathway
            </button>
          </div>
        </div>

        <div className="w-full lg:w-[340px] shrink-0 bg-white/[0.02] border border-white/10 rounded-xl p-6 backdrop-blur-md relative z-10">
          <div className="flex items-center justify-between mb-6">
            <h3 className="font-semibold text-white">Certificate Status</h3>
            <Shield size={18} className="text-amber-500" />
          </div>
          <div className="bg-black/40 rounded-xl p-4 border border-white/5 mb-6">
            <div className="flex items-center justify-between text-xs mb-3">
              <span className="text-slate-400 uppercase tracking-wider font-semibold">Progress</span>
              <span className="text-amber-500 font-medium">11%</span>
            </div>
            <div className="w-full h-2 bg-white/10 rounded-full overflow-hidden">
              <div className="w-[11%] h-full bg-amber-500 rounded-full"></div>
            </div>
            <p className="text-[11px] text-slate-500 mt-3 flex items-center gap-1.5">
              <AlertCircle size={12} /> 6 requirements remaining
            </p>
          </div>
          <p className="text-xs text-slate-500 leading-relaxed">
            Preview only. No certificate is issued. CDPH approval is not claimed.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {[
          { icon: <BookOpen size={20}/>, title: "12-Hour Required Theory", desc: "Orientation, six theory modules, and a final exam." },
          { icon: <Stethoscope size={20}/>, title: "Optional Clinical Support", desc: "Skills refresh and scenario coaching. No clinical-hour credit." },
          { icon: <Shield size={20}/>, title: "No PHI Policy", desc: "Never enter protected health info. Use simulated examples only." }
        ].map((f, i) => (
          <div key={i} className="p-6 rounded-xl bg-[#120a0a]/60 border border-white/5 hover:bg-[#120a0a] transition-colors">
            <div className="text-amber-500/80 mb-4">{f.icon}</div>
            <h4 className="text-sm font-semibold text-white mb-2">{f.title}</h4>
            <p className="text-xs text-slate-400 leading-relaxed">{f.desc}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

function ModulesView({ setView }) {
  const modules = [
    { id: 'M0', title: 'Orientation', time: '0.5 hr', status: 'completed', action: () => setView('module0') },
    { id: 'M1', title: 'Infection Control & PPE', time: '1.5 hr', status: 'ready', action: () => setView('module1') },
    { id: 'M2', title: 'Resident Rights & Abuse', time: '2.0 hr', status: 'locked' },
    { id: 'M3', title: 'Dementia & Comm.', time: '2.0 hr', status: 'locked' },
    { id: 'M4', title: 'Mobility & Safety', time: '2.0 hr', status: 'locked' },
    { id: 'M5', title: 'Nutrition, Skin & Vitals', time: '2.0 hr', status: 'locked' },
  ];

  return (
    <div className="flex flex-col lg:flex-row gap-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
      <div className="w-full lg:w-80 shrink-0 space-y-6">
        <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-8 sticky top-8">
          <div className="text-[10px] uppercase tracking-widest text-amber-500 font-bold mb-4">Required Online CE</div>
          <h2 className="text-3xl font-semibold text-white mb-4 leading-tight">Your success is our mission.</h2>
          <p className="text-sm text-slate-400 mb-8">Complete all required modules and pass the final assessment to reach certificate readiness.</p>
          <div className="space-y-2 mb-8">
            <div className="flex justify-between text-xs font-semibold">
              <span className="text-white">Program progress</span>
              <span className="text-amber-500">11%</span>
            </div>
            <div className="w-full h-1.5 bg-white/10 rounded-full overflow-hidden">
              <div className="w-[11%] h-full bg-amber-500 rounded-full"></div>
            </div>
          </div>
          <button className="w-full py-3 rounded-xl border border-white/10 text-white font-medium text-sm hover:bg-white/5 transition-colors">
            View certificate path
          </button>
        </div>
      </div>
      <div className="flex-1">
        <div className="mb-8">
          <h2 className="text-3xl font-semibold text-white mb-2">Choose your module</h2>
          <p className="text-slate-400 text-sm">Required theory modules unlock sequentially.</p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {modules.map((m) => (
            <div 
              key={m.id} 
              className={`p-6 rounded-xl border transition-all ${
                m.status === 'locked' ? 'bg-black/20 border-white/5 opacity-60' : 'bg-[#120a0a]/80 border-white/10 hover:border-white/20 hover:bg-[#150c0c] cursor-pointer'
              }`}
              onClick={m.status !== 'locked' ? m.action : undefined}
            >
              <div className="flex items-start justify-between mb-4">
                <div>
                  <span className={`text-xs font-bold uppercase tracking-wider mb-1 block ${m.status === 'ready' ? 'text-amber-500' : 'text-slate-500'}`}>{m.id}</span>
                  <span className="text-xs text-slate-500">{m.time}</span>
                </div>
                {m.status === 'completed' && <CheckCircle2 size={20} className="text-green-500" />}
                {m.status === 'locked' && <Lock size={16} className="text-slate-600" />}
              </div>
              <h3 className={`text-lg font-medium mb-8 ${m.status === 'locked' ? 'text-slate-400' : 'text-white'}`}>{m.title}</h3>
              <div className="mt-auto">
                {m.status === 'completed' && (
                  <button className="px-5 py-2 rounded-full bg-white/10 text-white text-xs font-semibold hover:bg-white/20 transition-colors flex items-center gap-2">
                    Review <ArrowRight size={14}/>
                  </button>
                )}
                {m.status === 'ready' && (
                  <button className="px-5 py-2 rounded-full bg-amber-500 text-black text-xs font-semibold hover:bg-amber-400 transition-colors flex items-center gap-2">
                    Start <Play size={12} className="fill-current"/>
                  </button>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function ModuleZeroView({ setView }) {
  const [agreed, setAgreed] = useState([true, false, false]);
  const toggleAgree = (index) => {
    const newAgreed = [...agreed];
    newAgreed[index] = !newAgreed[index];
    setAgreed(newAgreed);
  };
  const allAgreed = agreed.every(Boolean);

  return (
    <div className="max-w-3xl mx-auto animate-in fade-in slide-in-from-bottom-4 duration-500">
      <button onClick={() => setView('modules')} className="text-slate-400 hover:text-white flex items-center gap-2 text-sm mb-8 transition-colors">
        <ArrowLeft size={16} /> Back to Modules
      </button>
      <div className="mb-8">
        <div className="text-[10px] uppercase tracking-widest text-slate-500 font-bold mb-2">0.5 HR • REQUIRED ONLINE CE</div>
        <h1 className="text-3xl md:text-4xl font-semibold text-white mb-3">Module 0: Orientation and Compliance</h1>
        <p className="text-slate-400 text-sm">Course scope, identity confirmation, online cap and no-PHI acknowledgements.</p>
      </div>
      <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-8 md:p-10 shadow-xl">
        <h2 className="text-xl font-semibold text-white mb-2">Orientation & required acknowledgements</h2>
        <p className="text-sm text-slate-400 mb-8">Confirm your certificate identity and complete the required acknowledgements to unlock the theory pathway.</p>
        <div className="space-y-5 mb-10">
          <div>
            <label className="block text-xs font-medium text-slate-400 mb-1.5 ml-1">Legal first name</label>
            <input type="text" defaultValue="James" className="w-full bg-black/40 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-amber-500 transition-colors" />
          </div>
          <div>
            <label className="block text-xs font-medium text-slate-400 mb-1.5 ml-1">Legal last name</label>
            <input type="text" defaultValue="Bond" className="w-full bg-black/40 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-amber-500 transition-colors" />
          </div>
          <div>
            <label className="block text-xs font-medium text-slate-400 mb-1.5 ml-1">CNA certificate number</label>
            <input type="text" defaultValue="CNA_DEMO-007" className="w-full bg-black/40 border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-amber-500 transition-colors" />
          </div>
        </div>
        <div className="space-y-3 mb-10">
          {[
            "I understand the 24-hour online CE cap and that this course is partial renewal credit only.",
            "I will not enter or upload PHI about real patients, residents, or individuals anywhere in this course.",
            "I understand optional clinical support is separate and does not affect the online CE certificate."
          ].map((text, i) => (
            <div key={i} onClick={() => toggleAgree(i)} className={`flex items-start gap-4 p-4 rounded-xl border cursor-pointer transition-colors ${agreed[i] ? 'bg-amber-500/10 border-amber-500/30' : 'bg-black/20 border-white/5 hover:border-white/10'}`}>
              <div className="mt-0.5 text-amber-500">
                {agreed[i] ? <CheckSquare size={20} /> : <Square size={20} className="text-slate-500" />}
              </div>
              <p className={`text-sm leading-relaxed ${agreed[i] ? 'text-amber-100' : 'text-slate-400'}`}>{text}</p>
            </div>
          ))}
        </div>
        <div className="flex items-center gap-4 pt-6 border-t border-white/5">
          <button 
            onClick={() => setView('module1')}
            // Validation removed for preview
            className="px-8 py-4 rounded-xl font-semibold flex items-center justify-center gap-3 transition-all w-full sm:w-auto bg-amber-500 hover:bg-amber-400 text-black transform hover:-translate-y-0.5"
          >
            Continue to Module 1 <ArrowRight size={18} />
          </button>
        </div>
      </div>
    </div>
  );
}

function ModuleOneOverview({ setView }) {
  const lessons = [
    "Why Infection Control Matters in Long-Term Care",
    "The Chain of Infection",
    "Hand Hygiene — Your Most Important Tool",
    "Personal Protective Equipment (PPE)",
    "Recognizing and Reporting Infection Signs",
    "Environmental Cleaning and Safe Practices"
  ];

  return (
    <div className="max-w-4xl mx-auto animate-in fade-in slide-in-from-bottom-4 duration-500">
      <button onClick={() => setView('modules')} className="text-slate-400 hover:text-white flex items-center gap-2 text-sm mb-8 transition-colors">
        <ArrowLeft size={16} /> Back to Modules
      </button>

      <div className="mb-8 flex justify-between items-end">
        <div>
          <div className="text-[10px] uppercase tracking-widest text-slate-500 font-bold mb-2">1.5 HR • REQUIRED ONLINE CE</div>
          <h1 className="text-3xl md:text-5xl font-semibold text-white mb-3 tracking-tight">Infection Control and PPE</h1>
          <p className="text-slate-400 text-sm md:text-base">Chain of infection, hand hygiene, PPE, recognizing and reporting infection, and safe cleaning.</p>
        </div>
        <div className="hidden sm:flex px-4 py-2 rounded-xl border border-white/10 bg-white/5 items-center gap-2 text-xs font-medium text-slate-300">
          <Lock size={14} /> Not Started
        </div>
      </div>

      <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-8 mb-6 shadow-lg">
        <h2 className="text-lg font-semibold text-white mb-6">Learning goals</h2>
        <ul className="space-y-4">
          {[
            "Describe healthcare-associated infections (HAIs) and why LTC residents are at higher risk.",
            "Identify the six links in the chain of infection.",
            "Demonstrate proper hand hygiene technique, including the WHO 5 Moments.",
            "Select the correct PPE for common CNA tasks.",
            "Recognize common signs and symptoms of infection in LTC residents."
          ].map((goal, i) => (
            <li key={i} className="flex gap-3 items-start">
              <CheckCircle2 size={18} className="text-amber-500 shrink-0 mt-0.5" />
              <span className="text-slate-300 text-sm leading-relaxed">{goal}</span>
            </li>
          ))}
        </ul>
      </div>

      <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl p-8 shadow-lg">
        <h2 className="text-lg font-semibold text-white mb-6">Lessons</h2>
        <div className="space-y-2 mb-8">
          {lessons.map((lesson, i) => (
            <div 
              key={i} 
              onClick={() => i === 0 && setView('lesson')}
              className={`flex items-center justify-between p-4 rounded-xl border transition-all ${
                i === 0 ? 'bg-white/5 border-white/10 hover:bg-white/10 cursor-pointer group' : 'bg-black/20 border-white/5 opacity-60'
              }`}
            >
              <div className="flex items-center gap-4">
                <div className="w-8 h-8 rounded-full border border-white/10 flex items-center justify-center text-xs text-slate-400 bg-black/50">
                  {i + 1}
                </div>
                <div>
                  <h4 className={`text-sm font-medium ${i === 0 ? 'text-white' : 'text-slate-300'}`}>{lesson}</h4>
                  <p className="text-xs text-slate-500 mt-1">15 min</p>
                </div>
              </div>
              <ChevronRight size={18} className={i === 0 ? 'text-amber-500 transform group-hover:translate-x-1 transition-transform' : 'text-slate-600'} />
            </div>
          ))}
        </div>

        <button 
          onClick={() => setView('lesson')}
          className="bg-amber-500 hover:bg-amber-400 text-black font-semibold px-8 py-3.5 rounded-xl flex items-center justify-center gap-3 transition-all"
        >
          Start Module <Play size={16} className="fill-current" />
        </button>
      </div>
    </div>
  );
}

// ==========================================
// FLOW 5: HIGH-FIDELITY 4-CARD LESSON PLAYER
// Includes Completion Validations & 16:9 Media Panels
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

function LessonView({ setView }) {
  const [currentStep, setCurrentStep] = useState(0); 
  const [completedSteps, setCompletedSteps] = useState([]);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [submittedAnswer, setSubmittedAnswer] = useState(null);
  const [activeTime, setActiveTime] = useState(0);

  // Mark a step complete to unlock the Continue button
  const markStepComplete = (stepId) => {
    if (!completedSteps.includes(stepId)) {
      setCompletedSteps([...completedSteps, stepId]);
    }
  };

  useEffect(() => {
    const timer = setInterval(() => setActiveTime(t => t + 1), 1000);
    return () => clearInterval(timer);
  }, []);

  const formatTime = (secs) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  const handleNext = () => {
    // Validations removed for preview
    if (currentStep < 4) {
      markStepComplete(currentStep); // auto-complete for UI visuals
      setCurrentStep(c => c + 1);
    } else if (currentStep === 4) {
      setView('dashboard'); // Exit to dashboard on complete
    }
  };

  const handlePrev = () => {
    if (currentStep > 0) setCurrentStep(c => c - 1);
  };

  const steps = [
    { label: "Overview", id: 0 },
    { label: "Chain of Infection", id: 1 },
    { label: "HAIs", id: 2 },
    { label: "Challenge", id: 3 },
    { label: "Debrief", id: 4 }
  ];

  const canContinue = completedSteps.includes(currentStep);

  return (
    <div className="max-w-5xl mx-auto h-[85vh] flex flex-col animate-in zoom-in-95 duration-500">
      <div className="bg-[#120a0a]/95 backdrop-blur-xl border border-white/10 rounded-xl shadow-2xl flex flex-col h-full overflow-hidden relative">
        
        {/* Header - Minimalist */}
        <div className="px-6 py-4 border-b border-white/5 flex items-center justify-between bg-black/40 shrink-0">
          <button onClick={() => setView('module1')} className="text-slate-400 hover:text-white transition-colors p-2 -ml-2 rounded-xl hover:bg-white/5 flex items-center gap-2 text-sm font-medium">
            <ArrowLeft size={16} /> Exit
          </button>
          
          <div className="flex items-center gap-2 text-xs font-medium text-slate-500">
            <span>Module 1</span><ChevronRight size={12} />
            <span className="text-slate-300">Lesson 1</span>
          </div>

          <div className="flex items-center gap-2 text-amber-500 text-xs font-mono font-medium tracking-wider" title="MVP Active Time Engine">
            <div className="w-1.5 h-1.5 rounded-full bg-amber-500 animate-pulse"></div>
            {formatTime(activeTime)}
          </div>
        </div>

        {/* Floating Top Sequence Bar */}
        <div className="bg-white/[0.01] border-b border-white/5 px-6 py-3 flex items-center gap-6 overflow-x-auto custom-scrollbar shrink-0">
          {steps.map((step, idx) => (
            <div key={idx} className="flex items-center gap-3 shrink-0">
              <div className={`w-5 h-5 rounded-full border flex items-center justify-center text-[10px] transition-colors ${
                currentStep === step.id 
                  ? 'bg-amber-500 border-amber-500 text-black font-bold'
                  : completedSteps.includes(step.id) 
                    ? 'bg-[#120a0a] border-stone-500 text-stone-400' 
                    : 'bg-transparent border-white/10 text-stone-600'
              }`}>
                {completedSteps.includes(step.id) && currentStep !== step.id ? <Check size={10} strokeWidth={3} /> : step.id + 1}
              </div>
              <span className={`text-xs font-medium ${currentStep === step.id ? 'text-stone-200' : 'text-stone-500'}`}>
                {step.label}
              </span>
              {idx < steps.length - 1 && <div className="w-4 h-px bg-white/10 ml-3"></div>}
            </div>
          ))}
        </div>

        {/* Central Card Content */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-8 md:p-12 relative">
          <div className="max-w-4xl mx-auto pb-10">
            {currentStep === 0 && <Card1Overview onComplete={() => markStepComplete(0)} />}
            {currentStep === 1 && <Card2Delivery title="The Chain of Infection" onComplete={() => markStepComplete(1)} />}
            {currentStep === 2 && <Card2Delivery title="Healthcare-Associated Infections (HAIs)" onComplete={() => markStepComplete(2)} />}
            {currentStep === 3 && (
              <Card3Challenge 
                selectedAnswer={selectedAnswer}
                setSelectedAnswer={setSelectedAnswer}
                onSubmit={() => {
                  setSubmittedAnswer(selectedAnswer);
                  markStepComplete(3);
                  setCurrentStep(4);
                }}
              />
            )}
            {currentStep === 4 && <Card4Debrief submittedAnswer={submittedAnswer} onComplete={() => markStepComplete(4)} />}
          </div>
        </div>

        {/* Footer Navigation (With Validations) */}
        <div className="px-6 py-4 border-t border-white/5 bg-[#0a0505] flex items-center justify-between shrink-0">
          <button 
            onClick={handlePrev}
            disabled={currentStep === 0}
            className="px-6 py-2.5 rounded-xl text-slate-400 hover:text-white hover:bg-white/5 font-medium text-sm transition-all disabled:opacity-30 disabled:cursor-not-allowed disabled:hover:bg-transparent"
          >
            Previous
          </button>
          
          <button 
            onClick={handleNext}
            // Validations removed for preview
            className="px-8 py-2.5 rounded-xl font-semibold text-sm flex items-center gap-2 transition-all shadow-lg bg-[#7a1212] hover:bg-[#5c0d0d] text-stone-100 border border-[#8f1818]"
          >
            {currentStep === 4 ? 'Complete Lesson' : 'Continue'} <ArrowRight size={16} />
          </button>
        </div>

      </div>
    </div>
  );
}

// --- Card 1: Overview ---
function Card1Overview({ onComplete }) {
  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
      <div className="text-[10px] uppercase tracking-widest text-stone-500 font-bold">L01-CARD-1: Overview</div>
      <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl overflow-hidden shadow-2xl">
        <div className="p-8 border-b border-white/5">
          <div className="flex items-center gap-2 text-stone-400 text-sm mb-4 font-medium">
            <Clock size={16} className="text-amber-500" /> Estimated time: 15 min
          </div>
          <h1 className="text-3xl font-semibold text-stone-100 tracking-tight leading-tight mb-6">
            Why Infection Control Matters in Long-Term Care
          </h1>
          
          <div className="bg-[#1a0f0f] border-l-2 border-amber-500 p-4 rounded-r-xl mb-8">
            <p className="text-stone-300 text-sm leading-relaxed">
              <strong className="text-amber-500 font-semibold uppercase tracking-wider text-[10px] block mb-1">Learning Goal</strong>
              Explain why long-term care residents are at higher risk for infection and the CNA's role in prevention.
            </p>
          </div>

          <MediaPanel label="Video Placeholder: Infection Risks in LTC" icon={Video} />
          
          <div className="grid sm:grid-cols-2 gap-8">
            <div>
              <h3 className="text-[11px] uppercase tracking-widest text-stone-500 font-semibold mb-3">Why this matters</h3>
              <p className="text-stone-400 text-sm leading-relaxed">
                Residents with weakened immune systems can become seriously ill from common germs. Early recognition and prevention protect every resident on the unit.
              </p>
            </div>
            <div>
              <h3 className="text-[11px] uppercase tracking-widest text-stone-500 font-semibold mb-3">After this lesson, you will</h3>
              <ul className="space-y-3">
                <li className="flex items-start gap-2 text-stone-400 text-sm leading-relaxed">
                  <Check size={16} className="text-amber-500 shrink-0 mt-0.5" /> Recognize the chain of infection.
                </li>
                <li className="flex items-start gap-2 text-stone-400 text-sm leading-relaxed">
                  <Check size={16} className="text-amber-500 shrink-0 mt-0.5" /> Identify high-risk HAI scenarios.
                </li>
              </ul>
            </div>
          </div>
        </div>
        <NarrationBlock audioDuration="1:45" onInteract={onComplete} />
      </div>
    </div>
  );
}

// --- Card 2: Delivery ---
function Card2Delivery({ title, onComplete }) {
  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
      <div className="text-[10px] uppercase tracking-widest text-stone-500 font-bold">L01-CARD-2: Delivery</div>
      <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl overflow-hidden shadow-2xl">
        <div className="p-8 border-b border-white/5">
          <h2 className="text-2xl font-semibold text-stone-100 tracking-tight leading-tight mb-8">
            {title}
          </h2>

          <MediaPanel label="Diagram: The Chain of Infection" />

          <div className="mb-8">
            <h3 className="text-[11px] uppercase tracking-widest text-stone-500 font-semibold mb-3">Key Concept</h3>
            <p className="text-stone-300 text-base leading-relaxed">
              Infection requires a clear path to spread. If any link in the chain is broken, the infection stops. As a CNA, your primary tool to break the chain is rigorous hand hygiene and proper use of personal protective equipment (PPE).
            </p>
          </div>

          <div className="bg-[#1a0f0f] rounded-xl p-6 border border-white/5">
            <h3 className="text-[11px] uppercase tracking-widest text-stone-500 font-semibold mb-3 flex items-center gap-2">
              <ShieldAlert size={14} className="text-amber-500"/> CNA Practice Example
            </h3>
            <p className="text-stone-400 text-sm italic leading-relaxed">
              "You are assisting Mr. Davis with catheter care. Without proper gloves and handwashing, bacteria from his indwelling device can be transferred to the bed linens, and subsequently to your next resident."
            </p>
          </div>
        </div>
        <NarrationBlock audioDuration="2:10" onInteract={onComplete} />
      </div>
    </div>
  );
}

// --- Card 3: Challenge ---
function Card3Challenge({ selectedAnswer, setSelectedAnswer, onSubmit }) {
  const choices = [
    { id: 'A', text: "Put on appropriate mask and gloves before entering the room." },
    { id: 'B', text: "Serve the resident breakfast quickly to minimize contact time." },
    { id: 'C', text: "Inform the charge nurse immediately, then return to the room." },
    { id: 'D', text: "Open the window to improve ventilation before providing care." }
  ];

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
      <div className="text-[10px] uppercase tracking-widest text-stone-500 font-bold">L01-CARD-3: Challenge</div>
      <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl overflow-hidden shadow-2xl p-8">
        
        <h3 className="text-[11px] uppercase tracking-widest text-stone-500 font-semibold mb-3">Scenario</h3>
        <p className="text-stone-200 text-lg leading-relaxed mb-8">
          A resident has a new, persistent cough and a mild fever.
        </p>

        <MediaPanel label="Scenario: A Resident with a Cough" />

        <p className="text-stone-200 text-base font-medium mb-6">
          What is the <strong className="text-amber-500">FIRST</strong> action you should take before helping with morning care?
        </p>

        <div className="space-y-3">
          {choices.map((choice) => (
            <button
              key={choice.id}
              onClick={() => setSelectedAnswer(choice.id)}
              className={`w-full text-left p-5 rounded-xl border transition-all flex items-start gap-4 ${
                selectedAnswer === choice.id
                  ? 'bg-[#1a0f0f] border-amber-500/50 shadow-[0_0_15px_rgba(245,158,11,0.05)]'
                  : 'bg-black/20 border-white/5 hover:border-white/20'
              }`}
            >
              <div className={`w-6 h-6 shrink-0 rounded border flex items-center justify-center text-xs font-bold mt-0.5 transition-colors ${
                selectedAnswer === choice.id ? 'bg-amber-500 text-black border-amber-500' : 'border-stone-600 text-stone-500'
              }`}>
                {choice.id}
              </div>
              <span className={`text-sm leading-relaxed ${selectedAnswer === choice.id ? 'text-stone-100 font-medium' : 'text-stone-400'}`}>
                {choice.text}
              </span>
            </button>
          ))}
        </div>

        <div className="mt-8 pt-6 border-t border-white/5">
          <button 
            onClick={onSubmit}
            // Validations removed for preview
            className="w-full sm:w-auto px-10 py-3.5 rounded-xl font-semibold text-sm transition-all bg-[#7a1212] hover:bg-[#5c0d0d] text-stone-100 border border-[#8f1818]"
          >
            Submit Answer
          </button>
        </div>
      </div>
    </div>
  );
}

function Card4Debrief({ submittedAnswer, onComplete }) {
  const [viewedRationales, setViewedRationales] = useState([]);

  // Check completion: Learner must view Correct answer (A) AND their selected answer (if not A)
  useEffect(() => {
    const requiredViews = ['A'];
    if (submittedAnswer && submittedAnswer !== 'A') {
      requiredViews.push(submittedAnswer);
    }
    const hasViewedAllRequired = requiredViews.every(req => viewedRationales.includes(req));
    if (hasViewedAllRequired) {
      onComplete();
    }
  }, [viewedRationales, submittedAnswer, onComplete]);

  const handleRationaleView = (id) => {
    if (!viewedRationales.includes(id)) {
      setViewedRationales([...viewedRationales, id]);
    }
  };

  const rationales = [
    {
      id: 'A', isCorrect: true,
      rationale: "Putting on appropriate mask and gloves protects you and prevents you from becoming a vector before any care begins.",
      practice: "Always prioritize barrier protection when new respiratory symptoms appear.",
    },
    {
      id: 'B', isCorrect: false,
      rationale: "Speed does not replace infection control. Serving breakfast without protection directly exposes you to potential pathogens.",
      practice: "Never skip PPE for the sake of efficiency.",
    },
    {
      id: 'C', isCorrect: false,
      rationale: "While the nurse must be informed, your immediate physical safety and the prevention of spread takes precedent before leaving the area.",
      practice: "Protect first, then report changes in condition.",
    },
    {
      id: 'D', isCorrect: false,
      rationale: "Opening a window does not stop direct droplet or contact transmission during close personal care.",
      practice: "Environmental controls are secondary to direct PPE.",
    }
  ];

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
      <div className="text-[10px] uppercase tracking-widest text-stone-500 font-bold">L01-CARD-4: Debrief</div>
      <div className="bg-[#120a0a]/80 border border-white/5 rounded-xl overflow-hidden shadow-2xl p-6 sm:p-8">
        <h2 className="text-2xl font-semibold text-stone-100 mb-2">Challenge Review</h2>
        <p className="text-stone-400 text-sm mb-8">
          Review the rationale below. You selected <strong className="text-amber-500">Answer {submittedAnswer}</strong>. 
          {submittedAnswer === 'A' ? ' Great job!' : ' Let\'s look at why that wasn\'t the safest choice.'}
        </p>

        <MediaPanel label="Summary Diagram: Safe CNA Practice" />

        {/* 2x2 Grid / Stacked on Mobile */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {rationales.map((item) => (
            <RationalePanel 
              key={item.id} 
              item={item} 
              isSelected={submittedAnswer === item.id} 
              onInteract={() => handleRationaleView(item.id)}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

function RationalePanel({ item, isSelected, onInteract }) {
  const [expanded, setExpanded] = useState(isSelected || item.isCorrect);

  return (
    <div className={`border rounded-xl overflow-hidden transition-colors ${
      isSelected ? 'bg-[#1a0f0f] border-white/20' : 'bg-black/20 border-white/5'
    }`}>
      <button 
        onClick={() => {
          setExpanded(!expanded);
          if (!expanded) onInteract();
        }}
        className="w-full p-4 flex items-center justify-between text-left hover:bg-white/[0.02]"
      >
        <div className="flex items-center gap-3">
          <div className="w-6 h-6 rounded bg-black border border-white/10 flex items-center justify-center text-xs font-bold text-stone-400">
            {item.id}
          </div>
          <span className={`text-xs font-bold uppercase tracking-wider ${item.isCorrect ? 'text-green-500' : 'text-red-500/80'}`}>
            {item.isCorrect ? 'Correct' : 'Incorrect'}
          </span>
          {isSelected && <span className="text-[10px] bg-white/10 px-2 py-0.5 rounded text-stone-300 ml-2">Your Answer</span>}
        </div>
      </button>

      {expanded && (
        <div className="p-4 pt-0 border-t border-white/5 mt-2 animate-in slide-in-from-top-2">
          <p className="text-sm text-stone-300 leading-relaxed mb-4">
            {!item.isCorrect && <strong className="text-stone-500 font-normal">Not quite. Remember that... </strong>}
            {item.rationale}
          </p>
          <div className="bg-black/40 rounded-lg p-3 border border-white/5 mb-4">
            <h4 className="text-[10px] uppercase tracking-widest text-stone-500 font-bold mb-1">Real Practice</h4>
            <p className="text-xs text-stone-400 italic">{item.practice}</p>
          </div>
          
          <div className="flex items-center justify-between bg-black/60 rounded p-2 border border-white/5">
            <button 
              onClick={onInteract}
              className="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-amber-500 hover:text-amber-400"
            >
              <Play size={12} className="fill-current" /> Listen
            </button>
            <button 
              onClick={onInteract}
              className="text-[10px] uppercase tracking-widest text-stone-500 hover:text-stone-300"
            >
              Read Transcript
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

function NarrationBlock({ audioDuration, onInteract }) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [showTranscript, setShowTranscript] = useState(false);

  const handlePlay = () => {
    setIsPlaying(!isPlaying);
    if (onInteract) onInteract();
  };

  const handleTranscript = () => {
    setShowTranscript(!showTranscript);
    if (onInteract) onInteract();
  };

  return (
    <div className="bg-black/40 p-4 lg:px-8 lg:py-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
      <div className="flex items-center gap-4">
        <button 
          onClick={handlePlay}
          className="w-10 h-10 rounded-full bg-[#1a0f0f] border border-white/10 flex items-center justify-center text-amber-500 hover:bg-[#222] transition-colors shrink-0"
        >
          {isPlaying ? <Pause size={16} className="fill-current" /> : <Play size={16} className="fill-current ml-0.5" />}
        </button>
        <div>
          <div className="text-xs font-semibold text-stone-300 mb-0.5">Lesson Narration</div>
          <div className="text-[10px] text-stone-500 font-mono">{isPlaying ? '0:14' : '0:00'} / {audioDuration}</div>
        </div>
      </div>
      
      <button 
        onClick={handleTranscript}
        className={`flex items-center gap-2 text-xs font-semibold uppercase tracking-wider transition-colors px-4 py-2 rounded-xl border ${
          showTranscript ? 'bg-white/10 text-stone-200 border-white/10' : 'bg-transparent text-stone-500 hover:text-stone-300 border-transparent hover:bg-white/5'
        }`}
      >
        <FileText size={14} /> Transcript
      </button>

      {showTranscript && (
        <div className="w-full sm:hidden mt-4 p-4 bg-black/60 rounded-xl border border-white/5 text-xs text-stone-400 leading-relaxed italic animate-in fade-in">
          (Transcript text would appear here to satisfy the reading completion condition for mobile users.)
        </div>
      )}
    </div>
  );
}