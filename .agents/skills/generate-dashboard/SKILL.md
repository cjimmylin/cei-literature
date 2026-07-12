---
name: generate-dashboard
description: Regenerate interactive HTML dashboard from JSON classification data. Creates self-contained HTML with ECharts visualizations.
disable-model-invocation: true
---

# Generate Dashboard

**Purpose:** Regenerate the interactive HTML dashboard from the vault's JSON classification data. Produces a single self-contained HTML file with ECharts visualizations, filterable tables, and KPI cards.

**When to use:** After updating classification data (new papers imported, re-running benchmark survey, updating normative classifications) or when you want a fresh dashboard reflecting current vault state.

**Trigger:** `/generate-dashboard`

---

## Overview

```
Step 1: Run the Python generator
  └─ ../.venv/bin/python PYTHON/generate_vault_dashboard.py

Step 2: Verify KPIs match expected values
  ├─ Total papers (currently 2,034)
  ├─ Benchmark candidates (currently 989)
  ├─ Public benchmarks (currently 375)
  ├─ Pluralistic relevance (currently 76%)
  └─ Normative ethics (currently 45)

Step 3: Open in browser for visual check
  └─ open DASHBOARDS/20260216-vault-dashboard.html

Step 4: Validate papers untouched
  └─ ../.venv/bin/python PYTHON/validate_all_papers.py
```

---

## Data Sources (4 JSON files in `logs/`)

| File | Records | Description |
|------|---------|-------------|
| `20260216-benchmark_survey_all_classifications.json` | 2,002 | All papers from deep-read survey (Sessions 70s-84) |
| `20260216-benchmark_survey_candidates.json` | 989 | Benchmark/evaluation candidates |
| `20260207-normative_v2_all_classifications.json` | 266 | Normative ethics classification |
| `20260208-author_paper_map.json` | 846 | Author-paper mapping (pre-expansion) |

**Important:** If the data files are updated (e.g., new papers added), the assertions in the script will need updating. The script currently asserts exact counts — comment out or update the assertions if data has changed.

---

## Output

**File:** `DASHBOARDS/20260216-vault-dashboard.html` (~202 KB)

**Self-contained:** HTML + inline CSS + inline JS + embedded JSON data blob (~95 KB). Only external dependencies are CDN-loaded:
- ECharts 5.5.1 (~300 KB, cached)
- Inter font (Google Fonts)
- JetBrains Mono font (Google Fonts)

**Dashboard Sections (6 tabs):**

1. **Overview** — KPI cards (animated count-up), stacked bar timeline (2016-2026), category distribution bar, availability donut, top 15 authors bar
2. **Taxonomy** — Category x Year heatmap, 10x10 co-occurrence matrix
3. **Models & Methods** — Top 15 model families bar, 14 methodology types bar, model x category heatmap (top 12)
4. **Cultural Coverage** — Pluralistic relevance donut, ethical tradition bar (severity-coded), language bar, language x category heatmap
5. **Resources** — Filterable/sortable table of 306 public benchmarks with search, category/year dropdowns, public-only toggle, pagination (25/page)
6. **Normative** — Classification donut (Yes/Borderline/Excluded), framework distribution bar, paper detail cards

---

## Architecture

**Pattern:** "Fat data, thin client"

- **Python side:** Loads 4 JSON files, runs all regex normalization (27 model families, 14 methodology types, 10 ethical traditions, 20 languages, 16 normative frameworks), computes cross-tabulations, co-occurrence matrices, and per-category breakdowns. Outputs a `const DATA = {...}` JSON blob embedded in the HTML.
- **Browser side:** Initializes ECharts charts from pre-computed arrays/matrices. Vanilla JS handles tab switching, table filtering/sorting/pagination, and KPI count-up animation. No framework needed (528 data points is trivial).

**Normalization engine:** Shared with `generate_vault_overview_report.py`. Functions are copied (not imported) to keep the dashboard script self-contained except for CATEGORIES/classify_entry from `generate_benchmark_survey_report.py`.

---

## Customization

### Updating the date prefix
If regenerating on a different date, update:
1. `OUTPUT_FILE` path in the script (line ~37)
2. Header subtitle in the HTML template
3. Footer text in the HTML template

### Adding new chart sections
1. Add the data computation in `compute_dashboard_data()`
2. Add the HTML container `<div>` in the appropriate section
3. Add the ECharts initialization in the `<script>` block
4. Remember: all JS `{` and `}` must be doubled (`{{`, `}}`) since it's a Python f-string

### Changing the color scheme
CSS custom properties are in `:root` at the top of the `<style>` block. Category colors are in the `CAT_COLORS` JS array.

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Script fails with assertion error | Data files have different record counts (new papers added) | Update or remove the `assert` statements |
| Charts don't render | ECharts CDN blocked or offline | Download echarts.min.js locally, update `<script src>` |
| Empty heatmap cells | No data for that combination | Expected — heatmap shows 0 as dark background |
| Table shows no results | All filters active simultaneously | Clear filters one at a time |
| Charts don't resize on tab switch | ECharts needs resize event after display:none→block | Already handled via `setTimeout(() => window.dispatchEvent(new Event('resize')), 50)` |

---

## Related Scripts

| Script | Purpose |
|--------|---------|
| `PYTHON/generate_vault_overview_report.py` | Markdown report (same data, static tables) |
| `PYTHON/generate_benchmark_survey_report.py` | CATEGORIES dict + classify_entry source |
| `PYTHON/consolidate_benchmark_survey.py` | Creates the candidate JSON from agent batches |
| `PYTHON/generate_vault_dashboard_5b.py` | Multi-file dashboard v9 (data.js + split files) |

---

**Version:** 1.1
**Updated:** 2026-02-16
