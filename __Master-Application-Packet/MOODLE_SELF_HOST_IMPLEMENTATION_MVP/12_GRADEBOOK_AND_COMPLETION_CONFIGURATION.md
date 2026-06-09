# 12 - Gradebook and Completion Configuration

Status: Draft / Pending Approval. Companion: `import_assets/GRADEBOOK_SETUP_REFERENCE.csv`, `import_assets/COMPLETION_RULES_IMPORT_REFERENCE.csv`.

## Grade categories

- CNA (`CNA-CE-24`): Unit Quizzes; Scenario/Documentation; Final Assessment.
- RCFE (each course): Course Final; Scenario/Judgment.
- BRN (`BRN-CM-30`): Module Quizzes; Module Activities; Capstone Final.

## Pass thresholds (configurable defaults; confirm with SME/regulator)

- CNA unit quizzes & Final: 80%.
- RCFE course finals: 70%.
- BRN module quizzes & Capstone: 80%.
- Set per quiz under "Grade to pass"; this drives the activity-completion "require passing grade" condition.

## Quiz weighting

- CNA: Unit Quizzes 60%, Scenario/Documentation 10%, Final 30%.
- RCFE: Course Final 80%, Scenario/Judgment 20%.
- BRN: Module Quizzes 50%, Module Activities 20%, Capstone 30%.

## Final assessment weighting

- CNA Final = 30% of course grade and a hard completion gate (must pass).
- RCFE Final = 80% and a hard gate per course (must pass).
- BRN Capstone = 30% and a hard gate (must pass).

## Course completion criteria

- CNA: all 12 units complete AND Final passed.
- RCFE (per course): all required activities complete AND final passed AND evaluation AND attestation.
- BRN: all 10 modules complete AND Capstone passed.

## Activity completion settings

- Pages/Resources: "require view".
- Content with seat-time: "require view" + time guidance (per seat-time policy).
- Interactions/Checkpoints: "require interaction/attempt".
- Quizzes: "require passing grade" (and optionally "require attempts").
- Scenario/Documentation/Evaluation/Attestation: "require submission/attempt" (graded or complete-on-submit).

## Manual override restrictions

- Manual grade or completion overrides are restricted to Manager/Admin roles.
- Every override must be documented (who, when, why) in an override log. Overrides must never be used to bypass a required passing assessment for CE credit.

## Failed attempt handling

- Failed attempts are retained; the activity stays incomplete; gated next activities stay locked until a passing attempt.

## Retake policy

- Multiple attempts allowed; grading method "highest grade" by default. Optional attempt cap before a remediation checkpoint (see `generated_missing_elements/GENERATED_REMEDIATION_RULES.md`).

## Completion export fields

- Learner name/ID, course, activity, completion status, completion date, grade, attempt count, pass/fail. Exported via Reports per `import_assets/REPORTING_EXPORT_CHECKLIST.csv`.
