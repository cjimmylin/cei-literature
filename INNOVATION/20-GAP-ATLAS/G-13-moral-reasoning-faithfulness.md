# G-13 — Moral-Reasoning Faithfulness

**Stage E** · **Ratings S/T/F: H/H/H** · **Programs: RP-06 SAYDO** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## Statement                       [KERNEL — FROZEN]
Chain-of-thought faithfulness became a measurement subfield — metrics, obfuscation stress tests, faithfulness training — validated entirely on math/QA; whether models' stated MORAL reasoning causes their moral behavior has never been tested, and every justification-scored values benchmark assumes it does.

## Why it matters                  [KERNEL — FROZEN]
Severity H: if moral justifications are epiphenomenal, rubric-scored reasoning measures rhetoric, and framework-steerability results (FRAMESHIFT-style) may be style transfer. It also decides whether the labs' reasons-based training thesis has the mechanism it claims. CEI-fit H: the triangulation needs expressed-value, revealed-value, and justification instruments on matched content — CEI owns all three.

## Evidence                        (corpus + field)
**Corpus baseline (2026-07-07):** the CoT-faithfulness cluster returns effectively zero hits across 2,368 paper notes; the vault's mass is evaluation-side (Moral Reasoning 268, Helpfulness/RLHF 299), but nothing tests whether *stated* moral reasoning is causal. The vault holds no faithfulness metrics, no obfuscation-monitor literature, and no moral-domain application of either.

**Field (Front E causal story):** CoT monitorability consolidated from a July-2025 cross-lab position paper into a measurement subfield within one year. The stack now includes a faithfulness × verbosity decomposition, pragmatic monitorability metrics, obfuscation stress tests (reasoning models can hide reasoning from monitors), covert sandbagging against CoT monitors, and counterfactual-simulation faithfulness *training*. Every artifact validates on math/QA. The unfaithfulness finding — the reasoning models show is not reliably the reasoning that drives their answers — converts every CEI bench that rubric-scores justifications, and FRAMESHIFT's framework-conditioned-reasoning claim specifically, into an *assumption* that stated reasoning is load-bearing. That assumption is now empirically attackable, and no one has attacked it on normative content.

## State of the art
Faithfulness is a mature methods subfield for math/QA and an empty field for morality. The open seam (RP-06): a three-way triangle — expressed value (survey), revealed value (agentic/behavioral choice, UNMARKED machinery), stated reasoning (justification) — on matched dilemmas, with a premise-swap causal test (counterfactually alter the model's own stated key premise; does the choice flip?). The reasoning-model-vs-non-reasoning-sibling contrast doubles as a falsifiable test of the deliberative-alignment paradigm: if teaching reasons produces robust values, reason-causality should be *higher* in reasoning models. Nobody outside has the matched expressed/revealed/justification instruments to run it.

## What closing looks like         [KERNEL — FROZEN]
M1 — faithfulness stack acquired. M2 — SAYDO's pilot confound analysis establishes (or fails) that premise-swap perturbations isolate the stated reason. M3 — reason-causality rates published across frontier models with the reasoning-model vs. sibling contrast, directly testing the deliberative-alignment paradigm.

## CEI response                    [KERNEL — FROZEN]
RP-06 SAYDO. The design pre-commits to the correlational fallback (K1) — a triangle without causal arrows is still the first moral-domain faithfulness data.

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read the CoT monitorability position paper (2507.11473) and record how it defines faithfulness as monitor-usability; note what transfers to normative content and what doesn't.
- [ ] Extract the faithfulness × verbosity decomposition (2510.27378) and the obfuscation stress-test protocol (2510.19851); assess whether either metric applies to a moral justification with no ground-truth answer key.
- [ ] Draft the premise-swap confound-analysis plan (RP-06 K1): enumerate the scenario features a premise swap co-perturbs and how raters would detect them — the pilot's whole job.
- [ ] Specify the reasoning-model / non-reasoning-sibling model pairs available API-only, and pre-register the deliberative-alignment prediction (reason-causality higher in reasoning models).
- [ ] Cross-reference FRAMESHIFT's validity section: mark exactly which of its steerability claims become "style transfer" if H3 (rhetorical steering) holds.
- [ ] Check Front E watch-list: if faithfulness-trained frontier models ship labeled as such, add a trained/untrained contrast to the SAYDO design.

## Sources                         (evidence classes marked)
- CoT Monitorability (cross-lab position paper) — arXiv:2507.11473 (July 2025) — **SEARCH-CONFIRMED** — G-13 anchor.
- Faithfulness + Verbosity decomposition — arXiv:2510.27378 — **SEARCH-CONFIRMED**.
- Pragmatic CoT monitorability — arXiv:2510.23966 — **SEARCH-CONFIRMED**.
- Obfuscated reasoning (stress test) — arXiv:2510.19851 — **SEARCH-CONFIRMED**.
- Covert sandbagging vs CoT monitors — arXiv:2508.00943 — **SEARCH-CONFIRMED**.
- Counterfactual Simulation Training — arXiv:2602.20710 — **⚠ UNCONFIRMED** (verify-at-download).
- Corpus grep baseline (CoT-faithfulness ~0 hits, 2,368 notes, 2026-07-07) — **VERIFIED** (`../02-gap-atlas.md`).
