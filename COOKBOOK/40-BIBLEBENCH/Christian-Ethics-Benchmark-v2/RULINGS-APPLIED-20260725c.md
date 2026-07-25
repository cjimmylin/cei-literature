# RULINGS APPLIED — 2026-07-25c: df-proportional baseline and graded flip verdicts

**Date:** 2026-07-25 · **Session:** phase-7 (boot prompt `20260725d-boot-prompt-phase7-claims-adjudication.md`)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Predecessor:** `RULINGS-APPLIED-20260725b.md` — its §"Framing correction that binds both
manuscripts" is **SUPERSEDED by this file** (see RULING 1 below). Its assembly-target and
§7 rulings are untouched and remain in force.
**Escalation adjudicated:** `REPORTS/20260725-manuscripts/20260725-ESCALATION-claims-validity.md`
(Q2 and Q3; Q1 was already corrected in phase 6 and needs only the successor note).
**Spend:** $0. No model calls. Adjudication + one offline stdlib computation.

---

## RULING 1 (escalation Q3) — df-proportional no-effect baseline: **ADOPTED, as a descriptive reference line.**

**Owner ruling:** variance shares are reported against the df-proportional expectation
under no effect. In the balanced 5 (SUT) × 2 (judge) × 3 (epoch) layout —
`SS_total (df 29) = SS_SUT (4) + SS_judge (1) + SS_SUT×judge (4) + SS_error (20)` — the
reference line is E[share] = df/29: **SUT 13.79%, judge 3.45%, SUT×judge 13.79%,
error 68.97%.**

**R3 compatibility (binding interpretation):** the line is an *expectation*, not a test.
No p-value, no rejection decision, no significance language may be attached to it. Shares
are described as "above/below the df-proportional reference line", never as
"significant/non-significant". Withholding the line was judged the less honest option:
raw shares invite a reader to treat a 9.9% interaction as evidence when it sits below
what pure epoch noise produces.

**Consequences (all binding on both manuscripts and all successor artifacts):**

1. **"non-zero in 8 of 8" is DROPPED as an evidential claim everywhere.** An SS on a
   continuous metric is almost surely non-zero; the claim carries no information.
2. The *"large model effect, judges still reorder it"* narrative is **restricted to
   design 01 alone** — the only exemplar whose interaction (23.0%) is clearly above the
   line. Designs 06 (11.4%) and 09 (9.9%) sit **below** 13.79% and are re-grounded in the
   flip result (subject to RULING 2's graded reporting: design 06's flip is a single
   adjacent transposition; design 09 ep3 is tie-affected).
3. **"The models genuinely differ" becomes design-specific, not suite-wide.** %SUT is
   below the 13.79% line in designs 02 (5.8%), 03 (6.6%) and 08 (9.1%).
4. The target framing for both papers is:

   > *The models differ on most designs. On a minority of designs the judges clearly
   > disagree about the ordering; on the rest the systems are too tightly spaced for
   > either judge to resolve. Either way, no comparative claim survives the swap.*

**What this ruling does NOT touch (do not over-retract):** the operational conclusion
rests on two independent legs unaffected by Q3 — (1) the ordering flips, and (2) the
judge-free surface's 0-of-10 C1 contrasts excluding zero. **"No SUT-vs-SUT claim is
licensed" stands in full.** Only the suite-wide mechanistic story (that judge-ordering
disagreement is the cause *in every judged design*) is narrowed.

**Free corroboration ratified for inclusion (paper (b) §5.5):** design 05 is judge-free,
so its two judge levels are exact duplicates and the layout collapses to 5 × 3, giving
E[%SUT] = 4/14 = **28.6%** against an observed **27.4%**. The positive control's own
system main effect sits at its null expectation — independent, $0 corroboration that the
judge-free surface genuinely does not separate these five systems.

## RULING 2 (escalation Q2) — graded flip verdicts: **ADOPTED, τ alongside the binary verdict.**

**Owner ruling:** Kendall's τ (τ_a = (C−D)/10 over the 10 system pairs) is computed per
design × epoch between the two judges' orderings, from the swap cells already on disk
(`logs/fullbank-3ep-20260724/judgeswap-ep{1,2,3}.txt`), and reported **alongside** the
binary flip verdict — never instead of it, because rule R4 is written in binary terms.

**Binding reporting requirements:**

1. The flip criterion is stated verbatim wherever the flip result is reported: exact
   equality of the full five-way permutation of unrounded point estimates, stable-sort
   tie-break, no intervals ("naive point-estimate order", the tool's own qualifier).
2. τ, the discordant-pair count, and a tie flag accompany the binary verdict.
   Tie-affected cells (~10 of 27 judged design-epochs, incl. design 09 ep3) are flagged
   explicitly. Design 07 judge-A (0.0000 × 5 in ep1/ep2) is ORDER-UNDEFINED, not a flip.
3. Design 06's headline status is qualified: its epoch-1 "flip" is one adjacent
   transposition (τ = +0.80), positions 3–5 identical.

**Explicitly REJECTED (do not adopt in any artifact):** the reviewer's
*"P(preserved) = 1/120 under pure noise, so the test has no power"* argument. The two
judges score the same stored transcripts; their orderings are correlated by construction,
so a uniform-random-permutation null is far too permissive. The reviewer is directionally
right that the binary test is uncalibrated — that is what the graded τ reporting fixes —
but the specific 1/120 figure must not enter any artifact.

## Supersession record

- `RULINGS-APPLIED-20260725b.md` §"Framing correction that binds both manuscripts" is
  superseded **in part**: its prohibition on "the judge dominates" **remains binding**
  (judge and SUT footprints are comparable at the median, 35.3% vs 35.6%). Its positive
  framing — "the models genuinely differ … non-zero in 8 of 8 … 01/06/09 as the sharpest
  illustration" — is replaced by RULING 1's consequences 1–4 above.
- `20260725b-variance-decomposition-addendum.md` §3 (immutable) receives a successor
  addendum applying RULING 1; `20260725-fullbank-3ep-run-report.md` §0/§3 (immutable)
  receives a successor correction note for the Q1 "nine of ten" count (correct statement:
  **eight of the nine judged designs flip; 07 yields no judge-A ordering; 05 is
  judge-free by construction**). No existing dated report is edited.

## Carried forward UNCHANGED — not reopened by this ruling

- **`pushback_rate` is CLOSED** (A′ affirmed, `RULINGS-APPLIED-20260725.md`).
- **Holdout: recommended NOT to spend; owner has not ruled.** Quarantined, untouched.
- **Classifier pinned at `gpt-4.1-nano`** (`RULINGS-APPLIED-20260724e.md`); the v-next
  re-pin bundles with the d02 taxonomy revision as one instrument version (C6).
- **Bank revision 2026-07-24b.** No code, rubric, metric, or bank edit in this session
  (the new `kendall_tau.py` is an offline audit script in a gitignored run root, not an
  instrument component).
- **Assembly target SPLIT and §7 disposition** (`RULINGS-APPLIED-20260725b.md` Rulings
  1–2) remain in force.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
