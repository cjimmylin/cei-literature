# WALKWORTHY v2 — Owner Briefing Suite (scale-up readiness)

**Date:** 2026-07-17 · **Status:** internal briefing artifacts — writing-only session;
no benchmark, analysis, or instrument changes were made in producing these reports.
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content anywhere in this suite.

## What this is

Six reports reviewing the full WALKWORTHY v2 arc (Christian-Ethics-Benchmark-v2 on
Inspect AI) from the 2026-07-15 migration through the 2026-07-17 Sol referee arm, written
to support the owner's scale-up decision (many-SUT leaderboard run → leaderboard paper +
benchmark-design paper). All existing memos remain the immutable primary records; these
reports consolidate and supersede nothing except by pointer.

## Reading order

| # | File | What it answers | Length |
|---|------|-----------------|--------|
| 1 | `01-benchmark-card.md` | What is the benchmark? Composition, all 10 designs with full example items and good/bad responses, methodology, innovations, limitations | longest |
| 2 | `02-evaluation.md` | What has it been run on and how did models do? Every live run, scoring/judging mechanics, per-design results, the caveated leaderboard | long |
| 3 | `03-meta-judging.md` | Were the judges judged? The two-arm referee meta-audit (Opus + GPT-5.6-Sol, n=942, $0), findings, and the 5 open decision hooks | medium |
| 4 | `04-development-history.md` | How did we get here? Consolidated lab-notebook history, F-ledger, spend & governance | long |
| 5 | `05-next-steps.md` | Are we ready to scale up? Four readiness axes, gap ladder, candid verdict | medium |
| 6 | `06-messaging.md` | What's the headline? Ranked findings; title + abstract drafts for both papers | short |

Figures are in `figures/` (generated offline from the two referee agreement JSONs and
stored pilot logs by `figures/make_figures.py`; provenance per figure in
`figures/README.md`). Working files (real example transcripts extracted from pilot logs,
the authored design-07 exemplar, judge-swap numbers) are in `working/`.

## The four rulings that shaped this suite (owner, this session)

1. **Leaderboard:** shown, but caveated — labeled post-hoc/hypothesis-generating per the
   C9 first-use rule, both judges side-by-side, flips annotated (02-evaluation §5).
2. **Examples:** hybrid — real pilot transcripts where a clean pair exists; authored
   rubric-keyed exemplars where none does (design 07's "good"), every example
   provenance-labeled.
3. **Decision hooks:** presented as OPEN with evidence; nothing was ruled this session.
4. **Messaging:** both papers drafted — the benchmark-design/leaderboard paper and the
   judge meta-audit methods note.

## Standing guardrails (apply to every report in this suite)

The referee meta-audit is NOT benchmark work and adds nothing to the benchmark. "Closer
to Opus/Sol" = reference-model concordance, not ground truth — the referees are stronger
models, not oracles; two referees agreeing may share correlated error (consensus
evidence, not correctness evidence). Results change NO judge pins, enter NO benchmark
reports, and trigger NO instrument changes without a separate explicit owner ruling
(R1/R3/C9 + RATIFIED F11 govern benchmark claims; this data lives outside that
instrument). The referee sample is deliberately disagreement-enriched — no pooled
"overall agreement" headline without the per-stratum split adjacent. No SUT-vs-SUT
ordering claims exist anywhere in this suite (R1/R4); the §5 leaderboard in
02-evaluation is hypothesis-generating only. v2 remains a PARALLEL experiment to
canonical v1 by owner ruling.

## Authoritative number sources

`logs/jr-referee-20260716/referee-agreement.json` · `referee-agreement-sol.json` ·
`20260716-pilot-report.md` §1–§3 · `20260715-conversion-parity-report.md` ·
`working/judge-swap-numbers.json` (offline recompute; provenance nuance documented in
02-evaluation §5).

Canary: WALKWORTHY-CANARY-7f3e2026
