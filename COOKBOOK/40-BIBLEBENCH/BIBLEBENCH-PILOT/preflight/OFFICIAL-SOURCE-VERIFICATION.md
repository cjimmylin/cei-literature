# PF-002 Official-Source Verification

Status: `PUBLIC_DOCUMENTATION_ONLY`

Verified: 2026-07-13

This record verifies the proposed PF-002 roster from public, first-party
documentation only. No credential, provider API, model, or billing surface was
accessed. Provider calls: **0**. Spend: **$0.00**.

| Actor | Exact model | Standard text price per 1M tokens | Limits | First-party family |
|---|---|---:|---:|---|
| actor-alpha | `gpt-5-nano-2025-08-07` | $0.05 input / $0.40 output | 400,000 context / 128,000 output | Responses |
| actor-beta | `gemini-2.5-flash-lite` | $0.10 input / $0.40 output | 1,048,576 input / 65,536 output | Generate Content |
| actor-gamma | `claude-haiku-4-5-20251001` | $1.00 input / $5.00 output | 200,000 context / 64,000 output | Messages |

## Official evidence

- OpenAI: [GPT-5 nano model](https://developers.openai.com/api/docs/models/gpt-5-nano)
  identifies the exact snapshot, price, context window, maximum output, and
  Responses endpoint. [Text generation](https://platform.openai.com/docs/guides/text-generation)
  documents the Responses API as the recommended text-generation family.
- Google: [Gemini 2.5 Flash-Lite model](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite)
  identifies the stable model code and token limits. [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
  gives the standard paid-tier text input/output prices. [Generating content](https://ai.google.dev/api/generate-content)
  documents the Generate Content family.
- Anthropic: [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
  identifies the exact Claude API ID, price, context window, and maximum output.
  [Messages reference](https://docs.anthropic.com/en/api/messages) identifies the
  first-party Messages API family.

These facts establish proposal eligibility only. They are not an availability
probe, account entitlement check, authorization record, or permission to call
any model.
