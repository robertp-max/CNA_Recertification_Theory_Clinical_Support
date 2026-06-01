"""apply_time_model.py

Add explicit, defensible time-model fields to the canonical ContentV2 JSON.

SOURCE OF TRUTH for the required theory allocation is ContentV1:
    CNA-Recert-Course/Content/02_THEORY_SYLLABUS_TABLE.md

The 720-minute total is NOT recomputed from narration length or card count. It is
inherited from the syllabus module allocation. Narration / reading / interaction /
assessment minutes are tracked SEPARATELY (descriptive component estimates) and never
replace the authoritative instructional allocation. Optional Clinical Support and all
assessment time are excluded from the 720 instructional total.

Idempotent: safe to re-run. Edits ONLY the canonical JSON; rerun the generator after.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CANON = ROOT / "CNA-Recert-Course" / "ContentV2" / "data" / "courseContentV2.json"

SYLLABUS_BASIS = "CNA-Recert-Course/Content/02_THEORY_SYLLABUS_TABLE.md (required theory allocation)"

# Authoritative ContentV1 syllabus allocation (minutes). Sums to 720.
MODULE_ALLOCATION = {
    "M00": 30, "M01": 90, "M02": 120, "M03": 120,
    "M04": 120, "M05": 120, "M06": 90, "M07": 30,
}

# Descriptive pacing constants (documented, not used to derive the 720 total).
REVIEW_READING_WPM = 140          # silent comprehension/review reading pace
CHALLENGE_INTERACTION_MIN = 1.5   # per challenge card
DEBRIEF_REMEDIATION_MIN = 2.0     # per debrief/remediation card


def words(text: str) -> int:
    return len([w for w in re.split(r"\s+", text or "") if w])


def r1(x: float) -> float:
    return round(x, 1)


def r2(x: float) -> float:
    return round(x, 2)


def card_component_minutes(card: dict) -> tuple[float, float, float]:
    """Returns (narration_min, reading_min, interaction_min) for a card."""
    narration = (card.get("estimated_narration_seconds") or 0) / 60.0
    reading = words(card.get("learner_facing_content") or card.get("transcript_text") or "") / REVIEW_READING_WPM
    ctype = card.get("card_type")
    interaction = 0.0
    if ctype == "challenge":
        interaction = CHALLENGE_INTERACTION_MIN
    elif ctype in ("debrief", "remediation"):
        interaction = DEBRIEF_REMEDIATION_MIN
    return narration, reading, interaction


def apply_card_time(card: dict, counts_720: bool, gate: bool, status: str) -> tuple[float, float, float]:
    n, rd, it = card_component_minutes(card)
    card["estimated_narration_minutes"] = r2(n)
    card["estimated_reading_minutes"] = r2(rd)
    card["estimated_interaction_minutes"] = r2(it)
    card["estimated_active_learning_minutes"] = r2(n + rd + it)
    card["counts_toward_720_instructional_minutes"] = bool(counts_720)
    card["counts_toward_certificate_gate"] = bool(gate)
    card["counts_toward_optional_clinical_support"] = False
    card["time_model_status"] = status
    return n, rd, it


def main() -> int:
    data = json.loads(CANON.read_text(encoding="utf-8"))

    # ---- Modules / lessons / cards -------------------------------------------------
    required_total = 0
    for module in data["modules"]:
        mid = module["module_id"]
        alloc = MODULE_ALLOCATION.get(mid, module.get("estimated_minutes", 0))
        counts_720 = mid in MODULE_ALLOCATION            # all required theory modules M00-M07
        gate = True                                       # all required theory gates the certificate
        is_repair = (module.get("status") == "source-repair")

        mod_narr = mod_read = mod_int = 0.0
        lesson_allocated = 0
        for lesson in module.get("lessons", []):
            l_narr = l_read = l_int = 0.0
            for card in lesson.get("cards", []):
                c_status = "source-repair" if "source repair" in (
                    (card.get("display_title", "") + card.get("learner_facing_content", "")).lower()
                ) else "modeled"
                n, rd, it = apply_card_time(card, counts_720, gate, c_status)
                l_narr += n; l_read += rd; l_int += it
            lesson_min = lesson.get("estimated_minutes", 0) or 0
            lesson_allocated += lesson_min
            lesson["instructional_minutes"] = lesson_min
            lesson["estimated_narration_minutes"] = r1(l_narr)
            lesson["estimated_reading_minutes"] = r1(l_read)
            lesson["estimated_interaction_minutes"] = r1(l_int)
            lesson["estimated_active_learning_minutes"] = r1(l_narr + l_read + l_int)
            lesson["estimated_assessment_minutes"] = 0
            lesson["assessment_minutes_excluded_from_instructional_total"] = True
            lesson["counts_toward_720_instructional_minutes"] = counts_720
            lesson["counts_toward_certificate_gate"] = gate
            lesson["counts_toward_optional_clinical_support"] = False
            lesson["source_time_basis"] = SYLLABUS_BASIS
            lesson["time_model_status"] = "source-repair" if is_repair else "modeled"
            lesson["time_model_notes"] = (
                f"Lesson allocation {lesson_min} min (ContentV1). Narration {r1(l_narr)} min, reading {r1(l_read)} min, "
                f"interaction {r1(l_int)} min are descriptive components tracked separately; narration is NOT the full lesson time."
            )
            mod_narr += l_narr; mod_read += l_read; mod_int += l_int

        ma = data.get("assessments", {}).get("module_assessments", {}).get(mid, {})
        mod_assessment_min = ma.get("estimated_minutes", 0) or 0
        gap = alloc - lesson_allocated

        module["instructional_minutes"] = alloc
        module["estimated_active_learning_minutes"] = r1(mod_narr + mod_read + mod_int)
        module["estimated_narration_minutes"] = r1(mod_narr)
        module["estimated_reading_minutes"] = r1(mod_read)
        module["estimated_interaction_minutes"] = r1(mod_int)
        module["estimated_assessment_minutes"] = mod_assessment_min
        module["assessment_minutes_excluded_from_instructional_total"] = True
        module["counts_toward_720_instructional_minutes"] = counts_720
        module["counts_toward_certificate_gate"] = gate
        module["counts_toward_optional_clinical_support"] = False
        module["source_time_basis"] = SYLLABUS_BASIS
        if is_repair:
            module["time_model_status"] = "source-repair"
        elif gap > 0 or mod_narr < 1:
            module["time_model_status"] = "authored-partial"
        else:
            module["time_model_status"] = "authored"
        notes = (
            f"Instructional allocation {alloc} min inherited from ContentV1 syllabus (not recomputed from narration). "
            f"Lessons currently allocate {lesson_allocated} min."
        )
        if gap > 0:
            notes += (
                f" CONTENT-DEPTH GAP: {gap} min of the {alloc}-min allocation is not yet covered by authored lesson cards; "
                f"expand only from ContentV1 source (do not pad). "
            )
        if mid == "M07":
            notes += (
                " M07 retains its 30-min required final-review theory allocation per ContentV1; the graded final exam and "
                "affidavit are tracked separately under assessments.final_assessment and are NOT double-counted here."
            )
        notes += (
            f" Narration {r1(mod_narr)} min and module-assessment {mod_assessment_min} min are tracked separately and "
            "excluded from the 720 instructional total."
        )
        module["time_model_notes"] = notes

        if counts_720:
            required_total += alloc

    # ---- Module assessments (excluded from instructional total) --------------------
    for mid, block in data.get("assessments", {}).get("module_assessments", {}).items():
        block["estimated_assessment_minutes"] = block.get("estimated_minutes", 0) or 0
        block["assessment_minutes_excluded_from_instructional_total"] = True
        block["counts_toward_720_instructional_minutes"] = False
        block["counts_toward_certificate_gate"] = True
        block["counts_toward_optional_clinical_support"] = False
        block["source_time_basis"] = "CNA-Recert-Course/Content/08_MODULE_KNOWLEDGE_CHECK_BLUEPRINT.md"
        block["time_model_status"] = "assessment"
        block["time_model_notes"] = (
            f"{mid} module assessment ({block.get('estimated_assessment_minutes', 0)} min) is tracked separately and "
            "excluded from the 720 instructional total. May gate the certificate but is not instructional theory time."
        )

    # ---- Final assessment (excluded; not used to inflate lesson narration) ---------
    fa = data.get("assessments", {}).get("final_assessment", {})
    if fa:
        attempt = fa.get("attempt_size", 25) or 25
        fa["estimated_assessment_minutes"] = int(round(attempt * 1.0))  # ~1 min/question planning estimate
        fa["assessment_minutes_excluded_from_instructional_total"] = True
        fa["counts_toward_720_instructional_minutes"] = False
        fa["counts_toward_certificate_gate"] = True
        fa["counts_toward_optional_clinical_support"] = False
        fa["source_time_basis"] = f"Final exam attempt_size ({attempt} Q) at ~1 min/question (planning estimate)"
        fa["time_model_status"] = "assessment"
        fa["time_model_notes"] = (
            "Final exam time is tracked separately and excluded from the 720 instructional total. It must not inflate "
            "lesson narration time, and learner-facing results never reveal answer keys."
        )

    # ---- Optional Clinical Support (never counts toward 720) -----------------------
    cs = data.get("clinical_support", {})
    cs["instructional_minutes"] = 0
    cs["estimated_assessment_minutes"] = 0
    cs["assessment_minutes_excluded_from_instructional_total"] = True
    cs["counts_toward_720_instructional_minutes"] = False
    cs["counts_toward_certificate_gate"] = False
    cs["counts_toward_optional_clinical_support"] = True
    cs["source_time_basis"] = "CNA-Recert-Course/Content/03_CLINICAL_SUPPORT_SYLLABUS_TABLE.md (optional, non-credit)"
    cs["time_model_status"] = "optional-non-credit"
    cs["time_model_notes"] = (
        "Optional Clinical Support is optional, non-credit, non-gating, and never counts toward the 720 required theory "
        "instructional minutes. No clinical-hour credit is claimed."
    )

    # ---- Top-level time model summary ---------------------------------------------
    module_assessment_total = sum(
        b.get("estimated_assessment_minutes", 0)
        for b in data.get("assessments", {}).get("module_assessments", {}).values()
    )
    data["time_model"] = {
        "source_basis": SYLLABUS_BASIS,
        "required_theory_instructional_minutes_total": required_total,
        "required_theory_hours": round(required_total / 60.0, 2),
        "module_allocation": MODULE_ALLOCATION,
        "module_assessment_minutes_excluded": module_assessment_total,
        "course_final_assessment_minutes_excluded": fa.get("estimated_assessment_minutes", 0),
        "optional_clinical_support_counts_toward_720": False,
        "rules": [
            "Instructional minutes inherit from the ContentV1 syllabus allocation; the 720 total is not recomputed from narration or card count.",
            "Narration, reading/review, interaction/challenge/remediation, and assessment minutes are tracked separately.",
            "Module assessments and the final exam are excluded from the 720 instructional total.",
            "Optional Clinical Support never counts toward the 720 required theory minutes.",
            "Content-depth gaps are reported, not padded; SME/source-repair flags are preserved.",
            "No clinical-hour credit is claimed; production certificate remains disabled; no PHI.",
        ],
    }

    CANON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "OK",
        "required_theory_instructional_minutes_total": required_total,
        "module_allocation": MODULE_ALLOCATION,
        "module_assessment_minutes_excluded": module_assessment_total,
        "course_final_assessment_minutes_excluded": fa.get("estimated_assessment_minutes", 0),
        "optional_clinical_support_counts_toward_720": False,
    }, indent=2))
    return 0 if required_total == 720 else 1


if __name__ == "__main__":
    raise SystemExit(main())
