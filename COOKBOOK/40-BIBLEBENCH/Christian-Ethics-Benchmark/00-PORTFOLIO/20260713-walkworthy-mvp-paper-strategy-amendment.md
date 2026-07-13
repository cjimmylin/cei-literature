# WALKWORTHY — MVP Paper Strategy Amendment

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Owner:** Jimmy Lin
**Status:** RATIFIED STRATEGY; execution and spending remain separately gated
**Scope:** WALKWORTHY only
**Purpose:** reach a complete, reviewable MVP paper quickly and cheaply before scaling
to a larger model panel, stronger judges, or release-grade validation.

## 1. Owner direction

Jimmy directed WALKWORTHY to prioritize the fastest low-spend path to seeing what the
paper will look like. The approved design is a separate small-panel MVP pilot using
three inexpensive SUTs and two inexpensive judges under a hard **$5.00 not-to-exceed
cap**.

This amendment implements the BibleBench paper-first default for WALKWORTHY. It does
not alter the frozen O5 gate rules, reinterpret existing results, authorize a paid
call, or lower the evidence standard for release-grade claims.

## 2. Two-lane strategy

### Lane A — MVP-PILOT (paper preview; immediate priority)

The MVP-PILOT exists to populate the manuscript's full visible shape: methods,
descriptive results tables, figures, limitations, and a provisional narrative. Its
results are explicitly exploratory and may not support release verdicts.

### Lane B — O5 (release-grade validation; preserved)

The existing O5 lane remains the sole source for frozen-gate verdicts, judge-validity
claims, item kills or demotions, release status, and leaderboard/public benchmark
claims. The MVP-PILOT never replaces, merges into, or silently modifies O5 evidence.

## 3. Registered MVP-PILOT contract

### Model panel

- **3 inexpensive SUTs**, from three distinct provider families where feasible.
- **2 inexpensive cross-family judges**. They need not be frontier or release-grade;
  their unvalidated status must be disclosed adjacent to every result.
- Every model uses an explicit, versioned slug. No harness default may select a model.
- Exact slugs are chosen from currently available low-price models and require a
  separate written run authorization before credentials or paid calls are used.
- One minimal reliability probe per model precedes the batch. A failed probe stops
  that model's thread; there is no unapproved substitution.

### Item surface

Use the PUBLIC split only. For each of the ten designs, select deterministically by
item ID:

- the first **2 runnable easy** items; and
- the first **4 runnable hard** items.

This yields **60 items** and **180 item×SUT cells** before design-specific multi-turn or
paired administrations. The manifest records the exact 60 item IDs before any call.
No private split is loaded, and this selector is independent of the frozen G7
perturbation selector.

### Spending boundary

- Hard cap: **$5.00 total**, including SUT, classifier, and judge calls.
- The run order must expose a checkpoint before projected spend exceeds $3.00.
- If actual plus projected remaining cost can exceed $5.00, stop and ask Jimmy.
- No balance check, credential access, network call, or paid execution is authorized
  by this strategy amendment alone.

### Evidence and custody

- Persist complete prompts/responses, explicit model slugs, usage/cost, rubric output,
  and errors in a new immutable run directory.
- Preserve deterministic manifests and resumable checkpoints.
- Never overwrite historical O4/O5 runs or dated reports.
- Report exclusions and defects; never fill missing cells by inference.
- Minimum completeness for an MVP descriptive row is **at least 90% of the registered
  item×SUT cells for that design and SUT**. Below that threshold, render the row as
  incomplete rather than interpreting it.

## 4. MVP claim license

The MVP-PILOT may support only:

1. a demonstration that the WALKWORTHY methods and reporting pipeline execute across
   all ten designs on a small heterogeneous panel;
2. descriptive, explicitly provisional model-by-design statistics;
3. a complete preview of planned tables, figures, profiles, and limitations; and
4. observations that motivate which release-grade validation would be most valuable.

It may **not** support:

- a model ranking or leaderboard claim;
- a gate PASS/FAIL, release, redesign, kill, or demotion verdict;
- a claim that the inexpensive judges are valid substitutes for human labels or the
  registered O5 judge-validation process;
- a population-level or frontier-model generalization; or
- combining MVP and O5 cells as if they came from one registered panel.

Every MVP results surface must state: **small exploratory panel; inexpensive,
unvalidated judges; descriptive only; not release-grade evidence.**

## 5. Paper-first stopping rule

The MVP session is complete when all of the following exist:

1. a reproducible 60-item × 3-SUT run snapshot within the $5 cap;
2. a dated descriptive MVP analysis artifact;
3. every manuscript results-table and figure shape populated or explicitly marked
   unavailable;
4. limitations describing small-panel power, judge validity, subset sampling, and
   non-release status; and
5. a concise scaling memo listing only additional evidence that could materially
   change a named paper claim, table, or figure.

Once these exist, stop. Do not automatically add models, stronger judges, more items,
human labels, or durability engineering.

## 6. Scaling gate

Scaling requires Jimmy to review the MVP paper preview and separately authorize a
specific next increment. The authorization must identify:

- the paper claim or table that needs stronger evidence;
- the additional model, judge, item, or human-label surface;
- the spend cap; and
- the stop condition.

Preferred scaling order is incremental: first add only the cheapest evidence capable
of changing the targeted paper conclusion; use larger or more expensive panels only
when cheaper evidence is scientifically insufficient.

## 7. Deferred work

Until the MVP paper preview is reviewed, the following are nonblocking unless they
resolve an active evidentiary-integrity defect on the MVP surface:

- frontier or expensive judge substitution;
- expansion beyond three SUTs;
- full-bank reruns;
- release engineering and leaderboard work;
- generalized transport hardening;
- extra concurrency experiments; and
- P2/P3 robustness or polish that cannot change an MVP paper claim.

## 8. Next authorized documentation step

Prepare a separate execution order that names the exact cheap model slugs, verifies
current prices and availability, calculates the worst-case call budget, and requests
Jimmy's explicit paid-run authorization. Until that order is ratified, manuscript work
may use existing eligible evidence and this amendment's planned MVP table structure,
but no new live call is authorized.
