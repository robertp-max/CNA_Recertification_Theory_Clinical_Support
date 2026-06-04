"""author_m04_from_cccco.py

Rebuild M04 delivery content from approved CCCCO/NATP source evidence.

Scope:
  - Canonical JSON only: ContentV2/data/courseContentV2.json
  - Module only: M04 (Mobility, Falls, and Workplace Safety)
  - Sources:
      CCCCO Module 14: Rehabilitative Nursing
      CCCCO Module 12: Emergency Procedures
      CCCCO Module 13: Long Term Care Resident (musculoskeletal/aging/fall-risk only)

The script adds source-supported depth without inventing content, padding, or
implying hands-on competency validation. CNA role remains observe, assist as
directed, follow the care plan, report, document, and escalate.
"""
from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CANON = ROOT / "CNA-Recert-Course" / "ContentV2" / "data" / "courseContentV2.json"

MODULE_ID = "M04"
MODULE_TITLE = "Mobility, Falls, and Workplace Safety"
CONTENTV1 = "CNA-Recert-Course/Content/theory/modules/26_THEORY_MODULE_04_MOBILITY_FALLS_WORKPLACE_SAFETY_FULL.md"
SME_FLAG = "None identified"
COMPLIANCE_FLAG = (
    "Compliance review required; keep CNA role within observe, assist as directed, follow the care plan, "
    "report, document, and escalate. Online theory does not validate hands-on competency or clinical-hour credit."
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


def loc(lesson_id: str, card_id: str) -> str:
    return f"module.m04.lesson.{lesson_id.lower()}.card.{card_id.lower()}"


def media(location: str, title: str) -> dict:
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
        "negative_prompt": "No PHI, no real patient records, no readable charts, no facility names, no gore, no unsafe clinical actions, no plastic-looking people.",
        "alt_text": f"Training visual: {title}. De-identified illustration; no PHI.",
        "media_status": "placeholder-pending",
        "asset_path": f"/assets/media/{location}.png",
        "required_for_mvp": False,
        "phi_safety_note": "No real patient/resident identifiers or facility data.",
        "status": "Placeholder only - no media generated.",
    }


def quality_meta(*, source_reference: str, source_module_number: str, source_topic: str,
                 transformation_type: str, unique_learning_value: str,
                 why_this_card_exists: str, not_duplicate_of: str,
                 survey_evidence_status: str, source_confidence: str = "high") -> dict:
    return {
        "unique_learning_value": unique_learning_value,
        "source_reference": source_reference,
        "source_module_number": source_module_number,
        "source_topic": source_topic,
        "source_confidence": source_confidence,
        "transformation_type": transformation_type,
        "why_this_card_exists": why_this_card_exists,
        "not_duplicate_of": not_duplicate_of,
        "survey_evidence_status": survey_evidence_status,
    }


def base_card(lesson: dict, card_id: str, title: str, text: str, meta: dict) -> dict:
    location = loc(lesson["lesson_id"], card_id)
    sec = narration_seconds(text)
    return {
        "module_id": MODULE_ID,
        "module_title": MODULE_TITLE,
        "lesson_id": lesson["lesson_id"],
        "lesson_title": lesson["lesson_title"],
        "card_id": card_id,
        "card_type": "delivery",
        "app": {"location": location},
        "display_title": title,
        "learner_facing_content": text,
        "learning_goal": lesson.get("learning_goal", "Apply source-supported CNA theory within scope."),
        "cna_practice_example": "Apply this teaching during routine CNA observation, assisting as directed, reporting, documentation, and resident support while staying within scope.",
        "why_it_matters": [
            "Supports safe CNA judgment within scope of practice.",
            "Builds audit-ready completion evidence for required online theory only.",
            "Preserves compliance boundaries: no PHI, no clinical-hour credit, certificate production disabled.",
        ],
        "key_terms": [],
        "completion_condition": "Learner views this card and continues through the lesson sequence.",
        "narration_script": text,
        "transcript_text": text,
        "estimated_narration_seconds": sec,
        "estimated_word_count": words(text),
        "target_duration_status": target_status(sec),
        "media_prompt_placeholder": media(location, title),
        "status": "draft",
        "sme_review_flag": SME_FLAG,
        "compliance_review_flag": COMPLIANCE_FLAG,
        "internal_challenge": None,
        "debrief_rationale": None,
        **meta,
    }


def refresh_non_delivery(card: dict, lesson: dict, default_meta: dict) -> dict:
    out = deepcopy(card)
    out["status"] = out.get("status") or "draft"
    out["sme_review_flag"] = SME_FLAG
    out["compliance_review_flag"] = COMPLIANCE_FLAG
    for key, value in default_meta.items():
        out[key] = value
    if out.get("card_type") == "overview":
        out["unique_learning_value"] = f"Introduces the {lesson['lesson_title']} source-supported lesson sequence and scope boundaries."
        out["why_this_card_exists"] = "Frames the lesson before delivery, practice challenge, and debrief/remediation."
        out["not_duplicate_of"] = "Delivery cards; overview orients rather than teaches source details."
        out["transformation_type"] = "lesson-orientation"
    if out.get("card_type") in ("challenge", "debrief"):
        out["survey_evidence_status"] = default_meta["survey_evidence_status"] + "; practice/remediation evidence"
    if out.get("media_prompt_placeholder"):
        out["media_prompt_placeholder"]["app_location"] = out["app"]["location"]
    return out


LESSON_SPECS = {
    "L01": [
        {
            "title": "Why Alignment Protects the Body",
            "topic": "Body alignment and musculoskeletal function",
            "source": "CCCCO Module 13, Objective 7, Musculoskeletal System anatomy/functions; CCCCO Module 14, Objective 8 preventive methods",
            "module": "13/14",
            "status": "M13.7/M14.8 body mechanics context improved",
            "text": "CCCCO Module 13 explains that bones give the body shape, protect internal organs, store minerals, and form the framework that supports movement. Joints allow movement, and muscles move body parts, maintain posture, and produce body heat. CCCCO Module 14 lists body alignment as a method to prevent complications from inactivity.\n\nFor CNA practice, body mechanics are not just about protecting your back. Correct alignment protects the resident's joints, breathing, circulation, skin, and comfort. Before assisting, check the care plan, ask for help when needed, keep the resident aligned, and stop if pain, dizziness, weakness, or unsafe positioning appears.",
            "value": "Connects body mechanics to musculoskeletal function and resident safety.",
            "why": "Repairs M04/L01 under-depth with source-supported rationale rather than repeating generic lifting rules.",
            "notdup": "Aging musculoskeletal and fall-risk cards; this card focuses on alignment and body function.",
        },
        {
            "title": "Aging, Strength, and Injury Risk",
            "topic": "Aging musculoskeletal changes",
            "source": "CCCCO Module 13, Objective 8, Musculoskeletal/Nervous System aging changes",
            "module": "13",
            "status": "M13.8 mobility/fall-risk portion improved",
            "text": "CCCCO Module 13 describes aging changes that directly affect safe movement. Muscles weaken and lose tone, muscle mass decreases, joints become less flexible and stiffer, bones lose minerals and become more brittle, posture may become stooped, and reflexes may decrease. Slower nerve transmission can also reduce coordination and balance.\n\nThese changes do not mean a resident cannot move safely. They mean the CNA must move deliberately, allow extra time, use assigned assistive devices, keep paths clear, protect from falls, and avoid sudden pulling or twisting. Handle gently, especially when osteoporosis, fracture history, pain, or weakness is present.",
            "value": "Adds source-supported aging context for mobility and workplace-safety decisions.",
            "why": "Explains why older residents need slower, care-plan-guided assistance.",
            "notdup": "Fall prevention environment card; this card focuses on body changes.",
        },
        {
            "title": "Complications of Inactivity",
            "topic": "Inactivity complications",
            "source": "CCCCO Module 14, Objective 8, Content Outline A",
            "module": "14",
            "status": "M14.8 Covered; M04/L01 expanded",
            "text": "CCCCO Module 14 lists many complications of inactivity: stress, depression, behavior and sleep changes, stasis pneumonia or atelectasis, thrombophlebitis, pulmonary embolism, contractures, osteoporosis, muscle atrophy, pressure sores, constipation, decreased appetite, urinary complications, loneliness, and depression.\n\nA CNA does not diagnose these complications, but CNAs often notice early warning signs: less participation, shortness of breath, cough, pain, swelling, skin change, constipation, poor appetite, toileting changes, or new sadness and withdrawal. Report changes promptly so the nurse and care team can respond.",
            "value": "Adds the CCCCO inactivity complication list and observable CNA cues.",
            "why": "Turns body mechanics into resident-outcome prevention, not just worker safety.",
            "notdup": "Prevention methods card; this card focuses on what inactivity can cause.",
        },
        {
            "title": "Preventing Inactivity Complications",
            "topic": "Preventive methods from restorative source",
            "source": "CCCCO Module 14, Objective 8, Content Outline B",
            "module": "14",
            "status": "M14.8 Covered; M04/L01 expanded",
            "text": "The CCCCO preventive methods include turning and repositioning, turn-cough-deep-breathing exercises as directed, body alignment, range of motion, supportive devices, skin care, encouraging independence, toileting, bowel and bladder training, elastic stockings, and ambulation.\n\nAmbulation is identified as especially helpful because it maintains muscles and bones, moves joints, reduces pressure on the skin, increases circulation, supports respiratory and heart function, improves bowel and bladder function, and promotes independence and self-esteem. If a resident cannot walk, standing or transferring to a chair may still be part of the care plan.",
            "value": "Adds specific source-supported prevention methods and why ambulation matters.",
            "why": "Provides source-backed prevention depth without creating a hands-on skills sign-off.",
            "notdup": "Complications card; this card focuses on prevention steps.",
        },
        {
            "title": "Pain, Arthritis, and Fracture Clues",
            "topic": "Musculoskeletal observations",
            "source": "CCCCO Module 13, Objective 7, Musculoskeletal diseases/disorders",
            "module": "13",
            "status": "M13.7 musculoskeletal portion improved",
            "text": "CCCCO Module 13 lists arthritis signs such as joint pain, deformity, swelling, tenderness, heat at the inflamed site, and fatigue. Fracture signs vary, but can include pain, swelling, bruising, exposed bone in a compound fracture, immobility of the affected area, and deformity. Osteoporosis can lead to fracture from little or no trauma, often in the hip or low back.\n\nCNA actions stay in scope: report pain, protect alignment, avoid forcing movement, use gentle handling, and follow the care plan or nurse direction for splints, braces, mechanical lifts, or positioning. Do not diagnose the condition or decide a resident is safe to move after a fall.",
            "value": "Adds source-supported musculoskeletal warning signs and scope boundaries.",
            "why": "Builds workplace safety judgment around when movement may be unsafe.",
            "notdup": "Fall prevention post-fall card; this card focuses on musculoskeletal clues before/during care.",
        },
        {
            "title": "CNA Workplace Safety Boundaries",
            "topic": "Care-plan guided assistance and escalation",
            "source": "CCCCO Module 14, Objectives 5, 8, and 10; ContentV1 M04 body mechanics",
            "module": "14",
            "status": "M14.5/M14.8/M14.10 applied to M04/L01",
            "text": "CCCCO Module 14 repeatedly anchors CNA work in the care plan: follow instructions of the immediate supervisor, implement rehabilitative measures as ordered, use equipment and devices appropriately, and report significant changes. Workplace safety starts with that boundary.\n\nDo not improvise a transfer, lift, ROM exercise, or device use because you are in a hurry. If the resident is heavier than expected, weaker than usual, dizzy, confused, in pain, unable to follow directions, or missing assigned equipment, stop and get help. Protect the resident, protect yourself, report the concern, and document according to facility policy.",
            "value": "Explicitly connects body mechanics to care-plan/supervisor boundaries.",
            "why": "Prevents unsafe interpretation that online theory validates independent transfer decisions.",
            "notdup": "Transfer-specific cards; this card focuses on global workplace safety boundaries.",
        },
    ],
    "L02": [
        {
            "title": "Readiness for Mobility Assistance",
            "topic": "Assessing readiness for independence",
            "source": "CCCCO Module 14, Objective 10, Content Outline A",
            "module": "14",
            "status": "M14.10 improved from Partial toward Covered",
            "text": "Before mobility assistance, CCCCO Module 14 says to consider whether the resident can be more independent by checking physical strength and ability, available special training, assistive devices, financial resources, cognitive ability, and motivation. In CNA practice, you do not perform a formal therapy assessment, but you do observe readiness and follow the care plan.\n\nAsk: Can the resident follow directions today? Is the assigned device present? Is the resident weaker, dizzy, short of breath, in pain, or more confused than usual? Can the resident sit steadily or stand briefly as directed? If readiness changes, report before proceeding.",
            "value": "Adds source-supported mobility readiness checks before transfers/ambulation.",
            "why": "Deepens M04/L02 beyond procedure steps and reinforces observe/report boundaries.",
            "notdup": "Device and transfer-boundary cards; this card focuses on readiness.",
        },
        {
            "title": "Transfer Safety and Help Requirements",
            "topic": "Transfer procedure boundaries",
            "source": "CCCCO Module 14, Objective 10, Content Outline B",
            "module": "14",
            "status": "M14.10 improved from Partial toward Covered",
            "text": "The CCCCO source directs staff to follow facility policy on lifting and transferring. It also identifies situations needing extra caution, including residents over 100 pounds, osteoporosis, and transfers requiring team lift or mechanical assistance. The safest rule is to use the care plan and facility policy, not guesswork.\n\nIf the resident cannot assist as expected, if equipment is missing, if the lift plan is unclear, or if you feel unsafe, stop and get help. Do not drag, twist, rush, or perform a transfer alone when the plan calls for help. A delayed transfer is safer than an unsafe transfer.",
            "value": "Adds explicit source-supported transfer safety thresholds and stop points.",
            "why": "Prevents online theory from being interpreted as permission for unsupervised transfers.",
            "notdup": "Readiness card; this card focuses on help requirements and policy boundaries.",
        },
        {
            "title": "Gait Belt and Ambulation Checks",
            "topic": "Ambulation procedures",
            "source": "CCCCO Module 14, Objective 10, Content Outline B",
            "module": "14",
            "status": "M14.10 improved from Partial toward Covered",
            "text": "CCCCO Module 14 includes gait training, self-transfer training, use of a gait belt for ambulation, and checking whether the resident can sit unassisted and steadily and stand a few seconds alone. These are care-plan-guided activities, not independent CNA decisions.\n\nBefore ambulation, verify the assignment, the device, footwear, pathway, and resident readiness. During ambulation, stay close, watch balance and fatigue, and be ready to call for help. Afterward, report changes such as dizziness, pain, shortness of breath, new weakness, near-fall, or inability to complete the usual distance.",
            "value": "Adds source-supported ambulation checks and reportable changes.",
            "why": "Improves M04/L02 active decision depth around ambulation.",
            "notdup": "Transfer card; this card focuses on walking/ambulation.",
        },
        {
            "title": "Assistive Devices for Mobility",
            "topic": "Mobility and assistive devices",
            "source": "CCCCO Module 14, Objective 10, Content Outline C-D",
            "module": "14",
            "status": "M14.10 improved from Partial toward Covered",
            "text": "CCCCO Module 14 lists assistive devices used to promote mobility and independence: cane, walker, wheelchair, transfer board, braces, splints, prostheses, service animals, Braille, and wheelchair-access modifications. The device is part of the care plan; the CNA supports proper use as assigned.\n\nObserve whether the resident uses the device as taught, whether the device is in reach, damaged, poorly fitted, or creating rubbing or pressure, and whether the resident is suddenly unsafe with it. Report device problems rather than substituting equipment or changing the plan independently.",
            "value": "Adds the CCCCO device list and CNA observation responsibilities.",
            "why": "Closes a mapped partial gap for mobility/ambulation devices.",
            "notdup": "Adaptive-device card in restorative lesson; this card focuses on mobility devices.",
        },
        {
            "title": "Visual Impairment and Environment Support",
            "topic": "Mobility with physical/visual impairment",
            "source": "CCCCO Module 14, Objective 10, Content Outline C-D",
            "module": "14",
            "status": "M14.10 improved from Partial toward Covered",
            "text": "The CCCCO source includes visual impairment supports such as service animals, Braille, and environmental modifications. For a resident with visual impairment, safe mobility often depends on consistent placement, clear pathways, verbal orientation, and respecting the resident's trained routines.\n\nDo not move personal items, assistive devices, call lights, or furniture without considering the resident's orientation and care plan. Announce yourself, explain what you are doing, keep paths clear, and report hazards or new difficulty finding objects, following directions, or moving safely.",
            "value": "Adds source-supported visual-impairment mobility context.",
            "why": "Prevents mobility teaching from focusing only on walkers and wheelchairs.",
            "notdup": "Assistive-device card; this card focuses on visual impairment and environmental consistency.",
        },
        {
            "title": "Osteoporosis and Fracture Precautions",
            "topic": "Osteoporosis/fracture transfer risk",
            "source": "CCCCO Module 13, Objective 7, Osteoporosis and Fractured Hip duties/observations",
            "module": "13",
            "status": "M13.7 musculoskeletal/fall-risk portion improved",
            "text": "CCCCO Module 13 describes osteoporosis as lost bone mass that leaves bones porous, spongy, and easily fractured. It notes that fractures can occur from little or no trauma, and that fractured hip is often related to falling and osteoporosis. CNA care emphasizes preventing further fractures, reporting pain, gentle handling, ordered splints or braces, mechanical lift when required, and gentle positioning.\n\nIf a resident falls, has severe hip or knee pain, cannot get up, has a shortened or externally rotated leg, or has swelling/bruising after movement, do not move the resident unless directed for immediate safety. Call for the nurse and follow facility emergency policy.",
            "value": "Adds source-supported osteoporosis/fracture precautions to transfer decisions.",
            "why": "Connects M13 musculoskeletal fall-risk context directly to M04 mobility safety.",
            "notdup": "Fall post-fall card; this card focuses on transfer/handling precautions.",
        },
        {
            "title": "When Ambulation Must Stop",
            "topic": "Escalation during mobility assistance",
            "source": "CCCCO Module 14, Objectives 5 and 10; CCCCO Module 13 musculoskeletal observations",
            "module": "13/14",
            "status": "M14.10/M13.7 applied to M04/L02",
            "text": "Stop mobility assistance and get help if the resident becomes dizzy, weak, short of breath, pale, sweaty, confused, has chest pain, has new one-sided weakness, complains of severe joint or hip pain, loses balance, or can no longer follow directions. These signs may signal a change of condition or an unsafe transfer.\n\nStay with the resident, protect from injury, call for assistance, and report exactly what changed. Document according to facility policy. Do not continue walking just to finish the task, and do not promise the resident that everything is fine when a nurse needs to assess.",
            "value": "Adds a clear stop-and-escalate decision rule for ambulation.",
            "why": "Builds practical judgment from CCCCO observation and mobility source material.",
            "notdup": "Readiness card; this card focuses on in-progress escalation.",
        },
    ],
    "L03": [
        {
            "title": "Restorative Care Promotes Potential",
            "topic": "Rehabilitation/restorative care purpose",
            "source": "CCCCO Module 14, Objectives 2 and 3, Content Outline A-B",
            "module": "14",
            "status": "M14.2/M14.3 Covered; M04/L03 expanded",
            "text": "CCCCO Module 14 states that restorative or rehabilitative care helps people return to the highest possible level of physical and psychological functioning and promotes independence. It helps residents adjust to disability, emphasizes abilities, supports new and retained skills, prevents decline, and prevents complications.\n\nFor CNA practice, this means the goal is not to do everything for the resident as quickly as possible. The goal is to support the resident's highest safe ability within the care plan. Encourage what the resident can do, praise progress, and report barriers or decline to the nurse or restorative team.",
            "value": "Adds source-supported restorative-care purpose and mindset.",
            "why": "Deepens M04/L03 beyond ROM mechanics.",
            "notdup": "Team and ADL cards; this card focuses on restorative purpose.",
        },
        {
            "title": "The Rehabilitation Team and CNA Role",
            "topic": "Rehabilitation team and CNA responsibilities",
            "source": "CCCCO Module 14, Objective 4, Content Outline A-C",
            "module": "14",
            "status": "M14.4 improved from Partial to Covered",
            "text": "CCCCO Module 14 lists the rehabilitation team as the resident, family, CNA, licensed nursing staff, physical therapist, occupational therapist, speech therapist, physician, activity leader, social worker, clergy, and dietitian. The team evaluates function, establishes care-plan goals, adjusts the plan, and works toward the resident's optimal function.\n\nThe CNA role is to participate in care planning when assigned, observe and report responses to care, follow the care plan, encourage the resident to follow the rehabilitation plan, and report early signs of complications. The CNA does not independently create or change the therapy plan.",
            "value": "Adds the full team/purpose list and CNA team responsibilities.",
            "why": "Closes the M14.4 partial gap while preserving scope boundaries.",
            "notdup": "Care-plan documentation card; this card focuses on team membership and role.",
        },
        {
            "title": "Promoting Self-Care and ADLs",
            "topic": "Self-care responsibilities and ADLs",
            "source": "CCCCO Module 14, Objectives 5 and 6, Content Outline A-B",
            "module": "14",
            "status": "M14.5/M14.6 Covered; M04/L03 expanded",
            "text": "CCCCO Module 14 says CNA responsibilities include protecting rights, ensuring safety and privacy, using therapeutic communication, following supervisor instructions and the plan of care, reporting significant changes, implementing ordered rehabilitative measures, encouraging independence, praising even small accomplishments, providing reassurance, and focusing on abilities.\n\nADLs include grooming, dressing, eating, hygiene, elimination, mobility and ambulation, self-turning, and positioning. A CNA supports independence by breaking tasks into safe steps, offering cues, allowing time, and helping only as much as needed under the care plan.",
            "value": "Adds source-supported self-care duties and ADL examples.",
            "why": "Strengthens M04/L03 restorative-care application without duplicating M05 ADL mention.",
            "notdup": "Restorative purpose card; this card focuses on practical self-care duties.",
        },
        {
            "title": "Comfort and Adaptive Devices",
            "topic": "Comfort/adaptive devices and purposes",
            "source": "CCCCO Module 14, Objective 7, Content Outline A-B",
            "module": "14",
            "status": "M14.7 improved from Partial to Covered",
            "text": "CCCCO Module 14 lists comfort devices such as footboards to prevent plantar flexion, trochanter rolls to prevent external rotation and pressure sores, hard splints to prevent contractures, bed cradles to prevent foot drop, trapezes to strengthen muscles and facilitate movement, heel and elbow protectors to reduce friction and breakdown, special mattresses and pads to protect pressure points, pillows for support and positioning, and cast or traction alignment supports.\n\nIt also lists adaptive devices such as cuffed utensils, plate guards, long-handled combs, button hooks, sock pullers, reachers, telephone holders, communication boards, artificial limbs, casts, and splints. Use only assigned devices as directed and report poor fit, rubbing, pain, skin changes, or refusal.",
            "value": "Adds device names, purposes, and CNA observation boundaries.",
            "why": "Closes the M14.7 partial device-catalog gap.",
            "notdup": "Mobility assistive-device card; this card focuses on comfort/adaptive/self-help devices.",
        },
        {
            "title": "ROM Purpose and Types",
            "topic": "Range-of-motion purpose and types",
            "source": "CCCCO Module 14, Objective 9, Content Outline A-D",
            "module": "14",
            "status": "M14.9 Deferred for hands-on performance; theory expanded",
            "text": "Range of motion is movement of joints through their normal range to the point of resistance or discomfort. CCCCO Module 14 states that ROM helps maintain muscle strength, stimulate circulation, maintain body alignment, make positioning easier, prevent thrombophlebitis, and prevent contractures.\n\nThe source distinguishes active ROM, where the resident moves their own joints; passive ROM, where the CNA moves joints through the normal range; and active-assistive ROM, where the CNA helps or the resident uses a resistive device. Online theory explains purpose and distinctions; hands-on ROM remains a clinical skill performed only as trained, assigned, and care-plan directed.",
            "value": "Adds ROM purpose/types while preserving hands-on deferral.",
            "why": "Improves M14.9 theory evidence without claiming competency validation.",
            "notdup": "ROM safety card; this card focuses on purpose and types.",
        },
        {
            "title": "ROM Safety Rules",
            "topic": "Range-of-motion safety",
            "source": "CCCCO Module 14, Objective 9, Content Outline E",
            "module": "14",
            "status": "M14.9 Deferred for hands-on performance; theory expanded",
            "text": "CCCCO Module 14 gives general ROM safety rules: exercise the joint correctly, avoid unnecessary exposure, use good body mechanics, fully support each extremity, move slowly, smoothly, and gently, do not force past resistance or discomfort, do not cause pain, and report pain to the licensed nurse.\n\nA CNA should stop if the resident has pain, guarding, sudden weakness, shortness of breath, dizziness, new swelling, or cannot cooperate safely. Follow the care plan and assignment. Do not add extra exercises or change frequency because it seems helpful.",
            "value": "Adds source-specific ROM safety limits and stop points.",
            "why": "Gives learners safety judgment for deferred ROM skills.",
            "notdup": "ROM purpose card; this card focuses on safety and escalation.",
        },
        {
            "title": "Care Plan Meetings and Restorative Documentation",
            "topic": "Care plan, MDS/RAI, and CNA information",
            "source": "CCCCO Module 14, Objective 12, Content Outline A-G",
            "module": "14",
            "status": "M14.12 Covered; M04/L03 expanded",
            "text": "CCCCO Module 14 explains that the CNA helps team members complete resident assessment information and provides valuable direct-care observations, especially in ADLs. The care plan is reviewed during the interdisciplinary team meeting, where the team discusses interventions and updates information reflecting current function.\n\nThe CNA contribution is practical and specific: what the resident can do, what assistance is needed, what cues work, what devices are used, what changed, and how the resident responds. Document and report according to facility policy so the plan reflects current function.",
            "value": "Adds source-supported care-plan documentation role for restorative care.",
            "why": "Connects M04 restorative work to audit-ready observation/documentation evidence.",
            "notdup": "Rehab team card; this card focuses on care-plan data and documentation.",
        },
        {
            "title": "Self-Esteem, Family, and Progress",
            "topic": "Self-esteem and family involvement",
            "source": "CCCCO Module 14, Objective 11, Content Outline A-B",
            "module": "14",
            "status": "M14.11 improved but remains Partial because broader psychosocial coverage spans M03/M06",
            "text": "CCCCO Module 14 links restorative care with love, belonging, self-esteem, and self-actualization needs. It recommends involving the resident and family in the plan when appropriate, promoting interaction with the rehabilitation team, treating the resident and family with respect and dignity, supporting them, using praise to reinforce progress, encouraging independence, and using a positive approach.\n\nFor CNAs, small words matter. Avoid comparing residents. Praise progress without exaggeration. Include the resident in choices within the care plan. Report discouragement, refusal, or family concerns so the team can adjust support.",
            "value": "Adds psychosocial and family-involvement context to restorative care.",
            "why": "Improves M14.11 evidence within M04 while leaving broader psychosocial mapping honest.",
            "notdup": "Self-care card; this card focuses on motivation, family, and dignity.",
        },
    ],
    "L04": [
        {
            "title": "Why Falls Increase With Aging",
            "topic": "Aging, balance, and fall risk",
            "source": "CCCCO Module 13, Objective 8, Musculoskeletal/Nervous System aging changes",
            "module": "13",
            "status": "M13.8 mobility/fall-risk portion improved",
            "text": "CCCCO Module 13 states that aging can weaken muscles, reduce muscle tone, reduce flexibility, make bones more brittle, stiffen joints, slow movement, reduce reflexes, and slow nerve transmission. These changes can lead to poor coordination and balance and make older adults more prone to injury and falls.\n\nFalls are not just accidents. They often reflect a mismatch between the resident's current ability, the environment, devices, footwear, toileting needs, medications, or illness. A CNA helps by observing changes, keeping the environment safe, following the care plan, and reporting new weakness, dizziness, confusion, pain, or unsteady gait.",
            "value": "Adds source-supported aging/fall-risk rationale.",
            "why": "Deepens fall prevention beyond a generic hazard checklist.",
            "notdup": "Environment and post-fall cards; this card focuses on body changes.",
        },
        {
            "title": "Environment Controls That Prevent Falls",
            "topic": "Fall-prevention environment",
            "source": "CCCCO Module 13, Effects of Aging and Nursing Care Measures handout",
            "module": "13",
            "status": "M13.8 fall-prevention portion improved",
            "text": "The CCCCO aging handout recommends safety measures to prevent falls: remove scatter rugs from the floor, keep paths for ambulation open and free of clutter, and use handrails on walls and in toilets to assist transfers and ambulation. It also emphasizes giving residents time to adjust to position changes and protecting from falls or fainting.\n\nFor CNA practice, keep call lights, mobility devices, footwear, and needed personal items in reach as assigned. Watch for wet floors, clutter, poor lighting, missing handrails, bed or chair height concerns, and pathways blocked by equipment. Fix what is within your assignment and report hazards you cannot correct.",
            "value": "Adds source-specific environmental controls and handrail/pathway guidance.",
            "why": "Repairs M04/L04 under-depth using direct M13 fall-prevention source.",
            "notdup": "Aging fall-risk card; this card focuses on environment.",
        },
        {
            "title": "Position Changes and Fainting Risk",
            "topic": "Slow position changes and syncope prevention",
            "source": "CCCCO Module 13 aging handout; CCCCO Module 12 syncope signs/role",
            "module": "12/13",
            "status": "M12.2/M13.8 applied to fall prevention",
            "text": "The CCCCO aging handout says older adults may need to move more slowly and should be given time to adjust to position changes. CCCCO Module 12 describes syncope signs such as dizziness, temporary vision changes, pallor, cool moist skin, unsteadiness, possible fall, and weak pulse.\n\nBefore standing or walking a resident, pause and observe. If the resident is dizzy, pale, sweaty, weak, or unsteady, do not push forward. Have the resident sit or lie safely as directed by the situation, call for help, stay with the resident, observe changes, and report to the licensed nurse.",
            "value": "Connects position changes, syncope signs, and fall prevention.",
            "why": "Adds source-supported fall prevention through emergency/distress recognition.",
            "notdup": "Environment card; this card focuses on physiologic fall risk.",
        },
        {
            "title": "Falls, Osteoporosis, and Fractured Hip Warning Signs",
            "topic": "Fall injury/fracture warning signs",
            "source": "CCCCO Module 13, Objective 7, Osteoporosis and Fractured Hip",
            "module": "13",
            "status": "M13.7 musculoskeletal/fall-risk portion improved",
            "text": "CCCCO Module 13 states that osteoporosis makes bones porous and easily fractured and that fractured hip is often related to falling and osteoporosis. Warning signs can include inability to get up after a fall, a shortened and externally rotated affected side, severe hip or knee pain, and edema in the hip, thigh, or groin.\n\nAfter a fall, do not pull the resident up or assume there is no injury because the resident can talk. Keep the resident safe, call the nurse according to facility policy, observe for pain or deformity, and follow directions. Moving an injured resident without direction can worsen harm.",
            "value": "Adds source-specific post-fall fracture warning signs.",
            "why": "Strengthens fall response without inventing emergency protocols.",
            "notdup": "Osteoporosis transfer card; this card focuses on post-fall observations.",
        },
        {
            "title": "Assistive Devices Are Part of the Fall Plan",
            "topic": "Devices, pathways, and falls",
            "source": "CCCCO Module 14, Objective 10; CCCCO Module 13 aging handout",
            "module": "13/14",
            "status": "M14.10/M13.8 applied to fall prevention",
            "text": "Fall prevention often depends on consistent use of the assigned device. CCCCO Module 14 lists canes, walkers, wheelchairs, transfer boards, braces, splints, prostheses, and environmental modifications. CCCCO Module 13 stresses clear pathways and handrails.\n\nThe CNA should check that the assigned device is available, within reach, and not creating a new hazard. Do not swap devices between residents or let a resident walk without an assigned device because the distance seems short. If the resident refuses or misuses the device, report the pattern so the care plan can be reviewed.",
            "value": "Links M14 devices with M13 environmental fall prevention.",
            "why": "Adds a distinct fall-prevention concept around device consistency.",
            "notdup": "Mobility-device card; this card focuses on fall-prevention use.",
        },
        {
            "title": "Reporting a Near-Fall",
            "topic": "Near-fall observation and escalation",
            "source": "CCCCO Module 12, Objective 2 distress signs; CCCCO Module 14, Objective 5 reporting changes",
            "module": "12/14",
            "status": "M12.2/M14.5 applied to fall prevention",
            "text": "A near-fall is evidence. If the resident stumbles, grabs furniture, knees buckle, becomes dizzy, has a sudden gait change, or needs more help than usual, treat it as a change worth reporting. CCCCO Module 14 directs CNAs to report significant changes, and CCCCO Module 12 emphasizes recognizing distress and responding.\n\nDocument what happened objectively: where the resident was, what assistance was being given, what device was used, what the resident said, and what you observed. Do not simply write \"almost fell\" without details. Report promptly so the nurse can reassess risk and update the plan.",
            "value": "Adds active reporting practice for near-falls, not just completed falls.",
            "why": "Builds CNA judgment around early escalation before injury occurs.",
            "notdup": "Post-fall card; this card focuses on near-fall documentation and prevention.",
        },
    ],
    "L05": [
        {
            "title": "Recognizing Distress Early",
            "topic": "Emergency distress signs",
            "source": "CCCCO Module 12, Objective 2, Content Outline A-I",
            "module": "12",
            "status": "M12.2 Assessed; M04/L05 expanded",
            "text": "CCCCO Module 12 lists signs of distress across emergencies: chest pain or pressure, shortness of breath, diaphoresis, cold clammy skin, confusion, fainting, weakness, nausea, irregular pulse, one-sided weakness, aphasia, headache, vision changes, seizure activity, severe bleeding, shock signs, respiratory distress, cyanosis, dyspnea, and anxiety or confusion.\n\nThe CNA does not diagnose the emergency. The CNA recognizes that something is wrong, stays calm, stays with the resident, calls for help, pulls the emergency light when available, observes vital signs or condition as directed, and reports specific signs to the licensed nurse.",
            "value": "Adds a broad CCCCO distress-sign recognition framework.",
            "why": "Deepens M12.2 beyond isolated emergency examples.",
            "notdup": "Specific emergency response cards; this card focuses on early recognition.",
        },
        {
            "title": "General Emergency Response Sequence",
            "topic": "Immediate interventions and CNA role",
            "source": "CCCCO Module 12, Objective 3, Content Outline C",
            "module": "12",
            "status": "M12.3 improved from Partial to Covered",
            "text": "CCCCO Module 12 gives general emergency guidelines: stay calm, call for help, gain assistance from the licensed nurse, remain with the resident, intervene only at the level of competence as directed by the licensed nurse, reassure and calm the resident, and know the location of emergency equipment such as the crash cart or AED.\n\nThis online lesson does not replace CPR or AED training. If CPR, AED, abdominal thrusts, or other skills are required, follow facility policy and only perform tasks for which you are trained and assigned. The theory goal is to recognize, call, protect, report, and follow direction.",
            "value": "Adds source-supported emergency sequence and competency boundary.",
            "why": "Closes M12.3 partial coverage without implying hands-on validation.",
            "notdup": "Choking/seizure/bleeding cards; this card focuses on universal emergency sequence.",
        },
        {
            "title": "Advance Directives and Code Status Boundaries",
            "topic": "Advance directives and DNR awareness",
            "source": "CCCCO Module 12, Objective 3, Content Outline A",
            "module": "12",
            "status": "M12.3 improved from Partial to Covered",
            "text": "CCCCO Module 12 identifies advance directives such as full code, Do Not Resuscitate (DNR), living will, and durable power of attorney for healthcare. These are medical/legal instructions that guide emergency care when a resident cannot make decisions.\n\nA CNA should know facility process for code status information but must not interpret or override orders independently. In an emergency, call for help, follow facility policy, and follow licensed nurse direction. Do not tell families what code status means beyond your role or make promises about what will happen.",
            "value": "Adds emergency-code-status boundary content from M12.",
            "why": "Deepens emergency theory and reduces unsafe CNA interpretation.",
            "notdup": "Emergency response sequence card; this card focuses on directives/code status.",
        },
        {
            "title": "Choking: Causes, Signs, and Deferred Skill",
            "topic": "Choking signs and abdominal thrust boundaries",
            "source": "CCCCO Module 12, Objective 4, Content Outline A-E",
            "module": "12",
            "status": "M12.4 Deferred for hands-on performance; theory expanded",
            "text": "CCCCO Module 12 teaches that choking or airway obstruction can lead to cardiac arrest. Causes include foreign bodies such as poorly chewed meat, the tongue blocking the airway in an unconscious person, small objects, vomitus aspiration, thick mucus, and dentures. Signs include respiratory difficulty, high-pitched sounds, inability to speak or cough, and the universal choking sign of hands at the throat.\n\nAbdominal thrusts are a hands-on emergency skill for a conscious choking victim and remain clinical/skills training, not validated by this online theory. The CNA must recognize signs, call for help, follow facility policy, and perform only skills for which they are trained and assigned.",
            "value": "Adds choking causes/signs while keeping abdominal thrusts deferred.",
            "why": "Improves M12.4 theory evidence without claiming skill competency.",
            "notdup": "Feeding aspiration content in M05; this card focuses on emergency choking response.",
        },
        {
            "title": "Seizure Safety",
            "topic": "Seizure signs and CNA response",
            "source": "CCCCO Module 12, Objective 2, Seizure section",
            "module": "12",
            "status": "M12.2 emergency signs expanded",
            "text": "CCCCO Module 12 describes seizures as interference with normal electrical activity in the brain, with possible mental status change. Signs may include a mild blackout, daydreaming appearance, uncontrolled muscle contractions, head jerking, frothing at the mouth, or loss of bowel and bladder control.\n\nThe CNA role is to assist the resident safely to the ground if needed, note the time, cushion the head, remain calm, call for help, stay with the resident, loosen restrictive clothing or jewelry, move hazards away, and observe. Do not restrain the resident and do not put anything in the resident's mouth.",
            "value": "Adds source-supported seizure-specific safety steps.",
            "why": "Provides a distinct emergency scenario beyond generic call-for-help content.",
            "notdup": "General emergency sequence card; this card focuses on seizure response.",
        },
        {
            "title": "Bleeding, Shock, and Respiratory Distress",
            "topic": "Emergency observations and interim support",
            "source": "CCCCO Module 12, Objective 2, Hemorrhaging/Shock/Respiratory Distress sections",
            "module": "12",
            "status": "M12.2/M12.3 expanded",
            "text": "CCCCO Module 12 lists severe bleeding signs such as spurting, steady flow, slow oozing, coughing bright red blood, coffee-ground vomit, or blood in urine or stool. Shock may include pale cold clammy skin, rapid weak pulse, low or falling blood pressure, shallow or labored respirations, dull eyes, nausea, thirst, confusion, anxiety, restlessness, or collapse. Respiratory distress may include shortness of breath, cyanosis, dyspnea, hyperventilation or hypoventilation, hypoxia, and anxiety or confusion.\n\nCall for help, stay with the resident, use standard precautions for bleeding, keep the resident calm and warm as directed, do not give food or drink when contraindicated, and follow licensed nurse direction.",
            "value": "Adds grouped emergency signs and safe interim CNA actions.",
            "why": "Expands M12 emergency intervention breadth without teaching unsupervised treatment.",
            "notdup": "Choking and seizure cards; this card focuses on bleeding/shock/respiratory distress.",
        },
        {
            "title": "Emergency Codes and Special Considerations",
            "topic": "Long-term care emergency codes",
            "source": "CCCCO Module 12, Objective 5, Content Outline A-C",
            "module": "12",
            "status": "M12.5 Covered; M04/L05 expanded",
            "text": "CCCCO Module 12 lists common emergency codes: Code Red for fire, Code Blue for adult medical emergency, Code Yellow for bomb threat, Code Gray for combative person, Code Silver for a person with a weapon or hostage, and Code Orange for hazardous waste spill or release. It also notes that codes may vary by facility.\n\nKnow your facility's codes, alarms, exits, and emergency equipment locations. Follow the facility plan and pay attention to residents with hearing or vision impairment who may not understand alarms or directions. Your role is to follow instructions, protect residents, communicate clearly, and report hazards.",
            "value": "Adds source-specific code list and sensory-impairment considerations.",
            "why": "Deepens M12.5 beyond a basic code mention.",
            "notdup": "General emergency sequence card; this card focuses on facility codes.",
        },
    ],
}


def make_delivery_cards(lesson: dict) -> list[dict]:
    cards = []
    for idx, spec in enumerate(LESSON_SPECS[lesson["lesson_id"]]):
        card_id = f"C02{chr(ord('A') + idx)}_DELIVERY"
        meta = quality_meta(
            source_reference=spec["source"],
            source_module_number=spec["module"],
            source_topic=spec["topic"],
            source_confidence=spec.get("source_confidence", "high"),
            transformation_type=spec.get("transformation_type", "source-supported expansion"),
            unique_learning_value=spec["value"],
            why_this_card_exists=spec["why"],
            not_duplicate_of=spec["notdup"],
            survey_evidence_status=spec["status"],
        )
        cards.append(base_card(lesson, card_id, spec["title"], spec["text"], meta))
    return cards


def retarget_existing_card(card: dict, lesson: dict) -> dict:
    default_meta = quality_meta(
        source_reference=card.get("source_reference") or f"{CONTENTV1}#{lesson['lesson_id']}",
        source_module_number="12/13/14",
        source_topic=f"{lesson['lesson_title']} practice/remediation",
        source_confidence="high",
        transformation_type="existing practice/remediation with required evidence metadata",
        unique_learning_value=f"Provides practice/remediation evidence for {lesson['lesson_title']}.",
        why_this_card_exists="Maintains the required practice challenge and debrief/remediation sequence for the lesson.",
        not_duplicate_of="Delivery cards; practice/remediation applies rather than introduces source content.",
        survey_evidence_status=f"M04 {lesson['lesson_id']} practice/remediation evidence retained after CCCCO expansion",
    )
    return refresh_non_delivery(card, lesson, default_meta)


def rebuild_lesson(lesson: dict) -> None:
    existing = lesson["cards"]
    overview = next(c for c in existing if c.get("card_type") == "overview")
    challenge = next(c for c in existing if c.get("card_type") == "challenge")
    debrief = next(c for c in existing if c.get("card_type") == "debrief")

    default_meta = quality_meta(
        source_reference=lesson.get("source_reference") or f"{CONTENTV1}#{lesson['lesson_id']}",
        source_module_number="12/13/14",
        source_topic=lesson["lesson_title"],
        source_confidence="high",
        transformation_type="lesson-orientation",
        unique_learning_value=f"Introduces the {lesson['lesson_title']} source-supported lesson sequence and scope boundaries.",
        why_this_card_exists="Frames the lesson before delivery, practice challenge, and debrief/remediation.",
        not_duplicate_of="Delivery cards; overview orients rather than teaches source details.",
        survey_evidence_status=f"M04 {lesson['lesson_id']} overview retained after CCCCO expansion",
    )
    overview = refresh_non_delivery(overview, lesson, default_meta)
    lesson["cards"] = [overview, *make_delivery_cards(lesson), retarget_existing_card(challenge, lesson), retarget_existing_card(debrief, lesson)]
    lesson["status"] = "draft"


def main() -> int:
    data = json.loads(CANON.read_text(encoding="utf-8"))
    module = next(m for m in data["modules"] if m["module_id"] == MODULE_ID)
    before_count = sum(len(l.get("cards", [])) for l in module["lessons"])
    before_active = module.get("estimated_active_learning_minutes")

    module["status"] = "draft"
    module["sme_review_flag"] = SME_FLAG
    module["compliance_review_flag"] = COMPLIANCE_FLAG
    module["source_status_flag"] = "None identified"

    for lesson in module["lessons"]:
        if lesson["lesson_id"] in LESSON_SPECS:
            rebuild_lesson(lesson)

    after_count = sum(len(l.get("cards", [])) for l in module["lessons"])
    CANON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "OK",
        "module": MODULE_ID,
        "prior_card_count": before_count,
        "new_card_count_before_time_model": after_count,
        "prior_estimated_active_learning_minutes": before_active,
        "note": "Run apply_time_model.py next to refresh time fields.",
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
