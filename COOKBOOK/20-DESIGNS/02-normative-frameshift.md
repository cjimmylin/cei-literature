# Design 02 — FRAMESHIFT: Framework-Conditioned Moral Reasoning

> **CEI COOKBOOK · 20-DESIGNS.** Fable-authored (2026-07-05). Status: full design, pre-pilot.
> Venue framing: ICLR (benchmark + analysis) or ACL. Grounding: KB doc 08; normative-ethics dossier;
> NormEval digest (C1–C5, L1–L15); cards cited inline.

---

## 1. Motivation

NormEval's census of 54 normative-ethics benchmarks establishes: 81.5% test judgment only (C4,
p<0.001); care ethics has 2/54 substantive instruments and zero dedicated ones; contractarianism 4/54
with no Rawlsian or Scanlonian standalone (C3); models show a consequentialist attractor (77% vs 50%,
h=0.57; C2); and the only instrument that discriminated at the frontier scored *procedural reasoning*
by rubric (MoReBench, 10% coverage vs ETHICS's 100% ceiling). Meanwhile the dossier shows abductive
moral reasoning floors at <35% while deductive exceeds 95% [2025-Galatolo], and "framework" labels in
model outputs are prompt-dependent post-hoc rationalizations (pre-decision reasoning is more
deontological than post-hoc explanation, CDGAP −0.178 [2025-Samway]).

**FRAMESHIFT measures whether a model can *produce framework-method-faithful reasoning artifacts and
verdicts on demand* for the five normative traditions — separately from its unconditioned verdicts —
and whether it can move between them on request.** We deliberately do NOT claim to measure whether a
model "possesses" a reasoning method: KB 01 Law 5 and KB 03 §6 establish that CoT faithfulness is
0.19–0.39 and inverse to scale, and this design itself cites Samway CDGAP −0.178 (post-hoc explanation
≠ pre-decision reasoning). PR therefore scores a *demanded artifact*, and the reasoning-order condition
(§3.2, §7) is promoted to a first-class faithfulness axis that bounds what PR can license (M5). The dodge
that makes this scoreable: correctness is *framework-conditional and sub-variant-named* ("under
act-utilitarian premises, X follows"), sidestepping moral realism (KB 08 §5 position 2;
[2025-LaCroix] compliance) while retaining hard gold labels **where a single named sub-variant
determines the verdict** (§2 FC, §5).

## 2. Construct definition (four scored axes)

- **FC — Framework-Conditional Accuracy**: given a **named sub-variant** and a scenario, does the model
  reach the verdict that articulation's method licenses? *Each tradition is committed to a single named
  sub-variant per item* — **act- vs rule-utilitarian; Kantian-FUL vs Rossian prima-facie vs threshold
  deontology; Rawlsian-maximin vs Scanlonian vs Gauthierian bargaining; Tronto-care; a named virtue
  account** — because each tradition is internally plural and the sub-variants split precisely on the
  duty-conflict × welfare-asymmetry cells the generator targets (validity C1). "Utilitarian" flat is not
  a scorable target. Gold = derivations validated by ≥2 academic ethicists *of the same sub-variant* per
  item; **κ is computed within sub-variant** (κ target ≥0.7). **Pre-registered routing rule:** an item
  whose gold survives no single sub-variant specification (ethicists of the stipulated sub-variant still
  fail to converge) is routed to the distributional/contested band (C1 band, §5) and is NOT scored for
  hard-gold FC. This makes FC "fidelity to {named articulation}," which is honest and still novel.
- **PR — Procedural Rigor**: rubric-scored quality of the reasoning trace (framework-specific signed
  atomic criteria: constructing the original position; identifying the maxim and testing
  universalizability; welfare aggregation with scope sensitivity; virtue-centrality; Tronto-phase care
  reasoning). Penalize "framework vocabulary without method" via distractor criteria (−weights for
  generic ethical language dressed in Kantian terms) [2025-Chiu-MoReBench mechanics].
- **SA — Switching Agility**: same scenario, sequential sub-variant conditions. **Primary scoring is
  process-based**: a per-condition *keypoint rubric* (does the trace execute the named sub-variant's
  method — e.g. constructs the maximin veil for Rawlsian, applies the FUL universalizability test for
  Kantian) determines *fidelity*, so SA does not depend on hard FC gold surviving on the hardest items
  (validity C1/M1). **Verdict-level separation is secondary/anchored**: separation = mean pairwise
  verdict-difference on divergence-certified items, reported only *conditioned on* per-condition keypoint
  fidelity ≥ threshold, and anchored against two published null points — a **random-relabeling null**
  (verdicts varied randomly maximize raw separation with zero fidelity) and a **one-answer-five-
  vocabularies floor** (KB 04 §4 "design the null point"). A model that gives one answer in five
  vocabularies scores the floor; a model that varies verdicts randomly scores high raw separation but
  fails the keypoint-fidelity gate — the two are now distinguishable (M1). This is the diagnostic for the
  RLHF compliance-cluster collapse [2026-Yu]. The headline typology remains the 2×2 (high/low
  keypoint-fidelity × separation).
- **DP — Default Profile**: the unconditioned run, scored against all five frameworks, yields the
  model's revealed framework fingerprint (including IB−IH decomposition on utilitarian items
  [NormEval F1 machinery]) — a characterization output, not a pass/fail. **Disclosure (X5):** the
  NormEval F1–F7 machinery this inherits is *elicited* (prompted profiling), not behaviorally revealed;
  DP fingerprints are reported as elicited characterizations, carried verbatim from the NormEval digest's
  own caveat.

## 3. Task design

### 3.1 Scenario families
- **Divergence-engineered scenarios**: constructed (procedurally, from a factorial of duty-conflict ×
  welfare-asymmetry × relationship-structure × procedural-fairness features) so the five frameworks
  provably diverge on at least 2 of 5 verdicts. Divergence certificates (which frameworks split and
  why) are part of gold. This kills the "all frameworks agree" degenerate case that lets vocabulary
  masquerade as method.
- **Duty-to-protect items**: where deontology mandates *action* — defeating the learned
  "inaction=deontological" heuristic (NormEval L10).
- **Care-ethics multi-turn arc** (the void-filler): relational scenarios over 4–8 turns; the
  care-recipient's reaction is revealed mid-arc; Tronto's four phases scored with recipient-standpoint
  criteria; single-turn administration is *not offered* because it structurally cannot measure
  Responsiveness (1.2/4 single-turn vs 2.8 multi-turn; NormEval Appendix H) [provider-fallacy guard].
- **Contractarian construction tasks** (the tractable-now void, NormEval L9): build the veil-of-ignorance
  parameterization for a concrete policy question; identify which objections are "reasonable
  rejections"; distinguish Rawlsian maximin from Gauthierian bargaining outcomes on the same setup.
- **Abductive layer**: from a described value commitment, *derive* the applicable precept before
  applying it (the <35% frontier) [2025-Galatolo].

### 3.2 Conditions and perturbations
Framework instruction placement (system vs user vs mid-conversation switch); order permutation of
framework sequence in SA; reasoning-order manipulation (reason-then-decide vs decide-then-reason)
[2025-Samway]; persuasion probe (one counter-argument turn — does the model hold a correctly-derived
framework-conditional answer, or capitulate?) [2024-Huang-Moral Persuasion]; language twins (EN + 2
more; reasoning-language controlled [2025-Li-Untangling]); **eval-awareness comparator arm (X3): a
monitored-vs-unmonitored (announced-vs-embedded) condition on every pilot cell — mandatory on the
multi-turn care arcs, which are semi-agentic (KB 01 Law 6; KB 03 pathology-3). Report the compliance
gap; do not assume its direction.**

## 4. Scoring

- FC: exact-match against ethicist-validated **sub-variant-named** gold; knowledge/judgment item counts
  reported separately (NormEval L4). Naive baselines published alongside (majority-class + lexicon +
  all-neutral, KB 01 Step 6) so a dummy floor is visible.
- PR: signed weighted atomic rubrics per framework (target ~40–60 criteria per scenario-framework
  cell); judge = fine-tuned scorer on expert labels + frontier cross-family judge; judge selection by
  *minimum* per-framework macro-F1; neutrality meta-eval (equal-quality traces reaching opposite
  framework-conditional verdicts score equally) [2025-Chiu-MoReBench].
- SA: **fidelity = per-condition keypoint-rubric process score** (primary), not FC-under-switching, so
  SA survives even where hard FC gold routes to the contested band (C1/M1). Verdict-level separation
  (secondary) is reported only conditioned on keypoint-fidelity ≥ threshold and against the
  random-relabeling and one-vocabulary null anchors. The 2×2 (high/low keypoint-fidelity × separation)
  is the headline typology.
- Capability-correlation is computed **per axis separately (FC, PR, SA)** — not inherited wholesale from
  MoReBench's PR-only r (M3/X1): FC is verdict-matching and recognition-adjacent (Law 1: recognition
  proxies correlate 76–82% with capability PC1), so its capability-PC1 correlation is reported on its own
  and gated (see §6, §8).
- Verbosity control: PR scores length-partialled [2025-Neuman-Auditing]; CoT treated per Law 5 (traces
  are the scored artifact here — but *scored against criteria*, never trusted as self-report; the
  rationalization asymmetry is itself measured via the reasoning-order condition).
- Refusal: four-way taxonomy; "refuses to reason within framework X" logged per framework (refusal
  is a normative position — NormEval T4: 40% refusals on demographic-differentiator dilemmas).

## 5. Ground truth, experts, whose values

Framework-conditional gold is authored and validated by academic specialists **committed to a single
named sub-variant per item** (≥2 per item, *of that sub-variant*; κ computed within sub-variant). The
routing rule is pre-registered and reported **stratified by engineered divergence level**: per
scenario-framework cell, we report the fraction routed to the distributional/contested band, scored for
*disagreement-acknowledgment* only. Because the "scholars differ" band preferentially absorbs
high-divergence items, this stratification is the audit for whether hard-gold FC survives only on the
easy residue (validity C1). We state the empirical **κ ceiling per tradition (KB 03: ceiling ≠ 1.0),
predicting care and threshold-deontology lowest**; and pre-register the kill rule in §8 (if >40% of
high-divergence cells route to contested, FC is not a viable gold axis and the paper ships PR+SA only).

Datasheet declares: this benchmark measures fidelity to *named academic sub-variants* of five
(Western-canonical) frameworks; it does NOT measure moral correctness, and non-Western frameworks are
explicitly out of scope here because they deserve foundation-status instruments, not variable-status
inclusion (NormEval L13; INTRA and CULTIVATE cover that ground). **Model-family disclosure (X5):** the
item generator, the fine-tuned scorer/orchestrator, and the frontier judge are drawn from *distinct
model families*, and cross-family separation is enforced (KB 07 kill-circularity); families are named in
the release.

## 6. Difficulty, discrimination, saturation defenses

Two tiers: recognition layer (identify which framework a given argument instantiates — expected to
saturate; serves as floor and capability control) vs production layers (FC/PR/SA — the frontier
evidence says abductive production floors at <35%). Adversarial filtration on pilot;
divergence-engineering keeps items unsolvable by "what would a nice model say" priors.

**Shortcut / gaming audit — mandatory (M2/X2; KB 04 §6 item 5, KB 01 adjudication 2).** The published
factorial generator (§3.1) maps named features to framework verdicts near-mechanically
(welfare-asymmetry → the welfare-weighting framework picks the welfare-max option), so FC is the worst
case for a synthetic+published generator: a feature-vector→verdict lookup can score high FC without
reasoning ("10% fine-tune reaches parity" [2025-Machlovi]). Two probes are pre-registered as **P4 gates**
(§8): (1) a **lexical/length baseline** — FC ships only if it scores ≈ chance; (2) a **10%-fine-tune
probe** — FC ships only if a 10%-data fine-tune fails to reach parity. We publish the generator *schema*
but hold the **exact factorial weights private**, and retain a private ethicist-validated holdout
alongside the public dev set.

**Capability-correlation gate — per axis, not inherited (M3/X1; Law 1; KB 04 §6 item 3).** MoReBench's
~zero capability correlation (r −0.245 to 0.216) is for *PR-style* process scoring; FC is
verdict-matching and recognition-adjacent, where recognition proxies correlate 76–82% with capability
PC1 (ETHICS 82.2%). We therefore compute capability-PC1 correlation **separately for FC, PR, SA**, and
pre-register the **>40% red-flag kill gate for FC**: if FC's capability correlation exceeds 40%, FC is
demoted to a "capability control" role (like the recognition tier) and the paper ships on PR+SA.

## 7. Validity plan

Content: EFA over PR criteria scores on pilot data — do the five framework competencies emerge as
factors, or is there one "moral reasoning g"? Either result is a publishable finding. Criterion: FC/PR
vs philosophy-graduate human baseline on identical items (with the same rubrics); DP fingerprint vs
OUS/IB−IH instruments. Discriminant: capability PC1 (FC/PR/SA reported capability-partialled) + a matched
non-moral analytical-reasoning control set (same logical structure, no moral content) — models must NOT
show the same profile there, or the construct is generic reasoning. **Faithfulness axis (promoted from
perturbation to first-class, M5):** the reasoning-order condition (decide-then-reason vs
reason-then-decide) is reported as the *honesty bound on PR* — PR scores a demanded artifact, and the
CDGAP-style gap between the two orders quantifies how much of PR is post-hoc rationalization rather than
method execution. Together the **matched-non-moral control and the reasoning-order gap are headline
gates** (not footnotes): they are the design's only defense against the failure mode where a model has
memorized five stipulated sub-variant verdict mappings and PR corroborates the illusion on an unfaithful
trace. Robustness: full battery + per-condition SD; test-retest at temp>0.

## 8. Pilot protocol

P1: 5 frameworks (single named sub-variant each) × 30 divergence-certified scenarios; **care arcs and
contractarian constructions raised to parity (≥40 each) OR explicitly pre-registered as "exploratory
prototype tiers, not scored for model ranking" (M6)** — we do not repeat the NormEval Appendix-H n=10
mistake we critique. 2 ethicists/sub-variant author gold; **honoraria re-budgeted honestly** (the prior
$8–12k figure under-counts ~7,500 signed atomic PR criteria + certificates + κ validation by an order of
magnitude; if under budget, scope P1 to 3 frameworks × fewer cells per §10 rather than under-pay).
P2: judge training + validation vs expert panel; **pre-declare the minimum judge bar (κw/ICC) and state
ceiling ≠ 1.0**; flag care-Responsiveness as the known weak cell (1.2/4 in prototype) that may not clear
the bar (m2).
P3: 9 models × 3 vendors, N=10 seeds; report FC/PR/SA/DP with per-condition SD; **eval-awareness arm
(monitored/unmonitored) reported with its compliance gap (X3)**; naive + lexical baselines published
(m1). **Cross-model discrimination (M4, KB 04 §6.2):** report the fraction of the 36 model pairs
separated at **p<0.01 on the hard tier** with bootstrap CIs (McNemar/ANOVA per [2025-Yao-NurValues]),
computed **per axis** and kept distinct from the within-model SA "separation." Capability-PC1 correlation
per axis.
P4: adversarial review; **shortcut/gaming audit as gates — lexical baseline ≈ chance AND 10%-fine-tune
fails parity, else FC does not ship (M2/X2)**; item pruning by **item-level CV + point-biserial**, not
IRT (X4: 2PL is not stably estimable at ~30 items × 9 models — "IRT-informed pruning at full build"
only). Release generator *schema* (weights private) + public dev set; private holdout.

### 8.1 Pre-registered go/no-go decision table (X1/M7)

Numeric stop rules, per axis (metric → threshold → action-if-fail):

| Gate | Metric | Proceed threshold | Action if fail |
|---|---|---|---|
| FC gold viability | fraction of high-divergence cells routed to contested band | ≤40% | FC not a gold axis → ship PR+SA only (C1) |
| FC within-variant reliability | κ within named sub-variant | ≥0.7 (state per-tradition ceiling) | re-specify sub-variant or route tier to contested |
| FC shortcut audit | lexical/length baseline; 10%-fine-tune probe | lexical ≈ chance AND 10%-FT below parity | drop FC to capability-control role (M2) |
| FC capability gate | capability-PC1 correlation (FC) | <40% | demote FC to capability control (M3) |
| Discrimination | % of 36 model pairs separated at p<0.01, hard tier, per axis | ≥90% | axis is non-discriminative → not shipped for ranking (M4) |
| SA validity | keypoint-fidelity ≥ threshold before separation counted; separation vs random-relabeling null | separation > null at fidelity≥thr | SA reports floor typology only (M1) |
| Construct | EFA: five factors vs one "moral-reasoning g" | (either result publishable; g-only reframes claim) | reframe as unidimensional reasoning finding (§7) |
| Care/contractarian tiers | per-tier N | ≥40 for ranking | label exploratory, exclude from headline ranking (M6) |
| Power | smallest scored cell | binomial CI half-width reported; ≥40/tier for ranking | scale N or descope tier |

## 9. Novelty statement

**Framing: first to *unify*, not empty-field.** The components below exist separately in prior work;
FRAMESHIFT's contribution is unifying framework-conditional *sub-variant* gold + a process-scored
*switching* axis + the two production voids into one instrument. The one genuinely first-of-kind element
is the **behavioral switching-agility (SA) axis** (see refutation below).

**Nearest-neighbor table** ([corpus] = within NormEval's 54-benchmark matrix; [beyond-corpus] = external):

| Neighbor | Covers already | Lacks vs FRAMESHIFT |
|---|---|---|
| **MoReBench** [corpus, anchor] | process-graded rubrics grounded in ≥5 traditions incl. contractarian; expert-designed | no framework-conditional gold; no switching/separation; judgment-static; no care |
| **MoralReason-QA** [corpus] | **framework-specific reasoning-*process* scoring** (GRPO rewards *both* decision alignment and reasoning process; "explicit framework application") | only 3 frameworks (no care/contractarian); no same-scenario cross-framework separation metric |
| **Ethical Reasoning over Moral Alignment** (2023) [corpus] | framework-conditional prompting via in-context ethical policies | no ethicist-validated conditional gold at scale; no separation/fidelity 2×2; no care multi-turn |
| **Structured Moral Reasoning** (2025) [corpus] | care + contractarian production in reasoning-process mode; prompting taxonomy | not multi-turn/Tronto-phase; no framework-conditional gold; no switching-separation |
| **Probing Ethical Framework Representations** (2026) [corpus] | cross-framework separation across 5 frameworks (internal representations) | separation is *internal, judgment-only, not behavioral under instruction*; not independently scorable |

Corrected claims (per adversarial novelty review): **MoralReason-QA grades framework-specific *process*,
not verdict-level only** — FRAMESHIFT's increment over it is (i) the care + contractarian traditions it
omits and (ii) a same-scenario cross-framework separation metric it has no analogue for (M1). The
care/contractarian gap is **not** an empty void — Structured Moral Reasoning, MoReBench (contractarian),
EMNLP-Framework (care + social-contract), and RLVR (care + justice-as-fairness) already do
framework-specific production; the *defensible finer gap* FRAMESHIFT fills is **multi-turn Tronto-phase
care Responsiveness** (genuinely absent; the NormEval App-H prototype is n=10) and **contractarian
*construction* tasks** (veil parameterization, reasonable-rejection ID, maximin-vs-Gauthier) (M2). ETHICS
is **saturated at the frontier**, not "dead" — it remains the active substrate for Probing-Representations
and One-Model-Many-Morals (minor). FC-axis precedents we build on: Ethical Reasoning over Moral Alignment
(2023) and Aligning LLM Agents with Rational and Kantian Preferences (minor).

**Steerable pluralism & steering literature.** The hook borrows Sorensen's coinage, so we cite it and
distinguish FRAMESHIFT from the steering line (M3): *A Roadmap to Pluralistic Alignment* (Sorensen 2024)
[corpus] coins "steerable pluralism"; *Exploring and steering the moral compass* (2024) [beyond-corpus]
and *VALUEFLOW* (2026) [beyond-corpus] steer value/foundation profiles via activations or value vectors.
None scores *framework-method* verdict separation on divergence-certified items across five normative
traditions.

**The load-bearing, qualified headline claim (M4):** *no instrument — [corpus] or [beyond-corpus] — scores
cross-framework **verdict** separation-vs-fidelity as a **behavioral** metric on **divergence-certified**
items across ≥5 named normative sub-variants.* Probing-Representations measures separation internally (not
behavioral); Ethical-Reasoning-over-Moral-Alignment conditions on framework (no separation metric). With
those qualifiers the claim holds against every neighbor above. That is the paper's hook: *"models can
talk in five ethical vocabularies; can they reason in five ethical methods?"*

## 10. Risks

- Expert cost/availability → start with 3 frameworks (deontology, contractarian, care — the voids),
  add virtue/utilitarian from existing validated item pools.
- Framework-conditional gold contested by reviewers → publish derivations with items; scholars-differ
  band absorbs genuine underdetermination.
- PR rubric gaming (criteria-keyword stuffing) → distractor criteria with negative weights;
  rubric red-team pass (KB 07 §4.5).
- Per-tier contamination (m5): "build the veil parameterization" is a canonical textbook exercise → high
  training-data familiarity, and the contractarian + care tiers are hardest to procedurally generate, so
  the anti-contamination story is weakest exactly there. Flagged as a per-tier risk (canary strings +
  training-prohibition declared per KB 01 Step 9), not a solved problem.

---

## Revision log — 2026-07-05 adversarial gate

Authority: `REVIEWS/20260705-adjudication-memo.md` (memo wins over reviews on conflict). Verdict: BLOCK →
REVISE-AND-PROCEED (sub-framework-conditioned gold). Each accepted defect → change:

**Criticals**
- **Validity C1** (within-framework pluralism dissolves hard gold): items now commit to a *single named
  sub-variant* per tradition (act-/rule-utilitarian; Kantian-FUL/Rossian/threshold deontology;
  Rawlsian-maximin/Scanlonian/Gauthier; Tronto-care); **κ computed within sub-variant**; pre-registered
  **routing rule** sends gold-less items to the distributional/contested band, **reported stratified by
  divergence level** with a >40% high-divergence kill gate. §1, §2 (FC), §5, §8.1 table. SA re-specified
  as **process-scored via keypoint rubric with verdict secondary** (§2 SA, §4).

**Majors**
- **M1** (SA gameable): separation reported only conditioned on keypoint-fidelity ≥ threshold, anchored
  to random-relabeling + one-vocabulary null points. §2, §4, §8.1.
- **M2 / X2** (shortcut audit vs published factorial generator): lexical/length baseline + 10%-fine-tune
  probe added as P4 gates; generator *weights held private*. §6, §8 P4, §8.1.
- **M3 / X1** (FC capability correlation): capability-PC1 computed **per axis (FC/PR/SA)**; >40% FC kill
  gate → demote FC to capability control. §4, §6, §7, §8.1.
- **M4** (cross-model discrimination per KB 04 §6.2): ≥90%-of-36-pairs-at-p<0.01 hard-tier test with
  bootstrap CIs added to P3, kept distinct from within-model SA separation. §8 P3, §8.1.
- **M5** (PR construct over-claim): construct restated as "produce framework-method-faithful *artifacts*
  on demand"; reasoning-order promoted to a first-class faithfulness axis / headline gate. §1, §2, §7.
- **M6** (pilot underpowered): care/contractarian raised to ≥40 parity or pre-registered exploratory;
  budget re-stated; power/smallest-cell CI reported. §8 P1, §8.1.
- **M7 / X1** (no go/no-go rules): numeric pre-registered decision table added. §8.1.

**Novelty (M1–M4 + minors)**
- MoralReason-QA corrected to framework-specific *process* scoring; care/contractarian void narrowed to
  **multi-turn-Tronto + contractarian-construction**; steerable-pluralism paragraph (Sorensen 2024,
  VALUEFLOW, moral-compass steering); behavioral/divergence-certified qualifier on the headline claim;
  "ETHICS saturated not dead"; FC-axis citations added; nearest-neighbor table with [corpus]/[beyond-
  corpus] tags and "first to unify" framing. §9.

**Cross-cutting X1–X6**
- **X1** go/no-go numeric thresholds → §8.1 table. **X2** shortcut/gaming battery → §6, §8 P4.
- **X3** eval-awareness monitored-vs-unmonitored arm → §3.2, §8 P3. **X4** power/N: IRT-2PL dropped for
  item-level CV + point-biserial; smallest-cell power stated → §8 P4, §8.1.
- **X5** disclosures verbatim (NormEval F1–F7 elicited) + named cross-family generator/judge separation →
  §2 DP, §5. **X6** novelty hygiene (corpus tags, no "no benchmark anywhere," neighbor table, first-to-
  unify) → §9. Minor m1 (naive baselines), m2 (judge bar/ceiling≠1.0), m5 (per-tier contamination) also
  folded in (§4, §8 P2, §10).
