# RP-02 FAIRGOLD — Aggregation-Invariance for Values Benchmarks

**Gaps:** G-10 (social choice for alignment)
**Portfolio claims:** measurement science; no-gold substrate · **Wave:** 3
**Author:** Fable 5 · 2026-07-07

## Motivation

The social-choice-for-alignment literature (Harvard/MIT/CMU line, culminating in the June-2026 SIGecom survey) established that vanilla RLHF is a disguised majoritarian aggregator with formal pathologies: Condorcet cycles, minority erasure, clone-sensitivity, quantifiable distortion from the welfare optimum. That entire critique targets *training*. But values **benchmarks** commit the identical sin at the evaluation layer: "majority-gold" labels aggregate annotator judgments by plurality, then leaderboards rank models against the flattened label. The COOKBOOK already identifies majority-gold as a design smell (KB-12's population-scoring ceiling); what's missing is the demonstration that this is not just philosophically awkward but *changes scientific conclusions* — and a replacement practice with axiomatic footing.

## Core hypothesis

**H1:** Values-benchmark verdicts are not aggregation-invariant: rescoring existing benchmarks under different defensible aggregation rules (majority, population-proportional, maximal-lottery/randomized, calibrated-distribution matching) produces materially different model rankings.
**H2:** Rank instability concentrates in identifiable item strata (contested items, demographically split items), so aggregation-sensitivity can be *reported per benchmark* as a validity statistic rather than discovered per study.

## Method sketch

1. **Corpus of disaggregated-label datasets.** Inventory values benchmarks that ship per-annotator or per-group labels (the pluralism literature produced several; CEI's 965-benchmark characterization corpus identifies candidates). This inventory is itself a deliverable — most benchmarks *discard* disaggregated labels, which is finding #0.
2. **Rescoring engine.** Implement the aggregation-rule family with clean interfaces: plurality, Borda-style scoring, proportional representation of label distributions, maximal lottery, distributional-distance scoring (model's answer distribution vs. population distribution). Rules imported from the cited literature, not invented.
3. **Invariance study.** Score 8–12 frontier models on each benchmark under each rule; report Kendall-τ rank stability across rules; identify the items driving instability; test H2's stratum prediction (consensus-stratified via CRUX-style tiering).
4. **Reporting standard.** Draft "aggregation-sensitivity analysis" as a proposed standard benchmark statistic (one table: verdict stability across rules + the stratum where it breaks), aligned with the COOKBOOK's pre-registration checklist so all future CEI benches carry it natively.

## Novelty vs. published work

Distortion, proportionality, and calibration are published for *reward learning*; nobody has applied aggregation-sensitivity analysis to *evaluation gold labels* or shown leaderboard consequences. The bridge is short (which is why it's winnable) but it lands in benchmark-methods territory CEI already owns, and it retro-validates (or indicts) the majority-gold verdicts in the existing meta-evaluation corpus.

## Deliverables

1. Disaggregated-label benchmark inventory (with a note on how many benchmarks destroy this information).
2. `fairgold` rescoring toolkit (Python, runs on stored predictions — no live model calls needed for the core study if prediction dumps exist).
3. Invariance study + paper (target: NeurIPS D&B / EMNLP).
4. Proposed reporting standard, folded into `COOKBOOK/00-KNOWLEDGEBASE/01` as an amendment candidate.

## Opus build tasks

- O1: Inventory pass over the 965-benchmark corpus + web check for disaggregated releases (Sonnet sweep, Opus verify).
- O2: Implement rescoring engine + rule test suite (pure computation; no keys needed — good credential-blocked-period task).
- O3: Collect/produce model predictions on 2–3 anchor benchmarks (needs runner/keys where dumps don't exist).
- O4: Run invariance analysis; draft paper skeleton for Fable-tier review.

## Kill criteria

- **K1:** If rankings are invariant (τ > 0.95 across all rule pairs on all tested benchmarks), the critique has no empirical bite at the evaluation layer — publish the null (it's a *reassuring* result the field would cite) and close the program.
- **K2:** If fewer than 3 usable disaggregated-label benchmarks exist and none can be reconstructed, downgrade to a position paper + the reporting standard, and add "release disaggregated labels" to CEI's own bench-release checklist.
