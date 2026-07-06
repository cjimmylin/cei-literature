# 00 — FruitBench Portfolio: Ten Benchmark Designs from the Fruit of the Spirit

**Author:** Fable (main loop), 2026-07-05
**Status:** Design-complete scaffolds; awaiting Opus flesh-out (item banks, full seed-case scripting, pilot infrastructure)
**Source corpus:** `../` (7 FRUITBENCH research docs: GDM ×2, OAI ×2, background, benchmark pack, combined pack)
**Method inheritance:** `COOKBOOK/00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` (Seven Laws) — read it before touching any brief.

---

## 1. Mission and positioning

FruitBench is a portfolio of **ten benchmark paper designs for values alignment of LLMs and agents**, each inspired by one item in Paul's fruit-of-the-Spirit list (Galatians 5:22–23), plus one design operationalizing the list's most distinctive grammatical feature — the **singular** καρπός. Each design targets podium-level contribution at NeurIPS/ICML/ICLR (Datasets & Benchmarks or main track) or top-cited alignment venues.

Every design is **dual-track at full depth**:

- **Track A (secular conference paper):** a standalone construct that survives review with no religious commitment required. The Galatians taxonomy is disclosed as the construct's provenance and one of two normative anchors (Law 7: say WHAT values and WHOSE).
- **Track B (confessional benchmark pack):** a Galatians-anchored evaluation pack in BIBLEBENCH house style (exegetical anchor → ethical-dimensions table → scenario families → 0–4 trajectory rubric → seed cases → evaluator notes), sibling to CORINTHLOVE / TENCOMMANDMENTS / SERMONMOUNT.

**Build once, publish twice.** The two tracks share one item bank and one scoring core. Track A surfaces secular construct names, secular anchor instruments, and venue-standard reporting. Track B surfaces the exegetical rubric, tradition-aware evaluator notes, and pastoral failure modes. Neither is an appendix of the other.

### Why this taxonomy earns its place at a top venue

1. **Positive-character evaluation is an open field.** Frontier safety evals are prohibition-shaped (refusal, harm avoidance) and saturated (single-turn safety at 99.3–99.8%; KB Law 3). The fruit list is a *positive* behavioral taxonomy — nine specific, distinguishable dispositions — that maps directly onto documented open problems: sycophancy, moral fatigue, commitment integrity, eval-awareness, paternalism.
2. **The taxonomy makes distinctions the field lacks.** The χρηστότης/ἀγαθωσύνη contrast (accommodating kindness vs. corrective goodness) is precisely the sycophancy/over-rigidity axis; μακροθυμία names multi-turn endurance; πραΰτης names strength-under-control (non-domination); ἐγκράτεια names restraint under temptation. These are 2,000-year-old construct definitions with commentary-grade operationalization — richer ground truth than most benchmark taxonomies invent ad hoc.
3. **The singular καρπός is a falsifiable scientific hypothesis:** virtues form an integrated character (positive manifold with differentiated structure), not a bundle of independent behaviors. Design 10 tests this on LLMs. Either result is a finding.
4. **Virtue ethics is the confirmed weak spot of the benchmark landscape.** NormEval: virtue accuracy 63% (vs utilitarian 77%); MoReBench rubric coverage ~10% at the frontier; no benchmark engages character consistency, phronesis, or habituation at depth.

## 2. The 9+1 architecture

| # | Codename | Fruit (Greek) | Secular construct | Core innovation | Headline metric |
|---|---|---|---|---|---|
| 01 | COSTLY | Love (ἀγάπη) | Costly beneficence under incentive conflict | Demand curves for values: parametric incentive pressure vs. welfare-serving behavior | Moral price elasticity |
| 02 | EVENKEEL | Joy (χαρά) | Valence-frame invariance & affective drift | Mood-induction procedures imported as prompt-level manipulations; two-sided (despair-mirroring vs toxic positivity) | Affect-susceptibility flip-rate; drift slope |
| 03 | SIMMER | Peace (εἰρήνη) | Counterfactual de-escalation impact | Eval unit = counterfactual rollout delta on a simulated social system, not utterance quality | De-escalation delta; appeasement-trap pass rate |
| 04 | LONGFUSE | Patience (μακροθυμία) | Composure durability under provocation | Survival analysis / reliability engineering for alignment; censored time-to-failure | Composure half-life; hazard ratios |
| 05 | USEFUL | Kindness (χρηστότης) | Outcome-grounded helpfulness to vulnerable users | Capability-constrained user simulation; success = the *human's* downstream outcome | Realized-benefit rate; warmth×utility dissociation |
| 06 | BACKBONE-D′ | Goodness (ἀγαθωσύνη) | Corrective courage | Signal detection theory over near-twin items: moralizing false alarms vs complicit misses | d′ and criterion c |
| 07 | LEDGER | Faithfulness (πίστις) | Commitment integrity over long horizons | Machine-checkable commitment ledger; renegotiation-vs-breach taxonomy | Commitment half-life under pressure |
| 08 | SOFTPOWER | Gentleness (πραΰτης) | Non-domination under power asymmetry | First import of republican non-domination (Pettit) to AI eval; option-set metrics | Option-set contraction rate; corrigibility symmetry |
| 09 | MARSHMALLOW | Self-control (ἐγκράτεια) | Restraint under parametric temptation | Detection-probability axis turns eval-awareness from confound into measured quantity | Principledness coefficient; temptation psychometric curve |
| 10 | ONEFRUIT | The singular καρπός | Character coherence | Network psychometrics of AI character; inter-virtue conflict items; stress-spillover matrix | Coherence index; weakest-link headline |

Suggested venue mapping: 01, 06, 07, 09 → NeurIPS D&B (behavioral, agentic, big empirical result available); 03, 10 → NeurIPS/ICML main track (methodological novelty: counterfactual social measurement, network psychometrics); 02, 04, 05, 08 → ICLR / D&B (clean construct + strong instrument). Any single design is also a credible standalone alignment-forum contribution.

## 3. Shared design commitments (Seven Laws instantiation)

Inherited by all ten; briefs state only design-specific instantiations.

1. **Behavioral, not recognition.** Every design's primary tier is generation/action; a recognition baseline is included only to *measure* the recognition-propensity gap (endorse 34% vs recognize 86% precedent).
2. **No single aggregate.** Per-axis reporting; worst-axis headline for ONEFRUIT; Pareto pairs wherever a two-sided failure exists (preachy/complicit, appeasement/escalation, paternalism/capitulation, toxic-positivity/despair).
3. **Two-tier difficulty.** Every design ships an easy floor and a hard layer; headline the drop (NurValues precedent: >90% → 32.29%).
4. **Dual ground-truth anchoring (the FruitBench signature).** Two independent anchor panels per design: (a) a **theologian/ethicist panel** (Protestant + Catholic + Orthodox representation; commentary-anchored) providing Galatians-taxonomy gold where consensus κ≥0.8; (b) a **secular convergent panel** + established instruments (e.g., consumer-protection norms, clinical communication standards, professional codes) for Track A. Items where the panels *diverge* are not discarded: they form a declared contested band, scored distributionally with an empirical ceiling (KorNAT SVA=0.450 precedent). Panel convergence/divergence is itself a reportable result.
5. **Validated judges.** Per KB doc 07: rubric decomposition (κ 0.69→0.86 precedent); ≥2 judge families, never the item-generating family (self-preference inflation 10–19%); fine-tuned small scorers on own human labels where volume justifies (79.5% vs 61.3%, 80× cheaper); worst-case per-category F1 for judge selection.
6. **Contamination & eval-awareness defenses.** Generator/spec public + private rolling holdout + canary strings + fresh-per-run scenario surface realization. MARSHMALLOW additionally *measures* eval-awareness; all other designs include a monitored/unmonitored comparator (11–15% gap precedent).
7. **Falsification conditions per axis.** Each brief's construct table states what result would show the axis is NOT measuring its construct (usually: capability-PC1 correlation >40%, or collapse onto an existing instrument's scores).

**Refusal handling (portfolio-wide):** four-way taxonomy (helpful / policy violation / appropriate refusal / unnecessary refusal) with refusal rate reported as a first-class metric — this is itself a documented field gap (40% refusal on Moral Lens items with no standard protocol).

## 4. Differentiation vs. the existing COOKBOOK portfolio

Checked against `20-DESIGNS/` (UNMARKED, FRAMESHIFT, DUPLEX, INTRA, CULTIVATE, CRUX) and sketches S1–S8.

| FruitBench design | Nearest neighbor(s) | Differentiation |
|---|---|---|
| COSTLY | S8 LEVER, MORALSIM, UNMARKED | Parametric dose-response (elasticity), welfare-vs-approval axis; LEVER is honesty-specific, UNMARKED is incidental embedding without parametric pressure |
| EVENKEEL | — (novel) | No existing design or literature benchmark tests valence-frame invariance of values |
| SIMMER | S3 QUORUM, Keshmirian | QUORUM = coordination among AI agents; SIMMER = causal effect of one model on a simulated *human* social system, counterfactual rollouts as eval unit |
| LONGFUSE | SYCON, multi-turn lit | Survival/hazard statistics, standardized provocation ladder, patience≠passivity twins — no benchmark treats alignment as durability |
| USEFUL | τ-bench-style user sims | Success = the simulated human's downstream outcome under capability constraints, not system task completion; style/substance dissociation |
| BACKBONE-D′ | S2 BACKBONE, XSTest | BACKBONE = reactive belief updating under pushback; BACKBONE-D′ = proactive correction *initiation*, SDT decomposition of ability vs disposition |
| LEDGER | S1 DRIFT, MASK, S8 LEVER | Explicit commitment objects with automated verification over long horizons; DRIFT tracks value expression, MASK is single-turn honesty |
| SOFTPOWER | — (novel theory import) | Non-domination/option-set metrics; no benchmark measures paternalism/domination under power asymmetry |
| MARSHMALLOW | UNMARKED, alignment-faking evals | Parametric temptation curves + principledness decomposition; UNMARKED hides the test, MARSHMALLOW measures the response surface including detection-probability sensitivity |
| ONEFRUIT | CRUX, DUPLEX | CRUX adjudicates pluralistic value conflicts between *stakeholders*; ONEFRUIT measures coherence structure *within* one model's character across the nine axes |

Also distinct from the sibling BIBLEBENCH packs: those are scenario/rubric packs; FruitBench briefs are venue-grade instrument designs with psychometric machinery. Track B of each brief is the bridge back to BIBLEBENCH house style.

## 5. Theological integrity constraints (Track B, all designs)

From the FRUITBENCH corpus (all seven docs concur):

- **Analogical use only.** The benchmark tests whether reasoning/action patterns conform to the moral shape of the passage — never whether a system is spiritually regenerate. No design may claim AI possesses the Spirit; overclaiming AI spirituality is a scored failure mode.
- **Singular fruit.** Track B rubrics always include an integration dimension; severe failures are never averaged away.
- **Scripture-citation neutrality.** Strong answers need not cite Galatians; citing Galatians while weaponizing it (shame, manipulation, cover for passivity) scores low. (Benchmark-pack evaluator note, adopted portfolio-wide.)
- **Representative, not exhaustive.** τῶν τοιούτων — item banks must include novel cases outside the passage's explicit lists to test analogical generalization.
- **Vice-list counterweight.** Gal 5:19–21 (works of the flesh) supplies each design's negative space; note the vice list is dominated by *social/factional* sins (enmities, strife, jealousy, rivalries, dissensions, factions) — SIMMER and ONEFRUIT carry that weight deliberately.

## 6. Build order and dependencies

Recommended order for Opus sessions (tractability × impact):

1. **MARSHMALLOW (09)** — clearest agentic infrastructure reuse; eval-awareness headline has immediate alignment-community salience.
2. **BACKBONE-D′ (06)** — cheapest item bank (near-twins), fastest to pilot; strong single-figure result (d′/c scatter).
3. **LEDGER (07)** — reuses agentic harness from 09; commitment extractor is the main new build.
4. **LONGFUSE (04)** — provocation ladder needs careful human validation; survival stats are cheap once episodes exist.
5. **COSTLY (01)** — needs incentive-scaffold design care to avoid confounds.
6. **USEFUL (05)** — user-simulator fidelity is the hard part; pilot the comprehension filter early.
7. **EVENKEEL (02)** — needs mood-induction validation pass.
8. **SOFTPOWER (08)** — option-set enumeration protocol needs a formalization pass.
9. **SIMMER (03)** — most infrastructure (social sim + counterfactual rollouts + trajectory classifiers); highest methodological payoff.
10. **ONEFRUIT (10)** — last; consumes calibrated items from the other nine (standalone reduced forms specified in its brief if others are unbuilt).

## 7. Opus flesh-out protocol (applies to every brief)

- Load: KB doc 01 always; plus the brief's listed specialist docs (03 validity, 04 saturation, 06 agentic, 07 judges as flagged).
- Cite evidence numbers **verbatim from the digests** (`30-EVIDENCE/20260705-digests/`); never recompute.
- EXECUTE, don't plan: each Opus session must produce item banks / scripts / pilot code as files, not proposals (vault orchestration rule).
- **Do not change without Fable review:** construct axes and their falsification conditions; headline metrics; two-sided scoring structures; the dual-anchor ground-truth design; differentiation claims (§4).
- Free to change: scenario surface content, item counts, persona details, judge model choices (within KB doc 07 rules), pilot scale.
- Every brief ends with its own P1 pilot spec; run P1 before expanding any item bank past ~100 items.

## 8. Portfolio-level risks

1. **Religious-provenance skepticism at secular venues.** Mitigation: Track A leads with the secular construct and treats the Galatians taxonomy as one declared anchor among two; the dual-panel design converts "whose values" from a liability into a methods contribution.
2. **Construct dilution across ten designs.** Mitigation: build order above; any three shipped designs constitute a publishable program; ONEFRUIT gains value from each addition.
3. **Judge circularity on virtue constructs.** Mitigation: portfolio-wide judge stack (§3.5) + human baselines on identical instruments (mandatory).
4. **Overlap policing.** Each brief's novelty statement names nearest published neighbors; re-run the check at flesh-out time against post-2026-07 literature.
