from __future__ import annotations

import json
import re
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parent
REPORT_JSON = ROOT / "ALL_PDF_STYLE_TRUNCATION_SCAN.json"
REPORT_MD = ROOT / "ALL_PDF_STYLE_TRUNCATION_SCAN.md"

OFFICIAL_NAMES = (
    "OFFICIAL_FORMS_READY_FOR_SIGNATURE",
    "CDPH",
    "LIC_9140",
    "LIC_9141",
    "BRN_CEP_OFFICIAL",
)

MARKDOWN_PATTERNS = [
    re.compile(r"^\s{0,3}#{1,6}\s+\S", re.MULTILINE),
    re.compile(r"\*\*[^*\n]{2,}\*\*"),
    re.compile(r"^\s*\|.*\|\s*$", re.MULTILINE),
    re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", re.MULTILINE),
    re.compile(r"`[^`\n]+`"),
]

RAW_MARKDOWN_WORDS = (
    "```",
    "markdown",
    "## ",
    "### ",
    "**",
    "| ---",
    "|---",
)

AGENCY_DRAFT_TERMS = (
    "Draft / Pending Agency Approval",
    "Draft / Pending CDSS/ACS Approval",
    "Draft / Pending BRN CEP Approval",
    "Draft / Pending CDPH Approval",
)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def is_official_pdf(path: Path) -> bool:
    name = path.name.upper()
    return "OFFICIAL_FORMS_READY_FOR_SIGNATURE" in name


def page_flags(page: fitz.Page, page_index: int) -> dict:
    text = page.get_text("text")
    flags: dict[str, object] = {
        "page": page_index + 1,
        "raw_markdown_hits": [],
        "bottom_text_blocks": [],
        "overflow_blocks": [],
        "agency_draft_terms": [],
        "draft_text_hits": 0,
    }

    for pattern in MARKDOWN_PATTERNS:
        matches = pattern.findall(text)
        if matches:
            flags["raw_markdown_hits"].append(pattern.pattern)

    for word in RAW_MARKDOWN_WORDS:
        if word in text:
            flags["raw_markdown_hits"].append(word)

    for term in AGENCY_DRAFT_TERMS:
        if term in text:
            flags["agency_draft_terms"].append(term)

    if "DRAFT" in text.upper():
        flags["draft_text_hits"] = text.upper().count("DRAFT")

    page_height = page.rect.height
    footer_guard_y = page_height - 44
    trim_guard_y = page_height - 12
    for block in page.get_text("blocks"):
        x0, y0, x1, y1, block_text = block[:5]
        snippet = " ".join(str(block_text).split())[:130]
        if not snippet:
            continue
        if y1 > footer_guard_y:
            flags["bottom_text_blocks"].append(
                {"bbox": [round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1)], "text": snippet}
            )
        if y1 > trim_guard_y or x1 > page.rect.width - 8 or x0 < 8:
            flags["overflow_blocks"].append(
                {"bbox": [round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1)], "text": snippet}
            )

    return flags


def main() -> None:
    pdfs = sorted(ROOT.rglob("*.pdf"))
    findings = []
    totals = {
        "pdf_count": len(pdfs),
        "pdfs_with_raw_markdown": 0,
        "pdfs_with_bottom_text": 0,
        "pdfs_with_overflow": 0,
        "pdfs_with_agency_draft_terms": 0,
        "official_pdfs_with_draft_text": 0,
    }

    for pdf in pdfs:
        item = {
            "rel": rel(pdf),
            "official_form_pdf": is_official_pdf(pdf),
            "page_count": 0,
            "raw_markdown_pages": [],
            "bottom_text_pages": [],
            "overflow_pages": [],
            "agency_draft_pages": [],
            "draft_text_pages": [],
            "open_error": None,
        }
        try:
            doc = fitz.open(pdf)
        except Exception as exc:  # pragma: no cover - report only
            item["open_error"] = str(exc)
            findings.append(item)
            continue

        item["page_count"] = doc.page_count
        for page_index in range(doc.page_count):
            flags = page_flags(doc[page_index], page_index)
            page_no = flags["page"]
            if flags["raw_markdown_hits"]:
                item["raw_markdown_pages"].append(
                    {"page": page_no, "hits": sorted(set(flags["raw_markdown_hits"]))[:8]}
                )
            if flags["bottom_text_blocks"]:
                item["bottom_text_pages"].append(
                    {"page": page_no, "blocks": flags["bottom_text_blocks"][:4]}
                )
            if flags["overflow_blocks"]:
                item["overflow_pages"].append(
                    {"page": page_no, "blocks": flags["overflow_blocks"][:4]}
                )
            if flags["agency_draft_terms"]:
                item["agency_draft_pages"].append(
                    {"page": page_no, "terms": sorted(set(flags["agency_draft_terms"]))}
                )
            if flags["draft_text_hits"]:
                item["draft_text_pages"].append({"page": page_no, "hits": flags["draft_text_hits"]})
        doc.close()

        if item["raw_markdown_pages"]:
            totals["pdfs_with_raw_markdown"] += 1
        if item["bottom_text_pages"]:
            totals["pdfs_with_bottom_text"] += 1
        if item["overflow_pages"]:
            totals["pdfs_with_overflow"] += 1
        if item["agency_draft_pages"]:
            totals["pdfs_with_agency_draft_terms"] += 1
        if item["official_form_pdf"] and item["draft_text_pages"]:
            totals["official_pdfs_with_draft_text"] += 1
        findings.append(item)

    report = {"root": str(ROOT), "totals": totals, "findings": findings}
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# All PDF Style / Truncation Scan",
        "",
        f"- PDFs scanned: {totals['pdf_count']}",
        f"- PDFs with raw Markdown indicators: {totals['pdfs_with_raw_markdown']}",
        f"- PDFs with text in footer guard area: {totals['pdfs_with_bottom_text']}",
        f"- PDFs with trim-edge overflow indicators: {totals['pdfs_with_overflow']}",
        f"- PDFs with agency draft wording: {totals['pdfs_with_agency_draft_terms']}",
        f"- Official-form PDFs with DRAFT text: {totals['official_pdfs_with_draft_text']}",
        "",
        "## Suspect Files",
        "",
    ]
    for item in findings:
        if not (
            item["open_error"]
            or item["raw_markdown_pages"]
            or item["bottom_text_pages"]
            or item["overflow_pages"]
            or item["agency_draft_pages"]
            or (item["official_form_pdf"] and item["draft_text_pages"])
        ):
            continue
        lines.append(f"### {item['rel']}")
        lines.append(f"- Pages: {item['page_count']}")
        if item["open_error"]:
            lines.append(f"- Open error: {item['open_error']}")
        if item["raw_markdown_pages"]:
            pages = ", ".join(str(p["page"]) for p in item["raw_markdown_pages"][:24])
            lines.append(f"- Raw Markdown indicator pages: {pages}")
        if item["bottom_text_pages"]:
            pages = ", ".join(str(p["page"]) for p in item["bottom_text_pages"][:24])
            lines.append(f"- Footer guard pages: {pages}")
        if item["overflow_pages"]:
            pages = ", ".join(str(p["page"]) for p in item["overflow_pages"][:24])
            lines.append(f"- Trim-edge overflow pages: {pages}")
        if item["agency_draft_pages"]:
            pages = ", ".join(str(p["page"]) for p in item["agency_draft_pages"][:24])
            lines.append(f"- Agency draft wording pages: {pages}")
        if item["official_form_pdf"] and item["draft_text_pages"]:
            pages = ", ".join(str(p["page"]) for p in item["draft_text_pages"][:24])
            lines.append(f"- Official-form DRAFT text pages: {pages}")
        lines.append("")
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(totals, indent=2))


if __name__ == "__main__":
    main()
