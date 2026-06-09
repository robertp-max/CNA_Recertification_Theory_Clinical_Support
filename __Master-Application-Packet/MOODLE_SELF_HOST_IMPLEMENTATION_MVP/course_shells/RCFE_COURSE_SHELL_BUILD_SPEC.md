# RCFE Course Shell Build Spec

Status: Draft / Pending Approval. Controlling structure = filed 9 LIC 9140 courses / 27 hours. The 40-hour/12-module concept is FUTURE EXPANSION ONLY - do not build it as the current structure.

- Category: `CI-RCFE-CETP`
- One Moodle course per LIC 9140 course (9 total). Completion tracking ON; Topics format.

## Courses (short name / full name / hours / quiz category)
- RCFE-CETP-001 / Laws, Regulations, Policies, and Procedural Standards / 4h / `RCFE/RCFE-CETP-001`
- RCFE-CETP-002 / Alzheimer's/Dementia: Person-Centered Care Foundations / 4h / `RCFE/RCFE-CETP-002`
- RCFE-CETP-003 / Alzheimer's/Dementia: Safety, Environment, Documentation / 4h / `RCFE/RCFE-CETP-003`
- RCFE-CETP-004 / Resident Rights, Dignity, Councils, Abuse Prevention / 2h / `RCFE/RCFE-CETP-004`
- RCFE-CETP-005 / Medication Management in RCFE Operations / 4h / `RCFE/RCFE-CETP-005`
- RCFE-CETP-006 / Admission, Retention, Reappraisal, Needs and Services Plans / 3h / `RCFE/RCFE-CETP-006`
- RCFE-CETP-007 / Emergency Procedures and Physical Environment Controls / 2h / `RCFE/RCFE-CETP-007`
- RCFE-CETP-008 / Staff Supervision, Training Records, Administrator Accountability / 2h / `RCFE/RCFE-CETP-008`
- RCFE-CETP-009 / Business Operations, Records, Claim-Safe Communications / 2h / `RCFE/RCFE-CETP-009`

Total = 27 hours. Dementia coverage concentrated in 002 and 003.

## Per-course build (each of the 9)
1. `Overview` (Page) - require view.
2. `Objectives` (Page) - require view; restrict: Overview complete.
3. `Timed Content` (Lesson/Book) - require view + seat-time guidance (hours x 50 min target); restrict: Objectives complete.
4. `Checkpoint` (interaction) - require interaction; restrict: Content complete.
5. `Scenario / Admin Judgment` (Assignment) - require submission; restrict: Checkpoint complete.
6. `Final Assessment` (Quiz, `RCFE/RCFE-CETP-00X`, 15-item bank) - require passing grade (>=70%); restrict: Scenario complete.
7. `Participant Evaluation` (Feedback) - require submission; restrict: Final passed.
8. `Attestation` (Choice/Feedback) - require submission; restrict: Evaluation complete. Text from GENERATED_ATTESTATION_TEXTS.md.
9. Course completion = all required activities complete + final passed + evaluation + attestation.

## Gradebook (per course)
- Course Final (80%), Scenario/Judgment (20%).

## Certificate gate dependency
- Completion + final passed + evaluation + attestation + approval metadata flag (post-approval only). RCFE certificate must match CDSS-approved terms.

## Quiz bank categories
- `RCFE/RCFE-CETP-001`...`009` (import from `import_assets/RCFE_GIFT_QUESTION_BANK.gift`).
