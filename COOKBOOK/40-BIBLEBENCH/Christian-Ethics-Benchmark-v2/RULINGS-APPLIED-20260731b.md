# RULINGS APPLIED — 2026-07-31b: decision-menu item 2 OPENED — scoped instrument-repair ruling ($0, one bundled version)

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-07-31 · **Spend authorized by this ruling: $0.**
**Predecessors:** `RULINGS-APPLIED-20260729d.md` (Tier 0 authorized; bank/scorer changes and
item authoring explicitly withheld pending their own authorization — this ruling IS that
authorization, for the scope below only) · `RULINGS-APPLIED-20260729b.md` (holdout quarantine
RATIFIED) · `RULINGS-APPLIED-20260729.md` · `RULINGS-APPLIED-20260725c.md`. All remain in
force except where this ruling explicitly supersedes.

---

## RULING — the owner opens decision-menu item 2 (repair ruling for documented defects)

Recorded from an interactive owner decision, 2026-07-31 (structured-question channel).
The decision menu is `20260730j-boot-prompt-reentry-gate-a-stopped.md` §5, carried forward
by `20260731-boot-prompt-reentry-consolidated.md` §2. Item 1 (paper-c) was already complete;
item 3 (reopen a tier) was offered and NOT taken.

**The Gate A STOP is not reversed.** The stop criterion fired on the Tier 0 evidence and
stands. This ruling opens the *instrument-repair* queue as a new-instrument-version
decision — it authorizes no measurement, changes no published number, and leaves every
Tier 0 / paper-c claim exactly as shipped (those artifacts describe `WW-v2-20260724b`
and remain immutable and correct about it).

### Authorized scope — three repairs, and nothing else

1. **`walkworthy_inspect/metrics.py` docstring correction.** The docstring calling
   exemplars "gold-standard references" is known wrong (spec-bank exemplar items run live
   per system — `tools/convert_banks.py:490`). Correct the docstring. No behavior change.
   This supersedes the "deliberately uncorrected" status recorded in the consolidated
   boot prompt §4 item 2, which existed only because code edits were gated.

2. **d03 judge synonym-key extraction fix.** Per `20260730h` §5: 6 of 990 administrations
   fail forced-choice extraction by one mechanism — the judge's JSON used a synonym key
   (observed: `classified_judgment`, `interpreted_judgment`, `explained_judgment`,
   `represented_judgment`, `mentioned_judgment`, `indicated_judgment`) instead of the
   schema key `expressed_judgment`, and coercion found no match. Authorized: extend the
   coercion to accept `*_judgment` synonym keys, with the schema key taking precedence.
   **Verification is frozen-log re-extraction only** (stored judge JSON under
   `logs/fullbank-3ep-20260724/`) — zero model calls. Characterization tests that pin the
   old miss behavior may be updated, each change documented in the session report.

3. **Bank item repairs, $0 edits only.**
   - **WW-05-L01** (design 05): coverage-starved — csr_undecidable in 13 of 15 cells
     under both judges; mistral, gemini, llama have no scored administration in any
     epoch (`20260730e` §6.1). Rework the item so the constraint read-out is decidable.
   - **WW-03-L02** (design 03): zero-pass — 0 of 14 scored cells faithful under each
     judge, no cell anywhere faithful (`20260730e` §6.2). Rework the item.
   - **Five twinless d04 items** — WW-04-B05, WW-04-D03, WW-04-E02, WW-04-H04,
     WW-04-I02: single `base` administration, no alpha/beta twin, 0 of 15 under both
     judges, excluded from every design-04 aggregate (denominator 24, not 29)
     (`20260730e` §5). Author the missing twin administrations.
   - Every repaired or newly authored line carries the canary; no holdout content may
     be consulted or echoed; the v1 sibling stays read-only.

### Versioning — ONE bundled successor version

All three repairs land together as a single successor instrument version to
`WW-v2-20260724b` (new `bank_revision` dated this ruling; version ID assigned at
re-stamp). `INSTRUMENT.json` is re-stamped over the repaired tree;
`tools/verify_instrument.py` must return ALL PASS against the new stamp, and the stamp
must continue to declare the holdout quarantined, not hashed, not counted, not read.
Per C6 discipline, partial landings are prohibited: either all three repairs ship in the
one version or the version does not ship.

### NOT authorized by this ruling

- **Any spend. Any model call** — SUT, judge, or classifier. $0 strictly.
- **Live validation of the repaired items.** Repaired and newly authored items ship
  marked **UNVALIDATED pending live administration**; no repaired item may enter any
  published statistic until a future ruling authorizes validation runs.
- **The d02 taxonomy revision + classifier re-pin** (C6 bundle). Explicitly considered
  and NOT taken; it stays closed and still ships only as its own single bundled version
  if ever opened.
- **Reopening Tiers 1–3**; the holdout guard in `walkworthy_inspect/datasets.py`;
  `pushback_rate` (stays CLOSED); ablation promotion. All unchanged.

### Verification gates for everything this ruling produces

`lint_claims.py` 0 blockers on every new artifact · canary count ≥ 2 per artifact ·
full pytest suite green after code edits (count may exceed 103 if tests are added;
every characterization-test change individually documented) · `verify_instrument.py`
ALL PASS against the re-stamped instrument · commit by explicit path, message via
`git commit -F`, verified with `git log -1 --stat`.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
