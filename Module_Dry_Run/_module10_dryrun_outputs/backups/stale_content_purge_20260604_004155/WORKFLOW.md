# Workflow

This repository supports documentation and staging preparation for Prototype Build 1 - Certificate Gate Proof of Concept.

## Boundaries

- Do not generate final course content.
- Do not configure production.
- Do not implement custom plugins.
- Do not treat optional clinical support as required.
- Do not include clinical hours on the online CE certificate.
- Do not collect or commit PHI.

## Staging Sequence

1. Begin Moodle staging configuration using `staging/prototype_1_certificate_gate_poc/MOODLE_ADMIN_EXECUTION_RUNBOOK.md`.
2. Configure Moodle settings according to `staging/prototype_1_certificate_gate_poc/MOODLE_SETTINGS_MAP.md`.
3. Create synthetic QA learners using `staging/prototype_1_certificate_gate_poc/TEST_LEARNER_MATRIX.md`.
4. Execute `staging/prototype_1_certificate_gate_poc/QA_EXECUTION_TRACKER.md`.
5. Capture evidence using `staging/prototype_1_certificate_gate_poc/EVIDENCE_CAPTURE_CHECKLIST.md`.
6. Log implementation actions in `staging/prototype_1_certificate_gate_poc/STAGING_IMPLEMENTATION_LOG.md`.
7. Log defects in `staging/prototype_1_certificate_gate_poc/DEFECT_LOG.md`.

## Evidence Handling

Evidence folders such as `/audit-evidence/`, `/screenshots/`, `/learner-data/`, `/test-evidence/`, `/private-approvals/`, and `/production-evidence/` are ignored by Git and should remain outside committed source control history.

