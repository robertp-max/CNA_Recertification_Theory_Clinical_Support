# 11 — Audit Packet Evidence Map

## Purpose

Map the layered evidence model required for the certificate gate to its sources of record, so an
audit packet can be assembled. Identity, completion, interaction, active-time, exam, affidavit, and
admin clearance must all be evidenced — not Moodle logs alone.

## Inputs Reviewed

- `CNA-Recert-Course\Content\00_EXECUTIVE_SUMMARY.md` (layered evidence model).
- `manifest.json` (export provenance).
- App pages/components.

## Evidence Table

| Evidence type | Source / record | Status | Notes |
|---|---|---|---|
| Identity capture | M00 identity fields (name + CNA cert #) | Needs App Verification | DOB excluded |
| Completion evidence | completion tracking export | In Progress | Layered, not logs alone |
| Interaction evidence | interaction/check logs | In Progress | |
| Active-time evidence | active-time records | Needs Compliance Review | Plugin not validated |
| Exam result evidence | exam attempt/pass record | In Progress | Keys internal only |
| Affidavit evidence | signed affidavit record | Needs Legal/CDPH Review | E-sign unresolved |
| Admin clearance evidence | manual review log | In Progress | |
| Export provenance | `manifest.json` | Complete | Copy provenance for source docs |

## Preserved Facts

- Do not rely on Moodle logs alone as active-participation evidence.
- No PHI may appear in any audit artifact (no patient names, DOB, MRN, chart images).

## Gaps Found

- Audit records for active-time and affidavit/e-sign are not yet producible (upstream blockers).
- No assembled, retained audit packet exists yet.

## Owner / Action Needed

- Compliance: define retention period and packet contents.
- App Engineer: ensure each gate emits an auditable record.

## Blocker Status

Audit packet cannot be finalized until certificate blockers (active-time, affidavit, CDPH) clear.

## Next Verification Step

Define the audit packet schema (one record per gate per learner) and confirm no-PHI fields.
