# 00 — CI-ION Export Reconciliation: Executive Summary

**Generated:** 2026-06-01
**Repo:** `C:\AI\Git\CNA_Recertification_Theory_Clinical_Support`
**GitHub reference:** `robertp-max/CNA_Recertification_Theory_Clinical_Support`
**Scope:** Documentation + tracker reconciliation only. No app/source/ContentV2 code was modified.
**Status:** NOT production-ready. Certificate issuance is BLOCKED. No CDPH approval claimed.

---

## Purpose

Reconcile the local CI-ION course export against the repository's CNA Recertification
source documentation, ContentV2, and the `standalone-course-mvp` app; register every
spreadsheet URL with an evidence status; identify missing documentation; and produce a
polished master tracker workbook. Also define a reusable documentation standard for
CNA Recert, RCFE Admin, and Case Manager programs.

## Inputs Reviewed

| Input | Path | Result |
|---|---|---|
| CI-ION export folder | `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428` | Found and inspected |
| Export manifest | `…\manifest.json` (53,719 bytes) | Found and inspected |
| Active spreadsheet export | `…\CI-ION - Course Structures - Contents.xlsx` (455,709 bytes) | Present; tabs not yet parsed |
| Linked files | `…\linked-files\` (39 files: 34 PDF, 1 DOCX, 4 PNG) | Present |
| CNA source packet | `CNA-Recert-Course\Content\` (docs 00–23, theory modules, exam, clinical-support) | Present |
| ContentV2 | `CNA-Recert-Course\ContentV2\` (JSON, schema, generated TS, narration CSVs, docs 00–11) | Present |
| Standalone app | `standalone-course-mvp\src\data\` + pages | Present (working tree dirty) |

## Headline Findings (Evidence-Based)

- The export is a **Google Drive linked-document + active-spreadsheet export** (produced by a
  Google Apps Script, per `manifest.json`). It is **NOT** a Moodle `.mbz` backup, not an app
  export, and not a custom CI-ION package with course-structure JSON.
- **162 URLs** were discovered in the source spreadsheet (`links_found`). Of these:
  - **39** map to copied/imported files (`files_added`).
  - **36** were skipped by copy config (35 videos + 1 oversized 63 MB Google Doc).
  - **22** are copy/convert errors (20 native Google Docs + 1 Google Sheet failed Office
    conversion; 1 Google Doc returned "no item found / no permission").
  - **57** are duplicates or alternate `tab=` anchors of the same source document.
  - **7** are external-reference links (Figma, Maps, WhatsApp, Calendar, Moodle docs, the live
    Moodle shell, an external blog).
  - **1** is a Drive folder ("Admission Exam") that was found but not copied (folder copy disabled).
  - **59 URLs still require document import / extraction / owner decision** and must NOT be
    treated as documented.
- The CNA source packet, ContentV2, and the standalone app **are all present locally**. ContentV2
  is **not** missing from this clone.
- The eight required theory modules **M00–M07 exist** as source markdown and map to CCCCO NA
  Model Curriculum module PDFs carried in the export.

## Production Blockers (P0)

These remain unresolved and are not invented as satisfied:

1. **CDPH provider/course approval** — not confirmed (no provider/NAC IDs, hours, or title approved).
2. **Approved certificate wording** — DRAFT only; no CDPH-approved language.
3. **Affidavit + e-signature acceptance** — not legally approved.
4. **Active-time validation** — plugin not validated; Moodle logs alone are insufficient.

## What This Reconciliation Produced

- 16 markdown reconciliation documents (this file + 01–15 and the prompts file).
- `CI_ION_Course_Reconciliation_Master_Tracker.xlsx` (16 sheets, dashboard, conditional
  formatting, dropdowns, filters, frozen panes, URL evidence register, program matrix).
- A 162-row spreadsheet URL evidence register.
- A reusable 26-artifact documentation standard for CNA / RCFE Admin / Case Manager.
- Claude prompts to generate the remaining missing documentation.

## Gaps Found (Summary)

- Spreadsheet positional data (sheet/row/cell per URL) not yet extracted from the `.xlsx`.
- 22 native Google Docs/Sheets failed export conversion → undocumented locally.
- 35 clinical-skill / tutorial videos + 1 oversized doc + 1 folder skipped → owner decision needed.
- Module 1 (infection control) and Module 5 (skin integrity) require SME review.
- Module 3 carries source-repair risk (possible interrupted source content).

## Owner / Action Needed

- Program Owner: obtain CDPH approval, provider metadata, certificate wording, e-sign decision.
- Program Owner: decide on video/folder transfer and re-export of failed Google Docs as PDF.
- SME (RN/Clinical Educator): review M01, M05, dementia language, and final-exam mapping.
- App Engineer/QA: verify app wiring and run negative tests.

## Blocker Status

**NO-GO for production / certificate issuance.** Documentation reconciliation is in progress;
several deliverables are intentionally marked *Incomplete — evidence missing* where source
evidence is not locally available.

## Next Verification Step

Parse `CI-ION - Course Structures - Contents.xlsx` to backfill sheet/row/cell positions for each
URL in `15_SPREADSHEET_URL_DOCUMENTATION_EVIDENCE_REGISTER.md`, then re-export the 22 failed
Google Docs as PDF to close the largest documentation gap.
