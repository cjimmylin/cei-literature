# Claude 3.7 Sonnet

## Overview
Hybrid reasoning model introducing "extended thinking" mode that allows Claude to reason at length before providing answers. Trained via reinforcement learning to produce chains of thought. First model to offer both instant responses and extended reasoning in a single model.

## Technical Specifications
- **Release Year:** 2025 (February)
- **Version:** 3.7
- **Knowledge Cutoff:** October 2024
- **Context Window:** 200k tokens
- **Model ID:** `claude-3-7-sonnet-20250219`
- **Key Feature:** Extended thinking mode for improved reasoning

## Documentation & Links

### Blog Posts & Announcements
- [Introducing Claude 3.7 Sonnet](https://www.anthropic.com/news/claude-3-7-sonnet) - Official announcement
- [Extended Thinking Announcement](https://www.anthropic.com/news/claude-3-7-sonnet) - Extended thinking feature details

### API Documentation
- [Extended Thinking Models](https://docs.anthropic.com/en/docs/about-claude/models/extended-thinking-models) - Extended thinking documentation
- [Models Overview](https://docs.anthropic.com/en/docs/about-claude/models) - Claude models documentation
- [All Models](https://docs.anthropic.com/en/docs/about-claude/models/all-models) - Complete model specifications
- [Extended Thinking Guide](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) - How to use extended thinking
- [Vision Guide](https://docs.anthropic.com/en/docs/build-with-claude/vision) - Image understanding documentation
- [Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) - Function calling documentation
- [API Reference](https://docs.anthropic.com/en/api/messages) - Messages API reference

### System Card
- [Claude 3.7 Sonnet System Card (PDF)](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf) - System card with extended thinking, safety evaluations, prompt injection analysis, RSP compliance

### Benchmarks & Evaluations
| Benchmark | Standard Mode | Extended Thinking |
|-----------|---------------|-------------------|
| MATH | 78.3% | 96.2% |
| GPQA Diamond | 68.0% | 84.8% |
| SWE-bench Verified | 49.0% | 62.3% |
| HumanEval | 93.7% | 97.0% |

### Key Features
- **Extended Thinking Mode:** Allows Claude to think through complex problems step-by-step before responding
- **Hybrid Architecture:** Same model supports both fast responses and deep reasoning
- **Streaming Thinking:** Can stream thinking blocks during extended reasoning
- **Budget Control:** Configurable thinking budget for cost/quality tradeoffs

### Research
- [Extended Thinking Research](https://www.anthropic.com/research/extended-thinking) - Research on chain-of-thought reasoning
- [Anthropic Research](https://www.anthropic.com/research) - Research publications

### Related Links
- [Claude Sonnet Product Page](https://www.anthropic.com/claude/sonnet) - Product information
- [Pricing](https://www.anthropic.com/pricing) - API pricing information
- [Anthropic Transparency Hub](https://www.anthropic.com/transparency) - Transparency reports

## Papers
| Paper | Description | Local PDF |
|-------|-------------|-----------|
| Claude 3.7 Sonnet System Card | Covers extended thinking, safety evaluations, prompt injection analysis, and RSP compliance | [PDF](Claude_3.7_Sonnet_System_Card.pdf) |
