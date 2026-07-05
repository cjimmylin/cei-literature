---
stem: "2026-Hu-The Straight and Narrow Do LLMs Possess an Internal Moral Path"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, cultural-linguistic, validity-psychometrics]
task_format: "n/a"
scoring_type: "LLM-judge"
dataset_size: 15222
dataset_construction: "LLM-generated"
languages: ["en", "zh"]
models_tested: ["Llama-3.1-8B-Instruct", "Llama-3.1 family"]
headline_numbers:
  - "Unified Moral Probe achieves 65.6% 10-way classification accuracy at Layer 17 for English (p.5)"
  - "Chinese probes achieve ~63% accuracy at Layers 15-17 (p.14)"
  - "Adaptive Moral Fusion (AMF) reduces HarmBench Attack Success Rate to 19.66% (p.8)"
  - "AMF lowers XSTest incorrect refusals to 2.00%, comparable to Claude-3.5-Sonnet (p.8)"
  - "Positive steering (λ=+2.0) drives virtuous responses above 85% across foundations; Care reaches 92% (p.7, p.18)"
  - "Total MVV dataset: 15,222 samples; Chinese 11,014 from C-MFD, English 4,208 from MFD (p.12)"
  - "Care dimension shows Chinese-dominant asymmetry: Transfer Discrepancy δ ≈ −0.28 (p.6)"
---
## 1. Gist
This paper investigates whether LLMs possess genuine internal moral representations rather than superficial behavioral guardrails. Using Moral Foundations Theory (MFT) as a framework, the authors construct a bilingual (English/Chinese) dataset of Moral Virtue-Vice (MVV) sentence pairs, train linear probes on hidden states across all Transformer layers, and extract "Moral Vectors" — steerable directions in latent space corresponding to each of the five MFT foundations (Care, Fairness, Loyalty, Authority, Sanctity). Their key finding is that moral representations are linearly separable in middle Transformer layers and partially shared across English and Chinese — but with culturally conditioned asymmetries. The resulting Adaptive Moral Fusion (AMF) method uses probe-detected vice signals to dynamically inject corrective moral vectors at inference time, simultaneously reducing jailbreak success and over-refusal. This matters for values-alignment benchmarking because it demonstrates that moral evaluation can move beyond behavioral output scoring to probe internal latent representations, offering a richer and more manipulation-resistant lens.

## 2. Benchmark/eval design features
Not a benchmark paper; this is a mechanistic interpretability study. Core claims:
1. **Linear separability**: A unified 10-class linear probe (5 foundations × 2 polarities) trained on last-token hidden states achieves peak accuracy at Layer 17 (~65.6% for English), demonstrating that moral categories are encoded as distinct directions in mid-layer residual streams.
2. **Cross-lingual shared subspace**: Transfer probes between English and Chinese reveal a "shared yet different" moral subspace. Some foundations show isomorphic alignment (|δ| < 0.06), while others show asymmetric feature coverage (|δ| up to 0.30). Chinese representations dominate for Care and Loyalty-Vice; English dominates for Sanctity-Virtue and Authority-Virtue.
3. **Causal steerability**: Mean-difference Moral Vectors causally modulate outputs along a continuous Virtue↔Vice axis (λ ∈ [−2, +2]), validated by an LLM judge (GPT-5).
4. **Safety application**: AMF dynamically gates vector injection via probe confidence, outperforming static global virtue vectors on both HarmBench (harm reduction) and XSTest (over-refusal reduction).

## 3. Task format & example item
The evaluation uses generation steering rather than a fixed MCQ format. Example steering task (p.7, Table 1):

> **Context**: "At the animal shelter,"
> **Original (λ=0)**: "It was a sign that something was wrong."
> **Steered (λ=+2, Care)**: "The little girl gently picked it up to help."

Another example (p.19, Table 11):
> **Context**: "When the elderly woman dropped her groceries,"
> **Negative Steering (λ=−2)**: "I was too busy to help." (Indifference)
> **Positive Steering (λ=+2)**: "I offered to help her carry them to her car." (Compassion)

## 4. Scoring / grading methodology
Behavioral output steering is scored by GPT-5 as an external LLM judge, classifying generated responses into three categories: Virtue, Vice, or Neutral (p.7). Internal steering efficacy is validated by feeding steered activations back through the Unified Moral Probe and measuring probability shifts per category. Safety evaluation uses HarmBench Attack Success Rate (ASR) and XSTest incorrect refusal rate — both lower-is-better metrics (p.8).

## 5. Dataset construction & provenance
The MVV dataset (15,222 samples total; 4,208 English from MFD, 11,014 Chinese from C-MFD) is constructed via a "Moral Minimal Pair" (MMP) paradigm (p.12). Shared neutral contexts are generated, then contrasting Virtue and Vice suffixes are produced by Gemini 3 Pro using strict symmetry constraints: same word count, same syntactic structure, identical topic — only moral polarity differs. Seed vocabulary comes from the Moral Foundations Dictionary (MFD; Frimer et al., 2019) for English and the Chinese Moral Foundations Dictionary (C-MFD; Cheng & Zhang, 2023) for Chinese. The dataset is entirely LLM-generated without large-scale human annotation. Train/test split is 8:2 (p.7).

## 6. Validity evidence
- Cross-lingual transfer accuracy substantially exceeds random baseline (10%) for both languages, confirming that moral representations are not language-specific artifacts (p.5–6).
- Activation Oracle decoding (Karvonen et al., 2025) verifies that extracted Moral Vectors trigger semantically aligned concepts when injected into an interpretable prompt template (e.g., Fairness vector → "Justice"; Care vector → "Respect for all living beings") (p.18, Table 9).
- 5-fold stratified cross-validation is used for probe training (p.13).
- No formal human inter-rater reliability or human baseline is reported.

## 7. Saturation / discrimination
Peak probe accuracy of 65.6% on a 10-class task is well above chance (10%), but leaves substantial room for improvement, indicating the moral space is not trivially separable. Sanctity shows highest classification confidence (~0.71 for Sanctity-Virtue at Layer 17), while Authority and Loyalty show the most confusion due to semantic overlap (p.14). The "rise-peak-decline" layer trajectory (p.14) suggests that mid-layers (13–20) are the richest for moral encoding and that later layers shift representations toward next-token prediction, reducing separability.

## 8. Multiturn / agentic aspects
Not applicable. All experiments use single-turn inference-time activation steering with static inputs.

## 9. Key numbers
- Peak probe accuracy: 65.6% (English, Layer 17) (p.5)
- Chinese probe peak: ~63% (Layers 15–17) (p.14)
- MVV dataset total: 15,222 samples (English 4,208, Chinese 11,014) (p.12)
- AMF HarmBench ASR: 19.66% (p.8)
- AMF XSTest incorrect refusals: 2.00% (p.8)
- Positive steering (λ=+2.0): >85% virtuous responses across all foundations; Care peaks at 92% (p.7)
- Negative steering (λ=−2.0): virtuous responses drop below 20% for most foundations (p.7)
- Care Transfer Discrepancy δ ≈ −0.28 (Chinese-dominant) (p.6)
- Sanctity-Virtue δ ≈ 0.30 (English-dominant) (p.6)
- Sanctity-Vice: strong mutual transferability (|δ| < 0.06), high mutual accuracy (p.6)
- AMF threshold ablation optimum: τ = 0.2 (p.16)

## 10. Pitfalls & limitations
- **Cultural scope limited to English and Chinese**: The binary cross-lingual comparison excludes low-resource, non-WEIRD, non-Sinosphere cultures. Authors acknowledge the framework may not generalize without further tuning (p.9).
- **MFT-only normative grounding**: The Moral Vectors may reflect intuitionist moral responses at the expense of deliberative reasoning (utilitarian or deontological). MFT does not exhaust machine ethics (p.9).
- **LLM-generated dataset**: All 15,222 samples were produced by Gemini 3 Pro without large-scale human annotation, inheriting the generator's biases and limited semantic diversity (p.9).
- **Dual-use risk**: Inverting steering direction (λ < 0) can induce harmful "Vice" content. The same extraction techniques could be weaponized to bypass safety guardrails (p.9–10).
- **Cultural homogenization risk**: A static "Moral Vector" applied globally could impose Western or Sinosphere cultural hegemony on concepts like Authority or Loyalty (p.10).
- **Architecture restricted to Llama-3.1**: Cross-architecture generalizability is hypothesized but not tested (p.9).

## 11. Novel ideas worth stealing
1. **Moral Minimal Pair (MMP) paradigm**: Generating stimulus pairs that share a neutral context but differ only in moral polarity (Virtue vs. Vice) with matched syntax and length — directly isolates the moral signal from confounding linguistic features. Highly reusable for building values-alignment evaluation stimuli.
2. **Cross-lingual transfer discrepancy (δ) as validity check**: Training probes on one language and testing on another provides a rigorous, non-circular validity test for whether a construct is language-agnostic or language-specific. Directly applicable to any cross-cultural values benchmark.
3. **Activation Oracle for semantic verification**: Using the model's own generative capabilities to decode what a latent direction "means" is a lightweight, interpretable sanity check that requires no external resources.
4. **Layerwise probe accuracy curve as architecture diagnostic**: The "rise-peak-decline" pattern reveals which layers encode high-level semantic content vs. lexical vs. output prediction. Useful for choosing probe insertion points in any probing evaluation.
5. **Dynamic coefficient gating via probe confidence**: AMF's ReLU-thresholded dynamic weighting (αf = ReLU(Pvice − τ) · λbase) prevents over-correction and preserves helpfulness. This pattern is reusable in any evaluation scenario where different steering intensities are needed across inputs.
6. **Cultural asymmetry discovery via probe transfer**: The bidirectional transfer discrepancy analysis systematically reveals which moral concepts have richer Chinese vs. English semantic scope — a concrete method for detecting cross-cultural measurement non-equivalence.

## 12. Notable quotes
- "Current models may merely mimic moral verdicts to satisfy reward functions, without internalizing a robust representation of morality." (p.1)
- "Our results reveal the shared nature of middle-layer moral representations formed in a shared but different moral subspace. This finding not only validates that LLMs have developed abstract, language-agnostic moral representations but also highlights cultural nuances in how concepts like 'Loyalty' or 'Authority' are encoded." (p.1–2)
- "Fairness and Loyalty amplify Authority-virtue, suggesting semantic entwinement. Furthermore, the universal suppression of Sanctity-vice identifies it as a 'universal negative pole', implying that virtue fundamentally requires distancing from degradation." (p.7)
- "While our primary objective is to enhance safety through Adaptive Moral Fusion to mitigate jailbreaks, the same mechanism poses dual-use risks." (p.9)

## 13. UNKNOWN / not in extract
- The exact size of train/test splits per foundation and language is not specified beyond the 8:2 global ratio.
- Human inter-rater reliability statistics for the MVV dataset construction are not reported.
- Performance breakdown by individual moral foundation in HarmBench and XSTest is not given in the main text; only aggregate ASR and refusal rates are reported.
- Full model card / compute requirements for the experiments are not in the extract.
- Whether the Activation Oracle interpretations were validated by human experts is not stated.
