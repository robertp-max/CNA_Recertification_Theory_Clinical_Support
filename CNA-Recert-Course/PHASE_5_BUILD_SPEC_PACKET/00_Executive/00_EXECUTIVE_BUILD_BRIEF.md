# Phase 5 Executive Build Brief

**Project:** California CNA Recertification Course in Self-Hosted Moodle  
**Phase:** Phase 5 Build Specification Packet  
**Controlling source:** `FINAL_UNIFIED_IMPLEMENTATION_BLUEPRINT.md`  
**Purpose:** Convert the reconciled blueprint into staging-build artifacts for Moodle admins, instructional designers, registrars, compliance reviewers, RN clinical educators, QA testers, and support leads.

---

## What Is Being Built

| Build Area | MVP Build Decision |
|---|---|
| 12-hour asynchronous theory pathway | Build as a Moodle-based partial California CNA online CE pathway, certificate-disabled until CDPH provider/course approval, NAC#, approved course list, approved certificate wording, and affidavit method are documented. |
| 12-hour clinical practice pathway | Build as optional clinical support, skills refresh, scheduling/resource support, documentation support, and staff support. It remains outside the online CE certificate gate by default. |
| Moodle evidence model | Build layered evidence: identity confirmation, online cap acknowledgement, required theory completion, active-time evidence, interaction/feedback, final exam/test pass, final signed statement/affidavit, certificate fields, issue logs, and audit packet exports. |
| Learner experience | Build mobile-first, low-burden, plain-language flows for exhausted working CNAs. |
| Audit packet | Build export specs and staging proof that records can be reproduced for compliance review. |

## What Is Not Being Built

| Excluded From MVP | Reason |
|---|---|
| New video production | MVP must not depend on new video; use Moodle-native content and authorized TTS only if approved. |
| Final CDPH certificate wording | Must wait for CDPH/legal confirmation. |
| Clinical-hour credit logic | Phase 0 did not verify California renewal clinical-hour requirements; do not add unless CDPH gives written approval. |
| Simulation/LTI clinical credit | Not allowed without written CDPH approval. |
| Automatic trust in time plugins | Active-time plugins are candidates until staging proves behavior and exportability. |
| PHI collection | No PHI should be collected. Clinical documentation must use structured non-PHI fields and warnings. |
| QR verification portal, SMS, custom dashboards | Post-MVP/elite unless required by pilot evidence. |

## MVP Boundaries

- MVP uses self-hosted Moodle with required/optional separation, core activities, validated plugins only, and no new video dependency.
- MVP may use approved cloned-voice TTS only with authorization, approved scripts, transcripts, and version records.
- MVP certificate issuance is disabled until all certificate blockers are closed.
- MVP clinical support is integrated but non-gating and non-credit by default.

## Launch Blockers

| Blocker | Blocks Certificate-Enabled Pilot? |
|---|---|
| CDPH online CE provider/course approval missing | Yes |
| NAC# or approval metadata missing | Yes |
| Approved certificate wording missing | Yes |
| Affidavit signature method unresolved | Yes |
| Active-time control not validated | Yes |
| Audit packet cannot be exported | Yes |
| PHI prevention workflow missing where uploads exist | Yes |
| Optional clinical support accidentally gates certificate | Yes |
| New video incomplete | No; exclude from MVP |

## Certificate Blockers

Certificate release must not be enabled until these are complete:

1. CDPH provider/course approval metadata is active.
2. Learner legal name and CNA certificate number are present.
3. Online cap acknowledgement is complete.
4. Required theory activities are complete.
5. Active-time threshold is met with validated evidence.
6. Required interactions are complete.
7. Final exam/test is passed.
8. Final signed statement/affidavit is complete using an approved method.
9. Required certificate fields populate correctly.
10. Admin hold is clear.
11. Manual override is absent or fully documented.

## Clinical-Support Boundaries

Use only these labels unless compliance approves stronger wording:

- Optional clinical support.
- Skills refresh.
- Practice support.
- Scheduling/resource support.
- Documentation support.

Do not use wording that implies required California renewal clinical hours, clinical-hour credit, or competency validation unless written CDPH approval exists.

## First Staging Prototype Goal

“Prove Moodle can prevent certificate release until identity, required theory completion, active-time evidence, interaction/feedback, final exam/test pass, final signed statement/affidavit, and required certificate fields are complete, while keeping optional clinical support outside the certificate gate.”

## Build Readiness Verdict

### Can Be Built Immediately

- Moodle course/category shell in staging.
- Required vs optional labels and navigation.
- Theory module prototype using placeholder approved-content blocks.
- Optional Clinical Support Hub shell with disclaimers.
- Certificate gate prototype with certificate issuance disabled.
- Audit packet folder/export specification.
- QA negative-test scripts.
- Learner-facing draft copy for compliance review.

### Must Wait for CDPH/Legal Confirmation

- Production certificate release.
- Final certificate wording.
- NAC#/provider approval metadata.
- Course-hour packaging as one certificate or multiple certificates.
- Affidavit signature method.
- Any clinical/in-service credit claim.
- Any simulation credit claim.
- Cloned-voice TTS authorization.

### Must Be Validated in Staging

- Active-time plugin or custom hold.
- Certificate gate behavior.
- Report/export completeness.
- Mobile browser and Moodle app behavior if used.
- Plugin privacy/data behavior.
- Role permissions.
- Backup/restore.
- Optional clinical support non-gating behavior.

### Should Stay Out of MVP

- New video production.
- LTI simulation credit logic.
- QR verification portal unless required by approval.
- SMS reminders.
- Advanced dashboards.
- Custom preceptor workflow beyond basic non-PHI documentation support.

### First Prototype Module to Build

Build **Module 0: Orientation and Compliance Boundaries** plus a minimal **Module 1 interaction/exam prototype**. This proves identity fields, online cap acknowledgement, required theory completion, interaction/feedback, active-time control, final exam/test, affidavit, and certificate lock behavior before building the full course.

### First Staging Prototype Success Criteria

| Success Criterion | Required Result |
|---|---|
| Learner missing legal name or CNA number | Certificate unavailable. |
| Learner skips required theory activity | Exam/certificate unavailable. |
| Learner completes theory but active-time threshold is not met | Exam/certificate unavailable or admin hold remains active. |
| Learner skips interaction/feedback | Final exam/test unavailable. |
| Learner fails final exam/test | Certificate unavailable and remediation message shown. |
| Learner skips affidavit | Certificate unavailable. |
| Learner skips optional clinical support | Certificate still available after all required theory gates pass. |
| Audit export | Test learner packet can be assembled with all required evidence. |
| Mobile test | Learner can complete prototype path on phone without required video. |
