"""author_m05_from_cccco.py

Rebuild M05 delivery content from approved CCCCO/NATP source evidence.

Scope:
  - Canonical JSON only: ContentV2/data/courseContentV2.json
  - Module only: M05 (Nutrition, Skin Integrity, Vital Signs, and Observation)
  - Sources:
      CCCCO Module 10: Vital Signs
      CCCCO Module 11: Nutrition
      CCCCO Module 13: Long Term Care Resident (skin/conditions only)

The script is deliberately conservative: it adds source-supported depth without
inventing content, padding, or changing CNA scope. It preserves M05 SME/source
review flags for skin integrity / pressure injury content.
"""
from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CANON = ROOT / "CNA-Recert-Course" / "ContentV2" / "data" / "courseContentV2.json"

MODULE_ID = "M05"
MODULE_TITLE = "Nutrition, Skin Integrity, Vital Signs, and Observation"
CONTENTV1 = "CNA-Recert-Course/Content/theory/modules/27_THEORY_MODULE_05_NUTRITION_SKIN_INTEGRITY_VITAL_SIGNS_FULL.md"
SME_FLAG = "Skin integrity / pressure injury content requires SME/source review."
COMPLIANCE_FLAG = (
    "Compliance review required; keep CNA role as observe/report, document, follow the care plan, "
    "and escalate to the nurse/supervisor; no independent pressure-injury staging or treatment authority."
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
    return f"module.m05.lesson.{lesson_id.lower()}.card.{card_id.lower()}"


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


def base_card(lesson: dict, card_id: str, card_type: str, title: str, text: str, meta: dict) -> dict:
    location = loc(lesson["lesson_id"], card_id)
    sec = narration_seconds(text)
    return {
        "module_id": MODULE_ID,
        "module_title": MODULE_TITLE,
        "lesson_id": lesson["lesson_id"],
        "lesson_title": lesson["lesson_title"],
        "card_id": card_id,
        "card_type": card_type,
        "app": {"location": location},
        "display_title": title,
        "learner_facing_content": text,
        "learning_goal": lesson.get("learning_goal", "Apply source-supported CNA theory within scope."),
        "cna_practice_example": "Apply this teaching during routine CNA observation, reporting, documentation, and resident support while staying within scope.",
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
        "status": "sme-review",
        "sme_review_flag": SME_FLAG,
        "compliance_review_flag": COMPLIANCE_FLAG,
        "internal_challenge": None,
        "debrief_rationale": None,
        **meta,
    }


def refresh_non_delivery(card: dict, lesson: dict, default_meta: dict) -> dict:
    out = deepcopy(card)
    out.setdefault("status", "sme-review")
    out["sme_review_flag"] = SME_FLAG
    out["compliance_review_flag"] = COMPLIANCE_FLAG
    # Keep existing source when more specific, but add required quality fields.
    for key, value in default_meta.items():
        out[key] = value
    if out.get("card_type") in ("challenge", "debrief"):
        out["survey_evidence_status"] = default_meta["survey_evidence_status"] + "; practice/remediation evidence"
    if out.get("card_type") == "overview":
        out["unique_learning_value"] = f"Introduces the {lesson['lesson_title']} source-supported lesson sequence and scope boundaries."
        out["why_this_card_exists"] = "Frames the lesson before delivery, practice challenge, and debrief/remediation."
        out["not_duplicate_of"] = "Delivery cards; overview orients rather than teaches source details."
        out["transformation_type"] = "lesson-orientation"
    return out


LESSON_SPECS = {
    "L01": [
        {
            "title": "Why Food and Fluids Matter",
            "topic": "Body need for food and fluids",
            "source": "CCCCO Module 11, Objective 2, Content Outline A-C",
            "module": "11",
            "status": "M11.2 Covered; M05/L01 expanded",
            "text": "Food and fluids are not just comfort items. CCCCO Module 11 explains that the body depends on them to provide energy for daily living, promote growth and tissue repair, supply substances that regulate body functions, and meet a basic need for survival.\n\nFor CNA practice, this means poor intake is never just a tray-count problem. A resident who eats very little, refuses fluids, or suddenly changes intake may be showing a nutrition, hydration, swallowing, mood, medication, or illness concern. Your role is to observe intake, encourage ordered foods and fluids, document accurately, and report concerns to the licensed nurse.",
            "value": "Connects nutrition/hydration to body function and CNA observation duties.",
            "why": "Repairs M05/L01 under-depth by adding source-supported rationale for why intake matters.",
            "notdup": "Hydration signs, nutrient food sources, therapeutic diets, cultural preferences.",
        },
        {
            "title": "Common Nutrients and Food Sources",
            "topic": "Nutrients, sources, and functions",
            "source": "CCCCO Module 11, Objective 3, Content Outline A",
            "module": "11",
            "status": "M11.3 improved from Partial to Covered",
            "text": "CCCCO Module 11 lists common nutrients with food sources and functions. Carbohydrates from grains, pastas, breads, cereals, fruits, and vegetables are a main energy source and provide fiber. Proteins from eggs, milk, meat, fish, nuts, poultry, cheese, beans, peanut butter, and soy products support tissue growth and repair. Fats from oils, milk, cream, cheese, meats, butter, and mayonnaise provide energy, help carry vitamins, conserve body heat, and protect internal organs.\n\nVitamins and minerals are found in many foods and help regulate body functions and repair tissue. Dietary fiber from raw fruits, vegetables, whole grains, and cereals adds bulk for normal bowel elimination.",
            "value": "Adds source-specific nutrient groups, food sources, and functions.",
            "why": "Closes a mapped M11.3 partial gap without repeating the existing general nutrient overview.",
            "notdup": "Hydration card and therapeutic diet card; this card focuses on nutrient-source-function mapping.",
        },
        {
            "title": "Food Guidance and Balanced Choices",
            "topic": "MyPlate / food guidance system",
            "source": "CCCCO Module 11, Objective 4, Content Outline A-F",
            "module": "11",
            "status": "M11.4 SME Review retained; source content uses My Plate despite objective wording",
            "text": "The CCCCO Module 11 objective list says My Pyramid, but the content outline teaches the My Plate food guidance system. Because the source has that internal wording difference, this course keeps SME review visible and does not claim a resolved standard.\n\nThe source-supported teaching point is balanced selection: grains, vegetables, fruits, dairy, protein, and oils each have a role. For CNA practice, you do not prescribe a diet or counsel residents independently. You support the ordered diet, notice what is eaten or refused, respect resident preferences within the care plan, and report patterns such as poor intake, frequent refusal, or difficulty chewing and swallowing.",
            "value": "Handles the MyPyramid/MyPlate source inconsistency transparently while teaching CNA boundaries.",
            "why": "Addresses M11.4 without hiding SME review or inventing updated regulatory guidance.",
            "notdup": "Nutrient-source card; this card focuses on the guidance-system/currency issue and CNA scope.",
        },
        {
            "title": "Nutrition and Fluid Needs in Older Adults",
            "topic": "Age-related nutrition and hydration needs",
            "source": "CCCCO Module 11, Objective 6, Content Outline A-B",
            "module": "11",
            "status": "M11.6 Covered; M05/L01 expanded",
            "text": "CCCCO Module 11 identifies several age-related changes that can affect nutrition and fluids. A less active resident may need fewer calories, while digestive disturbances can affect vitamin and mineral needs. Medications may interfere with fluid balance, digestion, and nutrient use. Poor oral hygiene, missing teeth, or ill-fitting dentures can make eating harder. Diminished taste, common diseases, and social isolation can also reduce appetite or nutrient use.\n\nAs a CNA, look for the pattern: meal refusal, poor fluid intake, mouth discomfort, denture problems, isolation, nausea, vomiting, or new difficulty eating. Report these observations rather than assuming the resident is simply being difficult.",
            "value": "Adds source-supported older-adult risk factors beyond generic dehydration signs.",
            "why": "Builds active learning depth for a covered but under-depth objective.",
            "notdup": "Food/fluid rationale card; this card focuses on age-related barriers and reportable patterns.",
        },
        {
            "title": "Fluids, Minimum Intake, and Water Functions",
            "topic": "Fluids and normal body functioning",
            "source": "CCCCO Module 11, Objectives 2 and 3, Content Outline C and Objective 3 item 7",
            "module": "11",
            "status": "M11.2/M11.3 Covered; M05/L01 expanded",
            "text": "CCCCO Module 11 notes that a balanced diet includes enough fluids and gives approximately 1500 milliliters per day as a minimum adult fluid reference unless the care plan restricts fluids. The source also identifies water, juices, and other beverages as fluid sources and states that water is essential for normal body function because chemical reactions in the body take place in water.\n\nFor CNA practice, this supports careful observation. If a resident has force fluids, fluid restriction, thickened liquids, or I&O orders, follow the care plan exactly. Encourage allowed fluids, keep water or ordered beverages in reach when appropriate, document intake accurately, and report poor intake, dark urine, dizziness, confusion, dry mouth, or sudden output changes.",
            "value": "Adds source-specific fluid minimum/context and water-function rationale.",
            "why": "Improves L01 depth with a distinct fluid-function concept rather than repeating dehydration signs.",
            "notdup": "Older-adult nutrition card; this card focuses on fluid amount, water function, and ordered fluid boundaries.",
        },
        {
            "title": "Therapeutic Diets and Texture Orders",
            "topic": "Therapeutic diets and ordered consistencies",
            "source": "CCCCO Module 11, Objective 7, Content Outline A-C",
            "module": "11",
            "status": "M11.7 Assessed; M05/L01 expanded",
            "text": "Therapeutic diets are ordered to meet a resident's health needs. CCCCO Module 11 lists common examples: low sodium, diabetic, low fat, low cholesterol, liquid diets, bland diets, and texture changes such as mechanical soft, pureed, soft, and thickened liquids.\n\nThe CNA responsibility is not to choose the diet. It is to make sure the right tray reaches the right resident, check the diet card or meal ticket, follow specific instructions and allergies, and report problems such as chewing or swallowing difficulty, nausea or vomiting, anorexia, food intolerance, refusal, or poor intake. Do not offer extra food, condiments, or substitutions without checking the order or the licensed nurse.",
            "value": "Separates common diet categories from CNA responsibilities and restrictions.",
            "why": "Deepens M11.7 while reinforcing care-plan and order boundaries.",
            "notdup": "Feeding-assistance cards; this card is about diet orders and tray accuracy.",
        },
        {
            "title": "Food Preferences, Allergies, Culture, and Religion",
            "topic": "Dietary preferences and cultural/religious influences",
            "source": "CCCCO Module 11, Objectives 6 and 9, Content Outline B-C and A-E",
            "module": "11",
            "status": "M11.9 improved from Partial to Covered for dietary-practice objective",
            "text": "CCCCO Module 11 directs CNAs to know allergies, check every tray served, watch for new allergies, and recognize lactose intolerance or food additive allergies such as peanuts, shellfish, and wheat. It also lists factors that affect food choices: likes and dislikes, menus, medical restrictions, culture, and religious beliefs.\n\nThe safest CNA approach is to ask rather than assume. Ask the resident about food preferences and practices when appropriate. If a resident cannot communicate, ask the family according to facility process. Encourage allowed cultural or ethnic foods only if they fit the care plan. Document and report preferences, refusals, and concerns so the nurse and dietary team can respond.",
            "value": "Adds dietary culture/allergy content that was previously thin in M05.",
            "why": "Closes a survey-evidence partial gap using CCCCO M11 dietary-practice source text.",
            "notdup": "Therapeutic diet card; this card focuses on preferences, allergies, and cultural/religious practice.",
        },
        {
            "title": "Vegetarian and Vegan Basics",
            "topic": "Vegetarian and vegan food groups",
            "source": "CCCCO Module 11, Objective 5, Content Outline A-C",
            "module": "11",
            "status": "M11.5 improved from Partial to Covered",
            "text": "CCCCO Module 11 distinguishes vegetarian and vegan dietary patterns. A vegetarian diet excludes meat, including game, slaughter by-products, fish, shellfish, other sea animals, and poultry; variations may include or exclude milk, fish, eggs, and honey. A vegan diet excludes all animal products, including milk, fish, eggs, and honey.\n\nThe vegan basic four food groups in the source are whole grains, vegetables, fruits, and legumes. A CNA does not judge or redesign the resident's diet. The CNA supports the ordered diet, respects preferences, avoids substitutions that violate the order, and reports if the available tray does not match the resident's diet, preference, or allergy needs.",
            "value": "Adds distinct vegan/vegetarian guidance and CNA boundaries.",
            "why": "Repairs M11.5 partial coverage without duplicating general culture content.",
            "notdup": "Food preference card; this card focuses specifically on vegetarian/vegan categories.",
        },
        {
            "title": "Meal Refusal, Intake Percent, and What to Report",
            "topic": "Dietary responsibilities and intake monitoring",
            "source": "CCCCO Module 11, Objective 7, Content Outline C",
            "module": "11",
            "status": "M11.7 Assessed; M05/L01 expanded",
            "text": "The CCCCO source emphasizes tray checks and intake documentation: correctly identify residents, check the diet card for name, diet order, instructions, and allergies, accurately record food and fluid intake, and report significant changes in dietary habits to the licensed nurse.\n\nIf a resident refuses a tray or eats very little, do not ignore it and do not pressure the resident. Determine the reason if you can do so respectfully: dislike, nausea, fatigue, pain, chewing difficulty, swallowing concern, religious preference, or fear of incontinence. Offer allowed alternatives only as permitted by the care plan or facility process. If the alternate is refused or the concern continues, report to the nurse and document according to facility policy.",
            "value": "Turns meal refusal into an observe-report-document decision sequence.",
            "why": "Adds active CNA decision depth to M05/L01 without creating a new medical role.",
            "notdup": "Therapeutic diet card; this card focuses on refusal, intake percent, and escalation.",
        },
    ],
    "L02": [
        {
            "title": "Feeding Assistance: Dignity and Pace",
            "topic": "Proper feeding techniques",
            "source": "CCCCO Module 11, Objective 8, Content Outline A",
            "module": "11",
            "status": "M11.8 Deferred for hands-on performance; theory expanded",
            "text": "CCCCO Module 11 teaches that feeding assistance should be comfortable and respectful. Sit at the resident's eye level, maintain a positive attitude, identify the foods on the tray, and encourage the resident to participate as able, such as holding bread, picking up a juice cup, or moving a fork to the mouth after food is placed on it.\n\nDo not rush. Allow the resident to set the pace as much as possible. Assistance should support independence, not take it away. The online lesson teaches the theory and safety reasoning; hands-on feeding technique remains a clinical skill and must follow facility policy, training, and the care plan.",
            "value": "Adds dignity, participation, and pace to feeding-assistance theory.",
            "why": "Improves a deferred hands-on objective without pretending online theory validates feeding competency.",
            "notdup": "Aspiration and tube-feeding cards; this card focuses on respectful meal assistance.",
        },
        {
            "title": "Dysphagia and Choking Risk",
            "topic": "Dysphagia signs and choking prevention",
            "source": "CCCCO Module 11, Objective 8, Content Outline B-C",
            "module": "11",
            "status": "M11.8 Deferred for hands-on performance; theory expanded",
            "text": "Residents at high risk for dysphagia and choking include those with stroke, neurological disease, head/neck/throat trauma, or dementia. CCCCO Module 11 lists warning signs to report: long intervals before swallowing, swallowing several times with each bite, frequent throat clearing, difficulty handling food or fluids in the mouth, wet or gurgling voice, pocketing food, excessive drooling, or the feeling that food is sticking.\n\nPrevention starts with following the individual feeding plan: small bites, small amounts, enough time to chew and swallow, close supervision, ordered thickened liquids, and upright positioning during and after meals.",
            "value": "Adds source-specific dysphagia signs and feeding-plan prevention steps.",
            "why": "Deepens aspiration prevention without adding unsourced emergency procedure content.",
            "notdup": "Dignity/pace card; this card focuses on dysphagia signs and choking risk.",
        },
        {
            "title": "Ordered Textures and Thickened Liquids",
            "topic": "Diet consistency and aspiration prevention",
            "source": "CCCCO Module 11, Objectives 7 and 8, Content Outline A-C",
            "module": "11",
            "status": "M11.7 Assessed; M11.8 theory expanded",
            "text": "Mechanical soft, pureed, soft foods, clear or full liquids, and thickened liquids are not interchangeable. CCCCO Module 11 identifies thickened liquids as part of therapeutic diet consistency. If nectar-thick, honey-thick, or another consistency is ordered, the CNA follows the order every time, not only at meals.\n\nIf a resident dislikes the texture, respond respectfully and stay in scope. Do not provide thin liquids or unapproved foods because the resident asks. Offer allowed choices if available, explain that the order is for safety, and report the concern to the nurse for care-plan review. A resident's preference matters, but the CNA cannot change the order.",
            "value": "Clarifies the difference between preference support and changing a diet order.",
            "why": "Prevents unsafe drift in thickened-liquid decisions while preserving resident dignity.",
            "notdup": "Therapeutic diet card in L01; this card applies the diet order during feeding assistance.",
        },
        {
            "title": "Tube Feeding: CNA Observation Boundaries",
            "topic": "Alternative nutrition - tube feeding",
            "source": "CCCCO Module 11, Objective 10, Content Outline A",
            "module": "11",
            "status": "M11.10 improved from Partial to Covered at CNA-scope theory level",
            "text": "CCCCO Module 11 states that tube feedings are ordered by the doctor and started by a licensed nurse. The CNA does not start, stop, adjust, or troubleshoot the feeding pump independently.\n\nThe CNA observation role is still important. Monitor for pressure on or kinking of tubing, watch the feeding level and report when it is low, keep the head of bed elevated as ordered by the care plan, and notify the licensed nurse of pump alarms or signs and symptoms of aspiration. If repositioning is needed, protect the tubing and follow the care plan. The safety rule is observe, protect, report, and do not adjust the order or equipment.",
            "value": "Adds alternative-nutrition content with explicit CNA boundaries.",
            "why": "Closes the M11.10 partial gap without implying independent tube-feeding authority.",
            "notdup": "IV boundary card; this card focuses on tube feeding observation only.",
        },
        {
            "title": "IV Fluids and Nutrition: What the CNA Reports",
            "topic": "Alternative nutrition - IV infusion",
            "source": "CCCCO Module 11, Objective 10, Content Outline B",
            "module": "11",
            "status": "M11.10 improved from Partial to Covered at CNA-scope theory level",
            "text": "The CCCCO source also describes intravenous infusion as ordered by the physician and started and monitored by a licensed nurse according to facility policy. CNA responsibilities are observation and reporting, not adjustment.\n\nKeep IV tubing free from kinks, twisting, pressure, or obstruction. Report alarms, pain or burning at the IV site, swelling or redness, fever, difficulty breathing, bleeding or leakage, disconnected tubing, or an empty IV fluid container. The CNA should never adjust or turn off IV monitoring equipment and should make sure the resident or family does not handle, adjust, or stop the infusion. Escalate concerns promptly to the licensed nurse.",
            "value": "Adds reportable IV-infusion signs and equipment boundary language.",
            "why": "Completes alternative-nutrition/infusion theory while staying within CNA scope.",
            "notdup": "Tube-feeding card; this card focuses on IV infusion observations and prohibitions.",
        },
        {
            "title": "When Feeding Becomes a Reportable Change",
            "topic": "Feeding observations and escalation",
            "source": "CCCCO Module 11, Objectives 7 and 8, Content Outline C and B",
            "module": "11",
            "status": "M11.7/M11.8 theory expanded",
            "text": "A feeding problem becomes reportable when it may affect safety, nutrition, hydration, or the care plan. Report difficulty chewing or swallowing, nausea or vomiting, anorexia, food intolerance, repeated refusal, new coughing during meals, wet or gurgling voice, pocketing food, excessive drooling, or a resident saying food feels stuck.\n\nUse objective words: what you saw, heard, measured, and what the resident said. Avoid diagnosing. Instead of writing that a resident aspirated, report that the resident coughed repeatedly after thin liquid, had a wet voice, and stopped eating. Then follow the nurse's direction and document according to facility policy.",
            "value": "Turns feeding observations into objective reporting practice.",
            "why": "Adds active decision depth that bridges M05 nutrition and M06 documentation without duplicating either.",
            "notdup": "Dysphagia card; this card focuses on when and how observations escalate.",
        },
    ],
    "L03": [
        {
            "title": "Skin Layers and Why Integrity Matters",
            "topic": "Integumentary anatomy and functions",
            "source": "CCCCO Module 13, Objective 7, Integumentary System anatomy/functions",
            "module": "13",
            "status": "M13.7 skin portion improved",
            "text": "CCCCO Module 13 describes skin as the largest organ of the body. The epidermis is the top surface layer and acts as a barrier against water loss and infection. The dermis gives skin strength and contains blood vessels, lymph vessels, nerve endings, oil glands, and hair follicles. Deeper subcutaneous tissue contains fat and connective tissue and does not tolerate lack of oxygen well.\n\nSkin protects against microorganisms, provides sensation, shields tissue from injury, regulates body temperature, eliminates waste products, helps produce vitamin D, and prevents too much water loss. When skin integrity breaks, the resident is at higher risk for infection, pain, and worsening tissue injury.",
            "value": "Adds source-supported skin anatomy/function as rationale for prevention.",
            "why": "Improves M13.7 applied skin coverage without attempting full A&P expansion.",
            "notdup": "Pressure injury staging/prevention cards; this card explains why intact skin matters.",
        },
        {
            "title": "Aging Skin and Immobility Risk",
            "topic": "Aging changes and skin breakdown risk",
            "source": "CCCCO Module 13, Objective 8, Effects of Aging handout; Objective 7 immobility complications",
            "module": "13",
            "status": "M13.8 skin-related portion improved; overall M13.8 remains Partial",
            "text": "The CCCCO aging handout notes that older skin becomes thinner, more fragile, dry, itchy, and wrinkled; chills can occur more easily because of loss of fatty tissue, and bruising can occur more easily because blood vessels are fragile. Immobility can cause skin breakdown faster.\n\nFor CNA care, this means routine personal care is also a skin-observation opportunity. Notice dry, irritated, bruised, reddened, blue, black, or open areas. Avoid rough handling, hot water, friction, and dragging during repositioning. Keep the resident covered and comfortable, use lotion as ordered or allowed, and report changes early before a small problem becomes a wound.",
            "value": "Adds aging-specific skin risk and practical CNA observation cues.",
            "why": "Gives M05/L03 a distinct aging-skin concept rather than repeating pressure-injury definitions.",
            "notdup": "Skin anatomy card and prevention bundle card; this card focuses on aging-related fragility.",
        },
        {
            "title": "High-Risk Skin Areas",
            "topic": "Bony prominences and pressure-risk locations",
            "source": "CCCCO Module 13, Objective 7, Pressure Sores signs/symptoms and duties",
            "module": "13",
            "status": "M13.7 skin portion improved; SME flag retained",
            "text": "The CCCCO source explains that pressure sores develop over bony prominences. For CNA observation, that means skin checks during care should pay special attention to places where bone, equipment, moisture, or body position creates pressure: heels, sacrum, hips, elbows, shoulder blades, ankles, ears, skin folds, and areas under tubing, braces, cushions, or restraints.\n\nLook at skin tone changes, warmth, tenderness, moisture, drainage, blisters, open areas, and resident complaints. On darker skin, early pressure changes may appear blue, purple, black, shiny, warmer, cooler, firmer, or softer rather than bright red. Report suspicious changes promptly and document objective details according to facility policy.",
            "value": "Adds source-supported bony-prominence and device-area observation focus.",
            "why": "Improves skin assessment depth without duplicating the pressure-injury definition or prevention list.",
            "notdup": "Pressure injury recognition card; this card focuses on where CNAs should look during care.",
        },
        {
            "title": "Skin Lesions and Wounds: What to Report",
            "topic": "Skin lesions, wound signs, and reporting",
            "source": "CCCCO Module 13, Objective 7, Skin Lesions/Wounds duties and observations",
            "module": "13",
            "status": "M13.7 skin portion improved",
            "text": "CCCCO Module 13 lists skin lesion and wound signs such as rash, raised spots filled with pus or fluid, irregular reddened areas that itch, dry crusts or scabs, and breaks in skin integrity. CNA duties include observing and reporting skin abnormalities and drainage on dressings.\n\nReport immediately if a skin lesion drains, the drainage changes or increases, drainage has an odor or color change, a dressing needs changing, or a wound has redness, red streaks, heat, pus, or drainage. Do not remove crusts, pick scabs, diagnose infection, or decide treatment. Observe, protect the resident, follow facility policy and the care plan, and notify the licensed nurse.",
            "value": "Adds wound/lesion reporting triggers beyond pressure-injury staging.",
            "why": "Repairs source-supported skin-observation depth while preserving CNA treatment boundaries.",
            "notdup": "Pressure injury cards; this card covers broader skin lesions and drainage reporting.",
        },
        {
            "title": "Pressure Injuries: Recognize Risk, Do Not Diagnose",
            "topic": "Pressure injuries and CNA scope",
            "source": "CCCCO Module 13, Objective 7, Pressure Sores signs/symptoms and duties",
            "module": "13",
            "status": "M13.7 skin portion improved; SME flag retained",
            "text": "CCCCO Module 13 defines pressure sores as a break in skin integrity that develops over a bony prominence as a result of pressure. The source describes staged changes, but a CNA does not independently diagnose, stage, or treat a pressure injury.\n\nThe CNA learns the warning signs to report: redness over a bony prominence that does not go away, blue or black color changes on darker skin, abrasions, blisters, shallow crater, deeper crater, exposed deeper tissue, pain, warmth, drainage, or any open area. Use plain objective descriptions. For example: \"left heel red and warm after repositioning\" is safer than writing a stage unless the nurse has documented it.",
            "value": "Teaches pressure-injury recognition while explicitly limiting CNA authority.",
            "why": "Improves skin-integrity evidence without removing SME/compliance flags.",
            "notdup": "Prevention bundle card; this card focuses on recognition and scope boundary.",
        },
        {
            "title": "Pressure Injury Prevention Bundle",
            "topic": "Pressure injury prevention measures",
            "source": "CCCCO Module 13, Objective 7, Pressure Sores duties and observations",
            "module": "13",
            "status": "M13.7/M14.8 skin-prevention portion improved",
            "text": "The CCCCO source lists prevention measures that are directly relevant to CNA work: change position at least every two hours or as ordered, remind or help seated residents shift weight, support proper nutrition and hydration, remove feces or urine promptly, inspect skin whenever personal care is given, remove wrinkles and foreign objects from linens, avoid hot water and friction, and separate body areas to prevent rubbing.\n\nPrevention is easier than treatment. Use turning sheets or other assigned aids for dependent residents, avoid dragging, keep heels protected as ordered, and report signs immediately to the licensed nurse. Do not improvise devices or treatments that are not in the care plan.",
            "value": "Adds a source-supported prevention sequence tied to CNA care-plan duties.",
            "why": "Expands prevention beyond a generic list into ordered observe-report-care-plan behavior.",
            "notdup": "Skin recognition card; this card focuses on prevention measures.",
        },
        {
            "title": "Devices, Tubing, Braces, and Bed Position",
            "topic": "Mechanical aids and rubbing/pressure checks",
            "source": "CCCCO Module 13, Objective 7, Pressure Sores duties j-o",
            "module": "13",
            "status": "M13.7 skin portion improved",
            "text": "CCCCO Module 13 includes mechanical aids and pressure checks in prevention: alternating-pressure mattresses, pillows for bridging, gel or air cushions, heel protectors, and turning sheets may be used according to the care plan. It also tells staff to check improperly fitted braces or restraints and check tubing for rubbing.\n\nThe CNA does not select or order the device independently. The CNA checks that assigned equipment is in place, notices slipping, bunching, rubbing, tubing pressure, damp linens, wrinkles, or a head-of-bed position that conflicts with the care plan, and reports concerns. If an ordered device is missing or causing pressure, escalate to the nurse.",
            "value": "Adds overlooked source detail about equipment and tubing pressure checks.",
            "why": "Prevents duplicate prevention content by focusing on device-related pressure risks.",
            "notdup": "Prevention bundle card; this card focuses on equipment, tubing, and assigned aids.",
        },
        {
            "title": "Objective Skin Reporting",
            "topic": "Objective documentation of skin findings",
            "source": "CCCCO Module 13, Objective 7, duties and observations; ContentV2 M06 documentation crosswalk",
            "module": "13",
            "status": "M13.7 skin portion improved; cross-linked to M06 documentation",
            "text": "When reporting skin, use observable details. Include location, size if facility policy allows, color, temperature, drainage, odor, pain complaint, whether skin is open or intact, and what care-plan step you were doing when you noticed it. Quote the resident's words if the resident reports pain, itching, burning, or tenderness.\n\nAvoid diagnosing or staging independently. Say, \"red area over sacrum did not fade after repositioning\" or \"dressing on left lower leg has new yellow drainage and odor,\" then report to the licensed nurse and document according to policy. This keeps the CNA role clear: observe, report, document, follow the care plan, and escalate.",
            "value": "Turns skin-integrity observations into documentation-ready CNA language.",
            "why": "Adds active reporting practice and reinforces no independent staging/treatment authority.",
            "notdup": "Skin lesion and pressure injury cards; this card focuses on documentation language.",
        },
        {
            "title": "Skin Safety Boundaries",
            "topic": "CNA skin care boundaries",
            "source": "CCCCO Module 13, Objective 7, Skin Lesions/Wounds duties and Pressure Sores duties",
            "module": "13",
            "status": "M13.7 skin portion improved; SME flag retained",
            "text": "The CCCCO source includes both actions CNAs can support and actions that require caution. CNAs can keep skin clean and dry, prevent friction and shearing, use assigned aids, inspect skin during personal care, and report changes. CNAs should not remove crusts, pick scabs, change wound treatment, diagnose infection, or decide that a pressure area is safe to ignore.\n\nIf you see drainage, odor, heat, pus, red streaks, a dressing problem, a new open area, or pressure-related discoloration, report promptly. If the resident asks you to \"just put something on it,\" explain that you need to tell the nurse so the resident receives the correct care.",
            "value": "Adds a clear can/cannot boundary for skin integrity care.",
            "why": "Strengthens compliance around pressure-injury content while preserving source-review flags.",
            "notdup": "Objective reporting card; this card focuses on scope limits and resident requests.",
        },
    ],
    "L04": [
        {
            "title": "Vital Signs: Purpose and Observation",
            "topic": "Vital signs purpose and observations",
            "source": "CCCCO Module 10, Objective 2, Content Outline A-D",
            "module": "10",
            "status": "M10.2 Assessed; M05/L04 expanded",
            "text": "CCCCO Module 10 defines vital signs as temperature, pulse, respirations, and blood pressure, with pain affecting vital signs depending on the type of pain. Vital signs are indicators of body function because they help assess body systems and signal changes occurring in the body.\n\nWhen taking vital signs, the CNA is also observing. Notice skin color and temperature, resident behavior, statements about how the resident feels, comfort level, and pain. A number by itself is not the whole picture. A pulse, temperature, or breathing rate that changes with new confusion, sweating, pale skin, pain, or shortness of breath should be reported promptly to the licensed nurse.",
            "value": "Adds the CCCCO rationale for why vital signs are taken and what else to observe.",
            "why": "Deepens M10.2 beyond a list of normal ranges.",
            "notdup": "Temperature, pulse, respiration, and BP detail cards.",
        },
        {
            "title": "Temperature Regulation and Measurement Sites",
            "topic": "Temperature as body function indicator",
            "source": "CCCCO Module 10, Objective 3, Content Outline A-G",
            "module": "10",
            "status": "M10.3 Covered; M05/L04 expanded",
            "text": "Temperature reflects the balance between heat gained and heat lost. CCCCO Module 10 identifies the hypothalamus as the temperature regulation center. Heat is produced by cellular activity, food metabolism, muscle activity, and hormones. Infection, brain injury, hot drinks, warm air, clothing, exercise, or dehydration can alter temperature.\n\nThe source lists common measurement sites: oral, rectal, tympanic, axillary, and temporal. Online theory can explain these sites and normal differences, but hands-on measurement must follow facility policy and clinical training. Report abnormal temperature or a sudden change from baseline to the licensed nurse rather than treating the temperature independently.",
            "value": "Explains temperature physiology and site differences from CCCCO source.",
            "why": "Adds source depth that current M05 had only as normal-range summary.",
            "notdup": "Temperature comfort-measures card; this card explains regulation and measurement sites.",
        },
        {
            "title": "Comfort Measures for Temperature Changes",
            "topic": "Measures to raise/lower temperature",
            "source": "CCCCO Module 10, Objective 4, Content Outline A-B",
            "module": "10",
            "status": "M10.4 improved from Partial to Covered",
            "text": "CCCCO Module 10 lists nursing measures to raise or lower body temperature. Measures to raise temperature include increasing room temperature, adding coverings, providing hot liquids, and warm baths or soaks. Measures to lower temperature include decreasing room temperature, removing coverings, offering cool liquids, and providing a cool bath or sponging.\n\nFor CNA practice, use only measures allowed by the care plan, assignment, and facility policy. Report fever, low temperature, sudden change from baseline, chills, sweating, confusion, or resident discomfort. Do not decide independently to treat fever or hypothermia. Your role is comfort support within assignment, accurate observation, documentation, and escalation.",
            "value": "Adds the specific CCCCO measures while maintaining CNA scope.",
            "why": "Closes M10.4 partial coverage without inventing treatment authority.",
            "notdup": "Temperature regulation card; this card focuses on comfort/support measures and reporting.",
        },
        {
            "title": "Pulse Sites, Factors, and Qualities",
            "topic": "Pulse circulation, sites, factors, and qualities",
            "source": "CCCCO Module 10, Objectives 5 and 6, Content Outline A-C",
            "module": "10",
            "status": "M10.5 improved from Partial to Covered; M10.6 Covered",
            "text": "A pulse is the expansion of arterial walls each time the heart contracts and forces blood into the arterial system. CCCCO Module 10 lists major pulse sites: carotid, apical, brachial, radial, femoral, popliteal, and dorsalis pedis. Routine CNA vital signs often use the radial site unless the care plan or nurse directs otherwise.\n\nFactors that can increase pulse include exercise, fever, hemorrhage, pain, shock, and strong emotions. Factors that can decrease pulse include sleep, rest, depression, some medications, and athletic conditioning. Observe rate, rhythm, and strength. Report irregular rhythm even if the rate is normal, and report weak, thready, bounding, or baseline-changing pulse findings.",
            "value": "Adds pulse physiology, pulse sites, and factor/quality distinctions.",
            "why": "Closes M10.5 partial coverage and deepens M10.6.",
            "notdup": "Respiration card; this card focuses on pulse.",
        },
        {
            "title": "Respirations and Abnormal Patterns",
            "topic": "Respiration observations and abnormal breathing patterns",
            "source": "CCCCO Module 10, Objectives 7, 8, and 9, Content Outline A-J",
            "module": "10",
            "status": "M10.9 improved from Partial to Covered",
            "text": "Respiration is the exchange of oxygen and carbon dioxide in the lungs. CCCCO Module 10 lists normal adult breathing as quiet, effortless, and regular, with a normal adult rate of 12 to 20 per minute. When measuring respirations, observe rate, rhythm, depth, symmetry, effort, discomfort, position, sounds, skin and mucous membrane color, nail beds, and behavior changes.\n\nAbnormal patterns to recognize and report include labored breathing, orthopnea, stertorous or snoring sounds that may signal partial airway obstruction, abdominal breathing, shallow breathing, dyspnea, tachypnea, bradypnea, apnea, and Cheyne-Stokes respirations. Report abnormal pattern or appearance changes to the licensed nurse promptly.",
            "value": "Adds the CCCCO abnormal breathing pattern catalog and observation cues.",
            "why": "Closes M10.9 partial coverage and strengthens respiratory reporting.",
            "notdup": "Pulse and BP cards; this card focuses on breathing observations.",
        },
        {
            "title": "Blood Pressure: What the Numbers Mean",
            "topic": "Blood pressure physiology and ranges",
            "source": "CCCCO Module 10, Objective 11, Content Outline A-B",
            "module": "10",
            "status": "M10.11 improved from Partial to Covered",
            "text": "Blood pressure is the force of blood pushing against artery walls. CCCCO Module 10 explains systolic pressure as the first number, when the heart contracts and pressure is highest in the arteries. Diastolic pressure is the second number, when the heart is at rest and pressure is lowest.\n\nThe source lists normal adult blood pressure around 120/80, with systolic generally 90 to 140 and diastolic 60 to 90. Persistent readings above normal are hypertension; persistent readings below normal are hypotension. Pulse pressure is the difference between systolic and diastolic and may provide information about blood vessels. The CNA reports abnormal or changed readings; diagnosis belongs to licensed staff.",
            "value": "Adds systolic/diastolic physiology and pulse pressure concept.",
            "why": "Closes M10.11 partial coverage without turning the CNA into a diagnostician.",
            "notdup": "BP accuracy/equipment card; this card explains what the numbers mean.",
        },
        {
            "title": "Blood Pressure Accuracy and Safety Boundaries",
            "topic": "BP factors, equipment, and measurement cautions",
            "source": "CCCCO Module 10, Objectives 12, 13, and 14, Content Outline A-B",
            "module": "10",
            "status": "M10.12 Covered; M10.13/M10.14 remain Deferred for hands-on performance but theory expanded",
            "text": "CCCCO Module 10 lists factors that can raise blood pressure, including strong emotion, exercise, standing or sitting, excitement, pain, smaller blood vessel size, digestion, and an improperly placed cuff. Factors that can lower it include rest, sleep, lying down, depression, shock, and hemorrhage.\n\nThe source also identifies equipment and accuracy cautions: cuff, bulb, manometer, stethoscope, or electronic cuff. A cuff that is too narrow or small can give a falsely high reading; a loose or improperly placed cuff can give a falsely low reading. Measurement on an arm with injury, IV line, dialysis site, cast, recent trauma, or certain surgery history requires nurse direction. Hands-on BP performance remains a clinical skill.",
            "value": "Adds source-supported BP accuracy risks while keeping hands-on skill deferred.",
            "why": "Improves M10.13/M10.14 theory evidence without claiming online competency validation.",
            "notdup": "BP physiology card; this card focuses on accuracy, equipment, and safety boundaries.",
        },
        {
            "title": "TPR Sequence and When to Escalate",
            "topic": "Temperature-pulse-respiration combined procedure",
            "source": "CCCCO Module 10, Objective 10, Content Outline A-C",
            "module": "10",
            "status": "M10.10 Deferred for hands-on performance; theory expanded",
            "text": "CCCCO Module 10 teaches that TPR is usually taken in sequence: temperature first, then pulse, then respirations. The source notes that the pulse rate should be remembered while counting respirations so the numbers can be documented together, and that stopping to record pulse before counting respirations can interfere with a smooth combined procedure.\n\nFor online theory, the key point is not hands-on validation. The key point is accurate sequence, attention, and reporting. If any part of TPR is abnormal, significantly different from baseline, or paired with concerning symptoms such as pain, color change, confusion, weakness, or difficult breathing, report promptly to the licensed nurse and document according to facility policy.",
            "value": "Adds TPR sequence reasoning while keeping hands-on performance deferred.",
            "why": "Improves M10.10 theory evidence without using online content as a clinical skills sign-off.",
            "notdup": "Temperature, pulse, and respiration cards; this card focuses on combined sequence and escalation.",
        },
        {
            "title": "Pain Observation and Reporting",
            "topic": "Pain effects on vital signs and CNA reporting",
            "source": "CCCCO Module 10, Objective 15, Content Outline A-D",
            "module": "10",
            "status": "M10.15 Covered; M05/L04 expanded",
            "text": "CCCCO Module 10 states that pain is not a normal part of aging and may be a warning or distress signal. CNAs may be the first to notice pain, especially when a resident does not say it directly. Pain may affect pulse, respirations, and blood pressure, and may cause sweating, nausea, vomiting, restlessness, agitation, tension, difficulty moving, moaning, crying, or guarding a body part.\n\nAsk about pain using the facility method, observe facial expression and movement, and report complaints of pain to the licensed nurse. Use the resident's words when possible, including location, frequency, duration, and quality. Do not judge, minimize, or independently treat pain.",
            "value": "Adds source-specific pain signs and reporting details tied to vital signs.",
            "why": "Expands M10.15 in M05 without duplicating general vital-sign purpose.",
            "notdup": "Respiration and BP cards; this card focuses on pain as observation/reporting.",
        },
    ],
    "L05": [
        {
            "title": "Intake and Output (I&O)",
            "topic": "I&O monitoring and imbalance reporting",
            "source": "CCCCO Module 11, Objective 7, Content Outline C; ContentV1 M05 L05",
            "module": "11",
            "status": "M11.7 Assessed; M05/L05 maintained",
            "text": "Intake is all fluid taken in, including oral fluids, tube feeding, and other ordered sources recorded by facility policy. Output is fluid leaving the body, such as urine, emesis, wound drainage, or diarrhea. If I&O is ordered, measure and record in milliliters rather than estimating.\n\nRecord at the intervals required by the care plan. Report large imbalances, very low output, much more output than intake, dark urine, new edema, shortness of breath, sudden weight change, or any finding that may suggest dehydration or fluid overload. Accurate I&O helps the nurse evaluate fluid balance; it does not authorize the CNA to change fluids or diet orders.",
            "value": "Maintains I&O teaching and strengthens source-supported report triggers.",
            "why": "Keeps L05 concise because it already met depth threshold, while improving source fidelity.",
            "notdup": "L01 hydration card; this card focuses on ordered measurement and documentation.",
        },
        {
            "title": "Vital Sign Recording",
            "topic": "Recording vital signs",
            "source": "CCCCO Module 10, Objective 16, Content Outline A-B",
            "module": "10",
            "status": "M10.16 Assessed; M05/L05 expanded",
            "text": "CCCCO Module 10 teaches that temperature, pulse, and respirations are recorded in TPR order and that normal and abnormal findings are reported to the licensed nurse. Temperature route matters: for example, rectal and axillary readings are noted by route according to facility policy. Pulse readings other than radial may need notation, such as apical pulse, and blood pressure is written as systolic over diastolic.\n\nThe CNA documents the value, route or site when required, date/time, and any relevant observation. Never guess, round from memory, or write a value before it is taken. If a reading seems wrong, follow policy for retaking or reporting it.",
            "value": "Adds source-specific vital-sign charting rules from CCCCO M10 objective 16.",
            "why": "Improves M10.16 evidence in M05/L05 without duplicating M06 documentation lessons.",
            "notdup": "I&O card and weight card; this card focuses on TPR/BP recording.",
        },
        {
            "title": "Weight Monitoring and Change Reporting",
            "topic": "Weight monitoring and reportable changes",
            "source": "ContentV1 M05 L05; CCCCO Module 11 nutrition/fluid monitoring rationale",
            "module": "11",
            "status": "M05/L05 maintained; nutrition observation support",
            "source_confidence": "medium",
            "text": "Weight changes can signal nutrition problems, dehydration, fluid retention, or disease progression. Use the same scale, similar clothing, and the same general time of day when facility policy requires weight monitoring. Record the weight, date, time, and any factor that may affect accuracy.\n\nReport sudden weight gain, unexpected weight loss, repeated poor intake, swelling, shortness of breath, or a weight that is very different from baseline. Do not interpret the cause independently. Your job is to notice the change, verify the measurement according to policy, document accurately, and report promptly to the licensed nurse.",
            "value": "Keeps weight monitoring as a concise observation/reporting bridge.",
            "why": "Retains useful ContentV1 implementation detail but aligns it with CCCCO nutrition/fluid rationale.",
            "notdup": "I&O and vital-sign recording cards; this card focuses on weight trend observation.",
        },
    ],
}


def make_delivery_cards(lesson: dict) -> list[dict]:
    cards = []
    for idx, spec in enumerate(LESSON_SPECS[lesson["lesson_id"]]):
        letter = chr(ord("A") + idx)
        card_id = f"C02{letter}_DELIVERY"
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
        cards.append(base_card(lesson, card_id, "delivery", spec["title"], spec["text"], meta))
    return cards


def retarget_existing_card(card: dict, lesson: dict, idx_after_delivery: int) -> dict:
    out = deepcopy(card)
    # Preserve existing challenge/debrief card IDs and app locations (C03/C04A).
    out["module_id"] = MODULE_ID
    out["module_title"] = MODULE_TITLE
    out["lesson_id"] = lesson["lesson_id"]
    out["lesson_title"] = lesson["lesson_title"]
    out["status"] = "sme-review"
    out["sme_review_flag"] = SME_FLAG
    out["compliance_review_flag"] = COMPLIANCE_FLAG
    default_meta = quality_meta(
        source_reference=out.get("source_reference") or f"{CONTENTV1}#{lesson['lesson_id']}",
        source_module_number="10/11/13",
        source_topic=f"{lesson['lesson_title']} practice/remediation",
        source_confidence="high" if lesson["lesson_id"] != "L03" else "high for CCCCO M13 skin source; SME review retained",
        transformation_type="existing practice/remediation with required evidence metadata",
        unique_learning_value=f"Provides practice/remediation evidence for {lesson['lesson_title']}.",
        why_this_card_exists="Maintains the required practice challenge and debrief/remediation sequence for the lesson.",
        not_duplicate_of="Delivery cards; practice/remediation applies rather than introduces source content.",
        survey_evidence_status=f"M05 {lesson['lesson_id']} practice/remediation evidence retained after CCCCO expansion",
    )
    out = refresh_non_delivery(out, lesson, default_meta)
    # Update media placeholder location/title if it is missing or stale.
    if out.get("media_prompt_placeholder"):
        out["media_prompt_placeholder"]["app_location"] = out["app"]["location"]
    return out


def rebuild_lesson(lesson: dict) -> None:
    existing = lesson["cards"]
    overview = next(c for c in existing if c.get("card_type") == "overview")
    challenge = next(c for c in existing if c.get("card_type") == "challenge")
    debrief = next(c for c in existing if c.get("card_type") == "debrief")

    default_meta = quality_meta(
        source_reference=lesson.get("source_reference") or f"{CONTENTV1}#{lesson['lesson_id']}",
        source_module_number="10/11/13",
        source_topic=lesson["lesson_title"],
        source_confidence="high" if lesson["lesson_id"] != "L03" else "high for CCCCO M13 skin source; SME review retained",
        transformation_type="lesson-orientation",
        unique_learning_value=f"Introduces the {lesson['lesson_title']} source-supported lesson sequence and scope boundaries.",
        why_this_card_exists="Frames the lesson before delivery, practice challenge, and debrief/remediation.",
        not_duplicate_of="Delivery cards; overview orients rather than teaches source details.",
        survey_evidence_status=f"M05 {lesson['lesson_id']} overview retained after CCCCO expansion",
    )
    overview = refresh_non_delivery(overview, lesson, default_meta)
    delivery = make_delivery_cards(lesson)
    challenge = retarget_existing_card(challenge, lesson, len(delivery))
    debrief = retarget_existing_card(debrief, lesson, len(delivery) + 1)
    lesson["cards"] = [overview, *delivery, challenge, debrief]
    lesson["status"] = "sme-review"


def main() -> int:
    data = json.loads(CANON.read_text(encoding="utf-8"))
    module = next(m for m in data["modules"] if m["module_id"] == MODULE_ID)
    before_count = sum(len(l.get("cards", [])) for l in module["lessons"])
    before_active = module.get("estimated_active_learning_minutes")

    module["status"] = "sme-review"
    module["sme_review_flag"] = SME_FLAG
    module["compliance_review_flag"] = COMPLIANCE_FLAG
    module["source_status_flag"] = "Skin integrity source review active; CCCCO Module 13 skin source mapped but SME review retained."

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
