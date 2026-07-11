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

## Next session = O5 (judge validation + gate adjudication)
**Gated on human labels.** Prereq: Part A CSVs in `labels/20260710-partA/*-partA-blind.csv`
filled (≥ wave 1 = 02/07/01) + a 2nd labeler on the 20/design overlap (or the disclosed
test–retest fallback). If labels aren't present, STOP and say O5 is blocked on labeling.

Then, applying the frozen rules only:
1. `harness/walkworthy/judge_validation.py` → per design × judge κ (GOODNESS-weighted /
   quadratic / unweighted per §4) vs the human gold + human–human ceiling → **G4** (§C:
   releasable iff ≥2 cross-family judges pass; else §E escalation / rubric rework).
2. Apply §C to the complete panel: G1/G2/G3/G6/G8 (already computed — see the report), **G4**
   (now), **G5** (06/09 blind matched-reference scoring — LIVE calls), **G7** (name-swap +
   non-generator paraphrase perturbation — LIVE).
3. Write the **O5 gate-adjudication report** as a NEW dated file
   (`00-PORTFOLIO/YYYYMMDD-o5-…`): verdicts, item kills/demotes (§C G8), release-per-design.
   Route judgment beyond the frozen rules (disagreement/kill/redesign disputes) to
   `PENDING-RULINGS.md` for Jimmy — do not guess.

Read alongside §C: `00-PORTFOLIO/20260710-human-label-protocol.md`,
`00-PORTFOLIO/20260710-fable-PR3-ruling.md`, `00-PORTFOLIO/PENDING-RULINGS.md` (PR-1..PR-6).

### Interim work that does NOT need labels (optional, no verdicts)
- Wire the §E tie-breaker judge (`mistralai/mistral-large-2512`) into `run_panel`: re-judge
  `needs_adjudication` cells with the 3rd family, own-family-SUT exclusion → human Part-B.
- Apply the mechanical W4 06-reference fixes in `00-PORTFOLIO/20260710-W4-06-references-REVIEW.md`
  to the gitignored DRAFT (A01/K01/E01 relabels, re-key K01, trim D01/L03/N01) — needs Jimmy
  ratification before entering `DESIGNS/06-*.md`; 06 stays PROVISIONAL until G5 regardless.
- Dry-run `judge_validation.py` against the blind-CSV format with mock labels to confirm the
  G4 pipeline is turnkey.

## Session convention
Work TDD. End every session with a NEW dated handoff (`00-PORTFOLIO/YYYYMMDD-*-handoff.md`)
summarizing what was done / what remains / file locations / known issues, then a commit +
fast-forward push of WALKWORTHY paths only (explicit pathspecs). There is no external memory —
the handoff IS the persistence.
