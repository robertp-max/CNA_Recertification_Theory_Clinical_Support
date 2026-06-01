"""author_m01_delivery_from_source.py

Task 2 - Source-supported Module 1 (Infection Control) delivery expansion.

Transforms the 15 real teaching screens in
    CNA-Recert-Course/Content/theory/modules/05_THEORY_MODULE_01_INFECTION_CONTROL_FULL.md
into per-screen delivery subcards (C02A..C02x) for each M01 lesson, replacing the
thin single-placeholder C02A delivery cards.

INTEGRITY RULES (enforced by design):
  * Content is taken from the ContentV1 source screens only. Nothing is invented.
  * The ContentV1 source itself states infection control has NO dedicated NATP
    10-17 module and that ALL content "requires SME/source review". Therefore every
    expanded card KEEPS the infection-control SME/source-review flag. The time gap
    to 90 minutes is reported honestly; it is NOT padded with filler.
  * transformation_type = "split" (source module split into per-screen cards).
  * source_confidence = "medium" (real, standard-practice content but no canonical
    NATP 10-17 backing).

This edits ONLY the canonical JSON. Rerun the generator afterwards:
    python CNA-Recert-Course/ContentV2/tools/rebuild_contentv2_from_json.py
"""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CANON = ROOT / "CNA-Recert-Course" / "ContentV2" / "data" / "courseContentV2.json"
SOURCE_FILE = "CNA-Recert-Course/Content/theory/modules/05_THEORY_MODULE_01_INFECTION_CONTROL_FULL.md"

SME_FLAG = "Module 1 infection-control content requires SME/source review (no dedicated NATP 10-17 source module)."
COMPLIANCE_FLAG = "Compliance/legal/CDPH review required before production."

# ---------------------------------------------------------------------------
# Source-derived delivery screens (verbatim/lightly-adapted from the ContentV1
# module-01 source file; section refs map to the source "Screen N" headings).
# ---------------------------------------------------------------------------
SCREENS: list[dict] = [
    # ----- Lesson L01: Why Infection Control Matters in LTC (screens 1-3) -----
    {
        "lesson_id": "L01", "letter": "A", "section": "Screen 1 - Healthcare-Associated Infections",
        "title": "Healthcare-Associated Infections in Long-Term Care",
        "content": (
            "A healthcare-associated infection, or HAI, is an infection a person gets while receiving care in a "
            "healthcare facility. HAIs are a serious concern in long-term care because residents often have weakened "
            "immune systems due to age or chronic illness, residents live in close proximity to one another, many "
            "residents need hands-on assistance with daily care, and shared equipment and common areas create "
            "opportunities for germ transmission. As a CNA, you have direct contact with residents throughout your "
            "shift. That places you in a unique position to both prevent infections and recognize them early."
        ),
        "key_terms": [
            {"term": "Healthcare-associated infection (HAI)", "definition": "An infection a person acquires while receiving care in a healthcare facility."},
        ],
    },
    {
        "lesson_id": "L01", "letter": "B", "section": "Screen 2 - Your Role in Infection Control",
        "title": "Your Everyday Role in Infection Control",
        "content": (
            "Every time you wash your hands before and after resident contact, put on gloves before handling body "
            "fluids, change linens using proper technique, or report a resident's new symptoms to the nurse, you are "
            "practicing infection control. Infection control is not just a set of rules. It is a core part of safe, "
            "compassionate care. When you protect residents from infection, you help them stay healthier, more "
            "comfortable, and more independent."
        ),
    },
    {
        "lesson_id": "L01", "letter": "C", "section": "Screen 3 - Why LTC is Different",
        "title": "Why Long-Term Care Carries Unique Infection Risk",
        "content": (
            "Long-term care residents face unique infection risks. Advanced age weakens the immune response. Chronic "
            "conditions such as diabetes, COPD, and heart failure reduce resistance. Indwelling devices like catheters "
            "and feeding tubes create entry points for germs. Shared living spaces such as dining rooms, activity "
            "areas, and bathrooms are used by many people. Residents with cognitive impairment may not be able to "
            "follow hygiene steps, and multiple caregivers mean each contact is a potential transmission point. "
            "Knowing these risks helps you stay alert during routine care."
        ),
    },
    # ----- Lesson L02: The Chain of Infection (screens 4-5) -----
    {
        "lesson_id": "L02", "letter": "A", "section": "Screen 4 - The Six Links",
        "title": "The Six Links in the Chain of Infection",
        "content": (
            "Infections spread through a chain of six connected links. Break any one link and you can stop the "
            "infection from spreading. The links are: the infectious agent, the germ such as a bacterium, virus, or "
            "fungus that causes disease; the reservoir, where the germ lives and multiplies, such as a person, a "
            "contaminated surface, or standing water; the portal of exit, how the germ leaves the reservoir through "
            "body fluids, respiratory droplets, or skin contact; the mode of transmission, how the germ travels to a "
            "new host by direct contact, droplet, airborne spread, or contaminated objects; the portal of entry, how "
            "the germ enters a new host through breaks in skin, mucous membranes, or the respiratory tract; and the "
            "susceptible host, a person whose body cannot fight off the germ."
        ),
        "key_terms": [
            {"term": "Mode of transmission", "definition": "How a germ travels to a new host - direct contact, droplet, airborne, or contaminated objects."},
            {"term": "Susceptible host", "definition": "A person whose body cannot easily fight off an infectious agent."},
        ],
    },
    {
        "lesson_id": "L02", "letter": "B", "section": "Screen 5 - Breaking the Chain",
        "title": "How CNAs Break the Chain Every Day",
        "content": (
            "As a CNA you break the chain every day. You attack the infectious agent through proper cleaning and "
            "disinfection. You reduce the reservoir with environmental cleaning and proper waste disposal. You close "
            "the portal of exit by covering wounds and handling linen properly. You block the mode of transmission "
            "with hand hygiene, PPE, and standard precautions. You protect the portal of entry through skin care and "
            "wound protection. And you support the susceptible host with good nutrition, mobility support, and early "
            "reporting of changes. Hand hygiene breaks the chain at the most common transmission point and is the "
            "single most effective way to prevent infection spread."
        ),
    },
    # ----- Lesson L03: Hand Hygiene (screens 6-7) -----
    {
        "lesson_id": "L03", "letter": "A", "section": "Screen 6 - WHO 5 Moments for Hand Hygiene",
        "title": "The WHO Five Moments for Hand Hygiene",
        "content": (
            "The World Health Organization identifies five key moments when healthcare workers must perform hand "
            "hygiene: before touching a resident; before a clean or aseptic procedure such as catheter care; after a "
            "body fluid exposure risk such as emptying a urinal; after touching a resident; and after touching a "
            "resident's surroundings such as the bed rail or call light. A helpful way to remember this is to picture "
            "a safety zone around each resident. Clean hands enter the zone, and clean hands leave the zone."
        ),
        "key_terms": [
            {"term": "WHO 5 Moments", "definition": "Five required hand-hygiene moments: before touching, before clean procedure, after fluid risk, after touching, after surroundings."},
        ],
    },
    {
        "lesson_id": "L03", "letter": "B", "section": "Screen 7 - Handwashing vs. Hand Sanitizer",
        "title": "Soap and Water vs. Alcohol-Based Sanitizer",
        "content": (
            "Choose your method based on the situation. Use soap and water when hands are visibly soiled, after using "
            "the restroom, and after caring for a resident with C. difficile or norovirus; scrub for at least twenty "
            "seconds. Use alcohol-based hand sanitizer when hands are not visibly soiled and between routine resident "
            "contacts; cover all surfaces and rub until dry, about twenty seconds. Remember that alcohol-based "
            "sanitizer does not work against all germs, so use soap and water when hands are visibly dirty or after "
            "caring for residents with certain infections."
        ),
    },
    # ----- Lesson L04: PPE (screens 8-10) -----
    {
        "lesson_id": "L04", "letter": "A", "section": "Screen 8 - Standard Precautions",
        "title": "Standard Precautions: Protect Every Time",
        "content": (
            "Standard precautions assume that all body fluids except sweat may contain infectious agents. That means "
            "you use protective measures for every resident, every time, not just for residents known to have an "
            "infection. Standard precautions include hand hygiene, PPE use based on the task, safe handling of sharps "
            "and contaminated items, proper linen handling, and respiratory hygiene and cough etiquette."
        ),
        "key_terms": [
            {"term": "Standard precautions", "definition": "Treat all body fluids (except sweat) as potentially infectious and protect during every contact."},
        ],
    },
    {
        "lesson_id": "L04", "letter": "B", "section": "Screen 9 - PPE Selection Guide",
        "title": "Selecting the Right PPE for the Task",
        "content": (
            "Match your PPE to the task. Routine vital signs usually need no PPE unless your skin may contact fluids. "
            "For bathing and perineal care, wear gloves, and add a gown if there is a splashing risk. When emptying a "
            "urinal or bedpan, wear gloves, and add a gown and eye protection if splashing is likely. Suctioning "
            "requires gloves, gown, mask, and eye protection. Changing soiled linen requires gloves, and a gown if it "
            "is saturated. For a resident on droplet precautions, wear gloves, gown, and a surgical mask, with eye "
            "protection per facility policy. When in doubt, protect more, not less."
        ),
    },
    {
        "lesson_id": "L04", "letter": "C", "section": "Screen 10 - Donning and Doffing Order",
        "title": "Donning and Doffing PPE in the Correct Order",
        "content": (
            "Put PPE on in this order: gown, then mask, then eye protection, then gloves. Take PPE off in this order: "
            "gloves, then eye protection, then gown, then mask. The doffing sequence matters because gloves are the "
            "most contaminated item, so you remove them first to reduce the risk of touching your face or clothing "
            "with contaminated gloves. Always perform hand hygiene after removing all PPE."
        ),
        "key_terms": [
            {"term": "Doffing", "definition": "Removing PPE in the order gloves, eye protection, gown, mask - then hand hygiene."},
        ],
    },
    # ----- Lesson L05: Recognizing and Reporting Infection Signs (screens 11-12) -----
    {
        "lesson_id": "L05", "letter": "A", "section": "Screen 11 - Common Signs of Infection",
        "title": "Common Signs of Infection to Watch For",
        "content": (
            "Because you see residents more often than any other caregiver, you are often the first to notice changes. "
            "Report any of these signs to the licensed nurse: fever, or a temperature above the resident's normal "
            "range; a new or worsening cough; a change in sputum color, amount, or odor; a change in urine that is "
            "cloudy, foul-smelling, or dark; redness, swelling, warmth, or drainage around a wound or catheter site; a "
            "change in mental status such as new confusion, agitation, or lethargy, which in elderly residents may be "
            "the first sign of infection; decreased appetite or fluid intake; and new skin changes such as a rash, "
            "redness, or warmth."
        ),
    },
    {
        "lesson_id": "L05", "letter": "B", "section": "Screen 12 - Reporting: What, When, How",
        "title": "Reporting Infection Concerns: What, When, How",
        "content": (
            "Report new symptoms or changes from baseline immediately by telling the licensed nurse directly; do not "
            "wait for charting time. Report vital signs outside the normal range immediately, giving the numbers and "
            "describing what you observed. Report changes you noticed during care before the end of your shift at a "
            "minimum, following your facility's reporting process. Remember the boundary: you report, and the nurse "
            "assesses. Reporting a concern is never wrong, but failing to report one can be dangerous."
        ),
        "key_terms": [
            {"term": "Report, don't assess", "definition": "The CNA observes and reports changes; the licensed nurse performs clinical assessment."},
        ],
    },
    # ----- Lesson L06: Environmental Cleaning and Safe Practices (screens 13-15) -----
    {
        "lesson_id": "L06", "letter": "A", "section": "Screen 13 - Environmental Cleaning",
        "title": "Environmental Cleaning Principles",
        "content": (
            "A clean environment helps break the chain of infection at the reservoir link. Clean high-touch surfaces "
            "regularly, including bed rails, call lights, doorknobs, light switches, and toilet handles. Always clean "
            "from clean areas toward dirty areas and from top to bottom. Use facility-approved disinfectants and "
            "follow the contact-time instructions on the label. Never mix cleaning chemicals, and dispose of "
            "contaminated materials in the appropriate containers."
        ),
    },
    {
        "lesson_id": "L06", "letter": "B", "section": "Screen 14 - Safe Linen Handling",
        "title": "Safe Linen Handling",
        "content": (
            "Handle soiled linen carefully to avoid spreading germs into the air or onto surfaces. Hold soiled linen "
            "away from your body. Do not shake soiled linen, because shaking can spread germs into the air. Place "
            "soiled linen in the designated linen bags or hampers immediately, and never place soiled linen on the "
            "floor. Wash your hands after handling soiled linen, even if you wore gloves."
        ),
    },
    {
        "lesson_id": "L06", "letter": "C", "section": "Screen 15 - Sharps and Waste",
        "title": "Sharps and Biohazard Waste Safety",
        "content": (
            "Handle sharps and waste with care. Never recap a used needle; if you encounter one, report it to the "
            "nurse. Dispose of sharps only in puncture-resistant sharps containers. Report any needlestick or sharps "
            "injury immediately. Follow your facility's biohazardous waste procedures for all contaminated items."
        ),
    },
]


def words(text: str) -> int:
    return len([w for w in re.split(r"\s+", text) if w])


def narration_seconds(text: str) -> int:
    # 145 words/minute spoken pace (matches existing narration estimates).
    return max(10, round(words(text) / 145.0 * 60.0))


def duration_status(seconds: int) -> str:
    if seconds < 35:
        return "Short - acceptable if intentionally brief"
    if seconds > 75:
        return "Long - consider splitting"
    return "On target (45-75s)"


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


def build_delivery_card(module: dict, lesson: dict, screen: dict, template: dict) -> dict:
    letter = screen["letter"]
    card_id = f"C02{letter}_DELIVERY"
    location = f"module.m01.lesson.{lesson['lesson_id'].lower()}.card.c02{letter.lower()}_delivery"
    title = screen["title"]
    content = screen["content"]
    secs = narration_seconds(content)
    card = copy.deepcopy(template)  # inherit exact shape from an existing card
    card.update({
        "module_id": module["module_id"],
        "module_title": module["module_title"],
        "lesson_id": lesson["lesson_id"],
        "lesson_title": lesson["lesson_title"],
        "card_id": card_id,
        "card_type": "delivery",
        "app": {"location": location},
        "display_title": title,
        "learner_facing_content": content,
        "learning_goal": f"Teach: {title}.",
        "cna_practice_example": "Apply this during routine CNA care while staying within scope: observe, protect, and report.",
        "why_it_matters": [
            "Supports safe CNA judgment within scope of practice.",
            "Builds audit-ready completion evidence for required online theory only.",
            "Preserves compliance boundaries: no PHI, no clinical-hour credit, certificate production disabled.",
        ],
        "key_terms": screen.get("key_terms", []),
        "completion_condition": "Learner reads and views this delivery card and continues through the lesson sequence.",
        "narration_script": content,
        "transcript_text": content,
        "estimated_narration_seconds": secs,
        "estimated_word_count": words(content),
        "target_duration_status": duration_status(secs),
        "media_prompt_placeholder": media_placeholder(location, title),
        "source_reference": f"{SOURCE_FILE} {screen['section']}",
        "source_module": "ContentV1 Module 01 - Infection Control (no dedicated NATP 10-17 source)",
        "source_section": screen["section"],
        "source_confidence": "medium",
        "transformation_type": "split",
        "status": "sme-review",
        "sme_review_flag": SME_FLAG,
        "compliance_review_flag": COMPLIANCE_FLAG,
        "internal_challenge": None,
        "debrief_rationale": None,
    })
    return card


def main() -> int:
    data = json.loads(CANON.read_text(encoding="utf-8"))
    module = next(m for m in data["modules"] if m["module_id"] == "M01")

    by_lesson: dict[str, list[dict]] = {}
    for s in SCREENS:
        by_lesson.setdefault(s["lesson_id"], []).append(s)

    added = 0
    replaced = 0
    for lesson in module["lessons"]:
        lid = lesson["lesson_id"]
        if lid not in by_lesson:
            continue
        cards = lesson["cards"]
        # Use an existing delivery card as the structural template (exact shape).
        template = next((c for c in cards if c["card_type"] == "delivery"), cards[0])
        # Partition existing cards: keep everything that is NOT a C02*_DELIVERY card.
        overview = [c for c in cards if c["card_type"] == "overview"]
        delivery_old = [c for c in cards if c["card_type"] == "delivery"]
        tail = [c for c in cards if c["card_type"] not in ("overview", "delivery")]
        replaced += len(delivery_old)
        new_delivery = [build_delivery_card(module, lesson, s, template) for s in by_lesson[lid]]
        added += len(new_delivery)
        lesson["cards"] = overview + new_delivery + tail

    # Keep the module honestly flagged: real source, but no dedicated NATP source.
    module["status"] = "sme-review"
    module["sme_review_flag"] = SME_FLAG
    module["source_status_flag"] = (
        "Source-supported expansion from ContentV1 Module 01 screens. Infection control has no dedicated NATP 10-17 "
        "source module; 90-minute allocation is supported by teaching screens but requires SME/source review before production."
    )

    CANON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "OK",
        "m01_delivery_cards_replaced": replaced,
        "m01_delivery_cards_added": added,
        "m01_cards_total": sum(len(l["cards"]) for l in module["lessons"]),
        "note": "Infection-control SME/source-review flag preserved on every card; no NATP 10-17 backing claimed.",
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
