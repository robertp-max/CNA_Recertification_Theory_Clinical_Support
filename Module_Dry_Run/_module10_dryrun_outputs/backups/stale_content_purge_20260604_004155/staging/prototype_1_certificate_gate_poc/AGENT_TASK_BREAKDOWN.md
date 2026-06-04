# Agent Task Breakdown

Use small parallel batches. One agent handles one narrow job. No agent should edit more than 1-3 files.

## Global Rules

- Do not change compliance meaning.
- Do not change certificate gate logic.
- Do not change required vs optional separation.
- Do not generate course content.
- Do not configure production.
- Do not touch learner data, PHI, credentials, certificates, or audit evidence.
- Read one document at a time when possible.
- Avoid large bundled file reads because prior shell reads failed with a Windows sandbox spawn error.

## Batch 1 - Root And Scaffold Docs

| Agent | Files To Inspect | Exact Task | Do Not Change | Expected Output | Risk Flag |
|---|---|---|---|---|---|
| Agent 1 - Root README Cleanup | `README.md` | Normalize headings, blank lines, and markdown tables. | Compliance rules, certificate gate logic, course scope. | Formatting cleanup notes or narrow patch. | Read one file only. |
| Agent 2 - Root Governance Docs Cleanup | `REPOSITORY_STRUCTURE.md`, `BUILD_READINESS_STATUS.md`, `NEXT_BUILD_STEP.md` | Check formatting consistency and next-step alignment. | Build status meaning or staging scope. | Cleanup notes or narrow patch. | Max 3 files. |
| Agent 3 - Prototype README Build Plan Cleanup | `staging/prototype_1_certificate_gate_poc/README.md`, `staging/prototype_1_certificate_gate_poc/PROTOTYPE_1_BUILD_PLAN.md` | Normalize markdown layout and table readability. | Prototype Build 1 scope. | Formatting issue list or narrow patch. | Avoid expanding content. |

## Batch 2 - Moodle Build And Gate Docs

| Agent | Files To Inspect | Exact Task | Do Not Change | Expected Output | Risk Flag |
|---|---|---|---|---|---|
| Agent 4 - Moodle Runbook Review | `staging/prototype_1_certificate_gate_poc/MOODLE_STAGING_BUILD_STEPS.md`, `staging/prototype_1_certificate_gate_poc/MOODLE_ADMIN_EXECUTION_RUNBOOK.md` | Compare for staging execution clarity and formatting. | Production/custom-plugin boundaries. | Gaps, duplicate instructions, or narrow patch. | Inspect one file at a time. |
| Agent 5 - Certificate Gate Config Review | `staging/prototype_1_certificate_gate_poc/CERTIFICATE_GATE_POC_CONFIG.md`, `staging/prototype_1_certificate_gate_poc/MOODLE_SETTINGS_MAP.md` | Verify certificate gate consistency. | Gate requirements. | Mismatch list or narrow patch. | Compliance-sensitive. |
| Agent 6 - Active-Time Test Plan Review | `staging/prototype_1_certificate_gate_poc/ACTIVE_TIME_POC_TEST_PLAN.md` | Check formatting and unvalidated-tool language. | Active-time evidence standard. | Cleanup notes or narrow patch. | Moodle logs must remain insufficient alone. |

## Batch 3 - Optional Clinical And QA Docs

| Agent | Files To Inspect | Exact Task | Do Not Change | Expected Output | Risk Flag |
|---|---|---|---|---|---|
| Agent 7 - Required Optional Separation Review | `staging/prototype_1_certificate_gate_poc/REQUIRED_OPTIONAL_SEPARATION_CHECK.md` | Verify required vs optional separation language. | Optional non-gating status. | Risk findings or narrow patch. | High compliance impact. |
| Agent 8 - Optional Clinical Hub Review | `staging/prototype_1_certificate_gate_poc/OPTIONAL_CLINICAL_HUB_STUB_SPEC.md` | Review wording for support-only status. | No clinical-hour credit without CDPH written approval. | Wording risk list or narrow patch. | Do not make optional items required. |
| Agent 9 - QA Tracker And Defect Review | `staging/prototype_1_certificate_gate_poc/QA_EXECUTION_TRACKER.md`, `staging/prototype_1_certificate_gate_poc/DEFECT_LOG.md`, `staging/prototype_1_certificate_gate_poc/TEST_LEARNER_MATRIX.md` | Confirm QA tests map to learner matrix and defect logging. | Tests or expected outcomes. | Coverage gaps or narrow patch. | Max 3 files. |

## Batch 4 - Hygiene And Readiness

| Agent | Files To Inspect | Exact Task | Do Not Change | Expected Output | Risk Flag |
|---|---|---|---|---|---|
| Agent 10 - CSV Consistency Review | `.csv` files only, one per pass | Check headers and format consistency. | Learner data or evidence. | CSV inventory and issues. | Do not inspect PHI-like data if present. |
| Agent 11 - Security/Hygiene Review | `SECURITY.md`, `.gitignore`, `WORKFLOW.md` | Confirm exclusions and repo hygiene rules. | Security boundaries. | Missing ignore/security items or narrow patch. | Private approvals must remain excluded. |
| Agent 12 - Final Readiness Summary | Agent outputs from Agents 1-11 only | Produce final readiness decision. | Repository files. | Ready/not ready, blockers, next action. | Depends on prior agents. |
