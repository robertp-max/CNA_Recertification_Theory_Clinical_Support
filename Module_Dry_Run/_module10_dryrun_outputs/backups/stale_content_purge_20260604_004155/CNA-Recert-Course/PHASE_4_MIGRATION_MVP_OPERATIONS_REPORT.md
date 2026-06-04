# Phase 4: Migration, MVP Build, Operations, QA, and Launch Roadmap

**Project:** California CNA Recertification Course in Moodle  
**Prepared for:** CI Institute of Nursing  
**Scope:** Phase 4 only: migration, MVP build, operations, QA, launch readiness, and post-launch operations  
**Controlling compliance source:** `PHASE_0_COMPLIANCE_FOUNDATION.md`  
**Status:** Implementation planning report; not legal advice; not final reconciliation  
**Date:** May 25, 2026

---

## 1. Executive Summary

This report defines a practical Phase 4 plan to migrate approved CNA recertification content into Moodle, launch a no-new-video MVP, operate the course with audit-ready controls, and run QA through pilot and launch. Phase 0 is the controlling compliance source for California CNA renewal requirements and certificate controls.

The MVP should launch as a **12-hour Moodle theory course for partial California CNA renewal credit only**, subject to CDPH provider/course approval and the learner's 24-hour online CE cap. The Moodle certificate workflow must include identity confirmation, interaction/feedback, active-time controls, an exam/test, a final signed statement/affidavit, required certificate fields, and retention/export evidence. [S0] [S1] [S2]

The proposed clinical Moodle component should be operated as **optional learner support**, skills refresh, scheduling/resource support, and documentation support. It must not be treated as required California renewal clinical hours, a substitute for compensated supervised work, or a certificate gate unless CDPH gives written approval for the exact use case. Simulation, virtual simulation, or LTI simulation must not count toward clinical hours without written CDPH approval. [S0]

The fastest safe launch path is to clone approved content, convert it into Moodle-native Books, Pages, Lessons, quizzes, downloadable job aids, approved text-based interactions, and optional approved TTS audio with transcripts. New video production, advanced simulation, custom dashboards, SMS automation, and custom audit generators belong in a later elite version, not the MVP.

---

## 2. Compliance Guardrails for Phase 4

| Guardrail | Operational Meaning | Phase 4 Control |
|---|---|---|
| California CNA renewal is 48 hours over two years, with at least 12 hours each year. | A 12-hour Moodle course is partial credit only. | Learner-facing copy, certificate disclaimers, and support scripts must avoid "complete renewal" language. |
| Only 24 of the 48 hours may be online through CDPH-approved online CE. | Learners may have already used online hours elsewhere. | Add learner attestation and certificate language noting the online cap. |
| Online CE requires identity confirmation, interaction/feedback, exam/test, active-time/pause control, signed statement, and certificate fields. | Certificate release cannot rely on attendance or self-attestation alone. | Configure sequenced completion, final exam, affidavit, identity fields, and audit exports. |
| Clinical renewal requirement not verified in Phase 0. | Optional clinical support cannot become state-required clinical credit. | Keep clinical support non-gating unless legal/CDPH approval says otherwise. |
| Simulation is not approved as clinical-hour replacement in Phase 0. | Simulation can support learning only. | Label as practice/support; do not include as clinical hours on certificates. |
| CDPH/legal decisions are outside Phase 4 authority. | Unverified claims must be flagged. | Maintain a decision log and block certificate launch until required approvals are documented. |

---

## 3. Implementation Philosophy

The Phase 4 operating model should optimize for fast MVP launch, low learner friction, low admin burden, audit-ready evidence, and conservative compliance claims. The course should feel simple to an exhausted working CNA on a phone: clear next step, short content chunks, obvious completion status, minimal uploads, and support contact points.

Operationally, the Moodle build should prefer native, maintainable tools before custom code. Moodle course backups, site backups, cron, roles/capabilities, activity completion, logs, and reports should be configured and tested because the evidence trail is part of the product, not an afterthought. Moodle documentation emphasizes regular site backups, course backups for reusable course copies, cron for scheduled tasks, role-based access control, security checks, and activity completion behavior. [S15] [S16] [S17] [S18] [S19] [S20]

The MVP should be production-light and compliance-heavy: approved text, Moodle-native delivery, TTS only when authorized, transcripts, quizzes, completion rules, certificate controls, audit exports, support procedures, and rollback plans.

---

## 4. Legacy Content Audit Framework

All legacy assets should be inventoried before migration. The audit should separate content quality from compliance authority: an asset can be useful but not approved, approved but outdated, or operationally valuable but not appropriate for learner release.

| Existing Asset | Keep / Revise / Retire | Conversion Method | Moodle Destination | Compliance Risk | Engagement Upgrade | MVP or Elite |
|---|---|---|---|---|---|---|
| Approved course text | Keep if approval and version are current | Clean text, chunk into lessons/pages | Book, Page, Lesson | High if approval status unknown | Plain-language headings, short knowledge checks | MVP |
| PDFs | Revise unless accessible and mobile-friendly | Extract text, remediate tables/images, create downloadable PDF backup | Book/Page plus File | Medium if PDF is inaccessible or outdated | Mobile-native content, transcript-like summaries | MVP |
| PowerPoints | Revise | Convert slides to structured text and images with alt text | Book/Lesson/Page | Medium if speaker notes contain unapproved content | Scenario prompts, recall checks | MVP |
| Existing videos | Keep only if approved/current | Embed with captions/transcripts if already production-ready | Page/Book embed | Medium/high if outdated, inaccessible, or unapproved | Captions, transcript, short reflection | MVP only if already approved |
| New videos | Retire from MVP dependency | Defer production | Not MVP | High schedule risk | Rich demo library | Elite |
| Paper checklists | Revise | Convert to Moodle checklist/forms and downloadable job aids | Checklist, Assignment, Page | Medium if treated as required clinical credit | One-page mobile checklist | MVP |
| Existing quizzes | Revise | Build question bank, tag by objective/version | Quiz | High if not tied to approved objectives | Feedback per answer | MVP |
| Sign-in sheets | Keep as operational archive | Convert to upload template or reference only | File/Assignment | Medium if used as CE proof without approval | Simple evidence instructions | MVP |
| Instructor-led materials | Revise | Convert to readings, prompts, job aids | Book/Lesson | Medium if classroom assumptions do not fit online CE | Short cases, self-checks | MVP |
| Compliance documentation | Keep | Store in restricted admin archive | Folder/repository outside learner course | High if outdated | Version-controlled approval archive | MVP |
| Old LMS exports | Revise | Import only after validation | Backup/import staging course | Medium/high if completion logic does not map | Clean course shell rebuild | MVP |
| Paper certificates | Revise | Map fields to locked certificate template | Custom certificate or certificate tool | High if fields missing | QR/token verification if approved | MVP |
| Clinical logs | Revise | Convert to de-identified support templates | Assignment/Form/Database | High if PHI or clinical credit claim | Minimal upload workflow | MVP |
| Existing policies | Keep/revise | Version and approve | Admin resource folder; learner handbook where relevant | Medium if inconsistent with Phase 0 | Short learner-facing summary | MVP |
| State approval documents | Keep | Lock in compliance archive | Restricted file area | High if missing | Approval crosswalk | MVP |
| Course maps | Revise | Map to approved title/objective/hour | Admin workbook and Moodle labels | High if not traceable | Version map | MVP |
| Skills checklists | Revise | Use as optional support unless approved | Clinical support hub | High if used as certificate gate | Confidence check language | MVP |
| Audio/narration | Keep only if approved and consented | Compress, transcript, accessibility review | Page/Book audio block | High for voice authorization and transcript gaps | Short audio support | MVP if authorized |

---

## 5. Migration Strategy Into Moodle-Native Formats

Migration should run through a controlled staging course before any production certificate is enabled.

1. Build a locked source inventory with asset owner, approval status, source file, version, and proposed Moodle destination.
2. Confirm every theory asset maps to a CDPH-approved course title, objective, outline, and hour value before learner release. This is a compliance dependency, not a Phase 4 redesign task.
3. Convert approved content into Moodle-native Books, Pages, Lessons, Quiz, Question bank, File, Assignment, and H5P/text interactions where useful.
4. Preserve original approved source files in a restricted evidence archive.
5. Assign content version IDs to every migrated module, quiz, certificate template, affidavit, and learner-facing disclaimer.
6. Test activity completion, availability restrictions, quiz gating, and certificate gating in a staging course using learner, instructor, admin reviewer, and support roles.
7. Freeze the MVP course version before pilot; log any post-freeze changes as release notes.

| Migration Item | Preferred MVP Format | Rationale | Required QA |
|---|---|---|---|
| Long readings | Moodle Book | Better mobile navigation and progress chunking than PDFs | Heading order, links, alt text, completion |
| Short policy notices | Page | Fast maintenance and clear revision history | Mobile view and readability |
| Guided sequence | Lesson | Supports branching and required progression without custom code | Completion, feedback, skip prevention |
| Knowledge checks | Quiz or H5P text interaction | Supports feedback and evidence | Attempts, feedback, gradebook behavior |
| Final exam/test | Moodle Quiz | Strong audit trail and configurable passing rules | Randomization, pass threshold, retake rules |
| Affidavit | Quiz essay/assignment/form or policy acknowledgement workflow | Timestamped final statement before certificate | Signed/e-signed acceptance and export |
| Certificate | Certificate tool/custom certificate | Locked fields and issue record | Field accuracy, release conditions |
| Clinical support guide | Book/Page | Keeps optional support clear and accessible | Non-gating behavior and disclaimers |
| Clinical uploads | Assignment/Form | Simple evidence collection and resubmission | PHI warning, rejection/resubmission, role access |
| Admin evidence archive | Restricted Folder/repository | Audit readiness | Permission and export testing |

---

## 6. MVP No-New-Video / Approved TTS Workflow

MVP launch should not depend on video production. Use approved source text, short Moodle-native learning blocks, approved cloned-voice TTS only when authorization is documented, and transcripts for every audio item. Do not generate cloned-voice audio from unapproved text, do not impersonate a real person without authorization, and do not make audio required when text provides the instructional content.

| Production Step | Owner | Input | Output | QA Check | Risk |
|---|---|---|---|---|---|
| Content extraction | Content converter | Approved source PDFs/PPTs/docs | Clean text draft | Source/version match | Pulling unapproved text |
| Compliance review | Compliance reviewer | Clean text draft | Approved MVP content set | Maps to approved course/hour | Compliance drift |
| Plain-language pass | Instructional designer | Approved text | Shorter learner-facing text | Meaning unchanged | Accidental content change |
| Moodle chunking | Moodle builder | Approved text | Books/Pages/Lessons | Mobile readability | Overlong pages |
| Interaction build | Moodle builder | Objectives and approved content | H5P/text prompts/knowledge checks | Tracks as expected | Token interaction |
| Question bank build | QA + educator | Existing approved quiz items | Tagged questions | Correct answers/feedback | Unmapped exam items |
| TTS script approval | Compliance + program owner | Approved text excerpt | Approved TTS script | Exact text/version | Unauthorized alteration |
| Voice authorization check | Program owner | TTS voice record/consent | Authorization log | Consent present | Cloned voice risk |
| TTS generation | Audio producer | Approved script | Short audio files | Audio matches transcript | Mispronunciation/quality |
| Transcript pairing | Content converter | TTS output | Transcript block | Transcript complete | Accessibility failure |
| Moodle embed | Moodle builder | Audio + transcript | Page/Book audio block | Mobile playback | Large file/low bandwidth |
| Accessibility QA | QA tester | Course pages/audio/files | Accessibility findings log | WCAG-oriented checks | Poor access for disabled learners |
| Completion logic QA | Moodle admin | Built modules | Completion report | Gates work correctly | Premature certificate |

---

## 7. Moodle Build Workstreams

This section identifies operational build streams without prescribing Phase 2 architecture choices.

| Workstream | Key Tasks | Owner | Dependencies | Deliverables | Risk |
|---|---|---|---|---|---|
| Moodle environment setup | Confirm hosting, cron, backups, email, SSL, staging/prod split | Moodle admin | Phase 2 architecture decisions | Staging and production environments | Misconfigured cron/backups |
| Theme/mobile UX setup | Configure mobile-friendly theme, navigation, course format | Moodle admin + UX tester | Branding assets and theme decision | Mobile-tested learner shell | Poor smartphone experience |
| Course shell build | Create course, sections, labels, naming, version fields | Moodle builder | Approved module map | Frozen MVP course shell | Scope creep |
| Theory content conversion | Convert approved source to Books/Pages/Lessons | Content converter | Approved content inventory | Native Moodle content | Unapproved content migration |
| TTS/audio implementation | Generate authorized short audio and transcripts | Audio producer | Voice consent and approved scripts | Audio/transcript blocks | Authorization gap |
| H5P/text interaction build | Add text-based interactions where approved | Moodle builder | Approved objectives | Interaction set | Tracking mismatch |
| Question bank build | Import/tag final and module questions | QA + RN educator | Approved exam blueprint | Versioned question bank | Incorrect answer keys |
| Assessment configuration | Configure final exam/test, attempts, passing score, retake policy | Moodle admin | Compliance-approved exam rules | Tested final exam | Premature pass |
| Clinical support hub | Build optional resources, scheduling guidance, confidence checks | Clinical coordinator | Legal/CDPH boundaries | Non-gated support hub | Clinical credit confusion |
| Clinical documentation workflow | Configure upload, signoff, rejection, resubmission | Admin reviewer + Moodle admin | Legal/privacy review | Evidence workflow | PHI uploads |
| Scheduling setup | Add scheduling instructions or scheduler tool if selected | Operations | Staffing/site availability | Learner scheduling guide | Overpromising slots |
| Certificate configuration | Configure locked fields, release gates, certificate ID | Registrar + Moodle admin | CDPH certificate wording | Certificate template | Missing required fields |
| Reporting setup | Configure logs, completion, grade, certificate, override exports | Moodle admin | Report requirements | Audit export checklist | Incomplete packet |
| Role/permission setup | Assign learner, instructor, RN/preceptor, admin reviewer, support roles | Moodle admin | Phase 2 role model | Least-privilege role matrix | Excess data access |
| Support setup | Create help channels, templates, escalation paths | Support lead | Staffing plan | Support playbook | Unstaffed launch |
| QA/UAT | Execute test scripts across roles/devices | QA manager | Frozen build | Defect log and signoff | Undetected gate failure |
| Pilot launch | Enroll small cohort and monitor | Program owner | QA pass | Pilot report | Learner confusion |
| Post-launch improvement | Triage issues, update content log, plan v2 | Program owner | Pilot/live data | Improvement backlog | Uncontrolled changes |

---

## 8. Operational Model

### Enrollment and Learner Profile

Enrollment should be structured enough to support certificate fields but light enough to avoid learner drop-off.

| Step | Operational Control | Owner | Evidence |
|---|---|---|---|
| Account creation | Legal name, email, CNA certificate number, state, cohort/course | Registrar/support | User profile and enrollment record |
| Identity confirmation | Learner confirms identity before coursework and again before certificate | Registrar + Moodle admin | Timestamped identity attestation |
| Online cap acknowledgement | Learner acknowledges California 24-hour online CE cap | Registrar | Attestation export |
| Course scope acknowledgement | Learner acknowledges 12-hour theory is partial credit only | Registrar | Attestation export |
| Clinical support acknowledgement | Learner acknowledges optional clinical support is not state-required credit unless approved | Clinical coordinator | Attestation export |
| Support orientation | Learner receives clear next steps and support contact | Support lead | Welcome message log |

### Identity Verification

MVP identity confirmation should include unique login credentials, locked learner profile fields, pre-certificate identity attestation, and support review for profile changes. Any stronger model, such as document review or third-party identity verification, requires legal/privacy review because it increases sensitive data collection.

### Certificate Release

Certificate release should be automated only after all required online CE gates pass:

| Gate | Required for MVP Certificate? | Evidence |
|---|---|---|
| Approved course enrollment | Yes | Enrollment record |
| Required theory activities completed | Yes | Activity completion report |
| Required active-time threshold met | Yes | Time tracking/reporting evidence |
| Required interactions/feedback completed | Yes | Activity/H5P/quiz logs |
| Final exam/test passed | Yes | Quiz attempt and grade |
| Identity fields complete | Yes | User profile/identity attestation |
| Final signed statement/affidavit complete | Yes | Timestamped signed statement |
| Certificate fields populated | Yes | Certificate issue record |
| Optional clinical support completed | No, unless CDPH/legal approval requires it | Separate support record |

### Manual Overrides

Manual overrides must be exceptional. Only the Program Owner or Compliance Lead should authorize certificate-related overrides, and the Moodle admin/registrar should record the reason, approving person, date/time, affected learner, gate bypassed, evidence reviewed, and corrective action. A monthly override audit should be part of post-launch operations.

### Audit Packet Export

Each learner should have an exportable packet that can be reproduced from Moodle records and the restricted approval archive. Moodle course backups can include user completion, course logs, grade history, and user data when permitted; site backup should be treated as the main disaster recovery backup, while course backup supports reusable course copies and evidence preservation. [S15] [S16]

| Audit Item | Moodle Source | Export Method | Owner | Required or Recommended |
|---|---|---|---|---|
| Enrollment record | Participants/enrollment report | CSV/PDF export | Registrar | Required |
| Learner profile fields | User profile/custom fields | CSV export | Registrar | Required |
| Identity attestation | Quiz/form/policy acknowledgement | CSV/PDF export | Registrar | Required |
| Online cap acknowledgement | Quiz/form/policy acknowledgement | CSV/PDF export | Registrar | Recommended/required by policy |
| Theory completion report | Activity/course completion | CSV export | Moodle admin | Required |
| Active-time report | Time tracking/log report if used | CSV/PDF export | Moodle admin | Required for time control evidence |
| Interaction completion | Activity/H5P/lesson logs | CSV/screenshots/PDF | Moodle admin | Required |
| Final exam/test | Quiz report and gradebook | CSV/PDF export | QA/Registrar | Required |
| Affidavit/signed statement | Final acknowledgement activity | PDF/CSV export | Registrar | Required |
| Certificate issue record | Certificate report/log | CSV/PDF certificate | Registrar | Required |
| Course version | Course settings/version log | PDF/change log | Moodle admin | Required |
| Content version | Content inventory | PDF/change log | Content owner | Required |
| State disclaimer | Certificate and course copy | PDF snapshot | Compliance reviewer | Required |
| Manual override log | Override form/log | CSV/PDF export | Compliance reviewer | Required if applicable |
| Optional clinical documentation | Assignment/form records | PDF/CSV export | Clinical coordinator | Recommended; not certificate gate unless approved |
| Admin review notes | Assignment feedback/review checklist | PDF/CSV export | Admin reviewer | Recommended |
| Exceptions | Decision/exception log | PDF export | Compliance lead | Required if applicable |

### Privacy Incident Handling

Moodle clinical support areas should be designed to prevent PHI collection. HHS de-identification guidance describes Safe Harbor and Expert Determination methods; HHS cloud guidance warns that cloud service providers handling ePHI may implicate HIPAA business associate obligations. [S12] [S13] Phase 4 operations should therefore collect minimum necessary learner data and prohibit patient/resident identifiers.

Privacy incident workflow:

1. Learner or staff flags possible PHI in an upload or message.
2. Support escalates to Privacy Officer within one business day.
3. Privacy Officer quarantines access to the submission and determines whether deletion, redaction, legal review, or breach analysis is required.
4. Admin reviewer records the incident in a restricted privacy log.
5. Learner receives resubmission instructions using a de-identified template.
6. Monthly privacy trend review updates instructions and upload warnings.

### Backup, Retention, and Recovery

Moodle site backups should cover database, moodledata/uploaded files, configuration, code customizations, plugins, and theme changes. Course backups should support reusable course snapshots and course-level evidence but should not be the only disaster recovery method. Moodle documentation recommends regular site backups and notes course backups can include completion, logs, grade history, and user data when selected. [S15] [S16]

Retention should follow the stricter Phase 0 position: retain completion evidence, certificate records, affidavits, exam/test evidence, logs supporting certificate release, and relevant provider records at least four years unless legal/compliance sets a longer period. [S0]

Operational backup controls:

| Control | MVP Requirement |
|---|---|
| Backup schedule | Daily database/files where feasible; weekly full site backup; course backup at major release milestones |
| Backup testing | Restore test before launch and quarterly after launch |
| Backup access | Restricted to site admin/IT; no broad teacher download of user-data backups |
| Backup logs | Review failed backup logs after each scheduled run |
| Course version archive | Backup frozen MVP, pilot version, and each launched revision |
| Retention archive | Export learner audit packets according to retention schedule |
| Recovery objective | Define acceptable restore point and restore time before launch |

### Staff Roles

| Role | Responsibilities | Needed for MVP? | Needed for Elite? |
|---|---|---|---|
| Program owner | Scope, launch authority, staffing, go/no-go | Yes | Yes |
| Compliance reviewer | Phase 0 alignment, CDPH/legal flags, certificate wording | Yes | Yes |
| RN clinical educator | Clinical support accuracy and signoff logic | Yes | Yes |
| Moodle admin | Site/course setup, roles, reports, backups, cron | Yes | Yes |
| Instructional designer | Moodle-native conversion, learner flow, accessibility basics | Yes | Yes |
| Content converter | Extract, clean, format approved content | Yes | Yes |
| TTS/audio producer | Generate authorized TTS and transcripts | Conditional | Yes |
| QA tester | Test gates, mobile UX, reports, negative cases | Yes | Yes |
| Support lead | Learner help, triage, communication templates | Yes | Yes |
| Preceptor/RN evaluator | Optional clinical support review/signoff if used | Conditional | Yes |
| Admin reviewer | Evidence review, rejected uploads, exceptions | Yes | Yes |
| Registrar | Enrollment, certificate fields, certificate release | Yes | Yes |
| Data/privacy owner | PHI prevention, privacy incident handling, retention | Yes | Yes |
| IT/security owner | Hosting, SSL, backups, security checks | Yes | Yes |

---

## 9. Clinical Operations Workflow

The clinical support hub should be helpful, optional, and clearly separated from online CE certificate gates unless written CDPH approval changes that rule. The workflow should minimize learner steps and avoid turning support into busywork.

| Step | Learner Action | RN/Preceptor Action | Admin Action | Moodle Tool | Evidence Created | Friction Risk |
|---|---|---|---|---|---|---|
| Clinical support orientation | Read optional support overview and disclaimer | None | Confirm wording approved | Page/Book | View/completion optional | Low |
| Schedule guidance | Review available pathways and contact instructions | Provide site availability if applicable | Update dates/contacts | Page/Scheduler if selected | Guidance page/version | Medium if stale |
| Optional sign-up | Choose slot or follow workplace guidance | Confirm slot if applicable | Monitor capacity | Scheduler/choice/form | Sign-up record | Medium |
| Preparation resources | Review skills refresh/job aids | None | Keep resources current | Book/File | Optional completion | Low |
| Optional confidence check | Complete self-check or reflection | None unless requested | Monitor only if support needed | Quiz/H5P/form | Learner support record | Medium if perceived as graded |
| Practice attendance | Attend lab/workplace/preceptor activity if arranged | Observe/support as locally approved | None unless exception | Offline activity + instructions | Attendance/signoff if used | Medium |
| Signoff | Upload or submit non-PHI documentation | Verify name/title/date/contact if applicable | Review completeness | Assignment/form | Signoff record | High if too complex |
| Evidence review | Respond to missing-info notice | Clarify if requested | Accept/reject with reason | Assignment feedback | Review notes | Medium |
| Rejection/resubmission | Upload corrected non-PHI evidence | Re-sign if needed | Re-review | Assignment resubmission | Resubmission log | Medium |
| Clinical support completion | View support status | None | Mark support complete if applicable | Completion/admin mark | Support completion | Low |
| Certificate release | No clinical action required for online CE certificate unless approved | None | Ensure clinical support is not a gate unless required | Certificate restrictions | Certificate release independent of optional clinical support | High if misconfigured |

Required clinical support disclaimer:

> The clinical support hub provides optional skills refresh, scheduling/resource support, and documentation support. It does not represent required California CNA renewal clinical hours and does not count as clinical-hour credit unless CI Institute of Nursing receives written CDPH approval for that exact use.

---

## 10. QA and Testing Protocol

QA must prove both learner usability and compliance gate integrity. Testing should run in staging first, then in a pilot cohort before full launch.

### Compliance and Certificate Tests

| Test | Role | Expected Result | Pass/Fail | Fix Needed |
|---|---|---|---|---|
| Learner attempts to skip required module | Learner | Next activity/exam remains locked | TBD | TBD |
| Learner completes fewer than 12 theory hours | Learner | Certificate unavailable | TBD | TBD |
| Learner completes content but not active-time threshold | Learner | Exam/certificate remains locked per configured rules | TBD | TBD |
| Learner tries final exam before interactions | Learner | Final exam unavailable | TBD | TBD |
| Learner fails final exam | Learner | Certificate unavailable; retake policy shown | TBD | TBD |
| Learner passes exam but skips affidavit | Learner | Certificate unavailable | TBD | TBD |
| Learner lacks CNA certificate number | Learner | Certificate unavailable or profile correction required | TBD | TBD |
| Learner completes all gates | Learner | Certificate issues with required fields | TBD | TBD |
| Certificate shows provider name/address/contact/NAC# | Registrar | Fields match approved template | TBD | TBD |
| Certificate shows learner name/CNA number/course/date/hours | Registrar | Fields accurate and complete | TBD | TBD |
| Certificate includes online-course and retention language if approved | Registrar | Language matches compliance-approved wording | TBD | TBD |
| Manual certificate override | Admin reviewer | Requires approval and logs reason | TBD | TBD |
| Audit packet export | Admin reviewer | Packet can be produced from records | TBD | TBD |
| Course version captured | Moodle admin | Version appears in audit packet | TBD | TBD |

### Optional Clinical Support Tests

| Test | Role | Expected Result | Pass/Fail | Fix Needed |
|---|---|---|---|---|
| Learner ignores optional clinical support | Learner | Theory certificate can still release if required online CE gates pass | TBD | TBD |
| Learner completes optional confidence check | Learner | Record appears as support evidence only | TBD | TBD |
| Learner uploads clinical evidence with PHI warning visible | Learner | Warning appears before upload | TBD | TBD |
| Admin rejects incomplete evidence | Admin reviewer | Learner sees reason and resubmission path | TBD | TBD |
| Learner resubmits evidence | Learner | Admin can review new version | TBD | TBD |
| RN/preceptor signoff submitted | RN/preceptor | Name/title/date/contact captured if workflow used | TBD | TBD |
| Optional clinical completion accidentally added as certificate condition | QA tester | Test fails; condition removed unless approved | TBD | TBD |

### User Experience and Accessibility Tests

W3C WCAG organizes accessibility under perceivable, operable, understandable, and robust principles, with testable success criteria; W3C encourages use of the latest WCAG version. Section508.gov describes federal ICT accessibility obligations and notes harmonization with WCAG. [S10] [S11]

| Test | Role | Expected Result | Pass/Fail | Fix Needed |
|---|---|---|---|---|
| Smartphone navigation | Learner | Learner can find next required activity within two taps/clicks | TBD | TBD |
| Low-bandwidth access | Learner | Text loads before optional media; no video dependency | TBD | TBD |
| TTS playback | Learner | Audio plays on mobile and is optional | TBD | TBD |
| Transcript availability | Learner | Transcript appears next to each audio file | TBD | TBD |
| Keyboard navigation | Learner | Core path can be completed without mouse | TBD | TBD |
| Screen reader smoke test | Learner | Headings, links, quiz controls readable | TBD | TBD |
| Color contrast check | QA tester | Buttons/labels readable | TBD | TBD |
| File accessibility | QA tester | PDFs/job aids have meaningful text and alt text where applicable | TBD | TBD |
| Upload from phone | Learner | Learner can upload photo/PDF without PHI prompt confusion | TBD | TBD |
| Learner fatigue review | Learner pilot | Instructions are short and next step is clear | TBD | TBD |

### Security, Privacy, and Operations Tests

| Test | Role | Expected Result | Pass/Fail | Fix Needed |
|---|---|---|---|---|
| Role access | Moodle admin | Learner cannot view other learner data | TBD | TBD |
| RN/preceptor role | RN/preceptor | Access limited to assigned evidence/workflow | TBD | TBD |
| Support role | Support user | Can help learners without certificate override access | TBD | TBD |
| Backup job | IT/security | Backup completes and log is reviewed | TBD | TBD |
| Restore test | IT/security | Staging restore works | TBD | TBD |
| Cron status | Moodle admin | Scheduled tasks run without errors | TBD | TBD |
| Security checks | IT/security | Moodle security checks reviewed and remediated | TBD | TBD |
| PHI negative case | QA tester | Submission is quarantined/rejected per privacy workflow | TBD | TBD |
| Email notifications | Learner/support | Messages deliver and do not disclose sensitive data | TBD | TBD |

---

## 11. Operational Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|
| State requirements misunderstood | Medium | High | Use Phase 0 as controlling source; obtain CDPH/legal review | Compliance lead | Open |
| Course not approved before use | Medium | High | Disable certificate release until approval/NAC# verified | Program owner | Open |
| Clinical hours not accepted | High | High | Keep clinical support optional and non-credit unless approved | Compliance lead | Open |
| Simulation not accepted | High | High | Do not count simulation/LTI toward clinical hours without written approval | Program owner | Open |
| Seat time over-relied upon | Medium | High | Combine active time, interaction, exam, affidavit, identity, logs | Moodle admin | Open |
| Learners bypass content | Medium | High | Use availability restrictions and completion gates | Moodle admin | Open |
| Certificate issued prematurely | Medium | High | Negative testing and restricted overrides | Registrar | Open |
| Plugin becomes unsupported | Medium | Medium | Prefer native Moodle; document plugin owner/version | Moodle admin | Open |
| H5P interactions not tracked properly | Medium | Medium | Test reporting before launch | QA manager | Open |
| TTS audio not approved | Medium | High | Require script approval and content version control | Program owner | Open |
| Cloned voice authorization unclear | Medium | High | Require written voice authorization before generation | Program owner | Open |
| Transcript missing | Medium | Medium | Transcript required in audio QA checklist | Content converter | Open |
| Mobile app/browser incompatibility | Medium | Medium | Test mobile browser and app if supported | QA manager | Open |
| Poor accessibility | Medium | High | WCAG-oriented QA and remediation backlog | Instructional designer | Open |
| Inadequate identity verification | Medium | High | Profile locks, attestations, support review | Registrar | Open |
| Incomplete RN/preceptor documentation | Medium | Medium | Simplified signoff fields and rejection/resubmission | Clinical coordinator | Open |
| Data privacy gaps | Medium | High | Least privilege, PHI prevention, privacy incident workflow | Privacy owner | Open |
| Uploads contain PHI | Medium | High | Warnings, de-identified templates, quarantine process | Privacy owner | Open |
| Moodle logs not retained long enough | Medium | High | Four-year minimum retention and export schedule | Operations | Open |
| Legacy content outdated | Medium | High | Content audit and approval/version map | Content owner | Open |
| Admin workflow too burdensome | Medium | Medium | Minimize manual reviews; batch reports | Support lead | Open |
| Clinical LMS support becomes busywork | Medium | Medium | Keep optional workflow short and helpful | Clinical coordinator | Open |
| Learners feel surveilled instead of supported | Medium | Medium | Explain time controls as compliance requirements | Support lead | Open |
| Optional assessments configured as required | Medium | High | QA negative test; certificate condition review | QA manager | Open |
| Reporting incomplete | Medium | High | Audit packet dry run before pilot | Moodle admin | Open |
| Manual overrides not tracked | Medium | High | Locked override form and monthly audit | Registrar | Open |
| Course version not documented | Medium | Medium | Version field and release notes | Moodle admin | Open |
| Broken certificate condition | Medium | High | Regression testing after any course edit | QA manager | Open |
| Support queue not staffed | Medium | Medium | Launch staffing schedule and triage templates | Support lead | Open |
| Learners confused by clinical documentation | Medium | Medium | Clear optional/non-credit disclaimer and examples | Clinical coordinator | Open |
| Backup restore fails | Low/medium | High | Restore test before launch and quarterly | IT/security | Open |
| Cron failure delays completion/reporting | Medium | Medium | Cron monitoring and scheduled task checks | Moodle admin | Open |
| Marketing overstates renewal value | Medium | High | Compliance review of all public copy | Compliance lead | Open |
| QR/certificate verification leaks private data | Low/medium | Medium | Minimal tokenized verification only | IT/security | Open |

---

## 12. MVP vs. Elite Build

| Area | MVP Version | Elite Version | Upgrade Trigger |
|---|---|---|---|
| Content | Cloned approved text in Moodle-native pages/books/lessons | Richer multimedia and refreshed examples | Stable approval and learner feedback |
| Video | No new video dependency | Custom videos with captions/transcripts | Budget, time, and approved scripts |
| Audio/TTS | Approved short TTS only where authorized; transcript paired | Larger audio library and multilingual supports if approved | Verified learner demand |
| Interactions | Text-based H5P/knowledge checks | Advanced branching scenarios | Evidence that interaction improves outcomes |
| Simulation | Not clinical credit; optional only if included | LTI/virtual simulation only if CDPH-approved for intended use | Written state approval |
| Assessment | Core quizzes and final exam/test | Adaptive practice, item analytics | Item performance data |
| Completion | Native completion and availability restrictions | Custom dashboard | High support volume or complex cohorts |
| Clinical support | Optional resource hub, simple uploads, signoff support | Custom preceptor workflow, reminders, analytics | Confirmed operational need |
| Scheduling | Basic guidance or simple scheduler | Integrated scheduling/reminders | Multiple sites/cohorts |
| Certificate | Locked template with required fields and issue record | QR/token verification portal | Audit/verification demand |
| Reports | Manual audit packet exports | Automated audit packet generator | Staff time burden |
| Accessibility | Essential WCAG-oriented QA | Formal third-party accessibility review | Scale or institutional requirement |
| Support | Email/helpdesk templates | SMS reminders/chatbot/knowledge base | Support volume thresholds |

---

## 13. Phased Implementation Roadmap

| Phase | Key Tasks | Owner | Dependencies | Deliverables | Risks |
|---|---|---|---|---|---|
| 1. Discovery and compliance verification | Confirm provider/course approval, certificate language, online cap copy, clinical boundary | Compliance lead | Phase 0 and CDPH/legal review | Compliance decision log | Approval gaps |
| 2. Existing content audit | Inventory assets and approval status | Content owner | Source files and state approval docs | Asset audit workbook | Missing source/version |
| 3. Moodle environment setup | Configure staging/prod, cron, SSL, backups, email | Moodle admin | Phase 2 architecture choices | Working environments | Misconfiguration |
| 4. Theme/mobile UX configuration | Configure theme/navigation/branding | Moodle admin | Branding assets and theme decision | Mobile learner shell | Poor mobile UX |
| 5. Course shell build | Build module structure and placeholders | Moodle builder | Approved module map | Course shell v0.1 | Scope creep |
| 6. Theory content conversion | Convert approved text to native Moodle | Content converter | Approved content set | Theory modules | Compliance drift |
| 7. TTS/audio conversion | Generate authorized audio and transcripts | Audio producer | Voice authorization | Audio/transcript set | Consent gaps |
| 8. Clinical support hub build | Build optional resource hub and disclaimers | Clinical coordinator | CDPH/legal boundary | Clinical support hub | Credit confusion |
| 9. Clinical documentation workflow | Build upload/review/resubmission flow | Admin reviewer | Privacy review | Evidence workflow | PHI risk |
| 10. Scheduling setup | Add scheduling guidance/tool | Operations | Site/staff availability | Scheduling instructions | Capacity gaps |
| 11. Assessment and question bank | Build quizzes/final exam/test | QA + educator | Approved exam blueprint | Tagged question bank | Invalid items |
| 12. Reporting and certificate | Configure reports, audit packet, certificate gates | Registrar + Moodle admin | Certificate wording | Tested certificate | Premature release |
| 13. Role/permission setup | Configure least-privilege roles | Moodle admin | Operational role model | Role matrix | Over-access |
| 14. QA and UAT | Execute test protocol | QA manager | Frozen staging build | Defect log/signoff | Late blockers |
| 15. Pilot testing | Run small cohort | Program owner | QA pass | Pilot report | Learner confusion |
| 16. Compliance review | Review pilot evidence and certificate packet | Compliance lead | Pilot data | Go/no-go recommendation | Audit gaps |
| 17. Launch | Open production enrollment | Program owner | Go decision | Live course | Support overload |
| 18. Post-launch improvement | Monitor support, defects, completion, audits | Program owner | Live data | Backlog and release plan | Uncontrolled changes |

---

## 14. First 30-Day Action Plan

| Day Range | Priority | Tasks | Output |
|---|---|---|---|
| Days 1-3 | Compliance lock | Confirm Phase 0 controls, certificate gates, clinical disclaimer, CDPH/legal questions | Phase 4 decision log |
| Days 1-5 | Source inventory | Collect approved content, approval docs, quizzes, certificates, policies | Asset audit workbook |
| Days 4-7 | Moodle readiness | Confirm staging/prod plan, backup approach, cron, roles, theme path | Environment checklist |
| Days 6-10 | MVP scope | Define exact MVP modules, excluded elite items, no-new-video plan | MVP scope document |
| Days 8-14 | Content conversion sprint 1 | Convert first modules into Books/Pages/Lessons | Prototype module |
| Days 10-15 | Certificate design | Draft certificate field map and affidavit workflow | Certificate/affidavit draft |
| Days 12-18 | Assessment build | Build question bank and final exam prototype | Quiz bank v0.1 |
| Days 15-20 | Clinical support prototype | Build optional support hub with disclaimers and upload warning | Clinical support v0.1 |
| Days 18-22 | Reporting dry run | Export enrollment, completion, quiz, affidavit, certificate evidence | Audit packet sample |
| Days 20-25 | QA scripts | Build test cases across learner/admin/RN/support roles | QA script set |
| Days 24-28 | Pilot readiness | Fix blockers and prepare pilot cohort instructions | Pilot launch packet |
| Days 29-30 | Go/no-go review | Review readiness, unresolved risks, staffing, rollback | MVP pilot decision |

---

## 15. Launch Readiness Checklist

| Area | Go Criteria |
|---|---|
| Compliance | Provider/course approval status and certificate language are documented or certificate launch is blocked. |
| Learner claims | Course copy states partial credit, online cap, and optional clinical support boundaries. |
| Content | Approved content is migrated, versioned, and frozen for pilot. |
| Time control | Active-time/pause mechanism is configured, tested, and exportable. |
| Interaction | Required interactions provide feedback and are tracked as expected. |
| Exam/test | Final exam/test is configured with approved pass/retake rules. |
| Affidavit | Final signed statement is required before certificate release and exportable. |
| Certificate | Required fields populate correctly; optional clinical support is not a gate unless approved. |
| Audit packet | Admin can export complete packet for a test learner. |
| Privacy | PHI warnings, upload instructions, and incident workflow are live. |
| Accessibility | Mobile, transcript, keyboard, screen reader smoke, and contrast checks are complete. |
| Roles | Least-privilege role matrix is tested. |
| Backups | Backup and restore test completed before launch. |
| Cron | Scheduled tasks run and completion/reporting updates as expected. |
| Support | Support queue, templates, escalation, and staffing schedule are ready. |
| Rollback | Rollback owner, trigger, and steps are documented. |

---

## 16. Go/No-Go Criteria, Rollback, and Monitoring

### Go Criteria

Launch can proceed only if certificate-related compliance gates pass, the audit packet can be generated, support is staffed, backup/restore is tested, and unresolved CDPH/legal dependencies are either closed or explicitly blocked from production certificate use.

### No-Go Criteria

Do not launch certificate issuance if any of the following remain unresolved:

- CDPH provider/course approval is missing for the online CE claim.
- Certificate template lacks required fields or approved wording.
- Learner can receive a certificate without identity confirmation, required time control, interaction/feedback, exam/test, or affidavit.
- Optional clinical support is configured as a certificate gate without written approval.
- Audit packet export cannot reproduce completion and certificate evidence.
- Privacy workflow for PHI uploads is not in place.

### Rollback Plan

| Trigger | Action | Owner |
|---|---|---|
| Certificate gate defect | Disable certificate activity; notify affected learners if needed; investigate logs | Moodle admin + registrar |
| Incorrect certificate issued | Void/reissue per policy; record exception; legal/compliance review | Registrar + compliance lead |
| PHI upload incident | Quarantine/delete per privacy workflow; suspend affected upload if needed | Privacy owner |
| Moodle outage | Activate support notice; restore from backup if required | IT/security |
| Content error in approved module | Hide affected activity; issue correction; version change log | Program owner |
| Support overload | Pause new enrollments or extend response SLA notice | Program owner |

### Monitoring

| Metric | Frequency | Owner | Action Threshold |
|---|---|---|---|
| Enrollment errors | Daily during launch | Registrar | More than 3 unresolved profile issues |
| Certificate failures | Daily during launch | Moodle admin | Any unexplained failure |
| Manual overrides | Weekly | Compliance lead | Any certificate override |
| Support tickets | Daily during launch | Support lead | Response SLA missed |
| Completion bottlenecks | Weekly | QA/support | More than 20% stuck at same activity |
| Backup status | Daily/weekly by schedule | IT/security | Any failed backup |
| Cron/scheduled tasks | Daily during launch | Moodle admin | Any repeated scheduled task failure |
| PHI/privacy incidents | Immediate/monthly trend | Privacy owner | Any confirmed PHI upload |
| Accessibility issues | Weekly pilot; monthly live | QA manager | Any blocker for core path |

---

## 17. Post-Launch Improvement Plan

Post-launch changes should be controlled through release notes and versioned course updates. Do not edit live certificate conditions casually.

| Timeframe | Focus | Outputs |
|---|---|---|
| Week 1 | Stabilize support, certificate gates, login/profile issues | Daily issue log and hotfix list |
| Weeks 2-4 | Analyze completion bottlenecks and support themes | Pilot/live launch report |
| Month 2 | Improve instructions, mobile UX, and audit exports | Minor release v1.1 |
| Month 3 | Review content accuracy and QA findings | Compliance/content review log |
| Quarterly | CDPH/CMS source monitoring and audit packet sample | Quarterly compliance operations review |
| Version 2 planning | Evaluate elite features only after MVP stabilizes | Prioritized upgrade roadmap |

Elite-version candidates should be justified by operational data: repeated support tickets, completion bottlenecks, learner feedback, audit burden, or documented clinical education value.

---

## 18. Source Register

[S0] CI Institute of Nursing, `PHASE_0_COMPLIANCE_FOUNDATION.md`, controlling compliance source for this Phase 4 report.  
[S1] California Health and Safety Code section 1337.6, renewal and online computer training requirements: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1337.6.  
[S2] CDPH, "Online Continuing Education Providers": https://www.cdph.ca.gov/Programs/CHCQ/LCP/Pages/Online-Continuing-Education-Providers.aspx  
[S3] CDPH 283A, "Certified Nurse Assistant (CNA) / Home Health Aide (HHA) In-Service Training / Continuing Education Units (CEUs)": https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph283a.pdf  
[S4] CDPH 283C, "Certified Nurse Assistant (CNA) and/or Home Health Aide (HHA) Renewal Application": https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph283c.pdf  
[S5] 22 CCR section 71839, "Renewal of Unexpired Certificates": https://www.law.cornell.edu/regulations/california/22-CCR-71839  
[S6] CDPH 192B, "Application for Initial/Renewal Approval as an Online Continuing Education Provider": https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph192b.pdf  
[S7] CDPH 192, "Application for Initial/Renewal Approval as a Continuing Education (CE) Provider": https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph192.pdf  
[S8] 42 CFR 483.95(g), required in-service training for nurse aides: https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-483/subpart-B/section-483.95  
[S9] California Health and Safety Code section 1337.1: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1337.1.  
[S10] W3C Web Accessibility Initiative, "WCAG 2 Overview": https://www.w3.org/WAI/standards-guidelines/wcag/  
[S11] Section508.gov, "IT Accessibility Laws and Policies": https://www.section508.gov/manage/laws-and-policies/  
[S12] HHS OCR, "Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the HIPAA Privacy Rule": https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html  
[S13] HHS OCR, "Guidance on HIPAA & Cloud Computing": https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html  
[S14] HHS/ED, "Joint Guidance on the Application of FERPA and HIPAA to Student Health Records" (2019): https://www.hhs.gov/sites/default/files/2019-hipaa-ferpa-joint-guidance.pdf  
[S15] Moodle Docs, "Site backup": https://docs.moodle.org/405/en/Site_backup  
[S16] Moodle Docs, "Course backup": https://docs.moodle.org/405/en/Course_backup  
[S17] Moodle Docs, "Automated course backup": https://docs.moodle.org/400/en/Automated_course_backup  
[S18] Moodle Developer Resources, "Access API": https://moodledev.io/docs/5.0/apis/subsystems/access  
[S19] Moodle Developer Resources, "Roles API": https://moodledev.io/docs/5.0/apis/subsystems/roles  
[S20] Moodle Docs, "Security checks": https://docs.moodle.org/500/en/Security_checks  
[S21] Moodle Docs, "Cron": https://docs.moodle.org/402/en/Cron  
[S22] Moodle Developer Resources, "Activity completion API": https://moodledev.io/docs/5.2/apis/core/activitycompletion

---

## Dependencies / Items for Final Reconciliation

This Phase 4 report should not be merged with other phases until the following items are reconciled by the final coordinating agent or project owner.

### Compliance / CDPH / Legal

| Item | Needed Decision |
|---|---|
| CDPH online CE provider status and NAC# | Confirm active approval before certificate issuance. |
| Course-level approval | Confirm each Moodle theory course/module title, objective, hour value, exam/test, and certificate language. |
| One certificate vs. multiple certificates | Confirm whether a 12-hour bundle can issue one certificate or must issue per approved course. |
| Electronic affidavit | Confirm whether the final signed statement may be electronic and what evidence must be retained. |
| Clinical support use | Confirm whether any clinical/lab/workplace support may count as CE/in-service credit; default is no. |
| Simulation/LTI | Confirm in writing before any simulation is counted for clinical or CE credit. |
| Direct reporting | Confirm whether CI Institute of Nursing has any direct ATCS/TULIP/CDPH reporting obligation. |
| Privacy obligations | Confirm HIPAA/FERPA/CMIA/business associate implications for hosting and uploads. |

### Moodle Architecture

| Item | Needed Decision |
|---|---|
| Hosting and backup architecture | Confirm production/staging, backup schedule, restore process, and retention storage. |
| Time tracking/control method | Confirm plugin/native method that enforces active time and excludes idle/bypass behavior. |
| Certificate tool | Confirm selected certificate plugin/tool supports required fields, release gates, and exports. |
| Role matrix | Confirm least-privilege roles for learner, instructor, RN/preceptor, admin reviewer, support, registrar, and site admin. |
| Reporting/export approach | Confirm how audit packets will be produced without excessive manual burden. |
| Security configuration | Confirm SSL, cron, password policy, security checks, plugin update process, and access restrictions. |

### Instructional Design

| Item | Needed Decision |
|---|---|
| Approved content map | Confirm migrated content maps to approved course objectives and hour values. |
| Interaction model | Confirm each required interaction gives meaningful feedback and is tracked. |
| Final exam blueprint | Confirm exam/test aligns with approved course material and retake policy. |
| TTS scripts | Confirm TTS scripts are exact approved content and voice authorization is documented. |
| Clinical support language | Confirm optional clinical support does not read as required credit or certificate gating. |
| Accessibility remediation | Confirm content files, transcripts, alt text, headings, and mobile layout pass QA. |

### Operations / Launch

| Item | Needed Decision |
|---|---|
| Staffing | Confirm launch support coverage, escalation owners, and backup staff. |
| Manual override authority | Confirm who can approve certificate-related overrides and how exceptions are audited. |
| Privacy incident response | Confirm quarantine/deletion/redaction steps and legal notification thresholds. |
| Pilot cohort | Confirm pilot size, entry criteria, success metrics, and feedback method. |
| Rollback authority | Confirm who can disable certificate release, pause enrollment, or revert a course version. |
| Post-launch audit | Confirm first audit packet review date and quarterly review cadence. |
