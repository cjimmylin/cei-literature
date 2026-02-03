# Nemotron-3-Nano-30b-a3b Model Card

## Overview
The Nemotron-3-Nano-30b-a3b is an open, efficient mixture-of-experts (MoE) model developed by NVIDIA, featuring a 1-million token context window.

## Key Capabilities
According to the documentation, this model excels in:
- Coding tasks
- Reasoning and logical analysis
- Instruction following
- Tool calling and function integration
- Extended context understanding

## Model Architecture
The model employs a mixture-of-experts architecture, allowing for efficient parameter distribution and specialized task handling across different expert modules.

## Technical Specifications
- **Context Window**: 1 million tokens
- **Max Output Tokens**: Up to 32,768 tokens
- **Temperature Range**: 0-1 (default: 1)
- **Top-p Sampling**: Configurable (default: 1)

## Deployment Options
The model supports multiple deployment methods:
- **NVIDIA NIM** (Neural Inference Microservice) via API
- **Local Docker Deployment** with GPU support
- **OpenAI-compatible** REST API interface

## Reasoning Capabilities
The model supports internal reasoning/thinking with configurable budgets, enabling complex problem-solving with "a maximum number of tokens the model is allowed to use for internal reasoning."

## Licensing
The model operates under the NVIDIA Nemotron Open Model License Agreement and the NVIDIA API Trial Terms of Service.

## API Access
Available through `https://integrate.api.nvidia.com/v1/` with support for streaming and non-streaming chat completions.

## Resources
- Model Card: https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard
- Hugging Face: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
- Technical Report: Nemotron-3-Nano-Technical-Report.pdf
- White Paper: Nemotron-3-White-Paper.pdf
