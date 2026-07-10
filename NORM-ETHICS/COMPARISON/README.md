# NormEval Comparison

This folder contains cross-model comparison artifacts for the NormEval replicated trial group (`T6-T15`).

Included providers:

- Anthropic
- OpenAI
- Google

Structured per-item model runs included:

- `claude-sonnet-4-6`
- `claude-haiku-4-5`
- `gpt-5 (Codex agent)`
- `gpt-5-mini (Codex agent)`
- `gemini-2.5-flash`
- `gemini-2.5-flash-lite`
- `gemini-2.5-pro`
- `gemini-3.1-pro`

Metric-level baseline included:

- `claude-opus-4-6` via the existing `STATISTICS/20260404-normeval-cross-model-comparison.json`

Generated outputs:

- `20260404-normeval-all-models-comparison.json`
- `20260404-normeval-all-models-summary.md`

Generator:

- `generate_normeval_all_models_comparison.py`
