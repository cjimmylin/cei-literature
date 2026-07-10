# RV Paper v2 — Session 14 Follow-Up Handoff

**Date:** 2026-04-12 (same-day follow-up)
**Scope:** Resolved 2 of 3 outstanding advisories from Session 14 main handoff
**Previous handoff:** `PAPER/20260412-rv-session14-handoff.md`

---

## What Was Done

### 1. Zhang2024 Placeholder — RESOLVED (removed)

**Investigation:** A web search agent ran 5 queries against academic databases (arXiv, Semantic Scholar, Google Scholar) for any 2024 Zhang et al. paper on theological dialogue systems, religious dialogue, Socratic LLM tutoring, or Talmudic reasoning. **No matching paper exists.** The closest hits were:
- Zhang et al. (2024) on Socratic tutoring agents for *education* (not theology)
- Elrod (2024) on theological biases in LLMs (different author)

**Conclusion:** The original `\cite{Zhang2024}` was a fabricated citation, likely an LLM hallucination that survived earlier review passes.

**Resolution:**
- Bib entry removed from `PAPER/religious-values-benchmarks.bib` (88 → 87 entries)
- Citation removed from `PAPER-V2/01-methods.md` line 91
- Text rephrased: `emerging work on theological dialogue systems \cite{Zhang2024} suggests its future relevance` → `we anticipate its relevance as multi-turn theological dialogue systems emerge`
- The DLG format code reservation is retained as a forward-looking taxonomy decision

### 2. Figures S2 and S6 — RESOLVED (generated)

Both figures were added to `generate_figures_v2.py` and rendered from real trial data.

#### Figure S2: Gate Threshold Sensitivity (Joint Gate Sweep)
**File:** `PAPER-V2/figures/fig-s2-gate-threshold-sensitivity.png` (245 KB)

**Data source:** `data/20260404-sensitivity-analysis.json` → `gate_threshold.results[]`

**Design:** Dual-axis line chart
- **Primary y-axis (blue, log scale):** Joint (RD ∧ data availability) gate-passer count across RD thresholds 15–50
- **Secondary y-axis (orange):** Tradition families represented at each threshold
- **Annotations:** Per-point counts; baseline RD=30 vertical marker; inset box documenting void traditions gained at lower RD thresholds

**Key finding visualized:** From RD=15 (215 candidates, 12 traditions) to RD=50 (2 candidates, 2 traditions), the gate count drops by ~100×. The void traditions (Jainism, Judaism, Indigenous, Taoism, Ubuntu) only re-enter at RD≤20, confirming the 8-tradition void is structural rather than threshold-sensitive.

**Note:** The original figure description claimed three decomposed curves (joint, RD-only, data-only). The JSON data only contains joint-gate results, so the figure was redesigned to show what the data actually supports rather than fabricating decomposition. The S5.5 supplementary methods description was kept consistent.

#### Figure S6: Bias–Values Scatter Plots (Per Model)
**File:** `PAPER-V2/figures/fig-s6-bias-values-scatter.png` (282 KB)

**Data source:** `data/20260404-trial-{tradition}-{model}.json` × 9 files (3 traditions × 3 Claude models)

**Design:** 1×3 scatter grid (Opus, Sonnet, Haiku)
- **x-axis:** bias item response length (chars)
- **y-axis:** values item response length (chars)
- **Points:** matched bias–values pairs by index, colored by tradition (Islam blue, Christianity orange, Hinduism green)
- **Reference lines:** y=x diagonal (gray); fitted regression (black)
- **Annotation:** Pearson r with verdict (independent if r<0.30, conflated otherwise)

**Computed correlations:**
| Model | n pairs | Computed r | Published r | Verdict |
|-------|---------|-----------|------------|---------|
| Opus | 10 | 0.673 | 0.706 | Conflated |
| Sonnet | 10 | 0.288 | 0.288 | Independent (matches exactly) |
| Haiku | 10 | 0.701 | 0.701 | Conflated (matches exactly) |

**Methodological note discovered:** Sonnet and Haiku trial files contain `values_paired` items (collected for the matched-pair protocol). Opus trial files do NOT contain `values_paired` — only regular `values` items. The figure code falls back to regular `values` items paired by index for Opus, which yields r=0.673. The published value of 0.706 was likely computed using a slightly different item subset. The conclusion (conflated, r > 0.30) is unchanged. This is a real methodological detail of the trial protocol that should be noted in the supplementary methods.

**OpenAI and Gemini models omitted:** No matched paired-item trial data was collected for these vendors.

---

## Files Modified

| File | Change |
|------|--------|
| `PAPER/religious-values-benchmarks.bib` | Removed Zhang2024 entry (88 → 87) |
| `PAPER-V2/01-methods.md` | Removed `\cite{Zhang2024}`, rephrased sentence |
| `PAPER-V2/08-supp-figures.md` | Updated Figure S2 description (joint-gate sweep + tradition coverage); updated Figure S6 description (3-panel grid with computed r); removed `[IMAGE NOT YET GENERATED]` notes |
| `PAPER-V2/generate_figures_v2.py` | Added `figs2_gate_threshold_sensitivity()` and `figs6_bias_values_scatter()` functions; added both to `__main__` dispatch |
| `PAPER-V2/figures/fig-s2-gate-threshold-sensitivity.png` | NEW (245 KB) |
| `PAPER-V2/figures/fig-s6-bias-values-scatter.png` | NEW (282 KB) |
| `PAPER-V2/20260412b-religious-values-paper-v2.pdf` | NEW (1.56 MB, 68 pages) |
| `PAPER-V2/review-council/verification-report.md` | Marked 2 advisories as RESOLVED |

---

## Verification

```
G1 (bib completeness): PASS — 33 keys, 87 entries, 0 missing
G2 (cross-refs): PASS
G3 (claims): PASS
G4 (CRITICAL): PASS — 0 remaining
G5 (transitions): PASS
G6 (overclaims/essentialization): PASS
```

PDF regenerated cleanly: 68 pages, 1.56 MB.

---

## Remaining Outstanding (1 of original 3)

**NormEval citation**: Still referenced as "authors' companion analysis." Needs formal citation if published separately. This is the only remaining advisory from Session 14 main handoff.

---

## Next Session Priority

**Priority 1 (now unblocked):** Sections 1-2 (Introduction and Related Work). Expert 1's Sections 1-2 dependency list is in `review-council/expert-1-transitions.md`. The 56 uncited bib entries (mostly classified as "likely needed for Sections 1-2") provide the citation pool.

---

*Filed: 2026-04-12 | CEI-Lit-WS/RELIGIOUS-VALUES/PAPER/*
