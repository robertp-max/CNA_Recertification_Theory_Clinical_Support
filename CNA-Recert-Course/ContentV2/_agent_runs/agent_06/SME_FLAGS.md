# SME Flags

## Required Preserved Flags

| Area | Required flag | Coordinator action |
|---|---|---|
| Module 1 Infection Control and Prevention | SME/source-review required for all Module 1 infection-control content and narration. | Preserve flag on all Module 1 cards, narration rows, schema records, and media placeholders. Do not finalize audio/media until approved source review is complete. |
| Module 5 Skin Integrity / Pressure Injury Prevention | SME/source-review required for skin integrity and pressure injury content. | Preserve flag on `modules.m5.l3.c01`, related skin-integrity media placeholders, and any pressure-injury assessment items. |
| Final exam Q01, Q02, Q03, Q41 | Preserve existing flags where present. | Do not drop, rename, or flatten these flags during schema migration. |
| Final exam Q21/Q38 | Preserve existing flags where present. | Treat as flagged exam-bank rows until coordinator confirms disposition. |

## New SME Notes From This Pass

- No new SME issue was independently validated because only the TTS planning source was directly reviewed.
- TTS source itself already marks Module 1 content and Module 5 skin integrity content as requiring SME/source confirmation before audio production.

## SME Merge Caution

If app/data adapters normalize content into JSON, make SME flags explicit fields such as:

```json
{
  "smeReviewFlag": "Module 1 infection-control SME/source-review required",
  "smeReviewStatus": "Required"
}
```

Avoid preserving flags only in free-text notes.
