# 11_CONTENTV2_REBUILD_AUDIT.md
# ContentV2 Rebuild Audit — Instructional Depth & Time Reconciliation

**Branch:** `content-v2-codex-gpt55-orchestration`
**Audit date:** 2026-06-01
**Auditor role:** Instructional design architect / CNA-NATP conversion / compliance reviewer / content-data engineer / QA lead
**Source of truth:** `CNA-Recert-Course/Content` (ContentV1) + NATP curriculum PDFs in `CNA-Recert-Course/CNA_Modules/`
**Subject:** `CNA-Recert-Course/ContentV2` canonical data (`data/courseContentV2.json`, mirrored to `.ts` and to `standalone-course-mvp/src/data/contentV2.generated.ts`)

> This audit is descriptive and read-only. No content was changed to produce it. All counts are measured directly from `courseContentV2.json` and the narration manifests, not estimated.

---

## 0. Executive finding

ContentV2 is **structurally valid but instructionally shallow and architecturally mismatched** to the declared course model. Three independent problems compound:

1. **Wrong module architecture.** ContentV2 ships the ContentV1 *topical-cluster* model (`M00`–`M07`: Orientation, Infection Control, Resident Rights, Dementia, Mobility, Nutrition/Skin/VS, Documentation, Review). The declared/contracted model requires **`M00` Orientation + NATP `M10`–`M17`** (1:1 with the CCCCO NATP curriculum modules). These are not the same modules and cannot be silently renamed — they require re-mapping per `01_SOURCE_TO_COURSE_CROSSWALK.md`.
2. **Declared time is not supported by actual content.** Modules declare **690 instructional minutes** (sum of `estimated_minutes` for `counts_toward_theory = true`), but the actual learner-facing narrated content totals only **~184.7 minutes** across all lesson cards. The gap is ~505 minutes of declared-but-absent instruction.
3. **Time model conflates instruction and assessment.** The schema has a single `estimated_minutes` per module/lesson with no separation of `instructional_minutes` vs. `assessment_minutes_excluded`. There is no machine-checkable guarantee that assessments are excluded from the 720-minute clock.

The scaffolding (card types, media placeholders, remediation slots, source references, PHI/compliance guardrails) is sound and reusable. The rebuild is therefore a **source-transformation + re-architecture + depth-authoring** effort, not a UI or generation-from-scratch effort.

---

## 1. Current module list (as shipped)

| # | module_id | Title | counts_toward_theory |
|---|-----------|-------|----------------------|
| 0 | M00 | Orientation and Compliance Boundaries | true |
| 1 | M01 | Infection Control and PPE | true |
| 2 | M02 | Resident Rights, Abuse Prevention, and Boundaries | true |
| 3 | M03 | Dementia, Communication, and Respectful Care | true |
| 4 | M04 | Mobility, Falls, and Workplace Safety | true |
| 5 | M05 | Nutrition, Skin Integrity, Vital Signs, and Observation | true |
| 6 | M06 | Documentation, Reporting, PHI Avoidance, and Scope | true |
| 7 | M07 | Final Review, Exam/Test, Affidavit, and Certificate Status | false |

**Mismatch:** Required model is `M00, M10, M11, M12, M13, M14, M15, M16, M17`. Current model is `M00–M07`. Module IDs, count, titles, and topical boundaries all differ.

---

## 2. Current declared minutes vs. actual narrated content

| module_id | Declared min | counts_toward_theory | Lessons | Cards | Narrated min (cards) | Depth gap (declared − narrated) |
|-----------|-------------:|----------------------|--------:|------:|---------------------:|--------------------------------:|
| M00 | 30 | true | 5 | 20 | 8.8 | −21.2 |
| M01 | 90 | true | 6 | 24 | 12.7 | −77.3 |
| M02 | 120 | true | 5 | 55 | 32.7 | −87.3 |
| M03 | 120 | true | 5 | 37 | 20.5 | −99.5 |
| M04 | 120 | true | 5 | 55 | 31.4 | −88.6 |
| M05 | 120 | true | 5 | 49 | 28.6 | −91.4 |
| M06 | 90 | true | 5 | 43 | 25.0 | −65.0 |
| M07 | 30 | false | 5 | 46 | 25.0 | (excluded from clock) |
| **Total** | **690 (counted)** | — | **41** | **329** | **~184.7 (all cards)** | **~−505** |

> Note: declared instructional total is **690**, not 720, because `M07` (review/exam/affidavit) is already `counts_toward_theory = false`. The required model instead puts the 720 minutes into `M00 (30)` + `M10–M17 (690)` and excludes assessment time. So the current data is both ~505 minutes short of its *own* declared content and structured against the wrong module map.

---

## 3. Current lessons per module

Total **41 lessons** across 8 modules: M00=5, M01=6, M02=5, M03=5, M04=5, M05=5, M06=5, M07=5. Lesson count is reasonable; **per-lesson depth is not** (see §5).

---

## 4. Current cards per lesson

Total **329 cards / 41 lessons = ~8.0 cards per lesson average**, but cards are thin. The dominant lesson shape is the rejected pattern:

```
C01_OVERVIEW  →  C02A_DELIVERY (often a Source-Repair placeholder)  →  C03_CHALLENGE  →  C04x_DEBRIEF
```

Card-type distribution observed: every lesson has exactly **1 challenge** and **1 remediation/debrief** card (41 each). Delivery cards are typically a **single** `C02A` (frequently a placeholder), not the required `C02A…C02F+` delivery sequence.

---

## 5. Current narration seconds per card (depth signature)

Representative measured values from M00 L00:
- `C01_OVERVIEW` — **20 s** (47 words)
- `C02A_DELIVERY` — **17 s** (39 words, *Source Repair placeholder*)
- `C03_CHALLENGE` — **20 s** (47 words)
- `C04x_DEBRIEF` — **~25–30 s**

This confirms the reported pattern: **lessons run ~1–2 minutes of narrated time**, far below the 10–20 minutes per lesson the time model requires. Card 2 (delivery) is the thinnest element and is frequently a placeholder rather than real instruction.

---

## 6. Current total narration minutes

- **Lesson cards (canonical JSON):** ~**184.7 minutes** of narration across 329 cards.
- **Narration manifest (`narration_metadata.json`):** **393 clips / 12,071 s ≈ 201.2 minutes** total — the larger figure includes non-lesson clips (`APP`, `FINAL` exam, clinical support, module assessments) beyond the 329 lesson cards.

Either way, actual narrated instruction is **~185–201 minutes** against a **720-minute** target — roughly **26–28% of required depth**.

---

## 7. Current visible placeholder count (media)

**329 / 329 cards** carry `media_status: "placeholder-pending"` with `required_for_mvp: false`. Media is 100% placeholder (by design — no assets generated), but every card does carry a 16:9 prompt + alt text + PHI-safety note. Media scaffolding is complete; no real assets exist.

---

## 8. Current source-repair placeholder count

**17 cards** are explicit *Source Repair Required* placeholders (learner-facing text reads "Draft / Source Repair Required: canonical source text … is missing or incomplete"). These are correctly flagged with `sme_review_flag: "SME/source repair required"` and must remain flagged until repaired with approved source. Most appear in the `C02A_DELIVERY` slot — i.e., the primary teaching card is missing for those lessons.

---

## 9. Current learner-facing internal-answer-language count

**41 cards** (every challenge/debrief lesson) contain at least one phrase matching the prohibited internal-answer / answer-key family (e.g., "answer key" / "Correct. Continue…" / instructor-rationale language) inside learner-facing fields. The internal challenge objects additionally carry `correct_id_internal`-style structures; these are *internal* and must never render, but the debrief copy currently leaks answer-key phrasing to the learner and must be replaced with the structured remediation model (Safety Principle → Safest Response → Option Review → Continue After Review).

---

## 10. Modules whose declared minutes are unsupported by actual content

**All 8 modules** are under-supported relative to their declared minutes (see §2). Worst absolute gaps: M03 (−99.5), M05 (−91.4), M04 (−88.6), M02 (−87.3), M01 (−77.3). M00 Orientation is −21.2 (declares 30, narrates 8.8) — **present but not yet a real 30-minute orientation**.

---

## 11. Final assessment answer-key exposure risk

- **Final assessment** (`assessments.final_assessment`) and **module assessments** (`assessments.module_assessments`) exist as separate objects — good.
- Risk is **at the lesson-challenge layer**, not the final exam: lesson debriefs currently use answer-key phrasing (§9). The final-exam pool (`30_FINAL_EXAM_POOL_50_COMPLETE.md`, 50 Q) must remain answer-key-hidden in the app. Current app wiring must be verified to ensure final-exam results never render option-level rationales or correct answers (Task 7 / Task 13 #12).
- **Action:** keep detailed remediation at the *lesson* layer only; final-assessment results may show score / pass-fail / topics-missed / review path only.

---

## 12. Current app data wiring status

- App consumes `standalone-course-mvp/src/data/contentV2.generated.ts` (2.25 MB, 25,193 lines) via `contentV2Adapter.ts`, plus supporting modules (`lessonModel.ts`, `remediation.ts`, `remediationOverrides.ts`, `mediaManifest.ts`, `narrationManifest.ts`, `v2ModuleQuiz.ts`, `examPool.ts`, `courseModules.ts`).
- `contentV2.generated.ts` mirrors `courseContentV2.json` exactly (same 25k lines), so the app will reflect whatever the canonical JSON becomes once regenerated/synced.
- There are **unrelated in-flight working changes** on this branch (NIA assistant, branding toggle, reviewer login). Per instructions these are **out of scope** (do not alter login, do not redesign V2 UI) and were left untouched.

---

## Specifically-requested flags (confirmed)

- ✅ **Orientation present but not a real 30-minute orientation** — M00 narrates 8.8 min vs. 30 declared; source (`04_THEORY_MODULE_00_ORIENTATION_FULL.md`) is rich enough to support a true 30-minute build.
- ✅ **Course declared 720/690 but actual learner content much shorter** — ~185 narrated minutes.
- ✅ **Many lessons ~1–2 minutes long** — confirmed by per-card narration seconds (§5).
- ✅ **Card 2 (delivery) too thin** — frequently a single placeholder card.
- ✅ **Remediation uses internal answer-key language** — 41 cards (§9).
- ✅ **Media/TTS are placeholders only** — 329/329 media placeholders; narration is planning-only.
- ✅ **Module assessments + course final assessment need separation from the 720-minute clock** — no `instructional_minutes` / `assessment_minutes_excluded` fields exist yet.

---

## Source availability (feasibility of a defensible rebuild)

Genuine source exists to support most of the 720 minutes **without inventing content**:

| Required module | Primary NATP source (present) | Transformed ContentV1 module (present) | Pages/size |
|-----------------|-------------------------------|------------------------------------------|-----------|
| M00 Orientation (30) | Blueprint/cert-gate specs | `04_THEORY_MODULE_00_ORIENTATION_FULL.md` | rich (217 ln) |
| M10 Vital Signs (75) | `module-10.pdf` (786 KB) | `27_…NUTRITION_SKIN_INTEGRITY_VITAL_SIGNS_FULL.md` (VS portions) | 46 pp |
| M11 Nutrition (85) | `module-11.pdf` (391 KB) | `27_…` (nutrition portions) | 31 pp |
| M12 Emergency Procedures (75) | `module-12.pdf` (253 KB) | `26_…MOBILITY_FALLS_WORKPLACE_SAFETY_FULL.md` (emergency portions) | 24 pp |
| M13 LTC / Aging / Dementia / Skin (140) | `module-13.pdf` (537 KB) | `25_…DEMENTIA…` + `27_…` (skin) | 82 pp (largest) |
| M14 Rehab / Mobility / Restorative (85) | `module-14.pdf` (300 KB) | `26_…MOBILITY…` | 27 pp |
| M15 Observation & Charting (75) | `module-15.pdf` (340 KB) | `28_…DOCUMENTATION…` | 21 pp |
| M16 Death & Dying (60) | `module-16.pdf` (97 KB) | (folded into `25_…` currently) | 17 pp |
| M17 Abuse & Rights (95) | `module-17.pdf` (84 KB) | `24_…RESIDENT_RIGHTS_ABUSE_PREVENTION_FULL.md` | 14 pp |

**Conclusion:** The NATP PDFs (modules 10–17) and transformed theory files contain enough real content to build defensible depth for most modules. Where a NATP source section is thin (notably M16 Death & Dying at 17 pp and M17 at 14 pp relative to a 95-min allocation), depth must come from faithful expansion of that source — and any remaining shortfall must be flagged **Source Repair Required**, never invented.

---

## Recommended rebuild order (informs Tasks 2–14)

1. Add the **time-model fields** to schema + data (`instructional_minutes`, `assessment_minutes_excluded`, `module_assessment_minutes_excluded`, `course_final_assessment_minutes_excluded`, `counts_toward_720_instructional_minutes`).
2. Re-architect modules to **M00 + M10–M17** using the crosswalk; carry forward existing source-grounded cards by topic, re-homed to the correct NATP module.
3. Rebuild **M00 Orientation** to a true 30 minutes (source is sufficient).
4. Author per-module delivery depth from the NATP PDFs (`C02A…C02F+`), one hard challenge per lesson with plausible distractors, and the structured 4-part-per-option remediation.
5. Strip all learner-facing internal-answer language.
6. Regenerate all artifacts (JSON/TS/generated.ts/CSV/XLSX/docs) from a single source-grounded pass to keep them in sync.
7. Wire the app, validate (`typecheck`/`build`/`test`) and the 21-point content checklist.

**Guardrails preserved throughout:** no PHI; certificate production disabled; Optional Clinical Support optional/non-credit/non-gating; no CDPH-approval claims; no invented clinical content.
