**# Review 02_objectives_source_map — Module 10**

**Verdict:** PASS WITH RISKS

**Top findings:**
- [Critical] Hard scope violation on literal Module 10 packet path: `Module10_Dry_Run` is explicitly listed as `exists=False` (kind=missing) in Actual Path / File-State Facts, while all generated artifacts (source_map/, data/, reports/, audio/, media/) and the app root live under `Module_Dry_Run` and `Module_Dry_Run/_module10_dryrun_outputs`. Preflight and final_handoff reports claim `Module10_Dry_Run` as output root and write scope. This directly contradicts the checkpoint requirement for original packet path `Module10_Dry_Run`.
- [High] App content pointer failure breaks Module 10 isolation: `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts` contains `import module13CourseContent from './module13.content.generated.json'; export const courseContentV2 = module13CourseContent;`. Module 10 generated files (`module10.content.generated.json`, `module10.content.json`) exist but are not wired. Evidence: Current active app content pointer block + Current App Data State section.
- [High] Activities layer has empty objective titles despite count compliance: `data/module10.activities.json` reports `objectives: count=16, minute_sum=180, min_activities=3` but lists titles as "1. ; 2. ; 3. ; ... 16. ". This contrasts with full titles in the source map and content JSON. Evidence: Deterministic JSON/CSV Metrics for data/module10.activities.json.
- [Medium] Source map artifact itself meets core counts and mapping: `source_map/source_objective_map.json` (size=75657) has `objectives: count=16, minute_sum=180`, exact 16 titles matching the declared list (e.g., "Define key terminology", "Describe what is meant by vital signs...", up to "Record vital signs on chart, graph, and Nursing Assistant notes"), sample source refs to `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-4` etc., `source_assets: count=17`, and validation dict with `objective_count:16`, `weighted_minutes_total:180`, `answer_keys_internal_only:True`, `backup_content_used_as_authority:False`, `contentv2_used_as_authority:False`. Evidence: Deterministic JSON/CSV Metrics + top-level keys.
- [Medium] Self-reported PASS in validation_report.md is weaker than file metrics and does not catch the above: Report claims "16 objectives present", "weighted minutes total exactly 180", "each objective has >=3 activities", and "answer key internal-only", but activities.json titles are blank and contentV2 pointer is wrong. Evidence: reports/validation_report.md vs. actual JSON contents and file-state facts. Treat self-reported PASS as lower-strength per instructions.
- [Low] Terminology and source assets present in source map: `source_objective_map.json` includes top-level `terminology` and `source_assets` (samples: terminology_list, handout_10_1a, handout_10_1b, handout_10_2, manual_10_3a, manual_10_3b) tied to the official PDF. No contradictory terminology handling observed in the map itself. Evidence: source_map/source_objective_map.json structure.
- [Low] Narration package format gap noted but out of primary scope for this lens: `audio/narration_batch_import_package.json` is MISSING (audio_scripts.csv with 64 rows and audio_manifest.json with status "scripts_only_no_audio_generated" are present). Per guidelines this is a post-patch preference; Module 10 may predate. Evidence: Output File Inventory + Deterministic metrics.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| Objective count exactly 16 | PASS (source map/content) | source_objective_map.json: count=16; data/module10.content.json: count=16; data/content.generated.json references M10 objectives=16 |
| Weighted theory minutes exactly 180 | PASS | source_objective_map.json: theory_minutes_total=180; module10.content.json: total_weighted_minutes=180; time_allotment_report sums per-objective to 180 |
| Objective titles present and source-matched | PASS (source map) / FAIL (activities) | source_objective_map.json + module10.content.json have full 16 titles with PDF page refs; data/module10.activities.json has blank titles ("1. ;") |
| Source references to official PDF | PASS | Multiple `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-X` refs in source_objective_map.json and module10.content.json |
| Source assets mapped (count=17) | PASS | source_objective_map.json: source_assets count=17 with samples |
| Answer keys internal-only | PASS | source_objective_map.json validation: 'answer_keys_internal_only': True; reports/validation_report.md confirms sample_test_answer_key internal-only |
| No backup/ContentV2 as authority | PASS | source_objective_map.json validation flags both False; preflight_report confirms source PDF only |
| Active output/app scope = `Module10_Dry_Run` | FAIL | Actual Path / File-State Facts: Module10_Dry_Run missing; all artifacts and app data under Module_Dry_Run |
| App data correctly points to module10 content | FAIL | contentV2.generated.ts points to module13; module10.*.generated.json files exist but are not exported |

**Open questions / residual risks:**
- Evidence bundle contains direct self-contradiction on directory naming (reports/final_handoff + preflight claim `Module10_Dry_Run` paths and scope; Actual Path / File-State Facts and app pointers show `Module_Dry_Run`). Which state is authoritative for the dry-run packet?
- Is the blank-titles state in data/module10.activities.json an intentional separation of concerns (titles only in source map/content) or a generation defect? The activities JSON still claims 16 objectives and 3 activities each.
- Terminology key exists in source_objective_map.json but no expanded content is provided in the bundle for deeper audit of term coverage or consistency with the PDF.
- `source_map/source_objective_map.md` (size=16800) and `source_map/module10_source_layout.txt` exist but were not sampled for title/ref fidelity in this bundle.

**One-sentence go/no-go recommendation.**  
The core source_objective_map.json and module10.content.json correctly deliver 16 objectives, exactly 180 weighted minutes, PDF page references, 17 source assets, and internal-only answer key handling from the official curriculum PDF, but hard scope/path mismatches (`Module10_Dry_Run` missing vs. `Module_Dry_Run` usage), broken activities titles, and incorrect contentV2 wiring create integration failures that block clean Module 10 isolation.