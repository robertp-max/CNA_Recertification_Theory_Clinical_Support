# App Location Map Suggestions

These are suggested V2 app locations only. No app source was read or modified.

## Cross-Course Boundary Locations

| app.location | Suggested Use | Notes |
|---|---|---|
| `dashboard.hero` | Course status and next required theory module | Show Module 2 or Module 3 progress without claiming full CNA renewal completion. |
| `dashboard.modules.m2.status` | Module 2 tile/status | Required theory module, 120 minutes, locked until Module 1 requirement is satisfied if current rules require it. |
| `dashboard.modules.m3.status` | Module 3 tile/status | Required theory module, 120 minutes, locked until Module 2 knowledge check is passed if current rules require it. |
| `certificate.gate.status` | Course completion status | Keep certificate production disabled. Do not generate certificate wording, provider number, CDPH contact, NAC number, or affidavit language. |
| `final.assessment.splash` | Final assessment entry | Preserve existing final exam flags for Q01, Q02, Q03, Q41, and Q21/Q38 where present. |
| `clinical.unit01.overview` | Optional clinical-support reminder | Optional clinical support remains non-credit, non-gating, non-certificate, and not clinical-hour credit. |

## Module 2 Locations

| app.location | Content | Status |
|---|---|---|
| `modules.m2.overview` | Module intro, CE boundary, objectives, time | Source-ready. |
| `modules.m2.l1.c01` | What are resident rights? | Source-ready. |
| `modules.m2.l1.c02` | Rights in daily care | Source-ready. |
| `modules.m2.l1.c03` | Ombudsman and resident council check | Source-ready. |
| `modules.m2.l1.c04` | Advance directives and DNR | Source-ready, SME/scope review recommended. |
| `modules.m2.l2.c01` | Defining abuse | Source-ready. |
| `modules.m2.l2.c02` | Abuse types | Source-ready, SME/source review recommended for legal alignment. |
| `modules.m2.l2.c03` | Match the abuse type | Source-ready, must support non-drag interaction. |
| `modules.m2.l2.c04` | Neglect vs negligence | Source-ready, SME/source review recommended. |
| `modules.m2.l3.c01` | Signs and symptoms of abuse | Source-ready. |
| `modules.m2.l3.c02` | Objective vs subjective observations | Source-ready. |
| `modules.m2.l4.c01` | Mandated reporter obligations | Source-ready, legal/source review required. |
| `modules.m2.l4.c02` | Reporting decision path | Source-ready, legal/source review required. |
| `modules.m2.l4.c03` | Reporting scenario branch | Source-ready, legal/source review required. |
| `modules.m2.l5.c01` | Abuse prevention strategies | Source-ready. |
| `modules.m2.l5.c02` | Professional boundaries | Source-ready. |
| `modules.m2.l5.c03` | HIPAA and confidentiality in abuse situations | Source-ready, compliance/source review recommended. |
| `modules.m2.assessment.splash` | Knowledge check intro | Source-ready. |
| `modules.m2.assessment.q01` | Verbal abuse question | Source-ready. |
| `modules.m2.assessment.q02` | Objective observation question | Source-ready. |
| `modules.m2.assessment.q03` | Mandated reporter question | Source-ready, legal/source review required. |
| `modules.m2.assessment.q04` | Neglect question | Source-ready. |
| `modules.m2.assessment.q05` | Abuse-prevention strategy question | Source-ready. |
| `modules.m2.completion` | Completion/remediation recommendation | Source-ready, ensure gate means course-progress gate only. |

## Module 3 Locations

| app.location | Content | Status |
|---|---|---|
| `modules.m3.overview` | Module intro, objectives, time | Source-ready from available text. |
| `modules.m3.l1.c01` | Dementia vs delirium | Source-ready, SME/source review recommended for current clinical framing. |
| `modules.m3.l1.c02` | Behavioral symptoms of dementia | Source-ready. |
| `modules.m3.l1.c03` | Alzheimer's disease stages | Source-ready. |
| `modules.m3.l1.c04` | Other cognitive conditions plus repeated-question check | Source-ready, SME review recommended for scope and mental-health wording. |
| `modules.m3.l2.c01` | Core communication principles | Source-ready. |
| `modules.m3.l2.c02` | Best Friends approach | Source-ready. |
| `modules.m3.l2.c03` | Mrs. Okafor communication scenario | Blocked. Source cuts off before answer options and feedback. |
| `modules.m3.l3.c01` | Cultural sensitivity and spiritual respect | Blocked. Listed in metadata/time breakdown, but no lesson body present. |
| `modules.m3.l4.c01` | End-of-life care, grief, and hospice | Blocked. Listed in metadata/time breakdown, but no lesson body present. |
| `modules.m3.l5.c01` | Trauma-informed care and de-escalation | Blocked. Listed in metadata/time breakdown, but no lesson body present. |
| `modules.m3.assessment.splash` | Module 3 knowledge check intro | Blocked. No quiz source rows present. |
| `modules.m3.assessment.q01` through `modules.m3.assessment.q05` | Module 3 knowledge check questions | Blocked. No quiz source rows present. |
| `modules.m3.completion` | Completion/remediation recommendation | Blocked. Not present in reviewed source. |
