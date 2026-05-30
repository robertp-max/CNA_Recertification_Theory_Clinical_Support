# App Location Map - Modules 4-6

These are suggested locations for coordinator merge planning. Verify against the canonical ContentV2 schema before merge.

| Content | Suggested `app.location` | Notes |
|---|---|---|
| Course/dashboard module progress entry for assigned set | `dashboard.hero` | Show M4-M6 progress only if the dashboard supports active module summaries. |
| Module 4 overview | `modules.m4.overview` | Required theory module; 120 minutes. |
| M4 Lesson 4.1 Body Mechanics | `modules.m4.l1.c01` to `modules.m4.l1.c02` | Concept plus quick check. |
| M4 Lesson 4.2 Transfers and Ambulation | `modules.m4.l2.c01` to `modules.m4.l2.c04` | Include two-person assist scenario. |
| M4 Lesson 4.3 ROM and Restorative Care | `modules.m4.l3.c01` to `modules.m4.l3.c03` | Keep restorative care distinct from therapy. |
| M4 Lesson 4.4 Fall Prevention | `modules.m4.l4.c01` to `modules.m4.l4.c04` | Include fall response and multi-select check. |
| M4 Lesson 4.5 Emergency Procedures | `modules.m4.l5.c01` to `modules.m4.l5.c03` | RACE/PASS, choking, disaster preparedness. |
| M4 Knowledge Check | `modules.m4.assessment.quiz` | 5 items, 80% pass. |
| Module 5 overview | `modules.m5.overview` | Required theory module; 120 minutes. |
| M5 Lesson 5.1 Nutrition and Hydration | `modules.m5.l1.c01` to `modules.m5.l1.c03` | Nutrients, hydration, modified diets. |
| M5 Lesson 5.2 Feeding and Aspiration | `modules.m5.l2.c01` to `modules.m5.l2.c03` | Include thickened-liquid scenario. |
| M5 Lesson 5.3 Skin Integrity | `modules.m5.l3.c01` to `modules.m5.l3.c04` | Preserve pressure injury SME/source-review flag. |
| M5 Lesson 5.4 Vital Signs | `modules.m5.l4.c01` to `modules.m5.l4.c04` | Use common adult ranges with SME/facility-policy caution. |
| M5 Lesson 5.5 Monitoring and Reporting | `modules.m5.l5.c01` to `modules.m5.l5.c03` | I&O, weight, BP change scenario. |
| M5 Knowledge Check | `modules.m5.assessment.quiz` | 5 items, 80% pass. |
| Module 6 overview | `modules.m6.overview` | Required theory module; 90 minutes. |
| M6 Lesson 6.1 Observation | `modules.m6.l1.c01` to `modules.m6.l1.c02` | Objective vs subjective check. |
| M6 Lesson 6.2 Documentation | `modules.m6.l2.c01` to `modules.m6.l2.c03` | Legal documentation rules and scenario. |
| M6 Lesson 6.3 Change of Condition | `modules.m6.l3.c01` to `modules.m6.l3.c03` | Include SBAR reporting and immediate-report check. |
| M6 Lesson 6.4 Scope of Practice | `modules.m6.l4.c01` to `modules.m6.l4.c03` | Tasks CNA can/cannot do; sterile dressing scenario. |
| M6 Lesson 6.5 Professionalism and Delegation | `modules.m6.l5.c01` to `modules.m6.l5.c02` | Delegation five rights. |
| M6 Knowledge Check | `modules.m6.assessment.quiz` | 5 items, 80% pass. |
| Final assessment entry point | `final.assessment.splash` | Preserve existing final exam flags Q01, Q02, Q03, Q41, and Q21/Q38 where present. |
| Certificate status messaging | `certificate.gate.status` | Certificate production stays disabled; do not add certificate wording or approval metadata. |
| Optional clinical support overview | `clinical.unit01.overview` | Optional, non-credit, non-gating, not clinical-hour credit. Do not gate theory completion or certificate status on it. |
