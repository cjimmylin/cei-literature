#!/usr/bin/env python3
"""Generate a combined PDF of the entire NormEval Paper v2.

Converts all markdown sections to a single publication-style PDF using
markdown → HTML → fpdf2 pipeline. Embeds all figures inline.

Output: PAPER-v2/20260405-normeval-paper-v2.1.pdf
"""
from __future__ import annotations

import re
from pathlib import Path

import markdown
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# ── Paths ────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent  # NORM-ETHICS/
PAPER = BASE / "PAPER-v2"
FIGS = PAPER / "figures"
SUPP = PAPER / "supplement"

VERSION = "2.1"
DATE_PREFIX = "20260405"
OUT_NAME = f"{DATE_PREFIX}-normeval-paper-v{VERSION}.pdf"

# ── Section ordering (excluding introduction) ────────────────────────
MAIN_SECTIONS = [
    ("abstract-normeval-v2.md", "Abstract"),
    ("methods-normeval-v2.md", "3. Methods"),
    ("results-landscape-normeval-v2.md", "4.1–4.2 Results: Landscape Analysis"),
    ("results-trials-normeval-v2.md", "4.3–4.4 Results: Implementation Trials"),
    ("results-crossvendor-normeval-v2.md", "4.5–4.6 Results: Cross-Vendor Analysis"),
    ("discussion-normeval-v2.md", "5. Discussion"),
    ("limitations-normeval-v2.md", "6. Limitations"),
    ("conclusion-normeval-v2.md", "7. Conclusion"),
    ("references-normeval-v2.md", "References"),
]

SUPPLEMENT_SECTIONS = [
    ("appendix-A-feature-matrix.md", "Appendix A: Complete Feature Matrix"),
    ("appendix-B-scoring-methodology.md", "Appendix B: Scoring Methodology"),
    ("appendix-C-trials-T1-T5.md", "Appendix C: Per-Trial Results (T1–T5)"),
    ("appendix-D-trials-T6-T15.md", "Appendix D: Cross-Vendor Trial Results (T6–T15)"),
    ("appendix-E-excluded-benchmarks.md", "Appendix E: Excluded Benchmarks"),
    ("appendix-F-harness-matrix.md", "Appendix F: Harness Compatibility Matrix"),
    ("appendix-G-statistical-methods.md", "Appendix G: Statistical Methods"),
    ("appendix-H-care-ethics-prototype.md", "Appendix H: Care Ethics Prototype"),
    ("appendix-I-v2-features.md", "Appendix I: V2 Extended Features"),
    ("appendix-J-council-deliberation.md", "Appendix J: Council Deliberation"),
]

# Map of figure references to PNG files
FIGURE_FILES = {
    "Figure 1": "fig1-tradition-heatmap.png",
    "Figure 2": "fig2-framework-difficulty.png",
    "Figure 3": "fig3-nd-vs-pe-scatter.png",
    "Figure 4": "fig4-data-availability.png",
    "Figure 5": "fig5-trial-accuracy-discriminative.png",
    "Figure 6": "fig6-ih-ib-scaling.png",
    "Figure 7": "fig7-cross-vendor-heatmap.png",
    "Figure 8": "fig8-knowledge-judgment-divergence.png",
    "Figure S1": "figS1-pca-clusters.png",
    "Figure S2": "figS2-temporal-trends.png",
    "Figure S5": "figS5-provider-radar.png",
    "Figure S6": "figS6-cbr-by-model.png",
}


UNICODE_FONT = "/Library/Fonts/Arial Unicode.ttf"
UNICODE_FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
UNICODE_FONT_ITALIC = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
UNICODE_FONT_BI = "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"


class NormEvalPDF(FPDF):
    """Custom PDF with header/footer and markdown rendering."""

    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=20)
        self.current_section = ""
        self.toc_entries: list[tuple[int, str, int]] = []  # (level, title, page)
        # Register Unicode font family
        self.add_font("ArialUni", "", UNICODE_FONT)
        self.add_font("ArialUni", "B", UNICODE_FONT_BOLD)
        self.add_font("ArialUni", "I", UNICODE_FONT_ITALIC)
        self.add_font("ArialUni", "BI", UNICODE_FONT_BI)

    def header(self):
        if self.page_no() <= 1:
            return
        self.set_font("ArialUni", "I", 7)
        self.set_text_color(128, 128, 128)
        title = "NormEval Paper v2.1 — Lin (2026)"
        self.cell(0, 6, title, align="L")
        self.cell(0, 6, self.current_section, align="R",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)
        self.set_text_color(0, 0, 0)

    def footer(self):
        self.set_y(-15)
        self.set_font("ArialUni", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")
        self.set_text_color(0, 0, 0)

    def add_toc_entry(self, level: int, title: str):
        self.toc_entries.append((level, title, self.page_no()))

    def render_toc(self):
        """Render table of contents."""
        self.add_page()
        self.current_section = "Table of Contents"
        self.set_font("ArialUni", "B", 14)
        self.cell(0, 10, "Table of Contents", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(5)

        for level, title, page in self.toc_entries:
            indent = (level - 1) * 8
            self.set_x(15 + indent)
            if level == 1:
                self.set_font("ArialUni", "B", 10)
            else:
                self.set_font("ArialUni", "", 9)
            # Title on left, page number on right
            title_w = 160 - indent
            self.cell(title_w, 6, title[:80])
            self.cell(20, 6, str(page), align="R",
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def clean_markdown(text: str) -> str:
    """Clean markdown for fpdf2 HTML rendering."""
    # Remove YAML frontmatter
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            text = text[end + 3:].strip()

    # Remove markdown image links (we'll embed figures separately)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)

    # Fix LaTeX-style escapes that break HTML
    text = text.replace("\\%", "%")
    text = text.replace("\\cite{", "[")
    text = re.sub(r"\\cite\{([^}]+)\}", r"[\1]", text)
    text = text.replace("\\newpage", "")

    # Convert > blockquotes to a styled format
    lines = text.split("\n")
    cleaned = []
    in_blockquote = False
    for line in lines:
        if line.startswith("> "):
            if not in_blockquote:
                cleaned.append('<blockquote style="color: #555; font-style: italic;">')
                in_blockquote = True
            cleaned.append(line[2:])
        else:
            if in_blockquote:
                cleaned.append("</blockquote>")
                in_blockquote = False
            cleaned.append(line)
    if in_blockquote:
        cleaned.append("</blockquote>")

    return "\n".join(cleaned)


def md_to_html(md_text: str) -> str:
    """Convert markdown to HTML with table support."""
    cleaned = clean_markdown(md_text)
    html = markdown.markdown(
        cleaned,
        extensions=["tables", "fenced_code", "nl2br"],
    )
    # Fix table styling for fpdf2
    html = html.replace("<table>",
                         '<table border="1" cellpadding="3" cellspacing="0" width="100%">')
    html = html.replace("<th>",
                         '<th bgcolor="#e8e8e8" align="left">')
    # Limit image widths
    html = re.sub(r'<img ([^>]*)>', r'<img \1 width="500">', html)
    return html


def embed_section_figures(pdf: NormEvalPDF, section_text: str):
    """Check if this section references figures and embed them at the end."""
    embedded = set()
    for fig_ref, fig_file in FIGURE_FILES.items():
        if fig_ref in section_text and fig_ref not in embedded:
            fig_path = FIGS / fig_file
            if fig_path.exists():
                pdf.ln(5)
                # Check if enough space, otherwise new page
                if pdf.get_y() > 200:
                    pdf.add_page()
                try:
                    # Use full width for tall figures, reduced for others
                    if "heatmap" in fig_file and "tradition" in fig_file:
                        pdf.image(str(fig_path), x=30, w=150)
                    else:
                        pdf.image(str(fig_path), x=15, w=180)
                except Exception as e:
                    pdf.set_font("ArialUni", "I", 8)
                    pdf.cell(0, 6, f"[{fig_ref}: {fig_file} — could not embed: {e}]",
                             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.ln(3)
                pdf.set_font("ArialUni", "I", 8)
                pdf.set_text_color(100, 100, 100)
                pdf.cell(0, 5, f"{fig_ref}: {fig_file.replace('.png', '').replace('-', ' ').title()}",
                         align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.set_text_color(0, 0, 0)
                pdf.ln(5)
                embedded.add(fig_ref)


def render_section(pdf: NormEvalPDF, md_path: Path, section_title: str, toc_level: int = 1):
    """Render a markdown file as a PDF section."""
    if not md_path.exists():
        print(f"  SKIP: {md_path.name} (not found)")
        return

    text = md_path.read_text(encoding="utf-8")
    html = md_to_html(text)

    pdf.add_page()
    pdf.current_section = section_title
    pdf.add_toc_entry(toc_level, section_title)

    # Section header
    pdf.set_font("ArialUni", "B", 14)
    pdf.cell(0, 10, section_title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    # Render HTML content
    pdf.set_font("ArialUni", size=9)
    try:
        pdf.write_html(html)
    except Exception as e:
        # Fallback: render as plain text
        pdf.set_font("ArialUni", size=9)
        plain = re.sub(r"<[^>]+>", "", html)
        for para in plain.split("\n\n"):
            para = para.strip()
            if para:
                pdf.multi_cell(0, 4.5, para)
                pdf.ln(2)

    # Embed referenced figures after the section text
    embed_section_figures(pdf, text)


def build_title_page(pdf: NormEvalPDF):
    """Create the title page."""
    pdf.add_page()
    pdf.current_section = ""

    pdf.ln(30)
    pdf.set_font("ArialUni", "B", 18)
    pdf.multi_cell(0, 9, "Three Ethical Profiles, One Knowledge Ceiling", align="C")
    pdf.ln(3)
    pdf.set_font("ArialUni", "", 13)
    pdf.multi_cell(0, 7,
                   "A Meta-Evaluation of 54 Normative Ethics Benchmarks\n"
                   "Across Nine LLMs and Three Vendors",
                   align="C")

    pdf.ln(12)
    pdf.set_font("ArialUni", "B", 11)
    pdf.cell(0, 8, "Jimmy Lin", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("ArialUni", "", 10)
    pdf.cell(0, 7, "Center for Ethical Intelligence", align="C",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.ln(12)
    pdf.set_font("ArialUni", "", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, f"Version {VERSION}  |  {DATE_PREFIX[:4]}-{DATE_PREFIX[4:6]}-{DATE_PREFIX[6:8]}",
             align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 6, "NormEval Paper v2 — Combined Document",
             align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(0, 0, 0)

    # Composition note
    pdf.ln(15)
    pdf.set_font("ArialUni", "I", 8)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 4.5,
                   "This document contains the complete paper text (excluding introduction and "
                   "related work), all main body figures and tables, supplementary appendices A–J, "
                   "and supplementary figures. Generated from 21 markdown source files and 12 "
                   "publication-quality figures.",
                   align="C")
    pdf.set_text_color(0, 0, 0)

    # Stats box
    pdf.ln(10)
    pdf.set_fill_color(245, 245, 250)
    pdf.set_font("ArialUni", "", 8)
    stats = [
        "54 benchmarks  |  26-feature framework  |  4 axes",
        "15 trials  |  9 models  |  3 vendors  |  114 comparable items",
        "5 claims  |  7 cross-vendor findings  |  3 ethical profiles",
        "12-member interdisciplinary council  |  10 consensus recommendations",
        "24 gate-passing benchmarks  |  70 discriminating items",
    ]
    for s in stats:
        pdf.cell(0, 5, s, align="C", fill=True,
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def build_figures_gallery(pdf: NormEvalPDF, title: str, fig_prefix: str, is_supp: bool = False):
    """Add a gallery page with all figures of a given type."""
    toc_level = 2 if is_supp else 1
    pdf.add_page()
    pdf.current_section = title
    pdf.add_toc_entry(toc_level, title)
    pdf.set_font("ArialUni", "B", 14)
    pdf.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    pattern = f"{fig_prefix}*.png"
    fig_files = sorted(FIGS.glob(pattern))
    for f in fig_files:
        if pdf.get_y() > 180:
            pdf.add_page()
        pdf.set_font("ArialUni", "B", 9)
        caption = f.stem.replace("-", " ").replace("fig", "Figure ").replace("S", "S")
        pdf.cell(0, 6, caption, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        try:
            if "tradition-heatmap" in f.name:
                pdf.image(str(f), x=30, w=150)
            else:
                pdf.image(str(f), x=15, w=180)
        except Exception as e:
            pdf.set_font("ArialUni", "I", 8)
            pdf.cell(0, 6, f"[Could not embed: {e}]",
                     new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)


def main():
    print(f"Building combined PDF: {OUT_NAME}")
    print(f"  Version: {VERSION}")
    print(f"  Date: {DATE_PREFIX}")

    pdf = NormEvalPDF()

    # ── Title page ───────────────────────────────────────────────
    print("\n  Title page...")
    build_title_page(pdf)

    # Placeholder for TOC (we'll insert it after we know all pages)
    toc_page_placeholder = pdf.page_no() + 1

    # ── Main body sections ───────────────────────────────────────
    print("\n  Main body sections:")
    for filename, title in MAIN_SECTIONS:
        md_path = PAPER / filename
        print(f"    {title}...")
        render_section(pdf, md_path, title, toc_level=1)

    # ── Main body figures gallery ────────────────────────────────
    print("\n  Main body figures gallery...")
    build_figures_gallery(pdf, "Main Body Figures (Gallery)", "fig[0-9]")

    # ── Supplementary divider ────────────────────────────────────
    pdf.add_page()
    pdf.current_section = "Supplementary Materials"
    pdf.add_toc_entry(1, "Supplementary Materials")
    pdf.ln(40)
    pdf.set_font("ArialUni", "B", 20)
    pdf.cell(0, 15, "Supplementary Materials", align="C",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("ArialUni", "", 11)
    pdf.ln(8)
    pdf.cell(0, 8, "Appendices A through J", align="C",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, "Supplementary Figures S1–S6", align="C",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # ── Supplementary sections ───────────────────────────────────
    print("\n  Supplementary sections:")
    for filename, title in SUPPLEMENT_SECTIONS:
        md_path = SUPP / filename
        print(f"    {title}...")
        render_section(pdf, md_path, title, toc_level=2)

    # ── Supplementary figures gallery ────────────────────────────
    print("\n  Supplementary figures gallery...")
    build_figures_gallery(pdf, "Supplementary Figures (Gallery)", "figS", is_supp=True)

    # ── Output ───────────────────────────────────────────────────
    out_path = PAPER / OUT_NAME
    pdf.output(str(out_path))
    print(f"\n  Output: {out_path}")
    print(f"  Pages: {pdf.page_no()}")
    print(f"  Size: {out_path.stat().st_size / 1024 / 1024:.1f} MB")
    print("\nDone!")


if __name__ == "__main__":
    main()
