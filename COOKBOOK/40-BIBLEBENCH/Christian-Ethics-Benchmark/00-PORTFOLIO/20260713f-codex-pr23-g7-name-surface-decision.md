# WALKWORTHY — PR-23 G7 Name-Swap Surface Decision

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Prepared by:** Codex
**Status:** OWNER RULING REQUIRED; W5 LIVE RUN NOT AUTHORIZED
**Scope:** Residual D1 materialization only; PR-18 otherwise remains closed

## Decision needed

PR-18 D1 requires explicit roles and exact field occurrences, but it does not say
whether the name-swap battery changes:

1. every model-visible occurrence, including administration `system` text; or
2. only the four user-authored field types registered for B1 paraphrasing.

This is material. Swapping a role in a user turn while leaving the same role's system
identity unchanged can create a contradictory prompt. Conversely, extending B1's
user-only rule to name swaps without an owner ruling would silently narrow R-J13's
“rendered role” language.

The 73-item PUBLIC A2 audit also found two source forms the existing first-name
inventory cannot rotate without changing grammar or role cardinality:

- `WW-01-A01`: plural family surname `Hendersons`;
- `WW-08-B04`: compound tenant label `Larsen/Whitby`; `Ana Ferreira` is later rendered
  as `Mrs. Ferreira`, so the surname/title must remain consistent if only `Ana` rotates.

Ten selected items contain no personal given-name token at all. The code now supports
an explicit zero-role declaration so those items are never silently omitted.

## Options

### Option 1 — all model-visible given-name occurrences; protect surname forms (recommended)

- Manifest every fictional personal **given-name token** across model-visible
  administration `system`, `turn.text`, branch value, `cold_open`, and `terminal_ask`
  fields.
- Rotate every occurrence of each declared token together. Hidden metadata, keys,
  anchors, `facts_diff`, and extras remain unchanged.
- Treat `Hendersons`, `Larsen/Whitby`, `Ferreira`, initials, and other surname/family/
  compound forms as explicit protected non-role literals; do not invent a surname
  inventory. Thus `WW-01-A01` has zero rotatable roles, while `WW-08-B04` may rotate
  eligible given names such as `Ana` and must leave `Mrs. Ferreira` intact.
- Explicit zero-role items remain in the fixed 438-cell denominator; no sampled item
  is replaced and no no-op cell is excluded.

This preserves prompt consistency, uses the already-ratified given-name inventory,
and adds no new name source or item-selection rule.

### Option 2 — B1 user-authored surface only

Rotate declared given-name occurrences only in `turn.text`, branch values,
`cold_open`, and `terminal_ask`; never touch system text. Protect the same surname and
compound forms. This is narrower but can leave different names for one role across the
system/user prompt.

### Option 3 — add a surname/household inventory

Expand R-J13 with a new versioned surname/household source and rotate all model-visible
given-name and surname roles. This is the broadest perturbation and requires a new
inventory/provenance review.

## Recommended owner one-liner

> Ratify PR-23 option 1: G7 name swaps cover every exact declared personal given-name
> occurrence in model-visible administration system and user fields; hidden metadata,
> keys, anchors, facts_diff, and extras remain unchanged; plural family surnames,
> compound household labels, surnames, and initials are protected non-role literals;
> explicit zero-role items remain fixed-denominator no-op name-swap cells; do not add a
> surname inventory, replace sampled items, shrink the denominator, or make live calls.

## Current boundary

The A2 selector, B1 protected-paraphrase contract, explicit-role/no-reuse primitives,
and C3/E3 aggregation have no-call tests. The checked-in 73-item production role
manifest and any W5 call remain blocked until this surface choice is ratified and the
role audit is regenerated against it. A separate exact budget/custody order will still
be required before credential access or live calls.
