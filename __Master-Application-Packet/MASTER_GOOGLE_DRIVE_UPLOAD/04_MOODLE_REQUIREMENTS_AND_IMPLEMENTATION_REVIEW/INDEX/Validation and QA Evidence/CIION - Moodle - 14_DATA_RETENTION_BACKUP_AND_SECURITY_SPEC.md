# 14 - Data Retention, Backup, and Security Specification

Status: Draft / Pending Approval. Exact retention periods require SME/legal verification per each regulator's recordkeeping rules.

## Backup schedule
- Automated daily database + `moodledata` backups; automated course backups (.mbz) on a regular schedule.
- Retain a rolling set of backups plus periodic long-term snapshots; keep an offsite/secondary copy.
- Technical admin final verification required - exact cadence and storage targets.

## User data retention
- Retain learner accounts and records per the applicable recordkeeping requirement and privacy policy. Provide a process for data subject requests where required (Moodle privacy tools).

## Course completion evidence retention
- Retain completion reports, grade reports, quiz attempts (incl. failed), logs, and certificate issuance logs (post-approval) in the secure evidence archive.

## BRN record retention alignment
- Align BRN learner/CE completion records and rosters to BRN CEP recordkeeping requirements (contact hours). Exact period: SME/legal verification required.

## RCFE record retention alignment
- Align RCFE course completion and participant records to CDSS/CETP recordkeeping requirements. Exact period: SME/legal verification required.

## CNA record retention alignment
- Align CNA online CE completion records to CDPH recordkeeping expectations. Exact period: SME/legal verification required.

## Encryption / HTTPS
- Force HTTPS site-wide with a valid TLS certificate; secure cookies. Encrypt backups at rest where supported. Technical admin final verification required.

## Admin account control
- Dedicated, named administrator/manager accounts; no shared logins; MFA where supported; least-privilege roles.

## Password rules
- Strong password policy (length/complexity/expiry per policy). Reviewer accounts use temporary passwords with forced reset and account expiration.

## Role review schedule
- Periodically review role assignments (e.g., quarterly) and immediately deprovision accounts no longer needed (especially reviewer accounts after the survey window).

## No-PHI monitoring
- Monitor open-text/submission activities for accidental PHI; apply the quarantine/deletion process in `16_NO_PHI_AND_PRIVACY_CONTROLS.md`.

## Incident escalation
- Define an incident response/escalation path (detect, contain, notify, document) for security or privacy incidents. Named responder assignment: final human verification required - do not fabricate a person. Technical admin final verification required - incident runbook and contacts.
