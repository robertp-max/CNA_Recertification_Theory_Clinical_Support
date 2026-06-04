# 02 — Export → Source Documentation Crosswalk

## Purpose

Map files inside the CI-ION export to the repository's CNA source documentation packet
(`CNA-Recert-Course\Content\`), and identify where source-of-truth differs.

## Inputs Reviewed

- Export `linked-files\` (CCCCO modules 1–17, syllabus, catalog, final exam, skills decks).
- `CNA-Recert-Course\Content\00_EXECUTIVE_SUMMARY.md` (authoritative source list).
- `CNA-Recert-Course\Content\01_SOURCE_TO_COURSE_CROSSWALK.md`.
- `CNA-Recert-Course\Content\theory\modules\` (M00–M07).

## Key Reconciliation Note

The course `00_EXECUTIVE_SUMMARY.md` states primary content is sourced from **NATP Modules 10–17**
(CCCCO NA Model Curriculum, Revised December 2018). The export carries **CCCCO modules 1–17**
(all 17), so modules 1–9 are present as additional source context but are not the primary
required-theory source.

## Evidence Table

| Export source file | Repo source doc | Course module | Status |
|---|---|---|---|
| `cccco-na-model-curriculum-module-10.pdf` (Vital Signs) | `27_THEORY_MODULE_05_...` | M05 | Mapped |
| `cccco-na-model-curriculum-module-11.pdf` (Nutrition) | `27_THEORY_MODULE_05_...` | M05 | Mapped |
| `cccco-na-model-curriculum-module-12.pdf` (Emergency) | `26_THEORY_MODULE_04_...` | M04 | Mapped |
| `cccco-na-model-curriculum-module-13.pdf` (LTC Resident) | `25_THEORY_MODULE_03_...` | M03 | Mapped — source-repair check |
| `cccco-na-model-curriculum-module-14.pdf` (Rehabilitative) | `26_THEORY_MODULE_04_...` | M04 | Mapped |
| `cccco-na-model-curriculum-module-15.pdf` (Observation/Charting) | `28_THEORY_MODULE_06_...` | M06 | Mapped |
| `cccco-na-model-curriculum-module-16.pdf` (Death/Dying) | (referenced in LTC/M03/M06) | — | Supplemental |
| `cccco-na-model-curriculum-module-17.pdf` (Abuse) | `24_THEORY_MODULE_02_...` | M02 | Mapped |
| `cccco-na-model-curriculum-module-1..9.pdf` | not primary source | — | Supplemental context |
| `CI-ION NATP Final Exam.pdf` | `30_FINAL_EXAM_POOL_50_COMPLETE.md` | M07 | Needs item-match |
| `CI-ION_ Pre-Orientation Student Catalog Test.pdf` | `04_THEORY_MODULE_00_...` | M00 | Needs mapping |
| `CI Institute of Nursing - Course Syllabus.pdf` | `02_THEORY_SYLLABUS_TABLE.md` | all | Compliance review |
| `Day */PM Day * Module *.pdf` | clinical-support / skills | Optional Clinical | Mapped (support only) |

## Gaps Found

- No discrete CCCCO module covers **infection control** (M01). Source is scattered + legacy
  CNA-CE-001 only → SME + source review required (see `00_EXECUTIVE_SUMMARY.md` GAP_LOG).
- Final exam PDF not item-matched to the repo 50-question pool.
- M00 pre-orientation test not yet mapped to orientation identity/ack fields.

## Owner / Action Needed

- SME: confirm clinical accuracy of mapped modules against CCCCO source PDFs.
- Repo Auditor: item-match final exam; map pre-orientation test to M00.

## Blocker Status

Not a production blocker. SME review flags carried to `10_SOURCE_REPAIR_SME_COMPLIANCE_FLAGS.md`.

## Next Verification Step

Open `cccco-na-model-curriculum-module-13.pdf` and compare against `25_THEORY_MODULE_03_...` to
confirm M03 completeness (source-repair risk).
