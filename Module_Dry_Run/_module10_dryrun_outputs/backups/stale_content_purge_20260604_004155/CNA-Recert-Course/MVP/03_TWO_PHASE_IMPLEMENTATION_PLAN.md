# 03 — Two-Phase Implementation Plan

Phase 1 = **MVP stabilization + redesign foundation** (stakeholder-demo ready).
Phase 2 = **Full asynchronous delivery completion + evidence readiness** (learner-pilot ready).

The sign-in/login page is **approved and frozen** in both phases.

---

## PHASE 1 — Stabilization & Redesign Foundation

### Objective
Convert the messy, checkbox-driven prototype into a clean, routed, dark-cinematic guided page-view system with one fully working prototype module (Infection Control), while preserving every existing compliance guardrail.

### Scope (in)
- Componentize the monolith + add routing + persisted state.
- Apply Dark Premium Cinematic design system + desktop and mobile shells.
- Remove the task/checkbox interface from the learner path.
- Rebuild Dashboard (command center), Course/Landing, Modules, Module Detail, and the Lesson/Player **foundation**.
- Certificate Status + Gate Center **foundation** (read from one unified gate model).
- Enforce required/optional separation + pinned No-PHI blocks.
- Build **Module 1** end-to-end as the prototype using the Standard Lesson Template.
- Fix asset paths; build/preview verification; demo negative-test pass.

### Out of scope (Phase 1)
- Converting all modules (2–6) to micro-lessons.
- Real active-time heartbeat engine (visual placeholder only; logic clearly "simulated").
- Real 25/50 exam engine, TTS audio, full audit export, Moodle map polish.
- Module 3 source repair; production certificate issuance; e-signature method.

### Workstreams → Step-by-step tasks
1. **Architecture (A-01→A-06)**
   1. Scaffold `src/{app,pages,components,features,lib,data}`; extract each view to a page file.
   2. Add React Router; map URLs (`/`, `/dashboard`, `/modules`, `/modules/:id`, `/lesson/:moduleId/:lessonId`, `/certificate`, `/gate-center`, `/clinical`, `/audit`, `/moodle`); add guards for locked routes.
   3. Lift `LearnerState` into a typed store with localStorage persistence; add "Resume".
   4. Move stock/brand images into `public/brand/**`; rewrite `stockImages` to `/brand/...`.
   5. Unify gate logic into `lib/gates.ts`; delete the duplicate model.
   6. Add ESLint/Prettier + `lint`/`typecheck` scripts.
2. **Design system (B-01→B-07)** — tokens, type scale, contrast pass, component library, desktop top nav + mobile bottom nav, status-badge system, focus ring.
3. **Task-interface replacement (C-01)** — strip evidence checkboxes from learner pages; relocate all gate toggles to Reviewer Tools.
4. **Core pages (C-02→C-07, E-01→E-03, E-06)** — Dashboard, Landing, Modules, Module Detail, Lesson/Player shell, Certificate Status, Gate Center foundation, separation + PHI blocks.
5. **Prototype module (D-01)** — render Module 1 with full Standard Lesson Template from data; completion driven by viewing + a single real knowledge check (not a checkbox).
6. **Verification (A-04, G-03)** — `npm run build` + preview; negative-test pass; cross-device smoke.

### Files likely affected (Phase 1)
- New: `src/app/router.tsx`, `src/lib/{gates.ts,store.ts,activeTime.ts(stub)}`, `src/components/{AppShell,TopNav,BottomNav,Card,StatusBadge,Progress,GateRow,PhiWarning,LessonCard}.tsx`, `src/pages/{Landing,Dashboard,Modules,ModuleDetail,LessonPlayer,Certificate,GateCenter,ClinicalHub,Audit,MoodleMap,ReviewerTools}.tsx`.
- Modified: `src/main.tsx` (reduced to bootstrap), `src/styles.css` (tokenized; likely split into `styles/` later), `src/data/*` (typed; M1 lesson body enriched), `public/brand/**`, `vite.config.ts` (aliases).
- Untouched: `ReviewerLogin` + `api/demo-login.ts` (approved).

### Deliverables
Routed, componentized app; cinematic design system; 6 redesigned core pages; Module 1 prototype lesson; unified gate model; passing build + negative tests; demo script.

### Acceptance criteria
- Every page has a URL; refresh preserves progress; locked routes redirect.
- No learner-facing checkbox sets completion; reviewer toggles only in Reviewer Tools.
- Dashboard "Next Up" routes to the correct next required step; Required vs Optional rings visually separated and Optional never affects readiness.
- Module 1 renders all Standard Lesson Template sections and completes via a real knowledge check.
- Core screens use cinematic tokens, pass AA contrast, and have mobile bottom nav with 44px targets.
- `npm run build` succeeds; all images load in preview.

### QA checks (Phase 1)
- Negative tests QA-002…QA-009 (cert blocked per failing gate), QA-011/013/014 (optional non-gating), QA-018 (PHI warning visible).
- Keyboard-only traversal of core pages; visible focus ring.
- Mobile smoke on small viewport (no horizontal scroll; bottom nav reachable).

### Risks (Phase 1)
- Refactor regression of gate behavior → mitigate with G-03 negative tests run continuously.
- Contrast failures in dark mode → run B-02b plugin audit before demo.
- Scope creep into Phase 2 features → enforce out-of-scope list.

### Exit criteria
Stakeholders can navigate the full guided page system on desktop + mobile, see the cinematic redesign, complete Module 1 as a real lesson, and watch the certificate stay correctly locked/unlocked — with all compliance guardrails intact and no checkbox task interface.

---

## PHASE 2 — Async Delivery Completion & Evidence Readiness

### Objective
Complete the asynchronous learning system: all modules as micro-lessons with checks/feedback, a real active-time engine, a real final-exam flow, full certificate/gate logic UI, the optional clinical hub, audit evidence view, Moodle map, and mobile/accessibility QA — pilot- and audit-ready.

### Scope (in)
- Convert all module content (0,2,4,5,6; then 3 after source repair) into 3–5 min micro-lessons.
- Port real per-module knowledge checks + scenario cards + feedback/remediation.
- Build the active-time engine (heartbeat, idle pause, time-gated Next).
- Build real final exam (25/50 randomized, 80% pass, attempt logging, no answer reveal).
- Complete certificate path + Gate Center plain-English rows + audit-packet tie-in.
- Complete Clinical Support Hub (CS-1…CS-7) as walled-off sandbox.
- Complete Audit evidence view (required vs optional, trail timeline, exports).
- Complete Moodle Map stakeholder view.
- Full mobile + WCAG 2.2 AA QA; optional TTS/transcript.
- Final stakeholder-ready documentation.

### Out of scope (Phase 2)
- Production Moodle migration/build (separate program; this app maps to it).
- Real certificate issuance / NAC# go-live / final e-signature legal decision (flagged, not enabled).
- Advanced branching simulations, neural-voice production at scale, offline mode (P3).

### Workstreams → Step-by-step tasks
1. **Content conversion (D-02, G-05)** — ID re-chunks modules into micro-lessons; SME signs off M1 gap, M5 skin, M3 repair; port lesson bodies from `Content/theory/modules/*` into typed data.
2. **Checks & feedback (D-03, D-04, D-05)** — implement WCAG-safe H5P-equivalent check components; wire 6 KCs/module; scenario cards; explanatory non-punitive feedback; remediation routing.
3. **Active-time (D-06)** — heartbeat + idle modal + time-gated Next + accrual logging; surface subtle indicator; reviewer can inspect accrued time.
4. **Assessment (E-04, E-05)** — randomized exam engine; lock until prereqs; affidavit gate after pass; flag e-signature as unresolved.
5. **Compliance surfaces (E-02, F-01, F-02, E-06)** — Gate Center rows; Clinical Hub sandbox; Audit master-detail + timeline + exports; PHI blocks everywhere.
6. **Roadmap surface (F-03)** — Moodle Map executive view.
7. **QA + a11y (G-01, G-02, A-07)** — full audit, mobile matrix, automated tests.
8. **Docs (G-04)** — final MVP doc set + designer/content handoffs.

### Files likely affected (Phase 2)
- New: `src/features/{activeTime,knowledgeCheck,exam,remediation}/*`, `src/components/{ScenarioCard,KnowledgeCheckCard,FeedbackState,TranscriptPanel,AuditTrail,ExportButtons}.tsx`, `src/data/{module1..module6}.ts` (full lesson bodies), `src/data/examPool.ts`, test files under `tests/`.
- Modified: `LessonPlayer`, `GateCenter`, `Certificate`, `ClinicalHub`, `Audit`, `MoodleMap`, styles.

### Deliverables
All theory modules deliverable as micro-lessons; working active-time + exam + certificate/gate logic; complete Clinical Hub, Audit, Moodle Map; passing a11y + mobile QA; automated tests; final documentation set.

### Acceptance criteria
- Every module completes via real content consumption + KC pass + active-time threshold (no manual toggles in learner path).
- Optional clinical support, when fully skipped, still yields certificate readiness once required gates pass.
- Final exam randomizes, requires 80%, logs attempts, hides answers post-submit, and is locked until theory + active-time are met.
- Audit view cleanly separates required vs optional evidence and shows a timestamped trail with PDF/CSV export affordances.
- WCAG 2.2 AA audit passes; mobile matrix (SE→15 Pro) passes; CI tests green.

### QA checks (Phase 2)
- Active-time: idle pauses timer; Next stays disabled until time+interaction; tab-away does not accrue time.
- Exam: retake shows different items; pass/fail logged; answers never revealed.
- Full negative-test suite + a11y + mobile matrix.

### Risks (Phase 2)
- Module 3 source remains unrepaired → keep it visibly flagged/locked; do not ship incomplete clinical content.
- Active-time accuracy disputes → document algorithm + thresholds; align with future Moodle plugin (Dedication/Timestat).
- Exam item validity (M1 gap, skin items) → gate exam go-live on SME sign-off.
- TTS redundancy/version drift → lock text before audio; pair transcripts.

### Exit criteria
A pilot learner can log in, complete all required theory as micro-lessons with checks and validated active time, pass the final exam, complete the affidavit, and see certificate readiness unlock — generating defensible, audit-ready evidence — while optional clinical support remains fully separate and non-gating, on both desktop and mobile, meeting WCAG 2.2 AA.
