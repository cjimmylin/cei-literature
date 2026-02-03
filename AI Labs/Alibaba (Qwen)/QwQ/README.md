# QwQ (Qwen with Questions)

## Overview
QwQ is the reasoning model series developed by the Qwen team at Alibaba Cloud. Unlike conventional instruction-tuned models, QwQ is capable of thinking and reasoning, achieving significantly enhanced performance on downstream tasks, especially complex problems requiring multi-step reasoning.

## Technical Specifications
- **Release Year:** 2024
- **Version:** Based on Qwen2.5
- **Parameters:** 32B
- **Architecture:** Reasoning-specialized architecture with thinking mode
- **Key Innovation:** Integration of thinking mode for complex, multi-step reasoning

## Key Capabilities
- **Advanced Reasoning:** Specialized for complex problem-solving
- **Critical Thinking:** Enhanced ability to analyze and evaluate information
- **Multi-Step Reasoning:** Superior performance on tasks requiring multiple reasoning steps
- **Competitive Performance:** Beats OpenAI o1-preview on certain benchmarks

## Documentation & Links

### Official Resources
- **Main Paper:** Documented in [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115) (Section on specialized models)
- **Qwen3 Integration:** [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) discusses unified thinking/non-thinking modes

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/QwQ](https://github.com/QwenLM/QwQ)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| QwQ-32B | [huggingface.co/Qwen/QwQ-32B](https://huggingface.co/Qwen/QwQ-32B) |
| QwQ-32B-Preview | [huggingface.co/Qwen/QwQ-32B-Preview](https://huggingface.co/Qwen/QwQ-32B-Preview) |

### Demo & API
- **Qwen Chat:** [chat.qwenlm.ai](https://chat.qwenlm.ai/)
- **Alibaba Cloud API:** [DashScope](https://dashscope.aliyun.com/)

## Evolution
QwQ's reasoning capabilities have been integrated into Qwen3, which features:
- **Unified Framework:** Combines thinking mode (for complex reasoning) and non-thinking mode (for rapid responses)
- **No Model Switching:** Eliminates the need to switch between chat-optimized models and dedicated reasoning models like QwQ-32B

## Related Papers
While QwQ doesn't have a standalone technical report, it is documented in:
- **Qwen2.5 Technical Report** ([2412.15115](https://arxiv.org/abs/2412.15115)) - Discusses QwQ as a specialized model
- **Qwen3 Technical Report** ([2505.09388](https://arxiv.org/abs/2505.09388)) - Integration of reasoning capabilities

## Note
QwQ represents Alibaba's response to OpenAI's o1 reasoning models, focusing on open-source reasoning capabilities. The technology has been further refined and integrated into the Qwen3 series.
