# Front D — Aggregation

**Snapshot:** 2026-07-07 · **Author:** Fable 5 · Gaps: G-10, G-11, G-12 · Programs: RP-02 FAIRGOLD, RP-08 CONCLAVE

## Causal story

"Whose values?" spent years as a rhetorical question. Two arms made it operational. The **theory arm**: social choice theorists noticed RLHF is an aggregation mechanism and proved it a bad one — Bradley-Terry preference fitting behaves like a Borda count, majoritarian and cycle-prone as annotator pools diversify. The response literature builds aggregators with axiomatic guarantees: population-proportional alignment, pairwise-calibrated reward *distributions* (keep disagreement, don't average it away), Nash-learning-as-maximal-lottery, distortion bounds, clone-robustness (astroturf resistance). The **practice arm**: participatory pipelines matured from CCAI's proof-of-concept into standing infrastructure — OpenAI's Collective Alignment team now runs public input into actual Model Spec revisions; DeepMind's Habermas Machine spawned a mediation-theory cluster; Democratic ICAI distills deliberation into steering principles. A **critical arm** matured in parallel: legitimacy analyses (what would make any of this *authorized* rather than merely consultative), the "democratic ontology deficit," WEIRD-skew and Global-South critiques, and the observation that consensus-optimization isn't even faithful to Habermas. The arms barely cite each other.

## Key results

- **The survey that names the field:** "AI Alignment From Social Choice Perspectives" (Halpern, Micha, Procaccia et al.; ⚠ 2606.21550, SIGecom Exchanges, June 2026), descending from the ICML-2024 position paper (2404.10271, Conitzer/Procaccia/Russell et al.).
- **Axiomatic aggregators:** population-proportional (MIT/Ozdaglar; 2506.05619); pairwise-calibrated reward distributions — annotator-fraction-matching without annotator IDs (2506.06298); multiplayer Nash preference optimization as maximal lottery (2509.23102); distortion of preference optimization (2505.23749); clone-robust reward learning (2501.09254); ranked-choice feedback beyond pairwise (2510.23631).
- **Pipelines:** OpenAI Collective Alignment → Model Spec (Aug 2025 onward — the live deliberation→artifact loop); Democratic ICAI (⚠ 2606.28294); fair consensus statements on token-level MDPs with social-choice guarantees (Blair & Larson; 2510.14106); Habermas-trilemma follow-up (⚠ 2601.05904); moral graph elicitation (MAI; 2404.10636, tooling active through 2025).
- **Bridging:** quality-sensitive matrix factorization for Community Notes (⚠ 2604.11224) — the deployed, manipulation-resistant cross-factional aggregator.
- **Distributional pluralism:** Spectrum Tuning (2510.06084), survey-distribution alignment (2510.21977) — match populations, not medians.
- **Critique:** democratic-ontology deficit (⚠ 2604.03865); six problematic assumptions of Democratic Inputs (2407.11613); Habermas-machine consensus-telos critique (Ethics & IT 2025); hybrid expert+stakeholder justification analysis (2507.19548).

## Actors

Harvard/CMU/MIT theory cluster; OpenAI Collective Alignment; DeepMind mediation line; Meaning Alignment Institute; Collective Intelligence Project; governance/legal scholars. **Nobody handles tradition-level (vs. demographic) pluralism** — the pipelines sample individuals, not normative structures.

## 12-month trajectory

Theory-practice contact increases (aggregation axioms applied to real participatory data); a second lab stands up a collective-input pipeline; Pluralistic Alignment workshops institutionalize (ICML 2026 signal); legitimacy critiques force pipelines to publish representation audits; distributional-pluralism evaluation seeps into benchmark practice — which is where CEI gets pulled in whether or not it moves.

## CEI entry points (ranked)

1. **Aggregation-sensitivity for evaluation** (RP-02): the theory arm indicts training aggregation; the *same indictment applies to majority-gold benchmark labels* and nobody has run it. Short bridge, CEI-owned territory, publishable fast.
2. **Tradition-aware pipeline** (RP-08): CEI's unique asset — 14 traditions operationalized — against the field's demographically-representative-but-tradition-blind default. The fidelity-gate methodology is a standalone contribution even before results.
3. **Non-negotiables vs. preferences distinction**: CEI's normative depth can formalize what opinion-sampling flattens — feeds both RPs and the position paper (P3).
4. **Import, don't prove**: use published aggregators as tools; leave theorem-proving to the theory arm.

## Open problems (field-level)

1. No pipeline preserves deep normative difference (tradition structures, incommensurable reasons) — everything reduces to opinion distributions (RP-08's seam).
2. Evaluation-layer aggregation is unexamined (RP-02's seam).
3. Legitimacy: consultation ≠ authorization; no pipeline has an answer (CEI contributes vocabulary, not the solution).
4. Manipulation-resistance of participatory pipelines at adversarial scale (bridging helps; unproven for constitution-writing).
5. Whose *disagreements* count: annotator pools still WEIRD-skewed; representation audits are not yet standard.

## Watch-list triggers

- A lab sources constitution content from structured multi-tradition input (bet B5) → RP-08's thesis validated externally; pitch collaboration immediately.
- Aggregation-sensitivity analysis published for any benchmark → RP-02 novelty check; accelerate or reposition within a cycle.
- Community-Notes-style bridging applied to value/principle aggregation in any deployed system → acquire, and test as CONCLAVE pipeline (b) upgrade.
- MAI moral-graph v2 or successor at population scale → re-evaluate whether tradition structures can be *elicited* rather than corpus-derived (would change RP-08 Phase A).
