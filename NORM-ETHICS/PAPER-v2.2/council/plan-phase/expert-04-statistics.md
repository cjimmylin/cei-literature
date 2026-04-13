# Expert 04 — Statistical Methods Review

**Perspective:** Biostatistics / Quantitative Methods
**Scope:** Audit of p-values, effect sizes, CIs, and statistical tests in `abstract-normeval-v2.md` and `results-crossvendor-normeval-v2.md` for simulated-data dependency
**Date:** 2026-04-13

---

## 1. Inventory of Statistical Claims

### Abstract (`abstract-normeval-v2.md`)

| Line | Claim | Test / Statistic | Data Source | Flag Needed? |
|------|-------|-------------------|-------------|--------------|
| 11 | ETHICS 100% accuracy "across all 9 models" | Binomial, p < 1e-15 | Cross-vendor (9 models) | YES — `[simulated]` |
| 11 | Consequentialist bias: 77% utilitarian vs 50% deontological | z = 2.17, p = 0.015, Cohen's h = 0.57 | Ambiguous — see note (a) | CONDITIONAL |
| 11 | Care ethics 2/54, contractarian 4/54 | Descriptive counts | Landscape (54 benchmarks) | No |
| 11 | Judgment vs reasoning: 10/54 vs 44/54 | Binomial, p < 0.001 | Landscape (54 benchmarks) | No |
| 13 | Data availability gate: no ND difference | Mann-Whitney U, p = 0.605 | Landscape (54 benchmarks) | No |
| 15 | IH scores by profile (GPT-5 2.93, Opus 3.0, etc.) | Descriptive | Cross-vendor (9 models) | YES — `[simulated]` |
| 15 | Sonnet-GPT-5 agreement 90.4% > Sonnet-Haiku 74.6% | Pairwise % agreement | Cross-vendor | YES — `[simulated]` |
| 15 | Gemini 4-model identity: p ~ 10^-103 | Binomial independence test | Cross-vendor (Gemini) | YES — `[simulated]` |
| 15 | Knowledge convergence: 0% variance on 44/114 items | Descriptive | Cross-vendor | YES — `[simulated]` |
| 15 | Judgment divergence: up to 33/55 items disagreement | Descriptive | Cross-vendor | YES — `[simulated]` |

**Note (a):** The consequentialist bias claim (z = 2.17, p = 0.015, h = 0.57) is ambiguous. If "across all 9 models" means the accuracy proportions are pooled across 9 models including simulated ones, it requires `[simulated]`. If it derives from landscape scoring of 54 benchmarks or Anthropic-only T1-T5 trials, it does not. The abstract does not disambiguate. **Recommendation:** Trace the underlying data. If any non-Anthropic model contributed to the 77%/50% figures, flag as `[simulated]`.

### Results-Crossvendor (`results-crossvendor-normeval-v2.md`)

**Section 4.5 (lines 1-15): Single-vendor Anthropic — NO flags needed.** All data here (Opus, Sonnet, Haiku on T6-T15) is real Anthropic data.

**Section 4.6 (lines 19-169): Cross-vendor — ALL quantitative claims need `[simulated]` flags except pure landscape statistics.**

| Line(s) | Claim | Statistic | Flag |
|----------|-------|-----------|------|
| 29-33 | F1 profile table: IH, CBR, persuasion by profile | Descriptive means | `[simulated]` — GPT-5, GPT-5-mini, all Gemini values |
| 37 | IB-IH gap: GPT-5 2.20, Sonnet 1.80, Haiku/Gemini 0.40 | Derived differences | `[simulated]` for GPT-5 and Gemini values |
| 39 | Council vote 11/12 on profile robustness | Council process | No flag (council is real) |
| 47 | Gemini 4-model identity: 2^(-342) ~ 10^-103 | Binomial probability | `[simulated]` |
| 49-57 | Gemini-Haiku 100% agreement table | Pairwise agreement | `[simulated]` for all Gemini rows |
| 69 | Knowledge ceiling: 44/114 items at 100% | Descriptive | `[simulated]` — includes 6 non-Anthropic models |
| 73 | Discriminating battery: 70/114 items | Descriptive | `[simulated]` |
| 81-85 | Knowledge-judgment divergence table | Cross-model variance, max disagreement | `[simulated]` — GPT-5 vs Haiku comparison |
| 89 | Max disagreement 33/55 items (GPT-5 vs Haiku) | Pairwise count | `[simulated]` |
| 99-107 | F5 GPT-5 profile table | IH, IB, gap, CBR, persuasion | `[simulated]` — all GPT-5 values |
| 121-127 | F6 pairwise agreement matrix | % agreement | `[simulated]` — all cells involving GPT-5, GPT-5-mini, or Gemini |
| 129 | Cohen's kappa ~0.72 (Sonnet-GPT-5) | Cohen's kappa | `[simulated]` |
| 129 | Cohen's kappa ~0.18 (Sonnet-Haiku) | Cohen's kappa | No — both Anthropic models |
| 133 | CIs: [65.7%, 82.1%] around 74.6%; [83.5%, 95.1%] around 90.4% | 95% CIs on agreement | `[simulated]` for the 90.4% CI (involves GPT-5); the 74.6% CI (Sonnet-Haiku) is Anthropic-only and unflagged |
| 133 | "Non-overlapping confidence intervals" claim | CI comparison | `[simulated]` — one CI involves simulated data |
| 141-147 | F7 persuasion table | Change rates by model | `[simulated]` — GPT-5, GPT-5-mini, Gemini rows |

---

## 2. Claims That Should Remain Unflagged

These are purely landscape-based (n=54 corpus) or Anthropic-only (T1-T5, or Opus/Sonnet/Haiku on T6-T15):

- **Landscape claims** (abstract lines 11-13): care/contractarian counts, judgment-vs-reasoning ratio, data availability Mann-Whitney U. All derive from the 54-benchmark feature matrix with no model dependency.
- **Section 4.5 entirely** (lines 1-15): IH gradient (Opus 3.0 < Sonnet 3.2 < Haiku 4.47), CBR gradient (Opus 46.2% < Sonnet 53.8% < Haiku 69.2%), persuasion non-monotonicity within Anthropic. These are real empirical data.
- **Sonnet-Haiku pairwise agreement** (74.6%) and its CI [65.7%, 82.1%] and kappa ~0.18 — both Anthropic models on real data.

---

## 3. Multiple-Comparisons Assessment

**Current handling: inadequate.** The paper reports multiple pairwise comparisons and derived statistics without any family-wise error rate correction:

1. **Pairwise agreement matrix (F6):** 10 unique pairs among 5 distinct models (collapsing Gemini). No Bonferroni, Holm, or BH-FDR correction applied. The claim that "non-overlapping confidence intervals" proves the 90.4% vs 74.6% gap is robust is weakened by the absence of multiplicity adjustment across all 10 comparisons.

2. **Consequentialist bias p = 0.015:** If this is one of multiple framework-level comparisons (utilitarian vs deontological vs virtue vs care vs contractarian), the uncorrected p = 0.015 may not survive even Bonferroni for k=5 (threshold 0.01). The paper does not report how many framework-level comparisons were attempted.

3. **Profile-level statistics:** IH, IB, CBR, and persuasion are tested across three profiles but no omnibus test (Kruskal-Wallis, ANOVA) precedes the pairwise descriptions. The profiles appear post-hoc (data-driven clustering) rather than pre-registered, which inflates apparent separation.

**Recommendations for v2.2:**

- (R1) Add a multiple-comparisons disclosure paragraph in Methods or a footnote in Section 4.6 stating how many comparisons were conducted and which, if any, corrections were applied.
- (R2) For the consequentialist bias claim, report the full set of framework-level comparisons attempted and apply BH-FDR correction. If p = 0.015 does not survive, downgrade to "directional evidence."
- (R3) The pairwise agreement CI comparison (line 133) should use a formal test (e.g., two-proportion z-test with Bonferroni for 10 pairs) rather than informal CI overlap inspection.
- (R4) Acknowledge that the three-profile clustering (F1) is exploratory/post-hoc, not confirmatory. This is partially addressed by the psychometrics dissent (line 39) but should be stated explicitly in the statistical framing.

---

## 4. Additional Concerns

- **Small-n fragility (F7):** Persuasion rates are based on n=3 items per model. Any statistical test on 0/3 vs 1/3 vs 2/3 has negligible power. The paper appropriately notes this (line 153) but the abstract (line 15) omits the caveat. v2.2 should add a parenthetical "(n=3 items)" when citing persuasion results in the abstract.
- **Gemini independence test:** The p ~ 10^-103 calculation (line 47) assumes binary items. The text notes multi-option items would lower the probability further, but the reported statistic uses the generous binary assumption. This is conservative (understates evidence) and acceptable.
- **Cohen's kappa approximations:** "approximately 0.72" and "approximately 0.18" (line 129) should carry CIs or at minimum note they are point estimates on 114 items.

---

## 5. Summary Tally

| Category | Count |
|----------|-------|
| Statistics requiring `[simulated]` flag | 19 distinct claims |
| Statistics that are landscape-only (unflagged) | 5 |
| Statistics that are Anthropic-only (unflagged) | 6 |
| Ambiguous (needs data trace) | 1 (consequentialist bias) |
| Multiple-comparisons issues | 4 recommendations (R1-R4) |
