---
stem: "NVIDIA-SteerLM_Attribute_Conditioned_SFT"
company: "NVIDIA"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, design-space, validity-psychometrics, normative-ethics]
headline_numbers:
  - "STEERLM 43B achieves 104.2% of ChatGPT 3.5 performance on Vicuna benchmark (p.6)"
  - "STEERLM Elo rating 1139 vs. ChatGPT 3.5 at 1023 (automatic evaluation) (p.7)"
  - "Human evaluation: STEERLM 43B Elo 1040 vs. ChatGPT 3.5 at 981; Fleiss' κ = 0.46 (p.7)"
  - "STEERLM annotation cost ~10x lower than RLHF (1 rating vs. 6–36 pairwise comparisons per prompt) (p.13)"
  - "Attribute prediction model use improves performance by 4.6% over human annotations (p.8)"
  - "STEERLM 43B mean response length 1,906 chars vs. ChatGPT 3.5 at 1,193 chars (p.7)"
---

## 1. Gist

SteerLM (EMNLP 2023) proposes Attribute-Conditioned Supervised Fine-Tuning (ACSFT) as a simpler, cheaper, and more user-controllable alternative to RLHF for aligning language models. Rather than training a scalar reward model and using online RL, SteerLM trains the language model to condition its generation on a discrete attribute vector (quality, toxicity, humor, helpfulness, creativity, violence, inappropriateness) at both training and inference time. Users can then dial each attribute value at inference without retraining. The method uses a 4-step pipeline: (1) train an Attribute Prediction Model (LLM regression head) on Open Assistant; (2) use it to annotate larger datasets (e.g., HH-RLHF); (3) train the policy conditioned on predicted attributes; (4) bootstrap with high-quality self-generated samples. STEERLM 43B outperforms ChatGPT 3.5 on the Vicuna benchmark in both automatic (104.2%) and human (Elo 1040 vs. 981) evaluations, while requiring substantially less compute than RLHF.

## 2. Alignment/values methods used

- **Attribute-Conditioned SFT (ACSFT)**: Core alignment method. Trains the LLM to generate responses conditioned on a linearized attribute vector using standard language modeling loss only. No RL, no reward model training.
- **Attribute Prediction Model**: LLM fine-tuned to predict multi-dimensional attribute scores (quality:0–9, toxicity, humor, creativity, violence, helpfulness, inappropriateness) given a prompt-response pair. Used as a pseudo-reward model to annotate unlabeled data.
- **Bootstrapping (Step 4)**: Sample policy at high-quality attribute settings, re-annotate with Attribute Prediction Model, re-train. Analogous to RLHF's online improvement loop but fully offline.
- **No RLHF, PPO, or DPO** used for the primary SteerLM method.

## 3. Values specification

SteerLM operationalizes values as 7 named attributes (from Open Assistant dataset), scaled 0–9 at training:

- **Quality**: Overall response quality
- **Helpfulness**: How useful the response is
- **Toxicity**: Level of harmful/offensive content (can be steered high for specific use cases like NPCs)
- **Humor**: Comedy/levity level
- **Creativity**: Originality
- **Violence**: Explicit violent content
- **Inappropriateness**: Inappropriate content level

Attributes can be independently set at inference time. Default settings: quality=9, helpfulness=9, toxicity=0, humor=0, creativity=0, violence=0, inappropriateness=0. This operationalizes a nuanced value system where different use cases can call for different value profiles (e.g., a gaming NPC might warrant toxicity > 0). The ethics statement explicitly acknowledges that developers should control which attributes users can adjust (p.10).

## 4. Safety & values evaluation methodology

- **Perspective API**: Used to measure toxicity on Anthropic Red Team dataset (100 conversations, rank 4). STEERLM 43B at toxicity=0 scores 0.06346 vs. ChatGPT 3.5 at 0.06622 (p.8).
- **Human evaluation**: 12 volunteer annotators (university-level CS background); A/B forced choice; Fleiss' κ = 0.46 (p.6–7). Notably higher than crowd-worker studies (cited) due to screened annotators.
- **GPT-4 automatic evaluation** (Vicuna benchmark): Position bias mitigated by averaging across both response orderings (p.6).
- **Steerability demos**: Qualitative tests of toxicity and humor attributes across discrete settings (p.8–9).
- No third-party audits or red-teaming beyond the toxicity steerability demo.

## 5. Benchmarks used or introduced

- **Vicuna Benchmark** (Chiang et al., 2023): 80 single-turn diverse prompts; GPT-4-as-judge scores 1–10; primary evaluation benchmark (p.5–6).
- **Anthropic Red Team Dataset** (Ganguli et al., 2022): 100 high-ranked harmful conversations; used to measure toxicity control (p.8).
- **Perspective API**: External toxicity classifier from Google; measures toxicity of model outputs (p.8).
- No new benchmark introduced; SteerLM itself is introduced as an alignment method.

## 6. Agentic / multiturn evaluation aspects

The Vicuna benchmark used is single-turn. Open Assistant training data includes multi-turn conversations (conversation trees), so the model is trained on multi-turn data implicitly. The Model Self-Identification Dataset (M-SID, 910 samples) covers identity questions ("Who are you?") relevant to persona consistency across turns (p.5). No explicit agentic or long-horizon evaluation conducted.

## 7. Key numbers

- STEERLM 43B: 104.2% of ChatGPT 3.5 on Vicuna benchmark; Elo 1139 (auto), 1040 (human) (p.6–7)
- ChatGPT 3.5 Elo: 1023 (auto), 981 (human) (p.7)
- Guanaco 65B (larger model): 102.4% of ChatGPT 3.5; Elo 1065 auto, 977 human (p.6–7)
- STEERLM 43B human win rate vs. ChatGPT 3.5: 59% (p.7)
- Human Fleiss' κ = 0.46 (p.6)
- Annotation cost: RLHF requires 6–36 pairwise comparisons per prompt vs. SteerLM 1 rating (p.13)
- Attribute prediction model use: +4.6% improvement over using raw human annotations (p.8)
- Adding HH-RLHF data: +1.0% performance (p.8)
- Bootstrapping with high-quality samples: +0.5% performance (p.8)
- STEERLM 43B mean response: 1,906 chars, 144 unique words vs. ChatGPT 3.5: 1,193 chars, 77 unique words (p.14)
- Toxicity scores at different settings: toxicity=0: 0.06346; toxicity=9: 0.10408; ChatGPT 3.5: 0.06622 (p.8)
- Training: 16 A100-DGX nodes (128 A100-80GB GPUs), 5 epochs, batch size 128, max seq 4096 tokens (p.5)

## 8. Findings relevant to values-benchmark design

- **Single-dimensional reward is insufficient**: RLHF with a scalar reward fails to capture multifaceted human preferences. SteerLM's success suggests that named, decompositional value attributes are more informative than a single preference score (p.1–2).
- **Attribute prediction model denoises human annotation noise**: Using the model's predicted attributes (rather than raw human labels) improved performance by 4.6% (p.8). This has implications for benchmark construction: model-in-the-loop re-annotation can improve label quality over raw crowdsourcing.
- **GPT-4 auto-evaluation favors length and vocabulary**: STEERLM 43B's longer responses (1,906 chars vs. ChatGPT's 1,193) likely inflate its automatic evaluation scores. The 74-Elo gap on automatic evaluation narrows to 59 on human evaluation (p.7). Values benchmarks relying on LLM judges should control for or penalize length.
- **Bootstrapping with quality-maximized samples**: Generating responses with high attribute targets and then retraining improves performance. This suggests iterative self-improvement can surface latent model capabilities without new human data.
- **Attribute steerability at inference as a benchmark property**: A model's ability to modulate attribute outputs (e.g., reduce toxicity, increase humor on command) is a measurable property distinct from average response quality. Benchmark items could test control compliance.
- **Ethics of controllable toxicity**: NVIDIA explicitly acknowledges that allowing users to set high-toxicity outputs has legitimate use cases (NPCs, red-teaming) but malicious uses are possible. This raises design questions for any benchmark that evaluates "values compliance"—compliance with whom and in what context?

## 9. Novel ideas worth stealing

1. **Conditional generation as values alignment**: Format a benchmark's "ideal response" as a vector of named attribute values (quality=4, helpfulness=4, toxicity=0, complexity=2). Evaluate models' ability to comply with this specification on demand.
2. **Attribute prediction model for dataset annotation**: Train a regression head on expert-labeled data, then use it to cheaply annotate large unlabeled datasets. Applicable to scaling values annotation to millions of samples.
3. **10x annotation cost reduction via absolute rating vs. pairwise comparison**: For benchmark construction, absolute rating (1 annotation per sample) is far cheaper than pairwise comparison (6–36 per prompt). Document this tradeoff explicitly in benchmark design docs.
4. **Toxicity steerability as a safety evaluation**: Test whether models can generate appropriately low-toxicity output on demand (and whether they can generate targeted high-toxicity output when legitimately asked). Measures fine-grained values compliance rather than blanket safety.
5. **Volunteer annotators vs. crowd workers for human eval**: Fleiss' κ = 0.46 with CS-educated volunteers substantially exceeds typical crowd-worker agreement rates. Budget for qualified annotators in benchmark validation.

## 10. Notable quotes

- "RLHF treats human preference of model responses as mono-dimensional without regard for the diversity of aspects (e.g. helpfulness, humor, toxicity) that contribute to such preferences and thereby limiting users' ability to adjust individual aspects at inference time based on their use cases." (p.1)
- "In general, we believe that giving developers explicit control over model's value system is preferred to dictating one that they can not adjust." (p.10)
- "Automatic evaluation with GPT-4 has a tendency to prefer longer responses that have more unique tokens... STEERLM 43B responses satisfy both criteria and this might lead to GPT-4 rating its responses higher than other counterparts." (p.7)
- "Utilizing predictions from the Attribute Prediction model for the Attribute Conditioned SFT process provides a substantial benefit to STEERLM 43B amounting to 4.6% in performance, relative to using human annotations." (p.8)

## 11. UNKNOWN / not in extract

- Inter-rater reliability statistics for the Open Assistant attribute annotations used to train the Attribute Prediction Model.
- Whether the Attribute Prediction Model transfers well to non-English data or non-Western cultural contexts.
- Detailed failure analysis: types of prompts where STEERLM underperforms ChatGPT.
- How attribute conditioning affects reasoning and factual accuracy (no TruthfulQA results in this paper; those appear in the HelpSteer paper).
- Long-term model behavior under extreme attribute settings (e.g., creativity=9 + toxicity=0).
