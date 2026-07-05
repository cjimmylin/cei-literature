---
stem: "2024-Joy-Gender Bias Mitigation for Bangla Classification Tasks"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, validity-psychometrics, normative-ethics]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: 31537
dataset_construction: "crowdsourced"
languages: ["bn"]
models_tested: ["BanglaSARC (ELECTRA)", "Abusive-MuRIL", "BanglaBERT-Sentiment", "multilingual toxicity BERT"]
headline_numbers:
  - "Toxicity detection model has highest bias: 7.48% mismatch rate (p.1)"
  - "Sarcasm detection model has lowest bias: 0.46% mismatch rate (p.1)"
  - "Joint Loss Optimization (JLO) achieves 11.73 normalized bias score vs. 100 baseline (p.4)"
  - "Token Masking (TM) achieves 0 normalized bias score but accuracy drops to 61.71% on hate speech (p.4)"
  - "JLO overall average accuracy: 80.30%; FOA overall average accuracy: 79.95% (p.4)"
  - "Gendered word pair dictionary: 573 pairs in Bangla (p.2)"
---
## 1. Gist
This paper addresses gender bias in Bangla pretrained language models (PLMs), a significantly underexplored area in low-resource NLP. The authors curate four task-specific datasets for sentiment analysis, toxicity detection, hate speech detection, and sarcasm detection by applying gender-name swapping to existing Bangla datasets, then propose and evaluate a joint loss optimization (JLO) technique—combining cross-entropy and cosine similarity loss—to reduce gender bias while preserving classification accuracy. The paper is relevant to values-alignment benchmarking as it demonstrates a practical methodology for bias detection and mitigation in low-resource languages, and introduces a Bangla-specific gender-bias detection protocol based on counterfactual pair generation.

## 2. Benchmark/eval design features
This is a bias detection and mitigation study, not a standalone benchmark. Core approach: measure gender bias as the rate of label disagreement between original texts and gender-name-swapped counterparts. Four task dimensions: sentiment (positive/negative), sarcasm (sarcastic/non-sarcastic), toxicity (toxic/non-toxic), hate speech (hate/non-hate). Bias detection: a model is considered biased if predictions differ between original and swapped pairs. Mitigation methods compared: (1) zero-shot inference, (2) fine-tuning on original data only (FOD), (3) token masking (TM) of all gender terms, (4) joint loss optimization (JLO), and (5) fine-tuning on original+augmented data (FOA).

The JLO method is the core contribution: a custom loss function combining cross-entropy loss (for classification accuracy) and cosine similarity loss (to align embeddings of original and gender-swapped texts). The loss: Jloss = LCE + λLGB, where LGB = 1 − cos(e1, e2) for embeddings e1, e2 of original and swapped texts.

## 3. Task format & example item
The tasks are binary/multiclass classification of Bangla text. Example of gender swapping (Table 5, p.9):

Original: "Sister Tisha can write very beautiful poems." [Bangla text with female gender term "Apu"]
→ After gender term swap: "Brother Tisha can write very beautiful poems." [female term replaced with male]
→ After NER-based name swap: "Brother Ashraf can write very beautiful poems." [female name "Tisha" replaced with male name "Ashraf"]

The gender-name-swapped text is the counterfactual input. Bias is detected when the model's label changes between original and swapped texts.

## 4. Scoring / grading methodology
Bias Percentage = (count of mismatched predictions) / (total number of pairs) × 100. Normalized Bias Score = (count of mismatched predictions for approach) / (count for zero-shot baseline) × 100, so zero-shot always scores 100, lower is better. Classification accuracy measured on both original and gender-swapped versions separately, with average reported. Metrics: accuracy for classification performance; normalized bias score and raw mismatch percentage for fairness.

## 5. Dataset construction & provenance
Four existing Bangla datasets were collected and transformed:
- Sentiment (Sazzed 2020): 11,807 texts → 4,857 with gender terms
- Sarcasm (BenSarc/Lora et al. 2023): 25,636 → 9,589 with gender terms
- Toxicity (Belal et al. 2023): 16,073 → 7,057 with gender terms
- Hate Speech (Romim et al. 2021): 30,000 → 10,034 with gender terms
Total: ~31,537 original texts with gender terms (doubled to ~63,074 with swapped pairs).

Transformation: (1) Built 573-pair Bangla gender dictionary from internet/grammar books. (2) Applied NER model to identify person names. (3) Swapped gender terms and names. (4) Human evaluators (4 undergraduate annotators selected from 10 via exam) reviewed and corrected: 28 missing gender terms found, 397 complex cases requiring manual conversion, 548 incorrect conversions corrected, 749 NER mistakes corrected. The bias test sets are the mismatched-prediction subsets (from Table 1): Sentiment 218, Sarcasm 45, Toxicity 528, Hate Speech 525.

## 6. Validity evidence
Human review by 4 annotators provides some quality control. The annotation quality of the underlying datasets was not re-assessed. No formal inter-annotator agreement study was conducted for the gender-swapping process itself (though the annotators were tested for competence). Construct validity is supported by prior English-language work showing that gender-name swapping reveals latent biases.

## 7. Saturation / discrimination
The bias percentages are relatively small (0.46%–7.48%), meaning most original tasks show limited gender sensitivity. Token Masking fully eliminates bias but at cost to accuracy (hate speech accuracy drops to 61.71%). JLO and FOA both leave modest residual bias, meaning they discriminate bias levels effectively. The zero-shot baseline shows large disparity between original and swapped accuracy (e.g., sentiment original: 27.06% vs. swapped: 45.87%), indicating strong label asymmetry in baseline models.

## 8. Multiturn / agentic aspects
Not applicable. Single-turn classification tasks only.

## 9. Key numbers
- Bias rates (zero-shot): Sentiment 4.48%, Sarcasm 0.46%, Toxicity 7.48%, Hate Speech 5.23% (Table 1, p.2)
- Dataset sizes: Sentiment 4,857; Sarcasm 9,589; Toxicity 7,057; Hate Speech 10,034 (Table 1, p.2)
- Gender dictionary: 573 masculine/feminine word pairs (p.2)
- 28 missing gender terms found in human review (p.9)
- 397 instances of complex gender terms not swapped automatically (p.10)
- 548 incorrect gender conversions corrected (p.10)
- 749 NER errors corrected (p.10)
- Normalized bias scores: TM=0, JLO=11.73, FOA=7.18, FOD=20.39 (Table 3, p.4)
- JLO overall average accuracy: 80.30%; FOA: 79.95%; TM: 78.63%; FOD: 76.02% (Table 2, p.4)
- Hyperparameters: batch size 16, LR 1e-4, dropout 0.2, λ=1, 15 epochs (p.3)

## 10. Pitfalls & limitations
- Binary gender assumption: only male/female, excludes non-binary identities (p.5)
- NER model accuracy limited for Bangla, requires extensive human correction (p.5)
- Only PLMs tested; LLMs not evaluated, limiting relevance to current frontier models (p.5)
- Consistent hyperparameters across all approaches may disadvantage some methods (p.5)
- Datasets may lack diversity and balance, limiting generalizability (p.5)
- Bias test sets derived from model mismatches (circular): training on these may overfit to the original model's specific biases
- No analysis of whether the gender-swapped text preserves semantic naturalness in all cases

## 11. Novel ideas worth stealing
1. **Counterfactual pair generation for bias detection**: The gender-name swapping protocol—dictionary-based term replacement combined with NER-based name replacement—is a replicable methodology for building counterfactual test sets in low-resource languages. Directly applicable to building bias detection benchmarks for any language with a gender dictionary.
2. **Joint embedding alignment loss**: The JLO approach of jointly minimizing classification loss and cosine distance between original/counterfactual embeddings is a clean in-processing debiasing technique that balances fairness and accuracy—worth adopting in value-aligned classifier fine-tuning.
3. **Task-specific bias measurement**: Measuring bias separately across different NLP tasks (sentiment, toxicity, hate speech, sarcasm) reveals that bias severity varies substantially by task type (0.46% to 7.48%)—a design principle for comprehensive bias benchmarks that should cover multiple task types.
4. **Low-resource language focus**: Most bias research is in English. The methodology here is adaptable to any low-resource language given a basic gender term dictionary and NER model, providing a template for expanding bias evaluations globally.

## 12. Notable quotes
- "Despite the increasing availability of pretrained Bangla language models, there are a very few works... that focused only on gender bias detection and mitigation." (p.1)
- "Token Masking (TM) was the most effective, achieving a bias score of 0, indicating complete bias elimination by masking names and gender terms." (p.4)
- "Our approach assumes binary gender categories, excluding non-binary identities, which restricts the scope of bias detection." (p.5)
- "Joint Loss Optimization (JLO) strikes the best balance... between bias mitigation and accuracy, with scores ranging from 70.94% to 85.77%." (p.4)

## 13. UNKNOWN / not in extract
- Full list of 573 gender word pairs (referenced as Appendix H but not extracted)
- Full male and female name lists (Appendix C, partially visible)
- Model architecture details beyond brief summaries (Appendix D, partially extracted)
- Full dataset statistics table (Table 6, partially readable)
- Statistical significance tests for accuracy/bias score differences
- Comparison with English-language debiasing benchmarks
- License information for the four source datasets
