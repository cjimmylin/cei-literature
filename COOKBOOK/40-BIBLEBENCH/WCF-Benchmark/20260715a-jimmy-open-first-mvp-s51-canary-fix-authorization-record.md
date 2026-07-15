# WCF-Bench Open-First MVP — Session-51 Canary FIX Authorization

**Date:** 2026-07-15
**Owner:** Jimmy Lin
**Scope:** exact Session-51 canary retry-boundary P1 only

## Owner ruling (verbatim)

> I authorize the exact Session-51 canary retry-boundary FIX, its one regression, and named-only specification and quality reviews. If both pass, resume the already-authorized sequence under the unchanged cumulative $10 cap.

## Controlling interpretation

- Add exactly one regression for the reproduced retry-boundary failure.
- Make the smallest correction that permits the four-record OPEN fallback only after a true process-level mechanical failure of the initial eight-record task.
- Missing or malformed records that have already consumed the adapter's initial attempt plus two retries fail the canary; they do not receive a second fallback allowance.
- Run fresh named-only specification and quality reviews of this boundary. Only if both pass may Codex resume the previously authorized gate-locked sequence.
- The strict cumulative OpenRouter NTE remains **$10.00**, inclusive of every attempt and retry. All prior automatic stops and prohibitions remain unchanged.

This record authorizes no roster, protocol, claim, manuscript, or publication change.
