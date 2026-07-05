#!/usr/bin/env python3
"""
COOKBOOK Phase 2 — dossier assignment generator.

Splits each theme's card list (from 20260705-card-index.json) into balanced
chunks of <= CAP cards and writes one assignment file per chunk to
20260705-dossier-assignments/<theme>-part<k>.json. Themes with one chunk get
a single part file. Prints the part counts per theme (hardcoded into the
Phase 2 workflow script).
"""

import json
import math
from datetime import datetime
from pathlib import Path

EVIDENCE_DIR = Path(__file__).resolve().parents[1] / "30-EVIDENCE"
INDEX = EVIDENCE_DIR / "20260705-card-index.json"
OUT_DIR = EVIDENCE_DIR / "20260705-dossier-assignments"

CAP = 65


def main():
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    cards = idx["cards"]
    OUT_DIR.mkdir(exist_ok=True)

    summary = {}
    for theme, stems in idx["themes"].items():
        if not stems:
            continue
        # quality-order: benchmark cards first, then high confidence
        def rank(stem):
            c = cards[stem]
            return (
                0 if c.get("is_benchmark") else 1,
                0 if c.get("confidence") == "high" else 1,
                stem,
            )
        ordered = sorted(stems, key=rank)
        n_parts = math.ceil(len(ordered) / CAP)
        # balanced round-robin so each part mixes benchmark + context cards
        parts = [ordered[i::n_parts] for i in range(n_parts)]
        for k, part in enumerate(parts, 1):
            payload = {
                "theme": theme,
                "part": k,
                "of": n_parts,
                "generated_at": datetime.now().isoformat(timespec="seconds"),
                "cards": [
                    {"stem": s, "path": cards[s]["path"], "kind": cards[s]["kind"]}
                    for s in part
                ],
            }
            (OUT_DIR / f"{theme}-part{k}.json").write_text(
                json.dumps(payload, indent=1), encoding="utf-8"
            )
        summary[theme] = {"cards": len(ordered), "parts": n_parts}

    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
