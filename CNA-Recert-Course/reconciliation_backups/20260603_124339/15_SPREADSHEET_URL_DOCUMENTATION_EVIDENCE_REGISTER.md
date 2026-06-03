# 15 — Spreadsheet URL Documentation Evidence Register

## Purpose

Map **every** URL discovered in the CI-ION source spreadsheet to a documentation/evidence status.
A URL appearing in the spreadsheet does NOT mean the linked item is documented locally.

## Inputs Reviewed

- `manifest.json` → `links_found` (162 URLs), `files_added`, `skipped`, `errors`,
  `folders_found_but_not_exported`.
- `linked-files\` directory (copied evidence).

## Method

Each URL is classified by cross-referencing its Google Drive/Docs ID against the manifest's
copied/skipped/error/folder records. Duplicate IDs and alternate `tab=` anchors of the same
document are collapsed to a canonical row; the rest are marked as duplicates.

## Evidence Summary

| Status bucket | Count |
|---|---:|
| Total URLs found | 162 |
| Copied/imported document exists and is mapped | 39 |
| Skipped (video / oversized — copy config) | 36 |
| Copy/convert error (needs extraction or access) | 22 |
| Duplicate URL / alternate tab anchor | 57 |
| External reference only | 7 |
| Folder found but not copied | 1 |
| **Still requires document import / owner decision** | **59** |

## Gaps Found

- Positional columns (sheet name / row / cell) are **Needs verification** until the `.xlsx` is
  parsed (REC-003). The full positional register lives in the `Spreadsheet URL Evidence` sheet of
  `CI_ION_Course_Reconciliation_Master_Tracker.xlsx`.
- 22 native Google Docs/Sheet links failed Office conversion and are undocumented.
- 36 media/oversized items and 1 folder were skipped by config.

## Owner / Action Needed

- Program Owner: re-export failed Google Docs as PDF; decide on videos/folder.
- Repo Auditor: parse `.xlsx` to backfill sheet/row/cell positions.

## Blocker Status

**Status: Incomplete — evidence missing** for positional columns and 59
undocumented URLs. Do not treat the spreadsheet URL set as fully documented.

## Next Verification Step

Parse `CI-ION - Course Structures - Contents.xlsx` to attach each URL to its sheet/row/cell.

---

## Full URL Evidence Register (162 URLs)

| URL Evidence ID | Source URL | URL Type | Source ID | Tab/Anchor | Copy Status | Needs New Doc? | Priority |
|---|---|---|---|---|---|---|---|
| URL-001 | https://calendar.app.google/zkyKoPUjyad9iPAX8 | External link |  |  | External reference only | Maybe | P3 Low |
| URL-002 | https://chat.whatsapp.com/FCWHuQ26dSeG9luFkuaDdA?mode=ac_t | External link |  |  | External reference only | Maybe | P3 Low |
| URL-003 | https://discover.trinitydc.edu/moodle/2017/08/22/how-do-i-make-the-existing... | External link |  |  | External reference only | Maybe | P3 Low |
| URL-004 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.1ysvgirrkiax | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-005 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.4o3lxfrzco6y | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-006 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.5dup8gwi85qm | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-007 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.7xso3sem90yz | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-008 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.9ivjc0drbzew | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-009 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.co7wlbsqwbtg | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-010 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.e3s9y0h8xvi9 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-011 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.ebcwgvpawq23 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-012 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.kg6wv4h1jueq | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-013 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.pqhu58w1339k | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-014 | https://docs.google.com/document/d/11bT4y1vmotyypr8ZQpJ62chFQOguBh977ZFOrz8... | Google Doc | 11bT4y1vmotyypr8ZQpJ62 | t.qh1vfbdwfhc0 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-015 | https://docs.google.com/document/d/17GxLf9wq7NbnFsrh6u8H8j-Oh2ZMBbjlW0Xo20O... | Google Doc | 17GxLf9wq7NbnFsrh6u8H8 |  | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-016 | https://docs.google.com/document/d/17d0_hyv-qhed5RodmVzQr1GRkMfs5Gc7/edit?u... | Google Doc | 17d0_hyv-qhed5RodmVzQr |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-017 | https://docs.google.com/document/d/184yt77NNMf8yalVu1-64u11Psrc2Y-BbA0xddJp... | Google Doc | 184yt77NNMf8yalVu1-64u |  | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-018 | https://docs.google.com/document/d/1FRGsxYGuyJUp1rIDzDIan3syc6Nw26U8aAkl4mn... | Google Doc | 1FRGsxYGuyJUp1rIDzDIan | t.0 | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-019 | https://docs.google.com/document/d/1FRGsxYGuyJUp1rIDzDIan3syc6Nw26U8aAkl4mn... | Google Doc | 1FRGsxYGuyJUp1rIDzDIan | t.go9vq2guqn86 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-020 | https://docs.google.com/document/d/1FRGsxYGuyJUp1rIDzDIan3syc6Nw26U8aAkl4mn... | Google Doc | 1FRGsxYGuyJUp1rIDzDIan | t.lujh47vaaqnw | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-021 | https://docs.google.com/document/d/1IAzoD_AzxX8IYB1_m7zIsxDOfnQeNK14HtcJnZA... | Google Doc | 1IAzoD_AzxX8IYB1_m7zIs |  | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-022 | https://docs.google.com/document/d/1MXcWg9nDrEwcwEt6IRVrHfEbzsuvcSaS9Ng1uL1... | Google Doc | 1MXcWg9nDrEwcwEt6IRVrH |  | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-023 | https://docs.google.com/document/d/1OghuL0rboJ83NzJeOsAEqSKjQ2LKXn-_dRWOoM_... | Google Doc | 1OghuL0rboJ83NzJeOsAEq | t.0 | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-024 | https://docs.google.com/document/d/1PpM-XiiHSR0CidkcZ30Qq1tVe1J2NUXPXPekncd... | Google Doc | 1PpM-XiiHSR0CidkcZ30Qq | t.0 | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-025 | https://docs.google.com/document/d/1PpM-XiiHSR0CidkcZ30Qq1tVe1J2NUXPXPekncd... | Google Doc | 1PpM-XiiHSR0CidkcZ30Qq | t.4vx18197f7ez | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-026 | https://docs.google.com/document/d/1RbvkwBH7mPBR2VcaYUfRl5mACqKP-CeMXpIjaih... | Google Doc | 1RbvkwBH7mPBR2VcaYUfRl | t.lu9x8exizem7 | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-027 | https://docs.google.com/document/d/1RbvkwBH7mPBR2VcaYUfRl5mACqKP-CeMXpIjaih... | Google Doc | 1RbvkwBH7mPBR2VcaYUfRl | t.v4xr0ca887si | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-028 | https://docs.google.com/document/d/1SW8VYdQiX4G1kkS2i0q9w7ZfxUOFjpOCoC7l5AU... | Google Doc | 1SW8VYdQiX4G1kkS2i0q9w | t.0 | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-029 | https://docs.google.com/document/d/1SW8VYdQiX4G1kkS2i0q9w7ZfxUOFjpOCoC7l5AU... | Google Doc | 1SW8VYdQiX4G1kkS2i0q9w | t.bg8lfqhmhwxb | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-030 | https://docs.google.com/document/d/1SW8VYdQiX4G1kkS2i0q9w7ZfxUOFjpOCoC7l5AU... | Google Doc | 1SW8VYdQiX4G1kkS2i0q9w | t.opjt394kcfw6 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-031 | https://docs.google.com/document/d/1UzdUDKgeGX357U6jNAoYpKMzlzC4SNjhMHqnan5... | Google Doc | 1UzdUDKgeGX357U6jNAoYp |  | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-032 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.2kyue5j4kg8v | Skipped by Copy Config | Yes | P2 High |
| URL-033 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.4e7q5a8bnplu | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-034 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.4xc235uyk158 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-035 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.5r8td36ap864 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-036 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.aogncpid40l4 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-037 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.bqg9tj71ysg2 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-038 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.d1k7u75nvjpa | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-039 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.d5jqk2bf4rts | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-040 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.e5cbqry5ypo | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-041 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.ezuoarmirwmq | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-042 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.hnphcjo3z75x | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-043 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.ieur3chqgyyi | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-044 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.je6ofew1ptgd | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-045 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.jsbbzdnrts1h | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-046 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.mpb25krgelbk | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-047 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.njq5pt77owji | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-048 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.nmenv1ic55tz | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-049 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.prin14qu0p79 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-050 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.qcu8kk4y98e | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-051 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.qebwadkrttnu | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-052 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.qh1vfbdwfhc0 | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-053 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.vkdg35rpkzio | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-054 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.vp9isapajart | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-055 | https://docs.google.com/document/d/1XZyL6Y-nZm5HNcBEWkbPQjsPDfYjMRMc5ceP07a... | Google Doc | 1XZyL6Y-nZm5HNcBEWkbPQ | t.x0cbpdos0hrh | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-056 | https://docs.google.com/document/d/1_F3jLGPga0ZhCFWdZRR3NVpVwjiVIcSvuKZe9sr... | Google Doc | 1_F3jLGPga0ZhCFWdZRR3N | t.pdpps3g0qdml | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-057 | https://docs.google.com/document/d/1aGEBmMt2PqT9CxZWB_rdpEdA19kpF4uNT6vOWKi... | Google Doc | 1aGEBmMt2PqT9CxZWB_rdp | t.0 | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-058 | https://docs.google.com/document/d/1aGEBmMt2PqT9CxZWB_rdpEdA19kpF4uNT6vOWKi... | Google Doc | 1aGEBmMt2PqT9CxZWB_rdp |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-059 | https://docs.google.com/document/d/1aIx_kNjfZF9zktuoRmlmjItwIsR2UpYkRER_7mv... | Google Doc | 1aIx_kNjfZF9zktuoRmlmj |  | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-060 | https://docs.google.com/document/d/1mNA503NSb8H-zGjWpxdiMtFmt9DEsRqtLjh1aKl... | Google Doc | 1mNA503NSb8H-zGjWpxdiM | t.dcn6ynfu7736 | Copy failed due to access or missing item | Yes | P1 High |
| URL-061 | https://docs.google.com/document/d/1p68p5sH8w93u0WyWUFSZvXhTEio4x0Lir8S0rpa... | Google Doc | 1p68p5sH8w93u0WyWUFSZv |  | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-062 | https://docs.google.com/document/d/1skVpG42aV14Ob0TbWG7L7CIcQizSSEzatt7qgbL... | Google Doc | 1skVpG42aV14Ob0TbWG7L7 |  | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-063 | https://docs.google.com/document/d/1u1GdQ31u__JDx_FibzL3LaDb-_bjyWKj0h9NPac... | Google Doc | 1u1GdQ31u__JDx_FibzL3L | t.7wumkcko9b93 | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-064 | https://docs.google.com/document/d/1u1GdQ31u__JDx_FibzL3LaDb-_bjyWKj0h9NPac... | Google Doc | 1u1GdQ31u__JDx_FibzL3L | t.mbirm069c8eh | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-065 | https://docs.google.com/document/d/1u1GdQ31u__JDx_FibzL3LaDb-_bjyWKj0h9NPac... | Google Doc | 1u1GdQ31u__JDx_FibzL3L | t.rp7mm468mnab | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-066 | https://docs.google.com/document/d/1u1GdQ31u__JDx_FibzL3LaDb-_bjyWKj0h9NPac... | Google Doc | 1u1GdQ31u__JDx_FibzL3L | t.tcwtbmka1b4h | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-067 | https://docs.google.com/document/d/1vJW8RrM8KjbKhkuB7E2HoEfN-WYkLZw5Q9KrhU9... | Google Doc | 1vJW8RrM8KjbKhkuB7E2Ho | t.0 | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-068 | https://docs.google.com/document/d/1vJW8RrM8KjbKhkuB7E2HoEfN-WYkLZw5Q9KrhU9... | Google Doc | 1vJW8RrM8KjbKhkuB7E2Ho | t.9jn6osq0jm0a | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-069 | https://docs.google.com/document/d/1vJW8RrM8KjbKhkuB7E2HoEfN-WYkLZw5Q9KrhU9... | Google Doc | 1vJW8RrM8KjbKhkuB7E2Ho | t.fjpiqd9a2ifb | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-070 | https://docs.google.com/document/d/1xJuYP8Nr0tlJAFBPHqQzb2Gkmufl8eG3Tdv-adY... | Google Doc | 1xJuYP8Nr0tlJAFBPHqQzb | t.pugcy46u0f48 | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-071 | https://docs.google.com/document/d/1xJuYP8Nr0tlJAFBPHqQzb2Gkmufl8eG3Tdv-adY... | Google Doc | 1xJuYP8Nr0tlJAFBPHqQzb | t.qvfk0wepkncs | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-072 | https://docs.google.com/document/d/1xJuYP8Nr0tlJAFBPHqQzb2Gkmufl8eG3Tdv-adY... | Google Doc | 1xJuYP8Nr0tlJAFBPHqQzb | t.smzjndxqtuve | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-073 | https://docs.google.com/document/d/1zO4-DU1N2uV2ULVKhDoYcqWJyookJP_6dEcW4N0... | Google Doc | 1zO4-DU1N2uV2ULVKhDoYc |  | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-074 | https://docs.google.com/spreadsheets/d/1l-Q42fB-f9UWCIYcGYeZ_YaIwF_IKDTTqhF... | Google Sheet | 1l-Q42fB-f9UWCIYcGYeZ_ |  | Copied/imported file exists but needs extraction or conversion | Yes | P1 High |
| URL-075 | https://docs.moodle.org/500/en/Grade_hiding | External link |  |  | External reference only | Maybe | P3 Low |
| URL-076 | https://drive.google.com/drive/folders/1cyDJYkaXaQxVQLlMERJ7DEDLX9AiTGni?us... | Google Drive folder | 1cyDJYkaXaQxVQLlMERJ7D |  | Folder was found but not copied because folder copying was disabled | Yes | P1 High |
| URL-077 | https://drive.google.com/file/d/10JWvptJKknHmS7m-n361bE8k9vKmlsIH/view?usp=... | Google Drive file | 10JWvptJKknHmS7m-n361b |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-078 | https://drive.google.com/file/d/10JWvptJKknHmS7m-n361bE8k9vKmlsIH/view?usp=... | Google Drive file | 10JWvptJKknHmS7m-n361b |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-079 | https://drive.google.com/file/d/11VQ-Kvx1EVJF1lHfn9bc78Ego2D81mPw/view?usp=... | Google Drive file | 11VQ-Kvx1EVJF1lHfn9bc7 |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-080 | https://drive.google.com/file/d/138aKYcs0souubNtX7xhrD8tSZuHiwQSQ/view?usp=... | Google Drive file | 138aKYcs0souubNtX7xhrD |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-081 | https://drive.google.com/file/d/15UAOZGj0BPfLJqCVSjBAq7RneIYpcAgF/view?usp=... | Google Drive file | 15UAOZGj0BPfLJqCVSjBAq |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-082 | https://drive.google.com/file/d/15m2D8dBNGxkoVzf_zcJay00AdB6JbI99/view?usp=... | Google Drive file | 15m2D8dBNGxkoVzf_zcJay |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-083 | https://drive.google.com/file/d/16FUX7666tfiJHPEIwgiQalQ4d2LsYNWT/view?usp=... | Google Drive file | 16FUX7666tfiJHPEIwgiQa |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-084 | https://drive.google.com/file/d/17DbGGTUItN7vRqBvq1Lr2JzfWxtjX4L9/view?usp=... | Google Drive file | 17DbGGTUItN7vRqBvq1Lr2 |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-085 | https://drive.google.com/file/d/17hzvd-vUpmZEEbQwKPitnCqz7yYGQ2x-/view?usp=... | Google Drive file | 17hzvd-vUpmZEEbQwKPitn |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-086 | https://drive.google.com/file/d/19X-cAC7GxByuG4d29GyqdpJskLngBolV/view?usp=... | Google Drive file | 19X-cAC7GxByuG4d29Gyqd |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-087 | https://drive.google.com/file/d/19X-cAC7GxByuG4d29GyqdpJskLngBolV/view?usp=... | Google Drive file | 19X-cAC7GxByuG4d29Gyqd |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-088 | https://drive.google.com/file/d/1B9JjyYPOYZnSW_zF2pp73H-L5SfUfwTo/view?usp=... | Google Drive file | 1B9JjyYPOYZnSW_zF2pp73 |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-089 | https://drive.google.com/file/d/1BLAAo1BuMhx77VHEcki5bJBHmiv-_3S9/view?usp=... | Google Drive file | 1BLAAo1BuMhx77VHEcki5b |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-090 | https://drive.google.com/file/d/1CGDbCREHJZlgCHhaRqH7Q2JQ-1Qq6E4W/view?usp=... | Google Drive file | 1CGDbCREHJZlgCHhaRqH7Q |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-091 | https://drive.google.com/file/d/1D6d-NSQKz4Cb_8yLcBZHbk12SiGZ_bJg/view?usp=... | Google Drive file | 1D6d-NSQKz4Cb_8yLcBZHb |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-092 | https://drive.google.com/file/d/1DTEwssb194rZAMe4f6RsPAAmXPP1bnrw/view?usp=... | Google Drive file | 1DTEwssb194rZAMe4f6RsP |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-093 | https://drive.google.com/file/d/1DTEwssb194rZAMe4f6RsPAAmXPP1bnrw/view?usp=... | Google Drive file | 1DTEwssb194rZAMe4f6RsP |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-094 | https://drive.google.com/file/d/1Dc5GoP4VDyGYhFnYAqGGGAMEgZAdPm80/view?usp=... | Google Drive file | 1Dc5GoP4VDyGYhFnYAqGGG |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-095 | https://drive.google.com/file/d/1Dc5GoP4VDyGYhFnYAqGGGAMEgZAdPm80/view?usp=... | Google Drive file | 1Dc5GoP4VDyGYhFnYAqGGG |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-096 | https://drive.google.com/file/d/1EiV0ZWvTGAwD6dR7QsHnHikRKisQgtVo/view?usp=... | Google Drive file | 1EiV0ZWvTGAwD6dR7QsHnH |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-097 | https://drive.google.com/file/d/1FfjG-bqgRCnj52F6mP-NReI3ZB7cKlpX/view?usp=... | Google Drive file | 1FfjG-bqgRCnj52F6mP-NR |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-098 | https://drive.google.com/file/d/1HKz1WgV90INNVHTgi_3jdArS-vrXBsYD/view?usp=... | Google Drive file | 1HKz1WgV90INNVHTgi_3jd |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-099 | https://drive.google.com/file/d/1JRUbhXs8y-2a5Gu71WTl9bEyhKfyaxd-/view?usp=... | Google Drive file | 1JRUbhXs8y-2a5Gu71WTl9 |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-100 | https://drive.google.com/file/d/1Jaiwn8X-DdD0JR1GvXvYsIw7_iV3JpwE/view?usp=... | Google Drive file | 1Jaiwn8X-DdD0JR1GvXvYs |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-101 | https://drive.google.com/file/d/1LxOHldGeix950JVxR4jchP9Dd2elg4Gt/view?usp=... | Google Drive file | 1LxOHldGeix950JVxR4jch |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-102 | https://drive.google.com/file/d/1M-TAvXPYta8KpIZtCMsKiR9PXXmPwSGB/view?usp=... | Google Drive file | 1M-TAvXPYta8KpIZtCMsKi |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-103 | https://drive.google.com/file/d/1M-TAvXPYta8KpIZtCMsKiR9PXXmPwSGB/view?usp=... | Google Drive file | 1M-TAvXPYta8KpIZtCMsKi |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-104 | https://drive.google.com/file/d/1NkfXp4e1GY5wqwltNT5muWty2Teq9t9y/view?usp=... | Google Drive file | 1NkfXp4e1GY5wqwltNT5mu |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-105 | https://drive.google.com/file/d/1P9_UlVFp70gBg67ML9Adk6kseCgz2V4W/view?usp=... | Google Drive file | 1P9_UlVFp70gBg67ML9Adk |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-106 | https://drive.google.com/file/d/1PdTCJNd0VGeyRgkxqMGwLsqkZQJaS53Z/view?usp=... | Google Drive file | 1PdTCJNd0VGeyRgkxqMGwL |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-107 | https://drive.google.com/file/d/1PdTCJNd0VGeyRgkxqMGwLsqkZQJaS53Z/view?usp=... | Google Drive file | 1PdTCJNd0VGeyRgkxqMGwL |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-108 | https://drive.google.com/file/d/1PlAgQMGuQAmOdxAUChoZnenbloa9W-5X/view?usp=... | Google Drive file | 1PlAgQMGuQAmOdxAUChoZn |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-109 | https://drive.google.com/file/d/1Q1aOELWgW_aUploZFvxZ1VL13mZ_oWt5/view?usp=... | Google Drive file | 1Q1aOELWgW_aUploZFvxZ1 |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-110 | https://drive.google.com/file/d/1QSN9Y07Yc3NG4S-VmXZLU01vXuY0802T/view?usp=... | Google Drive file | 1QSN9Y07Yc3NG4S-VmXZLU |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-111 | https://drive.google.com/file/d/1QiPgt5yCKt2faGVaR-6l_c1nATK8m6T-/view?usp=... | Google Drive file | 1QiPgt5yCKt2faGVaR-6l_ |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-112 | https://drive.google.com/file/d/1ROzQHsWC5yROZp44roDvfsVyYFWDRyJQ/view?usp=... | Google Drive file | 1ROzQHsWC5yROZp44roDvf |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-113 | https://drive.google.com/file/d/1RSiZNXtvyi5zUc8zgVaKT0wlLxOqKrPh/view?usp=... | Google Drive file | 1RSiZNXtvyi5zUc8zgVaKT |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-114 | https://drive.google.com/file/d/1RhQfGcFbrJ01im4kRAHICy4Ia2yfUu4F/view?usp=... | Google Drive file | 1RhQfGcFbrJ01im4kRAHIC |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-115 | https://drive.google.com/file/d/1SCadMh7_JA6q7P7euJLNmbdzmMDt1MTb/view?usp=... | Google Drive file | 1SCadMh7_JA6q7P7euJLNm |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-116 | https://drive.google.com/file/d/1TOHQR_DsHe6bHlHN7ZYJqA9d81UNiJgN/view?usp=... | Google Drive file | 1TOHQR_DsHe6bHlHN7ZYJq |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-117 | https://drive.google.com/file/d/1V2z3AFIcY3R_uMEIl3Peb098kYOK1IR-/view?usp=... | Google Drive file | 1V2z3AFIcY3R_uMEIl3Peb |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-118 | https://drive.google.com/file/d/1W-JJuykteCH0meaBZdg5YlXKsii1iB5K/view?usp=... | Google Drive file | 1W-JJuykteCH0meaBZdg5Y |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-119 | https://drive.google.com/file/d/1XpEFDbuinrHg2TDyBrcHD0AN_i4krkpA/view?usp=... | Google Drive file | 1XpEFDbuinrHg2TDyBrcHD |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-120 | https://drive.google.com/file/d/1XpEFDbuinrHg2TDyBrcHD0AN_i4krkpA/view?usp=... | Google Drive file | 1XpEFDbuinrHg2TDyBrcHD |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-121 | https://drive.google.com/file/d/1XtKr2ASDVFGfFMRyFrc-LMC9dJvd4v46/view?usp=... | Google Drive file | 1XtKr2ASDVFGfFMRyFrc-L |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-122 | https://drive.google.com/file/d/1XtKr2ASDVFGfFMRyFrc-LMC9dJvd4v46/view?usp=... | Google Drive file | 1XtKr2ASDVFGfFMRyFrc-L |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-123 | https://drive.google.com/file/d/1Yk3wAiiZZDGAX23k2MgGjbriida85fYG/view?usp=... | Google Drive file | 1Yk3wAiiZZDGAX23k2MgGj |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-124 | https://drive.google.com/file/d/1ZGdwYv4xVTIiRLMfFd5GgnV3PkATbcLN/view?usp=... | Google Drive file | 1ZGdwYv4xVTIiRLMfFd5Gg |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-125 | https://drive.google.com/file/d/1ZSR9EID-IX3z0ttP64e1hZyAY9ZdtI9D/view?usp=... | Google Drive file | 1ZSR9EID-IX3z0ttP64e1h |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-126 | https://drive.google.com/file/d/1_7wvYCbxEvA7v_uOnTxXOwE_ZnHVs1zU/view?usp=... | Google Drive file | 1_7wvYCbxEvA7v_uOnTxXO |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-127 | https://drive.google.com/file/d/1_Zjzz6n6lyq-WuYy8Ode6tWQA7FoR9Dc/view?usp=... | Google Drive file | 1_Zjzz6n6lyq-WuYy8Ode6 |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-128 | https://drive.google.com/file/d/1aHFRYdpKSuM7aB_9XAEbWtogkD70x-h4/view?usp=... | Google Drive file | 1aHFRYdpKSuM7aB_9XAEbW |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-129 | https://drive.google.com/file/d/1bdGeAcD9ihjejnJ56FIGgzxvm7bIdgah/view?usp=... | Google Drive file | 1bdGeAcD9ihjejnJ56FIGg |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-130 | https://drive.google.com/file/d/1bhFKJ3Mub01Yh9bdhtIHXOo6tG5xTS8Q/view?usp=... | Google Drive file | 1bhFKJ3Mub01Yh9bdhtIHX |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-131 | https://drive.google.com/file/d/1bw2whsd6O5pMdZqCOgVQxDd4hNPEoB-v/view?usp=... | Google Drive file | 1bw2whsd6O5pMdZqCOgVQx |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-132 | https://drive.google.com/file/d/1cIZqiovDO-LcK-8uvWsmjVXLfXSbSZa4/view?usp=... | Google Drive file | 1cIZqiovDO-LcK-8uvWsmj |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-133 | https://drive.google.com/file/d/1cktrciiRdZQzV-sA1LHs_qXtim_fFKDg/view?usp=... | Google Drive file | 1cktrciiRdZQzV-sA1LHs_ |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-134 | https://drive.google.com/file/d/1dxhGGg_3126kl0hrMQrf_QdgXui4KdK7/view?usp=... | Google Drive file | 1dxhGGg_3126kl0hrMQrf_ |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-135 | https://drive.google.com/file/d/1dxhGGg_3126kl0hrMQrf_QdgXui4KdK7/view?usp=... | Google Drive file | 1dxhGGg_3126kl0hrMQrf_ |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-136 | https://drive.google.com/file/d/1eRAoboxZh815OMMt9682lzuI4CLOlloO/view?usp=... | Google Drive file | 1eRAoboxZh815OMMt9682l |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-137 | https://drive.google.com/file/d/1enLDd1Rx4tNYF5Fz4FV0btXQkyvdjLdJ/view?usp=... | Google Drive file | 1enLDd1Rx4tNYF5Fz4FV0b |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-138 | https://drive.google.com/file/d/1enLDd1Rx4tNYF5Fz4FV0btXQkyvdjLdJ/view?usp=... | Google Drive file | 1enLDd1Rx4tNYF5Fz4FV0b |  | Duplicate URL or same source document with different tab/anchor | No | P3 Low |
| URL-139 | https://drive.google.com/file/d/1firsvTipcO5A1dgs2YTsq_6UsV4ZlTLV/view?usp=... | Google Drive file | 1firsvTipcO5A1dgs2YTsq |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-140 | https://drive.google.com/file/d/1gWvKPPjAYQjn_YwjP-_B3q7riueefezY/view?usp=... | Google Drive file | 1gWvKPPjAYQjn_YwjP-_B3 |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-141 | https://drive.google.com/file/d/1g_xmw1crGNXmvA3cG76Y8dB6c616b70Y/view?usp=... | Google Drive file | 1g_xmw1crGNXmvA3cG76Y8 |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-142 | https://drive.google.com/file/d/1j7pyb6iL1ZDXmqq_R3Lu7uTsmxqPRg4R/view?usp=... | Google Drive file | 1j7pyb6iL1ZDXmqq_R3Lu7 |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-143 | https://drive.google.com/file/d/1jpgBpZB56-LNQD75p0AvtpAZHi7XTmAx/view?usp=... | Google Drive file | 1jpgBpZB56-LNQD75p0Avt |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-144 | https://drive.google.com/file/d/1lMYz3sAMxdj_IVHG2IpS_8LGcZsvy3oS/view?usp=... | Google Drive file | 1lMYz3sAMxdj_IVHG2IpS_ |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-145 | https://drive.google.com/file/d/1lpbawCo9zmyYkSuq8zvMjz6ETYNkjPtj/view?usp=... | Google Drive file | 1lpbawCo9zmyYkSuq8zvMj |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-146 | https://drive.google.com/file/d/1m3zq9vhc5rF6WVYoz2MhQw1O46eihdXt/view?usp=... | Google Drive file | 1m3zq9vhc5rF6WVYoz2MhQ |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-147 | https://drive.google.com/file/d/1mMy-CYXxo9U1Kdv22d04OJHR9mCYvn3e/view?usp=... | Google Drive file | 1mMy-CYXxo9U1Kdv22d04O |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-148 | https://drive.google.com/file/d/1pA2NRbc6kvdEu7ms8LPnDFjTB48d9ngx/view?usp=... | Google Drive file | 1pA2NRbc6kvdEu7ms8LPnD |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-149 | https://drive.google.com/file/d/1pcbJZ1TjurVKgZfSk_NevtY9jqXwNLgM/view?usp=... | Google Drive file | 1pcbJZ1TjurVKgZfSk_Nev |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-150 | https://drive.google.com/file/d/1rV_L4FnKn7MH3Yu91c__o9-8RYklFbqF/view?usp=... | Google Drive file | 1rV_L4FnKn7MH3Yu91c__o |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-151 | https://drive.google.com/file/d/1tL55ld9MA-5KfRnKlnKeAuYza6Bbr_lW/view?usp=... | Google Drive file | 1tL55ld9MA-5KfRnKlnKeA |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-152 | https://drive.google.com/file/d/1tSLunhlkRfdzxqvC0iJYB5BbAS6wObCk/view?usp=... | Google Drive file | 1tSLunhlkRfdzxqvC0iJYB |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-153 | https://drive.google.com/file/d/1thct5_HqxZ00gZLZfZG9hDaMyKLxMMm8/view?usp=... | Google Drive file | 1thct5_HqxZ00gZLZfZG9h |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-154 | https://drive.google.com/file/d/1vC4nuiuNhvmoxIbuuK9mO3zw5TZLth_z/view?usp=... | Google Drive file | 1vC4nuiuNhvmoxIbuuK9mO |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-155 | https://drive.google.com/file/d/1w0lkIZ93JZYy3fixHN8nepni0mF3-tCp/view?usp=... | Google Drive file | 1w0lkIZ93JZYy3fixHN8ne |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-156 | https://drive.google.com/file/d/1xEWTAvkT0hba5ILTuyPPpRMKJXgUZRm1/view?usp=... | Google Drive file | 1xEWTAvkT0hba5ILTuyPPp |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-157 | https://drive.google.com/file/d/1xkZRCW-MjOUiFmmCEHvDly6PiVBLzFAY/view?usp=... | Google Drive file | 1xkZRCW-MjOUiFmmCEHvDl |  | Copied/imported document exists and is mapped | No | P3 Low |
| URL-158 | https://drive.google.com/file/d/1ytdG7bYcYPkaMbxy8gdmHIBDEa6ZhT0c/view?usp=... | Google Drive file | 1ytdG7bYcYPkaMbxy8gdmH |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-159 | https://drive.google.com/file/d/1zUEuTcodzkWRfl_-ByeQdDvMqLIv7t_f/view?usp=... | Google Drive file | 1zUEuTcodzkWRfl_-ByeQd |  | Video was skipped because video copying was disabled | Yes | P2 High |
| URL-160 | https://learn.ciinstituteofnursing.com/course/view.php?id=13 | External link |  |  | External reference only | Maybe | P3 Low |
| URL-161 | https://maps.app.goo.gl/LmiigtC8X9zLTYy77 | External link |  |  | External reference only | Maybe | P3 Low |
| URL-162 | https://www.figma.com/board/KD7E72xfOhD6DdsCIYnLvx/CI-ION-User-Flows?node-i... | External link |  |  | External reference only | Maybe | P3 Low |
