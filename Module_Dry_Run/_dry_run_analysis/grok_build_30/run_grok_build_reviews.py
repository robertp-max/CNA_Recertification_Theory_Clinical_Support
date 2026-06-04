#!/usr/bin/env python3
"""
Run 30 read-only Grok Build dry-run reviews through the Grok CLI chat proxy.

Why direct proxy instead of `grok -p`?
- Local Grok headless CLI was able to authenticate and receive prompts, but stalled without
  returning content in this pi harness.
- The same Grok Build model is accessible through the authenticated CLI chat proxy when the
  same headers used by Grok CLI are supplied.

This script writes analysis outputs only under Module_Dry_Run/_dry_run_analysis/grok_build_30/.
It never edits dry-run app/output artifacts.
"""
from __future__ import annotations

import concurrent.futures as cf
import csv
import datetime as dt
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback
import urllib.error
import urllib.request
from typing import Any

PROJECT_ROOT = Path(r"C:/AI/Git/CNA_Recertification_Theory_Clinical_Support")
DRY_ROOT = PROJECT_ROOT / "Module_Dry_Run"
OUT_ROOT = DRY_ROOT / "_dry_run_analysis" / "grok_build_30"
BUNDLE_DIR = OUT_ROOT / "input_bundles"
REVIEWS_DIR = OUT_ROOT / "reviews"
RAW_DIR = OUT_ROOT / "raw"
LOG_DIR = OUT_ROOT / "logs"
for d in [BUNDLE_DIR, REVIEWS_DIR, RAW_DIR, LOG_DIR]:
    d.mkdir(parents=True, exist_ok=True)

MODEL = "grok-build"
VERSION = "0.2.22"
API_URL = "https://cli-chat-proxy.grok.com/v1/chat/completions"
AUTH_SCOPE = "https://auth.x.ai::b1a00492-073a-47ea-816f-4c329264a828"

MODULES = {
    10: {
        "root": DRY_ROOT / "_module10_dryrun_outputs",
        "title": "NATP Module 10: Vital Signs",
        "declared_objectives": 16,
        "declared_minutes": 180,
        "source_pdf": "CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf",
        "checkpoint_note": "This is the original checkpoint packet module; all Module 10-specific requirements apply literally.",
    },
    11: {
        "root": DRY_ROOT / "_module11_dryrun_outputs",
        "title": "NATP Module 11: Nutrition",
        "declared_objectives": 10,
        "declared_minutes": 120,
        "source_pdf": "CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf",
        "checkpoint_note": "Apply Module 10 checkpoint principles, but use Module 11's own official objective count and weighted minutes for module-specific checks.",
    },
    13: {
        "root": DRY_ROOT / "_module13_dryrun_outputs",
        "title": "NATP Module 13: Long Term Care Resident",
        "declared_objectives": 8,
        "declared_minutes": 780,
        "source_pdf": "CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-13.pdf",
        "checkpoint_note": "Apply Module 10 checkpoint principles, but use Module 13's own official objective count and 13 source-recommended theory hours = 780 weighted minutes for module-specific checks.",
    },
}

LENSES = [
    ("01_scope_path_source", "Scope/path/source-authority audit: active write scope, app root, output root, source PDF, stale ContentV2/backups, path contradictions, and whether reports over-claim."),
    ("02_objectives_source_map", "Official objective coverage and source-map audit: objective counts, objective titles, page/source references, source assets, terminology, answer-key internal-only handling."),
    ("03_time_allotment", "Weighted theory time audit: exact minute total, per-objective distribution, clinical/assessment/certificate exclusion, and whether source-recommended versus minimum hours are handled correctly."),
    ("04_content_quality_scope", "Learner content and CNA scope audit: source-first instructional fidelity, CNA observation/report/document boundaries, overreach, missing teaching content, and learner safety."),
    ("05_activities_assessment", "Activities/assessment audit: >=3 activities per objective, activity fit, quiz/distractor quality, internal answer-key leakage, and confusing learner-facing wrong answers."),
    ("06_app_integration_build", "App integration/build audit: generated data copied to app, active contentV2 pointer, LessonPlayer reuse, build/typecheck evidence, and current-tree validation caveats."),
    ("07_media_audio_qwen", "Media/audio/Qwen/SFX/image audit: Qwen requirement, narration manifest/package format, CSV vs JSON, generated WAV status, image alt text/prompt-only status, SFX license gates."),
    ("08_compliance_regulatory", "Compliance/regulatory audit: no approval/certificate/clinical-hour/online competency/PHI claims, clinical boundaries, manual-skill deferral, production-readiness caveats."),
    ("09_data_schema_json", "Data/schema/JSON audit: schema shape, generated content package, narration batch package, consistency across module.content, activities, source map, and app data."),
    ("10_watchdog_handoff", "Final handoff/watchdog/orchestration audit: reports consistency, worker failure handling, residual risks, dirty repo risk, and whether PASS status is justified."),
]

RUBRIC = """
# Checkpoint / Rubric Used for All Grok Build Reviews

Primary packet: NATP Module 10 Vital Signs — Source-First Dry Run.
Use it as the strict Module 10 checkpoint and as the cross-module dry-run quality rubric for Modules 11 and 13.

Hard checkpoint principles:
- Source-first only: official NATP source PDF for the active module is the instructional authority.
- Active scope is one module only; avoid stale ContentV2, backups, prior module outputs, deployment, commits, pushes, PRs, or broad cleanup.
- Module 10 literal requirements: 16 official objectives; weighted theory minutes must total exactly 180; active output/app scope was specified as `Module10_Dry_Run` in the packet.
- For Module 11/13, adapt the objective/time checks to the module's own declared source requirements while still applying Module 10 checkpoint principles.
- No CDPH/TPRU approval claim, no certificate-production readiness claim, no online clinical-hour credit claim, no online hands-on competency validation claim, no PHI.
- Clinical/manual skills must be treated as theory preparation and deferred to in-person/evaluator-supported validation.
- Qwen TTS is required/gated, using model `C:/AI/Qwen3-TTS-12Hz-1.7B-Base`, Python env `C:/AI/qwen3-tts-env`, and CI-ION voice reference `C:/AI/Git/training/CI-ION/CI-ION_OASIS-E2_SOC/src/content/narration/Additional Narrations OASIS-E2/FINAL_REVIEW_EXPORT_GUIDANCE_001.wav`.
- Image prompts require alt text and must avoid PHI/facility logos; final image generation is separate unless authorized.
- SFX must remain queued/license-gated unless licensed assets are selected.
- Narration package preference after orchestration patch: JSON narration batch package, no CSV, where feasible. Note that Module 10 may predate that patch and uses CSV; evaluate as a gap/risk if relevant.
- Validate actual files/metrics over self-reported PASS text. Explicitly call out contradictions between report claims and observed file state.
""".strip()

FORBIDDEN_TERMS = [
    "CDPH", "TPRU", "approval", "approved", "certificate", "clinical credit",
    "clinical-hour", "clinical hour", "online hands-on", "hands-on competency", "PHI",
    "ContentV2", "Module 10", "Module 11", "Module 13", "prior Module",
]

REPORT_FILES = [
    "reports/preflight_report.md",
    "reports/final_handoff.md",
    "reports/validation_report.md",
    "reports/time_allotment_report.md",
    "reports/watchdog_report.md",
    "reports/lessonplayer_review.md",
    "reports/app_integration_notes.md",
    "reports/async_failure_diagnostic.md",
]

DATA_FILES = [
    "source_map/source_objective_map.json",
    "source_map/source_objective_map.md",
    "data/module{m}.content.json",
    "data/module{m}.activities.json",
    "data/content.generated.json",
    "audio/audio_manifest.json",
    "audio/narration_batch_import_package.json",
    "audio/audio_scripts.csv",
    "audio/sfx_manifest.json",
    "media/image_manifest.json",
    "media/image_prompt_queue.json",
]


def read_text(path: Path, max_chars: int | None = None) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return f"[[READ ERROR: {e}]]"
    if max_chars and len(text) > max_chars:
        return text[:max_chars] + f"\n\n[[TRUNCATED at {max_chars} of {len(text)} chars]]"
    return text


def load_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return None


def count_csv_rows(path: Path) -> int | None:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            return max(0, sum(1 for _ in csv.reader(f)) - 1)
    except Exception:
        return None


def deep_text_values(obj: Any, limit: int = 1000000) -> str:
    chunks: list[str] = []
    used = 0
    def walk(x: Any):
        nonlocal used
        if used >= limit:
            return
        if isinstance(x, str):
            s = x.strip()
            if s:
                chunks.append(s)
                used += len(s)
        elif isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(obj)
    return "\n".join(chunks)


def find_contexts(text: str, patterns: list[str], max_each: int = 3, radius: int = 180) -> list[str]:
    out: list[str] = []
    for pat in patterns:
        flags = re.I
        starts = [m.start() for m in re.finditer(re.escape(pat), text, flags)]
        for i, pos in enumerate(starts[:max_each]):
            snippet = text[max(0, pos - radius): pos + len(pat) + radius].replace("\n", " ")
            out.append(f"- `{pat}` context {i+1}: ...{snippet}...")
    return out


def summarize_json_file(rel: str, p: Path, module: int) -> list[str]:
    lines: list[str] = []
    d = load_json(p)
    if d is None:
        return [f"- {rel}: JSON parse failed or not JSON; size={p.stat().st_size if p.exists() else 'missing'}"]
    lines.append(f"- {rel}: JSON type={type(d).__name__}, size={p.stat().st_size}")
    if isinstance(d, dict):
        lines.append(f"  - top-level keys: {list(d.keys())[:20]}")
        # Common structure metrics.
        objectives = d.get("objectives") or d.get("learning_objectives")
        if isinstance(objectives, list):
            minutes = []
            titles = []
            activity_counts = []
            source_refs = []
            for o in objectives:
                if isinstance(o, dict):
                    titles.append(o.get("objective_title") or o.get("title") or o.get("learning_goal") or o.get("objective") or "")
                    for key in ["weighted_minutes", "theory_minutes", "minutes"]:
                        if isinstance(o.get(key), (int, float)):
                            minutes.append(o[key])
                            break
                    acts = o.get("activities") or o.get("learning_activities") or []
                    if isinstance(acts, list):
                        activity_counts.append(len(acts))
                    sr = o.get("source_reference") or o.get("source_refs") or o.get("source_pages")
                    if sr:
                        source_refs.append(str(sr))
            lines.append(f"  - objectives: count={len(objectives)}, minute_sum={sum(minutes) if minutes else 'not-found'}, min_activities={min(activity_counts) if activity_counts else 'not-found'}, max_activities={max(activity_counts) if activity_counts else 'not-found'}")
            if titles:
                lines.append("  - objective titles: " + "; ".join(f"{i+1}. {t}" for i, t in enumerate(titles[:20])))
            if source_refs:
                lines.append("  - sample source refs: " + " | ".join(source_refs[:6]))
        modules = d.get("modules")
        if isinstance(modules, list):
            desc = []
            for m in modules:
                if isinstance(m, dict):
                    mos = m.get("learning_objectives") or m.get("objectives") or []
                    desc.append(f"{m.get('id') or m.get('module_id')}:{m.get('module_title') or m.get('title')} objectives={len(mos) if isinstance(mos, list) else '?'}")
            lines.append(f"  - generated modules: {desc}")
        for key in ["module_id", "title", "source_authority", "source_title", "learner_facing_title", "theory_minutes_total", "total_weighted_minutes", "source_recommended_theory_hours", "source_recommended_clinical_hours", "source_required_clinical_hours", "online_clinical_credit_claimed", "online_hands_on_competency_validated", "status", "csv_used", "qwen_sent", "qwen_voice_cloning_started"]:
            if key in d:
                lines.append(f"  - {key}: {d[key]!r}")
        assets = d.get("source_assets")
        if isinstance(assets, list):
            lines.append(f"  - source_assets: count={len(assets)}; sample={[a.get('asset_id') or a.get('title') or a.get('name') for a in assets[:6] if isinstance(a, dict)]}")
        clips = d.get("clips")
        if isinstance(clips, list):
            statuses = {}
            final_nonempty = 0
            voice_nonempty = 0
            for c in clips:
                if isinstance(c, dict):
                    statuses[c.get("generated_status") or c.get("status") or "unknown"] = statuses.get(c.get("generated_status") or c.get("status") or "unknown", 0) + 1
                    if c.get("final_path"):
                        final_nonempty += 1
                    if c.get("voice_reference"):
                        voice_nonempty += 1
            lines.append(f"  - clips: count={len(clips)}, statuses={statuses}, final_path_nonempty={final_nonempty}, voice_reference_nonempty={voice_nonempty}")
        elif isinstance(clips, str):
            lines.append(f"  - clips: {clips!r}")
        items = d.get("items")
        if isinstance(items, list):
            alt = sum(1 for item in items if isinstance(item, dict) and item.get("alt_text"))
            lines.append(f"  - items: count={len(items)}, alt_text_count={alt}")
        validation = d.get("validation")
        if isinstance(validation, dict):
            lines.append(f"  - validation: {validation}")
    return lines


def build_bundle(module: int, info: dict[str, Any]) -> str:
    root: Path = info["root"]
    now = dt.datetime.now().isoformat(timespec="seconds")
    lines: list[str] = []
    lines.append(f"# Grok Build Review Input Bundle — Module {module}")
    lines.append(f"Generated: {now}")
    lines.append(f"Module title: {info['title']}")
    lines.append(f"Declared objective count for this module: {info['declared_objectives']}")
    lines.append(f"Declared weighted theory minutes for this module: {info['declared_minutes']}")
    lines.append(f"Declared source PDF: `{info['source_pdf']}`")
    lines.append(info["checkpoint_note"])
    lines.append("")
    lines.append(RUBRIC)
    lines.append("")

    # Actual path state, including known Module10 path discrepancy.
    lines.append("## Actual Path / File-State Facts")
    paths = [
        PROJECT_ROOT / "Module10_Dry_Run",
        PROJECT_ROOT / "Module10_Dry_Run_module10_dryrun_outputs",
        DRY_ROOT,
        root,
        DRY_ROOT / "standalone-course-mvp",
        DRY_ROOT / "standalone-course-mvp" / "src" / "data" / "contentV2.generated.ts",
        DRY_ROOT / "standalone-course-mvp" / "src" / "data" / f"module{module}.generated.ts",
        DRY_ROOT / "standalone-course-mvp" / "src" / "data" / f"module{module}.content.generated.json",
        PROJECT_ROOT / info["source_pdf"],
    ]
    for p in paths:
        try:
            exists = p.exists()
            kind = "dir" if p.is_dir() else "file" if p.is_file() else "missing"
            size = p.stat().st_size if p.exists() and p.is_file() else ""
            lines.append(f"- `{p.relative_to(PROJECT_ROOT).as_posix() if str(p).startswith(str(PROJECT_ROOT)) else p}`: exists={exists}, kind={kind}, size={size}")
        except Exception as e:
            lines.append(f"- `{p}`: stat error {e}")
    cv2 = DRY_ROOT / "standalone-course-mvp" / "src" / "data" / "contentV2.generated.ts"
    if cv2.exists():
        lines.append("\n### Current active app content pointer (`contentV2.generated.ts`)")
        lines.append("```ts\n" + read_text(cv2, 2000) + "\n```")

    # File inventory.
    lines.append("\n## Output File Inventory")
    if root.exists():
        for p in sorted(root.rglob("*")):
            if not p.is_file():
                continue
            parts = set(part.lower() for part in p.parts)
            if "backups" in parts or "qwen_tts" in parts or "__pycache__" in parts:
                continue
            rel = p.relative_to(root).as_posix()
            lines.append(f"- `{rel}` size={p.stat().st_size}")
    else:
        lines.append(f"- output root missing: {root}")

    # Deterministic data summaries.
    lines.append("\n## Deterministic JSON/CSV Metrics")
    for template in DATA_FILES:
        rel = template.format(m=module)
        p = root / rel
        if not p.exists():
            lines.append(f"- {rel}: MISSING")
            continue
        if p.suffix.lower() == ".json":
            lines.extend(summarize_json_file(rel, p, module))
        elif p.suffix.lower() == ".csv":
            lines.append(f"- {rel}: CSV rows={count_csv_rows(p)}, size={p.stat().st_size}")
        else:
            lines.append(f"- {rel}: size={p.stat().st_size}")

    # App data file states for all modules, because later dry runs may overwrite active pointer.
    lines.append("\n## Current App Data State Across Reviewed Modules")
    app_data = DRY_ROOT / "standalone-course-mvp" / "src" / "data"
    for m in [10, 11, 13]:
        for name in [f"module{m}.generated.ts", f"module{m}.content.generated.json", f"module{m}.content.json", f"module{m}.activities.json", f"module{m}.schema.json"]:
            p = app_data / name
            lines.append(f"- `{p.relative_to(PROJECT_ROOT).as_posix()}` exists={p.exists()} size={p.stat().st_size if p.exists() else ''}")

    # Report contents.
    lines.append("\n## Report File Contents")
    for rel in REPORT_FILES:
        p = root / rel
        if not p.exists():
            lines.append(f"\n### `{rel}`\nMISSING")
            continue
        max_chars = 14000 if rel.endswith("final_handoff.md") or rel.endswith("preflight_report.md") else 8000
        lines.append(f"\n### `{rel}`")
        lines.append("```markdown\n" + read_text(p, max_chars) + "\n```")

    # Search contexts for risk terms in generated packages.
    lines.append("\n## Risk-Term Contexts From Generated Data")
    combined = []
    for rel in [f"data/module{module}.content.json", "data/content.generated.json", "source_map/source_objective_map.json", "audio/audio_manifest.json", "audio/narration_batch_import_package.json"]:
        p = root / rel
        if p.exists():
            combined.append(f"\n-- {rel} --\n" + read_text(p, 200000))
    combined_text = "\n".join(combined)
    term_counts = {term: len(re.findall(re.escape(term), combined_text, flags=re.I)) for term in FORBIDDEN_TERMS}
    lines.append("Term counts (counts may include allowed negations like 'No PHI' or quiz distractors):")
    lines.append(json.dumps(term_counts, indent=2))
    contexts = find_contexts(combined_text, ["Use Module 10 generated content", "Use prior Module 10/11", "clinical-hour credit", "online hands-on", "certificate-production", "approval claim", "No PHI", "ContentV2"], max_each=4)
    if contexts:
        lines.append("\nSelected contexts:")
        lines.extend(contexts)
    else:
        lines.append("No selected risk contexts found.")

    # Qwen runtime state (mostly for Module 13 but included in all for comparison).
    lines.append("\n## Qwen / Audio Runtime Observations")
    qwen_dir = root / "audio" / "qwen_tts"
    wavs = sorted(qwen_dir.glob("*.wav")) if qwen_dir.exists() else []
    lines.append(f"- qwen_tts directory: exists={qwen_dir.exists()}, wav_count={len(wavs)}")
    if wavs:
        lines.append("- sample wavs: " + ", ".join(w.name for w in wavs[:12]))
    logs = root / "audio" / "logs"
    if logs.exists():
        for p in sorted(logs.glob("*")):
            if p.is_file():
                lines.append(f"\n### audio log `{p.relative_to(root).as_posix()}` size={p.stat().st_size}")
                lines.append("```text\n" + read_text(p, 4000)[-4000:] + "\n```")

    return "\n".join(lines) + "\n"


def get_token() -> str:
    auth_path = Path.home() / ".grok" / "auth.json"
    data = json.loads(auth_path.read_text(encoding="utf-8"))
    entry = data.get(AUTH_SCOPE) or next(iter(data.values()))
    return entry["key"]


def call_grok(prompt: str, review_id: str, max_retries: int = 3) -> dict[str, Any]:
    token = get_token()
    body = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are Grok Build performing a strict read-only LMS dry-run audit. You cannot inspect files except through the evidence bundle supplied by the user. Give evidence-grounded findings with severity and avoid generic praise.",
            },
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "temperature": 0.2,
    }
    data = json.dumps(body).encode("utf-8")
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "X-XAI-Token-Auth": "xai-grok-cli",
        "x-grok-model-override": MODEL,
        "x-grok-client-version": VERSION,
        "x-grok-client-identifier": "grok-shell",
        "User-Agent": f"grok/{VERSION} dry-run-review-runner",
    }
    for attempt in range(1, max_retries + 1):
        req = urllib.request.Request(API_URL, data=data, headers=headers)
        start = time.time()
        try:
            with urllib.request.urlopen(req, timeout=420) as resp:
                text = resp.read().decode("utf-8", errors="replace")
                parsed = json.loads(text)
                parsed["_runner"] = {"review_id": review_id, "attempt": attempt, "elapsed_sec": round(time.time() - start, 2), "status": resp.status}
                return parsed
        except urllib.error.HTTPError as e:
            err = e.read().decode("utf-8", errors="replace")
            if e.code in (429, 500, 502, 503, 504) and attempt < max_retries:
                time.sleep(10 * attempt)
                continue
            return {"_runner": {"review_id": review_id, "attempt": attempt, "elapsed_sec": round(time.time() - start, 2), "status": "HTTPError", "code": e.code}, "error": err}
        except Exception as e:
            if attempt < max_retries:
                time.sleep(10 * attempt)
                continue
            return {"_runner": {"review_id": review_id, "attempt": attempt, "status": "Exception"}, "error": repr(e), "traceback": traceback.format_exc()}
    raise RuntimeError("unreachable")


def extract_text(resp: dict[str, Any]) -> str:
    try:
        return resp["choices"][0]["message"].get("content") or ""
    except Exception:
        return ""


def make_prompt(module: int, lens_id: str, lens_desc: str, bundle: str) -> str:
    info = MODULES[module]
    return f"""
You are one of 10 independent Grok Build reviewers for Module {module}.

Review lens ID: {lens_id}
Review lens: {lens_desc}

Task:
- Audit the supplied dry-run evidence bundle against the checkpoint/rubric.
- Be read-only. Do not propose running commands or modifying files as if you are executing; only analyze evidence.
- Separate hard failures from residual risks and from module-specific non-applicable checks.
- For Module 10, apply Module 10-specific checkpoint values literally: 16 objectives, exactly 180 weighted theory minutes, original packet path `Module10_Dry_Run`.
- For Modules 11/13, apply checkpoint principles but use the module's own declared values from the bundle: objectives={info['declared_objectives']}, weighted minutes={info['declared_minutes']}.
- Treat self-reported PASS as lower-strength evidence than actual deterministic metrics/path checks.
- If the evidence contradicts itself, call that out.
- Include file/path evidence where possible.

Output format (Markdown):
1. `# Review {lens_id} — Module {module}`
2. `Verdict:` PASS / PASS WITH RISKS / CONDITIONAL PASS / FAIL / INSUFFICIENT EVIDENCE.
3. `Top findings:` 5-10 bullets, each with severity `[Critical|High|Medium|Low]`, evidence, and recommended action.
4. `Checkpoint table:` concise table with Check, Status, Evidence.
5. `Open questions / residual risks:` bullets.
6. `One-sentence go/no-go recommendation.`

EVIDENCE BUNDLE START
{bundle}
EVIDENCE BUNDLE END
""".strip()


def run_one(args: tuple[int, str, str, str]) -> dict[str, Any]:
    module, lens_id, lens_desc, bundle = args
    review_id = f"module{module}_{lens_id}"
    prompt = make_prompt(module, lens_id, lens_desc, bundle)
    prompt_path = LOG_DIR / f"{review_id}.prompt.md"
    prompt_path.write_text(prompt, encoding="utf-8")
    resp = call_grok(prompt, review_id)
    raw_path = RAW_DIR / f"{review_id}.json"
    raw_path.write_text(json.dumps(resp, indent=2, ensure_ascii=False), encoding="utf-8")
    text = extract_text(resp)
    if not text:
        text = "# ERROR / EMPTY RESPONSE\n\n```json\n" + json.dumps(resp, indent=2, ensure_ascii=False)[:8000] + "\n```\n"
    review_path = REVIEWS_DIR / f"{review_id}.md"
    review_path.write_text(text, encoding="utf-8")
    return {
        "module": module,
        "lens_id": lens_id,
        "review_id": review_id,
        "review_path": str(review_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "raw_path": str(raw_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "runner": resp.get("_runner"),
        "error": bool(resp.get("error")) or not bool(extract_text(resp)),
        "chars": len(text),
    }


def main() -> int:
    started = dt.datetime.now().isoformat(timespec="seconds")
    bundles: dict[int, str] = {}
    for module, info in MODULES.items():
        bundle = build_bundle(module, info)
        bundles[module] = bundle
        (BUNDLE_DIR / f"module{module}_bundle.md").write_text(bundle, encoding="utf-8")
    tasks: list[tuple[int, str, str, str]] = []
    for module in [10, 11, 13]:
        for lens_id, lens_desc in LENSES:
            tasks.append((module, lens_id, lens_desc, bundles[module]))

    results: list[dict[str, Any]] = []
    # Keep concurrency moderate to avoid rate limit and avoid disturbing other GPU/TTS jobs.
    max_workers = int(os.environ.get("GROK_REVIEW_CONCURRENCY", "3"))
    print(f"Starting {len(tasks)} Grok Build reviews with concurrency={max_workers}", flush=True)
    with cf.ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(run_one, task): task for task in tasks}
        for fut in cf.as_completed(futures):
            task = futures[fut]
            try:
                res = fut.result()
            except Exception as e:
                module, lens_id, _, _ = task
                res = {"module": module, "lens_id": lens_id, "review_id": f"module{module}_{lens_id}", "error": True, "exception": repr(e), "traceback": traceback.format_exc()}
            results.append(res)
            print(json.dumps(res, ensure_ascii=False), flush=True)
            manifest = {
                "started": started,
                "updated": dt.datetime.now().isoformat(timespec="seconds"),
                "model": MODEL,
                "api_url": API_URL,
                "count_requested": len(tasks),
                "count_complete": len(results),
                "results": sorted(results, key=lambda r: r.get("review_id", "")),
            }
            (OUT_ROOT / "run_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    completed = dt.datetime.now().isoformat(timespec="seconds")
    manifest = {
        "started": started,
        "completed": completed,
        "model": MODEL,
        "api_url": API_URL,
        "count_requested": len(tasks),
        "count_complete": len(results),
        "errors": [r for r in results if r.get("error")],
        "results": sorted(results, key=lambda r: r.get("review_id", "")),
    }
    (OUT_ROOT / "run_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Done. Manifest: {OUT_ROOT / 'run_manifest.json'}", flush=True)
    return 0 if not manifest["errors"] else 2

if __name__ == "__main__":
    raise SystemExit(main())
