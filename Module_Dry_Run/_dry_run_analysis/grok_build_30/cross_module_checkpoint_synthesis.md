# Grok Build 30-Review Cross-Module Checkpoint Synthesis

Date: 2026-06-04
Model used: `grok-build` via authenticated Grok CLI chat proxy
Scope: 10 read-only reviews each for Module 10, Module 11, and Module 13

## Run evidence

- Run manifest: `Module_Dry_Run/_dry_run_analysis/grok_build_30/run_manifest.json`
- Input bundles: `Module_Dry_Run/_dry_run_analysis/grok_build_30/input_bundles/`
- Individual Grok review markdown: `Module_Dry_Run/_dry_run_analysis/grok_build_30/reviews/`
- Raw Grok responses: `Module_Dry_Run/_dry_run_analysis/grok_build_30/raw/`
- Count completed: 30/30
- Failed/empty Grok responses: 0

Headless `grok -p` continued to stall in this pi harness, but the same available Grok Build model responded through the documented CLI chat proxy when `x-grok-client-version: 0.2.22` and `X-XAI-Token-Auth: xai-grok-cli` headers were supplied.

## Verdict matrix

| Module | Fail | Conditional Pass | Pass With Risks | Plain Pass | Overall checkpoint disposition |
|---|---:|---:|---:|---:|---|
| Module 10 | 2 | 4 | 4 | 0 | **FAIL for handoff/app validation** despite good source/time core metrics |
| Module 11 | 4 | 3 | 3 | 0 | **FAIL for active app/data consistency** despite good source/time core metrics |
| Module 13 | 0 | 2 | 8 | 0 | **CONDITIONAL PASS / major risks**; source/time/app pointer mostly OK, Qwen/audio state not OK |

## Cross-cutting high-priority findings

1. **Self-reported PASS reports are contradicted by deterministic file state.** All modules have at least one report saying PASS while raw path/data/app/audio evidence shows unresolved defects.
2. **Active app pointer only serves Module 13 right now.** `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts` imports `module13.content.generated.json`. This invalidates current-tree app validation claims for Module 10 and Module 11.
3. **Module 10 path/scope mismatch is critical.** The Module 10 packet and reports claim `Module10_Dry_Run`, but the actual observed outputs are under `Module_Dry_Run/_module10_dryrun_outputs`; `Module10_Dry_Run` does not exist.
4. **Activities JSON objective titles are blank across all three modules.** Source maps/content JSON have objective titles, but `module10.activities.json`, `module11.activities.json`, and `module13.activities.json` report empty title strings in the deterministic review bundle.
5. **Source-map vs activities activity-count evidence is inconsistent.** Reviews repeatedly observed source maps showing `min_activities=0/max_activities=0` while activities JSON reports 3 activities per objective, yet validation reports claim this as PASS.
6. **Module 13 Qwen TTS state is inconsistent and runner failed.** There are 26 WAV files in `audio/qwen_tts/`, but `audio_manifest.json` still says `scripts_only_no_audio_generated`, `qwen_sent=false`, all clips queued, and the PowerShell background runner log shows parse errors caused by `??` and missing blocks.
7. **Module 11 and Module 13 generated quizzes contain meta/stale distractors.** Examples include “Use Module 10 generated content…” and “Use prior Module 10/11 generated content as the source authority…”. Even as wrong answers, these are learner-facing and undermine source-first discipline.
8. **Module 10 narration package is CSV-only.** `audio_scripts.csv` exists, but `narration_batch_import_package.json` is missing; later orchestration preference is JSON/no CSV.
9. **Dirty/untracked repo state remains a material risk.** Reports mention extensive pre-existing dirty state; no broad cleanup should be performed without explicit approval.
10. **Build success does not prove active-module integration.** Module 10/11 build reports are not sufficient when current `contentV2.generated.ts` points to Module 13.

## Module-specific summary

### Module 10 — NATP Module 10 Vital Signs

Strengths:
- Core source/time metrics are good: 16 objectives and exactly 180 weighted theory minutes are confirmed in source map/content JSON.
- Source PDF authority is correctly referenced in generated artifacts.
- Image/SFX are queued/gated rather than generated.

Blocking issues:
- `Module10_Dry_Run` path required by packet/reports is missing; outputs are under `Module_Dry_Run/_module10_dryrun_outputs`.
- Active app pointer serves Module 13, not Module 10.
- Activities JSON has blank objective titles.
- JSON narration batch package is missing; CSV is used.
- Qwen TTS prerequisites were noted, but no generated audio exists for Module 10.

Disposition: **Do not treat Module 10 as a valid app-integrated handoff until path, app pointer, activities titles, and narration packaging are fixed.**

### Module 11 — NATP Module 11 Nutrition

Strengths:
- Core source/time metrics are good: 10 objectives and exactly 120 weighted theory minutes.
- JSON narration package is present and CSV absent, matching the post-patch preference.
- Image/SFX are queued/gated.

Blocking issues:
- Active app pointer serves Module 13, not Module 11, contradicting handoff/app integration claims.
- Generated content includes Module 10 meta/stale distractors.
- Activities JSON has blank objective titles.
- Schema/data consistency issues between source map, content, activities, and generated package.
- No Qwen audio generated.

Disposition: **Fail current app/data consistency checkpoint.** Source/time work appears salvageable, but app activation and generated content cleanup are required.

### Module 13 — NATP Module 13 Long Term Care Resident

Strengths:
- Core source/time metrics are good: 8 objectives and 780 weighted theory minutes from 13 recommended theory hours.
- Active app pointer correctly points to Module 13.
- Build/typecheck evidence is stronger than Modules 10/11.
- Async failure diagnostic exists and recovery is documented.

Major risks:
- Qwen TTS runner failed with PowerShell parse errors; no process is running.
- Audio manifests are stale/contradictory: 26 WAV files exist, but manifests still say no audio generated and all clips queued.
- Activities JSON has blank objective titles.
- Generated assessment distractors contain prior Module 10/11 source-authority language.
- Dirty repo state remains high risk.

Disposition: **Conditional pass only after Qwen/audio manifest repair, activities-title repair, and assessment distractor cleanup.**

## Recommended repair order

1. **Freeze and clarify path/scope convention** before more dry-run changes. Decide whether Module 10 must literally be under `Module10_Dry_Run` or whether reports must be corrected to `Module_Dry_Run/_module10_dryrun_outputs`.
2. **For each module under review, set `contentV2.generated.ts` to that module and rebuild** before claiming app integration. Alternatively preserve separate app snapshots/worktrees per module.
3. **Regenerate/repair all `module*.activities.json` objective titles** and add validation checks that titles match source map/content JSON.
4. **Remove build-process/stale-module distractors** from Module 11/13 generated assessments.
5. **Fix Module 13 Qwen runner** for Windows PowerShell compatibility, then reconcile `audio_manifest.json` with existing WAVs and finish remaining clips.
6. **Backfill JSON narration package for Module 10** or explicitly document CSV as a legacy pre-patch artifact.
7. **Add deterministic validation gates** for path existence, active app pointer, activities titles, source-map/activity consistency, manifest/WAV consistency, and positive-regulatory-claim scans.
8. **Keep repo-cleanup actions blocked** until the unrelated dirty state is reviewed by the owner.
