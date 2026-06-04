# 07 - Assessment and Quiz Bank Reconciliation

## Title

07 - Assessment and Quiz Bank Reconciliation

## Status

Status: Incomplete - evidence missing for final exam item-match and SME approval

## Priority

P1 High

## Owner

Instructional Designer

## Reviewer

SME / Compliance

## Last checked

2026-06-03

## Source files inspected

- `CNA-Recert-Course\reconciliation\MISSING_DOCUMENTATION_GENERATION_AUDIT.md`
- `CNA-Recert-Course\reconciliation\00_CI_ION_RECONCILIATION_EXECUTIVE_SUMMARY.md`
- `CNA-Recert-Course\reconciliation\05_MISSING_DOCUMENTATION_REGISTER.md`
- `CNA-Recert-Course\reconciliation\13_GO_NO_GO_BLOCKERS_AND_DECISIONS.md`
- `CNA-Recert-Course\reconciliation\15_SPREADSHEET_URL_DOCUMENTATION_EVIDENCE_REGISTER.md`
- `CNA-Recert-Course\Content`
- `CNA-Recert-Course\ContentV2`
- `standalone-course-mvp\src\data`
## Export evidence inspected

- `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428`
- `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\manifest.json`
- `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\CI-ION - Course Structures - Contents.xlsx`
- `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files`

Recalculated from `manifest.json`: 162 URLs, 39 copied/imported, 36 skipped, 22 errored, 57 duplicate/tab-anchor rows, 7 external-only, 1 owner-decision folder rows, 59 still undocumented.
## Purpose

Reconcile assessment evidence while keeping final exam answer keys and rationales internal/admin-only.

## Findings

| Assessment evidence | Inspected path | Status |
|---|---|---|
| Final exam source PDF | `linked-files\CI-ION NATP Final Exam.pdf` | Exists locally; internal source only |
| Final exam markdown pool | `CNA-Recert-Course\Content\theory\exam\30_FINAL_EXAM_POOL_50_COMPLETE.md` | Exists; item-match not completed in this pass |
| ContentV2 final assessment map | `CNA-Recert-Course\ContentV2\05_FINAL_ASSESSMENT_MAP.md` | Exists; not proof of SME approval |
| App exam data | `standalone-course-mvp\src\data\examPool.ts` | Exists; runtime exposure not verified |
| Module assessment map | `CNA-Recert-Course\ContentV2\04_MODULE_ASSESSMENT_MAP.md` | Exists; module check runtime not verified |

## Gaps

- No item-by-item mapping was completed between `CI-ION NATP Final Exam.pdf`, the 50-question pool, ContentV2, and app exam data.
- No SME approval record for assessment validity was inspected.
- Answer-key exposure was not runtime-tested.

## Required decisions

- SME must approve final exam content and any pass threshold.
- QA must verify answer keys/rationales are not learner-facing.

## Acceptance criteria

- Final exam answer keys and rationales remain internal/admin-only.
- No learner-facing reconciliation document exposes answers or rationales.
- Assessment cannot be marked complete until item-match and SME review are documented.

## Next action

Perform an internal-only item map from the export final exam PDF to the repo pool and app data, with answer keys redacted from learner-facing materials.
