# Prototype 1 Open Blockers

## Current Blocker List

| Blocker | Category | Impact | Owner | Resolution Needed | Blocks Prototype? | Blocks Certificate Pilot? |
|---|---|---|---|---|---|---|
| CDPH provider/course approval metadata not documented | CDPH/legal blockers | Production certificate cannot be enabled | Compliance Lead | Document approval, NAC#/provider metadata, approved course list, and approval dates | No, staging override allowed | Yes |
| Final certificate wording not approved | CDPH/legal blockers | Production certificate PDF cannot be issued | Compliance Lead / Registrar | Obtain approved wording and field requirements | No, staging-only template allowed | Yes |
| Final affidavit/e-signature method not approved | CDPH/legal blockers | Final statement workflow cannot be treated as production-ready | Compliance Lead / Legal | Approve e-sign, assignment, feedback, or wet-sign method | No, placeholder allowed | Yes |
| Optional clinical support not approved as clinical-hour credit | CDPH/legal blockers | Optional support cannot count as required clinical hours | Compliance Lead | Written CDPH approval required for any credit claim | No | Yes, if pilot intends clinical-hour credit |
| Active-time plugin candidate not validated | Active-time blockers | Automatic time gate may be unreliable | Moodle Admin | Run Prototype 1 active-time test plan | Yes, unless manual fallback is configured | Yes |
| Manual active-time review fallback not configured | Active-time blockers | No defensible fallback if plugin fails | Moodle Admin / Compliance Lead | Configure admin review record and compliance hold | Yes if plugin fails | Yes |
| Certificate plugin not validated | Certificate blockers | Certificate gating, issue log, and field output may fail | Moodle Admin / Registrar | Validate certificate plugin in staging | Yes for certificate POC | Yes |
| Required profile fields not configured in staging | Moodle/plugin blockers | Identity gates cannot be tested | Registrar / Moodle Admin | Configure legal name and CNA certificate number fields | Yes | Yes |
| QA test users not created | QA blockers | Negative tests cannot run | QA Lead / Moodle Admin | Create learner, admin, instructor/support, registrar, and compliance test users | Yes | Yes |
| Audit export path not proven | QA blockers | Evidence package may be incomplete | QA Lead / Moodle Admin | Run audit dry run and log gaps | Yes | Yes |
| Optional/required progress separation not configured | Moodle/plugin blockers | Optional support may inflate required CE progress or gate certificate | Moodle Admin | Separate progress/completion and verify certificate restrictions | Yes | Yes |
| PHI warning not configured near documentation support | Privacy blockers | Learners may upload/type PHI | Privacy Officer / Moodle Admin | Add warning and disable PHI collection | Yes if documentation stub exists | Yes |
| Final lesson content absent | Content blockers | Full course cannot launch | Instructional Design Lead | Build final content in later phase | No | Yes |
| New video production excluded | Content blockers | Video-dependent course design cannot proceed | Product Lead | Use non-video MVP approach or later approved media plan | No | No, if MVP avoids new video |
| Staging Moodle access details not available to build agent | Moodle/plugin blockers | Moodle category, course shells, profile fields, gate restrictions, test users, evidence capture, and QA execution cannot be configured or verified | Moodle Admin / Build Lead | Provide staging Moodle URL, admin-capable access path, and selected certificate and active-time candidate tools outside the repository | Yes | Yes |
| Role permission override path untested | QA blockers | Unauthorized users might bypass gates | Moodle Admin / QA Lead | Run role permission tests | Yes | Yes |
