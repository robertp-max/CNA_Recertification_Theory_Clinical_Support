from __future__ import annotations

import hashlib
import json
import re
import tempfile
import urllib.request
from pathlib import Path

import fitz
from PIL import Image
from pypdf import PdfReader, PdfWriter


ROOT = Path(r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet")
SRC = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN - Copy - Copy"
OUT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED"
TARGET_REL = Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf")
OFFICIAL_REL = Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/03_CNA_CDPH_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf")

TARGET = OUT / TARGET_REL
SOURCE_CI = SRC / TARGET_REL
OFFICIAL_SRC = SRC / OFFICIAL_REL
TEMP_TARGET = TARGET.with_suffix(".studio-refit.tmp.pdf")
QA_DIR = Path(tempfile.gettempdir()) / "ci_ion_cna_minimum_studio_refit_qa"

LOGOMARK_WHITE_URL = "https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg"
ROBOTO_CSS_URL = "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap"

LETTER_W = 612
LETTER_H = 792

MAROON = (0x8B / 255, 0x15 / 255, 0x15 / 255)
MAROON_DEEP = (0x61 / 255, 0, 0)
MAROON_BLACK = (0x26 / 255, 0, 0)
MAROON_DARKER = (0x3D / 255, 0, 0)
GOLD = (0xFF / 255, 0xC1 / 255, 0x07 / 255)
GOLD_DARK = (0xD4 / 255, 0xAF / 255, 0x37 / 255)
CREAM = (0xFD / 255, 0xFC / 255, 0xF7 / 255)
TEXT = (0x21 / 255, 0x25 / 255, 0x29 / 255)
MUTED = (0x6C / 255, 0x75 / 255, 0x7D / 255)
LIGHT_LINE = (0xE6 / 255, 0xE0 / 255, 0xD7 / 255)
TABLE_LINE = (0xDD / 255, 0xD4 / 255, 0xCA / 255)
ROW_TINT = (0xFC / 255, 0xF4 / 255, 0xF1 / 255)
NOTE_FILL = (1.0, 0xFA / 255, 0xE8 / 255)


def fail(message: str) -> None:
    raise RuntimeError(message)


def request_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def assets() -> dict[str, object]:
    asset_dir = Path(tempfile.gettempdir()) / "ci_ion_pdf_assets"
    asset_dir.mkdir(parents=True, exist_ok=True)

    css = request_bytes(ROBOTO_CSS_URL).decode("utf-8", errors="replace")
    font_urls = re.findall(r"url\((https://[^)]+)\)", css)
    if len(font_urls) < 5:
        fail("Roboto font URLs were not available from Google Fonts.")

    font_paths: dict[str, Path] = {}
    # Google returns the requested weights in order: 300, 400, 500, 600, 700.
    for name, url in zip(["RobotoLight", "RobotoRegular", "RobotoMedium", "RobotoSemi", "RobotoBold"], font_urls):
        path = asset_dir / f"{name}.ttf"
        if not path.exists():
            path.write_bytes(request_bytes(url))
        font_paths[name] = path

    logo_svg = request_bytes(LOGOMARK_WHITE_URL)
    logo_doc = fitz.open(stream=logo_svg, filetype="svg")
    logo_pix = logo_doc[0].get_pixmap(matrix=fitz.Matrix(5, 5), alpha=True)
    logo_doc.close()

    return {"fonts": font_paths, "logo": logo_pix}


def put_fonts(page: fitz.Page, a: dict[str, object]) -> None:
    fonts: dict[str, Path] = a["fonts"]  # type: ignore[assignment]
    for name, path in fonts.items():
        page.insert_font(fontname=name, fontfile=str(path))


def text_box(
    page: fitz.Page,
    rect: fitz.Rect,
    text: str,
    font: str,
    size: float,
    color: tuple[float, float, float],
    align: int = fitz.TEXT_ALIGN_LEFT,
    min_size: float = 5.5,
    lineheight: float | None = None,
) -> None:
    current = size
    while current >= min_size:
        rc = page.insert_textbox(
            rect,
            text,
            fontname=font,
            fontsize=current,
            color=color,
            align=align,
            lineheight=lineheight,
        )
        if rc >= 0:
            return
        current -= 0.4
    page.insert_textbox(rect, text, fontname=font, fontsize=min_size, color=color, align=align)


def draw_radial_maroon(page: fitz.Page, center_y: float = 276) -> None:
    cache = Path(tempfile.gettempdir()) / f"ci_ion_smooth_maroon_{int(center_y)}.png"
    if not cache.exists():
        scale = 2
        w = int(LETTER_W * scale)
        h = int(LETTER_H * scale)
        cx = 0.5 * w
        cy = (center_y / LETTER_H) * h
        max_dist = ((max(cx, w - cx) ** 2 + max(cy, h - cy) ** 2) ** 0.5)
        center = (0x8B, 0x15, 0x15)
        mid = (0x5B, 0x00, 0x00)
        edge = (0x26, 0x00, 0x00)
        img = Image.new("RGB", (w, h))
        px = img.load()
        for y in range(h):
            for x in range(w):
                d = (((x - cx) ** 2 + (y - cy) ** 2) ** 0.5) / max_dist
                d = min(1.0, max(0.0, d))
                if d < 0.42:
                    t = d / 0.42
                    c = tuple(int(center[i] * (1 - t) + mid[i] * t) for i in range(3))
                else:
                    t = (d - 0.42) / 0.58
                    c = tuple(int(mid[i] * (1 - t) + edge[i] * t) for i in range(3))
                px[x, y] = c
        cache.parent.mkdir(parents=True, exist_ok=True)
        img.save(cache, optimize=True)
    page.insert_image(page.rect, filename=str(cache))


def draw_studio_frame(page: fitz.Page) -> None:
    outer = fitz.Rect(16, 16, LETTER_W - 16, LETTER_H - 16)
    inner = fitz.Rect(21.25, 21.25, LETTER_W - 21.25, LETTER_H - 21.25)
    page.draw_rect(outer, color=GOLD, width=1.8)
    page.draw_rect(inner, color=GOLD_DARK, width=0.65)
    block = 41.8
    offset = 21
    for sx, sy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        x = offset if sx == 1 else LETTER_W - offset
        y = offset if sy == 1 else LETTER_H - offset
        page.draw_line((x, y), (x + sx * block, y), color=GOLD, width=1.6)
        page.draw_line((x, y), (x, y + sy * block), color=GOLD, width=1.6)
        for n in range(3):
            step = 7 + n * 7
            line_len = 23 - n * 6
            page.draw_line((x + sx * step, y + sy * step), (x + sx * (step + line_len), y + sy * step), color=GOLD, width=0.75)
            page.draw_line((x + sx * step, y + sy * step), (x + sx * step, y + sy * (step + line_len)), color=GOLD, width=0.75)


def vertical_label(page: fitz.Page, text: str, x: float, y0: float, y1: float, rotate: int) -> None:
    # PyMuPDF text rotation is page-axis based; use a narrow textbox for studio-like side labels.
    rect = fitz.Rect(x - 8, y0, x + 8, y1)
    page.insert_textbox(
        rect,
        text.upper(),
        fontname="RobotoMedium",
        fontsize=6.2,
        color=GOLD_DARK,
        align=fitz.TEXT_ALIGN_CENTER,
        rotate=rotate,
        morph=None,
    )


def studio_cover(doc: fitz.Document, a: dict[str, object]) -> None:
    page = doc.new_page(width=LETTER_W, height=LETTER_H)
    put_fonts(page, a)
    draw_radial_maroon(page)
    draw_studio_frame(page)

    vertical_label(page, "CNA / CDPH SUBMISSION PACKET", 38, 110, 682, 90)
    vertical_label(page, "DRAFT / PENDING CDPH APPROVAL", LETTER_W - 38, 110, 682, 270)

    page.insert_image(fitz.Rect(200, 78, 412, 290), pixmap=a["logo"], keep_proportion=True)
    text_box(page, fitz.Rect(86, 318, 526, 345), "CALIFORNIA", "RobotoLight", 15.5, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    text_box(page, fitz.Rect(72, 355, 540, 396), "CNA / CDPH MINIMUM REQUIRED", "RobotoLight", 25.5, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    text_box(page, fitz.Rect(82, 407, 530, 432), "SUBMISSION PACKET", "RobotoSemi", 14.5, GOLD, fitz.TEXT_ALIGN_CENTER)
    text_box(page, fitz.Rect(82, 434, 530, 454), "ONLINE CE - SIGNER-REVIEW BINDER", "RobotoRegular", 9.5, (0.86, 0.86, 0.86), fitz.TEXT_ALIGN_CENTER)

    y = 470
    text_box(page, fitz.Rect(108, y, 504, y + 18), "24 Online CE Hours    |    12 Units x 2 Hours    |    Source Backbone: CCCCO/NATP 10-17", "RobotoRegular", 7.6, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    text_box(page, fitz.Rect(118, y + 15, 494, y + 31), "CCCCO / NATP SOURCE BACKBONE - LEARNER-FACING STRUCTURE REMAINS U01-U12", "RobotoLight", 6.3, (0.72, 0.72, 0.72), fitz.TEXT_ALIGN_CENTER)

    page.draw_line((105, 520), (292, 520), color=GOLD_DARK, width=0.7)
    page.draw_rect(fitz.Rect(303, 516.5, 309, 522.5), color=GOLD, fill=GOLD)
    page.draw_line((320, 520), (507, 520), color=GOLD_DARK, width=0.7)

    text_box(page, fitz.Rect(108, 553, 504, 574), "CI Institute of Nursing, Inc.", "RobotoMedium", 10.5, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    text_box(page, fitz.Rect(108, 578, 504, 596), "PREPARED BY TJ PADILLA - JUNE 9, 2026", "RobotoRegular", 7.2, (0.72, 0.72, 0.72), fitz.TEXT_ALIGN_CENTER)

    page.draw_line((108, 665), (176, 665), color=GOLD_DARK, width=0.8)
    page.draw_line((436, 665), (504, 665), color=GOLD_DARK, width=0.8)
    text_box(page, fitz.Rect(180, 653, 432, 675), "STATUS: DRAFT / PENDING CDPH APPROVAL", "RobotoRegular", 10.0, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    text_box(page, fitz.Rect(146, 679, 466, 696), "Ready for verification, signature, and submission review.", "RobotoLight", 7.0, (0.78, 0.78, 0.78), fitz.TEXT_ALIGN_CENTER)
    text_box(
        page,
        fitz.Rect(72, 754, 540, 765),
        "No public approval claim, enrollment for approved credit, or certificate release is authorized until applicable agency approval metadata is issued.",
        "RobotoLight",
        5.1,
        (0.58, 0.58, 0.58),
        fitz.TEXT_ALIGN_CENTER,
    )


def page_header_footer(page: fitz.Page, a: dict[str, object], page_no: int, total: int) -> None:
    put_fonts(page, a)
    page.draw_rect(page.rect, color=CREAM, fill=CREAM)
    page.draw_line((54, 85), (558, 85), color=MAROON, width=1.2)
    text_box(page, fitz.Rect(54, 66, 320, 80), "CNA/CDPH CE SIGNER-REVIEW BINDER", "RobotoBold", 7.5, MAROON, fitz.TEXT_ALIGN_LEFT)
    text_box(page, fitz.Rect(332, 66, 558, 80), "CI INSTITUTE OF NURSING, INC.", "RobotoRegular", 7.0, MUTED, fitz.TEXT_ALIGN_RIGHT)
    page.draw_line((54, 733), (558, 733), color=LIGHT_LINE, width=0.6)
    text_box(page, fitz.Rect(54, 739, 210, 752), "TJ PADILLA - COMPILER", "RobotoRegular", 6.2, MUTED, fitz.TEXT_ALIGN_LEFT)
    text_box(page, fitz.Rect(222, 739, 390, 752), "PREPARED JUNE 09, 2026", "RobotoRegular", 6.2, MUTED, fitz.TEXT_ALIGN_CENTER)
    text_box(page, fitz.Rect(410, 739, 558, 752), f"PAGE {page_no} OF {total}", "RobotoBold", 6.2, MUTED, fitz.TEXT_ALIGN_RIGHT)


def section_title(page: fitz.Page, y: float, title: str) -> float:
    text_box(page, fitz.Rect(54, y, 285, y + 26), title.upper(), "Times-Bold", 17.0, MAROON_DEEP, fitz.TEXT_ALIGN_LEFT)
    page.draw_line((267, y + 11.5), (558, y + 11.5), color=GOLD_DARK, width=0.9)
    return y + 43


def paragraph(page: fitz.Page, y: float, text: str, height: float, size: float = 8.8, bold: bool = False) -> float:
    text_box(page, fitz.Rect(54, y, 558, y + height), text, "RobotoMedium" if bold else "RobotoRegular", size, TEXT, fitz.TEXT_ALIGN_LEFT, lineheight=1.12)
    return y + height + 9


def note_box(page: fitz.Page, y: float, text: str, height: float, accent: tuple[float, float, float] = GOLD) -> float:
    page.draw_rect(fitz.Rect(54, y, 558, y + height), color=NOTE_FILL, fill=NOTE_FILL)
    page.draw_rect(fitz.Rect(54, y, 57.5, y + height), color=accent, fill=accent)
    text_box(page, fitz.Rect(66, y + 8, 548, y + height - 5), text, "RobotoRegular", 7.6, TEXT, fitz.TEXT_ALIGN_LEFT, min_size=6.0, lineheight=1.12)
    return y + height + 14


def draw_table(page: fitz.Page, y: float) -> float:
    headers = ["MINIMUM REQUIRED MATERIAL", "STATUS", "NOTES"]
    rows = [
        ("Compiled CNA/CDPH application binder", "Included or referenced", "Required for current lane"),
        ("CDPH 192B / online CE provider application materials", "Included or referenced", "Required for current lane"),
        ("CDPH 193 / relevant provider/course form materials", "Included or referenced", "Required for current lane"),
        ("Course list and 12-unit / 24-online-hour course structure", "Included or referenced", "Required for current lane"),
        ("Instructor/SME evidence where required", "Included or referenced", "Required for current lane"),
        ("Certificate controls, identity confirmation, interactivity, and final participant statement controls", "Included or referenced", "Required for current lane"),
        ("Official forms ready for signature/date", "Included or referenced", "Required for current lane"),
        ("Reviewer access and final verification checklist", "Included or referenced", "Required for current lane"),
    ]
    x0 = 54
    widths = [236, 142, 126]
    row_h = 24
    header_h = 22
    page.draw_rect(fitz.Rect(x0, y, x0 + sum(widths), y + header_h), color=MAROON_DEEP, fill=MAROON_DEEP)
    cursor = x0
    for i, h in enumerate(headers):
        text_box(page, fitz.Rect(cursor + 8, y + 6, cursor + widths[i] - 6, y + header_h - 2), h, "RobotoBold", 6.9, (1, 1, 1), fitz.TEXT_ALIGN_LEFT)
        if i:
            page.draw_line((cursor, y), (cursor, y + header_h + row_h * len(rows)), color=TABLE_LINE, width=0.45)
        cursor += widths[i]
    y += header_h
    for idx, row in enumerate(rows):
        fill = ROW_TINT if idx % 2 else CREAM
        page.draw_rect(fitz.Rect(x0, y, x0 + sum(widths), y + row_h), color=TABLE_LINE, fill=fill, width=0.45)
        cursor = x0
        for col, cell in enumerate(row):
            font = "RobotoBold" if col == 0 else "RobotoRegular"
            color = MAROON_DEEP if col == 0 else TEXT
            text_box(page, fitz.Rect(cursor + 8, y + 5, cursor + widths[col] - 6, y + row_h - 3), cell, font, 6.9, color, fitz.TEXT_ALIGN_LEFT, min_size=5.8, lineheight=1.05)
            cursor += widths[col]
        y += row_h
    return y + 17


def studio_content_page(doc: fitz.Document, a: dict[str, object]) -> None:
    page = doc.new_page(width=LETTER_W, height=LETTER_H)
    page_header_footer(page, a, 2, 8)
    y = section_title(page, 108, "Minimum Submission Scope")
    y = paragraph(
        page,
        y,
        "CNA 24-hour online CE course using CCCCO/NATP Modules 10-17 as the source backbone, delivered as 12 Moodle units.",
        28,
    )
    y = paragraph(
        page,
        y,
        "This PDF includes the minimum application-submission index and exact official form pages where source PDFs were available. Optional LMS implementation materials, source folders, old module fragments, internal build notes, and raw source files are excluded.",
        42,
    )
    y = note_box(
        page,
        y,
        "Approval-safe posture: Draft / Pending CDPH Approval. Certificate release remains disabled pending approval metadata and completion evidence gates. No public approval claim is made.",
        38,
    )
    text_box(page, fitz.Rect(54, y, 558, y + 18), "Project Submission Materials", "RobotoBold", 10.0, MAROON, fitz.TEXT_ALIGN_LEFT)
    y += 23
    y = draw_table(page, y)
    text_box(page, fitz.Rect(54, y, 558, y + 18), "Official Form Handling", "Times-Bold", 11.5, MAROON_DEEP)
    y = note_box(
        page,
        y + 23,
        "Official government forms appended after this index are preserved as source PDF pages without CI headers, branding, crop, watermark, or restyling. A standalone official forms PDF is also available in the same folder.",
        42,
        accent=MAROON,
    )
    text_box(page, fitz.Rect(54, y, 558, y + 18), "Course Materials", "Times-Bold", 11.5, MAROON_DEEP)
    paragraph(
        page,
        y + 23,
        "Course materials are provided in the lane's 02_COURSE_MATERIALS folder. Do not substitute old one-page module fragments or source folders for the compiled course-materials PDFs and workbooks.",
        34,
        size=7.8,
    )


def studio_appendix_divider(doc: fitz.Document, a: dict[str, object]) -> None:
    page = doc.new_page(width=LETTER_W, height=LETTER_H)
    put_fonts(page, a)
    draw_radial_maroon(page, center_y=380)
    draw_studio_frame(page)
    text_box(page, fitz.Rect(74, 326, 538, 368), "APPENDIX", "Times-Bold", 31.0, GOLD, fitz.TEXT_ALIGN_CENTER)
    text_box(page, fitz.Rect(74, 374, 538, 398), "OFFICIAL FORMS PACKET", "RobotoLight", 13.0, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    text_box(
        page,
        fitz.Rect(96, 426, 516, 492),
        "Official government forms are appended as original unbranded PDF pages. No CI styling, headers, footers, borders, watermarks, page numbers, or visual alterations have been applied.",
        "RobotoRegular",
        9.4,
        (0.86, 0.86, 0.86),
        fitz.TEXT_ALIGN_CENTER,
        lineheight=1.18,
    )


def build_ci_prefix(a: dict[str, object], out_path: Path) -> None:
    doc = fitz.open()
    studio_cover(doc, a)
    studio_content_page(doc, a)
    studio_appendix_divider(doc, a)
    doc.save(out_path, garbage=4, deflate=True, clean=True)
    doc.close()


def merge_with_official(ci_prefix: Path, final_path: Path) -> None:
    writer = PdfWriter()
    ci_reader = PdfReader(str(ci_prefix))
    official_reader = PdfReader(str(OFFICIAL_SRC))
    for page in ci_reader.pages:
        writer.add_page(page)
    for page in official_reader.pages:
        writer.add_page(page)
    with final_path.open("wb") as handle:
        writer.write(handle)
    if getattr(ci_reader, "stream", None):
        ci_reader.stream.close()
    if getattr(official_reader, "stream", None):
        official_reader.stream.close()


def compare_official_pages(candidate: Path) -> dict[str, object]:
    official_doc = fitz.open(OFFICIAL_SRC)
    candidate_doc = fitz.open(candidate)
    issues: list[str] = []
    compared = 0
    start = 3
    try:
        if candidate_doc.page_count - start != official_doc.page_count:
            issues.append("Official form page count mismatch.")
        else:
            for idx in range(official_doc.page_count):
                src_pix = official_doc[idx].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                out_pix = candidate_doc[start + idx].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                compared += 1
                if src_pix.width != out_pix.width or src_pix.height != out_pix.height or src_pix.samples != out_pix.samples:
                    issues.append(f"Official form page {idx + 1} render mismatch.")
    finally:
        official_doc.close()
        candidate_doc.close()
    return {"compared": compared, "issues": issues}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def render_samples(candidate: Path) -> list[str]:
    if QA_DIR.exists():
        for p in sorted(QA_DIR.rglob("*"), reverse=True):
            if p.is_file():
                p.unlink()
            elif p.is_dir():
                p.rmdir()
    QA_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(candidate)
    outputs: list[str] = []
    try:
        for page_index in [0, 1, 2, 3, doc.page_count - 1]:
            pix = doc[page_index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            dest = QA_DIR / f"target_page_{page_index + 1:03d}.png"
            pix.save(dest)
            outputs.append(str(dest))
    finally:
        doc.close()
    return outputs


def main() -> None:
    if not SOURCE_CI.exists():
        fail(f"Missing source CI PDF: {SOURCE_CI}")
    if not OFFICIAL_SRC.exists():
        fail(f"Missing source official CDPH form PDF: {OFFICIAL_SRC}")
    if not TARGET.exists():
        fail(f"Missing output target PDF: {TARGET}")

    a = assets()
    prefix = Path(tempfile.gettempdir()) / "ci_ion_cna_minimum_studio_prefix.pdf"
    build_ci_prefix(a, prefix)
    merge_with_official(prefix, TEMP_TARGET)

    comparison = compare_official_pages(TEMP_TARGET)
    if comparison["issues"]:
        fail("; ".join(comparison["issues"]))

    before_hash = sha256(TARGET)
    official_hash = sha256(OFFICIAL_SRC)
    samples = render_samples(TEMP_TARGET)
    TEMP_TARGET.replace(TARGET)
    prefix.unlink(missing_ok=True)

    print(json.dumps({
        "status": "complete",
        "target": str(TARGET),
        "previous_target_sha256": before_hash,
        "new_target_sha256": sha256(TARGET),
        "official_source_sha256": official_hash,
        "page_count": len(PdfReader(str(TARGET)).pages),
        "official_pages_appended_from": str(OFFICIAL_SRC),
        "official_visual_compare": comparison,
        "qa_samples": samples,
    }, indent=2))


if __name__ == "__main__":
    main()
