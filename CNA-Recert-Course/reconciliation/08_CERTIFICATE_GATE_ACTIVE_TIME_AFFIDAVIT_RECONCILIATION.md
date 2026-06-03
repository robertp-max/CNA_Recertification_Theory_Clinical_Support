# 08 - Certificate Gate, Active-Time, and Affidavit Reconciliation

## Title

08 - Certificate Gate, Active-Time, and Affidavit Reconciliation

## Status

Status: Incomplete - evidence missing; certificate production remains disabled

## Priority

P0 Blocker

## Owner

Program Owner / Legal

## Reviewer

Compliance / CDPH as applicable

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

Document available certificate gate evidence and the unresolved approval, affidavit, and active-time gaps.

## Findings

| Gate / approval item | Inspected evidence | Status | Blocker |
|---|---|---|---|
| Provider/course approval metadata | No local approval artifact found in inspected reconciliation/source files | Missing | P0 Blocker |
| NAC/provider details | No local approved metadata found | Missing | P0 Blocker |
| Approved certificate wording | `Content\14_CERTIFICATE_FIELD_MAPPING.csv` exists as mapping evidence; no approval proof inspected | Missing approval | P0 Blocker |
| Affidavit/e-sign method | `Content\13_AFFIDAVIT_TEXT.md` exists; no e-sign/wet-sign approval proof inspected | Missing approval | P0 Blocker |
| Active-time validation | No validation record inspected; Moodle logs alone are insufficient | Missing validation | P0 Blocker |
| App gate prototype | App page evidence referenced, but no runtime verification run | Needs App Verification | P1 High |

## Gaps

- No inspected evidence authorizes live certificate issuance.
- No inspected evidence approves active-time validation, affidavit method, or certificate wording.
- No PHI may be requested, typed, uploaded, shown, or implied as part of any gate.

## Required decisions

- Program Owner/Legal/CDPH must provide approval metadata, NAC/provider details, approved wording, and accepted affidavit method.
- QA/Compliance must validate active-time evidence or document a manual review hold.

## Acceptance criteria

- Certificate production remains disabled until every P0 item has written evidence.
- No reconciliation artifact claims certificate approval, CDPH approval, production readiness, or survey readiness.

## Next action

Collect written approval artifacts and rerun a gate-specific reconciliation before any certificate issuance is enabled.
