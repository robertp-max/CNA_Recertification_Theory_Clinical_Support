# 11 - Course Shell Build Specifications

Status: Draft / Pending Approval. Consolidated build specs for all three lanes. Lane-specific detail also in `course_shells/`.

Common per-activity completion pattern is defined in `import_assets/COMPLETION_RULES_IMPORT_REFERENCE.csv`; restrict-access in `import_assets/RESTRICT_ACCESS_RULES_REFERENCE.csv`; gradebook in `import_assets/GRADEBOOK_SETUP_REFERENCE.csv`.

## CNA - 12 units (one course)

- Moodle category: `CI-CNA-CE`
- Course short name: `CNA-CE-24`
- Course full name: "CI Institute of Nursing - CNA Continuing Education (12 Units / 24 Online CE Hours) [Draft / Pending Approval]"
- Section names: "Year 1" then U01-U06; "Year 2" then U07-U12; plus "Comprehensive Final Assessment".
- Activity list per unit: Overview page; Objectives page; Lesson/Resource; Interaction/checkpoint; Unit Quiz; Scenario/documentation activity; Attestation.
- Timing evidence expectation: ~100 min per 2-hour unit (50 min/CE hour target; confirm seat-time policy); activity-completion + time-in-activity guidance.
- Completion condition (unit): all activities complete + unit quiz passed (>=80%).
- Quiz bank category: `CNA/U01`...`CNA/U12`; final `CNA/FINAL`.
- Gradebook category: "Unit Quizzes" (60%), "Scenario/Documentation" (10%), "Final Assessment" (30%).
- Certificate gate dependency: course complete + Final passed + attestation + approval metadata flag (post-approval only).

| unit | full name | source module | quiz category |
| --- | --- | --- | --- |
| U01 | Vital Signs I | Module 10 | CNA/U01 |
| U02 | Vital Signs II | Module 10 | CNA/U02 |
| U03 | Nutrition, Hydration, Diets, Feeding, Aspiration | Module 11 | CNA/U03 |
| U04 | Emergency Procedures, Distress, Choking, Codes | Module 12 | CNA/U04 |
| U05 | LTC Resident I: Aging, Body Systems, Conditions | Module 13 | CNA/U05 |
| U06 | LTC Resident II: Dementia-Sensitive, Psychosocial | Module 13 | CNA/U06 |
| U07 | Rehabilitative Nursing and Restorative Care | Module 14 | CNA/U07 |
| U08 | Observation and Charting I | Module 15 | CNA/U08 |
| U09 | Observation and Charting II (Legal Documentation) | Module 15 | CNA/U09 |
| U10 | Death and Dying | Module 16 | CNA/U10 |
| U11 | Resident Abuse I | Module 17 | CNA/U11 |
| U12 | Resident Abuse II (Mandated Reporting) | Module 17 | CNA/U12 |
| FINAL | Comprehensive Final Assessment | Modules 10-17 | CNA/FINAL |

## RCFE - 9 courses

- Moodle category: `CI-RCFE-CETP`
- One Moodle course per LIC 9140 course (short names = RCFE-CETP-001..009; full names per COURSE_SHELL_NAMING_CONVENTIONS.csv).
- Section names per course: Overview; Objectives; Timed Content; Interaction/Checkpoint; Scenario/Admin Judgment; Final Assessment; Evaluation; Attestation; Completion.
- Timing evidence expectation: hours x 50 min target (e.g., 4h = 200 min); activity-completion + time guidance.
- Completion condition: all activities complete + final passed (>=70%) + evaluation + attestation.
- Quiz bank category: `RCFE/RCFE-CETP-00X`.
- Gradebook category: "Course Final" (80%), "Scenario/Judgment" (20%).
- Certificate gate dependency: completion + final passed + evaluation + attestation + approval metadata flag (post-approval only); certificate must match approved terms.

| course | hours | quiz category | dementia focus |
| --- | --- | --- | --- |
| RCFE-CETP-001 Laws/Regulations | 4 | RCFE/RCFE-CETP-001 | no |
| RCFE-CETP-002 Dementia Foundations | 4 | RCFE/RCFE-CETP-002 | yes |
| RCFE-CETP-003 Dementia Safety/Env/Doc | 4 | RCFE/RCFE-CETP-003 | yes |
| RCFE-CETP-004 Resident Rights | 2 | RCFE/RCFE-CETP-004 | no |
| RCFE-CETP-005 Medication Management | 4 | RCFE/RCFE-CETP-005 | no |
| RCFE-CETP-006 Admission/Retention | 3 | RCFE/RCFE-CETP-006 | no |
| RCFE-CETP-007 Emergency/Environment | 2 | RCFE/RCFE-CETP-007 | no |
| RCFE-CETP-008 Staff Supervision | 2 | RCFE/RCFE-CETP-008 | no |
| RCFE-CETP-009 Business Operations | 2 | RCFE/RCFE-CETP-009 | no |

Total = 27 hours. Do NOT build the 40-hour/12-module concept as the current structure.

## BRN - 10 modules (one course)

- Moodle category: `CI-BRN-CM`
- Course short name: `BRN-CM-30`
- Course full name: "RN Case Management in Home Health - 30 Contact Hours (10 Modules) [Pending BRN CEP Approval]"
- Section names: M01-M10 (titles below); plus "Capstone Final Assessment".
- Activity list per module: Objectives; Timed content; Case scenario; Documentation/decision activity; Module Quiz.
- Timing evidence expectation: >= 150 instructional minutes per 3-contact-hour module (50 min/contact hour); 10 modules = at least 1,500 minutes.
- Completion condition (module): all activities complete + module quiz passed (>=80%).
- Quiz bank category: `BRN/M01`...`BRN/M10`; capstone `BRN/CAPSTONE_FINAL`.
- Gradebook category: "Module Quizzes" (50%), "Module Activities" (20%), "Capstone Final" (30%).
- Certificate gate dependency: course complete + Capstone passed + approval metadata flag (post-approval only). Contact hours, not CEUs; no certification/scope claim.

| module | full name | quiz category |
| --- | --- | --- |
| M01 | Foundations of RN Case Management and Nursing Scope | BRN/M01 |
| M02 | Assessment, Intake, and Patient-Centered Care Planning | BRN/M02 |
| M03 | Care Coordination Across Disciplines and Settings | BRN/M03 |
| M04 | Documentation, Legal Charting, and Audit-Ready Records | BRN/M04 |
| M05 | Patient Rights, Consent, Advocacy, and Ethical Boundaries | BRN/M05 |
| M06 | Transitions of Care, Discharge Planning, Community Resources | BRN/M06 |
| M07 | Utilization Review, Medical Necessity, Payer-Safe Communication | BRN/M07 |
| M08 | Quality Assurance, Risk Management, Incident Reporting, Escalation | BRN/M08 |
| M09 | Chronic Disease, Geriatric, and High-Risk Patient Management | BRN/M09 |
| M10 | Integrated Case Management Capstone | BRN/M10 |
| CAPSTONE_FINAL | Comprehensive Capstone Final Assessment | BRN/CAPSTONE_FINAL |
