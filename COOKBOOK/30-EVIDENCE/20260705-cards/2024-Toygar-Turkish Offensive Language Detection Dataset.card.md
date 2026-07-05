---
stem: "2024-Toygar-Turkish Offensive Language Detection Dataset"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics, agentic-multiturn]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 28808
dataset_construction: "crowdsourced"
languages: ["Turkish"]
models_tested: ["BERTurk", "Logistic Regression", "KNN", "SVM", "Random Forest", "Multinomial Naive Bayes"]
headline_numbers:
  - "BERTurk F1 improves from 70.28% (reply-only) to 73.57% (with context) on offensive language detection (p.4)"
  - "Final dataset: 28,808 tweet-reply pairs; 94.48% non-offensive, 5.52% offensive (p.3)"
  - "Cohen Kappa for final dataset: 88.97%; initial two-annotator agreement was only 46.26% (p.3)"
  - "Traditional ML models fail: SVM best with 47.18% F1, worse than majority classifier (p.4)"
---
## 1. Gist
This EMNLP 2023 findings paper introduces a Turkish tweet-reply pair dataset focused on offensive language against unvaccinated people during the COVID-19 pandemic, with the explicit research question: does including the "replied tweet" (contextual prior turn) improve offensive language detection in reply tweets? The paper constructs 28,808 tweet-reply pairs from Turkish Twitter (March 2020 – September 2022) and annotates reply tweets for offensiveness toward unvaccinated people. Experiments with both traditional ML and BERTurk show that contextual information (the prior tweet) provides only marginal improvement (+3.29% F1 for BERTurk). The paper is relevant to values-alignment benchmarking as it represents a rare attempt to operationalize context in offensive language annotation, and documents why naive context injection often fails: many reply tweets have weak semantic relationships to the tweet they reply to.

## 2. Benchmark/eval design features
Dataset: 28,808 tweet-reply pairs in Turkish. Binary target: offensive vs. non-offensive against unvaccinated people (target-group-specific, not general offensiveness). Three collection strategies: (1) Dataset 1 — keyword in reply tweet; (2) Dataset 2 — keyword in replied tweet that is itself a reply; (3) Dataset 3 — keyword in replied tweet that is a root post. Combined and annotated. Models evaluated in two conditions: (Scenario 1) reply tweet only; (Scenario 2) reply + replied tweet concatenated. This design allows direct measurement of the marginal value of conversational context.

## 3. Task format & example item
Binary classification of reply tweet as offensive/non-offensive against unvaccinated people. Example pairs from Appendix (p.6-7):

- **Context necessary**: Replied: "If we are closed at home again because of those who are not vaccinated, you will see curses that you have not seen so far in this account." Reply: "+1" — reply is offensive only because of context.
- **Context misleads**: Replied: "Vaccination opponents misread the National Anthem." Reply: "Go away the army of brainless people to your village, you can't live in the metropolis without a vaccine." — reply is offensive but replied tweet is benign; adding it misleads the model.
- **Context doesn't matter**: A reply tweet that is offensive on its own without needing the prior post.

## 4. Scoring / grading methodology
Binary annotation with three label options (offensive, not offensive, ambiguous); ambiguous cases removed from final dataset. Two annotators per pair; third annotator used to resolve inconsistencies. Pairs where annotators disagreed (one offensive, one not-offensive) were also removed as ambiguous. Inter-annotator agreement: initial F1 = 55.22%, Cohen Kappa = 46.26%; final dataset version F1 = 95.21%, Cohen Kappa = 88.97% (p.3). Evaluation metric: macro-averaged F1. 80/20 train/test split.

## 5. Dataset construction & provenance
Source: Turkish Twitter, March 2020–September 2022. Search using 16 keyword variants meaning "unvaccinated" in Turkish (singular/plural/morphological variants). Three collection sub-datasets combined: 13,478 from Dataset 1, 1,515 from Dataset 2, 13,815 from Dataset 3. Final: 27,219 non-offensive, 1,589 offensive (94.48%/5.52%). Annotators: three of the paper's authors. Dataset and code publicly available at https://github.com/boun-tabi/CovidOffensiveLanguageUltimateDatasets.

## 6. Validity evidence
High final inter-annotator agreement (Cohen Kappa 88.97%) after adjudication. The large drop from initial (46.26%) to final (88.97%) agreement reflects the importance of the adjudication process for subjective tasks. The paper provides example pairs illustrating cases where context helps, hurts, or is irrelevant — a qualitative validity analysis grounded in real data. The observation that "most reply tweets have only a weak relationship to the replied tweet in terms of meaning" (p.5) is an empirically grounded validity finding about the Twitter reply conversation structure.

## 7. Saturation / discrimination
Dataset is severely imbalanced (94.48% non-offensive). Traditional ML models perform near or below majority-class baseline even with downsampling (SVM best at 47.18% macro-F1 vs. majority classifier 48.58% F1) (p.4). BERTurk achieves 70.28% F1 without context and 73.57% with context — a small improvement. This suggests the task has room for improvement and is not trivially solved. The offensive class (1,589 examples in training) is a limiting factor for model performance.

## 8. Multiturn / agentic aspects
This paper directly studies a minimal form of multiturn context: tweet-reply pairs. The replied tweet is the single prior turn. Findings: context is marginally useful on average for transformer models (+3.29% F1), but traditional ML models actually perform worse with context. The paper identifies two failure modes: (1) the replied tweet is irrelevant to the reply's offensiveness; (2) a non-offensive replied tweet misleads the model about an offensive reply. This is one of the few papers in hate/offensive language detection that directly operationalizes and tests conversational context, making it relevant to multiturn benchmark design.

## 9. Key numbers
- Total dataset: 28,808 tweet-reply pairs (p.3)
- Non-offensive: 27,219 (94.48%); Offensive: 1,589 (5.52%) (p.3)
- Initial 2-annotator IAA: F1=55.22%, Cohen Kappa=46.26% (p.3)
- Final dataset IAA: F1=95.21%, Cohen Kappa=88.97% (p.3)
- BERTurk reply-only: F1=70.28%, Precision=65.73%, Recall=82.68% (p.4)
- BERTurk with context: F1=73.57%, Precision=70.11%, Recall=79.03% (p.4)
- Best traditional ML (SVM, reply-only): F1=47.18% — worse than majority classifier (p.4)
- Majority classifier: Precision=47.24%, Recall=50.0%, F1=48.58% (p.4)
- Dataset 1: 13,478 pairs; Dataset 2: 1,515; Dataset 3: 13,815 (p.3)

## 10. Pitfalls & limitations
- Annotators are three of the paper's authors — risk of self-selection bias and reduced independence; no external annotators.
- Single target group (unvaccinated people) and single language limits generalizability.
- Domain (COVID-19 vaccine discourse) is time-specific; model may not transfer to other offensive language contexts.
- The study only considers a single prior turn (replied tweet); longer conversation history not explored.
- Traditional ML experiments use downsampled not-offensive class to 4,500 — arbitrary threshold.
- No ablation of longer context windows; hypothesis that longer context might help more is not tested.
- No LLM-based models tested (only BERTurk and classical ML).

## 11. Novel ideas worth stealing
1. **Operationalizing conversational context in annotation**: Providing both the reply tweet and the replied tweet as annotation context — and requiring annotators to label only the reply tweet — is a clean experimental design for studying context effects in values-sensitive tasks.
2. **Failure mode taxonomy for context**: The paper provides a concrete taxonomy of cases where context helps vs. hurts vs. doesn't matter (with examples), which is a useful framework for designing multiturn/contextual benchmarks.
3. **Target-group-specific offensiveness**: Restricting annotation to offensiveness against a specific target group (unvaccinated people) rather than general offensiveness makes the task more focused and the label more reliable — applicable to any values benchmark that needs fine-grained harm classification.
4. **Three-option annotation with ambiguous removal**: Providing "ambiguous" as a third option and then removing ambiguous cases from the final dataset preserves data quality without forcing annotators into binary choices on genuinely unclear cases.
5. **Parallel condition design (with/without context)**: Training and evaluating identical models with and without contextual information is a clean experimental design for measuring the marginal value of any additional input feature in NLP benchmarks.

## 12. Notable quotes
- "our results showed that this resulted in only a slight improvement in the F1-score for some models and did not significantly improve the performance of the studied models for offensive language detection in general." (p.5)
- "in analyzing our dataset, we found that most reply tweets have only a weak relationship to the replied tweet in terms of meaning. Moreover, interaction with other tweets is dominated by the use of other features on Twitter, such as 'like' or 'retweet.'" (p.5)
- "The annotation of datasets is an essential step, which ought to be carried out responsibly. Despite the fact that we tried to use multiple annotators for the labeling process, developing better strategies are possible since some examples regarding offensive language are very subjective." (p.5)
- Example pair (p.6): "Reply Tweet: '+1' [to a tweet about unvaccinated people causing lockdowns]" — illustrates cases where context is essential for classification.

## 13. UNKNOWN / not in extract
- Full keyword list for Turkish morphological variants of "unvaccinated" is in the Appendix (partially shown but full list may differ from what is extracted).
- Exact demographic information about annotators beyond being three of the paper's authors.
- Whether BERTurk was fine-tuned from scratch or from an existing checkpoint.
- Hyperparameter details for traditional ML models (e.g., regularization for LR, kernel for SVM).
- Whether dataset includes tweet IDs that can be reconstructed or just preprocessed text.
