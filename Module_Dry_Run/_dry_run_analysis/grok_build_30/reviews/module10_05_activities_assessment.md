**# Review 05_activities_assessment — Module 10**

**Verdict:** PASS WITH RISKS

**Top findings:**
- [High] Direct contradiction on activity counts per objective: `source_map/source_objective_map.json` reports `min_activities=0, max_activities=0` under its objectives array, while `data/module10.activities.json` reports `min_activities=3, max_activities=3`; `reports/validation_report.md` self-reports "each objective has >=3 activities | PASS | all source map objectives have 3 required activities". Evidence: deterministic JSON top-level keys and validation table. Recommended action: reconcile source map vs. activities generation before relying on either.
- [High] `data/module10.activities.json` lists all 16 objective titles as empty strings ("1. ; 2. ; ... ; 16. ") despite claiming exactly 3 activities each and 180 minute_sum; contrast with full titles present in `data/module10.content.json` and `source_map/source_objective_map.json`. Evidence: "objective titles" field in activities.json metrics. This blocks verification of activity fit to the 16 official objectives.
- [Medium] No raw activity text, quiz items, or per-objective activity lists are supplied in the evidence bundle despite `data/module10.activities.json` (62,165 bytes) and `data/content.generated.json` (assessments section) existing; only metadata and 4 scattered quiz-option examples in risk-term contexts. Evidence: absence of excerpts in "Deterministic JSON/CSV Metrics" and report files. Prevents audit of activity fit or quiz/distractor quality.
- [Medium] Self-reported validation PASS for activities is lower-strength evidence per rubric; actual metrics show the above contradictions and blank titles rather than deterministic per-objective activity counts or content. Evidence: `reports/validation_report.md` vs. JSON summaries.
- [Low] Answer-key handling claimed internal-only: `source_map/source_objective_map.json` validation section has `'answer_keys_internal_only': True`; `reports/validation_report.md` states "sample_test_answer_key internal-only" and "no learner-facing key report generated". No explicit leakage found in provided risk-term contexts.
- [Low] Limited distractor examples in risk-term contexts include meta options such as "Use old ContentV2 examples if the PDF is hard to read." (as choice C) and "This would falsely claim online hands-on competency validation." These appear in multiple quiz-like structures but cannot be assessed for plausibility or learner confusion without full `module10.activities.json` content.
- [Low] `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts` currently exports `module13CourseContent` (not module 10), while `module10.activities.json` and `module10.content.generated.json` exist under the same tree; this mismatches the declared `Module10_Dry_Run` packet scope and may affect activity delivery.
- [Low] Path naming inconsistency in bundle: reports and handoff repeatedly reference `Module10_Dry_Run/_module10_dryrun_outputs/...` and `Module10_Dry_Run/standalone-course-mvp`, but "Actual Path / File-State Facts" lists `Module10_Dry_Run` as missing (exists=False) while `Module_Dry_Run` and its `_module10_dryrun_outputs` subdir are present. Evidence: file-state table and report file contents.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| >=3 activities per objective | CONFLICTING | `source_objective_map.json`: min=0/max=0; `module10.activities.json`: min=3/max=3 (titles blank); `validation_report.md`: PASS citing source map |
| Activity fit to objectives | INSUFFICIENT | Blank titles in `module10.activities.json`; no activity descriptions or mappings excerpted; 16 objectives declared but titles empty |
| Quiz/distractor quality | INSUFFICIENT | Only 4 scattered option examples in risk-term contexts; no full quiz items or per-objective activities in bundle |
| Internal answer-key leakage | PASS (per claims) | `source_objective_map.json` validation: answer_keys_internal_only=True; `validation_report.md`: sample_test_answer_key internal-only |
| Confusing learner-facing wrong answers | INSUFFICIENT | No raw quiz content for review; meta distractors (e.g., ContentV2 references) visible in limited contexts but un-auditable |

**Open questions / residual risks:**
- Full text of `data/module10.activities.json` (especially the objectives array contents) is not provided, so activity text, exact quiz wording, and distractor plausibility cannot be directly inspected.
- Whether the 3 activities per objective (if present) are source-traced to the 16 official objectives from `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf` or merely counted in metadata.
- Status of any sample_test_answer_key file or embedded keys relative to learner-facing content (only claims, no file path or excerpt).
- Impact of the contentV2 pointer and path-naming contradictions on actual activity rendering in the app.
- All reports note SME/compliance review is still required; this lens audit cannot substitute for it given the data gaps.

**One-sentence go/no-go recommendation.**  
Conditional go only after the activity-count contradiction between source_objective_map.json and module10.activities.json is resolved, blank titles in activities.json are fixed, and the full activities/quiz content is supplied for direct fit/quality/distractor review.