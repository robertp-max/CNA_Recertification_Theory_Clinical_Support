# CNA Recertification Online CE Package - Modules 10–17 - Draft / Pending Approval

> **Compliance-safe status banner:** Pending applicable approval. Do not advertise, issue certificates, or represent this course as approved until approval status, provider/course identifiers, and certificate wording are confirmed.

**Working Course Title:** California CNA Recertification Online Continuing Education: Modules 10–17
**Audience:** California Certified Nursing Assistants completing online continuing education toward CNA renewal.
**Delivery:** 100% online, asynchronous, self-paced continuing education (CE) only.
**Approval status:** Draft / Pending Approval.
**Primary deliverable:** This markdown course package. The XLSX workbook and PDF-ready documentation are support/defensibility artifacts only.

---

## A. Executive Summary

This package converts the approved/source **CCCCO Nurse Assistant Model Curriculum (Revised December 2018), Modules 10–17** into an LMS-ready, 24-hour online continuing education (CE) course design for the California CNA two-year renewal cycle, built for Moodle implementation.

- The course preserves the eight source modules exactly as numbered and titled in the source curriculum. No new module topics are invented; no module is split into unrelated topics.
- The 24 online CE hours are organized into a **Year 1 (12 hours) / Year 2 (12 hours)** structure across the two-year renewal period.
- Online CE hours are kept strictly separate from clinical hours. This package does **not** claim hands-on clinical competency validation and does **not** claim clinical hours.
- All learner-facing artifacts (flyer, certificate, catalog copy) carry draft/pending-approval placeholder language. No real approval, provider, or course numbers are used.
- Every scenario is fictional and de-identified. No PHI, no real resident names, no real facility names, and no real clinical records appear anywhere in the package.

**Critical reconciliation finding (must be resolved before submission):** The master application packet's *official, CDPH-facing* 24-hour allocation (`__Master-Application-Packet/01_CNA_CDPH_CE_PACKET/24_HOUR_CNA_COURSE_MATRIX_FINAL.md` and `CDPH_192B_COURSE_LIST_ATTACHMENT.md`) is organized as **12 Units × 2 hours = 24 hours**, using different unit titles, and does **not** map one-to-one to Modules 10–17. The master packet therefore does **not** contain an official Modules-10–17 hour allocation. This package builds the Modules 10–17 lane as instructed and provides a defensible draft allocation, but the Module-vs-Unit structure conflict is flagged as the top open item in Section V. **Do not submit the Modules 10–17 structure to CDPH as if it were the already-documented 12-Unit structure without owner/SME/CDPH reconciliation.**

---

## B. Compliance Guardrails

These guardrails apply to every artifact in this package and every downstream LMS build.

1. **Approval language.** Use only placeholder approval language. Required banner on all public/learner-facing materials: *"Pending applicable approval. Do not advertise, issue certificates, or represent this course as approved until approval status, provider/course identifiers, and certificate wording are confirmed."*
2. **Credit language.** "24 online CE hours" is **draft course-design math only** unless the master packet confirms approved wording. Do not print approved CEU language.
3. **Online CE only.** Every learner-facing surface must state the course delivers **online continuing education only**; it does not provide, simulate, or validate hands-on clinical skills and does not award clinical hours.
4. **No full-renewal claim.** Do not state or imply that this online course alone completes all California CNA renewal requirements. CNA renewal requirements (including any in-service/clinical and employment verification) are set by CDPH and must be confirmed; treat as "Needs confirmation."
5. **Scope of practice.** Every scenario, knowledge check, and exercise must reinforce CNA scope of practice: observe, assist, report to the licensed nurse, document within CNA scope. CNAs do not diagnose, do not interpret results clinically, do not change care plans, and do not perform tasks reserved for licensed staff.
6. **No PHI / no real data.** No real resident names, real facility names, real medical record numbers, dates of birth, or real clinical records. All names are fictional (e.g., "Resident A," "Mr. F (fictional)"). Learners must be instructed never to enter real resident or facility data into any LMS field, free-text box, or upload.
7. **Source fidelity.** Modules 10–17 are the controlling source set (CCCCO NA Model Curriculum, Rev. Dec 2018). Preserve source titles, statements of purpose, and performance objectives. Where source titles differ from the prompt's working titles, the source title governs (see Section C).
8. **Draft posture everywhere.** All outputs are Draft / Application Packet / Pending CDPH or applicable approval until the master packet proves otherwise.
9. **Infection control.** No standalone Infection Control module is added (the master packet does not require one inside the Modules 10–17 lane). Infection-control concepts are mapped only where they appear inside the source modules (e.g., glove use and equipment cleaning in Module 10 skills context, aspiration prevention in Module 11).

---

## C. Source Module Control Statement: Modules 10–17

**Controlling source:** California Community Colleges Chancellor's Office (CCCCO) Nurse Assistant Model Curriculum — Revised December 2018, Modules 10–17.
**Source evidence in repo:** `CNA-Recert-Course/ContentV2/survey-evidence/_source_text/module-10.txt` … `module-17.txt` and `cccco_objectives.json` (objectives, statements of purpose, source theory hours). These raw source texts — not generated ContentV2 deliverables — are used as the source of truth for titles, objectives, and intent.

**Exact source titles (these govern over the prompt's working titles where they differ):**

| Module | Source title (preserved exactly) | Prompt working title | Source statement-of-purpose theory hours |
| --- | --- | --- | --- |
| 10 | Vital Signs | Vital Signs | 3 |
| 11 | Nutrition | Nutrition | 2 |
| 12 | Emergency Procedures | Emergency Procedures | 2 |
| 13 | Long Term Care Patient/Resident | Long-Term Care Resident | 5 SNF/ICF (or 3 non-SNF/ICF + 2 add'l) |
| 14 | Rehabilitative Nursing | Rehabilitative / Restorative Nursing | 2 |
| 15 | Observation and Charting | Observation and Charting | 4 |
| 16 | Death and Dying | Death and Dying | 2 |
| 17 | Patient/Resident Abuse | Patient / Resident Abuse | 6 (suggested 7) |

Notes:
- Module 13's source title is **"Long Term Care Patient/Resident."** Use this exact title in CDPH-facing documents.
- Module 14's source title is **"Rehabilitative Nursing"** (the source body uses "restorative care/rehabilitation" interchangeably). Use "Rehabilitative Nursing" as the official title; "Restorative" may appear as a subtitle.
- The source theory hours are **not uniform** and total ~26 (or 24 with the non-SNF/ICF Module 13 option). They reflect *initial CNA training* theory hours, not a 24-hour CE redesign. See Section D for how the 24 CE hours are reconciled.

---

## D. 24-Hour Course Map

**Hour-math convention (conservative):** 1 online CE hour = **60 minutes** of documented, engaged seat time (content + activities + assessment), counted conservatively at the full 60 minutes (not 50). Estimated minutes are documented behind every hour in each module blueprint (Section G) and in the workbook `Course_Map` sheet.

**Allocation basis:** The master packet has **no** official Modules 10–17 hour allocation (its official allocation is the separate 12-Unit structure). Per the prompt, a defensible draft allocation is therefore proposed: **3 online CE hours per module × 8 modules = 24 hours**, which also satisfies the required Year 1 = 12 / Year 2 = 12 split. This even allocation is a CE **design** decision and is intentionally normalized away from the uneven CCCCO initial-training theory hours; the difference is flagged for SME/CDPH confirmation (Section V).

| # | Year | Source module | Source title | Online CE hours | Est. minutes | Source reference |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 10 | Vital Signs | 3 | 180 | `_source_text/module-10.txt` |
| 2 | 1 | 11 | Nutrition | 3 | 180 | `_source_text/module-11.txt` |
| 3 | 1 | 12 | Emergency Procedures | 3 | 180 | `_source_text/module-12.txt` |
| 4 | 1 | 13 | Long Term Care Patient/Resident | 3 | 180 | `_source_text/module-13.txt` |
| 5 | 2 | 14 | Rehabilitative Nursing | 3 | 180 | `_source_text/module-14.txt` |
| 6 | 2 | 15 | Observation and Charting | 3 | 180 | `_source_text/module-15.txt` |
| 7 | 2 | 16 | Death and Dying | 3 | 180 | `_source_text/module-16.txt` |
| 8 | 2 | 17 | Patient/Resident Abuse | 3 | 180 | `_source_text/module-17.txt` |
| | | | **Total** | **24** | **1,440** | |

**Reconciliation statement:** 8 modules × 3 online CE hours = 24 online CE hours = 1,440 minutes of documented seat time. Year 1 = Modules 10–13 = 12 hours. Year 2 = Modules 14–17 = 12 hours. These are draft online CE design hours only; they are not approved CEUs and are not clinical hours.

---

## E. Year 1 / Year 2 Split

| Year | Modules | Theme (descriptive, source-derived) | Online CE hours |
| --- | --- | --- | --- |
| **Year 1** | 10 Vital Signs, 11 Nutrition, 12 Emergency Procedures, 13 Long Term Care Patient/Resident | Core observation, nutrition/hydration, emergency response, and the long-term-care resident | 12 |
| **Year 2** | 14 Rehabilitative Nursing, 15 Observation and Charting, 16 Death and Dying, 17 Patient/Resident Abuse | Restorative care, documentation/observation, end-of-life care, and abuse prevention/reporting | 12 |

- Each Year is a Moodle course **section group** with its own completion roll-up and Year-level assessment.
- Year 2 modules unlock per the restrict-access rules in Section H; the renewal cycle spans two years, so Year 2 may be gated by date and/or by Year 1 completion (configurable; see Section H).
- A learner earns the certificate only after **both** Years are complete (Section K).

---

## F. Source-to-LMS Module Map

| Source module | Source topic (statement of purpose, condensed) | Required content to preserve | LMS destination (Moodle section) | Assessment linkage |
| --- | --- | --- | --- | --- |
| 10 Vital Signs | How/when/why vitals are taken; measure T/P/R/BP; recognize & report normal/abnormal; pain observation; record vitals | TPR + BP concepts, normal ranges, factors raising/lowering each vital, pain as observation, scope-safe reporting & charting | Y1 › M10 | KC-M10 + Scenario S-M10 + Year 1 Assessment |
| 11 Nutrition | Body's need for food/fluids; nutrients; therapeutic diets; feeding techniques; hydration; cultural/religious diet influences | Basic nutrients/food groups, common therapeutic diets, dysphagia/aspiration awareness, hydration (I&O), feeding assistance, cultural respect, alternative nutrition routes (observe/report only) | Y1 › M11 | KC-M11 + Scenario S-M11 + Year 1 Assessment |
| 12 Emergency Procedures | Signs/symptoms of distress; CNA role in immediate/temporary response; choking/airway; emergency codes | Recognize distress, activate help/EMS chain, choking response within scope, common facility codes, CNA role boundaries in emergencies | Y1 › M12 | KC-M12 + Scenario S-M12 + Year 1 Assessment |
| 13 Long Term Care Patient/Resident | Aging effects on body; common conditions; dementia care; community resources; basic A&P | Human needs of elderly, dementia-sensitive approaches, special needs populations, body systems overview, complications of immobility | Y1 › M13 | KC-M13 + Scenario S-M13 + Year 1 Assessment |
| 14 Rehabilitative Nursing | Restorative care; independence; rehab team; ADLs; ROM; adaptive devices; preventing complications of inactivity | Restorative philosophy, CNA role on rehab team, ADLs, ROM types, adaptive/comfort devices, immobility-complication prevention, documentation/care-plan role | Y2 › M14 | KC-M14 + Scenario S-M14 + Year 2 Assessment |
| 15 Observation and Charting | Objective/subjective observation; medical terminology/abbreviations; charting documents; MDS/ADL; charting procedures | Senses used in observation, objective vs subjective, charting document types, accurate/timely/factual recording, incident reporting, scope-safe documentation | Y2 › M15 | KC-M15 + Scenario S-M15 + Year 2 Assessment |
| 16 Death and Dying | Grieving stages (Kübler-Ross); emotional/spiritual needs; rights of the dying; signs of approaching death; hospice; postmortem care | Five stages of grief, comfort/dignity measures, dying patient rights, signs of approaching vs biological death, hospice role, postmortem care responsibilities | Y2 › M16 | KC-M16 + Scenario S-M16 + Year 2 Assessment |
| 17 Patient/Resident Abuse | Types of abuse; issues; CNA role in prevention; CNA role in reporting | Abuse types/definitions, mandated-reporter duty, prevention, recognition, reporting pathways (ombudsman, supervisor, state), confidentiality/HIPAA basics | Y2 › M17 | KC-M17 + Scenario S-M17 + Year 2 Assessment |

---

## G. Detailed LMS Blueprints for Modules 10–17

Each blueprint uses the same structure. Hours are draft online CE design hours; minutes are conservative seat-time estimates summing to 180 per module. Objectives are the source CCCCO performance standards, restated as measurable, online-CE-appropriate learning objectives (cognitive/observation/reporting level — no hands-on competency claim).

### Module 10 — Vital Signs (Year 1 · 3 CE hours · 180 min)

- **Source reference:** `_source_text/module-10.txt`; objectives in `cccco_objectives.json` (16 objectives).
- **Source content summary:** Vital signs = temperature, pulse, respiration, blood pressure; pain as an observation. Normal ranges, factors that raise/lower each vital, observation cues (skin color/temperature, behavior), TPR as a combined process, BP concepts and equipment, and scope-safe recording/reporting.
- **Measurable learning objectives (online CE level).** The learner will be able to:
  1. Define key vital-signs terminology (e.g., febrile, tachycardia, dyspnea, systolic/diastolic, hypertension).
  2. State adult normal ranges for temperature (by route), pulse, respiration, and blood pressure.
  3. Identify factors that increase or decrease each vital sign.
  4. Distinguish normal from abnormal findings that must be reported to the licensed nurse.
  5. Describe the correct order and rationale for measuring TPR as a combined process.
  6. Identify objective observations of pain and scope-safe pain-reporting steps.
  7. Record vital signs accurately and in correct order (T, P, R; BP as systolic/diastolic) within CNA documentation scope.
- **Lesson breakdown (minutes):** L10.1 Terminology & purpose (25) · L10.2 Temperature: routes, ranges, factors (35) · L10.3 Pulse & respiration: sites, ranges, abnormal patterns (35) · L10.4 Blood pressure concepts, equipment, normal/abnormal (35) · L10.5 Pain observation & scope-safe reporting (20) · L10.6 Recording/charting vitals + knowledge check (30). **= 180 min.**
- **LMS activity sequence:** Page (objectives & banner) → Lesson (branching content L10.1–L10.5) → Interactive H5P "drag normal/abnormal" → Scenario (S-M10) → Knowledge Check quiz (KC-M10) → Reflection/attestation page.
- **Knowledge checks (KC-M10):** 8–10 low-stakes auto-graded items (multiple choice / true-false / matching) on ranges, factors, abnormal-finding recognition, and reporting. Unlimited attempts; feedback on each.
- **Scenario / judgment exercise (S-M10):** Fictional "Resident A" returns from a walk reporting shortness of breath and chest tightness. Learner selects the correct first CNA action (stay with resident, call the nurse immediately) and the scope boundary (does not diagnose, does not medicate). Branching feedback.
- **Documentation/reporting exercise:** Learner completes a *simulated, blank* vitals flow-sheet entry (fictional values) in correct T-P-R / BP format and writes a one-line scope-safe report to the nurse. No real data.
- **Completion requirement:** All lessons viewed + KC-M10 attempted + Scenario completed + documentation exercise submitted. (Year 1 Assessment is separate.)
- **Evidence artifact:** Activity-completion timestamps, KC-M10 attempt record, scenario branch log, submitted simulated flow-sheet, time-in-module log.
- **SME/compliance flags:** Confirm normal-range figures against current facility/CDPH standards; ensure no hands-on measurement competency is implied.
- **PHI / no-real-data notes:** Fictional resident and values only; learner warned not to enter real data.
- **Accessibility notes:** Captioned media, alt text on equipment images, color-independent normal/abnormal cues, screen-reader-friendly tables.
- **Suggested Moodle activity types:** Lesson, Quiz, H5P, Assignment (simulated flow-sheet), Page.

### Module 11 — Nutrition (Year 1 · 3 CE hours · 180 min)

- **Source reference:** `_source_text/module-11.txt`; 10 objectives.
- **Source content summary:** Body's need for food/fluids; nutrients and food sources; food-guidance system; nutritional/fluid needs of the elderly; common therapeutic diets and the CNA's responsibilities; safe feeding techniques; cultural/religious dietary influences; alternative nutrition routes (awareness/observe-report only).
- **Measurable learning objectives.** The learner will be able to:
  1. Define key nutrition terminology (e.g., dysphagia, aspiration, NPO, therapeutic diet, I&O, dehydration).
  2. Explain the body's need for food and fluids and signs of dehydration/over-hydration to report.
  3. List common nutrients and their food sources.
  4. Match common therapeutic diets (clear/full liquid, pureed, mechanical soft, low-sodium, etc.) to the CNA's role.
  5. Describe safe feeding-assistance techniques and aspiration-prevention precautions.
  6. Describe how cultural and religious preferences affect dietary care and how to respect them.
  7. Identify alternative nutrition routes (e.g., NG, PEG, TPN) as observe-and-report-only for the CNA.
- **Lesson breakdown (minutes):** L11.1 Terminology & body's need for food/fluids (25) · L11.2 Nutrients & food groups (30) · L11.3 Hydration, I&O, elderly needs (30) · L11.4 Therapeutic diets & CNA role (35) · L11.5 Safe feeding & aspiration prevention (30) · L11.6 Cultural/religious respect + alternative routes + KC (30). **= 180 min.**
- **LMS activity sequence:** Page → Lesson → Matching H5P (diet ↔ description) → Scenario (S-M11) → KC-M11 → Reflection.
- **Knowledge checks (KC-M11):** 8–10 items on diets, hydration signs, aspiration precautions, scope of feeding assistance.
- **Scenario (S-M11):** Fictional resident on a pureed/thickened-liquid diet is served a regular tray by mistake; learner selects correct CNA action (do not serve, verify the diet order with the nurse, report) and aspiration-risk precautions.
- **Documentation/reporting exercise:** Complete a simulated intake/output and meal-percentage entry (fictional) and report a hydration concern.
- **Completion requirement:** Lessons viewed + KC-M11 attempted + Scenario completed + I&O exercise submitted.
- **Evidence artifact:** Completion timestamps, KC attempt, scenario log, submitted I&O exercise, time log.
- **SME/compliance flags:** Confirm therapeutic-diet list matches facility menu/diet manual; ensure feeding content stays at assistance level, not clinical assessment.
- **PHI notes:** Fictional diets/values only.
- **Accessibility:** Captions, alt text, plain-language diet descriptions.
- **Moodle types:** Lesson, H5P, Quiz, Assignment, Page.

### Module 12 — Emergency Procedures (Year 1 · 3 CE hours · 180 min)

- **Source reference:** `_source_text/module-12.txt`; 5 objectives.
- **Source content summary:** Signs/symptoms of distress; CNA's role/responsibility in preventing and responding to emergencies (immediate and temporary intervention only); causes/signs of choking and use of abdominal thrusts; common LTC emergency codes. (Source notes this may be taught with Module 4 Safe Environment.)
- **Measurable learning objectives.** The learner will be able to:
  1. Define key emergency terminology (e.g., syncope, hypoxia, cardiac arrest, recovery position, EMS, DNR).
  2. Recognize common signs/symptoms of resident distress and the CNA's prevention/response role.
  3. Sequence the CNA's immediate, scope-safe actions in a medical emergency (stay, call for help/nurse, activate EMS chain).
  4. Identify causes/signs of choking and describe response within scope for a conscious choking adult.
  5. Match common facility emergency codes to the appropriate response.
- **Lesson breakdown (minutes):** L12.1 Terminology & distress recognition (30) · L12.2 CNA role & immediate interventions (35) · L12.3 Choking/airway response within scope (35) · L12.4 Emergency codes & chain of response (30) · L12.5 DNR/advance-directive awareness (group reading) (20) · L12.6 Scenario + KC (30). **= 180 min.**
- **LMS activity sequence:** Page → Lesson → "Code matching" H5P → Scenario (S-M12) → KC-M12 → Reflection.
- **Knowledge checks (KC-M12):** 8–10 items on distress signs, first actions, choking response, codes, scope limits.
- **Scenario (S-M12):** Fictional resident is coughing forcefully at lunch, then stops coughing and clutches the throat. Learner selects correct escalation and within-scope action and identifies when to call for the nurse/EMS. **Reinforces that online CE does not certify hands-on CPR/first-aid; hands-on certification is separate.**
- **Documentation/reporting exercise:** Complete a simulated incident-report narrative (fictional) using objective facts only.
- **Completion requirement:** Lessons viewed + KC-M12 attempted + Scenario completed + incident-narrative submitted.
- **Evidence artifact:** Completion timestamps, KC attempt, scenario log, submitted narrative, time log.
- **SME/compliance flags:** **High** — explicitly state no hands-on CPR/Heimlich competency is granted; confirm facility code list; align with current AHA/ARC guidance language.
- **PHI notes:** Fictional only.
- **Accessibility:** Captions, alt text, no reliance on color alone for code identification.
- **Moodle types:** Lesson, H5P, Quiz, Assignment, Page.

### Module 13 — Long Term Care Patient/Resident (Year 1 · 3 CE hours · 180 min)

- **Source reference:** `_source_text/module-13.txt`; 8 objectives. (Source theory hours 5 SNF/ICF or 3 non-SNF/ICF + 2; see Section V.)
- **Source content summary:** Basic human needs of the elderly (environmental, psychological, social, recreational, spiritual); community resources; special needs (developmental/mental disorders, Alzheimer's/related dementias); body organization and systems; aging changes; complications of immobility.
- **Measurable learning objectives.** The learner will be able to:
  1. Define key LTC terminology (e.g., chronic, dementia, reality orientation, validation therapy, contractures).
  2. Describe common human needs of the elderly resident and scope-safe CNA interventions.
  3. Identify community resources that support elderly residents.
  4. Describe dementia-sensitive care approaches and de-escalation within scope.
  5. Describe special needs of residents with developmental/mental disorders.
  6. Summarize aging changes by body system and the complications of immobility a CNA observes/reports.
- **Lesson breakdown (minutes):** L13.1 Terminology & LTC settings (25) · L13.2 Human needs of the elderly (30) · L13.3 Dementia-sensitive care & approaches (40) · L13.4 Special-needs populations (25) · L13.5 Body systems & aging changes overview (30) · L13.6 Complications of immobility + Scenario + KC (30). **= 180 min.**
- **LMS activity sequence:** Page → Lesson → "Dementia approach" branching H5P → Scenario (S-M13) → KC-M13 → Reflection.
- **Knowledge checks (KC-M13):** 8–10 items on needs, dementia approaches, aging changes, immobility complications.
- **Scenario (S-M13):** Fictional resident with dementia becomes agitated during evening care (sundowning). Learner selects scope-safe, dignity-preserving approaches and identifies what to report.
- **Documentation/reporting exercise:** Document an observed behavior change objectively and identify the reporting pathway.
- **Completion requirement:** Lessons viewed + KC-M13 attempted + Scenario completed + observation note submitted.
- **Evidence artifact:** Completion timestamps, KC attempt, scenario log, submitted note, time log.
- **SME/compliance flags:** Confirm dementia-care language aligns with current person-centered-care standards; keep within CNA scope (no behavioral diagnosis).
- **PHI notes:** Fictional only.
- **Accessibility:** Captions, alt text, plain language, content warnings where appropriate.
- **Moodle types:** Lesson, H5P, Quiz, Assignment, Page.

### Module 14 — Rehabilitative Nursing (Year 2 · 3 CE hours · 180 min)

- **Source reference:** `_source_text/module-14.txt`; 12 objectives.
- **Source content summary:** Restorative care promotes independence and optimal functioning; goals of restorative care; the rehab team and the CNA's role; promoting self-care; ADLs; comfort/adaptive devices; preventing complications of inactivity; ROM exercises; mobility/ambulation devices; self-esteem and family involvement; documentation and care-plan role.
- **Measurable learning objectives.** The learner will be able to:
  1. Define key rehab/restorative terminology (e.g., ADLs, ROM, contractures, atrophy, prosthesis, ambulation).
  2. Explain restorative-care philosophy and how it promotes independence.
  3. Describe the rehab team and the CNA's scope-safe role on it.
  4. List ADLs and CNA approaches that promote resident self-care.
  5. Identify common comfort/adaptive devices and their purposes.
  6. Describe ROM types and steps the CNA takes to prevent complications of inactivity (observe/assist/report).
  7. Describe the CNA's documentation and care-plan-meeting role.
- **Lesson breakdown (minutes):** L14.1 Terminology & restorative philosophy (25) · L14.2 Rehab team & CNA role (25) · L14.3 ADLs & promoting self-care (30) · L14.4 Comfort/adaptive devices (30) · L14.5 ROM & immobility-complication prevention (40) · L14.6 Documentation/care plan + Scenario + KC (30). **= 180 min.**
- **LMS activity sequence:** Page → Lesson → "Device-to-purpose" matching H5P → Scenario (S-M14) → KC-M14 → Reflection.
- **Knowledge checks (KC-M14):** 8–10 items on ADLs, ROM types, devices, immobility complications, scope.
- **Scenario (S-M14):** Fictional resident recovering from a hip procedure wants to do everything for them; learner selects the restorative approach (assist only as needed, encourage independence) within scope and identifies what to document.
- **Documentation/reporting exercise:** Record a restorative-care contribution and an observation for the care plan (fictional).
- **Completion requirement:** Lessons viewed + KC-M14 attempted + Scenario completed + care-plan note submitted.
- **Evidence artifact:** Completion timestamps, KC attempt, scenario log, submitted note, time log.
- **SME/compliance flags:** Ensure ROM content stays at assist/observe level (no claim of independent therapy); confirm device list.
- **PHI notes:** Fictional only.
- **Accessibility:** Captions, alt text, step diagrams with text equivalents.
- **Moodle types:** Lesson, H5P, Quiz, Assignment, Page.

### Module 15 — Observation and Charting (Year 2 · 3 CE hours · 180 min)

- **Source reference:** `_source_text/module-15.txt`; 8 objectives.
- **Source content summary:** Objective and subjective observation using the senses; medical word elements, terminology, and abbreviations; types of charting documents (Kardex, MDS, care plan, incident report); accurate ADL/MDS observation input; scope-safe recording procedures.
- **Measurable learning objectives.** The learner will be able to:
  1. Define key documentation terminology (e.g., objective, subjective, MDS, Kardex, incident report, ADL).
  2. Identify common medical word elements (prefix/root/suffix) and abbreviations used in facilities.
  3. Distinguish objective from subjective observations and the senses used to observe.
  4. Match charting document types to their use.
  5. Describe accurate, timely, factual, scope-safe recording procedures and correction practices.
  6. Identify when and how to complete an incident report objectively.
- **Lesson breakdown (minutes):** L15.1 Terminology & word elements (30) · L15.2 Abbreviations commonly used (25) · L15.3 Objective vs subjective observation (35) · L15.4 Charting document types (30) · L15.5 Recording procedures & corrections (30) · L15.6 Incident reporting + Scenario + KC (30). **= 180 min.**
- **LMS activity sequence:** Page → Lesson → "Objective vs subjective" sorting H5P → Scenario (S-M15) → KC-M15 → Reflection.
- **Knowledge checks (KC-M15):** 8–10 items on terminology, abbreviations, objective/subjective, charting rules.
- **Scenario (S-M15):** A fictional charting entry contains opinion and a diagnosis-like statement; learner rewrites it as an objective, scope-safe entry and flags what must be reported to the nurse.
- **Documentation/reporting exercise:** Convert subjective notes into an objective entry and complete a simulated incident report (fictional).
- **Completion requirement:** Lessons viewed + KC-M15 attempted + Scenario completed + rewritten entry submitted.
- **Evidence artifact:** Completion timestamps, KC attempt, scenario log, submitted entry, time log.
- **SME/compliance flags:** Reinforce that CNAs document observations, not diagnoses; confirm abbreviation list against facility "do-not-use" list.
- **PHI notes:** **High emphasis** — charting module; learners must use only fictional data and must never paste real records.
- **Accessibility:** Captions, alt text, readable tables, plain language.
- **Moodle types:** Lesson, H5P, Quiz, Assignment, Page.

### Module 16 — Death and Dying (Year 2 · 3 CE hours · 180 min)

- **Source reference:** `_source_text/module-16.txt`; 8 objectives.
- **Source content summary:** Death as a normal stage of life; five stages of grief (Kübler-Ross); emotional/spiritual needs of the terminally ill and families; rights of the dying resident; signs of approaching vs biological death; comfort measures; hospice philosophy and the CNA's role with a licensed hospice nurse; postmortem care responsibilities.
- **Measurable learning objectives.** The learner will be able to:
  1. Define key end-of-life terminology (e.g., palliative care, hospice, DNR, postmortem care, rigor mortis, mottling).
  2. Describe the five stages of grief per Kübler-Ross.
  3. Describe scope-safe approaches to emotional and spiritual needs of dying residents and families.
  4. List the rights of the dying resident.
  5. Differentiate common signs of approaching death from biological death.
  6. Identify comfort/dignity measures and the CNA's role with the hospice team.
  7. Describe CNA responsibilities in postmortem care.
- **Lesson breakdown (minutes):** L16.1 Terminology & death as normal stage (25) · L16.2 Five stages of grief (30) · L16.3 Emotional/spiritual needs & dying rights (35) · L16.4 Signs of approaching vs biological death (30) · L16.5 Comfort measures & hospice role (30) · L16.6 Postmortem care + Scenario + KC (30). **= 180 min.**
- **LMS activity sequence:** Page (with content/sensitivity note) → Lesson → "Grief-stage" matching H5P → Scenario (S-M16) → KC-M16 → Reflection.
- **Knowledge checks (KC-M16):** 8–10 items on grief stages, dying rights, signs of death, hospice role, postmortem care.
- **Scenario (S-M16):** A fictional family member is angry at staff while their loved one is dying; learner selects compassionate, scope-safe responses and identifies what to report and to whom.
- **Documentation/reporting exercise:** Document observed signs and comfort measures provided (fictional), and note the reporting step.
- **Completion requirement:** Lessons viewed + KC-M16 attempted + Scenario completed + note submitted.
- **Evidence artifact:** Completion timestamps, KC attempt, scenario log, submitted note, time log.
- **SME/compliance flags:** Add a learner sensitivity/content note; confirm postmortem-care steps match facility policy; keep within scope (no pronouncement of death).
- **PHI notes:** Fictional only.
- **Accessibility:** Captions, alt text, content warning, plain language.
- **Moodle types:** Lesson, H5P, Quiz, Assignment, Page.

### Module 17 — Patient/Resident Abuse (Year 2 · 3 CE hours · 180 min)

- **Source reference:** `_source_text/module-17.txt`; 5 objectives. (Source theory hours 6, suggested 7; see Section V.)
- **Source content summary:** Types of abuse and key legal/ethical terms; issues related to elder abuse; the CNA's role in preventing abuse; the CNA's role in recognizing and reporting abuse (mandated-reporter duty, ombudsman, supervisor, state channels); confidentiality/HIPAA, restraints, involuntary seclusion, and resident rights basics.
- **Measurable learning objectives.** The learner will be able to:
  1. Define key abuse terminology (e.g., abuse, neglect, battery, false imprisonment, mandated reporter, ombudsman, involuntary seclusion).
  2. Identify and describe types of abuse (physical, psychological/verbal, sexual, financial, neglect).
  3. Discuss issues related to elder abuse and contributing factors.
  4. Explain the CNA's role in preventing abuse and protecting resident rights.
  5. Describe the CNA's mandated-reporter role and the correct reporting pathways and timelines.
- **Lesson breakdown (minutes):** L17.1 Terminology & legal/ethical basics (25) · L17.2 Types of abuse (35) · L17.3 Issues & contributing factors (25) · L17.4 Prevention & resident rights (30) · L17.5 Recognizing & reporting; mandated-reporter duty (35) · L17.6 Scenario + KC (30). **= 180 min.**
- **LMS activity sequence:** Page → Lesson → "Abuse-type identification" H5P → Scenario (S-M17) → KC-M17 → Reflection/attestation.
- **Knowledge checks (KC-M17):** 8–10 items on abuse types, prevention, mandated reporting, channels, confidentiality.
- **Scenario (S-M17):** A fictional CNA observes a coworker handling a resident roughly and threatening them. Learner selects the correct mandated-reporter actions (ensure resident safety, report immediately per policy and to required authorities, document objectively) and confidentiality obligations.
- **Documentation/reporting exercise:** Complete a simulated abuse-report log (fictional) with objective facts and the reporting chain/timeline.
- **Completion requirement:** Lessons viewed + KC-M17 attempted + Scenario completed + report log submitted.
- **Evidence artifact:** Completion timestamps, KC attempt, scenario log, submitted report log, time log.
- **SME/compliance flags:** **High** — confirm current California mandated-reporter channels, timelines, and ombudsman contact framing; ensure no real names/cases used.
- **PHI notes:** Fictional only; emphasize confidentiality.
- **Accessibility:** Captions, alt text, content warning, plain language.
- **Moodle types:** Lesson, H5P, Quiz, Assignment, Page.

---

## H. LMS / Moodle Build Plan

### H.1 Course shell structure
- **Course full name (draft):** California CNA Recertification Online Continuing Education: Modules 10–17 (Draft / Pending Approval)
- **Course short name (draft):** CNA-RECERT-1017-DRAFT
- **Format:** Topics or Flexible sections format, with two top-level **section groups**: *Year 1* and *Year 2*.
- **Course summary:** Includes the compliance banner, "online CE only," and "no clinical hours" statements.

### H.2 Section layout
```
Course: CNA Recertification Online CE — Modules 10–17 (Draft)
├─ Section 0: Start Here (orientation, identity confirmation, learner attestation, no-PHI agreement, how CE hours/time work)
├─ Year 1 (12 CE hours)
│   ├─ M10 Vital Signs (3h)
│   ├─ M11 Nutrition (3h)
│   ├─ M12 Emergency Procedures (3h)
│   ├─ M13 Long Term Care Patient/Resident (3h)
│   └─ Year 1 Assessment + Year 1 progress check
└─ Year 2 (12 CE hours)
    ├─ M14 Rehabilitative Nursing (3h)
    ├─ M15 Observation and Charting (3h)
    ├─ M16 Death and Dying (3h)
    ├─ M17 Patient/Resident Abuse (3h)
    └─ Year 2 Assessment + Course completion / certificate gate
```

### H.3 Completion tracking configuration
- Enable **Completion tracking** at course level.
- Each module's Lesson, Scenario, Knowledge Check, and Assignment set **activity completion** conditions (viewed / attempted / submitted / minimum time where supported).
- Each module has a **manual or automatic module-completion** roll-up; each Year has a section roll-up.
- Course completion = all module roll-ups + both Year assessments passed + attestation/affidavit complete.

### H.4 Restrict access rules
- Section 0 (Start Here) must be completed (identity confirmation + attestation + no-PHI agreement) before Year 1 opens.
- Within a module: Scenario restricted until Lesson viewed; Knowledge Check restricted until Scenario complete; documentation Assignment available alongside.
- Year 1 Assessment restricted until M10–M13 complete.
- Year 2 restricted until **Year 1 complete** and/or by **date** (configurable for the two-year cycle — confirm policy in Section V).
- Year 2 Assessment restricted until M14–M17 complete.
- Certificate restricted until all certificate-gate conditions met (Section K).

### H.5 Quiz / attempt settings
- **Knowledge checks (formative):** unlimited attempts, immediate per-question feedback, shuffle questions/answers, not heavily weighted, "no final answer key shown" — show feedback/remediation, not a printable master key.
- **Year assessments (summative):** limited attempts (e.g., 3), questions and answers shuffled, question behavior "deferred feedback," **review options disabled** so correct answers are not exposed after submission (only score + remediation guidance), random selection from category question banks.
- **Passing threshold:** **80%** minimum on each Year assessment (and any cumulative assessment), unless the master packet specifies otherwise (Needs confirmation).
- **Timing:** Optional time limit per assessment; open/close dates align with the renewal cycle.

### H.6 Gradebook structure
- Gradebook categories: *Year 1 — Formative*, *Year 1 — Summative*, *Year 2 — Formative*, *Year 2 — Summative*.
- Knowledge checks: low or zero weight (gate by completion, not grade).
- Year assessments: graded, 80% pass, drive certificate gate.
- Aggregation: natural; pass conditions enforced via activity completion + grade-to-pass on each assessment.

### H.7 Certificate gate conditions
See Section K. Certificate issuance is blocked until all gate items pass; certificate carries placeholder approval/provider/course identifiers only.

### H.8 Activity completion conditions (per module)
- Lesson: require view (and minimum pages/time where applicable).
- Scenario: require completion/submission.
- Knowledge check: require attempt (and optionally minimum score for formative gating).
- Documentation Assignment: require submission.

### H.9 Identity confirmation checkpoints
- At enrollment/Section 0: learner confirms legal name and (if required by master packet) CNA certificate number — **Needs confirmation whether CNA number is collected; do not assume.**
- Per-Year re-attestation checkpoint before each Year assessment ("I am the registered learner completing this work").
- Optional secondary identity prompt at certificate gate.
- Document SSO/authentication method as an LMS administration control (Needs confirmation of the production auth method).

### H.10 Affidavit / learner attestation workflow
See Section L.

### H.11 Time / participation evidence strategy
- Define 1 CE hour = 60 minutes documented engaged seat time; total target 1,440 minutes.
- Use Moodle **logs**, activity completion timestamps, and (where supported) minimum-time conditions on Lessons.
- Use the dedicated reports for time-on-task as supplemental evidence; do not rely on a single signal.
- Record assessment attempt timestamps and durations.
- Note: automated seat-time tracking is an estimate; pair it with the attestation. Flag exact CDPH seat-time expectations as Needs confirmation.

### H.12 Learner progress dashboard recommendations
- Course-level completion progress block; per-module checklist; Year 1 / Year 2 progress bars.
- "What's next / what's locked" guidance; estimated minutes remaining per module.
- Admin/faculty dashboard: cohort completion, attempt counts, time logs, attestation status, flagged items.

### H.13 Mobile-first design notes
- Responsive Moodle theme (Boost-based); single-column lessons; tap-friendly targets; short scrollable lesson pages; H5P responsive content; avoid hover-only interactions; downloadable summaries for low-connectivity.

### H.14 Accessibility requirements
- WCAG 2.1 AA target: captions/transcripts for media, alt text, color-independent cues, keyboard navigability, sufficient contrast, readable fonts, accessible tables, screen-reader-tested H5P, content warnings on sensitive modules (16, 17).

### H.15 No-PHI / no-real-data guardrails (LMS)
- Section 0 no-PHI agreement (required).
- Standing banner on all free-text/upload activities: "Use fictional data only. Do not enter real resident, patient, or facility information."
- Admin policy: periodic review and redaction of any free-text submissions; restrict uploads to course-related fictional artifacts.

### H.16 Audit evidence export plan
See Section Q.

---

## I. Assessment Plan

1. **Low-stakes knowledge checks (formative)** — one per module (KC-M10…KC-M17), 8–10 auto-graded items each, unlimited attempts, per-item feedback, completion-gated. Reinforce scope-of-practice in feedback.
2. **Scenario-based activities (applied judgment)** — one per module (S-M10…S-M17), branching decisions, scope guardrails in every branch, fictional residents only.
3. **Summative assessments** — **Year 1 Assessment** (covers M10–M13) and **Year 2 Assessment** (covers M14–M17), each drawn from question banks; **80% pass**; limited attempts; review options restricted (no answer key exposed). A cumulative end-of-course assessment is optional if the master packet requires one (Needs confirmation) — default is the two Year assessments.
4. **Pass threshold:** 80% minimum unless master packet says otherwise.
5. **Remediation guidance after failed attempts:** On fail, learner is routed to targeted module review (the specific lessons mapped to missed objectives) before the next attempt; remediation text references objectives, not specific answers.
6. **No final answer key shown to learners.** Learners see score + objective-level remediation only.
7. **Internal answer key** maintained separately for administrator/faculty use (see workbook `Assessment_Blueprint` and each module PDF's *Internal Answer Key Appendix*); never published in the learner-facing course.
8. **Scope-of-practice guardrails** embedded in every scenario and many knowledge-check rationales.
9. **No PHI / fictional only** across all items.

---

## J. Final Assessment Blueprint

Default structure = two Year-level summative assessments (no single high-stakes final), with an optional cumulative final if required by the master packet.

| Item | Year 1 Assessment | Year 2 Assessment |
| --- | --- | --- |
| Scope | Modules 10–13 | Modules 14–17 |
| Source of items | Year 1 module question banks | Year 2 module question banks |
| # items (recommended) | 24 (≈6 per module) | 24 (≈6 per module) |
| Item types | MCQ, T/F, matching, scenario-based MCQ | Same |
| Pass threshold | 80% | 80% |
| Attempts | up to 3 (configurable) | up to 3 |
| Question/answer order | shuffled | shuffled |
| Review options | score + remediation only; correct answers hidden | same |
| Remediation on fail | objective-mapped module review, then re-attempt | same |
| Learner visibility of key | none | none |
| Admin/faculty key | internal answer key (separate) | internal answer key (separate) |
| Completion effect | unlocks Year 1 completion roll-up | contributes to certificate gate |

Blueprint coverage rule: each summative item maps to at least one source objective; the workbook `Assessment_Blueprint` sheet holds stems, choices, correct answers, rationales, remediation, and visibility flags for the seed item set.

---

## K. Certificate Gate and Completion Logic

Certificate issuance is **blocked** until every gate item is satisfied. The certificate uses placeholder approval/provider/course identifiers only.

| Gate item | Required condition | LMS evidence source | Manual review? |
| --- | --- | --- | --- |
| Identity confirmed | Section 0 identity checkpoint complete | Section 0 activity completion + attestation | Optional |
| No-PHI agreement | Accepted in Section 0 | Activity completion record | No |
| Year 1 modules complete | M10–M13 all activities complete | Activity completion roll-up | No |
| Year 1 assessment passed | ≥ 80% | Gradebook (grade-to-pass) | No |
| Year 2 modules complete | M14–M17 all activities complete | Activity completion roll-up | No |
| Year 2 assessment passed | ≥ 80% | Gradebook (grade-to-pass) | No |
| Seat-time evidence | Minimum documented engaged time met | Logs / time reports / min-time conditions | Recommended spot-check |
| Learner attestation/affidavit | Final affidavit submitted | Assignment/Feedback submission | Recommended |
| Approval status confirmed | **Provider/course approval + certificate wording confirmed** | Master packet / CDPH confirmation | **Required — currently NOT met (Draft)** |

**Completion logic:** Course completion requires all module roll-ups + both Year assessments passed + attestation. The certificate activity (Moodle `mod_customcert` or `mod_certificate`) is restricted behind course completion. **Until "Approval status confirmed" is true, no certificate may be issued or advertised — the course remains in Draft.**

---

## L. Learner Attestation / Affidavit Workflow

1. **Enrollment attestation (Section 0):** Learner confirms identity (legal name; CNA number only if master packet requires — Needs confirmation), agrees to academic-integrity terms, and accepts the **no-PHI agreement**.
2. **Per-Year integrity attestation:** Before each Year assessment, learner re-attests that they are personally completing the work without prohibited assistance.
3. **Final affidavit (pre-certificate):** Learner submits a signed affidavit attesting that (a) they personally completed all online CE work, (b) the time logged reflects their genuine engagement, (c) they understand this is online CE only and does not include clinical hours, and (d) they used no real resident/facility data.
4. **Storage:** Attestations stored as activity submissions with timestamps; included in the audit evidence export (Section Q).
5. **Template:** See Section M (Draft Course/Application Support Content) item 11 and the PDF packet for the affidavit template.

---

## M. Draft Course / Application Support Content

> All items below are **Draft — Pending Approval**. No real approval/provider/course numbers are used.

1. **CNA CE course/application support content (summary):** Online CE course converting CCCCO Modules 10–17 into 24 online CE hours across a two-year renewal cycle, delivered via Moodle, with formative knowledge checks, scenario-based judgment exercises, two summative Year assessments (80% pass), identity/attestation controls, and a gated certificate. Online CE only; no clinical hours.
2. **Course outline:** Section 0 orientation → Year 1 (M10 Vital Signs, M11 Nutrition, M12 Emergency Procedures, M13 Long Term Care Patient/Resident) → Year 1 Assessment → Year 2 (M14 Rehabilitative Nursing, M15 Observation and Charting, M16 Death and Dying, M17 Patient/Resident Abuse) → Year 2 Assessment → Attestation → Certificate gate.
3. **Course objectives (course-level):** Upon completion, the learner will be able to apply, at the cognitive/observation/reporting level appropriate to CNA scope, the knowledge in Modules 10–17: measuring-and-reporting concepts for vital signs; nutrition/hydration support; scope-safe emergency response; long-term-care and dementia-sensitive care; restorative care; objective observation and charting; end-of-life care; and abuse prevention and mandated reporting. (No hands-on competency is claimed.)
4. **24-hour allocation table:** See Section D.
5. **Year 1 / Year 2 split table:** See Section E.
6. **Source Modules 10–17 mapping table:** See Sections C and F.
7. **Proposed flyer/brochure text:** See Section N.
8. **Sample certificate text:** See Section O.
9. **Course evaluation form:** See Section P.
10. **Attendance / completion / proof-of-participation policy (draft):** Participation is evidenced by activity-completion tracking, time/log data, assessment attempts, and learner attestation. A learner is deemed to have "attended" an online CE module when all activity-completion conditions are met and the minimum documented engaged time is recorded. Proof-of-participation = LMS completion report + attestation + assessment records, retained per the recordkeeping policy.
11. **Learner attestation / affidavit template (draft):**
    > "I, [Learner Legal Name], [CNA Certificate No.: __________ — if required], attest that I personally completed all online continuing education activities in this course; that the time recorded reflects my genuine engagement; that I understand this course provides **online CE hours only and does not include clinical hours** and does not by itself complete all CNA renewal requirements; and that I did not enter any real resident, patient, or facility information. Signature: __________ Date: __________." (Draft — Pending Approval.)
12. **Recordkeeping policy (draft):** See Section Q.
13. **Refund / cancellation policy (placeholder):** "[Provider Name placeholder] refund/cancellation terms to be confirmed and inserted from the institution's approved BPPE/CDPH-aligned policy. Draft placeholder — do not publish until confirmed." (Repo contains BPPE refund/pro-rata source material to reconcile — Needs confirmation.)
14. **Advertising compliance checklist:** See Section T.
15. **LMS evidence checklist:** See Section Q.
16. **SME / compliance review checklist:** See Sections T and U.
17. **Owner approval checklist before submission:** See Section W.

---

## N. Draft Flyer / Brochure Copy

> **Draft - Pending Approval.** *Pending applicable approval. Do not advertise, issue certificates, or represent this course as approved until approval status, provider/course identifiers, and certificate wording are confirmed.*

**California CNA Recertification Online Continuing Education: Modules 10–17 (Draft)**

- **Who it's for:** California Certified Nursing Assistants completing online continuing education toward CNA renewal.
- **What it is:** A 100% online, self-paced continuing education course built on the CCCCO Nurse Assistant Model Curriculum, Modules 10–17, organized for the two-year renewal cycle.
- **Source module sequence (Modules 10–17):** Vital Signs · Nutrition · Emergency Procedures · Long Term Care Patient/Resident · Rehabilitative Nursing · Observation and Charting · Death and Dying · Patient/Resident Abuse.
- **What you'll learn (summary):** Scope-safe vital-signs concepts and reporting; nutrition, hydration, and feeding support; recognizing and responding to emergencies within CNA scope; long-term-care and dementia-sensitive care; restorative care and ADLs; objective observation and charting; compassionate end-of-life care; and abuse prevention and mandated reporting.
- **Draft online CE hours:** 24 online CE hours (draft design math) across **Year 1 (12 hours)** and **Year 2 (12 hours)**.
- **Delivery:** Online, asynchronous, mobile-friendly (Moodle).
- **Completion requirements:** Complete all module activities, pass each Year assessment at 80%, meet documented seat-time, and submit the learner attestation.
- **Refund / cancellation:** [Placeholder — provider policy to be confirmed before publication.]
- **Important disclaimers:** This is **online continuing education only.** It does **not** include or validate clinical/hands-on hours, does **not** expand CNA scope of practice, and does **not** by itself complete all California CNA renewal requirements. No real resident or facility information is used in this course. **Pending approval — not yet an approved course.**

---

## O. Draft Certificate Text

> **Draft - Pending Approval.** Do not issue. Placeholder identifiers only; no real approval/provider/course number is used.

```
[PROVIDER NAME PLACEHOLDER]
Certificate of Completion — Online Continuing Education (DRAFT)

This certifies that

    [Learner Legal Name]
    CNA Certificate No.: [____________]   (if required by approving authority)

has completed the online continuing education course

    California CNA Recertification Online Continuing Education: Modules 10–17

Online CE Hours: [24 online CE hours — DRAFT design math]
Completion Date: [____________]
Unique Certificate ID: [AUTO-GENERATED-PLACEHOLDER]

Approval / Provider / Course No.: [APPROVAL PLACEHOLDER — PENDING APPROVAL]
Authorized Signature: ____________________   Title: [____________]

This certificate reflects ONLINE CONTINUING EDUCATION HOURS ONLY.
It does NOT include or represent clinical/hands-on hours and does not
expand CNA scope of practice.

PENDING APPLICABLE APPROVAL. This certificate is a DRAFT and may not be
issued, advertised, or represented as approved until approval status,
provider/course identifiers, and certificate wording are confirmed.
```

Certificate field checklist (all present): learner legal name; CNA certificate number field (conditional on master packet — Needs confirmation); course title; completion date; provider name placeholder; approval/provider/course number placeholder; online CE hours placeholder; signature/title placeholder; unique certificate ID placeholder; approval placeholder language; "online CE hours only" statement; "does not include clinical hours" statement.

---

## P. Course Evaluation Form

> Draft. Administered at end of each Year and/or end of course. Anonymous option recommended; no PHI.

1. The learning objectives were clearly stated. (Strongly disagree → Strongly agree, 1–5)
2. The content reflected the source Modules 10–17 accurately. (1–5)
3. The scenarios helped me apply CNA judgment within scope. (1–5)
4. The knowledge checks and assessments fairly measured the objectives. (1–5)
5. The online platform was easy to navigate on my device. (1–5)
6. The estimated time matched my actual time. (1–5)
7. Accessibility features met my needs. (1–5 / N/A)
8. I understood that this is online CE only and does not include clinical hours. (Yes/No)
9. What was most useful? (free text — *no real resident/facility information*)
10. What should be improved? (free text — *no real resident/facility information*)
11. Overall rating of this CE course. (1–5)

---

## Q. Recordkeeping and Audit Evidence Plan

**Recordkeeping policy (draft):** Maintain, for each learner, the enrollment record, identity-confirmation record, activity-completion data, time/log data, knowledge-check and assessment attempts/scores, attestations/affidavit, and certificate record (once approved). Retention period: **[Needs confirmation — set to the longer of CDPH and BPPE requirements; placeholder pending confirmation].** Store in the LMS with secured backups; restrict access to authorized administrators/faculty.

**Audit evidence log (what / generated by / stored where / retention / responsibility / export):**

| Evidence item | Generated by | Stored where | Retention | Responsibility | Export method |
| --- | --- | --- | --- | --- | --- |
| Enrollment & identity record | Section 0 / LMS enrollment | Moodle user + activity records | [confirm] | LMS admin | CSV/PDF export |
| Activity completion data | Module activities | Moodle completion report | [confirm] | LMS admin/faculty | Completion report export (CSV) |
| Time / participation logs | Moodle logs | Moodle logs/reports | [confirm] | LMS admin | Logs export (CSV) |
| Knowledge-check attempts | Quizzes (formative) | Gradebook/quiz reports | [confirm] | Faculty | Quiz report export |
| Year assessment attempts/scores | Summative quizzes | Gradebook | [confirm] | Faculty | Grade export |
| Scenario decision logs | Lesson/H5P | Activity reports | [confirm] | Faculty | Report export |
| Learner attestation / affidavit | Assignment/Feedback | Submission records | [confirm] | LMS admin | PDF/CSV export |
| Course evaluation responses | Feedback/Questionnaire | Feedback module | [confirm] | Admin | CSV export |
| Certificate record (post-approval) | Certificate activity | Certificate logs | [confirm] | LMS admin | PDF + verification ID |

**LMS evidence checklist:** completion report ✓ · time logs ✓ · assessment scores ✓ · scenario logs ✓ · attestation ✓ · evaluation ✓ · certificate record (post-approval) ✓ · periodic no-PHI review ✓.

---

## R. Supporting XLSX Workbook Plan

A supporting workbook is generated at `CNA_Recert_Modules_10_17_24HR_LMS_BUILD_WORKBOOK.xlsx` (build script: `build_workbook.py`). It is a build-support and defensibility artifact only; this markdown package remains the primary deliverable. Sheets:

1. `Course_Map` — Year, source module #, title, online CE hours, est. minutes, source reference, completion requirement, evidence artifact, SME/compliance flag.
2. `Module_Source_Map` — source module #, title, source topic, required content to preserve, LMS destination, assessment linkage, notes/risks.
3. `LMS_Activity_Map` — activity ID, year, source module #, activity name, Moodle activity type, learner action, completion tracking setting, restrict-access rule, gradebook category, evidence generated.
4. `Assessment_Blueprint` — assessment ID, source module #, question type, stem, answer choices, correct answer, rationale, remediation, learner visibility, admin/faculty visibility.
5. `Certificate_Gate` — gate item, required condition, LMS evidence source, manual review needed, approval placeholder, risk if omitted.
6. `Application_Packet_Checklist` — packet item, draft status, owner, source reference, missing information, approval status, notes.
7. `SME_Compliance_Flags` — item ID, source module #, flag type, issue, risk level, reviewer needed, required action, status.
8. `Audit_Evidence_Log` — evidence item, generated by, stored where, retention period, review responsibility, export method, notes.

---

## S. PDF-Ready Module Documentation Packet

PDF-ready Markdown files are written to `./pdf-ready/` with exact target file names and a conversion README. If direct PDF generation is unavailable in your environment, convert the Markdown with the instructions in `pdf-ready/README_PDF_CONVERSION.md`.

- `CNA_Recert_Modules_10_17_24HR_Course_Documentation_Packet.md` → `...Packet.pdf`
- `CNA_M10_Vital_Signs.md` → `CNA_M10_Vital_Signs.pdf`
- `CNA_M11_Nutrition.md` → `CNA_M11_Nutrition.pdf`
- `CNA_M12_Emergency_Procedures.md` → `CNA_M12_Emergency_Procedures.pdf`
- `CNA_M13_Long_Term_Care_Resident.md` → `CNA_M13_Long_Term_Care_Resident.pdf`
- `CNA_M14_Rehabilitative_Restorative_Nursing.md` → `CNA_M14_Rehabilitative_Restorative_Nursing.pdf`
- `CNA_M15_Observation_and_Charting.md` → `CNA_M15_Observation_and_Charting.pdf`
- `CNA_M16_Death_and_Dying.md` → `CNA_M16_Death_and_Dying.pdf`
- `CNA_M17_Patient_Resident_Abuse.md` → `CNA_M17_Patient_Resident_Abuse.pdf`

---

## T. Compliance Review Checklist

- [ ] Approval/provider/course identifiers are placeholders only; no real numbers used anywhere.
- [ ] Every learner-facing surface states "online CE only" and "no clinical hours."
- [ ] No claim that the course alone completes all CNA renewal requirements.
- [ ] "24 online CE hours" labeled as draft design math.
- [ ] Module titles match the source CCCCO titles (Module 13 = "Long Term Care Patient/Resident"; Module 14 = "Rehabilitative Nursing").
- [ ] No standalone Infection Control module added.
- [ ] All scenarios fictional; no PHI/real resident/facility names.
- [ ] No-PHI agreement and banners present on all free-text/upload activities.
- [ ] Scope-of-practice guardrails in every scenario and key rationales.
- [ ] Mandated-reporter content (M17) and emergency content (M12) reviewed against current CA requirements.
- [ ] Refund/cancellation, recordkeeping retention, and identity-data fields confirmed against master packet/BPPE/CDPH.
- [ ] Master-packet structure conflict (12-Unit vs Modules 10–17) resolved before any CDPH-facing use.
- [ ] Advertising checklist (below) passed.

**Advertising compliance checklist:** flyer marked "Draft - Pending Approval" ✓ · no approved-provider/approved-course language except placeholder ✓ · no full-renewal claim ✓ · no clinical-hours claim ✓ · no scope-expansion claim ✓ · no-PHI warning present ✓ · refund/cancellation placeholder present ✓.

---

## U. SME Review Checklist

- [ ] Clinical accuracy of vital-signs ranges and factors (M10).
- [ ] Therapeutic-diet list and aspiration precautions current (M11).
- [ ] Emergency response sequence and code list align with facility + current AHA/ARC language; hands-on disclaimer present (M12).
- [ ] Dementia-sensitive/person-centered care language current (M13).
- [ ] ROM/restorative content stays at assist/observe level (M14).
- [ ] Charting rules and abbreviation/do-not-use list current; objective vs subjective accurate (M15).
- [ ] End-of-life/hospice content and postmortem steps align with policy; sensitivity note present (M16).
- [ ] Abuse types, mandated-reporter channels, timelines, and ombudsman framing current for California (M17).
- [ ] All objectives map to source CCCCO performance standards.
- [ ] Internal answer keys correct and kept out of the learner-facing course.
- [ ] SME/instructor of record assignment confirmed (master packet references Vanessa Valerio for the CNA lane — confirm assignment for this Modules 10–17 build).

---

## V. Open Questions / Missing Packet Items

1. **STRUCTURE CONFLICT (top priority).** The master packet's official 24-hour allocation is **12 Units × 2 hours** (`24_HOUR_CNA_COURSE_MATRIX_FINAL.md`, `CDPH_192B_COURSE_LIST_ATTACHMENT.md`), not Modules 10–17. Decide which structure is submitted to CDPH and whether the Modules 10–17 build is (a) an internal content lane that rolls up into the 12-Unit submission, or (b) a separate/updated submission requiring CDPH reconciliation. **Needs confirmation (owner + SME + CDPH).**
2. **Hour allocation.** The even 3-hours-per-module (24h) allocation is a draft CE design normalization; the source CCCCO theory hours are uneven (M10=3, M11=2, M12=2, M13=5/3, M14=2, M15=4, M16=2, M17=6). Confirm whether CDPH expects source-proportional hours or a normalized CE allocation. **Needs confirmation.**
3. **Approval status & identifiers.** No approved provider/course number exists for this Modules 10–17 lane in the reviewed files; certificate and advertising remain Draft. **Needs confirmation.**
4. **Pass threshold.** 80% assumed; confirm CDPH/provider-required threshold. **Needs confirmation.**
5. **CNA certificate number collection.** Whether the LMS must capture the learner's CNA number for the certificate. **Needs confirmation.**
6. **Seat-time expectation.** Exact CDPH online seat-time/clock-hour definition and whether minimum-time gating is required. **Needs confirmation.**
7. **Renewal completeness.** Whether/how this online CE counts toward the full CNA renewal requirement (and any in-service/clinical/employment-verification components). **Needs confirmation.**
8. **Retention period.** Recordkeeping retention duration (CDPH vs BPPE). **Needs confirmation.**
9. **Refund/cancellation policy.** Pull the institution's approved policy from BPPE source material; placeholder only at present. **Needs confirmation.**
10. **Module 13 SNF/ICF variant.** The source distinguishes SNF/ICF vs non-SNF/ICF hour requirements; confirm which applies. **Needs confirmation.**
11. **Cumulative final.** Whether a single cumulative final is required in addition to the two Year assessments. **Needs confirmation (default: two Year assessments).**
12. **Production auth/identity method.** SSO/proctoring expectations, if any. **Needs confirmation.**

---

## W. Final Build Handoff Checklist

- [ ] Owner reviews and resolves the structure conflict (Open Item #1).
- [ ] SME of record confirmed and signs off on content accuracy (Section U).
- [ ] Compliance reviewer signs off (Section T).
- [ ] Hour allocation and pass threshold confirmed against master packet/CDPH.
- [ ] Refund/cancellation, retention, and identity-data fields finalized.
- [ ] Approval/provider/course identifiers obtained and inserted (until then, remain Draft).
- [ ] Moodle shell built per Section H; completion/restrict/quiz settings verified.
- [ ] Question banks and scenarios loaded; internal answer keys stored separately.
- [ ] Certificate activity gated; "Approval status confirmed" condition wired and currently OFF.
- [ ] No-PHI agreement, banners, and accessibility features verified.
- [ ] Audit evidence export tested (Section Q).
- [ ] Flyer/certificate/eval reviewed and kept in Draft until approval.
- [ ] Final owner approval recorded before any submission or learner launch.

---

*Do not advertise, issue certificates, or represent this course as approved until the official approval status, provider/course identifiers, and certificate wording are confirmed.*
