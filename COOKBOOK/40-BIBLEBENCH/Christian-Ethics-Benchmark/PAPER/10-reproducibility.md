<!-- WALKWORTHY-CANARY-7f3e2026 -->
# 10. Reproducibility and Contamination Policy

**Status:** DRAFT — living document. **Owner:** Opus draft, pending Fable adversarial review.

This section states what we release and what we withhold, the contamination controls that
constrain both, the provenance discipline that makes every reported number traceable, and a
reproducibility checklist for later venue use. All release actions described here are
**conditional on a human-only release sign-off** by the project lead; nothing is published
automatically <!-- source: 20260706-master-plan.md §5 -->.

## 10.1 Released versus withheld

Conditional on release sign-off, the artifact repository is intended to contain:

- The **public split** of the benchmark: the runnable items and their authored siblings
  (356 authored / 344 runnable items across ten designs)
  <!-- source: outline.md §2 -->.
- The **anchor packs** (consensus claims with resolvable citations to the source corpus),
  the **harness code**, the **run manifests with fixed seeds**, the **judge rubric prompts**,
  and the **run transcripts**.

We **withhold**:

- The **private holdout** of 158 items (33.4% of the 473 authored seed cases), stratified on
  the same variables as the public split <!-- source: 20260709-O1-session-handoff.md §3 -->. This is a deliberate
  trade-off, disclosed here: we prioritize **contamination resistance over full
  reproducibility**. A withheld holdout means an independent party cannot re-run the exact
  holdout evaluation, but it lets us detect train-on-benchmark contamination in future
  models; we judge that trade worthwhile for a values benchmark and state it explicitly
  rather than leaving it implicit.
- **Raw human-label data** to the extent needed to protect labeler blinding and any future
  rater confidentiality; aggregate agreement statistics and the labeling protocol are
  released.

The holdout is described only by **count, percentage, and stratification variables**; it is
never loaded, quoted, or otherwise surfaced in this paper or in any released artifact
<!-- source: outline.md §6 -->.

## 10.2 Contamination policy

- **Canary.** Every released file — including every file of this paper — carries the canary
  comment `WALKWORTHY-CANARY-7f3e2026`, so that later models trained on scraped copies can be
  detected <!-- source: 20260706-normative-charter.md §6 -->.
- **Holdout isolation.** The private holdout is **never placed in version control** and never
  travels with the public artifact <!-- source: 20260706-normative-charter.md §6 -->.
- **Perturbation battery.** A required perturbation battery (paraphrase, name-swap,
  order-swap; the G7 gate) must be run before any headline claim, so that a result cannot
  rest on memorized surface strings <!-- source: 20260706-normative-charter.md §6 -->
  <!-- source: 20260712-fable-codex-full-handoff.md §4 -->.
- **Paraphrase-not-quote.** This paper **paraphrases runnable items and reports counts**
  rather than quoting them; the only verbatim item text that may appear comes from a small
  set of explicitly non-runnable illustrative sketches, marked as such
  <!-- source: outline.md §6 -->.

## 10.3 Determinism and provenance

- **Manifest-driven runs.** Runs are specified by manifest using **item identifiers, not item
  text**, so a manifest can be shared without leaking item content; **permutation seeds are
  fixed constants** (for example the label-sampling seed frozen at 20260710)
  <!-- source: 20260710-human-label-protocol.md §2 -->
  <!-- source: 20260712-fable-codex-full-handoff.md §4 -->.
- **Pinned model slugs via one gateway.** Every judge, classifier, tie-breaker, and
  paraphrase call uses an **explicit model slug** routed through a single API gateway;
  harness defaults are never relied upon for the frozen judge pair
  <!-- source: 20260712-fable-codex-full-handoff.md §7 -->.
- **Checkpoint / resume.** Panel runs checkpoint per cell and resume idempotently, so an
  interrupted run reproduces the same records on restart
  <!-- source: 20260712-fable-codex-full-handoff.md §2 -->.
- **Fail-closed MVP custody.** The stopped MVP-A1 snapshot retains the exact 60-item PUBLIC
  manifest, 180/180 SUT executions, a 27-record partial verdict file, and an append-only
  ledger containing 829 request attempts. Judging stopped at the first missing required
  rubric field; the absent Meta pass is explicit, and no missing verdict was inferred or
  backfilled. **Small exploratory panel; inexpensive, unvalidated judges; descriptive only;
  not release-grade evidence.**
  <!-- source: 00-PORTFOLIO/20260713-mvp-a1-descriptive-stop-report.md §§1–5 -->
- **Immutable, dated provenance.** Every reported number traces to a **dated, immutable
  report file**; reports are never overwritten or regenerated in place, and new results are
  written to new dated files <!-- source: 20260712-fable-codex-full-handoff.md §7 -->.
- **Frozen pre-registration.** The gate computations, statistics, and judge plan were
  pre-registered and frozen to exact form before any full-panel score existed; the frozen
  documents may be amended only by a **logged ruling**, never by silent edit
  <!-- source: outline.md §2 -->.

## 10.4 Verification

- A **mock-first test suite** (276 tests, no live API calls) exercises the harness end to end
  against recorded transcripts, so the pipeline can be verified without any paid inference
  <!-- source: 20260712-fable-codex-full-handoff.md §2 -->.
- **Exact reproduction commands** — for the mock suite, for a smoke run, and for a scored
  panel run from a shared manifest — will be included with the artifact release.

## 10.5 Reproducibility checklist

A venue-ready checklist; locations are placeholders to be resolved at artifact release.

| Item | Status | Location (placeholder) |
|---|---|---|
| Public item split (344 runnable / 356 authored) | Released (on sign-off) | artifact repository — `items/` |
| Private holdout (158 items, 33.4%) | **Withheld** by policy | not released |
| Anchor packs (corpus citations) | Released (on sign-off) | artifact repository — `anchor-packs/` |
| Harness code | Released (on sign-off) | artifact repository — `harness/` |
| Run manifests + fixed seeds | Released (on sign-off) | artifact repository — `manifests/` |
| Judge rubric prompts | Released (on sign-off) | artifact repository — `rubrics/` |
| Run transcripts | Released (on sign-off) | artifact repository — `runs/` |
| Raw human-label data | Withheld / aggregate only | protocol + aggregate stats released |
| Mock-first test suite (276 tests) | Released (on sign-off) | artifact repository — `harness/tests/` |
| Canary string in all released files | Enforced | every released file |
| Perturbation battery (G7) evidence | Released (on sign-off) | dated readings report |
| Pre-registration documents (frozen) | Released (on sign-off) | dated pre-registration files |
| Reproduction commands | To be included | artifact `README` at release |
