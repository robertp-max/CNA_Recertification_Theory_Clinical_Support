from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import fitz
from bs4 import BeautifulSoup
from pypdf import PdfReader, PdfWriter


ROOT = Path(r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet")
OUTPUT_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED - Copy"
SOURCE_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN - Copy - Copy"
STUDIO_HTML = ROOT / "PDF_Design_Studio" / "pdf_design_studio.html"
TARGET = OUTPUT_ROOT / "01_CNA_CDPH_CE_APPLICATION" / "01_APPLICATION_SUBMISSION" / "02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf"
OFFICIAL_SOURCE = SOURCE_ROOT / "01_CNA_CDPH_CE_APPLICATION" / "01_APPLICATION_SUBMISSION" / "03_CNA_CDPH_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"
QA_DIR = Path(tempfile.gettempdir()) / "ci_ion_cna_minimum_content_typography_qa"

CHROME_CANDIDATES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]


def fail(message: str) -> None:
    raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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


def page_html() -> str:
    extra = """
      .minimum-content-page {
        padding: 0.72in 0.75in !important;
        display: block !important;
        justify-content: initial !important;
      }
      .minimum-content-page .page-header {
        margin-bottom: 22px !important;
      }
      .minimum-content-page .page-body {
        display: block !important;
        flex: none !important;
      }
      .minimum-content-page .doc-section-title {
        margin-bottom: 18px !important;
        gap: 10px !important;
        white-space: nowrap !important;
        align-items: center !important;
      }
      .minimum-content-page .doc-section-title::after {
        height: 1px !important;
        flex: 1 1 auto !important;
        min-width: 1.15in !important;
        margin-top: 1px !important;
        background: linear-gradient(90deg, var(--ci-gold) 0%, rgba(255, 193, 7, 0.55) 42%, rgba(255, 193, 7, 0.10) 82%, transparent 100%) !important;
      }
      .minimum-content-page .intro-text {
        font-size: 11px !important;
        line-height: 1.42 !important;
        margin: 0 0 13px !important;
        max-width: 6.85in;
      }
      .minimum-content-page .intro-strong {
        font-weight: 700;
        margin-bottom: 14px !important;
      }
      .minimum-content-page .notice-block {
        margin: 16px 0 17px !important;
        padding: 10px 12px !important;
        font-size: 10px !important;
        line-height: 1.35 !important;
        border-radius: 0 !important;
      }
      .minimum-content-page .section-label {
        color: var(--ci-maroon);
        font-size: 13px;
        font-weight: 700;
        margin: 0 0 9px;
      }
      .minimum-content-page .ci-table {
        table-layout: fixed !important;
        border-collapse: collapse !important;
        border-spacing: 0 !important;
        width: 100% !important;
        margin: 0 0 14px !important;
        font-size: 10px !important;
      }
      .minimum-content-page .ci-table th {
        padding: 6px 10px !important;
        border: 1px solid var(--ci-maroon-black) !important;
        border-top: 1.5px solid var(--ci-gold-dark) !important;
        background: linear-gradient(180deg, #9C1A1A 0%, var(--ci-maroon-deep) 100%) !important;
        vertical-align: middle !important;
        line-height: 1.1 !important;
      }
      .minimum-content-page .ci-table td {
        padding: 6px 10px !important;
        line-height: 1.22 !important;
        vertical-align: middle !important;
      }
      .minimum-content-page .row-title {
        font-weight: 700 !important;
      }
      .minimum-content-page .compact-note-title {
        font-family: var(--font-serif);
        font-size: 14px;
        color: var(--ci-maroon-deep);
        margin: 12px 0 6px;
      }
      .minimum-content-page .page-footer {
        position: absolute;
        left: 0.75in;
        right: 0.75in;
        bottom: 0.46in;
        margin-top: 0 !important;
      }
    """
    body = """
    <div id="p2" class="page minimum-content-page">
      <header class="page-header">
        <div class="header-left">CNA/CDPH CE Signer-Review Binder</div>
        <div class="header-right">CI Institute of Nursing, Inc.</div>
      </header>
      <section class="page-body">
        <h2 class="doc-section-title">Minimum Submission Scope</h2>
        <p class="intro-text">CNA 24-hour online CE course using CCCCO/NATP Modules 10&ndash;17 as the source backbone, delivered as 12 Moodle units.</p>
        <p class="intro-text intro-strong">This PDF includes the minimum application-submission index and exact official form pages where source PDFs were available. Optional LMS implementation materials, source folders, old module fragments, internal build notes, and raw source files are excluded.</p>
        <div class="notice-block">Approval-safe posture: Draft / Pending CDPH Approval. Certificate release remains disabled pending approval metadata and completion evidence gates. No public approval claim is made.</div>
        <h3 class="section-label">Project Submission Materials</h3>
        <table class="ci-table">
          <colgroup>
            <col style="width: 50%;">
            <col style="width: 24%;">
            <col style="width: 26%;">
          </colgroup>
          <thead>
            <tr>
              <th>Minimum Required Material</th>
              <th>Status</th>
              <th>Notes</th>
            </tr>
          </thead>
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
        <h3 class="compact-note-title">Official Form Handling</h3>
        <div class="notice-block" style="border-left-color: var(--ci-maroon); margin-top: 7px !important;">Official government forms appended after this index are preserved as source PDF pages without CI headers, branding, crop, watermark, or restyling. A standalone official forms PDF is also available in the same folder.</div>
        <h3 class="compact-note-title">Course Materials</h3>
        <p class="intro-text" style="font-size: 10px !important;">Course materials are provided in the lane's 02_COURSE_MATERIALS folder. Do not substitute old one-page module fragments or source folders for the compiled course-materials PDFs and workbooks.</p>
      </section>
      <footer class="page-footer">
        <div class="footer-left">Yadvir Saandal / CNA CDPH Submission Packet</div>
        <div class="footer-center">Prepared June 09, 2026</div>
        <div class="footer-right">Page 2 of 8</div>
      </footer>
    </div>
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
  <style>
{studio_css()}
{extra}
    .page:last-child {{ page-break-after: auto !important; break-after: auto !important; }}
    @media print {{ .page:last-child {{ page-break-after: auto !important; break-after: auto !important; }} }}
  </style>
</head>
<body>
  <main class="document-container">
    {body}
  </main>
</body>
</html>
"""


def render_content_page(pdf: Path) -> None:
    html_path = pdf.with_suffix(".html")
    html_path.write_text(page_html(), encoding="utf-8")
    pdf.unlink(missing_ok=True)
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
            html_path.as_uri(),
        ]
        result = subprocess.run(command, capture_output=True, text=True, timeout=90)
    html_path.unlink(missing_ok=True)
    if result.returncode != 0 or not pdf.exists():
        fail(f"Chrome print-to-PDF failed: {result.stderr.strip() or result.stdout.strip()}")
    if page_count(pdf) != 1:
        fail(f"Expected one rendered page, got {page_count(pdf)}.")


def replace_page_2(rendered_page: Path) -> tuple[str, str]:
    before = sha256(TARGET)
    target_reader = PdfReader(str(TARGET))
    page_reader = PdfReader(str(rendered_page))
    if len(target_reader.pages) != 8:
        fail(f"Unexpected target page count: {len(target_reader.pages)}")
    writer = PdfWriter()
    writer.add_page(target_reader.pages[0])
    writer.add_page(page_reader.pages[0])
    for index in range(2, len(target_reader.pages)):
        writer.add_page(target_reader.pages[index])
    tmp = TARGET.with_suffix(".page2-typography.tmp.pdf")
    with tmp.open("wb") as handle:
        writer.write(handle)
    if getattr(target_reader, "stream", None):
        target_reader.stream.close()
    if getattr(page_reader, "stream", None):
        page_reader.stream.close()
    verify_official_pages(tmp)
    tmp.replace(TARGET)
    return before, sha256(TARGET)


def verify_official_pages(candidate: Path) -> None:
    issues: list[str] = []
    with fitz.open(candidate) as output_doc, fitz.open(OFFICIAL_SOURCE) as official_doc:
        if output_doc.page_count != 3 + official_doc.page_count:
            issues.append("official page count mismatch")
        else:
            for idx in range(official_doc.page_count):
                src = official_doc[idx].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                out = output_doc[3 + idx].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                if src.width != out.width or src.height != out.height or src.samples != out.samples:
                    issues.append(f"official page {idx + 1} render mismatch")
    if issues:
        fail("; ".join(issues))


def render_qa() -> list[str]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []
    with fitz.open(TARGET) as doc:
        for index in [0, 1, 2, 7]:
            pix = doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            out = QA_DIR / f"02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET_p{index + 1:03d}.png"
            pix.save(out)
            outputs.append(str(out))
    return outputs


def main() -> None:
    if not TARGET.exists():
        fail(f"Missing target PDF: {TARGET}")
    if not STUDIO_HTML.exists():
        fail(f"Missing Studio HTML: {STUDIO_HTML}")
    if not OFFICIAL_SOURCE.exists():
        fail(f"Missing official form source PDF: {OFFICIAL_SOURCE}")

    rendered = Path(tempfile.gettempdir()) / "ci_ion_cna_minimum_page2_typography.pdf"
    render_content_page(rendered)
    before, after = replace_page_2(rendered)
    rendered.unlink(missing_ok=True)
    print(json.dumps({
        "status": "complete",
        "file": str(TARGET),
        "pages_replaced": [2],
        "locked_pages": [1, 3],
        "official_pages_verified": 5,
        "previous_sha256": before,
        "new_sha256": after,
        "qa_samples": render_qa(),
    }, indent=2))


if __name__ == "__main__":
    main()
