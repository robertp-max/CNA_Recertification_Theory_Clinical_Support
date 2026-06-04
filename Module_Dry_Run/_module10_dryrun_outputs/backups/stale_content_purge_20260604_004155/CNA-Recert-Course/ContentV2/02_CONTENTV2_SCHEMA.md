# ContentV2 Schema

Canonical JSON: `data/courseContentV2.json`
Schema: `data/courseContentV2.schema.json`
TypeScript export: `data/courseContentV2.ts`

Every card includes: module_id, module_title, lesson_id, lesson_title, card_id, card_type, app.location, display title, learner-facing content, learning goal, CNA practice example, why it matters, key terms, completion condition, narration script, transcript text, estimated narration seconds, estimated word count, media prompt placeholder, source reference, status, SME review flag, and compliance review flag.

App locations use the locked pattern such as `module.m01.lesson.l01.card.c01_overview`, `module.m01.assessment.a00_splash`, `course.final.splash`, `certificate.gate.status`, and `clinical.hub.overview`.
