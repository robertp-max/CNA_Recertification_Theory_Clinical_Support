from __future__ import annotations

import hashlib
import io
import json
import re
import shutil
import sys
import tempfile
import urllib.request
from pathlib import Path

import fitz
from pypdf import PdfReader, PdfWriter

try:
    from PIL import Image
except ImportError:
    Image = None


ROOT = Path(r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet")
SRC = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN - Copy - Copy"
OUT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED"
BUILD = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED.__building"
DESIGN_HTML = Path(r"C:\Users\razer\Downloads\ci_ion_pdf_binder_studio.html")
QA_DIR = Path(tempfile.gettempdir()) / "ci_ion_pdf_redesign_qa"

LOGOMARK_WHITE_URL = "https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg"
LOGO_ORIGINAL_URL = "https://ciinstituteofnursing.com/assets/logos/ci-ion-logo-original.svg"
ROBOTO_CSS_URL = "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400&display=swap"

MAROON = (0x8B / 255, 0x15 / 255, 0x15 / 255)
MAROON_DEEP = (0x61 / 255, 0, 0)
MAROON_BLACK = (0x26 / 255, 0, 0)
GOLD = (0xFF / 255, 0xC1 / 255, 0x07 / 255)
GOLD_DARK = (0xD4 / 255, 0xAF / 255, 0x37 / 255)
CREAM = (0xFD / 255, 0xFC / 255, 0xF7 / 255)
WARM_WHITE = (1, 1, 1)
DARK_TEXT = (0x21 / 255, 0x25 / 255, 0x29 / 255)
MUTED = (0x66 / 255, 0x66 / 255, 0x66 / 255)
BORDER = (0xDE / 255, 0xD8 / 255, 0xC8 / 255)

LETTER_W = 612
LETTER_H = 792


OFFICIAL_FORMS = {
    "cna": Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/03_CNA_CDPH_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"),
    "rcfe": Path("02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/03_RCFE_CDSS_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"),
    "brn": Path("03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/03_BRN_CEP_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"),
}

MIXED = {
    Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/01_CNA_CDPH_APPLICATION_BINDER.pdf"): ("cna", 12),
    Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf"): ("cna", 2),
    Path("02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/01_RCFE_CDSS_APPLICATION_BINDER.pdf"): ("rcfe", 11),
    Path("02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/02_RCFE_CDSS_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf"): ("rcfe", 2),
    Path("03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/01_BRN_CEP_APPLICATION_BINDER.pdf"): ("brn", 11),
    Path("03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/02_BRN_CEP_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf"): ("brn", 2),
}


def die(message: str) -> None:
    print(json.dumps({"status": "hard_stop", "message": message}, indent=2))
    sys.exit(2)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read()


def prepare_assets() -> dict[str, object]:
    asset_dir = Path(tempfile.gettempdir()) / "ci_ion_pdf_assets"
    asset_dir.mkdir(parents=True, exist_ok=True)

    css = download(ROBOTO_CSS_URL).decode("utf-8", errors="replace")
    font_urls = re.findall(r"url\((https://[^)]+)\)", css)
    if len(font_urls) < 2:
        die("Could not locate Roboto Light and Roboto Regular font URLs from Google Fonts CSS.")

    light_font = asset_dir / "Roboto-Light.ttf"
    regular_font = asset_dir / "Roboto-Regular.ttf"
    if not light_font.exists():
        light_font.write_bytes(download(font_urls[0]))
    if not regular_font.exists():
        regular_font.write_bytes(download(font_urls[1]))

    logo_white_svg = download(LOGOMARK_WHITE_URL)
    logo_original_svg = download(LOGO_ORIGINAL_URL)

    white_doc = fitz.open(stream=logo_white_svg, filetype="svg")
    original_doc = fitz.open(stream=logo_original_svg, filetype="svg")
    white_pix = white_doc[0].get_pixmap(matrix=fitz.Matrix(4, 4), alpha=True)
    original_pix = original_doc[0].get_pixmap(matrix=fitz.Matrix(1, 1), alpha=True)

    return {
        "roboto_light": light_font,
        "roboto_regular": regular_font,
        "white_logomark": white_pix,
        "original_logo": original_pix,
    }


def rel_posix(path: Path) -> str:
    return path.as_posix()


def clean_text(value: str) -> str:
    value = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def title_from_stem(stem: str) -> str:
    tokens = [t for t in re.split(r"[_\-]+", stem) if t and not t.isdigit()]
    acronyms = {"CNA", "CDPH", "RCFE", "CDSS", "CETP", "BRN", "CEP", "LMS", "SME", "CE"}
    words: list[str] = []
    for token in tokens:
        upper = token.upper()
        if upper in acronyms:
            words.append(upper)
        elif upper in {"HR"}:
            words.append("Hour")
        else:
            words.append(token.capitalize())
    return " ".join(words)


def lane_for_rel(rel: Path) -> str:
    text = rel_posix(rel).upper()
    if "CNA_CDPH" in text:
        return "cna"
    if "RCFE_CDSS" in text:
        return "rcfe"
    if "BRN_CARE_MANAGER" in text or "BRN_CEP" in text:
        return "brn"
    return "general"


def lane_info(lane: str) -> dict[str, object]:
    if lane == "cna":
        return {
            "status": "Draft / Pending CDPH Approval",
            "subtitle": "Online CE Signer-Review Binder",
            "chips": ["24 Online CE Hours", "12 Units x 2 Hours", "Source Backbone: CCCCO/NATP 10-17"],
            "note": "Certificate release disabled pending approval metadata and completion evidence gates.",
        }
    if lane == "rcfe":
        return {
            "status": "Draft / Pending CDSS/ACS Approval",
            "subtitle": "RCFE Administrator Continuing Education",
            "chips": ["27 Filed Hours", "9 Filed Courses", "RCFE Administrator Continuing Education"],
            "note": "Filed-hour language retained. No approval claim is made until CDSS/ACS metadata is issued.",
        }
    if lane == "brn":
        return {
            "status": "Draft / Pending BRN CEP Approval",
            "subtitle": "RN Case Management Continuing Education Provider Packet",
            "chips": ["30 Contact Hours", "10 Modules x 3 Contact Hours", "Contact hours, not CEUs"],
            "note": "Contact-hour language retained. No BRN CEP approval claim is made until provider metadata is issued.",
        }
    return {
        "status": "Draft / Pending Agency Approval",
        "subtitle": "CI-ION End-User Submission Packet",
        "chips": ["Signer Review", "SME Hold", "Agency Approval Pending"],
        "note": "LMS development remains held until approved SME review and applicable agency metadata are complete.",
    }


def infer_cover(rel: Path, src_doc: fitz.Document) -> tuple[str, str]:
    lane = lane_for_rel(rel)
    info = lane_info(lane)
    stem_title = title_from_stem(rel.stem)

    text = src_doc[0].get_text("text") if src_doc.page_count else ""
    lines = [clean_text(x) for x in text.splitlines()]
    lines = [x for x in lines if x]
    skip_exact = {
        "CI Institute of Nursing",
        "CI Institute of Nursing, Inc.",
        "Page 1",
        "Prepared",
        "Status",
        "Folder",
    }
    filtered = []
    for line in lines:
        if line in skip_exact:
            continue
        if "Clean Google Drive End-User Submission Packet" in line:
            continue
        if re.fullmatch(r"[A-Z][a-z]+ \d{2}, \d{4}", line):
            continue
        filtered.append(line)

    if "APPLICATION_BINDER" in rel.stem:
        if lane == "cna":
            # Match the design studio HTML example for the CNA binder cover
            return "CNA Recertification", "CNA Recert Binder"
        if lane == "rcfe":
            return "RCFE / CDSS-ACS Application Binder", str(info["subtitle"])
        if lane == "brn":
            return "BRN CEP Application Binder", "30 Contact Hour Representative Course Packet"

    if "MINIMUM_REQUIRED_SUBMISSION_PACKET" in rel.stem:
        return stem_title, "Minimum required submission packet"

    if "COURSE_MATERIALS_COMPILED" in rel.stem:
        return stem_title, "Compiled course materials"

    if "LMS_RAW_COURSE_CONTENT" in rel.stem:
        return stem_title, "Raw LMS course content for post-SME build"

    if "MISSING_OR_PENDING" in rel.stem:
        return stem_title, "Submission gap and final human-action tracker"

    if filtered:
        title = filtered[0]
        subtitle = filtered[1] if len(filtered) > 1 else str(info["subtitle"])
        if len(title) < 12 and len(filtered) > 1:
            title = filtered[1]
            subtitle = filtered[2] if len(filtered) > 2 else str(info["subtitle"])
        return title[:110], subtitle[:120]

    return stem_title, str(info["subtitle"])


def put_font(page: fitz.Page, assets: dict[str, object]) -> None:
    page.insert_font(fontname="RobotoLight", fontfile=str(assets["roboto_light"]))
    page.insert_font(fontname="RobotoRegular", fontfile=str(assets["roboto_regular"]))


def insert_text_fit(
    page: fitz.Page,
    rect: fitz.Rect,
    text: str,
    fontname: str,
    fontsize: float,
    color: tuple[float, float, float],
    align: int = fitz.TEXT_ALIGN_LEFT,
    min_size: float = 7,
    lineheight: float | None = None,
) -> None:
    size = fontsize
    while size >= min_size:
        rc = page.insert_textbox(
            rect,
            text,
            fontname=fontname,
            fontsize=size,
            color=color,
            align=align,
            lineheight=lineheight,
        )
        if rc >= 0:
            return
        size -= 0.75
    page.insert_textbox(rect, text, fontname=fontname, fontsize=min_size, color=color, align=align)


def draw_corner_border(page: fitz.Page, color: tuple[float, float, float], margin: float = 28) -> None:
    rect = fitz.Rect(margin, margin, LETTER_W - margin, LETTER_H - margin)
    page.draw_rect(rect, color=color, width=0.8)
    length = 38
    width = 1.6
    # outer Ls
    # top left
    page.draw_line((margin, margin), (margin + length, margin), color=color, width=width)
    page.draw_line((margin, margin), (margin, margin + length), color=color, width=width)
    # top right
    page.draw_line((LETTER_W - margin, margin), (LETTER_W - margin - length, margin), color=color, width=width)
    page.draw_line((LETTER_W - margin, margin), (LETTER_W - margin, margin + length), color=color, width=width)
    # bottom left
    page.draw_line((margin, LETTER_H - margin), (margin + length, LETTER_H - margin), color=color, width=width)
    page.draw_line((margin, LETTER_H - margin), (margin, LETTER_H - margin - length), color=color, width=width)
    # bottom right
    page.draw_line((LETTER_W - margin, LETTER_H - margin), (LETTER_W - margin - length, LETTER_H - margin), color=color, width=width)
    page.draw_line((LETTER_W - margin, LETTER_H - margin), (LETTER_W - margin, LETTER_H - margin - length), color=color, width=width)
    # small inner decorative Ls for double treatment (closer to studio reference)
    inner_off = 7
    inner_len = 18
    page.draw_line((margin + inner_off, margin + inner_off), (margin + inner_off + inner_len, margin + inner_off), color=color, width=1.0)
    page.draw_line((margin + inner_off, margin + inner_off), (margin + inner_off, margin + inner_off + inner_len), color=color, width=1.0)
    page.draw_line((LETTER_W - margin - inner_off, margin + inner_off), (LETTER_W - margin - inner_off - inner_len, margin + inner_off), color=color, width=1.0)
    page.draw_line((LETTER_W - margin - inner_off, margin + inner_off), (LETTER_W - margin - inner_off, margin + inner_off + inner_len), color=color, width=1.0)
    page.draw_line((margin + inner_off, LETTER_H - margin - inner_off), (margin + inner_off + inner_len, LETTER_H - margin - inner_off), color=color, width=1.0)
    page.draw_line((margin + inner_off, LETTER_H - margin - inner_off), (margin + inner_off, LETTER_H - margin - inner_off - inner_len), color=color, width=1.0)
    page.draw_line((LETTER_W - margin - inner_off, LETTER_H - margin - inner_off), (LETTER_W - margin - inner_off - inner_len, LETTER_H - margin - inner_off), color=color, width=1.0)
    page.draw_line((LETTER_W - margin - inner_off, LETTER_H - margin - inner_off), (LETTER_W - margin - inner_off, LETTER_H - margin - inner_off - inner_len), color=color, width=1.0)


def _radial_cover_bg(w: float, h: float) -> fitz.Pixmap:
    """Create a smooth radial gradient pixmap matching the .cover-page CSS in pdf_design_studio.html
    to eliminate banding and circular glare artifacts from solid rect approximations.
    """
    if Image is None:
        pm = fitz.Pixmap(fitz.csRGB, (int(w), int(h)))
        pm.fill((0x26, 0, 0))
        return pm
    img = Image.new('RGB', (int(w), int(h)), (0x26, 0, 0))
    pixels = img.load()
    cx, cy = w / 2.0, h * 0.35
    max_dist = max(cx, w - cx, cy, h * 0.65) * 1.1 or 1.0
    stops = [
        (0.0, (0x8B, 0x15, 0x15)),
        (0.65, (0x5b, 0, 0)),
        (1.0, (0x26, 0, 0)),
    ]
    for y in range(int(h)):
        for x in range(int(w)):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 / max_dist
            if dist <= stops[1][0]:
                t = dist / stops[1][0] if stops[1][0] > 0 else 0
                r = int(stops[0][1][0] + t * (stops[1][1][0] - stops[0][1][0]))
                g = int(stops[0][1][1] + t * (stops[1][1][1] - stops[0][1][1]))
                b = int(stops[0][1][2] + t * (stops[1][1][2] - stops[0][1][2]))
            else:
                t = (dist - stops[1][0]) / (1.0 - stops[1][0])
                r = int(stops[1][1][0] + t * (stops[2][1][0] - stops[1][1][0]))
                g = int(stops[1][1][1] + t * (stops[2][1][1] - stops[1][1][1]))
                b = int(stops[1][1][2] + t * (stops[2][1][2] - stops[1][1][2]))
            # vignette from the ::after
            v = max(0.0, min(1.0, (dist - 0.4) / 0.6))
            r = int(r * (1 - 0.4 * v))
            g = int(g * (1 - 0.4 * v))
            b = int(b * (1 - 0.4 * v))
            pixels[x, y] = (r, g, b)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return fitz.Pixmap(buf.getvalue())


def draw_cover(
    out_doc: fitz.Document,
    rel: Path,
    src_doc: fitz.Document,
    assets: dict[str, object],
) -> None:
    lane = lane_for_rel(rel)
    info = lane_info(lane)
    title, subtitle = infer_cover(rel, src_doc)

    page = out_doc.new_page(width=LETTER_W, height=LETTER_H)
    put_font(page, assets)

    # Exact smooth radial background from .cover-page CSS in pdf_design_studio.html
    # Eliminates banding and circular glare/artifact from solid rect approximations.
    bg = _radial_cover_bg(LETTER_W, LETTER_H)
    page.insert_image(page.rect, pixmap=bg)

    # .frame double gold border (outer 2px, inner 1.15px) from the studio HTML
    fm = 0.22 * 72
    page.draw_rect(fitz.Rect(fm, fm, LETTER_W - fm, LETTER_H - fm), color=GOLD, width=2.0)
    im = 0.075 * 72
    page.draw_rect(fitz.Rect(fm + im, fm + im, LETTER_W - fm - im, LETTER_H - fm - im), color=GOLD, width=1.15)

    draw_corner_border(page, GOLD_DARK, 0.29 * 72)

    # Side labels vertical (exact from .side-label and the HTML cover for binder)
    side_gold = (0.85, 0.70, 0.10)
    fs = 5.0
    left_label = "CNA / CDPH APPLICATION BINDER" if lane == "cna" else f"{lane.upper()} APPLICATION"
    right_label = "DRAFT / PENDING APPROVAL"
    start_y = 1.52 * 72
    x_l = 0.45 * 72
    for i, c in enumerate(left_label):
        page.insert_text((x_l, start_y + i * (fs * 0.65)), c, fontsize=fs, color=side_gold, fontname="RobotoRegular")
    x_r = LETTER_W - 0.45 * 72 - fs * 0.4
    for i, c in enumerate(right_label):
        page.insert_text((x_r, start_y + i * (fs * 0.65)), c, fontsize=fs, color=side_gold, fontname="RobotoRegular")

    # Logo + logo-aura exact from CSS (.logo top 0.45in size 3.18in centered, .logo-aura 3.75in with border opacity .45)
    # Drop-shadow approximated by the aura and placement. This + radial bg eliminates glare/artifact.
    logo_w = 3.18 * 72
    logo_h = 3.18 * 72
    logo_x = (LETTER_W - logo_w) / 2
    logo_y = 0.45 * 72
    aura_w = 3.75 * 72
    aura_h = 3.55 * 72
    aura_x = (LETTER_W - aura_w) / 2
    aura_y = 0.29 * 72
    # aura as circle (close to the oval in CSS; draw_circle is supported)
    page.draw_circle(((aura_x + aura_w/2), (aura_y + aura_h/2)), (aura_w + aura_h)/4 , color=(0.92, 0.82, 0.35), width=0.7)
    page.insert_image(fitz.Rect(logo_x, logo_y, logo_x + logo_w, logo_y + logo_h), pixmap=assets["white_logomark"], keep_proportion=True)

    # Small CI INSTITUTE header (from the studio cover HTML)
    insert_text_fit(
        page,
        fitz.Rect(48, 20, LETTER_W - 48, 40),
        "CI INSTITUTE OF NURSING",
        "RobotoRegular",
        8.2,
        GOLD,
        fitz.TEXT_ALIGN_CENTER,
    )

    # Title stack exact from .title-stack top 3.9in in studio HTML + the cover #p1 content
    # Matches the design studio screenshot and HTML for the CNA binder (and layout for others)
    ts_top = 3.9 * 72
    ts_w = 6.72 * 72
    ts_x = (LETTER_W - ts_w) / 2
    # h2 .title-california metallic-white
    insert_text_fit(page, fitz.Rect(ts_x, ts_top, ts_x + ts_w, ts_top + 22), "California", "RobotoLight", 21, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    # h1 .title-main metallic-white (uses the studio-matched title from infer_cover for binder)
    insert_text_fit(page, fitz.Rect(ts_x, ts_top + 24, ts_x + ts_w, ts_top + 58), title, "RobotoLight", 35, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    # .binder-title
    insert_text_fit(page, fitz.Rect(ts_x, ts_top + 60, ts_x + ts_w, ts_top + 78), subtitle, "RobotoRegular", 17, GOLD, fitz.TEXT_ALIGN_CENTER)
    # .subtitle
    insert_text_fit(page, fitz.Rect(ts_x, ts_top + 80, ts_x + ts_w, ts_top + 92), "Online CE — Signer-Review Binder", "RobotoRegular", 9, (0.90, 0.90, 0.90), fitz.TEXT_ALIGN_CENTER)

    # facts-line + source-note + .rule with .rule-mark (diamond)
    insert_text_fit(page, fitz.Rect(ts_x, ts_top + 100, ts_x + ts_w, ts_top + 115), " | ".join(info.get("chips", ["24 Online CE Hours", "12 Units × 2 Hours", "Source Backbone: CCCCO/NATP 10–17"])), "RobotoRegular", 8, (0.95, 0.95, 0.95), fitz.TEXT_ALIGN_CENTER)
    insert_text_fit(page, fitz.Rect(ts_x, ts_top + 118, ts_x + ts_w, ts_top + 130), "CCCCO / NATP source backbone · learner-facing structure remains U01–U12", "RobotoRegular", 6, (0.70, 0.70, 0.70), fitz.TEXT_ALIGN_CENTER)
    rule_y = ts_top + 140
    page.draw_line((ts_x + 50, rule_y), (ts_x + ts_w - 50, rule_y), color=GOLD, width=0.6)
    # rule-mark diamond
    dm = LETTER_W / 2
    s = 3.5
    page.draw_line((dm, rule_y - s), (dm + s, rule_y), color=GOLD, width=0.8)
    page.draw_line((dm + s, rule_y), (dm, rule_y + s), color=GOLD, width=0.8)
    page.draw_line((dm, rule_y + s), (dm - s, rule_y), color=GOLD, width=0.8)
    page.draw_line((dm - s, rule_y), (dm, rule_y - s), color=GOLD, width=0.8)

    # status-text exact from studio HTML at ~8.5in
    stat_y = 8.5 * 72
    insert_text_fit(page, fitz.Rect(50, stat_y, LETTER_W - 50, stat_y + 16), "Status: " + str(info["status"]), "RobotoRegular", 11, (1, 1, 1), fitz.TEXT_ALIGN_CENTER)
    insert_text_fit(page, fitz.Rect(50, stat_y + 18, LETTER_W - 50, stat_y + 30), "Ready for verification, signature, and submission review.", "RobotoRegular", 7, (0.80, 0.80, 0.80), fitz.TEXT_ALIGN_CENTER)

    # provider-stack + prepared-line from studio HTML (provider at ~7.0in)
    prov_y = 7.0 * 72
    insert_text_fit(page, fitz.Rect(50, prov_y, LETTER_W - 50, prov_y + 18), "CI Institute of Nursing, Inc.", "RobotoRegular", 11, (0.95, 0.95, 0.95), fitz.TEXT_ALIGN_CENTER)
    insert_text_fit(page, fitz.Rect(50, prov_y + 20, LETTER_W - 50, prov_y + 32), "Prepared by TJ Padilla · June 9, 2026", "RobotoRegular", 7, GOLD, fitz.TEXT_ALIGN_CENTER)

    # footer-note from studio HTML
    insert_text_fit(page, fitz.Rect(30, 10.7 * 72, LETTER_W - 30, 10.85 * 72), "No public approval claim, enrollment for approved credit, or certificate release is authorized until applicable agency approval metadata is issued.", "RobotoRegular", 5.5, (0.60, 0.60, 0.60), fitz.TEXT_ALIGN_CENTER)


def draw_light_shell(page: fitz.Page, rel: Path, assets: dict[str, object], page_label: str) -> None:
    put_font(page, assets)
    page.draw_rect(page.rect, color=CREAM, fill=CREAM)
    draw_corner_border(page, GOLD_DARK, 26)
    page.insert_image(fitz.Rect(45, 32, 165, 79), pixmap=assets["original_logo"], keep_proportion=True)

    lane = lane_for_rel(rel)
    info = lane_info(lane)
    doc_title = title_from_stem(rel.stem)
    insert_text_fit(
        page,
        fitz.Rect(188, 34, LETTER_W - 52, 55),
        doc_title,
        "RobotoRegular",
        9.6,
        MAROON,
        fitz.TEXT_ALIGN_RIGHT,
    )
    insert_text_fit(
        page,
        fitz.Rect(188, 56, LETTER_W - 52, 73),
        str(info["status"]),
        "RobotoLight",
        8.2,
        MUTED,
        fitz.TEXT_ALIGN_RIGHT,
    )
    page.draw_line((54, 91), (LETTER_W - 54, 91), color=GOLD_DARK, width=0.9)
    page.draw_rect(fitz.Rect(45, 101, LETTER_W - 45, 752), color=BORDER, fill=WARM_WHITE, width=0.5)
    page.draw_line((54, 766), (LETTER_W - 54, 766), color=GOLD_DARK, width=0.5)
    insert_text_fit(
        page,
        fitz.Rect(56, 770, LETTER_W - 56, 784),
        f"CI-created page | {page_label}",
        "RobotoLight",
        7,
        MUTED,
        fitz.TEXT_ALIGN_CENTER,
    )


def draw_ci_page(
    out_doc: fitz.Document,
    src_doc: fitz.Document,
    src_index: int,
    rel: Path,
    assets: dict[str, object],
    page_label: str,
) -> None:
    page = out_doc.new_page(width=LETTER_W, height=LETTER_H)
    draw_light_shell(page, rel, assets, page_label)

    src_page = src_doc[src_index]
    src_rect = src_page.rect
    clip = fitz.Rect(42, 58, src_rect.width - 42, src_rect.height - 57)
    if clip.width <= 0 or clip.height <= 0:
        clip = src_rect
    dest = fitz.Rect(54, 101, LETTER_W - 54, 748)
    page.show_pdf_page(dest, src_doc, src_index, clip=clip, keep_proportion=True)


def draw_appendix_divider(out_doc: fitz.Document, rel: Path, lane: str, assets: dict[str, object]) -> None:
    page = out_doc.new_page(width=LETTER_W, height=LETTER_H)
    draw_light_shell(page, rel, assets, "Appendix divider")
    info = lane_info(lane)
    page.draw_rect(fitz.Rect(70, 178, LETTER_W - 70, 548), color=BORDER, fill=CREAM, width=0.5)
    page.draw_line((100, 252), (LETTER_W - 100, 252), color=GOLD_DARK, width=1.2)
    insert_text_fit(
        page,
        fitz.Rect(88, 202, LETTER_W - 88, 244),
        "Official Government Forms Appendix",
        "RobotoLight",
        23,
        MAROON,
        fitz.TEXT_ALIGN_CENTER,
        min_size=16,
    )
    body = (
        "Official government forms are appended as original unbranded PDF pages. "
        "No CI styling, headers, footers, borders, watermarks, page numbers, or visual alterations have been applied."
    )
    insert_text_fit(
        page,
        fitz.Rect(98, 292, LETTER_W - 98, 370),
        body,
        "RobotoRegular",
        12,
        DARK_TEXT,
        fitz.TEXT_ALIGN_CENTER,
        min_size=9,
        lineheight=1.15,
    )
    insert_text_fit(
        page,
        fitz.Rect(100, 410, LETTER_W - 100, 448),
        str(info["status"]),
        "RobotoRegular",
        11,
        MAROON,
        fitz.TEXT_ALIGN_CENTER,
    )


def source_has_appendix_divider(src_doc: fitz.Document, last_ci_page_count: int) -> bool:
    if last_ci_page_count < 1 or last_ci_page_count > src_doc.page_count:
        return False
    text = src_doc[last_ci_page_count - 1].get_text("text")
    return "APPENDIX" in text.upper() and "OFFICIAL GOVERNMENT FORMS" in text.upper()


def generate_ci_pdf(src_pdf: Path, out_pdf: Path, rel: Path, assets: dict[str, object], ci_pages: int | None = None) -> int:
    src_doc = fitz.open(src_pdf)
    if src_doc.page_count < 1:
        die(f"PDF has no pages: {rel_posix(rel)}")
    count = ci_pages if ci_pages is not None else src_doc.page_count
    if count > src_doc.page_count:
        die(f"Requested CI page split exceeds page count: {rel_posix(rel)}")

    out_doc = fitz.open()
    draw_cover(out_doc, rel, src_doc, assets)
    for i in range(1, count):
        draw_ci_page(out_doc, src_doc, i, rel, assets, f"Source page {i + 1}")

    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    out_doc.save(out_pdf, garbage=4, deflate=True, clean=True)
    out_doc.close()
    src_doc.close()
    return count


def generate_mixed_pdf(src_pdf: Path, out_pdf: Path, rel: Path, lane: str, ci_pages: int, assets: dict[str, object]) -> dict[str, object]:
    official_src = SRC / OFFICIAL_FORMS[lane]
    if not official_src.exists():
        die(f"Missing original official government form PDF for {lane}: {official_src}")

    src_doc = fitz.open(src_pdf)
    ci_doc = fitz.open()

    draw_cover(ci_doc, rel, src_doc, assets)
    for i in range(1, ci_pages):
        draw_ci_page(ci_doc, src_doc, i, rel, assets, f"Source page {i + 1}")

    inserted_divider = False
    if not source_has_appendix_divider(src_doc, ci_pages):
        draw_appendix_divider(ci_doc, rel, lane, assets)
        inserted_divider = True

    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    ci_tmp = Path(tempfile.gettempdir()) / ("ci_ion_ci_part_" + hashlib.sha256(str(out_pdf).encode("utf-8")).hexdigest()[:16] + ".pdf")
    if ci_tmp.exists():
        ci_tmp.unlink()
    ci_doc.save(ci_tmp, garbage=4, deflate=True, clean=True)
    ci_pages_out = ci_doc.page_count
    ci_doc.close()
    src_doc.close()

    # Use pypdf for the final merge so appended government-form page content streams
    # are copied without MuPDF cleaning or restyling.
    ci_reader = PdfReader(str(ci_tmp))
    official_reader = PdfReader(str(official_src))
    writer = PdfWriter()
    for page in ci_reader.pages:
        writer.add_page(page)
    for page in official_reader.pages:
        writer.add_page(page)
    with out_pdf.open("wb") as handle:
        writer.write(handle)

    official_start = ci_pages_out
    result = {
        "lane": lane,
        "ci_pages": ci_pages,
        "inserted_divider": inserted_divider,
        "official_source": rel_posix(OFFICIAL_FORMS[lane]),
        "official_pages": len(official_reader.pages),
        "official_start_page": official_start + 1,
        "output_pages": len(ci_reader.pages) + len(official_reader.pages),
    }
    if getattr(ci_reader, "stream", None):
        ci_reader.stream.close()
    if getattr(official_reader, "stream", None):
        official_reader.stream.close()
    ci_tmp.unlink(missing_ok=True)
    return result


def copy_non_pdf_files(files: list[Path], summary: dict[str, object]) -> None:
    copied = 0
    for path in files:
        rel = path.relative_to(SRC)
        dest = BUILD / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
        copied += 1
    summary["non_pdf_copied"] = copied


def render_page(path: Path, page_index: int, out_png: Path, zoom: float = 1.0) -> None:
    doc = fitz.open(path)
    try:
        page = doc[page_index]
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), colorspace=fitz.csRGB, alpha=False)
        out_png.parent.mkdir(parents=True, exist_ok=True)
        pix.save(out_png)
    finally:
        doc.close()


def render_samples(out_pdfs: list[Path], mixed_details: dict[str, dict[str, object]]) -> dict[str, object]:
    if QA_DIR.exists():
        shutil.rmtree(QA_DIR)
    QA_DIR.mkdir(parents=True, exist_ok=True)
    rendered = 0
    issues: list[str] = []
    for pdf in out_pdfs:
        rel = pdf.relative_to(BUILD)
        doc = fitz.open(pdf)
        try:
            if doc.page_count < 1:
                issues.append(f"No pages: {rel_posix(rel)}")
                continue
            indexes = {0, doc.page_count // 2}
            detail = mixed_details.get(rel_posix(rel))
            if detail:
                start = int(detail["official_start_page"]) - 1
                indexes.add(max(0, start - 1))
                indexes.update(range(start, doc.page_count))
            for idx in sorted(i for i in indexes if 0 <= i < doc.page_count):
                out_png = QA_DIR / rel.with_suffix("") / f"page_{idx + 1:03d}.png"
                pix = doc[idx].get_pixmap(matrix=fitz.Matrix(0.8, 0.8), colorspace=fitz.csRGB, alpha=False)
                out_png.parent.mkdir(parents=True, exist_ok=True)
                pix.save(out_png)
                rendered += 1
                # Simple nonblank guard for generated CI pages.
                if not detail or idx < int(detail["official_start_page"]) - 1:
                    sample = pix.samples
                    if len(set(sample[0:: max(1, len(sample) // 5000)])) <= 2:
                        issues.append(f"Possible blank render: {rel_posix(rel)} page {idx + 1}")
        finally:
            doc.close()
    return {"sample_pages_rendered": rendered, "qa_render_dir": str(QA_DIR), "issues": issues}


def compare_official_pages(mixed_details: dict[str, dict[str, object]]) -> dict[str, object]:
    comparisons = 0
    issues: list[str] = []
    for rel_text, detail in mixed_details.items():
        out_pdf = BUILD / Path(rel_text)
        official_src = SRC / Path(str(detail["official_source"]))
        out_doc = fitz.open(out_pdf)
        src_doc = fitz.open(official_src)
        try:
            start = int(detail["official_start_page"]) - 1
            if out_doc.page_count - start != src_doc.page_count:
                issues.append(f"Official page count mismatch in {rel_text}")
                continue
            for i in range(src_doc.page_count):
                src_pix = src_doc[i].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                out_pix = out_doc[start + i].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                comparisons += 1
                if src_pix.width != out_pix.width or src_pix.height != out_pix.height:
                    issues.append(f"Official render dimension mismatch in {rel_text} page {start + i + 1}")
                    continue
                if src_pix.samples != out_pix.samples:
                    issues.append(f"Official render pixel mismatch in {rel_text} page {start + i + 1}")
        finally:
            out_doc.close()
            src_doc.close()
    return {"official_pages_compared": comparisons, "issues": issues}


def validate_pdfs(out_pdfs: list[Path]) -> dict[str, object]:
    page_counts: dict[str, int] = {}
    issues: list[str] = []
    for pdf in out_pdfs:
        rel = pdf.relative_to(BUILD)
        try:
            reader = PdfReader(str(pdf))
            count = len(reader.pages)
            page_counts[rel_posix(rel)] = count
            with fitz.open(pdf) as doc:
                if doc.page_count != count:
                    issues.append(f"Reader/page render count mismatch: {rel_posix(rel)}")
        except Exception as exc:
            issues.append(f"Open/check failed for {rel_posix(rel)}: {exc!r}")
    return {"page_counts": page_counts, "issues": issues}


def main() -> None:
    if not SRC.exists():
        die(f"Source folder does not exist: {SRC}")
    if not DESIGN_HTML.exists():
        die(f"Design HTML does not exist: {DESIGN_HTML}")
    if OUT.exists():
        die(f"Output folder already exists; refusing to overwrite: {OUT}")
    if BUILD.exists():
        die(f"Temporary build folder already exists; remove or inspect before rerun: {BUILD}")

    for rel in OFFICIAL_FORMS.values():
        if not (SRC / rel).exists():
            die(f"Missing standalone original government-form PDF: {rel_posix(rel)}")

    assets = prepare_assets()
    BUILD.mkdir(parents=True)

    pdf_files = sorted(SRC.rglob("*.pdf"))
    non_pdf_files = sorted(path for path in SRC.rglob("*") if path.is_file() and path.suffix.lower() != ".pdf")
    official_only = set(OFFICIAL_FORMS.values())

    summary: dict[str, object] = {
        "source_folder_verified": True,
        "design_html_verified": True,
        "source_pdf_count": len(pdf_files),
        "source_non_pdf_count": len(non_pdf_files),
        "official_forms_copied_unchanged": 0,
        "mixed_binders_corrected": 0,
        "pdfs_redesigned": 0,
        "ci_created_pdfs": 0,
        "course_material_packets": 0,
        "tracker_checklist_index_pdfs": 0,
        "moodle_support_pdfs": 0,
        "files_skipped": [],
        "missing_original_government_forms": [],
    }

    copy_non_pdf_files(non_pdf_files, summary)

    mixed_details: dict[str, dict[str, object]] = {}
    generated_pdfs: list[Path] = []
    official_hashes: dict[str, dict[str, str]] = {}

    for src_pdf in pdf_files:
        rel = src_pdf.relative_to(SRC)
        out_pdf = BUILD / rel
        rel_s = rel_posix(rel)

        if rel in official_only:
            out_pdf.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_pdf, out_pdf)
            summary["official_forms_copied_unchanged"] = int(summary["official_forms_copied_unchanged"]) + 1
            official_hashes[rel_s] = {"source": sha256(src_pdf), "output": sha256(out_pdf)}
            generated_pdfs.append(out_pdf)
            continue

        if rel in MIXED:
            lane, ci_pages = MIXED[rel]
            detail = generate_mixed_pdf(src_pdf, out_pdf, rel, lane, ci_pages, assets)
            mixed_details[rel_s] = detail
            summary["mixed_binders_corrected"] = int(summary["mixed_binders_corrected"]) + 1
            summary["pdfs_redesigned"] = int(summary["pdfs_redesigned"]) + 1
            generated_pdfs.append(out_pdf)
            continue

        generate_ci_pdf(src_pdf, out_pdf, rel, assets)
        summary["pdfs_redesigned"] = int(summary["pdfs_redesigned"]) + 1
        summary["ci_created_pdfs"] = int(summary["ci_created_pdfs"]) + 1
        rel_upper = rel_s.upper()
        if "COURSE_MATERIALS" in rel_upper:
            summary["course_material_packets"] = int(summary["course_material_packets"]) + 1
        if any(k in rel_upper for k in ("TRACKER", "CHECKLIST", "INDEX", "MISSING_OR_PENDING")):
            summary["tracker_checklist_index_pdfs"] = int(summary["tracker_checklist_index_pdfs"]) + 1
        if "MOODLE" in rel_upper:
            summary["moodle_support_pdfs"] = int(summary["moodle_support_pdfs"]) + 1
        generated_pdfs.append(out_pdf)

    official_hash_mismatches = [
        rel for rel, hashes in official_hashes.items() if hashes["source"] != hashes["output"]
    ]
    if official_hash_mismatches:
        die(f"Copied official government form hash mismatch: {official_hash_mismatches}")

    validation = validate_pdfs(generated_pdfs)
    compare = compare_official_pages(mixed_details)
    render = render_samples(generated_pdfs, mixed_details)

    qa_issues = []
    qa_issues.extend(validation["issues"])
    qa_issues.extend(compare["issues"])
    qa_issues.extend(render["issues"])
    if qa_issues:
        print(json.dumps({"status": "qa_failed", "issues": qa_issues}, indent=2))
        sys.exit(3)

    BUILD.rename(OUT)

    summary["output_folder_created"] = str(OUT)
    summary["page_counts"] = validation["page_counts"]
    summary["mixed_details"] = mixed_details
    summary["official_form_hashes_identical"] = True
    summary["official_page_visual_comparison"] = compare
    summary["qa_rendering"] = render
    summary["confirmation"] = "Official government forms were copied or appended as original unbranded PDF pages without CI overlays."
    print(json.dumps({"status": "complete", "summary": summary}, indent=2))


if __name__ == "__main__":
    main()
