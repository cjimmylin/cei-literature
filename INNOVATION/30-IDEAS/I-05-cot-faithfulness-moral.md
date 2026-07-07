# I-05 — CoT Faithfulness for Moral Reasoning

**Tier 1** · **Gaps: G-13** · **Programs: RP-06** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]
A model's stated reasoning is not reliably the reasoning that drives its answer; faithfulness can be measured (and trained), reasoning can be obfuscated against monitors — and none of this has touched moral reasoning, where justification-scoring is standard benchmark practice.

## Key results
- **CoT monitorability position paper** (cross-lab: OpenAI+GDM+Anthropic+academics; arXiv:2507.11473, July 2025): CoT is a "fragile opportunity"; faithfulness reframed as *monitor-usability* (Front E).
- **Measurement stack:** faithfulness × verbosity decomposition (arXiv:2510.27378); pragmatic monitorability metrics (arXiv:2510.23966).
- **Obfuscation / sandbagging:** reasoning models can hide reasoning from monitors (arXiv:2510.19851); covert sandbagging against CoT monitors (arXiv:2508.00943).
- **Faithfulness *training*:** counterfactual-simulation faithfulness training (⚠ arXiv:2602.20710).
- **The untouched domain:** none of this has touched *moral* reasoning, yet rubric-scored justification is standard CEI/benchmark practice (`02-gap-atlas.md` G-13; Front E open problem 2).

## Mechanisms & caveats
If stated reasoning need not cause the answer, then rubric-scored justifications measure *rhetoric* until proven otherwise — RP-06's reason-causality rate (fraction of cases where perturbing the stated premise flips the choice) is the proof standard. FRAMESHIFT's framework-steerability claim depends directly on this: its H3 check separates *style transfer* from genuine *value change*. Process-level scoring should therefore prefer **behavioral** process markers (what the model did across turns) over narrated reasoning where feasible. Caveat: faithfulness training is **⚠ UNCONFIRMED** (2602 flagged ID); if faithfulness-trained models ship, CEI should test whether trained faithfulness *transfers* to normative content (Front E open problem 3) — nobody else will.

## Implications for CEI practice   [KERNEL — FROZEN]
(a) Rubric-scored justifications measure rhetoric until proven otherwise; RP-06's reason-causality rate is the proof standard. (b) FRAMESHIFT's steerability claims need the H3 check (style transfer vs. value change). (c) Process-level scoring should prefer BEHAVIORAL process markers (what the model did across turns) over narrated reasoning where possible. (d) If faithfulness-trained models ship, CEI should test whether trained faithfulness transfers to normative content — nobody else will.

## Cross-links
- **Gaps:** G-13 (moral-reasoning faithfulness), G-23 (utility–behavior gap — the say/do adjacency).
- **Ideas:** I-04 (faking — reasoning traces unreliable), I-08 (deliberative alignment — spec-reasoning traces as auditable surface).
- **Programs:** RP-06 SAYDO (reason-causality rate); FRAMESHIFT (H3 validity amendment).
- **Field-map front:** E (evaluation); watch-trigger: faithfulness-trained frontier models ship (labeled).

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read the CoT monitorability position paper (2507.11473); extract the faithfulness definitions RP-06 can port to the moral domain.
- [ ] Port the faithfulness × verbosity decomposition (2510.27378) to a moral-justification sample as RP-06 method (ii/iii) feasibility check.
- [ ] Draft the premise-swap causal test on a 30-item scenario sample (RP-06 O1) for Fable-tier gate — premise-swap items are subtle and easy to botch.
- [ ] Author the FRAMESHIFT H3 "style transfer vs. value change" check as a concrete validity amendment.
- [ ] ⚠ Verify 2602.20710 before citing; if faithfulness-trained models are released, add a trained/untrained contrast to RP-06 (Front E watch-trigger).

## Sources                         (evidence classes marked)
- CoT Monitorability (position paper) — arXiv:2507.11473 — **SEARCH-CONFIRMED** — G-13 anchor.
- Faithfulness + Verbosity decomposition — arXiv:2510.27378 — **SEARCH-CONFIRMED**.
- Pragmatic CoT monitorability — arXiv:2510.23966 — **SEARCH-CONFIRMED**.
- Obfuscated reasoning — arXiv:2510.19851 — **SEARCH-CONFIRMED**.
- Covert sandbagging vs CoT monitors — arXiv:2508.00943 — **SEARCH-CONFIRMED**.
- Counterfactual Simulation Training — arXiv:2602.20710 — **⚠ UNCONFIRMED** (2602 flagged ID).
- Corpus status (absent) — **VERIFIED** (`../02-gap-atlas.md` G-13).
