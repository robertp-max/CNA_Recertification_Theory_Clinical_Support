# 03 - Export to ContentV2 Crosswalk

## Title

03 - Export to ContentV2 Crosswalk

## Status

Status: Incomplete - evidence missing for line-by-line source-to-ContentV2 validation

## Priority

P2 Medium

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

Map inspected export evidence to local ContentV2 artifacts without treating generated runtime content as approval evidence.

## Findings

| Export/source evidence | ContentV2 evidence inspected | Reconciliation status |
|---|---|---|
| `manifest.json` and copied CCCCO PDFs | `ContentV2\01_SOURCE_CONTENT_AUDIT.md` | File-level source audit exists; item-level validation still needed |
| Source packet theory modules M00-M07 | `ContentV2\03_MODULE_LESSON_4CARD_MAP.md` | Lesson map exists; source-to-card validation still needed |
| Module checks / final assessment docs | `ContentV2\04_MODULE_ASSESSMENT_MAP.md`, `05_FINAL_ASSESSMENT_MAP.md` | Maps exist; final exam item match still internal/admin-only |
| Course timing model | `ContentV2\10_CONTENT_COVERAGE_AND_TIME_RECONCILIATION.md` | 720-minute model preserved: M00 30, M01 90, M02 120, M03 120, M04 120, M05 120, M06 90, M07 30 |
| Generated runtime package | `ContentV2\data\courseContentV2.json`, `courseContentV2.ts` | Present; not proof of approval |
| Narration package | `ContentV2\narration\narration_master.csv`, `tts_narration_import.csv` | Present; TTS/audio production not authorized |

## Gaps

- ContentV2 generated files are not proof of SME, compliance, legal, CDPH, certificate, or active-time approval.
- No inspected evidence proves every ContentV2 lesson line maps to a copied source PDF.
- Failed/skipped spreadsheet URL sources cannot be used as ContentV2 evidence until imported.

## Required decisions

- SME must decide whether M01 infection control, M03 source/sensitive-content, and M05 skin integrity content are acceptable after source review.
- Owner/legal/compliance must decide whether TTS/audio is authorized.

## Acceptance criteria

- Every ContentV2 module and assessment row must cite source files that exist locally or be marked `Needs Document Import`.
- ContentV2 must remain documented as generated runtime content, not approval evidence.

## Next action

Create a line-level ContentV2-to-source validation pass for M01, M03, M05, and final assessment mapping after missing Google Docs are re-exported.
