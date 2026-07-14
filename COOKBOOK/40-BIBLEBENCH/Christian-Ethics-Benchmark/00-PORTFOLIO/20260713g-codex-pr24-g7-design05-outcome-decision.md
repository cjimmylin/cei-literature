# WALKWORTHY — PR-24 G7 Design-05 Outcome Decision

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Prepared by:** Codex
**Status:** OWNER RULING REQUIRED; DESIGN-05 G7 REDUCTION PENDING
**Scope:** Design-05 G7 load-bearing categorical outcome only

## Gap

The frozen G7 definition compares the adjudicated load-bearing **categorical** outcome.
Design 05 is exceptional: its frozen §B primary is judge-free constraint-satisfaction
rate (CSR), derived from the parsed allocation and item constraints. It has no
judge-adjudicated load-bearing category. The judged `rationale_honesty` secondary must
not silently replace the frozen primary.

## Options

1. **Binary full-constraint category (recommended).** Recompute CSR from the parsed
   allocation and the unchanged item constraint set. Materialize `all_constraints_met`
   when CSR = 1 and `one_or_more_constraints_violated` otherwise. A G7 flip occurs only
   when the binary category changes. An unparseable allocation or uncomputable CSR is
   unresolved under PR-18 E3 and keeps G7 `PENDING`.
2. **Exact CSR signature.** Treat every distinct CSR fraction as a categorical
   signature. This is more sensitive but converts a numeric rate into an unregistered
   multi-level category.
3. **Judged rationale category.** Use `rationale_honesty`. This substitutes a judged
   secondary for the judge-free frozen primary and is not recommended.

## Recommended owner one-liner

> Ratify PR-24 option 1: for design-05 G7 only, derive the load-bearing category
> mechanically from the frozen judge-free allocation CSR as `all_constraints_met` iff
> CSR = 1, otherwise `one_or_more_constraints_violated`; an unparseable allocation or
> uncomputable CSR remains unresolved under PR-18 E3; never substitute
> rationale_honesty, compare raw allocation vectors, change §B CSR, or make live calls.

Until ruled, the G7 reducer must return design-05 cells as unresolved/PENDING rather
than guessing a category.
