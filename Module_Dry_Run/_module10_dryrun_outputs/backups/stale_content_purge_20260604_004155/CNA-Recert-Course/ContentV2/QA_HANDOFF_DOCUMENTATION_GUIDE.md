# ContentV2 QA Handoff Documentation Guide

Status: QA handoff guide for the current NATP package model.

This guide tells QA what the current ContentV2 package model is, which files are authoritative, which documents are generated support artifacts, and where to find the evidence needed for review. It does not claim CDPH/TPRU approval, production certificate issuance, hands-on competency validation, clinical-hour credit, or survey approval.

## Current QA Summary

ContentV2 has been rebuilt around NATP Modules 10-17 with a reusable orientation and three package paths:

- Package A: Year 1 Online CE Course, NATP Modules 10-13.
- Package B: Year 2 Online CE Course, NATP Modules 14-17.
- Package C: custom 12-hour NATP package where modules are hand-picked to focus on learner improvement needs.

Shared orientation:

- Internal module ID: `M00`.
- Learner purpose: navigation, privacy, identity, scope, completion evidence, online-hour limits, and certificate boundaries.
- Reusable for Package A, Package B, and Package C.
- Excluded from each package's 720-minute required instructional total.

Current validation facts:

- Required theory instructional total: `720` minutes.
- Displayed lesson minutes including orientation: `750`.
- Estimated active-learning including orientation: `782.73` minutes, about `13.05` hours.
- NATP-only estimated active-learning: about `747.24` minutes.
- Module assessments excluded from instructional time: `85` minutes.
- Final assessment excluded from instructional time: `25` minutes.
- NATP objectives mapped: `72`.
- Coverage status: `64` Covered, `8` Deferred for hands-on or facility-specific performance.
- Failing lessons/modules: `0`.
- Source repair flags: `0`.
- SME review flags: `0`.
- Certificate production enabled: `false`.
- Optional clinical support counts toward theory: `false`.

## Primary Source Files

Use these as the controlling instructional source:

- `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf`
- `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf`
- `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-12.pdf`
- `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-13.pdf`
- `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-14.pdf`
- `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-15.pdf`
- `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-16.pdf`
- `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-17.pdf`

Extracted source text and objectives:

- `CNA-Recert-Course/ContentV2/survey-evidence/_source_text/module-10.txt` through `module-17.txt`
- `CNA-Recert-Course/ContentV2/survey-evidence/_source_text/cccco_objectives.json`

QA note: learner-facing language should say `NATP Module 10`, `NATP Module 11`, etc. The file names still include `cccco` because they come from the source curriculum PDFs and older tooling names.

## Canonical Runtime Data

These are the files QA should treat as the current runtime truth:

- `CNA-Recert-Course/ContentV2/data/courseContentV2.json`
  - Canonical ContentV2 data source.
  - Contains modules, lessons, cards, assessments, compliance guardrails, source manifest, and package-neutral orientation content.

- `CNA-Recert-Course/ContentV2/tools/author_cccco_10_17_course.py`
  - Deterministic authoring tool that rebuilds canonical ContentV2 content from NATP Module 10-17 source inputs.
  - Despite the historical filename, current learner-facing content uses NATP naming.

- `CNA-Recert-Course/ContentV2/tools/rebuild_contentv2_from_json.py`
  - Regenerates generated/mirrored artifacts from canonical JSON.
  - Use this to confirm generated artifacts should not be manually edited independently.

- `standalone-course-mvp/src/data/contentV2.generated.ts`
  - App-consumable generated data.
  - Should match canonical JSON after the rebuild pipeline runs.

## Validation And Audit Files

Use these for QA evidence and pass/fail checks:

- `CNA-Recert-Course/ContentV2/data/generation_validation_summary.json`
  - High-level generated metrics.
  - Confirms module, lesson, card, narration, location, flag, minute, and warning counts.

- `CNA-Recert-Course/ContentV2/qa/time-depth-audit.json`
  - Detailed machine-readable active-learning and time-depth audit.
  - Confirms challenge/debrief cards are counted in active-learning estimates.
  - Confirms assessments and optional clinical support are excluded from required theory minutes.

- `CNA-Recert-Course/ContentV2/qa/TIME_DEPTH_AUDIT.md`
  - Human-readable time-depth audit.
  - Useful for quick review, but if numbers conflict, prefer `time-depth-audit.json`.

- `CNA-Recert-Course/ContentV2/tools/validate_cccco_10_17_rebuild.py`
  - Current global validator for the NATP 10-17 rebuild.
  - Historical filename still says `cccco`; current validation intent is NATP Module 10-17 coverage and compliance.

## Generated ContentV2 Documentation

These files are generated or mirror-style review documents:

- `CNA-Recert-Course/ContentV2/00_CONTENTV2_EXECUTIVE_SUMMARY.md`
  - High-level ContentV2 summary.
  - Use for quick orientation only. Confirm current numbers against validation JSON.

- `CNA-Recert-Course/ContentV2/01_SOURCE_CONTENT_AUDIT.md`
  - Source inventory and audit context.

- `CNA-Recert-Course/ContentV2/02_CONTENTV2_SCHEMA.md`
  - Schema/reference notes for the ContentV2 data structure.

- `CNA-Recert-Course/ContentV2/03_MODULE_LESSON_4CARD_MAP.md`
  - Module, lesson, and card map.
  - Useful for QA navigation through M00 and NATP M10-M17.

- `CNA-Recert-Course/ContentV2/04_MODULE_ASSESSMENT_MAP.md`
  - Module knowledge-check map.

- `CNA-Recert-Course/ContentV2/05_FINAL_ASSESSMENT_MAP.md`
  - Final assessment map.
  - Final assessment answer keys and rationales are internal only and should not be shown to learners.

- `CNA-Recert-Course/ContentV2/06_NARRATION_PRODUCTION_GUIDE.md`
  - TTS/narration production guide.

- `CNA-Recert-Course/ContentV2/07_MEDIA_PROMPT_PLACEHOLDERS.md`
  - Placeholder media prompts and alt-text references.
  - Media is not final clinical demonstration approval.

- `CNA-Recert-Course/ContentV2/08_SME_COMPLIANCE_REVIEW_FLAGS.md`
  - SME/compliance flag summary.
  - Current generated metric reports `0` source repair flags and `0` SME review flags.

- `CNA-Recert-Course/ContentV2/09_APP_INTEGRATION_NOTES.md`
  - App integration notes for the generated data and runtime flow.

- `CNA-Recert-Course/ContentV2/10_CONTENT_COVERAGE_AND_TIME_RECONCILIATION.md`
  - Time and coverage reconciliation.

- `CNA-Recert-Course/ContentV2/11_CONTENTV2_REBUILD_AUDIT.md`
  - Rebuild audit trail and generated artifact context.

## Survey Evidence Documents

Use these for source-to-runtime traceability. These support survey/audit readiness but do not guarantee approval.

- `CNA-Recert-Course/ContentV2/survey-evidence/README.md`
  - Overview of the survey-evidence folder.

- `CNA-Recert-Course/ContentV2/survey-evidence/SOURCE_TO_LESSON_MAP.md`
  - Maps NATP source objectives/topics to ContentV2 module and lesson locations.

- `CNA-Recert-Course/ContentV2/survey-evidence/COVERAGE_BY_SOURCE_MODULE.md`
  - Coverage rollup by NATP source module.

- `CNA-Recert-Course/ContentV2/survey-evidence/ASSESSMENT_EVIDENCE_MAP.md`
  - Assessment coverage evidence.

- `CNA-Recert-Course/ContentV2/survey-evidence/CONTENT_GAPS_AND_DISPOSITIONS.md`
  - Deferred and dispositioned items.
  - Deferred items are generally hands-on or facility-specific performance items, not missing theory.

- `CNA-Recert-Course/ContentV2/survey-evidence/SURVEY_READINESS_COVERAGE_SUMMARY.md`
  - Survey-readiness summary.
  - QA caution: if this file contains older action wording that conflicts with the generated rollup, prefer the current rollup values and `survey_evidence.json`.

- `CNA-Recert-Course/ContentV2/survey-evidence/survey_evidence.json`
  - Machine-readable evidence map.
  - Prefer this file for exact counts/statuses.

## Narration, Media, And XLSX Outputs

- `CNA-Recert-Course/ContentV2/narration/narration_master.csv`
  - Master narration export.

- `CNA-Recert-Course/ContentV2/narration/tts_narration_import.csv`
  - TTS import-ready narration export.

- `CNA-Recert-Course/ContentV2/narration/narration_metadata.json`
  - Machine-readable narration metadata.

- `CNA-Recert-Course/ContentV2/xlsx/CNA_RECERT_CONTENTV2_MASTER.xlsx`
  - Spreadsheet-style master content export.

## Binder And QA Packet Documents

The `_CNA_Recert` folder is an internal documentation/binder package. It is useful for QA and administrative review, but it should be regenerated after ContentV2 changes so it does not fall behind canonical data.

Primary folder:

- `CNA-Recert-Course/_CNA_Recert/CNA-Recert-Course_CNA_Recert/`

Main files:

- `CNA-Recert-Course/_CNA_Recert/CNA-Recert-Course_CNA_Recert/README.md`
  - Binder packet overview.

- `CNA-Recert-Course/_CNA_Recert/CNA-Recert-Course_CNA_Recert/CNA_Recertification_Project_Binder.pdf`
  - PDF binder for internal execution review.

- `CNA-Recert-Course/_CNA_Recert/CNA-Recert-Course_CNA_Recert/CNA_Recertification_Project_Binder.md`
  - Markdown source/version of the binder.

- `CNA-Recert-Course/_CNA_Recert/CNA-Recert-Course_CNA_Recert/CNA_Recertification_Critical_Path_Flowchart.pdf`
  - Flowchart PDF.

- `CNA-Recert-Course/_CNA_Recert/CNA-Recert-Course_CNA_Recert/CNA_Recertification_Critical_Path_Flowchart.png`
  - Flowchart image.

- `CNA-Recert-Course/_CNA_Recert/CNA-Recert-Course_CNA_Recert/CNA_Recertification_Executive_Task_Tracker.xlsx`
  - Executive task tracker workbook.

- `CNA-Recert-Course/_CNA_Recert/CNA-Recert-Course_CNA_Recert/CNA_Recertification_Binder_Source_Index.md`
  - Binder source index.

- `CNA-Recert-Course/_CNA_Recert/CNA-Recert-Course_CNA_Recert/CNA_Recertification_Binder_Build_Report.md`
  - Binder build report.

Generator:

- `CNA-Recert-Course/_CNA_Recert/CNA-Recert-Course_CNA_Recert_build/generate_cna_recert_binder.py`
  - Binder generator.
  - QA caution: if this generator or binder output references old M01-M07 modules, 8 modules, 41 lessons, 277 cards, 447.12 active-learning minutes, source-repair placeholders, or M01/M03/M05 SME signoff, it is stale and must be regenerated or corrected against current ContentV2 data.

## Planning And Visual Review

- `C:\Users\razer\.cursor\plans\cccco_rebuild_722b0afe.plan.md`
  - Current Cursor plan for the NATP Package Model.
  - Tracks completed baseline work and pending Package A/B/C package-runtime work.

- `C:\Users\razer\.cursor\projects\c-AI-Git-CNA-Recertification-Theory-Clinical-Support\canvases\contentv2-reconciliation.canvas.tsx`
  - Visual reconciliation canvas.
  - Use for quick stakeholder review, not as the canonical source of truth.

## QA Review Order

1. Confirm source basis:
   - Review NATP Module PDFs and `_source_text/cccco_objectives.json`.

2. Confirm canonical data:
   - Review `courseContentV2.json`.
   - Confirm M00 is package-neutral and M10-M17 use NATP Module naming.

3. Confirm validation:
   - Review `generation_validation_summary.json`.
   - Review `qa/time-depth-audit.json`.
   - Run or review `validate_cccco_10_17_rebuild.py`.

4. Confirm objective coverage:
   - Review `survey_evidence.json`.
   - Review `SOURCE_TO_LESSON_MAP.md`.
   - Review `CONTENT_GAPS_AND_DISPOSITIONS.md`.

5. Confirm learner/app output:
   - Review `standalone-course-mvp/src/data/contentV2.generated.ts`.
   - Spot-check app pages for package-neutral orientation, NATP module labels, challenge/debrief gating, and no exposed internal answer keys.

6. Confirm binder/docs:
   - Review `_CNA_Recert` files only after they are regenerated from the current model.
   - Check for stale M01-M07 or old minute/card counts.

## Known QA Watch Items

- Package metadata for Package A, Package B, and Package C is planned but not yet fully first-class in canonical data.
- Package C needs explicit enforcement rules for custom module selection and 720-minute reconciliation.
- Some historical files under `ContentV2/source_copy/` preserve old ContentV1/M00-M07 materials. Treat these as historical source-copy references, not current runtime truth.
- Some generated/handoff documents may still carry historical filenames with `cccco`. Current learner-facing terminology should be `NATP Module`.
- The survey summary should not be read as an approval claim. It is evidence support only.
- Certificate production remains disabled pending approval metadata, NAC number, approved wording, affidavit method, and active-time validation.

## QA Questions To Answer

- Does every learner-facing module label say `NATP Module` rather than `CCCCO Module`?
- Does M00 avoid fixed Package A/B content so it can also support custom Package C?
- Are module assessments and final assessment minutes excluded from the 720-minute instructional total?
- Are challenge and debrief cards included in active-learning estimates?
- Are deferred hands-on objectives clearly marked as theory covered but performance not validated online?
- Are answer keys and internal rationales hidden from learner-facing content?
- Are there any PHI prompts, real resident/facility identifiers, certificate-production claims, clinical-hour credit claims, or CDPH approval claims?
- Does `_CNA_Recert` match the current ContentV2 model and not the old M01-M07 model?
