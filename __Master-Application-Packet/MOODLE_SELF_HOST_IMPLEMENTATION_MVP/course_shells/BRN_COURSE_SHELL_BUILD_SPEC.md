# BRN Course Shell Build Spec

Status: Pending BRN CEP approval. Provider-approval framing (not course-by-course). Contact hours, not CEUs. No certification claim; no scope-expansion claim. No 4-contact-hour language.

- Category: `CI-BRN-CM`
- Course short name: `BRN-CM-30`
- Course full name: "RN Case Management in Home Health - 30 Contact Hours (10 Modules) [Pending BRN CEP Approval]"
- Format: Topics; completion tracking ON.
- 10 modules x 3 contact hours = 30 contact hours; 50 instructional minutes per contact hour; >= 1,500 instructional minutes total (>= 150 min/module).

## Modules (section / title / quiz category)
- M01 / Foundations of RN Case Management and Nursing Scope / `BRN/M01`
- M02 / Assessment, Intake, and Patient-Centered Care Planning / `BRN/M02`
- M03 / Care Coordination Across Disciplines and Settings / `BRN/M03`
- M04 / Documentation, Legal Charting, and Audit-Ready Records / `BRN/M04`
- M05 / Patient Rights, Consent, Advocacy, and Ethical Boundaries / `BRN/M05`
- M06 / Transitions of Care, Discharge Planning, Community Resources / `BRN/M06`
- M07 / Utilization Review, Medical Necessity, Payer-Safe Communication / `BRN/M07`
- M08 / Quality Assurance, Risk Management, Incident Reporting, Escalation / `BRN/M08`
- M09 / Chronic Disease, Geriatric, and High-Risk Patient Management / `BRN/M09`
- M10 / Integrated Case Management Capstone / `BRN/M10`

## Per-module build (M01-M10)
1. `M## - Objectives` (Page) - require view; restrict: prior module complete (M02-M10).
2. `M## - Timed Content` (Lesson/Book) - require view + seat-time guidance (>=150 min/module); restrict: Objectives complete.
3. `M## - Case Scenario` (Assignment) - require submission; restrict: Content complete.
4. `M## - Documentation/Decision Activity` (Assignment) - require submission; restrict: Case Scenario complete.
5. `M## - Module Quiz` (Quiz, `BRN/M##`, 12-item bank) - require passing grade (>=80%); restrict: Documentation activity complete.

Module complete = all 5 complete (quiz passed).

## Capstone / Final
- `Capstone Final Assessment` (Quiz, `BRN/CAPSTONE_FINAL`, 30-item bank) - require passing grade (>=80%); restrict: all M01-M10 complete.
- Course completion = all modules complete + Capstone passed.

## Gradebook
- Module Quizzes (50%), Module Activities (20%), Capstone Final (30%).

## Certificate gate dependency
- Course complete + Capstone passed + approval metadata flag (post-approval only). BRN certificate uses "contact hours" (30); never CEUs (except "not CEUs" explanatory wording). No certification/scope claim.

## Quiz bank categories
- `BRN/M01`...`BRN/M10`, `BRN/CAPSTONE_FINAL` (import from `import_assets/BRN_GIFT_QUESTION_BANK.gift`).
