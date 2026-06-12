# 98 - Missing or Human-Verification Items

Status: Draft / Pending Approval. This list is explicit. Items below are NOT build blockers unless marked TRUE BLOCKER (none are, for the MVP build). Signature/payment/reviewer-credential/regulator-decision items are human-verification items that do not block building the Moodle MVP environment.

## A. Items requiring human verification only (do NOT block MVP build)

| item | lane | type | owner/action | blocks MVP build? |
| --- | --- | --- | --- | --- |
| Regulator approval number(s) | All | Regulator-issued | Enter when issued (CDPH/CDSS/BRN); gate field exists | No |
| Authorizing legal signature | All | Legal signature | Signer signs at submission/activation | No |
| Payment/check numbers (RCFE $410, BRN $750) | RCFE/BRN | Payment data | Finance records actual numbers | No |
| Reviewer account password | All | Credential | Set securely at provisioning; never stored here | No |
| Named admin/owner, privacy/incident contacts | All | Real person data | Assign named staff; do not fabricate | No |
| SME/instructor credential evidence (e.g., resume/CV, license, expiration) | CNA/BRN | Credential data | Attach verified credentials | No |
| Final passing-score confirmation (CDPH/CDSS/BRN) | All | Regulatory judgment | SME/regulator confirms thresholds; defaults set | No |
| Exact record-retention periods | All | Regulatory fact | SME/legal confirm; placeholders noted | No |
| Moodle version + PHP/DB exact values | All | Technical fact | Technical admin verifies from official docs | No |
| Privacy/jurisdiction-specific requirements | All | Legal fact | Legal/compliance confirm | No |

## B. Generated replacement artifacts (created because source artifact was missing/incomplete)

| generated artifact | why generated | review flag |
| --- | --- | --- |
| Quiz banks (CNA 170, RCFE 135, BRN 150) GIFT/CSV/MD | No Moodle-ready item banks existed | SME review; 53 items flagged SME/legal (`SME_REVIEW_REQUIRED_QUIZ_ITEMS.md`) |
| Completion/restrict-access/gradebook/role/reporting reference CSVs | No Moodle config artifacts existed | Admin review |
| Course shell build specs (CNA/RCFE/BRN) | No Moodle shell specs existed | Admin/SME review |
| Generated objectives & activities (per lane) | Build-ready objectives/activities needed | SME review |
| Generated attestation texts | No Moodle attestation copy existed | Legal/compliance review |
| Generated remediation rules | No remediation policy artifact existed | SME review |
| Generated survey reviewer script | No reviewer script existed | Manager review |
| Generated no-PHI learner warnings | No learner-facing warning copy existed | Compliance review |
| Generated certificate gate copy | No gate text existed | Legal/compliance review |

## C. True missing blockers
- None for the Moodle MVP build. All items required to BUILD the self-hosted MVP environment are present or generated. Items in section A are required before public CE issuance / survey submission but do not block constructing and internally testing the MVP. See `99_MOODLE_MVP_FINAL_VALIDATION.md`.
