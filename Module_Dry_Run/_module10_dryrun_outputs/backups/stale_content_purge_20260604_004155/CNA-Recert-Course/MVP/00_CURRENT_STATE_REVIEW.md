# 00 — Current State Review

**Project:** CNA Recertification Theory + Clinical Support MVP — CI Institute of Nursing
**Review mode:** Review + Planning only (no source code modified in this pass)
**Date:** 2026-05-28

---

## 0. Preflight Verification

| # | Check | Result |
|---|-------|--------|
| 1 | Current working directory | `C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\CNA-Recert-Course` ✅ matches required guardrail path |
| 2 | Git branch | `main` |
| 3 | `package.json` present | Not in `CNA-Recert-Course`. The runnable app lives in the **sibling** folder `../standalone-course-mvp` (`standalone-course-mvp/package.json` v0.1.0) |
| 4 | Framework / package manager | **React 19 + Vite 7 + TypeScript 5.9**, npm (package-lock.json present). Icons via `lucide-react`. No router, no state library, no test runner |
| 5 | Top-level structure of `CNA-Recert-Course` | `Branding_Kit/`, `CNA_Modules/`, `Content/`, `MVP/`, `PHASE_5_BUILD_SPEC_PACKET/`, plus `FINAL_UNIFIED_IMPLEMENTATION_BLUEPRINT.md`, `PHASE_0_COMPLIANCE_FOUNDATION.md`, `PHASE_2/3/4` reports |
| 6 | `Content/` folder exists | ✅ Yes — `theory/`, `clinical-support/`, `exam/`, `csv/`, `index/`, `qa/`, `source-verification/`, `Raw/` plus 18 numbered package docs |
| 7 | `MVP/` output folder exists | ✅ Yes — contained the two attached docs; now also holds these 11 generated deliverables |
| 8 | Reference docs accessible | ✅ `CNA Recertification MVP UI_UX Research.md` and `CNA Recertification Asynchronous Training Blueprint.md` both read in full |
| 9 | App architecture type | **Standalone single-page React/Vite prototype** with Moodle-migration mapping baked in as a stakeholder view. It is *not* a Moodle export; it is a review/demo SPA that anchors to the Phase 5 build packet and mirrors future Moodle activities |

Guardrail satisfied: repo path matches. Review proceeded.

---

## 1. Application Architecture (as built)

```
standalone-course-mvp/
├── index.html
├── package.json            # react 19, react-dom 19, lucide-react, vite 7, typescript 5.9
├── vite.config.ts
├── vercel.json             # Vite build + dist output
├── api/demo-login.ts       # Vercel Function: stakeholder demo credential gate
├── public/brand/           # logos, favicons, stock imagery (the canonical asset home)
└── src/
    ├── main.tsx            # 2,731 lines — ENTIRE app (shell + all 12 views + helpers)
    ├── styles.css          # 4,173 lines — single global stylesheet
    ├── vite-env.d.ts
    └── data/
        ├── courseData.ts                 # derives module list (+ "final") from moduleContent
        ├── moduleContent.ts              # 441 lines — seeded m0–m6 content + exam preview
        ├── clinicalSupportContent.ts     # 10 optional support sections
        ├── gateCommandCenterData.ts      # 11 gate definitions + 12 scenarios
        └── auditAndMigrationData.ts       # audit items, source inventory, Moodle map, QA tests
```

### 1.1 Routing structure
- **No router library.** Navigation is a single `useState<View>` in `App()`. `View` is a union of 13 string keys: `landing | dashboard | module0 | module1 | modules | exam | affidavit | certificate | gateCenter | clinical | audit | moodle | qa`.
- The header `primaryNav` array drives the top nav; `module1` view is reused to render **all** of Modules 1–6 by swapping `selectedModuleId`.
- **Consequence:** no URLs, no deep links, no browser back/forward, no shareable lesson state, no route guards. Everything is in-memory and resets on refresh.

### 1.2 Page views present
| View key | Component | Purpose | Maturity |
|----------|-----------|---------|----------|
| `landing` | `Landing` | Course intro hero + gate preview + module rail | Works (partial; depends on broken image paths) |
| `dashboard` | `Dashboard` | "Next required step", required vs optional progress, gate summary, reviewer profile drawer | Works |
| `modules` | `ModuleCatalog` | Module card grid w/ progress + status | Works |
| `module0` | `TrainingShell` (m0) | Orientation: identity fields + 3 acknowledgements | Works (real flow) |
| `module1` | `TrainingShell` (m1…m6) | Lesson rail + lesson canvas + context panel | Partial — see §3 |
| `exam` | `FinalExam` | Preview question cards + simulate pass/fail buttons | Mock only |
| `affidavit` | `Affidavit` | Draft attestation checkbox | Mock only |
| `certificate` | `Certificate` | Gate status, integrity checklist, mock certificate watermark | Works (mock) |
| `gateCenter` | `GateCommandCenter` | Scenario simulator over 11 gates + optional boundary | Works (strong) |
| `clinical` | `ClinicalHub` | Optional support tools, featured case, PHI warnings | Works (mock) |
| `audit` | `AuditPreview` | Audit items, source inventory table, JSON snapshot | Works |
| `moodle` | `MoodleMigrationMap` | Standalone→Moodle mapping table | Works |
| `qa` | `QAPanel` | Reviewer gate-state controls + negative tests | Works (internal) |

All 10 product pages the brief asks for **already exist in some form** — this is a redesign + depth problem, not a greenfield build.

### 1.3 Shared components
All components live inside `main.tsx`. Reusable primitives include: `StockImagePanel`, `SectionHeader`, `InfoBlock`, `ProgressBar`/`ProgressPanel`/`ModuleProgress`, `StatusPill`, `StatusBadge`, `GateRow`, `CheckBox`, `LockNotice`, `PhiWarning`, `TranscriptBox`, `ThemeToggle`. They are **not** exported to separate files, so they cannot be reused, unit-tested, or storybooked independently.

### 1.4 Data models
- `LearnerState` (16 booleans/strings) is the single source of truth for all gating: identity fields, `onlineCapAck`, `phiAck`, `orientationFinalAck`, `module1Interaction`, `module1QuizPassed`, `remainingTheorySimulated`, `activeTimeMet`, `finalExamAttempted/Passed`, `affidavitComplete`, `certificateFieldsPopulated`, `adminHoldClear`.
- `SeededModuleContent` (in `moduleContent.ts`) is well structured: `objectives[]`, `lessonSections[]` (title/minutes/summary/sourceStatus), `scenarioChecks[]` (prompt/choices/correctAnswer/feedback/remediation), `tts`, `reviewFlags[]`, `moodleNotes`.
- `computeGates(state)` returns 10 gates; `GateCommandCenter` uses a richer 11-gate model (`gateCommandCenterData.ts`) — **two parallel gate definitions exist** (drift risk).

### 1.5 Content loading approach
- Content is **hand-seeded summaries** in `moduleContent.ts`, *not* loaded from the `Content/` markdown source files. The `sourcePath` strings reference the real files but the app never reads them. Lesson "body" text is one-line `summary` fields, not the full lesson prose that exists in `Content/theory/modules/*`.
- `buildLessonSteps()` synthesizes a generic 5-part lesson spine for every module: Overview → (one step per lessonSection) → Scenario Check → Knowledge Check → Summary/Evidence.

### 1.6 Styling approach
- One 4,173-line `styles.css` with CSS custom properties and a `data-theme` light/dark toggle.
- **Current tokens are a LIGHT maroon/gold theme**: `--ci-primary: #8b1515`, `--ci-accent: #ffc107` (bright amber), `--ci-bg: #f8f9fa`, white surfaces. Fonts: Poppins + Open Sans + Montserrat.
- This **diverges from the target** "Dark Premium Cinematic" palette in the UI/UX research (`#121212` charcoal base, `#7A1026` oxblood, `#D2A84C` antique gold, `#F7EEDC` warm white, Serif display + Inter/Public Sans body). A dark theme variant exists via `data-theme` but is not the researched cinematic system.

### 1.7 Asset folders
- Canonical assets: `standalone-course-mvp/public/brand/{logos,favicons,images,stock}`.
- **Bug:** `stockImages` in `main.tsx` points most images to `../../CNA-Recert-Course/Branding_Kit/Stock/Student(s) (NN).png` — relative paths *outside* the Vite `public/` root. These will not resolve in a production build and several of those source files show as **deleted/untracked** in git status. Only `login` uses a valid `/brand/...` path. Result: landing/dashboard/lesson hero imagery is likely broken in build.

### 1.8 Build / test scripts
- `dev`: `vite --host 127.0.0.1` · `build`: `tsc && vite build` · `preview`: `vite preview`.
- **No test tooling** (no Vitest/Jest/Playwright config in package.json, though `playwright-login-*.png` screenshots exist at repo root and a `test-results/` folder is present). No lint config. No CI.

### 1.9 Login / sign-in (APPROVED — do not change)
- `ReviewerLogin` component + `reviewerCredentials = {admin/1234}` + `api/demo-login.ts` Vercel function with `DEMO_LOGIN_*` env fallback. This is the **approved** sign-in experience and is explicitly out of scope for redesign.

---

## 2. What Works / Partial / Broken / Missing

### ✅ Works (keep & re-skin)
- All 13 views render and are reachable from the top nav.
- **Gate Command Center** is the strongest asset: 11-gate model, 12 switchable scenarios, explicit optional-clinical-boundary rows, audit-evidence tie-in. This already embodies the "Gate Center" paradigm the research wants.
- **Required vs optional separation** is correctly modeled in logic (optional clinical is excluded from `computeGates` and from the dashboard required-progress ring).
- PHI warnings render before free-text/upload zones in the Clinical Hub.
- Certificate page renders a watermarked, non-issuable mock with field map + integrity checklist.
- Moodle map + audit source inventory are populated and accurate to the content package.
- Compliance footer + reviewer "Unlock Mode" (navigation-only, non-gating) are present.

### 🟡 Partial
- **Lesson player** exists (rail + canvas tabs: Lesson/Terms/Practice/Transcript/Evidence) but is generic and content-thin. It shows one-line summaries, not microlearning cards (Scenario → Key Concept → Why it Matters → Example → Common Mistake → Check → Feedback).
- **Modules 2–6** are not individually completable: their entire completion collapses into one shared `remainingTheorySimulated` checkbox toggled in Reviewer Tools. Their rich `scenarioChecks` data exists but is not wired to gates.
- **Knowledge checks**: only Module 1's scenario radio writes to a gate (`module1Interaction`); Module 1 quiz pass is a manual checkbox; other modules have no scored interaction.
- **Final exam**: 5 preview question cards + "simulate pass/fail" buttons; no real 25-of-50 randomized engine, no 80% scoring, no attempt logging.
- **Dark theme**: toggle exists but is the legacy theme, not the cinematic system.

### 🔴 Broken / risk
- Stock image paths (§1.7) resolve outside `public/` → likely broken images in build.
- Two divergent gate models (`computeGates` vs `gateDefinitions`) can drift.
- Completion is driven by **manual reviewer checkboxes** ("evidence states") rather than real content interaction — this is the "messy task interface" the brief calls out: the learner experience reads like an admin to-do list of toggles.

### ⛔ Missing
- React Router / URLs / deep links / persistence (state resets on reload).
- True **active-time tracking** (heartbeat, idle pause, time-gated Next button) — only a boolean exists.
- Mobile **bottom navigation** bar; current nav is desktop top-nav only.
- Real microlearning lesson rendering from `Content/` source markdown.
- Real knowledge-check / quiz engine with scoring, attempts, remediation routing.
- WCAG AA dark-mode contrast pass; status-not-by-color audit; keyboard focus styling per spec.
- Componentization (everything is one 2.7k-line file).
- Automated tests / lint / CI.

---

## 3. The "Messy Task Interface" — Root Cause

The brief's complaint maps to a concrete pattern: **learner progress is recorded by checking boxes** (`module1QuizPassed`, `remainingTheorySimulated`, evidence checkboxes, QA toggles) instead of by *doing the lesson*. The lesson workspace surfaces reviewer/evidence controls (Evidence tab, completion-control cards, "Reviewer evidence state" checkboxes) directly in the learner path. The redesign must:
1. Move all reviewer/evidence toggles into the existing hidden **Advanced Reviewer Tools** (`qa`) drawer only.
2. Replace box-checking with **real microlearning consumption + knowledge-check pass** as the completion driver.
3. Make Modules 2–6 first-class (each with its own lessons, checks, and completion), retiring the shared `remainingTheorySimulated` toggle for production logic.

---

## 4. Obvious Architectural Problems (prioritized)

| # | Problem | Impact | Fix phase |
|---|---------|--------|-----------|
| A1 | 2,731-line monolithic `main.tsx` | Unmaintainable; blocks parallel work, testing, reuse | Phase 1 |
| A2 | No routing / URLs / persistence | No deep links, no resume-after-refresh, no route guards | Phase 1 |
| A3 | Broken stock-image paths outside `public/` | Broken imagery in production build | Phase 1 |
| A4 | Completion via manual checkboxes in learner path | The "messy task interface"; compliance/UX risk | Phase 1 |
| A5 | Modules 2–6 share one completion toggle | Cannot deliver/complete real theory | Phase 1→2 |
| A6 | Legacy light theme ≠ cinematic dark system | Off-brief visual identity | Phase 1 |
| A7 | Two divergent gate models | Logic drift, audit inconsistency | Phase 1 |
| A8 | No active-time engine | Core CDPH audit evidence absent | Phase 2 |
| A9 | Content not loaded from `Content/` source | Lesson body is thin summaries | Phase 2 |
| A10 | No tests / lint / CI / a11y audit | Regression + accessibility risk | Phase 1→2 |

---

## 5. Summary Judgment

The MVP is **further along than "greenfield"**: all 10 target pages exist, the compliance/gate engine is genuinely strong, and required/optional separation is correctly modeled. The real work is (1) **re-skinning** to the dark cinematic system, (2) **replacing checkbox-driven completion** with a real microlearning lesson player, (3) **componentizing + routing** the monolith, (4) **promoting Modules 2–6** to first-class delivery, and (5) building the **active-time + knowledge-check** evidence engines. None of the existing compliance guardrails should be weakened in the process.
