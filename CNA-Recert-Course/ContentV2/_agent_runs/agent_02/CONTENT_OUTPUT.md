# Content Output: Modules 0 and 1 V2 Guidance

## Conversion Stance

Use these notes as coordinator guidance only. Do not create canonical `ContentV2` files from this scratch output without source/SME review where flagged. Module 0 can be converted as compliance/navigation content. Module 1 must retain an all-content SME/source-review flag before production use.

## Module 0: Orientation and Compliance Boundaries

Suggested V2 structure: short required orientation flow, 5 lessons, 12 primary cards, 4 required acknowledgement/check interactions. Keep Module 0 administrative and compliance-focused; do not add clinical teaching.

| Lesson | Suggested Cards | App Locations | Guidance |
|---|---|---|---|
| M0 overview | Welcome / partial-credit frame | `dashboard.hero`, `modules.m0.overview` | State that the course provides up to 12 hours of online theory CE and is partial California CNA renewal credit only. Avoid any promise of full renewal completion. |
| 0.1 Welcome and Course Purpose | Welcome, who this course is for, how the course works | `modules.m0.l1.c01`, `modules.m0.l1.c02`, `modules.m0.l1.c03` | Present 7 required theory modules, Module 0 orientation, final review/exam, and optional clinical support. Keep "required" and "optional" visually distinct. |
| 0.2 What This Course Covers and Does Not Cover | Partial credit disclosure, exclusions, online CE cap acknowledgement | `modules.m0.l2.c01`, `modules.m0.l2.c02`, `modules.m0.l2.c03_ack` | Required acknowledgement: learner understands 48-hour renewal requirement, 24-hour online cap, and this 12-hour course is partial credit only. |
| 0.3 Identity Confirmation | Why identity is confirmed, legal name/CNA certificate number fields | `modules.m0.l3.c01`, `modules.m0.l3.c02_form` | Limit identity fields to legal name and CNA certificate number. Do not request DOB, SSN, uploads, or patient/resident identifiers. |
| 0.4 Navigation and Progress | Course layout, active participation tracking | `modules.m0.l4.c01`, `modules.m0.l4.c02` | Explain required theory modules versus optional clinical support. Active-time language should be neutral: tracking evidence of engagement, not discipline. |
| 0.5 Acknowledgement and Compliance Check | No-PHI policy, final orientation confirmation | `modules.m0.l5.c01_ack`, `modules.m0.l5.c02_gate` | Required acknowledgement: no real patient/resident PHI in any activity. Final check unlocks Module 1. |

Module 0 interactions:

| Interaction | App Location | Type | Coordinator Note |
|---|---|---|---|
| Online cap acknowledgement | `modules.m0.l2.c03_ack` | Required checkbox / acknowledgement | Store timestamp as gate evidence. |
| Identity confirmation | `certificate.gate.status` | Required profile/status field group | Certificate production remains disabled; this is gate-status evidence only. |
| PHI acknowledgement | `modules.m0.l5.c01_ack` | Required checkbox / acknowledgement | Must explicitly prohibit real patient/resident names, room numbers, MRNs, DOBs, and other identifiers. |
| Final orientation check | `modules.m0.l5.c02_gate` | Required multi-item confirmation | Unlocks Module 1 only after required items are complete. |

## Module 1: Infection Control and Standard Precautions

Suggested V2 structure: 6 required lessons, 15 primary cards, 3 interaction cards, 6 knowledge checks, 1 module quiz. Every Module 1 lesson/card should carry the SME/source-review flag until cleared.

| Lesson | Suggested Cards | App Locations | Guidance |
|---|---|---|---|
| M1 overview | Module intro, objectives, SME flag | `modules.m1.overview` | Preserve source warning: no dedicated infection control NATP module; content uses scattered NATP references, draft legacy sources, and standard CNA principles. |
| 1.1 Why Infection Control Matters in LTC | HAIs in LTC, CNA role, LTC risk factors | `modules.m1.l1.c01`, `modules.m1.l1.c02`, `modules.m1.l1.c03` | Focus on resident vulnerability, close contact, shared spaces, and CNA prevention/reporting role. Mark all as SME/source review required. |
| 1.2 Chain of Infection | Six links, breaking the chain, matching/check card | `modules.m1.l2.c01`, `modules.m1.l2.c02`, `modules.m1.l2.c03_kc` | The chain matching activity needs a text alternative. Hand hygiene as key break point requires SME/source validation. |
| 1.3 Hand Hygiene | WHO 5 Moments, soap/water versus sanitizer, body-fluid scenario | `modules.m1.l3.c01`, `modules.m1.l3.c02`, `modules.m1.l3.c03_kc` | Verify exact sanitizer limits, C. difficile/norovirus wording, and body-fluid handwashing guidance with SME/source review. |
| 1.4 PPE | Standard precautions, PPE task guide, donning/doffing, removal check | `modules.m1.l4.c01`, `modules.m1.l4.c02a`, `modules.m1.l4.c03`, `modules.m1.l4.c04_kc` | PPE selection and don/doff order are high-risk accuracy items. Keep facility-policy language where appropriate. |
| 1.5 Recognizing and Reporting Infection Signs | Common signs, reporting table, confusion scenario | `modules.m1.l5.c01`, `modules.m1.l5.c02`, `modules.m1.l5.c03_kc` | Maintain CNA scope: CNA observes and reports; licensed nurse assesses. Fictional examples only. |
| 1.6 Environmental Cleaning and Safe Practices | Cleaning principles, safe linen handling, sharps/waste, linen check | `modules.m1.l6.c01`, `modules.m1.l6.c02`, `modules.m1.l6.c03`, `modules.m1.l6.c04_kc` | Verify cleaning sequence, disinfectant contact-time phrasing, linen handling, and sharps wording with SME/source review. |

Module 1 interactions:

| Interaction | App Location | Type | Coordinator Note |
|---|---|---|---|
| Chain of Infection Matching | `modules.m1.l2.c02a` | Drag/drop or text matching | Must include non-drag text alternative for accessibility/mobile. |
| PPE Selection Scenario | `modules.m1.l4.c02a` | Scenario MC / select all | Gloves required for perineal care; gown if splash risk. SME/source review required. |
| Reporting Priority | `modules.m1.l5.c03_kc` | Scenario MC | Use fictional resident such as "Mrs. J"; report new confusion immediately to licensed nurse. SME/source review required. |

## Cross-Module Guidance

- Keep Module 0 as a certificate-gate evidence flow, but do not enable certificate production or draft certificate wording.
- Keep Module 1 required and gated by Module 0 completion.
- Optional Clinical Support references may appear in dashboard/navigation only and must remain optional, non-credit, non-gating, not clinical-hour credit, and not a certificate gate.
- Normalize source encoding artifacts during canonical merge. The reviewed sources display mojibake in headings, arrows, warnings, and check/cross symbols.
