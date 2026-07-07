# RP-03 NOGOLD — Oversight Protocols on Contested Normative Ground

**Gaps:** G-07 (no-ground-truth oversight), G-08 (weak-to-strong for values), G-09 (judge corruption)
**Portfolio claim:** the no-gold normative substrate · **Wave:** 2 (flagship)
**Author:** Fable 5 · 2026-07-07

## Motivation

Scalable oversight reframed itself in 2025–26 as mechanism design for the no-ground-truth regime: peer prediction (honesty via mutual predictability, robust at >100× capability gaps), recursive self-critiquing ("critique-of-critique is easier"), nested-oversight scaling laws, debate-for-reward-training. But essentially every empirical validation rides on tasks with *hidden* gold (QA, code, math) — the protocols are advertised for value questions and tested on trivia. Meanwhile the judge-corruption literature (confirmation bias that debate doesn't fix; debaters more persuasive arguing their priors; LLM judges collapsing at 5–20× capability gaps) suggests the normative case may fail badly. Nobody has run the experiment. CEI owns the missing piece: CRUX (`COOKBOOK/ENGINE/`, built) generates value-conflict items with **consensus stratification** — a gold tier (near-universal agreement), a contested tier (reasonable pluralism), and a no-gold tier — which is precisely the graded substrate an oversight experiment needs.

## Core hypothesis

**H1 (degradation):** Oversight protocols that beat direct-judging on gold-tier items degrade differentially as items move to contested/no-gold tiers — and the degradation ranking across protocols is stable.
**H2 (reliability without truth):** On contested items, protocol quality is still measurable *without* accuracy, via pre-registerable invariance properties: a valid protocol's verdicts should be (a) debater-assignment-invariant (swap which model argues which side → verdict stable), (b) judge-prior-independent (verdict uncorrelated with the judge's own elicited prior), (c) order/format-invariant. Corrupt protocols fail these even where no one knows the right answer.
**H3 (the fear):** On no-gold items, debate-style protocols add nothing over asking the judge directly — verdicts are prior-echo.

## Method sketch

1. **Substrate.** 300–600 CRUX items, stratified by consensus tier, balanced across value-conflict types (the engine's factorial dimensions). Freeze and version.
2. **Protocols.** Direct judging (baseline); two-sided debate; consultancy (one-sided, the standard control); recursive critique (judge sees critique-of-answer, then critique-of-critique); peer prediction (adapted: multiple answerers scored on mutual predictability — the hardest adaptation, may slip to phase 2).
3. **Capability gaps.** Judge/debater pairs spanning tiers: Haiku judging Opus, Sonnet judging Opus, Opus judging Opus, plus one cross-vendor pairing (anti-leakage discipline per `dispatching-parallel-agents` norms).
4. **Metrics.** Gold tier: accuracy vs. direct baseline. Contested tier: swap-invariance rate, judge-prior correlation (elicit each judge's own answer separately, before exposure), format sensitivity. All tiers: verdict-flip rate under debater swap as the headline statistic.
5. **Pre-registration.** H1–H3 with effect sizes and analysis code frozen before the main run (COOKBOOK pre-reg discipline; deviations logged).

## Novelty vs. published work

The DeepMind W2S-judging line and the debate literature use QA with hidden gold; FindTheFlaws supplies flawed *reasoning* traces, not contested *values*. No published study runs any oversight protocol across a consensus gradient, and none uses assignment-invariance as the validity criterion where accuracy is undefined. That criterion is this program's methodological contribution — it gives the field a way to say "this protocol is trustworthy on questions nobody can grade," which is the actual superalignment use case.

## Deliverables

1. Frozen stratified item set (public release candidate — the field lacks this substrate).
2. Protocol harness (extends the FRUITBENCH-v2 spine; respects the live-mode hard-block until spine fixes S-1/S-2 land).
3. The NOGOLD study + paper (target: ICLR/NeurIPS main track — this is a headline-capable result in either direction).
4. NOGOLD metric suite (swap-invariance, prior-independence) as a reusable validity standard.

## Opus build tasks

- O1: Generate + tier the CRUX item set; adversarial spot-check per COOKBOOK gate protocol.
- O2: Build protocol harness (debate transcripts, critique chains, judge isolation — careful prompt hygiene so judges never see tier labels).
- O3: Prior-elicitation module (judge's own answers, collected in a separate session to avoid contamination).
- O4: Dry-run on 30 items, Fable-tier review of transcripts *before* the main run (judge-corruption failure modes are subtle; this review is where Fable earns its keep).
- O5: Main run + pre-registered analysis. **Blocked on keys.**

## Kill criteria

- **K1:** If gold-tier accuracy shows no protocol beating direct judging (replication failure of the base literature on our substrate), the substrate or harness is suspect — debug before interpreting contested-tier data; do not proceed to H2/H3 claims.
- **K2:** If swap-invariance and prior-independence turn out statistically inseparable from noise at n=600 (power failure), report the design lesson and required n; pause rather than expand silently.
- **K3:** H3 confirming (protocols = prior-echo on no-gold) is NOT a kill — it is the paper. Kill only if results are unstable across reruns (test-retest of the headline statistic r < 0.5), which would mean the phenomenon itself isn't measurable this way.
