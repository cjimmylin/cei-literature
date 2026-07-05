---
stem: "Alibaba (Qwen)-Qwen3_Technical_Report_2505.09388"
company: "Alibaba (Qwen)"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, design-space, agentic-multiturn, cultural-linguistic]
headline_numbers:
  - "Qwen3-235B-A22B scores 85.7 on AIME'24 and 81.5 on AIME'25 (p.3)"
  - "Qwen3-235B-A22B achieves CodeForces rating 2056 / 98.2 percentile (p.14)"
  - "Qwen3-235B-A22B scores 70.8 on BFCL v3 and 70.7 on LiveCodeBench v5 (p.3)"
  - "Pre-training data: 36 trillion tokens across 119 languages and dialects (p.2)"
  - "Multilingual annotation applied to over 30 trillion tokens across multiple dimensions (p.4)"
  - "Strong-to-Weak Distillation requires only 1/10 of GPU hours vs. four-stage training (p.10)"
  - "AIME'24 score of Qwen3-235B-A22B increased from 70.1 to 85.1 over 170 RL training steps (p.11)"
  - "General RL reward system covers over 20 distinct tasks (p.12)"
---

## 1. Gist

The Qwen3 Technical Report presents Alibaba's Qwen3 model family, comprising 8 models (6 dense + 2 MoE) ranging from 0.6B to 235B parameters. The flagship is Qwen3-235B-A22B, a MoE model with 235B total and 22B activated parameters. The central architectural innovation is a unified "thinking/non-thinking" mode that allows dynamic switching within a single model between slow deliberate reasoning (Chain-of-Thought) and fast response, eliminating the need for separate chat-optimized and reasoning models. A thinking budget mechanism allows users to cap the number of thinking tokens. The post-training pipeline follows four stages: Long-CoT Cold Start, Reasoning RL (GRPO), Thinking Mode Fusion (SFT), and General RL. Lightweight models (0.6B–14B dense + 30B-A3B MoE) are trained via Strong-to-Weak Distillation rather than full four-stage training. Qwen3 expands multilingual support from 29 (Qwen2.5) to 119 languages. All models are released open-weight under Apache 2.0.

## 2. Alignment/values methods used

The report describes alignment primarily through its General RL stage (Stage 4 of post-training). Three reward types are used:

1. **Rule-based reward**: Used for instruction following and format adherence. The report notes well-designed rule-based rewards prevent reward hacking (p.12).
2. **Model-based reward with reference answer**: A judge model (Qwen2.5-72B-Instruct) scores model responses against a reference answer, allowing flexible handling of diverse tasks without strict formatting requirements (p.12).
3. **Model-based reward without reference answer**: A trained reward model using human preference data assigns scalar scores without requiring a reference answer; handles broader query types and improves helpfulness and engagement (p.12).

The General RL stage targets five capability clusters: Instruction Following, Format Following, Preference Alignment (helpfulness, engagement, style), Agent Ability (multi-turn tool use with real environment feedback), and Abilities for Specialized Scenarios (e.g., RAG hallucination minimization). No constitutional AI approach, RLHF with explicit human labeling pipeline, or DPO is described. The "preference alignment" component is characterized as improving naturalness and user satisfaction on open-ended queries.

## 3. Values specification

The report provides **no explicit values specification document**, model spec, or stated ethical principles. The term "preference alignment" is used to cover helpfulness, engagement, and style (p.12), but no formal value hierarchy or policy framework is described. The closest analogue is the checklist-based quality assessment for "non-thinking" SFT data (p.11), which evaluates response quality across coding, mathematics, instruction-following, multilingual tasks, creative writing, question answering, and role-playing, but without normative ethical content. The training data annotation system rates content across dimensions including "safety" (p.4), but no details are given on how safety labels are defined or used downstream.

## 4. Safety & values evaluation methodology

The report **does not describe safety evaluations** in any dedicated section. No red-teaming, adversarial testing, harm rate measurements, refusal evaluations, or third-party audits are mentioned. The evaluation suite for post-trained models (Section 4.6) covers: General Tasks (MMLU-Redux, GPQA-Diamond, C-Eval, LiveBench), Alignment Tasks (IFEval, Arena-Hard, AlignBench v1.1, Creative Writing v3, WritingBench), Math & Text Reasoning (MATH-500, AIME, ZebraLogic, AutoLogi), Agent & Coding (BFCL v3, LiveCodeBench, CodeForces), and Multilingual Tasks (Multi-IF, INCLUDE, MMMLU, MT-AIME2024, PolyMath, MLogiQA). Safety and values evals are absent. The "alignment tasks" category measures instruction-following accuracy and human preference scores (Arena-Hard, AlignBench) but not harm avoidance.

## 5. Benchmarks used or introduced

**Used (pre-training evaluation):** MMLU (5-shot), MMLU-Pro (5-shot, CoT), MMLU-redux (5-shot), BBH (3-shot, CoT), SuperGPQA (5-shot, CoT), GPQA (5-shot, CoT), GSM8K (4-shot, CoT), MATH (4-shot, CoT), EvalPlus (HumanEval + MBPP + variants), MultiPL-E (8 languages), MBPP-3shot, CRUXEval CRUX-O (1-shot), MGSM (8-shot, CoT), MMMLU (5-shot), INCLUDE (5-shot).

**Used (post-training evaluation):**
- MMLU-Redux — general knowledge
- GPQA-Diamond — graduate-level science reasoning (sampled 10× per query, averaged)
- C-Eval — Chinese evaluation suite
- LiveBench (2024-11-25) — contamination-free live benchmark
- IFEval (strict prompt accuracy) — instruction following
- Arena-Hard — LLM-judge preference benchmark against GPT-4 baseline
- AlignBench v1.1 — Chinese alignment benchmark
- Creative Writing V3 — creative writing quality
- WritingBench — generative writing
- MATH-500 — mathematical reasoning
- AIME'24 and AIME'25 — competition math (64 samples per question, averaged)
- ZebraLogic — logical reasoning
- AutoLogi — logic puzzle reasoning
- BFCL v3 — function calling / tool use
- LiveCodeBench v5 (2024.10–2025.02) — live code benchmark
- CodeForces / CodeElo — competitive programming (Elo rating)
- Multi-IF — multilingual instruction following (8 languages)
- INCLUDE — regional knowledge (44 languages)
- MMMLU — multilingual MMLU (14 languages)
- MT-AIME2024 — multilingual AIME (55 languages)
- PolyMath — multilingual math (18 languages)
- MLogiQA — multilingual logical reasoning (10 languages)
- RULER — long-context retrieval
- Belebele — multilingual reading comprehension (80 languages)

**No new benchmarks introduced** by this report.

## 6. Agentic / multiturn evaluation aspects

Agent capability receives direct treatment in General RL Stage 4: "During the RL rollout, the model is allowed to perform complete multi-turn interaction cycles with real environment execution feedback, thereby improving its performance and stability in long-horizon decision-making tasks" (p.12). This constitutes online multi-turn RL with real tool/environment calls, not just static trajectory scoring.

BFCL v3 is the primary agentic benchmark; multi-turn evaluation within BFCL uses yarn-deployed 64k context windows (p.13). The /think and /no-think mode flags can appear multiple times in multi-turn dialogs, with the model following the last flag encountered (p.11). For complex multi-turn dialogs, the chat template randomly inserts multiple /think and /no-think flags during training (p.11), which is a form of multi-turn instruction-following training.

LiveCodeBench evaluations adjust prompts in thinking mode to allow freer reasoning by removing the "only return code" restriction (p.13), suggesting evaluation protocols need to be mode-aware.

## 7. Key numbers

- Pre-training corpus: ~36 trillion tokens, 119 languages (p.2)
- Pre-training Stage 1 (general): >30 trillion tokens, 4K sequence length (p.4)
- Pre-training Stage 2 (reasoning): ~5 trillion higher-quality tokens (p.4)
- Multilingual annotation: >30 trillion tokens annotated for educational value, fields, domains, safety (p.4)
- Reasoning RL: 3,995 query-verifier pairs, trained with GRPO (p.10)
- Reasoning RL training steps (flagship): 170 steps; AIME'24 improved from 70.1 to 85.1 (p.11)
- Strong-to-Weak Distillation efficiency: requires only 1/10 GPU hours vs. full four-stage training (p.10)
- General RL reward system: >20 distinct tasks (p.12)
- Flagship model: 235B total parameters, 22B activated, 94 layers, 64/4 attention heads, 128 experts (8 activated), 128K context (p.3, Table 2)
- AIME'24 (thinking): 85.7 vs. DeepSeek-R1 79.8, o1 74.3, Gemini2.5-Pro 92.0 (p.14, Table 11)
- AIME'25 (thinking): 81.5 vs. DeepSeek-R1 70.0, o1 79.2, Gemini2.5-Pro 86.7 (p.14, Table 11)
- CodeForces rating: 2056 / 98.2% vs. DeepSeek-R1 2029 / 98.1%, o1 1891 / 96.7% (p.14, Table 11)
- Arena-Hard (non-thinking): 96.1 vs. GPT-4o 85.3, DeepSeek-V3 85.5 (p.14, Table 12)
- BFCL v3 (thinking): 70.8 vs. o1 67.8, DeepSeek-R1 56.9, Gemini2.5-Pro 62.9 (p.14, Table 11)
- LiveCodeBench v5 (thinking): 70.7 vs. o1 63.9, Gemini2.5-Pro 70.4 (p.14, Table 11)
- Qwen3-32B AIME'24 (thinking): 81.4, outperforms QwQ-32B 79.5 and o3-mini (medium) 79.6 (p.16, Table 13)
- Belebele (Qwen3-32B thinking, Indo-European): 90.7 (p.30, Table 37)

## 8. Findings relevant to values-benchmark design

**No values-alignment ceiling effects studied.** The report treats alignment benchmarks (IFEval, Arena-Hard, AlignBench, Creative Writing, WritingBench) as performance metrics without analysis of saturation, ceiling effects, or construct validity. Several admitted gaps:

1. **Long-context thinking degradation**: "In thinking mode, the model's performance slightly degrades [on RULER]. We hypothesize that the thinking content does not provide significant benefits for these retrieval tasks... and may instead interfere with the retrieval process" (p.23). This suggests mode-specific eval design matters — thinking mode is not uniformly beneficial.

2. **Evaluation efficiency compromise**: For multilingual benchmarks INCLUDE and MMMLU, "we sample only 10% of the original data to improve evaluation efficiency" (p.13). This is a methodological shortcut that may affect reliability, especially for low-resource languages.

3. **AIME sampling**: 64 samples per question with averaged accuracy. This reduces variance but obscures whether correct answers reflect understanding vs. stochastic coverage (pass@64 treated as expected accuracy).

4. **Alignment tasks gap**: No safety, harm-avoidance, or ethical values benchmarks appear anywhere. The "Alignment Tasks" category is entirely about instruction compliance and human preference for helpfulness/style, not normative values.

5. **Multilingual math gap**: MT-AIME2024 covers 55 languages for competition math — a useful model for designing multilingual values benchmarks that span diverse language communities.

6. **Mode-awareness requirement**: Evaluation protocols for thinking-capable models must specify whether thinking mode is enabled and what token budget is set, as these choices substantially affect scores (e.g., LiveCodeBench prompt is adjusted for thinking mode, p.13).

## 9. Novel ideas worth stealing

1. **Thinking budget as a values-alignment lever**: The thinking budget mechanism (p.11) provides a controllable compute dial. For values benchmarks, one could systematically vary thinking budget to study whether extended reasoning improves or degrades value alignment on complex ethical dilemmas — a form of "moral compute scaling."

2. **Multi-turn mode-switching in evaluation**: The training of multi-turn dialogs with randomly inserted /think and /no-think flags (p.11) suggests an evaluation protocol: present multi-turn moral vignettes where the system prompt instructs different reasoning modes, and measure consistency across modes.

3. **Multilingual math as a template**: The MT-AIME2024 benchmark (55 languages) and PolyMath (18 languages) provide a model for constructing a multilingual values benchmark covering diverse language communities. The language-stratified results tables (Tables 24–35) demonstrate how to report per-language results systematically.

4. **Instance-level data mixture optimization**: The report describes optimizing data mixture at the instance level (not source/domain level) using fine-grained labels from a multilingual annotation system (p.4). For values benchmarks, this implies annotating individual items for cultural/linguistic provenance and difficulty rather than relying on corpus-level demographics.

5. **Dual Pass@1 and Pass@64 tracking**: The distillation section mentions that Strong-to-Weak Distillation improves both Pass@1 (immediate performance) and Pass@64 (exploration potential) (p.10). For values benchmarks, measuring both single-attempt scores and consensus-over-samples would distinguish reliable alignment from lucky outputs.

6. **Online RL with real environment feedback for agent evals**: Multi-turn agent RL using real tool-call feedback (p.12) sets a standard that static agentic values benchmarks may not capture — evaluating values in agentic contexts may require live execution environments rather than scripted trajectories.

## 10. Notable quotes

"The General RL stage aims to broadly enhance the models' capabilities and stability across diverse scenarios. To facilitate this, we have established a sophisticated reward system covering over 20 distinct tasks, each with customized scoring criteria." (p.12)

"Preference Alignment: For open-ended queries, preference alignment focuses on improving the model's helpfulness, engagement, and style, ultimately delivering a more natural and satisfying user experience." (p.12)

"In thinking mode, the model's performance slightly degrades [on long-context retrieval]. We hypothesize that the thinking content does not provide significant benefits for these retrieval tasks, which do not rely on reasoning and may instead interfere with the retrieval process. We are committed to enhancing the long-context capability in the thinking mode in future versions." (p.23)

"Distillation from advanced teacher models significantly outperforms reinforcement learning in performance and training efficiency." (p.2)

## 11. UNKNOWN / not in extract

- No safety evaluation methodology described (red-teaming, harm rates, refusal benchmarks, TruthfulQA, BBQ, WinoBias, etc.)
- No model spec, policy document, or ethical framework referenced
- No constitutional AI or similar normative constraint mechanism described
- No information on RLHF from human labelers (human preference data collection process for reward model training is not described)
- No third-party audits or external safety reviews mentioned
- No data on model behavior on sensitive topics, hate speech, or politically contested content
- No information on demographic bias evaluations
- No details on how "safety" dimension in the multilingual annotation system is defined or operationalized (p.4 mentions it as one of several annotation dimensions but provides no elaboration)
- Unclear whether the General RL reward model was trained on proprietary preference data or external datasets
- No information on deployment safety guardrails, system prompt restrictions, or post-deployment monitoring
