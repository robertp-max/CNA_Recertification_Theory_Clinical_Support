# Generated Remediation Rules

Status: Draft / Pending Approval. Generated Moodle MVP implementation artifact. SME review required.

## Principle
A failing assessment result blocks completion and the next gated activity. Remediation directs the learner back to the relevant content before re-attempting, supporting genuine mastery (not answer memorization).

## Rules
1. Retakes allowed: learners may re-attempt a failed quiz. Grading method "highest grade" by default (configurable).
2. Pre-attempt remediation: on a failed attempt, display feedback directing the learner to review the specific unit/module content before re-attempting.
3. Optional attempt cap: after a configurable number of failed attempts (e.g., 3), require a remediation checkpoint (re-view content + acknowledge) before further attempts.
4. Retained evidence: all attempts (including failed) are retained and exportable (survey evidence; test QZ-03).
5. No bypass: manual override must not be used to pass a learner who has not met the passing threshold for a required CE assessment. Any override is documented (who/when/why) and restricted to Manager/Admin.
6. Final/Capstone: the same rules apply; the final/capstone remains gated behind full content completion (tests FA-01, QZ-01, QZ-02).
7. Support: persistent failure triggers a support/SME outreach option (role-based), not an automatic pass.

## Pass thresholds (defaults; confirm with SME/regulator)
- CNA unit/Final: 80%. RCFE final: 70%. BRN module/Capstone: 80%.
