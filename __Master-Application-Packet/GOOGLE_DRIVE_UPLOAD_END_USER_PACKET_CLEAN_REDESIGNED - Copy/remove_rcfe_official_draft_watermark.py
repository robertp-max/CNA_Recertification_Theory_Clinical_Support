from __future__ import annotations

import json
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "RCFE_OFFICIAL_DRAFT_WATERMARK_REMOVAL_QA.json"

TARGET_RELS = [
    "02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/01_RCFE_CDSS_APPLICATION_BINDER.pdf",
    "02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/02_RCFE_CDSS_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf",
    "02_RCFE_CDSS_CETP_APPLICATION/01_APPLICATION_SUBMISSION/03_RCFE_CDSS_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf",
]


def draft_text_pages(doc: fitz.Document) -> list[int]:
    pages: list[int] = []
    for index, page in enumerate(doc):
        if "DRAFT" in page.get_text("text").upper():
            pages.append(index + 1)
    return pages


def remove_draft_xobjects(path: Path) -> dict[str, object]:
    with fitz.open(path) as doc:
        before_pages = draft_text_pages(doc)
        draft_xrefs: set[int] = set()
        for page in doc:
            for xref, _name, *_rest in page.get_xobjects():
                try:
                    stream = doc.xref_stream(xref)
                except Exception:
                    continue
                if b"(DRAFT)Tj" in stream or b"DRAFT" in stream:
                    draft_xrefs.add(xref)
        for xref in sorted(draft_xrefs):
            doc.update_stream(xref, b"q\nQ\n")
        after_pages = draft_text_pages(doc)
        temp = path.with_suffix(".no-draft.tmp.pdf")
        doc.save(temp, garbage=4, deflate=True)
    temp.replace(path)
    with fitz.open(path) as verify_doc:
        verify_pages = draft_text_pages(verify_doc)
        page_count = verify_doc.page_count
    return {
        "rel": str(path.relative_to(ROOT)),
        "page_count": page_count,
        "draft_pages_before": before_pages,
        "draft_xobjects_removed": sorted(draft_xrefs),
        "draft_pages_after_save": after_pages,
        "draft_pages_after_reopen": verify_pages,
    }


def main() -> None:
    results = []
    for rel in TARGET_RELS:
        path = ROOT / rel
        if not path.exists():
            results.append({"rel": rel, "missing": True})
            continue
        results.append(remove_draft_xobjects(path))
    REPORT.write_text(json.dumps({"results": results}, indent=2), encoding="utf-8")
    print(json.dumps({"updated": len([r for r in results if not r.get("missing")]), "report": str(REPORT)}, separators=(",", ":")))


if __name__ == "__main__":
    main()
