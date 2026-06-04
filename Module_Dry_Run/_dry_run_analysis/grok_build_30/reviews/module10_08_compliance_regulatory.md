**# Review 08_compliance_regulatory — Module 10**

**Verdict:** CONDITIONAL PASS

**Top findings:**
- [High] Active output/app scope path mismatch: packet and reports repeatedly specify `Module10_Dry_Run` (and `Module10_Dry_Run/_module10_dryrun_outputs`) as the literal checkpoint scope, but deterministic path facts state `Module10_Dry_Run` exists=False (missing) while artifacts are under `Module_Dry_Run/_module10_dryrun_outputs`. Evidence: "Actual Path / File-State Facts" section and preflight/final_handoff reports. Recommended action: Reconcile directory naming to packet specification before any further use.
- [High] App content pointer failure for Module 10 scope: `Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts` imports `module13.content.generated.json` and exports it as `courseContentV2`. Evidence: explicit code block in bundle. Recommended action: Update pointer to module10 data for this dry-run; current state violates module-specific scope.
- [Medium] Self-reported "PASS" in validation_report.md and final_handoff.md is lower-strength evidence and contradicted by path/pointer facts above. Evidence: validation_report.md table claims "PASS" on scope items while file-state facts and contentV2 block show otherwise. Recommended action: Rely only on deterministic JSON metrics and path checks.
- [Medium] High volume of boundary terms (certificate:72, hands-on competency:98, clinical-hour:49+, PHI:84, approval:4) even in denial contexts. Evidence: "Risk-Term Contexts From Generated Data" section with sampled strings such as "no online hands-on competency validation is claimed" and "Dry-run only; no certificate". Recommended action: Audit full generated content for clarity of negative phrasing before any external review.
- [Low] Missing expected narration package: `audio/narration_batch_import_package.json` is MISSING (CSV used instead). Evidence: "Output File Inventory" and audio_manifest.json. Recommended action: Note as pre-patch gap per rubric; confirm CSV is acceptable for Module 10.
- [Low] Qwen TTS runtime observation contradicts preflight: final bundle states `qwen_tts directory: exists=False, wav_count=0`, while preflight_report claims model/env paths observed. Evidence: "Qwen / Audio Runtime Observations" vs. preflight TTS section. Recommended action: Re-verify gated status before any audio generation.
- [Low] Repo dirty state and untracked `Module10_Dry_Run` (or `Module_Dry_Run`) obscures changes. Evidence: preflight_report "Git status / dirty state" (87 D, 22 M) and final_handoff exclusion note. Recommended action: Future workers must avoid broad cleanup per existing warnings.
- [Medium] Positive deterministic compliance metrics present: source_objective_map.json and module10.content.json both show objectives=16, theory_minutes_total=180, online_clinical_credit_claimed=False, online_hands_on_competency_validated=False, backup/contentv2_used_as_authority=False. Evidence: JSON top-level keys and validation object.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| 16 objectives | PASS | source_objective_map.json: count=16; module10.content.json: count=16; data/content.generated.json: "M10... objectives=16" |
| Exactly 180 weighted theory minutes | PASS | source_objective_map.json: theory_minutes_total=180; module10.content.json: total_weighted_minutes=180; time_allotment_report.md confirms sum |
| No online clinical-hour credit claim | PASS | source_objective_map.json: online_clinical_credit_claimed=False; preflight/final_handoff: "deferred; no online clinical credit... claim is made" |
| No certificate-production readiness claim | PASS | validation_report.md: "no certificate-production readiness claim"; final_handoff: "no certificate... claim"; content shows "Dry-run only" |
| No online hands-on competency validation claim | PASS | source_objective_map.json: online_hands_on_competency_validated=False; multiple reports state "deferred to in-person/evaluator-supported" |
| No PHI | PASS | image_prompts and compliance flags use "De-identified illustration; no PHI"; validation_report: "No PHI examples... intentionally generated" |
| Clinical/manual skills deferred | PASS | preflight: "Six (6) clinical hours are source-recommended only and deferred"; content boundaries state "observe, measure, record... within facility policy" |
| Source authority only (no ContentV2/backup) | PASS | source_objective_map.json: source_authority=PDF path, validation: backup=false, contentv2=false; reports confirm |
| Media generation gated (scripts/prompts only) | PASS | audio_manifest.json: "scripts_only_no_audio_generated"; image_manifest: "prompt_queue_only_no_images_generated"; sfx: "queued_no_sfx_assets_used" |
| Active scope path `Module10_Dry_Run` | FAIL | Actual Path facts: Module10_Dry_Run exists=False; reports and file inventory reference mismatched `Module_Dry_Run` |
| contentV2 points to Module 10 | FAIL | contentV2.generated.ts imports/exports module13 content |

**Open questions / residual risks:**
- Does the running app actually serve Module 10 data given the contentV2 pointer and path mismatch?
- Are there any positive (non-denial) claims buried in the large `data/content.generated.json` (233k) or `module10.content.json` that the term counts do not fully surface?
- Why do preflight and final reports assert `Module10_Dry_Run` paths while the bundle's deterministic file-state facts and contentV2 block contradict them?
- npm vulnerabilities (1 critical) noted in preflight; not a direct compliance item but relevant to production-readiness caveats.
- Image alt text present (15/15) but no runtime verification of generation tooling.

**One-sentence go/no-go recommendation.**  
Conditional go for compliance/regulatory review of the generated artifacts only after the `Module10_Dry_Run` path and contentV2 pointer mismatches are resolved; core no-claim boundaries and 16/180 metrics hold in the source-mapped JSONs but scope execution evidence is inconsistent.