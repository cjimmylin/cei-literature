---
stem: "2019-Fortuna-A Hierarchically-Labeled Portuguese Hate Speech Dataset"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [design-space, validity-psychometrics, cultural-linguistic, normative-ethics]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 5668
dataset_construction: "crowdsourced"
languages: ["pt"]
models_tested: ["LSTM + word embeddings + xgBoost"]
headline_numbers:
  - "5,668 Portuguese tweets annotated; 31.5% labeled hate speech in binary annotation (p.4)"
  - "Binary annotation Fleiss's Kappa = 0.17 (low, non-expert annotators) (p.4)"
  - "Hierarchical annotation Cohen's Kappa = 0.72 (expert annotator subset of 500 messages) (p.5)"
  - "81 hate speech categories in total across 4 levels of hierarchy (p.1)"
  - "Binary classification test set F1-score = 0.72; cross-validation F1 = 0.78 (p.8)"
---
## 1. Gist
Fortuna et al. (2019, University of Porto / Pompeu Fabra University) present a Portuguese Twitter hate speech dataset of 5,668 tweets with two annotation schemes: a binary non-expert annotation (hate vs. not hate) and a fine-grained hierarchical expert annotation using 81 categories organized as a Rooted Directed Acyclic Graph (rooted DAG). The key innovation is the hierarchical, intersectional taxonomy that captures overlapping hate speech types (e.g., "fat women" inherits from both "sexism" and "body"). The paper matters for values-alignment benchmarking as a rare non-English hate speech resource that introduces an ontological structure for content moderation labels, enabling multi-label and hierarchical classification with explicit intersectionality modeling.

## 2. Benchmark/eval design features
- **Two annotation tiers**:
  - *Binary*: 18 non-expert Portuguese native speakers (student volunteers); 3 annotators per tweet; majority vote; 31.5% labeled hate speech. Fleiss's Kappa = 0.17.
  - *Hierarchical*: One expert annotator (researcher with social psychology training) built and applied a rooted DAG with 81 categories; second annotator verified 500 messages; Cohen's Kappa = 0.72.
- **Hierarchy structure**: Rooted DAG where each node can have multiple parents, enabling intersectional classification. Root = "hate speech"; Level-1 nodes = Sexism, Body, Origin, Homophobia, Racism, Ideology, Religion, Health, Other-Lifestyle (Table 1, p.5); further subdivisions to terminal nodes.
- **Multi-label**: Instances assigned to both terminal and non-terminal nodes; intersectional classes (e.g., "fat women" ∈ {Women, Fat people}).
- **Baseline classification**: LSTM + pre-trained GloVe (Portuguese) + xgBoost; 10-fold cross-validation.

## 3. Task format & example item
Binary annotation guideline (non-expert), from Appendix A.1 (p.11):
> Tweet: "Black people should go back to their land!!" → HS label: 1
> Tweet: "Meat and black beans are delicious!" → HS label: 0
> Tweet: "Muslim people are terrorists!" → HS label: 1

Annotators marked each tweet with 1 (hate speech) or 0 (not hate speech) per the provided guidelines.

## 4. Scoring / grading methodology
- Binary classification: F1-score (micro-averaged) on test set and cross-validation folds.
- Hierarchical annotation validity: Cohen's Kappa per class (Table 2, p.6).
- Binary baseline: CV F1 = 0.78, test set F1 = 0.72 (Table 4, p.8).
- No systematic metrics reported for the hierarchical classification task in experiments (binary only).

## 5. Dataset construction & provenance
- Crawled from Twitter via Search API on 8–9 March 2017 using 19 keywords, 10 hashtags, and 29 profiles focused on hate speech in Portuguese. (p.4)
- 42,930 initial messages collected; filtered for Portuguese, deduplicated, removed short/HTML content → 33,890 tweets. (p.4)
- Sampled to max 200 tweets per search instance for diversity; final dataset: 5,668 tweets from 1,156 users. (p.4)
- >95% of tweets from January–March 2017. (p.4)
- Dataset publicly available on GitHub for research purposes; tweet IDs anonymized (no tweet_id in release) to protect user privacy. (p.8)
- Binary annotation: 18 non-expert student volunteers, Fleiss's Kappa = 0.17.
- Hierarchical annotation: single expert researcher + one verification annotator on 500-tweet sample.
- Hierarchical dataset: 22% hate speech instances (vs. 31.5% in binary). (p.5)

## 6. Validity evidence
- Binary inter-annotator agreement (Fleiss's Kappa = 0.17) is low, attributed to task difficulty for non-experts and the subtlety of hate speech vs. offensive language. (p.4)
- Hierarchical agreement (K = 0.72) is substantially higher with expert annotators but measured only on a 500-message sample. (p.5)
- Agreement varies substantially by category (Table 2): Lesbians K = 0.879, Health K = 0.856, Homophobia K = 0.823 vs. Gays K = 0.300, Ugly women K = 0.276, Origin K = 0.329. (p.6)
- Baseline classification achieves "state-of-the-art outcome" for the Portuguese hate speech task, validating dataset utility. (p.8)

## 7. Saturation / discrimination
- The dataset is biased toward sexism/homophobia (most common categories) and sparse for some terminal nodes (many categories with 1–5 instances in Table 3). (p.7)
- Majority classes: Sexism (672), Women (544), Homophobia (322), Homosexuals (288), Lesbians (248). Minority classes: many terminal nodes with 1–4 instances.
- The hierarchical structure is a design solution for rare-class sparsity: rare terminal nodes still contribute to parent-class training data.
- Binary test set: 567 instances; some categories have single instances and cannot be reliably modeled.

## 8. Multiturn / agentic aspects
n/a — single-tweet classification.

## 9. Key numbers
- 5,668 total tweets; 1,156 unique users (p.4)
- Binary annotation: 31.5% hate speech; Fleiss's Kappa = 0.17 (p.4)
- Hierarchical annotation: 22% hate speech; K = 0.72 on 500-message sample (p.5)
- 81 total hate speech categories across ≥4 hierarchy levels (p.1)
- 9 Level-1 hate speech subtypes (Table 1, p.5)
- Binary classification: CV F1 = 0.78; test F1 = 0.72; training N = 5,099; test N = 567 (p.8)
- Top classes by frequency: Sexism 672, Women 544, Homophobia 322, Homosexuals 288, Lesbians 248 (Table 3, p.7)

## 10. Pitfalls & limitations
- Low binary inter-annotator agreement (K = 0.17) raises concerns about label reliability for the primary annotation layer used in experiments. (p.4)
- Hierarchical annotation performed by a single expert; second annotator verified only 500 of 5,668 messages. (p.5)
- Sampling bias: Twitter API provides only a subset of posts; keyword/profile-based crawling skews toward explicitly marked hate speech. (p.8)
- Dataset not representative of all Portuguese hate speech; coverage of minority categories is very sparse (many single-instance nodes).
- Only tweets from a short time window (Jan–Mar 2017); may not generalize to other periods.
- No hierarchical classification experiments conducted; hierarchical annotation remains under-utilized in reported experiments.
- Privacy: tweet IDs removed, but text searchable; real user privacy still at risk.
- The paper notes the "open coding" methodology for building the hierarchy relied on a single researcher's judgment, which may introduce perspective-specific biases.

## 11. Novel ideas worth stealing
1. **Rooted DAG (not tree) for label ontology**: Allows intersectional labels (a node can have multiple parents) so that "fat women" inherits from both "sexism" and "body." For values-alignment benchmarks covering overlapping harm categories, DAG structure avoids forcing arbitrary single-category decisions and enables both fine-grained and coarse-grained evaluation.
2. **Two-tier annotation for difficult/subjective tasks**: Use non-expert annotators for a quick binary pass to establish rough ground truth, then deploy expert annotators for nuanced fine-grained labeling on the same data. This staggers annotation cost and also reveals which categories require expert judgment by comparing agreement levels.
3. **Inter-annotator agreement stratified by category**: Report K per label rather than a single aggregate K. Categories with low K are conceptually ambiguous and should receive more annotator training or have their definitions tightened before use in benchmarks.
4. **Keyword + profile dual crawl strategy**: Combining keyword-based search (broader coverage) with hate-oriented account crawling (higher density of target content) is an efficient way to build a dataset with high positive-class representation without sacrificing diversity.
5. **Rare-class preservation through hierarchy**: By organizing rare categories under common parents, models can still learn about uncommon identity groups from limited examples. A practical solution for the long tail of minority identity categories in any benchmark.

## 12. Notable quotes
- "Hate speech is language that attacks or diminishes, that incites violence or hate against groups, based on specific characteristics such as physical appearance, religion, descent, national or ethnic origin, sexual orientation, gender identity or other, and it can occur with different linguistic styles, even in subtle forms or when humour is used." (p.2)
- "We observed a low agreement with a value of K = 0.17. We think that this low value is the result of relying exclusively on non-expert annotators for classifying hate speech." (p.4)
- "Distinct types of hate speech present different agreement levels between annotators. Therefore, future guidelines for annotation may benefit from specifying the particularities of the different subtypes of hate speech." (p.8)
- "By classifying discrimination against both black people and refugees simply as 'racism', we ignore that in this case, different characteristics with a different motivation are targeted." (p.2)

## 13. UNKNOWN / not in extract
- Full numerical content of Table 3 for minority classes (some values listed but many truncated in OCR).
- The specific annotation guidelines given to expert hierarchical annotators (only non-expert guidelines in Appendix A.1).
- Whether the dataset is still available at the GitHub link and current license terms.
- Performance breakdown for hierarchical classification (no experiments on multi-label hierarchical task reported).
- Demographic breakdown of the 18 non-expert annotators beyond "Information Science students."
- Any analysis of temporal drift or cross-cultural validity of Portuguese hate speech categories.
