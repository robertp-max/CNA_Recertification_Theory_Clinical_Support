from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import tempfile
from html import escape
from pathlib import Path

import fitz
from bs4 import BeautifulSoup
from pypdf import PdfReader, PdfWriter


ROOT = Path(r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet")
OUTPUT_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED - Copy"
SOURCE_ROOT = ROOT / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN - Copy - Copy"
STUDIO_HTML = ROOT / "PDF_Design_Studio" / "pdf_design_studio.html"

TARGET_REL = Path("02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/01_RCFE_CDSS_APPLICATION_BINDER.pdf")
OFFICIAL_REL = Path("02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/03_RCFE_CDSS_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf")
TARGET = OUTPUT_ROOT / TARGET_REL
SOURCE_OFFICIAL = SOURCE_ROOT / OFFICIAL_REL
QA_DIR = Path(tempfile.gettempdir()) / "ci_ion_rcfe_app_studio_html_qa"

CHROME_CANDIDATES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]


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
    raise RuntimeError("Chrome or Edge was not found for HTML print-to-PDF rendering.")


def page_count(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def studio_css() -> str:
    soup = BeautifulSoup(STUDIO_HTML.read_text(encoding="utf-8"), "html.parser")
    style = soup.find("style")
    if style is None or style.string is None:
        raise RuntimeError("Could not locate CSS in PDF_Design_Studio\\pdf_design_studio.html.")
    return style.string


def render_html_to_pdf(html: str, pdf: Path) -> None:
    chrome = chrome_path()
    with tempfile.TemporaryDirectory(prefix="ci_ion_rcfe_print_") as print_dir, tempfile.TemporaryDirectory(prefix="ci_ion_chrome_profile_") as profile:
        html_path = Path(print_dir) / "rcfe_app_binder_print.html"
        temp_pdf = Path(print_dir) / "rendered.pdf"
        html_path.write_text(html, encoding="utf-8")
        pdf.unlink(missing_ok=True)
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
        result = subprocess.run(command, capture_output=True, text=True, timeout=90)
        html_path.unlink(missing_ok=True)
        if result.returncode != 0 or not temp_pdf.exists():
            raise RuntimeError(f"Chrome print-to-PDF failed: {result.stderr.strip() or result.stdout.strip()}")
        shutil.move(str(temp_pdf), str(pdf))


def footer(page_number: int, page_total: int = 46) -> str:
    return f"""
      <footer class="page-footer">
        <div class="footer-left">Yadvir Saandal / Implementation Requirement Binder</div>
        <div class="footer-center">Page {page_number} of {page_total}</div>
        <div class="footer-right">Prepared June 09, 2026</div>
      </footer>
    """


def table(headers: list[str], rows: list[list[str]], widths: list[int] | None = None) -> str:
    width_attrs = widths or []
    ths = []
    for index, header in enumerate(headers):
        style = f' style="width:{width_attrs[index]}%"' if index < len(width_attrs) else ""
        ths.append(f"<th{style}>{escape(header)}</th>")
    trs = []
    for row in rows:
        cells = []
        for index, value in enumerate(row):
            cls = ' class="row-title"' if index == 0 else ""
            cells.append(f"<td{cls}>{value}</td>")
        trs.append("<tr>" + "".join(cells) + "</tr>")
    return f"""
      <table class="ci-table">
        <thead><tr>{''.join(ths)}</tr></thead>
        <tbody>{''.join(trs)}</tbody>
      </table>
    """


def badge(text: str) -> str:
    lookup = {
        "ALIGNED": "badge-aligned",
        "FILLED": "badge-complete",
        "MAPPED": "badge-complete",
        "VERIFIED": "badge-aligned",
        "PREPARED": "badge-complete",
        "ATTACH": "badge-verify",
        "VERIFY": "badge-verify",
        "PENDING": "badge-pending",
    }
    cls = lookup.get(text.upper(), "badge-complete")
    return f'<span class="badge {cls}">{escape(text)}</span>'


def page(page_number: int, title: str, body: str, *, compact: bool = False) -> str:
    compact_class = " compact-page" if compact else ""
    return f"""
    <div id="p{page_number}" class="page{compact_class}">
      <header class="page-header">
        <div class="header-left">RCFE/CDSS CETP Signer-Review Binder</div>
        <div class="header-right">CI Institute of Nursing, Inc.</div>
      </header>
      <section class="page-body">
        <h2 class="doc-section-title">{escape(title)}</h2>
        {body}
      </section>
      {footer(page_number)}
    </div>
    """


def pages() -> list[str]:
    return [
        page(
            2,
            "Executive Summary",
            f"""
            <p class="intro-text">This binder consolidates the CI Institute of Nursing RCFE Continuing Education Training Program (CETP) submission for CDSS signer verification and submission review. It covers one LIC 9141 vendor application and nine LIC 9140 course approval requests totaling 27 continuing education hours.</p>
            <p class="intro-text"><strong>This binder reflects the current filed application packet: 9 LIC 9140 courses / 27 hours.</strong> A separate 40-hour / 12-module RCFE administrator-renewal LMS concept exists in the repository; it is classified as future LMS expansion and is intentionally excluded from this submission because no matching updated LIC 9140 forms exist.</p>
            <div class="notice-block">Pending CDSS/ACS approval. Do not advertise, issue certificates, or claim vendor/course approval until the applicable approval is issued.</div>
            <h3 class="studio-subhead">Project Charter Parameters</h3>
            {table(["Field", "Value"], [
                ["Institution / Vendor", "CI Institute of Nursing, Inc."],
                ["Program Track", "RCFE Administrator Continuing Education Training Program (CETP)"],
                ["Scope", "9 LIC 9140 courses / 27 CE hours + 1 LIC 9141 vendor application"],
                ["Delivery", "Live-stream / instructor-led with LMS post-test"],
                ["Authorized Signer", "Maria Divina Bustos, CEO / Authorized Representative"],
                ["Instructor of Record", "Vanessa Valerio, RN (License No. 788389)"],
                ["Filing Address", "419 E. Hamilton Ave., Campbell, CA 95008"],
                ["Fees", "Vendor (LIC 9141) $140 + course fees $270 = $410 total"],
            ], [30, 70])}
            """,
        ),
        page(
            3,
            "Readiness & Status Matrix",
            f"""
            <p class="intro-text">Review state of alignment and documentation integrity across all components of the RCFE submission package prior to final verification signatures.</p>
            {table(["Area", "Status", "Note"], [
                ["LIC 9141 vendor application", badge("FILLED"), "Native PDF fields filled; signature + representative legal attestations at signing."],
                ["Nine LIC 9140 course requests", badge("FILLED"), "All 9 filled with source-backed course + instructor data; instructor attestations at signing."],
                ["Vendor + course fee notices", badge("FILLED"), "$140 + $270 = $410 mapped; check/money-order number at payment."],
                ["Course set / hours", badge("ALIGNED"), "9 courses / 27 hours match the filed application packet."],
                ["Instructor of record", badge("MAPPED"), "Vanessa Valerio assigned across all nine LIC 9140 instructor fields."],
                ["Approval status", badge("PENDING"), "No CDSS vendor/course approval issued; remains pending until issued."],
            ], [32, 16, 52])}
            """,
        ),
        page(
            4,
            "Final Verification & Critical Path",
            f"""
            {table(["Workstream", "Final Verification Item", "Gate"], [
                ["Vendor form", "Sign LIC 9141; complete authorized-representative declarations.", "Gate 1"],
                ["Course forms", "Sign nine LIC 9140 forms; instructor completes Sections 7-10; attach course narratives.", "Gate 2"],
                ["Instructor", "Attach Vanessa Valerio resume + RN license verification.", "Gate 2"],
                ["Reviewer access", "Provide live-stream/LMS reviewer access for course inspection.", "Gate 3"],
                ["Payment", "Insert $410 check/money order and record the number.", "Gate 3"],
                ["Approval claim", "No approval/number claim until CDSS issues approval.", "Final"],
            ], [24, 58, 18])}
            <div class="notice-block">Operational rule: Course materials, the LMS shell, and reviewer access may proceed in parallel. The final gate blocks submission, signatures, payment claims, certificates, and use of any issued number until CDSS approval.</div>
            """,
        ),
        page(
            5,
            "Course Catalog - 9 Courses / 27 Hours",
            table(["Ref", "Course Title", "Hrs", "Core Subject Category", "Fee"], [
                ["001", "RCFE Laws, Regulations, Policies, and Procedural Standards", "4", "Laws, Regulations & Standards", "$40"],
                ["002", "Alzheimer's Disease & Related Dementias: Person-Centered Care", "4", "Managing Alzheimer's / Dementias", "$40"],
                ["003", "Alzheimer's Disease & Related Dementias: Safety, Environment & Documentation", "4", "Managing Alzheimer's / Dementias", "$40"],
                ["004", "Resident Rights, Dignity, Councils, & Abuse Prevention", "2", "Residents' Rights", "$20"],
                ["005", "Medication Management in RCFE Operations", "4", "Medication Management", "$40"],
                ["006", "Admission, Retention, Reappraisal, & Needs/Services Plans", "3", "Admission, Retention & Assessments", "$30"],
                ["007", "Emergency Procedures and Physical Environment Controls", "2", "Managing the Physical Environment", "$20"],
                ["008", "Staff Supervision, Training Records, & Administrator Accountability", "2", "Management / Supervision of Staff", "$20"],
                ["009", "RCFE Business Operations, Records, and Claim-Safe Communications", "2", "Business Operations", "$20"],
                ["Total", "9 courses", "27", "CDSS core categories", "$270"],
            ], [9, 43, 8, 28, 12]),
            compact=True,
        ),
        page(
            6,
            "Course Syllabus - Representative Modules",
            f"""
            <p class="intro-text">Each LIC 9140 course is documented with objectives, a timed content outline, and an 80%-pass post-test in the attached course narratives. Representative summaries:</p>
            {table(["Course", "Core", "Summary"], [
                ["RCFE-CETP-001 (4 hrs): RCFE Laws, Regulations, Policies, and Procedural Standards", "Laws, Regulations & Standards", "RCFE laws, regulations, Title 22 standards, procedural compliance, documentation, and audit readiness."],
                ["RCFE-CETP-002 (4 hrs): Alzheimer's Disease & Related Dementias: Person-Centered Care", "Managing Alzheimer's / Dementias", "Person-centered dementia care foundations: communication, behavior interpretation, individualized service planning, and staff direction."],
                ["RCFE-CETP-005 (4 hrs): Medication Management in RCFE Operations", "Medication Management", "Centrally stored medications, MAR documentation, error prevention, and the administrator's oversight role."],
                ["RCFE-CETP-006 (3 hrs): Admission, Retention, Reappraisal, & Needs/Services Plans", "Admission, Retention & Assessments", "Admission, retention, reappraisal, and NSP processes aligned to resident assessment requirements."],
            ], [38, 24, 38])}
            """,
        ),
        page(
            7,
            "Instructor / SME Evidence Checklist",
            f"""
            <p class="intro-text">Instructor of record for all nine LIC 9140 courses: <strong>Vanessa Valerio, RN (License No. 788389)</strong>, source-backed from the CDPH E279 instructor file.</p>
            {table(["Evidence Item", "Standard", "Status"], [
                ["Instructor assignment", "Mapped to all nine LIC 9140 instructor sections.", badge("MAPPED")],
                ["RN license", "Active CA RN license on file (No. 788389).", badge("VERIFIED")],
                ["Resume / CV", "Attach resume evidencing RCFE-relevant teaching/experience.", badge("ATTACH")],
                ["LIC 9140A instructor declarations", "Instructor completes Sections 7-10 and signs.", badge("PREPARED")],
            ], [32, 50, 18])}
            """,
        ),
        page(
            8,
            "Reviewer-Access & Payment Checklist",
            table(["Item", "Detail", "Status"], [
                ["Reviewer access (live-stream/LMS)", "Provide reviewer URL/credentials for course inspection.", badge("VERIFY")],
                ["Vendor fee (LIC 9141)", "$140 vendor application fee.", badge("MAPPED")],
                ["Course fees", "$270 across the nine courses; per-line itemization at payment.", badge("MAPPED")],
                ["Total payment", "$410 check/money order; record number at insertion.", badge("VERIFY")],
            ], [36, 46, 18]),
        ),
        page(
            9,
            "Recordkeeping & Proof-of-Completion",
            """
            <ul class="studio-list">
              <li>Approved course files, instructor dossiers, course roster/completion files, and evaluation logs retained for the required minimum.</li>
              <li>Completion records with verified time stamps retained per CDSS requirements.</li>
              <li>No certificate or approval-number use until CDSS approval is issued.</li>
              <li>No PHI / no real resident data in any course material or record.</li>
            </ul>
            <div class="notice-block">Retention and proof-of-completion language is operational documentation only. It does not claim CDSS/ACS approval or authorize certificate release before approval metadata is issued.</div>
            """,
        ),
        page(
            10,
            "Source Index",
            table(["Reference Baseline", "Application / Intent Mapping"], [
                ["CDSS LIC 9141", "RCFE CETP vendor application core form; filled, unbranded, appended."],
                ["CDSS LIC 9140 (x9)", "Course approval request forms for the nine-course / 27-hour set; filled, unbranded, appended."],
                ["Vendor & Course Fee Notices", "Payment notices: $140 vendor + $270 course = $410; filled, appended."],
                ["RCFE master application packet", "Controlling source for course titles, hours, and vendor identity."],
                ["CDPH E279 - Vanessa Valerio", "Source evidence for the instructor of record (RN License No. 788389)."],
            ], [36, 64]),
        ),
        page(
            11,
            "Final Sign-Off Gate",
            f"""
            <p class="intro-text">This binder is documentation-complete and ready for verification, signature, and submission review. Sign-off authorizes submission once the final-gate items above are satisfied.</p>
            {table(["Authorization", "Detail"], [
                ["Applicant / Authorized Signer", "Maria Divina Bustos, Chief Executive Officer; signature and date at submission."],
                ["Instructor / SME of Record", "Vanessa Valerio, RN - License No. 788389; instructor attestation at submission."],
                ["Packet Coordination", "Yadvir Saandal; final packet routing, verification tracking, and submission coordination."],
            ], [34, 66])}
            <div class="notice-block">Signature posture: Wet/e-signatures, initials, and dates are applied by the authorized signer and instructor at submission.</div>
            """,
        ),
    ]


def html_document(style: str, body_pages: list[str]) -> str:
    # White is allowed only for text in the dark table headers/badges. Page,
    # table-cell, row, and notice backgrounds remain cream/warm-tinted.
    extra_css = """
      body { background: var(--paper-cream) !important; }
      .document-container { gap: 0 !important; }
      .page { background: var(--paper-cream) !important; box-shadow: none !important; }
      .page-body { background: var(--paper-cream) !important; }
      .doc-section-title { font-size: 20px !important; color: var(--ci-maroon-deep) !important; margin-bottom: 18px !important; }
      .doc-section-title::after { height: 1px !important; background: linear-gradient(90deg, var(--ci-gold), transparent) !important; }
      .studio-subhead { font-size: 14px; color: var(--ci-maroon); margin: 20px 0 10px; }
      .intro-text { font-size: 12px !important; line-height: 1.58 !important; color: var(--text-dark) !important; }
      .ci-table { font-size: 10.8px !important; margin-top: 14px !important; margin-bottom: 18px !important; }
      .compact-page .ci-table { font-size: 9.3px !important; }
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
      .ci-table td { background: transparent !important; border: 1px solid var(--border-gray) !important; color: var(--text-dark) !important; }
      .ci-table .row-title { color: var(--ci-maroon) !important; font-weight: 700 !important; }
      .notice-block { background: #FFFDE7 !important; border-left: 4px solid var(--ci-gold) !important; }
      .studio-list { margin: 12px 0 0 0; padding-left: 18px; font-size: 12px; line-height: 1.58; color: var(--text-dark); }
      .studio-list li { margin-bottom: 10px; }
      .page-footer {
        margin-top: auto !important;
        font-size: 8px !important;
        letter-spacing: 0.1em !important;
      }
      .footer-left { font-weight: 400 !important; }
      .footer-center { font-weight: 300 !important; }
      .footer-right { font-weight: 700 !important; }
      .page:last-child { page-break-after: auto !important; break-after: auto !important; }
      @media print { .page:last-child { page-break-after: auto !important; break-after: auto !important; } }
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>RCFE CDSS CETP Signer Review Binder - Studio Content Pages</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
  <style>{style}
{extra_css}</style>
</head>
<body>
  <main class="document-container">
    {''.join(body_pages)}
  </main>
</body>
</html>
"""


def append_pages(writer: PdfWriter, reader: PdfReader, start: int, end: int) -> None:
    for index in range(start, end):
        writer.add_page(reader.pages[index])


def build() -> dict[str, object]:
    if not TARGET.exists():
        raise RuntimeError(f"Missing target PDF: {TARGET}")
    if not SOURCE_OFFICIAL.exists():
        raise RuntimeError(f"Missing source official PDF: {SOURCE_OFFICIAL}")
    if not STUDIO_HTML.exists():
        raise RuntimeError(f"Missing Studio HTML: {STUDIO_HTML}")

    before = sha256(TARGET)
    prefix = TARGET.with_suffix(".studio-content-pages.pdf")
    render_html_to_pdf(html_document(studio_css(), pages()), prefix)
    if page_count(prefix) != 10:
        raise RuntimeError(f"Rendered RCFE content page count {page_count(prefix)}, expected 10.")

    temp = TARGET.with_suffix(".studio-html.tmp.pdf")
    writer = PdfWriter()
    current_reader = PdfReader(str(TARGET))
    content_reader = PdfReader(str(prefix))
    official_reader = PdfReader(str(SOURCE_OFFICIAL))

    append_pages(writer, current_reader, 0, 1)  # locked cover
    append_pages(writer, content_reader, 0, len(content_reader.pages))
    append_pages(writer, current_reader, 11, 12)  # existing appendix divider
    append_pages(writer, official_reader, 0, len(official_reader.pages))
    with temp.open("wb") as handle:
        writer.write(handle)

    prefix.unlink(missing_ok=True)
    temp.replace(TARGET)

    issues = compare_official_appendix(TARGET, 12)
    if issues:
        raise RuntimeError("; ".join(issues))

    samples = render_samples()
    report = {
        "target": str(TARGET),
        "before_sha256": before,
        "after_sha256": sha256(TARGET),
        "pages": page_count(TARGET),
        "official_appendix_verified": True,
        "qa_samples": samples,
    }
    report_path = OUTPUT_ROOT / "RCFE_APPLICATION_BINDER_STUDIO_HTML_REPORT.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def compare_official_appendix(candidate: Path, official_start_index: int) -> list[str]:
    issues: list[str] = []
    with fitz.open(candidate) as output_doc, fitz.open(SOURCE_OFFICIAL) as official_doc:
        if output_doc.page_count - official_start_index != official_doc.page_count:
            return ["official appendix page count mismatch"]
        for index in range(official_doc.page_count):
            src = official_doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            out = output_doc[official_start_index + index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            if src.digest != out.digest:
                issues.append(f"official appendix page {index + 1} render mismatch")
    return issues


def render_samples() -> list[str]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []
    with fitz.open(TARGET) as doc:
        for index in [1, 2, 6, 11, 12]:
            out = QA_DIR / f"{TARGET.stem}_p{index + 1:03d}.png"
            doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False).save(out)
            outputs.append(str(out))
    return outputs


if __name__ == "__main__":
    result = build()
    print(json.dumps({"pages": result["pages"], "official_appendix_verified": result["official_appendix_verified"]}, indent=2))
