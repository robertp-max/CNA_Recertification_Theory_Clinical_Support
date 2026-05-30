# Content Output

## Narration Guidance

- Keep narration as planning text only until course-owner authorization and compliance review approve production.
- Preserve the current short-segment model: roughly 30-90 seconds per segment.
- Add a normalized narration CSV layer with stable `app.location` values, source references, estimated word counts, estimated seconds, and explicit SME/compliance flags.
- Target duration status should be a QA field, not a production promise. Recommended statuses: `Within target`, `Review timing`, `Too long`, `Too short`, `Blocked`.
- Voice notes should include pronunciation guidance already present in the TTS source and should not introduce new claims.

## Media Placeholder Guidance

- Use placeholders only. Do not generate images, video, audio, avatars, voiceovers, or clinical simulation media in this pass.
- Media prompt placeholders should describe intent and compliance constraints, not asset production commands.
- Use fictional/de-identified scenarios only. Avoid resident names that could be mistaken for real learners or patients.
- Do not request uploads, identifiers, facility records, resident photos, medical records, or PHI.
- Suggested placeholder types:
  - `media.placeholder.infection-chain.diagram`
  - `media.placeholder.hand-hygiene.sequence`
  - `media.placeholder.resident-rights.scenario`
  - `media.placeholder.transfer-safety.checklist`
  - `media.placeholder.skin-integrity.positioning`
  - `media.placeholder.documentation.sbar`
  - `media.placeholder.final-review.summary`

## JSON / Schema Expectations

Recommended narration object fields:

```json
{
  "project": "CNA Recertification Theory",
  "moduleId": "m1",
  "moduleTitle": "Infection Control and Prevention",
  "lessonId": "m1.l1",
  "lessonTitle": "Chain of Infection",
  "cardId": "m1.l1.c01",
  "cardType": "narration",
  "title": "Chain of Infection",
  "appLocation": "modules.m1.l1.c01",
  "narration": "Planning transcript text only.",
  "transcript": "Same as narration unless edited for captions.",
  "estimatedSeconds": 50,
  "estimatedWordCount": 120,
  "targetDurationStatus": "Within target",
  "voiceNotes": "Pronunciation notes.",
  "sourceReference": "CNA-Recert-Course/Content/theory/tts/34_TTS_NARRATION_PACKAGE_COMPLETE.md#TTS-1-001",
  "smeReviewFlag": "Module 1 infection-control SME/source-review required.",
  "complianceReviewFlag": "TTS planning only; no audio production.",
  "status": "Draft"
}
```

Schema cautions:

- Require stable `appLocation` strings and avoid deriving them from visible titles.
- Treat `moduleId`, `lessonId`, `cardId`, and `appLocation` as immutable adapter keys once canonicalized.
- Keep `narration` and `transcript` text separate even when identical so captions can diverge later if needed.
- Use explicit null/empty flag values such as `None identified` rather than omitting review fields.

## App Adapter Wiring Risks

- App locations must be mapped from canonical content identifiers, not from array position, route text, or learner-facing headings.
- Final exam bank flags must survive any JSON transform, especially Q01, Q02, Q03, Q41, and Q21/Q38 where present.
- Certificate gate UI must remain disabled/status-only until certificate production is authorized.
- Optional Clinical Support routes/cards must not be counted in theory completion, active-time requirements, final exam eligibility, affidavit release, or certificate release.
- If `standalone-course-mvp/src/data` uses static arrays, coordinator should add validation for duplicate IDs, missing `app.location`, and accidental optional-clinical gating fields.

## Final QA Checklist

- No PHI or upload request language.
- No generated media/audio.
- TTS authorization disclaimer preserved.
- Module 1 infection-control SME/source-review flag preserved.
- Module 5 skin integrity/pressure injury SME/source-review flag preserved.
- Final exam Q01/Q02/Q03/Q41 and Q21/Q38 flags preserved where present.
- Optional Clinical Support optional, non-credit, non-gating, and not clinical-hour credit.
- Certificate production disabled; no fabricated NAC, CDPH, provider, approval, affidavit, or certificate wording.
