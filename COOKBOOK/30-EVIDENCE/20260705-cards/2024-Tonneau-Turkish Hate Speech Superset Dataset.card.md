---
stem: "2024-Tonneau-Turkish Hate Speech Superset Dataset"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, best-practices, design-space]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 2311
dataset_construction: "crowdsourced"
languages: ["Turkish"]
models_tested: ["BERTurk"]
headline_numbers:
  - "Binary classification accuracy 77.06% on Istanbul Convention dataset with BERTurk (p.6)"
  - "Binary classification accuracy 71.06% on Refugees dataset (p.6)"
  - "Multi-class accuracy 72.22% on Istanbul Convention and 71.74% on Refugees (p.7)"
  - "Krippendorff alpha 0.84 (binary) and 0.82 (multi-class) for Istanbul Convention dataset (p.4)"
  - "Istanbul Convention: 499 'No Hate' and 534 total hate tweets; Refugees: 774 'No Hate' and 504 hate tweets (p.5)"
---
## 1. Gist
This LREC 2022 paper (Beyhan et al.) presents a Turkish hate speech dataset and detection system, collected from two domain-specific contexts: Turkish Twitter discourse following Turkey's withdrawal from the Istanbul Convention (gender-based hate) and tweets about refugees in Turkey (xenophobic/ethnic hate). The dataset uses a 5-level hate speech annotation scheme (No Hate, Insult, Exclusion, Wishing Harm, Threatening Harm) plus separate annotations for offensive language, target group, and tweet stance. The paper also reports BERTurk-based classification results as baselines. The paper is notable for its iterative, domain-grounded annotation design and serves as a component of the Turkish superset dataset referenced in related work by Tonneau et al. (2024) for cross-lingual hate speech research.

## 2. Benchmark/eval design features
Two datasets from distinct domains: (1) Istanbul Convention dataset — 1,033 tweets (after removing conflicting annotations from 1,206) collected during the five days after Turkey's withdrawal from the Istanbul Convention (March 20–25, 2021); (2) Refugees dataset — 1,278 tweets collected between January 2020 and September 2021, filtered for refugee-related keywords. Each tweet annotated along four dimensions: (1) offensive language level (None/Weak/Strong); (2) stance (Pro/Against/Neutral); (3) target group (Race/Ethnicity, Country/Nationality, Religion, Gender, Sexual Orientation, Opinion Groups); (4) hate speech category on 5-point scale. The 5-level taxonomy: No Hate Speech, Insult, Exclusion, Wishing Harm, Threatening Harm — with examples provided to annotators in LabelStudio.

## 3. Task format & example item
Hate speech level classification (5-class or binary). Example items from Table 1 (p.3):

- No Hate Speech: "Do not give priority to these people for vaccines."
- Insult: "Do you see how these animals are jumping over the border?"
- Exclusion: "I do not want my kids to be in the same classroom as Syrian kids."
- Wishing Harm: "I hope these refugees drown with those boats and cannot come back!"
- Threatening Harm: "I am so full that I will kill the first Syrian that comes my way!"

Error analysis examples also provided (p.7-8), including a tweet using "people of Lut" as anti-LGBTQ+ reference requiring cultural background knowledge to classify.

## 4. Scoring / grading methodology
Multiple annotators per tweet; Krippendorff's α measured for inter-annotator agreement. Istanbul Convention: 1,206 total tweets, 173 with conflicting annotations removed, leaving 1,033 non-conflicting. Krippendorff's α = 0.84 (binary) and 0.82 (multi-class) (p.4). Refugees dataset annotated by two groups: 398 tweets by Hrant Dink Foundation experts, 953 by student annotators. Classification and regression experiments use 5-fold cross-validation (70/10/20 train/val/test) with 3 different random seeds (15 runs total). Micro-averaged F1 reported for multi-class; binary accuracy and F1 reported for binary.

## 5. Dataset construction & provenance
Istanbul Convention tweets: collected during 5 days using trending topics; 284,989 original tweets filtered to ~10,000 by removing off-topic hashtags, then further filtered with topical keywords; 1,206 annotated. Refugees tweets: Twitter Academic API, Jan 2020–Sep 2021, refugee-related keyword filter, removed news accounts, near-duplicates, short tweets (<100 chars), and tweets with >3 hashtags; 1,278 annotated. Annotators: senior undergraduate Cultural Studies students for Istanbul Convention; cultural studies students plus Hrant Dink Foundation (HDV) for Refugees. Dataset publicly available at https://github.com/verimsu/Turkish-HS-Dataset.

## 6. Validity evidence
High Krippendorff's α for Istanbul Convention (0.84 binary, 0.82 multi-class) indicates reliable annotation. The annotation process was iterative — started with 10-point scale, switched to 5-level after annotators reported difficulty, and initial annotations were discarded. The paper notes individual annotator variation (minimum/maximum average hate level: 0.66/0.88 for Istanbul Convention, 0.42/0.90 for Refugees) indicating residual subjectivity (p.5). Cross-domain generalization is limited: same model architecture shows performance gap between datasets (77% vs 71% binary accuracy), likely due to different annotation teams, different keyword filtering, and domain differences.

## 7. Saturation / discrimination
With ~52% hate-labeled tweets in Istanbul Convention and ~40% in Refugees, class balance is near 50-50 — unusual compared to real-world distributions. This is an artifact of keyword-based and topically-focused collection. The model has difficulty at category boundaries (Insult vs. Exclusion) and with very rare extreme categories (Wishing Harm, Threatening Harm) — the confusion matrix shows no samples from categories 3–4 correctly classified (p.7). BERTurk's R² for regression is low (0.24, 0.23), indicating limited ability to predict hate severity on a continuous scale.

## 8. Multiturn / agentic aspects
n/a. Single-tweet classification only. The paper does note that tweets requiring background/context knowledge (religious references, political shorthand) pose classification challenges (p.7), which implies a potential role for contextual/multiturn approaches.

## 9. Key numbers
- Istanbul Convention dataset: 1,206 total, 1,033 non-conflicting tweets (p.5)
- Refugees dataset: 1,278 tweets (p.5)
- Istanbul Convention hate distribution: 499 No Hate, 380 Insult, 118 Exclusion, 35 Wishing Harm, 1 Threatening Harm (p.5)
- Refugees hate distribution: 774 No Hate, 181 Insult, 277 Exclusion, 39 Wishing Harm, 7 Threatening Harm (p.5)
- Krippendorff's α: 0.84 binary, 0.82 multi-class for Istanbul Convention (p.4)
- BERTurk binary 5-fold CV: 77.06% (±1.92) Istanbul Convention; 71.06% (±4.43) Refugees (p.6)
- BERTurk multi-class 5-fold CV: 72.22% (±2.94) Istanbul Convention; 71.74% (±2.17) Refugees (p.6)
- Regression RMSE: 0.66 Istanbul Convention; 0.83 Refugees (p.7)
- ~15% and ~24% improvements over majority-class baseline for binary and multi-class tasks (p.7)

## 10. Pitfalls & limitations
- Dataset sizes are small (~1,000–1,300 per domain); limited statistical power.
- Keyword and topic-based filtering creates selection bias — hate prevalence is inflated versus real-world Twitter.
- The Istanbul Convention dataset is highly imbalanced within hate categories (1 Threatening Harm example), making fine-grained classification infeasible.
- Annotation quality may differ between Hrant Dink Foundation experts and student annotators in Refugees dataset.
- BERTurk was pretrained on formal text (Wikipedia, news) but the task involves informal tweets — known limitation acknowledged (p.7).
- Detection requires background knowledge (cultural, religious, political) that NLP models lack.
- Authors acknowledge that offensive language was given to annotators without a clear definition (p.4), introducing inconsistency in that dimension.

## 11. Novel ideas worth stealing
1. **Multi-dimensional annotation per item**: Annotating for hate level, offensive language, stance, and target group simultaneously — this multi-label scheme enables analysis of relationships between dimensions (e.g., stance-based hate) and makes the dataset more reusable for multiple tasks.
2. **5-level severity taxonomy with anchor examples**: The iterative process of starting with a 10-point scale, failing, then landing on 5 labeled categories with concrete examples is a useful lesson in annotation scheme design — coarser is better when the fine-grained distinctions are not reliably perceivable.
3. **Domain-contrastive dataset design**: Collecting two datasets from thematically different but equally visible public controversies (gender rights and refugee policy) allows comparison of how domain affects both annotation quality and model performance — useful for any multi-topic values benchmark.
4. **Inclusion of expert annotators for subdomains**: Partnering with domain experts (Hrant Dink Foundation monitors hate speech professionally) alongside academic annotators, and comparing their annotation behavior, is a model for quality control in specialized hate speech tasks.
5. **Regression alongside classification**: Training a regression model on an ordinal hate scale captures gradations that multi-class models discretize. Low R² values here reveal that the scale may not be truly ordinal — a signal useful for future benchmark designers considering severity scales.

## 12. Notable quotes
- "Hate speech comes in a spectrum, ranging from mild stereotyping to open calls to violence toward the target group, partially explaining the difficulty in coming up with a description and annotating collected samples." (p.1)
- "we have found that some annotators are more inclined to call a tweet as hate speech compared to others. Among the annotators who labelled the same dataset, the minimum and maximum average hate speech level is 0.66 & 0.88 and 0.42 & 0.90 for the Istanbul Convention Dataset and Refugees Dataset, respectively." (p.5)
- "detecting hate speech may require knowing the background; that is something that may not be hate speech on the surface, may be hate speech when one knows the context." (p.5)
- "Analysis of errors show that the system is able to capture hate speech that is visible on the surface (e.g. swear words), while missing those that require background knowledge or use of infrequent words or shorthands." (p.8)

## 13. UNKNOWN / not in extract
- Full confusion matrix in the appendix (only partially discussed in text).
- Exact number of annotators for Refugees dataset by group (HDV vs. students) and their specific inter-annotator agreement.
- Whether the dataset has been subsequently merged into a Turkish superset (referenced in related Tonneau et al. work but not described here).
- Dataset license terms beyond "publicly available at GitHub."
- Long-term plans for dataset expansion mentioned but not detailed.
