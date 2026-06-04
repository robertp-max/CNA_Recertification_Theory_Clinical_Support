# Phase 2: Self-Hosted Moodle Architecture Report

**Project:** California CNA Recertification Moodle Architecture  
**Prepared for:** CI Institute of Nursing  
**Scope:** Phase 2 only - self-hosted Moodle architecture, plugins, tracking, certificates, mobile UX, optional clinical support hub  
**Controlling source:** `PHASE_0_COMPLIANCE_FOUNDATION.md`  
**Status:** Technical architecture blueprint; not legal advice; not final reconciliation  
**Prepared:** May 25, 2026

---

## 1. Executive Summary

CI Institute of Nursing should build the California CNA online CE experience as a self-hosted Moodle site with a strict separation between: (1) the CDPH-approved online CE theory pathway that may issue a California CNA online CE certificate only after all required gates are met, and (2) a clinical support hub used for optional learner support, scheduling, refresh resources, de-identified documentation support, and staff review. The optional clinical support hub must not become a certificate gate for the 12-hour online CE certificate unless CDPH gives written approval for the exact use case.

The MVP should prioritize Moodle-native content conversion, not new video production: Books, Pages, Lessons, H5P, Quiz, Feedback, Assignment/Database forms, transcripts, downloadable job aids, approved cloned-voice TTS where authorized, completion tracking, Restrict access, logs, a time-tracking plugin, Custom certificate, and exportable audit packets. This aligns with Phase 0: California CNA renewal requires 48 hours over two years, at least 12 hours each year, with only 24 hours allowed online through CDPH-approved online CE. The proposed 12-hour Moodle theory course is partial renewal credit only.

The core compliance architecture should use layered evidence, not seat time alone: identity confirmation, required profile fields, sequential gates, active-time tracking, meaningful interaction/feedback, final exam/test, signed statement/affidavit before certificate issuance, immutable certificate records, manual override controls, and exportable logs. Moodle core provides much of the gate structure; third-party plugins are useful for certificate generation, active-time evidence, scheduling, attendance/checklists, and custom SQL reporting, but every plugin must be tested for Moodle version compatibility, privacy API support, mobile behavior, and update cadence before production.

---

## 2. Recommended Self-Hosted Moodle Architecture

### Version Strategy

Use a supported Moodle release with security runway and plugin compatibility. As of the Moodle release calendar, Moodle 4.5 is the current LTS with security support through October 2027; Moodle 5.2 is current stable with security support through October 2027; Moodle 5.3 LTS is planned for October 2026 with security support through October 2029. Moodle 5.0 is already outside general bug-fix support and should not be selected for a new compliance-sensitive build. [M1]

**Recommended path:** launch MVP on Moodle 4.5 LTS if plugin compatibility and operational conservatism are most important; evaluate Moodle 5.2/5.3 LTS in staging before production if CI Institute wants the newer interface and can validate all plugins. Do not launch on an unsupported or near-end-of-support version.

### Hosting Pattern

Use a self-hosted production environment with separate development and staging environments. Production should run on a hardened Linux VM or managed container platform with a dedicated database server, object/file storage or protected Moodledata volume, TLS, web application firewall controls if available, cron, monitored backups, and centralized logs. Use PostgreSQL or MySQL/MariaDB versions supported by the selected Moodle release. Moodle 5.0 minimums include PHP 8.2+, PostgreSQL 14+, MySQL 8.4+, MariaDB 10.11+, and required PHP sodium; exact requirements must match the selected version. [M2]

### Environment Model

- **Development:** plugin trials, theme changes, custom dashboards, report prototypes, no real learner data.
- **Staging:** production-like copy with masked data; certificate gate testing; plugin upgrade testing; mobile app testing; audit packet dry runs.
- **Production:** locked certificate templates, controlled roles, approved course content only, PHI-prevention controls, monitored cron and backups.

### Course Structure

Create a course category for `California CNA Online CE` and a separate category or course shell for `Optional Clinical Support`. The theory course should be organized in short, mobile-first sections using Topics format or a one-topic-at-a-time course format after mobile testing. Use one-hour or approved-hour units that map exactly to the approved CDPH course list. The optional clinical hub should be visibly labeled as learner support and documentation support, not California renewal clinical-hour credit unless written CDPH approval exists.

---

## 3. Moodle Core Configuration Matrix

| Architecture Area | Moodle-Native Setting | Recommended Configuration | Compliance Value | Learner Value | Admin Risk |
|---|---|---|---|---|---|
| Version | Moodle release branch | Use 4.5 LTS for MVP unless 5.2/5.3 plugin testing is complete | Supported security lifecycle | Stable interface | Newer plugins may target newer branches |
| Environments | Separate sites | Dev, staging, production with no production edits directly | Change control and evidence integrity | Fewer disruptions | Requires disciplined deployment |
| Course categories | Course/category management | Separate online CE from optional clinical support | Prevents credit confusion | Clear pathways | Mislabeling may create regulatory risk |
| Course format | Topics or tested mobile-friendly format | Short units, clear "next required step" labels | Supports sequential evidence | Less cognitive load | Third-party formats add plugin risk |
| Completion tracking | Site advanced feature and course completion | Enable globally; define activity and course completion rules | Required evidence layer | Progress visibility | Misconfigured completion can release certificate early |
| Restrict access | Advanced feature and per-activity restrictions | Lock each required item behind prior completion/time/grade conditions | Prevents bypass to exam/certificate | Clear sequence | Hidden restrictions can confuse learners |
| Gradebook | Categories and grade-to-pass | Separate practice, final exam, affidavit, optional clinical; final exam must have pass threshold | Assessment gate evidence | Shows status | Wrong aggregation can pass learners incorrectly |
| Question bank | Categories/subcategories | Organize by approved course/module/objective; use draft/review status | Exam traceability and QA | Better assessments | Poor version control undermines audit |
| Quiz | Core activity | Final exam/test with attempts, time limits if appropriate, grade-to-pass, review controls | Required CDPH exam/test evidence | Clear completion target | Question exposure and retake policy need approval |
| H5P | Core H5P activity + Content bank | Use accessible, low-bandwidth H5P activities; track attempts and completion | Interaction/feedback evidence | Short active practice | H5P reports are not the same as Moodle grade-to-pass [M3] |
| Lesson/Book/Page | Core resources/activities | Convert approved content into Moodle-native readings and lessons | No-video MVP content delivery | Phone-friendly chunks | View-only completion is weak alone |
| Feedback | Core activity | Identity/course attestation, course feedback, support requests where appropriate | Interaction/support evidence | Simple forms | Not a substitute for final affidavit |
| Assignment | Core activity | Use only for de-identified optional support uploads | Timestamped optional evidence | Easy mobile upload | PHI upload risk |
| Database activity | Core activity | Structured optional clinical evidence records with required non-PHI attestations | Exportable support records | Guided documentation | Free text can collect PHI |
| Groups/cohorts | Core enrollment tools | Use cohorts for CNA CE cohorts; groups for sections, reviewers, clinical support | Scoped reporting and permissions | Relevant announcements | Group leakage if roles are broad |
| Roles | Role definitions/capabilities | Learner, Instructor, RN/Preceptor Evaluator, Admin Reviewer, Registrar, Site Admin | Least privilege | Right staff respond | Over-broad roles threaten certificate integrity |
| Reports | Logs, activity completion, course completion, grade export | Preserve raw logs and summary reports; export per learner | Audit packet foundation | Transparent status | Log retention must be configured |
| Notifications | Forum/calendar/messaging | Use announcements, due reminders, exam/certificate alerts | Supports timely completion | Reduces missed steps | Too many messages cause fatigue |
| Data privacy | Data registry/privacy officer workflow | Retention purpose for CE records at least four years pending legal review | Record retention and privacy governance | Predictable data handling | Plugin privacy gaps can block SAR/export [M4] |
| Backups | Site/database/file backups plus course backups | Nightly database/file backups; tested restore; course backups not primary backup | Evidence recoverability | Continuity | Course backups alone are insufficient [M5] |

---

## 4. Plugin and Feature Matrix

| Need | Moodle Core Option | Plugin Option | Why Use It | MVP or Elite? | Compliance Value | Learner Value | Maintenance / Privacy Risk |
|---|---|---|---|---|---|---|---|
| Interactive activities | H5P activity, Lesson, Quiz | H5P content libraries | Core H5P supports Content bank, attempts, grades, and app support | MVP | Interaction/feedback evidence | Short practice | Choose accessible maintained content types [M3][M6] |
| Certificate generation | Completion + manual PDF outside Moodle | Custom certificate (`mod_customcert`) | Dynamic PDF, certificate code verification, revocation/issued list | MVP | Certificate issuance evidence | Instant certificate after gates | Plugin must match Moodle branch; public verification must not expose private data [P1] |
| Active time tracking | Logs only | Timestat (`block_timestat`) or Dedication (`block_dedication`) | Timestat counts active browser/tab time and pauses on inactivity; Dedication estimates from logs | MVP pilot | Supports 50-minute active participation requirement | Visible time progress if enabled | Time plugins must be validated; logs/seat time alone insufficient [P2][P3] |
| Sequential progress display | Activity completion report | Completion Progress block | Visual progress bar | MVP if compatible | Helps learners complete gates | Reduces confusion | Verify compatibility with selected Moodle version |
| Checklist/skills list | Moodle completion, Database, Assignment rubrics | Checklist plugin | Simple optional support checklist | Post-MVP unless validated | Optional documentation support only | Clear to-do list | Plugin compatibility/privacy review required |
| Scheduling | Calendar, Choice, groups | Scheduler (`mod_scheduler`) | Teachers create slots; learners book; staff record outcomes | MVP if clinical support included | Optional clinical/support scheduling records | Easy appointment booking | Latest Moodle plugin directory release may lag; test branch and mobile behavior [P4] |
| Attendance | Manual grade item, Database | Attendance plugin | Tracks session attendance for optional support or live workshops | Post-MVP | Optional evidence; not online CE gate | Clear attendance status | Do not imply state clinical credit |
| Reporting | Core logs, completion, grade export, Report builder | Ad-hoc database queries (`report_customsql`) | Admin SQL reports can run on demand/schedule and export CSV | MVP for audit exports | Audit packet automation | Faster support | SQL access is powerful; restrict to admins [P5] |
| Configurable reports | Core Report builder | Configurable Reports | Historically useful but support concerns exist | Avoid for new build | Custom reports | Admin convenience | Open LMS notes phase-out/security/compatibility concerns [P6] |
| Forms | Feedback, Database, Assignment, Quiz | Questionnaire/Form plugins | Core tools are enough for MVP | Core MVP | Attestations/support requests | Simple forms | Third-party form plugins add privacy burden |
| QR verification | Custom certificate verification code | Custom QR element or custom verification page | Verify certificates without exposing data | Post-MVP if not built into template | Fraud reduction | Employer confidence | Public verification must use minimal disclosure |
| SMS reminders | Email/calendar/app notifications | SMS gateway/local plugin/custom integration | Useful for working CNAs | Post-MVP | Reduces missed deadlines | Helpful nudges | Consent, opt-out, data sharing, cost |
| LTI simulation | External tool | LTI provider tools | Do not use as MVP compliance dependency | Avoid for MVP | None unless approved | Optional practice | Do not count toward clinical hours without CDPH approval |
| SCORM/xAPI | SCORM package | xAPI/LRS plugins | Not needed if using Moodle-native content | Avoid MVP | Can add trace data | Familiar package model | Adds complexity; avoid if cloned content can be native |
| Accessibility checking | Moodle editor tools/manual QA | Brickfield or external accessibility checker | Useful quality control | Post-MVP/Elite | Accessibility risk reduction | Better readable content | Plugin/service privacy and license review |
| Learning analytics | Core analytics | Custom risk dashboard | Useful for intervention, not certificate gate | Elite | Early support flags | Timely help | Avoid opaque automated decisions |

---

## 5. Time Tracking and Completion Model

Moodle can natively track activity completion, course completion, grades, quiz attempts, H5P attempts, assignment submissions, logs, and report exports. Moodle core cannot by itself prove CDPH's active-time control requirement with idle exclusion at the precision needed for online CE; use a validated active-time plugin or custom time-control component paired with completion, interaction, and assessment evidence.

### Recommended Theory Gate Sequence

1. Learner completes identity/profile confirmation: legal name, CNA certificate number, renewal-cycle acknowledgement, online-hour cap acknowledgement, no shared account attestation.
2. Learner completes approved content unit: Book/Page/Lesson readings, TTS audio with transcript if used, downloadable job aid if relevant.
3. Learner completes required interaction: H5P, Lesson question, discussion prompt, short knowledge check, or Feedback activity with meaningful automated or instructor feedback.
4. Active-time plugin records at least 50 active minutes per approved CE hour, excluding idle time to the extent technically feasible.
5. Sequential Restrict access unlocks the module quiz or final exam only after required content, interaction, and active-time milestones.
6. Learner passes exam/test with approved passing score and retake rules.
7. Learner signs final statement/affidavit before certificate issuance.
8. Custom certificate releases only if all automated conditions are met and no admin hold exists.

### Evidence Matrix

| Evidence Type | Moodle Source | Native / Plugin / Custom | Purpose | Strength | Weakness | Audit Use |
|---|---|---|---|---|---|---|
| Login/authentication logs | Moodle logs | Native | Identity/access trail | Medium | Shared account risk | Supports identity confirmation |
| Required profile fields | User profile/custom fields | Native | Legal name/CNA number capture | Medium | Self-entered | Certificate field source |
| Activity completion | Completion tracking | Native | Shows required resources/activities completed | Medium | Completion can be view-only | Gate and summary report |
| Sequential unlocking | Restrict access | Native | Prevents bypass | Strong | Configuration-sensitive | Demonstrates no direct exam/certificate access |
| H5P attempts | H5P attempts report | Native H5P | Interaction and feedback evidence | Medium/strong | H5P completion not identical to grade-to-pass | Interaction proof |
| Lesson/Quiz grades | Gradebook/Quiz reports | Native | Knowledge checks/final exam | Strong | Question quality/retake policy risk | Assessment evidence |
| Active time | Timestat/Dedication/custom | Plugin/custom | Active participation minutes | Strong if validated | Plugin accuracy and browser/app limitations | Time/pause evidence |
| Moodle event logs | Standard logs/logstore | Native | Raw chronology | Strong | Retention/performance planning needed | Audit reconstruction |
| Affidavit | Feedback/Assignment/custom form | Native/custom | Required signed statement before certificate | Strong if e-sign accepted | E-sign acceptance needs CDPH/legal review | Required certificate precondition |
| Certificate issue record | Custom certificate report | Plugin | Certificate ID/code/date/revocation | Strong | Plugin dependency | Issuance proof |
| Manual override record | Custom form/log | Custom/manual | Exception control | Strong if restricted | Human process risk | Exception audit |
| Export packet | Report builder/custom SQL/script | Native/plugin/custom | Consolidated evidence | Strong | Needs QA | CDPH/internal review packet |

**Audit packet contents:** learner identity fields, enrollment and completion dates, module completion report, active-time report, H5P/interaction attempt evidence, final exam attempt/score, affidavit record, certificate PDF and issue log, override log if any, course version/approval metadata, and export timestamp.

---

## 6. Certificate Release Architecture

The online CE certificate must map to Phase 0 requirements and should be released only for the approved online theory CE pathway. Optional clinical support evidence should not gate the online CE certificate unless CDPH/legal review explicitly requires it. If CI Institute later obtains written approval for a combined online/clinical certificate, create a separate certificate type and approval-controlled rule set; do not retrofit the online CE certificate silently.

### Certificate Fields

Use locked certificate template fields for provider/program name, provider address, contact person/telephone, learner legal name, CNA certificate number, approved course name, completion date, CE hours, online-course indicator, CE provider ID/NAC#, retention statement, certificate ID, verification code, authorized signature line, and state-specific partial-credit disclaimer. Do not include clinical hours as California renewal credit unless written CDPH approval exists.

### Release Conditions

| Certificate Condition | Moodle Tool / Setting | Automated or Manual | Risk if Misconfigured | QA Test |
|---|---|---|---|---|
| Legal name present | Required profile field | Automated | Wrong certificate identity | Try certificate with blank/mismatched profile |
| CNA certificate number present | Required profile field | Automated | Missing required field | Attempt release without CNA number |
| Online-hour cap acknowledgement | Feedback/Quiz attestation | Automated | Learner may exceed 24 online hours | Attempt release without attestation |
| Identity confirmation | Profile + attestation + login controls | Automated/manual | Shared account or false identity | Confirm audit fields and admin review path |
| All required theory modules complete | Course completion | Automated | Premature certificate | Skip one module and verify lock |
| Active time threshold met | Time plugin condition/custom hold | Automated/custom/manual | Fails CDPH time/pause control | Try exam/certificate before minimum active time |
| Required interaction complete | H5P/Lesson/Quiz completion | Automated | Token non-interactive content | Skip H5P and verify lock |
| Final exam/test attempted | Quiz | Automated | No assessment evidence | Attempt release without exam |
| Passing score met | Quiz grade-to-pass + Restrict access | Automated | Failed learner receives certificate | Submit failing attempt and verify lock |
| Final signed affidavit | Feedback/Assignment/custom e-sign | Automated/manual | Missing statutory statement | Attempt release without signed statement |
| Admin hold clear | Custom profile/course field or manual review workflow | Manual/custom | Known exception still issues certificate | Place hold and verify lock |
| Certificate template locked | Custom certificate permissions | Manual/admin | Staff edit approved wording | Confirm only Registrar/Admin can edit |
| Verification code generated | Custom certificate | Automated | Weak fraud control | Validate code and privacy-limited verification |
| Manual override logged | Custom form + logs | Manual | Undocumented exception | Override test requires approver/reason/date |

**CDPH/legal review flag:** electronic signature acceptability for the final signed statement/affidavit should be confirmed in writing. If not accepted, the system must collect and retain the required wet-signature process before certificate release.

---

## 7. Clinical Documentation Architecture

The clinical Moodle component should be a supportive hub, not a California renewal clinical-credit engine. It may help learners prepare, schedule optional refresh activities, track de-identified documentation, request staff support, and organize employer/preceptor signoffs. It must not be represented as required California renewal clinical hours and must not count simulation, virtual simulation, or LTI simulation toward clinical hours without written CDPH approval.

| Clinical Need | Moodle Tool | Learner Steps | RN/Preceptor Steps | Admin Steps | Evidence Created | Friction Risk |
|---|---|---|---|---|---|---|
| Clinical support orientation | Page/Book | Read expectations and non-PHI rules | None | Keep page current | View/completion log | Low |
| Scheduling guidance | Scheduler or Choice + Calendar | Pick available support slot or express preference | Confirm slot if applicable | Manage capacity | Booking record | Medium if plugin mobile UX is poor |
| Optional skills confidence checks | Ungraded Quiz/H5P | Complete self-check | None unless reviewed | Monitor support needs | Attempt/completion record | Low if clearly optional |
| De-identified evidence upload | Assignment | Upload only permitted non-PHI document/photo | Optional comment/signoff | Review/accept/reject | Timestamped submission | High PHI risk |
| Structured support log | Database activity | Enter date, setting type, non-PHI activity category | Optional verification fields | Export records | Structured record | Medium |
| RN/preceptor signoff | Assignment rubric, Database fields, or custom form | Invite/upload signed non-PHI form | Confirm name/title/contact/signature | Verify sample records | Signoff artifact | Medium/high if unverifiable |
| Attendance support | Attendance plugin or Database | Check status | Mark attendance if live session | Export as optional support record | Attendance log | Medium if mistaken for CE credit |
| Rejected submission workflow | Assignment feedback | Read reason and resubmit | Add clarification if needed | Reject with standard reasons | Feedback history | Medium |
| Resource hub | Book/Page/File | Use job aids/checklists | None | Maintain current resources | Access logs | Low |
| Admin review | Completion report/custom SQL | Respond to requests | N/A | Review dashboard | Review decision log | Medium |

**Required privacy design:** every upload/form area must display a non-PHI warning, require a no-PHI attestation, prefer structured fields over narratives, and include a quarantine/delete workflow for accidental PHI. Learners should be told not to upload patient names, faces, medical record numbers, chart screenshots, dates of birth, medication records, addresses, or any information that can identify a patient/resident. HHS guidance treats de-identification as Safe Harbor removal or Expert Determination; cloud systems that maintain PHI can trigger HIPAA business associate obligations. [C1][C2]

---

## 8. Scheduling Architecture

| Scheduling Need | Moodle Tool | Learner Experience | Admin Experience | Mobile UX | Risk / Limitation |
|---|---|---|---|---|---|
| Simple cohort due dates | Calendar | Sees course/exam/support dates | Create events and reminders | Good in app/browser | Not appointment booking |
| One-time preference poll | Choice | Select preferred time/location | Export choices manually | Simple on phone | No robust capacity workflow |
| Appointment slots | Scheduler plugin | Book available slot | Create slots, capacity, notes/outcomes | Must be tested | Plugin release cadence/compatibility risk |
| Group support sessions | Groups + Scheduler/Calendar | Sees group-specific slot | Assign group capacity | Good if labels clear | Wrong group settings can hide info |
| Waitlist | Choice/Database/manual | Submit waitlist request | Manually process | Acceptable MVP fallback | Manual burden |
| Reminders | Calendar, forum announcements, messaging, app notifications | Receives due-date nudges | Configure reminders | App push requires mobile services | Notification fatigue |
| Manual scheduling fallback | Page + support form | Request help from staff | Staff books externally | Works on phone | Less audit automation |

MVP should use Calendar, Announcements, Choice, and manual support forms unless Scheduler is validated on the selected Moodle version and mobile workflow. Scheduler is valuable for optional support slots because it lets teachers define slots and students choose appointments; teachers can record outcomes and optional grades, but that outcome should not be used for online CE certificate release unless CDPH approves a clinical gate. [P4]

---

## 9. Mobile UX and Accessibility Strategy

The target learner is likely working on a phone, during limited breaks, with fatigue and variable bandwidth. The design should minimize scrolling fatigue, avoid large media, and show the next required action plainly.

| UX Need | Moodle Configuration | Theme / Plugin Option | Implementation Note | Risk |
|---|---|---|---|---|
| Phone-first navigation | Boost-based responsive theme | Boost core; evaluate Moove/Trema/Edwiser only after compatibility review | Use short section names and one clear next step | Theme plugins can lag releases |
| Low bandwidth | Pages/Books/Lessons, compressed images, short audio | No new video MVP | Keep H5P packages small; avoid autoplay-heavy media | Large H5P packages hurt app/offline use |
| Clear progress | Completion checkboxes, course completion, progress block | Completion Progress block if compatible | Show module progress and certificate gates | Progress can mislead if optional items mixed |
| App support | Enable Moodle App services | Official Moodle App | Requires trusted SSL; self-signed certs do not work | App offline logs sync with sync time, not original offline time [M7] |
| Push reminders | Messaging/mobile notifications | Moodle notifications/AirNotifier | Use for due dates, missing affidavit, failed exam support | Registered site/app plan limitations [M7] |
| Accessibility | WCAG-aware content and Moodle accessibility baseline | Accessibility checker post-MVP | Use headings, alt text, captions, transcripts, readable fonts | Third-party H5P/LTI accessibility varies [M6][M8] |
| TTS audio | Embedded short audio + transcript | Approved TTS workflow outside Moodle | Audio is supplemental; transcript is primary | Unauthorized voice clone risk |
| H5P mobile fit | Core H5P activity | Use accessible H5P types | Prefer True/False, Summary, Accordion, Interactive Book; test drag/drop | Some H5P types have known limits [M6] |
| Tap targets | Theme/content authoring | Core theme CSS | Avoid dense tables inside lessons; use buttons and headings | Custom CSS may break upgrades |
| Offline/limited connectivity | Moodle App download settings | Official app | Offline support useful for content, but compliance time evidence must be reviewed carefully | Offline tracking sync limitations |

Moodle's accessibility conformance work aligns to WCAG 2.2 AA, but third-party content, themes, H5P content types, and locally authored materials determine the real learner experience. Accessibility QA must test the actual course on iOS/Android, browser, screen reader/keyboard navigation, zoom, and low bandwidth. [M8]

---

## 10. MVP No-Video / Approved TTS Technical Plan

MVP must not depend on new video production. Convert approved cloned content into Moodle-native formats with short readings, interactions, and assessments. Use approved cloned-voice TTS only when the voice is authorized, documented, cleared for this training purpose, generated from approved course text, and paired with transcripts. No impersonation or unapproved voice use.

| Content Type | MVP Moodle Format | TTS Use? | Transcript Requirement | Compliance Risk | Production Effort |
|---|---|---|---|---|---|
| Approved lesson text | Book/Page/Lesson | Optional short segments | Required if audio used | Low if source text approved | Low |
| Case prompt | Lesson or H5P | Usually no | Text is primary | Low | Low |
| Knowledge check | Quiz/Lesson/H5P | No | N/A | Low | Low |
| Job aid/checklist | PDF/File/Page | Optional | Required if audio used | Low | Low |
| Procedure refresh | Book/Page with still images | Optional | Required | Medium; avoid implying clinical validation | Medium |
| Instructor lecture | Text lesson + TTS | Yes only if approved | Required | Voice authorization risk | Medium |
| Video replacement | Book + H5P + TTS | Yes if approved | Required | Must not reduce required interactivity/exam | Medium |
| Optional clinical support instructions | Page/Book | Optional | Required | Must not imply required clinical credit | Low |
| Final exam | Quiz | No | N/A | High if questions not approved | Medium |
| Affidavit | Feedback/custom form | No | N/A | E-sign acceptance needs review | Low |

---

## 11. Custom Component Opportunities

| Component | Purpose | User Role Served | Build Complexity | Compliance Value | Learner Value | MVP Alternative |
|---|---|---|---|---|---|---|
| Compliance status widget | Shows missing gates for certificate | Learner/Admin | Medium | High | High | Course completion + labels |
| Admin audit packet generator | Exports identity, time, quiz, affidavit, certificate | Admin/Registrar | Medium/high | High | Indirect | Custom SQL + manual export |
| Active-time compliance hold | Converts time plugin output into release condition | Admin/Learner | High | High | Clear status | Manual admin review of time report |
| Certificate verification page | Privacy-limited public verification | Employer/Admin | Medium | Medium/high | Confidence | Custom certificate code verification |
| Clinical support tracker | Optional support status, not certificate gate | Learner/Admin | Medium | Medium | Medium | Database activity |
| Preceptor signoff workflow | Structured signoff and verification sampling | Preceptor/Admin | High | Medium if optional | Medium | Assignment upload + rubric |
| "Next best action" dashboard | One-button next step | Learner | Medium | Medium | High | Course format labels |
| SMS reminder integration | Text nudges for deadlines | Learner | Medium/high | Medium | High | Email/app notifications |
| Expiring certificate reminder | Renewal-cycle reminders | Learner/Registrar | Medium | Medium | Medium | Calendar reminders |
| Progress heatmap | Intervention targeting | Instructor | Medium | Low/medium | Indirect | Completion reports |
| State audit report | CDPH-focused summary | Admin | High | High | Indirect | Custom SQL reports |
| Clinical resource hub widget | Quick access to optional resources | Learner | Low/medium | Low | Medium | Course section |

**Build first:** audit packet generator, compliance status widget, active-time compliance hold if plugin data cannot gate certificates natively.  
**Build later:** certificate verification page, next best action dashboard, SMS integration, clinical support tracker.  
**Avoid unless necessary:** LTI simulation credit logic, custom SCORM/xAPI stack, complex AI risk scoring, any workflow that converts optional clinical support into required renewal credit without written CDPH approval.

---

## 12. Support and Communication Model

| Support Need | Moodle Tool | Learner Experience | Staff Workflow | Required or Optional |
|---|---|---|---|---|
| Official updates | Announcements forum | Receives course announcements | Instructor posts controlled updates | Required |
| "I'm stuck" path | Page + Feedback form | One clear help button | Staff triage submissions | Required |
| Course Q&A | Forum | Ask non-private questions | Instructor moderates | Optional but useful |
| Private help | Messaging or support form | Contact staff | Staff respond with SLA | Required |
| Tech support FAQ | Book/Database | Search quick answers | Admin maintains entries | Required |
| Missing gate alert | Completion report + manual message | Receives targeted nudge | Staff run weekly report | Required for MVP |
| Failed exam support | Quiz feedback + message | Gets next steps | Instructor reviews attempts | Required |
| Affidavit reminder | Restrict access label + notification | Knows certificate is waiting on signature | Registrar monitors | Required |
| Clinical support contact | Page/support form | Gets optional clinical help | Clinical coordinator responds | Optional support |
| Office hours | Scheduler/Calendar | Books support slot | Staff manage appointments | Optional |
| Preceptor communication | Downloadable instructions/form | Shares clear instructions | Admin verifies returned form | Optional |
| Admin alerts | Custom SQL/report | N/A | Admin reviews exceptions | Post-MVP helpful |

---

## 13. Security, Privacy, Backup, and Log Retention Notes

### Security Controls

- Enforce TLS with trusted certificates; Moodle App does not work with self-signed certificates. [M7]
- Use MFA for administrators, registrars, instructors, and reviewers if available through SSO or authentication plugin.
- Disable self-registration unless needed; use controlled enrollment/cohorts.
- Apply least privilege: RN/preceptor evaluator should not edit certificate templates, gradebook formulas, or course completion rules.
- Restrict plugin installation to site administrators and require staging validation before production.
- Keep Moodle core, plugins, PHP, database, and OS patched.
- Configure cron and task monitoring; completion, backups, H5P libraries, notifications, and reports depend on scheduled tasks.
- Use locked certificate templates and restricted Custom certificate capabilities.
- Log manual overrides with approver, reason, learner, course, date/time, and evidence reviewed.

### Privacy and PHI Prevention

The system should be designed to avoid PHI entirely. Optional clinical support workflows must not request patient/resident information. Use structured fields, required no-PHI attestation, upload warnings, staff review, and deletion/quarantine workflow for accidental PHI. If PHI collection becomes unavoidable, stop and obtain legal/privacy review, HIPAA/CMIA analysis, and hosting/BAA review before launch. [C1][C2]

### Backups and Retention

Use database backups, Moodledata backups, configuration backups, and restore testing as the primary disaster recovery model. Moodle automated course backups can help recover or reuse courses but should not be the only backup method. [M5] Retain certificate, completion, affidavit, exam, active-time, and log evidence for at least four years from completion unless counsel approves a different longer schedule; Phase 0 notes CDPH provider/CNA record expectations and three-year online signed statement retention, so the stricter four-year minimum is recommended pending final review.

### Plugin Privacy

Before installing a plugin in production, verify that it supports the selected Moodle release, implements Moodle Privacy API expectations where it stores personal data, has a credible maintenance path, and can be exported/deleted through Moodle privacy workflows where required. Moodle's privacy registry flags plugins that do not implement the privacy API; those plugins can create data export/deletion gaps. [M4]

---

## 14. Moodle Architecture Risk Register

| Risk | Likelihood | Impact | Mitigation | CDPH/Legal Review Flag |
|---|---:|---:|---|---|
| Online CE certificate issued before all controls are met | Medium | High | Automated gates, negative QA tests, manual hold | No, unless control model changes |
| Optional clinical hub treated as required renewal clinical credit | Medium | High | Separate course/category, disclaimers, no certificate gate | Yes |
| Simulation/LTI counted as clinical hours | Medium | High | Exclude from MVP credit logic | Yes |
| Active-time plugin inaccurate or incompatible | Medium | High | Pilot, compare logs, document settings, manual review fallback | Possibly |
| Learner exceeds 24-hour online cap | High | High | Learner attestation and certificate disclaimer | No |
| Certificate missing required fields | Medium | High | Locked template mapped to Phase 0 matrix | Possibly for exact wording |
| E-sign affidavit not accepted | Medium | High | Written CDPH/legal confirmation; wet-sign fallback | Yes |
| PHI uploaded in optional clinical area | Medium | High | No-PHI warnings, structured forms, quarantine/delete process | Yes |
| Plugin abandoned after launch | Medium | Medium/high | Prefer core, LTS branch, staging tests, update plan | No |
| Mobile app offline evidence timing misunderstood | Medium | Medium/high | Treat offline records cautiously; require sync before certificate | No |
| Manual override abused | Low/medium | High | Restrict capability, approval record, monthly audit | No |
| New video production delays launch | Medium | Medium | No-video MVP, Moodle-native content and TTS | No |
| Accessibility gaps in H5P/theme | Medium | Medium/high | Use accessible H5P types and QA on devices | No |
| Logs deleted before audit | Low/medium | High | Retention policy, backup/export schedule | No |

---

## 15. MVP Technical Stack

- **Moodle version:** Moodle 4.5 LTS unless staging proves Moodle 5.2/5.3 readiness.
- **Theme:** Boost or minimally customized Boost child theme; use CI Institute logo/brand colors from the Branding Kit without heavy custom UX.
- **Core activities:** Book, Page, Lesson, Quiz, H5P, Feedback, Assignment, Database, Forum, Calendar.
- **Core controls:** Completion tracking, Course completion, Restrict access, Gradebook, Question bank, Logs, Reports, Cohorts, Groups, Roles, Data privacy registry.
- **Plugins:** Custom certificate; one validated active-time tracking plugin such as Timestat or Dedication; Ad-hoc database queries for admin-only audit exports if needed; Scheduler only if optional clinical support scheduling is in MVP and plugin compatibility is validated.
- **Content approach:** approved cloned content converted into Moodle-native text/interaction formats, approved TTS audio snippets where authorized, transcripts, no new video dependency.
- **Certificate:** online CE certificate only; gated by identity, completion, active-time evidence, interaction, final exam/pass, affidavit, and admin hold status.
- **Clinical hub:** optional support resources, scheduling guidance, non-PHI evidence upload/support forms, clear disclaimers, no online CE certificate gate.
- **Exports:** per-learner audit packet using native reports plus custom SQL/manual assembly.

---

## 16. Elite Technical Stack

- **Custom learner dashboard:** next required step, active-time progress, exam readiness, affidavit status, certificate status.
- **Audit packet generator:** one-click ZIP/PDF/CSV package per learner and cohort.
- **Certificate verification portal:** tokenized, privacy-limited validation with certificate code/QR.
- **Custom active-time hold:** native-grade/completion compatible condition fed by validated time data.
- **Advanced support nudges:** app notifications, email, and SMS with consent/opt-out.
- **Clinical support workflow:** structured preceptor signoff, verification sampling, rejection/resubmission workflow, non-PHI enforcement.
- **Accessibility QA tooling:** external checker or validated Moodle plugin plus human mobile/screen-reader testing.
- **Operational dashboards:** plugin health, cron status, backup restore status, certificate exceptions, learners at risk.
- **Upgrade pipeline:** automated staging clone, plugin compatibility test scripts, negative certificate gate tests.

---

## 17. Recommendations for the Compliance Team

- Confirm CI Institute's CDPH online CE provider status, NAC#, approved course list, approved certificate wording, and whether each one-hour module requires separate certificate handling.
- Confirm e-signature acceptability for the final signed statement/affidavit; if uncertain, require a wet-signature fallback before certificate issuance.
- Approve exact learner-facing disclaimers: 12-hour online theory is partial renewal credit only, California online CE cap is 24 hours per renewal cycle, and optional clinical support is not required California renewal clinical credit unless CDPH approves it.
- Review all certificate fields against Phase 0 before production.
- Review PHI/CMIA/HIPAA/FERPA exposure for optional clinical documentation workflows.

---

## 18. Recommendations for the Instructional Design Team

- Convert only approved source content into Moodle-native formats for MVP.
- Use meaningful interaction in every required unit: H5P, Lesson decision points, short quizzes, case prompts, or feedback with learner input and feedback.
- Keep activities short, mobile-first, transcript-supported, and low bandwidth.
- Avoid building instructional content for Phase 3 in this architecture document; maintain placeholders for approved course objectives and assessments.
- Label optional clinical practice, confidence checks, and simulations as support/practice only unless written CDPH approval says otherwise.

---

## 19. Recommendations for the Migration/Operations Team

- Build dev, staging, and production before importing real learners.
- Create a deployment checklist for Moodle core version, PHP/database versions, cron, backups, TLS, mail, mobile services, plugins, and permissions.
- Test negative certificate cases before launch: missing CNA number, insufficient active time, skipped H5P, failed exam, missing affidavit, admin hold, expired approval metadata, manual override.
- Maintain a plugin register with version, source URL, maintainer, selected branch, privacy API status, mobile status, and rollback plan.
- Run restore tests and audit-packet export tests before go-live.
- Monitor CDPH/CMS source changes in coordination with the compliance team, but do not perform final reconciliation in Phase 2.

---

## Source Register

### Moodle Core and App Sources

[M1] Moodle Developer Resources, "Releases," current Moodle release support calendar: https://moodledev.io/general/releases  
[M2] Moodle Developer Resources, "Moodle 5.0," server requirements and release notes: https://moodledev.io/general/releases/5.0  
[M3] Moodle Docs, "H5P activity," Content bank and H5P attempts/completion behavior: https://docs.moodle.org/500/en/H5P_activity  
[M4] Moodle Docs / Developer Resources, "Data privacy" and "Privacy API," retention registry and plugin privacy requirements: https://docs.moodle.org/400/en/Data_privacy and https://moodledev.io/docs/4.5/apis/subsystems/privacy  
[M5] Moodle Docs, "Automated course backup," cron and backup limitations: https://docs.moodle.org/400/en/Automated_course_backup  
[M6] H5P, "Content types recommendations," accessibility and maintenance status by H5P content type: https://help.h5p.com/hc/en-us/articles/7505649072797-Content-types-recommendations  
[M7] Moodle Docs, "Moodle app guide for admins," "Moodle app offline features," and "Moodle app notifications": https://docs.moodle.org/500/en/Moodle_app_guide_for_admins, https://docs.moodle.org/401/en/Moodle_app_offline_features, https://docs.moodle.org/400/en/Moodle_app_notifications  
[M8] Moodle, "Moodle LMS VPAT," accessibility conformance information: https://moodle.com/accessibility/lms-vpat/  
[M9] Moodle Docs, "Course completion settings" and "Restrict access settings": https://docs.moodle.org/500/en/Course_completion_settings and https://docs.moodle.org/500/en/Restrict_access_settings  
[M10] Moodle Docs, "Question banks," question organization, status, versioning, and quiz use: https://docs.moodle.org/500/en/Question_banks  

### Plugin Sources

[P1] Moodle Docs / Moodle Plugins / GitHub, Custom certificate (`mod_customcert`), dynamic PDF certificates and verification codes: https://docs.moodle.org/500/en/Custom_certificate_module and https://github.com/mdjnelson/moodle-mod_customcert  
[P2] Moodle Plugins, Timestat (`block_timestat`), active browser/tab time and inactivity pause: https://moodle.org/plugins/block_timestat  
[P3] GitHub, Dedication block (`block_dedication`), estimated time-spent reports from logs: https://github.com/catalyst/moodle-block_dedication  
[P4] Moodle Plugins / GitHub, Scheduler (`mod_scheduler`), appointment slots and outcomes: https://moodle.org/plugins/mod_scheduler and https://github.com/bostelm/moodle-mod_scheduler  
[P5] Moodle Docs, "Custom SQL queries report" (`report_customsql`), admin-defined SQL reports and CSV downloads: https://docs.moodle.org/500/en/Custom_SQL_queries_report  
[P6] Open LMS Support, "Configurable Reports Plugin Support," support phase-out and compatibility/security caution: https://support.openlms.net/hc/en-us/articles/15975709248028-Configurable-Reports-Plugin-Support  

### Compliance and Privacy Sources From Phase 0

[C1] HHS OCR, "Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the HIPAA Privacy Rule": https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html  
[C2] HHS OCR, "Guidance on HIPAA & Cloud Computing": https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html  
[C3] California Health and Safety Code section 1337.6, CNA renewal and online computer training requirements: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1337.6  
[C4] CDPH 192B, online continuing education provider application and controls: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph192b.pdf  
[C5] CDPH 192, continuing education provider application and certificate/record expectations: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph192.pdf  
[C6] CDPH 283A and 283C, CNA/HHA CE documentation and renewal application: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph283a.pdf and https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph283c.pdf  

---

## Dependencies / Items for Final Reconciliation

1. CDPH/legal review must confirm CI Institute's online CE provider status, NAC#, approved course list, approved certificate wording, and whether course certificates must be issued per one-hour course or as a bundled certificate.
2. CDPH/legal review must confirm whether electronic signatures satisfy the final signed statement/affidavit requirement; otherwise the architecture needs a wet-signature release path.
3. CDPH/legal review must confirm that optional clinical support, preceptor signoff, lab practice, simulation, virtual simulation, and LTI simulation are not being counted as California renewal clinical hours unless written approval is obtained.
4. Final instructional design must map every required Moodle unit, interaction, quiz, and exam item to approved course objectives and approved CE hour values without changing Phase 0 findings.
5. Operations must validate the selected Moodle version, plugins, mobile behavior, active-time reports, certificate gates, privacy controls, backups, restores, and audit exports in staging before production.
6. Compliance, operations, and instructional design must reconcile learner-facing language across Moodle, certificates, marketing, handbook copy, and support materials so the 12-hour online theory course is presented as partial renewal credit only and the optional clinical hub is not presented as a state-required renewal component.
