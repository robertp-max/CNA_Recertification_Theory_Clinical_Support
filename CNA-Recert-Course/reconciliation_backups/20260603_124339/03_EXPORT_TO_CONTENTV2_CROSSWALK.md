# 03 — Export → ContentV2 Crosswalk

## Purpose

Reconcile the CI-ION export and source documentation against the local ContentV2 package.

## Inputs Reviewed

- `CNA-Recert-Course\ContentV2\` docs `00_…`–`11_…`, `masterprompt.md`.
- `CNA-Recert-Course\ContentV2\data\courseContentV2.json`, `courseContentV2.schema.json`,
  `courseContentV2.ts`, `generation_validation_summary.json`.
- `CNA-Recert-Course\ContentV2\narration\` (`narration_master.csv`,
  `narration_metadata.json`, `tts_narration_import.csv`).
- `CNA-Recert-Course\ContentV2\source_copy\` (full copy of the Content packet).

## Presence Confirmation (Reconciliation Question 13 / Phase 2)

**ContentV2 IS present locally** and is well-populated. It is **not** missing from this clone.
The export predates ContentV2 and does not contain ContentV2 artifacts.

## Evidence Table

| ContentV2 artifact | Present | Maps To | Status |
|---|:--:|---|---|
| `00_CONTENTV2_EXECUTIVE_SUMMARY.md` | Yes | program overview | Present |
| `01_SOURCE_CONTENT_AUDIT.md` | Yes | source audit | Present |
| `02_CONTENTV2_SCHEMA.md` + `courseContentV2.schema.json` | Yes | schema alignment | Present |
| `03_MODULE_LESSON_4CARD_MAP.md` | Yes | lesson card map | Present |
| `04_MODULE_ASSESSMENT_MAP.md` | Yes | module checks | Present |
| `05_FINAL_ASSESSMENT_MAP.md` | Yes | final exam | Present |
| `06_NARRATION_PRODUCTION_GUIDE.md` | Yes | narration | Present (planning) |
| `07_MEDIA_PROMPT_PLACEHOLDERS.md` | Yes | media prompts | Present |
| `08_SME_COMPLIANCE_REVIEW_FLAGS.md` | Yes | SME/compliance | Present |
| `09_APP_INTEGRATION_NOTES.md` | Yes | app wiring | Present |
| `10_CONTENT_COVERAGE_AND_TIME_RECONCILIATION.md` | Yes | time model | Present |
| `11_CONTENTV2_REBUILD_AUDIT.md` | Yes | rebuild audit | Present |
| `data\courseContentV2.json` | Yes | structured content | Present |
| `narration\narration_master.csv` | Yes | narration master | Present |
| `narration\tts_narration_import.csv` | Yes | TTS import | Present (authorization pending) |
| `xlsx\CNA_RECERT_CONTENTV2_MASTER.xlsx` | Yes | master workbook | Present |

## Gaps Found

- ContentV2 lessons have not been cross-checked line-by-line against the export source PDFs
  (CCCCO modules) in this pass — only file-level presence confirmed.
- The export's spreadsheet (`.xlsx`) URL structure is not reflected in ContentV2.
- TTS import CSV exists but TTS authorization is unconfirmed (planning-only).

## Owner / Action Needed

- SME/Instructional Designer: validate ContentV2 lesson content against CCCCO source modules.
- Program Owner/Legal: authorize (or hold) TTS before narration production.

## Blocker Status

Not a production blocker for documentation. TTS authorization is a downstream gate.

## Next Verification Step

Diff `courseContentV2.json` module ordering/timing against `02_THEORY_SYLLABUS_TABLE.md` and the
720-minute model in `06_MODULE_TIME_AND_STRUCTURE_RECONCILIATION.md`.
