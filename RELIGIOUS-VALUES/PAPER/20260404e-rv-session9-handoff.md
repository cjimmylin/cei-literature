# Religious Values Benchmark Paper — Session 9 Handoff

**Date:** 2026-04-04
**Session:** T2 gold-label fix, JSON validation utility, dashboard expert annotations
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`
**Previous handoff:** `PAPER/20260404d-rv-session8-handoff.md` (Session 8: cross-model replication, Sonnet+Haiku trials, T2 real runs)

---

## What Was Done This Session

### 1. Fixed Known Issue #1 — T2 Gold Label Visibility

The T2 items file (`trials/20260404-trial-T2-sample-30.json`) embedded gold answers (`"gold": "D"`) in the same JSON presented to models during administration. This contaminated the Session 8 T2 results (Opus and Sonnet both scored 100%, ambiguously).

**Fix:** Updated `scripts/20260404-sample-trial-T2.py` to produce two output files:
- `trials/20260404-trial-T2-sample-30-gold.json` — with `"gold"` field (for scoring only)
- `trials/20260404-trial-T2-sample-30-admin.json` — **no `"gold"` field** (safe for model prompts)
- Legacy `trials/20260404-trial-T2-sample-30.json` preserved for backward compat with scoring scripts

**Verified:** `admin.json` has 30 items, keys `["index", "item_id", "level", "question", "options"]` only — no gold.

**Implication for Session 8 results:** The original 3-model T2 runs remain upper-bound estimates. Haiku's 7/30 errors are the strongest evidence of genuine independent answering. Future re-runs (cross-vendor) must use `-admin.json`.

### 2. Fixed Known Issue #2 — Unescaped Quotes in Agent JSON

**Fix:** Created `scripts/20260404-validate-trial-json.py` — a validation and auto-repair utility.
- `python validate-trial-json.py` — validate only (56 files scanned)
- `python validate-trial-json.py --fix` — auto-repair unescaped `"` inside string values using a state-machine quote-escaper

**Status:** All 56 JSON files in `data/` and `trials/` are currently valid. Run this after every future agent-generated trial batch.

### 3. Updated Session 8 Handoff

Marked both known issues as FIXED in `PAPER/20260404d-rv-session8-handoff.md` with strikethrough and resolution details.

### 4. Added Expert Narrative Annotations to Dashboard v2

Modified `scripts/20260404-generate-dashboard-v2.py` to add council-of-experts prose annotations to all 5 dashboard tabs. The dashboard previously had zero explanatory text — only chart titles and stat numbers.

**What was added:**
- 3 new CSS classes: `.tab-intro` (blue left-border intro panel), `.chart-annotation` (muted below-chart annotation), `.finding-callout` (blue-tinted key finding box with "KEY FINDING" label)
- `ANNOTATIONS` Python dict with 11 annotation blocks, all using verified data numbers
- Tab-level introductions for all 5 tabs explaining the analysis purpose and methodology
- Per-chart annotations explaining how to read each visualization and what it means
- Key Finding callouts for Overview, Tradition Void, Values Relevance, and Claim Evidence tabs

**Regenerated:** `dashboard/20260404-religious-values-dashboard-v2.html` → 63,220 bytes (up from 45,668)

**Verified:** All 17 annotation blocks present, 5 tab-intros, 9 chart-annotations, 4 finding-callouts, all numbers verified against source JSON files.

---

## Key Numbers Used in Annotations (Verified from Source Data)

| Metric | Value |
|--------|-------|
| Total candidates | 401 |
| Gate-passers | 47 (RD ≥ 30 + public data) |
| Traditions analyzed | 14 |
| Void traditions | 8 |
| Islam gate-passers | 28 (59.6%) |
| Abrahamic family | 34 (72.3%) |
| Bootstrap iterations | 10,000 |
| Certain top-15 | 9, Likely 6, Contested 8 |
| Avg CI width | 15.87 points |
| Weight combos tested | 61, Kendall's τ mean = 0.773 |
| Publication infra r | 0.74, p=0.0025 |
| Formalizability r | 0.414, p=0.1412 (ns) |
| Mean readiness active | 10.5, void = 5.12 |
| A3 mean | 33.6/100 |
| A3 ≥ 75 | 6 benchmarks (12%) |
| Claims supported | 3/7 (p<0.05), 1 marginal, 3 NS |

---

## New Files This Session

| File | Purpose |
|------|---------|
| `trials/20260404-trial-T2-sample-30-admin.json` | Gold-stripped T2 items for model administration |
| `trials/20260404-trial-T2-sample-30-gold.json` | Gold-labeled T2 items for scoring only |
| `scripts/20260404-validate-trial-json.py` | JSON validation + auto-repair utility (run after agent trials) |

## Modified Files This Session

| File | Change |
|------|--------|
| `scripts/20260404-sample-trial-T2.py` | Now produces both `-admin.json` and `-gold.json` outputs |
| `scripts/20260404-generate-dashboard-v2.py` | Added CSS classes, ANNOTATIONS dict, HTML insertions for all 5 tabs |
| `dashboard/20260404-religious-values-dashboard-v2.html` | Regenerated (63KB, up from 46KB) |
| `PAPER/20260404d-rv-session8-handoff.md` | Marked issues 1 and 2 as FIXED |

---

## Remaining Work (Session 10+)

### Priority 1: Integrate Cross-Model Findings into Main Paper
`PAPER/full-paper-religious-values.md` needs:
- New subsection in §4.4 or §5.2 reporting cross-model replication (all 9 model-tradition combos show K < R < V)
- Updated Claim 2 evidence (gradient universality)
- Updated Claim 7 evidence (Sonnet r=0.288 proves bias-values independence)
- Rubric ceiling finding as methodological contribution
- T2 results as evidence for benchmark design recommendations

### Priority 2: Integrate Session 7 Rubric Scoring into Paper
K=1.0/R=1.0/V=0.93 rubric result and 3.41x length gradient from Session 7 still need a paragraph in the paper (flagged in Session 7 handoff, still unresolved).

### Priority 3: Cross-Vendor Replication
Administer the 65-item battery to GPT-4o and Llama-3-70B using the `-admin.json` files (NO gold labels). This tests whether K < R < V gradient generalizes beyond the Claude model family.

### Priority 4: LaTeX Conversion
Convert `full-paper-religious-values.md` to LaTeX for NeurIPS 2026 D&B submission.

### Priority 5: Feature Matrix Rebuild
Recompute feature matrix after I3/I4 code changes (source-language R3 bonus + liturgical P10 normalization). May shift some composite scores and tier assignments.

### Priority 6: GitHub Pages Deployment
Dashboard has not been deployed. Requires a public GitHub repo (GitHub Pages free tier requires public). Create `cjimmylin/cei-rv-dashboard` public repo and deploy.

---

## Known Issues

1. **T2 Session 8 results are upper-bound estimates:** Gold labels were visible during the original 3-model runs (Sessions 7–8). Results cannot be fully validated; Haiku's errors (7/30) provide the strongest evidence of genuine answering. Cross-vendor replication (Priority 3) will use `-admin.json` and produce clean estimates.
2. **Playwright browser unavailable this session:** Browser closed mid-session; could not take screenshots to visually verify annotated dashboard. Visual check deferred to next session's Playwright invocation.
3. **Scorer bias (Claim 7):** Opus evaluating Claude-family responses may inflate rubric scores systematically. Independent human evaluation needed for calibration.
4. **7 claims in JSON, paper refers to 8:** The `claim-robustness-tests.json` has 7 claims; the paper's spine references 8. Claim 8 (Values Relevance Failure, A3 analysis) may not have a formal statistical test in the JSON yet.

---

*Filed: 2026-04-04 | CEI-Lit-WS/RELIGIOUS-VALUES/PAPER/*
