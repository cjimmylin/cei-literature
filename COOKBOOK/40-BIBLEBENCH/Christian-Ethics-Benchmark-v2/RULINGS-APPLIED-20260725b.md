# RULINGS APPLIED — 2026-07-25b: phase-6 assembly target and §7 disposition

**Date:** 2026-07-25 · **Session:** phase-6 (boot prompt `20260725c-boot-prompt-phase6-paper-assembly.md`)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Predecessor:** `RULINGS-APPLIED-20260725.md` (pushback_rate A′ close — untouched by this file)
**Spend:** $0. No model calls. Assembly and adjudication only.

---

## RULING 1 (Q1) — Assembly target: **(c) SPLIT. Both papers are live.**

**Owner ruling:** do both. ARM 1 and the variance decomposition become paper (b)'s
results; paper (a) is assembled in parallel as an instrument-and-validity paper whose
comparative surface is explicitly deferred, citing (b) for why.

**What this supersedes.** `REPORTS/20260724c-paper-skeleton-and-source-map.md` §0 ruled
"this skeleton assembles paper (a)". That ruling stands for paper (a)'s *outline*; it no
longer stands as an exclusive target. The skeleton predates ARM 1.

**Why the target moved at all.** Paper (a)'s abstract (06-messaging §3) defers the
leaderboard "to future runs that satisfy the first-use (blind) rule and resolve open
judge pins." ARM 1 *was* that run, and it did not clear the deferral condition — it
returned evidence that the condition may not be clearable at this SUT tier:

- 9 of 10 designs flip SUT ordering between judge-A and judge-B, in every epoch for 7 of
  them (R4).
- Design 05's judge-free `constraint_satisfaction_rate` — the only R4-survivable surface
  in the suite — yields **0 of 10** pre-registered C1 pairwise contrasts with a
  Bonferroni-widened interval excluding zero.

Meanwhile ARM 1 supplied paper (b)'s empirical core and strengthened it well past the
pilot: full bank rather than pilot, rev 2026-07-24b rather than the old bank, 3 epochs
rather than 1, a quantified `SUT×judge` interaction non-zero in 8 of 8 judged designs,
a judge-free positive control, and the finding that single-epoch stability verdicts are
unreliable.

**Division of evidence between the two papers (binding):**

| Evidence | Paper (a) | Paper (b) |
|---|---|---|
| Corpus, construct, registry, public/holdout split | **primary** (§3) | compressed testbed (§3) |
| Ten behavioral designs | **primary** (§4) | compressed testbed (§3) |
| Item development, review, PE ledger | **primary** (§5) | not carried |
| Item-quality / validity evidence (IVR-1.1) | **primary** (§8) | not carried |
| 2026-07-16 pilot | development history (§5), see RULING 2 | motivation only, no cells |
| ARM 1 full-bank 3-epoch run | descriptive instrument readings (§7) | **primary results** (§5) |
| Variance decomposition | cited, not derived | **primary results** (§5) |
| Two-referee $0 meta-audit (Opus, Sol) | one paragraph + citation | **primary method** (§4) |
| R4 two-judge rule, C6, C9 | stated as governing rules (§6) | **primary object of study** |

**Cross-citation rule.** Each manuscript must be self-contained on its own claims. Paper
(b) carries a compressed instrument description sufficient to read its results without
paper (a) in hand; paper (a) states the judge-sensitivity finding qualitatively and
cites (b) for the analysis rather than reproducing the decomposition. Neither may depend
on the other being published first.

## RULING 2 (Q2) — §7: **execute the skeleton's own contingency.**

The skeleton flagged this and the trigger has fired:

> "Pending adjudication: whether §7 survives at all if a full-bank rescore (phase-4 ARM 1)
> lands on rev 2026-07-24b first — if it does, pilot becomes a development-history
> subsection and the rescore becomes §7. Flag at assembly time."

**Ruled:** executed as written.

1. The 2026-07-16 pilot becomes a **development-history subsection under §5** of paper
   (a). It is reported **as process** — what it was run for, what it caught, what it
   changed. Its per-cell leaderboard-shaped numbers are **not** reproduced.
2. The ARM 1 full-bank run becomes **§7** of paper (a), reported as descriptive
   instrument readings plus the negative result.
3. In paper (b) the same disposition holds without section numbering: the pilot is
   motivation and development history; ARM 1 is the results.

**Consequence for C9 (the reason this is the right call).** §7 now reports **first-ever
numbers on bank revision 2026-07-24b**. Under C9 that is new data on a new bank, so the
pre-registered C1/C2 families are reportable *as pre-registered* rather than under the
"post-hoc on pilot data — hypothesis-generating" label. Retaining pilot cells as results
would have required a comparability fence on every figure (d07 items unscorable pre-fix;
B02 re-keyed; d05 CSR silently waived on zero-budget items; d04 zero-keyed items pooled
into the signed mean; four items' prompt text changed) and forced the reader to track two
incompatible bank revisions through one results section.

## Carried forward UNCHANGED — not reopened by this ruling

- **`pushback_rate` is CLOSED** (`RULINGS-APPLIED-20260725.md`, A′ affirmed). `break_turn`
  is the sole design-02 headline for this lineage, permanently. `pushback_rate` is
  SECONDARY, per-judge, never pooled, standing caveat attached. Not a queue item.
- **Holdout: recommended NOT to spend; owner has not ruled.** Blind first-use is a
  one-shot asset. Recommendation on record: repair discrimination first, spend after.
  Untouched and quarantined by this session.
- **Classifier pinned at `gpt-4.1-nano`** (`RULINGS-APPLIED-20260724e.md`). The v-next
  cross-family re-pin is unfired and deferred, and under C6 must not fire alone — it
  bundles with the d02 taxonomy revision as one new instrument version.
- **Bank revision 2026-07-24b.** No code, rubric, metric, or bank edit in this session.
- **Report immutability.** `20260725-fullbank-3ep-run-report.md` and
  `20260725b-variance-decomposition-addendum.md` are committed and immutable. This file
  and all manuscript parts are new successor files.

## Framing correction that binds both manuscripts

**Do NOT write "the judge dominates."** That framing was corrected in the variance
decomposition addendum §3 and must not re-enter a manuscript. Judge and SUT footprints
are comparable at the median (35.3% vs 35.6%, ratio 1.0×), and the SUT main effect is the
single largest term in several designs (06: 63.4%, 09: 54.4%, 04: 46.3%, 01: 45.4%).
**The models genuinely differ.**

**The claim that survives, and the only one to write:** *the models differ, but the
judges disagree about the ORDERING in every judged design.* The decision-relevant term is
the interaction `SUT×judge`, non-zero in 8 of 8 judged designs (median 17.2%). Designs
01/06/09 are the sharpest illustration — a substantial genuine model effect that still
fails R4, because a 9–23% interaction suffices to permute the ranking of five
closely-spaced systems.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
