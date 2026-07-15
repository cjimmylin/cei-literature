# WCF-Bench Open-First MVP — Session-52 Live-Seam FIX Authorization

**Date:** 2026-07-15
**Owner:** Jimmy Lin
**Scope:** exact Session-52 response/checkpoint interruption-custody P1 only

## Owner ruling (verbatim)

> I authorize the exact Session-52 live-seam interruption-custody FIX, its one recovery regression, and named-only specification and quality reviews. If both pass, resume the already-authorized sequence under the unchanged cumulative $10 cap.

## Controlling interpretation

- Add exactly one deterministic recovery regression for a fully persisted, costed,
  successful raw response whose later checkpoint is absent.
- Make the smallest correction that recovers only that unambiguous successful response as
  completed without calling transport again.
- Duplicate, malformed, uncosted, errored, or otherwise ambiguous evidence must fail
  closed; no new retry, rerun, fallback, or protocol allowance is created.
- Run fresh named-only specification and quality reviews of this boundary. Only if both
  pass may Codex resume the previously authorized gate-locked sequence.
- The strict cumulative OpenRouter NTE remains **$10.00**, inclusive of every attempt and
  retry. All prior automatic stops and prohibitions remain unchanged.

This record authorizes no roster, prompt, price, retry-policy, judging-contract, claim,
accepted-manuscript, or publication change.
