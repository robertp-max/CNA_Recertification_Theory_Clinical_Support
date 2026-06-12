from __future__ import annotations

import json
import re
import gc
from dataclasses import dataclass
from html import escape
from pathlib import Path

import fitz
from pypdf import PdfReader, PdfWriter

from rebuild_cna_submission_from_studio_html import (
    OUTPUT_ROOT,
    SOURCE_ROOT,
    render_html_to_pdf,
    sha256,
    studio_parts,
)


QA_DIR = Path(r"C:\Users\razer\AppData\Local\Temp\ci_ion_remaining_old_shell_studio_qa")
REPORT = OUTPUT_ROOT / "REMAINING_OLD_SHELL_STUDIO_REPORT.json"


@dataclass(frozen=True)
class Spec:
    rel: str
    label: str
    content_start: int = 1
    content_end: int | None = None
    divider_index: int | None = None
    official_rel: str | None = None


SPECS = [
    Spec("00_START_HERE/00_YADVIR_READ_ME_FIRST_COMPLETE_GUIDE.pdf", "Start Here Read Me"),
    Spec("00_START_HERE/01_MASTER_END_USER_PACKET_INDEX.pdf", "Master End User Packet Index"),
    Spec("00_START_HERE/03_CE_CATALOG_ADDENDUM_AND_WEBSITE_UPDATE_GUIDE.pdf", "Catalog And Website Guide"),
    Spec("01_CNA_CDPH_CE_APPLICATION/02_COURSE_MATERIALS/02_CNA_COURSE_MATRIX_AND_SOURCE_CROSSWALK.pdf", "CNA Course Matrix"),
    Spec(
        "03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/01_BRN_CEP_APPLICATION_BINDER.pdf",
        "BRN CEP Application Binder",
        content_start=1,
        content_end=11,
        divider_index=11,
        official_rel="03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/03_BRN_CEP_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf",
    ),
    Spec(
        "03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/02_BRN_CEP_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf",
        "BRN CEP Minimum Submission Packet",
        content_start=1,
        content_end=2,
        divider_index=2,
        official_rel="03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/03_BRN_CEP_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf",
    ),
    Spec("03_BRN_CARE_MANAGER_CEP_APPLICATION/01_APPLICATION_SUBMISSION/04_BRN_CEP_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf", "BRN CEP Review Context"),
    Spec("03_BRN_CARE_MANAGER_CEP_APPLICATION/02_COURSE_MATERIALS/02_BRN_CONTACT_HOUR_MAP_AND_REPRESENTATIVE_COURSE_PACKET.pdf", "BRN Contact Hour Map"),
]


SKIP_LINE_PATTERNS = [
    re.compile(r"^CI Institute of Nursing$", re.I),
    re.compile(r"^Draft / Pending", re.I),
    re.compile(r"^CI-created page", re.I),
    re.compile(r"^Source page \d+", re.I),
    re.compile(r"^TJ PADILLA /", re.I),
    re.compile(r"^PREPARED JUNE", re.I),
    re.compile(r"^PAGE \d+ OF \d+$", re.I),
    re.compile(r"compiler", re.I),
    re.compile(r"non[- ]operational", re.I),
    re.compile(r"operational role", re.I),
    re.compile(r"operational capacity", re.I),
    re.compile(r"role represents", re.I),
]


def clean_text(value: object) -> str:
    if value is None:
        return ""
    text = str(value).replace("\u2022", "-")
    text = re.sub(r"(?i)\bTJ\s+Padilla\b", "packet records custodian", text)
    text = re.sub(r"(?i)\bYadvir\s+Saandal\b", "packet records custodian", text)
    text = re.sub(r"(?i)\bTJ PADILLA\b", "PACKET RECORDS CUSTODIAN", text)
    text = re.sub(r"(?i)\bYADVIR SAANDAL\b", "PACKET RECORDS CUSTODIAN", text)
    text = re.sub(r"(?i)\bWhat Yadvir Submits and Does Not Submit\b", "What Is Submitted and Not Submitted", text)
    text = re.sub(r"(?i)\bYadvir Deficiency-Response Workflow\b", "Deficiency-Response Workflow", text)
    text = re.sub(r"(?i)\bYadvir guide\b", "Read-me guide", text)
    text = re.sub(r"(?i)\bYadvir / owner\b", "Packet owner", text)
    text = re.sub(r"(?i)\bYadvir Saandal\s*;\s*", "", text)
    text = re.sub(r"(?i)\bYadvir Saandal\s*\(>=\s*4-year retention\)", "Records retained >= 4 years", text)
    text = re.sub(r"(?i)\bRecords custodian:\s*Yadvir Saandal\s*,?\s*", "Records custodian: packet records custodian, ", text)
    text = re.sub(r"(?i)\bYadvir Saandal\b", "packet records custodian", text)
    text = re.sub(r"(?i)\bhuman reviewers\b", "reviewers", text)
    text = re.sub(r"(?i)\bhuman review\b", "review", text)
    text = re.sub(r"(?i)\bhuman verification\b", "verification", text)
    text = re.sub(r"(?i)\b99_NOT_FOR_SUBMISSION_REFERENCE\b", "internal reference archive", text)
    text = re.sub(r"(?i)\braw markdown\b", "raw source documents", text)
    text = re.sub(r"(?i)\bmarkdown\b", "source documents", text)
    text = re.sub(r"(?i)\bOf\s+cial\b", "Official", text)
    text = re.sub(r"(?i)\bO\s+cial\b", "Official", text)
    text = re.sub(r"(?i)\bof\s+icial\b", "official", text)
    text = re.sub(r"(?i)\bconf\s+identiality\b", "confidentiality", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def is_skipped_line(text: str, y0: float, y1: float) -> bool:
    if y0 < 40 or y1 > 735:
        return True
    if not text:
        return True
    return any(pattern.search(text) for pattern in SKIP_LINE_PATTERNS)


def is_meaningful_table(data: list[list[object]]) -> bool:
    if len(data) < 2:
        return False
    header = [clean_text(cell) for cell in data[0]]
    non_empty = [cell for cell in header if cell]
    joined = " ".join(header).lower()
    if len(non_empty) < 2:
        return False
    if "draft / pending" in joined or "ci institute of nursing" in joined:
        return False
    if len(data) <= 3 and any("source page" in clean_text(cell).lower() for row in data for cell in row):
        return False
    return True


def extract_tables(page: fitz.Page) -> list[dict[str, object]]:
    objects: list[dict[str, object]] = []
    try:
        tables = page.find_tables().tables
    except Exception:
        return objects
    for found in tables:
        data = found.extract()
        if not is_meaningful_table(data):
            continue
        rows = [[clean_text(cell) for cell in row] for row in data]
        rows = [row for row in rows if any(row)]
        if not rows:
            continue
        objects.append({"kind": "table", "y": float(found.bbox[1]), "bbox": fitz.Rect(found.bbox), "rows": rows})
    return objects


def page_lines(page: fitz.Page) -> list[dict[str, object]]:
    lines: list[dict[str, object]] = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            bbox = fitz.Rect(line["bbox"])
            text = clean_text(" ".join(span["text"] for span in line.get("spans", [])))
            if is_skipped_line(text, bbox.y0, bbox.y1):
                continue
            size = max((span.get("size", 0) for span in line.get("spans", [])), default=0)
            lines.append({"bbox": bbox, "text": text, "size": size})
    return sorted(lines, key=lambda item: (float(item["bbox"].y0), float(item["bbox"].x0)))


def row_groups(lines: list[dict[str, object]], tolerance: float = 3.5) -> list[list[dict[str, object]]]:
    groups: list[list[dict[str, object]]] = []
    for line in lines:
        y0 = float(line["bbox"].y0)
        if groups and abs(float(groups[-1][0]["bbox"].y0) - y0) <= tolerance:
            groups[-1].append(line)
        else:
            groups.append([line])
    for group in groups:
        group.sort(key=lambda item: float(item["bbox"].x0))
    return groups


def looks_like_table_header(group: list[dict[str, object]]) -> bool:
    if len(group) < 2:
        return False
    joined = " ".join(str(item["text"]).lower() for item in group)
    header_terms = (
        "module",
        "title",
        "hrs",
        "hours",
        "folder",
        "contents",
        "item",
        "status",
        "detail",
        "course",
        "unit",
        "source",
        "map",
        "element",
        "required",
        "notes",
    )
    return sum(1 for term in header_terms if term in joined) >= 2


def nearest_column(x0: float, columns: list[float]) -> int | None:
    distances = [abs(x0 - column) for column in columns]
    if not distances:
        return None
    best = min(range(len(distances)), key=lambda index: distances[index])
    return best if distances[best] <= 34 else None


def extract_aligned_tables(page: fitz.Page) -> list[dict[str, object]]:
    """Recover simple source-PDF tables rendered as aligned text, not PDF table objects."""
    lines = page_lines(page)
    groups = row_groups(lines)
    tables: list[dict[str, object]] = []
    consumed_group_indexes: set[int] = set()

    for start_index, group in enumerate(groups):
        if start_index in consumed_group_indexes or not looks_like_table_header(group):
            continue
        columns = [float(item["bbox"].x0) for item in group]
        if len(columns) < 2:
            continue

        rows: list[list[str]] = [[""] * len(columns)]
        table_rect = fitz.Rect(group[0]["bbox"])
        for item in group:
            col = nearest_column(float(item["bbox"].x0), columns)
            if col is not None:
                rows[0][col] = clean_text(item["text"])
                table_rect.include_rect(item["bbox"])

        current_row: list[str] | None = None
        previous_y = float(group[0]["bbox"].y0)
        used_indexes = {start_index}
        for index in range(start_index + 1, len(groups)):
            next_group = groups[index]
            group_y = float(next_group[0]["bbox"].y0)
            if group_y - previous_y > 52:
                break
            if any(float(item.get("size", 0)) >= 12 for item in next_group):
                break

            mapped = []
            for item in next_group:
                col = nearest_column(float(item["bbox"].x0), columns)
                if col is not None:
                    mapped.append((col, item))
            if not mapped:
                if current_row is not None and group_y - previous_y <= 18:
                    previous_y = group_y
                    continue
                break

            has_first_col = any(col == 0 for col, _ in mapped)
            if len(mapped) == 1 and mapped[0][0] == 0 and current_row is not None and group_y - previous_y <= 14:
                has_first_col = False
            if len(mapped) == 1 and mapped[0][0] == 0 and current_row is not None and group_y - previous_y > 18:
                break
            if has_first_col or current_row is None:
                current_row = [""] * len(columns)
                rows.append(current_row)

            for col, item in mapped:
                text = clean_text(item["text"])
                if not text:
                    continue
                if current_row[col]:
                    if col == 0 and re.fullmatch(r"[A-Z0-9_]+", current_row[col] + text):
                        current_row[col] = f"{current_row[col]}{text}"
                    else:
                        current_row[col] = f"{current_row[col]} {text}"
                else:
                    current_row[col] = text
                table_rect.include_rect(item["bbox"])

            used_indexes.add(index)
            previous_y = group_y

        rows = [row for row in rows if any(cell.strip() for cell in row)]
        if len(rows) < 2 or not is_meaningful_table(rows):
            continue
        for index in used_indexes:
            consumed_group_indexes.add(index)
        tables.append({"kind": "table", "y": float(table_rect.y0), "bbox": table_rect, "rows": rows})
    return tables


def inside_table(line_bbox: fitz.Rect, tables: list[dict[str, object]]) -> bool:
    center = fitz.Point((line_bbox.x0 + line_bbox.x1) / 2, (line_bbox.y0 + line_bbox.y1) / 2)
    return any(table["bbox"].contains(center) for table in tables)


def extract_page_objects(page: fitz.Page, fallback_title: str) -> tuple[str, list[dict[str, object]]]:
    tables = extract_tables(page)
    aligned_tables = extract_aligned_tables(page)
    for table in aligned_tables:
        if not any(table["bbox"].intersects(existing["bbox"]) for existing in tables):
            tables.append(table)
    events: list[dict[str, object]] = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            bbox = fitz.Rect(line["bbox"])
            text = clean_text(" ".join(span["text"] for span in line.get("spans", [])))
            if is_skipped_line(text, bbox.y0, bbox.y1) or inside_table(bbox, tables):
                continue
            size = max((span.get("size", 0) for span in line.get("spans", [])), default=0)
            kind = "heading" if size >= 12 else "bullet" if text.startswith(("?", "-", "*")) else "text"
            if kind == "bullet":
                text = text.lstrip("?-* ").strip()
            events.append({"kind": kind, "y": bbox.y0, "text": text, "size": size})
            events[-1]["x"] = bbox.x0
    events.extend(tables)
    events.sort(key=lambda item: float(item["y"]))

    title = fallback_title
    body_events: list[dict[str, object]] = []
    title_taken = False
    paragraph: list[str] = []
    bullet_group: list[str] = []
    last_bullet_y = -999.0

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            body_events.append({"kind": "paragraph", "text": " ".join(paragraph)})
            paragraph = []

    def flush_bullets() -> None:
        nonlocal bullet_group
        if bullet_group:
            body_events.append({"kind": "bullets", "items": bullet_group})
            bullet_group = []

    for event in events:
        kind = event["kind"]
        if kind == "table":
            flush_paragraph()
            flush_bullets()
            body_events.append(event)
            continue
        text = clean_text(event.get("text", ""))
        if not text:
            continue
        if kind == "heading":
            flush_paragraph()
            flush_bullets()
            if not title_taken:
                title = text
                title_taken = True
            else:
                body_events.append({"kind": "subhead", "text": text})
            continue
        if kind == "bullet":
            flush_paragraph()
            bullet_group.append(text)
            last_bullet_y = float(event.get("y", last_bullet_y))
            continue
        if bullet_group and float(event.get("x", 0)) >= 60 and float(event.get("y", 999)) - last_bullet_y <= 18:
            bullet_group[-1] = f"{bullet_group[-1]} {text}"
            last_bullet_y = float(event.get("y", last_bullet_y))
            continue
        flush_bullets()
        paragraph.append(text)
    flush_paragraph()
    flush_bullets()

    if not body_events:
        body_events.append({"kind": "paragraph", "text": "No additional CI-created content extracted from this page."})
    return title, body_events


def table_html(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    normalized = [row + [""] * (width - len(row)) for row in rows]
    head = "".join(f"<th>{escape(cell)}</th>" for cell in normalized[0])
    body_rows = []
    for row in normalized[1:]:
        row_text = " ".join(row).lower()
        if any(term in row_text for term in ["compiler", "non-operational", "operational role"]):
            continue
        body_rows.append("<tr>" + "".join(f"<td>{escape(cell)}</td>" for cell in row) + "</tr>")
    return f"<table class=\"ci-table\"><thead><tr>{head}</tr></thead><tbody>{''.join(body_rows)}</tbody></table>"


def body_html(events: list[dict[str, object]]) -> str:
    parts: list[str] = []
    for event in events:
        kind = event["kind"]
        if kind == "subhead":
            parts.append(f"<h3 class=\"studio-subhead\">{escape(str(event['text']))}</h3>")
        elif kind == "paragraph":
            parts.append(f"<p class=\"intro-text\">{escape(str(event['text']))}</p>")
        elif kind == "bullets":
            items = "".join(f"<li>{escape(str(item))}</li>" for item in event["items"])
            parts.append(f"<ul class=\"studio-list\">{items}</ul>")
        elif kind == "table":
            parts.append(table_html(event["rows"]))
    return "\n".join(parts)


def content_page(page_number: int, total_pages: int, label: str, title: str, html: str, compact: bool) -> str:
    compact_class = " compact-page" if compact else ""
    return f"""
    <div class="page{compact_class}">
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
      .page {
        width: 8.5in !important;
        height: 11in !important;
        min-height: 11in !important;
        background: var(--paper-cream) !important;
        box-shadow: none !important;
        break-after: page !important;
        page-break-after: always !important;
      }
      .page-body { background: var(--paper-cream) !important; }
      .doc-section-title {
        font-family: var(--font-serif) !important;
        font-size: 20px !important;
        color: var(--ci-maroon-deep) !important;
        margin-bottom: 14px !important;
      }
      .doc-section-title::after { flex: 0 0 1.55in !important; max-width: 1.55in !important; background: linear-gradient(90deg, var(--ci-gold) 0%, rgba(255,193,7,.72) 55%, transparent 100%) !important; }
      .intro-text { font-size: 10.6px !important; line-height: 1.48 !important; margin-bottom: 8px !important; color: var(--text-dark) !important; }
      .studio-subhead { font-family: var(--font-serif); font-size: 14px; color: var(--ci-maroon-deep); margin: 12px 0 6px; }
      .studio-list { margin: 6px 0 10px 18px; padding: 0; font-size: 10.3px; line-height: 1.45; }
      .studio-list li { margin-bottom: 4px; }
      .ci-table { font-size: 8.5px !important; margin: 8px 0 12px !important; }
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
      .ci-table td { background: transparent !important; border: 1px solid var(--border-gray) !important; color: var(--text-dark) !important; padding: 6px 8px !important; line-height: 1.35 !important; }
      .compact-page .intro-text { font-size: 9.8px !important; line-height: 1.38 !important; margin-bottom: 6px !important; }
      .compact-page .studio-subhead { font-size: 13px; margin: 9px 0 5px; }
      .compact-page .ci-table { font-size: 7.8px !important; }
      .page-footer { margin-top: auto !important; color: var(--text-gray) !important; border-top: 1px solid var(--border-gray) !important; }
      .page:last-child { break-after: auto !important; page-break-after: auto !important; }
      @media print {
        html, body { background: var(--paper-cream) !important; }
        .page { break-after: page !important; page-break-after: always !important; }
        .page:last-child { break-after: auto !important; page-break-after: auto !important; }
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


def build_content_pdf(spec: Spec, style: str, target: Path, content_indices: list[int]) -> Path:
    source = SOURCE_ROOT / spec.rel
    content_source = source if source.exists() else target
    total = len(PdfReader(str(target)).pages)
    with fitz.open(content_source) as doc:
        pages: list[str] = []
        for index in content_indices:
            if index >= doc.page_count:
                raise RuntimeError(f"{spec.rel}: source content page {index + 1} is missing.")
            fallback = spec.label
            title, events = extract_page_objects(doc[index], fallback)
            compact = len(events) > 16 or sum(len(event.get("rows", [])) for event in events if event["kind"] == "table") > 12
            pages.append(content_page(index + 1, total, spec.label, title, body_html(events), compact))
    temp = target.with_suffix(".studio-content.tmp.pdf")
    render_html_to_pdf(html_document(style, spec.label, pages), temp)
    if len(PdfReader(str(temp)).pages) != len(content_indices):
        raise RuntimeError(f"{spec.rel}: rendered {len(PdfReader(str(temp)).pages)} content pages, expected {len(content_indices)}")
    return temp


def replace_pdf(spec: Spec, style: str) -> dict[str, object]:
    target = OUTPUT_ROOT / spec.rel
    if not target.exists():
        raise FileNotFoundError(target)
    before = sha256(target)
    current_reader = PdfReader(str(target))
    original_pages = len(current_reader.pages)
    end = spec.content_end if spec.content_end is not None else original_pages
    content_indices = list(range(spec.content_start, end))
    content_pdf = build_content_pdf(spec, style, target, content_indices)
    content_reader = PdfReader(str(content_pdf))
    writer = PdfWriter()
    writer.add_page(current_reader.pages[0])
    for page in content_reader.pages:
        writer.add_page(page)
    if spec.divider_index is not None:
        writer.add_page(current_reader.pages[spec.divider_index])
    if spec.official_rel:
        official_path = SOURCE_ROOT / spec.official_rel
        if not official_path.exists():
            raise FileNotFoundError(official_path)
        official_reader = PdfReader(str(official_path))
        for page in official_reader.pages:
            writer.add_page(page)
    temp = target.with_suffix(".merged.tmp.pdf")
    with temp.open("wb") as handle:
        writer.write(handle)
    for reader in [current_reader, content_reader] + ([official_reader] if spec.official_rel else []):
        stream = getattr(reader, "stream", None)
        if stream:
            stream.close()
    del writer, current_reader, content_reader
    if spec.official_rel:
        del official_reader
    gc.collect()
    try:
        temp.replace(target)
    except PermissionError as exc:
        pending = target.with_suffix(".pending-replace.pdf")
        temp.replace(pending)
        content_pdf.unlink(missing_ok=True)
        return {
            "rel": spec.rel,
            "before_sha256": before,
            "after_sha256": before,
            "pages": original_pages,
            "content_pages_regenerated": len(content_indices),
            "official_appended_from_source": bool(spec.official_rel),
            "status": "blocked_target_locked",
            "pending_replacement": str(pending),
            "error": str(exc),
        }
    content_pdf.unlink(missing_ok=True)
    after_pages = len(PdfReader(str(target)).pages)
    expected_pages = (
        1
        + len(content_indices)
        + (1 if spec.divider_index is not None else 0)
        + (len(PdfReader(str(SOURCE_ROOT / spec.official_rel)).pages) if spec.official_rel else 0)
    )
    if after_pages != expected_pages:
        raise RuntimeError(f"{spec.rel}: output has {after_pages} pages, expected {expected_pages}")
    return {
        "rel": spec.rel,
        "before_sha256": before,
        "after_sha256": sha256(target),
        "pages": after_pages,
        "content_pages_regenerated": len(content_indices),
        "official_appended_from_source": bool(spec.official_rel),
        "status": "updated",
    }


def render_samples(results: list[dict[str, object]]) -> list[str]:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []
    for result in results:
        path = OUTPUT_ROOT / str(result["rel"])
        with fitz.open(path) as doc:
            index = min(1, doc.page_count - 1)
            pix = doc[index].get_pixmap(matrix=fitz.Matrix(0.85, 0.85), colorspace=fitz.csRGB, alpha=False)
            out = QA_DIR / f"{path.stem}_p{index + 1:03d}.png"
            pix.save(out)
            outputs.append(str(out))
    return outputs


def verify_official_appends() -> list[dict[str, object]]:
    checks: list[dict[str, object]] = []
    for spec in SPECS:
        if not spec.official_rel:
            continue
        target = OUTPUT_ROOT / spec.rel
        official = SOURCE_ROOT / spec.official_rel
        prefix_count = 1 + len(range(spec.content_start, spec.content_end or 0)) + (1 if spec.divider_index is not None else 0)
        issues: list[str] = []
        with fitz.open(target) as output_doc, fitz.open(official) as official_doc:
            if output_doc.page_count - prefix_count != official_doc.page_count:
                issues.append("official appendix page count mismatch")
            else:
                for index in range(official_doc.page_count):
                    src_pix = official_doc[index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                    out_pix = output_doc[prefix_count + index].get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
                    if src_pix.width != out_pix.width or src_pix.height != out_pix.height or src_pix.samples != out_pix.samples:
                        issues.append(f"official page {index + 1} render mismatch")
                        break
        checks.append({"rel": spec.rel, "issues": issues})
    return checks


def verify_updated_official_appends(results: list[dict[str, object]]) -> list[dict[str, object]]:
    updated = {str(result["rel"]) for result in results if result.get("status") == "updated"}
    original_specs = SPECS
    try:
        globals()["SPECS"] = tuple(spec for spec in original_specs if spec.rel in updated)
        return verify_official_appends()
    finally:
        globals()["SPECS"] = original_specs


def main() -> None:
    style, _ = studio_parts()
    results = [replace_pdf(spec, style) for spec in SPECS]
    official_checks = verify_updated_official_appends(results)
    failures = [check for check in official_checks if check["issues"]]
    if failures:
        raise RuntimeError(json.dumps(failures, indent=2))
    report = {
        "updated": sum(1 for result in results if result.get("status") == "updated"),
        "blocked": [result for result in results if result.get("status") != "updated"],
        "results": results,
        "official_checks": official_checks,
        "qa_samples": render_samples([result for result in results if result.get("status") == "updated"]),
    }
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"updated": report["updated"], "blocked": len(report["blocked"]), "official_compare_failures": 0, "report": str(REPORT)}, separators=(",", ":")))


if __name__ == "__main__":
    main()
