from __future__ import annotations

import json
import math
import re
from html import escape
from pathlib import Path

import fitz
from pypdf import PdfReader, PdfWriter

from rebuild_rcfe_application_binder_studio_html import (
    OUTPUT_ROOT,
    QA_DIR,
    ROOT,
    SOURCE_ROOT,
    footer,
    page_count,
    render_html_to_pdf,
    sha256,
    studio_css,
    table,
)


RCFE_ROOT = OUTPUT_ROOT / "02_RCFE_CDSS_CETP_APPLICATION"
SOURCE_OFFICIAL = SOURCE_ROOT / "02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/03_RCFE_CDSS_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"
RAW_ROOT = ROOT / "MOODLE_COURSE_CONTENT_READY_FOR_BUILD" / "02_RCFE_COURSE_CONTENT"


def html_document(title: str, pages: list[str]) -> str:
    extra_css = """
      body { background: var(--paper-cream) !important; }
      .document-container { gap: 0 !important; }
      .page { background: var(--paper-cream) !important; box-shadow: none !important; }
      .page-body { background: var(--paper-cream) !important; }
      .doc-section-title { font-size: 20px !important; color: var(--ci-maroon-deep) !important; margin-bottom: 16px !important; }
      .doc-section-title::after { flex: 0 0 1.55in !important; max-width: 1.55in !important; height: 1px !important; background: linear-gradient(90deg, var(--ci-gold) 0%, rgba(255,193,7,.72) 55%, transparent 100%) !important; }
      .studio-subhead { font-family: var(--font-serif); font-size: 15px; color: var(--ci-maroon-deep); margin: 14px 0 8px; }
      .studio-subhead-small { font-size: 12px; color: var(--ci-maroon); text-transform: uppercase; letter-spacing: .04em; margin: 12px 0 6px; }
      .intro-text, .md-p, .md-li { font-size: 10.8px !important; line-height: 1.5 !important; color: var(--text-dark) !important; }
      .md-p { margin: 0 0 7px; }
      .md-ul, .md-ol { margin: 6px 0 10px 18px; padding: 0; }
      .md-li { margin-bottom: 4px; }
      .ci-table { font-size: 8.7px !important; margin-top: 8px !important; margin-bottom: 12px !important; }
      .ci-table thead tr,
      .ci-table th {
        background: linear-gradient(180deg, #9C1A1A 0%, var(--ci-maroon-deep) 100%) !important;
        background-color: var(--ci-maroon-deep) !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
        color: #fff !important;
        border: 1px solid var(--ci-maroon-black) !important;
        border-top: 1.5px solid var(--ci-gold-dark) !important;
        font-weight: 500 !important;
        letter-spacing: 0.08em !important;
        padding: 6px 8px !important;
      }
      .ci-table tbody tr { background: rgba(253, 252, 247, 0.98) !important; }
      .ci-table tbody tr:nth-child(even) { background: rgba(139, 21, 21, 0.035) !important; }
      .ci-table td { background: transparent !important; border: 1px solid var(--border-gray) !important; color: var(--text-dark) !important; padding: 6px 8px !important; }
      .ci-table .row-title { color: var(--ci-maroon) !important; font-weight: 700 !important; }
      .notice-block { background: #FFFDE7 !important; border-left: 4px solid var(--ci-gold) !important; }
      .page-footer { margin-top: auto !important; font-size: 8px !important; letter-spacing: 0.1em !important; }
      .footer-left { font-weight: 400 !important; }
      .footer-center { font-weight: 300 !important; }
      .footer-right { font-weight: 700 !important; }
      .page:last-child { page-break-after: auto !important; break-after: auto !important; }
      @media print {
        html, body { background: var(--paper-cream) !important; }
        .page:last-child { page-break-after: auto !important; break-after: auto !important; }
      }
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>{escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
  <style>{studio_css()}
{extra_css}</style>
</head>
<body>
  <main class="document-container">
    {''.join(pages)}
  </main>
</body>
</html>
"""


def content_page(page_number: int, total_pages: int, header: str, title: str, body: str) -> str:
    return f"""
    <div id="p{page_number}" class="page">
      <header class="page-header">
        <div class="header-left">{escape(header)}</div>
        <div class="header-right">CI Institute of Nursing, Inc.</div>
      </header>
      <section class="page-body">
        <h2 class="doc-section-title">{escape(title)}</h2>
        {body}
      </section>
      {footer(page_number, total_pages, left=f"TJ Padilla / {header}")}
    </div>
    """


def append_pages(writer: PdfWriter, reader: PdfReader, start: int, end: int) -> None:
    for index in range(start, end):
        writer.add_page(reader.pages[index])


def replace_with_cover_and_pages(target: Path, pages: list[str], total_pages: int, title: str) -> dict[str, object]:
    before = sha256(target)
    generated = target.with_suffix(".studio-body.pdf")
    render_html_to_pdf(html_document(title, pages), generated)
    temp = target.with_suffix(".studio-html.tmp.pdf")
    writer = PdfWriter()
    current = PdfReader(str(target))
    body = PdfReader(str(generated))
    append_pages(writer, current, 0, 1)
    append_pages(writer, body, 0, len(body.pages))
    with temp.open("wb") as handle:
        writer.write(handle)
    generated.unlink(missing_ok=True)
    temp.replace(target)
    return {"rel": str(target.relative_to(OUTPUT_ROOT)), "before_sha256": before, "after_sha256": sha256(target), "pages": page_count(target), "expected_total": total_pages}


def replace_mixed_minimum(target: Path, body_page: str) -> dict[str, object]:
    before = sha256(target)
    generated = target.with_suffix(".studio-body.pdf")
    render_html_to_pdf(html_document("RCFE Minimum Submission Packet", [body_page]), generated)
    temp = target.with_suffix(".studio-html.tmp.pdf")
    writer = PdfWriter()
    current = PdfReader(str(target))
    body = PdfReader(str(generated))
    official = PdfReader(str(SOURCE_OFFICIAL))
    append_pages(writer, current, 0, 1)
    append_pages(writer, body, 0, len(body.pages))
    append_pages(writer, current, 2, 3)
    append_pages(writer, official, 0, len(official.pages))
    with temp.open("wb") as handle:
        writer.write(handle)
    generated.unlink(missing_ok=True)
    temp.replace(target)
    issues = compare_official(target, 3)
    if issues:
        raise RuntimeError("; ".join(issues))
    return {"rel": str(target.relative_to(OUTPUT_ROOT)), "before_sha256": before, "after_sha256": sha256(target), "pages": page_count(target), "official_verified": True}


def compare_official(candidate: Path, start_index: int) -> list[str]:
    issues: list[str] = []
    with fitz.open(candidate) as output_doc, fitz.open(SOURCE_OFFICIAL) as official_doc:
        if output_doc.page_count - start_index != official_doc.page_count:
            return ["official appendix page count mismatch"]
        for index in range(official_doc.page_count):
            src = official_doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            out = output_doc[start_index + index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
            if src.digest != out.digest:
                issues.append(f"official appendix page {index + 1} render mismatch")
    return issues


def minimum_page() -> str:
    body = f"""
      <p class="intro-text">This packet keeps the RCFE/CDSS-ACS submission set to the currently filed 9-course / 27-hour CETP application package.</p>
      <div class="notice-block">Official government forms after the appendix divider are preserved as original unbranded PDF pages. No CI styling is applied to those pages.</div>
      <h3 class="studio-subhead">Minimum Submission Contents</h3>
      {table(["Material", "Status", "Notes"], [
          ["LIC 9141 vendor application", "Included", "Official form appended after divider."],
          ["Nine LIC 9140 course approval requests", "Included", "Official forms appended after divider."],
          ["Vendor and course fee notices", "Included", "$140 + $270 = $410 total."],
          ["Course catalog and 27-hour matrix", "Included", "9 filed courses / 27 hours."],
          ["Instructor evidence reference", "Included", "Vanessa Valerio, RN License No. 788389."],
          ["Reviewer-access and payment checklist", "Included", "Final verification before submission."],
      ], [34, 18, 48])}
    """
    return content_page(2, 37, "RCFE/CDSS Minimum Required Submission Packet", "Minimum Submission Scope", body)


def context_page() -> str:
    body = f"""
      <p class="intro-text">This page records final review context only. It is not an assignment tracker, build task list, or approval claim.</p>
      <div class="notice-block">No CDSS/ACS vendor or course approval claim is made until issued approval metadata exists.</div>
      <h3 class="studio-subhead">Review Context</h3>
      {table(["Context Item", "Review Purpose", "Packet Location"], [
          ["Official signatures/dates", "Final execution review", "Official forms packet"],
          ["Payment/check number", "Confirm before mailing/submission", "Fee notices"],
          ["Instructor evidence attachment", "Confirm completeness", "Application binder attachments"],
          ["Reviewer access", "Confirm credential delivery works", "Reviewer-access material"],
          ["Public catalog language", "Confirm before external release", "Catalog addendum"],
      ], [34, 34, 32])}
    """
    return content_page(2, 2, "RCFE/CDSS Post-Handoff Context", "Review Context After Handoff", body)


def matrix_page() -> str:
    body = f"""
      <p class="intro-text">Current filed RCFE CDSS/ACS packet: 9 LIC 9140 courses totaling 27 hours.</p>
      <p class="intro-text">The future 40-hour / 12-module RCFE concept is excluded from current submission and is not included as current.</p>
      {table(["Item", "Description", "Hours/Status", "Notes"], [
          ["RCFE-CETP-001", "Laws, Regulations, Policies, and Standards", "4", "Laws/regulations block"],
          ["RCFE-CETP-002", "Alzheimer's Disease and Related Dementias Foundations", "4", "Dementia block"],
          ["RCFE-CETP-003", "Dementia Safety, Environment, and Documentation", "4", "Dementia block"],
          ["RCFE-CETP-004 to 009", "Rights, medication, admission/reappraisal, emergency, supervision, business operations", "15", "Filed 9-course packet total 27 hours"],
          ["Excluded future concept", "Future 40-hour / 12-module RCFE concept", "0", "Excluded from current submission and not included as current"],
      ], [18, 38, 16, 28])}
    """
    return content_page(2, 2, "RCFE Course Matrix and Dementia Block", "Map Summary", body)


def md_blocks(text: str) -> list[tuple[str, object]]:
    blocks: list[tuple[str, object]] = []
    lines = text.replace("\r\n", "\n").split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            blocks.append(("heading", (level, line.lstrip("#").strip())))
            i += 1
            continue
        if line.lstrip().startswith(("- ", "* ")):
            items = []
            while i < len(lines) and lines[i].lstrip().startswith(("- ", "* ")):
                items.append(lines[i].lstrip()[2:].strip())
                i += 1
            blocks.append(("list", items))
            continue
        if line.startswith("|") and "|" in line[1:]:
            table_lines = []
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i])
                i += 1
            rows = [[cell.strip() for cell in row.strip("|").split("|")] for row in table_lines]
            if len(rows) >= 2 and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in rows[1]):
                blocks.append(("table", (rows[0], rows[2:])))
            else:
                blocks.append(("table", (rows[0], rows[1:])))
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines):
            next_line = lines[i].rstrip()
            if not next_line.strip() or next_line.startswith("#") or next_line.startswith("|") or next_line.lstrip().startswith(("- ", "* ")):
                break
            para.append(next_line.strip())
            i += 1
        blocks.append(("paragraph", " ".join(para)))
    return blocks


def inline_md(value: str) -> str:
    value = escape(value)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    return value


def block_weight(block: tuple[str, object]) -> int:
    kind, data = block
    if kind == "heading":
        level, text = data
        return 6 if level <= 2 else 4
    if kind == "paragraph":
        return max(2, math.ceil(len(str(data)) / 96) * 2)
    if kind == "list":
        return 2 + sum(max(1, math.ceil(len(str(item)) / 90)) for item in data)
    if kind == "table":
        headers, rows = data
        return 4 + sum(max(2, math.ceil(sum(len(str(cell)) for cell in row) / 95) + 1) for row in rows)
    return 2


def block_html(block: tuple[str, object]) -> str:
    kind, data = block
    if kind == "heading":
        level, text = data
        cls = "studio-subhead" if level <= 2 else "studio-subhead-small"
        return f'<h3 class="{cls}">{inline_md(text)}</h3>'
    if kind == "paragraph":
        return f'<p class="md-p">{inline_md(str(data))}</p>'
    if kind == "list":
        return "<ul class=\"md-ul\">" + "".join(f'<li class="md-li">{inline_md(str(item))}</li>' for item in data) + "</ul>"
    if kind == "table":
        headers, rows = data
        return table([str(h) for h in headers], [[inline_md(str(cell)) for cell in row] for row in rows])
    return ""


def split_large_table(block: tuple[str, object], capacity: int = 46) -> list[tuple[str, object]]:
    kind, data = block
    if kind != "table" or block_weight(block) <= capacity:
        return [block]
    headers, rows = data
    chunks: list[tuple[str, object]] = []
    current: list[list[str]] = []
    current_weight = 4
    for row in rows:
        row_weight = max(2, math.ceil(sum(len(str(cell)) for cell in row) / 95) + 1)
        if current and current_weight + row_weight > capacity:
            chunks.append(("table", (headers, current)))
            current = []
            current_weight = 4
        current.append(row)
        current_weight += row_weight
    if current:
        chunks.append(("table", (headers, current)))
    return chunks


def markdown_pages(markdown_text: str, *, header: str, title: str, page_total: int | None = None) -> list[str]:
    raw_blocks: list[tuple[str, object]] = []
    for block in md_blocks(markdown_text):
        raw_blocks.extend(split_large_table(block))
    pages_blocks: list[list[tuple[str, object]]] = []
    current: list[tuple[str, object]] = []
    used = 0
    capacity = 52
    for block in raw_blocks:
        weight = block_weight(block)
        if current and used + weight > capacity:
            pages_blocks.append(current)
            current = []
            used = 0
        current.append(block)
        used += weight
    if current:
        pages_blocks.append(current)
    total = page_total or (1 + len(pages_blocks))
    rendered = []
    for index, blocks in enumerate(pages_blocks, start=2):
        page_title = title
        if blocks and blocks[0][0] == "heading":
            level, heading_text = blocks[0][1]
            if level <= 2:
                page_title = str(heading_text)
                blocks = blocks[1:]
        body = "".join(block_html(block) for block in blocks)
        rendered.append(content_page(index, total, header, page_title, body))
    return rendered


def build_course_material_pages() -> list[str]:
    parts = []
    for name in [
        "00_RCFE_COURSE_CONTENT_INDEX.md",
        "01_RCFE_ADMIN_9_COURSE_27HR_MOODLE_COURSE_CONTENT.md",
        "04_RCFE_COMPLETION_AND_CERTIFICATE_RULES.md",
        "05_RCFE_ACTIVITY_AND_PARTICIPATION_MAP.md",
        "06_RCFE_INSTRUCTOR_REVIEW_NOTES.md",
    ]:
        path = RAW_ROOT / name
        if path.exists():
            parts.append(path.read_text(encoding="utf-8", errors="replace"))
    return markdown_pages("\n\n".join(parts), header="RCFE Course Materials", title="RCFE Course Materials")


def build_lms_raw_pages() -> list[str]:
    path = RAW_ROOT / "01_RCFE_ADMIN_9_COURSE_27HR_MOODLE_COURSE_CONTENT.md"
    return markdown_pages(path.read_text(encoding="utf-8", errors="replace"), header="RCFE LMS Raw Course Content", title="RCFE LMS Raw Course Content")


def render_samples(paths: list[Path]) -> list[str]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []
    for path in paths:
        with fitz.open(path) as doc:
            indices = sorted({0, min(1, doc.page_count - 1), min(2, doc.page_count - 1), min(doc.page_count - 1, 4), doc.page_count - 1})
            for index in indices:
                out = QA_DIR / f"{path.stem}_p{index + 1:03d}.png"
                doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False).save(out)
                outputs.append(str(out))
    return outputs


def build() -> dict[str, object]:
    results: list[dict[str, object]] = []

    min_target = RCFE_ROOT / "01_APPLICATION_SUBMISSION" / "02_RCFE_CDSS_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf"
    ctx_target = RCFE_ROOT / "01_APPLICATION_SUBMISSION" / "04_RCFE_CDSS_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf"
    matrix_target = RCFE_ROOT / "02_COURSE_MATERIALS" / "02_RCFE_COURSE_MATRIX_AND_DEMENTIA_BLOCK.pdf"
    course_target = RCFE_ROOT / "02_COURSE_MATERIALS" / "01_RCFE_9_COURSE_27HR_COURSE_MATERIALS_COMPILED.pdf"
    raw_target = RCFE_ROOT / "02_COURSE_MATERIALS" / "03_RCFE_LMS_RAW_COURSE_CONTENT_FOR_POST_SME_BUILD.pdf"

    results.append(replace_mixed_minimum(min_target, minimum_page()))
    results.append(replace_with_cover_and_pages(ctx_target, [context_page()], 2, "RCFE Review Context"))
    results.append(replace_with_cover_and_pages(matrix_target, [matrix_page()], 2, "RCFE Course Matrix"))

    course_pages = build_course_material_pages()
    course_total = 1 + len(course_pages)
    course_pages = [content_page(i, course_total, "RCFE Course Materials", "RCFE Course Materials" if i == 2 else "RCFE Course Materials Continued", page_html.split('<section class="page-body">', 1)[1].split('</section>', 1)[0].split('</h2>', 1)[1]) for i, page_html in enumerate(course_pages, start=2)]
    results.append(replace_with_cover_and_pages(course_target, course_pages, course_total, "RCFE Course Materials"))

    skipped = [
        {
            "rel": str(raw_target.relative_to(OUTPUT_ROOT)),
            "reason": "Redundant with compiled RCFE course-materials packet; LMS raw course-content PDF intentionally not generated.",
        }
    ]

    samples = render_samples([min_target, ctx_target, matrix_target, course_target])
    report = {"updated": len(results), "results": results, "skipped": skipped, "qa_samples": samples}
    (OUTPUT_ROOT / "RCFE_REMAINING_STUDIO_HTML_REPORT.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


if __name__ == "__main__":
    result = build()
    print(json.dumps({"updated": result["updated"], "sample_count": len(result["qa_samples"])}, indent=2))
