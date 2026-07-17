#!/usr/bin/env python3
"""Assemble the six session-9 readiness-briefing reports into one Typst-built PDF.
Reporting-only build artifact. Reads the six markdown reports, writes a master
markdown with a title page + TOC + page breaks, and renders via pandoc's typst engine.
Run from the WCF-Benchmark-v2/ project root."""
import subprocess, sys, pathlib

R = pathlib.Path("reports")
PARTS = [
    "20260717-session9-01-benchmark-card.md",
    "20260717-session9-02-evaluation.md",
    "20260717-session9-03-meta-judging.md",
    "20260717-session9-04-overview-of-work.md",
    "20260717-session9-05-next-steps.md",
    "20260717-session9-06-messaging.md",
]
MASTER = R / "20260717-session9-readiness-briefing.master.md"
OUT = R / "20260717-session9-readiness-briefing.pdf"

META = """---
title: "WCF-Bench-v2 — Scale-Up Readiness Briefing"
subtitle: "Christian-Ethics-Benchmark-v2 · sessions 1–8 · internal owner briefing"
date: "2026-07-17"
lang: en
---

*EXPLORATORY / NON-QUOTABLE. All scores are 0–100 panel-median rubric conformity
against the Westminster Standards — not accuracy; bank versions are separate
instruments. Prepared for internal review of scale-up readiness.*

"""

PAGEBREAK = "\n\n```{=typst}\n#pagebreak()\n```\n\n"

def main():
    body = META
    for i, name in enumerate(PARTS):
        p = R / name
        if not p.exists():
            sys.exit(f"MISSING: {p}")
        if i:
            body += PAGEBREAK
        body += p.read_text(encoding="utf-8").rstrip() + "\n"
    MASTER.write_text(body, encoding="utf-8")
    cmd = [
        "pandoc", str(MASTER), "-o", str(OUT),
        "--pdf-engine=typst", "--toc", "--toc-depth=2",
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
