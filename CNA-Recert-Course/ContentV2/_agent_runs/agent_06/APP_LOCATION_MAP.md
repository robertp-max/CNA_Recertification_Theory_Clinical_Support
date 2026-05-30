# App Location Map

These are proposed adapter keys for coordinator merge planning. They are not canonical `ContentV2` files.

## Global / Dashboard

| app.location | Purpose | Notes |
|---|---|---|
| `dashboard.hero` | Course dashboard hero/status area | Should summarize online theory progress only. |
| `dashboard.progress.theory` | Required theory progress | Exclude optional clinical support. |
| `dashboard.progress.clinicalSupport` | Optional clinical support progress | Non-credit, non-gating, visually separate. |
| `dashboard.alerts.compliance` | Compliance notices | TTS planning-only, partial-credit, no clinical-hour credit reminders. |

## Modules And Lessons

| app.location | Purpose | Source anchor |
|---|---|---|
| `modules.m0.overview` | Orientation overview | TTS-0-001 to TTS-0-003 |
| `modules.m0.l1.c01` | Course welcome narration | TTS-0-001 |
| `modules.m0.l2.c01` | Navigation narration | TTS-0-002 |
| `modules.m0.l3.c01` | Compliance disclaimers narration | TTS-0-003 |
| `modules.m1.overview` | Infection control overview | Module 1 SME/source-review required |
| `modules.m1.l1.c01` | Chain of infection narration | TTS-1-001 |
| `modules.m1.l1.c02a` | Chain of infection media/check placeholder | Use as a non-audio placeholder key only; Module 1 SME/source-review required. |
| `modules.m1.l2.c01` | Hand hygiene narration | TTS-1-002 |
| `modules.m1.l3.c01` | Standard Precautions narration | TTS-1-003 |
| `modules.m1.l4.c01` | PPE donning/doffing narration | TTS-1-004 |
| `modules.m1.l5.c01` | Transmission-Based Precautions narration | TTS-1-005 |
| `modules.m2.overview` | Resident rights overview | TTS-2 series |
| `modules.m2.l1.c01` | Resident rights foundation narration | TTS-2-001 |
| `modules.m2.l2.c01` | Abuse and neglect types narration | TTS-2-002 |
| `modules.m2.l3.c01` | Abuse signs narration | TTS-2-003 |
| `modules.m2.l4.c01` | Mandated reporter narration | TTS-2-004 |
| `modules.m2.l5.c01` | Prevention and boundaries narration | TTS-2-005 |
| `modules.m3.overview` | Dementia and communication overview | TTS-3 series |
| `modules.m3.l1.c01` | Understanding dementia narration | TTS-3-001 |
| `modules.m3.l2.c01` | Communication strategies narration | TTS-3-002 |
| `modules.m3.l3.c01` | Cultural and spiritual respect narration | TTS-3-003 |
| `modules.m3.l4.c01` | End-of-life care narration | TTS-3-004 |
| `modules.m3.l5.c01` | Trauma-informed care narration | TTS-3-005 |
| `modules.m4.overview` | Mobility and safety overview | TTS-4 series |
| `modules.m4.l1.c01` | Body mechanics narration | TTS-4-001 |
| `modules.m4.l2.c01` | Transfers and ambulation narration | TTS-4-002 |
| `modules.m4.l3.c01` | ROM and restorative care narration | TTS-4-003 |
| `modules.m4.l4.c01` | Fall prevention narration | TTS-4-004 |
| `modules.m4.l5.c01` | Emergency procedures narration | TTS-4-005 |
| `modules.m5.overview` | Nutrition, skin integrity, vital signs overview | Skin integrity SME/source-review required |
| `modules.m5.l1.c01` | Nutrition and hydration narration | TTS-5-001 |
| `modules.m5.l2.c01` | Feeding assistance narration | TTS-5-002 |
| `modules.m5.l3.c01` | Skin integrity narration | TTS-5-003 |
| `modules.m5.l4.c01` | Vital signs narration | TTS-5-004 |
| `modules.m5.l5.c01` | Monitoring/documentation narration | TTS-5-005 |
| `modules.m6.overview` | Documentation and scope overview | TTS-6 series |
| `modules.m6.l1.c01` | Objective vs subjective observations narration | TTS-6-001 |
| `modules.m6.l2.c01` | Documentation standards narration | TTS-6-002 |
| `modules.m6.l3.c01` | Change-of-condition narration | TTS-6-003 |
| `modules.m6.l4.c01` | CNA scope narration | TTS-6-004 |
| `modules.m6.l5.c01` | Professionalism/delegation narration | TTS-6-005 |

## Final / Certificate / Clinical Support

| app.location | Purpose | Notes |
|---|---|---|
| `final.assessment.splash` | Final review and exam intro | TTS-7-001. Keep exam-bank flags intact in related data. |
| `final.assessment.review` | Final review area | Required theory flow only. |
| `final.assessment.exam` | Final exam route/view | Do not alter Q01/Q02/Q03/Q41 and Q21/Q38 flags. |
| `final.affidavit.status` | Affidavit status placeholder | Do not create final affidavit wording. |
| `certificate.gate.status` | Certificate gate status placeholder | Certificate production disabled. |
| `certificate.gate.blocked` | Certificate blocked state | No certificate text or approval metadata. |
| `clinical.unit01.overview` | Optional Clinical Support overview | Optional, non-credit, non-gating. |
| `clinical.unit01.practice` | Optional practice/support card | Must not gate certificate. |
| `clinical.unit01.resources` | Optional resource card | Must not imply clinical-hour credit. |

## Adapter Validation Rules

- Every content card intended for app display should have exactly one `app.location`.
- `app.location` values should be unique and stable.
- Optional clinical support locations must be namespaced under `clinical.*` and excluded from required theory completion gates.
- Certificate locations must remain status placeholders until production authorization exists.
