# WCF-Bench PPP-1 zero-paid preflight

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

- SUT roster: meta-llama/llama-3.1-8b-instruct, deepseek/deepseek-chat, qwen/qwen3.7-plus
- Sole judge: google/gemini-2.5-flash
- Calls: 1722 total = 678 SUT + 1044 judge
- Initial / retry-reserved API attempts: 1722 / 3444
- Conservative forecast: $11.569859
- Minimum 80%-safe cap: $14.47
- Ratified strategy ceiling: $5.00
- Strategy ceiling feasible: false
- Current balance: $62.974009
- Required top-up: $0.00
- Runtime baseline: 265.5 minutes
- Runtime planning band: 212.4–354.0 minutes
- Paid inference calls: not authorized and not performed.

## Completion-cap branches

| Branch | SUT cap | Judge cap | Executable | Forecast | Minimum cap | Within $5 |
|---|---:|---:|:---:|---:|---:|:---:|
| judge_max_tokens_2048 | 2048 | 2048 | true | $11.569859 | $14.47 | false |
| judge_max_tokens_1024 | 2048 | 1024 | true | $8.897219 | $11.13 | false |
| judge_max_tokens_512 | 2048 | 512 | true | $7.560899 | $9.46 | false |
| judge_max_tokens_256 | 2048 | 256 | true | $6.892739 | $8.62 | false |
| zero_completion_price_floor | 0 | 0 | false | $5.247923 | $6.56 | false |

The zero-completion row is a non-executable price floor. No branch is selected by this preflight.

Canary: `WCFBENCH-CANARY-c1647-x9k4q`
