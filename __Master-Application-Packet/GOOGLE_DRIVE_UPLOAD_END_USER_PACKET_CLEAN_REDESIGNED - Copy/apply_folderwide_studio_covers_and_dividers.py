from __future__ import annotations

import base64
import hashlib
import json
import shutil
import subprocess
import tempfile
import urllib.request
from pathlib import Path

import fitz
from bs4 import BeautifulSoup
from pypdf import PdfReader, PdfWriter


ROOT = Path(r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet")
SOURCE_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN - Copy - Copy"
OUTPUT_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED - Copy"
STUDIO_HTML = ROOT / "PDF_Design_Studio" / "pdf_design_studio.html"
QA_DIR = Path(tempfile.gettempdir()) / "ci_ion_folderwide_studio_covers_qa"

LOGO_URL = "https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg"
CHROME_CANDIDATES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]

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

TITLE_MAP = {
    "00_YADVIR_READ_ME_FIRST_COMPLETE_GUIDE": ("Start Here", "Read Me First"),
    "01_MASTER_END_USER_PACKET_INDEX": ("Master Packet Index", "Submission Roadmap"),
    "03_CE_CATALOG_ADDENDUM_AND_WEBSITE_UPDATE_GUIDE": ("CE Catalog Addendum", "Website Update Guide"),
    "01_CNA_CDPH_APPLICATION_BINDER": ("CNA Recertification", "CNA Recert Binder"),
    "02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET": ("CNA / CDPH Minimum Required", "Submission Packet"),
    "04_CNA_CDPH_MISSING_OR_PENDING_SUBMISSION_ITEMS": ("CNA / CDPH Review Context", "Post-Handoff Context"),
    "01_CNA_24HR_12_UNIT_COURSE_MATERIALS_COMPILED": ("CNA Course Materials", "24 Hour / 12 Unit Packet"),
    "02_CNA_COURSE_MATRIX_AND_SOURCE_CROSSWALK": ("CNA Course Matrix", "Source Crosswalk"),
    "03_CNA_LMS_RAW_COURSE_CONTENT_FOR_POST_SME_BUILD": ("CNA LMS Course Content", "Post-SME Build"),
    "01_RCFE_CDSS_APPLICATION_BINDER": ("RCFE / CDSS Application", "Signer-Review Binder"),
    "02_RCFE_CDSS_MINIMUM_REQUIRED_SUBMISSION_PACKET": ("RCFE / CDSS Minimum Required", "Submission Packet"),
    "04_RCFE_CDSS_MISSING_OR_PENDING_SUBMISSION_ITEMS": ("RCFE / CDSS Review Context", "Post-Handoff Context"),
    "01_RCFE_9_COURSE_27HR_COURSE_MATERIALS_COMPILED": ("RCFE Course Materials", "9 Course / 27 Hour Packet"),
    "02_RCFE_COURSE_MATRIX_AND_DEMENTIA_BLOCK": ("RCFE Course Matrix", "Dementia Block"),
    "03_RCFE_LMS_RAW_COURSE_CONTENT_FOR_POST_SME_BUILD": ("RCFE LMS Course Content", "Post-SME Build"),
    "01_BRN_CEP_APPLICATION_BINDER": ("BRN CEP Application", "Signer-Review Binder"),
    "02_BRN_CEP_MINIMUM_REQUIRED_SUBMISSION_PACKET": ("BRN CEP Minimum Required", "Submission Packet"),
    "04_BRN_CEP_MISSING_OR_PENDING_SUBMISSION_ITEMS": ("BRN CEP Review Context", "Post-Handoff Context"),
    "01_BRN_30_CONTACT_HOUR_COURSE_MATERIALS_COMPILED": ("BRN Course Materials", "30 Contact Hour Packet"),
    "02_BRN_CONTACT_HOUR_MAP_AND_REPRESENTATIVE_COURSE_PACKET": ("BRN Contact Hour Map", "Representative Course Packet"),
    "03_BRN_LMS_RAW_COURSE_CONTENT_FOR_POST_SME_BUILD": ("BRN LMS Course Content", "Post-SME Build"),
    "01_MOODLE_SELF_HOST_IMPLEMENTATION_REQUIREMENTS_ONLY": ("Moodle Requirements", "Self-Host Implementation"),
    "01_POST_SME_MOODLE_BUILD_HANDOFF_READ_ME": ("Post-SME Handoff", "Moodle Build Read Me"),
    "02_POST_SME_MOODLE_BUILD_REQUIREMENTS_AND_COURSE_CONTENT_INDEX": ("Moodle Build Index", "Requirements and Course Content"),
}


def fail(message: str) -> None:
    raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rel(path: Path) -> Path:
    return path.relative_to(OUTPUT_ROOT)


def rel_text(path: Path) -> str:
    return str(path).replace("/", "\\")


def page_count(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def chrome_path() -> Path:
    for candidate in CHROME_CANDIDATES:
        if candidate.exists():
            return candidate
    found = shutil.which("chrome") or shutil.which("chrome.exe") or shutil.which("msedge") or shutil.which("msedge.exe")
    if found:
        return Path(found)
    fail("Chrome or Edge was not found.")


def studio_css() -> str:
    soup = BeautifulSoup(STUDIO_HTML.read_text(encoding="utf-8"), "html.parser")
    style = soup.find("style")
    if style is None or style.string is None:
        fail("Could not read CSS from PDF_Design_Studio\\pdf_design_studio.html.")
    return style.string


def logo_src() -> str:
    try:
        request = urllib.request.Request(LOGO_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()
        return "data:image/svg+xml;base64," + base64.b64encode(data).decode("ascii")
    except Exception:
        return LOGO_URL


def lane_for(rel_path: Path) -> str:
    text = rel_text(rel_path).upper()
    if "CNA_CDPH" in text or "\\01_CNA" in text:
        return "cna"
    if "RCFE_CDSS" in text or "\\02_RCFE" in text:
        return "rcfe"
    if "BRN" in text:
        return "brn"
    return "general"


def lane_copy(lane: str) -> dict[str, object]:
    if lane == "cna":
        return {
            "facts": ["24 Online CE Hours", "12 Units × 2 Hours", "Source Backbone: CCCCO/NATP 10–17"],
            "source_note": "CCCCO / NATP source backbone · learner-facing structure remains U01–U12",
            "right_label": "DRAFT / PENDING CDPH APPROVAL",
            "status": "Status: Draft / Pending CDPH Approval",
        }
    if lane == "rcfe":
        return {
            "facts": ["27 Filed Hours", "9 Filed Courses", "RCFE Administrator Continuing Education"],
            "source_note": "Filed-hour structure remains draft / pending CDSS/ACS approval metadata",
            "right_label": "DRAFT / PENDING CDSS/ACS APPROVAL",
            "status": "Status: Draft / Pending CDSS/ACS Approval",
        }
    if lane == "brn":
        return {
            "facts": ["30 Contact Hours", "10 Modules × 3 Contact Hours", "RN Care Manager CEP"],
            "source_note": "Contact-hour structure remains draft / pending BRN CEP approval metadata",
            "right_label": "DRAFT / PENDING BRN CEP APPROVAL",
            "status": "Status: Draft / Pending BRN CEP Approval",
        }
    return {
        "facts": ["CI Institute of Nursing", "Application Packet", "Draft Review Materials"],
        "source_note": "No public approval claim is made unless agency approval metadata is issued",
        "right_label": "DRAFT / PENDING APPROVAL",
        "status": "Status: Draft / Pending Approval",
    }


def title_for(rel_path: Path) -> tuple[str, str]:
    stem = rel_path.stem
    if stem in TITLE_MAP:
        return TITLE_MAP[stem]
    words = stem.replace("_", " ").title()
    return words[:42], "Review Packet"


def side_label_for(rel_path: Path, lane: str, title: str) -> str:
    text = rel_text(rel_path).upper()
    if "APPLICATION_SUBMISSION" in text:
        return f"{lane.upper()} APPLICATION PACKET" if lane != "general" else "APPLICATION PACKET"
    if "COURSE_MATERIALS" in text:
        return f"{lane.upper()} COURSE MATERIALS" if lane != "general" else "COURSE MATERIALS"
    if "MOODLE" in text:
        return "MOODLE IMPLEMENTATION"
    if "START_HERE" in text:
        return "START HERE"
    return title.upper()[:36]


def title_class(title: str) -> str:
    if len(title) >= 34:
        return " xlong-title"
    if len(title) >= 25:
        return " long-title"
    return ""


def cover_page(rel_path: Path, logo: str) -> str:
    lane = lane_for(rel_path)
    copy = lane_copy(lane)
    title, binder_title = title_for(rel_path)
    facts = copy["facts"]
    facts_html = "\n".join(
        f"<span>{item}</span>" + ("""<span class="pipe">|</span>""" if index < len(facts) - 1 else "")
        for index, item in enumerate(facts)
    )
    return f"""
    <div id="p1" class="page cover-page" role="document" aria-label="Binder Cover Page">
      <div class="frame"></div>
      <div class="corner-block tl"></div>
      <div class="corner-block tr"></div>
      <div class="corner-block bl"></div>
      <div class="corner-block br"></div>
      <div class="side-label left">{side_label_for(rel_path, lane, title)}</div>
      <div class="side-label right">{copy['right_label']}</div>

      <div class="cover-content">
        <div class="logo-aura"></div>
        <img class="logo" src="{logo}" alt="CI Institute of Nursing Logo" />
        <div class="title-stack">
          <h2 class="title-california metallic-white">California</h2>
          <h1 class="title-main metallic-white{title_class(title)}">{title}</h1>
          <div class="binder-title">{binder_title}</div>
          <div class="subtitle">Online CE &mdash; Signer-Review Binder</div>
          <div class="facts-line" aria-label="Binder facts">{facts_html}</div>
          <span class="source-note">{copy['source_note']}</span>
          <div class="rule"><span class="rule-mark"></span></div>
        </div>
        <div class="provider-stack">
          <p class="provider-name">CI Institute of Nursing, Inc.</p>
          <div class="prepared-line">Prepared by <strong>TJ Padilla</strong> &middot; June 9, 2026</div>
        </div>
        <div class="status-text" aria-label="Status">
          <div class="status-title">{copy['status']}</div>
          <div class="status-subtitle">Ready for verification, signature, and submission review.</div>
        </div>
      </div>
      <div class="footer-note">
        No public approval claim, enrollment for approved credit, or certificate release is authorized until applicable agency approval metadata is issued.
      </div>
    </div>
    """


def appendix_divider() -> str:
    return """
    <div id="p-divider" class="page divider-page">
      <div class="frame"></div>
      <div class="corner-block tl"></div>
      <div class="corner-block tr"></div>
      <div class="corner-block bl"></div>
      <div class="corner-block br"></div>
      <div class="divider-content">
        <h1 class="divider-title">Appendix</h1>
        <h2 style="color: white; font-size: 16px; font-weight: 300; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 20px;">Official Forms Packet</h2>
        <div class="divider-sub">
          Official government forms are appended as original unbranded PDF pages. No CI styling, headers, footers, borders, watermarks, page numbers, or visual alterations have been applied.
        </div>
      </div>
    </div>
    """


def html_document(body: str, css: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
  <style>
{css}
    .metallic-white {{
      background: none !important;
      -webkit-background-clip: initial !important;
      background-clip: initial !important;
      -webkit-text-fill-color: #f7f7f7 !important;
      color: #f7f7f7 !important;
    }}
    .title-main {{
      white-space: nowrap !important;
    }}
    .title-main.long-title {{
      font-size: 0.365in !important;
      letter-spacing: 0.045em !important;
    }}
    .title-main.xlong-title {{
      font-size: 0.30in !important;
      letter-spacing: 0.025em !important;
    }}
    .divider-page {{
      background: radial-gradient(circle at center, #610000 0%, #3d0000 70%, #1a0000 100%) !important;
    }}
    .page:last-child {{ page-break-after: auto !important; break-after: auto !important; }}
    @media print {{ .page:last-child {{ page-break-after: auto !important; break-after: auto !important; }} }}
  </style>
</head>
<body>
  <main class="document-container">{body}</main>
</body>
</html>
"""


def render_one_page(body: str, pdf: Path, css: str) -> None:
    pdf.unlink(missing_ok=True)
    html = pdf.with_suffix(".html")
    html.write_text(html_document(body, css), encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix="ci_ion_chrome_profile_") as profile:
        command = [
            str(chrome_path()),
            "--headless=new",
            "--disable-gpu",
            "--disable-extensions",
            "--no-first-run",
            "--no-default-browser-check",
            "--no-pdf-header-footer",
            "--print-to-pdf-no-header",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=5000",
            f"--user-data-dir={profile}",
            f"--print-to-pdf={pdf}",
            html.as_uri(),
        ]
        result = subprocess.run(command, capture_output=True, text=True, timeout=90)
    html.unlink(missing_ok=True)
    if result.returncode != 0 or not pdf.exists():
        fail(f"Chrome print-to-PDF failed for {pdf.name}: {result.stderr.strip() or result.stdout.strip()}")
    if page_count(pdf) != 1:
        fail(f"Expected one rendered page for {pdf.name}, got {page_count(pdf)}.")


def replace_pages(target: Path, replacements: dict[int, Path]) -> tuple[str, str]:
    before = sha256(target)
    original = PdfReader(str(target))
    replacement_readers = {index: PdfReader(str(path)) for index, path in replacements.items()}
    writer = PdfWriter()
    for index, page in enumerate(original.pages):
        if index in replacement_readers:
            writer.add_page(replacement_readers[index].pages[0])
        else:
            writer.add_page(page)
    tmp = target.with_suffix(".folderwide-cover.tmp.pdf")
    with tmp.open("wb") as handle:
        writer.write(handle)
    if getattr(original, "stream", None):
        original.stream.close()
    for reader in replacement_readers.values():
        if getattr(reader, "stream", None):
            reader.stream.close()
    tmp.replace(target)
    return before, sha256(target)


def compare_appended_official(candidate: Path, lane: str, official_start_index: int) -> list[str]:
    official = SOURCE_ROOT / OFFICIAL_FORMS[lane]
    issues: list[str] = []
    with fitz.open(candidate) as output_doc, fitz.open(official) as official_doc:
        if output_doc.page_count - official_start_index != official_doc.page_count:
            return ["official appendix page count mismatch"]
        for index in range(official_doc.page_count):
            src = official_doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            out = output_doc[official_start_index + index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            if src.width != out.width or src.height != out.height or src.samples != out.samples:
                issues.append(f"official appendix page {index + 1} render mismatch")
    return issues


def verify_official_only() -> list[str]:
    issues: list[str] = []
    for official_rel in OFFICIAL_ONLY:
        src = SOURCE_ROOT / official_rel
        out = OUTPUT_ROOT / official_rel
        if not src.exists() or not out.exists():
            issues.append(f"official file missing: {official_rel}")
        elif sha256(src) != sha256(out):
            issues.append(f"official file hash mismatch: {official_rel}")
    return issues


def render_qa_samples(updated: list[Path]) -> list[str]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []
    sample = sorted(set(updated))[:8]
    for path in sample:
        try:
            with fitz.open(path) as doc:
                for index in sorted({0, min(1, doc.page_count - 1), doc.page_count - 1}):
                    pix = doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                    out = QA_DIR / f"{path.stem}_p{index + 1:03d}.png"
                    pix.save(out)
                    outputs.append(str(out))
        except Exception:
            continue
    return outputs


def main() -> None:
    if not OUTPUT_ROOT.exists():
        fail(f"Missing output root: {OUTPUT_ROOT}")
    if not SOURCE_ROOT.exists():
        fail(f"Missing source root: {SOURCE_ROOT}")
    if not STUDIO_HTML.exists():
        fail(f"Missing Studio HTML: {STUDIO_HTML}")

    official_issues = verify_official_only()
    if official_issues:
        fail("; ".join(official_issues))

    css = studio_css()
    logo = logo_src()
    work = Path(tempfile.gettempdir()) / "ci_ion_folderwide_cover_pages"
    work.mkdir(parents=True, exist_ok=True)

    updated: list[Path] = []
    skipped: list[dict[str, str]] = []
    results: list[dict[str, object]] = []

    for pdf in sorted(OUTPUT_ROOT.rglob("*.pdf")):
        relative = rel(pdf)
        relative_posix = Path(str(relative).replace("\\", "/"))
        if relative_posix in OFFICIAL_ONLY:
            skipped.append({"rel": rel_text(relative), "reason": "official government form copied unchanged"})
            continue

        cover_pdf = work / (hashlib.sha256(rel_text(relative).encode("utf-8")).hexdigest()[:16] + "_cover.pdf")
        render_one_page(cover_page(relative, logo), cover_pdf, css)
        replacements = {0: cover_pdf}

        official_start_index = None
        lane = MIXED_TO_OFFICIAL.get(relative_posix)
        if lane:
            official_pages = page_count(SOURCE_ROOT / OFFICIAL_FORMS[lane])
            total_pages = page_count(pdf)
            divider_index = total_pages - official_pages - 1
            if divider_index <= 0:
                fail(f"Could not locate appendix divider for {rel_text(relative)}")
            divider_pdf = work / (hashlib.sha256((rel_text(relative) + "_divider").encode("utf-8")).hexdigest()[:16] + "_divider.pdf")
            render_one_page(appendix_divider(), divider_pdf, css)
            replacements[divider_index] = divider_pdf
            official_start_index = divider_index + 1

        before, after = replace_pages(pdf, replacements)
        if lane and official_start_index is not None:
            issues = compare_appended_official(pdf, lane, official_start_index)
            if issues:
                fail(f"{rel_text(relative)}: " + "; ".join(issues))
        updated.append(pdf)
        results.append(
            {
                "rel": rel_text(relative),
                "pages_replaced": [index + 1 for index in sorted(replacements)],
                "previous_sha256": before,
                "new_sha256": after,
            }
        )

    samples = render_qa_samples(updated)
    print(
        json.dumps(
            {
                "status": "complete",
                "updated_pdf_count": len(updated),
                "skipped_official_count": len(skipped),
                "studio_html": str(STUDIO_HTML),
                "official_only_verified": len(OFFICIAL_ONLY),
                "results": results,
                "skipped": skipped,
                "qa_samples": samples,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
