from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitz
from pypdf import PdfReader


SOURCE_ROOT = Path(
    r"C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\__Master-Application-Packet\GOOGLE_DRIVE_UPLOAD_END_USER_PACKET_CLEAN - Copy - Copy"
)
OUTPUT_ROOT = Path(__file__).resolve().parent
DESIGN_HTML = Path(r"C:\Users\razer\Downloads\ci_ion_pdf_binder_studio.html")

PROGRESS_PATH = OUTPUT_ROOT / "REDESIGN_PROGRESS.json"
RUN_LOG_PATH = OUTPUT_ROOT / "REDESIGN_RUN_LOG.txt"
QA_REPORT_PATH = OUTPUT_ROOT / "REDESIGN_QA_REPORT.md"
SKIPPED_PATH = OUTPUT_ROOT / "REDESIGN_SKIPPED_FILES.md"

OFFICIAL_FORM_RELS = {
    r"01_CNA_CDPH_CE_APPLICATION\01_APPLICATION_SUBMISSION\03_CNA_CDPH_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf",
    r"02_RCFE_CDSS_CETP_APPLICATION\01_APPLICATION_SUBMISSION\03_RCFE_CDSS_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf",
    r"03_BRN_CARE_MANAGER_CEP_APPLICATION\01_APPLICATION_SUBMISSION\03_BRN_CEP_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf",
}

MIXED_APPENDIX_MAP = {
    r"01_CNA_CDPH_CE_APPLICATION\01_APPLICATION_SUBMISSION\01_CNA_CDPH_APPLICATION_BINDER.pdf": (
        r"01_CNA_CDPH_CE_APPLICATION\01_APPLICATION_SUBMISSION\03_CNA_CDPH_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"
    ),
    r"01_CNA_CDPH_CE_APPLICATION\01_APPLICATION_SUBMISSION\02_CNA_CDPH_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf": (
        r"01_CNA_CDPH_CE_APPLICATION\01_APPLICATION_SUBMISSION\03_CNA_CDPH_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"
    ),
    r"02_RCFE_CDSS_CETP_APPLICATION\01_APPLICATION_SUBMISSION\01_RCFE_CDSS_APPLICATION_BINDER.pdf": (
        r"02_RCFE_CDSS_CETP_APPLICATION\01_APPLICATION_SUBMISSION\03_RCFE_CDSS_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"
    ),
    r"02_RCFE_CDSS_CETP_APPLICATION\01_APPLICATION_SUBMISSION\02_RCFE_CDSS_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf": (
        r"02_RCFE_CDSS_CETP_APPLICATION\01_APPLICATION_SUBMISSION\03_RCFE_CDSS_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"
    ),
    r"03_BRN_CARE_MANAGER_CEP_APPLICATION\01_APPLICATION_SUBMISSION\01_BRN_CEP_APPLICATION_BINDER.pdf": (
        r"03_BRN_CARE_MANAGER_CEP_APPLICATION\01_APPLICATION_SUBMISSION\03_BRN_CEP_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"
    ),
    r"03_BRN_CARE_MANAGER_CEP_APPLICATION\01_APPLICATION_SUBMISSION\02_BRN_CEP_MINIMUM_REQUIRED_SUBMISSION_PACKET.pdf": (
        r"03_BRN_CARE_MANAGER_CEP_APPLICATION\01_APPLICATION_SUBMISSION\03_BRN_CEP_OFFICIAL_FORMS_READY_FOR_SIGNATURE.pdf"
    ),
}

PENDING_CONTEXT_RELS = {
    r"01_CNA_CDPH_CE_APPLICATION\01_APPLICATION_SUBMISSION\04_CNA_CDPH_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf",
    r"02_RCFE_CDSS_CETP_APPLICATION\01_APPLICATION_SUBMISSION\04_RCFE_CDSS_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf",
    r"03_BRN_CARE_MANAGER_CEP_APPLICATION\01_APPLICATION_SUBMISSION\04_BRN_CEP_MISSING_OR_PENDING_SUBMISSION_ITEMS.pdf",
}

REMOVED_PENDING_TERMS = (
    "Final verification",
    "Yadvir / owner confirmation",
    "Build-Remediable vs Human/Regulator Items",
    "Why pending",
    "Due/action needed",
    "Blocks submission?",
)

BUILD_ARTIFACT_SUFFIXES = (
    ".tmp.pdf",
    ".tmp.html",
    ".bak",
    ".log.tmp",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def rel_from_root(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("/", "\\")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def page_count(path: Path) -> int:
    reader = PdfReader(str(path))
    return len(reader.pages)


def extract_text(path: Path) -> str:
    with fitz.open(path) as doc:
        return "\n".join(page.get_text("text") for page in doc)


def render_digest(path: Path, page_index: int) -> dict[str, Any]:
    with fitz.open(path) as doc:
        page = doc.load_page(page_index)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
        digest = hashlib.sha256(pix.samples).hexdigest()
        return {"width": pix.width, "height": pix.height, "sha256": digest}


def classify(rel: str) -> str:
    upper = rel.upper()
    name = Path(rel).name.upper()
    if rel in OFFICIAL_FORM_RELS:
        return "official_government_form"
    if rel in MIXED_APPENDIX_MAP:
        return "mixed_binder_with_official_appendix"
    if "COURSE_MATERIALS" in upper:
        return "ci_created_course_material_packet"
    if "MISSING_OR_PENDING" in name or "INDEX" in name or "CHECKLIST" in name or "TRACKER" in name:
        return "tracker_checklist_index"
    if "MOODLE" in upper or "HANDOFF" in upper:
        return "moodle_requirement_support_document"
    return "ci_created_binder_document"


def source_pdf_rels() -> list[str]:
    return sorted(rel_from_root(p, SOURCE_ROOT) for p in SOURCE_ROOT.rglob("*.pdf") if p.is_file())


def output_pdf_rels() -> list[str]:
    return sorted(rel_from_root(p, OUTPUT_ROOT) for p in OUTPUT_ROOT.rglob("*.pdf") if p.is_file())


def is_build_artifact(rel: str) -> bool:
    lower = rel.lower()
    return any(lower.endswith(suffix) for suffix in BUILD_ARTIFACT_SUFFIXES)


def base_progress() -> dict[str, Any]:
    rels = source_pdf_rels()
    return {
        "run_id": "ci-ion-redesign-safe-checkpoint",
        "mode": "safe_checkpoint",
        "source_root": str(SOURCE_ROOT),
        "output_root": str(OUTPUT_ROOT),
        "design_html": str(DESIGN_HTML),
        "created_utc": utc_now(),
        "last_updated_utc": utc_now(),
        "total_source_pdfs": len(rels),
        "completed": 0,
        "pending": len(rels),
        "blocked": 0,
        "skipped": 0,
        "next_file": rels[0] if rels else None,
        "official_forms_altered": False,
        "hard_stop_encountered": False,
        "files": [
            {
                "rel": rel,
                "classification": classify(rel),
                "status": "pending",
                "source_pages": None,
                "output_pages": None,
                "source_sha256": None,
                "output_sha256": None,
                "qa": [],
                "notes": [],
                "updated_utc": None,
            }
            for rel in rels
        ],
        "skipped_files": [],
        "qa": {
            "mixed_appendix_verified": [],
            "mixed_appendix_failed": [],
            "pending_context_terms_found": [],
            "official_form_hash_mismatches": [],
        },
    }


def load_progress() -> dict[str, Any]:
    if PROGRESS_PATH.exists():
        data = json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
        if "files" in data:
            return data
    return base_progress()


def write_json_atomic(path: Path, data: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=True), encoding="utf-8")
    tmp.replace(path)


def log(message: str) -> None:
    RUN_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with RUN_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"{utc_now()} {message}\n")


def recalc_counts(progress: dict[str, Any]) -> None:
    files = progress["files"]
    progress["completed"] = sum(1 for item in files if item["status"] == "completed")
    progress["blocked"] = sum(1 for item in files if item["status"] == "blocked")
    progress["pending"] = sum(1 for item in files if item["status"] in {"pending", "in_progress"})
    progress["skipped"] = len(progress.get("skipped_files", []))
    next_item = next((item for item in files if item["status"] in {"pending", "in_progress"}), None)
    progress["next_file"] = next_item["rel"] if next_item else None
    progress["last_updated_utc"] = utc_now()
    progress["hard_stop_encountered"] = progress["blocked"] > 0


def write_reports(progress: dict[str, Any]) -> None:
    recalc_counts(progress)
    qa = progress.get("qa", {})
    lines = [
        "# CI-ION Redesign QA Report",
        "",
        f"- Source folder verified: {SOURCE_ROOT.exists()}",
        f"- Output folder verified: {OUTPUT_ROOT.exists()}",
        f"- Design HTML verified: {DESIGN_HTML.exists()}",
        f"- PDFs processed/adopted: {progress['completed']}",
        f"- PDFs pending: {progress['pending']}",
        f"- PDFs blocked: {progress['blocked']}",
        f"- Standalone official form hash mismatches: {len(qa.get('official_form_hash_mismatches', []))}",
        f"- Mixed appendix verifications passed: {len(qa.get('mixed_appendix_verified', []))}",
        f"- Mixed appendix verifications failed: {len(qa.get('mixed_appendix_failed', []))}",
        f"- Removed pending-context terms found: {len(qa.get('pending_context_terms_found', []))}",
        "",
        "Official government forms are preserved by direct PDF copy/append validation. No CI styling is applied by this checkpoint runner.",
    ]
    if qa.get("mixed_appendix_failed"):
        lines.append("")
        lines.append("## Mixed Appendix Failures")
        for item in qa["mixed_appendix_failed"]:
            lines.append(f"- {item['mixed_rel']}: {item['reason']}")
    if qa.get("pending_context_terms_found"):
        lines.append("")
        lines.append("## Removed Pending-Context Terms Found")
        for item in qa["pending_context_terms_found"]:
            lines.append(f"- {item['rel']}: {item['term']}")
    QA_REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    skipped_lines = ["# Skipped Files", ""]
    skipped = progress.get("skipped_files", [])
    if not skipped:
        skipped_lines.append("No skipped files recorded.")
    else:
        for item in skipped:
            skipped_lines.append(f"- {item['rel']}: {item['reason']}")
    SKIPPED_PATH.write_text("\n".join(skipped_lines) + "\n", encoding="utf-8")


def save_progress(progress: dict[str, Any]) -> None:
    recalc_counts(progress)
    write_json_atomic(PROGRESS_PATH, progress)
    write_reports(progress)


def validate_roots() -> None:
    missing = []
    if not SOURCE_ROOT.exists():
        missing.append(f"source folder missing: {SOURCE_ROOT}")
    if not DESIGN_HTML.exists():
        missing.append(f"design HTML missing: {DESIGN_HTML}")
    if not OUTPUT_ROOT.exists():
        missing.append(f"output folder missing: {OUTPUT_ROOT}")
    if missing:
        raise RuntimeError("; ".join(missing))


def process_pdf(progress: dict[str, Any], item: dict[str, Any]) -> None:
    rel = item["rel"]
    src = SOURCE_ROOT / rel
    out = OUTPUT_ROOT / rel
    item["status"] = "in_progress"
    item["updated_utc"] = utc_now()
    save_progress(progress)

    if not src.exists():
        item["status"] = "blocked"
        item["notes"].append("Source PDF missing.")
        log(f"BLOCKED source missing {rel}")
        save_progress(progress)
        return

    item["source_sha256"] = sha256(src)
    item["source_pages"] = page_count(src)

    if not out.exists():
        if item["classification"] == "official_government_form":
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, out)
            item["notes"].append("Official form copied unchanged because output was missing.")
        else:
            item["status"] = "pending"
            item["notes"].append("Output PDF missing; CI-created regeneration is required.")
            log(f"PENDING output missing {rel}")
            save_progress(progress)
            return

    try:
        item["output_sha256"] = sha256(out)
        item["output_pages"] = page_count(out)
    except Exception as exc:
        item["status"] = "blocked"
        item["notes"].append(f"Output PDF failed validation: {exc}")
        log(f"BLOCKED output validation failed {rel}: {exc}")
        save_progress(progress)
        return

    if item["classification"] == "official_government_form":
        if item["source_sha256"] != item["output_sha256"]:
            item["status"] = "blocked"
            item["qa"].append("FAIL: standalone official form hash differs from source.")
            progress["official_forms_altered"] = True
            progress["qa"]["official_form_hash_mismatches"].append(rel)
            log(f"BLOCKED official form hash mismatch {rel}")
            save_progress(progress)
            return
        item["qa"].append("PASS: standalone official form copied byte-identical to source.")
    else:
        item["qa"].append("PASS: output PDF opens and page count was recorded.")

    item["status"] = "completed"
    item["updated_utc"] = utc_now()
    log(f"COMPLETED {rel}")
    save_progress(progress)


def verify_mixed_appendices(progress: dict[str, Any]) -> None:
    verified = []
    failed = []
    for mixed_rel, official_rel in MIXED_APPENDIX_MAP.items():
        mixed = OUTPUT_ROOT / mixed_rel
        official = OUTPUT_ROOT / official_rel
        if not official.exists():
            official = SOURCE_ROOT / official_rel
        if not mixed.exists() or not official.exists():
            failed.append(
                {
                    "mixed_rel": mixed_rel,
                    "official_rel": official_rel,
                    "reason": "mixed output or official source missing",
                }
            )
            continue

        try:
            official_pages = page_count(official)
            mixed_pages = page_count(mixed)
            if mixed_pages < official_pages:
                failed.append(
                    {
                        "mixed_rel": mixed_rel,
                        "official_rel": official_rel,
                        "reason": "mixed output has fewer pages than official appendix",
                    }
                )
                continue
            for i in range(official_pages):
                official_digest = render_digest(official, i)
                mixed_digest = render_digest(mixed, mixed_pages - official_pages + i)
                if official_digest != mixed_digest:
                    failed.append(
                        {
                            "mixed_rel": mixed_rel,
                            "official_rel": official_rel,
                            "reason": f"render digest mismatch at appended official page {i + 1}",
                        }
                    )
                    break
            else:
                verified.append(
                    {
                        "mixed_rel": mixed_rel,
                        "official_rel": official_rel,
                        "official_pages": official_pages,
                    }
                )
        except Exception as exc:
            failed.append({"mixed_rel": mixed_rel, "official_rel": official_rel, "reason": str(exc)})

    progress["qa"]["mixed_appendix_verified"] = verified
    progress["qa"]["mixed_appendix_failed"] = failed
    if failed:
        progress["hard_stop_encountered"] = True
        for item in progress["files"]:
            if item["rel"] in {failure["mixed_rel"] for failure in failed}:
                item["status"] = "blocked"
                item["qa"].append("FAIL: mixed official appendix verification failed.")


def scan_pending_context_terms(progress: dict[str, Any]) -> None:
    found = []
    for rel in PENDING_CONTEXT_RELS:
        path = OUTPUT_ROOT / rel
        if not path.exists():
            continue
        try:
            text = extract_text(path)
        except Exception as exc:
            found.append({"rel": rel, "term": f"text extraction failed: {exc}"})
            continue
        for term in REMOVED_PENDING_TERMS:
            if term in text:
                found.append({"rel": rel, "term": term})
    progress["qa"]["pending_context_terms_found"] = found
    if found:
        for item in progress["files"]:
            if item["rel"] in {entry["rel"] for entry in found}:
                item["status"] = "blocked"
                item["qa"].append("FAIL: removed pending-context language remains.")


def scan_skipped_files(progress: dict[str, Any]) -> None:
    source_rels = set(source_pdf_rels())
    skipped = []
    for rel in output_pdf_rels():
        if rel not in source_rels and is_build_artifact(rel):
            skipped.append({"rel": rel, "reason": "leftover generated build artifact; not part of source packet"})
    progress["skipped_files"] = skipped


def run(args: argparse.Namespace) -> dict[str, Any]:
    validate_roots()
    progress = load_progress()
    existing_rels = {item["rel"] for item in progress["files"]}
    for rel in source_pdf_rels():
        if rel not in existing_rels:
            progress["files"].append(
                {
                    "rel": rel,
                    "classification": classify(rel),
                    "status": "pending",
                    "source_pages": None,
                    "output_pages": None,
                    "source_sha256": None,
                    "output_sha256": None,
                    "qa": [],
                    "notes": ["Added during resume inventory."],
                    "updated_utc": None,
                }
            )

    processed = 0
    for item in progress["files"]:
        if item["status"] == "completed" and not args.force_recheck:
            continue
        if item["status"] == "blocked" and not args.force_recheck:
            continue
        process_pdf(progress, item)
        processed += 1
        if args.batch_size and processed >= args.batch_size:
            break

    if args.verify_appendices:
        verify_mixed_appendices(progress)
    scan_pending_context_terms(progress)
    scan_skipped_files(progress)
    save_progress(progress)
    return progress


def main() -> int:
    parser = argparse.ArgumentParser(description="Resumable CI-ION PDF redesign checkpoint runner.")
    parser.add_argument("--batch-size", type=int, default=0, help="Maximum PDFs to process this run; 0 means all pending.")
    parser.add_argument("--force-recheck", action="store_true", help="Revalidate completed and blocked entries.")
    parser.add_argument("--verify-appendices", action="store_true", help="Render-compare mixed binder appendix form pages.")
    args = parser.parse_args()

    try:
        progress = run(args)
    except Exception as exc:
        log(f"ERROR {exc}")
        print(json.dumps({"error": str(exc)}, ensure_ascii=True))
        return 1

    summary = {
        "completed": progress["completed"],
        "pending": progress["pending"],
        "blocked": progress["blocked"],
        "skipped": progress["skipped"],
        "output_root": progress["output_root"],
        "next_file": progress["next_file"],
    }
    print(json.dumps(summary, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
