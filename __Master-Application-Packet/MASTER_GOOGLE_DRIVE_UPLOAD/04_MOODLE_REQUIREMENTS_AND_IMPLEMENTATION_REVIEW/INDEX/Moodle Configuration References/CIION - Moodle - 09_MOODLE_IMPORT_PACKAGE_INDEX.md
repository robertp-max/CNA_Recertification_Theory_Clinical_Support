# 09 - Moodle Import Package Index

Status: Draft / Pending Approval. Indexes all import assets in `import_assets/` and explains how to use them.

## Assets

| file | type | direct import to Moodle? | use |
| --- | --- | --- | --- |
| CNA_GIFT_QUESTION_BANK.gift | GIFT | Yes - Question bank import (GIFT) | CNA questions into `CNA/U01..U12`, `CNA/FINAL` |
| RCFE_GIFT_QUESTION_BANK.gift | GIFT | Yes | RCFE questions into `RCFE/RCFE-CETP-001..009` |
| BRN_GIFT_QUESTION_BANK.gift | GIFT | Yes | BRN questions into `BRN/M01..M10`, `BRN/CAPSTONE_FINAL` |
| CNA_QUIZ_BANK.csv / RCFE_QUIZ_BANK.csv / BRN_QUIZ_BANK.csv | CSV | No (review/staging) | SME review + traceability |
| CNA_QUIZ_BANK.md / RCFE_QUIZ_BANK.md / BRN_QUIZ_BANK.md | Markdown | No | Human-readable SME review |
| COURSE_SHELL_NAMING_CONVENTIONS.csv | CSV | No (reference) | Course short/full names per lane |
| COMPLETION_RULES_IMPORT_REFERENCE.csv | CSV | No (reference) | Activity completion + pass conditions |
| GRADEBOOK_SETUP_REFERENCE.csv | CSV | No (reference) | Grade categories, weights, thresholds |
| RESTRICT_ACCESS_RULES_REFERENCE.csv | CSV | No (reference) | Restrict-access dependencies |
| ROLE_MATRIX_IMPORT_REFERENCE.csv | CSV | No (reference) | Role/permission setup |
| REPORTING_EXPORT_CHECKLIST.csv | CSV | No (reference) | Reports/exports for evidence |
| SME_REVIEW_REQUIRED_QUIZ_ITEMS.md | Markdown | No | Items needing SME/legal sign-off |
| QUIZ_BANK_COVERAGE_AUDIT.csv / .md | CSV/MD | No | Proof of minimum question counts |

## What can be imported directly

- GIFT question banks import directly via Course/Question bank > Import > GIFT format into the matching question category.
- Course backups (.mbz), once built, can be restored across environments.

## What requires manual Moodle setup

- Categories, courses, sections, activities, completion settings, restrict-access rules, gradebook setup, roles, certificate controls, and attestations are built manually per the reference CSVs and course_shells specs (Moodle has no single import for all of these in the MVP).

## Order of import

1. Create categories (CI-CNA-CE, CI-RCFE-CETP, CI-BRN-CM).
2. Create courses (naming conventions CSV).
3. Create question-bank categories per lane (e.g., `CNA/U01`).
4. Import GIFT banks into the matching question categories.
5. Build sections/activities; attach quizzes from the imported bank.
6. Configure gradebook, completion, and restrict-access.
7. Add attestations and (disabled) certificate controls.
8. Provision roles/reviewer accounts.
9. Run QA test plan.

## Naming conventions

- Category naming: `CI-CNA-CE`, `CI-RCFE-CETP`, `CI-BRN-CM`.
- Course naming: per COURSE_SHELL_NAMING_CONVENTIONS.csv (short + full names with "[Draft / Pending Approval]" / "[Pending BRN CEP Approval]").
- Quiz category naming: `CNA/U01`..`CNA/U12`, `CNA/FINAL`; `RCFE/RCFE-CETP-001`..`009`; `BRN/M01`..`M10`, `BRN/CAPSTONE_FINAL`.
- Activity naming: `<UNIT/MODULE> - <Activity Type>` (e.g., `U01 - Unit Quiz`).

## Completion rule references

- See COMPLETION_RULES_IMPORT_REFERENCE.csv and RESTRICT_ACCESS_RULES_REFERENCE.csv.

## Role setup references

- See ROLE_MATRIX_IMPORT_REFERENCE.csv and `04_ROLE_ACCESS_AND_WORKFLOW_MATRIX.md`.
