# Phi-1

## Overview
Phi-1 is Microsoft's first small language model (1.3B parameters) trained on high-quality "textbook" data to achieve competitive code generation performance despite its compact size.

## Technical Specifications
- **Release Year:** 2023
- **Parameters:** 1.3B
- **Training:** 4 days on 8 A100 GPUs
- **Dataset:** 6B tokens from web + 1B synthetic tokens from GPT-3.5

## Performance
- **HumanEval:** 50.6% pass@1 accuracy
- **MBPP:** 55.5% pass@1 accuracy

## Papers
| Paper | File | arXiv |
|-------|------|-------|
| Textbooks Are All You Need | [[Textbooks_Are_All_You_Need.pdf]] | [2306.11644](https://arxiv.org/abs/2306.11644) |

## Documentation & Links

### Official Resources
- [Microsoft Research Publication](https://www.microsoft.com/en-us/research/publication/textbooks-are-all-you-need/) - Official research page
- [arXiv Paper](https://arxiv.org/abs/2306.11644) - Technical report

### Model Weights
- [HuggingFace: Microsoft](https://huggingface.co/microsoft) - Model hub

### Related Work
- See also: [[Phi-1.5]], [[Phi-2]], [[Phi-3]], [[Phi-4]] for the evolution of the Phi series
