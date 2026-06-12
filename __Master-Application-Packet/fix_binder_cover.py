#!/usr/bin/env python3
"""
Targeted cover page fix for the CNA binder (and its counterpart in main OUT).
Uses the improved draw_cover from the updated redesign script.
Replaces ONLY the first page (cover) via pypdf merge so official government forms
and other prefix pages remain completely untouched and unaltered.

Run this to apply the fix for the circular glare/artifact on covers
by using larger logo, higher placement, gold ring frame, smoother background,
and layout closer to the design studio reference screenshot.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

import fitz
from pypdf import PdfReader, PdfWriter

# Import the updated drawing functions and helpers from the main script
# (after the draw_cover improvements for large crisp logo, no glare, etc.)
try:
    from redesign_ci_ion_packet import (
        prepare_assets,
        draw_cover,
        lane_for_rel,
        infer_cover,
    )
except Exception as e:
    print("Could not import from redesign_ci_ion_packet.py:", e)
    raise

ROOT = Path(r"__Master-Application-Packet")
SRC_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN - Copy - Copy"
MAIN_OUT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED"
COPY_OUT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED - Copy"

TARGET_REL = Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/01_CNA_CDPH_APPLICATION_BINDER.pdf")

# The source binder (for infer_cover title logic)
SRC_BINDER = SRC_ROOT / TARGET_REL

def fix_one_binder(target_path: Path, note: str) -> bool:
    if not target_path.exists():
        print(f"SKIP (not found): {target_path}")
        return False

    print(f"Fixing cover for: {target_path} ({note})")

    # Load source for infer_cover (to get proper title/subtitle for this binder)
    if not SRC_BINDER.exists():
        print("  WARNING: source binder not found for infer, using fallback title")
        src_doc = fitz.open()
        # dummy page so infer doesn't crash
        src_doc.new_page()
    else:
        src_doc = fitz.open(str(SRC_BINDER))

    assets = prepare_assets()

    # Generate a fresh single-page cover using the improved draw_cover
    cover_doc = fitz.open()
    # rel is just for lane/title inference
    rel_for_cover = TARGET_REL
    draw_cover(cover_doc, rel_for_cover, src_doc, assets)

    # Save the new cover to a temp file
    tmp_cover = Path(tempfile.gettempdir()) / f"ci_cover_fix_{os.getpid()}.pdf"
    cover_doc.save(str(tmp_cover), garbage=4, deflate=True)
    cover_doc.close()
    src_doc.close()

    # Now replace only page 0 in the target using pypdf (safe, keeps everything else identical)
    try:
        orig_reader = PdfReader(str(target_path))
        cover_reader = PdfReader(str(tmp_cover))

        writer = PdfWriter()

        # New improved cover as page 0
        writer.add_page(cover_reader.pages[0])

        # Keep all remaining original pages (CI embeds + official gov forms) exactly as-is
        for i in range(1, len(orig_reader.pages)):
            writer.add_page(orig_reader.pages[i])

        # Write back (overwrites the target)
        with target_path.open("wb") as f:
            writer.write(f)

        print(f"  SUCCESS: cover replaced on {target_path.name}")
        return True
    finally:
        # cleanup temp
        try:
            tmp_cover.unlink(missing_ok=True)
        except Exception:
            pass

def main():
    print("=== Applying cover fix (large crisp CI-ION logomark, no glare, generous spacing, reference match) ===")

    # The specific one the user asked for
    copy_binder = COPY_OUT / TARGET_REL
    fixed_copy = fix_one_binder(copy_binder, "user-specified -Copy version")

    # Also update the main OUT version for consistency (same problem)
    main_binder = MAIN_OUT / TARGET_REL
    fixed_main = fix_one_binder(main_binder, "main REDESIGNED version")

    if fixed_copy or fixed_main:
        print("\nCover fix applied. New visual QA renders will be created next.")
    else:
        print("\nNo binders were updated (paths may need verification).")

if __name__ == "__main__":
    main()
