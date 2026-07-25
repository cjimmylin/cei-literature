**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

> **PART FILE — assembles into paper (a).** §§1–8 are drafted separately.
> Target paper: *WALKWORTHY: A Behavioral Benchmark for Christian-Ethics-Aligned Conduct in
> Language Models, Anchored to a Named Ethics Corpus.* Venue-generic and author-generic by
> ruling.

---

## 9 Limitations and non-claims

This section states what the instrument and its administration do not establish. It is
organised in three parts: limitations of the instrument itself, limitations of the
measurement reported in §7, and an explicit enumeration of claims the data do not license.

### Limitations of the instrument

**Single-benchmark scope.** All content- and construct-validity evidence in §8 is drawn
entirely from the WALKWORTHY v2 item banks. None of it speaks to generalisation beyond this
benchmark, to other corpora, or to other ethical traditions.

**Validity evidence rests on model raters.** Every agreement coefficient reported in §8 is
LLM-versus-LLM agreement under the IVR-1.1 review instrument, and each is read as an **upper
bound** on the human-rater agreement the same instrument would achieve, because two model
raters share systematic priors that two human raters would not. Keyed validity reaches
κ_w 0.760 on the public surface and 0.758 on the holdout, and mechanically derived severity
sits at κ_w 0.539 public and 0.627 holdout; these are ceilings on human reproducibility, not
estimates of it.

**Comparability discontinuities are structural, not incidental.** Bank revision 2026-07-24b
is not comparable to the 2026-07-16 pilot on the changed cells: design-07 items were
unscorable then and are validly scorable now, design-05 constraint satisfaction now enforces
a sum-correctness check that was previously waived on zero-budget items, design-04 zero-keyed
items are now excluded from the signed motive mean, WW-08-B02 was re-keyed, and four items'
prompt text changed. The pilot therefore **predates bank revision 2026-07-24b in every
respect** and is reported in §5 as development history rather than as results. Two further
comparability lines run alongside it. First, design-08 judge verdicts produced before and
after the 2026-07-24c rubric-anchor revision are **separate comparability lines and must
never be compared as cells**; the anchor changed the text the judge reads, so pre-anchor
stores (the pilot and the smoke judge-A verdicts) and post-anchor verdicts belong to
different instrument versions. Second, all `pushback_rate` figures produced before revision
2026-07-24b are **single-judge-era** figures from the judge-A period and carry no cross-judge
information at all.

**Design 07 is floor-saturated at this system tier.** `arc_pass_rate` sits at or near zero
under both judges on all five systems (judge-A 0.000–0.012; judge-B 0.000–0.062), with 27 of
27 items scored and none excluded, and the floor persists after the three repaired items
(WW-07-F02 / I04 / L02) became validly scorable. A floor is a **ceiling-room property of the
instrument at this tier** and cannot, by construction, exhibit between-model separation. Its
variance percentages describe noise around a floor and are excluded from every summary. The
design supports only the statement that none of these five systems clears the terminal
`faithful_counsel` bar.

**The corpus-distinctiveness triage is an annotation, not a test.** CV-1 records the
judgement that only designs 04, 05 and 10 are candidate-distinct from generic RLHF
harmlessness at cheap tier. This is a construct-validity annotation applied by inspection,
not an empirical discriminant test, and it needs a positive demonstration — a
harmlessness-only control system, or a discriminant correlation against a generic-safety
benchmark — before it can be stated as a finding rather than as a caveat. Its own provisional
status is visible in its revision history: the per-design non-generic share surfaced designs
06 and 07 at 96.3% non-generic each, ranking above two of the three designs CV-1 flagged, and
the annotation was amended to add them (PE-22). An annotation that moves under a descriptive
re-reading is not yet a discriminant.

**The design-08 protected-state boundary remains judge-dependent.** The rubric anchor added
under the 2026-07-24c ruling halved the watch-item flips in the smoke re-judge (4 of 30 to
2 of 30, with judge agreement rising from 25 of 30 to 27 of 30, and the only moved verdicts
shifting toward the keyed reading on the overt arm). The residual disagreement is documented
rather than resolved, and it is confirmed at full n in §7: `protected → steamrolled` is the
largest design-08 disagreement transition at **113 of 965 comparable verdicts (11.7%)**, with
a further 45 (4.7%) in the reverse direction, against overall design-08 agreement of 0.718.

**The branch classifier is pinned.** Branch classification is pinned at `gpt-4.1-nano` for
this lineage, carrying a documented cross-family disagreement property: two alternative
classifier families agree with each other at 0.902 but with the pinned route at 0.685–0.721,
and on 24.4% of branch turns both alternatives agree against it. Under the project's
no-cross-classifier-pooling rule (C6), cells produced under this pin **may never be pooled
with cells produced under any future cross-family pin**; such cells would constitute a
different experiment, not additional data.

### Limitations of the measurement

**Five systems under test, all cheap-tier.** Every conclusion in §7 is scoped to that tier.
The floor saturation, and the closely-spaced headline cells that make a modest interaction
sufficient to permute an ordering, are both tier properties and neither is known to hold
above it.

**Two judges only.** The judge contrast is a one-degree-of-freedom comparison between judge-A
(`gpt-4.1-nano`) and judge-B (`llama-3.3-70b-instruct`). It is not an estimate drawn from a
population of judges, and no percentage reported here may be read as "judges in general
account for X%." Whether the instability documented below is a pairwise property of these two
instruments or a genuine multi-judge fan-out is not decidable from two judges.

**The comparative surface is not merely deferred — it is unsupported at this
instrument-and-tier combination.** The earlier planning-round framing, which deferred a
leaderboard "to future runs", should not be read as a scheduling statement. The full-bank administration reported in §7 was
that run, and it returned evidence that the deferral condition may not be clearable here at
all: eight of the nine judged designs flip their system ordering between judge-A and judge-B, and the
one judge-free surface in the suite — design 05's `constraint_satisfaction_rate`, where the
two-judge precondition is satisfied by construction rather than by luck — yields **0 of 10
pre-registered pairwise contrasts with a Bonferroni-widened interval that excludes zero**. The
five systems span 0.0313 of constraint-satisfaction rate while per-item standard deviations
run 0.12–0.21, so the between-system signal is small relative to within-system item variance
at this n. This is a limitation of the instrument-plus-tier combination and **not** a defect
of the corpus or of the ten designs. The variance decomposition cited from the companion
analysis makes the mechanism precise: the models genuinely differ on most designs — the
system main effect is the single largest term in four of the eight judged, non-saturated
designs — and the system-by-judge interaction, read against its df-proportional no-effect
expectation of 13.79%, is clearly elevated in four designs (up to 46.5%), where it suffices
to permute the ranking of five closely-spaced systems; in the other four the systems are too
tightly spaced for either judge to resolve the ordering. *The models differ on most designs;
either way, no comparative claim survives the judge swap.*

**Reporting-surface discipline on design 02.** `break_turn` is the sole design-02 headline
for this instrument lineage. `pushback_rate` is a **secondary** metric, reported per judge
only, never pooled across judges, with every cell naming its judge, and it carries a standing
caveat that the cross-judge stability of the `pushback_with_alternative` state is
judge-dependent where tested and untested before revision 2026-07-24b. The §7 design-02 cells
follow exactly that surface.

**Smoke evidence is descriptive only.** The changed-items smoke rescore reported in §8 carries
no rankings and no composites; the per-channel spreads it reports are liveness evidence,
not model measurement. Its cell n's are 1–6 items by design and its
role is verification that the repaired instrument runs end to end, not model measurement.

### Explicit non-claims

The following are claims this manuscript does **not** make and which the underlying data do
not license.

1. **No system-under-test rankings, from any surface, anywhere.** No leaderboard is printed,
   and no ordering should be reconstructed from the descriptive cells in §7. The governing
   conclusion of the run is that no system-versus-system comparative claim is supported
   anywhere in this suite on this data.
2. **No claim that the referees prove any judge correct.** The two-referee meta-audit cited
   in §5.6–5.7 and §10 establishes reference-model *concordance*, not truth. That both referees side with
   one shipped judge on a design is evidence about the other judge's character, not a
   certification that the first is right; two referees may share correlated error inherited
   from similar training regimes.
3. **No pooled referee-agreement figure without its per-stratum split.** The referee sample
   is disagreement-enriched by construction, so a single overall-agreement headline would be
   invalid. Strata — control versus disagreement, and per design — are never pooled here and
   must not be pooled downstream.
4. **No religious-authority or theological-truth claim.** The corpus is a named fifteen-work
   registry, Protestant-Reformed-dominant and named as such, and direct Scripture anchoring is
   disallowed by construction. The benchmark measures **behavioral concordance with that named
   registry** — never fidelity to Christianity, to Scripture, or to moral truth. A response is
   described as aligned with the registry corpus, never as correctly Christian.
5. **v2 is parallel, not canonical.** The v1 harness remains the canonical execution path for
   release-grade evidence. No number in this manuscript is offered as release evidence.
6. **No cross-classifier pooling, ever.** Results obtained under different pinned classifiers
   are different experiments (C6).
7. **No comparative reading of the offline anchor-ablation or cross-family classifier
   analyses.** These are non-blind and post-pilot; their load-bearing conclusions are
   instrument-level and judge-level, not system-comparative.
8. **No significance language.** No hypothesis test is performed on any quantity reported
   here. Interval statements are phrased as "excludes zero" or "crosses zero."
9. **No holdout evidence.** A stratified 158-item holdout is withheld from all public
   surfaces and quarantined; it was untouched by this work, and no holdout content or
   identifier appears anywhere in this manuscript.

## 10 Future work

The ordering of this queue is itself an argument. **Instrument repair comes before further
measurement**, because more measurement on an instrument that cannot separate these systems
buys nothing: it purchases precision on quantities whose definitions are contested, and it
consumes budget and — in one case — a non-renewable asset.

**First, one bundled new instrument version: the design-02 taxonomy revision together with
the deferred cross-family classifier re-pin.** These must fire as a single new instrument
version rather than separately. Under the no-cross-classifier-pooling rule, a classifier
change alone creates a new experiment whose cells cannot be pooled with anything already on
record; if that discontinuity is going to be paid for, it should carry the taxonomy fix with
it. The evidence that design 02's problem is taxonomy-level rather than judge-quality-level
is convergent. It is the most judge-fragile instrument in the suite, with exact primary-field
agreement between judges of **0.232** across 1,041 pooled verdicts, and its variance is
**46.5% system-by-judge interaction sitting on a 5.8% system main effect** — judge
disagreement over a near-absent model signal. The two largest disagreement transitions both
involve the contested state, from the "held" side (`holds_line → pushback_with_alternative`,
142 turns, 13.6%) and from the "conceded" side (`pushback_with_alternative →
material_concession`, 127 turns, 12.2%). And the earlier two-referee meta-audit found that
**both shipped judges diverge from the referee consensus** on that design: the two referees
agree with each other at 0.735 (κ 0.653) on the disagreement stratum but with either shipped
judge at only 0.23–0.27, landing jointly on the same "neither" state on 83 of 200 contested
units. **The non-obvious conclusion, and the operative one: a stronger judge will not fix
design 02.** The states themselves are the defect. (This is a taxonomy question only. The
design-02 headline decision is closed — `break_turn` is the sole headline for this lineage —
and is not reopened here.)

**Second, the design-08 `protected → steamrolled` boundary.** Flagged as a watch item at
smoke scale and confirmed at full n — 113 of 965 comparable verdicts (11.7%), quantified as a
quantified in the companion analysis as a substantial system-by-judge interaction — this is an open instrument question about where an
exclusion-with-stated-ground stops honouring an embedded stake. It must be resolved before
any promotion of design-08 metrics to claims.

**Third, harder systems under test for design 07 — not a scoring fix.** The design is
floor-saturated at this tier under both judges even after the three item repairs, so the
floor is a property of the systems and the arc, not of the scoring path. The pastoral
comfort-then-truth arc may separate models above the cheap tier; nothing about it can be
learned by re-scoring what is already on disk.

**Fourth, design 03 may be judge-defined rather than model-defined.** Its variance is
**a near-uniform judge-level threshold shift rather than a reordering** (see the companion analysis) — the two judges apply near-uniformly
different thresholds rather than reordering the systems — and the dominant transition
(`no → yes`, 345 turns, 36.2%) is what collapses `say_do_gap` from the judge-A range to
approximately zero or below under judge-B on every system. This is worth investigating as a
rubric-threshold question: where exactly does the "do" side count as compliant, and can the
threshold be anchored so that it is a property of the rubric rather than of the reader?

**Fifth, a third judge.** Two judges can establish that an ordering is unstable; they cannot
distinguish pairwise noise between two idiosyncratic instruments from a genuine multi-judge
fan-out in which each judge imposes its own ordering. A third family also begins to convert a
one-degree-of-freedom contrast into something with a population interpretation.

**Sixth, at least three epochs as a standing budget requirement before any stability claim.**
This is the administration's own methodological finding: designs 03, 04 and 06 each read
stable in one or two epochs and judge-sensitive in the others, so a single-epoch run would
have reported those orderings as stable when they do not reproduce. Replication across epochs
is also what makes the system-by-judge interaction estimable separately from residual error
at all.

**Seventh, a discriminant-validity test to upgrade CV-1 from annotation to finding.** The
concrete forms are a harmlessness-only control system expected to pass the non-distinctive
designs while failing 04, 05 and 10, or a discriminant correlation against a generic-safety
benchmark. Until one of these exists, corpus-distinctiveness remains a caveat that scopes
claims rather than a result that supports them.

**Eighth — carried as a recommendation, not as a plan, and not yet decided.** The stratified
holdout's blind first use is a **one-shot asset**: once spent, first-use blindness cannot be
restored, and no subsequent analysis can recover it. The instrument demonstrably cannot
separate these five systems at present. The recommendation on record is therefore to **fix
discrimination first and spend the holdout after**. This has not been ruled, and it is stated
here as a recommendation awaiting a decision rather than as scheduled work.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
