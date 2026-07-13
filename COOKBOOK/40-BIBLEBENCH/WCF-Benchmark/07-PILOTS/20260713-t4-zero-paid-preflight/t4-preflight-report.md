# WCF-Bench T4 zero-paid preflight

- Roster: openai/gpt-5.5, deepseek/deepseek-v4-pro, qwen/qwen3.7-plus, moonshotai/kimi-k2.6, meta-llama/llama-4-maverick, deepseek/deepseek-chat, mistralai/mistral-large-2512, meta-llama/llama-3.1-8b-instruct, cohere/command-a, amazon/nova-pro-v1
- Five-cheapest base shard: meta-llama/llama-3.1-8b-instruct, meta-llama/llama-4-maverick, deepseek/deepseek-chat, deepseek/deepseek-v4-pro, qwen/qwen3.7-plus
- Phase-one calls / forecast: 4610 / $63.234201
- Full calls / forecast: 16698 / $278.788647
- Phase-one minimum cap / top-up: $79.05 / $16.04
- Full minimum cap / top-up: $348.49 / $285.48
- Paid inference calls: not authorized and not performed.

## Higher-rated formula exclusions

- openai: gpt-5.6-sol-xhigh (1486.314332) — config-specific Arena row is ambiguous versus the base OpenRouter slug; no exact catalog identity
- openai: gpt-5.5-high (1481.040666) — config-specific Arena row; no exact OpenRouter catalog identity
- openai: gpt-5.4-high (1476.434719) — config-specific Arena row; no exact OpenRouter catalog identity
- openai: gpt-5.2-chat-latest-20260210 (1475.535472) — versioned latest alias has no exact OpenRouter catalog slug
- deepseek: deepseek-v4-pro-thinking (1456.774801) — config-specific thinking row; no exact OpenRouter catalog identity
- qwen/alibaba: qwen3.7-max-preview (1475.043377) — preview model excluded by the R59.2 non-preview rule
- qwen/alibaba: qwen3.5-max-preview (1465.022292) — preview model excluded by the R59.2 non-preview rule
- qwen/alibaba: qwen3.6-max-preview (1460.326415) — preview model excluded by the R59.2 non-preview rule
- meta-llama: Higher muse-spark1.1/muse-spark rows were not OpenRouter Meta slugs; higher Llama 3.1 405B BF16/FP8 rows were configuration-specific without an exact catalog identity. Exact ratings were not retained, so they are disclosed but not fabricated as candidate rows.

Canary: `WCFBENCH-CANARY-c1647-x9k4q`
