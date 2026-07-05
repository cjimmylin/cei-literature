---
stem: "2025-Su-Understanding How Value Neurons Shape the"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, validity-psychometrics, design-space, normative-ethics]
task_format: "generative"
scoring_type: "LLM-judge"
dataset_size: 15000
dataset_construction: "LLM-generated"
languages: ["en"]
models_tested: ["LLama-3.1-8B", "Qwen2-0.5B", "LLama-3.2-1B", "gemma-2-9B"]
headline_numbers:
  - "ValueInsight contains 640 second-person value descriptions and 15,000 scenario-based open-ended questions (p.1)"
  - "Less than 0.4% of neurons in LLama-3.1-8B are value-related (p.7)"
  - "Value-related neurons are concentrated in middle layers (~15th layer) across all four value dimensions (p.7)"
  - "ValueLocate outperforms all three baselines on ValueInsight, PVQ40, and ValueBench across 4 LLMs (p.6)"
  - "ValueLocate G-EVAL scores: 4.68 (Openness to Change), 4.60 (Self-Transcendence), 4.15 (Conservation), 4.08 (Self-Enhancement) for LLama-3.1-8B (p.7)"
---
## 1. Gist
This paper introduces ValueLocate, a mechanistic interpretability framework that identifies and causally validates neurons in LLMs responsible for encoding specific values from the Schwartz Values Survey. To enable this analysis, the authors construct ValueInsight, a generative dataset of 15,000 scenario-based open-ended questions paired with contrastive value descriptions. The key contribution is an activation-difference-based neuron identification method that contrasts neuron firings between opposing value orientations (e.g., "Openness to Change" vs. its reversed counterpart) to localize a sparse set of value-critical neurons (<0.4% of total), predominantly in middle transformer layers. Causal validation via neuron activation editing confirms that manipulating these neurons shifts model value orientations measurably and monotonically. For benchmarking purposes, this work is significant because it demonstrates that values are localized, sparse, and causally editable in neural networks, with direct implications for building more principled values-alignment methods.

## 2. Benchmark/eval design features
ValueInsight is a generative benchmark grounded in the Schwartz Values Survey's four higher-order dimensions (Openness to Change, Self-Transcendence, Conservation, Self-Enhancement) and 57 atomic values. Each dataset item is a pair: a second-person value description (positive or reversed/negative) plus a situational open-ended question requiring the model to respond as if it holds that value. The benchmark is designed to elicit genuine value orientation in generated text rather than surface-level agreement scoring.

The neuron identification method (ValueLocate) computes activation probability difference δ = p⁺_{l,k} − p⁻_{l,k} between positive and negative value prompts; neurons with |δ| > 3% are classified as value-related. Validation proceeds by editing (amplifying or suppressing) identified neurons and measuring downstream value scores via G-EVAL.

Key claim: Existing benchmarks based on MCQ or binary yes/no formats reveal what models *understand* about values rather than their actual *orientation* — ValueInsight's generative format addresses this gap (p.2).

## 3. Task format & example item
Generative. A situational open-ended question is paired with a value description and the model is instructed to respond from that value perspective.

Example (p.4): Value description = "Openness_to_Change: You thrive in situations where you can make your own choices. Being able to decide what happens next makes you feel truly alive..." Situation = "You are on a cruise that offers a variety of excursions at each port. One of the excursions is a visit to a local village that is rarely visited by tourists, offering a chance to learn about traditional customs and lifestyles. However......" The model must respond in-character with the assigned value orientation. A reversed (Conservation) value description would produce a qualitatively different response (preferring conventional, structured excursions).

The prompt template instructs: "forget who you are and fully immerse yourself in the value described... Don't overthink your response—just begin writing and let your thoughts flow naturally... Try to keep your response under 300 words." (p.12)

## 4. Scoring / grading methodology
G-EVAL: a chain-of-thought LLM judge (using GPT-4o or equivalent) that scores each generated response on a 1–5 scale reflecting relevance to the target Schwartz value dimension. G-EVAL uses probability-weighted continuous scoring: score = Σ p(sᵢ) × sᵢ where S = {1,2,3,4,5}. Each response is scored across 10 independent G-EVAL runs and averaged to reduce variance (p.6). Text quality is evaluated separately using a GPT-4o judge on a 1–5 scale focusing on fluency and grammaticality (p.8).

Causal validation: value scores are compared before and after neuron manipulation (amplification γ=2.0 for positive neurons, suppression for negative neurons), with random neuron manipulation as a control.

## 5. Dataset construction & provenance
- Value descriptions: GPT-4o generates second-person narratives for each atomic value and its reversed counterpart; baseline descriptions are generated from templated prompts, then manually refined, then used as exemplars for iterative rephrasing. Total: 640 descriptions (p.3).
- Situational questions: GPT-4o generates questions grounded in real-world behavioral topics drawn from UltraChat (Ding et al., 2023). Topics include family, environment, arts, and others. Each question is further refined by GPT-4o to remove judgmental tone, cultural sensitivity, and emotionally charged phrasing (p.3-4). Total: 15,000 questions, averaging ~3,750 per higher-order dimension and ~300 per atomic value.
- No human annotation; fully automated pipeline using GPT-4o as generator and refiner.
- Evaluation subsets: 100 questions per higher-order dimension for neuron identification experiments; PVQ40 and ValueBench used as external validation datasets.
- No explicit license or public release URL mentioned in the extract.

## 6. Validity evidence
- **Cross-dataset replication**: ValueLocate evaluated on three distinct datasets (ValueInsight, PVQ40, ValueBench) with consistent results (Tables 1-3, p.7).
- **Causal validation**: Neuron editing causally manipulates value orientation; editing randomly selected neurons produces no significant change, confirming specificity (p.7-8).
- **Monotonic dose-response**: Increasing the number of edited value neurons (10, 20, 30, 40, 50) produces a consistent monotonic increase in G-EVAL value scores; random neuron counts produce no effect (Figure 5, p.7).
- **Bidirectional validation**: Both positive amplification and negative suppression produce predictable directional shifts (Appendix Tables 4-6).
- **Ablation studies**: γ parameter ablation and δ threshold ablation confirm the chosen 3% threshold is an empirically optimal operating point for value score vs. text quality tradeoff (Figure 6, p.8).

## 7. Saturation / discrimination
- Value-related neurons are sparse (<0.4% of total neurons in LLama-3.1-8B), indicating there is room to identify more neurons or higher layers.
- G-EVAL scores for Conservation and Self-Enhancement (~4.08–4.35) are systematically lower than for Openness-to-Change and Self-Transcendence (~4.55–4.80), suggesting harder discrimination for Conservation/Self-Enhancement — likely due to semantic overlap between Self-Enhancement and Openness-to-Change ("Enjoying life" appears in both dimensions) (p.6-7).
- CGVST occasionally outperforms ValueLocate on Self-Enhancement in gemma-2-9B, suggesting ceiling effects may exist for this dimension (p.6).

## 8. Multiturn / agentic aspects
n/a — single-turn generative evaluation; no interaction protocol or tool use.

## 9. Key numbers
- 640 second-person value descriptions (p.1)
- 15,000 scenario-based open-ended questions (p.1)
- 57 atomic values, 10 subvalues, 4 higher-order dimensions (Schwartz) (p.13)
- <0.4% of neurons in LLama-3.1-8B are value-related (p.7)
- Value-related neurons concentrated around 15th transformer layer (p.7)
- 14,336 neurons per layer in LLama-3.1-8B (p.7)
- ValueLocate LLama-3.1-8B G-EVAL (ValueInsight, positive editing): 4.68 / 4.60 / 4.15 / 4.08 (OTC/ST/CON/SE) (p.7)
- Best baseline CGVST: 4.42 / 4.25 / 3.85 / 3.88 (p.7)
- Threshold δ = 3% chosen as empirically optimal operating point (p.5)
- γ = 2.0 used as activation scaling factor in all main experiments (p.6)
- 10 independent G-EVAL runs per response (p.6)
- 4 LLMs tested: LLama-3.1-8B, Qwen2-0.5B, LLama-3.2-1B, gemma-2-9B (p.6)

## 10. Pitfalls & limitations
- Schwartz value dimensions are not entirely independent (e.g., both Self-Enhancement and Openness-to-Change include "Enjoying life"), causing systematic confusion in neuron identification (p.9).
- Experiments conducted on only four LLMs; method may require adaptation for other architectures (p.9).
- Evaluation focuses solely on value orientation scores, not text coherence, factual accuracy, or logical reasoning — high value score may co-occur with incoherent or hallucinated text (p.9).
- G-EVAL as judge introduces LLM-in-the-loop bias; no human validation of G-EVAL agreement is reported.
- Dataset is fully LLM-generated with no human curation of final items; normative/cultural biases from GPT-4o may be embedded in the benchmark.
- The "second-person value description + situational question" format may prompt models to perform role-play rather than reveal latent value encodings — conflating instruction-following with value representation.
- No contamination analysis; ValueBench and PVQ40 may have been seen during training of evaluated models.

## 11. Novel ideas worth stealing
1. **Contrastive value description format**: Pairing positive and reversed value descriptions to elicit differential neural activations is a powerful design principle. For benchmarks, this "value pole contrast" structure can be used to measure whether models respond differently to semantically opposite value framings.
2. **Activation difference as a value signal**: Computing δ = p⁺ − p⁻ at the neuron level operationalizes value orientation as a differential activation rather than an absolute score. This idea could inform soft disagreement metrics at the annotation level.
3. **Generative format over MCQ for value measurement**: The paper's core motivation — that MCQ reveals understanding of values rather than actual orientation — is directly actionable for benchmark design. Open-ended situational responses capture emergent value-consistent reasoning rather than selection from pre-seeded options.
4. **Real-world behavioral scenarios from topic databases**: Situational questions are grounded in life topics (family, environment, arts) rather than abstract philosophical dilemmas. This makes items more ecologically valid and reduces the tendency for models to give normatively "correct" abstract answers.
5. **Causal editing as benchmark validation**: Testing whether a benchmark truly measures what it claims to measure by showing that manipulating the target construct (value neurons) produces predicted changes in benchmark scores — this is a novel validity paradigm applicable beyond neurons (e.g., RAG document manipulation, system prompt swapping).
6. **Sparse localization in middle layers**: The finding that value neurons cluster in middle transformer layers (around layer 15 in LLama-3.1-8B) has implications for efficient value alignment: targeted interventions in middle layers may be more effective than global fine-tuning.

## 12. Notable quotes
- "Unlike existing related datasets mainly in the multichoice format, ValueInsight offers a distinct approach, performing generative value tasks in LLMs using real-world test cases." (p.2)
- "The dual nature of values refers to the opposing dimensions represented by a target value (e.g., Conservation) and its reversed counterpart (e.g., Conservation_reversed). This duality allows the measurement of neuronal activation differences between opposing value dimensions." (p.5)
- "Although each layer of LLama-3.1-8B consists of 14,336 neurons... we found that less than 0.4% of them are related to values, demonstrating that value orientations are significantly influenced by a small subset of neurons." (p.7)
- "Traditional evaluation questionnaires, such as PVQ40... often do not capture meaningful value tendencies. For example, a PVQ40 item such as 'It is important to her to be rich. She wants to have a lot of money and expensive things.' could lead to similar surface-level responses or prompt an LLM to assign a score; however, it fails to uncover the underlying value orientations." (p.3)

## 13. UNKNOWN / not in extract
- Whether ValueInsight is publicly released (no URL mentioned in the extract).
- Human validation of G-EVAL scores — no inter-rater reliability against human judges reported.
- Results on models larger than 9B parameters or closed-source models (GPT-4, Claude).
- Whether value neurons identified in one model transfer to or predict behavior in other models.
- Cross-lingual generalization: all experiments appear to be English-only.
- The complete list of 15,000 questions or the generation process checkpoints.
