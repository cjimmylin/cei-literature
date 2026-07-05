---
stem: "2020-Yasseri-Detecting Weak and Strong Islamophobic Hate"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, saturation-discrimination, religious-values]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 1341
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: ["Naïve-Bayes", "Random Forests (trees=10,100,1000)", "Logistic Regression", "Decision Trees", "SVM (one-against-one, radial kernel)", "Deep Learning (feed-forward)"]
headline_numbers:
  - "Classifier accuracy on unseen data: 77.3%; balanced accuracy: 83% (p.5)"
  - "Fleiss' kappa on training annotations: 0.837; Krippendorf's alpha: 0.895 (p.3)"
  - "Domain-specific GloVe embeddings outperform generic GloVe by 5.9 percentage points (69.13% vs 63.2%; p.3)"
  - "SVM outperforms Deep Learning by 1.03 percentage points (72.17% vs 71.14%; p.4)"
  - "Applied to 109,488 far-right tweets: 36,963 weak Islamophobic vs 14,895 strong Islamophobic (p.5)"
---
## 1. Gist
This paper presents a three-class classifier distinguishing non-Islamophobic, weakly Islamophobic, and strongly Islamophobic content on Twitter, trained on 1,341 annotated tweets (downsampled from 4,000). The key theoretical contribution is moving beyond binary hate-speech detection to distinguish between strong Islamophobia (explicit negativity against all Muslims) and weak Islamophobia (either subtle/indirect negativity against all Muslims, or explicit negativity against a specific subset). The classifier achieves 77.3% accuracy and 83% balanced accuracy on unseen data and is applied to 109,488 tweets from 45 far-right Twitter accounts in 2017. For values-alignment benchmarking, this paper demonstrates the importance of fine-grained hate intensity scales over binary labels, the value of domain-specific training corpora, and the difficulty of distinguishing gradations within a single hate target even with expert annotators.

## 2. Benchmark/eval design features
Three-class classification task: None / Weak Islamophobic / Strong Islamophobic. Weak is further defined as (a) subtle/indirect negativity against all Muslims OR (b) explicit negativity against a specific subset of Muslims. Strong is explicit negativity against all Muslims. Feature selection is theoretically motivated (not just grid-searched): text (one-hot), non-text (50 surface/derived features including sentiment, swear words, POS, named entities, Muslim names, mosque mentions), and domain-specific GloVe embeddings trained on 140M tweets from UK political Twitter.

## 3. Task format & example item
Binary/multi-class annotation of tweets. Three expert annotators (experts in UK politics and prejudice).

Category definitions (p.2):
- Strong Islamophobic: "Speech which explicitly expresses negativity against all Muslims" — e.g., describing Muslims as barbarians, calling for Muslims to be banned from the UK.
- Weak Islamophobic (type 1): "Speech which weakly expresses negativity against all Muslims" — e.g., commenting on Muslims being "different" or having unusual cultural practices.
- Weak Islamophobic (type 2): "Speech which explicitly expresses negativity against a specific subset of Muslims" — e.g., sharing a news story about a terrorist attack while foregrounding the perpetrator's Muslim identity.

No verbatim tweet items are provided in the extract.

## 4. Scoring / grading methodology
Ten-fold cross-validation on training data (n=1,341). Metrics: accuracy, balanced accuracy (Velez et al., 2007), precision, recall, F1 using macro-aggregation (each class weighted equally). For unseen data validation: 300 tweets sampled from classifier predictions (100 per class), re-annotated blind by original annotators (95% perfect agreement). Final model (model 7): domain-specific GloVe + 6 non-text features (mosque mentions, HTML presence, RT presence, conjunction POS, location NER, organization NER) + one-against-one SVM.

## 5. Dataset construction & provenance
Training corpus: 140M tweets collected from followers of UK political parties (UKIP, Conservatives, Labour, Liberal Democrats, BNP, Britain First) and mentions of 45 far-right accounts during 2017. 4,000 tweets sampled for annotation (including 1,000 from keyword searches for "Muslims" and "Islam" to oversample hate content). Annotated blind by three experts using iteratively developed guidelines (two 200-tweet pilot rounds). Final training dataset: 1,341 tweets (downsampled to balance classes: 447 None + 484 Weak + 410 Strong). Test application: 109,488 tweets from 45 far-right accounts during 2017.

## 6. Validity evidence
Inter-rater agreement on training annotations: percentage agreement 89.9%, Fleiss' kappa 0.837, Krippendorf's alpha 0.895 (p.3). Category-wise Fleiss' kappa: Weak Islamophobia κ=0.737 (hardest), Strong Islamophobia κ=0.907 (easiest). The classifier's performance improves slightly from cross-validation to unseen data (accuracy 74.6% → 77.3%; balanced accuracy 80.7% → 83%), which the authors interpret as evidence of generalizability rather than overfitting (p.5). Model explainability is explicitly prioritized: only theoretically justified input features are included.

## 7. Saturation / discrimination
The hardest confusion is between Weak and adjacent classes: of 100 Strong tweets, 23 are classified as Weak; of 100 Weak tweets, 22 are classified as None (Figure 1, p.5). The classifier performs best at distinguishing None from Strong. The Weak class is the most problematic both for models and annotators (lowest kappa). Confusion between weak/subtle hate and non-hate is the fundamental discrimination challenge, reflecting real conceptual ambiguity. Applied to far-right tweets: majority are not Islamophobic (57,630), with weak >> strong (36,963 vs 14,895) — consistent with gradation hypothesis.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- Training dataset size (balanced): 1,341 tweets (p.3)
- Original annotated pool: 4,000 tweets (p.3)
- Fleiss' kappa: 0.837; Krippendorf's alpha: 0.895 (p.3)
- Weak Islamophobia kappa: 0.737; Strong: 0.907 (p.3)
- Domain-specific GloVe accuracy: 69.13% vs generic GloVe: 63.2% (+5.93 pp; p.3)
- SVM accuracy: 72.17% vs Deep Learning: 71.14% (p.4)
- Final model (model 7) accuracy on unseen data: 77.3%; balanced accuracy: 83% (p.5)
- Application corpus: 109,488 far-right tweets (p.5)
- Weak Islamophobia in application: 36,963; Strong: 14,895; None: 57,630 (p.5)
- Keyword-searched tweets in training: 1,000 of 4,000 (p.3)
- In unseen data validation: 95% of 300 cases had all three annotators in perfect agreement (p.5)

## 10. Pitfalls & limitations
- Training corpus is specific to UK far-right Twitter (2017); classifier generalizability to other contexts (different countries, time periods, platforms) is not tested.
- The Weak Islamophobia class is conceptually heterogeneous — it combines two distinct phenomena (subtle generalised negativity and explicit targeted negativity against a subset), which may hinder model learning.
- The classifier performance on Weak class remains lowest (22% misclassified as None; 23% of Strong misclassified as Weak), and the boundary between weak and strong hate is genuinely ambiguous.
- The training set is small (1,341 after downsampling) and the authors note plans to increase its size.
- No cross-platform testing (classifier is trained on Twitter, applied to Twitter only).
- The paper was written in 2018/2020 and uses GloVe embeddings; transformer-based approaches are not tested.

## 11. Novel ideas worth stealing
- **Intensity/strength dimension over binary classification**: Distinguishing weak vs. strong Islamophobia (rather than hate vs. no hate) enables detection of radicalization dynamics and nuanced monitoring of hate escalation — directly applicable to values-alignment benchmarks that aim to distinguish degrees of normative violation.
- **Domain-specific corpus for embedding training**: Training word embeddings on a large topically relevant corpus (140M UK political tweets) vs. generic corpora demonstrates a 5.9pp improvement — a strong argument for domain-tailored benchmark construction rather than generic representations.
- **Theoretically justified feature selection to prevent black-box overfitting**: Including only features with prior theoretical rationale (e.g., mosque mentions as an Islamic-context proxy) is an explicit design principle for interpretable and generalizable classifiers — valuable for benchmark evaluation rubrics.
- **Mosque mention count as an engineered feature**: Novel feature derived from Wikipedia mosques pages that consistently contributed to performance — illustrates how domain knowledge can be operationalized as structured features.
- **Balanced accuracy metric for skewed multi-class evaluation**: The use of balanced accuracy (combining specificity and sensitivity) is superior to raw accuracy for imbalanced multi-class settings and should be a standard metric in hate/offense evaluation.
- **Expert annotators from relevant disciplinary backgrounds**: Using scholars who specialize in UK politics and prejudice (rather than generic crowdworkers) for sensitive, nuanced classification achieves very high inter-rater reliability (α=0.895) — a design choice for fine-grained values annotation tasks.

## 12. Notable quotes
- "Distinguishing between different types of Islamophobic speech offers considerable empirical and theoretical advantages over using a single category of 'Islamophobia'. It enables researchers to better understand the dynamics of Islamophobia (which may differ across different manifestations) and to investigate radicalization processes." (p.1)
- "The benefits of having tweets which are contextually-specific outweighs the cost of having a smaller dataset." (p.3)
- "Thus, it is crucial that the model is not only accurate but that its choice of inputs can be explained and thus avoids becoming a 'black box'." (p.3)
- "Contrary to our initial expectations, we opt to use SVM for the classifier." (p.4)

## 13. UNKNOWN / not in extract
- Whether the 140M-tweet corpus is publicly available.
- The specific annotation guidelines beyond the definitions of strong/weak Islamophobia.
- Verbatim example tweets from the dataset.
- Whether the full 4,000-tweet annotated dataset is released.
- How the 45 far-right accounts were selected and whether this list is publicly available.
- Whether the classifier was updated with larger training data in subsequent work.
