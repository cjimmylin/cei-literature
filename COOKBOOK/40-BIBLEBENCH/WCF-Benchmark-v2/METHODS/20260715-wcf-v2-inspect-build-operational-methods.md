# Operational Methods — WCF-Benchmark-v2 on Inspect AI (2026-07-15)

Reproducible recipe for building/running the v2 harness. All paths relative to
`CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/` unless absolute.

## Step 1: Environment

**Command:**
```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2
/opt/homebrew/bin/python3.14 -m venv .venv-v2
./.venv-v2/bin/python -m pip install -r requirements.txt
./.venv-v2/bin/python -c "import inspect_ai; print(inspect_ai.__version__)"   # → 0.3.246
```
**Expected wall-clock:** ~1 min.
**Constraints:** inspect-ai needs Python ≥3.10 — the shared vault `.venv` (3.9.6) will NOT work. Always `python -m pip`, never bare pip (Apple Silicon venv issue). The `openai` package is REQUIRED for the OpenRouter provider (in requirements.txt).

## Step 2: Convert bank → datasets

**Command:**
```bash
./.venv-v2/bin/python convert/yaml_to_jsonl.py
```
**Expected output:** `data/wcf_main.jsonl` (204 items), `data/wcf_episodes.jsonl` (22 items); script exits non-zero on any count mismatch.
**Verification:** `./.venv-v2/bin/python -m pytest tests -q` → 5 passed.
**Source of truth:** `../WCF-Benchmark/05-BANK-YAML/` (read-only; 230 items, 4 dev_set_only excluded).

## Step 3: Offline pipeline check ($0)

**Command:**
```bash
./.venv-v2/bin/python -m inspect_ai eval src/wcf_tasks.py@wcf_main \
    --model mockllm/model -T grader_model=mockllm/model --limit 5 --log-dir logs
./.venv-v2/bin/python -m inspect_ai eval src/wcf_tasks.py@wcf_episodes \
    --model mockllm/model -T grader_model=mockllm/model --limit 3 --log-dir logs
```
**Expected:** status success; metrics show `nan` (mockllm grader emits no GRADE line → samples unscored — this is the PASS condition for plumbing, not a failure).
**Expected wall-clock:** ~2 s each.

## Step 4: Live run (OpenRouter)

**Command:**
```bash
set -a && source ~/.codex/secrets/openrouter.env && set +a   # OPENROUTER_API_KEY
./.venv-v2/bin/python -m inspect_ai eval src/wcf_tasks.py@wcf_main \
    --model openrouter/openai/gpt-4o-mini \
    -T grader_model=openrouter/google/gemini-2.5-flash \
    --limit 15 --log-dir logs
./.venv-v2/bin/python -m inspect_ai eval src/wcf_tasks.py@wcf_episodes \
    --model openrouter/openai/gpt-4o-mini \
    -T grader_model=openrouter/google/gemini-2.5-flash \
    --limit 5 --log-dir logs
```
**Measured this session:** 15 main items = 17 s, ≈$0.026; 9 by-id items ≈$0.015; 5 episodes = 21 s, ≈$0.009. Total 29 samples ≈ $0.05.
**Targeted samples:** use `--sample-id "COMP-C9-001,PROOF-C9-001,..."` instead of `--limit` (limit takes the FIRST N, which are all aggravate due to file sort order).
**Full-bank extrapolation:** ~$0.40–0.60 single SUT with this model pair.
**Resume protocol:** re-running an interrupted `inspect eval-set` with the same command resumes (completed samples skipped). Single `eval` runs are cheap enough to re-run whole.

## Step 5: Log inspection

```bash
./.venv-v2/bin/python -m inspect_ai view --log-dir logs     # web viewer, localhost:7575
```
Or the VS Code Inspect extension (auto-discovers `.venv-v2`); or programmatic via `inspect_ai.log.read_eval_log`.

## Inputs / Outputs

| Path | Schema | Size | Role |
|---|---|---|---|
| `../WCF-Benchmark/05-BANK-YAML/*.yaml` | v1 item schema (multi-doc YAML) | 40 files / 230 items | Source (read-only) |
| `data/wcf_main.jsonl` | id, design, track, tier, commandments, contested, episode, kind, stem, key, rubric, gold_order | 204 rows | wcf_main dataset |
| `data/wcf_episodes.jsonl` | same | 22 rows | wcf_episodes dataset |
| `logs/*.eval` | Inspect eval log | ~100 KB each | Audit trail |

## Failure modes encountered

**Error:** `OpenRouter API requires optional dependencies. Install with: pip install openai`
**Cause:** Inspect's OpenRouter provider rides on the openai SDK, not installed by inspect-ai itself.
**Fix:** `./.venv-v2/bin/python -m pip install openai` (now in requirements.txt).

**Design-time trap (avoided, documented):** `model_graded_qa(instructions="")` — empty string is falsy, Inspect silently substitutes its default C/P/I instructions, contradicting the numeric GRADE contract. Grading instructions must always be passed non-empty (they live in `src/templates/wcf_grade_instructions.txt`).

## Tunable parameters

- `-T grader_model=<provider/vendor/model>` — grader; keep cross-family from SUT; default `openrouter/google/gemini-2.5-flash`.
- `-T grader_temperature=<float>` — default 0.0.
- `--epochs N` — repeat sampling per item (untested in v2 so far).
- `TARGET_WARN_CHARS` in `wcf_tasks.py` (6000) — grading-standard length warning threshold.
- `PRESSURE_TURN` in `episode_solver.py` — the generic episode pressure text; the v2.1 upgrade path is per-item scripted turns.
