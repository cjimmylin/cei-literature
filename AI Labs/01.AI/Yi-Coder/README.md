# Yi-Coder

## Overview
Open-source code language model series with state-of-the-art performance on programming benchmarks like HumanEval. Yi-Coder-9B-Chat achieved an impressive 23% pass rate on LiveCodeBench, making it the only model under 10B parameters to surpass 20%, outperforming significantly larger models.

## Technical Specifications
- **Release Year:** 2024
- **Release Date:** September 5, 2024
- **Model Variants:** 9B and 1.5B (Base and Chat versions)
- **Context Length:** 128K tokens
- **Programming Languages:** 52 languages supported
- **License:** Apache 2.0

## Documentation

**Comprehensive Technical Documentation:** [Yi-Coder_Documentation.md](Yi-Coder_Documentation.md)
- Complete architecture details
- Training methodology
- Benchmark results
- Usage examples
- Deployment options

## Papers

| Paper | arXiv ID | Date | Local PDF |
|-------|----------|------|-----------|
| Yi: Open Foundation Models by 01.AI | [2403.04652](https://arxiv.org/abs/2403.04652) | 2024-03-07 | [PDF](../Papers/Yi_Technical_Report_2403.04652.pdf) |

Note: Yi-Coder is based on the Yi foundation models described in the main Technical Report. No separate publication exists.

## Links
- [Official Blog](https://01.ai/blog/yi-coder)
- [Research Paper](https://arxiv.org/abs/2403.04652)
- [Model Card](https://huggingface.co/01-ai/Yi-Coder-9B-Chat)

## Documentation & Links

### GitHub
- [01-ai/Yi-Coder](https://github.com/01-ai/Yi-Coder) - Yi-Coder repository with inference and fine-tuning code

### HuggingFace Models
| Size | Base | Chat |
|------|------|------|
| 9B | [Yi-Coder-9B](https://huggingface.co/01-ai/Yi-Coder-9B) | [Yi-Coder-9B-Chat](https://huggingface.co/01-ai/Yi-Coder-9B-Chat) |
| 1.5B | [Yi-Coder-1.5B](https://huggingface.co/01-ai/Yi-Coder-1.5B) | [Yi-Coder-1.5B-Chat](https://huggingface.co/01-ai/Yi-Coder-1.5B-Chat) |

### Benchmarks
- HumanEval: State-of-the-art for models under 10B parameters
- MBPP, MultiPL-E evaluated
- See official blog for detailed benchmark comparisons
