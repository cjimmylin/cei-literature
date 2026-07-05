---
stem: "2024-Faysse-CroissantLLM A Truly Bilingual French-English Language Model"
reader_model: "opus"
confidence: "medium"
is_benchmark: true
theme_tags: [cultural-linguistic, contamination-robustness, ai-lab-practices, design-space]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: null
dataset_construction: "mixed"
languages: [en, fr]
models_tested: [CroissantLLM-1.3B, Bloom-1.7B, Bloom-3B, Llama-7B, Mistral-7B]
headline_numbers: ["Model 1.3B params, pretrained on ~3T tokens at 1:1 English:French ratio (p.1)", "303B-token curated French corpus released (p.2)", "Validates 81% of FMTI transparency criteria (p.1)", "Gutenberg canaries = 555M tokens, <0.04% of training tokens (p.6)", "FrenchBench: novel French benchmark spanning generation + multiple-choice tasks (p.12)"]
---
## 1. Gist
CroissantLLM is a 1.3B-parameter *intrinsically bilingual* French-English LLM trained on ~3T tokens at a deliberate 1:1 English:French ratio with a bilingualism-optimized tokenizer, released with full training data, checkpoints, and code. Its relevance to values-alignment benchmarking is twofold: (1) it introduces **FrenchBench**, a novel French-language evaluation suite spanning generation, multiple-choice reasoning/knowledge, linguistic proficiency, and a bespoke **French Trivia** cultural-knowledge task designed to detect whether bilingual pretraining instills *different cultural knowledge and biases* than English-centric models; and (2) it foregrounds transparency and contamination auditing (Gutenberg "canaries" seeded to measure memorization; FMTI transparency scoring). The paper's core alignment-relevant claim is that language-balanced pretraining reduces Anglocentric cultural bias and equips models with genuinely non-English cultural knowledge — a data-side lever for cultural-linguistic pluralism.
## 2. Benchmark/eval design features
FrenchBench (p.12) has three arms. **FrenchBench Gen** (few-shot generative, ROUGE-1 scored): FQuAD question-answering variants (FQuADGenQ question generation, FquadGenAns answer generation, MultiFQuAD multi-span), OrangeSum summarization (title + abstract). **FrenchBench Multiple Choice** (likelihood-based): French Language Test (fr-grammar, fr-vocabulary), French HellaSwag and Arc-C (GPT-3.5 machine translations), assessing reasoning, factual knowledge, linguistic capability, and model biases. **French Trivia** (p.12): short-answer questions about French culture, deliberately phrased in English to isolate latent cultural *knowledge* from language ability. Plus MT-Bench French (human-adapted), WMT/FLORES/TICO translation, and Belebele reading comprehension. The bias/culture construct is operationalized through the trivia knowledge gap between bilingual and English-centric models.
## 3. Task format & example item
French Trivia example implied (p.19 footnote): prompted "Which French club won the UEFA Champions League?" the model answers "Paris Saint-[Germain]". MMLU-format MC items give answers prefixed A/B/C/D and the model predicts the correct letter; HellaSwag-format items require choosing the most likely continuation without seeing other options (p.13). Verbatim full items not reproduced in extract beyond these fragments.
## 4. Scoring / grading methodology
Mixed: ROUGE-1 for generative tasks (title/question/answer generation, summarization); likelihood-based selection (highest-likelihood completion) for multiple choice; BLEU (sacreBLEU) + COMET for translation; MT-Bench French uses GPT-4-as-judge over two turns. For French Trivia, ROUGE-1 primary metric, cross-checked with GPT-4-as-judge to confirm ROUGE-1 suitability given short closed answers (p.16). Transparency scored against the 100-criterion FMTI framework.
## 5. Dataset construction & provenance
Training corpus: 303B-token curated French split (web via CulturaX/Oscar/mC4, legal/administrative OpenData 5.3B, cultural — all French Gutenberg, BnF manuscripts, poetry, podcasts, OpenSubtitles 41.8M, Wikisource 2.7B; encyclopedia Wikipedia 2B; industrial PDFs 191M), English from SlimPajama (copyrighted docs removed, Gutenberg substituted), 140B code tokens (StarCoder/The Stack), 36B parallel EN-FR tokens (OPUS). All under permissive commercial licenses (p.4–7). FrenchBench draws on existing datasets (FQuAD, OrangeSum, Belebele) plus newly released annotated data (French Language Test, French Trivia, MultiFQuAD eval set under CC-BY-NC-SA 4.0). French HellaSwag/Arc-C are GPT-3.5 machine translations (author-acknowledged imperfect, p.13).
## 6. Validity evidence
MT-Bench French questions underwent "rigorous human review and adaption to guarantee authentic wording… and to account for cultural discrepancies" (p.13). French Trivia validated by cross-scoring ROUGE-1 against GPT-4 judge (p.16). Transparency independently framed via FMTI (81% criteria). Manual verification of French web-data language tagging and country representation. Limited formal psychometric validity (no reliability coefficients, no factor analysis) — this is a model paper, not a validation study.
## 7. Saturation / discrimination
CroissantLLM-1.3B reported "top-of-its-class" below 7B, edging out Bloom-3B on most tasks, but "All models remain far off from the performance of the strong 7B Llama and Mistral models" (p.16) — i.e. clear headroom above the 1.3B class. On French Trivia the bilingual model beats English-centric sub-7B models "by significant margins," giving the cultural-knowledge task real discriminative power (p.16). Machine-translated HellaSwag/Arc-C are "far from perfect but sufficient… as a correct performance proxy" (p.13), limiting their discrimination.
## 8. Multiturn / agentic aspects
Limited: MT-Bench French evaluates two conversational turns via GPT-4 judge (p.16); otherwise single-shot few-shot tasks. No tool use or agentic environment.
## 9. Key numbers
- 1.3B params; ~3T (2988B) training tokens; 1:1 EN:FR ratio (p.1, Table 1 p.4)
- French corpus 303B tokens; total data mix 2988.35B tokens including 288.92B code, 219.26B parallel (Table 1, p.4)
- Largest model trained at 2300:1 token-to-parameter ratio, ~115× Chinchilla-optimal (p.3)
- Gutenberg canaries: 555M tokens, <0.04% of training tokens (p.6)
- FMTI transparency: 81% of criteria validated (p.1)
- OpenSubtitles 41.8M tokens; French Wikipedia >2.5M articles / >2B tokens; parallel data 400M sentence pairs / ~36B tokens (p.5–6)
- Belebele released across 122 languages; EN + FR splits used (p.13)
## 10. Pitfalls & limitations
Author-admitted: French HellaSwag/Arc-C are imperfect GPT-3.5 translations used only as "performance proxy" (p.13); heuristic metrics (ROUGE) may miss answer diversity, mitigated with GPT-4 judge (p.16). Observed flaws for values-benchmarking use: FrenchBench mixes translated and native tasks unevenly; the "cultural bias reduction" claim rests largely on a single Trivia knowledge task (knowledge ≠ bias/values); only two languages and one Western-European culture, so "cultural pluralism" is narrow; no reliability/inter-annotator statistics for the newly authored sets; French Trivia questions are France-focused and English-phrased, conflating knowledge, retrieval, and language. Contamination is actively managed for canaries but FrenchBench's reuse of public datasets (FQuAD, HellaSwag) risks train-test overlap in baselines.
## 11. Novel ideas worth stealing
- **Cultural-knowledge probe phrased in a neutral/second language**: French Trivia asks France-culture questions *in English* to disentangle latent cultural *knowledge* from language *fluency* — a clean design for isolating whether a model "knows" a culture vs. merely speaks its language. Reusable for any culture/values-knowledge benchmark.
- **Seeded "canaries" for contamination/memorization auditing**: intentionally inject modified/repeated samples (555M tokens, <0.04%) to later measure worst-case memorization — a proactive contamination-robustness instrument that a values benchmark could adopt to detect leakage.
- **Language-balanced (1:1) pretraining as a bias-reduction lever**, empirically motivated by scaling-law experiments, framing cultural alignment as a data-mix decision rather than post-hoc RLHF.
- **Format-sensitivity study (MMLU-letter vs. HellaSwag-continuation)**: showing smaller models score better under continuation formatting — a validity caution that item *format*, not just content, drives measured "capability."
- **Full transparency scoring via FMTI + released per-step training data** — enabling contamination and provenance audits others can reproduce.
- **Dual-metric scoring (ROUGE + GPT-4 judge cross-check)** to validate cheap automatic metrics on short-answer cultural tasks.
## 12. Notable quotes
"we craft a novel benchmark, FrenchBench, consisting of an array of classification and generation tasks, covering various orthogonal aspects of model performance in the French Language." (p.1)
"The French Trivia dataset is built from online trivia questions pertaining to French culture… Intentionally, questions are formulated in English for comparison with monolingual English models." (p.12)
"whether training on bilingual data goes beyond augmenting the language understanding… but also equips the models with novel knowledge and different cultural biases." (p.16)
"we stress test the model by including 'canaries'… that will enable a posteriori evaluation of the model capacity to memorize data in a 'worse than worst-case' situation." (p.6)
## 13. UNKNOWN / not in extract
- Exact item counts for FrenchBench subtasks (French Trivia, French Language Test sizes not stated in extract).
- Full quantitative benchmark result tables (Tables 4–5 values not in read portion).
- Precise number of models compared and their full configurations.
- Whether French Trivia/French Language Test underwent inter-annotator reliability checks.
- Detailed canary memorization results (stated to be published separately).
