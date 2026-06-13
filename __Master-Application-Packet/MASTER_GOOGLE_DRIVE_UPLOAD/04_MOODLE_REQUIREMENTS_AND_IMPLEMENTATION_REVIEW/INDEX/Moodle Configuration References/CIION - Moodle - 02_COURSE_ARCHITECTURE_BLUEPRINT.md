# 02 - Course Architecture Blueprint (All Three Lanes)

Status: Draft / Pending Approval. Controlling source: master application packet (`00_FINAL_COURSE_ALIGNMENT_AUDIT.md`).

Recommended Moodle category structure:
- `CI-CNA-CE` (CNA / CDPH CE)
- `CI-RCFE-CETP` (RCFE / CDSS CETP)
- `CI-BRN-CM` (BRN / CEP RN Case Management)

Use the Topics format with one section per unit/module/course as described below. Turn on "Enable completion tracking" at site and course level. Set restrict-access dependencies per `import_assets/RESTRICT_ACCESS_RULES_REFERENCE.csv`.

---

## CNA / CDPH CE - one Moodle course recommended for the MVP

- Course short name: `CNA-CE-24`; full name: "CI Institute of Nursing - CNA Continuing Education (12 Units / 24 Online CE Hours) [Draft / Pending Approval]".
- 12 units U01-U12; each unit = 2 online CE hours (total 24).
- Section groups: "Year 1 (U01-U06, 12 hours)" and "Year 2 (U07-U12, 12 hours)" - implemented as labeled section dividers or two section ranges.
- Online CE only; no clinical hours; no hands-on competency validation.

Per-unit activity pattern (sequential, completion-gated):
1. Overview page
2. Objectives page
3. Lesson/Resource (content)
4. Interaction/checkpoint
5. Quiz (unit quiz bank)
6. Scenario/documentation activity
7. Attestation
8. Completion gate (unit complete when all above complete and quiz passed)

Plus a comprehensive Final Assessment gated behind all 12 units.

Source module mapping (backbone, CCCCO/NATP Modules 10-17):
- U01, U02 -> Module 10 (Vital Signs)
- U03 -> Module 11 (Nutrition)
- U04 -> Module 12 (Emergency Procedures)
- U05, U06 -> Module 13 (Long Term Care Patient/Resident)
- U07 -> Module 14 (Rehabilitative Nursing)
- U08, U09 -> Module 15 (Observation and Charting)
- U10 -> Module 16 (Death and Dying)
- U11, U12 -> Module 17 (Patient/Resident Abuse)

Detailed shell spec: `course_shells/CNA_COURSE_SHELL_BUILD_SPEC.md`.

---

## RCFE / CDSS CETP - 9 separate Moodle courses (filed LIC 9140 list)

Nine courses matching the filed LIC 9140 set (no 40-hour substitution):
- RCFE-CETP-001 - Laws, Regulations, Policies, and Procedural Standards (4h)
- RCFE-CETP-002 - Alzheimer's/Dementia: Person-Centered Care Foundations (4h)
- RCFE-CETP-003 - Alzheimer's/Dementia: Safety, Environment, and Documentation (4h)
- RCFE-CETP-004 - Resident Rights, Dignity, Councils, and Abuse Prevention (2h)
- RCFE-CETP-005 - Medication Management in RCFE Operations (4h)
- RCFE-CETP-006 - Admission, Retention, Reappraisal, and Needs and Services Plans (3h)
- RCFE-CETP-007 - Emergency Procedures and Physical Environment Controls (2h)
- RCFE-CETP-008 - Staff Supervision, Training Records, and Administrator Accountability (2h)
- RCFE-CETP-009 - Business Operations, Records, and Claim-Safe Communications (2h)

Total = 27 hours. Dementia-specific coverage is concentrated in RCFE-CETP-002 and RCFE-CETP-003.

Per-course activity pattern (sequential, completion-gated):
1. Overview
2. Objectives
3. Timed content sections
4. Interaction/checkpoint
5. Scenario/admin judgment exercise
6. Quiz/final assessment
7. Evaluation (participant course evaluation)
8. Attestation
9. Completion evidence (course completion)

Note: The 40-hour / 12-module RCFE Administrator Renewal program is FUTURE EXPANSION ONLY and is NOT part of this submission or controlling structure. Do not build it as the current structure.

Detailed shell spec: `course_shells/RCFE_COURSE_SHELL_BUILD_SPEC.md`.

---

## BRN / CEP RN Case Management - one 30-contact-hour Moodle course recommended for the MVP

- Course short name: `BRN-CM-30`; full name: "RN Case Management in Home Health - 30 Contact Hours (10 Modules) [Pending BRN CEP Approval]".
- 10 modules x 3 contact hours = 30 contact hours.
- 50 instructional minutes minimum per contact hour; 30 contact hours = at least 1,500 instructional minutes (design target ~1,680 minutes).
- Contact hours, not CEUs. Provider (CEP) approval framing. No certification or scope-expansion claim.

Modules:
- M01 Foundations of RN Case Management and Nursing Scope
- M02 Assessment, Intake, and Patient-Centered Care Planning
- M03 Care Coordination Across Disciplines and Settings
- M04 Documentation, Legal Charting, and Audit-Ready Records
- M05 Patient Rights, Consent, Advocacy, and Ethical Boundaries
- M06 Transitions of Care, Discharge Planning, and Community Resources
- M07 Utilization Review, Medical Necessity, and Payer-Safe Communication
- M08 Quality Assurance, Risk Management, Incident Reporting, and Escalation
- M09 Chronic Disease, Geriatric, and High-Risk Patient Management
- M10 Integrated Case Management Capstone

Per-module activity pattern (sequential, completion-gated):
1. Objectives
2. Timed content (>= 150 instructional minutes per 3-contact-hour module target)
3. Case scenario
4. Documentation/decision activity
5. Quiz (module quiz bank)
6. Completion evidence

Plus a Capstone/Final Assessment gate behind all 10 modules.

Detailed shell spec: `course_shells/BRN_COURSE_SHELL_BUILD_SPEC.md`.
