# Required / Optional Activity Map

**Purpose:** Prevent optional support features from becoming certificate gates and prevent optional activity progress from inflating required online CE progress.

---

## Configuration Rules

- Required theory CE activities may appear in required progress and certificate gate logic.
- Required certificate activities may gate certificate release.
- Optional clinical support activities must not gate online CE certificate release by default.
- Optional support resources must not inflate required CE progress.
- Admin-only activities must not be visible to learners.
- Optional clinical confidence checks should not affect certificate completion.
- Optional clinical support uploads should not affect online CE certificate completion.

## Activity Map

| Activity | Required / Optional / Admin Only | Moodle Tool | Learner-Facing Label | Completion Tracking? | Certificate Gate? | Risk if Misconfigured |
|---|---|---|---|---|---|---|
| Course scope orientation page | Required | Page | Required for Online CE Certificate: Start Here | Yes | Yes | Learner may miss partial-credit limits. |
| Legal name field | Required | User profile | Required Certificate Information: Legal Name | Yes, via profile check | Yes | Certificate issued with wrong/missing name. |
| CNA certificate number field | Required | User profile | Required Certificate Information: CNA Certificate Number | Yes, via profile check | Yes | Certificate lacks required learner identifier. |
| Online cap acknowledgement | Required | Quiz/Feedback | Required: California Online CE Limit Acknowledgement | Yes | Yes | Learner may exceed 24-hour online cap. |
| No-PHI acknowledgement | Required for upload areas; recommended in orientation | Quiz/Feedback | Required Privacy Acknowledgement | Yes where configured | Yes only if part of required theory path | PHI risk and unclear privacy obligations. |
| Theory module reading | Required | Book/Page/Lesson | Required Theory Module | Yes | Yes | Learner bypasses required content. |
| Theory interaction | Required | Lesson/H5P/Quiz | Required Interaction and Feedback | Yes | Yes | Online CE interaction evidence missing. |
| Module quiz | Required | Quiz | Required Module Check | Yes | Yes if configured in module completion | Weak mastery evidence. |
| Active-time threshold | Required | Time plugin/custom/manual review | Required Active Participation Time | Yes | Yes | Time control requirement unsupported. |
| Final exam/test | Required | Quiz | Required Final Exam/Test | Yes | Yes | Certificate without assessment evidence. |
| Final signed statement/affidavit | Required | Feedback/Assignment/custom/wet-sign | Required Final Signed Statement | Yes | Yes | Certificate issued without required statement. |
| Certificate activity | Required after gates | Custom Certificate/equivalent | Online CE Certificate | Issue record | N/A | Premature or incomplete certificate. |
| Admin hold | Admin Only | Restricted profile/course field | Not learner-facing except status message | Yes | Yes | Known exception still receives certificate. |
| Manual override log | Admin Only | Restricted form/log | Not learner-facing | Yes if used | Yes indirectly | Undocumented exception. |
| Clinical support overview | Optional | Page/Book | Optional Clinical Support: Start Here | Optional or no | No | Learner thinks clinical hub is required credit. |
| Skills Refresh Library | Optional | Book/Page/File | Optional Skills Refresh | Optional or no | No | Optional support inflates CE progress. |
| Practice Planner | Optional | Page/Choice | Optional Practice Planner | Optional | No | Scheduling support mistaken for required clinical hours. |
| Scheduling Guidance | Optional | Page/Calendar/Scheduler candidate | Optional Scheduling Guidance | Optional | No | Capacity confusion or plugin burden. |
| What to Bring / What to Expect | Optional | Page/File | Optional Practice Support Resource | Optional or no | No | Learner thinks attendance is required for CE certificate. |
| Transfer confidence check | Optional | Feedback/Ungraded Quiz | Optional Confidence Check: Transfers | Optional | No | Confidence check becomes punitive. |
| Hand hygiene/PPE confidence check | Optional | H5P/Ungraded Quiz | Optional Confidence Check: PPE | Optional | No | Simulation/practice mistaken for clinical hours. |
| Documentation practice | Optional | Ungraded Quiz/Feedback | Optional Practice: Documentation | Optional | No | Free text may collect PHI. |
| Clinical documentation upload | Optional | Assignment/Database | Optional Documentation Support Upload | Optional | No | Missing upload blocks certificate or PHI collected. |
| RN/preceptor signoff upload | Optional | Assignment/Database | Optional RN/Preceptor Signoff Support | Optional | No | Signoff treated as state-required validation. |
| Simulation/LTI practice | Optional / Post-MVP | External Tool/H5P | Optional Practice Scenario - Not Clinical Hours | Optional | No | Simulation counted as clinical credit. |
| Support request form | Optional | Feedback/Form | Optional Help Request | No or optional | No | Learners avoid support if it appears graded. |
| Office hours booking | Optional | Calendar/Scheduler | Optional Office Hours | Optional | No | Attendance becomes perceived requirement. |
| Approval archive | Admin Only | Restricted Folder | Admin Only | N/A | Yes indirectly | Learners see admin docs or certificate unblocked without approval. |
| Audit packet export | Admin Only | Reports/custom SQL/manual export | Admin Only | N/A | No direct learner gate | Records incomplete for audit. |
| PHI incident log | Admin Only | Restricted log | Admin Only | N/A | No | Privacy response not documented. |

## Progress Bar Rule

If a progress block/dashboard is used, create separate progress sections:

1. `Online CE Certificate Requirements`.
2. `Optional Clinical Support`.

Never merge these into a single percentage.
