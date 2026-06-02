"""build_survey_evidence.py

Generate CCCCO/NATP survey-readiness evidence for Modules 10-17 from a single
authored crosswalk + the canonical ContentV2 data + the time-depth audit.

It does NOT claim survey approval. It makes coverage, assessment, and gaps
defensible and inspectable: every CCCCO objective is mapped to a ContentV2
lesson location with an honest coverage status, evidence type, depth flag
(from the time-depth audit), and a disposition note.

Inputs (all read-only):
  survey-evidence/_source_text/cccco_objectives.json   (parsed CCCCO objectives)
  data/courseContentV2.json                            (canonical content + assessments)
  qa/time-depth-audit.json                             (honest active-learning depth)

Outputs (survey-evidence/):
  SOURCE_TO_LESSON_MAP.md      + source_to_lesson_map.csv
  COVERAGE_BY_SOURCE_MODULE.md
  ASSESSMENT_EVIDENCE_MAP.md
  CONTENT_GAPS_AND_DISPOSITIONS.md
  SURVEY_READINESS_COVERAGE_SUMMARY.md
  survey_evidence.json         (machine-readable)
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SE = ROOT / "CNA-Recert-Course" / "ContentV2" / "survey-evidence"
CANON = ROOT / "CNA-Recert-Course" / "ContentV2" / "data" / "courseContentV2.json"
AUDIT = ROOT / "CNA-Recert-Course" / "ContentV2" / "qa" / "time-depth-audit.json"
OBJ = SE / "_source_text" / "cccco_objectives.json"

STATUSES = ["Covered", "Assessed", "Partial", "Deferred", "Source Repair", "Out of Scope", "SME Review"]

# ---------------------------------------------------------------------------
# AUTHORED CROSSWALK: (cccco_module, objective_n) -> dict
#   refs:     list of "Mxx/Lyy" ContentV2 lesson references
#   status:   one of STATUSES (conceptual coverage judgement)
#   evidence: short evidence-type phrase
#   note:     disposition rationale (why this status; honest gaps kept visible)
# Hands-on PERFORMANCE of clinical skills is "Deferred" (theory introduces; the
# graded skill belongs to clinical training / Optional Clinical Support and is
# never required to issue the (disabled) certificate).
# ---------------------------------------------------------------------------
CROSSWALK = {
    # ---- CCCCO M10 Vital Signs -> M05 L04/L05 ----
    (10, 1): (["M05/L04"], "Covered", "Theory delivery (key terms)", "Vital-signs terminology taught in M05/L04."),
    (10, 2): (["M05/L04"], "Assessed", "Theory delivery + challenge/debrief", "Meaning/purpose of vital signs and observations taught and exercised in M05/L04 challenge."),
    (10, 3): (["M05/L04"], "Covered", "Theory delivery", "Temperature as an indicator of body function."),
    (10, 4): (["M05/L04"], "Partial", "Theory delivery", "Comfort measures to raise/lower temperature touched; nursing-measure depth limited (expand from CCCCO M10)."),
    (10, 5): (["M05/L04"], "Partial", "Theory delivery", "Pulse sites covered; circulatory-system anatomy depth limited (CCCCO M10 / M13 A&P)."),
    (10, 6): (["M05/L04"], "Covered", "Theory delivery", "Factors affecting pulse and pulse qualities."),
    (10, 7): (["M05/L04"], "Covered", "Theory delivery", "Respiration and factors affecting respiratory rate."),
    (10, 8): (["M05/L04"], "Covered", "Theory delivery", "Observations when measuring respirations."),
    (10, 9): (["M05/L04"], "Partial", "Theory delivery", "Abnormal breathing patterns introduced; pattern catalog (Cheyne-Stokes, etc.) thin (expand from CCCCO M10)."),
    (10, 10): (["M05/L04"], "Deferred", "Deferred to clinical (hands-on)", "TPR as a combined hands-on procedure; theory introduces, performance is a clinical skill."),
    (10, 11): (["M05/L04"], "Partial", "Theory delivery", "How blood pressure is produced introduced; physiology depth limited."),
    (10, 12): (["M05/L04"], "Covered", "Theory delivery", "Factors increasing/decreasing blood pressure."),
    (10, 13): (["M05/L04"], "Deferred", "Deferred to clinical (hands-on)", "Identifying/handling BP equipment parts is a hands-on clinical competency."),
    (10, 14): (["M05/L04"], "Deferred", "Deferred to clinical (hands-on)", "Performing a BP reading is a graded clinical skill; theory introduces the procedure."),
    (10, 15): (["M05/L04", "M05/L05"], "Covered", "Theory delivery", "Pain observation and reporting covered in M05/L04-L05."),
    (10, 16): (["M05/L05", "M06/L02"], "Assessed", "Theory delivery + module check", "Recording vital signs on chart/graph/notes; documentation taught and assessed in M06."),

    # ---- CCCCO M11 Nutrition -> M05 L01/L02 ----
    (11, 1): (["M05/L01"], "Covered", "Theory delivery (key terms)", "Nutrition terminology in M05/L01."),
    (11, 2): (["M05/L01"], "Covered", "Theory delivery", "Body's need for food and fluids."),
    (11, 3): (["M05/L01"], "Partial", "Theory delivery", "Common nutrients and food sources introduced; per-nutrient breadth limited (expand from CCCCO M11)."),
    (11, 4): (["M05/L01"], "SME Review", "Theory delivery", "CCCCO cites 'MyPyramid'; current guidance is MyPlate. SME to confirm modernized framing; not invented here."),
    (11, 5): (["M05/L01"], "Partial", "Theory delivery", "Vegan/vegetarian dietary framing thin; expand from CCCCO M11."),
    (11, 6): (["M05/L01"], "Covered", "Theory delivery", "Nutrition/fluid needs of the elderly."),
    (11, 7): (["M05/L01"], "Assessed", "Theory delivery + module check", "Therapeutic diets and NA responsibilities taught and assessed."),
    (11, 8): (["M05/L02"], "Deferred", "Theory delivery + deferred clinical", "Feeding techniques taught; safe hands-on feeding/positioning is a clinical skill (aspiration prevention covered in M05/L02)."),
    (11, 9): (["M05/L01", "M03/L03"], "Partial", "Theory delivery", "Cultural/religious dietary influences; ties to M03/L03 (cultural respect) which is a source-repair placeholder."),
    (11, 10): (["M05/L02"], "Partial", "Theory delivery", "Alternative nutrition (e.g., tube feeding) at NA observation/scope level only; NAs do not administer."),

    # ---- CCCCO M12 Emergency Procedures -> M04 L05 ----
    (12, 1): (["M04/L05"], "Covered", "Theory delivery (key terms)", "Emergency terminology in M04/L05."),
    (12, 2): (["M04/L05"], "Assessed", "Theory delivery + challenge/debrief", "Signs/symptoms of distress and NA prevent/respond role taught and exercised."),
    (12, 3): (["M04/L05"], "Partial", "Theory delivery", "Immediate interventions introduced; scenario breadth limited (expand from CCCCO M12)."),
    (12, 4): (["M04/L05"], "Deferred", "Theory delivery + deferred clinical", "Choking causes/signs taught; abdominal-thrust performance is a hands-on clinical skill."),
    (12, 5): (["M04/L05"], "Covered", "Theory delivery", "Common LTC emergency codes. (CCCCO notes may be taught with Module 4: Safe Environment.)"),

    # ---- CCCCO M13 Long Term Care Resident -> M03 / M04 / M05 L03 / M02 ----
    (13, 1): (["M03/L01"], "Covered", "Theory delivery (key terms)", "LTC-resident terminology in M03/L01."),
    (13, 2): (["M03/L01", "M03/L03", "M02/L01"], "Partial", "Theory delivery", "Basic human needs (environmental/psychological/social/recreational/spiritual); recreational/spiritual depth thin and partly in M03/L03 placeholder."),
    (13, 3): (["M03/L01"], "SME Review", "Theory delivery", "Community resources for the elderly not substantively covered; SME to confirm scope for recert theory (expand from CCCCO M13 or disposition Out of Scope)."),
    (13, 4): (["M03/L05"], "Source Repair", "Placeholder pending SME", "Special needs (developmental/mental disorders: ID, CP, epilepsy, Parkinson's, mental illness) map to M03/L05, currently a Source Repair placeholder."),
    (13, 5): (["M03/L01", "M03/L02"], "Covered", "Theory delivery", "Alzheimer's/related dementias are the core of M03/L01-L02 (authored)."),
    (13, 6): (["M05/L03"], "Out of Scope", "Disposition", "Body's basic organization/composition (intro A&P). CCCCO 'B' anatomy minimum is clinical-foundational; recert theory addresses applied A&P only (skin in M05/L03). SME to confirm."),
    (13, 7): (["M04/L01", "M04/L03", "M05/L03"], "Partial", "Theory delivery", "Body systems / immobility complications applied in M04 (body mechanics, ROM) and M05/L03 (skin); systematic A&P not the recert-theory focus."),
    (13, 8): (["M03/L01", "M04/L03"], "Partial", "Theory delivery", "Aging changes across body systems addressed in applied form; comprehensive aging-changes catalog thin. (CCCCO SNF/ICF 276C A1/A2/B hour split noted in source.)"),

    # ---- CCCCO M14 Rehabilitative Nursing -> M04 L03 (restorative) ----
    (14, 1): (["M04/L03"], "Covered", "Theory delivery (key terms)", "Restorative-care terminology in M04/L03."),
    (14, 2): (["M04/L03"], "Covered", "Theory delivery", "Restorative care promotes independence/potential."),
    (14, 3): (["M04/L03"], "Covered", "Theory delivery", "Goals of restorative care."),
    (14, 4): (["M04/L03", "M06/L05"], "Partial", "Theory delivery", "Rehabilitation team and NA role; interdisciplinary-team depth limited (also M06/L05 delegation)."),
    (14, 5): (["M04/L03"], "Covered", "Theory delivery", "NA responsibilities promoting self-care."),
    (14, 6): (["M04/L03", "M05/L01"], "Covered", "Theory delivery", "Activities of Daily Living (ADLs)."),
    (14, 7): (["M04/L02", "M04/L03"], "Partial", "Theory delivery", "Comfort/adaptive devices introduced; device catalog/purpose breadth limited."),
    (14, 8): (["M04/L03", "M05/L03"], "Covered", "Theory delivery", "Preventing complications of inactivity/immobility (ROM, skin)."),
    (14, 9): (["M04/L03"], "Deferred", "Theory delivery + deferred clinical", "ROM exercises taught; performing ROM is a hands-on clinical skill."),
    (14, 10): (["M04/L02"], "Partial", "Theory delivery", "Mobility/ambulation devices incl. visual-impairment supports; depth limited (expand from CCCCO M14)."),
    (14, 11): (["M03/L01", "M06/L05"], "Partial", "Theory delivery", "Self-esteem and family involvement in care; psychosocial depth thin."),
    (14, 12): (["M06/L02", "M06/L05"], "Covered", "Theory delivery", "Documentation and NA role in the care-plan meeting."),

    # ---- CCCCO M15 Observation and Charting -> M06 / M05 L05 ----
    (15, 1): (["M06/L01"], "Covered", "Theory delivery (key terms)", "Observation/charting terminology in M06/L01."),
    (15, 2): (["M06/L02"], "SME Review", "Theory delivery", "Medical word-elements (prefix/root/suffix) not emphasized; SME to confirm necessity for recert theory."),
    (15, 3): (["M06/L02"], "Partial", "Theory delivery", "Common medical terms/abbreviations introduced via documentation standards; standardized-abbreviation list thin."),
    (15, 4): (["M06/L01"], "Covered", "Theory delivery", "Definition of observation and the senses used."),
    (15, 5): (["M06/L01"], "Assessed", "Theory delivery + challenge/debrief", "Objective vs subjective observation taught and exercised (core M06/L01)."),
    (15, 6): (["M06/L02"], "Covered", "Theory delivery", "Types of charting documents and their use."),
    (15, 7): (["M06/L02"], "Deferred", "Disposition / facility-specific", "ADL assessment for the MDS is facility/EHR-specific; theory explains purpose, completion is on-the-job. SME to confirm."),
    (15, 8): (["M06/L02"], "Covered", "Theory delivery", "Procedures for recording on the chart (incl. correction/PHI rules in M06)."),

    # ---- CCCCO M16 Death and Dying -> M03 L04 (Source Repair placeholder) ----
    (16, 1): (["M03/L04"], "Source Repair", "Placeholder pending SME", "Death/dying terminology maps to M03/L04, currently a Source Repair placeholder."),
    (16, 2): (["M03/L04"], "Source Repair", "Placeholder pending SME", "Kubler-Ross five stages of grief: M03/L04 placeholder; author from CCCCO M16."),
    (16, 3): (["M03/L04"], "Source Repair", "Placeholder pending SME", "Emotional/spiritual needs of the terminally ill and families: M03/L04 placeholder."),
    (16, 4): (["M03/L04", "M02/L01"], "Partial", "Theory delivery", "Rights of the dying patient/resident overlap resident-rights (M02/L01, authored); dying-specific framing in M03/L04 placeholder."),
    (16, 5): (["M03/L04"], "Source Repair", "Placeholder pending SME", "Signs of approaching death vs biological death: M03/L04 placeholder; author from CCCCO M16."),
    (16, 6): (["M03/L04"], "Source Repair", "Placeholder pending SME", "Care/comfort measures for dying patients/residents: M03/L04 placeholder."),
    (16, 7): (["M03/L04"], "Source Repair", "Placeholder pending SME", "Hospice philosophy/goals and NA role: M03/L04 placeholder; author from CCCCO M16."),
    (16, 8): (["M03/L04"], "Deferred", "Placeholder + deferred clinical", "Postmortem care is a hands-on clinical procedure; M03/L04 theory placeholder pending SME."),

    # ---- CCCCO M17 Patient/Resident Abuse -> M02 (authored, well developed) ----
    (17, 1): (["M02/L01", "M02/L02"], "Covered", "Theory delivery (key terms)", "Abuse terminology in M02/L01-L02."),
    (17, 2): (["M02/L02"], "Assessed", "Theory delivery + challenge/debrief", "Types of elder abuse taught and exercised (core M02/L02)."),
    (17, 3): (["M02/L03"], "Covered", "Theory delivery", "Issues related to elder abuse (signs/symptoms/evidence in M02/L03)."),
    (17, 4): (["M02/L05"], "Assessed", "Theory delivery + module check", "NA role in preventing abuse (boundaries/safety, M02/L05) taught and assessed."),
    (17, 5): (["M02/L04"], "Assessed", "Theory delivery + module check", "NA role in reporting abuse / mandated-reporter duties (M02/L04) taught and assessed."),
}


def load():
    canon = json.loads(CANON.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    objs = json.loads(OBJ.read_text(encoding="utf-8"))
    return canon, audit, objs


def index_canon(canon: dict):
    lessons = {}
    repair_lessons = set()
    module_under = {}
    module_status = {}
    for m in canon["modules"]:
        mid = m["module_id"]
        module_under[mid] = bool(m.get("under_depth"))
        module_status[mid] = m.get("status")
        for l in m.get("lessons", []):
            key = f"{mid}/{l['lesson_id']}"
            loc_prefix = f"module.{mid.lower()}.lesson.{l['lesson_id'].lower()}"
            is_repair = any("Source Repair" in (c.get("display_title") or "") for c in l.get("cards", []))
            lessons[key] = {
                "title": l.get("lesson_title"),
                "app_location_prefix": loc_prefix,
                "instructional_minutes": l.get("instructional_minutes"),
                "estimated_active_learning_minutes": l.get("estimated_active_learning_minutes"),
                "under_depth": bool(l.get("under_depth")),
                "time_model_status": l.get("time_model_status"),
                "placeholder": is_repair,
            }
            if is_repair:
                repair_lessons.add(key)
    return lessons, repair_lessons, module_under, module_status


def build(canon, audit, objs):
    lessons, repair_lessons, module_under, module_status = index_canon(canon)
    ma = canon.get("assessments", {}).get("module_assessments", {})
    fa = canon.get("assessments", {}).get("final_assessment", {})

    rows = []
    for m in objs["modules"]:
        cm = m["cccco_module"]
        for o in m["objectives"]:
            key = (cm, o["n"])
            refs, status, evidence, note = CROSSWALK.get(
                key, ([], "SME Review", "Unmapped", "No crosswalk entry; SME to map.")
            )
            ref_details = []
            any_under = False
            any_placeholder = False
            for r in refs:
                ld = lessons.get(r)
                if ld:
                    ref_details.append({"ref": r, "title": ld["title"], "app_location_prefix": ld["app_location_prefix"],
                                        "under_depth": ld["under_depth"], "placeholder": ld["placeholder"]})
                    any_under = any_under or ld["under_depth"]
                    any_placeholder = any_placeholder or ld["placeholder"]
                else:
                    ref_details.append({"ref": r, "title": "(unresolved)", "app_location_prefix": None,
                                        "under_depth": False, "placeholder": False})
            # module knowledge-check + final-exam evidence for the primary content module
            content_mods = sorted({r.split("/")[0] for r in refs})
            assessed_mods = [cmid for cmid in content_mods if cmid in ma]
            rows.append({
                "cccco_module": cm,
                "cccco_module_title": m["title"],
                "objective_n": o["n"],
                "objective": o["text"],
                "content_v2_refs": refs,
                "ref_details": ref_details,
                "coverage_status": status,
                "evidence_type": evidence,
                "depth_status": ("under-depth" if any_under else "ok"),
                "source_repair_placeholder": any_placeholder,
                "assessed_module_checks": [ma[c]["title"] for c in assessed_mods],
                "assessed_module_locations": [ma[c]["splash_app_location"] for c in assessed_mods],
                "final_exam_pool": bool(fa),
                "note": note,
            })
    return rows, lessons, repair_lessons, module_under, module_status, ma, fa


def summarize(rows):
    by_status = {s: 0 for s in STATUSES}
    for r in rows:
        by_status[r["coverage_status"]] = by_status.get(r["coverage_status"], 0) + 1
    return by_status


# --------------------------- writers --------------------------------------

def w_source_map(rows):
    L = ["# CCCCO/NATP Source-to-Lesson Map (Modules 10-17)", "",
         "> Every CCCCO Module 10-17 performance objective mapped to a ContentV2 lesson",
         "> location with an honest coverage status, evidence type, time-depth flag, and",
         "> disposition note. **This evidence does not claim or guarantee survey approval.**",
         "> `depth_status = under-depth` reflects the deterministic time-depth audit: the",
         "> objective is addressed but the lesson is below its active-learning allocation",
         "> and is queued for source-grounded expansion (no padding).", ""]
    cur = None
    for r in rows:
        if r["cccco_module"] != cur:
            cur = r["cccco_module"]
            L += ["", f"## {r['cccco_module_title']}", "",
                  "| # | Objective | ContentV2 location(s) | Status | Evidence | Depth | Notes |",
                  "|--:|---|---|---|---|---|---|"]
        refs = "<br>".join(f"{d['ref']} {d['title']}" + (" [PLACEHOLDER]" if d["placeholder"] else "")
                           for d in r["ref_details"])
        L.append(f"| {r['objective_n']} | {r['objective']} | {refs} | {r['coverage_status']} | "
                 f"{r['evidence_type']} | {r['depth_status']} | {r['note']} |")
    (SE / "SOURCE_TO_LESSON_MAP.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def w_csv(rows):
    with (SE / "source_to_lesson_map.csv").open("w", newline="", encoding="utf-8") as fh:
        wcsv = csv.writer(fh)
        wcsv.writerow(["cccco_module", "cccco_module_title", "objective_n", "objective",
                       "content_v2_refs", "app_location_prefixes", "coverage_status",
                       "evidence_type", "depth_status", "source_repair_placeholder",
                       "assessed_module_checks", "final_exam_pool", "note"])
        for r in rows:
            wcsv.writerow([
                r["cccco_module"], r["cccco_module_title"], r["objective_n"], r["objective"],
                "; ".join(r["content_v2_refs"]),
                "; ".join(d["app_location_prefix"] or "" for d in r["ref_details"]),
                r["coverage_status"], r["evidence_type"], r["depth_status"],
                r["source_repair_placeholder"], "; ".join(r["assessed_module_checks"]),
                r["final_exam_pool"], r["note"],
            ])


def w_coverage_by_module(rows):
    L = ["# Coverage by CCCCO Source Module (10-17)", "",
         "> Per-source-module coverage rollup. Status counts use the authored crosswalk.",
         "> Survey approval is not claimed or implied.", "",
         "| CCCCO module | Objectives | Covered | Assessed | Partial | Deferred | Source Repair | Out of Scope | SME Review |",
         "|---|--:|--:|--:|--:|--:|--:|--:|--:|"]
    mods = {}
    for r in rows:
        mods.setdefault((r["cccco_module"], r["cccco_module_title"]), []).append(r)
    for (cm, title), rs in sorted(mods.items()):
        c = {s: sum(1 for x in rs if x["coverage_status"] == s) for s in STATUSES}
        L.append(f"| {title} | {len(rs)} | {c['Covered']} | {c['Assessed']} | {c['Partial']} | "
                 f"{c['Deferred']} | {c['Source Repair']} | {c['Out of Scope']} | {c['SME Review']} |")
    L += ["", "## Notes by module", ""]
    for (cm, title), rs in sorted(mods.items()):
        flagged = [x for x in rs if x["coverage_status"] in ("Source Repair", "SME Review", "Out of Scope")
                   or x["depth_status"] == "under-depth"]
        L.append(f"### {title}")
        L.append(f"- Objectives: {len(rs)}; flagged for attention: {len(flagged)}")
        for x in flagged:
            L.append(f"  - Obj {x['objective_n']} [{x['coverage_status']}/{x['depth_status']}]: {x['note']}")
        L.append("")
    (SE / "COVERAGE_BY_SOURCE_MODULE.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def w_assessment(rows, ma, fa):
    L = ["# Assessment Evidence Map", "",
         "> Where CCCCO objectives are exercised by ContentV2 assessments. Module knowledge",
         "> checks and the final exam are tracked SEPARATELY from the 720 instructional",
         "> minutes and never reveal answer keys to learners.", "",
         "## Module knowledge checks", "",
         "| Module | Title | Pass % | Est. min (excluded from 720) | Splash location |",
         "|---|---|--:|--:|---|"]
    for mid, b in ma.items():
        L.append(f"| {mid} | {b.get('title')} | {b.get('pass_percent')} | {b.get('estimated_minutes')} | "
                 f"{b.get('splash_app_location')} |")
    L += ["", "## Final assessment", "",
          f"- Title: {fa.get('title')}",
          f"- Question bank size: {fa.get('question_bank_size')}; attempt size: {fa.get('attempt_size')}; pass %: {fa.get('pass_percent')}",
          f"- Answer-key policy: {fa.get('answer_key_policy')}",
          f"- Estimated minutes (excluded from 720): {fa.get('estimated_assessment_minutes')}",
          "", "## CCCCO objectives with direct assessment evidence", "",
          "| CCCCO obj | Objective | Assessed via | Final pool |", "|---|---|---|:--:|"]
    for r in rows:
        if r["coverage_status"] == "Assessed" or r["assessed_module_checks"]:
            via = "; ".join(r["assessed_module_checks"]) or "(module check)"
            L.append(f"| M{r['cccco_module']}.{r['objective_n']} | {r['objective'][:70]} | {via} | "
                     f"{'Y' if r['final_exam_pool'] else ''} |")
    (SE / "ASSESSMENT_EVIDENCE_MAP.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def w_gaps(rows):
    L = ["# Content Gaps and Dispositions", "",
         "> Honest disposition of every CCCCO 10-17 objective that is not fully covered at",
         "> depth. Gaps are reported, never padded; no invented content. Dispositions:",
         "> **Source Repair** (placeholder pending SME-authored source), **Partial / under-depth**",
         "> (addressed but below allocation; queued for source-grounded expansion),",
         "> **Deferred** (hands-on clinical skill; theory introduces, performance is clinical),",
         "> **Out of Scope** / **SME Review** (scope/currency to be confirmed by SME).", ""]
    buckets = {
        "Source Repair (placeholder pending SME source)": [r for r in rows if r["coverage_status"] == "Source Repair"],
        "Deferred to clinical (hands-on skill)": [r for r in rows if r["coverage_status"] == "Deferred"],
        "Out of Scope (disposition)": [r for r in rows if r["coverage_status"] == "Out of Scope"],
        "SME Review (scope/currency)": [r for r in rows if r["coverage_status"] == "SME Review"],
        "Partial / under-depth (expand from approved source)": [
            r for r in rows if r["coverage_status"] == "Partial" or r["depth_status"] == "under-depth"
        ],
    }
    for name, rs in buckets.items():
        L += [f"## {name}  ({len(rs)})", ""]
        if not rs:
            L += ["- None.", ""]
            continue
        L += ["| CCCCO obj | Objective | ContentV2 | Disposition note |", "|---|---|---|---|"]
        for r in rs:
            refs = "; ".join(r["content_v2_refs"])
            L.append(f"| M{r['cccco_module']}.{r['objective_n']} | {r['objective'][:80]} | {refs} | {r['note']} |")
        L.append("")
    (SE / "CONTENT_GAPS_AND_DISPOSITIONS.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def w_summary(rows, by_status, audit, module_under, module_status):
    total = len(rows)
    addressed = sum(1 for r in rows if r["coverage_status"] in ("Covered", "Assessed", "Partial", "Deferred"))
    L = ["# Survey Readiness Coverage Summary (CCCCO/NATP Modules 10-17)", "",
         "> **This document does NOT claim or guarantee survey/audit approval.** It provides",
         "> defensible, inspectable evidence that all CCCCO Module 10-17 objectives are",
         "> discussed, mapped, or explicitly dispositioned, with honest depth and gap flags.", "",
         "## Objective coverage rollup", "",
         f"- Total CCCCO 10-17 objectives mapped: **{total}**",
         f"- Addressed in ContentV2 theory (Covered/Assessed/Partial/Deferred): **{addressed}**",
         ""]
    L += ["| Coverage status | Count |", "|---|--:|"]
    for s in STATUSES:
        L.append(f"| {s} | {by_status.get(s, 0)} |")
    L += ["", "## Honest depth context (from the time-depth audit)", "",
          f"- Course declared theory model: **{audit.get('required_theory_instructional_minutes_total')} min**",
          f"- Estimated active-learning: **{audit.get('course_estimated_active_learning_minutes')} min "
          f"(~{audit.get('course_estimated_active_learning_hours')} h)**",
          f"- Failing/under-depth lessons: **{audit.get('failing_lessons')}**",
          "- Modules currently under-depth or source-repair (objectives addressed but expansion pending):", ""]
    for mid in sorted(set(list(module_under.keys()))):
        flags = []
        if module_under.get(mid):
            flags.append("under-depth")
        if module_status.get(mid) == "source-repair":
            flags.append("source-repair")
        if flags:
            L.append(f"  - {mid}: {', '.join(flags)}")
    L += ["", "## What is intentionally NOT counted as theory coverage", "",
          "- Hands-on clinical skill performance (TPR, BP technique, ROM, abdominal thrusts,",
          "  postmortem care, hands-on feeding) is **Deferred** to clinical training / Optional",
          "  Clinical Support; theory introduces these but does not grade performance.",
          "- Module knowledge checks and the final exam are tracked separately and excluded",
          "  from the 720 instructional minutes; answer keys are never revealed.",
          "- No CDPH approval is claimed; the production certificate remains disabled; no PHI.",
          "", "## Top survey-readiness actions (honest, source-grounded)", "",
          "1. Author CCCCO M16 (Death & Dying) into M03/L04 (currently a Source Repair",
          "   placeholder) and M03/L03, L05 from the CCCCO source.",
          "2. Expand under-depth M02/M04/M05/M06 objectives marked Partial from CCCCO 10-17.",
          "3. SME to confirm dispositions marked SME Review / Out of Scope (e.g., MyPyramid vs",
          "   MyPlate, MDS specifics, intro A&P scope, community resources).", ""]
    (SE / "SURVEY_READINESS_COVERAGE_SUMMARY.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def main() -> int:
    canon, audit, objs = load()
    rows, lessons, repair_lessons, module_under, module_status, ma, fa = build(canon, audit, objs)
    by_status = summarize(rows)

    SE.mkdir(parents=True, exist_ok=True)
    w_source_map(rows)
    w_csv(rows)
    w_coverage_by_module(rows)
    w_assessment(rows, ma, fa)
    w_gaps(rows)
    w_summary(rows, by_status, audit, module_under, module_status)

    (SE / "survey_evidence.json").write_text(json.dumps({
        "disclaimer": "Evidence mapping only; does not claim or guarantee survey/audit approval.",
        "source_hierarchy": [
            "CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-{10..17}.pdf (highest)",
            "CNA-Recert-Course/Content (crosswalk/implementation)",
            "CNA-Recert-Course/ContentV2/data/courseContentV2.json (runtime target)",
        ],
        "total_objectives": len(rows),
        "status_counts": by_status,
        "source_repair_lessons": sorted(repair_lessons),
        "rows": rows,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps({"status": "OK", "objectives": len(rows), "status_counts": by_status}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
