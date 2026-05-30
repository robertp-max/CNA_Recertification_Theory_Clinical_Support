# App Location Map: Modules 0 and 1

## Dashboard / Global

| app.location | Purpose | Source |
|---|---|---|
| `dashboard.hero` | Orientation welcome and course-purpose entry point. | Module 0 learner intro and Lesson 0.1 |
| `dashboard.required_modules` | Required theory module list and progress. | Module 0 Lesson 0.4 |
| `dashboard.optional_clinical_support` | Optional Clinical Support entry marked optional/non-credit/non-gating. | Module 0 Lessons 0.1 and 0.4 |
| `certificate.gate.status` | Identity, online cap, PHI acknowledgement, orientation completion, module completion status. Certificate production remains disabled. | Module 0 Lessons 0.2, 0.3, 0.5; Module 1 metadata |
| `final.assessment.splash` | Future final exam entry should remain separate from M0/M1. Preserve final exam question flags outside this assignment. | Global guardrail, not M0/M1 content |
| `clinical.unit01.overview` | Optional Clinical Support boundary reminder only, if surfaced near dashboard/course navigation. | Module 0 optional clinical support language |

## Module 0

| app.location | Suggested Card / UI Role | Gate / Review Notes |
|---|---|---|
| `modules.m0.overview` | Module title, estimated time, objectives. | Required orientation module. |
| `modules.m0.l1.c01` | Welcome to CNA Continuing Education Course. | Administrative/compliance content only. |
| `modules.m0.l1.c02` | Who this course is for. | Avoid adding eligibility promises beyond source. |
| `modules.m0.l1.c03` | How the course works. | Clearly distinguish required theory from optional clinical support. |
| `modules.m0.l2.c01` | Partial California CNA renewal credit disclosure. | Must include 48-hour requirement and 24-hour online cap. |
| `modules.m0.l2.c02` | What this course does not provide. | Not full renewal, not clinical hours, not hands-on competency validation. |
| `modules.m0.l2.c03_ack` | Online CE cap acknowledgement. | Required gate evidence, timestamp recommended. |
| `modules.m0.l3.c01` | Why identity is confirmed. | Do not request DOB, SSN, uploads, or PHI. |
| `modules.m0.l3.c02_form` | Legal name and CNA certificate number fields. | Identity evidence only; no certificate production. |
| `modules.m0.l4.c01` | Course dashboard layout. | Required modules versus optional support. |
| `modules.m0.l4.c02` | Active participation tracking. | Use neutral compliance language. |
| `modules.m0.l5.c01_ack` | No-PHI policy acknowledgement. | Required gate evidence. |
| `modules.m0.l5.c02_gate` | Final orientation confirmation. | Unlocks Module 1 when complete. |

## Module 1

| app.location | Suggested Card / UI Role | Gate / Review Notes |
|---|---|---|
| `modules.m1.overview` | Module intro, estimated time, objectives, SME/source-review banner. | Preserve all-content SME/source-review flag. |
| `modules.m1.l1.c01` | Healthcare-associated infections in LTC. | SME/source review required. |
| `modules.m1.l1.c02` | CNA role in infection control. | SME/source review required. |
| `modules.m1.l1.c03` | Why LTC is different: resident risk factors. | SME/source review required. |
| `modules.m1.l2.c01` | Six links in the chain of infection. | SME/source review required. |
| `modules.m1.l2.c02` | Breaking the chain. | SME/source review required. |
| `modules.m1.l2.c02a` | Chain matching interaction. | Text alternative required. SME/source review required. |
| `modules.m1.l2.c03_kc` | Knowledge check: most effective daily prevention practice. | SME/source review required. |
| `modules.m1.l3.c01` | WHO 5 Moments for Hand Hygiene. | SME/source review required. |
| `modules.m1.l3.c02` | Handwashing versus sanitizer. | SME/source review required. |
| `modules.m1.l3.c03_kc` | Scenario: bowel movement/glove removal hand hygiene. | SME/source review required. |
| `modules.m1.l4.c01` | Standard precautions. | SME/source review required. |
| `modules.m1.l4.c02a` | PPE selection guide/scenario. | SME/source review required; facility-policy language may be needed. |
| `modules.m1.l4.c03` | Donning and doffing order. | SME/source review required. |
| `modules.m1.l4.c04_kc` | Knowledge check: first PPE item removed. | SME/source review required. |
| `modules.m1.l5.c01` | Common signs of infection. | SME/source review required; CNA observes/reports. |
| `modules.m1.l5.c02` | What, when, and how to report. | SME/source review required; licensed nurse assesses. |
| `modules.m1.l5.c03_kc` | Scenario: new confusion/agitation. | Fictional example only. SME/source review required. |
| `modules.m1.l6.c01` | Environmental cleaning principles. | SME/source review required. |
| `modules.m1.l6.c02` | Safe linen handling. | SME/source review required. |
| `modules.m1.l6.c03` | Sharps and waste. | SME/source review required. |
| `modules.m1.l6.c04_kc` | Knowledge check: soiled linen handling. | SME/source review required. |
| `modules.m1.quiz.splash` | Module quiz instructions. | Quiz unlocks after six lessons; pass threshold 80%. |
| `modules.m1.quiz.results` | Module quiz result and remediation. | Passing Module 1 gates Module 2. |
