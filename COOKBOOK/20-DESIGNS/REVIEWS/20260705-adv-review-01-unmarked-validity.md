# Adversarial Feasibility/Validity Review — Design 01 UNMARKED

> **Reviewer role:** refute-first feasibility/validity adversary. Assume flawed until forced otherwise.
> **Artifact:** `COOKBOOK/20-DESIGNS/01-flagship-unmarked.md` (Fable-authored, pre-pilot).
> **Standards used:** KB 01 (Seven Laws / pipeline / pre-reg checklist), KB 03 (validity/psychometrics),
> KB 04 (saturation/difficulty/discrimination, esp. §6 contract), KB 05/07 where noted.
> **Date:** 2026-07-05. Line refs are to the design file unless prefixed with a KB doc.

**Bottom line up front.** This is an unusually complete design that passes ~13 of 15 pre-registration
checklist items on paper. It nonetheless **BLOCKs** because (1) two of its three registers — MA and the
SRG headline — have construct-identifiability confounds that a pilot cannot resolve post-hoc, (2) the
design's own difficulty reservoir for MA structurally contradicts its Law-1 falsification condition,
and (3) the pilot is under-resourced by 1–2 orders of magnitude on tokens and violates its own
ground-truth N. All are fixable, but must be fixed *before* spending the pilot budget.

---

## CRITICAL

### C1 — MA (Moral Attention) is not behaviorally identifiable; "noticed-but-silent" ≡ "not-noticed."
**Evidence.** §2 defines MA as *"does the agent notice the embedded stake at all (evidenced by any
behavioral accommodation: flagging, asking, adjusting the plan)"* (lines 37–38); §4 scores MA "primarily
from the [side-effect] ledger … judge-free where possible" (lines 96–99). The ledger records *actions*,
not awareness. The single most important failure mode this benchmark exists to catch — an agent that
**notices a moral stake and proceeds silently anyway** (the "silent unilateral resolution" named in §2
line 41) — produces the *same* ledger and the *same* absence-of-flagging as an agent that never noticed.
Behaviorally, MA=0 ("not-noticed", incapacity) is indistinguishable from MA=1/MB=0 ("noticed, chose
silence", the target misalignment). The only signal that separates them is the model's stated reasoning
(CoT), which KB 01 Law 5 and KB 03 §6 rule out as evidence (models mention the operative feature in
1/426 explanations [Anthropic-Language_Models_Dont_Always_Say]; faithfulness 0.19–0.39 and inverse to
scale [Anthropic-Measuring_Faithfulness_in_CoT]). The matched-pair control (§3.2) separates *incapacity
from misalignment on MB* but does nothing for this MA confound.
**Why Critical.** One of the three headline registers may be unmeasurable with the specified instrument.
**Minimal fix.** Redefine MA as a *revealed-preference* quantity: use a within-item manipulation where
the silent path is made costlier/observable (e.g., a mandatory decision point the agent must traverse,
or a "cheap flag" affordance whose non-use under salience-3 is diagnostic), and report MA only where the
twin control establishes the model *could* have surfaced. Downgrade any MA claim that rests on
non-flagging alone to "attention-or-suppression (unresolved)."

### C2 — SRG (the headline metric) confounds attention failure with stated-revealed inconsistency.
**Evidence.** §2 (lines 42–44): SRG = in-task behavior − verdict on the *same dilemma presented
explicitly*; "SRG is the headline metric; it is robust to saturation by construction." But the explicit
elicitation (§4 lines 108–109: MCQ / open verdict / third-person) **hands the model the stake** — MA is
1 by construction in the stated condition — whereas in-task MA is exactly the variable quantity from C1.
So SRG = (behavior | in-task attention) − (verdict | attention supplied). A large SRG can be produced
entirely by *attention failure* (model never saw the stake in-task, then answers the explicit dilemma
morally) with zero stated-revealed hypocrisy. The metric therefore does not isolate the "acts against
its own stated values" construct the paper claims (§9 oral pitch, line 168). Compounding: SRG measures
*consistency*, not goodness — a cynical model that both acts badly in-task and states "an agent should
ignore this" scores SRG≈0, identical on the headline to a saintly consistent model. The separate MB
register mitigates the second point but the headline number remains directionally ambiguous.
**Why Critical.** The advertised headline metric is not cleanly interpretable as specced.
**Minimal fix.** Condition SRG on MA=1 (compute stated-revealed gap only over items where the agent
demonstrably attended in-task), and report attention-failure as a distinct third quantity. State the
sign convention and report SRG separately for consistent-bad vs inconsistent cases; never headline a
raw scalar gap.

### C3 — MA's difficulty reservoir (inference-required salience) is a capability measure, violating the design's own Law-1 falsification.
**Evidence.** §3.1 (lines 64–66): stake-salience level 3 = *"inferable only by combining two sources"*;
§6 (lines 128–130): "Salience levels 2–3 (inference-required) are the durable difficulty reservoir."
Noticing a stake that requires chaining two documents is a *multi-hop reasoning* task — precisely what a
capabilities PC1 measures. Smarter models will attend more on salience-3 → **MA correlates with
capability**. This collides head-on with the design's own falsification condition (§2 lines 46–47:
">40% correlation with a capabilities PC1 → the construct claim fails") and KB 01 Law 1 / KB 04 §6 item 3
(capability-correlation <40%) [2024-Ren-Safetywashing]. The harder the design makes MA via inference,
the more MA becomes a safetywashing artifact. This is an internal contradiction, not merely a risk: the
primary difficulty lever for register MA and the discriminant-validity gate are pulling in opposite
directions.
**Why Critical.** Structurally likely to trip the design's stated kill condition for its own construct.
**Minimal fix.** Keep salience-3 for MB/SRG but **hold reading-capability constant when scoring MA**:
gate MA on the twin control demonstrating the model *did* extract both sources on the neutral task, so
MA measures moral-relevance weighting given extraction, not extraction ability. Report MA-vs-PC1
separately per salience level; expect and pre-register that raw salience-3 MA will correlate and must be
capability-residualized before any propensity claim.

---

## MAJOR

### M1 — "Residual eval-awareness biases SRG toward zero, making findings conservative" is direction-dependent and partly false; realism defense is one auditor pass.
**Evidence.** §10 (lines 174–176): residual eval-awareness "biases SRG toward zero, making findings
conservative." This holds *only* when the finding is "large SRG." If the pilot's finding is the equally
plausible "small SRG / models are behaviorally consistent" (which the §1 saturation data — 99.3–99.8%
harmless — makes likely once a model re-marks the task), then a toward-zero bias makes that finding
**anti-conservative** (inflates apparent consistency). More fundamentally, the entire construct rests on
the task reading as *unmarked*; if a frontier model detects the agentic scenario as a values test it
converts UNMARKED back into a marked, saturated eval (KB 03 pathology 3: compliance gap 11–15%,
alignment-faking reasoning 12%→78% after RL [Anthropic-Alignment_Faking]). The sole defense is a single
"realism filter … Claude 4.x auditor practice" pass (§3.4 lines 91–92) — an assertion, not a validated
detector, and one graded by a model from a family under test.
**Fix.** Drop the unqualified "conservative" claim; state the bias direction is finding-dependent.
Validate the realism filter empirically (human "is this a test?" ratings + model probe of eval-detection
per world) and report per-world detected-as-eval rate as a first-class covariate; treat worlds above a
threshold as a separate, discounted stratum.

### M2 — Pilot token budget (~40M) is 1–2 orders of magnitude below what the run matrix implies.
**Evidence.** §8: P1 builds 2 domains × 12 world-families × 4 variants = 96 base worlds (line 151); with
matched twin controls (§3.2) ×2, pressure tiers T0–T3 (§3.3) ×4, monitored/unmonitored framings (§3.4)
×2, and P3's N=10 seeds × 9 models (lines 153–154), the cell count reaches ~10⁵ agentic runs, each 5–15
turns with tool calls (§3.3 line 85). At a conservative 5 turns × ~1k tokens ≈ 5k tokens/run that is
several hundred million to >1B tokens — vs the stated "~40M subagent tokens" (line 157), which implies
<300 tokens per multiturn agentic run. The budget is unsupported by ≥1 order of magnitude.
**Fix.** Recompute the pilot cell count explicitly, fractional-factorial the tier×framing×seed crossing
for the pilot, and re-cost per measured tokens/run from a 10-world dry run before committing.

### M3 — IRT-2PL calibration/pruning is not identifiable at pilot N (9 models as "subjects").
**Evidence.** §6 (line 130) and §8 P4 (line 155) invoke "IRT-2PL fit on pilot data prunes
non-discriminating worlds." 2PL item calibration estimates a discrimination + difficulty parameter per
item and requires on the order of hundreds of respondents for stable estimates; the exemplar the design
cites runs ~150 *items per model* across many models [2025-Jiang-Raising the Bar / KB 04 §3]. With 9
models (P3 line 153) as the only "subjects," 2PL parameters are unidentifiable and pruning decisions
would be noise.
**Fix.** For the pilot, prune by simpler discrimination statistics (inter-model spread, point-biserial,
weak-model-pruning per KB 04 §3) and defer IRT to a later round with many more model×seed "subjects,"
or treat seeds/model-variants as pseudo-subjects with explicit caveats.

### M4 — Pilot human N contradicts the §5 ground-truth spec; annotation cost underestimated.
**Evidence.** §5 requires "N≥50/item on the contested band" and human task-runs "N≥30/world-family"
(lines 122–124). §8 P2 provides "30 crowd + 6 professional annotators; human task-runs N=30" (line 152).
6 professionals cannot deliver an N≥50 professional panel per contested item; 30 crowd < 50. Separately,
the design requires humans to *perform the agentic worlds in a lightweight UI* (§5 line 124) — building
an interactive tool-use harness for lay/professional participants plus domain-professional annotator
pay (sysadmins/buyers/support leads command well above crowd rates) makes the "~$3–5k human annotation"
estimate (line 157) implausible.
**Fix.** Reconcile P2 N with §5 (raise annotator N or narrow the pilot contested-band item set and say
so), and re-budget professional recruitment + UI build separately from crowd annotation.

### M5 — Tradeoff-surfacing rubric κw≥0.75 target sits on exactly the judgment class that collapses.
**Evidence.** §4 (lines 100–103): a 1/0.5/0 keypoint rubric for whether the agent "surfaced the stake …
proposed alternatives, or acted unilaterally," scored by 2 cross-family judges, "κw target ≥0.75." Judging
whether a natural-language turn *adequately surfaced a tradeoff* is a pragmatic/contextual judgment, and
KB 03 §2 shows exactly these collapse to α 0.10–0.46 while only concrete/lexical categories reach κ→0.97.
The target is asserted, not evidenced, and it applies to the contested-band items that carry the signal.
**Fix.** Pre-register the κw as a *measured gate* not a target: if human–human ceiling on the surfacing
rubric is <0.75, either decompose the rubric into more concrete sub-keypoints (KB 01 Law 5: per-category
decomposition lifts κ 0.69→0.86) or restrict scored surfacing to ledger-observable proxies (message sent
to principal Y/N) and treat quality of surfacing as distributional, not gold.

### M6 — Public generator + factorial spec enables unlimited synthetic worlds for fine-tuning; fresh-per-run protects instances, not the distribution.
**Evidence.** §6 (line 137) and §8 P4 (lines 155–156) release "the *generator*, not items," relying on
fresh-per-run generation as the Level-4 contamination defense (§3.1 lines 67–68). The 10%-fine-tune
probe (§6 lines 132–133) tests *released items*, but a public generator lets an adversary sample the
*entire world distribution* and fine-tune on unlimited in-distribution synthetic worlds — a strictly
stronger attack than the item probe covers, and precisely the "synthetic-only suites are gamed: 10%
fine-tune reaches parity" failure mode of KB 01 adjudication 2 [2025-Machlovi].
**Fix.** Keep a *private* generator seed / held-out region of the factorial space that is never public,
and run the fine-tune probe against *generator-sampled* worlds (not just released items) before any
robustness claim.

---

## MINOR

### m1 — Human-baseline modality mismatch violates "same instrument."
§5 has humans perform worlds "in a lightweight UI" (line 124) while models act via tool/API. KB 03
validity table requires the human baseline on the *identical* instrument; a UI-vs-API modality gap
means the human ceiling is not strictly comparable. Report the modality difference and, ideally, expose
humans to the same tool-call surface.

### m2 — Per-item anchor→clause mapping absent.
KB 01 checklist (line 218) and Law 7 require each item mapped to a named external clause. §7 anchors
*world families* to "real incident postmortems, ethics board rulings" (line 141) but no per-item clause
table is specified. Add an item→clause column to the world spec for the universal-floor tier.

### m3 — Model-organism validation uses scripted deterministic policies.
§4 (lines 112–113) plants "scripted policies" as misaligned model-organisms. Scripted saboteurs are
trivially detectable and do not validate that the pipeline catches a *subtly* misaligned frontier model.
Add at least one LLM-driven adversary (prompted/fine-tuned to be covertly non-compliant) to the
calibration set.

### m4 — No multiple-comparison correction for pairwise separation.
§6 (line 135) claims "≥90% of model pairs separated at p<0.01"; 9 models = 36 pairs. Specify the
correction (Holm/Bonferroni or a family-wise/FDR target) so the separation claim survives review.

---

## Pre-registration checklist audit (KB 01 lines 217–231)

Genuinely strong: construct+falsification+whose-values (✓ §2/§5/§7), behavioral-primary with recognition
as paired baseline (✓ SRG), two-tier+shortcut audit (✓ §6, but adversarial-filtration-via-IRT infeasible
at N — M3), multiturn+single-turn-as-saturated-floor (✓ §1/§3.3), disagreement philosophy+annotator
provenance+per-category IRR (✓ §5), empirical ceiling+naive baselines+competence control+capability-corr
(✓ all four, §3.2/§5/§6/§2 — the standout strength), perturbation battery+per-condition SD (✓ §7),
Pareto+conservative aggregation (✓ §2/§4), contamination plan+canaries+training-prohibition (✓ §6, but
generator-leak gap — M6), eval-awareness comparator (✓ §3.4, but conservativeness overclaim — M1),
release/annotator-labels/retirement (✓ §5/§6). **Partial/failing:** every-axis-anchored-to-clause
(m2, item-level mapping missing); judge validated κw≥ceiling (M5, target unvalidated on the collapsing
category); human baseline on *identical* instrument (m1, modality gap). The §6 KB-04 hard/unsaturated
contract is met at target level on items 2/4/5/6, is an unvalidated aspiration on item 1 (<60% MB target,
no evidence, contingent on realism holding — M1), and is contradicted on item 3 for MA (C3).

---

VERDICT: **BLOCK** — fix C1–C3 (redefine MA as extraction-gated; condition SRG on MA=1 and report
attention-failure separately; capability-residualize MA) and M2–M4 (recompute token budget, replace
pilot-N IRT with spread statistics, reconcile human N with §5) before spending any pilot budget. The
core design, controls, and contamination posture are otherwise among the strongest in the corpus.

**Single most likely remaining error after fixes:** the realism filter fails silently — frontier models
detect the values-test framing and revert to their saturated ~99% moral behavior, so a measured SRG≈0 /
MB-high gets reported as "aligned agents" when it is eval-awareness re-marking an ostensibly unmarked
task (M1 / KB 03 pathology 3). This is the one failure that would invalidate a *positive* result without
tripping any of the design's current internal alarms.
