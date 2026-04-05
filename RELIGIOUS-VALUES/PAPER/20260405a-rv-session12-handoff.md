# Religious Values Benchmark Paper -- Session 12 Handoff

**Date:** 2026-04-05
**Session:** Resolve 5 known issues (methodological caveats, Claim 8, side-by-side layout)
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`
**Previous handoff:** `PAPER/20260405-rv-session11-handoff.md` (Session 11: dashboard v4/v5, multi-vendor + UX council)

---

## What Was Done This Session

### 1. Claim 8 Formalized (Values Relevance Failure)

Added a formal statistical test for "Values Relevance Failure" -- previously described qualitatively in Section 5.3 but absent from the claims JSON and robustness battery.

**Statistical results** (from 16 assessed gate-passers' A3 values relevance scores):
- Mean A3 = 30.0/100 (sd=16.2), significantly below midpoint
- One-sample t-test: t=-4.93, p=0.000181, Cohen's d=-1.23 (large effect)
- Wilcoxon signed-rank: W=5.0, p=0.00061
- Binomial (A3>=50): 3/16, p=0.011
- Binomial (A3>=75): 0/16, p=0.000015

This is now the **strongest result** in the robustness battery. Paper updated from "seven claims" to "eight claims", with 4/8 now supported (previously 3/7).

### 2. Three Methodological Caveats Added

Added limitations to paper Section 5.7 and caveat badges to dashboard Cross-Vendor tab:

1. **T2 Blinding** -- Original 3-model T2 trials (Opus/Sonnet/Haiku) administered with gold labels visible. Scores are upper-bound estimates. Cross-vendor trials used blind protocol.
2. **Scorer Bias** -- All rubric scoring by Claude Opus 4.6, including Claude-family model responses. Same-vendor scoring may inflate rubric scores. Cross-vendor relative comparisons remain valid.
3. **Gemini Data Provenance** -- Gemini results collected via backfilled protocol with template-based extraction, not interactive API. 0.0 rubric scores may partly reflect methodological difference.

### 3. Dashboard v6 -- Side-by-Side Layout + Caveats

**Generator:** `scripts/20260405-generate-dashboard-v4.py` (updated, ~2,750 lines)
**Output:** `dashboard/20260405-religious-values-dashboard-v6.html` (132KB)
**Deployed:** `cjimmylin.github.io/cei-rv-dashboard/` (v6 live, commit `0cf68f1`)

#### Layout Changes
- Side-by-side chart+annotation layout (col-md-7/col-md-5) on Tabs 2, 3, 4, 5
- `.annotation-sidebar` CSS with sticky positioning
- Collapses to single-column on mobile (<768px) automatically

#### Caveat Badges
- `.caveat-badge` CSS: amber/gold border with warning icon
- 3 badges in Cross-Vendor tab annotations (T2, rubric, Gemini)
- Visible when annotation "Read more" is expanded

#### Claim 8 Integration
- Bar chart: C8 green bar (p<0.001)
- Claim card: "Values relevance failure: most benchmarks do not actually test religious values" SUPPORTED
- Cross-Vendor Claim Validation table: C8 row with "Strongest result (d=-1.23)"
- Key Findings bullet: "4 of 8 Claims Supported"
- Tab subtitle: "8 statistical tests"
- Summary table: "4 of 8 (p<0.05)"

---

## Dashboard Version History This Session

| Version | Size | Charts | Key Change |
|---------|------|--------|-----------|
| v5 (start) | 128KB | 16 | Previous session's council UX output |
| v6 | 132KB | 17 | Claim 8 + 3 caveats + side-by-side layout |

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| v6 generator | `scripts/20260405-generate-dashboard-v4.py` | Dashboard generator (updated) |
| v6 HTML | `dashboard/20260405-religious-values-dashboard-v6.html` | v6 output (132KB, deployed) |
| Claims JSON | `data/20260404-claim-robustness-tests.json` | 8 claims with statistical tests |
| Paper | `PAPER/full-paper-religious-values.md` | Updated Sections 5.6 and 5.7 |
| Live dashboard | `cjimmylin.github.io/cei-rv-dashboard/` | GitHub Pages (v6) |

---

## Remaining Work (Session 13+)

### Priority 1: Integrate Cross-Model Findings into Main Paper
`PAPER/full-paper-religious-values.md` needs:
- New subsection reporting cross-model replication (K<R<V universality across 9 models)
- Updated Claim 2 evidence (gradient universality)
- Updated Claim 7 evidence (Sonnet r=0.288 proves bias-values independence)
- Rubric ceiling finding as methodological contribution

### Priority 2: Session 7 Rubric Scoring Integration
K=1.0/R=1.0/V=0.93 rubric result and 3.41x length gradient still need a paragraph in the paper.

### Priority 3: Cross-Vendor Replication (GPT-4o, Llama)
Administer the 65-item battery + T2 to non-Claude, non-Gemini models.

### Priority 4: LaTeX Conversion
Convert `full-paper-religious-values.md` to LaTeX for NeurIPS 2026 D&B submission.

### Priority 5: Feature Matrix Rebuild
Recompute after I3/I4 code changes (source-language R3 bonus + liturgical P10 normalization).

---

## Known Issues

1. **T2 Session 8 results remain upper-bound estimates** -- Now disclosed in paper and dashboard, but not yet re-administered under blind conditions.
2. **Scorer bias not independently validated** -- Disclosed but not resolved; would require scoring by a non-Claude model.
3. **Gemini data not replicated with interactive API** -- Disclosed as preliminary; requires verified API access.
4. **Claim 8 sample size (n=16)** -- Only 16 gate-passers had complete A3 assessment. Paper's earlier figure of 33.6 comes from broader assessment; formal test uses the 16 with complete scoring.
5. **Side-by-side layout not applied to Tab 6 (Cross-Vendor)** -- Tab 6 already used side-by-side for some chart pairs; adding more would over-compress the rubric heatmap.

---

*Filed: 2026-04-05 | CEI-Lit-WS/RELIGIOUS-VALUES/PAPER/*
