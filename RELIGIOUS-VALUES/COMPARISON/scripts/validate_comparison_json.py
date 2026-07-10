#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def main() -> int:
    files = sorted(BASE.rglob("*.json"))
    bad = 0
    for path in files:
        try:
            json.load(open(path, encoding="utf-8"))
        except Exception as exc:
            bad += 1
            print(f"ERR {path.relative_to(BASE)}: {exc}")
    if bad:
        print(f"{bad} invalid JSON file(s)")
        return 1
    print(f"Validated {len(files)} JSON file(s). All valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
