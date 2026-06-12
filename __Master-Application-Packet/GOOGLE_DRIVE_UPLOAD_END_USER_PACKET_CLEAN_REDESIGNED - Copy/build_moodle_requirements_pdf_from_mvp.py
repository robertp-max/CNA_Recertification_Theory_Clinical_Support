from __future__ import annotations

import base64
import hashlib
import html
import json
import os
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
SOURCE_ROOT = ROOT / "MOODLE_SELF_HOST_IMPLEMENTATION_MVP - Copy"
OUTPUT_PDF = (
    ROOT
    / "GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN_REDESIGNED - Copy"
    / "04_MOODLE_IMPLEMENTATION_REQUIREMENTS"
    / "01_MOODLE_SELF_HOST_IMPLEMENTATION_REQUIREMENTS_ONLY.pdf"
)
STUDIO_HTML = ROOT / "PDF_Design_Studio" / "pdf_design_studio.html"
QA_DIR = Path(tempfile.gettempdir()) / "ci_ion_moodle_requirements_pdf_qa"

LOGO_URL = "https://ciinstituteofnursing.com/assets/logos/ci-ion-logomark-white.svg"
CHROME_CANDIDATES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]
PLAYWRIGHT_CWD = ROOT.parent / "standalone-course-mvp"


def fail(message: str) -> None:
    raise RuntimeError(message)


def chrome_path() -> Path:
    for candidate in CHROME_CANDIDATES:
        if candidate.exists():
            return candidate
    found = shutil.which("chrome") or shutil.which("chrome.exe") or shutil.which("msedge") or shutil.which("msedge.exe")
    if found:
        return Path(found)
    fail("Chrome or Edge was not found for PDF rendering.")


def playwright_cwd() -> Path:
    if (PLAYWRIGHT_CWD / "node_modules" / "playwright").exists():
        return PLAYWRIGHT_CWD
    fail(f"Playwright install was not found at {PLAYWRIGHT_CWD}.")


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


def markdown_files() -> tuple[list[Path], list[Path], list[Path]]:
    root_docs = sorted(SOURCE_ROOT.glob("*.md"))
    course_shells = sorted((SOURCE_ROOT / "course_shells").glob("*.md")) if (SOURCE_ROOT / "course_shells").exists() else []
    additional = (
        sorted((SOURCE_ROOT / "generated_missing_elements").glob("*.md"))
        if (SOURCE_ROOT / "generated_missing_elements").exists()
        else []
    )
    return root_docs, course_shells, additional


def display_title(path: Path, additional: bool = False) -> str:
    stem = path.stem
    if additional:
        stem = re.sub(r"^README_GENERATED_", "README_", stem)
        stem = re.sub(r"^GENERATED_", "", stem)
        stem = stem.replace("GENERATED", "")
    stem = stem.replace("MISSING_OR_HUMAN_VERIFICATION_ITEMS", "VERIFICATION_ITEMS")
    stem = stem.replace("MISSING_ELEMENTS", "ADDITIONAL_ELEMENTS")
    stem = stem.replace("MISSING", "ADDITIONAL")
    stem = re.sub(r"^\d+_", "", stem)
    stem = stem.replace("_", " ").strip()
    stem = stem.replace("Moodle Mvp", "Moodle MVP")
    stem = stem.replace("Phi", "PHI")
    stem = stem.replace("Brn", "BRN")
    stem = stem.replace("Cna", "CNA")
    stem = stem.replace("Rcfe", "RCFE")
    stem = stem.replace("Cdph", "CDPH")
    stem = stem.replace("Cdss", "CDSS")
    return stem.title().replace("Mvp", "MVP").replace("Phi", "PHI")


def humanize_artifact_token(token: str) -> str:
    cleaned = token.replace("\\", "/").strip("`.,;:()[]{}")
    lower = cleaned.lower()
    if "moodle_self_host_implementation_mvp" in lower:
        return "Moodle implementation package"
    if "course_shells/" in lower:
        return "course shell specification"
    if "additional_elements/" in lower or "generated_missing_elements/" in lower:
        return "additional implementation element"
    if "final_submission_review_package/" in lower:
        return "submission review package"
    stem = Path(cleaned).stem
    stem = re.sub(r"^\d+_", "", stem)
    stem = re.sub(r"(?i)generated_", "", stem)
    stem = re.sub(r"(?i)missing_or_human_verification_items", "verification items", stem)
    stem = re.sub(r"(?i)missing", "additional", stem)
    stem = stem.replace("_", " ").replace("-", " ")
    stem = re.sub(r"\s+", " ", stem).strip()
    if not stem:
        return "implementation artifact"
    replacements = {
        "cna": "CNA",
        "rcfe": "RCFE",
        "brn": "BRN",
        "cdph": "CDPH",
        "cdss": "CDSS",
        "acs": "ACS",
        "mvp": "MVP",
        "lms": "LMS",
        "sme": "SME",
        "qa": "QA",
        "phi": "PHI",
    }
    return " ".join(replacements.get(word.lower(), word.lower()) for word in stem.split())


def clean_presentation_text(text: str) -> str:
    replacements = [
        (r"(?i)\bgenerated_missing_elements\b", "additional implementation elements"),
        (r"(?i)\badditional_elements\b", "additional implementation elements"),
        (r"(?i)\bREADME_GENERATED_MISSING_ELEMENTS\.md\b", "additional elements overview"),
        (r"(?i)\b98_MISSING_OR_HUMAN_VERIFICATION_ITEMS\.md\b", "verification items"),
        (r"(?i)\bGenerated Moodle MVP implementation artifact\.?", "Moodle MVP implementation support artifact."),
        (r"(?i)\bgenerated missing elements\b", "additional implementation elements"),
        (r"(?i)\bMoodle Missing Elements Draft Assets\b", "Moodle Additional Implementation Assets"),
        (r"(?i)\bMissing or Human-Verification Items\b", "Verification Items"),
        (r"(?i)\bMissing or Human Verification Items\b", "Verification Items"),
        (r"(?i)\bGenerated replacement artifacts \(created because source artifact was missing/incomplete\)", "Additional implementation artifacts"),
        (r"(?i)\bTrue missing blockers\b", "Verification blockers"),
        (r"(?i)\bsource artifact was missing/incomplete\b", "source artifact required completion"),
        (r"(?i)\bwhere a required Moodle implementation artifact was missing\b", "where a required Moodle implementation artifact required completion"),
        (r"(?i)\bsurvey risk if missing\b", "survey risk if unresolved"),
        (r"(?i)\bgen/missing status\b", "status"),
        (r"(?i)\bMissing quiz mapping\b", "Quiz mapping coverage gap"),
        (r"(?i)\bMissing active-time/seat-time evidence\b", "Active-time/seat-time evidence gap"),
        (r"(?i)\bgenerated quiz items\b", "prepared quiz items"),
        (r"(?i)\bgenerated conservatively\b", "prepared conservatively"),
        (r"(?i)\bevidence generated\b", "evidence produced"),
        (r"(?i)\bno CE certificate is generated\b", "no CE certificate is issued"),
        (r"(?i)\ba test certificate may be generated\b", "a test certificate may be created"),
        (r"(?i)\bQuiz banks generated\b", "Quiz banks prepared"),
        (r"(?i)\bExact file list generated by this package\b", "Exact file list prepared for this package"),
        (r"(?i)\bReviewer workflow \(generated\)", "Reviewer workflow"),
        (r"(?i)\bgenerated artifact\b", "prepared artifact"),
        (r"(?i)\bwhy generated\b", "purpose"),
        (r"(?i)\bAll items required to BUILD the self-hosted MVP environment are present or generated\b", "All items required to build the self-hosted MVP environment are present or prepared"),
        (r"(?i)\bfinal human verification required\b", "final verification required"),
        (r"(?i)\bfinal human verification\b", "final verification"),
        (r"(?i)\bhuman-verification items\b", "verification items"),
        (r"(?i)\bhuman-verification\b", "verification"),
        (r"(?i)\bhuman verification items\b", "verification items"),
        (r"(?i)\bhuman verification\b", "verification"),
        (r"(?i)\bNamed human owner\b", "Named owner"),
        (r"(?i)\bhuman/AI review\b", "reviewer review"),
        (r"(?i)\bhuman-readable\b", "readable"),
        (r"(?i)\bDraft / Pending Agency Approval\b", "Implementation Requirement Binder"),
        (r"(?i)\bStatus: Draft / Pending Approval\b", "Status: Implementation Requirement Binder"),
        (r"(?i)\bStatus: Pending BRN CEP approval\b", "Status: Implementation Requirement Binder"),
        (r"(?i)\bDraft / Pending CDPH Approval\b", "Implementation Requirement Binder"),
        (r"(?i)\bDraft / Pending CDSS/ACS Approval\b", "Implementation Requirement Binder"),
        (r"(?i)\bDraft / Pending BRN CEP Approval\b", "Implementation Requirement Binder"),
        (r"(?i)\bapplicable agency approval metadata\b", "certificate-release authorization metadata"),
        (r"(?i)\bagency approval metadata\b", "certificate-release authorization metadata"),
        (r"(?i)\bagency approval\b", "certificate-release authorization"),
        (r"(?i)\bregulator approval\b", "certificate-release authorization"),
        (r"(?i)\bmust not start until Vanessa Valerio, RN or another approved SME has reviewed and approved the course materials\b", "may start after Vanessa Valerio, RN has reviewed and approved the course materials"),
        (r"(?i)\bInternal SME approval is required before Aldrin/Dagny begin Moodle course-shell build, content import, quiz import, learner-access configuration, certificate setup, or production implementation\b", "Vanessa course-material approval is required before Aldrin/Dagny begin Moodle course-shell build, content import, quiz import, learner-access configuration, certificate setup, or production implementation"),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)
    text = re.sub(
        r"\b(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+\.(?:md|csv|gift|zip)\b",
        lambda match: humanize_artifact_token(match.group(0)),
        text,
        flags=re.I,
    )
    text = re.sub(r"\bMOODLE_SELF_HOST_IMPLEMENTATION_MVP(?:\.zip)?\b", "Moodle implementation package", text, flags=re.I)
    text = re.sub(r"\bcourse_shells/", "course shell specifications", text, flags=re.I)
    text = re.sub(r"\bcourse_shells\b", "course shell specifications", text, flags=re.I)
    text = re.sub(r"\s*/\s*\.md\b", " Markdown", text, flags=re.I)
    text = re.sub(r"\.md\b", " Markdown", text, flags=re.I)
    text = re.sub(r"\bFINAL_SUBMISSION_REVIEW_PACKAGE/\b", "submission review package", text, flags=re.I)
    text = re.sub(r"(?i)\bpass/fail\s*\(placeholder\)", "pass/fail configuration value", text)
    text = re.sub(r"(?i)\bplaceholder\b", "to be configured", text)
    text = re.sub(r"\s*\(see\s+import_assets/[^)]*\)", "", text, flags=re.I)
    text = re.sub(r"`?import_assets/[^`\s),]+`?", "", text, flags=re.I)
    text = re.sub(r"(?i)\bimport_assets\b", "asset import package", text)
    text = re.sub(r"(?i)\basset import package/", "import package", text)
    text = re.sub(r"(?i)\bMarkdown\b", "narrative reference", text)
    text = re.sub(r"(?i)\bCSV/MD\b", "CSV/reference", text)
    text = re.sub(r"(?i)\bGIFT\s*\+\s*CSV\s*\+\s*MD\b", "GIFT, CSV, and reference", text)
    text = re.sub(r"(?i)\bcourse shell specifications specs\b", "course shell specifications", text)
    text = re.sub(r"\s*\([^)]*asset import package[^)]*\)", "", text, flags=re.I)
    text = re.sub(r"\s*\(see\s*\)", "", text, flags=re.I)
    text = re.sub(r"\s*\(\s*\)", "", text)
    text = re.sub(r"\bGENERATED_", "", text)
    text = re.sub(r"(?i)\bgenerated\s+", "", text)
    text = re.sub(r"(?i)\bgenerated\b", "prepared", text)
    text = re.sub(r"(?i)\bmissing-elements folder\b", "additional-elements source folder", text)
    text = re.sub(r"(?i)\bmissing elements\b", "additional implementation elements", text)
    text = re.sub(r"(?i)\bmissing\b", "pending", text)
    return text


def clean_additional_text(text: str) -> str:
    text = re.sub(r"(?im)^Generated Moodle MVP implementation artifact\.\s*", "", text)
    text = re.sub(r"(?im)^#\s*Generated\s+", "# ", text)
    text = re.sub(r"(?im)^##\s*Generated\s+", "## ", text)
    return clean_presentation_text(text).strip()


def inline_md(text: str) -> str:
    text = clean_presentation_text(text)
    text = text.replace("M##", "Module")
    text = text.replace("U##", "Unit")
    text = text.replace("Q##", "Question")
    text = text.replace("CNA/Unit", "CNA unit category")
    text = text.replace("BRN/Module", "BRN module category")
    text = re.sub(r"\s*\(import from\s*\)\.?", "", text, flags=re.I)
    text = re.sub(r"<LANE>-<CATEGORY>-Question number", "lane-category question number", text)
    text = re.sub(r"<LANE>", "lane", text)
    text = re.sub(r"<CATEGORY>", "category", text)
    text = re.sub(r"#{2,}\s*feedback", "feedback text", text, flags=re.I)
    text = re.sub(r"\s{2,}", " ", text).strip()
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    return escaped


def md_table(lines: list[str]) -> str | None:
    if len(lines) < 2:
        return None
    if "|" not in lines[0] or "|" not in lines[1]:
        return None
    if not re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[1]):
        return None
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append(cells)
    header = rows[0]
    body = rows[2:]
    thead = "<thead><tr>" + "".join(f"<th>{inline_md(cell)}</th>" for cell in header) + "</tr></thead>"
    tbody = "<tbody>" + "".join(
        "<tr>" + "".join(f"<td>{inline_md(cell)}</td>" for cell in row) + "</tr>" for row in body
    ) + "</tbody>"
    return f'<table class="ci-table compact-table">{thead}{tbody}</table>'


def markdown_has_table(text: str) -> bool:
    lines = text.splitlines()
    for index in range(len(lines) - 1):
        if "|" not in lines[index] or "|" not in lines[index + 1]:
            continue
        if re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[index + 1]):
            return True
    return False


def markdown_to_html(text: str, title_override: str | None = None, additional: bool = False) -> str:
    if additional:
        text = clean_additional_text(text)
    else:
        text = clean_presentation_text(text)
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    in_ul = False
    in_ol = False
    in_code = False
    code_lines: list[str] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    while i < len(lines):
        line = lines[i].rstrip()

        if line.strip().startswith("```"):
            if not in_code:
                close_lists()
                in_code = True
                code_lines = []
            else:
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                in_code = False
            i += 1
            continue
        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if not line.strip():
            close_lists()
            i += 1
            continue

        table_block: list[str] = []
        j = i
        while j < len(lines) and "|" in lines[j] and lines[j].strip():
            table_block.append(lines[j].rstrip())
            j += 1
        table_html = md_table(table_block)
        if table_html:
            close_lists()
            out.append(table_html)
            i = j
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            close_lists()
            level = len(heading.group(1))
            text_value = heading.group(2).strip()
            if additional:
                text_value = re.sub(r"(?i)^Generated\s+", "", text_value)
                text_value = re.sub(r"(?i)\bgenerated missing elements\b", "Additional Implementation Elements", text_value)
            text_value = clean_presentation_text(text_value)
            if level == 1 and title_override:
                text_value = title_override
            tag = "h2" if level <= 1 else "h3" if level == 2 else "h4"
            cls = "doc-section-title" if tag == "h2" else ""
            out.append(f'<{tag} class="{cls}">{inline_md(text_value)}</{tag}>')
            i += 1
            continue

        bullet = re.match(r"^\s*[-*]\s+(.+)$", line)
        if bullet:
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(bullet.group(1))}</li>")
            i += 1
            continue

        numbered = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if numbered:
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(numbered.group(1))}</li>")
            i += 1
            continue

        close_lists()
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,6})\s+|^\s*[-*]\s+|^\s*\d+\.\s+|^```", lines[i]):
            if "|" in lines[i] and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}:?", lines[i + 1]):
                break
            para.append(lines[i].rstrip())
            i += 1
        out.append(f'<p class="intro-text">{" ".join(inline_md(p.strip()) for p in para)}</p>')

    close_lists()
    if in_code:
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(out)


def cover_page(logo: str) -> str:
    return f"""
    <div class="page cover-page" role="document" aria-label="Moodle Requirements Cover">
      <div class="frame"></div>
      <div class="corner-block tl"></div>
      <div class="corner-block tr"></div>
      <div class="corner-block bl"></div>
      <div class="corner-block br"></div>
      <div class="side-label left">MOODLE IMPLEMENTATION REQUIREMENTS</div>
      <div class="side-label right">MVP / SURVEY-READY</div>
      <div class="cover-content">
        <div class="logo-aura"></div>
        <img class="logo" src="{logo}" alt="CI Institute of Nursing Logo" />
        <div class="title-stack">
          <h2 class="title-california metallic-white">California</h2>
          <h1 class="title-main metallic-white xlong-title">Moodle Requirements</h1>
          <div class="binder-title">Self-Hosted MVP / Survey-Ready</div>
          <div class="subtitle">Implementation Requirement Binder</div>
          <div class="facts-line" aria-label="Moodle facts">
            <span>CNA / CDPH</span><span class="pipe">|</span><span>RCFE / CDSS-ACS</span><span class="pipe">|</span><span>BRN CEP</span>
          </div>
          <span class="source-note">Includes additional implementation elements &middot; import assets excluded</span>
          <div class="rule"><span class="rule-mark"></span></div>
        </div>
        <div class="provider-stack">
          <p class="provider-name">CI Institute of Nursing, Inc.</p>
          <div class="prepared-line">Prepared by <strong>TJ Padilla</strong> &middot; June 9, 2026</div>
        </div>
        <div class="status-text" aria-label="Status">
          <div class="status-title">Implementation Requirement Binder</div>
          <div class="status-subtitle">Vanessa course-material approval required before implementation.</div>
        </div>
      </div>
      <div class="footer-note">
        Moodle implementation may begin after Vanessa approves the course materials. Certificate release remains separately gated.
      </div>
    </div>
    """


def section_page(title: str, body: str, subtitle: str | None = None, landscape: bool = False) -> str:
    sub = f'<p class="section-subtitle">{html.escape(subtitle)}</p>' if subtitle else ""
    class_name = "requirement-section landscape-section" if landscape else "requirement-section"
    return f"""
    <section class="{class_name}">
      <header class="page-header">
        <div class="header-left">Moodle Self-Host Implementation Requirements</div>
        <div class="header-right">CI Institute of Nursing, Inc.</div>
      </header>
      <h2 class="doc-section-title">{html.escape(title)}</h2>
      {sub}
      <div class="section-body">{body}</div>
    </section>
    """


def toc_section(root_docs: list[Path], course_shells: list[Path], additional: list[Path]) -> str:
    def list_items(files: list[Path], additional_flag: bool = False) -> str:
        return "".join(f"<li>{html.escape(display_title(path, additional_flag))}</li>" for path in files)

    body = f"""
    <div class="notice-block">This consolidated PDF is assembled from the Moodle MVP implementation copy. The asset import folder is excluded. Additional implementation elements are included with presentation labels cleaned for review.</div>
    <div class="inventory-grid">
      <div>
        <h3>Core Requirement Documents</h3>
        <ol>{list_items(root_docs)}</ol>
      </div>
      <div>
        <h3>Course Shell Specifications</h3>
        <ol>{list_items(course_shells)}</ol>
      </div>
      <div>
        <h3>Additional Implementation Elements</h3>
        <ol>{list_items(additional, True)}</ol>
      </div>
    </div>
    """
    return section_page("Document Inventory", body, "One consolidated requirement PDF for Moodle implementation review.")


def html_document(document_part: str = "full") -> str:
    if not SOURCE_ROOT.exists():
        fail(f"Missing source folder: {SOURCE_ROOT}")
    if not STUDIO_HTML.exists():
        fail(f"Missing Studio HTML: {STUDIO_HTML}")
    if document_part not in {"full", "cover", "content"}:
        fail(f"Unknown HTML document part: {document_part}")

    root_docs, course_shells, additional = markdown_files()
    if not root_docs:
        fail("No Moodle root markdown documents found.")

    cover = cover_page(logo_src())
    content_sections = [toc_section(root_docs, course_shells, additional)]
    for path in root_docs:
        text = path.read_text(encoding="utf-8", errors="replace")
        content_sections.append(
            section_page(
                display_title(path),
                markdown_to_html(text, display_title(path)),
                rel_label(path),
                markdown_has_table(clean_presentation_text(text)),
            )
        )
    if course_shells:
        content_sections.append(section_page("Course Shell Specifications", "<p class=\"intro-text\">The following specifications define build structure for each lane.</p>"))
        for path in course_shells:
            text = path.read_text(encoding="utf-8", errors="replace")
            content_sections.append(
                section_page(
                    display_title(path),
                    markdown_to_html(text, display_title(path)),
                    rel_label(path),
                    markdown_has_table(clean_presentation_text(text)),
                )
            )
    if additional:
        content_sections.append(
            section_page(
                "Additional Implementation Elements",
                '<div class="notice-block">These additional implementation elements are included for review. Presentation labels are cleaned; source files remain unchanged.</div>',
            )
        )
        for path in additional:
            text = path.read_text(encoding="utf-8", errors="replace")
            content_sections.append(
                section_page(
                    display_title(path, True),
                    markdown_to_html(text, display_title(path, True), True),
                    rel_label(path),
                    markdown_has_table(clean_additional_text(text)),
                )
            )
    if document_part == "cover":
        sections = [cover]
    elif document_part == "content":
        sections = content_sections
    else:
        sections = [cover] + content_sections

    css = studio_css()
    custom_css = """
    @media print {
      @page { size: letter; margin: 0; }
      @page portrait { size: 8.5in 11in; margin: 0; }
      @page landscape { size: 11in 8.5in; margin: 0; }
      html, body { width: auto !important; height: auto !important; }
    }
    body {
      display: block !important;
      padding-left: 0 !important;
      background: white !important;
      overflow-x: hidden !important;
    }
    .content-document {
      background: var(--paper-cream) !important;
      position: relative;
    }
    .content-document,
    .content-document .document-container {
      min-height: 100vh;
    }
    .content-document .document-container,
    .content-document .requirement-section {
      position: relative;
      z-index: 1;
    }
    .document-container {
      display: block !important;
      padding: 0 !important;
      gap: 0 !important;
    }
    .metallic-white {
      background: none !important;
      -webkit-background-clip: initial !important;
      background-clip: initial !important;
      -webkit-text-fill-color: #f7f7f7 !important;
      color: #f7f7f7 !important;
    }
    .title-main { white-space: nowrap !important; }
    .cover-page {
      page: portrait;
    }
    .title-main.xlong-title {
      font-size: 0.38in !important;
      letter-spacing: 0.04em !important;
    }
    .requirement-section {
      page: portrait;
      break-before: page;
      page-break-before: always;
      min-height: 11in;
      padding: 0.72in 0.75in 0.62in;
      background: var(--paper-cream);
      color: var(--text-dark);
      font-family: var(--font-main);
      overflow-x: hidden;
      -webkit-box-decoration-break: clone;
      box-decoration-break: clone;
    }
    .landscape-section {
      page: landscape;
      min-height: 8.5in;
      padding: 0.52in 0.58in 0.42in;
    }
    .requirement-section .page-header {
      margin-bottom: 24px;
    }
    .landscape-section .page-header {
      margin-bottom: 18px;
    }
    .requirement-section .doc-section-title {
      margin: 0 0 17px;
      gap: 10px;
      white-space: normal;
    }
    .requirement-section .doc-section-title::after {
      background: linear-gradient(90deg, var(--ci-gold) 0%, rgba(255,193,7,.55) 42%, rgba(255,193,7,.10) 82%, transparent 100%);
    }
    .section-subtitle {
      font-size: 10px;
      color: var(--text-gray);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin: -8px 0 18px;
    }
    .section-body h2,
    .section-body h3 {
      color: var(--ci-maroon);
      font-size: 14px;
      margin: 18px 0 8px;
    }
    .section-body h4 {
      color: var(--ci-maroon-deep);
      font-size: 12px;
      margin: 13px 0 6px;
    }
    .section-body .intro-text,
    .section-body li {
      font-size: 10.4px;
      line-height: 1.45;
      overflow-wrap: anywhere;
      word-break: break-word;
    }
    .section-body p {
      margin: 0 0 10px;
    }
    .section-body ul,
    .section-body ol {
      margin: 6px 0 12px 18px;
      padding: 0;
    }
    .section-body li {
      margin: 0 0 5px;
    }
    .section-body code {
      font-family: Consolas, monospace;
      font-size: .92em;
      color: var(--ci-maroon-deep);
      overflow-wrap: anywhere;
      word-break: break-word;
    }
    .section-body pre {
      white-space: pre-wrap;
      border-left: 4px solid var(--ci-gold);
      background: #FFFDE7;
      padding: 10px 12px;
      font-size: 9px;
      line-height: 1.35;
      overflow-wrap: anywhere;
      word-break: break-word;
      max-width: 100%;
    }
    .section-body pre code {
      white-space: pre-wrap;
    }
    .compact-table {
      table-layout: fixed;
      width: 100%;
      font-size: 9.4px;
      margin: 10px 0 14px;
      break-inside: avoid;
    }
    .compact-table th {
      padding: 6px 8px;
    }
    .compact-table td {
      padding: 6px 8px;
      vertical-align: top;
      overflow-wrap: anywhere;
      word-break: break-word;
    }
    .landscape-section .compact-table {
      font-size: 7.2px;
      line-height: 1.22;
      margin: 8px 0 12px;
      break-inside: auto;
      page-break-inside: auto;
    }
    .landscape-section .compact-table th,
    .landscape-section .compact-table td {
      padding: 4px 5px;
    }
    .compact-table thead {
      display: table-header-group;
    }
    .compact-table tr {
      break-inside: avoid;
      page-break-inside: avoid;
    }
    .landscape-section .section-body .intro-text,
    .landscape-section .section-body li {
      font-size: 9.2px;
      line-height: 1.34;
    }
    .landscape-section .section-body h2,
    .landscape-section .section-body h3 {
      font-size: 12px;
      margin: 12px 0 6px;
    }
    .notice-block {
      border-radius: 0 !important;
      margin: 12px 0 16px;
      font-size: 10px;
      overflow-wrap: anywhere;
      word-break: break-word;
    }
    .inventory-grid {
      display: grid;
      grid-template-columns: 1.45fr 0.9fr 1fr;
      gap: 20px;
      align-items: start;
    }
    .inventory-grid h3 {
      font-size: 11px;
      margin: 0 0 8px;
    }
    .inventory-grid ol {
      margin-left: 14px;
    }
    .inventory-grid li {
      font-size: 8.8px;
      line-height: 1.35;
      margin-bottom: 4px;
    }
    .print-fixed-header,
    .print-fixed-footer,
    .print-page-bg {
      display: none;
    }
    @media print {
      html,
      html body.content-document,
      body.content-document {
        background: var(--paper-cream) !important;
      }
      .content-document .print-page-bg {
        position: fixed;
        inset: 0;
        z-index: 0;
        display: block;
        background: var(--paper-cream);
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      .content-document .print-fixed-header {
        position: fixed;
        top: 0.72in;
        left: 0.75in;
        right: 0.75in;
        z-index: 50;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1.5px solid var(--ci-maroon);
        padding-bottom: 6px;
        font-family: var(--font-main);
        text-transform: uppercase;
      }
      .content-document .print-fixed-header .header-left {
        font-size: 10px;
        letter-spacing: 0.12em;
        font-weight: 500;
        color: var(--ci-maroon);
      }
      .content-document .print-fixed-header .header-right {
        font-size: 9px;
        letter-spacing: 0.08em;
        font-weight: 400;
        color: var(--text-gray);
      }
      .content-document .print-fixed-footer {
        position: fixed;
        bottom: 0.55in;
        left: 0.75in;
        right: 0.75in;
        z-index: 50;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-top: 1px solid var(--border-gray);
        padding-top: 6px;
        color: var(--text-gray);
        font-family: var(--font-main);
        font-size: 8px;
        letter-spacing: 0.1em;
        text-transform: uppercase;
      }
      .content-document .print-fixed-footer .footer-center {
        font-weight: 300;
        text-align: center;
      }
      .content-document .print-fixed-footer .footer-left,
      .content-document .print-fixed-footer .footer-right {
        font-weight: 400;
      }
      .content-document .requirement-section .page-header {
        display: none;
      }
      .content-document .requirement-section {
        padding-top: 1.32in;
        padding-bottom: 1.0in;
      }
      .content-document .landscape-section {
        padding-top: 1.04in;
        padding-bottom: 0.78in;
      }
      .single-section .requirement-section {
        break-before: auto;
        page-break-before: auto;
      }
      .landscape-document .print-fixed-header,
      .landscape-document .print-fixed-footer {
        left: 0.58in;
        right: 0.58in;
      }
      .landscape-document .print-fixed-footer {
        bottom: auto;
        top: 7.60in;
      }
    }
    """
    body_class = ' class="content-document"' if document_part == "content" else ""
    fixed_chrome = (
        """
  <div class="print-page-bg"></div>
  <div class="print-fixed-header">
    <span class="header-left">Moodle Self-Host Implementation Requirements</span>
    <span class="header-right">CI Institute of Nursing, Inc.</span>
  </div>
  <div class="print-fixed-footer">
    <span class="footer-left">TJ Padilla / Implementation Requirement Binder</span>
    <span class="footer-center">Prepared June 09, 2026</span>
    <span class="footer-right">&nbsp;</span>
  </div>
"""
        if document_part == "content"
        else ""
    )
    html_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Moodle Self-Host Implementation Requirements</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
  <style>
{css}
{custom_css}
  </style>
</head>
<body{body_class}>
{fixed_chrome}
  <main class="document-container">
    {''.join(sections)}
  </main>
</body>
</html>
"""
    html_out = re.sub(r"(?i)\bcourse shell specifications specs\b", "course shell specifications", html_out)
    html_out = re.sub(r"(?i)(course shell specifications</code>)\s+specs\b", r"\1", html_out)
    html_out = re.sub(r"(?i)\basset import package/", "import package", html_out)
    return html_out


def rel_label(path: Path) -> str:
    label = str(path.relative_to(SOURCE_ROOT)).replace("\\", "/")
    return humanize_artifact_token(label).title().replace("Cna", "CNA").replace("Rcfe", "RCFE").replace("Brn", "BRN").replace("Mvp", "MVP")


def render_with_playwright(html_path: Path, pdf_path: Path) -> None:
    script = """
const { chromium } = require('playwright');

const fileUrl = process.argv[2];
const outPath = process.argv[3];
const executablePath = process.argv[4];

(async () => {
  const browser = await chromium.launch({ executablePath, headless: true });
  const page = await browser.newPage({
    viewport: { width: 816, height: 1056 },
    deviceScaleFactor: 1,
  });
  await page.goto(fileUrl, { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.pdf({
    path: outPath,
    width: '8.5in',
    height: '11in',
    margin: { top: '0', right: '0', bottom: '0', left: '0' },
    printBackground: true,
    preferCSSPageSize: true,
    scale: 1,
  });
  await browser.close();
})().catch((error) => {
  console.error(error && error.stack ? error.stack : error);
  process.exit(1);
});
"""
    with tempfile.TemporaryDirectory(prefix="ci_ion_moodle_playwright_") as tmp_dir:
        script_path = Path(tmp_dir) / "render_pdf.cjs"
        script_path.write_text(script, encoding="utf-8")
        env = dict(os.environ)
        env["NODE_PATH"] = str(playwright_cwd() / "node_modules")
        result = subprocess.run(
            [
                "node",
                str(script_path),
                html_path.resolve().as_uri(),
                str(pdf_path),
                str(chrome_path()),
            ],
            cwd=playwright_cwd(),
            env=env,
            capture_output=True,
            text=True,
            timeout=180,
        )
    if result.returncode != 0 or not pdf_path.exists():
        fail(f"Playwright print-to-PDF failed: {result.stderr.strip() or result.stdout.strip()}")


def merge_pdf_parts(parts: list[Path], output: Path) -> None:
    writer = PdfWriter()
    for part in parts:
        reader = PdfReader(str(part))
        for page in reader.pages:
            writer.add_page(page)
    with output.open("wb") as handle:
        writer.write(handle)


def stamp_page_numbers(path: Path) -> None:
    numbered = path.with_suffix(".numbered.pdf")
    numbered.unlink(missing_ok=True)
    with fitz.open(path) as doc:
        total = doc.page_count
        for index, page in enumerate(doc, start=1):
            if index == 1:
                continue
            rect = page.rect
            landscape = rect.width > rect.height
            margin = 41.8 if landscape else 54.0
            baseline_y = rect.height - 52.0 if landscape else rect.height - 38.5
            text = f"PAGE {index} OF {total}"
            fontsize = 5.6
            text_width = fitz.get_text_length(text, fontname="helv", fontsize=fontsize)
            page.insert_text(
                fitz.Point(rect.width - margin - text_width, baseline_y),
                text,
                fontname="helv",
                fontsize=fontsize,
                color=(0.54, 0.54, 0.54),
            )
        doc.save(numbered, deflate=True)
    numbered.replace(path)


def content_section_documents(base_html: str) -> list[tuple[str, bool]]:
    base_soup = BeautifulSoup(base_html, "html.parser")
    main = base_soup.find("main", class_="document-container")
    if main is None:
        fail("Could not find content document container for section rendering.")
    sections = main.find_all("section", recursive=False)
    documents: list[tuple[str, bool]] = []
    for section in sections:
        classes = section.get("class") or []
        landscape = "landscape-section" in classes
        soup = BeautifulSoup(base_html, "html.parser")
        body = soup.body
        if body is None:
            fail("Could not find body for section rendering.")
        body["class"] = "content-document single-section landscape-document" if landscape else "content-document single-section portrait-document"
        section_main = soup.find("main", class_="document-container")
        if section_main is None:
            fail("Could not find content document container for section rendering.")
        section_main.clear()
        section_main.append(BeautifulSoup(str(section), "html.parser"))
        documents.append((str(soup), landscape))
    return documents


def render_pdf() -> dict[str, object]:
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    before_hash = sha_file(OUTPUT_PDF) if OUTPUT_PDF.exists() else None
    content_html = html_document("content")
    section_documents = content_section_documents(content_html)
    with tempfile.TemporaryDirectory(prefix="ci_ion_moodle_render_") as render_tmp:
        render_dir = Path(render_tmp)
        cover_html_path = render_dir / "cover.html"
        cover_pdf = render_dir / "cover.pdf"
        tmp_pdf = render_dir / "merged.pdf"
        section_pdfs: list[Path] = []
        cover_html_path.write_text(html_document("cover"), encoding="utf-8")
        render_with_playwright(cover_html_path, cover_pdf)
        for index, (section_html, _landscape) in enumerate(section_documents, start=1):
            section_html_path = render_dir / f"s{index:03d}.html"
            section_pdf = render_dir / f"s{index:03d}.pdf"
            section_html_path.write_text(section_html, encoding="utf-8")
            render_with_playwright(section_html_path, section_pdf)
            section_pdfs.append(section_pdf)
        merge_pdf_parts([cover_pdf] + section_pdfs, tmp_pdf)
        stamp_page_numbers(tmp_pdf)
        tmp_pdf.replace(OUTPUT_PDF)
    page_total = len(PdfReader(str(OUTPUT_PDF)).pages)
    samples = render_samples()
    return {
        "status": "complete",
        "output_pdf": str(OUTPUT_PDF),
        "previous_sha256": before_hash,
        "new_sha256": sha_file(OUTPUT_PDF),
        "page_count": page_total,
        "source_folder": str(SOURCE_ROOT),
        "excluded_folder": "import_assets",
        "additional_elements_folder": str(SOURCE_ROOT / "generated_missing_elements"),
        "qa_samples": samples,
    }


def sha_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def render_samples() -> list[str]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []
    with fitz.open(OUTPUT_PDF) as doc:
        indices = sorted({0, min(1, doc.page_count - 1), min(2, doc.page_count - 1), doc.page_count - 1})
        for index in indices:
            pix = doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            out = QA_DIR / f"moodle_requirements_p{index + 1:03d}.png"
            pix.save(out)
            outputs.append(str(out))
    return outputs


def main() -> None:
    print(json.dumps(render_pdf(), indent=2))


if __name__ == "__main__":
    main()
