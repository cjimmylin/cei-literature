# I-15 — Social Choice as RLHF's Missing Theory

**Tier 3** · **Gaps: G-10** · **Programs: RP-02 FAIRGOLD** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]

Vanilla RLHF is a disguised majoritarian aggregator — Bradley-Terry fitting behaves like a Borda count, Condorcet cycles become near-certain as annotator pools grow — and axiomatically superior alternatives now exist: population-proportional alignment, pairwise-calibrated reward distributions, maximal-lottery Nash learning, distortion bounds, clone-robustness.

## Key results

- **The survey that names the field** (Halpern, Micha, Procaccia et al.; ⚠ 2606.21550, SIGecom Exchanges, June 2026 — ⚠ UNCONFIRMED), descending from the ICML-2024 position paper (2404.10271, Conitzer/Procaccia/Russell et al. — SEARCH-CONFIRMED): RLHF is an aggregation mechanism and a majoritarian, cycle-prone one.
- **Axiomatic aggregators** (all SEARCH-CONFIRMED): population-proportional alignment (2506.05619); pairwise-calibrated reward *distributions* that match annotator fractions without annotator IDs (2506.06298); multiplayer Nash preference optimization as maximal lottery (2509.23102); distortion of preference optimization (2505.23749); clone-robust reward learning (2501.09254); ranked-choice feedback beyond pairwise (2510.23631).
- **Distributional pluralism** (SEARCH-CONFIRMED): Spectrum Tuning (2510.06084), survey-distribution alignment (2510.21977) — match the population distribution, not the median.

## Mechanisms & caveats

The Borda-count analogy is the crux: Bradley-Terry fitting scores an option by summed pairwise wins, which inherits Borda's known pathologies (clone-sensitivity, cycle-induced instability) that intensify as annotator pools diversify. The alternatives carry *axiomatic* guarantees (proportionality, distortion bounds, clone-robustness) but are proven for *training*, not evaluation — the transfer to gold-labeling is CEI's to make, not the theory arm's. The survey ID is ⚠ UNCONFIRMED (same-month 2606.*); verify the abstract before external citation. Import discipline is essential: CEI applies axioms, it does not re-prove theorems.

## Implications for CEI practice   [KERNEL — FROZEN]

(a) The same indictment applies to majority-gold benchmark labels — RP-02's whole premise; CEI applies the axioms to evaluation, where it has standing. (b) "Aggregation-sensitivity analysis" should become a CEI reporting standard and an exported one. (c) Distributional scoring (match the population's answer distribution) is a scoring mode CEI banks can support with disaggregated labels — design new banks to RETAIN disaggregation. (d) Import, don't prove: cite the theory arm; CEI's contribution is empirical consequence, not theorems.

## Cross-links

- **Gaps:** G-10 (social choice for alignment); adjacent G-11 (deliberation pipelines → I-16), G-05 (preference-data provenance).
- **Ideas:** I-16 (the practice arm applies these axioms to deliberation); I-10 (RMs are where training-side aggregation lands).
- **Programs:** RP-02 FAIRGOLD (H1 aggregation-invariance of benchmark verdicts; the `fairgold` rescoring toolkit implements exactly this rule family); RP-08 CONCLAVE (aggregation over traditions).
- **Field map:** Front D — Aggregation (theory arm; entry point 1 "aggregation-sensitivity for evaluation").
- **Vault:** overlaps KB-12 ("whose values") conceptually, but that lacks the technical literature.

## OPUS-EXPAND checklist           (LIVING)

- [ ] Verify the ⚠ 2606.21550 survey abstract/authorship at download; upgrade to SEARCH-CONFIRMED or correct the ID before any external use.
- [ ] Fetch 2505.23749 (distortion) and 2506.05619 (population-proportional); extract the exact rule definitions to implement in the `fairgold` rescoring engine (RP-02 O2).
- [ ] Build the concrete Bradley-Terry ≈ Borda demonstration as a worked example for the RP-02 paper's framing.
- [ ] Inventory which CEI banks already retain disaggregated labels vs. discard them (kernel point c — feeds RP-02 "finding #0").
- [ ] Draft "aggregation-sensitivity analysis" as a one-table reporting standard for the COOKBOOK pre-registration checklist.

## Sources

- ⚠ 2606.21550 Social Choice for AI Alignment (survey) — ⚠ UNCONFIRMED (P1, G-10)
- 2404.10271 Social Choice should guide AI (ICML position) — SEARCH-CONFIRMED
- 2506.05619, 2506.06298, 2509.23102, 2505.23749, 2501.09254, 2510.23631 (axiomatic aggregators) — SEARCH-CONFIRMED
- 2510.06084 Spectrum Tuning; 2510.21977 Survey-distribution alignment — SEARCH-CONFIRMED
- Companion: `../02-gap-atlas.md` §G-10; `../10-FIELD-MAP/D-aggregation.md`; `../05-research-programs/RP-02-FAIRGOLD.md`
