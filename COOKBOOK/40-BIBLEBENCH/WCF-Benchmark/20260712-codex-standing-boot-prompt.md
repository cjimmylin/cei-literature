# WCF-Bench — Codex STANDING Boot Prompt (paste this to start every Codex session)

Continue WCF-Bench, scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/` in
`/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS`. You are the project's
**standing executor**: all build/run/analysis work is yours; all judgment (new scoring
semantics, gold interpretation, gate adjudication, R-chain extension) is escalated,
never improvised. Work on **main** (the old `codex/wcfbench-mvp-testable` branch is
merged — do not reuse it).

## Session open (state-adaptive — this prompt never goes stale)

1. Open `project-dashboard.html` — Live-status first, then §Instructions for next
   session (if it names a MORE specific current prompt, follow that one).
2. Read `AGENTS.md` (rules + escalation protocol) and
   `20260712-codex-execution-plan-v2.md` (§Progress).
3. Check `PENDING-QUESTIONS.md` for new Jimmy rulings since last session; apply any
   without reinterpretation.
4. Baseline: run the offline suite from `04-HARNESS/`
   (`/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/ -q`).

## Work

Execute the execution plan **top-down from the first unchecked task whose gate is
open** (gates are listed per task; a closed gate = skip, never force). Currently that
means: **T1** (the R47–R53 offline work order, detail in
`20260712-codex-work-order-boot-prompt.md`) then **T2** (EPISODE registry application
per R54/R56). Both are fully offline. **Make no paid OpenRouter call unless the task's
gate explicitly says Jimmy authorized that specific run.**

If you hit a decision the R-chain (R1–R57) does not settle: STOP that thread, record it
in `PENDING-QUESTIONS.md` (question, why it blocks, evidence, suggested default), and —
when the evidence supports it — write a provisional adjudication packet with **reserved,
never assigned** R-numbers for Jimmy to ratify. Continue other open work.

## Session close (mandatory)

1. Update `project-dashboard.html` per `AGENTS.md §The project dashboard` (Live-status,
   progress, checkboxes mirrored with the execution plan, S-row, update-log line;
   rewrite §Instructions if the next session's entry point changed).
2. Write a new dated session handoff (`YYYYMMDD-codex-session-handoff.md` convention).
3. Verify offline suite green; `git log -1` first, then commit EXPLICIT WCF-Benchmark
   paths only (never `git add -A`); push fast-forward.

## Hard rules (violations have caused real data loss — no exceptions)

Never delete files (`mv` to `RECYCLE-BIN/` if ever needed) · immutable dated run
dirs/reports/memos are never edited (new dated files; dashboard = sole exception) ·
frozen bank `05-BANK-YAML/` untouched · no gold minted, no item edited · candidate
ladder CLOSED (no judge screening) · no G6 activity · canary
`WCFBENCH-CANARY-c1647-x9k4q` never re-minted or embedded in new prompts · secrets never
committed · sibling benches read-only precedent at most.

## Standing context (one paragraph)

R47–R53 ruled the Task-4 "zero OPEN eligibility" a parser artifact (willingness veto
tripped by judges quoting the fixture's "I won't…" line; counterfactual = both
incumbents 8/8 perfect) and directed the T1 work order; R54–R56 approved the EPISODE
registry with exact field corrections; R57 pre-registered the acceptance checklist that
ratifies T1/T2 (Jimmy or the final Fable session F2 checks it — not you). After T1+T2,
the project is one ratification away from **MVP testable** (R53 definition) with zero
further live spend. The gated G1–G7 run waits on the F2 pre-registration memo, G6 human
labels (Jimmy recruiting), and budget. Full map: `20260712-wcf-codex-handover-plan.md`.
