#!/usr/bin/env python3
"""Build the session-21 revision of the v1.x manuscript draft into a Typst-built PDF.
Same pipeline as 20260731-session20-build-pdf.py (pandoc -> typst, one input file),
pointed at the s21 revision, which supersedes the s20 draft with the T2a/T2b tier-label
correction. Prepends a title-page YAML metadata block to the paper's existing content.
Does not modify the source paper; writes a separate master file for pandoc. The
.master.md is a build intermediate: do not commit it (s9 tree-hygiene precedent).
Requires pandoc AND the typst CLI on PATH. Run from the WCF-Benchmark-v2/ project root."""
import subprocess, sys, pathlib

R = pathlib.Path("reports")
SRC = R / "20261018-session21-v1x-paper-draft.md"
MASTER = R / "20261018-session21-v1x-paper-draft.master.md"
OUT = R / "20261018-session21-v1x-paper-draft.pdf"

META = """---
title: "WCF-Bench-v2: Measuring Costly-Obedience Reasoning Under a Confessional Rubric"
subtitle: "v1.x manuscript draft, session-21 revision — venue-generic"
date: "2026-10-18"
lang: en
---

"""

TOC_DEPTH = "2"  # unchanged from the s20 script; see its comment for the rationale

def main():
    if not SRC.exists():
        sys.exit(f"MISSING: {SRC}")
    body = META + SRC.read_text(encoding="utf-8").rstrip() + "\n"
    MASTER.write_text(body, encoding="utf-8")
    cmd = [
        "pandoc", str(MASTER), "-o", str(OUT),
        "--pdf-engine=typst", "--toc", "--toc-depth", TOC_DEPTH,
        # No re-wrapping of the generated Typst: pandoc 3.1 can wrap a sentence so that a line
        # starts with "2." and Typst then reads it as a numbered list item.
        "--wrap=none",
        "-V", "fontsize=9pt",
        "-V", "margin-x=1.5cm", "-V", "margin-y=1.7cm",
        "-V", "papersize=a4",
    ]
    print("RUN:", " ".join(cmd))
    r = subprocess.run(cmd, capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    sys.stderr.write(r.stderr)
    if r.returncode != 0:
        sys.exit(f"pandoc failed ({r.returncode})")
    print(f"OK -> {OUT} ({OUT.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
