# 10 - Source Repair, SME, and Compliance Flags

## Title

10 - Source Repair, SME, and Compliance Flags

## Status

Status: Incomplete - flags remain open until reviewed evidence exists

## Priority

P1 High

## Owner

Instructional Designer / Program Owner

## Reviewer

SME / Compliance / Legal

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

Consolidate unresolved source repair, SME, compliance, legal, TTS/audio, and optional clinical support flags.

## Findings

| Flag | Evidence inspected | Owner | Reviewer | Blocker level | Status |
|---|---|---|---|---|---|
| Module 1 infection-control source review | `Content\theory\modules\05_THEORY_MODULE_01_INFECTION_CONTROL_FULL.md`; source packet summary | Instructional Designer | SME | P1 High | Open |
| Module 3 source repair and sensitive-content review | `Content\theory\modules\25_THEORY_MODULE_03_DEMENTIA_COMMUNICATION_CULTURAL_RESPECT_FULL.md` | Instructional Designer | SME / Compliance | P1 High | Open |
| Module 5 skin integrity / pressure injury review | `Content\theory\modules\27_THEORY_MODULE_05_NUTRITION_SKIN_INTEGRITY_VITAL_SIGNS_FULL.md` | Instructional Designer | SME | P1 High | Open |
| Certificate wording / approval metadata | `Content\13_AFFIDAVIT_TEXT.md`, `Content\14_CERTIFICATE_FIELD_MAPPING.csv` | Program Owner / Legal | Compliance / CDPH as applicable | P0 Blocker | Open |
| TTS/audio authorization | `ContentV2\narration`, `standalone-course-mvp\src\data\narrationManifest.ts` | Program Owner | Legal / Compliance | P2 Medium | Open |
| Optional Clinical Support separation | `Content\clinical-support`, app clinical hub evidence | Program Owner | Compliance | P1 High | Open pending runtime verification |

## Gaps

- No reviewed/sign-off artifact was inspected for M01, M03, or M05.
- No inspected evidence authorizes TTS/audio production.
- No inspected evidence authorizes Optional Clinical Support as clinical-hour credit; it remains optional, non-credit, and non-gating.

## Required decisions

- SME must approve or request repairs for M01, M03, and M05.
- Legal/compliance must decide certificate, affidavit, active-time, and TTS/audio status.

## Acceptance criteria

- Do not clear a flag without a dated evidence file and reviewer role.
- Do not count Optional Clinical Support as required theory, clinical-hour credit, or a certificate gate.

## Next action

Create reviewer sign-off records or source-repair tasks for each open flag.
