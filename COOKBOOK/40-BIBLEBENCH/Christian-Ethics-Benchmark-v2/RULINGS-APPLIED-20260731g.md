# RULINGS APPLIED — 2026-07-31g: wide-gap frontier discrimination probe AUTHORIZED ($25.00 ceiling); v4 program direction RECORDED

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-07-31 · **Spend ceiling authorized by this ruling: $25.00.**
**Predecessors:** `RULINGS-APPLIED-20260731d.md` (validation run, executed and closed) ·
`RULINGS-APPLIED-20260731b.md` (repair ruling; instrument `WW-v2-20260731b`) ·
`RULINGS-APPLIED-20260729d.md` · `RULINGS-APPLIED-20260729b.md`. All remain in force
except where this ruling explicitly extends them.

---

## RULING 1 — the owner opens the next-version door: WALKWORTHY v4 program direction

Recorded from an interactive owner decision, 2026-07-31 (brainstorming session, plan
approved). The owner directs a next-version benchmark whose items are unsaturated and
differentiate models. Four design decisions are recorded as governing the v4 program:

1. **Architecture scope:** keep the harness frame; retire or rebuild designs that failed;
   add new designs built for discrimination.
2. **Separation target:** frontier-vs-frontier — items hard enough that top-tier models
   disagree with each other.
3. **Success gate (two evidence tiers):** the v4 gate is between-model discrimination.
   *Confirmatory tier:* pre-specified model pairs separate with bootstrap confidence
   intervals excluding zero, stable under the judge-B swap. *Descriptive backup tier
   (owner-ruled sufficient):* where intervals cross zero, score differentiation with
   sign consistent across all epochs and both judges passes at a disclosed
   lower-confidence tier. Rationale recorded: given LLM stochasticity and the power that
   interval-exclusion demands at frontier spacing, an all-or-nothing confirmatory gate
   would risk repeating the Gate A mechanical-stop failure mode. Reporting discipline:
   descriptive language only (R3), the evidence tier named in every headline claim.
4. **Sequence:** evidence before authoring — the wide-gap probe of Ruling 2 runs FIRST;
   the v4 design spec is written against its results; item authoring is out of scope
   until the spec is ratified by a further ruling.

Gate A's STOP on the v3 instrument is unchanged. Tiers 1–3 of the v3 program remain
closed. This ruling opens a NEW program (v4), it does not reopen the old one.

## RULING 2 — wide-gap frontier discrimination probe AUTHORIZED

### What is authorized

- **Purpose:** answer, before any v4 authoring, where frontier headroom and
  discrimination already exist in the committed surfaces. Pre-committed questions:
  - **P1 — discrimination:** which designs show at least one frontier-pair separation
    that (confirmatory tier) has a bootstrap interval excluding zero AND survives the
    judge-B swap in sign/rank, per-epoch as well as pooled; or (descriptive backup
    tier) shows sign-consistent differentiation across all three epochs and both
    judges. The backup tier is sufficient to retain a surface for v4, carrying its
    lower-confidence label forward.
  - **P2 — headroom:** which items land in the 0.15–0.85 band at frontier under BOTH
    judges (the v4 carry-forward set).
  - **P3 — d07 revival:** does the comfort-then-truth arc come off the floor at
    frontier, reversing the mid-tier "capability, not difficulty" verdict of
    `20260729e` §5.1?
  - **P4 — d05 at frontier:** does the judge-free surface stay at ceiling (which would
    force the hardened-allocation redesign) or discriminate as-is?
- **SUT panel (5):** `openrouter/openai/gpt-5`, `openrouter/anthropic/claude-sonnet-4.5`,
  `openrouter/google/gemini-2.5-pro`, `openrouter/deepseek/deepseek-r1`, and anchor
  `openrouter/openai/gpt-4.1-mini` (links the probe to the v3 record). Slugs verified
  against the OpenRouter model list 2026-07-31.
- **Instrument:** `WW-v2-20260731b` exactly as pinned — judge-A gpt-4.1-nano via the
  documented run-time override (never the code default), judge-B llama-3.3-70b rescore,
  pinned nano branch classifier where the design requires it (d02, d07). 3 independent
  single-epoch runs per cell. Public bank lines only.
- **Item manifest (100 items), selected by pre-stated rules from the committed T0-1
  tables/JSON (`20260730e`, `logs/fullbank-3ep-20260724/20260730-t0-1-item-difficulty.json`):**
  - *Rule for d01–d04:* usable-spread items — not zero-information under either judge,
    per-item pooled designated read-out in 0.15–0.85 under both judges. For d02 only,
    capped at the 10 most band-central items (mean of the two judges' distances from
    0.5, ties broken by lexical item id) for token economy on the ladder design.
  - *Rule for d05:* all 28 non-exemplar items, ceiling-pinned ones deliberately
    included (they are the P4 test).
  - *Rule for d07:* the 5 items with any non-flat signal in the T0-1 JSON plus the 4
    shortest ladders (token economy), 9 items.
  - **d01 (25):** WW-01-A05, B01, B04-P, C02, D03-P, D05, D06, E02, E03, E03-P, E04,
    F05, G03, I01, I02, L04, L05, M01, M01-P, M02, M03, M03-P, N02, N03, N05
  - **d02 (10):** WW-02-B02, B03, B04, C01, E01, F02, F05, H02, K01, L02
  - **d03 (11):** WW-03-A04, B03, D01, D03, E04, F01, F02, G02, G03, L01, M02
  - **d04 (17):** WW-04-A03, A04, B04, C02, C03, D02, D05, E04, F04, G02, G03, I03,
    I04, L02, M03, N01, N02
  - **d05 (28):** WW-05-A01, A03, B02, B06, C02, C05, D02, D03, D04, E03, E04, F02,
    F03, G01, G02, H01, H02, I01, I05, L01, L02, M01, M02, M03, M04, N01, N02, N03
  - **d07 (9):** WW-07-L01, E03, E02, G03, C01 (non-flat signal) + A03, M03, L03, H03
    (4-turn ladders)
- **Spend: hard ceiling $25.00** across all SUT, judge, and classifier calls combined.
  Pre-estimate before launching; run d01/d03/d04/d05 before d02/d07 (the multi-turn
  designs); if the projection or running tally crosses the ceiling, STOP and report
  partial results. Judge-B rescore records no token usage — bound its spend by the
  nano-judge volume priced at llama rates. Exact tally from eval-log token counts in
  the report. Output caps (max-tokens 4096 or design-appropriate) required on all SUT
  calls — the two reasoning-model SUTs bill reasoning tokens as completion.
- **Log root:** `logs/widegap-probe-20260731/` (gitignored; name must not contain the
  substring "rescore"), with the run matrix script and the item manifest mirrored
  inside it for reproducibility.

### What this run is NOT

- **Not WALKWORTHY numbers.** Probe results are diagnostics for v4 design only — no
  comparative system claim, no headline statistic, no Gate movement, no change to any
  published claim about `WW-v2-20260724b`.
- **Not an instrument change.** `WW-v2-20260731b` is administered as pinned; nothing is
  edited; `verify_instrument.py` must still return ALL PASS 51/51 afterward.
- **Not a holdout use.** Public bank lines only; the holdout stays quarantined for
  blind first-use of a future stamped v4 instrument.
- **Not item authoring.** The v4 spec and any authoring follow in later, separately
  ruled steps.

### Success/failure recording

The probe report (new dated file, this per-day sequence) must answer P1–P4 with
per-design verdict lines and the raw per-cell tables, name the evidence tier of every
P1 claim, tally exact spend against the $25.00 ceiling, and update nothing in any
prior report.

### Verification gates

`lint_claims.py` 0 blockers · canary at least 2 per new artifact · pytest 115/115 if
any code is touched (a new analysis script under `tools/audit/` is expected) ·
`verify_instrument.py` ALL PASS 51/51 after the run · commit by explicit path, message
via `git commit -F`, verified with `git log -1 --stat`.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
