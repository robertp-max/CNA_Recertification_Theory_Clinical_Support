# 05 — Missing Documentation Register

## Purpose

List documentation that is missing, incomplete, blocked, or needs source access, with owner and
priority. Authoring prompts for each are in `CLAUDE_MISSING_DOCUMENTATION_PROMPTS.md`.

## Inputs Reviewed

- All files in `CNA-Recert-Course\Content`, `CNA-Recert-Course\ContentV2`, and this reconciliation
  folder.
- `manifest.json` errors/skips/folders.

## Evidence Table

| ID | Program | Documentation Area | Target File / Location | Status | Priority | Owner |
|---|---|---|---|---|---|---|
| MD-01 | CNA Recert | Export inventory | `01_CI_ION_EXPORT_INVENTORY.md` | Created | P2 | Repo Auditor |
| MD-02 | CNA Recert | Export→Source crosswalk | `02_EXPORT_TO_SOURCE_DOC_CROSSWALK.md` | Created | P2 | Repo Auditor |
| MD-03 | CNA Recert | Export→ContentV2 crosswalk | `03_EXPORT_TO_CONTENTV2_CROSSWALK.md` | Created | P2 | Repo Auditor |
| MD-04 | CNA Recert | Export→App crosswalk | `04_EXPORT_TO_STANDALONE_APP_CROSSWALK.md` | Created | P1 | App Engineer |
| MD-05 | CNA Recert | URL evidence register | `15_SPREADSHEET_URL_DOCUMENTATION_EVIDENCE_REGISTER.md` | Created (positional cols incomplete) | P1 | Repo Auditor |
| MD-06 | CNA Recert | Spreadsheet positional map | `01` appendix | **Needs evidence** (parse `.xlsx`) | P1 | Repo Auditor |
| MD-07 | CNA Recert | Re-export failed Google Docs | `linked-files\` (22 items) | **Blocked — copy error** | P1 | Program Owner |
| MD-08 | CNA Recert | CDPH approval packet | PHASE_0 / CDPH submission | **Blocked — P0** | P0 | Program Owner / Legal |
| MD-09 | RCFE Admin | Full 26-artifact set | `RCFE Admin Docs` sheet | **Needs source** | P2 | Program Owner |
| MD-10 | Case Manager | Full 26-artifact set | `Case Manager Docs` sheet | **Needs source** | P2 | Program Owner |
| MD-11 | CNA Recert | Operations & Support Guide | (to create) | Missing | P2 | Program Owner |
| MD-12 | CNA Recert | Admission Exam folder docs | export folder (not copied) | **Needs owner decision** | P1 | Program Owner |

## Gaps Found

- The single largest documentation gap is the 22 failed Google Doc/Sheet conversions plus the
  positional spreadsheet mapping — together these leave 59 URLs undocumented.
- RCFE Admin and Case Manager have **no local source** and therefore only placeholder docs.

## Owner / Action Needed

- Program Owner: unblock MD-07, MD-08, MD-09, MD-10, MD-12.
- Repo Auditor: complete MD-06.

## Blocker Status

MD-08 is a **P0 production blocker** (CDPH approval). Others are documentation gaps.

## Next Verification Step

Execute the prompts in `CLAUDE_MISSING_DOCUMENTATION_PROMPTS.md` once source evidence is supplied.
