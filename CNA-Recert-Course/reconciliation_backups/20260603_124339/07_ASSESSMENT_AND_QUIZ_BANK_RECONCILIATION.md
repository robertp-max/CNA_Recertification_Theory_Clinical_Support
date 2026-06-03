# 07 — Assessment and Quiz Bank Reconciliation

## Purpose

Reconcile module knowledge checks, interaction checks, and the final exam / 50-question pool
against the export's final-exam source and the app's exam pool.

## Inputs Reviewed

- `CNA-Recert-Course\Content\08_MODULE_KNOWLEDGE_CHECK_BLUEPRINT.md`.
- `CNA-Recert-Course\Content\09_FINAL_EXAM_BLUEPRINT.md`.
- `CNA-Recert-Course\Content\12_INTERACTION_CHECK_MATRIX.csv`.
- `CNA-Recert-Course\Content\theory\exam\30_FINAL_EXAM_POOL_50_COMPLETE.md`.
- `CNA-Recert-Course\ContentV2\04_MODULE_ASSESSMENT_MAP.md`, `05_FINAL_ASSESSMENT_MAP.md`.
- Export: `linked-files\CI-ION NATP Final Exam.pdf`.
- App: `standalone-course-mvp\src\data\examPool.ts`, `v2ModuleQuiz.ts`.

## Evidence Table

| Item | Repo source | Export/App evidence | Status |
|---|---|---|---|
| Module knowledge checks | `08_MODULE_KNOWLEDGE_CHECK_BLUEPRINT.md` | ContentV2 `04_MODULE_ASSESSMENT_MAP` | In Progress |
| Interaction check matrix | `12_INTERACTION_CHECK_MATRIX.csv` | — | In Progress |
| Final exam blueprint | `09_FINAL_EXAM_BLUEPRINT.md` | `CI-ION NATP Final Exam.pdf` | Needs SME Review |
| Final exam pool (50) | `30_FINAL_EXAM_POOL_50_COMPLETE.md` | `examPool.ts` | Needs SME Review |
| Quiz bank master | ContentV2 `source_copy\csv\31_QUIZ_BANK_MASTER` | — | In Progress |

## Critical Compliance Rule

**Final exam answer keys must remain internal/admin-only.** This document and any learner-facing
documentation must not expose answer keys. The export's `CI-ION NATP Final Exam.pdf` must be treated
as internal source.

## Gaps Found

- The export final exam PDF has not been item-matched to the repo 50-question pool.
- Pass-mark threshold is **Needs verification** (not asserted from inspected files here).
- Each module's required check + interaction has not been confirmed 1:1.

## Owner / Action Needed

- SME: validate exam items and confirm pass mark.
- Instructional Designer: confirm per-module check + interaction coverage.

## Blocker Status

Not a P0 production blocker, but exam SME sign-off is required before any go decision.

## Next Verification Step

Item-map `CI-ION NATP Final Exam.pdf` to `30_FINAL_EXAM_POOL_50_COMPLETE.md` (internal review only).
