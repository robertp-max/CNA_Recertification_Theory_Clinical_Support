# App Location Map

| app.location | Source Path | Source Section | Implementation Suggestion | Gate/Credit Behavior |
|---|---|---|---|---|
| `dashboard.hero` | `CNA-Recert-Course/Content/theory/modules/29_THEORY_MODULE_07_REVIEW_FINAL_EXAM_AFFIDAVIT_FULL.md` | Learner intro copy | Show course completion trajectory and remaining gate status. | Informational only. |
| `modules.m7.overview` | Same as above | Module overview and objectives | Module 7 landing summary. | Required module content. |
| `modules.m7.l1.c01` | Same as above | Screen 7.1.1 Module 1 Review | Infection control review card. Preserve SME/source-review note. | Required; certificate gate content view. |
| `modules.m7.l1.c02` | Same as above | Screen 7.1.2 Module 2 Review | Resident rights and abuse prevention review card. | Required; certificate gate content view. |
| `modules.m7.l1.c03` | Same as above | Screen 7.1.3 Module 3 Review | Dementia, communication, cultural respect review card. | Required; certificate gate content view. |
| `modules.m7.l2.c01` | Same as above | Screen 7.2.1 Module 4 Review | Mobility, falls, workplace safety review card. | Required; certificate gate content view. |
| `modules.m7.l2.c02` | Same as above | Screen 7.2.2 Module 5 Review | Nutrition, skin integrity, vital signs review card. Preserve skin integrity SME/source-review note. | Required; certificate gate content view. |
| `modules.m7.l2.c03` | Same as above | Screen 7.2.3 Module 6 Review | Documentation, change of condition, scope review card. | Required; certificate gate content view. |
| `final.assessment.splash` | Same as above | Lesson 7.3 final exam instructions | Rules, attempts, timer, pass threshold, integrity notice. No answer key. | Required before exam. |
| `final.assessment.quiz` | `CNA-Recert-Course/Content/theory/exam/30_FINAL_EXAM_POOL_50_COMPLETE.md` | Q01-Q50 | Server-side random draw from protected bank. | Required; pass at 80%. |
| `final.assessment.result` | Same as above | Exam pass/fail metadata | Pass/fail, attempt count, next available step. | Gates affidavit access. |
| `admin.examBank.protected` | Same as above and `CNA-Recert-Course/Content/csv/31_QUIZ_BANK_MASTER_COMPLETE.csv` | Q01-Q50 with answers/rationales | Admin-only question bank/import tooling. | Never learner-facing. |
| `certificate.gate.affidavit` | `CNA-Recert-Course/Content/theory/modules/29_THEORY_MODULE_07_REVIEW_FINAL_EXAM_AFFIDAVIT_FULL.md` | Lesson 7.4 | Affidavit flow after final exam pass. Requires approved legal wording before production. | Required gate, but production disabled. |
| `certificate.gate.status` | Same as above | Lesson 7.5 | Gate checklist: modules, quizzes, final, active time, affidavit. | Required status; do not generate certificate. |
| `certificate.gate.disabled` | Same as above | Certificate status/metadata | Explicit disabled state until coordinator enables certificate production. | No certificate output. |
| `certificate.nextSteps` | Same as above | Screen 7.5.3 | Renewal next steps with placeholders resolved by approved policy only. | Informational. |
| `clinical.unit01.overview` | `CNA-Recert-Course/Content/clinical-support/32_CLINICAL_SUPPORT_FULL_CONTENT.md` | Unit 1 | Optional support orientation and global disclaimer. | Optional, non-credit, non-gating. |
| `clinical.unit02.skillsMenu` | Same as above | Unit 2 | Skills refresh menu; each topic can map to `clinical.unit02.skillNN`. | Optional, non-credit, non-gating. |
| `clinical.unit03.scheduling` | Same as above | Unit 3 | Employer-dependent scheduling guidance. | Optional, non-credit, non-gating. |
| `clinical.unit04.confidence` | Same as above and confidence-check file | Unit 4 / Checks 01-21 | Self-rating confidence checks. | Optional, not graded, not certificate-gated. |
| `clinical.confidence.c01` through `clinical.confidence.c21` | `CNA-Recert-Course/Content/clinical-support/confidence-checks/33_OPTIONAL_CLINICAL_CONFIDENCE_CHECKS_COMPLETE.md` | Confidence Checks 01-21 | Individual optional check cards/forms. | Optional; do not store as CE evidence. |
| `clinical.unit05.documentationPractice` | `CNA-Recert-Course/Content/clinical-support/32_CLINICAL_SUPPORT_FULL_CONTENT.md` | Unit 5 | Practice documentation templates with no-PHI warning. | Optional; no upload required. |
| `clinical.unit06.preceptorWorkflow` | Same as above | Unit 6 | RN/preceptor support workflow and employer-only sample form. | Optional; not clinical-hour evidence. |
| `clinical.unit07.help` | Same as above | Unit 7 | Help path and support follow-up. | Optional, post-completion reference. |
