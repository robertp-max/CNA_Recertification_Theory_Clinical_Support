# 12 - QA Negative Test and Acceptance Plan

## Title

12 - QA Negative Test and Acceptance Plan

## Status

Status: Incomplete - tests not executed in this documentation-only pass

## Priority

P1 High

## Owner

QA Lead

## Reviewer

Compliance / Program Owner

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

Define negative tests required before any go decision, focused on PHI, optional clinical separation, answer-key protection, certificate disabled state, active-time, source gaps, URL errors, and app/export mismatch.

## Findings

| Test ID | Negative test | Evidence basis | Expected result | Status |
|---|---|---|---|---|
| QA-01 | PHI entry prevention | PHI guardrail and `PhiWarningBlock` path | No PHI requested, typed, uploaded, shown, or implied | Not executed |
| QA-02 | Optional clinical non-gating | Optional Clinical docs and app clinical hub path | Certificate path unaffected by optional clinical | Not executed |
| QA-03 | Final answer key exposure | Final exam/internal-answer guardrail | No keys/rationales learner-facing | Not executed |
| QA-04 | Certificate disabled state | P0 blocker docs | Certificate production disabled | Not executed |
| QA-05 | Active-time evidence | Missing validation evidence | Idle/log-only evidence cannot satisfy active time | Not executed |
| QA-06 | Missing approval metadata | Certificate gate docs | Gate blocks completion/cert output | Not executed |
| QA-07 | Source gaps | M01/M03/M05 flags | Flagged modules cannot be marked reviewed | Not executed |
| QA-08 | Copied URL errors | Manifest `errors[]` | Failed URLs remain blocked/needs import | Not executed |
| QA-09 | Skipped videos/folder | Manifest `skipped[]`, `folders_found_but_not_exported[]` | Owner decision required; not assumed documented | Not executed |
| QA-10 | App/export mismatch | Export + app data paths | Runtime displays only verified content | Not executed |

## Gaps

- No app tests were run because this is a documentation reconciliation task only.
- No runtime/browser screenshots or logs were generated.

## Required decisions

- QA and Compliance must decide acceptance thresholds and evidence capture format.
- Program Owner must decide whether skipped export items are required for launch scope.

## Acceptance criteria

- All P0 negative tests pass before any certificate/go decision.
- Tests must not use or generate PHI.
- Answer keys/rationales remain internal/admin-only.

## Next action

Run these tests only after source imports, reviewer decisions, and P0 approval artifacts are available.
