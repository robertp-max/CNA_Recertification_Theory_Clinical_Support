Act as the lead Codex CLI coordinator, principal instructional design architect, compliance-safe content engineer, React/Vite data integration lead, and QA-oriented multi-agent orchestrator.

You are working on the CNA Recertification Theory + Clinical Support project.

This task combines:

1. ContentV2 creation from the existing source content.
2. Narration CSV generation.
3. Narration master CSV generation.
4. XLSX production workbook generation.
5. Media prompt placeholder generation.
6. App data/schema generation.
7. Safe app data wiring into the standalone V2 UI.
8. Parallel GPT-5.5 worker orchestration using Codex CLI only.

Use Codex CLI.
Do not use Cursor Agent.
Do not use Cursor background agents.
Do not use Grok build.
Do not use Claude Code.
Do not use Gemini.
Do not use any IDE agent panel.

You may use terminal commands, Codex CLI, filesystem inspection, scripts, and repo tooling.

Primary mission:
Review the existing source content at:

C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\CNA-Recert-Course\Content

Create a complete ContentV2 package at:

C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\CNA-Recert-Course\ContentV2

Then safely wire ContentV2 into the app at:

C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\standalone-course-mvp

The app should continue using the selected V2 visual design. This is not a UI redesign task.

Approved V2 design reference:
Before content conversion or app wiring, inspect every file in:

C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\standalone-course-mvp\screenshots\v2-design

This folder is the approved V2 visual and interaction reference. It currently includes 19 PNG screen references plus:

* v2.tsx
* sign-in_card.tsx

Treat these files as a design contract for learner-facing app wiring:

1. 01-dashboard-default.png
2. 02-reviewer-tools-panel.png
3. 03-certificate-gate-locked.png
4. 04-modules-default.png
5. 05-module-0-orientation.png
6. 06-modules-unlocked-final-ready.png
7. 07-module-1-overview.png
8. 08-lesson-card-1-overview.png
9. 09-lesson-card-2-delivery.png
10. 10-lesson-card-3-challenge.png
11. 11-lesson-card-4-debrief.png
12. 12-module-1-assessment-splash.png
13. 13-module-1-assessment-quiz.png
14. 14-final-assessment-splash.png
15. 15-final-assessment-quiz.png
16. 16-final-result-passed.png
17. 17-certificate-gate-ready.png
18. 18-mock-certificate-preview.png
19. 19-clinical-hub.png

Design preservation requirements:

* Preserve the dark burgundy / near-black / stone / amber V2 design system.
* Preserve the compact professional layout, bordered panels, restrained cards, and existing spacing density.
* Preserve the current navigation model: Dashboard, CE Modules, Certificate Gate, Clinical Hub.
* Preserve the sign-in card design and logo treatment from sign-in_card.tsx.
* Preserve the reviewer tools label: Reviewer Tools - Prototype Controls Only.
* Preserve the certificate production-disabled behavior and mock certificate watermark/restrictions.
* Preserve the optional clinical hub's visual separation and PHI warning treatment.
* Do not replace the approved V2 UI with a new design system, landing page, Moodle-like page dump, or generic course shell.
* Content wiring may change displayed text/data, but must not degrade the approved screen structure.

Repository guardrail:
Do not execute if the current working directory does not resolve inside:

C:\AI\Git\CNA_Recertification_Theory_Clinical_Support

Before making any file changes, verify and report:

1. Current working directory
2. Git branch
3. Git status
4. Source content folder exists:
   C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\CNA-Recert-Course\Content
5. Target ContentV2 folder path:
   C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\CNA-Recert-Course\ContentV2
6. Standalone app exists:
   C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\standalone-course-mvp
7. package.json location for the standalone app
8. Current app content/data files
9. Current app route/view structure
10. Whether `codex` CLI is available
11. Output of:
    codex --help
12. Output of:
    codex exec --help
    if available
13. Output of any Codex CLI subagent/help command if available
14. Whether GPT-5.5 is available in local Codex CLI config or model list

Source-scope restriction:
Do not recursively process the entire C:\AI\Git folder.
Do not crawl backup folders, copied repos, node_modules, dist, build, .git, .vite, unrelated screenshots, prior agent runs, or unrelated repositories.

Only inspect these paths unless explicitly needed:
1. CNA-Recert-Course\Content
2. CNA-Recert-Course\ContentV2, only after creating it
3. standalone-course-mvp\screenshots\v2-design, for approved V2 design reference
4. standalone-course-mvp, only for app data wiring
5. project documentation files directly relevant to compliance/content rules

Backup safety:
Before write-heavy operations, confirm whether a backup exists outside the active repo.
If no backup is found, continue only after creating a git patch/snapshot record of the current state.

If git status is dirty before starting:
1. Record the dirty files in the preflight report.
2. Create a timestamped patch file:
   _RUN_BACKUPS\pre_content_v2_dirty_state_[YYYYMMDD_HHMMSS].patch
3. Do not overwrite existing uncommitted work.
4. Do not use destructive cleanup commands.

If repo path does not match, stop immediately and output:

STOPPED: Repo path mismatch. No files changed.

Branch:
Create or switch to:

content-v2-codex-gpt55-orchestration

Do not commit.
Do not push.
Do not create PR.
Do not alter production/staging remote deployment settings.

Model requirement:
Use GPT-5.5 for coordinator and worker agents where Codex CLI supports model selection.

Preferred model invocation:
Use the actual Codex CLI syntax discovered from help.

If the supported syntax matches standard model selection, use:

codex -m gpt-5.5

or:

codex exec -m gpt-5.5

Do not invent unsupported flags. Use the syntax confirmed by `codex --help` and `codex exec --help`.

Parallel agent requirement:
Use as many GPT-5.5 Codex CLI agents as needed, up to 32 concurrent workers at any single time.

Hard cap:
Maximum 32 GPT-5.5 workers concurrently.

Do not exceed 32 concurrent workers.

Concurrency sanity:
Do not launch 32 workers automatically just because the cap allows it.
First inspect source size and task split.
Use the smallest batch size that can complete the task correctly.
Start with a small pilot batch if needed to verify worker output format.
Scale up only after confirming workers write to isolated scratch folders correctly.
Report why the selected batch size was used.

Concurrency safety rule:
Do not allow parallel agents to write directly into the same canonical output files.
Do not allow parallel agents to modify app source files directly.
Do not allow parallel agents to modify the original Content folder.
Do not allow parallel agents to modify package.json, lockfiles, build config, routing, or login files.

Only the coordinator may merge final outputs into canonical ContentV2 and app data files.

If Codex CLI supports native subagents:
Use native subagents and instruct each subagent to write only to its assigned scratch folder.

If Codex CLI does not support native subagents through the local CLI:
Use separate Codex CLI executions with isolated scratch folders, or run sequential batches.
If true parallel execution is not safely supported, use the largest safe batch size and explain the limitation.

Preferred batch sizes:

* 32 if stable and supported
* 16 if 32 is too risky
* 8 if 16 is too risky
* 4 if lower concurrency is needed
* 1 only if Codex CLI cannot safely run parallel workers

Do not fake parallel execution. Report what actually ran.

Original Content folder rule:
Never modify:

CNA-Recert-Course\Content

The original Content folder is read-only.

If source content requires no update:
Copy or represent it in ContentV2 and mark it as “copied without changes.”

If source content requires V2 alignment:
Write the updated version only in ContentV2.

Target output root:
Create:

CNA-Recert-Course\ContentV2\

Worker output root:
Create:

CNA-Recert-Course\ContentV2\_agent_runs\

Each worker must write only to:

CNA-Recert-Course\ContentV2\_agent_runs\agent_[ID]\

Each worker folder must include:

1. AGENT_REPORT.md
2. SOURCE_FILES_REVIEWED.md
3. CONTENT_OUTPUT.md or assigned JSON/CSV draft
4. APP_LOCATION_MAP.md
5. NARRATION_DRAFT.csv if assigned narration
6. SME_FLAGS.md
7. COMPLIANCE_FLAGS.md
8. SOURCE_COVERAGE.md
9. MERGE_NOTES.md

Coordinator-only merge targets:
Only the coordinator may create or update these canonical files:

CNA-Recert-Course\ContentV2\00_CONTENTV2_EXECUTIVE_SUMMARY.md
CNA-Recert-Course\ContentV2\01_SOURCE_CONTENT_AUDIT.md
CNA-Recert-Course\ContentV2\02_CONTENTV2_SCHEMA.md
CNA-Recert-Course\ContentV2\03_MODULE_LESSON_4CARD_MAP.md
CNA-Recert-Course\ContentV2\04_MODULE_ASSESSMENT_MAP.md
CNA-Recert-Course\ContentV2\05_FINAL_ASSESSMENT_MAP.md
CNA-Recert-Course\ContentV2\06_NARRATION_PRODUCTION_GUIDE.md
CNA-Recert-Course\ContentV2\07_MEDIA_PROMPT_PLACEHOLDERS.md
CNA-Recert-Course\ContentV2\08_SME_COMPLIANCE_REVIEW_FLAGS.md
CNA-Recert-Course\ContentV2\09_APP_INTEGRATION_NOTES.md
CNA-Recert-Course\ContentV2\10_CONTENT_COVERAGE_AND_TIME_RECONCILIATION.md
CNA-Recert-Course\ContentV2\data\courseContentV2.json
CNA-Recert-Course\ContentV2\data\courseContentV2.schema.json
CNA-Recert-Course\ContentV2\data\courseContentV2.ts
CNA-Recert-Course\ContentV2\narration\tts_narration_import.csv
CNA-Recert-Course\ContentV2\narration\narration_master.csv
CNA-Recert-Course\ContentV2\narration\narration_metadata.json
CNA-Recert-Course\ContentV2\xlsx\CNA_RECERT_CONTENTV2_MASTER.xlsx

ContentV2 folder structure:
Create this exact structure:

CNA-Recert-Course\ContentV2\
  00_CONTENTV2_EXECUTIVE_SUMMARY.md
  01_SOURCE_CONTENT_AUDIT.md
  02_CONTENTV2_SCHEMA.md
  03_MODULE_LESSON_4CARD_MAP.md
  04_MODULE_ASSESSMENT_MAP.md
  05_FINAL_ASSESSMENT_MAP.md
  06_NARRATION_PRODUCTION_GUIDE.md
  07_MEDIA_PROMPT_PLACEHOLDERS.md
  08_SME_COMPLIANCE_REVIEW_FLAGS.md
  09_APP_INTEGRATION_NOTES.md
  10_CONTENT_COVERAGE_AND_TIME_RECONCILIATION.md
  data\
    courseContentV2.json
    courseContentV2.schema.json
    courseContentV2.ts
  narration\
    tts_narration_import.csv
    narration_master.csv
    narration_metadata.json
  xlsx\
    CNA_RECERT_CONTENTV2_MASTER.xlsx
  source_copy\
  updated_content\
  _agent_runs\

If an existing workbook is present, use it as a schema/style reference, not as the only truth:
CNA_RECERT_ALL_MODULES_NARRATION_MEDIA_PRODUCTION.xlsx

Source package facts to preserve:
The reviewed Content package contains 49 files at review time, including:

* required theory module files for Module 0 through Module 7
* optional clinical support full content and 21 confidence checks
* final exam pools and quiz bank CSVs
* TTS narration planning files
* QA, risk, source-verification, and build-readiness reports
* Raw\Claude batch files
* the existing narration/media XLSX and generator script

Verify the current source inventory again during preflight, but preserve these controlling facts unless a newer source file explicitly supersedes them:

* Required theory total: 720 minutes / 12 hours.
* Module 0 Orientation: 30 minutes.
* Module 1 Infection Control: 90 minutes; source gap active; all Module 1 infection-control content remains SME/source-review flagged.
* Module 2 Resident Rights and Abuse Prevention: 120 minutes.
* Module 3 Dementia, Communication, and Cultural Respect: 120 minutes.
* Module 4 Mobility, Falls, and Workplace Safety: 120 minutes.
* Module 5 Nutrition, Skin Integrity, and Vital Signs: 120 minutes; skin integrity / pressure injury content remains SME/source-review flagged.
* Module 6 Documentation, Change of Condition, and Scope: 90 minutes.
* Module 7 Review, Final Exam, and Affidavit/Certificate: 30 minutes, corrected from a prior 90-minute error.
* Optional Clinical Support includes 7 units and 21 confidence checks; it is optional, non-credit, non-gating, and not clinical-hour credit.
* Final exam pool includes 50 questions; learner-facing final results must not reveal the full answer key.
* Module 1 flagged questions include Q01, Q02, Q03, and Q41 where present in the complete exam/CSV sources.
* Skin integrity flagged questions include Q21 and Q38 where present in the complete exam/CSV sources.
* TTS scripts are planning artifacts only; do not synthesize audio or imply TTS production authorization.
* Affidavit, certificate wording, CE provider NAC#/provider identification, CDPH contact information, e-signature acceptance, active-time validation, and certificate production require compliance/legal/CDPH or owner approval before production.

Source precedence and duplicate handling:

* Use Content\index\35_CONTENT_PACKAGE_INDEX_UPDATED.md, Content\qa\CONTENT_PACKAGE_QA_REPORT.md, Content\qa\CONTENT_PACKAGE_RISK_REGISTER.md, Content\source-verification\SOURCE_TITLE_VERIFICATION_PASS.md, and Content\source-verification\TIME_ALLOCATION_CORRECTION_NOTICE.md as controlling QA/source-status references.
* When older and newer files overlap, use the newer complete artifact as the canonical source and preserve the older file only for traceability.
* Treat 30_FINAL_EXAM_POOL_50_COMPLETE.md as newer than 10_FINAL_EXAM_POOL_50.md.
* Treat 31_QUIZ_BANK_MASTER_COMPLETE.csv as newer than 11_QUIZ_BANK_MASTER.csv.
* Treat 34_TTS_NARRATION_PACKAGE_COMPLETE.md as newer than 16_TTS_NARRATION_PACKAGE.md.
* Treat 35_CONTENT_PACKAGE_INDEX_UPDATED.md as newer than 23_CONTENT_PACKAGE_INDEX.md.
* Treat Raw\Claude\Batch1.md and Raw\Claude\Batch2.md as secondary provenance/reference material, not direct learner-facing copy.
* Do not remove SME, compliance, legal, CDPH, TTS, PHI, active-time, certificate, or placeholder flags during V2 conversion.
* In 01_SOURCE_CONTENT_AUDIT.md, include a source manifest with every source file path, file type, role, canonical/secondary status, source flags, and how it was copied or represented in ContentV2.

Encoding and text hygiene:

* Write generated ContentV2 files as UTF-8.
* Do not introduce mojibake such as corrupted punctuation or replacement glyphs.
* If existing source text appears encoding-corrupted, preserve its meaning in ContentV2 using clean UTF-8 punctuation, and note the normalization in 01_SOURCE_CONTENT_AUDIT.md.
* Keep regulatory placeholders bracketed and explicit; do not fabricate CDPH contact data, provider numbers, approval metadata, or certificate wording.

Primary content objective:
Convert all available course content into a V2 app-ready instructional package that fits the selected V2 app design and the 4-card lesson player.

V2 learner flow:
Dashboard
→ CE Modules
→ Module 0 Orientation
→ Module 1 Overview
→ 4-Card Lesson Player
→ Module Assessment Splash
→ Module Assessment Quiz
→ Final Assessment Splash
→ Final Assessment Quiz
→ Final Result / Remediation
→ Certificate Gate
→ Mock Certificate Preview
→ Optional Clinical Support Hub

Content must support this flow.

Data-to-screen mapping requirement:
Generated ContentV2 data must support every approved V2 screen, not only markdown deliverables.

Map ContentV2 fields to these app surfaces:

* Dashboard hero, compliance notice, gate status, progress summary, theory/clinical cards, and audit safety copy.
* CE Modules list, curriculum summary, module cards, locked/unlocked/final-ready states, and module prerequisites.
* Module 0 orientation identity, acknowledgement, online-cap, no-PHI, and required-completion copy.
* Module overview pages for all required Modules 1 through 7, even if the current prototype visibly demonstrates Module 1 first.
* Lesson player card data for Overview, Delivery, Challenge, and Debrief/Remediation.
* Module assessment splash and quiz data for required modules where source supports assessment.
* Final assessment splash, quiz bank selection metadata, pass/fail result copy, remediation copy, and answer-key protection.
* Certificate gate locked/ready copy, affidavit gate copy, active-time explanation, disabled production certificate messaging, and mock certificate preview copy.
* Clinical Hub optional/non-gating copy, units, confidence checks, practice documentation support, and PHI/no-upload warnings.

Do not collapse Modules 2 through 7 into empty locked placeholders. If the current UI has not yet implemented routes for every module, still generate complete ContentV2 data for every required module and wire the adapter so future screens can consume it.

V2 lesson model:
Each lesson must use this structure:

Card 1 — Overview
Card 2 — Delivery
Card 3 — Challenge
Card 4 — Debrief / Remediation

For longer lessons, split Card 2 into:

* Card 2A
* Card 2B
* Card 2C
* Card 2D if needed

If any card narration would exceed approximately 1 minute, split the content into additional subcards or sublessons.

Narration target:

* preferred: 45–65 seconds
* acceptable: 35–75 seconds
* hard max: 75 seconds unless clearly flagged

Do not reduce content to meet narration duration.
Split content instead.

No source reduction rule:
Never reduce source content.
Never remove required meaning.
Never remove compliance warnings.
Never remove CNA safety/scope content.
Never remove assessment coverage.
Never remove PHI warnings.
Never remove partial-credit disclaimers.

You may add or extend content only when:

1. The source material is too thin to satisfy the V2 lesson structure or target time.
2. The addition is consistent with CNA scope and reviewed source content.
3. The addition is marked as:
   Draft enrichment — SME review required.
4. The addition does not claim CDPH approval.
5. The addition does not create clinical-credit, simulation-credit, or competency-validation claims.
6. The addition does not introduce PHI.

If source is missing, incomplete, contradictory, or weak:

* do not fabricate clinical instructions
* create a safe placeholder only
* label it:
  Draft / Source Repair Required
* list exactly what source content is missing
* flag for SME/compliance review

Content required for every lesson card/subcard:

* module_id
* module_title
* lesson_id
* lesson_title
* card_id
* card_type
* app.location
* display title
* learner-facing content
* learning goal or key concept
* CNA practice example
* why it matters
* key terms
* completion condition
* narration script
* transcript text
* estimated narration seconds
* estimated word count
* media prompt placeholder
* source reference
* status
* SME review flag
* compliance review flag

Card 1 — Overview must include:

* lesson title
* estimated time
* learning goal
* why this lesson matters
* what learner will be able to do
* required completion condition
* narration
* transcript

Card 2 — Delivery must include:

* one practical idea per subcard
* plain-language teaching
* CNA practice example
* common mistake or risk
* key takeaway
* narration
* transcript
* media prompt placeholder

Card 3 — Challenge must include:

* realistic CNA scenario
* one decision point
* one question
* four answer choices where possible
* correct answer for internal data only
* no answer reveal until submission
* narration
* transcript
* rationale source mapping

Card 4 — Debrief / Remediation must include:

* why correct answer is correct
* why each distractor is wrong
* non-punitive remediation
* what the CNA should remember
* resident safety implication
* CNA scope implication
* narration
* transcript

Lesson practice challenge rule:
It is acceptable for lesson practice debriefs to explain correct and incorrect options.

Final assessment rule:
Do not reveal final assessment answer keys in learner-facing results.
Final assessment results may show:

* score
* pass/fail
* topic-level remediation
* suggested modules to review

Do not show exact correct answers after the final exam.

Narration requirements:
The entire module set must be narrated from overview through final assessment.

Narrate:

* dashboard/course welcome if used in app data
* Module 0 orientation
* each module overview
* every lesson card/subcard
* every module assessment splash
* module assessment instructions
* module assessment remediation messages
* final assessment splash
* final assessment instructions
* final result pass/fail messages
* certificate gate explanation
* clinical support disclaimers if presented as narrated content

Do not generate actual audio files.
Create scripts only.

Narration style:

* clear
* warm
* professional
* direct
* respectful of experienced working CNAs
* not childish
* not dramatic
* not legalistic
* not academic
* TTS-ready
* short sentences
* no stage directions inside the Narration field
* spell out abbreviations on first use where needed
* avoid awkward symbols
* avoid slash-heavy phrasing that TTS may read poorly
* use “CNA” naturally

Every narration must have a matching transcript.

Consistent naming convention:
Use this exact naming convention everywhere.

Module ID:
M00, M01, M02, M03, M04, M05, M06, M07, M08

Suggested module mapping:
M00 — Orientation and Compliance Boundaries
M01 — Infection Control and PPE
M02 — Resident Rights, Abuse Prevention, and Boundaries
M03 — Dementia, Communication, and Respectful Care
M04 — Mobility, Falls, and Workplace Safety
M05 — Nutrition, Skin Integrity, Vital Signs, and Observation
M06 — Documentation, Reporting, PHI Avoidance, and Scope
M07 — Final Review, Exam/Test, Affidavit, and Certificate Status
M08 — Optional Clinical Support Hub

Lesson ID:
L00 for module-level overview/orientation
L01, L02, L03, etc. for lessons

Card ID:
C01_OVERVIEW
C02A_DELIVERY
C02B_DELIVERY
C02C_DELIVERY
C02D_DELIVERY
C03_CHALLENGE
C04A_DEBRIEF
C04B_DEBRIEF
C04C_DEBRIEF
C04D_DEBRIEF

Assessment IDs:
A00_SPLASH
A01_Q01
A02_Q02
A03_Q03
A99_RESULT

Final assessment IDs:
FINAL_SPLASH
FINAL_Q01
FINAL_Q02
FINAL_Q03
FINAL_RESULT_PASS
FINAL_RESULT_FAIL

App location format:
module.m00.lesson.l00.card.c01_overview
module.m01.lesson.l01.card.c02a_delivery
module.m01.assessment.a00_splash
module.m01.assessment.q01
course.final.splash
course.final.q01
course.final.result.pass
certificate.gate.status
certificate.preview.mock
clinical.hub.overview

Use this exact app.location pattern in:

* JSON
* TypeScript data
* narration CSV
* narration master CSV
* XLSX workbook
* media prompt placeholders
* app adapter
* review reports

Required CSV:
Create:

CNA-Recert-Course\ContentV2\narration\tts_narration_import.csv

Use exactly these columns:
Project,Title,app.location,Narration

No extra columns.

Project value:
CNA Recertification Theory + Clinical Support

Title format:
M00 L00 C01 Overview
M01 L01 C01 Overview
M01 L01 C02A Delivery
M01 L01 C03 Challenge
M01 L01 C04A Debrief
M01 Assessment Splash
Course Final Assessment Splash
Certificate Gate Status
Clinical Hub Overview

Narration master CSV:
Create:

CNA-Recert-Course\ContentV2\narration\narration_master.csv

Columns:
Project
Module ID
Module Title
Lesson ID
Lesson Title
Card ID
Card Type
Title
app.location
Narration
Transcript
Estimated Seconds
Estimated Word Count
Target Duration Status
Voice Notes
Source Reference
SME Review Flag
Compliance Review Flag
Status

Narration metadata:
Create:

CNA-Recert-Course\ContentV2\narration\narration_metadata.json

Include:

* generated_at
* source_folder
* total_clips
* total_estimated_seconds
* total_estimated_minutes
* clips_over_target
* unique_app_locations
* modules_covered
* validation_status

XLSX workbook:
Create:

CNA-Recert-Course\ContentV2\xlsx\CNA_RECERT_CONTENTV2_MASTER.xlsx

Use existing workbook style/schema as reference if available.

Required sheets:

1. README
2. ContentV2 Master
3. Narration Only
4. TTS Import Preview
5. Image + Video Prompt Placeholders
6. Assessment Map
7. Final Assessment Map
8. App Location Map
9. Source Coverage Map
10. Runtime Summary
11. SME Review Flags
12. Compliance Review Flags
13. Deferred Items
14. Agent Contribution Map

XLSX must include all information needed for:

* module/lesson/card content
* narration
* transcripts
* media placeholders/prompts
* assessment mapping
* final assessment mapping
* app.location mapping
* source traceability
* duration tracking
* content readiness status
* SME/compliance flags

Runtime Summary must include:

* total modules
* total lessons
* total cards/subcards
* total narration clips
* total estimated narration seconds
* total estimated narration minutes
* estimated active learning time
* estimated assessment time
* source content coverage percentage
* number of SME flags
* number of compliance flags
* number of draft enrichment items
* number of source repair required items
* number of worker agents used
* batch size used

Media prompt placeholder requirements:
Do not generate images.
Do not generate video files.
Create prompts/placeholders only.

For each card/subcard, include:

* module_id
* lesson_id
* card_id
* app.location
* scene title
* 16:9 image prompt
* optional video prompt
* negative prompt
* PHI safety note
* whether media is required for MVP or future enhancement
* status

Media prompts must be:

* realistic healthcare education style
* no PHI
* no real patient records
* no readable charts
* no facility names
* no logos unless CI-approved branding asset is explicitly intended
* no sensationalism
* no gore
* no unsafe clinical actions
* no artificial plastic-looking people

Assessment requirements:
Create module assessment content for each module only where source supports it.

For each module assessment include:

* splash page copy
* coverage topics
* estimated completion time
* question format
* completion evidence created
* remediation rule
* question bank draft if source supports it
* answer key for internal data only
* learner-facing feedback for module assessments only
* source mapping
* SME/compliance flags

Final assessment requirements:
Create:

* final assessment splash
* course-wide coverage map
* final assessment instructions
* question bank draft if source supports it
* final result pass copy
* final result fail copy
* topic-level remediation map
* certificate gate next-step copy

Do not expose final assessment answer key in learner-facing result.

If source is insufficient for final assessment:

* create a draft blueprint only
* mark:
  Question bank requires SME review
* do not pretend it is final approved exam content

Required compliance guardrails:
Every worker and coordinator output must preserve these rules:

* This is partial online CE only unless provider/course approval exists.
* This does not complete full California CNA renewal by itself.
* Learners remain responsible for total renewal hours, annual minimums, online-hour limits, and work/practice documentation.
* Optional Clinical Support is separate, optional, non-credit, and non-gating unless written CDPH approval says otherwise.
* Clinical support, confidence checks, simulation, virtual simulation, LTI simulation, uploads, scheduling, and RN/preceptor support must not count as clinical hours or certificate gates unless written approval exists.
* No PHI may be requested, typed, uploaded, shown, or implied.
* Active-time remains demo/MVP unless the real active-time engine is implemented and validated.
* Final exam/test does not reveal the full answer key.
* Certificate production issuance remains disabled until approval metadata, NAC#, approved certificate wording, affidavit method, active-time validation, and all gates are complete.
* TTS/audio generation requires authorized voice approval and transcript pairing.
* Do not generate actual audio or media files.

Content-package hard stops:

* Do not mark the course production-ready.
* Do not remove the Module 1 infection-control SME/source-review flag.
* Do not remove the Module 5 skin integrity / pressure injury SME/source-review flag.
* Do not remove flagged status from Module 1 exam questions or skin integrity exam questions unless a newer controlling source explicitly approves it.
* Do not convert optional clinical support, simulations, confidence checks, documentation practice, uploaded notes, or RN/preceptor support into certificate gates.
* Do not count optional clinical support toward active CE time, clinical hours, certificate hours, or renewal completion.
* Do not add clinical hours to certificate copy.
* Do not enable production certificate print/download/export in the standalone preview app.
* Do not fabricate provider NAC#, CE provider number, CDPH phone/address/web contact, approval metadata, issuance rules, or legal attestation wording.
* Do not collect or request SSN, DOB, patient identifiers, resident identifiers, facility identifiers, medical record numbers, or real PHI.
* Do not describe simulated or virtual activities as competency validation, clinical practicum, skills checkoff, or clinical credit.
* Do not generate audio, images, video, PDFs, or final certificate files unless explicitly authorized outside this prompt.

Use safe learner copy from project docs where available:

* Orientation Page
* Partial Credit Disclaimer
* 24-Hour Online Cap Acknowledgement
* Course Completion Disclaimer
* Certificate Release Reminder
* Clinical Support Disclaimer
* Simulation Disclaimer
* PHI / No-Upload Warning
* Active-Time Explanation
* Failed Exam Remediation Message
* Missing Certificate Field Message
* Support Request Message
* Optional Confidence Check Label

Worker assignment plan:
Use Codex GPT-5.5 worker agents in parallel across non-overlapping packages.

If using 32 workers, split as follows:

Worker 01 — Preflight support and source tree inventory
Worker 02 — Source coverage map, source file listing, duplication scan
Worker 03 — Module 0 Orientation and Compliance Boundaries
Worker 04 — Module 1 Infection Control source audit
Worker 05 — Module 1 4-card lesson conversion
Worker 06 — Module 1 assessment and narration
Worker 07 — Module 2 Resident Rights source audit
Worker 08 — Module 2 4-card lesson conversion
Worker 09 — Module 2 assessment and narration
Worker 10 — Module 3 Dementia/Communication source audit
Worker 11 — Module 3 4-card lesson conversion
Worker 12 — Module 3 assessment and narration
Worker 13 — Module 4 Mobility/Falls source audit
Worker 14 — Module 4 4-card lesson conversion
Worker 15 — Module 4 assessment and narration
Worker 16 — Module 5 Nutrition/Skin/Vitals source audit
Worker 17 — Module 5 4-card lesson conversion
Worker 18 — Module 5 assessment and narration
Worker 19 — Module 6 Documentation/Reporting/Scope source audit
Worker 20 — Module 6 4-card lesson conversion
Worker 21 — Module 6 assessment and narration
Worker 22 — Final Review / Final Assessment / Affidavit / Certificate Gate copy
Worker 23 — Optional Clinical Support Hub content and warnings
Worker 24 — Narration QA for Modules 0–2
Worker 25 — Narration QA for Modules 3–6
Worker 26 — App location uniqueness and naming QA
Worker 27 — Media prompt placeholders
Worker 28 — Schema design and JSON validation
Worker 29 — CSV generation validation
Worker 30 — XLSX workbook generation/validation
Worker 31 — App data adapter review
Worker 32 — Final compliance and SME flag review

If fewer workers are used:
Combine adjacent tasks while preserving separation between content generation, narration QA, schema, app wiring, and compliance review.

Worker prompt template:
Each worker must receive:

1. Exact worker ID
2. Exact assignment
3. Source files/folders it may read
4. Scratch output folder it may write to
5. Naming convention
6. Hard compliance guardrails
7. No original Content modification
8. No canonical output modification
9. No app source modification
10. Required worker report format

Each worker must output:

* AGENT_REPORT.md
* SOURCE_FILES_REVIEWED.md
* assigned content draft
* APP_LOCATION_MAP.md
* SME_FLAGS.md
* COMPLIANCE_FLAGS.md
* SOURCE_COVERAGE.md
* MERGE_NOTES.md

Coordinator merge process:
After worker completion:

1. Read all AGENT_REPORT.md files.
2. Read all MERGE_NOTES.md files.
3. Check source coverage.
4. Check duplicate modules/lessons/cards.
5. Check app.location uniqueness.
6. Check narration duration.
7. Check final exam answer key exposure.
8. Check optional clinical support is non-gating.
9. Check no PHI introduced.
10. Check all draft enrichment is flagged.
11. Check source repair required items are listed.
12. Deduplicate overlapping outputs.
13. Merge into canonical ContentV2 markdown.
14. Generate canonical JSON/schema/TypeScript data.
15. Generate narration CSV files.
16. Generate XLSX workbook.
17. Generate media prompt placeholder file.
18. Generate final integration notes.
19. Wire app data if safe.
20. Run validation/build.

App data wiring:
HARD APP WIRING REQUIREMENT:

The updated ContentV2 must be loaded into the standalone app, not only generated as external files.

After creating ContentV2, inspect the app's current data/content source and update the actual consumed app data layer so the V2 UI displays the new ContentV2 content.

Required:
1. The app must import or consume ContentV2 data from generated ContentV2 data files or a generated adapter.
2. Dashboard, Modules, Module 0, Module 1, lesson cards, assessments, final assessment, certificate gate copy, and clinical hub copy must display ContentV2 data where those screens use learner-facing content.
3. Do not leave old hardcoded placeholder lesson content as the primary displayed content.
4. If old hardcoded fallback content remains, label it clearly as fallback only and ensure ContentV2 is primary.
5. Add a clear app data adapter if needed, such as:
   standalone-course-mvp\src\data\courseContentV2.ts
   or
   standalone-course-mvp\src\data\contentV2Adapter.ts
6. Update imports/components to use the adapter.
7. Run the app build after wiring.
8. Preserve visual parity with standalone-course-mvp\screenshots\v2-design and do not redesign the approved V2 screens while wiring data.
9. Preserve production-disabled certificate behavior, reviewer prototype label, optional/non-gating clinical support, and PHI/no-upload warnings.

If ContentV2 cannot be safely wired without breaking the app, stop and output:
STOPPED: ContentV2 generated, but app wiring is unsafe. No partial app wiring performed.

Do not merely write a wiring plan unless wiring is truly unsafe.

Inspect:

C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\standalone-course-mvp

Identify its current data/content source.

If safe:

* create or update a ContentV2 data adapter
* wire modules, lessons, cards, narration/transcripts, assessment splash, quiz content, final assessment, certificate gate copy, and clinical hub copy into the existing V2 UI
* do not redesign UI
* do not change login
* do not change certificate production-disabled behavior
* do not change required/optional separation
* do not make clinical support a gate

If full app wiring is risky:

* create the data files
* create adapter file if safe
* document exact wiring steps
* do not break the app

Protected app areas:
Do not modify:

* sign-in/login page
* approved V2 visual design
* certificate production-disabled logic
* reviewer tools prototype-only label
* routing unless required for data loading
* package.json unless absolutely necessary and explained

Dependency safety:
Do not modify package.json, lockfiles, or install new app dependencies unless absolutely required and explicitly reported.

For XLSX generation:
- Prefer an external script or existing local Python/openpyxl capability.
- Do not add spreadsheet libraries to the React app package just to generate the workbook.
- If XLSX generation is blocked by missing local tooling, generate all CSV/JSON outputs, document the blocker, and stop before app package changes.

Validation requirements:
After generating ContentV2:

1. Validate JSON schema.
2. Validate CSV files can be read.
3. Validate XLSX opens and all sheets exist.
4. Validate every narration row has non-empty app.location.
5. Validate every app.location is unique.
6. Validate every narration clip target duration is <=75 seconds unless flagged.
7. Validate no final assessment learner-facing content reveals full answer key.
8. Validate no optional clinical support appears as certificate gate.
9. Validate no PHI examples exist.
10. Validate no source content was reduced or omitted without flagging.
11. Validate original Content folder is untouched.
12. Validate all source files are copied or represented in ContentV2.
13. Validate all added content is flagged as draft enrichment.
14. Validate all missing content is flagged Source Repair Required.

App verification:
If app data wiring is completed, run:

cd C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\standalone-course-mvp
npm run typecheck
npm run build

Run if available:
npm run lint
npm test

Manual app verification:

1. app loads
2. login unchanged
3. dashboard still V2 visual design
4. modules load ContentV2 data
5. Module 0 loads updated orientation content
6. Module 1 lesson player loads ContentV2 cards/subcards
7. narration/transcript controls have content
8. assessment splash pages load ContentV2 copy
9. final assessment splash/result content loads
10. certificate gate copy remains mock/production-disabled
11. clinical hub remains optional/non-gating
12. no console errors

V2 design parity verification:
After app wiring, compare the running app against the screenshots in:

C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\standalone-course-mvp\screenshots\v2-design

Verify these surfaces still match the approved V2 design intent:

1. sign-in card
2. dashboard default
3. reviewer tools panel
4. certificate gate locked
5. modules default
6. Module 0 orientation
7. modules unlocked/final-ready
8. Module 1 overview
9. lesson card 1 overview
10. lesson card 2 delivery
11. lesson card 3 challenge
12. lesson card 4 debrief
13. module assessment splash
14. module assessment quiz
15. final assessment splash
16. final assessment quiz
17. final result passed
18. certificate gate ready
19. mock certificate preview
20. clinical hub

If screenshot tooling is available, capture updated screenshots and list their paths in the final report. If screenshot tooling is not available, perform manual browser inspection and document the limitation.

Flag as a blocker before completion:

* old hardcoded placeholder content is still primary
* approved V2 visual design is replaced or degraded
* sign-in card changes unexpectedly
* reviewer tools lose prototype-only labeling
* certificate print/download/export becomes enabled in preview
* mock certificate loses watermark or production-disabled messaging
* clinical support appears required, certificate-gated, or credit-bearing
* PHI/no-upload warning disappears from clinical/documentation support
* final assessment exposes the full answer key
* Module 7 timing reverts to 90 minutes or total theory time no longer equals 720 minutes

Memory/output/concurrency limit rule:
If context, memory, output, or process limits are reached, stop cleanly and output:

MEMORY/OUTPUT/CONCURRENCY LIMIT REACHED.
Recommended split:

1. Preflight + Codex help + orchestration plan
2. Source audit worker batch
3. Module 0–1 worker batch
4. Module 2–3 worker batch
5. Module 4–5 worker batch
6. Module 6–Final worker batch
7. Narration CSV/XLSX worker batch
8. App data wiring
9. QA/build verification

Do not produce partial broken output.
Do not silently omit modules.
Do not claim completion if only some modules are processed.

Final report required:
At the end, provide:

1. Preflight results
2. Codex CLI help findings
3. Codex model availability
4. Number of GPT-5.5 workers launched
5. Maximum concurrent batch size used
6. Why that batch size was selected
7. Worker assignment table
8. Worker completion summary
9. Branch used
10. Files created
11. Files changed
12. Original Content untouched confirmation
13. ContentV2 folder summary
14. Source files reviewed
15. Source files copied unchanged
16. Source files revised for V2
17. Modules processed
18. Lessons/cards/subcards created
19. Narration clip count
20. Narration duration summary
21. CSV output paths
22. XLSX output path and sheet list
23. Source coverage summary
24. Draft enrichment count
25. Source repair required items
26. SME review flags
27. Compliance review flags
28. App wiring completed/deferred
29. Build/typecheck/lint/test results
30. Manual verification checklist
31. V2 design reference files reviewed
32. V2 design parity verification result
33. Known issues
34. Whether memory/output/concurrency limits were reached
35. Exact recommended next QA prompt

Acceptance criteria:

* Codex CLI is used, not Cursor Agent.
* GPT-5.5 is used where supported.
* Up to 32 GPT-5.5 workers are used if safe/supported.
* Workers write only to scratch folders.
* Coordinator performs final merge.
* Original Content folder is untouched.
* ContentV2 folder is complete.
* All original source content is copied or represented in ContentV2.
* No source content is reduced.
* Narration CSV is generated.
* Narration master CSV is generated.
* XLSX master workbook is generated.
* Consistent app.location naming is used everywhere.
* Each narration clip targets roughly 1 minute or less.
* Longer content is split into cards/subcards/sublessons.
* Optional Clinical Support remains non-gating.
* Production certificate remains disabled.
* No PHI is introduced.
* Final assessment does not reveal answer key.
* App loads ContentV2 data or provides a safe adapter/wiring plan.
* Build passes if app wiring is completed.
* V2 design reference folder was reviewed and app wiring preserves the approved V2 screen structure.
* 720-minute / 12-hour theory total is preserved.
* Module 1 infection-control and Module 5 skin integrity flags remain visible where applicable.
* Optional Clinical Support remains non-gating and non-credit.
* Production certificate output remains disabled in the preview app.
