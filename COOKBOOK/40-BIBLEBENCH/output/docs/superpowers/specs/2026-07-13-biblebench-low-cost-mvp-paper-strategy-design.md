# BibleBench Low-Cost MVP Paper Strategy

**Date:** 2026-07-13
**Status:** OWNER-APPROVED DESIGN; awaiting written-spec review
**Owner:** Jimmy Lin
**Scope:** Consolidated FruitBench, CORINTHLOVE, 10CBench, and SermonMount pilot

## 1. Decision

BibleBench will optimize first for a complete, inspectable MVP paper rather than
for a definitive benchmark release. The first empirical preview will use three
inexpensive general-purpose models under a **$5.00 absolute spend cap**. It will
use the founding theologian-technical owner as the sole judge and will defer
expensive models, larger panels, formal concordance, and release-grade
hardening until the owner has reviewed the complete paper-shaped artifact.

The purpose of this phase is to learn what the paper, analyses, tables,
limitations, and benchmark PDFs actually look like. It is not to establish a
leaderboard, a final model comparison, Christian consensus, or population-level
benchmark validity.

## 2. MVP empirical geometry

The MVP uses all 48 frozen episodes so that all four passage benchmarks retain
representation:

- 12 FruitBench episodes;
- 12 CORINTHLOVE episodes;
- 12 10CBench episodes; and
- 12 SermonMount episodes.

Each of the three models receives one preregistered prompt surface per episode,
normally the C1 de-cued surface, plus the matched observable probe. This yields
an intended maximum of:

`48 episodes × 3 models × 2 calls = 288 calls`

The exact surface, provider route, model identifiers, context limits, token
caps, retry policy, and forecast cost must be frozen in the run manifest before
the first paid call. If C1 cannot faithfully preserve a Christian-facing task,
the episode is excluded or receives an explicitly registered surface exception
before execution; the surface is never changed after viewing a response.

The MVP does not execute all C0/C1/C2 variants and therefore does not estimate
cue effects. It also does not execute capability twins and therefore does not
make capability-adjusted ethical attributions.

## 3. Model and spend policy

The roster contains exactly three currently available, inexpensive,
general-purpose language models. Selection occurs at a just-in-time preflight
so the roster reflects current availability and pricing. The selection should
prefer three distinct model families when feasible, but diversity never
overrides the spend cap.

The financial rules are:

1. **$5.00 is a hard not-to-exceed cap**, including retries.
2. The preflight forecast should target no more than $3.00, preserving at least
   $2.00 for bounded transport retries or price variance.
3. If the forecast exceeds $5.00, reduce token caps or replace models; do not
   raise the budget inside the MVP phase.
4. A failed cell receives at most the preregistered bounded technical retry.
   Thereafter it remains missing and is reported as such.
5. The run stops automatically at the first of roster completion, the spend
   cap, a custody failure, or a P0 safety/integrity event.

This strategy sets the ceiling and roster class. It does **not** by itself
authorize credentials, provider access, or paid calls. The exact three-model
manifest and forecast require a separate owner authorization immediately before
execution.

## 4. Minimum human-judging design

Jimmy Lin serves as the founding theologian-technical judge. The MVP requires:

- one scientifically adequate pass over episode-level provisional gold;
- one blinded scoring pass over each completed model episode bundle;
- separate observable-behavior and passage-interpretation judgments where
  applicable;
- brief rationales for red lines, contested cases, revisions, rejections, and
  deferrals; and
- explicit preservation of `NOT_APPLICABLE` as a non-score.

The MVP does not require a second judge, a formal theologian panel, a domain
expert panel, an expensive judge model, or formal inter-rater concordance. A
blinded intra-rater repeat may be reported if it is already inexpensive and
ready, but it is not a prerequisite for generating the MVP paper preview. If it
is omitted, the manuscript must remove or retain as future work every
repeat-stability claim.

The resulting labels remain `single_expert_provisional_gold`. They do not
represent Christian consensus, multi-judge validation, or a definitive account
of evangelical-Protestant interpretation.

## 5. Permitted paper claims

The MVP paper may report:

- the four-benchmark shared-episode design;
- the distinction between observable ethical behavior and biblical or pastoral
  interpretation;
- execution feasibility, completion, missingness, and custody outcomes;
- descriptive module-native patterns for the three inexpensive models;
- common-life versus Christian-facing descriptive observations;
- action/probe consistency and registered red-line incidents;
- qualitative examples selected under a declared procedure; and
- the limitations of a small model roster and one founding expert judge.

The MVP paper must not claim:

- a best model, general leaderboard, or stable model ranking;
- family-level estimates for construct families represented by one episode;
- C0/C1/C2 cue effects;
- capability-adjusted ethical failure;
- inter-rater reliability, cross-tradition agreement, or Christian consensus;
- broad external validity to deployed systems or real-world conduct; or
- release readiness, hostile-deployment robustness, or definitive benchmark
  validation.

All reported model comparisons are exploratory and descriptive. Uncertainty,
missingness, and item dependence remain visible rather than being compressed
into a qualified composite score.

## 6. Paper-shaped closing artifact

The MVP phase closes only when the owner can inspect a complete preview package:

1. a venue-neutral methods-and-pilot manuscript;
2. a frozen three-model run manifest and spend ledger;
3. descriptive tables and figures for all four modules;
4. a limitations and claim-boundary section;
5. the required benchmark PDF reports; and
6. a one-page scale-up decision memo.

The manuscript may use explicit placeholders before the run, but after the MVP
run it must contain the actual pilot results or a documented failure account.
Engineering test counts alone do not satisfy this closing condition.

## 7. Deferred work and scale-up gate

Until the owner reviews the complete MVP preview, defer:

- additional or premium model families;
- model panels large enough for formal concordance;
- paid or larger human-judge panels;
- all-surface C0/C1/C2 experiments;
- capability-twin execution and capability-adjusted attribution;
- formal family-level estimation;
- composite rankings or leaderboard construction;
- production transport, hostile-deployment, and broad compatibility hardening;
  and
- publication-scale layout polish beyond readable, verified PDFs.

No scale-up is automatic. After reviewing the MVP paper, the owner chooses one
of three dispositions:

- **stop:** the paper or benchmark is not promising enough to expand;
- **repair:** make a bounded content or analysis correction and rerun only the
  affected cells; or
- **scale:** authorize a larger model roster, higher spend, stronger judge
  design, or additional experimental surfaces through a new registered phase.

## 8. Critical-path and stop rules

Only the following may block the MVP preview:

- a P0 evidence, safety, or custody failure;
- a P1 that could materially change an MVP paper conclusion;
- absence of a minimally usable provisional-gold subset;
- inability to freeze a reproducible one-surface schedule;
- inability to remain within the $5.00 cap; or
- lack of exact owner authorization for the final paid manifest.

P2/P3 robustness, compatibility, judge-scale, and release concerns are disclosed
and deferred. Review loops stop when the narrowed MVP claims are scientifically
adequate, even when the broader benchmark remains provisional.

## 9. Supersession and implementation targets

After written-spec review, this design should be memorialized as a new ratified
entry in `PAPER-FIRST-DECISIONS.md` and reflected in:

- `PAPER-FIRST-WORKFLOW.md`;
- `ACTIVE-CRITICAL-PATHS.md`;
- `project-dashboard.html`;
- the consolidated pilot manuscript and claims registry; and
- the exact pilot run manifest and budget checkpoint.

This ruling narrows the first empirical milestone. It does not weaken immutable
evidence custody, safety boundaries, truthful limitation reporting, or the
requirement for separate authorization before paid execution.
