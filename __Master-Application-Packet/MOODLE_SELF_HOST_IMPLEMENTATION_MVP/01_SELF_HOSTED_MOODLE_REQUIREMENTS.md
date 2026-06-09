# 01 - Self-Hosted Moodle Requirements

Status: Draft / Pending Approval. Generated Moodle MVP implementation artifact where source technical values were not available locally. Items marked "Technical admin final verification required" must be confirmed by the technical administrator before production install.

## Moodle version recommendation

- Default recommendation: Moodle 4.5 LTS for survey-stable self-hosting and plugin compatibility (long-term support release lifecycle reduces forced upgrades during a survey window).
- Moodle 5.2 may be considered only if all required plugins, import tools (GIFT/CSV question import), themes, and the certificate plugin are verified compatible.
- Version recommendation requires final technical verification before production install. Do not make unsupported version/security-support claims unless verified from current Moodle documentation.
- Action: Technical admin final verification required - confirm the exact current LTS version and its supported PHP/database matrix from current official Moodle documentation at install time.

## Web server requirement

- A supported web server (e.g., Apache or Nginx) configured for the chosen Moodle version.
- HTTPS enforced (see below).
- Technical admin final verification required - confirm exact web server version against the Moodle release's requirements.

## PHP / database requirement

- PHP version and required PHP extensions as specified for the chosen Moodle release.
- A supported database engine (e.g., MariaDB/MySQL or PostgreSQL) at a version supported by the chosen Moodle release.
- Do not hard-code specific version numbers here that are not verified. Technical admin final verification required - confirm PHP version, extensions, and database engine/version from the chosen release's official requirements page.

## HTTPS / domain requirement

- A dedicated domain or subdomain for the LMS.
- Valid TLS certificate; force HTTPS site-wide; set `wwwroot` to the https URL.
- Technical admin final verification required - domain ownership and certificate issuance.

## SMTP / email requirement

- Working outbound email (SMTP) for account creation, password reset, and notifications.
- A monitored no-reply/support mailbox.
- Technical admin final verification required - SMTP host/credentials.

## Cron requirement

- Moodle cron must run on a reliable schedule (e.g., every 1 minute) for completion processing, notifications, scheduled tasks, and backups.
- Technical admin final verification required - cron configured and monitored.

## Backups

- Automated scheduled backups of the database and `moodledata`, plus Moodle automated course backups (.mbz).
- Offsite/secondary copy. See `14_DATA_RETENTION_BACKUP_AND_SECURITY_SPEC.md`.

## Logging

- Standard Moodle logging enabled; logs retained per retention policy; log export available for survey/audit (see `13_REPORTING_AND_AUDIT_EXPORT_SPEC.md`).

## Storage

- Adequate disk for `moodledata`, database, and backups, with growth headroom.
- Technical admin final verification required - sizing based on expected enrollment and media.

## Authentication

- Manual accounts and/or email-based self-registration controlled by admin policy.
- Strong password policy; reviewer accounts use temporary credentials with forced reset (see `04_ROLE_ACCESS_AND_WORKFLOW_MATRIX.md` and `15_REVIEWER_ACCESS_AND_SURVEY_WORKFLOW.md`).
- Multi-factor authentication for privileged accounts where supported. Technical admin final verification required.

## Roles

- Use the role set defined in `04_ROLE_ACCESS_AND_WORKFLOW_MATRIX.md` and `import_assets/ROLE_MATRIX_IMPORT_REFERENCE.csv`, including a custom read-only External Survey Reviewer role.

## Permissions

- Least-privilege configuration. Only Site Administrator / Manager may change site configuration, enable certificates, or perform documented grade overrides.

## Plugin policy

- Minimize plugins. Permitted/expected: a certificate plugin (e.g., a maintained Custom Certificate plugin) kept DISABLED until approval; optionally a configurable reports plugin.
- Only install plugins verified compatible with the chosen Moodle version and from trusted sources. Technical admin final verification required for each plugin.

## Theme / branding

- A maintained, accessible theme; CI Institute of Nursing branding applied conservatively.
- No approval-claim language in branding before approval. See `17_ACCESSIBILITY_AND_MOBILE_REQUIREMENTS.md`.

## Accessibility

- WCAG-oriented configuration (headings, alt text, contrast, captions/transcripts). See `17_ACCESSIBILITY_AND_MOBILE_REQUIREMENTS.md`.

## No-PHI controls

- Learner warnings, activity prompt rules, and a quarantine/deletion process for any PHI accidentally entered. Fictional, de-identified scenarios only. See `16_NO_PHI_AND_PRIVACY_CONTROLS.md`.

## Privacy / security hardening

- Force HTTPS; secure cookies; disable unused features; restrict admin to dedicated accounts; keep Moodle and server patched.
- Configure Moodle privacy/GDPR-style tools and a privacy policy page. Technical admin final verification required - jurisdiction-specific privacy requirements.

## Retention / export

- Define retention for completion evidence and learner records aligned with each lane's recordkeeping requirements (see `14_DATA_RETENTION_BACKUP_AND_SECURITY_SPEC.md`). Exact retention periods: SME/legal verification required.

## Disaster recovery

- Documented restore procedure; periodic restore test (see `08_SURVEY_READINESS_QA_TEST_PLAN.md`, test BR-01). Technical admin final verification required - DR runbook.

## Admin ownership

- A named Site Administrator/Manager owns the environment, configuration, and approvals. (Named human owner assignment: final human verification required - do not fabricate a person.)

## Reviewer account controls

- External Survey Reviewer accounts are read-only, time-limited, forced to reset password on first login, scoped to assigned categories/courses, and deactivated/expired after the survey window. See `15_REVIEWER_ACCESS_AND_SURVEY_WORKFLOW.md`.

## Evidence retention

- Retain completion reports, grade reports, quiz attempts (including failed attempts), logs, certificate issuance logs (post-approval), and course backups in a secure evidence archive for the required retention period (SME/legal verification required for exact periods).
