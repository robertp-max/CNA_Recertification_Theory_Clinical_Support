# Prototype 1 Build Plan

## Exact Scope

Prototype Build 1 proves the certificate gate path only. It uses a staging Moodle course shell with minimal representative activities and placeholder controls. It does not create final content, production configuration, custom plugins, or final certificate issuance.

## Governing Rules

- The 12-hour Moodle theory course is partial renewal credit only.
- California CNA renewal requires 48 hours over 2 years, with at least 12 hours each year.
- Only 24 hours may be completed online through CDPH-approved online CE.
- Optional clinical support is support/documentation only unless CDPH gives written approval.
- Optional clinical support, optional confidence checks, optional documentation support, simulation, virtual simulation, and LTI simulation must not gate the online CE certificate by default.
- Active-time tools/plugins are unvalidated until staging tests pass.
- Moodle logs alone are not enough.

## Prototype Component Matrix

| Prototype Component | Purpose | Moodle Tool / Process | Required or Optional | Certificate Gate? | Evidence Created | QA Test |
|---|---|---|---|---|---|---|
| Orientation page | Explain scope, partial-credit limits, required path, no-PHI rule, and optional clinical separation | Page | Required | Yes | Page completion record | QA-004, QA-005 |
| Legal name field | Populate required learner certificate identity | Required user profile field | Required | Yes | User profile export | QA-002 |
| CNA certificate number field | Populate required learner certificate identifier | Required user profile field | Required | Yes | User profile export | QA-003 |
| Online cap acknowledgement | Confirm learner understands 24-hour online CE cap | Feedback or Quiz acknowledgement | Required | Yes | Timestamped acknowledgement export | QA-004 |
| One required theory content activity | Represent required online CE theory completion | Page, Book, or Lesson | Required | Yes | Activity completion report | QA-005 |
| One required interaction/check | Create interaction/feedback evidence | Quiz, Lesson question, H5P, or Feedback | Required | Yes | Attempt/completion record | QA-006 |
| Active-time threshold placeholder/control | Prove active participation evidence can gate final exam/certificate or trigger admin hold | Candidate time plugin, report, or manual admin review hold | Required | Yes | Time report or admin review record | QA-007, AT-P1-001 to AT-P1-010 |
| Final exam/test placeholder | Prove assessment pass condition gates certificate | Moodle Quiz with grade-to-pass | Required | Yes | Quiz attempt, score, timestamp | QA-008, QA-020 |
| Final signed statement/affidavit placeholder | Prove final statement completion blocks certificate until complete | Feedback, Assignment, or approved e-sign placeholder | Required | Yes | Statement completion record or admin review record | QA-009 |
| Certificate activity disabled or gated | Prove certificate cannot release early and remains staging-only | Custom Certificate/equivalent with Restrict Access and disabled production status | Required after gates | N/A; target activity | Lock/issue status, template field map | QA-001, QA-015, QA-019 |
| Optional clinical support landing page | Prove optional support is separate and not required for certificate | Page or section label | Optional | No | Optional page access/completion if enabled | QA-011 |
| Optional confidence check | Prove optional checks are not graded and do not gate certificate | Ungraded Quiz or Feedback | Optional | No | Optional attempt record separately labeled | QA-012 |
| Optional documentation support stub | Provide non-PHI documentation support placeholder without certificate impact | Page or disabled/upload-off Assignment stub | Optional | No | Optional status separately labeled | QA-013 |
| Audit packet dry-run export | Prove required gate evidence can be exported | Moodle reports, plugin exports, screenshots, admin logs | Admin Only | No direct learner gate | Dry-run export folder/checklist | Audit dry run |

## Prototype Output

The prototype is complete when QA can demonstrate both failure and success paths: incomplete required gates block certificate release, completed required gates allow staging-only certificate availability, and skipped optional clinical support does not block the certificate.
