# 19 - Go-Live Hold and Release Criteria

Status: Draft / Pending Approval.

## Hard hold until approval
- The environment may be BUILT and internally tested, but it remains in a HARD HOLD for public/learner CE issuance until each lane's regulator approval is granted. No CE certificate is issued and no approval claim is published before approval.

## Release criteria (all must be satisfied to lift the hold per lane)

1. Regulator approval granted and approval metadata entered (number, dates, approved titles/hours). Approval number/decision = regulator-issued (final human verification required).
2. Legal/privacy signoff recorded (final human verification - legal signature required).
3. SME quiz review completed and sign-off recorded; SME-flagged items resolved (`import_assets/SME_REVIEW_REQUIRED_QUIZ_ITEMS.md`).
4. Certificate metadata confirmed and wording matches approved terms (per lane; RCFE must match approved terms; CNA = online CE/no clinical hours; BRN = contact hours/no certification claim).
5. Reviewer account tested (read-only, scoped, expiring - test RV-01).
6. Report export tested (completion, grade, logs - tests RP-01/02/03).
7. Backup tested and restore verified (test BR-01).
8. No forbidden language present (validation scan clean): no false approval claim; no CNA clinical-hour overclaim; no BRN 4-hour/CEU stale language.
9. No stale structures (CNA 12x2=24; RCFE 9 courses/27h only; BRN 10x3=30 contact hours; 40-hour RCFE remains future-only).
10. No PHI present (test PH-02).

## Decision
- Lift the hold for a lane only when that lane's criteria are all met and recorded. Otherwise remain on hold. See `20_POST_APPROVAL_ACTIVATION_PLAN.md`.
