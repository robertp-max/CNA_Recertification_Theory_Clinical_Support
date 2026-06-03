"""Validate the one-phase CCCCO Modules 10-17 ContentV2 rebuild."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CV2 = ROOT / "CNA-Recert-Course" / "ContentV2"
CANON = CV2 / "data" / "courseContentV2.json"
AUDIT = CV2 / "qa" / "time-depth-audit.json"
EVIDENCE = CV2 / "survey-evidence" / "survey_evidence.json"
OBJECTIVES = CV2 / "survey-evidence" / "_source_text" / "cccco_objectives.json"

EXPECTED_MODULES = ["M00", "M10", "M11", "M12", "M13", "M14", "M15", "M16", "M17"]
REQUIRED_META = [
    "unique_learning_value",
    "source_reference",
    "source_module_number",
    "source_topic",
    "source_confidence",
    "transformation_type",
    "why_this_card_exists",
    "not_duplicate_of",
    "survey_evidence_status",
    "estimated_active_learning_minutes",
    "counts_toward_720_instructional_minutes",
    "time_model_status",
]
FORBIDDEN_REQUIRED = {"M01", "M02", "M03", "M04", "M05", "M06", "M07"}


def main() -> int:
    data = json.loads(CANON.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    objectives = json.loads(OBJECTIVES.read_text(encoding="utf-8"))
    failures: list[str] = []

    module_ids = [m["module_id"] for m in data["modules"]]
    if module_ids != EXPECTED_MODULES:
        failures.append(f"module order mismatch: {module_ids}")

    if data.get("time_model", {}).get("required_theory_instructional_minutes_total") != 720:
        failures.append("required theory total is not 720")

    allocation = data.get("time_model", {}).get("module_allocation", {})
    if sum(allocation.values()) != 720:
        failures.append(f"module allocation does not sum to 720: {allocation}")
    if set(allocation) & FORBIDDEN_REQUIRED:
        failures.append(f"old required module IDs remain in allocation: {sorted(set(allocation) & FORBIDDEN_REQUIRED)}")

    objective_total = sum(m["objective_count"] for m in objectives["modules"])
    if objective_total != 72:
        failures.append(f"parsed CCCCO objective count changed: {objective_total}")
    rows = evidence.get("rows", evidence if isinstance(evidence, list) else [])
    if len(rows) != 72:
        failures.append(f"survey evidence rows != 72: {len(rows)}")

    bad_statuses = [
        (r.get("cccco_module"), r.get("objective_n"), r.get("coverage_status"))
        for r in rows
        if r.get("coverage_status") not in {"Covered", "Assessed", "Deferred", "Out of Scope", "SME Review"}
    ]
    if bad_statuses:
        failures.append(f"unexpected coverage statuses: {bad_statuses[:10]}")

    for module in data["modules"]:
        mid = module["module_id"]
        if mid != "M00" and not mid.startswith("M1"):
            failures.append(f"non-CCCCO instructional module remains: {mid}")
        if mid != "M00" and "CCCCO Module" not in module["module_title"]:
            failures.append(f"learner-facing title does not use CCCCO Module naming: {mid}")
        for lesson in module.get("lessons", []):
            for card in lesson.get("cards", []):
                cid = f"{mid}/{lesson['lesson_id']}/{card.get('card_id')}"
                for key in REQUIRED_META:
                    if key not in card or card.get(key) in ("", None, []):
                        failures.append(f"{cid} missing {key}")
                if mid != "M00":
                    ref = card.get("source_reference", "")
                    if f"CCCCO Module {int(mid[1:])}" not in ref:
                        failures.append(f"{cid} source reference is not CCCCO module-specific: {ref}")
                    if card.get("source_module_number") != mid[1:]:
                        failures.append(f"{cid} source_module_number mismatch")
                learner_blob = "\n".join(str(card.get(k) or "") for k in ("display_title", "learner_facing_content", "narration_script", "transcript_text"))
                for bad in ("correct_id_internal", "rationale_internal", "Correct Answer:", "Rationale for instructor/internal use"):
                    if bad in learner_blob:
                        failures.append(f"{cid} leaks learner-facing scaffold/internal phrase: {bad}")
                if "clinical-hour credit" in learner_blob.lower() and not any(x in learner_blob.lower() for x in ("does not", "no clinical-hour", "not create")):
                    failures.append(f"{cid} may imply clinical-hour credit")

    if audit.get("required_theory_instructional_minutes_total") != 720:
        failures.append("time-depth audit required total is not 720")
    if audit.get("failing_lessons") != 0:
        failures.append(f"time-depth audit has failing lessons: {audit.get('failing_lessons')}")
    failing_modules = [m["module_id"] for m in audit.get("modules", []) if m.get("failing")]
    if failing_modules:
        failures.append(f"time-depth audit has failing modules: {failing_modules}")

    result = {
        "status": "OK" if not failures else "FAIL",
        "modules": module_ids,
        "required_theory_minutes": data.get("time_model", {}).get("required_theory_instructional_minutes_total"),
        "objective_rows": len(rows),
        "coverage_counts": evidence.get("status_counts"),
        "failing_lessons": audit.get("failing_lessons"),
        "failures": failures,
    }
    print(json.dumps(result, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
