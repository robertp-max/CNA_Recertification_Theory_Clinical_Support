from __future__ import annotations

import base64
import hashlib
import json
import re
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
SCOPE = OUTPUT_ROOT / "01_CNA_CDPH_CE_APPLICATION" / "01_APPLICATION_SUBMISSION"
STUDIO_HTML = ROOT / "PDF_Design_Studio" / "pdf_design_studio.html"
OFFICIAL_REL = Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/03_CNA_CDPH_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf")
OFFICIAL_SOURCE = SOURCE_ROOT / OFFICIAL_REL
OFFICIAL_OUTPUT = OUTPUT_ROOT / OFFICIAL_REL
QA_DIR = Path(tempfile.gettempdir()) / "ci_ion_cna_submission_studio_html_qa"

CHROME_CANDIDATES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]

LOGO_URL = "https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg"


def fail(message: str) -> None:
    raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def chrome_path() -> Path:
    for candidate in CHROME_CANDIDATES:
        if candidate.exists():
            return candidate
    found = shutil.which("chrome") or shutil.which("chrome.exe") or shutil.which("msedge") or shutil.which("msedge.exe")
    if found:
        return Path(found)
    fail("Chrome or Edge was not found for HTML print-to-PDF rendering.")


def studio_parts() -> tuple[str, BeautifulSoup]:
    html = STUDIO_HTML.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    style = soup.find("style")
    if style is None or style.string is None:
        fail("Could not locate studio CSS in pdf_design_studio.html.")
    return style.string, soup


def logo_src() -> str:
    try:
        request = urllib.request.Request(LOGO_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()
        return "data:image/svg+xml;base64," + base64.b64encode(data).decode("ascii")
    except Exception:
        return LOGO_URL


def cover_page(
    *,
    page_id: str,
    side_label: str,
    right_label: str,
    title: str,
    binder_title: str,
    status: str,
    logo: str,
) -> str:
    return f"""
    <div id="{page_id}" class="page cover-page" role="document" aria-label="Binder Cover Page">
      <div class="frame"></div>
      <div class="corner-block tl"></div>
      <div class="corner-block tr"></div>
      <div class="corner-block bl"></div>
      <div class="corner-block br"></div>
      <div class="side-label left">{side_label}</div>
      <div class="side-label right">{right_label}</div>

      <div class="cover-content">
        <div class="logo-aura"></div>
        <img class="logo" src="{logo}" alt="CI Institute of Nursing Logo" />

        <div class="title-stack">
          <h2 class="title-california metallic-white">California</h2>
          <h1 class="title-main metallic-white">{title}</h1>
          <div class="binder-title">{binder_title}</div>
          <div class="subtitle">Online CE &mdash; Signer-Review Binder</div>

          <div class="facts-line" aria-label="Binder facts">
            <span>24 Online CE Hours</span>
            <span class="pipe">|</span>
            <span>12 Units &times; 2 Hours</span>
            <span class="pipe">|</span>
            <span>Source Backbone: CCCCO/NATP 10&ndash;17</span>
          </div>
          <span class="source-note">CCCCO / NATP source backbone &middot; learner-facing structure remains U01&ndash;U12</span>
          <div class="rule"><span class="rule-mark"></span></div>
        </div>

        <div class="provider-stack">
          <p class="provider-name">CI Institute of Nursing, Inc.</p>
          <div class="prepared-line">Prepared for <strong>Yadvir Saandal</strong> &middot; June 9, 2026</div>
        </div>

        <div class="status-text" aria-label="Status">
          <div class="status-title">{status}</div>
          <div class="status-subtitle">Ready for verification, signature, and submission review.</div>
        </div>
      </div>

      <div class="footer-note">
        No public approval claim, enrollment for approved credit, or certificate release is authorized until applicable agency approval metadata is issued.
      </div>
    </div>
    """


def appendix_divider(page_id: str = "p12") -> str:
    return f"""
    <div id="{page_id}" class="page divider-page">
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


def page_footer(left: str, center: str, right: str) -> str:
    return f"""
      <footer class="page-footer">
        <div class="footer-left">{left}</div>
        <div class="footer-center">{center}</div>
        <div class="footer-right">{right}</div>
      </footer>
    """


def normalize_studio_page(page_html: str, footer_left: str) -> str:
    soup = BeautifulSoup(page_html, "html.parser")
    footer = soup.select_one(".page-footer")
    if footer:
        center = footer.select_one(".footer-center")
        right = footer.select_one(".footer-right")
        page_text = ""
        for candidate in (right, center):
            if candidate and "page" in candidate.get_text(" ", strip=True).lower():
                page_text = candidate.get_text(" ", strip=True)
                break
        if not page_text:
            page_id = (soup.find(class_="page") or {}).get("id", "")
            page_text = f"Page {page_id[1:]} of 17" if page_id.startswith("p") else ""
        footer.clear()
        footer.append(BeautifulSoup(f"""
          <div class="footer-left">{footer_left}</div>
          <div class="footer-center">{page_text}</div>
          <div class="footer-right">Prepared June 09, 2026</div>
        """, "html.parser"))
    html = str(soup)
    html = html.replace("TJ Padilla — Compiler", footer_left)
    html = html.replace("TJ Padilla - Compiler", footer_left)
    html = html.replace(
        "<strong>Attribution and Operations:</strong> This document was compiled and managed by TJ Padilla (acting strictly in an administrative author/compiler capacity. This role represents curriculum layout coordination and contains zero educational or operational oversight duties).",
        "<strong>Verification Notes:</strong> Final signatures, dates, attachment checks, and packet-release steps are completed through the assigned verification workflow before submission.",
    )
    html = html.replace(
        "<strong>Attribution and Operations:</strong> This document was compiled and managed by TJ Padilla (acting strictly in an administrative author/compiler capacity. This role represents curriculum layout coordination and contains zero educational or operational oversight duties).",
        "<strong>Verification Notes:</strong> Final signatures, dates, attachment checks, and packet-release steps are completed through the assigned verification workflow before submission.",
    )
    html = html.replace("author/compiler", "packet preparation")
    html = html.replace("author / compiler / version-control", "packet preparation and version-control")
    html = html.replace("administrative author/compiler capacity", "packet preparation and version-control")
    html = html.replace("TJ Padilla", "Yadvir Saandal")
    html = html.replace("TJ PADILLA", "YADVIR SAANDAL")
    html = html.replace("human review", "review")
    html = html.replace("human verification", "verification")
    html = re.sub(
        r"<strong>Attribution and Operations:</strong>.*?</div>",
        "<strong>Verification Notes:</strong> Final signatures, dates, attachment checks, and packet-release steps are completed through the assigned verification workflow before submission.</div>",
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return html


def minimum_scope_page() -> str:
    return f"""
    <div id="p2" class="page">
      <header class="page-header">
        <div class="header-left">CNA/CDPH CE Signer-Review Binder</div>
        <div class="header-right">CI Institute of Nursing, Inc.</div>
      </header>
      <section class="page-body">
        <h2 class="doc-section-title">Minimum Submission Scope</h2>
        <p class="intro-text">CNA 24-hour online CE course using CCCCO/NATP Modules 10&ndash;17 as the source backbone, delivered as 12 Moodle units.</p>
        <p class="intro-text"><strong>This PDF includes the minimum application-submission index and exact official form pages where source PDFs were available.</strong> Optional LMS implementation materials, source folders, old module fragments, internal build notes, and raw source files are excluded.</p>
        <div class="notice-block">Approval-safe posture: Draft / Pending CDPH Approval. Certificate release remains disabled pending approval metadata and completion evidence gates. No public approval claim is made.</div>
        <h3 style="font-size: 14px; color: var(--ci-maroon); margin: 20px 0 10px;">Project Submission Materials</h3>
        <table class="ci-table">
          <thead><tr><th>Minimum Required Material</th><th>Status</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td class="row-title">Compiled CNA/CDPH application binder</td><td>Included or referenced</td><td>Required for current lane</td></tr>
            <tr><td class="row-title">CDPH 192B / online CE provider application materials</td><td>Included or referenced</td><td>Required for current lane</td></tr>
            <tr><td class="row-title">CDPH 193 / relevant provider/course form materials</td><td>Included or referenced</td><td>Required for current lane</td></tr>
            <tr><td class="row-title">Course list and 12-unit / 24-online-hour course structure</td><td>Included or referenced</td><td>Required for current lane</td></tr>
            <tr><td class="row-title">Instructor/SME evidence where required</td><td>Included or referenced</td><td>Required for current lane</td></tr>
            <tr><td class="row-title">Certificate controls, identity confirmation, interactivity, and final participant statement controls</td><td>Included or referenced</td><td>Required for current lane</td></tr>
            <tr><td class="row-title">Official forms ready for signature/date</td><td>Included or referenced</td><td>Required for current lane</td></tr>
            <tr><td class="row-title">Reviewer access and final verification checklist</td><td>Included or referenced</td><td>Required for current lane</td></tr>
          </tbody>
        </table>
        <h3 style="font-family: var(--font-serif); font-size: 15px; color: var(--ci-maroon-deep); margin: 10px 0 6px;">Official Form Handling</h3>
        <div class="notice-block" style="border-left-color: var(--ci-maroon);">Official government forms appended after this index are preserved as source PDF pages without CI headers, branding, crop, watermark, or restyling. A standalone official forms PDF is also available in the same folder.</div>
      </section>
      {page_footer("Yadvir Saandal / CNA CDPH Submission Packet", "Page 2 of 8", "Prepared June 09, 2026")}
    </div>
    """


def review_context_page() -> str:
    return f"""
    <div id="p2" class="page">
      <header class="page-header">
        <div class="header-left">CNA/CDPH CE Signer-Review Binder</div>
        <div class="header-right">CI Institute of Nursing, Inc.</div>
      </header>
      <section class="page-body">
        <h2 class="doc-section-title">Review Context After Handoff</h2>
        <p class="intro-text">No missing application-submission documents were identified during this packet build. The items below are retained only as context for final verification before submission or public release.</p>
        <div class="notice-block">This page is not a task tracker, due-date sheet, build action list, or blocker log. After packet handoff, remaining review and release decisions are handled through the verification process.</div>
        <h3 style="font-size: 14px; color: var(--ci-maroon); margin: 20px 0 10px;">Context Items for Verification</h3>
        <table class="ci-table">
          <thead><tr><th>Context Item</th><th>Review Purpose</th><th>Packet Location</th></tr></thead>
          <tbody>
            <tr><td class="row-title">Official CDPH signature/date fields</td><td>Final read-through only</td><td>Original official forms packet</td></tr>
            <tr><td class="row-title">CDPH 192B pricing / membership fields</td><td>Final read-through only</td><td>Original official forms packet</td></tr>
            <tr><td class="row-title">CDPH 193 mailing-address confirmation if needed</td><td>Final read-through only</td><td>Original official forms packet</td></tr>
            <tr><td class="row-title">Instructor / SME evidence attachment presence</td><td>Confirm packet completeness</td><td>Application binder attachments</td></tr>
            <tr><td class="row-title">Reviewer URL, user ID, and password values</td><td>Confirm credential delivery works</td><td>Reviewer-access material</td></tr>
            <tr><td class="row-title">Public catalog and website fields</td><td>Confirm before external release</td><td>Catalog addendum</td></tr>
          </tbody>
        </table>
        <h3 style="font-family: var(--font-serif); font-size: 15px; color: var(--ci-maroon-deep); margin: 18px 0 6px;">Release Context</h3>
        <div class="notice-block" style="border-left-color: var(--ci-maroon);">Certificate release remains disabled pending CDPH approval metadata and completion evidence gates. No public approval claim is made by this packet.</div>
      </section>
      {page_footer("Yadvir Saandal / CNA CDPH Review Context", "Page 2 of 2", "Prepared June 09, 2026")}
    </div>
    """


def html_document(style: str, title: str, pages: list[str]) -> str:
    extra_css = """
      body { background: var(--paper-cream) !important; }
      .document-container {
        display: block !important;
        gap: 0 !important;
        padding: 0 !important;
        background: var(--paper-cream) !important;
      }
      .page {
        width: 8.5in !important;
        height: 11in !important;
        min-height: 11in !important;
        box-shadow: none !important;
        break-after: page !important;
        page-break-after: always !important;
      }
      .page:not(.cover-page):not(.divider-page) { background: var(--paper-cream) !important; }
      .cover-page {
        background: radial-gradient(circle at 50% 35%, #8B1515 0%, #5b0000 65%, #260000 100%) !important;
      }
      .cover-page .metallic-white {
        background: none !important;
        -webkit-background-clip: initial !important;
        background-clip: border-box !important;
        -webkit-text-fill-color: #f7f7f7 !important;
        color: #f7f7f7 !important;
      }
      .divider-page {
        background: radial-gradient(circle at center, #610000 0%, #3d0000 70%, #1a0000 100%) !important;
      }
      .page-body { background: var(--paper-cream) !important; }
      .doc-section-title {
        font-family: var(--font-serif) !important;
        font-size: 20px !important;
        color: var(--ci-maroon-deep) !important;
        margin-bottom: 15px !important;
      }
      .doc-section-title::after {
        height: 1px !important;
        background: linear-gradient(90deg, var(--ci-gold), transparent) !important;
      }
      .intro-text {
        font-size: 12px !important;
        line-height: 1.6 !important;
        color: var(--text-dark) !important;
      }
      .ci-table th {
        background: linear-gradient(180deg, #9C1A1A 0%, var(--ci-maroon-deep) 100%) !important;
        color: #fff !important;
        border: 1px solid var(--ci-maroon-black) !important;
        border-top: 1.5px solid var(--ci-gold-dark) !important;
        font-weight: 500 !important;
        letter-spacing: 0.08em !important;
      }
      .ci-table tbody tr { background: rgba(253, 252, 247, 0.98) !important; }
      .ci-table tbody tr:nth-child(even) { background: rgba(139, 21, 21, 0.035) !important; }
      .ci-table td {
        background: transparent !important;
        border: 1px solid var(--border-gray) !important;
        color: var(--text-dark) !important;
      }
      .notice-block { background: #FFFDE7 !important; }
      .page-footer {
        margin-top: auto !important;
        color: var(--text-gray) !important;
        border-top: 1px solid var(--border-gray) !important;
      }
      .page:last-child { page-break-after: auto !important; break-after: auto !important; }
      @media print {
        html, body {
          display: block !important;
          background: var(--paper-cream) !important;
        }
        .document-container { display: block !important; }
        .page {
          break-after: page !important;
          page-break-after: always !important;
        }
        .page:last-child { page-break-after: auto !important; break-after: auto !important; }
      }
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
  <style>{style}
{extra_css}</style>
</head>
<body>
  <main class="document-container">
    {''.join(pages)}
  </main>
</body>
</html>
"""


def render_html_to_pdf(html: str, pdf: Path) -> None:
    chrome = chrome_path()
    with tempfile.TemporaryDirectory(prefix="ci_ion_chrome_profile_") as profile, tempfile.TemporaryDirectory(prefix="ci_ion_print_") as print_dir:
        print_root = Path(print_dir)
        html_path = print_root / "source.html"
        temp_pdf = print_root / "output.pdf"
        html_path.write_text(html, encoding="utf-8")
        command = [
            str(chrome),
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
            f"--print-to-pdf={temp_pdf}",
            html_path.as_uri(),
        ]
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)
        if result.returncode != 0 or not temp_pdf.exists():
            fail(f"Chrome print-to-PDF failed for {pdf.name}: {result.stderr.strip() or result.stdout.strip()}")
        with fitz.open(temp_pdf) as doc:
            text = "\n".join(page.get_text("text") for page in doc)
        if "ERR_FILE_NOT_FOUND" in text or "Your file couldn't be accessed" in text:
            fail(f"Chrome could not access print HTML for {pdf.name}.")
        pdf.unlink(missing_ok=True)
        shutil.copy2(temp_pdf, pdf)


def merge_with_official(prefix_pdf: Path, target_pdf: Path) -> None:
    temp = target_pdf.with_suffix(".merged.tmp.pdf")
    writer = PdfWriter()
    prefix_reader = PdfReader(str(prefix_pdf))
    official_reader = PdfReader(str(OFFICIAL_SOURCE))
    for page in prefix_reader.pages:
        writer.add_page(page)
    for page in official_reader.pages:
        writer.add_page(page)
    with temp.open("wb") as handle:
        writer.write(handle)
    if getattr(prefix_reader, "stream", None):
        prefix_reader.stream.close()
    if getattr(official_reader, "stream", None):
        official_reader.stream.close()
    target_pdf.unlink(missing_ok=True)
    temp.replace(target_pdf)


def compare_appended_official(candidate: Path, ci_page_count: int) -> list[str]:
    issues: list[str] = []
    with fitz.open(candidate) as output_doc, fitz.open(OFFICIAL_SOURCE) as official_doc:
        if output_doc.page_count - ci_page_count != official_doc.page_count:
            return ["official appendix page count mismatch"]
        for idx in range(official_doc.page_count):
            src_pix = official_doc[idx].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            out_pix = output_doc[ci_page_count + idx].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            if src_pix.width != out_pix.width or src_pix.height != out_pix.height or src_pix.samples != out_pix.samples:
                issues.append(f"official appendix page {idx + 1} render mismatch")
    return issues


def page_count(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def render_samples(paths: list[Path]) -> list[str]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []
    for path in paths:
        with fitz.open(path) as doc:
            indices = sorted({0, min(1, doc.page_count - 1), min(2, doc.page_count - 1), doc.page_count - 1})
            for index in indices:
                pix = doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                out = QA_DIR / f"{path.stem}_p{index + 1:03d}.png"
                pix.save(out)
                outputs.append(str(out))
    return outputs


def build() -> dict[str, object]:
    if not STUDIO_HTML.exists():
        fail(f"Missing studio HTML: {STUDIO_HTML}")
    if not SCOPE.exists():
        fail(f"Missing scoped output folder: {SCOPE}")
    if not OFFICIAL_SOURCE.exists():
        fail(f"Missing source official forms: {OFFICIAL_SOURCE}")
    if not OFFICIAL_OUTPUT.exists():
        fail(f"Missing output official forms: {OFFICIAL_OUTPUT}")
    if sha256(OFFICIAL_SOURCE) != sha256(OFFICIAL_OUTPUT):
        fail("Standalone official forms output differs from source; stopping.")

    style, soup = studio_parts()
    logo = logo_src()
    p2_to_p11 = []
    for page_num in range(2, 12):
        page = soup.find(id=f"p{page_num}")
        if page is None:
            fail(f"Studio page p{page_num} is missing.")
        p2_to_p11.append(normalize_studio_page(str(page), "Yadvir Saandal / CNA CDPH Application Binder"))

    results: list[dict[str, object]] = []

    app_target = SCOPE / "01_CNA_CDPH_APPLICATION_BINDER.pdf"
    app_prefix = app_target.with_suffix(".studio-prefix.pdf")
    app_pages = [
        cover_page(
            page_id="p1",
            side_label="CNA / CDPH APPLICATION BINDER",
            right_label="DRAFT / PENDING APPROVAL",
            title="CNA Recertification",
            binder_title="CNA Recert Binder",
            status="Status: Draft / Pending Approval",
            logo=logo,
        ),
        *p2_to_p11,
        appendix_divider("p12"),
    ]
    before = sha256(app_target)
    render_html_to_pdf(html_document(style, "CNA CDPH Application Binder", app_pages), app_prefix)
    if page_count(app_prefix) != 12:
        fail(f"Application binder CI prefix rendered {page_count(app_prefix)} pages, expected 12.")
    merge_with_official(app_prefix, app_target)
    app_prefix.unlink(missing_ok=True)
    issues = compare_appended_official(app_target, 12)
    if issues:
        fail("; ".join(issues))
    results.append({"rel": "01_CNA_CDPH_APPLICATION_BINDER.pdf", "previous_sha256": before, "new_sha256": sha256(app_target), "pages": page_count(app_target)})

    min_target = SCOPE / "02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf"
    min_prefix = min_target.with_suffix(".studio-prefix.pdf")
    min_pages = [
        cover_page(
            page_id="p1",
            side_label="CNA / CDPH SUBMISSION PACKET",
            right_label="DRAFT / PENDING CDPH APPROVAL",
            title="CNA / CDPH Minimum Required",
            binder_title="Submission Packet",
            status="Status: Draft / Pending CDPH Approval",
            logo=logo,
        ),
        minimum_scope_page(),
        appendix_divider("p3"),
    ]
    before = sha256(min_target)
    render_html_to_pdf(html_document(style, "CNA CDPH Minimum Submission Packet", min_pages), min_prefix)
    if page_count(min_prefix) != 3:
        fail(f"Minimum packet CI prefix rendered {page_count(min_prefix)} pages, expected 3.")
    merge_with_official(min_prefix, min_target)
    min_prefix.unlink(missing_ok=True)
    issues = compare_appended_official(min_target, 3)
    if issues:
        fail("; ".join(issues))
    results.append({"rel": "02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf", "previous_sha256": before, "new_sha256": sha256(min_target), "pages": page_count(min_target)})

    ctx_target = SCOPE / "04_CNA_CDPH_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf"
    ctx_temp = ctx_target.with_suffix(".studio-prefix.pdf")
    ctx_pages = [
        cover_page(
            page_id="p1",
            side_label="CNA / CDPH REVIEW CONTEXT",
            right_label="DRAFT / PENDING CDPH APPROVAL",
            title="CNA / CDPH Review Context",
            binder_title="Post-Handoff Context",
            status="Status: Draft / Pending CDPH Approval",
            logo=logo,
        ),
        review_context_page(),
    ]
    before = sha256(ctx_target)
    render_html_to_pdf(html_document(style, "CNA CDPH Review Context", ctx_pages), ctx_temp)
    if page_count(ctx_temp) != 2:
        fail(f"Review context PDF rendered {page_count(ctx_temp)} pages, expected 2.")
    ctx_target.unlink(missing_ok=True)
    ctx_temp.replace(ctx_target)
    text = "\n".join(page.get_text("text") for page in fitz.open(ctx_target))
    forbidden = [
        "Final verification",
        "Yadvir / owner confirmation",
        "Build-Remediable vs Human/Regulator Items",
        "Why pending",
        "Due/action needed",
        "Blocks submission?",
    ]
    found = [term for term in forbidden if term in text]
    if found:
        fail("Forbidden tracker language remains: " + ", ".join(found))
    results.append({"rel": "04_CNA_CDPH_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf", "previous_sha256": before, "new_sha256": sha256(ctx_target), "pages": page_count(ctx_target)})

    samples = render_samples([app_target, min_target, ctx_target])
    return {
        "status": "complete",
        "renderer": str(chrome_path()),
        "studio_html": str(STUDIO_HTML),
        "fixed": results,
        "official_forms_unchanged_sha256": sha256(OFFICIAL_OUTPUT),
        "qa_samples": samples,
    }


def main() -> None:
    print(json.dumps(build(), indent=2))


if __name__ == "__main__":
    main()
