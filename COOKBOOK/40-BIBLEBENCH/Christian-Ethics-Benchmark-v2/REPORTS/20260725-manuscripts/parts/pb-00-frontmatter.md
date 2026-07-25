PART FILE — assembles into paper (b). Title, abstract, keywords.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

---

# Judging the Judges for $0: A Two-Referee Concordance Method for Localizing LLM-as-Judge Failure on Value-Laden Rubrics

> **STATUS: v0.1 — DO NOT CIRCULATE.** An adversarial review returned three blocking
> findings. The verified factual corrections have been applied. Two contested
> interpretive questions remain open and are escalated for owner adjudication in
> `20260725-ESCALATION-claims-validity.md`: whether the ordering-flip test is
> reportable without a calibrated null, and whether variance shares must carry a
> df-proportional no-effect baseline. **Both bear on the central claim of this paper**,
> and both are deliberately left unresolved here rather than settled by the drafting
> session.

*Venue-generic and author-generic draft. No venue, authorship, acknowledgements, or
funding statement has been decided for this manuscript.*

## Abstract

LLM-as-judge scoring is now standard for value-laden benchmarks, yet a cheap judge can
silently drive the result. On a ten-design behavioral benchmark anchored to a named
fifteen-work Christian-ethics registry, we administer the full public bank — 344 items
across 563 administration lines — to five cheap-tier systems under test in three
independent epochs, and rescore every administration offline with a second judge drawn
from a different model family, so that the only variable between scorings is the judge.
**Eight of the nine judged designs flip their system ordering under the swap.** The ninth
judged design is floor-saturated — its judge-A headline is 0.000 on all five systems in two
of three epochs — and so yields no ordering to test. The tenth design, whose primary metric
is computed from a parsed allocation against keyed constraints and never reaches a judge at
all, does not flip by construction.

Because three epochs were run, the judge's footprint is recoverable quantitatively rather
than as a binary verdict. We decompose each design's headline variance into system, judge,
system-by-judge, and epoch-noise components, using the epochs as replicates — which is
what makes the interaction estimable separately from residual error. The decomposition
corrects a tempting reading. The judge does not simply dominate: system and judge
footprints are comparable at the median (35.6% versus 35.3%), and the system main effect
is the single largest term in four of the eight judged, non-saturated designs, reaching
63.4%. **The models genuinely differ.** What voids comparison is the interaction. The
system-by-judge term is non-zero in all **8** judged, non-saturated designs (median 17.2%), and an
interaction of that size is enough to permute the ranking of five closely-spaced systems
even where the underlying model effect is large. The claim the data support is therefore
narrower and more useful than "the judge decides": *the models differ, but the judges
disagree about the ordering in every judged design.*

Two controls guard the inference. The judge-free design is an exact positive control — its
judge and interaction terms are 0.000000 by construction and are recovered as such — and
its pre-registered pairwise contrasts yield **0 of 10** Bonferroni-widened intervals
excluding zero — inconsistent with, though at this n not excluding, the reading that a real
ranking is merely being obscured by judge noise. Replication yields a further methodological result the single-epoch
predecessor could not produce: **single-epoch judge-stability verdicts are unreliable**,
with three designs reading stable in one or two epochs and judge-sensitive in the others.

Finally, we localize *where* the judging fails at no API cost. Two independent frontier
referees, dispatched through subscription channels and run blind on a frozen,
disagreement-enriched sample, partition the shipped judge pair's failure into a
judge-character component, a rubric-and-state-taxonomy component, and a small set of
defect items whose empty keyed anchors mechanically generate disagreement. We frame
referee agreement throughout as **reference-model concordance, not ground truth**: two
referees may share correlated error. We offer the combination — cross-family judge swap,
epoch-replicated variance decomposition, and $0 two-referee localization — as a
pre-publication QA pattern for any benchmark whose rubric encodes contested values.

## Keywords

LLM-as-judge; evaluation validity; judge sensitivity; variance decomposition; benchmark
methodology; value-laden rubrics; reference-model concordance; inter-rater agreement

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
