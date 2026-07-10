# Codex NormEval Replication

This folder contains a Codex-administered GPT replication of the NormEval trials that already had Claude Opus, Sonnet, and Haiku coverage.

- Scope: `T6-T15`
- Model label: `gpt-5 (Codex agent)`
- Administration mode: direct agent reasoning in-session
- SDK/API usage: none
- Write boundary: all generated artifacts live under this `Codex/` folder only

Contents:

- `results/`: per-trial GPT JSON outputs
- `reports/`: Codex-only comparison summary and machine-readable comparison JSON
- `build_codex_outputs.py`: local generator used to emit the files above from the direct Codex judgments
