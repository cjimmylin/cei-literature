# DeepSeek Research Papers Collection

This directory contains all DeepSeek research papers organized in one central location. Papers are also duplicated in their respective model family directories for convenience.

## Papers Inventory (13 Papers)

### Architectural & Foundational Research

#### Native Sparse Attention (Feb 2025)
- **File:** `Native_Sparse_Attention_arxiv_2502.11089.pdf`
- **arXiv:** 2502.11089
- **Title:** Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention
- **Key Innovation:** Dynamic hierarchical sparse strategy for efficient long-context modeling
- **Performance:** Maintains/exceeds Full Attention on 64k-length sequences
- **Status:** Latest efficiency innovation

#### mHC: Manifold-Constrained Hyper-Connections (Dec 2025 - Jan 2026)
- **File:** `mHC_Manifold_Constrained_Hyper_Connections_arxiv_2512.24880.pdf`
- **arXiv:** 2512.24880
- **Title:** mHC: Manifold-Constrained Hyper-Connections
- **Authors:** Co-authored by DeepSeek founder Liang Wenfeng
- **Key Innovation:** Projects residual connection space onto specific manifold
- **Significance:** Architectural rethink for foundational AI models
- **Status:** Cutting-edge research

#### DeepSeek-MoE (Jan 2024)
- **File:** `DeepSeek-MoE_arxiv_2401.06066.pdf`
- **arXiv:** 2401.06066
- **Title:** DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models
- **Key Innovation:** Ultimate expert specialization in MoE
- **Impact:** Foundation for V2/V3 MoE architecture
- **Status:** Foundational paper

### Mathematical Reasoning

#### DeepSeekMath (Feb 2024)
- **File:** `DeepSeekMath_arxiv_2402.03300.pdf`
- **arXiv:** 2402.03300
- **Title:** DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models
- **Achievement:** 51.7% on competition-level MATH benchmark
- **Innovation:** No external toolkits or voting needed
- **Model:** 7B parameters
- **Status:** Foundational math reasoning model

#### DeepSeekMath-V2 (Nov 2025)
- **File:** `DeepSeekMath-V2_arxiv_2511.22570.pdf`
- **arXiv:** 2511.22570
- **Title:** DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning
- **Achievement:** Gold medals on IMO 2025, CMO 2024; 118/120 on Putnam 2024
- **Innovation:** Self-verifiable reasoning with test-time compute scaling
- **Note:** Highly regarded but did NOT win ACL 2024 Best Paper
- **Status:** State-of-the-art math model

### Formal Theorem Proving

#### DeepSeek-Prover (May 2024)
- **File:** `DeepSeek-Prover_arxiv_2405.14333.pdf`
- **arXiv:** 2405.14333
- **Title:** DeepSeek-Prover: Advancing Theorem Proving in LLMs through Large-Scale Synthetic Data
- **Innovation:** Large-scale synthetic data generation for Lean 4
- **Status:** Foundational theorem proving model

#### DeepSeek-Prover-V1.5 (Aug 2024)
- **File:** `DeepSeek-Prover-V1.5_arxiv_2408.08152.pdf`
- **arXiv:** 2408.08152
- **Title:** DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search
- **Innovation:** RL + MCTS with proof assistant feedback
- **Improvement:** Enhanced proof search capabilities
- **Status:** Intermediate version

#### DeepSeek-Prover-V2 (Apr 2025)
- **File:** `DeepSeek-Prover-V2_arxiv_2504.21801.pdf`
- **arXiv:** 2504.21801
- **Title:** DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition
- **Achievement:** 88.9% on MiniF2F-test (SOTA); 49/658 on PutnamBench
- **Innovation:** Subgoal decomposition via RL, cold-start from DeepSeek-V3
- **Model:** 671B parameters
- **Status:** State-of-the-art theorem prover

### Multimodal: Janus Series

#### Janus (Oct 2024)
- **File:** `Janus_arxiv_2410.13848.pdf`
- **arXiv:** 2410.13848
- **Title:** Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation
- **Innovation:** Decoupled visual encoders for understanding vs. generation
- **Architecture:** Single unified transformer
- **Model:** 1.3B parameters
- **Status:** Foundational multimodal model

#### JanusFlow (Nov 2024)
- **File:** `JanusFlow_arxiv_2411.07975.pdf`
- **arXiv:** 2411.07975
- **Title:** JanusFlow: Harmonizing Autoregression and Rectified Flow for Unified Multimodal Understanding and Generation
- **Innovation:** Integrates rectified flow into LLM framework without complex modifications
- **Performance:** 74.9 MMBench, 9.51 MJHQ FID-30k, 0.63 GenEval
- **Model:** 1.3B parameters (DeepSeek-LLM based)
- **Status:** Enhanced generation capabilities

#### Janus-Pro (Jan 2025)
- **File:** `Janus-Pro_arxiv_2501.17811.pdf`
- **arXiv:** 2501.17811
- **Title:** Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling
- **Innovation:** Optimized training, expanded data, scaled model size
- **Models:** 1B, 7B parameters
- **Status:** Latest Janus version

### Multimodal: Vision-Language

#### DeepSeek-VL (Mar 2024)
- **File:** `DeepSeek-VL_arxiv_2403.05525.pdf`
- **arXiv:** 2403.05525
- **Title:** DeepSeek-VL: Towards Real-World Vision-Language Understanding
- **Focus:** Real-world vision-language applications
- **Status:** Foundational VL model

#### DeepSeek-VL2 (Dec 2024)
- **File:** `DeepSeek-VL2_arxiv_2412.10302.pdf`
- **arXiv:** 2412.10302
- **Title:** DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding
- **Innovation:** MoE architecture for vision-language
- **Models:** Tiny (1.0B), Small (2.8B), Standard (4.5B activated parameters)
- **Status:** Latest VL model

## Organization

Papers are organized both:
1. **Here (Papers/):** Central collection of all research papers
2. **Model Directories:** Duplicated in respective model family folders for convenience
   - `/Janus/` - 3 papers (Janus, JanusFlow, Janus-Pro)
   - `/DeepSeekMath/` - 2 papers (Math, Math-V2)
   - `/DeepSeek-Prover/` - 3 papers (Prover, V1.5, V2)

## Research Timeline

### 2024
- Jan: DeepSeek-MoE
- Feb: DeepSeekMath
- Mar: DeepSeek-VL
- May: DeepSeek-Prover
- Aug: DeepSeek-Prover-V1.5
- Oct: Janus
- Nov: JanusFlow
- Dec: DeepSeek-VL2

### 2025
- Jan: Janus-Pro
- Feb: Native Sparse Attention
- Apr: DeepSeek-Prover-V2
- Nov: DeepSeekMath-V2
- Dec: mHC

### 2026
- Jan: mHC (updated)

## Categories

- **Architectural:** 3 papers (MoE, Sparse Attention, mHC)
- **Mathematical:** 5 papers (Math x2, Prover x3)
- **Multimodal:** 5 papers (Janus x3, VL x2)
- **Total:** 13 papers in this directory

## Additional Papers

See parent directory and model-specific subdirectories for complete collection of 28 total papers including:
- Core language models (LLM, V2, V3, V3.2, R1)
- Coding models (Coder, Coder-V2)

## Notes

- All PDFs are complete downloads from arXiv
- Each paper also has corresponding markdown extracts (`.md` files)
- README files in model directories provide detailed context
- Main DeepSeek README provides comprehensive overview
