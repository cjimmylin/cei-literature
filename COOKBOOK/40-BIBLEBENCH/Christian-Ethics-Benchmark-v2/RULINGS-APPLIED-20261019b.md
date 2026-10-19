# RULINGS APPLIED — 2026-10-19b: judge-B input bound $0.80/M and in-flight reserve $0.30 for the 20261018b re-judge package

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-10-19
**Predecessor:** `RULINGS-APPLIED-20261019a.md`. Everything in it and in `-20261018b` stays in force
except the two parameters below. Newest ruling wins.

---

## What happened

The second `--live` start passed the launch-price check and ran **Stage 1a** to completion: d02
anchored, judges A+B, 468 calls, every call parsed, **$0.1903**. The runner then stopped before
Stage 1b, with the stop-and-report reason:

> stage 1a: a recorded job cost $0.00418 exceeds the $0.00413 per-job bound the in-flight reserve
> assumes (live prices above the bounds?)

**Cause.** OpenRouter routes judge-B (`meta-llama/llama-3.3-70b-instruct`) to several providers.
Some of them charge well above the model's listed $0.10/M input price.

- Stage 1a judge-B effective input cost per call: median $0.165/M, 90th percentile $0.204/M,
  maximum $0.713/M.
- The maximum was one call of 5,860 prompt tokens costing $0.00418.
- 4 of 234 judge-B calls cost more than $0.0015.
- Judge-A stayed at list price, with a maximum call of $0.00065.

Nothing was wrong with the spend accounting. The runner records OpenRouter's `usage.cost` for
every call ("actual" basis, 468/468). The per-job bound was simply sized on list prices.

## RULING — size the reserve for real prices

The owner was asked on 2026-10-19 and chose **"Size reserve for real prices"**. The other options
offered were pinning judge-B to a list-price provider, or stopping after Stage 1a.

Applied in `tools/audit/rejudge_package_20261018b.py`:

1. **`JUDGE_B_PRICE` = (0.80, 0.40) $/M**, previously (0.10, 0.40). It feeds:
   - the launch-price check (the live list price of $0.10/$0.32 is inside it);
   - the per-job bound (1a and 1b: $0.0321 per job, previously $0.0041);
   - the `--price-bound` passed to the d02 and d07 tools. The tools use it only when OpenRouter
     returns no `usage.cost`, so fallback costing is now conservative.
2. **`RESERVE_USD` = 0.30**, previously 0.10. The worst-case in-flight exposure for 8 workers at
   the new per-job bound is $0.257. The reserve must cover it, as the preflight requires. Each tool
   now receives `--ceiling` = 3.00 − 0.30 − spend, so the reserve makes the run stop *earlier*.

**Unchanged:**
- The **$3.00 hard ceiling** on projection and actual spend.
- The candidate bound $0.25/$1.00 and k ≤ 10.
- Prompts, models, items, analysis and the pre-committed read-outs `20261018d`.
- Zero SUT calls; the holdout is never read.
- D3–D7 remain open.

**Stage 1a is kept, not re-run.** The runner is resume-safe: recorded calls are skipped, and the
spend so far ($0.1903) counts against the same $3.00.

**Checks before resuming:**
- Offline suite: 16 passed. The tests now also assert that the worst observed job is inside both
  judge-B stage bounds, and that the reserve covers every stage.
- Dry run: OK, projection $0.6787, spent so far $0.1903.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
