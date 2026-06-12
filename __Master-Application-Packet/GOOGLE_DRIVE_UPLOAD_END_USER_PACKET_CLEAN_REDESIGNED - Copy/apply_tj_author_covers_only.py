import hashlib
import json
import shutil
import tempfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter

from apply_folderwide_studio_covers_and_dividers import (
    OFFICIAL_ONLY,
    OUTPUT_ROOT,
    QA_DIR,
    cover_page,
    logo_src,
    rel,
    rel_text,
    render_one_page,
    render_qa_samples,
    sha256,
    studio_css,
)


REPORT = OUTPUT_ROOT / "TJ_AUTHOR_COVER_ONLY_REPORT.json"


def replace_cover_page(target: Path, cover_pdf: Path) -> None:
    original = PdfReader(str(target))
    replacement = PdfReader(str(cover_pdf))
    writer = PdfWriter()
    for index, page in enumerate(original.pages):
        writer.add_page(replacement.pages[0] if index == 0 else page)
    tmp = target.with_suffix(".folderwide-cover.tmp.pdf")
    with tmp.open("wb") as handle:
        writer.write(handle)
    for reader in (original, replacement):
        stream = getattr(reader, "stream", None)
        if stream:
            stream.close()
    try:
        tmp.replace(target)
    except PermissionError:
        shutil.copyfile(tmp, target)
        tmp.unlink(missing_ok=True)


def main() -> None:
    css = studio_css()
    logo = logo_src()
    work = Path(tempfile.gettempdir()) / "ci_ion_tj_author_covers_only"
    work.mkdir(parents=True, exist_ok=True)
    updated: list[Path] = []
    skipped: list[dict[str, str]] = []
    results: list[dict[str, object]] = []

    for pdf in sorted(OUTPUT_ROOT.rglob("*.pdf")):
        if "QA_RENDER" in str(pdf):
            continue
        relative = rel(pdf)
        relative_posix = Path(str(relative).replace("\\", "/"))
        if relative_posix in OFFICIAL_ONLY:
            skipped.append({"rel": rel_text(relative), "reason": "official government form left unchanged"})
            continue
        cover_pdf = work / (hashlib.sha256(rel_text(relative).encode("utf-8")).hexdigest()[:16] + "_tj_cover.pdf")
        render_one_page(cover_page(relative, logo), cover_pdf, css)
        before = sha256(pdf)
        page_total = len(PdfReader(str(pdf)).pages)
        replace_cover_page(pdf, cover_pdf)
        after_total = len(PdfReader(str(pdf)).pages)
        if after_total != page_total:
            raise RuntimeError(f"{rel_text(relative)} page count changed from {page_total} to {after_total}")
        updated.append(pdf)
        results.append(
            {
                "rel": rel_text(relative),
                "pages_replaced": [1],
                "previous_sha256": before,
                "new_sha256": sha256(pdf),
                "pages": after_total,
            }
        )

    samples = render_qa_samples(updated[:12])
    REPORT.write_text(
        json.dumps(
            {
                "status": "complete",
                "updated_pdf_count": len(updated),
                "skipped_official_count": len(skipped),
                "results": results,
                "skipped": skipped,
                "qa_samples": samples,
                "qa_dir": str(QA_DIR),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps({"updated": len(updated), "skipped_official": len(skipped), "report": str(REPORT)}, separators=(",", ":")))


if __name__ == "__main__":
    main()
