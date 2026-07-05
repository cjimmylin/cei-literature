---
stem: "2022-Bang-Enabling Classifiers to Make Judgements"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, pluralism-aggregation, cultural-linguistic, best-practices]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 17720
dataset_construction: "LLM-generated"
languages: ["en"]
models_tested: ["OPT-175B", "GPT-Jurassic 6B", "GPT-Jurassic 17B", "GPT-Jurassic 178B", "OPT-1.3B", "OPT-6.7B", "ALBERT-base", "RoBERTa-base", "BART-base"]
headline_numbers:
  - "VA-BART achieves 74.07% accuracy and 74.36% W-F1, surpassing best baseline by 15.56% W-F1 (p.6)"
  - "OPT-175B few-shot baseline: 55.18% accuracy, 54.78% W-F1 (p.6)"
  - "Test set: 17,720 samples; label ratio 1:1:1 (Sexist:Non-Sexist:NA) (p.5)"
  - "19 sexism categories, 38 human values (19 value + 19 counter-value pairs) (p.4)"
  - "VA-BART on unseen values: 57.98% accuracy vs. OPT-175B 32.97% (p.8)"
---
## 1. Gist
Bang et al. introduce a **value-aligned classification framework** that separates the process of defining human values from the process of training classifiers. Rather than training a fixed classifier on labeled data encoding implicit societal norms, their VA-MODEL takes an explicit human value as a natural-language instruction and predicts whether a given piece of content is consistent with that value. The key methodological contribution is using LLMs (OPT-175B) to generate synthetic value-aligned training data through few-shot prompting, then distilling this into smaller classifiers (ALBERT, RoBERTa, BART). Applied to sexism classification across 19 culturally variable categories, VA-MODELs substantially outperform few-shot LLM baselines and semantic augmentation methods. This paper is directly relevant to values-alignment benchmarking: it operationalizes the insight that value judgments are culturally relative and demonstrates a practical architecture for encoding that variability.

## 2. Benchmark/eval design features
The **value-aligned judgement task** requires models to predict labels from {Sexist, Non-Sexist, NA} given a (content, value) pair:
- **Same content, different judgements**: The same text about role stereotyping can be judged "Sexist" with the value "Men and women are equally capable for any role" but "Non-Sexist" with "Men and women are biologically different; hence certain roles are more appropriate for women."
- **19 sexism categories** with opposing value/counter-value pairs (Table 6, p.13): Role stereotyping, Attribute stereotyping, Body shaming, Hyper-sexualization, Internalized sexism, Pay gap, Denial/trivialization, Threats, Sexual assault, Sexual harassment, Tone policing, Moral policing, Victim blaming, Slut shaming, Motherhood discrimination, Menstruation discrimination, Religion-based sexism, Physical violence, Mansplaining.
- **NA class**: Created by pairing content with an unrelated value/counter-value.

## 3. Task format & example item
Input format (p.4): `value [sep] content [sep]` → label ∈ {Sexist, Non-Sexist, NA}

Example value-counter-value pair for Role Stereotyping (p.5, Table 6 p.13):
- Value: "Men and Women are equally capable for any role."
- Counter-value: "Men and women are biologically different hence certain roles are more appropriate for women."

Same content labeled "Sexist" with value and "Non-Sexist" with counter-value.

## 4. Scoring / grading methodology
Weighted F1 (W-F1) and accuracy, evaluated on human-labeled test set. Results reported as mean ± std across 5 random seeds, with statistical significance via t-test (p<0.05) (p.6). Per-category results also reported for VA-BART (Figure 3).

## 5. Dataset construction & provenance
**Test set**: Derived from Parikh et al. (2019) multi-label sexism categorization dataset. 10 items per category held for prompt construction; remainder used for test. Each item converted to triplet {content, value, label}. 17,720 test samples; label ratio 1:1:1 (p.5).

**Training set (VA-MODEL)**: Synthetic — 100 content pieces generated per value/counter-value via OPT-175B few-shot prompting. 10,722 total samples (including prompt construction examples), split 4:1 train/validation. Duplicates, prompt copies, and sub-3-word items removed (p.4).

Human evaluation on two categories: Pay gap training data 69.44% judged relevant and sexist (R&S), Internalized sexism only 25% R&S (p.7) — revealing quality variation by category.

## 6. Validity evidence
- VA-MODELs significantly outperform all baselines by 15.56–40.83% W-F1 (p.6), indicating the approach captures value-aligned judgement better than baselines.
- Human evaluation of generated data quality reveals that data quality correlates with per-category model performance (Pay gap high quality → high performance; Internalized sexism low quality → low performance) (p.7).
- Removing human-labeled data (training with only synthetic data) shows minimal degradation: VA-BART drops −1.65% W-F1; VA-ALBERT actually improves slightly (p.7, Table 2).
- Generalization to unseen values: VA-MODELs maintain 55–58% accuracy while baselines drop to 33–48% (p.8, Table 3).

## 7. Saturation / discrimination
On the full test set, VA-BART achieves 74.07% accuracy — well above baselines but below ceiling (100%). Per-category variation is large: Menstruation-related discrimination and Pay gap achieve >90%, while Internalized Sexism is substantially lower (Figure 3). This discrimination across categories reflects real task difficulty differences rather than saturation. The 3-class balanced test set (1:1:1 ratio) prevents class imbalance from inflating accuracy.

## 8. Multiturn / agentic aspects
n/a — single-turn classification. The value is provided as a textual instruction in the input.

## 9. Key numbers
- 19 sexism categories, 38 values (19 value + 19 counter-value) (p.4)
- Test set: 17,720 samples, 1:1:1 label ratio (p.5)
- Training set: 10,722 synthetic samples (p.5)
- VA-BART accuracy: 74.07%, W-F1: 74.36% (p.6)
- Best baseline (Nlpaug-ALBERT) W-F1: 58.80% (p.6)
- VA-BART gain over best baseline: 74.36 − 58.80 = 15.56% W-F1 (p.6)
- OPT-175B few-shot W-F1: 54.78% (p.6)
- Vocabulary overlap train/test: 51.79%; only 0.01% samples share >80% vocabulary with test (p.7)
- GPT-Jurassic 178B vs. OPT-175B: 74.24% vs. 74.36% W-F1 (p.8, Table 4)
- W-F1 plateau above 200 training samples per category (p.8, Figure 5)

## 10. Pitfalls & limitations
- English only; value-aligned knowledge distillation may be harder for languages with less LLM coverage (p.9)
- Requires 100B+ parameter LLM for data generation; smaller models (OPT-1.3B: 66.50%, OPT-6.7B: 66.44%) substantially underperform (p.8)
- Per-category quality of generated data varies significantly; Internalized Sexism only 25% rated relevant-and-sexist by humans (p.7)
- Task tested only on sexism; extension to racism, toxicity, or other value-aligned tasks is future work
- The counter-values (e.g., "Women should be physically punished for misbehavior") are ethically uncomfortable — authors note this is a case study in cultural variation, not endorsement (p.9)
- W-F1 does not improve beyond 200 synthetic training samples per category; noisy data hurts at larger scales (p.8)

## 11. Novel ideas worth stealing
1. **Value-as-instruction input design**: Providing explicit natural-language values as part of the model input, rather than encoding them implicitly in training labels, enables a single model to make culturally relative judgements. This is the core design pattern for pluralism-aware values benchmarking.
2. **Value/counter-value test pair construction**: For each category, constructing both a "violating" value and a "permitting" value for the same content creates a powerful test of whether a model responds appropriately to value differences — directly reusable for measuring value sensitivity.
3. **LLM-distilled synthetic training data generation**: Using LLMs to generate training data for value-aligned tasks sidesteps costly human labeling. The approach is model-agnostic (GPT-Jurassic 178B ≈ OPT-175B, p.8).
4. **NA class construction via value mismatch**: Pairing content with a completely unrelated value/counter-value to create NA labels — a cheap, scalable way to add a "value not applicable" category to any alignment benchmark.
5. **Per-category quality analysis**: Human evaluation of generated training data quality per category (Table in p.7) as a quality control step before training — should be standard practice in LLM-generated benchmark construction.

## 12. Notable quotes
- "Different individuals and cultures may perceive sexism differently. As is shown in Figure 1, the same content can be considered to be sexist or non-sexist depending on the values provided to make the judgements." (p.1)
- "We propose that the human value definition should be decoupled from the value-alignment task. The former should be defined together with society, ethicists, social scientists, and so on. However, the mechanics of value alignment should be independent of the first part so that engineers do not define these values directly in the training data or in the code itself." (p.9)
- "The distinction from the existing value-aligned classification task and conventional classification tasks is that our task expects the model to incorporate explicitly provided values along with other inputs for making judgements." (p.3)
- "We observe that the vocabulary overlaps are generally small, which illustrates that OPT-175B can generate diverse data for different values (e.g., sexism categories) provided in prompts." (p.7)

## 13. UNKNOWN / not in extract
- The original Parikh et al. (2019) multi-label sexism dataset size and source
- How the 19 sexism categories were defined (linguists? literature?)
- Whether the full list of 10 human-labeled prompt construction examples per category is available
- Human evaluation methodology (rater demographics, number of raters, agreement scores)
- Whether the synthetic training data is released
- Results for non-sexism domains (racism, toxicity) mentioned as future work
