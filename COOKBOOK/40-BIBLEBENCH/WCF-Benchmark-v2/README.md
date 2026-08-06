# WCF-Benchmark-v2 — Inspect AI rebuild

> **This banner is historical** (original v2.0 build-out README; item counts and the
> scoring-model description below reflect the project's early state, not its current
> one). **For current status, read `INDEX.md`, not this file.** As of session 19–20
> (2026-07-31) the project shipped its first QUOTABLE results report and an
> owner-accepted v1.x paper draft — the "every number is exploratory and non-quotable"
> claim originally on this line no longer holds project-wide; it describes sessions
> 1–18 only. The Inspect `.eval` logs in `logs/` remain the audit trail.

## What this is

A rebuild of the WCF benchmark (conduct/counsel alignment with the Westminster
Standards) on the [Inspect AI](https://inspect.aisi.org.uk/) evaluation framework,
replacing the v1 bespoke harness (`../WCF-Benchmark/04-HARNESS/`, abandoned) whose
own retrospective concluded "infrastructure became the deliverable." Inspect provides
the runner, retries, resume, parallelism, logging, and viewer that v1 hand-rolled.

**Content provenance:** the item bank is converted from
`../WCF-Benchmark/05-BANK-YAML/` (read-only source of truth; 230 items → 226 runnable
after excluding 4 `dev_set_only`). Prompt frames (system prompt, Track A/B framing,
RANKING/ANCHOR format asks) are ported verbatim from v1 `promptbuilder.py`; scorer
routing precedence is ported from v1 `routing.py`.

## Layout

| Path | Role |
|---|---|
| `convert/yaml_to_jsonl.py` | Bank YAML → `data/*.jsonl` (regenerable; run after any bank change) |
| `data/wcf_main.jsonl` | 204 single-completion items (16 ordinal, 161 open, 4 contested, 23 anchor) |
| `data/wcf_episodes.jsonl` | 22 NARROWGATE episodes |
| `src/wcf_tasks.py` | Inspect tasks: `wcf_main`, `wcf_episodes` |
| `src/prompt_frames.py` | Verbatim v1 prompt content — do not edit casually |
| `src/episode_solver.py` | 2-generation scripted-pressure dialogue solver |
| `src/templates/` | Grading template + numeric grading instructions |
| `tests/test_converter.py` | Counts / leakage / routing invariants |
| `logs/` | Inspect `.eval` logs (audit trail) |
| `reports/` | `YYYYMMDD-` prefixed human summaries |

## Scoring model (v2.0, "simplest viable")

Every item — all five v1 scorer kinds — is graded by a **fixed separate grader model**
(`-T grader_model=...`, temperature 0, cross-family from the model under test by
convention) via `model_graded_qa`: the grader awards the item's weighted rubric
points against the gold key and emits `GRADE: <0-100>`.

**All reported metrics are means on a 0–100 scale, not accuracies.** Deliberately
dropped from v1: Kendall-τ ordinal scoring, triaxial Matter/Manner/End sub-scores,
refusal co-scorer, contested adherence scorer (contested items keep their metadata
flag for breakdowns but flow through the same grader). Episodes are flattened from
the v1 state machine to a single generic scripted pressure turn.

## Running

Environment: dedicated venv (`.venv-v2`, Python 3.14 — the vault's shared `.venv`
is 3.9 and cannot run inspect-ai). The VS Code Inspect extension auto-discovers it.

```bash
cd "$(dirname "$0")"   # the v2 root
PY=.venv-v2/bin/python

# 0. regenerate data + tests
$PY convert/yaml_to_jsonl.py && $PY -m pytest tests -q

# 1. offline pipeline check ($0) — grades show nan/unscored, expected
$PY -m inspect_ai eval src/wcf_tasks.py@wcf_main --model mockllm/model \
    -T grader_model=mockllm/model --limit 5 --log-dir logs

# 2. live (needs OPENROUTER_API_KEY in env or .env; slugs: openrouter/<vendor>/<model>)
$PY -m inspect_ai eval src/wcf_tasks.py@wcf_main \
    --model openrouter/openai/gpt-4o-mini \
    -T grader_model=openrouter/google/gemini-2.5-flash --limit 15 --log-dir logs

# 3. view logs
$PY -m inspect_ai view --log-dir logs
```

## Safety / conventions

- Never modify `../WCF-Benchmark/` or `../WCF/` from here; never delete files
  (superseded artifacts go to `RECYCLE-BIN/`).
- `.env` (API keys) and `.venv-v2/` are git-ignored; never commit them.
- Reports carry `YYYYMMDD-` prefixes and are immutable once written.
