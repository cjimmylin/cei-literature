---
stem: "OpenAI-gpt-oss-model-card-arxiv-2508.10925"
company: "OpenAI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, agentic-multiturn, contamination-robustness, saturation-discrimination]
headline_numbers:
  - "gpt-oss-120b has 116.8B total parameters but only 5.1B active parameters per token (p.5)"
  - "gpt-oss-120b scores 96.6% on AIME 2024 with tools (p.6)"
  - "Standard disallowed content eval saturated — all models at ~0.996 on hate aggregate (p.12)"
  - "Production Benchmarks illicit/nonviolent: 0.692 for gpt-oss-120b vs 0.658 for o4-mini (p.14)"
  - "All models score 0% on cyber range scenarios without hints (p.27)"
  - "22 external recommendations received; 11 acted on including 9 of 12 high-urgency items (p.18)"
---

## 1. Gist

This is the arXiv preprint version (arXiv:2508.10925v1, posted August 8, 2025) of the gpt-oss-120b & gpt-oss-20b Model Card by OpenAI. The substantive content is identical to the separately extracted non-arXiv version (`OpenAI-gpt-oss-model-card`). Both documents cover the same 35 pages of model architecture, capability benchmarks, safety evaluations, and Preparedness Framework assessments for OpenAI's first open-weight reasoning models. The arXiv version differs only in the addition of an arXiv identifier on page 1.

For full analysis, see the companion card `OpenAI-gpt-oss-model-card.card.md`. The summary below highlights key points sufficient for cross-referencing and indexing purposes.

OpenAI releases gpt-oss-120b and gpt-oss-20b as Mixture-of-Experts reasoning models under Apache 2.0. Post-training uses chain-of-thought reinforcement learning (similar to o3), deliberative alignment, and instruction hierarchy training. A central safety finding is that even adversarially fine-tuned gpt-oss-120b, trained by OpenAI using its best RL stack, does not reach the "High" capability threshold on biological/chemical or cyber risk domains under the Preparedness Framework. The card also contains notable benchmark design implications: the standard disallowed content evaluation is now explicitly declared saturated by OpenAI, and the new Production Benchmarks — drawn from real multi-turn production data — reveal far larger safety gaps (e.g., illicit/nonviolent drops from ~0.99 in standard eval to 0.692 in production benchmark).

## 2. Alignment/values methods used

Identical to companion card. Summarized: deliberative alignment (post-training), instruction hierarchy training (System > Developer > User > Assistant > Tool), CBRN pre-training data filtering, CoT RL post-training without direct CoT optimization pressure (to preserve monitorability). No constitutional AI or explicit model spec referenced in this card.

## 3. Values specification

Values encoded operationally via OpenAI's safety policies (unstated specifics), the harmony chat format role hierarchy, and the three Preparedness Framework risk categories. No explicit constitution or model spec document cited.

## 4. Safety & values evaluation methodology

LLM-graded Standard Disallowed Content Evaluation (being retired due to saturation), Production Benchmarks (multi-turn, production-representative), StrongReject jailbreak evaluation, instruction hierarchy evaluations, SimpleQA/PersonQA hallucination evals, BBQ fairness eval, adversarial fine-tuning Preparedness evaluations (bio, cyber, AI self-improvement). External review by METR, SecureBio, Daniel Kang. Expert baselines from PhD scientists on biosecurity benchmarks.

## 5. Benchmarks used or introduced

Same set as companion card: AIME, GPQA Diamond, HLE, MMLU/MMMLU, Codeforces, SWE-bench Verified, τ-Bench, HealthBench, BBQ, SimpleQA, PersonQA, Long-form Biorisk Questions, Multimodal Troubleshooting Virology (350 questions, SecureBio), ProtocolQA Open-Ended (108 questions), Tacit Knowledge MCQ (uncontaminated, Gryphon Scientific), TroubleshootingBench (new, 52 protocols × 3 questions, PhD-sourced), CTF Challenges, Cyber Range, OpenAI PRs, PaperBench.

## 6. Agentic / multiturn evaluation aspects

Harmony chat format enables interleaved CoT, tool calls, and responses in agentic workflows. Three tool types: browsing, Python/Jupyter, developer functions. Production Benchmarks are "highly multi-turn" (p.11). Cyber Range requires fully autonomous end-to-end cyber operations including planning and multi-step exploitation chaining. τ-Bench tests multi-turn tool-agent-user interaction.

## 7. Key numbers

- Total parameters: 116.8B (120b), 20.9B (20b); active parameters: 5.1B and 3.6B respectively (p.5)
- Training: 2.1 million H100-hours (120b) (p.5)
- AIME 2025 with tools: 97.9% (120b), 98.7% (20b), 99.5% (o4-mini) (p.6)
- HealthBench: 57.6% (120b), 59.8% (o3), 50.1% (o4-mini) (p.10)
- Standard disallowed hate aggregate: 0.996 across all tested models (p.12)
- Production Benchmarks illicit/nonviolent: 0.692 (120b), 0.658 (o4-mini), 0.573 (GPT-4o) (p.14)
- Instruction hierarchy prompt injection: 0.780 (120b) vs 0.917 (o4-mini) (p.14)
- Cyber Range pass@12 without hints: 0% for all models (p.27)
- ProtocolQA: all models below consensus expert baseline of 54% (p.20)
- TroubleshootingBench: all models below 80th percentile human score of 36.4% (p.22)

## 8. Findings relevant to values-benchmark design

Standard disallowed content evals are saturated and no longer provide incremental signal (p.11). Production-representative multi-turn benchmarks reveal much larger safety gaps. Expert human baselines (consensus, median, 80th percentile) situate model capability within the expert performance distribution, offering richer benchmarking signal than pass/fail thresholds. Uncontaminated, privately-sourced evaluation items (TroubleshootingBench) are essential for valid high-stakes capability assessment.

## 9. Novel ideas worth stealing

Same as companion card. Key insights: (1) use production conversations for benchmark construction; (2) report the distribution of human expert performance rather than a single threshold; (3) source evaluation items from practitioners' unpublished personal experience; (4) test adversarially fine-tuned variants to measure safety headroom; (5) distinguish refusal-based from non-refusal-based failures; (6) plan formal benchmark retirement when saturation is reached.

## 10. Notable quotes

"Our recent models saturate this benchmark (as visible in the results table), and thus no longer provide useful signal for incremental safety progress." (p.11)

"We further found that models could learn to hide their thinking while still misbehaving if their CoTs were directly pressured against having 'bad thoughts.'" (p.15)

"Safety is foundational to our approach to open models. They present a different risk profile than proprietary models: Once they are released, determined attackers could fine-tune them to bypass safety refusals or directly optimize for harm without the possibility for OpenAI to implement additional mitigations or to revoke access." (p.4)

## 11. UNKNOWN / not in extract

This arXiv version is substantively identical to the non-arXiv version (`OpenAI-gpt-oss-model-card`). Any gaps noted in that card apply equally here. The primary distinction is the arXiv identifier (arXiv:2508.10925v1) and submission date (August 8, 2025). Full deliberative alignment training details, Production Benchmarks dataset composition, adversarial fine-tuning hyperparameters, and CBRN filter specifics are not disclosed in either version.
