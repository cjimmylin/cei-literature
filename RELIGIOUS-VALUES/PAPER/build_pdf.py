#!/usr/bin/env python3
"""Convert introduction-religious-values.md to PDF via pandoc + typst.

Preprocesses LaTeX-style \cite{} into readable bracketed references,
cleans up LaTeX escapes, then runs pandoc with typst backend.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

PAPER_DIR = Path(__file__).parent
INPUT = PAPER_DIR / "introduction-religious-values.md"
OUTPUT = PAPER_DIR / "introduction-religious-values.pdf"

TITLE = "What Do Religious Values Benchmarks Actually Test?"
SUBTITLE = "A Systematic Meta-Evaluation of LLM Religious Alignment Assessments"
AUTHOR = "Jimmy Lin — Center for Ethical Intelligence"
DATE = "April 2026 — DRAFT"


def preprocess(text: str) -> str:
    """Convert LaTeX-isms to clean markdown for typst rendering."""

    # \cite{Key1, Key2} -> [Key1; Key2]
    def cite_repl(m: re.Match) -> str:
        keys = [k.strip() for k in m.group(1).split(",")]
        return "[" + "; ".join(keys) + "]"

    text = re.sub(r"\\cite\{([^}]+)\}", cite_repl, text)

    # \% -> %
    text = text.replace("\\%", "%")

    # --- (em-dash) already fine in typst/pandoc
    # *text* (italics) already fine

    # **bold** is fine for pandoc

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
    raw = INPUT.read_text(encoding="utf-8")
    cleaned = preprocess(raw)
    full = build_pandoc_metadata_block() + cleaned

    tmp = PAPER_DIR / "_tmp_for_pdf.md"
    tmp.write_text(full, encoding="utf-8")

    cmd = [
        "pandoc",
        str(tmp),
        "-o", str(OUTPUT),
        "--pdf-engine=typst",
        "--wrap=auto",
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Clean up temp file
    tmp.unlink(missing_ok=True)

    if result.returncode != 0:
        print("STDERR:", result.stderr, file=sys.stderr)
        sys.exit(1)

    print(f"PDF written to: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
