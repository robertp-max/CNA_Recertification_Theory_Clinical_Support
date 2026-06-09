# CNA Course Shell Build Spec

Status: Draft / Pending Approval. Online CE only; no clinical hours; no hands-on competency validation; no full 48-hour renewal claim.

- Category: `CI-CNA-CE`
- Course short name: `CNA-CE-24`
- Course full name: "CI Institute of Nursing - CNA Continuing Education (12 Units / 24 Online CE Hours) [Draft / Pending Approval]"
- Format: Topics; completion tracking ON.
- Section groups: "Year 1 (U01-U06, 12 hours)", "Year 2 (U07-U12, 12 hours)", "Comprehensive Final Assessment".

## Per-unit build (U01-U12)

For each unit section, create activities in this order with completion + restrict-access:
1. `U## - Overview` (Page) - require view.
2. `U## - Objectives` (Page) - require view; restrict: Overview complete.
3. `U## - Content` (Lesson/Resource/Book) - require view + seat-time guidance (~100 min/unit); restrict: Objectives complete.
4. `U## - Checkpoint` (H5P/Choice/short activity) - require interaction; restrict: Content complete.
5. `U## - Unit Quiz` (Quiz, questions from `CNA/U##`) - require passing grade (>=80%); restrict: Checkpoint complete.
6. `U## - Scenario` (Assignment) - require submission; restrict: Unit Quiz passed.
7. `U## - Attestation` (Choice/Feedback) - require submission; restrict: Scenario complete. Text from GENERATED_ATTESTATION_TEXTS.md.

Unit complete = all 7 complete (quiz passed). U02-U12 restricted by previous unit completion.

## Final
- `Comprehensive Final Assessment` (Quiz, `CNA/FINAL`, 50-item bank) - require passing grade (>=80%); restrict: all U01-U12 complete.

## Source module mapping
- U01/U02->M10; U03->M11; U04->M12; U05/U06->M13; U07->M14; U08/U09->M15; U10->M16; U11/U12->M17.

## Gradebook
- Categories: Unit Quizzes (60%), Scenario/Documentation (10%), Final Assessment (30%).

## Certificate gate dependency
- Course complete + Final passed + attestation + approval metadata flag (post-approval only). CNA certificate states online CE hours only (no clinical hours).

## Quiz bank categories
- `CNA/U01`...`CNA/U12`, `CNA/FINAL` (import from `import_assets/CNA_GIFT_QUESTION_BANK.gift`).
