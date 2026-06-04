**# Review 09_data_schema_json — Module 10**

**Verdict:** CONDITIONAL PASS

**Top findings:**
- [Critical] Declared active scope `Module10_Dry_Run` (per packet and checkpoint) is missing (exists=False); all generated data/schema artifacts are under `Module_Dry_Run/_module10_dryrun_outputs` and `Module_Dry_Run/standalone-course-mvp/src/data/`. Evidence: Actual Path / File-State Facts + Output File Inventory. Violates literal Module 10 packet path requirement.
- [Critical] App data pointer is wrong: `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts` imports `module13CourseContent` and exports it as `courseContentV2`. Evidence: explicit TS snippet in bundle. Breaks consistency for Module 10 app data package despite module10.* files existing.
- [High] Objective titles are empty in activities package: `data/module10.activities.json` reports count=16 and minute_sum=180 with min/max_activities=3, but titles are literally `"1. ; 2. ; 3. ; ... 16. "`. Evidence: Deterministic JSON/CSV Metrics section. Source_map and module10.content.json have full matching titles.
- [High] Required narration batch JSON is absent: `audio/narration_batch_import_package.json: MISSING` (rubric preference is JSON batch package post-orchestration patch). Evidence: Deterministic JSON/CSV Metrics. Only `audio_scripts.csv` (64 rows) and `audio_manifest.json` (status: scripts_only_no_audio_generated) exist.
- [Medium] Schema file is present but minimal and unaudited in detail: `data/module10.schema.json` (size=560). Evidence: Output File Inventory. No shape/content provided for cross-check against content/activities.
- [Medium] Strong consistency on core metrics where present: `source_map/source_objective_map.json` and `data/module10.content.json` both show exactly 16 objectives, 180 minutes, matching titles, and source refs to the PDF. Evidence: top-level keys + objectives sections in Deterministic JSON/CSV Metrics.
- [Medium] `data/content.generated.json` (size=233269) correctly packages M10 (`generated modules: ['M10:NATP Module 10: Vital Signs objectives=16']`) with top-level keys including modules/assessments. Evidence: Deterministic JSON/CSV Metrics.
- [Low] Self-reported "PASS" in `reports/validation_report.md` and `reports/final_handoff.md` (including "16 objectives present", "weighted minutes total exactly 180") is lower-strength than the deterministic path/activities/pointer contradictions above. Evidence: Report File Contents sections.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| 16 objectives + exactly 180 min in source_objective_map.json | PASS | count=16, minute_sum=180, full titles, validation dict confirms |
| 16 objectives + exactly 180 min in module10.content.json | PASS | count=16, minute_sum=180, matching titles and source refs |
| 16 objectives + 180 min in module10.activities.json | PASS (partial) | count=16, minute_sum=180, min/max_activities=3; titles empty |
| Narration batch package (JSON) present | FAIL | narration_batch_import_package.json: MISSING; only CSV present |
| module10.schema.json present | PASS | size=560 under data/ |
| content.generated.json includes M10 correctly | PASS | top-level keys + 'M10:NATP Module 10: Vital Signs objectives=16' |
| Objective title consistency across source_map / content.json / activities | FAIL | Full titles in first two; blank in activities.json |
| App data pointer matches Module 10 | FAIL | contentV2.generated.ts points to module13 |
| Path scope matches declared `Module10_Dry_Run` | FAIL | Module10_Dry_Run missing; artifacts under Module_Dry_Run |

**Open questions / residual risks:**
- Whether the activities.json empty titles are a generation artifact or downstream consumer issue (affects lesson player / activity rendering).
- Status of `module10.schema.json` shape validation (size only; no content in bundle for audit).
- Whether the `Module_Dry_Run` vs `Module10_Dry_Run` mismatch is a one-time execution artifact or indicates broader scope drift that affects reproducibility of the data package.
- No deterministic evidence of narration_batch_import_package.json ever being generated despite CSV output.

**One-sentence go/no-go recommendation.** No-go for production data package use until path scope, contentV2 pointer, activities titles, and missing narration JSON batch are resolved; the core source_map + content.json metrics are solid but the package as a whole is inconsistent.