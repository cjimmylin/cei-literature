---
stem: "2025-Yoo-Moral Judgment of LLM Using Korean Datasets and Eastern Ethical"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: true
theme_tags: [cultural-linguistic, moral-psychology, normative-ethics]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: null
dataset_construction: "scraped"
languages: ["ko", "en"]
models_tested: ["GPT-3.5-Turbo-0125", "GPT-4-0613"]
headline_numbers:
  - "GPT-3.5-Turbo: Heinz dilemma accuracy 100% in English, 60% in Korean (p.2)"
  - "GPT-4: Rajesh dilemma accuracy 60% in English, 100% in Korean (p.2)"
  - "Model size increase correlates with reduced ethical bias across languages (p.2)"
---
## 1. Gist
This is a 2-page short paper (ASK 2025 conference proceedings, in Korean with an English abstract) from Incheon National University. It examines whether GPT-3.5-Turbo and GPT-4 exhibit different moral judgments when presented with moral dilemmas in English vs. Korean, and whether applying Eastern ethical frameworks (Confucian, Taoist, Buddhist) as system-level policies reduces bias differently than Western ethical frameworks (virtue ethics, deontology, consequentialism). The paper finds that moral judgments can shift with input language, that larger models show smaller language-induced bias, and that Eastern ethics policies sometimes reduce bias in Korean-language settings. Relevant to values-alignment benchmarking as a preliminary cross-lingual, cross-cultural ethics evaluation, though the paper is brief and details are limited.

## 2. Benchmark/eval design features
**Constructs measured**: Moral judgment consistency across language (English vs. Korean) and ethical policy (Western vs. Eastern frameworks). Bias operationalized as the tendency to maintain a default moral judgment even when a contrary ethical policy is applied.

**Items**: 4 moral dilemmas (Heinz, Monica, Rajesh, Timmy) drawn from Rao et al. (2023), translated to Korean using Google Translate. Each dilemma allows three responses: "should," "should not," "cannot decide."

**Experimental design**: 
- Baseline: 4 dilemmas × 6 option permutations × 5 repetitions per model.
- Policy experiments: same dilemmas with Western ethical policies (virtue ethics, deontology, consequentialism) or Eastern policies (Confucian, Taoist, Buddhist) prepended as system instructions. Bias measured as the proportion of responses that maintain the baseline preference when an opposing policy is applied.

## 3. Task format & example item
Forced-choice moral dilemma with three options (should / should not / cannot decide), presented in either English or Korean. The four dilemmas (Heinz, Monica, Rajesh, Timmy) are standard moral philosophy cases from Rao et al. (2023). No verbatim example items are reproduced in the extract; the paper references the source dataset. Experiments run via OpenAI API (Temperature=0, Top-P=0.95, Presence Penalty=1) (p.2).

## 4. Scoring / grading methodology
Baseline accuracy: proportion of responses matching a pre-identified "expected" answer across 5 repetitions × 6 permutations = 30 runs per dilemma per language. Bias metric: when the opposite ethical policy is applied, what proportion of responses still match the baseline preference (i.e., the model resists policy direction). Higher bias = less responsive to the ethical policy.

## 5. Dataset construction & provenance
Dilemmas from Rao et al. (2023) — "Ethical Reasoning over Moral Alignment: A Case and Framework for In-Context Ethical Policies in LLMs" (ACL EMNLP Findings 2023). Korean translations produced via Google Translate (same method as Agarwal et al., 2024). Dataset size and license not specified in the extract.

## 6. Validity evidence
Very limited: 2-page short paper with minimal methodological detail. No inter-rater reliability, no statistical tests reported, no discussion of whether Google Translate preserves moral nuance. The 4-dilemma set is small. Results are reported as percentage tables (Tables 1 and 2 referenced in text) but the actual heatmap for Table 2 is not extractable from the OCR.

## 7. Saturation / discrimination
With only 4 dilemmas, the benchmark has very limited coverage. The paper shows some dilemma-specific variability (GPT-3.5 performs differently on Heinz in Korean vs. GPT-4 on Rajesh in English), suggesting inter-dilemma variance that a larger set would be needed to characterize. Larger models (GPT-4) generally show lower language-induced bias than smaller ones (GPT-3.5).

## 8. Multiturn / agentic aspects
n/a — single-turn prompts only.

## 9. Key numbers
- 4 moral dilemmas: Heinz, Monica, Rajesh, Timmy (p.2)
- 5 repetitions × 6 permutations = 30 runs per dilemma per condition (p.2)
- GPT-3.5-Turbo Heinz: 100% (English), 60% (Korean) (p.2)
- GPT-4 Rajesh: 60% (English), 100% (Korean) (p.2)
- Temperature=0, Top-P=0.95, Presence Penalty=1 (p.2)
- Funded by IITP (IITP-2025-RS-2023-00260175) (p.2)

## 10. Pitfalls & limitations
- **Very short paper**: 2-page conference abstract with minimal methodological and results detail; findings cannot be fully evaluated.
- **Machine translation**: Korean dataset produced by Google Translate, which may introduce artifacts that confound language effects with translation quality effects.
- **Small dilemma set**: 4 scenarios is insufficient for robust conclusions about cross-lingual moral judgment.
- **Eastern ethics policies underspecified**: how Confucian, Taoist, and Buddhist ethics are formulated as system prompts is not described in the extract.
- **No statistical significance tests**: results reported as percentages without confidence intervals or tests.
- **Limited models**: only GPT-3.5-Turbo and GPT-4; results may not generalize to other model families or to Korean-native models.

## 11. Novel ideas worth stealing
- **Eastern ethics as system-level policy prompt**: prepending Confucian, Taoist, or Buddhist ethical frameworks as system instructions (alongside Western virtue ethics, deontology, consequentialism) is a concrete method for measuring whether a model's moral judgment shifts in culturally appropriate directions. Directly reusable in cross-cultural values-alignment benchmarks.
- **Bias operationalization via policy resistance**: measuring the proportion of responses that maintain a baseline preference even when an opposing ethical policy is explicitly applied is a clean operationalization of "moral rigidity" vs. "ethical responsiveness." This can be adapted as a sensitivity metric in any policy-conditioned moral evaluation.
- **Cross-lingual consistency as validity check**: running the same dilemmas in both a high-resource language (English) and a low-resource language (Korean) and checking for consistency is a simple method to detect language-induced moral drift in LLMs.
- **Permutation testing for robustness**: using 6 option permutations per dilemma guards against position bias in forced-choice tasks. This is a reusable robustness check for any MCQ-style moral benchmark.

## 12. Notable quotes
- "LLM의도덕적판단이입력언어에따라달라질수있음을시사한다." [The experimental results suggest that LLM moral judgments can vary depending on the input language.] (p.2)
- "Moral Judgment of LLM Using Korean Datasets and Eastern Ethical Principles" — title (p.1)
- "모델의크기가커질수록이러한편향성이점진적으로감소하는경향도관찰되었다." [A tendency was also observed that as the model size increases, this bias gradually decreases.] (p.2)

## 13. UNKNOWN / not in extract
- Full content of Table 2 (bias heatmap by ethical policy and language) — referenced but not extractable from OCR
- Exact wording of Eastern ethics policy prompts (Confucian, Taoist, Buddhist)
- Full dataset and dilemma texts
- Whether results replicate with other Korean-native or multilingual models
- Statistical significance of the observed differences
- Whether the 4 dilemma scenarios were balanced across moral domains
