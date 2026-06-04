# QA Execution Tracker

## Prototype 1 QA Matrix

| Test ID | Scenario | Role | Expected Result | Evidence Needed | Status |
|---|---|---|---|---|---|
| P1-QA-001 | Provider/course approval metadata missing or staging override absent | Learner | Certificate unavailable | Certificate lock screenshot; admin metadata screenshot | Blocked - no staging Moodle access |
| P1-QA-002 | Missing legal name blocks certificate | Learner | Certificate unavailable and profile correction message shown if configured | Profile screenshot; certificate lock screenshot | Blocked - no staging Moodle access |
| P1-QA-003 | Missing CNA number blocks certificate | Learner | Certificate unavailable | Profile export; learner screenshot | Blocked - no staging Moodle access |
| P1-QA-004 | Online cap acknowledgement missing blocks certificate | Learner | Next required gate or certificate locked | Completion report; learner screenshot | Blocked - no staging Moodle access |
| P1-QA-005 | Theory activity skipped blocks certificate | Learner | Final exam or certificate locked | Activity completion report | Blocked - no staging Moodle access |
| P1-QA-006 | Interaction skipped blocks certificate | Learner | Final exam or certificate locked | Interaction completion report | Blocked - no staging Moodle access |
| P1-QA-007 | Active-time threshold not met blocks certificate | Learner | Final exam/certificate locked or admin hold remains active | Active-time report; certificate lock screenshot | Blocked - no staging Moodle access |
| P1-QA-008 | Final exam failed blocks certificate | Learner | Certificate unavailable and remediation message shown if configured | Quiz attempt report | Blocked - no staging Moodle access |
| P1-QA-009 | Affidavit missing blocks certificate | Learner | Certificate unavailable | Affidavit completion report | Blocked - no staging Moodle access |
| P1-QA-010 | Admin hold active blocks certificate | Learner/Admin | Certificate unavailable until hold cleared | Admin hold log; learner screenshot | Blocked - no staging Moodle access |
| P1-QA-011 | Direct certificate URL blocked | Learner | Access denied or unavailable before gates complete | Direct URL attempt screenshot | Blocked - no staging Moodle access |
| P1-QA-012 | Direct final exam URL blocked | Learner | Access denied or unavailable before prerequisites complete | Direct URL attempt screenshot | Blocked - no staging Moodle access |
| P1-QA-013 | Optional clinical support skipped does not block certificate | Learner | Certificate available if all required theory gates pass | Certificate status/issue log; optional completion report | Blocked - no staging Moodle access |
| P1-QA-014 | Optional confidence check skipped does not block certificate | Learner | Certificate availability unaffected | Completion settings screenshot; certificate status | Blocked - no staging Moodle access |
| P1-QA-015 | Optional documentation upload skipped does not block certificate | Learner | Certificate availability unaffected | Upload/stub settings screenshot; certificate status | Blocked - no staging Moodle access |
| P1-QA-016 | Optional clinical support does not inflate required CE progress | Learner/QA | Required progress excludes optional support | Progress/settings screenshot | Blocked - no staging Moodle access |
| P1-QA-017 | Certificate field blank fails QA | Registrar | Certificate blocked or defect logged | Field map; staging PDF or template screenshot | Blocked - no staging Moodle access |
| P1-QA-018 | Unauthorized manual override attempt | Instructor/Support | Override denied | Role test log | Blocked - no staging Moodle access |
| P1-QA-019 | Manual override missing documentation | Admin | QA fails or process blocks undocumented bypass | Override log check | Blocked - no staging Moodle access |
| P1-QA-020 | No PHI collection present | Learner/QA | Prototype has PHI warning and no required PHI collection | Optional hub screenshot; privacy review note | Blocked - no staging Moodle access |
| P1-QA-021 | Mobile required path with optional skipped | Learner | Certificate available only after required gates pass | Mobile screenshots; issue/lock status | Blocked - no staging Moodle access |

## Execution Notes

- Capture pass and fail evidence for each required gate.
- Use test learners only.
- Do not use real PHI or real production certificate records.
- Record defects in the staging QA evidence folder and update `PROTOTYPE_1_OPEN_BLOCKERS.md` when a failure blocks prototype acceptance.
- 2026-05-26: QA execution blocked before Moodle testing because no staging Moodle URL, admin access path, or selected certificate/active-time tooling details were available in the repository.
