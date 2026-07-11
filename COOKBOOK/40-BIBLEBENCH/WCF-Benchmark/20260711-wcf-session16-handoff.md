# WCF-Bench — Session 16 Handoff (2026-07-11, Fable adjudication + Codex handover — THREAD CLOSED)

**Date:** 2026-07-11 · **Session:** 16 (Fable main loop; adjudication only — no code, no
live calls) · **Commits this session:** `acb00f2a9` (binding memo R42–R46 + Opus boot
prompt), `8150b5510` (AGENTS.md + Codex execution plan), this handoff. All pushed to
`origin/main`. · **Predecessor:** `20260710m-wcf-session-handoff.md` (session 15, §6b).
**Project root:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`

> **This closes the Claude-side execution thread.** WCF-Bench execution is handed to
> **Codex** (worktree branch `codex/wcfbench-mvp-testable` existed at close, zero commits —
> fresh). Claude models re-entering this project: your role is now **adjudication and
> review**, not building — read §4 before doing anything.

---

## 1. What session 16 did

1. **The MVP-run payoff read** — first sample-level adjudication of the 816-cell run's
   cross-SUT judge disagreements (all 309 transcript-backed cells statistically profiled;
   worst-spread cells read verbatim) → **BINDING memo
   `20260711-fable-mvp-disagreement-adjudication-memo.md` (R42–R46)**. Headlines:
   - **R42:** panel HEALTHY post-requal (settled-core floor 16/16; gemini = most central
     grader). The top-3 "worst disagreements" were harness artifacts: a **first-match
     `SCORE:` parse bug** (incl. one silent in-range corruption) + R24-fenced off-scale
     raws inflating `disagreement.json` spreads. One gpt award overruled on **fabricated
     evidence**. gemini strict-tilt recorded as G6 calibration material, NOT bias.
   - **R43:** gpt-4o-mini **DROPPED** from the panel (→ gemini-flash + grok-4.20).
   - **R44:** OPEN-award **format-bridge AUTHORIZED** (conditions incl. full K=8 re-qual +
     exactly-3-candidate re-screen, ≤$10; zero-pass → ladder CLOSED).
   - **R45:** complete build directives (parse fix, disagreement display, cost estimator,
     EPISODE runs, PROOFTEXT judge-assisted upgrade; one-manifest sequencing).
2. **Codex handover package** (Jimmy's direction: move execution to Codex, with explicit
   anti-rabbit-hole discipline after Codex over-dug in other threads):
   - `AGENTS.md` (in this directory) — Codex entry point: manual safety rules (no hooks
     fire for Codex), environment, OpenRouter gotchas, read order, rabbit-hole rules.
   - `20260711-codex-execution-plan.md` — 6 bounded tasks implementing R42–R46, each with
     Done-when (a CEILING, not a floor) + Do-NOT lists, progress checkboxes, an
     out-of-scope table, and a `PENDING-QUESTIONS.md` escalation protocol.
3. Memory notes + this handoff updated; thread closed.

## 2. State at close (the numbers a re-entrant needs)

- Bank: **230/230**, frozen, independently audited. Suite: **444 pytest green** (~4s, no
  network). MVP run: **816/816 cells, 0 errors** (`07-PILOTS/20260710-mvp-run/`) —
  DESCRIPTIVE/PRE-GATE; report + adjudicated companion (the R42–R46 memo) both stand.
- Panel of record: **gemini-flash (google) + grok-4.20 (x-ai)** per R43 (the physical
  roster-drop is Codex Task 4). Manifest of record until Task 4 replaces it:
  `07-PILOTS/20260710-settled-requal/20260710-settled-requal-manifest.json`.
- OpenRouter key: `~/.codex/secrets/openrouter.env`, ~$30 remaining 2026-07-10; internal
  cost estimator undercounts ~10× until Codex Task 3.
- SUT roster (unchanged): llama-3.1-8b-instruct, deepseek-chat, mistral-large-2512,
  claude-haiku-4.5.

## 3. Document map (who reads what)

| reader | entry point | then |
|---|---|---|
| **Codex / coding agents** | `AGENTS.md` | `20260711-codex-execution-plan.md` → R42–R46 memo → earlier docs only when a task cites them |
| **Future Claude (adjudication)** | this handoff §4 | plan checkboxes + latest `*codex-session-handoff.md` + `PENDING-QUESTIONS.md` |
| **Claude fallback builder** (only if Codex handover is abandoned — ask Jimmy first) | `20260711-opus-postadjudication-build-boot-prompt.md` | same work as the Codex plan, Claude-idiom |
| **Binding decisions (all readers)** | R-chain memos R1–R46; latest = `20260711-fable-mvp-disagreement-adjudication-memo.md` | never relitigate; new judgment questions → Jimmy |
| **Raw evidence** | `07-PILOTS/` (append-only) | per-run `transcripts.jsonl` / `disagreement.json` / reports |

## 4. If you are a future Claude model re-entering this project

1. **Check whether Codex has progressed:** the checkboxes in
   `20260711-codex-execution-plan.md` §Progress, any `YYYYMMDD-codex-session-handoff.md`,
   `PENDING-QUESTIONS.md`, and `git log --oneline -- COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`
   (+ branch `codex/wcfbench-mvp-testable`, unmerged at close). Do not redo or duplicate
   Codex work; do not "fix up" its in-flight branch.
2. **Your default role is adjudication:** answer `PENDING-QUESTIONS.md` entries, review
   completed tasks against their Done-when specs, and do sample-level judge adjudication in
   the R29/R31 mode when a run surfaces disagreements. Extend the R-chain (R47+) with a new
   dated memo — never edit old memos or re-score old run dirs.
3. **Only build if Jimmy redirects execution back to Claude** — then use the Opus boot
   prompt, honoring any checkboxes Codex already ticked.
4. Safety rules are in root `CLAUDE.md` (hook-enforced for you) and mirrored manually in
   `AGENTS.md`. Shared git index is LIVE across parallel sessions: `git log -1` before
   commit, explicit paths, never `git add -A`.

## 5. Remaining queue (nothing Claude-blocked, nothing Fable-blocked)

| item | owner |
|---|---|
| Execution plan Tasks 1–6 (parse/display/cost → format-bridge+re-qual → EPISODE → PROOFTEXT) | **Codex** |
| G6 confessional panel → gated G1–G7 run, H-DISC promotion, W304/W305 position maps, 4 LIB `[DISPUTED]` legs | **Jimmy** (recruit raters; instrument ready at `06-G6-PANEL/`) |
| Full-bank re-run under the post-Task-4 manifest (~$15) | **Jimmy decision** (optional) |
| PENDING-QUESTIONS adjudication, task review, R47+ | **future Claude** (on demand) |
| Perturbation battery P1–P6 at scale | post-MVP, needs a new directive |

## 6. Loose ends disclosed at close (deliberately NOT touched — sibling lanes)

- `codex/wcfbench-mvp-testable` worktree branch: created (by Codex setup), **0 commits**
  at close — it is Codex's active lane, left alone.
- Dirty CORINTHLOVE `07-charitroc/` files + untracked root `CEI-Lit-WS/AGENTS.md` and
  `.agents/`: other sessions'/Codex-setup's files, not this session's lane
  (lane-isolation ruling, Jimmy 2026-07-10). Not staged, not cleaned.
- Older `codex/*` branches (fruitbench ×2, sermonmount, skim-p1-bank) + their worktrees:
  other projects' lanes.

## 7. Guardrails honored

No code, no live calls, no gold minted, no item edited, no G6 activity. Report immutability
(all new dated files; `07-PILOTS/` untouched). Canary `WCFBENCH-CANARY-c1647-x9k4q` not
re-minted. Shared git index: `git log -1` before each commit, explicit paths only, sibling
dirty files untouched, fast-forward pushes. Secrets untouched. Scope-locked to
`COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`.
