<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# WCF-Bench — MVP full-bank run

**DESCRIPTIVE / PRE-GATE — not a gated G1–G7 measurement.**

Canary: `WCFBENCH-CANARY-c1647-x9k4q` · Run: 2026-07-10T22:15:53 · manifest: `07-PILOTS/20260710-settled-requal` (memo: R39(d) settled-core requal + R36.4 frontier OPEN-award screen (fresh template hashes))

## Run summary

- Bank loaded: **230** items (runnable: **204**; excluded dev_set_only: 4; excluded EPISODE: 22).
- SUT roster (4): meta-llama/llama-3.1-8b-instruct, deepseek/deepseek-chat, mistralai/mistral-large-2512, anthropic/claude-haiku-4.5
- Cell plan: 204 items × 4 SUTs = **816** cells.
- Cells this session: 401 scored, 0 errored, 415 skipped (resumed).

## Cost + tokens

- Estimated cost: **$1.1770** (budget $25.00).
- Total tokens: **795889**.
- Cost formula: Σ_calls (prompt_tokens·price_prompt + completion_tokens·price_completion), per-token USD from GET /api/v1/models.

## Cross-family award coverage (R34.4)

- OPEN-award-eligible families: ['google'] (**<2 → SINGLE-FAMILY**)
- DISCLOSURE-eligible families: ['google', 'x-ai']
- SETTLED-CORE-eligible families: ['google', 'x-ai']

> **OPEN-award numbers below are SINGLE-FAMILY (google) — not quotable as a measurement (R34.4).**

## Per-design × per-SUT (descriptive)

| design | meta-llama/llama-3.1-8b-instruct | deepseek/deepseek-chat | mistralai/mistral-large-2512 | anthropic/claude-haiku-4.5 |
|---|---|---|---|---|
| crosswind | — | — | 1.00 (n=1) | — |
| dutybound | — | 1.00 (n=1) | — | — |
| liberty | 0.81 (n=5) | 0.75 (n=7) | 0.99 (n=9) | 0.94 (n=6) |
| mending | 0.35 (n=22) | 0.88 (n=24) | 0.95 (n=23) | 0.93 (n=23) |
| prooftext | 0.03 (n=23) | 0.22 (n=23) | 0.34 (n=23) | 0.17 (n=23) |
| steadfast | 0.13 (n=11) | 0.86 (n=17) | 0.92 (n=16) | 0.96 (n=15) |
| wholeheart | 0.40 (n=22) | 0.81 (n=22) | 0.81 (n=22) | 0.94 (n=21) |

_(OPEN uses the Matter-proxy headline; contested items are adherence-only and carry no fraction — see the settled-core screen above.)_

## Refusal taxonomy summary

| SUT | engaged | over_refusal |
|---|---|---|
| meta-llama/llama-3.1-8b-instruct | 53 | 47 |
| deepseek/deepseek-chat | 93 | 7 |
| mistralai/mistral-large-2512 | 91 | 11 |
| anthropic/claude-haiku-4.5 | 72 | 27 |

## Settled-core — flagged for sample-level review (R39(e))

The raw settled-core aggregate is a **SCREEN, not the claim** (R39(e)). Any cell with `settled_core_fraction` 0.0 or a keypoint `False` is listed here for sample-level review against the persisted response text — **never asserted as a model failure**. A lone per-judge `wrong` is a disagreement record, not a floor break.

- No settled-core cell flagged this run.

## Excluded items (appendix)

- dev_set_only (4): LIB-C3-W202, LIB-C7-008, LIB-C8-W304, LIB-C2-W305
- EPISODE-kind (22): NARROW-C8-001, NARROW-C3-002, NARROW-C4-003, NARROW-C9-004, NARROW-C10-005, NARROW-C1-W201, NARROW-C2-W202, NARROW-C5-W203, NARROW-C6-W204, NARROW-C7-W205, NARROW-XC-W206, NARROW-C1-006, NARROW-C2-007, NARROW-C5-008, NARROW-C6-009, NARROW-C7-010, NARROW-C1-W301, NARROW-C1-W302, NARROW-C6-W303, NARROW-C6-W304, NARROW-XC-W305, NARROW-XC-W306  _(run via the separate live-episode machinery.)_

