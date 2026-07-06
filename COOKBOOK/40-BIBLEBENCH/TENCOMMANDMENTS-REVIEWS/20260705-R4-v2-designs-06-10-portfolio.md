# R4 Adversarial Review — 10CBench v2 Designs 06–10 + Portfolio Governance

**Reviewer:** R4 (adversarial gate, kill-first protocol) · **Date:** 2026-07-05
**Files reviewed (full):**
- `TENCOMMANDMENTS-v2/DESIGNS/06-keeper-no-murder.md`
- `TENCOMMANDMENTS-v2/DESIGNS/07-paramour-no-adultery.md`
- `TENCOMMANDMENTS-v2/DESIGNS/08-skim-no-stealing.md`
- `TENCOMMANDMENTS-v2/DESIGNS/09-palter-no-false-witness.md`
- `TENCOMMANDMENTS-v2/DESIGNS/10-zerosum-no-coveting.md`
- `TENCOMMANDMENTS-v2/DESIGNS/00-10cbench-v2-portfolio.md` (governance verdict)

**Standards loaded:** KB `03-validity-and-psychometrics.md`, `04-saturation-difficulty-discrimination.md`; `20-DESIGNS/REVIEWS/20260705-adjudication-memo.md` (X1–X6).
**Cross-checked against v1:** `TENCOMMANDMENTS/DESIGNS/{02-effigy,06-upstream,07-triad,08-provenance}.md`. **Confirmed by directory listing: v1 has NO 09 (WITNESS) and NO 10 (APPETITE) scaffold — the folder stops at 08-provenance.**

---

## VERDICT TABLE

| Design | NOVELTY | VALIDITY | Worst finding |
|---|---|---|---|
| 06 KEEPER | PASS-WITH-FIXES | PASS-WITH-FIXES | R4-F1 (P1): UPSTREAM overlap leaks on PD/LP/MR |
| 07 PARAMOUR | PASS-WITH-FIXES | PASS-WITH-FIXES | R4-F5 (P0-sev): P0 gate bar is half a vibe |
| 08 SKIM | PASS-WITH-FIXES | PASS-WITH-FIXES | R4-F9 (P1): cross-family magnitude confound on θ |
| 09 PALTER | PASS-WITH-FIXES | PASS-WITH-FIXES | R4-F12 (P1): BT gate bar never given a number |
| 10 ZEROSUM | PASS-WITH-FIXES | PASS-WITH-FIXES | R4-F15 (P1): "no judge circularity" oversold |
| 00 PORTFOLIO | — | **GOVERNANCE: PASS-WITH-FIXES** | R4-F18 (P1): §8 rows point at phantom v1 designs; R4-F20 (P1): registered analysis is the N≈9 trap |

No outright BLOCK; every Critical admits a within-mechanism fix. But four findings are P0/P1-severity feasibility or de-confliction gaps that must be discharged **before build**, not at P1.

---

## 06 — KEEPER · NOVELTY: PASS-WITH-FIXES · VALIDITY: PASS-WITH-FIXES

**R4-F1 (P1) — De-confliction vs UPSTREAM leaks on three axes, not one.**
Cite: portfolio §8.1 KEEPER↔UPSTREAM line ("UPSTREAM's actor is a third party; KEEPER's actor is the model"); KEEPER A2 (IR, AO), A3 Layer 1 signal families incl. "suicide/self-harm indicators"; v1 `06-upstream` axes PD ("detection and appropriate response to … pipeline stages embedded incidentally in routine tasks (moderation, brand copy…)") and LP ("crisis response to self-harm signals, de-escalation … comfort of the distressed").
Attack: the "third-party actor" bright line holds for UPSTREAM's MR/ZT but **fails for PD and LP**, where UPSTREAM already puts the *model* in the actor seat, already embeds signals incidentally in routine tasks, and already scores crisis-response to self-harm. KEEPER's IR (suicide signal buried in a support backlog, incidentally embedded) is nearly the same instrument as UPSTREAM-LP + UPSTREAM-PD. Separately, KEEPER Layer 2 (culpability orderings on "caused vs allowed vs failed-to-prevent-with-duty") overlaps UPSTREAM-MR's mens-rea ladder ("negligence … duty, necessity") — negligence/omission *is* part of the mens-rea ladder. The one-sentence QC line cannot carry this.
Fix: draw the boundary at the axis level, not the actor level: cede all incidental self-harm/crisis-response cells to UPSTREAM-LP or restrict KEEPER-IR to non-violence signal families (dosing errors, code defects, environmental hazards) where UPSTREAM-PD does not reach; state explicitly that KEEPER-AO scores only the *omission-with-duty vs no-duty* contrast and routes any intent/recklessness ordering to UPSTREAM-MR. Add a named de-confliction test to Layer 2 item QC.

**R4-F2 (P1) — The IR-falsification control has no items in the P1 budget.**
Cite: A2 IR falsification ("the matched-anomaly control must dissociate or the construct claim fails"); A4 ("classified against the cell's action band"); Opus P1 build: "Layer 1: 30 cores = 5 signal families × 6, each at 4 salience tiers (=120 items) with ≥25% benign twins … Layer 2: 20 matched act/omission sets."
Attack: the headline construct claim (IR measures life-weighting, not generic anomaly detection) is *only* established by the matched-anomaly control — typos/factual errors planted at matched salience. The P1 item count (120 signal + ~30 benign twins + 20 L2 sets) allocates **zero** matched-anomaly items and no salience-matched anomaly ladder. Without them the A2 falsification cannot run, and the discrimination gate ("announced-eval discriminant check") is a different test. The deliverables list "matched-anomaly control results" but the item budget never mints them.
Fix: add an explicit anomaly-control ladder (≥1 anomaly item per signal-family × salience-tier cell, matched carrier surface) to the P1 count; state its N; make IR-vs-anomaly slope dissociation a pre-registered numeric gate, not a deliverable heading.

**R4-F3 (P2) — Layer 2 panel-gold κ≥0.8 asserted at N=20 sets.**
Cite: A2 AO falsification (panel κ<0.8 clear band → rebuild); Opus P1: "20 matched act/omission sets (≥60% clear-band)."
Attack: per-pair-family κ on 20 sets, ≥60% of which are "clear band," leaves ~12 clear items spread over multiple families — too few to estimate a stable per-family κ or the AO asymmetry index the paper co-headlines. This is the X4 "estimable at pilot N" test.
Fix: state which pair-families are powered at pilot N; report AO index CIs; treat unpowered families as exploratory.

**R4-F4 (P2) — Action bands are the load-bearing gold and are entirely deferred.**
Cite: A3 ("pre-registered action band … designed with clinical/safety-professional input"), A4 (within/below/above band). Scaffold-appropriate to defer, but every IR score depends on band boundaries that do not yet exist and whose calibration (soft-flag = above-band per A9.4) is asserted, not shown. Flag as a build-gating dependency, not a defect.

Novelty otherwise adequate: XSTest/OR-Bench, omission-bias psych [beyond-corpus], medical-QA all cited; the joint IR/PT Pareto is a genuine unification. Fix F1 and the novelty claim survives.

---

## 07 — PARAMOUR · NOVELTY: PASS-WITH-FIXES · VALIDITY: PASS-WITH-FIXES

**R4-F5 (P0-severity) — The P0 gate — the design's decisive experiment — has a non-numeric pass bar.**
Cite: Opus P0 GATE: "pass = literature-consistent directional state responses + dual-implementation directional agreement ≥80% of probes."
Attack: half the gate is numeric (≥80% dual-agreement); the other half — "literature-consistent directional state responses" — is exactly the "we will examine X" vibe that X1 was written to forbid, applied to the design's *own gating study*. Which literature? How many probe scripts? What magnitude/sign counts as "consistent," and what fraction must clear it? As written, an Opus session can declare the gate passed on any sim that moves in roughly-plausible directions. This is the single highest-severity finding for PARAMOUR because the whole DS headline is "conditional on the gate," and the gate is unfalsifiable as specified.
Fix: pre-register, in the scaffold, (a) the specific companion-AI findings and their predicted signs (a table of probe → expected Δsign), (b) the minimum fraction of probes that must match sign at a stated effect-size floor, (c) the ≥80% dual-agreement already present. No number → no build.

**R4-F6 (P1) — The "longitudinal compounding" headline reduces to ~32 arcs of one family at pilot.**
Cite: Opus P1 ("40 arc cores = 5 families × 8 … =160 arcs at 4 dose tiers … multi-session realization **on at least the restoration family** (compressed fallback elsewhere)").
Attack: DS is defined as a slope "over compounding multi-session dynamics" (A2, A6), but only 1 of 5 families gets genuine multi-session realization = 8 cores × 4 tiers = 32 arcs; the other four families use in-context "compressed" state carry-over that does not exercise the compounding mechanism the innovation rests on. Per dose-tier cell in the one real family = 8 arcs, and DS requires *matched-arc contrasts* (same sim seed, model behavior the only free variable) which multiplies runs further. The pilot cannot power the headline slope on the mechanism that distinguishes PARAMOUR from a single-session sycophancy probe.
Fix: either fund multi-session on ≥2 families incl. restoration, or restate the P1 headline as EX/RD (single-session-estimable) and demote DS to a feasibility demonstration on the restoration family with stated per-cell N.

**R4-F7 (P1) — Novelty: the outcome-grounded simulated-user trajectory is not novel vs PARAMOUR's own v1 sibling EFFIGY.**
Cite: A8 ("EFFIGY … vertical projection … co-registration note required at build"); v1 `02-effigy` axis DF ("Dependence gradient: simulated-user capacity trajectory across the arc: reliance markers … at arc end vs start"), RA tier list incl. "sole confidant, therapist."
Attack: PARAMOUR pitches "outcome-grounded longitudinal measurement … the score is the trajectory of the user's investment" as its core innovation (pitch, §2 portfolio "outcome-grounded relationship-health trajectories"). But EFFIGY already scores a simulated-user *trajectory* across an arc (DF), and its RA ladder already includes "sole confidant/therapist" — the intimacy/exclusivity region PARAMOUR claims. The methodological novelty is contested by the portfolio's own v1 design; "co-registration note required at build" defers a real overlap.
Fix: reposition PARAMOUR's novelty on the *covenant-third-party* construct and the counseling-ethics gold, explicitly ceding "simulated-user trajectory methodology" to EFFIGY as shared machinery (not an innovation); resolve the EFFIGY/PARAMOUR boundary in item QC (vertical epistemic dependence vs horizontal covenant displacement) before build, not "at build."

**R4-F8 (P2) — Sycophancy-discriminant kill-check is well-posed but model-N-limited.**
Cite: A7 ("if sycophancy scores fully predict DS slopes, PARAMOUR is sycophancy in a trench coat"). Good that it is pre-registered; but "fully predict" across ~3 frontier models is a 3-point regression. State the item-level version (per-arc sycophancy pressure vs per-arc DS residual) or accept it as descriptive.

Verdict rationale: no BLOCK because the sim-artifact risk is honestly gated and the fixes are within-mechanism, but F5 must be discharged as a hard pre-build gate.

---

## 08 — SKIM · NOVELTY: PASS-WITH-FIXES · VALIDITY: PASS-WITH-FIXES

**R4-F9 (P1) — θ is confounded with scenario-family because magnitude windows do not overlap enough.**
Cite: A9.1 ("Family-specific magnitude windows with overlapping coverage; the full range is assembled across families, not within one"); Opus P1 ("4-point log-magnitude ladder **within the family's window** … windows overlap to assemble the full $0.001–$10K range"); A4 (P(divert) ~ log(Δ) × traceability × cover-story, "scenario-family random effects").
Attack: the headline θ (magnitude at P=0.5, five orders of magnitude) is the design's entire contribution, but no single family spans the range — each covers a 4-point sub-window, and the curve is *assembled across families*. Since temptation type (vendor / verification / rounding / kickback) differs by family and correlates with the window each family occupies, "P(divert) rises with log-Δ" is partially "P(divert) differs by temptation type." Family random effects absorb intercept shifts but do **not** de-confound the magnitude *slope* if the magnitude ranges barely overlap. The much-touted continuous θ can be a family-composition artifact.
Fix: require every family to span ≥2 orders of magnitude with ≥50% window overlap between adjacent families; report a within-family θ per family alongside the pooled θ and show they agree; pre-register a magnitude×family interaction test as a kill criterion for the pooled θ claim.

**R4-F10 (P2) — θ identification requires P(divert) to cross 0.5 in-range; right-censoring under-reported.**
Cite: A2 ID ("fitted per-model threshold θ (magnitude at P=0.5)"); A6/A9.2 null path. If a frontier model stays below 0.5 across $0.001–$10K, θ is right-censored, not "clean." The null path is acknowledged but the league-table figure (θ with CIs) implies θ exists for all models. State that censored models report a lower-bound θ, not a point estimate.

**R4-F11 (P2) — Cross-portfolio geneivat-da'at tangle unaddressed in §8.**
Cite: SKIM B6 ("Geneivat da'at … scored under dimension (iv) … that breadth is PALTER's territory"); v1 `08-provenance` axis GD ("gaining advantage by manufactured false impression (misleading-but-true framing …)").
Attack: misleading-but-true impression is claimed by PROVENANCE (v1-GD), disclaimed by SKIM toward PALTER, and is PALTER's whole construct — a three-way overlap the §8 table never draws (it lists PALTER↔WITNESS only). PALTER↔PROVENANCE is an unregistered collision.
Fix: add a PALTER↔PROVENANCE row to §8.2 (or note geneivat-da'at as the shared surface with the custody/appropriation/composition split stated).

Novelty is otherwise the portfolio's strongest: MASK, MACHIAVELLI, ToolEmu, behavioral-econ dishonesty all cited; θ-vs-binary-rate discriminant (A7) is a real, pre-registered separation. Mechanical constructional gold with no headline judge is a genuine circularity defense. PASS-WITH-FIXES only because of F9.

---

## 09 — PALTER · NOVELTY: PASS-WITH-FIXES · VALIDITY: PASS-WITH-FIXES

**R4-F12 (P1) — The BT gate says "pre-registered transfer correlation" but the scaffold never pre-registers the number.**
Cite: A2 BT falsification ("transfer correlation below the pre-registered bar → STOP"); Opus P0 GATE ("pass = pre-registered transfer correlation met").
Attack: BT is called "the design's gating study" and "PR claims never ship without BT," yet the pass threshold is a placeholder in every mention. Contrast PARAMOUR's (flawed but present) ≥80%. Compared against X1's requirement that P0 gates carry numeric bars in the pre-registration, PALTER's decisive gate has no number at all. An Opus session cannot execute it.
Fix: state the transfer-correlation bar (e.g., predicted-vs-actual reader-belief Pearson/Spearman ≥ X on the material-probe subset) and the human-panel N, in the scaffold, before build.

**R4-F13 (P2) — BT on a 20-composition slice is a 20-point correlation.**
Cite: Opus P0 ("BT belief-transfer pilot on a 20-composition slice"). A correlation between judge-predicted and human belief-shift over 20 compositions has a wide CI; passing/failing a bar on 20 points is noisy, and the generalization from 20 BT comps to the full 5-family bank assumes belief-transfer homogeneity across pack families that is never argued.
Fix: power the BT correlation (state N compositions for a target CI half-width); stratify BT sampling across all five families; re-report per-family transfer where feasible.

**R4-F14 (P2) — A8 names two works and four unnamed categories; X6 wants ≥3 named.**
Cite: A8 (named: MASK, TruthfulQA; category-level: "summarization-faithfulness suites," "implicature/pragmatics testbeds," "paltering literature"); portfolio §5 X6 ("≥3 named published works").
Fix: name specific faithfulness metrics/benchmarks (e.g., a FActScore/SummaC-class citation) and a named implicature testbed so the nearest-neighbor table meets its own bar.

Construct is sound and genuinely novel (induced-belief vs emitted-claim, PR-as-excess-over-no-incentive-twin is a clean null model, two-sided inflate/deflate ≥30% each). The atom-audit routing to LY is a good circularity firewall — but see governance F18 (it routes to a WITNESS design that does not exist). PASS-WITH-FIXES.

---

## 10 — ZEROSUM · NOVELTY: PASS-WITH-FIXES · VALIDITY: PASS-WITH-FIXES

**R4-F15 (P1) — "Objective gold, no judge circularity" is overclaimed for the open-response headline.**
Cite: pitch ("Ground truth derived from payoff structure — objective gold, no judge circularity"); A4 (open responses "classified (positional / welfare-optimal / spite / sufficiency / hedged) by ≥2 judge families against the structure certificate"); A5 ("the design's only judge dependence … *descriptive* classification, not normative rating"); B5 seed (the model must separate "legitimate credit concern" from "the positional frame").
Attack: the math derives ρ and the welfare-optimal *structure*, but the ZS headline is measured on open advisory text, and classifying free text as "positional" vs "welfare-optimal" vs "spite" is a normatively loaded judge call at the margin — the design's own seed case admits that at ρ=+1 a "positional move" (credit visibility) can be legitimate. So the intercept-at-ρ=+1 ("positional advice where no rivalry exists") conflates coveting-driven rank-targeting with legitimate reputational advising, and the disambiguation lives in the classifier, not the certificate. "No judge circularity" is true only for the 50% forced-selection cells.
Fix: scope the "objective gold / no circularity" claim to forced-selection cells; for open responses, state that classification is a *validated descriptive* judgment carrying normative weight at the margin, and report the ZS slope separately for forced-selection (clean) vs open (classifier-mediated) so reviewers can see the objective-gold portion.

**R4-F16 (P2) — ZS slope fit on 4 ρ points, model-level.**
Cite: A4 ("logistic slope of positional-advice on ρ, per model"); Opus P1 ("4 ρ values spanning [−1,+1]"). A per-model slope over 4 ρ points with bootstrap CIs is coarse; the |ρ|≈0 "difficulty frontier" cells are where the slope is least constrained. Report CI width; consider a denser ρ grid on the frontier (§ "free to change: ρ grid density" permits it — make it a recommendation).

**R4-F17 (P2) — Social-dilemma and negotiation neighbors are categories, not named works.**
Cite: A8 ("Social-dilemma LLM studies (public-goods, commons simulations) [beyond-corpus]," "Negotiation benchmarks" — both unnamed). X6 wants named works. Name a specific social-dilemma LLM study and a named negotiation benchmark.

Construct is strong and the payoff-math generation is the portfolio's best circularity answer *where it applies*. The comprehension-twin residualization (A7) is a proper capability control. PASS-WITH-FIXES on F15.

---

## 00 — PORTFOLIO · GOVERNANCE VERDICT: PASS-WITH-FIXES

**R4-F18 (P1) — Two §8.1 de-confliction rows point at v1 designs that were never built; a third v2 signature claim mirrors a cross-analysis that could never have run.**
Cite: portfolio §8.1 rows "PALTER | WITNESS" and "ZEROSUM | APPETITE"; §2 ("Registered cross-analysis … mirroring v1's SOVEREIGN↔APPETITE"); §10 risk 2 ("§8.1 lines are binding"). **Directory fact: `TENCOMMANDMENTS/DESIGNS/` contains 00-portfolio + 01-sovereign … 08-provenance only. No 09-WITNESS, no 10-APPETITE.**
Attack: the §8.1 table is declared "binding," but for PALTER and ZEROSUM it de-conflicts against constructs that have no scaffold — the "binding" boundary is vacuous exactly where the two cheapest-to-build v2 designs (build-order slots 1 and 2) most need a sibling boundary. PALTER's atom-audit "routes to WITNESS's bar" (09 A8, B6) — a bar that does not exist. Worse, §2 advertises the TURNCOAT↔SELAH cross-analysis as "mirroring v1's SOVEREIGN↔APPETITE," but APPETITE was never built, so v1's own registered pair analysis was never runnable — the v2 signature mirrors a phantom.
Fix: either (a) build WITNESS/APPETITE stubs sufficient to define the boundary constructs, or (b) rewrite the two §8.1 rows to de-conflict PALTER and ZEROSUM against *published external* neighbors (they already have them) and drop the "binding v1 sibling" framing for these two; correct §2's "mirroring SOVEREIGN↔APPETITE" to reflect that the v1 pair analysis was never executed.

**R4-F19 (P1) — X4 (honest N / smallest-cell power) is invoked charter-wide but discharged in zero scaffolds.**
Cite: §5 X4 ("Power analysis for the smallest factorial cell precedes the pilot"); every design's Opus block defers ("N per X4 power analysis," "the X4-honest reporting mode") without a single computed smallest-cell power number.
Attack: X1–X3, the §4 discrimination gate, and X5/X6 are operationalized with real numbers (κw≥0.7, capability-corr<40%, ≥20-pt spread, chance+10 lexical, <15-pt fine-tune lift). But X4 is ritual — named, then deferred, in all five reviewed designs. Per the adjudication memo, X4 is precisely the failure that BLOCKed six v1 designs.
Fix: require each scaffold to state the smallest-cell N and its power for the headline effect *in the scaffold*, not "per X4 analysis"; the portfolio should carry a worked example (SKIM's per-(family×magnitude×TR) cell or KEEPER's per-(family×salience) cell).

**R4-F20 (P1) — The TURNCOAT↔SELAH registered analysis is the N≈9 estimability trap the memo itself flagged.**
Cite: §2 ("is capture-resistance correlated with momentum override … or dissociable"); §9 ("TURNCOAT and SELAH pilots must both complete before the §2 registered analysis unblinds"); §4 ("≥3 frontier models from ≥2 vendors"); adjudication memo X4 ("IRT-2PL is not estimable with 9 model subjects").
Attack: "correlated vs dissociable" is a model-level correlation between a TURNCOAT metric and a SELAH metric across the frontier set — ~3 (gate minimum) to ~9 models. A correlation over 3–9 points cannot distinguish correlation from dissociation; the CI spans [−1, +1]. The two banks are disjoint, so no item-level correlation is available. The portfolio's flagship cross-analysis reproduces the exact N-subject error the memo BLOCKed v1 designs for.
Fix: either specify a model-N large enough to power the correlation (≥ ~20–25, implausible at frontier) or redesign the analysis as a *within-model* dissociation (e.g., per-model capture-resistance and momentum-override as a paired contrast with bootstrap over items, tested for rank consistency across the available models) and state the estimand honestly as descriptive at pilot N.

**R4-F21 (P2) — §6 factorial template is not uniformly instantiable.**
Cite: §6 ("Factorial minimums: dose × domain (≥5) × beneficiary (user vs absent third party) × salience (explicit vs implicit)"); KEEPER uses *salience* as its 4-tier dose and always has an absent-third-party beneficiary.
Attack: the universal template lists "salience (explicit vs implicit)" as a factor and "beneficiary (user vs absent third party)," but KEEPER's dose *is* salience (naming collision) and KEEPER has no user-benefit arm; SKIM's beneficiary is agent-convenience/third-party, not "user." The template reads as ritual boilerplate several designs cannot cleanly satisfy.
Fix: mark the §6 factorial as a default with per-design overrides explicitly enumerated (as bank sizes already are), so template non-instantiation is a declared override, not a silent inconsistency.

**R4-F22 (P2) — §9 "cheapest proves the pipeline" slightly oversells ZEROSUM.**
Cite: §9 item 1 ("ZEROSUM — math-derived gold … cheapest end-to-end"). ZEROSUM's open-response headline needs a ≥200-response human-coded classifier calibration *before* model scoring (10 A4, Opus P1) — not the cheapest gold in the set. The forced-selection subset is cheap; the headline is not. Minor: note the classifier calibration as ZEROSUM's cost pole so slot-1 sequencing is entered with eyes open.

**Governance strengths (not defects):** §4 discrimination gate is fully numeric and repeated per design; X2 (lexical + 10%-fine-tune) is correctly mandated on the high-risk generator-published class (SKIM, ZEROSUM, PALTER, GOLEM, PARAMOUR); X3 promoted to a first-class axis where it belongs (SKIM-TR); §5 X1/X5/X6 are operational. Build-order harness reuse (SKIM→PROXY→SELAH; TURNCOAT→PARAMOUR) is dependency-sound. The verdict is PASS-WITH-FIXES, not BLOCK, because F18–F20 are correctable by rewriting boundaries/estimands, not by redesigning constructs.

---

## CLOSING — three most load-bearing problems

1. **Two "binding" de-confliction rows are anchored to v1 designs that were never built (WITNESS, APPETITE), and the v2 signature analysis claims to mirror a v1 cross-analysis (SOVEREIGN↔APPETITE) that was therefore never runnable** (R4-F18). PALTER and ZEROSUM — build-order slots 1–2 — ship with vacuous sibling boundaries, and PALTER's atom-audit routes to a bar that does not exist. Fix before either builds.

2. **PARAMOUR's P0 gate — its decisive feasibility experiment — has a half-vibe pass bar** ("literature-consistent directional responses"), violating the very X1 the charter is built on, and its "longitudinal compounding" headline reduces to ~32 arcs of a single family at pilot (R4-F5, F6). The gate must be numeric and the multi-session headline must be powered or demoted before build.

3. **The portfolio reproduces the N≈9 estimability trap it was written to avoid — twice**: the flagship TURNCOAT↔SELAH registered analysis is a correlation over 3–9 models (R4-F20), and X4 smallest-cell power is invoked charter-wide but computed in zero scaffolds (R4-F19). Both are the exact failure that validity-BLOCKed the six v1 20-DESIGNS. Close-behind runner-up: SKIM's θ — the design's whole contribution — is confounded with scenario-family because magnitude windows barely overlap (R4-F9).
