# RULINGS APPLIED — 2026-10-19a: judge-B price bound amended to $0.10/$0.40 for the 20261018b re-judge package

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-10-19
**Predecessor:** `RULINGS-APPLIED-20261018b.md`. Everything in it stays in force except the one
bound below. Newest ruling wins.

---

## What happened

The first `--live` start of `tools/audit/rejudge_package_20261018b.py` (2026-10-19 09:35 UTC) stopped
at **$0.00**, before any paid call. The launch-price check read OpenRouter's model list and found:

| Model | Live price ($/M in/out) | Bound | Result |
|---|---|---|---|
| judge-A `openai/gpt-4.1-nano` | 0.10 / 0.40 | 0.10 / 0.40 | within |
| judge-B `meta-llama/llama-3.3-70b-instruct` | 0.10 / **0.32** | 0.10 / 0.30 | **exceeds** |
| judge-C `qwen/qwen3-235b-a22b-2507` | 0.09 / 0.55 | 0.25 / 1.00 | within (k = 1.375 vs judge-A) |

As the run guide requires, the runner stopped and reported. Nothing was spent. The record is in
`logs/rejudge-20261018b/summary.json` and `package_tally.json`.

## RULING — judge-B bound $0.10/$0.40

The owner was asked on 2026-10-19 and chose **"Raise bound to $0.40"**, leaving some headroom
against another small price change. The other options offered were $0.32 (today's price) and
stopping.

Applied as:
- `tools/audit/rejudge_package_20261018b.py`: `JUDGE_B_PRICE` = (0.10, 0.40). It feeds the
  launch-price check (`LIVE_BOUNDS`) and the in-flight reserve.
- Stages 1a (d02 tool) and 1b (d07 tool) now pass `--price-bound
  meta-llama/llama-3.3-70b-instruct=0.10,0.40`. The tools therefore cost judge-B calls at the same
  bound whenever OpenRouter returns no `usage.cost`. Both stages already write to new log roots
  under `logs/rejudge-20261018b/`, as an override requires. Prompts, models, items and analysis
  are unchanged.
- Test `test_stage_commands_carry_candidate_and_ceiling_but_no_key` now also checks that exactly
  the two judge-B stages carry the bound. Offline suite: 16 passed. Dry run: OK, projection
  $0.6787. That projection uses recorded per-call actuals, so it does not move.

**Unchanged:**
- The $3.00 hard ceiling (projection and actual), the $0.10 reserve and the calibration
  micro-runs;
- the candidate bound $0.25/$1.00 and k ≤ 10;
- zero SUT calls, the holdout never read, the pre-committed read-outs `20261018d`;
- D3–D7 remain open.

The tools' built-in `PRICE_BOUND` constants keep $0.10/$0.30. Default behaviour without the flag
is byte-identical, as Stage 0 established.

## Run environment (for the record)

The package ran from a Claude Code cloud session.
- **Inputs:** the stored run trees were copied from the owner's machine through a private
  repository (`cjimmylin/walkworthy-run-inputs`; holdout check: only the canary line mentions
  "holdout").
- **Python:** 3.14, because the stored `.eval` archives use Zstandard compression, which Python
  3.13's `zipfile` cannot read.
- **Key:** injected by the environment's network secret for `openrouter.ai`. No key file was
  read and no key value was printed or written.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
