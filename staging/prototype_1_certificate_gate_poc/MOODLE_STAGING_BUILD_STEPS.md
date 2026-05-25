# Moodle Staging Build Steps

## Admin Build Checklist

Use this checklist in a non-production Moodle staging site. Do not enable production certificate issuance.

| Step | Moodle Area | Action | Owner | Dependency | Done? |
|---|---|---|---|---|---|
| 1 | Course categories | Create staging course category named `Prototype Build 1 - Certificate Gate POC` | Moodle Admin | Staging Moodle access | No |
| 2 | Course shell | Create theory course shell for `California CNA Online CE Theory - Prototype 1` | Moodle Admin | Step 1 | No |
| 3 | Course shell | Confirm course completion tracking is enabled | Moodle Admin | Step 2 | No |
| 4 | Optional support | Create separate optional clinical support course or clearly separated section | Moodle Admin | Step 2 | No |
| 5 | Admin archive | Create admin-only compliance archive placeholder | Moodle Admin | Step 2 | No |
| 6 | Roles/permissions | Confirm learner, instructor, registrar, compliance reviewer, QA, and admin test roles | Moodle Admin | Staging user policy | No |
| 7 | Profile fields | Configure required legal name field or confirm source user identity field | Registrar | Moodle user profile access | No |
| 8 | Profile fields | Configure required CNA certificate number field | Registrar | Step 7 | No |
| 9 | Completion tracking | Configure required activity completion for orientation, theory activity, interaction, exam, affidavit, and acknowledgement | Moodle Admin | Steps 2, 3 | No |
| 10 | Restrict Access | Configure required sequence and hide/lock downstream gates until prerequisites complete | Moodle Admin | Step 9 | No |
| 11 | Orientation | Configure Module 0 orientation acknowledgement | Instructional Designer | Learner copy draft | No |
| 12 | Sample theory module | Configure one sample required theory content activity with completion | Instructional Designer | Step 9 | No |
| 13 | Required interaction | Configure one required interaction/check with completion record | Instructional Designer | Step 12 | No |
| 14 | Active-time | Install/select candidate active-time report in staging or define manual admin review hold | Moodle Admin | Plugin candidate decision | No |
| 15 | Active-time | Configure active-time threshold placeholder/control for final exam and certificate availability | Moodle Admin | Step 14 | No |
| 16 | Final exam/test | Configure final exam/test placeholder with grade-to-pass and direct URL restriction | RN Educator / Moodle Admin | Steps 10, 15 | No |
| 17 | Affidavit | Configure final signed statement/affidavit placeholder | Registrar / Compliance | Affidavit method not final | No |
| 18 | Certificate | Configure certificate activity as disabled or staging-only gated activity | Registrar / Moodle Admin | Certificate plugin candidate | No |
| 19 | Certificate | Add staging-only field map placeholders; do not publish final wording | Registrar | Step 18 | No |
| 20 | Admin hold | Configure admin hold field/log and require clear hold before certificate access | Compliance Lead | Step 18 | No |
| 21 | Optional support | Add optional clinical support landing page with no certificate restriction dependency | Instructional Designer | Step 4 | No |
| 22 | Optional support | Add optional confidence check as ungraded and not in required completion | Instructional Designer | Step 21 | No |
| 23 | Optional support | Add optional documentation support stub with PHI warning; do not require upload for certificate | Privacy Officer / Moodle Admin | Step 21 | No |
| 24 | Audit export | Configure audit export dry-run folder/process for profile, completion, time, interaction, quiz, affidavit, certificate, and optional status evidence | QA Lead / Moodle Admin | Steps 7-23 | No |
| 25 | QA users | Configure QA test users for missing fields, incomplete gates, failing exam, admin hold, optional skipped, and mobile path | QA Lead | Roles configured | No |
| 26 | QA execution | Run QA tracker and capture evidence | QA Lead | Steps 1-25 | No |
| 27 | Defect triage | Log defects and retest gate failures | QA Lead / Owners | Step 26 | No |
| 28 | Readiness decision | Decide whether staging certificate gate POC passes, fails, or requires fallback | Compliance Lead / Build Lead | Step 27 | No |
