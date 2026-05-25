# Phase 3: Instructional Design, Learner Engagement, Theory Blueprint, and Clinical Support Hub

**Project:** CI Institute of Nursing California CNA Recertification Course  
**Phase:** Phase 3 - Instructional Design  
**Prepared for:** CI Institute of Nursing  
**Status:** Instructional design report only; not legal advice; not final reconciliation  
**Controlling compliance source:** `PHASE_0_COMPLIANCE_FOUNDATION.md`  
**Last updated:** May 25, 2026

---

## 1. Executive Summary

This Phase 3 report designs the learning experience for a **12-hour asynchronous Moodle theory course** intended only as **partial California CNA renewal online continuing education credit**, subject to CDPH provider/course approval and the compliance controls identified in Phase 0. It does not redefine Phase 0 findings and does not claim that 12 online hours satisfy full California renewal. California CNA renewal requires 48 hours over two years, at least 12 hours each year, and no more than 24 hours through CDPH-approved online CE. [P0-S1] [P0-S2] [P0-S3] [P0-S4]

The recommended instructional model is mobile-first, respectful, scenario-based, and low burden. It avoids new video production as an MVP dependency and prioritizes cloned approved content, Moodle-native learning units, approved cloned-voice TTS only where authorized, transcripts, short checks, meaningful feedback, final exam/test controls, active-time evidence, identity confirmation, signed statement/affidavit, and audit-ready completion records. [P0-S1] [P0-S6]

The proposed clinical Moodle component is designed as an **optional Clinical Support Hub**, not a required California renewal clinical-hour pathway. It may support scheduling, skills refresh, confidence checks, resource access, non-PHI documentation support, and optional preceptor/RN signoff workflows, but it should not become a certificate gate unless CDPH/legal review requires it in writing. Simulation, virtual simulation, and LTI simulation must not be counted toward clinical hours without written CDPH approval. [P0-S3] [P0-S4] [P0-S6]

---

## 2. Scope Boundaries

| Area | Phase 3 Position |
|---|---|
| 12-hour asynchronous theory | In scope as a learner experience and instructional blueprint for partial online CE only. |
| Moodle infrastructure | Out of scope except high-level instructional dependencies such as activity completion, quiz flow, TTS/transcripts, and evidence needs. |
| Phase 4 migration/operations | Out of scope except dependencies that must be reconciled later. |
| Compliance interpretation | Phase 0 controls. This report applies them instructionally and does not replace them. |
| Clinical component | Optional learner support, skills refresh, scheduling/resource hub, and documentation support only unless CDPH gives written approval. |
| Certificate gating | Theory certificate gate may include required online CE controls. Optional clinical support must not be a gate unless compliance requires it. |
| Video production | Not an MVP dependency. Use text, Moodle-native formats, H5P-style interactions where approved, TTS if authorized, transcripts, job aids, and quizzes. |

---

## 3. Learner Profile: Exhausted Working CNAs

The primary learner is an experienced working CNA who may be completing renewal education after long shifts, on a smartphone, with limited time and limited patience for generic compliance modules. The design should respect what CNAs already know from real care settings while correcting unsafe habits, reinforcing resident safety, and making completion requirements clear.

| Learner Reality | Design Implication | Moodle / Content Response |
|---|---|---|
| Works full-time or multiple shifts. | Keep lessons short and resumable. | Use 15-30 minute units with visible progress and clear stopping points. |
| Often studies on a phone. | Avoid dense PDFs, wide tables, and tiny click targets as the main learning path. | Build mobile-friendly Pages, Books, Lessons, and quizzes with short screens. |
| May be tired after resident care work. | Reduce cognitive load and avoid long lectures. | Use one practical idea per screen, plain headings, and short checks. [L1] [L2] |
| May be skeptical of mandatory training. | Lead with why it matters to residents and CNAs. | Open units with realistic resident safety cases instead of abstract objectives. |
| Has real experience. | Avoid talking down to the learner. | Use respectful language: "You may have seen..." and "In practice..." |
| Needs renewal clarity. | Separate course completion from full state renewal eligibility. | Add learner-facing reminders about 48 hours, annual minimums, and 24-hour online cap. |
| May have anxiety about tests. | Use low-stakes practice before graded checks. | Include confidence checks, practice scenarios, remediation, and retakes. |
| May struggle with English-heavy materials. | Use plain language without removing professional vocabulary. | Define terms in context; provide audio and transcripts. [L3] [L4] |
| May not want surveillance. | Keep optional clinical support helpful and non-punitive. | Label confidence checks optional and do not gate certificates unless required. |
| May be concerned about privacy. | Avoid patient/resident identifiers in submissions. | Put PHI warnings at every upload/reflection point. [P0-S11] [P0-S12] |

---

## 4. Engagement Philosophy

The course should feel like practical renewal education for working caregivers, not a school-like hurdle. The engagement model should be direct, respectful, scenario-based, and focused on safety, confidence, and completion clarity.

| Weak Design | Better Design | Why It Works for CNAs |
|---|---|---|
| Long PDF followed by a quiz. | Short Moodle Book/Lesson sections with checks and feedback. | Learners can complete small pieces after shifts and remember key decisions. |
| Childish badges or games. | Progress milestones and practical feedback. | Respects adult learners and keeps motivation tied to resident safety. |
| Generic policy language. | "What would you do?" resident care scenarios. | Connects rules to real CNA judgment. |
| Seat time only. | Active time plus interactions, checks, exam/test, and affidavit. | Supports Phase 0 compliance controls and better learning. [P0-S6] |
| New custom videos for every topic. | Moodle-native content, approved TTS, transcripts, and job aids. | Faster MVP, easier updates, lower production risk. |
| Punitive clinical checklist. | Optional confidence check and refresh resources. | Helps learners prepare without implying unapproved clinical-hour credit. |
| Dense legal disclaimers buried at the end. | Short reminders at enrollment, certificate page, and clinical hub. | Reduces misunderstanding about partial credit and online-hour limits. |
| Complex navigation. | One clear path: learn, check, remediate, test, sign, certificate. | Reduces completion friction on mobile devices. |

Design principles:

1. Respect the CNA as an experienced caregiver.
2. Keep each activity tied to compliance, safety, confidence, clarity, or meaningful engagement.
3. Use realistic scenarios instead of decorative interactivity.
4. Make required and optional items visually distinct.
5. Keep the MVP maintainable and auditable.
6. Never imply that optional clinical support creates California renewal clinical credit without written CDPH approval.

---

## 5. Compliance-Aligned Instructional Assumptions

| Assumption | Instructional Design Impact | Review Flag |
|---|---|---|
| CI Institute of Nursing will seek or hold CDPH online CE provider approval and course approval. | Course titles, objectives, hours, quiz items, certificate fields, and completion rules must match approved records. | CDPH/legal review required. |
| The 12-hour theory course is partial online CE only. | Learner copy must say the course does not complete all California renewal requirements. | Required from Phase 0. |
| The learner may have taken other online CE elsewhere. | Add a learner attestation/reminder about the 24-hour online cap. | Compliance review recommended. |
| Clinical support is optional. | Do not make optional clinical support a certificate gate unless required in writing. | CDPH/legal review required before changing. |
| Approved TTS cloned voice may be used only if authorized and documented. | Add TTS as an optional accessibility/engagement layer, not required content. | Legal/IP/consent review required. |
| No patient/resident PHI should be collected. | Clinical reflections and uploads must use de-identified templates and warnings. | Privacy/legal review required. |
| E-signature for the final statement/affidavit must be acceptable. | Gate certificate behind the affidavit workflow only after compliance confirms exact method. | CDPH/legal review required. |

---

## 6. 12-Hour Theory Course Map

The proposed map breaks 12 hours into practical 15-30 minute units. Final CDPH approval may require different course titles, hour groupings, or one-hour course certificates; the map should be reconciled with approved course records before build.

| Module | Topic | Estimated Time | Learning Objective | Moodle Activity Type | Engagement Method | Assessment Method | Completion Rule | Compliance Notes |
|---|---|---:|---|---|---|---|---|---|
| 0 | Orientation, renewal boundaries, online-hour cap, privacy rules | 30 min | Explain what this course does and does not provide for California CNA renewal. | Page + acknowledgement quiz | Plain-language checklist | 5-item readiness check | View page, pass check, acknowledge disclaimers | State 48 hours/2 years, 12/year, 24-hour online cap; no PHI uploads. [P0-S1] [P0-S3] |
| 1A | Infection control foundations | 30 min | Apply standard precautions to everyday CNA care. | Moodle Lesson | Opening case: busy shift, missed hand hygiene | Scenario check | Complete lesson and check | Strong best-practice topic; course must match approved outline. |
| 1B | Hand hygiene and PPE sequencing | 30 min | Select correct hand hygiene and PPE steps for common resident care situations. | H5P Drag and Drop or Quiz | Sequence activity | Embedded knowledge check | Score threshold or completion | Interaction/feedback supports online CE control. [P0-S1] |
| 1C | Infection control scenario review | 30 min | Identify infection control mistakes and safer alternatives. | Branching scenario | Resident room decision path | Scenario outcome feedback | Complete path + remediation if needed | Text-based scenario avoids video dependency. |
| 2A | Resident rights and dignity | 30 min | Recognize rights-related risks during daily care. | Moodle Book + quiz | "What would you say?" examples | Knowledge check | Complete content and quiz | Part of abuse/resident-rights coverage. [P0-S10] |
| 2B | Abuse, neglect, exploitation, and reporting | 60 min | Recognize and report suspected abuse, neglect, exploitation, and rights violations. | Lesson + scenario quiz | Reporting decision tree | Module quiz | Pass quiz; remediation required if below threshold | HSC 1337.1 requires abuse/resident-rights continuing education coverage. [P0-S10] |
| 2C | Professional boundaries and privacy | 30 min | Maintain boundaries, privacy, and respectful care communication. | Page + reflection | Social media/privacy scenario | Ungraded reflection + check | Submit reflection/check | Avoid PHI in reflection instructions. |
| 3A | Dementia and Alzheimer disease care | 45 min | Use person-centered communication with residents with cognitive impairment. | Moodle Lesson | Agitation/redirection case | Scenario questions | Complete lesson + check | CMS facility in-service includes dementia/cognitive impairment. [P0-S9] |
| 3B | Communication with residents and families | 30 min | Use calm, respectful communication and report concerns through proper channels. | H5P Dialog Cards or Lesson | Choose-the-response prompts | Embedded checks | Complete activity | Keep scope-of-practice boundaries clear. |
| 3C | Trauma-informed and culturally sensitive care | 45 min | Support dignity, choice, and cultural respect within CNA role. | Moodle Book + reflection | Short resident preference cases | Confidence check + quiz | Complete check | Requires clinical education review for exact scope and language. |
| 4A | Body mechanics and safe transfers | 45 min | Choose safer transfer and body mechanics actions within facility policy. | Lesson + image-free sequence quiz | Unsafe transfer decision | Scenario quiz | Pass module quiz | Do not treat as hands-on competency validation. |
| 4B | Fall prevention and ambulation support | 45 min | Identify fall risks and report changes that increase risk. | Branching scenario | Resident wants to walk alone | Scenario decision | Complete scenario | Supports resident safety and observation/reporting. |
| 4C | Workplace safety | 30 min | Identify safety risks for CNAs and residents during routine care. | Page + quiz | Short hazard examples | Knowledge check | Complete quiz | Workplace safety topic; align with approved course objectives. |
| 5A | Nutrition, hydration, and feeding support | 30 min | Recognize nutrition/hydration risks and report concerns. | Moodle Lesson | Meal tray observation case | Embedded check | Complete lesson | Include scope limits and aspiration-risk reporting. |
| 5B | Skin integrity and pressure injury prevention | 45 min | Recognize skin-risk observations and report promptly. | Moodle Book + scenario | Repositioning/skin observation case | Scenario quiz | Pass quiz | Avoid instructing beyond CNA role. |
| 5C | Vital signs and observation | 45 min | Identify when vital signs or observations require reporting. | Lesson + practice quiz | Change in baseline case | Practice questions | Complete practice | Skills refresh only unless approved as competency assessment. |
| 6A | Documentation basics and PHI avoidance | 30 min | Document objectively and avoid prohibited information in course submissions. | Page + check | "Objective vs subjective" examples | Knowledge check | Pass check | Reinforces privacy and non-PHI upload rules. [P0-S11] |
| 6B | Change-of-condition reporting | 45 min | Decide what to report immediately and how to organize the message. | Branching scenario | Resident change over a shift | Scenario questions | Complete scenario | SBAR-style language may be used if clinically approved. |
| 6C | Team communication and CNA scope of practice | 45 min | Distinguish CNA duties, reporting duties, and tasks requiring licensed staff. | Lesson + quiz | Delegation/boundary cases | Module quiz | Pass quiz | Prevents unsafe role confusion. |
| 7A | Emergency preparedness and dignity-focused care | 30 min | Follow role-appropriate emergency and dignity principles. | Moodle Book | Short "during an event" cases | Knowledge check | Complete check | Align final wording with approved objectives/facility policies. |
| 7B | Course review and readiness check | 30 min | Identify personal weak areas before the final exam/test. | Practice quiz + feedback | Mixed-topic review | Ungraded practice | Complete practice | Low-stakes confidence support. |
| 8 | Final comprehensive exam/test and affidavit | 60 min | Demonstrate understanding of approved course material and complete required final statement. | Moodle Quiz + affidavit activity | Randomized question bank | Final exam/test | Meet passing threshold, complete identity/affidavit gates | Required for online CE certificate release. [P0-S1] [P0-S6] |

Total estimated time: 12 hours.

---

## 7. Microlearning Design System

Each learning unit should follow a consistent pattern so learners know what to expect and can move quickly on mobile devices.

| Learning Unit Element | Purpose | Moodle Tool | Required or Optional | Mobile UX Note |
|---|---|---|---|---|
| Short opening case | Anchor the topic in real care work. | Lesson, Page, Book | Required for most units | 75-150 words; no long setup. |
| Plain-language concept explanation | Teach the rule, principle, or decision point. | Book or Page | Required | Use headings, bullets, and examples. |
| "Why it matters" section | Connect to resident safety and CNA confidence. | Page/Book block | Required | Keep under one screen where possible. |
| Quick knowledge check | Confirm basic understanding. | Quiz, Lesson question, H5P Question Set | Required | 1-3 questions per short unit. |
| Scenario decision point | Require learner input and feedback. | Lesson or H5P Branching Scenario | Required where feasible | Avoid complex branching that is hard on phones. |
| TTS audio option | Offer low-burden listening support. | Embedded audio file | Optional; only if approved | Keep clips short; never audio-only. |
| Transcript | Accessibility and low-bandwidth alternative. | Page/Book text | Required if audio is used | Transcript appears next to the audio. |
| Downloadable job aid | Support later use and clinical confidence. | File or Page printable | Optional | One page, mobile-readable. |
| Reflection prompt | Encourage transfer to practice. | Feedback, text response, or ungraded prompt | Optional | Avoid asking for resident details or PHI. |
| Confidence check | Identify learner support needs. | Moodle Feedback or ungraded quiz | Optional | Use "for your planning" language. |
| Mastery checkpoint | Confirm readiness for next topic or final test. | Quiz | Required by module | Clear retake/remediation path. |
| Remediation path | Help learners recover from missed concepts. | Restrict Access + review page | Required for failed checks | Point to exact section, not full-module repeat unless needed. |

Recommended unit rhythm:

1. Case: "A resident..." or "During a busy shift..."
2. Key idea: one main concept.
3. CNA action: what the learner should do or report.
4. Check: one or two questions with feedback.
5. Confidence prompt: optional, brief, non-punitive.

---

## 8. MVP No-New-Video / Approved TTS Design Plan

The MVP should avoid new video production. Video can be valuable later, but it should not block a compliant first build.

| Existing Content Type | MVP Conversion | Engagement Upgrade | TTS Use | Risk |
|---|---|---|---|---|
| Approved PDF lesson | Convert into Moodle Book with short sections. | Add embedded checks every 5-10 minutes. | Optional short section summaries if authorized. | Risk if original approval does not cover edited wording. |
| PowerPoint deck | Convert to Moodle Lesson or H5P Course Presentation. | Add decision questions and feedback. | Optional narration for key slides only. | Avoid slide-dump design. |
| Long policy text | Break into short Pages with examples. | Add "What this means during care" blocks. | Optional audio recap. | Plain-language changes need review if compliance-sensitive. |
| Case example | Convert to Lesson branch or H5P Branching Scenario. | Add safe/risky choices with feedback. | Usually not needed. | Do not imply simulation clinical credit. |
| Quiz handout | Convert to Moodle Question Bank. | Categorize by objective and difficulty. | Not needed. | Need item review for accuracy and approved objectives. |
| Clinical packet | Convert to Clinical Support Hub resources. | Add schedule checklist, signoff guidance, and PHI warnings. | Optional quick refreshers. | Must not become certificate gate unless required. |
| Narrated text | Use approved cloned-voice TTS only with authorization. | Pair with transcript and visible controls. | Short clips, not long lectures. | Voice/IP/consent and accessibility review needed. |
| Skills demonstration video placeholder | Replace with text/photo-free steps, checklist, and job aid for MVP. | Add confidence check and "ask your supervisor" prompt. | Optional recap. | Do not claim hands-on competency validation. |

TTS rules:

1. Use only approved cloned voice with documented authorization.
2. Keep audio optional and paired with identical or equivalent transcript.
3. Avoid audio as the only source of testable information.
4. Version-control scripts used to generate TTS.
5. Do not use TTS to create an inaccessible "mini-lecture"; keep clips short.

---

## 9. Assessment and Mastery Strategy

The assessment system should be mastery-based without becoming punitive. It must include meaningful interaction/feedback, an exam/test for online CE, and certificate controls required by Phase 0. [P0-S1] [P0-S6]

| Module | Formative Check | Summative Check | Mastery Rule | Remediation Rule |
|---|---|---|---|---|
| 0 Orientation | Disclaimers and readiness questions | Acknowledgement quiz | 100% acknowledgement on required statements | Re-read orientation page before retry. |
| 1 Infection control | Sequencing and scenario checks | Module quiz | Suggested 80% or approved passing threshold | Review missed objective page, then retry. |
| 2 Rights/abuse/boundaries | Reporting decision questions | Module quiz | Suggested 80% or approved threshold | Review reporting pathway and rights summary. |
| 3 Dementia/communication/culture | Choose-the-response checks | Scenario quiz | Suggested 80% or approved threshold | Review communication examples. |
| 4 Mobility/falls/workplace safety | Transfer/fall-risk scenarios | Module quiz | Suggested 80% or approved threshold | Review safety steps and reporting triggers. |
| 5 Nutrition/skin/vitals | Observation/reporting checks | Module quiz | Suggested 80% or approved threshold | Review change-of-condition examples. |
| 6 Documentation/reporting/scope | Objective documentation and scope checks | Module quiz | Suggested 80% or approved threshold | Review CNA scope and PHI guidance. |
| 7 Review | Mixed practice quiz | Not graded or low stakes | Completion only | Links to missed topic pages. |
| 8 Final exam/test | Final readiness check | Comprehensive final exam/test | Passing score must match approved policy | Retake after targeted remediation. |

Recommended rules, subject to compliance approval:

| Item | Recommendation |
|---|---|
| Pre-checks | Optional and ungraded; used to direct attention, not skip required content. |
| Embedded checks | Required for interaction/feedback; feedback should teach, not merely say correct/incorrect. |
| Module quizzes | Required completion checkpoints; allow retakes after remediation. |
| Final exam/test | Required before certificate release; randomized from objective-aligned categories. |
| Passing score | Use approved standard, commonly 80% if not otherwise specified by approved policy. |
| Retakes | Allow retake after review; consider attempt limits only if approved and learner support is available. |
| Randomization | Randomize question order and answer order where appropriate. |
| Feedback timing | For practice checks, immediate feedback. For final exam, show outcome and remediation guidance without exposing full answer key if integrity requires. |
| Unlocking | Next module may unlock after required activity completion and mastery checkpoint. Final exam unlocks only after all required units and active-time controls are satisfied. |
| Certificate | Release only after identity confirmation, active-time evidence, required interactions, exam/test pass, signed statement/affidavit, and required certificate fields. |

Sample scenario question types:

| Type | Example |
|---|---|
| Best next action | "A resident who usually walks steadily is suddenly leaning to one side. What should you do first within CNA scope?" |
| Sequence | "Put these steps in order before assisting with a transfer." |
| Risk identification | "Which observation should be reported immediately?" |
| Boundary decision | "A family member asks you to explain a diagnosis. What is the safest response?" |
| Documentation judgment | "Which note is objective and appropriate?" |

Sample feedback style:

| Learner Choice | Feedback Style |
|---|---|
| Safe choice | "Yes. This protects the resident and keeps you within CNA scope. Report the change promptly and follow facility policy." |
| Risky choice | "Not the safest choice. Waiting can delay care. Review the change-of-condition reporting steps, then try a similar case." |
| Common misconception | "This is a common shortcut on a busy shift, but it creates risk. The safer step is..." |

---

## 10. Scenario-Based Learning Guide

Scenarios should be short, realistic, and respectful. They should not require elaborate multimedia to be effective.

| Scenario Topic | Setup | Decision Point | Good Choice | Risky Choice | Feedback Style | Moodle/H5P Tool |
|---|---|---|---|---|---|---|
| Infection control mistake | A resident call light goes off while the CNA is removing gloves. | What should the CNA do before responding? | Complete glove removal and hand hygiene, then respond safely. | Skip hand hygiene because the resident is waiting. | Acknowledge urgency while reinforcing standard precautions. | Lesson or Branching Scenario |
| Resident rights conflict | A resident refuses a bath before breakfast. | How should the CNA respond? | Respect refusal, offer choices, report/document per policy. | Force the bath because it is on the schedule. | Reinforce dignity, choice, and reporting. | Lesson |
| Possible abuse/neglect reporting | The CNA notices unexplained bruising and a resident seems fearful. | What is the safest next step? | Report promptly through required chain/policy. | Wait to see if it happens again. | Emphasize prompt reporting and no personal investigation beyond role. | Quiz scenario |
| Dementia communication | A resident with dementia says they need to leave for work. | What response is most supportive? | Validate feeling, redirect calmly, ensure safety. | Argue that the resident is retired. | Explain validation and de-escalation. | Dialog Cards or Lesson |
| Unsafe transfer decision | A resident asks for help standing but seems weaker than usual. | What should the CNA do? | Pause, assess within role, get help/report change. | Transfer alone to stay on schedule. | Link body mechanics, fall prevention, and reporting. | Branching Scenario |
| Fall risk observation | The room has a spill and call light is out of reach. | What should be addressed first? | Secure safety, clean/report spill, keep call light accessible. | Leave it for housekeeping later. | Reinforce immediate environmental safety actions. | Drag and Drop or Quiz |
| Nutrition/hydration concern | A resident eats almost nothing for two meals. | What should the CNA do? | Encourage as appropriate and report intake concern. | Assume the resident is not hungry. | Reinforce observation and timely reporting. | Lesson |
| Skin integrity observation | Redness is seen over a bony area during care. | What should be done? | Report promptly and follow repositioning/care plan. | Massage the red area. | Correct unsafe habits and scope boundaries. | Quiz scenario |
| Change-of-condition reporting | A resident is suddenly confused compared with baseline. | What information should be reported? | Objective changes, time noticed, vitals if collected, relevant observations. | "Resident is acting weird" with no details. | Teach objective communication. | Lesson |
| Scope-of-practice boundary | A resident asks whether to stop taking medication. | What should the CNA say/do? | Do not advise; report question to licensed nurse. | Give personal opinion. | Reinforce role limits and team communication. | Quiz scenario |

Scenario writing standards:

1. Use one decision per screen.
2. Use believable shift constraints without blaming the learner.
3. Give feedback that explains the resident safety reason.
4. Avoid patient-identifying details.
5. Do not label online scenarios as clinical hours or clinical competency validation.

---

## 11. Clinical LMS Support Hub Design

The Clinical Support Hub should feel like a helpful resource center. It should not be required for the theory certificate unless CDPH/legal review specifically requires a clinical support item as part of the approved online CE pathway.

| Clinical LMS Element | Required for Compliance? | Optional Support? | Learner Benefit | Admin Benefit |
|---|---|---|---|---|
| Clinical support overview | No, unless approved as part of course | Yes | Explains that support is optional and not California clinical-hour credit unless approved. | Reduces learner confusion. |
| Schedule guidance | No | Yes | Helps learner plan workplace/lab/preceptor time where applicable. | Fewer support questions. |
| Pre-clinical checklist | No | Yes | Clarifies what to bring and how to prepare. | Standardizes expectations. |
| Skills refresh menu | No | Yes | Quick review before practice. | Encourages readiness. |
| Optional confidence checks | No | Yes | Helps learner identify topics to review. | May identify support needs without grading. |
| Downloadable skills checklist | No, unless approved | Yes | Gives learner a structured practice guide. | Supports consistent documentation. |
| RN/preceptor signoff tool | Needs state verification | Yes, if used | Helps organize evidence when appropriate. | Creates reviewable records. |
| Upload portal | Needs privacy review | Yes, if used | Central place for de-identified documentation. | Easier admin review. |
| Communication forum/message link | No | Yes | Reduces uncertainty. | Centralizes support. |
| Clinical completion certificate gate | No by default | No | Should not block online CE certificate unless required. | High compliance risk if unapproved. |
| Simulation/LTI activity | No clinical credit without written CDPH approval | Optional learning support only | Practice judgment in low-stakes format. | Must be clearly labeled non-credit support. |

Required learner-facing clinical hub language:

> The Clinical Support Hub is an optional learner support resource unless CI Institute of Nursing gives you written instructions that a specific item is required. Clinical support activities, simulations, virtual simulations, uploads, confidence checks, and skills refreshers are not California CNA renewal clinical hours and do not replace CDPH renewal documentation unless CDPH has approved that use in writing.

---

## 12. Scheduling and Pre-Clinical Prep Design

| Resource | Moodle Tool | Required or Optional | Purpose | Mobile UX Note |
|---|---|---|---|---|
| "What to expect" page | Moodle Page | Optional support | Reduce anxiety and clarify support purpose. | Use short sections and direct language. |
| "What to bring" checklist | Moodle Page/File | Optional support | Help learner prepare for workplace/lab/preceptor activity. | Printable one-page version. |
| Before-your-day checklist | Moodle Checklist or Page | Optional support | Encourage readiness without grading. | Checkboxes large enough for phone use. |
| Location/contact details | Page | Optional support | Provide contact and scheduling clarity. | Keep phone numbers tap-friendly. |
| How to document support hours | Page + template | Optional; not credit unless approved | Explain documentation support and limitations. | Include disclaimer above template. |
| RN/preceptor signoff guidance | Page + form | Optional; needs review | Explain what information to collect if signoff is used. | Avoid free-text PHI fields. |
| What not to upload | Page + acknowledgement | Strongly recommended if uploads exist | Prevent PHI submission. | Put warning before every upload. |
| Skills refresher menu | Book or folder | Optional support | Let learners review topics before practice. | Organize by skill, not module number only. |
| Quick confidence check | Feedback | Optional support | Let learner self-identify weak areas. | 1-5 scale plus suggested resources. |
| Printable checklist | File | Optional support | Support offline use. | One page per major skill category. |

Recommended PHI warning for upload/reflection areas:

> Do not upload or type patient/resident names, faces, medical record numbers, dates of birth, addresses, chart screenshots, medication records, facility records, or any information that could identify a patient or resident. Use only de-identified learning documentation requested by the course. Submissions containing patient/resident identifiers may be rejected or deleted according to privacy procedures.

---

## 13. Optional Clinical Confidence Check Design

Clinical confidence checks should help learners prepare. They should not affect theory certificate completion unless compliance later requires a specific item.

| Optional Assessment | Moodle Tool | Learner Value | Should It Affect Completion? | Notes |
|---|---|---|---|---|
| Transfer confidence rating | Moodle Feedback | Identifies whether learner should review body mechanics. | No | Offer link to transfer refresher. |
| Hand hygiene/PPE sequence | Ungraded Quiz or H5P Drag and Drop | Practice infection control sequence. | No | Can provide immediate feedback. |
| Change-of-condition self-check | H5P Question Set | Builds reporting confidence. | No | Scenario only; not competency validation. |
| Fall-risk observation check | Ungraded Quiz | Reinforces what to report. | No | Use practical examples. |
| Documentation practice | Moodle Quiz or Lesson | Practice objective wording. | No | Do not allow PHI examples from real residents. |
| Scope boundary check | Ungraded Quiz | Reduces unsafe advice/delegation. | No | Link to licensed nurse escalation language. |
| Skills readiness checklist | Moodle Checklist | Helps learner plan practice/support. | No | Learner-owned planning tool. |
| Reflection prompt | Moodle Feedback | Encourages transfer to practice. | No | Prompt must prohibit resident identifiers. |
| Optional support request | Moodle Choice or Feedback | Lets learner ask for help. | No | Route to support staff; not a grade. |

Learner-facing label:

> This confidence check is for your own preparation. It is not graded, does not count as clinical hours, and does not block your online CE certificate unless CI Institute of Nursing separately notifies you of a CDPH-approved requirement.

---

## 14. Clinical Skills Checklist

This checklist is a support and planning tool. It should not be represented as California renewal clinical-hour credit, competency validation, or certificate eligibility unless CDPH/legal review approves that use in writing.

| Skill | Verification Method | Evaluator Role | Evidence Required | Learner Support Resource | Completion Rule |
|---|---|---|---|---|---|
| Hand hygiene | Optional observation or self-check | Self, supervisor, or approved evaluator if required | Checklist only; no PHI | Infection control refresher | Optional support only |
| PPE use | Optional observation or sequence check | Self/supervisor/evaluator | Checklist or ungraded quiz | PPE sequence job aid | Optional support only |
| Bed bath or partial bath | Optional supervised practice | Facility/preceptor if available | De-identified signoff if used | Dignity/privacy reminder | Optional support only |
| Transfer techniques | Optional supervised practice | Supervisor/preceptor if available | Signoff if used; no resident identifiers | Body mechanics refresher | Optional support only |
| Ambulation assistance | Optional supervised practice | Supervisor/preceptor if available | Signoff if used | Fall prevention refresher | Optional support only |
| Feeding assistance | Optional observation/practice | Supervisor/preceptor if available | Checklist if used | Nutrition/hydration refresher | Optional support only |
| Vital signs | Optional practice/refresh | Supervisor/preceptor if available | Checklist or practice log if used | Vital signs/reporting refresher | Optional support only |
| Range of motion | Optional supervised practice | Supervisor/preceptor if available | Checklist if used | Mobility support guide | Optional support only |
| Perineal care | Optional supervised practice | Supervisor/preceptor if available | Signoff only if appropriate; no details | Privacy/dignity guide | Optional support only |
| Turning/repositioning | Optional supervised practice | Supervisor/preceptor if available | Checklist if used | Skin integrity refresher | Optional support only |
| Catheter care where allowed | Optional policy-based refresh | Licensed staff/supervisor if appropriate | Checklist only if within facility policy | Scope warning + facility policy note | Optional support only |
| Intake and output | Optional practice | Supervisor/preceptor if available | Practice worksheet; no resident identifiers | Documentation refresher | Optional support only |
| Dementia communication | Optional scenario/reflection | Self/supervisor if available | Reflection without PHI | Dementia communication guide | Optional support only |
| Fall prevention | Optional observation checklist | Self/supervisor if available | Environmental checklist | Fall-risk refresher | Optional support only |
| Skin observation | Optional scenario/refresher | Self/supervisor if available | Scenario responses only | Skin reporting guide | Optional support only |
| Reporting abnormal observations | Optional scenario/reflection | Self/supervisor if available | Scenario response; no real resident data | Change-of-condition guide | Optional support only |
| Resident rights and dignity | Optional reflection/scenario | Self/supervisor if available | Reflection without identifiers | Rights/dignity guide | Optional support only |

If CI Institute of Nursing later seeks approval for any clinical or in-service credit pathway, this checklist must be reviewed for exact evaluator credentials, setting, evidence, CDPH forms, signature requirements, certificate wording, and whether Moodle documentation is acceptable.

---

## 15. Mobile-First Learner Experience Notes

| Design Area | Recommendation |
|---|---|
| Navigation | Use a single course landing page with "Start here," current module, required gates, optional clinical support, and certificate status. |
| Unit length | Keep most learning units 15-30 minutes. Put natural breaks every 5-10 minutes. |
| Text | Use short paragraphs, descriptive headings, and plain language. Avoid walls of text. |
| Tables | Avoid large tables inside the learner course where possible; convert to cards or short lists. |
| Audio | Optional short TTS clips with transcripts; do not require headphones to complete. |
| Downloads | Job aids should be one page and readable on a phone. |
| Quizzes | Use one question per screen or very small groups; avoid tiny drag targets where possible. |
| Progress | Show completed/remaining requirements clearly. |
| Remediation | Link directly to the relevant concept, not the full course. |
| Clinical support | Separate optional hub visually from required theory pathway. |
| Low bandwidth | Ensure core content is text-based and does not require streaming video. |
| Return visits | Make it easy to resume where the learner stopped. |

---

## 16. Accessibility and Plain-Language Guidance

The course should follow recognized accessibility and health-literacy practices, including WCAG principles, plain language, readable structure, captions/transcripts for media, keyboard accessibility, sufficient contrast, and alternatives for audio. [L3] [L4] [L5]

| Area | Guidance |
|---|---|
| Structure | Use headings in order and descriptive link text. |
| Reading level | Use plain language while preserving essential CNA and healthcare terms. Define terms in context. |
| Audio/TTS | Provide transcripts for all audio; do not require audio-only learning. |
| Images | Use alt text where images are instructional. Avoid decorative image overload. |
| Color | Do not rely on color alone for meaning. |
| Interactions | Ensure quizzes and H5P-style activities are usable on mobile and accessible by keyboard/screen reader where possible. |
| Cognitive load | Introduce one main concept at a time and reduce extraneous content. [L1] [L2] |
| Adult learning | Start with practical relevance and respect learner experience. [L6] |
| Universal design | Offer multiple ways to access content where feasible: text, audio, transcript, practice questions, job aids. [L5] |
| Language tone | Use direct, respectful wording; avoid shame-based feedback. |

---

## 17. Learner-Facing Disclaimer Language

These are recommended plain-language blocks for compliance/legal review before use.

### Partial Credit Disclaimer

> This course provides 12 hours of online continuing education only if CI Institute of Nursing and this course are approved for California CNA online CE and if the hours fit within your renewal limits. California CNA renewal requires 48 hours over each two-year certification period, with at least 12 hours completed each year. Only 24 of the 48 hours may be completed through CDPH-approved online CE. This course does not, by itself, complete all California CNA renewal requirements.

### Online-Hour Cap Attestation

> I understand that California limits online CNA renewal CE credit to 24 hours per two-year renewal period. I am responsible for tracking whether these 12 online hours fit within my allowed online CE hours.

### Clinical Support Disclaimer

> The Clinical Support Hub is optional learner support unless CI Institute of Nursing gives written instructions that a specific item is required. Clinical support resources, confidence checks, scheduling tools, uploads, simulations, and skills refreshers do not count as California CNA renewal clinical hours or replace CDPH renewal documentation unless CDPH approves that use in writing.

### Simulation Disclaimer

> Online scenarios, virtual simulations, LTI simulations, and practice activities are learning supports only. They do not count as clinical hours or hands-on competency verification for California CNA renewal unless CDPH provides written approval for that specific use.

### PHI Avoidance Disclaimer

> Do not upload or type any patient/resident identifiers or protected health information. Do not include names, faces, medical record numbers, birth dates, addresses, facility chart screenshots, medication records, or any details that could identify a patient or resident.

### Certificate Gate Reminder

> Your online CE certificate can be released only after all required course activities, active-time requirements, interaction/feedback activities, exam/test requirements, identity confirmation, final signed statement/affidavit, and required certificate fields are complete.

---

## 18. Risks Where Instructional Design Could Become Busywork

| Risk | Why It Matters | Prevention |
|---|---|---|
| Too many reflections | Tired learners may experience them as filler. | Use reflections only when they support transfer or confidence. |
| Overbuilt branching | Complex scenarios can become frustrating on mobile. | Keep branches shallow and feedback practical. |
| Optional clinical tasks look required | Learners may think support tasks block renewal. | Label optional tasks clearly and keep them outside certificate gates. |
| Gamification feels childish | Experienced CNAs may disengage. | Use progress clarity and meaningful feedback instead of games. |
| Dense PDF reliance | Learners may skim without understanding. | Convert to short Moodle-native sections with checks. |
| TTS becomes long lectures | Audio can recreate passive video problems. | Keep TTS short, optional, and transcript-supported. |
| Quiz overload | Learners may focus on passing rather than practice meaning. | Use fewer, better questions with feedback and remediation. |
| Clinical upload burden | Uploads can create privacy and support load. | Use structured, minimal, non-PHI templates only if needed. |
| Misleading skill checks | Confidence checks can be mistaken for competency validation. | Label as practice/support and require review before any credit claim. |
| Certificate gates multiply | Unnecessary gates create frustration and support tickets. | Gate only compliance-required theory items; keep support optional. |

---

## 19. Recommendations for Compliance Team

| Recommendation | Rationale |
|---|---|
| Confirm CI Institute of Nursing provider status, NAC#, course approvals, approved titles, approved hours, and certificate language before certificate release. | Phase 0 identifies this as necessary before issuing California CNA renewal online CE certificates. |
| Approve exact learner-facing disclaimers before launch. | Disclaimers must accurately state partial credit, online cap, clinical support limits, and simulation limits. |
| Confirm whether 12 hours may be issued as one certificate or must be separated by approved course. | Impacts instructional packaging and final exam/certificate logic. |
| Confirm e-signature acceptability for final signed statement/affidavit. | Certificate release depends on this workflow. |
| Review all clinical hub language before publication. | Prevents optional support from becoming an unapproved clinical-hour claim. |
| Review privacy language and upload controls. | Avoids PHI collection and related legal exposure. |
| Review TTS authorization and records. | Cloned voice use requires authorization and version control. |

---

## 20. Recommendations for Moodle Architecture Team

These are Phase 3 instructional dependencies only, not a Phase 2 infrastructure design.

| Dependency | Instructional Need |
|---|---|
| Mobile-friendly content formats | Learning units must work well for phone-based CNAs. |
| Activity completion and Restrict Access | Required to sequence lessons, checks, exam/test, affidavit, and certificate release. |
| Active-time/pause control | Required by Phase 0 for online CE timing; instructional units must align to 50 active minutes per CE hour. [P0-S6] |
| Quiz/question bank categories | Needed for module quizzes, final exam/test, randomization, and remediation. |
| Feedback/remediation links | Needed so missed items point learners to relevant review sections. |
| TTS/audio transcript support | Needed if approved audio is added. |
| Optional hub separation | Clinical support must be visibly separate from required online CE certificate pathway. |
| Non-PHI upload warnings | Needed if any clinical support uploads exist. |
| Audit evidence export | Needed to document identity, completion, active time, interactions, exam/test, affidavit, and certificate release. |

---

## 21. Recommendations for Migration/Operations Team

These are Phase 3 dependencies only and should be reconciled in later phases.

| Dependency | Instructional Need |
|---|---|
| Approved source content inventory | ID team needs to know which legacy/approved content can be cloned faithfully. |
| Content change-control process | Any edits to approved wording, objectives, titles, hours, or assessments may require review. |
| TTS script approval workflow | Scripts must match approved content and be retained for audit/versioning. |
| Question review workflow | Quiz items need clinical and compliance review before import. |
| Learner support process | Retakes, remediation, and technical support need clear ownership. |
| Clinical support communications | Staff must explain optional clinical hub boundaries consistently. |
| PHI incident workflow | Operations needs a response if learners upload prohibited information. |
| Certificate exception process | Manual overrides must be restricted, documented, and audited. |

---

## 22. Explicit Assumptions, Risks, and Review Flags

| Item | Status | Action Needed |
|---|---|---|
| 12-hour theory course can be approved as online CE. | Depends on CDPH approval. | Obtain/confirm approval before issuing credit. |
| Course can be built as one 12-hour course. | Needs CDPH confirmation. | Verify whether one certificate or separate course certificates are required. |
| Suggested 80% mastery threshold is acceptable. | Assumption. | Align with approved course policy. |
| E-signature affidavit is acceptable. | Needs CDPH/legal confirmation. | Confirm before launch. |
| Approved cloned-voice TTS can be used. | Needs authorization. | Confirm voice consent/IP and script controls. |
| Clinical hub can collect signoffs. | Needs legal/privacy/clinical review. | Confirm fields, evaluator role, storage, and non-PHI procedures. |
| Optional clinical support will not gate certificate. | Required default position from Phase 0. | Do not change unless written compliance approval requires it. |
| Simulation can be used as interaction/support. | Acceptable only as support or approved online CE interaction, not clinical hours. | Label clearly and obtain approval if counted toward CE course activity. |
| Mobile H5P-style activities are accessible enough. | Needs testing. | Validate on phones and with accessibility checks before launch. |
| Learners understand partial credit. | Risk. | Place disclaimers at enrollment, orientation, certificate page, and clinical hub. |

---

## 23. Source Register

Phase 0 source references are cited from `PHASE_0_COMPLIANCE_FOUNDATION.md` and are treated as the controlling compliance source.

| ID | Source |
|---|---|
| P0-S1 | California Health and Safety Code section 1337.6, renewal and online computer training requirements: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1337.6 |
| P0-S2 | CDPH, Online Continuing Education Providers: https://www.cdph.ca.gov/Programs/CHCQ/LCP/Pages/Online-Continuing-Education-Providers.aspx |
| P0-S3 | CDPH 283A, CNA/HHA In-Service Training / Continuing Education Units: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph283a.pdf |
| P0-S4 | CDPH 283C, CNA/HHA Renewal Application: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph283c.pdf |
| P0-S5 | 22 CCR section 71839, Renewal of Unexpired Certificates: https://www.law.cornell.edu/regulations/california/22-CCR-71839 |
| P0-S6 | CDPH 192B, Online Continuing Education Provider application and controls: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph192b.pdf |
| P0-S7 | CDPH 192, Continuing Education Provider application and records: https://www.cdph.ca.gov/CDPH%20Document%20Library/ControlledForms/cdph192.pdf |
| P0-S9 | 42 CFR 483.95(g), nurse aide in-service training: https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-483/subpart-B/section-483.95 |
| P0-S10 | California Health and Safety Code section 1337.1, abuse/resident-rights continuing education: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1337.1 |
| P0-S11 | HHS OCR, De-identification of Protected Health Information: https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html |
| P0-S12 | HHS OCR, HIPAA and Cloud Computing guidance: https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html |
| L1 | Sweller, Cognitive Load Theory overview, Center for Open Education Research: https://www.oerknowledgecloud.org/archive/sweller-cognitive-load-theory.pdf |
| L2 | Mayer, Multimedia Learning principles, Cambridge University Press overview: https://www.cambridge.org/core/books/multimedia-learning/ |
| L3 | HHS, Health Literacy Online: https://health.gov/healthliteracyonline/ |
| L4 | PlainLanguage.gov, Federal plain language guidelines: https://www.plainlanguage.gov/guidelines/ |
| L5 | W3C Web Content Accessibility Guidelines (WCAG) 2.2: https://www.w3.org/TR/WCAG22/ |
| L6 | Knowles, adult learning principles summarized by InstructionalDesign.org: https://www.instructionaldesign.org/theories/andragogy/ |
| L7 | CAST Universal Design for Learning Guidelines: https://udlguidelines.cast.org/ |

---

## Dependencies / Items for Final Reconciliation

1. Confirm CDPH approval status, NAC#, approved course titles, approved hours, objectives, outlines, certificate wording, and whether the 12 hours must be issued as one certificate or separate certificates.
2. Confirm exact certificate gate sequence: identity confirmation, active-time control, required interactions, exam/test, signed statement/affidavit, certificate fields, and retention/export evidence.
3. Confirm whether e-signature is acceptable for the final signed statement/affidavit, or whether a different signature method is required.
4. Confirm whether any clinical support item is required by compliance. Until confirmed in writing, clinical support remains optional and must not gate the online CE certificate.
5. Confirm all clinical support hub copy, signoff forms, upload fields, and privacy workflows with legal/privacy/clinical education reviewers before launch.
6. Confirm that simulation, virtual simulation, and LTI simulation are not counted toward clinical hours unless written CDPH approval is obtained for the exact use.
7. Confirm TTS cloned-voice authorization, script approval, transcript requirements, and version-control procedures.
8. Confirm accessibility testing expectations for Moodle-native content, quizzes, and H5P-style activities on mobile devices.
9. Reconcile this Phase 3 blueprint with Phase 2 Moodle architecture only for required instructional dependencies, not by redesigning infrastructure here.
10. Reconcile this report with Phase 4 migration/operations only for source content cloning, review workflow, learner support, PHI incident handling, and certificate exception handling.
