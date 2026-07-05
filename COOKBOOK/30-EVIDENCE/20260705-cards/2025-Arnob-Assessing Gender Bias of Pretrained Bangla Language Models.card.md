---
stem: "2025-Arnob-Assessing Gender Bias of Pretrained Bangla Language Models"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, validity-psychometrics, saturation-discrimination]
task_format: "n/a"
scoring_type: "mixed"
dataset_size: 237
dataset_construction: "hand-authored"
languages: ["bn"]
models_tested: ["csebuetnlp/banglabert", "saiful9379/Bangla_GPT2", "flax-community/gpt2-bengali", "ritog/bangla-gpt2", "csebuetnlp/banglat5", "neuropark/sahajBERT", "Kowsher/bangla-bert", "csebuetnlp/banglishbert", "sagorsarker/bangla-bert-base", "shahidul034/text_generation_bangla_model", "Bangla Fasttext"]
headline_numbers:
  - "sagorsarker/bangla-bert-base shows strongest bias: WEAT Cohen's d = -0.803 (p = 1.00) (p.5)"
  - "Only 4.25% of STEM-specific Pokkhopat words appear in Bangla2B+ corpus (p.7)"
  - "No model achieves statistically significant gender bias at p < 0.05 via WEAT p-values (p.6)"
  - "Pokkhopat dataset: 57 male, 56 female, 47 STEM, 73 SHAPE words = 237 total Bangla terms (p.3)"
---
## 1. Gist
Arnob et al. introduce Pokkhopat, a curated Bangla-language dataset of gendered terms and profession-related words across STEM and SHAPE (Social Sciences, Humanities, and Arts) domains, and use five embedding-based bias detection metrics to audit 11 pretrained Bangla language models (PBLMs). The paper fills a gap: gender bias in Bangla NLP — spoken by 240+ million people — was essentially unstudied. The key finding is that statistically significant gender bias is difficult to detect not because it is absent, but because most STEM/SHAPE vocabulary is out-of-vocabulary (OOV) in existing Bangla corpora. This has implications for any values-alignment benchmark working with low-resource or non-English languages: OOV issues can mask biases that are structurally present.

## 2. Benchmark/eval design features
This is an audit study, not a benchmark. Five embedding-based bias metrics are applied to 11 models:

1. **WEAT (Word Embedding Association Test)**: Cohen's d measuring association of STEM/SHAPE terms with male/female embeddings. Null hypothesis: no gender-profession association. Range [−1, +1]; near 0 = unbiased.
2. **ECT (Embedding Coherence Test)**: Spearman correlation between STEM (or SHAPE) similarities to male vs. female mean embeddings. Near +1 = unbiased.
3. **Cosine Similarity Visualization**: 2D scatter plot of mean cosine similarity (STEM vs. male) on x-axis vs. (STEM vs. female) on y-axis. Points near the identity line y=x indicate no bias.
4. **RND (Relative Norm Distance)**: Sum of (||STEM − male||₂ − ||STEM − female||₂). Near 0 = unbiased.
5. **RIPA (Relational Inner Product Association)**: Dot product of STEM embeddings with normalized (male − female) direction. Near 0 = unbiased.

## 3. Task format & example item
This is an embedding-distance audit, not an item-response task. No individual "items" in the MCQ sense. The evaluation procedure passes word lists through each model to obtain embeddings, then computes metric scores. n/a for task format.

## 4. Scoring / grading methodology
Each metric produces a continuous scalar per model per domain (STEM or SHAPE). WEAT p-values are computed via permutation test (16 threads parallel, following Caliskan et al. 2017). Threshold for rejecting null bias hypothesis: p < 0.05. ECT near +1 = less bias; RND near 0 = less bias; RIPA near 0 = less bias. No aggregate composite score across metrics is proposed — they are read jointly.

## 5. Dataset construction & provenance
Pokkhopat dataset: 57 male words, 56 female words, 47 STEM words, 73 SHAPE words (237 total Bangla words, 2,242 characters). Gender-specific words drawn from existing Bangla linguistic resources and validated by two native speakers. STEM words sourced from U.S. Bureau of Labor Statistics occupational taxonomy; SHAPE words from University of Edinburgh SHAPE definition. Dataset includes synonyms and family relation terms for coverage. Type-Token Ratio = 0.970 (high lexical diversity). Publicly available at Mendeley Data. Notable: Bangla lacks grammatical gender, so the dataset relies on semantic gender distinctions.

## 6. Validity evidence
- No human baseline for bias assessment is provided.
- Two native Bangla speakers validated the dataset for linguistic accuracy and semantic clarity.
- WEAT p-values show no model achieves p < 0.05 — no statistically significant bias detected, but authors argue this is an artifact of OOV issues rather than genuine absence of bias.
- t-SNE visualization (Figure 5) demonstrates that OOV SHAPE words are embedded in a distinct latent space from in-vocabulary words in csebuetnlp/banglabert, providing direct evidence that OOV terms corrupt bias measurements.

## 7. Saturation / discrimination
Low discrimination is the central finding. Most bias metrics show values near zero for most models, but this is largely explained by OOV: only 4.25% of STEM words appear in Bangla2B+ corpus, and 26.98% of SHAPE words. sagorsarker/bangla-bert-base is the notable exception with the highest measured bias (WEAT Cohen's d = −0.803, p = 1.00; high RNDSHAPE = 0.25). ECT scores for all models remain close to 1 (near-zero bias signal). RIPA scores for ritog/bangla-gpt2 show some STEM-male association (RIPASTEM = 0.1476).

## 8. Multiturn / agentic aspects
n/a — embedding-space bias audit, no interaction protocol.

## 9. Key numbers
- 11 PBLMs evaluated, ranging 18.1M to 321.6M parameters (p.5)
- Pokkhopat: 57 male, 56 female, 47 STEM, 73 SHAPE words; 237 total (p.3)
- Type-Token Ratio: 0.970 (p.3)
- sagorsarker/bangla-bert-base: WEAT Cohen's d = −0.803 (p = 1.00), RNDSHAPE = 0.258, RNDSTEM = 0.357 (p.5)
- Bangla2B+ corpus: 56.14% male words in vocab, 51.78% female, only 4.25% STEM, 26.98% SHAPE (p.8, Table 2)
- BanglaLM corpus: 27.65% STEM, 52.38% SHAPE in vocabulary (p.8)
- OSCAR_Bn: 4.25% STEM, 28.57% SHAPE in vocabulary (p.8)
- Bangla internet users: 131 million as of 2023 (p.2)
- Over 240 million Bangla speakers worldwide (p.1)

## 10. Pitfalls & limitations
- **OOV problem dominates results**: The primary finding is that OOV issues prevent detection of bias, not that bias is absent — a significant interpretive challenge.
- Binary gender only; non-binary/third gender identities not represented (Bangladesh census reports 12,629 identifying as "Third Gender").
- Standard metrics (WEAT, ECT, etc.) may be insufficiently sensitive for morphologically rich, low-resource languages with complex tokenization.
- Analysis restricted to 11 Bangla models; newer LLaMA/Gemma-based Bangla models are not included.
- Only static word embeddings analyzed; no generative or instruction-following behavior assessed.
- p-values show weak statistical significance throughout.
- Comparisons across 11 models are complicated because vocabulary coverage varies substantially — some unfair comparisons.

## 11. Novel ideas worth stealing
- **OOV as a bias measurement validity threat**: Explicitly measuring and reporting what percentage of target words are in-vocabulary before running bias metrics. Any benchmark evaluating cultural or domain-specific bias should check OOV rates as a methodological prerequisite.
- **Multi-metric battery for bias**: Running five complementary metrics (WEAT, ECT, cosine similarity, RND, RIPA) rather than any single metric, since different metrics can detect biases that others miss.
- **t-SNE OOV visualization**: Using dimensionality reduction to visually demonstrate embedding space divergence between in-vocabulary and OOV target words — a compelling validity check for embedding-based evaluations.
- **Pokkhopat as a template**: The structured word list format (male/female/STEM/SHAPE in JSON with synonyms and family-relation terms) is a reusable template for building gender-profession bias evaluation datasets in other low-resource languages.

## 12. Notable quotes
- "Most Pokkhopat words are absent from Bangla corpora, potentially hindering the detection of statistically significant gender bias in PBLMs." (p.8)
- "When attribute words, like those related to STEM and SHAPE, are missing from a model's pretrained data, their embeddings are either underrepresented or significantly different from those seen in the training corpus." (p.8-9)
- "The creators of Bangla2B+ tried to eliminate harmful content from the corpus as much as possible, which could have contributed to detecting the lowest bias for models trained on Bangla2B+." (p.5)

## 13. UNKNOWN / not in extract
- Full JSON content of the Pokkhopat word lists not reproduced in the extract.
- Exact IRB protocol or ethics approval not mentioned.
- Whether results generalize to generative LLMs or instruction-tuned models is untested.
- Inter-annotator agreement for the native-speaker validation is not reported.
- Licensing terms for Pokkhopat dataset not stated in the extract.
