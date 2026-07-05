---
stem: "2025-Mahran-Mechanistic Interpretability with SAEs Probing Religion"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [religious-values, validity-psychometrics, design-space, normative-ethics]
task_format: "n/a"
scoring_type: "behavioral"
dataset_size: null
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-2 Small", "Gemma-2-2B", "Gemma-2-9B", "Gemma-2-9B-IT", "Llama3.1-8B"]
headline_numbers:
  - "Islam consistently registers the highest Violence Association Index (VAI) across all five models tested (p.4)"
  - "Islam VAI = 117 in Gemma-2-2b; other religions range 94–96 (p.4)"
  - "Islam crime-text percentage = 3.46% in Gemma-2-9b-IT vs. 2.44% for Christianity (p.5)"
  - "Total unique features across religions ranged 18 to 145 across models (p.4)"
  - "Five models analyzed; 20 top-activating features stored per prompt per model (p.3)"
---
## 1. Gist
Simbeck and Mahran (HTW Berlin, AIES/EQITAS 2025 workshop paper) use mechanistic interpretability via Sparse Autoencoders (SAEs) to probe how five major world religions are internally represented inside LLMs, specifically whether religious concepts co-activate with violence-related features. Rather than studying model outputs, they query the Neuronpedia API to retrieve the top-20 latent features activated by religion-related prompts for five model families (GPT-2 Small, Gemma-2-2B, Gemma-2-9B, Gemma-2-9B-IT, Llama3.1-8B). They measure intra-group coherence (how consistently same-religion prompts activate shared features) and inter-group overlap with violence prompts, plus semantic analysis of activation texts for crime and geographic terms. The paper matters for values-alignment benchmarking because it demonstrates a methodology for auditing not just model outputs but the internal representational structures that shape them — directly relevant to designing benchmarks that probe religious-values sensitivity at the mechanistic level.

## 2. Benchmark/eval design features
This is not a benchmark paper but an interpretability audit methodology paper. Core constructs: (1) intra-group latent feature overlap — how compactly each religion is encoded; (2) inter-group overlap with violence prompts — whether religious feature sets share neurons with violence/terrorism features; (3) crime-term density in activation texts; (4) geographic association patterns. The Violence Association Index (VAI) is a normalized metric: raw overlap between a religion's feature set and violence-related features, divided by the model's mean overlap across all five religions, multiplied by 100. VAI > 100 indicates stronger-than-average violence association within that model. Key finding: Islam consistently scores highest on VAI (117 in Gemma-2-2b vs. 94–96 for other religions), a pattern that holds across all five models but with variation in which non-Islamic religion ranks second.

## 3. Task format & example item
Prompts are constructed as minimal declarative sentences: "This is the Quran," "This is a church," "This is a mosque." (p.3, Appendix A). Each keyword from religion-specific lists is wrapped in this fixed template. Example Islam terms: burka, hijab, mosque, muslim, quran, allah, halal, islam, mecca, imam, ramadan, eid, hajj. Violence/bias prompts: "terrorist," "militant," "radical," "extremist," "attack," "bombing," "bomb," "gun," "weapon," "terror attack," "massacre," "shooting." (p.10). These are submitted to the Neuronpedia API, not to the LLM directly for response generation.

## 4. Scoring / grading methodology
No human ratings. Scoring is automatic:
- Intra-group overlap: discrete count of shared latent feature IDs across prompts within the same religion category.
- Inter-group overlap (VAI): count of shared features between a religion's feature set and the violence prompt feature set, normalized by within-model mean across religions.
- Crime-text percentage: keyword-based search over activation text returns; matches normalized as a percentage of all activation texts per religion per model.
- Geographic association: keyword count per region category per religion across activation texts.
Initial attempt at cosine similarity over binary feature vectors was abandoned due to extreme sparsity (p.3).

## 5. Dataset construction & provenance
Data collected via Neuronpedia API (https://www.neuronpedia.org), which provides pre-trained SAEs for GPT-2 Small (res-jb, att-kk), Gemma-2-2B (gemmascope variants), Gemma-2-9B, Gemma-2-9B-IT, and Llama3.1-8B (llamascope-res-32k). SAEs were trained on OpenWebText (GPT-2), Pile-Uncopyrighted (Gemma variants), and SlimPajama (Llama). Number of features per SAE ranged from 16,384 to 131,072. Per model, top-20 activating features were retrieved per query; for each feature, activation texts were returned. Code and data available at https://github.com/iug-htw/SAE_fairness. The paper does not report total number of activation texts; Table 3 shows per-religion text counts ranging from ~7,253 to ~23,695 per model.

## 6. Validity evidence
Construct validity: the finding that Islam consistently shows the highest VAI across all five architecturally diverse models provides convergent evidence. The pattern in crime-text percentages is consistent with the latent-feature overlap finding, supporting the claim that the two measurement approaches capture the same underlying phenomenon. However, no human validation of feature content is reported beyond relying on Neuronpedia's SAE-derived feature explanations. The paper acknowledges model-level variation (e.g., Hinduism shows highest crime rates in GPT-2 Small and Llama3.1-8B rather than Islam), which the authors attribute to training data composition — this is interpretable but not formally verified.

## 7. Saturation / discrimination
Intra-group overlap scores show that all five religions are represented with similar structural cohesion within each model, which is the intended baseline finding (no strong differentiation at the representational-consistency level). Discrimination between religions is primarily on the inter-group (violence) dimension. The VAI values are relatively modest (117 for Islam vs. 94–96 for others in Gemma-2-2b), suggesting the bias is real but not extreme in magnitude at the latent-feature level. No floor/ceiling analysis reported.

## 8. Multiturn / agentic aspects
n/a — probing is done via single prompts submitted to Neuronpedia API, not via direct model generation.

## 9. Key numbers
- 5 models analyzed across 7 SAE configurations (p.3, Table 1)
- 20 top-activating features stored per query per model (p.3)
- 5 religions, each with 13 representative keywords (p.10, Table 4)
- Islam VAI: Gemma-2-2b = 117, Gemma-2-9b = 122, Gemma-2-9b-IT = 110, GPT2-small = 113, Llama3.1-8B = 109 (p.4, Table 2)
- Christianity VAI: 96, 94, 94, 94, 100 across same models (p.4, Table 2)
- Islam crime-text %: Gemma-2-2b = 2.02%, Gemma-2-9b = 2.98%, Gemma-2-9b-IT = 3.46%, GPT2-small = 6.88%, Llama3.1-8B = 3.23% (p.5, Table 3)
- All-religions combined intra-group overlap: Gemma-2-9b = 18 (most compact), GPT2-small = 145 (p.4)
- Crime keyword list contains 12 terms (p.9, Table 5)
- Geographic keyword list covers 7 regions (p.9–12, Table 5)

## 10. Pitfalls & limitations
- Analysis covers only five major world religions; indigenous, syncretic, or minority faiths excluded.
- Only English-language models and prompts analyzed; multilingual model behavior unexplored.
- Neuronpedia API feature explanations are themselves model-derived, potentially circular.
- Keyword lists for religious terms and crime terms are manually curated; coverage and cultural sensitivity not validated externally.
- The VAI methodology shows consistent relative ordering but the absolute magnitudes are close, making practical significance unclear.
- The paper does not address whether observed biases lead to differential downstream output harms (the link from internal representation to output behavior is posited but not demonstrated).
- GPT-2 Small is a very small, old model; mixing its results with larger models may conflate architecture effects with bias.
- Only one layer/position per model is analyzed (attention or residual stream at a specific layer); bias may manifest differently across layers.

## 11. Novel ideas worth stealing
1. **Violence Association Index (VAI)**: Normalize inter-group latent-feature overlap by within-model mean across categories before comparing across models. This solves the model-size confound when comparing raw overlap counts — a pattern directly reusable in any benchmark that compares bias across demographic or value groups using internal representations.
2. **Intra-group coherence as a validity baseline**: Before running bias analysis, first check that all groups are encoded with similar internal structural coherence (similar intra-group overlap). If one group's representation is highly diffuse, observed differences in inter-group analyses may be artifacts of representation quality, not bias. This is a principled validity pre-check for any representation-level audit.
3. **Template-controlled minimal probes**: Using a fixed declarative sentence frame ("This is a [X]") rather than standalone keywords reduces confounds from sentence-level context while maintaining minimal semantic load — a useful design principle for any probe study.
4. **Multi-model convergence as evidence**: The finding that Islam-violence associations persist across five architecturally and training-data-diverse models provides stronger evidence than any single-model finding. Designing evaluations to report results across multiple diverse model families should be a standard practice in values-alignment benchmarks.
5. **Semantic text analysis of activation contexts**: Going beyond the feature IDs to analyze the textual activation contexts (which real texts caused each SAE feature to fire) adds an interpretable layer that connects internal representations to concrete real-world associations.

## 12. Notable quotes
- "Stable representations make linked stereotypes more deeply embedded and harder to remove." (p.5)
- "LLMs do not merely learn language but also reproduce the narratives and frames prevalent in their training corpora." (p.5)
- "Downstream harms do not always stem from what models say, but from how they internally prioritize and structure information." (p.5)
- "What looks like a universal association may in fact be contingent on model class." (p.5)

## 13. UNKNOWN / not in extract
- Specific SAE layers (layer indices within the transformer) used for each model are not reported in the body; only attention vs. residual stream distinction is noted.
- Number of unique prompts submitted per religion (beyond the keyword count) is not clearly stated.
- Whether Neuronpedia API returns the same features deterministically (no stochasticity in feature retrieval) is not discussed.
- The paper was accepted for a workshop (AEQUITAS 2025 at ECAI); full peer review status is noted as "under peer review" for the att-kk SAE specifically.
- Mitigation strategies or debiasing experiments are not included (scoped to audit only).
