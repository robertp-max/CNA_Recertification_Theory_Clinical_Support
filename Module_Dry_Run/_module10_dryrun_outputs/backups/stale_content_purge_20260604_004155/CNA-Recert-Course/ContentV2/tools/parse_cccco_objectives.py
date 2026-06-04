"""parse_cccco_objectives.py

Parse the structured front-matter of each extracted CCCCO module text file:
title, theory hours, statement of purpose, terminology count, and the numbered
"Performance Standards (Objectives)" list. These objectives are the atomic units
the survey-evidence source-to-lesson mapping is built against.

Input:  survey-evidence/_source_text/module-{NN}.txt  (from extract_cccco_text.py)
Output: survey-evidence/_source_text/cccco_objectives.json
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "CNA-Recert-Course" / "ContentV2" / "survey-evidence" / "_source_text"

# Keywords that mark the end of the objectives list (start of content outline etc.)
END_MARKERS = re.compile(
    r"^(content outline|instructional|suggested|demonstrate|references|resources|"
    r"unit outline|outline of|teaching|methods of evaluation|evaluation)",
    re.I,
)


def parse_module(n: int) -> dict:
    f = SRC / f"module-{n:02d}.txt"
    text = f.read_text(encoding="utf-8")
    lines = text.splitlines()

    title = lines[0].strip() if lines else f"Module {n}"
    theory = next((re.sub(r".*Theory Hours:\s*", "", l).strip()
                   for l in lines if "Theory Hours" in l), "?")

    # Statement of Purpose
    purpose = ""
    for i, l in enumerate(lines):
        if l.strip().lower().startswith("statement of purpose"):
            buf = []
            for j in range(i + 1, min(i + 12, len(lines))):
                s = lines[j].strip()
                if not s:
                    if buf:
                        break
                    continue
                if s.lower().startswith("terminology"):
                    break
                buf.append(s)
            purpose = " ".join(buf).strip()
            break

    # Objectives: numbered list after the "Performance Standards (Objectives)" header.
    # Prefer to start after an "Upon completion ... able to:" stem if present within a
    # few lines of the header; otherwise start right after the header line itself.
    objectives = []
    start = None
    header_idx = next((i for i, l in enumerate(lines)
                       if re.search(r"performance standards\s*\(objectives\)", l, re.I)), None)
    if header_idx is not None:
        start = header_idx + 1
        for k in range(header_idx + 1, min(header_idx + 8, len(lines))):
            if "able to:" in lines[k].lower():
                start = k + 1
                break
    else:
        for i, l in enumerate(lines):
            if "able to:" in l.lower():
                start = i + 1
                break
    if start is not None:
        last_num = 0
        for j in range(start, len(lines)):
            s = lines[j].strip()
            if not s:
                continue
            if END_MARKERS.match(s):
                break
            m = re.match(r"^(\d+)\.\s+(.*)$", s)
            if m:
                num = int(m.group(1))
                # objectives increase sequentially; reset/large jump => left the list
                if num == last_num + 1 or (num == 1 and last_num == 0):
                    objectives.append({"n": num, "text": m.group(2).strip()})
                    last_num = num
                elif num <= last_num:
                    # likely a new numbered list (terminology already passed) -> stop
                    if num == 1 and last_num >= 3:
                        break
                else:
                    # gap in numbering: still accept but record
                    objectives.append({"n": num, "text": m.group(2).strip()})
                    last_num = num
            elif objectives and not re.match(r"^(page \d+|module \d+|california community)", s, re.I):
                # continuation line of the previous objective (wrapped text)
                if len(s) > 2 and not s.startswith("Patient"):
                    objectives[-1]["text"] += " " + s

    # tidy continuation artifacts
    for o in objectives:
        o["text"] = re.sub(r"\s+", " ", o["text"]).strip()

    return {
        "cccco_module": n,
        "title": title,
        "theory_hours": theory,
        "statement_of_purpose": purpose,
        "objective_count": len(objectives),
        "objectives": objectives,
    }


def main() -> int:
    out = {"modules": [parse_module(n) for n in range(10, 18)]}
    (SRC / "cccco_objectives.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for m in out["modules"]:
        print(f"M{m['cccco_module']} {m['title'][:45]:45s} hours={m['theory_hours'][:30]:30s} objectives={m['objective_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
