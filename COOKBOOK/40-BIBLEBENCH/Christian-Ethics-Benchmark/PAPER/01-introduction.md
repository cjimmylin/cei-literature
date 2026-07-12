<!-- WALKWORTHY-CANARY-7f3e2026 -->
# 1. Introduction

**Status:** DRAFT — living document. **Owner:** Fable.
**Claim discipline:** every contribution paragraph ends with a bracketed license tag
`[LICENSE: …]` naming the condition under which it may survive to submission. Tags are
stripped at submission time by whoever holds sign-off (Jimmy-only, master-plan §5).

---

Language models increasingly serve users who hold specific, articulated moral
traditions — and who reasonably want to know not whether a model is "aligned" in the
abstract, but how it behaves when serving someone from within their tradition: whether
its advice, drafts, allocations, and multi-turn counsel accord with what that tradition
actually teaches. Existing ethics evaluations largely cannot answer this question. They
score models against crowd-sourced judgments, survey distributions, or philosophers'
dilemma corpora — ground truths that are either aggregations across traditions or
deliberately tradition-neutral. And they overwhelmingly measure *stated* values — what a
model says when asked — rather than *enacted* values: what it does across a drafting
task, a resource allocation, an escalating request, a counseling conversation.

We present **WALKWORTHY**, a benchmark family that measures the degree to which a
model's *behavior* accords with the consensus moral teaching of a named corpus of
fifteen works of Christian ethics, as operationalized through item-level anchors
citable to specific chapters of those works. The name is the construct: from the
Pauline injunction to "walk worthy of the calling," the family measures *walk*
(conduct), not *talk* (professed values).

Three design commitments distinguish the effort.

**A deliberately narrow construct.** WALKWORTHY does not measure whether a model "is
ethical" or "is Christian" — we take that construct to be unbenchmarkable in principle,
and its claim language is contractually forbidden throughout the project. What is
measured is accordance with *this specific corpus*: a declared fifteen-work Source
Registry whose consensus and internal disputes are documented claim-by-claim. Where the
corpus agrees internally but society polarizes (e.g., sexual ethics, end-of-life
questions), items are quarantined in a separately-reported *contested tier* scored as
fidelity-and-fair-representation when serving an in-tradition user — with a
refusal-quality rubric so that a model that respectfully declines is scored on how it
declines, never punished for declining. (The v1 bank ships this contested tier
schema-complete but deliberately unpopulated — a disclosed sequencing choice, §3.4.)
Where the corpus itself disagrees, items carry dispute tags and any well-executed,
registry-attested position earns credit. The
corpus's limits (Protestant-dominant; no dedicated Catholic, Orthodox, liberationist,
womanist, Pentecostal, or Global-South work) are disclosed in every reporting surface:
all claims are indexed to "this corpus," never to "Christianity."
<!-- source: 20260706-normative-charter.md §1, §2, §4, §5 -->

**Behavior over profession, method by method.** The family's ten designs are
*method-major*: each is built around one behavioral elicitation method rather than one
topic — cost-ladder obedience decay, multi-turn erosion under pressure, say–do twin
comparison, motive-sensitivity deltas, judge-free constrained allocation, rubric-profiled
advice, counsel-arc conformance, covert–overt protection gaps, two-seat symmetry, and
mercy-delta pairing. Topics (a fourteen-area registry from truth-telling to creation
care) cross-cut the methods, so any area × method cell is in principle observable and
the reporting spine forbids collapsing them into a single scalar.
<!-- source: 20260706-normative-charter.md §3, §6; prereg §B -->

**Governance before scores.** Every validity-relevant decision was frozen before the
data that could tempt us to bend it existed. Ten gates — headroom, spread,
capability-wash, judge validity against human labels, reference neutrality, lexical
shortcut, perturbation robustness, item kills, mandatory gap headlines, and a composite
ban — were pre-registered at design time and frozen to exact computations and decision
rules before any full-panel score existed. A release formula composes them: a design's
scores cannot be published at all until its gates clear, human-label validation of the
LLM judges being the release gate (scores land provisional; labels release them). Items
are never edited in response to model performance ("fix mechanics only"), and every
amendment requires a logged human ruling.
<!-- source: 20260706-master-plan.md §3; prereg §B/§C/§E; o5-framework §4 -->

## 1.1 Contributions

**C1 — The artifact.** Ten method-major designs; 356 authored public items (344
runnable) plus a 158-item private holdout (33.4% of the 473 authored seed cases),
stratified by area, difficulty, authoring wave, and author; a 14-area ethics registry with published coverage
matrices; a three-stratum ground-truth schema; a 12-entry intra-corpus dispute registry
with per-position credit; and 14 citation-verified anchor packs resolving every item
key to work-and-chapter.
`[LICENSE: assertable now as a construction claim. Any "validated instrument" phrasing
requires C5's gate outcomes.]`

**C2 — The construct.** A corpus-indexed *behavioral accordance* construct that answers
"whose values?" by declaration rather than aggregation, with contested-tier separation
and dispute-tagging as first-class schema rather than post-hoc caveats.
`[LICENSE: assertable now; charter frozen 2026-07-06.]`

**C3 — The governance.** A fully pre-registered gate system with frozen per-design
primary statistics, a cross-family judge architecture with home-advantage testing and
own-family exclusion, human-label validation waves, an eight-status release vocabulary,
and wave-based partial release. We document the gates working as designed: one design
already failed its headroom and spread gates on adjudicated data and is excluded from
any release this cycle pending difficulty rework — the pipeline treats that as the
system functioning, not as a result to suppress.
`[LICENSE: prereg narrative assertable now. The 05 instance is citable as REWORK-DIFFICULTY
(FR-5) — a gate outcome, not a model result. Further "gates caught X" instances only from
the O5 report.]`

**C4 — The template.** The pipeline — declared corpus → area registry → stratum schema →
method-major designs → pre-registered gated release — is *designed to instantiate* for
any normative tradition with a canonical corpus: the tradition-specific inputs are the
registry, the anchor packs, and the dispute table, while the gates, judge architecture,
and release machinery are tradition-independent. We claim design portability, not
demonstrated generality: exactly one instantiation exists, and demonstrating a second
is future work.
`[LICENSE: assertable ONLY with this hedge intact. "Shown to generalize" is forbidden.]`

**C5 — Feasibility and gated readouts.** A six-model frontier panel (2,064/2,064
records, zero schema errors) plus judging and adjudication cost under fifty dollars via
a commercial API gateway — evidence that tradition-specific, validity-gated benchmarking
is within reach of small research groups. Gate and release-status outcomes per design
are reported in §6 [SCAFFOLD]; per-design scores appear only for designs whose release
formula evaluates true, in the approved claim-sentence form.
`[LICENSE: mechanics assertable now (o4-panel-report, mechanics facts). Everything in §6
fills only from the post-adjudication readings file + O5 report; sign-off gated.]`

## 1.2 What this paper is not

This is a methods-first artifact paper. It is not a leaderboard: the results section
reports gate outcomes and release statuses, and scores only where release conditions
are met. It makes no claim that any model is or is not ethical, Christian, or aligned
with Christianity — sentences of that form are forbidden by the project's charter
regardless of what the data show. And it does not claim the corpus speaks for
Christianity; the corpus is the measurement standard, full stop.
<!-- source: 20260706-normative-charter.md §1, §8 -->

## 1.3 Paper organization

§2 situates the work against published values benchmarks, religious/cultural
evaluation, say–do evaluation, LLM-judge validity, and benchmark-governance literature.
§3 documents construction: corpus, areas, strata, designs, items, holdout. §4 gives the
measurement methodology: judging architecture, human-label protocol, the ten gates, and
the release formula. §5 describes the experimental setup. §6 reports gate outcomes and
released readouts. §7 discusses. §8 states threats to validity. Ethics and
reproducibility statements follow.
