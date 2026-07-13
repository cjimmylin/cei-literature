# WCF-Bench Codex Session 38 Handoff — PPP-1 Zero-Paid Preflight

**Date:** 2026-07-13
**Executor:** Codex
**Scope:** PPP-1 credential/auth/catalog preflight only
**Spend:** `$0`; no inference call was made

## Outcome

The authorized PPP-1 preflight is complete and immutable at:

`07-PILOTS/20260713-ppp1-zero-paid-preflight/`

Final verification found that its blanket retry reserve did not match the production
runner/scorer seams. The original packet remains unchanged; this zero-network append-only
correction supersedes only its retry-reserved attempt and retry-inclusive cap fields:

`07-PILOTS/20260713-ppp1-zero-paid-preflight-retry-correction/`

The final zero-network branch-interpretation addendum is:

`07-PILOTS/20260713-ppp1-zero-paid-preflight-branch-addendum/`

A concurrent same-session worker also froze an equivalent pre-canonical retry packet at
`07-PILOTS/20260713-ppp1-zero-paid-preflight-correction/`. It differs from the controlling
`-retry-correction/` packet only in its source-path string. It is preserved as non-controlling
provenance under the no-delete/run-immutability rules and is not an additional ratification
surface.

It used exactly one OpenRouter auth GET and one models-catalog GET. It made no completion,
response, or other inference request. The exact ratified roster is live in the catalog:

| Role | Exact slug | Prompt $/token | Completion $/token |
|---|---|---:|---:|
| SUT | `meta-llama/llama-3.1-8b-instruct` | 0.00000002 | 0.00000003 |
| SUT | `deepseek/deepseek-chat` | 0.0000002002 | 0.0000008001 |
| SUT | `qwen/qwen3.7-plus` | 0.00000032 | 0.00000128 |
| sole judge | `google/gemini-2.5-flash` | 0.0000003 | 0.0000025 |

The catalog was retrieved at `2026-07-13T17:23:54Z`; the frozen relevant-row SHA-256 is
`8aaf8aed304c97244239224bedd4e0677762ea1c69fa8005c429737a49b74268`.

## Exact geometry, cost, and time

- Runnable items: 226; four `dev_set_only` items remain excluded.
- SUT calls: 678.
- Single-judge calls: 1,044.
- Total logical / initial API attempts: 1,722.
- Corrected maximum API attempts: 3,624; the original blanket 3,444 field is superseded.
- Expected no-retry forecast: `$11.5698587676`.
- Logical planning cap with 20% headroom: `$14.47`.
- Maximum-retry forecast: `$29.9010952848`.
- Strict maximum-retry NTE cap: `$37.38`.
- Baseline runtime: 265.475 minutes (about 4h25m).
- Planning band: 212.38–353.97 minutes (about 3h32m–5h54m).
- Contextual shared-key balance: `$62.97400935900009`.
- Required top-up for every PPP-1 branch: `$0`.

## Owner decision now required

PF-003's proposed `$5.00` ceiling is not executable for the exact frozen scope. Even the
logical non-executable zero-completion price floor is `$5.2479232028`; at maximum retry
geometry it is `$14.0837670544`. The frozen executable choices are:

| Judge `max_tokens` | Expected no-retry / planning cap | Maximum-retry / strict NTE | Status |
|---:|---:|---:|---|
| 2,048 | `$11.5698587676 / $14.47` | `$29.9010952848 / $37.38` | full reviewed ceiling |
| 1,024 | `$8.8972187676 / $11.13` | `$22.5282952848 / $28.17` | executable |
| 512 | `$7.5608987676 / $9.46` | `$18.8418952848 / $23.56` | executable; recommended balance |
| 256 | `$6.8927387676 / $8.62` | `$16.9986952848 / $21.25` | executable; cheapest, highest truncation risk |

The expected forecast is not an NTE guarantee: a retry storm can consume the logical cap
and stop the run early. `PENDING-QUESTIONS.md` now asks Jimmy to choose one branch and its
strict maximum-retry NTE cap, or explicitly
amend the scope/roster/judge to retain `$5.00`. No choice is self-ratified. No paid-call,
runner-change, model-substitution, or scope-change authority follows from this preflight.

## Minimal remaining blocker

The existing 204-item and 22-EPISODE runners do not expose one shared, single-Gemini,
strict-pre-call-cap path without bypassing production-panel qualification semantics.
After Jimmy selects a branch, a valid next authorization must explicitly cover:

1. the unchanged 226-item × exact three-SUT × sole-Gemini scope;
2. the selected judge completion cap and strict NTE dollar cap;
3. only the minimal offline runner seam needed to enforce that cap; and
4. one paid PPP-1 execution followed immediately by the paper packet.

The output remains mandatory:

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

## Files created or updated

- `04-HARNESS/ppp1_preflight.py`
- `04-HARNESS/tests/test_ppp1_preflight.py`
- `20260713l-codex-ppp1-zero-paid-preflight-plan.md`
- `07-PILOTS/20260713-ppp1-zero-paid-preflight/` — exactly five immutable artifacts
- `07-PILOTS/20260713-ppp1-zero-paid-preflight-retry-correction/` — exactly three
  append-only offline correction artifacts
- `07-PILOTS/20260713-ppp1-zero-paid-preflight-correction/` — equivalent pre-canonical
  provenance copy, preserved but non-controlling
- `07-PILOTS/20260713-ppp1-zero-paid-preflight-branch-addendum/` — exactly three
  zero-network branch-envelope artifacts
- `PENDING-QUESTIONS.md`
- `project-dashboard.html`
- `../ACTIVE-CRITICAL-PATHS.md` — WCF contract only
- `../project-dashboard.html` — WCF card/update only
- this handoff

The frozen bank, existing run directories, registered T4, R1–R68, production panel and
manifest, and T4 preflight packet were not edited.

## Verification

- Focused: 10 PPP-1 preflight/correction/addendum tests passed.
- Full offline harness: **700 passed in 108.98s**; pytest emitted only its pre-existing
  temporary-directory cleanup warning after the successful run.
- Controlling artifact count: exactly five source artifacts plus three canonical correction
  and three branch-addendum artifacts; the three-file pre-canonical provenance copy is
  preserved separately and is non-controlling.
- JSON/CSV readability, 1,722-call arithmetic, exact slugs/prices, catalog hash, validity
  label, canary, and secret absence were verified.
- Controller source contains no inference endpoint.
- Paid inference performed: false.
- Paid inference authorized: false.
- Spend: `$0`.

## Next session

On session open: load `project-dashboard.html` (Live-status first).

Read this handoff, `PENDING-QUESTIONS.md`, and the three controlling immutable PPP-1 packets.
Do not refresh
metadata. If Jimmy has not ruled, ask him in chat to select a branch and strict maximum-
retry NTE; recommend 512 judge tokens, expected `$7.5608987676`, strict `$23.56` NTE. He
may instead amend scope/roster/judge to retain `$5.00`; then stop. If his written ruling
also grants the exact minimal-runner and paid-run
authority, implement only that seam, run once, and immediately build the manuscript
preview packet. Full T4 remains separate and unauthorized.

On session close: update the dashboard per `AGENTS.md §The project dashboard`, then
open/reload it in the browser and leave the verified next-session view open for Jimmy.

## Dashboard close

The local dashboard source was updated with the exact logical and maximum-retry forecasts/
caps, branch choices, balance, owner gate, S38 row, and next-session instruction. Concurrent
portfolio-level files were already dirty in the shared worktree and are deliberately preserved
unstaged rather than sweeping sibling changes into this WCF commit. The established
in-app browser policy rejects local `file://` pages and prohibits retry/workaround paths;
visual verification was therefore unavailable. Source and structural verification are the
documented exception for this session.

## Session allocation

Empirical execution 0% · paper work 0% · infrastructure 65% · governance/admin 35%.
The session removed the exact PPP-1 spend uncertainty and stopped at the owner decision;
it did not start another hardening or review loop.
