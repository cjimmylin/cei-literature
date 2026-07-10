#!/usr/bin/env python3
"""
Write author geography and WEIRD score fields to all paper YAML files.

Reads pre-computed JSON data and writes 4 fields to each paper:
  - author_country: "XX"  (ISO code, quoted string)
  - author_region: "Region Name"  (quoted string)
  - author_global_north_south: "Global North" / "Global South" / "Ambiguous"  (quoted string)
  - weird_score: NN  (integer)

Usage:
    python write_all_cultural_fields.py [--dry-run]
"""
from __future__ import annotations

import functools
import json
import re
import sys
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent  # CULTURAL-GLOBAL/SCRIPTS/ → CEI-Lit-WS/
sys.path.insert(0, str(_CEI_LIT_WS / "PYTHON"))
sys.path.insert(0, str(_CEI_LIT_WS / ".agent" / "lib"))

from config import PAPERS_DIR

# ── Data paths ───────────────────────────────────────────────────────
DATA_DIR = _SCRIPT_DIR.parent / "DATA"
GEO_PATH = DATA_DIR / "20260403-author-geography.json"
WEIRD_PATH = DATA_DIR / "20260403-weird-scores.json"


def set_or_add_yaml_field(content: str, key: str, value: str) -> str:
    """Set existing field or insert before closing ---.

    Safe pattern per CLAUDE.md rule #2: uses re.subn with count=1.
    """
    pattern = rf'^{re.escape(key)}:.*$'
    replacement = f'{key}: {value}'
    new_content, count = re.subn(pattern, replacement, content, count=1, flags=re.MULTILINE)
    if count > 0:
        return new_content
    # Insert before closing ---
    first_end = content.find('---', 0)
    if first_end == -1:
        return content
    second_end = content.find('---', first_end + 3)
    if second_end == -1:
        return content
    before = content[:second_end].rstrip('\n')
    after = content[second_end:]
    return f"{before}\n{replacement}\n{after}"


def main() -> int:
    dry_run = "--dry-run" in sys.argv

    # ── Load data ────────────────────────────────────────────────────
    print(f"Loading geography data from {GEO_PATH.name}...")
    geo_data = json.loads(GEO_PATH.read_text())
    geo_by_file: dict[str, dict] = {}
    for entry in geo_data["papers"]:
        geo_by_file[entry["filename"]] = entry

    print(f"Loading WEIRD scores from {WEIRD_PATH.name}...")
    weird_data = json.loads(WEIRD_PATH.read_text())
    weird_by_file: dict[str, dict] = {}
    for entry in weird_data["papers"]:
        weird_by_file[entry["filename"]] = entry

    print(f"  Geography entries: {len(geo_by_file)}")
    print(f"  WEIRD entries: {len(weird_by_file)}")

    # ── Process papers ───────────────────────────────────────────────
    papers = sorted(PAPERS_DIR.glob("*.md"))
    total = len(papers)
    print(f"\nProcessing {total} papers...")
    if dry_run:
        print("  (DRY RUN — no files will be written)")

    written = 0
    skipped = 0
    missing_geo = 0
    missing_weird = 0

    for i, paper_path in enumerate(papers, 1):
        if i % 200 == 0:
            print(f"  Progress: {i}/{total} (written: {written})")

        fname = paper_path.name
        geo = geo_by_file.get(fname)
        weird = weird_by_file.get(fname)

        if not geo:
            missing_geo += 1
        if not weird:
            missing_weird += 1

        # Skip if we have no data at all
        if not geo and not weird:
            skipped += 1
            continue

        content = paper_path.read_text(encoding="utf-8", errors="replace")
        original = content

        # Write geography fields (quoted strings)
        if geo:
            country = geo.get("author_country", "")
            region = geo.get("author_region", "")
            ns = geo.get("author_global_north_south", "")

            if country:
                content = set_or_add_yaml_field(content, "author_country", f'"{country}"')
            if region:
                content = set_or_add_yaml_field(content, "author_region", f'"{region}"')
            if ns:
                content = set_or_add_yaml_field(content, "author_global_north_south", f'"{ns}"')

        # Write WEIRD score (integer)
        if weird:
            score = weird.get("weird_score")
            if score is not None:
                content = set_or_add_yaml_field(content, "weird_score", str(int(score)))

        if content != original and not dry_run:
            paper_path.write_text(content, encoding="utf-8")
            written += 1
        elif content != original:
            written += 1

    print(f"\n{'='*60}")
    print(f"CULTURAL FIELD WRITE RESULTS")
    print(f"{'='*60}")
    print(f"Total papers: {total}")
    print(f"Written: {written}")
    print(f"Skipped (no data): {skipped}")
    print(f"Missing geography: {missing_geo}")
    print(f"Missing WEIRD: {missing_weird}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
