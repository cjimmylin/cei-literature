# Phi-3.5

## Overview
An upgrade to the Phi-3 family, introducing Mixture-of-Experts (MoE) architectures and native vision-language capabilities with enhanced multilingual support and longer context capabilities.

## Technical Specifications
- **Release Year:** 2024 (August)
- **Variants:** mini / MoE / vision
- **Context Length:** Up to 128K tokens

## Models
- **Phi-3.5-mini:** Enhanced with multilingual support and improved conversation quality
- **Phi-3.5-MoE:** 16 x 3.8B MoE with 6.6B active parameters, competitive with Llama 3.1 and Mixtral
- **Phi-3.5-vision:** 4.2B parameters with multimodal capabilities (text and images)

## Performance Highlights
- Phi-3.5-MoE achieves performance on par with Gemini-1.5-Flash and GPT-4o-mini
- Phi-3.5-vision excels in reasoning tasks with single and multi-image prompts
- Substantial gains in multilingual and multi-turn conversation quality

## Papers
| Paper | File | arXiv |
|-------|------|-------|
| Phi-3 Technical Report (covers Phi-3.5) | See [[Phi-3]] | [2404.14219](https://arxiv.org/abs/2404.14219) |
| Phi-3 Safety Post-Training | [[Phi-3_Safety_Post-Training.pdf]] | [Microsoft Download](https://download.microsoft.com/download/c/4/f/c4f6e8d4-c34b-4b12-9c2a-e1dd37e8ae4d/phi3_safety_paper_final%201.pdf) |

## Documentation & Links

### Official Resources
- [Official Blog Post](https://azure.microsoft.com/en-us/blog/phi-3-5-models-are-now-available/) - Azure announcement
- [Phi-3 Technical Report](https://arxiv.org/abs/2404.14219) - Covers Phi-3.5 family

### Model Weights
- [HuggingFace: Phi-3.5 Collection](https://huggingface.co/collections/microsoft/phi-35-66c6691a337424caed6f7c1d) - All Phi-3.5 variants
- [HuggingFace: Phi-3.5-mini-instruct](https://huggingface.co/microsoft/Phi-3.5-mini-instruct)
- [HuggingFace: Phi-3.5-MoE-instruct](https://huggingface.co/microsoft/Phi-3.5-MoE-instruct)
- [HuggingFace: Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

### Code & Implementation
- [GitHub: Phi-3 Cookbook](https://github.com/microsoft/Phi-3CookBook) - Examples and tutorials

### Azure Deployment
- [Azure AI Model Catalog](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/model-catalog) - Deploy on Azure
- [Azure AI Studio](https://ai.azure.com/) - AI development platform

### Related Work
- See also: [[Phi-1]], [[Phi-1.5]], [[Phi-2]], [[Phi-3]], [[Phi-4]] for the evolution of the Phi series
