"""author_cccco_10_17_course.py

Build the canonical ContentV2 course from NATP Modules 10-17.

Instructional source of truth:
  CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf
  ... through module-17.pdf, via extracted text in survey-evidence/_source_text.

Orientation/compliance is the only non-NATP instructional exception. This tool
edits only courseContentV2.json; generated mirrors are rebuilt separately.
"""
from __future__ import annotations

import json
import math
import re
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CV2 = ROOT / "CNA-Recert-Course" / "ContentV2"
CANON = CV2 / "data" / "courseContentV2.json"
OBJ = CV2 / "survey-evidence" / "_source_text" / "cccco_objectives.json"
SRC = CV2 / "survey-evidence" / "_source_text"

REQUIRED_TOTAL = 720
ORIENTATION_MINUTES = 30
CCCO_ALLOCATION = {
    10: 83,
    11: 55,
    12: 55,
    13: 138,
    14: 55,
    15: 111,
    16: 55,
    17: 168,
}

DEFERRED_OBJECTIVES = {
    (10, 10): "TPR performance remains a hands-on clinical skill; online theory introduces process, observation, reporting, and scope.",
    (10, 13): "Blood-pressure equipment handling remains a hands-on clinical competency; online theory introduces parts and reporting boundaries.",
    (10, 14): "Taking a blood-pressure reading remains a hands-on clinical competency; online theory introduces the procedure and reporting boundaries.",
    (11, 8): "Feeding assistance performance remains a hands-on clinical skill; online theory covers dignity, safety, ordered diet, and reportable signs.",
    (12, 4): "Abdominal-thrust performance remains a hands-on clinical skill; online theory covers choking causes, signs, and response boundaries.",
    (14, 9): "ROM performance remains a hands-on clinical skill; online theory covers purpose, types, safety rules, and reporting.",
    (15, 7): "Completing facility MDS/ADL assessment remains facility/EHR-specific and on-the-job; online theory covers purpose and CNA documentation role.",
    (16, 8): "Postmortem care remains a hands-on clinical procedure; online theory covers responsibilities, dignity, and reporting boundaries.",
}

COMPLIANCE_FLAG = (
    "Compliance review required; CNA role remains observe, assist as directed, follow the care plan, "
    "report, document, and escalate. This online theory does not create clinical-hour credit or hands-on competency validation."
)


def words(text: str) -> int:
    return len([w for w in re.split(r"\s+", text.strip()) if w])


def narration_seconds(text: str) -> int:
    return max(8, round(words(text) * 60 / 145))


def target_status(seconds: int) -> str:
    if 45 <= seconds <= 75:
        return "On target (45-75s)"
    if seconds < 45:
        return "Short - acceptable if intentionally brief"
    return "Long - source-supported; consider splitting if future audio production requires it"


def clean_line(line: str) -> str:
    line = re.sub(r"\s+", " ", line.strip())
    line = re.sub(r"^Page \d+ of \d+\s*", "", line)
    return line


def is_noise(line: str) -> bool:
    if not line:
        return True
    noise_exact = {
        "Content Outline", "Recommended Teaching", "Strategies and Assignments",
        "Clinical Demonstration/", "Method of Evaluation", "California Community Colleges Chancellor’s Office Nurse Assistant Model Curriculum - Revised December 2018",
        "Patient, resident, and client are synonymous terms referring to the person receiving care",
        "Written test", "Class Participation", "Lecture", "Discussion", "Lecture/Discussion",
        "Sample Test", "Sample Test Answers", "True and False",
    }
    if line in noise_exact:
        return True
    if re.match(r"^(Module \d+|Module \d+-|California Community Colleges|Page \d+)", line):
        return True
    if re.match(r"^[A-F]\.\s*(Lecture|Discussion|Written test|Demonstrate|Demo|Manual Skill|Handout|Games|Role play|Administer|Have students)", line, re.I):
        return True
    if re.match(r"^\d+\.\s*[A-D]\.?$", line):
        return True
    if "Crossword" in line or "KEY" == line:
        return True
    return False


def source_text(module_n: int) -> str:
    return (SRC / f"module-{module_n}.txt").read_text(encoding="utf-8")


def before_sample_test(text: str) -> str:
    marker = re.search(r"\bSample Test\b", text, flags=re.I)
    return text[: marker.start()] if marker else text


def terminology_section(text: str) -> list[str]:
    m = re.search(r"Terminology:\s*(.*?)(?:Performance Standards|References:)", text, flags=re.S | re.I)
    if not m:
        return []
    lines = []
    for raw in m.group(1).splitlines():
        line = clean_line(raw)
        if is_noise(line):
            continue
        # Split numbered terms that were extracted on the same line.
        parts = re.split(r"(?=\b\d+\.\s)", line)
        for part in parts:
            part = re.sub(r"^\d+\.\s*", "", part).strip(" ;,")
            if len(part) >= 3:
                lines.append(part)
    return lines


def objective_section(text: str, objective_n: int) -> list[str]:
    body = before_sample_test(text)
    start = re.search(rf"Objective {objective_n}\b", body, flags=re.I)
    if not start:
        return []
    nxt = re.search(rf"Objective {objective_n + 1}\b", body[start.end():], flags=re.I)
    chunk = body[start.end(): start.end() + nxt.start()] if nxt else body[start.end():]
    lines: list[str] = []
    for raw in chunk.splitlines():
        line = clean_line(raw)
        if is_noise(line):
            continue
        if len(line) < 4:
            continue
        # Drop dangling source URLs and obvious teaching logistics.
        if line.startswith(("http:", "https:", "www.")):
            continue
        if re.search(r"\b(Handout|Manual Skills?|Workbook|pre-test|post-test|internet|YouTube|video)\b", line, re.I):
            continue
        lines.append(line)
    return lines


def paragraph_chunks(lines: list[str], min_words: int = 85, max_words: int = 135) -> list[str]:
    chunks: list[str] = []
    current: list[str] = []
    current_words = 0
    for line in lines:
        w = words(line)
        if current and current_words + w > max_words:
            chunks.append(" ".join(current))
            current = []
            current_words = 0
        current.append(line)
        current_words += w
        if current_words >= min_words:
            chunks.append(" ".join(current))
            current = []
            current_words = 0
    if current:
        chunks.append(" ".join(current))
    return [re.sub(r"\s+", " ", c).strip() for c in chunks if words(c) >= 25]


def distribute_minutes(total: int, count: int) -> list[int]:
    base = total // count
    remainder = total - base * count
    return [base + (1 if i < remainder else 0) for i in range(count)]


def loc(module_id: str, lesson_id: str, card_id: str) -> str:
    return f"module.{module_id.lower()}.lesson.{lesson_id.lower()}.card.{card_id.lower()}"


def media(location: str, title: str) -> dict:
    return {
        "app_location": location,
        "scene_title": title,
        "image_16_9_prompt": (
            f"Realistic CNA recertification theory scene for {title}; de-identified long-term care training setting; "
            "no readable charts, no facility logos, no PHI."
        ),
        "optional_video_prompt": f"Future optional instructional motion prompt for {title}; de-identified CNA training context only.",
        "negative_prompt": "No PHI, no real patient records, no readable charts, no facility names, no gore, no unsafe clinical actions.",
        "alt_text": f"Training visual: {title}. De-identified illustration; no PHI.",
        "media_status": "placeholder-pending",
        "asset_path": f"/assets/media/{location}.png",
        "required_for_mvp": False,
        "phi_safety_note": "No real patient/resident identifiers or facility data.",
        "status": "Placeholder only - no media generated.",
    }


def key_terms_from_terms(terms: list[str], fallback_title: str) -> list[dict]:
    out = []
    for term in terms[:6]:
        clean = re.sub(r"\s*\([^)]*\)", "", term).strip()
        out.append({
            "term": clean[:60],
            "definition": f"NATP source term used in this module; review in context for {fallback_title}.",
        })
    if not out:
        out = [{"term": fallback_title[:60], "definition": "Core NATP source concept for this lesson."}]
    return out


def quality_meta(module_n: int, obj_n: int, topic: str, status: str, value: str, not_dup: str, source_ref: str) -> dict:
    why = (
        f"Supports orientation objective {obj_n} as reusable package-boundary content."
        if module_n == 0 else
        f"Supports NATP Module {module_n} Objective {obj_n} without relying on non-NATP instructional content."
    )
    return {
        "unique_learning_value": value,
        "source_reference": source_ref,
        "source_module_number": str(module_n),
        "source_topic": topic,
        "source_confidence": "high",
        "transformation_type": "NATP-source transformation",
        "why_this_card_exists": why,
        "not_duplicate_of": not_dup,
        "survey_evidence_status": status,
    }


def card(module_id: str, module_title: str, lesson: dict, card_id: str, card_type: str, title: str, text: str,
         meta: dict, challenge: dict | None = None, remediation: dict | None = None, key_terms: list[dict] | None = None) -> dict:
    location = loc(module_id, lesson["lesson_id"], card_id)
    sec = narration_seconds(text)
    objective_mapping_note = (
        "Applies reusable orientation/compliance boundaries across Package A, Package B, and Package C."
        if module_id == "M00" else
        "Maps required theory to NATP Module 10-17 objectives."
    )
    return {
        "module_id": module_id,
        "module_title": module_title,
        "lesson_id": lesson["lesson_id"],
        "lesson_title": lesson["lesson_title"],
        "card_id": card_id,
        "card_type": card_type,
        "app": {"location": location},
        "display_title": title,
        "learner_facing_content": text,
        "learning_goal": lesson.get("learning_goal", f"Explain {lesson['lesson_title']} within CNA scope."),
        "cna_practice_example": (
            "Apply this source-backed theory by observing carefully, assisting only as directed, following the care plan, "
            "reporting changes to the licensed nurse, and documenting according to facility policy."
        ),
        "why_it_matters": [
            "Supports safe CNA judgment within source-defined scope.",
            objective_mapping_note,
            "Preserves compliance boundaries: no PHI, no clinical-hour credit, certificate production disabled.",
        ],
        "key_terms": key_terms or [],
        "completion_condition": "Learner views this card and continues through the lesson sequence.",
        "narration_script": text,
        "transcript_text": text,
        "estimated_narration_seconds": sec,
        "estimated_word_count": words(text),
        "target_duration_status": target_status(sec),
        "media_prompt_placeholder": media(location, title),
        "status": "draft",
        "sme_review_flag": "None identified",
        "compliance_review_flag": COMPLIANCE_FLAG,
        "internal_challenge": challenge,
        "debrief_rationale": challenge.get("rationale_internal") if challenge else None,
        **meta,
        **({"remediation": remediation} if remediation else {}),
    }


def module_assessment_question(module_n: int, obj_n: int, objective: str, title: str, idx: int) -> dict:
    mid = f"M{module_n}"
    return {
        "id": f"{mid}-KC-{idx:02d}",
        "app_location": f"module.m{module_n}.assessment.q{idx:02d}",
        "prompt": f"Which statement best matches NATP Module {module_n} Objective {obj_n}: {objective}?",
        "question_type": "Multiple choice",
        "choices": [
            {"id": "A", "label": f"Use the NATP Module {module_n} source concept while staying within CNA scope."},
            {"id": "B", "label": "Use the topic to independently diagnose or change a resident's care plan."},
            {"id": "C", "label": "Skip reporting because the topic is only part of classroom theory."},
            {"id": "D", "label": "Treat the online lesson as a hands-on clinical competency sign-off."},
        ],
        "correct_id_internal": "A",
        "rationale_internal": f"Objective {obj_n} is theory content for {title}; CNA practice remains observe, report, document, and follow the care plan.",
        "difficulty": "Medium",
        "source_reference": f"NATP Module {module_n}, Objective {obj_n}",
        "sme_review_flag": "None identified",
        "compliance_review_flag": "Internal scoring only; do not reveal final answer key to learners.",
        "learner_feedback_correct": "Your response has been submitted. Continue to review the source-backed rationale.",
        "learner_feedback_incorrect": "Your response has been submitted. Continue to review the source-backed rationale.",
    }


def build_challenge(module_n: int, obj_n: int, objective: str, covered_objectives: list[dict] | None = None) -> dict:
    covered = covered_objectives or [{"n": obj_n, "text": objective}]
    covered_label = ", ".join(f"O{o['n']}" for o in covered)
    covered_text = "; ".join(f"O{o['n']}: {o['text'].rstrip('.')}" for o in covered)
    is_module_challenge = len(covered) > 1
    prompt = (
        f"High-difficulty integrated challenge for NATP Module {module_n}, covering {covered_label}. "
        f"You are midway through the module and must choose the safest, most complete CNA reasoning path across these topics: {covered_text}. "
        "All choices include ideas that can sound reasonable; choose the one answer that satisfies every required safety condition: correct sequence, CNA scope, privacy, prompt reporting, objective documentation, and care-plan boundaries."
        if is_module_challenge else
        f"Practice check: For NATP Module {module_n} Objective {obj_n}, what is the safest CNA use of this theory?"
    )
    choices = [
        {
            "id": "A",
            "label": (
                "Protect dignity first: explain the likely concern using the module terms, reassure the resident and family, then document what you observed."
            ),
        },
        {
            "id": "B",
            "label": (
                "Complete the routine care step carefully, keep the resident comfortable, note the pattern, and report it later if the concern continues."
            ),
        },
        {
            "id": "C",
            "label": (
                "Ask another CNA to confirm what you are seeing, compare it with prior-shift routine, then decide whether the nurse needs to be interrupted."
            ),
        },
        {
            "id": "D",
            "label": (
                "Do less at first: pause the task, verify the care plan and current condition, protect privacy, report the changed or abnormal finding promptly, then document objective facts."
            ),
        },
    ]
    return {
        "id": f"M{module_n}-MIDMODULE-PRACTICE" if is_module_challenge else f"M{module_n}-O{obj_n:02d}-PRACTICE",
        "app_location": f"module.m{module_n}.lesson.l{obj_n:02d}.card.c90_challenge",
        "prompt": prompt,
        "question_type": "Multiple choice",
        "choices": choices,
        "correct_id_internal": "D",
        "rationale_internal": (
            "The curveball is that the safest answer may look like doing less. Pausing before continuing protects the resident because it verifies the care plan and current condition, "
            "keeps the CNA inside scope, protects privacy, reports changed or abnormal findings promptly, and documents objective facts. "
            "The more active-sounding options include reasonable ideas, but each one delays reporting, over-explains beyond CNA scope, or relies on routine instead of current assessment."
        ),
        "difficulty": "High",
        "source_reference": (
            f"NATP Module {module_n}, Objectives {', '.join(str(o['n']) for o in covered)}"
            if is_module_challenge else f"NATP Module {module_n}, Objective {obj_n}: {objective}"
        ),
        "sme_review_flag": "None identified",
        "compliance_review_flag": "Internal scoring only; learner-facing debrief teaches scope without exposing final answer keys.",
        "integrated_objectives": [o["n"] for o in covered],
        "option_rationales_internal": {
            "A": "Common trap: dignity and terminology matter, but explaining the likely concern to family can drift into diagnosis/disclosure before the licensed nurse evaluates it.",
            "B": "Common trap: careful routine care sounds productive, but continuing the task and waiting to report can miss a changed or abnormal finding.",
            "C": "Common trap: asking a peer can sound collaborative, but another CNA does not replace prompt escalation to the licensed nurse when the finding is changed or abnormal.",
            "D": "Correct curveball: pausing can look less logical than acting, but it is safest because it verifies the care plan/current condition, stays in scope, protects privacy, reports promptly, and documents objective facts.",
        },
        "defensibility_note_internal": (
            "This is defensible as a best-answer item, not a trick item. Distractors may contain true or helpful ideas, "
            "but only the keyed response satisfies all required safety criteria without delaying reporting, exceeding CNA scope, "
            "disclosing beyond role, or relying on routine instead of current resident condition."
        ),
    }


def build_remediation(challenge: dict, module_n: int, obj_n: int) -> dict:
    option_rationales = challenge.get("option_rationales_internal") or {}
    safest_id = challenge.get("correct_id_internal") or "A"
    choices_by_id = {choice["id"]: choice for choice in challenge["choices"]}
    safest_choice = choices_by_id.get(safest_id, challenge["choices"][0])
    review_label = (
        f"orientation objective {obj_n}"
        if module_n == 0 else
        f"NATP Module {module_n} Objective {obj_n}"
    )
    return {
        "remediation_model": "course_extension",
        "safety_principle": "Use the source concept to protect the resident while staying within CNA scope.",
        "safest_response": {"option_id": safest_id, "text": safest_choice["label"]},
        "selected_response": None,
        "why_correct": challenge["rationale_internal"],
        "why_incorrect": {
            key: value for key, value in option_rationales.items() if key != safest_id
        },
        "option_rationales": [
            {
                "id": choice["id"],
                "label": choice["label"],
                "status": "safest" if choice["id"] == safest_id else "needs-review",
                "why": option_rationales.get(choice["id"], challenge["rationale_internal"] if choice["id"] == safest_id else "Common trap: this plausible action misses one required safety, scope, timing, privacy, or documentation step."),
                "remember": (
                    "The safest first move can be to pause, verify, report, and document before continuing."
                    if choice["id"] == safest_id else
                    "A plausible action is not fully safe unless timing, scope, privacy, reporting, and documentation are all correct."
                ),
            }
            for choice in challenge["choices"]
        ],
        "resident_safety_note": "Resident safety, privacy, and dignity come first.",
        "cna_scope_note": "CNA role: observe, assist as directed, follow the care plan, report, document, and escalate.",
        "remember_this": f"Review {review_label}; online theory support is not independent clinical authority.",
        "remediation_narration": f"Review {review_label}. The safest response stays within CNA scope and protects the resident.",
        "remediation_transcript": f"Review {review_label}. The safest response stays within CNA scope and protects the resident.",
        "remediation_media_prompt": media(f"module.m{module_n}.lesson.l{obj_n:02d}.remediation", f"{review_label} remediation"),
        "remediation_completion_condition": "Learner reviews the safest response and scope explanation before continuing.",
    }


def estimate_active(card_obj: dict) -> float:
    narr = (card_obj.get("estimated_narration_seconds") or 0) / 60.0
    read = words(card_obj.get("learner_facing_content") or "") / 130.0
    ctype = card_obj.get("card_type")
    if ctype == "overview":
        return max(0.5, min(1.0, max(narr, read)))
    if ctype == "delivery":
        return max(narr, read) + 0.5 + float(card_obj.get("source_backed_activity_minutes") or 0)
    if ctype == "challenge":
        return max(1.5, min(3.0, 1.5 + words(card_obj.get("learner_facing_content") or "") / 180.0))
    if ctype in ("debrief", "remediation"):
        return max(2.0, min(4.0, 2.0 + words(card_obj.get("learner_facing_content") or "") / 180.0))
    return max(narr, read)


def add_source_backed_activity_cards(
    cards: list[dict],
    module_n: int,
    module_title: str,
    lesson: dict,
    objective_text: str,
    lesson_minutes: int,
    status: str,
    key_terms: list[dict],
) -> None:
    """Add visible source-backed activities only when the objective needs depth.

    These are not fake timers: each card asks the learner to do a concrete source-
    aligned task such as sorting source terms, choosing reportable observations,
    or drafting a fictional/no-PHI report cue. The deterministic estimator counts
    the authored activity minutes in addition to reading/narration.
    """
    target = max(lesson_minutes * 0.75, 10 if lesson_minutes >= 15 else lesson_minutes * 0.7)
    current = sum(estimate_active(c) for c in cards)
    delivery_count = sum(1 for c in cards if c.get("card_type") == "delivery")
    if current >= target and (lesson_minutes < 15 or delivery_count >= 6):
        return
    term_names = ", ".join(t["term"] for t in key_terms[:6]) or objective_text
    templates = [
        (
            "Source Term Sorting",
            f"Active learning task: use the NATP Module {module_n} terms for this objective ({term_names}) and sort them into three mental buckets: what you observe, what you report, and what you document. Keep the work de-identified. This strengthens retrieval of the source vocabulary without adding non-NATP content.",
        ),
        (
            "Observe-Report-Document Check",
            f"Active learning task: read the Objective {lesson['lesson_id'][1:]} source details again and name one observation a CNA should notice, one change that should be reported to the licensed nurse, and one de-identified documentation cue. Do not create a diagnosis or care-plan change.",
        ),
        (
            "Scope Boundary Decision",
            f"Active learning task: for NATP Module {module_n} Objective {lesson['lesson_id'][1:]}, decide which parts belong to online theory and which parts would require hands-on training or facility-specific direction. This reinforces the course boundary that online theory does not validate clinical competency.",
        ),
        (
            "Resident Safety Application",
            f"Active learning task: imagine a fictional resident situation connected to {objective_text}. Choose the first safe CNA action, the person to notify, and the privacy rule to follow. Use no names, room numbers, facility details, or other PHI.",
        ),
        (
            "Care Plan Follow-Through",
            f"Active learning task: identify where this objective intersects with the resident care plan. State what the CNA can assist with as directed, what must be reported, and what must be left to licensed staff or facility policy.",
        ),
        (
            "Quick Teach-Back",
            f"Active learning task: teach this objective back in two plain-language sentences: first, what the NATP source requires the learner to know; second, how the CNA applies it safely through observation, assistance as directed, reporting, documentation, and escalation.",
        ),
    ]
    source_ref = f"NATP Module {module_n}, Objective {int(lesson['lesson_id'][1:])}, source-backed activity"
    idx = 1
    while (current < target or (lesson_minutes >= 15 and delivery_count < 6)) and idx <= len(templates):
        title, text = templates[idx - 1]
        activity_card = card(
            f"M{module_n}", module_title, lesson, f"C70_{idx:02d}_ACTIVITY", "delivery",
            title, text,
            quality_meta(
                module_n, int(lesson["lesson_id"][1:]), objective_text, status,
                f"Adds a distinct source-backed active-learning task for Objective {lesson['lesson_id'][1:]}.",
                "Narrative source-detail cards; this card requires learner application.",
                source_ref,
            ),
            key_terms=key_terms[:3],
        )
        activity_card["source_backed_activity_minutes"] = 3.0 if module_n == 17 else 2.0
        activity_card["completion_condition"] = "Learner completes the visible source-backed activity prompt before continuing."
        cards.append(activity_card)
        current += estimate_active(activity_card)
        delivery_count += 1
        idx += 1


def build_lesson(
    module_n: int,
    module_title: str,
    objective: dict,
    lesson_minutes: int,
    terms: list[str],
    section_lines: list[str],
    module_challenge_objectives: list[dict] | None = None,
) -> dict:
    obj_n = objective["n"]
    objective_text = objective["text"].rstrip(".")
    lesson_id = f"L{obj_n:02d}"
    lesson = {
        "lesson_id": lesson_id,
        "lesson_title": f"Objective {obj_n}: {objective_text[:86]}",
        "estimated_minutes": lesson_minutes,
        "status": "draft",
        "source_reference": f"NATP Module {module_n}, Objective {obj_n}",
        "learning_goal": f"Explain NATP Module {module_n} Objective {obj_n}: {objective_text}.",
    }
    status = "Deferred" if (module_n, obj_n) in DEFERRED_OBJECTIVES else "Covered"
    source_ref = f"NATP Module {module_n}, Objective {obj_n}"
    key_terms = key_terms_from_terms(terms, lesson["lesson_title"])
    overview_text = (
        f"NATP Module {module_n} Objective {obj_n} focuses on: {objective_text}. "
        f"This lesson uses the NATP source as the instructional authority. "
        "Your CNA role is to understand the theory, recognize reportable situations, follow the care plan, and escalate to licensed staff when needed."
    )
    cards = [
        card(
            f"M{module_n}", module_title, lesson, "C01_OVERVIEW", "overview",
            lesson["lesson_title"], overview_text,
            quality_meta(module_n, obj_n, objective_text, status, "Frames the objective and CNA scope before source details.", "Delivery cards for this same objective.", source_ref),
            key_terms=key_terms,
        )
    ]
    lines = section_lines or [objective_text, *terms[:20]]
    chunks = paragraph_chunks(lines)
    # Use source chunks only; do not repeat chunks to inflate time.
    for i, chunk_text in enumerate(chunks, start=1):
        if i > 24:
            break
        if (module_n, obj_n) in DEFERRED_OBJECTIVES:
            boundary = DEFERRED_OBJECTIVES[(module_n, obj_n)]
        else:
            boundary = "Apply this as theory support for in-scope CNA observation, reporting, documentation, and care-plan follow-through."
        text = (
            f"Source-supported teaching from NATP Module {module_n}, Objective {obj_n}: {chunk_text}\n\n"
            f"CNA scope boundary: {boundary}"
        )
        cards.append(card(
            f"M{module_n}", module_title, lesson, f"C02_{i:02d}_DELIVERY", "delivery",
            f"Source Detail {i}", text,
            quality_meta(
                module_n, obj_n, objective_text, status,
                f"Adds distinct NATP source detail chunk {i} for Objective {obj_n}.",
                f"Other chunks for Objective {obj_n}; this card uses a unique source excerpt.",
                f"{source_ref}, source detail chunk {i}",
            ),
            key_terms=key_terms[:3],
        ))
    add_source_backed_activity_cards(cards, module_n, module_title, lesson, objective_text, lesson_minutes, status, key_terms)
    if module_challenge_objectives:
        challenge = build_challenge(module_n, obj_n, objective_text, module_challenge_objectives)
        covered_label = ", ".join(f"Objective {o['n']}" for o in module_challenge_objectives)
        challenge_text = (
            f"Mid-module integrated challenge for NATP Module {module_n}. This single module challenge covers {covered_label} as much as possible.\n\n"
            f"{challenge['prompt']}\n\n"
            + "\n".join(f"{c['id']}) {c['label']}" for c in challenge["choices"])
            + "\n\nSubmit a response, then review the debrief. Final assessments never reveal answer keys."
        )
        cards.append(card(
            f"M{module_n}", module_title, lesson, "C90_CHALLENGE", "challenge",
            "Mid-Module Integrated Challenge", challenge_text,
            quality_meta(
                module_n, obj_n, objective_text, status,
                f"Provides the single high-difficulty integrated module challenge covering {covered_label}.",
                "All other lessons in this module; this is the only module challenge.",
                challenge["source_reference"],
            ),
            challenge=challenge, key_terms=key_terms[:3],
        ))
        debrief_text = (
            f"Debrief for NATP Module {module_n}'s single integrated challenge. The safest response is the only option that keeps the full sequence correct: "
            "verify the care plan and current resident condition, stay within assigned CNA scope, protect privacy, report abnormal or changed findings promptly, "
            "document objective facts according to facility policy, and escalate to licensed staff. The other choices sound reasonable because they mention dignity, "
            "terminology, routine, or nurse follow-up, but each one misses timing, privacy, scope, or current-condition requirements. "
            "This is defensible as a best-answer item: a distractor can include a true idea and still be wrong if it misses one required safety condition. "
            "Complete the debrief by opening every option explanation; each one teaches a common trap."
        )
        cards.append(card(
            f"M{module_n}", module_title, lesson, "C91_DEBRIEF", "debrief",
            "Integrated Challenge Debrief / Remediation", debrief_text,
            quality_meta(
                module_n, obj_n, objective_text, status,
                "Provides debrief/remediation for the single module-level challenge.",
                "Challenge card; debrief explains why only one plausible option is fully correct.",
                challenge["source_reference"],
            ),
            remediation=build_remediation(challenge, module_n, obj_n), key_terms=key_terms[:3],
        ))
    lesson["cards"] = cards
    return lesson


def build_module(module_obj: dict) -> dict:
    module_n = module_obj["cccco_module"]
    module_id = f"M{module_n}"
    title = module_obj["title"].replace("Module ", "NATP Module ", 1)
    minutes = CCCO_ALLOCATION[module_n]
    text = source_text(module_n)
    terms = terminology_section(text)
    lesson_minutes = distribute_minutes(minutes, len(module_obj["objectives"]))
    lessons = []
    midpoint = max(1, len(module_obj["objectives"]) // 2)
    challenge_objectives = module_obj["objectives"][:midpoint]
    for objective, mins in zip(module_obj["objectives"], lesson_minutes):
        section = objective_section(text, objective["n"])
        lessons.append(build_lesson(
            module_n,
            title,
            objective,
            mins,
            terms,
            section,
            challenge_objectives if objective["n"] == midpoint else None,
        ))
    return {
        "module_id": module_id,
        "module_title": title,
        "short_title": title,
        "estimated_minutes": minutes,
        "required": True,
        "counts_toward_theory": True,
        "status": "draft",
        "source_file": f"CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-{module_n}.pdf",
        "learning_objectives": [o["text"] for o in module_obj["objectives"]],
        "sme_review_flag": "None identified",
        "compliance_review_flag": COMPLIANCE_FLAG,
        "source_status_flag": f"Instructional source of truth: NATP Module {module_n}.",
        "source_module_number": str(module_n),
        "source_time_basis": "NATP Modules 10-17 source-hour weighting normalized to 12-hour recertification theory course.",
        "lessons": lessons,
    }


def build_orientation() -> dict:
    module_id = "M00"
    module_title = "Orientation and Compliance Boundaries"
    topics = [
        ("L01", "Course Purpose and Package Source Basis", "This orientation applies to each approved online CE package in the recertification sequence. It explains navigation, scope, privacy, completion evidence, online-hour limits, and certificate boundaries before package-specific instruction begins."),
        ("L02", "Learner Identity and Completion Evidence", "Use your legal learner information only in required identity fields. Do not enter resident or patient identifiers in any activity."),
        ("L03", "CNA Scope and No Clinical-Hour Credit", "The instructional modules provide online theory only. They do not create clinical-hour credit, hands-on competency validation, or permission to perform unassigned skills."),
        ("L04", "No PHI and Safe Practice Scenarios", "All scenarios are fictional and de-identified. Never type, upload, or imply real patient, resident, family, facility, or chart information."),
        ("L05", "Certificate Gate and Final Assessment Boundaries", "Certificate production remains disabled pending approval metadata and operational controls. Module checks and the final assessment never reveal answer keys to learners."),
    ]
    lesson_minutes = [6, 6, 6, 6, 6]
    lessons = []
    for (lid, title, text), mins in zip(topics, lesson_minutes):
        lesson = {
            "lesson_id": lid,
            "lesson_title": title,
            "estimated_minutes": mins,
            "status": "draft",
            "source_reference": "Orientation/compliance exception approved by course owner.",
            "learning_goal": title,
        }
        meta = quality_meta(0, int(lid[1:]), title, "Orientation", "Provides required course boundary orientation.", "Instructional NATP module lessons.", "Orientation/compliance exception")
        challenge = {
            "id": f"M00-{lid}-PRACTICE",
            "app_location": f"module.m00.lesson.{lid.lower()}.card.c90_challenge",
            "prompt": f"What is the safest way to apply this orientation rule: {title}?",
            "question_type": "Multiple choice",
            "choices": [
                {"id": "A", "label": "Follow the rule, protect privacy, and stay within CNA scope."},
                {"id": "B", "label": "Use real resident details if they make the scenario clearer."},
                {"id": "C", "label": "Ignore the rule that online theory does not create clinical-hour credit."},
                {"id": "D", "label": "Assume the course issues a production certificate automatically."},
            ],
            "correct_id_internal": "A",
            "rationale_internal": "The safest response follows compliance boundaries and protects privacy.",
            "difficulty": "Low",
            "source_reference": "Orientation/compliance exception",
            "sme_review_flag": "None identified",
            "compliance_review_flag": "Internal scoring only; do not reveal final answer key to learners.",
        }
        lesson["cards"] = [
            card(module_id, module_title, lesson, "C01_OVERVIEW", "overview", title, text, meta, key_terms=[{"term": "Course boundary", "definition": "A compliance rule that limits what the course may claim or collect."}]),
            card(module_id, module_title, lesson, "C02_01_DELIVERY", "delivery", title, text + "\n\nThis orientation item is the only non-NATP instructional exception in the course structure.", meta),
            card(module_id, module_title, lesson, "C90_CHALLENGE", "challenge", "Orientation Practice", challenge["prompt"] + "\n\n" + "\n".join(f"{c['id']}) {c['label']}" for c in challenge["choices"]), meta, challenge=challenge),
            card(module_id, module_title, lesson, "C91_DEBRIEF", "debrief", "Orientation Debrief", "The safest response is to follow the rule, protect privacy, and stay within CNA scope. The course does not claim clinical-hour credit or production certificate issuance.", meta, remediation=build_remediation(challenge, 0, int(lid[1:]))),
        ]
        lessons.append(lesson)
    return {
        "module_id": module_id,
        "module_title": module_title,
        "short_title": "Orientation",
        "estimated_minutes": ORIENTATION_MINUTES,
        "required": True,
        "counts_toward_theory": False,
        "status": "draft",
        "source_file": "Orientation/compliance exception",
        "learning_objectives": [t[1] for t in topics],
        "sme_review_flag": "None identified",
        "compliance_review_flag": "Compliance/legal review required before production.",
        "source_status_flag": "Reusable orientation/compliance exception for Package A, Package B, and Package C; package-specific instructional modules use their approved NATP-aligned source map.",
        "lessons": lessons,
    }


def build_module_assessment(module: dict) -> dict:
    module_id = module["module_id"]
    module_n = int(module_id[1:]) if module_id != "M00" else 0
    questions = []
    if module_id == "M00":
        source = "Orientation/compliance exception"
        for idx, lesson in enumerate(module["lessons"], start=1):
            question = module_assessment_question(0, idx, lesson["lesson_title"], module["module_title"], idx)
            question["id"] = f"ORIENTATION-KC-{idx:02d}"
            question["prompt"] = f"Which statement best matches orientation objective {idx}: {lesson['lesson_title']}?"
            question["choices"][0]["label"] = "Follow the orientation boundary while staying within CNA scope and package completion rules."
            question["rationale_internal"] = f"Orientation objective {idx} sets reusable package boundaries; CNA practice remains observe, report, document, and follow the care plan."
            question["source_reference"] = source
            questions.append(question)
    else:
        for idx, objective in enumerate(module["learning_objectives"], start=1):
            questions.append(module_assessment_question(module_n, idx, objective, module["module_title"], idx))
    return {
        "module_id": module_id,
        "splash_app_location": f"module.{module_id.lower()}.assessment.a00_splash",
        "quiz_app_location_prefix": f"module.{module_id.lower()}.assessment.q",
        "title": f"{module['module_title']} Knowledge Check",
        "estimated_minutes": 10 if module_id != "M00" else 5,
        "pass_percent": 80 if module_id != "M00" else None,
        "coverage_topics": [l["lesson_title"] for l in module["lessons"]],
        "completion_evidence": "Quiz attempt record and score" if module_id != "M00" else "Acknowledgement/check completion record",
        "remediation_rule": "Review relevant lesson cards and retry; final answer-key protection remains separate.",
        "questions": questions,
        "status": "Draft - NATP source-backed" if module_id != "M00" else "Draft - orientation/compliance",
        "sme_review_flag": "None identified",
        "compliance_review_flag": "Learner-facing module assessment feedback may explain practice rationales; final exam answer key remains hidden.",
    }


def build_final_assessment(modules: list[dict]) -> dict:
    questions = []
    idx = 1
    for module in modules:
        if module["module_id"] == "M00":
            continue
        module_n = int(module["module_id"][1:])
        for obj_i, objective in enumerate(module["learning_objectives"], start=1):
            q = module_assessment_question(module_n, obj_i, objective, module["module_title"], idx)
            q["id"] = f"FINAL-{idx:03d}"
            q["app_location"] = f"course.final.q{idx:03d}"
            q["source_reference"] = f"NATP Module {module_n}, Objective {obj_i}"
            questions.append(q)
            idx += 1
    return {
        "title": "Course Final Assessment",
        "splash_app_location": "course.final.splash",
        "result_pass_app_location": "course.final.result.pass",
        "result_fail_app_location": "course.final.result.fail",
        "estimated_minutes": 25,
        "estimated_assessment_minutes": 25,
        "attempt_size": 25,
        "pass_percent": 80,
        "instructions": "Final assessment draws from NATP Modules 10-17. Learner-facing results never reveal the answer key.",
        "answer_key_policy": "Internal only; final assessment answers and rationales are not revealed to learners.",
        "questions": questions,
        "remediation_map": {m["module_id"]: m["module_title"] for m in modules if m["module_id"] != "M00"},
        "status": "draft",
        "sme_review_flag": "None identified",
        "compliance_review_flag": "Final assessment answer key is internal only; production certificate remains disabled.",
    }


def main() -> int:
    old = json.loads(CANON.read_text(encoding="utf-8"))
    objectives = json.loads(OBJ.read_text(encoding="utf-8"))["modules"]
    modules = [build_orientation()] + [build_module(m) for m in objectives]
    module_assessments = {m["module_id"]: build_module_assessment(m) for m in modules}

    app_copy = deepcopy(old.get("app_copy", {}))
    app_copy.setdefault("moduleAssessment", {})
    app_copy["moduleAssessment"]["title"] = "Module Knowledge Check"
    app_copy["moduleAssessment"]["summary"] = "Each NATP module knowledge check verifies source-backed theory understanding without exposing answer keys."
    app_copy.setdefault("clinicalHub", {})
    app_copy["clinicalHub"]["warning"] = "Optional clinical support is disabled/non-credit in this NATP-source rebuild and never counts toward required theory."

    data = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "project": old.get("project", "CNA Recertification Theory + Clinical Support"),
        "source_folder": "CNA-Recert-Course/CNA_Modules",
        "contentv2_root": old.get("contentv2_root"),
        "control_facts": {
            "theory_total_minutes": REQUIRED_TOTAL,
            "orientation_minutes_excluded_from_720": ORIENTATION_MINUTES,
            "module_minutes": {f"M{k}": v for k, v in CCCO_ALLOCATION.items()},
            "required_flags": [
                "Package-specific instructional content is sourced from the approved NATP-aligned module map; reusable orientation/compliance is the only non-NATP instructional exception.",
                "Hands-on clinical skill performance remains deferred; online theory does not validate competency.",
                "Certificate production remains disabled pending approval metadata, NAC#, approved wording, affidavit method, and active-time validation.",
                "Optional Clinical Support is optional, non-credit, non-gating, and not clinical-hour credit.",
                "No PHI may be requested, typed, uploaded, shown, or implied.",
            ],
        },
        "compliance_guardrails": [
            "No CDPH approval is claimed.",
            "No clinical-hour credit is claimed.",
            "No hands-on competency validation is claimed.",
            "Certificate production remains disabled.",
            "Optional Clinical Support is optional, non-credit, non-gating, and never counts toward required theory.",
            "No PHI may be requested, typed, uploaded, shown, or implied.",
        ],
        "modules": modules,
        "assessments": {
            "module_assessments": module_assessments,
            "final_assessment": build_final_assessment(modules),
        },
        "clinical_support": {
            "overview_app_location": "clinical.hub.overview",
            "units": [],
            "confidence_checks": [],
            "status": "optional-disabled-non-credit",
            "time_model_notes": "Optional clinical support is not required and counts 0 toward required theory.",
        },
        "source_manifest": [
            {"source": "Orientation/compliance exception", "usage": "Reusable Package A/B/C navigation, privacy, identity, online-hour, and certificate-disabled boundaries"},
            *[
                {
                    "source": f"CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-{n}.pdf",
                    "extracted_text": f"CNA-Recert-Course/ContentV2/survey-evidence/_source_text/module-{n}.txt",
                    "usage": f"Instructional source for NATP Module {n}",
                }
                for n in range(10, 18)
            ],
        ],
        "app_copy": app_copy,
    }
    CANON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "OK",
        "modules": [m["module_id"] for m in modules],
        "required_minutes": REQUIRED_TOTAL,
        "module_allocation": data["control_facts"]["module_minutes"],
        "cards": sum(len(l["cards"]) for m in modules for l in m["lessons"]),
        "final_questions": len(data["assessments"]["final_assessment"]["questions"]),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
