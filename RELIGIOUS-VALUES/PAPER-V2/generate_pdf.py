#!/usr/bin/env python3
"""Generate tables-and-figures.pdf and supp-tables-and-figures.pdf for Paper v2.

Uses fpdf2 to create publication-quality PDFs with tables and embedded figures.
"""
from __future__ import annotations

import os
import sys

from fpdf import FPDF

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(SCRIPT_DIR, "figures")
EXISTING_FIGS = os.path.join(os.path.dirname(SCRIPT_DIR), "PAPER", "figures")
PRISMA_FIG = os.path.join(os.path.dirname(SCRIPT_DIR), "PAPER", "fig-prisma-flow.png")


def sanitize(text: str) -> str:
    """Replace Unicode chars unsupported by latin-1 core fonts."""
    return (text
            .replace("\u2014", "--")   # em dash
            .replace("\u2013", "-")    # en dash
            .replace("\u2018", "'")    # left single quote
            .replace("\u2019", "'")    # right single quote
            .replace("\u201c", '"')    # left double quote
            .replace("\u201d", '"')    # right double quote
            .replace("\u2026", "...")  # ellipsis
            .replace("\u00d7", "x")    # multiplication sign
            .replace("\u2265", ">=")   # >=
            .replace("\u2264", "<=")   # <=
            .replace("\u03c7", "chi")  # chi
            .replace("\u03c4", "tau")  # tau
            )


class PaperPDF(FPDF):
    """Custom PDF class with consistent header/footer styling."""

    def __init__(self, title: str):
        super().__init__(orientation="P", unit="mm", format="A4")
        self._title = sanitize(title)
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 6, self._title, align="L")
        self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title: str):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, sanitize(title), new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def subsection_title(self, title: str):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, sanitize(title), new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text: str):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 4.5, sanitize(text))
        self.ln(2)

    def add_table(self, headers: list[str], rows: list[list[str]],
                  col_widths: list[float] | None = None,
                  font_size: int = 8):
        """Add a formatted table."""
        if col_widths is None:
            w = (self.w - 20) / len(headers)
            col_widths = [w] * len(headers)

        # Header
        self.set_font("Helvetica", "B", font_size)
        self.set_fill_color(60, 60, 80)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 6, sanitize(h), border=1, fill=True, align="C")
        self.ln()

        # Rows
        self.set_font("Helvetica", "", font_size)
        self.set_text_color(0, 0, 0)
        for r_idx, row in enumerate(rows):
            if r_idx % 2 == 0:
                self.set_fill_color(240, 240, 245)
            else:
                self.set_fill_color(255, 255, 255)
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 5, sanitize(str(cell)), border=1,
                          fill=True, align="C" if i > 0 else "L")
            self.ln()
        self.ln(3)

    def add_figure(self, path: str, caption: str, max_width: float = 170):
        """Add a figure with caption, centered."""
        if not os.path.exists(path):
            self.body_text(f"[Figure not found: {os.path.basename(path)}]")
            return

        # Check if we need a new page
        if self.get_y() > 180:
            self.add_page()

        x = (self.w - max_width) / 2
        self.image(path, x=x, w=max_width)
        self.ln(2)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(80, 80, 80)
        self.multi_cell(0, 4, sanitize(caption), align="C")
        self.set_text_color(0, 0, 0)
        self.ln(4)


# ── Main Tables and Figures PDF ──────────────────────────────────────

def build_main_pdf():
    pdf = PaperPDF("Religious Values Benchmarks — Tables and Figures")
    pdf.alias_nb_pages()
    pdf.add_page()

    # Title page
    pdf.set_font("Helvetica", "B", 18)
    pdf.ln(30)
    pdf.multi_cell(0, 10, sanitize("Tables and Figures"), align="C")
    pdf.ln(5)
    pdf.set_font("Helvetica", "", 12)
    pdf.multi_cell(0, 7,
        "What Do Religious Values Benchmarks Actually Test?\n"
        "A Systematic Meta-Evaluation of LLM Religious Alignment Assessments",
        align="C")
    pdf.ln(5)
    pdf.set_font("Helvetica", "I", 10)
    pdf.cell(0, 6, "Jimmy Lin, Center for Ethical Intelligence", align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(0, 6, "Paper v2 | Generated 2026-04-05", align="C")

    # ── Table 1: 3-Axis Scoring Framework ──
    pdf.add_page()
    pdf.section_title("Table 1: 3-Axis Scoring Framework")
    pdf.body_text(
        "22 features across Religious/Theological Depth (RD), Practical Ease (PE), "
        "and Citation Impact (CI). Weight indicates contribution to axis composite."
    )
    headers = ["Axis", "ID", "Feature", "Scale", "Weight"]
    widths = [15, 12, 45, 40, 15]
    rows = [
        ["RD", "R1", "Tradition Count", "1-14", "15"],
        ["RD", "R2", "Theological Depth", "1-5 ordinal", "25"],
        ["RD", "R3", "Scriptural Grounding", "0-5", "15"],
        ["RD", "R4", "Denom. Awareness", "0-3", "10"],
        ["RD", "R5", "Pluralistic Coverage", "0-5", "15"],
        ["RD", "R6", "Expert Validation", "0-5", "20"],
        ["PE", "P1", "Task Format", "12 codes", "--"],
        ["PE", "P2", "Dataset Size", "count", "--"],
        ["PE", "P3", "Data Availability", "categorical", "25"],
        ["PE", "P4", "Code Availability", "categorical", "10"],
        ["PE", "P5", "License Terms", "categorical", "10"],
        ["PE", "P7", "Implementability", "0-10", "30"],
        ["PE", "P8", "Scorer Type", "categorical", "--"],
        ["PE", "P9", "Model Compatibility", "categorical", "15"],
        ["PE", "P10", "Language Coverage", "categorical", "10"],
        ["CI", "C1", "Raw Citations", "count", "--"],
        ["CI", "C2", "Citations/Year", "float", "30"],
        ["CI", "C3", "Venue Tier", "categorical", "20"],
        ["CI", "C4", "Downstream Adoption", "count", "25"],
        ["CI", "C5", "Leaderboard Presence", "boolean", "10"],
        ["CI", "C6", "Community Engagement", "boolean", "15"],
    ]
    pdf.add_table(headers, rows, widths)

    # ── Table 3: Tradition Coverage ──
    pdf.add_page()
    pdf.section_title("Table 3: 14-Tradition Coverage Analysis")
    pdf.body_text(
        "Status: STRONG (>20 gate-passers), MODERATE (2-10), WEAK (1-2), "
        "CRITICAL GAP (candidates but 0 gate-passers), VOID (0 or near-0)."
    )
    headers = ["Tradition", "Family", "Cands", "GP", "T1", "Status"]
    widths = [35, 30, 15, 12, 12, 28]
    rows = [
        ["Islam", "Abrahamic", "113", "28", "8", "STRONG"],
        ["Christianity", "Abrahamic", "117", "6", "0", "MODERATE"],
        ["Judaism", "Abrahamic", "25", "0", "0", "CRIT. GAP"],
        ["Hinduism", "Dharmic", "43", "5", "1", "MODERATE"],
        ["Buddhism", "Dharmic", "31", "3", "1", "MODERATE"],
        ["Jainism", "Dharmic", "59", "0", "0", "CRIT. GAP"],
        ["Sikhism", "Dharmic", "9", "2", "0", "WEAK"],
        ["Confucianism", "East Asian", "25", "1", "0", "WEAK"],
        ["Taoism", "East Asian", "4", "0", "0", "VOID"],
        ["Shinto", "East Asian", "2", "0", "0", "VOID"],
        ["Ubuntu Phil.", "Afr./Indig.", "5", "0", "0", "VOID"],
        ["Indigenous Sp.", "Afr./Indig.", "18", "0", "0", "VOID"],
        ["Baha'i", "Other", "0", "0", "0", "VOID"],
        ["Zoroastrianism", "Other", "4", "0", "0", "VOID"],
    ]
    pdf.add_table(headers, rows, widths)

    # ── Table 4: Claim Robustness ──
    pdf.add_page()
    pdf.section_title("Table 4: Claim Robustness Summary (8 Claims)")
    headers = ["#", "Claim", "Test", "Stat", "p", "Effect", "Result"]
    widths = [8, 40, 28, 18, 16, 16, 18]
    rows = [
        ["C1", "Tradition asymmetry", "Chi-squared", "64.96", "<.001", "V=0.53", "YES"],
        ["C2", "K-R conflation", "Binomial", "13/47", ".0015", "--", "YES"],
        ["C3", "Data bottleneck", "Binomial", "47/47", "<.001", "--", "YES"],
        ["C4", "Struct. injustice", "Logistic reg.", "R2=.068", ".112", "--", "REVISED"],
        ["C5", "Field recency", "Binomial", "28/47", ".121", "--", "MARGINAL"],
        ["C6", "WEIRD bias", "Fisher exact", "OR=0.58", ".090", "--", "REVISED"],
        ["C7", "Bias-values", "Binomial", "10/23", ".678", "--", "REVISED"],
        ["C8", "Values relevance", "One-sample t", "t=-4.93", "<.001", "d=-1.23", "YES"],
    ]
    pdf.add_table(headers, rows, widths, font_size=7)

    # ── Table 5: Cross-Model Construct Validity ──
    pdf.section_title("Table 5: Cross-Model Response Length Gradient")
    headers = ["Model", "K (chars)", "R (chars)", "V (chars)", "V/K", "Gradient?"]
    widths = [25, 25, 25, 25, 18, 20]
    rows = [
        ["Opus", "1,853", "4,586", "6,327", "3.41x", "YES"],
        ["Sonnet", "1,771", "5,194", "6,364", "3.59x", "YES"],
        ["Haiku", "766", "3,354", "7,026", "9.18x", "YES"],
    ]
    pdf.add_table(headers, rows, widths)

    # ── Table 6: Cross-Vendor Overview ──
    pdf.add_page()
    pdf.section_title("Table 6: Cross-Vendor Performance Overview (9 Models)")
    pdf.body_text(
        "Caveat: T2 blinding asymmetry, same-vendor scorer bias, and Gemini "
        "backfilled data provenance limit cross-vendor comparability (see Section 3.5)."
    )
    headers = ["Model", "Vendor", "Grad?", "V/K", "Rub.V", "T2%", "BV r"]
    widths = [25, 22, 14, 14, 14, 14, 14]
    rows = [
        ["Opus", "Anthropic", "YES", "3.41", "0.93", "100", "0.71"],
        ["Sonnet", "Anthropic", "YES", "3.59", "1.00", "100", "0.29"],
        ["Haiku", "Anthropic", "YES", "9.18", "1.00", "76.7", "0.70"],
        ["GPT-Codex", "OpenAI", "NO", "5.63", "0.87", "100", "0.30"],
        ["Codex-Mini", "OpenAI", "YES", "5.33", "0.90", "86.7", "0.08"],
        ["Gem-FL", "Gemini", "NO", "1.60", "0.20", "20.0", "1.00"],
        ["Gem-Flash", "Gemini", "NO", "1.11", "0.00", "10.0", "1.00"],
        ["Gem-Pro", "Gemini", "NO", "1.06", "0.00", "6.7", "1.00"],
        ["Gem-3.1P", "Gemini", "NO", "1.03", "0.00", "10.0", "1.00"],
    ]
    pdf.add_table(headers, rows, widths, font_size=7)

    # ── Figures ──
    pdf.add_page()
    pdf.section_title("Figures")

    # Existing figures (1-4)
    for num, fname, cap in [
        (1, "fig1-tradition-heatmap.png",
         "Figure 1: Tradition coverage heatmap across 14 traditions."),
        (2, "fig2-tradition-distribution.png",
         "Figure 2: Candidate distribution by tradition family (401 total)."),
        (3, "fig3-rd-vs-pe-scatter.png",
         "Figure 3: RD vs. PE scatter plot. Bubble size = log(citations)."),
        (4, "fig4-data-availability.png",
         "Figure 4: Data availability by tradition (available vs. unavailable)."),
    ]:
        path = os.path.join(EXISTING_FIGS, fname)
        pdf.add_figure(path, cap, max_width=150)

    # Existing figures (5-9)
    for num, fname, cap in [
        (5, "fig5-bootstrap-ci-forest.png",
         "Figure 5: Bootstrap CI forest plot for all gate-passing benchmarks."),
        (6, "fig6-void-factor-radar.png",
         "Figure 6: Void factor analysis for 8 missing traditions."),
        (7, "fig7-values-relevance-histogram.png",
         "Figure 7: A3 values relevance score distribution (Claim 8)."),
        (8, "fig8-claim-robustness.png",
         "Figure 8: Claim robustness summary (4 supported, 1 marginal, 3 revised)."),
        (9, "fig9-gate-threshold-sensitivity.png",
         "Figure 9: Gate threshold sensitivity curves."),
    ]:
        path = os.path.join(EXISTING_FIGS, fname)
        pdf.add_figure(path, cap, max_width=150)

    # New figures (10-13)
    for num, fname, cap in [
        (10, "fig10-cross-model-gradient.png",
         "Figure 10: K < R < V response length gradient (Claude family)."),
        (11, "fig11-rubric-heatmap.png",
         "Figure 11: Cross-vendor rubric scores (9 models x 4 dimensions)."),
        (12, "fig12-t2-accuracy.png",
         "Figure 12: T2 Islamic inheritance law accuracy (30 items, 9 models)."),
        (13, "fig13-vendor-radar.png",
         "Figure 13: Vendor capability radar (normalized metrics)."),
    ]:
        path = os.path.join(FIGURES_DIR, fname)
        pdf.add_figure(path, cap, max_width=150)

    out = os.path.join(SCRIPT_DIR, "tables-and-figures.pdf")
    pdf.output(out)
    print(f"  Main PDF: {out} ({os.path.getsize(out) // 1024} KB)")


# ── Supplementary Tables and Figures PDF ─────────────────────────────

def build_supp_pdf():
    pdf = PaperPDF("Religious Values Benchmarks — Supplementary Materials")
    pdf.alias_nb_pages()
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 16)
    pdf.ln(30)
    pdf.multi_cell(0, 10, "Supplementary Tables and Figures", align="C")
    pdf.ln(5)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 7,
        "What Do Religious Values Benchmarks Actually Test?\n"
        "A Systematic Meta-Evaluation of LLM Religious Alignment Assessments",
        align="C")

    # ── Table S3: Format Taxonomy ──
    pdf.add_page()
    pdf.section_title("Table S3: Format Taxonomy (12 Codes)")
    headers = ["Code", "Name", "Harness"]
    widths = [15, 55, 20]
    rows = [
        ["MCQ", "Multiple Choice (A/B/C/D)", "High"],
        ["MRC", "Machine Reading Comprehension", "High"],
        ["BIN", "Binary Classification", "High"],
        ["TXT", "Text Classification", "High"],
        ["SHT", "Shared Task (train/dev/test)", "High"],
        ["SCN", "Scenario-based (dilemmas)", "Medium"],
        ["PSY", "Psychometric/Survey (Likert)", "Medium"],
        ["MIX", "Mixed Format", "Medium"],
        ["OPN", "Open-ended Generation", "Low"],
        ["MTN", "Multi-turn Dialogue", "Low"],
        ["RAG", "Retrieval-Augmented", "Low"],
        ["MUL", "Multimodal (visual+text)", "Low"],
    ]
    pdf.add_table(headers, rows, widths)

    # ── Table S6: Cross-Model Gradient ──
    pdf.section_title("Table S6: Cross-Model Response Length (All 9 Models)")
    headers = ["Model", "Vendor", "K", "R", "V", "V/K", "Grad?"]
    widths = [22, 20, 18, 18, 18, 14, 14]
    rows = [
        ["Opus", "Anthropic", "1,853", "4,586", "6,327", "3.41", "YES"],
        ["Sonnet", "Anthropic", "1,771", "5,194", "6,364", "3.59", "YES"],
        ["Haiku", "Anthropic", "766", "3,354", "7,026", "9.18", "YES"],
        ["GPT-Codex", "OpenAI", "82", "472", "461", "5.63", "NO"],
        ["Codex-Mini", "OpenAI", "78", "415", "416", "5.33", "YES*"],
        ["Gem-FL", "Gemini", "63", "104", "101", "1.60", "NO"],
        ["Gem-Flash", "Gemini", "201", "268", "222", "1.11", "NO"],
        ["Gem-Pro", "Gemini", "231", "305", "244", "1.06", "NO"],
        ["Gem-3.1P", "Gemini", "310", "328", "318", "1.03", "NO"],
    ]
    pdf.add_table(headers, rows, widths, font_size=7)
    pdf.body_text("*Codex-Mini: V (416) marginally exceeds R (415).")

    # ── Table S8: T2 by Model and Difficulty ──
    pdf.section_title("Table S8: T2 Arabic MCQ by Model and Difficulty")
    headers = ["Model", "Vendor", "Beginner", "Advanced", "Overall", "Delta"]
    widths = [22, 20, 22, 22, 22, 16]
    rows = [
        ["Opus", "Anthropic", "100%", "100%", "100%", "0"],
        ["Sonnet", "Anthropic", "100%", "100%", "100%", "0"],
        ["Haiku", "Anthropic", "80%", "73.3%", "76.7%", "-6.7pp"],
        ["GPT-Codex", "OpenAI", "100%", "100%", "100%", "0"],
        ["Codex-Mini", "OpenAI", "80%", "93.3%", "86.7%", "+13.3pp"],
        ["Gem-FL", "Gemini", "20%", "20%", "20%", "0"],
        ["Gem-Flash", "Gemini", "6.7%", "13.3%", "10%", "+6.7pp"],
        ["Gem-Pro", "Gemini", "0%", "13.3%", "6.7%", "+13.3pp"],
        ["Gem-3.1P", "Gemini", "13.3%", "6.7%", "10%", "-6.7pp"],
    ]
    pdf.add_table(headers, rows, widths, font_size=7)

    # ── Table S9: Claim Robustness Full ──
    pdf.add_page()
    pdf.section_title("Table S9: Claim Robustness Battery (Full Details)")
    headers = ["Claim", "Test", "n", "Stat", "p", "ES", "Result"]
    widths = [18, 26, 10, 18, 16, 18, 18]
    rows = [
        ["C1a", "Chi-sq (unif)", "47", "64.96", "<.001", "V=0.526", "YES"],
        ["C1b", "Chi-sq (prop)", "47", "21.84", ".0006", "V=0.305", "YES"],
        ["C2", "Binomial", "47", "k=13", ".0015", "--", "YES"],
        ["C3", "Binomial", "47", "k=47", "<.001", "--", "YES"],
        ["C4", "Logistic", "401", "R2=.068", ".112", "--", "REVISED"],
        ["C5", "Binomial", "47", "k=28", ".121", "--", "MARGINAL"],
        ["C6", "Fisher", "401", "OR=0.58", ".090", "--", "REVISED"],
        ["C7", "Binomial", "23", "k=10", ".678", "--", "REVISED"],
        ["C8a", "t-test", "16", "t=-4.93", ".0002", "d=-1.23", "YES"],
        ["C8b", "Wilcoxon", "16", "W=5.0", ".0006", "--", "YES"],
        ["C8c", "Binom(>=50)", "16", "k=3", ".011", "--", "YES"],
        ["C8d", "Binom(>=75)", "16", "k=0", ".00002", "--", "YES"],
    ]
    pdf.add_table(headers, rows, widths, font_size=7)

    # ── Table S10: Void Factors ──
    pdf.section_title("Table S10: Void Factor Analysis (8 Missing Traditions)")
    headers = ["Tradition", "Corpus", "NLP", "Tasks", "Formal.", "Obstacle"]
    widths = [28, 18, 18, 18, 18, 30]
    rows = [
        ["Judaism", "HIGH", "MOD", "NONE", "HIGH", "Coordination"],
        ["Jainism", "MOD", "LOW", "NONE", "MOD", "Coordination"],
        ["Taoism", "HIGH", "LOW", "NONE", "MOD", "Coordination"],
        ["Confucianism", "HIGH", "MOD", "NONE", "HIGH", "Coordination"],
        ["Shinto", "LOW", "LOW", "NONE", "LOW", "Exclusion"],
        ["Ubuntu Phil.", "LOW", "LOW", "NONE", "LOW", "Exclusion"],
        ["Indigenous Sp.", "LOW", "LOW", "NONE", "LOW", "Exclusion"],
        ["Baha'i", "MOD", "LOW", "NONE", "MOD", "Min. presence"],
        ["Zoroastrianism", "MOD", "LOW", "NONE", "MOD", "Min. presence"],
    ]
    pdf.add_table(headers, rows, widths, font_size=7)

    # ── Supplementary Figures ──
    pdf.add_page()
    pdf.section_title("Supplementary Figures")

    # PRISMA
    if os.path.exists(PRISMA_FIG):
        pdf.add_figure(PRISMA_FIG,
                       "Figure S1: PRISMA flow diagram (2,099 -> 401 -> 47 -> 45 -> 25).",
                       max_width=140)

    # Existing S3
    s3_path = os.path.join(EXISTING_FIGS, "fig-s3-correlation-heatmap.png")
    if os.path.exists(s3_path):
        pdf.add_figure(s3_path,
                       "Figure S3: Pairwise correlation heatmap of scoring features.",
                       max_width=140)

    # New supplementary figures
    for fname, cap in [
        ("fig-s4-tradition-gradient.png",
         "Figure S4: K < R < V gradient by tradition and model (3x3 small multiples)."),
        ("fig-s5-cross-vendor-length.png",
         "Figure S5: Cross-vendor response length comparison (log scale, 9 models)."),
        ("fig-s7-t2-beginner-advanced.png",
         "Figure S7: T2 beginner vs. advanced accuracy by model."),
        ("fig-s8-year-distribution.png",
         "Figure S8: Temporal distribution of 401 benchmark candidates."),
    ]:
        path = os.path.join(FIGURES_DIR, fname)
        pdf.add_figure(path, cap, max_width=150)

    out = os.path.join(SCRIPT_DIR, "supp-tables-and-figures.pdf")
    pdf.output(out)
    print(f"  Supp PDF: {out} ({os.path.getsize(out) // 1024} KB)")


if __name__ == "__main__":
    print("Generating PDFs...")
    build_main_pdf()
    build_supp_pdf()
    print("Done.")
