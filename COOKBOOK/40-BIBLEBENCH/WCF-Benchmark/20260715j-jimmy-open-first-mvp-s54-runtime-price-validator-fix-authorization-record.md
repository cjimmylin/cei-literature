# WCF-Bench Open-First MVP — Session-54 Runtime Price-Validator FIX Authorization

**Date:** 2026-07-15
**Owner:** Jimmy Lin
**Scope:** exact Session-54 runtime endpoint-price validator P1 only

## Owner ruling (verbatim)

> FIX

## Controlling interpretation

This ruling selects the exact **FIX** option in
`20260715h-wcf-open-first-mvp-s54-runtime-price-gate-escalation.md`:

- Add exactly one TDD regression proving that an above-ceiling aggregate model row passes
  when at least one current parameter-compatible, data-policy-eligible endpoint is at or
  below both frozen price ceilings.
- Make the live public metadata fetch include endpoint rows for all six exact model slugs.
- Apply the already-binding eligible-endpoint rule at runtime while preserving fail-closed
  behavior when the exact slug is missing, endpoint metadata is missing, required
  capability is insufficient, or no eligible endpoint is within both frozen ceilings.
- Preserve the frozen `max_price`, `require_parameters=true`, and
  `data_collection="deny"` request controls unchanged.
- Run fresh named-only specification review and, only after it passes, fresh named-only
  quality review. Only if both pass may Codex resume the already-authorized gate-locked
  sequence.
- The strict cumulative OpenRouter NTE remains **$10.00**, including every attempt and
  retry; the frozen inner execution cap remains **$8.57**.

This ruling changes no roster, model slug, endpoint-price ceiling, prompt, parameter,
retry rule, one-run boundary, judge contract, validity label, claim, accepted manuscript,
or publication status. It authorizes no top-up, substitution, fallback, perturbation,
rerun, T4 work, ranking, release claim, or spending above the unchanged cap. Every prior
automatic stop remains controlling.
