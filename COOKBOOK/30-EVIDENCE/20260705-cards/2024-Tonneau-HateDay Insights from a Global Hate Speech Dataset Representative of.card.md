---
stem: "2024-Tonneau-HateDay Insights from a Global Hate Speech Dataset Representative of"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, cultural-linguistic, contamination-robustness, llm-judges-scoring]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 240000
dataset_construction: "crowdsourced"
languages: ["Arabic", "English", "French", "German", "Indonesian", "Portuguese", "Spanish", "Turkish"]
models_tested: ["Llama 3.1 8B", "Aya 23 8B", "Perspective API", "various open-source HuggingFace classifiers"]
headline_numbers:
  - "Average precision on HATEDAY is 9.4%, versus 40% on academic datasets and 87.2% on functional tests (p.5)"
  - "Hate speech prevalence averages 0.7% across all languages/countries in HATEDAY (p.3)"
  - "European languages average 23.1% AP on HATEDAY vs non-European 9.3% (p.5)"
  - "Alignment between academic target coverage and real-world prevalence correlates with performance at Pearson's r=0.76, p=0.003 (p.6)"
  - "Moderating >80% of hate requires human review of at least 10% of all daily tweets (p.7)"
---
## 1. Gist
HATEDAY is the first global hate speech dataset built from a random, representative sample of Twitter traffic — 240,000 tweets drawn from all posts on September 21, 2022, covering eight languages and four English-speaking countries. By comparing model performance on this representative sample against standard academic datasets and functional tests, the paper provides the most rigorous empirical demonstration to date that academic benchmarks dramatically overestimate real-world hate speech detection performance. Average precision drops from ~87% on functional tests and ~40% on academic datasets to just 9.4% on HATEDAY. The paper identifies the hate/offensive speech distinction, misalignment of target categories, and language resource gaps as key drivers, with major implications for both hate speech moderation design and the general problem of benchmark validity in NLP.

## 2. Benchmark/eval design features
The study evaluates hate speech detection models on three settings: (1) HATEDAY (HD) — a representative sample, 20,000 tweets per language/country; (2) Academic Datasets (AD) — existing hate speech corpora combined into per-language supersets; (3) HateCheck (HC) — functional test suites for six of the eight languages. The primary evaluation metric is average precision (area under precision-recall curve), chosen for suitability with severe class imbalance. The three-class annotation scheme (hateful, offensive, neutral) with free-text target labels captures the key offensive/hate distinction that bedevils deployed classifiers. Models evaluated include supervised transformers fine-tuned on hate speech, zero-shot LLMs (Aya23 8B, Llama3.1 8B), and the Perspective API.

## 3. Task format & example item
Binary/three-class classification task on tweets. Example items from Table 1 (p.3):

- Class: Hateful, Target: Politics — "Greens are vermin" (German)
- Class: Hateful, Target: National Origin — "Venezuelans are useless" (Spanish)
- Class: Hateful, Target: Gender — "I hate women" (Portuguese)
- Class: Offensive — "Stop spewing rubbish, fool." (Nigeria)
- Class: Neutral — "Reunited by the mercy of God" (Turkish)

Annotators assigned each tweet to hateful/offensive/neutral, with free-text target labels for hateful tweets.

## 4. Scoring / grading methodology
Majority vote of three annotators per tweet; Krippendorff's α threshold of 0.7 required during pilot phase before proceeding to main annotation. Overall annotators agreed on 93.4% of all labeled tweets; 6.4% had 2/3 agreement; 0.2% had full disagreement (p.3). Model evaluation uses average precision (AP = area under precision-recall curve), which appropriately handles severe class imbalance (hate speech prevalence ~0.7%). Models are compared across three dataset types: HD, AD, and HC.

## 5. Dataset construction & provenance
Built from TWITTERDAY (Pfeffer et al., 2023), a crawl of all ~375 million tweets in a 24-hour window. Language filtering used automated detection; country filtering used Google Geocoding API on self-reported user locations. Retweets excluded; 20,000 random tweets sampled per language/country stratum. 36 annotators (three per language/country) recruited with diversity of origins for global languages. Pilot phase required Krippendorff's α ≥ 0.7. Dataset available at https://huggingface.co/datasets/manueltonneau/hateday. Note: Kenya and Nigeria lacked existing academic hate speech supersets, so authors constructed these (p.4). Final size: 240,000 annotated tweets (12 strata × 20,000).

## 6. Validity evidence
Strong face validity: representative random sample directly mirrors real-world Twitter. Cross-lingual comparison enabled by uniform annotation scheme. IAA is high: annotators agreed on 93.4% of cases across all languages/countries (p.3). The strong correlation between academic target coverage alignment and real-world performance (r=0.76, p=0.003) provides evidence that the dataset is capturing a theoretically meaningful signal, not measurement noise (p.6). No formal factor analysis reported.

## 7. Saturation / discrimination
Hate speech is rare: average prevalence of 0.7% across strata (p.3). This creates extreme class imbalance making discrimination very challenging — the entire study motivation is that existing benchmarks inflate scores by oversampling positive examples. On HATEDAY, no model achieves F1 >0.47 in any context (p.5). The discriminative challenge is genuine: offensive content (2.5–19× more prevalent than hate) consistently appears in the top of hate score distributions, degrading precision (p.5). Non-European languages show the lowest performance (Arabic, Indonesian, Turkish: ~9% AP) indicating under-resourced and under-studied portions of the evaluation space.

## 8. Multiturn / agentic aspects
n/a. Single-tweet classification only. However, the paper notes that many reply tweets lack context (p.9), indicating a gap in the current framework that could be addressed by future multiturn/contextual annotation designs.

## 9. Key numbers
- 240,000 total tweets, 12 strata of 20,000 each (p.2)
- Hate prevalence: average 0.7%, range 0.2% (Kenya/Nigeria) to 1.7% (India) (p.3)
- AP on HD: 9.4% avg; on AD: 40%; on HC: 87.2% (p.5)
- European languages AP on HD: 23.1%; non-European: 9.3% (p.5)
- Offensive content makes up 32.3% of top 50 scored tweets on average (p.5)
- Pearson's r between academic-real-world target alignment and performance: 0.76, p=0.003 (p.6)
- Correlation between dataset size and HD performance: r=-0.47, p=0.127 (not significant) (p.6)
- To moderate >80% of hate: requires reviewing ≥10% of daily tweets (p.7)
- Number of hateful examples in HATEDAY per stratum: 31 (Kenya) to 430 (India) (p.9)
- 36 annotators recruited, IAA threshold Krippendorff's α ≥ 0.7 required (p.3)

## 10. Pitfalls & limitations
- Very few positive examples per stratum (31–430 hateful tweets), making performance estimates uncertain with wide confidence intervals (p.9).
- Single platform (Twitter), single day: limits generalizability to other platforms and timespans (p.9).
- Text-only: ignores image/video hate speech (p.10).
- Country-level representativeness imperfect due to language detection and geolocation errors (p.10).
- Some hate may have been pre-moderated by Twitter before collection window (posts collected 10 minutes after posting) (p.10).
- Zero-shot prompts not varied — other prompts might yield different LLM performance (p.10).
- Analysis limited to public models; platforms have private models and user-history signals that may perform better (p.10).

## 11. Novel ideas worth stealing
1. **Representative sampling as the gold standard**: Build the evaluation set from a random sample of real-world content rather than keyword-seeded or adversarially curated examples. This provides ecological validity and reveals the true class imbalance that deployed systems face.
2. **Three-way hate/offensive/neutral taxonomy**: The distinction between offensive (no identity target) and hateful (targeting identity group) is critical for precision; conflating them inflates model scores.
3. **Target category alignment metric**: Measuring cosine similarity between academic dataset target distribution and real-world target prevalence as a predictor of performance gap — a portable diagnostic for benchmark validity.
4. **Cost-recall tradeoff visualization**: Plotting review rate vs. hate recall under human-in-the-loop moderation as a policy-relevant output alongside standard precision/recall — directly useful for resource planning in deployed systems.
5. **Stratified evaluation across languages AND countries sharing a language**: Separating English (global), US English, India English, Nigeria English, Kenya English reveals that language-level averages mask significant country-level variation, an under-appreciated granularity for cross-cultural benchmarks.
6. **Average precision as primary metric with severe class imbalance**: AP is more informative than F1 or accuracy when positives are <1% of data — transferable lesson for any benchmark where the harmful behavior is rare.

## 12. Notable quotes
- "average precision is just 9.4% on HD, compared to 40% on AD and 87.2% on HC." (p.5)
- "we find a strong and significant positive correlation between this alignment and detection performance (Pearson's r: 0.76, p = 0.003). This indicates that the better hate speech detection resources reflect hate target coverage in real-world social media data for a given language or country, the higher the detection performance." (p.6)
- "We find that successfully moderating a large share of all hateful content (>80%) using the best publicly available detection models would require human review of at least 10% of all daily tweets." (p.7)
- "our results highlight the need to evaluate NLP tools in realistic settings, especially where human harm might arise. This applies more broadly to the detection of harmful content on social media, such as misinformation... as well as the evaluation of the bias and safety of generative large language models... both of which have relied so far on non-representative benchmarks for evaluation." (p.7)

## 13. UNKNOWN / not in extract
- Full per-model breakdown for all 12 strata not included in main paper (referenced as Appendix §E.2, not in extract).
- Precision-recall curves (Figure 5) are in the appendix, not in the extracted portion.
- Full annotator demographics and diversity details (§B.1 referenced but not extracted).
- Full annotation guidelines taxonomy (§B.2 referenced but not extracted).
- Confidence intervals on all per-stratum results (Tables 5 and 6 referenced but not extracted).
- Exact dataset license/terms of use beyond "research purposes only."
