# MVP Implementation Index

CNA Recertification Theory + Clinical Support MVP — CI Institute of Nursing
Review + planning package generated 2026-05-28. **No source code was modified.** The sign-in/login page is approved and frozen.

This index links every deliverable produced in this folder (relative paths).

---

## Deliverables

| # | File | What it contains |
|---|------|------------------|
| 00 | [00_CURRENT_STATE_REVIEW.md](./00_CURRENT_STATE_REVIEW.md) | Preflight verification; full app architecture audit (routing, pages, components, data, styling, assets, login, build); what works/partial/broken/missing; root cause of the "messy task interface"; prioritized architectural problems |
| 01 | [01_CONTENT_REVIEW_AND_READINESS.md](./01_CONTENT_REVIEW_AND_READINESS.md) | Content package shape; module-by-module readiness table (theory + clinical support); per-criterion readiness; app-vs-source gap; consolidated gaps/defects; content conversion priority |
| 02 | [02_ACTIONABLE_ITEM_REGISTRY.md](./02_ACTIONABLE_ITEM_REGISTRY.md) | Full registry (ID, priority, workstream, page/area, action, rationale, source, owner, deps, acceptance criteria, risk, phase) across 7 workstreams |
| 03 | [03_TWO_PHASE_IMPLEMENTATION_PLAN.md](./03_TWO_PHASE_IMPLEMENTATION_PLAN.md) | Phase 1 (stabilization + redesign foundation) and Phase 2 (async delivery + evidence readiness): objective, scope, out-of-scope, tasks, files, deliverables, acceptance, QA, risks, exit criteria |
| 04 | [04_UIUX_DESIGN_SPECIFICATION.md](./04_UIUX_DESIGN_SPECIFICATION.md) | Design principles, color palette, typography, grid/nav, shells, card system, status badges, progress, certificate timeline, gate/audit rows, PHI blocks, active-time, feedback/locked states; page-by-page UI/UX plan; anti-patterns |
| 05 | [05_ASYNCHRONOUS_LESSON_DELIVERY_BLUEPRINT.md](./05_ASYNCHRONOUS_LESSON_DELIVERY_BLUEPRINT.md) | Lesson player layout; full micro-lesson anatomy; worked Module 1 / Lesson 1.3 walkthrough start→completion→unlock |
| 06 | [06_END_USER_JOURNEY_MAP.md](./06_END_USER_JOURNEY_MAP.md) | 31-step journey (first login → theory completion → certificate readiness) with goal/page/action/system response/evidence/UI status/blocker/recovery; journey invariants |
| 07 | [07_MODULE_LESSON_DELIVERY_MAP.md](./07_MODULE_LESSON_DELIVERY_MAP.md) | Module 0–7 + CS-1…CS-7: purpose, duration, lessons, delivery, interaction, knowledge-check, scenario, job aid, completion/remediation rules, UI components |
| 08 | [08_RECOMMENDATIONS_AND_RISKS.md](./08_RECOMMENDATIONS_AND_RISKS.md) | Build-first order, highest-value page, prototype module, postpone list, manual vs automated testing, review owners; risk register with mitigations; guardrails |
| 09 | [09_EXECUTIVE_SUMMARY_FOR_STAKEHOLDERS.md](./09_EXECUTIVE_SUMMARY_FOR_STAKEHOLDERS.md) | Non-technical summary, findings, deliverables, compliance rationale, decisions needed, recommended next step, demo talking point |

## Source documents reviewed (in this folder)
- [CNA Recertification MVP UI_UX Research.md](./CNA%20Recertification%20MVP%20UI_UX%20Research.md)
- [CNA Recertification Asynchronous Training Blueprint.md](./CNA%20Recertification%20Asynchronous%20Training%20Blueprint.md)

## Application under review
- `../../standalone-course-mvp/` (React 19 + Vite 7 + TypeScript). Entry: `src/main.tsx`; data: `src/data/*`; styles: `src/styles.css`.

## Content package reviewed
- `../Content/**` (theory modules, clinical support, exam pool, syllabus tables, knowledge-check/TTS blueprints, gap/compliance logs).

---

## Suggested reading order
1. **09** (executive summary) → 2. **00** (current state) → 3. **01** (content) → 4. **04** (design) → 5. **05** (lesson delivery) → 6. **06/07** (journey + module maps) → 7. **02/03** (registry + plan) → 8. **08** (recommendations + risks).

## How to use this package
- **Designers:** start with 04, 05, 07.
- **Engineers:** start with 00, 02, 03.
- **Instructional designers / SMEs:** start with 01, 05, 07.
- **Compliance / leadership:** start with 09, then 06 and 08.
