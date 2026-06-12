from __future__ import annotations

import json
from io import BytesIO
from pathlib import Path

import fitz
from PIL import Image


OUTPUT_ROOT = Path(r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet\GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED - Copy")
REPORT = OUTPUT_ROOT / "COVER_PREPARED_LINE_SMOOTH_REPORT.json"


def blended_patch(page: fitz.Page, rect: fitz.Rect, zoom: int = 3) -> bytes:
    matrix = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=matrix, colorspace=fitz.csRGB, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    x0 = max(0, int(rect.x0 * zoom))
    y0 = max(0, int(rect.y0 * zoom))
    x1 = min(pix.width, int(rect.x1 * zoom))
    y1 = min(pix.height, int(rect.y1 * zoom))
    width = x1 - x0
    height = y1 - y0
    patch = Image.new("RGB", (width, height))
    top_y = max(0, y0 - 10 * zoom)
    bottom_y = min(pix.height - 1, y1 + 10 * zoom)
    top = [img.getpixel((x, top_y)) for x in range(x0, x1)]
    bottom = [img.getpixel((x, bottom_y)) for x in range(x0, x1)]
    for y in range(height):
        t = y / max(1, height - 1)
        for x in range(width):
            rgb = tuple(int(top[x][channel] * (1 - t) + bottom[x][channel] * t) for channel in range(3))
            patch.putpixel((x, y), rgb)
    buffer = BytesIO()
    patch.save(buffer, format="PNG")
    return buffer.getvalue()


def smooth_pdf(path: Path) -> dict[str, object] | None:
    doc = fitz.open(path)
    try:
        if doc.page_count == 0:
            return None
        page = doc[0]
        text = page.get_text("text")
        if "YADVIR SAANDAL" not in text.upper() or "PREPARED FOR" not in text.upper():
            return None
        rects = page.search_for("YADVIR SAANDAL")
        if not rects:
            return None
        rect = rects[0]
        line_rect = fitz.Rect(
            max(0, rect.x0 - 66),
            max(0, rect.y0 - 3),
            min(page.rect.width, rect.x1 + 40),
            min(page.rect.height, rect.y1 + 4),
        )
        png = blended_patch(page, line_rect)
        page.insert_image(line_rect, stream=png, overlay=True)
        page.insert_textbox(
            line_rect,
            "PREPARED FOR YADVIR SAANDAL · JUNE 9, 2026",
            fontsize=7.0,
            fontname="helv",
            color=(0.72, 0.72, 0.72),
            align=fitz.TEXT_ALIGN_CENTER,
            overlay=True,
        )
        temp = path.with_suffix(".cover-smooth.tmp.pdf")
        doc.save(temp, garbage=4, deflate=True)
    finally:
        doc.close()
    temp.replace(path)
    return {"rel": str(path.relative_to(OUTPUT_ROOT)), "page": 1}


def main() -> None:
    changed = []
    for path in sorted(OUTPUT_ROOT.rglob("*.pdf")):
        result = smooth_pdf(path)
        if result:
            changed.append(result)
    REPORT.write_text(json.dumps({"changed_count": len(changed), "changed": changed}, indent=2), encoding="utf-8")
    print(json.dumps({"changed_count": len(changed), "report": str(REPORT)}, separators=(",", ":")))


if __name__ == "__main__":
    main()
