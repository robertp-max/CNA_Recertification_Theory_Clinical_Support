# Merge Notes

## Coordinator Merge Cautions

1. Merge this scratch output as audit input only. Do not treat `CONTENT_OUTPUT.md` as canonical course content.
2. Reconcile Content file count before source_copy merge. Current controls say 43, 45, and current inventory surfaced 47.
3. Resolve the QA filename mismatch before citing next-build controls: `GROK_NEXT_BUILD_ACTIONS.md` is referenced by QA, but `NEXT_MOODLE_BUILD_PROMPT.md` is the file surfaced in the current listing.
4. Confirm whether `CNA-Recert-Course/Content/Raw/Claude/Batch2.md` exists locally, is untracked, or was omitted. Do not claim full raw source-copy coverage until this is resolved.
5. Use uppercase `CNA-Recert-Course/Content` in manifests and scripts.
6. Do not ingest old duplicate files when complete current files exist. Guard File 10 versus 30, File 11 versus 31, File 16 versus 34, and File 23 versus 35.
7. Preserve Module 1 infection-control and Module 5 skin integrity / pressure injury SME/source-review flags in every migration layer.
8. Preserve final exam Q01, Q02, Q03, Q41, and Q21/Q38 flags in both exam content and machine-readable quiz metadata.
9. Keep Optional Clinical Support optional, non-credit, non-gating, not clinical-hour credit, and excluded from certificate gate logic.
10. Keep certificate production disabled. Do not fabricate NAC#, provider number, CDPH contact information, certificate wording, approval metadata, or affidavit wording.
11. Keep TTS as planning only. Do not generate audio/media from File 34 or the production workbook helper.
12. Treat QA/build readiness as staging readiness only. Production launch remains blocked by placeholders, legal/compliance review, active-time validation, certificate gate testing, and source review.

## Suggested Merge Order

1. Build the source_copy manifest first.
2. Apply source precedence labels to duplicate groups.
3. Attach SME and compliance flags as metadata before migrating learner content.
4. Map learner content to app locations only after flags and source status are attached.
5. Keep certificate and optional clinical gate logic disabled until a separate coordinator-approved implementation pass.

## Do Not Merge Automatically

- Raw transcript content as learner-facing copy.
- QA reports as learner-facing copy.
- Placeholder CDPH/provider/contact text.
- TTS production workbook output.
- Certificate or affidavit wording as final production wording.
- Any source flag removal.

## Handoff State

This worker did not run build/test, did not commit, did not push, did not modify original Content, and did not modify canonical ContentV2 files outside this scratch folder.
