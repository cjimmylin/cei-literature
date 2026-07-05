---
stem: "2025-Mahajan-Mapping Moral Reasoning in LLMs"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, validity-psychometrics, design-space]
task_format: "free-text"
scoring_type: "mixed"
dataset_size: 90
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: ["qwq:latest", "deepseek-r1:32b", "gemma3:27b"]
headline_numbers:
  - "90 total responses (3 models × 3 scenarios × 10 runs) analyzed (p.5)"
  - "Statistically significant inter-model differences in reasoning steps (H=32.21, p<0.001), density (H=44.27, p<0.001), and moral terms (H=17.70, p<0.001) (p.7)"
  - "ARI between baseline and ablation cluster assignments = 0.475 [95% CI: 0.346, 0.645] (p.9)"
  - "Silhouette score dropped from 0.665 (baseline) to 0.400 under dictionary-ablation (p.9)"
  - "qwq:latest mean reasoning steps = 18.10; gemma3:27b = 6.37 (p.8)"
  - "Cosine intra-model similarity: qwq:latest = 0.926, deepseek-r1 = 0.894 (p.8)"
---
## 1. Gist
This paper by Sachit Mahajan (ETH Zurich, AIES 2025) develops and validates a multi-dimensional moral profiling pipeline for open-weight LLMs. Rather than evaluating models on standard ethical benchmarks, Mahajan presents three structured dilemmas designed to elicit conflicts between competing safety principles (public welfare vs. confidentiality; corporate responsibility vs. whistleblowing; system transparency vs. protection), then encodes each model response into an 11-dimensional normative alignment vector derived from a hybrid of semantic similarity to canonical ethical theories and dictionary-based moral-vocabulary counts. The resulting profiles enable quantitative taxonomy of reasoning styles via unsupervised clustering. The paper is relevant to values-alignment benchmarking as a methodology paper: it demonstrates a replicable, interpretable pipeline for auditing and comparing LLMs' latent ethical orientations across multiple normative dimensions, moving beyond binary safety flags or aggregate accuracy scores.

## 2. Benchmark/eval design features
The study is a methodology demonstration, not a benchmark release. Core constructs measured: (1) which ethical frameworks dominate LLM responses (utilitarianism, deontology, virtue ethics, care ethics, autonomy, justice, and five others forming an 11-dimension space); (2) safety prioritization along five dimensions (immediate harm, long-term impact, systemic risk, individual protection, collective welfare); (3) reasoning complexity (causal steps, density, moral term frequency); (4) behavioral consistency across runs (cosine stability). Item structure: three open-ended safety dilemma scenarios, each presented as a natural-language prompt. Answer space: free-text, up to 4000 tokens, at temperature 0.7. The key analytical moves are computing a hybrid alignment vector v ∈ R¹¹ (semantic embedding cosine similarity weighted at 1.0 plus dictionary score weighted at ω = 0.4), normalizing to a probability distribution, and applying PCA + KMeans (k=3) to discover latent reasoning styles. Three clusters are identified in an unsupervised fashion: Balanced Integration, Rule-Based Conservatism, and Contextual Pragmatism.

## 3. Task format & example item
The paper does not reproduce the full prompts verbatim in the extract, but characterizes the three dilemma types:

- "Public Safety vs. Confidentiality: Disclosure of contagious disease status against privacy." (p.5)
- "Corporate Responsibility vs. Whistleblowing: Reporting internal safety violations at the risk of breaching confidentiality." (p.5)
- "System Bias vs. Transparency: Acknowledging bias in an AI hiring system while safeguarding proprietary algorithmic details." (p.5)

No verbatim prompt text is reproduced in the extract.

## 4. Scoring / grading methodology
No human raters or ground-truth labels are used for scoring individual responses. Scoring is fully automated:
- Dictionary-based: tokenization via spaCy, keyword matching normalized by sentence length, yielding proportional moral-category scores.
- Semantic: sentence embeddings via all-MiniLM-L6-v2, cosine similarity to 3-5 canonical sentences per ethical framework, top-score aggregation.
- Combination: v_i = s_i + ω·d_i (ω = 0.4), then L1-normalized.
- Downstream metrics: Shannon entropy over the 11-dim vector, top-2 dominance ratio, causal step counts, reasoning density, systemic safety recall.
- Statistical testing: Kruskal–Wallis H-tests with Tukey HSD post-hoc for inter-model comparisons.

## 5. Dataset construction & provenance
Three dilemma scenarios were hand-authored by the researcher to probe safety-principle conflicts in high-stakes domains. Each of three open-weight models (hosted via Ollama API) was queried 10 times per scenario, yielding 90 responses total (3 × 3 × 10). Temperature = 0.7, max_tokens = 4000. All source code, prompts, scenario texts, and outputs are archived on GitHub (https://github.com/sachit27/Moral-Reasoning-in-LLMs). No held-out test set; no formal train/validation split; no contamination controls beyond using publicly available, instruction-tuned open-weight models. Dataset is extremely small (90 items), limiting statistical power.

## 6. Validity evidence
Inter-model differences in reasoning complexity are statistically significant (Kruskal–Wallis p < 0.001 for steps, density, moral terms), providing some construct validity for the pipeline's ability to differentiate model behaviors. Robustness is assessed through an ablation removing all dictionary features (ω = 0): the three-cluster structure persists with ARI = 0.475 (bootstrapped 95% CI [0.346, 0.645]), showing semantic embeddings alone carry sufficient ethical signal. Results replicated with HDBSCAN (ARI = 0.461). Silhouette scores decline under ablation (0.665 → 0.400), confirming dictionary features add clustering quality but are not load-bearing. No human validation of cluster labels; no inter-rater reliability reported.

## 7. Saturation / discrimination
The 90-response dataset provides meaningful discrimination across three model families on reasoning-complexity metrics, but shows no significant differences on entropy or top-2 dominance (p = 0.912 and p = 0.349 respectively), suggesting those metrics may not discriminate well at this scale. Systemic-risk recall is consistently low across all models (range 0.028–0.034), indicating a real and consistent gap in LLM moral reasoning, but also a floor effect for that dimension. The small N (30 responses per model) limits power for fine-grained scenario-level analyses.

## 8. Multiturn / agentic aspects
n/a — all evaluations are single-turn prompts queried via the Ollama inference API.

## 9. Key numbers
- 90 total responses: 3 models × 3 scenarios × 10 runs (p.3)
- Temperature = 0.7, max_tokens = 4000 (p.3)
- Dictionary weight ω = 0.4 (p.4)
- Mean reasoning steps: qwq:latest = 18.10, deepseek-r1:32b = 10.33, gemma3:27b = 6.37 (p.8)
- Mean moral terms: qwq:latest = 9.37, deepseek-r1 = 8.37, gemma3 = 5.77 (p.8)
- Cosine similarity (intra-model): qwq = 0.926, deepseek = 0.894, gemma3 = 0.891 (p.8)
- Kruskal–Wallis H for reasoning steps: H = 32.21, p < 0.001 (p.7)
- Kruskal–Wallis H for density: H = 44.27, p < 0.001 (p.7)
- Kruskal–Wallis H for moral terms: H = 17.70, p < 0.001 (p.7)
- ARI baseline vs. ablation (KMeans): 0.475, 95% CI [0.346, 0.645] (p.9)
- ARI baseline vs. ablation (HDBSCAN): 0.461 (p.9)
- Silhouette: 0.665 baseline, 0.400 ablation (KMeans); 0.562 / 0.319 (HDBSCAN) (p.9)
- Individual protection emphasis (mean weight): qwq = 0.521, deepseek = 0.477, gemma3 = 0.331 (p.6)
- Systemic risk emphasis: all models 0.028–0.034 (p.6)

## 10. Pitfalls & limitations
- Tiny dataset (90 responses, 3 models, 3 scenarios) limits generalizability.
- Only three open-weight reasoning-style models tested; no proprietary frontier models.
- Scenarios are all English-language and drawn from Western professional contexts; cultural specificity not addressed.
- Moral lexicon may omit culturally specific or non-Western ethical vocabulary (author-acknowledged, p.10).
- Clustering reveals reasoning style descriptors but provides no normative guidance on which style is preferable for which application (author-acknowledged).
- Unsupervised cluster labels (e.g., "Rule-Based Conservatism") are post-hoc interpretations by the researcher, not validated against human annotations.
- Dictionary-based scoring relies on surface lexical matching; sarcasm, negation, and complex reasoning structures may be mis-scored.
- The weight ω = 0.4 was selected by empirical clustering consistency, introducing a circularity risk if the same data inform both parameter choice and evaluation.

## 11. Novel ideas worth stealing
1. **11-dimensional hybrid alignment vector**: Combine semantic embedding similarity (to canonical ethical theory exemplars) with dictionary-based lexical scoring into a single normalized vector per response. This allows unsupervised discovery of reasoning style clusters without requiring human labels — directly applicable to any values-alignment benchmark that collects free-text model responses.
2. **Behavioral consistency metric via cosine stability**: Compute pairwise cosine similarity between alignment vectors across repeated runs of the same prompt to quantify moral consistency / drift. This complements accuracy-based reliability measures and is particularly useful when ground truth is ambiguous.
3. **Ablation to validate measurement instrument**: Systematically remove the handcrafted lexicon contribution (ω = 0) and recheck cluster structure via ARI. This "dictionary ablation" is a lightweight but principled check that the semantic signal — not the engineered features — is doing the measurement work.
4. **Safety prioritization profiling**: Decompose a single "safety emphasis" score into five sub-dimensions (immediate harm, long-term impact, systemic risk, individual protection, collective welfare) and report distribution across them. The consistent finding that "systemic risk" is neglected across all models is the kind of actionable, dimension-specific finding that a holistic score would miss.
5. **Reasoning path extraction via discourse connectives**: Parse causal/justificatory connectives ("because," "therefore," "as a result") into DAGs to quantify reasoning complexity. A simple, domain-agnostic measure of structural depth that does not require fine-tuned classifiers.

## 12. Notable quotes
- "LLMs tend to resolve safety dilemmas by emphasizing proximal, agent-focused consequences (e.g., protection, immediate harm), with comparatively minimal attention to systemic outcomes." (p.6)
- "A model that systematically downplays long-term impact or collective welfare may be unsuitable for high-stakes public use, regardless of benchmark accuracy." (p.10)
- "These clusters are discovered in an unsupervised manner without human labeling, indicating that model outputs exhibit structurally meaningful patterns." (p.9)
- "Systemic recall shows modest variance across models, despite being low in absolute magnitude, which may indicate systemic considerations are either under-emphasized or stably encoded across model architectures." (p.7)

## 13. UNKNOWN / not in extract
- Full verbatim text of the three dilemma prompts is not reproduced in the extract.
- Details of the 11 canonical ethical theory exemplar sentences used for semantic similarity are not listed.
- Specifics of the moral keyword dictionary beyond the description of hierarchical structure are not provided.
- Whether the code/dataset repository (GitHub) has been made publicly accessible and is complete is not confirmed in the text.
- No information on compute infrastructure or inference time.
- No demographic or geographic information about the author beyond institutional affiliation.
