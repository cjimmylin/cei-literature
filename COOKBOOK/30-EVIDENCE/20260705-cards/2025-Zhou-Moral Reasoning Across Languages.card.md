---
stem: "2025-Zhou-Moral Reasoning Across Languages"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, moral-psychology, contamination-robustness, normative-ethics]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 2170
dataset_construction: "mixed"
languages: [en, zh, ru, vi, id]
models_tested: [GPT-4, GPT-3.5, Llama3-70B-Instruct, Llama3-8B-Instruct, Mixtral-8x7B-Instruct-v0.1]
headline_numbers: ["2,170 moral scenarios across 5 languages and 3 complexity levels (p.1)", "GPT-4 ETHICSBASE English 96.5% vs Vietnamese 86.7% (p.3)", "Indonesian fine-tuning gave largest cross-lingual alignment gains (up to +27.1 on VI) (p.3)", "Vietnamese poisoning caused largest multilingual degradation (up to -28.7) (p.3)"]
---
## 1. Gist
The Multilingual Moral Reasoning Benchmark (MMRB) evaluates LLM moral reasoning across five typologically diverse languages (English, Chinese, Russian, Vietnamese, Indonesian) and three levels of contextual complexity (sentence, paragraph, document). It repurposes ETHICS-style datasets, translating them and layering complexity, then measures consistency across languages. The headline finding for values-alignment: moral judgments are not consistent across languages, high-resource languages generally score higher, and — surprisingly — fine-tuning on low-resource languages (Indonesian, Vietnamese) has a disproportionately strong effect on multilingual moral reasoning, both for good (alignment) and ill (poisoning). It matters because it shows monolingual (English) benchmarks overstate a model's cross-cultural moral robustness and that data quality in under-resourced languages is a leverage point.

## 2. Benchmark/eval design features
Three nested datasets: (1) ETHICSBASE — sentence-level binary classification over five moral dimensions (commonsense, justice, etc.); (2) ETHICSPRO — paragraph-level, enhanced from BASE via LLM-generated moral reasoning with richer implicit ethical cues; (3) ETHICSMAX — document-level structured moral dilemmas, each with three ethical branches (Virtue, Deontological, Consequentialist), six normative principles, and three answer choices (p.2). Constructs: cross-lingual consistency and context-complexity robustness of moral judgment. Total 2,170 high-quality scenarios.

## 3. Task format & example item
MCQ / classification. ETHICSBASE is sentence-level binary moral classification; ETHICSMAX presents a moral dilemma with three normative branches and three answer choices each. No fully verbatim item text appears in the extract (only structural description, p.2). "n/a" for exact verbatim wording.

## 4. Scoring / grading methodology
Accuracy (exact match to gold labels), reported as per-language and averaged. Inference uses greedy decoding (temperature = 0) for determinism (p.2). Statistical significance of cross-language differences assessed via Mann-Whitney U tests; pairwise win-rate analysis also used (p.3-4). Fine-tuning effects reported as signed accuracy deltas.

## 5. Dataset construction & provenance
Built from ETHICS (Hendrycks 2020), ETHICSPRO (Ma 2023), and curated ETHICSMAX from Moral Stories (Scherrer 2024) + moral-dilemma framework (Rao 2023b). Initial translation via DeepSeek API, then manual verification by bilingual annotators; cross-validation with Google Translate to catch inconsistencies/cultural mismatches; ambiguous scenarios filtered out (p.2). Result: 2,170 scenarios. Anonymized code repo referenced (anonymous.4open.science). Fine-tuning via LLaMA-Factory with QLoRA-style monolingual alignment and label-corrupted "poisoning" settings on LLaMA3-8B.

## 6. Validity evidence
Cross-lingual consistency probed with Mann-Whitney U tests (most cross-language comparisons fail to reach significance, indicating inconsistency, p.3). Three ethical branches (Table 2) follow similar trends across models, offering internal consistency. Human baseline absent. Translation quality controlled by dual-tool cross-validation + bilingual annotators but no inter-annotator agreement statistic reported.

## 7. Saturation / discrimination
Good spread. English ETHICSBASE 86.48–96.49% vs Vietnamese 54.25–86.71% (p.3). Non-monotonic difficulty: performance drops from sentence (BASE) to paragraph (PRO) then recovers at document (MAX) because explicit moral principles in long context aid models (p.3). Low-resource languages (VI, ID) show the largest headroom and volatility, especially for smaller models (Mixtral ETHICSMAX-VI 27.6%, p.3).

## 8. Multiturn / agentic aspects
n/a — single-turn classification, no interaction or tools.

## 9. Key numbers
- 2,170 scenarios, 5 languages, 3 complexity levels (p.1).
- ETHICSBASE avg accuracy: GPT-4 90.6, Llama3-70B 83.7, Mixtral 80.4, GPT-3.5 76.6, Llama3-8B 74.5 (p.3).
- ETHICSBASE English GPT-4 96.5 vs Vietnamese 86.7; Llama3-8B EN 88.3 vs VI 65.2 (p.3).
- ETHICSMAX-VI Mixtral collapses to 27.6 (p.3).
- Monolingual alignment: Indonesian FT lifts VI +27.1, ID self +21.2 on ETHICSBASE (p.3).
- Monolingual poisoning: Vietnamese FT drops ETHICSPRO-VI -18.70 and ETHICSPRO-ID -28.70 (p.3).

## 10. Pitfalls & limitations
Author-admitted: potential translation inaccuracies, model-specific variability, moral scenarios may not capture real-world complexity (p.5). Reviewer-visible: paragraph-level ETHICSPRO is itself LLM-generated (ChatGPT), risking style/label contamination and circularity when LLMs are evaluated; no human moral baseline to anchor "correct" answers; gold labels for translated dilemmas assume the English normative answer transfers cross-culturally, which conflates translation error with genuine cultural moral divergence; small model set (5); no inter-annotator agreement reported.

## 11. Novel ideas worth stealing
- **Three-tier complexity ladder (sentence → paragraph → document)** from the same underlying moral content — cleanly isolates context-load effects and reveals the non-monotone dip-then-recover curve; reusable to probe whether a values benchmark's difficulty comes from ambiguity or from missing explicit principles.
- **Structured branch encoding**: each MAX dilemma tagged with Virtue/Deontological/Consequentialist branches + six normative principles + three choices — lets you score which normative framework a model defaults to, not just right/wrong.
- **Low-resource-language leverage**: deliberately measuring alignment/poisoning transfer FROM low-resource languages exposes an under-appreciated attack/robustness surface; a values benchmark should include low-resource languages precisely because they move the needle most.
- **Dual-tool translation QA** (DeepSeek + Google Translate cross-check + bilingual verify) as a cheap multilingual data-quality control.
- **Win-rate matrix across languages** as a consistency metric beyond raw accuracy.

## 12. Notable quotes
- "Even state-of-the-art models such as the GPT series do not produce consistent moral judgments across languages." (p.3)
- "low-resource languages have a stronger impact on multilingual reasoning than high-resource ones, highlighting their critical role" (p.1).
- "performance improves again on ETHICSMAX (document-level), likely because longer contexts include explicit moral principles that help guide the model's decisions" (p.3).
- "harmful data in these languages is less diluted during pretraining" (p.4).

## 13. UNKNOWN / not in extract
Verbatim item wording; exact per-dimension counts within ETHICSBASE; licensing of MMRB; inter-annotator agreement statistics; number of bilingual annotators; how gold labels were adjudicated for cross-cultural cases; whether the benchmark is peer-reviewed vs preprint (arXiv 2504.19759); exact size split across the three complexity tiers.
