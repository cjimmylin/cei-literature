#!/usr/bin/env python3
"""CLI wrapper for name-lint validation of dashboard files.

Usage:
    python lint_dashboard_interpretations.py [--format human|json] FILE [FILE ...]

Exit codes:
    0  clean (no violations)
    1  violations found
    2  file I/O error
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Cross-project import from .agent/lib/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / ".agent" / "lib"))
from name_lint import NameViolation, lint_file  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lint dashboard files for fabricated names, honorifics, and postnominals."
    )
    parser.add_argument("files", nargs="+", type=Path, metavar="FILE")
    parser.add_argument(
        "--format",
        choices=["human", "json"],
        default="human",
        dest="output_format",
    )
    args = parser.parse_args()

    all_violations: list[NameViolation] = []
    for filepath in args.files:
        if not filepath.exists():
            print(f"ERROR: {filepath} does not exist", file=sys.stderr)
            return 2
        try:
            violations = lint_file(filepath)
        except Exception as exc:
            print(f"ERROR: {filepath}: {exc}", file=sys.stderr)
            return 2
        all_violations.extend(violations)

    if args.output_format == "json":
        records = [
            {
                "path": str(v.file),
                "line": v.line,
                "col": v.column,
                "rule": v.rule,
                "matched_text": v.matched_text,
            }
            for v in all_violations
        ]
        print(json.dumps(records, indent=2))
    else:
        for v in all_violations:
            print(f"{v.file}:{v.line}:{v.column} [{v.rule}] {v.matched_text}")

    if all_violations:
        if args.output_format == "human":
            print(f"\n{len(all_violations)} violation(s) found.")
        return 1
    else:
        if args.output_format == "human":
            print("Clean — no violations found.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
