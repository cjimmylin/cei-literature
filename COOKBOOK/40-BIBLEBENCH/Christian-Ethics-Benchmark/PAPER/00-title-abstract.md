<!-- WALKWORTHY-CANARY-7f3e2026 -->
# Title & Abstract (skeleton)

**Status:** DRAFT — living document. **Owner:** Fable. Abstract slots fill LAST (outline §4.5).

---

## Title

**Primary:** WALKWORTHY: A Method-Major Benchmark Family for Measuring Behavioral Accordance with a Declared Corpus of Christian Ethics

**Alternate:** Walk, Not Talk: A Gated, Pre-Registered Benchmark Family for Tradition-Specific Value Accordance in Language Models

**Authors:** [AUTHORS] · [INSTITUTION] *(swap block, outline §7)*

## Abstract (slotted skeleton — ~250 words when filled)

> Existing ethics benchmarks for language models predominantly score agreement with
> crowd-sourced or universalist moral judgments, leaving a basic question unmeasured:
> whether a model's *behavior* accords with the teaching of a *specific, named normative
> tradition* — the question that matters to communities who want to know how a model
> serves users from within their tradition. We present WALKWORTHY, a benchmark family of
> ten method-major designs measuring whether model behavior — advice trajectories,
> allocations, drafts, and multi-turn counsel — accords with the consensus moral teaching
> of a declared corpus of fifteen works of Christian ethics. The construct is deliberately
> narrow: accordance with *this corpus*, never "being ethical" or "being Christian."
> The family comprises 356 authored public items (344 runnable; a further 158-item
> private holdout, 33.4% of authored seed cases) across a 14-area registry, with a
> three-stratum ground-truth schema that routes societally-contested doctrine to a
> separate fidelity tier (schema-complete, deliberately unpopulated in this release)
> and grants per-position credit on intra-corpus disputes. Measurement is governed end-to-end by
> ten pre-registered validity gates — headroom, spread, capability-wash, judge validity
> against human labels, reference neutrality, lexical shortcut, perturbation, item kills,
> mandatory gap headlines, and a composite ban — frozen to exact computations before any
> panel score existed, with a release formula under which a design's scores may not be
> published at all until its gates clear. [SLOT-A: one sentence — gate/status outcomes
> per design from the O5 report.] [SLOT-B: one sentence — headline released readouts,
> approved claim-sentence form only.] We release the public split, harness, rubrics, and
> the full pre-registration trail [SLOT-C: artifact URL — release is sign-off-gated],
> and argue the pipeline instantiates for any tradition with a canonical corpus.

**Slot rules:** SLOT-A/B fill only from the O5 gate-adjudication report; SLOT-B only for
designs with status RELEASED + sign-off; if the released set is small, SLOT-B reports
statuses instead of scores — that outcome is publishable as-is (methods-first framing).

## Keywords

LLM evaluation · values benchmarks · benchmark validity · pre-registration ·
LLM-as-judge · religious values · construct validity
