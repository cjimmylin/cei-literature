# WCF-Bench Pilot 2 — Offline Implementation Plan

**Date:** 2026-07-15
**Status:** IMPLEMENTED FOR REVIEW · ZERO PAID CALLS
**Paper-facing milestone:** an executable manifest proposal and exact refreshed cap,
followed by an owner authorization decision.
**Sufficiency gate:** all five pinned endpoints pass public-metadata validation without
roster, price, reasoning, or data-policy drift.
**Session stop:** amount-specific authorization gate; no credential access or inference.

## Bounded implementation

- `pilot2_preflight.py` freezes the five-SUT identity, 230/226/4 schedule, costs, provider
  pins, reasoning controls, byte limits, and explicit no-authorization state from supplied
  public metadata.
- `pilot2_run.py` builds exact requests, validates provider canaries, preserves the
  sequential five-model first-cell gate, forms three model shards, projects final answers
  without reasoning, dynamically packs judge records, and retains missingness semantics.
- `pilot2_live.py` supplies append-only identity, manifest copying, request reservations,
  response-attributed settlement, and missing checkpoints for a future authorized run.
- `pilot2_judge.py` reuses the reviewed isolated Codex-OAuth Sol/medium process adapter and
  changes only the Pilot 2 input byte ceilings.
- `pilot2_oauth_canary.py` defines the exact synthetic 8 OPEN / 4 CONTESTED / 4 EPISODE
  canary, including a near-ceiling record; `pilot2_report.py` refuses output before complete
  empirical data and enforces roster-order, coverage, and claim boundaries.

## Verification and next action

Focused tests cover roster, providers, reasoning settings, 8,192-token reservations,
geometry, canary retry semantics, first-cell ordering, dynamic byte packing, final-answer
projection, missingness, custody, budget, neutral reporting, and fixture-only end-to-end
structure. The full offline suite must remain green before integration.

After specification and quality reviews, run one append-only zero-paid public catalog
preflight. Return the exact endpoint roster, prices, cap, balance/top-up requirement, task
counts, and runtime to Jimmy. Stop there. Credentials, OAuth canary, paid SUT requests,
judging, and supplement generation require the next written authorization.
