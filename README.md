# California CNA Recertification Theory + Optional Clinical Support

## Project Purpose

This repository holds implementation planning, compliance boundaries, Moodle build specifications, QA/UAT controls, and staging artifacts for a California CNA recertification support project.

The planned Moodle implementation includes a 12-hour online theory CE course and a visually and technically separate optional clinical support hub. The online theory course is partial renewal credit only. California CNA renewal requires 48 hours over 2 years, with at least 12 hours each year, and only 24 hours may be completed online through CDPH-approved online CE.

## Current Phase

Current phase: Prototype Build 1 - Certificate Gate Proof of Concept.

The repository is ready to move from planning packet to Moodle staging configuration, limited to proving certificate release controls. It is not ready for production launch or certificate-enabled pilot.

## Compliance Boundary

- Do not assume CDPH approval, final certificate wording, final e-signature approval, or validated active-time plugin accuracy.
- Do not collect PHI.
- Do not treat optional clinical support, simulation, virtual simulation, or LTI simulation as clinical-hour credit unless CDPH approves that use in writing.
- Do not include clinical hours on the online CE certificate.
- Moodle logs alone are not enough for active participation evidence.

## Required vs Optional Rule

Required online CE activities may gate certificate release. Optional clinical support activities must remain separate, optional, ungraded by default, and outside the online CE certificate gate.

Required learner-facing progress should be labeled as online CE certificate requirements. Optional clinical support should be labeled as optional clinical support, skills refresh, practice support, or documentation support.

## Certificate Gate Priority

Prototype Build 1 prioritizes proving that Moodle can block certificate release until the required identity, theory, interaction, active-time, assessment, affidavit, certificate-field, admin-hold, and audit evidence conditions are satisfied.

Optional clinical support completion must not be a certificate gate by default.

## Repository Folder Map

| Path | Purpose |
|---|---|
| `CNA-Recert-Course/PHASE_0_COMPLIANCE_FOUNDATION.md` | Compliance foundation and governing assumptions. |
| `CNA-Recert-Course/PHASE_2_MOODLE_ARCHITECTURE_REPORT.md` | Moodle architecture direction. |
| `CNA-Recert-Course/PHASE_3_INSTRUCTIONAL_DESIGN_REPORT.md` | Instructional design planning. |
| `CNA-Recert-Course/PHASE_4_MIGRATION_MVP_OPERATIONS_REPORT.md` | MVP operations and migration planning. |
| `CNA-Recert-Course/FINAL_UNIFIED_IMPLEMENTATION_BLUEPRINT.md` | Unified implementation blueprint. |
| `CNA-Recert-Course/PHASE_5_BUILD_SPEC_PACKET/` | Build specification packet, matrices, QA scripts, learner copy, and audit specs. |
| `staging/prototype_1_certificate_gate_poc/` | Prototype Build 1 staging implementation scaffold. |

## First Staging Prototype Goal

Prototype Build 1 must prove the certificate gate logic with a Moodle shell, Module 0 orientation, one sample required theory module, one required interaction/check, one final exam/test placeholder, one affidavit placeholder, one certificate gate prototype, one optional clinical support section, one active-time validation setup, and one audit export dry run.

## Next Action

Create the Moodle staging course shell and configure completion tracking, Restrict Access, required profile fields, active-time validation, and certificate activity availability according to `staging/prototype_1_certificate_gate_poc/MOODLE_STAGING_BUILD_STEPS.md`.
