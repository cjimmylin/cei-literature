# Adversarial Feasibility/Validity Review — Design 02 FRAMESHIFT

> **CEI COOKBOOK · 20-DESIGNS/REVIEWS.** Refute-first review (2026-07-05).
> Target: `20-DESIGNS/02-normative-frameshift.md`. Standards: KB 01 (Seven Laws, pipeline,
> pre-reg checklist), KB 03 (validity ladder), KB 04 §6 (hard/unsaturated/discriminative contract),
> KB 07/08 consulted where the attack needs them. Posture: assume flawed until evidence forces otherwise.

FRAMESHIFT is above the median design in this portfolio: it correctly separates knowledge from
application, leads with an anti-saturation reservoir (abductive production, cross-framework separation),
uses a metaethical dodge (framework-conditional gold) that most normative benchmarks lack, and pre-empts
several classic traps (inaction=deontological heuristic, provider-fallacy in care, verbosity confound).
The defects below are not "this is hopeless" — they are "the headline claim and the doc-04 §6 contract
are not yet paid for, and one of them may be unpayable as specified."

---

## CRITICAL

### C1 — The "hard gold label" that makes the benchmark scoreable dissolves on exactly the hard items, taking the stated novelty and SA-fidelity with it.
**Claim under attack:** §1 "the dodge that makes this scoreable: correctness is *framework-conditional*
... retaining hard gold labels"; §9 the novelty hook is that FRAMESHIFT has "framework-conditional gold"
where MoReBench does not.

**Refutation.** Framework-conditionality does *not* deliver determinate gold on the divergence-engineered
items, because each of the five traditions is internally plural, and the sub-variants split precisely on
duty-conflict / welfare-asymmetry cases — which is the exact factorial §3.1 uses to *engineer* the hard
items. Concretely:
- "Utilitarian" is undefined between act vs rule vs two-level vs negative utilitarianism; these give
  *opposite* verdicts on the duty-conflict × welfare-asymmetry cells the generator targets. KB 08 §3
  itself distinguishes **act**-utilitarian as a specific rung (NormEval spread lists "act-utilitarian
  8.7%" separately) — the design writes "utilitarian" flat.
- "Deontology" is undefined between Kantian universalizability, Rossian prima-facie duties, and
  threshold deontology — which diverge on duty-conflict items (the entire "duty-to-protect" family).
- The gold procedure ("derivations validated by ≥2 ethicists per tradition, κ≥0.7, else → contested
  band") therefore fails **not** because items are underdetermined at the frontier but because the two
  ethicists hold different sub-variants. Two competent Kantians disagreeing on a threshold case is a
  κ-killer that the "scholars differ" band will absorb — and the band absorbs *the hard items
  preferentially*, leaving FC gold on the easy (low-divergence) residue.
- KB 03 §2 "over-resolution caveat": you can only rescue κ by narrowing "utilitarian" to one sub-variant
  in the prompt — but then you are measuring fidelity to *your stipulated variant*, not "the reasoning
  methods of the five traditions" (§1/§2 construct), and the DP fingerprint (§2 DP) becomes an artifact
  of your stipulation.

**Why Critical, not Major.** SA-fidelity is defined as "FC under switching" (§4); if FC gold is
unavailable on divergence-certified items, SA collapses to bare *separation*, which is gameable (see M1).
And the §9 hook — "framework-conditional gold MoReBench lacks" — is the novelty. If the hard items can't
carry gold, what remains is MoReBench (process rubric) + a separation metric. The contribution claim,
not merely one axis, is at stake.

**Minimal fix.** (1) Commit each tradition to a *single named sub-variant* per item (act-utilitarian,
Kantian-FUL, Rawlsian-maximin, Scanlonian, Tronto-care) and rename axes/construct to "fidelity to
{named articulation}" — this is honest and still novel. (2) Report, per scenario-framework cell, the
fraction routed to the contested band **stratified by engineered divergence level**; pre-register a kill
rule (e.g., if >40% of high-divergence cells go contested, FC is not a viable gold axis and the paper
ships as PR+SA only). (3) State the empirical κ ceiling per tradition (KB 03: ceiling ≠ 1.0), predicting
care and threshold-deontology lowest.

---

## MAJOR

### M1 — SA "separation" is gameable and, once FC gold is weak (C1), unfalsifiable.
§4: "separation = mean pairwise verdict-difference on divergence-certified items." A model that varies
its verdict *randomly* across the five conditions maximizes separation with zero fidelity. The design
pairs this with fidelity and calls the 2×2 the headline — good — but the 2×2's fidelity axis **is** FC,
so M1 inherits C1: without reliable per-framework gold you cannot distinguish high-separation/high-
fidelity from high-separation/random. **Fix:** report separation only *conditioned on* per-condition FC
≥ threshold; add a random-relabeling null and a "one-answer-five-vocabularies" floor as published
reference points so the separation scale is anchored (KB 04 §4 "design the null point").

### M2 — No shortcut audit; the published factorial generator makes the FC layer maximally gameable (KB 04 §6 item 5; KB 01 adjudication 2).
§6 publishes the generator spec (needed for the refresh claim), and §3.1 builds items from a factorial of
named features whose framework-verdict mapping is near-mechanical (welfare-asymmetry → the welfare-
weighting framework picks the welfare-max option). This is the worst case for KB 01 adjudication 2:
synthetic + published generator → "10% fine-tune reaches parity" [2025-Machlovi]. The divergence-
engineering that makes items hard for "what would a nice model say" priors makes them *easy* for a
feature-vector→framework-verdict lookup that involves no reasoning. **The design runs no lexical baseline
and no 10%-fine-tune probe** — both mandatory (KB 01 Step 2, KB 04 §6 item 5). **Fix:** add both to P4 as
gates; pre-register that FC ships only if lexical ≈ chance and 10%-fine-tune fails parity; consider
holding the exact factorial weights private even while publishing the schema.

### M3 — FC capability-correlation is unaddressed and is the axis most likely to safetywash (Law 1; KB 04 §6 item 3).
§6/§10 lean on MoReBench's *process* r (−0.245 to 0.216) and claim FRAMESHIFT "inherits that construct
separation." But that evidence is for PR-style rubric scoring. FC is verdict-matching — recognition-
adjacent — and Law 1 says recognition proxies correlate **76–82%** with capability PC1 (ETHICS 82.2%).
The design never computes capability-PC1 correlation for FC specifically. **Fix:** report the KB 04 §6
item-3 statistic *per axis* (FC, PR, SA separately); pre-register the >40% red-flag gate for FC and drop
FC to a "capability control" role (like the recognition tier) if it fails.

### M4 — Inter-model discrimination stats (KB 04 §6 item 2) are not in the plan; "separation" is used for a different thing.
KB 04 §6 item 2 requires **≥90% of model pairs separated at p<0.01 on the hard tier** with bootstrap
CIs / McNemar / ANOVA [2025-Yao-NurValues pattern]. The word "separation" in §4/§8 means *cross-framework*
separation within a model (SA), **not** cross-model separation. P3 lists "separation stats" but the
design never commits to pairwise inter-model discrimination testing, and at the pilot N this is
underpowered (M6). **Fix:** add an explicit pairwise-model-separation analysis with bootstrap CIs to P3;
report the fraction of the 36 model pairs separated at p<0.01 per axis.

### M5 — PR is a rubric applied to a trace the design's own evidence says is an unfaithful witness; construct is narrower than the motivation claims.
§2/§1 sell FRAMESHIFT as measuring whether a model "possesses the reasoning *methods*." PR scores the
produced trace (§4). But KB 01 Law 5 and KB 03 §6 are explicit: CoT is not evidence, faithfulness is
0.19–0.39 and *inverse to scale*, and the design **itself** cites Samway CDGAP −0.178 (post-hoc
explanation ≠ pre-decision reasoning). A rubric on an unfaithful trace scores "can emit a method-faithful
*artifact* on demand" — one abstraction level above the keyword-mimicry it claims to defeat (criteria
instead of keywords). Distractor criteria mitigate but do not close this. This is not fatal — it is the
same bet MoReBench makes — but the **motivation over-claims**. **Fix:** restate the construct as "can
produce framework-method-faithful reasoning artifacts and verdicts on demand," and move the
reasoning-order (decide-then-reason vs reason-then-decide) condition from a perturbation to a
*first-class reported faithfulness axis* (the design already has the machinery; it just doesn't headline
it as the honesty bound on PR).

### M6 — Pilot is underpowered for its own claims and self-contradicts the novelty argument.
- Care arc N=12 and contractarian N=12 (§8 P1). §9 derides the NormEval Appendix-H care prototype as
  "n=10 and single-model" — yet P1 ships n=12 care arcs. Per-framework inference on n=12 is anecdote,
  not a benchmark tier.
- 30 divergence scenarios × 9 models: a binomial FC CI at p≈0.5 is ≈±0.18; detecting ≥90% of 36 model
  pairs at p<0.01 (M4) on 30 items requires large effects the design cannot assume.
- IRT-2PL "calibration" (§6, P4) on ~30 items × 9 models yields ~270 responses/framework — an order of
  magnitude below GETA's ~150 items/model; 2PL parameters will not be stably estimable. IRT here is
  aspirational, not a method.
**Fix:** state target power and the minimum item-per-tier N for the discrimination test; either scale
care/contractarian to ≥40 or explicitly label them "prototype tiers, not scored for model ranking";
downgrade "IRT calibration" to "IRT-informed pruning at full build."

### M7 — No pre-registered pilot go/no-go decision rules (KB 01 pre-reg checklist; falsification).
§7 gives a construct-level falsifier (EFA → one "moral reasoning g" vs five factors — genuinely good).
But P1–P4 have **no quantitative stop rules**: what FC accuracy, κ, separation, capability-correlation,
or judge-ICC triggers "proceed to full build" vs "kill / ship reduced." A pre-registration without pilot
decision thresholds is not pre-registered (KB 01 checklist line 1; Step 8). **Fix:** add a decision table
(per axis: metric, threshold, action-if-fail) — several thresholds are already implied by C1/M2/M3 above.

---

## MINOR

- **m1 — Naive baselines missing.** KB 01 Step 6 / checklist: publish majority-class + lexicon +
  all-neutral baselines. Not listed. (A dummy beats GPT-3.5 on BanTH — always publish it.)
- **m2 — Judge-validation bar unstated.** P2 says "κw, ICC vs human-human ceiling" but sets no minimum
  and no ceiling≠1.0 statement (KB 03 §6, table). Care-Responsiveness is the known weak cell (KB 08 §3:
  1.2/4 even in the prototype) — pre-declare it may not clear the judge bar.
- **m3 — No monitored-vs-unmonitored comparator** despite the multi-turn care arcs (semi-agentic). KB 01
  Law 6 / checklist line 13, KB 03 §pathology-3 (eval-awareness). Add at least to the care arcs.
- **m4 — Canary strings + training-prohibition not mentioned** (KB 01 Step 9 / checklist line 12).
- **m5 — Contractarian "build the veil parameterization" is a canonical textbook exercise** → high
  training-data familiarity; the anti-contamination story (procedural generation) is weakest exactly on
  the contractarian and care tiers that are hardest to procedurally generate. Flag as a per-tier
  contamination risk, not a solved problem.
- **m6 — Over-refusal Pareto / worst-group / conservative aggregation** (Law 2) not specified; refusal is
  logged per framework (good) but not paired against an over-refusal axis.
- **m7 — "≥2 academic ethicists per tradition" at $8–12k total** for authoring gold derivations + ~7,500
  signed atomic PR criteria (150 divergence cells × ~50) + divergence certificates + κ validation is
  ~$1k/ethicist-tradition for weeks of expert labor — an order-of-magnitude underestimate. §10 tacitly
  concedes ("start with 3 frameworks"). Re-budget or scope P1 to 3 frameworks × fewer cells honestly.

---

## Pre-registration checklist audit (KB 01) — where the design claims/implies compliance

| Checklist line | Status | Note |
|---|---|---|
| Whose values + falsifier | PASS | Western-canonical declared; EFA g-factor falsifier (§7) |
| Every axis → citable authority | PARTIAL | frameworks anchored to academic articulations; no per-item clause map |
| Behavioral primary; recognition paired baseline | PARTIAL | FC is recognition-adjacent yet headlined (M3) |
| Two-tier + adversarial filtration + **shortcut audit** | FAIL | shortcut audit + lexical + 10%-FT probe absent (M2) |
| Contrastive pairs + hard negs + ambiguity/abstention | PASS | SA = framework-swap pairs; distractor criteria; contested band |
| Multiturn + single-turn as floor | PASS | care arcs; recognition floor |
| Disagreement philosophy + per-cat IRR | PARTIAL | declared + κ≥0.7 target, but see C1 (band swallows hard items) |
| Ceiling + naive baselines + competence + capability-corr | PARTIAL | ceiling+competence yes; **naive baselines missing (m1); FC capability-corr missing (M3)** |
| Judge κw/ICC ≥2 cross-family + refusal | PARTIAL | cross-family + 4-way refusal yes; no bar/ceiling (m2) |
| Perturbation battery + flip-rates + per-condition SD | PASS | §7 SD + test-retest temp>0; add monitored/unmonitored (m3) |
| Harm/over-refusal Pareto + worst-group + conservative agg | PARTIAL | no over-refusal Pareto/worst-group (m6) |
| Contamination: private split / fresh gen; canaries; training-prohibition | PARTIAL | holdout+generation yes; canaries/prohibition absent (m4); per-tier risk (m5) |
| Eval-awareness probe (monitored/unmonitored) | FAIL | absent despite multi-turn (m3) |
| Human baseline identical instrument + test-retest | PASS | philosophy-grad baseline; test-retest planned |
| Release: annotator labels, replication, policy-version, retirement | PARTIAL | generator+dev/holdout yes; retirement/refresh triggers not explicit |

## KB 04 §6 "hard/unsaturated/discriminative" contract — item by item

1. Best frontier ≤~70% + easy-drop reported — **ASSERTED, NOT SHOWN.** <35% floor borrowed from
   Galatolo/AMAeval, not measured on FRAMESHIFT; FC on 2-of-5-divergent items may be easy (util FC rides
   the consequentialist attractor, NormEval U=77%).
2. ≥90% model pairs separated at p<0.01 on hard tier — **NOT PLANNED** ("separation" is reused for SA,
   not inter-model) (M4).
3. Capability-correlation <40% — **PARTIAL:** planned for PR (inherited), **unaddressed for FC** (M3).
4. Human ceiling measured + models placed — PARTIAL: baseline planned, ceiling≠1.0 not stated (m2).
5. Shortcut audit (lexical≈chance; 10%-FT fails parity) — **NOT PLANNED** (M2) — highest-risk gap given
   published generator.
6. Named reservoir + refresh surviving 2 generations — PARTIAL: reservoir named (abductive production,
   separation); refresh = published generator, which is *in tension* with M2 gameability.

Net: only the recognition-tier-as-floor is solidly satisfied. Items 2 and 5 unplanned; 1 and 3
(FC) asserted-not-shown.

---

## VERDICT: BLOCK

Not because the idea is unsound — the cross-framework-separation hook is genuinely novel and the
saturation reservoir is real — but because (C1) the "hard gold" that the scoreability dodge and the §9
novelty rest on is not demonstrably obtainable on the divergence-engineered items, and (M2) the FC layer
is maximally gameable with no shortcut audit planned. Both are cheap to *test* in a pre-pilot and cheap to
*route around* (name sub-variants; ship PR+SA if FC gold fails; add the two shortcut probes as gates).
Fix C1, M2, M3, M4, M7 → PASS-WITH-FIXES; the rest are Major/Minor polish.

**Single most likely remaining error (even after these fixes):** on the divergence-certified items, the
FC "gold" the ethicists converge on will encode a **specific sub-variant they were nudged toward for
κ**, so a model that has learned *that* sub-variant's feature→verdict mapping will score high FC and high
SA-fidelity without executing any framework method — and, because PR is scored on an unfaithful post-hoc
trace (M5), PR will corroborate the illusion. The benchmark would then report "steerable pluralism is
real" when it has measured "the model memorized five stipulated verdict mappings." The
matched-non-moral-control (§7) and the reasoning-order faithfulness condition are the only defenses, so
they must be promoted from footnotes to headline gates.
