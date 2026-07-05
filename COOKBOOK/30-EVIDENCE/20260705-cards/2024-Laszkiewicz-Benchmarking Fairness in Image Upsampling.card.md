---
stem: "2024-Laszkiewicz-Benchmarking Fairness in Image Upsampling"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [design-space, validity-psychometrics, pluralism-aggregation]
task_format: "generative"
scoring_type: "classifier"
dataset_size: 1400
dataset_construction: "scraped"
languages: [n/a]
models_tested: [PULSE, pSp, fair-pSp, "Posterior Sampling", DDRM]
headline_numbers: ["No method produces statistically fair and diverse results; Pearson chi-squared rejects PRDP=U and PPR=U for all models even on FairFace (p.8)", "UnfairFace ~20k samples, >80% labeled White (p.5)", "Test set 1400 images = 200 per race x 7 races (p.5)", "FairFace race classifier ~71% accuracy (p.10)"]
---
## 1. Gist
This FAccT'24 paper builds a benchmarking framework for the fairness and diversity of *conditional* generative models, instantiated on face image upsampling (super-resolution). It contributes (a) a family of divergence-based fairness metrics that operationalize Jalal et al.'s representation-demographic-parity (RDP), proportional-representation (PR) and conditional-proportional-representation (CPR) definitions, and (b) UnfairFace, a subset of FairFace resampled to mimic the racial skew of common web-scraped datasets (>80% White). It matters for values-alignment benchmarking not because it touches LLMs (it does not) but because it is a rigorous template for turning abstract fairness *definitions* into statistically testable, plug-in-estimable metrics with hypothesis tests — the same move a values benchmark needs when converting a normative property (parity across groups/cultures/religions) into a measurable, discriminating score. Its central empirical finding is that no upsampling method is statistically fair, and that dataset skew, not just architecture, drives measured unfairness.

## 2. Benchmark/eval design features
Constructs measured: (i) performance — expected reconstruction loss (LPIPS, DSSIM), referenceless quality (NIQE, blur index), and expected attribute-reconstruction loss (race classifier 0-1 and cosine); (ii) fairness — ΔRDP and ΔPR as divergences (Pearson chi-squared and Chebyshev) between an induced class distribution and the uniform distribution; (iii) diversity — ΔUCPR, measuring whether an *uninformative* low-res input yields group-balanced outputs. Answer space: generated high-res images, scored via a pretrained race classifier over 7 race categories. Key formal result (Corollary 3.1): a model satisfies RDP/PR/UCPR iff the corresponding Δ = 0, giving each metric a clean zero-point.

## 3. Task format & example item
n/a — the "items" are low-resolution 16x16 (and uninformative 4x4) face images fed to upsampling models; there is no textual prompt. Figures 1-2 show LR inputs and reconstructions by race (p.1, p.6).

## 4. Scoring / grading methodology
Automated. A pretrained FairFace race classifier labels each generated image; losses (Eq. 4-5) feed plug-in estimators of PRDP/PPR/PUCPR (Eq. 6, 10). Divergence to uniform is computed via chi-squared (Eq. 8) and Chebyshev/max-violation (Eq. 9). Statistical tests: Wilcoxon signed-rank for UFF-vs-FF performance differences (with Anderson-Darling normality pre-check, Pearson chi-squared for the binary race loss), and Pearson chi-squared at alpha=0.05 to test the null that PRDP/PPR/PUCPR equals uniform (p.7-8).

## 5. Dataset construction & provenance
Base: FairFace (~87k training images, 224x224, 7 approximately uniform race categories) (p.5). UnfairFace: subsampled from FairFace to imitate CelebA's racial distribution, ~20k samples, >80% White (p.5). Test set: first 200 correctly-classified samples per race = 1400 images, balanced (p.5). Images downscaled to 128x128 (nearest power of two) then to 16x16 LR; uninformative conditions built by averaging per-race then downsampling to 4x4 (p.6). Code repo released (github.com/MikeLasz/Benchmarking-Fairness-ImageUpsampling). CC-BY license (p.1).

## 6. Validity evidence
Construct validity is grounded in Corollary 3.1 (metric = 0 iff definition satisfied). Criterion checks use formal hypothesis tests rather than eyeballing confusion matrices (an improvement the authors explicitly claim over prior work). Limitation acknowledged: the race classifier that grounds all measurement is only ~71% accurate on FairFace (p.10); they mitigate by testing only on correctly-classified reals. No inter-rater/human-baseline study; ground-truth race is itself contested (ethics statement, Section 8).

## 7. Saturation / discrimination
Strong discrimination: scores spread widely across methods and training sets. ΔRDP-chi-squared ranges from 0.05 (Posterior Sampling, UFF) to 0.70 (DDRM, UFF), collapsing to ~0.03-0.12 on FairFace (p.8). ΔUCPR-chi-squared spans 0.08-5.67 (p.8). No ceiling: every method fails the fairness null even at best, so headroom remains for all.

## 8. Multiturn / agentic aspects
n/a — single-shot image generation, no interaction, tools, or environment.

## 9. Key numbers
- No method is statistically fair or diverse; chi-squared rejects PRDP=U and PPR=U for all models, even trained on balanced FairFace (p.8).
- UnfairFace: ~20k samples, >80% "White" (p.5).
- Test set: 1400 images, 200 per race x 7 races (p.5).
- DDRM ΔRDP-chi-squared: 0.70 on UnfairFace to 0.05 on FairFace — most volatile to training data (p.8).
- Posterior Sampling ΔRDP-chi-squared: 0.05 (UFF), most robust to data skew (p.8).
- ΔUCPR-chi-squared: PULSE 5.67 (UFF) to 2.43 (FF); DDRM 5.20 to 0.08 (p.8).
- FairFace race classifier ~71% accuracy (p.10).
- 7 uninformative conditions x 100 reconstructions = 700 diversity samples (p.7).

## 10. Pitfalls & limitations
Author-admitted: only 128x128 resolution (vs 1024x1024 for original PULSE) because large HQ datasets lack fairness labels (p.10); race labels are coarse and partition-granularity-dependent (p.10); the grounding classifier is imperfect (~71%); ITA skin-tone estimates were unreliable so were dropped (p.10); models had to be retrained (pretrained CelebA/FFHQ weights transfer poorly), so hyperparameters may be suboptimal (p.10). Seen flaws: pSp/fair-pSp are deterministic and so are excluded from the diversity (UCPR) analysis entirely (p.8), making the diversity leaderboard non-comparable across all methods; the entire fairness signal is mediated by a single classifier, so classifier bias contaminates the metric.

## 11. Novel ideas worth stealing
- **Definition-to-metric with a provable zero-point:** wrap each fairness *definition* in a divergence to a reference distribution such that metric=0 iff the property holds (Corollary 3.1). A values benchmark could define "cultural parity satisfied iff Δ(P_responses || target) = 0."
- **Two divergences per property:** report both chi-squared (ties to a significance test) *and* Chebyshev (interpretable as *maximum* single-group violation). Pairing an aggregate score with a worst-group score is directly reusable for pluralism/aggregation benchmarks.
- **Statistical acceptance test, not a leaderboard number:** run a hypothesis test (chi-squared at alpha=0.05) of "is this model actually fair?" and report reject/accept — a stronger claim than a smaller-is-better rank.
- **Deliberately skewed twin dataset (UnfairFace vs FairFace):** hold the source constant and vary only group balance to isolate *data-driven* vs *architecture-driven* unfairness. Analogue: build parallel balanced/skewed value-corpora to attribute an LLM's cultural bias to training data vs method.
- **Uninformative-input diversity probe:** feed a maximally ambiguous input (averaged, 4x4) where any group answer is equally valid, and measure whether outputs stay balanced — a clean isolation of prior bias from legitimate conditioning. Values analogue: ask value-underdetermined prompts and check response-distribution balance.
- **Filter evaluation set to items the grader classifies correctly** to reduce grader-error leakage into the metric.

## 12. Notable quotes
- "Alarmingly, we find that none of the considered methods produces statistically fair and diverse results." (p.2)
- "fairness is achieved if and only if our fairness violation metrics equal zero" (p.2)
- "even though some methods are more fair than others, the statistical evidence suggests that PRDP != U([k]) and PPR != U([k]), i.e., no method can be considered fair." (p.8)
- "the FairFace race classifier used in our experiments has an average prediction accuracy of around 71%" (p.10)

## 13. UNKNOWN / not in extract
- Full appendix content (pp.12-29): synthetic examples (9.1), per-model hyperparameters (9.2), p-value tables (9.5), and the ethics statement (Section 8) beyond the footnote summary were not read in detail.
- Exact CelebA racial proportions used to build UnfairFace (only ">80% White" given).
- Licensing terms of FairFace itself.
- Number of training epochs / compute per model.
