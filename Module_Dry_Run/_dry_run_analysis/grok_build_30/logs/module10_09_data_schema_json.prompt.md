You are one of 10 independent Grok Build reviewers for Module 10.

Review lens ID: 09_data_schema_json
Review lens: Data/schema/JSON audit: schema shape, generated content package, narration batch package, consistency across module.content, activities, source map, and app data.

Task:
- Audit the supplied dry-run evidence bundle against the checkpoint/rubric.
- Be read-only. Do not propose running commands or modifying files as if you are executing; only analyze evidence.
- Separate hard failures from residual risks and from module-specific non-applicable checks.
- For Module 10, apply Module 10-specific checkpoint values literally: 16 objectives, exactly 180 weighted theory minutes, original packet path `Module10_Dry_Run`.
- For Modules 11/13, apply checkpoint principles but use the module's own declared values from the bundle: objectives=16, weighted minutes=180.
- Treat self-reported PASS as lower-strength evidence than actual deterministic metrics/path checks.
- If the evidence contradicts itself, call that out.
- Include file/path evidence where possible.

Output format (Markdown):
1. `# Review 09_data_schema_json — Module 10`
2. `Verdict:` PASS / PASS WITH RISKS / CONDITIONAL PASS / FAIL / INSUFFICIENT EVIDENCE.
3. `Top findings:` 5-10 bullets, each with severity `[Critical|High|Medium|Low]`, evidence, and recommended action.
4. `Checkpoint table:` concise table with Check, Status, Evidence.
5. `Open questions / residual risks:` bullets.
6. `One-sentence go/no-go recommendation.`

EVIDENCE BUNDLE START
# Grok Build Review Input Bundle — Module 10
Generated: 2026-06-04T10:06:52
Module title: NATP Module 10: Vital Signs
Declared objective count for this module: 16
Declared weighted theory minutes for this module: 180
Declared source PDF: `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf`
This is the original checkpoint packet module; all Module 10-specific requirements apply literally.

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
- `Module_Dry_Run/_module10_dryrun_outputs`: exists=True, kind=dir, size=
- `Module_Dry_Run/standalone-course-mvp`: exists=True, kind=dir, size=
- `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts`: exists=True, kind=file, size=129
- `Module_Dry_Run/standalone-course-mvp/src/data/module10.generated.ts`: exists=True, kind=file, size=129
- `Module_Dry_Run/standalone-course-mvp/src/data/module10.content.generated.json`: exists=True, kind=file, size=233269
- `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf`: exists=True, kind=file, size=805210

### Current active app content pointer (`contentV2.generated.ts`)
```ts
import module13CourseContent from './module13.content.generated.json';

export const courseContentV2 = module13CourseContent;

```

## Output File Inventory
- `audio/audio_manifest.json` size=365
- `audio/audio_scripts.csv` size=33991
- `audio/sfx_manifest.json` size=7054
- `data/content.generated.json` size=233269
- `data/generate_module10_artifacts.py` size=16502
- `data/module10.activities.json` size=62165
- `data/module10.content.json` size=69002
- `data/module10.schema.json` size=560
- `media/image_manifest.json` size=12004
- `media/image_prompt_queue.json` size=11631
- `reports/app_integration_notes.md` size=263
- `reports/cleanup_report.md` size=7108
- `reports/final_handoff.md` size=4847
- `reports/generate_final_reports.py` size=10286
- `reports/lessonplayer_review.md` size=432
- `reports/orchestration_control_rule_addendum.md` size=6204
- `reports/preflight_report.md` size=11375
- `reports/stale_content_purge_manifest.md` size=10885
- `reports/time_allotment_report.md` size=1685
- `reports/validation_report.md` size=1935
- `reports/watchdog_report.md` size=1137
- `source_map/generate_source_map.py` size=18559
- `source_map/module10_source_layout.txt` size=81350
- `source_map/source_objective_map.json` size=75657
- `source_map/source_objective_map.md` size=16800

## Deterministic JSON/CSV Metrics
- source_map/source_objective_map.json: JSON type=dict, size=75657
  - top-level keys: ['run_name', 'source_authority', 'source_title', 'learner_facing_title', 'theory_minutes_total', 'source_recommended_clinical_hours', 'online_clinical_credit_claimed', 'online_hands_on_competency_validated', 'purpose', 'terminology', 'objectives', 'source_assets', 'validation']
  - objectives: count=16, minute_sum=180, min_activities=0, max_activities=0
  - objective titles: 1. Define key terminology; 2. Describe what is meant by vital signs, their purpose, and observations made while performing the procedures; 3. Discuss the use of temperature as an indicator of body function; 4. Describe nursing measures to raise and lower the temperature of the body; 5. Describe the circulatory system as it relates to pulse, and identify the pulse sites; 6. Describe factors that increase and decrease pulse, and the qualities to observe in taking a pulse; 7. Define and describe respiration and factors that affect respiratory rate; 8. Describe observations to be made when measuring respirations; 9. Describe abnormal breathing patterns; 10. Describe the process for taking TPR as a combined procedure; 11. Describe what happens in the circulatory system to produce blood pressure; 12. Identify factors that increase or decrease blood pressure; 13. Identify parts of the blood pressure equipment; 14. Discuss the procedure for taking a blood pressure reading; 15. Discuss observation and reporting of patient’s/resident’s pain; 16. Record vital signs on chart, graph, and Nursing Assistant notes
  - sample source refs: CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-4 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-4 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-5-6-7 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-7 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-8 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-8-9
  - source_authority: 'CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf'
  - source_title: 'Module 10: Vital Signs'
  - learner_facing_title: 'NATP Module 10: Vital Signs'
  - theory_minutes_total: 180
  - source_recommended_clinical_hours: 6
  - online_clinical_credit_claimed: False
  - online_hands_on_competency_validated: False
  - source_assets: count=17; sample=['terminology_list', 'handout_10_1a', 'handout_10_1b', 'handout_10_2', 'manual_10_3a', 'manual_10_3b']
  - validation: {'objective_count': 16, 'weighted_minutes_total': 180, 'answer_keys_internal_only': True, 'backup_content_used_as_authority': False, 'contentv2_used_as_authority': False}
- source_map/source_objective_map.md: size=16800
- data/module10.content.json: JSON type=dict, size=69002
  - top-level keys: ['module_id', 'title', 'source_authority', 'purpose', 'total_weighted_minutes', 'clinical_boundary', 'objectives']
  - objectives: count=16, minute_sum=180, min_activities=0, max_activities=0
  - objective titles: 1. Define key terminology; 2. Describe what is meant by vital signs, their purpose, and observations made while performing the procedures; 3. Discuss the use of temperature as an indicator of body function; 4. Describe nursing measures to raise and lower the temperature of the body; 5. Describe the circulatory system as it relates to pulse, and identify the pulse sites; 6. Describe factors that increase and decrease pulse, and the qualities to observe in taking a pulse; 7. Define and describe respiration and factors that affect respiratory rate; 8. Describe observations to be made when measuring respirations; 9. Describe abnormal breathing patterns; 10. Describe the process for taking TPR as a combined procedure; 11. Describe what happens in the circulatory system to produce blood pressure; 12. Identify factors that increase or decrease blood pressure; 13. Identify parts of the blood pressure equipment; 14. Discuss the procedure for taking a blood pressure reading; 15. Discuss observation and reporting of patient’s/resident’s pain; 16. Record vital signs on chart, graph, and Nursing Assistant notes
  - sample source refs: CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-4 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-4 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-5-6-7 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-7 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-8 | CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf#pages-8-9
  - module_id: 'M10'
  - title: 'NATP Module 10: Vital Signs'
  - source_authority: 'CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf'
  - total_weighted_minutes: 180
- data/module10.activities.json: JSON type=dict, size=62165
  - top-level keys: ['module_id', 'source_authority', 'objectives']
  - objectives: count=16, minute_sum=180, min_activities=3, max_activities=3
  - objective titles: 1. ; 2. ; 3. ; 4. ; 5. ; 6. ; 7. ; 8. ; 9. ; 10. ; 11. ; 12. ; 13. ; 14. ; 15. ; 16. 
  - module_id: 'M10'
  - source_authority: 'CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf'
- data/content.generated.json: JSON type=dict, size=233269
  - top-level keys: ['app_copy', 'control_facts', 'clinical_support', 'modules', 'assessments']
  - generated modules: ['M10:NATP Module 10: Vital Signs objectives=16']
- audio/audio_manifest.json: JSON type=dict, size=365
  - top-level keys: ['status', 'qwen_model', 'voice_reference', 'clips', 'compliance']
  - status: 'scripts_only_no_audio_generated'
  - clips: 'See audio_scripts.csv'
- audio/narration_batch_import_package.json: MISSING
- audio/audio_scripts.csv: CSV rows=64, size=33991
- audio/sfx_manifest.json: JSON type=dict, size=7054
  - top-level keys: ['status', 'items']
  - status: 'queued_no_sfx_assets_used'
  - items: count=16, alt_text_count=0
- media/image_manifest.json: JSON type=dict, size=12004
  - top-level keys: ['status', 'items']
  - status: 'prompt_queue_only_no_images_generated'
  - items: count=15, alt_text_count=15
- media/image_prompt_queue.json: JSON type=list, size=11631

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
# Worker 0 Preflight Report — NATP Module 10 Vital Signs Source-First Dry Run

**Date:** 2026-06-04  
**Worker:** Worker 0 — Preflight only  
**Scope:** NATP Module 10: Vital Signs; learner-facing title `NATP Module 10: Vital Signs`; 180 theory minutes. Six (6) clinical hours are source-recommended only and deferred; no online clinical credit, competency validation, CDPH/TPRU approval, or certificate-production claim is made.  
**Output root:** `Module10_Dry_Run/_module10_dryrun_outputs`  
**Report path:** `Module10_Dry_Run/_module10_dryrun_outputs/reports/preflight_report.md`

## Repo hard-stop confirmation

| Check | Status | Evidence |
|---|---:|---|
| Working directory resolves inside approved repo path | PASS | `pwd` returned `/c/AI/Git/CNA_Recertification_Theory_Clinical_Support`; `git rev-parse --show-toplevel` returned `C:/AI/Git/CNA_Recertification_Theory_Clinical_Support`; Python path check returned `inside=True` for approved path `C:\AI\Git\CNA_Recertification_Theory_Clinical_Support`. |
| Approved app/write scope | PASS | Active app/write scope exists at `Module10_Dry_Run`; nested app root exists at `Module10_Dry_Run/standalone-course-mvp`. This report is the only intentionally written/updated artifact. |

## Preflight checks

| Area | Check | Status | Evidence / notes |
|---|---|---:|---|
| Repo | Git branch | PASS | `git branch --show-current` returned `module-10-source-first-dry-run`. |
| Repo | Target branch exists/can be used | PASS | `git show-ref --verify --quiet refs/heads/module-10-source-first-dry-run` exit code `0`; remote branch check exit code `1` (no remote branch observed), but local target branch exists and is active. |
| Repo | Git status / dirty state | PASS with risk | Repo is dirty before/after preflight. `git status --short` summary after build/report: `87 D`, `22 M`, `6 ??`, total `115` entries. Evidence includes unrelated deleted `RCFE CETP Vendor Packet for CDSS/...` files, modified root `standalone-course-mvp/...` files, untracked `CLAUDE_DAY_MODE_FIX_PROMPT.md`, `GLOBAL_MASTER_PROMPT.md`, `CNA-Recert-Course/V3/`, `standalone-course-mvp/src/nia/`, and untracked `Module10_Dry_Run/`. Treat as user/pre-existing work; do not overwrite or clean without explicit authorization. |
| Repo | Risk to unrelated user work | PASS with risk | Unrelated dirty state is extensive and outside `Module10_Dry_Run`. Future workers must avoid broad cleanup, checkout, reset, delete, or overwrite operations. |
| Source | Source PDF exists/readable | PASS | `ls -lh CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf` returned readable file size `787K`. |
| Source | PDF text extraction available | PASS | `command -v pdftotext` returned `/mingw64/bin/pdftotext`; Python library check: `pypdf=True`, `PyPDF2=False`, `pdfplumber=False`, `fitz=False`. |
| Source | PDF text extraction smoke check | PASS | `pdftotext -f 1 -l 2 ... -` extracted text beginning `Module 10: Vital Signs`; evidence included `Minimum Number of Theory Hours: 3 Recommended Clinical Hours: 6`, statement of purpose, terminology, and performance standards. No source map/content generation was performed. |
| Source | Source authority boundary | PASS | Approved source authority observed only as `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf`. Cleanup context confirms backups under `_module10_dryrun_outputs/backups/` must not be source authority. |
| App | App root exists | PASS | `Module10_Dry_Run/standalone-course-mvp` exists and is readable. |
| App | Package/build files exist | PASS | Nested app contains `package.json`, `package-lock.json`, `index.html`, `vite.config.ts`, `tsconfig.json`, `tailwind.config.cjs`, `vitest.config.ts`, `public/`, `src/`, and existing `node_modules/` and `dist/`. |
| App | Build scripts exist | PASS | `package.json` scripts include `build: tsc && vite build`, `typecheck: tsc --noEmit`, `test: vitest run`, `dev`, `preview`, and screenshot scripts. |
| App | Lesson-player / media-player / renderer equivalent | PASS | Found `src/pages/LessonPlayerPage.tsx` and narration/media equivalent `src/components/v2/NarrationPlayer.tsx` in nested app. |
| App data | Clean placeholder state | PASS | `src/data/contentV2.generated.ts` header states `Module10_Dry_Run clean shell data`, stale generated multi-module course content purged, source extraction pending, and not source authority. Placeholder copy includes Module 10 title and compliance boundaries; no production certificate/approval/clinical-credit claim observed in sampled file. |
| Cleanup | Active stale `Content` / `ContentV2` paths absent outside backups | PASS | `find Module10_Dry_Run -path '*/_module10_dryrun_outputs/backups/*' -prune ... '*Content*'` produced no active paths. `find Module10_Dry_Run -maxdepth 4 ... Content/ContentV2` found only backup paths under `_module10_dryrun_outputs/backups/`. |
| Cleanup | Recovery backups present and excluded as source authority | PASS | Existing backup folders: `_module10_dryrun_outputs/backups/stale_content_purge_20260604_004155` and `_module10_dryrun_outputs/backups/stale_content_purge_20260604_014122_app_data`. Future workers must ignore these for source authority. |
| TTS | Qwen TTS model path | PASS | Observed local Qwen TTS assets: `/c/AI/Qwen3-TTS`, `/c/AI/Qwen3-TTS-12Hz-1.7B-Base/model.safetensors` (`3767008 KB`), `/c/AI/Qwen3-TTS-12Hz-1.7B-Base/speech_tokenizer/model.safetensors` (`666304 KB`), `/c/AI/Qwen3-TTS-Tokenizer-12Hz/model.safetensors` (`666304 KB`), and `/c/AI/qwen3-tts-env/Scripts/qwen-tts-demo.exe`. No audio was generated. |
| TTS | CI-ION voice reference file | PASS | Exact run-packet path verified: `/c/AI/Git/training/CI-ION/CI-ION_OASIS-E2_SOC/src/content/narration/Additional Narrations OASIS-E2/FINAL_REVIEW_EXPORT_GUIDANCE_001.wav`; file exists, size `439K`, WAV format `RIFF`, PCM 16-bit mono 24000 Hz. No audio was generated. |
| Image generation | Image generation availability | NA / not runtime-verified | No image generation was run. Local ComfyUI/Qwen image-related folders/blueprints were observed (for example `/c/AI/ComfyUI_windows_portable/ComfyUI/blueprints/Image Edit (Qwen 2511).json` and Qwen image code folders), but runtime/model readiness was not validated. |
| SFX/assets | SFX folders or asset libraries | NA / not verified for SFX | No SFX generation or library validation was run. Repo search found brand/image asset folders, including `Module10_Dry_Run/standalone-course-mvp/public/brand/images` and `dist/assets`, but no dedicated SFX folder was validated. |
| Output folders | Existing output folders | PASS | `_module10_dryrun_outputs`, `_module10_dryrun_outputs/reports`, and `_module10_dryrun_outputs/backups` exist. Reports folder already contained `cleanup_report.md`, previous `preflight_report.md`, and `stale_content_purge_manifest.md`. |
| Output folders | Required future output folders create-list only | PASS | Do not create during preflight. Future workers may need explicitly authorized folders such as `_module10_dryrun_outputs/source_extraction/`, `_module10_dryrun_outputs/source_maps/`, `_module10_dryrun_outputs/media/`, `_module10_dryrun_outputs/validation/`, or similar run-specific folders. |
| Build | `npm install` in nested app | PASS with risk | Ran from `Module10_Dry_Run/standalone-course-mvp`. Output: `up to date, audited 181 packages in 569ms`; `37 packages are looking for funding`; `5 vulnerabilities (4 moderate, 1 critical)`. `package-lock.json` SHA-256 before/after remained `0db68d00d75c388f27c9eb5bb9e4b2e2bd589091698a1e17e8a2b507163d59ef`. |
| Build | `npm run build` in nested app | PASS | Build succeeded: `tsc && vite build`, `vite v7.3.3`, `1762 modules transformed`, output included `dist/index.html 0.61 kB`, `dist/assets/index-CAgn5VpC.css 51.72 kB`, `dist/assets/index-HtD3I53T.js 422.35 kB`, `built in 1.69s`. Dist content hash before/after remained `2fd744f259825608175399f30c27ad24f1292ed1fcb7fa735c99ef718aff0ab0`. |
| Guardrails | No full LMS chain/source extraction/app implementation/media generation | PASS | Only preflight inspection/build validation and this report were performed. No source map, media, audio, app implementation, commit, push, or PR was performed. |

## Commands run

- `pwd && git rev-parse --show-toplevel && git branch --show-current && git status --short --branch`
- `test -d Module10_Dry_Run ...; ls -la Module10_Dry_Run; ls -la Module10_Dry_Run/standalone-course-mvp`
- `ls -lh CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf`
- `find Module10_Dry_Run ... Content/ContentV2 ...`
- `cat Module10_Dry_Run/standalone-course-mvp/package.json`
- `find Module10_Dry_Run/standalone-course-mvp/src ... LessonPlayer/NarrationPlayer/MediaPlayer/CourseRenderer ...`
- `command -v pdftotext`; Python import availability check for `pypdf`, `PyPDF2`, `pdfplumber`, `fitz`
- `pdftotext -f 1 -l 2 CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf -`
- `find /c/AI ... qwen ...` and model file listings under `/c/AI/Qwen3-TTS-12Hz-1.7B-Base` and `/c/AI/Qwen3-TTS-Tokenizer-12Hz`
- `find /c/AI ... CI-ION/reference/voice audio ...`
- `find /c/AI/Git/CNA_Recertification_Theory_Clinical_Support ... sfx/audio/media/image/asset dirs ...`
- `sha256sum package-lock.json`; dist aggregate SHA check before and after build
- `cd Module10_Dry_Run/standalone-course-mvp && npm install && npm run build`
- `git status --short` summaries after build/report preparation

## Readiness statement

**CONDITIONAL GO for source-first next workers only, after explicit user authorization.**

Source PDF existence/readability/text extraction, active branch, app shell, LessonPlayer equivalent, cleanup state, output reports folder, Qwen TTS local paths, CI-ION voice reference path, and nested app install/build checks are ready for the next source-first dry-run step.

**NO-GO for media generation during the next step unless separately authorized.** TTS prerequisites are present, but speech audio must still wait until scripts are source-validated and explicitly approved. Image generation and SFX availability were not runtime-verified and should remain queued/not generated unless explicitly authorized.

## Blocking items and residual risks

1. **Extensive unrelated dirty repo state** — 87 deletions, 22 modifications, and 6 untracked entries observed. Future workers must not run broad reset/clean/checkout operations and must protect user work.
2. **`Module10_Dry_Run/` is untracked at repo level** — future changes inside it are obscured by the top-level untracked directory in `git status`; reviewers should inspect paths directly.
3. **`npm install` reported vulnerabilities** — 5 vulnerabilities (4 moderate, 1 critical). This does not block dry-run preflight/build, but should be triaged separately before production claims.
4. **Image/SFX runtime not validated** — no generation or library smoke test performed under this preflight-only scope.
5. **TTS generation still gated** — Qwen model/env and CI-ION voice reference are present, but no speech audio should be generated until source-validated scripts are produced and explicit media authorization is given.

## Stop point

Preflight is complete. Stop here. User should explicitly authorize continuation before any source extraction, source-map generation, app implementation, media generation, commit, push, or PR.

```

### `reports/final_handoff.md`
```markdown
# Final Handoff — NATP Module 10 Vital Signs Source-First Dry Run

Date: 2026-06-04T02:59:30

## Active Requirements Used

Authorized full orchestration for NATP Module 10: Vital Signs only; 180 weighted theory minutes; source authority is the official Module 10 PDF; no old ContentV2/backups; no deployment/commit/push/PR; no approval, certificate, clinical-hour, or online competency claims.

## Repo / Branch / Scope

- Repo path: `C:/AI/Git/CNA_Recertification_Theory_Clinical_Support`
- Branch: `module-10-source-first-dry-run`
- Approved write scope: `Module10_Dry_Run`
- App root: `Module10_Dry_Run/standalone-course-mvp`
- Output root: `Module10_Dry_Run/_module10_dryrun_outputs`

## Files Created


- `Module10_Dry_Run/_module10_dryrun_outputs/source_map/source_objective_map.json`
- `Module10_Dry_Run/_module10_dryrun_outputs/source_map/source_objective_map.md`
- `Module10_Dry_Run/_module10_dryrun_outputs/data/module10.content.json`
- `Module10_Dry_Run/_module10_dryrun_outputs/data/module10.activities.json`
- `Module10_Dry_Run/_module10_dryrun_outputs/data/module10.schema.json`
- `Module10_Dry_Run/_module10_dryrun_outputs/data/content.generated.json`
- `Module10_Dry_Run/_module10_dryrun_outputs/audio/audio_manifest.json`
- `Module10_Dry_Run/_module10_dryrun_outputs/audio/audio_scripts.csv`
- `Module10_Dry_Run/_module10_dryrun_outputs/audio/sfx_manifest.json`
- `Module10_Dry_Run/_module10_dryrun_outputs/media/image_manifest.json`
- `Module10_Dry_Run/_module10_dryrun_outputs/media/image_prompt_queue.json`
- `Module10_Dry_Run/_module10_dryrun_outputs/reports/time_allotment_report.md`
- `Module10_Dry_Run/_module10_dryrun_outputs/reports/lessonplayer_review.md`
- `Module10_Dry_Run/_module10_dryrun_outputs/reports/app_integration_notes.md`
- `Module10_Dry_Run/standalone-course-mvp/src/data/module10.content.json`
- `Module10_Dry_Run/standalone-course-mvp/src/data/module10.activities.json`
- `Module10_Dry_Run/standalone-course-mvp/src/data/module10.schema.json`
- `Module10_Dry_Run/standalone-course-mvp/src/data/module10.generated.ts`
- `Module10_Dry_Run/standalone-course-mvp/src/data/module10.content.generated.json`

## Files Modified

- `Module10_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts`
- `Module10_Dry_Run/standalone-course-mvp/src/data/remediationOverrides.ts`

## Proof Modifications Stayed Inside Module10_Dry_Run

Generated/written paths are all prefixed with `Module10_Dry_Run/`. Outside dirty state sample remains unrelated/pre-existing:

```text
fatal: ':(exclude)Module10_Dry_Run': '':(exclude)Module10_Dry_Run'' is outside repository at 'C:/AI/Git/CNA_Recertification_Theory_Clinical_Support'
```

## Source Coverage Result

- Objectives covered: 16/16
- Required source assets mapped: 17 including answer key internal-only.
- Source map files written: JSON and Markdown.

## Weighted Time-Allotment Result

- Weighted theory total: 180 minutes.
- Assessment, clinical, certificate, and optional support time excluded.

## LessonPlayer Decision

Preserve/reuse existing `LessonPlayerPage.tsx` MediaLessonPlayer-equivalent and feed Module 10 source-first generated data. No blind replacement.

## Images / Speech / SFX

- Images: queued prompt-only, no image files generated.
- Speech audio: scripts and manifest generated; no final audio generated. Qwen/CI-ION reference recorded and generation remains gated.
- SFX: manifest generated with all required items queued/license-gated; no SFX used.

## Build Result

`npm install` completed with audit warnings; `npm run build` passed.

## Validation Result

Validation report result: **PASS**. See `validation_report.md`.

## Compliance Flags

No PHI, approval, certificate-production, online clinical-credit, or online competency claim is intentionally present. Manual skills are treated as theory preparation and deferred to in-person/evaluator-supported work.

## Unresolved Dependencies

- SME/compliance review needed before production.
- TTS generation needs explicit media approval after script review.
- Licensed SFX sources must be selected before use.
- Image generation/tooling must be approved before generating final images.
- npm audit vulnerabilities should be triaged separately before production.

## Paused / Terminated / Reassigned Workers

- Paused jobs: none.
- Terminated/reassigned: packaged orchestrator failed before work; source-extraction async runner failed/disappeared after partial layout artifact. Parent orchestrator completed/reassigned those tasks manually under the wrapper-timeout/escalation rule.

## Next Recommended Step

Review `source_objective_map.*`, generated data, and validation report. Then run SME/compliance review before authorizing any final media generation or production packaging.

```

### `reports/validation_report.md`
```markdown
# Validation Report — NATP Module 10 Dry Run

Date: 2026-06-04T02:59:30
Validation result: **PASS**

## Checks

| Check | Status | Evidence |
|---|---:|---|
| 16 objectives present | PASS | count=16 |
| weighted minutes total exactly 180 | PASS | total=180 |
| each objective has >=3 activities | PASS | all source map objectives have 3 required activities |
| activities JSON has 16 objectives | PASS | count=16 |
| no clinical/certificate time in theory | PASS | clinical deferred; certificate excluded |
| source assets mapped | PASS | assets=17 |
| answer key internal-only | PASS | sample_test_answer_key internal-only |
| audio scripts/manifest queued no generation | PASS | scripts_only_no_audio_generated |
| SFX manifest license-gated | PASS | items=16 |
| image prompts have alt text | PASS | items=15 |
| backup/ContentV2 not source authority | PASS | false/false |
| app build artifact exists | PASS | dist/index.html present after npm run build |

## Build Result

`npm install` completed with existing audit warnings: 5 vulnerabilities (4 moderate, 1 critical). `npm run build` passed (`tsc && vite build`), producing `dist/index.html` and bundled assets. Large chunk warning noted.

## Compliance Flags

- No CDPH/TPRU approval claim.
- No certificate-production readiness claim.
- No online clinical-hour credit claim.
- No online hands-on competency validation claim.
- No PHI examples or requests intentionally generated.
- Sample test answer key mapped as internal-only.

## Residual Risks

- Generated instructional copy is source-map-derived draft and needs SME/compliance review before production.
- Speech audio was not generated; scripts/manifests only.
- SFX assets are queued/license-gated; no usable SFX selected.
- Images are prompt queue only; no generated images.
- Repo has unrelated dirty state outside Module10_Dry_Run that predates/exists outside this run.

```

### `reports/time_allotment_report.md`
```markdown
# Time Allotment Report

Total weighted theory minutes: 180. Assessment, clinical, certificate, and optional support minutes excluded.

- Objective 1: 12 minutes — Define key terminology
- Objective 2: 8 minutes — Describe what is meant by vital signs, their purpose, and observations made while performing the procedures
- Objective 3: 22 minutes — Discuss the use of temperature as an indicator of body function
- Objective 4: 6 minutes — Describe nursing measures to raise and lower the temperature of the body
- Objective 5: 8 minutes — Describe the circulatory system as it relates to pulse, and identify the pulse sites
- Objective 6: 12 minutes — Describe factors that increase and decrease pulse, and the qualities to observe in taking a pulse
- Objective 7: 7 minutes — Define and describe respiration and factors that affect respiratory rate
- Objective 8: 10 minutes — Describe observations to be made when measuring respirations
- Objective 9: 9 minutes — Describe abnormal breathing patterns
- Objective 10: 7 minutes — Describe the process for taking TPR as a combined procedure
- Objective 11: 12 minutes — Describe what happens in the circulatory system to produce blood pressure
- Objective 12: 6 minutes — Identify factors that increase or decrease blood pressure
- Objective 13: 8 minutes — Identify parts of the blood pressure equipment
- Objective 14: 24 minutes — Discuss the procedure for taking a blood pressure reading
- Objective 15: 15 minutes — Discuss observation and reporting of patient’s/resident’s pain
- Objective 16: 14 minutes — Record vital signs on chart, graph, and Nursing Assistant notes

```

### `reports/watchdog_report.md`
```markdown
# Watchdog Report — Module 10 Dry Run

Status: completed monitoring pass.

## Monitored Rules

- Repo path: approved repo remained `C:/AI/Git/CNA_Recertification_Theory_Clinical_Support`.
- Branch: `module-10-source-first-dry-run`.
- Write scope: generated artifacts are under `Module10_Dry_Run`.
- Active scope: Module 10 only.
- Source authority: approved Module 10 PDF only; backups ignored.
- Time total: 180 theory minutes.
- Prohibited claims: not detected in generated reports/manifests.
- PHI risk: generated examples are generic/de-identified; no PHI requested.
- Answer keys: sample test answer key internal-only; no learner-facing key report generated.

## Worker Failures / Reassignment

- Packaged `lms-orchestrator` failed before work due pi-subagents extension conflict. Parent orchestrator reassigned manually.
- `source-extraction` async runner disappeared after producing only `module10_source_layout.txt`; parent orchestrator completed source extraction in-scope rather than stopping whole run.

## Paused Jobs

None. Media generation was intentionally queued/gated, not paused as a blocker.

```

### `reports/lessonplayer_review.md`
```markdown
# LessonPlayer Review

Decision: preserve and reuse the existing `standalone-course-mvp/src/pages/LessonPlayerPage.tsx` MediaLessonPlayer-equivalent. It already supports chapter/step cards, narration controls, transcript panel, image placeholder renderer, challenge/debrief flow, completion event, reviewer source IDs, and mobile layout. Integration should feed Module 10-only source-traced data rather than replacing the shell.

```

### `reports/app_integration_notes.md`
```markdown
# App Integration Notes

Integrated Module 10 by replacing clean placeholder data with source-first generated `module10.content.generated.json` and `contentV2.generated.ts` adapter export. Preserved existing LessonPlayer shell. No deployment settings changed.

```

### `reports/async_failure_diagnostic.md`
MISSING

## Risk-Term Contexts From Generated Data
Term counts (counts may include allowed negations like 'No PHI' or quiz distractors):
{
  "CDPH": 2,
  "TPRU": 2,
  "approval": 4,
  "approved": 66,
  "certificate": 72,
  "clinical credit": 1,
  "clinical-hour": 49,
  "clinical hour": 34,
  "online hands-on": 49,
  "hands-on competency": 98,
  "PHI": 84,
  "ContentV2": 33,
  "Module 10": 53,
  "Module 11": 0,
  "Module 13": 0,
  "prior Module": 0
}

Selected contexts:
- `clinical-hour credit` context 1: ...",       "locked_body": "Certificate remains locked and non-production.",       "ready_body": "Dry-run complete does not issue a production certificate.",       "restriction": "No clinical-hour credit, CDPH/TPRU approval, or online hands-on competency validation is claimed.",       "affidavit_text": "I confirm this is a non-production Module 10 dry run."     },     "clinicalHub...
- `clinical-hour credit` context 2: ...ontext\n\nCNA boundary: observe, measure, record, and report according to facility policy and licensed-nurse direction. This dry run does not validate hands-on competency or claim clinical-hour credit.",               "learning_goal": "Objective 1: Define key terminology",               "learner_facing_content": "Source-traced teaching outline: review listed terminology spell/p...
- `clinical-hour credit` context 3: ...ontext\n\nCNA boundary: observe, measure, record, and report according to facility policy and licensed-nurse direction. This dry run does not validate hands-on competency or claim clinical-hour credit.",               "why_it_matters": [                 "This supports source Objective 1 and CNA observe-report-record responsibilities."               ],               "cna_practic...
- `clinical-hour credit` context 4: ...ontext\n\nCNA boundary: observe, measure, record, and report according to facility policy and licensed-nurse direction. This dry run does not validate hands-on competency or claim clinical-hour credit.",               "sme_review_flag": "Source-traced draft; SME review required before production.",               "internal_challenge": null             },             {           ...
- `online hands-on` context 1: ..._reporting_charting_scope_boundaries": [         "CNA observes/measures/records/reports within facility policy; abnormal findings and complaints are reported to licensed nurse; no online hands-on competency validation is claimed."       ],       "media_opportunities": [         "mobile diagram/visual placeholder/source-traced prompt only until generated assets approved"   ...
- `online hands-on` context 2: ..._reporting_charting_scope_boundaries": [         "CNA observes/measures/records/reports within facility policy; abnormal findings and complaints are reported to licensed nurse; no online hands-on competency validation is claimed."       ],       "media_opportunities": [         "mobile diagram/visual placeholder/source-traced prompt only until generated assets approved"   ...
- `online hands-on` context 3: ..._reporting_charting_scope_boundaries": [         "CNA observes/measures/records/reports within facility policy; abnormal findings and complaints are reported to licensed nurse; no online hands-on competency validation is claimed."       ],       "media_opportunities": [         "mobile diagram/visual placeholder/source-traced prompt only until generated assets approved"   ...
- `online hands-on` context 4: ..._reporting_charting_scope_boundaries": [         "CNA observes/measures/records/reports within facility policy; abnormal findings and complaints are reported to licensed nurse; no online hands-on competency validation is claimed."       ],       "media_opportunities": [         "mobile diagram/visual placeholder/source-traced prompt only until generated assets approved"   ...
- `approval claim` context 1: ...ey_notice": "Answer keys are internal-only and not shown as learner content.",       "pass_title": "Module 10 Review Complete",       "pass_body": "Dry-run only; no certificate or approval claim.",       "fail_title": "Review Module 10 Objectives"     },     "certificate": {       "checklist_title": "Certificate Disabled for Dry Run",       "intro": "Certificate productio...
- `No PHI` context 1: ...media_prompt_placeholder": {                 "scene_title": "Objective 1 Overview",                 "alt_text": "Training visual: Objective 1 Overview. De-identified illustration; no PHI."               },               "estimated_narration_seconds": 45,               "narration_script": "This lesson covers Objective 1: Define key terminology. Weighted theory time...
- `No PHI` context 2: ...laceholder": {                 "scene_title": "Objective 1 Source Teaching",                 "alt_text": "Training visual: Objective 1 Source Teaching. De-identified illustration; no PHI."               },               "estimated_narration_seconds": 45,               "narration_script": "Source-traced teaching outline: review listed terminology spell/pronounce te...
- `No PHI` context 3: ..._placeholder": {                 "scene_title": "Objective 1 Practice Check",                 "alt_text": "Training visual: Objective 1 Practice Check. De-identified illustration; no PHI."               },               "estimated_narration_seconds": 45,               "narration_script": "Practice applying Objective 1 using the source-traced content.",            ...
- `No PHI` context 4: ... "media_prompt_placeholder": {                 "scene_title": "Objective 1 Debrief",                 "alt_text": "Training visual: Objective 1 Debrief. De-identified illustration; no PHI."               },               "estimated_narration_seconds": 45,               "narration_script": "Review the safest source-traced response for Objective 1.",               "l...
- `ContentV2` context 1: ...ce and report abnormal findings or complaints to the licensed nurse."                   },                   {                     "id": "C",                     "label": "Use old ContentV2 examples if the PDF is hard to read."                   },                   {                     "id": "D",                     "label": "Skip source references once the activit...
- `ContentV2` context 2: ...         "A": "This would falsely claim online hands-on competency validation.",                   "B": "This preserves source meaning and CNA scope.",                   "C": "Old ContentV2 is not source authority.",                   "D": "Every artifact must remain source-traced."                 },                 "source_reference": "CNA-Recert-Course/CNA_Modules...
- `ContentV2` context 3: ...ce and report abnormal findings or complaints to the licensed nurse."                   },                   {                     "id": "C",                     "label": "Use old ContentV2 examples if the PDF is hard to read."                   },                   {                     "id": "D",                     "label": "Skip source references once the activit...
- `ContentV2` context 4: ...         "A": "This would falsely claim online hands-on competency validation.",                   "B": "This preserves source meaning and CNA scope.",                   "C": "Old ContentV2 is not source authority.",                   "D": "Every artifact must remain source-traced."                 },                 "source_reference": "CNA-Recert-Course/CNA_Modules...

## Qwen / Audio Runtime Observations
- qwen_tts directory: exists=False, wav_count=0

EVIDENCE BUNDLE END