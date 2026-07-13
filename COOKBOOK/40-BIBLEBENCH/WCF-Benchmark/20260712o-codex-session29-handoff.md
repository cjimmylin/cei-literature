# WCF-Bench — Codex Session 29 Handoff

**Date:** 2026-07-12

**Branch:** `main`

**Scope:** Jimmy-authorized shadow judge bakeoff design checkpoint. No live calls or spend.

On session open: load `project-dashboard.html` (Live-status first).
On session close: update the dashboard per `AGENTS.md §The project dashboard`.

## Completed

- Jimmy chose **shadow** scope: results cannot change T4, reopen the R47.4 candidate
  ladder, or alter the manifest of record.
- Jimmy approved the exact comparison design and a strict **$1.00 NTE** paid-call cap.
- Wrote `20260712n-shadow-judge-bakeoff-design.md` with the fixed candidates,
  deterministic evidence design, evaluation contract, safety/accounting requirements,
  TDD surface, Done-when ceiling, and out-of-scope list.
- Updated `PENDING-QUESTIONS.md` to record the bounded authorization while preserving the
  paid-call locks on T3/T4 and all other models/runs.
- No execution-plan checkbox changed: this is an adjunct shadow study, not T3 or T4.
- No OpenRouter key was loaded and no paid call was made.

## Exact authorized study

- Paid: `z-ai/glm-5.2` and `deepseek/deepseek-v4-pro` only.
- Offline-only comparators: persisted `x-ai/grok-4.20` and
  `google/gemini-2.5-flash` evidence.
- Battery: all six frozen probes, K=8, threshold >=5/8.
- Real-response sample: deterministic 8 units × four surfaces from the immutable MVP,
  seed 1647; 64 planned new shadow verdicts.
- Hard cap: $1.00; expected approximately $0.15–$0.30.
- Output: a new append-only shadow run, never a qualification manifest or score of record.

## Review gate

Per the design workflow, Jimmy reviews the written spec before implementation. If the spec
is approved without changes, the next Codex turn invokes the writing-plans workflow and
creates the TDD implementation plan. Paid execution remains downstream of the offline
implementation and verification.

## Preserved gates

- T3 remains closed pending its exact four-SUT roster and paid-run authorization.
- T4 remains closed pending its exact budget/paid-call authorization; this $1 cap is not
  T4 authorization.
- The current panel and R47.3 manifest remain the record.
- The candidate ladder remains closed.

## Verification

- Full offline harness suite: **520/520 passed** in 8.62 seconds. Pytest emitted only
  post-suite temporary-directory cleanup warnings; no test failed.
- `git diff --check`: clean.
- Spec placeholder scan: clean (`TBD`, `TODO`, `FIXME`, `PLACEHOLDER` absent).
- Spec self-review found no unresolved contradiction or ambiguity: exact slugs, evidence
  universe, ranking contract, budget behavior, outputs, gates, and non-effects are fixed.
- Dashboard source contains the S29 history row, exact authorization, $0-spend budget row,
  and next-session review gate. The in-app browser disallowed local `file://` navigation,
  so no visual browser claim is made.
- Dirty sibling-benchmark files were observed and left untouched; WCF-only path-scoped
  staging is required.
