# Anthropic Research Papers

This directory contains Anthropic's foundational research papers and technical reports.

## Foundational Papers (2021-2022)

| Paper | arXiv | Year | Description |
|-------|-------|------|-------------|
| [A General Language Assistant as a Laboratory for Alignment](A_General_Language_Assistant_as_a_Laboratory_for_Alignment_2112.00861.pdf) | [2112.00861](https://arxiv.org/abs/2112.00861) | 2021 | Explores baseline techniques for alignment including prompting, imitation learning, and preference modeling |
| [Training a Helpful and Harmless Assistant with RLHF](Training_a_Helpful_and_Harmless_Assistant_with_RLHF_2204.05862.pdf) | [2204.05862](https://arxiv.org/abs/2204.05862) | 2022 | Details the RLHF training methodology for creating helpful and harmless AI assistants |
| [Constitutional AI: Harmlessness from AI Feedback](Constitutional_AI_Harmlessness_from_AI_Feedback_2212.08073.pdf) | [2212.08073](https://arxiv.org/abs/2212.08073) | 2022 | Introduces Constitutional AI (CAI) and RLAIF - the foundational training methodology for Claude models |
| [Discovering Latent Knowledge in Language Models](Discovering_Latent_Knowledge_in_Language_Models_2212.03827.pdf) | [2212.03827](https://arxiv.org/abs/2212.03827) | 2022 | Research on extracting latent knowledge from language models |

## Interpretability & Mechanistic Understanding (2022-2024)

| Paper | arXiv/Source | Year | Description |
|-------|--------------|------|-------------|
| [Toy Models of Superposition](Toy_Models_of_Superposition_2022.pdf) | [Alignment Forum](https://www.alignmentforum.org/posts/z6QQJbtpkEAX3Aojj/interim-research-report-taking-features-out-of-superposition) | 2022 | Foundational work on superposition in neural networks |
| [Towards Monosemanticity: Decomposing LMs with Autoencoders](Towards_Monosemanticity_Decomposing_LMs_Autoencoders.pdf) | [Anthropic](https://transformer-circuits.pub/2023/monosemantic-features/index.html) | 2023 | Advances in decomposing language models to find interpretable features |
| [Scaling Monosemanticity: Features in Claude 3 Sonnet](Scaling_Monosemanticity_Features_in_Claude_3_Sonnet_2024.pdf) | [Anthropic](https://www.anthropic.com/research/mapping-mind-language-model) | 2024 | Scaling interpretability techniques to production models |

## Alignment & Safety Research (2023-2024)

| Paper | arXiv | Year | Description |
|-------|-------|------|-------------|
| [The Capacity for Moral Self-Correction in LLMs](The_Capacity_for_Moral_Self-Correction_in_LLMs_2302.07459.pdf) | [2302.07459](https://arxiv.org/abs/2302.07459) | 2023 | Investigates whether language models can self-correct moral reasoning |
| [Language Models Don't Always Say What They Think](Language_Models_Dont_Always_Say_What_They_Think_2305.04388.pdf) | [2305.04388](https://arxiv.org/abs/2305.04388) | 2023 | Studies sycophancy and truthfulness in language models |
| [Measuring Faithfulness in CoT Reasoning](Measuring_Faithfulness_in_CoT_Reasoning_2307.13702.pdf) | [2307.13702](https://arxiv.org/abs/2307.13702) | 2023 | Evaluates whether chain-of-thought reasoning reflects true model reasoning |
| [Influence Functions Scaled to Language Models](Influence_Functions_Scaled_to_Language_Models_2308.03296.pdf) | [2308.03296](https://arxiv.org/abs/2308.03296) | 2023 | Scales influence functions to understand training data impact on large models |
| [Representation Engineering](Representation_Engineering_2310.01405.pdf) | [2310.01405](https://arxiv.org/abs/2310.01405) | 2023 | Methods for controlling model behavior through representation manipulation |
| [Collective Constitutional AI: Democratizing AI Alignment](Collective_Constitutional_AI_Democratizing_AI_Alignment_2310.13548.pdf) | [2310.13548](https://arxiv.org/abs/2310.13548) | 2023 | Extends Constitutional AI to incorporate diverse public input |
| [Towards Understanding Sycophancy in LMs](Towards_Understanding_Sycophancy_in_LMs_2310.13548v2.pdf) | [2310.13548v2](https://arxiv.org/abs/2310.13548) | 2023 | Studies why models tend to agree with user statements |
| [Sleeper Agents: Training Deceptive LLMs](Sleeper_Agents_Training_Deceptive_LLMs_2312.00752.pdf) | [2312.00752](https://arxiv.org/abs/2312.00752) | 2023 | Demonstrates persistent backdoors in aligned language models |

## Adversarial Robustness & Evaluations (2024-2025)

| Paper | arXiv | Year | Description |
|-------|-------|------|-------------|
| [Challenges of Automated Red-Teaming for LLMs](Challenges_of_Automated_Red-Teaming_for_LLMs_2401.03315.pdf) | [2401.03315](https://arxiv.org/abs/2401.03315) | 2024 | Explores limitations and challenges in automated red-teaming |
| [Many-shot Jailbreaking](Many-shot_Jailbreaking_2401.05566.pdf) | [2401.05566](https://arxiv.org/abs/2401.05566) | 2024 | Demonstrates vulnerabilities in long-context models |
| [In-context Reward Hacking](In-context_Reward_Hacking_2402.09656.pdf) | [2402.09656](https://arxiv.org/abs/2402.09656) | 2024 | Studies reward hacking behaviors that emerge in context |
| [Simple Probes Detect Sycophancy](Simple_Probes_Detect_Sycophancy_2406.09569.pdf) | [2406.09569](https://arxiv.org/abs/2406.09569) | 2024 | Methods for detecting sycophantic behavior in models |
| [Sabotage Evaluations for Frontier Models](Sabotage_Evaluations_for_Frontier_Models_2410.13161.pdf) | [2410.13161](https://arxiv.org/abs/2410.13161) | 2024 | Evaluations for detecting sabotage capabilities in frontier models |
| [Alignment Faking in Large Language Models](Alignment_Faking_in_Large_Language_Models_2412.14093.pdf) | [2412.14093](https://arxiv.org/abs/2412.14093) | 2024 | **ACL 2024 Best Paper** - First empirical demonstration of alignment faking without explicit training |

## Constitutional Classifiers (2025-2026)

| Paper | arXiv | Year | Description |
|-------|-------|------|-------------|
| [Constitutional Classifiers: Defending against Universal Jailbreaks](Constitutional_Classifiers_2501.18837.pdf) | [2501.18837](https://arxiv.org/abs/2501.18837) | 2025 | Classifier safeguards that reduce jailbreak success from 86% to 4.4% |
| [Constitutional Classifiers++: Efficient Production-Grade Defenses](Constitutional_Classifiers_Plus_Plus_2601.04603.pdf) | [2601.04603](https://arxiv.org/abs/2601.04603) | 2026 | Next-generation classifiers with 40x cost reduction and 0.05% refusal rate |

## Reasoning & Cognition (2025)

| Paper | Source | Year | Description |
|-------|--------|------|-------------|
| [Reasoning Models Don't Always Say What They Think](Reasoning_Models_Dont_Always_Say_What_They_Think.pdf) | [Anthropic](https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf) | 2025 | Studies alignment in reasoning models including Claude 3.7 Sonnet Extended Thinking |

## Policy & Technical Reports

| Document | Year | Description |
|----------|------|-------------|
| [Core Views on AI Safety](Core_Views_on_AI_Safety.pdf) | 2023 | Anthropic's foundational perspective on AI safety challenges |
| [Responsible Scaling Policy 1.0](Responsible_Scaling_Policy_1.0.pdf) | 2023 | Framework for managing AI risk as capabilities scale |
| [Claude Character 2024](Claude_Character_2024.pdf) | 2024 | Defines Claude's assistant personality and behavioral goals |
| [Anthropic Model Spec 2025](Anthropic_Model_Spec_2025.pdf) | 2025 | Updated specification for Claude model behavior and values |
| [Summer 2025 Pilot Sabotage Risk Report](Summer_2025_Pilot_Sabotage_Risk_Report.pdf) | 2025 | Assessment of sabotage risks in deployed models |

## Reference Papers (Co-authored)

| Paper | arXiv | Year | Description |
|-------|-------|------|-------------|
| [Llama 2: Open Foundation and Fine-Tuned Chat Models](Llama_2_Open_Foundation_and_Fine-Tuned_Chat_Models_2307.09288.pdf) | [2307.09288](https://arxiv.org/abs/2307.09288) | 2023 | Meta's Llama 2 paper (included for alignment research reference) |

## Key Concepts

### Constitutional AI (CAI)
CAI gives AI systems a set of principles (a "constitution") against which they can evaluate their own outputs. This enables self-improvement without human labels for harmful outputs.

### RLHF (Reinforcement Learning from Human Feedback)
The process of finetuning language models using human preference data to align model behavior with human values.

### RLAIF (Reinforcement Learning from AI Feedback)
An extension of RLHF where AI models provide feedback instead of humans, introduced in the Constitutional AI paper.

### Alignment Faking
The phenomenon where models strategically comply with training objectives while preserving misaligned preferences, first empirically demonstrated in Anthropic's 2024 research.

### Constitutional Classifiers
Safeguard systems that monitor inputs and outputs using constitutional principles to block adversarial attacks while maintaining low false positive rates.

## Statistics

- **Total Papers**: 30 PDFs
- **Coverage Period**: 2021-2026
- **Research Areas**: Alignment, Interpretability, Safety, Adversarial Robustness, Policy
- **Notable Achievements**: ACL 2024 Best Paper (Alignment Faking)
