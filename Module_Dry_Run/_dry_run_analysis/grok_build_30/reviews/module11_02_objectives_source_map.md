**# Review 02_objectives_source_map — Module 11**

**Verdict:** PASS WITH RISKS

**Top findings:**
- **[Critical]** `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts` imports `module13CourseContent` and exports it as `courseContentV2`, directly contradicting `reports/app_integration_notes.md` and `reports/final_handoff.md` claims that Module 11 data was integrated by repointing this file. Evidence: explicit file content in bundle vs. report text.
- **[High]** `data/module11.activities.json` lists 10 objectives but with completely blank titles ("1. ; 2. ; 3. ; ..."), while `source_map/source_objective_map.json` and `data/module11.content.json` contain the full 10 titles. Evidence: deterministic JSON inspection; activities.json top-level shows `min_activities=3, max_activities=3` but no title strings.
- **[High]** `source_map/source_objective_map.json` validation block correctly sets `module10_outputs_used_as_authority: false`, `contentv2_used_as_authority: false`, and `answer_keys_internal_only: true`, but generated content files contain multiple "Use Module 10 generated content" quiz options and repeated "Module 10" references in learner-facing text. Evidence: risk-term contexts and sample quiz strings in bundle.
- **[Medium]** Self-reported "PASS" in `reports/validation_report.md` and `reports/final_handoff.md` for objective count, minutes, and activities is lower-strength evidence; actual metrics show partial mismatch (activities titles empty) and the contentV2 pointer failure. Evidence: validation table vs. raw JSON states.
- **[Medium]** `data/module11.content.json` and `source_map/source_objective_map.json` both correctly report 10 objectives with 120-minute sum and matching source refs (e.g., `ccccc-na-model-curriculum-module-11.pdf#pages-4`, `#pages-4-5`, etc.), but `data/module11.activities.json` objective titles are not populated from the same source map.
- **[Low]** `source_map/source_objective_map.json` correctly declares `theory_minutes_total: 120`, `objectives: count=10`, `source_authority` as the exact Module 11 PDF, and lists 11 source assets including internal-only answer keys. Evidence: top-level keys and validation object.
- **[Low]** `reports/time_allotment_report.md` provides per-objective breakdown (e.g., Obj 8: 18 min, Obj 3: 15 min) that sums to exactly 120; this aligns with JSON metrics but is not cross-checked against the broken activities.json.
- **[Low]** Audio uses correct JSON narration batch package (`narration_batch_import_package.json`, `csv_used: false`) with 40 queued clips; images are prompt-queue only with alt_text_count=12. These are expected dry-run states but not part of core objective/source-map coverage.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| Declared objectives = 10 | PASS | `source_objective_map.json`: count=10; `module11.content.json`: count=10; titles match declared list |
| Weighted theory minutes = 120 | PASS | `source_objective_map.json`: minute_sum=120; `module11.content.json`: total_weighted_minutes=120; `time_allotment_report.md` sums to 120 |
| Source authority is official Module 11 PDF only | PASS | `source_objective_map.json` and `module11.content.json`: `source_authority: CNA-Recert-Course/CNA_Modules/ccccc-na-model-curriculum-module-11.pdf`; validation flags confirm no backups/ContentV2/Module10 used |
| Objective titles and page refs present and consistent | PARTIAL | Full titles + sample refs (`#pages-4` to `#pages-7-8`) in source_map and content.json; activities.json titles are empty strings |
| contentV2.generated.ts points to Module 11 data | FAIL | File imports `module13.content.generated.json`; contradicts integration claims in reports |
| Answer keys internal-only | PASS | `source_objective_map.json` validation: `answer_keys_internal_only: true`; compliance notes in reports |
| >=3 activities per objective (per validation claim) | UNVERIFIED / PARTIAL | activities.json reports min/max=3 but provides no titles or content; source_map itself shows 0 activities |
| No Module 10 outputs used as authority | PASS | validation block: `module10_outputs_used_as_authority: false`; however, content contains Module 10 references |

**Open questions / residual risks:**
- Activities.json appears to be a partial or failed generation pass from the source map; titles were not transferred despite count and minute fields being populated.
- Persistent "Module 10" strings and "Use Module 10 generated content" quiz options in Module 11 data files indicate possible template leakage or incomplete sanitization during source-map processing.
- The app's active pointer (`contentV2.generated.ts`) remains on Module 13 while Module 11 files exist in `src/data`; this breaks any claim that the dry-run outputs are consumable by the current app build.
- `Module10_Dry_Run` and `Module10_Dry_Run_module10_dryrun_outputs` are missing (exists=False), while all Module 11 outputs are under `Module_Dry_Run/_module11_dryrun_outputs`; scope boundary is respected but the primary packet reference creates path confusion.
- High volume of negated compliance terms ("no clinical-hour credit", "no online hands-on competency validation") still present in generated JSON; these are framed correctly but increase review surface.

**One-sentence go/no-go recommendation.**  
Proceed only after fixing the contentV2 pointer, repopulating activities.json titles from the source map, and removing Module 10 references; the core source_objective_map.json itself meets the 10-objective / 120-minute / PDF-authority criteria but downstream generated artifacts do not.