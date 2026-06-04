"""audit_time_depth.py

Deterministic learner-facing TIME-DEPTH estimator for ContentV2.

Motivation: a lesson displayed as 15 minutes can be completed in ~5 minutes by
playing narration and clicking through. This tool computes a defensible estimate
of actual active-learning time from the canonical data and compares it against the
displayed/declared instructional minutes, so the real content-depth gap is visible
(it does NOT lower displayed labels and does NOT fabricate content).

ESTIMATION MODEL (documented, deterministic)
  Reading pace: 130 words/minute (conservative adult healthcare-training reading).
  Narration:    estimated_narration_seconds / 60.
  Anti-double-count: in ContentV2 a delivery card's narration_script,
    transcript_text and learner_facing_content are largely identical. A learner
    consumes that content ONCE (listen OR read), so a delivery card's consumption
    time = max(narration_minutes, reading_minutes) - NOT their sum. The transcript
    is treated as an audio fallback, never as automatic extra time.
    Per-card active-learning time:
    overview  : clamp(max(narration, reading), 0.5, 1.0)
    delivery  : max(narration, reading) + 0.5 reflection/check + optional
                source_backed_activity_minutes for authored NATP activities
    challenge : clamp(1.5 + words/180, 1.5, 3.0)   (module-level scenario + decide)
    debrief   : clamp(2.0 + words/180, 2.0, 4.0)   (module-level rationale review)
  Assessment time (module + final) is reported SEPARATELY and never added to
  lesson instructional depth. Optional clinical support contributes 0.

Outputs:
  CNA-Recert-Course/ContentV2/qa/TIME_DEPTH_AUDIT.md
  CNA-Recert-Course/ContentV2/qa/time-depth-audit.json
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CANON = ROOT / "CNA-Recert-Course" / "ContentV2" / "data" / "courseContentV2.json"
QA_DIR = ROOT / "CNA-Recert-Course" / "ContentV2" / "qa"

WPM_READ = 130.0

# Scaffolding / internal answer-key phrases that should never be learner-facing.
SCAFFOLD_PHRASES = [
    "On-Screen Text:", "TTS/Transcript-Ready Text:", "Pronunciation Notes:",
    "Correct Answer:", "Correct Feedback:", "Incorrect Feedback",
    "correct_id_internal", "rationale_internal",
]


def words(text: str) -> int:
    return len([w for w in re.split(r"\s+", text or "") if w])


def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def r2(x: float) -> float:
    return round(x, 2)


def card_minutes(card: dict) -> dict:
    ctype = card.get("card_type")
    narr_min = (card.get("estimated_narration_seconds") or 0) / 60.0
    lf = card.get("learner_facing_content") or ""
    wc = words(lf)
    read_min = wc / WPM_READ

    if ctype == "overview":
        active = clamp(max(narr_min, read_min), 0.5, 1.0)
        return {"type": ctype, "wc": wc, "narration": narr_min, "reading": read_min,
                "interaction": 0.0, "challenge": 0.0, "remediation": 0.0, "active": active}
    if ctype == "delivery":
        consumption = max(narr_min, read_min)  # no double-count of identical text
        source_activity = float(card.get("source_backed_activity_minutes") or 0)
        active = consumption + 0.5 + source_activity
        return {"type": ctype, "wc": wc, "narration": narr_min, "reading": read_min,
                "interaction": 0.5 + source_activity, "challenge": 0.0, "remediation": 0.0, "active": active}
    if ctype == "challenge":
        mins = clamp(1.5 + wc / 180.0, 1.5, 3.0)
        return {"type": ctype, "wc": wc, "narration": narr_min, "reading": read_min,
                "interaction": 0.0, "challenge": mins, "remediation": 0.0, "active": mins}
    if ctype in ("debrief", "remediation"):
        rem = card.get("remediation")
        extra = words(json.dumps(rem)) if isinstance(rem, (dict, list)) else 0
        mins = clamp(2.0 + (wc + extra) / 180.0, 2.0, 4.0)
        return {"type": ctype, "wc": wc, "narration": narr_min, "reading": read_min,
                "interaction": 0.0, "challenge": 0.0, "remediation": mins, "active": mins}
    # any other card type: light touch
    active = clamp(max(narr_min, read_min), 0.0, 1.0)
    return {"type": ctype, "wc": wc, "narration": narr_min, "reading": read_min,
            "interaction": 0.0, "challenge": 0.0, "remediation": 0.0, "active": active}


def has_scaffold(card: dict) -> str | None:
    blob = "\n".join(str(card.get(f) or "") for f in ("learner_facing_content", "narration_script", "transcript_text"))
    return next((p for p in SCAFFOLD_PHRASES if p in blob), None)


def assess_minutes(block: dict) -> int:
    return int(block.get("estimated_assessment_minutes", block.get("estimated_minutes") or 0) or 0)


def audit(data: dict) -> dict:
    modules_out = []
    course_displayed = 0.0
    course_active = 0.0
    failing_lessons = 0

    module_assessments = data.get("assessments", {}).get("module_assessments", {})

    for m in data.get("modules", []):
        mid = m["module_id"]
        m_instructional = int(m.get("instructional_minutes") or m.get("estimated_minutes") or 0)
        m_active = 0.0
        m_displayed = 0.0
        m_wc = 0
        lessons_out = []
        lessons_below = []
        is_repair_mod = (m.get("status") == "source-repair")
        module_challenge_count = 0
        module_debrief_count = 0
        module_challenge_minutes = 0.0
        module_remediation_minutes = 0.0

        for l in m.get("lessons", []):
            agg = {"narration": 0.0, "reading": 0.0, "interaction": 0.0, "challenge": 0.0,
                   "remediation": 0.0, "active": 0.0, "wc": 0}
            counts = {"overview": 0, "delivery": 0, "challenge": 0, "debrief": 0}
            scaffold_hits = []
            repair_placeholder = False
            for c in l.get("cards", []):
                cm = card_minutes(c)
                for k in ("narration", "reading", "interaction", "challenge", "remediation", "active"):
                    agg[k] += cm[k]
                agg["wc"] += cm["wc"]
                ct = c.get("card_type")
                if ct in counts:
                    counts[ct] += 1
                if "Source Repair Placeholder" in (c.get("display_title") or ""):
                    repair_placeholder = True
                hit = has_scaffold(c)
                if hit:
                    scaffold_hits.append((c.get("card_id"), hit))

            displayed = float(l.get("estimated_minutes") or 0)
            instructional = float(l.get("instructional_minutes") or l.get("estimated_minutes") or 0)
            active = agg["active"]
            gap = max(0.0, instructional - active)

            # Failure thresholds (lesson)
            reasons = []
            if displayed >= 15 and active < 10:
                reasons.append("displayed>=15min but active<10min")
            if displayed > 0 and active < 0.70 * displayed:
                reasons.append(f"active {r2(active)}min < 70% of displayed {displayed}min")
            if displayed >= 15 and counts["delivery"] < 6:
                reasons.append(f"only {counts['delivery']} delivery cards for {displayed}min")
            if counts["challenge"] or counts["debrief"]:
                if counts["challenge"] != 1 or counts["debrief"] != 1:
                    reasons.append("lesson with module challenge must include exactly one challenge and one debrief")
                elif agg["challenge"] < 1.5 or agg["remediation"] < 2.0:
                    reasons.append("challenge/debrief too thin")
            if scaffold_hits:
                reasons.append(f"scaffolding/answer-key phrase: {scaffold_hits[0][1]}")

            failing = bool(reasons)
            if failing:
                failing_lessons += 1
                lessons_below.append(l["lesson_id"])

            # Source-supported expansion availability (honest):
            # ContentV1 teaching screens are already fully transformed for M01-M06;
            # M03 L03-L05 have no canonical source. So no invent-free expansion remains.
            if repair_placeholder or (is_repair_mod and l["lesson_id"] in ("L03", "L04", "L05")):
                expansion = False
                gap_reason = "No canonical ContentV1 source (truncated/contaminated after Screen 3.2.3); Source Repair Required."
            else:
                expansion = False
            gap_reason = ("NATP source-backed lesson cards and activities are already transformed; "
                          "remaining gap, if any, must be closed only from NATP Modules 10-17 source - not padded.")

            status = l.get("time_model_status") or ("source-repair" if is_repair_mod else "modeled")
            if failing and status not in ("source-repair",):
                status = "under-depth"

            lessons_out.append({
                "module_id": mid,
                "lesson_id": l["lesson_id"],
                "lesson_title": l.get("lesson_title"),
                "displayed_estimated_minutes": displayed,
                "instructional_minutes": instructional,
                "card_count": len(l.get("cards", [])),
                "delivery_card_count": counts["delivery"],
                "challenge_card_count": counts["challenge"],
                "debrief_card_count": counts["debrief"],
                "learner_facing_word_count": agg["wc"],
                "narration_minutes": r2(agg["narration"]),
                "reading_review_minutes": r2(agg["reading"]),
                "interaction_minutes": r2(agg["interaction"]),
                "challenge_minutes": r2(agg["challenge"]),
                "remediation_minutes": r2(agg["remediation"]),
                "estimated_active_learning_minutes": r2(active),
                "content_depth_gap_minutes": r2(gap),
                "time_model_status": status,
                "source_supported_expansion_available": expansion,
                "source_gap_reason": gap_reason,
                "failing": failing,
                "failure_reasons": reasons,
            })
            m_active += active
            m_displayed += displayed
            m_wc += agg["wc"]
            module_challenge_count += counts["challenge"]
            module_debrief_count += counts["debrief"]
            module_challenge_minutes += agg["challenge"]
            module_remediation_minutes += agg["remediation"]

        ma = module_assessments.get(mid, {})
        module_assessment_minutes = assess_minutes(ma)
        m_gap = max(0.0, m_instructional - m_active)
        m_reasons = []
        if m_instructional > 0 and m_active < 0.75 * m_instructional:
            m_reasons.append(f"active {r2(m_active)}min < 75% of declared {m_instructional}min")
        # narration treated as full lesson time?
        m_narr = sum(lo["narration_minutes"] for lo in lessons_out)
        if m_narr >= m_instructional and m_instructional > 0:
            m_reasons.append("narration >= full instructional allocation")
        if mid != "M00" and m_instructional > 0:
            if module_challenge_count != 1 or module_debrief_count != 1:
                m_reasons.append(
                    f"expected exactly one module-level challenge/debrief, found {module_challenge_count}/{module_debrief_count}"
                )
            elif module_challenge_minutes < 1.5 or module_remediation_minutes < 2.0:
                m_reasons.append("module-level challenge/debrief too thin")

        modules_out.append({
            "module_id": mid,
            "module_title": m.get("module_title"),
            "declared_instructional_minutes": m_instructional,
            "displayed_lesson_minutes_sum": r2(m_displayed),
            "estimated_active_learning_minutes": r2(m_active),
            "module_content_depth_gap_minutes": r2(m_gap),
            "module_assessment_minutes_excluded": module_assessment_minutes,
            "lessons_below_threshold": lessons_below,
            "status": m.get("status"),
            "sme_review_flag": m.get("sme_review_flag"),
            "source_status_flag": m.get("source_status_flag"),
            "counts_toward_optional_clinical_support": bool(m.get("counts_toward_optional_clinical_support")),
            "module_challenge_card_count": module_challenge_count,
            "module_debrief_card_count": module_debrief_count,
            "failing": bool(m_reasons),
            "failure_reasons": m_reasons,
            "lessons": lessons_out,
        })
        course_displayed += m_displayed
        course_active += m_active

    fa = data.get("assessments", {}).get("final_assessment", {})
    cs = data.get("clinical_support", {})
    tm = data.get("time_model", {})

    return {
        "model": {
            "reading_wpm": WPM_READ,
            "delivery_active": "max(narration_min, reading_min) + 0.5 reflection (no double-count of identical text)",
            "overview_active": "clamp(max(narration,reading),0.5,1.0)",
            "challenge_active": "clamp(1.5 + words/180,1.5,3.0)",
            "debrief_active": "clamp(2.0 + (words+remediation)/180,2.0,4.0)",
            "assessment": "module + final assessment minutes excluded from lesson depth",
            "clinical_support": "0 toward required theory",
        },
        "required_theory_instructional_minutes_total": tm.get("required_theory_instructional_minutes_total", 720),
        "course_displayed_lesson_minutes": r2(course_displayed),
        "course_estimated_active_learning_minutes": r2(course_active),
        "course_estimated_active_learning_hours": r2(course_active / 60.0),
        "module_assessment_minutes_excluded": tm.get("module_assessment_minutes_excluded"),
        "course_final_assessment_minutes_excluded": assess_minutes(fa),
        "optional_clinical_support_counts_toward_720": bool(cs.get("counts_toward_720_instructional_minutes")),
        "certificate_production_enabled": bool(data.get("certificate", {}).get("production_enabled", False)),
        "failing_lessons": failing_lessons,
        "modules": modules_out,
    }


def write_md(rep: dict) -> None:
    L = []
    L.append("# ContentV2 Time-Depth Audit")
    L.append("")
    L.append("> Deterministic estimate of actual learner-facing active-learning time vs the displayed/declared")
    L.append("> instructional minutes. Displayed labels are NOT lowered and content is NOT fabricated; the gap is")
    L.append("> reported so it can be closed with approved ContentV1 source or kept visible as under-depth.")
    L.append("")
    L.append("## Estimation model")
    for k, v in rep["model"].items():
        L.append(f"- **{k}**: {v}")
    L.append("")
    L.append("## Course totals")
    L.append(f"- Required theory model (declared): **{rep['required_theory_instructional_minutes_total']} min** "
             f"({round(rep['required_theory_instructional_minutes_total']/60,1)} h)")
    L.append(f"- Displayed lesson minutes (sum): **{rep['course_displayed_lesson_minutes']} min**")
    L.append(f"- Estimated active-learning: **{rep['course_estimated_active_learning_minutes']} min "
             f"(~{rep['course_estimated_active_learning_hours']} h)**")
    L.append(f"- Module-assessment minutes excluded: {rep['module_assessment_minutes_excluded']}")
    L.append(f"- Final-assessment minutes excluded: {rep['course_final_assessment_minutes_excluded']}")
    L.append(f"- Optional clinical support counts toward 720: {rep['optional_clinical_support_counts_toward_720']}")
    L.append(f"- Certificate production enabled: {rep['certificate_production_enabled']}")
    L.append(f"- Failing lessons: **{rep['failing_lessons']}**")
    L.append("")
    L.append("## Per-module summary")
    L.append("")
    L.append("| Module | Declared min | Est. active min | Gap min | % of declared | Failing | Status |")
    L.append("|---|---:|---:|---:|---:|:--:|---|")
    for m in rep["modules"]:
        pct = round(100 * m["estimated_active_learning_minutes"] / m["declared_instructional_minutes"]) if m["declared_instructional_minutes"] else 0
        L.append(f"| {m['module_id']} | {m['declared_instructional_minutes']} | {m['estimated_active_learning_minutes']} | "
                 f"{m['module_content_depth_gap_minutes']} | {pct}% | {'YES' if m['failing'] else 'no'} | {m['status']} |")
    L.append("")
    for m in rep["modules"]:
        L.append(f"### {m['module_id']} - {m['module_title']}")
        if m["failure_reasons"]:
            L.append(f"- **Module flags:** {'; '.join(m['failure_reasons'])}")
        if m.get("sme_review_flag") and m["sme_review_flag"] != "None identified":
            L.append(f"- SME flag: {m['sme_review_flag']}")
        if m.get("source_status_flag") and m["source_status_flag"] != "None identified":
            L.append(f"- Source status: {m['source_status_flag']}")
        L.append("")
        L.append("| Lesson | Disp | Instr | Cards | Dlv | Chl | Dbf | Words | Narr | Read | Intr | Chl-m | Rem-m | Active | Gap | Fail | Expand? |")
        L.append("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--:|:--:|")
        for x in m["lessons"]:
            L.append(
                f"| {x['lesson_id']} | {x['displayed_estimated_minutes']} | {x['instructional_minutes']} | "
                f"{x['card_count']} | {x['delivery_card_count']} | {x['challenge_card_count']} | {x['debrief_card_count']} | "
                f"{x['learner_facing_word_count']} | {x['narration_minutes']} | {x['reading_review_minutes']} | "
                f"{x['interaction_minutes']} | {x['challenge_minutes']} | {x['remediation_minutes']} | "
                f"{x['estimated_active_learning_minutes']} | {x['content_depth_gap_minutes']} | "
                f"{'Y' if x['failing'] else ''} | {'Y' if x['source_supported_expansion_available'] else 'N'} |"
            )
        L.append("")
        # source gap reasons for failing lessons
        for x in m["lessons"]:
            if x["failing"]:
                L.append(f"  - {x['lesson_id']} flags: {'; '.join(x['failure_reasons'])}")
                L.append(f"    - source gap: {x['source_gap_reason']}")
        L.append("")
    QA_DIR.mkdir(parents=True, exist_ok=True)
    (QA_DIR / "TIME_DEPTH_AUDIT.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def main() -> int:
    data = json.loads(CANON.read_text(encoding="utf-8"))
    rep = audit(data)
    QA_DIR.mkdir(parents=True, exist_ok=True)
    (QA_DIR / "time-depth-audit.json").write_text(json.dumps(rep, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_md(rep)
    print(json.dumps({
        "status": "OK",
        "course_displayed_lesson_minutes": rep["course_displayed_lesson_minutes"],
        "course_estimated_active_learning_minutes": rep["course_estimated_active_learning_minutes"],
        "course_estimated_active_learning_hours": rep["course_estimated_active_learning_hours"],
        "failing_lessons": rep["failing_lessons"],
        "failing_modules": [m["module_id"] for m in rep["modules"] if m["failing"]],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
