# Merge Notes

## Coordinator Merge Cautions

- Treat every file in this folder as scratch guidance only. Do not copy directly into canonical `ContentV2` without coordinator normalization.
- Preserve TTS authorization language. The TTS package is not production authorization.
- Preserve Module 1 infection-control SME/source-review flags and Module 5 skin integrity/pressure injury SME/source-review flags in every generated schema row.
- Preserve final exam Q01, Q02, Q03, Q41 and Q21/Q38 flags where present. Add an automated check if canonical data is transformed.
- Keep Optional Clinical Support out of all required theory gates, final exam gates, affidavit gates, active-time minimums, and certificate gates.
- Keep certificate production disabled. Do not merge certificate copy, certificate metadata, provider numbers, NAC fields, CDPH approval language, or final affidavit wording from scratch notes.
- Do not attach media files or audio assets. Media guidance here is placeholder-only.
- Before merging app adapter changes, inspect local `standalone-course-mvp/src/data` and `standalone-course-mvp/src/pages`; this pass could not verify local TSX wiring due shell failure.

## Suggested Validation Before Canonical Merge

- Validate unique IDs: `moduleId`, `lessonId`, `cardId`, and `app.location`.
- Validate required review fields exist on every narration/media/content row.
- Validate optional clinical support namespace starts with `clinical.*`.
- Validate no `clinical.*` item is included in certificate-gating arrays or completion requirements.
- Validate certificate gate displays disabled/status-only states.
- Validate no row contains PHI collection language or real-identifier upload requests.
