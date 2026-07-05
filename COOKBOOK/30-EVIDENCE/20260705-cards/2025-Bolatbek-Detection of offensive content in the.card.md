---
stem: "2025-Bolatbek-Detection of offensive content in the"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: false
theme_tags: [best-practices, cultural-linguistic]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Initial literature search returned 203 articles; 40 met inclusion criteria (p.1)"
  - "Naïve Bayes with 10 tweets and 100 features achieves 90% accuracy on Arabic abusive account detection (p.3)"
  - "Random Forest achieved highest accuracy of 76.42% in ontological hate speech classification (p.4)"
  - "Meta-classifiers outperformed base classifiers; RBF kernel SVM yields best accuracy of 79.8% in profanity vs. hate speech discrimination (p.4)"
---
## 1. Gist
This 8-page review paper, published in FUOYE Journal of Engineering and Technology (Vol. 6, Issue 1, March 2021), surveys automated detection of offensive language in social media platforms. Despite the "2025" stem in the vault filename, the paper's journal date is March 2021 and its references extend only to 2020. The review covers five method categories: NLP/machine learning approaches (SVM, Naïve Bayes, Random Forest), deep learning (CNN, RNN, LSTM, BiLSTM), multi-label/sentiment-based classification, hybrid approaches, and multilingual detection. From 203 initially identified articles, 40 met inclusion criteria; studies are summarised in structured tables. The paper is relevant to values-alignment benchmarking primarily as background on the evolution of hate/offensive content detection methodology and its multilingual challenges up to 2021, before the LLM era.

**Note on date discrepancy:** The vault stem says "2025-Bolatbek" but the paper's publication date is March 2021 (FUOYEJET Vol. 6 Issue 1). The stem may reflect a vault acquisition date, not the paper's publication year.

## 2. Benchmark/eval design features
This is a structured literature review, not a benchmark paper. Core claims and arguments:

1. **Method evolution:** Three phases identified — (a) pre-deep-learning: SVM dominant, relies on handcrafted n-gram/sentiment features, poor contextual understanding; (b) deep learning: CNN/LSTM improve contextual capture; (c) hybrid and multilingual: combining lexicons with neural models improves cross-domain/cross-lingual robustness.

2. **Preprocessing consensus:** Cleaning pipeline (lowercase, punctuation removal, stemming, stop-word removal, deduplication) is standard; crowdsourced labelling noted as scalable but subjective.

3. **Persistent challenges identified:** Data sparsity, class imbalance, sarcasm/ambiguity, multilingual code-switching, text embedded in images (not addressed by any reviewed method).

4. **Proposed future direction:** Linear SVC extended to detect profane text in both raw text and text-embedded-in-images (using OCR + PCA for image classification). This is a proposal, not a completed study.

5. **Multilingual coverage:** Arabic, Thai, Danish, Turkish, Greek, Indonesian, Mexican Spanish, Hindi-English (Hinglish) — the review captures a breadth of non-English contexts rarely covered in 2021 NLP surveys.

## 3. Task format & example item
n/a — review paper. No original items. The surveyed tasks are binary or multi-class offensive language classification (input: social media post; output: hate/non-hate, or fine-grained categories: toxic, severe toxic, obscene, insult, threat, identity hate).

## 4. Scoring / grading methodology
n/a — review paper. The surveyed studies use accuracy, F1-score (macro/micro), AUC-ROC; SVM with non-linear programming features outperformed deep learning in one study (Table 1, p.3); attention-based models proved "better alternative than traditional methods" (Table 3, p.4).

## 5. Dataset construction & provenance
n/a — review paper. Surveyed datasets include: Twitter corpora (various languages), Stormfront forum (white supremacy), Scratch website children's comments, Arabic Facebook/Twitter (abusive accounts), Danish Reddit/Facebook, Indonesian Twitter, Mexican Spanish tweets. Selection criteria for the review: peer-reviewed articles from Google Scholar using search terms including "profane words," "natural language processing," "multilingual context," "hybrid methods," "deep learning approach" (p.1).

## 6. Validity evidence
Not applicable at the level of the review. The review notes inter-study comparability problems: different datasets, splits, and metrics make direct comparison of reported accuracies unreliable. No meta-analysis is conducted; the review is descriptive/tabular.

## 7. Saturation / discrimination
Not applicable. The review documents a performance ceiling for pre-transformer methods: best NLP/ML results ~90% accuracy on narrow datasets; deep learning ~77-79% macro-F1; hybrid approaches improve but remain below 85% on realistic cross-domain tasks. The paper predates transformer/LLM-era results.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 3.2 billion social media users worldwide (~42% of world population) cited (p.1)
- 203 initial articles found; 40 met inclusion criteria (p.1): 6 NLP, 6 deep learning, 5 hybrid, 13 multi-level/multilingual, 10 other
- Best NLP result: Naïve Bayes, 90% accuracy on Arabic abusive account detection (Table 1, p.3)
- Best deep learning (as reviewed): BiLSTM ranked 4th in an SemEval competition (Table 2, p.3)
- CNN+LSTM: best F1 for categorisation using CNN for identification, LSTM for type classification (Table 2, p.3)
- Deep word+character CNN: 77.93% macro-averaged F1 (Table 2, p.3)
- RBF kernel SVM best accuracy 79.8% for profanity vs. hate speech discrimination (Table 3, p.4)
- Random Forest: 76.42% accuracy for ontological harmful speech classification (Table 3, p.4)
- Multi-level classifier SVM precision 75.76% for insult detection (Table 4, p.5)
- FID/corpus distances not in this paper; those numbers are from the Bhattacharjee religious texts paper

## 10. Pitfalls & limitations
- Paper is from 2021 and predates BERT-fine-tuned and LLM-era results; findings are now substantially outdated
- The review is descriptive (tables of papers) with no quantitative meta-analysis; effect sizes and confidence intervals not reported
- Inclusion/exclusion criteria are high-level; reproducibility of the search strategy is limited
- Proposed SVC-for-image-text extension is not empirically validated in this paper
- No analysis of dataset bias, annotation quality, or inter-annotator agreement across surveyed studies
- Multilingual studies are included but language-specific challenges are not deeply analysed

## 11. Novel ideas worth stealing
1. **Taxonomy of offensive content detection methods:** The five-category taxonomy (NLP/ML, deep learning, sentiment/multi-label, hybrid, multilingual) provides a useful framework for organising benchmark evaluation categories — values benchmarks could use a similar taxonomy to classify their evaluation approaches.

2. **Image-embedded text as an overlooked evaluation domain:** The review identifies detection of profanity embedded in image files as an entirely unaddressed research gap (as of 2021). This remains relevant: multimodal values-alignment benchmarks should include text-in-image items.

3. **Cross-domain generalisation as the key challenge:** The review repeatedly notes that models trained on one dataset/platform fail to generalise to others. This "cross-domain generalisation" challenge is equally critical for values benchmarks: a model that appears aligned on benchmark items scraped from one platform may fail on items from another cultural context.

4. **Crowdsourcing limitations for subjective annotation:** The review notes crowdsourcing is scalable but that "subjectivity analysis can be best done by human beings" (p.6). This suggests that for values-alignment tasks involving fine-grained moral judgement, expert annotation (as in INDOHATEMIX) may be necessary despite higher cost.

## 12. Notable quotes
- "Research into detection of offensive content online is moving away from rule-based techniques towards deciphering context of analyzed messages." (p.1)
- "Legal scholars noted that offensive utterances harm people the same way that physical blows do." (p.1)
- "Previous researches on the detection of offensive contents have focused solely on the detection of profanity in texts directly uploaded by the users and have overlooked the detection of profanity in texts embedded in uploaded graphics and profane gestures in images. This is a significant gap which creates a vast field for research." (p.7)
- "Enhanced techniques such as incorporation of pattern-based features are needed to perform a deep analysis of meaning of sentences to enable the automatic detection of sarcasm and ambiguous words in statements." (p.7)

## 13. UNKNOWN / not in extract
- Who "Bolatbek" is — the stem name does not match any listed author (authors are Akinboro, Adebusoye, Onamade from Nigerian universities); the stem may be a vault cataloguing artefact
- Why the paper is catalogued as "2025" when it was published in March 2021
- Whether the proposed SVC-for-image-text profanity detection was subsequently implemented or published
- Full details of the inclusion/exclusion criteria beyond the short description in the abstract
- The specific Google Scholar search date range for the literature review
