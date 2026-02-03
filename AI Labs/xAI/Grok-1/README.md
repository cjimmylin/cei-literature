# Grok-1

## Overview
Massive 314B parameter Mixture-of-Experts (MoE) model open-sourced by xAI, designed with a focus on real-time world knowledge. Released as open-weights under the Apache 2.0 license in March 2024.

## Technical Specifications
- **Release Year:** 2023 (open-sourced March 2024)
- **Version:** 1.0
- **Parameters:** 314B
- **Architecture:** Mixture of 8 Experts (MoE)
- **Experts Utilization:** 2 experts used per token
- **Layers:** 64
- **Attention Heads:** 48 for queries, 8 for keys/values
- **Embedding Size:** 6,144
- **Tokenization:** SentencePiece tokenizer with 131,072 tokens
- **Maximum Context Length:** 8,192 tokens
- **Weight Format:** int8 (8-bit quantization)
- **Additional Features:**
  - Rotary embeddings (RoPE)
  - Supports activation sharding and 8-bit quantization
- **License:** Apache 2.0

## Papers
No official technical paper has been published by xAI for Grok-1. Technical specifications are available in the GitHub repository and HuggingFace model card.

## Links
- [Official Blog](https://x.ai/blog/grok-os)
- [Model Card](https://huggingface.co/xai-org/grok-1)
- [GitHub Repository](https://github.com/xai-org/grok-1)

## Documentation & Links

### GitHub
- [xai-org/grok-1](https://github.com/xai-org/grok-1) - Official repository with model architecture and weights

### HuggingFace
- [xai-org/grok-1](https://huggingface.co/xai-org/grok-1) - Model weights and documentation

### Key Documentation
| Resource | Description |
|----------|-------------|
| [README](https://github.com/xai-org/grok-1/blob/main/README.md) | Architecture details, requirements |
| [Model Card](https://huggingface.co/xai-org/grok-1) | Usage instructions, limitations |
| [Apache 2.0 License](https://github.com/xai-org/grok-1/blob/main/LICENSE) | Open-source license |

### Running Grok-1
- Requires significant GPU memory (8x A100 80GB recommended)
- JAX/Flax implementation
- See GitHub repo for detailed requirements
