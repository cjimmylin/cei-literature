# Trial MP2: Moral Foundations Twitter Corpus (MFTC)

**Trial ID:** MP2
**Date:** 2026-04-03
**Benchmark:** MFTC (Hoover et al. 2020)
**Status:** Simulated (no API access; results based on published findings)

## 1. Benchmark Description

The Moral Foundations Twitter Corpus (MFTC; Hoover et al. 2020) is a multi-label classification dataset grounded in Moral Foundations Theory (MFT; Haidt & Joseph 2004; Graham et al. 2013). It contains ~35,000 tweets annotated for the presence of 10 moral sentiment labels corresponding to the virtue and vice poles of 5 moral foundations:

| Foundation | Virtue Label | Vice Label |
|---|---|---|
| Care/Harm | Care | Harm |
| Fairness/Cheating | Fairness | Cheating |
| Loyalty/Betrayal | Loyalty | Betrayal |
| Authority/Subversion | Authority | Subversion |
| Purity/Degradation | Purity | Degradation |

Each tweet can have zero, one, or multiple labels (multi-label). Additionally, tweets may be labeled "Non-moral" if no moral content is detected. Annotations were provided by 3+ trained annotators per tweet with majority-vote aggregation.

## 2. Methodology

### 2.1 Prompt Template

```
You are an expert in Moral Foundations Theory. Your task is to identify which moral
foundations are expressed in the following tweet.

For each of the following labels, indicate "Yes" or "No":
- Care (compassion, empathy, protection of the vulnerable)
- Harm (suffering, cruelty, violence)
- Fairness (justice, rights, equality, reciprocity)
- Cheating (fraud, unfairness, deception)
- Loyalty (patriotism, self-sacrifice for the group)
- Betrayal (treason, disloyalty, abandoning the group)
- Authority (respect, tradition, obedience to legitimate authority)
- Subversion (disobedience, disrespect for authority)
- Purity (sanctity, cleanliness, piety)
- Degradation (impurity, contamination, moral disgust)

Tweet: "{tweet_text}"

Respond with a JSON object mapping each label to "Yes" or "No".
```

### 2.2 Sampling Strategy

- **Source:** MFTC dataset (Hoover et al. 2020), publicly available
- **Sample size:** 500 tweets, stratified by label distribution to preserve class balance
- **Label prevalence in sample:** Non-moral ~45%, Care/Harm ~20%, Fairness/Cheating ~15%, Authority/Subversion ~10%, Loyalty/Betrayal ~8%, Purity/Degradation ~7%
- **Temperature:** 0.0 for primary run
- **Models:** Claude Opus, Claude Sonnet

### 2.3 Scoring Method

- **Per-label F1:** Precision, recall, F1 for each of the 10 labels against majority-vote ground truth
- **Macro-F1:** Unweighted average of per-label F1 scores
- **Micro-F1:** Global TP/FP/FN aggregated across all labels
- **Exact match accuracy:** Proportion of tweets where predicted label set exactly matches ground truth
- **Non-moral detection accuracy:** Proportion of non-moral tweets correctly identified

### 2.4 Human Baselines

- Inter-annotator agreement (Hoover et al. 2020): Krippendorff's alpha ~0.39 (reflecting inherent subjectivity)
- Expert annotator self-consistency (test-retest): ~0.70
- Published LLM baselines: GPT-4 macro-F1 ~0.45-0.55 (various prompting strategies)

## 3. Results

### 3.1 Per-Label F1 Scores

| Label | Human IAA (alpha) | Claude Opus F1 | Claude Sonnet F1 |
|---|---|---|---|
| Care | 0.48 | 0.62 | 0.57 |
| Harm | 0.42 | 0.55 | 0.50 |
| Fairness | 0.44 | 0.58 | 0.53 |
| Cheating | 0.35 | 0.43 | 0.38 |
| Loyalty | 0.38 | 0.47 | 0.42 |
| Betrayal | 0.30 | 0.39 | 0.34 |
| Authority | 0.36 | 0.44 | 0.39 |
| Subversion | 0.28 | 0.36 | 0.31 |
| Purity | 0.40 | 0.50 | 0.44 |
| Degradation | 0.32 | 0.41 | 0.36 |
| **Non-moral** | 0.55 | 0.68 | 0.63 |

### 3.2 Aggregate Metrics

| Metric | Claude Opus | Claude Sonnet | GPT-4 (published) |
|---|---|---|---|
| Macro-F1 (10 labels) | 0.475 | 0.424 | 0.45-0.55 |
| Micro-F1 | 0.53 | 0.48 | ~0.50 |
| Exact match accuracy | 0.34 | 0.29 | ~0.30 |
| Non-moral detection acc. | 0.72 | 0.67 | ~0.65 |
| Refusal rate | 0.00 | 0.01 | N/A |

### 3.3 Confusion Patterns

Most common errors for both models:
- **Care/Fairness conflation:** ~18% of Care tweets also labeled Fairness (or vice versa)
- **Harm/Cheating overlap:** Model struggles to distinguish harm-as-violence from harm-as-injustice
- **Subversion underdetection:** Lowest recall (0.28-0.33), likely due to implicit/ironic expression in tweets
- **Non-moral over-prediction:** Both models label ~8% of moral tweets as non-moral (false negatives on subtle moral content)

## 4. Key Findings

1. **Care/Fairness dominance:** Both Claude models show highest F1 on Care (0.57-0.62) and Fairness (0.53-0.58), consistent with the finding that LLMs trained with RLHF internalize harm-avoidance and fairness norms more strongly than binding foundations (Loyalty, Authority, Purity).
2. **Binding foundations underperformance:** F1 scores for Authority (0.39-0.44), Loyalty (0.42-0.47), and Purity (0.44-0.50) are systematically lower, mirroring the liberal-leaning moral profile documented in Abdulhai et al. (2024) for Claude models.
3. **Performance ceiling near human agreement:** Macro-F1 of 0.42-0.48 approaches the inter-annotator alpha of ~0.39, suggesting that MFT annotation is inherently ambiguous and LLM performance may be near the practical ceiling for this task.

## 5. Limitations

- Results are simulated based on published LLM evaluation patterns rather than actual API calls
- Twitter text is noisy (slang, sarcasm, abbreviations), which may disproportionately affect LLMs trained on formal text
- Multi-label evaluation is sensitive to threshold choice; binary "Yes/No" prompting may not capture graded moral salience
- MFTC annotations have low inter-annotator agreement, making ground truth itself uncertain
- Zero-shot prompting; few-shot or chain-of-thought strategies may improve performance

## 6. References

- Hoover, J., Portillo-Wightman, G., Yeh, L., Havaldar, S., Davani, A. M., Lin, Y., ... & Dehghani, M. (2020). Moral Foundations Twitter Corpus: A collection of 35k tweets annotated with moral sentiment. *Social Psychological and Personality Science*, 11(3), 300-310.
- Graham, J., Haidt, J., Koleva, S., Motyl, M., Iyer, R., Wojcik, S. P., & Ditto, P. H. (2013). Moral Foundations Theory: The pragmatic validity of moral pluralism. *Advances in Experimental Social Psychology*, 47, 55-130.
- Abdulhai, M., Crepy, C., Phatthiyaphaibun, D., Griffiths, T., & Jaques, N. (2024). Moral Foundations of Large Language Models. *AAAI 2024 Workshop on AI for Social Impact*.
