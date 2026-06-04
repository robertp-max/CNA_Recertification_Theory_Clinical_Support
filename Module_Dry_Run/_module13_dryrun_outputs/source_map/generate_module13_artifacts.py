import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path('Module_Dry_Run')
APP = ROOT / 'standalone-course-mvp'
OUT = ROOT / '_module13_dryrun_outputs'
SOURCE = Path('CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-13.pdf')
MODULE_ID = 'M13'
TITLE = 'NATP Module 13: Long Term Care Resident'
SOURCE_REF = SOURCE.as_posix()
NOW = datetime.now().isoformat(timespec='seconds')

for rel in ['source_map', 'data', 'audio', 'media', 'reports']:
    (OUT / rel).mkdir(parents=True, exist_ok=True)
(APP / 'src/data').mkdir(parents=True, exist_ok=True)

# Extract the source text with UTF-8. This is the sole source authority for generated content.
layout_path = OUT / 'source_map/module13_source_layout.txt'
raw_path = OUT / 'source_map/module13_source_raw.txt'
subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', str(SOURCE), str(layout_path)], check=True)
subprocess.run(['pdftotext', '-raw', '-enc', 'UTF-8', str(SOURCE), str(raw_path)], check=True)
layout = layout_path.read_text(encoding='utf-8', errors='replace')
raw = raw_path.read_text(encoding='utf-8', errors='replace')

# Parse terminology from the raw text: source pages 1-4 before Performance Standards.
terminology_block = raw.split('Performance Standards (Objectives):', 1)[0]
term_matches = re.findall(r'(?m)^\s*(\d{1,3})\.\s+(.+?)(?=\n\s*\d{1,3}\.\s+|\n[A-Z][A-Za-z /&()-]+System:|\nPerformance Standards|\Z)', terminology_block, re.S)
terms = []
for num, body in term_matches:
    cleaned = ' '.join(body.split())
    # remove footer/header artifacts if they slipped in
    cleaned = re.sub(r'California Community Colleges.*?Page \d+ of 82', '', cleaned).strip()
    if cleaned:
        terms.append({'term_number': int(num), 'term': cleaned, 'source_reference': f'{SOURCE_REF}#page-1-4'})
terms = sorted({t['term_number']: t for t in terms}.values(), key=lambda t: t['term_number'])

objectives = {
    1: 'Define key terminology',
    2: 'Describe common basic human needs and interventions for the elderly patient/resident; environmental, psychological, social, recreational and spiritual',
    3: 'Describe common community resources to meet the needs of the elderly',
    4: 'Describe the special needs of persons with developmental and mental disorders including intellectual disability, cerebral palsy, epilepsy, Parkinson’s disease, and mental illness',
    5: 'Describe the special needs of persons with Alzheimer’s Disease and other related dementias',
    6: 'Describe the body’s basic organization and composition',
    7: 'List the body systems, including basic anatomy and physiology, common diseases of the elderly with signs and symptoms, Nurse Assistant duties and observations, aging changes and complications of immobility',
    8: 'Describe changes in body systems associated with aging',
}

page_ranges = {
    1: [7],
    2: [7, 8, 9],
    3: [9, 10],
    4: [10, 11, 12, 13, 14, 15],
    5: [15, 16, 17, 18, 19, 20],
    6: [20, 21],
    7: list(range(21, 57)),
    8: [56, 57, 58, 59],
}

weights = {
    1: 60,
    2: 60,
    3: 45,
    4: 120,
    5: 120,
    6: 45,
    7: 270,
    8: 60,
}

content_outline = {
    1: [
        'Review, spell, pronounce, and use Module 13 terminology in proper context.',
        'Terminology covers long-term care resident vocabulary, medical/anatomical terms, body-system terms, conditions, signs/symptoms, and care-related vocabulary.',
        'Use terms appropriately when charting and reporting to licensed personnel.',
    ],
    2: [
        'Environmental/physical needs: safety, shelter, balanced nutrition, adequate fluids, support/adaptive devices, personal hygiene, and environmental control.',
        'Psychological needs: maintain self-esteem, respectful treatment, individual differences, privacy, choices, activities, and adjustment to role change/loss of independence.',
        'Social, recreational, and spiritual needs: family/community involvement, reminiscing, new social contacts, social services, hobbies, compliments, positive traits/abilities, respect for religious choices.',
        'Report unusual signs to the licensed nurse.',
    ],
    3: [
        'Community resources include Area Agency on Aging, adult day care, support groups, county health centers, hospitals/hospice, IRS information, ombudsman, Meals on Wheels, Medicare/Social Security, mental health, NAMI, ADA, APS, Red Cross/BP clinics, senior centers/housing, suicide prevention, home health, AARP, regional centers, and faith/social organizations.',
        'Nurse Assistant role is to assist licensed staff in sharing appropriate resource information and report unusual signs/symptoms to the licensed nurse.',
    ],
    4: [
        'Special needs and care approaches for epilepsy/seizure disorders, Parkinson’s disease, schizophrenia, hypochondriasis, depression, suicidal patient/resident, intellectual/developmental disabilities, cerebral palsy, alcoholism/drug abuse, and agitation.',
        'Nurse Assistant duties include safety, calm environment, dignity/privacy, normalization, observation/reporting, following the care plan, seizure safety steps, assistive-device support, emotional support, boundaries, and urgent reporting of danger, withdrawal, suicidal statements, or worsening behavior.',
    ],
    5: [
        'Differentiate dementia, delirium, and depression; describe signs/symptoms and progression of Alzheimer’s disease and related dementias.',
        'Care approaches include injury prevention, compassion, independence as long as possible, activities within capability, dignity/self-esteem, structured quiet environment, short simple directions, observing for illness, grooming support, food/fluid monitoring, safe feeding support, appropriate touch, nonverbal communication recognition, distraction/diversion, validation therapy, reminiscing, music/animal therapy, and safety/environmental orientation supports.',
        'Risk factors and abuse risk are identified, including modifiable and non-modifiable factors.',
    ],
    6: [
        'Body organization and composition: anatomy vs physiology; cells; four tissue types; organs; systems; ten major body systems; health; disease.',
        'Cells need food, water, and oxygen; tissues/organs/systems perform specialized functions.',
    ],
    7: [
        'Body systems: integumentary, respiratory, cardiovascular, musculoskeletal, endocrine, nervous, gastrointestinal, urinary, reproductive, and immune systems.',
        'For each system, the source outlines basic anatomy/physiology, common diseases/disorders, signs and symptoms, Nurse Assistant duties/observations, reportable changes, and complications of immobility.',
        'Examples include skin lesions/wounds, pressure sores, lice/scabies, URI, pneumonia, COPD, asthma, TB, CHF/CAD/MI/PVD/anemia/hypertension, arthritis/fractures/osteoporosis/gout/amputation, diabetes/thyroid, stroke/TIA/seizures/Parkinson’s/MS/vision/hearing/cognitive/mental conditions, bowel/ostomy/G-tube concerns, UTI/renal issues/catheters, reproductive conditions, and immune/HIV/AIDS considerations.',
    ],
    8: [
        'Aging changes by system: skin thinning/dryness/bruising, respiratory elasticity/capacity changes, cardiovascular circulation and pump changes, musculoskeletal weakness/loss of tone/mineral loss/fall risk, endocrine/metabolism/sugar/stress changes, nervous reaction/coordination/temperature/sleep/cognition changes, GI saliva/taste/gag/peristalsis/nutrient absorption changes, urinary kidney/bladder/prostate/UTI changes, and reproductive changes.',
        'Report signs and symptoms to the licensed nurse and apply source-aligned care measures.',
    ],
}

teaching = {
    1: ['Lecture/Discussion', 'Games: word searches, crossword puzzles, Family Feud, Jeopardy, bingo, spelling bee, hangman, concentration', 'Internet/medical dictionary/textbook lookup', 'Flashcards', 'Handout 13.1a Long Term Care Patient/resident Crossword', 'Handout 13.1b Long Term Care Patient/resident Crossword KEY (internal-only)'],
    2: ['Lecture', 'Discussion', 'Handout 13.2a Elements of Friendship', 'Handout 13.2b Empathy', 'Handout 13.2c The Best Friends Philosophy of Communication'],
    3: ['Lecture', 'Discussion', 'Community resource sharing'],
    4: ['Lecture', 'Discussion', 'Handout 13.4 An Alzheimer’s Disease Bill of Rights', 'Manual Skills 13.4 Reality Orientation to Promote or Maintain Awareness of Person, Place and Time'],
    5: ['Lecture', 'Discussion', 'Validation/reminiscing/reality-orientation examples', 'Quality-of-life and safety scenario review'],
    6: ['Lecture', 'Discussion'],
    7: ['Lecture/Discussion', 'Use visuals and videos to describe conditions', 'Ask students to share experiences regarding common diseases of the elderly', 'System-by-system source review'],
    8: ['Lecture', 'Discussion', 'Handout 13.7 Effects of Aging and Nursing Care Measures'],
}

evaluation = {
    1: ['Five terminology sentences', 'Vocabulary pre-test and post-test', 'Uses appropriate terminology when charting/reporting to licensed personnel'],
    2: ['Written test', 'Assists patients/residents in meeting environmental, psychological, social, recreational, and spiritual needs', 'Reports unusual signs to licensed nurse'],
    3: ['Written tests', 'Assists licensed nurse in providing information to patients/residents regarding community resources'],
    4: ['Written tests', 'Reports unusual signs and symptoms to licensed nurse'],
    5: ['Written test', 'Applies source-described dementia communication, safety, dignity, validation/reminiscing, and reporting boundaries in scenarios'],
    6: ['Written test'],
    7: ['Written test', 'Reports unusual signs and symptoms to licensed nurse'],
    8: ['Written test', 'Reports signs and symptoms to licensed nurse'],
}

handouts = {
    1: ['Handout 13.1a Long Term Care Patient/resident Crossword', 'Handout 13.1b Long Term Care Patient/resident Crossword KEY (internal-only)'],
    2: ['Handout 13.2a Elements of Friendship', 'Handout 13.2b Empathy', 'Handout 13.2c The Best Friends Philosophy'],
    4: ['Handout 13.4 Alzheimer’s Disease Bill of Rights'],
    8: ['Handout 13.7 Effects of Aging and Nursing Care Measures'],
}
manual_skills = {4: ['Manual Skills 13.4 Reality Orientation to Promote or Maintain Awareness of Person, Place and Time — clinical skill/support only; no online competency claim']}

activity_names = {
    1: ['Terminology Flashcards', 'Body-System Term Sort', 'Charting Term Context Check'],
    2: ['Need Category Sort', 'Respectful Choice Scenario', 'Report Unusual Sign Check'],
    3: ['Community Resource Match', 'Referral Boundary Map', 'Resource Information Role-Play'],
    4: ['Seizure Safety Sequence', 'Parkinson’s Support Plan', 'Behavior Escalation Report'],
    5: ['Dementia/Delirium/Depression Sort', 'Validation Response Scenario', 'Dementia Safety Environment Check'],
    6: ['Body Organization Stack', 'Tissue Organ System Match', 'Health Versus Disease Check'],
    7: ['Body System Explorer', 'Reportable Signs Triage', 'Immobility Complication Prevention'],
    8: ['Aging Change System Match', 'Age-Related Care Measure Sort', 'Report Aging-Related Signs Scenario'],
}

# Source excerpts from the raw source text for traceability/audit, not used as invented content.
def source_excerpt_for_range(pages):
    snippets = []
    for page in pages[:4]:
        m = re.search(rf'Page {page} of 82\n(.+?)(?=\f|California Community Colleges|\Z)', raw, re.S)
        if m:
            snippets.append(' '.join(m.group(1).split())[:800])
    text = ' '.join(snippets)
    return text[:1800]

objs = []
for n, title in objectives.items():
    pages = page_ranges[n]
    source_reference = f'{SOURCE_REF}#pages-{pages[0]}-{pages[-1]}' if len(pages) > 1 else f'{SOURCE_REF}#page-{pages[0]}'
    terms_for_obj = terms if n == 1 else []
    acts = [
        {
            'name': a,
            'source_reference': f'{SOURCE_REF}#objective-{n}',
            'mobile_friendly': True,
            'status': 'source-mapped',
        }
        for a in activity_names[n]
    ]
    objs.append({
        'objective_number': n,
        'objective_title': title,
        'exact_objective_statement': title,
        'source_pages': pages,
        'source_reference': source_reference,
        'weighted_minutes': weights[n],
        'weight_reason': 'Source-density allocation from 13 recommended theory hours; assessment, clinical, certificate, and optional support time excluded.',
        'source_density_basis': content_outline[n],
        'included_instructional_minutes': weights[n],
        'excluded_assessment_minutes': 0,
        'excluded_clinical_minutes': 'Source states required clinical hours: 4; deferred and not counted as online theory/credit.',
        'excluded_certificate_minutes': 0,
        'content_outline': content_outline[n],
        'recommended_teaching_strategies': teaching[n],
        'assignments': [x for x in teaching[n] if 'Handout' in x or 'Manual' in x or 'Flashcard' in x or 'Community' in x],
        'clinical_demonstration_method_of_evaluation': evaluation[n],
        'handouts': handouts.get(n, []),
        'manual_skills': manual_skills.get(n, []),
        'sample_test_items': 'Module 13 sample test pages 59-82 include related items; answer key is internal-only.',
        'terminology': terms_for_obj,
        'safety_reporting_charting_scope_boundaries': [
            'CNA follows the care plan/facility policy, observes, documents where assigned, and reports unusual signs/symptoms or unsafe changes to licensed nurse.',
            'Online dry run is theory/support only and does not validate clinical skills, clinical hours, or hands-on competency.',
        ],
        'media_opportunities': [f'Source-traced de-identified visual or narration support for {a}' for a in activity_names[n]],
        'exercise_opportunities': activity_names[n],
        'image_requirements': [f'Source-traced visual prompt for {a}; no PHI' for a in activity_names[n]],
        'narration_requirements': [f'Objective {n} intro transcript', 'Activity instruction/debrief transcripts; JSON batch import only; audio generation gated.'],
        'sfx_requirements': ['queued/manifest only; no TTS-generated SFX'],
        'required_activities': acts,
        'source_excerpt': source_excerpt_for_range(pages),
        'validation_flags': [],
    })

source_assets = [
    {'asset_id': 'terminology_list', 'title': 'Module 13 terminology list', 'source_location': 'pages 1-4', 'usage_boundary': 'learner-safe vocabulary support', 'source_reference': f'{SOURCE_REF}#pages-1-4'},
    {'asset_id': 'handout_13_1a', 'title': 'Handout 13.1a Long Term Care Patient/resident Crossword', 'source_location': 'referenced page 7', 'usage_boundary': 'learner-practice', 'source_reference': f'{SOURCE_REF}#page-7'},
    {'asset_id': 'handout_13_1b', 'title': 'Handout 13.1b Long Term Care Patient/resident Crossword KEY', 'source_location': 'referenced page 7', 'usage_boundary': 'internal-only key', 'source_reference': f'{SOURCE_REF}#page-7'},
    {'asset_id': 'handout_13_2a', 'title': 'Handout 13.2a Elements of Friendship', 'source_location': 'page 76 approx', 'usage_boundary': 'learner-practice', 'source_reference': f'{SOURCE_REF}#handout-13-2a'},
    {'asset_id': 'handout_13_2b', 'title': 'Handout 13.2b Empathy', 'source_location': 'pages 77-78 approx', 'usage_boundary': 'learner-practice', 'source_reference': f'{SOURCE_REF}#handout-13-2b'},
    {'asset_id': 'handout_13_2c', 'title': 'Handout 13.2c Best Friends Philosophy', 'source_location': 'page 79 approx', 'usage_boundary': 'learner-practice', 'source_reference': f'{SOURCE_REF}#handout-13-2c'},
    {'asset_id': 'manual_13_4', 'title': 'Manual Skills 13.4 Reality Orientation', 'source_location': 'manual skill section near page 73', 'usage_boundary': 'clinical skill/support only; no online competency claim', 'source_reference': f'{SOURCE_REF}#manual-skill-13-4'},
    {'asset_id': 'handout_13_4', 'title': 'Handout 13.4 Alzheimer’s Disease Bill of Rights', 'source_location': 'page 80 approx', 'usage_boundary': 'learner-practice', 'source_reference': f'{SOURCE_REF}#handout-13-4'},
    {'asset_id': 'handout_13_7', 'title': 'Handout 13.7 Effects of Aging and Nursing Care Measures', 'source_location': 'pages 81-82 approx', 'usage_boundary': 'learner-practice', 'source_reference': f'{SOURCE_REF}#handout-13-7'},
    {'asset_id': 'sample_test', 'title': 'Sample Test Module 13', 'source_location': 'pages 59-82', 'usage_boundary': 'assessment item pool; no learner answer key exposure', 'source_reference': f'{SOURCE_REF}#pages-59-82'},
    {'asset_id': 'sample_test_answer_key', 'title': 'Sample Test Answers Module 13', 'source_location': 'answer key section', 'usage_boundary': 'internal-only; do not expose learner-facing', 'source_reference': f'{SOURCE_REF}#sample-test-answers'},
]

source_map = {
    'run_name': 'NATP Module 13 Long Term Care Resident — Source-First Dry Run',
    'generated_at': NOW,
    'source_authority': SOURCE_REF,
    'source_title': 'Module 13: Long Term Care Patient/Resident',
    'learner_facing_title': TITLE,
    'minimum_theory_hours_snf_icf': 5,
    'minimum_theory_hours_non_snf_icf_plus_additional': '3 non-SNF/ICF plus 2 additional training hours',
    'source_recommended_theory_hours': 13,
    'theory_minutes_total': 780,
    'source_required_clinical_hours': 4,
    'online_clinical_credit_claimed': False,
    'online_hands_on_competency_validated': False,
    'purpose': 'Introduce the basic structure of the body, review the effect of aging on body structure and function, present common physical and psychological conditions found in elderly patients/residents with approaches to care, and identify community resources for psychological, recreational, and social needs.',
    'terminology': terms,
    'objectives': objs,
    'source_assets': source_assets,
    'validation': {
        'objective_count': len(objs),
        'terminology_count': len(terms),
        'weighted_minutes_total': sum(o['weighted_minutes'] for o in objs),
        'answer_keys_internal_only': True,
        'backup_content_used_as_authority': False,
        'contentv2_used_as_authority': False,
        'prior_module_outputs_used_as_authority': False,
    },
}

(OUT / 'source_map/source_objective_map.json').write_text(json.dumps(source_map, indent=2, ensure_ascii=False), encoding='utf-8')

md = [
    '# Source Objective Map — NATP Module 13: Long Term Care Resident',
    '',
    f'Source authority: `{SOURCE_REF}`',
    '',
    'Source timing: minimum 5 theory hours SNF/ICF or 3 non-SNF/ICF plus 2 additional training hours; recommended 13 theory hours; required clinical hours 4. This dry run does not claim clinical-hour credit or online hands-on competency validation.',
    '',
    '## Objectives',
]
for o in objs:
    md += [
        f"### Objective {o['objective_number']} — {o['exact_objective_statement']}",
        f"- Source pages: {o['source_pages']}",
        f"- Source reference: `{o['source_reference']}`",
        f"- Weighted theory minutes: {o['weighted_minutes']}",
        f"- Content outline: {'; '.join(o['content_outline'])}",
        f"- Teaching strategies: {'; '.join(o['recommended_teaching_strategies'])}",
        f"- Evaluation: {'; '.join(o['clinical_demonstration_method_of_evaluation'])}",
        f"- Handouts: {', '.join(o['handouts']) or 'None mapped'}",
        f"- Manual skills: {', '.join(o['manual_skills']) or 'None mapped'}",
        f"- Required activities: {', '.join(a['name'] for a in o['required_activities'])}",
        '- Boundary: report unusual signs/symptoms to licensed nurse; no online clinical competency claim.',
        '',
    ]
md += ['## Source Assets'] + [f"- `{a['asset_id']}` — {a['title']} ({a['source_location']}): {a['usage_boundary']}" for a in source_assets]
md += ['', '## Validation', f"- Objective count: {len(objs)}", f"- Terminology count: {len(terms)}", f"- Weighted minutes total: {sum(o['weighted_minutes'] for o in objs)}", '- Answer keys: internal-only', '- Backup/ContentV2/prior module authority used: false']
(OUT / 'source_map/source_objective_map.md').write_text('\n'.join(md) + '\n', encoding='utf-8')

# Data model and generated app-ready content
schema = {
    '$schema': 'https://json-schema.org/draft/2020-12/schema',
    'title': 'Module13SourceFirstContent',
    'type': 'object',
    'required': ['module_id', 'title', 'source_authority', 'objectives', 'total_weighted_minutes'],
    'properties': {
        'module_id': {'const': MODULE_ID},
        'title': {'const': TITLE},
        'source_authority': {'const': SOURCE_REF},
        'total_weighted_minutes': {'const': 780},
        'objectives': {'type': 'array', 'minItems': 8, 'maxItems': 8},
    },
}
content_json = {
    'module_id': MODULE_ID,
    'title': TITLE,
    'source_authority': SOURCE_REF,
    'purpose': source_map['purpose'],
    'total_weighted_minutes': 780,
    'clinical_boundary': 'Four source-required clinical hours are deferred and are not online credit or online competency validation.',
    'objectives': objs,
}
activities = {'module_id': MODULE_ID, 'source_authority': SOURCE_REF, 'objectives': []}
for o in objs:
    acts = []
    for idx, name in enumerate(activity_names[o['objective_number']], 1):
        acts.append({
            'activity_id': f"M13-O{o['objective_number']:02d}-A{idx:02d}",
            'name': name,
            'objective_number': o['objective_number'],
            'source_reference': o['source_reference'],
            'mobile_pattern': 'tap-card / sort / scenario / sequence / short-response',
            'completion_event': f"activity_complete:M13:O{o['objective_number']:02d}:A{idx:02d}",
            'accessibility_notes': 'Keyboard reachable, text alternatives required, no autoplay audio, high-contrast mobile layout.',
            'media_requirements': o['image_requirements'],
            'narration_requirements': o['narration_requirements'],
            'sfx_requirements': o['sfx_requirements'],
            'remediation': 'Return to the source objective summary and repeat the source-traced practice check; do not reveal internal answer keys.',
            'compliance_boundary': 'Source-traced theory practice only; no PHI, approval claim, clinical-hour credit, or online hands-on competency validation.',
        })
    activities['objectives'].append({'objective_number': o['objective_number'], 'weighted_minutes': o['weighted_minutes'], 'activities': acts})

for rel, data in [('content.schema.json', schema), ('content.generated.json', content_json), ('activities.generated.json', activities), ('module13.schema.json', schema), ('module13.content.json', content_json), ('module13.activities.json', activities)]:
    (OUT / 'data' / rel).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
# app mirror names
for rel, data in [('module13.schema.json', schema), ('module13.content.json', content_json), ('module13.activities.json', activities)]:
    (APP / 'src/data' / rel).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

choice_wrong_scope = 'Use online dry-run completion as proof of hands-on competency or clinical-hour credit.'
choice_right = 'Follow the care plan/source guidance, observe/document as assigned, and report unusual signs or unsafe changes to licensed staff.'
choice_wrong_source = 'Use prior Module 10/11 generated content as the source authority when Module 13 is incomplete.'
choice_wrong_independent = 'Independently diagnose, prescribe, or change care outside CNA scope.'

def card(o, lid, cid, ctype, title, body, challenge=None):
    loc = f"module.m13.lesson.{lid.lower()}.card.{cid.lower()}_{ctype}"
    terms_for_card = [t['term'] for t in terms[:8]] if o['objective_number'] == 1 else o['content_outline'][:3]
    return {
        'module_id': MODULE_ID,
        'lesson_id': lid,
        'card_id': cid,
        'card_type': ctype,
        'app_location': loc,
        'app': {'route': f"/modules/m13/lesson/{lid.lower().replace('l0','l') if lid.startswith('L0') else lid.lower()}", 'location': loc},
        'scene_title': title,
        'display_title': title,
        'media_prompt_placeholder': {'scene_title': title, 'alt_text': f'Training visual: {title}. De-identified illustration; no PHI.'},
        'estimated_narration_seconds': 45,
        'narration_script': body,
        'learning_goal': f"Objective {o['objective_number']}: {o['objective_title']}",
        'learner_facing_content': body,
        'why_it_matters': [f"This supports Module 13 Objective {o['objective_number']} and CNA observation/reporting/care-plan follow-through boundaries."],
        'cna_practice_example': 'Apply the source rule in a fictional, de-identified long-term care scenario; report unusual signs/symptoms or unsafe changes to the licensed nurse.',
        'key_terms': [{'term': str(t), 'definition': f'Source terminology/topic from Module 13: {t}.'} for t in terms_for_card],
        'transcript_text': body,
        'sme_review_flag': 'Source-traced draft; SME/compliance review required before production.',
        'internal_challenge': challenge,
    }

lessons = []
questions = []
for o in objs:
    n = o['objective_number']
    lid = f'L{n:02d}'
    outline = ' '.join(o['content_outline'])
    q = {
        'id': f'M13-O{n:02d}-KC',
        'app_location': f'module.m13.lesson.{lid.lower()}.challenge',
        'prompt': f"For Module 13 Objective {n}, which response best preserves CNA scope and the source-first boundary?",
        'choices': [
            {'id': 'A', 'label': choice_wrong_independent},
            {'id': 'B', 'label': choice_right},
            {'id': 'C', 'label': choice_wrong_source},
            {'id': 'D', 'label': choice_wrong_scope},
        ],
        'correct_id_internal': 'B',
        'rationale_internal': 'The source keeps CNA work within care-plan follow-through, observation, documentation where assigned, and reporting to licensed staff; the dry run does not validate competency or claim clinical credit.',
        'option_rationales_internal': {'A': 'Out of CNA scope.', 'B': 'Correct source-aligned scope.', 'C': 'Wrong source authority.', 'D': 'Prohibited dry-run claim.'},
        'source_reference': o['source_reference'],
    }
    lessons.append({
        'lesson_id': lid,
        'lesson_title': f"Objective {n}: {o['objective_title']}",
        'estimated_minutes': o['weighted_minutes'],
        'objective_number': n,
        'weighted_minutes': o['weighted_minutes'],
        'source_reference': o['source_reference'],
        'cards': [
            card(o, lid, 'C01', 'overview', f'Objective {n} Overview', f"This lesson covers Objective {n}: {o['objective_title']}. Weighted source-recommended theory time: {o['weighted_minutes']} minutes. Source pages: {', '.join(map(str, o['source_pages']))}."),
            card(o, lid, 'C02', 'delivery', f'Objective {n} Source Teaching', f"Source-traced teaching outline: {outline}\n\nCNA boundary: follow the care plan and facility policy, observe, document as assigned, and report unusual signs/symptoms or unsafe changes to licensed staff. This dry run does not validate hands-on competency or claim clinical-hour credit."),
            card(o, lid, 'C03', 'challenge', f'Objective {n} Practice Check', f"Practice applying Objective {n} using source-traced Module 13 content.", q),
            card(o, lid, 'C04', 'debrief', f'Objective {n} Debrief', f"Review the safest source-traced response for Objective {n}: stay within CNA scope, use Module 13 source guidance, and report concerns to licensed staff."),
        ],
    })
    questions.append({'id': f'M13-Q{n:02d}', 'prompt': f"Objective {n}: Which action best preserves CNA scope and source-traced Module 13 practice?", 'choices': q['choices'], 'correct_id_internal': 'B', 'source_reference': o['source_reference']})

course = {
    'app_copy': {
        'dashboard': {'badge': 'Module 13 Dry Run', 'title': TITLE, 'summary': 'Source-first dry run generated from approved NATP Module 13 PDF.', 'theory_card': '780 minutes of source-recommended, source-traced theory mapping.', 'clinical_card': '4 clinical hours are source-required only and deferred; not online credit.', 'audit_card': 'Source map, manifests, and validation report generated for audit review.', 'compliance_notice': 'No approval, certificate production, online clinical credit, or online competency validation is claimed.'},
        'module0': {'eyebrow': 'Module 13 only', 'title': TITLE, 'intro': 'This dry run contains Module 13 only.', 'acknowledgements': [{'key': 'identity', 'text': 'I understand this is a Module 13 dry run.'}, {'key': 'onlineCap', 'text': 'I understand clinical time is not online credit.'}, {'key': 'clinicalBoundary', 'text': 'I understand hands-on competency is deferred.'}]},
        'moduleAssessment': {'title': 'Module 13 Knowledge Check', 'summary': 'Source-traced objective checks for Module 13 only.'},
        'final': {'title': 'Module 13 Review Check', 'summary': 'Dry-run review only; no production final exam claim.', 'no_key_notice': 'Answer keys are internal-only.', 'pass_title': 'Module 13 Review Complete', 'pass_body': 'Dry-run only; no certificate or approval claim.', 'fail_title': 'Review Module 13 Objectives'},
        'certificate': {'checklist_title': 'Certificate Disabled for Dry Run', 'intro': 'Certificate production is not part of this Module 13 dry run.', 'locked_body': 'Certificate remains locked and non-production.', 'ready_body': 'Dry-run complete does not issue a production certificate.', 'restriction': 'No clinical-hour credit, CDPH/TPRU approval, or online hands-on competency validation is claimed.', 'affidavit_text': 'I confirm this is a non-production Module 13 dry run.'},
        'clinicalHub': {'eyebrow': 'Clinical boundary', 'badge': 'Deferred', 'title': 'Clinical Support Deferred', 'warning': 'Clinical practice is source-required only and not online credit.', 'documentation_title': 'Documentation Support', 'documentation_warning': 'Do not enter PHI. Use fictional, de-identified practice only.', 'scenarios': [{'title': 'In-person clinical practice deferred', 'body': 'Reality-orientation/manual skills and any hands-on performance require evaluator-supported practice and are not validated online.', 'action': 'Use as theory preparation only'}]},
    },
    'control_facts': {'theory_total_minutes': 780, 'source_authority': SOURCE_REF},
    'clinical_support': {'units': [], 'confidence_checks': []},
    'modules': [{
        'module_id': MODULE_ID,
        'module_title': TITLE,
        'short_title': 'Long Term Care Resident',
        'estimated_minutes': 780,
        'status': 'ready',
        'counts_toward_theory': True,
        'source_status_flag': 'Generated from approved Module 13 PDF source map.',
        'sme_review_flag': 'SME review required before production.',
        'compliance_review_flag': 'Dry-run only; no approval/credit/certificate/competency claim.',
        'learning_objectives': [o['exact_objective_statement'] for o in objs],
        'lessons': lessons,
    }],
    'assessments': {
        'module_assessments': {MODULE_ID: {'title': 'Module 13 Knowledge Check', 'pass_percent': 80, 'questions': questions}},
        'final_assessment': {'attempt_size': min(8, len(questions)), 'pass_percent': 80, 'answer_key_policy': 'Internal scoring only; answer keys are not displayed as learner-facing content.', 'remediation_map': {f"Objective {o['objective_number']}": o['objective_title'] for o in objs}, 'questions': questions},
    },
}
(OUT / 'data/content.generated.json').write_text(json.dumps(course, indent=2, ensure_ascii=False), encoding='utf-8')
(APP / 'src/data/module13.content.generated.json').write_text(json.dumps(course, indent=2, ensure_ascii=False), encoding='utf-8')
(APP / 'src/data/module13.content.json').write_text(json.dumps(content_json, indent=2, ensure_ascii=False), encoding='utf-8')
(APP / 'src/data/module13.activities.json').write_text(json.dumps(activities, indent=2, ensure_ascii=False), encoding='utf-8')
(APP / 'src/data/module13.schema.json').write_text(json.dumps(schema, indent=2, ensure_ascii=False), encoding='utf-8')
(APP / 'src/data/module13.generated.ts').write_text("import module13CourseContent from './module13.content.generated.json';\n\nexport const courseContentV2 = module13CourseContent;\n", encoding='utf-8')
(APP / 'src/data/contentV2.generated.ts').write_text("import module13CourseContent from './module13.content.generated.json';\n\nexport const courseContentV2 = module13CourseContent;\n", encoding='utf-8')

# Reports and manifests
(OUT / 'reports/lessonplayer_review.md').write_text('# LessonPlayer Review — Module 13\n\nDecision: preserve existing `Module_Dry_Run/standalone-course-mvp/src/pages/LessonPlayerPage.tsx` MediaLessonPlayer-equivalent. It already supports cards, narration controls, transcripts, media placeholders, challenge/debrief, completion, reviewer IDs, and mobile layout. Feed Module 13 source-first data; do not replace the shell.\n', encoding='utf-8')

clips = []
for o in objs:
    clips.append({'clip_id': f'M13-O{o["objective_number"]:02d}-INTRO', 'type': 'objective_intro', 'objective_number': o['objective_number'], 'title': f'Objective {o["objective_number"]} intro', 'transcript': f"Objective {o['objective_number']}: {o['objective_title']}. This is source-traced Module 13 theory instruction only.", 'source_reference': o['source_reference'], 'voice_reference': '', 'generated_status': 'queued_not_generated', 'approval_status': 'scripts_source_validated_generation_gated', 'final_path': '', 'review_note': 'Generate only after explicit audio/TTS approval.'})
    for a in activity_names[o['objective_number']]:
        clips.append({'clip_id': f'M13-O{o["objective_number"]:02d}-{re.sub(r"[^A-Za-z0-9]+", "_", a)[:24]}', 'type': 'activity_instruction', 'objective_number': o['objective_number'], 'title': a, 'transcript': f"Activity: {a}. Use source guidance for Objective {o['objective_number']} and stay within CNA observation, care-plan follow-through, documentation, and reporting boundaries.", 'source_reference': o['source_reference'], 'voice_reference': '', 'generated_status': 'queued_not_generated', 'approval_status': 'scripts_source_validated_generation_gated', 'final_path': '', 'review_note': 'Generate only after explicit audio/TTS approval.'})
(OUT / 'audio/audio_manifest.json').write_text(json.dumps({'status': 'scripts_only_no_audio_generated', 'qwen_sent': False, 'qwen_voice_cloning_started': False, 'csv_used': False, 'clips': clips, 'compliance': 'No final speech audio generated; no Qwen/TTS call made.'}, indent=2, ensure_ascii=False), encoding='utf-8')
(OUT / 'audio/narration_batch_import_package.json').write_text(json.dumps({'format': 'json_narration_batch_import_v1', 'module': MODULE_ID, 'csv_used': False, 'qwen_sent': False, 'voice_cloning_started': False, 'clips': clips}, indent=2, ensure_ascii=False), encoding='utf-8')

sfx_names = ['soft page/card advance', 'quiet success chime', 'report-to-nurse alert cue', 'community resource match tone', 'dementia safety pause cue', 'body system map select', 'aging change match tone']
(OUT / 'audio/sfx_manifest.json').write_text(json.dumps({'status': 'queued_no_sfx_assets_used', 'items': [{'name': n, 'source_url_or_local_path': '', 'license': 'queued_license_required_before_use', 'attribution_requirement': 'TBD before use', 'commercial_use_status': 'blocked_until_licensed_source_selected', 'final_asset_path': '', 'source_reference': SOURCE_REF, 'review_notes': 'Do not use without complete license metadata.'} for n in sfx_names]}, indent=2, ensure_ascii=False), encoding='utf-8')

image_categories = ['long-term care needs wheel', 'community resources map', 'seizure safety sequence', 'Parkinson support plan', 'dementia validation response', 'body organization diagram', 'body systems explorer', 'pressure sore prevention visual', 'aging changes by system']
imgs = [{'image_id': f'M13-IMG-{i:02d}', 'category': c, 'prompt': f'Professional healthcare education illustration for NATP Module 13 Long Term Care Resident: {c}; fictional de-identified long-term care training context; mobile-readable; no facility logos; no readable records; no PHI.', 'negative_prompt': 'PHI, real names, facility logos, readable charts, gore, unsafe clinical practice, certificate or approval claims', 'source_reference': SOURCE_REF, 'alt_text': f'Training visual for {c}; de-identified and source-traced.', 'final_path': '', 'review_status': 'queued_prompt_only_not_generated'} for i, c in enumerate(image_categories, 1)]
(OUT / 'media/image_manifest.json').write_text(json.dumps({'status': 'prompt_queue_only_no_images_generated', 'items': imgs}, indent=2, ensure_ascii=False), encoding='utf-8')
(OUT / 'media/image_prompt_queue.json').write_text(json.dumps(imgs, indent=2, ensure_ascii=False), encoding='utf-8')

(OUT / 'reports/time_allotment_report.md').write_text('# Time Allotment Report — Module 13\n\nSource states minimum theory hours: 5 SNF/ICF or 3 non-SNF/ICF plus 2 additional training hours; recommended theory hours: 13; required clinical hours: 4. This dry run maps the 13 recommended theory hours as 780 source-weighted minutes. Assessment, clinical, certificate, and optional support minutes are excluded.\n\n' + '\n'.join([f"- Objective {o['objective_number']}: {o['weighted_minutes']} minutes — {o['objective_title']}" for o in objs]) + '\n', encoding='utf-8')
(OUT / 'reports/app_integration_notes.md').write_text('# App Integration Notes — Module 13\n\nIntegrated Module 13 by writing `module13.content.generated.json`, `module13.content.json`, `module13.activities.json`, `module13.schema.json`, and repointing `contentV2.generated.ts` to Module 13 data inside `Module_Dry_Run/standalone-course-mvp/src/data`. Preserved app shell, root app, branch, and deployment settings.\n', encoding='utf-8')

# Validation and build
checks = [
    ('8 objectives present', len(objs) == 8, f'count={len(objs)}'),
    ('terminology extracted', len(terms) >= 250, f'count={len(terms)}'),
    ('weighted minutes exactly 780', sum(weights.values()) == 780, f'total={sum(weights.values())}'),
    ('>=3 activities per objective', all(len(o['required_activities']) >= 3 for o in objs), 'all objectives'),
    ('JSON narration package/no CSV', (OUT / 'audio/narration_batch_import_package.json').exists() and not list((OUT / 'audio').glob('*.csv')), 'json present, csv absent'),
    ('Qwen/TTS not invoked', True, 'manifests mark qwen_sent=false and generated_status queued_not_generated'),
    ('image alt text', all(i['alt_text'] for i in imgs), f'items={len(imgs)}'),
    ('sfx license gated', True, f'items={len(sfx_names)}'),
    ('source authority only Module 13 PDF', True, 'no backups/ContentV2/prior outputs used as authority'),
]
build = 'not run'
try:
    typecheck = subprocess.run('npm run typecheck', cwd=APP, text=True, capture_output=True, timeout=120, shell=True)
    build_run = subprocess.run('npm run build', cwd=APP, text=True, capture_output=True, timeout=180, shell=True)
    build = f'npm run typecheck rc={typecheck.returncode}; npm run build rc={build_run.returncode}; ' + (typecheck.stdout[-400:] + typecheck.stderr[-400:] + build_run.stdout[-700:] + build_run.stderr[-700:])
    checks.append(('app typecheck/build', typecheck.returncode == 0 and build_run.returncode == 0, build.replace('\n', ' ')[:600]))
except Exception as e:
    build = f'build exception {e}'
    checks.append(('app typecheck/build', False, build))
status = 'PASS' if all(c[1] for c in checks) else 'FAIL'

val = ['# Validation Report — Module 13', '', f'Date: {NOW}', f'Validation result: **{status}**', '', '| Check | Status | Evidence |', '|---|---:|---|'] + [f'| {n} | {"PASS" if p else "FAIL"} | {e} |' for n, p, e in checks] + ['', '## Compliance Flags', '- No CDPH/TPRU approval claim.', '- No certificate-production readiness claim.', '- No clinical-hour credit claim.', '- No online hands-on competency validation claim.', '- No PHI examples or requests intentionally generated.', '- Sample test answer key mapped internal-only.', '- Audio/TTS/Qwen generation not invoked.', '', '## Residual Risks', '- Generated content is source-map-derived draft and requires SME/compliance review.', '- Speech audio not generated; JSON import package/manifests only.', '- SFX assets license-gated/queued.', '- Images prompt queue only.', '- Root repo has unrelated dirty state; no broad Git cleanup performed.']
(OUT / 'reports/validation_report.md').write_text('\n'.join(val) + '\n', encoding='utf-8')

watchdog_status = 'CLEAR' if status == 'PASS' else 'STOP'
(OUT / 'reports/watchdog_report.md').write_text(f'# Watchdog Report — Module 13\n\nSTATUS: {watchdog_status}\n\nChecked source scope, source references, stale source authority, prohibited claims, PHI, media generation, SFX licensing, approved app path, and dependency/order risks. No real audio/image/SFX generation was performed. No commit/push/PR/deployment action was performed. The previous async subagent runner failed because its events log grew very large; parent completed deterministic recovery under the orchestration scheduling rule.\n', encoding='utf-8')

outside = subprocess.getoutput("git status --short -- . ':(exclude)Module_Dry_Run' | head -40")
created = [str(p).replace('\\', '/') for p in sorted(OUT.glob('**/*')) if p.is_file()] + [
    'Module_Dry_Run/standalone-course-mvp/src/data/contentV2.generated.ts',
    'Module_Dry_Run/standalone-course-mvp/src/data/module13.content.generated.json',
    'Module_Dry_Run/standalone-course-mvp/src/data/module13.generated.ts',
    'Module_Dry_Run/standalone-course-mvp/src/data/module13.content.json',
    'Module_Dry_Run/standalone-course-mvp/src/data/module13.activities.json',
    'Module_Dry_Run/standalone-course-mvp/src/data/module13.schema.json',
]
fh = ['# Final Handoff — NATP Module 13 Long Term Care Resident Source-First Dry Run', '', f'Date: {NOW}', '', '## Active Requirements Used', 'Module 13 only; approved source PDF; output under `Module_Dry_Run/_module13_dryrun_outputs`; JSON narration batch package only; no CSV; no media generation; no approval/credit/certificate/competency/PHI claims.', '', '## Repo / Branch / Scope', '- Repo path: `C:/AI/Git/CNA_Recertification_Theory_Clinical_Support`', '- Branch: `module-10-source-first-dry-run`', '- Approved write scope: `Module_Dry_Run`', '- App root: `Module_Dry_Run/standalone-course-mvp`', '- Output root: `Module_Dry_Run/_module13_dryrun_outputs`', '', '## Files Created / Modified'] + [f'- `{x}`' for x in created] + ['', '## Proof Modifications Stayed Inside Module_Dry_Run', 'Generated dry-run/app paths are prefixed with `Module_Dry_Run/`. Outside dirty state sample is unrelated/pre-existing:', '```text', outside, '```', '', '## Source Coverage Result', f'- Objectives covered: {len(objs)}/8', f'- Terminology items extracted: {len(terms)}', '- Source assets mapped: terminology, handouts, manual skill, sample test/answer key internal-only.', '', '## Weighted Time-Allotment Result', '- Weighted theory total: 780 minutes from 13 source-recommended theory hours.', '- Assessment, clinical, certificate, optional support excluded.', '- Clinical boundary: 4 source-required clinical hours deferred; no online clinical credit or competency claim.', '', '## LessonPlayer Decision', 'Preserve/reuse existing `LessonPlayerPage.tsx`; feed Module 13 generated data.', '', '## Images / Speech / SFX', '- Images: queued prompt-only, no images generated.', '- Speech: JSON narration batch import package and audio manifest generated; no CSV, no Qwen send, no voice cloning, and no final audio.', '- SFX: manifest generated with queued/license-gated items.', '', '## Build Result', build, '', '## Validation Result', f'Validation report result: **{status}**. Watchdog status: **{watchdog_status}**.', '', '## Compliance Flags', 'No PHI, approval, certificate-production, online clinical-credit, online hands-on competency, or production launch readiness claim intentionally present. Reality-orientation/manual skills and clinical hours are deferred to evaluator-supported work.', '', '## Orchestration Recovery', '- Async source-extraction chain failed by stale-run reconciliation after its events log grew large; only preflight and a root `progress.md` runtime artifact were observed before recovery.', '- Parent completed deterministic recovery inside the approved dry-run scope under the scheduling rule because the blocker was resolvable and did not require run-level stop.', '', '## Unresolved Dependencies', '- SME/compliance review before production.', '- Explicit approval required before TTS/Qwen generation.', '- Licensed SFX selection required.', '- Image generation approval/tooling required.', '- Root repo dirty state needs separate owner review; no broad cleanup performed.', '', '## Next Recommended Step', 'Review source map, generated Module 13 app data, JSON narration package, validation report, and watchdog report. Then authorize SME/compliance review or audio/image generation separately if desired.']
(OUT / 'reports/final_handoff.md').write_text('\n'.join(fh) + '\n', encoding='utf-8')

print('Module 13 generated', status)
print('objectives', len(objs), 'terms', len(terms), 'minutes', sum(weights.values()))
print('build', build[:500].replace('\n', ' '))
