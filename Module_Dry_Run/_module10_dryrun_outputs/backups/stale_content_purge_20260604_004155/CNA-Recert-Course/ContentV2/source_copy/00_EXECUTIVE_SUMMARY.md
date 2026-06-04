# 00_EXECUTIVE_SUMMARY.md
# California CNA Recertification â€” Content Development Packet
# Executive Summary

**Project:** California CNA Recertification Theory + Optional Clinical Support  
**Provider:** CI Institute of Nursing  
**Platform:** Self-Hosted Moodle (4.5 LTS target)  
**Date:** 2026-05-28  
**Status:** Content-development pass â€” NOT production-ready; requires SME, compliance, and legal review  

---

## 1. Overall Design Approach

This packet delivers implementation-ready content artifacts for:

- **A. 12-hour asynchronous online theory course** (Modules 0â€“7) â€” partial California CNA renewal CE credit only
- **B. 12-hour optional clinical support pathway** (Clinical Support 1â€“7) â€” NOT California clinical-hour credit; NOT certificate-gating

All content is sourced primarily from **NATP Modules 10â€“17** (CCCCO Nurse Assistant Model Curriculum, Revised December 2018) and structured according to the **FINAL_UNIFIED_IMPLEMENTATION_BLUEPRINT.md** (the controlling document).

Design principles:
- Mobile-first, text-forward, low-bandwidth
- Short resumable units for exhausted working CNAs studying after shifts
- Formative checks + summative final exam
- No new video production required
- Optional TTS with transcript-ready text
- Layered evidence model (not Moodle logs alone)
- Certificate gate logic requiring identity, completion, interaction, active-time, exam pass, affidavit, and admin clearance

---

## 2. Authoritative Sources Used (Precedence Order)

| Priority | Source | File ID | Role |
|---:|---|---|---|
| 1 | FINAL_UNIFIED_IMPLEMENTATION_BLUEPRINT.md | 6a155b723463cd690af8d023 | Controlling architecture, compliance, and design document |
| 2 | README.md (Theory + Clinical Support project) | 6a155b723463cd690af8d022 | Current project scope and phase status |
| 3 | CERTIFICATE_GATE_POC_CONFIG.md | 6a155b723463cd690af8d021 | Certificate gate logic and restrict-access chain |
| 3 | QA_EXECUTION_TRACKER.md | 6a155b713463cd690af8d01d | 21 QA test cases for Prototype 1 |
| 3 | ACTIVE_TIME_POC_TEST_PLAN.md | 6a155b723463cd690af8d020 | Active-time validation test cases |
| 3 | REQUIRED_OPTIONAL_SEPARATION_CHECK.md | 6a155b713463cd690af8d01f | Required vs. optional separation verification |
| 3 | OPTIONAL_CLINICAL_HUB_STUB_SPEC.md | 6a155b713463cd690af8d01e | Clinical support hub structure and wording |
| 3 | PROTOTYPE_1_ACCEPTANCE_CRITERIA.md | 6a155b713463cd690af8d01c | Pass/fail criteria for Prototype Build 1 |
| 4 | California Laws - Health and Safety Code.docx | 6a155b763463cd690af8d046 | California regulatory excerpts |
| 5 | NATP Module 10: Vital Signs | 6a155bab3463cd690af8d047 | Source content â€” vital signs |
| 5 | NATP Module 11: Nutrition | 6a155bab3463cd690af8d048 | Source content â€” nutrition |
| 5 | NATP Module 12: Emergency Procedures | 6a155bab3463cd690af8d049 | Source content â€” emergency/safety |
| 5 | NATP Module 13: Long Term Care Resident | 6a155bab3463cd690af8d04a | Source content â€” body systems, aging, dementia, conditions |
| 5 | NATP Module 14: Rehabilitative Nursing | 6a155bab3463cd690af8d04b | Source content â€” restorative care, mobility, ADLs |
| 5 | NATP Module 15: Observation and Charting | 6a155bab3463cd690af8d04c | Source content â€” documentation, observation, MDS |
| 5 | NATP Module 16: Death and Dying | 6a155bab3463cd690af8d04d | Source content â€” end-of-life, comfort care |
| 5 | NATP Module 17: Patient/Resident Abuse | 6a155bac3463cd690af8d04e | Source content â€” abuse prevention, rights, reporting |
| 6 | CNA_ONLINE_CE_MOODLE_SHELL_MAP.md | 6a155b763463cd690af8d045 | Legacy 12-course shell mapping (secondary reference) |
| 6 | CNA_ONLINE_CE_COURSE_SHELL_BLUEPRINTS.md | 6a155b763463cd690af8d044 | Legacy course shell blueprints (secondary reference) |
| 6 | MOODLE_COMPLETION_AND_REPORTING_PLAN.md | 6a155b763463cd690af8d043 | Moodle completion configuration reference |
| 6 | CNA_CE_COURSE_HOUR_MATRIX.md | 6a155b753463cd690af8d036 | Legacy 12-course hour matrix (secondary reference) |
| 6 | CNA_LMS_COMPLIANCE_NARRATIVE.md | 6a155b723463cd690af8d025 | Compliance narrative for CDPH TPRU |
| 7 | Legacy CNA-CE-001 through CNA-CE-012 build specs | Various | Question style, build packaging reference |
| 7 | Legacy CNA-CE-001 through CNA-CE-012 question banks | Various | Assessment structure, wording reference |
| 8 | TTS_RUNTIME_ESTIMATE.md, TTS_NARRATION_SCRIPT.md, SLIDE_DECK_OUTLINE.md, QUESTION_COVERAGE_MAP.md, HANDOFF_INDEX.md | Various | Supporting reference artifacts |

---

## 3. Conflicts Resolved Between Current and Legacy Sources

| Conflict | Resolution |
|---|---|
| Legacy sources assume 24-hour / 12-course library structure | Current architecture is one 12-hour theory course + one 12-hour optional clinical support. Legacy structure is secondary reference only. |
| Legacy identity fields include DOB | Current gate model requires only legal name + CNA certificate number. DOB excluded unless controlling approval uploaded. |
| Legacy CNA-CE files sometimes imply full renewal eligibility | Current wording is partial-credit only. Online cap acknowledgement required. |
| Legacy clinical support wording sometimes implies clinical-hour credit | Clinical support is explicitly optional, non-gating, and non-credit unless CDPH approves in writing. |
| Legacy 2-hour-per-course time model vs. current variable-time modules | Current blueprint allocates 0.5â€“2.0 hours per theory module, totaling 12 hours. Legacy time model overridden. |

---

## 4. Module Count Assumption

**Theory Course (Required):** 8 modules (Module 0 through Module 7) = 12 hours  
**Clinical Support (Optional):** 7 units (Clinical Support 1 through Clinical Support 7) = 12 hours  

This structure follows the FINAL_UNIFIED_IMPLEMENTATION_BLUEPRINT.md Section 6 (Theory) and Section 7 (Clinical Support).

---

## 5. Major Risks and Open Dependencies

| Risk | Severity | Notes |
|---|---|---|
| CDPH provider/course approval not yet confirmed | **BLOCKER** | Cannot issue production CE certificates without approval |
| Certificate wording not yet approved | **BLOCKER** | All certificate language is DRAFT ONLY |
| E-signature acceptance unresolved | High | Wet-sign fallback may be needed |
| Active-time plugin not yet validated in staging | High | Manual review hold is fallback |
| Infection control not directly covered in NATP Modules 10â€“17 | Medium | No dedicated infection-control NATP module in 10â€“17 range. Must rely on scattered references + legacy CNA-CE-001 as draft. GAP_LOG item created. |
| H5P accessibility on mobile not validated | Medium | Text alternatives required for all H5P |
| TTS authorization not confirmed | Low | TTS is optional; text is primary |
| Clinical support perceived as required by learners | Medium | Requires clear labeling and pilot testing |

---

## 6. What Grok Can Implement From These Outputs

- Convert theory module markdown into Moodle Book/Page/Lesson activities
- Convert CSV question banks into Moodle Quiz XML import format
- Build Moodle course sections following the activity map
- Configure completion tracking and restrict-access chains
- Create certificate template with draft field mapping
- Build interaction/check activities as Moodle Quiz or Feedback activities
- Configure optional clinical support as separate non-gating course section

---

## 7. What Still Requires SME / Compliance / Legal Review

| Item | Review Type |
|---|---|
| All clinical accuracy and CNA scope claims | SME (RN/Clinical Educator) |
| Infection control content (gap â€” no dedicated NATP module 10â€“17) | SME + Source Review |
| Affidavit wording | Legal/Compliance |
| Certificate wording | Legal/Compliance/CDPH |
| Online cap acknowledgement language | Compliance |
| Partial-credit disclaimers | Compliance |
| TTS authorization | Program Owner/Legal |
| E-signature acceptance | Legal |
| Active-time plugin accuracy | QA/Technical |
| PHI avoidance in all examples | Compliance/Privacy |
| Trauma-informed language in dementia/communication module | SME/Clinical |
SECTION 2 â€” SOURCE-TO-COURSE CROSSWALK
01_SOURCE_TO_COURSE_CROSSWALK.md
