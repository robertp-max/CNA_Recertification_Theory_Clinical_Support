"""validate_m05_no_padding.py

M05 quality guardrail for the CCCCO expansion pass.

Checks:
  - every M05 card has required evidence/value metadata
  - delivery cards are source-referenced to CCCCO 10/11/13 or ContentV1
  - delivery cards have a non-trivial unique_learning_value and why_this_card_exists
  - no delivery card appears to be a near-duplicate of another delivery card
  - no learner-facing delivery card leaks source scaffolding
  - skin/pressure-injury cards keep SME/compliance flags and CNA-scope boundaries
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
    "LESSON 5.5:",
    "Moodle Activity Type:",
]


def tokens(text: str) -> set[str]:
    return {
        t
        for t in re.findall(r"[a-z0-9]+", text.lower())
        if len(t) > 3 and t not in {"resident", "patient", "cna", "nurse", "report", "source"}
    }


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def words(text: str) -> int:
    return len([w for w in re.split(r"\s+", text.strip()) if w])


def main() -> int:
    data = json.loads(CANON.read_text(encoding="utf-8"))
    m05 = next(m for m in data["modules"] if m["module_id"] == "M05")
    failures: list[str] = []
    delivery = []

    if m05.get("sme_review_flag") in ("", None, "None identified"):
        failures.append("M05 module SME review flag was cleared; must remain visible for skin integrity / pressure injury content.")
    if "independent pressure-injury" not in (m05.get("compliance_review_flag") or ""):
        failures.append("M05 module compliance flag does not explicitly guard against independent pressure-injury staging/treatment.")

    for lesson in m05.get("lessons", []):
        cards = lesson.get("cards", [])
        if lesson.get("estimated_minutes", 0) >= 15:
            dcount = sum(1 for c in cards if c.get("card_type") == "delivery")
            if dcount < 6:
                failures.append(f"M05/{lesson['lesson_id']} has only {dcount} delivery cards for >=15 displayed minutes.")
        for card in cards:
            cid = f"M05/{lesson['lesson_id']}/{card.get('card_id')}"
            for key in REQUIRED_META:
                if key not in card or card.get(key) in ("", None, []):
                    failures.append(f"{cid} missing required metadata/time field: {key}")
            if card.get("card_type") == "delivery":
                text = "\n".join(str(card.get(k) or "") for k in ("display_title", "learner_facing_content", "narration_script", "transcript_text"))
                if words(card.get("learner_facing_content") or "") < 70:
                    failures.append(f"{cid} delivery content is too short to demonstrate unique instructional value.")
                hit = next((p for p in SCAFFOLD if p in text), None)
                if hit:
                    failures.append(f"{cid} leaks scaffolding/filler phrase: {hit}")
                ref = card.get("source_reference") or ""
                if "CCCCO Module 10" not in ref and "CCCCO Module 11" not in ref and "CCCCO Module 13" not in ref and "ContentV1" not in ref:
                    failures.append(f"{cid} source_reference is not traceable to CCCCO 10/11/13 or ContentV1: {ref}")
                delivery.append((cid, card.get("display_title"), tokens(card.get("learner_facing_content") or "")))
                blob = (card.get("learner_facing_content") or "").lower()
                if "pressure" in blob or "skin" in blob or "wound" in blob:
                    flag_blob = (card.get("sme_review_flag") or "") + " " + (card.get("compliance_review_flag") or "")
                    if "sme" not in flag_blob.lower() or "independent pressure-injury" not in flag_blob.lower():
                        failures.append(f"{cid} skin/pressure card lacks SME/scope guardrail.")
                    if re.search(r"\byou (stage|treat|diagnose)\b", blob):
                        failures.append(f"{cid} implies independent CNA staging/treatment/diagnosis.")

    for (cid_a, title_a, toks_a), (cid_b, title_b, toks_b) in combinations(delivery, 2):
        score = jaccard(toks_a, toks_b)
        # Allow related cards to share terms; fail only near-duplicates.
        if score > 0.72:
            failures.append(f"Possible duplicate delivery content ({score:.2f}): {cid_a} '{title_a}' vs {cid_b} '{title_b}'")

    print(json.dumps({
        "status": "OK" if not failures else "FAIL",
        "module": "M05",
        "delivery_cards_checked": len(delivery),
        "failures": failures,
    }, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
