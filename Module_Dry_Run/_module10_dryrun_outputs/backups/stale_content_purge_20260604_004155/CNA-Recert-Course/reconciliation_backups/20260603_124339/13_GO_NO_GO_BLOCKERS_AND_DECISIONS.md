# 13 — Go / No-Go Blockers and Decisions

## Purpose

State the production go/no-go posture and enumerate the decisions and blockers that must be
resolved before any certificate-issuing launch.

## Inputs Reviewed

- All reconciliation docs 00–12 and 15.
- `PHASE_0_COMPLIANCE_FOUNDATION.md`, `00_EXECUTIVE_SUMMARY.md`.

## Current Decision

**NO-GO for production / certificate issuance.** This is a content + documentation reconciliation
state. No CDPH approval, certificate approval, active-time validation, or export verification of a
Moodle build is claimed.

## P0 Blockers (must clear)

| ID | Blocker | Owner | Status |
|---|---|---|---|
| B1 | CDPH provider/course approval | Program Owner / Legal / CDPH | Open |
| B2 | Approved certificate wording | Legal / CDPH | Open |
| B3 | Affidavit + e-signature acceptance | Legal | Open |
| B4 | Active-time validation (or manual review hold) | QA / Compliance | Open |

## P1 Items (high, not necessarily launch-blocking for theory)

| ID | Item | Owner | Status |
|---|---|---|---|
| H1 | Re-export 22 failed Google Docs/Sheet as PDF | Program Owner | Open |
| H2 | Parse spreadsheet for URL positional mapping | Repo Auditor | Open |
| H3 | App-wiring runtime verification | App Engineer / QA | Open |
| H4 | Final exam SME item-match | SME | Open |
| H5 | Owner decision on skipped videos + Admission Exam folder | Program Owner | Open |

## Decisions Needed From Owner

1. Are clinical-skill videos in scope for transfer, or intentionally excluded?
2. Is the "Admission Exam" Drive folder in scope for recert theory?
3. E-signature vs wet-signature for the affidavit?
4. TTS/narration: authorize or keep as text-only?

## Gaps Found

- All P0 blockers are external approvals/validations not present in the repo.

## Owner / Action Needed

- Program Owner: drive B1–B4 and H1, H5; record decisions here.

## Blocker Status

**NO-GO.** Do not enable live certificate issuance.

## Next Verification Step

Schedule CDPH approval status review (B1) — it gates B2 and the entire go decision.
