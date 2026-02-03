# NVIDIA Reinforcement Learning Research

## Overview
This directory contains NVIDIA's cutting-edge research on reinforcement learning (RL) techniques for large language models, including novel approaches to scaling RL training and improving reasoning capabilities.

## Research Papers

### 1. Nemotron-Cascade: Scaling Cascaded Reinforcement Learning (December 2025)
**Paper:** Nemotron-Cascade-Scaling-Cascaded-RL.pdf
**arXiv:** 2512.13607
**Publication Date:** December 15, 2025

**Key Contributions:**
- Scales up cascaded reinforcement learning (Cascade RL) framework
- Trains models sequentially across domains
- 14B model outperforms DeepSeek-R1-0528 on LiveCodeBench v5/v6/Pro
- Achieves silver-medal performance in 2025 International Olympiad in Informatics (IOI)
- Introduces Nemotron-Cascade-8B with user-controlled thinking/non-thinking modes

### 2. RLP: Reinforcement as a Pretraining Objective (September 2025)
**Paper:** RLP-Reinforcement-Pretraining-Objective.pdf
**arXiv:** 2510.01265
**Publication Date:** September 26, 2025

**Key Contributions:**
- Brings reinforcement learning directly into the pretraining stage
- Information-driven RL pretraining objective
- Treats chain-of-thought as exploratory action
- Verifier-free dense reward signal
- 19% improvement on Qwen3-1.7B-Base across 8-benchmark math-and-science suite
- Largest gains on AIME25 and MMLU-Pro

**GitHub:** https://github.com/NVlabs/RLP

### 3. ProRL: Prolonged Reinforcement Learning (May 2025)
**Paper:** ProRL-Prolonged-Reinforcement-Learning.pdf
**arXiv:** 2505.24864
**Publication Date:** May 30, 2025

**Key Contributions:**
- Prolonged RL training methodology
- Incorporates KL divergence control and reference policy resetting
- Developed Nemotron-Research-Reasoning-Qwen-1.5B (world's best 1.5B reasoning model)
- Outperforms DeepSeek-R1-1.5B: +14.7% math, +13.9% coding, +54.8% logic, +25.1% STEM, +18.1% instruction-following
- Continued improvement after 2k+ training steps
- ProRL v2 extends to 3,000+ RL steps across five domains

### 4. BroRL: Scaling via Broadened Exploration (September 2025)
**Paper:** BroRL-Scaling-via-Broadened-Exploration.pdf
**arXiv:** 2510.01180

**Key Contributions:**
- Introduces rollout scaling as complementary dimension to step scaling
- Increases exploratory rollouts per prompt to hundreds
- Revives models saturated after 3K ProRL training steps
- Demonstrates continuous improvement beyond ProRL saturation point
- Achieves state-of-the-art results for 1.5B models

## Key Techniques

### Common Methods Across Papers:
- **KL-regularized trust regions**: Prevents policy divergence during RL training
- **Reference policy resets**: Maintains training stability
- **Scheduled cosine length penalties**: Promotes concise outputs
- **Multi-domain training**: Improves generalization
- **Extended training horizons**: Enables continued learning beyond traditional limits

## Impact
These research advances have positioned NVIDIA at the forefront of RL-based model alignment and reasoning enhancement, with practical applications in:
- Agentic AI systems
- Scientific reasoning
- Code generation
- Mathematical problem-solving
- Logical reasoning and puzzles

## Tools & Infrastructure
- **NeMo-Aligner**: Scalable toolkit for efficient model alignment (deprecated 5/15/2025)
- **NeMo RL**: Modern post-training library with Hugging Face integration and Ray scheduling
- **NeMo Gym**: Open-source, modular RL infrastructure for scientific domains

## Resources
- Research Blog: https://developer.nvidia.com/blog/
- Nemotron Research Page: https://research.nvidia.com/labs/nemotron/
- GitHub (NeMo-Aligner): https://github.com/NVIDIA/NeMo-Aligner
