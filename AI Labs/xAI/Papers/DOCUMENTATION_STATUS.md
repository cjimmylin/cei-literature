# xAI Documentation Status

**Last Updated:** 2026-01-31

## Summary

xAI has **not published any official technical papers or arxiv preprints** for their Grok model family. However, they have published **model cards for Grok 4 series models** starting in August 2025. This is still notably different from other major AI labs (OpenAI, Anthropic, Google DeepMind, Meta) which typically publish comprehensive technical reports alongside major model releases.

## Available Official Documentation

### Model Cards (PDF - Downloaded)

| Model | Documentation Type | Local Path | Source |
|-------|-------------------|-----------|--------|
| Grok 4 | Model Card PDF (Aug 20, 2025) | Grok-4/2025-08-20-grok-4-model-card.pdf | [data.x.ai](https://data.x.ai/2025-08-20-grok-4-model-card.pdf) |
| Grok 4 Fast | Model Card PDF (Sep 19, 2025) | Grok 4 Fast/2025-09-19-grok-4-fast-model-card.pdf | [data.x.ai](https://data.x.ai/2025-09-19-grok-4-fast-model-card.pdf) |
| Grok 4.1 | Model Card PDF (Nov 17, 2025) | Grok 4.1 Fast/2025-11-17-grok-4-1-model-card.pdf | [data.x.ai](https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf) |
| Grok Code Fast 1 | Model Card PDF (Aug 26, 2025) | Grok Code Fast/2025-08-26-grok-code-fast-1-model-card.pdf | [data.x.ai](https://data.x.ai/2025-08-26-grok-code-fast-1-model-card.pdf) |

### Web-Only Documentation

| Model | Documentation Type | Source |
|-------|-------------------|--------|
| Grok-1 | GitHub README with specs | [github.com/xai-org/grok-1](https://github.com/xai-org/grok-1) |
| Grok-1 | HuggingFace Model Card | [huggingface.co/xai-org/grok-1](https://huggingface.co/xai-org/grok-1) |
| Grok-1.5 | Blog Announcement | [x.ai/news/grok-1.5](https://x.ai/news/grok-1.5) |
| Grok-2 | Blog Announcement | [x.ai/news/grok-2](https://x.ai/news/grok-2) |
| Grok-3 | Web Model Card | [x.ai/model-card/grok-3](https://x.ai/model-card/grok-3) |
| All Models | Blog Posts | [x.ai/news](https://x.ai/news) |

## Known Technical Specifications

### Grok-1 (Only model with published architecture details)
- **Parameters:** 314B
- **Architecture:** Mixture of 8 Experts (MoE)
- **Experts per Token:** 2
- **Layers:** 64
- **Attention Heads:** 48 queries, 8 keys/values
- **Embedding Size:** 6,144
- **Tokenizer:** SentencePiece (131,072 tokens)
- **Context Length:** 8,192 tokens
- **License:** Apache 2.0

### Grok-1.5 (Blog Announcement - March 2024)
- **Context Length:** 128k tokens (16x increase from Grok-1)
- **MATH Benchmark:** 50.6%
- **GSM8K Benchmark:** 90%
- **HumanEval (Coding):** 74.1%
- **Infrastructure:** JAX, Rust, Kubernetes

### Grok-2 (Blog Announcement - August 2024)
- **Performance:** Competitive with Claude 3.5 Sonnet and GPT-4-Turbo
- **Vision:** State-of-the-art on MathVista and DocVQA
- **Variants:** Grok-2 and Grok-2 mini

### Other Models (Limited Public Information)
- **Grok-1.5V:** Multimodal (vision) capabilities
- **Grok-3:** 10x compute, DeepSearch, "Think" mode
- **Grok-4:** 256k context, agentic capabilities (PDF model card available)
- **Grok 4 Fast:** Fast inference variant (PDF model card available)
- **Grok 4.1 Fast:** 2M context window, tool calling (PDF model card available)
- **Grok Code Fast:** Specialized for agentic coding (PDF model card available)

## Third-Party Research Papers Mentioning Grok

The following arxiv papers reference xAI Grok models in their research:

| Paper Title | arxiv ID | Grok Model Referenced |
|------------|----------|----------------------|
| AI Transparency Atlas | 2512.12443 | Grok 4.1 |
| LLM-based Multi-class Attack Analysis | 2510.26941 | Grok 3 |
| Grokipedia vs Wikipedia Comparison | 2510.26899 | Grokipedia |
| ConsistencyAI Benchmark | 2510.13852 | Grok-3 |
| Deep Neural Networks Analysis | 2510.08591 | Grok-4 Heavy |
| LLM-Generated Code Evaluation | 2507.06463 | Grok 3-Think |
| Source Framing Bias Study | 2505.13488 | Grok 2 |
| Demystifying AI Agents | 2505.09932 | Grok (general) |
| Evaluating LLM Metrics | 2505.08253 | Grok |
| aiXamine Safety Platform | 2504.14985 | Grok-3 |

Note: These are independent research papers that evaluate or reference Grok models, not official xAI publications.

## Documentation Gaps

### Models WITHOUT PDF Model Cards
- **Grok-1** - Only GitHub README and HuggingFace card
- **Grok-1.5** - Only blog announcement (no PDF)
- **Grok-1.5V** - No dedicated documentation
- **Grok-2** - Only blog announcement (no PDF)
- **Grok-3** - Only web model card (no PDF download available)

### Models WITH PDF Model Cards (All Downloaded)
- Grok 4 (Aug 2025)
- Grok 4 Fast (Sep 2025)
- Grok 4.1 (Nov 2025)
- Grok Code Fast 1 (Aug 2025)

## Recommendations

1. **Monitor data.x.ai** for future model card PDFs
2. **Check x.ai/news** for blog announcements
3. **Watch for arxiv submissions** from xAI authors (currently none)
4. **Monitor x.ai/model-card/** for web-based model cards
5. **HuggingFace** may have updated model cards for future releases

## Why Limited Technical Documentation?

xAI's approach differs from other labs in that they:
1. Prioritize rapid deployment over academic publication
2. Focus on product integration with the X platform
3. May consider detailed architecture information as competitive advantage
4. Only published model cards starting with Grok 4 series (August 2025)
5. Grok-1 remains the only model with open weights; others are API-only
6. No technical papers or arxiv preprints as of January 2026
