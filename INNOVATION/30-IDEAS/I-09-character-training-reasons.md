# I-09 — Character Training with Reasons

**Tier 2** · **Gaps: G-22** · **Programs: RP-01/RP-09 axis** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]
Training on constitutional documents plus narratives of an aligned AI — teaching WHY, not just WHAT — cut agentic misalignment more than 3× on unrelated scenarios; reasons appear to generalize where rules memorize. Counterweight: optimizing a warmth trait measurably costs accuracy and raises sycophancy.

## Key results
- **"Teaching Claude why"** (Anthropic, May 2026): training on constitution + narratives of an aligned AI cuts agentic misalignment **>3×** on unrelated scenarios; *reasons generalize, rules memorize* (Front A/B).
- **Open Character Training** (arXiv:2511.01689): an open replication pipeline exists outside Anthropic — external baselines become possible.
- **Counterweight** (Nature 2026): optimizing a **warmth** trait measurably costs accuracy and raises sycophancy (the warmth→accuracy/sycophancy trade-off) — trait specification has costs.

## Mechanisms & caveats
The reasons-vs-rules contrast is **externally testable** with CEI's out-of-distribution value banks (G-22 M2) — the labs have only internal metrics, so CEI's OOD banks can answer "does teaching *why* beat teaching *rules*?" better than they can. The warmth result means spec grading (RP-01) should carry a **cost-side dimension**: a trait spec is not free. CEI's religious-ethics corpora are, structurally, reason-giving traditions — potential source material for character-training research collaborations. And narrative training data is a values vector whose *provenance* questions connect to subliminal transmission (I-12). Caveats: "Teaching Claude why" and the Nature warmth paper are SEARCH-CONFIRMED non-arXiv sources; external replication of the reasons-generalize claim is absent (Front A open problem 3) — treat the 3× as a lab-internal result pending OOD confirmation.

## Implications for CEI practice   [KERNEL — FROZEN]
(a) The reasons-vs-rules contrast is externally testable with CEI's OOD banks (G-22 M2) — the labs have only internal metrics. (b) Trait-specification costs (warmth result) mean spec grading (RP-01) should include a cost-side dimension. (c) CEI's religious-ethics corpora are, structurally, reason-giving traditions — potential source material for character-training research collaborations. (d) Narrative training data as a values vector: watch for its provenance questions (connects to I-12).

## Cross-links
- **Gaps:** G-22 (character-training science), G-20 (the misalignment it reduces).
- **Ideas:** I-08 (deliberative alignment — reasoning-side sibling), I-06 (constitutions as training data), I-12 (narrative-data provenance).
- **Programs:** RP-01/RP-09 shared axis (OOD generalization test); RP-09 SEISMOGRAPH (the dependent variable for the 3× claim).
- **Field-map front:** A + B + G; watch-trigger: character-training replications outside Anthropic (baselines for the reasons-vs-rules test).

## OPUS-EXPAND checklist           (LIVING)
- [ ] Manually ingest "Teaching Claude why" and the Nature warmth paper per `../04-missing-literature.md`; file `papers/` notes.
- [ ] Design the OOD reasons-vs-rules test using an existing CEI value bank as the external metric the labs lack (G-22 M2).
- [ ] Add a cost-side dimension (trait-specification trade-offs) to the RP-01 SPECGRADE metric suite (implication (b)).
- [ ] Deep-read Open Character Training 2511.01689; assess whether its pipeline yields the trained-model baselines RP-09 needs.
- [ ] Draft a one-page character-training collaboration pitch grounded in CEI's reason-giving religious-ethics corpora (implication (c)).

## Sources                         (evidence classes marked)
- Teaching Claude why (reason-based > rule-based) — anthropic.com/research/teaching-claude-why — **SEARCH-CONFIRMED** (non-arXiv, manual ingest).
- Open Character Training — arXiv:2511.01689 — **SEARCH-CONFIRMED**.
- Training warm models reduces accuracy (warmth→sycophancy) — Nature 2026 (s41586-026-10410-0) — **SEARCH-CONFIRMED** (non-arXiv, manual ingest).
- Corpus status (absent) — **VERIFIED** (`../02-gap-atlas.md` G-22).
