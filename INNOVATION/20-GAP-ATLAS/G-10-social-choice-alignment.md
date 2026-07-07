# G-10 — Social Choice for Alignment

**Stage D** · **Ratings S/T/F: H/M/M** · **Programs: RP-02 FAIRGOLD** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## Statement                       [KERNEL — FROZEN]
Social choice for alignment matured into a self-conscious subfield — RLHF exposed as a majoritarian aggregator, with axiomatically better alternatives — and the vault has ~5 mentions and none of the technical literature.

## Why it matters                  [KERNEL — FROZEN]
Severity H: aggregation choices silently decide whose values survive training AND evaluation; the theory arm proved the default choice is among the worst. Tractability M / CEI-fit M: CEI shouldn't prove theorems, but the evaluation-layer application (majority-gold labels commit the named sins) is unclaimed and entirely within CEI's competence.

## Evidence                        (corpus + field)
**Corpus baseline:** ~5 social-choice mentions; KB-12 covers "whose values" conceptually but not this technical literature.

**Field:** social choice theorists noticed RLHF is an aggregation mechanism and proved it a bad one — Bradley-Terry preference fitting behaves like a Borda count, majoritarian and cycle-prone as annotator pools diversify (Front D causal story):
- **The naming survey:** "AI Alignment From Social Choice Perspectives" (Halpern, Micha, Procaccia et al.; ⚠ arXiv:2606.21550, SIGecom Exchanges, June 2026), descending from the ICML-2024 position paper (arXiv:2404.10271).
- **Axiomatic aggregators:** population-proportional alignment (arXiv:2506.05619); pairwise-calibrated reward *distributions* — keep disagreement, don't average it (arXiv:2506.06298); multiplayer Nash preference optimization as maximal lottery (arXiv:2509.23102); distortion of preference optimization (arXiv:2505.23749); clone-robust reward learning (arXiv:2501.09254); ranked-choice feedback (arXiv:2510.23631).

## State of the art
A live theory arm with axiomatic guarantees, but its indictment targets *training* aggregation. The same indictment applies to **majority-gold benchmark labels** — which commit exactly the flattening these papers formalize — and nobody has run it (Front D open problem 2). That is RP-02's short, CEI-owned bridge: **import the axioms, don't reprove them**; build a fairgold rescoring toolkit that runs published aggregation rules over disaggregated-label benchmarks, demonstrate aggregation-sensitivity on ≥2 benchmarks, and propose it as a reporting standard. CEI shouldn't prove theorems (CEI-fit M) but has clear standing in evaluation practice.

## What closing looks like         [KERNEL — FROZEN]
M1 — the axiomatic cluster acquired (survey, proportional, calibrated, distortion, clone-robustness). M2 — the fairgold rescoring toolkit runs published aggregation rules over disaggregated-label benchmarks. M3 — aggregation-sensitivity analysis demonstrated on ≥2 benchmarks and proposed as a reporting standard (RP-02).

## CEI response                    [KERNEL — FROZEN]
RP-02 FAIRGOLD — import the axioms, don't reprove them; the target is evaluation practice, where CEI has standing.

## OPUS-EXPAND checklist           (LIVING)
- [ ] ⚠ Verify the survey 2606.21550 resolves and confirm author list (Halpern/Micha/Procaccia) before external citation.
- [ ] Deep-read population-proportional 2506.05619 and pairwise-calibrated 2506.06298; summarize both aggregation rules into §State of the art as the first two toolkit implementations.
- [ ] Identify ≥2 disaggregated-label benchmarks (with per-annotator labels retained) as M3 targets; add a candidate table.
- [ ] Specify the fairgold rescoring toolkit interface (M2): input disaggregated labels → apply {majority, proportional, calibrated, distortion-min, clone-robust} → output score deltas.
- [ ] Deep-read distortion 2505.23749 and clone-robust 2501.09254 to select the aggregation axioms most diagnostic for benchmark labels.
- [ ] Check Front D watch-list trigger: has aggregation-sensitivity analysis been published for any benchmark? If yes, run the RP-02 novelty check.

## Sources                         (evidence classes marked)
- Social Choice for AI Alignment (survey) — arXiv:2606.21550 (SIGecom Exchanges) — **⚠ UNCONFIRMED** (2606 ID; verify-at-download).
- Social Choice should guide AI (ICML position) — arXiv:2404.10271 — **SEARCH-CONFIRMED**.
- Population-Proportional Alignment — arXiv:2506.05619 — **SEARCH-CONFIRMED**.
- Pairwise Calibrated Rewards — arXiv:2506.06298 — **SEARCH-CONFIRMED**.
- Distortion of AI Alignment — arXiv:2505.23749 — **SEARCH-CONFIRMED**.
- Clone-Robust AI Alignment — arXiv:2501.09254 — **SEARCH-CONFIRMED**.
- Multiplayer Nash Preference Optimization — arXiv:2509.23102 — **SEARCH-CONFIRMED**.
- VISPA Pluralistic Alignment (Zheng) — arXiv:2601.12758 — **VERIFIED** (IN-VAULT: `papers/2026-Zheng-VISPA Pluralistic Alignment.md`).
- Corpus baseline (~5 mentions; KB-12 conceptual) — **VERIFIED** (`../02-gap-atlas.md`).
