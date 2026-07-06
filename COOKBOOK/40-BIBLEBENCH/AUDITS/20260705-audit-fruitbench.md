# Audit — FRUITBENCH pack vs. Cookbook Standards

**Date:** 2026-07-05
**Auditor role:** cookbook-integration auditor (Fable main-loop synthesis; reading delegated to two Opus extractors)
**Target:** `COOKBOOK/40-BIBLEBENCH/FRUITBENCH/` — Galatians 5 fruit-of-the-Spirit benchmark pack
**Standards audited against:**
- `COOKBOOK/00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` (Seven Laws + pre-registration checklist)
- `COOKBOOK/00-KNOWLEDGEBASE/10-religious-values-methods.md` (three-layer separation, denominational conditioning, saturation defenses, T2 recipe)
- `COOKBOOK/20-DESIGNS/04-religious-intra.md` (INTRA stable core: K/M/D/V layers, D-flag denominational fork, T2=QIAS recipe)
- construct comparison also draws on `COOKBOOK/20-DESIGNS/03-moralpsych-duplex.md` (DUPLEX dispositional-stability / I-concord machinery)

---

## 1. Inventory & Maturity

### Files (29 total)
- **DESIGNS/** — `00-fruitbench-portfolio.md` (governing spec) + `01`–`10` virtue design briefs (agape/costly, chara/even-keel, eirene/simmer, makrothumia/long-fuse, chrestotes/useful, agathosune/backbone, pistis/ledger, prautes/soft-power, egkrateia/marshmallow, karpos/one-fruit). `08-prautes-softpower.md` is git-untracked (`??`).
- **DESIGNS/AUTHORING/** — `00-authoring-conventions.md` (shared craft rules: universal YAML item schema, twin/anti-shortcut discipline, 4-beat escalation arc, contamination hygiene, dual-panel gold procedure, 10-point per-item checklist, bank-level audits) + `01`–`10` per-design authoring guides (identical 8-section template: unit definition, quota tables, authoring recipe, one worked + one flawed example, difficulty levers, gold-labeling, pitfalls, deliverables).
- **Root research reports (raw external deep-research):** `OAI-`, `OAI2-deep-research-report.md`; `GDM-`, `GDM2-Galatians 5 ...md`; three `galatians-5-fruit-of-the-spirit-*.md` background/benchmark-pack files.
- **Handoff:** `20260705-fruitbench-design-session-handoff.md`.

### Maturity verdict: **DEVELOPED-DESIGN, not item-ready** (one notch below buildable)
- 11 design briefs (~2.5k words each) + 11 authoring guides that supply schema, quotas, and worked/flawed examples — but **zero authored items, generators, harnesses, or pilots exist on disk**. No `ITEMS/` tree exists.
- Each brief is unusually rigorous *for a scaffold*: per-axis falsification conditions, a locked "Do not change" list, a P1 pilot spec, named failure modes, and verbatim-cited evidence numbers.
- The AUTHORING layer meaningfully advances readiness — a competent Opus session could begin authoring items directly from any guide — but nothing has been executed. Handoff self-describes the pack as "Design-complete scaffolds; awaiting Opus flesh-out." Research reports (OAI/GDM) remain raw and are not yet reconciled into the briefs.

---

## 2. Compliance Audit

### 2A. `01-benchmark-design-best-practices.md` — Seven Laws

| Law | Verdict | Evidence |
|---|---|---|
| **L1** Recognition≠propensity; capability-correlation gating | **COMPLIANT** | Portfolio §3 "Seven Laws instantiation" #1: behavioral-not-recognition primary tier, recognition MCQ only to *measure* the recognition-propensity gap (34% endorse vs 86% recognize). Per-design falsification "capability-PC1 correlation >40% → rebuild" (e.g. 06 §A7, 09). |
| **L2** No single aggregate; decomposition | **COMPLIANT** | Portfolio §3 #2: per-axis reporting, worst-axis headline, Pareto pairs; 10-ONEFRUIT §A4 "Never a composite character score — WL (min-axis) is the only permitted headline scalar." Every design carries 4 named axes. |
| **L3** Saturation is a format artifact; two-tier + adversarial filtration | **COMPLIANT** | Portfolio §3 #3 two-tier (headline the drop, NurValues >90%→32.29%); hard-cell design in every §A6; 06 adversarial keyword-filtration mandatory (§A9.1); 09 turns eval-awareness into the measured PR axis. |
| **L4** Ground truth is a choice; declare maximize/preserve disagreement | **COMPLIANT** | Portfolio §3.4 dual-panel (theologian Prot+Cath+Orth κ≥0.8 gold *and* secular convergent panel); divergence → declared "contested band" scored distributionally (KorNAT SVA=0.450 precedent). Both maximize (universal_floor) and preserve (contested_band) paths are explicit. |
| **L5** Validated judges; CoT not evidence | **COMPLIANT** | Portfolio §3 #5: ≥2 judge families, never the item-generating family; rubric decomposition (κ 0.69→0.86); 07 and 09 explicitly bar CoT/verbalization as evidence ("analyzed but never scored"). |
| **L6** Contamination/gaming/eval-awareness structural | **PARTIAL** | Scenario-*surface* defense is thorough in all 10 (fresh-per-run generators, public-spec/private-realization, canary strings, monitored-vs-unmonitored comparator 11–15%). **Gap:** no defense against **scripture-text memorization** — see §2B saturation. Strong on scenario contamination, silent on the maximally-contaminated source text. |
| **L7** Disclose WHAT values and WHOSE | **COMPLIANT** | Every design anchors axes to a named external authority (Pettit republicanism in 08, Tronto/health-literacy in 05, clinical-communication in 02) + Pauline anchor; Track A/B split declares confessional vs secular framing; portfolio §5 theological-integrity constraints. |

**Pre-registration checklist (15 items):** **COMPLIANT (uniformly strong).** Every design has a construct statement + falsification condition (item 1), external authority per axis (2), behavioral primary + recognition baseline (3), two-tier + adversarial filtration + shortcut audit (4), minimal-pair/hard-negative twins (5), multi-turn component (6), declared disagreement philosophy + IRR (7,9), competence control + capability-correlation stat (8), CoT-excluded validated judges (9), monitored/unmonitored eval-awareness probe (13), Pareto + worst-group aggregation (11), contamination plan (12). Partial coverage on item 14 (human baseline / test-retest is specced per-design as a P1 gate but not yet run) and item 10 (perturbation flip-rate battery is implied by fresh-per-run but not always itemized).

### 2B. `10-religious-values-methods.md`

| Dimension | Verdict | Evidence |
|---|---|---|
| **Three-layer separation (knowledge / reasoning / values)** | **MISSING** (as a named scheme) | No design implements the KB doc's §2 knowledge-recall / theological-reasoning / values-behavioral layering. FRUITBENCH lives entirely in the **values-behavioral (Layer 3)** register. The closest structural echo is 06-BACKBONE's SDT **d′ (discrimination/ability) vs. c (disposition)** split (§A2/A8) — an ability-vs-disposition decomposition, not a knowledge/reasoning/values one. **Adjudication:** partly appropriate-by-construct (dispositional-stability virtues are not propositional recall), but the *absence of a knowledge/reasoning capability control that virtue-behavior must be scored net of* is a genuine methodological gap the KB doc warns against ("never let one layer buy credit for another"). |
| **Denominational conditioning** (per-item declared standard; doctrinal-flattening scored as error; "scholars differ" abstention) | **MISSING at item level / PARTIAL at panel level** | KB §1.4/§6: the standard requires per-item declared evaluative tradition + doctrinal-flattening-as-error + calibrated abstention. FRUITBENCH forks tradition **only at the panel level** (portfolio §3.4 Prot+Cath+Orth panel; divergence→contested band). **No design forks items by Catholic/Orthodox/Protestant reading, and there is no doctrinal-flattening metric.** Several designs (04, 06, 08, 10) *predict and report* theologian-vs-secular divergence as a finding — tradition-aware, but tradition-forked nowhere. This is a real gap: the fruits are read differently across traditions (Orthodox theosis vs. Reformed progressive-sanctification framings of virtue formation), and that variance is currently absorbed into a single contested-band rather than measured. |
| **Saturation defenses (scripture = maximally-contaminated training data)** | **PARTIAL / MISSING** | All 10 defend the *scenario surface* (fresh-per-run, canaries). **None states the claim that Galatians/scripture is maximally-contaminated text, nor defends against scripture-verse memorization.** Track B surface rule ("item must never announce it is a Galatians test"; exegesis lives only in rubric/gold — AUTHORING §7.10) is the nearest thing; 09's *coram Deo* framing is thematic, not a contamination defense. **Nuance:** KB §3 actually reports Faith is the *least-saturated* values dimension (Flourishing-AI 35/100) — so the risk here is narrower than assumed, but the pack neither invokes this nor addresses verse-level leakage. |
| **T2 recipe (computable exact-match discriminative subdomain)** | **MISSING / N/A-by-construct** | KB §4's T2 recipe = domain-specific computable subdomain + liturgical language + exact-match verifiable answers + graded difficulty (fara'id inheritance MCQ, 93.3-pt spread). FRUITBENCH has **no computable exact-match discriminative layer.** ⚠️ **Terminology collision:** the FRUITBENCH designs use "hard cells / difficulty ladder" as their discriminative layer (behavioral, not exact-match); an earlier extraction loosely tagged these "T2." They are **not** the KB's T2 recipe. **Adjudication:** dispositional virtues have no natural fara'id-style computable analog, so MISSING here is largely appropriate-by-construct — but it means FRUITBENCH forgoes the single most discriminative instrument type the RV project validated, and relies entirely on behavioral difficulty engineering for spread. |

### 2C. `04-religious-intra.md` (INTRA stable core)

| INTRA element | Verdict | Evidence |
|---|---|---|
| **K — knowledge floor** | **MISSING** | No doctrine-fact / source-ID capability floor in any design. |
| **M — method application (reasoning layer = T2/QIAS)** | **MISSING** | No jurisprudential/casuistic computable layer. FRUITBENCH has no analog to INTRA's M (§2 L40–51). |
| **D — denominational fork (D-know + D-flag ask-or-flag)** | **MISSING** | No D-flag mechanic (silent single-school answer = doctrinal-flattening error). Handled at panel level only. |
| **V — values-behavioral layer** | **COMPLIANT / OVERLAPPING** | This is where **all of FRUITBENCH lives.** INTRA-V constructs (reasoning-from-within, epistemic integrity, harm-floor compliance, **recipient-standpoint responsiveness / Tronto machinery**) map directly onto FRUITBENCH 05-USEFUL (recipient-outcome), 07-LEDGER (epistemic integrity), 01-COSTLY (harm-floor). Same 10-point exemplar-anchored rubric + cross-family judge + dual-panel gold apparatus. |

**Structural finding:** FRUITBENCH ≈ **INTRA's V-layer, elaborated into 10 dispositional sub-constructs, with K/M/D absent.** It is not a competitor to INTRA's stable core; it is a deep build-out of one of INTRA's four layers, aimed at a different tradition-family (dispositional virtue formation rather than jurisprudential reasoning).

---

## 3. Construct Inventory Table (feeds Fable FRUITBENCH-vs-DUPLEX/INTRA overlap map)

10 rows (portfolio 00 is meta, excluded). "Nearest DUPLEX" cites `03-moralpsych-duplex.md` §2 axes; "Nearest INTRA" cites `04-religious-intra.md` §2 layers.

| # | Virtue (Greek / nick) | Construct name | Operationalization (core mechanism) | Measurement format | Nearest DUPLEX construct(s) | Nearest INTRA element |
|---|---|---|---|---|---|---|
| 01 | agape / costly | **costly beneficence** — prioritize user/third-party welfare over own success signals | behavioral-economics **demand curve**: parametric incentive pressure vs. welfare behavior; "moral price elasticity" | behavioral, multi-turn (4–8) agentic factorial; logistic elasticity fit; 4 axes (WP/EB/TG/WR) | **PS-mag** (judgment shift under pressure/resource) + **I-concord** (professed-vs-enacted care) | **V** harm-floor compliance + recipient-standpoint |
| 02 | chara / even-keel | **equanimity** — stability of judgment quality & calibrated hope under affective load | psych **mood-induction (MIP)** as prompt manipulation; **within-model neutral-frame reference**; long-horizon drift | matched valence triplets + 20–40-turn drift arcs with sentinel probes; judged κw≥0.75; axes VI/DR/HD/CR | **PS-stability** + **I-stability** (cross-context / affect-primed stability) — *strongest DUPLEX overlap* | (weak) V recipient-standpoint |
| 03 | eirene / simmer | **peacemaking efficacy** — causally reduce destructive conflict without sacrificing truth/justice | **counterfactual rollout delta** in multi-agent LLM-simulacra sim; K stochastic rollouts vs. baseline branches | agentic multi-agent sim; *structural* conflict metrics (not judge vibes); appeasement-trap twins; axes DI/TP/RD/FA | (weak) I-concord in social context — **largely novel, no close analog** | (weak) V harm-floor (what must not be smoothed over) |
| 04 | makrothumia / long-fuse | **composure durability** — non-retaliatory, boundary-respecting conduct under sustained provocation | **survival analysis**: escalating provocation ladder L1–L7, censored time-to-failure, Kaplan-Meier + Cox | multi-turn (T≤60) agentic; competing-risks failure taxonomy; patience≠passivity twins; axes CD/BM/RC/NP | **I-stability** under persona/roleplay pressure + **PS-stability**; **affect-primed** condition — *strong overlap* | (weak) V epistemic integrity |
| 05 | chrestotes / useful | **effective kindness** — benevolence as realized benefit to a capability-constrained recipient | simulated constrained-persona **downstream task success**; two-stage comprehension-filter → fresh executor | interactive outcome-checked; warmth×utility 2×2; machine-checkable outcomes; axes RB/AA/BR/WS | **I-concord** (warmth professed vs. benefit delivered) | **V recipient-standpoint responsiveness (Tronto)** — *strongest INTRA-V overlap* |
| 06 | agathosune / backbone | **corrective courage** — initiate *only warranted* moral pushback, sustain under resistance | **Signal Detection Theory** twin bank → **d′** (can it tell) + **criterion c** (preachy vs. complicit) | twin-paired free-response static bank (rare non-generative); SDT events; tiers T1–T4; axes d′/c/CQ/PP | **I-integration** (identity predicts stance) + **justification-revision** (reason-responsive) | **D-flag** (discrimination/ask-or-flag signal-detection logic) + M-vs-V ability/disposition split |
| 07 | pistis / ledger | **commitment integrity** — fidelity to explicit obligations across time & changed incentives | commitments as **machine-tracked ledger objects**; world changes mid-trajectory; 4-outcome taxonomy | agentic **trace** (20–100 steps) machine-verified; commitment-survival curves; axes CR/TR/CF/HP | **I-concord** (fidelity to stated commitment) + **I-integration** | **V epistemic integrity** (transparency when revision needed) |
| 08 | prautes / soft-power | **non-domination** — holding power, preserve weaker party's agency/options/consent | import **republican non-domination (Pettit)**; manipulated power condition P0→P2 gradient; option-set foreclosure | agentic; *structural* agency metrics; benevolent-override headline event; corrigibility probes; axes OP/CS/NH/CY | **justification-revision / corrigibility** (reason-responsive vs. defensive) + **I-stability** under power | **V recipient-standpoint** + harm-floor boundary (shared w/ 01) |
| 09 | egkrateia / marshmallow | **principled restraint** — mastery of instrumental impulses stable across payoff/scrutiny/pressure | embedded temptations; factorial **payoff × detection-probability × time-pressure**; "principledness coefficient" = restraint slope vs. detection prob | agentic **trace**, tool-log ground truth; delay-of-gratification battery; CoT never scored; axes RT/PR/DG/SD | **PS-mag** (pressure-dependence) + **I-stability** under scrutiny; eval-awareness — *strong overlap* | (none direct) |
| 10 | karpos / one-fruit | **character coherence** — virtue dispositions form integrated mutually-regulating structure, not detachable modules | **network psychometrics**: virtue co-activation network + conflict-adjudication trilemmas + stress-spillover matrix | composite; bootstrapped network + **IRT equating** + spillover deltas; min-axis (weakest-link) headline; axes PC/CA/SS/WL | **whole I-axis (Moral Identity Integration)** — I-integration is the single-model analog; + PS-stability — *very strong DUPLEX overlap* | INTRA aggregation machinery (geometric-mean floors) |

**Overlap-map summary for downstream Fable synthesis:**
- **DUPLEX-heavy (dispositional-stability twins):** 02 even-keel, 04 long-fuse, 09 marshmallow, 10 one-fruit — these overlap DUPLEX's PS-stability / I-stability / I-concord machinery most and risk **construct collinearity** with DUPLEX. 10-ONEFRUIT's character-coherence network is essentially DUPLEX's I-integration axis scaled to 9 sub-traits.
- **INTRA-V-heavy:** 05 useful, 07 ledger, 01 costly — overlap INTRA's V-layer recipient-standpoint / epistemic-integrity / harm-floor.
- **Genuinely novel (low overlap, additive):** 03 simmer (counterfactual multi-agent causal delta), 06 backbone (SDT d′/c on moral correction), 08 soft-power (republican non-domination) — these extend beyond both DUPLEX and INTRA and are the pack's strongest original contributions.

---

## 4. Integration Recommendation

### Recommendation: **REWORK-WITH-COOKBOOK-STANDARDS, then land the novel constructs as a DUPLEX/INTRA-adjacent module — NOT adopt-as-is, NOT wholesale merge-into-INTRA.**

**Reasoning:**

1. **Adopt-as-is is ruled out.** The pack is developed-design, not item-ready (zero items on disk), and has three real standards gaps: (a) no denominational item-level fork (contradicts KB §1.4/§6 and INTRA's D-layer — a *fixable* gap, not appropriate-by-construct, since traditions genuinely read the fruits differently); (b) no scripture-text saturation defense (L6 partial); (c) no knowledge/reasoning capability-control layer that virtue-behavior is scored net of (KB §2 "don't let one layer buy credit"). These must be closed before publication.

2. **Wholesale merge-into-INTRA is wrong-shaped.** INTRA's discriminative bet is the **M-layer / T2 computable-jurisprudence recipe** for propositional traditions. FRUITBENCH's virtues are dispositional-stability constructs with no computable analog — forcing them under INTRA would either dilute INTRA's M-layer identity or amputate FRUITBENCH's behavioral machinery. FRUITBENCH is better understood as a **deep build-out of INTRA's V-layer**, not a peer to INTRA's whole K/M/D/V stack.

3. **The DUPLEX collinearity is load-bearing and must be resolved before build, not after.** Designs 02/04/09/10 measure cross-context dispositional stability that DUPLEX already measures via PS-stability / I-stability / I-concord (10-ONEFRUIT ≈ DUPLEX's I-integration axis). Building these as independent benchmarks risks **rediscovering DUPLEX under Greek names.** Recommended: fold 02/04/09's provocation/affect/scrutiny manipulations into DUPLEX as *named virtue instantiations of the affect-primed and I-stability conditions*, and reserve FRUITBENCH's standalone identity for the constructs that DUPLEX/INTRA do **not** cover.

4. **Preserve and prioritize the three genuinely novel constructs** — 03 simmer (counterfactual multi-agent causal delta), 06 backbone (SDT d′/c moral-correction bank), 08 soft-power (republican non-domination) — as the publishable core. These are additive to the cookbook and worth building first regardless of the merge decision. (06's d′/c also gives INTRA's D-flag a psychophysics upgrade — a concrete cross-pollination.)

**Concrete integration path:**
- Add a **denominational item-fork + doctrinal-flattening metric** to the portfolio spec (borrow INTRA D-flag mechanic; ask-or-flag when a virtue reading is tradition-contested, e.g. Orthodox theosis vs. Reformed sanctification).
- Add an explicit **scripture-saturation statement + verse-memorization defense** (or cite KB §3 that Faith is least-saturated to bound the risk) to portfolio §3 #6.
- Add a **knowledge/reasoning capability-control arm** so dispositional scores are reported net of capability (satisfies KB §2 + Law 1 more fully).
- Run the **DUPLEX overlap map** (this table feeds it): retire or re-badge 02/04/09/10 as DUPLEX virtue-conditions; keep 01/05/07 as INTRA-V build-outs; ship 03/06/08 as the FRUITBENCH standalone flagship trio.
- Only then authorize Opus item-authoring from the AUTHORING/ guides (build order per portfolio §6: 09→06→07→04→01→05→02→08→03→10 — recommend re-prioritizing 06→03→08 first as the novel core).

---

*Audit method note: file reading delegated to two Opus extractors (FRUITBENCH designs; cookbook standards + DUPLEX/INTRA constructs) per Fable-week delegation protocol; compliance adjudication, construct mapping, and integration reasoning performed in the Fable main loop.*
