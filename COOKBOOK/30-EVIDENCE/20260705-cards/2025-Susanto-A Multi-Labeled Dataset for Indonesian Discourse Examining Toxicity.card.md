---
stem: "2025-Susanto-A Multi-Labeled Dataset for Indonesian Discourse Examining Toxicity"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, normative-ethics, pluralism-aggregation]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 28477
dataset_construction: "scraped"
languages: ["id"]
models_tested: ["IndoBERTweet", "NusaBERT", "Multi-e5", "Llama3.1-8B", "Aya23-8B", "SeaLLMs-7B", "GPT-4o", "GPT-4o-mini"]
headline_numbers:
  - "28,477 unique Indonesian texts annotated for toxicity and polarization (p.4)"
  - "IndoBERTweet achieves Macro F1 of 0.791 on toxicity detection (p.5)"
  - "GPT-4o achieves Macro F1 of 0.776 on toxicity, but only 0.553 on polarization detection (p.5)"
  - "Gwet's AC1 inter-coder reliability 0.61 for toxicity, 0.37 for polarization (p.3)"
  - "~48% of toxic texts during 2024 Indonesian election were polarizing; only 25% of polarizing texts are toxic (p.8)"
  - "Online toxicity in Indonesia increased tenfold from 1.35% (2019) to 13.8% (2024) (p.1)"
---

## 1. Gist

This paper introduces IndoToxic2024, the first multi-labeled Indonesian dataset combining toxicity detection, political polarization classification, and annotator demographic information. Collected from social media (Twitter/X, Facebook, Instagram) and news articles during Indonesia's 2024 presidential election campaign, the dataset contains 28,477 texts annotated by 29 demographically diverse annotators. The paper demonstrates that polarization information improves toxicity classification and vice versa, and that annotator demographic data (ethnicity, religion, domicile) significantly boosts polarization detection performance. For values-alignment benchmarking, this work is important because it shows how subjective constructs like polarization require demographic-aware annotation, and provides evidence that standard majority-vote aggregation may be counterproductive for highly subjective labels.

## 2. Benchmark/eval design features

The dataset operationalizes two constructs: (1) binary toxicity (toxic / not toxic), with subtypes including insults, threats, profanity, identity attacks, and sexually explicit content; and (2) binary polarization (polarized / not polarized), defined as content designed to reinforce inter-group biases and invoke in-group identity. A codebook was developed via literature review and consultations with minority community representatives, addressing both explicit (direct insults) and implicit (sarcasm) expressions.

Key design features:
- Multi-label: each text receives both toxicity and polarization labels
- Annotator demographic metadata recorded at fine granularity (religion, ethnicity, domicile, gender, age, education, vote choice)
- Variable annotation depth: 55.4% single-coder, 44.6% multi-coder
- Label aggregation via majority vote; texts with perfect disagreement excluded
- Stratified 5-fold cross-validation for BERT models; zero-shot for LLMs
- Cross-task feature experiments: toxicity as a feature for polarization prediction and vice versa

## 3. Task format & example item

The annotation task is binary classification (toxic / not toxic; polarized / not polarized) applied to social media texts. No verbatim example item is provided in the extract for annotators. However, the classification prompt structure for LLMs is referenced in Appendix I (not reproduced in the extract). The model evaluation uses standard binary classification prompts with optional demographic or cross-task feature augmentation appended to the input, e.g., "Average toxicity value (ranged 0 to 1): [value]" (p.6).

## 4. Scoring / grading methodology

- BERT models: stratified 5-fold cross-validation; metrics = Accuracy, Macro F1, Precision@1, Recall@1, ROC AUC
- LLMs: zero-shot classification (two-shot in appendix); same metrics except ROC AUC not computed for LLMs
- Inter-coder reliability: Gwet's AC1 (chosen over Cohen's Kappa for robustness to class imbalance)
- Label aggregation: majority vote (AGG) as primary; ANY (at least one annotator flags) as alternative
- Demographic experiment: "exploded" dataset splits multi-annotator entries into per-annotator records

## 5. Dataset construction & provenance

- Sources: X/Twitter via Brandwatch, Facebook/Instagram via CrowdTangle, news from CekFakta fact-checking site
- Time span: September 2023 – January 2024 (Indonesian presidential election period)
- Initial corpus: 42,846 texts (36,550 tweets, 1,548 Facebook posts, 3,881 Instagram posts, 867 news articles)
- After quality filtering (deduplication, spam removal, minimum 4 words): final annotated set = 28,477 texts
- 29 annotators recruited from diverse demographic backgrounds; compensated at 1.14 million IDR per 1,000 texts
- Class imbalance mitigated by 1:3 positive-to-negative balancing for experiments (Toxic Exp: 2,156 toxic; Polar Exp: 3,811 polarized)
- Dataset publicly available at https://huggingface.co/datasets/Exqrch/IndoToxic2024

## 6. Validity evidence

- Gwet's AC1 = 0.61 for toxicity after three training sessions (comparable to prior studies including Davidson et al. 2017)
- Gwet's AC1 = 0.37 for polarization (remains 0.39 after 1:3 balancing), indicating higher subjectivity
- Cross-task correlation: logistic regression predicting toxicity from polarization yields AUC-ROC > 0.68 in all splits (p.8)
- Kendall-Tau between toxicity and polarization labels: 0.28–0.40 depending on split (p.4)
- IndoBERTweet as highest-performing model provides implicit construct validation
- No formal factor analysis or external criterion validation reported

## 7. Saturation / discrimination

- Strong class imbalance in raw data (skewed toward non-toxic, non-polarized); corrected via 1:3 subsampling for experiments
- BERT models show moderate score spread (F1 range roughly 0.43–0.79); LLMs show more extreme variation (Aya23-8B at 0.429 Macro F1 due to classifying everything as non-toxic)
- Polarization detection harder than toxicity: best LLM Macro F1 for polarization = 0.553 (GPT-4o) vs 0.776 for toxicity
- Ceiling not reached: best model (IndoBERTweet + cross-task + demographic) achieves F1@1 = 0.748 for polarization and 0.765 for toxicity (p.9), leaving substantial headroom

## 8. Multiturn / agentic aspects

n/a — single-turn text classification task; no interactive or agentic protocol.

## 9. Key numbers

- 28,477 unique texts in final dataset (p.4)
- 29 annotators with diverse demographic profiles (p.3)
- Tenfold increase in online toxicity in Indonesia: 1.35% in 2019 → 13.8% in 2024 (p.1)
- Gwet's AC1: 0.61 toxicity, 0.37 polarization (p.3)
- IndoBERTweet baseline: Accuracy 0.844, Macro F1 0.791 for toxicity; Accuracy 0.801, Macro F1 0.731 for polarization (p.5)
- GPT-4o: Macro F1 0.776 toxicity, 0.553 polarization (p.5)
- Adding polarization as feature: IndoBERTweet toxicity Macro F1 0.791 → 0.828 (p.6)
- Best combined (featural + demographic): polarization Macro F1 = 0.830 (p.9)
- ~48% of toxic texts are also polarizing; only 25% of polarizing texts are toxic (p.8)
- Disability shows highest polarizing identity gap: Gwet's AC1 gap 0.37 toxicity, 0.46 polarization (p.8)

## 10. Pitfalls & limitations

- Low inter-coder reliability for polarization (AC1 = 0.37–0.39) introduces noise in polarization labels
- 29 annotators is potentially insufficient to capture Indonesia's full cultural/linguistic diversity (277 million population, many ethnic groups)
- No comparable existing dataset; cannot benchmark against prior work
- Mental burden of annotating toxic content acknowledged; some annotators did not complete assignments
- Single-coder annotations (55.4% of data) cannot undergo reliability checks
- GPT-4o-mini fails to leverage demographic information, likely due to Indonesian language underrepresentation in training data
- Annotation keywords derived from expert consultation may miss emerging forms of toxicity/polarization
- Majority-vote aggregation may be counterproductive for polarization given its inherent subjectivity

## 11. Novel ideas worth stealing

1. **Cross-task feature augmentation**: Using toxicity labels as features for polarization prediction (and vice versa) is a low-cost way to improve classification performance. For values-alignment benchmarks with correlated constructs (e.g., harm and offensiveness, or deception and manipulation), jointly modeling them as cross-task features could outperform independent assessment.

2. **Demographic-aware annotation design**: Recording annotator demographics at fine granularity enables post-hoc analysis of which identities produce the most polarizing disagreements. For values benchmarks, this allows identification of which demographic groups disagree most about what is harmful or normative—a key validity check.

3. **Polarizing identity gap metric**: Defining polarizing identities by the gap between in-group agreement and out-group disagreement (Gwet's AC1 gap) is a concrete operationalization. This could be applied to values-alignment benchmarks to identify which annotator identity groups produce the most divergent moral judgments.

4. **Wisdom-of-the-crowd experiment**: Systematically comparing single-coder vs multi-coder subsets and different label aggregation rules (majority vote vs ANY) reveals whether tasks are better treated as having ground truth vs inherently perspectival. This methodology should be standard for any subjective values benchmark.

5. **Exploded dataset for demographic conditioning**: Splitting multi-annotator entries into per-annotator records (the "exploded" dataset) allows testing whether demographic context improves model performance without requiring extra annotations—a resource-efficient design for demographically-aware evaluation.

## 12. Notable quotes

"Polarization detection is more challenging than toxicity detection. A possible explanation is that many models are explicitly trained to avoid generating toxic outputs, passively learning about toxicity detection, while polarization detection is largely neglected during training." (p.4–5)

"Although toxicity detection is inherently subjective, our findings suggest that polarization detection is even more so. In a large enough annotator pool, it is likely that at least one person will perceive a text as polarizing." (p.7)

"Approximately 48% of toxic texts during Indonesia's 2024 Presidential Election were used for polarizing purposes. Given that only 25% of polarizing texts are toxic, our dataset suggests that Indonesia is becoming polarized at a faster rate than it is becoming toxic." (p.8)

"GPT-4o-mini does not effectively utilize demographic information. Likely due to its training data limitations, GPT-4o-mini ignores demographic attributes except in one setup, where recall improves at the cost of precision." (p.9)

## 13. UNKNOWN / not in extract

- Full codebook contents (referenced as Appendix B but not reproduced)
- Exact LLM prompts used for classification (referenced as Appendix I)
- Two-shot LLM results (Appendix H)
- Full demographic conditioning results table (Appendix G.4, Table 20)
- Complete polarizing identity analysis for all demographic groups (Appendix L)
- License terms of the dataset beyond the usage statement
- Whether the dataset includes the original social media text or anonymized versions
