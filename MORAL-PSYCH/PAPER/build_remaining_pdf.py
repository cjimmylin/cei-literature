#!/usr/bin/env python3
"""Generate PDF for remaining moral-psych paper sections (abstract through conclusion).

Concatenates abstract, methodology, results, discussion, and conclusion into
a single PDF via pandoc + typst.  Follows the pattern in RELIGIOUS-VALUES/PAPER/build_pdf.py.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

PAPER_DIR = Path(__file__).parent
OUTPUT = PAPER_DIR / "remaining-sections-mpbench.pdf"

SECTIONS = [
    "abstract-mpbench.md",
    "methodology-mpbench.md",
    "results-mpbench.md",
    "discussion-mpbench.md",
    "conclusion-mpbench.md",
]

TITLE = "What Do Moral Psychology Benchmarks Actually Test?"
SUBTITLE = "Sections 3\u20136: Abstract, Methodology, Results, Discussion, Conclusion"
AUTHOR = "Jimmy Lin \u2014 Center for Ethical Intelligence"
DATE = "April 2026 \u2014 DRAFT"


def preprocess(text: str) -> str:
    """Convert LaTeX-isms to clean markdown for typst rendering."""

    # \cite{Key1, Key2} -> [Key1; Key2]
    def cite_repl(m: re.Match) -> str:
        keys = [k.strip() for k in m.group(1).split(",")]
        return "[" + "; ".join(keys) + "]"

    text = re.sub(r"\\cite\{([^}]+)\}", cite_repl, text)
    text = text.replace("\\%", "%")
    return text


def build_pandoc_metadata_block() -> str:
    return f"""---
title: "{TITLE}"
subtitle: "{SUBTITLE}"
author: "{AUTHOR}"
date: "{DATE}"
mainfont: "Georgia"
sansfont: "Helvetica Neue"
fontsize: "11pt"
margin-top: "1in"
margin-bottom: "1in"
margin-left: "1in"
margin-right: "1in"
---

"""


def main() -> None:
    parts: list[str] = []
    for fname in SECTIONS:
        path = PAPER_DIR / fname
        if not path.exists():
            print(f"WARNING: {fname} not found, skipping", file=sys.stderr)
            continue
        raw = path.read_text(encoding="utf-8")
        parts.append(preprocess(raw))

    if not parts:
        print("ERROR: No section files found", file=sys.stderr)
        sys.exit(1)

    combined = build_pandoc_metadata_block() + "\n\\newpage\n\n".join(parts)

    tmp = PAPER_DIR / "_tmp_remaining.md"
    tmp.write_text(combined, encoding="utf-8")

    cmd = [
        "pandoc",
        str(tmp),
        "-o", str(OUTPUT),
        "--pdf-engine=typst",
        "--wrap=auto",
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    tmp.unlink(missing_ok=True)

    if result.returncode != 0:
        print("STDERR:", result.stderr, file=sys.stderr)
        sys.exit(1)

    size_kb = OUTPUT.stat().st_size / 1024
    print(f"PDF written to: {OUTPUT}")
    print(f"Size: {size_kb:.1f} KB")


if __name__ == "__main__":
    main()
