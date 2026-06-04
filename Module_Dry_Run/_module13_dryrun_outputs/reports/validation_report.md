# Validation Report — Module 13

Date: 2026-06-04T08:09:30
Validation result: **PASS**

| Check | Status | Evidence |
|---|---:|---|
| 8 objectives present | PASS | count=8 |
| terminology extracted | PASS | count=290 |
| weighted minutes exactly 780 | PASS | total=780 |
| >=3 activities per objective | PASS | all objectives |
| JSON narration package/no CSV | PASS | json present, csv absent |
| Qwen/TTS processing completed | PASS | User clarified Qwen TTS is part of the requirement. Resumable Qwen TTS generator/runner scripts were repaired and completed: 32/32 manifest clips generated, 32 WAVs readable, 0 failures. See `qwen_audio_reconciliation_report.md`. |
| image alt text | PASS | items=9 |
| sfx license gated | PASS | items=7 |
| source authority only Module 13 PDF | PASS | no backups/ContentV2/prior outputs used as authority |
| app typecheck/build | PASS | npm run typecheck rc=0; npm run build rc=0;  > standalone-course-mvp@0.1.0 typecheck > tsc --noEmit   > standalone-course-mvp@0.1.0 build > tsc && vite build  [36mvite v7.3.3 [32mbuilding client environment for production...[36m[39m transforming... [32m✓[39m 1763 modules transformed. rendering chunks... computing gzip size... [2mdist/[22m[32mindex.html                 [39m[1m[2m  0.61 kB[22m[1m[22m[2m │ gzip:   0.37 kB[22m [2mdist/[22m[35massets/index-CAgn5VpC.css  [39m[1m[2m 51.72 kB[22m[1m[22m[2m │ gzip:  10.42 kB[22m [2mdist/[22m[36massets/index-BJnXFJxZ.js    |

## Compliance Flags
- No CDPH/TPRU approval claim.
- No certificate-production readiness claim.
- No clinical-hour credit claim.
- No online hands-on competency validation claim.
- No PHI examples or requests intentionally generated.
- Sample test answer key mapped internal-only.
- Audio/TTS/Qwen processing was authorized as a run requirement and completed through the resumable runner.

## Residual Risks
- Generated content is source-map-derived draft and requires SME/compliance review.
- Speech audio generation is complete for the current 32-clip Module 13 manifest; future script reruns should skip existing generated WAVs.
- SFX assets license-gated/queued.
- Images prompt queue only.
- Root repo has unrelated dirty state; no broad Git cleanup performed.
