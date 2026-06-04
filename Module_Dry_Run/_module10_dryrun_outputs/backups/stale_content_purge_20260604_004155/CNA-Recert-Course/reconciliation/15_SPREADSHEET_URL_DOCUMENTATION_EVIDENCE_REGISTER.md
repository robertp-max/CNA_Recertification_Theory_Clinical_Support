# 15 - Spreadsheet URL Documentation Evidence Register

## Title

15 - Spreadsheet URL Documentation Evidence Register

## Status

Status: Incomplete - evidence missing for 59 URL rows and spreadsheet sheet/row/cell positions

## Priority

P1 High

## Owner

Repo Auditor

## Reviewer

Program Owner

## Last checked

2026-06-03

## Source files inspected

- `CNA-Recert-Course\reconciliation\MISSING_DOCUMENTATION_GENERATION_AUDIT.md`
- `CNA-Recert-Course\reconciliation\00_CI_ION_RECONCILIATION_EXECUTIVE_SUMMARY.md`
- `CNA-Recert-Course\reconciliation\05_MISSING_DOCUMENTATION_REGISTER.md`
- `CNA-Recert-Course\reconciliation\13_GO_NO_GO_BLOCKERS_AND_DECISIONS.md`
- `CNA-Recert-Course\reconciliation\15_SPREADSHEET_URL_DOCUMENTATION_EVIDENCE_REGISTER.md`
- `CNA-Recert-Course\Content`
- `CNA-Recert-Course\ContentV2`
- `standalone-course-mvp\src\data`
## Export evidence inspected

- `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428`
- `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\manifest.json`
- `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\CI-ION - Course Structures - Contents.xlsx`
- `CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files`

Recalculated from `manifest.json`: 162 URLs, 39 copied/imported, 36 skipped, 22 errored, 57 duplicate/tab-anchor rows, 7 external-only, 1 owner-decision folder rows, 59 still undocumented.
## Purpose

Assign every URL in `manifest.json` `links_found` to an evidence status using inspected local evidence only.

## Findings

| Status bucket | Count | Evidence rule |
|---|---:|---|
| Total URLs found | 162 | `manifest.links_found` |
| Copied/imported document exists and is mapped | 39 | Source ID appears in `files_added` and copied file exists locally |
| Skipped by copy config | 36 | Source ID appears in `skipped` |
| Blocked/source access/copy error | 22 | Source ID appears in `errors` |
| Duplicate/tab-anchor URL | 57 | Repeated source ID after canonical row |
| External reference only | 7 | No local copied evidence in manifest |
| Needs owner decision | 1 | Folder found but not copied |
| Needs document import | 0 | No current rows after manifest classification |
| Still undocumented | 59 | skipped + errored + owner-decision + needs-import |

## Gaps

- The source spreadsheet `.xlsx` is present, but sheet name, row number, and cell address remain unparsed.
- 22 failed copy/convert/access rows need re-export or owner access action.
- 36 skipped rows and 1 folder row need owner decisions.
- External URLs are not used as evidence unless a local evidence note exists.

## Required decisions

- Program Owner must decide whether to import skipped videos and `Admission Exam` folder contents.
- Program Owner must provide access or alternative exports for failed Google Docs/Sheet.

## Acceptance criteria

- Every manifest URL has exactly one status in this register.
- Unavailable local evidence remains incomplete and is not treated as documented.

## Next action

Parse the `.xlsx` for sheet/row/cell positions and re-export failed Google Docs/Sheet as PDFs.

## Full URL Evidence Register

| URL Evidence ID | Source URL | URL Type | Source ID | Tab/Anchor | Evidence status | Copied file | Equivalent local/repo evidence | Needs new documentation? | Priority |
|---|---|---|---|---|---|---|---|---|---|
| URL-001 | https://calendar.app.google/zkyKoPUjyad9iPAX8 | External link |  |  | External reference only |  |  | Maybe | P3 Low |
| URL-002 | https://chat.whatsapp.com/FCWHuQ26dSeG9luFkuaDdA?mode=ac_t | External link |  |  | External reference only |  |  | Maybe | P3 Low |
| URL-003 | https://discover.trinitydc.edu/moodle/2017/08/22/how-do-i-make-the-existing-attendance-activi... | External link |  |  | External reference only |  |  | Maybe | P3 Low |
| URL-004 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.1y... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.1ysvgirrkiax | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-005 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.4o... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.4o3lxfrzco6y | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-006 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.5d... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.5dup8gwi85qm | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-007 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.7x... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.7xso3sem90yz | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-008 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.9i... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.9ivjc0drbzew | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-009 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.co... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.co7wlbsqwbtg | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-010 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.e3... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.e3s9y0h8xvi9 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-011 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.eb... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.ebcwgvpawq23 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-012 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.kg... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.kg6wv4h1jueq | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-013 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.pq... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.pqhu58w1339k | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-014 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8lA1A/edit?tab=t.qh... | Google Doc | 11bT4y1vmotyypr8ZQpJ62ch | t.qh1vfbdwfhc0 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-015 | https://docs.google.com/document/d/17GxLf9wq7NbnFsrh6u8H8j-Oh2ZMBbjlW0Xo20O2WSU/edit?usp=sharing | Google Doc | 17GxLf9wq7NbnFsrh6u8H8j- |  | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-016 | https://docs.google.com/document/d/17d0_hyv-qhed5RodmVzQr1GRkMfs5Gc7/edit?usp=sharing&ouid=11... | Google Doc | 17d0_hyv-qhed5RodmVzQr1G |  | Copied/imported document exists and is mapped | linked-files/CI Institute of Nursing Student Catalog 3-17-2026.docx | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\CI Institute of Nursing Student Catalog 3-17-2026.docx | No | P3 Low |
| URL-017 | https://docs.google.com/document/d/184yt77NNMf8yalVu1-64u11Psrc2Y-BbA0xddJpz_eE/edit?usp=sharing | Google Doc | 184yt77NNMf8yalVu1-64u11 |  | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-018 | https://docs.google.com/document/d/1FRGsxYGuyJUp1rIDzDIan3syc6Nw26U8aAkl4mns11A/edit?tab=t.0 | Google Doc | 1FRGsxYGuyJUp1rIDzDIan3s | t.0 | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-019 | https://docs.google.com/document/d/1FRGsxYGuyJUp1rIDzDIan3syc6Nw26U8aAkl4mns11A/edit?tab=t.go... | Google Doc | 1FRGsxYGuyJUp1rIDzDIan3s | t.go9vq2guqn86 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-020 | https://docs.google.com/document/d/1FRGsxYGuyJUp1rIDzDIan3syc6Nw26U8aAkl4mns11A/edit?tab=t.lu... | Google Doc | 1FRGsxYGuyJUp1rIDzDIan3s | t.lujh47vaaqnw | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-021 | https://docs.google.com/document/d/1IAzoD_AzxX8IYB1_m7zIsxDOfnQeNK14HtcJnZAL0xE/edit?usp=sharing | Google Doc | 1IAzoD_AzxX8IYB1_m7zIsxD |  | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-022 | https://docs.google.com/document/d/1MXcWg9nDrEwcwEt6IRVrHfEbzsuvcSaS9Ng1uL1ZqZ8/edit?usp=sharing | Google Doc | 1MXcWg9nDrEwcwEt6IRVrHfE |  | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-023 | https://docs.google.com/document/d/1OghuL0rboJ83NzJeOsAEqSKjQ2LKXn-_dRWOoM_37VY/edit?tab=t.0 | Google Doc | 1OghuL0rboJ83NzJeOsAEqSK | t.0 | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-024 | https://docs.google.com/document/d/1PpM-XiiHSR0CidkcZ30Qq1tVe1J2NUXPXPekncdckLA/edit?tab=t.0 | Google Doc | 1PpM-XiiHSR0CidkcZ30Qq1t | t.0 | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-025 | https://docs.google.com/document/d/1PpM-XiiHSR0CidkcZ30Qq1tVe1J2NUXPXPekncdckLA/edit?tab=t.4v... | Google Doc | 1PpM-XiiHSR0CidkcZ30Qq1t | t.4vx18197f7ez | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-026 | https://docs.google.com/document/d/1RbvkwBH7mPBR2VcaYUfRl5mACqKP-CeMXpIjaihRNNk/edit?tab=t.lu... | Google Doc | 1RbvkwBH7mPBR2VcaYUfRl5m | t.lu9x8exizem7 | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-027 | https://docs.google.com/document/d/1RbvkwBH7mPBR2VcaYUfRl5mACqKP-CeMXpIjaihRNNk/edit?tab=t.v4... | Google Doc | 1RbvkwBH7mPBR2VcaYUfRl5m | t.v4xr0ca887si | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-028 | https://docs.google.com/document/d/1SW8VYdQiX4G1kkS2i0q9w7ZfxUOFjpOCoC7l5AUgnoU/edit?tab=t.0 | Google Doc | 1SW8VYdQiX4G1kkS2i0q9w7Z | t.0 | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-029 | https://docs.google.com/document/d/1SW8VYdQiX4G1kkS2i0q9w7ZfxUOFjpOCoC7l5AUgnoU/edit?tab=t.bg... | Google Doc | 1SW8VYdQiX4G1kkS2i0q9w7Z | t.bg8lfqhmhwxb | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-030 | https://docs.google.com/document/d/1SW8VYdQiX4G1kkS2i0q9w7ZfxUOFjpOCoC7l5AUgnoU/edit?tab=t.op... | Google Doc | 1SW8VYdQiX4G1kkS2i0q9w7Z | t.opjt394kcfw6 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-031 | https://docs.google.com/document/d/1UzdUDKgeGX357U6jNAoYpKMzlzC4SNjhMHqnan53zpA/edit?usp=sharing | Google Doc | 1UzdUDKgeGX357U6jNAoYpKM |  | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-032 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.2k... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.2kyue5j4kg8v | Skipped by Copy Config |  |  | Yes | P2 Medium |
| URL-033 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.4e... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.4e7q5a8bnplu | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-034 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.4x... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.4xc235uyk158 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-035 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.5r... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.5r8td36ap864 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-036 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.ao... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.aogncpid40l4 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-037 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.bq... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.bqg9tj71ysg2 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-038 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.d1... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.d1k7u75nvjpa | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-039 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.d5... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.d5jqk2bf4rts | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-040 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.e5... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.e5cbqry5ypo | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-041 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.ez... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.ezuoarmirwmq | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-042 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.hn... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.hnphcjo3z75x | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-043 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.ie... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.ieur3chqgyyi | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-044 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.je... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.je6ofew1ptgd | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-045 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.js... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.jsbbzdnrts1h | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-046 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.mp... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.mpb25krgelbk | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-047 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.nj... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.njq5pt77owji | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-048 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.nm... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.nmenv1ic55tz | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-049 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.pr... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.prin14qu0p79 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-050 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.qc... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.qcu8kk4y98e | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-051 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.qe... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.qebwadkrttnu | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-052 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.qh... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.qh1vfbdwfhc0 | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-053 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.vk... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.vkdg35rpkzio | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-054 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.vp... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.vp9isapajart | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-055 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07asfv0/edit?tab=t.x0... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQjs | t.x0cbpdos0hrh | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-056 | https://docs.google.com/document/d/1_F3jLGPga0ZhCFWdZRR3NVpVwjiVIcSvuKZe9sr5qwg/edit?disco=AA... | Google Doc | 1_F3jLGPga0ZhCFWdZRR3NVp | t.pdpps3g0qdml | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-057 | https://docs.google.com/document/d/1aGEBmMt2PqT9CxZWB_rdpEdA19kpF4uNT6vOWKib0fc/edit?tab=t.0 | Google Doc | 1aGEBmMt2PqT9CxZWB_rdpEd | t.0 | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-058 | https://docs.google.com/document/d/1aGEBmMt2PqT9CxZWB_rdpEdA19kpF4uNT6vOWKib0fc/edit?usp=sharing | Google Doc | 1aGEBmMt2PqT9CxZWB_rdpEd |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-059 | https://docs.google.com/document/d/1aIx_kNjfZF9zktuoRmlmjItwIsR2UpYkRER_7mvXMmI/edit?usp=sharing | Google Doc | 1aIx_kNjfZF9zktuoRmlmjIt |  | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-060 | https://docs.google.com/document/d/1mNA503NSb8H-zGjWpxdiMtFmt9DEsRqtLjh1aKljFp0/edit?tab=t.dc... | Google Doc | 1mNA503NSb8H-zGjWpxdiMtF | t.dcn6ynfu7736 | Copy failed due to access or missing item |  |  | Yes | P1 High |
| URL-061 | https://docs.google.com/document/d/1p68p5sH8w93u0WyWUFSZvXhTEio4x0Lir8S0rpaieSY/edit?usp=sharing | Google Doc | 1p68p5sH8w93u0WyWUFSZvXh |  | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-062 | https://docs.google.com/document/d/1skVpG42aV14Ob0TbWG7L7CIcQizSSEzatt7qgbL91zg/edit?usp=sharing | Google Doc | 1skVpG42aV14Ob0TbWG7L7CI |  | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-063 | https://docs.google.com/document/d/1u1GdQ31u__JDx_FibzL3LaDb-_bjyWKj0h9NPacPZ4Q/edit?tab=t.7w... | Google Doc | 1u1GdQ31u__JDx_FibzL3LaD | t.7wumkcko9b93 | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-064 | https://docs.google.com/document/d/1u1GdQ31u__JDx_FibzL3LaDb-_bjyWKj0h9NPacPZ4Q/edit?tab=t.mb... | Google Doc | 1u1GdQ31u__JDx_FibzL3LaD | t.mbirm069c8eh | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-065 | https://docs.google.com/document/d/1u1GdQ31u__JDx_FibzL3LaDb-_bjyWKj0h9NPacPZ4Q/edit?tab=t.rp... | Google Doc | 1u1GdQ31u__JDx_FibzL3LaD | t.rp7mm468mnab | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-066 | https://docs.google.com/document/d/1u1GdQ31u__JDx_FibzL3LaDb-_bjyWKj0h9NPacPZ4Q/edit?tab=t.tc... | Google Doc | 1u1GdQ31u__JDx_FibzL3LaD | t.tcwtbmka1b4h | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-067 | https://docs.google.com/document/d/1vJW8RrM8KjbKhkuB7E2HoEfN-WYkLZw5Q9KrhU9uTqI/edit?tab=t.0 | Google Doc | 1vJW8RrM8KjbKhkuB7E2HoEf | t.0 | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-068 | https://docs.google.com/document/d/1vJW8RrM8KjbKhkuB7E2HoEfN-WYkLZw5Q9KrhU9uTqI/edit?tab=t.9j... | Google Doc | 1vJW8RrM8KjbKhkuB7E2HoEf | t.9jn6osq0jm0a | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-069 | https://docs.google.com/document/d/1vJW8RrM8KjbKhkuB7E2HoEfN-WYkLZw5Q9KrhU9uTqI/edit?tab=t.fj... | Google Doc | 1vJW8RrM8KjbKhkuB7E2HoEf | t.fjpiqd9a2ifb | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-070 | https://docs.google.com/document/d/1xJuYP8Nr0tlJAFBPHqQzb2Gkmufl8eG3Tdv-adYtAco/edit?tab=t.pu... | Google Doc | 1xJuYP8Nr0tlJAFBPHqQzb2G | t.pugcy46u0f48 | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-071 | https://docs.google.com/document/d/1xJuYP8Nr0tlJAFBPHqQzb2Gkmufl8eG3Tdv-adYtAco/edit?tab=t.qv... | Google Doc | 1xJuYP8Nr0tlJAFBPHqQzb2G | t.qvfk0wepkncs | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-072 | https://docs.google.com/document/d/1xJuYP8Nr0tlJAFBPHqQzb2Gkmufl8eG3Tdv-adYtAco/edit?tab=t.sm... | Google Doc | 1xJuYP8Nr0tlJAFBPHqQzb2G | t.smzjndxqtuve | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-073 | https://docs.google.com/document/d/1zO4-DU1N2uV2ULVKhDoYcqWJyookJP_6dEcW4N0UABU/edit?usp=sharing | Google Doc | 1zO4-DU1N2uV2ULVKhDoYcqW |  | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-074 | https://docs.google.com/spreadsheets/d/1l-Q42fB-f9UWCIYcGYeZ_YaIwF_IKDTTqhF0_zOWL6c/edit?usp=... | Google Sheet | 1l-Q42fB-f9UWCIYcGYeZ_Ya |  | Blocked - Source Access / Copy Error |  |  | Yes | P1 High |
| URL-075 | https://docs.moodle.org/500/en/Grade_hiding | External link |  |  | External reference only |  |  | Maybe | P3 Low |
| URL-076 | https://drive.google.com/drive/folders/1cyDJYkaXaQxVQLlMERJ7DEDLX9AiTGni?usp=drive_link | Google Drive folder | 1cyDJYkaXaQxVQLlMERJ7DED |  | Needs owner decision |  |  | Yes | P1 High |
| URL-077 | https://drive.google.com/file/d/10JWvptJKknHmS7m-n361bE8k9vKmlsIH/view?usp=drive_link | Google Drive file | 10JWvptJKknHmS7m-n361bE8 |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-078 | https://drive.google.com/file/d/10JWvptJKknHmS7m-n361bE8k9vKmlsIH/view?usp=sharing | Google Drive file | 10JWvptJKknHmS7m-n361bE8 |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-079 | https://drive.google.com/file/d/11VQ-Kvx1EVJF1lHfn9bc78Ego2D81mPw/view?usp=drive_link | Google Drive file | 11VQ-Kvx1EVJF1lHfn9bc78E |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-080 | https://drive.google.com/file/d/138aKYcs0souubNtX7xhrD8tSZuHiwQSQ/view?usp=drive_link | Google Drive file | 138aKYcs0souubNtX7xhrD8t |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-16.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-16.pdf | No | P3 Low |
| URL-081 | https://drive.google.com/file/d/15UAOZGj0BPfLJqCVSjBAq7RneIYpcAgF/view?usp=drive_link | Google Drive file | 15UAOZGj0BPfLJqCVSjBAq7R |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-082 | https://drive.google.com/file/d/15m2D8dBNGxkoVzf_zcJay00AdB6JbI99/view?usp=sharing | Google Drive file | 15m2D8dBNGxkoVzf_zcJay00 |  | Copied/imported document exists and is mapped | linked-files/CI-ION_ Pre-Orientation Student Catalog Test.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\CI-ION_ Pre-Orientation Student Catalog Test.pdf | No | P3 Low |
| URL-083 | https://drive.google.com/file/d/16FUX7666tfiJHPEIwgiQalQ4d2LsYNWT/view?usp=drive_link | Google Drive file | 16FUX7666tfiJHPEIwgiQalQ |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-12.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-12.pdf | No | P3 Low |
| URL-084 | https://drive.google.com/file/d/17DbGGTUItN7vRqBvq1Lr2JzfWxtjX4L9/view?usp=drive_link | Google Drive file | 17DbGGTUItN7vRqBvq1Lr2Jz |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-1.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-1.pdf | No | P3 Low |
| URL-085 | https://drive.google.com/file/d/17hzvd-vUpmZEEbQwKPitnCqz7yYGQ2x-/view?usp=drive_link | Google Drive file | 17hzvd-vUpmZEEbQwKPitnCq |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-086 | https://drive.google.com/file/d/19X-cAC7GxByuG4d29GyqdpJskLngBolV/view?usp=drive_link | Google Drive file | 19X-cAC7GxByuG4d29GyqdpJ |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-087 | https://drive.google.com/file/d/19X-cAC7GxByuG4d29GyqdpJskLngBolV/view?usp=sharing | Google Drive file | 19X-cAC7GxByuG4d29GyqdpJ |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-088 | https://drive.google.com/file/d/1B9JjyYPOYZnSW_zF2pp73H-L5SfUfwTo/view?usp=drive_link | Google Drive file | 1B9JjyYPOYZnSW_zF2pp73H- |  | Copied/imported document exists and is mapped | linked-files/PM Day 15 Module 13 Long Term Patient Resident.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\PM Day 15 Module 13 Long Term Patient Resident.pdf | No | P3 Low |
| URL-089 | https://drive.google.com/file/d/1BLAAo1BuMhx77VHEcki5bJBHmiv-_3S9/view?usp=drive_link | Google Drive file | 1BLAAo1BuMhx77VHEcki5bJB |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-3.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-3.pdf | No | P3 Low |
| URL-090 | https://drive.google.com/file/d/1CGDbCREHJZlgCHhaRqH7Q2JQ-1Qq6E4W/view?usp=drive_link | Google Drive file | 1CGDbCREHJZlgCHhaRqH7Q2J |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-091 | https://drive.google.com/file/d/1D6d-NSQKz4Cb_8yLcBZHbk12SiGZ_bJg/view?usp=drive_link | Google Drive file | 1D6d-NSQKz4Cb_8yLcBZHbk1 |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-092 | https://drive.google.com/file/d/1DTEwssb194rZAMe4f6RsPAAmXPP1bnrw/view?usp=drive_link | Google Drive file | 1DTEwssb194rZAMe4f6RsPAA |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-093 | https://drive.google.com/file/d/1DTEwssb194rZAMe4f6RsPAAmXPP1bnrw/view?usp=sharing | Google Drive file | 1DTEwssb194rZAMe4f6RsPAA |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-094 | https://drive.google.com/file/d/1Dc5GoP4VDyGYhFnYAqGGGAMEgZAdPm80/view?usp=drive_link | Google Drive file | 1Dc5GoP4VDyGYhFnYAqGGGAM |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-095 | https://drive.google.com/file/d/1Dc5GoP4VDyGYhFnYAqGGGAMEgZAdPm80/view?usp=sharing | Google Drive file | 1Dc5GoP4VDyGYhFnYAqGGGAM |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-096 | https://drive.google.com/file/d/1EiV0ZWvTGAwD6dR7QsHnHikRKisQgtVo/view?usp=drive_link | Google Drive file | 1EiV0ZWvTGAwD6dR7QsHnHik |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-097 | https://drive.google.com/file/d/1FfjG-bqgRCnj52F6mP-NReI3ZB7cKlpX/view?usp=drive_link | Google Drive file | 1FfjG-bqgRCnj52F6mP-NReI |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-098 | https://drive.google.com/file/d/1HKz1WgV90INNVHTgi_3jdArS-vrXBsYD/view?usp=drive_link | Google Drive file | 1HKz1WgV90INNVHTgi_3jdAr |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-099 | https://drive.google.com/file/d/1JRUbhXs8y-2a5Gu71WTl9bEyhKfyaxd-/view?usp=drive_link | Google Drive file | 1JRUbhXs8y-2a5Gu71WTl9bE |  | Copied/imported document exists and is mapped | linked-files/Cover_Tutorials_Text.png | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\Cover_Tutorials_Text.png | No | P3 Low |
| URL-100 | https://drive.google.com/file/d/1Jaiwn8X-DdD0JR1GvXvYsIw7_iV3JpwE/view?usp=drive_link | Google Drive file | 1Jaiwn8X-DdD0JR1GvXvYsIw |  | Copied/imported document exists and is mapped | linked-files/Cover_Admission_Text.png | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\Cover_Admission_Text.png | No | P3 Low |
| URL-101 | https://drive.google.com/file/d/1LxOHldGeix950JVxR4jchP9Dd2elg4Gt/view?usp=sharing | Google Drive file | 1LxOHldGeix950JVxR4jchP9 |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-102 | https://drive.google.com/file/d/1M-TAvXPYta8KpIZtCMsKiR9PXXmPwSGB/view?usp=drive_link | Google Drive file | 1M-TAvXPYta8KpIZtCMsKiR9 |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-103 | https://drive.google.com/file/d/1M-TAvXPYta8KpIZtCMsKiR9PXXmPwSGB/view?usp=sharing | Google Drive file | 1M-TAvXPYta8KpIZtCMsKiR9 |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-104 | https://drive.google.com/file/d/1NkfXp4e1GY5wqwltNT5muWty2Teq9t9y/view?usp=drive_link | Google Drive file | 1NkfXp4e1GY5wqwltNT5muWt |  | Copied/imported document exists and is mapped | linked-files/Day 3 Module 15.1 Observation and Charting.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\Day 3 Module 15.1 Observation and Charting.pdf | No | P3 Low |
| URL-105 | https://drive.google.com/file/d/1P9_UlVFp70gBg67ML9Adk6kseCgz2V4W/view?usp=drive_link | Google Drive file | 1P9_UlVFp70gBg67ML9Adk6k |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-106 | https://drive.google.com/file/d/1PdTCJNd0VGeyRgkxqMGwLsqkZQJaS53Z/view?usp=drive_link | Google Drive file | 1PdTCJNd0VGeyRgkxqMGwLsq |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-107 | https://drive.google.com/file/d/1PdTCJNd0VGeyRgkxqMGwLsqkZQJaS53Z/view?usp=sharing | Google Drive file | 1PdTCJNd0VGeyRgkxqMGwLsq |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-108 | https://drive.google.com/file/d/1PlAgQMGuQAmOdxAUChoZnenbloa9W-5X/view?usp=drive_link | Google Drive file | 1PlAgQMGuQAmOdxAUChoZnen |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-109 | https://drive.google.com/file/d/1Q1aOELWgW_aUploZFvxZ1VL13mZ_oWt5/view?usp=drive_link | Google Drive file | 1Q1aOELWgW_aUploZFvxZ1VL |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-13.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-13.pdf | No | P3 Low |
| URL-110 | https://drive.google.com/file/d/1QSN9Y07Yc3NG4S-VmXZLU01vXuY0802T/view?usp=drive_link | Google Drive file | 1QSN9Y07Yc3NG4S-VmXZLU01 |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-111 | https://drive.google.com/file/d/1QiPgt5yCKt2faGVaR-6l_c1nATK8m6T-/view?usp=drive_link | Google Drive file | 1QiPgt5yCKt2faGVaR-6l_c1 |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-112 | https://drive.google.com/file/d/1ROzQHsWC5yROZp44roDvfsVyYFWDRyJQ/view?usp=drive_link | Google Drive file | 1ROzQHsWC5yROZp44roDvfsV |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-4.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-4.pdf | No | P3 Low |
| URL-113 | https://drive.google.com/file/d/1RSiZNXtvyi5zUc8zgVaKT0wlLxOqKrPh/view?usp=drive_link | Google Drive file | 1RSiZNXtvyi5zUc8zgVaKT0w |  | Copied/imported document exists and is mapped | linked-files/PM Day 2 Module 2 Patient Resident Rights.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\PM Day 2 Module 2 Patient Resident Rights.pdf | No | P3 Low |
| URL-114 | https://drive.google.com/file/d/1RhQfGcFbrJ01im4kRAHICy4Ia2yfUu4F/view?usp=drive_link | Google Drive file | 1RhQfGcFbrJ01im4kRAHICy4 |  | Copied/imported document exists and is mapped | linked-files/Day 6 Module 15.2 Observation and Charting.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\Day 6 Module 15.2 Observation and Charting.pdf | No | P3 Low |
| URL-115 | https://drive.google.com/file/d/1SCadMh7_JA6q7P7euJLNmbdzmMDt1MTb/view?usp=drive_link | Google Drive file | 1SCadMh7_JA6q7P7euJLNmbd |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-6.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-6.pdf | No | P3 Low |
| URL-116 | https://drive.google.com/file/d/1TOHQR_DsHe6bHlHN7ZYJqA9d81UNiJgN/view?usp=drive_link | Google Drive file | 1TOHQR_DsHe6bHlHN7ZYJqA9 |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-2.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-2.pdf | No | P3 Low |
| URL-117 | https://drive.google.com/file/d/1V2z3AFIcY3R_uMEIl3Peb098kYOK1IR-/view?usp=drive_link | Google Drive file | 1V2z3AFIcY3R_uMEIl3Peb09 |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-118 | https://drive.google.com/file/d/1W-JJuykteCH0meaBZdg5YlXKsii1iB5K/view?usp=drive_link | Google Drive file | 1W-JJuykteCH0meaBZdg5YlX |  | Copied/imported document exists and is mapped | linked-files/Cover_Day_Text.png | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\Cover_Day_Text.png | No | P3 Low |
| URL-119 | https://drive.google.com/file/d/1XpEFDbuinrHg2TDyBrcHD0AN_i4krkpA/view?usp=drive_link | Google Drive file | 1XpEFDbuinrHg2TDyBrcHD0A |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-120 | https://drive.google.com/file/d/1XpEFDbuinrHg2TDyBrcHD0AN_i4krkpA/view?usp=sharing | Google Drive file | 1XpEFDbuinrHg2TDyBrcHD0A |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-121 | https://drive.google.com/file/d/1XtKr2ASDVFGfFMRyFrc-LMC9dJvd4v46/view?usp=drive_link | Google Drive file | 1XtKr2ASDVFGfFMRyFrc-LMC |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-122 | https://drive.google.com/file/d/1XtKr2ASDVFGfFMRyFrc-LMC9dJvd4v46/view?usp=sharing | Google Drive file | 1XtKr2ASDVFGfFMRyFrc-LMC |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-123 | https://drive.google.com/file/d/1Yk3wAiiZZDGAX23k2MgGjbriida85fYG/view?usp=drive_link | Google Drive file | 1Yk3wAiiZZDGAX23k2MgGjbr |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-10.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-10.pdf | No | P3 Low |
| URL-124 | https://drive.google.com/file/d/1ZGdwYv4xVTIiRLMfFd5GgnV3PkATbcLN/view?usp=drive_link | Google Drive file | 1ZGdwYv4xVTIiRLMfFd5GgnV |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-5.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-5.pdf | No | P3 Low |
| URL-125 | https://drive.google.com/file/d/1ZSR9EID-IX3z0ttP64e1hZyAY9ZdtI9D/view?usp=sharing | Google Drive file | 1ZSR9EID-IX3z0ttP64e1hZy |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-126 | https://drive.google.com/file/d/1_7wvYCbxEvA7v_uOnTxXOwE_ZnHVs1zU/view?usp=drive_link | Google Drive file | 1_7wvYCbxEvA7v_uOnTxXOwE |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-14.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-14.pdf | No | P3 Low |
| URL-127 | https://drive.google.com/file/d/1_Zjzz6n6lyq-WuYy8Ode6tWQA7FoR9Dc/view?usp=drive_link | Google Drive file | 1_Zjzz6n6lyq-WuYy8Ode6tW |  | Copied/imported document exists and is mapped | linked-files/CI Institute of Nursing - Course Syllabus.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\CI Institute of Nursing - Course Syllabus.pdf | No | P3 Low |
| URL-128 | https://drive.google.com/file/d/1aHFRYdpKSuM7aB_9XAEbWtogkD70x-h4/view?usp=drive_link | Google Drive file | 1aHFRYdpKSuM7aB_9XAEbWto |  | Copied/imported document exists and is mapped | linked-files/PM Day 1 Module 2 Patient Resident Rights.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\PM Day 1 Module 2 Patient Resident Rights.pdf | No | P3 Low |
| URL-129 | https://drive.google.com/file/d/1bdGeAcD9ihjejnJ56FIGgzxvm7bIdgah/view?usp=drive_link | Google Drive file | 1bdGeAcD9ihjejnJ56FIGgzx |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-15.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-15.pdf | No | P3 Low |
| URL-130 | https://drive.google.com/file/d/1bhFKJ3Mub01Yh9bdhtIHXOo6tG5xTS8Q/view?usp=drive_link | Google Drive file | 1bhFKJ3Mub01Yh9bdhtIHXOo |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-9.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-9.pdf | No | P3 Low |
| URL-131 | https://drive.google.com/file/d/1bw2whsd6O5pMdZqCOgVQxDd4hNPEoB-v/view?usp=drive_link | Google Drive file | 1bw2whsd6O5pMdZqCOgVQxDd |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-132 | https://drive.google.com/file/d/1cIZqiovDO-LcK-8uvWsmjVXLfXSbSZa4/view?usp=drive_link | Google Drive file | 1cIZqiovDO-LcK-8uvWsmjVX |  | Copied/imported document exists and is mapped | linked-files/PM Day 13 Module 9 Patient Care Procedures-1-31.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\PM Day 13 Module 9 Patient Care Procedures-1-31.pdf | No | P3 Low |
| URL-133 | https://drive.google.com/file/d/1cktrciiRdZQzV-sA1LHs_qXtim_fFKDg/view?usp=drive_link | Google Drive file | 1cktrciiRdZQzV-sA1LHs_qX |  | Copied/imported document exists and is mapped | linked-files/PM Day 14 Module 9 Patient Care Procedures-32-43.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\PM Day 14 Module 9 Patient Care Procedures-32-43.pdf | No | P3 Low |
| URL-134 | https://drive.google.com/file/d/1dxhGGg_3126kl0hrMQrf_QdgXui4KdK7/view?usp=drive_link | Google Drive file | 1dxhGGg_3126kl0hrMQrf_Qd |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-135 | https://drive.google.com/file/d/1dxhGGg_3126kl0hrMQrf_QdgXui4KdK7/view?usp=sharing | Google Drive file | 1dxhGGg_3126kl0hrMQrf_Qd |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-136 | https://drive.google.com/file/d/1eRAoboxZh815OMMt9682lzuI4CLOlloO/view?usp=drive_link | Google Drive file | 1eRAoboxZh815OMMt9682lzu |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-137 | https://drive.google.com/file/d/1enLDd1Rx4tNYF5Fz4FV0btXQkyvdjLdJ/view?usp=drive_link | Google Drive file | 1enLDd1Rx4tNYF5Fz4FV0btX |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-138 | https://drive.google.com/file/d/1enLDd1Rx4tNYF5Fz4FV0btXQkyvdjLdJ/view?usp=sharing | Google Drive file | 1enLDd1Rx4tNYF5Fz4FV0btX |  | Duplicate URL or same source document with different tab/anchor |  |  | No | P3 Low |
| URL-139 | https://drive.google.com/file/d/1firsvTipcO5A1dgs2YTsq_6UsV4ZlTLV/view?usp=drive_link | Google Drive file | 1firsvTipcO5A1dgs2YTsq_6 |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-140 | https://drive.google.com/file/d/1gWvKPPjAYQjn_YwjP-_B3q7riueefezY/view?usp=drive_link | Google Drive file | 1gWvKPPjAYQjn_YwjP-_B3q7 |  | Copied/imported document exists and is mapped | linked-files/PM Day 8 Module 8 Patient Care Skills-12-16.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\PM Day 8 Module 8 Patient Care Skills-12-16.pdf | No | P3 Low |
| URL-141 | https://drive.google.com/file/d/1g_xmw1crGNXmvA3cG76Y8dB6c616b70Y/view?usp=drive_link | Google Drive file | 1g_xmw1crGNXmvA3cG76Y8dB |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-142 | https://drive.google.com/file/d/1j7pyb6iL1ZDXmqq_R3Lu7uTsmxqPRg4R/view?usp=drive_link | Google Drive file | 1j7pyb6iL1ZDXmqq_R3Lu7uT |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-7.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-7.pdf | No | P3 Low |
| URL-143 | https://drive.google.com/file/d/1jpgBpZB56-LNQD75p0AvtpAZHi7XTmAx/view?usp=drive_link | Google Drive file | 1jpgBpZB56-LNQD75p0AvtpA |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-11.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-11.pdf | No | P3 Low |
| URL-144 | https://drive.google.com/file/d/1lMYz3sAMxdj_IVHG2IpS_8LGcZsvy3oS/view?usp=drive_link | Google Drive file | 1lMYz3sAMxdj_IVHG2IpS_8L |  | Copied/imported document exists and is mapped | linked-files/PM Day 10 Module 8 Patient Care Skills-11-23.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\PM Day 10 Module 8 Patient Care Skills-11-23.pdf | No | P3 Low |
| URL-145 | https://drive.google.com/file/d/1lpbawCo9zmyYkSuq8zvMjz6ETYNkjPtj/view?usp=drive_link | Google Drive file | 1lpbawCo9zmyYkSuq8zvMjz6 |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-17.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-17.pdf | No | P3 Low |
| URL-146 | https://drive.google.com/file/d/1m3zq9vhc5rF6WVYoz2MhQw1O46eihdXt/view?usp=drive_link | Google Drive file | 1m3zq9vhc5rF6WVYoz2MhQw1 |  | Copied/imported document exists and is mapped | linked-files/PM Day 7 Module 8 Patient Care Skills-1-11.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\PM Day 7 Module 8 Patient Care Skills-1-11.pdf | No | P3 Low |
| URL-147 | https://drive.google.com/file/d/1mMy-CYXxo9U1Kdv22d04OJHR9mCYvn3e/view?usp=drive_link | Google Drive file | 1mMy-CYXxo9U1Kdv22d04OJH |  | Copied/imported document exists and is mapped | linked-files/AM Day 6 - PM Day 11 Module 8 Patient Care Skills.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\AM Day 6 - PM Day 11 Module 8 Patient Care Skills.pdf | No | P3 Low |
| URL-148 | https://drive.google.com/file/d/1pA2NRbc6kvdEu7ms8LPnDFjTB48d9ngx/view?usp=drive_link | Google Drive file | 1pA2NRbc6kvdEu7ms8LPnDFj |  | Copied/imported document exists and is mapped | linked-files/CI-ION NATP Final Exam.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\CI-ION NATP Final Exam.pdf | No | P3 Low |
| URL-149 | https://drive.google.com/file/d/1pcbJZ1TjurVKgZfSk_NevtY9jqXwNLgM/view?usp=drive_link | Google Drive file | 1pcbJZ1TjurVKgZfSk_NevtY |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-150 | https://drive.google.com/file/d/1rV_L4FnKn7MH3Yu91c__o9-8RYklFbqF/view?usp=drive_link | Google Drive file | 1rV_L4FnKn7MH3Yu91c__o9- |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-151 | https://drive.google.com/file/d/1tL55ld9MA-5KfRnKlnKeAuYza6Bbr_lW/view?usp=drive_link | Google Drive file | 1tL55ld9MA-5KfRnKlnKeAuY |  | Copied/imported document exists and is mapped | linked-files/cccco-na-model-curriculum-module-8.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\cccco-na-model-curriculum-module-8.pdf | No | P3 Low |
| URL-152 | https://drive.google.com/file/d/1tSLunhlkRfdzxqvC0iJYB5BbAS6wObCk/view?usp=drive_link | Google Drive file | 1tSLunhlkRfdzxqvC0iJYB5B |  | Copied/imported document exists and is mapped | linked-files/PM Day 16 Module 13 Long Term Patient Resident.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\PM Day 16 Module 13 Long Term Patient Resident.pdf | No | P3 Low |
| URL-153 | https://drive.google.com/file/d/1thct5_HqxZ00gZLZfZG9hDaMyKLxMMm8/view?usp=drive_link | Google Drive file | 1thct5_HqxZ00gZLZfZG9hDa |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-154 | https://drive.google.com/file/d/1vC4nuiuNhvmoxIbuuK9mO3zw5TZLth_z/view?usp=sharing | Google Drive file | 1vC4nuiuNhvmoxIbuuK9mO3z |  | Copied/imported document exists and is mapped | linked-files/Request for Live Scan Service (Example) .pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\Request for Live Scan Service (Example) .pdf | No | P3 Low |
| URL-155 | https://drive.google.com/file/d/1w0lkIZ93JZYy3fixHN8nepni0mF3-tCp/view?usp=drive_link | Google Drive file | 1w0lkIZ93JZYy3fixHN8nepn |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-156 | https://drive.google.com/file/d/1xEWTAvkT0hba5ILTuyPPpRMKJXgUZRm1/view?usp=drive_link | Google Drive file | 1xEWTAvkT0hba5ILTuyPPpRM |  | Copied/imported document exists and is mapped | linked-files/PM Day 9 Module 8 Patient Care Skills-1-10.pdf | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\PM Day 9 Module 8 Patient Care Skills-1-10.pdf | No | P3 Low |
| URL-157 | https://drive.google.com/file/d/1xkZRCW-MjOUiFmmCEHvDly6PiVBLzFAY/view?usp=drive_link | Google Drive file | 1xkZRCW-MjOUiFmmCEHvDly6 |  | Copied/imported document exists and is mapped | linked-files/Cover_Night_Text.png | CNA-Recert-Course\CI-ION-course-export-CI-ION - Course Structures - Contents-20260601-114428\linked-files\Cover_Night_Text.png | No | P3 Low |
| URL-158 | https://drive.google.com/file/d/1ytdG7bYcYPkaMbxy8gdmHIBDEa6ZhT0c/view?usp=drive_link | Google Drive file | 1ytdG7bYcYPkaMbxy8gdmHIB |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-159 | https://drive.google.com/file/d/1zUEuTcodzkWRfl_-ByeQdDvMqLIv7t_f/view?usp=drive_link | Google Drive file | 1zUEuTcodzkWRfl_-ByeQdDv |  | Video was skipped because video copying was disabled |  |  | Yes | P2 Medium |
| URL-160 | https://learn.ciinstituteofnursing.com/course/view.php?id=13 | External link |  |  | External reference only |  |  | Maybe | P3 Low |
| URL-161 | https://maps.app.goo.gl/LmiigtC8X9zLTYy77 | External link |  |  | External reference only |  |  | Maybe | P3 Low |
| URL-162 | https://www.figma.com/board/KD7E72xfOhD6DdsCIYnLvx/CI-ION-User-Flows?node-id=296-4423&t=LBYrR... | External link |  |  | External reference only |  |  | Maybe | P3 Low |
