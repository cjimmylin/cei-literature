# RP-06 SAYDO — Does Stated Moral Reasoning Cause Moral Behavior?

**Gaps:** G-13 (CoT faithfulness for values), G-23 (coherent values / utility–behavior gap)
**Portfolio claim:** measurement science · **Wave:** 3 (careful causal design)
**Author:** Fable 5 · 2026-07-07

## Motivation

Three literatures are circling one question without meeting. (1) CoT faithfulness: stated reasoning ≠ causal reasoning; metrics, obfuscation stress tests, and faithfulness training now exist — all validated on math/QA, never on moral reasoning. (2) Utility engineering vs. the utility–behavior gap: elicited value systems may not drive incentivized behavior. (3) CEI's own expressed-vs-revealed line (UNMARKED). The joint question — *when a model justifies an ethical choice, is the justification load-bearing?* — is foundational for every benchmark that rubric-scores moral reasoning (many CEI benches; FRAMESHIFT's framework-steerability claim depends on it directly) and for the lab thesis that teaching *reasons* produces robust values ("Teaching Claude why"). Nobody has run the moral-domain version.

## Core hypothesis

**H1 (gap exists):** There is a measurable say–do structure: expressed values (survey), revealed values (behavioral choice), and stated reasoning (justification) form a triangle with systematic, model-specific gaps — not a single coherent value system measured three ways.
**H2 (causality is partial):** Counterfactual perturbation of the reasoning premise changes the choice in only a fraction of cases (reason-causality rate < 1), and the rate varies by framework, stakes, and whether the setting is announced.
**H3 (steering is rhetorical):** Under instructed-framework conditions (FRAMESHIFT lineage), a measurable share of "framework-conditioned reasoning" changes the *justification style* without changing the *choice pattern* — steerability of rhetoric, not of values.

## Method sketch

1. **Matched triplets.** For each scenario: (a) expressed probe (direct question), (b) revealed probe (agentic version where the choice has task consequences — UNMARKED machinery), (c) reasoned probe (choice + justification elicited). Same underlying dilemma, delivery-isolated (separate sessions, order counterbalanced — the SERMONMOUNT counterbalance lesson applies: *execute* the counterbalance, don't just design it).
2. **Causal tests.** (i) Premise swap: rerun with the model's own stated key premise counterfactually altered in context; does the choice flip? (ii) Reason ablation: elicit choice-then-reason vs. reason-then-choice; compare choice distributions (if reasoning is causal, reason-first should shift choices). (iii) Faithfulness-metric transfer: apply the published faithfulness/verbosity decompositions to moral justifications.
3. **Moderators.** Framework (consequentialist/deontological/virtue framings), stakes (trivial ↔ severe), announcement (links to RP-07 HAWTHORNE).
4. **Models.** 6+ frontier models, cross-vendor; reasoning models vs. non-reasoning siblings are the key contrast (deliberative-alignment training should *increase* reason-causality if the lab thesis is right — a falsifiable prediction worth pre-registering).

## Novelty vs. published work

Faithfulness methods exist but have never touched normative content; the utility–behavior debate uses preference elicitation, not reasoning traces; CEI's expressed-vs-revealed work never perturbed the reasoning. The three-way triangulation with causal perturbation is new, and the reasoning-model-vs-sibling contrast turns a methods paper into an alignment-relevant test of the deliberative-alignment paradigm.

## Deliverables

1. SAYDO battery (matched triplets + perturbation variants; public release candidate).
2. Reason-causality estimates across frontier models (the headline table).
3. H3 finding as a direct amendment to FRAMESHIFT's validity section.
4. Paper (target: main-track — touches faithfulness, evaluation validity, and training-paradigm assessment at once).

## Opus build tasks

- O1: Triplet authoring from existing bank scenarios (Opus, with Fable-tier gate on a 30-item sample before scale-up — premise-swap items are subtle and easy to botch).
- O2: Delivery harness with session isolation + executed counterbalance verification (add an automated check, per the SERMONMOUNT MF-4 lesson).
- O3: Perturbation-pipeline + confound analysis plan (pre-registered; the premise-swap confound analysis is the pilot's whole job).
- O4: Main run (keys-gated) + analysis.

## Kill criteria

- **K1:** If the pilot confound analysis shows premise swaps can't isolate the stated reason (swaps change other scenario features raters detect), the causal design fails — fall back to the correlational triangle (H1 only) and say so plainly.
- **K2:** If choice measures lack test-retest stability (same model, same item, r < 0.6 across reruns at temperature), the say–do "gap" would be noise — fix decoding/administration before any gap claims.
- **K3:** A *high* reason-causality result (reasoning is faithful for values) is not a kill — it validates rubric-scored benches and the deliberative thesis; publish either way.
