"""extract_cccco_text.py

Deterministic text extraction from the highest source of truth -- the CCCCO/NATP
Model Curriculum module PDFs (Modules 10-17) -- into plain-text files that the
survey-evidence mapping is built from.

Source:  CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-{10..17}.pdf
Output:  CNA-Recert-Course/ContentV2/survey-evidence/_source_text/module-{NN}.txt
         CNA-Recert-Course/ContentV2/survey-evidence/_source_text/_extraction_manifest.json

No content is invented. This only mirrors the PDF text so the mapping has a
reproducible, inspectable basis. Re-run is idempotent.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
PDF_DIR = ROOT / "CNA-Recert-Course" / "CNA_Modules"
OUT_DIR = ROOT / "CNA-Recert-Course" / "ContentV2" / "survey-evidence" / "_source_text"

MODULES = list(range(10, 18))  # CCCCO Modules 10-17 (in-scope for recert theory crosswalk)


def clean(text: str) -> str:
    # Normalise whitespace/newlines without dropping structure (keep line breaks).
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # collapse runs of spaces/tabs
    text = re.sub(r"[ \t]+", " ", text)
    # collapse 3+ blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_module(n: int) -> dict:
    pdf = PDF_DIR / f"cccco-na-model-curriculum-module-{n}.pdf"
    if not pdf.exists():
        return {"module": n, "status": "MISSING", "pdf": pdf.name}
    reader = PdfReader(str(pdf))
    pages = []
    for i, page in enumerate(reader.pages):
        try:
            pages.append(page.extract_text() or "")
        except Exception as exc:  # pragma: no cover - defensive
            pages.append(f"[[extraction error page {i}: {exc}]]")
    body = clean("\n\n".join(pages))
    out = OUT_DIR / f"module-{n:02d}.txt"
    out.write_text(body, encoding="utf-8")
    return {
        "module": n,
        "status": "OK",
        "pdf": pdf.name,
        "pages": len(reader.pages),
        "chars": len(body),
        "words": len(body.split()),
        "out": str(out.relative_to(ROOT)).replace("\\", "/"),
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = [extract_module(n) for n in MODULES]
    (OUT_DIR / "_extraction_manifest.json").write_text(
        json.dumps({"source_dir": str(PDF_DIR.relative_to(ROOT)).replace("\\", "/"),
                    "modules": manifest}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": "OK", "modules": manifest}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
