---
stem: "2018-Ljubesic-Datasets of Slovene and Croatian Moderated News Comments"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 24639651
dataset_construction: "scraped"
languages: ["sl", "hr"]
models_tested: ["fastText"]
headline_numbers:
  - "MMC dataset: 7,596,686 comments; 8.3% deleted (p.2, Table 1)"
  - "STY dataset: 17,042,965 comments; 1.8% deleted (p.2, Table 1)"
  - "Combined: ~24.6 million comments, 732 million words (p.2, Table 1)"
  - "fastText ROC AUC: 0.794 (MMC) and 0.793 (STY) on test set (p.7)"
  - "Character n-grams (3-7) reduced error rate by 18% on both datasets (p.7)"
---
## 1. Gist
Ljubešić et al. (2018) present two large datasets of moderated online news comments in under-resourced Slavic languages — Slovene (MMC RTV, 7.6 million comments from 2010–2017) and Croatian (24sata, 17 million comments from 2007–2021) — where deleted comments serve as proxies for inappropriate content. The datasets are published in encrypted form to enable research without propagating harmful content. The paper analyzes deletion patterns by user, thread, and position within threads, and builds fastText baseline classifiers. For values-alignment benchmarking, the paper is relevant as a multilingual abusive-language resource and as a methodological study of how moderation behavior varies across cultures, platforms, and time.

## 2. Benchmark/eval design features
This is a dataset paper with baseline classification experiments. Core design: binary classification of comments as deleted (inappropriate) or retained (appropriate), using platform moderators' actual deletion decisions as labels. Annotation schema for a sample of 100 deleted comments per dataset uses 9 categories: calumniation, discrimination, disrespect, hooliganism, insult, irony, swearing, threat, other (from Pavlopoulos et al., 2017). Statistical analyses of deletion distributions test whether deletion is random or structured by user, thread, and position within thread using Kolmogorov-Smirnov tests and Wasserstein distances.

## 3. Task format & example item
Binary text classification task: given a news comment, predict whether it was deleted by moderators (1) or retained (0). No example items quoted in the extract (content is encrypted in the released dataset). The annotation example from manual analysis: MMC deleted comments most frequently contain "disrespect" (37/100 sample); STY deleted comments most frequently contain "insult" (42/100 sample, often combined with swearing).

## 4. Scoring / grading methodology
ROC AUC evaluated on test set (80/10/10 train/dev/test split at thread level to prevent data leakage across threads). Hyperparameter tuning on dev set. Final models: fastText with character n-grams (length 3–7), optimized epochs. ROC AUC chosen as threshold-independent metric: 0.5 = random, 1.0 = perfect. Results: 0.794 (MMC) and 0.793 (STY). Described as "promising, but still far from satisfying" for production use.

## 5. Dataset construction & provenance
MMC: Slovenian national broadcaster (RTV MRC) provided CSV dump of all comments from 2010–2017 including deleted comments. STY: Croatian commercial newspaper (24sata, owned by Styria Media International) provided SQL dump from 2007–2021. Both datasets cleaned (removed formatting errors, illegal UTF-8 characters), converted to XML. Published on CLARIN.SI repository in encrypted form (bijective character substitution mapping not disclosed). Baseline models trained on non-encrypted full text released separately. User metadata pseudo-anonymized; article text not available (copyright).

## 6. Validity evidence
Manual annotation of 100 random deleted comments per dataset by same annotator using Pavlopoulos et al.'s 9-category schema provides face validity for the deletion signal. Statistical tests (Kolmogorov-Smirnov + Wasserstein distance) confirm deletion is non-random with respect to user, thread, and position, supporting the signal's reliability. No inter-annotator reliability for the 100-comment samples (single annotator). The natural deletion rate in STY (~1.8%) required no artificial balancing; in MMC (~8.3%) also unbalanced.

## 7. Saturation / discrimination
AUC ~0.79 on both datasets indicates substantial headroom for improvement. The authors explicitly note this is "far from satisfying" for production systems. Deletion rates are very low (~1.8–8.3%), creating strong class imbalance. Most impactful hyperparameter improvement: adding character n-grams of length 3–7 reduced error rate by 18% on both datasets (vs. word unigrams default).

## 8. Multiturn / agentic aspects
Partial: the position-in-thread analysis shows deletion is more likely at the beginning of threads than later, counter to the expectation that discussions "heat up" gradually. This is a weak thread-level dependency. No modeling of conversational dynamics is attempted.

## 9. Key numbers
- MMC: 42,502 users; 7,596,686 comments; 325,225,576 words; 8.3% deleted (p.2, Table 1)
- STY: 185,266 users; 17,042,965 comments; 407,549,127 words; 1.8% deleted (p.2, Table 1)
- Combined: ~24.6 million comments; 732 million words; 3.8% deleted (p.2, Table 1)
- MMC manual annotation: 105 category labels assigned to 100 deleted comments (disrespect 37, irony 19, other 19, discrimination 11, insult 10, calumniation 6, swearing 3) (p.3, Table 2)
- STY manual annotation: 124 labels for 100 comments (insult 42, other 18, discrimination 10, disrespect 21, swearing 14, irony 10, calumniation 8) (p.3, Table 2)
- KS test statistics for user distribution: MMC 0.274, STY 0.371 (both p ≈ 0.0) (p.4)
- Wasserstein distances for user distribution: MMC 0.068, STY 0.032 (p.4)
- fastText baseline AUC (default): MMC 0.755, STY 0.746 (p.7, Table 3)
- fastText with char ngrams 3-7: MMC 0.798, STY 0.791 (p.7, Table 3)
- Test set AUC (final): MMC 0.794, STY 0.793 (p.7)

## 10. Pitfalls & limitations
- Single annotator for the 100-comment manual analysis — no inter-annotator reliability reported
- Encryption prevents direct text analysis or transfer learning on released datasets; only encrypted experiments possible
- Platform deletion policies changed significantly over time in STY (most deletions concentrated in 2016–2017 after policy tightening), creating temporal non-stationarity
- Deletion decisions conflate hate speech with off-topic content, spam, and other violations — no fine-grained label decomposition
- News articles not available (copyright), preventing topic-conditioned analysis
- Slovene and Croatian are closely related South Slavic languages — findings may not generalize to more diverse language pairs
- No demographic information on commenters

## 11. Novel ideas worth stealing
- **Thread-level train/test split**: splitting at the thread rather than comment level prevents data leakage from conversational context — applicable to any comment moderation benchmark.
- **Encrypted dataset release**: allows research on sensitive content without propagating it; the bijective character mapping enables exact-match experiments in controlled settings while protecting harmful content. Relevant design for future benchmark releases of toxic or sensitive material.
- **Separately releasing baseline models** (trained on non-encrypted data): lets practitioners use the models for feature extraction or direct deployment without access to the training text.
- **Multilingual paired design** (same annotation scheme, same platform type, different languages/cultures): enables cross-cultural comparison of inappropriateness norms — a model for values benchmarks that want to test cultural variation in harm judgments.
- **Deletion rate as proxy for inappropriateness** from diverse real-world platforms: avoids the need for additional human annotation while providing authentic behavioral signal about moderation norms.

## 12. Notable quotes
- "The two portals adopt somewhat different deletion policies: for MMC almost half of the users had at least one comment deleted, while under 10% had a comment deleted in STY." (p.2)
- "In general, the Croatian sample of deleted comments contains worse forms of inappropriate content compared to the Slovene one (e.g., many more cases of insults and swearing compared to more subtle irony which is particularly common in the Slovene sample)." (p.3)
- "We showed that the distribution of deleted content among users is the least random, followed by the distribution of that content among threads, with the location of the deleted content being closest to random. This shows that specific users seem to be the most deleted, followed by specific threads." (p.7)
- "Adding character n-grams of length 3 to 7 we lower the error rate on both datasets by 18%." (p.7)

## 13. UNKNOWN / not in extract
- Inter-annotator reliability for the 100-comment manual annotation samples
- Whether the character replacement encryption preserves morphological features (relevant for Slavic languages with rich inflection)
- Performance breakdown by content category (disrespect vs. insult vs. swearing etc.)
- Whether the fastText models have been used or improved by subsequent researchers
- Comparison with English hate speech detection systems on comparable tasks
