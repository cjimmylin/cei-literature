# CodeGeeX: Multilingual Code Generation Models

## Overview

CodeGeeX is Zhipu AI's family of multilingual code generation models, developed jointly with Tsinghua University and Huawei. The series provides open-source alternatives for code completion, generation, and understanding across 23+ programming languages.

## Model Versions

### CodeGeeX (2023)
- **Parameters**: 13 billion
- **Architecture**: Autoregressive transformer for code generation
- **Training Data**: 850 billion tokens across 23 programming languages (as of June 2022)
- **Key Innovation**: Multilingual code generation with strong performance across diverse programming languages
- **Conference/Publication**: KDD 2023
- **Technical Features**:
  - Pre-trained on 850B tokens of code
  - Support for 23 programming languages
  - HumanEval-X benchmark for multilingual evaluation
  - Strong zero-shot code generation capabilities
  - Cross-lingual code translation
- **Paper**: [CodeGeeX_2303.17568.pdf](CodeGeeX_2303.17568.pdf)
- **arXiv**: https://arxiv.org/abs/2303.17568

### CodeGeeX2 (2024)
- **Parameters**: 6 billion
- **Architecture**: More efficient architecture with improved multilingual capabilities
- **Training Data**: Additional 600 billion code tokens (1.45 trillion total)
- **Key Innovation**: Better performance than CodeGeeX-13B with less than half the parameters
- **Technical Features**:
  - Significant performance improvements over CodeGeeX-13B:
    - Python: +57% Pass@1
    - C++: +71% Pass@1
    - Java: +54% Pass@1
    - JavaScript: +83% Pass@1
    - Go: +56% Pass@1
  - Faster inference due to smaller size
  - Enhanced multilingual understanding
  - Better code completion quality
- **HuggingFace**: https://huggingface.co/THUDM/codegeex2-6b

### CodeGeeX3 (Upcoming)
- Status: Newer version referenced in 2024-2025 research but no dedicated arXiv paper yet published

## Key Capabilities

### Code Generation
- **Multilingual Support**: 23+ programming languages including Python, Java, C++, JavaScript, Go, Rust, etc.
- **Code Completion**: Real-time code suggestions and completions
- **Code Translation**: Cross-language code translation
- **Documentation**: Automatic code documentation generation

### Benchmarks
- **HumanEval-X**: Multilingual extension of HumanEval benchmark
- Competitive performance with CodeX and other commercial systems
- Strong results on functional correctness metrics

## Research Impact

The CodeGeeX series has contributed to:
- Open-source multilingual code generation
- HumanEval-X benchmark for multilingual code evaluation
- Efficient code models with strong performance-to-size ratios
- Cross-lingual code understanding and translation

## Technical Innovations

### HumanEval-X Benchmark
- Extension of HumanEval to multiple programming languages
- Consistent evaluation across languages
- Enables fair comparison of multilingual code models

### Training Approach
- Large-scale pre-training on diverse code corpora
- Careful data curation across programming languages
- Efficient architecture enabling better performance with fewer parameters

## IDE Integration

CodeGeeX provides plugins for:
- Visual Studio Code
- PyCharm
- IntelliJ IDEA
- Other popular IDEs

## Resources

- **Official Website**: https://codegeex.cn
- **GitHub**: https://github.com/THUDM/CodeGeeX
- **HuggingFace**: https://huggingface.co/THUDM/codegeex2-6b
- **VS Code Extension**: Available in VS Code Marketplace
- **API Platform**: https://open.bigmodel.cn

## Related Research

- **ChatGLM Series**: Foundation language models ([../GLM-4/](../GLM-4/))
- **NaturalCodeBench**: Natural code understanding benchmark ([Papers/NaturalCodeBench_2405.04520.pdf](../Papers/NaturalCodeBench_2405.04520.pdf))
- **ComplexFuncBench**: Complex function calling benchmark ([Papers/ComplexFuncBench_2501.10132.pdf](../Papers/ComplexFuncBench_2501.10132.pdf))

## Applications

- Code completion in IDEs
- Automated code generation
- Code translation between languages
- Programming education
- Code documentation
- Software development acceleration
- Research in code intelligence

## Performance Comparison

CodeGeeX2-6B demonstrates:
- Superior performance to CodeGeeX-13B despite smaller size
- Competitive with commercial code models
- Especially strong in Python, JavaScript, and Go
- Fast inference suitable for real-time IDE integration
