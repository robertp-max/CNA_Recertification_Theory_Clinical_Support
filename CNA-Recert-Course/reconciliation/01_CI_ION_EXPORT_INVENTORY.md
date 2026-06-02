# 01 — CI-ION Export Inventory

## Purpose

Provide a complete, evidence-based inventory of the local CI-ION export folder and classify what
was copied, skipped, errored, or left as an external reference.

## Inputs Reviewed

- `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\`
- `manifest.json` (the required Phase 3 evidence source)
- `CI-ION - Course Structures - Contents.xlsx`
- `linked-files\` (directory listing)

Verification commands used:

```powershell
Get-ChildItem -LiteralPath "CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428" -Recurse -Force
```

## Export Type (Reconciliation Question 3)

Per `manifest.json`, the export was produced by a Google Apps Script with the prefix
`CI-ION-course-export`. It contains:

- the active source spreadsheet exported as `.xlsx`,
- linked Google Drive files copied into `linked-files\`,
- a `manifest.json` recording config, links, copied files, skips, and errors.

**Conclusion:** This is a **Google Drive linked-doc + active-spreadsheet export**, not a Moodle
backup (`.mbz`), not an app/database export, and not a structured course-package (no course JSON,
no quiz XML, no completion config inside the export).

## Top-Level Inventory

| Item | Type | Size (bytes) | Notes |
|---|---|---|---|
| `manifest.json` | JSON | 53,719 | Export provenance — primary evidence |
| `CI-ION - Course Structures - Contents.xlsx` | XLSX | 455,709 | Master source spreadsheet |
| `linked-files\` | folder | — | 39 files (34 PDF, 1 DOCX, 4 PNG) |

**Total files in export:** 41 (39 linked + spreadsheet + manifest).

## Evidence Table — Manifest Counts

| Category | Count | Meaning |
|---|---:|---|
| `links_found` | 162 | All URLs discovered in the spreadsheet |
| `files_added` | 40 | 1 spreadsheet export + 39 linked Drive files copied |
| `skipped` | 36 | 35 video files + 1 oversized (63 MB) Google Doc |
| `errors` | 22 | 20 Google Doc + 1 Google Sheet conversion failures + 1 "no item found" |
| `folders_found_but_not_exported` | 1 | "Admission Exam" Drive folder (folder copy disabled) |

## Evidence Table — Copied Linked Files (Highlights)

| Pattern / File | Count | Maps To |
|---|---:|---|
| `cccco-na-model-curriculum-module-1..17.pdf` | 17 | CCCCO NA Model Curriculum source modules |
| `CI Institute of Nursing - Course Syllabus.pdf` | 1 | Provider syllabus |
| `CI Institute of Nursing Student Catalog 3-17-2026.docx` | 1 | Student catalog |
| `CI-ION NATP Final Exam.pdf` | 1 | Final exam source (keep keys internal) |
| `CI-ION_ Pre-Orientation Student Catalog Test.pdf` | 1 | Pre-orientation / catalog test → M00 |
| `PM Day */Day * Module *.pdf` | ~13 | Skills-day decks (rights, skills, procedures, charting, LTC) |
| `Cover_*_Text.png` | 4 | Section cover art (branding) |
| `Request for Live Scan Service (Example) .pdf` | 1 | Background-check example (no PHI) |

## Evidence Table — Not Copied

| Category | Count | Reason (from manifest) | Status |
|---|---:|---|---|
| Video files | 35 | `SKIP_VIDEO_FILES=true` | Skipped by Copy Config |
| Oversized Google Doc | 1 | "Tutorials - Instructor & Coordinator" 63 MB > `MAX_FILE_MB=45` | Skipped by Copy Config |
| Drive folder | 1 | "Admission Exam"; `INCLUDE_LINKED_FOLDERS=false` | Needs owner decision |
| Google Doc/Sheet conversions | 21 | Native Google formats not convertible to Office on export | Blocked — copy error |
| Missing item | 1 | "No item with the given ID could be found" | Blocked — source access |

## Gaps Found

- The `.xlsx` tabs/structure have not yet been parsed; positional URL mapping is pending.
- 35 clinical-skill/tutorial videos and the 63 MB instructor doc are not present locally.
- The "Admission Exam" folder contents are unknown (never enumerated).

## Owner / Action Needed

- Repo Auditor: parse `.xlsx` to enumerate tabs and URL cell positions (REC-003).
- Program Owner: decide on video/folder transfer and re-export of failed Google Docs.

## Blocker Status

Inventory is **Complete** for what is physically present. Items not copied are flagged but are not
production blockers for the *required theory* path (videos relate to Optional Clinical Support).

## Next Verification Step

Open the `.xlsx` and list sheet names + URL-bearing cells to backfill the URL evidence register.

> Full per-URL classification is in `15_SPREADSHEET_URL_DOCUMENTATION_EVIDENCE_REGISTER.md` and the
> `Spreadsheet URL Evidence` sheet of the master tracker workbook.
