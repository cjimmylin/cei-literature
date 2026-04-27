#!/usr/bin/env python3
"""Build combined PDF for MPBench Paper v2.

Combines all sections (except introduction and related work),
all supplementary material, and embeds figures inline.
Uses pandoc + typst for rendering.

Output: ../20260405-mpbench-v2-combined.pdf

Usage:
    cd CEI-Lit-WS/MORAL-PSYCH/PAPER-v2/scripts
    ../../../../.venv/bin/python build_combined_pdf.py
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PAPER_DIR = SCRIPT_DIR.parent
SECTIONS_DIR = PAPER_DIR / "sections"
SUPP_DIR = PAPER_DIR / "supplementary"
FIGURES_DIR = PAPER_DIR / "figures"
OUTPUT = PAPER_DIR / "20260405-mpbench-v3-combined.pdf"

# Main paper sections IN ORDER (excluding introduction and related work)
MAIN_SECTIONS = [
    "abstract-mpbench.md",
    "methodology-landscape-mpbench.md",
    "methodology-empirical-mpbench.md",
    "results-landscape-claims1-3.md",
    "results-landscape-claims4-5.md",
    "results-empirical-convergence.md",
    "results-empirical-scale-cot.md",
    "results-empirical-patterns.md",
    "discussion-mpbench.md",
    "conclusion-mpbench.md",
]

# Supplementary sections IN ORDER
SUPP_SECTIONS = [
    "supp-methods.md",
    "supp-results.md",
    "supp-tables.md",
    "supp-figures.md",
]

TITLE = "What Do Moral Psychology Benchmarks Actually Test?"
SUBTITLE = (
    "A Meta-Evaluation of the Benchmark Landscape and Cross-Vendor "
    "Empirical Replication Across Nine Models"
)
AUTHOR = "Jimmy Lin --- Center for Ethical Intelligence"
DATE = "April 2026 --- DRAFT v3.0"
VERSION = "v3.0"


def preprocess(text: str, base_dir: Path) -> str:
    """Clean markdown for typst rendering and resolve image paths."""

    # Convert \cite{Key1, Key2} -> [Key1; Key2]
    def cite_repl(m: re.Match) -> str:
        keys = [k.strip() for k in m.group(1).split(",")]
        return "[" + "; ".join(keys) + "]"

    text = re.sub(r"\\cite\{([^}]+)\}", cite_repl, text)
    text = text.replace("\\%", "%")

    # Resolve relative image paths to absolute paths
    # ![caption](figures/foo.png) -> ![caption](/absolute/path/figures/foo.png)
    def resolve_img(m: re.Match) -> str:
        caption = m.group(1)
        img_path = m.group(2)
        # Try to resolve relative to PAPER_DIR
        abs_path = PAPER_DIR / img_path
        if not abs_path.exists():
            # Try relative to section dir
            abs_path = base_dir / img_path
        if not abs_path.exists():
            # Try in figures dir directly
            fname = Path(img_path).name
            abs_path = FIGURES_DIR / fname
        if abs_path.exists():
            return f"![{caption}]({abs_path})"
        else:
            # Leave as-is, pandoc will warn
            return m.group(0)

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", resolve_img, text)

    return text


def build_metadata_block() -> str:
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


def read_section(path: Path) -> str:
    """Read and preprocess a section file."""
    if not path.exists():
        print(f"  WARNING: {path.name} not found, skipping", file=sys.stderr)
        return ""
    raw = path.read_text(encoding="utf-8")
    return preprocess(raw, path.parent)


def main() -> None:
    print(f"Building combined PDF for MPBench Paper v2...")
    print(f"Output: {OUTPUT}\n")

    parts: list[str] = []

    # --- Title page info ---
    parts.append(build_metadata_block())

    # --- Table of contents marker ---
    parts.append("# Table of Contents\n\n")
    parts.append("**Main Paper** (excluding Introduction and Related Work)\n\n")
    parts.append("- Abstract\n")
    parts.append("- 3. Methodology (Landscape: 3.1--3.5, 3.8)\n")
    parts.append("- 3. Methodology (Empirical: 3.6--3.7)\n")
    parts.append("- 4. Results Part I: Claims 1--3 (MFT Dominance, Construct Validity, Missing Theories)\n")
    parts.append("- 4. Results Part I: Claims 4--5 (Human Baselines, Format Mismatch) + Trial Highlights\n")
    parts.append("- 5. Results Part II: Cross-Vendor Convergence + RLHF Fingerprints\n")
    parts.append("- 5. Results Part II: Scale Sensitivity + Haiku CoT Effect\n")
    parts.append("- 5. Results Part II: Theory-Specific Patterns + Discrimination Audit\n")
    parts.append("- 6. Discussion\n")
    parts.append("- 7. Conclusion\n\n")
    parts.append("**Supplementary Material**\n\n")
    parts.append("- S1--S4. Supplementary Methods\n")
    parts.append("- S5--S7. Supplementary Results\n")
    parts.append("- ST1--ST5. Supplementary Tables\n")
    parts.append("- SF1--SF7. Supplementary Figures\n\n")
    parts.append(f"*Version: {VERSION} | Generated: 2026-04-05*\n\n")

    # --- Main paper sections ---
    print("Reading main paper sections:")
    for fname in MAIN_SECTIONS:
        path = SECTIONS_DIR / fname
        content = read_section(path)
        if content:
            parts.append(content)
            lines = content.count("\n")
            print(f"  + {fname} ({lines} lines)")

    # --- Supplementary divider ---
    parts.append("\n\n---\n\n")
    parts.append("# Supplementary Material\n\n")
    parts.append("*The following supplementary sections provide extended methodology, ")
    parts.append("detailed results, and comprehensive data tables that support the ")
    parts.append("main paper findings.*\n\n")

    # --- Supplementary sections ---
    print("\nReading supplementary sections:")
    for fname in SUPP_SECTIONS:
        path = SUPP_DIR / fname
        content = read_section(path)
        if content:
            parts.append(content)
            lines = content.count("\n")
            print(f"  + {fname} ({lines} lines)")

    # --- Combine ---
    combined = "\n\n\\newpage\n\n".join(parts)

    # Write temp file
    tmp = PAPER_DIR / "_tmp_combined.md"
    tmp.write_text(combined, encoding="utf-8")
    print(f"\nCombined markdown: {len(combined):,} characters")

    # Run pandoc
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
        print("\n--- PANDOC STDERR ---", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        print("--- END STDERR ---\n", file=sys.stderr)
        # Try to diagnose
        if "image" in result.stderr.lower() or "not found" in result.stderr.lower():
            print("HINT: Image path resolution issue. Check figure paths.", file=sys.stderr)
        sys.exit(1)

    size_kb = OUTPUT.stat().st_size / 1024
    print(f"\nPDF written to: {OUTPUT}")
    print(f"Size: {size_kb:.1f} KB")
    print("Done.")


if __name__ == "__main__":
    main()
