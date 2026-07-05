---
stem: "2025-Zhou-Bias Beyond English Evaluating Social Bias and Debiasing Methods in a"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, saturation-discrimination, best-practices]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 1042
dataset_construction: "scraped"
languages: ["en", "zh", "ru", "id", "th"]
models_tested: ["mBERT", "XLM-RoBERTa", "XGLM", "Gemma 3", "Qwen 2.5", "LLaMA 3"]
headline_numbers:
  - "mBERT average bias score in Thai: 90.69 (p.5)"
  - "LLaMA 3 average bias score in English: 7.68, lowest of all models (p.5)"
  - "SenDeb achieves -37.96% bias reduction in Chinese, highest cross-lingual gain (p.8)"
  - "Dataset covers 1,042 sentences across 5 languages and 4 bias types (p.4)"
---
## 1. Gist
This paper addresses a gap in NLP bias research: nearly all social bias benchmarks and debiasing methods target English. Zhou and Lu construct a multilingual bias evaluation dataset covering English, Chinese, Russian, Indonesian, and Thai—spanning high-resource and low-resource languages—and introduce the Normalized Bias Score (NBS) to enable cross-model comparisons. They evaluate six multilingual language models and then test whether debiasing techniques trained on English data transfer across languages. The finding that bias patterns differ dramatically by language and script (with low-resource Thai showing the worst bias scores), and that subspace-projection debiasing (SenDeb) transfers cross-lingually, has direct implications for values-alignment benchmarking that aims to be globally inclusive rather than Anglocentric.

## 2. Benchmark/eval design features
The paper repurposes CrowS-Pairs (Nangia et al., 2020) as its base: a dataset of stereotypical vs. counter-stereotypical sentence pairs designed for masked-language-model evaluation. The original 1,508 English items were filtered to 1,042 items across four bias types—Gender, Race-Color, Nationality, Religion—chosen for cross-cultural generalizability. These items were machine-translated (Google Translate API) into Chinese, Russian, Indonesian, and Thai. The key technical contribution is the Normalized Bias Score (NBS), which normalizes per-model predictions by the average absolute probability magnitude so that bias scores are comparable across models with different internal probability scales. NBS = 0 means no bias; higher values indicate stronger stereotypical preference. The evaluation covers both encoder-only (mBERT, XLM-R) and autoregressive (XGLM, Gemma 3, Qwen 2.5, LLaMA 3) models, using log-probability approximations for CLM models.

## 3. Task format & example item
The benchmark format is forced-choice at inference: given a stereotypical sentence and its counter-stereotypical version, the model implicitly "chooses" via relative probability. There is no explicit user-facing prompt; the task is purely a probability comparison.

No verbatim example item is provided in the extract, but the methodology section illustrates the approach: given "Mr. Li is a university professor," the modified version is "Mrs. Li is a university professor," and the model's preference for one over the other is measured via pseudo-log-likelihood (p.3). This is a stereotypicality cloze test, not a user-facing MCQ.

## 4. Scoring / grading methodology
The NBS formula (p.3) normalizes the raw probability difference between stereotypical (s) and counter-stereotypical (s̄) sentences by the average absolute magnitude across languages:

NBS(θ) = 2n · Σ|PS(s) − PS(s̄)| / Σ|PS(s) + PS(s̄)|

where n = number of languages. NBS closer to 0 means less bias. For causal LMs that cannot predict masked tokens, the authors remove the token and use the language modeling head's prediction scores as a proxy rather than true pseudo-log-likelihood (p.3). Debiasing effectiveness is measured as percentage reduction: (NBS − NBS′)/NBS × 100% (p.7).

## 5. Dataset construction & provenance
Base: CrowS-Pairs (Nangia et al., 2020), 1,508 English items filtered to 1,042 covering Gender, Race-Color, Nationality, Religion. The filtering retained only items amenable to translation across cultures. Translation: Google Translate API into Chinese (ZHO), Russian (RUS), Indonesian (IND), Thai (THA). Languages were selected from Common Crawl statistics; Thai (0.41%) and Indonesian (0.86%) are classified as low-resource, Chinese (4.42%) and Russian (5.95%) as medium-resource, English (45.51%) as high-resource (p.4). The translated dataset is artificial and not natively authored in each language, which the authors acknowledge as a limitation. No explicit licensing statement is in the extract; the underlying CrowS-Pairs is publicly available.

## 6. Validity evidence
The authors note that despite the translation-based construction, "the experimental results still reveal meaningful patterns, demonstrating the value of the evaluation" (p.4). There is no human validation of the translations, no inter-rater reliability reported, and no psychometric factor analysis. The main validity argument is face validity: translated items preserve the semantic polarity of stereotypical versus counter-stereotypical content. The NBS metric is analytically justified as normalizing for scale differences across models, but no convergent validity against human judgments is established.

## 7. Saturation / discrimination
The bias scores vary enormously across models (mBERT Thai: 90.69 vs. LLaMA 3 Thai: 10.21), indicating strong discrimination between models (p.5). Within language, LLaMA 3 consistently approaches low bias, suggesting this end of the spectrum may be near saturation for the best aligned models. Thai shows the highest raw scores, suggesting that low-resource languages with distinct scripts are harder benchmark targets—there is still headroom for improvement even in the best models. The scoring range is continuous, so there are no artificial floor/ceiling effects in the metric design, but near-zero scores for LLaMA 3 in English suggest English bias detection may be near saturation.

## 8. Multiturn / agentic aspects
n/a. The evaluation is purely a single-sentence probability comparison with no conversation or tool use.

## 9. Key numbers
- Dataset: 1,042 stereotypical/counter-stereotypical pairs across 5 languages and 4 bias types (p.4)
- mBERT Thai average NBS: 90.69 (highest bias, any model/language) (p.5)
- LLaMA 3 English average NBS: 7.68 (lowest bias) (p.5)
- LLaMA 3 Thai average NBS: 10.21 (p.5)
- Qwen 2.5 Chinese average NBS: 26.40 (p.5)
- SenDeb English bias reduction: -22.42% (p.8)
- SenDeb Chinese bias reduction: -37.96% (p.8)
- SenDeb Thai bias reduction: -34.33% (p.8)
- CDA English bias reduction: -12.69% (p.8)
- Debiasing conducted on 514,084 Wikipedia articles (10% sample) (p.7)

## 10. Pitfalls & limitations
- Translation-based dataset construction imports US-centric sociocultural norms into other languages; what counts as "stereotypical" in American English may be inappropriate for Chinese, Thai, or Indonesian contexts (p.9).
- Machine translation via Google Translate may miss culturally nuanced connotations; the authors acknowledge this and call for future natively constructed datasets (p.9).
- The NBS metric design (using CLM token removal rather than masking) is an approximation that may behave differently from true MLM scoring; no validation against human bias judgments (p.3).
- Qwen 2.5's "low" Thai bias score likely reflects lack of Thai comprehension rather than absence of bias—the model produces generic outputs that accidentally score as unbiased (p.4–5). This is a confound not fully addressed by the NBS metric.
- Only six models tested; no coverage of instruction-tuned or RLHF models other than LLaMA 3.
- Debiasing experiments only use XLM-RoBERTa; generalizability to other architectures unknown.
- No statistical significance testing reported.

## 11. Novel ideas worth stealing
- **Cross-model normalized bias score (NBS)**: normalizing by average probability magnitude allows fair comparison of bias across models with different scales. This idea is directly portable to any stereotypicality benchmark wanting to compare diverse model types.
- **Low-resource language as stress test**: explicitly including under-resourced scripts (Thai) as a hardest-case condition provides a discrimination gradient that separates well-aligned from poorly aligned models far better than English alone.
- **Cross-lingual debiasing transfer experiment design**: fine-tuning a debiasing method only on English data and measuring its effect in four other languages tests generalization in a way that is both cheap and informative. This design is reusable for any values-alignment benchmark concerned with multilingual consistency.
- **Bias subspace sharing hypothesis**: SenDeb's superior cross-lingual transfer is interpreted through the lens of shared multilingual representation spaces. This motivates designing alignment evals that test whether value-consistent behavior in one language transfers to others, without retraining.
- **Four generalizable bias dimensions**: Gender, Race-Color, Nationality, Religion were chosen specifically for cross-cultural applicability—a principled filtering criterion for what goes into a multilingual values benchmark.

## 12. Notable quotes
- "Most NLP research overlooks thousands of languages spoken by billions of people." (p.1)
- "Model performance in a given language does not always correlate with its bias score; in some cases, higher performance is associated with stronger biases, while models with poor language support may produce low bias scores simply due to unintelligible or generic outputs." (p.6)
- "SenDeb emerged as the most effective technique, suggesting that bias subspaces may share cross-linguistic properties, enabling cross-language debiasing." (p.8)
- "Our bias evaluation dataset was constructed through translation, using English—specifically American English—as the cultural and linguistic base… it risks importing U.S.-centric social norms into other languages." (p.9)

## 13. UNKNOWN / not in extract
- Licensing status of the translated dataset beyond the base CrowS-Pairs license
- Whether native speakers or cultural experts validated any of the translated items
- Statistical significance (p-values, confidence intervals) for any bias score comparisons
- Whether any items were excluded during translation due to untranslatability
- Performance of debiasing on models other than XLM-RoBERTa
- The exact NBS score for English in each debiased variant (only reduction percentage given)
