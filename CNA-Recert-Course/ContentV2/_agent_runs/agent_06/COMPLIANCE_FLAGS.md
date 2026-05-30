# Compliance Flags

## Preserved Compliance Boundaries

- TTS scripts are planning artifacts only. Do not record, synthesize, deploy, or link audio without explicit authorization and compliance review.
- No PHI. Use fictional/de-identified examples only.
- Do not request uploads, resident identifiers, learner medical information, facility records, or real clinical documentation.
- Optional Clinical Support is optional, non-credit, non-gating, not clinical-hour credit, and never a certificate gate.
- Certificate production stays disabled.
- Do not fabricate NAC numbers, CDPH contacts, provider numbers, approval metadata, affidavit wording, or certificate wording.
- Online theory is partial credit only. Do not imply full CNA renewal completion.

## App/Schema Compliance Risks

| Risk | Required control |
|---|---|
| Optional support accidentally counted in progress or certificate gate | Namespace optional support under `clinical.*`; exclude it from required completion and certificate gate calculations. |
| TTS fields treated as production-ready media | Add `status: Draft` or `mediaProductionStatus: Not authorized` to narration records. |
| Certificate UI appears enabled | Use `certificate.gate.status` as disabled/status-only placeholder until approval. |
| Final exam flags lost during adapter transform | Add schema validation for flagged question IDs Q01/Q02/Q03/Q41 and Q21/Q38 where present. |
| Media prompts imply real residents or facilities | Require fictional/de-identified prompt language and prohibit uploads or real identifiers. |

## No New Compliance Issue Found

No new compliance issue was identified in the reviewed TTS source beyond the existing required warnings and review flags.
