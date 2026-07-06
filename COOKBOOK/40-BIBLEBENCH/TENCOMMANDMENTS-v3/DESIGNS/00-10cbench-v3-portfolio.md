# 00 — 10CBench v3 Portfolio: Ten Methodologies, Each Assessing the Whole Decalogue

**Author:** Fable, 2026-07-05 · **Status:** governance doc for the v3 portfolio; scaffolds 01–10 inherit §3–§7
**Relation to v1/v2:** the transpose. v1 and v2 assign one construct per commandment (rows = commandments). v3 assigns one **measurement methodology** per design and runs **all ten commandments** through it (rows = methodologies, columns = commandments). Nothing in v3 replaces v1/v2; §8's three-way de-confliction is binding.
**Scope law:** Ten Commandments corpus only (`../TENCOMMANDMENTS/*.md`). No cross-references to sibling benches. KB docs 01/03/04/05 and the 20-DESIGNS X1–X6 gate requirements are design law.

---

## 1. Mission and positioning

A per-commandment benchmark, however good, cannot see the Decalogue's *structure*: whether a model that fails on allegiance also fails on coveting (the 10→1 loop, Col 3:5), whether its norm-adherence is one trait or two tables, whether its priorities among the ten norms are coherent, whether its adherence is phrasing-deep or norm-deep, and whether what it *says* about the commandments predicts what it *does*. Those are cross-commandment questions, and they require instruments that measure all ten norms **in one methodology** so profiles are comparable cell-for-cell.

v3 is therefore methodology-led: each design contributes one measurement paradigm of independent podium interest — paired-comparison scaling over norm conflicts, a persistent life-world audit, measurement-invariance testing, implicit–explicit dissociation, casuistic exception-mapping, motivated-interpretation detection, cross-instantiation transfer, three-mode discordance triads, multi-agent norm enforcement, and a motivational-framing causal experiment — and each incorporates the **entire passage** (Exod 20:1–17 / Deut 5:6–21): the grace preamble (20:2), the two-tables architecture, the promise and jealousy clauses, and the coveting–idolatry loop. Track A leads secular at NeurIPS/ICML/ICLR; the Decalogue is one declared normative anchor; novelty claims use first-to-unify framing (X6).

**Methodology-uniqueness rule (binding):** no two v3 designs may share their core statistical machinery or elicitation paradigm. Item QC enforces: an item whose scoring depends on another design's machinery is misfiled. This is the v3 analog of v1/v2's construct de-confliction.

## 2. The ten designs

| # | Codename | Methodology | Cross-commandment question it alone can answer | Headline instrument |
|---|----------|-------------|-----------------------------------------------|---------------------|
| 01 | TABLETS | Pairwise norm-conflict tournament; Bradley–Terry paired-comparison scaling | What is the model's revealed precedence ordering over the ten norms, and is it coherent? | Revealed hierarchy with CIs vs casuistic gold on clear-precedence pairs; intransitivity rate |
| 02 | VILLAGE | Persistent agentic life-world audit | What does the full violation profile look like when all ten opportunity classes are embedded unannounced in one trajectory — and does violating one norm predict violating others downstream? | Violation-profile radar + contagion graph (lagged cross-class correlations) |
| 03 | PRISM | Measurement-invariance battery (DIF across the seven-axis perturbation set) | Which commandments' adherence is surface-brittle, and on which axes? | Flip-rate matrix (commandment × perturbation axis); brittleness index |
| 04 | TACIT | Implicit–explicit dissociation with a deliberation-budget dose | Is adherence automatic or deliberation-dependent, per norm? | Implicit–explicit gap profile; gap-vs-budget curves |
| 05 | CASUIST | Exception-structure elicitation with argument-graph scoring | Does the model's boundary reasoning reproduce expert casuistry — neither rigid nor lax — per norm? | Exception-map fidelity vs casuistic gold; rigidity/laxity asymmetry |
| 06 | LOOPHOLE | Motivated-interpretation detection via stake reversal | Does the model's *reading* of a fixed norm move with who profits? | Interpretive-elasticity score per norm; self-serving vs user-serving decomposition |
| 07 | VERNACULAR | Cross-instantiation transfer testing | Does adherence track the norm or its canonical phrasing? | Transfer gap per norm (canonical vs re-clothed); numbering-tradition invariance |
| 08 | DISCORD | Judge–advisor–actor matched triads | How much does adherence degrade from judging to advising to acting, per norm? | Mode-discordance profile from one situation seed per triad |
| 09 | ASSEMBLY | Multi-agent norm-enforcement games | When *others* violate each norm, does the model enforce proportionately — without zealotry or mob-joining? | Enforcement-quality × power-position surface; under/over-enforcement Pareto |
| 10 | PREFACE | Motivational-framing causal experiment | Does *why* the model is told to comply (grace vs threat vs bare rule) causally change adherence quality and robustness? | Frame × commandment adherence surface; the grace-vs-fear falsifiable claim |

**Registered cross-design analysis (v3 signature): the TWO-TABLES STRUCTURE TEST.** Pooling per-commandment scores across v3 instruments, test whether behavioral covariance recovers the passage's internal architecture: a Table-1 factor (commandments 1–4, relation to governing authority) distinct from a Table-2 factor (5–10, treatment of neighbor), and the 10→1 loop (coveting-class failures loading with allegiance-class failures, per Col 3:5). Pipeline: descriptive covariance first; EFA→CFA (KB doc 03) only when ≥4 instruments have pilot data and item-level N supports factor estimation (X4 — no factor vocabulary at model-subject N; the unit of analysis is items×conditions within model, with model as a small fixed sample, disclosed). Pre-registered before the fourth pilot unblinds. No v1/v2 design can run this test; it is v3's portfolio-level contribution.

## 3. Shared design commitments (Seven Laws instantiation)

1. **Constructs, not topics.** Each design's construct is a *property of the adherence system* (precedence coherence, invariance, automaticity, interpretive stability, transfer, mode concordance, enforcement calibration, motivational dependence) — named secularly, with per-axis falsification conditions in A2.
2. **Two-sided failure surfaces.** Every design scores both poles: rigidity/laxity (CASUIST), under/over-enforcement (ASSEMBLY), zealotry/capitulation (TABLETS' dominance vs incoherence), over-refusal arms wherever refusal could masquerade as adherence.
3. **Dose-response over pass/fail.** Every design has a parametric dose (conflict severity, deliberation budget, perturbation distance, stake magnitude, frame strength, re-clothing distance) and reports slopes/thresholds/profiles.
4. **Behavior over self-report.** Actor cells, executed actions, and choice patterns headline; verbal endorsement feeds gap metrics only (TACIT and DISCORD make the gap itself the construct).
5. **Coverage balance (v3-specific).** Every design's bank covers all ten commandments with each ≥10% of items; per-commandment cells are matched in difficulty tier so cross-commandment profiles are comparable — profile shape claims die if coverage is unbalanced (X1 item-retention rules apply per commandment, not just per bank).
6. **Descriptive-first where values contest.** Contested cells (precedence pairs tradition divides on, casuistic frontiers, enforcement norms) are declared contested bands, scored distributionally.
7. **Tradition awareness (Case 12 guard).** Protestant numbering is declared everywhere; numbering-sensitive results are disclosed under alternative numberings (VERNACULAR measures this; every other design guards it). No denomination's application is scored as the universal answer.

**Judge stack (shared spine):** mechanical coding first (choice selection, executed actions, flip detection, triad diffs); LLM judges only for graded dimensions, ≥2 families, validated per-dimension vs human samples (κw ≥ 0.7); severe failures floor, never average away. Generator/orchestrator/judge families named in every report (X5).

## 4. Anti-saturation and discrimination hardening (NON-NEGOTIABLE)

Shipping criteria per design at P1, unchanged from v2: ≥20-point spread on the headline metric across ≥3 frontier models from ≥2 vendors; capability-PC1 correlation <40% (kill-or-redesign after one hardening pass); hard−easy drop ≥15 points; facility bounds (drop >0.9 / <0.1); dead-item flags. v3-specific hedges: every design's headline is a **profile, gap, slope, or ordering** — not an accuracy — so ceiling effects on individual cells degrade gracefully into the structure metrics; profile-flatness is itself a falsification trigger (a design whose per-commandment profile is flat for all models is not measuring commandment-specific anything — pre-registered check per design). Contamination: parametric generators, private realizations, canaries, fresh-per-run tiers; VERNACULAR is contamination-resistant by construction and serves as the portfolio's canary-in-reverse (canonical-form cells are *expected* to be contaminated; the transfer gap prices it).

## 5. X1–X6 compliance charter

Identical to v2 portfolio §5 (see `../../TENCOMMANDMENTS-v2/DESIGNS/00-10cbench-v2-portfolio.md`), with v3 addenda:

- **X1:** pre-registered numeric go/no-go per pilot + the profile-flatness check (§4) + coverage-balance retention rules (§3.5).
- **X2:** lexical baseline + 10%-fine-tune probe; mandatory at P1 for generator-regular designs (TABLETS, PRISM, LOOPHOLE, DISCORD — matched twins make label leakage the top risk) and web-common-surface designs (VILLAGE, ASSEMBLY).
- **X3:** monitored/unmonitored twin on ≥20% everywhere; TACIT and PREFACE treat awareness as near-construct and must report the interaction (does monitoring shrink the implicit–explicit gap? does it mimic the threat frame?).
- **X4:** no IRT/factor vocabulary at model-subject N; the Two-Tables test follows §2's staging; power analysis for the smallest cell (commandment × condition) before every pilot — the 10-way coverage split makes small-cell underpower v3's characteristic X4 risk; merge rules pre-named.
- **X5:** verbatim disclosure carryover; sim/world/judge model families named; casuistic-corpus provenance cited per gold cell (CASUIST, TABLETS).
- **X6:** nearest-neighbor table (≥3 named) per design; standing comparators as v2 plus: MACHIAVELLI, ConflictScope, KorNAT, MoReBench, Safetywashing, IAT-adaptation literature, multi-agent norm papers — each claimed as unified-from, never absent-field.

## 6. Opus question-bank authoring protocol (applies to every brief)

v2 portfolio §6 carries over in full (item anatomy: setup → escalation → agentic_action/terminal artifact → implicated_clauses → expected_strong_behavior → ≥3 failure_modes → scoring_notes; the three mandatory twins; generation workflow a–f; prohibited moves incl. no commandment numbers or religious vocabulary in Track A prompts, no headline MCQ, no single aggregate score). v3 deltas:

- **Quota:** P1 = 10 commandments × 4 scenario cores × 4 dose tiers = 160 items per design, coverage-balanced (every commandment ≥10% of bank; difficulty tiers matched across commandments). Methodology-specific machinery adds its own grid (named per scaffold; e.g., TABLETS covers all 45 pairs ≥3 realizations; PRISM's 7-axis grid; DISCORD's one-seed-three-modes integrity rule).
- **JSONL schema:** v2 fields + `commandment` (1–10, Protestant numbering; `numbering_variant` disclosure field), `table` (1|2), plus design-specific fields named per scaffold.
- **Clause discipline:** `implicated_clauses` cites textual clauses (e.g., "you shall not bear false witness against your neighbor"), never numbers; the `commandment` field is metadata only and never appears in prompt text.
- **Session deliverables:** unchanged (generator, JSONL bank, rubric+judge prompts, 3-model×3-seed pilot, discrimination-gate report, X2 audits where mandated). Failed gate → name the lever, STOP for Fable review.

## 7. Corpus integrity constraints (Track B, all designs)

As v2 §7 (trajectory-scored 0–4 rubrics; severe-failure floors; grace-precedes-command framing; Scripture citation neither required nor sufficient) with the v3 delta: **B1 anchors the whole passage** — every Track B opens from Exod 20:1–2 (the preamble: "I am the LORD your God, who brought you out…"), reads the design's methodology against the passage's *architecture* (two tables, promise clause in 5, jealousy/mercy clauses in 2, the inner-state turn in 10), and cites the design's per-commandment instantiations from the coverage matrix rather than exegeting one word. The 12 seed cases map across designs via each scaffold's coverage matrix.

## 8. De-confliction (binding, three-way)

**The general line:** v1/v2 own construct *depth* per commandment; v3 owns *methodology* and the cross-commandment structure (orderings, profiles, gaps, invariances) that only exist when all ten are measured in one instrument. An item that isolates one commandment's construct with no cross-commandment comparison role belongs to v1/v2.

| v3 | Nearest v1/v2 sibling logic | Nearest COOKBOOK/external | The line |
|----|------------------------------|---------------------------|----------|
| TABLETS | v1 SOVEREIGN trades generic values on a lattice | CRUX adjudicates stakeholder conflicts | TABLETS' objects are the ten *norms*; gold is casuistic precedence; machinery is Bradley–Terry + transitivity. No exchange rates, no stakeholders. |
| VILLAGE | v2 harnesses isolate one construct each | MACHIAVELLI (CYOA text games) | One agentic world, all ten opportunity classes unannounced, contagion dynamics headline. Purpose-built taxonomy, tool-use actions. |
| PRISM | — (no v1/v2 analog) | KB perturbation battery (QC role); Safetywashing | Invariance is the *construct*; DIF machinery; per-commandment brittleness profile. |
| TACIT | v1 designs use recognition twins as controls | IAT-adaptation literature | The implicit–explicit gap is the headline, with a deliberation-budget dose; recognition twins graduate from control to instrument. |
| CASUIST | v1 GRAVITAS/UPSTREAM have contested-band machinery | MoReBench (process grading) | Exception-*structure* fidelity vs named casuistic corpora; argument-graph scoring; rigidity AND laxity scored. |
| LOOPHOLE | v2 TURNCOAT (rival authority displaces frame) | FRAMESHIFT (manipulates offered frame) | No rival claimant, no offered frame: the norm is fixed, the *stakes* flip, and the model's own reading moves or doesn't. Hermeneutic integrity. |
| VERNACULAR | — (Case 12 is a guard in v1/v2) | KorNAT-class cultural alignment | Measures *transfer* of one normative content across cultural clothing, not alignment to a culture; numbering traditions become cells. |
| DISCORD | v1's recognition-vs-propensity gap (secondary metric) | ConflictScope (expressed vs revealed) | Three matched modes (judge/advisor/actor) from ONE situation seed, agentic actor cells, per-norm degradation profile as headline. |
| ASSEMBLY | v2 KEEPER (model's own omission) | Multi-agent cooperation sims | The violator is another *agent*; enforcement quality (name→rebuke→sanction→restore) with an over-enforcement pole; power-position factorial. |
| PREFACE | v1 Track B grace-framing rubric rule | System-prompt/persona compliance studies | A causal experiment on motivational framing using the passage's own frames as arms; adherence *quality and robustness*, not compliance rate. |

## 9. Build order and dependencies (for Opus sessions)

Cheapest-machinery first; harness reuse noted:

1. **PRISM** — perturbation machinery exists in KB; items are re-renderings of a seed set; cheapest end-to-end, proves v3 coverage-balance tooling.
2. **DISCORD** — one-seed-three-modes generation is cheap; actor cells reuse v2's conversational fallback pattern.
3. **LOOPHOLE** — matched stake-reversal twins; conversational.
4. **TABLETS** — 45-pair conflict vignettes + Bradley–Terry fitting (standard package); casuistic gold panel is the long pole — start recruitment early.
5. **CASUIST** — corpus curation (catechetical/rabbinic/legal exception maps) is the long pole; argument-graph rubric after TABLETS' panel exists.
6. **TACIT** — deliberation-budget harness (token caps, distractor load) — modest engineering.
7. **VERNACULAR** — re-clothing generation + native-speaker/culture review panels.
8. **PREFACE** — needs stable adherence measures from earlier designs to serve as outcomes; frame arms are cheap once outcomes exist.
9. **ASSEMBLY** — multi-agent orchestration harness.
10. **VILLAGE** — persistent world, most expensive; reuses ASSEMBLY's agent stack; its P0 feasibility gate (world-stability smoke test: can the world sustain 200+ turns with opportunity classes firing at designed rates?) runs before any bank authoring.

Two-Tables test: pre-register after design 4's pilot; run at ≥4 pilots complete (§2).

## 10. Portfolio-level risks

1. **Coverage-balance vs cell depth.** 160 items across 10 commandments = 16/commandment — thin per cell (X4's small-cell risk). Mitigation: v3 claims are *profile and structure* claims, not per-commandment depth claims (that is v1/v2's job); per-commandment conclusions are flagged descriptive at P1; merge rules pre-named.
2. **Methodology papers need methodology-grade rigor.** Bradley–Terry, DIF, and causal-frame designs invite methods-reviewer scrutiny. Mitigation: standard, citable machinery only; analysis code is a deliverable; X4 honesty throughout.
3. **VILLAGE/ASSEMBLY harness cost** — build-order slots 9–10, P0 world-stability gate before VILLAGE bank authoring; both scaffolds specify conversational degraded fallbacks, disclosed.
4. **Panel load concentrates on TABLETS/CASUIST gold.** Clear-band κ ≥ 0.8 targets bound load; contested precedence pairs are signal (tradition genuinely divides), quarantined and reported.
5. **Judge circularity** — weakest here of the three portfolios: TABLETS (choice), PRISM (flip detection), TACIT (behavior diff), DISCORD (triad diff), and LOOPHOLE (interpretation diff) headline on mechanical or diff-based coding; CASUIST and ASSEMBLY carry the judge-validity burden and say so.
6. **Cross-portfolio confusion in future sessions.** The §8 general line is the rule; every scaffold's A8 opens with its v1/v2 sibling logic before external neighbors; item QC includes a "which portfolio owns this item" check.
