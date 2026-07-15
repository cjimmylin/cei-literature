# WALKWORTHY Design 02 Labeling Helper — Plan Handoff

**Date:** 2026-07-15
**Agent:** Codex
**Scope:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/`

## Outcome

Jimmy approved the written Design 02 labeling-helper specification. Codex then wrote
and self-reviewed the complete TDD implementation plan:

- `00-PORTFOLIO/20260715-design02-labeling-helper-implementation-plan.md`

Implementation has **not** started. The next entry gate is Jimmy's review of that plan
and choice of execution mode: subagent-driven task execution or inline execution.

## Planned paper-facing deliverable

The approved design remains the smallest offline interface that can produce one
complete PR-29 Design 02 label packet:

- primary page: 12 blind rows / 21 ordered response turns;
- independent-reliability page: four blind rows / seven ordered response turns;
- finalizer: distinct-labeler declaration plus only true turn-state disagreements,
  using one-based integer `member` indices;
- README: exact human completion, return, verification, and G4 conversion workflow.

The eight-task plan covers frozen-source validation, deterministic self-contained HTML,
guided turn labeling, conditional Q-R2, exact CSV downloads, strict finalizer imports,
declaration/adjudication downloads, committed-artifact drift checks, real system-Chrome
`file://` acceptance, PR-29 regressions, full-suite verification, dashboard closure, and
fast-forward integration.

## Self-review corrections

- Test CSV readers and completed-label fixtures stay in
  `harness/tests/test_design02_labeling_helper.py`; no test-only API enters production.
- Native radio inputs have exact visible labels, so browser tests exercise accessible
  user controls rather than implementation-specific selectors.
- The plan explicitly requires Jimmy's plan review before Task 1 and preserves observed
  RED → minimal GREEN checkpoints throughout.
- Browser acceptance uses installed system Chrome through Python Playwright. It requires
  no server, Node runtime, browser download, or new dependency.

## Critical-path state

The helper is justified only because it directly reduces the current human-label
friction. Current labels remain **0/439**; no G4 report, Part-B conversion, verdict,
manuscript revision, or release claim was produced in this planning session.

The next paper-conversion trigger remains:

1. implement and verify the approved helper;
2. Jimmy completes the Design 02 primary page;
3. an independent second labeler completes the isolated reliability page;
4. Jimmy finalizes declaration and disagreements;
5. Codex verifies/imports the packet and immediately runs G4 → available Part B →
   frozen status/verdict branch → manuscript/PDF conversion.

OPEN6 remains stopped with PR-30 separate. G7 remains PENDING and closed. No paid call,
credential, live model, HOLDOUT access, item/key/denominator change, frozen-rule change,
O5 verdict, scale-up, or public release was authorized or performed.

## Verification

- Existing G4/PR-29 baseline: **25/25 passed**.
- Dashboard HTML parsed successfully and contains the approved-spec, plan-review, and
  continuation markers.
- The plan contains no unresolved test-only production helper references or placeholder
  instructions; all executable Python commands use the documented absolute virtual
  environment path so they also work from an isolated worktree.
- `git diff --check`: clean before staging.

The passing test run emitted only the repository's known macOS pytest temporary-folder
cleanup warning after completion; it did not change the 25/25 result.

## Next session

Review the implementation plan and choose one execution mode:

1. **Subagent-driven:** execute one plan task at a time with task-level review; or
2. **Inline:** execute the same ordered tasks in the primary Codex task.

Both modes are bound by the same plan, stop conditions, TDD checkpoints, scope lock,
and explicit-path git rules. Do not build a general annotation platform or revive a
local URL; the deliverables open directly as standalone files.

On session open, load `00-PORTFOLIO/project-dashboard.html` (Live status + §12 first).
On session close, update the dashboard per the local `AGENTS.md` project-dashboard
protocol, write a new dated handoff, and fast-forward push explicit WALKWORTHY paths.

## Ancillary work

Only plan, dashboard, and handoff maintenance was performed. This was the required
implementation-review gate after written-spec approval; it made no benchmark or paper
claim and did not expand the critical path.
