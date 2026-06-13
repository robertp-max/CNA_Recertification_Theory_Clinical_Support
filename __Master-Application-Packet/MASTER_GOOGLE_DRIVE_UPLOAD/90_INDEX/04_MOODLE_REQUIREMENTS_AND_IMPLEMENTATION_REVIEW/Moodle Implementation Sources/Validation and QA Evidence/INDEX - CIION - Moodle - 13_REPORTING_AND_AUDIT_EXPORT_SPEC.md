# 13 - Reporting and Audit Export Specification

Status: Draft / Pending Approval. Companion: `import_assets/REPORTING_EXPORT_CHECKLIST.csv`.

## Logs report
- Source: Reports > Logs. Captures user/admin actions, access times, IP (per privacy policy). Export CSV/Excel. Use for audit trail and reviewer-access evidence.

## Activity completion report
- Source: Reports > Activity completion. Per-learner, per-activity completion status. Demonstrates content/seat-time completion. Export CSV/Excel.

## Course completion report
- Source: Reports > Course completion. Overall completion status and date per learner. Demonstrates gating works. Export CSV/Excel.

## Grade report
- Source: Grades > Grader report / User report. Quiz and activity grades, pass/fail. Demonstrates thresholds enforced. Export CSV/Excel.

## Quiz attempts report
- Source: Quiz > Results > Responses / Statistics. All attempts including failed attempts retained. Demonstrates retake history. Export CSV/Excel.

## Configurable reports (if used)
- Optional configurable/custom reports plugin (verify compatibility) to combine completion + grade + time evidence into one survey bundle.

## Certificate report (if used)
- Post-approval only: certificate issuance log showing certificates issued after the approval flag was set. Pre-approval, this report should show zero issued certificates.

## Backup/export package
- Course backups (.mbz) per course; full-site DB + moodledata backups. Stored with offsite copy.

## Evidence retention location
- A secure evidence archive (access-controlled) holds exported reports, attempt data, logs, certificate logs (post-approval), and course backups. Exact retention periods: SME/legal verification required (align to CNA/RCFE/BRN recordkeeping).

## Reviewer export bundle
- A prepared, read-only bundle (folder/ZIP) for the survey reviewer containing: completion reports, grade reports, quiz attempt summaries, logs (reviewer-relevant), structure screenshots, and the coverage audit. No PHI; de-identified. See `15_REVIEWER_ACCESS_AND_SURVEY_WORKFLOW.md`.
