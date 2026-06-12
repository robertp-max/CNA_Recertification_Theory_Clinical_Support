from __future__ import annotations

import json
from io import BytesIO
from pathlib import Path

import fitz
from PIL import Image


OUTPUT_ROOT = Path(r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet\GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED - Copy")
REPORT = OUTPUT_ROOT / "COVER_PREPARED_LINE_REMOVED_VISUAL_REPORT.json"


def background_patch(page: fitz.Page, rect: fitz.Rect, zoom: int = 3) -> bytes:
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), colorspace=fitz.csRGB, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    x0 = max(0, int(rect.x0 * zoom))
    y0 = max(0, int(rect.y0 * zoom))
    x1 = min(pix.width, int(rect.x1 * zoom))
    y1 = min(pix.height, int(rect.y1 * zoom))
    width = x1 - x0
    height = y1 - y0
    patch = Image.new("RGB", (width, height))
    top_y = max(0, y0 - 14 * zoom)
    bottom_y = min(pix.height - 1, y1 + 14 * zoom)
    top = [img.getpixel((x, top_y)) for x in range(x0, x1)]
    bottom = [img.getpixel((x, bottom_y)) for x in range(x0, x1)]
    for y in range(height):
        t = y / max(1, height - 1)
        for x in range(width):
            patch.putpixel((x, y), tuple(int(top[x][c] * (1 - t) + bottom[x][c] * t) for c in range(3)))
    buffer = BytesIO()
    patch.save(buffer, format="PNG")
    return buffer.getvalue()


def clean(path: Path) -> dict[str, object] | None:
    doc = fitz.open(path)
    try:
        if doc.page_count == 0:
            return None
        page = doc[0]
        text = page.get_text("text").upper()
        if "YADVIR SAANDAL" not in text and "TJ PADILLA" not in text:
            return None
        rect = fitz.Rect(190, 564, 422, 586)
        page.insert_image(rect, stream=background_patch(page, rect), overlay=True)
        temp = path.with_suffix(".cover-line-removed.tmp.pdf")
        doc.save(temp, garbage=4, deflate=True)
    finally:
        doc.close()
    temp.replace(path)
    return {"rel": str(path.relative_to(OUTPUT_ROOT)), "page": 1}


def main() -> None:
    changed = []
    for path in sorted(OUTPUT_ROOT.rglob("*.pdf")):
        result = clean(path)
        if result:
            changed.append(result)
    REPORT.write_text(json.dumps({"changed_count": len(changed), "changed": changed}, indent=2), encoding="utf-8")
    print(json.dumps({"changed_count": len(changed), "report": str(REPORT)}, separators=(",", ":")))


if __name__ == "__main__":
    main()
