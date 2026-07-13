# AGENTS.md — BibleBench Portfolio

**Scope:** Every current and future benchmark under `COOKBOOK/40-BIBLEBENCH/`.

## Binding paper-first workflow

Before work, read `PAPER-FIRST-WORKFLOW.md`, `project-dashboard.html`, and `ACTIVE-CRITICAL-PATHS.md`, followed by the benchmark's current local state.

At session opening, state the next paper-facing milestone, sufficiency gate, open P0/P1 blocker, engineering timebox, and expected closing artifact.

P2/P3 findings do not block manuscript, pilot, analysis, or PDF work unless Jimmy approves an exception recorded in `PAPER-FIRST-DECISIONS.md` and the dashboard.

At session close, report a paper-facing artifact, a removed or narrowed P0/P1 blocker, or an explicit escalation. Test counts and implementation volume do not substitute for paper-facing progress.

No paid call, credential access, frozen-surface edit, or historical handoff rewrite is authorized by this file.

## Precedence

Safety rules, evidentiary-integrity requirements, frozen surfaces, spending boundaries, credential boundaries, and explicit owner rulings remain controlling. Benchmark-specific instructions may strengthen these rules but may not weaken the portfolio paper-first rule.

If a local instruction appears to require P2/P3 hardening before paper work, stop and seek an owner ruling instead of silently expanding the critical path.

## Required working surfaces

- `PAPER-FIRST-WORKFLOW.md` — binding policy.
- `ACTIVE-CRITICAL-PATHS.md` — living benchmark contracts and next deliverables.
- `project-dashboard.html` — visible portfolio progress and drift state.
- `PAPER-FIRST-DECISIONS.md` — append-only owner rulings and exceptions.
- `templates/` — contract and session templates.

## Git and concurrent work

- Preserve unrelated and pre-existing changes.
- Use path-scoped staging; never use `git add -A`.
- Run `git log -1` immediately before every commit.
- Do not stage another task's dashboard, run, evidence, checkpoint, or agent-instruction changes.
- If a required hunk cannot be isolated, leave it unstaged and escalate.

## New benchmark rule

Before engineering begins, add the benchmark to `ACTIVE-CRITICAL-PATHS.md` with a concrete paper claim, deliverable, sufficiency gate, timebox, stop condition, and owner-exception state. A blank template is not an active contract.
