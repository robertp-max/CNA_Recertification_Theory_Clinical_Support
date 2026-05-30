# App Location Map Suggestions

These are mapping suggestions only. They are not route, app source, or ContentV2 implementation changes.

| app.location | Source/control basis | Suggested use | Merge caution |
|---|---|---|---|
| `dashboard.hero` | `35_CONTENT_PACKAGE_INDEX_UPDATED.md`; `CONTENT_PACKAGE_QA_REPORT.md` | Course identity and boundary summary: 12-hour theory CE, partial California CNA online CE, no PHI, optional clinical support separate. | Do not imply full renewal completion or clinical-hour credit. |
| `dashboard.sourceStatus` | `SOURCE_TITLE_VERIFICATION_PASS.md`; `CONTENT_PACKAGE_RISK_REGISTER.md` | Internal/admin source status panel for confirmed NATP Module 10-17 titles and open source gaps. | Do not show unresolved internal review language to learners unless compliance wants it exposed. |
| `dashboard.readiness` | `CONTENT_PACKAGE_BUILD_READINESS.md` | Internal/admin readiness state: staging allowed, production blocked. | Certificate must remain disabled. |
| `modules.m0.overview` | Content listing File 04; index File 00-23 summary | Module 0 orientation overview. | Do not alter 30-minute allocation. |
| `modules.m1.overview` | Content listing File 05; QA/Risk R01 | Module 1 infection-control overview. | Preserve SME/source-review flag until confirmed approved source and SME signoff. |
| `modules.m1.l1.c02a` | QA/Risk R01; exam flag references | Infection-control lesson/card area where source metadata should attach. | Do not remove or hide internal Module 1 flag in source metadata. |
| `modules.m2.overview` | Index File 24 | Module 2 overview: resident rights and abuse prevention. | Confirm source labels use NATP Module 17, 13, and 15 as stated by index. |
| `modules.m3.overview` | Index File 25 | Module 3 overview: dementia, communication, cultural respect. | Maintain fictional/de-identified examples only. |
| `modules.m4.overview` | Index File 26 | Module 4 overview: mobility, falls, workplace safety. | Keep emergency and restorative source labels aligned with verified NATP titles. |
| `modules.m5.overview` | Index File 27; `SOURCE_TITLE_VERIFICATION_PASS.md`; Risk R02 | Module 5 overview: nutrition, skin integrity, vital signs. | Skin integrity / pressure injury is conditional and must keep SME/source-review flag. |
| `modules.m5.l3.c01` | Risk R02; source-title verification skin gap | Skin integrity / pressure injury card cluster. | Do not finalize for production until confirmed source exists. |
| `modules.m6.overview` | Index File 28 | Module 6 overview: documentation, change of condition, scope. | Continue no-PHI and scope-of-practice boundaries. |
| `modules.m7.overview` | `TIME_ALLOCATION_CORRECTION_NOTICE.md`; Index File 29 | Module 7 overview and 30-minute review/exam/affidavit structure. | Keep 30-minute allocation, not 90 minutes. |
| `final.assessment.splash` | Index File 29; QA report exam checks | Final exam instructions: 25 random questions from 50, 80% pass, 2 attempts, 20-minute exam activity. | Preserve Q01, Q02, Q03, Q41, Q21, and Q38 review flags in metadata. |
| `final.assessment.q01` | QA report Check 7; risk R01 | Final exam Q01 metadata. | Preserve Module 1 SME/source-review flag. |
| `final.assessment.q02` | QA report Check 7; risk R01 | Final exam Q02 metadata. | Preserve Module 1 SME/source-review flag. |
| `final.assessment.q03` | QA report Check 7; risk R01 | Final exam Q03 metadata. | Preserve Module 1 SME/source-review flag. |
| `final.assessment.q21` | `SOURCE_TITLE_VERIFICATION_PASS.md`; QA report Check 7; risk R02 | Final exam Q21 metadata. | Preserve skin integrity SME/source-review flag. |
| `final.assessment.q38` | `SOURCE_TITLE_VERIFICATION_PASS.md`; QA report Check 7; risk R02 | Final exam Q38 metadata. | Preserve skin integrity SME/source-review flag. |
| `final.assessment.q41` | QA report Check 7; risk R01 | Final exam Q41 metadata. | Preserve Module 1 SME/source-review flag. |
| `certificate.gate.status` | `CONTENT_PACKAGE_BUILD_READINESS.md`; Risk R03, R04, R08 | Certificate gate/admin status. | Production certificate disabled; no fabricated NAC#, provider number, CDPH contact, or certificate wording. |
| `certificate.affidavit.review` | Index File 29; Risk R03 | Internal legal/compliance review state for affidavit language. | Do not publish "under penalty of perjury" attestation without legal/CDPH review. |
| `clinical.unit01.overview` | Index File 32; QA required/optional check | Optional clinical support Unit 1 overview. | Optional, non-credit, non-gating, not clinical-hour credit, not certificate gate. |
| `clinical.unit03.scheduling` | QA placeholder check; Risk R05 | Optional clinical support scheduling guidance. | Replace CDPH/contact placeholders only with verified real information; do not fabricate. |
| `clinical.unit06.signoff` | Risk R09; build readiness compliance review | Optional RN/preceptor signoff support. | Must not become clinical-hour documentation or certificate gate. |
| `clinical.unit07.help` | QA placeholder check; Risk R05 | Optional support/help path. | CDPH contact placeholder blocks production. |
| `narration.planning.index` | Index File 34; QA TTS check; Risk R06 | TTS script planning metadata. | Planning only. Do not generate audio/media or imply TTS authorization. |
| `admin.sourceCopy.manifest` | This audit; source-verification and QA controls | Internal manifest for exact source path, status class, precedence, and flags. | Should include path casing rule: `CNA-Recert-Course/Content`, not lowercase `content`. |
