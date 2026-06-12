from __future__ import annotations

import json
from pathlib import Path

import fitz


OUTPUT_ROOT = Path(r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet\GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED - Copy")
REPORT = OUTPUT_ROOT / "COVER_PREPARED_LINE_CLEANUP_REPORT.json"

OFFICIAL_MARKERS = (
    "OFFICIAL_FORMS_READY_FOR_SIGNATURE",
    "CDPH 192B",
    "CDPH 193",
    "LIC 9140",
    "LIC 9141",
    "Board of Registered Nursing",
    "State of California",
    "Department of Public Health",
    "Department of Social Services",
)


def average_background(page: fitz.Page, rect: fitz.Rect) -> tuple[float, float, float]:
    # Sample just above the text line so the fill matches the cover gradient better than a hard-coded maroon.
    sample = fitz.Rect(rect.x0, max(0, rect.y0 - 12), rect.x1, max(1, rect.y0 - 4))
    pix = page.get_pixmap(clip=sample, colorspace=fitz.csRGB, alpha=False)
    if not pix.samples:
        return (0.18, 0.0, 0.0)
    data = pix.samples
    channels = [0, 0, 0]
    count = 0
    for idx in range(0, len(data), 3):
        channels[0] += data[idx]
        channels[1] += data[idx + 1]
        channels[2] += data[idx + 2]
        count += 1
    return tuple((value / count) / 255 for value in channels) if count else (0.18, 0.0, 0.0)


def should_skip(path: Path, first_page_text: str) -> bool:
    rel = str(path.relative_to(OUTPUT_ROOT))
    haystack = rel + "\n" + first_page_text[:2500]
    return any(marker.lower() in haystack.lower() for marker in OFFICIAL_MARKERS)


def cleanup_pdf(path: Path) -> dict[str, object] | None:
    doc = fitz.open(path)
    try:
        if doc.page_count == 0:
            return None
        page = doc[0]
        text = page.get_text("text")
        if should_skip(path, text) or "TJ PADILLA" not in text.upper():
            return None

        rects = page.search_for("TJ PADILLA")
        prepared_rects = page.search_for("P R E PA R E D")
        if not rects:
            return None

        tj_rect = rects[0]
        if prepared_rects:
            line_rect = prepared_rects[0] | tj_rect
        else:
            line_rect = tj_rect
        line_rect = fitz.Rect(
            max(0, line_rect.x0 - 28),
            max(0, line_rect.y0 - 3),
            min(page.rect.width, line_rect.x1 + 86),
            min(page.rect.height, line_rect.y1 + 4),
        )
        fill = average_background(page, line_rect)
        page.add_redact_annot(line_rect, fill=fill)
        page.apply_redactions()
        replacement = "PREPARED FOR YADVIR SAANDAL · JUNE 9, 2026"
        page.insert_textbox(
            line_rect,
            replacement,
            fontsize=7.0,
            fontname="helv",
            color=(0.72, 0.72, 0.72),
            align=fitz.TEXT_ALIGN_CENTER,
        )
        temp = path.with_suffix(".cover-clean.tmp.pdf")
        doc.save(temp, garbage=4, deflate=True)
    finally:
        doc.close()
    temp.replace(path)
    return {"rel": str(path.relative_to(OUTPUT_ROOT)), "page": 1}


def main() -> None:
    changed = []
    for path in sorted(OUTPUT_ROOT.rglob("*.pdf")):
        result = cleanup_pdf(path)
        if result:
            changed.append(result)
    REPORT.write_text(json.dumps({"changed_count": len(changed), "changed": changed}, indent=2), encoding="utf-8")
    print(json.dumps({"changed_count": len(changed), "report": str(REPORT)}, separators=(",", ":")))


if __name__ == "__main__":
    main()
