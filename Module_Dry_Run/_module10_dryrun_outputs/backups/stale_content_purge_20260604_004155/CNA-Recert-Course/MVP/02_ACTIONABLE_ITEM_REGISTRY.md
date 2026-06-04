# 02 — Comprehensive Actionable Item Registry

**Priority:** P0 (blocks stakeholder demo) · P1 (blocks learner pilot) · P2 (polish) · P3 (future)
**Source codes:** Repo · Content · UIUX (UI/UX Research) · Async (Async Blueprint) · Compliance · Rec (recommendation)
**Owner roles:** PA=Product Architect · FE=React/Vite Eng · ID=Instructional Designer · CA=Compliance Analyst · UX=UI/UX Lead · TPM=Program Mgr · SME=Clinical Educator/RN

> Acceptance criteria are written to be testable. "Login page" is explicitly excluded from all redesign items.

---

## Workstream A — Repo Cleanup / Architecture

| ID | P | Page/Area | Action Item | Rationale | Source | Owner | Deps | Acceptance Criteria | Risk if not done | Phase |
|----|---|-----------|-------------|-----------|--------|-------|------|---------------------|------------------|-------|
| A-01 | P0 | Whole app | Split 2,731-line `main.tsx` into `src/{app,components,pages,features,lib,data}` modules | Monolith blocks reuse/testing/parallel work | Repo | FE/PA | — | No file >400 lines; each page/component in own file; build passes | Velocity collapse | 1 |
| A-02 | P0 | Routing | Introduce React Router with URL per view + route guards | No deep links/resume/back; needed for guided flow | Repo,UIUX | FE | A-01 | Each page has a URL; back/forward works; locked routes redirect | No shareable/resumable state | 1 |
| A-03 | P1 | State | Add persisted learner state (localStorage now; API later) + single typed store | State resets on refresh; no resume | Repo,UIUX | FE | A-01 | Refresh preserves progress; "Resume lesson" works | Learner loses progress | 1 |
| A-04 | P0 | Assets | Move all stock/brand images into `public/brand/**`; fix `stockImages` paths | Current `../../` paths break in build | Repo | FE | — | `npm run build` + preview shows all imagery; no 404s | Broken visuals in demo | 1 |
| A-05 | P1 | Gate model | Unify duplicate gate logic (`computeGates` vs `gateDefinitions`) into one module | Drift risk between two models | Repo,Compliance | FE/CA | A-01 | Single gate source consumed by Dashboard, Cert, Gate Center, Audit | Inconsistent gate decisions | 1 |
| A-06 | P1 | Tooling | Add ESLint + Prettier + typecheck in CI script | No lint/CI today | Repo | FE | A-01 | `npm run lint` + `tsc` clean in CI | Regressions ship | 1 |
| A-07 | P2 | Tooling | Add Vitest (unit) + Playwright (e2e) harness | No tests | Repo,Rec | FE | A-01 | Gate logic + core flow covered; CI green | Undetected breakage | 2 |

---

## Workstream B — Design System & App Shell

| ID | P | Page/Area | Action Item | Rationale | Source | Owner | Deps | Acceptance Criteria | Risk | Phase |
|----|---|-----------|-------------|-----------|--------|-------|------|---------------------|------|-------|
| B-01 | P0 | Tokens | Replace legacy light tokens with Dark Premium Cinematic tokens (`#121212`,`#1E1E1E`,`#7A1026`,`#5A0F1D`,`#D2A84C`,`#B7892B`,`#F7EEDC`,`#E0E0E0`,`#B0B0B0`) | Off-brief visual identity | UIUX | UX/FE | — | All core screens use tokens; no pure black; gold reserved for CTAs/active | Fails stakeholder buy-in | 1 |
| B-02 | P0 | Type | Dual-font scale: Serif display (Playfair/Lora) for h1–h3, Inter/Public Sans body ≥16px, line-height ≥1.5 | Institutional + legible | UIUX | UX/FE | B-01 | Heading/body styles defined; semantic h1→h3 mapping | Inconsistent type | 1 |
| B-02b | P1 | A11y | WCAG 2.2 AA contrast pass on all token pairings (4.5:1 text, 3:1 large) | Dark-mode contrast is #1 failure mode | UIUX,Compliance | UX | B-01 | Contrast plugin report attached; no failures | Legal/a11y exposure | 1 |
| B-03 | P0 | Shell | Desktop sticky top nav + max-1200px content; build component library (App Shell, Page Header, Card, Badge, Progress, Gate Row) | Reusable shell | UIUX | FE/UX | A-01,B-01 | Components used across ≥3 pages; states (hover/active/disabled) | Re-skin inconsistency | 1 |
| B-04 | P0 | Mobile shell | Persistent 4–5 icon bottom nav (Home/Modules/Certificate/Hub), 44×44px targets | Shift workers are mobile-first | UIUX,Async | FE/UX | B-03 | Bottom nav on <768px; targets ≥44px; one-handed reachable | Mobile abandonment | 1 |
| B-05 | P1 | Status system | Status Badge system: shape+icon+text (Complete/In Progress/Needs Review/Blocked/Optional) — never color-only | WCAG status-not-by-color | UIUX | UX/FE | B-03 | Each state has icon+label; passes color-blind check | A11y failure | 1 |
| B-06 | P2 | Glass | Standardized safe glassmorphism (blur ≤15px, 5–10% tint, 1px border, `@supports` flat fallback) | Perf + a11y safe depth | UIUX | FE/UX | B-03 | Applied only to progress/help panels; no scroll lag on mid devices | Perf/contrast risk | 2 |
| B-07 | P1 | Focus | Custom keyboard focus ring (2px `#D2A84C`, 2px offset); full keyboard nav | Default ring invisible on dark | UIUX,Compliance | FE | B-03 | Tab traversal reaches all controls with visible focus | Keyboard users blocked | 1 |

---

## Workstream C — Task Interface Replacement & Core Pages

| ID | P | Page/Area | Action Item | Rationale | Source | Owner | Deps | Acceptance Criteria | Risk | Phase |
|----|---|-----------|-------------|-----------|--------|-------|------|---------------------|------|-------|
| C-01 | P0 | All learner pages | Remove evidence/reviewer checkboxes from learner path; move ALL gate toggles into hidden Reviewer Tools only | This IS the "messy task interface" | UIUX,Compliance | FE/UX | A-01 | No learner-facing checkbox sets completion; QA panel holds toggles | Compliance/UX confusion | 1 |
| C-02 | P0 | Dashboard | Rebuild as command center: greeting → "Next Up" card (gold) → locked Certificate banner → Required CE progress ring → separate Optional progress | Answer "what now + how close" in 5s | UIUX | FE/UX | B-03 | "Next Up" routes to correct next required step; rings isolated | Decision fatigue | 1 |
| C-03 | P0 | Course/Landing | Two distinct pathway cards (12-hr Required CE vs Optional Support); No-PHI block; module progress strip; primary CTA above fold | Pathway clarity | UIUX,Compliance | FE/UX | B-03 | Required vs optional visually separated; CTA above fold mobile | Pathway blending | 1 |
| C-04 | P0 | Modules | Streaming-style module catalog cards: title, duration, linear progress, status badge; left mission/brand panel | Premium, not file directory | UIUX | FE/UX | B-03,B-05 | All 8 modules as cards w/ status; not Started/In Progress/Needs Review/Complete | Generic LMS feel | 1 |
| C-05 | P0 | Module Detail | Overview + learning goals + sequential lesson rows w/ locked/unlocked opacity + Start/Continue FAB | Bridge catalog→lesson | UIUX | FE/UX | C-04 | Lesson rows reflect real lesson list; locked future lessons dimmed | No clear entry | 1 |
| C-06 | P0 | Lesson/Player | 3-column desktop (left nav / center cards / right status+transcript+terms); mobile single-column w/ bottom sheet + sticky prev/next | Core execution env | UIUX,Async | FE/UX | C-05,D-01 | Renders microlearning cards; Next disabled until reqs met | "Document dump" | 1→2 |
| C-07 | P1 | Lesson nav icons | Lesson rail status icons: empty/half/solid-check + label (not color-only) | WCAG + endowed progress | UIUX,Async | UX/FE | C-06,B-05 | Three distinct shapes+labels per state | A11y status loss | 1 |

---

## Workstream D — Microlearning, Checks, Feedback, Active-Time

| ID | P | Page/Area | Action Item | Rationale | Source | Owner | Deps | Acceptance Criteria | Risk | Phase |
|----|---|-----------|-------------|-----------|--------|-------|------|---------------------|------|-------|
| D-01 | P0 | Lesson model | Implement Standard Lesson Template (Title/Time, Goal, Scenario, Key Concept, Why It Matters, Example, Common Mistake, Quick Check, Feedback, Key Terms, Transcript, Summary, Next) | Pedagogical consistency | Async | ID/FE | C-06 | Module 1 renders all template sections from data | Inconsistent lessons | 1 (M1) |
| D-02 | P1 | Microlearning | Re-chunk all modules into 3–5 min micro-lessons, ≤100–150 words/screen, 3–5 screens each | Cognitive load + microlearning | Async,Content | ID | D-01 | Each micro-lesson ≤5 min; word counts verified | Fatigue/drop-off | 2 |
| D-03 | P1 | Knowledge checks | Port real 6-KC sets per module; WCAG-safe types only (MC, Single Choice, True/False, Dialog Cards); one question per screen on mobile | Testing effect + a11y | Async,Content | ID/FE | D-01 | M1–M6 KCs scored; drag/drop & matching excluded | Weak retention/a11y | 2 |
| D-04 | P1 | Scenario cards | Distinct scenario card styling/iconography; each topic opens with clinical scenario | Scenario-based learning | Async,UIUX | UX/FE | D-01 | Scenario cards visually distinct from info cards | No clinical priming | 2 |
| D-05 | P1 | Feedback/remediation | Immediate explanatory, non-punitive feedback ("Not quite. Remember that…"); failed module quiz routes to specific chapter before retry | Feedback design | Async | ID/FE | D-03 | Correct/incorrect states show rationale; remediation link works | Misconceptions encoded | 2 |
| D-06 | P1 | Active-time | Active-time engine: heartbeat (~30s), idle pause + 60s countdown modal, time-gated Next button, subtle filling-hourglass indicator | CDPH audit defensibility | Async,UIUX,Compliance | FE | C-06 | Idle pauses timer; Next disabled until time+interaction met; logs accrued time | Audit failure | 2 |
| D-07 | P2 | Audio/TTS | Optional ≤60–90s neural TTS toggle (no autoplay) + transcript accordion; pause audio on KC; lock text before audio gen | Modality w/o redundancy | Async | ID/FE | D-02 | Audio optional, transcript paired; no autoplay | Redundancy overload | 2 |

---

## Workstream E — Certificate, Gate Center, Compliance Separation

| ID | P | Page/Area | Action Item | Rationale | Source | Owner | Deps | Acceptance Criteria | Risk | Phase |
|----|---|-----------|-------------|-----------|--------|-------|------|---------------------|------|-------|
| E-01 | P0 | Certificate Status | Large readiness ring + plain-English gate checklist + "optional support does not affect this" notice; mock-only watermark | Learner comprehension | UIUX,Compliance | FE/UX | A-05 | Locked state shows exactly what remains; no DB jargon | Confusion on lock | 1 |
| E-02 | P1 | Gate Center | Human-readable requirement rows (icon+title+plain desc+status badge); never expose raw booleans; audit-packet tie-in | Compliance control center | UIUX,Compliance | FE/CA | A-05 | All 11 gates as rows w/ plain English; scenario simulator retained | Auditor confusion | 1→2 |
| E-03 | P0 | Separation | Required CE progress ring computes from required gates ONLY; Optional progress always separate, never summed | CDPH 24-hr cap integrity | Compliance,UIUX | FE/CA | C-02 | Skipping all optional support never changes cert readiness (QA-011/013/014 pass) | Regulatory exposure | 1 |
| E-04 | P1 | Final exam gate | Build real 25-of-50 randomized engine, 80% pass, attempt logging, locked until theory+active-time met; no answer-key reveal post-submit | Summative integrity | Async,Content | FE/ID | D-06,Content SME | Exam locked until prereqs; randomized; pass logged; answers hidden | Integrity loss | 2 |
| E-05 | P1 | Affidavit | Affidavit gate locked until exam pass; mark e-signature method UNRESOLVED; wet-sign fallback note | Legal attestation | Compliance | CA/FE | E-04 | Affidavit unlocks only after pass; method flagged | Invalid attestation | 2 |
| E-06 | P0 | No-PHI | Pinned, non-dismissible oxblood PHI warning block above every free-text/upload (Clinical Hub, M6 practice) | HIPAA liability | UIUX,Compliance | UX/FE | B-01 | Warning above every input; cannot be dismissed | PHI leak liability | 1 |

---

## Workstream F — Clinical Hub, Audit, Moodle Map

| ID | P | Page/Area | Action Item | Rationale | Source | Owner | Deps | Acceptance Criteria | Risk | Phase |
|----|---|-----------|-------------|-----------|--------|-------|------|---------------------|------|-------|
| F-01 | P1 | Clinical Hub | Walled-off sandbox visual language (lighter charcoal, no burgundy borders); persistent "Optional / Non-Credit" badge on every card; CS-1…CS-7 tools | Subconscious separation | UIUX,Compliance | UX/FE | B-03,E-06 | Distinct styling; badge on each tool; PHI warnings present | Pathway blending | 2 |
| F-02 | P2 | Audit | Master-detail/tabbed: Required Evidence vs Optional Records; audit-trail timeline w/ timestamps; Export PDF/CSV buttons; premium tables (16px padding) | Defensible records | UIUX,Compliance | FE/CA | A-05 | Required/optional segregated; timeline shows timestamps | Looks like raw dump | 2 |
| F-03 | P2 | Moodle Map | Executive 3-column mapping (MVP section / Moodle component / notes) using app shell styling | Stakeholder roadmap | UIUX | FE/UX | B-03 | Reads as roadmap, not Jira; maps each page to mod_* | Stakeholder doubt | 2 |

---

## Workstream G — QA, Accessibility, Documentation

| ID | P | Page/Area | Action Item | Rationale | Source | Owner | Deps | Acceptance Criteria | Risk | Phase |
|----|---|-----------|-------------|-----------|--------|-------|------|---------------------|------|-------|
| G-01 | P1 | A11y | Full WCAG 2.2 AA audit: contrast, keyboard, screen-reader headings, tap targets, status-not-by-color | DOJ Title II Spring 2026 | UIUX,Async,Compliance | UX/FE | B-02b,B-05,B-07 | Documented audit; all P1 issues fixed | Legal exposure | 2 |
| G-02 | P1 | Mobile QA | Test on iPhone SE→15 Pro + low bandwidth; single-column, no horizontal scroll, sticky controls, one-question-per-screen | Mobile-first rules | Async,UIUX | FE/UX | C-06 | Manual matrix passes; tables stack as cards | Mobile frustration | 2 |
| G-03 | P0 | Demo QA | Negative-test pass: cert blocked when each required gate fails; optional skips non-blocking; PHI warning visible | Demo defensibility | Repo,Compliance | TPM/FE | A-05 | QA-002…QA-018 pass | Demo breaks | 1 |
| G-04 | P2 | Docs | Stakeholder-ready MVP doc set + designer handoff (Figma) + content-conversion guide | Handoff | Rec | TPM/UX | all | Docs delivered; demo script ready | Misalignment | 2 |
| G-05 | P1 | Content review | SME/compliance review of M1 (gap), M3 (source repair), M5 (skin), affidavit, NAC# metadata | Production safety | Content,Compliance | SME/CA | — | Sign-offs logged in compliance checklist | Unsafe clinical content | 1→2 |
| G-06 | P1 | Content fix | Author Module 1 graded module quiz (≥8 items, 80% pass) — referenced but not written | Module 1 cannot complete per syllabus without it | Content | ID/SME | G-05 | Quiz items authored + SME-reviewed; wired to M1 completion | M1 ungradeable | 2 |
| G-07 | P1 | Content fix | Repair Module 3 source (Lessons 3.3–3.5 + quiz + metadata); correct erroneous "complete" QA status | Truncated at Screen 3.2.3; QA status wrong | Content | ID/SME | G-05 | M3 source complete + QA status corrected | Ships incomplete clinical content | 2 |
| G-08 | P1 | Spec reconcile | Reconcile final-exam spec conflicts: attempts (3 vs 2), timer (none vs 45 min), Module 7 minutes — across `09_`, `29_`, `34_` | Build engine needs one truth | Content,Compliance | ID/CA | — | Single agreed exam config documented; E-04 built to it | Wrong exam behavior | 2 |
| G-09 | P2 | Content hygiene | Canonicalize duplicates: exam pool `30_`, quiz CSV `31_`, TTS `34_`, index `35_`; retire/flag `10_/11_/16_/23_` | Multiple drifting source versions | Content | ID/TPM | — | One canonical set referenced; legacy flagged superseded | Wrong-version delivery | 2 |

---

## Priority Rollup

| Priority | Count | Theme |
|----------|-------|-------|
| P0 | 16 | Architecture split, routing, asset fix, design tokens, shells, task-interface removal, core pages, separation, PHI, demo QA |
| P1 | 22 | State persistence, gate unify, microlearning, checks, feedback, active-time, gate center, exam, a11y, mobile, SME review, M1 quiz, M3 repair, exam-spec reconcile |
| P2 | 9 | Tests, glass, audio, audit, Moodle map, hub polish, docs, content de-duplication |
| P3 | 1 | Future elite (offline mode, advanced branching) |
