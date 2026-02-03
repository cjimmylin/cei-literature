# Llama 3.2

## Overview
Multimodal (vision) and small, fast mobile-optimized models designed for efficient local deployment.

## Technical Specifications
- **Release Year:** 2024
- **Release Date:** September 25, 2024
- **Version:** Vision / Edge
- **Parameters:** 1B, 3B (Edge) / 11B, 90B (Vision)
- **Context Window:** 128k tokens
- **Training Data:** 6B image-text pairs (Vision models)
- **Knowledge Cutoff:** December 2023
- **Supported Languages:** English (image+text), multilingual text-only (8 languages)

## Documentation & Links

| Type | Link |
|------|------|
| Official Blog | [Llama 3.2: Connect 2024](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/) |
| Research Paper | [arXiv:2407.21783](https://arxiv.org/abs/2407.21783) |
| GitHub | [meta-llama/llama-models](https://github.com/meta-llama/llama-models) |
| HuggingFace (1B) | [meta-llama/Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) |
| HuggingFace (3B) | [meta-llama/Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B) |
| HuggingFace (11B Vision) | [meta-llama/Llama-3.2-11B-Vision](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision) |
| HuggingFace (11B Vision Instruct) | [meta-llama/Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) |
| HuggingFace (90B Vision) | [meta-llama/Llama-3.2-90B-Vision](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision) |
| HuggingFace (90B Vision Instruct) | [meta-llama/Llama-3.2-90B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct) |
| Model Card (GitHub) | [MODEL_CARD.md](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md) |
| Model Downloads | [Llama Downloads](https://llama.meta.com/llama-downloads/) |
| License | [Llama 3.2 Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE) |
| Responsible Use Guide | [Llama Responsible Use](https://llama.meta.com/responsible-use-guide/) |
| Acceptable Use Policy | [Llama 3.2 Use Policy](https://www.llama.com/llama3_2/use-policy) |
| Trust & Safety | [Llama Trust & Safety](https://llama.meta.com/trust-and-safety/) |
| Llama Guard 3 | [meta-llama/Llama-Guard-3-11B](https://huggingface.co/meta-llama/Llama-Guard-3-11B) |

## Benchmarks (Vision Models)

| Benchmark | Llama 3.2 11B Vision | Llama 3.2 90B Vision |
|-----------|---------------------|---------------------|
| VQAv2 | 75.2% | 78.1% |
| DocVQA (ANLS) | 88.4 | 90.1 |
| ChartQA | 83.4% | 85.5% |
| MMLU (text) | 73.0% | 86.0% |

## Papers and Documentation

| Document | Type | File | Size |
|----------|------|------|------|
| Llama 3.2 Model Card | Model Card | [MODEL_CARD.md](MODEL_CARD.md) | 25 KB |

Note: Llama 3.2 is covered by The Llama 3 Herd of Models paper (arxiv:2407.21783) available in the Llama 3 and Llama 3.1 directories.
