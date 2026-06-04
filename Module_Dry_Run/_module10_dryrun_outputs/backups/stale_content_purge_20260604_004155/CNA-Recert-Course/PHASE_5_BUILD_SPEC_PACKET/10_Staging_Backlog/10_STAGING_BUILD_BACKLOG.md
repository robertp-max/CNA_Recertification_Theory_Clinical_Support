# Staging Build Backlog

**Priority scale:**  
P0 = must be done before certificate-enabled pilot.  
P1 = must be done before full launch.  
P2 = post-MVP improvement.  
P3 = elite/version-two.

---

| Backlog Item | Workstream | Priority | Owner | Dependency | Acceptance Criteria | Launch Blocker? |
|---|---|---|---|---|---|---|
| Create approval metadata record shell | Compliance metadata and approval archive | P0 | Compliance Lead | Final blueprint/Phase 0 | Record includes provider approval status, NAC#, course list, certificate wording status, affidavit status | Yes |
| Upload approval docs to restricted archive | Compliance metadata and approval archive | P0 | Compliance Lead | Approval documents | Restricted archive visible only to authorized roles | Yes |
| Build staging course categories | Moodle shell | P0 | Moodle Admin | Moodle staging site | Required theory and optional clinical support separated | Yes |
| Build required/optional labels | Moodle shell | P0 | Moodle Admin / ID Lead | Course shell | Learner sees required vs optional labels clearly | Yes |
| Build learner dashboard prototype | Moodle shell | P1 | Moodle Admin | Completion settings | Dashboard shows required CE status separately from optional support | No for pilot if labels suffice |
| Build Module 0 orientation | Theory CE pathway | P0 | ID Lead | Learner copy review | Orientation includes partial credit, online cap, no PHI, certificate path | Yes |
| Build first theory prototype module | Theory CE pathway | P0 | ID Lead | Approved source content placeholder | Includes content, interaction, quiz/check, completion | Yes |
| Build full 12-hour theory shell | Theory CE pathway | P1 | ID Lead | Approved content map | All sections present with placeholders/content status | No for first prototype |
| Validate active-time candidate | Active-time control | P0 | Moodle Admin | Plugin candidate installed in staging | Active-time test matrix passed or fallback selected | Yes |
| Build custom/manual compliance hold if needed | Active-time control | P0 | Moodle Admin | Active-time validation result | Certificate cannot release without time review/status | Yes |
| Build question bank structure | Quiz/exam | P0 | RN Educator / ID Lead | Approved exam blueprint | Categories by module/objective/version | Yes |
| Configure final exam/test prototype | Quiz/exam | P0 | Moodle Admin / RN Educator | Question bank | Pass/fail controls and remediation message work | Yes |
| Confirm final pass/retake policy | Quiz/exam | P0 | Compliance Lead | CDPH/course approval | Approved standard documented | Yes |
| Build affidavit workflow prototype | Affidavit | P0 | Registrar / Moodle Admin | Legal/CDPH signature decision pending | Staging workflow blocks certificate if missing | Yes |
| Decide e-sign vs wet-sign process | Affidavit | P0 | Legal/Compliance | CDPH/legal review | Approved method documented | Yes |
| Build certificate template draft | Certificate | P0 | Registrar | Certificate field map | Draft has required placeholders and disabled production issue | Yes |
| Lock certificate permissions | Certificate | P0 | Moodle Admin | Role matrix | Only authorized roles edit template/release | Yes |
| Build certificate gate conditions | Certificate | P0 | Moodle Admin | Completion/time/exam/affidavit settings | Negative tests pass | Yes |
| Build clinical support hub landing page | Clinical support hub | P0 | Clinical Coordinator / ID Lead | Approved disclaimer draft | Hub clearly states optional support boundary | Yes |
| Build skills refresh library shell | Clinical support hub | P1 | RN Educator | Clinical resource list | Resources labeled optional support | No |
| Build optional confidence checks | Clinical support hub | P1 | RN Educator / ID Lead | Support objectives | Ungraded and non-gating | No |
| Build optional upload workflow | Clinical support hub | P1 | Clinical Coordinator | Privacy review | Upload warning, non-PHI attestation, reject/resubmit path | Yes if uploads in pilot |
| Build PHI warning blocks | PHI prevention | P0 | Privacy Officer / ID Lead | Privacy copy | Warning appears before any upload/free-text clinical reflection | Yes if uploads/free text exist |
| Build PHI incident workflow | PHI prevention | P0 | Privacy Officer | Operational policy | Quarantine/reject/escalate steps documented | Yes if uploads exist |
| Configure audit exports | Reports/audit packet | P0 | Moodle Admin | Reports available | Sample packet produced for test learner | Yes |
| Build manual override log | Reports/audit packet | P0 | Compliance Lead | Override policy | Override requires approver/reason/evidence/date | Yes |
| Configure role matrix | Roles/permissions | P0 | Moodle Admin | Staff role list | Learner/instructor/RN/support/registrar/admin permissions tested | Yes |
| Test mobile browser path | Mobile/accessibility | P0 | QA Tester | Prototype path | Required path works on phone | Yes |
| Run accessibility smoke test | Mobile/accessibility | P1 | QA Tester | Prototype path | Headings, contrast, keyboard/screen reader smoke pass | No for first prototype; yes before launch |
| Execute negative certificate tests | QA/UAT | P0 | QA Manager | Prototype configured | QA-001 through QA-020 pass as applicable | Yes |
| Create support scripts | Support operations | P1 | Support Lead | Learner copy | Scripts explain partial credit, active time, certificate holds | No for first prototype |
| Configure backups and restore test | Backup/restore | P0 | IT/Security | Staging environment | Backup and restore test documented | Yes |
| Build QR verification | Certificate | P3 | IT/Security | MVP stable | Privacy-limited verification only | No |
| Build SMS reminders | Support operations | P3 | Support Lead | Consent/privacy review | Opt-in/out tested | No |
| Build custom audit packet generator | Reports/audit packet | P2 | Moodle Admin / Developer | Manual burden data | One-click export matches spec | No |
| Add new videos | Theory CE pathway | P3 | Media Lead | Approved scripts/budget | Captions/transcripts and approval records | No |
| Add LTI simulation | Clinical support hub | P3 | Program Owner | CDPH written approval if credit claimed | Labeled support unless approved | No |
