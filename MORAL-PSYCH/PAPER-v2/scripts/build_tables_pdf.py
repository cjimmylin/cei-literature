#!/usr/bin/env python3
"""Generate standalone PDF tables for MPBench Paper v2.

Uses fpdf2 to render each table as a clean, single-page (or multi-page) PDF.
Tables are written to ../tables-pdf/

Usage:
    cd CEI-Lit-WS/MORAL-PSYCH/PAPER-v2/scripts
    ../../.venv/bin/python build_tables_pdf.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# Add venv to path
SCRIPT_DIR = Path(__file__).resolve().parent
PAPER_DIR = SCRIPT_DIR.parent
TABLES_DIR = PAPER_DIR / "tables-pdf"
TABLES_DIR.mkdir(exist_ok=True)

from fpdf import FPDF


def sanitize(text: str) -> str:
    """Replace Unicode chars that Helvetica can't render."""
    return (text
            .replace("\u2014", "--")   # em dash
            .replace("\u2013", "-")    # en dash
            .replace("\u2018", "'")    # left single quote
            .replace("\u2019", "'")    # right single quote
            .replace("\u201c", '"')    # left double quote
            .replace("\u201d", '"')    # right double quote
            .replace("\u2026", "...")  # ellipsis
            .replace("\u2265", ">=")   # >=
            .replace("\u2264", "<=")   # <=
            .replace("\u00d7", "x")    # multiplication sign
            .replace("\u2248", "~"))   # approximately


class TablePDF(FPDF):
    """Custom PDF class for academic tables."""

    def __init__(self, title: str = "", landscape: bool = False):
        orientation = "L" if landscape else "P"
        super().__init__(orientation=orientation, unit="mm", format="letter")
        self.table_title = title
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 8, sanitize(self.table_title), align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, sanitize(f"MPBench Paper v2 -- {self.table_title}"), align="C")

    def add_table(self, headers: list[str], rows: list[list[str]],
                  col_widths: list[float] | None = None,
                  header_bg: tuple = (41, 65, 122),
                  alt_row_bg: tuple = (240, 240, 248)):
        """Render a table with header row and alternating row colors."""
        self.add_page()

        avail_width = self.w - self.l_margin - self.r_margin
        if col_widths is None:
            col_widths = [avail_width / len(headers)] * len(headers)

        # Header row
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(*header_bg)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, sanitize(h), border=1, fill=True, align="C")
        self.ln()

        # Data rows
        self.set_font("Helvetica", "", 8)
        self.set_text_color(0, 0, 0)
        for row_idx, row in enumerate(rows):
            if row_idx % 2 == 1:
                self.set_fill_color(*alt_row_bg)
                fill = True
            else:
                fill = False

            max_h = 7
            # Calculate row height for wrapping
            for i, cell_text in enumerate(row):
                lines = self.multi_cell(col_widths[i], 5, sanitize(cell_text),
                                        dry_run=True, output="LINES")
                cell_h = len(lines) * 5
                if cell_h > max_h:
                    max_h = cell_h

            x_start = self.get_x()
            y_start = self.get_y()

            for i, cell_text in enumerate(row):
                self.set_xy(x_start + sum(col_widths[:i]), y_start)
                self.multi_cell(col_widths[i], 5, sanitize(cell_text), border=1,
                                fill=fill, align="L", max_line_height=5)

            self.set_xy(x_start, y_start + max_h)
            # Ensure we move to next line
            if self.get_y() <= y_start:
                self.set_y(y_start + max_h)


def build_table_1():
    """T1: Dual Expert Council Composition."""
    pdf = TablePDF("Table 1: Dual Expert Council Composition", landscape=True)
    headers = ["Council", "ID", "Role", "Expertise", "Key Responsibility"]
    rows = [
        ["A (Meta-Eval)", "A1", "Narrative Architect", "Rhetorical structure, journal conventions", "Story arc, abstract, transitions"],
        ["A (Meta-Eval)", "A2", "Moral Psych Historian", "Intellectual genealogy, theory taxonomy", "Theory overview, synthesis"],
        ["A (Meta-Eval)", "A3", "MFT Deep Expert", "MFQ, MFTC, computational MFT", "MFT dominance analysis"],
        ["A (Meta-Eval)", "A4", "Process Theories Spec.", "Dual Process, Social Intuitionism", "Missing theory gaps"],
        ["A (Meta-Eval)", "A5", "Psychometric Authority", "Messick validity, measurement invariance", "Construct validity gap"],
        ["A (Meta-Eval)", "A6", "Cross-Cultural Expert", "WEIRD critique, Schwartz, Dyadic", "Cultural implications"],
        ["A (Meta-Eval)", "A7", "Benchmark Surveyor", "BIG-bench, HELM, ETHICS", "Positioning"],
        ["A (Meta-Eval)", "A8", "Format Specialist", "Likert, forced-choice, response bias", "Format mismatch analysis"],
        ["A (Meta-Eval)", "A9", "NLP/Eval Specialist", "Harness compatibility, scorer design", "Pipeline methodology"],
        ["A (Meta-Eval)", "A10", "Bibliometrician", "Citation analysis, venue tiers", "Citation maturity confound"],
        ["A (Meta-Eval)", "A11", "Survey Methodologist", "Systematic review, PRISMA standards", "Search protocol rigor"],
        ["A (Meta-Eval)", "A12", "Meta-Science Critic", "Replication crisis, QRPs, open science", "Limitations, meta-critique"],
        ["B (Empirical)", "B1", "Cross-Vendor Analyst", "Variance decomposition, convergence", "Homogeneity finding"],
        ["B (Empirical)", "B2", "RLHF/Alignment Expert", "Constitutional AI, RLHF, DPO", "RLHF fingerprints"],
        ["B (Empirical)", "B3", "AI Safety Researcher", "Value monoculture, audit strategies", "Safety implications"],
        ["B (Empirical)", "B4", "Scale Sensitivity Analyst", "Scaling laws, emergent capabilities", "DIT non-linearity"],
        ["B (Empirical)", "B5", "Cross-Cultural Psych", "Hofstede, cultural persona validity", "WEIRD convergence critique"],
        ["B (Empirical)", "B6", "Dual-Process Cog Sci", "System 1/2, CoT as deliberation", "Haiku CoT effect"],
        ["B (Empirical)", "B7", "Psychometrician (Emp)", "Ceiling/floor effects, discrimination", "Benchmark fitness audit"],
        ["B (Empirical)", "B8", "Statistical Method.", "N=1 inference, bootstrap CIs", "Quantitative claims"],
        ["B (Empirical)", "B9", "Moral Philosophy", "Normative characterization, meta-ethics", "Philosophical framing"],
        ["B (Empirical)", "B10", "Policy & Governance", "Algorithmic auditing, regulation", "Policy recommendations"],
        ["B (Empirical)", "B11", "Developmental Psych", "Kohlberg, DIT applicability", "Developmental reframing"],
        ["B (Empirical)", "B12", "Phil. of Mind", "Functional moral agency, consciousness", "Interpretive constraints"],
    ]
    col_widths = [28, 10, 35, 60, 50]
    pdf.add_table(headers, rows, col_widths)
    pdf.output(str(TABLES_DIR / "table1-expert-council.pdf"))
    print("  T1: Expert Council Composition")


def build_table_2():
    """T2: Theory Representation Across the Pipeline."""
    pdf = TablePDF("Table 2: Theory Representation Across the Pipeline")
    headers = ["Theory", "Vault Detection", "Candidates (of 222)", "Top-15"]
    rows = [
        ["MFT", "101", "28 (MFT-primary)", "5"],
        ["Schwartz", "69", "11", "4"],
        ["Trolley", "58", "13", "5"],
        ["Kohlberg", "35", "11", "4"],
        ["Social Intuitionism", "18", "3", "0"],
        ["Moral Identity", "12", "1", "0"],
        ["Dual Process", "9", "3", "0"],
        ["Dyadic Morality", "7", "1", "1"],
    ]
    col_widths = [45, 40, 50, 30]
    pdf.add_table(headers, rows, col_widths)
    pdf.output(str(TABLES_DIR / "table2-theory-representation.pdf"))
    print("  T2: Theory Representation")


def build_table_3():
    """T3: Construct Validity Distribution."""
    pdf = TablePDF("Table 3: Construct Validity Distribution (A6 Scores)")
    headers = ["A6 Score", "Interpretation", "Count", "Percentage"]
    rows = [
        ["5", "Multi-study validated", "6", "11%"],
        ["4", "Single-study validated", "20", "36%"],
        ["3", "Adapts validated instrument", "20", "36%"],
        ["2", "Theory-inspired, no validation", "7", "13%"],
        ["1", "Keyword-level engagement only", "2", "4%"],
    ]
    col_widths = [25, 60, 25, 30]
    pdf.add_table(headers, rows, col_widths)
    pdf.output(str(TABLES_DIR / "table3-construct-validity.pdf"))
    print("  T3: Construct Validity Distribution")


def build_table_4():
    """T4: Theory Gap Summary."""
    pdf = TablePDF("Table 4: Theory Gap Summary")
    headers = ["Theory", "Dedicated LLM Benchmarks", "Papers Partially Engaging", "Core Prediction Tested?"]
    rows = [
        ["Dual Process", "0", "9", "No -- no time-pressure or cognitive load manipulation"],
        ["Social Intuitionism", "0", "18", "No -- no moral dumbfounding protocol"],
        ["Dyadic Morality", "0", "7", "No -- no agent-patient manipulation"],
    ]
    col_widths = [35, 40, 40, 50]
    pdf.add_table(headers, rows, col_widths)
    pdf.output(str(TABLES_DIR / "table4-theory-gaps.pdf"))
    print("  T4: Theory Gap Summary")


def build_table_5():
    """T5: Human Baseline Availability."""
    pdf = TablePDF("Table 5: Human Baseline Availability (A5 Distribution)")
    headers = ["Baseline Level", "Count", "Percentage"]
    rows = [
        ["Published norms (population-level)", "23", "42%"],
        ["Paper-specific (study-level)", "18", "33%"],
        ["Partial (some dimensions only)", "4", "7%"],
        ["None", "10", "18%"],
    ]
    col_widths = [70, 30, 30]
    pdf.add_table(headers, rows, col_widths)
    pdf.output(str(TABLES_DIR / "table5-human-baselines.pdf"))
    print("  T5: Human Baseline Availability")


def build_table_6():
    """T6: Task Format Distribution."""
    pdf = TablePDF("Table 6: Task Format Distribution in Top 15")
    headers = ["Format", "Count", "LLM Suitability", "Key Challenge"]
    rows = [
        ["Forced-choice (binary)", "3", "Excellent", "None -- trivially scorable"],
        ["Multiple-choice (MCQ)", "2", "Excellent", "Answer position bias"],
        ["Multi-label classification", "1", "Good", "Standard NLP task"],
        ["Likert scale (rating)", "3", "Moderate", "Scale compression; LLMs avoid extremes"],
        ["Scenario rating + ranking", "3", "Difficult", "Multi-step reasoning; ranking is hard"],
        ["Free-text + MCQ", "2", "Moderate", "Requires model-graded scoring"],
        ["Behavioral task", "1", "Poor", "Paradigm change needed"],
    ]
    col_widths = [40, 15, 30, 60]
    pdf.add_table(headers, rows, col_widths)
    pdf.output(str(TABLES_DIR / "table6-format-distribution.pdf"))
    print("  T6: Task Format Distribution")


def build_table_7():
    """T7: 9-Model Inventory."""
    pdf = TablePDF("Table 7: Cross-Vendor Model Inventory", landscape=True)
    headers = ["Vendor", "Model", "Size Class", "Alignment Method", "Benchmarks"]
    rows = [
        ["Anthropic", "Claude Opus 4.6", "Flagship", "Constitutional AI + RLHF", "23/23"],
        ["Anthropic", "Claude Sonnet 4.6", "Mid-tier", "Constitutional AI + RLHF", "23/23"],
        ["Anthropic", "Claude Haiku 3.5", "Small", "Constitutional AI + RLHF", "23/23"],
        ["Google", "Gemini 2.5 Pro", "Flagship", "Instruction tuning + RLHF", "23/23"],
        ["Google", "Gemini 3.1 Pro", "Flagship (next-gen)", "Instruction tuning + RLHF", "23/23"],
        ["Google", "Gemini 2.5 Flash", "Mid-tier", "Instruction tuning + RLHF", "23/23"],
        ["Google", "Gemini 2.5 Flash-Lite", "Small", "Instruction tuning + RLHF", "23/23"],
        ["OpenAI", "GPT-5 Codex", "Flagship", "Iterative RLHF", "23/23"],
        ["OpenAI", "GPT Mini", "Small", "Iterative RLHF", "23/23"],
    ]
    col_widths = [25, 40, 30, 50, 25]
    pdf.add_table(headers, rows, col_widths)
    pdf.output(str(TABLES_DIR / "table7-model-inventory.pdf"))
    print("  T7: Model Inventory")


def build_table_8():
    """T8: Benchmark Convergence Ranking."""
    pdf = TablePDF("Table 8: Benchmark Convergence Ranking (Lowest to Highest CV)", landscape=True)
    headers = ["Benchmark", "Primary Metric", "9-Model Range", "CV", "Classification"]
    rows = [
        ["MP6 (DIT-EMNLP)", "P-score", "90.0 -- 90.0", "0.000", "Ceiling"],
        ["MP7 (TrolleyBench)", "ECI", "1.0 -- 1.0", "0.000", "Ceiling"],
        ["MP11 (Kaleidoscope)", "task_c_accuracy", "1.0 -- 1.0", "0.000", "Ceiling"],
        ["MP22 (Tracing MF)", "foundation_id", "1.0 -- 1.0", "0.000", "Ceiling"],
        ["MP19 (Conscience)", "authority_win_rate", "0.29 -- 0.29", "0.000", "Invariant"],
        ["MP-DM (Dyadic)", "mean_blame", "3.208 -- 3.292", "~0.01", "Near-invariant"],
        ["MP-DP (Dual Process)", "ECI", "1.0 -- 1.0", "0.000", "Ceiling (CoT varies)"],
        ["MP2 (MFQ-30)", "ind_bind_ratio", "2.43 -- 2.83", "~0.06", "Low variation"],
        ["MP4 (MFV)", "care_score", "3.50 -- 3.85", "~0.04", "Low variation"],
        ["MP5 (ValueCompass)", "conformity", "varies", "Low", "Low variation"],
        ["MP8 (Moral Machine)", "utilitarian_pref", "0.91 -- 0.95", "~0.02", "Low variation"],
        ["MP9 (MFTC)", "accuracy", "0.63 -- 1.00", "~0.20", "Moderate variation"],
        ["MP10 (MoralCode)", "classification_acc", "0.79 -- 1.00", "~0.10", "Moderate variation"],
        ["MP12 (ValAct)", "gap_score", "varies", "Moderate", "Moderate variation"],
        ["MP15 (UniMoral)", "consistency", "varies", "Low", "Low variation"],
        ["MP16 (Moral Identity)", "internalization", "varies", "Moderate", "Moderate variation"],
        ["MP17 (Social Chem)", "accuracy", "varies", "Low", "Low variation"],
        ["MP18 (Cultural Persona)", "mfq_shift", "varies", "Moderate", "Discriminating"],
        ["MP20 (M3oralBench)", "accuracy", "varies", "Low", "Low variation"],
        ["MP21 (PRIME)", "priming_effect", "varies", "Low", "Low variation"],
        ["MP-CC (Cross-Cultural)", "perspective_acc", "4.0 -- 4.2", "~0.02", "Low variation"],
        ["MP-SI (Intuitionism)", "dumbfounding_rate", "~0.30", "Low", "Low variation"],
        ["MP3 (DIT)", "P-score", "60 -- 90", "~0.15", "Discriminating"],
    ]
    col_widths = [40, 35, 35, 20, 35]
    pdf.add_table(headers, rows, col_widths)
    pdf.output(str(TABLES_DIR / "table8-convergence-ranking.pdf"))
    print("  T8: Benchmark Convergence Ranking")


def build_table_9():
    """T9: Six Universal RLHF Fingerprints."""
    pdf = TablePDF("Table 9: Six Universal RLHF Moral Fingerprints")
    headers = ["#", "Signature", "Evidence", "Benchmark(s)"]
    rows = [
        ["1", "WEIRD-liberal moral foundation bias", "Ind/Bind ratio > 2.0 for all 9 models (range: 2.43-2.83)", "MP2, MP18"],
        ["2", "Purity floor", "All models score ~1.0 on MFT purity (functional minimum on 0-5 scale)", "MP4"],
        ["3", "Authority deference suppression", "Authority win rate = 0.29 for ALL 9 models in forced-choice", "MP19"],
        ["4", "Ethical consistency ceiling", "ECI = 1.0 for ALL models (perfect trolley consistency)", "MP-DP"],
        ["5", "Post-conventional moral default", "P-scores 60-90; zero models at Kohlberg conventional level", "MP3, MP6"],
        ["6", "Deontological refusal asymmetry", "Personal harm 0.1-0.5 vs. impersonal harm 0.9-1.0", "MP-DP"],
    ]
    col_widths = [8, 42, 75, 20]
    pdf.add_table(headers, rows, col_widths)
    pdf.output(str(TABLES_DIR / "table9-rlhf-fingerprints.pdf"))
    print("  T9: RLHF Fingerprints")


def build_table_10():
    """T10: DIT P-Score Non-Monotonic Pattern."""
    pdf = TablePDF("Table 10: DIT P-Score Across Anthropic Model Family")
    headers = ["Model", "Size Class", "MP3 P-score", "MP6 P-score (Teacher)", "Delta"]
    rows = [
        ["Claude Haiku 3.5", "Small", "60", "90", "+30"],
        ["Claude Opus 4.6", "Flagship", "75", "90", "+15"],
        ["Claude Sonnet 4.6", "Mid-tier", "85", "90", "+5"],
    ]
    col_widths = [40, 30, 30, 40, 20]
    pdf.add_table(headers, rows, col_widths)

    # Add note
    pdf.ln(3)
    pdf.set_font("Helvetica", "I", 8)
    pdf.multi_cell(0, 4, sanitize(
        "Note: The non-monotonic pattern (Sonnet > Opus > Haiku) contradicts the assumption "
        "that larger models produce more 'mature' moral reasoning. The teacher-persona ceiling "
        "(P=90 for all models) confirms that P-score is prompt-determined, not structurally fixed. "
        "All Gemini and OpenAI models cluster between 70-85, similar to Opus."))
    pdf.output(str(TABLES_DIR / "table10-dit-nonmonotonic.pdf"))
    print("  T10: DIT Non-Monotonic Pattern")


def build_table_11():
    """T11: MFT Profile Across 9 Models (selected metrics)."""
    pdf = TablePDF("Table 11: MFT Profile Across 9 Models", landscape=True)
    headers = ["Metric", "Opus", "Sonnet", "Haiku", "Gem 2.5P", "Gem 3.1P", "Gem Flash", "Gem FL", "Codex", "Mini"]
    rows = [
        ["Ind/Bind Ratio (MP2)", "2.83", "~2.7", "2.62", "~2.6", "~2.6", "~2.5", "~2.5", "~2.7", "~2.5"],
        ["MFV Care (MP4)", "~3.5", "3.50", "~3.4", "~3.5", "3.85", "~3.5", "~3.4", "~3.5", "~3.4"],
        ["MFV Purity (MP4)", "~1.0", "~1.0", "~1.0", "~1.0", "~1.0", "~1.0", "~1.0", "~1.0", "~1.0"],
        ["Authority Win (MP19)", "0.29", "0.29", "0.29", "0.29", "0.29", "0.29", "0.29", "0.29", "0.29"],
        ["Foundation ID (MP22)", "1.00", "1.00", "1.00", "1.00", "1.00", "1.00", "1.00", "1.00", "1.00"],
        ["MFTC Acc (MP9)", "0.63", "1.00", "0.97", "~0.9", "~0.9", "~0.9", "~0.9", "~0.9", "~0.9"],
    ]
    col_widths = [32, 17, 17, 17, 17, 17, 17, 17, 17, 17]
    pdf.add_table(headers, rows, col_widths)

    pdf.ln(3)
    pdf.set_font("Helvetica", "I", 8)
    pdf.multi_cell(0, 4, sanitize(
        "Note: Values marked with ~ are approximate, derived from cross-vendor comparison data. "
        "21 of 23 Gemini benchmarks were administered using cloned Opus prompts; only MP4 and MP9 "
        "have independently verified Gemini data. All models show a strongly WEIRD-liberal profile: "
        "high Individualizing, low Binding, functional purity elimination."))
    pdf.output(str(TABLES_DIR / "table11-mft-profile.pdf"))
    print("  T11: MFT Profile Across Models")


def main():
    print("Building table PDFs for MPBench Paper v2...")
    print(f"Output directory: {TABLES_DIR}\n")

    build_table_1()
    build_table_2()
    build_table_3()
    build_table_4()
    build_table_5()
    build_table_6()
    build_table_7()
    build_table_8()
    build_table_9()
    build_table_10()
    build_table_11()

    n_files = len(list(TABLES_DIR.glob("*.pdf")))
    print(f"\nDone. Generated {n_files} table PDFs in {TABLES_DIR}")


if __name__ == "__main__":
    main()
