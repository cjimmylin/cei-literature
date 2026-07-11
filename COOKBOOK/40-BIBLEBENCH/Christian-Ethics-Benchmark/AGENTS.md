# AGENTS.md — WALKWORTHY (Christian-Ethics-Benchmark)

Guide for **Codex / any coding agent** working in this directory. WALKWORTHY is a family of
10 method-major benchmarks measuring *enacted* Christian ethics against a fixed corpus.

> **You are not Claude Code.** The `.claude/` memory, SessionStart hooks, and the auto-loaded
> `CLAUDE.md` are Claude-Code-specific and **do not apply to you**. The durable project state
> lives in the in-repo `00-PORTFOLIO/*.md` handoffs — treat those as the source of truth. The
> safety rules below were *hook-enforced* for Claude Code; **you must enforce them yourself.**

## Scope
Stay entirely inside `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/`. Do not
pull in or edit sibling benches (WCF-Bench, FruitBench, CORINTHLOVE, …). Differentiate this
work only against *published literature*, never sibling benches.

## Safety rules (MANUAL — no hooks here; violating these has caused real data loss)
- **Never delete.** No `rm`, `unlink`, `find -delete`, `git clean -f`. To remove something,
  `mv` it to the nearest `RECYCLE-BIN/`.
- **Report immutability.** Never overwrite or regenerate an existing report (e.g.
  `00-PORTFOLIO/20260711b-o4-panel-report.md`, anything under `STATISTICS/`). Always write a
  **new** file with a `YYYYMMDD-` date prefix. Old reports are historical snapshots.
- **Frozen gate rules.** The §B primary-metric formulas, §C gate computations/decision rules,
  and §E judge plan (in `00-PORTFOLIO/20260710-fable-gate-prereg-pilot-adjudication.md`) are
  **pre-registered and binding**. Changing any of them after data exists requires a logged
  Jimmy ruling in `00-PORTFOLIO/PENDING-RULINGS.md` — apply them, don't re-derive them.
- **HOLDOUT is never loaded** in a public run. `harness/walkworthy/loader.py` hard-refuses any
  `HOLDOUT/` path (`HoldoutAccessError`) — keep it that way; HOLDOUT is gitignored, contamination/
  perturbation use only.
- **YAML edits** (if ever needed): edit in place with `re.subn`; never `parse_frontmatter →
  rebuild` (it destroys list-valued fields).
- **Shared git index.** ≥3 concurrent sessions share this one worktree. Before staging:
  `git log -1`; stage WALKWORTHY paths **explicitly** (never `git add -A`); never rewrite
  sibling commits; **fast-forward pushes only**. `runs/*/scored_items.jsonl` and `*-DRAFT.md`
  are gitignored.
- **No verdicts without the gate.** Descriptive readings ≠ gate verdicts. Item kills, tier
  demotions, and release claims are O5 outputs and require the frozen §C rules + validated
  judges (G4) — never assert them from the descriptive report alone.

## Environment
- Repo root: `/Users/jimmy.lin/Documents/CEI-Literature-Vault` (git, GitHub-tracked).
- Python: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python`. On Apple Silicon
  invoke pip as `python -m pip` (bare `pip` can `permission denied`). The `walkworthy` package
  is under `harness/` — run Python from `harness/`.
- Tests: `cd harness && …/.venv/bin/python -m pytest tests/ -q` (currently 261 green, TDD).
- **OpenRouter key:** `~/.codex/secrets/openrouter.env` (your own config dir). **Never print or
  commit it.** Live judge/SUT calls need network access enabled.
- PDF generation, if needed: `fpdf2` or Typst — **not** LaTeX/Pango.

## OpenRouter gotcha (bit this project twice — read before any live run)
OpenRouter reserves `max_tokens × output-price` against the account balance **per request**,
up front. A missing cap reserves the model's full default (65536), so calls 402 **"requires
more credits"** whenever the balance dips below that reservation — even with cents of real
cost. `harness/walkworthy/openrouter_backend.py` now caps at `DEFAULT_MAX_TOKENS = 32768`
(measurement-neutral: above every observed response). Keep the cap; if you see a 402, check the
message's "can only afford N tokens" (× output price ≈ real balance) before assuming depletion.

## Current state (2026-07-11)
The full **6-model × 10-design O4 panel is COMPLETE**: `runs/20260711-o4-panel/` = 2064/2064,
0 schema errors, $48.75 (scored_items.jsonl is gitignored; `panel_summary.json` committed).
- Descriptive report (readings only, verdicts=O5): `00-PORTFOLIO/20260711b-o4-panel-report.md`
  (supersedes the immutable 94% `20260711-o4-panel-report.md`).
- Part A label samples drawn for **all 10 designs** (439 blind units): `labels/20260710-partA/`
  (+ `00-WAVE-PLAN-README.md`; wave 1 = {02, 07, 01}).
- Capability battery for G3: `00-PORTFOLIO/20260711-capability-battery-scores.json` (+ SOURCES).

**Re-entry doc (read first):** `00-PORTFOLIO/20260711-O4run-session-handoff.md`.

## Next session = O5 — EXECUTE THE FABLE TRANSITION PACKAGE (2026-07-11)

**All O5 judgment is pre-made.** A Fable session froze the last judgment layer on
2026-07-11; O5 is now mechanical. Your execution plan, in read order:

1. `00-PORTFOLIO/20260711e-fable-codex-transition-package.md` — **the plan**: phases,
   exact commands, build specs (tie-breaker, §E Δ(J) test, G5 driver, G7 batteries),
   guardrails, boot prompt.
2. `00-PORTFOLIO/20260711d-fable-o5-decision-framework.md` — **the decisions**: rulings
   FR-1…FR-15, the G4 branch table, the release formula + status vocabulary, firm
   PR-1..PR-6 dispositions, STOP-AND-ASK-JIMMY triggers.
3. `00-PORTFOLIO/20260711c-fable-o4-validity-review.md` — which panel readings are real
   vs artifact (V-1…V-14). Do not re-litigate; do not quote artifact readings as signals.

Load-bearing decisions you inherit (details in the docs above):
- **Phase 1 is label-free and comes first**: tie-breaker adjudication of the 609
  `pending_adjudication` cells (turn/seat-level, FR-2; probe grok-4 first), the §E judge
  Δ(J) home-advantage permutation test (never yet run), post-adjudication recompute
  (NEW dated file), G5 driver, G7 batteries. Labels only gate Phase 2 (G4) onward.
- **No S/H-derived verdict** for a design until unresolved exclusions ≤ 10% of §B S-units
  (FR-1) — the current 02/04/07/09 readings are artifacts of effective-n collapse.
- **05 verdict is already made** (FR-5): G1+G2 FAIL on the judge-free primary is real →
  difficulty-ladder rework, out of this cycle's release set.
- **G6 N/A ≠ PASS** (FR-4); G3 FAIL ⇒ charter §6.2 "capability-washed — redesign",
  excluded from release (FR-3).
- **Always pass judge/classifier/tie-breaker models explicitly** — `panel.py` and
  `render_o4_report.py` defaults do NOT match the frozen §E pair (FR-12).
- If labels are absent when Phase 2 would start, stop there and report
  "O5 blocked on labeling" — never proceed to verdicts.

Read alongside: `00-PORTFOLIO/20260710-human-label-protocol.md`,
`00-PORTFOLIO/20260710-fable-PR3-ruling.md`, `00-PORTFOLIO/PENDING-RULINGS.md`
(PR-1..PR-8; operate under the framework §5 dispositions, marked "pending ratification").

### Other interim work (unchanged, optional)
- Apply the mechanical W4 06-reference fixes in `00-PORTFOLIO/20260710-W4-06-references-REVIEW.md`
  to the gitignored DRAFT (A01/K01/E01 relabels, re-key K01, trim D01/L03/N01) — needs Jimmy
  ratification before entering `DESIGNS/06-*.md`; 06 stays PROVISIONAL until G5 regardless.

## Session convention
Work TDD. End every session with a NEW dated handoff (`00-PORTFOLIO/YYYYMMDD-*-handoff.md`)
summarizing what was done / what remains / file locations / known issues, then a commit +
fast-forward push of WALKWORTHY paths only (explicit pathspecs). There is no external memory —
the handoff IS the persistence.
