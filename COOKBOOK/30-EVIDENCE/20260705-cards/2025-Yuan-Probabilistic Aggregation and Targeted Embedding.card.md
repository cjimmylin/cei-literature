---
stem: "2025-Yuan-Probabilistic Aggregation and Targeted Embedding"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, moral-psychology, llm-judges-scoring]
task_format: "free-text"
scoring_type: "mixed"
dataset_size: 42501
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["Llama-2-7B-chat", "Llama-2-13B-chat", "Llama-3.2-3B-Instruct", "Llama-3-8B-Instruct", "GPT-3.5-Turbo", "GPT-4o-Mini", "Claude-3-Haiku-20240307", "Moonshot-v1-8k"]
headline_numbers:
  - "Llama2-13B F1 on deontology improved from 37.68% to 58.96% after embedding optimization (p.7)"
  - "Llama2-13B F1 on utilitarianism improved from 41.55% to 49.76% after embedding optimization (p.7)"
  - "Justice/virtue inter-theory correlation ≈0.83; deontology/utilitarianism correlation ≈0.55 (p.8)"
  - "Human-AI alignment score for deontology at high-clarity samples: 67.53% (p.15)"
  - "Human-AI alignment score for utilitarianism at high-clarity samples: 77.92% (p.15)"
  - "42,501 moral dilemmas from AITA dataset, summarized to ≤150 tokens via GPT-4o-Mini (p.6)"
---
## 1. Gist
This paper proposes a two-part framework for achieving collective moral reasoning across multiple LLMs. The first component is a truncated-normal Expectation-Maximization (EM) algorithm that fuses continuous moral acceptability scores (in [0,1]) from multiple LLMs into a single collective probability, weighting each model by its reliability. The second component is a targeted embedding optimization that adjusts only the token embeddings for specific moral philosophical theories (virtue, justice, deontology, utilitarianism, commonsense) for models that diverge significantly from the consensus. Evaluated on 42,501 social moral dilemmas sourced from the Reddit AITA dataset, the framework demonstrates that reliable multi-LLM consensus can be built, and that localized embedding adjustments can partially correct theory-level misalignment in weaker models. This matters for values-alignment benchmarking because it surfaces a principled method for aggregating diverse model moral judgments, identifies which moral theories prove hardest for which model families, and raises fundamental questions about how to define a ground truth for moral evaluation.

## 2. Benchmark/eval design features
This is not a benchmark paper; it is a method paper proposing a collective moral reasoning framework. Key constructs:
- **Five moral theories from ETHICS (Hendrycks et al., 2021):** virtue, justice, deontology, utilitarianism, commonsense morality.
- **Continuous annotation:** Each LLM assigns a score in [0,1] for each scenario × theory pair, representing its estimated probability that the narrator's behavior is morally acceptable.
- **Collective opinion:** A consensus probability γ_{j,i} derived from the truncated-normal EM procedure, accounting for each model's reliability (mean and variance of positive and negative predictions).
- **Misalignment detection:** F1 score between each LLM's binarized judgment and the consensus label; models with low F1 on specific theories are flagged for embedding optimization.
- **Embedding optimization target:** Only the tokenized theory-name tokens (e.g., "_de", "ont", "ology" for deontology) plus a lightweight feedforward head are trained; all other parameters are frozen.

Core claim: moral consensus should be evaluated not as accuracy against a single ground truth, but as coherence with an emergent model-based reference. The framework "emphasizes coherence over correctness" (p.2).

## 3. Task format & example item
LLMs are prompted with a summarized moral scenario (≤150 tokens) and asked to rate moral acceptability under each of the five theories. An example prompt from Figure 11 (p.18):

> "You represent a wide range of people's thoughts. Your task is to assess the morality of my behavior in the given 'Moral Situation' across various moral concepts... Justice: Does my behavior treat everyone equally? ... Output: Justice Vector: [Moral ratio, Immoral ratio]" (p.18)

A representative scenario used in the human annotation case study (Table 9, p.16):
> "My family controls every aspect of my life… I want to see a friend… I will be a legal adult, and I plan to pay for the trip myself. Would it be wrong to go without their permission?" (p.1, Figure 1)

## 4. Scoring / grading methodology
- Primary metric: **F1 score** comparing each LLM's binarized moral judgment against the binarized consensus label (threshold τ = 0.5).
- Secondary metrics: reliability parameters μ₁(m), σ₁(m), μ₀(m), σ₀(m) — mean and variance of each model's annotations on positive (morally acceptable) vs. negative (immoral) scenarios.
- Human alignment: measured as proportion of matched binarized judgments between LLM collective and human annotations, stratified by moral clarity level (high/moderate/full sample).
- Robustness test: "Random01" model (always assigns extreme 0 or 1) is injected to test whether the aggregation method is skewed by an unreliable participant.

## 5. Dataset construction & provenance
- Source: 42,501 posts from the Reddit r/AmITheAsshole (AITA) dataset (Nguyen et al., 2022), a large-scale repository of interpersonal moral dilemmas.
- Preprocessing: GPT-4o-Mini summarizes each post to ≤150 tokens (targeting ~100 words) to reduce idiosyncratic noise and make inference tractable.
- Annotation: Each summarized dilemma × five moral theory = continuous score from each LLM (8 models evaluated across different experiment configurations).
- Human annotation: 400 samples annotated by two groups of 10 annotators each (Asian and European backgrounds), recruited via Prolific; covering deontology and utilitarianism only.
- Train/val/test split for embedding optimization: 8:1:1, with class balancing via downsampling.
- No explicit contamination controls mentioned.

## 6. Validity evidence
- **Human–LLM alignment:** At high-clarity moral scenarios (clearly moral or immoral per human raters), the collective LLM framework achieves 67.53% (deontology) and 77.92% (utilitarianism) alignment with human annotation (p.15). This degrades as moral ambiguity increases, which is expected.
- **Inter-theory correlation:** Computed Pearson correlations among five theories under the five-LLM setting show expected patterns: justice/virtue most correlated (≈0.83), deontology/utilitarianism least correlated (≈0.55, p.8).
- **Robustness check:** When Random01 is added to mean-based aggregation, Random01 spuriously achieves the highest F1 (≈80.85 on justice, p.14); the truncated-normal EM correctly assigns Random01 low F1 (≈55.64 on justice, p.14), confirming the aggregation method is outlier-robust.
- **Embedding projection:** PCA+t-SNE visualization shows trained deontology tokens drift toward semantically related tokens (law, policy, culture) rather than moving arbitrarily (p.8, Figure 4).

## 7. Saturation / discrimination
- GPT-4o-Mini is consistently near ceiling (F1 ~88–89% on justice), suggesting strong alignment with the generated consensus.
- Smaller and older Llama models (Llama2-7B, Llama2-13B) show floor effects specifically on deontology and utilitarianism (F1 37–42% pre-optimization), indicating substantial discrimination between model families on these harder moral theories.
- After optimization, Llama2-7B F1 actually declines slightly (e.g., deontology 39.82→37.89), suggesting embedding optimization fails when initial consensus signal is too weak (p.8, Table 4).
- The alignment score gradient by moral clarity (67.53% high → 56.25% full for deontology) reveals that the framework discriminates moral difficulty well.

## 8. Multiturn / agentic aspects
n/a. All evaluations are single-turn prompts. The embedding optimization involves a separate fine-tuning loop but not interactive/agentic behavior.

## 9. Key numbers
- Dataset size: 42,501 AITA moral dilemmas (p.6)
- Number of moral theories: 5 (justice, virtue, deontology, utilitarianism, commonsense) (p.6)
- Models evaluated: 8, in groups of 4–5 (p.6)
- Llama2-13B deontology F1: 37.68% → 58.96% (+21.28%) after embedding optimization in 4-LLM setting (p.7, Table 3)
- Llama2-13B utilitarianism F1: 41.55% → 49.76% (+8.21%) (p.7, Table 3)
- GPT-4o-Mini justice F1: 88.73% (p.7, Table 3)
- Justice/virtue Pearson correlation: ≈0.83 (p.8)
- Deontology/utilitarianism Pearson correlation: ≈0.55 (p.8)
- Human annotation: 400 samples, 20 annotators from Asian and European groups (p.13)
- Human alignment (high clarity): 67.53% deontology, 77.92% utilitarianism (p.15)
- Embedding optimization compute: 57 GB GPU, ~4 hours/epoch for Llama2-13B (p.9)
- Morally acceptable samples in aggregated opinions: ~39–64% across theories (p.13, Figure 7)

## 10. Pitfalls & limitations
- **Limited model variety:** Only 4–5 models per experiment; no PaLM, T5, or large proprietary models beyond GPT-4o-Mini (p.9).
- **No true ground truth:** The "consensus" is itself derived from LLMs, creating a circular validation problem. Human annotation is limited to 400 samples and two cultural groups (p.9, 15).
- **Optimization failure mode:** When model agreement is already low (as in the Llama-only group), the embedding optimization fails or degrades performance, suggesting it can only exploit rather than create consensus (p.8).
- **Cultural and contextual variation:** Framework treats consensus as culturally uniform; human annotation reveals meaningful disagreement between Asian and European annotators on several scenarios (p.16, Table 9).
- **Computational overhead:** 57 GB GPU memory and ~4 hours/epoch for embedding optimization limits scalability (p.9).
- **Single intervention:** Embedding optimization only adjusts theory-name token embeddings; broader semantic misalignment is not addressed.

## 11. Novel ideas worth stealing
1. **Continuous moral scores instead of binary labels:** Requiring LLMs to output a [Moral %, Immoral %] vector per moral theory is much richer than yes/no judgment, enabling reliability modeling and gradient signals for alignment.
2. **Truncated-normal EM for annotator reliability:** Adapting multi-annotator reliability estimation (Dawid-Skene style) to continuous [0,1] scores with bounded domains is a directly transferable technique for any benchmark that aggregates LLM or human raters.
3. **Theory-specific misalignment diagnostic:** Plotting F1 scores per model × moral theory in a heatmap (Figure 3) immediately reveals which model-theory combinations are underperforming — a useful diagnostic for any multi-theory ethics benchmark.
4. **Random01 robustness stress test:** Injecting a randomly-responding agent into the annotation pool and checking whether it spuriously gains consensus weight is a clean, cheap adversarial validity check for any aggregation scheme.
5. **Token-level embedding surgery:** Fine-tuning only the sub-word tokens of theory names (not the whole model) to reduce misalignment is a low-cost, high-interpretability intervention that could be applied in benchmark construction to probe what theory concepts a model has actually internalized.
6. **Inter-theory correlation as a validity probe:** The expected philosophical tension (deontology vs. utilitarianism, r≈0.55) being recoverable from continuous LLM scores serves as a construct validity check without requiring human annotation.

## 12. Notable quotes
- "The fundamental premise of our approach is that social dilemmas rarely admit objectively correct judgments. In morally ambiguous real-world contexts, individuals often seek reference, not truth." (p.2)
- "Rather than claiming a single 'true' moral label, our goal is to provide a principled reference that balances multiple perspectives and pinpoints where real misalignment occurs." (p.2)
- "Our method is intentionally sensitive to epistemic uncertainty: it does not fabricate a consensus where none exists. This behavior is consistent with real-world moral conflict, where no single aggregation method can force agreement in the absence of shared values." (p.8)
- "Moral judgments inherently vary across cultures and contexts… Our current framework treats consensus as a single unified measure; in practice, alignment might need to be sensitive to cultural or individual differences." (p.9)

## 13. UNKNOWN / not in extract
- Exact prompt wording used for all five moral theories in the continuous annotation prompt (Figure 11 shows the full prompt but only virtue/justice/deontology/utilitarianism/commonsense headers are listed without the detailed sub-descriptions for each theory beyond what is in Figure 11 on p.18).
- Whether the AITA dataset has a license permitting redistribution.
- Number of EM iterations required for convergence in practice.
- Full set of hyperparameters for models other than Llama2 (learning rate, batch size for non-Llama variants).
- Whether the human annotators passed an attention or comprehension check.
- Details of the Prolific recruitment: compensation, exclusion criteria, demographic balance within the 20 annotators.
