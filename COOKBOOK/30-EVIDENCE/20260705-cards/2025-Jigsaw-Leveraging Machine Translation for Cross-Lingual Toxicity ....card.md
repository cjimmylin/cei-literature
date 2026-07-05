---
stem: "2025-Jigsaw-Leveraging Machine Translation for Cross-Lingual Toxicity ..."
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, llm-judges-scoring, best-practices, validity-psychometrics]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 120568
dataset_construction: "scraped"
languages: [am, ar, de, es, fr, he, hi, it, kn, ml, pt, ru, ta, te, th, tr, uk]
models_tested: ["Llama 3.1 8B Instruct", "Gemma 3 4B Instruct", "GPT-4o", "NLLB 200 3.3B", "BERT-based classifiers (toxic-bert, XLM-RoBERTa variants)"]
headline_numbers:
  - "translate-classify outperforms classify (OOD) in 81.3% of languages — 13 of 16 (p.5)"
  - "MT-SFT (+TowerBlocks/MT) achieves 100% TNR (no refusals) across all annotated examples in 5 languages (p.7)"
  - "Best translate-classify AUC for Amharic = 0.99; best OOD AUC for Amharic = 0.88 (p.15)"
  - "LLM judges underperform traditional classifiers in 6 of 7 low-resource languages (p.8)"
---
## 1. Gist
This paper from FAIR at Meta provides an empirical comparison of translation-based versus direct-classification pipelines for multilingual toxicity detection across 17 languages spanning multiple resource levels. It evaluates 27 pipeline variants combining five MT systems (including GPT-4o, Llama 3.1 8B Instruct, Gemma 3 4B, and NLLB) with nine toxicity classifiers. The central finding—that translate-then-classify beats out-of-distribution direct classification in 81% of cases—has direct implications for values-alignment benchmarking: any evaluator building a multilingual content-moderation or toxicity benchmark must decide whether to translate to English first or assess natively. The study also illuminates failure modes of LLM-as-judge for toxicity in low-resource languages, a concern directly relevant to scoring strategies in cross-lingual values benchmarks.

## 2. Benchmark/eval design features
The paper operationalizes four pipeline regimes: (1) classify ID — in-distribution finetuned classifier in the source language; (2) classify OOD — off-the-shelf classifier applied out-of-distribution; (3) translate-classify — MT → English classifier; (4) translate-judge / judge — LLM prompt for zero-shot toxicity label. Performance is measured by AUC (for classifiers) or accuracy (for LLM judges). Language resourcefulness is quantified via FineWeb-2 document counts. Translation quality is measured via COMETKiwi-DA-XL scores. The study thus provides a factorial design across MT system quality × language resource level × pipeline type, yielding interpretable interaction effects.

## 3. Task format & example item
The judge prompt used in the paper reads:
"You are a toxicity classifier. Classify the following text as toxic or not toxic. Respond with 'toxic' or 'not toxic' with no other comments or explanation. Text: {{ sample }} Classification:" (p.8)

The translation prompt reads:
"Translate the following sentence from {{lang}} into English. Respond only with the translation into English, without any additional comments. {{ sentence }}" (p.5)

## 4. Scoring / grading methodology
For classifiers: AUC (area under ROC curve) computed on test partitions; threshold-free metric avoids need for threshold tuning. For LLM judges: binary accuracy (toxic / not toxic label), since judge outputs are categorical rather than continuous scores. Comparisons use ∆AUC across pipeline pairs. Human annotation verified refusal predictions (TPR) and refusal mitigation (TNR) for 5% samples across 5 languages.

## 5. Dataset construction & provenance
Ten benchmarks spanning 17 languages, all using natural human-generated text with human-annotated gold labels. Criteria: permissive license, clear provenance, accessible online. Key datasets: Jigsaw Multilingual (es, fr, it, tr — up to 14,000 samples per language), MACD (hi, kn, ml, ta, te), ToLD-Br (pt, 21,000 samples), Russian Language Toxic Comments (ru, 14,412), TextDetox 2024 Ukrainian (5,000). Only test partitions used for evaluation. See Table 1 (p.3–4) for full dataset sizes. Total across all languages approximately 120,000+ samples.

## 6. Validity evidence
Translation quality (COMETKiwi-DA-XL) is validated against MT performance on BOUQuET dataset. Human annotations of refusal detection verify automated refusal classifier accuracy (TPR 100% for TH, DE, UK; slightly lower for ML and AR). The study uses the entire test partition of each dataset, not a subsample. Correlation analyses between language resource level (FineWeb-2 docs) and ∆AUC are provided graphically (Figures 4, 5) and shown to be consistent across four MT systems.

## 7. Saturation / discrimination
Results show very high AUC for well-resourced languages (Russian ID: 0.97; Turkish translated: 0.96) and poor performance on low-resource languages (Kannada OOD: 0.42; Malayalam OOD: 0.38). Hebrew shows near-chance AUC in both OOD and translated conditions (0.44), suggesting either poor MT or annotation noise. This ceiling/floor bifurcation means the benchmark effectively discriminates well for high-resource but not low-resource languages, which is itself a finding about the limits of current evaluation.

## 8. Multiturn / agentic aspects
n/a — this is a single-turn classification pipeline evaluation, not an interactive or agentic setup.

## 9. Key numbers
- translate-classify wins in 13/16 languages vs OOD baseline (p.5)
- With fixed classifier, still wins in 12/16 (p.5)
- translate-classify wins in 3/7 languages even vs ID-finetuned classifiers (p.5)
- ELECTRA-style: MT-SFT (TowerBlocks) improves AUC in 11/17 languages (p.7)
- MT-SFT reduces refusal in every language; Thai original Llama 3.1 refusal rate ~20%, drops to 0% (Figure 8, p.8)
- LLM judges dominate only at high resources; translate-classify wins in 6/7 low-resource languages vs translate-judge (p.8)
- Amharic translated AUC = 0.99 vs OOD = 0.88 (p.15, Table S1)
- Best Turkish translated AUC = 0.96 (p.15)

## 10. Pitfalls & limitations
- Cross-dataset comparison confounds domain differences (Twitter vs. WikiMedia) with language effects; authors acknowledge conclusions are indicative of trends, not per-language guarantees (p.10).
- No classifiers finetuned on translated text — the translate-classify advantage could be further improved.
- Evaluation queried Nov 1, 2023 (for MT systems), though classifiers are more recent; model generations may have shifted.
- Hebrew results near chance (AUC ~0.44) in both OOD and translated conditions — could reflect dataset quality or domain issues, not just language resource level.
- LLM judge comparison uses Llama 3.1 8B only, not GPT-4o in judge mode; the comparison may underestimate LLM judge potential.

## 11. Novel ideas worth stealing
1. **Translate-then-classify as a benchmark baseline**: For any cross-lingual values benchmark, translating to English and applying an English classifier is a defensible default that typically outperforms direct multilingual classification when native training data is absent. Benchmark designers should report translate-classify AUC alongside native results.
2. **Language resourcefulness as a moderator variable**: Report ∆AUC (or ∆accuracy) as a function of FineWeb-2 document count or similar proxy. This surfaces inequity in benchmark performance across resource levels explicitly, not just as an aggregate.
3. **Refusal-aware scoring**: When using LLMs as classifiers or judges on sensitive content (toxicity, hate speech, value violations), refusal rates must be measured and reported separately; they can skew apparent accuracy dramatically. MT-SFT is a tractable mitigation.
4. **Separating OOD vs. ID regimes**: Clearly distinguishing in-distribution (ID) from out-of-distribution (OOD) evaluation is essential for values benchmarks — most downstream uses will be OOD, so benchmark papers should lead with OOD numbers.
5. **AUC over accuracy for imbalanced toxicity labels**: AUC is threshold-free and handles class imbalance; benchmark papers reporting binary accuracy for toxicity tasks should also report AUC.

## 12. Notable quotes
- "Translation benefit is increased for higher resourced languages." (p.6, Figure 4 caption)
- "Unlike many other NLP tasks, an LLM judge demonstrates only a limited performance advantage on select higher-resourced languages when compared to traditional (e.g., BERT-based) classifiers." (p.10)
- "Toxic language is culturally and contextually grounded, with expressions, slurs, and taboos that often lack direct equivalents across languages, making transfer more brittle than for semantically simpler labels." (p.2)
- "We find that translation-based pipelines consistently outperform out-of-distribution classifiers in 81.3% of cases (13 of 16 languages), with translation benefits strongly correlated with both the resource level of the target language and the quality of the machine translation (MT) system." (p.1)

## 13. UNKNOWN / not in extract
- Exact statistical significance values for resource-level correlations (only graphical evidence in Figures 4–5).
- Details on annotation schema differences across the 10 benchmarks (only mentioned as a limitation).
- Runtime / cost comparisons across pipeline types.
- Results for Gemma 3 4B and GPT-4o in judge mode (only Llama 3.1 used as judge).
