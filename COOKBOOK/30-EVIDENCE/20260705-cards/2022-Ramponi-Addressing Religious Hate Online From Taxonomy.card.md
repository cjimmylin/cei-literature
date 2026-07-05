---
stem: "2022-Ramponi-Addressing Religious Hate Online From Taxonomy"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [religious-values, cultural-linguistic, normative-ethics, validity-psychometrics]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 10028
dataset_construction: "crowdsourced"
languages: ["en", "it"]
models_tested: ["BERT", "RoBERTa", "AlBERTo", "UmBERTo", "multilingual BERT", "XLM-RoBERTa"]
headline_numbers:
  - "Dataset contains 10,028 annotated tweets (3,000 Italian, 7,028 English) (p.15)"
  - "Best monolingual religious hate detection: UmBERTo 65.69 F1 (Italian), RoBERTa 64.94 F1 (English) (p.20)"
  - "Italian abusive language proportion: 31.8%; English: 14.3% (p.16)"
  - "Italian inter-annotator agreement: κ=0.6530 for abusiveness; English Krippendorff α=0.8386 for religion-related abusiveness (p.13)"
  - "Zero-shot XLM-RoBERTa EN→IT religious hate: 60.27 F1 (p.3)"
---
## 1. Gist
This paper addresses the underexplored problem of religious hate speech in online social media by (1) creating a five-level taxonomy for annotating religious hate targeting Judaism, Christianity, and Islam; (2) building and releasing a bilingual Twitter dataset (English and Italian) of 10,028 annotated tweets; and (3) benchmarking multiple NLP classifiers on abusive language and religious hate speech detection tasks. The work is significant for values-alignment benchmarking because it demonstrates that inter-religious hate requires fine-grained, target-specific annotation schemes, documents the difficulty of automated detection (best F1 ~65), and shows that cross-lingual transfer via multilingual models is partially viable for religious hate—providing a foundation for multilingual evaluation of religious content moderation systems.

## 2. Benchmark/eval design features
The taxonomy has five hierarchical levels: (L1) abusive vs. not abusive; (L2) target type (group, individual, others, untargeted); (L3) hate speech category (misogyny, racism, religious hate, others); (L4) religious target (anti-christianity, anti-islam, anti-judaism); (L5) hate form (animosity, derogation-and-dehumanization, threatening language, abusive humor). The annotation scheme was specifically designed to be interoperable with existing taxonomies (Zeinert et al. 2021 for misogyny; Vidgen et al. 2021 for general abuse), enabling cross-dataset reuse. Classification tasks are framed as binary: abusive vs. not, and religious hate vs. not, using macro-averaged F1 with 5-fold cross-validation.

## 3. Task format & example item
The classification tasks are binary. Example annotated tweet (English, anti-islam):
"world wake up before you accept muslims in your countries, those people they're not refugees, they're all terrorist who want to come to your state and make a plan how to attack, make sure to deport them all back." (p.8)

Example annotated tweet (Italian, anti-judaism, abusive humor):
"la differenza tra un ebreo e una torta? il tempo di cottura" — translation: "the difference between a Jew and a cake? cooking time" (p.11)

## 4. Scoring / grading methodology
All classification experiments use macro-averaged precision, recall, and F1 (to give equal weight to minority classes) plus accuracy. Evaluation is 5-fold stratified cross-validation. Inter-annotator agreement: Cohen's kappa for the Italian expert subset (κ=0.6530 abusiveness, κ=0.5651 religion-related pre-adjudication); Krippendorff's alpha for the English crowd-sourced subset (α=0.2667 abusiveness, α=0.8386 religion-related).

## 5. Dataset construction & provenance
Tweets collected September 2021 from Twitter API using neutral religious keyword queries (December 2020–August 2021 time range) to avoid bias toward explicit hate. Italian: 3,000 tweets annotated by 3 expert native speakers with adjudication; multi-label allowed. English: 8,000 tweets (final 7,028 accepted) via Amazon Mechanical Turk, 5 annotators per tweet, EasyTurk quality control with gold standard checks. Dataset released publicly at https://github.com/dhfbk/religious-hate-speech. Tweets are anonymized (user mentions → [USER], URLs → [URL]).

## 6. Validity evidence
Inter-annotator reliability reported for both subsets (see section 4). Moderate kappa (κ≈0.65) for Italian expert annotation is described as consistent with other abusive language datasets. The high Krippendorff alpha (α=0.84) for English religion-related abusiveness is attributed to the multi-stage annotation workflow. Lexical artifacts (top 15 informative tokens per class) are documented, revealing that search terms without offensive words still produce datasets with meaningful content signals. Multiple classifier benchmarks (from naive baselines to transformer LMs) provide convergent evidence that the task is genuinely difficult (F1 plateauing ~65-76 depending on task and language).

## 7. Saturation / discrimination
Religious hate detection F1 of ~65 indicates substantial headroom and that the task is hard even for fine-tuned LMs. The class imbalance (Italian: 18.57% religious hate; English: 8.26%) creates ceiling effects on accuracy while F1 remains the more discriminating metric. Distribution across hate forms shows animosity is most frequent (implicit hate), while threats are least frequent, suggesting current datasets skew toward the easier explicit forms for future benchmarks to address.

## 8. Multiturn / agentic aspects
n/a — all classification is at the individual tweet level with no multiturn or agentic components.

## 9. Key numbers
- Total dataset: 10,028 tweets (3,000 Italian, 7,028 English) (p.15)
- Italian abusive: 31.8%; English abusive: 14.3% (p.16)
- Italian religious hate: 557 instances (18.57%); English: 663 (8.26%) (p.18)
- Best Italian abusive language detection: UmBERTo 76.31 F1 (p.21)
- Best English abusive language detection: RoBERTa 72.56 F1 (p.22)
- Best Italian religious hate detection: UmBERTo 65.69 F1 (p.21)
- Best English religious hate detection: RoBERTa 64.94 F1 (p.22)
- Italian IAA (abusiveness, pre-adjudication): κ=0.6530 (p.13)
- English IAA (religion-related abusiveness): α=0.8386 (p.13-14)
- Zero-shot XLM-RoBERTa EN→IT religious hate: 60.27 F1 (p.3)
- Italian: 60% anti-islam, 24% anti-judaism, 16% anti-christianity (p.16)
- English: 40% anti-islam, 33% anti-christianity, 27% anti-judaism (p.16)

## 10. Pitfalls & limitations
- Different annotation methodologies for Italian (expert, multi-label allowed) and English (crowd, single-label) complicate cross-lingual comparisons.
- Moderate Italian IAA (κ≈0.65) reflects genuine annotation difficulty; English IAA for general abusiveness (α=0.27) is low.
- Dataset is Twitter-specific and time-bounded (December 2020–August 2021), limiting generalizability.
- Only three monotheistic religions covered; other religions (e.g., Hinduism, Buddhism) are absent.
- No demographic data on English crowd-workers (prohibited by GDPR).
- Lower English performance despite larger dataset may reflect platform-specific linguistic diversity, annotation methodology differences, or more challenging class distribution.

## 11. Novel ideas worth stealing
- **Five-level hierarchical taxonomy aligned across multiple existing annotation schemes**: building upward compatibility with prior corpora increases data reusability. A values-alignment benchmark could adopt similar interoperability by mapping onto an established taxonomy (e.g., Vidgen et al. 2021).
- **Hate speech form labels (animosity, derogation, threatening, abusive humor)**: separating implicit animosity from explicit derogation/dehumanization is a reusable design pattern for evaluating whether models handle subtle versus overt normative violations differently.
- **Lexical artifact documentation**: explicitly releasing the top 15 most informative tokens per class flags known annotation artifacts before model training—valuable transparency mechanism.
- **Counter-claim of interoperability**: annotating for out-of-scope categories (misogyny, racism) even when the study targets religion allows the dataset to be repurposed for other hate targets without re-annotation. Design principle: annotate broad, study narrow.
- **Cross-lingual zero-shot as baseline**: treating zero-shot cross-lingual transfer as a standard experimental condition (rather than an afterthought) provides a realistic deployment-relevant baseline for multilingual values benchmarks.
- **Neutral keyword collection strategy**: avoiding offensive search terms to prevent dataset skew toward explicit hate is a reusable data-collection principle for any sensitive-topic benchmark.

## 12. Notable quotes
- "Religious hate is very much dependent on country-specific factors, including the presence and visibility of religious minorities, societal issues, historical background, and current political decisions." (p.1)
- "We argue that providing annotations even for classes which are not of direct interest in this study (e.g., misogyny, racism) allows data to be easily repurposed in future studies concerning other targets." (p.5)
- "Abusive humor: an understudied case of implicit hate which uses jokes and black humor, indirectly leading to the stereotyping of target religious groups, and potentially perpetuating prejudices and causing harm to such groups." (p.11)
- "Recent works advocate for reporting annotators' information when releasing datasets with toxicity annotation to account for biases and disagreement cases (Sap et al., 2022), but the processing of personal data concerning religious beliefs is explicitly prohibited by the EU General Data Protection Regulation." (p.14)

## 13. UNKNOWN / not in extract
- Exact training/test splits for the monolingual experiments (only cross-validation splits are reported).
- Whether the dataset has since been expanded or updated post-2022.
- Full annotation guidelines (referenced as publicly available but not reproduced in the extract).
- Results for fine-grained multi-class classification (levels 4 and 5) beyond binary religious hate/not-religious hate.
