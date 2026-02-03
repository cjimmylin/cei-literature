# DeepSeekMath

## Overview
DeepSeekMath is DeepSeek's series of specialized language models focused on mathematical reasoning. The models push the limits of mathematical problem-solving in open-source LLMs.

## Model Versions

### DeepSeekMath (February 2024)
- **arXiv:** 2402.03300
- **Release Date:** February 2024
- **Key Achievement:** 51.7% on competition-level MATH benchmark without external toolkits or voting
- **Key Features:**
  - Specialized mathematical reasoning capabilities
  - No reliance on external computational tools
  - Strong performance on competition mathematics
- **Model Sizes:** 7B parameters

### DeepSeekMath-V2 (November 2025)
- **arXiv:** 2511.22570
- **Release Date:** November 2025
- **Subtitle:** "Towards Self-Verifiable Mathematical Reasoning"
- **Key Achievements:**
  - Gold-level scores on IMO 2025 and CMO 2024
  - Near-perfect 118/120 on Putnam 2024 with scaled test-time compute
  - Strong theorem-proving capabilities
- **Key Features:**
  - Self-verifiable reasoning approach
  - Advanced test-time compute scaling
  - Olympic-level mathematics performance

## Research Papers

All papers are available in this directory:
- `DeepSeekMath_arxiv_2402.03300.pdf` - Original DeepSeekMath
- `DeepSeekMath-V2_arxiv_2511.22570.pdf` - Second generation with self-verification

## Note on ACL 2024
While DeepSeekMath is highly regarded in the research community, it did NOT receive an ACL 2024 Best Paper Award. The ACL 2024 Best Paper Awards went to other works on memorization profiles and multilingual language models.

## Key Innovations

1. **Mathematical Specialization:** Purpose-built for mathematical reasoning tasks
2. **Self-Verification (V2):** Ability to verify its own mathematical reasoning
3. **Test-Time Compute Scaling:** DeepSeekMath-V2 effectively uses additional compute at inference time
4. **Competition-Level Performance:** Achieves gold medals on international mathematics olympiads

## Benchmark Performance

### DeepSeekMath V1
- MATH: 51.7%
- No external tools or voting required

### DeepSeekMath V2
- IMO 2025: Gold level
- CMO 2024: Gold level
- Putnam 2024: 118/120 (near-perfect)

## Links

- **GitHub:** [github.com/deepseek-ai/DeepSeek-Math](https://github.com/deepseek-ai/DeepSeek-Math)
- **Hugging Face:** [deepseek-ai math models](https://huggingface.co/deepseek-ai)
