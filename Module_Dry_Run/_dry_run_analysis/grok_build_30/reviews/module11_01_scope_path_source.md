**# Review 01_scope_path_source — Module 11**

**Verdict:** FAIL

**Top findings:**
- [Critical] `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts` actively points to Module 13 (`import module13CourseContent from './module13.content.generated.json'; export const courseContentV2 = module13CourseContent;`), not Module 11. Evidence: explicit file content in bundle. Violates single-module active scope.
- [Critical] Direct contradiction between reports and file state: `final_handoff.md` and `reports/app_integration_notes.md` claim "repointing `contentV2.generated.ts` to Module 11 data" and successful Module 11 integration, but the actual `.ts` file content shows Module 13. Evidence: side-by-side comparison of report text vs. provided TS snippet.
- [High] Generated content contains explicit "Use Module 10 generated content if the nutrition source is incomplete" strings (multiple instances) inside what appear to be assessment/quiz structures. Evidence: Risk-Term Contexts section with 4+ repeated contexts. Violates source-first rule and the validation claim `module10_outputs_used_as_authority: false`.
- [High] App data directory contains active Module 10 and Module 13 generated files (`module10.content.generated.json`, `module13.content.generated.json`, etc.) alongside Module 11 files. Evidence: "Current App Data State Across Reviewed Modules" inventory. Creates path mixing and stale cross-module state.
- [High] `data/module11.activities.json` reports 10 objectives and 120 minutes but lists completely empty objective titles ("1. ; 2. ; 3. ; ..."). Evidence: deterministic JSON metrics. Contradicts `module11.content.json` which has proper titles.
- [Medium] Output root and app root use the generic `Module_Dry_Run` (containing multi-module data) rather than the checkpoint-specified `Module10_Dry_Run` pattern (which is missing: `exists=False`). Evidence: Actual Path / File-State Facts.
- [Medium] `audio/audio_scripts.csv` is MISSING while JSON narration package is present. Evidence: Output File Inventory. (JSON is the post-patch preference, but the absence is still a gap vs. full inventory.)
- [Low] Qwen TTS runtime directory does not exist (`qwen_tts: exists=False`, wav_count=0), consistent with "scripts_only_no_audio_generated" status but confirms no actual TTS execution occurred.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| Source PDF exists and is declared authority | PASS | `CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf` (size=400160); `source_authority` fields in `source_objective_map.json`, `module11.content.json`, and `module11.activities.json` all point to it |
| Objectives exactly 10 (Module 11 declared value) | PASS | `source_objective_map.json` and `module11.content.json`: count=10; titles match source PDF refs |
| Weighted theory minutes exactly 120 | PASS | `theory_minutes_total: 120`, `total_weighted_minutes: 120`; `time_allotment_report.md` sums to 120 |
| Active scope limited to one module only | FAIL | contentV2 points to module13; mixed module10/11/13 files in `standalone-course-mvp/src/data`; reports claim single-module but state shows otherwise |
| No stale ContentV2 / prior module outputs used as authority | FAIL | `contentV2.generated.ts` is active and wrong; "Use Module 10 generated content" strings present in generated data despite validation flag claiming false |
| Reports match observed deterministic file state | FAIL | Multiple self-reported PASS claims (repointing, integration, no Module 10 authority) contradicted by actual file contents and inventories |
| App root / output root / write scope correct | CONDITIONAL | Output files under `Module_Dry_Run/_module11_dryrun_outputs`; app root at `standalone-course-mvp`; however scope pollution present |
| No over-claims (approval, clinical credit, etc.) in scope | CONDITIONAL | Compliance language exists in reports, but "Module 10" references and mixed pointers undermine isolation |

**Open questions / residual risks:**
- Why does the actual `contentV2.generated.ts` content contradict the integration claims in `final_handoff.md` and `app_integration_notes.md`?
- Are the "Use Module 10 generated content" strings embedded in learner-facing quiz options or only in internal notes? (Current evidence suggests learner content.)
- The presence of `Module_Dry_Run/standalone-course-mvp/src/data/module11.content.generated.json` (size=165179) alongside the wrong contentV2 pointer means the running app would not load Module 11.
- `Module10_Dry_Run` is missing while `Module_Dry_Run` is used as the container; this deviates from the primary packet checkpoint pattern.
- Self-reported "PASS" in `validation_report.md` and `preflight_report.md` is lower-strength evidence than the path/JSON contradictions shown.

**One-sentence go/no-go recommendation.**  
Fail for scope/path/source-authority: the app is not isolated to Module 11, contentV2 points to the wrong module, reports contradict file state, and Module 10 references appear in generated content; do not accept as clean dry-run output until these are resolved.