# Adversarial Novelty Review — Design 06 CRUX (Value-Conflict Adjudication)

> Refute-first review. Artifact: `COOKBOOK/20-DESIGNS/06-crosscutting-crux.md` (BUILD SECOND — extra scrutiny).
> Reviewer model: Opus. Date: 2026-07-05. Corpus: 965 characterizations / 737 distinct
> (NormEval 54, Moral Psych 292, Religious 401, Cultural 218). Evidence swept across all four
> feature matrices per §8 file pointers. Beyond-corpus items flagged `[beyond-corpus]`.

## Bottom line up front

CRUX's novelty is a **conjunction/integration claim** — "no instrument *combines* conflict-specific
procedural generation + consensus-stratified dual-regime scoring + coherence auditing +
argument-quality-controlled pressure." That claim survives refutation: I found **no single benchmark
in the 965 covering ≥3 of the five CRUX axes**. But the claim is *weak by construction* (conjunction
novelty is almost always technically true), and two of the five axes are so thoroughly precedented
that the differentiated contribution is narrower than the pitch implies. The novelty statement also
**omits four in-corpus conflict-named neighbors** — a credibility problem for a design that concedes
"value-conflict is a crowded space." Fixable without changing the construct. **PASS-WITH-FIXES.**

---

## Refutation attempt — axis-by-axis coverage in the corpus

Each CRUX axis is individually well-precedented; the design is candid about most but not all of this.

| CRUX axis | Best in-corpus precedent(s) | Verdict on axis novelty |
|---|---|---|
| **CR** — conflict recognition / value-of-information | Value Kaleidoscope (MP high), CCD-Bench (Cultural rank 6 / MP high), Conscience Conflict (MP high), RoleConflictBench (Cultural), ConflictScope `[beyond-corpus]` | Conflict-recognition itself is **crowded**. The **value-of-information branch** (seek the decision-relevant fact; design cites only 4% of field tests it [2025-Snoswell]) is the one genuinely thin sub-component. |
| **PF** — priority fingerprint (revealed value ordering) | ValueBench, DailyDilemmas (MP top), VALUEFLOW (MP med), Assessing LLMs for Moral Value Pluralism (MP med) | **Well-covered** — value-priority profiling is exactly what DailyDilemmas/ValueBench do. Design admits this ("DailyDilemmas profiles"). |
| **CO** — coherence (GARP/transitivity, AMCE irrelevant-edit) | Seror GARP/CCEI [2024], MoCa AMCE [2023-Nie], Staircase non-transitivity under escalation [2025-Wu] | **Method fully precedented.** CRUX imports GARP wholesale ("GARP/CCEI-style") and AMCE wholesale ("paired AMCE… wrong-factor movement [2023-Nie]"). Novelty is domain transfer, not method. |
| **DC** — disagreement calibration (distributional match) | Scruples distributional [2021-Lourie], Pluralistic Moral Gap (MP/Cultural med), KorNAT/DICES/PluriHarms (cited) | Distributional matching is established. The **dual-regime split** (high-consensus gold *floor* vs contested-distributional *cannot-saturate* tier) + calibrated **incomparability** option is the freshest single element. |
| **PS** — pressure stability (argument-quality-controlled) | Staircase escalation [2025-Wu]; sycophancy lit; links to Sketch S2 | **Argument-quality-controlled** counter-argument (separating reason-responsive updating from sycophantic capitulation) is relatively fresh; the escalation-pressure frame is not. |

**Conjunction holds, but is thin.** Value Kaleidoscope covers CR+PF only; Seror covers CO only; the
strongest multi-axis competitor covers 2 of 5. No refuting counterexample exists — so the core claim
is **not false** (not Critical). But once CO (Seror/MoCa) and the generation discipline (OffTheRails,
which CRUX explicitly "scales") are subtracted as imported machinery, the *differentiated* novelty
reduces to **dual-regime DC + argument-quality-controlled PS + the value-of-information branch**. The
4-way conjunction over-sells; a reviewer defeats each conjunct individually.

---

## Ranked defects

### MAJOR 1 — Novelty is a conjunction claim leaning on imported machinery; re-pitch around the 2–3 fresh elements
The pitch ("no instrument combines A+B+C+D") is technically true but structurally weak: every conjunct
is old. CRUX itself sources CO from Seror GARP/CCEI + MoCa AMCE, procedural generation from OffTheRails
[2024-Franken] ("scaled"), consensus-stratification-as-difficulty from PluriHarms genetic middle-sampling
[2026-Li], and distributional DC from Lourie/KorNAT. A skeptical D&B reviewer will note the design is an
*assembly* and ask what is invented. **Fix:** foreground the genuinely-fresh trio — (a) the dual-regime
gold-vs-contested scoring where the contested tier is *unsaturable by construction*, (b) argument-quality-
*controlled* pressure that discriminates reason-responsiveness from sycophancy, (c) the value-of-information
branch — and demote the 4-way conjunction to a supporting "and unifies these on one generator" line.

### MAJOR 2 — Four in-corpus conflict-named neighbors omitted from the novelty statement
The novelty statement cites 6 neighbors (ConflictScope, DailyDilemmas, Scruples, VAL-Bench, MoCa, Seror)
but omits these, all present in the swept matrices and all directly on the CR/PF axes:
- **Value Kaleidoscope** [2024-Sorensen] — MP tier=high (PD 56.5/CI 45.25), also in Religious & Cultural.
  Explicitly models value *pluralism and conflict* (which values are relevant to a situation and whether
  they support/oppose an action) at ~218k scale. This is the single most important omission — a direct
  CR+PF precedent stronger than several cited neighbors.
- **CCD-Bench: Probing Cultural Conflict in LLM Decision-Making** [2025] — Cultural rank 6, MP high.
- **RoleConflictBench** [2025] — Cultural corpus; role-conflict scenarios for contextual sensitivity
  (overlaps CR + AMCE-style factor sensitivity).
- **Conscience Conflict: Evaluating LMs' Moral Understanding** [2024] — MP high (PD 73.5).

Omitting four conflict-titled benchmarks while asserting the space is uniquely un-integrated undercuts
credibility. **Fix:** add all four to the nearest-neighbor list; explicitly state each covers CR/PF only
and lacks CO/DC/PS — which *strengthens*, not weakens, the integration argument.

### MINOR 1 — "Vs the 965" framing then leans on beyond-corpus items
ConflictScope [2025-Liu], MoralSim, and UNMARKED-MB are cited as anchors (nearest neighbor; criterion
validity) but are **absent from the 965 corpus** (confirmed: 0 title matches across all four matrices).
The §8 novelty header "Vs the 965 characterizations" is then partly argued against un-characterized,
announced work. **Fix:** tag corpus-vs-beyond-corpus provenance on each named neighbor so "965" is not
implicitly credited with ConflictScope/MoralSim.

### MINOR 2 — "No existing instrument combines…" (Motivation §1) should read as "first to unify," not "gap exists"
The sentence "no existing instrument combines conflict adjudication with consensus-stratified ground
truth, coherence auditing, and contamination-proof generation" is true but every component is one the
design itself imports and cites (Lourie/PluriHarms; Seror; OffTheRails). Rephrase to claim *unification*
rather than imply an empty field — avoids the easy reviewer rebuttal "each of these already exists."

---

## Nearest-neighbor table (5)

| # | Benchmark | Source | CRUX components already covered | What it lacks (CRUX's wedge) |
|---|---|---|---|---|
| 1 | **Value Kaleidoscope** [2024-Sorensen] | Moral Psych (high), Religious, Cultural | CR (value relevance / support-oppose), PF (pluralistic value set) at scale | No adjudication-to-single-decision; no CO/DC/PS; no difficulty engineering |
| 2 | **CCD-Bench** [2025] | Cultural (rank 6), Moral Psych (high) | CR (cultural value conflict in decision-making), some PF | No coherence auditing, no human-disagreement calibration, no pressure axis |
| 3 | **The Staircase of Ethics** [2025-Wu] | NormEval, Moral Psych (high), Cultural | PS (escalation), CO (non-transitivity under escalation) | No procedural conflict generation, no consensus-stratified DC, no VoI |
| 4 | **ConflictScope** [2025-Liu] `[beyond-corpus]` | (announced; not in 965) | CR + PF (value-conflict, revealed priority) | Single-turn, announced, no coherence/calibration/pressure axes (design's own concession) |
| 5 | **DailyDilemmas** [2024-Chiu] | NormEval, Moral Psych (top), Cultural | CR + PF (value-preference profiling from dilemmas) | Profiling only; no difficulty engineering, no CO/DC/PS, no matched-triad control |

*Also-ran precedents subtracting from specific axes:* Seror GARP/CCEI [2024] (CO only, economic frame);
MoCa AMCE [2023-Nie] (CO wrong-factor movement only); VAL-Bench [2025-Gupta] (CO/consistency, refusal-
gameable ρ=0.91); Scruples [2021-Lourie] (DC distributional only); Pluralistic Moral Gap [2025] (DC-adjacent).

---

## VERDICT: PASS-WITH-FIXES

Core claim (no single instrument combines all five axes) is **not refuted** — the strongest competitor
covers 2 of 5. But apply MAJOR 1 (re-pitch around the 2–3 genuinely-fresh elements, not the defeatable
4-way conjunction) and MAJOR 2 (add the four omitted in-corpus conflict neighbors, Value Kaleidoscope
foremost) before it goes to a D&B venue.

**Single most likely remaining error:** the differentiation rests heavily on **ConflictScope
[beyond-corpus, unpublished]** being single-turn with no coherence/calibration axes. It is announced,
not released — if its published version already ships a consistency or human-distribution axis, CRUX's
lead over the acknowledged nearest neighbor collapses from "four extra axes" to "one or two." The design
is betting against an unseen competitor; hedge the pitch accordingly.
