const fs = require('fs');
const path = require('path');
const d = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data', 'courseContentV2.json'), 'utf8'));
const [mid, lid] = (process.argv[2] || 'M06:L02').split(':');
const m = d.modules.find(x => x.module_id === mid);
const l = m.lessons.find(x => x.lesson_id === lid);
for (const c of l.cards) {
  if (c.card_type !== 'delivery') continue;
  const n = c.estimated_narration_seconds || 0;
  console.log(`\n--- ${c.card_id} (${n}s) "${c.display_title}" src=${c.source_reference || c.source_section || 'n/a'}`);
  console.log((c.narration_script || c.learner_facing_content || '').trim());
}
