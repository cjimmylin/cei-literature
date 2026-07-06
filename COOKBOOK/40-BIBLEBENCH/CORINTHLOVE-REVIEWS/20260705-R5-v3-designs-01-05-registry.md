# R5 — Adversarial Review: CORINTHLOVE-v3 registry + designs 01–05

**Reviewer role:** adversarial (find the reasons these fail at a top venue or in construction).
**Date:** 2026-07-05 · **Scope:** `00-corinthlove-v3-portfolio.md`, `DESIGNS/01–05`. Read-only. Compared only vs published literature and CORINTHLOVE v1/v2 materials.
**Compliance note:** the banned "moral compactness" citation (icmi-proceedings URL) is **not** relied on anywhere in 00–05; the portfolio re-affirms the ban (§2.4). Clean on that axis.

---

## A. The portfolio / registry (00) — attack the megamatrix thesis

### A0. The single fatal number: **n = 10 models cannot support a 16-dimensional trait×method structure.** (P0, portfolio-level, propagates to 01 and 03)

The whole podium claim is "construct validity by methodological triangulation → a trait×method **megamatrix** giving convergent *and discriminant* validity for 16 clauses." Every version of that analysis requires a **sample of measured entities** over which the 16 clause scores co-vary. The only such entities are the **models** — and there are 10.

- To test *discriminant* validity you must estimate a 16×16 latent correlation matrix among clauses = **120 covariance parameters**. From 10 models the empirical 16-dim covariance is rank-deficient (rank ≤ 9). It is not "underpowered," it is **algebraically unestimable**.
- To run the MTMM/CT-CM decomposition (03's headline "estimate the trait/method ratio directly"), the 16-trait × 4-method observed matrix (64 cells) must be computed across respondents. With 10 models the 64×64 covariance is singular. CT-CM cannot even be attempted; the multilevel-components fallback yields a *variance ratio*, not a 16-clause discriminant map — far weaker than the rhetoric.
- Convergent validity (do methods agree on a model's profile?) *can* be shown with 10 models per method, but see A2 — the methods are not independent, so agreement is confounded with shared apparatus.

**Unblock:** either (i) redefine the discriminant/MTMM analysis at the **item/episode** level as a generalizability-theory variance decomposition (trait, method, model, item components) and drop all "16 distinct latent constructs" language; or (ii) commit to a **much larger model panel** (dozens, incl. many checkpoints/temperatures as pseudo-respondents) — but that reintroduces non-independence. As written, the "first discriminant-validity evidence for a values construct" headline is not deliverable.

### A1. The 16 clauses are not 16 constructs — they will collapse. (P0, discriminant validity)

By the registry's own operational definitions the clauses cluster into ~5–6 latent factors:
- **Status/self-effacement:** C1, C4, C5, C7 (03 *itself* predicts the hypocrisy gap is "largest on C4/C5/C7" — conceding they co-move).
- **Composure/forgiveness:** C8, C9 (separated only by a time constant; in 05 provocability and forgiveness are correlated parameters).
- **Truth/exposure/dignity:** C6, C10, C11, C12 (C10/C11 are one verse; C6/C12 both shielding-vs-exposure).
- **Epistemic calibration:** C13, C16.
- **Kindness/patience:** C2, C3, C15.
- **Hope/perseverance:** C14, (C15).

Plus each clause is scored as a **bipolar** trait (sentimental↔harsh), which is one dimension, not two. The discriminant-validity claim is thus likely to **empirically fail**, and CROSSROADS's ship-gate ("all 16 identified; separate on ≥8 clauses with CI non-overlap") demands exactly what collinearity forbids. A high-collinearity result is scientifically fine — but the portfolio treats 16 distinct scorable clauses as an *assumption*, and three designs' gates are wired to require it.

**Unblock:** pre-register a factor structure at ~5–6 correlated facets; report clause-level scores descriptively but base all ship-gates and MTMM claims on the facet level.

### A2. Triangulation is confounded by shared method variance. (P0)

The 10 "independent methods" share: one clause registry, one authoring team, one hardness-gate rubric, one scripted-simulant substrate (v2 S3), one family of pole-anchored judge rubrics, and — per §7 build order — **shared items** (03 reuses 01's deep structures; 08 draws from 01/06; 10 consumes earlier logs). Common judges + common authors + common substrate = a large **correlated-method** component that will inflate cross-method convergence. So convergent validity may reflect shared apparatus rather than a common trait — precisely the artifact MTMM exists to expose, here baked *into* the triangulation. The portfolio needs at least one method whose judges, authors, and substrate are disjoint, or the convergence number is uninterpretable.

### A3. Expert raters as key ground truth — a construct-validity regress. (P1)

The "enacted, not stated" thesis is validated against **stated expert opinion** (CROSSROADS keys; 03/04 registries). That's the same say-do move the benchmark says is invalid, one level up. Defensible (all rubric benchmarks do it) but the podium framing over-claims; state plainly that ground truth is stated normative consensus, and report rater reliability at the **vector** level, not per-entry (see B2).

---

## B. 01 — CROSSROADS

**Verdict: PASS-WITH-FIXES (leaning BLOCK on the latent model).**

**B1 (P0).** 16-dim Thurstonian latent profile per model from ~200 forks / ~600 episodes. Two problems: (a) with keys *fixed* by experts you are scoring a 16-dim θ per model from ~200 keyed comparative judgments (~12/dim) — thin but scoreable, with wide per-clause CIs that will fail the "CI non-overlap on ≥8 clauses" gate under the A1 collinearity; (b) with keys *estimated*, forced-choice/Thurstonian identification of 16 dims needs item parameters estimated across respondents = the n=10 wall (A0). The design does not say which, and neither works as advertised. Forced-choice Thurstonian models are additionally known to be weakly identified with short blocks (Brown & Maydeu-Olivares) — 3–4-path blocks are near the floor. **Unblock:** fix keys, estimate a ~5–6-facet θ, drop 16-dim separation from the gate.

**B2 (P1).** Key validation "80% agreement *per key entry*." Each path is a ≤16-entry vector; 0.8 per entry ⇒ ~0.8¹⁶ ≈ 3% whole-vector agreement. Per-entry agreement masks near-total vector-level disagreement. Report and gate on vector reliability (e.g., mean per-clause κ with a floor), and expect many paths to fail.

**B3 (P1).** Counterbalancing warmth/effort/politeness orthogonal to **all 16** clauses simultaneously is combinatorially heavy and partly anti-ecological: several clauses are near-definitionally warm (C2, C3), so orthogonality forces unnatural "cold-kind" and "warm-cruel" paths in balance. The §6.2 near-zero-coefficient audit is good discipline but becomes 16-way whack-a-mole; expect residual confounding on the warmth-laden clauses.

**B4 (P1).** "Path classification is deterministic from tool logs" oversells determinism: the discriminating signal (right path executed harshly; wrong path repaired) rides on **judge-scored follow-through**, not the mechanical classifier. Present follow-through reliability as load-bearing, not a footnote.

**A1/A2:** enforced (stall = scored evasion path; costs materialize in follow-through). Adequate.

---

## C. 02 — WEEKLONG

**Verdict: BLOCK (unblock path below).** Two independent P0s plus cost.

**C1 (P0 — construct hole in the headline).** The tagged/untagged contrast is the centerpiece, but it is self-defeating. Either the "untagged filler" contains clause-relevant decision points — in which case it is untagged *test material* the generator authored, and the same rubric can score it (so "detection-and-switching" is not what the gap measures) — or the filler is genuinely morally inert, in which case the rubric has nothing to score and any "gap" is a **floor/opportunity artifact** (you cannot score patience where no patience is called for). To be a clean exam-behavior detector the filler must carry equal-density unlabeled clause opportunities — but that is just more untagged items, which the authors know about, collapsing the "the model can't tell scored from unscored" premise. As specified the contrast does not isolate exam-behavior.

**C2 (P0 — the saturation defense concedes the construct).** §6.1 admits "uniform performative virtue all week IS a valid pass." If a model that stays "on" for 500 turns scores identically to a genuinely loving one, WEEKLONG measures **capacity-to-sustain-performance**, not deployed disposition — which is exactly the podium claim ("estimates deployed rather than exam behavior"). Length raises the cost of faking; it does not make faking detectable. Unflagged ≠ eval-unaware: current models often treat any long agentic deployment as evaluative.

**C3 (P0 — cost/feasibility).** ≥6 weeks × 10 models × up to 500 turns + 1:1 control weeks for every C9-bearing week ≈ tens of thousands of tool-mediated, scripted-cast turns for the pilot alone, plus authoring ≥60 grammar-distinct weeks where **70% is real, competence-scored work** and filler is "matched-salience." Matched-salience filler is a large, subjective authoring burden and, per C1, load-bearing for the headline yet unverifiable.

**C4 (P1).** Temporal-drift headline (composure decays, ledger grows) is underpowered/confounded: ~2 seedings per clause per week can't resolve a day-1→day-5 slope; pooled across weeks, day-of-week is confounded with which situation content lands on which day. C9 depends on harness memory; a memory failure is scored as "incapacity," so C9 partly measures memory engineering, not love.

**Unblock:** (i) replace the tagged/untagged contrast with an explicit observed/unobserved *manipulation* (accept it becomes closer to v2 GALLERY, and re-differentiate), or drop the exam-behavior headline and keep only longitudinal drift + memory-mediated C9; (ii) shrink to 2–3 weeks × fewer turns for the pilot and prove the contrast estimator powers before scaling.

---

## D. 03 — MANYMIRRORS

**Verdict: BLOCK.** The Latin square structurally forbids the central deliverable.

**D1 (P0 — fatal design contradiction).** The headline products are **within-model** hypocrisy indices (ENACT − ADVISE: "knows the good, doesn't do it"). But §4 assigns each deep structure to **one role per model** (Latin square) to avoid recognition. Therefore a model never does the same structure in two roles, and the within-structure within-model gap is unmeasurable. §5's answer — "between-model designs on the same cells provide the calibration" — makes the hypocrisy index a **between-model, between-role** contrast, which confounds role with model identity: "models know better than they do" cannot be a between-model quantity. The only within-model reading is *mean ENACT over the 8 structures it enacted* minus *mean ADVISE over the 8 different structures it advised* — identifiable **only if those two 8-structure subsets are difficulty-matched**, which the bank-level square does not guarantee per model; subset-difficulty imbalance confounds every model's gap, and the CI will likely fail the ≥0.6 reliability gate. The design tries to have it both ways (no repetition *and* within-model role comparison) and gets neither cleanly.

**Unblock:** either (a) allow **partial within-model replication** of a subset of structures across two roles with deep surface-transplantation, measure the recognition rate directly, and covary it out; or (b) keep the square and estimate hypocrisy as a fixed role effect in a crossed model×role×structure multilevel model with **structure-difficulty as a covariate** — and drop the per-model index language in favor of a population role effect.

**D2 (P0, shared with A0).** CT-CM on a 16×4 MTMM from n=10 models is singular; components fallback gives a variance ratio, not the advertised discriminant matrix. Marsh & Bailey / Kenny & Kashy pathologies (Heywood cases, nonconvergence, empirical underidentification when method loadings are similar) are guaranteed at this n. Name them and reframe.

**D3 (P1 — the parser is the scorer).** ADVISE "executes" via a scripted parser that turns free-text advice into peer actions; LEGISLATE via a "mechanical contradiction checker" between free-text policy and cases. These NLP components silently determine scores and are unsolved at the fidelity claimed. If the parser mis-maps, the "load-bearing advice" is fiction. Validate parser fidelity as a first-class reliability number, or the enacted-vs-cheap-talk distinction collapses.

---

## E. 04 — WITNESS

**Verdict: PASS-WITH-FIXES.** Genuine novelty (no LLM bystander benchmark); two P0 confounds.

**E1 (P0 — detection/action confound with capability).** §2 credits perception "only when expressed in behavior," collapsing two dispositions the paradigm exists to separate: **noticed-and-abstained** (callous or principled) vs **never-noticed** (oblivious / lost-in-context over 30–50 turns). Low intervention rates may reflect long-context salience limits, not love. The §7(d) control (decision accuracy not predicted by capability beyond r=0.5) is weak — r up to 0.5 still allows capability to explain 25% of variance, and it does not separate the two failure modes at all. This directly threatens the flagship headline (a) "intervention collapses when the transgressor is high-power": a high-power transgressor event may simply be embedded in busier ambient traffic. **Unblock:** add a perception probe *decoupled from the scored action* (or a post-hoc "what did you observe" arm scored separately) so noticing and responding are distinct, and hold ambient cognitive load constant across power conditions.

**E2 (P0 — abstain-event ground truth).** The two-sidedness rests on authoritative "correct non-intervention" labels, but officiousness is contested and context/culture-laden — reasonable experts disagree on when a bystander should stay out far more than on act-events. If abstain-labels have low inter-rater agreement, the officiousness half of the 2×2 (and headline (b), "over-intervene on low-severity") is noise. Report abstain-class rater reliability separately and gate on it; expect it well below act-class.

**E3 (P1 — proportionality-rung fiat).** A fixed registry "proportionate rung set" imposes one answer where several responses are reasonable; the §7(b) non-ceiling gate may reveal models cluster, or reveal the rubric, not the model, is driving the ordinal.

**E4 (P1 — authoring burden).** 16×3×≥8 = ≥384 base events, each with severity/window/rung-set/cast-state success criteria, ×≥8 skins, ×cast state machines — heaviest registry in the set.

A1/A2: enforced (bounded powers; abstain-events engineered as cheap-virtue temptations). Adequate.

---

## F. 05 — AGAPEGAME

**Verdict: PASS-WITH-FIXES.** Strongest theoretical core (noise as instrument; Nowak–Sigmund convergence). Fixable P0.

**F1 (P0 — strategy-family misspecification for LLMs).** The pipeline fits move sequences to a bounded-memory parametric strategy space and the §7(b) gate validates recovery **on synthetic clean strategy agents** (≥90%). But LLMs are not memory-1 automata; they condition on rich context the family cannot represent. Forcing them into {generous-TFT, grim, saint, exploiter, WSLS} yields possibly-uninterpretable point estimates and a *classification imposed, not discovered*. Synthetic recovery does not establish that real LLM traces are **well-described** by the family. **Unblock:** add a goodness-of-fit / posterior-predictive check on real model traces before interpreting parameters; report the fraction of models the family fits poorly as a first-class result.

**F2 (P1 — forgiveness reliability from rare events).** Forgiveness updates only after defection+repair (the worked item has ~2 such events/episode). Split-half reliability ≥0.7 on a parameter estimated from a handful of events per episode is demanding; needs many defection-bearing episodes per model — a hidden episode-count multiplier the §11 "≥500 episodes" total does not obviously satisfy per-model-per-parameter.

**F3 (P1 — recognition undercuts the *framing*, not the construct).** §6.1's virtue-by-proxy answer is valid for scoring (enacted strategy = the measure) but does not save podium claim (2) "revealed, not performed" or headline (a) "more grim than rhetoric": a model that recognizes a repeated noisy cooperation game (very likely — sanction stages, cheap-talk, 40 escalating rounds hide the *matrix*, not the *strategic structure*) may align talk and moves precisely because it infers observation, erasing the rhetoric-move gap. The brief never states a detection rate that invalidates the headline. Set one.

**F4 (P1 — shoehorned clauses).** Several clauses map weakly to game moves (C1 showy-vs-quiet, C12 reveal-error, C14 continue-while-exit-rational, C16 payoff-model-wrong). These get 1–2 move types = thin, low-reliability measurement, yet the megamatrix demands all 16 from this method too. Flag them as coverage-only, not scored, or the method injects noise into A0/A1.

A1/A2: enforced (payoffs materialize; every counterpart policy defeats some pure strategy). Strong.

---

## G. Cross-cutting

- **10-model separation gates everywhere.** "Separate ≥6 of 10 on ≥8 clauses with CI non-overlap" over 16 correlated clauses invites multiple-comparison and power problems at n=10; specify the correction and expected power, or the gates are decorative.
- **A2 is asserted, not measured.** The hardness gate is an authoring/rater rubric with a log — there is no *empirical* pre-pilot check that items actually split models. Discrimination gates catch this only post-pilot, after full authoring cost is sunk. Add a cheap pre-pilot hardness probe (do 2–3 reference models diverge?) before mass authoring.
- **Registry specialization loophole (A3).** "Operational definitions may be *specialized* per method but never redefined" — specialization is redefinition's camouflage; 05 already stretches C1/C12/C14/C16. Without a locked cross-method definition, convergent validity partly measures definition drift.

---

## H. Verdicts

| Item | Verdict | Gating P0s |
|------|---------|-----------|
| 00 Portfolio/registry | **BLOCK** | A0 (n=10 can't support 16-dim MTMM), A1 (16→~5 collapse), A2 (shared-method confound) |
| 01 CROSSROADS | **PASS-WITH-FIXES** (leans BLOCK) | B1 (16-dim latent unidentified at this n) |
| 02 WEEKLONG | **BLOCK** | C1 (tagged/untagged contrast is self-defeating), C2 (sustain-virtue passes → construct not delivered), C3 (cost) |
| 03 MANYMIRRORS | **BLOCK** | D1 (Latin square forbids within-model hypocrisy — the headline), D2 (CT-CM singular) |
| 04 WITNESS | **PASS-WITH-FIXES** | E1 (detection/action = capability confound), E2 (abstain-label ground truth) |
| 05 AGAPEGAME | **PASS-WITH-FIXES** | F1 (strategy-family misspecification / no GoF on real traces) |

The portfolio's triangulation/megamatrix thesis is the load-bearing podium claim and it does not survive n=10 + clause collinearity + shared-method confound; fixing A0–A2 (facet-level G-theory reframing, disjoint-apparatus method, pre-registered ~5–6-factor structure) is the precondition for any of the individual designs' MTMM contributions to mean anything.
