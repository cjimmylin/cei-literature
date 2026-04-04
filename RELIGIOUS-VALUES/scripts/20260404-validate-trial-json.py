#!/usr/bin/env python3
"""Validate and optionally repair trial JSON files.

Agent-generated JSON (via Write tool) often contains unescaped quotes
inside string values. This script detects and fixes them.

Usage:
    python 20260404-validate-trial-json.py              # validate only
    python 20260404-validate-trial-json.py --fix        # validate + repair in-place
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data"
TRIALS_DIR = BASE / "trials"


def fix_unescaped_quotes(text: str) -> str:
    """Fix unescaped double quotes inside JSON string values.

    Strategy: walk the text character-by-character tracking whether we're
    inside a JSON string. A quote that isn't preceded by backslash and
    isn't a structural string delimiter (opener/closer) gets escaped.
    """
    result = []
    i = 0
    in_string = False
    while i < len(text):
        ch = text[i]
        if ch == '\\' and in_string:
            # Escaped character — pass through both chars
            result.append(ch)
            if i + 1 < len(text):
                i += 1
                result.append(text[i])
            i += 1
            continue
        if ch == '"':
            if not in_string:
                in_string = True
                result.append(ch)
            else:
                # Is this the closing quote? Look ahead for structural JSON
                rest = text[i + 1:].lstrip()
                if rest and rest[0] in ',:}]\n\r':
                    # Structural close
                    in_string = False
                    result.append(ch)
                else:
                    # Unescaped quote inside string — escape it
                    result.append('\\"')
            i += 1
            continue
        result.append(ch)
        i += 1
    return ''.join(result)


def validate_file(path: Path, fix: bool = False) -> bool:
    """Validate a single JSON file. Returns True if valid (or fixed)."""
    text = path.read_text(encoding="utf-8")
    try:
        json.loads(text)
        print(f"  OK   {path.name}")
        return True
    except json.JSONDecodeError as e:
        print(f"  FAIL {path.name}: {e}")
        if not fix:
            return False

        # Attempt repair
        fixed = fix_unescaped_quotes(text)
        try:
            json.loads(fixed)
            path.write_text(fixed, encoding="utf-8")
            print(f"       -> REPAIRED {path.name}")
            return True
        except json.JSONDecodeError as e2:
            print(f"       -> REPAIR FAILED: {e2}")
            return False


def main() -> None:
    fix = "--fix" in sys.argv

    print(f"Mode: {'validate + repair' if fix else 'validate only'}")
    print(f"Scanning: {DATA_DIR} and {TRIALS_DIR}\n")

    json_files = sorted(DATA_DIR.glob("*.json")) + sorted(TRIALS_DIR.glob("*.json"))
    if not json_files:
        print("No JSON files found.")
        return

    ok = 0
    fail = 0
    for path in json_files:
        if validate_file(path, fix=fix):
            ok += 1
        else:
            fail += 1

    print(f"\nResults: {ok} valid, {fail} {'repaired' if fix else 'invalid'} out of {ok + fail} files")


if __name__ == "__main__":
    main()
