# Final Unified Implementation Blueprint

**Project:** California CNA Recertification Course in Self-Hosted Moodle  
**Prepared for:** CI Institute of Nursing  
**Purpose:** Reconciled implementation-ready blueprint across compliance, Moodle architecture, instructional design, clinical support, migration, operations, QA, and launch  
**Controlling compliance source:** `PHASE_0_COMPLIANCE_FOUNDATION.md`  
**Status:** Final reconciliation blueprint; not legal advice  
**Date:** May 25, 2026

---

## 1. Executive Summary

The strongest build is a **12-hour asynchronous Moodle theory course** plus a **meaningfully integrated 12-hour clinical practice support pathway**, with a strict compliance boundary: the Moodle theory course may issue California CNA online CE credit only if CI Institute of Nursing and the exact courses are CDPH-approved online CE, and the learner remains within California's 24-hour online CE cap. The clinical pathway remains integrated in Moodle as scheduling support, skills refresh, optional confidence checks, resource hub, documentation support, and staff review support, but it is **not represented as required California CNA renewal clinical hours** unless CDPH gives written approval for that exact use.

The reconciled MVP should be conservative and buildable: self-hosted Moodle, Moodle-native content cloned from approved source materials, no new video production, optional approved cloned-voice TTS only with authorization and transcripts, short mobile-first lessons, meaningful interaction/feedback, active-time control, exam/test, final signed statement/affidavit, locked certificate fields, audit packet exports, and privacy controls that prevent PHI collection.

The main corrections to the phase reports are:

| Issue Reconciled | Final Decision |
|---|---|
| Clinical support vs. clinical credit | Preserve a 12-hour clinical practice support pathway, but do not count it as California renewal clinical hours or gate the online CE certificate unless CDPH approves it in writing. |
| Time tracking | Moodle logs alone are not enough. Use validated active-time control plus activity completion, interaction, exam/test, affidavit, certificate logs, and audit exports. |
| Plugin certainty | Treat plugins as candidates until version compatibility, mobile behavior, privacy API support, reporting, and maintenance are validated in staging. |
| Certificate release | Release the online CE certificate only after required theory compliance gates pass; optional clinical support stays outside the certificate gate by default. |
| MVP media scope | No new video production. Use Moodle-native text, lessons, quizzes, job aids, authorized TTS with transcripts, and simple interactions. |
| Simulation | Text scenarios may support learning/interaction, but simulation, virtual simulation, and LTI simulation do not count toward clinical hours without written CDPH approval. |

---

## 2. Verified Compliance Foundation

| Compliance Item | Verified Finding | Implementation Rule | Source |
|---|---|---|---|
| California CNA renewal cycle | Certificates renew every two years. | Track course completion date and learner-facing renewal-period disclaimers. | HSC 1337.6; CDPH 283C; 22 CCR 71839. |
| Renewal hours | Renewal requires 48 hours of in-service training/CEUs within the certification period. | The 12-hour theory course is partial credit only. | HSC 1337.6; CDPH 283A/283C. |
| Annual minimum | At least 12 hours must be completed in each year of the two-year period. | Certificate must show completion date and CE hours. | HSC 1337.6; CDPH 283A/283C. |
| Online cap | Only 24 of 48 hours may be obtained through CDPH-approved online computer training. | Add online-hour cap attestation and certificate/learner disclaimer. | HSC 1337.6; CDPH Online CE Providers. |
| Provider/course approval | CE credit requires CDPH-approved provider/course with valid NAC# where applicable. | Block production certificate issuance until approval/NAC# and approved course list are documented. | CDPH 192B; CDPH 283A/283C. |
| Online course controls | Online CE requires identity confirmation, interaction/feedback, exam/test, time/pause control, final signed statement, and certificate fields. | Implement certificate gates and audit exports around these controls. | HSC 1337.6; CDPH 192B. |
| Active-time standard | CDPH 192B requires at least 50 minutes active participation per CE hour and prevents direct jump to exam/certificate. | Use validated active-time control; do not rely on login duration alone. | CDPH 192B. |
| Work/practice requirement | Renewal also requires compensated nursing/nursing-related services in a facility under licensed supervision during the certification period. | Course certificate cannot claim full renewal eligibility. | CDPH 283C. |
| Clinical renewal hours | No reviewed California renewal authority establishes a separate 12-hour renewal clinical-hour requirement. | Clinical practice is integrated support/documentation unless CDPH approves credit. | Phase 0 review of HSC 1337.6, CDPH 283A/283C, 22 CCR 71839. |
| Simulation | No reviewed source authorizes simulation/virtual simulation/LTI simulation as renewal clinical-hour credit. | Label only as support/interaction unless written CDPH approval exists. | Phase 0 simulation analysis. |
| Record retention | Provider/CNA completion records generally require four-year retention; online signed statement has three-year statutory retention. | Retain all certificate-supporting Moodle evidence at least four years unless counsel sets longer retention. | CDPH 192; CDPH 283A; HSC 1337.6. |
| Privacy | Clinical uploads can create PHI risk; de-identification and cloud/BAA issues may apply. | Avoid PHI entirely; use warnings, structured fields, quarantine/delete process. | HHS OCR HIPAA de-identification and cloud guidance. |

---

## 3. Open Compliance Questions

| Question | Default Until Resolved | Owner | Blocks MVP Certificate? |
|---|---|---|---|
| Is CI Institute of Nursing approved as a CDPH online CNA CE provider and what NAC# applies? | Do not issue California CNA online CE certificate. | Compliance Lead | Yes |
| Are the exact 12 hours, course titles, objectives, outlines, exams/tests, and hours approved by CDPH? | Build only in staging or as non-credit draft. | Program Director | Yes |
| Can the 12 hours issue one bundled certificate or must each approved course issue separately? | Configure certificate model to match written CDPH approval. | Compliance Lead/Registrar | Yes |
| Is electronic signature acceptable for the final signed statement/affidavit? | Use e-sign only after written approval; otherwise create wet-sign fallback. | Legal/Compliance | Yes |
| Can any clinical/lab/workplace/preceptor practice be counted as CDPH-approved CE/in-service credit? | Treat as support/documentation only. | Legal/Compliance | No for theory certificate; yes if clinical credit claimed |
| Does CI Institute have any direct ATCS/TULIP/CDPH reporting obligation? | Provide learner certificate and exportable records; do not promise direct reporting. | Operations/Compliance | No, but affects operations |
| What exact certificate language is approved? | Use draft template only; block issue until approved. | Registrar/Compliance | Yes |
| What privacy laws/contracts apply if PHI is uploaded? | Design to avoid PHI; quarantine suspected PHI. | Privacy Officer/Legal | No if PHI avoided |
| Is cloned-voice TTS authorized? | Do not generate/use cloned voice. | Program Owner/Legal | No; TTS is optional |

---

## 4. Learner Profile: Exhausted Working CNAs

| Learner Reality | Design Response | Moodle Implementation |
|---|---|---|
| Learners may study after long shifts. | Use short, resumable units with plain next steps. | Books/Lessons split into 10-20 minute sections; clear progress indicators. |
| Many learners will use phones. | Avoid dense PDFs, large tables, drag-heavy interactions, and required video. | Mobile-tested Moodle pages, quizzes, one-question screens, compressed files. |
| Learners need renewal clarity. | Repeat short, accurate compliance reminders at key points. | Orientation acknowledgement, certificate page disclaimer, support scripts. |
| Learners may feel surveilled by time tracking. | Explain time tracking as a CDPH online CE requirement, not a punishment. | Friendly labels: "Active participation progress." |
| Learners may be test-anxious. | Use practice checks, remediation, and retakes subject to approved policy. | Low-stakes quizzes before final exam/test. |
| Learners are experienced caregivers. | Use respectful scenarios that recognize practical work realities. | "During a busy shift..." cases with useful feedback. |
| Learners may avoid optional support if it feels risky. | Keep clinical hub helpful, non-punitive, and separate from certificate gates. | Optional labels, no grades, support-request path. |

---

## 5. Design Philosophy: Engagement Without Burden

The reconciled design should follow one principle: **every activity must create compliance evidence, improve safety judgment, reduce learner confusion, or provide useful support.** Anything else should be removed from MVP.

| Recommendation | Moodle Tool / Plugin / Process | Learner Experience | Admin / Instructor Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|
| Use short scenario-based learning instead of long passive content. | Book, Lesson, Quiz, H5P where accessible. | Practical decisions in small chunks. | Easier content review and updates. | Completion, attempts, responses. | Supports interaction/feedback. | Confirm each required unit has learner input and feedback. |
| Keep optional and required activities visually distinct. | Course labels, separate sections/categories, completion settings. | Learner knows what affects certificate. | Fewer support tickets. | Completion configuration record. | Prevents optional clinical support becoming a gate. | Complete theory while skipping clinical hub; certificate should still release if all theory gates pass. |
| Avoid busywork reflections. | Feedback only where useful. | Fewer forms after long shifts. | Less review burden. | Targeted reflection record if used. | Reduces admin load and PHI risk. | Review every reflection for purpose and PHI warning. |
| Use plain-language compliance copy. | Page, Quiz acknowledgement, certificate disclaimer. | Learner understands partial credit and online cap. | Consistent support messaging. | Acknowledgement timestamp. | Reduces misrepresentation risk. | Learner pilot asks: "Does this complete renewal?" Expected answer: no. |
| Preserve clinical support without making it punitive. | Optional Clinical Support Hub. | Helpful resources and planning tools. | Clinical coordinator monitors support only. | Support records, not certificate gates. | Keeps clinical integration without unsupported claim. | Verify optional hub is not in online CE completion criteria. |

---

## 6. Unified 12-Hour Theory Blueprint

The 12-hour theory course is built as partial California CNA online CE only. Final course names, objectives, hour groupings, exam rules, and certificate packaging must match CDPH-approved records.

| Module | Time | Core Topics | Moodle Tools | Learner Experience | Evidence Created | Compliance Value | Risks / Review Flags | QA Test |
|---|---:|---|---|---|---|---|---|---|
| 0. Orientation and Compliance Boundaries | 0.5 hr | Partial credit, 48-hour renewal, 12/year, 24 online cap, no PHI, course path. | Page + Quiz/Feedback acknowledgement. | Short start-here checklist. | Identity/profile attestation, online-cap attestation. | Prevents false renewal expectations. | Exact disclaimer needs legal review. | Learner cannot continue until acknowledgements complete. |
| 1. Infection Control | 1.5 hr | Standard precautions, hand hygiene, PPE, scenarios. | Book/Lesson + Quiz/H5P. | Practical shift-based infection decisions. | Completion, active time, interaction attempts, quiz. | Approved CE topic if mapped to course list. | H5P accessibility/mobile behavior. | Required interaction gives feedback and records completion. |
| 2. Resident Rights and Abuse Prevention | 2.0 hr | Rights, dignity, abuse/neglect/exploitation, reporting, boundaries. | Lesson + Quiz + job aid. | Clear reporting decision paths. | Quiz attempts, module completion. | Supports HSC 1337.1 abuse/resident-rights coverage. | Must map to approved hours and required content. | Failing quiz triggers remediation before retry. |
| 3. Dementia, Communication, Cultural Respect | 2.0 hr | Dementia/cognitive impairment, communication, trauma-informed/cultural sensitivity. | Lesson, scenario quiz, optional TTS transcript. | Choose-the-response scenarios. | Responses, feedback, completion. | Supports CMS facility in-service topics and best practice. | Trauma-informed language needs clinical review. | Mobile screen review and screen-reader smoke test. |
| 4. Mobility, Falls, Workplace Safety | 2.0 hr | Body mechanics, safe transfers, falls, workplace safety. | Book/Lesson + sequence quiz. | Refreshes safety without claiming competency validation. | Completion, quiz score. | Best-practice CNA skill refresh. | Do not imply hands-on competency. | Check language avoids "validated skill" claims. |
| 5. Nutrition, Skin Integrity, Vital Signs | 2.0 hr | Nutrition/hydration, skin risk, vital signs, observation. | Lesson + scenario quiz. | What to observe and when to report. | Scenario attempts and quiz. | Supports resident safety and CNA scope. | Scope boundaries need RN review. | Questions align to CNA scope. |
| 6. Documentation, Change-of-Condition, Scope | 1.5 hr | Objective documentation, reporting, PHI avoidance, scope/team communication. | Page/Lesson + Quiz. | Practice objective wording without PHI. | Quiz attempts, PHI acknowledgement. | Strengthens audit/privacy posture. | Avoid collecting real resident examples. | Free-text prompts prohibit PHI and are reviewed. |
| 7. Review, Final Exam/Test, Affidavit | 0.5 hr | Mixed review, final exam/test, final signed statement. | Practice quiz + final Quiz + affidavit form. | Clear "test, sign, certificate" path. | Exam attempt/score, affidavit, certificate issue record. | Required for online CE certificate release. | E-signature acceptance unresolved. | Certificate unavailable until exam pass and affidavit complete. |

**Reconciled time model:** Each approved CE hour must include at least 50 active minutes. The course should be structured so total required activity time supports 12 CE hours without padding. Active time is a compliance control, not the only learning evidence.

---

## 7. Unified 12-Hour Clinical LMS Support Blueprint

The program preserves a **12-hour clinical practice pathway** as a meaningful Moodle-integrated support experience. It is not represented as a California renewal clinical-hour requirement unless CDPH approves it in writing. The pathway is designed to help learners plan, refresh skills, document optional practice, and get support without making tired CNAs feel punished.

| Clinical Component | Time Target | Moodle Tool / Process | Learner Experience | Admin / RN / Preceptor Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---:|---|---|---|---|---|---|---|
| Clinical orientation | 0.5 hr | Page/Book with acknowledgement. | Understands support purpose and non-credit boundary. | Maintains approved wording. | View/acknowledgement log. | Prevents unsupported clinical-credit claims. | Learner may still misunderstand. | Pilot learner explains clinical hub status correctly. |
| Skills refresh menu | 2.0 hr | Book/Page/File job aids. | Quick refresh by skill area. | Clinical educator reviews accuracy. | Access logs, optional completion. | Supports learning without clinical credit claim. | Content could imply competency validation. | Review wording for "practice/support" labels. |
| Scheduling guidance | 1.0 hr | Calendar, Choice, Page; Scheduler only if validated. | Clear options for lab/workplace/preceptor practice. | Staff manage capacity manually or by Scheduler. | Booking/preference records. | Operational support. | Plugin mobile issues or overpromised slots. | Book/cancel flow on phone. |
| Optional confidence checks | 2.0 hr | Ungraded Quiz/Feedback/H5P. | Learner self-identifies weak areas. | Staff can see support trends, not grades. | Attempts and support needs. | Engagement/support evidence only. | Learner perceives it as graded. | Certificate releases even if confidence checks skipped. |
| Practice documentation | 3.0 hr | Structured Assignment/Database; no free PHI narrative. | Uploads minimal non-PHI evidence if requested. | Admin reviews completeness and rejects PHI/incomplete uploads. | Timestamped submission, feedback, resubmission. | Optional support documentation. | PHI upload, admin burden. | PHI warning appears before every upload. |
| RN/preceptor support signoff | 2.0 hr | Downloadable form + upload or structured form. | Simple signoff path where applicable. | RN/preceptor confirms name/title/date/contact/signature only. | Signoff artifact and review log. | Useful if later approved or for internal support. | Unverifiable signoff or false credit implication. | Verify required fields and role permissions. |
| Support follow-up | 1.5 hr | Feedback form, message, office hours. | Learner asks for help without penalty. | Clinical coordinator triages. | Support ticket/message log. | Reduces learner frustration. | Unstaffed support queue. | SLA test with sample support request. |

**Final rule:** clinical support may appear in the learner dashboard and progress view, but it must be marked as **support pathway** or **practice pathway**, not as a required California renewal certificate condition. If leadership wants a program-level "clinical practice completion" acknowledgment, it must be separate from the CDPH online CE certificate and legally reviewed before use.

---

## 8. Moodle Technical Architecture

| Architecture Decision | Moodle Tool / Plugin / Process | Learner Experience | Admin / Instructor Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|
| Use supported Moodle LTS for MVP. | Moodle 4.5 LTS preferred unless newer branch passes staging. | Stable UI and fewer plugin surprises. | Easier maintenance. | Version register. | Security and plugin stability. | Verify Moodle version support and plugin compatibility. |
| Maintain dev, staging, production. | Separate Moodle instances/environments. | Fewer live disruptions. | Safer testing and rollback. | Deployment logs. | Change-control evidence. | Restore staging from production-like masked copy. |
| Separate theory CE and clinical support. | Separate course sections or separate linked courses/categories. | Clear required vs. support navigation. | Easier permissions and reports. | Course/category configuration. | Prevents clinical-credit confusion. | Clinical support not included in certificate completion criteria. |
| Use Moodle-native content first. | Book, Page, Lesson, Quiz, Feedback, Assignment, Database, Forum, Calendar. | Fast, low-bandwidth, mobile-friendly. | Easier edits and versioning. | Completion, logs, attempts. | Stronger audit than static files. | Test each activity on mobile browser. |
| Use completion and restrict access. | Course completion, activity completion, Restrict access. | Clear step-by-step progression. | Configurable gate model. | Completion reports. | Prevents bypass. | Negative tests for skipped module/exam. |
| Use validated active-time control. | Candidate plugin/custom component plus Moodle logs. | Visible active participation progress. | Exportable time report. | Active-time report and settings. | Required CDPH time/pause evidence. | Try idle tab, multiple tabs, app/offline, premature exam access. |
| Use locked certificate tool. | Custom certificate candidate or equivalent. | Certificate appears after gates. | Registrar controls template and issue records. | Certificate PDF, issue log, code. | Required certificate evidence. | Missing field and premature issue tests. |
| Use limited admin reporting. | Core reports + Report builder/custom SQL if validated. | No direct learner impact. | Faster audit packets. | CSV/PDF exports. | Audit readiness. | Produce full packet for test learner. |
| Configure privacy and security. | Roles, capabilities, data privacy registry, TLS, backups, cron, security checks. | Trustworthy system. | Controlled access and recovery. | Role matrix, backup logs. | Protects records. | Learner cannot see other learner data. |

---

## 9. Plugin and Feature Matrix

| Need | Final MVP Decision | Tool / Plugin Candidate | Verification Required | Learner Experience | Admin Experience | Evidence Created | Risk | QA Test |
|---|---|---|---|---|---|---|---|---|
| Certificates | Use certificate plugin if compatible. | Custom certificate (`mod_customcert`) or equivalent. | Moodle version, field mapping, verification privacy, exports. | Instant certificate after gates. | Locked templates and issue logs. | Certificate PDF, issue record, code. | Missing fields or privacy leak. | Generate certificate with every required field and masked verification. |
| Active time | Required; plugin/custom must be validated. | Timestat preferred candidate; Dedication only corroborative unless validated for active-time control; custom hold if needed. | Idle exclusion, app/browser behavior, exportability, gate integration. | Progress visible, not confusing. | Time reports usable for audit. | Active-time logs/reports. | Inaccurate time or easy bypass. | Idle for 10 minutes; time should pause or not count. |
| H5P | Use selectively for accessible text interactions. | Core H5P. | Content-type accessibility, mobile usability, tracking. | Short practice interactions. | Content bank management. | Attempt/completion reports. | Drag/drop/mobile accessibility issues. | Complete H5P on phone and screen-reader smoke path. |
| Scheduling | Start with core Calendar/Choice; Scheduler only after validation. | Scheduler plugin optional. | Plugin release cadence, mobile booking, privacy. | Easy appointment/preferences. | Capacity management. | Booking records. | Overhead and plugin risk. | Book/cancel slot on phone. |
| Clinical checklists | Use core Page/Database/Assignment for MVP. | Checklist plugin post-MVP only if needed. | Compatibility and privacy. | Simple optional to-do. | Less plugin burden. | Optional support records. | Optional tasks look required. | Checklist not part of certificate condition. |
| Reports | Use core exports first; add custom SQL for admin only if needed. | Report builder, Custom SQL report. | Least privilege and SQL safety. | None. | Faster audit packet. | CSV exports. | Sensitive data exposure. | Non-admin cannot access SQL reports. |
| Configurable Reports | Avoid for new MVP. | None. | N/A. | N/A. | Avoids phase-out/support risk. | N/A. | Unsupported plugin. | N/A. |
| Accessibility checker | Manual QA in MVP; plugin/tool post-MVP. | Brickfield/external checker later. | License, privacy, value. | Better accessible course. | Remediation workflow. | Accessibility findings. | False sense of compliance. | Human QA remains required. |
| LTI simulation | Exclude from MVP credit logic. | External tool only in elite/support build. | Written CDPH approval for any credit claim. | Optional practice only. | Additional vendor/privacy burden. | Practice logs only. | Clinical-credit misclaim. | Simulation completion never appears as clinical-hour credit. |
| SMS reminders | Post-MVP. | SMS gateway/custom. | Consent, opt-out, privacy, cost. | Helpful nudges. | More support automation. | Message logs. | Privacy/cost. | Consent and opt-out test. |

---

## 10. Time Tracking, Completion, and Audit Evidence Model

Time tracking is necessary but insufficient. The final evidence model uses layered proof.

| Evidence Layer | Moodle Tool / Process | Learner Experience | Admin / Instructor Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|
| Identity | Login, profile fields, acknowledgement. | Confirms legal name/CNA number. | Registrar reviews corrections. | Profile export, attestation. | Required identity confirmation. | Wrong or shared account. | Try certificate with missing CNA number. |
| Approved content completion | Book/Page/Lesson completion. | Sees checked-off required steps. | Completion report. | Activity completion log. | Shows content path completed. | View-only completion is weak. | Completion requires meaningful activity where possible. |
| Interaction/feedback | Lesson questions, Quiz, H5P, Feedback. | Receives practical feedback. | Attempts visible. | Attempt/response records. | Required online CE interactivity. | Token clicks. | Each module has input and feedback. |
| Active participation | Validated time plugin/custom hold. | Active minutes tracked transparently. | Exported active-time report. | Active-time report/settings. | CDPH 50-minute-per-hour support. | Plugin inaccuracy. | Idle/multi-tab/offline negative tests. |
| Assessment | Module quizzes and final exam/test. | Practice, remediate, final test. | Quiz reports and gradebook. | Attempts, scores, timestamps. | Required exam/test evidence. | Bad questions/retake rules. | Failed final blocks certificate. |
| Affidavit | Final signed statement workflow. | Signs before certificate. | Registrar exports statement. | Signed statement record. | Required before certificate issuance. | E-sign not accepted. | Certificate blocked without affidavit. |
| Certificate | Locked certificate activity. | Downloads certificate after gates. | Issue/revoke report. | PDF, issue log, code. | Required completion proof. | Premature/incorrect issue. | All negative gate tests pass. |
| Overrides | Restricted exception form/log. | Rare; not visible unless affected. | Approval required. | Override log. | Audit integrity. | Abuse or missing log. | Override requires approver/reason/date. |
| Audit packet | Core reports + custom export process. | None unless requested. | Admin can reproduce evidence. | Packet of CSV/PDF/screenshots. | CDPH/internal review. | Manual burden. | Produce packet for sample learner in under defined SLA. |

**Weak point resolved:** active-time plugins can be imperfect. The final design requires plugin validation, documented settings, raw Moodle logs as corroboration, and certificate release tests that prove learners cannot jump directly to the exam/certificate.

---

## 11. Certificate Release Model

The online CE certificate is for the **approved online theory CE pathway only**. It does not include clinical hours unless written CDPH approval authorizes exact certificate language and clinical evidence rules.

### Required Release Gates

| Gate | Moodle Tool / Process | Learner Experience | Admin Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|
| Provider/course approval active | Manual approval metadata / admin hold. | Certificate unavailable until course is approved. | Compliance lead enters approval/NAC# metadata. | Approval archive and course version. | Prevents unapproved credit. | Staff forget to block certificate. | Certificate hidden when approval status is pending. |
| Legal name and CNA number | Required profile fields. | Corrects profile before certificate. | Registrar can review changes. | Profile export. | Required certificate fields. | Incorrect identity. | Blank/mismatched fields block certificate. |
| Online cap acknowledgement | Quiz/Feedback attestation. | Acknowledges 24-hour cap. | Exportable attestation. | Timestamped acknowledgement. | Reduces learner over-credit risk. | Learner ignores meaning. | Attestation missing blocks certificate. |
| Required theory completion | Completion tracking. | Clear progress. | Completion report. | Completion logs. | Required content evidence. | Misconfigured optional activities. | Skip required activity; certificate locked. |
| Active-time threshold | Validated time control + hold. | Sees active-time status. | Admin can export time report. | Active-time report. | Required time/pause evidence. | Time plugin failure. | Premature exam/certificate attempt fails. |
| Interaction/feedback complete | Lesson/H5P/Quiz completion. | Receives feedback. | Attempts available. | Interaction records. | Required online CE interaction. | Token activity. | Interaction skipped; final exam locked. |
| Final exam/test pass | Quiz with grade-to-pass. | Pass or remediate. | Quiz reports. | Attempt, score, timestamp. | Required assessment. | Bad pass logic. | Failed score blocks certificate. |
| Signed statement/affidavit | Approved e-sign/wet-sign workflow. | Signs final statement. | Registrar exports record. | Signed statement. | Required before certificate issuance. | E-sign unresolved. | Missing affidavit blocks certificate. |
| Admin hold clear | Manual restricted field/process. | Support resolves issue. | Registrar/compliance controls release. | Hold/clearance log. | Prevents known bad issue. | Invisible learner frustration. | Admin hold blocks certificate despite other gates. |

### Certificate Fields

| Field | Status | Final Rule |
|---|---|---|
| Provider/program name, address, contact/telephone | Required | Locked template from approved provider profile. |
| Learner legal name and CNA certificate number | Required | Pull from verified profile fields. |
| Course name, completion date, CE hours | Required | Match approved course list exactly. |
| NAC#/CE provider ID | Required if applicable | Do not issue until active approval documented. |
| Online course indicator | Required/conditional | Use exact approved language. |
| Retention statement | Required | Use exact CDPH-approved four-year retention language. |
| Certificate ID/code | Recommended | Include immutable ID for audit. |
| QR/verification link | Post-MVP recommended | Use only if privacy-limited. |
| Clinical hours | Not included by default | Include only with written CDPH approval and separate rule set. |
| Partial-credit disclaimer | Recommended/required by policy | State course is partial credit and subject to 24-hour online cap. |

---

## 12. Mobile UX and Accessibility Strategy

| Strategy | Moodle Tool / Process | Learner Experience | Admin / Instructor Experience | Evidence Created | Compliance / Quality Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|
| Phone-first layout | Boost/minimal theme; short sections. | One clear next step. | Less design complexity. | UX QA checklist. | Reduces dropout. | Theme plugin incompatibility. | Complete path on iPhone/Android browser. |
| Low-bandwidth content | Book/Page/Lesson; no required video. | Text loads quickly; audio optional. | Easier updates. | Content version logs. | MVP resilience. | Dense pages. | 3G/low-bandwidth smoke test. |
| Accessible audio/TTS | Optional audio + transcript. | Can read or listen. | Script/version control. | Transcript files, audio logs. | Accessibility and learner support. | Unauthorized voice clone. | Every audio item has adjacent transcript. |
| Simple quizzes | One question or small groups per screen. | Less fatigue. | Easier item QA. | Quiz attempt logs. | Better completion. | Too many quizzes. | Pilot fatigue review. |
| Avoid wide tables in learner content | Convert to cards/lists. | Easier phone reading. | More content formatting work. | UX review notes. | Accessibility. | Loss of detail. | Zoom/text reflow test. |
| Accessible interactions | Use tested H5P/Lesson types. | Touch-friendly practice. | Content-type restrictions. | Interaction QA log. | WCAG-aligned experience. | Drag/drop inaccessible. | Keyboard and screen-reader smoke test. |
| Clear progress | Completion checkboxes/progress block if validated. | Knows what remains. | Fewer support tickets. | Completion report. | Reduces confusion. | Optional items skew progress. | Optional hub does not appear as required progress. |

---

## 13. Clinical Resource Hub Design

The Clinical Resource Hub is the Moodle home for the 12-hour clinical practice support pathway. It should feel like a practical toolkit, not a compliance trap.

| Hub Area | Moodle Tool | Learner Experience | Admin / Clinical Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|
| Start Here | Page/Book. | "What this is / what this is not." | Compliance-approved copy. | Acknowledgement log if used. | Prevents unsupported claims. | Overly legalistic copy. | Learner can summarize optional status. |
| Practice Planner | Page + Calendar/Choice. | Plans lab/workplace/preceptor time. | Staff update schedule/capacity. | Booking/preference records. | Operational support. | Stale dates. | Dates/contact info review before launch. |
| Skills Refresh Library | Book/File. | Quick refresh by skill. | RN educator maintains. | Access logs. | Supports safe practice. | Content outdated. | RN review signoff. |
| Confidence Checks | Ungraded Quiz/Feedback. | Private self-checks with resource links. | Optional trend review. | Non-grade attempts. | Learner support. | Feels punitive. | Check labels: not graded, not clinical credit. |
| Documentation Support | Assignment/Database. | Minimal non-PHI uploads if needed. | Admin review, reject/resubmit. | Upload, feedback, resubmission. | Audit/support documentation. | PHI/admin burden. | PHI warning visible and required. |
| Preceptor/RN Instructions | Page + downloadable form. | Easy instructions to share. | Standard fields collected. | Signoff artifact if used. | Supports verification if later needed. | Unverified credentials. | Form captures name/title/contact/date/signature. |
| Help and Office Hours | Feedback/form/Calendar. | Gets help without penalty. | Staff triage. | Support log. | Reduces frustration. | Unstaffed requests. | SLA test. |

---

## 14. Instructor, Preceptor, RN Evaluator, and Admin Workflows

| Role | Workflow | Moodle Tool / Process | Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|
| Instructor / ID Lead | Maintain approved theory content and feedback. | Book/Lesson/Quiz question bank; version log. | Reviews course without touching certificate settings. | Content version, question tags. | Approved content traceability. | Unapproved edits. | Instructor cannot alter certificate gate/template. |
| RN Clinical Educator | Review clinical support resources and scope language. | Clinical hub pages, job aids, checklist review. | Ensures safe practice language. | Review signoff. | Clinical accuracy. | Claims competency validation. | Review all skill resources for support-only language. |
| Preceptor/RN Evaluator | Optional signoff where used. | Downloadable form/upload or structured form. | Minimal fields, no patient data. | Signoff artifact. | Support documentation. | Credential unverifiable. | Required fields present and access limited. |
| Admin Reviewer | Review optional clinical uploads and exceptions. | Assignment/Database feedback. | Accept/reject with standard reasons. | Review decision log. | PHI prevention and documentation quality. | Too much manual work. | Batch review workflow timed. |
| Registrar | Manage profile fields and certificate release records. | User fields, certificate reports. | Reviews identity/certificate issues. | Profile exports, issue logs. | Certificate accuracy. | Wrong certificate field. | Sample certificate field audit. |
| Moodle Admin | Configure gates, plugins, reports, backups, roles. | Site/course settings, reports, cron. | Maintains system integrity. | Config register, backup logs. | Audit and security. | Over-broad admin changes. | Regression after every settings change. |
| Compliance Lead | Own approval records and unresolved questions. | Restricted archive, decision log, admin hold. | Can block issuance. | Approval/decision log. | Prevents unsupported claims. | Delayed decisions. | Certificate disabled when approval metadata missing. |
| Support Lead | Help learners through access/completion issues. | Help form, messaging, templates. | Clear scripts and escalation. | Support log. | Reduces learner burden. | Gives incorrect compliance advice. | Support script review. |

---

## 15. Support and Communication Model

| Support Need | Moodle Tool / Process | Learner Experience | Staff Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|
| Welcome and expectations | Announcement + Orientation page. | Knows path and partial-credit boundary. | Standardized messaging. | Announcement log. | Reduces misrepresentation. | Too much text. | Pilot learner understands path. |
| "I am stuck" help | Feedback form/help link on every major page. | One place to ask. | Routed triage. | Support ticket/log. | Prevents abandonment. | Understaffed queue. | Test ticket and response SLA. |
| Completion nudges | Completion report + targeted messages. | Helpful reminders. | Weekly report run. | Message log. | Reduces missed gates. | Notification fatigue. | Message cadence review. |
| Failed exam support | Quiz feedback + remediation links. | Knows what to review. | Instructor monitors attempts. | Quiz/remediation records. | Supports mastery. | Exposes answer key. | Final feedback does not reveal full key if policy prohibits. |
| Certificate issue support | Certificate status page + registrar contact. | Knows missing gate. | Registrar resolves field issues. | Support/correction log. | Prevents incorrect certificates. | Learner frustration. | Missing field message is clear. |
| Clinical support help | Clinical hub support form. | Can ask without penalty. | Clinical coordinator triages. | Support log. | Keeps clinical support helpful. | Looks required. | Help copy says optional support. |
| Privacy incident support | PHI report/escalation process. | Learner gets safe resubmission instructions. | Privacy Officer handles. | Incident log. | Privacy protection. | Mishandled PHI. | Simulated PHI upload workflow. |

---

## 16. Custom Moodle Component Opportunities

| Component | MVP / Elite | Purpose | Learner Experience | Admin Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|---|
| Compliance status widget | MVP if feasible; otherwise post-MVP. | Shows missing gates. | One clear checklist. | Fewer support questions. | Status snapshots. | Prevents premature certificate confusion. | Widget matches actual completion rules. |
| Active-time compliance hold | MVP if plugin cannot gate natively. | Converts validated time into certificate condition. | Clear "time met/not met." | Reliable release control. | Time hold log. | High. | Time below threshold blocks exam/certificate. |
| Audit packet generator | Post-MVP unless manual burden is high. | One-click evidence packet. | None. | Saves audit time. | PDF/CSV bundle. | High. | Packet matches manual audit checklist. |
| Certificate verification portal | Elite. | Employer/verifier checks validity. | Optional QR/code confidence. | Verification logs. | Fraud reduction. | Privacy leak. | Public page shows minimal data only. |
| Clinical support tracker | Elite. | Better optional practice status. | Simple support progress. | Clinical coordinator dashboard. | Support records. | Medium if optional. | Tracker never gates online CE certificate. |
| SMS reminders | Elite. | Nudges exhausted learners. | Helpful texts with consent. | More automation. | Message logs. | Privacy/consent/cost. | Opt-in/opt-out test. |
| LTI/virtual simulation | Elite only with approval. | Rich practice. | Optional practice. | Vendor/admin burden. | Practice logs. | None for clinical hours unless CDPH approves. | Completion not counted as clinical hours. |

---

## 17. Legacy Content Migration Strategy

| Migration Step | Tool / Process | Learner Experience | Admin / Instructor Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|
| Inventory all assets. | Asset workbook/restricted archive. | N/A. | Knows what is approved/current. | Asset inventory. | Prevents unapproved content. | Missing source/version. | Every module maps to source asset. |
| Separate approved from useful but unapproved content. | Compliance review labels. | Only approved content goes live for credit. | Clear build boundaries. | Approval status log. | Reduces compliance drift. | Useful content sneaks in. | Unapproved items blocked from production course. |
| Convert to Moodle-native. | Book/Page/Lesson/Quiz. | Better mobile experience. | Easier revisions. | Content version log. | Stronger completion evidence. | Meaning changes during rewrite. | Side-by-side content review. |
| Build question bank. | Moodle Question bank categories/tags. | Fair aligned quizzes. | Easier exam maintenance. | Tagged items, version. | Exam/test traceability. | Wrong answers/outdated questions. | RN/compliance item review. |
| Archive originals. | Restricted folder/repository. | N/A. | Source retained. | Archive log. | Audit support. | Overexposure of admin files. | Permission test. |
| Freeze MVP version. | Release notes/course backup. | Stable course. | Controlled changes. | Version ID and backup. | Audit reproducibility. | Live edits break gates. | Regression after freeze. |

---

## 18. MVP No-New-Video / Approved TTS Build Plan

| Build Item | MVP Decision | Moodle Tool / Process | Learner Experience | Admin / Instructor Experience | Evidence Created | Compliance Value | Risk | QA Test |
|---|---|---|---|---|---|---|---|---|
| New videos | Excluded. | N/A. | No streaming dependency. | Faster launch. | Scope decision log. | Avoids schedule/accessibility risk. | Less rich demonstration. | Confirm no required path depends on new video. |
| Existing approved videos | Use only if already approved, captioned, transcripted, and mobile-tested. | Page/Book embed. | Optional enhancement. | Maintains media assets. | Approval/caption record. | Accessible if compliant. | Outdated content. | Video not required for completion unless approved. |
| Approved text | Core MVP. | Book/Page/Lesson. | Readable chunks. | Easy updates. | Completion/version logs. | Strong content control. | Text too dense. | Mobile readability review. |
| Approved cloned-voice TTS | Conditional optional. | Audio file embedded with transcript. | Listen or read. | Script/voice authorization management. | Authorization log, transcript. | Accessibility support if authorized. | Voice/IP/consent risk. | No audio without transcript and authorization. |
| Interactions | Required. | Lesson questions, Quiz, H5P. | Short decision checks. | Attempt reports. | Interaction evidence. | Required online CE feedback. | Token interactions. | Feedback is meaningful and tracked. |
| Job aids | Included. | File/Page printable. | Practical quick reference. | Easy to update. | File version. | Supportive. | Inaccessible PDFs. | PDF/text accessibility check. |

---

## 19. Quality Assurance and Testing Protocol

| QA Area | Test | Expected Result | Tool / Process | Evidence | Owner |
|---|---|---|---|---|---|
| Compliance gate | Learner skips required module. | Exam/certificate locked. | Test learner. | Screenshot/log. | QA Manager |
| Active time | Learner idles, changes tabs, tries early exam. | Idle time not counted; exam/certificate locked. | Time plugin/custom test. | Time report. | Moodle Admin |
| Interaction | Learner skips H5P/Lesson question. | Next gate locked. | Completion test. | Completion report. | QA Manager |
| Exam | Learner fails final exam. | Certificate unavailable; remediation shown. | Quiz test. | Quiz report. | Instructor/QA |
| Affidavit | Learner passes exam but does not sign. | Certificate unavailable. | Affidavit workflow. | Missing affidavit log. | Registrar |
| Certificate fields | Learner completes all gates. | Certificate fields match approved template. | Certificate test. | PDF and issue log. | Registrar |
| Optional clinical | Learner skips clinical hub. | Theory certificate still available after required theory gates. | Completion/certificate test. | Certificate issue log. | QA Manager |
| PHI warning | Learner opens upload form. | Warning appears before upload and no-PHI attestation required. | Assignment/Database test. | Screenshot. | Privacy Officer |
| PHI incident | Learner uploads test PHI. | Quarantine/reject workflow triggered. | Simulated upload. | Incident log. | Privacy Officer |
| Mobile | Learner completes core path on phone. | No blocker; next step obvious. | iOS/Android browser test. | UX findings. | UX Tester |
| Accessibility | Keyboard/screen-reader smoke test. | Core path usable. | Manual QA. | Accessibility log. | QA Manager |
| Roles | RN/preceptor accesses assigned item only. | No unrelated learner data. | Role test. | Access test log. | Moodle Admin |
| Reports | Admin exports audit packet. | Packet includes identity, time, interactions, exam, affidavit, certificate, version. | Export checklist. | Audit packet sample. | Compliance Lead |
| Backups | Restore test. | Staging restore successful. | Site/course backup. | Restore log. | IT/Security |
| Cron | Scheduled tasks run. | Completion/reports/certificates update. | Cron monitor. | Cron log. | Moodle Admin |

---

## 20. Compliance and Operational Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner | Review Flag |
|---|---:|---:|---|---|---|
| Course marketed as complete renewal | Medium | High | Required partial-credit disclaimers and marketing review. | Compliance/Marketing | Legal |
| Provider/course approval missing | Medium | High | Block certificate issuance until approval/NAC# documented. | Compliance Lead | CDPH |
| Learner exceeds 24 online hours | High | High | Attestation and certificate disclaimer. | Registrar | Compliance |
| Clinical support treated as required renewal clinical hours | Medium | High | Separate course/hub labels; no certificate gate by default. | Clinical Coordinator | CDPH/Legal |
| Simulation counted as clinical hours | Medium | High | Exclude from credit logic; disclaimer. | Program Owner | CDPH |
| Active-time control fails | Medium | High | Validate plugin/custom hold and use corroborating logs. | Moodle Admin | Technical |
| Certificate issued prematurely | Medium | High | Negative tests and admin hold. | Registrar | Compliance |
| Certificate missing fields | Medium | High | Locked template and field QA. | Registrar | CDPH |
| E-sign affidavit not accepted | Medium | High | Written approval or wet-sign fallback. | Legal/Compliance | CDPH/Legal |
| PHI uploaded | Medium | High | No-PHI design, warning, quarantine/delete. | Privacy Officer | Legal |
| Optional activities become busywork | Medium | Medium | Limit optional clinical checks and reflections. | ID Lead | Clinical Education |
| Admin review burden too high | Medium | Medium | Structured forms, batch reports, minimal uploads. | Operations Lead | Operational |
| H5P not accessible/mobile-friendly | Medium | Medium | Use tested content types and alternatives. | QA Manager | Accessibility |
| Plugin unsupported | Medium | Medium/High | Prefer core; keep plugin register and staging tests. | Moodle Admin | Technical |
| Logs not retained | Low/Medium | High | Four-year retention/export policy. | Operations/IT | Compliance |
| Support queue overwhelmed | Medium | Medium | Support scripts, SLA, pilot, pause enrollment if needed. | Support Lead | Operational |
| Legacy content outdated | Medium | High | Asset inventory and approval mapping. | Content Owner | Compliance |
| TTS authorization unclear | Medium | High | Written consent and script/version log before use. | Program Owner | Legal/IP |
| Mobile navigation confusing | Medium | Medium | Pilot with working CNAs and revise. | UX Tester | Learner Experience |
| Manual overrides abused | Low/Medium | High | Restricted roles, approval, monthly audit. | Compliance Lead | Operational |

---

## 21. MVP Version vs. Elite Version

| Area | MVP Version | Elite / Version Two |
|---|---|---|
| Moodle version | Supported LTS/stable branch, validated plugins. | Upgrade after staging and plugin validation. |
| Content | Approved content cloned into Moodle-native Books/Pages/Lessons. | Richer custom media and refreshed examples. |
| Video | No new video dependency. | New captioned/transcripted videos if approved and funded. |
| Audio/TTS | Approved cloned-voice TTS only if authorized and transcripted. | Larger audio library, multilingual support if approved. |
| Interactions | Simple text scenarios, quizzes, H5P where accessible. | Advanced branching and simulations. |
| Simulation | Not clinical credit. | Only if written CDPH approval supports intended use. |
| Clinical support | Optional 12-hour support/practice hub with resources, scheduling, confidence checks, minimal documentation. | Custom preceptor workflows, reminders, richer analytics. |
| Time tracking | Validated plugin/custom hold plus logs. | Custom compliance-grade active-time dashboard. |
| Certificate | Locked template, required gates, issue log. | QR/token verification portal. |
| Reports | Manual/core exports plus custom SQL if needed. | One-click audit packet generator. |
| Support | Email/forms/announcements/manual nudges. | SMS, chat, advanced knowledge base. |
| Accessibility | Human QA and mobile testing. | Formal accessibility tooling/third-party review. |

---

## 22. Phased Implementation Roadmap

| Phase | Duration | Key Work | Exit Criteria |
|---|---:|---|---|
| 1. Compliance Lock | 1-2 weeks | Confirm provider/NAC#, approved course list, certificate language, affidavit method, clinical boundary, TTS authorization. | Decision log complete; certificate blockers identified. |
| 2. Content Inventory and Approval Map | 1 week | Inventory source content, quizzes, policies, certificates, clinical materials. | Every MVP item labeled approved/revise/retire. |
| 3. Moodle Environment | 1-2 weeks | Dev/staging/prod, TLS, cron, backups, mail, roles, plugin register. | Staging works and restore test passes. |
| 4. MVP Course Build | 3-5 weeks | Convert theory content, build interactions, quizzes, active-time controls, affidavit, certificate. | Frozen staging build with all gates. |
| 5. Clinical Support Hub Build | 1-2 weeks parallel | Build optional 12-hour support pathway, resources, scheduling guidance, documentation controls. | Hub reviewed for optional/non-credit language and PHI prevention. |
| 6. QA/UAT | 1-2 weeks | Negative tests, mobile, accessibility, role, certificate, audit packet, backups. | Critical defects closed; sample audit packet accepted. |
| 7. Pilot | 2-4 weeks | Small learner cohort, support monitoring, completion evidence review. | Pilot report and go/no-go recommendation. |
| 8. Launch | 1 week | Production enrollment, monitoring, support coverage, rollback readiness. | Live course stable; certificate issues audited daily at first. |
| 9. Post-Launch Stabilization | 30-90 days | Fix bottlenecks, sample audits, support trend review, v2 backlog. | Version 1.1 release plan and elite backlog. |

---

## 23. First 30-Day Action Plan

| Day Range | Priority | Tasks | Output |
|---|---|---|---|
| Days 1-3 | Compliance blockers | Confirm approval/NAC#, certificate language, clinical disclaimer, e-sign question, online cap copy. | Compliance decision log v1. |
| Days 1-5 | Asset inventory | Collect source content, quizzes, policies, certificates, branding, clinical materials. | Asset inventory with approval status. |
| Days 4-7 | Moodle technical decision | Select Moodle branch, hosting, backup, certificate tool candidate, active-time candidate. | Technical stack decision memo. |
| Days 6-10 | Learner flow prototype | Build orientation, one theory module, one interaction, one quiz, one certificate gate mock. | Prototype in staging. |
| Days 8-14 | Content conversion sprint | Convert 3-4 hours approved content into Moodle-native modules. | Theory modules v0.1. |
| Days 10-15 | Certificate/affidavit prototype | Build locked certificate draft and final statement workflow. | Certificate test artifact. |
| Days 12-18 | Question bank | Tag/import/review module and final exam questions. | Question bank v0.1. |
| Days 15-20 | Clinical hub prototype | Build optional support hub, scheduling guidance, confidence check, upload warning. | Clinical hub v0.1. |
| Days 18-22 | Active-time validation | Test plugin/custom control, idle behavior, report exports. | Time-control validation log. |
| Days 20-25 | Audit packet dry run | Export all evidence for a test learner. | Sample audit packet. |
| Days 24-28 | QA script execution | Run negative tests and mobile/accessibility checks. | Defect log. |
| Days 29-30 | Pilot go/no-go | Review blockers, staffing, support scripts, rollback. | Pilot readiness decision. |

---

## 24. Launch Readiness Checklist

| Area | Go Criteria | Status |
|---|---|---|
| CDPH approval | Provider/course approval, NAC#, course list, certificate language documented or certificate disabled. | TBD |
| Compliance copy | Partial credit, 24-hour online cap, clinical support, simulation, and PHI disclaimers approved. | TBD |
| Theory course | 12-hour approved theory structure built, versioned, and tested. | TBD |
| Clinical support | 12-hour support pathway integrated, optional/non-credit language clear, no certificate gate by default. | TBD |
| Active time | 50-minute-per-hour control validated, exportable, and tested against idle/bypass cases. | TBD |
| Interaction | Required learner input and feedback included and tracked. | TBD |
| Exam/test | Final exam/test configured with approved pass/retake rules. | TBD |
| Affidavit | Final signed statement workflow approved and exportable. | TBD |
| Certificate | Required fields populate correctly; clinical hours excluded unless approved. | TBD |
| Audit packet | Sample packet includes identity, completion, time, interactions, exam, affidavit, certificate, version, overrides. | TBD |
| Privacy | No-PHI warnings, upload controls, incident workflow, least-privilege access tested. | TBD |
| Mobile UX | Core path tested on phones and low bandwidth. | TBD |
| Accessibility | Transcript, keyboard, screen-reader smoke, contrast, heading/link checks complete. | TBD |
| Roles | Learner, instructor, RN/preceptor, reviewer, registrar, support, admin permissions tested. | TBD |
| Backups/restore | Site backup, course snapshot, restore test, retention process complete. | TBD |
| Support | Help channels, scripts, SLA, escalation, staffing schedule ready. | TBD |
| Rollback | Certificate disablement, enrollment pause, content hotfix, PHI incident, and outage procedures documented. | TBD |

---

## 25. Final Implementation Checklist

### Compliance

- Confirm CDPH online CE provider status, NAC#, approved course list, approved hours, approved exam/test expectations, and approved certificate language.
- Confirm whether one 12-hour certificate is allowed or separate certificates are required.
- Confirm final signed statement/affidavit method.
- Confirm learner-facing disclaimers.
- Confirm clinical support cannot be marketed as California renewal clinical hours without written approval.

### Moodle Build

- Use supported Moodle release with dev/staging/production.
- Configure completion, Restrict access, gradebook, question bank, final quiz, affidavit, certificate, logs, reports, backups, and roles.
- Validate active-time control before production.
- Keep optional clinical support outside online CE certificate conditions.
- Maintain plugin register and rollback plan.

### Instructional Design

- Convert only approved source content into Moodle-native formats.
- Use short, respectful, scenario-based modules.
- Include meaningful interaction/feedback in each required unit.
- Pair authorized TTS with transcripts.
- Avoid new video and simulation dependencies in MVP.

### Clinical Support

- Build 12-hour clinical practice support hub with orientation, resources, scheduling guidance, confidence checks, documentation support, and help.
- Keep activities supportive, optional, non-punitive, and non-credit unless approved.
- Prohibit PHI in all uploads and reflections.
- Use minimal structured forms and clear rejection/resubmission flow.

### Operations and QA

- Run all negative certificate tests.
- Produce a complete sample audit packet.
- Test mobile, accessibility, roles, PHI workflow, cron, backups, and restore.
- Staff learner support before pilot.
- Freeze MVP version before pilot and control post-freeze changes.

---

## Source Register

- `PHASE_0_COMPLIANCE_FOUNDATION.md`, controlling compliance source for California CNA renewal, online CE, certificate fields, clinical support boundary, simulation warning, retention, and privacy.
- California Health and Safety Code section 1337.6: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1337.6
- CDPH Online Continuing Education Providers: https://www.cdph.ca.gov/Programs/CHCQ/LCP/Pages/Online-Continuing-Education-Providers.aspx
- CDPH 192B, Online Continuing Education Provider application: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph192b.pdf
- CDPH 192, Continuing Education Provider application: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph192.pdf
- CDPH 283A, CNA/HHA In-Service Training / CEUs: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph283a.pdf
- CDPH 283C, CNA/HHA Renewal Application: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph283c.pdf
- 22 CCR section 71839: https://www.law.cornell.edu/regulations/california/22-CCR-71839
- 42 CFR 483.95(g): https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-483/subpart-B/section-483.95
- HHS OCR HIPAA de-identification guidance: https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html
- HHS OCR HIPAA cloud computing guidance: https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html
- Moodle release information: https://moodledev.io/general/releases
- Moodle Docs, Course completion and Restrict access: https://docs.moodle.org/500/en/Course_completion_settings and https://docs.moodle.org/500/en/Restrict_access_settings
- Moodle Docs, H5P activity: https://docs.moodle.org/500/en/H5P_activity
- Moodle Docs, Moodle app guide and offline features: https://docs.moodle.org/500/en/Moodle_app_guide_for_admins and https://docs.moodle.org/401/en/Moodle_app_offline_features
- Moodle Docs, Site backup and Course backup: https://docs.moodle.org/405/en/Site_backup and https://docs.moodle.org/405/en/Course_backup
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
