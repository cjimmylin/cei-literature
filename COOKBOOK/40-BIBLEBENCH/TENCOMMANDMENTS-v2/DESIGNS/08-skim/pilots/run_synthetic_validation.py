#!/usr/bin/env python3
"""Execute the full disclosed SKIM P1 synthetic validation panel."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
BENCH_ROOT = ROOT.parents[2]
for search_root in (ROOT, BENCH_ROOT):
    if str(search_root) not in sys.path:
        sys.path.insert(0, str(search_root))

from harness.run_p1 import run_synthetic_validation  # noqa: E402


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run all six deterministic fixture profiles over the exact "
            "14,400-request SKIM P1 synthetic schedule."
        )
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        type=Path,
        help="new directory for event logs and synthetic-result.json",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=6,
        help="parallel profile workers (1-6; default: 6)",
    )
    return parser


def main(argv=None) -> int:
    args = _parser().parse_args(argv)
    result = run_synthetic_validation(
        output_dir=args.output_dir,
        max_workers=args.max_workers,
    )
    summary = {
        "status": result["status"],
        "eligible_for_empirical_decision": result[
            "eligible_for_empirical_decision"
        ],
        "scheduled_requests": result["scheduled_requests"],
        "completed_episodes": result["completed_episodes"],
        "valid_terminal_episodes": result["valid_terminal_episodes"],
        "parked_episodes": result["parked_episodes"],
        "external_paid_calls": result["external_paid_calls"],
        "total_cost_usd": result["total_cost_usd"],
        "result_path": str(args.output_dir / "synthetic-result.json"),
    }
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
