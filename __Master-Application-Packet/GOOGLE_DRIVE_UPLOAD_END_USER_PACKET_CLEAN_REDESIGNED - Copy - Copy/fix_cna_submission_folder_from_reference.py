from __future__ import annotations

import hashlib
import json
import math
import random
import sys
import tempfile
from pathlib import Path

import fitz
from PIL import Image
from pypdf import PdfReader, PdfWriter


ROOT = Path(r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet")
SOURCE_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN - Copy - Copy"
OUTPUT_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED - Copy"
SCOPE = OUTPUT_ROOT / "01_CNA_CDPH_CE_APPLICATION" / "01_APPLICATION_SUBMISSION"
OFFICIAL_REL = Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/03_CNA_CDPH_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf")
OFFICIAL_SOURCE = SOURCE_ROOT / OFFICIAL_REL
OFFICIAL_OUTPUT = OUTPUT_ROOT / OFFICIAL_REL
DESIGN_REFERENCE = ROOT / "PDF_Design_Studio"
QA_DIR = Path(tempfile.gettempdir()) / "ci_ion_cna_submission_folder_fix_qa"

sys.path.insert(0, str(ROOT))
import refit_cna_minimum_packet_studio_style as studio  # noqa: E402


LETTER_W = studio.LETTER_W
LETTER_H = studio.LETTER_H


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    raise RuntimeError(message)


def write_pdf_atomic(doc: fitz.Document, target: Path) -> Path:
    temp = target.with_suffix(".fixed.tmp.pdf")
    doc.save(temp, garbage=4, deflate=True, clean=True)
    doc.close()
    return temp


def replace_after_verify(temp: Path, target: Path) -> tuple[str, str]:
    before = sha256(target) if target.exists() else ""
    temp.replace(target)
    return before, sha256(target)


def draw_matte_gradient(page: fitz.Page, center_y: float = 276) -> None:
    cache = Path(tempfile.gettempdir()) / f"ci_ion_matte_gradient_{int(center_y)}_v3.png"
    if not cache.exists():
        scale = 2
        w = int(LETTER_W * scale)
        h = int(LETTER_H * scale)
        cx = 0.50 * w
        cy = (center_y / LETTER_H) * h
        center = (0x82, 0x10, 0x10)
        mid = (0x58, 0x03, 0x03)
        edge = (0x25, 0x00, 0x00)
        rng = random.Random(20260611 + int(center_y))
        img = Image.new("RGB", (w, h))
        px = img.load()
        for y in range(h):
            ny = (y - cy) / (h * 0.58)
            vertical = y / h
            for x in range(w):
                nx = (x - cx) / (w * 0.72)
                d = min(1.0, math.sqrt(nx * nx + ny * ny))
                # Smooth elliptical gradient, not a tight circular spotlight.
                t = d * d * (3 - 2 * d)
                if t < 0.58:
                    local = t / 0.58
                    color = tuple(int(center[i] * (1 - local) + mid[i] * local) for i in range(3))
                else:
                    local = (t - 0.58) / 0.42
                    color = tuple(int(mid[i] * (1 - local) + edge[i] * local) for i in range(3))
                vignette = 0.08 + 0.20 * abs(vertical - 0.46)
                grain = rng.randint(-2, 2)
                weave = int(
                    0.6 * math.sin((x * 0.75 + y * 0.25) / 37.0)
                    + 0.45 * math.sin((x - y) / 61.0)
                )
                color = tuple(max(0, min(255, int(c * (1 - vignette)) + grain + weave)) for c in color)
                px[x, y] = color
        cache.parent.mkdir(parents=True, exist_ok=True)
        img.save(cache, optimize=True)
    page.insert_image(page.rect, filename=str(cache))


def generic_cover(
    doc: fitz.Document,
    assets: dict[str, object],
    left_label: str,
    title: str,
    subtitle: str,
    footnote: str,
) -> None:
    page = doc.new_page(width=LETTER_W, height=LETTER_H)
    studio.put_fonts(page, assets)
    draw_matte_gradient(page)
    studio.draw_studio_frame(page)

    studio.vertical_label(page, left_label, 38, 110, 682, 90)
    studio.vertical_label(page, "DRAFT / PENDING CDPH APPROVAL", LETTER_W - 38, 110, 682, 270)

    page.insert_image(fitz.Rect(200, 78, 412, 290), pixmap=assets["logo"], keep_proportion=True)
    studio.text_box(page, fitz.Rect(86, 318, 526, 345), "CALIFORNIA", "RobotoLight", 15.5, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    studio.text_box(page, fitz.Rect(64, 355, 548, 396), title, "RobotoLight", 25.5, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    studio.text_box(page, fitz.Rect(82, 407, 530, 432), subtitle, "RobotoSemi", 14.5, studio.GOLD, fitz.TEXT_ALIGN_CENTER)
    studio.text_box(page, fitz.Rect(82, 434, 530, 454), "ONLINE CE - SIGNER-REVIEW BINDER", "RobotoRegular", 9.5, (0.86, 0.86, 0.86), fitz.TEXT_ALIGN_CENTER)

    y = 470
    studio.text_box(
        page,
        fitz.Rect(108, y, 504, y + 18),
        "24 Online CE Hours    |    12 Units x 2 Hours    |    Source Backbone: CCCCO/NATP 10-17",
        "RobotoRegular",
        7.6,
        (1, 1, 1),
        fitz.TEXT_ALIGN_CENTER,
    )
    studio.text_box(
        page,
        fitz.Rect(118, y + 15, 494, y + 31),
        "CCCCO / NATP SOURCE BACKBONE - LEARNER-FACING STRUCTURE REMAINS U01-U12",
        "RobotoLight",
        6.3,
        (0.72, 0.72, 0.72),
        fitz.TEXT_ALIGN_CENTER,
    )

    page.draw_line((105, 520), (292, 520), color=studio.GOLD_DARK, width=0.7)
    page.draw_rect(fitz.Rect(303, 516.5, 309, 522.5), color=studio.GOLD, fill=studio.GOLD)
    page.draw_line((320, 520), (507, 520), color=studio.GOLD_DARK, width=0.7)

    studio.text_box(page, fitz.Rect(108, 553, 504, 574), "CI Institute of Nursing, Inc.", "RobotoMedium", 10.5, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    studio.text_box(page, fitz.Rect(108, 578, 504, 596), "PREPARED FOR YADVIR SAANDAL - JUNE 9, 2026", "RobotoRegular", 7.2, (0.72, 0.72, 0.72), fitz.TEXT_ALIGN_CENTER)

    page.draw_line((108, 665), (176, 665), color=studio.GOLD_DARK, width=0.8)
    page.draw_line((436, 665), (504, 665), color=studio.GOLD_DARK, width=0.8)
    studio.text_box(page, fitz.Rect(180, 653, 432, 675), "STATUS: DRAFT / PENDING CDPH APPROVAL", "RobotoRegular", 10.0, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    studio.text_box(page, fitz.Rect(146, 679, 466, 696), "Ready for verification, signature, and submission review.", "RobotoLight", 7.0, (0.78, 0.78, 0.78), fitz.TEXT_ALIGN_CENTER)
    studio.text_box(page, fitz.Rect(72, 754, 540, 765), footnote, "RobotoLight", 5.1, (0.58, 0.58, 0.58), fitz.TEXT_ALIGN_CENTER)


def source_body_bbox(page: fitz.Page) -> fitz.Rect:
    blocks = []
    for block in page.get_text("blocks"):
        text = " ".join(str(block[4]).split())
        if not text:
            continue
        if block[1] < 68 or block[3] > 735:
            continue
        blocks.append(block)
    if not blocks:
        return fitz.Rect(54, 108, 558, 720)
    x0 = max(54, min(b[0] for b in blocks) - 8)
    y0 = max(70, min(b[1] for b in blocks) - 10)
    x1 = min(558, max(b[2] for b in blocks) + 8)
    y1 = min(720, max(b[3] for b in blocks) + 12)
    return fitz.Rect(x0, y0, x1, y1)


def add_source_body_page(
    out_doc: fitz.Document,
    source_doc: fitz.Document,
    source_index: int,
    assets: dict[str, object],
    page_no: int,
    total: int,
) -> None:
    page = out_doc.new_page(width=LETTER_W, height=LETTER_H)
    studio.page_header_footer(page, assets, page_no, total)
    clip = source_body_bbox(source_doc[source_index])
    ratio = clip.height / clip.width
    dest_w = 504
    dest_h = min(615, dest_w * ratio)
    dest = fitz.Rect(54, 108, 558, 108 + dest_h)
    page.show_pdf_page(dest, source_doc, source_index, clip=clip, keep_proportion=True)


def build_application_binder(assets: dict[str, object]) -> tuple[Path, dict[str, object]]:
    rel = Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/01_CNA_CDPH_APPLICATION_BINDER.pdf")
    source = SOURCE_ROOT / rel
    target = OUTPUT_ROOT / rel
    if not source.exists():
        fail(f"Missing source application binder: {source}")
    if not OFFICIAL_SOURCE.exists():
        fail(f"Missing source official CDPH forms: {OFFICIAL_SOURCE}")

    source_doc = fitz.open(source)
    out_doc = fitz.open()
    total = 12 + len(PdfReader(str(OFFICIAL_SOURCE)).pages)
    generic_cover(
        out_doc,
        assets,
        "CNA / CDPH APPLICATION BINDER",
        "CNA / CDPH APPLICATION",
        "SIGNER-REVIEW BINDER",
        "No public approval claim, enrollment for approved credit, or certificate release is authorized until applicable agency approval metadata is issued.",
    )
    for source_index in range(1, min(11, source_doc.page_count)):
        add_source_body_page(out_doc, source_doc, source_index, assets, source_index + 1, total)
    studio.studio_appendix_divider(out_doc, assets)
    prefix = write_pdf_atomic(out_doc, target)
    source_doc.close()

    merged = target.with_suffix(".merged.tmp.pdf")
    writer = PdfWriter()
    ci_reader = PdfReader(str(prefix))
    official_reader = PdfReader(str(OFFICIAL_SOURCE))
    for page in ci_reader.pages:
        writer.add_page(page)
    for page in official_reader.pages:
        writer.add_page(page)
    with merged.open("wb") as handle:
        writer.write(handle)
    if getattr(ci_reader, "stream", None):
        ci_reader.stream.close()
    if getattr(official_reader, "stream", None):
        official_reader.stream.close()
    prefix.unlink(missing_ok=True)
    return merged, {"rel": str(rel).replace("/", "\\"), "official_pages": len(PdfReader(str(OFFICIAL_SOURCE)).pages)}


def build_minimum_submission_packet(assets: dict[str, object]) -> tuple[Path, dict[str, object]]:
    rel = Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf")
    target = OUTPUT_ROOT / rel
    if not target.exists():
        fail(f"Missing trusted minimum packet target: {target}")
    prefix = target.with_suffix(".prefix.tmp.pdf")
    doc = fitz.open()
    studio.studio_cover(doc, assets)
    studio.studio_content_page(doc, assets)
    studio.studio_appendix_divider(doc, assets)
    doc.save(prefix, garbage=4, deflate=True, clean=True)
    doc.close()

    merged = target.with_suffix(".merged.tmp.pdf")
    writer = PdfWriter()
    ci_reader = PdfReader(str(prefix))
    official_reader = PdfReader(str(OFFICIAL_SOURCE))
    for page in ci_reader.pages:
        writer.add_page(page)
    for page in official_reader.pages:
        writer.add_page(page)
    with merged.open("wb") as handle:
        writer.write(handle)
    if getattr(ci_reader, "stream", None):
        ci_reader.stream.close()
    if getattr(official_reader, "stream", None):
        official_reader.stream.close()
    prefix.unlink(missing_ok=True)
    return merged, {"rel": str(rel).replace("/", "\\"), "official_pages": len(PdfReader(str(OFFICIAL_SOURCE)).pages)}


def table(page: fitz.Page, y: float, headers: list[str], rows: list[tuple[str, str, str]]) -> float:
    widths = [220, 142, 142]
    x0 = 54
    header_h = 22
    row_h = 34
    page.draw_rect(fitz.Rect(x0, y, x0 + sum(widths), y + header_h), color=studio.MAROON_DEEP, fill=studio.MAROON_DEEP)
    x = x0
    for idx, header in enumerate(headers):
        studio.text_box(page, fitz.Rect(x + 8, y + 6, x + widths[idx] - 6, y + header_h - 2), header.upper(), "RobotoBold", 6.8, (1, 1, 1))
        x += widths[idx]
    y += header_h
    for idx, row in enumerate(rows):
        fill = studio.ROW_TINT if idx % 2 else studio.CREAM
        page.draw_rect(fitz.Rect(x0, y, x0 + sum(widths), y + row_h), color=studio.TABLE_LINE, fill=fill, width=0.45)
        x = x0
        for col, cell in enumerate(row):
            font = "RobotoBold" if col == 0 else "RobotoRegular"
            color = studio.MAROON_DEEP if col == 0 else studio.TEXT
            studio.text_box(page, fitz.Rect(x + 8, y + 7, x + widths[col] - 6, y + row_h - 4), cell, font, 6.7, color, lineheight=1.05, min_size=5.8)
            x += widths[col]
        y += row_h
    return y + 18


def build_missing_pending_context(assets: dict[str, object]) -> tuple[Path, dict[str, object]]:
    rel = Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/04_CNA_CDPH_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf")
    target = OUTPUT_ROOT / rel
    out_doc = fitz.open()
    generic_cover(
        out_doc,
        assets,
        "CNA / CDPH REVIEW CONTEXT",
        "CNA / CDPH REVIEW CONTEXT",
        "POST-HANDOFF CONTEXT",
        "Context only for final review before submission or public release. No build tasks are created here.",
    )

    page = out_doc.new_page(width=LETTER_W, height=LETTER_H)
    studio.page_header_footer(page, assets, 2, 2)
    y = studio.section_title(page, 108, "Review Context After Handoff")
    y = studio.paragraph(
        page,
        y,
        "No missing application-submission documents were identified during this packet build. The items below are retained only as context for final review before submission or public release.",
        42,
        size=8.7,
    )
    y = studio.note_box(
        page,
        y + 12,
        "This page is not a task tracker, due-date sheet, build action list, or blocker log. After packet handoff, remaining review and release decisions are handled through the verification process.",
        44,
    )
    studio.text_box(page, fitz.Rect(54, y + 6, 558, y + 22), "Context Items for Human Review", "RobotoBold", 10.0, studio.MAROON)
    rows = [
        ("Official CDPH signature/date fields", "Final read-through only", "Original official forms packet"),
        ("CDPH 192B pricing / membership fields", "Final read-through only", "Original official forms packet"),
        ("CDPH 193 mailing-address confirmation if needed", "Final read-through only", "Original official forms packet"),
        ("Instructor / SME evidence attachment presence", "Confirm packet completeness", "Application binder attachments"),
        ("Reviewer URL, user ID, and password values", "Confirm credential delivery works", "Reviewer-access material"),
        ("Public catalog and website fields", "Confirm before external release", "Catalog addendum"),
    ]
    y = table(page, y + 32, ["Context item", "Review purpose", "Packet location"], rows)
    studio.text_box(page, fitz.Rect(54, y, 558, y + 18), "Release Context", "Times-Bold", 11.5, studio.MAROON_DEEP)
    studio.note_box(
        page,
        y + 23,
        "Certificate release remains disabled pending CDPH approval metadata and completion evidence gates. No public approval claim is made by this packet.",
        42,
        accent=studio.MAROON,
    )
    temp = write_pdf_atomic(out_doc, target)
    return temp, {"rel": str(rel).replace("/", "\\")}


def compare_appended_official(candidate: Path, official: Path, ci_prefix_pages: int) -> list[str]:
    issues = []
    with fitz.open(candidate) as cand, fitz.open(official) as src:
        if cand.page_count - ci_prefix_pages != src.page_count:
            return ["official appendix page count mismatch"]
        for idx in range(src.page_count):
            src_pix = src[idx].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            out_pix = cand[ci_prefix_pages + idx].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            if src_pix.width != out_pix.width or src_pix.height != out_pix.height or src_pix.samples != out_pix.samples:
                issues.append(f"official appendix page {idx + 1} render mismatch")
    return issues


def render_samples(paths: list[Path]) -> list[str]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    outputs = []
    for path in paths:
        with fitz.open(path) as doc:
            indices = sorted({0, min(1, doc.page_count - 1), min(2, doc.page_count - 1), doc.page_count - 1})
            for index in indices:
                pix = doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                out = QA_DIR / f"{path.stem}_p{index + 1:03d}.png"
                pix.save(out)
                outputs.append(str(out))
    return outputs


def main() -> None:
    if not SCOPE.exists():
        fail(f"Missing scope folder: {SCOPE}")
    if not DESIGN_REFERENCE.exists():
        fail(f"Missing design reference folder: {DESIGN_REFERENCE}")
    if not OFFICIAL_SOURCE.exists():
        fail(f"Missing source official form PDF: {OFFICIAL_SOURCE}")
    if not OFFICIAL_OUTPUT.exists():
        fail(f"Missing output official form PDF: {OFFICIAL_OUTPUT}")
    if sha256(OFFICIAL_SOURCE) != sha256(OFFICIAL_OUTPUT):
        fail("Output official forms packet differs from source; stopping before any changes.")

    studio.draw_radial_maroon = draw_matte_gradient
    assets = studio.assets()
    results: list[dict[str, object]] = []

    app_temp, app_meta = build_application_binder(assets)
    app_issues = compare_appended_official(app_temp, OFFICIAL_SOURCE, 12)
    if app_issues:
        app_temp.unlink(missing_ok=True)
        fail("; ".join(app_issues))
    target = OUTPUT_ROOT / Path(app_meta["rel"])
    before, after = replace_after_verify(app_temp, target)
    results.append({**app_meta, "previous_sha256": before, "new_sha256": after, "status": "fixed"})

    minimum_temp, minimum_meta = build_minimum_submission_packet(assets)
    minimum_issues = compare_appended_official(minimum_temp, OFFICIAL_SOURCE, 3)
    if minimum_issues:
        minimum_temp.unlink(missing_ok=True)
        fail("; ".join(minimum_issues))
    target = OUTPUT_ROOT / Path(minimum_meta["rel"])
    before, after = replace_after_verify(minimum_temp, target)
    results.append({**minimum_meta, "previous_sha256": before, "new_sha256": after, "status": "fixed"})

    pending_temp, pending_meta = build_missing_pending_context(assets)
    target = OUTPUT_ROOT / Path(pending_meta["rel"])
    before, after = replace_after_verify(pending_temp, target)
    text = "\n".join(page.get_text("text") for page in fitz.open(target))
    forbidden = [
        "Final verification",
        "Yadvir / owner confirmation",
        "Build-Remediable vs Human/Regulator Items",
        "Why pending",
        "Due/action needed",
        "Blocks submission?",
        "assigned reviewers",
        "owner-assignment",
    ]
    found = [term for term in forbidden if term in text]
    if found:
        fail("Forbidden tracker language remains: " + ", ".join(found))
    results.append({**pending_meta, "previous_sha256": before, "new_sha256": after, "status": "fixed"})

    artifact = SCOPE / "02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.chrome-refit.tmp.pdf"
    artifact_removed = False
    if artifact.exists() and artifact.is_file() and artifact.name.endswith(".tmp.pdf"):
        artifact.unlink()
        artifact_removed = True

    qa_samples = render_samples([
        SCOPE / "01_CNA_CDPH_APPLICATION_BINDER.pdf",
        SCOPE / "02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf",
        SCOPE / "04_CNA_CDPH_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf",
    ])
    print(json.dumps({
        "status": "complete",
        "fixed": results,
        "official_forms_unchanged_sha256": sha256(OFFICIAL_OUTPUT),
        "artifact_removed": artifact_removed,
        "qa_samples": qa_samples,
    }, indent=2))


if __name__ == "__main__":
    main()
