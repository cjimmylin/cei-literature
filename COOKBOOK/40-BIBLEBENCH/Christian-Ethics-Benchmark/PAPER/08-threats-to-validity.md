<!-- WALKWORTHY-CANARY-7f3e2026 -->
# 8. Threats to Validity and Limitations

**Status:** DRAFT — living document. **Owner:** Fable.
**Rule:** this section states threats candidly even where a gate exists to answer them —
the gate is the *response*, not a reason to omit the threat. Update after O5 with
actual gate outcomes; never soften a threat because a gate passed.

---

## 8.1 Construct validity

**The corpus is not Christianity.** Every score is indexed to a fifteen-work,
Protestant-dominant corpus with no dedicated Catholic, Orthodox, liberationist,
womanist, Pentecostal, or Global-South work. A model faithful to Catholic moral
theology could score poorly in cells where the corpus's consensus diverges. We disclose
this in every reporting surface and forbid "Christianity"-level claims, but the
limitation is real: the construct measured is *accordance with this corpus*, and
readers who want a broader construct must not read one in.
<!-- source: 20260706-normative-charter.md §2 -->

**Consensus extraction is itself an interpretive act.** Anchor packs operationalize
"corpus consensus" via a ≥3-works-affirm / none-deny rule with citations, and disputes
are registered rather than resolved — but the claim inventory was assembled by the
project, not by the works' authors. Mis-stratified claims (a consensus tag that should
be a dispute tag) would mis-key items. The dispute registry, per-position credit, and
the contested tier bound this risk; they do not eliminate it.
<!-- source: 20260706-normative-charter.md §4 -->

**The contested tier is designed but unexercised.** The v1 bank ships zero stratum-(b)
items: the contested tier's scoring philosophy (fidelity-and-fair-representation for
in-tradition users, refusal-quality rubric) is schema-complete but has never been run
against a model. Claims about the contested-tier *machinery* are design claims until a
populated tier exists; the paper marks its contested-tier readouts not-applicable
rather than omitting them.
<!-- source: 20260709-O1-session-handoff.md §3; 20260706-master-plan.md §0 -->

**Behavioral scenarios under-determine ethics.** Ten methods sample the space of
"enacted values" (allocation, erosion, counsel arcs, …) but the sample is not
exhaustive, and each design's primary statistic is one operationalization among
several defensible ones. The frozen §B formulas make the choice explicit and
non-negotiable post hoc; they do not make it uniquely correct.

**Capability leakage.** A design can accidentally measure general capability rather
than value accordance. G3 tests this (Spearman ρ vs a six-benchmark capability
composite, PASS iff ρ ≤ 0.40), and any failing design is excluded from release as
capability-washed rather than shipped with a caveat. But at a six-model panel the
correlation is noisy (permutation p published; power disclosure mandatory), and for
design 01 capability is partially collinear with authorship provenance, disclosed
separately. A G3 pass at n = 6 is weak evidence of absence.
<!-- source: prereg §C-G3; o5-framework FR-3 -->

## 8.2 Measurement validity (judges)

**LLM judges are the central threat, and per-turn state coding is its sharpest edge.**
In the pilot, per-turn judge agreement fell to 0.43 and 0.49 on the two multi-turn
designs (vs 0.94 on the rubric design) — at least one judge is far from truth on
per-turn coding. Our response is structural, not rhetorical: no design's scores are
releasable until ≥2 cross-family judges individually reach κ ≥ 0.65 AND ≥ 0.80 × the
human–human ceiling against blind human labels on that design (G4), with an escalation
ladder and a rubric-decomposition rework path if judges fail. Until those labels exist,
every score in the project is formally provisional. The threat survives the mitigation
in one form: human labels validate judges on a sample; judge error on the unsampled
remainder is bounded only statistically.
<!-- source: prereg §D-4, §C-G4; human-label protocol -->

**Exploratory judging remained incomplete.** Although MVP-A1 persisted all 180 registered
PUBLIC item×SUT executions, its first inexpensive judge produced a response missing a
required rubric field before that pass completed, and the second judge was never invoked.
No missing judgment was imputed and no MVP judge-derived statistic is interpreted. The stop
exposes structured-output compatibility as an additional operational threat; it is not
evidence about model ethical performance or judge validity. **Small exploratory panel;
inexpensive, unvalidated judges; descriptive only; not release-grade evidence.**
<!-- source: 00-PORTFOLIO/20260713-mvp-a1-descriptive-stop-report.md §§3–5 -->

**Judge family overlap with SUTs.** The panel deliberately contains OpenAI and Google
SUTs while the judges are OpenAI- and Google-family; the generator family (Anthropic)
is also a SUT. Mitigations are pre-registered: a per-judge own-family inflation test
(Δ(J), permutation, α = 0.01) with rerouting on failure; a third-family tie-breaker
that never adjudicates its own family's cells; and every gate statistic computed on
the full panel AND minus-generator rows with the conservative row governing. Residual
risk: uniform (family-symmetric) judge severity biases pass Δ(J) by construction and
are caught only by G4's absolute κ floor.
<!-- source: prereg §E; o5-framework FR-7/FR-11 -->

**The tie-breaker is also a SUT.** After the preferred third-family model failed its
reliability probe, the tie-breaker of record is a model that also sits on the SUT
panel. Its own-family cells route to human adjudication rather than self-judgment, and
the overlap is disclosed — but tie-broken cells for other SUTs still carry a judge that
has a stake in the leaderboard sense. The same disclosure applies to the G7 paraphrase
author (no fully-disjoint frontier family exists once the panel spans the majors).
<!-- source: o5-framework FR-14; codex-full-handoff §2 -->

**Adjudication incompleteness is a selection effect.** Cells unresolved after
tie-breaking and human Part-B labeling are excluded with published counts; designs
above 10% unresolved S-units get no verdict at all (FR-1). Exclusion correlates with
judge disagreement, which plausibly correlates with the hardest moral content — so
released statistics may systematically under-weight exactly the items where models
diverge most. We publish exclusion rates per design × model so readers can bound this.
<!-- source: o5-framework FR-1; prereg §B adjudication rule -->

## 8.3 Human-label validity

**A single primary labeler who is also the project lead.** Part-A labels are blind and
drawn by fixed seed before adjudication outcomes existed, but the labeler is not
independent of the project. The protocol's ceiling arm (second labeler on a
double-labeled overlap, or a disclosed test–retest fallback) calibrates *reliability*,
not *independence*. Recruiting independent raters is future work and is the single
highest-value external check on the entire pipeline.
<!-- source: human-label protocol §5 -->

**Label volume.** 439 Part-A units across ten designs (per-design samples of ~30–60)
gives κ estimates with wide intervals on the rarer categories; the prevalence-paradox
guard (AC1 + raw-agreement supplements, escalation on divergence) is pre-registered
for the imbalanced designs.
<!-- source: human-label protocol §2/§4; o5-framework §3 row 5 -->

## 8.4 Internal / statistical validity

**Small panels everywhere.** Six SUTs bound G3's power (above), make G2's spread range
sensitive to single-model outliers, and mean per-design × per-area cells are thin
(≥2 items per covered area is a floor, not a comfort). We report per-cell n and forbid
composite claims without adjacent per-design cells (G10).

**Lexical shortcut and perturbation tests are themselves low-powered.** G6's
bag-of-words probe runs on ~31–49 items/design (marginal fails go to review, CI
disclosed); constant-key designs render G6 not-evaluable (disclosed, non-blocking,
amendment filed). G7 perturbs a deterministic 20% sample — flip-rates on the remaining
80% are extrapolation.
<!-- source: prereg §C-G6/G7; o5-framework FR-4 -->

**Proxy-scalar contamination of early signals.** All pilot numbers were computed on a
coarse illustrative scalar, not the frozen primaries; we treat them exclusively as
mechanics lessons and wave-prioritization signals, and the paper never cites a pilot
number as evidence about a model. The discipline exists precisely because two pilot
"ceiling" flags dissolved on inspection into proxy artifacts.
<!-- source: prereg §D -->

## 8.5 External validity

**Provider-mediated measurement.** All inference ran through one commercial gateway;
provider routing, quantization, and serving configuration are pinned only to the
extent the gateway pins them. Slugs and run manifests are recorded; bit-level
reproducibility of generations is not attainable and is not claimed.

**Time-boxed model panel.** The panel is a 2026 snapshot of six frontier models;
scores do not transfer to successors. The artifact's durable contribution is the
instrument and its governance, not the panel readout — which is why the paper is
methods-first.

**One instantiation of the claimed template.** We argue the pipeline instantiates for
any tradition with a canonical corpus (C4), but no second instantiation exists. The
tradition-specific labor (registry selection, anchor mining, dispute registration) is
the expensive part, and its difficulty likely varies across traditions in ways one
case cannot reveal.

## 8.6 Contamination and gaming

**Public-split exposure.** Released items enter future training corpora the day they
are released. Defenses: canary string in every released file, a 33.4% never-released
holdout stratified to mirror the public split, perturbation batteries before headline
claims, and paraphrase-not-quote discipline inside the paper itself. The holdout
defends the *benchmark*; it does not defend any individual public-split score, and
post-release scores on the public split should be read accordingly.
<!-- source: 20260706-normative-charter.md §6.6 -->

**Items were LLM-drafted (see Ethics Statement).** Two specific risks follow: (i)
stylistic regularities an LLM SUT might exploit — addressed by G6's lexical probe and
G7's paraphrase battery, both of which are partial (above); (ii) generator-family
familiarity advantaging the generator's sibling SUT — addressed by the minus-generator
sensitivity rows (FR-11 conservative-row rule). Residual risk is disclosed rather than
quantified.

## 8.7 What would falsify our validity story

We commit to reading the following as evidence *against* the instrument, not as noise:
G4 failures surviving the full escalation ladder on multiple designs; a human–human
ceiling below 0.65 on any design (category scheme unreliable — rework before any
release); Δ(J) own-family inflation in the frozen test; G7 flip-rates above 10%
post-revision; human contradiction of the refusal-adjudication semantics beyond the
pre-registered FR-15 thresholds. Each has a pre-committed consequence up to and
including no release of the affected design.
<!-- source: o5-framework §3/§6; prereg §C -->
