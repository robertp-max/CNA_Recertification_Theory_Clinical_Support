# Generated Survey Reviewer Script

Status: Draft / Pending Approval. Generated Moodle MVP implementation artifact. Reviewer-facing orientation. Read-only access only.

## Purpose
Orient a regulator/surveyor or compliance reviewer to the self-hosted Moodle MVP so they can verify structure, completion evidence, assessment integrity, and certificate controls without edit rights.

## Reviewer posture statement (read at start)
"This is a self-hosted Moodle learning environment in a pre-approval, survey-readiness state. No continuing-education certificates are issued until regulatory approval. You have read-only access. All examples are fictional and contain no protected health information."

## Guided walkthrough
1. Login + role: reviewer logs in with a temporary credential; confirm read-only (no edit icons, no grade changes). (Test RV-01)
2. Course catalog: show CNA (1 course, 12 units), RCFE (9 courses / 27 hours), BRN (1 course, 10 modules / 30 contact hours).
3. Structure: open one CNA unit, one RCFE course, one BRN module; show the standard activity set and timing expectations.
4. Gating: demonstrate content locked until prerequisite complete and quiz-fail blocking completion. (Tests CG-01, QZ-01, QZ-02)
5. Completion evidence: show activity-completion and course-completion reports. (Test RP-01)
6. Assessment: show quiz attempts retained including failed attempts; confirm no answer key is exposed to learners. (Test QZ-03)
7. Certificate control: show certificate issuance is blocked pre-approval and sample is watermarked NOT VALID FOR CE CREDIT. (Test CT-01)
8. No-PHI: show learner warnings/attestations; confirm fictional scenarios. (Test PH-01)
9. Exports: provide the reviewer export bundle (completion, grades, logs, config report).

## Reviewer must NOT
- edit content, change grades, alter completion, issue certificates, or view unrelated user PII beyond scope.

## Closeout
Deactivate reviewer credential after the session; log access; retain export bundle in the evidence location.
