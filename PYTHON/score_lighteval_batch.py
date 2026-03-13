#!/usr/bin/env python3
"""
score_lighteval_batch.py — Score a slice of papers for lighteval implementability.

Usage:
    cd CEI-Lit-WS && ../.venv/bin/python PYTHON/score_lighteval_batch.py START END AGENT_NUM

Args:
    START     - Start index (0-based, inclusive)
    END       - End index (0-based, inclusive)
    AGENT_NUM - Agent number (1-8), used to name the output file
"""

import functools
import json
import os
import sys
from pathlib import Path

print = functools.partial(print, flush=True)

# Path setup
_script_dir = Path(__file__).resolve().parent
if str(_script_dir) not in sys.path:
    sys.path.insert(0, str(_script_dir))

from lighteval_scoring import score_paper

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent  # CEI-Lit-WS/
LOGS = BASE / "logs"
INPUT_JSON = LOGS / "20260312-lm-eval-implementability-data.json"


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} START END AGENT_NUM")
        sys.exit(1)

    start = int(sys.argv[1])
    end = int(sys.argv[2])
    agent_num = int(sys.argv[3])

    output_path = LOGS / f"20260312-lighteval-scores-{agent_num}.json"

    print(f"Agent {agent_num}: scoring papers [{start}..{end}]")

    # Load input data
    with open(INPUT_JSON) as f:
        data = json.load(f)

    papers = data["papers"]
    total = len(papers)
    slice_papers = papers[start:end + 1]
    print(f"Agent {agent_num}: {len(slice_papers)} papers (of {total} total)")

    # Score each paper
    results = []
    for i, paper in enumerate(slice_papers):
        result = score_paper(paper)
        results.append(result)
        if (i + 1) % 50 == 0:
            print(f"  Agent {agent_num}: scored {i + 1}/{len(slice_papers)}")

    # Sort by score descending within this chunk
    results.sort(key=lambda r: r["total_score"], reverse=True)

    # Write with PID-scoped temp file for safety
    tmp_path = output_path.with_suffix(f".tmp.{os.getpid()}.json")
    with open(tmp_path, "w") as f:
        json.dump({
            "agent": agent_num,
            "range": [start, end],
            "count": len(results),
            "results": results,
        }, f, indent=2)
    os.replace(str(tmp_path), str(output_path))

    print(f"Agent {agent_num}: wrote {len(results)} scores to {output_path.name}")

    # Quick stats
    tier_counts = {}
    for r in results:
        tier_counts[r["tier"]] = tier_counts.get(r["tier"], 0) + 1
    for tier, count in sorted(tier_counts.items()):
        print(f"  {tier}: {count}")


if __name__ == "__main__":
    main()
