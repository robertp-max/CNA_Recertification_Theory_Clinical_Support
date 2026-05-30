# 09 — Executive Summary for Stakeholders

**Product:** CNA Recertification Theory + Clinical Support MVP — CI Institute of Nursing
**Audience:** Leadership, Compliance, Clinical Education, Product/Design stakeholders
**Status:** Review + plan complete; implementation not yet started (this pass changed no source code).

---

## The one-paragraph story

We have a working React/Vite prototype that already contains all ten target pages and a genuinely strong compliance/gate engine. Its weakness is that it *feels like an administrative to-do list*: learners advance by checking boxes instead of doing lessons, the visual identity is a legacy light theme rather than the approved dark cinematic look, and the code is a single 2,700-line file with no routing. The plan is to convert it into a **clean, guided, mobile-first learning journey** — re-skinned to the dark premium cinematic system, organized as proper page views (Dashboard → Modules → Module Detail → Lesson Player → Certificate/Gate Center), with real microlearning lessons replacing the checkbox interface — **without weakening a single compliance guardrail**. The approved sign-in page is frozen.

---

## What we found

- **Architecture:** Standalone React 19 + Vite 7 + TypeScript SPA in `standalone-course-mvp/`. No router, no persistence, one 2,731-line `main.tsx`, one 4,173-line stylesheet.
- **Good news:** All 10 pages exist; the **Gate Command Center** (11 gates, 12 scenarios, explicit optional-support boundary) is excellent and audit-aware; required-vs-optional separation is already modeled correctly in logic.
- **The "messy task interface":** Completion is driven by manual evidence checkboxes (e.g., one shared toggle covers Modules 2–6). This is the core thing to replace.
- **Content:** A substantial, well-organized 12-hour theory package (Modules 0–7) plus 7 optional clinical-support tracks. Module 1 has full, lesson-ready prose with knowledge checks. Three content risks: Module 1 lacks a dedicated source (needs SME review), Module 3's source is interrupted/incomplete, and Module 5 skin-integrity items are flagged.
- **Compliance:** 12-hr online theory fits safely within the CDPH 24-hr online cap; optional clinical support is correctly non-credit/non-gating; certificate is mock-only; no PHI.

## What we will deliver

- **Phase 1 (demo-ready):** componentized + routed app, dark cinematic design system, desktop + mobile shells, the task interface removed, redesigned Dashboard/Landing/Modules/Module Detail/Lesson Player/Certificate/Gate Center, and **Module 1 built end-to-end** as a real microlearning lesson.
- **Phase 2 (pilot-ready):** all modules converted to 3–5 min micro-lessons with checks/feedback, a real active-time engine, a real final-exam flow, complete certificate/gate logic, the optional Clinical Hub, Audit evidence view, Moodle Map, and full mobile + WCAG 2.2 AA QA.

## Why this matters to compliance

Every design decision protects the certificate's defensibility: required CE progress is computed from required gates only; optional support is walled off and badged "Optional · Non-Credit"; PHI warnings are pinned above every input; the final exam is gated and never reveals answers; and the certificate stays a mock until provider NAC#/wording and the e-signature method are approved.

## Top decisions we need from stakeholders

1. **E-signature acceptance method** for the affidavit (or wet-sign fallback).
2. **Provider NAC# + certificate wording** sign-off (blocks certificate go-live).
3. **SME review** scheduling for Module 1 (gap), Module 3 (source repair), Module 5 (skin items).
4. Confirmation that **no clinical-support activity counts** toward renewal without written CDPH approval.

## Recommended next step

Approve Phase 1 and begin with the architecture split + routing + asset fix, then the design system and Module 1 prototype — targeting a stakeholder demo of the redesigned core loop on desktop and mobile. (See `02_ACTIONABLE_ITEM_REGISTRY.md` and `03_TWO_PHASE_IMPLEMENTATION_PLAN.md`.)

---

### Demo talking point (reusable)
> "This MVP protects certificate integrity. A learner can complete optional clinical support or skip it entirely — the certificate depends only on the required online CE gates. That gives leadership and compliance a clear, auditable reason for every certificate decision."
