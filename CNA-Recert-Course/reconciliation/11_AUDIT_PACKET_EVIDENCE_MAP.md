# 11 - Audit Packet Evidence Map

## Title

11 - Audit Packet Evidence Map

## Status

Status: Incomplete - evidence missing for approval, active-time, affidavit, and runtime records

## Priority

P1 High

## Owner

Compliance Lead

## Reviewer

Program Owner / Legal / QA

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

Map what evidence exists for an internal audit packet and what must still be retained for survey/internal review.

## Findings

| Evidence category | Existing inspected evidence | Missing evidence | Retention note |
|---|---|---|---|
| Export provenance | `manifest.json`, copied `linked-files` | Failed/skipped source imports | Retain manifest, spreadsheet export, linked files |
| Spreadsheet URL evidence | `15_SPREADSHEET_URL_DOCUMENTATION_EVIDENCE_REGISTER.md`, workbook URL sheet | Sheet/row/cell positions; failed Google Docs | Retain URL register and copy-error log |
| Source content | `Content`, `ContentV2`, `CNA_Modules` | SME sign-off for flagged modules | Retain versioned source docs |
| ContentV2 runtime package | `ContentV2\data`, app `src\data` | Source-line validation and runtime proof | Retain generation metadata |
| Assessment | Final exam source and app data paths | Item-match, SME sign-off, key-protection proof | Keep keys/rationales admin-only |
| Certificate gate | Affidavit/certificate draft files | Approval metadata, approved wording, affidavit method | No live cert until P0 resolved |
| Active-time | No validation evidence inspected | Active-time validation/manual review records | Moodle logs alone insufficient |
| PHI controls | PHI warning component path referenced | Runtime coverage proof | Do not retain PHI |

## Gaps

- Audit packet cannot be final until approval metadata, active-time validation, affidavit method, and app runtime evidence exist.
- Failed/skipped URL sources must be imported or logged as blocked/owner-decision.

## Required decisions

- Program Owner decides whether this package is for internal reconciliation review only.
- Compliance determines retention requirements for non-PHI evidence.

## Acceptance criteria

- Audit packet includes source provenance, decision logs, and reviewer sign-offs.
- Audit packet excludes PHI and does not expose final exam keys/rationales.

## Next action

Create an evidence-retention index after failed URL imports and P0 approval decisions are resolved.
