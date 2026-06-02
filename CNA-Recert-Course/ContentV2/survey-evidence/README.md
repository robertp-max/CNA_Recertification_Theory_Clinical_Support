# Survey Evidence (CCCCO/NATP Modules 10–17)

> **This folder does NOT claim or guarantee survey/audit approval.** It is
> defensible, reproducible evidence that every CCCCO/NATP Model Curriculum
> Module 10–17 performance objective is **discussed, mapped, or explicitly
> dispositioned** in ContentV2 — with honest coverage status, assessment links,
> time-depth flags, and gap dispositions. No content is invented and no source
> gaps are hidden.

## Source-of-truth hierarchy

1. **Highest:** `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-{10..17}.pdf`
2. **Crosswalk/implementation:** `CNA-Recert-Course/Content`
3. **Runtime target:** `CNA-Recert-Course/ContentV2/data/courseContentV2.json`

## Files

| File | Purpose |
|---|---|
| `SOURCE_TO_LESSON_MAP.md` / `source_to_lesson_map.csv` | Every CCCCO 10–17 objective → ContentV2 lesson location, coverage status, evidence type, depth flag, note. |
| `COVERAGE_BY_SOURCE_MODULE.md` | Per-source-module status rollup + flagged items. |
| `ASSESSMENT_EVIDENCE_MAP.md` | Module knowledge checks + final-exam evidence per objective. |
| `CONTENT_GAPS_AND_DISPOSITIONS.md` | Honest dispositions: Source Repair / Partial-under-depth / Deferred / Out of Scope / SME Review. |
| `SURVEY_READINESS_COVERAGE_SUMMARY.md` | Executive rollup + honest depth context + top actions. |
| `survey_evidence.json` | Machine-readable mapping (all rows + status counts). |
| `_source_text/` | Extracted CCCCO module text + parsed objectives (`cccco_objectives.json`). |

## How it is generated (reproducible)

```bash
python CNA-Recert-Course/ContentV2/tools/extract_cccco_text.py        # PDF -> text
python CNA-Recert-Course/ContentV2/tools/parse_cccco_objectives.py    # text -> objectives JSON
python CNA-Recert-Course/ContentV2/tools/build_survey_evidence.py     # crosswalk -> evidence artifacts
```

The CCCCO→ContentV2 crosswalk is authored in `tools/build_survey_evidence.py`;
depth, source-repair, and assessment flags are pulled automatically from the
canonical data and the time-depth audit.

## Coverage snapshot (72 objectives)

Covered 27 · Assessed 8 · Partial 18 · Deferred 8 · Source Repair 7 · Out of Scope 1 · SME Review 3.

Key honest gaps: CCCCO **Module 16 (Death & Dying)** maps to **M03/L04**, a
Source Repair placeholder pending SME-authored source; several M02/M04/M05/M06
objectives are addressed but **under-depth** and queued for source-grounded
expansion (no padding).
