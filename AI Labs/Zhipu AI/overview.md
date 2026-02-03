# Zhipu AI Overview

## Lab Overview

Zhipu AI (Beijing Zhipu Huazhang Technology Co., Ltd.) is a leading Chinese AI company founded in 2019 as a spin-off from Tsinghua University's Knowledge Engineering Group (KEG). The company develops foundation models across language, vision, and multimodal domains, with a strong focus on bilingual (Chinese-English) capabilities and open-source releases.

---

## Model Summary

| Model | Year | Type | Parameters | Key Features |
|-------|------|------|------------|--------------|
| GLM | 2021 | Language | Various | Autoregressive blank infilling pre-training |
| GLM-130B | 2022 | Language | 130B | Bilingual, INT4 quantization, open weights |
| ChatGLM-6B | 2023 | Chat | 6B | First open bilingual chat model |
| ChatGLM2-6B | 2023 | Chat | 6B | Improved context length (32K), Flash Attention |
| ChatGLM3-6B | 2023 | Chat | 6B | Function calling, code interpreter |
| GLM-4 | 2024 | Chat | Various | Multi-stage alignment, All Tools capability |
| CogView | 2021 | Text-to-Image | 4B | First open Chinese text-to-image |
| CogView2 | 2022 | Text-to-Image | - | Improved efficiency and quality |
| CogView3 | 2024 | Text-to-Image | - | Relay diffusion (ECCV 2024) |
| CogView3-Plus | 2024 | Text-to-Image | 3B | DiT-based with zero-SNR diffusion |
| CogView4 | 2025 | Text-to-Image | - | First open-source Chinese character generation |
| CogVLM | 2023 | Vision-Language | 17B | Visual expert in attention/FFN |
| CogVLM2 | 2024 | Vision-Language | 19B | Enhanced resolution, video understanding |
| CogAgent | 2023 | GUI Agent | 18B | GUI grounding and navigation |
| CogVideo | 2022 | Text-to-Video | 9.4B | Inherits CogView image generation |
| CogVideoX | 2024 | Text-to-Video | 5B | 3D VAE, expert transformer |
| GLM-4.6 | 2025 | Chat/Code | 355B MoE | 200K context, MIT license, coding focus |
| GLM-4.6V | 2025 | Vision-Language | 106B | 128K context, native multimodal tool calling |
| CodeGeeX | 2023 | Code | 13B | Multilingual code generation (23 languages) |
| CodeGeeX2 | 2024 | Code | 6B | Improved efficiency, +57-83% performance |

---

## Model Families

### GLM (General Language Model)

**GLM (Original)** - Introduced autoregressive blank infilling as a unified pre-training approach combining masked LM and autoregressive objectives. Achieves strong performance on NLU, conditional, and unconditional generation tasks.
- Paper: [GLM_Original_2103.10360.pdf](Papers/GLM_Original_2103.10360.pdf)

**GLM-130B** - A 130 billion parameter bilingual model trained on Chinese and English corpora. Notable for INT4 quantization without quality loss and open availability, enabling inference on consumer GPUs (4x RTX 3090).
- Paper: [GLM-130B_2210.02414.pdf](GLM-130B/GLM-130B_2210.02414.pdf)

### ChatGLM Series

**ChatGLM-6B** - An open bilingual chat model based on GLM architecture with supervised fine-tuning, feedback bootstrap, and RLHF. One of the first accessible open-weight Chinese chat models.
- Paper: [ChatGLM_Technical_Report_2406.12793.pdf](ChatGLM-6B/ChatGLM_Technical_Report_2406.12793.pdf)

**ChatGLM2-6B** - Second generation with improved architecture supporting 32K context length via Flash Attention and Multi-Query Attention. Enhanced quantization and inference efficiency.
- Paper: [ChatGLM_Technical_Report_2406.12793.pdf](ChatGLM2-6B/ChatGLM_Technical_Report_2406.12793.pdf)

**ChatGLM3-6B** - Third generation adding function calling, code interpreter, and complex agent behaviors. Native tool use integration.
- Paper: [ChatGLM_Technical_Report_2406.12793.pdf](ChatGLM3-6B/ChatGLM_Technical_Report_2406.12793.pdf)

**GLM-4** - Latest generation featuring multi-stage alignment training and "All Tools" capability for autonomous tool selection. Competitive with GPT-4 on various benchmarks.
- Paper: [ChatGLM_Technical_Report_2406.12793.pdf](GLM-4/ChatGLM_Technical_Report_2406.12793.pdf)

### CogVLM Family

**CogVLM** - A 17B vision-language model introducing visual experts in both attention and FFN layers. Achieves state-of-the-art on 10+ benchmarks while maintaining frozen LLM capabilities.
- Paper: [CogVLM_2311.03079.pdf](CogVLM/CogVLM_2311.03079.pdf)

**CogVLM2** - Successor with 19B parameters supporting higher resolution (1344x1344), video understanding, and improved OCR. Multiple variants including CogVLM2-Video.
- Paper: [CogVLM2_2408.16500.pdf](CogVLM/CogVLM2_2408.16500.pdf)

**CogAgent** - An 18B visual agent model specialized in GUI understanding and navigation. Achieves state-of-the-art on GUI grounding benchmarks and supports both PC and mobile interfaces.
- Paper: [CogAgent_2312.08914.pdf](CogVLM/CogAgent_2312.08914.pdf)

### Video Generation (CogVideo)

**CogVideo** - A 9.4B parameter text-to-video generation model inheriting from CogView. Uses multi-frame-rate hierarchical training for video generation from text or image inputs.
- Paper: [CogVideo_2205.15868.pdf](Papers/CogVideo_2205.15868.pdf)

**CogVideoX** - Next-generation text-to-video model using 3D VAE and expert transformer architecture. Generates 6-second videos at 720p with improved temporal consistency.
- Paper: [CogVideoX_2408.06072.pdf](Papers/CogVideoX_2408.06072.pdf)

### Image Generation (CogView)

**CogView** - A 4B parameter transformer for text-to-image generation, the first large-scale open Chinese text-to-image model. Introduced techniques for stable training of ultra-high resolution generation.
- Paper: [CogView_2105.13290.pdf](CogView/CogView_2105.13290.pdf)

**CogView2** - Second generation with improved efficiency and quality through hierarchical transformer architecture.
- Paper: [CogView2_2204.14217.pdf](CogView/CogView2_2204.14217.pdf)

**CogView3** - Revolutionary relay diffusion framework achieving 77% win rate vs SDXL. Presented at ECCV 2024. Generates images through cascaded refinement (512→1024→2048).
- Paper: [CogView3_2403.05121.pdf](CogView/CogView3_2403.05121.pdf)

**CogView3-Plus** - DiT-based variant with zero-SNR diffusion noise scheduling and text-image joint attention (3B parameters, open-sourced Oct 2024).
- Repository: https://github.com/THUDM/CogView3

**CogView4** - First open-source model capable of generating Chinese characters. Uses bilingual GLM-4 encoder, SOTA on DPG-Bench (Released Mar 2025).
- Repository: https://github.com/THUDM/CogView4

### Code Generation (CodeGeeX)

**CodeGeeX** - A 13B parameter multilingual code generation model supporting 23 programming languages. Trained on 850B tokens, presented at KDD 2023.
- Paper: [CodeGeeX_2303.17568.pdf](CodeGeeX/CodeGeeX_2303.17568.pdf)

**CodeGeeX2** - More efficient 6B model with superior performance (+57-83% across languages) through training on additional 600B code tokens.
- HuggingFace: https://huggingface.co/THUDM/codegeex2-6b

### GLM-4.6 Series

**GLM-4.6** - Frontier 355B MoE model (~32B active) with 200K context window and MIT license. 15% more efficient than GLM-4.5, excels in coding tasks.
- Release: September 2025

**GLM-4.6V** - Vision-language model (106B) with 128K context supporting native multimodal function calling. Uses RLCS for comprehensive multimodal reasoning.
- Paper: [GLM-4.6V_2507.01006.pdf](GLM-4.6/GLM-4.6V_2507.01006.pdf)
- Release: December 2025

---

## Research Papers

**WebGLM** - A web-enhanced QA system combining GLM with search retrieval. Introduces a generator-supported retriever training approach for improved accuracy.
- Paper: [WebGLM_2306.07906.pdf](Papers/WebGLM_2306.07906.pdf)

**AgentTuning** - A method for improving LLM agent capabilities through instruction tuning on diverse agent tasks while maintaining general abilities. Introduces AgentInstruct dataset.
- Paper: [AgentTuning_2310.12823.pdf](Papers/AgentTuning_2310.12823.pdf)

**Self-Contrast** - A training approach enabling models to learn from self-generated contrastive examples for improved reasoning and instruction following.
- Paper: [Self-Contrast_2404.00228.pdf](Papers/Self-Contrast_2404.00228.pdf)

**LongWriter** - A method and dataset (LongWriter-6k) for training models to generate coherent long-form outputs (10,000+ words). Introduces AgentWrite for automated long-text construction.
- Paper: [LongWriter_2408.07055.pdf](Papers/LongWriter_2408.07055.pdf)
