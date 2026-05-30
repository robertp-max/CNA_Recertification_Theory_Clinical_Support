# Compliance Flags

## Standing Compliance Boundaries

These boundaries must be preserved in any merge:
- The course is partial California CNA online CE theory only.
- The theory total is 720 minutes / 12 hours.
- Module 7 is 30 minutes, not 90 minutes.
- Optional Clinical Support is optional, non-credit, non-gating, not clinical-hour credit, and never a certificate gate.
- Certificate production remains disabled.
- TTS scripts are planning artifacts only. Do not generate audio or media.
- No PHI. Use only fictional or de-identified examples. Do not request uploads or real identifiers.
- Do not fabricate NAC#, CE provider number, CDPH contact information, approval metadata, affidavit wording, or certificate wording.

## Active Compliance/Legal Flags

| Flag | Source/control basis | Required action |
|---|---|---|
| Affidavit legal review | Index File 29; QA report; Risk R03 | Legal/compliance/CDPH review required before learner-facing affidavit use. |
| Certificate wording and CE claim | Index File 29; Risk R03/R04/R08 | Certificate disabled until provider ID, wording, and gate behavior are approved and tested. |
| CE provider NAC# pending | Risk R04; QA placeholder check | Do not invent or infer. Insert only confirmed current provider information. |
| CDPH contact placeholders | QA placeholder check; Risk R05 | Replace only with verified current contact details before production. |
| Active-time plugin validation | Risk R07 | Must be validated before CE credit workflows are trusted. |
| Certificate gate implementation | Risk R08 | Build and test all gate conditions in staging before production. |
| Optional clinical support separation | QA required/optional check; Risk R09 | Must remain visibly separate, non-prerequisite, non-credit, and excluded from certificate gate logic. |
| Final exam Moodle configuration | QA check; Risk R10 | Configure 25 random questions from full 50-question pool, 80% pass, 2 attempts. Preserve flagged question metadata. |
| TTS authorization and AI disclosure | QA TTS check; Risk R06 | No synthesis, recording, or media production without explicit authorization and required disclosure review. |

## PHI Status

Reviewed QA controls report that scenario names are fictional and no PHI was detected. Merge should retain no-PHI warnings and avoid any workflow that asks learners to upload real resident, patient, employer, or medical identifiers.

## New Compliance Issues Found

No new compliance issue was found beyond existing reviewed blockers. The main merge risk is that placeholders or disabled certificate logic could accidentally become learner-facing during migration.
