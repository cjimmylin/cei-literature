# RP-08 CONCLAVE — Tradition-Aware Deliberative Alignment

**Gaps:** G-11 (deliberation→artifact pipelines), G-12 (legitimacy/procedural justice)
**Portfolio claim:** tradition-aware pluralism (CEI's unique differentiator) · **Wave:** 3 (human-gated for the strong version)
**Author:** Fable 5 · 2026-07-07

## Motivation

Deliberation now reaches production value documents: OpenAI's Collective Alignment pipeline feeds public input into the Model Spec; Democratic ICAI distills steering principles from preference data; consensus generation has social-choice guarantees. But every existing pipeline is **tradition-blind**: it samples individuals demographically and aggregates opinions, treating pluralism as *opinion spread*. Deep normative difference — a Confucian and a Rawlsian don't just weight answers differently, they disagree about what counts as a reason — is exactly what these pipelines flatten, and exactly what the critical literature (democratic-ontology deficit, WEIRD-skew critiques, Habermas-machine consensus-telos critique) says is being lost. CEI is the only group with 14 traditions *operationalized* (classified corpora, item banks, denominational resolution in INTRA) rather than merely surveyed. That asset converts directly into the missing pipeline.

## Core hypothesis

**H1 (information loss):** Opinion-pooling pipelines produce constitution clauses that fail tradition-fidelity checks — each tradition's non-negotiables are detectably violated or erased — at rates that tradition-structured deliberation substantially reduces, without materially worsening majority-satisfaction.
**H2 (procedure matters):** *How* traditions interact in the pipeline (parallel elicitation → bridging synthesis, vs. sequential deliberation, vs. adversarial exchange) changes clause content measurably — i.e., the deliberation protocol is a real design variable, not plumbing.

## Method sketch

1. **Tradition agents (Phase A — synthetic, clearly labeled as such).** Instantiate tradition representatives from CEI's corpora (grounding: retrieval over the tradition's operationalized texts, not just a persona prompt). **Fidelity gate first:** each tradition-agent must pass validation against corpus-derived held-out items (does it answer as the tradition's own literature answers?) before any deliberation runs. This gate is the program's foundation — without it the whole exercise is ventriloquism.
2. **Pipelines under test.** (a) Flat opinion-pooling baseline (CCAI-style); (b) parallel tradition-elicitation + bridging synthesis (Community-Notes-style bridging adapted to traditions); (c) structured deliberation (Habermas-machine-style mediation among tradition agents); (d) Democratic-ICAI-style principle distillation from tradition-stratified preference data.
3. **Outcome measures.** Tradition-fidelity score per tradition (violations of pre-registered non-negotiables, drawn from the corpora); majority-satisfaction; clause coverage vs. SPECGRADE's value-situation taxonomy (cross-program synergy); minority-preservation vs. erasure analysis.
4. **Phase B — human graduation (Jimmy-gated).** Replace synthetic agents with small human panels per tradition for the 2–3 highest-stakes comparisons. Phase A results select *which* comparisons deserve the expensive human pass. All Phase-A claims carry explicit synthetic-data caveats until then.

## Novelty vs. published work

No published pipeline structures deliberation by ethical tradition; no fidelity-gated tradition-agent methodology exists; the moral-graph line elicits individual values, not tradition structures. The result speaks simultaneously to the alignment-engineering audience (better constitution pipelines) and the legitimacy literature (a concrete answer to the WEIRD-flattening critique) — a two-community paper.

## Deliverables

1. Tradition-agent fidelity-gate methodology + validation report (standalone methods contribution, publishable even if downstream results disappoint).
2. CONCLAVE pipeline implementations (a–d) + tradition-fidelity metric suite.
3. Comparison study (H1/H2) with synthetic caveats; Phase-B human replication design as a pre-registered protocol.
4. Position paper: "Tradition-aware collective alignment" (target: FAccT/AIES — the venue where both audiences sit).

## Opus build tasks

- O1: Fidelity-gate construction — held-out item sets per tradition from existing corpora (INTRA design's denominational machinery is the template; start with 4–6 best-operationalized traditions, not all 14).
- O2: Retrieval-grounded tradition-agent harness (RAG over tradition corpora; NOT persona prompts alone).
- O3: Pipeline implementations (b)–(d), reusing published methods (bridging MF, mediation prompts, ICAI distillation) — read-first tasks from the acquisition list.
- O4: Non-negotiables registries per tradition (Fable-tier review mandatory — these are load-bearing normative judgments and the program's most contestable artifact).
- O5: Run comparison + analysis; position-paper draft for Fable-tier review.

## Kill criteria

- **K1 (the hard gate):** If tradition-agents fail fidelity validation (below pre-registered accuracy on held-out tradition items) for more than 2 of the starting traditions after one retrieval-architecture revision, Phase A is invalid — halt everything downstream, publish the fidelity-gate methodology and the negative, and wait for human panels.
- **K2:** If H1 shows no fidelity difference between pooling and tradition-structured pipelines, the differentiator thesis fails — publish honestly; the fidelity metrics and non-negotiables registries survive as reusable artifacts.
- **K3:** Never let Phase-A (synthetic) results be cited — by us or others — without the caveat attached; if that discipline can't be maintained in practice, restrict outputs to methods-only until Phase B.
