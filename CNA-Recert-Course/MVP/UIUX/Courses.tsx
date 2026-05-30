import React, { useState, useEffect } from 'react';
import { 
  Play, Shield, Stethoscope, BookOpen, CheckCircle2, 
  Lock, ArrowRight, AlertCircle, ChevronRight, ArrowLeft, 
  Clock, CheckSquare, Square
} from 'lucide-react';

export default function App() {
  const [currentView, setCurrentView] = useState('dashboard'); 
  // Views: 'dashboard', 'modules', 'module0', 'module1', 'lesson'

  // Ambient deep burgundy background shared across all views
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
        <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center border border-white/20">
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
        <div className="w-8 h-8 rounded-full bg-amber-500/20 text-amber-500 flex items-center justify-center border border-amber-500/30 ml-2 md:ml-4">
          <span className="text-xs font-bold">JD</span>
        </div>
      </div>
    </header>
  );
}

// ==========================================
// FLOW 1: DASHBOARD
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
              className="w-full sm:w-auto bg-amber-500 hover:bg-amber-400 text-black font-semibold px-8 py-4 rounded-lg flex items-center justify-center gap-3 transition-all transform hover:-translate-y-0.5 shadow-[0_0_20px_rgba(245,158,11,0.15)]"
            >
              Start Module 0 <Play size={18} className="fill-current" />
            </button>
            <button 
              onClick={() => setView('modules')}
              className="w-full sm:w-auto bg-white/5 hover:bg-white/10 text-white font-medium px-8 py-4 rounded-lg transition-all border border-white/5"
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
          <div className="bg-black/40 rounded-lg p-4 border border-white/5 mb-6">
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

// ==========================================
// FLOW 2: MODULES GRID
// ==========================================
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
      
      {/* Left Sidebar */}
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

          <button className="w-full py-3 rounded-lg border border-white/10 text-white font-medium text-sm hover:bg-white/5 transition-colors">
            View certificate path
          </button>
        </div>
      </div>

      {/* Right Grid */}
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
                m.status === 'locked' 
                  ? 'bg-black/20 border-white/5 opacity-60' 
                  : 'bg-[#120a0a]/80 border-white/10 hover:border-white/20 hover:bg-[#150c0c] cursor-pointer'
              }`}
              onClick={m.status !== 'locked' ? m.action : undefined}
            >
              <div className="flex items-start justify-between mb-4">
                <div>
                  <span className={`text-xs font-bold uppercase tracking-wider mb-1 block ${m.status === 'ready' ? 'text-amber-500' : 'text-slate-500'}`}>
                    {m.id}
                  </span>
                  <span className="text-xs text-slate-500">{m.time}</span>
                </div>
                {m.status === 'completed' && <CheckCircle2 size={20} className="text-green-500" />}
                {m.status === 'locked' && <Lock size={16} className="text-slate-600" />}
              </div>
              
              <h3 className={`text-lg font-medium mb-8 ${m.status === 'locked' ? 'text-slate-400' : 'text-white'}`}>
                {m.title}
              </h3>

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

// ==========================================
// FLOW 3: MODULE 0 (ORIENTATION ONBOARDING)
// ==========================================
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
            <input type="text" defaultValue="James" className="w-full bg-black/40 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-amber-500 transition-colors" />
          </div>
          <div>
            <label className="block text-xs font-medium text-slate-400 mb-1.5 ml-1">Legal last name</label>
            <input type="text" defaultValue="Bond" className="w-full bg-black/40 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-amber-500 transition-colors" />
          </div>
          <div>
            <label className="block text-xs font-medium text-slate-400 mb-1.5 ml-1">CNA certificate number</label>
            <input type="text" defaultValue="CNA_DEMO-007" className="w-full bg-black/40 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-amber-500 transition-colors" />
          </div>
        </div>

        <div className="space-y-3 mb-10">
          {[
            "I understand the 24-hour online CE cap and that this course is partial renewal credit only.",
            "I will not enter or upload PHI about real patients, residents, or individuals anywhere in this course.",
            "I understand optional clinical support is separate and does not affect the online CE certificate."
          ].map((text, i) => (
            <div 
              key={i} 
              onClick={() => toggleAgree(i)}
              className={`flex items-start gap-4 p-4 rounded-lg border cursor-pointer transition-colors ${
                agreed[i] ? 'bg-amber-500/10 border-amber-500/30' : 'bg-black/20 border-white/5 hover:border-white/10'
              }`}
            >
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
            disabled={!allAgreed}
            className={`px-8 py-4 rounded-lg font-semibold flex items-center justify-center gap-3 transition-all w-full sm:w-auto ${
              allAgreed 
                ? 'bg-amber-500 hover:bg-amber-400 text-black transform hover:-translate-y-0.5' 
                : 'bg-white/5 text-slate-500 cursor-not-allowed'
            }`}
          >
            Continue to Module 1 <ArrowRight size={18} />
          </button>
        </div>
      </div>
    </div>
  );
}

// ==========================================
// FLOW 4: MODULE 1 OVERVIEW
// ==========================================
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
        <div className="hidden sm:flex px-4 py-2 rounded-lg border border-white/10 bg-white/5 items-center gap-2 text-xs font-medium text-slate-300">
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
              className={`flex items-center justify-between p-4 rounded-lg border transition-all ${
                i === 0 
                  ? 'bg-white/5 border-white/10 hover:bg-white/10 cursor-pointer group' 
                  : 'bg-black/20 border-white/5 opacity-60'
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
          className="bg-amber-500 hover:bg-amber-400 text-black font-semibold px-8 py-3.5 rounded-lg flex items-center justify-center gap-3 transition-all"
        >
          Start Module <Play size={16} className="fill-current" />
        </button>
      </div>
    </div>
  );
}

// ==========================================
// FLOW 5: SINGLE LESSON CARD (UNIFIED)
// ==========================================
function LessonView({ setView }) {
  const [timer, setTimer] = useState(30);

  useEffect(() => {
    const interval = setInterval(() => setTimer(p => p + 1), 1000);
    return () => clearInterval(interval);
  }, []);

  const formatTime = (secs) => `${Math.floor(secs / 60).toString().padStart(2, '0')}:${(secs % 60).toString().padStart(2, '0')}`;

  return (
    <div className="max-w-3xl mx-auto h-[85vh] flex flex-col animate-in zoom-in-95 duration-500">
      <div className="bg-[#120a0a]/95 backdrop-blur-xl border border-white/10 rounded-xl shadow-2xl flex flex-col h-full overflow-hidden">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-white/5 flex items-center justify-between bg-white/[0.02] shrink-0">
          <button onClick={() => setView('module1')} className="text-slate-400 hover:text-white transition-colors p-2 -ml-2 rounded-lg hover:bg-white/5 flex items-center gap-2 text-sm font-medium">
            <ArrowLeft size={16} /> Exit
          </button>
          <div className="flex items-center gap-2 text-xs font-medium text-slate-500">
            <span>Module 1</span><ChevronRight size={12} />
            <span className="text-slate-300">Lesson 1 of 6</span>
          </div>
          <div className="flex items-center gap-2 text-amber-500 text-xs font-mono font-medium tracking-wider">
            <div className="w-1.5 h-1.5 rounded-full bg-amber-500 animate-pulse"></div>
            {formatTime(timer)}
          </div>
        </div>

        {/* Scrollable Content */}
        <div className="p-8 md:p-12 overflow-y-auto custom-scrollbar flex-1 relative">
          <div className="max-w-2xl mx-auto space-y-12 pb-10">
            <header>
              <div className="text-[10px] uppercase tracking-widest text-slate-500 font-bold mb-3">Lesson 1</div>
              <h1 className="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-6 leading-snug">
                Why Infection Control Matters in Long-Term Care
              </h1>
              <p className="text-lg text-amber-500/90 font-medium leading-relaxed border-l-2 border-amber-500/50 pl-5 bg-gradient-to-r from-amber-500/5 to-transparent py-2">
                Learning goal: Explain why long-term care residents are at higher risk for infection and the CNA's role in prevention.
              </p>
            </header>

            <section>
              <h3 className="text-xs uppercase tracking-widest text-slate-500 font-semibold mb-4">Scenario</h3>
              <p className="text-slate-300 leading-relaxed text-lg italic bg-white/[0.02] p-6 rounded-lg border border-white/5">
                "It is a busy morning shift. You are moving between several residents — helping with breakfast, changing linens, and answering call lights. Each contact is a chance to either spread germs or stop them."
              </p>
            </section>

            <section>
              <h3 className="text-xs uppercase tracking-widest text-slate-500 font-semibold mb-4">Key Concept</h3>
              <p className="text-slate-300 leading-relaxed text-base">
                A <strong className="text-white">Healthcare-associated infection (HAI)</strong> is an infection a person gets while receiving care. LTC residents are especially vulnerable because of advanced age, chronic conditions, indwelling devices, shared living spaces, and frequent hands-on care.
              </p>
            </section>

            <section className="bg-[#1a0f0f] -mx-8 md:-mx-12 px-8 md:px-12 py-10 border-y border-red-900/20">
              <h3 className="text-xs uppercase tracking-widest text-red-200/50 font-semibold mb-6">Why it matters</h3>
              <ul className="space-y-5">
                {[
                  "Residents with weakened immune systems can become seriously ill from common germs.",
                  "You have more contact with residents than any other caregiver.",
                  "Early recognition and prevention protect every resident on the unit."
                ].map((item, i) => (
                  <li key={i} className="flex gap-4 items-start">
                    <CheckCircle2 size={20} className="text-amber-500 shrink-0 mt-0.5" />
                    <span className="text-slate-200 leading-relaxed">{item}</span>
                  </li>
                ))}
              </ul>
            </section>
          </div>
        </div>

        {/* Footer Navigation */}
        <div className="px-6 py-4 border-t border-white/5 bg-[#0a0505] flex items-center justify-between shrink-0">
          <button className="px-6 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-white/5 font-medium text-sm transition-all opacity-50 cursor-not-allowed">
            Previous
          </button>
          <div className="hidden md:flex gap-1.5">
            {[1,2,3,4,5,6].map((step) => (
               <div key={step} className={`w-8 h-1 rounded-sm ${step === 1 ? 'bg-amber-500' : 'bg-white/10'}`}></div>
            ))}
          </div>
          <button 
            onClick={() => setView('dashboard')}
            className="px-8 py-2.5 rounded-lg bg-white text-black hover:bg-slate-200 font-semibold text-sm flex items-center gap-2 transition-all"
          >
            Complete <CheckCircle2 size={16} />
          </button>
        </div>
      </div>
    </div>
  );
}
