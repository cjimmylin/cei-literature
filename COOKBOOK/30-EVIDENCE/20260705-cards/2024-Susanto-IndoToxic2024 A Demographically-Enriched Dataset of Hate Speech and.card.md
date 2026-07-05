---
stem: "2024-Susanto-IndoToxic2024 A Demographically-Enriched Dataset of Hate Speech and"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, pluralism-aggregation, llm-judges-scoring]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 43692
dataset_construction: "crowdsourced"
languages: ["id"]
models_tested: ["IndoBERTweet", "gpt-3.5-turbo", "SeaLLM-7B-v2.5"]
headline_numbers:
  - "43,692 entries annotated by 19 diverse Indonesian annotators (p.1)"
  - "6,894 texts labeled as toxic out of 43,692 total (p.4)"
  - "Baseline macro-F1 of 0.78 for hate speech classification with IndoBERTweet (p.1)"
  - "GPT-3.5-turbo zero-shot baseline macro-F1 of 0.627 (p.6)"
  - "Gwet's AC1 inter-coder reliability score of 0.61 for toxicity label after three training sessions (p.3)"
  - "Males labeled 19.3% of data as toxic; females labeled 13% (p.4)"
  - "Adding demographic info to gpt-3.5-turbo improved zero-shot performance; adding to IndoBERTweet hurt performance due to data fragmentation (p.6-7)"
---

## 1. Gist
IndoToxic2024 is a demographically-enriched Indonesian hate speech and toxicity classification dataset comprising 43,692 social media texts annotated by 19 individuals from diverse demographic backgrounds (religion, ethnicity, gender, disability, LGBTQ+ status, political affiliation, etc.). Collected during Indonesia's 2024 presidential election period, the dataset is unique in preserving per-annotator labels rather than aggregating to a single ground truth, enabling the study of annotation subjectivity. For values-alignment benchmarking, the paper is important because it empirically demonstrates that hate speech annotation is inherently subjective along demographic lines, that models inherit the biases of their training annotators, and that demographic persona injection improves zero-shot LLM performance on toxicity detection—a design principle directly applicable to culturally-sensitive alignment evaluation.

## 2. Benchmark/eval design features
The dataset covers seven binary classification tasks:
1. Hate speech (binary: toxic / not toxic)
2. Identity attack
3. Incitement to violence
4. Insult
5. Profanity or obscenity
6. Sexually explicit content

Each entry is accompanied by **ten-dimensional demographic metadata** on the annotator: disability status, domicile, ethnicity, gender, generation (age group), LGBTQ+ status, education level, religion, work status, and political leaning. Labels are preserved per annotator (not majority-voted), allowing subjectivity analysis.

**Key subjectivity findings:**
- Chi-square tests confirm that annotation behavior differs significantly across demographic groups (except domicile) — rejecting the null hypothesis that random assignment would produce uniform hate speech ratios (p.4–5).
- Within-group ICR scores are not consistently higher than between-group ICR scores, revealing that intersectional identity (not single-axis demographics) drives agreement patterns (p.4–5).
- Models trained on one demographic group's annotations perform worse when tested on another group's annotations (e.g., Islam vs. Non-Islam: F1 drops from 0.66 to 0.597) (p.5, Table 3).

## 3. Task format & example item
**Task format**: Binary forced-choice classification (hate speech: yes/no; toxicity type: yes/no per category).

**Annotation instrument** (from codebook, Appendix C):
> "Q3: Does this text contain toxicity (hate speech)? Note: Irrelevant toxicity or hate speech includes hate speech that is meant as a joke among friends or is not considered hate speech by the recipient. Thus, it will be coded as 'No'. Yes / No"

**Prompt for gpt-3.5-turbo zero-shot** (p.6):
> "Is the Indonesian text below a hate speech [Demographic Information]? If yes, respond with 1, otherwise respond with 0. [TEXT]"

**Example of a divisive text** (p.11, Table 6):
> "Around 800 to 1000 Christians still live in Gaza, which is one of the oldest Christian communities worldwide. They are also evicted and killed. Entire faith groups died out in the land where Christianity originated." — 3 of 3 Christian/Catholic annotators labeled as hate speech; 0 of 10 non-Christian annotators labeled as hate speech.

## 4. Scoring / grading methodology
- Primary metric: **macro-F1 score** across binary classification tasks (stratified 10-fold cross-validation for fine-tuned models).
- Inter-coder reliability: **Gwet's AC1** (preferred over Cohen's Kappa for class-imbalanced social media data).
- For zero-shot models: macro-F1 without cross-validation.
- Subjectivity analysis: chi-square tests for distribution differences across demographic groups; within-group and between-group ICR score comparison.

## 5. Dataset construction & provenance
- **Source**: Social media posts from Facebook, Instagram, and Twitter/X, plus Cek Fakta (Indonesian fact-checking) articles, collected September 2023–January 2024 using keyword-based scraping.
- **Keywords**: Targeting vulnerable groups (Chinese Indonesians, LGBTQ+, Ahmadiyya, Shia, Catholics, Christians, disabled persons, Rohingya, Jewish groups, etc.) — full keyword list in Appendix B.
- **Annotators**: 18 external + 1 internal; recruited via focus group discussion with vulnerable community representatives; compensated at 1.5M IDR per 1,000 texts (~43% of average monthly wage).
- **Annotation phases**: 3 training rounds (100, 100, 249 texts respectively until Gwet's AC1 ≥ 0.61) + main annotation phase.
- **Augmentation**: CSIS private dataset (licensed by collaboration) and GPT-3.5-turbo synthetic data (10-shot generation) used for training baselines only.
- **License/access**: Code available at https://github.com/izzako/IndoToxic2024
- **Contamination controls**: Texts are from a specific election period (Sep 2023–Jan 2024); synthetic data used only for training, not evaluation.

## 6. Validity evidence
- **Inter-coder reliability**: Gwet's AC1 = 0.61 for toxicity label (moderate agreement); required three training sessions to achieve this (p.3).
- **Construct validity**: Subjectivity analysis shows annotation patterns align with expected group identity effects (e.g., texts targeting Shia/Ahmadiyya are easier for Islamic annotators to annotate; LGBTQ+ topics harder for Islamic annotators) (p.5, Figure 3).
- **Criterion validity**: Fine-tuned IndoBERTweet achieves macro-F1 0.78 on hate speech task (p.1), suggesting dataset supports meaningful classifier training.
- **External validity concern**: Baseline performance relies on a private CSIS dataset not publicly available, limiting reproducibility.

## 7. Saturation / discrimination
- Hate speech class prevalence: 6,894 toxic / 43,692 total (≈15.8%) — imbalanced.
- Worst-performing task: Incitement to violence (macro-F1 = 0.53), indicating this category is harder to classify and has room for improvement (p.6).
- Best-performing tasks: Insult (F1 = 0.85), Identity Attack (F1 = 0.80), Sexually Explicit (F1 = 0.80) (p.7, Table 4).
- SeaLLM-7B-v2.5 showed "subpar performance" (F1 = 0.517) zero-shot and was discontinued (p.9).
- GPT-3.5-turbo zero-shot: F1 = 0.627 without demographic info, improving with demographic persona injection — up to +0.47 macro-F1 improvement on specific topic-location combinations (p.7, Figure 5).

## 8. Multiturn / agentic aspects
n/a — single-turn binary classification tasks.

## 9. Key numbers
- Total dataset size: 43,692 entries (p.1)
- Toxic entries: 6,894 (p.4)
- Insult: 3,140 toxic texts (p.4, Table 2)
- Threat/Incitement to Violence: 2,837 (p.4)
- Profanity/Obscenity: 1,271 (p.4)
- Identity Attack: 1,061 (p.4)
- Sexually Explicit: 224 (p.4)
- Number of annotators: 19 (p.1)
- Annotation compensation: 1.5M IDR per 1,000 texts (p.3)
- ICR Gwet's AC1: 0.61 (p.3)
- Hate speech baseline (IndoBERTweet, full augmented data): macro-F1 0.78 (p.1)
- IndoBERTweet on IndoToxic2024 only (no augmentation): macro-F1 0.718 (p.6, Table 5a)
- IndoBERTweet + topic info: macro-F1 0.755 (p.6, Table 5b)
- IndoBERTweet + demographic info: macro-F1 0.672 — worse than baseline (p.6, Table 5b)
- GPT-3.5-turbo zero-shot: macro-F1 0.627 (p.6)
- Islam-trained / Islam-tested: F1 0.660; Islam-trained / Non-Islam-tested: F1 0.597 (p.5, Table 3)
- GPT-3.5-turbo improvement from domicile info (Medan + Rohingya texts): +0.47 macro-F1 (p.7)

## 10. Pitfalls & limitations
- **Private dataset dependency**: Best baselines use the private CSIS dataset, limiting reproducibility.
- **Fine-tuned vs. zero-shot comparison**: gpt-3.5-turbo was not fine-tuned due to computational constraints, making direct comparisons with IndoBERTweet unfair.
- **Inconsistent annotator count**: Varying numbers of annotators across phases may produce uneven demographic coverage.
- **Controlled topic distribution**: In main annotation phase 1, annotators received 50% in-group texts (except Shia/Ahmadiyya at 39.3%), introducing allocation bias.
- **Keyword-based topic extraction**: Naive keyword matching may miss nuanced or emergent topics.
- **Small annotator pool**: 19 annotators is very small for a 43,692-entry dataset, especially after demographic sub-grouping — some groups have only 1–2 annotators (e.g., Ahmadiyya, Buddhist).
- **Political context specificity**: Dataset collected during a specific election; generalizability to other contexts is uncertain.
- **Mental health toll**: Authors acknowledge the psychological burden of annotating hate speech, which may have affected annotation consistency.

## 11. Novel ideas worth stealing
1. **Per-annotator label preservation**: Rather than majority-voting labels, preserving individual annotator labels enables subjectivity analysis and persona-conditioned evaluation. New values benchmarks should preserve annotator identity metadata alongside labels to study whose values a model is aligned with.

2. **Demographic persona injection for zero-shot evaluation**: Providing the LLM with an annotator persona ("Reader information: Chinese ethnicity, Christian, Male, Millennial") improves zero-shot performance significantly on culturally-grounded tasks. This is a direct design principle: use demographic conditioning to probe cultural value alignment.

3. **Within-group vs. between-group ICR analysis**: Comparing inter-rater reliability within demographic groups vs. across groups reveals whether disagreement is driven by demographics or by item difficulty. This analytical framework applies to any annotation task with demographic diversity.

4. **Topic × demographic interaction mapping**: The paper plots how adding demographic info affects performance per topic (Figures 5–7), revealing which topics are culturally specific and which are universal. Values benchmarks could adopt this as a standard diagnostic.

5. **Data fragmentation warning**: Adding demographic conditioning to fine-tuned models can hurt performance when demographic groups are small (fewer training samples per demographic bucket). This is a practical caution for benchmark designers using demographically-stratified training data.

6. **Codebook-driven implicit hate speech annotation**: The annotation guidelines explicitly address both manifest (explicit slurs) and latent (implicit/sarcastic) hate speech. This distinction—and the training sessions required to achieve inter-annotator agreement—is a model for values annotation tasks involving subtle norm violations.

## 12. Notable quotes
- "The perception of hate speech is influenced by the identity of a person or a group. A text may be considered hate speech by one group of people, while another group may not view it as such." (p.1, Figure 1 caption)
- "A model fine-tuned on Non-Islam annotators' labels tends to perform worse when tested on Islam annotators' labels compared to when tested on their own labels." (p.5)
- "Demographic information makes gpt-3.5-turbo a better hate speech detector. There could be other unexplored scenarios where demographic information is beneficial for different tasks." (p.8)
- "Though we hoped to increase the model's performance by providing demographic information, this instead fragmented the training data, with fewer training data for each demographic." (p.8)

## 13. UNKNOWN / not in extract
- The full content of appendices G and H (figures only, no text visible in pages 15–56 of the extract).
- Whether IndoToxic2024 dataset is publicly released and under what license.
- Specific demographic breakdown of annotators by religion (full fine-grained table beyond coarse-grained Table 1).
- Exact prompts used for synthetic data generation via GPT-3.5-turbo (referenced as Figure 8 in Appendix E, not visible in text).
- Publication venue details (arXiv preprint 2406.19349v2, updated June 2025).
