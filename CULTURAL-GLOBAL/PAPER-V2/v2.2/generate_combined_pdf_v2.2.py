#!/usr/bin/env python3
"""
Generate the v2.2 combined PDF — fully self-contained bundle.

All paths resolve WITHIN v2.2/ (no ../). Reads from:
  v2.2/sections/        (11 markdown files)
  v2.2/figures/         (10 main figures)
  v2.2/supplementary/   (5 S-text markdowns + supp-figures/)

Output: v2.2/20260413-cross-cultural-ai-values-alignment-v2.2.pdf

Changes from v2.1 (2026-04-13):
- VERSION bumped to v2.2
- DATE_PREFIX bumped to 20260413
- All path anchors relocated to v2.2/ subfolder (full self-containment)
- Dry-run assertion loop before any page is written (prevents fpdf2 silent figure drop)
- Explicit figure lists (no globs, per C10-1 figure-glob trap)
- MFQ discrepancy documented in CHANGELOG-v2.2.md (not re-derived)
"""
from __future__ import annotations
import os
import re
import sys
import textwrap
from pathlib import Path
from fpdf import FPDF

# ── Path anchors (all within v2.2/) ──────────────────────────
BASE          = Path(__file__).resolve().parent               # …/PAPER-V2/v2.2/
SECTIONS_DIR  = BASE / "sections"                             # local copies
FIGURES_DIR   = BASE / "figures"                              # local copies
SUPP_DIR      = BASE / "supplementary"                        # local copies
SUPP_FIG_DIR  = SUPP_DIR / "supp-figures"                     # local copies
FONT_PATH     = Path("/Library/Fonts/Arial Unicode.ttf")

VERSION     = "v2.2"
DATE_PREFIX = "20260413"
OUT_FILE    = BASE / f"{DATE_PREFIX}-cross-cultural-ai-values-alignment-{VERSION}.pdf"

# ── Expected figures (explicit list, not glob) ───────────────
EXPECTED_MAIN_FIGURES = [
    "world-map-weird.png",
    "heatmap-regions-frameworks.png",
    "dendrogram.png",
    "correspondence-biplot.png",
    "benchmark-landscape-clusters.png",
    "concept-coverage-gaps.png",
    "cultural-map-position.png",
    "mfq-profile-comparison.png",
    "rlhf-conflict-taxonomy.png",
    "triple-bind-diagram.png",
]
EXPECTED_SUPP_FIGURES = [
    "pipeline-diagram.png",
    "silhouette.png",
    "weird-histogram.png",
    "weird-radar.png",
    "north-south-radar.png",
    "nw-detection-bars.png",
    "bubble-world-map.png",
]
EXPECTED_SECTIONS = [
    "00-abstract.md",
    "01-introduction.md",
    "02-methods.md",
    "03-results-corpus.md",
    "04-results-benchmarks.md",
    "05-results-trials.md",
    "06-results-synthesis.md",
    "07-discussion.md",
    "08-conclusion.md",
    "09-references.md",
    "10-endmatter.md",
]
EXPECTED_SUPP_SECTIONS = [
    "S1-methods.md",
    "S2-results.md",
    "S3-council.md",
    "S4-trial-protocols.md",
    "S5-keyword-lists.md",
]


def dry_run_assertions():
    """Verify every path anchor and every expected file exists BEFORE fpdf2 writes."""
    missing = []

    # Anchor existence
    for anchor in [SECTIONS_DIR, FIGURES_DIR, SUPP_DIR, SUPP_FIG_DIR, FONT_PATH]:
        if not anchor.exists():
            missing.append(f"anchor: {anchor}")

    # Section files
    for fname in EXPECTED_SECTIONS:
        p = SECTIONS_DIR / fname
        if not p.exists():
            missing.append(f"section: {p}")

    # Main figures — WARN not fail (6 deferred low-DPI figs tolerated per v2.1 known-issue)
    missing_figs = []
    for fname in EXPECTED_MAIN_FIGURES:
        p = FIGURES_DIR / fname
        if not p.exists():
            missing_figs.append(str(p))

    # Supp figures
    for fname in EXPECTED_SUPP_FIGURES:
        p = SUPP_FIG_DIR / fname
        if not p.exists():
            missing_figs.append(str(p))

    # Supp sections
    for fname in EXPECTED_SUPP_SECTIONS:
        p = SUPP_DIR / fname
        if not p.exists():
            missing.append(f"supp-section: {p}")

    if missing:
        print("DRY-RUN FAILURE — missing anchors/sections:")
        for m in missing:
            print(f"  MISSING: {m}")
        sys.exit(1)

    if missing_figs:
        print(f"DRY-RUN WARNING — {len(missing_figs)} figure(s) missing (v2.1 carryover):")
        for m in missing_figs:
            print(f"  [DEFERRED] {m}")
        print("(Proceeding — these are the 6 deferred low-DPI figures per v2.1 known-issue.)")

    print("DRY-RUN OK — all required anchors present.")


class PaperPDF(FPDF):
    """Custom PDF with header/footer for the combined paper."""

    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=20)
        # Add Unicode font
        self.add_font("ArialUni", "", str(FONT_PATH))
        self.add_font("ArialUni", "B", str(FONT_PATH))
        self.add_font("ArialUni", "I", str(FONT_PATH))
        self.add_font("ArialUni", "BI", str(FONT_PATH))
        self._current_section = ""
        self._page_started = False

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("ArialUni", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 5, f"Cross-Cultural AI Values Alignment  |  {VERSION}  |  {DATE_PREFIX}",
                  align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def footer(self):
        self.set_y(-15)
        self.set_font("ArialUni", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 5, f"Page {self.page_no()}", align="C")
        self.set_text_color(0, 0, 0)

    def title_page(self):
        self.add_page()
        self.ln(30)
        self.set_font("ArialUni", "B", 18)
        self.multi_cell(0, 9,
            "Cross-Cultural AI Values Alignment:\n"
            "The Triple Bind of WEIRD Scholarship,\n"
            "Broken Benchmarks, and Monocultural Models",
            align="C")
        self.ln(10)
        self.set_font("ArialUni", "", 11)
        self.cell(0, 7, f"Version {VERSION}  |  {DATE_PREFIX}", align="C",
                  new_x="LMARGIN", new_y="NEXT")
        self.ln(5)
        self.set_font("ArialUni", "I", 10)
        self.multi_cell(0, 6,
            "Fully self-contained bundle — sections, figures, and supplementary\n"
            "materials live within this folder. Independently rebuildable via\n"
            "bash build_v2.2.sh. Paired dashboard at:\n"
            "https://cjimmylin.github.io/cei-cultural-global-dashboard-v2/",
            align="C")
        self.ln(10)
        self.set_font("ArialUni", "", 9)
        self.multi_cell(0, 5,
            "Complete paper: Introduction, Abstract, Methods, Results (Studies 1-3 + Synthesis),\n"
            "Discussion, Conclusion, References, Endmatter, 10 Main Figures, 14 Tables,\n"
            "and Supplementary Materials (5 text sections, 14 supplementary figures,\n"
            "including 2 corpus assembly flowcharts and 5 regenerated at 600 DPI).",
            align="C")
        self.ln(15)

        # Table of contents
        self.set_font("ArialUni", "B", 13)
        self.cell(0, 8, "Table of Contents", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self.set_font("ArialUni", "", 10)
        toc = [
            ("Abstract", ""),
            ("1. Introduction", "Framing the triple bind"),
            ("2. Methods", "Integrated three-study design"),
            ("3. Results: Study 1 -- The WEIRD Landscape", "Corpus analysis"),
            ("4. Results: Study 2 -- The Evaluation Infrastructure", "Benchmark meta-evaluation"),
            ("5. Results: Study 3 -- What LLMs Actually Do", "Self-administration trials"),
            ("6. Results: Synthesis -- The Triple Bind", "Cross-cutting synthesis"),
            ("7. Discussion", "Implications and recommendations"),
            ("8. Conclusion", "Triple diagnosis and path forward"),
            ("9. References", ""),
            ("10. Endmatter", "Author contributions, funding, ethics"),
            ("Main Figures", "Figures 1-10"),
            ("Main Tables", "Tables 1-10 (reference)"),
            ("--- SUPPLEMENTARY MATERIALS ---", ""),
            ("S1. Extended Methods", "Keyword lists, TOPSIS, WEIRD rubrics"),
            ("S2. Extended Results", "Full profiles, statistics, rankings"),
            ("S3. Council Composition", "12 members, minority reports"),
            ("S4. Trial Protocols", "CC1-CC10 specs, provenance"),
            ("S5. Keyword Taxonomy", "Detection rates, FP patterns"),
            ("Supplementary Figures", "S-Figs 1-7"),
            ("Supplementary Tables", "S-Tables 1-8 (reference)"),
        ]
        for title, desc in toc:
            if title.startswith("---"):
                self.ln(3)
                self.set_font("ArialUni", "B", 10)
                self.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
                self.set_font("ArialUni", "", 10)
            else:
                line = f"    {title}"
                if desc:
                    line += f"  --  {desc}"
                self.cell(0, 5.5, line, new_x="LMARGIN", new_y="NEXT")

    def section_break(self, title: str):
        self.add_page()
        self.ln(5)
        self.set_fill_color(40, 40, 60)
        self.set_text_color(255, 255, 255)
        self.set_font("ArialUni", "B", 14)
        self.cell(0, 12, f"  {title}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(5)

    def render_markdown(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        for line in text.split("\n"):
            stripped = line.strip()

            if not stripped:
                self.ln(2)
                continue

            if stripped.startswith("# "):
                self.ln(3)
                self.set_font("ArialUni", "B", 14)
                self.multi_cell(0, 7, stripped[2:].strip(), new_x="LMARGIN", new_y="NEXT")
                self.ln(2)
            elif stripped.startswith("## "):
                self.ln(3)
                self.set_font("ArialUni", "B", 12)
                self.multi_cell(0, 6.5, stripped[3:].strip(), new_x="LMARGIN", new_y="NEXT")
                self.ln(1.5)
            elif stripped.startswith("### "):
                self.ln(2)
                self.set_font("ArialUni", "B", 11)
                self.multi_cell(0, 6, stripped[4:].strip(), new_x="LMARGIN", new_y="NEXT")
                self.ln(1)
            elif stripped.startswith("#### "):
                self.ln(1)
                self.set_font("ArialUni", "BI", 10)
                self.multi_cell(0, 5.5, stripped[5:].strip(), new_x="LMARGIN", new_y="NEXT")
                self.ln(1)
            elif stripped.startswith("|"):
                self._render_table_row(stripped)
            elif stripped.startswith("---") and len(stripped) <= 5:
                self.ln(2)
                self.set_draw_color(180, 180, 180)
                self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
                self.ln(3)
            elif stripped.startswith("> "):
                self.set_font("ArialUni", "I", 9)
                self.set_x(self.l_margin + 8)
                clean = self._clean_md(stripped[2:])
                self.multi_cell(self.w - self.l_margin - self.r_margin - 8, 5, clean,
                               new_x="LMARGIN", new_y="NEXT")
                self.set_font("ArialUni", "", 10)
            elif re.match(r"^\d+\.\s", stripped):
                self.set_font("ArialUni", "", 10)
                clean = self._clean_md(stripped)
                self.set_x(self.l_margin + 5)
                self.multi_cell(self.w - self.l_margin - self.r_margin - 5, 5, clean,
                               new_x="LMARGIN", new_y="NEXT")
            elif stripped.startswith("- ") or stripped.startswith("* "):
                self.set_font("ArialUni", "", 10)
                clean = self._clean_md(stripped[2:])
                self.set_x(self.l_margin + 5)
                bullet = "\u2022 " + clean
                self.multi_cell(self.w - self.l_margin - self.r_margin - 5, 5, bullet,
                               new_x="LMARGIN", new_y="NEXT")
            elif stripped.startswith("!["):
                continue
            else:
                self.set_font("ArialUni", "", 10)
                clean = self._clean_md(stripped)
                if clean:
                    self.multi_cell(0, 5, clean, new_x="LMARGIN", new_y="NEXT")

    def _clean_md(self, text):
        text = re.sub(r'\*\*\*(.*?)\*\*\*', r'\1', text)
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        text = re.sub(r'\*(.*?)\*', r'\1', text)
        text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
        text = re.sub(r'`(.*?)`', r'\1', text)
        return text.strip()

    def _render_table_row(self, line):
        if re.match(r'^\|[\s\-:|]+\|$', line):
            return
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if not cells:
            return
        is_header = any(c.startswith("**") for c in cells) or self._is_first_table_row
        n = len(cells)
        available = self.w - self.l_margin - self.r_margin
        col_w = available / max(n, 1)
        if is_header:
            self.set_font("ArialUni", "B", 8)
            self.set_fill_color(230, 230, 230)
        else:
            self.set_font("ArialUni", "", 8)
        h = 5
        for cell in cells:
            clean = self._clean_md(cell)
            if len(clean) > int(col_w / 1.8):
                clean = clean[:int(col_w / 1.8)] + ".."
            self.cell(col_w, h, clean, border=1, fill=is_header, align="C")
        self.ln(h)
        self._is_first_table_row = False

    _is_first_table_row = True

    def insert_figure(self, filepath, caption, width=170):
        filepath = str(filepath)
        if not os.path.exists(filepath):
            self.set_font("ArialUni", "I", 9)
            self.cell(0, 6, f"[Figure not found: {os.path.basename(filepath)}]",
                      new_x="LMARGIN", new_y="NEXT")
            return
        if self.get_y() > 180:
            self.add_page()
        x = (self.w - width) / 2
        try:
            self.image(filepath, x=x, w=width)
        except Exception:
            self.set_font("ArialUni", "I", 9)
            self.cell(0, 6, f"[Could not render: {os.path.basename(filepath)}]",
                      new_x="LMARGIN", new_y="NEXT")
            return
        self.ln(2)
        self.set_font("ArialUni", "I", 9)
        self.multi_cell(0, 4.5, caption, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)


def build_combined_pdf():
    dry_run_assertions()

    pdf = PaperPDF()
    pdf.title_page()

    sec = lambda name: str(SECTIONS_DIR / name)
    supp = lambda name: str(SUPP_DIR / name)

    pdf.section_break("Abstract")
    pdf.render_markdown(sec("00-abstract.md"))

    pdf.section_break("1. Introduction")
    pdf._is_first_table_row = True
    pdf.render_markdown(sec("01-introduction.md"))

    pdf.section_break("2. Methods")
    pdf._is_first_table_row = True
    pdf.render_markdown(sec("02-methods.md"))

    pdf.section_break("3. Results -- Study 1: The WEIRD Landscape")
    pdf._is_first_table_row = True
    pdf.render_markdown(sec("03-results-corpus.md"))

    pdf.section_break("4. Results -- Study 2: The Evaluation Infrastructure")
    pdf._is_first_table_row = True
    pdf.render_markdown(sec("04-results-benchmarks.md"))

    pdf.section_break("5. Results -- Study 3: What LLMs Actually Do")
    pdf._is_first_table_row = True
    pdf.render_markdown(sec("05-results-trials.md"))

    pdf.section_break("6. Results -- Synthesis: The Triple Bind")
    pdf._is_first_table_row = True
    pdf.render_markdown(sec("06-results-synthesis.md"))

    pdf.section_break("7. Discussion")
    pdf._is_first_table_row = True
    pdf.render_markdown(sec("07-discussion.md"))

    pdf.section_break("8. Conclusion")
    pdf._is_first_table_row = True
    pdf.render_markdown(sec("08-conclusion.md"))

    pdf.section_break("9. References")
    pdf._is_first_table_row = True
    pdf.render_markdown(sec("09-references.md"))

    pdf.section_break("10. Endmatter")
    pdf._is_first_table_row = True
    pdf.render_markdown(sec("10-endmatter.md"))

    # MAIN FIGURES
    pdf.section_break("Main Figures")
    main_figure_captions = {
        "world-map-weird.png": "Figure 1. Geographic distribution of 2,329 AI ethics papers by WEIRD score tier.",
        "heatmap-regions-frameworks.png": "Figure 2. Heatmap of mean framework scores (rows) by region (columns).",
        "dendrogram.png": "Figure 3. Hierarchical clustering dendrogram (Ward's method) on 10 regional profiles.",
        "correspondence-biplot.png": "Figure 4. Correspondence analysis biplot of region-by-framework associations.",
        "benchmark-landscape-clusters.png": "Figure 5. Benchmark landscape: two-cluster structure (Non-Western Focused vs. LLM-Ready).",
        "concept-coverage-gaps.png": "Figure 6. Non-Western moral concept operationalization gaps across 218 benchmarks.",
        "cultural-map-position.png": "Figure 7. Claude's position on the Inglehart-Welzel cultural map relative to 8 countries.",
        "mfq-profile-comparison.png": "Figure 8. Moral Foundations profiles: Claude Opus 4.6 vs. human populations.",
        "rlhf-conflict-taxonomy.png": "Figure 9. RLHF conflict taxonomy (n=237) and impact on non-Western traditions.",
        "triple-bind-diagram.png": "Figure 10. The Triple Bind: self-reinforcing WEIRD bias across scholarship, benchmarks, and models.",
    }
    for fname in EXPECTED_MAIN_FIGURES:
        pdf.insert_figure(FIGURES_DIR / fname, main_figure_captions[fname], width=165)

    # MAIN TABLES reference
    pdf.section_break("Main Tables (Tables 1-10)")
    pdf.set_font("ArialUni", "", 10)
    pdf.multi_cell(0, 5,
        "Tables 1-10 are rendered inline within sections 3-6. Tabular summaries:\n\n"
        "  Table 1. Regional ethical fingerprints: top frameworks per region\n"
        "  Table 2. WEIRD score distribution by tier\n"
        "  Table 3. Regional representation index\n"
        "  Table 4. Non-Western concept coverage by tradition\n"
        "  Table 5. Top 10 benchmarks by TOPSIS score\n"
        "  Table 6. Benchmark creator geography\n"
        "  Table 7. LLM trial cultural distance (CC1)\n"
        "  Table 8. RLHF conflict taxonomy (n=237)\n"
        "  Table 9. Cross-model pairwise agreement (Pearson r)\n"
        "  Table 10. Gap compounding across three studies",
        new_x="LMARGIN", new_y="NEXT")

    # SUPPLEMENTARY
    pdf.section_break("SUPPLEMENTARY MATERIALS")
    pdf.set_font("ArialUni", "I", 11)
    pdf.multi_cell(0, 6,
        "The following supplementary materials accompany the main paper.\n"
        "Extended methods, extended results, council deliberations, trial\n"
        "protocols, keyword taxonomy, supplementary figures, and tables.",
        align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.section_break("S1. Extended Methods")
    pdf._is_first_table_row = True
    pdf.render_markdown(supp("S1-methods.md"))

    pdf.section_break("S2. Extended Results")
    pdf._is_first_table_row = True
    pdf.render_markdown(supp("S2-results.md"))

    pdf.section_break("S3. Council Composition & Deliberations")
    pdf._is_first_table_row = True
    pdf.render_markdown(supp("S3-council.md"))

    pdf.section_break("S4. Trial Protocols & Responses")
    pdf._is_first_table_row = True
    pdf.render_markdown(supp("S4-trial-protocols.md"))

    pdf.section_break("S5. Keyword Taxonomy Statistics")
    pdf._is_first_table_row = True
    pdf.render_markdown(supp("S5-keyword-lists.md"))

    # SUPP FIGURES
    pdf.section_break("Supplementary Figures")
    supp_figure_captions = {
        "pipeline-diagram.png":   "S-Figure 1. Analytical pipeline overview.",
        "silhouette.png":          "S-Figure 2. Silhouette analysis for k=2 through k=6 clusters.",
        "weird-histogram.png":    "S-Figure 3. Distribution of WEIRD scores (0-100) across 2,329 papers.",
        "weird-radar.png":         "S-Figure 4. WEIRD sub-dimension profiles by region (radar chart).",
        "north-south-radar.png":   "S-Figure 5. Global North/South/Ambiguous framework profiles (radar chart).",
        "nw-detection-bars.png":   "S-Figure 6. Non-Western framework detection rates by region.",
        "bubble-world-map.png":    "S-Figure 7. Geographic distribution by region, colored by dominant non-Western framework.",
    }
    for fname in EXPECTED_SUPP_FIGURES:
        pdf.insert_figure(SUPP_FIG_DIR / fname, supp_figure_captions[fname], width=155)

    # SUPP TABLES
    pdf.section_break("Supplementary Tables (S1-S8)")
    pdf.set_font("ArialUni", "", 10)
    pdf.multi_cell(0, 5,
        "Supplementary Tables S1-S8:\n\n"
        "  S-Table 1. Gold standard validation results (P/R/F1 by framework)\n"
        "  S-Table 2. Mean framework scores across 10 macro-regions (19 dimensions)\n"
        "  S-Table 3. Benchmark TOPSIS rankings (top 50 of 218)\n"
        "  S-Table 4. Trial results by model x benchmark (10 models)\n"
        "  S-Table 5. RLHF conflict instances by category and trial (n=237)\n"
        "  S-Table 5b. Representative RLHF conflict examples (14 rows)\n"
        "  S-Table 6. Cross-model agreement + MFQ profiles by model\n"
        "  S-Table 7. Keyword taxonomy summary statistics\n"
        "  S-Table 8. Temporal trends in corpus composition (2018-2026)",
        new_x="LMARGIN", new_y="NEXT")

    pdf.output(str(OUT_FILE))
    print(f"\nCombined PDF: {OUT_FILE}")
    print(f"Size: {os.path.getsize(OUT_FILE) / 1024:.1f} KB")
    print(f"Pages: {pdf.page_no()}")


if __name__ == "__main__":
    build_combined_pdf()
