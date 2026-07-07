# RP-04 HIDDENCURRICULUM — What Values Do Reward Models and Judges Actually Teach?

**Gaps:** G-04 (RM values science), G-05 (preference-data provenance), G-09 (judge corruption)
**Portfolio claim:** measurement science · **Wave:** 1 (dogfood phase) → 2 (full)
**Author:** Fable 5 · 2026-07-07

## Motivation

Reward models are the narrow gate through which all RLHF-era values pass, and 2025–26 established they are value-laden in ways nobody chose: RMs inherit "sticky" value biases from *pretraining* that identical preference data cannot scrub (Llama-family RMs prefer agency, Gemma-family prefer communion — Christian et al. 2026); RMs cannot represent full value profiles (EVALUESTEER: <75% on value+style profiles); models can learn to exploit RM error patterns as an objective (Anthropic auditing-hidden-objectives). The auditing so far uses ad hoc probes. CEI has what the literature lacks: multi-dimensional, adversarially-gated, tradition-aware item banks — plus a selfish reason to start immediately: **every CEI benchmark scores with LLM judges, and the judge-corruption literature is a standing validity threat to CEI's own results.**

## Core hypothesis

**H1:** RMs and LLM judges have measurable, stable value profiles at item-bank granularity (test-retest and paraphrase reliability sufficient for profiling).
**H2:** Profiles cluster by base-model family more than by preference-data recipe (the pretraining-inheritance signature, replicated on richer instruments).
**H3 (dogfood):** CEI's own scoring judges carry quantifiable value biases that materially interact with bank content (e.g., a judge family systematically over-rewards one framework's rhetoric), and judge-family triangulation bounds the error.

## Method sketch

**Phase 1 — dogfood (no new infra, start now):** re-score a frozen sample of existing CEI bank responses (FRUITBENCH THORNS pilot outputs, DIMGLASS bank exemplars, SERMONMOUNT WITNESS harness outputs — all on disk) with 3+ judge families; quantify inter-judge disagreement structure by item type, framework, and tradition; publish an internal judge-bias memo that every BibleBench family cites. This doubles as the third-judge-family requirement already imposed on SERMONMOUNT (D1).
**Phase 2 — open-weight RM audit:** administer CEI banks as *preference pairs* (the banks' case/exemplar structure converts naturally: aligned vs. misaligned response per scenario) to open RMs across families (Llama-, Gemma-, Qwen-derived; Tulu/OLMo document their full pipelines). Extract profiles: which traits/frameworks/traditions get rewarded. Test H2 with family-vs-recipe variance decomposition.
**Phase 3 — downstream link (stretch):** for open pipelines with documented RMs and released post-RLHF checkpoints, test whether RM profile predicts the trained model's bank scores — the values-transmission correlation the field hasn't measured.

## Novelty vs. published work

Existing RM audits probe single dimensions with synthetic pairs; nobody has profiled RMs on validated multi-trait, multi-tradition instruments, and nobody has connected RM profiles to downstream model values on the same instrument (Phase 3 would be first). The dogfood phase is also, quietly, the first systematic judge-bias audit of a large values-benchmark portfolio — publishable as measurement methodology.

## Deliverables

1. Judge-bias memo for CEI pipelines (internal, then methods-paper section).
2. RM value-profile dataset (public release: profiles × RM families × instruments).
3. H2 paper: "Reward models have value profiles; pretraining chooses them" (replication + extension of the inheritance result on richer instruments).
4. Phase-3 note (even a null on values-transmission is informative).

## Opus build tasks

- O1 (now, key-light): assemble frozen response corpus from existing pilot outputs; design re-scoring matrix; run with available keys.
- O2: pair-conversion tooling — banks → preference pairs with polarity metadata (mechanical; Sonnet).
- O3: open-RM inference lane (hosted endpoints suffice; no training) — needs modest budget sign-off.
- O4: variance-decomposition analysis per H2 (pixi/R stack: lme4 is already in the lockfile).
- O5: Fable-tier review of the judge-bias memo before it becomes binding on other CEI programs.

## Kill criteria

- **K1:** If profiles fail paraphrase reliability (r < 0.5), RMs don't have measurable value profiles at this granularity — publish the reliability finding, stop Phases 2–3.
- **K2:** If dogfood finds judge biases large enough to threaten published CEI verdicts, that's not a kill — it's a mandatory errata/robustness pass on affected benches (pre-commit to this; do not soften).
- **K3:** Phase 3 kills itself if fewer than 3 documented RM→model open pipelines exist; fold the question into a future collaboration pitch instead.
