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
SCOPE = OUTPUT_ROOT / "01_CNA_CDPH_CE_APPLICATION" / "01_APPLICATION_SUBMISSION"
STUDIO_HTML = ROOT / "PDF_Design_Studio" / "pdf_design_studio.html"
OFFICIAL_REL = Path("01_CNA_CDPH_CE_APPLICATION/01_APPLICATION_SUBMISSION/03_CNA_CDPH_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf")
OFFICIAL_SOURCE = SOURCE_ROOT / OFFICIAL_REL
OFFICIAL_OUTPUT = OUTPUT_ROOT / OFFICIAL_REL
QA_DIR = Path(tempfile.gettempdir()) / "ci_ion_cna_covers_only_studio_qa"

LOGO_URL = "https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg"
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


def logo_src() -> str:
    try:
        request = urllib.request.Request(LOGO_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()
        return "data:image/svg+xml;base64," + base64.b64encode(data).decode("ascii")
    except Exception:
        return LOGO_URL


def cover_page(
    side_label: str,
    right_label: str,
    title: str,
    binder_title: str,
    status: str,
    logo: str,
    title_class: str = "",
) -> str:
    return f"""
    <div id="p1" class="page cover-page" role="document" aria-label="Binder Cover Page">
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
          <h1 class="title-main metallic-white{title_class}">{title}</h1>
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


def html_document(body: str) -> str:
    # Use the studio CSS directly. The final override only prevents Chrome from
    # printing an extra blank page when a single replacement page is rendered.
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
  <style>
{studio_css()}
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
    .divider-page {{
      background: radial-gradient(circle at 50% 35%, #8B1515 0%, #5b0000 65%, #260000 100%) !important;
    }}
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


def render_html_to_pdf(body: str, pdf: Path) -> None:
    chrome = chrome_path()
    pdf.unlink(missing_ok=True)
    html_path = pdf.with_suffix(".html")
    html_path.write_text(html_document(body), encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix="ci_ion_chrome_profile_") as profile:
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
            f"--print-to-pdf={pdf}",
            html_path.as_uri(),
        ]
        result = subprocess.run(command, capture_output=True, text=True, timeout=90)
    html_path.unlink(missing_ok=True)
    if result.returncode != 0 or not pdf.exists():
        fail(f"Chrome print-to-PDF failed: {result.stderr.strip() or result.stdout.strip()}")
    if page_count(pdf) != 1:
        fail(f"Expected one rendered replacement page for {pdf.name}, got {page_count(pdf)}.")


def replace_pages(target: Path, replacements: dict[int, Path]) -> tuple[str, str]:
    before = sha256(target)
    temp = target.with_suffix(".covers-only.tmp.pdf")
    original = PdfReader(str(target))
    replacement_readers = {idx: PdfReader(str(path)) for idx, path in replacements.items()}
    writer = PdfWriter()
    for idx, page in enumerate(original.pages):
        if idx in replacement_readers:
            writer.add_page(replacement_readers[idx].pages[0])
        else:
            writer.add_page(page)
    with temp.open("wb") as handle:
        writer.write(handle)
    target.unlink()
    temp.replace(target)
    for reader in replacement_readers.values():
        if getattr(reader, "stream", None):
            reader.stream.close()
    if getattr(original, "stream", None):
        original.stream.close()
    return before, sha256(target)


def compare_appended_official(candidate: Path, official_start_index: int) -> list[str]:
    issues: list[str] = []
    with fitz.open(candidate) as output_doc, fitz.open(OFFICIAL_SOURCE) as official_doc:
        if output_doc.page_count - official_start_index != official_doc.page_count:
            return ["official appendix page count mismatch"]
        for idx in range(official_doc.page_count):
            src_pix = official_doc[idx].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            out_pix = output_doc[official_start_index + idx].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            if src_pix.width != out_pix.width or src_pix.height != out_pix.height or src_pix.samples != out_pix.samples:
                issues.append(f"official appendix page {idx + 1} render mismatch")
    return issues


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


def main() -> None:
    if not STUDIO_HTML.exists():
        fail(f"Missing studio HTML: {STUDIO_HTML}")
    if not SCOPE.exists():
        fail(f"Missing scope folder: {SCOPE}")
    if sha256(OFFICIAL_SOURCE) != sha256(OFFICIAL_OUTPUT):
        fail("Standalone official forms output differs from source; stopping.")

    logo = logo_src()
    work = Path(tempfile.gettempdir()) / "ci_ion_covers_only_studio_pages"
    work.mkdir(parents=True, exist_ok=True)

    app_cover = work / "app_cover.pdf"
    min_cover = work / "min_cover.pdf"
    ctx_cover = work / "ctx_cover.pdf"
    divider = work / "appendix_divider.pdf"

    render_html_to_pdf(
        cover_page("CNA / CDPH APPLICATION BINDER", "DRAFT / PENDING APPROVAL", "CNA Recertification", "CNA Recert Binder", "Status: Draft / Pending Approval", logo),
        app_cover,
    )
    render_html_to_pdf(
        cover_page("CNA / CDPH SUBMISSION PACKET", "DRAFT / PENDING CDPH APPROVAL", "CNA / CDPH Minimum Required", "Submission Packet", "Status: Draft / Pending CDPH Approval", logo, " long-title"),
        min_cover,
    )
    render_html_to_pdf(
        cover_page("CNA / CDPH REVIEW CONTEXT", "DRAFT / PENDING CDPH APPROVAL", "CNA / CDPH Review Context", "Post-Handoff Context", "Status: Draft / Pending CDPH Approval", logo, " long-title"),
        ctx_cover,
    )
    render_html_to_pdf(appendix_divider(), divider)

    results = []
    app = SCOPE / "01_CNA_CDPH_APPLICATION_BINDER.pdf"
    before, after = replace_pages(app, {0: app_cover, 11: divider})
    issues = compare_appended_official(app, 12)
    if issues:
        fail("; ".join(issues))
    results.append({"file": app.name, "pages_replaced": [1, 12], "previous_sha256": before, "new_sha256": after})

    minimum = SCOPE / "02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf"
    before, after = replace_pages(minimum, {0: min_cover, 2: divider})
    issues = compare_appended_official(minimum, 3)
    if issues:
        fail("; ".join(issues))
    results.append({"file": minimum.name, "pages_replaced": [1, 3], "previous_sha256": before, "new_sha256": after})

    context = SCOPE / "04_CNA_CDPH_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf"
    before, after = replace_pages(context, {0: ctx_cover})
    results.append({"file": context.name, "pages_replaced": [1], "previous_sha256": before, "new_sha256": after})

    samples = render_samples([app, minimum, context])
    print(json.dumps({
        "status": "complete",
        "operation": "covers_and_appendix_dividers_only",
        "studio_html": str(STUDIO_HTML),
        "official_forms_unchanged_sha256": sha256(OFFICIAL_OUTPUT),
        "fixed": results,
        "qa_samples": samples,
    }, indent=2))


if __name__ == "__main__":
    main()
