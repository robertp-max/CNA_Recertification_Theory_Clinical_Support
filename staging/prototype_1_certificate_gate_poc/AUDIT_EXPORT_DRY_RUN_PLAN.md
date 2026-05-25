# Audit Export Dry Run Plan

## Purpose

Prototype Build 1 must prove that required certificate-gate evidence can be exported or captured for review. This is a dry run only and does not establish production retention or final audit policy.

## Audit Matrix

| Audit Item | Prototype Source | Export Method | Required for Prototype? | Notes |
|---|---|---|---|---|
| Learner profile fields | Legal name and CNA certificate number profile fields | User profile CSV/export screenshot | Yes | Confirms certificate identity fields are present. |
| Identity confirmation | Required profile fields and orientation acknowledgement | Profile export plus acknowledgement attempt export | Yes | If separate identity acknowledgement is added later, include it here. |
| Online cap acknowledgement | Feedback or Quiz acknowledgement | Attempt/submission CSV or screenshot | Yes | Must show timestamp and learner. |
| Theory completion | Sample required theory activity | Activity completion report CSV | Yes | One activity is enough for Prototype 1. |
| Interaction record | Required interaction/check | Quiz/Lesson/H5P/Feedback attempt export | Yes | Must show learner submitted/attempted. |
| Active-time report or admin review record | Candidate time plugin or manual admin review hold | Time report CSV/PDF or admin review log export | Yes | Moodle logs alone are not enough. |
| Final exam/test record | Moodle Quiz placeholder | Quiz attempt/grade export | Yes | Must show pass/fail and timestamp. |
| Affidavit record | Feedback, Assignment, e-sign placeholder, or wet-sign placeholder | Submission export, file record, or admin review screenshot | Yes | Final method pending approval. |
| Certificate issue/lock status | Certificate plugin/equivalent and Restrict Access settings | Issue log export, lock screenshot, or staging PDF if generated | Yes | Certificate must remain disabled or staging-only until approval metadata exists. |
| Certificate fields populated | Certificate field map and staging template | Template screenshot or staging PDF marked test only | Yes | Do not use final certificate wording. |
| Admin hold status | Admin hold field/log | Hold log export or screenshot | Yes | Must show active hold blocks certificate and clear hold allows access after gates. |
| Approval metadata/staging override | Admin-only compliance archive placeholder | Admin archive screenshot or export | Yes | Production approval not assumed. |
| Optional clinical support status separately labeled | Optional support completion/report area | Separate optional support export or screenshot | Yes | Must not be merged into required online CE evidence. |
| Role permission evidence | Role test results | Screenshots/test notes | Yes | Unauthorized override must fail. |
| No-PHI confirmation | Optional documentation stub and PHI warning | Screenshot and QA note | Yes | Prototype must not collect PHI. |

## Dry-Run Procedure

1. Create at least two learner test accounts: one complete required path, one incomplete required gate.
2. Complete required gates for the passing test learner while skipping optional clinical support.
3. Attempt certificate access for negative-test learners with missing gates.
4. Export or screenshot each audit item in the matrix.
5. Store dry-run evidence in a dated QA evidence folder outside production learner records.
6. Log missing export fields as defects or blocker items.

## Pass Standard

The dry run passes only if each required audit item is exportable, screenshot-capturable, or represented by a documented manual admin review record.
