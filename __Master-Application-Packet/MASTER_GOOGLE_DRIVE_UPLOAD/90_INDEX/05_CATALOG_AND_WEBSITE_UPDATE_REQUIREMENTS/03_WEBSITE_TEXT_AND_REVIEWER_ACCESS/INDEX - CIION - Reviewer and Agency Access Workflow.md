# 15 - Reviewer Access and Survey Workflow

Status: Draft / Pending Approval. Companion reviewer-facing script: `generated_missing_elements/GENERATED_SURVEY_REVIEWER_SCRIPT.md`.

## Reviewer account request
- A reviewer (regulator surveyor, internal compliance, or designated evaluator) requests access for a defined window. Manager records the request (who, scope, dates).

## Account setup
- Manager creates a manual-auth account with a non-personal username (e.g., `surveyreviewer1`), a strong temporary password (delivered securely - not stored in this package), and "force password change on next login."

## Read-only role
- Assign the custom External Survey Reviewer role (read-only) at the assigned category/course context only. The role has no edit, grade, enrollment, or certificate capabilities.

## Reviewer dashboard / course list
- Provide the reviewer a simple list of the courses in scope (CNA course; the 9 RCFE courses; BRN course as applicable) with read-only access and a short orientation (the reviewer script).

## Report export packet
- Provide the prepared read-only evidence bundle (see `13_REPORTING_AND_AUDIT_EXPORT_SPEC.md`): completion reports, grade reports, quiz attempt summaries, structure screenshots, coverage audit, and (post-approval) certificate logs. De-identified; no PHI.

## Temporary credential control
- Credentials are temporary, single-purpose, and time-boxed to the survey window. No reuse across windows.

## Deactivation
- After the survey window, suspend or delete the reviewer account; revoke role assignments; record deactivation date. Capture reviewer-account access logs as evidence.

## Screenshot / evidence package
- Maintain dated screenshots of: locked content before prerequisites, quiz pass/fail gating, certificate disabled pre-approval, completion/grade exports, and reviewer read-only view.

## Survey day checklist
1. Confirm reviewer account active, read-only, scoped, expiring.
2. Confirm no certificate issuance and no approval-claim language.
3. Confirm structure matches: CNA 12x2=24; RCFE 9 courses/27h; BRN 10x3=30 contact hours.
4. Confirm no stale BRN 4-hour language; contact hours only.
5. Confirm no PHI in any activity/submission.
6. Have evidence bundle and QA test results ready.
7. Provide the reviewer script and answer access questions only (no edits during survey).
8. After: deactivate reviewer account; archive logs and evidence.
