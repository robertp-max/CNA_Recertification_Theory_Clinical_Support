# QA / UAT Negative-Test Script

**Purpose:** Prove certificate release cannot occur unless required online CE gates are complete, while optional clinical support remains outside the certificate gate.

---

## Hard Rule

Skipping optional clinical support must not block the online CE certificate if all required theory gates are complete.

## Negative-Test Matrix

| Test ID | Scenario | Role | Steps | Expected Result | Evidence Captured | Pass/Fail | Fix Owner |
|---|---|---|---|---|---|---|---|
| QA-001 | Provider/course approval metadata is missing | Learner | Complete all learner gates while admin approval metadata is pending | Certificate unavailable | Certificate status screenshot; approval metadata screenshot | TBD | Compliance Lead |
| QA-002 | Legal name is missing | Learner | Remove/blank legal name, complete all other gates | Certificate unavailable; profile correction message shown | Profile screenshot; certificate lock screenshot | TBD | Registrar |
| QA-003 | CNA number is missing | Learner | Blank CNA certificate number and attempt certificate | Certificate unavailable | Profile export; learner screenshot | TBD | Registrar |
| QA-004 | Online cap acknowledgement missing | Learner | Skip acknowledgement and attempt theory module/exam/certificate | Next required gate or certificate locked | Completion report; learner screenshot | TBD | Compliance Reviewer |
| QA-005 | Theory module skipped | Learner | Skip a required theory activity and attempt final exam/certificate | Final exam or certificate locked | Activity completion report | TBD | Moodle Admin |
| QA-006 | Required interaction skipped | Learner | Complete reading but skip required interaction | Final exam/certificate locked | Interaction completion report | TBD | Instructional Designer |
| QA-007 | Active-time threshold not met | Learner | Complete activities quickly without meeting active-time requirement | Final exam/certificate locked or admin hold remains active | Active-time report; certificate lock screenshot | TBD | Moodle Admin |
| QA-008 | Final exam failed | Learner | Submit final exam below passing threshold | Certificate unavailable; remediation message shown | Quiz attempt report | TBD | RN Educator |
| QA-009 | Affidavit missing | Learner | Pass final exam but skip final signed statement | Certificate unavailable | Affidavit completion report | TBD | Registrar |
| QA-010 | Admin hold active | Learner/Admin | Admin places learner on hold after all learner gates complete | Certificate unavailable until hold cleared | Admin hold log; learner screenshot | TBD | Compliance Lead |
| QA-011 | Optional clinical support skipped | Learner | Complete all required theory gates; skip all clinical hub activities | Certificate available if all required theory gates pass | Certificate issue log; clinical completion report | TBD | QA Manager |
| QA-012 | Optional clinical confidence check skipped | Learner | Skip confidence checks; complete required theory gates | Certificate available if all required theory gates pass | Completion settings screenshot | TBD | QA Manager |
| QA-013 | Clinical upload missing | Learner | Do not submit optional upload; complete all required theory gates | Certificate available if all required theory gates pass | Certificate issue log; upload completion status | TBD | QA Manager |
| QA-014 | Simulation skipped | Learner | Skip all optional simulations/scenarios marked clinical support; complete required theory gates | Certificate available if all required theory gates pass | Completion report | TBD | QA Manager |
| QA-015 | Certificate template field blank | Registrar | Remove required field placeholder from staging template and attempt issue | QA fails; certificate blocked or defect logged | Certificate PDF; field map | TBD | Registrar |
| QA-016 | Unauthorized manual override attempt | Instructor/Support | Non-authorized role attempts to override certificate gate | Override denied | Role test log | TBD | Moodle Admin |
| QA-017 | Manual override missing documentation | Admin | Authorized admin bypasses gate without required override form | QA fails; process blocks or defect logged | Override log check | TBD | Compliance Lead |
| QA-018 | PHI upload negative case | Learner | Upload test file containing fake patient identifiers in clinical support upload | Upload warning shown; admin quarantine/reject process triggered | Warning screenshot; incident log | TBD | Privacy Officer |
| QA-019 | Learner accesses certificate by direct URL | Learner | Use direct URL to certificate activity before gates complete | Access denied or unavailable | URL attempt screenshot | TBD | Moodle Admin |
| QA-020 | Learner accesses final exam by direct URL | Learner | Use direct URL to exam before required gates complete | Access denied or unavailable | URL attempt screenshot | TBD | Moodle Admin |
| QA-021 | Multiple tab time inflation | Learner | Open multiple tabs and attempt to inflate time | Time not double-counted; certificate remains controlled | Time report | TBD | Moodle Admin |
| QA-022 | Mobile completion path | Learner | Complete required path on phone, skipping optional support | Certificate available only after required gates | Mobile screenshots; issue log | TBD | UX Tester |

## Test Evidence Storage

Store test evidence in:

`PHASE_5_BUILD_SPEC_PACKET/08_QA_UAT/Test_Evidence/[YYYYMMDD]_[test_cycle]/`

Suggested files:

- `qa_test_results.csv`
- `screenshots/`
- `exports/`
- `defect_log.md`
- `certificate_gate_settings_snapshot.pdf`

## Pass Criteria

Certificate-enabled pilot cannot begin unless:

- QA-001 through QA-010 pass.
- QA-011 through QA-014 prove optional clinical activities do not block certificate.
- QA-015 through QA-017 pass for certificate integrity.
- QA-018 privacy workflow passes if uploads exist.
- QA-019 through QA-020 pass direct URL bypass tests.
- Active-time tests pass or manual/custom fallback is implemented.
