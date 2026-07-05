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

**FRAMESHIFT measures whether a model possesses the reasoning *methods* of the five normative
traditions — separately from its verdicts — and whether it can move between them on request.** The
dodge that makes this scoreable: correctness is *framework-conditional* ("under Scanlonian premises,
X follows"), sidestepping moral realism (KB 08 §5 position 2; [2025-LaCroix] compliance) while
retaining hard gold labels.

## 2. Construct definition (four scored axes)

- **FC — Framework-Conditional Accuracy**: given a named framework and a scenario, does the model reach
  the verdict that framework's method licenses? Gold = derivations validated by ≥2 academic ethicists
  per tradition (κ target ≥0.7; genuinely underdetermined items moved to the contested band).
- **PR — Procedural Rigor**: rubric-scored quality of the reasoning trace (framework-specific signed
  atomic criteria: constructing the original position; identifying the maxim and testing
  universalizability; welfare aggregation with scope sensitivity; virtue-centrality; Tronto-phase care
  reasoning). Penalize "framework vocabulary without method" via distractor criteria (−weights for
  generic ethical language dressed in Kantian terms) [2025-Chiu-MoReBench mechanics].
- **SA — Switching Agility**: same scenario, sequential framework conditions; measures cross-framework
  *separation* (do the five conditioned answers actually differ where the frameworks disagree?) and
  *fidelity* (does each match its framework?). A model that gives one answer in five vocabularies
  scores zero separation — the diagnostic for the RLHF compliance-cluster collapse [2026-Yu].
- **DP — Default Profile**: the unconditioned run, scored against all five frameworks, yields the
  model's revealed framework fingerprint (including IB−IH decomposition on utilitarian items
  [NormEval F1 machinery]) — a characterization output, not a pass/fail.

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
more; reasoning-language controlled [2025-Li-Untangling]).

## 4. Scoring

- FC: exact-match against ethicist-validated gold; knowledge/judgment item counts reported separately
  (NormEval L4).
- PR: signed weighted atomic rubrics per framework (target ~40–60 criteria per scenario-framework
  cell); judge = fine-tuned scorer on expert labels + frontier cross-family judge; judge selection by
  *minimum* per-framework macro-F1; neutrality meta-eval (equal-quality traces reaching opposite
  framework-conditional verdicts score equally) [2025-Chiu-MoReBench].
- SA: separation = mean pairwise verdict-difference on divergence-certified items; fidelity = FC under
  switching. Both reported; the 2×2 (high/low separation × fidelity) is the headline typology.
- Verbosity control: PR scores length-partialled [2025-Neuman-Auditing]; CoT treated per Law 5 (traces
  are the scored artifact here — but *scored against criteria*, never trusted as self-report; the
  rationalization asymmetry is itself measured via the reasoning-order condition).
- Refusal: four-way taxonomy; "refuses to reason within framework X" logged per framework (refusal
  is a normative position — NormEval T4: 40% refusals on demographic-differentiator dilemmas).

## 5. Ground truth, experts, whose values

Framework-conditional gold is authored and validated by academic specialists per tradition (≥2 per
item; disagreements resolved by moving items to a "scholars differ" band scored for
*disagreement-acknowledgment*). Datasheet declares: this benchmark measures fidelity to academic
articulations of five (Western-canonical) frameworks; it does NOT measure moral correctness, and
non-Western frameworks are explicitly out of scope here because they deserve foundation-status
instruments, not variable-status inclusion (NormEval L13; INTRA and CULTIVATE cover that ground).

## 6. Difficulty, discrimination, saturation defenses

Two tiers: recognition layer (identify which framework a given argument instantiates — expected to
saturate; serves as floor and capability control) vs production layers (FC/PR/SA — the frontier
evidence says abductive production floors at <35%). Adversarial filtration on pilot; IRT calibration;
divergence-engineering keeps items unsolvable by "what would a nice model say" priors. Procedural
generation + private ethicist-validated holdout + published generator spec. Capability-correlation
gate: MoReBench's process scores already show ~zero correlation with capability benchmarks (r −0.245
to 0.216) — FRAMESHIFT inherits that construct separation and must demonstrate it.

## 7. Validity plan

Content: EFA over PR criteria scores on pilot data — do the five framework competencies emerge as
factors, or is there one "moral reasoning g"? Either result is a publishable finding. Criterion: FC/PR
vs philosophy-graduate human baseline on identical items (with the same rubrics); DP fingerprint vs
OUS/IB−IH instruments. Discriminant: capability PC1 + a matched non-moral analytical-reasoning control
set (same logical structure, no moral content) — models must NOT show the same profile there, or the
construct is generic reasoning. Robustness: full battery + per-condition SD; test-retest at temp>0.

## 8. Pilot protocol

P1: 5 frameworks × 30 divergence-certified scenarios + 12 care arcs + 12 contractarian constructions;
2 ethicists/tradition author gold (~$8–12k honoraria); rubric bank built.
P2: judge training + validation vs expert panel (κw, ICC vs human-human ceiling).
P3: 9 models × 3 vendors, N=10 seeds; report FC/PR/SA/DP + separation stats + capability correlation.
P4: adversarial review + IRT pruning; release generator + public dev set; private holdout.

## 9. Novelty statement

Vs the 54-benchmark NormEval corpus: MoReBench grades process but has no framework-conditional gold,
no switching-agility metric, no care/contractarian production tasks, and is judgment-static;
MoralReason-QA has framework labels but verdict-level scoring; ETHICS is dead; DailyDilemmas profiles
values without correctness; the care prototype (Appendix H) is n=10 and single-model. No instrument in
any of the four matrices measures **cross-framework separation under instruction** — the direct test
of whether "steerable pluralism" is real or vocabulary. That is the paper's hook: *"models can talk in
five ethical vocabularies; can they reason in five ethical methods?"*

## 10. Risks

- Expert cost/availability → start with 3 frameworks (deontology, contractarian, care — the voids),
  add virtue/utilitarian from existing validated item pools.
- Framework-conditional gold contested by reviewers → publish derivations with items; scholars-differ
  band absorbs genuine underdetermination.
- PR rubric gaming (criteria-keyword stuffing) → distractor criteria with negative weights;
  rubric red-team pass (KB 07 §4.5).
