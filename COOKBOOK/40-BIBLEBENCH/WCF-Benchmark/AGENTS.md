# AGENTS.md — WCF-Bench (Westminster Standards benchmark)

Guide for **Codex / any coding agent** working in this directory. WCF-Bench is a family of
10 method-major benchmark designs (230 items, complete) measuring model alignment against
the Westminster Standards, scored by a qualified cross-family LLM judge panel.

> **You are not Claude Code.** The `.claude/` memory, SessionStart hooks, and auto-loaded
> `CLAUDE.md` are Claude-Code-specific and **do not apply to you**. Durable project state
> lives in the in-repo dated handoffs and binding memos in THIS directory — treat those as
> the source of truth. The safety rules below were *hook-enforced* for Claude Code;
> **you must enforce them yourself.**

## Your mission (read this before anything else)

**Get the benchmark MVP to fully testable. Nothing else.** The concrete finish line and the
ordered task list live in **`20260711-codex-execution-plan.md`** — read it immediately after
this file. That plan is the whole job. If work you are considering is not in the plan, it is
almost certainly out of scope (see "Staying out of rabbit holes" below).

## Read order (total ~15 min; do NOT read the whole directory)

1. This file.
2. `20260711-codex-execution-plan.md` — the task list you will execute.
3. `20260711-fable-mvp-disagreement-adjudication-memo.md` (R42–R46) — the binding decisions
   your tasks implement. You implement these; you never re-decide them.
4. Only when a task's spec cites one: earlier memos (R1–R41), handoffs, reports. On demand,
   never up front.

## Decisions are already made (the R-chain)

This project runs on **binding adjudication memos** (`*-memo.md`, rulings numbered R1–R46).
Every design decision, judge qualification, scoring rule, and disputed item has been ruled.
**Do not relitigate, "improve," or re-derive any ruling.** If a task seems to require a new
decision, that's an escalation (see below), not an invitation to reason it out yourself.

## Safety rules (MANUAL — no hooks here; violating these has caused real data loss)

- **Never delete.** No `rm`, `unlink`, `find -delete`, `git clean -f`. To remove something,
  `mv` it to the nearest `RECYCLE-BIN/`.
- **Report + run-dir immutability.** Everything under `07-PILOTS/` is append-only history —
  never re-score, regenerate, or edit an existing run dir or dated report. New work → NEW
  dated dir/file (`YYYYMMDD-`). Superseded ≠ overwritten.
- **Never edit bank items.** `05-BANK-YAML/` is frozen (230/230, independently audited).
  Item edits are Jimmy/G6 territory. If a task needs an example text, it must come from
  fixtures or be newly authored NON-bank material.
- **Canary:** `WCFBENCH-CANARY-c1647-x9k4q` — never mint it into new item/exemplar/prompt
  content (reproducing it in a report header for provenance is fine).
- **The examinee stays blind.** No gold keys, rubric text, anchor tokens, or contestedness
  flags may leak into SUT-facing prompts. `promptbuilder` tests guard this — keep them green.
- **Shared git index.** Multiple concurrent sessions share this one worktree. Before staging:
  `git log -1` (HEAD may have moved). Stage WCF-Benchmark paths **explicitly** (never
  `git add -A` — a pathspec trap here once swept 2,388 sibling files). Never rewrite sibling
  commits. Fast-forward pushes only.
- **Secrets are runtime-only.** Never print or commit the OpenRouter key.

## Scope

Stay entirely inside `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`. Sibling benches
(Christian-Ethics-Benchmark/WALKWORTHY, FruitBench, CORINTHLOVE, …) are separate projects —
never cross-reference, reuse, or edit them. Normative sources = the Westminster texts in
`../WCF/` only.

## Environment

- Repo root: `/Users/jimmy.lin/Documents/CEI-Literature-Vault` (git, GitHub-tracked).
- Python: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python`. On Apple
  Silicon invoke pip as `python -m pip` (bare `pip` can `permission denied`).
- Harness package: `04-HARNESS/wcfbench/`. Run everything from `04-HARNESS/`.
- Tests: `cd 04-HARNESS && <venv-python> -m pytest tests/ -q` — **444 green** as of
  2026-07-11, ~4s, zero network. Keep it that way: every code change is TDD (failing test
  first), and the suite must be green before every commit.
- **OpenRouter key:** `~/.codex/secrets/openrouter.env` (`export OPENROUTER_API_KEY=…`).
  Live runs are opt-in (`--go` flags). **Pre-flight before ANY live run:**
  `GET https://openrouter.ai/api/v1/auth/key` to check limit/usage (~$30 remained
  2026-07-10). If a top-up is needed, STOP and surface to Jimmy.
- OpenRouter gotchas (both bit this vault): (1) it reserves `max_tokens × output-price` per
  request UP FRONT — an uncapped call can 402 "requires more credits" on a healthy balance;
  keep max_tokens caps. (2) model slugs drift — resolve against `GET /api/v1/models`
  (the harness fail-loud slug validation does this).
- The internal cost estimator **undercounts ~10×** (pricing-lookup gaps; fixing it is a plan
  task). Until fixed, treat `--budget` as a rough guard and check key-side spend.

## Staying out of rabbit holes (this section exists because it happened before)

Past agent sessions have burned entire days polishing details that did not move the
benchmark toward testable. The rules:

1. **Acceptance criteria are ceilings, not floors.** Every plan task has a "Done when"
   checklist. When it's met, STOP — commit and move to the next task. Do not add polish,
   extra tests beyond the spec, refactors, or "while I'm here" improvements.
2. **The 30-minute rule.** If you've worked ~30 minutes on a sub-problem without closing it,
   stop and ask: *"does solving this actually block a Done-when item?"* If no → note it in
   `PENDING-QUESTIONS.md` and move on. If yes but you're stuck → checkpoint what you have,
   escalate, and move to the next independent task.
3. **Two-retry rule for external flakiness.** A flaky API call, a weird model response, a
   transient error: retry twice, then record it (the harness has per-cell error survival for
   exactly this) and continue. Never build tooling to investigate a one-off.
4. **No new abstractions, no refactors, no dependency changes.** The harness works
   (444 tests). Make the smallest change that satisfies the spec, in the existing style.
   Refactoring working code is explicitly out of scope.
5. **Never expand a live run beyond its spec** (items, SUTs, K, candidates, budget). Bigger
   samples are not better here — run scope is pre-registered by the memos.
6. **Decision needed → escalate, don't research.** If the plan + R42–R46 don't answer a
   question, append it to `PENDING-QUESTIONS.md` (create if absent: date, question, why it
   blocks, your one-line suggested default), pick the most conservative compliant option (or
   skip that sub-item), and continue. Do NOT go read six memos or explore the codebase to
   synthesize an answer to a judgment question — judgment questions belong to Jimmy.
7. **Prompt/wording changes are load-bearing.** Judge-prompt or template text changes
   invalidate qualification manifests (R35.4) and force expensive re-qualification. Never
   reword a prompt except where the plan explicitly says to.

## Current state (2026-07-11) — one paragraph, details in the plan

Bank 230/230 (audited). Harness complete through the full-bank **MVP run: 816/816 cells,
0 errors** (`07-PILOTS/20260710-mvp-run/`, descriptive report inside). Judge panel after
adjudication: **gemini-flash + grok-4.20** (gpt-4o-mini is ruled DROPPED — removal is a plan
task). Manifest of record (until the plan's re-qual task replaces it):
`07-PILOTS/20260710-settled-requal/20260710-settled-requal-manifest.json`. Remaining work =
the 5 tasks in the execution plan (parse/display/cost fixes → format-bridge + re-qual →
EPISODE runs → PROOFTEXT upgrade). Human-rater work (G6) and the gated G1–G7 measurement
are **Jimmy-gated — not agent work, do not start them.**

## Session convention

Work TDD. End every session with: (1) suite green, (2) a NEW dated handoff
(`YYYYMMDD-codex-session-handoff.md`: what was done / what remains / file locations / known
issues / any PENDING-QUESTIONS entries), (3) commit + fast-forward push of WCF-Benchmark
paths only (explicit pathspecs). There is no external memory — the handoff IS the
persistence. Update the checkbox state in `20260711-codex-execution-plan.md` §Progress as
tasks complete (that file's checkboxes are the only part of it you may edit).
