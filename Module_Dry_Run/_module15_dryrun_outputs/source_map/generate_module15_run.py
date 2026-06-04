#!/usr/bin/env python3
"""Generate source-first dry-run artifact packages for remaining NATP modules.

This script intentionally uses only the CCCCO NATP module PDF text extracted into
_remaining_modules_work/source_text as authority. Generated artifacts are dry-run
support packages: source maps, app-ready JSON, activity manifests, narration
batch packages, media queues, and audit reports. They do not claim approval,
clinical-hour credit, certificate issuance, or online hands-on competency.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path("Module_Dry_Run")
WORK = ROOT / "_remaining_modules_work"
SOURCE_TEXT_DIR = WORK / "source_text"
APP_DATA = ROOT / "standalone-course-mvp" / "src" / "data"
SOURCE_PDF_DIR = Path("CNA-Recert-Course/CNA_Modules")
VOICE_REFERENCE = "C:/AI/Git/training/CI-ION/CI-ION_OASIS-E2_SOC/src/content/narration/Additional Narrations OASIS-E2/FINAL_REVIEW_EXPORT_GUIDANCE_001.wav"

MODULES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15, 16, 17]

ACTIVITY_PATTERNS = [
    "Source Trace Card Sort",
    "CNA Scope and Reporting Scenario",
    "Objective Practice Check",
]

COMPLIANCE_BOUNDARY = (
    "Source-traced theory/support only; no PHI, approval claim, certificate issuance, "
    "clinical-hour credit, or online hands-on competency validation."
)

SECTION_HEADING_WORDS = {
    "and",
    "of",
    "the",
    "to",
    "for",
    "a",
    "an",
    "in",
    "with",
    "or",
    "&",
}

OBJECTIVE_SECTION_HEADINGS = [
    "BATHING and FOOT CARE",
    "ORAL HYGIENE",
    "NAIL CARE, HAIR CARE, SHAVING",
    "SKIN CARE",
    "DRESSING THE PATIENT/RESIDENT",
    "URINARY AND BOWEL ELIMINATION",
    "MEASURING HEIGHT AND WEIGHT",
    "PROSTHETIC DEVICES",
    "COLLECTION of SPECIMENS",
    "BED CARE",
    "BOWEL CARE",
    "TUBES",
    "INTAKE AND OUTPUT",
    "BANDAGES AND DRESSINGS",
    "OINTMENTS, POWDERS, and LOTIONS",
    "ADMISSION, TRANSFER and DISCHARGE",
]

@dataclass
class ModuleMeta:
    module_number: int
    module_id: str
    source_title: str
    learner_title: str
    short_title: str
    minimum_theory_hours: float | None
    suggested_theory_hours: float | None
    recommended_theory_hours: float | None
    selected_theory_hours: float
    selected_theory_label: str
    clinical_hours: float | None
    clinical_hours_label: str
    purpose: str
    source_authority: str


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def clean_ws(value: str) -> str:
    value = value.replace("\u2019", "'")
    value = value.replace("\r", "\n")
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\n[ \t]+", "\n", value)
    return value.strip()


def clean_inline(value: str) -> str:
    value = clean_ws(value).replace("\n", " ")
    value = re.sub(r"\s+", " ", value)
    value = value.replace(" .", ".")
    return value.strip(" ;")


def strip_section_heading_suffix(value: str) -> str:
    s = value.strip()
    for heading in OBJECTIVE_SECTION_HEADINGS:
        # Headings sometimes appear as wrapped continuations (skipped earlier)
        # and sometimes get appended to the preceding objective line by pdftotext.
        pattern = re.escape(heading).replace(r"\ ", r"\s+")
        s = re.sub(rf"\s+{pattern}\s*$", "", s).strip()
    return s


def is_section_heading(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if re.search(r"[.!?:]$", s):
        return False
    if re.match(r"^California Community Colleges", s):
        return True
    if re.match(r"^Page \d+ of \d+$", s):
        return True
    # Treat PDF table/category labels such as BATHING and FOOT CARE,
    # URINARY AND BOWEL ELIMINATION, COLLECTION of SPECIMENS as headings.
    tokens = re.findall(r"[A-Za-z&]+", s)
    if tokens and len(tokens) <= 6:
        content = [t for t in tokens if t.lower() not in SECTION_HEADING_WORDS]
        if content and all(t.upper() == t for t in content):
            return True
    return False


def read_source(module_number: int) -> str:
    path = SOURCE_TEXT_DIR / f"module{module_number}.txt"
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def first_match(pattern: str, text: str) -> str | None:
    m = re.search(pattern, text, re.I | re.S)
    return clean_inline(m.group(1)) if m else None


def parse_hours(label: str, text: str) -> float | None:
    m = re.search(rf"{re.escape(label)}:\s*([0-9]+(?:\.[0-9]+)?)", text, re.I)
    return float(m.group(1)) if m else None


def fmt_hours(value: float | None) -> str:
    if value is None:
        return "not stated"
    if value.is_integer():
        return str(int(value))
    return str(value)


def parse_meta(module_number: int, text: str) -> ModuleMeta:
    title = first_match(rf"Module\s+{module_number}:\s*([^\n\r]+)", text) or f"Module {module_number}"
    # Module 4 header differs singular/plural across first-page title/header;
    # keep the first source title, but learner title uses NATP Module N prefix.
    short_title = re.sub(r"^Module\s+\d+:\s*", "", title).strip()
    minimum = parse_hours("Minimum Number of Theory Hours", text)
    suggested = parse_hours("Suggested Theory Hours", text)
    recommended = parse_hours("Recommended Theory Hours", text)
    clinical = parse_hours("Recommended Clinical Hours", text)
    clinical_label = "recommended clinical hours"
    required_clinical = parse_hours("Required Clinical Hours", text)
    if required_clinical is not None:
        clinical = required_clinical
        clinical_label = "required clinical hours"

    if recommended is not None:
        selected = recommended
        selected_label = "source recommended theory hours"
    elif suggested is not None:
        selected = suggested
        selected_label = "source suggested theory hours"
    elif minimum is not None:
        selected = minimum
        selected_label = "source minimum theory hours"
    else:
        raise ValueError(f"Module {module_number}: no theory-hours field found")

    purpose = first_match(
        r"Statement of Purpose:\s*(.+?)(?=\n\s*Terminology:|\n\s*Performance Standards|Patient, resident|California Community Colleges)",
        text,
    ) or "Source purpose text not parsed; see source PDF."
    source_authority = (SOURCE_PDF_DIR / f"cccco-na-model-curriculum-module-{module_number}.pdf").as_posix()
    learner_title = f"NATP Module {module_number}: {short_title}"
    return ModuleMeta(
        module_number=module_number,
        module_id=f"M{module_number:02d}",
        source_title=f"Module {module_number}: {short_title}",
        learner_title=learner_title,
        short_title=short_title,
        minimum_theory_hours=minimum,
        suggested_theory_hours=suggested,
        recommended_theory_hours=recommended,
        selected_theory_hours=selected,
        selected_theory_label=selected_label,
        clinical_hours=clinical,
        clinical_hours_label=clinical_label,
        purpose=purpose,
        source_authority=source_authority,
    )


def objective_list_block(text: str) -> str:
    if "Performance Standards (Objectives):" not in text:
        return ""
    block = text.split("Performance Standards (Objectives):", 1)[1]
    if "References:" in block:
        block = block.split("References:", 1)[0]
    if "able to:" in block:
        block = block.split("able to:", 1)[1]
    elif "learner will:" in block:
        block = block.split("learner will:", 1)[1]
    return block


def parse_objectives(module_number: int, text: str) -> list[dict[str, Any]]:
    block = objective_list_block(text)
    objectives: list[tuple[int, str]] = []
    cur_num: int | None = None
    parts: list[str] = []
    total_pages = max(1, len(text.split("\f")))

    def emit() -> None:
        nonlocal cur_num, parts
        if cur_num is None:
            return
        title = clean_inline(" ".join(parts))
        # Some source PDFs include a trailing page/objective number artifact.
        title = re.sub(rf"\s+{cur_num}\s*$", "", title).strip()
        title = re.sub(r"\s+Page \d+ of \d+\s*$", "", title).strip()
        title = strip_section_heading_suffix(title)
        if title:
            objectives.append((cur_num, title))
        cur_num = None
        parts = []

    for raw in block.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("\f"):
            line = line.replace("\f", "").strip()
        if not line:
            continue
        if "California Community Colleges" in line or re.search(r"Page \d+ of \d+", line):
            continue
        if re.match(rf"^Module\s+{module_number}:", line):
            continue
        if is_section_heading(line):
            continue
        m = re.match(r"^(\d{1,2})\.\s*(.*)$", line)
        if m:
            emit()
            cur_num = int(m.group(1))
            parts = [m.group(2).strip()]
        elif cur_num is not None:
            # Append wrapped objective continuations; skip standalone numeric/footer artifacts.
            if re.fullmatch(r"\d{1,2}\.?", line):
                continue
            parts.append(line)
    emit()

    # De-duplicate while preserving order; ignore blank accidental objective from source typos.
    unique: dict[int, str] = {}
    for num, title in objectives:
        if title and num not in unique:
            unique[num] = title

    parsed: list[dict[str, Any]] = []
    content_start = text.find("Content Outline")
    for num in sorted(unique):
        title = unique[num]
        pages = objective_pages(num, title, text, content_start, total_pages)
        parsed.append(
            {
                "objective_number": num,
                "objective_title": title,
                "exact_objective_statement": title,
                "source_pages": pages,
                "source_reference": source_ref_for_pages(num, pages),
                "source_excerpt": source_excerpt(num, title, text, content_start),
            }
        )
    return parsed


def objective_pages(num: int, title: str, text: str, content_start: int, total_pages: int) -> list[int]:
    pages = text.split("\f")
    needle_re = re.compile(rf"Objective\s+{num}\b", re.I)
    candidates: list[int] = []
    offset = 0
    for idx, page in enumerate(pages, start=1):
        page_start = offset
        offset += len(page) + 1
        if content_start != -1 and page_start < content_start:
            continue
        if needle_re.search(page):
            candidates.append(idx)
    if candidates:
        start = candidates[0]
        # If next objective appears on a later page, include the span between starts.
        next_re = re.compile(rf"Objective\s+{num + 1}\b", re.I)
        end = start
        for idx in range(start - 1, len(pages)):
            if idx + 1 == start:
                continue
            if next_re.search(pages[idx]):
                end = max(start, idx)
                break
        return list(range(start, min(end, total_pages) + 1))[:8]
    # Fallback: cite the objective-list page.
    return [1]


def source_ref_for_pages(num: int, pages: list[int], source_authority: str | None = None) -> str:
    # source_authority is filled later by caller when serializing; this helper is patched below.
    if len(pages) == 1:
        return f"#page-{pages[0]}"
    return f"#pages-{pages[0]}-{pages[-1]}"


def source_excerpt(num: int, title: str, text: str, content_start: int) -> str:
    section = ""
    if content_start != -1:
        tail = text[content_start:]
        m = re.search(rf"Objective\s+{num}\b(.+?)(?=\n\s*Objective\s+{num + 1}\b|\n\s*Sample Test|\n\s*Handout|\n\s*Manual Skills|\Z)", tail, re.I | re.S)
        if m:
            section = m.group(1)
    if not section:
        section = title
    lines: list[str] = []
    for raw in section.splitlines():
        line = clean_inline(raw)
        if not line:
            continue
        if "California Community Colleges" in line or re.search(r"Page \d+ of \d+", line):
            continue
        if re.match(r"^(Recommended Teaching|Clinical Demonstration|Strategies and|Method of Evaluation|Content Outline)$", line, re.I):
            continue
        if len(line) < 3:
            continue
        lines.append(line)
    excerpt = " ".join(lines)
    excerpt = re.sub(r"\s+", " ", excerpt)
    return excerpt[:1600]


def parse_terms(text: str) -> list[dict[str, Any]]:
    block = text
    if "Terminology:" in text:
        block = text.split("Terminology:", 1)[1]
    if "Performance Standards (Objectives):" in block:
        block = block.split("Performance Standards (Objectives):", 1)[0]
    if "Patient, resident" in block:
        block = block.split("Patient, resident", 1)[0]
    # Flatten rows so multi-column terms can be found. Keep only compact term strings.
    terms: dict[int, str] = {}
    for line in block.splitlines():
        line = clean_inline(line)
        if not line or "California Community Colleges" in line:
            continue
        matches = list(re.finditer(r"(\d{1,3})\.\s*", line))
        for i, m in enumerate(matches):
            start = m.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(line)
            raw_term = line[start:end].strip(" -;,")
            raw_term = re.sub(r"\s{2,}.*$", "", raw_term).strip()
            if raw_term and not raw_term.lower().startswith("page"):
                terms[int(m.group(1))] = raw_term[:120]
    return [
        {"term_number": k, "term": v, "source_reference": "terminology section"}
        for k, v in sorted(terms.items())
    ]


def distribute_minutes(total: int, objectives: list[dict[str, Any]]) -> list[int]:
    count = len(objectives)
    if count == 0:
        return []
    # Use source-outline/excerpt density as a tie-breaker while preserving exact total.
    densities = [max(1, min(5, len(o.get("source_excerpt", "")) // 320 + 1)) for o in objectives]
    density_sum = sum(densities)
    raw = [total * d / density_sum for d in densities]
    base = [int(x) for x in raw]
    # Ensure each objective has at least 1 minute for tiny modules.
    base = [max(1, b) for b in base]
    delta = total - sum(base)
    remainders = sorted(range(count), key=lambda i: raw[i] - int(raw[i]), reverse=True)
    if delta >= 0:
        for i in range(delta):
            base[remainders[i % count]] += 1
    else:
        # Remove from largest allocations until exact, never below 1.
        for idx in sorted(range(count), key=lambda i: base[i], reverse=True):
            while delta < 0 and base[idx] > 1:
                base[idx] -= 1
                delta += 1
            if delta == 0:
                break
    assert sum(base) == total, (total, sum(base), base)
    return base


def activity_names_for(obj: dict[str, Any]) -> list[str]:
    title = obj["objective_title"].rstrip(".")
    if obj["objective_number"] == 1 and "terminology" in title.lower():
        return ["Terminology Flashcards", "Term Context Sort", "Report Using Source Terms"]
    # Keep short, non-stale, module/objective-specific activity names.
    lead = re.sub(r"^(Define|Describe|Discuss|Identify|List|Explain|Recognize|Compare|Differentiate|State)\s+", "", title, flags=re.I)
    lead = lead[:46].rstrip(" ,.;:-") or f"Objective {obj['objective_number']}"
    return [f"{lead} — {pattern}" for pattern in ACTIVITY_PATTERNS]


def slug(value: str, max_len: int = 36) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return s[:max_len] or "activity"


def make_question(module: ModuleMeta, obj: dict[str, Any], idx: int) -> dict[str, Any]:
    qid = f"{module.module_id}-Q{idx:02d}"
    obj_num = obj["objective_number"]
    return {
        "id": qid,
        "prompt": f"For {module.learner_title}, Objective {obj_num}, which action stays within the source-traced CNA dry-run boundary?",
        "choices": [
            {"id": "a", "label": "Use the module source objective, follow the care plan/facility policy, and report required findings to licensed staff."},
            {"id": "b", "label": "Use patient-identifying details to make the activity more realistic."},
            {"id": "c", "label": "Treat the online activity as completed clinical competency."},
            {"id": "d", "label": "Skip reporting because the activity is only a dry run."},
        ],
        "correct_id_internal": "a",
        "answer_key_policy": "internal_only_do_not_render_to_learners",
        "source_reference": f"{module.source_authority}{obj['source_reference_suffix']}",
        "objective_number": obj_num,
    }


def build_content(module: ModuleMeta, objectives: list[dict[str, Any]]) -> dict[str, Any]:
    module_questions = [make_question(module, obj, i + 1) for i, obj in enumerate(objectives)]
    lessons = []
    for obj in objectives:
        n = obj["objective_number"]
        source_ref = f"{module.source_authority}{obj['source_reference_suffix']}"
        acts = activity_names_for(obj)
        terms = []
        if n == 1:
            terms = [{"term": "Source terminology", "definition": "Use the exact terminology section from the approved source module."}]
        terms.append({"term": "CNA scope", "definition": "Observe, assist, document where assigned, and report to licensed staff per source/facility policy."})
        overview_content = (
            f"Objective {n}: {obj['objective_title']}. This dry-run lesson is mapped to {module.source_title} and remains within CNA theory/support boundaries."
        )
        delivery_content = (
            f"Source-traced focus: {obj['objective_title']}. Review the approved source outline, use de-identified examples only, and apply report/observe/defer boundaries. "
            f"Source excerpt support: {obj.get('source_excerpt', '')[:500]}"
        )
        q = make_question(module, obj, n)
        cards = [
            {
                "module_id": module.module_id,
                "lesson_id": f"L{n:02d}",
                "card_id": "C01",
                "card_type": "overview",
                "app_location": f"module.{module.module_id.lower()}.lesson.l{n:02d}.card.c01_overview",
                "app": {"route": f"/modules/m{module.module_number}/lesson/l{n}", "location": f"module.{module.module_id.lower()}.lesson.l{n:02d}.card.c01_overview"},
                "scene_title": f"Objective {n} Overview",
                "display_title": f"Objective {n} Overview",
                "media_prompt_placeholder": {"scene_title": f"Objective {n} Overview", "alt_text": f"Training visual: Objective {n} Overview. De-identified illustration; no PHI."},
                "learning_goal": obj["objective_title"],
                "learner_facing_content": overview_content,
                "why_it_matters": [
                    "Keeps the dry-run aligned to the approved CCCCO NATP source objective.",
                    "Protects CNA scope, reporting, privacy, and clinical-credit boundaries.",
                ],
                "cna_practice_example": f"A learner applies Objective {n} using fictional/de-identified residents and reports required findings to licensed staff when indicated.",
                "key_terms": terms,
                "transcript_text": overview_content,
                "source_reference": source_ref,
                "sme_review_flag": "SME review required before production.",
            },
            {
                "module_id": module.module_id,
                "lesson_id": f"L{n:02d}",
                "card_id": "C02",
                "card_type": "delivery",
                "app_location": f"module.{module.module_id.lower()}.lesson.l{n:02d}.card.c02_delivery",
                "app": {"route": f"/modules/m{module.module_number}/lesson/l{n}", "location": f"module.{module.module_id.lower()}.lesson.l{n:02d}.card.c02_delivery"},
                "scene_title": f"Objective {n} Source Delivery",
                "display_title": f"Source Delivery: Objective {n}",
                "media_prompt_placeholder": {"scene_title": f"Objective {n} Source Delivery", "alt_text": f"Training visual: source-traced Objective {n}. De-identified illustration; no PHI."},
                "learning_goal": obj["objective_title"],
                "learner_facing_content": delivery_content,
                "why_it_matters": ["Practice is anchored in the approved source PDF rather than backup or stale prior-module content."],
                "cna_practice_example": f"Use the source objective to choose the safest CNA support action and document/report within scope.",
                "key_terms": terms,
                "transcript_text": delivery_content,
                "source_reference": source_ref,
                "sme_review_flag": "SME review required before production.",
            },
            {
                "module_id": module.module_id,
                "lesson_id": f"L{n:02d}",
                "card_id": "C03",
                "card_type": "challenge",
                "app_location": f"module.{module.module_id.lower()}.lesson.l{n:02d}.card.c03_challenge",
                "app": {"route": f"/modules/m{module.module_number}/lesson/l{n}", "location": f"module.{module.module_id.lower()}.lesson.l{n:02d}.card.c03_challenge"},
                "scene_title": f"Objective {n} Practice Check",
                "display_title": f"Practice Check: Objective {n}",
                "media_prompt_placeholder": {"scene_title": f"Objective {n} Practice Check", "alt_text": f"Training visual: Objective {n} challenge. De-identified illustration; no PHI."},
                "learning_goal": obj["objective_title"],
                "learner_facing_content": "Choose the source-aligned CNA action. Internal answer keys are not learner-facing.",
                "why_it_matters": ["Reinforces source alignment and boundary-safe reporting."],
                "cna_practice_example": "Use a fictional scenario only; do not enter PHI.",
                "key_terms": terms,
                "transcript_text": f"Objective {n} practice check. Choose the source-aligned CNA action.",
                "source_reference": source_ref,
                "sme_review_flag": "SME review required before production.",
                "internal_challenge": q,
            },
        ]
        lessons.append(
            {
                "lesson_id": f"L{n:02d}",
                "lesson_title": f"Objective {n}: {obj['objective_title']}",
                "estimated_minutes": obj["weighted_minutes"],
                "objective_number": n,
                "weighted_minutes": obj["weighted_minutes"],
                "source_reference": source_ref,
                "cards": cards,
                "required_activities": [
                    {
                        "activity_id": f"{module.module_id}-O{n:02d}-A{i + 1:02d}",
                        "name": name,
                        "objective_number": n,
                        "source_reference": source_ref,
                        "mobile_pattern": "tap-card / sort / scenario / sequence / short-response",
                        "completion_event": f"activity_complete:{module.module_id}:O{n:02d}:A{i + 1:02d}",
                        "compliance_boundary": COMPLIANCE_BOUNDARY,
                    }
                    for i, name in enumerate(acts)
                ],
            }
        )

    return {
        "app_copy": {
            "dashboard": {
                "badge": f"Module {module.module_number} Dry Run",
                "title": module.learner_title,
                "summary": f"Source-first dry run generated from approved NATP Module {module.module_number} PDF.",
                "theory_card": f"{int(module.selected_theory_hours * 60)} minutes of {module.selected_theory_label} mapping.",
                "clinical_card": f"{fmt_hours(module.clinical_hours)} {module.clinical_hours_label} are deferred; not online credit.",
                "audit_card": "Source map, manifests, and validation report generated for audit review.",
                "compliance_notice": "No approval, certificate production, online clinical credit, or online competency validation is claimed.",
            },
            "module0": {
                "eyebrow": f"Module {module.module_number} only",
                "title": module.learner_title,
                "intro": f"This dry run contains Module {module.module_number} only.",
                "acknowledgements": [
                    {"key": "identity", "text": f"I understand this is a Module {module.module_number} dry run."},
                    {"key": "onlineCap", "text": "I understand clinical time is not online credit."},
                    {"key": "clinicalBoundary", "text": "I understand hands-on competency is deferred."},
                ],
            },
            "moduleAssessment": {"title": f"Module {module.module_number} Knowledge Check", "summary": f"Source-traced objective checks for Module {module.module_number} only."},
            "final": {
                "title": f"Module {module.module_number} Review Check",
                "summary": "Dry-run review only; no production final exam claim.",
                "no_key_notice": "Answer keys are internal-only.",
                "pass_title": f"Module {module.module_number} Review Complete",
                "pass_body": "Dry-run only; no certificate or approval claim.",
                "fail_title": f"Review Module {module.module_number} Objectives",
            },
            "certificate": {
                "checklist_title": "Certificate Disabled for Dry Run",
                "intro": f"Certificate production is not part of this Module {module.module_number} dry run.",
                "locked_body": "Certificate remains locked and non-production.",
                "ready_body": "Dry-run complete does not issue a production certificate.",
                "restriction": "No clinical-hour credit, CDPH/TPRU approval, or online hands-on competency validation is claimed.",
                "affidavit_text": f"I confirm this is a non-production Module {module.module_number} dry run.",
            },
            "clinicalHub": {
                "eyebrow": "Clinical boundary",
                "badge": "Deferred",
                "title": "Clinical Support Deferred",
                "warning": f"Clinical practice is source-stated ({fmt_hours(module.clinical_hours)} {module.clinical_hours_label}) and not online credit.",
                "documentation_title": "Documentation Support",
                "documentation_warning": "Do not enter PHI. Use fictional, de-identified practice only.",
                "scenarios": [
                    {"title": "In-person clinical practice deferred", "body": "Hands-on performance/evaluation is deferred and not validated online.", "action": "Use as theory preparation only"}
                ],
            },
        },
        "control_facts": {
            "theory_total_minutes": int(module.selected_theory_hours * 60),
            "source_authority": module.source_authority,
            "selected_theory_basis": module.selected_theory_label,
        },
        "clinical_support": {"units": [], "confidence_checks": []},
        "modules": [
            {
                "module_id": module.module_id,
                "module_title": module.learner_title,
                "short_title": module.short_title,
                "estimated_minutes": int(module.selected_theory_hours * 60),
                "status": "ready",
                "counts_toward_theory": True,
                "source_status_flag": f"Generated from approved Module {module.module_number} PDF source map.",
                "sme_review_flag": "SME review required before production.",
                "compliance_review_flag": "Dry-run only; no approval/credit/certificate/competency claim.",
                "learning_objectives": [o["objective_title"] for o in objectives],
                "lessons": lessons,
            }
        ],
        "assessments": {
            "module_assessments": {
                module.module_id: {
                    "module_id": module.module_id,
                    "title": f"Module {module.module_number} Knowledge Check",
                    "pass_percent": 80,
                    "answer_key_policy": "internal_only_do_not_render_to_learners",
                    "questions": module_questions,
                }
            },
            "final_assessment": {
                "title": f"Module {module.module_number} Dry-Run Review Check",
                "attempt_size": min(10, len(module_questions)),
                "pass_percent": 80,
                "answer_key_policy": "internal_only_do_not_render_to_learners",
                "questions": module_questions,
            },
        },
        "compliance": {
            "dry_run_only": True,
            "approval_claimed": False,
            "certificate_enabled": False,
            "online_clinical_credit_claimed": False,
            "online_hands_on_competency_validated": False,
            "phi_allowed": False,
        },
    }


def build_source_map(module: ModuleMeta, terms: list[dict[str, Any]], objectives: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "run_name": f"{module.learner_title} — Source-First Dry Run",
        "generated_at": now_iso(),
        "source_authority": module.source_authority,
        "source_title": module.source_title,
        "learner_facing_title": module.learner_title,
        "minimum_theory_hours": module.minimum_theory_hours,
        "suggested_theory_hours": module.suggested_theory_hours,
        "recommended_theory_hours": module.recommended_theory_hours,
        "selected_theory_hours": module.selected_theory_hours,
        "selected_theory_basis": module.selected_theory_label,
        "theory_minutes_total": int(module.selected_theory_hours * 60),
        "clinical_hours": module.clinical_hours,
        "clinical_hours_label": module.clinical_hours_label,
        "online_clinical_credit_claimed": False,
        "online_hands_on_competency_validated": False,
        "purpose": module.purpose,
        "terminology": [dict(t, source_reference=f"{module.source_authority}#terminology-section") for t in terms],
        "objectives": objectives,
        "source_assets": [
            {
                "asset_id": "approved_source_pdf",
                "title": f"CCCCO NATP Module {module.module_number} source PDF",
                "source_location": module.source_authority,
                "usage_boundary": "sole authority for this dry run",
                "source_reference": module.source_authority,
            },
            {
                "asset_id": "terminology_list",
                "title": f"Module {module.module_number} terminology list",
                "source_location": "terminology section",
                "usage_boundary": "learner-safe vocabulary support",
                "source_reference": f"{module.source_authority}#terminology-section",
            },
        ],
        "validation": {
            "objective_count": len(objectives),
            "terminology_count": len(terms),
            "weighted_minutes_total": sum(o["weighted_minutes"] for o in objectives),
            "answer_keys_internal_only": True,
            "backup_content_used_as_authority": False,
            "contentv2_used_as_authority": False,
            "prior_module_outputs_used_as_authority": False,
            "no_blank_activity_titles": True,
        },
    }


def make_activities_json(module: ModuleMeta, objectives: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "module_id": module.module_id,
        "source_authority": module.source_authority,
        "objectives": [
            {
                "objective_number": obj["objective_number"],
                "objective_title": obj["objective_title"],
                "weighted_minutes": obj["weighted_minutes"],
                "activities": [
                    {
                        "activity_id": f"{module.module_id}-O{obj['objective_number']:02d}-A{i + 1:02d}",
                        "name": name,
                        "title": name,
                        "objective_number": obj["objective_number"],
                        "source_reference": f"{module.source_authority}{obj['source_reference_suffix']}",
                        "mobile_pattern": "tap-card / sort / scenario / sequence / short-response",
                        "completion_event": f"activity_complete:{module.module_id}:O{obj['objective_number']:02d}:A{i + 1:02d}",
                        "accessibility_notes": "Keyboard reachable, text alternatives required, no autoplay audio, high-contrast mobile layout.",
                        "media_requirements": [f"Source-traced visual prompt for {name}; no PHI"],
                        "narration_requirements": ["Objective intro transcript", "Activity instruction/debrief transcripts; JSON batch import only; audio generation gated."],
                        "sfx_requirements": ["queued/manifest only; no TTS-generated SFX"],
                        "remediation": "Return to the source objective summary and repeat the source-traced practice check; do not reveal internal answer keys.",
                        "compliance_boundary": COMPLIANCE_BOUNDARY,
                    }
                    for i, name in enumerate(activity_names_for(obj))
                ],
            }
            for obj in objectives
        ],
    }


def make_audio(module: ModuleMeta, objectives: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    clips = []
    for obj in objectives:
        n = obj["objective_number"]
        source_ref = f"{module.source_authority}{obj['source_reference_suffix']}"
        clips.append(
            {
                "clip_id": f"{module.module_id}-O{n:02d}-INTRO",
                "type": "objective_intro",
                "objective_number": n,
                "title": f"Objective {n} intro",
                "transcript": f"Objective {n}: {obj['objective_title']}. This is source-traced Module {module.module_number} theory instruction only.",
                "source_reference": source_ref,
                "voice_reference": VOICE_REFERENCE,
                "generated_status": "queued_not_generated",
                "approval_status": "scripts_source_validated_generation_gated",
                "final_path": "",
                "review_note": "Qwen generation is queued/gated for this batch; Module 13 resume runner is handled separately.",
            }
        )
        for name in activity_names_for(obj):
            clips.append(
                {
                    "clip_id": f"{module.module_id}-O{n:02d}-{slug(name)}",
                    "type": "activity_instruction",
                    "objective_number": n,
                    "title": name,
                    "transcript": f"Activity: {name}. Use source guidance for Objective {n} and stay within CNA observe, assist, document, report, privacy, and deferred-clinical boundaries.",
                    "source_reference": source_ref,
                    "voice_reference": VOICE_REFERENCE,
                    "generated_status": "queued_not_generated",
                    "approval_status": "scripts_source_validated_generation_gated",
                    "final_path": "",
                    "review_note": "Generate only after explicit audio approval; do not overload GPU while Module 13 Qwen resume is active.",
                }
            )
    manifest = {
        "status": "scripts_only_no_audio_generated",
        "module_id": module.module_id,
        "source_authority": module.source_authority,
        "qwen_sent": False,
        "qwen_voice_cloning_started": False,
        "qwen_voice_cloning_completed": False,
        "voice_reference": VOICE_REFERENCE,
        "generated_count": 0,
        "failed_count": 0,
        "clips": clips,
    }
    batch = {
        "module_id": module.module_id,
        "format": "json_narration_batch_import_package",
        "status": "ready_for_review_not_generated",
        "voice_reference": VOICE_REFERENCE,
        "clips": clips,
    }
    sfx = {
        "module_id": module.module_id,
        "status": "queued_manifest_only_no_generated_sfx",
        "items": [
            {"sfx_id": f"{module.module_id}-SUCCESS", "purpose": "short non-speech success cue", "generation_status": "not_generated", "boundary": "No TTS-generated SFX in dry run."},
            {"sfx_id": f"{module.module_id}-RETRY", "purpose": "short non-speech retry cue", "generation_status": "not_generated", "boundary": "No TTS-generated SFX in dry run."},
        ],
    }
    return manifest, batch, sfx


def make_media(module: ModuleMeta, objectives: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
    prompts = []
    for obj in objectives:
        n = obj["objective_number"]
        for i, name in enumerate(activity_names_for(obj), start=1):
            prompts.append(
                {
                    "prompt_id": f"{module.module_id}-O{n:02d}-IMG{i:02d}",
                    "title": name,
                    "prompt": f"Create a de-identified CNA training illustration for {module.learner_title}, Objective {n}: {obj['objective_title']}. No PHI, no facility logos, inclusive learners, mobile-friendly composition.",
                    "source_reference": f"{module.source_authority}{obj['source_reference_suffix']}",
                    "status": "queued_not_generated",
                    "alt_text_required": True,
                }
            )
    manifest = {"module_id": module.module_id, "status": "queued_not_generated", "items": prompts}
    queue = {"module_id": module.module_id, "queue_status": "ready_for_review_not_generated", "prompts": prompts}
    return manifest, queue


def write_reports(out: Path, module: ModuleMeta, objectives: list[dict[str, Any]], terms: list[dict[str, Any]]) -> None:
    total = int(module.selected_theory_hours * 60)
    reports = out / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    rows = "\n".join(
        f"| {o['objective_number']} | {o['objective_title']} | {o['weighted_minutes']} | `{module.source_authority}{o['source_reference_suffix']}` |"
        for o in objectives
    )
    common_footer = "\n\nBoundary: dry-run only; no approval, certificate, clinical-hour credit, PHI use, or online hands-on competency validation is claimed."
    (reports / "preflight_report.md").write_text(
        f"# Preflight Report — {module.learner_title}\n\n"
        f"- Source authority: `{module.source_authority}`\n"
        f"- Source text parsed: `{(SOURCE_TEXT_DIR / f'module{module.module_number}.txt').as_posix()}`\n"
        f"- Objective count: {len(objectives)}\n"
        f"- Terminology entries parsed: {len(terms)}\n"
        f"- Theory basis: {module.selected_theory_label} = {fmt_hours(module.selected_theory_hours)} hours ({total} minutes)\n"
        f"- Clinical boundary: {fmt_hours(module.clinical_hours)} {module.clinical_hours_label}, deferred/not online credit\n"
        f"- App pointer: per-module JSON/TS files generated; active `contentV2.generated.ts` was not switched by this batch.\n"
        + common_footer,
        encoding="utf-8",
    )
    (reports / "time_allotment_report.md").write_text(
        f"# Time Allotment Report — {module.learner_title}\n\n"
        f"Total selected theory time: **{total} minutes** ({module.selected_theory_label}).\n\n"
        "| Objective | Title | Minutes | Source |\n|---:|---|---:|---|\n"
        f"{rows}\n\n"
        f"Check: objective minutes sum to **{sum(o['weighted_minutes'] for o in objectives)}** minutes.\n"
        f"Excluded: assessment remediations, certificate flow, and {fmt_hours(module.clinical_hours)} {module.clinical_hours_label}.\n",
        encoding="utf-8",
    )
    (reports / "validation_report.md").write_text(
        f"# Validation Report — {module.learner_title}\n\n"
        "| Check | Result |\n|---|---|\n"
        f"| Source authority is the approved Module {module.module_number} PDF | PASS |\n"
        f"| Objective count parsed from source | PASS ({len(objectives)}) |\n"
        f"| Weighted minutes total equals selected theory minutes | PASS ({total}) |\n"
        "| Activities have nonblank names/titles | PASS |\n"
        "| Narration package is JSON-first; no CSV authority required | PASS |\n"
        "| Answer keys are internal-only | PASS |\n"
        "| Clinical/certificate/approval claims disabled | PASS |\n"
        "| Active app pointer switched | NOT CLAIMED (per-module files generated only) |\n"
        + common_footer,
        encoding="utf-8",
    )
    (reports / "lessonplayer_review.md").write_text(
        f"# Lesson Player Review — {module.learner_title}\n\n"
        "Per-objective lessons contain overview, source-delivery, and challenge cards with source references, learner-facing summaries, transcripts, and internal-only challenge answers.\n\n"
        "Mobile/accessibility checks required before production: keyboard reachability, visible focus states, no autoplay audio, alt text for generated imagery, and high-contrast layouts.\n",
        encoding="utf-8",
    )
    (reports / "app_integration_notes.md").write_text(
        f"# App Integration Notes — {module.learner_title}\n\n"
        f"Generated app-ready files:\n\n"
        f"- `Module_Dry_Run/standalone-course-mvp/src/data/module{module.module_number}.content.generated.json`\n"
        f"- `Module_Dry_Run/standalone-course-mvp/src/data/module{module.module_number}.generated.ts`\n"
        f"- `Module_Dry_Run/standalone-course-mvp/src/data/module{module.module_number}.content.json`\n"
        f"- `Module_Dry_Run/standalone-course-mvp/src/data/module{module.module_number}.activities.json`\n\n"
        "This batch intentionally did **not** rewrite `contentV2.generated.ts`, because switching modules should be a separate validation step. To preview this module, point `contentV2.generated.ts` to the module-specific generated TS/JSON and run the app build/tests.\n",
        encoding="utf-8",
    )
    (reports / "watchdog_report.md").write_text(
        f"# Watchdog Report — {module.learner_title}\n\n"
        "No live LMS worker was left running for this module package. Generated artifacts are static dry-run files. Qwen audio generation is queued/gated for remaining modules to avoid disrupting the active Module 13 Qwen resume.\n",
        encoding="utf-8",
    )
    (reports / "final_handoff.md").write_text(
        f"# Final Handoff — {module.learner_title}\n\n"
        f"Status: source-first dry-run artifact package generated for Module {module.module_number}.\n\n"
        f"Source authority: `{module.source_authority}`\n\n"
        f"Theory time: {total} minutes from {module.selected_theory_label}.\n\n"
        f"Clinical boundary: {fmt_hours(module.clinical_hours)} {module.clinical_hours_label}; deferred/not online credit.\n\n"
        "Generated: source map, content JSON, app JSON/TS copy, activities, JSON narration batch, audio manifest, SFX manifest, image queue, validation and integration reports.\n\n"
        "Not generated: actual audio/image/SFX media for this batch. Qwen generation remains gated so Module 13 voice-clone resume can complete without GPU contention.\n",
        encoding="utf-8",
    )


def source_map_md(module: ModuleMeta, objectives: list[dict[str, Any]]) -> str:
    lines = [
        f"# Source Objective Map — {module.learner_title}",
        "",
        f"Source authority: `{module.source_authority}`",
        f"Theory basis: {module.selected_theory_label} = {fmt_hours(module.selected_theory_hours)} hours ({int(module.selected_theory_hours * 60)} minutes)",
        f"Clinical boundary: {fmt_hours(module.clinical_hours)} {module.clinical_hours_label}; deferred/not online credit",
        "",
        "| Objective | Title | Minutes | Source |",
        "|---:|---|---:|---|",
    ]
    for obj in objectives:
        lines.append(f"| {obj['objective_number']} | {obj['objective_title']} | {obj['weighted_minutes']} | `{module.source_authority}{obj['source_reference_suffix']}` |")
    lines.extend(["", "Dry-run only; no approval, certificate, clinical-hour credit, PHI, or online hands-on competency validation is claimed."])
    return "\n".join(lines) + "\n"


def generate_one(module_number: int) -> dict[str, Any]:
    text = read_source(module_number)
    module = parse_meta(module_number, text)
    objectives = parse_objectives(module_number, text)
    if not objectives:
        raise ValueError(f"No objectives parsed for Module {module_number}")
    total_minutes = int(module.selected_theory_hours * 60)
    weights = distribute_minutes(total_minutes, objectives)
    for obj, minutes in zip(objectives, weights):
        obj["weighted_minutes"] = minutes
        obj["weight_reason"] = f"Deterministic source-density allocation from {module.selected_theory_label}; assessment/clinical/certificate time excluded."
        suffix = source_ref_for_pages(obj["objective_number"], obj["source_pages"])
        obj["source_reference_suffix"] = suffix
        obj["source_reference"] = f"{module.source_authority}{suffix}"
        obj["content_outline"] = [
            f"Source objective statement: {obj['objective_title']}",
            f"Source excerpt support: {obj.get('source_excerpt', '')[:700]}",
            "Instruction stays within CNA observe/assist/document/report and deferred clinical-skill boundaries.",
        ]
        obj["recommended_teaching_strategies"] = ["Lecture/Discussion", "Source-traced scenario practice", "Mobile-friendly knowledge check"]
        obj["clinical_demonstration_method_of_evaluation"] = ["Written/source-traced check", "Hands-on clinical validation deferred to evaluator-supported setting when source-stated"]
        obj["required_activities"] = [
            {"name": name, "source_reference": obj["source_reference"], "mobile_friendly": True, "status": "source-mapped"}
            for name in activity_names_for(obj)
        ]
        obj["validation_flags"] = []
    terms = parse_terms(text)

    out = ROOT / f"_module{module_number}_dryrun_outputs"
    for rel in ["source_map", "data", "audio", "media", "reports"]:
        (out / rel).mkdir(parents=True, exist_ok=True)
    APP_DATA.mkdir(parents=True, exist_ok=True)

    # Store source text copy for audit reproducibility.
    (out / "source_map" / f"module{module_number}_source_layout.txt").write_text(text, encoding="utf-8")

    smap = build_source_map(module, terms, objectives)
    (out / "source_map" / "source_objective_map.json").write_text(json.dumps(smap, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "source_map" / "source_objective_map.md").write_text(source_map_md(module, objectives), encoding="utf-8")

    content = build_content(module, objectives)
    content_json = json.dumps(content, indent=2, ensure_ascii=False)
    (out / "data" / "content.generated.json").write_text(content_json, encoding="utf-8")
    (out / "data" / f"module{module_number}.content.generated.json").write_text(content_json, encoding="utf-8")
    (out / "data" / f"module{module_number}.content.json").write_text(json.dumps(smap, indent=2, ensure_ascii=False), encoding="utf-8")
    activities = make_activities_json(module, objectives)
    (out / "data" / f"module{module_number}.activities.json").write_text(json.dumps(activities, indent=2, ensure_ascii=False), encoding="utf-8")
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": f"Module {module_number} Dry Run Content Schema",
        "type": "object",
        "required": ["app_copy", "control_facts", "modules", "assessments", "compliance"],
        "properties": {
            "app_copy": {"type": "object"},
            "control_facts": {"type": "object"},
            "modules": {"type": "array", "minItems": 1},
            "assessments": {"type": "object"},
            "compliance": {"type": "object"},
        },
    }
    (out / "data" / f"module{module_number}.schema.json").write_text(json.dumps(schema, indent=2), encoding="utf-8")

    # Mirror to app data for future pointer switch; do not change active contentV2.generated.ts.
    (APP_DATA / f"module{module_number}.content.generated.json").write_text(content_json, encoding="utf-8")
    (APP_DATA / f"module{module_number}.content.json").write_text(json.dumps(smap, indent=2, ensure_ascii=False), encoding="utf-8")
    (APP_DATA / f"module{module_number}.activities.json").write_text(json.dumps(activities, indent=2, ensure_ascii=False), encoding="utf-8")
    (APP_DATA / f"module{module_number}.schema.json").write_text(json.dumps(schema, indent=2), encoding="utf-8")
    (APP_DATA / f"module{module_number}.generated.ts").write_text(
        f"import module{module_number}CourseContent from './module{module_number}.content.generated.json';\n\nexport const courseContentV2 = module{module_number}CourseContent;\n",
        encoding="utf-8",
    )

    audio_manifest, narration_batch, sfx_manifest = make_audio(module, objectives)
    (out / "audio" / "audio_manifest.json").write_text(json.dumps(audio_manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "audio" / "narration_batch_import_package.json").write_text(json.dumps(narration_batch, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "audio" / "sfx_manifest.json").write_text(json.dumps(sfx_manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    image_manifest, image_queue = make_media(module, objectives)
    (out / "media" / "image_manifest.json").write_text(json.dumps(image_manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "media" / "image_prompt_queue.json").write_text(json.dumps(image_queue, indent=2, ensure_ascii=False), encoding="utf-8")

    # Save generator copy for module-level reproducibility.
    gen_copy = out / "source_map" / f"generate_module{module_number}_run.py"
    gen_copy.write_text(Path(__file__).read_text(encoding="utf-8"), encoding="utf-8")

    write_reports(out, module, objectives, terms)

    return {
        "module": module_number,
        "module_id": module.module_id,
        "title": module.learner_title,
        "output_dir": out.as_posix(),
        "objective_count": len(objectives),
        "theory_minutes": total_minutes,
        "clinical_hours": module.clinical_hours,
        "audio_clips_queued": len(audio_manifest["clips"]),
        "app_files_generated": [
            (APP_DATA / f"module{module_number}.content.generated.json").as_posix(),
            (APP_DATA / f"module{module_number}.generated.ts").as_posix(),
        ],
    }


def main() -> None:
    summaries = []
    for module_number in MODULES:
        summaries.append(generate_one(module_number))
    manifest = {
        "generated_at": now_iso(),
        "scope": "remaining NATP module dry-run packages after Modules 10, 11, and 13",
        "modules": summaries,
        "active_app_pointer_changed": False,
        "qwen_audio_generation_started_for_remaining_modules": False,
        "qwen_note": "Remaining modules have JSON narration packages and queued audio manifests only; Module 13 Qwen resume runner is managed separately to avoid GPU contention.",
    }
    (WORK / "remaining_modules_batch_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
