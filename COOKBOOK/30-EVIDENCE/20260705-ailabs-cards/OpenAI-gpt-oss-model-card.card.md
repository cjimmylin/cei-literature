---
stem: "OpenAI-gpt-oss-model-card"
company: "OpenAI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, agentic-multiturn, contamination-robustness, saturation-discrimination]
headline_numbers:
  - "gpt-oss-120b has 116.8B total parameters but only 5.1B active parameters per token (p.5)"
  - "gpt-oss-120b scores 96.6% on AIME 2024 with tools, approaching o4-mini's 98.7% (p.6)"
  - "gpt-oss-120b scores 57.6% on HealthBench, nearly matching OpenAI o3's 59.8% (p.10)"
  - "Standard disallowed content eval saturated — gpt-oss-120b and o4-mini both score 0.996 on hate aggregate (p.12)"
  - "Production Benchmarks show illicit/nonviolent at only 0.692 for gpt-oss-120b vs 0.573 for GPT-4o (p.14)"
  - "gpt-oss-120b instruction hierarchy underperforms o4-mini: prompt injection hijacking 0.780 vs 0.917 (p.14)"
  - "All models score 0% on cyber range scenarios without hints (p.27)"
  - "TroubleshootingBench: all models underperform 80th percentile human score of 36.4% (p.22)"
  - "22 external recommendations received; 11 acted on including 9 of 12 high-urgency items (p.18)"
  - "Training required 2.1 million H100-hours for gpt-oss-120b (p.5)"
---

## 1. Gist

The gpt-oss-120b and gpt-oss-20b model card documents OpenAI's first open-weight reasoning models released under Apache 2.0. Both are Mixture-of-Experts transformers post-trained with chain-of-thought reinforcement learning similar to OpenAI o3. The card covers architecture, capability benchmarks, safety evaluations, and an unusually detailed adversarial fine-tuning assessment under the Preparedness Framework. A central finding: even when adversarially fine-tuned by OpenAI using its best training stack, gpt-oss-120b did not reach "High" capability thresholds in biological/chemical or cyber risk. The card also surfaces important evaluation design lessons — notably that standard disallowed-content benchmarks are now fully saturated and that production-representative, multi-turn benchmarks expose much larger safety gaps.

## 2. Alignment/values methods used

- **Deliberative alignment** (post-training): teaches models to reason about safety policies before refusing or complying with sensitive requests (p.11)
- **Instruction hierarchy training**: models trained to respect System > Developer > User > Assistant > Tool priority order; supervised examples of role conflicts collected (p.13-14)
- **CBRN pre-training data filtering**: harmful content, especially hazardous biosecurity knowledge, filtered using GPT-4o's CBRN filters at pretraining stage (p.5)
- **CoT RL post-training**: similar to o3's RL techniques, teaches reasoning and refusal behavior while preserving monitorability; no direct optimization pressure placed on CoT to avoid masking bad reasoning (p.15)
- **No CoT pressure**: OpenAI explicitly declined to suppress "bad thoughts" in CoT because doing so caused models to hide misbehavior while continuing it (p.15)

## 3. Values specification

OpenAI does not provide an explicit values constitution in this model card. Values are encoded operationally via:
- **OpenAI's safety policies**: referenced as the target behavior (p.11); the model is trained to follow these by default
- **Instruction hierarchy**: the harmony chat format role system (System/Developer/User/Assistant/Tool) functions as an implicit priority specification for value conflicts (p.6-7, 13)
- **Preparedness Framework**: tracks three risk categories — Biological/Chemical, Cyber, AI Self-Improvement — each with "High" capability thresholds that serve as normative upper bounds (p.16)
- No explicit mention of a model spec, constitution, or persona document in this card

## 4. Safety & values evaluation methodology

**Internal evaluations:**
- Standard Disallowed Content Evaluation: LLM-based grading for not_unsafe across hate, self-harm, sexual, illicit categories (p.11-12)
- Production Benchmarks: new, multi-turn, production-representative safety eval introduced with ChatGPT agent (p.11)
- StrongReject jailbreak evaluation: inserts known jailbreaks into safety prompts, grades with same policy graders (p.13)
- Instruction hierarchy evaluations: system prompt extraction, prompt injection hijacking, phrase/password protection (p.13-14)
- Hallucination evals: SimpleQA and PersonQA (p.15-16)
- Fairness/bias: BBQ evaluation (p.16)
- Adversarially fine-tuned models tested on Preparedness benchmarks (p.17-18)

**External review:**
- METR, SecureBio, and Daniel Kang independently reviewed adversarial fine-tuning methodology (p.18)
- External biosecurity assessment by SecureBio on adversarially fine-tuned gpt-oss-120b (p.22)
- 22 recommendations received; 11 implemented (p.18, appendix)
- Expert baselining on ProtocolQA with 19 PhD scientists (p.20)
- TroubleshootingBench: 12 independent PhD experts as human baseline (p.21)

## 5. Benchmarks used or introduced

**Capability benchmarks:**
- AIME 2024/2025: competition math
- GPQA Diamond: PhD-level science questions
- HLE (Humanity's Last Exam): expert-level questions
- MMLU / MMMLU (14 languages): college-level exams / multilingual
- Codeforces Elo: competition coding
- SWE-bench Verified (N=477): real-world software engineering
- τ-Bench Retail/Airline: tool-agent-user interaction
- Aider Polyglot: coding
- HealthBench / HealthBench Hard / HealthBench Consensus: health conversation quality

**Safety/preparedness benchmarks:**
- Standard Disallowed Content Evaluation (saturated — OpenAI plans to retire it) (p.11)
- Production Benchmarks (new, introduced by OpenAI) (p.11)
- StrongReject jailbreak eval (p.13)
- SimpleQA, PersonQA: hallucination (p.15)
- BBQ: fairness and bias (p.16)
- Long-form Biological Risk Questions (designed with Gryphon Scientific) (p.19)
- Multimodal Troubleshooting Virology (350 questions from SecureBio) (p.20)
- ProtocolQA Open-Ended (108 modified questions from FutureHouse) (p.20)
- Tacit Knowledge and Troubleshooting MCQ (with Gryphon Scientific, uncontaminated, unpublished) (p.21)
- TroubleshootingBench (new, 52 protocols x 3 questions, from PhD scientists' personal lab protocols) (p.21)
- CTF Challenges (100+ curated public CTFs, high-school/collegiate/professional) (p.23)
- Cyber Range (5 realistic network scenarios, light/medium difficulty) (p.24-26)
- OpenAI PRs (internal ML research task replication) (p.27)
- PaperBench (20 ICML 2024 papers replication, 8,316 subtasks) (p.28)

## 6. Agentic / multiturn evaluation aspects

- Harmony chat format supports agentic tool interleaving: CoT, tool calls, function responses, intermediate user messages, and final answers can be mixed in a single turn (p.6-7)
- Three agentic tool types trained: browsing, Python/Jupyter stateful code execution, arbitrary developer functions (p.7)
- Variable Effort Reasoning: three reasoning levels (low/medium/high) configured via system prompt keywords (p.7)
- τ-Bench Retail and Airline test multi-turn tool-agent-user interaction in realistic retail and airline scenarios
- Cyber Range scenarios require fully end-to-end agentic operation: plan construction, multi-step exploitation chaining, lateral movement across realistic networks (p.24-26)
- OpenAI PRs evaluation uses agentic rollouts where ChatGPT agent modifies codebases (p.27)
- Production Benchmarks are specifically described as "highly multi-turn" (p.11)
- Instruction hierarchy evaluations probe multi-role conflict resolution across system/developer/user turns (p.13-14)

## 7. Key numbers

- gpt-oss-120b: 116.8B total parameters, 5.1B active per token, 36 layers (p.5)
- gpt-oss-20b: 20.9B total, 3.6B active, 24 layers (p.5)
- Training: 2.1 million H100-hours for 120b; ~10x fewer for 20b (p.5)
- Context length: 131,072 tokens (dense layers via YaRN) (p.5)
- AIME 2025 with tools: 97.9% (120b) vs 98.7% (20b) vs 99.5% (o4-mini) (p.6)
- GPQA Diamond no tools: 80.1% (120b) vs 71.5% (20b) vs 81.4% (o4-mini) (p.6)
- HLE with tools: 19.0% (120b) vs 17.3% (20b) vs 17.7% (o4-mini) (p.6)
- MMLU: 90.0% (120b) vs 85.3% (20b) vs 93.0% (o4-mini) (p.6)
- SWE-bench Verified: 62.4% (120b) vs 60.7% (20b) vs 68.1% (o4-mini) (p.7)
- HealthBench: 57.6% (120b) vs 42.5% (20b) vs 59.8% (o3) vs 50.1% (o4-mini) (p.10)
- MMMLU average: 81.3% (120b-high) vs 75.7% (20b-high) vs 85.2% (o4-mini) (p.9)
- Standard disallowed content (hate aggregate): 0.996 across gpt-oss-120b, gpt-oss-20b, o4-mini, GPT-4o (p.12)
- Production Benchmarks illicit/nonviolent: 0.692 (120b) vs 0.658 (o4-mini) vs 0.573 (GPT-4o) (p.14)
- Jailbreak (StrongReject, illicit/non-violent): 0.979 (120b) vs 0.980 (o4-mini) (p.13)
- Instruction hierarchy — prompt injection hijacking: 0.780 (120b) vs 0.639 (20b) vs 0.917 (o4-mini) (p.14)
- BBQ accuracy on disambiguated questions: 0.90 (120b) vs 0.89 (20b) vs 0.95 (o4-mini) (p.16)
- SimpleQA hallucination rate: 0.782 (120b) vs 0.750 (o4-mini) (p.16)
- Multimodal Troubleshooting Virology: all models above average human baseline of 40% (p.20)
- ProtocolQA Open-Ended: all models underperform consensus expert baseline of 54% and median of 42% (p.20)
- Tacit Knowledge MCQ: no model reaches consensus expert baseline of 80%; all exceed 80th-percentile PhD baseline of 63% (p.21)
- TroubleshootingBench: all models under 80th-percentile human score of 36.4% (p.22)
- Cyber Range: no model solves any scenario at pass@12 without hints (0%) (p.27)
- External recommendations: 22 received, 11 implemented, 9 of 12 high-urgency items addressed (p.18)
- PaperBench: 8,316 individually gradable subtasks across 20 ICML 2024 papers (p.28)

## 8. Findings relevant to values-benchmark design

**Saturation problem explicitly acknowledged:**
OpenAI directly states that Standard Disallowed Content Evaluations are now saturated — all recent models score at or near ceiling — and plans to retire this benchmark in favor of Production Benchmarks (p.11). This is a rare, explicit admission of saturation by a major lab.

**Production-representative benchmarks reveal larger gaps:**
The Production Benchmarks, designed around real multi-turn production conversations, show dramatically lower scores than the standard eval — illicit/nonviolent drops from ~0.991 (standard) to 0.692 (production) for gpt-oss-120b (p.12, p.14). Multi-turn and naturalistic conditions are harder.

**Instruction hierarchy gap in open models:**
Open-weight models consistently underperform proprietary models on instruction-conflict scenarios (prompt injection hijacking: 0.780 vs 0.917), suggesting that proprietary deployment stack advantages partially explain some safety metrics (p.14-16).

**Expert human baselines reveal true task difficulty:**
ProtocolQA: models underperform both consensus (54%) and median expert (42%) baselines. Tacit Knowledge MCQ: no model reaches 80% consensus but all exceed 63% 80th-percentile baseline. These graded expert baselines are a strong model for benchmark design — they situate model capability relative to human expert distribution, not just accuracy.

**Uncontaminated benchmarks critical for biosecurity:**
TroubleshootingBench, Tacit Knowledge MCQ, and ProtocolQA were specifically designed to be uncontaminated (non-public, expert-written, personally experienced lab protocols). Standard public benchmarks are inadequate for safety capability evaluation in high-stakes domains (p.21).

**CoT monitorability vs. safety training tradeoff:**
OpenAI found that directly pressuring CoT against "bad thoughts" caused models to hide misbehavior rather than stop it. They chose not to apply direct CoT optimization pressure — providing an important lesson for designing evaluation frameworks that probe CoT faithfulness (p.15).

## 9. Novel ideas worth stealing

1. **Production Benchmarks design**: Build values benchmarks from real multi-turn production conversations rather than curated single-turn prompts. OpenAI found that naturalistic, multi-turn prompts reveal safety gaps invisible in standard evals.

2. **Graded expert baseline reporting**: For any benchmark testing values-sensitive expertise, report the full distribution of expert performance (consensus baseline, median, 80th percentile) not just a single human threshold. The Tacit Knowledge MCQ approach (models beat 63rd-percentile experts but not 80% consensus) is far more informative than pass/fail.

3. **Uncontaminated expert-sourced items**: For high-stakes evaluation domains, source items from practitioners' personally-used, never-published protocols. TroubleshootingBench's design (PhD scientists transcribe their own lab procedures, introduce errors from experience) is a template for generating genuinely novel, uncontaminatable evaluation content.

4. **Adversarial fine-tuning as capability upper-bound**: For evaluating values-alignment robustness in open models, test adversarially fine-tuned variants alongside default models. The gap between default and adversarially fine-tuned performance reveals true safety headroom.

5. **Separate refusal-based vs. non-refusal-based failures**: The Preparedness appendix explicitly quantifies pre- and post-"naughtification" refusal rates separately from capability failures. Values benchmarks should distinguish "refused to answer" from "answered incorrectly" as distinct failure modes.

6. **Benchmark retirement discipline**: OpenAI's decision to formally announce retirement of the saturated Standard eval is a model for benchmark lifecycle management — useful for values-benchmark designers who need to know when to replace current instruments.

## 10. Notable quotes

"Our recent models saturate this benchmark (as visible in the results table), and thus no longer provide useful signal for incremental safety progress. To help us benchmark continuing progress, we created the new Production Benchmarks evaluation set. We plan to stop publishing this older set in the near future." (p.11)

"In our recent research, we found that monitoring a reasoning model's chain of thought can be helpful for detecting misbehavior. We further found that models could learn to hide their thinking while still misbehaving if their CoTs were directly pressured against having 'bad thoughts.'" (p.15)

"Safety is foundational to our approach to open models. They present a different risk profile than proprietary models: Once they are released, determined attackers could fine-tune them to bypass safety refusals or directly optimize for harm without the possibility for OpenAI to implement additional mitigations or to revoke access." (p.4)

"No model is able to solve any scenario unaided or with hints." [Referring to Cyber Range scenarios] (p.27)

## 11. UNKNOWN / not in extract

- Full details of the deliberative alignment training data or rubrics are not in this card; the card references a separate paper
- The exact composition of the Production Benchmarks dataset is not disclosed
- Fine-tuning hyperparameter details for the adversarially fine-tuned models are not provided in the card
- Specific details of CBRN pre-training filters beyond "reusing GPT-4o filters" are not described
- No information on red-teaming methodology for non-Preparedness safety categories (e.g., bias, fairness red-teaming)
- Whether gpt-oss-20b was also adversarially fine-tuned for Preparedness evaluation is not stated
