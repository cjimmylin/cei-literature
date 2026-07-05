---
stem: "2025-Galea-From Measurement to Mitigation Exploring the Transferability of"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, design-space]
task_format: "mixed"
scoring_type: "behavioral"
dataset_size: null
languages: [mt, en]
models_tested: [BERT, mBERT, BERTu, mBERTu]
headline_numbers: ["baseline CrowS: BERTu 55.40, mBERTu 51.20 (p.5)", "CDA best method: BERTu CrowS 55.40->49.19 (p.6)", "CDA dataset 411k sentences, 17.4% augmented (p.3)", "193 male-female word pairs in Maltese gender wordlist (p.4)", "25.5% of sampled CDA sentences had grammatical errors (p.4)"]
---
## 1. Gist
This paper studies whether English-developed gender-bias measurement and mitigation methods transfer to Maltese, a low-resource, morphologically rich, gendered Semitic-Romance EU language. The authors adapt two intrinsic bias benchmarks (CrowS-Pairs and SEAT, plus template-based probing) into Maltese and apply four debiasing methods (Counterfactual Data Augmentation, Dropout Regularization, Auto-Debias, GuiDebias) to two Maltese BERT models (monolingual BERTu, multilingual mBERTu), benchmarking against English BERT/mBERT. Relevance to values-alignment benchmarking: it is a careful case study in cross-lingual transfer of both bias metrics and mitigations, showing that methods effective in English degrade or invert in a gendered low-resource language, and that a single metric can mislead (CrowS and SEAT frequently disagree). It also contributes released Maltese evaluation datasets.

## 2. Benchmark/eval design features
Constructs: intrinsic binary-gender bias in masked language models. Three measurement instruments: (1) CrowS-Pairs (Maltese extension from Fort et al. 2024, 9 bias categories, minimal biased/less-biased sentence pairs); (2) SEAT (sentence-level WEAT extension; SEAT6a/6b/7a/7b/8a/8b translated to Maltese); (3) Sentence Template-Based Analysis probing MLMs with masked occupation slots (BEC-Pro, DisCo, RoBERTa templates). Answer space: model preference between paired sentences (CrowS), effect-size association (SEAT), ranked mask fill-ins (templates). Higher CrowS/SEAT = more bias; ideal CrowS ~50. Four mitigation methods evaluated by pre/post score deltas plus t-SNE embedding visualizations of gendered word pairs.

## 3. Task format & example item
Template probe (p.4): "[X] jaħdem bħala [MASK]" ("[X] works as a [MASK]"), male vs. female variant "[X] taħdem bħala [MASK]". Rankings on BERTu (Table 2, p.5): for [X]=Hu (he), top fills are tabib (doctor), għalliem (teacher), maxtrudaxxa (carpenter), avukat (lawyer), pijunier; for female [X]=Hi, top fills are pijuniera, għalliema, infermier(a) (nurse), segretarja (secretary), tabib. English vs. Maltese names (John/Ġanni, Jane/Ġovanna) contrasted to probe name-language interaction.

## 4. Scoring / grading methodology
Behavioral/intrinsic: CrowS-Pairs bias score = fraction of pairs where the model assigns higher (pseudo-)likelihood to the more-biased sentence (ideal 50). SEAT = effect-size association between target and attribute sentence sets (reported as Avg. SEAT; lower = less bias). Template analysis = qualitative inspection of top-ranked mask completions by gender/name. Mitigation effectiveness = change in CrowS and Avg. SEAT from baseline to debiased, supplemented by t-SNE proximity of gendered nouns (e.g., tabib/tabiba) to positive/negative adjectives. No downstream-task utility metric applied.

## 5. Dataset construction & provenance
CrowS-Pairs Maltese: from Fort et al. (2024) multilingual extension, native-speaker translated with cultural adaptation. SEAT + templates: machine-translated then manually corrected by native speakers (authors). CDA corpus: unseen FLORES+ sentences plus unseen Korpus Malti v4.2 subset = 411k sentences; 17.4% altered via a gender wordlist to swap gender; two-sided CDA (original + swapped) for balance. Gender wordlist: 193 Maltese male-female pairs, MT-translated from Zhao et al. (2018) then linguist-corrected (some pairs dropped for duplicate/absent translations). English CDA comparison: 30% of Wikipedia 2.5 dump (Meade et al. 2023), 18.3% augmented. GuiDebias Maltese "Maltese Debiasing Dataset" built via ChatGPT-4-generated short sentences + human check. All code/data public (github.com/MLRS/Malti-Bias). Fine-tuning: CDA 5 epochs, batch 16, lr 2e-5; GuiDebias batch 1024, lr 2e-5, 1 epoch.

## 6. Validity evidence
Cross-linguistic baseline comparison (English BERT/mBERT vs. Maltese BERTu/mBERTu) grounds interpretation. Convergent/discriminant signal via using multiple metrics (CrowS, SEAT, templates, t-SNE), and the paper explicitly documents CrowS-SEAT disagreements as a validity caution. No inter-annotator reliability reported (single-author adaptation for templates). t-SNE acknowledged as subjective. Effect direction (favoring male terms; female forms near "incompetent") is consistent across instruments, lending qualitative construct validity.

## 7. Saturation / discrimination
Scores discriminate: monolingual models (BERT 60.50, BERTu 55.40 CrowS) are more biased than multilingual (mBERT 52.53, mBERTu 51.20) (Table 1, p.5). Mitigation deltas are small and often contradictory across metrics—e.g., Dropout lowers BERTu CrowS but raises its SEAT (0.530->0.737, Table 5). CDA is the most consistent reducer (BERTu CrowS 55.40->49.19, SEAT 0.530->0.460, Table 4). Baseline mBERTu is already near the 50 ideal, leaving little headroom; substantial residual bias persists in BERTu even post-CDA per t-SNE. No ceiling in the classic sense—rather, mitigation methods fail to reliably move scores.

## 8. Multiturn / agentic aspects
n/a — intrinsic embedding/MLM probing; no interaction, agentic behavior, or generation task.

## 9. Key numbers
- Baselines CrowS / Avg SEAT: BERT 60.50/0.620, mBERT 52.53/1.030, BERTu 55.40/0.530, mBERTu 51.20/0.540 (Table 1, p.5)
- CDA: BERTu 55.40->49.19 CrowS, 0.530->0.460 SEAT; mBERTu 51.20->48.83, 0.540->0.462 (Table 4, p.6)
- Dropout best config h=0.2, a=0.15; BERTu SEAT rose 0.530->0.737 (Table 5, p.6)
- GuiDebias Maltese: BERTu CrowS rose 55.40->57.84 (MT data) (Table 6, p.6)
- CDA corpus 411k sentences, 17.4% augmented (p.3)
- 193 male-female Maltese word pairs (p.4); 25.5% of 200 sampled augmented sentences had grammatical errors (p.4)
- Kotek et al. cited: LLMs 3-6x more likely to associate occupations with stereotypical genders (p.1)

## 10. Pitfalls & limitations
Author-admitted: CDA constructs grammatically poor sentences in gendered languages (only swaps the noun, not agreeing verbs); manual correction infeasible at 411k scale; only CrowS-Pairs natively available for Maltese (SEAT hand-translated on a small subset); tested on a limited set of gendered word pairs; t-SNE is subjective; no downstream-utility evaluation; binary gender only (excludes non-binary/gender diversity despite motivating it). Observed flaws: MT-generated debiasing data left some English tokens in, plausibly corrupting GuiDebias results; small score deltas may be within noise (no significance tests / variance reported); ChatGPT-4-generated debiasing data risks importing its own biases.

## 11. Novel ideas worth stealing
- Cross-lingual transferability as the unit of study: test whether both the metric AND the mitigation survive translation to a typologically distant, gendered, low-resource language—a template for auditing whether "safety" techniques are English-only artifacts.
- Deliberate multi-metric triangulation (CrowS + SEAT + templates + t-SNE) with explicit documentation of when metrics disagree—directly reusable as a validity guardrail for any bias/values benchmark.
- English-name vs. native-name minimal contrasts (John/Ġanni, Jane/Ġovanna) to disentangle name-language effects from gender effects.
- Handling morphology-induced probe failures (adding definite article "il-" to force noun rather than verb-suffix completions)—a practical lesson for template design in morphologically rich languages.
- Documenting wordlist-adaptation attrition (pairs dropped for duplicate/missing translations) as a provenance artifact.
- Pairing quantitative scores with embedding-space visual diagnostics to reveal residual bias invisible to aggregate metrics.

## 12. Notable quotes
- "relying on a single metric fails to provide a comprehensive understanding of the biases present in a language model" (p.3)
- "CDA proved to be the most effective debiasing method, although grammatical issues arose due to Maltese morphology." (p.6-7)
- "GuiDebias did not generalise well to Maltese, increasing bias in both models." (p.8)
- "Bias mitigation in morphologically rich, low-resource languages like Maltese necessitates tailored approaches that strike a balance between bias reduction and linguistic integrity." (p.7)

## 13. UNKNOWN / not in extract
- Exact dataset sizes for the Maltese CrowS-Pairs and translated SEAT subsets (pair counts).
- Variance / significance testing for score deltas (none reported).
- Downstream-task impact of debiasing (NER, sentiment) — flagged as future work.
- Full per-template quantitative results (referred to repository).
- Precise dropout grid beyond the best config.
