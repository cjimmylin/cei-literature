# All-Model Comparison

This folder contains a standalone comparison of all benchmark runs currently present in `CULTURAL-GLOBAL/`.

Included model sets:
- Anthropic: Opus, Sonnet, Haiku
- OpenAI: GPT-5.4, GPT-5.4-mini
- Gemini: 2.5 Pro, 2.5 Flash, 2.5 Flash-Lite, 3.1 Pro, 3.1 Flash-Lite Preview

Artifacts:
- `generate_all_model_comparison.py`: standalone comparison generator
- `20260404-all-model-comparison-summary.json`: per-model summary and inventory validation
- `20260404-all-model-comparison-details.json`: pairwise agreement, divergence items, and trial-group slices
- `20260404-all-model-comparison-report.md`: narrative report

Notes:
- Outputs are isolated to this folder and do not modify the existing dashboard or analysis pipeline.
- Gemini runs are included as project artifacts, but their directories contain `simulate_trials.py`, so the report flags them as template-derived simulated corpora.
