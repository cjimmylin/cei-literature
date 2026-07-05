---
stem: "2021-Ravikiran-DOSA Dravidian Code-Mixed Offensive Span Identification"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, design-space]
task_format: "free-text"
scoring_type: "exact-match"
dataset_size: 5883
dataset_construction: "crowdsourced"
languages: ["ta", "kn", "en"]
models_tested: ["BERT-M1", "BERT-M2", "DistilBERT-M1", "DistilBERT-M2", "XLM-RoBERTa-M1", "XLM-RoBERTa-M2"]
headline_numbers: ["Best average F1 0.403 for Kannada-English span identification (p.5)", "Best average F1 0.405 for Tamil-English span identification (p.5)", "Inter-annotator agreement Cohen's Kappa 0.6 (p.4)", "85.55% OOV words in Tamil dataset (p.3)"]
---
## 1. Gist
DOSA (Dravidian Offensive Span Identification dataset) introduces span-level annotations for offensive content in Tamil-English and Kannada-English code-mixed YouTube comments — the first such resource for Dravidian languages. Unlike prior work that classified entire comments as offensive, DOSA identifies the specific offensive word sequences (spans) within comments, providing finer-grained attribution that assists human moderators. The dataset comprises 4,786 Tamil-English comments with 6,202 annotated spans and 1,097 Kannada-English comments with 1,641 annotated spans. Baseline experiments with multilingual BERT-family models yield F1 scores around 0.37–0.42, demonstrating substantial room for improvement. The dataset matters for values-alignment benchmarking because it addresses content moderation in under-resourced, code-mixed language settings where existing English-centric approaches fail, revealing the cultural and linguistic specificity of what counts as offensive.

## 2. Benchmark/eval design features
**Task**: Sequence labeling — given a pre-classified offensive YouTube comment in Tamil-English or Kannada-English code-mixed text, identify the character offsets of the offensive span(s). Annotators label spans with a single CAUSE tag.

**Constructs measured**: Localized offensiveness in code-mixed text; model ability to distinguish offensive spans from non-offensive context; robustness to code-mixing, word pronunciation variants, sarcasm, and noisy text.

**Item structure**: Input is a raw code-mixed comment (already confirmed offensive); output is one or more character-offset spans corresponding to offensive words/phrases.

**Answer space**: Any contiguous token subsequence; spans can cover a single word or the entire comment.

**Ground truth**: Overlapping annotations from two annotators (only character offsets agreed upon by both are included); non-overlapping portions resolved by an annotation verifier. If all three annotators disagree, the comment is skipped.

## 3. Task format & example item
Sequence labeling (span extraction). Verbatim example with ground truth and prediction discrepancy (p.6):

Ground Truth: "Sir intha cinema madida mele dodda mattadalli prachara madbekittu. nNodi prem avru dabba film madudru hype build-up create madodralli etthida kai."
Prediction: "Sir intha cinema madida mele dodda mattadalli prachara madbekittu. nNodi prem avru dabba film madudru hype build-up create madodralli etthida kai."
(Translation: "Sir, after making this kind of movie, there was need of more publicity. Please see Mr. Prem, even after making useless movie still he is king in creating hype.")

The model missed one or more tokens at the boundary, illustrating the span-level F1 penalty for partial matches.

## 4. Scoring / grading methodology
Span/entity-level Precision, Recall, and F1 — a predicted span is correct only if it precisely matches the gold annotation character offsets. Partially correct spans receive no credit. Evaluation uses 3-fold cross-validation. This is equivalent to exact-match scoring at the span level, aligned with Pavlopoulos et al. (2021) SemEval Toxic Spans task.

## 5. Dataset construction & provenance
- **Sources**: TamilMixSentiment (Chakravarthi et al., 2020) — 15k Tamil-English YouTube comments; KanCMD (Hande et al., 2020) — 7k Kannada-English YouTube comments. Only comments already labeled as offensive were used.
- After filtering non-code-mixed comments: 9,049 Tamil-English and 1,311 Kannada-English offensive comments eligible.
- Final annotation: 5,000 Tamil-English + all 1,311 Kannada-English comments.
- **Annotators**: 15 recruited; 6 final (all native speakers of Tamil, Kannada, or both). Two served as annotation verifiers. Educational backgrounds: Bachelor's or Master's level. Iterative batches of 500 with quality checks.
- **Personal data**: All user tags/personal info anonymized; annotators informed of offensive content and allowed to withdraw.
- **Size**: Tamil-English 4,786 comments / 6,202 spans; Kannada-English 1,097 comments / 1,641 spans (p.4).
- **Availability**: https://github.com/manikandan-ravikiran/DOSA

## 6. Validity evidence
- Inter-annotator agreement: Cohen's Kappa = 0.6 on annotated tokens (moderate agreement) (p.4).
- Disagreement resolution: third annotator adjudicates; if all three disagree the comment is excluded.
- No external validation against human performance baselines beyond the annotation agreement measure.
- Baseline experiments on 6 multilingual models confirm low but consistent performance across folds, suggesting the task is genuinely difficult.

## 7. Saturation / discrimination
All baseline models perform poorly: best average F1 is ~0.40 for both language pairs (p.5), far from saturation. There is significant headroom. Errors cluster around: (1) complete-sentence annotations (span boundary misses); (2) pronunciation variants (same abusive meaning, different spelling); (3) noisy text with hashtags; (4) sarcastic comments. The Kannada-English models are especially prone to overfitting due to the smaller dataset size.

## 8. Multiturn / agentic aspects
n/a — single-turn span extraction task on static text.

## 9. Key numbers
- Tamil-English: 4,786 comments, 6,202 annotated spans, 22,096 unique tokens (p.4)
- Kannada-English: 1,097 comments, 1,641 annotated spans, 7,781 unique tokens (p.4)
- Average span size: ~21 characters for Tamil-English, ~20 for Kannada-English (p.4)
- OOV rate: 85.55% Tamil, 84.23% Malayalam, 83.03% Kannada (p.3)
- Best Kannada-English F1: BERT-M2 and XBERT-M1 both 0.403 average (p.5)
- Best Tamil-English F1: DBERT-M1 0.405 average (p.5)
- Cohen's Kappa inter-annotator agreement: 0.6 (p.4)
- XLM-RoBERTa-large-xnli-anli (XBERT-M2) Tamil-English average F1: 0.266 (worst) (p.5)

## 10. Pitfalls & limitations
- Small Kannada-English dataset leads to severe overfitting; several models saturate at training loss 0.1 (p.6).
- No hyperparameter tuning; baseline only.
- No simpler baselines (LSTM-CRF variants) provided (p.7).
- Only exact-span F1 used; partial credit metrics not reported.
- Inter-annotator Kappa of 0.6 is only moderate — some subjectivity in span boundaries.
- Dataset is restricted to pre-labeled offensive comments; span annotation on mixed (offensive + non-offensive) corpora would better mimic real moderation.
- Sarcasm and complete-comment annotations remain unresolved challenges.

## 11. Novel ideas worth stealing
- **Span-level annotation of offensive content** rather than document-level labels provides attribution that human reviewers need — a design move applicable to any values benchmark requiring explainability.
- **Overlapping-only ground truth creation**: using character-level overlap consensus (rather than majority vote on discrete labels) gives a conservative, high-precision ground truth for span tasks.
- **Iterative annotator quality control in batches of 500**: enables early detection and removal of low-quality annotators before the full dataset is contaminated.
- **Code-mixed corpora re-annotation**: building span resources by re-annotating existing coarser-grained datasets is cost-efficient and enables multi-task learning.
- **Documenting annotator demographics** (education, language medium, accent knowledge) enables post-hoc analysis of annotator-level biases — a practice that values benchmarks should adopt universally.

## 12. Notable quotes
- "emphasizing such offensive spans can assist human moderators who often deal with lengthy comments and prefer attribution instead of just a system-generated unexplained score per post." (p.1)
- "We achieved an inter-annotator agreement of 0.6 for the annotations." (p.7)
- "Both Tamil-English and Kannada-English, we found that comments with only one or more profane words causing offensiveness were correctly identified in their spans. However, for both Tamil-English and Kannada-English, we can see overall lower results for which one of the reasons we thought was the nature of code-mixed text themselves." (p.6)
- "the proportion of out-of-vocabulary (OOV) words (including code-mixed, English and misspelt words) in the dataset as 85.55%, 84.23% and 83.03% in Tamil, Malayalam and Kannada respectively." (p.3)

## 13. UNKNOWN / not in extract
- License details for the released dataset.
- Whether the full 9,049 Tamil-English or only the 4,786 annotated subset is included in the release.
- Performance of LSTM-CRF baselines (explicitly deferred to future work).
- Results on the development split separately from test.
- Human performance upper bound on the span identification task.
