---
stem: "2022-Vargas-HateBR A Large Expert Annotated Corpus of Brazilian Instagram"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, design-space, normative-ethics]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 7000
dataset_construction: "scraped"
languages: ["pt"]
models_tested: ["Naive Bayes", "SVM", "MLP", "Logistic Regression"]
headline_numbers:
  - "7,000 Instagram comments from Brazilian politicians' accounts (p.1)"
  - "Cohen's kappa for offensive language classification: 0.75 avg (p.6)"
  - "Cohen's kappa for offensiveness-level classification: 0.47 avg (p.6)"
  - "Best F1-score for offensive language detection: 85% (p.7)"
  - "Best F1-score for hate speech detection: 78% (p.7)"
---
## 1. Gist
HateBR is the first large-scale expert-annotated corpus of Brazilian Portuguese Instagram comments targeting the detection of offensive language and hate speech. Collected from six Brazilian politicians' public Instagram accounts during the second half of 2019, the corpus contains 7,000 comments annotated across three hierarchical layers: binary (offensive vs. non-offensive), offensiveness level (slightly/moderately/highly), and nine hate speech groups (xenophobia, racism, homophobia, sexism, religious intolerance, partyism, apology for dictatorship, antisemitism, fatphobia). Annotations were produced exclusively by domain specialists with diverse profiles, achieving high inter-annotator agreement (kappa ~0.75) for binary classification. The corpus fills a critical gap for low-resource hate speech research in Portuguese and provides a balanced, hierarchically-labeled resource outperforming prior Portuguese-language baselines.

## 2. Benchmark/eval design features
The corpus measures three levels of abusive language: (1) binary offensive classification (3,500 offensive, 3,500 non-offensive — perfectly balanced), (2) three-level offensiveness gradation (highly: 778, moderately: 1,044, slightly: 1,678), and (3) nine fine-grained hate speech groups applied to 727 hate speech comments. The annotation scheme distinguishes offensive language (any pejorative connotation) from hate speech (targeted against groups by characteristics), and distinguishes explicit vs. implicit expressions. Three PhD-level specialist annotators performed independent labeling; ties were resolved by the linguist/hate speech expert serving as judge. Baseline experiments use classical ML models (NB, SVM, MLP, LR) with n-gram and tf-idf features.

## 3. Task format & example item
Binary classification: given an Instagram comment, predict offensive vs. non-offensive; graded classification: predict offensiveness level; hate classification: predict which of nine hate groups applies.

Example from Table 4 (p.4):
- Offensive Language: "Essa besta humana é o câncer do País, tem q voltar para jaula, urgentemente! E viva o Presidente Bolsonaro." (Translation: "This human beast is the cancer of the country, it has to go back to the cage, urgently! And long live President Bolsonaro.")
- Non-Offensive: "Quem falou isso pra vc deputada? O sergio moro ta aprovado pela maioria dos brasileiros." (Translation: "Who said that to you deputy? Sergio Moro is approved by the majority of Brazilians.")

## 4. Scoring / grading methodology
Cohen's kappa and Fleiss' kappa for inter-annotator agreement. For binary offensive classification, Cohen's kappa = 0.75 avg across annotator pairs (AB: 0.76, BC: 0.72, CA: 0.76); Fleiss' kappa = 0.74. For offensiveness-level classification, Cohen's kappa = 0.47 avg; Fleiss' kappa = 0.46. Machine learning classifiers evaluated using precision, recall, and F1-score with 80/10/10 train/test/validation splits. Class balancing via undersampling for the imbalanced hate speech detection subtask.

## 5. Dataset construction & provenance
Data collected via Instagram API from 30 posts across six Brazilian politicians' accounts (three liberal, three conservative; four women, two men) published August–December 2019. Initially 15,000 comments extracted; 8,000 removed (noise: emoticons-only, laughs, mention-only; plus surplus non-offensive entries to achieve balance). Final corpus: 7,000 comments, balanced 50/50 offensive/non-offensive. The annotation process took approximately six months (August 2020 to January 2021). Annotators selected by PhD or PhD-candidate status, diverse political orientations (liberal and conservative), racial backgrounds (black and white), and regions (North and Southeast Brazil). Dataset publicly available at time of publication.

## 6. Validity evidence
High inter-annotator agreement for offensive language classification (kappa ~0.75, rated "substantial" by Cohen's scale). Moderate agreement for offensiveness-level (kappa ~0.47), expected given the task's high subjectivity. The expert annotation schema was pre-tested and refined with guidelines specifically addressing pejorative connotation distinctions (explicit vs. implicit, offensive vs. hate speech vs. non-offensive). Baseline F1-scores (85% offensive, 78% hate) exceed prior Portuguese-language state-of-the-art, supporting content validity. Annotator diversity (political orientation, race, region) was explicitly designed to minimize bias.

## 7. Saturation / discrimination
The best baseline achieves 85% F1 for offensive detection with simple n-gram features, indicating moderate headroom for transformer-based methods. Hate speech detection at 78% F1 shows more room for improvement. Offensiveness-level classification shows only moderate human agreement (0.47 kappa), suggesting fine-grained ordinal calibration remains hard even for humans. The imbalanced distribution of hate speech groups (partyism: 496, xenophobia: 1, antisemitism: 2) limits statistical reliability for rare categories.

## 8. Multiturn / agentic aspects
n/a — static comment-level classification benchmark with no interaction protocol.

## 9. Key numbers
- 7,000 total comments: 3,500 offensive, 3,500 non-offensive (p.7)
- Offensiveness breakdown: 1,678 slightly, 1,044 moderately, 778 highly offensive (p.7)
- 727 hate speech comments across nine groups (p.7)
- Partyism: 496; Sexism: 97; Religion intolerance: 47; Apology for dictatorship: 32; Fatphobia: 27; Homophobia: 17; Racism: 8; Antisemitism: 2; Xenophobia: 1 (p.7)
- Cohen's kappa offensive: 0.75 avg (p.6)
- Cohen's kappa offensiveness-level: 0.47 avg (p.6)
- Best F1 offensive language (SVM tf-idf): 0.85 (p.7–8)
- Best F1 hate speech detection (MLP/LR unigram): 0.78 (p.8)
- Outperforms Fortuna et al. (2019) LSTM F1 0.78 and de Pelle & Moreira (2017) SVM/NB F1 0.80 (p.8)

## 10. Pitfalls & limitations
- 70% of posts are from political-government subjects, limiting topical diversity and potentially skewing hate categories toward partyism (496 instances vs. xenophobia with 1).
- Annotations cover only one social media platform (Instagram) during one election-adjacent period (second half 2019), reducing temporal and platform generalizability.
- All in Brazilian Portuguese; not applicable to European Portuguese without adaptation.
- Only 727 hate speech examples among 7,000 comments (10.4%), with very sparse rare categories (xenophobia: 1), insufficient for training robust subcategory classifiers.
- Annotators are exclusively women with PhD-level education from two Brazilian regions — though diverse by design, this is still a narrow sample.
- Simple baseline classifiers (NB, SVM, MLP, LR) — no transformer results reported at time of submission.

## 11. Novel ideas worth stealing
- **Three-layer annotation hierarchy**: designing a corpus with coarse binary → ordinal severity → fine-grained category layers allows evaluation at multiple granularities, useful for values-alignment benchmarks that need to distinguish mere norm violation from targeted hate.
- **Expert-only annotators with profile diversity**: requiring PhD-level expertise in linguistics/hate speech/NLP plus diversity across political affiliation, race, and region as annotation eligibility criteria demonstrates that demographic diversity in annotators is operationalizable.
- **Balanced class design**: explicitly enforcing 50/50 offensive/non-offensive balance at collection time (removing surplus labeled comments) avoids class imbalance artifacts in binary classification performance metrics.
- **Implicit/explicit distinction**: separately coding implicit (context-dependent) vs. explicit pejorative content is a design move that benchmarks testing nuanced value violations should adopt.
- **"Fatphobia" as a hate category**: including physical-appearance-based discrimination as a named hate group alongside racism, sexism, etc. reflects a broader conception of protected characteristics.

## 12. Notable quotes
- "A well-deﬁned annotation schema has a considerable impact among the consistency and quality of the data, and the performance of the derived machine learning classiﬁers." (p.1)
- "Due to the degree of complexity of the offensive language and hate speech detection tasks, mainly because it involves a highly politicized domain, we decided to select only specialists at higher levels of education." (p.3)
- "We assume that hate speech is a kind of language that attacks or diminishes, that incites violence or hate against groups, based on speciﬁc characteristics such as physical appearance, religion, or others, and it may occur with different linguistic styles, even in subtle forms or when humor is used." (p.4)

## 13. UNKNOWN / not in extract
- Transformer-based model baselines (BERT, BERTimbau) — not reported in this version
- Whether the dataset is available under a specific open license
- Exact post-publication download/citation statistics
- Inter-annotator agreement broken down by hate speech category (reported only for binary and ordinal levels)
- Results for offensiveness-level classification as a standalone machine learning task
