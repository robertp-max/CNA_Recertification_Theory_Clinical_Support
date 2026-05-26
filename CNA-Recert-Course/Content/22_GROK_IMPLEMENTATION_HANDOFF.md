# 22_GROK_IMPLEMENTATION_HANDOFF.md
# Grok Implementation Handoff Guide

---

## Files Grok Should Create Next

| File | Source | Repo Path | Purpose |
|---|---|---|---|
| Module 2â€“6 full content (like Module 0 and 1) | 06_THEORY_MODULE_TEMPLATE_PACK.md + NATP sources | CNA-Recert-Course/content/theory/ | Learner-facing content for each module |
| Moodle Quiz XML for each module quiz | 11_QUIZ_BANK_MASTER.csv | CNA-Recert-Course/moodle-import/ | Importable quiz banks |
| Moodle Quiz XML for final exam | 10_FINAL_EXAM_POOL_50.md | CNA-Recert-Course/moodle-import/ | 50-question final exam pool |
| Clinical support page content | 07_CLINICAL_SUPPORT_TEMPLATE_PACK.md | CNA-Recert-Course/content/clinical-support/ | Learner-facing optional content |
| Skills refresh job aids (1-page per skill area) | NATP Modules 10â€“14 | CNA-Recert-Course/content/clinical-support/job-aids/ | Downloadable/viewable skill summaries |
| TTS narration scripts for Modules 2â€“6 | 16_TTS_NARRATION_PACKAGE.md format | CNA-Recert-Course/tts/ | Optional audio scripts |

## How to Convert Markdown to Moodle

| Content Type | Markdown Source | Moodle Activity | Conversion Method |
|---|---|---|---|
| Lesson content (multi-screen) | Module full content .md files | Moodle Book or Lesson | Create Book with chapters per lesson; paste markdown as HTML |
| Single-page content | Page text in .md files | Moodle Page | Paste as HTML |
| Knowledge checks | Quiz items in .csv | Moodle Quiz | Convert CSV to Moodle XML using script or manual entry |
| Final exam | 50-question pool in .csv | Moodle Quiz with question bank category | Import to question bank; configure random draw |
| Acknowledgements | Feedback prompts in .md | Moodle Feedback activity | Create Feedback with required completion |
| Affidavit | 13_AFFIDAVIT_TEXT.md | Moodle Feedback or Assignment | DRAFT â€” create as Feedback with required text |

## What NOT to Implement Yet

- âŒ Production certificate issuance (pending CDPH approval)
- âŒ Cloned-voice TTS generation (pending authorization)
- âŒ Scheduler plugin for clinical support (not validated)
- âŒ LTI simulation integrations
- âŒ SMS reminders
- âŒ Custom SQL reports (post-MVP)
- âŒ Any activity that claims clinical-hour credit

## What Must Remain Pending Approval

- Certificate text and fields (DRAFT watermark required on staging)
- Affidavit wording (DRAFT pending legal)
- Provider NAC# on certificate
- E-signature method
- Active-time plugin selection (use manual review hold as fallback)

## How to Preserve Certificate Gates

1. Set course completion to require ALL theory activities (Modules 0â€“7)
2. Use Restrict Access to chain: M0 â†’ M1 â†’ M2 â†’ M3 â†’ M4 â†’ M5 â†’ M6 â†’ M7
3. Set final exam quiz to require Module 6 quiz pass
4. Set certificate activity to require: course completion + final exam pass + affidavit completion + admin hold clear
5. NEVER include any CS (clinical support) activity in course completion criteria

## How to Keep Clinical Support Non-Gating

1. Place all CS activities in a SEPARATE course section labeled "Optional Clinical Support"
2. Set all CS activity completion to "Do not indicate completion" or "Students can manually mark"
3. NEVER add CS activities to the course completion criteria
4. NEVER add CS activities to Restrict Access conditions for any required activity
5. NEVER add CS activities to the certificate availability conditions
6. Verify with QA tests: complete all theory â†’ skip all CS â†’ certificate should release

## How to Avoid PHI

1. Include PHI warning text in every Assignment description
2. Enable "Require submission statement" on Assignments with custom PHI warning
3. Admin reviews all uploads for PHI
4. No free-text question types in graded quizzes
5. Scenario questions use only fictional names: "Mrs. J," "Mr. T," "Resident A"
6. Never use real facility names

## QA Scripts to Run After Import

1. **QA-001:** Approval metadata pending â†’ certificate blocked
2. **QA-002:** Missing legal name â†’ certificate blocked
3. **QA-003:** Missing CNA number â†’ certificate blocked
4. **QA-004:** Missing acknowledgement â†’ certificate blocked
5. **QA-005:** Theory activity skipped â†’ certificate blocked
6. **QA-006:** Interaction skipped â†’ certificate blocked
7. **QA-007:** Active-time threshold not met â†’ certificate blocked (or manual review hold)
8. **QA-008:** Failed exam â†’ certificate blocked
9. **QA-009:** Affidavit missing â†’ certificate blocked
10. **QA-011/012/013:** Clinical support skipped â†’ certificate STILL releases âœ…
11. **QA-015:** Blank certificate field â†’ fails QA
12. **QA-019:** Direct certificate URL â†’ blocked
13. **QA-020:** Direct final exam URL â†’ blocked
