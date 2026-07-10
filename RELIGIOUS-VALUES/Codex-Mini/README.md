# Codex Mini Benchmark Replication

This folder contains Codex/GPT mini-model benchmark outputs for the
`RELIGIOUS-VALUES` project.

Constraints followed:
- No existing project files were modified.
- All new artifacts live under `Codex-Mini/`.
- Benchmark administration was performed by the Codex mini agent itself, not via SDK or API.

Contents:
- `data/`: copied immutable benchmark inputs used for Codex mini runs
- `trials/`: copied blinded T2 administration and gold files
- `results/`: Codex mini responses, rubric scores, and aggregate summaries
- `scripts/`: Codex-mini-local scoring and validation utilities
- `logs/`: execution notes

Model label used in output files:
- `gpt-codex-mini`

Method notes:
- Construct-validity trials mirror the existing 3-tradition split:
  Islam, Christianity, Hinduism
- T2 uses `20260404-trial-T2-sample-30-admin.json` for administration and
  joins with `20260404-trial-T2-sample-30-gold.json` only during scoring
