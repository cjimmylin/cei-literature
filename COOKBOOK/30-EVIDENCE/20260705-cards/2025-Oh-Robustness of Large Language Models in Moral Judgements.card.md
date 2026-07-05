---
stem: "2025-Oh-Robustness of Large Language Models in Moral Judgements"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, validity-psychometrics, contamination-robustness, saturation-discrimination]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 14
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-3.5 (text-davinci-003)"]
headline_numbers:
  - "GPT-3.5 replicated 37.5% of original effects and 37.5% of Many Labs 2 effects across 8 analysable studies (p.4)"
  - "99.6% of GPT-3.5 runs self-identified as maximally conservative in original order; 99.3% as maximally liberal in reverse order (p.8)"
  - "100% of GPT-3.5 runs judged pushing Fat Man as morally impermissible — robust to demographic variation (p.11)"
  - "66.7% of 'correct answers' were robust to answer-order reversal (p.10, Table 3)"
  - "GPT-3.5's Less-is-better effect size: d=9.25 vs. human d=0.78 (p.6, Table 1)"
  - "Both self-reported GPT liberals and conservatives showed right-leaning Moral Foundations vs. human samples (p.12-13)"
---
## 1. Gist
NOTE: The extract filename ("2025-Oh-Robustness of Large Language Models in Moral Judgements") does not match the actual paper in the extract, which is "Diminished diversity-of-thought in a standard large language model" by Peter S. Park (MIT), Philipp Schoenegger (LSE), and Chongyang Zhu (CVS Health), published in Behavior Research Methods (2024) 56:5754–5770. This card describes the actual paper content.

This pre-registered empirical study replicates 14 studies from the Many Labs 2 psychology replication project using GPT-3.5 (text-davinci-003) to test whether LLMs can substitute for human participants in social science research. The central discovery is the "correct answer" effect: for 6 of 14 studies covering moral philosophy, political orientation, economic preference, and judgment, GPT-3.5 produced near-zero variance (99–100% uniformity) rather than the significant diversity shown by human participants. Additionally, even "correct answers" about political orientation completely reversed with answer-order reversal. Both self-reported GPT-liberals and GPT-conservatives displayed right-leaning Moral Foundations scores. The paper argues this pattern is evidence against LLMs as general human surrogates and raises concerns about AI-led homogenization of thought. For values-alignment benchmarking, this paper is essential: it empirically demonstrates that LLMs fail as valid instruments for measuring human moral diversity, and that apparent moral-philosophical responses may be position-order artifacts or robustly biased toward non-representative positions.

## 2. Benchmark/eval design features
This paper re-uses the Many Labs 2 (Klein et al., 2018) battery of psychology studies — a large-scale replication project. From 28 candidate studies, 14 were selected for GPT-3.5 replication (excluding those requiring images, handwriting, national comparisons, or non-text components).

Key studies include:
- **Moral Foundations Theory survey** (Graham et al., 2009): Self-reported political orientation + ratings of harm, fairness, ingroup, authority, purity relevance for moral judgment
- **Trolley dilemma** (Hauser et al., 2007): Whether sacrificing one to save five is permissible (lever variant vs. Fat Man variant)
- **Knobe effect** (Knobe, 2003): Whether a side effect is judged intentional when harmful vs. helpful
- **False consensus** (Ross et al., 1977): Estimating own and others' behavior
- **Affect and risk** (Rottenstreich & Hsee, 2001): Kiss vs. cash choice under certainty vs. 1% probability
- **Framing effects** (Tversky & Kahneman, 1981): Framing of discounts on cheap vs. expensive items

Each study ran ~1000 GPT-3.5 API calls at default temperature (1.0). Analysis followed pre-registered plans based on Many Labs 2. Exploratory follow-up studies tested order effects (reverse answer choices) and demographic variation in prompts.

## 3. Task format & example item
Trolley dilemma (Hauser et al., 2007) — verbatim from extract context:
"Subjects were asked whether they would sacrifice one life to save five lives, either by changing an out-of-control trolley's trajectory or by pushing a large man in front of a trolley." (p.5, Table 1)

The lever variant yielded 36% permissible / 64% not permissible across GPT-3.5 runs, but the Fat Man variant yielded 100% impermissible — creating the "correct answer" effect for the Fat Man condition.

Self-reported political orientation prompt (Graham et al., 2009):
Subjects first self-identified on liberal-conservative spectrum, then rated how relevant harm, fairness, ingroup, authority, and purity concepts are for moral judgment. In GPT-3.5, 99.6% chose the maximally conservative option in original order; 99.3% chose the maximally liberal option in reverse order — picking the last presented choice.

## 4. Scoring / grading methodology
Pre-registered analysis plans from Many Labs 2:
- Effect sizes computed as Cohen's d, Cohen's q, or odds ratios with 95% confidence intervals
- Successful replication defined as significant effect in the same direction as original
- "Correct answer" defined as 99%+ uniform responses (arbitrary threshold noted)
- Exploratory: Answer reversal robustness coded as "correct answer" robust if 90%+ still give original answer
- Moral Foundations comparison: L1 (absolute-error), L2 (Euclidean) distance, and cosine similarity between GPT and human response vectors

## 5. Dataset construction & provenance
Stimuli drawn directly from Many Labs 2 (Klein et al., 2018), which in turn reproduced the original study materials. Sample sizes: ~1000 GPT-3.5 API calls per study condition (520–1040 depending on conditions). Human comparison data from original studies (various N) and Many Labs 2 aggregated samples (N ranges: 20–7205 per study). Graham et al. (2011) provided human Moral Foundations norms for liberals (N=21,933), moderates (N=3,203), conservatives (N=4,128), and libertarians (N=2,999). Pre-registration on OSF: Park et al. (2023). Code in Python 3.9.15; analysis in JAMOVI and Excel.

## 6. Validity evidence
The paper is explicitly a validity study of LLMs as human surrogates. Key validity findings:
- GPT-3.5 replicated only 37.5% of studies (Many Labs 2 replicated 50% of the same studies), confirming LLMs are poorer human surrogates than direct human replication
- Effect sizes show extreme divergence: Less-is-better effect d=9.25 for GPT vs. d=0.78 for humans (p.6)
- Answer-order effects far exceed human order effects: 100% → 54% reversal for one condition
- Political orientation collapses to 100% one endpoint or the other based on answer ordering — direct measurement of position bias as validity threat
- Moral Foundations right-lean replicated across GPT-3 family (Abdulhai et al., 2023 cited at p.13)
- Demographic variation in prompts failed to break the Fat Man "correct answer" (100% impermissible persisted across 982 demographically varied runs)

## 7. Saturation / discrimination
The "correct answer" effect is the key saturation phenomenon: 6 of 14 studies showed 99–100% response uniformity, making statistical analysis impossible. This is extreme ceiling/floor saturation specifically on moral/political items. For the 8 analyzable studies, effect sizes ranged from near-zero to extreme (d=9.25). The studies showed substantial heterogeneity in whether GPT replicated findings. Only 2 studies replicated both original and Many Labs 2 results; 4 failed to replicate either. This pattern shows both under-discrimination (correct answer uniformity) and over-discrimination (extreme effect sizes like d=9.25 exceeding human range).

## 8. Multiturn / agentic aspects
Single-turn API calls; each run is one call representing one independent "participant." No multiturn interaction. The paper explicitly designed for single-turn to enable controlled experiments with large N. Temperature set to default 1.0.

## 9. Key numbers
- 14 studies from Many Labs 2 replicated (p.3)
- 8 studies analysable; 6 showed "correct answer" effect (p.4)
- GPT replication rate: 37.5% of original effects, 37.5% of Many Labs 2 effects (p.4)
- Many Labs 2 replication rate for the same subset: 50% (p.4)
- ~1000 GPT-3.5 runs per study (p.3)
- 99.6% GPT-3.5 runs chose maximally conservative in original-order condition (N=1030) (p.8)
- 99.3% chose maximally liberal in reverse-order condition (N=1030) (p.11)
- 100% of 1040 GPT-3.5 runs chose movie star's kiss in certain condition (Rottenstreich & Hsee) (p.8)
- 100% of 982 demographically varied GPT-3.5 runs judged Fat Man push as impermissible (p.11)
- 66.7% of "correct answers" robust to answer-order reversal (p.10)
- Less-is-better effect: GPT d=9.25 [8.67, 9.82] vs. ML2 d=0.78 [0.74, 0.83] (p.6)
- Reluctance to tempt fate: GPT d=−2.49 [−2.68, −2.29] vs. original d=0.39 [0.03, 0.75] — direction reversal (p.6)
- GPT-3.5 Moral Foundations: Harm=3.84–4.02, Fairness=4.26–4.33, Ingroup=2.10–2.24, Authority=3.34–3.36, Purity=2.88–3.07 (p.12, Table 4)

## 10. Pitfalls & limitations
- **Model-specific**: Results pertain to GPT-3.5 (text-davinci-003) specifically; different models show different political leanings (Hartmann et al. 2023 found ChatGPT left-libertarian)
- **Survey-only method**: Entirely text-based attitudinal responses; no behavioral validation of whether "correct answers" translate to actual behaviors
- **Training data contamination**: GPT-3.5 may have memorized the specific Many Labs 2 studies
- **Non-random study subsample**: 14 of 28 studies excluded for requiring graphical stimuli — non-random subsample
- **Causal ambiguity**: Three possible causes of "correct answers" identified (training data, fine-tuning, input/output modifications) but none confirmed due to black-box model access
- **Temporal instability**: ChatGPT's political leanings shifted over time (Rozado, 2023), so results may not generalize to later versions
- **English-only**: All studies conducted in English

## 11. Novel ideas worth stealing
1. **Pre-registered LLM replication of psychology studies**: The methodology of running an LLM through pre-existing, validated human psychology studies at scale (~1000 runs) provides a powerful validity check for LLM-as-participant claims — benchmark designers should adopt pre-registration and Many Labs-style multi-study designs.
2. **"Correct answer" effect as a benchmark quality indicator**: Any moral/values benchmark should be tested for response variance. Items where 99%+ of an LLM's responses are identical are effectively measuring nothing about the model's moral reasoning and should be flagged as invalid or trivially easy.
3. **Answer-order robustness as mandatory validity check**: Running benchmarks in both original and reverse answer-choice order and reporting the divergence is a low-cost but highly informative validity check — the political orientation finding (99.6% conservative → 99.3% liberal) demonstrates how catastrophically non-robust some "moral" measures are.
4. **Demographic prompt variation as robustness probe**: Adding random demographic identities to prompts and measuring whether responses change tests whether observed patterns are truly stable values or artifacts of an under-specified persona. The Fat Man finding (100% impermissible across all demographics) demonstrates some biases are genuinely robust.
5. **Moral Foundations vector distance metric**: Using L1, L2, and cosine similarity to compare LLM Moral Foundations vectors against human subgroup norms (liberal, moderate, conservative, libertarian) provides a compact quantitative profile of LLM political/moral positioning.
6. **Diversity-of-thought metric**: The paper implicitly proposes measuring the variance of LLM responses across runs as a proxy for moral diversity — a metric that could be used to detect benchmark items that have been "collapsed" by fine-tuning.

## 12. Notable quotes
- "Different runs of GPT-3.5 answered nuanced questions probing political orientation, economic preference, judgement, and moral philosophy with zero or near-zero variation in responses: with the supposedly 'correct answer.'" (abstract, p.1)
- "We call this the 'correct answer' effect. This terminology denotes GPT-3.5's tendency to sometimes answer survey questions – in a highly (or sometimes completely) uniform way." (p.4)
- "We robustly find that self-reported GPT liberals revealed right-leaning Moral Foundations: a right-leaning bias of lower magnitude, but a right-leaning bias nonetheless." (p.12)
- "A hypothetical AI-led future may be subject to a diminished diversity of thought." (abstract, p.1)

## 13. UNKNOWN / not in extract
- Whether the paper's results extend to GPT-4 or instruction-tuned ChatGPT (explicitly noted as a limitation)
- Full supplementary information contents (referenced but not in extract)
- The exact pre-registration document contents beyond what is described in text
- Results for the 14 excluded studies requiring graphical stimuli
- Whether the study has been replicated with other LLM families (only Abdulhai et al. 2023 cited for partial replication with GPT-3 family)
- Full details of the demographic variation follow-up study methods
- The relationship between this paper and the filename stem "Oh-Robustness of Large Language Models in Moral Judgements" — the extract contains a different paper (Park, Schoenegger & Zhu on diminished diversity-of-thought)
