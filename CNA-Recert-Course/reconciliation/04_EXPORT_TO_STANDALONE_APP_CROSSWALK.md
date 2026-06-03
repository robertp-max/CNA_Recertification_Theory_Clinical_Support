# 04 - Export to Standalone App Crosswalk

## Title

04 - Export to Standalone App Crosswalk

## Status

Status: Incomplete - evidence missing for runtime/browser verification

## Priority

P1 High

## Owner

App Engineer

## Reviewer

QA / Compliance

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

Map inspected export/source evidence to standalone app data files and flag what still requires runtime verification.

## Findings

| App evidence inspected | Source/export relationship | Status |
|---|---|---|
| `standalone-course-mvp\src\data\contentV2.generated.ts` | Generated from ContentV2 package | Needs App Verification |
| `standalone-course-mvp\src\data\contentV2Adapter.ts` | Runtime adapter for ContentV2 data | Needs App Verification |
| `standalone-course-mvp\src\data\examPool.ts` | Related to final assessment pool | Needs SME and app verification; answer keys internal/admin-only |
| `standalone-course-mvp\src\data\narrationManifest.ts` | Related to narration planning | Needs owner/legal/compliance authorization before production use |
| `standalone-course-mvp\src\data\v2ModuleQuiz.ts` | Related to module quiz/check flow | Needs runtime verification |
| App pages previously referenced in reconciliation | Certificate/clinical/module flow | Present in repo but not runtime-verified in this pass |

## Gaps

- No browser/runtime test was run in this documentation-only pass.
- App files in the working tree are dirty from pre-existing changes, so this pass does not assert stable app behavior.
- No inspected evidence proves certificate production is enabled or approved; it must remain disabled.

## Required decisions

- App Engineer/QA must decide when to run browser verification and capture evidence.
- Compliance must confirm PHI warning coverage before any upload/free-text workflow is accepted.

## Acceptance criteria

- App wiring cannot be marked complete until a running build confirms module, assessment, optional clinical, PHI warning, and certificate-disabled states.
- Optional Clinical Support must remain optional, non-credit, non-gating, and not clinical-hour credit.

## Next action

Run a browser verification pass against the app only after documentation evidence gaps are resolved enough to define expected behavior.
