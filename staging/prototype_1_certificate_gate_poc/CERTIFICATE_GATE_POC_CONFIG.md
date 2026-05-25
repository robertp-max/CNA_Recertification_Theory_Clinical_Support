# Certificate Gate POC Configuration

## Gate Logic

The certificate activity must remain disabled or clearly marked staging-only unless all required gates are complete and approval metadata is active or a documented staging override is present.

Optional clinical support completion is explicitly not a certificate gate.

## Gate Matrix

| Gate | Prototype Method | Moodle Tool / Process | Automated or Manual | Evidence | QA Negative Test |
|---|---|---|---|---|---|
| Provider/course approval metadata active or staging override | Admin-only placeholder record and certificate availability hold | Restricted admin archive plus certificate restriction/admin hold | Manual | Staging override record, approval metadata placeholder, screenshot | QA-001: approval metadata pending blocks certificate |
| Legal name present | Required profile field check | User profile field and registrar review | Automated with manual review | Profile export | QA-002: missing legal name blocks certificate |
| CNA certificate number present | Required profile field check | User profile field and registrar review | Automated with manual review | Profile export | QA-003: missing CNA number blocks certificate |
| Online cap acknowledgement complete | Learner submits acknowledgement | Feedback or Quiz acknowledgement | Automated | Timestamped acknowledgement export | QA-004: missing acknowledgement blocks certificate |
| Required theory activity complete | Sample theory activity completion | Page, Book, or Lesson completion | Automated | Activity completion report | QA-005: theory activity skipped blocks certificate |
| Required interaction complete | Required interaction attempt submitted | Quiz, Lesson question, H5P, or Feedback completion | Automated | Attempt/completion export | QA-006: interaction skipped blocks certificate |
| Active-time threshold met or admin-reviewed | Candidate time plugin threshold or manual review hold cleared | Time plugin report, custom hold, or admin hold | Automated if validated; otherwise manual | Active-time report or admin review record | QA-007: threshold not met blocks certificate |
| Final exam/test passed | Grade-to-pass condition | Moodle Quiz | Automated | Quiz attempt, score, timestamp | QA-008: failed exam blocks certificate |
| Final signed statement/affidavit complete | Statement submitted or reviewed | Feedback, Assignment, e-sign placeholder, or wet-sign workflow placeholder | Manual or automated pending approval | Statement completion record | QA-009: affidavit missing blocks certificate |
| Certificate fields populated | Field map verified before issue | Certificate plugin template fields plus profile/course metadata | Automated with registrar QA | Field map screenshot, staging PDF if generated | QA-015: blank certificate field fails QA |
| Admin hold clear | Admin hold field/log cleared | Restricted profile/course field or admin-only hold log | Manual | Hold and clearance log | QA-010: admin hold active blocks certificate |
| Manual override absent or documented | Override path restricted and logged | Restricted override form/log | Manual | Override log with approver, reason, date, learner, gate bypassed | QA-016 and QA-017: unauthorized or undocumented override fails |
| Direct certificate URL blocked | Availability restrictions apply to direct URL access | Restrict Access and role permissions | Automated | Direct URL attempt screenshot | QA-019: direct certificate URL blocked |
| Direct final exam URL blocked | Exam unavailable until prerequisites complete | Restrict Access and role permissions | Automated | Direct URL attempt screenshot | QA-020: direct final exam URL blocked |
| Optional clinical support completion is NOT a gate | Optional activities excluded from certificate restrictions and required course completion | Optional clinical support section/course settings | N/A | Settings screenshot showing no dependency | QA-011, QA-012, QA-013: optional support skipped does not block certificate |

## Required Restrict Access Chain

1. Orientation and online cap acknowledgement unlock the sample theory module.
2. Sample theory module unlocks the required interaction/check.
3. Required interaction/check plus active-time threshold or admin review unlocks the final exam/test.
4. Final exam/test pass unlocks the final signed statement/affidavit.
5. Certificate remains disabled or staging-only gated until all required gates, certificate fields, approval metadata/staging override, and admin hold clear are satisfied.

## Staging Certificate Rule

If a certificate PDF is generated during Prototype 1, it must be watermarked or labeled as staging/test only and must not be treated as a production CE certificate.
