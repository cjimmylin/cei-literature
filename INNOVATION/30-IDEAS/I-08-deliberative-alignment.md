# I-08 — Deliberative Alignment / Reasoning-over-the-Spec

**Tier 2** · **Gaps: G-02** · **Programs: RP-01 (context)** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]
Train models to explicitly reason over the spec at inference (deliberative alignment), extended by test-time deliberation methods that improve spec-following across models — making spec text behaviorally live and spec quality a direct behavioral variable.

## Key results
- **Deliberative alignment:** reasoning models trained to consult an explicit spec at inference — the mechanism that converts spec text from PR into a functional training target (Front A causal story).
- **Test-time deliberation** (SpecBench/Align3; arXiv:2509.14760): spec-following improves with inference-time reflection across **33 models** — spec quality is behaviorally live.
- **Applied to scheming reduction:** deliberative methods used to train against covert behavior, measured by CoT-based evals (Front E; OpenAI+Apollo 2025) — oversight and evaluation fusing.
- **The critique wing:** Millière's "shallow alignment" (arXiv:2506.04679, Phil Studies) — spec-following ≠ genuine normative deliberation; adversarial norm-conflict exposes the difference.

## Mechanisms & caveats
Spec bugs (G-02) now propagate to behavior through a **known mechanism**, giving RP-01's prospective H2 (ex-ante spec-quality scores predict adherence failures) a causal story rather than a mere correlation. The reasoning-mode vs. non-reasoning sibling contrast becomes a standing experimental control worth building into CEI designs — SAYDO already does, predicting deliberative-alignment training should *increase* reason-causality if the lab thesis holds. Deliberation traces over specs are auditable artifacts — a future probe surface for faithfulness work (I-05). Caveat to carry: Millière's shallow-alignment critique — spec-reasoning ≠ robust normativity; treat deliberative gains as **hypothesis, not fact** (Front A open problem 3). Evidence class: SEARCH-CONFIRMED across the cluster.

## Implications for CEI practice   [KERNEL — FROZEN]
(a) Spec bugs now propagate to behavior through a known mechanism — RP-01's prospective H2 has a causal story. (b) Reasoning-mode vs. non-reasoning siblings is a standing contrast worth building into CEI designs (SAYDO already does). (c) Deliberation traces over specs are auditable artifacts — a future probe surface for faithfulness work (I-05). (d) Caveat to carry: Millière's shallow-alignment critique — spec-reasoning ≠ robust normativity; treat deliberative gains as hypothesis, not fact.

## Cross-links
- **Gaps:** G-02 (specification engineering — bugs made behaviorally live), G-22 (reasons-vs-rules axis).
- **Ideas:** I-06 (the specs), I-07 (adherence auditing), I-05 (faithfulness of deliberation traces), I-09 (character training with reasons — the training-side sibling).
- **Programs:** RP-01 SPECGRADE (H2 causal story); RP-06 SAYDO (reasoning-mode contrast).
- **Field-map front:** A (specification).

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read SpecBench/Align3 2509.14760; extract the test-time deliberation manipulation as an RP-01 H2 model-condition (deliberation on/off).
- [ ] Deep-read Millière 2506.04679; capture the adversarial norm-conflict cases that expose shallow alignment as RP-01 stress items and a standing caveat.
- [ ] Specify the reasoning-mode vs. non-reasoning-sibling contrast as a reusable CEI design control (implication (b)); confirm SAYDO's version.
- [ ] Scope spec-deliberation traces as a faithfulness probe surface (implication (c)) linking to RP-06.
- [ ] Flag the "hypothesis, not fact" framing in any RP-01 write-up citing deliberative gains (implication (d)).

## Sources                         (evidence classes marked)
- Test-time deliberation (SpecBench/Align3) — arXiv:2509.14760 — **SEARCH-CONFIRMED**.
- Normative Conflicts & Shallow AI Alignment (Millière) — arXiv:2506.04679 (Phil Studies) — **SEARCH-CONFIRMED**.
- Scheming reduction via deliberative methods (OpenAI + Apollo 2025) — **SEARCH-CONFIRMED**.
- Corpus status (absent) — **VERIFIED** (`../02-gap-atlas.md` G-02).
