from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path

import fitz
from pypdf import PdfReader, PdfWriter


ROOT = Path(r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet")
SOURCE_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN - Copy - Copy"
OUTPUT_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED - Copy"
QA_DIR = Path(tempfile.gettempdir()) / "ci_ion_packet_content_studio_qa"

OFFICIAL_FORMS = {
    "cna": Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/03_CNA_CDPH_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"),
    "rcfe": Path("02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/03_RCFE_CDSS_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"),
    "brn": Path("03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/03_BRN_CEP_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"),
}

MIXED_TO_OFFICIAL = {
    Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/01_CNA_CDPH_APPLICATION_BINDER.pdf"): "cna",
    Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf"): "cna",
    Path("02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/01_RCFE_CDSS_APPLICATION_BINDER.pdf"): "rcfe",
    Path("02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/02_RCFE_CDSS_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf"): "rcfe",
    Path("03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/01_BRN_CEP_APPLICATION_BINDER.pdf"): "brn",
    Path("03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/02_BRN_CEP_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf"): "brn",
}

OFFICIAL_ONLY = set(OFFICIAL_FORMS.values())

SKIP_RELATIVE = {
    Path("04_MOODLE_IMPLEMENTATION_REQUIREMENTS/01_MOODLE_SELF_HOST_IMPLEMENTATION_REQUIREMENTS_ONLY.pdf"),
}

TITLE_MAP = {
    "00_YADVIR_READ_ME_FIRST_COMPLETE_GUIDE": "START HERE - READ ME FIRST",
    "01_MASTER_END_USER_PACKET_INDEX": "MASTER END USER PACKET INDEX",
    "03_CE_CATALOG_ADDENDUM_AND_WEBSITE_UPDATE_GUIDE": "CE CATALOG ADDENDUM AND WEBSITE UPDATE GUIDE",
    "01_CNA_CDPH_APPLICATION_BINDER": "CNA/CDPH CE SIGNER-REVIEW BINDER",
    "02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET": "CNA/CDPH MINIMUM REQUIRED SUBMISSION PACKET",
    "04_CNA_CDPH_MISSING_OR_PENDING_SUBMISSION_ITEMS": "CNA/CDPH POST-HANDOFF CONTEXT",
    "01_CNA_24HR_12_UNIT_COURSE_MATERIALS_COMPILED": "CNA 24-HOUR COURSE MATERIALS",
    "02_CNA_COURSE_MATRIX_AND_SOURCE_CROSSWALK": "CNA COURSE MATRIX AND SOURCE CROSSWALK",
    "03_CNA_LMS_RAW_COURSE_CONTENT_FOR_POST_SME_BUILD": "CNA LMS RAW COURSE CONTENT",
    "01_RCFE_CDSS_APPLICATION_BINDER": "RCFE/CDSS CETP SIGNER-REVIEW BINDER",
    "02_RCFE_CDSS_MINIMUM_REQUIRED_SUBMISSION_PACKET": "RCFE/CDSS MINIMUM REQUIRED SUBMISSION PACKET",
    "04_RCFE_CDSS_MISSING_OR_PENDING_SUBMISSION_ITEMS": "RCFE/CDSS POST-HANDOFF CONTEXT",
    "01_RCFE_9_COURSE_27HR_COURSE_MATERIALS_COMPILED": "RCFE COURSE MATERIALS",
    "02_RCFE_COURSE_MATRIX_AND_DEMENTIA_BLOCK": "RCFE COURSE MATRIX AND DEMENTIA BLOCK",
    "03_RCFE_LMS_RAW_COURSE_CONTENT_FOR_POST_SME_BUILD": "RCFE LMS RAW COURSE CONTENT",
    "01_BRN_CEP_APPLICATION_BINDER": "BRN CEP SIGNER-REVIEW BINDER",
    "02_BRN_CEP_MINIMUM_REQUIRED_SUBMISSION_PACKET": "BRN CEP MINIMUM REQUIRED SUBMISSION PACKET",
    "04_BRN_CEP_MISSING_OR_PENDING_SUBMISSION_ITEMS": "BRN CEP POST-HANDOFF CONTEXT",
    "01_BRN_30_CONTACT_HOUR_COURSE_MATERIALS_COMPILED": "BRN 30 CONTACT HOUR COURSE MATERIALS",
    "02_BRN_CONTACT_HOUR_MAP_AND_REPRESENTATIVE_COURSE_PACKET": "BRN CONTACT HOUR MAP",
    "03_BRN_LMS_RAW_COURSE_CONTENT_FOR_POST_SME_BUILD": "BRN LMS RAW COURSE CONTENT",
    "01_POST_SME_MOODLE_BUILD_HANDOFF_READ_ME": "POST-SME MOODLE BUILD HANDOFF",
    "02_POST_SME_MOODLE_BUILD_REQUIREMENTS_AND_COURSE_CONTENT_INDEX": "MOODLE BUILD REQUIREMENTS INDEX",
}

# PDF_Design_Studio source-of-truth colors.
CI_MAROON = (0x8B / 255, 0x15 / 255, 0x15 / 255)
CI_MAROON_DEEP = (0x61 / 255, 0, 0)
CI_GOLD = (0xFF / 255, 0xC1 / 255, 0x07 / 255)
PAPER_CREAM = (0xFD / 255, 0xFC / 255, 0xF7 / 255)
TEXT_GRAY = (0x66 / 255, 0x66 / 255, 0x66 / 255)
BORDER_GRAY = (0xE0 / 255, 0xE0 / 255, 0xE0 / 255)

LETTER_W = 612.0
LETTER_H = 792.0


def rel_text(path: Path) -> str:
    return str(path).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def page_count(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def header_label(rel_path: Path) -> str:
    return TITLE_MAP.get(rel_path.stem, rel_path.stem.replace("_", " ").upper())


def official_start_for(rel_path: Path, total_pages: int) -> int | None:
    lane = MIXED_TO_OFFICIAL.get(rel_path)
    if lane is None:
        return None
    official_pages = page_count(SOURCE_ROOT / OFFICIAL_FORMS[lane])
    return total_pages - official_pages


def is_old_bordered_page(doc: fitz.Document, index: int) -> bool:
    page = doc[index]
    pix = page.get_pixmap(matrix=fitz.Matrix(0.25, 0.25), colorspace=fitz.csRGB, alpha=False)
    w, h = pix.width, pix.height
    data = pix.samples
    stride = 3
    side_gold = 0
    side_total = 0
    for y in range(int(h * 0.04), int(h * 0.96)):
        for x in list(range(int(w * 0.03), int(w * 0.13))) + list(range(int(w * 0.87), int(w * 0.97))):
            offset = (y * w + x) * stride
            r, g, b = data[offset], data[offset + 1], data[offset + 2]
            if r > 150 and g > 105 and b < 80:
                side_gold += 1
            side_total += 1
    gold_ratio = side_gold / max(side_total, 1)
    text = page.get_text("text").upper()
    legacy_text = "CI INSTITUTE OF NURSING" in text and ("SOURCE PAGE" in text or "CI-CREATED PAGE" in text)
    return gold_ratio > 0.006 or legacy_text


def content_clip(page: fitz.Page) -> fitz.Rect:
    body_blocks = []
    for block in page.get_text("blocks"):
        x0, y0, x1, y1, text = block[:5]
        upper = str(text).upper()
        if y1 < 92 or y0 > 720:
            continue
        if "CI INSTITUTE OF NURSING" in upper and y0 < 145:
            continue
        if "SOURCE PAGE" in upper or "CI-CREATED PAGE" in upper:
            continue
        if not str(text).strip():
            continue
        body_blocks.append(fitz.Rect(x0, y0, x1, y1))
    if not body_blocks:
        return fitz.Rect(72, 112, page.rect.width - 72, page.rect.height - 72)
    rect = body_blocks[0]
    for block in body_blocks[1:]:
        rect |= block
    rect.x0 = max(48, rect.x0 - 24)
    rect.x1 = min(page.rect.width - 48, rect.x1 + 24)
    rect.y0 = max(92, rect.y0 - 18)
    rect.y1 = min(720, rect.y1 + 24)
    return rect


def draw_studio_footer(page: fitz.Page, page_number: int, page_total: int) -> None:
    left = 54.0
    right = page.rect.width - 54.0
    footer_y = page.rect.height - 42.0
    page.draw_line(fitz.Point(left, footer_y), fitz.Point(right, footer_y), color=BORDER_GRAY, width=0.8)
    footer_text_y = footer_y + 14.0
    left_text = "YADVIR SAANDAL / IMPLEMENTATION REQUIREMENT BINDER"
    center_text = f"PAGE {page_number} OF {page_total}"
    right_text = "PREPARED JUNE 09, 2026"
    page.insert_text(fitz.Point(left, footer_text_y), left_text, fontname="helv", fontsize=5.7, color=TEXT_GRAY)
    center_width = fitz.get_text_length(center_text, fontname="helv", fontsize=5.7)
    page.insert_text(fitz.Point((page.rect.width - center_width) / 2, footer_text_y), center_text, fontname="helv", fontsize=5.7, color=TEXT_GRAY)
    right_width = fitz.get_text_length(right_text, fontname="helv", fontsize=5.7)
    page.insert_text(fitz.Point(right - right_width, footer_text_y), right_text, fontname="helv", fontsize=5.7, color=TEXT_GRAY)


def replace_footer(page: fitz.Page, page_number: int, page_total: int) -> None:
    footer_band = fitz.Rect(40, page.rect.height - 58, page.rect.width - 40, page.rect.height - 18)
    page.draw_rect(footer_band, color=PAPER_CREAM, fill=PAPER_CREAM, overlay=True)
    draw_studio_footer(page, page_number, page_total)


def draw_studio_chrome(page: fitz.Page, rel_path: Path, page_number: int, page_total: int) -> None:
    page.draw_rect(page.rect, color=PAPER_CREAM, fill=PAPER_CREAM, overlay=False)
    header_y = 69.0
    left = 54.0
    right = page.rect.width - 54.0
    page.insert_text(fitz.Point(left, header_y - 8), header_label(rel_path), fontname="helv", fontsize=7.0, color=CI_MAROON)
    right_label = "CI INSTITUTE OF NURSING, INC."
    right_width = fitz.get_text_length(right_label, fontname="helv", fontsize=6.5)
    page.insert_text(fitz.Point(right - right_width, header_y - 8), right_label, fontname="helv", fontsize=6.5, color=TEXT_GRAY)
    page.draw_line(fitz.Point(left, header_y), fitz.Point(right, header_y), color=CI_MAROON, width=1.1)
    draw_studio_footer(page, page_number, page_total)


def rgb_from_int(value: int) -> tuple[float, float, float]:
    return (
        ((value >> 16) & 255) / 255,
        ((value >> 8) & 255) / 255,
        (value & 255) / 255,
    )


def font_key(value: str) -> str:
    return "".join(ch for ch in value.lower() if ch.isalnum())


def install_source_fonts(target_page: fitz.Page, src_doc: fitz.Document, src_index: int) -> dict[str, str]:
    installed: dict[str, str] = {}
    for font in src_doc.get_page_fonts(src_index, full=True):
        xref = int(font[0])
        font_type = str(font[1]).lower()
        full_name = str(font[3])
        resource_name = str(font[4])
        if font_type not in {"ttf", "otf"}:
            continue
        extracted = src_doc.extract_font(xref)
        font_buffer = extracted[3] if extracted else None
        if not font_buffer:
            continue
        pdf_font_name = f"SrcFont{xref}"
        target_page.insert_font(fontname=pdf_font_name, fontbuffer=font_buffer)
        for key_source in {full_name, resource_name, full_name.replace(" ", "-"), resource_name.replace(" ", "-")}:
            installed[font_key(key_source)] = pdf_font_name
    return installed


def is_near(value: float, target: float, tolerance: float = 1.5) -> bool:
    return abs(value - target) <= tolerance


def is_shell_drawing(rect: fitz.Rect | None, color: tuple[float, ...] | None, fill: tuple[float, ...] | None) -> bool:
    if rect is None:
        return True
    width = rect.width
    height = rect.height

    # Studio content starts below the top rule. Old logo/header items live above it.
    if rect.y1 < 96:
        return True

    # Old source-page footer and old footer rule.
    if rect.y0 > 744:
        return True

    # Full page background, outer gold binder border, and old white content container.
    if width > 500 and height > 620:
        return True
    if rect.x0 <= 46 and rect.y0 <= 104 and rect.x1 >= 566 and rect.y1 >= 748:
        return True

    # Old gold corner/border treatment and old header/footer rules.
    goldish = color is not None and len(color) >= 3 and color[0] > 0.70 and color[1] > 0.55 and color[2] < 0.35
    if goldish:
        if rect.x0 < 35 or rect.x1 > 577 or is_near(rect.y0, 91) or is_near(rect.y0, 766):
            return True

    # The legacy page-body card border is a large grey outline.
    if color is not None and width > 450 and height > 500:
        return True

    # The old full-page white card fill is the primary defect.
    if fill is not None and len(fill) >= 3 and all(component > 0.98 for component in fill) and width > 470 and height > 580:
        return True

    return False


def draw_filtered_drawing(target_page: fitz.Page, drawing: dict[str, object]) -> None:
    rect = drawing.get("rect")
    color = drawing.get("color")
    fill = drawing.get("fill")
    if is_shell_drawing(rect, color, fill):
        return
    if not isinstance(rect, fitz.Rect):
        return

    stroke = color if color is not None else None
    paint = fill if fill is not None else None
    width = float(drawing.get("width") or 0.5)

    if rect.width < 0.2 and rect.height < 0.2:
        return
    if rect.height < 0.2:
        target_page.draw_line(
            fitz.Point(rect.x0, rect.y0),
            fitz.Point(rect.x1, rect.y0),
            color=stroke or paint or TEXT_GRAY,
            width=width,
        )
        return
    if rect.width < 0.2:
        target_page.draw_line(
            fitz.Point(rect.x0, rect.y0),
            fitz.Point(rect.x0, rect.y1),
            color=stroke or paint or TEXT_GRAY,
            width=width,
        )
        return

    target_page.draw_rect(rect, color=stroke, fill=paint, width=width)


def draw_filtered_images(target_page: fitz.Page, source_page: fitz.Page, src_doc: fitz.Document) -> None:
    for image in source_page.get_image_info(xrefs=True):
        bbox = fitz.Rect(image["bbox"])
        if bbox.y1 < 100 or bbox.y0 > 742:
            continue
        if bbox.width > 500 and bbox.height > 600:
            continue
        xref = int(image.get("xref") or 0)
        if not xref:
            continue
        extracted = src_doc.extract_image(xref)
        stream = extracted.get("image") if extracted else None
        if not stream:
            continue
        target_page.insert_image(bbox, stream=stream, keep_proportion=False, overlay=True)


def span_font(span: dict[str, object], installed_fonts: dict[str, str]) -> str:
    font = str(span.get("font", ""))
    match = installed_fonts.get(font_key(font))
    if match:
        return match
    match = installed_fonts.get(font_key(font.replace("-", " ")))
    if match:
        return match
    lowered = font.lower()
    if "bold" in lowered and ("italic" in lowered or "oblique" in lowered):
        return "hebi"
    if "bold" in lowered:
        return "hebo"
    if "italic" in lowered or "oblique" in lowered:
        return "heit"
    return "helv"


def draw_filtered_text(target_page: fitz.Page, source_page: fitz.Page, installed_fonts: dict[str, str]) -> None:
    data = source_page.get_text("dict")
    for block in data.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span.get("text", "")
                if not text:
                    continue
                bbox = fitz.Rect(span.get("bbox"))
                if bbox.y1 < 100 or bbox.y0 > 742:
                    continue
                if "CI-created page | Source page" in text:
                    continue
                origin = span.get("origin")
                if not origin:
                    continue
                color = rgb_from_int(int(span.get("color", 0x222222)))
                target_page.insert_text(
                    fitz.Point(float(origin[0]), float(origin[1])),
                    text,
                    fontname=span_font(span, installed_fonts),
                    fontsize=float(span.get("size", 8.0)),
                    color=color,
                    overlay=True,
                )


def add_redrawn_content(
    out_doc: fitz.Document,
    src_doc: fitz.Document,
    src_index: int,
    rel_path: Path,
    page_number: int,
    page_total: int,
) -> None:
    source_page = src_doc[src_index]
    new_page = out_doc.new_page(width=LETTER_W, height=LETTER_H)
    draw_studio_chrome(new_page, rel_path, page_number, page_total)
    installed_fonts = install_source_fonts(new_page, src_doc, src_index)
    for drawing in source_page.get_drawings():
        draw_filtered_drawing(new_page, drawing)
    draw_filtered_images(new_page, source_page, src_doc)
    draw_filtered_text(new_page, source_page, installed_fonts)
    replace_footer(new_page, page_number, page_total)


def visual_compare_official(candidate: Path, lane: str, official_start_index: int) -> list[str]:
    official = SOURCE_ROOT / OFFICIAL_FORMS[lane]
    issues = []
    with fitz.open(candidate) as out_doc, fitz.open(official) as official_doc:
        if out_doc.page_count - official_start_index != official_doc.page_count:
            return ["official appendix page count mismatch"]
        for index in range(official_doc.page_count):
            src = official_doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            out = out_doc[official_start_index + index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            if src.digest != out.digest:
                issues.append(f"official appendix page {index + 1} render mismatch")
    return issues


def append_official_source_pages(prefix_pdf: Path, final_pdf: Path, lane: str) -> None:
    writer = PdfWriter()
    prefix_reader = PdfReader(str(prefix_pdf))
    for page in prefix_reader.pages:
        writer.add_page(page)
    official_reader = PdfReader(str(SOURCE_ROOT / OFFICIAL_FORMS[lane]))
    for page in official_reader.pages:
        writer.add_page(page)
    with final_pdf.open("wb") as handle:
        writer.write(handle)


def process_pdf(pdf: Path) -> dict[str, object]:
    rel_path = pdf.relative_to(OUTPUT_ROOT)
    if rel_path in OFFICIAL_ONLY:
        return {"rel": rel_text(rel_path), "status": "skipped_official"}
    if rel_path in SKIP_RELATIVE:
        return {"rel": rel_text(rel_path), "status": "skipped_not_in_scope"}

    before = sha256(pdf)
    changed_pages: list[int] = []
    footer_updated_pages: list[int] = []
    total_pages = page_count(pdf)
    lane = MIXED_TO_OFFICIAL.get(rel_path)
    official_start = official_start_for(rel_path, total_pages)
    divider_index = official_start - 1 if official_start is not None else None
    tmp: Path | None = None
    prefix_tmp: Path | None = None

    with fitz.open(pdf) as src_doc:
        with fitz.open() as out_doc:
            for index in range(src_doc.page_count):
                if index == 0:
                    out_doc.insert_pdf(src_doc, from_page=index, to_page=index)
                    continue
                if official_start is not None and index >= official_start:
                    continue
                if divider_index is not None and index == divider_index:
                    out_doc.insert_pdf(src_doc, from_page=index, to_page=index)
                    continue
                add_redrawn_content(out_doc, src_doc, index, rel_path, index + 1, src_doc.page_count)
                changed_pages.append(index + 1)
            if changed_pages or footer_updated_pages:
                tmp = pdf.with_suffix(".studio-content.tmp.pdf")
                tmp.unlink(missing_ok=True)
                if lane is not None and official_start is not None:
                    prefix_tmp = pdf.with_suffix(".ci-prefix.tmp.pdf")
                    prefix_tmp.unlink(missing_ok=True)
                    out_doc.save(prefix_tmp, deflate=True, garbage=4)
                else:
                    out_doc.save(tmp, deflate=True, garbage=4)

    if tmp is not None:
        if lane is not None and official_start is not None:
            if prefix_tmp is None:
                raise RuntimeError(f"{rel_text(rel_path)}: missing mixed-binder prefix temp file")
            append_official_source_pages(prefix_tmp, tmp, lane)
            prefix_tmp.unlink(missing_ok=True)
            official_issues = visual_compare_official(tmp, lane, official_start)
            if official_issues:
                tmp.unlink(missing_ok=True)
                raise RuntimeError(f"{rel_text(rel_path)}: {'; '.join(official_issues)}")
        tmp.replace(pdf)

    after = sha256(pdf)
    official_issues: list[str] = []
    if lane is not None and official_start is not None and (changed_pages or footer_updated_pages):
        official_issues = visual_compare_official(pdf, lane, official_start)
        if official_issues:
            raise RuntimeError(f"{rel_text(rel_path)}: {'; '.join(official_issues)}")
    return {
        "rel": rel_text(rel_path),
        "status": "updated" if (changed_pages or footer_updated_pages) else "unchanged",
        "changed_pages": changed_pages,
        "footer_updated_pages": footer_updated_pages,
        "before_sha256": before,
        "after_sha256": after,
        "official_verified": not official_issues,
    }


def render_qa(updated: list[Path]) -> list[str]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    samples = []
    for pdf in updated[:12]:
        with fitz.open(pdf) as doc:
            indices = sorted({0, min(1, doc.page_count - 1), min(2, doc.page_count - 1), doc.page_count - 1})
            for index in indices:
                out = QA_DIR / f"{pdf.stem}_p{index + 1:03d}.png"
                doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False).save(out)
                samples.append(str(out))
    return samples


def main() -> None:
    pdfs = sorted(path for path in OUTPUT_ROOT.rglob("*.pdf") if ".tmp" not in path.name)
    results = []
    updated = []
    for pdf in pdfs:
        result = process_pdf(pdf)
        results.append(result)
        if result["status"] == "updated":
            updated.append(pdf)
    samples = render_qa(updated)
    report = {
        "processed": len(pdfs),
        "updated": sum(1 for item in results if item["status"] == "updated"),
        "unchanged": sum(1 for item in results if item["status"] == "unchanged"),
        "skipped": sum(1 for item in results if str(item["status"]).startswith("skipped")),
        "results": results,
        "qa_samples": samples,
    }
    report_path = OUTPUT_ROOT / "STUDIO_CONTENT_PAGE_FIX_REPORT.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ["processed", "updated", "unchanged", "skipped"]}, indent=2))


if __name__ == "__main__":
    main()
