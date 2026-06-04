# Moodle Admin Execution Runbook

Prototype Build 1 - Certificate Gate Proof of Concept

This runbook is a staging-only manual for configuring the Moodle proof of concept. It does not create production configuration, final course content, custom plugins, or approved clinical-hour credit.

## 1. Pre-build assumptions

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Governance | Confirm this build is Prototype Build 1 only. | Build Lead | Staging build note |  |
| 2 | Compliance | Confirm the course represents 12 hours of online theory CE as partial CNA renewal credit only. | Compliance Lead | Compliance note |  |
| 3 | Compliance | Confirm optional clinical support is support/documentation only unless CDPH gives written approval. | Compliance Lead | Optional support note |  |
| 4 | Compliance | Confirm optional clinical support will not gate the online CE certificate. | Compliance Lead | Gate review note |  |
| 5 | Privacy | Confirm no PHI, learner records, certificate PDFs, production audit packets, credentials, Moodle backups, or private approval documents are committed to the repository. | Repository Lead | Repo hygiene check |  |

## 2. Required Moodle access

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Site Administration | Confirm administrator or manager access to staging Moodle. | Moodle Admin | Access screenshot without credentials |  |
| 2 | Course Administration | Confirm permission to create categories, courses, activities, completion settings, restrictions, reports, and test users. | Moodle Admin | Role capability screenshot |  |
| 3 | Reports | Confirm access to completion, activity, quiz, certificate, and log/report exports. | QA Lead | Report access screenshot |  |

## 3. Required plugins or candidate tools

| Tool Area | Candidate | Prototype Use | Validation Status |
|---|---|---|---|
| Certificate | Moodle certificate/custom certificate activity if already available in staging | Staging-only certificate gate test | Must be validated before use |
| Active time | Existing time-on-task, attendance, checklist, H5P, quiz timing, lesson timing, or report-based tool available in staging | Active-time candidate evidence | Unvalidated until staging tests pass |
| Interaction | Forum, assignment, quiz question, lesson question, H5P interaction, or similar existing Moodle activity | Required interaction/feedback evidence | Must produce auditable attempt evidence |
| Manual fallback | Manual completion, admin review hold, or grade item | Fallback if active-time candidate is not reliable | Must be documented |

Do not implement custom plugin code for Prototype Build 1.

## 4. Staging-only warning

This build is for Moodle staging configuration only. Do not configure production. Do not issue production certificates. Do not collect PHI. Do not treat optional clinical support as required. Do not include clinical hours on the online CE certificate.

## 5. Course category creation

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Site Administration > Courses | Create a staging category for CNA Recertification Prototype Build 1. | Moodle Admin | Category screenshot |  |
| 2 | Category Settings | Label the category as staging/prototype only. | Moodle Admin | Category settings screenshot |  |

## 6. Theory course shell creation

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Courses | Create the 12-hour online theory CE course shell. | Moodle Admin | Course settings screenshot |  |
| 2 | Course Settings | Enable completion tracking. | Moodle Admin | Completion setting screenshot |  |
| 3 | Course Format | Use clear required-theory sections. | Moodle Admin | Course homepage screenshot |  |
| 4 | Course Description | State that the course is partial renewal credit only and does not satisfy the full 48-hour renewal requirement by itself. | Compliance Lead | Description screenshot |  |

## 7. Optional clinical support shell creation

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Courses or Section | Create optional clinical support shell or clearly separated section. | Moodle Admin | Shell/section screenshot |  |
| 2 | Naming | Label it optional support/documentation only. | Moodle Admin | Label screenshot |  |
| 3 | Restrictions | Do not make optional clinical support required for certificate release. | Moodle Admin | Restriction screenshot |  |

## 8. Admin-only compliance archive placeholder

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Course or Hidden Section | Create an admin-only placeholder for compliance notes and audit references. | Moodle Admin | Visibility screenshot |  |
| 2 | Permissions | Restrict access to authorized admin/compliance roles only. | Moodle Admin | Permission screenshot |  |

## 9. Required user profile fields

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Site Administration > Users > Accounts > User Profile Fields | Create or confirm Required Legal Name field. | Moodle Admin | Field settings screenshot/export |  |
| 2 | User Profile Fields | Create or confirm Required CNA Certificate Number field. | Moodle Admin | Field settings screenshot/export |  |
| 3 | Privacy | Confirm the fields do not request PHI. | Compliance Lead | No-PHI warning screenshot |  |

## 10. Completion tracking setup

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Course Completion | Enable course completion criteria for required theory-only gates. | Moodle Admin | Course completion screenshot |  |
| 2 | Activity Completion | Configure completion on each required activity. | Moodle Admin | Activity completion screenshots |  |
| 3 | Optional Activities | Confirm optional clinical support activities do not count toward course completion or certificate gate. | QA Lead | Optional completion screenshot |  |

## 11. Restrict Access setup

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Certificate Activity | Restrict access until all required gates are satisfied. | Moodle Admin | Restrict Access screenshot |  |
| 2 | Direct URL Test | Confirm learners cannot bypass restrictions by direct URL. | QA Lead | Access denied screenshot |  |
| 3 | Optional Activities | Confirm optional clinical support has no certificate restriction dependency. | QA Lead | Restriction screenshot |  |

## 12. Orientation acknowledgement setup

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Module 0 | Create an Orientation Page. | Moodle Admin | Activity screenshot |  |
| 2 | Acknowledgement | Create Online Cap Acknowledgement activity. | Moodle Admin | Completion settings screenshot |  |
| 3 | Text | State that California CNA renewal requires 48 hours over 2 years, at least 12 hours each year, and only 24 hours may be completed online through CDPH-approved online CE. | Compliance Lead | Acknowledgement screenshot |  |

## 13. Sample theory activity setup

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Required Theory Section | Create one sample theory activity placeholder. | Moodle Admin | Activity screenshot |  |
| 2 | Completion | Require view/submission/completion evidence according to available tool behavior. | Moodle Admin | Completion settings screenshot |  |
| 3 | Content Boundary | Do not generate final course content. | Build Lead | Placeholder screenshot |  |

## 14. Required interaction/check setup

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Required Theory Section | Create a required interaction/check activity. | Moodle Admin | Activity screenshot |  |
| 2 | Evidence | Configure it to produce an auditable attempt, response, grade, or completion record. | Moodle Admin | Attempt/grade screenshot |  |
| 3 | Gate | Include this activity in certificate release criteria. | Moodle Admin | Gate settings screenshot |  |

## 15. Active-time candidate setup or manual fallback

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Active-Time Candidate | Configure the selected active-time candidate tool available in staging. | Moodle Admin | Tool settings screenshot |  |
| 2 | Validation | Mark the tool unvalidated until staging tests pass. | QA Lead | Validation note |  |
| 3 | Manual Fallback | Configure Active-Time Status or Manual Review Hold if candidate reporting is insufficient. | Moodle Admin | Manual hold screenshot |  |
| 4 | Evidence Rule | Confirm Moodle logs alone are not treated as sufficient active-time evidence. | QA Lead | Evidence review note |  |

## 16. Final exam/test placeholder setup

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Required Assessment Section | Create Final Exam/Test Placeholder. | Moodle Admin | Quiz/settings screenshot |  |
| 2 | Grade | Configure passing status required for completion. | Moodle Admin | Grade settings screenshot |  |
| 3 | Gate | Include pass status in certificate release criteria. | Moodle Admin | Gate settings screenshot |  |

## 17. Affidavit placeholder setup

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Required Final Statement Section | Create Final Signed Statement/Affidavit placeholder. | Moodle Admin | Activity screenshot |  |
| 2 | Completion | Require signed acknowledgement/submission/completion evidence. | Moodle Admin | Completion settings screenshot |  |
| 3 | Gate | Include affidavit completion in certificate release criteria. | Moodle Admin | Gate settings screenshot |  |

## 18. Certificate activity setup as disabled or staging-only

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Certificate Section | Create Certificate Activity as disabled, hidden, or clearly staging-only until gate testing. | Moodle Admin | Certificate settings screenshot |  |
| 2 | Required Fields | Confirm required certificate fields include legal name and CNA certificate number. | Moodle Admin | Field mapping screenshot |  |
| 3 | Exclusions | Confirm the online CE certificate does not include clinical hours. | Compliance Lead | Certificate preview screenshot |  |
| 4 | Restrictions | Require identity, theory completion, active-time evidence, interaction/feedback, final exam/test pass, affidavit, required certificate fields, admin hold clear, and audit evidence. | Moodle Admin | Restrict Access screenshot |  |

## 19. Admin hold setup

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Gradebook or Completion | Create Admin Hold status, grade item, group, or manual completion gate. | Moodle Admin | Admin hold settings screenshot |  |
| 2 | Certificate Gate | Require Admin Hold clear before certificate access. | Moodle Admin | Gate screenshot |  |
| 3 | Test | Confirm learner with admin hold cannot access certificate. | QA Lead | Negative test screenshot |  |

## 20. Optional clinical support stub setup

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Optional Clinical Support | Create Optional Clinical Support Landing Page. | Moodle Admin | Landing page screenshot |  |
| 2 | Optional Check | Create Optional Confidence Check. | Moodle Admin | Activity screenshot |  |
| 3 | Optional Stub | Create Optional Documentation Support Stub. | Moodle Admin | Activity screenshot |  |
| 4 | Compliance | State that simulation, virtual simulation, and LTI simulation must not count toward clinical hours unless CDPH approves in writing. | Compliance Lead | Warning screenshot |  |
| 5 | Gate Review | Confirm all optional clinical activities have Certificate Gate = No. | QA Lead | Settings screenshots |  |

## 21. Audit export dry run setup

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Reports | Identify export paths for profile fields, completions, interaction attempts, active-time evidence/manual review notes, quiz scores, affidavit completion, certificate status, and admin hold. | QA Lead | Export menu screenshots |  |
| 2 | Dry Run | Export staging test records only. | QA Lead | Redacted export files stored outside repo |  |
| 3 | Repository Hygiene | Do not commit learner records, certificate PDFs, Moodle backups, or production audit packets. | Repository Lead | Git status screenshot if allowed |  |

## 22. QA test user creation

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Users | Create test learners listed in TEST_LEARNER_MATRIX.md. | Moodle Admin | Test user list screenshot without credentials |  |
| 2 | Enrollment | Enroll test learners in the theory course and optional support shell if needed for testing. | Moodle Admin | Enrollment screenshot |  |
| 3 | Privacy | Use synthetic data only. | QA Lead | Synthetic data note |  |

## 23. Negative test execution order

Run negative tests before the passing learner test.

| Order | Negative Test | Expected Result |
|---|---|---|
| 1 | Missing legal name | Certificate blocked |
| 2 | Missing CNA certificate number | Certificate blocked |
| 3 | Skipped online cap acknowledgement | Certificate blocked |
| 4 | Skipped theory activity | Certificate blocked |
| 5 | Skipped interaction | Certificate blocked |
| 6 | Insufficient active-time evidence | Certificate blocked or manual review hold remains active |
| 7 | Failed exam/test | Certificate blocked |
| 8 | Missing affidavit | Certificate blocked |
| 9 | Admin hold active | Certificate blocked |
| 10 | Direct certificate URL access | Access denied |
| 11 | Optional clinical skipped | Certificate remains eligible if all required theory gates pass |

## 24. Evidence capture instructions

| Step | Moodle Area | Exact Action | Owner | Evidence to Capture | Done |
|---|---|---|---|---|---|
| 1 | Screenshots | Capture screenshots listed in EVIDENCE_CAPTURE_CHECKLIST.md. | QA Lead | Screenshots stored outside repo |  |
| 2 | Exports | Capture staging-only exports listed in EVIDENCE_CAPTURE_CHECKLIST.md. | QA Lead | Redacted exports stored outside repo |  |
| 3 | Logs | Record implementation changes in STAGING_IMPLEMENTATION_LOG.md. | Moodle Admin | Completed log rows |  |
| 4 | Defects | Record failed tests in DEFECT_LOG.md. | QA Lead | Defect log rows |  |

## 25. Pass/fail decision

| Decision Area | Pass Standard | Fail Condition |
|---|---|---|
| Certificate gate | Certificate releases only when all required theory gates, identity fields, active-time evidence/manual review, interaction, exam pass, affidavit, admin hold clear, required certificate fields, and audit evidence are satisfied. | Any required gate can be bypassed. |
| Optional clinical separation | Optional clinical support does not gate the certificate and is visually and technically separated. | Optional clinical support is required for certificate release or appears to award clinical hours. |
| Active-time evidence | Candidate tool passes staging validation or manual fallback blocks release until review. | Moodle logs alone are treated as sufficient evidence. |
| Compliance boundaries | No PHI collection, no clinical hours on online CE certificate, no production configuration, no custom plugin code. | Any compliance boundary is violated. |

