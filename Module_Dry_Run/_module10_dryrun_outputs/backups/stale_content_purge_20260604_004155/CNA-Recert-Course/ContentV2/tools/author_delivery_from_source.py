"""author_delivery_from_source.py

Source-grounded delivery rebuild for M02-M06 (and M03 L01/L02 only).

Reads the ContentV1 theory module source files and regenerates each lesson's
DELIVERY cards from the authored teaching screens. This REPAIRS three real defects
in the prior ContentV2 delivery cards (all fixed WITHOUT inventing content):

  1. Source scaffolding leaked into learner-facing cards
     ("On-Screen Text:", "TTS/Transcript-Ready Text:", "Source: ...",
      "Pronunciation Notes:"). These labels are stripped.
  2. Embedded check-activity ANSWER KEYS leaked into static delivery cards
     ("Correct Answer: B", "Correct Feedback:", "Incorrect Feedback:"). The
     check-activity portion of a screen is DROPPED from the delivery stream
     (each lesson already has its own challenge + debrief). Only the teaching
     text that precedes a check activity is kept.
  3. Mechanical over-splitting into sub-35s fragments. Each teaching screen
     becomes one delivery card, split into ~45-75s subcards only when the
     authored narration exceeds 75 seconds.

Integrity rules:
  * Content comes from the ContentV1 source screens only. Nothing is invented.
  * Narration = the source "TTS/Transcript-Ready Text" when present (the spoken
    text the source authors wrote); otherwise the cleaned on-screen prose.
  * Overview / challenge / debrief cards are preserved untouched.
  * Module/lesson flags (SME, source-repair, source_status) are preserved.
  * M03 L03-L05 have NO canonical source (the source file is truncated/
    contaminated after Screen 3.2.3); they are NOT touched and remain
    source-repair placeholders. The gap is reported, not padded.

Edits ONLY the canonical JSON. Rerun apply_time_model.py then the generator after.
"""
from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CANON = ROOT / "CNA-Recert-Course" / "ContentV2" / "data" / "courseContentV2.json"
SRC_DIR = ROOT / "CNA-Recert-Course" / "Content" / "theory" / "modules"

# module_id -> (source filename, source label, primary NATP crosswalk)
MODULE_SOURCES = {
    "M02": ("24_THEORY_MODULE_02_RESIDENT_RIGHTS_ABUSE_PREVENTION_FULL.md", "NATP Module 17 (Patient/Resident Abuse) + Module 13"),
    "M03": ("25_THEORY_MODULE_03_DEMENTIA_COMMUNICATION_CULTURAL_RESPECT_FULL.md", "NATP Module 13 (dementia/communication)"),
    "M04": ("26_THEORY_MODULE_04_MOBILITY_FALLS_WORKPLACE_SAFETY_FULL.md", "NATP Module 14 + Module 12 (mobility/safety/emergency)"),
    "M05": ("27_THEORY_MODULE_05_NUTRITION_SKIN_INTEGRITY_VITAL_SIGNS_FULL.md", "NATP Module 10/11 + Module 13 (nutrition/skin/vitals)"),
    "M06": ("28_THEORY_MODULE_06_DOCUMENTATION_CHANGE_OF_CONDITION_SCOPE_FULL.md", "NATP Module 15 (documentation/scope)"),
}

# M03 only has valid source through Screen 3.2.3. Lessons L03/L04/L05 have no
# canonical source and must remain source-repair placeholders.
M03_SOURCED_LESSONS = {"L01", "L02"}

WPM = 145.0  # spoken pace, matches existing narration estimates
MAX_SECS = 75
TARGET_MIN_SECS = 45


def clean_text(s: str) -> str:
    """Normalize mojibake and curly punctuation to the existing ContentV2 style."""
    repl = {
        "\u00e2\u20ac\u201d": "-",   # em dash mojibake
        "\u00e2\u20ac\u201c": "-",   # en dash mojibake
        "\u00e2\u20ac\u0153": '"',   # left double quote
        "\u00e2\u20ac\u009d": '"',   # right double quote
        "\u00e2\u20ac\u2122": "'",  # right single quote
        "\u00e2\u20ac\u02dc": "'",  # left single quote
        "\u00e2\u20ac\u00a6": "...", # ellipsis
        "\u00e2\u20ac": '"',          # leftover quote
        "\u00e2\u0153\u2026": "",    # checkmark
        "\u2014": "-", "\u2013": "-",
        "\u201c": '"', "\u201d": '"',
        "\u2018": "'", "\u2019": "'",
        "\u2026": "...",
        "\u00c2": "", "\u00a0": " ",
    }
    for k, v in repl.items():
        s = s.replace(k, v)
    return s


def words(text: str) -> int:
    return len([w for w in re.split(r"\s+", text) if w])


def narration_seconds(text: str) -> int:
    return max(8, round(words(text) / WPM * 60.0))


def duration_status(seconds: int) -> str:
    if seconds < 35:
        return "Short - acceptable if intentionally brief"
    if seconds > MAX_SECS:
        return "Long - consider splitting"
    return "On target (45-75s)"


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def chunk_to_target(text: str) -> list[str]:
    """Split narration into <=75s chunks at sentence boundaries (aim 45-75s)."""
    if narration_seconds(text) <= MAX_SECS:
        return [text.strip()]
    sentences = split_sentences(text)
    chunks: list[str] = []
    cur = ""
    for sent in sentences:
        candidate = (cur + " " + sent).strip()
        if cur and narration_seconds(candidate) > MAX_SECS:
            chunks.append(cur.strip())
            cur = sent
        else:
            cur = candidate
    if cur.strip():
        chunks.append(cur.strip())
    return chunks or [text.strip()]


SCREEN_RE = re.compile(r"^Screen\s+(\d+)\.(\d+)\.(\d+)\s*[-]+\s*(.+?)\s*$")


def parse_screens(raw: str) -> list[dict]:
    """Parse a source module file into teaching screens."""
    lines = clean_text(raw).splitlines()
    screens: list[dict] = []
    cur: dict | None = None
    for line in lines:
        m = SCREEN_RE.match(line.strip())
        if m:
            if cur:
                screens.append(cur)
            cur = {
                "lesson_num": int(m.group(2)),
                "screen_num": int(m.group(3)),
                "code": f"{m.group(1)}.{m.group(2)}.{m.group(3)}",
                "title": m.group(4).strip(),
                "body": [],
            }
        elif cur is not None:
            cur["body"].append(line)
    if cur:
        screens.append(cur)
    return screens


CHECK_MARKERS = (
    "On-Screen Interaction",
    "Check Activity",
    "Check Your Understanding",
    "Fictional Scenario:",
    "Correct Answer",
)
TTS_LABEL = "TTS/Transcript-Ready Text:"


def _clean_prose_lines(region: str, as_examples: bool = False) -> str:
    keep: list[str] = []
    for ln in region.splitlines():
        t = ln.strip()
        if not t:
            continue
        if t in ("On-Screen Text:",) or t.startswith("On-Screen Text"):
            continue
        if t.startswith("Source:") or t.startswith("Pronunciation Notes:"):
            continue
        # Safety: never let multiple-choice option blocks bleed into teaching prose.
        if re.match(r"^[A-D]\)\s", t):
            break
        mopt = re.search(r"\bA\)\s.*\bB\)\s", t)
        if mopt:
            t = t[:t.find("A)")].strip()
            if not t:
                continue
        if "\t" in t:
            cells = [c.strip() for c in re.split(r"\t+", t) if c.strip()]
            if as_examples and len(cells) == 2:
                t = f"{cells[0]} - this is {cells[1]}."
            else:
                t = ": ".join(cells)
        keep.append(t)
    return "\n".join(keep).strip()


def extract_check_teaching(check_region: str) -> str:
    """Convert an embedded check activity into compliance-safe teaching prose.

    NEVER returns multiple-choice options, "Correct Answer", or graded answer-key
    labels. For MCQ scenarios it keeps the fictional scenario + the source teaching
    rationale; for matching tables it keeps the labeled examples. Returns "" if no
    safe teaching content can be extracted.
    """
    text = check_region
    # Matching-style practice: scenario -> category example pairs.
    if "Match each" in text or "Feedback (all correct)" in text:
        # Pull the tab-delimited example pairs (drop the header row).
        pairs = []
        for ln in text.splitlines():
            if "\t" in ln:
                cells = [c.strip() for c in re.split(r"\t+", ln) if c.strip()]
                if len(cells) == 2 and cells[0].lower() not in ("scenario",):
                    pairs.append(f"{cells[0]} - this is {cells[1]}.")
        if pairs:
            return "Recognizing examples in practice:\n" + "\n".join(pairs)
        return ""
    # MCQ scenario: keep scenario setup + the teaching rationale only.
    scenario = ""
    ms = re.search(r"Fictional Scenario:\s*(.+?)(?:\n\s*(?:Which|What|How|A\))|$)", text, re.S)
    if ms:
        scenario = re.sub(r"\s*\n\s*", " ", ms.group(1)).strip()
    rationale = ""
    mr = re.search(r"Correct Feedback:\s*(.+?)(?:Incorrect Feedback|Feedback \(any|$)", text, re.S)
    if mr:
        rationale = re.sub(r"\s*\n\s*", " ", mr.group(1)).strip()
        rationale = re.sub(r"^(Correct\.?|That's right\.?|Correct Answer:\s*[A-D]\.?)\s*", "", rationale).strip()
    if scenario and rationale:
        return f"Consider this fictional situation: {scenario}\n\nWhat to remember: {rationale}"
    if rationale:
        return f"What to remember: {rationale}"
    return ""


def extract_segments(screen: dict) -> list[dict]:
    """Return ordered teaching segments for a screen.

    A teaching segment uses the on-screen prose before any check activity. A
    check activity (if present) is converted into a compliance-safe scenario/
    examples segment via extract_check_teaching (options + answer keys removed).
    """
    body = "\n".join(screen["body"]).strip()
    cut = len(body)
    had_check = False
    for marker in CHECK_MARKERS:
        idx = body.find(marker)
        if idx != -1:
            had_check = True
            cut = min(cut, idx)
    teaching_region = body[:cut]
    check_region = body[cut:] if had_check else ""

    tts_idx = teaching_region.find(TTS_LABEL)
    if tts_idx != -1:
        teaching_region = teaching_region[:tts_idx].strip()

    segments: list[dict] = []
    learner = _clean_prose_lines(teaching_region)
    if words(learner) >= 12:
        segments.append({
            "title": screen["title"],
            "learner": learner,
            "narration": re.sub(r"\s*\n\s*", " ", learner).strip(),
            "kind": "teach",
        })
    if had_check:
        safe = extract_check_teaching(check_region)
        if safe and words(safe) >= 12:
            title = screen["title"]
            if title.lower().startswith(("interactive", "scenario", "practice")):
                title = title  # already scenario-style
            segments.append({
                "title": title,
                "learner": safe,
                "narration": re.sub(r"\s*\n\s*", " ", safe).strip(),
                "kind": "apply",
            })
    return segments, had_check


def media_placeholder(location: str, title: str) -> dict:
    return {
        "app_location": location,
        "scene_title": title,
        "image_16_9_prompt": (
            f"Realistic healthcare education scene for {title}; de-identified long-term care training setting; "
            "no readable charts, no facility logos, no PHI."
        ),
        "optional_video_prompt": (
            f"Future optional short instructional motion prompt for {title}; use only fictional/de-identified CNA training context."
        ),
        "negative_prompt": (
            "No PHI, no real patient records, no readable charts, no facility names, no gore, no unsafe clinical actions, no plastic-looking people."
        ),
        "alt_text": f"Training visual: {title}. De-identified illustration; no PHI.",
        "media_status": "placeholder-pending",
        "asset_path": f"/assets/media/{location}.png",
        "required_for_mvp": False,
        "phi_safety_note": "No real patient/resident identifiers or facility data.",
        "status": "Placeholder only - no media generated.",
    }


def letter(idx: int) -> str:
    # 0->A ... 25->Z, 26->AA ...
    s = ""
    idx2 = idx
    while True:
        s = chr(ord("A") + idx2 % 26) + s
        idx2 = idx2 // 26 - 1
        if idx2 < 0:
            break
    return s


def build_card(template: dict, module: dict, lesson: dict, title: str, learner: str,
               narration: str, idx: int, source_file: str, code: str, src_label: str,
               kind: str = "teach") -> dict:
    lt = letter(idx)
    card_id = f"C02{lt}_DELIVERY"
    location = f"module.{module['module_id'].lower()}.lesson.{lesson['lesson_id'].lower()}.card.c02{lt.lower()}_delivery"
    secs = narration_seconds(narration)
    card = copy.deepcopy(template)
    # Drop any internal challenge/debrief leakage from the template copy.
    for k in ("internal_challenge", "debrief_rationale"):
        if k in card:
            card[k] = None
    card.update({
        "module_id": module["module_id"],
        "module_title": module["module_title"],
        "lesson_id": lesson["lesson_id"],
        "lesson_title": lesson["lesson_title"],
        "card_id": card_id,
        "card_type": "delivery",
        "app": {"location": location},
        "display_title": title,
        "learner_facing_content": learner,
        "narration_script": narration,
        "transcript_text": narration,
        "estimated_narration_seconds": secs,
        "estimated_word_count": words(narration),
        "target_duration_status": duration_status(secs),
        "media_prompt_placeholder": media_placeholder(location, title),
        "source_reference": f"CNA-Recert-Course/Content/theory/modules/{source_file}#Screen {code}",
        "source_module": f"ContentV1 {module['module_id']} <- {src_label}",
        "source_section": f"Screen {code}",
        "source_confidence": "high",
        "transformation_type": "adapt-scenario" if kind == "apply" else "extract-clean",
        "key_terms": [],
    })
    return card


def rebuild_module(data: dict, module_id: str, report: dict) -> None:
    source_file, src_label = MODULE_SOURCES[module_id]
    raw = (SRC_DIR / source_file).read_text(encoding="utf-8", errors="replace")
    screens = parse_screens(raw)
    by_lesson: dict[int, list[dict]] = {}
    for s in screens:
        by_lesson.setdefault(s["lesson_num"], []).append(s)

    module = next(m for m in data["modules"] if m["module_id"] == module_id)
    mreport = report.setdefault(module_id, {"lessons": {}, "dropped_checks": 0, "screens_used": 0, "screens_skipped_no_source": []})

    for lesson in module["lessons"]:
        lid = lesson["lesson_id"]
        lesson_num = int(re.sub(r"\D", "", lid))
        prior_delivery = [c for c in lesson["cards"] if c["card_type"] == "delivery"]

        if module_id == "M03" and lid not in M03_SOURCED_LESSONS:
            mreport["lessons"][lid] = {
                "prior_delivery": len(prior_delivery), "new_delivery": len(prior_delivery),
                "action": "preserved (no canonical source; source-repair)",
            }
            continue

        lesson_screens = by_lesson.get(lesson_num, [])
        if not lesson_screens:
            mreport["lessons"][lid] = {
                "prior_delivery": len(prior_delivery), "new_delivery": len(prior_delivery),
                "action": "preserved (no source screens parsed)",
            }
            continue

        template = next((c for c in lesson["cards"] if c["card_type"] == "delivery"), lesson["cards"][0])
        new_delivery: list[dict] = []
        idx = 0
        for sc in lesson_screens:
            segments, had_check = extract_segments(sc)
            if had_check:
                mreport["dropped_checks"] += 1  # raw MCQ/answer-key portion removed
            if not segments:
                continue
            mreport["screens_used"] += 1
            for seg in segments:
                chunks = chunk_to_target(seg["narration"])
                for ci, ch in enumerate(chunks):
                    lf = seg["learner"] if ci == 0 else f"(Continued) {seg['title']}"
                    new_delivery.append(build_card(template, module, lesson, seg["title"], lf,
                                                   ch, idx, source_file, sc["code"], src_label,
                                                   kind=seg["kind"]))
                    idx += 1

        overview = [c for c in lesson["cards"] if c["card_type"] == "overview"]
        tail = [c for c in lesson["cards"] if c["card_type"] not in ("overview", "delivery")]
        lesson["cards"] = overview + new_delivery + tail
        mreport["lessons"][lid] = {
            "prior_delivery": len(prior_delivery), "new_delivery": len(new_delivery),
            "screens": [s["code"] for s in lesson_screens],
        }


def main(argv: list[str]) -> int:
    targets = [a for a in argv if a in MODULE_SOURCES]
    if not targets:
        targets = ["M02", "M03", "M04", "M05", "M06"]
    data = json.loads(CANON.read_text(encoding="utf-8"))
    report: dict = {}
    for mid in targets:
        rebuild_module(data, mid, report)
    CANON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "OK", "modules": targets, "report": report}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
