# 06_THEORY_MODULE_TEMPLATE_PACK.md
# Theory Module Template Pack â€” Modules 2 through 7

This template is designed so Grok (or any implementation agent) can scale each module into Moodle-ready markdown and CSV artifacts by filling in the placeholders with NATP source content.

---

## TEMPLATE â€” Repeat for Each Module (2, 3, 4, 5, 6, 7)

### Module [NUMBER]: [TITLE]

---

#### A. Module Title
**Module [NUMBER]: [FULL TITLE]**

#### B. Module Purpose
[1â€“2 sentences describing what this module covers and why it matters for working CNAs.]

#### C. Learning Objectives
By the end of Module [NUMBER], learners will be able to:
1. [Objective 1 â€” use action verb: Identify, Describe, Apply, Recognize, Explain, List, Distinguish]
2. [Objective 2]
3. [Objective 3]
4. [Objective 4]
5. [Objective 5]
6. [Objective 6]
7. [Objective 7 â€” if applicable]

*Map each objective to a specific NATP source section where possible.*

#### D. NATP Source References
| NATP Module | Relevant Sections | Content to Preserve | Page Range (approx.) |
|---|---|---|---|
| Module [XX] | Objectives [Xâ€“Y], Content sections [Aâ€“D] | [Key topics, procedures, vocabulary, safety points] | pp. [Xâ€“Y] |
| Module [XX] | [Additional] | [Additional] | pp. [Xâ€“Y] |

#### E. Legacy Source References (If Used)
| Legacy File | Use Type | Specific Use |
|---|---|---|
| CNA-CE-[XXX]_BUILD_SPEC.md | Style/format reference | [What was used] |
| CNA-CE-[XXX]_QUESTION_BANK.md | Question style reference | [What was used] |

**Rule:** Legacy content does NOT override NATP or current blueprint.

#### F. Lesson Skeleton (6 Lessons per Module)

| Lesson # | Lesson Title | Est. Minutes | NATP Source Section | Key Content Points | Interaction Type |
|---|---|---:|---|---|---|
| [X].1 | [Title] | [XX] | Module [XX], Obj [X] | [3â€“5 bullet points] | [Knowledge check / scenario / matching] |
| [X].2 | [Title] | [XX] | Module [XX], Obj [X] | [3â€“5 bullet points] | [Knowledge check / scenario] |
| [X].3 | [Title] | [XX] | Module [XX], Obj [X] | [3â€“5 bullet points] | [Knowledge check] |
| [X].4 | [Title] | [XX] | Module [XX], Obj [X] | [3â€“5 bullet points] | [Knowledge check / scenario] |
| [X].5 | [Title] | [XX] | Module [XX], Obj [X] | [3â€“5 bullet points] | [Knowledge check] |
| [X].6 | [Title] | [XX] | Module [XX], Obj [Xâ€“Y] | [Summary/review points] | [Module quiz introduction] |

**Total lesson time must approximate the module's allocated minutes from the syllabus table.**

#### G. Slide Text Skeleton (Per Lesson)

For each lesson, create 2â€“3 slides:

| Slide # | Lesson | Heading | Body (Key Points â€” 3â€“5 bullets or 1 short paragraph) |
|---:|---|---|---|
| [X] | [X.Y] | [Heading] | [Content] |

**Rule:** Each slide should contain no more than 200â€“250 words. Use bullet points, short paragraphs, and tables. Do not create dense text blocks.

#### H. Transcript Skeleton (Per Lesson)

For each lesson, create a TTS-ready transcript:

--- SEGMENT [MODULE]-[LESSON]-[SLIDE] --- [Narration text â€” conversational, clear, 8th-grade reading level] [Pronunciation notes for healthcare terms in brackets: e.g., (say: SFIG-moh-muh-NOM-uh-ter)] --- END SEGMENT ---


**Rule:** TTS is OPTIONAL. Text is the required learning medium. TTS must match written content exactly.

#### I. Quiz Pool Placeholder Format

For each module, create a minimum of 8 questions:

| Question ID | Module | Lesson | Type | Stem | Choice A | Choice B | Choice C | Choice D | Correct | Rationale | Difficulty | NATP Source | Final Exam Candidate | Needs SME Review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M[X]-Q-01 | [X] | [X.Y] | MC | [Stem text] | [A] | [B] | [C] | [D] | [Letter] | [Why correct; why others wrong] | Easy/Medium/Hard | Module [XX], Obj [Y] | Yes/No | Yes/No |

**Rules:**
- At least 2 scenario-based questions per module
- At least 1 select-all-that-apply if appropriate
- No PHI in any question stem
- All fictional names for any person referenced
- Mark any question not directly supported by uploaded NATP content as "Needs SME Review: Yes"

#### J. Scenario/Interaction Placeholder Format

| Interaction ID | Module | Lesson | Name | Type | Learner Prompt | Expected Response Type | Feedback Logic | Completion Rule | Certificate Gate |
|---|---|---|---|---|---|---|---|---|---|
| M[X]-INT-01 | [X] | [X.Y] | [Name] | [Scenario MC / Matching / Sequencing / Reflection prompt] | [Prompt text] | [MC selection / text entry / sequence order] | [Correct feedback / Incorrect feedback with guidance] | Attempted | Yes |

**Rules:**
- All required theory interactions are certificate-gate compatible
- Text-forward, mobile-friendly
- No required video
- No drag-heavy interactions without text alternative
- Reflection prompts must include PHI warning: "Do not use real patient or resident information"

#### K. Completion/Gate Metadata Format

| Field | Value |
|---|---|
| Module Number | [X] |
| Module Title | [Title] |
| Required/Optional | Required |
| Completion Type | Activity completion (all lessons + quiz pass) |
| Grade to Pass | 80% |
| Restrict Access Dependency | Module [X-1] quiz pass |
| Certificate Gate | Yes |
| Evidence Created | [Lesson completion, quiz attempts/scores, interaction attempts] |

#### L. Accessibility Checklist

- [ ] All content uses heading hierarchy (H1 > H2 > H3)
- [ ] Paragraphs are 3 sentences or fewer
- [ ] Plain language (8th-grade reading level target)
- [ ] Transcripts provided for any audio
- [ ] Alt text placeholder for any images (prefer no images)
- [ ] Tables use simple structure â€” no merged cells
- [ ] Color is not the only indicator of meaning
- [ ] Knowledge checks display one question at a time on mobile
- [ ] No required video content
- [ ] Keyboard navigable interactions
- [ ] Screen-reader compatible quiz formatting

#### M. Evidence Capture Notes

| Evidence Type | Moodle Source | Export Method | Audit Value |
|---|---|---|---|
| Lesson completion | Activity completion report | CSV export | Shows content viewed |
| Quiz attempt | Quiz report | CSV export | Shows assessment attempt, score, timestamp |
| Interaction attempt | Activity completion + attempt data | CSV export | Shows learner engagement |
| Active time | Time plugin report | Plugin export | Shows participation duration |

#### N. Non-PHI Wording Check

- [ ] No real patient/resident names in any content
- [ ] No real facility names
- [ ] No medical record numbers, room numbers, or identifiers
- [ ] All scenarios use fictional, de-identified examples
- [ ] Reflection/documentation prompts include explicit PHI warning
- [ ] Free-text fields include PHI prohibition notice

#### O. SME Review Notes

| Review Item | Reviewer Type | Status |
|---|---|---|
| Clinical accuracy of content | RN / Clinical Educator | Pending |
| CNA scope compliance | RN / Clinical Educator | Pending |
| Question accuracy and fairness | SME + Assessment Specialist | Pending |
| Source fidelity to NATP Modules | Content Developer + SME | Pending |
| Trauma-informed language (if applicable) | Clinical Psychologist / SME | Pending |

---

## MODULE-SPECIFIC NOTES

### Module 2: Resident Rights and Abuse Prevention
- **Primary NATP Source:** Module 17 (Patient/Resident Abuse) â€” 6 theory hours, 14 pages
- **Key content to preserve:** All abuse types, signs/symptoms, mandated reporting, prevention, negligence vs. abuse distinction, resident rights, restraints, HIPAA
- **Condensation challenge:** Module 17 is 6 hours originally; this module allocates 2 hours. Prioritize: abuse types, signs, reporting obligations, rights. Mark detailed legal definitions for supplementary reading.
- **Legacy reference:** CNA-CE-002 for question style

### Module 3: Dementia, Communication, Cultural Respect
- **Primary NATP Sources:** Module 13 (dementia/Alzheimer's/psychological sections), Module 16 (death/dying, cultural sensitivity)
- **Key content to preserve:** Alzheimer's stages, validation therapy, reality orientation, sundowner syndrome, catastrophic reactions, communication techniques, cultural/spiritual considerations, grief stages, comfort care
- **Placement decision:** Death/dying content from Module 16 is integrated here for cultural sensitivity and compassionate communication context. SME should confirm this placement.
- **Legacy reference:** CNA-CE-012 for end-of-life question style

### Module 4: Mobility, Falls, Workplace Safety
- **Primary NATP Sources:** Module 14 (Rehabilitative Nursing), Module 12 (Emergency Procedures)
- **Key content to preserve:** Restorative care philosophy, ADLs, adaptive devices, ROM types, complications of immobility, safe transfers, body mechanics, fall prevention, emergency response (choking, Heimlich, fire safety, emergency codes)
- **DO NOT imply:** Hands-on competency validation through online content
- **Legacy reference:** CNA-CE-004 (safety), CNA-CE-005 (body mechanics)

### Module 5: Nutrition, Skin Integrity, Vital Signs
- **Primary NATP Sources:** Module 11 (Nutrition), Module 10 (Vital Signs), Module 13 (integumentary/skin sections)
- **Key content to preserve:** Nutrients and food groups, therapeutic diets, dehydration/aspiration risks, feeding techniques, I&O measurement, pressure ulcer staging/prevention, VS measurement procedures, normal/abnormal ranges, pain scales
- **Heavy module:** Content from 3 NATP modules. Prioritize judgment and reporting content.
- **Legacy reference:** CNA-CE-006 (nutrition), CNA-CE-009 (vital signs)

### Module 6: Documentation, Change-of-Condition, Scope
- **Primary NATP Sources:** Module 15 (Observation and Charting), Module 13 (scope/professionalism)
- **Key content to preserve:** Objective vs. subjective observation, ABCs of observation, medical terminology/abbreviations, charting documents (ADL sheets, MDS, Kardex), legal charting rules, CNA scope of practice, reporting changes
- **Critical:** PHI avoidance instruction. All documentation practice must use fictional examples.
- **Legacy reference:** CNA-CE-003 (communication/documentation), CNA-CE-010 (professionalism)

### Module 7: Review, Final Exam/Test, Affidavit
- **Sources:** All NATP Modules 10â€“17 via question pool
- **Structure:** Practice review quiz (ungraded) â†’ Final Exam (25 questions, 80% pass, from 50-question pool) â†’ Affidavit/completion statement
- **Gate:** Final exam pass + affidavit completion â†’ certificate release
- **Affidavit:** See 13_AFFIDAVIT_TEXT.md â€” DRAFT only
- **No new instructional content in this module**
SECTION 6 â€” CLINICAL SUPPORT TEMPLATE PACK
07_CLINICAL_SUPPORT_TEMPLATE_PACK.md
