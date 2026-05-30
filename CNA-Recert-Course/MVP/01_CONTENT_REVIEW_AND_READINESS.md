# 01 — Content Review and Readiness

**Scope reviewed:** `CNA-Recert-Course/Content/**` (theory modules, clinical support, exam pool, syllabus tables, knowledge-check & TTS blueprints, gap/compliance logs) and the app's seeded mirror in `standalone-course-mvp/src/data/`.

---

## 1. Content Package Shape

The content package is **well-organized and substantially drafted**, structured as a Moodle-ready build packet:

| Area | Location | State |
|------|----------|-------|
| Theory syllabus (12 hr) | `Content/02_THEORY_SYLLABUS_TABLE.md` | Complete — 8 modules (0–7), 720 min total |
| Clinical support syllabus | `Content/03_CLINICAL_SUPPORT_SYLLABUS_TABLE.md` | Complete — CS-1…CS-7, all optional/non-gating |
| Theory module full content | `Content/theory/modules/04…29_*.md` | Module 0,1,2,4,5,6 drafted in depth; Module 3 interrupted |
| Module templates | `Content/06_THEORY_MODULE_TEMPLATE_PACK.md` | Template pack for remaining modules |
| Knowledge-check blueprint | `Content/08_MODULE_KNOWLEDGE_CHECK_BLUEPRINT.md` | Present |
| Final exam | `Content/09_FINAL_EXAM_BLUEPRINT.md`, `theory/exam/30_FINAL_EXAM_POOL_50_COMPLETE.md`, `csv/31_QUIZ_BANK_MASTER_COMPLETE.csv` | 50-item pool; 25-item attempt; 80% pass |
| Affidavit | `Content/13_AFFIDAVIT_TEXT.md` | Draft text; legal/CDPH review pending |
| TTS narration | `Content/16_TTS_NARRATION_PACKAGE.md`, `theory/tts/34_*.md` | Transcript planning only; **no audio generated** |
| Clinical support full | `Content/clinical-support/32_CLINICAL_SUPPORT_FULL_CONTENT.md` + confidence checks `33_*.md` | Drafted; optional |
| Compliance & QA | `Content/19_COMPLIANCE_REVIEW_CHECKLIST.md`, `20_GAP_LOG.md`, `21_SOURCE_CONFLICT_LOG.md`, `qa/*` | Present |
| Accessibility/mobile QA | `Content/17_ACCESSIBILITY_AND_MOBILE_QA_CHECKLIST.md` | Present |

**Total theory time: 720 min = 12.0 CE hours** — fits safely inside the CDPH 24-hr online cap. Clinical support is a separate 720 min that must **never** be summed with theory.

---

## 2. Module-by-Module Readiness Table (Required Theory)

Legend — Readiness: 🟢 Production-draft (full prose + checks) · 🟡 Partial / flagged · 🔴 Blocked (source defect)

| Mod | Title | Time | Lessons | Readiness | KCs present | Scenarios | Remediation copy | TTS/transcript | PHI risk | Pathway | Key gaps / actions |
|----|-------|------|---------|-----------|-------------|-----------|-----------------|----------------|----------|---------|--------------------|
| 0 | Orientation & Compliance Boundaries | 0.5 hr | 3 sections (scope, identity, acknowledgements) | 🟢 | Acknowledgement checks | n/a | n/a | Planned, no audio | Low (collects name/CNA#) | Required (gating) | Finalize disclaimer wording w/ compliance; keep DRAFT labels |
| 1 | Infection Control & PPE | 1.5 hr | 6 (HAIs, Chain, Hand Hygiene, PPE, Recognize/Report, Cleaning) | 🟡 | **6 inline KCs** (none on 1.1) + 3 interactions, w/ answers + ✅/❌ feedback. **Graded module quiz referenced but NOT authored** | Yes (reporting, PPE) | Yes, per KC | Planned | Low (fictional "Mrs. J") | Required (gating) | **CRITICAL GAP:** no dedicated NATP 10–17 infection module; built from legacy CNA-CE-001 + scattered NATP refs. **All content NEEDS SME/source review**; **author the 80%-pass module quiz** before pilot |
| 2 | Resident Rights, Abuse Prevention & Boundaries | 2.0 hr | 6 | 🟢 | 6 formative + scenario quiz | 2 strong scenarios (grievance, mandated report) | Yes | Planned | Low | Required (gating) | NATP Module 17 is 6 theory hrs compressed to 2 — prioritize critical content; compliance + CDPH/legal review |
| 3 | Dementia, Communication & Cultural Respect | 2.0 hr | 6 (truncated mid-3.2) | 🔴 | Partial through 3.2 | 1 usable (repeated-question); Mrs. Okafor scenario incomplete (no choices/answers) | Partial | Planned | Low | Required (gating) | **Source truncated at Screen 3.2.3** — Lessons 3.3–3.5, module quiz, completion/metadata all missing. **QA/closeout docs incorrectly mark this module "complete."** Source remediation required before delivery |
| 4 | Mobility, Falls & Workplace Safety | 2.0 hr | 6 | 🟢 | 6 formative + safety scenario | 2 scenarios (2-person transfer, restorative feeding) | Yes | Planned | Low | Required (gating) | Use "knowledge refresh" language (no hands-on competency claim); emergency wording review |
| 5 | Nutrition, Skin Integrity, Vital Signs & Observation | 2.0 hr | 6 | 🟡 | 6 formative + VS scenario | 2 scenarios (thickened liquids, BP change) | Yes | Planned (skin section flagged) | Low (warns against PHI) | Required (gating) | **Skin-integrity / pressure-injury content + exam Q21 & Q38 flagged for SME review** |
| 6 | Documentation, Change-of-Condition & Scope (PHI avoidance) | 1.5 hr | 5 | 🟢 | 5 formative + doc scenarios + PHI ack | 2 scenarios (objective note, out-of-scope dressing) | Yes | Planned | **Teaches PHI avoidance — free-text prompts must prohibit PHI** | Required (gating) | Compliance + CDPH/legal review of scope/affidavit alignment |
| 7 | Review, Final Exam/Test & Affidavit | 0.5 hr | Review + exam + affidavit | 🟡 | Practice quiz + Final Exam (25/50, 80%) | Case-based review recommended | Exam remediation (review modules before retry) | n/a | Low | Required (gating) | E-signature acceptance unresolved (wet-sign fallback); certificate disabled until all gates pass; flagged exam items (M1, skin) pending |

### Per-criterion content readiness (theory)

| Criterion | Status across theory modules |
|-----------|------------------------------|
| Suitable for asynchronous delivery | Yes — content is text-first, chunked into screens, matches microlearning model |
| Needs chunking into micro-lessons | **Yes** — current lessons are 15-min sections; the Async Blueprint requires 3–5 min micro-lessons (≤100–150 words/screen). Existing "screens" are a good chunking seed but must be re-segmented |
| Needs knowledge checks | Mostly present (M1, M2, M4, M5, M6 have KCs); M3 partial; format must be normalized to WCAG-safe H5P types (MC, Single Choice, True/False, Dialog Cards) |
| Needs scenario cards | Present in M1,2,4,5,6; **M0 has none** (acceptable); M3 has one usable + one broken |
| Needs remediation copy | Present per KC and per module; final-exam remediation defined; normalize tone to "Not quite. Remember that…" |
| Needs transcript/TTS prep | Transcripts planned for all; **no audio exists**. Do not generate audio until script locked + cloned-voice authorization |
| PHI risk / sanitization | Low overall; scenarios use fictional names ("Mrs. J"). **M6 documentation practice + all Clinical Hub free-text/upload** are the real PHI-exposure surfaces and already carry warnings in content |
| Maps to required vs optional | Clean — Modules 0–7 = Required theory; CS-1…CS-7 = Optional support |

---

## 3. Clinical Support (Optional, Non-Gating) Readiness

| ID | Title | Time | Readiness | PHI surface | Gate impact | Notes |
|----|-------|------|-----------|-------------|-------------|-------|
| CS-1 | Clinical Orientation | 30m | 🟢 | None | **None** | Must display "optional / does not count toward online CE certificate" |
| CS-2 | Skills Refresh Menu / Library | 120m | 🟡 | None | None | Skin-integrity references retain SME flag; access-only, no grades |
| CS-3 | Scheduling Guidance | 60m | 🟢 | None | None | Choice/Calendar; scheduler plugin only after validation |
| CS-4 | Optional Confidence Checks | 120m | 🟡 | None | None | Ungraded; checks 06/07 (skin) flagged; must not report to gradebook |
| CS-5 | Practice Documentation Support | 180m | 🟢 | **High** | None | PHI warning before every upload; admin reviews & rejects PHI |
| CS-6 | RN/Preceptor Signoff Workflow | 120m | 🟢 | Medium | None | Name/title/date/contact/signature only; **not** clinical-hour credit |
| CS-7 | Support Follow-up / Help Path | 90m | 🟢 | Low | None | Unstaffed support queue is an operational risk |

**Hard boundary confirmed in content:** every clinical-support source file explicitly states non-credit, non-gating, no renewal clinical-hour credit. The redesign must preserve this verbatim.

---

## 4. App vs. Source Content Gap

The app's `moduleContent.ts` is a **faithful but shallow mirror** of the source: it carries titles, objectives, lesson-section titles/minutes, and 1–2 scenario checks per module — but **not** the full screen-by-screen prose, the full 6-KC sets, or the interaction definitions that exist in `Content/theory/modules/*`. Phase 2 must load/port the real lesson bodies (e.g., Module 1's 15 screens + 6 KCs) rather than the current one-line summaries.

| Content asset | Exists in `Content/` | Wired into app today |
|---------------|----------------------|----------------------|
| Full lesson prose (screens) | Yes (M0,1,2,4,5,6) | No (summaries only) |
| 6 KCs/module w/ feedback | Yes (M1 confirmed) | No (only M1 single scenario + manual quiz checkbox) |
| H5P interaction specs | Yes (M1: 3 interactions) | No |
| 50-item exam pool | Yes | No (5 preview cards only) |
| TTS transcripts | Planned | Placeholder text only |

---

## 5. Gaps, Duplication, and Defects (consolidated)

| ID | Type | Item | Severity | Action |
|----|------|------|----------|--------|
| C-1 | **Source defect** | Module 3 interrupted at Screen 3.2.3; cultural/EOL/trauma bodies missing | High | Regenerate/repair source; do not deliver incomplete sections |
| C-2 | **Coverage gap** | Module 1 has no dedicated NATP 10–17 infection module | High | SME verification that drafted content meets CDPH expectations |
| C-3 | **SME flag** | Module 5 skin integrity + exam Q21/Q38 | Medium | SME review of staging content & items |
| C-4 | Scope compression | Module 2 compresses NATP-17 (6 hr) into 2 hr | Medium | ID prioritization; mark remainder as supplementary reading |
| C-5 | Unresolved | Affidavit e-signature acceptance method | High | Legal/CDPH decision; wet-sign fallback |
| C-6 | Unresolved | Provider NAC#/certificate metadata | High | Confirm before any certificate surface goes live |
| C-7 | Production rule | TTS audio not generated; redundancy risk | Medium | Lock text, then generate optional ≤60–90s neural audio + transcript |
| C-8 | Duplication/drift | Two content indexes (`23_…` and `index/35_…UPDATED`); **two exam pools** (`10_…PARTIAL` vs `30_…COMPLETE`); **two TTS packages** (`16_…` partial vs `34_…COMPLETE`); **two quiz CSVs** (`11_…` legacy vs `31_…COMPLETE`); two app gate models | Med | Mark `30_/31_/34_/index-35` as canonical; retire/flag `10_/11_/16_/23_`; unify app gate model |
| C-9 | Format | Existing KCs include drag/match interactions | Medium | Replace drag/drop & matching with WCAG-safe MC/Single-Choice/Dialog Cards per Interaction Matrix |
| C-10 | **Missing assessment** | **Module 1 graded module-quiz questions are referenced but not authored** in the module file (only 6 formative KCs exist; syllabus promises a 80%-pass module quiz) | High | Author Module 1 module quiz (≥8 items per template) before pilot |
| C-11 | **Spec conflict** | Final-exam parameters disagree: blueprint `09_…` says **3 attempts, no timer**; Module 7 file `29_…` says **2 attempts, 45-min timer**; Module 7 total time 30 min vs 45-min exam timer | High | Reconcile exam attempts/timer/minutes across `09_`, `29_`, `34_` before building exam engine |
| C-12 | **Structure mismatch** | Syllabus/template specify **6 lessons/module**, but module files 2–6 implement **5 lessons + 1 graded quiz**; Module 0 has 5 lessons | Med | Decide canonical lesson structure; align UI lesson rail + completion rules |
| C-13 | **QA status error** | QA/closeout docs mark **Module 3 "complete"**, but its source is truncated mid-Lesson 3.2 | Med | Correct QA status; treat M3 as not build-ready |
| C-14 | Duplication | Clinical-support unit durations differ: syllabus `03_` (e.g., CS-1 30 min) vs full content `32_` (CS-1 15 min) | Low | Pick authoritative CS durations |

---

## 6. Content Conversion Priority (for Phase 2)

1. **Module 1 — Infection Control & PPE** → prototype module (full prose + 6 KCs already drafted; highest pedagogical clarity; named as prototype in both source docs).
2. Module 6 (Documentation/PHI) — anchors the PHI-avoidance teaching that protects the whole platform.
3. Modules 2, 4, 5 — complete drafts, straightforward micro-lesson conversion.
4. Module 0 — small; convert alongside M1 (it gates everything).
5. Module 3 — **blocked** until source remediation; convert last.
6. Final exam (Module 7) — build real 25/50 randomized engine after question items pass SME review (M1, skin items).
