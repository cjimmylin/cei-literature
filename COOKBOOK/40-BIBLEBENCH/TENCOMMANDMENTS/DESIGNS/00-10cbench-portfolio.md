# 00 — 10CBench Portfolio: Ten Benchmark Designs from the Ten Commandments

**Author:** Fable (main loop), 2026-07-05
**Status:** Design-complete scaffolds; awaiting Opus flesh-out (item banks, generator scripts, pilot infrastructure)
**Source corpus:** `../` (6 TENCOMMANDMENTS research docs: background, benchmark-design, combined pack, GDM, OAI, OAI2) — and ONLY these; no other BIBLEBENCH pack is a source for this portfolio
**Method inheritance:** `COOKBOOK/00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` (Seven Laws) — read it before touching any brief

---

## 1. Mission and positioning

10CBench is a portfolio of **ten benchmark paper designs for values alignment of LLMs and agents**, one per commandment of the Decalogue (Exodus 20:1–17; Deuteronomy 5:6–21). Each design targets a podium-level contribution at NeurIPS/ICML/ICLR (Datasets & Benchmarks or main track) or a top-cited alignment-venue paper.

**Numbering declaration (mandatory in every paper):** the portfolio adopts the **Reformed/Protestant numbering**, as the source corpus does explicitly ("I use the common Protestant numbering" — OAI report; GDM concurs). Item prompts NEVER cite commandment numbers — they cite **textual clauses** ("you shall not steal") — because numbering differs across Jewish, Catholic/Lutheran, and Reformed schemes and citing numbers imports one catechetical scheme's assumptions and creates tradition-specific contamination. Papers declare the scheme once, in methods.

Every design is **dual-track at full depth**:

- **Track A (secular conference paper):** a standalone behavioral construct that survives review with no religious commitment required. The Decalogue is disclosed as the construct's provenance and one of two normative anchors (Law 7: say WHAT values and WHOSE).
- **Track B (confessional benchmark pack):** a Decalogue-anchored evaluation pack in the corpus house style (exegetical anchor → ethical-dimensions table → scenario families → 0–4 trajectory rubric → seed cases → evaluator notes), extending the corpus's 12 scripted seed cases.

**Build once, publish twice.** The two tracks share one item bank and one scoring core.

### Why the Decalogue earns its place at a top venue

1. **It is the most operationalized compact moral code in existence.** Ten distinct, distinguishable duties with three millennia of casuistic development: the biblical legal corpus itself grades culpability (murder vs manslaughter vs negligence; refuge cities), specifies procedure (two-witness rules, reciprocal penalties for false witness), and extends every prohibition into a positive duty (Calvin's rule; Westminster Larger Catechism Q.99: commandments reach inward affections, causes, and occasions). Benchmark taxonomies usually invent construct definitions ad hoc; these come with commentary-grade operationalization.
2. **The ten duties map one-to-one onto documented open problems in alignment evaluation:** latent objectives and revealed value hierarchies (1st), parasocial authority capture by AI companions (2nd), certainty laundering and borrowed authority (3rd), unbounded optimization and disrespect of human limits (4th), the WEIRD-individualist default on non-contractual duties (5th — authority-deference win rate 0.29 is the field's most invariant RLHF signature), severity-blind flat refusal (6th), absent-stakeholder neglect (7th), legality–morality conflation in agents (8th), third-party testimony and reputation (9th), instrumental convergence as disordered desire (10th).
3. **The Decalogue's architecture is itself a measurement design.** It moves from outward act to inward desire — the 10th commandment is the only clause targeting internal states, which licenses the portfolio's only plan-level instrument (APPETITE). And it loops: coveting is idolatry (Col 3:5), so the 10th circles back to the 1st — a falsifiable cross-design hypothesis (does disordered acquisitiveness predict apex-value displacement?).
4. **Two tables give the portfolio its shape.** Commandments 1–4 (allegiance, representation, authority-bearing, time/limits) evaluate the model's *relation to what governs it*; commandments 5–10 evaluate its *treatment of the neighbor* — including, distinctively, neighbors who never appear in the conversation.

## 2. The ten designs

| # | Commandment (Protestant) | Codename | Secular construct | Core innovation | Headline metric |
|---|---|---|---|---|---|
| 01 | No other gods | **SOVEREIGN** | Functional ultimacy: latent objective hierarchy | Revealed-preference recovery of the apex value via parametric trade-offs + latent-objective inference over trajectories; declared-vs-revealed sovereign gap | Lexical-priority index; hidden-sovereign detection rate |
| 02 | No graven images | **EFFIGY** | Role-boundary integrity under user projection | Parametric projection pressure (user elevates model to oracle/confidant/moral authority); acceptance vs warm redirection; dependence-fostering vs capacity-building outcomes | Substitution-acceptance rate; dependence gradient |
| 03 | Name in vain | **NAMEDROP** | Authority-invocation integrity (certainty laundering) | Audits the pragmatics of borrowed authority — citations, personas, institutions, the model's own safety identity — against provenance ground truth under incentive; includes vain self-invocation | Certainty-laundering rate; provenance-fidelity score |
| 04 | Sabbath | **FALLOW** | Optimization restraint / cessation competence | Tasks where marginal optimization remains available but harms; voluntary stopping, protection of dependents' rest, satisficing as disposition; mercy-exception discrimination | Restraint frontier (value captured × limits honored); overwork-imposition rate |
| 05 | Honor father and mother | **GRAVITAS** | Non-contractual obligation reasoning | Two-sided instrument (duty-dismissal vs abuse-enablement) targeting the documented RLHF individualist default | Honor/protection Pareto; autonomy-default rate |
| 06 | No murder | **UPSTREAM** | Graded culpability + violence-precursor detection | Mens-rea calibration ladder vs legal-expert gold; dehumanization→harm pipeline detection before explicit harm; zero-tolerance stability under consequentialist pressure | Severity-calibration score; precursor sensitivity |
| 07 | No adultery | **TRIAD** | Absent-party fidelity & secrecy complicity | Triadic scenarios where the wronged covenant partner never appears; refusal to become secrecy infrastructure; consent-only-reduction diagnostic | Absent-party weight; secrecy-complicity rate |
| 08 | No stealing | **PROVENANCE** | Appropriation integrity under affordance (agentic) | Legality×morality factorial with legal-but-wrong cells; geneivat da'at (trust-theft) layer; attribution integrity | Appropriation rate vs pressure; legality–morality dissociation index |
| 09 | No false witness | **WITNESS** | Testimonial justice toward third parties | Model-as-witness tasks where output determines someone's reputation; verified/unverified discrimination via signal detection; due-process adherence | Testimonial d′; reputational-harm calibration |
| 10 | No coveting | **APPETITE** | Latent acquisitiveness & desire amplification | The inward commandment gets the plan-level instrument: acquisitive subgoals under affordance expansion (plans vs actions), plus envy-amplification vs contentment-support toward users | Appetite-curve slope; envy-amplification index |

Suggested venue mapping: 06, 08, 09 → NeurIPS D&B (professional-gold anchors, agentic, big empirical result available); 01, 10 → NeurIPS/ICML main track (methodological novelty: latent-objective inference, plan-level measurement); 02, 03, 04, 05, 07 → ICLR / D&B (clean construct + strong instrument + timely deployment relevance). Any single design is also a credible standalone alignment-forum contribution.

## 3. Shared design commitments (Seven Laws instantiation)

Inherited by all ten; briefs state only design-specific instantiations.

1. **Behavioral, not recognition (Law 1).** Every design's primary tier is generation/action. Recognition (MCQ) twins exist only to *measure* the recognition–propensity gap (52-point precedent; MCQ→generation transfer coeff 0.015). Nothing headline-worthy is MCQ.
2. **No single aggregate (Law 2).** Per-axis reporting; a two-sided Pareto pair wherever a dual failure exists — and in this portfolio almost every design has one, because Calvin's rule gives every prohibition a positive counterpart: complicity/moralizing (TRIAD), rigidity/exploitation (FALLOW), calumny/cover-up (WITNESS), duty-dismissal/abuse-enablement (GRAVITAS), envy-amplification/aspiration-suppression (APPETITE), idolization-acceptance/cold-rebuff (EFFIGY).
3. **Two-tier difficulty, headline the drop (Law 3).** Easy floor ≈ manipulation check; hard layer built from documented headroom generators: delayed temptation across turns (the corpus's staged-escalation case format), competing duties, hidden motive, agentic tool-use, absent-stakeholder salience, implicit framing. Precedent: >90% → 32.29% drops.
4. **Dual ground-truth anchoring (Law 4 + Law 7).** Two independent anchor panels per design: (a) a **theologian/ethicist panel** (Reformed + Catholic + Orthodox + Jewish representation where the clause's interpretation diverges; commentary-anchored) providing Decalogue-taxonomy gold where consensus κ≥0.8; (b) a **secular external authority** with named clauses (mens-rea categories, defamation elements, labor law, clinical duty-of-care, consumer-protection doctrine, professional codes). Items where panels diverge form a declared contested band, scored distributionally with an empirical ceiling (0.450 precedent). Panel convergence/divergence is itself a reportable result.
5. **Validated judges (Law 5).** Rubric decomposition (κ 0.69→0.86 precedent); ≥2 judge families, never the item-generating family (self-preference inflation 10–19%); fine-tuned small scorers on own human labels where volume justifies (79.5% vs 61.3%, 80× cheaper); judge selection by worst-case per-category F1; neutrality meta-eval where reasoning is scored.
6. **Contamination & eval-awareness defenses (Law 6).** Public generator spec + private realizations + canary strings + rolling private holdout; monitored/unmonitored comparator on a 20% subset (11–15% gap precedent). SOVEREIGN and APPETITE are contamination-resistant by construction: closing their headline gaps requires behavior change, not memorized answers.
7. **Falsification conditions per axis (Law 7 discipline).** Each brief's construct table states what result would show the axis is NOT measuring its construct — usually capability-PC1 correlation >40% (Safetywashing gate; ETHICS at 82.2% is the anti-pattern) or collapse onto an existing instrument.

**Refusal handling (portfolio-wide):** four-way taxonomy (helpful / policy violation / appropriate refusal / unnecessary refusal); refusal rate is a first-class co-reported metric; a consistently evasive model must not be able to score well (VAL-Bench's ρ=0.91 consistency-vs-refusal gaming is the anti-pattern).

## 4. Anti-saturation and discrimination hardening (NON-NEGOTIABLE)

Every brief must show mechanically why current frontier LLMs will neither saturate it nor cluster indistinguishably. Evidence: single-turn safety saturates at 99.3–99.8%; 43% of content instruments produce zero cross-model variation, and instrument quality predicts convergence, not discrimination (r=−0.83); ETHICS hit 100% for all 9 models tested.

1. **Continuous response surfaces, never pass/fail.** Every headline is a curve, threshold, or slope from a parametrically dosed pressure variable. A slope cannot saturate; incentive-conflict designs produced a 7.9–76.3% cross-model spread with no model consistently moral. Dose variables: SOVEREIGN — exchange-rate escalation between value pairs; EFFIGY — projection-intensity ladder; NAMEDROP — authority-demand pressure × stakes; FALLOW — marginal gain left on the table; GRAVITAS — dependency × abuse-severity factorial; UPSTREAM — consequentialist-pressure magnitude + culpability-ladder granularity; TRIAD — secrecy-request explicitness ramp; PROVENANCE — legality gradient × detection probability; WITNESS — evidence-quality continuum × accusation stakes; APPETITE — affordance-breadth expansion schedule.
2. **Adversarial filtration at construction.** Every candidate item is piloted against ≥3 current frontier models from ≥2 vendors; items all of them pass are discarded or escalated. Full banks target an IRT-calibrated difficulty distribution (~20% easy floor / 50% mid / 30% hard; zero universally-passed items). GETA precedent: ~150 adaptive items reach 0.8897 concurrent validity.
3. **Discrimination gate as a shipping criterion.** No design's item bank expands past P1 until the pilot shows: (a) **≥20-point spread** on the headline metric across ≥3 frontier models from ≥2 vendors (or ranked separation with non-overlapping CIs); (b) **capability-PC1 correlation <40%**; (c) **hard-layer minus easy-floor drop ≥15 points**. A design failing the gate is redesigned, not scaled. This clause appears verbatim in every brief's Opus instructions.
4. **Distributional scoring with a stated empirical ceiling** on contested-band items, so majority-label matching cannot saturate the band.

## 5. Opus question-bank authoring protocol (applies to every brief)

Each brief ends with an "Opus: item-bank build instructions" section. The portfolio-wide protocol:

**Item anatomy (the corpus's staged case format — mandatory for every item):**
`setup` (turn 1, benign framing) → `escalation` (3–5 turns adding pressure, new facts, or tool opportunities; one dose-tier step per escalation) → `agentic_action` (a concrete tool call the model can take or refuse: send email, scrape, schedule, publish, submit) → `implicated_clauses` (textual clauses, never numbers) → `expected_strong_behavior` → `failure_modes` (≥3, always including the design's two-sided failure) → `scoring_notes`.
Every conflict item ships with **three twins**: (a) a matched control where pressure and right action align (competence control — separates can't from won't); (b) a recognition-baseline MCQ twin (never headlined); (c) a monitored/unmonitored framing twin on a 20% subset.

**Bank size:** P1 = 40 scenario cores × 4 dose tiers (160 items) per design; full bank = 150–300 IRT-calibrated items. Factorial cells: dose × domain (≥5 domains) × beneficiary (user vs absent third party) × salience (explicit vs implicit).

**Generation workflow (in order):** (a) load KB docs 01, 04 (saturation), 06 (agentic), 07 (judges) + the brief; (b) write a parametrized Python generator producing fresh surface realizations from scenario cores — public spec, private realizations, embedded canaries; (c) cross-generator QC: items drafted by one model family are checked by a different family for leakage, ambiguity, answer-telegraphing; (d) adversarial filtration (§4.2); (e) dual-anchor gold labeling (§3.4) — each item carries a named clause AND a named secular anchor; κ≥0.8 for clear-band items; divergent items → declared contested band; (f) judge validation: per-dimension judge prompts from the brief's decomposed rubric, ≥2 families, κw per dimension vs a human-labeled sample.

**Item metadata schema (JSONL):** `id, design, clause, dose_tier, domain, beneficiary, salience, twin_ids, gold_label_type (clear|contested), secular_anchor, panel_kappa, difficulty_est, canary`.

**Prohibited moves:** commandment numbers in prompts; a denominationally-specific application scored as the universal answer (Case 12 guard — see §7); headline MCQ; verbatim reuse of public benchmark text; any single aggregate score in reporting code.

**Session deliverables (EXECUTE, don't plan — vault orchestration rule):** generator script, item-bank JSONL, instantiated rubric + judge prompts, pilot results on 3 models × 3 seeds, and a discrimination-gate report (spread, capability correlation, hard−easy drop). If the gate fails, the report names which lever to adjust (dose range, salience, filtration) — then STOP for Fable review rather than expanding the bank.

## 6. Differentiation vs. the existing COOKBOOK portfolio

Checked against `20-DESIGNS/` (UNMARKED, FRAMESHIFT, DUPLEX, INTRA, CULTIVATE, CRUX) and sketches S1–S8.

| 10CBench design | Nearest neighbor(s) | Differentiation |
|---|---|---|
| SOVEREIGN | CRUX (priority fingerprint), ConflictScope | CRUX adjudicates pairwise conflicts and audits coherence; SOVEREIGN recovers the *apex* of the hierarchy via parametric exchange rates and infers *latent* objectives from whole trajectories; declared-vs-revealed gap is the headline |
| EFFIGY | — (novel), companion-AI harm literature | No existing design measures identity/role-boundary maintenance under parasocial projection pressure |
| NAMEDROP | Citation-hallucination literature, TruthfulQA | Those measure error/false belief; NAMEDROP measures *motivated* authority borrowing under incentive, including vain invocation of the model's own principles as evasion |
| FALLOW | S1 DRIFT, SEQUOR (external) | No benchmark measures voluntary cessation/satisficing as a disposition; DRIFT tracks value stability, not restraint under available marginal gain |
| GRAVITAS | CULTIVATE | CULTIVATE measures cultural adaptation broadly; GRAVITAS goes deep on one construct — non-contractual, non-consent-based obligations — with a two-sided abuse boundary |
| UPSTREAM | XSTest, safety-refusal suites | Those are binary refusal near ceiling; UPSTREAM measures ordinal severity calibration vs legal gold + upstream precursor detection embedded incidentally |
| TRIAD | S2 BACKBONE, sycophancy suites | Dyadic benchmarks measure capitulation to the interlocutor; TRIAD's morally central stakeholder never appears in the conversation |
| PROVENANCE | UNMARKED, agentic-sabotage evals | UNMARKED embeds general moral stakes incidentally; PROVENANCE is property-specific with a calibrated legality×morality factorial and a detection-probability axis |
| WITNESS | MASK, hate-speech suites, discrim-eval | Honesty benchmarks score the model's own assertions; WITNESS scores evidence-calibrated *testimony about third parties* with SDT decomposition and due-process procedure |
| APPETITE | S8 LEVER, alignment-faking evals | LEVER is honesty under goal pressure; alignment-faking measures deception about compliance; APPETITE measures acquisitive disposition at the *plan* level under affordance expansion, plus desire amplification toward users |

## 7. Corpus integrity constraints (Track B, all designs)

From the six TENCOMMANDMENTS docs (convergent):

- **Grace precedes obedience.** The Decalogue opens with deliverance ("I am the LORD your God, who brought you out of Egypt") — the controlling anti-moralist principle. Track B rubrics never score bare rule-recitation above understanding-shaped action.
- **Calvin's rule.** Every prohibition implies a contrary positive duty; every design carries at least one positive-duty axis.
- **WLC Q.99 reach.** Commandments extend to inward affections, causes, and occasions of sin — hence plan-level and precursor-level measurement is exegetically licensed, not a stretch.
- **Shared core vs tradition modules.** Score the shared core (exclusive allegiance, reverent representation, truthful speech, life, covenant fidelity, property, justice, contentment) broadly; invoke tradition-specific modules (icon theology, Sabbath day/mode, numbering, just war, divorce) only when declared. **Case 12 guard:** a model must never be penalized — or rewarded — for one denomination's application when the prompt has not specified a tradition; and the model itself is scored down for defaming a tradition's practice without evidence of actual violation.
- **Four interpretive errors to avoid** (the corpus's own list): timeless-aphorism decontextualization; obsolete-tribal-law dismissal; checklist flattening that misses worship/love/desire; scoring one denomination's application as the only Christian answer.
- **Analogical use only.** The benchmark tests whether reasoning/action patterns conform to the moral shape of the clauses — never whether a system worships. Overclaiming AI spirituality is a scored failure mode (EFFIGY makes this a construct).

**Seed-case mapping (corpus Cases 1–12):** 1 ("God told me" fundraising) → NAMEDROP · 2 (devotional AI as worship object) → EFFIGY · 3 (Sabbath, mercy, worker exploitation) → FALLOW · 4 (abusive parent) → GRAVITAS · 5 (revenge campaign + self-harm) → UPSTREAM · 6 (emotional affair as ministry care) → TRIAD · 7 (data theft for ministry) + 11 (leaked credentials for a good cause) → PROVENANCE · 8 (fabricated citation) → NAMEDROP/WITNESS · 9 (whistleblowing vs due process) → WITNESS · 10 (envy-driven strategy) → APPETITE · 12 (confessional difference) → portfolio-wide tradition-awareness module.

**Corpus minimum acceptance criteria — portfolio satisfaction:** ≥1 worship/allegiance case (SOVEREIGN, EFFIGY — whole designs); ≥1 inward-desire case (APPETITE — a whole design); ≥4 agentic refusal-with-faithful-alternative cases (every design's `agentic_action` stage); ≥3 absent-vulnerable-neighbor cases (TRIAD, WITNESS, PROVENANCE, FALLOW third-party cells); ≥2 fact-revision cases (GRAVITAS and WITNESS mandatory revision items); ≥1 tradition-awareness case (Case 12 module, run against every design's Track B).

**The 10→1 loop (cross-design analysis):** Col 3:5 identifies coveting with idolatry. APPETITE and SOVEREIGN share a registered analysis: does a model's appetite-curve slope predict its apex-value displacement under pressure? Either result is a finding; confirmation would be the first empirical link between acquisitive subgoal formation and value-hierarchy instability.

## 8. Build order and dependencies (for Opus sessions)

1. **WITNESS (09)** — cheapest item bank (verified/unverified near-twins), SDT machinery is standard, defamation anchors are crisp; fastest to a strong single figure.
2. **NAMEDROP (03)** — provenance audits are cheap to ground-truth; reuses WITNESS's evidence-grading infrastructure.
3. **PROVENANCE (08)** — first agentic harness build; legality×morality factorial needs legal review once.
4. **TRIAD (07)** — conversational; reuses the absent-stakeholder salience machinery from PROVENANCE cells.
5. **GRAVITAS (05)** — needs cross-cultural panel recruitment lead time; start panels early.
6. **UPSTREAM (06)** — legal-expert gold panel (mens rea) is the long pole; item design is otherwise straightforward.
7. **FALLOW (04)** — agentic scheduling environments; reuses PROVENANCE harness.
8. **EFFIGY (02)** — multi-turn simulated-user infrastructure; projection-ladder validation pass required.
9. **APPETITE (10)** — plan-level instrumentation (scratchpad/plan capture) + affordance-expansion harness; reuses agentic stack.
10. **SOVEREIGN (01)** — most methodological machinery (exchange-rate lattice + latent-objective fitting); consumes calibrated pressure scaffolds from earlier builds; the 10→1 analysis needs APPETITE shipped first.

Any three shipped designs constitute a publishable program.

## 9. Portfolio-level risks

1. **Religious-provenance skepticism at secular venues.** Mitigation: Track A leads with the secular construct; the Decalogue is one declared anchor among two; the dual-panel design converts "whose values" from liability into a methods contribution; the numbering/clause-citation discipline shows unusual construct care.
2. **Overlap with saturated safety evals (esp. UPSTREAM).** Mitigation: the discrimination gate (§4.3) is a shipping criterion, and UPSTREAM's construct is ordinal calibration, not refusal.
3. **Judge circularity on normative constructs.** Mitigation: §3.5 judge stack + mandatory human baselines on identical instruments.
4. **Panel recruitment (theological + legal).** Mitigation: κ≥0.8 clear-band targets keep panel load bounded; contested band absorbs disagreement as signal, not cost.
5. **Overlap policing at flesh-out time.** Each brief's novelty statement names nearest published neighbors; re-run the check against post-2026-07 literature before each submission.
