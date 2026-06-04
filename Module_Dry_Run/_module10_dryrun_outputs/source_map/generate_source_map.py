import json
from pathlib import Path

OUT = Path('Module10_Dry_Run/_module10_dryrun_outputs/source_map')
OUT.mkdir(parents=True, exist_ok=True)
SOURCE = 'CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf'
weights = {1:12,2:8,3:22,4:6,5:8,6:12,7:7,8:10,9:9,10:7,11:12,12:6,13:8,14:24,15:15,16:14}
objectives_text = {
1:'Define key terminology',
2:'Describe what is meant by vital signs, their purpose, and observations made while performing the procedures',
3:'Discuss the use of temperature as an indicator of body function',
4:'Describe nursing measures to raise and lower the temperature of the body',
5:'Describe the circulatory system as it relates to pulse, and identify the pulse sites',
6:'Describe factors that increase and decrease pulse, and the qualities to observe in taking a pulse',
7:'Define and describe respiration and factors that affect respiratory rate',
8:'Describe observations to be made when measuring respirations',
9:'Describe abnormal breathing patterns',
10:'Describe the process for taking TPR as a combined procedure',
11:'Describe what happens in the circulatory system to produce blood pressure',
12:'Identify factors that increase or decrease blood pressure',
13:'Identify parts of the blood pressure equipment',
14:'Discuss the procedure for taking a blood pressure reading',
15:'Discuss observation and reporting of patient’s/resident’s pain',
16:'Record vital signs on chart, graph, and Nursing Assistant notes',
}
pages = {1:[4],2:[4],3:[5,6,7],4:[7],5:[8],6:[8,9],7:[9],8:[10],9:[10],10:[11],11:[11,12],12:[12,13],13:[13],14:[13,14],15:[14,15,16],16:[16]}
terms = ['Afebrile','Axilla','Celsius','Fahrenheit','Febrile','Metabolism','Mucosa','Pyrexia','Tympanic','Aneroid manometer','Bell','Diaphragm','Diastolic','Hypertension','Hypotension','Orthostatic hypotension','Pre-hypertension','Pulse pressure','Sphygmomanometer','Stethoscope','Systolic','Apical','Arrhythmia','Bounding','Brachial','Bradycardia','Carotid','Pulse deficit','Radial','Rhythm','Thready','Tachycardia','Abdominal respirations','Apnea','Bradypnea','Cheyne-Stokes','Cyanosis','Diaphragm','Dyspnea','Labored respiration','Orthopnea','Shallow respiration','Stertorous','Tachypnea','Temperature, Pulse, Respiration (TPR)','Acute pain','Chronic pain','Phantom pain','Pain scales']
activity_names = {
1:['Vital Signs Flashcard Deck','Crossword Quest','Five-Term Report Sentence'],
2:['Vital Signs Dashboard','Resident Room Spot-Check','Vital Signs Chart Builder'],
3:['Heat Balance Simulator','Thermometer Museum','Temperature Route Choice'],
4:['Raise or Lower Sort','Comfort Switchboard','Fever/Chill Micro-Scenario'],
5:['Pulse Site Body Map','Heart-to-Artery Animation','Site Match Speed Round'],
6:['Pulse Detective','Beat Trainer','One-Full-Minute Practice'],
7:['Breath Cycle Loop','Respiration Factor Race','Normal Breathing Pick'],
8:['Respiration Observation Lens','Cyanosis Alert','Report Now or Routine?'],
9:['Breathing Pattern Theater','Pattern Match','Urgency Ladder'],
10:['TPR Flow Timeline','Do Not Break the Flow','Memory Sticky Note'],
11:['Artery Pressure Pump','First Sound / Last Sound Demo','BP Fraction Builder'],
12:['BP Elevator Game','Before You Take BP Checklist','False Reading Mini-Lab'],
13:['Equipment Labeling Lab','Manual vs Automated Sort','Clean Setup Challenge'],
14:['One-Step / Two-Step BP Procedure Player','Cuff Placement Coach','Do Not Use This Arm'],
15:['Pain Scale Role Play','Nonverbal Pain Clue Hunt','Bias Check Scenario'],
16:['TPR/BP Charting Sandbox','Find the Charting Error','Report + Record Simulation'],
}
content = {
1:['review listed terminology','spell/pronounce terms accurately','use terms in proper charting/reporting context'],
2:['vital signs are temperature, pulse, respirations, blood pressure','pain has measurable effects on vital signs','vital signs indicate body-system function/change','observe skin color/temperature, behavior, comfort and pain statements'],
3:['temperature balances heat gained/lost','hypothalamus regulates temperature','heat production via cellular activity, metabolism, muscle activity, hormones','heat loss via skin, lungs, elimination','heat conservation by reduced perspiration/blood flow and shivering','oral, rectal, tympanic, axillary, temporal sites','glass/digital/electronic/disposable/tympanic/temporal thermometers','normal ranges and route differences','contraindications and abnormal reporting'],
4:['raise temperature: warmer room, coverings, hot liquids, warm baths/soaks','lower temperature: cooler room, remove coverings, cool liquids, cool bath/sponging'],
5:['pulse is arterial wall expansion after heart contraction','count palpated expansions for pulse rate','average adult pulse 60-100/minute','pulse sites: carotid, apical, brachial, radial, femoral, popliteal, dorsalis pedis'],
6:['increase pulse: exercise, fever, hemorrhage, pain, shock, strong emotions, tachycardia over 100','decrease pulse: sleep/rest, depression, drugs, athlete conditioning, bradycardia below 60','qualities: rate, rhythm, strength/force, thready, bounding','report irregular rhythm even if rate normal'],
7:['respiration is oxygen/carbon dioxide exchange in lungs','breathing is inhalation/exhalation','medulla regulation','normal adult rate 12-20/minute','normal breathing quiet, effortless, regular','increase/decrease factors'],
8:['observe rate, rhythm, depth, symmetry, effort, discomfort, position, sounds','observe color of skin/mucous membranes/nail beds for cyanosis','observe behavior changes','report rates above/below normal'],
9:['abnormal patterns: labored, orthopnea, stertorous, abdominal, shallow, dyspnea, tachypnea, bradypnea, apnea, Cheyne-Stokes','report abnormal breathing or appearance/behavior change to licensed nurse'],
10:['take temperature first, pulse second, respirations third','remember pulse while counting respirations','do not stop to record pulse before respirations','report abnormal findings'],
11:['blood pressure is force of blood against artery walls','systolic first/highest pressure; diastolic second/lowest pressure','sounds correspond to mm Hg readings','record systolic/diastolic fraction','normal/abnormal ranges, pre-hypertension, hypertension, hypotension, pulse pressure'],
12:['raising factors: strong emotion, exercise, standing/sitting, excitement, pain, decreased vessel size, digestion, improperly placed cuff','lowering factors: rest/sleep, lying down, depression, shock, hemorrhage'],
13:['manual sphygmomanometer parts: cuff, bulb, manometer','stethoscope parts/use','electronic sphygmomanometer: automated inflation/deflation, digital display, no stethoscope','facility monitoring devices may measure multiple vital signs'],
14:['BP usually measured at brachial artery; popliteal only when ordered','resident at rest and LSS position order','manometer calibration at 0','appropriate cuff size and false high/low errors','do not use arms/sides with IV, burns/injuries, paralysis, amputation, cast, trauma, dialysis site, mastectomy/breast surgery','arm level with heart, bare arm, sphygmomanometer at eye level','one-step/two-step methods','report abnormal BP'],
15:['pain effects on vital signs','pain not normal aging; warning/distress signal','CNA observation responsibility; residents may not verbalize','individual/cultural response, anxiety/stress, take seriously and avoid judging','acute/chronic/phantom pain','signs: increased pulse/respirations/BP, sounds, nausea/vomiting, sweating, facial/jaw/body tension, restlessness, mobility difficulty','ask about pain, use pain scale, describe location/frequency/duration/quality, observe expression/movement/respiration, report complaints','comfort measures'],
16:['report normal/abnormal TPR to licensed nurse','record on flow sheets, graphic records and Nursing Assistant notes according to policy','record in TPR order','R for rectal, AX for axillary','note non-radial pulse site','record respiratory rate','chart BP as systolic/diastolic fraction; note alternate site','practice facility flow/graphic sheets'],
}
teaching={1:['Lecture/Discussion','Games: word searches, crossword puzzles, Family Feud, Jeopardy, bingo, spelling bee, hangman, concentration','Internet/medical dictionary/textbook lookup','Create flashcards','Handout 10.1a','Handout 10.1b'],2:['Lecture/Discussion','Demonstration and return demonstration','Handout 10.2'],3:['Lecture/Discussion','Display thermometer types','Identify types','Demonstration/return demonstration with thermometers and contraindications','Manual Skills 10.3a-e','Ear temperature visual aid'],4:['Lecture','Discussion'],5:['Lecture/Discussion','Pulse-site visual aid','Role play','Advanced pulse deficit research/demonstration'],6:['Lecture/Discussion','Demonstration/return demonstration for radial/apical pulse full minute','Role play','Manual Skills 10.6a/10.6b'],7:['Lecture','Discussion'],8:['Lecture/Discussion','Manual Skills 10.8','Demonstration/return demonstration','Role play'],9:['Lecture','Discussion'],10:['Lecture/Discussion','Demonstration/return demonstration of TPR','Role play'],11:['Lecture/Discussion','Pulse pressure research'],12:['Lecture','Discussion'],13:['Lecture/Discussion','Show equipment'],14:['Lecture/Discussion','Manual Skills 10.14a/10.14b','Display equipment and identify parts','Demonstration/return demonstration','Role play'],15:['Lecture/Discussion','Handout 10.15','Role play pain scale','Discuss pain-management barriers'],16:['Lecture/Discussion','Facility flow chart/graphic sheets practice','Role play and record vital signs']}
evalm={1:['Five terminology sentences','Vocabulary pre/post test','Appropriate terminology in charting/reporting'],2:['Observe measuring vital signs','Ask skin/temperature/behavior changes'],3:['Written test','Demonstrate oral/axillary/temporal/rectal temperature','Use mercury-free glass/electronic/digital/tympanic/temporal thermometers','Report abnormal temperature'],4:['Written test','Observation in clinical setting'],5:['Written test','Locate major pulse sites'],6:['Written test','Measure radial/brachial pulse for full minute','Report abnormal pulse'],7:['Written test'],8:['Written test','Measure respirations','Report rate above/below normal'],9:['Written test','Report abnormal breathing pattern or appearance/behavior change'],10:['Demonstrate TPR in one process','Report abnormal to licensed nurse'],11:['Written test'],12:['Written test'],13:['Written test'],14:['Written test','Measure blood pressure','Report abnormal blood pressure'],15:['Written test','Observation in clinical setting'],16:['Written test','Accurately record vital signs on facility flow/graphic sheets per policy']}
manuals={3:['Manual Skills 10.3a Oral Temperature','Manual Skills 10.3b Axillary Temperature','Manual Skills 10.3c Tympanic Temperature','Manual Skills 10.3d Rectal Temperature','Manual Skills 10.3e Electronic Temperature'],6:['Manual Skills 10.6a Radial Pulse','Manual Skills 10.6b Apical Pulse','Manual Skill Count and Record Radial Pulse'],8:['Manual Skill 10.8 Count and Record Respiration'],14:['Manual Skills 10.14a Blood Pressure One-Step','Manual Skills 10.14b Blood Pressure Two-Step']}
handouts={1:['Handout 10.1a Vital Signs Crossword','Handout 10.1b Vital Signs Crossword Key (internal/instructor key)'],2:['Handout 10.2 Vital Signs Chart'],15:['Handout 10.15 Pain Scale']}
objs=[]
for n in range(1,17):
    objs.append({
        'objective_number': n,
        'objective_title': objectives_text[n],
        'exact_objective_statement': objectives_text[n],
        'source_pages': pages[n],
        'source_reference': f'{SOURCE}#pages-{"-".join(map(str,pages[n]))}',
        'weighted_minutes': weights[n],
        'weight_reason': 'User-approved weighted allocation based on source content density; assessment, clinical, certificate, and optional support time excluded.',
        'source_density_basis': content[n],
        'included_instructional_minutes': weights[n],
        'excluded_assessment_minutes': 0,
        'excluded_clinical_minutes': 'Source recommends 6 clinical hours for module overall; deferred to in-person/evaluator-supported work and not counted here.',
        'excluded_certificate_minutes': 0,
        'content_outline': content[n],
        'recommended_teaching_strategies': teaching.get(n,[]),
        'assignments': [x for x in teaching.get(n,[]) if 'Handout' in x or 'research' in x.lower() or 'flashcards' in x.lower() or 'practice' in x.lower()],
        'clinical_demonstration_method_of_evaluation': evalm.get(n,[]),
        'handouts': handouts.get(n,[]),
        'manual_skills': manuals.get(n,[]),
        'sample_test_items': 'Module 10 sample test pages 17-22 include related items; answer key page 23 is internal-only.',
        'terminology': terms if n==1 else [t for t in terms if any(k.lower() in t.lower() for k in objectives_text[n].split()[:3])],
        'safety_reporting_charting_scope_boundaries': ['CNA observes/measures/records/reports within facility policy; abnormal findings and complaints are reported to licensed nurse; no online hands-on competency validation is claimed.'],
        'media_opportunities': ['mobile diagram/visual placeholder/source-traced prompt only until generated assets approved'],
        'exercise_opportunities': activity_names[n],
        'image_requirements': [f'Source-traced visual for {activity_names[n][0]}', f'Source-traced visual for {activity_names[n][1]}', f'Source-traced visual for {activity_names[n][2]}'],
        'narration_requirements': [f'Objective {n} intro transcript', 'Activity instructions and debrief transcripts; Qwen CI-ION voice generation gated until scripts validated.'],
        'sfx_requirements': ['queued/manifest only unless licensed source is available; do not synthesize SFX with TTS'],
        'required_activities': [{'name': a, 'source_reference': f'{SOURCE}#objective-{n}', 'mobile_friendly': True, 'status':'source-mapped'} for a in activity_names[n]],
        'validation_flags': []
    })
assets=[
('terminology_list','Terminology list','pages 1-2','learner-safe'),('handout_10_1a','Handout 10.1a Vital Signs Crossword','referenced page 4; handout body later in PDF','learner-practice'),('handout_10_1b','Handout 10.1b Vital Signs Crossword Key','referenced page 4','internal-only key'),('handout_10_2','Handout 10.2 Vital Signs Chart','referenced page 4','learner-practice'),('manual_10_3a','Manual Skills 10.3a Oral Temperature','pages 24-25','clinical skill; no online competency claim'),('manual_10_3b','Manual Skills 10.3b Axillary Temperature','pages 26-27','clinical skill; no online competency claim'),('manual_10_3c','Manual Skills 10.3c Tympanic Temperature','pages 28-29','clinical skill; no online competency claim'),('manual_10_3d','Manual Skills 10.3d Rectal Temperature','pages 30-31','clinical skill; no online competency claim'),('manual_10_3e','Manual Skills 10.3e Electronic Temperature','pages 32-33','clinical skill; no online competency claim'),('manual_10_6b_apical','Manual Skills 10.6b Apical Pulse','pages 34-36','clinical skill; no online competency claim'),('manual_radial_pulse','Manual Skill Count and Record Radial Pulse','pages 36-37','clinical skill; no online competency claim'),('manual_10_8','Manual Skill 10.8 Count and Record Respiration','page 38','clinical skill; no online competency claim'),('manual_10_14a','Manual Skills 10.14a Blood Pressure One-Step','pages 39-40','clinical skill; no online competency claim'),('manual_10_14b','Manual Skills 10.14b Blood Pressure Two-Step','pages 41-42','clinical skill; no online competency claim'),('handout_10_15','Handout 10.15 Pain Scale','referenced page 15','learner-practice'),('sample_test','Sample Test Module 10','pages 17-22','assessment item pool; no answer key exposure'),('sample_test_answer_key','Sample Test Answer Key','page 23','internal-only; do not expose learner-facing')]
source_assets=[{'asset_id':i,'title':t,'source_location':loc,'usage_boundary':b,'source_reference':SOURCE} for i,t,loc,b in assets]
data={'run_name':'NATP Module 10 Vital Signs — Source-First Dry Run','source_authority':SOURCE,'source_title':'Module 10: Vital Signs','learner_facing_title':'NATP Module 10: Vital Signs','theory_minutes_total':180,'source_recommended_clinical_hours':6,'online_clinical_credit_claimed':False,'online_hands_on_competency_validated':False,'purpose':'Prepare students to know how, when and why vital signs are taken; report and chart procedures; measure temperature, pulse, respirations, and blood pressure; recognize and report normal and abnormal findings.','terminology':terms,'objectives':objs,'source_assets':source_assets,'validation':{'objective_count':len(objs),'weighted_minutes_total':sum(o['weighted_minutes'] for o in objs),'answer_keys_internal_only':True,'backup_content_used_as_authority':False,'contentv2_used_as_authority':False}}
(OUT/'source_objective_map.json').write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding='utf-8')
md=['# Source Objective Map — NATP Module 10: Vital Signs','',f'Source authority: `{SOURCE}`','','Clinical boundary: source recommends 6 clinical hours, deferred to in-person/evaluator-supported work; no online clinical credit or competency validation.','','## Objectives']
for o in objs:
    md += [f"### Objective {o['objective_number']} — {o['exact_objective_statement']}",f"- Source pages: {o['source_pages']}",f"- Weighted theory minutes: {o['weighted_minutes']}",f"- Content outline: {'; '.join(o['content_outline'])}",f"- Teaching strategies: {'; '.join(o['recommended_teaching_strategies'])}",f"- Evaluation: {'; '.join(o['clinical_demonstration_method_of_evaluation'])}",f"- Handouts: {', '.join(o['handouts']) or 'None mapped'}",f"- Manual skills: {', '.join(o['manual_skills']) or 'None mapped'}",f"- Required activities: {', '.join(a['name'] for a in o['required_activities'])}",'- Boundary: abnormal findings/complaints report to licensed nurse; no online clinical competency claim.','']
md += ['## Source Assets']
for a in source_assets:
    md.append(f"- `{a['asset_id']}` — {a['title']} ({a['source_location']}): {a['usage_boundary']}")
md += ['','## Validation','',f"- Objective count: {len(objs)}",f"- Weighted minutes total: {sum(o['weighted_minutes'] for o in objs)}",'- Answer keys: internal-only', '- Backup/ContentV2 authority used: false']
(OUT/'source_objective_map.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print('wrote', OUT/'source_objective_map.json')
print('objectives',len(objs),'total',sum(o['weighted_minutes'] for o in objs),'assets',len(source_assets))
