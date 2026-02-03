# DeepSeek-Prover

## Overview
DeepSeek-Prover is a series of large language models specialized for formal theorem proving in Lean 4. These models advance the state-of-the-art in neural theorem proving through innovative approaches to synthetic data generation and reinforcement learning.

## Model Versions

### DeepSeek-Prover (May 2024)
- **arXiv:** 2405.14333
- **Release Date:** May 2024
- **Subtitle:** "Advancing Theorem Proving in LLMs through Large-Scale Synthetic Data"
- **Key Features:**
  - Large-scale synthetic data generation
  - Formal theorem proving in Lean
  - Neural theorem proving approach

### DeepSeek-Prover-V1.5 (August 2024)
- **arXiv:** 2408.08152
- **Release Date:** August 2024
- **Subtitle:** "Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search"
- **Key Features:**
  - Proof assistant feedback integration
  - Reinforcement learning approach
  - Monte-Carlo Tree Search (MCTS)
  - Enhanced proof search capabilities

### DeepSeek-Prover-V2 (April 2025)
- **arXiv:** 2504.21801
- **Release Date:** April 30, 2025 (updated July 18, 2025)
- **Subtitle:** "Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition"
- **Key Features:**
  - Subgoal decomposition via reinforcement learning
  - Recursive theorem proving pipeline
  - Initialized with data from DeepSeek-V3
  - State-of-the-art neural theorem proving
- **Performance:**
  - 88.9% pass ratio on MiniF2F-test (SOTA)
  - 49/658 problems solved on PutnamBench
- **Model Size:** 671B parameters

## Research Papers

All papers are available in this directory:
- `DeepSeek-Prover_arxiv_2405.14333.pdf` - Original Prover (V1)
- `DeepSeek-Prover-V1.5_arxiv_2408.08152.pdf` - V1.5 with RL and MCTS
- `DeepSeek-Prover-V2_arxiv_2504.21801.pdf` - V2 with subgoal decomposition

## Key Innovations

1. **Synthetic Data Generation (V1):** Large-scale creation of training data for theorem proving
2. **Proof Assistant Feedback (V1.5):** Integration of formal verification feedback into RL training
3. **Subgoal Decomposition (V2):** Breaking complex proofs into manageable subgoals via RL
4. **Cold-Start Training (V2):** DeepSeek-V3 generates initial training data through problem decomposition
5. **Chain-of-Thought Synthesis (V2):** Combines resolved subgoals into coherent proof strategies

## Methodology (V2)

The DeepSeek-Prover-V2 training process:
1. DeepSeek-V3 decomposes complex problems into subgoals
2. Subgoals are resolved and synthesized into chain-of-thought reasoning
3. This creates initial cold-start data for reinforcement learning
4. RL further refines the model's theorem-proving capabilities

## Benchmark Performance

### DeepSeek-Prover-V2-671B
- **MiniF2F-test:** 88.9% pass ratio (state-of-the-art)
- **PutnamBench:** 49/658 problems solved
- **Framework:** Lean 4

## Links

- **GitHub:** [github.com/deepseek-ai/DeepSeek-Prover](https://github.com/deepseek-ai/DeepSeek-Prover)
- **Hugging Face:** [deepseek-ai prover models](https://huggingface.co/deepseek-ai)
