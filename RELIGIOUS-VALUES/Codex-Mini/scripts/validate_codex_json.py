#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
TARGETS = [BASE / "results", BASE / "data", BASE / "trials"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate JSON files under Codex/")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    files = []
    for root in TARGETS:
        if root.exists():
            files.extend(sorted(root.rglob("*.json")))

    bad = 0
    for path in files:
        try:
            with open(path, encoding="utf-8") as f:
                json.load(f)
            if args.verbose:
                print(f"OK  {path.relative_to(BASE)}")
        except Exception as exc:
            bad += 1
            print(f"ERR {path.relative_to(BASE)}: {exc}")

    if bad:
        print(f"\n{bad} JSON file(s) invalid.")
        return 1

    print(f"Validated {len(files)} JSON file(s). All valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
