const fs = require('fs');
const path = require('path');
const p = path.join(__dirname, '..', 'data', 'courseContentV2.json');
const d = JSON.parse(fs.readFileSync(p, 'utf8'));
const targets = (process.argv[2] || 'M02,M03,M04,M05,M06').split(',');
for (const m of d.modules) {
  if (!targets.includes(m.module_id)) continue;
  let tc = 0;
  console.log(`=== ${m.module_id} "${m.module_title}" alloc=${m.instructional_minutes} status=${m.status} narr=${m.estimated_narration_minutes}`);
  console.log(`   src_status=${(m.source_status_flag || '').slice(0, 120)}`);
  console.log(`   sme=${(m.sme_review_flag || '').slice(0, 120)}`);
  for (const l of m.lessons) {
    tc += l.cards.length;
    const types = {};
    for (const c of l.cards) types[c.card_type] = (types[c.card_type] || 0) + 1;
    console.log(`   ${l.lesson_id} "${l.lesson_title}" min=${l.estimated_minutes} cards=${l.cards.length} ${JSON.stringify(types)}`);
    for (const c of l.cards) {
      const narr = c.estimated_narration_seconds || 0;
      console.log(`       ${c.card_id} [${c.card_type}] ${narr}s :: ${(c.display_title || '').slice(0, 70)}`);
    }
  }
  console.log(`   TOTAL CARDS=${tc}`);
}
