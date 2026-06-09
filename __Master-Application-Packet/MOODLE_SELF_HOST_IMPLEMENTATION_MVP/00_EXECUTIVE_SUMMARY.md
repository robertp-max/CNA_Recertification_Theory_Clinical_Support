# 00 - Executive Summary: Self-Hosted Moodle Implementation MVP

Applicant: CI Institute of Nursing, Inc.
Prepared: June 09, 2026
Status: Draft / Pending Approval (all three lanes). This package is an implementation requirement set for a self-hosted Moodle MVP. It is not a regulator submission and makes no approval claim.

## Purpose of the Moodle MVP

Provide a complete, survey-defensible, self-hosted Moodle implementation requirement package so a Moodle administrator can build the learning environment for CI Institute of Nursing's current continuing-education application packet without guessing course names, categories, sections, activities, completion settings, restrict-access rules, quiz banks, passing scores, evidence reports, roles, review workflow, certificate controls, or backup/export requirements.

This package follows the controlling master application packet (see `FINAL_SUBMISSION_REVIEW_PACKAGE/00_MASTER_SUBMISSION_REVIEW_INDEX.md` and `00_FINAL_COURSE_ALIGNMENT_AUDIT.md`). Where a required Moodle implementation artifact was missing, it has been generated conservatively and clearly labeled "Generated Moodle MVP implementation artifact," with SME/admin review flags where content judgment is involved.

## Three lanes supported

1. CNA / CDPH CE - 12 units x 2 online CE hours = 24 online CE hours. Year 1 = U01-U06 (12 hrs); Year 2 = U07-U12 (12 hrs). Source backbone = CCCCO/NATP Modules 10-17. Online CE only; no clinical hours; no hands-on competency validation; no full 48-hour renewal claim. Draft / Pending Approval.
2. RCFE / CDSS CETP - filed packet = 9 LIC 9140 courses / 27 hours (RCFE-CETP-001 through 009). The 40-hour / 12-module program is listed only as a future, non-submitted expansion. Draft / Pending Approval.
3. BRN / CEP RN Case Management - 30 contact hours = 10 modules x 3 contact hours; 50 instructional minutes minimum per contact hour; 30 contact hours = at least 1,500 instructional minutes. Provider-approval framing (not course-by-course). Contact hours, not CEUs. Pending BRN CEP approval. No certification or scope-expansion claim. No stale 4-contact-hour language.

## What the MVP proves

- The course architecture for all three lanes can be built in Moodle exactly as filed/controlling.
- Completion gating, sequential progression, and assessment pass thresholds can be enforced.
- Seat-time / contact-hour evidence, completion evidence, grades, attempts, and logs can be captured and exported for survey review.
- Read-only external reviewer access can be provisioned without edit rights.
- Certificates can be hard-blocked until regulator approval and released only under documented approval metadata.

## What the MVP does NOT prove

- It does not prove or assert any regulator approval. All lanes are Draft / Pending Approval.
- CNA: it does not, by itself, complete all California CNA renewal requirements; it is online CE only with no clinical hours and no hands-on competency validation.
- BRN: it makes no certification claim and no scope-of-practice expansion claim; CE is measured in contact hours, not CEUs.
- RCFE: the controlling structure is the filed 9-course / 27-hour packet; the 40-hour / 12-module concept is future expansion only and is not the current submission.

## Pending-approval posture

Every learner-facing course, certificate control, and catalog statement is built in a "Pending Approval" posture. No approval numbers are invented. Where an approval number, signature, payment, reviewer credential, or regulator decision is required, the package creates a safe required field / gate / checklist item rather than fabricating data (see `98_MISSING_OR_HUMAN_VERIFICATION_ITEMS.md`).

## No certificate issuance before approval

Certificate activities are disabled before approval. An optional internal test certificate may exist only if watermarked "NOT VALID FOR CE CREDIT." Certificate release is gated behind approval metadata and an authorized role (see `06_CERTIFICATE_AND_APPROVAL_CONTROLS.md`).

## Survey-readiness posture

The build is designed to be defensible during a survey/audit: completion evidence is mapped per unit/course/module, retake history is retained, failed attempts block completion, reports/exports are defined, no PHI is permitted, and no false approval claims appear. See `08_SURVEY_READINESS_QA_TEST_PLAN.md` and `15_REVIEWER_ACCESS_AND_SURVEY_WORKFLOW.md`.

## Go / No-Go criteria (summary)

GO to build the MVP environment: all implementation artifacts in this package are present (validated). The MVP build can proceed in a non-production / pre-approval posture.

NO-GO to issue certificates or make public approval claims until: (1) regulator approval is granted and approval metadata is entered; (2) legal/privacy signoff is recorded; (3) SME quiz review is complete; (4) certificate wording is confirmed; (5) reviewer access and report/backup exports are tested. See `19_GO_LIVE_HOLD_AND_RELEASE_CRITERIA.md` and `20_POST_APPROVAL_ACTIVATION_PLAN.md`.

## Moodle version recommendation (summary)

Default recommendation: Moodle 4.5 LTS for survey-stable self-hosting and plugin compatibility. Moodle 5.2 may be considered only if all required plugins, import tools, and themes are verified compatible. Version recommendation requires final technical verification before production install. See `01_SELF_HOSTED_MOODLE_REQUIREMENTS.md`.

## Exact file list generated by this package

Root documents:
- 00_EXECUTIVE_SUMMARY.md
- 01_SELF_HOSTED_MOODLE_REQUIREMENTS.md
- 02_COURSE_ARCHITECTURE_BLUEPRINT.md
- 03_COMPLETION_AND_SURVEY_EVIDENCE_MATRIX.md
- 04_ROLE_ACCESS_AND_WORKFLOW_MATRIX.md
- 05_ASSESSMENT_AND_QUIZ_REQUIREMENTS.md
- 06_CERTIFICATE_AND_APPROVAL_CONTROLS.md
- 07_MOODLE_BUILD_CHECKLIST.md
- 08_SURVEY_READINESS_QA_TEST_PLAN.md
- 09_MOODLE_IMPORT_PACKAGE_INDEX.md
- 10_MOODLE_ADMIN_QUICK_START.md
- 11_COURSE_SHELL_BUILD_SPECIFICATIONS.md
- 12_GRADEBOOK_AND_COMPLETION_CONFIGURATION.md
- 13_REPORTING_AND_AUDIT_EXPORT_SPEC.md
- 14_DATA_RETENTION_BACKUP_AND_SECURITY_SPEC.md
- 15_REVIEWER_ACCESS_AND_SURVEY_WORKFLOW.md
- 16_NO_PHI_AND_PRIVACY_CONTROLS.md
- 17_ACCESSIBILITY_AND_MOBILE_REQUIREMENTS.md
- 18_IMPLEMENTATION_RISK_REGISTER.md
- 19_GO_LIVE_HOLD_AND_RELEASE_CRITERIA.md
- 20_POST_APPROVAL_ACTIVATION_PLAN.md
- 98_MISSING_OR_HUMAN_VERIFICATION_ITEMS.md
- 99_MOODLE_MVP_FINAL_VALIDATION.md

import_assets/: CNA/RCFE/BRN GIFT + CSV + MD quiz banks; COURSE_SHELL_NAMING_CONVENTIONS.csv; COMPLETION_RULES_IMPORT_REFERENCE.csv; GRADEBOOK_SETUP_REFERENCE.csv; RESTRICT_ACCESS_RULES_REFERENCE.csv; ROLE_MATRIX_IMPORT_REFERENCE.csv; REPORTING_EXPORT_CHECKLIST.csv; SME_REVIEW_REQUIRED_QUIZ_ITEMS.md; QUIZ_BANK_COVERAGE_AUDIT.csv; QUIZ_BANK_COVERAGE_AUDIT.md

course_shells/: CNA_COURSE_SHELL_BUILD_SPEC.md; RCFE_COURSE_SHELL_BUILD_SPEC.md; BRN_COURSE_SHELL_BUILD_SPEC.md

generated_missing_elements/: README_GENERATED_MISSING_ELEMENTS.md; GENERATED_CNA_UNIT_OBJECTIVES_AND_ACTIVITIES.md; GENERATED_RCFE_COURSE_OBJECTIVES_AND_ACTIVITIES.md; GENERATED_BRN_MODULE_OBJECTIVES_AND_ACTIVITIES.md; GENERATED_ATTESTATION_TEXTS.md; GENERATED_REMEDIATION_RULES.md; GENERATED_SURVEY_REVIEWER_SCRIPT.md; GENERATED_NO_PHI_LEARNER_WARNINGS.md; GENERATED_CERTIFICATE_GATE_COPY.md

Quiz banks generated: CNA 170, RCFE 135, BRN 150 (total 455), each in GIFT + CSV + Markdown, with coverage audit confirming minimums.
