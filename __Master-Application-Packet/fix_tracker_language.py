#!/usr/bin/env python3
"""
Targeted language cleanup for the 3 CI-ION missing/pending tracker PDFs.
Removes the word "owner" from the defensive sentence on page 2.
This makes a visible content change to the end-user PDFs.
Run from anywhere; paths are relative to the known redesigned folder.
"""

from __future__ import annotations

import fitz
from pathlib import Path

BASE = Path(r"__Master-Application-Packet/GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED")

TRACKERS = [
    "01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/04_CNA_CDPH_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf",
    "02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/04_RCFE_CDSS_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf",
    "03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/04_BRN_CEP_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf",
]

OLD_PHRASE = "owner-assignment"
NEW_SENTENCE = "This page is not an assignment tracker and does not create new build tasks. After handoff, remaining actions are handled through the assigned human review workflow."

def fix_one(rel: str) -> dict:
    p = BASE / rel
    if not p.exists():
        return {"rel": rel, "status": "missing"}

    doc = fitz.open(str(p))
    results = {"rel": rel, "pages": doc.page_count, "edits": []}

    for pi in range(doc.page_count):
        page = doc[pi]
        instances = page.search_for(OLD_PHRASE)
        if not instances:
            continue

        for inst in instances:
            # Expand the rect to cover the full likely sentence line(s)
            # The sentence is long; give generous horizontal and a bit of vertical
            redact_rect = fitz.Rect(
                inst.x0 - 25,
                inst.y0 - 3,
                inst.x0 + 480,   # covers most of the sentence width
                inst.y1 + 4
            )

            # Add redaction (white out)
            page.add_redact_annot(redact_rect, fill=(1, 1, 1))
            page.apply_redactions()

            # Insert the clean sentence.
            # Try to use a reasonable size and dark color to match body text.
            # Position slightly below the top of the redacted area.
            text_point = fitz.Point(redact_rect.x0 + 2, redact_rect.y0 + 9)
            # Use a common font; the page already has Roboto-like but we fall back safely.
            # fontsize ~9-10 matches the small body text in these trackers.
            rc = page.insert_text(
                text_point,
                NEW_SENTENCE,
                fontname="helv",
                fontsize=9.0,
                color=(0.13, 0.13, 0.13),  # dark gray ~ #212121
            )

            results["edits"].append({
                "page": pi + 1,
                "old_rect": str(inst),
                "redact_rect": str(redact_rect),
                "insert_point": str(text_point),
                "insert_rc": rc,
            })

    if results["edits"]:
        # Robust Windows-friendly save: write to temp, fully close, then swap
        import os, time, shutil
        tmp = p.with_name(p.name + ".languagefix.tmp.pdf")
        doc.save(str(tmp), garbage=4, deflate=True)
        doc.close()
        time.sleep(0.3)  # let Windows release any lingering handle
        # Prefer copy + unlink to avoid replace permission issues under locks
        shutil.copy2(str(tmp), str(p))
        os.unlink(str(tmp))
        results["status"] = "fixed"
        return results
    else:
        results["status"] = "no_match"

    doc.close()
    return results


def main():
    print("Applying targeted language cleanup to remove 'owner' word from tracker PDFs...")
    all_results = []
    for rel in TRACKERS:
        res = fix_one(rel)
        all_results.append(res)
        print(res)

    print("\nDone. Summary:")
    for r in all_results:
        print(f"  {r['rel']}: {r['status']} edits={len(r.get('edits', []))}")

if __name__ == "__main__":
    main()
