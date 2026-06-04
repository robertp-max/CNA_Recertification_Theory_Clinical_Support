# Moodle Course Shell Specification

**Scope:** Staging course shell only. Do not build final production configuration or final content until approval dependencies are closed.

---

## Recommended Category Structure

| Moodle Category / Course | Purpose | Notes |
|---|---|---|
| `California CNA Online CE` | Required theory CE pathway. | Certificate-enabled only after CDPH approval metadata is active. |
| `California CNA Optional Clinical Support` | Optional clinical support hub. | May be a separate linked course or clearly separated course section. Not a certificate gate by default. |
| `Admin - CNA CE Compliance Archive` | Restricted approval, certificate, audit, version records. | Admin-only; no learner access. |
| `Staging - CNA CE Prototype` | Prototype and QA build. | Use fake learner records only. |

## Theory CE Course Structure

Recommended course name in staging:

`CNA Recertification Online CE - 12 Hour Theory - Staging`

Learner-facing title after approval should include "Online CE" and "12 hours" but must not imply full renewal completion.

### Required Theory Sections

1. `Start Here: Course Scope, Identity, and Renewal Limits`
2. `Module 1: Infection Control and PPE`
3. `Module 2: Resident Rights, Abuse Prevention, and Boundaries`
4. `Module 3: Dementia, Communication, and Respectful Care`
5. `Module 4: Mobility, Falls, and Workplace Safety`
6. `Module 5: Nutrition, Skin Integrity, Vital Signs, and Observation`
7. `Module 6: Documentation, Reporting, PHI Avoidance, and Scope`
8. `Final Review, Exam/Test, Affidavit, and Certificate Status`

## Optional Clinical Support Hub Structure

Recommended name:

`Optional Clinical Support Hub - CNA Skills Refresh and Documentation Support`

Required learner-facing first line:

`This hub provides optional clinical support and documentation support. It is not California CNA renewal clinical-hour credit unless CI Institute of Nursing gives written CDPH-approved instructions.`

### Hub Sections

1. `Start Here: What This Is / What This Is Not`
2. `Skills Refresh Library`
3. `Practice Planner`
4. `Scheduling Guidance`
5. `What to Bring / What to Expect`
6. `Optional Confidence Checks`
7. `Documentation Support`
8. `RN/Preceptor Signoff Instructions`
9. `What Not to Upload: PHI Warning`
10. `Help / Office Hours / Contact`

## Naming Conventions

| Item Type | Convention | Example |
|---|---|---|
| Required theory activity | `REQ - [Module] - [Activity Name]` | `REQ - M1 - Infection Control Scenario Check` |
| Required certificate activity | `CERT - [Gate Name]` | `CERT - Final Signed Statement` |
| Optional clinical support | `OPT CLIN - [Activity Name]` | `OPT CLIN - Transfer Confidence Check` |
| Admin-only item | `ADMIN - [Item Name]` | `ADMIN - Approval Metadata Record` |
| QA-only staging item | `QA - [Test Name]` | `QA - Certificate Gate Negative Test Learner` |

## Required vs Optional Visual Labels

Use these exact label prefixes in staging:

- `Required for Online CE Certificate:`
- `Optional Clinical Support:`
- `Optional Practice / Confidence Check:`
- `Admin Only:`
- `Not for Clinical-Hour Credit:`

## Learner Dashboard Requirements

The learner dashboard should show:

- Next required theory step.
- Online CE completion status.
- Active participation status.
- Final exam/test status.
- Affidavit status.
- Certificate status.
- Optional Clinical Support Hub link.

The dashboard must not show optional clinical progress as part of required CE completion percentage.

## Admin-Facing Labels

Admin labels must make gate purpose explicit:

- `Certificate Gate - Required`.
- `Support Only - Not Certificate Gate`.
- `Clinical Support - Not California Renewal Clinical Credit`.
- `Approval Metadata Required Before Certificate Release`.
- `Active-Time Validation Pending`.

## Mobile-First Layout Rules

1. One clear "next step" button or link per section.
2. Avoid wide tables in learner-facing content.
3. Avoid required video.
4. Use short pages and Books with descriptive headings.
5. Put disclaimers above risky actions, not buried below them.
6. Use large tap targets for quizzes/forms.
7. Keep optional clinical support visually separate from required CE.

## What Must Not Appear in Learner Progress Bar

Hard rule: do not combine required CE progress and optional clinical support progress into one misleading progress score.

Exclude from the required online CE progress bar:

- Optional clinical confidence checks.
- Optional clinical upload portal.
- RN/preceptor signoff support.
- Scheduling requests.
- Skills refresh library pages unless they are explicitly approved and configured as required theory CE content.
- Simulation/LTI practice.
- Support request forms.
- Office hours attendance.

## Course Area Map

| Course Area | Required or Optional | Moodle Tool | Learner Label | Completion Rule | Certificate Gate? | Notes |
|---|---|---|---|---|---|---|
| Orientation scope page | Required | Page | Required for Online CE Certificate: Start Here | View + acknowledgement activity | Yes | Includes partial-credit and non-PHI overview. |
| Legal name profile field | Required | User profile field | Required Certificate Information: Legal Name | Field must be populated | Yes | Registrar review for corrections. |
| CNA certificate number | Required | User profile field | Required Certificate Information: CNA Certificate Number | Field must be populated | Yes | Required for certificate. |
| Online cap acknowledgement | Required | Quiz or Feedback | Required: California Online CE Limit Acknowledgement | Submit acknowledgement | Yes | Learner acknowledges 24-hour online cap. |
| Theory module content | Required | Book/Page/Lesson | Required Theory Module | Completion per activity | Yes | Must map to approved course list. |
| Required interaction | Required | Lesson/Quiz/H5P | Required Interaction and Feedback | Attempt/complete activity | Yes | Must produce meaningful feedback. |
| Active-time status | Required | Validated time plugin/custom hold | Required Active Participation Time | Threshold met or admin reviewed | Yes | Plugin candidate until validated. |
| Final exam/test | Required | Quiz | Required Final Exam/Test | Pass approved threshold | Yes | Exact threshold needs approval. |
| Final signed statement | Required | Feedback/Assignment/custom/wet-sign process | Required Final Signed Statement | Completed by approved method | Yes | E-sign acceptance not assumed. |
| Certificate | Required after gates | Custom Certificate/equivalent | Certificate Available After Required Steps | Release only after all gates | N/A | Disabled until approval metadata active. |
| Clinical hub overview | Optional | Page/Book | Optional Clinical Support: Start Here | Optional view | No | Must state non-credit boundary. |
| Skills refresh library | Optional | Book/File/Page | Optional Skills Refresh | Optional completion or no tracking | No | Do not inflate CE progress. |
| Practice planner | Optional | Page/Choice/Calendar | Optional Practice Planner | Optional | No | Scheduling support only. |
| Optional confidence checks | Optional | Feedback/Ungraded Quiz/H5P | Optional Confidence Check | Optional; no grade gate | No | Must not affect certificate. |
| Documentation support upload | Optional | Assignment/Database | Optional Documentation Support Upload | Optional submission | No | Non-PHI warning required. |
| RN/preceptor instructions | Optional | Page/File/Assignment | Optional RN/Preceptor Signoff Instructions | Optional | No | Signoff support, not CE gate. |
| Admin approval metadata | Admin Only | Restricted file/custom field | Admin Only: Approval Metadata | Admin review | Yes indirectly | Certificate disabled if absent. |
| Manual override log | Admin Only | Restricted form/log | Admin Only: Override Log | Required if override used | Yes indirectly | Override must be documented. |
