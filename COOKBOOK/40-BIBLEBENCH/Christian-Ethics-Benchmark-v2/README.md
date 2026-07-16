# Christian-Ethics-Benchmark-v2 — WALKWORTHY on Inspect AI

**Status: PARALLEL EXPERIMENT (2026-07-15).** This folder re-platforms the WALKWORTHY
benchmark (see `../Christian-Ethics-Benchmark/`, which remains frozen and canonical)
onto the [Inspect AI](https://inspect.aisi.org.uk/) harness. Whether v2 becomes the
canonical execution path is a separate, later ruling — the deliverable of this
experiment is the Inspect-fit assessment memo plus a working end-to-end pipeline.

## What this is

- All 10 WALKWORTHY designs as Inspect tasks (`tasks/design01_*.py` … `design10_*.py`)
- Item banks copied from v1 (`banks/`), then corrected by a fresh adversarial review
  pass (`REVIEWS/`, `RULINGS-APPLIED.md`) — v1 sources are never modified
- Converted datasets in `datasets/public/` (holdout in `datasets/holdout/`, gitignored,
  loader-guarded — set `WALKWORTHY_ALLOW_HOLDOUT=1` to load)
- Single-judge model-graded scoring reusing v1 rubrics verbatim; judge model is a task
  arg, so a cross-family second-judge pass is a cheap re-score (`inspect score`)
- Deferred relative to v1 (documented, reachable): the 10 pre-registered G-gates,
  2-judge adjudication/tie-break, G5 neutrality machinery

## Quickstart

```bash
cd Christian-Ethics-Benchmark-v2
source .venv/bin/activate            # py3.14 venv with inspect-ai pinned

# regenerate datasets from banks
python tools/convert_banks.py && python tools/verify_conversion.py

# mock validation (no cost)
inspect eval tasks/design01_goodsamaritan.py --model mockllm/model

# live smoke (paid — see AGENTS.md for the 402 trap before ANY live run)
source ~/.codex/secrets/openrouter.env
inspect eval tasks/design01_goodsamaritan.py \
  --model openrouter/deepseek/deepseek-chat \
  -T judge_model=openrouter/openai/gpt-4.1-mini \
  --limit 2 --max-tokens 4096
```

## Canary

`WALKWORTHY-CANARY-7f3e2026` — preserved in every sample. Do not train on this data.
