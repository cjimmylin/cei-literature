---
stem: "2024-Tonneau-NaijaHate"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, cultural-linguistic, contamination-robustness, best-practices]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 35976
dataset_construction: "crowdsourced"
languages: ["English", "Nigerian Pidgin", "Hausa", "Yoruba"]
models_tested: ["GPT-3.5", "Perspective API", "NaijaXLM-T (full)", "NaijaXLM-T (198M)", "BERTweet", "DeBERTaV3", "XLM-R", "XLM-T", "HateBERT", "fBERT", "AfriBERTa", "AfroXLM-R", "XLM-R Naija", "Conversational BERT", "mDeBERTaV3"]
headline_numbers:
  - "Average precision on the representative random sample averages 20.92% vs 73.75% on holdout and 81.88% on top-scored sets (p.6)"
  - "Best model (NaijaXLM-T full) achieves 33.7% AP on random sample vs 83.4% on holdout set (p.6)"
  - "Hate speech prevalence in random sample: approximately 0.16% (p.5)"
  - "1% review rate enables moderating 60% of hateful content on Nigerian Twitter (p.8)"
  - "Active learning sample has 72.5% of tweets without seed keywords vs 7.5% for stratified sample (p.4)"
---
## 1. Gist
NAIJAHATE is the first hate speech detection dataset for Nigerian Twitter that includes a genuinely representative evaluation sample, drawn from a pool of 2.2 billion Nigerian tweets collected over 16 years. The paper's central contribution is demonstrating that models evaluated on standard academic hate speech datasets report AP of 83–90% but drop to 34% average precision on the representative random sample — a greater than two-fold overestimation. Beyond the dataset, the paper introduces NAIJAXLM-T, a domain-adaptive pretrained model, and conducts careful ablations showing that in-domain pretraining, in-domain fine-tuning, and training data diversity (via active learning) each independently and substantially improve real-world performance. For values-alignment benchmarking, NAIJAHATE demonstrates that ecologically valid evaluation requires representative sampling, and that context-specific hate (e.g., Nigerian Pidgin slang, ethnicity targets specific to Nigeria) cannot be captured by datasets trained on North American English.

## 2. Benchmark/eval design features
The paper constructs four distinct data splits with intentionally different sampling strategies: (1) Stratified sample (N=1,607) — oversampled using 89 hate-related and 45 community-related seed keywords; (2) Active learning sample (N=2,405) — generated through certainty sampling with iterative fine-tuning; (3) Top-scored sample (N=1,965) — pooled high-confidence hate predictions from 10 models deployed on the evaluation corpus; (4) Random sample (N=29,999) — the representative evaluation set. The three-class taxonomy (hateful, offensive, neutral) matches the HATEDAY paper, with target categories for Nigerian context: North (Hausa, Fulani, Herdsmen, Northerner), South, East, Muslims, Women, and Other. Evaluation metric is average precision (AP) for the hateful class.

## 3. Task format & example item
Three-class classification. Example items from Table 1 (p.3):

- Hateful, Target North: "My hate for northern people keeps growing"
- Hateful, Target East: "IPOBs are animals....They lack tact or strategy."
- Hateful, Target Muslim: "Muslim baboons and their terrorist religion."
- Hateful, Target Women: "Nobody believes this ashawo (prostitute) woman"
- Offensive (no target): "Stop spewing rubbish, mumu (fool)."
- Neutral: "She don already made up her mind sha." [Nigerian Pidgin]

## 4. Scoring / grading methodology
Three annotators per tweet; majority vote for final label. Krippendorff's α = 0.7 across the dataset (p.3). Three annotators agreed on 90% of all labeled tweets; two of three agreed in 9.5%; all three disagreed in only 0.5% (p.3). Average precision used for model evaluation — appropriate for highly imbalanced datasets where positive class (hate) is ~0.16% of random sample. 5-fold cross-validation with 90-10 train-test split, averaged across 10 seeds for supervised models.

## 5. Dataset construction & provenance
Source: 2.2 billion tweets from 2.8 million Nigerian-profile users, collected via iterative Twitter API crawling (March 2007 – July 2023). Two random 100-million-tweet draws: one for training, one for evaluation. Language composition: 77% English, 7% Nigerian Pidgin, 1% Hausa, 1% Yoruba, 14% other (p.3). Annotators: four Nigerian annotators, two female/two male, from the four most populous Nigerian ethnic groups (Hausa, Yoruba, Igbo, Fulani). Dataset and models available at https://github.com/worldbank/NaijaHate. Total annotated: 35,976 tweets across training and evaluation splits.

## 6. Validity evidence
Strong ecological validity through representative random sampling from a massive real-world corpus. The dramatic gap between holdout performance and random-sample performance (73.75% vs 20.92% AP on average) itself constitutes evidence of poor benchmark validity for existing methods. The paper validates the role of diversity as a mediating variable: diversity metrics (proportion of tweets without seed keywords, unique tokens, average pairwise embedding distance) are quantified across sampling strategies (Table 2, p.4). Context-specific validity is demonstrated through cross-lingual error examples (e.g., "ya k*ke" meaning "How are you" in Hausa but a slur in US English context, p.7). IAA of Krippendorff's α = 0.7 for three-class task.

## 7. Saturation / discrimination
Hate prevalence in the random sample is 0.16%, making the task extremely challenging. Even the best model (NaijaXLM-T full) reaches F1 of only 0.395 (p.8), with no threshold allowing both precision and recall above 0.5. The top-scored evaluation set has ~50% hate prevalence, demonstrating that curated/biased sets appear much more tractable than real-world data. The active learning sample provides more diversity in the hateful class (closer to the random sample in diversity metrics) while holding cost constant — a practical finding for future benchmark construction.

## 8. Multiturn / agentic aspects
n/a. Single-tweet classification only.

## 9. Key numbers
- Total dataset size: 35,976 annotated tweets (p.2)
- Random sample (representative evaluation set): 29,999 tweets (p.5)
- Hate prevalence in random sample: ~0.16%; offensive: ~1.6% (p.5)
- Average AP across models: random sample 20.92%; holdout 73.75%; top-scored 81.88% (p.6)
- Best model (NaijaXLM-T full): random AP 33.7% ± 4.5; holdout AP 83.4% ± 2.1 (p.6)
- GPT-3.5 zero-shot: top-scored AP 60.3%, random AP 3.1% (p.6)
- Perspective API: top-scored AP 60.2%, random AP 4.3% (p.6)
- Diversity comparison: active learning 72.5% without seed keywords vs. stratified 7.5% (p.4)
- 1% tweet review → 60% hate recall in human-in-the-loop moderation (~9,200 tweets/day) (p.8)
- 10% review needed for 76% recall (p.8)
- 3-class IAA: Krippendorff's α = 0.7 (p.3)
- Source corpus: 2.2 billion tweets from 2.8 million Nigerian users (p.3)

## 10. Pitfalls & limitations
- Random sample contains only 49 hateful examples — very small positive class, large confidence intervals (p.9).
- Dataset is Twitter-specific and Nigerian-specific; generalizability to other platforms and English dialects uncertain (p.9).
- Target taxonomy may miss communities that are targeted on Nigerian Twitter (South Africans, British people, Men observed but not in main taxonomy) (p.9).
- Pre-collection moderation by Twitter creates a lower-bound estimate of hate prevalence (p.9).
- Prompt for GPT-3.5 does not include a definition of hate speech — zero-shot comparison may underestimate LLM performance (p.6).
- 16-year timespan of training data may include outdated hate patterns; annotation guidelines applied retroactively.

## 11. Novel ideas worth stealing
1. **Representative sampling from massive corpus for evaluation only**: Use keyword-stratified or active-learning data for training but a random sample for evaluation — this creates a fair real-world test while keeping training data tractable.
2. **Active learning for diversity, not just coverage**: Certainty sampling builds a more diverse positive-class training set than keyword stratification at the same cost, closing the gap with the random sample diversity distribution — directly applicable to any benchmark needing rare positive examples.
3. **Diversity metrics as dataset quality indicators**: Proportion of items without seed keywords, unique token rate, and average pairwise embedding distance as explicit indicators of how representative a curated training set is of the real world.
4. **Separate evaluation from training sampling**: The paper's design — four sampling strategies with different purposes — is a template for how future values-alignment benchmarks can distinguish training set construction from evaluation set validity.
5. **Domain-adaptive pretraining for low-resource cultural contexts**: For any cultural/linguistic context underrepresented in global corpora, domain-adaptive pretraining on in-domain data (even at matched scale to existing multilingual models) consistently outperforms generic multilingual baselines.
6. **Cost-recall tradeoff as policy output**: Providing the trade-off curve between review percentage and recall (Figure 3) gives decision-makers actionable information beyond accuracy metrics — directly useful for any human-in-the-loop harm evaluation system.

## 12. Notable quotes
- "the striking result is that across the wide range of models considered in this study, the average precision on the random sample (20.92% on average) is substantially lower than that on the holdout (73.75%) and top-scored sets (81.88%)." (p.6)
- "XLM-T HateXplain assigns very high hateful scores to tweets containing [ya k*ke] whereas XLM-T NaijaHate does not." (p.7) — demonstrating cultural specificity of hate patterns
- "finetuning on more diverse data significantly and consistently improves the average precision across models." (p.7)
- "the performance gains from in-domain pretraining may be particularly large when the finetuning data is less diverse, presumably because the lower diversity in the finetuning data is counterbalanced by a higher diversity and domain alignment in the pretraining data" (p.7)

## 13. UNKNOWN / not in extract
- Precision-recall curves (Figure 4) not in extracted portion.
- Diversity metrics figure (Figure 5) referenced but not extracted.
- Full hyperparameter details for all models not fully extracted (reference to Appendix A.4.4).
- Exact annotation guidelines text (Appendix A.2.2 referenced but not extracted).
- Zero-shot GPT-3.5 prompt wording (Appendix A.4.4 referenced but not extracted).
- Full dataset license beyond "available at GitHub."
