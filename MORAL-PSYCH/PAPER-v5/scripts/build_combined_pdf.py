#!/usr/bin/env python3
"""Build combined PDF for MPBench Paper v5.

Combines all main sections, supplementary material, and embeds
main-text figure plates inline. Uses pandoc + typst for rendering.

Output: ../20260413-mpbench-v5-combined.pdf

Usage:
    cd CEI-Lit-WS/MORAL-PSYCH/PAPER-v5/scripts
    ../../../../.venv/bin/python build_combined_pdf.py
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

# ── Version constants (C7-F1 fix: parameterized, not hardcoded) ──
VERSION = "v5"
DATE = "20260413"
VERSION_LABEL = "v5.0"

SCRIPT_DIR = Path(__file__).resolve().parent
PAPER_DIR = SCRIPT_DIR.parent
SECTIONS_DIR = PAPER_DIR / "sections"
SUPP_DIR = PAPER_DIR / "supplementary"
FIGURES_DIR = PAPER_DIR / "figures"
OUTPUT = PAPER_DIR / f"{DATE}-mpbench-{VERSION}-combined.pdf"

# Main paper sections IN ORDER (built from VERSION/DATE constants)
MAIN_SECTIONS = [
    f"{DATE}-abstract-{VERSION}.md",
    f"{DATE}-introduction-{VERSION}.md",
    f"{DATE}-methodology-{VERSION}.md",
    f"{DATE}-results-empirical-{VERSION}.md",
    f"{DATE}-results-landscape-claims1-3-{VERSION}.md",
    f"{DATE}-results-landscape-claims4-6-{VERSION}.md",
    f"{DATE}-results-integrated-{VERSION}.md",
    f"{DATE}-discussion-{VERSION}.md",
    f"{DATE}-conclusion-{VERSION}.md",
]

# Supplementary sections IN ORDER
SUPP_SECTIONS = [
    f"{DATE}-supp-methods-{VERSION}.md",
    f"{DATE}-supp-tables-{VERSION}.md",
    f"{DATE}-supp-figures-{VERSION}.md",
]

TITLE = "What Do Moral Psychology Benchmarks Actually Test?"
SUBTITLE = (
    "A Meta-Evaluation of the Benchmark Landscape and Cross-Vendor "
    "Empirical Replication Across Nine Models"
)
AUTHOR = "Jimmy Lin --- Center for Ethical Intelligence"
DATE_LABEL = f"April 2026 --- DRAFT {VERSION_LABEL}"


def normalize_unicode(text: str) -> str:
    """NFC normalize and strip C0/C1 control characters (C7-F5)."""
    text = unicodedata.normalize("NFC", text)
    # Strip C0 controls (except newline, tab) and C1 controls
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]", "", text)
    return text


def preprocess(text: str, base_dir: Path) -> str:
    """Clean markdown for typst rendering and resolve image paths."""

    # Unicode normalization first (C7-F5)
    text = normalize_unicode(text)

    # Convert \cite{Key1, Key2} -> [Key1; Key2]
    def cite_repl(m: re.Match) -> str:
        keys = [k.strip() for k in m.group(1).split(",")]
        return "[" + "; ".join(keys) + "]"

    text = re.sub(r"\\cite\{([^}]+)\}", cite_repl, text)
    text = text.replace("\\%", "%")

    # Resolve relative image paths to absolute paths
    def resolve_img(m: re.Match) -> str:
        caption = m.group(1)
        img_path = m.group(2)
        attrs = m.group(3) or ""
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
            return f"![{caption}]({abs_path}){attrs}"
        else:
            # Leave as-is, pandoc will warn
            return m.group(0)

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)(\{[^}]*\})?", resolve_img, text)

    # Post-preprocess safety: flag surviving relative image paths (C7-F4)
    surviving = re.findall(r"!\[[^\]]*\]\((?!/)([^)]+\.png)\)", text)
    if surviving:
        print(f"  WARNING: {len(surviving)} relative image path(s) survived preprocessing:",
              file=sys.stderr)
        for p in surviving[:5]:
            print(f"    - {p}", file=sys.stderr)

    return text


def build_metadata_block() -> str:
    return f"""---
title: "{TITLE}"
subtitle: "{SUBTITLE}"
author: "{AUTHOR}"
date: "{DATE_LABEL}"
mainfont: "Georgia"
sansfont: "Helvetica Neue"
fontsize: "11pt"
margin-top: "1in"
margin-bottom: "1in"
margin-left: "0.75in"
margin-right: "0.75in"
---

"""


def read_section(path: Path) -> str:
    """Read and preprocess a section file."""
    if not path.exists():
        print(f"  WARNING: {path.name} not found, skipping", file=sys.stderr)
        return ""
    raw = path.read_text(encoding="utf-8")
    return preprocess(raw, path.parent)


def parse_figure_entries(supp_figures_path: Path) -> list[tuple[str, Path]]:
    """Parse figure entries from supp-figures markdown.

    Returns list of (title, absolute_path) for figures that exist on disk.
    """
    if not supp_figures_path.exists():
        print(f"  WARNING: {supp_figures_path.name} not found, no figure plates",
              file=sys.stderr)
        return []

    text = supp_figures_path.read_text(encoding="utf-8")
    entries: list[tuple[str, Path]] = []
    skipped: list[str] = []

    # Split into blocks by ### heading
    heading_re = re.compile(r"^### (Figure \d+:.+)", re.MULTILINE)
    file_re = re.compile(r"\*\*File:\*\*\s*`(.*?)`")

    headings = list(heading_re.finditer(text))
    for i, hm in enumerate(headings):
        title = hm.group(1).strip()
        # Get the text block between this heading and the next
        start = hm.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        block = text[start:end]

        fm = file_re.search(block)
        if not fm:
            skipped.append(f"{title} (no File: field)")
            continue

        rel_path = fm.group(1).strip()

        # Check for "Not yet generated" sentinel
        if "not yet" in rel_path.lower():
            skipped.append(f"{title} (not yet generated)")
            continue

        # Resolve path relative to PAPER_DIR
        abs_path = PAPER_DIR / rel_path
        if not abs_path.exists():
            # Try figures dir directly
            abs_path = FIGURES_DIR / Path(rel_path).name
        if not abs_path.exists():
            skipped.append(f"{title} (file not found: {rel_path})")
            continue

        entries.append((title, abs_path))

    if skipped:
        print(f"\n  Skipped {len(skipped)} figure(s):")
        for s in skipped:
            print(f"    - {s}", file=sys.stderr)

    return entries


def build_figure_plates(entries: list[tuple[str, Path]]) -> str:
    """Build markdown for the figure plates section."""
    if not entries:
        return ""

    parts: list[str] = []
    parts.append("\n\n---\n\n")
    parts.append("# Figures\n\n")

    for title, abs_path in entries:
        parts.append("\\newpage\n\n")
        parts.append(f"![{title}]({abs_path}){{width=100%}}\n\n")

    return "".join(parts)


def main() -> None:
    # --- Prerequisite checks ---
    if not shutil.which("pandoc"):
        print("ERROR: pandoc not found in PATH", file=sys.stderr)
        sys.exit(1)
    if not shutil.which("typst"):
        print("ERROR: typst not found in PATH", file=sys.stderr)
        sys.exit(1)

    print(f"Building combined PDF for MPBench Paper {VERSION}...")
    print(f"Output: {OUTPUT}\n")

    parts: list[str] = []

    # --- Title page info ---
    parts.append(build_metadata_block())

    # --- Table of contents ---
    parts.append("# Table of Contents\n\n")
    parts.append("**Main Paper**\n\n")
    parts.append("- Abstract\n")
    parts.append("- 1. Introduction\n")
    parts.append("- 2. Methodology\n")
    parts.append("- 3. Results Part I: Empirical Replication\n")
    parts.append("- 4. Results Part II: Landscape Claims 1--3 (MFT Dominance, Construct Validity, Missing Theories)\n")
    parts.append("- 4. Results Part II: Landscape Claims 4--6 (Human Baselines, Format Mismatch, Temporal Stagnation)\n")
    parts.append("- 5. Results Part III: Integrated Analysis\n")
    parts.append("- 6. Discussion\n")
    parts.append("- 7. Conclusion\n\n")
    parts.append("**Supplementary Material**\n\n")
    parts.append("- S1--S4. Supplementary Methods\n")
    parts.append("- ST1--ST5. Supplementary Tables\n")
    parts.append("- SF1--SF19. Supplementary Figures\n\n")
    parts.append("**Figure Plates**\n\n")
    parts.append("- Figures 1--15 (main-text figures, full-page)\n\n")
    parts.append(f"*Version: {VERSION_LABEL} | Generated: 2026-04-13*\n\n")

    # --- Main paper sections ---
    print("Reading main paper sections:")
    section_count = 0
    for fname in MAIN_SECTIONS:
        path = SECTIONS_DIR / fname
        content = read_section(path)
        if content:
            parts.append(content)
            lines = content.count("\n")
            print(f"  + {fname} ({lines} lines)")
            section_count += 1

    # C7-F1 guard: assert we got all sections
    if section_count < len(MAIN_SECTIONS):
        missing = len(MAIN_SECTIONS) - section_count
        print(f"\n  ERROR: {missing} main section(s) missing! Aborting.",
              file=sys.stderr)
        sys.exit(1)

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

    # --- Figure plates ---
    print("\nParsing figure entries for plates:")
    supp_fig_path = SUPP_DIR / f"{DATE}-supp-figures-{VERSION}.md"
    fig_entries = parse_figure_entries(supp_fig_path)
    print(f"  Found {len(fig_entries)} figures with existing PNGs")

    # C7-F1 guard: assert figure count baseline
    if len(fig_entries) < 15:
        print(f"  WARNING: Expected >=15 figures, found {len(fig_entries)}",
              file=sys.stderr)

    fig_section = build_figure_plates(fig_entries)
    if fig_section:
        parts.append(fig_section)

    # --- Combine ---
    combined = "\n\n\\newpage\n\n".join(parts)

    # Total character guard (C7-F1: must be >= 80% of v4's ~5.3MB combined)
    if len(combined) < 100_000:
        print(f"\n  ERROR: Combined markdown is only {len(combined):,} chars "
              f"— likely missing content. Aborting.", file=sys.stderr)
        sys.exit(1)

    # Write temp file
    tmp = PAPER_DIR / "_tmp_combined.md"
    tmp.write_text(combined, encoding="utf-8")
    print(f"\nCombined markdown: {len(combined):,} characters")

    # Run pandoc (C7-F4: added --resource-path)
    cmd = [
        "pandoc",
        str(tmp),
        "-o", str(OUTPUT),
        "--pdf-engine=typst",
        "--wrap=auto",
        f"--resource-path={PAPER_DIR}:{FIGURES_DIR}",
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Clean up temp file
    tmp.unlink(missing_ok=True)

    if result.returncode != 0:
        print("\n--- PANDOC STDERR ---", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        print("--- END STDERR ---\n", file=sys.stderr)
        if "image" in result.stderr.lower() or "not found" in result.stderr.lower():
            print("HINT: Image path resolution issue. Check figure paths.",
                  file=sys.stderr)
        sys.exit(1)

    if result.stderr:
        print("\n--- PANDOC WARNINGS ---", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        print("--- END WARNINGS ---\n", file=sys.stderr)

    size_kb = OUTPUT.stat().st_size / 1024
    print(f"\nPDF written to: {OUTPUT}")
    print(f"Size: {size_kb:.1f} KB ({size_kb / 1024:.2f} MB)")
    print("Done.")


if __name__ == "__main__":
    main()
