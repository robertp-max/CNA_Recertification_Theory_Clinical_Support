**# Review 09_data_schema_json — Module 13**

**Verdict:** PASS WITH RISKS

**Top findings:**
- [High] Activities package contains empty objective titles ("1. ; 2. ; 3. ; ...") while source map and content packages contain the full 8 titles. Evidence: `data/module13.activities.json` (and `activities.generated.json`) explicitly lists blank titles; `source_objective_map.json` and `data/module13.content.json` list the complete titles matching the PDF (e.g., "Define key terminology", "Describe the special needs of persons with Alzheimer’s Disease..."). Recommended action: Regenerate activities package to pull titles from source_objective_map.
- [High] Validation report self-reports "PASS" for activities and overall structure, but actual file state shows the title defect. Evidence: `reports/validation_report.md` lists "8 objectives present", ">=3 activities per objective", and "PASS"; contradicts `data/module13.activities.json` metrics. Recommended action: Treat self-reported PASS as low-strength; add explicit title-consistency check to validation.
- [Medium] Two distinct content variants coexist with different sizes and unclear authority: `module13.content.json` (114523 bytes) vs `module13.content.generated.json` / `content.generated.json` (both 170250 bytes). Evidence: File inventory lists both in `_module13_dryrun_outputs/data/` and `standalone-course-mvp/src/data/`. Recommended action: Document which variant is canonical for the app and remove or alias the other.
- [Medium] Narration batch package correctly follows JSON-only rule (csv_used: false, no `audio_scripts.csv`), but all 32 clips remain queued with no audio produced. Evidence: `audio/narration_batch_import_package.json` and `audio/audio_manifest.json` show "scripts_only_no_audio_generated", "qwen_sent": false, clips statuses={'queued_not_generated': 32}. Recommended action: Confirm package shape is sufficient even if audio generation is deferred.
- [Medium] App data pointer is correct but sits alongside duplicate content files. Evidence: `standalone-course-mvp/src/data/contentV2.generated.ts` does `import module13CourseContent from './module13.content.generated.json'; export const courseContentV2 = module13CourseContent;`. Recommended action: Verify runtime loading uses only the intended generated file.
- [Low] Schema files exist and sizes match (`content.schema.json`, `module13.schema.json` both 693 bytes), but no schema validation run or shape diff is present in reports. Evidence: File inventory and deterministic metrics list the files; validation_report.md omits any schema check. Recommended action: Add deterministic schema validation output to future reports.
- [Low] Source map, content JSON, and activities JSON all report exactly 8 objectives and 780 weighted minutes with matching source refs to the PDF. Evidence: `source_objective_map.json` (validation: objective_count=8, weighted_minutes_total=780), `module13.content.json` (same), `module13.activities.json` (same counts, min/max activities=3). Recommended action: Maintain this metric parity as baseline.
- [Low] Top-level keys are consistent where present (module_id, source_authority, objectives array, total_weighted_minutes), but activities JSON omits titles that content and source map include. Evidence: Explicit key lists in deterministic metrics for all three JSONs.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| Objectives count = 8 (declared) | PASS | source_objective_map.json:8; module13.content.json:8; module13.activities.json:8 |
| Weighted minutes total = 780 | PASS | All three files report theory_minutes_total / total_weighted_minutes = 780; matches source_recommended_theory_hours=13 |
| Narration batch package is JSON (no CSV) | PASS | narration_batch_import_package.json: csv_used=false; audio_scripts.csv=MISSING; audio_manifest.json confirms JSON clips |
| Activities per objective >=3 | PASS | module13.activities.json: min_activities=3, max_activities=3 |
| Objective titles consistent across source map / content / activities | FAIL | Activities titles blank; source map + content have full titles from PDF |
| App content pointer correct for Module 13 | PASS | contentV2.generated.ts imports and exports module13.content.generated.json |
| Schema files present | PASS | content.schema.json and module13.schema.json both exist (693 bytes) |
| Source authority and no prior-module contamination in data packages | PASS | All JSONs cite only `ccccc-na-model-curriculum-module-13.pdf`; validation flags backup/contentv2/prior_module_used_as_authority=false |
| Generated content package shape (top-level keys) | PASS WITH RISK | Keys present (module_id, objectives, total_weighted_minutes, etc.); activities titles defect is the only structural gap observed |

**Open questions / residual risks:**
- Why did the activities generation step drop titles while source map and content retained them? Is this a deliberate split or a bug in `source_map/generate_module13_artifacts.py`?
- Do the two content JSON sizes represent intentional staged outputs (raw vs app-ready), or should one be deleted to prevent drift?
- No actual JSON Schema content or validation run (e.g., against content.schema.json) is visible in the bundle; only file presence.
- TTS runtime artifacts (PowerShell parse errors in run_qwen_tts_resume_until_done.ps1, qwen_sent=false) do not break the narration package JSON itself but leave the "required" Qwen path incomplete.
- Self-reported validation PASS is contradicted by deterministic file contents on titles; this pattern reduces trust in other PASS claims.

**One-sentence go/no-go recommendation.**  
Conditional pass on data/schema/JSON with remediation required for blank titles in the activities package and clarification of the duplicate content JSON variants before the artifacts can be treated as consistent.