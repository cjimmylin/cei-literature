# Yi-VL: Complete Vision-Language Model Documentation

**Source:** GitHub Repository (https://github.com/01-ai/Yi) and HuggingFace Model Cards
**Date Extracted:** January 31, 2026
**Reference Paper:** Yi: Open Foundation Models by 01.AI (arXiv:2403.04652)
**Release Date:** January 23, 2024

## Overview

Yi-VL (Yi Vision-Language) is an open-source multimodal vision-language model that combines advanced image understanding with bilingual (English/Chinese) text capabilities. **Yi-VL-34B is the first open-source 34B vision-language model worldwide** and ranks first among all open-source models on MMMU and CMMMU benchmarks (as of January 2024).

## Model Variants

| Model | Parameters | Vision Encoder | LLM Backbone | Input Resolution | Recommended GPU |
|-------|-----------|----------------|--------------|------------------|-----------------|
| **Yi-VL-34B** | 34B | CLIP ViT-H/14 | Yi-34B-Chat | 448×448 | 4× RTX 4090 or A800 (80GB) |
| **Yi-VL-6B** | 6B | CLIP ViT-H/14 | Yi-6B-Chat | 448×448 | RTX 3090/4090, A10, A30 |

Both models are available on HuggingFace, ModelScope, and WiseModel platforms.

## Architecture

Yi-VL adopts the **LLaVA architecture** consisting of three primary components:

### Architectural Components

```
┌─────────────────────────────────────────┐
│  Vision Transformer (ViT)               │
│  - CLIP ViT-H/14 (laion2B-s32B-b79K)   │
│  - Image encoding & feature extraction  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Projection Module (MLP)                │
│  - 2-layer MLP with layer normalization │
│  - Aligns image features to text space  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Large Language Model (LLM)             │
│  - Yi-34B-Chat or Yi-6B-Chat            │
│  - English & Chinese proficiency        │
└─────────────────────────────────────────┘
```

### Component Details

1. **Vision Transformer (ViT)**
   - **Model:** CLIP ViT-H/14 pre-trained on laion2B-s32B-b79K
   - **Function:** Image encoding and feature extraction
   - **Resolution:** 448×448 pixels

2. **Projection Module**
   - **Architecture:** 2-layer Multilayer Perceptron (MLP)
   - **Enhancement:** Layer normalization after each layer
   - **Purpose:** Align image features with text feature space

3. **Large Language Model**
   - **34B variant:** Initialized with Yi-34B-Chat
   - **6B variant:** Initialized with Yi-6B-Chat
   - **Capabilities:** Bilingual text generation (English & Chinese)

## Training Methodology

### Three-Stage Training Process

Yi-VL employs a sophisticated three-stage training approach:

| Stage | Resolution | Trainable Components | Dataset Size | Primary Objective |
|-------|-----------|---------------------|--------------|-------------------|
| **Stage 1** | 224×224 | ViT + Projection (LLM frozen) | 100M pairs | Vision-language alignment |
| **Stage 2** | 448×448 | ViT + Projection (LLM frozen) | 25M pairs | Fine-grained detail enhancement |
| **Stage 3** | 448×448 | All components | 1M pairs | Multimodal chat capability |

### Training Parameters

| Stage | Global Batch Size | Learning Rate | Gradient Clipping | Epochs |
|-------|------------------|---------------|-------------------|--------|
| 1, 2 | 4096 | 1e-4 | 0.5 | 1 |
| 3 | 256 | 2e-5 | 1.0 | 2 |

### Training Infrastructure

**Yi-VL-34B:**
- **Hardware:** 128 × NVIDIA A800 (80GB) GPUs
- **Training Time:** Approximately 10 days

**Yi-VL-6B:**
- **Hardware:** 128 × NVIDIA A800 (80GB) GPUs
- **Training Time:** Approximately 3 days

### Training Datasets

**Stage 1: Vision-Language Alignment**
- **Dataset:** LAION-400M
- **Size:** 100M image-text pairs
- **Goal:** Learn basic vision-to-text feature mapping

**Stage 2: Fine-Grained Enhancement**
- **Datasets:** LAION-400M, CLLaVA, LLaVAR, Flickr, VQAv2, RefCOCO, Visual7w
- **Size:** ~25M image-text pairs
- **Goal:** Improve detailed visual understanding at higher resolution

**Stage 3: Multimodal Chat**
- **Datasets:** GQA, VizWiz VQA, TextCaps, OCR-VQA, Visual Genome, LAION GPT4V
- **Size:** ~1M high-quality pairs (max 50K per source)
- **Goal:** Enable natural multi-turn conversations about images

## Technical Capabilities

### Supported Features

- ✅ **Multi-round text-image conversations** (with single image input)
- ✅ **Bilingual support** (English & Chinese text recognition)
- ✅ **Visual question answering (VQA)**
- ✅ **Fine-grained image analysis** (448×448 resolution)
- ✅ **Image comprehension and detail extraction**
- ✅ **Content recognition and description**
- ✅ **Complex scene interpretation**

### Known Limitations

- ❌ **Single image only** - Multiple images per input not supported
- ❌ **No text-to-3D generation**
- ❌ **No image-to-video generation**
- ⚠️ **Hallucination risks** in complex multi-object scenes
- ⚠️ **Fixed resolution** (448×448) - Higher resolution images don't improve performance
- ⚠️ **Information loss** with low-resolution input images

## Benchmark Results

### MMMU Benchmark (English)
**Yi-VL-34B: Rank #1** among all open-source models
- Comprehensive multimodal understanding evaluation
- Tests across multiple domains and question types

### CMMMU Benchmark (Chinese)
**Yi-VL-34B: Rank #1** among all open-source models
- Chinese multimodal understanding evaluation
- Demonstrates strong bilingual capabilities

### Additional Benchmarks
Yi-VL demonstrates exceptional performance on:
- VQAv2 (Visual Question Answering)
- GQA (General Question Answering)
- TextVQA (Text-based VQA)
- Visual Genome
- RefCOCO (Referring Expression Comprehension)

*(Benchmark rankings based on data available as of January 2024)*

## Installation & Setup

### System Requirements

**For Yi-VL-34B:**
- 4 × RTX 4090 (24GB each), or
- 1 × A800 (80GB), or
- Equivalent VRAM capacity

**For Yi-VL-6B:**
- RTX 3090 (24GB)
- RTX 4090 (24GB)
- A10
- A30
- Or equivalent GPU

**Software Requirements:**
- Python >= 3.8
- PyTorch >= 2.0
- Transformers library
- CUDA compatible GPU drivers

### Installation Steps

```bash
# Clone the Yi repository
git clone https://github.com/01-ai/Yi.git
cd Yi/VL

# Install dependencies
pip install -r requirements.txt

# Download model weights
# Via HuggingFace:
# - Yi-VL-34B: https://huggingface.co/01-ai/Yi-VL-34B
# - Yi-VL-6B: https://huggingface.co/01-ai/Yi-VL-6B
```

## Usage Examples

### Basic Inference (Python)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import torch

# Load model and tokenizer
model_path = "01-ai/Yi-VL-34B"
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_path)

# Load image
image = Image.open("path/to/image.jpg")

# Prepare conversation
messages = [
    {"role": "user", "content": [
        {"type": "image", "image": image},
        {"type": "text", "text": "What is shown in this image?"}
    ]}
]

# Generate response
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(
    inputs,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.9
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Multi-turn Conversation

```python
# Continue conversation with same image
messages.append({"role": "assistant", "content": response})
messages.append({"role": "user", "content": "Can you describe it in more detail?"})

# Generate next response
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(inputs, max_new_tokens=512)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
```

### Chinese Language Support

```python
# Using Chinese for both question and response
messages = [
    {"role": "user", "content": [
        {"type": "image", "image": image},
        {"type": "text", "text": "这张图片中显示了什么？"}
    ]}
]

# Model will respond in Chinese
```

## Deployment Options

### Available Platforms

1. **HuggingFace Hub**
   - Yi-VL-34B: https://huggingface.co/01-ai/Yi-VL-34B
   - Yi-VL-6B: https://huggingface.co/01-ai/Yi-VL-6B
   - Direct integration with Transformers library

2. **ModelScope** (Optimized for China)
   - Yi-VL-34B: https://www.modelscope.cn/models/01ai/Yi-VL-34B/summary
   - Yi-VL-6B: https://www.modelscope.cn/models/01ai/Yi-VL-6B/summary

3. **WiseModel**
   - Alternative model repository
   - Additional deployment options

### Inference Optimization

**Recommended Configurations:**
- Use `torch.float16` or `bfloat16` for faster inference
- Enable `device_map="auto"` for multi-GPU distribution
- Adjust `max_new_tokens` based on response length needs
- Tune `temperature` and `top_p` for creativity vs. accuracy balance

## Training Data Composition

### Stage 1: Foundation (100M pairs)
- **LAION-400M:** Web-scale image-text pairs
- **Focus:** Basic vision-language alignment

### Stage 2: Enhancement (~25M pairs)
- **LAION-400M:** Continued alignment
- **CLLaVA:** Curated language-vision data
- **LLaVAR:** Visual reasoning tasks
- **Flickr:** Natural image descriptions
- **VQAv2:** Question-answer pairs
- **RefCOCO:** Referring expressions
- **Visual7w:** Complex visual reasoning

### Stage 3: Chat Capability (~1M pairs)
- **GQA:** General question answering
- **VizWiz VQA:** Real-world visual questions
- **TextCaps:** Text-focused captions
- **OCR-VQA:** OCR-based questions
- **Visual Genome:** Dense annotations
- **LAION GPT4V:** High-quality synthetic data
- **Limitation:** Max 50K samples per source

## License & Usage

**License:** Apache 2.0

### Permissions
- ✅ Academic research (fully open)
- ✅ Commercial use (free with permission email to 01.AI)
- ✅ Modification and redistribution
- ✅ Derivative works

### Requirements
- Attribution to 01.AI required
- Include original license notice
- No warranty provided

## Citation

If using Yi-VL in research, please cite:

```bibtex
@misc{ai2024yi,
    title={Yi: Open Foundation Models by 01.AI},
    author={01.AI and Alex Young and Bei Chen and Chao Li and
            Chengen Huang and others},
    year={2024},
    eprint={2403.04652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

## Performance Optimization Tips

### Hardware Optimization
1. Use multiple GPUs for Yi-VL-34B (model parallelism)
2. Enable gradient checkpointing for memory efficiency
3. Use mixed precision (fp16/bf16) for faster inference
4. Consider quantization (8-bit/4-bit) for deployment

### Prompt Engineering
1. Be specific and clear in visual questions
2. For Chinese content, use Chinese prompts
3. Break complex questions into multiple turns
4. Reference specific regions or objects when relevant

### Best Practices
1. **Image Quality:** Use clear, well-lit images at appropriate resolution
2. **Context Length:** Keep conversations focused (long context may degrade)
3. **Validation:** Cross-check responses for hallucination in complex scenes
4. **Language Choice:** Match prompt language to expected response language

## Known Issues & Solutions

### Common Issues

**Issue: Hallucination in complex scenes**
- **Solution:** Ask for specific details rather than general descriptions
- **Mitigation:** Use multiple questions to verify consistency

**Issue: Low-resolution image performance**
- **Solution:** Ensure input images are at least 448×448 or larger
- **Note:** Images are resized to 448×448 internally

**Issue: Multiple image support**
- **Solution:** Process images separately and combine context manually
- **Status:** Multiple image input not currently supported

## Community & Support

### Official Resources
- **GitHub:** https://github.com/01-ai/Yi
- **HuggingFace:** https://huggingface.co/01-ai
- **Official Website:** https://01.ai
- **Technical Report:** https://arxiv.org/abs/2403.04652

### Community Channels
- GitHub Issues for bug reports
- HuggingFace Discussions for questions
- Twitter: @01ai_official for updates

## Related Models

### Yi Family
- **Yi-34B/6B:** Base language models
- **Yi-1.5:** Upgraded models with improved reasoning
- **Yi-Coder:** Specialized code generation models
- **Yi-Lightning:** Flagship frontier model

### Comparison with Yi-VL
- Yi-VL adds vision capabilities to base Yi models
- Maintains strong bilingual text performance
- Enables multimodal applications and research

## Future Directions

Potential improvements and research areas:
- Multi-image input support
- Higher resolution processing
- Video understanding capabilities
- 3D scene understanding
- Enhanced reasoning in complex scenes
- Reduced hallucination rates

## Release History

- **January 23, 2024:** Initial open-source release
- **Current Status:** Actively maintained and supported
- **Updates:** Community contributions and bug fixes ongoing
