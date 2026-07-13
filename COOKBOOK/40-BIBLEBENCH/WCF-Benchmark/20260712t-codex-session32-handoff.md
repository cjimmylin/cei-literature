# WCF-Bench — Codex Session 32 Handoff

**Date:** 2026-07-12
**Owner:** Codex + Jimmy
**Scope:** Permanent dashboard close-and-show protocol
**Outcome:** Protocol installed; benchmark state unchanged

On session open: load `project-dashboard.html` (Live-status first).

On session close: update the dashboard per `AGENTS.md §The project dashboard`, then
open or reload it in the browser, verify the rendered handoff surfaces, and leave it open
for Jimmy before the final response.

## 1. Jimmy's standing direction

Every future WCF-Bench session that changes repository state must finish with an updated,
rendered dashboard. This includes sessions that change only documents, generated artifacts,
plans, progress, handoffs, rulings, spend records, or other tracked files; a code change or
benchmark milestone is not required to trigger the close protocol.

The close gate is now:

1. update the dashboard banner and every affected LIVE surface;
2. append the session-history and update-log rows;
3. prepare §Instructions for next session, including the current handoff and blockers;
4. open or reload `project-dashboard.html` in the available browser;
5. visually verify the banner, Live status, newest session row, newest update-log row, and
   next-session instructions; and
6. leave that verified dashboard open for Jimmy before sending the final response.

If browser access is genuinely unavailable, the agent must verify the HTML source and say
explicitly that visual verification was unavailable. Silent omission is not allowed.

### Session 32 browser-verification status

The in-app browser was invoked and made the required attempt, but its URL security policy
rejected the local `file://` dashboard. No alternate browser surface or policy bypass was
attempted. This session therefore used the documented exception path: source and structural
verification were completed, and the visual-verification limitation is disclosed in this
handoff, the dashboard session row, and the final user response.

## 2. Durable changes

- `AGENTS.md` now makes the close protocol mandatory for every repo-changing session and
  defines the final browser show-and-handoff gate.
- `project-dashboard.html` records session 32, points to this handoff, and includes the
  browser verification requirement in the next-session paste block and footer protocol.

## 3. Benchmark state preserved

This protocol-only session changed no benchmark code, bank item, run artifact, ruling,
execution-plan checkbox, panel, manifest, candidate ladder, gate result, or spend state.

The current substantive state remains:

- shadow run: `PARTIAL / UNRECONCILED`;
- internal attributed cost: `$0.69776393843`;
- key-wide interval delta: `$5.426614419`;
- Pareto set: empty;
- all paid calls: frozen pending Jimmy's reconciliation ruling; and
- T3/T4: separately closed and unauthorized.

## 4. Next session

Start from the dashboard's §Instructions for next session and the standing v2 boot prompt.
Read this handoff, then `20260712s-codex-session31-handoff.md` and the OPEN reconciliation
question in `PENDING-QUESTIONS.md`. Continue only offline work whose existing gate is open.
Do not make a paid call, infer a shadow winner, or change production state without a new
written Jimmy ruling.
