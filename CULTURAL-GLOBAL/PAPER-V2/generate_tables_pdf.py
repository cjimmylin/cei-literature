#!/usr/bin/env python3
"""Generate main-text and supplementary table PDFs for PAPER-V2."""
from __future__ import annotations
from fpdf import FPDF
import os

BASE = os.path.dirname(os.path.abspath(__file__))

class TablePDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 8, "Cross-Cultural AI Values Alignment - Tables", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def section_title(self, title: str):
        self.set_font("Helvetica", "B", 11)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def table_row(self, cells: list[str], widths: list[float], bold: bool = False, fill: bool = False):
        self.set_font("Helvetica", "B" if bold else "", 8)
        if fill:
            self.set_fill_color(230, 230, 230)
        h = 6
        for i, (cell, w) in enumerate(zip(cells, widths)):
            self.cell(w, h, cell, border=1, fill=fill, align="C" if i > 0 else "L")
        self.ln(h)


def make_main_tables():
    pdf = TablePDF(orientation="L")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Table 1: Regional Ethical Fingerprints
    pdf.section_title("Table 1. Regional ethical fingerprints: top frameworks per region")
    cols = ["Region", "n", "Top Western", "Score", "Top Non-Western", "Score"]
    widths = [55, 15, 45, 18, 50, 18]
    pdf.table_row(cols, widths, bold=True, fill=True)
    rows = [
        ["North America", "840", "Utilitarian", "6.2", "Indigenous relational", "1.6"],
        ["Western Europe", "457", "Utilitarian", "6.6", "Confucian", "1.6"],
        ["East Asia", "271", "Utilitarian", "4.2", "Confucian", "3.5"],
        ["Latin America & Caribbean", "141", "Virtue", "1.1", "Indigenous relational", "6.0"],
        ["Southeast Asia", "115", "Utilitarian", "1.2", "Islamic ethics", "2.6"],
        ["MENA", "114", "Utilitarian", "1.2", "Islamic ethics", "3.4"],
        ["South Asia", "104", "Utilitarian", "1.2", "Confucian", "1.5"],
        ["Eastern Europe & C. Asia", "59", "Utilitarian", "2.0", "Confucian", "2.7"],
        ["Oceania", "46", "Virtue", "3.6", "Indigenous relational", "12.7"],
        ["Sub-Saharan Africa", "22", "Utilitarian", "1.6", "Ubuntu", "24.6"],
    ]
    for r in rows:
        pdf.table_row(r, widths)
    pdf.ln(5)

    # Table 2: WEIRD Distribution
    pdf.section_title("Table 2. WEIRD score distribution by tier")
    cols2 = ["Tier", "Score Range", "Count", "%"]
    w2 = [55, 35, 25, 25]
    pdf.table_row(cols2, w2, bold=True, fill=True)
    for r in [
        ["High-WEIRD", "70-100", "1,221", "59.7%"],
        ["Moderate-WEIRD", "50-69", "255", "12.5%"],
        ["Low-WEIRD", "30-49", "520", "25.4%"],
        ["Non-WEIRD", "0-29", "50", "2.4%"],
    ]:
        pdf.table_row(r, w2)
    pdf.ln(5)

    # Table 3: Representation Index
    pdf.section_title("Table 3. Regional representation index")
    cols3 = ["Region", "Corpus %", "World Pop %", "Index"]
    w3 = [55, 30, 30, 30]
    pdf.table_row(cols3, w3, bold=True, fill=True)
    for r in [
        ["North America", "39.5%", "4.7%", "8.4x over"],
        ["Western Europe", "20.6%", "5.4%", "3.8x over"],
        ["Oceania", "1.9%", "0.5%", "3.8x over"],
        ["East Asia", "12.7%", "20.9%", "0.6x under"],
        ["MENA", "5.5%", "7.6%", "0.7x under"],
        ["Southeast Asia", "5.0%", "8.6%", "0.6x under"],
        ["South Asia", "5.0%", "25.4%", "0.2x under"],
        ["Latin America", "4.4%", "8.3%", "0.5x under"],
        ["Sub-Saharan Africa", "1.1%", "14.7%", "0.07x under"],
    ]:
        pdf.table_row(r, w3)

    pdf.add_page()

    # Table 4: Concept Coverage
    pdf.section_title("Table 4. Non-Western concept coverage by tradition")
    cols4 = ["Tradition", "Benchmarks", "Concepts", "Measured", "Coverage"]
    w4 = [50, 25, 25, 25, 25]
    pdf.table_row(cols4, w4, bold=True, fill=True)
    for r in [
        ["Confucian", "30", "9", "2 (ren, li)", "22.2%"],
        ["Ubuntu", "5", "5", "1 (ubuntu)", "20.0%"],
        ["Islamic", "6", "7", "0", "0.0%"],
        ["Dharmic", "4", "6", "0", "0.0%"],
        ["Buddhist", "13", "6", "0", "0.0%"],
        ["Indigenous", "6", "6", "0", "0.0%"],
        ["Buen Vivir", "2", "5", "0", "0.0%"],
        ["TOTAL", "66", "44", "3", "6.8%"],
    ]:
        pdf.table_row(r, w4)
    pdf.ln(5)

    # Table 5: Top 10 TOPSIS
    pdf.section_title("Table 5. Top 10 benchmarks by TOPSIS score")
    cols5 = ["Rank", "Benchmark", "TOPSIS", "Key Strength"]
    w5 = [15, 80, 20, 80]
    pdf.table_row(cols5, w5, bold=True, fill=True)
    for r in [
        ["1", "Ray - Indigenous Knowledge Systems", "0.637", "NW scope, indigenous governance"],
        ["2", "Wu - CVC (Cultural Values Compass)", "0.597", "Chinese values, LLM-ready"],
        ["3", "Yu - CMoralEval", "0.569", "Chinese moral evaluation"],
        ["4", "Catapang - EMoTES-3K", "0.568", "Filipino emotion/morality"],
        ["5", "Alam - RAG to Agentic RAG (Islamic)", "0.565", "Islamic knowledge"],
        ["6", "Rahman - CCD-Bench", "0.553", "Cultural conflict, 37 countries"],
        ["7", "Lahmar - IslamTrust v1", "0.547", "Islamic values alignment"],
        ["8", "Lahmar - IslamTrust v2", "0.547", "Islamic values alignment"],
        ["9", "Rao - NormAd", "0.545", "Social norms, 37 countries"],
        ["10", "Rao - NORMAD (earlier)", "0.545", "Social norm adaptability"],
    ]:
        pdf.table_row(r, w5)
    pdf.ln(5)

    # Table 6: Benchmark Creator Geography
    pdf.section_title("Table 6. Benchmark creator geography")
    cols6 = ["Region", "Count", "% of Total"]
    w6 = [60, 25, 25]
    pdf.table_row(cols6, w6, bold=True, fill=True)
    for r in [
        ["North America", "86", "39.4%"],
        ["East Asia", "42", "19.3%"],
        ["Western Europe", "35", "16.1%"],
        ["South Asia", "18", "8.3%"],
        ["MENA", "9", "4.1%"],
        ["Southeast Asia", "7", "3.2%"],
        ["Oceania", "5", "2.3%"],
        ["Latin America", "3", "1.4%"],
        ["Sub-Saharan Africa", "2", "0.9%"],
        ["Eastern Europe", "1", "0.5%"],
    ]:
        pdf.table_row(r, w6)

    pdf.add_page()

    # Table 7: Trial Summary (simplified for PDF)
    pdf.section_title("Table 7. LLM trial cultural distance (CC1, n=50 items)")
    cols7 = ["Country", "Opus Distance", "Sonnet Distance", "Haiku Distance"]
    w7 = [50, 35, 35, 35]
    pdf.table_row(cols7, w7, bold=True, fill=True)
    for r in [
        ["Germany", "0.538", "0.550", "0.546"],
        ["United States", "0.884", "-", "-"],
        ["Japan", "0.990", "-", "-"],
        ["Brazil", "1.062", "-", "-"],
        ["China", "1.332", "-", "-"],
        ["India", "1.560", "-", "-"],
        ["Nigeria", "1.760", "-", "-"],
        ["Saudi Arabia", "1.974", "1.874", "1.874"],
    ]:
        pdf.table_row(r, w7)
    pdf.ln(5)

    # Table 8: RLHF Conflict Taxonomy
    pdf.section_title("Table 8. RLHF conflict taxonomy (n=237)")
    cols8 = ["Conflict Zone", "Count", "%", "Core Mechanism"]
    w8 = [50, 18, 14, 100]
    pdf.table_row(cols8, w8, bold=True, fill=True)
    for r in [
        ["Individual autonomy default", "51", "21.5", "Autonomy overrides collectivist frameworks"],
        ["Secular epistemology", "35", "14.8", "Cannot treat revelation as valid knowledge"],
        ["Consequentialist optimization", "31", "13.1", "Defaults to outcome-maximization"],
        ["Anti-authority bias", "8", "3.4", "Authority treated as suspect"],
        ["Gender equality lock", "6", "2.5", "Overrides complementarian frameworks"],
        ["Harm principle absolutism", "2", "0.8", "Purity/sanctity dismissed"],
        ["Other (diverse)", "116", "48.9", "Diverse conflicts"],
    ]:
        pdf.table_row(r, w8)
    pdf.ln(5)

    # Table 9: Cross-Model Agreement
    pdf.section_title("Table 9. Cross-model pairwise agreement (Pearson r)")
    cols9 = ["", "Opus", "Sonnet", "Haiku", "GPT-5.4", "GPT-Mini"]
    w9 = [35, 25, 25, 25, 25, 25]
    pdf.table_row(cols9, w9, bold=True, fill=True)
    for r in [
        ["Opus", "1.000", "0.952", "0.915", "-", "-"],
        ["Sonnet", "0.952", "1.000", "0.885", "-", "-"],
        ["Haiku", "0.915", "0.885", "1.000", "-", "-"],
        ["GPT-5.4", "-", "-", "-", "1.000", "0.842"],
        ["GPT-Mini", "-", "-", "-", "0.842", "1.000"],
    ]:
        pdf.table_row(r, w9)
    pdf.ln(5)

    # Table 10: Gap Compounding
    pdf.section_title("Table 10. Gap compounding across three studies")
    cols10 = ["Tradition", "Corpus (adj.)", "Concepts Measured", "Model Engagement"]
    w10 = [45, 35, 40, 45]
    pdf.table_row(cols10, w10, bold=True, fill=True)
    for r in [
        ["Buen Vivir", "~1 paper", "0 of 5", "Floor (1.0)"],
        ["Dharmic", "~4 papers", "0 of 6", "Haiku 4.0 (anomaly)"],
        ["Buddhist", "~7 papers", "0 of 6", "Floor (1.0)"],
        ["Indigenous", "~33 papers", "0 of 6", "Floor (1.0)"],
        ["Ubuntu", "~13 papers", "1 of 5", "Sonnet 4.0 (anomaly)"],
        ["Islamic", "~23 papers", "0 of 7", "Selective"],
        ["Confucian", "~14 papers", "2 of 9", "Floor (1.0)"],
    ]:
        pdf.table_row(r, w10)

    out = os.path.join(BASE, "tables", "main-tables.pdf")
    pdf.output(out)
    print(f"Main tables PDF: {out}")


def make_supp_tables():
    pdf = TablePDF(orientation="L")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # S-Table 1: Gold Standard Validation
    pdf.section_title("Supplementary Table S1. Gold standard validation results")
    cols = ["Framework", "Precision", "Recall", "F1", "TP", "FP", "FN", "Primary FP Pattern"]
    widths = [35, 20, 18, 15, 12, 12, 12, 80]
    pdf.table_row(cols, widths, bold=True, fill=True)
    for r in [
        ["Islamic", "1.000", "1.000", "1.000", "12", "0", "0", "(eliminated)"],
        ["Indigenous", "0.675", "0.900", "0.771", "27", "13", "3", "Indigenous language NLP"],
        ["Ubuntu", "0.579", "1.000", "0.733", "11", "8", "0", "Ubuntu OS; passing mentions"],
        ["Confucian", "0.364", "1.000", "0.533", "8", "14", "0", "Chinese NLP benchmarks"],
        ["Buddhist", "0.333", "1.000", "0.500", "3", "6", "0", "Buddhist text corpora"],
        ["Dharmic", "0.250", "1.000", "0.400", "2", "6", "0", "NLP on Hindu/Vedic texts"],
        ["Buen Vivir", "0.167", "1.000", "0.286", "1", "5", "0", "Passing mentions"],
        ["MEAN", "0.481", "0.986", "0.603", "64", "52", "3", ""],
    ]:
        pdf.table_row(r, widths)
    pdf.ln(5)

    # S-Table 6: Cross-Model MFQ
    pdf.section_title("Supplementary Table S6. MFQ profiles by model")
    cols6 = ["Model", "Provider", "Tier", "I:B Ratio", "Closest Country", "Farthest"]
    w6 = [40, 25, 25, 22, 35, 35]
    pdf.table_row(cols6, w6, bold=True, fill=True)
    for r in [
        ["Haiku 4.5", "Anthropic", "1 (Auth)", "4.82", "Germany", "Saudi Arabia"],
        ["Opus 4.6", "Anthropic", "1 (Auth)", "3.75", "Germany", "Saudi Arabia"],
        ["Sonnet 4.6", "Anthropic", "1 (Auth)", "3.23", "Germany", "Saudi Arabia"],
        ["GPT-5.4-Mini", "OpenAI", "2 (Codex)", "3.22", "-", "-"],
        ["GPT-5.4", "OpenAI", "2 (Codex)", "2.48", "-", "-"],
        ["Gemini (all 5)", "Google", "3 (Template)", "3.75", "-", "-"],
    ]:
        pdf.table_row(r, w6)

    out = os.path.join(BASE, "supplementary", "supp-tables", "supp-tables.pdf")
    pdf.output(out)
    print(f"Supplementary tables PDF: {out}")


if __name__ == "__main__":
    make_main_tables()
    make_supp_tables()
    print("Done.")
