# WCF-Bench Open-First MVP — Offline Implementation Plan

**Date:** 2026-07-14  
**Scope ceiling:** minimum offline controller + public zero-paid preflight  
**Review ceiling:** one fresh implementation agent, one fresh specification reviewer, one fresh quality reviewer, and one named-blocker fix cycle

## Done when

- Exact six-SUT roster, 230/226/4 split, 1,380/1,356/24 cell geometry, 2,088 logical judge decisions, and 264 batch tasks are tested.
- Dev-only cells are generated diagnostically but cannot be judged or aggregated.
- SUT payloads enforce temperature, output ceiling, reasoning suppression, provider price/data/parameter controls, and no model substitution.
- The Codex-OAuth adapter is isolated, schema-bound, tool-call rejecting, unique-ID checked, partially retryable, and fully dependency-injected in offline tests.
- The controller exposes three sequential SUT shards, judge concurrency one, immutable identity/resume custody, missingness, coverage, and first-cell reasoning/ignored-parameter stops.
- A public-catalog-only preflight freezes or fail-closes the exact roster, canonical slugs, current prices, capabilities, contexts, endpoint evidence, prompt ceilings, geometry, retry envelope, and proposed cap without touching authentication.
- Focused tests and the complete offline suite pass.
- A dated preflight packet, pending owner decision, handoff, and living dashboard close the session.

## Ordered work

1. Add failing tests for the frozen preflight geometry, request policy, prompt ceiling, price math, and failure conditions.
2. Add the smallest preflight module that makes those tests pass.
3. Add failing tests for Codex command isolation, JSON schema, event/tool rejection, unique IDs, and partial retries; then add the minimal injected adapter.
4. Add failing controller tests for diagnostic separation, sharding, custody, missingness, coverage, and first-cell stops; then add the minimal runner seam.
5. Run one specification review. Fix only named blockers, then re-review only those blockers.
6. Run one quality review. Apply no second general enhancement cycle.
7. Execute only the public, zero-paid preflight. Write a non-executable failure packet if any fail-closed condition triggers.
8. Verify, update `PENDING-QUESTIONS.md` and `project-dashboard.html`, append the Session 49 handoff, and path-scope commit/push.

## Explicit stops

No credential lookup, `codex exec` judge task, OpenRouter completion request, top-up, paid call, empirical run directory, supplement results, PPP-1 edit, bank edit, execution-plan checkbox, T4 work, extra model, substitution, perturbation, or rerun. A failed preflight returns to Jimmy; it is not repaired by silently changing the design.

