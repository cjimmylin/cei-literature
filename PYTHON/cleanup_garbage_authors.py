#!/usr/bin/env python3
"""
Clean up garbage author profiles — move to RECYCLE-BIN.

Categories:
1. Single-letter-dot stubs (A..md, B..md, ...)
2. Non-person names (approach.md, LLMs.md, ...)
3. "Multiple authors" variants
4. Institutional/org names
5. Malformed names (ampersand, duplicated)
6. Editor labels
7. Concatenated two-person stubs (two distinct names, no comma)

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/cleanup_garbage_authors.py
    ../.venv/bin/python PYTHON/cleanup_garbage_authors.py --dry-run
"""

import shutil
from pathlib import Path
from datetime import date
import sys

AUTHORS_DIR = Path("Authors")
RECYCLE_DIR = Path("RECYCLE-BIN") / f"{date.today().strftime('%Y%m%d')}-garbage-authors"

DRY_RUN = '--dry-run' in sys.argv

# === GARBAGE LIST ===

# Category 1: Single-letter-dot stubs
SINGLE_LETTER = [f"{c}." for c in "ABCDFGHJMNQSVXY"]

# Category 2: Non-person names
NON_PERSON = [
    "approach",
    "contributions",
    "LLMs",
    "Tuesday",
    "Microsoft",
]

# Category 3: "Multiple authors" variants
MULTIPLE = [
    "Multiple (Data in Brief",
    "Multiple (Journal of King Saud University",
    "Multiple (MDPI Big Data",
    "Multiple (MDPI Electronics 2025)",
    "Multiple (not fully specified in search",
    "Multiple authors (American University)",
    "Multiple authors (Turkish NLP community)",
    "Multiple authors (presented at conference on Human Freedom",
    "Multiple authors",
]

# Category 4: Institutional/org names
INSTITUTIONAL = [
    "IMSyPP Project Team",
    "People's Republic of China Ministry of Industry and Information Technology (MIIT)",
    "Research and Data Management Sector Chiefs of Ontario",
    "International Islamic Univ Malaysia",
]

# Category 5: Malformed names
MALFORMED = [
    "A. & Xu",
    "A.R",
    "K. & Chun",
    "S. & Demberg",
    "Yuan Yi Yuan Yi",
]

# Category 6: Editor labels
EDITORS = [
    "Katharina von der Wense (editors)",
    "Müller, Regina (eds.)",
]

# Category 7: Concatenated two-person stubs
CONCATENATED = [
    "Benjamin Olsen Nina Lutz",
    "Hiroshi Ishiguro Emily Burdett",
    "Hossein Sameti Ehsaneddin Asgari",
    "Jiseon Kim Jiho Jin",
    "Jordan Lachler Darren Flavelle",
    "Kosuke Sato Shogo Ikari",
    "Mary Reisel Vassilis Galanos",
    "Nadia Hajipour Farzaneh Goshtasb",
    "Parnian Fazel Farhan Farsi",
    "Qian Yu Zeming Liu",
    "Qiankun Li Chuanpu Liu",
    "Qiyuan Li Haijiang Liu",
    "Ramin Rahnamoun Rashin Rahnamoun",
    "Sadra Sabouri Sepand Haghighi",
    "Sanchit Ahuja Agrima Seth",
    "Tahu Kukutai Maggie Walter",
    "C. Mhungu D. Mykhaylychenko",
    "D. Baradari M. Thasin",
    "E. Glen Weyl Weishung Liu",
    "Holly Randell-Moon Jessica Russ-Smith",
    "Max Van Kleek William Seymour",
    "Olena Mykhailenko Todd J.B. Blayone",
    "Xiang Wan Ruoyu Sun",
    "Yo Nakawake Jonathan Jong",
    "Anders Blok Casper Bruun Jensen",
    "Terina Kamailelauli'i Fa'agau Ian Falefuafua Tapu",
]

ALL_GARBAGE = SINGLE_LETTER + NON_PERSON + MULTIPLE + INSTITUTIONAL + MALFORMED + EDITORS + CONCATENATED

def main():
    if DRY_RUN:
        print("=== DRY RUN ===\n")

    if not DRY_RUN:
        RECYCLE_DIR.mkdir(parents=True, exist_ok=True)

    moved = 0
    missing = 0
    categories = {
        "Single-letter": SINGLE_LETTER,
        "Non-person": NON_PERSON,
        "Multiple authors": MULTIPLE,
        "Institutional": INSTITUTIONAL,
        "Malformed": MALFORMED,
        "Editor labels": EDITORS,
        "Concatenated": CONCATENATED,
    }

    for cat_name, names in categories.items():
        cat_moved = 0
        for name in names:
            src = AUTHORS_DIR / f"{name}.md"
            if src.exists():
                if DRY_RUN:
                    print(f"  [DRY] Would move: {name}.md")
                else:
                    dst = RECYCLE_DIR / f"{name}.md"
                    shutil.move(str(src), str(dst))
                cat_moved += 1
            else:
                missing += 1
        if cat_moved:
            print(f"  {cat_name}: {cat_moved} moved")

    moved = sum(1 for n in ALL_GARBAGE if (AUTHORS_DIR / f"{n}.md").exists()) if DRY_RUN else \
            sum(1 for n in ALL_GARBAGE if (RECYCLE_DIR / f"{n}.md").exists())

    print(f"\n{'=' * 50}")
    print(f"CLEANUP SUMMARY")
    print(f"{'=' * 50}")
    print(f"Total garbage identified: {len(ALL_GARBAGE)}")
    print(f"Moved to RECYCLE-BIN:     {moved}")
    print(f"Already missing:          {missing}")
    print(f"Destination:              {RECYCLE_DIR}")
    print(f"{'=' * 50}")


if __name__ == '__main__':
    main()
