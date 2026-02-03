# Marco-o1

## Overview
Marco-o1 is an open-source large reasoning model developed by the MarcoPolo Team at Alibaba International Digital Commerce (AIDC). It is a fine-tuned version of Qwen2-7B-Instruct that integrates advanced techniques such as chain-of-thought (CoT) fine-tuning, Monte Carlo Tree Search (MCTS), and reasoning action strategies.

## Technical Specifications
- **Release Year:** 2024-2025
- **Version:** v1 (2024), v2 (2025)
- **Base Model:** Qwen2-7B-Instruct
- **Parameters:** 7B
- **Key Techniques:**
  - Chain-of-Thought (CoT) fine-tuning
  - Monte Carlo Tree Search (MCTS)
  - Reasoning Action Strategies
  - Knowledge Distillation (v2)

## Performance
- **MGSM (English):** +6.17% accuracy improvement
- **MGSM (Chinese):** +5.60% accuracy improvement
- Competitive with OpenAI's o1 on certain reasoning benchmarks

## Documentation & Links

### Official Resources
- **Technical Report v1:** [arXiv:2411.14405](https://arxiv.org/abs/2411.14405)
- **Technical Report v2:** [arXiv:2503.01461](https://arxiv.org/abs/2503.01461)

### GitHub Repositories
- **Main Repository:** [github.com/AIDC-AI/Marco-o1](https://github.com/AIDC-AI/Marco-o1)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Marco-o1 | [huggingface.co/AIDC-AI/Marco-o1](https://huggingface.co/AIDC-AI/Marco-o1) |

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Marco-o1: Towards Open Reasoning Models for Open-Ended Solutions | [2411.14405](https://arxiv.org/abs/2411.14405) | [Marco-o1_2411.14405.pdf](Marco-o1_2411.14405.pdf) |
| Marco o1 v2: Towards Widening The Distillation Bottleneck for Reasoning Models | [2503.01461](https://arxiv.org/abs/2503.01461) | [Marco-o1_v2_2503.01461.pdf](Marco-o1_v2_2503.01461.pdf) |

## Development Team
Developed by the MarcoPolo Team, AI Business, Alibaba International Digital Commerce (AIDC).

## Key Innovations

### Version 1 (November 2024)
- Integration of CoT fine-tuning with MCTS
- Reasoning action strategies for open-ended problem solving
- Enhanced performance on multilingual reasoning tasks

### Version 2 (January 2025)
- Focus on widening the distillation bottleneck
- Improved knowledge transfer from larger reasoning models
- Enhanced reasoning capabilities through advanced distillation techniques

## License
Open-source model available on GitHub and HuggingFace.

## Relation to Qwen Ecosystem
Marco-o1 is part of Alibaba's broader AI ecosystem but developed specifically by the international commerce division (AIDC). It complements the main Qwen reasoning models (QwQ) by providing an alternative approach focused on MCTS and distillation techniques.
