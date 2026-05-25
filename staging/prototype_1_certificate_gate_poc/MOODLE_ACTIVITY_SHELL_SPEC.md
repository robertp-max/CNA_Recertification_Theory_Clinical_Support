# Moodle Activity Shell Specification

## Prototype 1 Activity Shells

| Activity ID | Activity Name | Moodle Tool | Required / Optional / Admin Only | Completion Rule | Restrict Access Rule | Certificate Gate? | Notes |
|---|---|---|---|---|---|---|---|
| P1-A001 | Module 0: Start Here - Online CE Scope and Limits | Page | Required | Learner must view page or complete acknowledgement | Opens at course start | Yes | Include partial-credit, 48-hour, 12-hour annual, 24-hour online cap, no-PHI, and optional clinical separation summary. |
| P1-A002 | Required Certificate Information: Legal Name | User profile field | Required | Field present and not blank | Certificate restricted until present | Yes | Registrar review required for test data. |
| P1-A003 | Required Certificate Information: CNA Certificate Number | User profile field | Required | Field present and not blank | Certificate restricted until present | Yes | Local format validation may be staged later. |
| P1-A004 | Required: California Online CE Limit Acknowledgement | Feedback or Quiz | Required | Learner submits acknowledgement | Required before theory module and certificate | Yes | Uses draft acknowledgement copy pending review. |
| P1-A005 | Required Theory Module 1: Sample Content Shell | Page, Book, or Lesson | Required | View content or complete lesson shell | Requires orientation and online cap acknowledgement | Yes | Shell only; no final lesson content. |
| P1-A006 | Required Interaction and Feedback Check | Quiz, Lesson question, H5P, or Feedback | Required | Submit response/attempt | Requires sample theory module completion | Yes | Must create interaction evidence. |
| P1-A007 | Required Active Participation Time Control | Time plugin report or manual admin review hold | Required | Threshold met or admin review marked complete | Required before final exam and certificate | Yes | Plugin unvalidated until tests pass. Manual fallback allowed. |
| P1-A008 | Required Final Exam/Test Placeholder | Quiz | Required | Achieve grade-to-pass | Requires theory activity, interaction, active-time control, and no admin hold | Yes | Placeholder questions only; final test content out of scope. |
| P1-A009 | Required Final Signed Statement/Affidavit Placeholder | Feedback, Assignment, or approved e-sign placeholder | Required | Submit/complete statement | Requires final exam/test pass | Yes | Wording and e-sign method pending approval. |
| P1-A010 | Online CE Certificate - Staging Only / Disabled | Custom Certificate or equivalent | Required after gates | Issue record only in staging if enabled; otherwise blocked | Requires all gates and approval metadata/staging override | Target activity | Must be disabled or clearly staging-only until approval metadata exists. |
| P1-A011 | Admin-Only Approval Metadata Archive | Restricted Folder/Page | Admin Only | Admin record exists for staging override | Hidden from learners | Indirect | Production approval not assumed. |
| P1-A012 | Admin Hold Log / Compliance Hold | Restricted profile/course field or admin-only log | Admin Only | Hold clear before certificate access | Certificate restricted while hold active | Yes | Manual fallback can use this hold. |
| P1-A013 | Audit Packet Dry-Run Export Area | Admin-only folder/process | Admin Only | QA captures export files/screenshots | Hidden from learners | No direct gate | Used for dry-run evidence only. |
| P1-A014 | Optional Clinical Support: Start Here | Page | Optional | Optional or no completion | No required CE prerequisites; not in certificate restriction set | No | Optional clinical support, not required clinical hours, not graded. |
| P1-A015 | Optional Skills Refresh Stub | Page or Book | Optional | Optional or no completion | No certificate restriction | No | Optional skills refresh; not clinical-hour credit. |
| P1-A016 | Optional Confidence Check | Ungraded Quiz or Feedback | Optional | Optional completion only | No certificate restriction | No | Not graded, not a certificate gate, not clinical-hour credit. |
| P1-A017 | Optional Documentation Support Stub | Page or disabled/upload-off Assignment stub | Optional | Optional completion only if enabled | No certificate restriction | No | PHI warning required; do not collect PHI. |
| P1-A018 | Optional Help / Contact | Feedback or Page | Optional | No completion or optional | No certificate restriction | No | Support request does not affect certificate. |

## Configuration Notes

- Required online CE certificate requirements and optional clinical support must be visually separated.
- Optional clinical activities must be optional, not graded, not certificate gates, and not clinical-hour credit.
- Do not include optional clinical activities in required course completion aggregation.
- If a progress dashboard is used, configure separate progress areas for required online CE and optional clinical support.
