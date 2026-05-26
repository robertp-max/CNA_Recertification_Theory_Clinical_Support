# CONTENT_PACKAGE_BUILD_READINESS.md

**Repository:** CNA_Recertification_Theory_Clinical_Support
**Assessment Date:** Current build session
**Assessor:** Senior Repository Implementation Engineer / QA Lead

---

## WHAT IS READY FOR GROK PACKAGING

The following files are complete, QA-verified, and ready to be passed to the
next build phase for Moodle staging preparation:

| File | Path | Ready |
|------|------|-------|
| TIME_ALLOCATION_CORRECTION_NOTICE.md | /content/source-verification/ | âœ… |
| SOURCE_TITLE_VERIFICATION_PASS.md | /content/source-verification/ | âœ… |
| 24_THEORY_MODULE_02_...FULL.md | /content/theory/modules/ | âœ… |
| 25_THEORY_MODULE_03_...FULL.md | /content/theory/modules/ | âœ… |
| 26_THEORY_MODULE_04_...FULL.md | /content/theory/modules/ | âœ… |
| 27_THEORY_MODULE_05_...FULL.md | /content/theory/modules/ | âœ… Conditional â€” SME review of skin integrity required before production |
| 28_THEORY_MODULE_06_...FULL.md | /content/theory/modules/ | âœ… |
| 29_THEORY_MODULE_07_...FULL.md | /content/theory/modules/ | âœ… Time-corrected to 30 min |
| 30_FINAL_EXAM_POOL_50_COMPLETE.md | /content/theory/exam/ | âœ… |
| 31_QUIZ_BANK_MASTER_COMPLETE.csv | /content/csv/ | âœ… |
| 32_CLINICAL_SUPPORT_FULL_CONTENT.md | /content/clinical-support/ | âœ… |
| 33_OPTIONAL_CLINICAL_CONFIDENCE_CHECKS_COMPLETE.md | /content/clinical-support/confidence-checks/ | âœ… |
| 34_TTS_NARRATION_PACKAGE_COMPLETE.md | /content/theory/tts/ | âœ… Planning only â€” authorization required |
| 35_CONTENT_PACKAGE_INDEX_UPDATED.md | /content/index/ | âœ… |
| All QA files | /content/qa/ | âœ… |

---

## WHAT IS READY FOR MOODLE STAGING

The following content is ready to be converted and imported into a
**Moodle staging environment** (not production):

- Theory modules 24â€“28 (Modules 2â€“6): Convert Markdown to Moodle Lesson/Book HTML
- Module 7 (File 29): Convert to Moodle Lesson + Quiz + Questionnaire structure
- Quiz bank (File 31): Convert CSV to Moodle XML quiz import format
- Optional clinical support (File 32): Convert to Moodle non-gating section pages
- Confidence checks (File 33): Convert to Moodle Feedback/Questionnaire activities
- Final exam pool (File 30): Configure as Moodle Quiz with 25 random questions from 50-question pool

**Staging configuration must:**
- Keep all certificates DISABLED during staging
- Mark all optional content as optional with no prerequisites to CE content
- Not expose learner-facing placeholders during staging review
- Validate all 15 certificate gates before any learner access

---

## WHAT IS BLOCKED FROM PRODUCTION

The following items BLOCK production launch. Do not open the course to
real learners until all of these are resolved:

| Blocker | Risk # | Resolution Required |
|---------|--------|-------------------|
| CE provider NAC# not confirmed | R04 | Obtain from CDPH ATCS |
| CDPH contact placeholders not replaced | R05 | Insert real CDPH contact info |
| Affidavit legal review not complete | R03 | Legal/CDPH review and approval |
| Certificate language compliance review not complete | R03 | Legal review and approval |
| Active-time plugin not validated | R07 | Complete POC test plan |
| Certificate gate not built or tested | R08 | Build and test in staging |
| Course administrator contact placeholder not replaced | R11 | Insert real support contact |

---

## WHAT NEEDS SME REVIEW BEFORE PRODUCTION CONTENT APPROVAL

| Content Area | Files | SME Action Required |
|---|---|---|
| Module 1 â€” Infection Control | Prior session files; Q01â€“Q03, Q41 in Files 30â€“31; TTS Module 1 | Confirm against CDPH-approved infection control source. Update source references. Remove SME flag only after confirmation. |
| Module 5 Lesson 5.3 â€” Skin Integrity / Pressure Injury | File 27; Q21, Q38 in Files 30â€“31; Checks 06â€“07 in File 33; TTS-5-003 in File 34 | Upload confirmed NATP or CDPH source. Verify all content. Update source references. Remove flag only after confirmation. |

---

## WHAT NEEDS COMPLIANCE/LEGAL REVIEW

| Item | File | Review Type |
|------|------|------------|
| Affidavit attestation language ("under penalty of perjury") | File 29 Lesson 7.4 | Legal counsel / CDPH |
| Certificate copy text and CE credit claim | File 29 Lesson 7.5 | Legal counsel / CDPH |
| Optional clinical support disclaimers and signoff form language | File 32 Unit 6 | Compliance / Legal |
| CE course description and partial-credit boundary language | All module headers | Compliance / CDPH |
| TTS AI disclosure requirements (if TTS authorized) | File 34 | Legal / State AI disclosure rules |

---

## WHAT MUST NOT BE IMPORTED INTO PRODUCTION YET

- âŒ Do not enable the CE certificate in production Moodle
- âŒ Do not open any module to real learners before CE provider NAC# is confirmed
- âŒ Do not produce or deploy TTS audio without written authorization
- âŒ Do not remove any SME or compliance flags from any file
- âŒ Do not use the optional RN/preceptor signoff form as clinical-hour documentation
- âŒ Do not import Module 1 content into production until SME source confirmation is complete
- âŒ Do not use skin integrity exam questions (Q21, Q38) in a live exam until SME confirmation
