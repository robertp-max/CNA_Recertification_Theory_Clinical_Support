You are one of 10 independent Grok Build reviewers for Module 11.

Review lens ID: 09_data_schema_json
Review lens: Data/schema/JSON audit: schema shape, generated content package, narration batch package, consistency across module.content, activities, source map, and app data.

Task:
- Audit the supplied dry-run evidence bundle against the checkpoint/rubric.
- Be read-only. Do not propose running commands or modifying files as if you are executing; only analyze evidence.
- Separate hard failures from residual risks and from module-specific non-applicable checks.
- For Module 10, apply Module 10-specific checkpoint values literally: 16 objectives, exactly 180 weighted theory minutes, original packet path `Module10_Dry_Run`.
- For Modules 11/13, apply checkpoint principles but use the module's own declared values from the bundle: objectives=10, weighted minutes=120.
- Treat self-reported PASS as lower-strength evidence than actual deterministic metrics/path checks.
- If the evidence contradicts itself, call that out.
- Include file/path evidence where possible.

Output format (Markdown):
1. `# Review 09_data_schema_json — Module 11`
2. `Verdict:` PASS / PASS WITH RISKS / CONDITIONAL PASS / FAIL / INSUFFICIENT EVIDENCE.
3. `Top findings:` 5-10 bullets, each with severity `[Critical|High|Medium|Low]`, evidence, and recommended action.
4. `Checkpoint table:` concise table with Check, Status, Evidence.
5. `Open questions / residual risks:` bullets.
6. `One-sentence go/no-go recommendation.`

EVIDENCE BUNDLE START
# Grok Build Review Input Bundle — Module 11
Generated: 2026-06-04T10:06:52
Module title: NATP Module 11: Nutrition
Declared objective count for this module: 10
Declared weighted theory minutes for this module: 120
Declared source PDF: `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf`
Apply Module 10 checkpoint principles, but use Module 11's own official objective count and weighted minutes for module-specific checks.

# Checkpoint / Rubric Used for All Grok Build Reviews

Primary packet: NATP Module 10 Vital Signs — Source-First Dry Run.
Use it as the strict Module 10 checkpoint and as the cross-module dry-run quality rubric for Modules 11 and 13.

Hard checkpoint principles:
- Source-first only: official NATP source PDF for the active module is the instructional authority.
- Active scope is one module only; avoid stale ContentV2, backups, prior module outputs, deployment, commits, pushes, PRs, or broad cleanup.
- Module 10 literal requirements: 16 official objectives; weighted theory minutes must total exactly 180; active output/app scope was specified as `Module10_Dry_Run` in the packet.
- For Module 11/13, adapt the objective/time checks to the module's own declared source requirements while still applying Module 10 checkpoint principles.
- No CDPH/TPRU approval claim, no certificate-production readiness claim, no online clinical-hour credit claim, no online hands-on competency validation claim, no PHI.
- Clinical/manual skills must be treated as theory preparation and deferred to in-person/evaluator-supported validation.
- Qwen TTS is required/gated, using model `C:/AI/Qwen3-TTS-12Hz-1.7B-Base`, Python env `C:/AI/qwen3-tts-env`, and CI-ION voice reference `C:/AI/Git/training/CI-ION/CI-ION_OASIS-E2_SOC/src/content/narration/Additional Narrations OASIS-E2/FINAL_REVIEW_EXPORT_GUIDANCE_001.wav`.
- Image prompts require alt text and must avoid PHI/facility logos; final image generation is separate unless authorized.
- SFX must remain queued/license-gated unless licensed assets are selected.
- Narration package preference after orchestration patch: JSON narration batch package, no CSV, where feasible. Note that Module 10 may predate that patch and uses CSV; evaluate as a gap/risk if relevant.
- Validate actual files/metrics over self-reported PASS text. Explicitly call out contradictions between report claims and observed file state.

## Actual Path / File-State Facts
- `Module10_Dry_Run`: exists=False, kind=missing, size=
- `Module10_Dry_Run_module10_dryrun_outputs`: exists=False, kind=missing, size=
- `Module_Dry_Run`: exists=True, kind=dir, size=
- `Module_Dry_Run/_module11_dryrun_outputs`: exists=True, kind=dir, size=
- `Module_Dry_Run/standalone-course-mvp`: exists=True, kind=dir, size=
- `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts`: exists=True, kind=file, size=129
- `Module_Dry_Run/standalone-course-mvp/src/data/module11.generated.ts`: exists=True, kind=file, size=129
- `Module_Dry_Run/standalone-course-mvp/src/data/module11.content.generated.json`: exists=True, kind=file, size=165179
- `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf`: exists=True, kind=file, size=400160

### Current active app content pointer (`contentV2.generated.ts`)
```ts
import module13CourseContent from './module13.content.generated.json';

export const courseContentV2 = module13CourseContent;

```

## Output File Inventory
- `audio/audio_manifest.json` size=33915
- `audio/narration_batch_import_package.json` size=33691
- `audio/sfx_manifest.json` size=3586
- `data/content.generated.json` size=165179
- `data/module11.activities.json` size=36584
- `data/module11.content.json` size=44540
- `data/module11.schema.json` size=558
- `media/image_manifest.json` size=9385
- `media/image_prompt_queue.json` size=9072
- `reports/app_integration_notes.md` size=212
- `reports/final_handoff.md` size=5466
- `reports/lessonplayer_review.md` size=345
- `reports/preflight_report.md` size=222
- `reports/time_allotment_report.md` size=995
- `reports/validation_report.md` size=1472
- `reports/watchdog_report.md` size=291
- `source_map/generate_module11_run.py` size=35240
- `source_map/module11_source_layout.txt` size=54942
- `source_map/source_objective_map.json` size=49584
- `source_map/source_objective_map.md` size=11369

## Deterministic JSON/CSV Metrics
- source_map/source_objective_map.json: JSON type=dict, size=49584
  - top-level keys: ['run_name', 'source_authority', 'source_title', 'learner_facing_title', 'theory_minutes_total', 'source_recommended_clinical_hours', 'online_clinical_credit_claimed', 'online_hands_on_competency_validated', 'purpose', 'terminology', 'objectives', 'source_assets', 'validation']
  - objectives: count=10, minute_sum=120, min_activities=0, max_activities=0
  - objective titles: 1. Define key terminology; 2. Discuss the body's need for food and fluids; 3. List common nutrients and their food sources; 4. Describe the My Plate food guidance system; 5. Describe the vegan basic four food groups; 6. Discuss nutritional and fluid needs of the elderly; 7. Describe therapeutic diets commonly ordered for patients/residents and the responsibilities of the Nurse Assistant; 8. Describe proper techniques for feeding patients/residents; 9. Discuss cultural and religious influences on dietary practices; 10. Identify alternative ways to administer nutrition
  - sample source refs: CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-4 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-4-5 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-5-6 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-6-7 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-7 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-7-8
  - source_authority: 'CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf'
  - source_title: 'Module 11: Nutrition'
  - learner_facing_title: 'NATP Module 11: Nutrition'
  - theory_minutes_total: 120
  - source_recommended_clinical_hours: 6
  - online_clinical_credit_claimed: False
  - online_hands_on_competency_validated: False
  - source_assets: count=11; sample=['terminology_list', 'handout_11_1a', 'handout_11_1b', 'handout_11_3a', 'handout_11_3b', 'handout_11_5']
  - validation: {'objective_count': 10, 'weighted_minutes_total': 120, 'answer_keys_internal_only': True, 'backup_content_used_as_authority': False, 'contentv2_used_as_authority': False, 'module10_outputs_used_as_authority': False}
- source_map/source_objective_map.md: size=11369
- data/module11.content.json: JSON type=dict, size=44540
  - top-level keys: ['module_id', 'title', 'source_authority', 'purpose', 'total_weighted_minutes', 'clinical_boundary', 'objectives']
  - objectives: count=10, minute_sum=120, min_activities=0, max_activities=0
  - objective titles: 1. Define key terminology; 2. Discuss the body's need for food and fluids; 3. List common nutrients and their food sources; 4. Describe the My Plate food guidance system; 5. Describe the vegan basic four food groups; 6. Discuss nutritional and fluid needs of the elderly; 7. Describe therapeutic diets commonly ordered for patients/residents and the responsibilities of the Nurse Assistant; 8. Describe proper techniques for feeding patients/residents; 9. Discuss cultural and religious influences on dietary practices; 10. Identify alternative ways to administer nutrition
  - sample source refs: CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-4 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-4-5 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-5-6 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-6-7 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-7 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf#pages-7-8
  - module_id: 'M11'
  - title: 'NATP Module 11: Nutrition'
  - source_authority: 'CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf'
  - total_weighted_minutes: 120
- data/module11.activities.json: JSON type=dict, size=36584
  - top-level keys: ['module_id', 'source_authority', 'objectives']
  - objectives: count=10, minute_sum=120, min_activities=3, max_activities=3
  - objective titles: 1. ; 2. ; 3. ; 4. ; 5. ; 6. ; 7. ; 8. ; 9. ; 10. 
  - module_id: 'M11'
  - source_authority: 'CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf'
- data/content.generated.json: JSON type=dict, size=165179
  - top-level keys: ['app_copy', 'control_facts', 'clinical_support', 'modules', 'assessments']
  - generated modules: ['M11:NATP Module 11: Nutrition objectives=10']
- audio/audio_manifest.json: JSON type=dict, size=33915
  - top-level keys: ['status', 'clips', 'qwen_model', 'voice_reference', 'compliance']
  - status: 'scripts_only_no_audio_generated'
  - clips: count=40, statuses={'queued_not_generated': 40}, final_path_nonempty=0, voice_reference_nonempty=40
- audio/narration_batch_import_package.json: JSON type=dict, size=33691
  - top-level keys: ['format', 'module', 'csv_used', 'clips']
  - csv_used: False
  - clips: count=40, statuses={'queued_not_generated': 40}, final_path_nonempty=0, voice_reference_nonempty=40
- audio/audio_scripts.csv: MISSING
- audio/sfx_manifest.json: JSON type=dict, size=3586
  - top-level keys: ['status', 'items']
  - status: 'queued_no_sfx_assets_used'
  - items: count=8, alt_text_count=0
- media/image_manifest.json: JSON type=dict, size=9385
  - top-level keys: ['status', 'items']
  - status: 'prompt_queue_only_no_images_generated'
  - items: count=12, alt_text_count=12
- media/image_prompt_queue.json: JSON type=list, size=9072

## Current App Data State Across Reviewed Modules
- `Module_Dry_Run/standalone-course-mvp/src/data/module10.generated.ts` exists=True size=129
- `Module_Dry_Run/standalone-course-mvp/src/data/module10.content.generated.json` exists=True size=233269
- `Module_Dry_Run/standalone-course-mvp/src/data/module10.content.json` exists=True size=69002
- `Module_Dry_Run/standalone-course-mvp/src/data/module10.activities.json` exists=True size=62165
- `Module_Dry_Run/standalone-course-mvp/src/data/module10.schema.json` exists=True size=560
- `Module_Dry_Run/standalone-course-mvp/src/data/module11.generated.ts` exists=True size=129
- `Module_Dry_Run/standalone-course-mvp/src/data/module11.content.generated.json` exists=True size=165179
- `Module_Dry_Run/standalone-course-mvp/src/data/module11.content.json` exists=True size=44540
- `Module_Dry_Run/standalone-course-mvp/src/data/module11.activities.json` exists=True size=36584
- `Module_Dry_Run/standalone-course-mvp/src/data/module11.schema.json` exists=True size=558
- `Module_Dry_Run/standalone-course-mvp/src/data/module13.generated.ts` exists=True size=129
- `Module_Dry_Run/standalone-course-mvp/src/data/module13.content.generated.json` exists=True size=170250
- `Module_Dry_Run/standalone-course-mvp/src/data/module13.content.json` exists=True size=114523
- `Module_Dry_Run/standalone-course-mvp/src/data/module13.activities.json` exists=True size=36045
- `Module_Dry_Run/standalone-course-mvp/src/data/module13.schema.json` exists=True size=693

## Report File Contents

### `reports/preflight_report.md`
```markdown
# Quick Preflight Report — Module 11

PASS: repo/app/source verified. Source PDF text extracted with pdftotext. Orchestrator wrapper failed after partial sanity commands; parent continued manually under wrapper rule.

```

### `reports/final_handoff.md`
```markdown
# Final Handoff — NATP Module 11 Nutrition Source-First Dry Run

Date: 2026-06-04T03:40:24

## Active Requirements Used
Module 11 only; approved source PDF; output under `Module_Dry_Run/_module11_dryrun_outputs`; JSON narration batch package only; no CSV; no media generation; no approval/credit/certificate/competency/PHI claims.

## Repo / Branch / Scope
- Repo path: `C:/AI/Git/CNA_Recertification_Theory_Clinical_Support`
- Branch: `module-10-source-first-dry-run`
- Approved write scope: `Module_Dry_Run`
- App root: `Module_Dry_Run/standalone-course-mvp`
- Output root: `Module_Dry_Run/_module11_dryrun_outputs`

## Files Created / Modified
- `Module_Dry_Run\_module11_dryrun_outputs\audio\audio_manifest.json`
- `Module_Dry_Run\_module11_dryrun_outputs\audio\narration_batch_import_package.json`
- `Module_Dry_Run\_module11_dryrun_outputs\audio\sfx_manifest.json`
- `Module_Dry_Run\_module11_dryrun_outputs\data\content.generated.json`
- `Module_Dry_Run\_module11_dryrun_outputs\data\module11.activities.json`
- `Module_Dry_Run\_module11_dryrun_outputs\data\module11.content.json`
- `Module_Dry_Run\_module11_dryrun_outputs\data\module11.schema.json`
- `Module_Dry_Run\_module11_dryrun_outputs\media\image_manifest.json`
- `Module_Dry_Run\_module11_dryrun_outputs\media\image_prompt_queue.json`
- `Module_Dry_Run\_module11_dryrun_outputs\reports\app_integration_notes.md`
- `Module_Dry_Run\_module11_dryrun_outputs\reports\final_handoff.md`
- `Module_Dry_Run\_module11_dryrun_outputs\reports\lessonplayer_review.md`
- `Module_Dry_Run\_module11_dryrun_outputs\reports\preflight_report.md`
- `Module_Dry_Run\_module11_dryrun_outputs\reports\time_allotment_report.md`
- `Module_Dry_Run\_module11_dryrun_outputs\reports\validation_report.md`
- `Module_Dry_Run\_module11_dryrun_outputs\reports\watchdog_report.md`
- `Module_Dry_Run\_module11_dryrun_outputs\source_map\generate_module11_run.py`
- `Module_Dry_Run\_module11_dryrun_outputs\source_map\module11_source_layout.txt`
- `Module_Dry_Run\_module11_dryrun_outputs\source_map\source_objective_map.json`
- `Module_Dry_Run\_module11_dryrun_outputs\source_map\source_objective_map.md`
- `Module_Dry_Run\standalone-course-mvp\src\data\contentV2.generated.ts`
- `Module_Dry_Run\standalone-course-mvp\src\data\module11.content.generated.json`
- `Module_Dry_Run\standalone-course-mvp\src\data\module11.generated.ts`
- `Module_Dry_Run\standalone-course-mvp\src\data\module11.content.json`
- `Module_Dry_Run\standalone-course-mvp\src\data\module11.activities.json`
- `Module_Dry_Run\standalone-course-mvp\src\data\module11.schema.json`

## Proof Modifications Stayed Inside Module_Dry_Run
All generated paths are prefixed with `Module_Dry_Run/`. Outside dirty state sample is unrelated/pre-existing:
```text
fatal: ':(exclude)Module_Dry_Run': '':(exclude)Module_Dry_Run'' is outside repository at 'C:/AI/Git/CNA_Recertification_Theory_Clinical_Support'
```

## Source Coverage Result
- Objectives covered: 10/10
- Source assets mapped: 11 including internal-only answer keys.

## Weighted Time-Allotment Result
- Weighted theory total: 120 minutes.
- Assessment, clinical, certificate, optional support excluded.

## LessonPlayer Decision
Preserve/reuse existing `LessonPlayerPage.tsx`; feed Module 11 generated data.

## Images / Speech / SFX
- Images: queued prompt-only, no images generated.
- Speech: JSON narration batch import package and audio manifest generated; no CSV and no final audio.
- SFX: manifest generated with queued/license-gated items.

## Build Result
npm install rc=0; npm run build rc=0; nvironment for production...[36m[39m
transforming...
[32mâœ“[39m 1763 modules transformed.
rendering chunks...
computing gzip size...
[2mdist/[22m[32mindex.html                 [39m[1m[2m  0.61 kB[22m[1m[22m[2m â”‚ gzip:   0.37 kB[22m
[2mdist/[22m[35massets/index-CAgn5VpC.css  [39m[1m[2m 51.72 kB[22m[1m[22m[2m â”‚ gzip:  10.42 kB[22m
[2mdist/[22m[36massets/index-D3oNgJVD.js   [39m[1m[33m536.39 kB[39m[22m[2m â”‚ gzip: 129.94 kB[22m
[32mâœ“ built in 1.99s[39m
[33m
(!) Some chunks are larger than 500 kB after minification. Consider:
- Using dynamic import() to code-split the application
- Use build.rollupOptions.output.manualChunks to improve chunking: https://rollupjs.org/configuration-options/#output-manualchunks
- Adjust chunk size limit for this warning via build.chunkSizeWarningLimit.[39m


## Validation Result
Validation report result: **PASS**.

## Compliance Flags
No PHI, approval, certificate-production, online clinical-credit, or online competency claim intentionally present. Manual feeding skills are theory preparation only and deferred to in-person/evaluator-supported work.

## Unresolved Dependencies
- SME/compliance review before production.
- Explicit approval required before TTS generation.
- Licensed SFX selection required.
- Image generation approval/tooling required.
- npm audit vulnerabilities need separate triage.

## Paused / Terminated / Reassigned Workers
- Paused jobs: none.
- Reassigned/handled: `lms-orchestrator` async runner failed/disappeared; parent completed the run manually under wrapper/escalation rule.

## Next Recommended Step
Review source map, generated Module 11 app data, JSON narration package, and validation report. Then authorize SME/compliance review or next module dry run.

```

### `reports/validation_report.md`
```markdown
# Validation Report — Module 11

Date: 2026-06-04T03:40:24
Validation result: **PASS**

| Check | Status | Evidence |
|---|---:|---|
| 10 objectives present | PASS | count=10 |
| weighted minutes exactly 120 | PASS | total=120 |
| >=3 activities per objective | PASS | all objectives |
| JSON narration package/no CSV | PASS | json present, csv absent |
| image alt text | PASS | items=12 |
| sfx license gated | PASS | items=8 |
| source authority only Module 11 PDF | PASS | no backups/ContentV2/Module10 outputs used as authority |
| app build | PASS | npm install rc=0; npm run build rc=0; nvironment for production...[36m[39m transforming... [32mâœ“[39m 1763 modules transformed. rendering chunks... computing gzip size... [2mdist/[22m[32mindex.html                 [39m[1m[2m  0.61 kB[22m[1m[22m[2m â”‚ gzip:   0.37 kB[22m [2mdist/[2 |

## Compliance Flags
- No CDPH/TPRU approval claim.
- No certificate-production readiness claim.
- No clinical-hour credit claim.
- No online hands-on competency validation claim.
- No PHI examples or requests intentionally generated.
- Sample test answer key mapped internal-only.

## Residual Risks
- Generated content is source-map-derived draft and requires SME/compliance review.
- Speech audio not generated; JSON import package/manifests only.
- SFX assets license-gated/queued.
- Images prompt queue only.
- npm audit vulnerabilities remain from app dependencies.

```

### `reports/time_allotment_report.md`
```markdown
# Time Allotment Report — Module 11

Total weighted theory minutes: 120. Assessment, clinical, certificate, and optional support minutes excluded.

- Objective 1: 8 minutes — Define key terminology
- Objective 2: 8 minutes — Discuss the body's need for food and fluids
- Objective 3: 15 minutes — List common nutrients and their food sources
- Objective 4: 14 minutes — Describe the My Plate food guidance system
- Objective 5: 7 minutes — Describe the vegan basic four food groups
- Objective 6: 12 minutes — Discuss nutritional and fluid needs of the elderly
- Objective 7: 15 minutes — Describe therapeutic diets commonly ordered for patients/residents and the responsibilities of the Nurse Assistant
- Objective 8: 18 minutes — Describe proper techniques for feeding patients/residents
- Objective 9: 7 minutes — Discuss cultural and religious influences on dietary practices
- Objective 10: 16 minutes — Identify alternative ways to administer nutrition

```

### `reports/watchdog_report.md`
```markdown
# Watchdog Report — Module 11

Monitored repo/write scope/source authority/time/compliance. Packaged orchestrator async runner failed/disappeared after sanity commands; parent completed work manually inside `Module_Dry_Run`. No paused jobs. No media generation. No CSV narration files.

```

### `reports/lessonplayer_review.md`
```markdown
# LessonPlayer Review — Module 11

Decision: preserve existing `standalone-course-mvp/src/pages/LessonPlayerPage.tsx` MediaLessonPlayer-equivalent. It supports cards, narration controls, transcripts, media placeholders, challenge/debrief, completion, reviewer IDs, and mobile layout. Feed Module 11 source-first data; do not replace shell.

```

### `reports/app_integration_notes.md`
```markdown
# App Integration Notes — Module 11

Integrated Module 11 by writing `module11.content.generated.json` and repointing `contentV2.generated.ts` to Module 11 data. Preserved app shell and deployment settings.

```

### `reports/async_failure_diagnostic.md`
MISSING

## Risk-Term Contexts From Generated Data
Term counts (counts may include allowed negations like 'No PHI' or quiz distractors):
{
  "CDPH": 1,
  "TPRU": 1,
  "approval": 164,
  "approved": 2,
  "certificate": 48,
  "clinical credit": 1,
  "clinical-hour": 31,
  "clinical hour": 22,
  "online hands-on": 21,
  "hands-on competency": 92,
  "PHI": 61,
  "ContentV2": 1,
  "Module 10": 40,
  "Module 11": 202,
  "Module 13": 0,
  "prior Module": 0
}

Selected contexts:
- `Use Module 10 generated content` context 1: ...swallowing, allergy, tube, IV, or aspiration concerns to the licensed nurse."                   },                   {                     "id": "C",                     "label": "Use Module 10 generated content if the nutrition source is incomplete."                   },                   {                     "id": "D",                     "label": "Treat online feeding scenarios as han...
- `Use Module 10 generated content` context 2: ...swallowing, allergy, tube, IV, or aspiration concerns to the licensed nurse."                   },                   {                     "id": "C",                     "label": "Use Module 10 generated content if the nutrition source is incomplete."                   },                   {                     "id": "D",                     "label": "Treat online feeding scenarios as han...
- `Use Module 10 generated content` context 3: ...swallowing, allergy, tube, IV, or aspiration concerns to the licensed nurse."                   },                   {                     "id": "C",                     "label": "Use Module 10 generated content if the nutrition source is incomplete."                   },                   {                     "id": "D",                     "label": "Treat online feeding scenarios as han...
- `Use Module 10 generated content` context 4: ...swallowing, allergy, tube, IV, or aspiration concerns to the licensed nurse."                   },                   {                     "id": "C",                     "label": "Use Module 10 generated content if the nutrition source is incomplete."                   },                   {                     "id": "D",                     "label": "Treat online feeding scenarios as han...
- `clinical-hour credit` context 1: ...",       "locked_body": "Certificate remains locked and non-production.",       "ready_body": "Dry-run complete does not issue a production certificate.",       "restriction": "No clinical-hour credit, CDPH/TPRU approval, or online hands-on competency validation is claimed.",       "affidavit_text": "I confirm this is a non-production Module 11 dry run."     },     "clinicalHub...
- `clinical-hour credit` context 2: ...llow ordered diet/feeding plans, observe, record, and report according to facility policy and licensed-nurse direction. This dry run does not validate hands-on competency or claim clinical-hour credit.",               "learning_goal": "Objective 1: Define key terminology",               "learner_facing_content": "Source-traced teaching outline: review terminology spell/pronounc...
- `clinical-hour credit` context 3: ...llow ordered diet/feeding plans, observe, record, and report according to facility policy and licensed-nurse direction. This dry run does not validate hands-on competency or claim clinical-hour credit.",               "why_it_matters": [                 "This supports source Objective 1 and CNA diet/feeding/reporting responsibilities."               ],               "cna_practi...
- `clinical-hour credit` context 4: ...llow ordered diet/feeding plans, observe, record, and report according to facility policy and licensed-nurse direction. This dry run does not validate hands-on competency or claim clinical-hour credit.",               "sme_review_flag": "Source-traced draft; SME review required before production.",               "internal_challenge": null             },             {           ...
- `online hands-on` context 1: ...an, observes, records intake/output where assigned, documents/reports changes, allergies, dysphagia/choking/aspiration signs, tube/IV alarms or site concerns to licensed nurse; no online hands-on competency validation."       ],       "media_opportunities": [         "source-traced diet/feeding/hydration diagram prompt; no PHI"       ],       "exercise_opportunities": [   ...
- `online hands-on` context 2: ...an, observes, records intake/output where assigned, documents/reports changes, allergies, dysphagia/choking/aspiration signs, tube/IV alarms or site concerns to licensed nurse; no online hands-on competency validation."       ],       "media_opportunities": [         "source-traced diet/feeding/hydration diagram prompt; no PHI"       ],       "exercise_opportunities": [   ...
- `online hands-on` context 3: ...an, observes, records intake/output where assigned, documents/reports changes, allergies, dysphagia/choking/aspiration signs, tube/IV alarms or site concerns to licensed nurse; no online hands-on competency validation."       ],       "media_opportunities": [         "source-traced diet/feeding/hydration diagram prompt; no PHI"       ],       "exercise_opportunities": [   ...
- `online hands-on` context 4: ...an, observes, records intake/output where assigned, documents/reports changes, allergies, dysphagia/choking/aspiration signs, tube/IV alarms or site concerns to licensed nurse; no online hands-on competency validation."       ],       "media_opportunities": [         "source-traced diet/feeding/hydration diagram prompt; no PHI"       ],       "exercise_opportunities": [   ...
- `approval claim` context 1: ...n final exam claim.",       "no_key_notice": "Answer keys are internal-only.",       "pass_title": "Module 11 Review Complete",       "pass_body": "Dry-run only; no certificate or approval claim.",       "fail_title": "Review Module 11 Objectives"     },     "certificate": {       "checklist_title": "Certificate Disabled for Dry Run",       "intro": "Certificate productio...
- `No PHI` context 1: ...r site concerns to licensed nurse; no online hands-on competency validation."       ],       "media_opportunities": [         "source-traced diet/feeding/hydration diagram prompt; no PHI"       ],       "exercise_opportunities": [         "Nutrition Flashcard Deck",         "Crossword Quest",         "Five-Term Diet Report Sentence"       ],       "image_requireme...
- `No PHI` context 2: ...r site concerns to licensed nurse; no online hands-on competency validation."       ],       "media_opportunities": [         "source-traced diet/feeding/hydration diagram prompt; no PHI"       ],       "exercise_opportunities": [         "Food and Fluid Needs Sort",         "Balanced Diet Builder",         "Hydration Minimum Check"       ],       "image_requireme...
- `No PHI` context 3: ...r site concerns to licensed nurse; no online hands-on competency validation."       ],       "media_opportunities": [         "source-traced diet/feeding/hydration diagram prompt; no PHI"       ],       "exercise_opportunities": [         "Nutrient Source Match",         "Food Label Detective",         "Fiber and Fluid Quick Pick"       ],       "image_requirement...
- `No PHI` context 4: ...r site concerns to licensed nurse; no online hands-on competency validation."       ],       "media_opportunities": [         "source-traced diet/feeding/hydration diagram prompt; no PHI"       ],       "exercise_opportunities": [         "My Plate Drag-and-Balance",         "Food Journal Reflection",         "Oil and Solid Fat Sort"       ],       "image_requirem...
- `ContentV2` context 1: ...  }   ],   "validation": {     "objective_count": 10,     "weighted_minutes_total": 120,     "answer_keys_internal_only": true,     "backup_content_used_as_authority": false,     "contentv2_used_as_authority": false,     "module10_outputs_used_as_authority": false   } }  -- audio/audio_manifest.json -- {   "status": "scripts_only_no_audio_generated",   "clips": [    ...

## Qwen / Audio Runtime Observations
- qwen_tts directory: exists=False, wav_count=0

EVIDENCE BUNDLE END