# NormEval Paper v2 — Session 14 Handoff

**Date:** 2026-04-05
**Session:** Combined PDF generation + 3 bug fixes
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260405c-normeval-session13-handoff.md`

---

## What Was Done This Session

### Bug Fix 1: Figure S5 Provider Radar

Fixed `figS5_provider_radar()` in `generate_normeval_figures_v2.py`. The `provider_profiles` data structure has `dimensions` (list) + `profiles` (dict of provider→values), but the script was checking for the wrong nested structure. Now correctly renders a 3-provider radar chart with 6 dimensions (IH Acceptance, CBR Rate, Persuasion Resistance, Knowledge Acc., Kohlberg Stage, Altruism Rate). Figure S5 generated: 226KB PNG + 38KB PDF.

### Bug Fix 2: Introduction n=37 References

Created `introduction-comprehensive-normeval-v2.md` in PAPER-v2/ by copying the v1 comprehensive intro and updating 6 occurrences of stale n=37 references:
- Title: "37 LLM Moral Reasoning Assessments" → new v2 title
- Abstract: 37→54 benchmarks, 15→24 gate-passing, 150→114 items, 5→15 trials, added cross-vendor findings
- Contributions paragraph: three→four contributions, added cross-vendor profiles finding
- Roadmap paragraph: updated section descriptions for v2 structure (7 sections, 12-member council)
- Body text line 92: "27 of 37" → "44 of 54"
- Body text line 126: "37 benchmarks...12 (32%)" → "54 benchmarks...18 (33%)"
- Venue: NeurIPS → "Academic journal (general format)"

Verified: zero "37" grep matches in the v2 introduction.

### Bug Fix 3: fpdf2 Deprecation Warnings

Replaced all `ln=True` parameters with `new_x=XPos.LMARGIN, new_y=YPos.NEXT` in `generate_normeval_figures_v2.py` and also removed deprecated `uni=True` from `add_font()` in the combined PDF script. Both scripts now run with zero warnings.

### Combined PDF Generation

Created `PYTHON/generate_normeval_combined_pdf.py` — a comprehensive markdown→HTML→fpdf2 pipeline that:
1. Reads all 19 markdown sections in order (excluding introduction/related work)
2. Converts markdown to HTML via the `markdown` library (with tables, fenced_code, nl2br extensions)
3. Renders HTML to PDF via fpdf2's `write_html()` with Arial Unicode MS font (full Unicode support)
4. Embeds all 12 publication-quality figures inline where referenced
5. Adds a figures gallery section for both main and supplementary figures
6. Produces a single document with title page, running headers/footers, and page numbers

**Output:** `PAPER-v2/20260405-normeval-paper-v2.1.pdf` — 180 pages, 2.6 MB

### Figures Regenerated

Re-ran `generate_normeval_figures_v2.py` producing 12 figures (was 11 — Figure S5 now included):
- 8 main body: tradition heatmap, framework difficulty, ND-PE scatter, data availability, trial accuracy, IH/IB scaling, cross-vendor heatmap, knowledge-judgment divergence
- 4 supplementary: PCA clusters, temporal trends, provider radar (NEW), CBR by model

Also regenerated `normeval-figures-tables-v2.pdf` (figures-only combined PDF, 1.8 MB).

---

## Remaining Work

### Priority 1: LaTeX conversion
NeurIPS 2026 template or target journal format. Markdown is ready; needs typesetting.

### Priority 2: Cross-reference audit
Automated check that every `Figure N` / `Table N` / `Section N.N` in text has a corresponding file/section.

### Priority 3: Temperature sensitivity test
Gemini models at non-zero temperature to disambiguate shared infrastructure vs. deterministic decoding.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Combined PDF (v2.1) | `PAPER-v2/20260405-normeval-paper-v2.1.pdf` | 180-page combined document |
| Combined PDF script | `PYTHON/generate_normeval_combined_pdf.py` | Regenerates combined PDF |
| Figure script | `PYTHON/generate_normeval_figures_v2.py` | Generates all 12 figures |
| v2 Introduction | `PAPER-v2/introduction-comprehensive-normeval-v2.md` | Updated intro (n=54) |
| Figure S5 (new) | `PAPER-v2/figures/figS5-provider-radar.png` | Provider ethical profiles radar |
| Figures-only PDF | `PAPER-v2/normeval-figures-tables-v2.pdf` | 1.8 MB, figures only |
| S13 handoff | `METHODS/20260405c-normeval-session13-handoff.md` | Previous session |

## Known Issues

None. All 3 issues from Session 13 are resolved. The paper is complete pending LaTeX conversion.

---

*Filed: 2026-04-05 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
