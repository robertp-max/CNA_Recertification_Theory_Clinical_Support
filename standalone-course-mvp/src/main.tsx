import React, { useMemo, useState } from "react";
import { createRoot } from "react-dom/client";
import {
  AlertTriangle,
  BookOpen,
  CheckCircle2,
  ClipboardCheck,
  FileWarning,
  GraduationCap,
  HelpCircle,
  Lock,
  LogOut,
  Map,
  Moon,
  ShieldCheck,
  ShieldAlert,
  Stethoscope,
  Sun,
  UserRound,
  Wrench,
} from "lucide-react";
import { modules } from "./data/courseData";
import { auditItems, moodleMap, qaTests, sourceInventory } from "./data/auditAndMigrationData";
import { clinicalSupportSections } from "./data/clinicalSupportContent";
import {
  evaluateGateScenario,
  executiveCards,
  gateAuditEvidence,
  gateDefinitions,
  gateScenarios,
  optionalClinicalBoundaryRows,
  stakeholderDemoScript,
} from "./data/gateCommandCenterData";
import { examPreviewQuestions, moduleContents, type SeededModuleContent } from "./data/moduleContent";
import "./styles.css";

const demoLoginDefaults = {
  email: "admin@careindeed.com",
  password: "Caregiver2012!",
};

type View =
  | "landing"
  | "dashboard"
  | "module0"
  | "module1"
  | "modules"
  | "exam"
  | "affidavit"
  | "certificate"
  | "gateCenter"
  | "clinical"
  | "audit"
  | "moodle"
  | "qa";

type LearnerState = {
  legalFirstName: string;
  legalLastName: string;
  cnaNumber: string;
  onlineCapAck: boolean;
  phiAck: boolean;
  orientationFinalAck: boolean;
  module1Interaction: boolean;
  module1QuizPassed: boolean;
  remainingTheorySimulated: boolean;
  activeTimeMet: boolean;
  finalExamAttempted: boolean;
  finalExamPassed: boolean;
  affidavitComplete: boolean;
  certificateFieldsPopulated: boolean;
  adminHoldClear: boolean;
};

type DemoUserProfile = {
  displayName: string;
  role: string;
  email: string;
  legalFirstName: string;
  legalLastName: string;
  cnaNumber: string;
  renewalCycle: string;
  courseCohort: string;
  phone: string;
  organization: string;
  location: string;
  reviewStatus: string;
  notes: string;
};

const defaultDemoProfile: DemoUserProfile = {
  displayName: "James Bond",
  role: "Stakeholder Admin / Review Learner",
  email: "admin@careindeed.com",
  legalFirstName: "James",
  legalLastName: "Bond",
  cnaNumber: "CNA-DEMO-007",
  renewalCycle: "2026-2028",
  courseCohort: "CNA Recertification Standalone MVP Review",
  phone: "(650) 268-4983",
  organization: "Care Indeed / CI Institute of Nursing",
  location: "Menlo Park, CA",
  reviewStatus: "Stakeholder review user",
  notes: "Fictional seeded profile for internal review only; not a real learner record.",
};

const initialState: LearnerState = {
  legalFirstName: defaultDemoProfile.legalFirstName,
  legalLastName: defaultDemoProfile.legalLastName,
  cnaNumber: defaultDemoProfile.cnaNumber,
  onlineCapAck: false,
  phiAck: false,
  orientationFinalAck: false,
  module1Interaction: false,
  module1QuizPassed: false,
  remainingTheorySimulated: false,
  activeTimeMet: false,
  finalExamAttempted: false,
  finalExamPassed: false,
  affidavitComplete: false,
  certificateFieldsPopulated: true,
  adminHoldClear: true,
};

function App() {
  const [theme, setTheme] = useState<"dark" | "light">(() => (localStorage.getItem("ciTheme") === "light" ? "light" : "dark"));
  const [authenticated, setAuthenticated] = useState(() => sessionStorage.getItem("ciStakeholderSession") === "true");
  const [profile, setProfile] = useState<DemoUserProfile>(defaultDemoProfile);
  const [unlockMode, setUnlockMode] = useState(false);
  const [view, setView] = useState<View>("landing");
  const [state, setState] = useState<LearnerState>(initialState);
  const update = <K extends keyof LearnerState>(key: K, value: LearnerState[K]) =>
    setState((current) => ({ ...current, [key]: value }));
  const updateProfile = <K extends keyof DemoUserProfile>(key: K, value: DemoUserProfile[K]) => {
    setProfile((current) => ({ ...current, [key]: value }));
    if (key === "legalFirstName" || key === "legalLastName" || key === "cnaNumber") {
      setState((current) => ({ ...current, [key]: value as string }));
    }
  };
  const resetDemoProfile = () => {
    setProfile(defaultDemoProfile);
    setState((current) => ({
      ...current,
      legalFirstName: defaultDemoProfile.legalFirstName,
      legalLastName: defaultDemoProfile.legalLastName,
      cnaNumber: defaultDemoProfile.cnaNumber,
    }));
  };

  const gates = useMemo(() => computeGates(state), [state]);
  const requiredComplete = gates.every((gate) => gate.pass);
  const module0Complete =
    hasLegalName(state) && Boolean(state.cnaNumber.trim()) && state.onlineCapAck && state.phiAck && state.orientationFinalAck;
  const module1Complete = state.module1Interaction && state.module1QuizPassed;
  const theoryComplete = module0Complete && module1Complete && state.remainingTheorySimulated;
  const examUnlocked = theoryComplete && state.activeTimeMet;
  const certificateReady = requiredComplete;

  if (!authenticated) {
    return (
      <div className="app-shell" data-theme={theme}>
        <SplashLogin
          theme={theme}
          setTheme={setTheme}
          onAuthenticated={(identity) => {
            sessionStorage.setItem("ciStakeholderSession", "true");
            setAuthenticated(true);
            if (identity.email) updateProfile("email", identity.email);
          }}
        />
      </div>
    );
  }

  return (
    <div className="app-shell" data-theme={theme}>
      <div className="review-ribbon">Reviewer environment | Mock certificate controls only | No learner records</div>
      {unlockMode && <div className="unlock-ribbon">Unlock Mode Active | Internal navigation only | Gates remain unchanged</div>}
      <header className="app-header">
        <div>
          <img
            className="header-logo"
            src={theme === "dark" ? "/brand/logos/ci-ion-logomark-white.svg" : "/brand/logos/ci-ion-logomark-original.svg"}
            alt="CI Institute of Nursing"
          />
          <p className="eyebrow">CareIndeed / CI Institute of Nursing</p>
          <h1>CNA Recertification Theory + Clinical Support Review</h1>
          <p className="subhead">
            Premium stakeholder review for required online CE flow, certificate gates, optional clinical support,
            audit preview, and Moodle migration mapping.
          </p>
        </div>
        <div className="header-actions">
          <div className="identity-card">
            <UserRound />
            <div>
              <strong>{profile.displayName}</strong>
              <span>{profile.role}</span>
            </div>
          </div>
          <StatusPill pass={certificateReady} label={certificateReady ? "Certificate preview unlocked" : "Certificate preview locked"} />
          <ThemeToggle theme={theme} setTheme={setTheme} />
          <details className="admin-tools-menu">
            <summary><Wrench /> Reviewer Tools</summary>
            <button className="secondary" onClick={() => setView("qa")}>Open Advanced QA Controls</button>
            <p>Internal review utilities remain available but are kept out of the primary stakeholder path.</p>
          </details>
          <button
            className="ghost-button"
            onClick={() => {
              sessionStorage.removeItem("ciStakeholderSession");
              setAuthenticated(false);
              setUnlockMode(false);
            }}
          >
            <LogOut /> Sign out
          </button>
        </div>
      </header>

      <nav className="top-nav" aria-label="Primary">
        {[
          ["landing", "Course"],
          ["dashboard", "Dashboard"],
          ["modules", "Modules"],
          ["certificate", "Certificate"],
          ["gateCenter", "Gate Center"],
          ["clinical", "Clinical Hub"],
          ["audit", "Audit"],
          ["moodle", "Moodle Map"],
        ].map(([key, label]) => (
          <button key={key} className={view === key ? "active" : ""} onClick={() => setView(key as View)}>
            {label}
          </button>
        ))}
      </nav>

      <main key={view} className="view-stage">
        {view === "landing" && <Landing setView={setView} gates={gates} />}
        {view === "dashboard" && (
          <Dashboard
            state={state}
            profile={profile}
            updateProfile={updateProfile}
            resetDemoProfile={resetDemoProfile}
            unlockMode={unlockMode}
            setUnlockMode={setUnlockMode}
            gates={gates}
            module0Complete={module0Complete}
            module1Complete={module1Complete}
            theoryComplete={theoryComplete}
            examUnlocked={examUnlocked}
            setView={setView}
          />
        )}
        {view === "modules" && <ModuleShell setView={setView} module0Complete={module0Complete} module1Complete={module1Complete} unlockMode={unlockMode} />}
        {view === "module0" && <Module0 state={state} update={update} />}
        {view === "module1" && <Module1 state={state} update={update} module0Complete={module0Complete} unlockMode={unlockMode} />}
        {view === "exam" && <FinalExam state={state} update={update} examUnlocked={examUnlocked || unlockMode} unlockMode={unlockMode} />}
        {view === "affidavit" && <Affidavit state={state} update={update} enabled={state.finalExamPassed || unlockMode} unlockMode={unlockMode} />}
        {view === "certificate" && <Certificate gates={gates} certificateReady={certificateReady} state={state} profile={profile} />}
        {view === "gateCenter" && <GateCommandCenter setView={setView} />}
        {view === "clinical" && <ClinicalHub />}
        {view === "audit" && <AuditPreview state={state} gates={gates} />}
        {view === "moodle" && <MoodleMigrationMap />}
        {view === "qa" && <QAPanel state={state} setState={setState} gates={gates} />}
      </main>
    </div>
  );
}

function SplashLogin({
  onAuthenticated,
  theme,
  setTheme,
}: {
  onAuthenticated: (identity: { email?: string; displayName?: string }) => void;
  theme: "dark" | "light";
  setTheme: (theme: "dark" | "light") => void;
}) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const localHints = import.meta.env.DEV || import.meta.env.VITE_DEMO_LOGIN_HINTS === "true";
  const demoFallbackDisabled = import.meta.env.VITE_DEMO_LOGIN_ENABLED === "false";
  const expectedDemoEmail = String(import.meta.env.VITE_DEMO_LOGIN_EMAIL || demoLoginDefaults.email).trim().toLowerCase();
  const expectedDemoPassword = String(import.meta.env.VITE_DEMO_LOGIN_PASSWORD || demoLoginDefaults.password);

  async function submit(event: React.FormEvent) {
    event.preventDefault();
    setError("");
    setLoading(true);
    try {
      const response = await fetch("/api/demo-login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      if (response.ok) {
        const payload = await response.json();
        onAuthenticated({ email: payload.email, displayName: payload.displayName });
        return;
      }
    } catch {
      // Local Vite preview does not run Vercel Functions. Use only explicit Vite visual-demo env vars.
    }

    if (
      !demoFallbackDisabled &&
      email.trim().toLowerCase() === expectedDemoEmail &&
      password === expectedDemoPassword
    ) {
      onAuthenticated({ email });
      setLoading(false);
      return;
    }

    setError("Invalid review credentials or review login environment variables are not configured.");
    setLoading(false);
  }

  return (
    <main className="splash-page">
      <section className="splash-panel splash-layout">
        <div className="splash-copy">
          <div className="splash-toolbar">
            <span>Reviewer access</span>
            <ThemeToggle theme={theme} setTheme={setTheme} />
          </div>
          <div className="brand-lockup">
            <img
              className="brand-logo"
              src={theme === "dark" ? "/brand/logos/ci-ion-logomark-white.svg" : "/brand/logos/ci-ion-logo-original.svg"}
              alt="CI Institute of Nursing"
            />
            <div>
              <p className="eyebrow">CareIndeed / CI Institute of Nursing</p>
              <h1>CNA Recertification Theory + Clinical Support Review</h1>
            </div>
          </div>
          <span className="review-badge">Stakeholder Review Access</span>
          <p className="splash-warning">Mock review environment: not a live CE course or certificate system.</p>
          <form className="login-form" onSubmit={submit}>
            <label>
              Email
              <input autoComplete="email" value={email} onChange={(event) => setEmail(event.target.value)} />
            </label>
            <label>
              Password
              <input type="password" autoComplete="current-password" value={password} onChange={(event) => setPassword(event.target.value)} />
            </label>
            {localHints && (
              <details className="reviewer-disclosure">
                <summary>Local access note</summary>
                <p>
                  The local Vite fallback accepts the configured review credential when the Vercel Function is unavailable.
                  Use deployment protection or Vercel Authentication for deployed review links.
                </p>
              </details>
            )}
            {error && <div className="feedback bad">{error}</div>}
            <button disabled={loading}>{loading ? "Checking..." : "Sign in"}</button>
          </form>
          <div className="notice">
            Stakeholder access layer only. No real learner record, no PHI, and no certificate issuance occurs here.
          </div>
        </div>
        <aside className="splash-visual" aria-label="CNA students reviewing online coursework">
          <div className="image-frame login-image" />
          <div className="visual-stat-card">
            <span>Integrity Gates</span>
            <strong>Required CE only</strong>
          </div>
          <div className="visual-stat-card secondary-stat">
            <span>Support Boundary</span>
            <strong>Optional, non-gating</strong>
          </div>
        </aside>
      </section>
    </main>
  );
}

function ThemeToggle({ theme, setTheme }: { theme: "dark" | "light"; setTheme: (theme: "dark" | "light") => void }) {
  const nextTheme = theme === "dark" ? "light" : "dark";
  return (
    <button
      className="theme-toggle"
      aria-label={`Switch to ${nextTheme} mode`}
      onClick={() => {
        localStorage.setItem("ciTheme", nextTheme);
        setTheme(nextTheme);
      }}
    >
      {theme === "dark" ? <Sun /> : <Moon />}
      <span>{theme === "dark" ? "Light" : "Dark"}</span>
    </button>
  );
}

function Landing({ setView, gates }: { setView: (view: View) => void; gates: Gate[] }) {
  return (
      <section className="hero">
      <div className="hero-copy">
        <p className="eyebrow">12-hour asynchronous theory pathway</p>
        <h2>Premium online CE pathway with certificate integrity controls</h2>
        <p>
          This standalone review build demonstrates the intended learner/admin experience before Moodle launch. It
          preserves approval blockers, active-time validation warnings, final exam/test preview, final
          statement workflow, and audit packet structure.
        </p>
        <div className="button-row">
          <button onClick={() => setView("dashboard")}>Open learner dashboard</button>
          <button className="secondary" onClick={() => setView("module0")}>
            Start Module 0
          </button>
        </div>
      </div>
      <div className="hero-media" aria-label="CI Institute of Nursing brand image" />
      <aside className="status-card" aria-label="Course status preview">
        <h3>Certificate Status Preview</h3>
        <p className="warning-text">Mock preview only. No live certificate issuance. CDPH approval is not claimed.</p>
        {gates.slice(0, 6).map((gate) => (
          <GateRow key={gate.id} gate={gate} />
        ))}
      </aside>
      <div className="full-width three-col">
        <InfoBlock
          icon={<GraduationCap />}
          title="Required Online CE"
          text="Required theory progress is tracked separately and gates the certificate preview."
        />
        <InfoBlock
          icon={<Stethoscope />}
          title="Optional Clinical Support"
          text="Clinical support is helpful, separate, non-credit, and never counted toward online CE progress."
        />
        <InfoBlock
          icon={<ShieldAlert />}
          title="No PHI"
          text="PHI warnings appear before uploads, documentation support, and free-text areas."
        />
      </div>
    </section>
  );
}

function Dashboard(props: {
  state: LearnerState;
  profile: DemoUserProfile;
  updateProfile: <K extends keyof DemoUserProfile>(key: K, value: DemoUserProfile[K]) => void;
  resetDemoProfile: () => void;
  unlockMode: boolean;
  setUnlockMode: (enabled: boolean) => void;
  gates: Gate[];
  module0Complete: boolean;
  module1Complete: boolean;
  theoryComplete: boolean;
  examUnlocked: boolean;
  setView: (view: View) => void;
}) {
  const nextStep = getNextStep(props);
  const requiredProgress = percent([
    props.module0Complete,
    props.module1Complete,
    props.state.remainingTheorySimulated,
    props.state.activeTimeMet,
    props.state.finalExamPassed,
    props.state.affidavitComplete,
  ]);
  const optionalProgress = 0;
  return (
    <section>
      <SectionHeader icon={<ClipboardCheck />} title="Learner Dashboard" text="Required and optional progress are intentionally separate." />
      <ReviewNotes />
      <div className="dashboard-grid">
        <div className="panel primary-panel">
          <p className="eyebrow">Next required step</p>
          <h2>{nextStep.label}</h2>
          <p>{nextStep.note}</p>
          <button onClick={() => props.setView(nextStep.view)}>{nextStep.action}</button>
        </div>
        <ProgressPanel title="Required Theory Progress" value={requiredProgress} note="Includes required theory, active-time simulation, final exam, and affidavit only." />
        <ProgressPanel title="Optional Clinical Support" value={optionalProgress} note="Shown separately. Skipping it must not block the online CE certificate." />
      </div>
      <div className="dashboard-lower">
        <DemoUserProfilePanel
          profile={props.profile}
          updateProfile={props.updateProfile}
          resetDemoProfile={props.resetDemoProfile}
          unlockMode={props.unlockMode}
          setUnlockMode={props.setUnlockMode}
        />
        <aside className="panel gate-summary-panel">
          <div className="panel-heading">
            <div>
              <p className="eyebrow">Certificate readiness</p>
              <h3>Required Gate Evidence</h3>
            </div>
            <StatusPill pass={props.gates.every((gate) => gate.pass)} label={props.gates.every((gate) => gate.pass) ? "Ready" : "Blocked"} />
          </div>
          <div className="dashboard-image-strip" aria-label="CNA online learning visual" />
          <div className="gate-list">
            {props.gates.map((gate) => (
              <GateRow key={gate.id} gate={gate} />
            ))}
          </div>
        </aside>
      </div>
    </section>
  );
}

function ModuleShell({
  setView,
  module0Complete,
  module1Complete,
  unlockMode,
}: {
  setView: (view: View) => void;
  module0Complete: boolean;
  module1Complete: boolean;
  unlockMode: boolean;
}) {
  return (
    <section>
      <SectionHeader icon={<BookOpen />} title="Module Navigation" text="Full 12-hour review shell seeded from extracted content with review flags and Moodle migration notes." />
      <div className="module-layout">
        <aside className="panel module-context-card">
          <div className="module-visual" aria-label="CNA coursework visual" />
          <p className="eyebrow">Course experience</p>
          <h3>Guided, gated, and audit aware</h3>
          <p>
            Required theory modules move learners toward a locked certificate preview while optional clinical support remains separate.
          </p>
          <div className="tag-row">
            <span>12-hour theory pathway</span>
            <span>Optional support excluded</span>
          </div>
        </aside>
        <div className="module-grid">
          {modules.map((module) => (
            <article key={module.id} className="module-card">
              <p className="eyebrow">{module.time}</p>
              <h3>{module.title}</h3>
              <p>{module.summary}</p>
              <div className="tag-row">
                <span>{module.id === "final" ? "Required certificate gates" : "Required online CE"}</span>
                <span>{module.status}</span>
              </div>
              {module.id === "m0" && <button onClick={() => setView("module0")}>{module0Complete || unlockMode ? "Review Module 0" : "Open Module 0"}</button>}
              {module.id === "m1" && <button onClick={() => setView("module1")}>{module1Complete || unlockMode ? "Review Module 1" : "Open Module 1"}</button>}
              {module.id === "final" && <button onClick={() => setView("exam")}>Open Final Preview</button>}
              {module.id !== "final" && <SeededModuleDetails module={moduleContents.find((item) => item.id === module.id)} />}
              {module.placeholder && (
                <div className="notice">
                  <strong>Placeholder:</strong> Content placeholder pending approved source conversion. Question bank
                  placeholder pending approved exam blueprint.
                </div>
              )}
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

function Module0({ state, update }: { state: LearnerState; update: <K extends keyof LearnerState>(key: K, value: LearnerState[K]) => void }) {
  return (
    <section>
      <SectionHeader icon={<ShieldAlert />} title="Module 0: Orientation and Compliance Boundaries" text="Functional review screen based on extracted Module 0 source content." />
      <div className="content-stack">
        <article className="panel">
          <h3>Course Scope</h3>
          <p>
            This online course provides up to 12 hours of theory-based continuing education support for California CNA
            renewal only if CI Institute of Nursing and the course are approved for California CNA online CE.
          </p>
          <ul>
            <li>California CNA renewal requires 48 hours over each two-year certification period.</li>
            <li>At least 12 hours must be completed each year.</li>
            <li>Only 24 of the 48 hours may be completed through CDPH-approved online CE.</li>
            <li>This course does not complete all California CNA renewal requirements by itself.</li>
          </ul>
        </article>
        <TranscriptBox title="TTS / Transcript Placeholder" />
        <article className="panel">
          <h3>Identity/Profile Fields Mockup</h3>
          <div className="form-grid">
            <label>
              Legal first name
              <input value={state.legalFirstName} onChange={(event) => update("legalFirstName", event.target.value)} />
            </label>
            <label>
              Legal last name
              <input value={state.legalLastName} onChange={(event) => update("legalLastName", event.target.value)} />
            </label>
            <label>
              CNA certificate number
              <input value={state.cnaNumber} onChange={(event) => update("cnaNumber", event.target.value)} />
            </label>
          </div>
        </article>
        <article className="panel">
          <h3>Required Acknowledgements</h3>
          <CheckBox
            checked={state.onlineCapAck}
            onChange={(checked) => update("onlineCapAck", checked)}
            label="I understand the 24-hour online CE cap and that this 12-hour course is partial renewal credit only."
          />
          <CheckBox
            checked={state.phiAck}
            onChange={(checked) => update("phiAck", checked)}
            label="I will not enter or upload PHI about real patients, residents, or individuals in any part of this course."
          />
          <CheckBox
            checked={state.orientationFinalAck}
            onChange={(checked) => update("orientationFinalAck", checked)}
            label="I understand optional clinical support is separate and does not affect the online CE certificate gate."
          />
        </article>
      </div>
    </section>
  );
}

function Module1({
  state,
  update,
  module0Complete,
  unlockMode,
}: {
  state: LearnerState;
  update: <K extends keyof LearnerState>(key: K, value: LearnerState[K]) => void;
  module0Complete: boolean;
  unlockMode: boolean;
}) {
  const [answer, setAnswer] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const correct = answer === "report";
  return (
    <section>
      <SectionHeader icon={<BookOpen />} title="Module 1: Infection Control and PPE" text="Functional review screen using extracted Module 1 source content; source notes require SME/source review before production." />
      {!module0Complete && !unlockMode && <LockNotice text="Module 1 is intended to unlock after Module 0 identity, online cap, PHI, and orientation acknowledgements are complete." />}
      {!module0Complete && unlockMode && <LockNotice text="Unlock Mode lets stakeholders review Module 1 without marking Module 0 complete." />}
      <div className="content-stack">
        <article className="panel">
          <h3>Microlearning Sections</h3>
          <ul>
            <li>Why infection control matters in long-term care.</li>
            <li>The chain of infection and how CNAs break it.</li>
            <li>Hand hygiene: soap/water, sanitizer, and key moments.</li>
            <li>PPE selection, donning, and doffing.</li>
            <li>Recognizing and reporting infection signs.</li>
            <li>Environmental cleaning and safe linen handling.</li>
          </ul>
          <div className="notice">
            Module 1 production content is marked in the source package as needing SME/source review. This review build does
            not claim final approved content status.
          </div>
        </article>
        <TranscriptBox title="Optional TTS Placeholder: Infection Control Summary" />
        <article className="panel">
          <h3>Scenario Check</h3>
          <p>
            During a busy shift, Mrs. J is usually alert and talkative. Today she seems suddenly confused and agitated.
            She also ate very little at breakfast. What is the CNA's best first action?
          </p>
          <div className="answer-list" role="radiogroup" aria-label="Module 1 scenario choices">
            {[
              ["sleep", "Assume she did not sleep well and check again tomorrow."],
              ["chart", "Document the change and continue with rounds."],
              ["report", "Report the change to the licensed nurse immediately."],
            ].map(([value, label]) => (
              <label key={value}>
                <input type="radio" name="m1-scenario" value={value} checked={answer === value} onChange={() => setAnswer(value)} />
                {label}
              </label>
            ))}
          </div>
          <button
            onClick={() => {
              setSubmitted(true);
              if (correct) update("module1Interaction", true);
            }}
          >
            Submit scenario check
          </button>
          {submitted && (
            <div className={correct ? "feedback good" : "feedback bad"}>
              {correct
                ? "Correct. New confusion or a sudden change from baseline can signal infection or another urgent change. Report it directly to the licensed nurse."
                : "Not yet. Review the reporting section: sudden confusion in an older resident should be reported immediately. This remediation message is part of the review feedback evidence."}
            </div>
          )}
        </article>
        <article className="panel">
          <h3>Module Completion Status</h3>
          <CheckBox
            checked={state.module1QuizPassed}
            onChange={(checked) => update("module1QuizPassed", checked)}
            label="Prototype module quiz passed at 80% or higher."
          />
          <StatusPill pass={state.module1Interaction && state.module1QuizPassed} label={state.module1Interaction && state.module1QuizPassed ? "Module 1 complete" : "Module 1 incomplete"} />
        </article>
      </div>
    </section>
  );
}

function FinalExam({
  state,
  update,
  examUnlocked,
  unlockMode,
}: {
  state: LearnerState;
  update: <K extends keyof LearnerState>(key: K, value: LearnerState[K]) => void;
  examUnlocked: boolean;
  unlockMode: boolean;
}) {
  return (
    <section>
      <SectionHeader icon={<ClipboardCheck />} title="Final Exam/Test Preview" text="Uses extracted question-bank examples as review preview only. This is not a final approved exam." />
      {!examUnlocked && <LockNotice text="Final exam/test preview is locked until required theory completion and simulated active-time gates are met." />}
      {unlockMode && <LockNotice text="Unlock Mode is active for stakeholder navigation only. Passing/failing here still changes only review state." />}
      <div className="panel">
        <p>
          Extracted source indicates a 50-question final exam pool, 25-question attempt, 80% review passing
          threshold, and remediation after failed attempt. The pool is preview-only until approval and flagged items are
          reviewed.
        </p>
        <div className="question-preview-grid">
          {examPreviewQuestions.map((question) => (
            <article className="content-item" key={question.id}>
              <p className="eyebrow">{question.id} - {question.module}</p>
              <h3>{question.prompt}</h3>
              <p><strong>Source answer:</strong> {question.answer}</p>
              <p className="source-note">{question.reviewStatus}</p>
            </article>
          ))}
        </div>
        <div className="button-row">
          <button disabled={!examUnlocked} onClick={() => setExam(update, true)}>
            Simulate passing final exam
          </button>
          <button className="secondary" disabled={!examUnlocked} onClick={() => setExam(update, false)}>
            Simulate failing final exam
          </button>
        </div>
        {state.finalExamAttempted && (
          <div className={state.finalExamPassed ? "feedback good" : "feedback bad"}>
            {state.finalExamPassed
              ? "Prototype result: passed. Affidavit screen is now available."
              : "Prototype result: failed. Certificate remains unavailable. Review infection control, resident rights, dementia care, mobility/falls, nutrition/skin/vitals, and documentation/scope before retry."}
          </div>
        )}
      </div>
    </section>
  );
}

function Affidavit({
  state,
  update,
  enabled,
  unlockMode,
}: {
  state: LearnerState;
  update: <K extends keyof LearnerState>(key: K, value: LearnerState[K]) => void;
  enabled: boolean;
  unlockMode: boolean;
}) {
  return (
    <section>
      <SectionHeader icon={<FileWarning />} title="Final Statement / Affidavit Prototype" text="Draft only, pending legal/CDPH approval. E-signature acceptance is unresolved." />
      {!enabled && <LockNotice text="Draft affidavit unlocks after the final exam/test is passed." />}
      {unlockMode && <LockNotice text="Unlock Mode allows stakeholder review of this screen without treating the affidavit as complete." />}
      <div className="panel">
        <p>I affirm that I personally completed the required course activities, used my own login, did not receive unauthorized exam assistance, understand the online CE cap, and did not enter PHI.</p>
        <CheckBox
          disabled={!enabled}
          checked={state.affidavitComplete}
          onChange={(checked) => update("affidavitComplete", checked)}
          label="Prototype signature acknowledgement complete."
        />
      </div>
    </section>
  );
}

function Certificate({
  gates,
  certificateReady,
  state,
  profile,
}: {
  gates: Gate[];
  certificateReady: boolean;
  state: LearnerState;
  profile: DemoUserProfile;
}) {
  const blockers = gates.filter((gate) => !gate.pass);
  const profileReady = hasLegalName(state) && Boolean(state.cnaNumber.trim());
  return (
    <section>
      <SectionHeader icon={<Lock />} title="Certificate Gate Status" text="No live certificate is issued. The mock preview remains blocked until all required gates pass." />
      <div className="certificate-layout">
        <aside className="panel certificate-readiness-card">
          <p className="eyebrow">Readiness summary</p>
          <h3>{certificateReady ? "Mock preview ready" : "Certificate preview locked"}</h3>
          <p>
            Required gates drive this decision. Optional clinical support is excluded from certificate computation.
          </p>
          <StatusPill pass={certificateReady} label={certificateReady ? "All required gates pass" : `${blockers.length} blocker${blockers.length === 1 ? "" : "s"}`} />
          <div className="certificate-profile-list">
            <div>
              <span>Learner profile</span>
              <strong>{profileReady ? "Complete" : "Needs required fields"}</strong>
            </div>
            <div>
              <span>Review learner</span>
              <strong>{state.legalFirstName || "[missing]"} {state.legalLastName || "[missing]"}</strong>
            </div>
            <div>
              <span>CNA number</span>
              <strong>{state.cnaNumber || "[missing]"}</strong>
            </div>
          </div>
        </aside>
        <article className="panel certificate-gates-card">
          <div className="panel-heading">
            <div>
              <p className="eyebrow">Required gates</p>
              <h3>Completion Evidence</h3>
            </div>
            <span className="tag">{gates.filter((gate) => gate.pass).length}/{gates.length} passing</span>
          </div>
          <div className="gate-list">
            {gates.map((gate) => (
              <GateRow key={gate.id} gate={gate} />
            ))}
          </div>
        </article>
        <aside className="panel certificate-actions-card">
          <p className="eyebrow">Blockers and evidence</p>
          <h3>{blockers.length ? "Action Required" : "Evidence Complete"}</h3>
          {blockers.length ? (
            <div className="blocker-list">
              {blockers.slice(0, 4).map((gate) => (
                <span className="tag" key={gate.id}>{gate.label}</span>
              ))}
            </div>
          ) : (
            <div className="feedback good">All required gates pass. The certificate remains a mock/staged preview only.</div>
          )}
          <div className="mini-certificate-card">
            <span>Preview surface</span>
            <strong>{certificateReady ? "Unlocked mock" : "Locked mock"}</strong>
            <p>No live certificate behavior.</p>
          </div>
        </aside>
      </div>
      <div className="certificate-preview">
        <div className="watermark">STAGING / PROTOTYPE ONLY - NOT A LIVE CE CERTIFICATE</div>
        <div className="certificate-topline">
          <img src="/brand/logos/ci-ion-logo-original.svg" alt="CI Institute of Nursing" />
          <span className={certificateReady ? "certificate-seal available" : "certificate-seal locked"}>{certificateReady ? "Preview Open" : "Locked"}</span>
        </div>
        <div className="certificate-title-block">
          <p className="eyebrow">Mock continuing education certificate preview</p>
          <h2>{certificateReady ? "Certificate Preview Available" : "Certificate Preview Locked"}</h2>
          <p>CI Institute of Nursing - provider/NAC# metadata pending approval.</p>
        </div>
        <div className="certificate-field-grid">
          <div>
            <span>Learner</span>
            <strong>{state.legalFirstName || "[missing]"} {state.legalLastName || "[missing]"}</strong>
          </div>
          <div>
            <span>CNA certificate number</span>
            <strong>{state.cnaNumber || "[missing CNA number]"}</strong>
          </div>
          <div>
            <span>Course</span>
            <strong>CNA Recertification Online CE - 12 Hour Theory</strong>
          </div>
          <div>
            <span>Review cohort</span>
            <strong>{profile.courseCohort}</strong>
          </div>
          <div>
            <span>Renewal cycle</span>
            <strong>{profile.renewalCycle}</strong>
          </div>
          <div>
            <span>Status</span>
            <strong>{certificateReady ? "All required gates complete" : "Required gates incomplete"}</strong>
          </div>
        </div>
        <div className="certificate-footer-note">Optional clinical support is not included in this online CE certificate preview.</div>
      </div>
    </section>
  );
}

function GateCommandCenter({ setView }: { setView: (view: View) => void }) {
  const [selectedScenarioId, setSelectedScenarioId] = useState(gateScenarios[0].id);
  const selectedScenario = gateScenarios.find((item) => item.id === selectedScenarioId) || gateScenarios[0];
  const result = evaluateGateScenario(selectedScenario);
  const firstBlocker = result.blockers[0];

  return (
    <section>
      <SectionHeader
        icon={<ShieldCheck />}
        title="Certificate Gate Command Center"
        text="Premium compliance gate engine for certificate integrity, optional-support separation, and audit-ready decisions."
      />
      <div className="command-hero">
        <div>
          <p className="eyebrow">Compliance Gate Engine</p>
          <h2>We are not just building training. We are building certificate integrity.</h2>
          <p>
            The system prevents premature certificates, separates optional clinical support from required online CE
            progress, and gives admins an audit-ready explanation of every certificate decision.
          </p>
          <div className="button-row">
            <button onClick={() => setView("audit")}>View Audit Evidence Preview</button>
            <button className="secondary" onClick={() => setView("certificate")}>Open Certificate Status</button>
          </div>
        </div>
        <div className={result.available ? "decision-card available" : "decision-card blocked"}>
          <p className="eyebrow">Selected scenario</p>
          <h3>{selectedScenario.name}</h3>
          <strong>{result.available ? "Mock Certificate Available - Prototype Only" : "Certificate Locked"}</strong>
          <p>
            {result.available
              ? "All required online CE gates pass. Optional clinical support is shown separately and excluded from gate computation."
              : `Certificate cannot release because ${firstBlocker?.label || "a required gate"} is incomplete.`}
          </p>
        </div>
      </div>

      <div className="command-card-grid">
        {executiveCards.map((card) => (
          <article className="panel command-card" key={card.title}>
            <h3>{card.title}</h3>
            <p>{card.text}</p>
          </article>
        ))}
      </div>

      <div className="command-layout">
        <article className="panel scenario-panel">
          <div className="panel-heading">
            <div>
              <p className="eyebrow">Scenario switcher</p>
              <h3>Certificate Decision Simulator</h3>
            </div>
            <span className={result.available ? "pill pass" : "pill fail"}>{result.available ? "Available" : "Blocked"}</span>
          </div>
          <div className="scenario-button-grid">
            {gateScenarios.map((scenario) => (
              <button
                className={scenario.id === selectedScenario.id ? "scenario-button active" : "scenario-button"}
                key={scenario.id}
                onClick={() => setSelectedScenarioId(scenario.id)}
              >
                {scenario.name}
              </button>
            ))}
          </div>
          <div className="scenario-summary">
            <h4>{selectedScenario.name}</h4>
            <p>{selectedScenario.summary}</p>
            {result.available ? (
              <div className="feedback good">No required-gate blockers. Certificate preview can be shown as mock/staged only.</div>
            ) : (
              <div className="feedback bad">
                {result.blockers.map((blocker) => (
                  <p key={blocker.key}>Certificate cannot release because {blocker.label} is incomplete.</p>
                ))}
              </div>
            )}
          </div>
        </article>

        <aside className="panel boundary-panel">
          <p className="eyebrow">Excluded from gate</p>
          <h3>Optional Clinical Support Boundary</h3>
          <p>
            Support activities are visible for learner help and operations, but they do not count as online CE
            certificate requirements unless written approval changes the rule.
          </p>
          <div className="boundary-list">
            {optionalClinicalBoundaryRows.map((row) => (
              <div className="boundary-row" key={row.key}>
                <span>{row.label}</span>
                <strong>{selectedScenario.optionalClinical[row.key] ? "Viewed" : "Skipped"}</strong>
              </div>
            ))}
          </div>
          <div className="notice strong">Optional clinical support is not inside certificate gate computation.</div>
        </aside>
      </div>

      <div className="command-layout">
        <article className="panel">
          <div className="panel-heading">
            <div>
              <p className="eyebrow">Required gates only</p>
              <h3>Gate Evaluation</h3>
            </div>
            <span className="tag">Prototype only</span>
          </div>
          <div className="gate-list">
            {gateDefinitions.map((gate) => (
              <GateRow
                key={gate.key}
                gate={{
                  id: gate.key,
                  label: gate.label,
                  source: gate.source,
                  pass: selectedScenario.gates[gate.key],
                }}
              />
            ))}
          </div>
        </article>

        <aside className="panel">
          <p className="eyebrow">Audit packet tie-in</p>
          <h3>Evidence Categories</h3>
          <div className="evidence-list">
            {gateAuditEvidence.map((item) => (
              <span className="tag" key={item}>{item}</span>
            ))}
          </div>
          <button onClick={() => setView("audit")}>View Audit Evidence Preview</button>
          <details className="content-details">
            <summary>Stakeholder Demo Script</summary>
            <p>{stakeholderDemoScript}</p>
          </details>
        </aside>
      </div>

      <article className="certificate-preview command-certificate">
        <div className="watermark">STAGING / PROTOTYPE ONLY - NOT A LIVE CE CERTIFICATE</div>
        <h2>{result.available ? "Mock Certificate Available - Prototype Only" : "Certificate Locked"}</h2>
        <p>Scenario: {selectedScenario.name}</p>
        <p>
          {result.available
            ? "Required certificate gates are complete in this scenario. This remains a mock/staged preview only."
            : `Blocked required gates: ${result.blockers.map((blocker) => blocker.label).join(", ")}`}
        </p>
        <p>Optional clinical support is excluded from this certificate decision.</p>
      </article>
    </section>
  );
}

function ClinicalHub() {
  return (
    <section>
      <SectionHeader icon={<Stethoscope />} title="Optional Clinical Support Hub" text="Separate support pathway. Non-credit by default and not an online CE certificate gate." />
      <div className="clinical-hero">
        <div className="clinical-visual" aria-label="CNA clinical support visual" />
        <div className="panel">
          <p className="eyebrow">Optional support boundary</p>
          <h3>Helpful support, never a certificate gate</h3>
          <p>
            Skipping optional clinical support, uploads, confidence checks, simulation, scheduling, or RN/preceptor signoff
            must not block the online CE certificate when required theory gates are complete.
          </p>
          <div className="tag-row">
            <span>Non-credit support</span>
            <span>No PHI</span>
            <span>Non-gating</span>
          </div>
        </div>
      </div>
      <div className="module-grid">
        {clinicalSupportSections.map((item) => (
          <article className="module-card" key={item.title}>
            <h3>{item.title}</h3>
            <p>{item.description}</p>
            <span className="tag">Optional clinical support - not clinical-hour credit</span>
            <p className="source-note">{item.status}</p>
            <details className="content-details">
              <summary>Seeded support content</summary>
              <ul>
                {item.bullets.map((bullet) => (
                  <li key={bullet}>{bullet}</li>
                ))}
              </ul>
              <p className="source-note">Source: {item.sourcePath}</p>
              {item.reviewFlags?.map((flag) => (
                <div className="notice" key={flag}>{flag}</div>
              ))}
            </details>
            {item.phiWarning && <PhiWarning />}
          </article>
        ))}
      </div>
      <article className="panel">
        <h3>Documentation Support Mockup</h3>
        <PhiWarning />
        <label>
          Free-text support note using fictional/de-identified details only
          <textarea placeholder="Do not type patient or resident identifiers. Use fictional practice notes only." />
        </label>
        <button className="secondary">Mock upload disabled</button>
      </article>
    </section>
  );
}

function AuditPreview({ state, gates }: { state: LearnerState; gates: Gate[] }) {
  return (
    <section>
      <SectionHeader icon={<ClipboardCheck />} title="Audit Packet Preview" text="Shows what would be exported from the Moodle review environment. No real evidence files are created." />
      <div className="audit-grid">
        {auditItems.map((item) => (
          <article className="panel compact" key={item.id}>
            <h3>{item.label}</h3>
            <p>{item.source}</p>
            <span className="tag">{item.bucket}</span>
          </article>
        ))}
      </div>
      <article className="panel">
        <h3>Seeded Source Inventory</h3>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Source</th>
                <th>Topic</th>
                <th>Status / flags</th>
                <th>Used</th>
              </tr>
            </thead>
            <tbody>
              {sourceInventory.map((item) => (
                <tr key={`${item.path}-${item.topic}`}>
                  <td>{item.path}</td>
                  <td>{item.topic}</td>
                  <td>{item.status}<br /><span className="source-note">{item.flags}</span></td>
                  <td>{item.used ? "Yes" : "No"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </article>
      <div className="panel">
        <h3>Prototype Evidence Snapshot</h3>
        <pre>{JSON.stringify({ learnerProfile: maskProfile(state), gates: gates.map(({ label, pass }) => ({ label, pass })) }, null, 2)}</pre>
      </div>
    </section>
  );
}

function MoodleMigrationMap() {
  return (
    <section>
      <SectionHeader icon={<Map />} title="Moodle Migration Map" text="Standalone features mapped to future Moodle tools, evidence, gate status, and risks." />
      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Standalone feature</th>
              <th>Moodle equivalent</th>
              <th>Evidence generated</th>
              <th>Gate</th>
              <th>Notes / risks</th>
            </tr>
          </thead>
          <tbody>
            {moodleMap.map((row) => (
              <tr key={row.feature}>
                <td>{row.feature}</td>
                <td>{row.moodle}</td>
                <td>{row.evidence}</td>
                <td>{row.gate}</td>
                <td>{row.risk}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

function ReviewNotes() {
  return (
    <article className="panel review-notes">
      <h3>Review Environment Status</h3>
      <div className="three-col">
        <InfoBlock icon={<ShieldAlert />} title="Standalone Review Build" text="Vite/React review experience. Moodle launch migration is still pending." />
        <InfoBlock icon={<Lock />} title="Gate Simulation" text="Active-time validation is simulated only; Moodle plugin validation is not complete." />
        <InfoBlock icon={<Stethoscope />} title="Optional Support" text="Clinical support is non-gating, non-credit, and separated from required online CE progress." />
      </div>
      <div className="notice strong">No PHI, no real learner records, and no live certificate issuance in this review build.</div>
    </article>
  );
}

function DemoUserProfilePanel({
  profile,
  updateProfile,
  resetDemoProfile,
  unlockMode,
  setUnlockMode,
}: {
  profile: DemoUserProfile;
  updateProfile: <K extends keyof DemoUserProfile>(key: K, value: DemoUserProfile[K]) => void;
  resetDemoProfile: () => void;
  unlockMode: boolean;
  setUnlockMode: (enabled: boolean) => void;
}) {
  return (
    <article className="panel">
      <div className="panel-heading">
        <div>
          <p className="eyebrow">Stakeholder review profile</p>
          <h3>Demo User Profile</h3>
        </div>
        <span className="tag">{profile.reviewStatus}</span>
      </div>
      <p className="source-note">
        Fictional/test data only. Edits update visible dashboard/profile and certificate profile gates in review
        state; they do not create a real learner record.
      </p>
      <div className="form-grid">
        <label>
          Legal first name
          <input value={profile.legalFirstName} onChange={(event) => updateProfile("legalFirstName", event.target.value)} />
        </label>
        <label>
          Legal last name
          <input value={profile.legalLastName} onChange={(event) => updateProfile("legalLastName", event.target.value)} />
        </label>
        <label>
          Email
          <input value={profile.email} onChange={(event) => updateProfile("email", event.target.value)} />
        </label>
        <label>
          CNA certificate number
          <input value={profile.cnaNumber} onChange={(event) => updateProfile("cnaNumber", event.target.value)} />
        </label>
        <label>
          Course cohort
          <input value={profile.courseCohort} onChange={(event) => updateProfile("courseCohort", event.target.value)} />
        </label>
        <label>
          Phone
          <input value={profile.phone} onChange={(event) => updateProfile("phone", event.target.value)} />
        </label>
        <label>
          Renewal cycle
          <input value={profile.renewalCycle} onChange={(event) => updateProfile("renewalCycle", event.target.value)} />
        </label>
        <label>
          Organization
          <input value={profile.organization} onChange={(event) => updateProfile("organization", event.target.value)} />
        </label>
        <label>
          Location
          <input value={profile.location} onChange={(event) => updateProfile("location", event.target.value)} />
        </label>
      </div>
      <label>
        Notes
        <textarea value={profile.notes} onChange={(event) => updateProfile("notes", event.target.value)} />
      </label>
      <div className="button-row">
        <button className="secondary" onClick={resetDemoProfile}>Reset to James Bond Review User</button>
        <label className="switch-row">
          <input type="checkbox" checked={unlockMode} onChange={(event) => setUnlockMode(event.target.checked)} />
          <span>Stakeholder Unlock Mode</span>
        </label>
      </div>
      <div className="notice">
        Unlock Mode opens review screens for navigation only. It does not mark required gates complete, issue a
        certificate, or change learner completion unless QA controls are explicitly used.
      </div>
    </article>
  );
}

function QAPanel({
  state,
  setState,
  gates,
}: {
  state: LearnerState;
  setState: React.Dispatch<React.SetStateAction<LearnerState>>;
  gates: Gate[];
}) {
  return (
    <section>
      <SectionHeader icon={<HelpCircle />} title="Advanced Reviewer Tools" text="Internal controls for certificate-gate and optional-support non-gating checks." />
      <details className="panel reviewer-toolbox" open>
        <summary>Gate state controls</summary>
        <div className="button-row">
          <button onClick={() => setState(passAllState())}>Load passing required-theory learner</button>
          <button className="secondary" onClick={() => setState({ ...passAllState(), legalFirstName: "", legalLastName: "" })}>
            QA missing legal name
          </button>
          <button className="secondary" onClick={() => setState({ ...passAllState(), finalExamPassed: false, finalExamAttempted: true })}>
            QA failed exam
          </button>
          <button className="secondary" onClick={() => setState(initialState)}>Reset mock learner</button>
        </div>
      </details>
      <div className="reviewer-layout">
        <article className="panel">
          <h3>Current Gate Snapshot</h3>
          <div className="gate-list">
            {gates.map((gate) => (
              <GateRow key={gate.id} gate={gate} />
            ))}
          </div>
        </article>
        <aside className="panel">
          <h3>Internal Assertions</h3>
          <div className="notice">
            Optional clinical support skipped, optional upload missing, and simulation skipped are expected to remain
            non-blocking. Current optional state is intentionally not included in certificate gate computation.
          </div>
          <pre>{JSON.stringify(maskProfile(state), null, 2)}</pre>
        </aside>
      </div>
      <details className="panel reviewer-toolbox">
        <summary>Negative-test library</summary>
        <div className="audit-grid">
          {qaTests.map((test) => (
            <article className="panel compact" key={test.id}>
              <h3>{test.id}</h3>
              <p>{test.scenario}</p>
              <span className="tag">{test.expected}</span>
            </article>
          ))}
        </div>
      </details>
    </section>
  );
}

function SeededModuleDetails({ module }: { module?: SeededModuleContent }) {
  if (!module) return null;
  return (
    <details className="content-details">
      <summary>Seeded content, source, and review status</summary>
      <div className="source-box">
        <p><strong>Source:</strong> {module.sourcePath}</p>
        <p><strong>Source status:</strong> {module.sourceStatus}</p>
      </div>
      {module.reviewFlags.length > 0 && (
        <div className="flag-list">
          {module.reviewFlags.map((flag) => (
            <div className="notice" key={`${flag.kind}-${flag.note}`}>
              <strong>{flag.kind} review:</strong> {flag.note}
            </div>
          ))}
        </div>
      )}
      <h4>Learning objectives</h4>
      <ul>
        {module.objectives.map((objective) => (
          <li key={objective}>{objective}</li>
        ))}
      </ul>
      <h4>Lesson sections</h4>
      <div className="lesson-list">
        {module.lessonSections.map((section) => (
          <article className="content-item" key={section.title}>
            <p className="eyebrow">{section.minutes} min</p>
            <h4>{section.title}</h4>
            <p>{section.summary}</p>
            {section.sourceStatus && <p className="source-note">{section.sourceStatus}</p>}
          </article>
        ))}
      </div>
      {module.scenarioChecks.length > 0 && (
        <>
          <h4>Scenario/check content</h4>
          <div className="lesson-list">
            {module.scenarioChecks.map((check) => (
              <article className="content-item" key={check.title}>
                <h4>{check.title}</h4>
                <p>{check.prompt}</p>
                {check.correctAnswer && <p><strong>Expected answer:</strong> {check.correctAnswer}</p>}
                {check.feedback && <p><strong>Feedback:</strong> {check.feedback}</p>}
                {check.remediation && <p><strong>Remediation:</strong> {check.remediation}</p>}
                {check.sourceStatus && <p className="source-note">{check.sourceStatus}</p>}
              </article>
            ))}
          </div>
        </>
      )}
      <TranscriptBox title={`TTS / Transcript Placeholder: ${module.title}`} transcript={module.tts.transcriptSummary} status={module.tts.status} />
      <div className="source-box">
        <p><strong>Remediation:</strong> {module.remediation}</p>
        <p><strong>Moodle migration:</strong> {module.moodleNotes}</p>
      </div>
    </details>
  );
}

type Gate = { id: string; label: string; pass: boolean; source: string };

function computeGates(state: LearnerState): Gate[] {
  return [
    { id: "legal-name", label: "Legal name present", pass: hasLegalName(state), source: "Required profile fields" },
    { id: "cna", label: "CNA certificate number present", pass: Boolean(state.cnaNumber.trim()), source: "Required profile field" },
    { id: "cap", label: "Online cap acknowledgement complete", pass: state.onlineCapAck, source: "Module 0 acknowledgement" },
    { id: "theory", label: "Required theory complete", pass: state.orientationFinalAck && state.module1QuizPassed && state.remainingTheorySimulated, source: "Module completion simulation" },
    { id: "interaction", label: "Required interaction/feedback complete", pass: state.phiAck && state.module1Interaction, source: "Module 0/1 interactions" },
    { id: "time", label: "Active-time threshold met, simulated only", pass: state.activeTimeMet, source: "Review toggle; Moodle validation pending" },
    { id: "exam", label: "Final exam/test passed", pass: state.finalExamPassed, source: "Mock final exam preview" },
    { id: "affidavit", label: "Final statement/affidavit complete", pass: state.affidavitComplete, source: "Draft affidavit review screen" },
    { id: "fields", label: "Required certificate fields populated", pass: state.certificateFieldsPopulated, source: "Certificate field map placeholder" },
    { id: "hold", label: "Admin hold clear", pass: state.adminHoldClear, source: "Manual hold placeholder" },
  ];
}

function getNextStep({
  state,
  module0Complete,
  module1Complete,
  theoryComplete,
  examUnlocked,
}: {
  state: LearnerState;
  module0Complete: boolean;
  module1Complete: boolean;
  theoryComplete: boolean;
  examUnlocked: boolean;
}) {
  if (!module0Complete) return { label: "Complete Module 0", note: "Identity, online cap, no-PHI, and orientation acknowledgements are required.", action: "Open Module 0", view: "module0" as View };
  if (!module1Complete) return { label: "Complete Module 1 review", note: "Finish the infection control scenario and module quiz review.", action: "Open Module 1", view: "module1" as View };
  if (!state.remainingTheorySimulated) return { label: "Simulate remaining theory completion", note: "Modules 2-6 are seeded for review, but this standalone build still uses a review completion toggle.", action: "Open Reviewer Tools", view: "qa" as View };
  if (!state.activeTimeMet) return { label: "Meet active participation gate", note: "This is simulated only; Moodle active-time validation remains pending.", action: "Open Reviewer Tools", view: "qa" as View };
  if (!examUnlocked || !state.finalExamPassed) return { label: "Pass final exam/test preview", note: "Mock questions only; approved question bank still required.", action: "Open Final Exam", view: "exam" as View };
  if (!state.affidavitComplete) return { label: "Complete final statement", note: "Draft affidavit pending legal/CDPH approval.", action: "Open Affidavit", view: "affidavit" as View };
  return { label: "Review certificate gate status", note: "Mock certificate preview is unlocked but not a live CE certificate.", action: "Open Certificate Status", view: "certificate" as View };
}

function setExam(update: <K extends keyof LearnerState>(key: K, value: LearnerState[K]) => void, pass: boolean) {
  update("finalExamAttempted", true);
  update("finalExamPassed", pass);
}

function passAllState(): LearnerState {
  return {
    legalFirstName: defaultDemoProfile.legalFirstName,
    legalLastName: defaultDemoProfile.legalLastName,
    cnaNumber: defaultDemoProfile.cnaNumber,
    onlineCapAck: true,
    phiAck: true,
    orientationFinalAck: true,
    module1Interaction: true,
    module1QuizPassed: true,
    remainingTheorySimulated: true,
    activeTimeMet: true,
    finalExamAttempted: true,
    finalExamPassed: true,
    affidavitComplete: true,
    certificateFieldsPopulated: true,
    adminHoldClear: true,
  };
}

function hasLegalName(state: LearnerState) {
  return Boolean(state.legalFirstName.trim() && state.legalLastName.trim());
}

function percent(values: boolean[]) {
  return Math.round((values.filter(Boolean).length / values.length) * 100);
}

function maskProfile(state: LearnerState) {
  return {
    legalNamePresent: hasLegalName(state),
    cnaNumberPresent: Boolean(state.cnaNumber.trim()),
    onlineCapAck: state.onlineCapAck,
    phiAck: state.phiAck,
    optionalClinicalProgressExcluded: true,
  };
}

function SectionHeader({ icon, title, text }: { icon: React.ReactNode; title: string; text: string }) {
  return (
    <div className="section-header">
      <div className="icon-badge">{icon}</div>
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
    </div>
  );
}

function InfoBlock({ icon, title, text }: { icon: React.ReactNode; title: string; text: string }) {
  return (
    <article className="info-block">
      <div className="icon-badge">{icon}</div>
      <h3>{title}</h3>
      <p>{text}</p>
    </article>
  );
}

function ProgressPanel({ title, value, note }: { title: string; value: number; note: string }) {
  return (
    <article className="panel">
      <h3>{title}</h3>
      <div className="progress-bar" aria-label={`${title}: ${value}%`}>
        <span style={{ width: `${value}%` }} />
      </div>
      <p className="progress-value">{value}%</p>
      <p>{note}</p>
    </article>
  );
}

function StatusPill({ pass, label }: { pass: boolean; label: string }) {
  return <span className={pass ? "pill pass" : "pill fail"}>{pass ? <CheckCircle2 /> : <Lock />} {label}</span>;
}

function GateRow({ gate }: { gate: Gate }) {
  return (
    <div className="gate-row">
      <span className={gate.pass ? "gate-icon pass" : "gate-icon fail"}>{gate.pass ? <CheckCircle2 /> : <Lock />}</span>
      <div>
        <strong>{gate.label}</strong>
        <p>{gate.source}</p>
      </div>
    </div>
  );
}

function CheckBox({
  checked,
  onChange,
  label,
  disabled,
}: {
  checked: boolean;
  onChange: (checked: boolean) => void;
  label: string;
  disabled?: boolean;
}) {
  return (
    <label className="check-row">
      <input type="checkbox" checked={checked} disabled={disabled} onChange={(event) => onChange(event.target.checked)} />
      <span>{label}</span>
    </label>
  );
}

function LockNotice({ text }: { text: string }) {
  return (
    <div className="lock-notice">
      <Lock />
      <span>{text}</span>
    </div>
  );
}

function PhiWarning() {
  return (
    <div className="phi-warning">
      <AlertTriangle />
      <span>
        No PHI: do not upload or type patient/resident names, faces, medical record numbers, dates of birth,
        addresses, chart screenshots, medication records, or identifying details.
      </span>
    </div>
  );
}

function TranscriptBox({ title, transcript, status }: { title: string; transcript?: string; status?: string }) {
  return (
    <article className="panel transcript">
      <h3>{title}</h3>
      <p>
        {status ||
          "Optional audio would appear here only after approved cloned-voice authorization, approved script review, and transcript pairing. Audio is pending and not generated in this MVP."}
      </p>
      <details>
        <summary>Transcript panel</summary>
        <p>
          {transcript ||
            "This transcript placeholder shows where text equivalent narration would be retained for accessibility, low-bandwidth use, and audit/version review."}
        </p>
      </details>
    </article>
  );
}

createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
