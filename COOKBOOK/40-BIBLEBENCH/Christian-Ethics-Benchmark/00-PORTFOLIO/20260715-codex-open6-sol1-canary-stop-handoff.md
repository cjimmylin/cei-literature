# WALKWORTHY OPEN6-SOL1 — canary-stop handoff

**Date:** 2026-07-15 (PDT)

**Agent:** Codex

**Scope:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/`
only

## Paper-facing outcome

No OPEN6 descriptive results supplement was produced because the registered
six-SUT canary gate failed. The paper-facing artifact is instead the immutable
canary-stop report:
`00-PORTFOLIO/20260715-open6-sol1-canary-stop-report.md`.

The existing private MVP v0.1 manuscript/PDF and every O5 surface remain
unchanged. Human labels still control G4, verdict assembly, and the next
release-grade paper conversion.

## Work completed

1. Implemented the exact six-model / single-Sol-judge pilot under TDD, including
   immutable manifest/catalog custody, one-replay ledgers, max-two concurrency,
   `$15/$23/$25` budget controls, resume-only-missing behavior, explicit
   permanent missingness, systemic stops, full fake execution, canaries, and
   judge-aware stop checkpoints.
2. Closed all independent P1 review findings. Final serial OPEN6 suite:
   **127/127 green**.
3. Froze manifest SHA-256
   `4e21b2ecc9726fd92cbdb9c3b4efa44e2cf1fb37070e0dce714c35705dcff64c`
   and catalog SHA-256
   `7f11cde7939cbd8d5f0eee420a8bdb4046f5887f5cc84a2b28c52ab09fa61996`.
4. Completed the persistent `$0` fake run at exact geometry: 2,064 records,
   5,886 calls, 1,722 routes, 5,370 units, 10,008 cells, 227 batches.
5. Ran the live canaries. Both Sol canaries passed; MiniMax and GLM passed;
   DeepSeek returned HTTP 404 on the first exact request and its one identical
   replay. The driver stopped before any remaining or production work.

## Stop state

- OpenRouter: 4 attempts / 1 replay / 2 successes / `$0.0320949696` booked /
  `$0` inflight.
- Sol: 2 canary attempts / 2 successes / 0 production turns.
- SUT records: 2 complete / 2,062 missing under the original 2,064 denominator.
- Judge work: not entered.
- HOLDOUT: never loaded.
- Append-only stop key:
  `stop:74ae25e67fddfaae9b0bf1be47fdefd6`.

## What remains and next trigger

OPEN6-SOL1 has no permitted automatic continuation under the current contract:
the required DeepSeek canary exhausted its one replay. Do not rerun the execute
command, waive the canary, substitute a model/provider outside policy, or add a
third attempt without a new explicit Jimmy amendment.

The highest-value independent next session remains the already prepared
label-triggered path: once one design has complete primary labels, reliability
labels/declaration, and disagreement adjudications, run G4 → available Part B →
verdict/status → manuscript/PDF conversion.

If Jimmy instead wants OPEN6 resumed, the next input must be one bundled explicit
owner amendment resolving the failed canary and its exhausted logical key. No
additional engineering or paid request should precede that decision.

## Ancillary work and why it was blocking

Execution-custody engineering and independent P1 reviews were performed only
because they directly gated the authorized full pilot. After the required canary
failed, no analysis, PDF polishing, model expansion, or workaround work was done.
