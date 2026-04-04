# Methods: T2 Benchmark Blinding, JSON Validation, and Dashboard Annotation (Session 9)

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`

---

## Data and Materials

**T2 Items Source:**
- `data/20260404-Task1_MCQ_Test_gold_labels.csv` — 1,000 Islamic inheritance law (fara'id) items in Arabic, stratified into 500 Beginner and 500 Advanced items. CSV encoded as UTF-8 with BOM. Columns: `id_question`, `question`, `option1`–`option6`, `label` (gold answer A–F), `level`.
- Sampled subset: 30 items (15 Beginner, 15 Advanced), fixed random seed (42), stored as `trials/20260404-trial-T2-sample-30-gold.json`.

**Trial and Data Files:**
- 56 JSON files across `data/` and `trials/` directories validated for syntactic correctness.
- Dashboard generator: `scripts/20260404-generate-dashboard-v2.py` (975 lines pre-session, ~1,100 lines post-session).
- Source data for annotations drawn from 7 pre-existing JSON files: `sensitivity-analysis.json`, `void-factor-taxonomy.json`, `claim-robustness-tests.json`, `claude-assessment-batch{1,2}.json`, `religious-benchmark-feature-matrix-v2.json`, `correlation-matrix.json`.

---

## Procedure

### T2 Items Blinding

The sampling script `scripts/20260404-sample-trial-T2.py` was modified to produce two output files from the same stratified sample:

1. **Gold file** (`*-gold.json`): Contains the `"gold"` field with the correct answer letter (A–F) for each item. This file is intended exclusively for automated scoring after model responses are collected.

2. **Administration file** (`*-admin.json`): Contains identical item content (`index`, `item_id`, `level`, `question`, `options`) but omits the `"gold"` field entirely. This file is the only authorized input for model administration; it prevents gold label contamination in the model's context window.

Both files are derived from the same stratified sample (`random.seed(42)`, 15 Beginner + 15 Advanced) and maintain identical item ordering. A legacy file (`*-30.json`) is maintained as a copy of the gold file for backward compatibility with existing scoring scripts.

The blinding approach follows the psychometric principle of separating answer keys from test forms: models are administered item forms without embedded answers, and scoring is performed post-hoc by joining responses against the gold file on `item_id`.

### JSON Validation Utility

A state-machine-based JSON validation and repair utility was created at `scripts/20260404-validate-trial-json.py`. The utility:

1. Scans all `.json` files in `data/` and `trials/` directories.
2. Attempts `json.loads()` on each file; reports "OK" or logs the `JSONDecodeError` with position.
3. When invoked with `--fix`, attempts automated repair of unescaped double-quote characters inside string values using a character-by-character state machine that tracks string boundaries and distinguishes structural delimiters (quotes followed by `,`, `:`, `}`, or `]`) from embedded unescaped quotes (quotes followed by other characters).
4. Re-validates the repaired text before writing; if repair fails, reports and leaves the file unchanged.

The repair heuristic addresses the most common failure mode of agent-generated JSON: the Write tool does not invoke `json.dumps()` and therefore does not escape quotes inside string values when composing long JSON by hand.

### Dashboard Narrative Annotation

The dashboard generator was modified to embed static expert prose annotations in all five tabs of the output HTML file. The implementation strategy:

1. **CSS extension:** Three new utility classes were appended to the inline `<style>` block: `.tab-intro` (blue left-border panel for tab-level introductions), `.chart-annotation` (muted gray annotation placed below chart containers), and `.finding-callout` (blue-tinted box with uppercase "KEY FINDING" prefix for primary takeaways). All CSS uses existing CSS custom properties from the dark theme (Bootstrap 5.3.3 with GitHub-dark palette).

2. **Annotation dictionary:** A Python dictionary `ANNOTATIONS` mapping 11 string keys to HTML string values was inserted between the JS data serialization block and the HTML template definition in the generator. Annotations are stored as plain Python strings (not f-strings) to avoid brace-escaping conflicts with the surrounding f-string template.

3. **Template insertion:** Annotation blocks were inserted at specific positions within each tab's HTML template using `{ANNOTATIONS["key"]}` interpolation. Critically, all annotation divs were placed **outside** `.chart-container` elements to avoid interference with ECharts DOM resize handlers.

4. **Content grounding:** All numerical claims in the annotations were verified against the source JSON files before inclusion. The verified values included: 401 total candidates, 47 gate-passers, 8 void traditions, 28 Islam gate-passers (59.6%), bootstrap CI width of 15.87 points, 9 certain/6 likely/8 contested top-15 members, publication infrastructure correlation r=0.74 (p=0.0025), formalizability correlation r=0.414 (p=0.1412, ns), mean readiness 10.5 (active) vs. 5.12 (void), mean A3=33.6/100, A3≥75 in 6 benchmarks (12%), and claims results (3/7 supported, 1 marginal, 3 NS).

The annotation voice adopts a council-of-experts posture: assertions are made without individual hedging because they represent consensus findings backed by pre-registered statistical tests. Null results are reported with equal prominence to positive findings.

---

## Analysis

No new statistical analyses were performed in this session. The annotation content draws on analyses from Sessions 5–8: chi-square tests (tradition asymmetry), binomial tests (knowledge-reasoning conflation, data availability), Spearman/point-biserial correlations (structural predictors), logistic regression (multivariate prediction), Dirichlet-weighted bootstrap resampling (ranking robustness), and weight perturbation analysis (sensitivity).

---

## Computational Environment

- Python 3.x (system interpreter, `which python3` → `/opt/homebrew/bin/python3`)
- Standard library only for blinding and validation scripts: `csv`, `json`, `random`, `pathlib`, `sys`
- Dashboard generator dependencies: `json`, `math`, `pathlib` (standard library); output loaded by browser via CDN (Bootstrap 5.3.3, ECharts 5.5.0, Google Fonts)
- HTTP server for dashboard preview: `python3 -m http.server 8765`

---

## Limitations and Decisions

**T2 blinding:**
- The original 3-model T2 runs (Sessions 7–8) used the unblinded items file. Those results cannot be retroactively cleaned and should be reported as upper-bound estimates in the paper. Haiku's 7/30 error rate provides the strongest evidence of genuine independent answering under contaminated conditions.
- The `-admin.json` blinding approach prevents future contamination but does not resolve the ambiguity in the existing Opus and Sonnet T2 scores.

**JSON repair heuristic:**
- The state-machine repair approach is adequate for the most common failure mode (unescaped quotes in response strings) but is not a general JSON repair tool. It may fail on deeply nested structures or other malformation types. Files that fail repair are left unchanged and flagged for manual inspection.

**Annotation content:**
- Annotations are static strings hardcoded in the generator. If source data changes (e.g., after feature matrix rebuild, Priority 5), the annotation text will not auto-update and must be manually revised.
- The 7 claims in `claim-robustness-tests.json` are annotated as "7 claims" in the dashboard, which may diverge from the paper's prose if Claim 8 (Values Relevance Failure) is later added as a formal test.
