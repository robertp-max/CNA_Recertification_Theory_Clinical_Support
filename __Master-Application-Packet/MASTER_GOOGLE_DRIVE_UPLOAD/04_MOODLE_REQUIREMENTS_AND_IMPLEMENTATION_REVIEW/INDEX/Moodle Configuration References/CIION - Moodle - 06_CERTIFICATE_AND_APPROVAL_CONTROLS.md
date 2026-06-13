# 06 - Certificate and Approval Controls

Status: Draft / Pending Approval. No certificate may be issued for CE credit before regulator approval. See `generated_missing_elements/GENERATED_CERTIFICATE_GATE_COPY.md` for ready-to-use gate text.

## Certificates disabled before approval

- The certificate activity/plugin is installed but DISABLED (hidden and access-restricted) in every course until approval.
- Course completion may be recorded, but no CE certificate is generated or made available to learners pre-approval.

## Optional internal test certificate

- For internal QA only, a test certificate may be generated if and only if it is watermarked "NOT VALID FOR CE CREDIT" and "DRAFT / PENDING APPROVAL."
- Test certificates are restricted to QA/admin roles and are never available to learners. They are isolated from any production/issuance path.

## Approval metadata required before activation

A certificate cannot be enabled until the following approval metadata fields are populated (these are required gate fields; do not fabricate values):
- Lane (CNA / RCFE / BRN)
- Regulator/approval authority
- Approval/provider number (regulator-issued - final human verification required)
- Approval effective date and expiration (if applicable)
- Approved course title(s) and approved hours/contact hours
- Authorizing signer (legal signature - final human verification required)

## Certificate release gates

A certificate is released to a learner only when ALL are true:
1. Course completion criteria met (all units/modules/course activities complete).
2. Required assessment passed (CNA Final / RCFE final / BRN Capstone) at the configured threshold.
3. Required attestation submitted.
4. Approval metadata present and the "approved" flag set by an authorized role.

## Role authorized to activate

- Only the Site Administrator or Moodle Manager may enable the certificate activity and set the approval flag, and only after approval metadata is verified.

## Certificate fields by lane

- CNA: learner name, course title (12-unit / 24 online CE hours), completion date, "online CE only - not clinical hours," provider info, approval number (post-approval). No clinical hours stated on the certificate.
- RCFE: learner name, course title and approved hours per RCFE-CETP course, completion date, provider info, approval number (post-approval). Certificate must match approved terms after approval.
- BRN: learner name, course title (30 contact hours), completion date, "contact hours" (not CEUs), provider (CEP) info, CEP number (post-approval). No certification claim; no scope-expansion claim.

## No clinical hours on CNA certificate

- CNA certificates state online CE hours only and explicitly do not represent clinical hours or hands-on competency validation.

## BRN contact hours only

- BRN certificates use "contact hours" terminology; never "CEUs" (except explanatory "not CEUs" wording). No obsolete four-hour BRN wording.

## RCFE certificate must match approved terms after approval

- After approval, RCFE certificate wording, course titles, and hours must match exactly what CDSS approved before any issuance.

## Sample certificate isolation

- Any sample/test certificate templates are stored in a non-production context, watermarked "NOT VALID FOR CE CREDIT," and excluded from learner-facing release paths.

## Verification

- Test CT-01 (certificate blocked before approval) and CT-02 (release only after approval metadata) in `08_SURVEY_READINESS_QA_TEST_PLAN.md`.
