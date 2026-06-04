**# Review 09_data_schema_json — Module 11**

**Verdict:** FAIL

**Top findings:**
- [Critical] `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts` contains `import module13CourseContent from './module13.content.generated.json'; export const courseContentV2 = module13CourseContent;`, directly contradicting claims in `final_handoff.md` and `app_integration_notes.md` that it was repointed to `module11.content.generated.json`.
- [High] `data/module11.activities.json` lists 10 objectives with completely empty titles ("1. ; 2. ; 3. ; ...") and `min_activities=3, max_activities=3`, while `source_objective_map.json` and `data/module11.content.json` both list the same 10 objectives with full titles and `min_activities=0, max_activities=0`. Direct schema/content inconsistency across packages.
- [High] `data/content.generated.json` (and mirrored `module11.content.generated.json`) embeds multiple "Use Module 10 generated content if the nutrition source is incomplete" strings as quiz option labels (4+ contexts), violating source-first rule and introducing stale cross-module references.
- [High] `source_objective_map.json` validation block claims clean authority (`backup_content_used_as_authority: false`, `contentv2_used_as_authority: false`, `module10_outputs_used_as_authority: false`), but actual generated content and app pointer state contradict this.
- [Medium] Narration package is correctly JSON-only (`audio/narration_batch_import_package.json` has `csv_used: false`, 40 clips, `status: scripts_only_no_audio_generated`); however `audio/audio_scripts.csv` is explicitly MISSING.
- [Medium] `data/module11.content.json`, `module11.activities.json`, and `source_objective_map.json` all report exactly 10 objectives and 120 weighted minutes matching declared values, but `activities.json` title stripping and activity-count mismatch (0 vs 3) break cross-package consistency.
- [Medium] `data/content.generated.json` only lists `['M11:NATP Module 11: Nutrition objectives=10']`, yet `src/data/` contains full `module10.*`, `module11.*`, and `module13.*` files with the active pointer on module13.
- [Low] `data/module11.schema.json` (558 bytes) and `module11.content.generated.json` (165179 bytes) exist in both `_module11_dryrun_outputs/data/` and app `src/data/`, but no schema shape validation output or enforcement evidence is present in the bundle.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| Objectives count = 10 (Module 11 declared) | PASS | `source_objective_map.json`:10, `module11.content.json`:10, `module11.activities.json`:10, `time_allotment_report.md`:10 |
| Weighted theory minutes = 120 | PASS | `source_objective_map.json`:120, `module11.content.json`:120, `time_allotment_report.md`:120 (sum of per-objective values) |
| Narration batch package is JSON, no CSV | PASS | `narration_batch_import_package.json` (`csv_used: false`, 40 clips); `audio_manifest.json` present; `audio_scripts.csv` MISSING |
| Consistency across source_map, module11.content.json, module11.activities.json | FAIL | Empty titles + 0-vs-3 activities mismatch in activities.json vs full titles + 0 activities in content/source_map |
| App data pointer uses Module 11 content | FAIL | `contentV2.generated.ts` imports module13; `module11.content.generated.json` and `module11.generated.ts` exist but are not referenced |
| Source authority limited to Module 11 PDF only | PASS (partial) | All three JSONs cite `cccco-na-model-curriculum-module-11.pdf`; contradicted by embedded "Module 10" strings |
| Schema files present | PASS | `module11.schema.json` (558 bytes) exists in outputs and app src/data |
| No stale Module 10 / backup authority in generated content | FAIL | Multiple "Use Module 10 generated content" quiz labels in `content.generated.json` contexts |

**Open questions / residual risks:**
- No actual content of `module11.schema.json` is supplied, so shape enforcement (e.g., required fields for objectives/activities) cannot be verified beyond file existence and size.
- Activities.json appears to be a malformed or partially generated package (titles stripped, activity counts inflated); unclear if this is intended structure or generation defect.
- Reports (`validation_report.md`, `final_handoff.md`) uniformly self-report PASS on app integration and consistency, but deterministic file contents contradict them on the two most critical items (pointer + activities titles).
- Presence of full module10 and module13 data files in the same `src/data/` directory as the module11 outputs creates risk of accidental cross-loading even if pointer were corrected.
- `data/content.generated.json` (165179 bytes) duplicates the size of `module11.content.generated.json`; unclear which is the authoritative package for the app.

**One-sentence go/no-go recommendation.** No-go: regenerate activities.json with correct titles and activity counts, correct the contentV2.generated.ts pointer to module11, and re-validate cross-package consistency before any further use or build.