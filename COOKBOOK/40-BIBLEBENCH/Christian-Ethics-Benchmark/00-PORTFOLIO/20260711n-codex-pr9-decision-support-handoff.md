<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — Codex handoff: PR-9 decision surface quantified

**Date:** 2026-07-11. **Executor:** Codex. **Scope:** WALKWORTHY only.
**State:** O5 remains correctly stopped before W1. This session completed the offline
decision support that was possible without making Fable/Jimmy's PR-9 rulings.

## 1. What this session did

The session rechecked the actual branch, newest handoff chain, dashboard, and PR-9.
No newer Claude/Jimmy ruling had landed. Rather than starting W2–W5 out of order, Codex
mechanically quantified the two live spend/human-work surfaces and replaced the stale
pre-Grok Fable boot instructions.

New immutable evidence: `20260711l-codex-pr9-decision-evidence.md`.

- Reproduced: 2,064 panel records; 609 current-selector records; 1,767 selected
  unresolved cells; 3,172 full-surface unresolved cells; 1,405 outside-selector cells;
  20 non-tie-breakable pending records.
- Current-selector Mistral own-family exposure: **104 records / 295 cells**.
- Full-surface Mistral exposure: **225 records / 580 cells**.
- Increment outside the current selector: **121 records / 285 cells**.
- Exact historical six-SUT 02/07 cost: **$26.681701** (378 records, 10,037 calls),
  replacing the dashboard's unsupported ~$10–15 estimate as the historical baseline.

The evidence also records a later mechanical dependency: protocol Part B is cell-level,
while the current exporter emits record-level rows. Codex did not redesign it before
FR-16 fixes the surface and routing.

## 2. Updated ruling-session entry

`20260711m-fable-pr9-post-grok-boot-prompt.md` supersedes the operational state in the
immutable `20260711i` prompt. It tells the ruling session not to repeat Grok and asks for:

1. an FR-16-style selector/non-tie-breakable ruling;
2. Jimmy's 02/07 transcript/re-execution one-liner using the $26.68 baseline;
3. Jimmy's Mistral Part-B surface or logged §E replacement-model ruling;
4. explicit C-4/C-5 dispositions;
5. new zero-judgment Codex execution orders.

The living dashboard's §12 now contains the post-Grok prompt. PR-9 was appended with the
new quantities. No frozen memo, prior dated report/handoff, label file, design, O4 run,
or HOLDOUT artifact changed.

## 3. Verification

- Independent line-oriented `jq | awk` and `jq --slurp` aggregations matched per design.
- Machine assertions matched exactly:
  `2064 / 609 / 1767 / 3172 / 20 / 104 / 295 / 225 / 580`.
- Record-cost sum for the exact 02/07 surface: `$26.681700909999986`; the all-record
  cost sum reconciles to the panel summary's `$48.745`.
- Dashboard remains self-contained: no script or external URL source.
- `git diff --check`: clean.
- Full suite: **276/276 passed**.

No OpenRouter call occurred; spend = $0. HOLDOUT and sibling benchmarks were not loaded.

## 4. Files added/updated

- `00-PORTFOLIO/20260711l-codex-pr9-decision-evidence.md` (NEW)
- `00-PORTFOLIO/20260711m-fable-pr9-post-grok-boot-prompt.md` (NEW)
- `00-PORTFOLIO/PENDING-RULINGS.md` (PR-9 evidence append)
- `00-PORTFOLIO/project-dashboard.html` (living update and §12 replacement)
- this NEW dated handoff

## 5. Exact next action

Run the Fable session in `20260711m-fable-pr9-post-grok-boot-prompt.md` with Jimmy
present. Codex must not resume W1 until that session logs all three PR-9 dispositions
and issues new dated execution orders. After clearance: baseline → new immutable 02/07
run → full-turn contract validation → TDD cell-aware Part-B/tie-breaker → W1. Never skip
to W2.
