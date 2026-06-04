import csv
import json
import re
import sys
import time
from pathlib import Path

# The output directory is named `qwen_tts/`, which otherwise shadows the
# installed/editable Qwen package when this script is executed from the audio
# folder. Put the actual Qwen source checkout first on sys.path before import.
sys.path.insert(0, r"C:/AI/Qwen3-TTS")

import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

REPO = Path(r"C:/AI/Git/CNA_Recertification_Theory_Clinical_Support")
AUDIO_DIR = REPO / "Module_Dry_Run/_module13_dryrun_outputs/audio"
OUT_DIR = AUDIO_DIR / "qwen_tts"
MANIFEST_PATH = AUDIO_DIR / "audio_manifest.json"
PACKAGE_PATH = AUDIO_DIR / "narration_batch_import_package.json"
LOG_PATH = AUDIO_DIR / "qwen_tts_generation_report.md"
MODEL_PATH = r"C:/AI/Qwen3-TTS-12Hz-1.7B-Base"
REF_AUDIO = r"C:/AI/Git/training/CI-ION/CI-ION_OASIS-E2_SOC/src/content/narration/Additional Narrations OASIS-E2/FINAL_REVIEW_EXPORT_GUIDANCE_001.wav"
REF_MANIFEST_CSV = Path(r"C:/AI/Git/training/CI-ION/CI-ION_OASIS-E2_SOC/src/content/narration/oasis-narration-manifest.csv")
REF_NARRATION_ID = "FINAL_REVIEW_EXPORT_GUIDANCE_001"


def load_ref_text() -> str:
    with REF_MANIFEST_CSV.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("narrationId") == REF_NARRATION_ID:
                return row["text"].strip()
    raise RuntimeError(f"Reference transcript not found for {REF_NARRATION_ID}")


def safe_name(clip_id: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", clip_id).strip("_") + ".wav"


def load_payloads():
    manifest = json.load(MANIFEST_PATH.open(encoding="utf-8"))
    package = json.load(PACKAGE_PATH.open(encoding="utf-8"))
    clips = package.get("clips", [])
    if not clips:
        raise RuntimeError("No clips found in narration batch package")
    return manifest, package, clips


def update_clip_fields(clip, status, final_path="", error=""):
    clip["voice_reference"] = REF_AUDIO
    clip["qwen_model"] = MODEL_PATH
    clip["qwen_sent"] = True
    clip["voice_cloning_started"] = True
    clip["generated_status"] = status
    clip["approval_status"] = "qwen_tts_generation_required_by_run_requirement"
    if final_path:
        clip["final_path"] = final_path
    if error:
        clip["generation_error"] = error


def write_state(manifest, package, generated, failures, ref_text, status_note):
    by_id = {c["clip_id"]: c for c in package.get("clips", [])}
    for mclip in manifest.get("clips", []):
        if mclip.get("clip_id") in by_id:
            mclip.update(by_id[mclip["clip_id"]])
    manifest.update({
        "status": status_note,
        "qwen_sent": True,
        "qwen_voice_cloning_started": True,
        "qwen_voice_cloning_completed": status_note == "qwen_tts_generated",
        "qwen_model": MODEL_PATH,
        "voice_reference": REF_AUDIO,
        "voice_reference_transcript": ref_text,
        "generated_count": len(generated),
        "failed_count": len(failures),
        "output_dir": OUT_DIR.relative_to(REPO).as_posix(),
        "compliance": "Qwen TTS generation is required for this run. No SFX/image generation or approval/clinical-credit/competency claim.",
    })
    package.update({
        "status": status_note,
        "qwen_sent": True,
        "voice_cloning_started": True,
        "qwen_voice_cloning_started": True,
        "qwen_voice_cloning_completed": status_note == "qwen_tts_generated",
        "qwen_model": MODEL_PATH,
        "voice_reference": REF_AUDIO,
        "voice_reference_transcript": ref_text,
        "generated_count": len(generated),
        "failed_count": len(failures),
        "output_dir": OUT_DIR.relative_to(REPO).as_posix(),
    })
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    PACKAGE_PATH.write_text(json.dumps(package, indent=2, ensure_ascii=False), encoding="utf-8")
    lines = [
        "# Qwen TTS Generation Report — Module 13",
        "",
        f"Last update: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Status: `{status_note}`",
        f"Model: `{MODEL_PATH}`",
        f"Reference audio: `{REF_AUDIO}`",
        f"Reference transcript: {ref_text}",
        f"Generated clips: {len(generated)}",
        f"Failed clips: {len(failures)}",
        "",
        "## Generated Files",
    ]
    lines += [f"- `{g['clip_id']}` → `{g['path']}` ({g['bytes']} bytes, {g.get('sample_rate', 'unknown')} Hz, {g.get('seconds', 'existing')}s)" for g in generated]
    if failures:
        lines += ["", "## Failures"] + [f"- `{f['clip_id']}`: `{f['error']}`" for f in failures]
    lines += ["", "## Compliance", "- Source-validated narration scripts only.", "- No PHI introduced.", "- No certificate/approval/clinical-credit/competency claim.", "- No image/SFX generation performed by this step."]
    LOG_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ref_text = load_ref_text()
    manifest, package, clips = load_payloads()
    generated = []
    failures = []

    # Checkpoint existing WAVs from any interrupted foreground run.
    for clip in clips:
        out_file = OUT_DIR / safe_name(clip["clip_id"])
        if out_file.exists() and out_file.stat().st_size > 44:
            rel = out_file.relative_to(REPO).as_posix()
            update_clip_fields(clip, "generated", rel)
            generated.append({"clip_id": clip["clip_id"], "path": rel, "bytes": out_file.stat().st_size, "seconds": "existing", "sample_rate": "unknown"})
        else:
            update_clip_fields(clip, "qwen_processing_queued")
    write_state(manifest, package, generated, failures, ref_text, "qwen_tts_processing")

    remaining = [clip for clip in clips if clip.get("generated_status") != "generated"]
    print("QWEN_TTS_RESUME_START", "remaining", len(remaining), "existing", len(generated), flush=True)
    if not remaining:
        write_state(manifest, package, generated, failures, ref_text, "qwen_tts_generated")
        print("QWEN_TTS_DONE all_existing", flush=True)
        return

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
    print("device", device, "model", MODEL_PATH, flush=True)
    t0 = time.time()
    model = Qwen3TTSModel.from_pretrained(MODEL_PATH, device_map=device, dtype=dtype, attn_implementation="eager")
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    print("loaded_seconds", round(time.time() - t0, 2), flush=True)
    prompt = model.create_voice_clone_prompt(ref_audio=REF_AUDIO, ref_text=ref_text, x_vector_only_mode=False)

    for idx, clip in enumerate(remaining, 1):
        clip_id = clip["clip_id"]
        text = " ".join((clip.get("transcript") or "").split())
        out_file = OUT_DIR / safe_name(clip_id)
        print(f"[{idx}/{len(remaining)}] {clip_id} chars={len(text)}", flush=True)
        update_clip_fields(clip, "qwen_processing")
        write_state(manifest, package, generated, failures, ref_text, "qwen_tts_processing")
        try:
            t1 = time.time()
            wavs, sr = model.generate_voice_clone(
                text=text,
                language="English",
                voice_clone_prompt=prompt,
                max_new_tokens=768,
                do_sample=True,
                top_k=50,
                top_p=1.0,
                temperature=0.8,
                repetition_penalty=1.05,
                subtalker_dosample=True,
                subtalker_top_k=50,
                subtalker_top_p=1.0,
                subtalker_temperature=0.8,
            )
            if torch.cuda.is_available():
                torch.cuda.synchronize()
            sf.write(str(out_file), wavs[0], sr)
            rel = out_file.relative_to(REPO).as_posix()
            update_clip_fields(clip, "generated", rel)
            generated.append({"clip_id": clip_id, "path": rel, "bytes": out_file.stat().st_size, "seconds": round(time.time() - t1, 2), "sample_rate": sr})
            print("  wrote", rel, out_file.stat().st_size, flush=True)
        except Exception as exc:
            msg = repr(exc)
            update_clip_fields(clip, "failed", error=msg)
            failures.append({"clip_id": clip_id, "error": msg})
            print("  FAILED", msg, flush=True)
        write_state(manifest, package, generated, failures, ref_text, "qwen_tts_processing")

    final_status = "qwen_tts_generated" if not failures else "qwen_tts_partial_failure"
    write_state(manifest, package, generated, failures, ref_text, final_status)
    print("QWEN_TTS_DONE", json.dumps({"generated": len(generated), "failed": len(failures)}, ensure_ascii=False), flush=True)
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
