---
stem: "2024-Ranasinghe-SOLD Sinhala Offensive Language Dataset"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, best-practices, saturation-discrimination]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 10000
dataset_construction: "crowdsourced"
languages: ["si"]
models_tested: ["mBERT", "SinBERT", "XLM-RoBERTa", "XLM-T", "BiLSTM", "CNN", "SVC"]
headline_numbers:
  - "10,000 Sinhala tweets annotated at sentence- and token-level; 41% offensive (p.11)"
  - "Best sentence-level Macro F1: XLM-R 0.83 without transfer learning, 0.84 with Hindi transfer (p.22)"
  - "Best token-level Macro F1: XLM-R 0.73 with TSD transfer learning (p.24)"
  - "Sentence-level IAA: majority of pairwise Fleiss' Kappa scores 0.7–0.8 (p.10)"
  - "Token-level IAA: majority of pairwise Kappa scores 0.6–0.7 (p.10)"
  - "SemiSOLD semi-supervised dataset: >145,000 Sinhala tweets (p.3)"
---
## 1. Gist
SOLD (Sinhala Offensive Language Dataset) is a manually annotated benchmark of 10,000 Sinhala-script Twitter posts labeled for offensive language at both sentence level (binary: offensive / not-offensive) and token level (which specific tokens make a post offensive). It is the first large publicly available offensive-language dataset for Sinhala, a low-resource Indo-Aryan language spoken by 17 million people in Sri Lanka. The paper also introduces SemiSOLD, a semi-supervised extension of >145,000 tweets. Both datasets, combined with extensive experiments on transfer learning from high-resource languages and semi-supervised data augmentation, establish a comprehensive benchmark for Sinhala hate-speech / offensive-language identification. For values-alignment benchmarking the paper is particularly useful as a case study in (a) dual-level annotation (sentence + token) that enables explainability evaluation, (b) cross-lingual transfer for low-resource settings, and (c) rigorous inter-annotator agreement measurement in a culturally specific non-Western context.

## 2. Benchmark/eval design features
**Constructs measured:** Binary offensiveness of social media posts at sentence level, plus which tokens within an offensive post contribute to the offence (token-level).

**Label taxonomy (sentence-level):** OFF (offensive — profanity, targeted insults, threats) vs. NOT (not offensive), following OLID [104] Level A.

**Label taxonomy (token-level):** Each token within an offensive post is labeled offensive or not-offensive based on whether it contributes to the sentence-level judgement; non-verbal cues like emojis are included.

**Annotation design:** Ten native Sinhala-speaking annotators, aged 25–40, all with at least a bachelor's degree. Each tweet annotated by three annotators; gold labels by majority vote (>2/3 agreement). Maximum 10% of total annotations per annotator to reduce individual bias.

**Data collection:** Twitter API with predefined keywords targeting offensive context words and news accounts. Filtered to Sinhala script only. Usernames replaced with @USER and URLs with <URL> tokens.

**Splits:** 75% training / 25% test; similar class distribution in both splits.

**Evaluation metric:** Macro-averaged F1-score (chosen because of class imbalance).

## 3. Task format & example item
From Table 1 (p.11–12):

| Tweet | Class |
|-------|-------|
| "@USER @USER ඇය නලවෙන කොට බඩුව වේ go yo yo" [She is like a whore when she moves slowly yo yo] | OFF |
| "@USER අෙඩා කෑම බීම හරියට තිෙයනව ද?" [Do you have enough foods and drinks?] | NOT |

Offensive tokens are highlighted in red in the original annotation; annotators circled or tagged specific tokens justifying their sentence-level decision.

## 4. Scoring / grading methodology
- **Sentence-level:** Majority vote of 3 annotators → binary gold label. Models evaluated with Macro F1, plus per-class Precision/Recall/F1 and weighted average.
- **Token-level (supervised):** Direct token-classification training, evaluated with P/R/Macro-F1 on offensive tokens only.
- **Token-level (weakly supervised):** LIME applied at inference to a sentence-level classifier; probability threshold tuned on 1/5 of training data to binarize token importance scores.
- All experiments run with 5 different random seeds; mean reported.

## 5. Dataset construction & provenance
- **SOLD:** 10,000 tweets, 10,500 collected → 500 used for pilot and excluded from main set. Twitter API with Sinhala-script filter. Collected ~2022. Released on HuggingFace (sinhala-nlp/SOLD).
- **SemiSOLD:** 145,000+ additional Sinhala tweets labeled via ensemble of ML models trained on SOLD. Released on HuggingFace (sinhala-nlp/SemiSOLD).
- **Class balance:** 41% offensive in SOLD, comparable to training set distribution.
- **Licensing:** Open-access on HuggingFace; personally identifiable information removed.
- **Contamination controls:** Pilot set (500 tweets) excluded from main 10,000. No explicit deduplication of exact tweets mentioned, but Twitter language API filter ensures Sinhala-script content.

## 6. Validity evidence
- **Inter-annotator reliability:** Pairwise Fleiss' Kappa mostly 0.7–0.8 at sentence level (p.10), mostly 0.6–0.7 at token level (p.10) — token-level comparable to TSD (mean pairwise Kappa 0.55).
- **Human baselines:** Majority-class and minority-class baselines reported; all ML models exceed majority baseline.
- **Cross-lingual validity:** Transfer from Hindi, English, and code-mixed Sinhala all generally improves results, suggesting the label space is compatible across related annotation schemes.
- **Explainability validity (proxy):** LIME-based weakly supervised approach evaluated against gold token-level annotations, providing an implicit measure of whether sentence-level model attention aligns with human token-level rationales.

## 7. Saturation / discrimination
- Best Macro F1 at sentence level: 0.84 (XLM-R + Hindi transfer) — moderate room remains.
- Best Macro F1 at token level: 0.73 (XLM-R + TSD transfer) — meaningful gap from ceiling.
- mBERT (no Sinhala pre-training) achieves only 0.53 Macro F1 at sentence level (p.17) — confirms that language-specific pre-training matters and the task is non-trivial.
- Weakly supervised LIME achieves only 0.45 Macro F1 at token level, well below supervised upper bound (0.73), indicating discrimination headroom for better explainability methods.
- Class imbalance (41%/59%) is moderate; macro-F1 mitigates ceiling inflation.

## 8. Multiturn / agentic aspects
n/a — static dataset classification task; no interaction protocol.

## 9. Key numbers
- 10,000 annotated tweets in SOLD; 41% labeled offensive (p.11)
- 10 annotators, each covering max 10% of annotations (p.10)
- 3 annotators per tweet, majority voting for gold label (p.10)
- Sentence-level Kappa: mostly 0.7–0.8 (p.10)
- Token-level Kappa: mostly 0.6–0.7 (p.10)
- 75%/25% train/test split (p.11)
- Best sentence-level without TL: XLM-R Macro F1 = 0.83 (p.16)
- Best sentence-level with TL: XLM-R + Hindi Macro F1 = 0.84 (p.22)
- Best token-level without TL: XLM-R Macro F1 = 0.72 (p.19)
- Best token-level with TL: XLM-R + TSD Macro F1 = 0.73 (p.24)
- SemiSOLD: >145,000 tweets (p.3)
- CNN + fastText achieves Macro F1 = 0.82, competitive with language-specific SinBERT (p.17)
- mBERT (no Sinhala support): Macro F1 = 0.53 at sentence level (p.16)

## 10. Pitfalls & limitations
- **Keyword-based collection bias:** Tweets collected using pre-specified offensive keywords, so the dataset oversamples offensive content and may not reflect organic distribution of Sinhala social media. A rule-based system using these keywords performs poorly (30–50% offensive for most keywords), but selection bias still applies.
- **Binary label coarseness:** The sentence-level scheme is purely binary (OFF/NOT), missing nuanced categories (targeted vs. untargeted, severity levels, type of offence). Token-level annotations also binary.
- **Annotator demographics:** All 10 annotators are native speakers, but they are all aged 25–40 with at least a bachelor's degree — may not represent diverse Sinhala perspectives, especially rural, older, or less-educated speakers.
- **Script coverage:** Only Sinhala script; Roman-script Sinhala and code-mixed Sinhala are excluded. Code-mixed transfer learning showed no benefit (p.23).
- **Transfer learning limits:** No clear signal which source language/dataset benefits most; results vary by underlying model — practitioners must experiment for new languages.
- **Snapshot in time:** Twitter data from ~2022 Sri Lanka context; offensive language evolves with current events (government protests, Easter bombings referenced).
- **SemiSOLD quality:** Semi-supervised labels have noise; filtering threshold matters (0.15 threshold adds too many noisy instances, p.26).

## 11. Novel ideas worth stealing
1. **Dual-level annotation (sentence + token):** Simultaneously collecting sentence-level labels and token-level rationale annotations enables evaluation of both classification accuracy and model explainability with a single dataset — directly reusable for values-alignment tasks where identifying *which* content violates a value matters.
2. **LIME as weak explainability evaluator:** Using LIME on a sentence-level classifier and evaluating against gold token annotations provides a cheap proxy for explainability without requiring token-annotated training data — useful for auditing LLM refusals or value violations.
3. **Semi-supervised augmentation with ensemble uncertainty filtering:** Training on a small annotated set, generating pseudo-labels with multiple diverse models, filtering by standard deviation of model confidence, and iteratively adding confident predictions is a scalable low-resource strategy directly applicable to building value-annotation datasets.
4. **Cross-lingual transfer as coverage checker:** Testing whether transfer from related languages (Hindi for Sinhala) improves performance can serve as a validity check — if a new values dimension in a low-resource language benefits from transfer from a conceptually related high-resource annotation, the construct may be linguistically similar enough to share.
5. **Keyword-to-offensiveness ratio as item difficulty metric:** Reporting the percentage of offensive tweets per collection keyword (Table 2) reveals item difficulty heterogeneity — borrowable as a diagnostic for benchmark items that are too obviously problematic vs. genuinely ambiguous.

## 12. Notable quotes
- "SOLD is the first non-English offensive language detection dataset with explainable tokens." (p.3)
- "As can be seen, the majority of the agreements fall between 0.7-0.8, indicating high agreement at the sentence-level. For the token-level, following TSD dataset [62], we computed the pairwise Kappa by using character offsets. As can be seen, the majority of the agreements fall between 0.6-0.7." (p.10)
- "Transfer learning does not always improve the explainability. This finding will create a new direction in explainable ML research in offensive language identification." (p.25)
- "Having too many noisy instances with a larger uncertainty threshold can lead to reduced performance in ML models." (p.26)

## 13. UNKNOWN / not in extract
- Full list of exact keywords used for SemiSOLD collection (not stated to differ from SOLD keywords but not confirmed).
- Whether SemiSOLD token-level labels were generated.
- IRB/ethics approval status for the Twitter data collection.
- Specific annotation duration / payment for annotators.
- Whether inter-annotator disagreements were adjudicated beyond majority vote.
- Precise dates of Twitter data collection.
