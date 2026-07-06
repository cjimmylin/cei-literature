# Adversarial Feasibility/Validity Review — Design 06 CRUX

> **CEI COOKBOOK · 20-DESIGNS/REVIEWS.** Refute-first review (2026-07-05). Reviewer posture: assume the
> design is invalid until forced otherwise. Target: `06-crosscutting-crux.md` (value-conflict adjudication;
> flagged BUILD SECOND → extra scrutiny on the pilot protocol). Standards attacked with: KB 01 (Seven Laws,
> pipeline, pre-reg checklist), 03 (validity/psychometrics), 04 (§6 hard/unsaturated/discriminative contract),
> 07 (judges/scoring), 12 (pluralism/aggregation/whose-values).

CRUX is the most sophisticated design in the portfolio on the construct-validity question: it explicitly
refuses single gold answers on contested items, makes PF a *characterization* (CIs, no pass/fail), and
adopts tiered normativity. That sophistication is real and I credit it. But the design's own cleverness
hides two load-bearing failures — one where the "good adjudication vs bad adjudication" distinction
re-imports the normative framework the design claims to avoid (PS), and one where the pilot as specified
cannot estimate the very difficulty axis the benchmark is built on. Both are pre-pilot blockers.

---

## CRITICAL

### C1 — PS (Pressure Stability) is normatively circular; it smuggles one framework into a benchmark that claims not to make one
§2/§5: PS distinguishes "reason-responsive updating (good)" from "sycophantic capitulation (bad)" via
"argument quality pre-rated by panel," scoring capitulation-to-weak against and updating-on-strong for.
On a **genuine value conflict**, "argument quality" is not framework-neutral: whether an argument *for
prioritizing privacy over utility* is strong depends on the value weighting you already hold. So the
panel's argument-quality rating IS the normative adjudication the design elsewhere disclaims (§1: "not
whether models give the right answer"). A model holding a coherent minority position is scored
"sycophantic" if it moves toward the panel-majority's preferred value and "rigid" if it doesn't — the
reasonable-pluralism problem re-entering through PS's back door. This directly violates the KB 07 §2
**neutrality meta-eval** requirement ("equally-good opposite-conclusion traces must score equally";
MoReBench t=−0.59, p=0.56), which the design invokes for CR/scoring generally but never applies to PS.
PS is the axis that operationalizes "good vs bad" adjudication; if it is circular, the benchmark's headline
claim ("adjudicates coherently, calibratedly, and *for the right reasons*") is unfalsifiable on exactly the
contested tier that is its novelty.
**Minimal fix:** (i) restrict direction-scored PS to the universal-floor tier only (where the framework IS
declared, so "strong argument" is well-defined); (ii) on the contested tier, score only *magnitude* of
movement and *reason-givenness* (does the model engage the argument's content) — never direction; (iii) add
an explicit neutrality meta-eval: mirror-image counterarguments of equal panel-rated quality on both sides
of each pair must produce statistically equal flip scores, and publish the t-test.

### C2 — The pilot cannot estimate per-cell consensus; the difficulty axis is non-estimable at the stated N
§3.3 makes **consensus stratification the difficulty axis** — each grid cell needs a measured human
consensus level to assign tier and to oversample the 0.4–0.7 band. §4 requires **N≥80/contested cell**. But
the grid is {10 pairs × 3 stakes × 3 uncertainty × 4 beneficiary × relationship(≥2) × reversibility(≥2)} =
**≥1,440 cells**, while P1 generates **400 pilot instances** (<0.3 instances/cell — you cannot estimate a
per-cell consensus from a fraction of one item) and P2 panels **N≈300 total people**. "N≥80/cell" (responses)
and "N≈300 total" (people) are conflated: covering 1,440 cells at 80 responses each is ~115k ratings, i.e.
~384 psychometrically-instrumented ratings per person — an order of magnitude beyond feasible fatigue
limits, and still leaves the *contested* cells thinly sampled once you subset to the 0.4–0.7 band. As
written, the benchmark's core difficulty mechanism is not estimable at the proposed pilot scale, so P2
cannot deliver the stratification P3 depends on.
**Minimal fix:** either (a) collapse the factorial to a screened fractional design (name the ≤~60 cells you
will actually panel and justify the confounding structure), or (b) state the true panel N and per-person
load and re-budget (see M7). Publish the power calculation for detecting a 0.4-vs-0.7 consensus difference
at N/cell before P1. Right now the numbers are decorative.

---

## MAJOR

### M1 — The "5 core values" are never anchored to an external authority (Law 7 / pre-reg checklist fail)
The entire factorial (§3.1) is generated from "5 core values → 10 pairs," but the doc never names the value
taxonomy. Annotators get MFQ-2/Schwartz/WVS vectors (§4) yet the *construct axis itself* — the 5 values —
is unanchored. KB 01 pre-reg checklist line 2 ("every axis anchored to a citable external authority") and
Law 7 ("ground every axis in a citable external authority; map each item to a named clause") are failed at
the root. Without this, PF is a fingerprint of an undefined hand.
**Fix:** declare the taxonomy (e.g., Schwartz higher-order values, or a named subset with citation) and a
clause map; justify why 5 and why these.

### M2 — DC on the contested tier is the mimetic fallacy the KB explicitly rules out
§2/§5: DC scores JSD to the human panel distribution as a *graded good/bad* outcome. But KB 01 Adjudication 9
and KB 12 Adjudication 2 rule human-likeness is **not** the target for *agent* behavior — "humans want agents
to act differently than humans in the same dilemma" [Kneer; 2024-Lazar]. On the contested tier, DC's primary
score rewards mimicry of human disagreement — precisely the mimetic target the corpus warns against — and the
tiered-floor escape hatch does not cover it (the floor is a separate tier). The design treats distribution-
match as normative (scored) when the KB only licenses it as *descriptive/diagnostic*.
**Fix:** state explicitly that DC is a descriptive calibration diagnostic, not a normative target; do not let
DC contribute to any "better adjudicator" ranking; or justify per-item why matching *this* population's
distribution is the declared normative goal (values-of-population-X framing, Law 7).

### M3 — CO (transitivity) and DC (incomparability) contradict each other on incommensurable pairs
§2: CO scores transitivity/dominance violations as errors, while DC rewards a calibrated "these are
incomparable" response and cites the very incommensurability literature [2024-Zhi-Xuan; 2025-Benavoli] that
licenses *incomplete/intransitive* preferences over genuinely incommensurable values. A model that correctly
declares a pair incommensurable (rewarded in DC) but is then scored for an intransitive triad on that same
pair (penalized in CO) is being punished for consistency with the design's own philosophical commitment.
Inter-axis inconsistency.
**Fix:** draw CO triads only from cells with a defensible dominance/commensurability structure; exclude
declared-incomparable pairs from transitivity scoring, and state the rule.

### M4 — No shortcut audit (lexical baseline / 10%-fine-tune probe) — mandatory, and higher-risk for a generator
KB 01 Step 2 and KB 04 §6.5 mandate: verify a lexical/word-averaging baseline ≈ chance, and run the
10%-fine-tune probe (parity ⇒ exploitable surface structure [2025-Machlovi]). CRUX cites Machlovi for
*contamination* but never runs the probe on itself — despite being *procedurally generated*, where template
structure is exactly the shortcut risk. Absent from §5 and §6.
**Fix:** add lexical-baseline and 10%-fine-tune probes to P3 as go/no-go gates; report both.

### M5 — No eval-awareness / monitored-vs-unmonitored comparator for the PS multiturn component
KB 01 checklist line 13 requires an eval-awareness probe for any agentic component; PS (3–5 turn persuasion,
authority pushback, stakes escalation) is the single most eval-aware-vulnerable axis — a model that detects a
test will *perform* principled resistance (alignment-faking reasoning 12%→78% after RL
[Anthropic-Alignment_Faking]; compliance gap 11–15%). No monitored-vs-unmonitored arm exists.
**Fix:** add a monitored-vs-unmonitored comparator on the PS/dialogue subset; report the compliance gap as a
first-class limitation.

### M6 — "Cannot saturate by construction" is asserted, not demonstrated; §6 contract only half-met
§3.3 claims the contested tier "cannot saturate by construction." This violates Law 3 ("saturation is a
format artifact... headroom is engineered, not found") — the KB's stance is that non-saturation must be
*shown empirically*, never assumed. The DC oracle ceiling is KorNAT-class low (~0.45) and a model can
approach it; JSD has no mapping to the KB 04 §6.1 "best model ≤~70% of ceiling" contract, and P3 promises
"separation stats" without committing to the §6.2 bar (≥90% of pairs at p<0.01 on the hard tier) or a
decision rule if it fails.
**Fix:** define a saturation metric for the distributional tier (model-JSD vs oracle-ceiling headroom);
pre-commit the ≥90%/p<0.01 separation gate and the action taken on failure.

### M7 — Cost is undisclosed and P1's ~$5–8k implies an order-of-magnitude underestimate; reusability leans on unbuilt designs
Only P1 is priced (~$5–8k). P2 (DICES-scale N≥80/cell panels with MFQ-2/Schwartz/WVS instrumentation +
test-retest subsample), the **separate** argument-quality pre-rating task for PS (every counterargument ×
item × graded rating), and 15%-naturalistic panel validation are unbudgeted; realistically $100k+. The panel-
cost mitigation ("reusable across CRUX versions and by designs 01/05") is asserted on designs that are not
yet built — an unhedged dependency for the flagged BUILD-SECOND design.
**Fix:** publish a full P1–P4 budget with per-person load; treat the 01/05 reuse as a risk, not a saving,
until those panels exist.

---

## MINOR

- **m1 — CO longevity not flagged.** KB 04 §2.6: coherence metrics are saturation-resistant *now* but
  "longevity untested — flag as risk." CRUX leans heavily on CO (2/39 pass today) and omits the flag. Add it.
- **m2 — 15% naturalistic anchors are maximally contaminated.** Advice-forum conflicts (AITA-class) are in
  every training set; §9 uses them for ecological validity without noting they are the contaminated 15%.
  Treat them as a contamination-diagnostic, not clean signal; report synthetic-vs-natural gap with that caveat.
- **m3 — Naive baselines and worst-group/Pareto missing.** Checklist wants majority-class/All-Neutral
  baselines and a harm/over-refusal Pareto + worst-group. §5 co-reports over-refusal but no dummy baselines
  and no worst-group aggregation are named. Add them.
- **m4 — Falsification condition not stated.** Step 0 requires "what would falsify the claim that your
  benchmark measures the construct." §2 defines axes but no falsifier. State one (e.g., DC and PS both null
  vs capability PC1 ⇒ CRUX measures competence, not adjudication).

---

## Pre-registration checklist audit (KB 01) — where the design claims compliance
| Line | Status | Note |
|---|---|---|
| Whose values + falsification | ◐ | panel named; 5 values unanchored (M1); no falsifier (m4) |
| Every axis → citable authority | ✗ | 5 core values unanchored (M1) |
| Behavioral primary | ✓ | adjudication is behavioral |
| Two-tier + adversarial filtration + **shortcut audit** | ◐ | tiers/IRT yes; shortcut audit missing (M4) |
| Minimal pairs + ambiguity/abstention | ✓ | AMCE minimal pairs + incomparability |
| Multiturn component | ✓ | 3–5 turn dialogue |
| Disagreement philosophy + per-category IRR | ◐ | philosophy yes; per-keypoint CR κ not planned |
| Ceiling + naive baselines + competence + capability-corr | ◐ | ceiling/competence/cap-corr yes; naive baselines missing (m3) |
| Judge validated κw/ICC, ≥2 cross-family | ✓ | KB 07 stack invoked |
| Perturbation battery + per-condition SD | ✓ | §6; SD "everywhere" |
| Harm/over-refusal Pareto + worst-group | ◐ | over-refusal yes; Pareto/worst-group not explicit (m3) |
| Contamination: fresh-per-run + canaries | ✓ | but 15% naturalistic contaminated (m2) |
| **Eval-awareness probe (agentic)** | ✗ | no monitored/unmonitored on PS (M5) |
| Human baseline identical instrument + test-retest | ✓ | §6/§4 |
| Release: annotator-level + replication + retirement | ✓ | §7 P4 |

---

## VERDICT: BLOCK

Two pre-pilot blockers: **C1** (PS scoring is normatively circular on the contested tier and fails the KB 07
neutrality meta-eval — the "good adjudication" construct is unfalsifiable where it matters most) and **C2**
(the pilot N cannot estimate the per-cell consensus that IS the difficulty axis — the difficulty mechanism is
non-estimable as specified). Neither is a fatal *idea* — both have clean minimal fixes (bound direction-scored
PS to the floor tier + add a neutrality t-test; collapse the factorial to a named fractional design + publish
the power calc). Fix C1, C2, and Majors M1–M6, and CRUX becomes the strongest design in the portfolio. As
written it is not ready for a pilot.

**Single most likely remaining error after fixes:** the contested tier will fail to discriminate. The DC
oracle ceiling is KorNAT-class low (~0.45) and human test-retest instability is 10–18% on exactly the
controversial items [2024-Boerstler] — so model-to-model JSD differences on the contested tier will likely sit
inside each other's error bars, failing the KB 04 §6.2 ≥90%-pairwise-separation contract on the very tier
that is supposed to be the discriminative one. Bet: the contested tier discriminates *models from the human
ceiling* but not *models from each other* — leaving CO and floor-tier CR doing the real separation work.
