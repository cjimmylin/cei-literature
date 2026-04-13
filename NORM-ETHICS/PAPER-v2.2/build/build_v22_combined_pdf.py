#!/usr/bin/env python3
"""Build combined PDF for NormEval Paper v2.2-preliminary.

Assembles all markdown section files from PAPER-v2.2/source/ into a single
PDF with title page, watermark footer, embedded figures, and license page.

Forked from: CEI-AI-Statements/children/paper/generate_v3_combined_pdf.py
Adapted for NormEval v2.2-preliminary (2026-04-13, Session 19).

Output:
  PAPER-v2.2/build/20260413-normeval-paper-v2.2-preliminary.pdf

Usage:
  .venv/bin/python CEI-Lit-WS/NORM-ETHICS/PAPER-v2.2/build/build_v22_combined_pdf.py
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from fpdf import FPDF, XPos, YPos

# ── paths ────────────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent  # PAPER-v2.2/
SOURCE_DIR = BASE / "source"
FIG_DIR = BASE / "figures"
BUILD_DIR = BASE / "build"
OUT_PDF = BUILD_DIR / "20260413-normeval-paper-v2.2-preliminary.pdf"

# ── section order ────────────────────────────────────────────────────────────
SECTIONS = [
    ("Abstract", "abstract-normeval-v2.2-preliminary.md"),
    ("1. Introduction", "introduction-comprehensive-normeval-v2.2-preliminary.md"),
    ("2. Methods", "methods-normeval-v2.2-preliminary.md"),
    ("3. Results: Landscape Analysis", "results-landscape-normeval-v2.2-preliminary.md"),
    ("4. Results: Implementation Trials", "results-trials-normeval-v2.2-preliminary.md"),
    ("5. Results: Cross-Vendor Analysis", "results-crossvendor-normeval-v2.2-preliminary.md"),
    ("6. Discussion", "discussion-normeval-v2.2-preliminary.md"),
    ("7. Limitations", "limitations-normeval-v2.2-preliminary.md"),
    ("8. Conclusion", "conclusion-normeval-v2.2-preliminary.md"),
    ("Data Availability", "data-availability-normeval-v2.2-preliminary.md"),
    ("References", "references-normeval-v2.2-preliminary.md"),
]

APPENDICES = [
    ("Appendix K: Prompt Provenance", "appendix-k-prompt-provenance-v2.2-preliminary.md"),
]

# ── Unicode sanitization (from children paper builder) ───────────────────────
UNICODE_MAP = {
    "\u2013": "-",   # en-dash
    "\u2014": "--",  # em-dash
    "\u2018": "'",   # left single quote
    "\u2019": "'",   # right single quote
    "\u201c": '"',   # left double quote
    "\u201d": '"',   # right double quote
    "\u2026": "...", # ellipsis
    "\u00d7": "x",   # multiplication sign
    "\u2264": "<=",  # less than or equal
    "\u2265": ">=",  # greater than or equal
    "\u03b1": "alpha",
    "\u03b2": "beta",
    "\u03ba": "kappa",
    "\u2248": "~",   # approximately
    "\u221e": "inf", # infinity
    "\u00b2": "^2",  # superscript 2
    "\u207b": "-",   # superscript minus
    "\u00b9": "^1",  # superscript 1
    "\u2212": "-",   # minus sign
}

def sanitize(text: str) -> str:
    for char, repl in UNICODE_MAP.items():
        text = text.replace(char, repl)
    # Catch remaining non-Latin-1 characters
    return text.encode("latin-1", errors="replace").decode("latin-1")


# ── Heading size map ─────────────────────────────────────────────────────────
HEADING_SIZES = {1: 16, 2: 14, 3: 12, 4: 11, 5: 10, 6: 10}


class NormEvalPDF(FPDF):
    """PDF builder with watermark footer and title page."""

    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)
        # Use built-in fonts (no custom font files needed)
        self.add_page()

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(160, 160, 160)
        self.cell(
            0, 10,
            "DRAFT -- NOT FOR CITATION -- NormEval v2.2-preliminary -- Page %d" % self.page_no(),
            align="C",
            new_x=XPos.RIGHT, new_y=YPos.TOP,
        )

    def title_page(self):
        self.set_font("Helvetica", "B", 18)
        self.ln(40)
        self.multi_cell(0, 10, sanitize(
            "Three Ethical Profiles, One Knowledge Ceiling:\n"
            "A Meta-Evaluation of 54 Normative Ethics Benchmarks\n"
            "Across Nine LLMs and Three Vendors"
        ), align="C")
        self.ln(10)
        self.set_font("Helvetica", "", 12)
        self.cell(0, 8, "v2.2-preliminary", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(0, 8, "Generated: 2026-04-13", align="C",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(10)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(180, 80, 0)
        self.multi_cell(0, 7, sanitize(
            "DRAFT -- NOT FOR CITATION\n\n"
            "Cross-vendor results (GPT-5, GPT-5-mini, Gemini models) were generated\n"
            "through in-context elicitation, not direct API calls.\n"
            "These findings are exploratory hypotheses awaiting external replication.\n"
            "See Limitations Section 7 and Appendix K for methodology details."
        ), align="C")
        self.set_text_color(0, 0, 0)

    def license_page(self):
        self.add_page()
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "License", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(5)
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 6, sanitize(
            "Code and analysis scripts: MIT License\n"
            "Data artifacts (feature matrix, trial outputs, dashboards): "
            "Creative Commons Attribution 4.0 International (CC-BY-4.0)\n\n"
            "Third-party benchmark items remain under their original licenses; "
            "we redistribute only summary statistics and item-level scores, not source items.\n\n"
            "Interactive dashboards:\n"
            "  v1: https://cjimmylin.github.io/cei-normeval-dashboard/\n"
            "  v2: https://cjimmylin.github.io/cei-normeval-dashboard-v2/\n"
            "  v3: https://cjimmylin.github.io/cei-normeval-dashboard-v3/\n"
            "  v4: https://cjimmylin.github.io/cei-normeval-dashboard-v4/\n\n"
            "Project repository: https://github.com/cjimmylin/cei-literature"
        ))

    def add_section(self, title: str, md_path: Path):
        """Parse a markdown file and render it to PDF."""
        if not md_path.exists():
            print(f"  WARNING: {md_path.name} not found, skipping")
            return

        text = md_path.read_text(encoding="utf-8")
        # Strip YAML frontmatter
        if text.startswith("---"):
            end = text.find("---", 3)
            if end > 0:
                text = text[end + 3:].strip()

        # Section heading
        self.add_page()
        self.set_font("Helvetica", "B", HEADING_SIZES[1])
        self.cell(0, 10, sanitize(title),
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)

        # Process line by line
        self.set_font("Helvetica", "", 10)
        in_code_block = False
        in_table = False
        table_rows: list[list[str]] = []

        for line in text.split("\n"):
            # Code blocks
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                if not in_code_block and table_rows:
                    self._render_table(table_rows)
                    table_rows = []
                continue
            if in_code_block:
                self.set_font("Courier", "", 8)
                self.cell(0, 4, sanitize(line),
                          new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                self.set_font("Helvetica", "", 10)
                continue

            # Tables
            if "|" in line and line.strip().startswith("|"):
                cells = [c.strip() for c in line.strip().split("|")[1:-1]]
                # Skip separator rows
                if all(set(c) <= set("-: ") for c in cells):
                    continue
                table_rows.append(cells)
                in_table = True
                continue
            elif in_table:
                if table_rows:
                    self._render_table(table_rows)
                    table_rows = []
                in_table = False

            # Headings
            heading_match = re.match(r"^(#{1,6})\s+(.*)", line)
            if heading_match:
                level = len(heading_match.group(1))
                heading_text = heading_match.group(2)
                # Strip markdown formatting
                heading_text = re.sub(r"\*\*(.*?)\*\*", r"\1", heading_text)
                heading_text = re.sub(r"\*(.*?)\*", r"\1", heading_text)
                size = HEADING_SIZES.get(level, 10)
                self.ln(3)
                self.set_font("Helvetica", "B", size)
                self.multi_cell(0, size * 0.45, sanitize(heading_text))
                self.ln(2)
                self.set_font("Helvetica", "", 10)
                continue

            # Horizontal rule
            if line.strip() in ("---", "***", "___"):
                self.ln(2)
                self.set_draw_color(200, 200, 200)
                self.line(self.l_margin, self.get_y(),
                          self.w - self.r_margin, self.get_y())
                self.ln(4)
                continue

            # Bold lines (often used as labels)
            bold_match = re.match(r"^\*\*(.*?)\*\*\s*(.*)", line)
            if bold_match and not line.startswith("- "):
                self.set_font("Helvetica", "B", 10)
                label = sanitize(bold_match.group(1))
                rest = sanitize(bold_match.group(2))
                self.write(5, label)
                if rest:
                    self.set_font("Helvetica", "", 10)
                    self.write(5, " " + rest)
                self.ln(6)
                self.set_font("Helvetica", "", 10)
                continue

            # Bullet points
            if line.strip().startswith("- "):
                content = line.strip()[2:]
                content = re.sub(r"\*\*(.*?)\*\*", r"\1", content)
                content = re.sub(r"\*(.*?)\*", r"\1", content)
                content = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", content)  # links
                old_margin = self.l_margin
                self.set_left_margin(old_margin + 8)
                self.set_x(old_margin + 8)
                self.multi_cell(0, 5, sanitize("* " + content))
                self.set_left_margin(old_margin)
                continue

            # Empty line
            if not line.strip():
                self.ln(3)
                continue

            # Regular paragraph
            clean = re.sub(r"\*\*(.*?)\*\*", r"\1", line)
            clean = re.sub(r"\*(.*?)\*", r"\1", clean)
            clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", clean)  # links
            clean = re.sub(r"`([^`]+)`", r"\1", clean)  # inline code
            # Safety: ensure we have enough horizontal space
            self.set_x(self.l_margin)
            try:
                self.multi_cell(0, 5, sanitize(clean))
            except Exception:
                # If line is too long or margin is bad, force a fresh line
                self.ln(5)
                self.set_x(self.l_margin)
                self.multi_cell(0, 5, sanitize(clean[:200]))

        # Flush remaining table
        if table_rows:
            self._render_table(table_rows)

    def _render_table(self, rows: list[list[str]]):
        """Render a simple markdown table."""
        if not rows:
            return
        num_cols = max(len(r) for r in rows)
        col_width = (self.w - self.l_margin - self.r_margin) / max(num_cols, 1)

        self.ln(2)
        for i, row in enumerate(rows):
            # Pad short rows
            while len(row) < num_cols:
                row.append("")
            if i == 0:
                self.set_font("Helvetica", "B", 8)
            else:
                self.set_font("Helvetica", "", 8)
            for cell in row:
                cell_text = re.sub(r"\*\*(.*?)\*\*", r"\1", cell)
                cell_text = sanitize(cell_text)[:60]  # truncate long cells
                self.cell(col_width, 5, cell_text, border=1)
            self.ln()
        self.ln(3)
        self.set_font("Helvetica", "", 10)

    def add_figures_section(self):
        """Embed all PNG figures from the figures directory."""
        pngs = sorted(FIG_DIR.glob("*.png"))
        if not pngs:
            print("  WARNING: No figure PNGs found, skipping figures section")
            return

        self.add_page()
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Figures",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(5)

        for png in pngs:
            name = png.stem
            # Determine if this figure needs a [simulated] flag
            simulated_figs = {"fig6-ih-ib-scaling", "fig7-cross-vendor-heatmap",
                              "fig8-knowledge-judgment-divergence",
                              "figS5-provider-radar", "figS6-cbr-by-model"}
            flag = " [simulated -- awaits external validation]" if name in simulated_figs else ""

            # Check if we need a new page (leave room for image + caption)
            if self.get_y() > 200:
                self.add_page()

            self.set_font("Helvetica", "B", 10)
            caption = f"{name}{flag}"
            self.cell(0, 6, sanitize(caption),
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.ln(2)

            try:
                # Fit image to page width
                img_width = self.w - self.l_margin - self.r_margin - 10
                self.image(str(png), x=self.l_margin + 5, w=img_width)
                self.ln(8)
            except Exception as e:
                self.set_font("Helvetica", "I", 9)
                self.cell(0, 5, sanitize(f"[Figure {name} could not be embedded: {e}]"),
                          new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                self.ln(4)

            self.set_font("Helvetica", "", 10)


def main():
    print("Building NormEval v2.2-preliminary combined PDF...")
    print(f"  Source: {SOURCE_DIR}")
    print(f"  Figures: {FIG_DIR}")
    print(f"  Output: {OUT_PDF}")

    pdf = NormEvalPDF()

    # Title page
    pdf.title_page()

    # License page
    pdf.license_page()

    # Main sections
    for title, filename in SECTIONS:
        md_path = SOURCE_DIR / filename
        print(f"  Processing: {title} ({filename})")
        pdf.add_section(title, md_path)

    # Figures
    print("  Embedding figures...")
    pdf.add_figures_section()

    # Appendices separator
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.ln(60)
    pdf.cell(0, 10, "Appendices", align="C",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, "NormEval v2.2-preliminary", align="C",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Appendices
    for title, filename in APPENDICES:
        md_path = SOURCE_DIR / filename
        print(f"  Processing: {title} ({filename})")
        pdf.add_section(title, md_path)

    # Write PDF
    pdf.output(str(OUT_PDF))
    size_mb = OUT_PDF.stat().st_size / (1024 * 1024)
    print(f"\nDone! {OUT_PDF.name} ({size_mb:.2f} MB, {pdf.page_no()} pages)")


if __name__ == "__main__":
    main()
