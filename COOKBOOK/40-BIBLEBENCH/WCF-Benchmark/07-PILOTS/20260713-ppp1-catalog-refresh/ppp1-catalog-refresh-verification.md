# WCF-Bench PPP-1 catalog refresh verification

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

Result: **PASS** — metadata only; one catalog GET; zero inference calls.

- Exact roster: three SUTs (`meta-llama/llama-3.1-8b-instruct`, `deepseek/deepseek-chat`, `qwen/qwen3.7-plus`) and one judge (`google/gemini-2.5-flash`).
- Base prompt/completion prices: unchanged for all four models.
- Completion caps: SUT `2048`; judge `512`.
- Only catalog drift: Qwen override at `min_prompt_tokens=256000` with prompt/completion prices `0.00000096` / `0.00000384` and cache read/write prices `0.000000192` / `0.0000012`.
- Qwen prompt ceiling: `226/226` prompts checked using one token per UTF-8 byte over `EXAMINEE_SYSTEM + user prompt`; maximum `2221` at `MEND-C1-W301` (`1939` user + `282` system), leaving `253779` tokens of headroom.
- Refreshed catalog hash: `e97e482f8fc963ffe2e0743257e1d1041437ebdef1cbcf9babdb03c7b2d0318a`.
- Refreshed manifest SHA-256: `f1121b2bd279a83053f2521c99a45b4d116c1399da78776f515dceb4f210d796`.
