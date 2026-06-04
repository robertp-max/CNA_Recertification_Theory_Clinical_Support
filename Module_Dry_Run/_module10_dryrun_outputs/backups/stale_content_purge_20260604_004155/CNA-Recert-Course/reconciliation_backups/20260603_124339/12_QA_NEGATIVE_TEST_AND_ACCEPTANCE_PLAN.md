# 12 — QA Negative Test and Acceptance Plan

## Purpose

Define negative tests and acceptance criteria that protect the compliance guardrails (gate
integrity, PHI avoidance, optional-clinical separation, answer-key secrecy, active-time).

## Inputs Reviewed

- `00_EXECUTIVE_SUMMARY.md`, `19_COMPLIANCE_REVIEW_CHECKLIST.md`,
  `17_ACCESSIBILITY_AND_MOBILE_QA_CHECKLIST.md`.
- App pages/components (`CertificateGatePage`, `ClinicalHubPage`, `PhiWarningBlock`, exam).

## Evidence / Test Table

| ID | Negative / acceptance test | Procedure | Expected result | Status |
|---|---|---|---|---|
| QA-01 | Certificate cannot issue without all gates | Attempt cert with missing affidavit | Blocked at gate | Not Started |
| QA-02 | Optional clinical cannot gate certificate | Skip clinical, attempt cert | Cert path unaffected | Not Started |
| QA-03 | PHI warning before uploads/free-text | Open every upload/free-text surface | Warning + ack shown | Not Started |
| QA-04 | No PHI fields requested anywhere | Inspect all forms | No DOB/MRN/patient data | Not Started |
| QA-05 | Answer keys not learner-visible | Inspect exam UI + source | Keys server/admin only | Not Started |
| QA-06 | Active-time not satisfied by idle | Idle through a module | Active-time not credited | Not Started |
| QA-07 | Partial-credit disclaimer shown | Review M00 + cert copy | Online-cap ack present | Not Started |
| QA-08 | Mobile/accessibility | Mobile + screen-reader pass | Text alternatives present | Not Started |

## Acceptance Criteria

- All P0 negative tests (QA-01, QA-02, QA-03, QA-04, QA-05) must pass before any go decision.
- Active-time (QA-06) must pass or a documented manual-review hold must be in force.

## Gaps Found

- No automated or manual QA run recorded for these tests.

## Owner / Action Needed

- QA: execute tests against a running build; record evidence (screenshots/logs, no PHI).

## Blocker Status

Acceptance is **Not Started**. These tests are prerequisites to a go decision (not the only ones).

## Next Verification Step

Stand up the app build and run QA-01 through QA-05 first.
