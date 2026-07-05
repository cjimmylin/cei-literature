---
stem: "2025-Neplenbroek-Cross-Lingual Transfer of Debiasing and Detoxification in"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, contamination-robustness, validity-psychometrics, best-practices]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: null
dataset_construction: "scraped"
languages: ["Arabic", "Catalan", "Chinese", "Czech", "Dutch", "English", "French", "German", "Hindi", "Indonesian", "Italian", "Japanese", "Korean", "Maltese", "Polish", "Portuguese", "Russian", "Spanish", "Swedish", "Turkish"]
models_tested: ["Aya 23 8B", "Aya Expanse 8B", "Gemma 2 2B IT", "Gemma 2 9B IT", "Llama 3 8B Instruct", "Llama 3.1 8B Instruct", "Mistral 7B Instruct v0.3"]
headline_numbers:
  - "GPT sample replicated 37.5% of original effects and 37.5% of Many Labs 2 effects (p.4)"
  - "Aya 23 toxicity score 0.541 ± 0.066 (above 0.5 threshold) across non-English languages (p.5)"
  - "Llama 3.1 Instruct language consistency 80.8 ± 15.2% across non-English languages (p.5)"
  - "Llama 3 Instruct language consistency only 15.1 ± 7.2% (p.5)"
  - "Significant moderate correlation with Common Crawl data percentage: -0.6 < r < -0.4 for most models (p.9)"
  - "DPO on DetoxDPO reduces toxicity in English and non-English languages in all models (p.7)"
---
## 1. Gist
This paper presents an extensive empirical investigation into cross-lingual transfer of debiasing and detoxification in multilingual LLMs. The authors fine-tune 7 instruction-tuned LLMs using 4 different English datasets (2 for debiasing, 2 for detoxification) and evaluate whether the resulting bias/toxicity reductions transfer to 20 non-English languages. The central finding is that successful transfer — when it occurs — consistently comes at the cost of degraded language generation ability in non-English languages, particularly affecting language consistency (generating responses in the correct language). For values-alignment benchmarking, this paper is crucial because it demonstrates that evaluation using only English-language benchmarks cannot reliably predict model behavior in other languages, and that debiasing approaches effective in English may actually harm non-English speakers by making models switch to English.

## 2. Benchmark/eval design features
The paper evaluates along three dimensions: (1) **Bias** using CrowS-Pairs (revised multilingual versions covering race, gender, sexual orientation, religion, age, nationality, disability, appearance, socio-economic status), StereoSet (gender, profession, race, religion), and MBBQ (Dutch, Spanish, Turkish; MCQ format measuring bias in downstream QA); (2) **Toxicity** using RTP-LX benchmark across 17 languages measured via Perspective API, reporting Expected Maximum Toxicity (EMT) from 25 completions per prompt; (3) **Language generation ability** measured as language consistency (% in-language), fluency (mT5-XL perplexity), diversity (distinct unigrams), and Global-MMLU question-answering.

Core claims: SFT on curated non-harmful text effectively reduces bias; only DPO effectively reduces toxicity; both methods degrade non-English generation quality; transfer magnitude correlates with amount of pretraining data in the target language (Common Crawl % as proxy); bias types in the finetuning dataset transfer more strongly but cross-bias-type transfer also occurs.

## 3. Task format & example item
CrowS-Pairs bias score: model is presented two minimally different sentences (stereotypical vs. anti-stereotypical) and the bias score is the percentage of samples for which the model assigns higher probability to the stereotypical sentence. Ideal score = 50.

MBBQ ambiguous context example (paraphrased, no verbatim item in extract): Multiple-choice question about a person from a stereotyped group with three options: (a) stereotyped individual, (b) non-target individual, (c) "not enough information." In ambiguous contexts, (c) is correct; bias score = % choosing stereotyped answer. (p.4, Appendix A.1)

## 4. Scoring / grading methodology
- **CrowS-Pairs / StereoSet**: Probability-based; bias score = % of pairs where model prefers stereotypical sentence. Ideal = 50 (chance).
- **MBBQ**: Downstream QA; bias score computed via Equations 1 and 2 (Appendix A.1), ideal = 0 in both ambiguous and disambiguated contexts.
- **Toxicity (RTP-LX)**: Perspective API scores (0–1 scale) for 25 completions per prompt; Expected Maximum Toxicity (EMT) aggregated; only in-language completions counted.
- **Language consistency**: fastText detection of whether continuation is entirely in the prompting language; reported as % of 1000 Tatoeba sentences.
- **Fluency**: Median negative perplexity from mT5-XL, computed only on in-language generations.
- **Diversity**: Proportion of distinct unigrams not in input prompt, for in-language generations.
- **QA**: 5-shot Global-MMLU via lm-evaluation-harness.

## 5. Dataset construction & provenance
Fine-tuning datasets (all English):
- **Panda** (Qian et al., 2022): 95K sentences for SFT debiasing
- **Jigsaw** (cjadams et al., 2019): 95K non-toxic comments for SFT detoxification
- **BiasDPO** (Allam, 2024): 1.1K prompts with preferred/rejected completions for DPO debiasing
- **DetoxDPO** (Lee et al., 2024): 25K prompts with preferred/rejected completions for DPO detoxification

Evaluation benchmarks: CrowS-Pairs (revised by Fort et al. 2024 in 8 languages), StereoSet (Korean, German, French, Spanish, Turkish translations), MBBQ (Dutch, Spanish, Turkish), RTP-LX (17 languages), Global-MMLU (11 professionally translated + 6 machine-translated languages), Tatoeba sentences for language consistency.

Models fine-tuned using QLoRA on the English datasets.

## 6. Validity evidence
The paper uses well-established multilingual benchmarks. It notes that bias scores across different benchmarks (CrowS-Pairs vs. StereoSet vs. MBBQ) correlate poorly with each other, consistent with prior literature (Prakash & Lee, 2023; Delobelle et al., 2022; Zayed et al., 2024), which is a validity concern for any single bias metric. The paper explicitly acknowledges that English-centric benchmarks reflect US-centric stereotypes and may miss culturally unique biases (Ethical Considerations section, p.10). Qualitative analysis by two annotators of 100 most/least toxic generations adds triangulation (p.7). The use of Spearman correlations to assess predictors of cross-lingual transfer provides a systematic approach to understanding generalization.

## 7. Saturation / discrimination
Initial model evaluations show substantial variance across models and languages:
- CrowS-Pairs: 57.04–62.19 across models (ideal 50), indicating moderate bias above chance
- Toxicity EMT: 0.398–0.541, with Aya 23 and Llama 3.1 above 0.5 (toxic on average)
- Language consistency: 15.1–82.7%, showing models vary dramatically in ability to generate in target language

The wide variation in language consistency (15.1% for Llama 3 to 82.7% for Gemma 2 9B IT) means several models were excluded from finetuning experiments, limiting coverage. The small sample of languages per benchmark limits statistical power in correlation analyses.

## 8. Multiturn / agentic aspects
n/a. All evaluations are single-turn generation or classification tasks.

## 9. Key numbers
- 7 LLMs evaluated across 20 languages (p.1)
- 4 finetuning datasets: Panda (95K), Jigsaw (95K), BiasDPO (1.1K), DetoxDPO (25K) (p.4, Table 1)
- Aya 23 non-English CrowS-Pairs bias: 57.90 ± 5.25; toxicity 0.541 ± 0.066; language consistency 72.3 ± 22.3% (p.5, Table 2)
- Gemma 2 9B IT CrowS-Pairs: 62.19 ± 4.88 (highest bias on that benchmark) (p.5)
- Llama 3 Instruct language consistency: 15.1 ± 7.2% (lowest; excluded from finetuning) (p.5)
- Llama 3.1 Instruct language consistency: 80.8 ± 15.2% (p.5)
- SFT on DetoxDPO: increases toxicity rather than decreasing it (counterintuitive finding) (p.7)
- DPO on DetoxDPO: reduces toxicity in English and all non-English languages for all 4 finetuned models (p.7)
- Cross-lingual transfer correlation with Common Crawl data: -0.6 < r < -0.4 for non-Aya models (p.9)
- Languages covered by Perspective API (toxicity eval): 17 (p.4)
- 25 completions per prompt for toxicity, max 20 tokens, temperature 0.9, top-p 0.8 (p.4)

## 10. Pitfalls & limitations
- **English-centric bias measures**: CrowS-Pairs and StereoSet translations reflect US stereotypes, missing culturally specific biases in non-Western languages (p.10)
- **Perspective API limitations**: Black-box model with its own biases (Sap et al., 2019); frequently retrained complicating reproducibility (p.10)
- **GPU resource constraints**: Models trained for limited epochs, sometimes on dataset subsets (p.10)
- **Language benchmark gaps**: PolygloToxicityPrompts excluded; StereoSet semi-automatically translated (possible errors) (p.10)
- **Benchmark validity**: Low cross-benchmark correlations in bias measurement raise construct validity questions (p.6)
- **Generalizability**: Results specific to instruction-tuned models; base model results differ and are relegated to appendix
- **Selection bias in evaluation languages**: Coverage varies by benchmark; not all 20 languages are in all benchmarks
- **Author-identified**: The paper recommends language-specific debiasing rather than cross-lingual transfer but does not provide a solution

## 11. Novel ideas worth stealing
1. **Trade-off tracking as benchmark requirement**: Any values-alignment benchmark should measure not just the target value but also language generation quality (consistency, fluency, diversity) after interventions — measuring harms of alignment is as important as measuring alignment success.
2. **Language consistency as a hidden dimension of fairness**: For multilingual benchmarks, tracking what % of model responses stay in the evaluation language is a prerequisite validity check before any bias/values measure. A model generating only English for non-English prompts is not actually being evaluated cross-lingually.
3. **Pretraining data fraction as predictor of cross-lingual generalization**: Spearman correlations between Common Crawl language representation and transfer success suggest that benchmark designers can predict which languages will show similar model behavior to English — a cheap proxy for identifying which languages need language-specific evaluation.
4. **Qualitative + quantitative triangulation**: Side-by-side comparison of 100 most/least toxic completions across finetuning conditions catches patterns that aggregate metrics miss (e.g., DPO models adopt quotation style to avoid toxicity).
5. **Separating dataset size effect from finetuning method effect**: The paper's design (SFT on both SFT-format and DPO-format datasets) allows isolating whether differences are due to the data or the training objective — a useful factorial design for any evaluation of alignment techniques.

## 12. Notable quotes
- "We find evidence that the extent to which transfer takes place can be predicted by the amount of data in a given language present in the model's pretraining data." (p.1)
- "Whenever debiasing and detoxification successfully transfer from English, this comes paired with a decrease in language generation ability in other languages." (p.2)
- "Even before debiasing, LLMs may struggle to reply in the correct language, often generating English text in response to user input in a different language." (p.3)
- "We recommend executing bias and toxicity mitigation in the evaluation language rather than relying on transfer from English, particularly for lower resource languages." (p.9)

## 13. UNKNOWN / not in extract
- Exact quantitative results for individual language pairs beyond the aggregate figures and the selected figures (most per-language breakdown is in figures described but not fully transcribed in the extract)
- Full contents of Appendices A–L (referenced throughout but not visible in extract)
- Specific correlation values in Table 10 (Appendix J)
- The exact hyperparameters and compute budget (Appendix C)
- Detailed descriptions of finetuning datasets (Appendix A, Table 4)
- Full results for base (non-instruction-tuned) models (Appendix I)
- Whether the paper went through peer review (arXiv preprint, v4 as of June 2025)
