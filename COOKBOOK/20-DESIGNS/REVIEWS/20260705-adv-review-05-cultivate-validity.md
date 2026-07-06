# Adversarial Feasibility/Validity Review — Design 05 CULTIVATE

> **Refute-first review.** Reviewer posture: the design is flawed until evidence forces otherwise.
> Artifact: `COOKBOOK/20-DESIGNS/05-cultural-cultivate.md` (In-Situ Cultural Adaptation).
> Standards: KB 01 (Seven Laws / pipeline / pre-reg checklist), KB 03 (validity), KB 04 §6 (hard/unsaturated/
> discriminative contract), consulted KB 11 (cultural-linguistic), KB 12 (pluralism). Sources cross-checked
> against `30-EVIDENCE/20260705-digests/20260705-cultural-digest.md` (the Cultural-Global digest).
> Date: 2026-07-05.

CULTIVATE is one of the more sophisticated designs in the portfolio — it clears many pipeline items other
designs miss (two-tier drop, OA essentialism axis, per-locale judge validation, over-deference Pareto,
perturbation battery, canaries + procedural assembly). The defects below are therefore concentrated in the
**construct core** (what "correct adaptation" even means and whether it is separable from sycophancy),
the **feasibility of the headline methods artifact** (MGCFA), and **fidelity to its own evidence base**
(the N_eff≈3.4 disclosure and a denominator over-claim). Two of these are fatal as written.

---

## CRITICAL

### C1 — Adaptation is not operationally separated from sycophancy/pandering. (Construct validity)
The AA reward structure is: when a cultural cue appears, shift advice toward the locally-endorsed norm
(§2 AA; §5). That behavior is **observationally identical to sycophancy** — shifting position to match the
perceived identity of the user. The design provides no control that distinguishes "adapted because it is
culturally appropriate" from "adapted because agreeing with whoever the user appears to be is rewarded."
The OA axis (§2) is a *partial* essentialism control (it catches group-cue application when the individual
signals non-modal), but a pure panderer that simply tracks *whatever value the individual signals* passes
OA **and** scores high on AA. Law 1 (recognition≠propensity) and the corpus's best-replicated confound
(Sycophancy correlates −66.8% with capability PC1 [2024-Ren-Safetywashing]; the Anthropic Sycophancy result)
are directly in scope and unaddressed. **Minimal fix:** add a sycophancy/anti-adaptation control condition —
items where the culturally-cued user signals a preference the *survey marks as harmful or non-modal*, or an
arbitrary non-cultural preference; a model that "adapts" equally there is pandering, not culturally competent.
Report the adapt-toward-harm rate as a first-class discriminant, not an afterthought.

### C2 — The headline difficulty mechanism contradicts the declared ground-truth philosophy, and its "correct" answers may encode majority-endorsed harms. (Construct validity / Law 4 / doc 12)
§2 AA makes the **liberal-compatibility filter "the core difficulty mechanism"**: models allegedly score
"3–4/5 on liberal-convergent items and 0–1/5 on divergent ones," and CULTIVATE "makes that gap the headline."
A crisp 0–1/5 gap requires a **determinate correct divergent resolution** (a modal gold answer). But §4
declares the cultural layer is "scored against locale survey distributions … contested intra-locale items
distributional with entropy flags." The divergent exemplars the design names — *"filial obligation over
individual preference; communal consent over individual autonomy; complementarian family-role expectations"*
(§2 AA) — are **precisely the high-entropy, intra-locale-contested items** (women vs men, generation, caste,
urban/rural). You cannot simultaneously (a) score these distributionally with honest entropy flags and
(b) harvest a crisp determinate 0–1/5 "adaptation gap" as your headline. Whichever you pick breaks the other.
Worse, choosing (a-as-gold) means the benchmark scores a model **more aligned for endorsing complementarian
gender roles or filial-over-individual** — i.e., aligning to a survey majority that "may encode harmful
biases" (doc 12 §7.3 [2024-Jin-MULTITP]; Law 4). The floor-vs-divergent boundary that is supposed to prevent
this is **asserted but never operationalized**: nothing in the design states WHO rules that complementarian
gender roles are "divergent culture" (scored, rewarded) rather than a UDHR-floor violation (never traded).
That single undefined boundary decides whether the benchmark is a cultural-competence measure or an
illiberal-norm endorser. **Minimal fix:** (i) commit to one regime per item with a measured consensus
threshold (KB 01 Adjudication 1 — gold only above ~85% survey consensus, distributional below, entropy
reported); accept that genuinely divergent items are mostly *contested* and therefore scored distributionally,
which **demotes the crisp "0–1/5 gap headline" from a claim to a hypothesis.** (ii) Publish the operational
floor/divergent decision procedure (which authority, which clause) as a datasheet artifact, pre-registered,
not left to co-design discretion.

### C3 — The MGCFA "shipped artifact" is under-specified on unit-of-analysis and almost certainly under-powered. (Feasibility)
The measurement-invariance pipeline is sold as the standalone methods contribution and the "instantly
differentiated (0/218)" novelty (§1, §4, §5, Venue framing). But MGCFA (configural→metric→scalar) is a
**respondent-level latent-variable technique requiring large N per group** (rule-of-thumb ≥~200/group for
stable scalar invariance). The design never states **who the rows are.** If invariance is tested across locale
versions of construct scales *as answered by models*, N per group = 9 models (P3) — MGCFA is not estimable.
If across *human survey respondents*, that is a different instrument than the model benchmark and needs
hundreds per locale, not the N≥100 total the surveys budget (§8 P2), which is further split across
urban/rural × generation × region/caste strata (§10) down to ~25/cell. Either way the central methods claim
is not feasible at the scoped N, and the identification/unit ambiguity means the "first proper MGCFA" claim
cannot currently be evaluated. **Minimal fix:** specify the data matrix (rows = ?, columns = which invariant
indicators), do a Monte-Carlo power analysis for the target invariance level, and set survey N by that power
requirement (likely ≥200–300/locale, ≥400 if stratified). If the pilot cannot power MGCFA, re-frame it as a
*development* deliverable (invariance *machinery* + a powered follow-up), not a P1 result.

### C4 — Cost/human-effort is under-scoped by roughly an order of magnitude. (Practical feasibility)
P1 budgets **~$10–20k for 2 locales including surveys** while requiring: native co-design teams *authoring*
30 scenario-families × 4 variants with per-scenario keypoint rubrics; demographically-balanced local surveys
(survey-firm cost); **and** local expert panels rating full multi-turn transcripts for per-locale judge
validation (§5, §7) across 2 languages/locale. Nigeria is specified as a **Yoruba/Hausa/Igbo split** (§3.2) —
effectively 3 sub-locales of survey + co-design, not one, inside the "2-locale" budget. Realistic cost is
plausibly $50–150k+. The under-scope is load-bearing because C3's fix (power the surveys) multiplies survey
cost further. **Minimal fix:** rebuild the budget bottom-up (author-hours × rate + survey-firm quote at powered
N + panel-hours for transcript rating) and either raise the figure or cut scope (one language/locale in P1;
Nigeria as a single sub-locale in P1).

---

## MAJOR

### M1 — The design does not honor the Cultural-Global N_eff≈3.4 descriptive-only disclosure. (Data integrity)
The digest states verbatim: *"Minimum detectable effect at N_eff=3.4 is Cohen's d ≈ 2.5 → all cross-model
patterns are descriptive only, never inferential"* (`20260705-cultural-digest.md` §4; DEFF downgrade of 10
nominal models → N_eff≈3.4). CULTIVATE's motivation (§1) and its saturation defense (§6) lean on trial numbers
— **"92.5% knowledge-about vs reasoning-within gap," "100% Western-liberal resolution," "0–1/5 divergent
performance"** — as if they were robust findings and unsaturation evidence, with no reproduction of the
descriptive-only caveat. These are small item-level counts (37/40, 40/40; 40 items across 7 traditions) from a
descriptive study; using them as the empirical warrant that divergent items *are* unsaturated is exactly the
over-claim the digest disclaims. **Minimal fix:** add the descriptive-only disclosure where these numbers
appear; label the 0–1/5 gap a *motivating hypothesis to be established in-pilot*, not established fact
(this also aligns with the C2 demotion).

### M2 — "Exactly ONE of 218 benchmarks uses a community unit" is a denominator over-claim. (Data integrity)
The digest scores the unit-of-agency feature **only on the 32 deep-scored benchmarks**: *"community exactly
one paper"* is 1/32, not 1/218 (the 186 auto-scored benchmarks were not scored on this feature). CULTIVATE
repeats "exactly ONE of 218 benchmarks uses a community unit" (§3.1) and "one has a communal unit" (§9 novelty)
— both inheriting the KB-11 extrapolation, not the digest's actual denominator. This inflates a novelty pillar.
**Minimal fix:** state "1 of 32 deep-scored (community-unit feature not scored on the 186 auto-scored set)."

### M3 — Divergent items are heavily contaminated by trained Hofstede/WVS/stereotype priors, and the AA and OA cells reward/punish the same recalled stereotype. (Contamination — KB 05, Law 6)
On AA-divergent items the "correct" answer often *is* the culturally-modal stereotype ("Korean culture prizes
filial obligation") — which is exactly the recitation the design says it wants to move past (§1), and which is
saturated in pretraining. A model can produce the AA-correct divergent answer by **memorized stereotype recall**
rather than in-situ competence, defeating the difficulty reservoir; meanwhile the OA cells *penalize* that same
stereotype recall. The intended difference-aware/blind contrast (KB 01 Adjudication 5) is legitimate, but the
design never verifies that AA-divergent survives a **"recite the modal stereotype" baseline** — if that baseline
scores high on AA, the AA-divergent difficulty is a contamination artifact. **Minimal fix:** add a
Hofstede/stereotype-recall baseline agent and require AA-divergent to beat it; report the AA-vs-OA joint
distribution to show the two are not just measuring the same recall in opposite signs.

### M4 — Missing checklist items: eval-awareness comparator, 10%-fine-tune probe, lexical-baseline commitment. (Pre-reg checklist / KB 04 §6.5 / Law 6)
CULTIVATE has a multi-turn agentic component but no **monitored-vs-unmonitored comparator** (checklist line
"Eval-awareness probe … for any agentic component"; Law 6). The doc-04 §6 contract item 5 (shortcut audit) is
only *partially* met: the "culture-keyword-matching agent fails half" argument covers OA, but there is **no
10%-fine-tune probe** and **no explicit lexical-baseline≈chance commitment** for AA/CD/AVA. **Minimal fix:** add
a monitored/unmonitored framing axis to the perturbation battery; add the 10%-fine-tune parity probe and per-tier
lexical/majority-class baselines to §6/§7.

### M5 — Pilot lacks pre-registered decision rules, thresholds, and power. (Pre-reg checklist / KB 04 §6)
§8 lists activities but no **pre-registered pass/fail thresholds**: what pairwise-separation level counts
(§6 says "separation stats required" but not the ≥90%-of-pairs-at-p<0.01 bar of KB 04 §6.2); what κw floor
validates a per-locale judge; what invariance level (metric? scalar?) is required to license a scope claim;
what capability-correlation ceiling gates Law 1. No power analysis anywhere. The **empirical ceiling is
referenced but never given a target/commitment** (KorNAT's 0.450, not 1.0 — KB 03, doc 12); §4 says "reported
empirical ceilings" but the checklist bar is "ceiling ≠1.0 stated explicitly." **Minimal fix:** add a
pre-registration table: hypotheses, thresholds, power, stopping rules, ceiling-reporting commitment.

### M6 — Communal deliberation-facilitation "process-scoring" is the lowest-IRR construct in the design and carries no reliability target. (Label reliability — KB 03 §2)
§3.1/§5 score Ubuntu *indaba* / Confucian role-dyad cells on "deliberation-facilitation quality, not verdicts."
Pragmatic/contextual judgments are exactly where human agreement collapses (α 0.10–0.46; KB 03 §2). The design
sets **no κ/α target** for these cells and offers no evidence the co-design rubrics can be scored reliably.
**Minimal fix:** pilot IRR on the communal rubrics first; if α is uninterpretable, treat these cells as
exploratory/distributional, not scored.

---

## MINOR

- **m1 — "965 characterizations" (§9) is unverifiable.** The number does not appear in the Cultural-Global
  digest, KB 11, or KB 12 (218 benchmarks; 380 trial items; 703 RLHF instances are the digest's counts). Cite
  the source or remove.
- **m2 — 0/218 measurement-invariance may be a detection-method artifact.** 186 of 218 were auto-scored via
  regex on 13 features; the digest does not flag whether MI positives could be missed by that method. The
  motivation (§1) and novelty (§4) lean hard on 0/218; add one hedge that it is a *reported*/detectable-MI
  prevalence.
- **m3 — Falsification condition never stated** (Step 0 / Law 7). The construct names whose values (locale
  survey distributions) but not what observation would falsify "CULTIVATE measures in-situ adaptation." Add it.
- **m4 — No training-prohibition/retraction clause** in the release plan (§8 P4; checklist line "training-
  prohibition"). Add one.
- **m5 — CD "largely judge-free" (§5) is overstated.** Deciding whether a turn-t behavioral change is *an
  appropriate adjustment* in open dialogue is a judge call; either justify the automaticity or drop "judge-free."

---

## Checklist compliance snapshot (KB 01 pre-registration)

| Item | Status |
|---|---|
| Whose-values + falsification | Partial — whose=surveys; **falsification missing (m3)** |
| Axes anchored to external authority | OK (survey-grounded) |
| Behavioral primary / recognition paired | OK (interactive vs static-floor) |
| Two-tier + adversarial filtration + shortcut audit | Partial — filtration is post-hoc IRT pruning; **no 10%-fine-tune / lexical baseline (M4)** |
| Contrastive pairs + ambiguity/abstention | OK (OA =/≠ pairs; AVA abstention) |
| Multiturn + single-turn saturated floor | OK |
| Disagreement philosophy + per-category IRR | Partial — distributional declared; **no κ targets, communal IRR (M6)** |
| Ceiling + naive baselines + competence + capability-corr | Partial — competence & cap-corr OK; **ceiling value uncommitted, majority/lexical baselines missing (M4,M5)** |
| Judge validated κw/ICC + cross-family + refusal | OK (per-locale; four-way refusal) |
| Perturbation battery + flip-rates + per-condition SD | OK |
| Harm/over-refusal Pareto + worst-group | OK |
| Contamination: private/fresh + canaries + training-ban | Partial — private holdout+canaries OK; **training-ban missing (m4)** |
| Eval-awareness monitored-vs-unmonitored | **Missing (M4)** |
| Human baseline + test-retest | OK |
| Release: labels, scripts, versioning, retirement | OK-ish |

---

VERDICT: BLOCK

**Single most likely remaining error (beyond those listed):** even after adding a sycophancy control (C1) and
demoting the divergent gap to distributional (C2), the AA-divergent "correct" answers will fail to *separate
models* — the design's own evidence base shows cross-model outputs are near-clones (r=0.99–1.00 [2026-Huang],
doc 12), so on the culturally-modal answers that survive contamination filtering, all frontier models will
converge to the same Western-liberal default and the pairwise-separation contract (KB 04 §6.2) will not be met;
the benchmark will be *hard* but not *discriminative*, and that is only discoverable after the (under-powered,
under-budgeted) pilot has already been run.
