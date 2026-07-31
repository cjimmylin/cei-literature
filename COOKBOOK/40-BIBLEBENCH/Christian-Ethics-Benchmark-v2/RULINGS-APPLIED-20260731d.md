# RULINGS APPLIED — 2026-07-31d: validation run for the WW-v2-20260731b repairs AUTHORIZED ($3.00 ceiling)

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-07-31 · **Spend ceiling authorized by this ruling: $3.00.**
**Predecessors:** `RULINGS-APPLIED-20260731b.md` (repair ruling; produced instrument
`WW-v2-20260731b` with all repaired items UNVALIDATED) · `RULINGS-APPLIED-20260729d.md` ·
`RULINGS-APPLIED-20260729b.md`. All remain in force except where this ruling explicitly
extends them.

---

## RULING — the owner authorizes live validation of the repaired items (item 1 of the ROI memo)

Recorded from an interactive owner decision, 2026-07-31 ("proceed with item 1 with the
$3 ceiling"). The cost/ROI memo presented two open purchases; the owner takes item 1
only. Item 2 (the d02 taxonomy + classifier re-pin C6 bundle) remains NOT taken.

### What is authorized

- **Scope:** live administration of exactly the repaired surface of `WW-v2-20260731b` —
  the 13 repaired admin lines: `WW-05-L01#base`, `WW-03-L02#say`, `WW-03-L02#do`, and
  the ten design-04 lines of WW-04-B05 / WW-04-D03 / WW-04-E02 / WW-04-H04 / WW-04-I02
  (alpha + beta each). No other item may be administered.
- **Configuration = the pinned instrument, exactly:** the five SUTs of the frozen run
  (deepseek, mistral, gemini, llama, gpt41mini), 3 epochs, judge-A gpt-4.1-nano via the
  documented run-time override (never the code default), judge-B llama-3.3-70b rescore,
  pinned branch classifier where the design requires it.
- **Spend: hard ceiling $3.00** across all SUT, judge, and classifier calls combined.
  Pre-estimate before launching; if the projection or the running tally crosses the
  ceiling, STOP and report partial results. Exact tally from eval-log token counts in
  the report.
- **Purpose (validation, in this priority order):**
  1. WW-05-L01 — constraint read-out decidable (csr no longer collapsing to
     unscorable); evidence of spread rather than a new ceiling or floor.
  2. WW-03-L02 — revealed-faithful off the zero floor without saturating; expressed
     arm still keyed-scoreable.
  3. The five d04 conversions — complete alpha/beta pairs that score; deltas computable
     under the positive-keyed route; harshness guard read-out present.

### What this run is NOT

- **Not WALKWORTHY numbers.** No comparative system claim, no headline statistic, no
  Gate movement follows from this run. It validates instrument components only; its
  results are quotable solely as "the repaired items do / do not administer and
  discriminate as designed."
- **Not a reopening of any tier.** Gate A STOP unchanged; Tiers 1–3 closed; holdout
  quarantined and untouched (public bank lines only); pushback_rate and the C6 bundle
  closed.
- **Not a validation of the published record**, which remains a set of claims about
  `WW-v2-20260724b`.

### Success/failure recording

The validation report (new dated file, this per-day sequence) must state a per-item
verdict — VALIDATED / NOT VALIDATED / INDETERMINATE — against the purposes above, with
the raw per-cell table, and must update nothing in any prior report. If an item fails
validation, that is a recorded result, not a license to re-edit the item in this
session; further repair would be a new ruling.

### Verification gates

`lint_claims.py` 0 blockers · canary ≥ 2 per new artifact · exact spend tally vs the
$3.00 ceiling in the report · logs under `logs/` (gitignored) with the run tree named
for this ruling · commit by explicit path, message via `git commit -F`, verified with
`git log -1 --stat`.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
