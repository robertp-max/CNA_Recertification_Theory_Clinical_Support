"""validate_m04_no_padding.py

M04 quality guardrail for the CCCCO expansion pass.

Checks:
  - every M04 card has required evidence/value metadata
  - delivery cards are source-referenced to CCCCO 12/13/14 or ContentV1
  - delivery cards have non-trivial instructional value
  - no delivery card appears to be a near-duplicate of another delivery card
  - no learner-facing delivery card leaks source scaffolding
  - online theory does not imply hands-on competency validation or clinical-hour credit
"""
from __future__ import annotations

import json
import re
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CANON = ROOT / "CNA-Recert-Course" / "ContentV2" / "data" / "courseContentV2.json"

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
    "sme_review_flag",
    "compliance_review_flag",
    "estimated_narration_minutes",
    "estimated_reading_minutes",
    "estimated_interaction_minutes",
    "estimated_active_learning_minutes",
    "counts_toward_720_instructional_minutes",
    "time_model_status",
]

SCAFFOLD = [
    "On-Screen Text:",
    "TTS/Transcript-Ready Text:",
    "Correct Answer:",
    "Correct Feedback:",
    "Incorrect Feedback",
    "LESSON 4.",
    "Moodle Activity Type:",
]

FORBIDDEN_SCOPE = [
    "clinical-hour credit",
    "hands-on competency validated",
    "certifies you to perform",
    "you are now competent to perform",
]


def tokens(text: str) -> set[str]:
    return {
        t
        for t in re.findall(r"[a-z0-9]+", text.lower())
        if len(t) > 3
        and t not in {"resident", "patient", "cna", "nurse", "report", "source", "assist", "care", "module"}
    }


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def words(text: str) -> int:
    return len([w for w in re.split(r"\s+", text.strip()) if w])


def main() -> int:
    data = json.loads(CANON.read_text(encoding="utf-8"))
    m04 = next(m for m in data["modules"] if m["module_id"] == "M04")
    failures: list[str] = []
    delivery = []

    if m04.get("counts_toward_optional_clinical_support"):
        failures.append("M04 must not count toward optional clinical support.")
    module_guard = (m04.get("compliance_review_flag") or "").lower()
    if "does not validate hands-on competency" not in module_guard or "clinical-hour credit" not in module_guard:
        failures.append("M04 module compliance flag must explicitly prevent hands-on competency/clinical-hour credit claims.")

    for lesson in m04.get("lessons", []):
        cards = lesson.get("cards", [])
        if lesson.get("estimated_minutes", 0) >= 15:
            dcount = sum(1 for c in cards if c.get("card_type") == "delivery")
            if dcount < 6:
                failures.append(f"M04/{lesson['lesson_id']} has only {dcount} delivery cards for >=15 displayed minutes.")
        for card in cards:
            cid = f"M04/{lesson['lesson_id']}/{card.get('card_id')}"
            for key in REQUIRED_META:
                if key not in card or card.get(key) in ("", None, []):
                    failures.append(f"{cid} missing required metadata/time field: {key}")
            text = "\n".join(str(card.get(k) or "") for k in ("display_title", "learner_facing_content", "narration_script", "transcript_text"))
            low = text.lower()
            forbidden = next((p for p in FORBIDDEN_SCOPE if p in low), None)
            guarded = any(
                phrase in low
                for phrase in (
                    "does not validate",
                    "does not create",
                    "not validated",
                    "does not claim",
                    "no clinical-hour credit",
                    "does not replace",
                    "only perform",
                )
            )
            if forbidden and not guarded:
                failures.append(f"{cid} may imply forbidden scope/credit claim: {forbidden}")
            if card.get("card_type") == "delivery":
                if words(card.get("learner_facing_content") or "") < 70:
                    failures.append(f"{cid} delivery content is too short to demonstrate unique instructional value.")
                hit = next((p for p in SCAFFOLD if p in text), None)
                if hit:
                    failures.append(f"{cid} leaks scaffolding/filler phrase: {hit}")
                ref = card.get("source_reference") or ""
                if not any(s in ref for s in ("CCCCO Module 12", "CCCCO Module 13", "CCCCO Module 14", "ContentV1")):
                    failures.append(f"{cid} source_reference is not traceable to CCCCO 12/13/14 or ContentV1: {ref}")
                delivery.append((cid, card.get("display_title"), tokens(card.get("learner_facing_content") or "")))
                if re.search(r"\b(validate|validated|sign off|sign-off|certif(?:y|ies|ied))\b", low) and not guarded:
                    failures.append(f"{cid} may imply hands-on competency validation.")
                if "abdominal thrust" in low and not any(phrase in low for phrase in ("hands-on", "clinical skill", "only perform", "trained")):
                    failures.append(f"{cid} choking content must preserve hands-on skill boundary.")
                if "cpr" in low and "does not replace" not in low and "only perform" not in low:
                    failures.append(f"{cid} CPR/AED content must preserve training boundary.")

    for (cid_a, title_a, toks_a), (cid_b, title_b, toks_b) in combinations(delivery, 2):
        score = jaccard(toks_a, toks_b)
        if score > 0.72:
            failures.append(f"Possible duplicate delivery content ({score:.2f}): {cid_a} '{title_a}' vs {cid_b} '{title_b}'")

    print(json.dumps({
        "status": "OK" if not failures else "FAIL",
        "module": "M04",
        "delivery_cards_checked": len(delivery),
        "failures": failures,
    }, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
