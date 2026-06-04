# CLAUDE — Missing Documentation Prompts

Reusable, hardened prompts to generate the documentation still missing or blocked. Each prompt
preserves the compliance guardrails. **Do not invent CDPH approval, provider/NAC IDs, course hours,
certificate wording, e-signature acceptance, active-time validation, clinical-hour approval, or TTS
authorization. Do not generate PHI. Mark unknowns as `Needs verification`.**

Global constraints for every prompt below:
- Work only inside `C:\AI\Git\CNA_Recertification_Theory_Clinical_Support`.
- Write only inside `CNA-Recert-Course\reconciliation` (or the explicitly named target path).
- Do not modify app source, ContentV2 JSON, module files, quiz banks, or branding.
- Do not commit/push/PR. Back up before overwriting.

---

## Prompt MD-06 — Spreadsheet Positional URL Map

- **Target file:** `CNA-Recert-Course\reconciliation\01_CI_ION_EXPORT_INVENTORY.md` (appendix) and
  the `Spreadsheet URL Evidence` sheet positional columns.
- **Program:** CNA Recert
- **Source files to inspect:** `…\CI-ION - Course Structures - Contents.xlsx`, `manifest.json`.
- **Spreadsheet URL evidence required:** all 162 URLs from `links_found`.
- **Facts to preserve:** the 162-URL total; copied/skipped/error/duplicate counts in doc 15.
- **Must not invent:** sheet/row/cell positions you cannot read; mark unread cells
  `Needs verification`.
- **Expected sections:** sheet inventory; per-URL sheet/row/cell mapping; unresolved cells.
- **Acceptance:** every URL has a sheet name OR an explicit `Needs verification`.
- **Blocker status:** P1, not P0.
- **Owner/Reviewer:** Repo Auditor / Program Owner.

## Prompt MD-07 — Re-export Failed Google Docs as PDF

- **Target:** `…\linked-files\` PDFs for the 22 failed conversions + a note in doc 15.
- **Program:** CNA Recert
- **Source:** `manifest.json` `errors[]` (20 Google Docs, 1 Google Sheet, 1 missing item).
- **Facts to preserve:** the conversion errors are real export limitations, not content gaps.
- **Must not invent:** the contents of docs you cannot open. If access fails, mark
  `Blocked - Source Access / Copy Error`.
- **Expected sections:** list of doc IDs; re-export method; resulting local file; new status.
- **Acceptance:** each of the 22 items reaches `Copied/imported …` or a documented blocked status.
- **Blocker status:** P1.
- **Owner/Reviewer:** Program Owner / Repo Auditor.

## Prompt MD-08 — CDPH Approval Packet (BLOCKED)

- **Target:** `CNA-Recert-Course\PHASE_0_COMPLIANCE_FOUNDATION.md` (do not edit without backup) or a
  new reconciliation note.
- **Program:** CNA Recert
- **Source:** `PHASE_0_COMPLIANCE_FOUNDATION.md`, `00_EXECUTIVE_SUMMARY.md`.
- **Facts to preserve:** certificate issuance is BLOCKED; partial-credit only.
- **Must not invent:** CDPH approval, provider/NAC IDs, approved hours, approved titles, certificate
  wording, e-sign acceptance.
- **Expected sections:** required approvals checklist; current status (all `Open`); evidence needed.
- **Acceptance:** every approval item is `Open`/`Needs verification` until written proof exists.
- **Blocker status:** **P0**.
- **Owner/Reviewer:** Program Owner / Legal / CDPH.

## Prompt MD-09 — RCFE Admin Documentation Set (Placeholder)

- **Target:** `CNA-Recert-Course\reconciliation\RCFE_ADMIN_*` docs + `RCFE Admin Docs` sheet.
- **Program:** RCFE Admin
- **Source files to inspect:** any RCFE source folder the owner supplies (none present now).
- **Spreadsheet URL evidence required:** none unless owner supplies an RCFE export.
- **Facts to preserve:** use CNA *format* only.
- **Must not invent:** RCFE regulatory requirements (Title 22 / CDSS CCLD), CE/contact-hour
  approval, certificate wording, or source content.
- **Expected sections:** the 26-artifact list with `Missing — Needs Source` until source exists.
- **Acceptance:** no substantive RCFE curriculum claims without cited source.
- **Blocker status:** P2 (P1 for source authority).
- **Owner/Reviewer:** Program Owner / RCFE SME / Legal.

## Prompt MD-10 — Case Manager Documentation Set (Placeholder)

- **Target:** `CNA-Recert-Course\reconciliation\CASE_MANAGER_*` docs + `Case Manager Docs` sheet.
- **Program:** Case Manager
- **Source files to inspect:** any Case Manager source the owner supplies (none present now).
- **Facts to preserve:** use CNA *format* only.
- **Must not invent:** Case Manager regulatory framework, CE approval, certificate wording, content.
- **Expected sections:** the 26-artifact list with `Missing — Needs Source`.
- **Acceptance:** no substantive Case Manager claims without cited source.
- **Blocker status:** P2 (P1 for source authority).
- **Owner/Reviewer:** Program Owner / Case Mgmt SME / Legal.

## Prompt MD-11 — CNA Operations and Support Guide

- **Target:** `CNA-Recert-Course\reconciliation\CNA_OPERATIONS_AND_SUPPORT_GUIDE.md`.
- **Program:** CNA Recert
- **Source files to inspect:** `00_EXECUTIVE_SUMMARY.md`, app pages, support flows.
- **Facts to preserve:** no live certificate issuance; PHI never collected.
- **Must not invent:** SLAs, staffing, or approvals not evidenced.
- **Expected sections:** learner support, admin review workflow, escalation, no-PHI handling.
- **Acceptance:** every operational claim traces to an inspected file or is `Needs verification`.
- **Blocker status:** P2.
- **Owner/Reviewer:** Program Owner / Compliance.

## Prompt MD-12 — Admission Exam Folder Decision

- **Target:** note in `13_GO_NO_GO_BLOCKERS_AND_DECISIONS.md` + URL register update.
- **Program:** CNA Recert
- **Source:** `manifest.json` `folders_found_but_not_exported[]` (Admission Exam folder).
- **Facts to preserve:** folder was found but **not** copied (folder copy disabled).
- **Must not invent:** folder contents (never enumerated).
- **Expected sections:** scope question; owner decision; resulting action.
- **Acceptance:** decision recorded; status updated from `Needs owner decision`.
- **Blocker status:** P1.
- **Owner/Reviewer:** Program Owner / Repo Auditor.
