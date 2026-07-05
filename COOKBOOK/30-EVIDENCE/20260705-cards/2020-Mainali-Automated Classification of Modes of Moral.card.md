---
stem: "2020-Mainali-Automated Classification of Modes of Moral"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, design-space]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: 25
dataset_construction: "scraped"
languages: ["en"]
models_tested: []
headline_numbers:
  - "SVM classifier achieves over 90% accuracy on held-out philosophy articles (p.2)"
  - "Consequentialist reasoning in US circuit courts increased sharply in the 1930s (p.7)"
  - "Most consequentialist judge: Neil Gorsuch at 92.4%; most deontological: Jacob Trieber at 21.2% (p.8)"
  - "Training corpus: 14 consequentialist + 11 deontology philosophy papers (p.3)"
---

## 1. Gist

This paper presents an automated NLP classifier that distinguishes consequentialist from deontological moral reasoning in written text. The authors train a Linear SVM on a small corpus of applied ethics philosophy articles from PhilPapers (25 papers total, split into 200 chunks) and then apply it to over a century of U.S. circuit court opinions (1883–2013). The result is a quantitative mapping of how judicial moral reasoning has shifted over time, by judge, by legal topic, and by law school attended. For values-alignment benchmarking, this work is notable as an early demonstration that moral reasoning modes are machine-detectable from text surface features, and provides a validated methodology for operationalizing normative-ethics categories at scale.

## 2. Benchmark/eval design features

This is not a benchmark paper; it is a classifier construction and application study. Core claims:
- Consequentialism and deontology are distinguishable via tf-idf n-gram features in text paragraphs.
- A very small training corpus (25 philosophy papers) is sufficient to achieve high accuracy on held-out philosophy texts.
- The same classifier can be meaningfully applied cross-domain (legal opinions vs. philosophy articles), producing interpretable and historically coherent trends.
- Moral reasoning style in the judiciary correlates with time period, law school attended, and birth region — but not with political party or gender.

The classifier is binary (consequentialist vs. deontological); virtue ethics and other frameworks are not covered. The unit of analysis is a paragraph.

## 3. Task format & example item

n/a — this is a classifier application study, not a benchmark with presented items. The paper shows example paragraphs labeled by the model:

Deontological: "By reason of its nature as a public institution St. Elizabeths Hospital owes a duty to the public in carrying out its difficult responsibilities..." (p.5)

Consequentialist: "No rule of bankruptcy practice and procedure is designed to be considered in isolation. Each rule is to be considered in conjunction with every other rule..." (p.5–6)

## 4. Scoring / grading methodology

Linear SVM with tf-idf trigram features. Paragraphs are assigned a binary label (consequentialist/deontological) based on which side of the hyperplane their feature vector falls. The model's prediction function assigns signed weights to n-grams; sign indicates consequentialist (negative) or deontological (positive) loading. Accuracy reported on held-out philosophy article chunks. No inter-rater reliability or human baseline reported for the judicial corpus application.

## 5. Dataset construction & provenance

Training data: 25 applied ethics articles from PhilPapers.org tagged "Applied Consequentialism" (14 papers) or "Applied Deontology" (11 papers), filtered to English-only with both-tag papers excluded (p.3). Each corpus split into 100 equal-size chunks for training (200 chunks total). Application corpus: all U.S. circuit court opinions 1883–2013 (size not precisely stated, but includes thousands of opinions from judges with ≥50 opinions each). No license or availability information stated.

## 6. Validity evidence

The authors report >90% accuracy on held-out philosophy articles (p.2). Informal qualitative validation: example paragraphs labeled by the model are presented and assessed as intuitively correct (p.7–8). Top predictive n-grams are visualized and assessed for face validity (e.g., "pleasure" → consequentialist, "duty" → deontological) (p.4). No formal inter-rater reliability, no human baseline on legal opinions, no held-out test set from the judicial corpus.

## 7. Saturation / discrimination

On the training domain (philosophy articles), the model quickly reached near-100% validation accuracy, requiring manual pruning of overfitted features (e.g., institution names appearing in PDF headers) (p.4). The model is a binary classifier with no difficulty gradation. Judicial corpus results show wide variation across judges (21%–92% consequentialist), suggesting reasonable discrimination in the application domain.

## 8. Multiturn / agentic aspects

n/a

## 9. Key numbers

- Training corpus: 14 consequentialist + 11 deontology papers = 25 total, split into 200 chunks (p.3)
- Classifier accuracy on held-out philosophy text: >90% (p.2)
- Most deontological judge: Jacob Trieber, 21.2% consequentialist (p.8)
- Most consequentialist judge: Neil Gorsuch, 92.4% consequentialist (p.8)
- Discrete jump in consequentialism in the 1930s (p.7)
- Most deontological legal topic: Wills/Trusts/Estates at 44.7% consequentialist (p.13)
- Most consequentialist legal topic: Technology Law at 93.9% consequentialist (p.15)
- Law school range: Washington and Lee (−19.6% vs. average) to Georgetown (+17.2%) (p.11)
- Coastal states show relatively deontological leaning in birth-state analysis (p.9)

## 10. Pitfalls & limitations

- Extremely small training corpus (25 papers, 200 chunks); high overfitting risk despite tuning (p.3–4)
- Binary framework excludes virtue ethics, care ethics, and other moral frameworks (p.12)
- Cross-domain transfer (philosophy → legal writing) is assumed valid but not rigorously validated
- Junk features required manual removal (institutional names from PDF headers, irrelevant high-frequency terms) (p.4)
- No human baseline on judicial corpus; no inter-rater reliability for the main application
- The label "consequentialist" in legal writing may not map cleanly onto philosophical consequentialism
- Judge-level analyses filtered to those with ≥50 opinions, creating survivorship bias toward prolific judges (p.8)
- Time-series trends are confounded with topic popularity (acknowledged by authors) (p.8)

## 11. Novel ideas worth stealing

- **Small-corpus bootstrapping**: 25 philosophy articles suffice to train a paragraph-level moral reasoning classifier that transfers to a different domain. Benchmark builders needing moral-framework labels on unlabeled corpora could use this approach with minimal annotation.
- **Chunk-based training from long documents**: splitting long texts into equal-size chunks as training units allows fine-grained paragraph scoring while preserving domain signal.
- **Feature inspection as validity check**: visualizing top SVM n-gram weights as word clouds provides an interpretable sanity check on what the model learned, and identifies junk features before deployment.
- **Aggregate scoring to reveal trends**: applying item-level binary labels to aggregate over judges/topics/time creates a richer secondary analysis from a single classifier — useful for "moral style profiling" of text corpora at scale.
- **Cross-domain calibration probe**: presenting sample predictions from the new domain (legal opinions) and checking qualitative plausibility is a cheap validity check worth including in any benchmark paper.

## 12. Notable quotes

- "What is the role of moral reasoning in judge decision-making? To get at this question empirically one must first try to identify and measure the use of different modes of moral reasoning in judicial decisions." (p.2)
- "Our model very quickly approached a 100% prediction accuracy in the validation set, so the main hyperparameter tuning step was finding junk features in the prediction function and removing them." (p.4)
- "We see there is a discrete jump in consequentialism in the 1930s, indicating a major switch in thought at the time." (p.7)
- "Future work should expand the training data to get a more comprehensive view of moral reasoning language. We could also look at other moral frameworks, such as virtue ethics." (p.12)

## 13. UNKNOWN / not in extract

- Total size of the judicial corpus (number of opinions or judges)
- Exact held-out test accuracy figure (stated as ">90%" without decimal precision)
- Whether the trained model or data are publicly available
- Any formal inter-rater reliability measure for the judicial corpus application
- Publication venue and final publication year (the HAL preprint says 2023 but the SSRN number is listed as 2018; the "stem" year of 2020 is ambiguous)
