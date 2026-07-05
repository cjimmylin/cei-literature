---
stem: "2024-Neplenbroek-MBBQ A Dataset for Cross-Lingual Comparison of Stereotypes in"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, saturation-discrimination, best-practices, validity-psychometrics]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 10072
dataset_construction: "mixed"
languages: [en, nl, es, tr]
models_tested: ["Aya", "Falcon-7b-instruct", "GPT-3.5 Turbo", "Llama 2-Chat 7b", "Mistral 7b", "WizardLM 7b", "Zephyr 7b"]
headline_numbers: ["MBBQ contains 98 templates / 10,072 samples across 6 bias categories in 4 languages (p.5)", "GPT-3.5 overall control accuracy 84.9% vs Falcon 16.2% (chance 33%) (p.8)", "Models generally most biased in Spanish, least biased in English or Turkish (p.9)", "Falcon detects an answer in only 0.3% of Turkish samples (p.7)"]
---
## 1. Gist
MBBQ (Multilingual Bias Benchmark for Question-answering) is a hand-checked translation of a curated subset of the English BBQ dataset into Dutch, Spanish, and Turkish, designed to measure whether the social stereotypes generative LLMs exhibit differ as a function of the prompt language — while controlling for cultural differences and task accuracy. It matters for values-alignment benchmarking because it isolates a specific validity threat: cross-lingual inconsistency in bias/safety behavior, which most bias benchmarks (English-only) cannot detect. Its key methodological contribution is a parallel *control* dataset that measures raw QA reasoning ability independent of bias, so that measured bias differences across languages can be attributed to biased behavior rather than to differing task competence.

## 2. Benchmark/eval design features
Constructs measured: implicit social stereotypes across 6 bias categories (age, disability status, gender identity, physical appearance, socio-economic status, sexual orientation) — race, religion, and nationality were deliberately excluded as too culturally divergent (p.5). Item structure: each sample has a context mentioning two individuals, a question, and three answer options (one per individual + an "unknown" option). Samples split equally between ambiguous contexts (correct answer = "unknown") and disambiguated contexts (correct answer determinable), the latter further split into biased vs counter-biased contexts (p.4). Only stereotypes judged by native speakers to be held in all four languages/cultures were retained, so cross-lingual differences reflect model inconsistency, not culture.

## 3. Task format & example item
MCQ (three options). Verbatim from Figure 1 caption (p.7): "Example from the Gender identity category in English and Spanish, plus the control-MBBQ counterpart of the English sample. In ambiguous contexts, the correct answer is always the 'unknown' answer. In biased contexts, the correct answer to this question is the biased answer, and in counter-biased contexts this is the counter-biased answer." (Full item text is in the figure image, not the OCR.)

## 4. Scoring / grading methodology
Rule-based exact-match answer extraction from free-form generations, relying on phrases like "the answer to the question is ..." (translated + native-speaker-verified per language). When a model matches the wrong letter to its answer text, the answer text is prioritized; refusals/inability-to-answer are treated as the "unknown" option; undetectable answers count as incorrect (p.6). Bias metrics follow Jin et al. (2024): BiasA for ambiguous contexts = (#biased − #counter-biased answers)/#ambiguous contexts; BiasD for disambiguated = accuracy difference between pro- and counter-stereotype contexts (Eqs. 1–2, p.7). All results averaged over 5 prompts. Significance via Kruskal–Wallis H test (p.7).

## 5. Dataset construction & provenance
Source: English BBQ (Parrish et al. 2022; 58,492 samples, 9 categories). Curation: exclude race/religion/nationality; drop proper-name templates; replace US-specific names/terms with international equivalents; native speakers of Dutch, European Spanish, Turkish verify which remaining stereotypes hold in all languages (p.5). Translation: Google Translate + NLLB-200 machine translations, then native-speaker hand-checking/rewriting (p.5). Final: 98 templates / 10,072 samples (Table 1, p.5). Control set (control-MBBQ) built by replacing the two group-referencing individuals with two same-gender first names from top-30 baby names of 2022 per language; same size, gender-balanced (p.6). Publicly released (dataset + code) at github.com/Veranep/MBBQ, stated for evaluation only.

## 6. Validity evidence
Central validity move: the control set verifies models possess the reasoning ability to answer BBQ-style questions absent stereotypes, so bias is not confounded with incompetence (p.6). Bias analysis restricted to templates where each model scores above chance in disambiguated contexts in all languages (p.8). Native-speaker validation of both stereotype relevance and translations. Bias scores mathematically bounded by accuracy (a perfectly accurate model shows zero bias, p.6). Significance testing (Kruskal–Wallis) for cross-model and cross-language differences.

## 7. Saturation / discrimination
Strong discrimination across models: control accuracy ranges 84.9% (GPT-3.5) down to 16.2% (Falcon, below chance) (Table 2, p.8). Falcon and Wizard excluded from bias analysis for being at/below chance (p.8). The two most accurate models (Aya, GPT-3.5) are highly accurate and near-unbiased in disambiguated contexts, leaving "very little room for bias" — a ceiling that limits bias measurement for strong models (p.9). Ambiguous contexts yield higher bias scores and better discriminate. Bias scores are small in absolute terms (mostly <0.13), so headroom/signal is modest.

## 8. Multiturn / agentic aspects
n/a — single-turn multiple-choice prompting only.

## 9. Key numbers
- 98 templates / 10,072 samples across 6 categories, 4 languages (Table 1, p.5).
- English BBQ source: 58,492 samples, 9 categories (p.4).
- Control accuracy overall: GPT-3.5 84.9±5.06, Mistral 69.8, Aya 54.2, Zephyr 52.6, Llama 37.7, Wizard 34.6, Falcon 16.2 (chance 33%) (Table 2, p.8).
- Aya ambiguous-context accuracy only 18.0% vs 90.5% disambiguated — strong bias to pick an individual over "unknown" (Table 2, p.8).
- Falcon answer-detection: 88.3% English, <40% other languages, 0.3% Turkish (p.7).
- 5 prompts averaged per result (p.6); 7 LLMs evaluated (p.6).
- Zephyr ambiguous BiasA up to 0.1302 in Spanish (Table 3, p.10).

## 10. Pitfalls & limitations
Author-admitted: MBBQ is a non-exhaustive stereotype set and excludes language/culture-specific stereotypes by design, so a low bias score is no guarantee of unbiased behavior in other settings (p.10). Limited to the QA setting. My observations: absolute bias scores are very small, raising questions about effect-size interpretability; the 4 languages are all European-adjacent (WEIRD-leaning) except Turkish; rule-based answer extraction may systematically disadvantage low-resource-language generations (cf. Falcon Turkish 0.3%), conflating extraction failure with incorrectness; ceiling effect means the benchmark cannot measure bias in the strongest, most accurate models.

## 11. Novel ideas worth stealing
- **Parallel control set that neutralizes the construct**: swap the sensitive group references for neutral first names to measure raw task competence, then only interpret bias where competence is established. Directly transferable to any values benchmark to separate "wrong because misaligned" from "wrong because incapable."
- **Cross-lingual common-denominator design**: retain only items whose underlying value/stereotype holds across all target cultures, so cross-language score differences isolate *model inconsistency* rather than cultural variance — a clean way to test alignment stability across languages.
- **Accuracy-bounded bias metric**: tie the bias metric to accuracy so a perfect model is provably unbiased, preventing "high bias" artifacts from low-competence models.
- **Per-category reporting mandate**: authors show category-level bias varies within a model/language and recommend never reporting a single aggregate bias number.
- **Ambiguous-vs-disambiguated split** as a difficulty/behavior lever: ambiguous items reveal whether a model defaults to stereotypes when information is absent.
- **Answer-text-over-letter priority** in extraction to handle models that mislabel their own choice.

## 12. Notable quotes
"only if models show similar task performance across languages can we attribute measured differences in bias scores to biased model behavior" (p.4)
"we recommend evaluating model bias across different bias categories, rather than reporting on the bias of a model as a whole, and separating measurements of model bias from their performance, especially cross-lingually" (p.10)
"A low bias score does not mean that the model is completely free of biases, and is no guarantee that it will not display biased behavior in other settings." (p.11)
"models are generally most biased in Spanish, and least biased in English or Turkish" (p.2)

## 13. UNKNOWN / not in extract
- Exact verbatim text of the Figure 1 example item (embedded in image, not OCR).
- Licensing terms of the released dataset (only "for evaluation only" stated).
- Full per-language accuracy tables (Appendix D, Table 5) not in read pages.
- Exact prompt texts (Appendix C) not read.
- Inter-annotator agreement figures for native-speaker stereotype/translation validation (not reported in read pages).
