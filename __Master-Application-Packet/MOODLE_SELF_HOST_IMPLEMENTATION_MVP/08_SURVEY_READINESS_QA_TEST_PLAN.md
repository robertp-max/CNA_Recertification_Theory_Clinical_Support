# 08 - Survey Readiness QA Test Plan

Status: Draft / Pending Approval. Each test case: ID | purpose | steps | expected result | evidence artifact | severity | pass/fail (placeholder).

| ID | purpose | steps | expected result | evidence | severity | pass/fail |
| --- | --- | --- | --- | --- | --- | --- |
| LG-01 | Learner login | Log in as a test learner | Successful authenticated session | screenshot | high |  |
| ID-01 | Identity confirmation | Complete identity confirmation step at start | Identity step recorded before content | log/screenshot | high |  |
| PH-01 | No-PHI attestation | Open no-PHI acknowledgment | Learner must acknowledge no-PHI before activities | submission record | high |  |
| CS-01 | Course start | Open course; only first allowed section accessible | Locked sections show restriction text | screenshot | high |  |
| RA-01 | Content locked until prerequisite complete | Attempt to open U02/M02/next before completing prior | Access blocked with dependency message | screenshot | critical |  |
| QZ-01 | Quiz fail blocks completion | Submit failing quiz attempt | Activity not complete; next gated activity locked | grade + completion log | critical |  |
| QZ-02 | Quiz pass unlocks next content | Submit passing attempt | Activity complete; next content unlocks | grade + completion log | critical |  |
| QZ-03 | Retake history retained | Make 2+ attempts | All attempts (incl. failed) retained/exportable | quiz responses export | high |  |
| QZ-04 | No answer key shown | Review quiz after attempt | Full answer key not displayed to learner | screenshot | high |  |
| FA-01 | Final/capstone gate | Attempt final before all units/modules complete | Final locked until all complete | screenshot | critical |  |
| CT-01 | Certificate blocked before approval | Complete course pre-approval | No certificate available/issued | screenshot | critical |  |
| CT-02 | Certificate release after approval metadata only | Set approval metadata + flag (test) | Certificate available only after flag set | config + screenshot | critical |  |
| RP-01 | Completion report export | Export course completion report | CSV/Excel with per-learner completion | export file | high |  |
| RP-02 | Grade report export | Export grader report | CSV/Excel with grades | export file | high |  |
| RP-03 | Logs export | Export logs report | CSV/Excel audit trail | export file | medium |  |
| RV-01 | Reviewer access without edit rights | Log in as reviewer | Read-only; no edit/grade/enroll/cert controls | screenshot | critical |  |
| PH-02 | No PHI in activities | Review submissions/prompts | Only fictional/de-identified content present | review note | high |  |
| AP-01 | No approval claim present | Scan course text/certificates | No statement implying issued approval | scan note | critical |  |
| BR-LANG-01 | No stale BRN 4-hour language | Search BRN content for "4 contact hours"/"4-contact-hour" | None found (contact hours only) | search result | critical |  |
| ST-CNA-01 | CNA structure correct | Verify 12 units, 2 hrs each, Year1/Year2 | Matches 12x2=24 online CE | screenshot | high |  |
| ST-RCFE-01 | RCFE structure correct | Verify 9 courses / 27 hours | Matches filed LIC 9140 set | screenshot | high |  |
| ST-BRN-01 | BRN structure correct | Verify 10 modules x 3 + capstone | Matches 30 contact hours | screenshot | high |  |
| BR-01 | Backup/restore test | Backup a course; restore to test | Course restores intact | backup + restore log | high |  |
| AC-01 | Mobile/accessibility smoke test | Open on mobile + run accessibility check | Responsive; key a11y checks pass | screenshots/report | medium |  |
