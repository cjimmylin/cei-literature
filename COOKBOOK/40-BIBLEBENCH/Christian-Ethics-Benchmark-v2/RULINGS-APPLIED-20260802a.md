# RULINGS APPLIED — 2026-08-02a: v4-T Claude-tier differentiation probe AUTHORIZED (OAuth channel · $1.00 judging ceiling) · d02 re-pilot DISCHARGED

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-08-02 · **Spend ceiling authorized: $1.00 (v4-T judging only; SUT administration is subscription OAuth, $0 external; v4-A stays $0).**
**Predecessor:** `RULINGS-APPLIED-20260801a.md` — its RULING 4 (d02 hardened re-pilot)
was executed and CLOSED at $0.178 of $2.00; see report
`20260801c-d02-hardened-repilot-report.md` (commit `aa4ebd9d9`). Nothing of that
ceiling carries forward.
**Subject:** owner directive of 2026-08-02, recorded from an interactive owner
decision (scope, epochs, judge channel, and chain update each chosen explicitly):
add an ORTHOGONAL known-groups probe — do WALKWORTHY items differentiate Claude
models of known capability ordering (Haiku, Sonnet, Opus) — administered via the
Claude Code CLI's subscription OAuth, with no API keys on the SUT side.

---

## RULING 1 — v4-T tier-differentiation probe AUTHORIZED

A new probe, designated **v4-T**, orthogonal to the d02 judging thread and to the
B-phase reference runs. Scope as ratified:

1. **Items:** design-01 (goodsamaritan, 49 admin lines, model-graded) and design-05
   (ordoamoris, 32 admin lines, judge-free CSR) — the FULL public bank for both.
   Single-turn designs only; d02/d07 multi-turn ladders are excluded from v4-T.
   Holdout is never read.
2. **SUTs:** three Claude tiers via PINNED full model ids (aliases float and are
   forbidden): `claude-haiku-4-5-20251001`, `claude-sonnet-5`, `claude-opus-5`.
3. **Administration channel:** Claude Code CLI print mode under subscription OAuth
   (`claude -p --model <full-id> --output-format json`), porting the proven
   `CLIModelClient` pattern (WCF harness `wcfbench/cli_client.py`): API-key env vars
   unset in the child process, hygiene flags (no tools, no MCP, no settings
   sources, single turn), clean CLAUDE.md-free temp cwd. $0 external spend;
   modest-scale use per that client's own documented caveats.
4. **Epochs:** 2 per item × model → census 81 × 3 × 2 = **486 SUT calls**.
5. **Scoring:** d05 programmatically (existing `parsers` + `ordo_constraints`
   entry points, imported read-only, $0). d01 via the instrument's pinned
   cross-family judges — judge-A `openai/gpt-4.1-nano`, judge-B
   `meta-llama/llama-3.3-70b-instruct`, OpenRouter, temperature 0 — under a
   **$1.00 hard ceiling** (projection AND actual; calibration micro-run first;
   stop-and-report on breach). Cross-family judging is deliberate: no
   Claude-judging-Claude reads enter the record.
6. **Tooling:** new script(s) under `tools/audit/` only (not pinned by
   `INSTRUMENT.json`). No pinned component — `datasets/public/*.jsonl`,
   `tasks/*.py`, `walkworthy_inspect/*.py` — may be edited; the `WW-v2-20260731b`
   verify chain stays green.
7. **Interpretation guardrails:** all v4-T numbers are probe diagnostics, never
   WALKWORTHY numbers; they must NEVER be pooled or compared row-for-row with the
   inspect_ai/OpenRouter reference runs (different harness; the CLI overhead is
   constant across tiers, so tier CONTRASTS are the interpretable object).
   Pre-committed read-out criteria live in boot prompt `20260802b` §4.

## RULING 2 — entry-point supersession; d02 re-pilot DISCHARGED

Boot prompt `20260802b-boot-prompt-v4t-claude-tier-probe.md` supersedes
`20260801b` as the entry point for the next session. The `20260801b` §4 task (d02
hardened re-pilot) is DISCHARGED — executed 2026-08-01, evidence record
`20260801c`, run tree `logs/d02-btpilot2-20260801/`; do not re-run it. The
P-PRESSURE v4.0-scope decision remains with the owner, both pilots in hand; v4-T
neither advances nor closes it.

## Standing

Unchanged by reference: v4-A remains OPEN at $0 per `-20260801a` RULING 1; B1+B2
scale (~$180–230) REMAINS OPEN with B1 still blocked on the two v4-A code fixes;
d07 conditional-HOLD-exit and P-COMMITMENT not-advanced stand; holdout CLOSED
(never set WALKWORTHY_ALLOW_HOLDOUT); all `20260731f` §5 binding constraints in
force. Newest-ruling-wins: this file wins over `20260801b` and everything older.
Entry point for the next session: `20260802b`.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
