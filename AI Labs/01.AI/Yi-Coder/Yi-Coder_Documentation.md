# Yi-Coder: Complete Technical Documentation

**Source:** GitHub Repository (https://github.com/01-ai/Yi-Coder) and HuggingFace Model Cards
**Date Extracted:** January 31, 2026
**Reference Paper:** Yi: Open Foundation Models by 01.AI (arXiv:2403.04652)

## Overview

Yi-Coder is an open-source code language model series that delivers state-of-the-art coding performance with fewer than 10 billion parameters. Released by 01.AI in September 2024, Yi-Coder represents a significant advancement in efficient code generation models.

## Model Variants

| Model | Type | Parameters | Context Length | Tensor Type | License |
|-------|------|-----------|----------------|-------------|---------|
| Yi-Coder-9B-Chat | Instruction-tuned | 9B | 128K tokens | BF16 | Apache 2.0 |
| Yi-Coder-1.5B-Chat | Instruction-tuned | 1.5B | 128K tokens | BF16 | Apache 2.0 |
| Yi-Coder-9B | Base | 9B | 128K tokens | BF16 | Apache 2.0 |
| Yi-Coder-1.5B | Base | 1.5B | 128K tokens | BF16 | Apache 2.0 |

All models are available on HuggingFace, ModelScope, and Wisemodel platforms.

## Supported Programming Languages

Yi-Coder supports **52 major programming languages**, including:

### Core Languages
- Python, Java, C++, C#, JavaScript, TypeScript, Go, Rust

### Web Development
- HTML, CSS, PHP, JavaScript

### Specialized Languages
- SQL, Kotlin, Swift, Ruby, R, Scala, and 36 additional languages spanning functional, scripting, and compiled paradigms

## Key Capabilities

### Long-Context Understanding
- Maximum context window: **128K tokens**
- Enables understanding of large codebases and extended conversations
- Supports complex code generation tasks requiring extensive context

### Multilingual Support
- Comprehensive coverage of 52 programming languages
- Consistent performance across multiple language families
- Strong cross-language translation capabilities

### Efficient Architecture
- Delivers performance comparable to much larger models
- Optimized for both quality and computational efficiency
- Fewer than 10B parameters while maintaining state-of-the-art results

## Benchmark Performance

### LiveCodeBench (Industry-Leading Results)
**Yi-Coder-9B-Chat:**
- **23% pass rate** - Only model under 10B parameters to exceed 20%
- **Outperforms significantly larger models:**
  - DeepSeekCoder-33B-Ins: 22.3%
  - CodeGeex4-9B-all: 17.8%
  - CodeLLama-34B-Ins: 13.3%
  - CodeQwen1.5-7B-Chat: 12%

### Multi-lingual HumanEval (Base Models - 9B variant)
| Language | Pass Rate |
|----------|-----------|
| Python | 53.7% |
| C++ | 59.6% |
| TypeScript | 57.9% |
| C# | 58.2% |
| **Average** | **49.6%** |

### Math Programming (9B variant)
| Benchmark | Score |
|-----------|-------|
| GSM8k | 68.1% |
| MATH | 29.1% |
| TabMWP | 81.2% |
| MAWPS | 93.9% |
| **Average** | **70.3%** |

### CodeEditorBench Primary (9B-Chat)
- **Average Win Rate: 78.57%**
- Excellent performance across:
  - Debug tasks
  - Code translation
  - Code refactoring

## Installation & Setup

### System Requirements
```bash
Python >= 3.9
CUDA-compatible GPU (recommended)
```

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/01-ai/Yi-Coder.git
cd Yi-Coder

# Install dependencies
pip install -r requirements.txt
```

## Usage Examples

### Using Transformers (HuggingFace)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

device = "cuda"  # or "cpu"
model_path = "01-ai/Yi-Coder-9B-Chat"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto"
).eval()

# Prepare prompt
prompt = "Write a quick sort algorithm in Python."
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": prompt}
]

# Generate text
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(device)
generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=1024,
    eos_token_id=tokenizer.eos_token_id
)

# Decode response
response = tokenizer.batch_decode(
    [output_ids[len(input_ids):]
     for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)],
    skip_special_tokens=True
)[0]

print(response)
```

### Using vLLM (Fast Serving)

```python
from vllm import LLM, SamplingParams

# Initialize model
llm = LLM(model="01-ai/Yi-Coder-9B-Chat")

# Set sampling parameters
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.95,
    max_tokens=1024
)

# Generate
prompts = ["Write a binary search function in C++."]
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    print(output.outputs[0].text)
```

### Using Ollama (Local Deployment)

```bash
# Pull the model
ollama pull yi-coder:9b-chat

# Run inference
ollama run yi-coder:9b-chat "Write a REST API in Python using FastAPI"
```

## Deployment Options

### Available Platforms
1. **HuggingFace Hub** - https://huggingface.co/01-ai
   - Direct model downloads
   - Integration with Transformers library
   - Model cards and documentation

2. **ModelScope** - Chinese model hosting platform
   - Optimized for Chinese users
   - Fast download speeds in Asia

3. **Wisemodel** - Alternative model repository
   - Additional deployment options

### Inference Frameworks
- **Transformers**: Standard HuggingFace integration
- **vLLM**: High-throughput serving with optimized inference
- **Ollama**: Easy local deployment and testing
- **Custom**: Apache 2.0 license allows custom deployment

## Model Architecture

Based on the Yi foundation model architecture with code-specific optimizations:
- Transformer-based decoder architecture
- Enhanced for code understanding and generation
- Optimized tokenization for programming languages
- Extended context window (128K tokens)

## Training Data

Yi-Coder is trained on:
- High-quality code repositories
- Programming documentation
- Code-related Q&A pairs
- Multiple programming languages
- Technical documentation

Training methodology emphasizes:
- Data quality over quantity
- Diverse programming paradigms
- Real-world code patterns
- Clean, well-documented examples

## License

**Apache 2.0 License**
- Commercial use permitted
- Modification and distribution allowed
- Attribution required to 01.AI
- No warranty provided

## Community & Support

### Official Resources
- **GitHub**: https://github.com/01-ai/Yi-Coder
- **HuggingFace**: https://huggingface.co/01-ai
- **Blog**: https://01-ai.github.io/
- **Official Website**: https://01.ai

### Community Channels
- Discord server for discussions
- Twitter: @01ai_official
- WeChat groups for Chinese users

## Citation

If using Yi-Coder in research, please cite:

```bibtex
@article{yi2024coder,
  title={Yi: Open Foundation Models by 01.AI},
  author={01.AI Team},
  journal={arXiv preprint arXiv:2403.04652},
  year={2024}
}
```

## Additional Notes

### Release Information
- **Initial Release:** September 5, 2024
- **Current Status:** Actively maintained
- **Updates:** Regular model improvements and bug fixes

### Known Limitations
- Performance varies by programming language
- Context window limitations for extremely large codebases
- May require fine-tuning for domain-specific tasks

### Best Practices
1. Use chat variants for interactive coding assistance
2. Leverage full 128K context for large code analysis
3. Fine-tune on domain-specific code for specialized tasks
4. Consider vLLM for production deployments requiring high throughput
5. Use appropriate sampling parameters (temperature, top_p) based on task

## Related Models

- **Yi-Lightning**: Flagship frontier model with enhanced capabilities
- **Yi-VL**: Vision-language variant for multimodal tasks
- **Yi-1.5**: Upgraded foundation models with improved reasoning
- **Yi-34B/6B**: Base foundation models
