# WALKWORTHY — MVP Paper Strategy Handoff

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Scope:** WALKWORTHY strategy/documentation only
**Status:** MVP-PILOT strategy ratified and propagated; no live model call authorized

## Paper-facing progress

Jimmy approved a separate exploratory MVP-PILOT so the team can review the complete
paper shape before paying for a larger panel or stronger judges. The binding amendment
is `20260713-walkworthy-mvp-paper-strategy-amendment.md`:

- 60 deterministic PUBLIC items: first 2 runnable easy + first 4 runnable hard items
  by ID for each of the ten designs;
- 3 inexpensive SUTs and 2 inexpensive cross-family judges;
- $5.00 NTE, with a checkpoint before projected spend exceeds $3.00;
- at least 90% completeness per design×SUT descriptive row; and
- exploratory/descriptive claims only, never rankings, gates, release verdicts, item
  kills/demotions, or substitutes for human/O5 validation.

The existing O5 lane remains the sole release-grade lane and was not rewritten.

## Surfaces updated

- `AGENTS.md`: immediate paper priority now points to the MVP amendment while preserving
  O5 and the separate paid-run gate.
- `00-PORTFOLIO/project-dashboard.html`: live status, forecasts, progress, rulings,
  lanes, document map, changelog, and §12 now expose the MVP contract and the next
  roster/budget planning session.
- `../ACTIVE-CRITICAL-PATHS.md`: stale PR-13 state replaced by the ratified MVP contract.
- `../PAPER-FIRST-DECISIONS.md`: PF-004 records Jimmy's owner-approved WALKWORTHY
  exception and preserves the separate paid-run gate.
- `../project-dashboard.html`: WALKWORTHY card, P1 summary, next-session instruction,
  and update log reconciled.

## Next paper-conversion trigger

Run the dashboard §12 session to:

1. verify current OpenRouter availability/prices;
2. name exact 3-SUT and 2-judge cheap slugs;
3. calculate worst-case calls/spend including probes, classifier, judges, and retry
   reserve; and
4. present Jimmy a one-line paid-run authorization request capped at $5.00.

That planning session must make no credential, balance, or paid model call. After Jimmy
separately authorizes the exact order, execute the bounded pilot and immediately fill
the MVP paper results/limitations preview.

## Concurrency and custody note

An active WALKWORTHY W4 implementation and unrelated sibling/portfolio staged work were
already present in the shared worktree. This strategy session did not edit W4 source or
tests, did not touch sibling benchmark files, and did not stage or commit over the
existing shared index. Its documentation paths must be isolated at the next safe
session-close commit.
