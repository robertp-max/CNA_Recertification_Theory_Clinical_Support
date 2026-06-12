# 07 - Moodle Build Checklist

Status: Draft / Pending Approval. Each row: task | owner | evidence | pass/fail | severity | notes. Pass/fail left blank for the builder to complete.

| task | owner | evidence | pass/fail | severity | notes |
| --- | --- | --- | --- | --- | --- |
| Site install (chosen Moodle version) | Technical Admin |  screenshot of version page |  | critical | Confirm version per 01 doc; technical verification required |
| HTTPS / domain configured | Technical Admin | https loads; cert valid |  | critical | Force HTTPS; set wwwroot |
| SMTP / email working | Technical Admin | test email received |  | high | Password reset depends on this |
| Cron running | Technical Admin | cron last-run log |  | critical | Completion/notifications depend on cron |
| Roles created (incl. reviewer read-only) | Manager | role list screenshot |  | high | Per ROLE_MATRIX_IMPORT_REFERENCE.csv |
| Categories created (CNA/RCFE/BRN) | Manager/Creator | category tree |  | high | CI-CNA-CE, CI-RCFE-CETP, CI-BRN-CM |
| Courses created (1 CNA, 9 RCFE, 1 BRN) | Creator | course list |  | critical | Per COURSE_SHELL_NAMING_CONVENTIONS.csv |
| Content built (units/modules/sections) | Editing Teacher | section/activity list |  | high | Per course_shells specs |
| Quizzes imported (GIFT) | Editing Teacher | question bank counts |  | critical | 455 items total; verify per category |
| Gradebook configured | Manager | grade setup export |  | high | Per GRADEBOOK_SETUP_REFERENCE.csv |
| Completion enabled/configured | Manager | activity completion settings |  | critical | Per COMPLETION_RULES_IMPORT_REFERENCE.csv |
| Restrict access rules set | Editing Teacher | restriction screenshots |  | critical | Per RESTRICT_ACCESS_RULES_REFERENCE.csv |
| Attestations added | Editing Teacher | attestation activity |  | high | Text from GENERATED_ATTESTATION_TEXTS.md |
| Certificate controls (disabled/gated) | Manager | certificate disabled + gate config |  | critical | No issuance before approval |
| Backups scheduled | Technical Admin | backup schedule + .mbz |  | high | DB + moodledata + course backups |
| Reports verified/exportable | Manager | sample exports |  | high | Per REPORTING_EXPORT_CHECKLIST.csv |
| Reviewer accounts provisioned/tested | Manager | reviewer login (read-only) |  | high | Temporary, forced reset, expiring |
| UAT executed | Manager/Teacher | completed QA test plan |  | critical | Per 08 test plan |
| Legal/privacy review | Compliance/Legal | signoff record |  | critical | Final human verification required |
| Final approval hold confirmed | Manager | no certificate issuance; no approval claims |  | critical | Hard hold until regulator approval |
