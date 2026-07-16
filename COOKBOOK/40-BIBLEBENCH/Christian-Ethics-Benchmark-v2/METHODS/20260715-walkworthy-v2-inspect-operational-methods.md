# Operational Methods — WALKWORTHY v2 on Inspect AI (2026-07-15)

Reproducible runbook for the v2 pipeline. `V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2`.

### Step 1: Environment

**Command:**
```bash
cd "$V2"
/opt/homebrew/bin/python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt   # inspect-ai==0.3.246, openai
```
**Expected wall-clock:** ~1 min. **Verification:** `.venv/bin/python -c "import inspect_ai; print(inspect_ai.__version__)"` → `0.3.246`.
**Note:** the vault `.venv` (Python 3.9) cannot host inspect-ai; always use this local venv.

### Step 2: Convert banks → datasets

**Command:**
```bash
cd "$V2"
.venv/bin/python tools/convert_banks.py        # defaults: banks/, banks-holdout/ → datasets/
.venv/bin/python tools/verify_conversion.py    # write NEW dated report, never overwrite old ones
```
**Expected wall-clock:** seconds. **Expected outputs:** `datasets/public/design01..10.jsonl` (575 lines total, 344 runnable items), `datasets/holdout/…` (260 lines, gitignored), dated parity report.
**Verification:** report says 344 runnable public items, per-design counts match the v1 O4 manifest, 835 unique ids, canary 100%, public/holdout disjoint.

### Step 3: Mock validation (zero cost)

**Command:**
```bash
cd "$V2"
for t in tasks/design*.py; do
  .venv/bin/inspect eval "$t" --model mockllm/model -T judge_model=mockllm/model \
    --limit 5 --log-dir logs/mock-$(date +%Y%m%d)/
done
```
**Expected wall-clock:** ~2–4 min for all 10. **Verification:** every eval `status=success`; `inspect view --log-dir logs/mock-…` shows full multi-turn transcripts for designs 02/07.

### Step 4: Live smoke (paid — read AGENTS.md rule 1 first)

**Command:**
```bash
cd "$V2"
source ~/.codex/secrets/openrouter.env    # exports the OpenRouter key
for t in tasks/design*.py; do
  .venv/bin/inspect eval "$t" \
    --model openrouter/deepseek/deepseek-chat \
    -T judge_model=openrouter/openai/gpt-4.1-mini \
    --limit 2 --max-tokens 4096 --max-connections 4 \
    --log-dir logs/smoke-$(date +%Y%m%d)/
done
```
**Expected wall-clock:** ~10–20 min. **Measured 2026-07-15:** 10/10 success, 80,537 tokens, **≈ $0.038**.
**Verification:** every eval `status=success`; judge JSON parseable on scored samples; no 402 errors.
**Resume protocol:** Inspect retries/resumes natively; re-running the same command skips completed logs if using `inspect eval-retry <log>`.

### Inputs

| Path | Schema | Size | Source |
|---|---|---|---|
| `banks/*.md` (20) | fenced-YAML items in markdown | 10 designs | copied from v1 DESIGNS/, review-fixed 2026-07-15 |
| `banks-holdout/*.md` (10) | same | gitignored | copied from v1 HOLDOUT/, review-fixed |
| `tools/SCHEMA.md` | contract | — | frozen 2026-07-15 |

### Outputs

| Path | Schema | Size | Consumed by |
|---|---|---|---|
| `datasets/public/designNN.jsonl` | SCHEMA.md lines (admin-level) | 575 lines | `walkworthy_inspect.datasets` |
| `datasets/holdout/designNN.jsonl` | same | 260 lines; env-guarded | holdout runs only |
| `logs/**/*.eval` | Inspect log format | ~MBs | `inspect view`, `inspect score`, gate scripts |

### Failure modes encountered (this session)

- **Error:** design-05 CSR would mechanically zero. **Cause:** `é` in allocation tokens (A03/M04) unmatched by parser regex. **Fix:** review pass renamed tokens to ASCII in banks.
- **Error:** designs 06/09 judge prompts unanchored (empty keyed content). **Cause:** scorers guessed `metadata.keyed` sub-key names before real data existed. **Fix:** consumer-side reconciliation against actual emitted keys; fixtures regenerated from real data.
- **Observation:** deepseek-chat answers design-05 in prose (no allocation block) → CSR `unscorable`. This is SUT format-noncompliance signal, not a harness bug (verified with synthetic compliant answers).
- **Latent edge (open):** `parsers.py::reparse_allocation_response` logs `allocation_ok=True/values={}` on block-less answers; offline re-parse is correct. Needs a parser pass.

### Tunable parameters

- `judge_model` (task arg) = `openrouter/openai/gpt-4.1-mini`; change for cross-family re-score (`inspect score`), never needs SUT re-run.
- `--max-tokens` = 4096; raise to 8192 for verbose designs; NEVER omit (OpenRouter 402 reservation trap).
- `--limit` = per-sample; use multiples of a design's admin-group size to avoid splitting pairs in real pilots.
- `WALKWORTHY_ALLOW_HOLDOUT=1` — required env to load holdout datasets; leave unset otherwise.
- `--max-connections` = 4 for smokes; raise cautiously for panels.
