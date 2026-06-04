# Prototype Build 1 - Certificate Gate Proof of Concept

## Purpose

This folder contains the staging implementation scaffold for Prototype Build 1. The goal is to prove Moodle can prevent online CE certificate release until required certificate gates are complete, while keeping optional clinical support outside the certificate gate.

## Prototype Scope

Prototype Build 1 includes only:

- Moodle shell structure.
- Module 0 orientation.
- One sample theory module.
- One required interaction/check.
- One final exam/test placeholder.
- One affidavit placeholder.
- One certificate gate prototype.
- One optional clinical support section.
- One active-time validation setup.
- One audit export dry run.

## Hard Boundaries

- Do not build the full course.
- Do not generate final lesson content.
- Do not create production Moodle configuration.
- Do not implement custom Moodle plugins.
- Do not treat optional clinical support as a certificate gate.
- Do not include clinical hours on the online CE certificate.
- Do not assume CDPH approval, final certificate wording, e-signature approval, or active-time plugin accuracy.
- Do not collect PHI.
- Do not add new video production to MVP.

## File Index

| File | Use |
|---|---|
| `PROTOTYPE_1_BUILD_PLAN.md` | Exact prototype scope and component map. |
| `MOODLE_STAGING_BUILD_STEPS.md` | Moodle admin build checklist. |
| `MOODLE_ACTIVITY_SHELL_SPEC.md` | Activity shell configuration. |
| `CERTIFICATE_GATE_POC_CONFIG.md` | Gate logic and negative tests. |
| `ACTIVE_TIME_POC_TEST_PLAN.md` | Prototype active-time validation plan. |
| `REQUIRED_OPTIONAL_SEPARATION_CHECK.md` | Required vs optional validation checklist. |
| `OPTIONAL_CLINICAL_HUB_STUB_SPEC.md` | First optional clinical support stub and draft copy. |
| `AUDIT_EXPORT_DRY_RUN_PLAN.md` | Evidence export dry-run plan. |
| `QA_EXECUTION_TRACKER.md` | Prototype 1 QA matrix. |
| `PROTOTYPE_1_ACCEPTANCE_CRITERIA.md` | Pass criteria. |
| `PROTOTYPE_1_OPEN_BLOCKERS.md` | Current blockers. |
| `csv/` | Prototype-scoped CSV copies. |
