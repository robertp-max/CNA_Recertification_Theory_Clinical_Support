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
