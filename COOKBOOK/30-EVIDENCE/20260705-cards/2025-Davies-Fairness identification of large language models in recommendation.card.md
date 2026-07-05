---
stem: "2025-Davies-Fairness identification of large language models in recommendation"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [validity-psychometrics, cultural-linguistic, pluralism-aggregation]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 16000
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["ChatGLM3-6B", "Llama2-13B"]
headline_numbers:
  - "ChatGLM3 fairness-to-utility ratio (gender, n=5): 30.9289 vs. VAEgan 6.0159 on MovieLens (p.1)"
  - "ChatGLM3 identified 89.44% of MovieLens users as gender-fair (n=5 history records) (p.7)"
  - "Llama2 identified only 13.04% of MovieLens users as gender-fair (n=5) (p.7)"
  - "Incorporating LLM fairness recognition improves fairness significantly with minimal utility loss (p.1)"
---
## 1. Gist
This Scientific Reports (2025) paper by Liu et al. (Ningbo University) investigates whether LLMs can serve as "fairness recognizers" in recommendation systems — identifying when a recommendation list is unfairly correlated with a user's sensitive attributes (gender, age). Using MovieLens 1M and LastFM 360K datasets with VAE-based recommendation models, the authors design prompts that ask ChatGLM3-6B and Llama2-13B to reason about whether a user's recommendation results would change if their demographic attribute were different. LLMs that correctly identify unfair recommendations trigger a replacement with fairness-intervened recommendations from a fair VAE (VAEgan). The study finds that LLMs possess measurable "fairness awareness" and that incorporating their judgments achieves substantially better fairness-utility trade-offs than blanket fairness intervention. For values-alignment benchmarking, the paper demonstrates a concrete methodology for using LLMs as fairness judges and reveals that LLM fairness cognition is model-size-dependent and task-domain-specific.

## 2. Benchmark/eval design features
Not a standalone benchmark. The paper's evaluation framework consists of:
- **Fairness identification accuracy**: comparing fairness metrics (χ²@100, Kendall-Tau@100) for recommendations identified as "fair" by LLMs before and after fairness intervention.
- **Fairness-to-utility ratio**: percentage increase in fairness / percentage decrease in NDCG@10.
- **Sensitive attributes**: binary gender (female/male) and binary age (under/over 35).
- Two LLMs evaluated (ChatGLM3-6B, Llama2-13B) on two datasets (MovieLens 1M, LastFM 360K) with two prompt history lengths (n=5, n=7 movies; n=5, n=10 artists).
- Baseline comparison: VAErec (unfair) vs. VAEgan (uniformly fair) vs. LLM-gated hybrid.

## 3. Task format & example item
Forced-choice (Yes/No). Prompt templates shown in Table 2 (p.4):

**MovieLens gender template**: "You are a movie recommender. A [sensitive] user has watched these movies: [record]. If the user isn't [sensitive], do you think the user will be interest in these movies: [rec_result]? Yes/No, please do not provide any other information."

**LastFM age template**: "You are a music recommender. A user who is over 35 years old has listened to these artists: [record]. If the user isn't over 35 years old, do you think the user will be interest in these artists: [rec_result]? Yes/No, please do not provide any other information."

A "No" response = the LLM judges the recommendation as unfair (would not be recommended to the counterfactual user). A "Yes" response = fair.

## 4. Scoring / grading methodology
Three metrics:
- **NDCG@10**: utility of recommendation (higher = better).
- **χ²-statistic @100**: measures independence between recommendation distribution and sensitive attributes. Computed via contingency table across top-100 recommendations aggregated by sensitive group; lower = fairer.
- **Kendall-Tau distance @100**: similarity between recommendation ranked lists for different sensitive groups; closer to 1 = fairer.
- **Fairness-to-utility ratio**: (% increase in χ² or K.T@100) / (% decrease in NDCG@10), computed per experiment from Table 5 results. Higher ratio = better fairness per unit utility cost.

## 5. Dataset construction & provenance
- **MovieLens 1M**: ~6K users, ~3.5K items, ~575K records; ratings 4–5 converted to positive implicit feedback; 7:1:2 train/val/test split.
- **LastFM 360K**: ~10K users (filtered: ≥60 interactions), ~12.7K artists (filtered: ≥110 listening events), ~598K records; positive = played.
- Both datasets use disjoint user splits (train/val/test sets contain different users) to simulate recommendations to unseen users.
- LLM queries generated at inference time from these datasets; no additional dataset construction for the LLM fairness recognition experiments.
- Data publicly available: MovieLens at grouplens.org; LastFM 360K at upf.edu/web/mtg/lastfm360k.
- Code: https://github.com/sy-cg/LLM-fair-aware.

## 6. Validity evidence
- Discriminant validity: LLMs identify substantially different percentages of fair users (ChatGLM3 89% vs. Llama2 13% for gender in MovieLens), confirming models operate on different decision thresholds, not random noise.
- Construct validity (partial): fairness metrics for ChatGLM3-identified "fair" users are substantially better than the overall pre-intervention baseline (χ²@100: 533 vs. 3287), confirming the LLM is identifying genuinely less biased subsets.
- Cross-domain divergence: ChatGLM3 performance is strong in MovieLens but degrades in LastFM, suggesting domain-specificity limits generalization.
- No inter-rater reliability assessment between LLMs and human fairness judgments; no ground-truth "oracle" fairness labels.

## 7. Saturation / discrimination
ChatGLM3 identifies 89-95% of MovieLens users as gender-fair (high concentration at "fair" end), while Llama2 identifies only 12-19% — revealing extreme model divergence. For LastFM, ChatGLM3 identifies 79-80% as gender-fair but Llama2 identifies only 0.49-0.79%, essentially treating all music recommendations as unfair. These extreme divergences suggest the models are not measuring the same construct and that prompt sensitivity is high. The fairness-to-utility ratio is the most discriminating metric: ChatGLM3 achieves 30.9 vs. VAEgan's 6.0 for MovieLens gender (n=5), but drops to 3.1 for n=7; Llama2 achieves comparable (~5-7) ratios.

## 8. Multiturn / agentic aspects
Single-turn forced-choice inference only. Each user gets one query per recommendation list. No multi-turn or conversational elements.

## 9. Key numbers
- MovieLens: 6K users, 3.5K items, 575K records; LastFM: 10K users, 12.7K artists, 598K records (p.3, Table 1)
- ChatGLM3 gender-fair identification: MovieLens 89.44% (n=5), 94.88% (n=7); LastFM 79.80% (n=5), 79.70% (n=10) (p.7-8, Tables 3-4)
- Llama2 gender-fair identification: MovieLens 13.04% (n=5), 12.21% (n=7); LastFM ~0.49% (n=5), ~0.79% (n=10) (p.7-8)
- Fairness-to-utility ratio MovieLens gender: VAEgan=6.0159, ChatGLM3(n=5)=30.9289, Llama2(n=5)=5.1106 (p.9, Table 6)
- VAErec baseline: NDCG@10=0.3098, χ²@100=3286.8 for MovieLens gender (p.9, Table 5)
- VAEgan: NDCG@10=0.2716, χ²@100=848.7 for MovieLens gender (p.9)
- ChatGLM3(n=5) hybrid: NDCG@10=0.3097 (near-baseline utility), χ²@100=3253.9 — note: fairness improvement is small here; the ratio number derives from a different calculation (p.9)

## 10. Pitfalls & limitations
- The fairness criterion is operationalized as correlation independence between recommendations and sensitive attributes — a group fairness notion that may not capture individual-level fairness or intersectional fairness.
- No human validation of LLM fairness judgments; ground truth is comparative rather than absolute.
- LLM responses are purely based on whether items would appeal to the counterfactual demographic, not whether the algorithm discriminated — this is an indirect proxy for fairness.
- The "Yes/No only" instruction reduces reasoning transparency; LLMs cannot explain why a recommendation is flagged as unfair.
- ChatGLM3's high identification rate (89-95%) may reflect a bias toward judging recommendations as "fair" rather than genuine fairness detection.
- LastFM results are weaker and inconsistent, suggesting the approach may not generalize across recommendation domains.
- Only two LLMs tested; both are relatively small (6B and 13B parameters); results may not generalize to larger models.
- Age attribute performance was weaker than gender across models and datasets.

## 11. Novel ideas worth stealing
1. **Counterfactual demographic prompt for fairness judgment**: asking an LLM "would this same content be recommended if the user's [sensitive attribute] were different?" is a clean operationalization of counterfactual fairness suitable for any content domain. Directly applicable to values-alignment benchmarks testing whether AI systems exhibit demographic bias in advice or recommendations.
2. **Fairness-to-utility ratio as benchmark metric**: normalizing fairness gains by utility cost is more informative than either metric alone. Values benchmarks involving AI assistance could adopt this ratio to evaluate whether fairness interventions degrade helpfulness.
3. **LLM-as-fairness-gate hybrid architecture**: using LLM judgment to selectively apply fairness interventions only where needed (rather than uniformly) is a novel architectural pattern. This could be applied to values alignment where different users/contexts may require different levels of ethical caution.
4. **Model size as fairness cognition predictor**: Llama2-13B sometimes outperforms ChatGLM3-6B on χ² metric despite identifying far fewer users, suggesting that precision vs. recall in fairness identification varies by model scale. This calibration insight could inform LLM-judge selection in benchmark evaluation pipelines.

## 12. Notable quotes
- "LLMs possess a degree of fairness cognition, and employing LLMs for fairness identification in recommendation results helps achieve a better balance between effectiveness and fairness." (p.2)
- "Existing fairness strategies that intervene uniformly without user-specific identification can actually lead to decreased fairness in recommendation results." (p.9, Conclusion)
- "Different LLMs vary in fairness identification capabilities, with larger models generally performing better." (p.8)
- "The human-like cognition of LLMs offers new opportunities for fairness research in recommendation systems." (p.9)

## 13. UNKNOWN / not in extract
- Exact prompt templates for age attributes in MovieLens (only partial shown in Table 2).
- Whether LLM responses were validated against human fairness judgments on any subset.
- Details of how "Yes/No only" instruction affected model compliance rates.
- Whether models were fine-tuned or used zero-shot.
- Computational cost of LLM inference per recommendation.
- Statistical significance tests for fairness metric improvements.
- Whether the fairness-to-utility ratio differences are statistically significant.
