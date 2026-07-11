# Codex Execution Contract — 10CBench

**Status:** ACTIVE
**Effective:** 2026-07-11
**Scope:** ZEROSUM, SKIM, PALTER, TABLETS, and SOVEREIGN

This contract controls execution order, stopping rules, and reporting cadence. The existing governing-document stack continues to control benchmark semantics, frozen artifacts, scoring, adjudication, and scientific gates. If the two appear to conflict, preserve the scientific rule and use this contract to choose the next runnable milestone.

## Prime directive

Finish ZEROSUM, SKIM, PALTER, TABLETS, and SOVEREIGN as reproducible, resumable benchmarks that can first be tested with cheap OpenRouter models and then scaled to the official roster.

Progress is measured by completed runnable benchmarks, not by additional audit machinery.

## Priority order

ZEROSUM → SKIM → PALTER → TABLETS → SOVEREIGN

Finish and commit one benchmark before beginning the next.

## Definition of engineering-ready

A benchmark is engineering-ready when it has:

1. Frozen public bank, private gold, runtime manifest, and hashes.
2. Credential-free schema, leakage, replay, and cost preflight.
3. A mechanically testable scorer.
4. A cheap-model OpenRouter smoke that completes successfully.
5. A resumable diagnostic runner with checkpoints and a hard spend cap.
6. A diagnostic result and report that explicitly state empirical blockers.
7. Exact commands for smoke, resume, analysis, and later scale-up.

Professional ratings, human baselines, and official multi-seed evidence do not block engineering readiness. They must remain clearly marked `NOT_RUN` and prevent promotion to official empirical conclusions.

## Execution rules

- Always work on the next unmet engineering-readiness criterion.
- During an external provider cooldown, parallel agents may advance credential-free work for the next benchmark on non-overlapping paths. Do not execute its paid run or commit it ahead of the current benchmark.
- Do not add defensive hardening unless a failing test demonstrates that the issue could invalidate bank identity, leak private gold, duplicate paid calls, corrupt scoring, or falsely promote diagnostic evidence.
- Put all other improvements in a deferred-hardening list.
- Allow at most one implementation review and one final review per milestone.
- Use focused tests during development; run the full suite once before commit.
- After two unsuccessful fixes to the same problem, reassess the design instead of continuing patch cycles.
- Preserve all paid checkpoints. Never restart a paid run merely for cosmetic provenance improvements when an explicit repair attestation is sufficient.
- Never expose or serialize credentials.
- Cheap diagnostics are authorized only within the recorded per-run spend cap.
- Until the user explicitly authorizes scale execution, every live OpenRouter call must use the frozen cheap diagnostic roster. Official or expensive rosters may be documented and preflighted without network calls, but must not be executed.
- A benchmark may be called complete only with fresh test output and artifact hashes.
- Do not begin unrelated research, documentation, or calibration while a safe runnable next step remains.
- A diagnostic may account for parked rows and still finish its schedule, but reports must distinguish schedule rows accounted from successful model responses.

## Readiness boundaries

- **Engineering-ready:** the seven criteria above are satisfied; diagnostic evidence remains explicitly ineligible for official conclusions.
- **Scale-ready:** the official model roster, seeds, provider policy, spend ceiling, and exact launch command are frozen and pass preflight.
- **Publication-ready:** all preregistered professional, human, multi-vendor, multi-seed, calibration, and statistical gates have actually run and passed.

Do not hold engineering readiness open for publication-only evidence. Do not label diagnostic evidence official merely because the harness is engineering-ready.

## Reporting cadence

Every work update must state:

- Current benchmark
- Last completed milestone
- Current measurable count
- Exact next action
- Genuine blocker, if any
- Deferred noncritical issues

`BLOCKED` means external authority, unavailable credentials, unavailable service, or an unresolved decision that materially changes the benchmark. Ordinary bugs and test failures are work items, not blockers.

## Sources of current truth

1. `CURRENT-STATE.md` — mutable operational state and exact next command.
2. This execution contract — sequencing, stopping rules, and readiness definitions.
3. `20260706-PARKED-opus-reentry-prompt.md` — ordered scientific governing-document stack.
