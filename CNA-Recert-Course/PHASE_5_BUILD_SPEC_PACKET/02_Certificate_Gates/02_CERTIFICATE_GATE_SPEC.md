# Certificate Gate Specification

**Purpose:** Define the staging certificate release logic for the online CE theory pathway.  
**Hard rule:** Clinical support completion is not a certificate gate unless CDPH approval is explicitly documented.

---

## Gate Architecture

The online CE certificate must remain disabled in production until CDPH provider/course approval, NAC#, approved course list, approved certificate wording, and affidavit method are documented. In staging, use placeholder gates to prove the logic without issuing a real certificate.

## Certificate Gate Matrix

| Gate | Required? | Moodle Tool / Process | Automated or Manual | Evidence Created | Failure Condition | QA Test | Owner | Launch Blocker? |
|---|---|---|---|---|---|---|---|---|
| CDPH provider/course approval metadata active | Yes | Admin-only approval metadata record + certificate availability hold | Manual admin control | Approval record, NAC#, approved course list reference, approval date | Approval metadata missing, expired, or marked pending | Attempt certificate release with metadata pending | Compliance Lead | Yes |
| Learner legal name present | Yes | Required user profile field | Automated with registrar review | User profile export | Legal name blank or placeholder | Remove legal name and attempt certificate | Registrar | Yes |
| CNA certificate number present | Yes | Required user profile field | Automated with registrar review | User profile export | CNA number blank or invalid format per local validation | Remove CNA number and attempt certificate | Registrar | Yes |
| Online cap acknowledgement complete | Yes | Quiz/Feedback acknowledgement | Automated | Timestamped acknowledgement export | Learner has not acknowledged 24-hour online cap | Skip acknowledgement and attempt next gate | Compliance Reviewer | Yes |
| Required theory activities complete | Yes | Activity completion + course completion | Automated | Activity completion report | Any required theory activity incomplete | Skip one theory activity and attempt exam/certificate | Moodle Admin | Yes |
| Active-time threshold met | Yes | Validated time plugin/custom compliance hold; manual fallback if needed | Automated if validated; otherwise manual admin review | Active-time report, settings, review record | Active time below required threshold or report unavailable | Complete content without time threshold and attempt exam/certificate | Moodle Admin | Yes |
| Required interactions complete | Yes | Lesson, Quiz, H5P, Feedback completion | Automated | Attempt records and completion logs | Required interaction skipped or incomplete | Skip interaction and attempt final exam | Instructional Designer | Yes |
| Final exam/test passed | Yes | Moodle Quiz grade-to-pass | Automated | Quiz attempt, score, timestamp | Final exam/test failed, not attempted, or below approved threshold | Submit failing attempt and attempt certificate | RN Educator / QA | Yes |
| Final signed statement/affidavit complete | Yes | Approved e-sign workflow, Assignment/Feedback, or wet-sign process | Manual or automated depending on approved method | Signed statement record, timestamp, file if applicable | Affidavit missing or signature method not approved | Pass exam but skip affidavit | Registrar / Compliance | Yes |
| Certificate fields populated | Yes | Certificate plugin template fields + profile/course metadata | Automated with registrar QA | Test certificate PDF, field map | Any required field blank, incorrect, or unapproved wording | Generate certificate with blank NAC#/contact field | Registrar | Yes |
| Admin hold clear | Yes | Restricted profile/course field or manual hold log | Manual | Hold/clearance log | Admin hold active for learner or course | Place learner on hold and attempt certificate | Compliance Lead | Yes |
| Manual override absent or documented | Yes | Restricted override form/log | Manual | Override log with approver, reason, date, learner, gate bypassed | Override attempted by unauthorized role or missing documentation | Unauthorized role attempts override | Compliance Lead / QA | Yes |
| Optional clinical support completion | No by default | Optional Clinical Support Hub | N/A | Optional support records only | Misconfigured as certificate condition | Skip all clinical support and complete theory gates | QA Manager | Yes if misconfigured |

## Certificate Template Controls

Certificate template must be locked before pilot and must include only fields confirmed by compliance/CDPH. Do not invent final CDPH wording.

Required field categories for staging test:

- Provider/program name.
- Provider address.
- Contact person/telephone.
- Learner legal name.
- CNA certificate number.
- Course name.
- Completion date.
- CE hours.
- NAC#/provider ID placeholder, disabled until confirmed.
- Online-course indicator placeholder, wording pending approval.
- Retention statement placeholder, wording pending approval.
- Certificate ID.
- Authorized signature line placeholder.
- Partial-credit disclaimer draft, pending approval.

## Manual Override Rule

Certificate-related overrides must be exceptional. Required record:

- Learner.
- Course.
- Gate bypassed.
- Evidence reviewed.
- Approving person.
- Moodle admin performing change.
- Date/time.
- Reason.
- Corrective action.

Unauthorized override attempts must fail.
