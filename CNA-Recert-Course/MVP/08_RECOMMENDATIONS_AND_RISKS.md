# 08 — Recommendations & Risks

---

## 1. Recommendations (beyond the minimum)

### What to build first
1. **Architecture split + routing + asset fix (A-01, A-02, A-04).** Everything else is faster and safer once the 2,731-line monolith is decomposed and images load. Do this before any visual work.
2. **Design tokens + shells (B-01–B-04).** Re-skin to dark cinematic with desktop top nav + mobile bottom nav so stakeholders see the new identity immediately.
3. **Remove the task interface (C-01).** Move every evidence/gate toggle into Reviewer Tools; this is the single most visible fix to the stated problem.

### Highest UX-value page
**The Dashboard.** It is the command center that answers "what do I do now and how close am I?" The "Next Up" card + locked certificate banner + isolated required/optional rings deliver the biggest perceived-quality jump and most directly cure decision fatigue.

### Which content to convert first
**Module 1 (Infection Control & PPE)** — it already has full screen-by-screen prose, 6 knowledge checks with ✅/❌ feedback, and 3 interaction specs in `Content/theory/modules/05_*.md`. It is the lowest-effort, highest-fidelity path to a complete real lesson. **Module 6 (Documentation/PHI)** second, because it anchors platform-wide PHI safety.

### Prototype module
**Module 1** is the prototype module (also named as the single-lesson prototype in both source docs). Build it end-to-end in Phase 1.

### What to postpone (Phase 2 / P3)
- Real active-time heartbeat engine, real 25/50 exam engine, TTS audio (P2).
- Full audit export, Moodle map polish, glassmorphism fine-tuning (P2).
- Module 3 delivery until its source is repaired.
- Advanced branching simulations, neural-voice production at scale, offline mode (P3).

### What to test manually
- Mobile device matrix (iPhone SE → 15 Pro), low-bandwidth fallback, one-handed bottom-nav reach.
- Keyboard-only traversal + visible focus ring; screen-reader heading order.
- Negative gate tests (cert blocked per failing gate; optional skips non-blocking; PHI warning visible).

### What to automate
- Gate-logic unit tests (one unified gate model) — assert optional support never affects readiness.
- Core-loop e2e (login → M0 → M1 lesson → quiz → dashboard update).
- CI: typecheck + lint + tests on every PR.
- Contrast checks wired into the design-token build.

### What compliance/legal must review
- Affidavit text + **e-signature acceptance method** (wet-sign fallback decision).
- Provider **NAC#** / certificate metadata + final certificate wording before any issuance.
- Disclaimer wording (Module 0), online-cap language, optional/non-credit copy.
- That required CE progress is computed from required gates **only** (CDPH 24-hr cap integrity).

### What RN / clinical educator (SME) must review
- **Module 1** (no dedicated NATP source — verify alignment to CDPH expectations).
- **Module 5** skin-integrity/pressure-injury content + exam **Q21/Q38**.
- **Module 3** repaired source (cultural, end-of-life, trauma-informed) before delivery.
- Module 2 prioritization (NATP-17 6 hr → 2 hr) and emergency wording in Module 4.

### What UI/UX designer must validate
- WCAG AA contrast on every token pairing; status-not-by-color badge set.
- Glassmorphism perf on mid/older devices; 44×44px targets; sticky controls; lesson reading column 60–75 chars.
- Figma component library + 10 desktop + priority mobile views per the handoff checklist.

### What to validate before the stakeholder demo
- Build + preview clean (no broken images); all routes reachable; refresh preserves progress.
- Module 1 completes via real content + knowledge check (no checkbox).
- Required vs optional rings visually separate; certificate stays correctly locked/unlocked.
- Negative-test pass; mobile bottom nav works; cinematic tokens applied to core screens.
- A one-page demo script that explicitly calls out compliance separation (reuse `stakeholderDemoScript`).

---

## 2. Implementation Risks & Mitigations

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| R1 | Refactor of monolith regresses gate behavior | Med | High | Unify gate model (A-05); run negative tests continuously (G-03); add unit tests (A-07) |
| R2 | Optional clinical support visually/logically blends into required CE → CDPH exposure | Med | **Critical** | Separate rings, persistent "Optional · Non-Credit" badges, computational separation; QA-011/013/014 must pass |
| R3 | Dark-mode contrast failures | High | High | Enforce AA tokens (B-01/B-02b); contrast plugin gate before demo |
| R4 | Module 1 clinical content unverified (no NATP source) | High | High | SME sign-off before pilot; keep "NEEDS SME REVIEW" flags visible until cleared |
| R5 | Module 3 source defect ships incomplete | Med | High | Lock/flag incomplete sections; do not deliver until repaired |
| R6 | Active-time tracking inaccurate/disputed | Med | High | Document heartbeat + idle algorithm; align to future Moodle Dedication/Timestat; reviewer can inspect accrual |
| R7 | Final-exam integrity (answer leakage, weak items) | Med | High | No answer reveal post-submit; randomize; gate exam go-live on SME item review |
| R8 | E-signature method undecided blocks attestation validity | Med | High | Legal decision; wet-sign fallback; gate flagged in Gate Center |
| R9 | Certificate issued prematurely / wording wrong | Low | **Critical** | Keep mock-only watermark; disable issuance until NAC#/wording approved |
| R10 | PHI entered in free-text/uploads | Med | **Critical** | Non-dismissible oxblood PHI block above every input; admin rejects PHI; exclude free-text reflections |
| R11 | Glassmorphism scroll lag on older phones | Med | Med | Blur ≤15px; `@supports` flat fallback |
| R12 | Mobile nav = shrunken desktop header | Low | Med | Dedicated 4–5 icon bottom nav |
| R13 | State loss on refresh frustrates learners | Med | Med | Persisted store + Resume (A-03) |
| R14 | Scope creep blends Phase 1/2 | Med | Med | Enforce out-of-scope lists; phase gates |
| R15 | Two content indexes / divergent gate models drift | Low | Med | Canonicalize `index/35_…UPDATED`; unify gate model |

---

## 3. Guardrails That Must Not Be Weakened

- Required Online CE and Optional Clinical Support remain **separate, non-credit, non-gating** unless **written CDPH approval** changes the rule.
- Certificate stays a **mock preview**; no issuance until provider metadata + wording approved.
- **No PHI** anywhere; warnings pinned above every free-text/upload.
- The **sign-in/login page is approved** and must not be redesigned or modified.
