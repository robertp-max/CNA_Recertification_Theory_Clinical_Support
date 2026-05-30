# Source Coverage Audit

## Coverage Boundary

This audit reviewed assigned source/control files only. Non-assigned Content files were listed for inventory and classification, but their contents were not opened.

## Coverage Summary

| Area | Coverage status | Notes |
|---|---|---|
| Updated package index | Covered | `35_CONTENT_PACKAGE_INDEX_UPDATED.md` reviewed directly. |
| Source title verification | Covered | `SOURCE_TITLE_VERIFICATION_PASS.md` reviewed directly. |
| Time allocation correction | Covered | `TIME_ALLOCATION_CORRECTION_NOTICE.md` reviewed directly. |
| QA controls | Covered | Seven `Content/qa` files reviewed directly. |
| Full Content file listing | Covered as inventory only | Current connector inventory surfaced 47 Content paths. |
| Learner content files | Not content-reviewed in this assignment | Classification is based on index/QA controls and listing only. |
| Source PDFs or regulatory source originals | Not in assigned scope | No source PDF content was opened. |
| ContentV2 canonical files | Not in assigned scope | No canonical ContentV2 file was inspected or modified. |

## Source Count Reconciliation Needed

Reviewed controls do not agree on package counts:

| Control | Count stated | Interpretation |
|---|---:|---|
| `CONTENT_EXTRACTION_REPORT.md` | 43 files created | Reports 36 core package files, 2 source-verification files, and 5 QA files. |
| `GIT_TRACKING_VERIFICATION.md` | 45 tracked Content files | Dated 2026-05-26; confirms uppercase `Content` path. |
| `CNA_CONTENT_PHASE_CLOSEOUT.md` | 45 files counted under tracked Content path | Same closeout phase as git verification. |
| Current connector inventory | 47 Content paths surfaced | Includes seven QA files and the TTS production workbook helper path. |

Coordinator should reconcile the authoritative count before building `source_copy` or merge manifests.

## Coverage Risks

1. `CONTENT_PACKAGE_QA_REPORT.md` references `GROK_NEXT_BUILD_ACTIONS.md` as present, but the current `qa` listing showed `NEXT_MOODLE_BUILD_PROMPT.md`. This may be a rename or stale QA reference.
2. `CONTENT_EXTRACTION_REPORT.md` says extraction used `Content/Raw/Claude/Batch2.md`, but the current assigned listing surfaced only `Content/Raw/Claude/Batch1.md`. Confirm whether Batch2 exists locally, is untracked, was renamed, or was omitted.
3. Module 1 infection-control content remains flagged because reviewed controls do not identify a confirmed standalone NATP infection-control source.
4. Module 5 skin integrity / pressure injury content remains flagged because reviewed controls explicitly state no confirmed standalone NATP skin integrity module exists in the uploaded source set.
5. Older duplicate files remain in the Content tree and could be accidentally ingested if the merge process uses a broad glob. Prefer updated complete files by precedence.
6. `Content` path casing is significant. Use `CNA-Recert-Course/Content`, not lowercase `content`.
7. QA/control files include staging and production blockers. Do not transform "staging ready" into "production ready."

## Canonical Versus Secondary Status Rules

Use these rules for merge planning:

1. A file is canonical if it is the current learner/content/data artifact named by the updated package index and not superseded by a later complete artifact.
2. A file is secondary if it is raw transcript material, an older duplicate, a planning artifact, or a previous version superseded by a complete file.
3. A file is QA/control if it defines readiness, risks, source verification, timing corrections, templates, mappings, checklists, or implementation constraints.
4. QA/control files may block or qualify a canonical file, but they should not replace learner content unless the coordinator intentionally converts a control into admin metadata.
5. Source-verification controls override older source labels when they conflict.
6. Flags are part of the canonical metadata surface and must travel with affected content.

## Recommended source_copy Expectations

The coordinator should create or validate a `source_copy` area with:

- Exact uppercase source paths.
- Source status class: canonical, secondary, or QA/control.
- Source precedence notes for duplicate groups.
- Source verification records for NATP titles and Module 7 timing.
- Active SME flags for Module 1 and Module 5.
- Active compliance flags for optional clinical, certificate, affidavit, placeholders, no-PHI, and TTS.
- A recorded source commit, timestamp, or checksum method.
- A note that TTS scripts are planning artifacts only and that no audio/media was produced.
- A note that certificate production is disabled and no provider/CDPH metadata was fabricated.

Do not include:

- Any PHI or learner uploads.
- Generated audio/media.
- Fabricated certificate assets or approval metadata.
- Broad duplicated imports that include both old and updated versions without precedence labels.

## Duplicate/Superseded Groups To Guard

| Prefer | Do not prefer unless explicitly needed | Reason |
|---|---|---|
| `CNA-Recert-Course/Content/theory/exam/30_FINAL_EXAM_POOL_50_COMPLETE.md` | `CNA-Recert-Course/Content/exam/10_FINAL_EXAM_POOL_50.md` | Complete current final exam pool supersedes older pool. |
| `CNA-Recert-Course/Content/csv/31_QUIZ_BANK_MASTER_COMPLETE.csv` | `CNA-Recert-Course/Content/csv/11_QUIZ_BANK_MASTER.csv` | Complete current CSV supersedes older CSV. |
| `CNA-Recert-Course/Content/theory/tts/34_TTS_NARRATION_PACKAGE_COMPLETE.md` | `CNA-Recert-Course/Content/16_TTS_NARRATION_PACKAGE.md` | Current TTS package supersedes older planning package, but remains planning only. |
| `CNA-Recert-Course/Content/index/35_CONTENT_PACKAGE_INDEX_UPDATED.md` | `CNA-Recert-Course/Content/23_CONTENT_PACKAGE_INDEX.md` | Updated index supersedes older index. |
| `CNA-Recert-Course/Content/theory/modules/29_THEORY_MODULE_07_REVIEW_FINAL_EXAM_AFFIDAVIT_FULL.md` plus `TIME_ALLOCATION_CORRECTION_NOTICE.md` | Any 90-minute Module 7 reference | Module 7 must remain 30 minutes. |

## Coverage Conclusion

The reviewed controls are internally strong on compliance boundaries and flag preservation, but the source manifest still needs reconciliation before canonical merge. The highest merge risks are count drift, stale/renamed QA references, missing Batch2 source-copy traceability, duplicate file ingestion, and accidental production exposure of placeholders or certificate logic.
