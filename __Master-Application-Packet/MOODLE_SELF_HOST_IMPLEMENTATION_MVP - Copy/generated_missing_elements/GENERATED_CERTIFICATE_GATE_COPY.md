# Generated Certificate Gate Copy

Status: Draft / Pending Approval. Generated Moodle MVP implementation artifact. Legal/compliance review required. See 06_CERTIFICATE_AND_APPROVAL_CONTROLS.md.

## Pre-approval hold (controlling state)
Display wherever a certificate would otherwise be available:
"Continuing-education certificates are not available for this course. This course is pending regulatory approval. No CE certificate will be issued until approval is granted and approval metadata is configured."

## Sample/test certificate watermark (if an internal test certificate is enabled)
"NOT VALID FOR CE CREDIT - SAMPLE / TEST ONLY - PENDING REGULATORY APPROVAL"

## Required approval metadata (must be set by authorized role before any certificate release)
- Regulator/approval body
- Approval/provider number [Final human verification required - regulator-issued]
- Approval effective date [Final human verification required]
- Approved course title and hours/contact hours
- Authorized signer name/title [Final human verification required]

## Post-approval certificate copy (activate only after approval)
- CNA: "[Learner] completed [Course Title], [X] online continuing-education hours. Online CE only; no clinical hours. Provider/approval no.: ____. Date: ____."
- RCFE: "[Learner] completed [Course Title], [X] hours of RCFE continuing education. Approval/vendor no.: ____. Date: ____." Wording must match approved terms.
- BRN: "[Learner] completed [Course Title], [X] contact hours of RN continuing education (not CEUs). CEP provider no.: ____. Date: ____." No certification or scope-expansion claim.

## Release gate (authorized role: Manager/Site Admin only)
Certificate release is permitted only when: regulator approval granted; approval metadata complete; certificate wording matches approved terms; pre-approval audit preserved; backup taken. See 20_POST_APPROVAL_ACTIVATION_PLAN.md.
