# 05 - Assessment and Quiz Requirements

Status: Draft / Pending Approval. Quiz banks were generated (see `import_assets/`) and meet minimum counts (see `import_assets/QUIZ_BANK_COVERAGE_AUDIT.md`).

## Quiz design rules

- Question types: MCQ (primary), multi-select where appropriate, true/false (sparingly), matching for terminology only (optional manual build in Moodle), and scenario-based judgment questions (required).
- No trick questions. No unsupported clinical/legal claims. No PHI. No real resident/patient names. Fictional, de-identified scenarios only.
- Each item includes a rationale/feedback for learning.
- Items requiring legal/regulatory or clinical precision that is not source-backed are flagged for SME/legal review (see `import_assets/SME_REVIEW_REQUIRED_QUIZ_ITEMS.md`).

## Import format rules

- GIFT files use valid GIFT syntax, unique question names (`<LANE>-<CATEGORY>-Q##`), escaped special characters, and `#### feedback` where feasible.
- CSV files use the fixed field order (below) for traceability and SME review; CSV is a human/AI review and re-import-staging format (Moodle direct import uses GIFT).
- Markdown files are human-readable mirrors for SME review.
- CSV fields: `question_id,lane,category,course_unit_module,objective,question_type,question_text,option_a,option_b,option_c,option_d,option_e,correct_answer,rationale,difficulty,source_reference,sme_review_status,moodle_import_category`.

## Passing score

- CNA unit quizzes and Final: default 80% (configurable; confirm with SME/CDPH).
- RCFE course final assessments: default 70% (configurable; confirm with SME/CDSS).
- BRN module quizzes and Capstone: default 80% (configurable; confirm with SME/BRN).
- Thresholds are set in the Quiz "grade to pass" and used as the activity-completion pass condition.

## Retakes

- Multiple attempts allowed; "highest grade" used for grade-to-pass by default (configurable).
- All attempts (including failed attempts) are retained and exportable (survey evidence).
- A failing result blocks completion and the next gated activity until a passing attempt is achieved.

## Remediation

- On a failed attempt, the learner is directed back to the relevant content before re-attempting (see `generated_missing_elements/GENERATED_REMEDIATION_RULES.md`).
- Optional attempt limits before a manual review/remediation step may be configured.

## Item security

- Question bank organized by Moodle categories (`CNA/U01`...`CNA/FINAL`, `RCFE/RCFE-CETP-001`...`009`, `BRN/M01`...`M10`, `BRN/CAPSTONE_FINAL`).
- Shuffle questions and answers; restrict review options so learners do not see the full answer key.
- Limit question-bank visibility to teacher/manager roles.

## Answer key handling

- The full answer key (correct answers + rationales) is for SME/admin use only.
- Learners receive feedback per attempt per the configured review options but never a downloadable master answer key.

## SME review workflow

1. SME reviews each lane's Markdown bank and the SME-flagged items list.
2. SME confirms/edits correct answers, rationales, and any legal/clinical precision items.
3. Approved items are imported via GIFT into the correct Moodle question category.
4. SME sign-off recorded (final human verification - do not fabricate a signature).

## No final answer key shown to learners

- Quiz review options are configured to withhold the correct-answer key during/after attempts as appropriate; only per-item feedback (if enabled) is shown. This is verified in test QZ-04 (`08_SURVEY_READINESS_QA_TEST_PLAN.md`).

## Minimum quiz generation (met)

- CNA: 12 unit banks x 10 = 120 + Final 50 = 170 (met).
- RCFE: 9 course banks x 15 = 135 (met).
- BRN: 10 module banks x 12 = 120 + Capstone 30 = 150 (met).
- Overall: 455 questions (met). See `import_assets/QUIZ_BANK_COVERAGE_AUDIT.md`.

## Question item required fields (every item)

question_id, lane, course/unit/module, objective, question_type, question_text, options, correct_answer, rationale, difficulty, source_reference, SME_review_status, Moodle_import_category - all present in the CSV banks.
