<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# WCF-Bench — Codex STANDING Boot Prompt v2 (paste this to start every Codex session)

**SUPERSEDES `20260712-codex-standing-boot-prompt.md` (2026-07-12, S25).** Fable has
EXITED (R68) and the one amended Fable writing session (S24, paper pre-draft) is closed:
**you (Codex) are now the sole executor of ALL subsequent WCF-Bench activities — build,
run, analysis, AND the paper lane.** All judgment (new scoring semantics, gold
interpretation, gate adjudication, R-chain extension) is escalated to Jimmy, never
improvised. No further Fable sessions are planned or required.

Continue WCF-Bench, scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/` in
`/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS`. Work on **main** (the old
`codex/wcfbench-mvp-testable` branch is merged — do not reuse it).

## Session open (state-adaptive — this prompt never goes stale)

1. Open `project-dashboard.html` — Live-status first, then §Instructions for next
   session (if it names a MORE specific current prompt, follow that one).
2. Read `AGENTS.md` (rules + escalation protocol) and
   `20260712-codex-execution-plan-v2.md` (§Progress + the 2026-07-12 AMENDMENT section).
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

The binding R-chain now spans **R1–R68**: the gated-run pre-registration
`20260712c-fable-gated-run-prereg-memo.md` (R58–R68) is BINDING and satisfies T4's
"pre-registration memo" gate (conditional R58.3: valid iff the R57 checklist passes
unmodified). Execute it EXACTLY as written — **any silent deviation voids the gate**;
a forced deviation = logged Jimmy ruling BEFORE proceeding. T4's remaining gates are
Jimmy's: R57 ratification of T1/T2, budget/paid-call authorization ($300 NTE, R59.5),
and G6 labels — which gate RELEASE, not execution (R67.2).

If you hit a decision the R-chain (R1–R68) does not settle: STOP that thread, record it
in `PENDING-QUESTIONS.md` (question, why it blocks, evidence, suggested default), and —
when the evidence supports it — write a provisional adjudication packet with **reserved,
never assigned** R-numbers for Jimmy to ratify. Continue other open work.

## Paper lane (NEW in v2 — tasks P1–P4, detail in the execution plan's AMENDMENT)

The paper pre-draft is DONE (S24, Fable lane): `08-PAPER/` holds the master outline +
10 Fable-reviewed sections. Old task P is SUPERSEDED. Your paper tasks:

- **P1 (interleavable, no gate):** resolve the 3 `[VERIFY-CITATION]` tags in
  `08-PAPER/03-related-work.md`. Attempt with available tooling; if you have no web
  access, escalate via `PENDING-QUESTIONS.md` — never delete or invent a citation.
- **P2 (optional, low priority):** prose trim only; never touch verified material in
  §05/§06/§07.
- **P3 (gates: T4 gate report exists + Jimmy's R67.4 PASS/FAIL adjudication recorded):**
  mechanical results fill — FIRST write the explicit key-mapping table (T4 report keys ↔
  the `{{PREREG:*.<field>}}` registry in `08-PAPER/07-results-scaffold.md`, incl. derived
  `G4.min_kappa`), then substitute, then DELETE losing `[[IF ...]]` branches in §08
  (never rewrite them). Release-labeled league content stays draft until labels land
  (R67.2).
- **P4 (gate: P3 done):** adversarial self-review of the assembled paper against
  `08-PAPER/00-MASTER-outline.md` §2 hard constraints + the gate report, delivered as a
  provisional packet (reserved numbers) → Jimmy adjudicates. Paper release folds into
  T6's ratified-gate condition.

**Paper constraints (binding, from the outline):** editorial decisions E1–E8 are FROZEN
(`08-PAPER/00-MASTER-outline.md` §1 — arXiv-only; twin claims; steerability framing;
bank-public/holdout-withheld; `[AUTHORS]` placeholder; NO sibling-bench mentions; no
cap; file-per-section) — reopen only via Jimmy. No invented numbers; MVP figures only
in §05 and only DESCRIPTIVE/PRE-GATE-labeled; validity labels stay in every table;
canary comment stays in every `08-PAPER/` file.

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
`WCFBENCH-CANARY-c1647-x9k4q` never re-minted or embedded in new model-facing prompts ·
secrets never committed · sibling benches read-only precedent at most.

## Standing context (one paragraph)

R47–R53 ruled the Task-4 "zero OPEN eligibility" a parser artifact (willingness veto
tripped by judges quoting the fixture's "I won't…" line; counterfactual = both
incumbents 8/8 perfect) and directed the T1 work order; R54–R56 approved the EPISODE
registry with exact field corrections; R57 pre-registered the acceptance checklist that
ratifies T1/T2 (**Jimmy checks it — R58.1**). After T1+T2, the project is one
ratification away from **MVP testable** (R53 definition) with zero further live spend.
The gated G1–G7 run is fully pre-registered (R58–R68: 10-SUT roster formula, seed 1647,
$300 NTE + truncation ladder, all 7 gate computations frozen) and waits only on Jimmy's
ratification, budget, and (for release) G6 labels. The paper is pre-drafted in
`08-PAPER/` awaiting P1 citations now and P3/P4 after T4. You compute; Jimmy
adjudicates (R67.4). Full map: `20260712-wcf-codex-handover-plan.md` +
`20260712f-wcf-session24-handoff.md` (paper) + `20260712h-wcf-session25-handoff.md`
(this consolidation).
