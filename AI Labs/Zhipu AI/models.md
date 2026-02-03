# Zhipu AI Models

| Release Year | Model Name | Version | Description | Description URL | Link to Paper | Link to Model Card | Local PDF |
|--------------|------------|---------|-------------|-----------------|---------------|-------------------|-----------|
| 2022 | [[GLM-130B/README.md\|GLM-130B]] | 1.0 | Bilingual (En/Ch) bidirectional dense model, top performing open model in 2022. | [Blog](https://zhipu-ai.medium.com/glm-130b-an-open-bilingual-pre-trained-model-23de646c28f1) | [arXiv](https://arxiv.org/abs/2210.02414) | [HuggingFace](https://huggingface.co/THUDM/glm-130b) | [[GLM-130B/GLM-130B_2210.02414.pdf\|PDF]] |
| 2023 | [[ChatGLM-6B/README.md\|ChatGLM-6B]] | 1.0 | Lightweight bilingual dialogue model for local deployment. | [Blog](https://chatglm.cn/blog) | [arXiv](https://arxiv.org/abs/2406.12793) | [HuggingFace](https://huggingface.co/THUDM/chatglm-6b) | [[ChatGLM-6B/ChatGLM_Technical_Report_2406.12793.pdf\|PDF]] |
| 2023 | [[ChatGLM2-6B/README.md\|ChatGLM2-6B]] | 2.0 | Second gen with better performance and 32k context window. | [Blog](https://chatglm.cn/blog/chatglm2) | [arXiv](https://arxiv.org/abs/2406.12793) | [HuggingFace](https://huggingface.co/THUDM/chatglm2-6b) | [[ChatGLM2-6B/ChatGLM_Technical_Report_2406.12793.pdf\|PDF]] |
| 2023 | [[ChatGLM3-6B/README.md\|ChatGLM3-6B]] | 3.0 | Enhanced tool-calling and agentic capabilities. | [Blog](https://chatglm.cn/blog/chatglm3) | [arXiv](https://arxiv.org/abs/2406.12793) | [HuggingFace](https://huggingface.co/THUDM/chatglm3-6b) | [[ChatGLM3-6B/ChatGLM_Technical_Report_2406.12793.pdf\|PDF]] |
| 2024 | [[GLM-4/README.md\|GLM-4]] | 4.0 | Flagship frontier model family with vision and "All Tools" agentic support. | [Blog](https://chatglm.cn/blog/glm-4) | [arXiv](https://arxiv.org/abs/2406.12793) | [HuggingFace](https://huggingface.co/THUDM/glm-4-9b-chat) | [[GLM-4/ChatGLM_Technical_Report_2406.12793.pdf\|PDF]] |
| 2024 | [[CogVLM/README.md\|CogVLM]] | 1.0 | State-of-the-art vision-language model with visual-grounding. | [Blog](https://chatglm.cn/blog/cogvlm) | [arXiv](https://arxiv.org/abs/2311.03079) | [HuggingFace](https://huggingface.co/THUDM/cogvlm-chat-hf) | [[CogVLM/CogVLM_2311.03079.pdf\|PDF]] |
| 2025 | [[GLM-4.5/README.md\|GLM-4.5]] | 4.5 | MoE model series (up to 355B) optimized for high parameter efficiency. | [Blog](https://chatglm.cn/blog/glm-4.5) | - | - | - |
| 2025 | [[GLM-4.7/README.md\|GLM-4.7]] | 4.7 | Latest flagship with comprehensive reasoning and web-agent upgrades. | [Blog](https://chatglm.cn/blog/glm-4.7) | - | - | - |

## Foundational Papers

See the [[Papers/README.md|Papers]] directory for a complete collection of Zhipu AI / THUDM research papers including:
- GLM architecture papers
- Vision-language models (CogVLM, CogAgent)
- Visual generation (CogView, CogVideo, CogVideoX)
- Agents and tools (AgentTuning, WebGLM)
- Long context (LongWriter)

## Documentation Links

### Official Resources
| Resource | Link |
|----------|------|
| Official Website | [zhipuai.cn](https://www.zhipuai.cn) |
| ChatGLM Platform | [chatglm.cn](https://chatglm.cn) |
| API Platform | [open.bigmodel.cn](https://open.bigmodel.cn) |
| X/Twitter | [@zhipu_ai](https://x.com/zhipu_ai) |

### GitHub Repositories (THUDM)
| Repository | Description | Stars |
|------------|-------------|-------|
| [THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) | ChatGLM-6B inference | 40k+ |
| [THUDM/ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B) | ChatGLM2 with 32K context | 15k+ |
| [THUDM/ChatGLM3](https://github.com/THUDM/ChatGLM3) | ChatGLM3 series | 13k+ |
| [THUDM/GLM-4](https://github.com/THUDM/GLM-4) | GLM-4 open-source | 5k+ |
| [THUDM/CogVLM](https://github.com/THUDM/CogVLM) | Vision-language models | 6k+ |
| [THUDM/CogVideo](https://github.com/THUDM/CogVideo) | Video generation | 8k+ |
| [THUDM/CodeGeeX](https://github.com/THUDM/CodeGeeX) | Code generation | 8k+ |
| [THUDM/WebGLM](https://github.com/THUDM/WebGLM) | Web-enhanced LLM | 2k+ |

### HuggingFace Collections
| Organization | Link | Models |
|--------------|------|--------|
| THUDM (Legacy) | [huggingface.co/THUDM](https://huggingface.co/THUDM) | Redirects to zai-org |
| Zhipu AI (zai-org) | [huggingface.co/zai-org](https://huggingface.co/zai-org) | 142+ models |

### Key Model Links (HuggingFace zai-org)
| Category | Models |
|----------|--------|
| Text Generation | [GLM-4.7](https://huggingface.co/zai-org/GLM-4.7), [GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash), [ChatGLM3-6B](https://huggingface.co/THUDM/chatglm3-6b) |
| Vision-Language | [GLM-4.6V](https://huggingface.co/zai-org/GLM-4.6V), [CogVLM](https://huggingface.co/THUDM/cogvlm-chat-hf), [CogAgent](https://huggingface.co/THUDM/CogAgent) |
| Code | [CodeGeeX2-6B](https://huggingface.co/THUDM/codegeex2-6b) |
| Video | [CogVideoX-5B](https://huggingface.co/THUDM/CogVideoX-5b) |
| Agents | [AutoGLM-Phone-9B](https://huggingface.co/zai-org/AutoGLM-Phone-9B) |

### Benchmarks & Datasets
| Benchmark | Link |
|-----------|------|
| AlignBench | [huggingface.co/datasets/THUDM/AlignBench](https://huggingface.co/datasets/THUDM/AlignBench) |
| AgentBench | [github.com/THUDM/AgentBench](https://github.com/THUDM/AgentBench) |
| LVBench | Vision-language benchmark |
| MotionBench | Motion understanding |
