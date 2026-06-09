# 10 - Moodle Admin Quick Start

Status: Draft / Pending Approval. Practical, step-by-step guide for the Moodle administrator. Menu paths are typical for Moodle 4.5 LTS and may vary slightly by version/theme.

## 1. First login
- Log in with the dedicated Site Administrator account (no shared logins). Confirm HTTPS and version (Site administration > Notifications/Overview).

## 2. Turn on completion
- Site administration > Advanced features > "Enable completion tracking" = Yes.
- In each course: Settings > "Enable completion tracking" = Yes.

## 3. Create categories
- Site administration > Courses > Manage courses and categories > Create new category.
- Create: `CI-CNA-CE`, `CI-RCFE-CETP`, `CI-BRN-CM`.

## 4. Create courses
- Inside each category, create courses per `import_assets/COURSE_SHELL_NAMING_CONVENTIONS.csv` (1 CNA course, 9 RCFE courses, 1 BRN course).
- Use Topics format; create sections per `course_shells/` specs.

## 5. Import quiz banks
- In a course: Question bank > Categories > create `CNA/U01`...`CNA/FINAL` (and RCFE/BRN equivalents).
- Question bank > Import > GIFT format > upload the lane GIFT file > import into the matching category.
- Verify counts against `import_assets/QUIZ_BANK_COVERAGE_AUDIT.md`.

## 6. Configure gradebook
- Course > Grades > Setup > create grade categories and set weights/thresholds per `import_assets/GRADEBOOK_SETUP_REFERENCE.csv`.
- Set each quiz's "Grade to pass."

## 7. Configure restrict access
- On each gated activity: Restrict access > add restriction (Activity completion of the prerequisite, and/or Grade) per `import_assets/RESTRICT_ACCESS_RULES_REFERENCE.csv`.

## 8. Enroll a learner
- Course > Participants > Enrol users > assign Student role to a test learner.

## 9. Create a reviewer
- Site administration > Users > Add a new user (manual auth), force password change.
- Assign the custom read-only External Survey Reviewer role at the relevant category/course context. Set an account/enrollment end date. (Do not store a real reviewer password in this package.)

## 10. Inspect reports
- Course > Reports > Activity completion / Course completion / Logs.
- Course > Grades > Grader report. Quiz > Results > Responses/Statistics.

## 11. Export evidence
- Use Reports/Grades export (CSV/Excel) per `import_assets/REPORTING_EXPORT_CHECKLIST.csv`. Store in the secure evidence archive.

## 12. Block certificates before approval
- Keep the certificate activity hidden/disabled and access-restricted. Do not set the approval flag. See `06_CERTIFICATE_AND_APPROVAL_CONTROLS.md`.

## 13. Backup / restore
- Course > Backup to create .mbz; configure Site administration > Courses > Backups > Automated backup setup. Test Restore into a sandbox (test BR-01).

## 14. Handle failed attempts
- Failed quiz attempts are retained; completion remains incomplete until a passing attempt. Direct learners to remediation per `generated_missing_elements/GENERATED_REMEDIATION_RULES.md`.

## 15. Document admin overrides
- Any manual grade/completion override must be recorded (who/when/why) in an override log. Restrict override capability to Manager/Admin. See `12_GRADEBOOK_AND_COMPLETION_CONFIGURATION.md`.
