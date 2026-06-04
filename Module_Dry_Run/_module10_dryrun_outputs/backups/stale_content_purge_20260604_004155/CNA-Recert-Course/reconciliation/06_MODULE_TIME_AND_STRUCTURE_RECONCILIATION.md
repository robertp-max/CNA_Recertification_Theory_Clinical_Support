# 06 — Module Time and Structure Reconciliation

## Purpose

Reconcile the 8 required theory modules (M00–M07) and their target minutes against the
720-minute / 12-hour required-theory model.

## Inputs Reviewed

- `CNA-Recert-Course\Content\00_EXECUTIVE_SUMMARY.md` (8-module structure; 12 h theory).
- `CNA-Recert-Course\Content\02_THEORY_SYLLABUS_TABLE.md`.
- `CNA-Recert-Course\Content\theory\modules\` (M00–M07 files present).
- `CNA-Recert-Course\ContentV2\10_CONTENT_COVERAGE_AND_TIME_RECONCILIATION.md`.

## Preserved Facts (unless stronger evidence contradicts)

- Required theory = **720 minutes / 12 hours**, asynchronous online, partial CA renewal CE only.
- Optional Clinical Support is separate, non-credit, non-gating.

## Evidence Table

| Module | Title | Target min | Repo source file | Status |
|---|---|---:|---|---|
| M00 | Orientation | 30 | `04_THEORY_MODULE_00_ORIENTATION_FULL.md` | In Progress |
| M01 | Infection Control | 90 | `05_THEORY_MODULE_01_INFECTION_CONTROL_FULL.md` | Needs SME Review |
| M02 | Resident Rights / Abuse Prevention | 120 | `24_THEORY_MODULE_02_..._FULL.md` | In Progress |
| M03 | Dementia / Communication / Cultural Respect | 120 | `25_THEORY_MODULE_03_..._FULL.md` | Needs Source Repair |
| M04 | Mobility / Falls / Workplace Safety | 120 | `26_THEORY_MODULE_04_..._FULL.md` | In Progress |
| M05 | Nutrition / Skin Integrity / Vital Signs | 120 | `27_THEORY_MODULE_05_..._FULL.md` | Needs SME Review |
| M06 | Documentation / Change of Condition / Scope | 90 | `28_THEORY_MODULE_06_..._FULL.md` | In Progress |
| M07 | Review / Final Exam / Affidavit | 30 | `29_THEORY_MODULE_07_..._FULL.md` | Needs Legal/CDPH Review |
| **TOTAL** | | **720** | | **= 12.0 h (matches model)** |

Sum check: 30 + 90 + 120 + 120 + 120 + 120 + 90 + 30 = **720 minutes**. ✔ matches the target model.

## Gaps Found

- Per-module minutes are a **design target**, not validated active time. Active-time validation is
  unresolved (see `08_...`).
- The source PDFs do not assert per-module minutes; timing is from the blueprint, not the export.

## Owner / Action Needed

- Instructional Designer: confirm ContentV2 lesson runtime estimates align to targets.
- Compliance: confirm time model is acceptable for the partial-credit claim.

## Blocker Status

Structure reconciles. Active-time **validation** remains a P0-adjacent compliance item.

## Next Verification Step

Compare `courseContentV2.json` per-module estimated minutes to this table.
