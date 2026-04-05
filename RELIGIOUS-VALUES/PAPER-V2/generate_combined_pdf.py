#!/usr/bin/env python3
"""Generate a single combined PDF of the Religious Values Benchmark Paper v2.

Renders all markdown sections (Abstract through Conclusion + Supplementary)
into one PDF with embedded figures, formatted tables, and section headers.
Output: 20260405-religious-values-paper-v2.pdf
"""
from __future__ import annotations

import os
import re
import textwrap

from fpdf import FPDF

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NEW_FIGS = os.path.join(SCRIPT_DIR, "figures")
OLD_FIGS = os.path.join(os.path.dirname(SCRIPT_DIR), "PAPER", "figures")
PRISMA = os.path.join(os.path.dirname(SCRIPT_DIR), "PAPER", "fig-prisma-flow.png")

VERSION = "v2"
DATE_PREFIX = "20260405"
OUTPUT_NAME = f"{DATE_PREFIX}-religious-values-paper-{VERSION}.pdf"


# ── Text sanitization ────────────────────────────────────────────────

def sanitize(text: str) -> str:
    """Replace chars unsupported by latin-1 core fonts."""
    replacements = {
        "\u2014": "--", "\u2013": "-", "\u2018": "'", "\u2019": "'",
        "\u201c": '"', "\u201d": '"', "\u2026": "...", "\u00d7": "x",
        "\u2265": ">=", "\u2264": "<=", "\u03c7": "chi", "\u03c4": "tau",
        "\u2192": "->", "\u00b2": "2", "\u2248": "~", "\u221e": "inf",
        "\u00b5": "u", "\u2260": "!=", "\u03b1": "alpha", "\u03b2": "beta",
        "\u00b0": "deg",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def strip_latex(text: str) -> str:
    """Convert LaTeX math notation to readable plain text."""
    # Specific common patterns first
    text = re.sub(r'\$\\chi\^2\$', 'chi-sq', text)
    text = re.sub(r'\$\\geq?\$', '>=', text)
    text = re.sub(r'\$\\leq?\$', '<=', text)
    text = re.sub(r'\$\\times\$', 'x', text)
    text = re.sub(r'\$\\rightarrow\$', '->', text)
    # LaTeX commands in braces
    text = re.sub(r'\\texttt\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\textit\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\textbf\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\cite\{([^}]*)\}', r'[\1]', text)
    # Strip $ delimiters (keep content inside)
    text = re.sub(r'\$([^$]+)\$', r'\1', text)
    # Post-dollar cleanup: remaining backslash commands
    text = text.replace('\\chi^2', 'chi-sq')
    text = text.replace('\\chi', 'chi')
    text = text.replace('\\tau', 'tau')
    text = text.replace('\\geq', '>=')
    text = text.replace('\\leq', '<=')
    text = text.replace('\\times', 'x')
    text = text.replace('\\rightarrow', '->')
    text = text.replace('\\approx', '~')
    text = text.replace('\\infty', 'inf')
    text = text.replace('\\alpha', 'alpha')
    text = text.replace('\\beta', 'beta')
    text = text.replace('\\mu', 'mu')
    text = text.replace('\\sigma', 'sigma')
    text = text.replace('\\lambda', 'lambda')
    text = re.sub(r'\^(\d)', r'^\1', text)  # keep superscripts readable
    text = re.sub(r'\^{([^}]*)}', r'^\1', text)
    text = re.sub(r'_\{([^}]*)\}', r'_\1', text)
    text = text.replace('\\%', '%')
    text = text.replace('\\&', '&')
    text = text.replace('\\#', '#')
    text = text.replace('\\\\', ' ')
    text = text.replace('\\ ', ' ')
    return text


def clean_line(text: str) -> str:
    """Full pipeline: strip markdown bold/italic, LaTeX, sanitize."""
    text = strip_latex(text)
    text = sanitize(text)
    # Convert markdown bold to plain (fpdf2 can't do inline bold easily)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = text.replace('---', '--')
    return text


# ── PDF class ────────────────────────────────────────────────────────

class CombinedPDF(FPDF):

    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=18)
        self._current_section = ""

    def header(self):
        if self.page_no() <= 1:
            return
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(140, 140, 140)
        title = sanitize("Religious Values Benchmarks -- Paper v2")
        self.cell(0, 5, title, align="L")
        if self._current_section:
            self.cell(0, 5, sanitize(self._current_section), align="R")
        self.ln(7)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(140, 140, 140)
        self.cell(0, 8, f"Page {self.page_no()}", align="C")

    def add_section_header(self, level: int, text: str):
        """Add a section/subsection header."""
        text = clean_line(text)
        if level == 1:
            self.add_page()
            self._current_section = text[:60]
            self.set_font("Helvetica", "B", 16)
            self.set_text_color(30, 30, 80)
        elif level == 2:
            if self.get_y() > 240:
                self.add_page()
            self.ln(4)
            self._current_section = text[:60]
            self.set_font("Helvetica", "B", 13)
            self.set_text_color(40, 40, 60)
        elif level == 3:
            if self.get_y() > 250:
                self.add_page()
            self.ln(3)
            self.set_font("Helvetica", "B", 11)
            self.set_text_color(60, 60, 80)
        else:
            self.ln(2)
            self.set_font("Helvetica", "BI", 10)
            self.set_text_color(80, 80, 100)

        self.multi_cell(0, 6, text)
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def add_paragraph(self, text: str):
        """Add a body paragraph."""
        text = clean_line(text)
        if not text.strip():
            return
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 4.2, text)
        self.ln(1.5)

    def add_bold_paragraph(self, label: str, text: str):
        """Add a paragraph starting with a bold label."""
        label = clean_line(label)
        text = clean_line(text)
        # Combine as single paragraph — bold inline not supported,
        # so prepend label in caps-style
        combined = f"{label} {text}"
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 4.2, combined)
        self.ln(1.5)

    def add_md_table(self, header_line: str, sep_line: str, rows: list[str]):
        """Render a markdown table."""
        # Parse columns
        headers = [c.strip() for c in header_line.strip().strip("|").split("|")]
        n_cols = len(headers)
        avail = self.w - 20

        # Smart column widths: give first column 1.5x share for names
        if n_cols <= 3:
            col_widths = [avail / n_cols] * n_cols
        else:
            first_w = avail * 1.5 / (n_cols + 0.5)
            rest_w = avail / (n_cols + 0.5)
            col_widths = [first_w] + [rest_w] * (n_cols - 1)

        # Try to fit: if too many columns, use smaller font
        font_size = 6 if n_cols > 8 else (7 if n_cols > 6 else 8)
        row_h = 4.5

        # Check if we need new page
        needed = (len(rows) + 1) * row_h + 10
        if self.get_y() + needed > 270:
            self.add_page()

        # Header
        self.set_font("Helvetica", "B", font_size)
        self.set_fill_color(50, 50, 70)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            h = sanitize(clean_line(h))
            if len(h) > 24:
                h = h[:23] + "."
            self.cell(col_widths[i], row_h, h, border=1, fill=True, align="C")
        self.ln()

        # Rows
        self.set_font("Helvetica", "", font_size)
        self.set_text_color(0, 0, 0)
        for r_idx, row_line in enumerate(rows):
            cells = [c.strip() for c in row_line.strip().strip("|").split("|")]
            # Pad or trim to match header count
            while len(cells) < n_cols:
                cells.append("")
            cells = cells[:n_cols]

            if r_idx % 2 == 0:
                self.set_fill_color(242, 242, 248)
            else:
                self.set_fill_color(255, 255, 255)

            for i, cell in enumerate(cells):
                cell = sanitize(clean_line(cell))
                max_len = 32 if i == 0 else 24
                if len(cell) > max_len:
                    cell = cell[:max_len - 1] + "."
                align = "L" if i == 0 else "C"
                self.cell(col_widths[i], row_h, cell, border=1, fill=True, align=align)
            self.ln()

            if self.get_y() > 272:
                self.add_page()
                # Re-draw header
                self.set_font("Helvetica", "B", font_size)
                self.set_fill_color(50, 50, 70)
                self.set_text_color(255, 255, 255)
                for i, h in enumerate(headers):
                    h = sanitize(clean_line(h))
                    if len(h) > 18:
                        h = h[:17] + "."
                    self.cell(col_widths[i], row_h, h, border=1, fill=True, align="C")
                self.ln()
                self.set_font("Helvetica", "", font_size)
                self.set_text_color(0, 0, 0)

        self.ln(3)

    def add_figure_image(self, path: str, caption: str = "", max_w: float = 160):
        """Embed a PNG figure."""
        if not os.path.exists(path):
            self.add_paragraph(f"[Figure not found: {os.path.basename(path)}]")
            return
        if self.get_y() > 160:
            self.add_page()
        x = (self.w - max_w) / 2
        self.image(path, x=x, w=max_w)
        if caption:
            self.ln(2)
            self.set_font("Helvetica", "I", 7.5)
            self.set_text_color(100, 100, 100)
            self.multi_cell(0, 3.5, sanitize(clean_line(caption)), align="C")
            self.set_text_color(0, 0, 0)
        self.ln(4)


# ── Markdown renderer ────────────────────────────────────────────────

# Map figure references to actual files
FIGURE_MAP = {
    "fig1-tradition-heatmap.png": os.path.join(OLD_FIGS, "fig1-tradition-heatmap.png"),
    "fig2-tradition-distribution.png": os.path.join(OLD_FIGS, "fig2-tradition-distribution.png"),
    "fig3-rd-vs-pe-scatter.png": os.path.join(OLD_FIGS, "fig3-rd-vs-pe-scatter.png"),
    "fig4-data-availability.png": os.path.join(OLD_FIGS, "fig4-data-availability.png"),
    "fig5-bootstrap-ci-forest.png": os.path.join(OLD_FIGS, "fig5-bootstrap-ci-forest.png"),
    "fig6-void-factor-radar.png": os.path.join(OLD_FIGS, "fig6-void-factor-radar.png"),
    "fig7-values-relevance-histogram.png": os.path.join(OLD_FIGS, "fig7-values-relevance-histogram.png"),
    "fig8-claim-robustness.png": os.path.join(OLD_FIGS, "fig8-claim-robustness.png"),
    "fig9-gate-threshold-sensitivity.png": os.path.join(OLD_FIGS, "fig9-gate-threshold-sensitivity.png"),
    "fig-s3-correlation-heatmap.png": os.path.join(OLD_FIGS, "fig-s3-correlation-heatmap.png"),
    "fig-prisma-flow.png": PRISMA,
    "fig10-cross-model-gradient.png": os.path.join(NEW_FIGS, "fig10-cross-model-gradient.png"),
    "fig11-rubric-heatmap.png": os.path.join(NEW_FIGS, "fig11-rubric-heatmap.png"),
    "fig12-t2-accuracy.png": os.path.join(NEW_FIGS, "fig12-t2-accuracy.png"),
    "fig13-vendor-radar.png": os.path.join(NEW_FIGS, "fig13-vendor-radar.png"),
    "fig-s4-tradition-gradient.png": os.path.join(NEW_FIGS, "fig-s4-tradition-gradient.png"),
    "fig-s5-cross-vendor-length.png": os.path.join(NEW_FIGS, "fig-s5-cross-vendor-length.png"),
    "fig-s7-t2-beginner-advanced.png": os.path.join(NEW_FIGS, "fig-s7-t2-beginner-advanced.png"),
    "fig-s8-year-distribution.png": os.path.join(NEW_FIGS, "fig-s8-year-distribution.png"),
}

# Figure insertion points (after specific section headers or keywords)
FIGURE_INSERTIONS = {
    "Figure 1": "fig1-tradition-heatmap.png",
    "Figure 2": "fig2-tradition-distribution.png",
    "Figure 3": "fig3-rd-vs-pe-scatter.png",
    "Figure 4": "fig4-data-availability.png",
    "Figure 5": "fig5-bootstrap-ci-forest.png",
    "Figure 6": "fig6-void-factor-radar.png",
    "Figure 7": "fig7-values-relevance-histogram.png",
    "Figure 8": "fig8-claim-robustness.png",
    "Figure 9": "fig9-gate-threshold-sensitivity.png",
    "Figure 10": "fig10-cross-model-gradient.png",
    "Figure 11": "fig11-rubric-heatmap.png",
    "Figure 12": "fig12-t2-accuracy.png",
    "Figure 13": "fig13-vendor-radar.png",
    "Figure S1": "fig-prisma-flow.png",
    "Figure S3": "fig-s3-correlation-heatmap.png",
    "Figure S4": "fig-s4-tradition-gradient.png",
    "Figure S5": "fig-s5-cross-vendor-length.png",
    "Figure S7": "fig-s7-t2-beginner-advanced.png",
    "Figure S8": "fig-s8-year-distribution.png",
}


def render_markdown(pdf: CombinedPDF, md_path: str):
    """Render a markdown file to the PDF."""
    with open(md_path, "r") as f:
        lines = f.readlines()

    i = 0
    inserted_figures = set()

    while i < len(lines):
        line = lines[i].rstrip("\n")

        # Skip markdown image links (![...](...)
        if line.strip().startswith("!["):
            i += 1
            continue

        # Headers
        if line.startswith("####"):
            text = line.lstrip("#").strip()
            pdf.add_section_header(4, text)
            i += 1
            continue
        if line.startswith("###"):
            text = line.lstrip("#").strip()
            pdf.add_section_header(3, text)
            i += 1
            continue
        if line.startswith("##"):
            text = line.lstrip("#").strip()
            pdf.add_section_header(2, text)
            i += 1
            continue
        if line.startswith("#"):
            text = line.lstrip("#").strip()
            pdf.add_section_header(1, text)
            i += 1
            continue

        # Blockquote (used for formulas)
        if line.strip().startswith(">"):
            text = line.strip().lstrip(">").strip()
            pdf.set_font("Courier", "", 8)
            pdf.set_text_color(60, 60, 120)
            pdf.cell(10)  # indent
            pdf.multi_cell(0, 4, sanitize(strip_latex(text)))
            pdf.ln(2)
            pdf.set_text_color(0, 0, 0)
            i += 1
            continue

        # Table detection
        if "|" in line and i + 1 < len(lines) and re.match(r'\s*\|[\s\-:|]+\|', lines[i + 1]):
            header_line = line
            sep_line = lines[i + 1].rstrip("\n")
            table_rows = []
            j = i + 2
            while j < len(lines) and "|" in lines[j] and lines[j].strip():
                table_rows.append(lines[j].rstrip("\n"))
                j += 1
            pdf.add_md_table(header_line, sep_line, table_rows)
            i = j
            continue

        # Horizontal rule
        if re.match(r'^-{3,}$', line.strip()) or re.match(r'^\*{3,}$', line.strip()):
            pdf.ln(2)
            y = pdf.get_y()
            pdf.set_draw_color(180, 180, 180)
            pdf.line(15, y, pdf.w - 15, y)
            pdf.ln(3)
            i += 1
            continue

        # Empty line
        if not line.strip():
            pdf.ln(1)
            i += 1
            continue

        # Bold-lead paragraphs (e.g., **Stage 1: ...** text)
        bold_match = re.match(r'^\*\*([^*]+)\*\*\s*(.*)', line.strip())
        if bold_match:
            label = bold_match.group(1)
            rest = bold_match.group(2)
            # Gather continuation lines
            j = i + 1
            while j < len(lines) and lines[j].strip() and not lines[j].startswith("#") \
                    and not lines[j].startswith("|") and not lines[j].strip().startswith(">") \
                    and not lines[j].strip().startswith("- ") and not lines[j].strip().startswith("*"):
                rest += " " + lines[j].strip()
                j += 1
            pdf.add_bold_paragraph(label + ".", rest)

            # Check for figure references to insert
            for fig_label, fig_file in FIGURE_INSERTIONS.items():
                if fig_label in rest and fig_file not in inserted_figures:
                    path = FIGURE_MAP.get(fig_file)
                    if path and os.path.exists(path):
                        pdf.add_figure_image(path, fig_label, max_w=140)
                        inserted_figures.add(fig_file)

            i = j
            continue

        # List items
        if line.strip().startswith("- ") or line.strip().startswith("* "):
            text = line.strip().lstrip("-* ").strip()
            text = clean_line(text)
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(30, 30, 30)
            x = pdf.get_x()
            pdf.cell(8)
            pdf.cell(4, 4.2, sanitize("*"))
            pdf.multi_cell(0, 4.2, text)
            pdf.ln(0.5)
            i += 1
            continue

        # Numbered list
        num_match = re.match(r'^(\d+)\.\s+(.*)', line.strip())
        if num_match:
            num = num_match.group(1)
            text = clean_line(num_match.group(2))
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(30, 30, 30)
            pdf.cell(8)
            pdf.cell(6, 4.2, f"{num}.")
            pdf.multi_cell(0, 4.2, text)
            pdf.ln(0.5)
            i += 1
            continue

        # Regular paragraph — gather continuation lines
        paragraph = line.strip()
        j = i + 1
        while j < len(lines) and lines[j].strip() and not lines[j].startswith("#") \
                and not lines[j].startswith("|") and not lines[j].strip().startswith(">") \
                and not lines[j].strip().startswith("- ") \
                and not lines[j].strip().startswith("* ") \
                and not re.match(r'^\d+\.\s', lines[j].strip()) \
                and not lines[j].strip().startswith("!["):
            paragraph += " " + lines[j].strip()
            j += 1
        pdf.add_paragraph(paragraph)

        # Check for inline figure references
        for fig_label, fig_file in FIGURE_INSERTIONS.items():
            if fig_label in paragraph and fig_file not in inserted_figures:
                # Only insert if it's a clear reference like "(Figure 1)" or "Figure 1 presents"
                if re.search(rf'\b{re.escape(fig_label)}\b', paragraph):
                    path = FIGURE_MAP.get(fig_file)
                    if path and os.path.exists(path):
                        pdf.add_figure_image(path, fig_label, max_w=140)
                        inserted_figures.add(fig_file)

        i = j


# ── Build combined PDF ───────────────────────────────────────────────

def build():
    pdf = CombinedPDF()

    # ── Title page ──
    pdf.add_page()
    pdf.ln(40)
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(30, 30, 80)
    pdf.multi_cell(0, 10, sanitize(
        "What Do Religious Values Benchmarks\nActually Test?"
    ), align="C")
    pdf.ln(5)
    pdf.set_font("Helvetica", "", 13)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 7, sanitize(
        "A Systematic Meta-Evaluation of\n"
        "LLM Religious Alignment Assessments"
    ), align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, "Jimmy Lin", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "I", 10)
    pdf.cell(0, 6, "Center for Ethical Intelligence", align="C",
             new_x="LMARGIN", new_y="NEXT")
    pdf.ln(15)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 6, f"Paper {VERSION} | {DATE_PREFIX} | Sections 3-6 + Supplementary",
             align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6,
             "Note: Sections 1 (Introduction) and 2 (Related Work) are not included in this version.",
             align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)

    # Council info
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 4, sanitize(
        "Written under the guidance of a 12-member expert writing council "
        "spanning Islamic ethics, comparative religion, psychometrics, "
        "benchmark design, decolonial studies, cross-cultural NLP, "
        "science communication, statistics, philosophy of AI, "
        "Indigenous data governance, academic publishing, and Dharmic philosophy."
    ), align="C")

    # ── Main body sections ──
    sections = [
        ("00-abstract.md", "Abstract"),
        ("01-methods.md", "3. Methods"),
        ("02-results.md", "4. Results"),
        ("03-discussion.md", "5. Discussion"),
        ("04-conclusion.md", "6. Conclusion"),
    ]

    for filename, label in sections:
        path = os.path.join(SCRIPT_DIR, filename)
        if os.path.exists(path):
            print(f"  Rendering {filename}...")
            render_markdown(pdf, path)
        else:
            print(f"  SKIP (not found): {filename}")

    # ── Supplementary divider ──
    pdf.add_page()
    pdf.ln(50)
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(30, 30, 80)
    pdf.multi_cell(0, 10, "Supplementary Materials", align="C")
    pdf.ln(5)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 7, sanitize(
        "Supplementary Methods, Results, Tables, and Figures\n"
        "for the Religious Values Benchmark Paper v2"
    ), align="C")

    # ── Supplementary sections ──
    supp_sections = [
        ("05-supp-methods.md", "Supplementary Methods"),
        ("06-supp-results.md", "Supplementary Results"),
        ("07-supp-tables.md", "Supplementary Tables"),
        ("08-supp-figures.md", "Supplementary Figures"),
    ]

    for filename, label in supp_sections:
        path = os.path.join(SCRIPT_DIR, filename)
        if os.path.exists(path):
            print(f"  Rendering {filename}...")
            render_markdown(pdf, path)
        else:
            print(f"  SKIP (not found): {filename}")

    # ── Output ──
    out_path = os.path.join(SCRIPT_DIR, OUTPUT_NAME)
    pdf.output(out_path)
    size_kb = os.path.getsize(out_path) // 1024
    print(f"\n  Combined PDF: {out_path}")
    print(f"  Size: {size_kb} KB ({pdf.page_no()} pages)")


if __name__ == "__main__":
    print(f"Generating combined PDF: {OUTPUT_NAME}")
    build()
    print("Done.")
