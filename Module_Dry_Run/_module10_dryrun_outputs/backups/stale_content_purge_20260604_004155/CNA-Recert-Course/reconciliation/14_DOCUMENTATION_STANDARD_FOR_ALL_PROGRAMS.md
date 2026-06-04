# 14 — Documentation Standard for All Programs

## Purpose

Define a **reusable documentation standard** for three programs — CNA Recertification, RCFE
Administrator/Admin Training, and Case Manager Training — using the CNA Recert content packet as
the **format/template only**.

> **Guardrail:** Use CNA Recert as the documentation *format* template. **Do not** copy CNA-specific
> compliance assumptions (CDPH approval, NATP sourcing, 720-min model, CNA certificate wording,
> clinical-hour rules) into RCFE Admin or Case Manager. Those programs require their own source and
> regulatory authority, which must not be invented.

## Inputs Reviewed

- CNA Content packet (`CNA-Recert-Course\Content\` 00–23) and ContentV2 docs 00–11.
- Repo search for RCFE / Case Manager source folders (none found in this clone).

## The 26-Artifact Standard

| # | Artifact | CNA Recert (status) | RCFE Admin | Case Manager |
|---:|---|---|---|---|
| 1 | Executive Summary | Exists | Missing — Needs Source | Missing — Needs Source |
| 2 | Regulatory / Source Authority Crosswalk | Exists | Missing — Needs Source | Missing — Needs Source |
| 3 | Syllabus Table | Exists | Missing — Needs Source | Missing — Needs Source |
| 4 | Source Content Audit | Exists (ContentV2 01) | Missing — Needs Source | Missing — Needs Source |
| 5 | Module Lesson Card Map | Exists (ContentV2 03) | Missing — Needs Source | Missing — Needs Source |
| 6 | Module Assessment Map | Exists (ContentV2 04) | Missing — Needs Source | Missing — Needs Source |
| 7 | Final Assessment Map | Exists (ContentV2 05) | Missing — Needs Source | Missing — Needs Source |
| 8 | ContentV2 Schema Alignment Notes | Exists (ContentV2 02) | Missing — Needs Source | Missing — Needs Source |
| 9 | ContentV2 JSON Generation Plan / Package | Exists (courseContentV2.json) | Missing — Needs Source | Missing — Needs Source |
| 10 | Narration Production Guide | Exists (ContentV2 06) | Missing — Needs Source | Missing — Needs Source |
| 11 | Narration Master CSV Specification | Exists (narration_master.csv) | Missing — Needs Source | Missing — Needs Source |
| 12 | TTS Import CSV Specification | Exists (tts_narration_import.csv) | Missing — Needs Source | Missing — Needs Source |
| 13 | Media Prompt Placeholder Map | Exists (ContentV2 07) | Missing — Needs Source | Missing — Needs Source |
| 14 | SME Review Flags | Exists (18 + ContentV2 08) | Missing — Needs Source | Missing — Needs Source |
| 15 | Compliance Review Flags | Exists (19 + ContentV2 08) | Missing — Needs Source | Missing — Needs Source |
| 16 | App Integration Notes | Exists (ContentV2 09) | Missing — Needs Source | Missing — Needs Source |
| 17 | Certificate / Completion Gate Spec | Exists (14 + gate spec) | Missing — Needs Source | Missing — Needs Source |
| 18 | Active-Time Validation Plan (if CE/contact hours) | Partial — not validated | Missing — Needs Source | Missing — Needs Source |
| 19 | Audit Packet / Evidence Retention Plan | Partial (this packet, 11) | Missing — Needs Source | Missing — Needs Source |
| 20 | Accessibility and Mobile QA Checklist | Exists (17) | Missing — Needs Source | Missing — Needs Source |
| 21 | Export Reconciliation Tracker | Created (this tracker) | Missing — Needs Source | Missing — Needs Source |
| 22 | Operations and Support Guide | Missing — to create | Missing — Needs Source | Missing — Needs Source |
| 23 | Go/No-Go Checklist | Created (13) | Missing — Needs Source | Missing — Needs Source |
| 24 | Spreadsheet URL Evidence Register | Created (15) | Missing — Needs Source | Missing — Needs Source |
| 25 | Source Import / Copy Manifest | Exists (manifest.json) | Missing — Needs Source | Missing — Needs Source |
| 26 | Missing Source Access Log | Created (05) | Missing — Needs Source | Missing — Needs Source |

## Program-Specific Rules

### RCFE Administrator / Admin Training
- Source authority is **Title 22 / CDSS Community Care Licensing** (to be supplied by owner) — **not**
  CDPH/NATP. Do not assume CNA regulatory facts apply.
- Do not invent CE/contact-hour approval, certificate wording, or regulatory requirements.
- Create placeholder tracker rows and missing-doc prompts only, until source files are present.

### Case Manager Training
- Source authority and any certification/CE framework must be supplied by the owner.
- Do not invent source content, regulatory requirements, CE approval, or certificate wording.
- Create placeholder tracker rows and missing-doc prompts only, until source files are present.

## Gaps Found

- RCFE Admin and Case Manager have **no local source folders**; all 26 artifacts are placeholders.
- CNA Operations & Support Guide (artifact 22) is missing.

## Owner / Action Needed

- Program Owner: supply RCFE and Case Manager source + regulatory authority.
- Repo Auditor: author CNA Operations & Support Guide.

## Blocker Status

CNA standard is largely satisfied (format template). RCFE/Case Manager are **Needs Source**.

## Next Verification Step

Confirm with owner whether RCFE/Case Manager source material exists elsewhere before generating any
substantive curriculum claims.
