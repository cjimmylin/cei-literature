#!/usr/bin/env python3
"""Build the session-20 v1.x manuscript draft into a Typst-built PDF.
Single-source variant of 20260717-session9-build-pdf.py: one input file, no
page-break concatenation logic needed. Prepends a title-page YAML metadata
block to the paper's existing content and renders via pandoc's typst engine.
Does not modify the source paper; writes a separate master file for pandoc.
Run from the WCF-Benchmark-v2/ project root."""
import subprocess, sys, pathlib

R = pathlib.Path("reports")
SRC = R / "20260731-session20-v1x-paper-draft.md"
MASTER = R / "20260731-session20-v1x-paper-draft.master.md"
OUT = R / "20260731-session20-v1x-paper-draft.pdf"

META = """---
title: "WCF-Bench-v2: Measuring Costly-Obedience Reasoning Under a Confessional Rubric"
subtitle: "v1.x manuscript draft — venue-generic"
date: "2026-07-31"
lang: en
---

"""

TOC_DEPTH = "2"  # main sections only (##); the paper's #### worked-example
# subheadings (4 of them, under "### Worked examples") sit two levels below
# that and would need toc-depth=4 to surface, which — given they are four
# short, self-similar illustrative items nested under a section that's
# already itself a ToC entry — reads as clutter rather than navigation aid.
# Kept at 2 to match the s9 script's precedent and keep the ToC to the
# paper's 6 numbered top-level sections plus Abstract/Artifacts.

def main():
    if not SRC.exists():
        sys.exit(f"MISSING: {SRC}")
    body = META + SRC.read_text(encoding="utf-8").rstrip() + "\n"
    MASTER.write_text(body, encoding="utf-8")
    cmd = [
        "pandoc", str(MASTER), "-o", str(OUT),
        "--pdf-engine=typst", "--toc", "--toc-depth", TOC_DEPTH,
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
