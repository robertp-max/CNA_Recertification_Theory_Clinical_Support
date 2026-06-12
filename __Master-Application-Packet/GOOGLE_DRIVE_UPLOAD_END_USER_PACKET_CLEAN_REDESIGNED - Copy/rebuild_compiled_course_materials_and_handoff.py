from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

import fitz
from pypdf import PdfReader, PdfWriter

from rebuild_cna_submission_from_studio_html import OUTPUT_ROOT, ROOT, render_html_to_pdf, sha256, studio_parts


RAW_ROOT = ROOT / "MOODLE_COURSE_CONTENT_READY_FOR_BUILD"
REPORT = OUTPUT_ROOT / "COMPILED_COURSE_MATERIALS_AND_HANDOFF_REPORT.json"
QA_DIR = Path(r"C:\Users\razer\AppData\Local\Temp\ci_ion_compiled_course_materials_qa")


COURSE_SPECS = [
    {
        "rel": "01_CNA_CDPH_CE_APPLICATION/02_COURSE_MATERIALS/01_CNA_24HR_12_UNIT_COURSE_MATERIALS_COMPILED.pdf",
        "source": RAW_ROOT / "01_CNA_COURSE_CONTENT/01_CNA_24HR_12_UNIT_MOODLE_COURSE_CONTENT.md",
        "label": "CNA Course Materials",
        "title": "CNA 24-Hour / 12-Unit Course Materials",
    },
    {
        "rel": "02_RCFE_CDSS_CETP_APPLICATION/02_COURSE_MATERIALS/01_RCFE_9_COURSE_27HR_COURSE_MATERIALS_COMPILED.pdf",
        "source": RAW_ROOT / "02_RCFE_COURSE_CONTENT/01_RCFE_ADMIN_9_COURSE_27HR_MOODLE_COURSE_CONTENT.md",
        "label": "RCFE Course Materials",
        "title": "RCFE 9-Course / 27-Hour Course Materials",
    },
    {
        "rel": "03_BRN_CARE_MANAGER_CEP_APPLICATION/02_COURSE_MATERIALS/01_BRN_30_CONTACT_HOUR_COURSE_MATERIALS_COMPILED.pdf",
        "source": RAW_ROOT / "03_BRN_COURSE_CONTENT/01_BRN_RN_CASE_MANAGEMENT_30_CONTACT_HOUR_MOODLE_COURSE_CONTENT.md",
        "label": "BRN Course Materials",
        "title": "BRN 30 Contact-Hour Course Materials",
    },
]

RAW_LMS_RELS = [
    "01_CNA_CDPH_CE_APPLICATION/02_COURSE_MATERIALS/03_CNA_LMS_RAW_COURSE_CONTENT_FOR_POST_SME_BUILD.pdf",
    "03_BRN_CARE_MANAGER_CEP_APPLICATION/02_COURSE_MATERIALS/03_BRN_LMS_RAW_COURSE_CONTENT_FOR_POST_SME_BUILD.pdf",
]


def clean_inline(text: str) -> str:
    text = text.replace("`", "")
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"__(.*?)__", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", text)
    text = re.sub(r"(?i)\bOf\s+cial\b", "Official", text)
    text = re.sub(r"(?i)\bO\s+cial\b", "Official", text)
    text = re.sub(r"(?i)\bof\s+icial\b", "official", text)
    text = re.sub(r"(?i)\bconf\s+identiality\b", "confidentiality", text)
    text = re.sub(r"\b03_(?:CNA|BRN)_[A-Z0-9_]+\.csv\b", "the Moodle question-bank import file", text)
    text = re.sub(r"(?i)\bInternal answer/rationale preview\b", "Answer/rationale reference", text)
    text = re.sub(r"\b([UM]\d{2})_Q(\d{2})_source\b", r"\1 question \2 mapping", text)
    text = re.sub(r"\b([UM]\d{2})_Q(\d{2})_([A-Z0-9_]+)\b", lambda m: f"{m.group(1)} question {m.group(2)} {m.group(3).replace('_', ' ').lower()}", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_separator(row: str) -> bool:
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells)


def parse_markdown(text: str) -> list[dict[str, object]]:
    blocks: list[dict[str, object]] = []
    paragraph: list[str] = []
    bullets: list[str] = []
    table_rows: list[list[str]] = []
    in_code = False

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append({"kind": "paragraph", "text": clean_inline(" ".join(paragraph))})
            paragraph = []

    def flush_bullets() -> None:
        nonlocal bullets
        if bullets:
            blocks.append({"kind": "bullets", "items": bullets})
            bullets = []

    def flush_table() -> None:
        nonlocal table_rows
        if table_rows:
            blocks.append({"kind": "table", "rows": table_rows})
            table_rows = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            flush_bullets()
            flush_table()
            in_code = not in_code
            continue
        if in_code:
            if stripped:
                blocks.append({"kind": "paragraph", "text": clean_inline(stripped)})
            continue
        if not stripped:
            flush_paragraph()
            flush_bullets()
            flush_table()
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph()
            flush_bullets()
            if is_separator(stripped):
                continue
            table_rows.append([clean_inline(cell) for cell in stripped.strip("|").split("|")])
            continue
        flush_table()
        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            flush_bullets()
            level = len(heading.group(1))
            blocks.append({"kind": "heading", "level": level, "text": clean_inline(heading.group(2))})
            continue
        bullet = re.match(r"^[-*]\s+(.+)$", stripped)
        numbered = re.match(r"^\d+\.\s+(.+)$", stripped)
        if bullet or numbered:
            flush_paragraph()
            bullets.append(clean_inline((bullet or numbered).group(1)))
            continue
        flush_bullets()
        paragraph.append(stripped)
    flush_paragraph()
    flush_bullets()
    flush_table()
    return [block for block in blocks if block.get("text") or block.get("rows") or block.get("items")]


def block_weight(block: dict[str, object]) -> int:
    kind = block["kind"]
    if kind == "heading":
        return 5 if int(block.get("level", 2)) <= 2 else 4
    if kind == "paragraph":
        return max(2, len(str(block["text"])) // 95 + 1)
    if kind == "bullets":
        return 2 + sum(max(1, len(str(item)) // 90 + 1) for item in block["items"])
    if kind == "table":
        rows = block["rows"]
        return 4 + sum(max(1, len(" ".join(row)) // 80 + 1) for row in rows)
    return 2


def split_large_tables(blocks: list[dict[str, object]], max_table_weight: int = 34) -> list[dict[str, object]]:
    split_blocks: list[dict[str, object]] = []
    for block in blocks:
        if block.get("kind") != "table" or block_weight(block) <= max_table_weight:
            split_blocks.append(block)
            continue
        rows = list(block["rows"])
        if len(rows) <= 2:
            split_blocks.append(block)
            continue
        header = rows[0]
        chunk = [header]
        used = 4
        for row in rows[1:]:
            row_weight = max(1, len(" ".join(row)) // 80 + 1)
            if len(chunk) > 1 and used + row_weight > max_table_weight:
                split_blocks.append({"kind": "table", "rows": chunk})
                chunk = [header]
                used = 4
            chunk.append(row)
            used += row_weight
        if len(chunk) > 1:
            split_blocks.append({"kind": "table", "rows": chunk})
    return split_blocks


def paginate(blocks: list[dict[str, object]], capacity: int = 58) -> list[list[dict[str, object]]]:
    pages: list[list[dict[str, object]]] = []
    current: list[dict[str, object]] = []
    used = 0
    for block in blocks:
        weight = block_weight(block)
        if current and used + weight > capacity:
            pages.append(current)
            current = []
            used = 0
        current.append(block)
        used += weight
    if current:
        pages.append(current)
    return pages


def table_html(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    head = "".join(f"<th>{escape(cell)}</th>" for cell in rows[0])
    body = "".join("<tr>" + "".join(f"<td>{escape(cell)}</td>" for cell in row) + "</tr>" for row in rows[1:])
    return f"<table class=\"ci-table\"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"


def blocks_html(blocks: list[dict[str, object]], first_title: str) -> tuple[str, str]:
    title = first_title
    parts: list[str] = []
    title_used = False
    for block in blocks:
        kind = block["kind"]
        if kind == "heading":
            text = str(block["text"])
            level = int(block.get("level", 2))
            if not title_used and level <= 2:
                title = text
                title_used = True
            else:
                parts.append(f"<h3 class=\"studio-subhead\">{escape(text)}</h3>")
        elif kind == "paragraph":
            parts.append(f"<p class=\"intro-text\">{escape(str(block['text']))}</p>")
        elif kind == "bullets":
            items = "".join(f"<li>{escape(str(item))}</li>" for item in block["items"])
            parts.append(f"<ul class=\"studio-list\">{items}</ul>")
        elif kind == "table":
            parts.append(table_html(block["rows"]))
    return title, "\n".join(parts)


def content_page(page_number: int, total_pages: int, label: str, title: str, html: str) -> str:
    return f"""
    <div class="page">
      <header class="page-header">
        <div class="header-left">{escape(label)}</div>
        <div class="header-right">CI Institute of Nursing, Inc.</div>
      </header>
      <section class="page-body">
        <h2 class="doc-section-title">{escape(title)}</h2>
        {html}
      </section>
      <footer class="page-footer">
        <div class="footer-left">TJ Padilla / {escape(label)}</div>
        <div class="footer-center">Page {page_number} of {total_pages}</div>
        <div class="footer-right">Prepared June 09, 2026</div>
      </footer>
    </div>
    """


def html_document(style: str, title: str, pages: list[str]) -> str:
    extra_css = """
      html, body { width: 8.5in; margin: 0; background: var(--paper-cream) !important; }
      body { display: block !important; padding: 0 !important; }
      .document-container { display: block !important; padding: 0 !important; gap: 0 !important; background: var(--paper-cream) !important; }
      .page { width: 8.5in !important; height: 11in !important; min-height: 11in !important; box-shadow: none !important; break-after: page !important; page-break-after: always !important; }
      .page:not(.cover-page):not(.divider-page) { background: var(--paper-cream) !important; }
      .cover-page { background: radial-gradient(circle at 50% 35%, #8B1515 0%, #5b0000 65%, #260000 100%) !important; }
      .page-body { background: var(--paper-cream) !important; }
      .doc-section-title { font-family: var(--font-serif) !important; font-size: 20px !important; color: var(--ci-maroon-deep) !important; margin-bottom: 14px !important; }
      .doc-section-title::after { flex: 0 0 1.55in !important; max-width: 1.55in !important; background: linear-gradient(90deg, var(--ci-gold) 0%, rgba(255,193,7,.72) 55%, transparent 100%) !important; }
      .intro-text { font-size: 10.4px !important; line-height: 1.45 !important; margin-bottom: 7px !important; color: var(--text-dark) !important; }
      .studio-subhead { font-family: var(--font-serif); font-size: 13.2px; color: var(--ci-maroon-deep); margin: 10px 0 5px; }
      .studio-list { margin: 5px 0 9px 18px; padding: 0; font-size: 10.1px; line-height: 1.42; }
      .studio-list li { margin-bottom: 3px; }
      .ci-table { font-size: 7.8px !important; margin: 7px 0 10px !important; }
      .ci-table, .ci-table thead, .ci-table tbody, .ci-table tr, .ci-table td, .ci-table th { page-break-inside: avoid !important; break-inside: avoid !important; }
      .ci-table thead tr,
      .ci-table th { background: linear-gradient(180deg, #9C1A1A 0%, var(--ci-maroon-deep) 100%) !important; background-color: var(--ci-maroon-deep) !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; color: #fff !important; border: 1px solid var(--ci-maroon-black) !important; border-top: 1.5px solid var(--ci-gold-dark) !important; font-weight: 500 !important; letter-spacing: 0.06em !important; padding: 5px 6px !important; }
      .ci-table tbody tr { background: rgba(253, 252, 247, 0.98) !important; }
      .ci-table tbody tr:nth-child(even) { background: rgba(139, 21, 21, 0.035) !important; }
      .ci-table td { background: transparent !important; border: 1px solid var(--border-gray) !important; color: var(--text-dark) !important; padding: 5px 6px !important; line-height: 1.3 !important; vertical-align: top !important; }
      .page-footer { margin-top: auto !important; color: var(--text-gray) !important; border-top: 1px solid var(--border-gray) !important; }
      .page:last-child { break-after: auto !important; page-break-after: auto !important; }
      @media print { html, body { background: var(--paper-cream) !important; } .page { break-after: page !important; page-break-after: always !important; } .page:last-child { break-after: auto !important; page-break-after: auto !important; } }
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>{escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
  <style>{style}
{extra_css}</style>
</head>
<body><main class="document-container">{''.join(pages)}</main></body>
</html>"""


def replace_after_cover(target: Path, content_pdf: Path) -> int:
    writer = PdfWriter()
    current = PdfReader(str(target))
    generated = PdfReader(str(content_pdf))
    writer.add_page(current.pages[0])
    for page in generated.pages:
        writer.add_page(page)
    temp = target.with_suffix(".compiled-studio.tmp.pdf")
    with temp.open("wb") as handle:
        writer.write(handle)
    temp.replace(target)
    return len(writer.pages)


def rebuild_course(spec: dict[str, object], style: str) -> dict[str, object]:
    target = OUTPUT_ROOT / str(spec["rel"])
    source = Path(spec["source"])
    before = sha256(target)
    blocks = split_large_tables(parse_markdown(source.read_text(encoding="utf-8", errors="replace")))
    page_blocks = paginate(blocks)
    total = 1 + len(page_blocks)
    pages = []
    for offset, page in enumerate(page_blocks, start=2):
        title, body = blocks_html(page, str(spec["title"]))
        pages.append(content_page(offset, total, str(spec["label"]), title, body))
    tmp = target.with_suffix(".content.tmp.pdf")
    render_html_to_pdf(html_document(style, str(spec["title"]), pages), tmp)
    pages_written = replace_after_cover(target, tmp)
    tmp.unlink(missing_ok=True)
    return {
        "rel": spec["rel"],
        "source": str(source),
        "before_sha256": before,
        "after_sha256": sha256(target),
        "pages": pages_written,
        "content_pages": len(page_blocks),
    }


def handoff_cover(title: str, subtitle: str, side: str) -> str:
    return f"""
    <div class="page cover-page" role="document">
      <div class="frame"></div>
      <div class="corner-block tl"></div><div class="corner-block tr"></div>
      <div class="corner-block bl"></div><div class="corner-block br"></div>
      <div class="side-label left">{escape(side)}</div>
      <div class="side-label right">MVP / SURVEY-READY</div>
      <div class="cover-content">
        <div class="title-stack" style="top: 3.15in;">
          <h2 class="title-california" style="color:#f7f7f7;">California</h2>
          <h1 class="title-main" style="color:#f7f7f7;">{escape(title)}</h1>
          <div class="binder-title">{escape(subtitle)}</div>
          <div class="subtitle">Implementation may start after Vanessa course-material approval</div>
          <div class="facts-line"><span>Compiled Course Materials</span><span class="pipe">|</span><span>Moodle Requirements</span><span class="pipe">|</span><span>Survey-Ready Build Support</span></div>
          <div class="rule"><span class="rule-mark"></span></div>
        </div>
        <div class="provider-stack"><p class="provider-name">CI Institute of Nursing, Inc.</p></div>
        <div class="status-text"><div class="status-title">Status: Vanessa Course-Material Approval Required</div><div class="status-subtitle">Ready for implementation planning and build handoff.</div></div>
      </div>
    </div>
    """


def write_handoff_pdf(rel: str, title: str, subtitle: str, body_blocks: list[dict[str, object]], style: str) -> dict[str, object]:
    target = OUTPUT_ROOT / rel
    before = sha256(target)
    title2, body = blocks_html(body_blocks, title)
    pages = [
        handoff_cover(title, subtitle, "POST-SME MOODLE HANDOFF"),
        content_page(2, 2, "Post-SME Moodle Build Handoff", title2, body),
    ]
    render_html_to_pdf(html_document(style, title, pages), target)
    return {"rel": rel, "before_sha256": before, "after_sha256": sha256(target), "pages": len(PdfReader(str(target)).pages)}


def rebuild_handoff(style: str) -> list[dict[str, object]]:
    readme_blocks = [
        {"kind": "heading", "level": 2, "text": "Moodle Build Handoff"},
        {"kind": "paragraph", "text": "Moodle implementation may begin after Vanessa Valerio, RN approves the course materials for the applicable lane. This is the implementation-start gate for Aldrin and Dagny."},
        {"kind": "paragraph", "text": "Use the compiled course-material packets, Moodle requirements PDF, build workbooks, activity maps, question-bank spreadsheets, completion rules, certificate-gate rules, and implementation tracker. LMS raw course-content PDFs are intentionally excluded from this pass."},
        {"kind": "table", "rows": [["Item", "Build Use"], ["Compiled course-material packets", "Controlling learner-facing content for Moodle shell build."], ["Moodle requirements PDF", "Implementation controls, completion gates, evidence, and survey-ready build requirements."], ["Workbooks and activity maps", "Course setup, question-bank import, interaction mapping, and validation support."], ["Vanessa course-material approval", "Required before implementation work begins."]]},
    ]
    index_blocks = [
        {"kind": "heading", "level": 2, "text": "Moodle Build Index"},
        {"kind": "paragraph", "text": "This index points builders to the implementation materials that remain active for this pass. Raw LMS course-content PDFs are removed; use the compiled course-material packets instead."},
        {"kind": "table", "rows": [["Folder", "Use"], ["04_MOODLE_IMPLEMENTATION_REQUIREMENTS", "Requirements-only implementation binder and build controls."], ["01_CNA_CDPH_CE_APPLICATION/02_COURSE_MATERIALS", "CNA compiled course-material packet, matrix, and workbooks."], ["02_RCFE_CDSS_CETP_APPLICATION/02_COURSE_MATERIALS", "RCFE compiled course-material packet and course matrix."], ["03_BRN_CARE_MANAGER_CEP_APPLICATION/02_COURSE_MATERIALS", "BRN compiled course-material packet and contact-hour map."], ["Vanessa approval", "Course-material approval required before implementation begins."]]},
    ]
    return [
        write_handoff_pdf("05_ALDRIN_DAGNY_POST_SME_HANDOFF/01_POST_SME_MOODLE_BUILD_HANDOFF_READ_ME.pdf", "Moodle Build Handoff", "Post-SME Build Readiness", readme_blocks, style),
        write_handoff_pdf("05_ALDRIN_DAGNY_POST_SME_HANDOFF/02_POST_SME_MOODLE_BUILD_REQUIREMENTS_AND_COURSE_CONTENT_INDEX.pdf", "Moodle Build Index", "Requirements and Course Content Index", index_blocks, style),
    ]


def delete_raw_lms() -> list[dict[str, object]]:
    removed = []
    root_resolved = OUTPUT_ROOT.resolve()
    for rel in RAW_LMS_RELS:
        path = OUTPUT_ROOT / rel
        if path.exists():
            resolved = path.resolve()
            if not str(resolved).lower().startswith(str(root_resolved).lower()):
                raise RuntimeError(f"Refusing to delete outside output root: {resolved}")
            path.unlink()
            removed.append({"rel": rel})
    return removed


def render_samples(paths: list[Path]) -> list[str]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    outputs = []
    for path in paths:
        with fitz.open(path) as doc:
            for index in sorted({0, min(1, doc.page_count - 1)}):
                pix = doc[index].get_pixmap(matrix=fitz.Matrix(0.85, 0.85), colorspace=fitz.csRGB, alpha=False)
                out = QA_DIR / f"{path.stem}_p{index + 1:03d}.png"
                pix.save(out)
                outputs.append(str(out))
    return outputs


def main() -> None:
    style, _ = studio_parts()
    results = [rebuild_course(spec, style) for spec in COURSE_SPECS]
    handoff = rebuild_handoff(style)
    removed = delete_raw_lms()
    sample_paths = [OUTPUT_ROOT / str(spec["rel"]) for spec in COURSE_SPECS]
    sample_paths.extend(OUTPUT_ROOT / item["rel"] for item in handoff)
    report = {"course_results": results, "handoff_results": handoff, "removed_raw_lms": removed, "qa_samples": render_samples(sample_paths)}
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"courses": len(results), "handoff": len(handoff), "removed_raw_lms": len(removed), "report": str(REPORT)}, separators=(",", ":")))


if __name__ == "__main__":
    main()
