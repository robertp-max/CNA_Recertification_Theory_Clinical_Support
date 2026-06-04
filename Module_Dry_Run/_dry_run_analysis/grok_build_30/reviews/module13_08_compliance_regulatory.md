**# Review 08_compliance_regulatory — Module 13**

**Verdict:** PASS WITH RISKS

**Top findings:**
- [High] Hard failure: audio/audio_manifest.json and audio/narration_batch_import_package.json both report status="scripts_only_no_audio_generated", qwen_sent=False, csv_used=False, and all 32 clips as "queued_not_generated" with final_path_nonempty=0, directly contradicting final_handoff.md and validation_report.md claims that "Qwen voice-clone TTS processing was launched in background" and "may still be in progress". Evidence: audio/audio_manifest.json (lines on status/clips), reports/final_handoff.md, reports/validation_report.md.
- [High] Hard failure: audio/logs/qwen_tts_background.stderr.log contains multiple PowerShell parse errors (null-coalescing ?? operator, missing closing braces/parentheses, incomplete Try/Catch) in run_qwen_tts_resume_until_done.ps1, blocking execution. Evidence: full stderr.log excerpt showing "Unexpected token '??'", "Missing closing '}'", and "The Try statement is missing its Catch".
- [High] Gated requirement gap: no evidence in any log, manifest, or script that the exact required components were used (model `C:/AI/Qwen3-TTS-12Hz-1.7B-Base`, Python env `C:/AI/qwen3-tts-env`, voice reference `C:/AI/Git/training/CI-ION/.../FINAL_REVIEW_EXPORT_GUIDANCE_001.wav`). Evidence: absence across audio/ directory files, reports, and source_map/.
- [Medium] Self-reported "PASS" in validation_report.md for Qwen/TTS and overall validation is lower-strength evidence and contradicted by deterministic metrics (manifests show 0 generated clips; 26 WAVs noted in qwen_tts dir but not reflected in audio_manifest.json). Evidence: reports/validation_report.md "Qwen/TTS processing launched" row vs. audio/audio_manifest.json.
- [Medium] Clinical and hands-on terms appear in generated content (e.g., "clinical-hour credit", "hands-on competency", "online hands-on") even when framed as restrictions; requires explicit verification that no positive claims exist in final JSONs. Evidence: "Risk-Term Contexts From Generated Data" section listing multiple instances plus sample contexts from data/module13.content.json and data/content.generated.json.
- [Medium] Production-readiness caveats are present in reports but undermined by successful `npm run build` (rc=0) and app integration (contentV2.generated.ts repointed, build artifacts produced) without stronger isolation language. Evidence: reports/final_handoff.md "Build Result" section, Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts.
- [Low] data/module13.activities.json reports blank objective titles ("1. ; 2. ; ...") in the evidence summary despite correct count=8 and min_activities=3; minor data consistency risk vs. full titles in module13.content.json. Evidence: data/module13.activities.json top-level keys and objectives summary.
- [Low] 26 WAV files observed in qwen_tts directory while manifests report zero final_path_nonempty and status "scripts_only"; file-state vs. manifest mismatch. Evidence: "Qwen / Audio Runtime Observations" + audio/audio_manifest.json.

**Checkpoint table:**

| Check | Status | Evidence |
|-------|--------|----------|
| No CDPH/TPRU approval claim | PASS | Explicit disclaimers in reports/validation_report.md, reports/final_handoff.md, source_objective_map.json validation section; no positive statements |
| No certificate-production readiness claim | PASS | "Dry-run complete does not issue a production certificate", "Certificate remains locked and non-production" in reports/final_handoff.md and validation_report.md |
| No online clinical-hour credit claim | PASS | online_clinical_credit_claimed: False in source_objective_map.json; repeated "This dry run does not ... claim clinical-hour credit" in generated content contexts and reports |
| No online hands-on competency validation claim | PASS | online_hands_on_competency_validated: False in source_objective_map.json; explicit restrictions in clinicalHub and assessment sections |
| No PHI | PASS | All image prompts specify "no PHI"; no PHI examples in any generated JSON or reports; compliance_flags section confirms |
| Clinical/manual skills deferred to in-person | PASS | "4 source-required clinical hours deferred", "theory preparation only", "evaluator-supported validation" repeated in source_objective_map.json, reports/time_allotment_report.md, reports/final_handoff.md |
| Objectives count = 8 (module-declared) | PASS | source_objective_map.json (count=8), data/module13.content.json (count=8), data/module13.activities.json (count=8); titles match source PDF |
| Weighted theory minutes = 780 (module-declared) | PASS | source_objective_map.json theory_minutes_total=780, data/module13.content.json total_weighted_minutes=780; time_allotment_report.md breakdown sums to 780 |
| Narration package is JSON only (no CSV) | PASS | audio/narration_batch_import_package.json (format JSON, csv_used=False); audio/audio_manifest.json confirms csv_used=False |
| Source authority is official Module 13 PDF only | PASS | source_authority: 'CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-13.pdf' in source_objective_map.json, data/module13.content.json, data/module13.activities.json; validation confirms no ContentV2/prior outputs/backups used |
| Image prompts have alt text; generation gated | PASS | media/image_manifest.json (alt_text_count=9, status="prompt_queue_only_no_images_generated"); media/image_prompt_queue.json present |
| SFX license-gated/queued | PASS | audio/sfx_manifest.json (status="queued_no_sfx_assets_used", items=7) |
| Qwen TTS execution per gated requirement | FAIL | Script errors + manifests show no generation despite reports claiming launch; specific model/env paths unverified |

**Open questions / residual risks:**
- TTS requirement cannot be treated as satisfied; script failures and status contradictions mean the gated audio component remains incomplete.
- Whether all instances of clinical-hour/hands-on/approval terminology in the final generated JSONs (data/module13.content.json, data/content.generated.json) are strictly negative/disclaimer-only.
- Status and provenance of the 26 observed WAV files relative to manifests that claim zero generated output.
- Impact of pre-existing repo dirty state on long-term auditability of compliance artifacts.
- No deterministic confirmation that the exact rubric-specified TTS model, env, and voice reference paths were invoked.

**One-sentence go/no-go recommendation.**  
Module 13 meets core no-claim, boundary, and source-metric compliance requirements with explicit disclaimers and correct 8-objective/780-minute values, but the high-severity TTS execution failures and report-vs-metric contradictions block clean progression until remediated.