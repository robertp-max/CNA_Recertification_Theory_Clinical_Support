**# Review 03_time_allotment — Module 11**

**Verdict:** PASS WITH RISKS

**Top findings:**
- [High] Exact total of 120 weighted theory minutes confirmed by deterministic metrics: `source_map/source_objective_map.json` (theory_minutes_total: 120, objectives count=10, minute_sum=120), `data/module11.content.json` (total_weighted_minutes: 120, objectives count=10, minute_sum=120), and `reports/time_allotment_report.md` ("Total weighted theory minutes: 120"). Evidence: direct JSON top-level keys and report text. Recommended action: retain as primary evidence over self-reported PASS statements.
- [High] Per-objective distribution explicitly listed and sums to exactly 120 in `reports/time_allotment_report.md` (Obj1:8, Obj2:8, Obj3:15, Obj4:14, Obj5:7, Obj6:12, Obj7:15, Obj8:18, Obj9:7, Obj10:16). Evidence: full breakdown in the dedicated report file under `_module11_dryrun_outputs`. Recommended action: cross-verify allocation logic against source PDF page references in `source_objective_map.json`.
- [Medium] Clinical/assessment/certificate minutes explicitly excluded: `reports/time_allotment_report.md` states "Assessment, clinical, certificate, and optional support minutes excluded"; `source_objective_map.json` sets online_clinical_credit_claimed: False, online_hands_on_competency_validated: False, source_recommended_clinical_hours: 6. Evidence: report text + JSON validation block. Recommended action: confirm no leakage into theory minutes in final content files.
- [Critical] Direct contradiction on app integration of the time data: `reports/final_handoff.md` claims "repointing `contentV2.generated.ts` to Module 11 data", but actual file content at `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts` is `import module13CourseContent from './module13.content.generated.json'; export const courseContentV2 = module13CourseContent;`. Evidence: side-by-side report claim vs. provided file content. Recommended action: treat as hard integration failure for this dry-run scope.
- [Medium] Self-reported PASS in `reports/validation_report.md` ("weighted minutes exactly 120 | PASS") and `reports/time_allotment_report.md` is lower-strength than the matching JSON metrics in `source_objective_map.json` and `module11.content.json`. Evidence: report tables vs. parsed JSON values. Recommended action: always prioritize the JSON/path evidence.
- [Medium] Time data present under correct output paths (`Module_Dry_Run/_module11_dryrun_outputs/data/module11.content.json`, `source_map/source_objective_map.json`) with source_authority correctly set to the Module 11 PDF only; no Module10_Dry_Run or ContentV2 used as authority per validation block. Evidence: path inventory + JSON source_authority and validation fields. Recommended action: verify no stale copies override during app load.
- [Low] `data/module11.activities.json` reports minute_sum=120 but shows blank objective titles in the evidence parse ("1. ; 2. ; ..."), while `module11.content.json` and `source_objective_map.json` carry full titles. Evidence: parsed top-level keys and objective summaries. Recommended action: inspect activities.json structure for completeness.
- [Medium] Source-recommended clinical hours (6) are declared separately from theory minutes with no online credit claim, consistent with checkpoint principles for Module 11 (use declared 120 min / 10 objectives). Evidence: `source_objective_map.json` fields + time report exclusion statement.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| Total weighted theory minutes exactly 120 | PASS | source_objective_map.json: theory_minutes_total=120; module11.content.json: total_weighted_minutes=120; reports/time_allotment_report.md: "Total weighted theory minutes: 120" |
| Objectives count = 10 | PASS | source_objective_map.json: count=10; module11.content.json: count=10; source_objective_map.md and time report confirm |
| Per-objective minutes sum to total | PASS | reports/time_allotment_report.md explicit list (8+8+15+14+7+12+15+18+7+16=120); JSON minute_sum=120 |
| Clinical/assessment/certificate exclusion | PASS | reports/time_allotment_report.md explicit statement; source_objective_map.json: online_clinical_credit_claimed=False, source_recommended_clinical_hours=6 |
| Source-recommended vs. theory hours handled correctly | PASS | source_objective_map.json declares source_recommended_clinical_hours=6 separately; no online claim; theory isolated at 120 |
| App content pointer uses Module 11 time data | FAIL | contentV2.generated.ts (size=129) imports module13.content.generated.json despite final_handoff.md claim of repoint to module11 |
| Actual metrics over self-reported PASS | PASS (with caveat) | JSONs and time_allotment_report.md provide deterministic values; validation_report.md PASS is secondary |
| Source authority only (Module 11 PDF) | PASS | All time files (source_objective_map.json, module11.content.json, time report) cite CNA-Recert-Course/CNA_Modules/ccccc-na-model-curriculum-module-11.pdf; validation confirms no backups/Module10/ContentV2 authority |

**Open questions / residual risks:**
- Per-objective minute allocations (e.g., Obj8:18, Obj10:16) are asserted in the time report but lack direct extracted source PDF text in this bundle to prove they derive from the curriculum rather than arbitrary weighting.
- The contentV2.generated.ts pointer to module13 means the audited 120-minute Module 11 time data is not the active app content, creating a disconnect between dry-run outputs and what the standalone-course-mvp would actually load.
- `data/module11.activities.json` minute_sum=120 with blank titles in the parse may indicate incomplete objective metadata even if the sum is correct.
- No evidence of actual PDF page-by-page time extraction details beyond the source refs listed in source_objective_map.json.
- Module_Dry_Run/standalone-course-mvp/src/data/ contains both module11 and module13 files; risk of cross-module leakage if the pointer is not corrected.

**One-sentence go/no-go recommendation.**  
Go for the isolated dry-run outputs (time totals and exclusions match declared 120 min / 10 objectives with source authority), but no-go for app integration until the contentV2 pointer contradiction is resolved and the Module 11 time data is confirmed active.