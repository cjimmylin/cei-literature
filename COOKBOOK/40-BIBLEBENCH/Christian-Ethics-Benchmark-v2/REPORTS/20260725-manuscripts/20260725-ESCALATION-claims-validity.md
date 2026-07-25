# ESCALATION — three claims-validity questions the phase-6 session must NOT resolve alone

**Date:** 2026-07-25 · **Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Raised by:** phase-6 assembly session (Opus main loop), after two refute-first
adversarial reviews of the assembled manuscripts.
**Boot-prompt trigger:** *"Intended main-loop model: Opus … Switch to Fable only if a
genuine claims-validity call surfaces (say so when it happens)."* **It has. This is that.**
**Spend to raise this:** $0.

> **STATUS: paper (b) is marked DO-NOT-CIRCULATE pending these adjudications.**
> Paper (a) is SHIP-WITH-FIXES and is not blocked by them, but shares Question 1's
> consequence in a single sentence.

---

## 0. What this is, and what it is not

Two independent adversarial reviewers were run, one per manuscript, both instructed to
refute first. Between them they returned four blocking defects that are simple text
errors — those are being fixed directly and are **not** escalated here.

What IS escalated: **three findings that attack the underlying analysis rather than the
prose.** They impugn artifacts that are already committed and treated as settled:

- `20260725b-variance-decomposition-addendum.md` §3 (immutable, committed `1502e7433`)
- `RULINGS-APPLIED-20260725b.md` §"Framing correction that binds both manuscripts"
  (written earlier **today**, by this session)
- the phase-6 boot prompt's own carried-forward framing

**I verified all three myself** rather than taking the reviewers at their word, because
two of them contradict work this session had already ratified. Verification commands and
outputs are in §4. **All three replicate.**

**What is NOT in question.** Both reviewers independently recomputed and confirmed: the
variance decomposition arithmetic (every percentage, to rounding), all C1 Bonferroni
intervals, all summary medians and footprints, the run shape, spend, bank census, and
transplant fidelity. **No arithmetic error has been found.** Every issue below is
*interpretive* — the numbers are right; what they are claimed to mean is contested.

---

## Question 1 — Does design 07 belong in the "nine of ten designs flip" headline?

**Finding: NO, and this is verified.** Design 07's judge-A `arc_pass_rate` is identically
**0.0000 on all five systems in epochs 1 and 2**, and 0.0370/0/0/0/0 in epoch 3. There is
no judge-A ordering to preserve or to flip. The swap tool nevertheless emits an A-order —
that order is Python's stable sort falling back to system load order — and records
`JUDGE-SENSITIVE (order flips)` in all three epochs.

The manuscripts already concede design 07 is degenerate: they mark it floor-saturated,
state that *"a floor cannot exhibit an interaction,"* and exclude it from the variance
medians. **They do not exclude it from the flip headline.**

**Consequence.** The correct statement is narrower:
> *Eight of the nine judged designs flip; the ninth (07) is floor-saturated and yields no
> ordering to test. Design 05, the judge-free design, is the tenth and does not flip by
> construction.*

**Affected artifacts:** both manuscripts' abstracts and introductions;
`20260725-fullbank-3ep-run-report.md` §0 and §3 make the same "nine of ten" statement.
That report is **immutable** — the fix is a successor note, never an edit.

**Recommendation (not a decision):** adopt the narrower statement. It costs the headline
almost nothing and removes an error a hostile reader finds in one grep.

---

## Question 2 — The flip test has no stated criterion and no null baseline. Is it reportable as-is?

**Finding: the criterion is far stricter and far blunter than the prose implies.**

`tools/audit/pilot_judge_swap.py` line ~181:
```
oa = sorted(common, key=lambda s: a[s], reverse=True)
ob = sorted(common, key=lambda s: b[s], reverse=True)
flag = "STABLE" if oa == ob else "JUDGE-SENSITIVE (order flips)"
```

That is **exact equality of the full five-way permutation** of unrounded point estimates.
No intervals. No tie handling. No null model. The tool's own section header calls it
*"naive point-estimate order"* — a qualifier both manuscripts drop.

Two consequences the reader currently cannot see:

1. **A single adjacent transposition counts as a full flip.** Design 06, epoch 1:
   A-order `gemini(0.9180) > deepseek(0.8810) > gpt41mini > llama > mistral`;
   B-order `deepseek(0.9630) > gemini(0.9392) > gpt41mini > llama > mistral`.
   Positions 3, 4 and 5 are identical. The swapped pair differs by 0.037 under judge-A and
   0.024 under judge-B. **This lone swap is what makes design 06 "flip,"** and design 06 is
   one of the three headline *"large model effect, judges still reorder it"* exemplars.
2. **Ties are broken arbitrarily.** The reviewer counted tie-affected orderings in 10 of
   the 27 judged design-epoch cells, including design 09 epoch 3 (judge-A has
   deepseek = gemini = 0.8235) — and design 09 is another of those three exemplars.

**Where I part company with the reviewer.** The reviewer argues P(exact 5-way preservation)
= 1/120 under pure noise, so *"nine of ten flip is what a test with no power returns,"* and
that 4 STABLE in 27 judged design-epochs is therefore *more* stability than chance.
**The 1/120 figure is the wrong null and overstates the case.** The two judges score the
same stored transcripts; their orderings are correlated by construction even under
substantial judge noise, so a uniform-random-permutation null is far too permissive.
The reviewer's *direction* is right — the test is uncalibrated and a binary verdict hides
the magnitude of disagreement — but the specific 1/120 comparison should not be adopted
as-is.

**Recommendation (not a decision):** do not abandon the flip result — it is real and it is
the honest motivation for the two-judge rule. Instead (a) state the criterion verbatim
wherever the result is reported, (b) report the *magnitude* of each flip alongside the
binary verdict, and (c) stop describing designs 06 and 09 as cases where "the judges
reorder" without disclosing that the reordering is one adjacent transposition or a
tie-break. Kendall's τ per design-epoch is computable from cells already on disk at **$0**
and would replace a binary verdict with a graded one.

---

## Question 3 — Should variance shares carry a df-proportional no-effect baseline? **This is the hard one.**

**Finding: verified, and it reaches the project's central claim.**

Sums of squares are non-negative, and under a null of no effect their expectations are
proportional to degrees of freedom. In this balanced 5 (system) × 2 (judge) layout with
3 epochs as replicates — `SS_total (df 29) = SS_SUT (4) + SS_judge (1) + SS_SUT×judge (4)
+ SS_error (20)`:

| Term | df | E[share] under no effect |
|---|---:|---:|
| SUT | 4 | **13.79%** |
| judge | 1 | 3.45% |
| SUT × judge | 4 | **13.79%** |
| error | 20 | 68.97% |

Against that reference line (my own computation, §4.3):

| design | SUT×judge | vs 13.79% | SUT | vs 13.79% |
|---|---:|---|---:|---|
| 02 | 46.5% | above | 5.8% | **below** |
| 08 | 25.9% | above | 9.1% | **below** |
| 10 | 25.8% | above | 25.8% | above |
| 01 | 23.0% | above | 45.4% | above |
| 06 | 11.4% | **BELOW** | 63.4% | above |
| 09 | 9.9% | **BELOW** | 54.4% | above |
| 04 | 4.9% | **BELOW** | 46.3% | above |
| 03 | 1.4% | **BELOW** | 6.6% | **below** |

**Four of the eight judged, non-saturated designs have an interaction share at or below
what pure epoch noise would produce** — and two of them, **06 and 09**, are exemplars the
addendum and both manuscripts cite for *"large model effect, judges still reorder it."*

Two claims are directly affected:

1. **"`SUT×judge` is non-zero in 8 of 8 judged designs."** A sum of squares on a continuous
   metric is almost surely non-zero; the only design where it is genuinely zero is 05, and
   there it is zero *by construction*. As a claim about evidence this is close to vacuous.
2. **"The models genuinely differ."** %SUT is below the 13.79% line in designs 02, 03 and
   08, so this is design-specific rather than suite-wide.

**The genuine tension, stated fairly.** Rule R3 forbids significance testing and
significance language. A df-proportional reference line is arguably *descriptive* — it is
an expectation, not a test, and carries no p-value — in which case R3 permits it. But it
is unmistakably inferential in spirit, and a reviewer could fairly say the project cannot
both refuse significance testing and lean on a null-expectation comparison. **That single
judgment decides whether paper (b) needs a modest revision or a re-framing.** It is not
mine to make.

**Recommendation (not a decision):** adopt the baseline as a descriptive reference line
with no significance language, drop "non-zero in 8 of 8" as an evidential claim, and
restrict the "large model effect, judges still reorder it" narrative to design 01 — the
only exemplar clearly above the line — re-grounding 06 and 09 in the flip result instead.
The surviving claim would then be **narrower but defensible**:

> *The models differ on most designs. On a minority of designs the judges clearly disagree
> about the ordering; on the rest the systems are too tightly spaced for either judge to
> resolve. Either way, no comparative claim survives the swap.*

Note this narrower claim **still supports the paper's operational conclusion** — no
SUT-vs-SUT claim is licensed — and still supports paper (a)'s deferral of its leaderboard.
What it does not support is the stronger mechanistic story that judge disagreement about
ordering is what causes it *in every judged design*.

---

## 4. Verification performed (so the next session need not redo it)

**4.1 Design 07 has no judge-A ordering** —
`awk '/design 07\]/,/design 08\]/' logs/fullbank-3ep-20260724/judgeswap-ep{1,2,3}.txt`
→ judge-A is 0.0000 × 5 in ep1 and ep2; 0.0370 + 0.0000 × 4 in ep3. Confirmed.

**4.2 The flip criterion** — `tools/audit/pilot_judge_swap.py` ~line 181, quoted above.
Exact permutation equality, stable-sort tie-break. Confirmed. Design 06 ep1 magnitudes read
directly from `judgeswap-ep1.txt`. Confirmed.

**4.3 The df baseline** — computed directly from the reported df decomposition; 4 of 8
interactions below 13.79%; 3 of 8 SUT main effects below 13.79%. Confirmed.

**4.4 What I could NOT refute** — the decomposition arithmetic, the C1 intervals, the
medians and footprint ratio, the run shape and spend, the bank census, transplant fidelity,
holdout quarantine. Both reviewers attacked these independently and both conceded them.

## 5. Knock-on effects on already-settled artifacts

| Artifact | Status | Effect if Q1/Q3 are adopted |
|---|---|---|
| `20260725-fullbank-3ep-run-report.md` | committed, **immutable** | §0/§3 "nine of ten" needs a successor correction note — never an edit |
| `20260725b-variance-decomposition-addendum.md` | committed, **immutable** | §3's reading needs a successor addendum adding the df baseline |
| `RULINGS-APPLIED-20260725b.md` | written today, this session | its "framing correction" paragraph restates "non-zero in 8 of 8"; would need a successor ruling |
| phase-6 boot prompt | committed | carries the same framing forward |
| paper (a) | SHIP-WITH-FIXES | one sentence in §9 cites 8-of-8; adjust with Q3 |
| paper (b) | **DO-NOT-CIRCULATE** | abstract, §1, §5.3, §5.4 all affected |

**Report immutability is respected throughout: no existing dated report has been edited,
and none should be. Corrections travel as new dated successor files.**

## 6. What this session did NOT do, deliberately

- Did **not** re-frame either manuscript's central claim.
- Did **not** edit the committed run report or the decomposition addendum.
- Did **not** revise `RULINGS-APPLIED-20260725b.md` — a ruling is superseded by a new
  dated ruling, never by silent amendment.
- Did **not** compute Kendall's τ or add the df baseline to any manuscript, though both
  are $0 and offline, because both change what the paper claims.

Mechanically-verifiable defects from both reviews **were** fixed; they are listed in
`20260725-review-fixes-applied.md`.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
