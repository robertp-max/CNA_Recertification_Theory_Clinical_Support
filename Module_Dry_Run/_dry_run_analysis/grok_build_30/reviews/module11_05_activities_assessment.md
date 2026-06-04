**# Review 05_activities_assessment — Module 11**

**Verdict:** FAIL

**Top findings:**
- [Critical] Learner-facing quiz distractors contain internal build references: multiple risk-term contexts explicitly list options such as `"id": "C", "label": "Use Module 10 generated content if the nutrition source is incomplete."` (repeated across 4 contexts). Evidence: "Risk-Term Contexts From Generated Data" section pulling from generated JSON.
- [High] Direct contradiction on activity counts: `source_objective_map.json` reports `min_activities=0, max_activities=0`; `data/module11.activities.json` reports `min_activities=3, max_activities=3`. Evidence: Deterministic JSON/CSV Metrics for both files.
- [High] `data/module11.activities.json` metadata shows blank objective titles (`"objective titles: 1. ; 2. ; 3. ; ... 10. "`), while `source_objective_map.json` and `data/module11.content.json` list full titles. Evidence: Deterministic JSON/CSV Metrics for `module11.activities.json`.
- [High] Validation report self-reports "PASS" for `>=3 activities per objective` and `answer_keys_internal_only: True`, but this is contradicted by file metrics and leaked Module 10 references in the same bundle. Evidence: `reports/validation_report.md` table vs. source_objective_map.json and risk contexts.
- [Medium] No actual per-objective activity lists, quiz questions, or distractor sets are present in the evidence bundle despite the activities file existing (size 36584). Evidence: Output File Inventory and Deterministic JSON/CSV Metrics sections (only top-level keys and counts provided).
- [Medium] App integration state shows `contentV2.generated.ts` still imports `module13.content.generated.json` (not module 11), despite final_handoff claiming repoint to Module 11 data. Evidence: Actual Path / File-State Facts and `reports/final_handoff.md`.
- [Low] Activities.json declares exactly 3 activities per objective (min=max=3), but this cannot be verified against source PDF objectives or checked for fit because no activity content is extractable from the bundle. Evidence: `data/module11.activities.json` metadata only.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| >=3 activities per objective | CONFLICTING | source_objective_map.json (min=0); data/module11.activities.json (min=3, max=3); validation_report.md (PASS, "all objectives") |
| Activity fit to objectives | INSUFFICIENT EVIDENCE | No activity samples or per-objective breakdowns; blank titles in activities.json metadata |
| Quiz/distractor quality | FAIL | Multiple "Use Module 10 generated content..." distractors in risk-term contexts from generated data |
| Internal answer-key leakage | FAIL | Build-process references (Module 10) appear in quiz-option contexts despite validation claim of internal-only keys |
| Confusing learner-facing wrong answers | FAIL | Distractors referencing prior module outputs and build artifacts are inappropriate for learners |

**Open questions / residual risks:**
- Actual content of `data/module11.activities.json` (the 36k file) is not provided, so it is impossible to confirm the 3 activities per objective exist, are source-aligned, or avoid the distractor problems shown in risk extraction.
- Whether the Module 10 references are only in the risk-term extraction or are embedded in the final learner-facing `module11.activities.json` / `content.generated.json`.
- No evidence that generated activities were validated against the source PDF (ccccc-na-model-curriculum-module-11.pdf) for fit or that answer keys remain strictly internal.
- Current `contentV2.generated.ts` pointer remains on module13, creating uncertainty whether Module 11 activities would even be served in the app.

**One-sentence go/no-go recommendation.**  
No-go: regenerate activities and assessments to remove all internal Module 10 references from learner-facing content, reconcile the contradictory activity-count metrics across source_objective_map.json and module11.activities.json, and supply actual activity/quiz samples for re-audit before any further use.