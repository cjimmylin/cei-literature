#!/usr/bin/env python
"""Session-8 analysis-7 prep: style-normalized contamination spot-check rows.

Explicit-tell scan found 0/779 prompts with model/vendor self-identification,
so the residual contamination channel is STYLISTIC (markdown habits: bold,
headers, bullet glyphs, code fences). This script takes a seeded sample of 21
epochs-core samples (7 per SUT, balanced) and rewrites ONLY the
[BEGIN MODEL RESPONSE]..[END MODEL RESPONSE] span through a conservative
markdown-stripper that preserves words and line structure. Re-grading these
with J4 bounds the style-channel contamination of the kin estimate.

Output: analysis/20260717-session8-contamination-rows.jsonl (same sample_key
as originals so deltas map 1:1 to the J4 raw grades).
"""
from __future__ import annotations

import json
import random
import re
from collections import defaultdict
from pathlib import Path

V2 = Path(__file__).resolve().parent.parent
ROWS = V2 / "analysis" / "20260717-session8-replay-rows.jsonl"
OUT = V2 / "analysis" / "20260717-session8-contamination-rows.jsonl"
SEED = 4242
PER_SUT = 7
B, E = "[BEGIN MODEL RESPONSE]", "[END MODEL RESPONSE]"


def strip_style(text: str) -> str:
    t = text
    t = re.sub(r"```[a-zA-Z]*\n?", "", t)              # code fences
    t = re.sub(r"(?m)^#{1,6}\s+", "", t)               # headers
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)             # bold
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", t)  # italics
    t = re.sub(r"(?m)^\s*[-*•]\s+", "", t)             # bullet glyphs
    t = re.sub(r"(?m)^\s*\d+[.)]\s+", "", t)           # numbered lists
    t = re.sub(r"(?m)^[|+][-|+ ]+[|+]\s*$", "", t)     # table rules
    t = t.replace("—", ", ").replace("–", "-")          # em/en dashes
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t


def main() -> int:
    rows = [json.loads(l) for l in ROWS.read_text().splitlines()]
    core = [r for r in rows if r["stratum"] == "S1-epochs-core"]
    rng = random.Random(SEED)
    by_sut = defaultdict(list)
    for r in core:
        by_sut[r["sut_short"]].append(r)
    picked = []
    for sut in sorted(by_sut):
        picked.extend(rng.sample(by_sut[sut], PER_SUT))

    n_changed = 0
    with OUT.open("w") as fh:
        for r in picked:
            p = r["prompt"]
            i, j = p.index(B) + len(B), p.index(E)
            body = p[i:j]
            norm = strip_style(body)
            if norm != body:
                n_changed += 1
            r2 = dict(r)
            r2["prompt"] = p[:i] + norm + p[j:]
            r2["style_changed"] = norm != body
            fh.write(json.dumps(r2) + "\n")
    print(f"{len(picked)} rows ({n_changed} style-changed) -> {OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
