# `fairgold` — Aggregation-Invariance Rescoring Toolkit

**Date:** 2026-07-09
**Delivers:** RP-02 FAIRGOLD — objective **O2**, tool **T2** ("Implement rescoring engine + rule test suite; pure computation, no keys needed").
**Status:** tool only. No measurements, no results. Runs fully offline.
**Brief (binding):** `INNOVATION/05-research-programs/RP-02-FAIRGOLD.md`.

---

## 1. What the brief required (O2 / T2)

RP-02's method sketch (step 2) and deliverable 2 call for a Python rescoring
engine implementing "the aggregation-rule family with clean interfaces:
plurality, Borda-style scoring, proportional representation of label
distributions, maximal lottery, distributional-distance scoring. **Rules
imported from the cited literature, not invented.**" The engine must run on
*stored predictions* (no live model calls), report **Kendall-τ rank stability
across rules** (H1), and support **consensus-stratified** analysis so
instability can be localized per item stratum (H2). O2 is explicitly the
"good credential-blocked-period task" — pure computation, no keys.

The binding **kill criteria** (K1 invariance null, K2 <3 usable datasets) and
the **invariance study** itself (O3/O4) are downstream of this tool and are
**not** in scope for O2 — they require model predictions / datasets that do
not exist yet. This build produces *only the instrument that O4 would run*.

## 2. What is implemented

Package `fairgold/` (pure computation; deps: `numpy`, `scipy`):

| Module | Contents |
|---|---|
| `data.py` | `Item` (disaggregated per-annotator votes / rankings / group tags), `Benchmark`, `Predictions` (model → item → point-answer **or** distribution). |
| `stats.py` | `total_variation`, `jensen_shannon`, `shannon_entropy` / `normalized_entropy`, `kendall_tau` (tau-b, tie-corrected, via scipy), `maximal_lottery` (LP solver for the mixed equilibrium of a pairwise-majority margin game). |
| `rules.py` | The five-rule family, each producing an `ItemScoring` with per-option `credit ∈ [0,1]` for point answers and a `score_distribution` for models emitting distributions. |
| `engine.py` | `RescoringEngine`: score a model / all models under a rule; rank models; `stability()` → pairwise Kendall-τ across all rule pairs (the proposed **aggregation-sensitivity statistic**); `stratify()` + `stability_by_stratum()` by contestedness (H2). |

### The five rules (literature-anchored, not invented)

1. **`plurality`** — majority-gold, winner-take-all (the status-quo target of the critique). Ties → uniform random tie-break (expected credit 1/k).
2. **`proportional`** — proportional representation: credit = population share of the chosen option.
3. **`borda`** — Borda positional scoring rule (needs per-annotator rankings); credit normalized so the top-Borda option = 1.0.
4. **`maximal_lottery`** — Fishburn (1984) / Kreweras randomized maximal-lottery rule; credit = probability mass the maximal lottery places on the option. Correctly returns the uniform 1/3 mixture on a Condorcet cycle and full mass on a Condorcet winner (see tests).
5. **`distributional`** — distribution-matching: score = `1 − distance(model_dist, population_dist)`, distance ∈ {total-variation (default), Jensen-Shannon}.

### Interface (typical use)

```python
from fairgold import Benchmark, Item, Predictions, RescoringEngine, default_rules

bench = Benchmark("MY-BENCH", [
    Item("q1", options=["A","B","C"], votes=[...]),               # point labels
    Item("q2", options=["A","B","C"], rankings=[["A","B","C"], ...]),  # ranked labels
])
preds = Predictions({"model-x": {"q1": "A", "q2": "B"},           # point predictions
                     "model-y": {"q1": {"A":0.6,"B":0.4}, ...}})  # or distributions

eng = RescoringEngine(bench)
report = eng.stability(preds, default_rules())
report.scores          # model -> rule -> mean score
report.pairwise_tau    # (rule_a, rule_b) -> Kendall tau
report.min_tau         # worst-case rank stability across rules
eng.stability_by_stratum(preds, default_rules(), thresholds=(0.5,))  # H2
```

Per-item mechanics are exposed too: `rule.item_scoring(item).credit`,
`.score_point(answer)`, `.score_distribution(dist)`.

### Tests

`tests/` — 49 pytest cases exercising **every rule** and the engine, with
expected values hand-derived in the fixtures (e.g. the textbook
Borda-≠-plurality profile; rock-paper-scissors cycle → uniform maximal
lottery; Condorcet winner → full mass). Run:

```bash
cd INNOVATION/40-BUILDS/rp02-fairgold
../../../../.venv/bin/python -m pytest -q      # from vault root: ../.venv/bin/python
```

All fixtures in `tests/fixtures.py` are **clearly labelled synthetic
test toys** — not benchmark data, not findings (RP-02 evidence discipline).

## 3. What is deliberately NOT implemented (needs keys/data that don't exist yet)

Per the brief's task split and the standing "no fabricated datasets"
governance rule, the following are **out of scope for O2** and are left for
later cycles when their inputs exist:

- **Disaggregated-label benchmark inventory (O1, deliverable 1).** Requires the 965-benchmark corpus pass + web check. Not built here; O2 is engine-only.
- **Model predictions (O3).** No prediction dumps and no API keys/runner are available. The engine consumes a `Predictions` object; producing a *real* one needs the Cycle-2 shared runner (handoff 2.1). No synthetic predictions are shipped as data — only in-test toys.
- **The invariance study + Kendall-τ results (O4).** No real numbers are computed or reported. Running `stability()` on real benchmarks + real predictions is O4's job, and its verdict is gated by kill criteria K1/K2 (Fable/Jimmy adjudication).
- **CLI / batch report renderer.** Not required by O2; the library API is the deliverable. Easy to add once real inputs exist.
- **Loaders for specific benchmark formats.** `data.py` defines the neutral in-memory schema; format-specific adapters wait on O1 identifying which datasets actually ship disaggregated labels.

## 4. How Cycle-2 work plugs in

- **2.1 shared runner** produces per-model, per-item answers → serialize into a `Predictions` object (point strings or `{option: prob}` dicts). No engine change needed.
- **RP-02 O3** (collect predictions on 2–3 anchor benchmarks): load disaggregated labels into `Item`s (votes and/or rankings), models' answers into `Predictions`.
- **RP-02 O4** (invariance analysis): call `engine.stability(...)` for the τ matrix and `engine.stability_by_stratum(...)` for the H2 stratum test; apply **K1** (τ > 0.95 on all pairs on all benches → publish the null) and **K2** (<3 usable datasets → downgrade to position paper) — these remain Fable-tier/Jimmy rulings, not automated here.
- **Reporting standard (deliverable 4):** the `StabilityReport` (scores × rules + per-stratum breakdown) is exactly the one-table "aggregation-sensitivity analysis" the brief proposes folding into `COOKBOOK/00-KNOWLEDGEBASE/01`.

## 5. Ambiguities / conservative readings (flagged, not silently resolved)

The brief names the rule *family* but leaves several scoring conventions
under-specified. Each was resolved to the conservative/standard reading and
is documented in-code:

- **A1 — plurality ties.** Chose expected credit `1/k` under uniform random tie-break (a lottery interpretation, consistent with the randomized-rule spirit). Alternative "full credit 1.0 to any tied winner" is a one-line change.
- **A2 — "Borda-style scoring" = partial credit vs. winner-take-all.** Implemented as *normalized Borda credit* (top option = 1.0, others proportional to Borda points) so it parallels the other scoring rules; `BordaRule.borda_winner()` exposes the winner-take-all variant.
- **A3 — maximal lottery from votes only.** With single-choice votes (no rankings) the induced tournament is fully ordered by vote counts, so the maximal lottery collapses onto the plurality winner. This is mathematically correct, not a bug; non-degenerate ML behaviour requires per-annotator **rankings**. Flagged so O3 knows ranked disaggregation is what makes ML informative.
- **A4 — distributional (TV) reduces to proportional for point answers.** For a delta answer, `1 − TV(δ, pop) = pop[o]`, identical to proportional credit. The distributional rule therefore only diverges from `proportional` for models that emit genuine distributions; the JSD variant differs even for point answers. Documented so the two rules aren't mistaken for redundant.
- **A5 — missing predictions.** Default is strict (raise if a model lacks a prediction for a scored item); `skip_missing=True` scores only answered items but changes the denominator across models. Default chosen to avoid silently unfair cross-model comparisons.
- **A6 — contestedness metric.** Used normalized Shannon entropy of the vote distribution (consensus = 1 − entropy) for the CRUX-style tiering the brief references generically; thresholds are caller-supplied. Other contestedness proxies (plurality margin, variance) are equally defensible; entropy chosen as the standard, parameter-free option.

### Deviations from the brief

None substantive. The brief is followed as written: five named rules, stored-prediction input, Kendall-τ stability, stratified analysis, no live calls. The only expansion is the JSD distance option alongside TV (both are standard distribution distances; TV is the default and matches the brief's "distributional-distance" language).
