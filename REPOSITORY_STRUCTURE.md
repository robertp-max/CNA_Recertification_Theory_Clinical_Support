# Repository Structure

## Current Layout

| Path | Status | Notes |
|---|---|---|
| `README.md` | Active | Root project overview and current build direction. |
| `BUILD_READINESS_STATUS.md` | Active | Readiness, blockers, exclusions, and Prototype 1 success criteria. |
| `NEXT_BUILD_STEP.md` | Active | Immediate next implementation step. |
| `CNA-Recert-Course/` | Source planning package | Primary compliance, architecture, design, operations, blueprint, and build spec documents. |
| `CNA-Recert-Course/PHASE_5_BUILD_SPEC_PACKET/` | Source build spec packet | Certificate gate, active-time, required/optional, clinical support, audit, plugin, QA, learner copy, and staging backlog specs. |
| `CNA-Recert-Course/PHASE_5_BUILD_SPEC_PACKET/CSV/` | Source matrices | Original CSV matrices. Do not overwrite during prototype work. |
| `staging/prototype_1_certificate_gate_poc/` | Prototype Build 1 scaffold | Moodle staging build plan, activity shells, gate configuration, QA tracker, audit dry run, blockers, and prototype CSV copies. |
| `staging/prototype_1_certificate_gate_poc/csv/` | Prototype CSV copies | Prototype-specific rows and scoped matrices copied from source concepts without destroying originals. |

## Source Documents

| Document | Implementation Use |
|---|---|
| `PHASE_0_COMPLIANCE_FOUNDATION.md` | Governing compliance assumptions and boundaries. |
| `PHASE_2_MOODLE_ARCHITECTURE_REPORT.md` | Moodle platform and architecture guidance. |
| `PHASE_3_INSTRUCTIONAL_DESIGN_REPORT.md` | Course design and instructional direction. |
| `PHASE_4_MIGRATION_MVP_OPERATIONS_REPORT.md` | MVP and operating model planning. |
| `FINAL_UNIFIED_IMPLEMENTATION_BLUEPRINT.md` | Cross-phase implementation blueprint. |
| `PHASE_5_BUILD_SPEC_PACKET/` | Build-ready source specifications for staging. |

## Prototype Build 1 Boundary

Prototype Build 1 is limited to certificate gate proof of concept. It does not create final lesson content, production Moodle configuration, custom Moodle plugins, final certificate wording, or CDPH-approved certificate issuance.
