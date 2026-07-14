# WALKWORTHY — PR-18 G7 Production-Mechanics Ruling

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Owner:** Jimmy Lin
**Recorded by:** Codex
**Status:** RATIFIED / CLOSED
**Scope:** O5 W5/G7 mechanics only; no live call or spend authorization

## Owner ruling (verbatim)

> Ratify PR-18 choices A2/B1/C3/D1/E3: round half-up within each nonempty
> easy/hard stratum for 73 PUBLIC items and 438 item×model cells per battery;
> paraphrase only protected user-authored administration fields under exact
> structural, literal-invariant, and L1–L9 fail-closed checks; reduce the two
> batteries by any-battery flip per item×model cell, with PASS at at most 43/438
> flips and affected items at at least 3/6 models; use explicit checked-in role
> manifests plus a deterministic design-wide no-reuse registry; and keep the fixed
> denominator and G7 PENDING until every original and perturbed cell is adjudicated
> through the frozen P1/Part-B path. No HOLDOUT access, item/key edits, or live calls
> are authorized by this ruling.

## Mechanical materialization

1. **A2 — selector.** For every nonempty `(design, difficulty)` stratum, select the
   first `round_half_up(0.20 × N)` runnable PUBLIC items by stable item ID. The frozen
   surface is 73 items: per-design counts `10/8/7/7/7/7/6/7/7/7`. Each battery
   therefore contains 438 item×model cells.
2. **B1 — paraphrase.** Only user-authored administration fields may change:
   `turn.text`, branch values, `cold_open`, and `terminal_ask`. System text,
   structure, metadata, keys, anchors, `facts_diff`, names, quantities, quoted text,
   polarity/modality, and comparison direction are protected. Protected placeholders
   and structural checks must pass, followed by the registered L1–L9 lint. A failure
   stops that item before any SUT call and may not shrink the denominator.
3. **C3 — reduction.** A registered item×model cell flips when either battery changes
   the adjudicated load-bearing categorical outcome. The fixed denominator is 438;
   G7 passes only at no more than 43 flips. An affected item is listed when at least
   three of its six models flip in either battery. No item edit follows automatically.
4. **D1 — roles and names.** Every selected item receives checked-in explicit role
   metadata: original token, stable role index, source-supported apparent gender or
   `unspecified`, optional title, and field occurrences. Replacements are allocated
   in sorted `(design, item_id, role_index)` order against a target-design exclusion
   set and one design-wide no-reuse registry. Missing/ambiguous roles or inventory
   exhaustion stops the design.
5. **E3 — unresolved cells.** The fixed denominator is retained. Perturbed
   disagreements follow the frozen P1/Part-B adjudication path. G7 stays `PENDING`
   until every selected original and perturbed comparison has an adjudicated
   load-bearing category. Unresolved cells are never counted as pass, fail, or an
   exclusion.

## Authority boundary

This ruling authorizes mechanical implementation, deterministic PUBLIC-only dry runs,
tests, and an exact paid-run preflight. It does **not** authorize credential access,
model calls, spend, substitutions, HOLDOUT access, item/key edits, gate-rule changes,
or a G7 verdict before the full fixed surface is adjudicated.
