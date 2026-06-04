import React, { useState, useEffect, useRef } from 'react';
import { 
  Play, Pause, FileText, CheckCircle2, Circle, 
  ArrowRight, ArrowLeft, Clock, ShieldAlert, Image as ImageIcon,
  AlertTriangle, Info, Check, X, Shield, Stethoscope, 
  BookOpen, Lock, AlertCircle, ChevronRight, CheckSquare, Square,
  Video, HelpCircle, Eye, RefreshCw, Award, Settings,
  Flag, LayoutDashboard, FileCheck, Database, Search, ShieldQuestion,
  StopCircle, ShieldCheck, Ban, Printer, Share2, Download, User,
  Sun, Moon, Sparkles, Send, FileCode, CheckCircle, Radio,
  Layers, Sliders, Calendar, AlertOctagon, ClipboardCheck, ListFilter, ChevronDown
} from 'lucide-react';


// Consolidated compliance-safe data arrays for CNA Program Overview
export const recertProgramModules = [
  { code: "M00", name: "Orientation and Compliance Boundaries", duration: "30 min", focus: "Review mock credentials, 24-hr cap limits, and de-identification boundaries." },
  { code: "M01", name: "Infection Control and PPE", duration: "90 min", focus: "Recall chain links, standard precautions, and isolation barrier selection." },
  { code: "M02", name: "Resident Rights, Abuse Prevention, and Boundaries", duration: "120 min", focus: "Delineate resident liberties, advocate duties, and mandated reporting schedules." },
  { code: "M03", name: "Dementia, Communication, and Respectful Care", duration: "120 min", focus: "Manage cognitive decline, respectful redirection, and behavioral de-escalation." },
  { code: "M04", name: "Mobility, Falls, and Workplace Safety", duration: "120 min", focus: "Verify safe pivot assists, lift equipment guidelines, and injury containment." },
  { code: "M05", name: "Nutrition, Skin Integrity, Vital Signs, and Observation", duration: "120 min", focus: "Track pressure injury stages, hydration minimums, and vital log reporting." },
  { code: "M06", name: "Documentation, Reporting, PHI Avoidance, and Scope", duration: "90 min", focus: "Objective note standards, HIPAA guardrails, and CNA boundaries." },
  { code: "M07", name: "Final Review, Exam/Test, Affidavit, and Certificate Status", duration: "30 min", focus: "Complete the final assessment path and planned affidavit workflow, pending approval of final wording and signature method." }
];

export const comparisonMatrix = [
  {
    criteria: "Primary Purpose",
    recert: "Renewing an existing state-issued CNA certificate through structured continuing education.",
    initial: "Earning initial eligibility to take the state competency exam for new CNAs."
  },
  {
    criteria: "Learner Audience",
    recert: "Active or recently active Certified Nursing Assistants already holding certification.",
    initial: "Uncertified individuals entering the healthcare field for the first time."
  },
  {
    criteria: "Required Hours",
    recert: "Planned 12 Theory Hours (as part of cumulative continuing education hours).",
    initial: "Full NATP hours (usually 150+ hours including mandated clinical/theory balances)."
  },
  {
    criteria: "Clinical Component",
    recert: "Optional practical skills support (non-credit, non-gating for theory credit).",
    initial: "Mandatory supervised hands-on clinical hours in an approved care facility."
  },
  {
    criteria: "Certificate Meaning",
    recert: "Attestation of continuing education units achieved under state theory cap.",
    initial: "Graduation diploma from a State-Approved training program (NATP)."
  },
  {
    criteria: "CDPH Approval Status",
    recert: "Planned asynchronous online theory CE course (Requires provider metadata & CDPH review).",
    initial: "Full training site program approval with nurse instructor site visits."
  },
  {
    criteria: "Audit Evidence Needed",
    recert: "Planned identity/profile evidence, active-time evidence, assessment records, and final learner attestation/affidavit evidence.",
    initial: "Daily physical sign-in sheets, skills checklists, and clinical logs."
  }
];

export const documentationPackage = [
  {
    group: "Executive / Program Identity",
    documents: [
      {
        title: "00_CI_ION_RECONCILIATION_EXECUTIVE_SUMMARY.md",
        purpose: "High-level course reconciliation, timeline parameters, and explicit CDPH online CE theory cap boundaries.",
        status: "Generated - pending verification",
        category: "Executive Governance"
      },
      {
        title: "14_DOCUMENTATION_STANDARD_FOR_ALL_PROGRAMS.md",
        purpose: "Establishes unified institutional documentation rules, change logs, and archive integrity expectations.",
        status: "Generated",
        category: "Program Identity"
      }
    ]
  },
  {
    group: "Export / Source / Crosswalk Evidence",
    documents: [
      {
        title: "01_CI_ION_EXPORT_INVENTORY.md",
        purpose: "Master audit inventory mapping original exported file names to staging target systems.",
        status: "Needs export verification",
        category: "Source Mapping"
      },
      {
        title: "02_EXPORT_TO_SOURCE_DOC_CROSSWALK.md",
        purpose: "Bidirectional traceability matrix connecting raw legacy documents to Moodle file uploads.",
        status: "Needs export verification",
        category: "Crosswalk Map"
      },
      {
        title: "03_EXPORT_TO_CONTENTV2_CROSSWALK.md",
        purpose: "Comprehensive mapping verifying successful migration of parsed lessons to ContentV2 files.",
        status: "Needs export verification",
        category: "Crosswalk Map"
      },
      {
        title: "04_EXPORT_TO_STANDALONE_APP_CROSSWALK.md",
        purpose: "Maps original database parameters directly into the live preview app interactive state variables.",
        status: "Needs export verification",
        category: "Staging Proof"
      },
      {
        title: "15_SPREADSHEET_URL_DOCUMENTATION_EVIDENCE_REGISTER.md",
        purpose: "Central repository log tracking direct digital URLs, sheet indices, and active shared documents.",
        status: "Incomplete - evidence missing",
        category: "Evidence Registry"
      }
    ]
  },
  {
    group: "Missing Documentation / Reconciliation Controls",
    documents: [
      {
        title: "05_MISSING_DOCUMENTATION_REGISTER.md",
        purpose: "Isolates legacy course resource gaps, missing CDPH provider metadata fields, and unresolved actions.",
        status: "Needs source repair",
        category: "Gap Analysis"
      },
      {
        title: "MISSING_DOCUMENTATION_GENERATION_AUDIT.md",
        purpose: "Audit trail validating generated program assets against legal CDPH state-approved guidelines.",
        status: "Needs compliance/legal review",
        category: "Compliance Audit"
      },
      {
        title: "CLAUDE_MISSING_DOCUMENTATION_PROMPTS.md",
        purpose: "Preserves the complete set of strict prompt heuristics used to generate course reconciliation templates.",
        status: "Generated",
        category: "Prompts Register"
      },
      {
        title: "CI_ION_Course_Reconciliation_Master_Tracker.xlsx",
        purpose: "Central tracking spreadsheet containing size metrics, topic maps, and planned active-time evidence checks.",
        status: "Needs export verification",
        category: "Master Tracking"
      }
    ]
  },
  {
    group: "Course Structure / Time / Module Evidence",
    documents: [
      {
        title: "06_MODULE_TIME_AND_STRUCTURE_RECONCILIATION.md",
        purpose: "Documents the planned 720-minute theory allocation against a 50-active-minute-per-hour evidence model.",
        status: "Needs SME review",
        category: "Time Reconciliation"
      },
      {
        title: "10_SOURCE_REPAIR_SME_COMPLIANCE_FLAGS.md",
        purpose: "Logs mandatory state content adjustments, abuse prevention hours, and specialized SME safety warnings.",
        status: "Needs SME review",
        category: "SME Audit"
      }
    ]
  },
  {
    group: "Assessment / Certificate / Completion Evidence",
    documents: [
      {
        title: "07_ASSESSMENT_AND_QUIZ_BANK_RECONCILIATION.md",
        purpose: "Validates all quiz and exam items directly against CDPH learning objectives without revealing keys.",
        status: "Needs SME review",
        category: "Assessment Validation"
      },
      {
        title: "08_CERTIFICATE_GATE_ACTIVE_TIME_AFFIDAVIT_RECONCILIATION.md",
        purpose: "Documents planned affidavit/signature-method review, active-time evidence, and name-verification gates before certificate release.",
        status: "Needs compliance/legal review",
        category: "Gate Validation"
      },
      {
        title: "11_AUDIT_PACKET_EVIDENCE_MAP.md",
        purpose: "Coordinates Moodle log variables to construct a standardized, audit-ready examiner package.",
        status: "Needs export verification",
        category: "Audit Readiness"
      },
      {
        title: "12_QA_NEGATIVE_TEST_AND_ACCEPTANCE_PLAN.md",
        purpose: "Establishes a structured test plan for checking that bypass attempts keep draft certificate access disabled.",
        status: "Generated",
        category: "Quality Assurance"
      },
      {
        title: "13_GO_NO_GO_BLOCKERS_AND_DECISIONS.md",
        purpose: "Rigorous go/no-go checklist of stakeholder requirements that must be confirmed prior to production.",
        status: "Blocked pending approval metadata",
        category: "Stakeholder Sign-off"
      }
    ]
  },
  {
    group: "Optional Clinical Support Evidence",
    documents: [
      {
        title: "09_OPTIONAL_CLINICAL_SUPPORT_SEPARATION_RECONCILIATION.md",
        purpose: "Documents the structural, visual, and credit isolation of the non-credit clinical practice workshops.",
        status: "Needs compliance/legal review",
        category: "Clinical Separation"
      }
    ]
  },
  {
    group: "Platform / Wording Audit",
    documents: [
      {
        title: "MOODLE_PLATFORM_WORDING_AUDIT.md",
        purpose: "Ensures no legacy hosted-platform wording remains. Confirms system explicitly targets Self-Hosted Moodle 4.5 LTS.",
        status: "Needs Moodle platform wording audit",
        category: "Platform Validation"
      }
    ]
  }
];

export const fallbackKnowledgeBase = {
  "What should I do next?": "According to the master blueprint, your immediate next step is to complete Module 0 (Orientation and Compliance Boundaries). This is a planned 30-minute module where you verify mock credentials, accept the 24-hour online cap limits, and agree to the de-identification safeguards. Once confirmed, Module 1 (Infection Control & PPE) will unlock sequentially.",
  "Why is my certificate locked?": "Your certificate is locked because this preview uses a planned compliance gating model. The proposed path includes identity/profile evidence, active-time evidence, module and final assessment records, and a final learner attestation/affidavit workflow pending approval of final wording and signature method. Optional clinical support is non-gating and non-credit. Note: Production certificate issuance is disabled in this preview.",
  "What does Module 1 cover?": "Module 1 covers Infection Control and PPE (Planned duration: 90 minutes). It is a required theory unit mapping: (1) The six distinct links in the chain of infection, (2) Proper standard precautions and hand hygiene active scrub durations, and (3) Clinical isolation barriers (Contact, Droplet, and Airborne) for nurse aide safety.",
  "Does Clinical Support count for clinical hours?": "No. For this project’s current compliance model, this course is designed for partial California CNA renewal CE (asynchronous online theory only). The 12-hour Clinical Support Hub is purely for optional, non-credit practical skills refresh and workplace support. It does not count toward state-mandated clinical hours.",
  "Help me study for the final exam": "The final exam is a randomized 50-question comprehensive evaluation. To study effectively, focus on: (1) Abuse recognition and reporting timelines (HSC 1337.1), (2) Infection chains and barrier protocols, (3) Dementia verbal and non-verbal communication, (4) Safe transfers and ergonomics, and (5) Scope of practice limits. Correct answer keys are locked after submission to maintain exam integrity.",
  "What does no-PHI mean?": "No-PHI is our highest priority audit safety safeguard. Protected Health Information (PHI) includes real patient names, birth dates, room numbers, chart screenshots, or facility identifiers. You must NEVER enter real resident data in practice notes, forums, or upload fields. Always use fictional examples (e.g., 'Resident A' or 'Mr. Park')."
};


export default function App() {
  const [currentView, setCurrentView] = useState('recert'); 
  const [brandingMode, setBrandingMode] = useState('dark'); 
  const [activeSubTab, setActiveSubTab] = useState('blueprint'); 
  const [riskFilter, setRiskFilter] = useState('ALL');
  
  // Nia Panel State
  const [niaActiveTab, setNiaActiveTab] = useState('chat'); // 'chat' or 'reference'
  const [niaMessages, setNiaMessages] = useState([
    {
      sender: 'nia',
      text: "Hi — I'm Nia. I answer questions using this course's content only. Ask me what to do next, what a module covers, why your certificate is locked, how to study for the final, or about CNA scope and the no-PHI rules.",
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }
  ]);
  const [userInput, setUserInput] = useState('');
  const [isNiaThinking, setIsNiaThinking] = useState(false);
  
  // Accordion Expandable States for Reference Mode
  const [expandedAccordions, setExpandedAccordions] = useState({
    whatis: true,
    canhelp: false,
    cannot: false,
    nophi: false,
    gatehelp: false,
    examstudy: false
  });

  const chatEndRef = useRef(null);

  // Auto-scroll chat window
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [niaMessages, isNiaThinking]);

  const isDark = brandingMode === 'dark';

  const toggleAccordion = (id) => {
    setExpandedAccordions(prev => ({ ...prev, [id]: !prev[id] }));
  };

  // Secure Gemini Call Logic (Frontend Safe mockup with local processing fallback)
  const callGroundedNiaAPI = async (query) => {
    // PRODUCTION SECURITY NOTE: Frontend client-side API key injection is strictly disabled.
    // Real production environments route this request through a secure serverless backend.
    const apiKey = ""; 
    
    if (!apiKey) {
      console.warn("Nia Coach: Client-side API key omitted for security. Falling back to structured local database response.");
      return null;
    }

    const systemPrompt = `
      You are Nia, the AI Student Success Coach for the CI Institute of Nursing California CNA Recertification Course.
      Answer the student's question using ONLY the facts and blueprints provided below. 
      If the question is out of scope or asks for real patient medical information, remind them of the strict no-PHI rule and redirect them to course guidelines.
      Keep answers structured, concise, professional, and supportive. Never reveal final exam answers or exact correct keys.
      
      [GUIDELINE CONSTRAINTS]
      - Course provides 12 hours of online asynchronous theory CE only.
      - Online CE is capped by California at 24 hours per renewal cycle.
      - Optional Clinical Support Hub (12 hours) is non-credit, non-gating.
      - Active-time validation is planned around a 50-active-minute-per-hour evidence model, pending validation and approval.
      - No Protected Health Information (PHI) is ever allowed.
      
      [CURRICULUM MAPPING]
      - M00: Orientation (30 min)
      - M01: Infection Control (90 min)
      - M02: Resident Rights & Abuse (120 min) - mandate 4-hour requirement
      - M03: Dementia Care & Communication (120 min)
      - M04: Mobility and Safety (120 min)
      - M05: Nutrition and Vitals (120 min)
      - M06: Documentation and Scope (90 min)
      - M07: Final Evaluation and Perjury Affidavit (30 min)
    `;

    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`;
    let delay = 1000;

    for (let attempt = 1; attempt <= 5; attempt++) {
      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{ parts: [{ text: query }] }],
            systemInstruction: { parts: [{ text: systemPrompt }] }
          })
        });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const result = await response.json();
        return result.candidates?.[0]?.content?.parts?.[0]?.text;
      } catch (error) {
        if (attempt === 5) throw error;
        await new Promise(res => setTimeout(res, delay));
        delay *= 2;
      }
    }
  };

  // Safe color mapper avoiding unsupported Tailwind classes
  const getStatusStyle = (status) => {
    switch (status) {
      case 'Generated':
      case 'Generated - pending verification':
        return 'bg-emerald-950/20 text-emerald-400 border border-emerald-800/30';
      case 'Incomplete - evidence missing':
        return 'bg-red-950/20 text-red-400 border border-red-800/30';
      case 'Needs export verification':
        return 'bg-amber-950/20 text-amber-500 border border-amber-800/30';
      case 'Needs source repair':
        return 'bg-rose-950/20 text-rose-400 border border-rose-800/30';
      case 'Needs SME review':
        return 'bg-indigo-950/20 text-indigo-400 border border-indigo-800/30';
      case 'Needs compliance/legal review':
        return 'bg-violet-950/20 text-violet-400 border border-violet-800/30';
      case 'Blocked pending approval metadata':
        return 'bg-stone-900/60 text-stone-400 border border-stone-800/40';
      case 'Needs document import':
        return 'bg-cyan-950/20 text-cyan-400 border border-cyan-800/30';
      case 'Needs Moodle platform wording audit':
        return 'bg-amber-950/30 text-amber-500 border border-amber-700/50 font-bold';
      default:
        return 'bg-stone-900 text-stone-300 border border-stone-800';
    }
  };


  return (
    <div className={`min-h-screen font-sans flex flex-col relative overflow-x-hidden transition-colors duration-300 ${
      isDark ? 'bg-[#080404] text-stone-100' : 'bg-[#F8F9FA] text-[#212529]'
    }`}>
      
      {/* Background radial gradient glow for premium look */}
      {isDark && (
        <div className="fixed inset-0 pointer-events-none bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#4a0d0d]/10 via-[#080404] to-[#080404] z-0"></div>
      )}

      {/* Navigation Header */}
      <header className={`px-6 py-4 border-b relative z-40 flex items-center justify-between shrink-0 no-print transition-colors ${
        isDark ? 'border-stone-800/60 bg-[#0c0606]/85 backdrop-blur-md' : 'border-stone-200 bg-white shadow-sm'
      }`}>
        <div className="flex items-center gap-3 cursor-pointer" onClick={() => setCurrentView('recert')}>
          <div className={`w-8 h-8 rounded flex items-center justify-center border ${
            isDark ? 'bg-[#1f0909] border-[#5c1111]' : 'bg-[#8B1515] border-[#8B1515]/20'
          }`}>
            <span className="text-stone-100 font-bold text-xs tracking-tight">CI</span>
          </div>
          <div>
            <span className={`font-semibold tracking-wider text-sm block ${isDark ? 'text-stone-200' : 'text-[#212529]'}`}>CI INSTITUTE OF NURSING</span>
            <span className="text-[9px] text-stone-500 block -mt-1 font-mono uppercase tracking-widest">CNA Master Blueprint</span>
          </div>
        </div>
        
        <div className="flex items-center gap-1 sm:gap-4 text-xs sm:text-sm font-medium">
          {[
            { id: 'dashboard', label: 'Dashboard' },
            { id: 'modules', label: 'CE Modules' },
            { id: 'certificate', label: 'Certificate Gate' },
            { id: 'clinical', label: 'Clinical Hub' },
            { id: 'recert', label: 'Program Overview' }
          ].map(item => {
            const isActive = currentView === item.id;
            return (
              <button 
                key={item.id}
                onClick={() => {
                  setCurrentView(item.id);
                  window.scrollTo({ top: 0, behavior: 'smooth' });
                }}
                className={`transition-all px-3 py-1.5 rounded-lg border uppercase tracking-wider text-[11px] font-semibold ${
                  isActive 
                    ? isDark ? 'text-amber-500 bg-[#1f0d0d] border-[#5c1111]' : 'text-[#8B1515] bg-[#8B1515]/5 border-[#8B1515]/25 font-bold'
                    : isDark ? 'border-transparent text-stone-400 hover:text-stone-200 hover:bg-stone-900/40' : 'border-transparent text-stone-600 hover:text-[#212529] hover:bg-stone-100'
                }`}
              >
                {item.label}
              </button>
            );
          })}
          
          {/* Top Bar Theme Toggle */}
          <button 
            onClick={() => setBrandingMode(isDark ? 'normal' : 'dark')}
            className={`p-1.5 rounded-lg border transition-all ${
              isDark ? 'border-stone-800 hover:bg-stone-900 text-amber-500' : 'border-stone-200 hover:bg-stone-100 text-[#8B1515]'
            }`}
            title={isDark ? "Switch to Normal Branding" : "Switch to Dark Mode"}
          >
            {isDark ? <Sun size={15} /> : <Moon size={15} />}
          </button>
        </div>
      </header>

      {/* Main Split Interface Area */}
      <div className="flex-1 flex flex-col lg:flex-row relative z-10 w-full max-w-7xl mx-auto p-4 md:p-6 gap-6">
        
        {/* LEFT COLUMN: Main App & Blueprint Tabs */}
        <main className="flex-1 min-w-0 space-y-6">
          
          {/* Gated Empty Tab Placeholder */}
          {currentView !== 'recert' && (
            <div className={`rounded-xl p-8 md:p-12 text-center max-w-2xl mx-auto border transition-colors ${
              isDark ? 'bg-[#120909]/95 border-stone-800' : 'bg-white border-stone-200 shadow-sm'
            }`}>
              <div className={`w-16 h-16 rounded-full mx-auto flex items-center justify-center border mb-6 ${
                isDark ? 'bg-[#1a0f0f] border-amber-500/20 text-amber-500' : 'bg-stone-100 border-stone-200 text-[#8B1515]'
              }`}>
                <Lock size={28} />
              </div>
              <h2 className={`text-2xl font-bold tracking-tight mb-4 ${isDark ? 'text-stone-200' : 'text-stone-800'}`}>
                {currentView.toUpperCase()} Portal Locked
              </h2>
              <p className={`text-xs md:text-sm leading-relaxed mb-6 ${isDark ? 'text-stone-400' : 'text-stone-500'}`}>
                Under current Moodle deployment staging phases for CI Institute, live database records are simulated within the staging engine. All compliance-hardened metrics are available for immediate review under the <strong className="underline text-[#8B1515] dark:text-amber-500 cursor-pointer" onClick={() => setCurrentView('recert')}>Program Overview</strong> tab.
              </p>
              
              <div className={`p-4 rounded-lg border text-left text-xs mb-6 ${
                isDark ? 'bg-[#080404] border-stone-900 text-stone-400' : 'bg-[#F8F9FA] border-stone-200 text-stone-600'
              }`}>
                <span className="font-semibold block mb-1 uppercase tracking-wider text-[10px] text-amber-500 font-mono">Staging Mode Auditing Instructions:</span>
                Open the <strong className="underline cursor-pointer text-[#8B1515] dark:text-amber-500" onClick={() => setCurrentView('recert')}>Program Overview</strong> where the comprehensive state matrices, timetables, and Moodle templates have been fully populated.
              </div>

              <button
                onClick={() => setCurrentView('recert')}
                className={`w-full py-2.5 rounded font-bold text-xs uppercase tracking-wider transition-all border ${
                  isDark ? 'bg-[#5c1111] hover:bg-[#781616] text-stone-100 border-[#8a1d1d]' : 'bg-[#8B1515] hover:bg-[#a61a1a] text-white border-[#8B1515]'
                }`}
              >
                Go to Master Program Overview
              </button>
            </div>
          )}

          {/* STANDALONE AUDITING CENTER: PROGRAM OVERVIEW VIEW */}
          {currentView === 'recert' && (
            <div className="space-y-6">
              
              {/* Inner Sub-Navigation (Reports 1 to 6) */}
              <div className="border-b border-stone-800/80 flex flex-wrap gap-1">
                {[
                  { id: 'blueprint', label: '1. Master Blueprint', icon: <Sliders size={14} /> },
                  { id: 'compliance', label: '2. Compliance Matrix', icon: <Shield size={14} /> },
                  { id: 'architecture', label: '3. Technical Spec', icon: <Database size={14} /> },
                  { id: 'instructional', label: '4. Instructional Map', icon: <BookOpen size={14} /> },
                  { id: 'operations', label: '5. Build & Ops', icon: <ClipboardCheck size={14} /> },
                  { id: 'evidencePackage', label: '6. Docs & Evidence', icon: <FileCode size={14} /> }
                ].map(tab => (
                  <button
                    key={tab.id}
                    onClick={() => setActiveSubTab(tab.id)}
                    className={`flex items-center gap-2 px-4 py-3 text-xs uppercase tracking-wider font-bold transition-all border-b-2 -mb-[2px] ${
                      activeSubTab === tab.id
                        ? isDark ? 'border-amber-500 text-amber-500 bg-[#140606]' : 'border-[#8B1515] text-[#8B1515] bg-stone-100'
                        : 'border-transparent text-stone-500 hover:text-stone-300'
                    }`}
                  >
                    {tab.icon}
                    {tab.label}
                  </button>
                ))}
              </div>

              {/* -------------------------------------------------------------
                  REPORT 1: UNIFIED MASTER BLUEPRINT
                  ------------------------------------------------------------- */}
              {activeSubTab === 'blueprint' && (
                <div className="space-y-6 animate-in fade-in duration-300">
                  
                  {/* Executive Strategy Cards */}
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className={`p-5 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                      <h3 className="text-sm font-bold text-amber-500 uppercase tracking-widest mb-3 flex items-center gap-2">
                        <Sliders size={15} /> Executive Summary
                      </h3>
                      <p className={`text-xs leading-relaxed ${isDark ? 'text-stone-400' : 'text-stone-600'}`}>
                        Our design establishes a separate structural pathway between continuing education theory (planned for sequential module gating and identity constraints) and non-credit clinical practice workshops.
                      </p>
                    </div>

                    <div className={`p-5 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                      <h3 className="text-sm font-bold text-[#8B1515] dark:text-amber-500 uppercase tracking-widest mb-3 flex items-center gap-2">
                        <FileCode size={15} /> Controlling Guidelines
                      </h3>
                      <p className={`text-xs leading-relaxed ${isDark ? 'text-stone-400' : 'text-stone-600'}`}>
                        Designed for partial California CNA renewal CE. Built around a planned 12-hour asynchronous timeline to align with California's 24-hour online continuing education limit.
                      </p>
                    </div>
                  </div>

                  {/* Classification Comparison Matrix */}
                  <div className={`p-6 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                    <h3 className="text-base font-bold mb-4 flex items-center gap-2">
                      <Layers size={18} /> Course Classification Comparison Matrix
                    </h3>
                    <div className="overflow-x-auto">
                      <table className="w-full text-xs text-left border-collapse">
                        <thead>
                          <tr className="border-b border-stone-800 text-stone-400 uppercase tracking-widest text-[10px]">
                            <th className="py-3 px-4 font-bold w-1/4">Criteria Dimension</th>
                            <th className="py-3 px-4 font-bold text-emerald-400 bg-emerald-950/10 w-3/8">CNA Recertification (CE Program)</th>
                            <th className="py-3 px-4 font-bold text-red-400 bg-red-950/5 w-3/8">Not This Course: Initial Certification / NATP</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-stone-800/50 text-stone-300">
                          {comparisonMatrix.map((row, i) => (
                            <tr key={i} className="hover:bg-stone-900/5">
                              <td className="py-3 px-4 font-bold uppercase tracking-wider text-[9px] text-stone-400 font-mono">{row.criteria}</td>
                              <td className="py-3.5 px-4 text-stone-300 bg-emerald-950/5 leading-relaxed">{row.recert}</td>
                              <td className="py-3.5 px-4 text-stone-400 bg-red-950/5 leading-relaxed italic">{row.initial}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>

                  {/* Modules Table */}
                  <div className={`p-6 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                    <h3 className="text-base font-bold mb-4 flex items-center gap-2">
                      <Clock size={18} /> Curriculum Module Time Allocation
                    </h3>
                    <div className="overflow-x-auto">
                      <table className="w-full text-xs text-left border-collapse">
                        <thead>
                          <tr className="border-b border-stone-800 text-stone-400 uppercase tracking-widest text-[10px]">
                            <th className="py-3 px-4 font-bold">Module Code</th>
                            <th className="py-3 px-4 font-bold">Topic Name</th>
                            <th className="py-3 px-4 font-bold">Planned Duration</th>
                            <th className="py-3 px-4 font-bold">Auditing Focus</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-stone-800/50 text-stone-300">
                          {recertProgramModules.map((mod, i) => (
                            <tr key={i} className="hover:bg-stone-900/5">
                              <td className="py-3 px-4 font-mono font-bold text-amber-500">{mod.code}</td>
                              <td className="py-3 px-4 font-semibold text-stone-200">{mod.name}</td>
                              <td className="py-3 px-4 font-mono">{mod.duration}</td>
                              <td className="py-3 px-4 text-stone-400 italic">{mod.focus}</td>
                            </tr>
                          ))}
                          <tr className="bg-stone-900/40 font-bold border-t border-stone-800">
                            <td className="py-4 px-4 font-mono text-amber-500 text-sm">TOTAL</td>
                            <td className="py-4 px-4 text-sm text-stone-200">8 Modules Planned Pathway</td>
                            <td className="py-4 px-4 font-mono text-sm text-stone-200">720 min / 12 hrs</td>
                            <td className="py-4 px-4 text-stone-500 italic text-[10px] font-mono">Planned California Theory Cap Alignment</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>

                </div>
              )}

              {/* -------------------------------------------------------------
                  REPORT 2: REGULATORY & COMPLIANCE FOUNDATION
                  ------------------------------------------------------------- */}
              {activeSubTab === 'compliance' && (
                <div className="space-y-6 animate-in fade-in duration-300">
                  
                  {/* Verified California Renewal Criteria */}
                  <div className={`p-6 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                    <h3 className="text-base font-bold mb-4 flex items-center gap-2">
                      <Shield size={18} className="text-emerald-500" /> Verified California Renewal Criteria
                    </h3>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                      <div className="p-4 rounded-lg bg-stone-900/85 border border-stone-800 space-y-1">
                        <span className="font-bold text-amber-500 uppercase tracking-widest text-[9px] font-mono">HSC 1337.6 Cycle</span>
                        <p className="text-stone-300">Certificates renew every 2 years. Gated on 48 cumulative CE hours, with a minimum of 12 hours completed in each certification year.</p>
                      </div>
                      <div className="p-4 rounded-lg bg-stone-900/85 border border-stone-800 space-y-1">
                        <span className="font-bold text-emerald-500 uppercase tracking-widest text-[9px] font-mono">24-Hour Online CE Cap</span>
                        <p className="text-stone-300">Only 24 of the total 48 hours may be acquired via online, computer-based training. Learners are reminded of this limit at registration.</p>
                      </div>
                      <div className="p-4 rounded-lg bg-stone-900/85 border border-stone-800 space-y-1">
                        <span className="font-bold text-[#8B1515] dark:text-rose-400 uppercase tracking-widest text-[9px] font-mono">Compensated Services</span>
                        <p className="text-stone-300">CNA must perform supervised compensated nursing services in a healthcare facility within the renewal period to maintain licensing.</p>
                      </div>
                    </div>
                  </div>

                  {/* Open Auditing Questions */}
                  <div className={`p-6 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                    <h3 className="text-base font-bold mb-4 flex items-center gap-2">
                      <ShieldAlert size={18} className="text-[#8B1515]" /> Critical Open Compliance & Auditing Questions (Requires verification)
                    </h3>
                    <ul className="space-y-3 text-xs leading-relaxed">
                      {[
                        "Is CI Institute officially registered as an approved CDPH Online CNA CE Provider holding an active, valid NAC#?",
                        "Has CDPH formally reviewed and approved the specific 12 course hours, titles, objectives, outlines, and exams?",
                        "Will CDPH allow electronic signatures for final affidavits, or must a wet-signature backup path be established?",
                        "What exact certificate language has been authorized regarding Online-Course indicators and the 4-year retention clause?"
                      ].map((q, idx) => (
                        <li key={idx} className="flex gap-3 items-start text-stone-300">
                          <span className="text-[#8B1515] dark:text-rose-500 font-extrabold font-mono text-sm leading-none">{idx+1}.</span>
                          <span>{q}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

                  {/* State Gate Matrix */}
                  <div className={`p-6 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800/60' : 'bg-white border-stone-200'}`}>
                    <h3 className="text-base font-bold mb-4 flex items-center gap-2">
                      <ClipboardCheck size={18} /> State Verification & Certification Gate Matrix (Planned model)
                    </h3>
                    <div className="overflow-x-auto">
                      <table className="w-full text-xs text-left border-collapse">
                        <thead>
                          <tr className="border-b border-stone-800 text-stone-400 uppercase tracking-widest text-[10px]">
                            <th className="py-3 px-4 font-bold">Verification Item</th>
                            <th className="py-3 px-4 font-bold">Audit Purpose</th>
                            <th className="py-3 px-4 font-bold">Evidence Required</th>
                            <th className="py-3 px-4 font-bold">Compliance Status</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-stone-800/50 text-stone-300">
                          {[
                            { item: "CDPH Online CE Provider Status", purpose: "Prerequisite to legally issue online renewal credits", evidence: "Department-issued approval letter & unique NAC#", status: "PENDING LOGS" },
                            { item: "Signature Method Decision", purpose: "Confirms whether electronic or wet-signature affidavit wording and method may be used", evidence: "Written CDPH/TPRU legal policy guidelines", status: "STAGING MODEL" },
                            { item: "Simulation Exclusion Enforcement", purpose: "Prevents virtual scenarios from claiming clinical CE hours", evidence: "Moodle configuration matrix proving non-gating", status: "DESIGN LOCK" },
                            { item: "4-Year Record Retention Verification", purpose: "CDPH provider compliance requirement for all learner logs", evidence: "Database backup schedules & automated backup logs", status: "DESIGN LOCK" }
                          ].map((row, i) => (
                            <tr key={i} className="hover:bg-stone-900/5">
                              <td className="py-3 px-4 font-bold text-stone-200">{row.item}</td>
                              <td className="py-3 px-4 text-stone-400">{row.purpose}</td>
                              <td className="py-3 px-4 font-mono text-[11px] text-amber-500">{row.evidence}</td>
                              <td className="py-3 px-4">
                                <span className={`px-2 py-0.5 rounded text-[9px] font-bold ${
                                  row.status === 'DESIGN LOCK' ? 'bg-emerald-950/40 text-emerald-400 border border-emerald-800/30' : 'bg-amber-950/40 text-amber-500 border border-amber-800/30'
                                }`}>{row.status}</span>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>

                </div>
              )}

              {/* -------------------------------------------------------------
                  REPORT 3: TECHNICAL ARCHITECTURE & MOODLE SPEC
                  ------------------------------------------------------------- */}
              {activeSubTab === 'architecture' && (
                <div className="space-y-6 animate-in fade-in duration-300">
                  
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div className={`p-5 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                      <h3 className="text-sm font-bold text-amber-500 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <Database size={15} /> Self-Hosted Moodle 4.5 LTS target
                      </h3>
                      <p className="text-xs text-stone-400 leading-relaxed">
                        Configured for local hosting, targeting the stable Moodle 4.5 LTS branch with security support extending through October 2027.
                      </p>
                    </div>

                    <div className={`p-5 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                      <h3 className="text-sm font-bold text-emerald-500 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <Clock size={15} /> Active-time Validation Plan
                      </h3>
                      <p className="text-xs text-stone-400 leading-relaxed">
                        Planned integration of `mod_timestat` tracking to assist log checks while excluding idle browser states.
                      </p>
                    </div>

                    <div className={`p-5 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                      <h3 className="text-sm font-bold text-[#8B1515] dark:text-rose-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <Lock size={15} /> Planned Perjury Affidavit
                      </h3>
                      <p className="text-xs text-stone-400 leading-relaxed">
                        Planned gate model intended to keep draft certificate rendering disabled until the approved attestation/affidavit path is complete.
                      </p>
                    </div>
                  </div>

                  {/* Core Moodle Configuration Matrix */}
                  <div className={`p-6 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800/60' : 'bg-white border-stone-200'}`}>
                    <h3 className="text-base font-bold mb-4 flex items-center gap-2">
                      <Settings size={18} /> Core Moodle Configuration Matrix
                    </h3>
                    <div className="overflow-x-auto">
                      <table className="w-full text-xs text-left border-collapse">
                        <thead>
                          <tr className="border-b border-stone-800 text-stone-400 uppercase tracking-widest text-[10px]">
                            <th className="py-3 px-4 font-bold">Moodle Setting</th>
                            <th className="py-3 px-4 font-bold">Recommended Configuration</th>
                            <th className="py-3 px-4 font-bold">Planned Audit Value</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-stone-800/50 text-stone-300">
                          {[
                            { tool: "Topics Format", config: "Separate online theory modules into distinct one-hour segments.", value: "Supports structured curriculum review." },
                            { tool: "Activity Completion", config: "Lock lesson paths behind complete markers; require minimum interaction score.", value: "Demonstrates lesson milestone intent." },
                            { tool: "Restrict Access", config: "Gate successive modules until previous module exams achieve passing grades.", value: "Planned to enforce sequential progression." },
                            { tool: "Custom SQL Reports", config: "Configure SQL queries to compile progress records into instant PDF logs.", value: "Supports rapid state compliance review." }
                          ].map((row, i) => (
                            <tr key={i} className="hover:bg-stone-900/5">
                              <td className="py-3 px-4 font-mono font-bold text-amber-500">{row.tool}</td>
                              <td className="py-3 px-4 font-semibold text-stone-200">{row.config}</td>
                              <td className="py-3 px-4 text-stone-400 italic">{row.value}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>

                </div>
              )}

              {/* -------------------------------------------------------------
                  REPORT 4: INSTRUCTIONAL DESIGN BLUEPRINT
                  ------------------------------------------------------------- */}
              {activeSubTab === 'instructional' && (
                <div className="space-y-6 animate-in fade-in duration-300">
                  
                  {/* Microlearning Strategy Cards */}
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className={`p-5 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                      <h3 className="text-sm font-bold text-emerald-500 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <BookOpen size={15} /> Microlearning System
                      </h3>
                      <p className="text-xs text-stone-400 leading-relaxed">
                        Design modules into manageable 15-30 minute active sessions. Lead with a short, practical clinical scenario rather than dry, abstract lecture texts.
                      </p>
                    </div>

                    <div className={`p-5 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'}`}>
                      <h3 className="text-sm font-bold text-amber-500 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <HelpCircle size={15} /> Grounded Formative Checks
                      </h3>
                      <p className="text-xs text-stone-400 leading-relaxed">
                        Every module is planned with an interactive feedback quiz. Correct answers are not highlighted post-exam so the assessment path supports review integrity.
                      </p>
                    </div>
                  </div>

                  {/* 12-Hour Theory Course Map */}
                  <div className={`p-6 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800/60' : 'bg-white border-[#DEE2E6]'}`}>
                    <h3 className="text-base font-bold mb-4 flex items-center gap-2">
                      <Layers size={18} /> Curriculum & Theory Course Map (Module 0 to Module 7)
                    </h3>
                    <div className="overflow-x-auto">
                      <table className="w-full text-xs text-left border-collapse">
                        <thead>
                          <tr className="border-b border-stone-800 text-stone-400 uppercase tracking-widest text-[10px]">
                            <th className="py-3 px-4 font-bold">Module Topic & Code</th>
                            <th className="py-3 px-4 font-bold">Hour Value</th>
                            <th className="py-3 px-4 font-bold">Planned Auditing Focus</th>
                            <th className="py-3 px-4 font-bold">Proposed Threshold</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-stone-800/50 text-stone-300">
                          {[
                            { code: "M00 Orientation", hours: "0.5 hr", obj: "Explain partial-credit bounds, online cap restrictions, and privacy rules.", pass: "100% attestation" },
                            { code: "M01 Infection Control", hours: "1.5 hrs", obj: "Select standard precautions and isolation barriers based on pathogen vectors.", pass: "Min 80% score" },
                            { code: "M02 Resident Rights", hours: "2.0 hrs", obj: "Acknowledge legal rights and mandates regarding abuse reporting timelines.", pass: "Min 80% score" },
                            { code: "M03 Dementia & Care", hours: "2.0 hrs", obj: "Demonstrate person-centered de-escalation for cognitively anxious residents.", pass: "Min 80% score" },
                            { code: "M04 Mobility Safety", hours: "2.0 hrs", obj: "Identify fall risk indicators and safe body mechanics during transfers.", pass: "Min 80% score" },
                            { code: "M05 Nutrition & Observation", hours: "2.0 hrs", obj: "Evaluate nutrition risk and skin status reporting triggers.", pass: "Min 80% score" },
                            { code: "M06 Scope & Documentation", hours: "1.5 hrs", obj: "Write objective, de-identified shift reports adhering to CNA scope.", pass: "Min 80% score" },
                            { code: "M07 Evaluation", hours: "0.5 hr", obj: "Evaluate entire curriculum mastery before the planned attestation/affidavit workflow.", pass: "Min 80% + pending attestation path" }
                          ].map((row, i) => (
                            <tr key={i} className="hover:bg-stone-900/5">
                              <td className="py-3 px-4 font-bold text-stone-200">{row.code}</td>
                              <td className="py-3 px-4 font-mono text-amber-500">{row.hours}</td>
                              <td className="py-3 px-4 text-stone-400 leading-relaxed">{row.obj}</td>
                              <td className="py-3 px-4 text-stone-300 font-bold">{row.pass}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>

                </div>
              )}

              {/* -------------------------------------------------------------
                  REPORT 5: BUILD, OPERATIONS & RISKS
                  ------------------------------------------------------------- */}
              {activeSubTab === 'operations' && (
                <div className="space-y-6 animate-in fade-in duration-300">
                  
                  {/* Risks & Mitigation Selector Matrix */}
                  <div className={`p-6 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800/60' : 'bg-white border-[#DEE2E6]'}`}>
                    <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-6">
                      <div>
                        <h3 className="text-base font-bold flex items-center gap-2">
                          <AlertTriangle size={18} className="text-amber-500" /> Compliance & Technical Risk Register
                        </h3>
                        <p className="text-xs text-stone-400 mt-1">Audit mitigating strategies for core recertification operational risks.</p>
                      </div>
                      
                      <div className="flex items-center gap-2 text-xs">
                        <span className="text-stone-500 uppercase font-bold font-mono text-[10px]">Filter Impact:</span>
                        <div className="flex rounded-lg border border-stone-800 bg-[#080404] p-1">
                          {['ALL', 'HIGH', 'MEDIUM'].map(lvl => (
                            <button
                              key={lvl}
                              onClick={() => setRiskFilter(lvl)}
                              className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase transition-all ${
                                riskFilter === lvl ? 'bg-amber-50 text-black' : 'text-stone-400 hover:text-stone-200'
                              }`}
                            >
                              {lvl}
                            </button>
                          ))}
                        </div>
                      </div>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {[
                        { risk: "Unapproved Online CE Issuance", impact: "HIGH", detail: "Provider or course lacks active CDPH NAC# authorization.", mitigate: "Planned programmatic hold keeping production certificate issuance disabled until registrar inputs valid CDPH credentials." },
                        { risk: "Learner Exceeds 24-hr Online Cap", impact: "HIGH", detail: "CNA renews using more online theory hours than permitted.", mitigate: "Display permanent renewal-limit warnings; mandate online hours attestation check prior to final enrollment." },
                        { risk: "Active Time Tracking Bypass", impact: "HIGH", detail: "Learner bypasses module pages straight to quiz via tab tricks.", mitigate: "Planned configuration of sequential complete gates; enforce minimum Timestat active browser duration conditions before unlocking tests." },
                        { risk: "Accidental PHI Entry", impact: "MEDIUM", detail: "Learner writes real clinical names within practice notes.", mitigate: "Deploy strict validation regex; require 'No-PHI' checkboxes; deploy manual administrative review check on support uploads." },
                        { risk: "Preceptor Access Leakage", impact: "MEDIUM", detail: "Clinical evaluators accidentally gain course template rights.", mitigate: "Configure custom least-privilege roles; isolate clinical support logs from main database administrators." }
                      ]
                      .filter(r => riskFilter === 'ALL' || r.impact === riskFilter)
                      .map((r, idx) => (
                        <div key={idx} className="p-4 rounded-lg bg-stone-950/80 border border-stone-800 flex flex-col justify-between font-sans">
                          <div>
                            <div className="flex items-center justify-between mb-2">
                              <span className="text-[10px] font-mono font-bold text-stone-500">RISK #{idx+1}</span>
                              <span className={`px-2 py-0.5 rounded text-[8px] font-extrabold uppercase ${
                                r.impact === 'HIGH' ? 'bg-red-950/20 text-red-500 border border-red-800/30' : 'bg-amber-950/40 text-amber-500 border border-amber-800/30'
                              }`}>{r.impact} IMPACT</span>
                            </div>
                            <h4 className="text-xs font-bold text-stone-200 uppercase tracking-wider">{r.risk}</h4>
                            <p className="text-[11px] text-stone-400 leading-relaxed mt-1">{r.detail}</p>
                          </div>
                          <div className="mt-4 pt-3 border-t border-stone-900">
                            <span className="text-[10px] uppercase font-mono font-bold text-amber-500 block mb-0.5">Mitigation Protocol:</span>
                            <p className="text-[11px] text-stone-500 leading-relaxed italic">{r.mitigate}</p>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Operational Action Plan */}
                  <div className={`p-6 rounded-xl border ${isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-[#DEE2E6]'}`}>
                    <h3 className="text-base font-bold mb-6 flex items-center gap-2">
                      <Clock size={18} /> First 30-Day Operational Action Plan
                    </h3>
                    <div className="relative pl-6 border-l border-stone-800 space-y-6">
                      {[
                        { days: "Days 1-3", title: "Compliance Core Lock", desc: "Verify CDPH status requirements, draft certificate criteria, and perjury affidavit placeholder checks." },
                        { days: "Days 4-7", title: "Technical Environment Audit", desc: "Build mock database frames, establish local cron checks, and configure initial Bootstrap layout maps." },
                        { days: "Days 8-14", title: "Planned Content Conversion", desc: "Convert source-reviewed theory references into static Moodle-native layouts. Draft hand hygiene scenario loops." },
                        { days: "Days 15-20", title: "Clinical Support Hub Setup", desc: "Draft scheduling parameters and practice documentation pages. Integrate PHI checks across any upload areas." }
                      ].map((step, idx) => (
                        <div key={idx} className="relative font-sans">
                          <span className="absolute -left-[31px] top-0.5 w-4 h-4 rounded-full bg-stone-950 border-2 border-amber-500 flex items-center justify-center text-[8px] text-amber-500 font-bold font-mono">
                            {idx+1}
                          </span>
                          <span className="text-[10px] uppercase font-bold text-amber-500 font-mono block">{step.days} • {step.title}</span>
                          <p className="text-xs text-stone-400 mt-1 max-w-3xl leading-relaxed">{step.desc}</p>
                        </div>
                      ))}
                    </div>
                  </div>

                </div>
              )}

              {/* -------------------------------------------------------------
                  REPORT 6: DOCUMENTATION & EVIDENCE PACKAGE
                  ------------------------------------------------------------- */}
              {activeSubTab === 'evidencePackage' && (
                <div className="space-y-6 animate-in fade-in duration-300">
                  
                  {/* Explanatory Copy block */}
                  <div className={`p-6 rounded-xl leading-relaxed border ${
                    isDark ? 'bg-stone-900 border-stone-800 text-stone-300' : 'bg-amber-50/50 text-stone-800'
                  }`}>
                    <div className="flex gap-3 items-start">
                      <ShieldAlert size={20} className="text-amber-500 shrink-0 mt-0.5" />
                      <div className="space-y-2">
                        <p className="text-xs font-semibold leading-relaxed">
                          “This documentation package supports the CNA Recertification / renewal CE course direction. It is designed to preserve course identity, source mapping, module timing, assessment controls, certificate gate evidence, optional clinical separation, and audit readiness. It does not convert this course into an entry-level CNA training or eligibility pathway.”
                        </p>
                        <p className="text-[11px] text-stone-500 italic">
                          “Some reconciliation documents may be marked incomplete where local export evidence, spreadsheet URL evidence, approval metadata, active-time validation, or source access is still missing.”
                        </p>
                      </div>
                    </div>
                  </div>

                  {/* Warning: Platform Wording Audit Banner */}
                  <div className={`p-4 rounded-xl flex gap-3 items-center border ${
                    isDark ? 'bg-amber-950/20 border-amber-800/40 text-amber-400' : 'bg-amber-50'
                  }`}>
                    <AlertCircle size={18} className="text-amber-500 shrink-0" />
                    <span className="text-[11px] leading-relaxed">
                      <strong>Wording Guardrail Triggered:</strong> Needs wording audit: replace legacy hosted-platform wording with <strong>Self-Hosted Moodle 4.5 LTS target</strong> unless clearly historical.
                    </span>
                  </div>

                  {/* Polished Grid of Document Accordion Panels */}
                  <div className="space-y-6">
                    {documentationPackage.map((group, groupIdx) => (
                      <div 
                        key={groupIdx} 
                        className={`p-6 rounded-xl border ${
                          isDark ? 'bg-[#120909] border-stone-800' : 'bg-white border-stone-200'
                        }`}
                      >
                        <h3 className="text-xs uppercase font-extrabold tracking-widest text-amber-500 mb-4 flex items-center gap-2">
                          <FileCode size={14} />
                          {group.group}
                        </h3>
                        
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                          {group.documents.map((doc, docIdx) => (
                            <div 
                              key={docIdx} 
                              className={`p-4 rounded-lg flex flex-col justify-between space-y-3 transition-all border ${
                                isDark ? 'bg-[#080404]/80 border-stone-900' : 'bg-stone-50 border-stone-200'
                              }`}
                            >
                              <div className="space-y-1">
                                <div className="flex flex-wrap items-center justify-between gap-2">
                                  <span className="text-[10px] uppercase font-bold tracking-wider text-stone-500 font-mono">
                                    {doc.category}
                                  </span>
                                  <span className={`px-2 py-0.5 rounded text-[8px] font-bold uppercase ${getStatusStyle(doc.status)}`}>
                                    {doc.status}
                                  </span>
                                </div>
                                <h4 className="text-xs font-bold text-stone-200 break-all font-mono leading-tight">
                                  {doc.title}
                                </h4>
                              </div>
                              
                              <p className="text-[11px] text-stone-400 leading-relaxed">
                                {doc.purpose}
                              </p>
                            </div>
                          ))}
                        </div>
                      </div>
                    ))}
                  </div>

                </div>
              )}

              {/* Stakeholder Summary Footer */}
              <div className="bg-amber-950/15 p-6 rounded-xl text-xs space-y-2 border border-amber-900/30">
                <h4 className="font-bold text-amber-500 uppercase tracking-widest text-[10px] font-mono">Executive Summary</h4>
                <p className="text-stone-400 leading-relaxed">
                  This blueprint confirms the active implementation design: a CNA Recertification / renewal CE course, not an entry-level CNA training or eligibility pathway. The course is designed as a 12-hour online theory package with optional non-credit clinical support and audit-ready documentation guardrails.
                </p>
              </div>

            </div>
          )}

        </main>

        {/* RIGHT COLUMN: NIA CHAT / ADVISOR PANEL */}
        <aside className={`w-full lg:w-[350px] shrink-0 rounded-2xl flex flex-col transition-all h-[calc(100vh-140px)] sticky top-6 overflow-hidden border ${
          isDark 
            ? 'bg-[#120909]/95 border-stone-800 shadow-[0_25px_60px_rgba(0,0,0,0.85)]' 
            : 'bg-white border-stone-200 shadow-[0_15px_40px_rgba(0,0,0,0.06)]'
        }`}>
          
          {/* Header Block exactly duplicated from screenshots */}
          <div className={`p-4 border-b space-y-3 shrink-0 ${isDark ? 'border-stone-800 bg-transparent' : 'border-stone-200'}`}>
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-full bg-red-950 border border-red-500/30 flex items-center justify-center font-bold text-rose-500 text-lg shadow-inner">
                N
              </div>
              <div className="min-w-0">
                <h2 className={`font-semibold tracking-tight text-sm truncate ${isDark ? 'text-stone-100' : 'text-[#212529]'}`}>
                  Nia Student Success Coach
                </h2>
                <p className="text-[10px] text-stone-500 truncate -mt-0.5 font-sans">
                  Course Guidance • CNA Recertification • Grounded
                </p>
              </div>
            </div>

            {/* Quick Badges row */}
            <div className="flex items-center justify-between text-[10px]">
              <div className="flex items-center gap-1.5 px-2 py-0.5 rounded bg-amber-500/10 text-amber-500 border border-amber-500/20 font-bold font-mono uppercase tracking-wider text-[8.5px]">
                <Sparkles size={9} /> Course-grounded MVP
              </div>
              <a href="#help" className="text-stone-500 hover:text-amber-500 transition-colors uppercase tracking-wider font-bold text-[9px]">
                Help Center
              </a>
            </div>

            {/* Segmented Mode Selector Switch */}
            <div className={`flex rounded-lg p-1 text-[10px] font-semibold uppercase tracking-wider ${isDark ? 'bg-stone-950' : 'bg-stone-100'}`}>
              <button 
                onClick={() => setNiaActiveTab('chat')}
                className={`flex-1 py-1 text-center rounded transition-all ${
                  niaActiveTab === 'chat' 
                    ? isDark ? 'bg-[#3b0b0b] text-amber-500' : 'bg-white text-[#8B1515] shadow-sm'
                    : 'text-stone-500 hover:text-stone-300'
                }`}
              >
                Chat Coach
              </button>
              <button 
                onClick={() => setNiaActiveTab('reference')}
                className={`flex-1 py-1 text-center rounded transition-all ${
                  niaActiveTab === 'reference' 
                    ? isDark ? 'bg-[#3b0b0b] text-amber-500' : 'bg-white text-[#8B1515] shadow-sm'
                    : 'text-stone-500 hover:text-stone-300'
                }`}
              >
                Reference Guide
              </button>
            </div>
          </div>

          {/* Core Interactive Panel Content Area */}
          <div className="flex-1 overflow-y-auto min-h-0 p-4 scrollbar-thin">
            
            {/* Tab: Reference Guide (Duplicated exact accordion text from Screenshot 2026-06-01 124209.jpg) */}
            {niaActiveTab === 'reference' && (
              <div className="space-y-3 text-xs leading-relaxed animate-in fade-in duration-300 text-left">
                
                {/* 1. What is Nia */}
                <div className={`border rounded-lg overflow-hidden ${isDark ? 'border-stone-800 bg-stone-950/40' : 'border-stone-200'}`}>
                  <button 
                    onClick={() => toggleAccordion('whatis')}
                    className="w-full px-3 py-2.5 flex items-center justify-between text-left font-bold text-stone-200 hover:text-amber-500 transition-colors"
                  >
                    <span>What is Nia?</span>
                    <ChevronDown size={14} className={`transform transition-transform ${expandedAccordions.whatis ? 'rotate-180' : ''}`} />
                  </button>
                  {expandedAccordions.whatis && (
                    <div className={`px-3 pb-3 text-stone-400 text-[11px] leading-relaxed border-t pt-2 ${isDark ? 'border-stone-800' : 'border-stone-100'}`}>
                      Nia is a course-grounded student success coach for this CNA recertification course. Nia helps you understand where you are in the course, what to review next, why a gate may be locked, and how course topics connect to safe CNA practice.
                    </div>
                  )}
                </div>

                {/* 2. What Nia can help with */}
                <div className={`border rounded-lg overflow-hidden ${isDark ? 'border-stone-800 bg-stone-950/40' : 'border-stone-200'}`}>
                  <button 
                    onClick={() => toggleAccordion('canhelp')}
                    className="w-full px-3 py-2.5 flex items-center justify-between text-left font-bold text-stone-200 hover:text-amber-500 transition-colors"
                  >
                    <span>What Nia can help with</span>
                    <ChevronDown size={14} className={`transform transition-transform ${expandedAccordions.canhelp ? 'rotate-180' : ''}`} />
                  </button>
                  {expandedAccordions.canhelp && (
                    <div className={`px-3 pb-3 text-stone-400 text-[11px] leading-relaxed border-t pt-2 ${isDark ? 'border-stone-800' : 'border-stone-100'}`}>
                      Course navigation, module and lesson summaries, key terms, quiz and final-exam study readiness, the certificate gate, optional clinical support, the no-PHI rules, and CNA scope of practice.
                    </div>
                  )}
                </div>

                {/* 3. What Nia cannot do */}
                <div className={`border rounded-lg overflow-hidden ${isDark ? 'border-stone-800 bg-stone-950/40' : 'border-stone-200'}`}>
                  <button 
                    onClick={() => toggleAccordion('cannot')}
                    className="w-full px-3 py-2.5 flex items-center justify-between text-left font-bold text-stone-200 hover:text-amber-500 transition-colors"
                  >
                    <span>What Nia cannot do</span>
                    <ChevronDown size={14} className={`transform transition-transform ${expandedAccordions.cannot ? 'rotate-180' : ''}`} />
                  </button>
                  {expandedAccordions.cannot && (
                    <div className={`px-3 pb-3 text-stone-400 text-[11px] leading-relaxed border-t pt-2 ${isDark ? 'border-stone-800' : 'border-stone-100'}`}>
                      Nia cannot provide final exam answer keys, certify completion, issue certificates, grant clinical hours or credit, review real patient information, diagnose conditions, recommend treatment, or replace your instructor, employer, supervisor, licensed nurse, legal counsel, or CDPH guidance.
                    </div>
                  )}
                </div>

                {/* 4. No PHI */}
                <div className={`border rounded-lg overflow-hidden ${isDark ? 'border-stone-800 bg-stone-950/40' : 'border-stone-200'}`}>
                  <button 
                    onClick={() => toggleAccordion('nophi')}
                    className="w-full px-3 py-2.5 flex items-center justify-between text-left font-bold text-stone-200 hover:text-amber-500 transition-colors"
                  >
                    <span>No PHI Guidelines</span>
                    <ChevronDown size={14} className={`transform transition-transform ${expandedAccordions.nophi ? 'rotate-180' : ''}`} />
                  </button>
                  {expandedAccordions.nophi && (
                    <div className={`px-3 pb-3 text-stone-400 text-[11px] leading-relaxed border-t pt-2 ${isDark ? 'border-stone-800' : 'border-stone-100'}`}>
                      Do not type real patient, resident, family, facility, chart, medical record, DOB, room number, or identifying details. Use fictional examples only (for example, "Mr. Johnson" or "Mr. Park").
                    </div>
                  )}
                </div>

                {/* 5. Certificate gate help */}
                <div className={`border rounded-lg overflow-hidden ${isDark ? 'border-stone-800 bg-stone-950/40' : 'border-stone-200'}`}>
                  <button 
                    onClick={() => toggleAccordion('gatehelp')}
                    className="w-full px-3 py-2.5 flex items-center justify-between text-left font-bold text-stone-200 hover:text-amber-500 transition-colors"
                  >
                    <span>Certificate gate help</span>
                    <ChevronDown size={14} className={`transform transition-transform ${expandedAccordions.gatehelp ? 'rotate-180' : ''}`} />
                  </button>
                  {expandedAccordions.gatehelp && (
                    <div className={`px-3 pb-3 text-stone-400 text-[11px] leading-relaxed border-t pt-2 ${isDark ? 'border-stone-800' : 'border-stone-100'}`}>
                      A certificate can stay locked for required modules incomplete, final exam not passed, active-time/completion checks pending, or affidavit/approval metadata pending. Production certificate issuance remains disabled in this preview. Open the Certificate Gate for your specific status.
                    </div>
                  )}
                </div>

                {/* 6. Final exam study support */}
                <div className={`border rounded-lg overflow-hidden ${isDark ? 'border-stone-800 bg-stone-950/40' : 'border-stone-200'}`}>
                  <button 
                    onClick={() => toggleAccordion('examstudy')}
                    className="w-full px-3 py-2.5 flex items-center justify-between text-left font-bold text-stone-200 hover:text-amber-500 transition-colors"
                  >
                    <span>Final exam study support</span>
                    <ChevronDown size={14} className={`transform transition-transform ${expandedAccordions.examstudy ? 'rotate-180' : ''}`} />
                  </button>
                  {expandedAccordions.examstudy && (
                    <div className={`px-3 pb-3 text-stone-400 text-[11px] leading-relaxed border-t pt-2 ${isDark ? 'border-stone-800' : 'border-stone-100'}`}>
                      Nia helps you study by topic, review the related modules, focus on weak areas, and use the module knowledge checks. Nia never reveals the answer key.
                    </div>
                  )}
                </div>

              </div>
            )}

            {/* Tab: Active Chat Coach */}
            {niaActiveTab === 'chat' && (
              <div className="space-y-4 animate-in fade-in duration-300 flex flex-col justify-end text-left">
                {niaMessages.map((msg, idx) => (
                  <div 
                    key={idx} 
                    className={`flex flex-col max-w-[85%] space-y-1 ${
                      msg.sender === 'nia' ? 'self-start' : 'self-end items-end'
                    }`}
                  >
                    <div className={`px-3 py-2.5 rounded-2xl text-[11px] leading-relaxed ${
                      msg.sender === 'nia' 
                        ? isDark ? 'bg-stone-900 text-stone-200 border border-stone-800' : 'bg-stone-100 text-stone-800'
                        : isDark ? 'bg-[#5c1111] text-stone-100' : 'bg-[#8B1515] text-white'
                    }`}>
                      {msg.text}
                    </div>
                    <span className="text-[8px] text-stone-600 font-mono tracking-wider px-1">{msg.timestamp}</span>
                  </div>
                ))}

                {isNiaThinking && (
                  <div className="self-start flex flex-col max-w-[85%] space-y-1">
                    <div className={`px-3 py-2 rounded-2xl text-[11px] font-mono flex items-center gap-1.5 ${
                      isDark ? 'bg-stone-900 text-amber-500 border border-stone-800' : 'bg-stone-100 text-[#8B1515]'
                    }`}>
                      <span className="w-1.5 h-1.5 rounded-full bg-amber-500 animate-pulse"></span>
                      <span className="w-1.5 h-1.5 rounded-full bg-amber-500 animate-pulse [animation-delay:0.2s]"></span>
                      <span className="w-1.5 h-1.5 rounded-full bg-amber-500 animate-pulse [animation-delay:0.4s]"></span>
                      <span className="italic pl-1 text-[10px]">Analyzing compliance matrix...</span>
                    </div>
                  </div>
                )}
                
                <div ref={chatEndRef} />
              </div>
            )}

          </div>

          {/* Interactive Chat Input Controls - Bottom Area */}
          <div className={`p-3 shrink-0 border-t ${isDark ? 'border-stone-800 bg-stone-950/40' : 'border-stone-200 bg-stone-50'}`}>
            
            {/* Quick study queries pill buttons list */}
            <div className="flex gap-1.5 overflow-x-auto pb-2 scrollbar-none scroll-smooth">
              {Object.keys(fallbackKnowledgeBase).map((pillText, idx) => (
                <button
                  key={idx}
                  onClick={() => {
                    setNiaActiveTab('chat');
                    handleNiaSendMessage(pillText);
                  }}
                  className={`px-2.5 py-1 rounded-full border text-[9.5px] font-semibold whitespace-nowrap tracking-wide transition-all shrink-0 ${
                    isDark 
                      ? 'border-[#3b0b0b] bg-[#1a0808] text-amber-500 hover:border-amber-500/40' 
                      : 'border-stone-200 bg-white text-[#8B1515] hover:border-[#8B1515]/40'
                  }`}
                >
                  {pillText}
                </button>
              ))}
            </div>

            {/* Input message box with button */}
            <form 
              onSubmit={(e) => {
                e.preventDefault();
                handleNiaSendMessage();
              }}
              className="flex items-center gap-2 mt-1.5"
            >
              <input 
                type="text"
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                placeholder="Ask about modules, quizzes, gates, clinical sup..."
                className={`flex-grow px-3 py-2 border rounded-xl text-[11px] focus:outline-none focus:ring-1 focus:ring-amber-500 font-sans ${
                  isDark 
                    ? 'bg-[#080404] border-stone-800 text-stone-200 placeholder-stone-500' 
                    : 'bg-white border-stone-300 text-stone-900 placeholder-stone-400'
                }`}
              />
              <button
                type="submit"
                className="w-8 h-8 rounded-xl bg-[#5c1111] hover:bg-[#781616] text-stone-100 flex items-center justify-center transition-colors shrink-0"
                title="Send grounded question"
              >
                <Send size={12} />
              </button>
            </form>
          </div>

        </aside>

      </div>
    </div>
  );
}