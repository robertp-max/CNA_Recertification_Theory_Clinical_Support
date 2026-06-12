from __future__ import annotations

import json
import tempfile
from html import escape
from pathlib import Path

import fitz
from pypdf import PdfReader, PdfWriter

from rebuild_cna_submission_from_studio_html import render_html_to_pdf
from rebuild_rcfe_application_binder_studio_html import OUTPUT_ROOT, studio_css


TARGETS = [
    (
        OUTPUT_ROOT / "02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/01_RCFE_CDSS_APPLICATION_BINDER.pdf",
        11,
    ),
    (
        OUTPUT_ROOT / "02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/02_RCFE_CDSS_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf",
        2,
    ),
]

REPORT = OUTPUT_ROOT / "RCFE_DARK_APPENDIX_DIVIDER_FIX_REPORT.json"


def divider_html() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
  <style>
{studio_css()}
    html, body {{ width: 8.5in; margin: 0; background: #1a0000 !important; }}
    body {{ display: block !important; padding: 0 !important; }}
    .document-container {{ display: block !important; padding: 0 !important; gap: 0 !important; }}
    .page {{ width: 8.5in !important; height: 11in !important; min-height: 11in !important; box-shadow: none !important; page-break-after: auto !important; break-after: auto !important; }}
    .divider-page {{ background: radial-gradient(circle at center, #610000 0%, #3d0000 70%, #1a0000 100%) !important; }}
    .divider-title {{ color: var(--ci-gold) !important; }}
  </style>
</head>
<body>
  <main class="document-container">
    <div id="p-divider" class="page divider-page">
      <div class="frame"></div>
      <div class="corner-block tl"></div>
      <div class="corner-block tr"></div>
      <div class="corner-block bl"></div>
      <div class="corner-block br"></div>
      <div class="divider-content">
        <h1 class="divider-title">{escape("Appendix")}</h1>
        <h2 style="color: white; font-size: 16px; font-weight: 300; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 20px;">Official Forms Packet</h2>
        <div class="divider-sub">Official government forms are appended as original unbranded PDF pages. No CI styling, headers, footers, borders, watermarks, page numbers, or visual alterations have been applied.</div>
      </div>
    </div>
  </main>
</body>
</html>"""


def replace_page(target: Path, index: int, page_pdf: Path) -> dict[str, object]:
    reader = PdfReader(str(target))
    replacement = PdfReader(str(page_pdf))
    writer = PdfWriter()
    for page_index, page in enumerate(reader.pages):
        writer.add_page(replacement.pages[0] if page_index == index else page)
    temp = target.with_suffix(".dark-divider.tmp.pdf")
    with temp.open("wb") as handle:
        writer.write(handle)
    temp.replace(target)
    with fitz.open(target) as doc:
        text = doc[index].get_text("text")
        pix = doc[index].get_pixmap(matrix=fitz.Matrix(0.5, 0.5), colorspace=fitz.csRGB, alpha=False)
    return {"rel": str(target.relative_to(OUTPUT_ROOT)), "page": index + 1, "text_contains_appendix": "Appendix" in text, "sample_digest": pix.digest.hex()}


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="ci_ion_rcfe_dark_divider_") as tmp:
        divider_pdf = Path(tmp) / "divider.pdf"
        render_html_to_pdf(divider_html(), divider_pdf)
        results = [replace_page(path, index, divider_pdf) for path, index in TARGETS]
    REPORT.write_text(json.dumps({"results": results}, indent=2), encoding="utf-8")
    print(json.dumps({"updated": len(results), "report": str(REPORT)}, separators=(",", ":")))


if __name__ == "__main__":
    main()
