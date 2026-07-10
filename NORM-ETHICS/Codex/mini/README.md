# Codex NormEval Replication: Mini

This folder contains the mini-model Codex replication of the NormEval trials that already had Claude Opus, Sonnet, and Haiku coverage.

- Scope: `T6-T15`
- Model label: `gpt-5-mini (Codex agent)`
- Administration mode: direct agent reasoning in-session
- SDK/API usage: none
- Write boundary: all generated artifacts live under this `Codex/mini/` folder only

Contents:

- `results/`: per-trial GPT mini JSON outputs
- `reports/`: mini-specific cross-model comparison artifacts
- `build_codex_mini_outputs.py`: local generator for the files above
