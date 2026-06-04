# 01 - CI-ION Export Inventory

## Title

01 - CI-ION Export Inventory

## Status

Complete for local export inventory; Status: Incomplete - evidence missing for spreadsheet sheet/row/cell URL positions

## Priority

P1 High

## Owner

Repo Auditor

## Reviewer

Program Owner

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

Document exactly what the local CI-ION export contains, what it proves, and what it does not prove.

## Findings

- Exact export folder path: `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428`.
- Export folder type: Google Drive linked-file and active-spreadsheet export with Apps Script provenance in `manifest.json`; not a Moodle `.mbz`, not an app export, and not proof of a configured Moodle course.
- Top-level items: `manifest.json`, `CI-ION - Course Structures - Contents.xlsx`, and `linked-files`.
- Total export files inspected: 41; linked files: 39 ({'.pdf': 34, '.docx': 1, '.png': 4}).
- Manifest fields inspected: `created_at`, `spreadsheet`, `config`, `links_found`, `files_added`, `folders_found_but_not_exported`, `folders_scanned`, `skipped`, and `errors`.
- `files_added`: 40 total, including 1 active spreadsheet export and 39 linked Drive files.
- `skipped`: 36 total, including 35 video files skipped because `SKIP_VIDEO_FILES` is true and 1 oversized Google Doc.
- `errors`: 22 total: copy/convert/access failures that remain undocumented locally.
- `folders_found_but_not_exported`: 1 (`Admission Exam`) because linked-folder export was disabled.

| Local linked-file sample | Extension | Bytes | Evidence status |
|---|---:|---:|---|
| `AM Day 6 - PM Day 11 Module 8 Patient Care Skills.pdf` | `.pdf` | 91797 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-1.pdf` | `.pdf` | 1888082 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-10.pdf` | `.pdf` | 805210 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-11.pdf` | `.pdf` | 400160 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-12.pdf` | `.pdf` | 258863 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-13.pdf` | `.pdf` | 550134 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-14.pdf` | `.pdf` | 307538 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-15.pdf` | `.pdf` | 348178 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-16.pdf` | `.pdf` | 99636 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-17.pdf` | `.pdf` | 86441 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-2.pdf` | `.pdf` | 246810 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-3.pdf` | `.pdf` | 439222 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-4.pdf` | `.pdf` | 223041 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-5.pdf` | `.pdf` | 326763 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-6.pdf` | `.pdf` | 225577 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-7.pdf` | `.pdf` | 457369 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-8.pdf` | `.pdf` | 837346 | Copied local file in export `linked-files` |
| `cccco-na-model-curriculum-module-9.pdf` | `.pdf` | 393304 | Copied local file in export `linked-files` |
| `CI Institute of Nursing - Course Syllabus.pdf` | `.pdf` | 799354 | Copied local file in export `linked-files` |
| `CI Institute of Nursing Student Catalog 3-17-2026.docx` | `.docx` | 2025744 | Copied local file in export `linked-files` |
| ... | ... | ... | 19 additional linked files listed in workbook `Export Inventory` sheet |

## Gaps

- Spreadsheet tab names, row numbers, and cell addresses for each URL are still missing because the `.xlsx` has not been parsed into a positional URL map.
- The 22 `errors[]` source items are not copied/imported locally.
- The 35 videos, 1 oversized Google Doc, and 1 folder are not locally available as export evidence.

## Required decisions

- Program Owner must decide whether skipped videos and the `Admission Exam` folder should be imported or intentionally excluded.
- Program Owner must re-export failed Google Docs/Sheet as PDF or document source access blockers.

## Acceptance criteria

- Export inventory counts must match `manifest.json` and local directory listing.
- Export inventory must not claim Moodle/course completion, CDPH approval, certificate approval, or production readiness.

## Next action

Parse `CI-ION - Course Structures - Contents.xlsx` to add sheet/row/cell URL positions, then re-export or document all manifest `errors[]`.
