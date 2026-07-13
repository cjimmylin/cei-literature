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

## Next session = O5 — EXECUTE (all judgment closed 2026-07-12; Codex owns everything)

**All O5 judgment is pre-made and ALL rulings are now Jimmy-ratified.** The 2026-07-12
Fable ruling session (Jimmy present) closed PR-9 (FR-16 full-surface ruling + Jimmy's
re-execution and Mistral one-liners), issued FR-17 residuals, and ratified the ENTIRE
backlog (PR-1/2/3/4/6/8, FR-1..FR-16, W4 06-fixes). **Single entry point (paste-ready
boot prompt + execution sequence + re-entry protocol):**
`00-PORTFOLIO/20260712-fable-codex-full-handoff.md` — it operationally supersedes
`20260711g` (which remains the archived multi-session protocol). Build specs live in the
docs below, in read order:

1. `00-PORTFOLIO/20260711e-fable-codex-transition-package.md` — **the plan**: phases,
   exact commands, build specs (tie-breaker, §E Δ(J) test, G5 driver, G7 batteries),
   guardrails, boot prompt.
2. `00-PORTFOLIO/20260711d-fable-o5-decision-framework.md` — **the decisions**: rulings
   FR-1…FR-15, the G4 branch table, the release formula + status vocabulary, firm
   PR-1..PR-6 dispositions, STOP-AND-ASK-JIMMY triggers.
3. `00-PORTFOLIO/20260711c-fable-o4-validity-review.md` — which panel readings are real
   vs artifact (V-1…V-14). Do not re-litigate; do not quote artifact readings as signals.

Load-bearing decisions you inherit (details in the docs above; 2026-07-12 updates BIND):
- **W1 surface = the FULL §B unresolved surface** (FR-16, ratified): all 3,172
  `needs_adjudication` cells / 1,297 records at FR-2 turn/seat granularity — NOT the
  retired 609-record refusal-tag selector. Part-B export is CELL-level (exporter must be
  rebuilt TDD cell-aware first). 20 non-tie-breakable pendings: 11×05 → one bounded
  re-parse pass then Part-B; 9×09 arbiter-first → Part-B directly.
- **Tie-breaker = `mistralai/mistral-large-2512`** (grok-4 probe FAILED 0/10 HTTP 404 —
  NEVER re-probe; Jimmy accepted the own-family Part-B burden ≤225 records/580 cells,
  triaged per FR-17(a) wave order). Byte-identical rubric text per FR-17(c).
- **02/07 first need the NEW immutable six-SUT re-execution** (Jimmy-authorized,
  ~$26.68 baseline) — verify complete turn transcripts against the data-contract test
  before treating the run as done. The historical O4 run is untouched.
- **Phase 1 is label-free**: re-execution → cell-aware exporter + tie-breaker TDD → W1 →
  §E judge Δ(J) permutation test → post-adjudication recompute (NEW dated file) → G5
  driver (refs Fable-reviewed, pending Jimmy promotion) → G7 batteries (L7 list
  authorized). Labels only gate Phase 2 (G4) onward.
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
(PR-1..PR-6/PR-8/PR-9 all RATIFIED/CLOSED 2026-07-12 — release language no longer needs
"pending ratification" markers; PR-7 stays open as a next-cycle amendment), and
`00-PORTFOLIO/20260712-fable-ruling-session-log.md` (R-J1..R-J12 + FR-17).

### Other interim work (unchanged, optional)
- Apply the mechanical W4 06-reference fixes in `00-PORTFOLIO/20260710-W4-06-references-REVIEW.md`
  to the gitignored DRAFT (A01/K01/E01 relabels, re-key K01, trim D01/L03/N01) — needs Jimmy
  ratification before entering `DESIGNS/06-*.md`; 06 stays PROVISIONAL until G5 regardless.

## Paper-critical-path execution policy (BINDING)

The default objective is to convert validated benchmark evidence into paper-ready
statistics and claims as quickly as validity permits. The active priority is always:

1. Complete the current critical-path stage.
2. Run the next mechanically required stage.
3. When a paper-entry artifact becomes available, update the PAPER scaffold in the
   same session unless a frozen gate blocks interpretation.
4. Perform ancillary engineering only when it directly blocks steps 1–3.

W1 → W2 Δ(J) → W3 and the first licensed PAPER results fill are complete. The
immediate paper-facing priority is now the separately registered **MVP-PILOT** in
`00-PORTFOLIO/20260713-walkworthy-mvp-paper-strategy-amendment.md`: a deterministic
60-item PUBLIC preview using 3 inexpensive SUTs and 2 inexpensive cross-family judges,
under a $5.00 NTE cap. Its outputs are descriptive only and never substitute for O5.

The next authorized step is documentation-only: name exact model slugs, verify current
prices/availability, calculate worst-case spend, and obtain Jimmy's separate paid-run
authorization. Until then, no credential access or live call is authorized. O5 remains
the release-grade lane; human labels still gate G4/verdicts, and all frozen O5 rules
remain binding.

### Anti-tangent rules

- No refactoring, new infrastructure, concurrency experiments, broad audits, or paper
  polish unless required to unblock the next critical-path command.
- Log a newly discovered non-blocking issue in `PENDING-RULINGS.md`, park it, and
  continue independent critical-path work. A blocking gap gets one concise ruling
  request with a recommended one-line disposition; do not multiply decision memos.
- Use existing validated concurrency. Investigate additional concurrency only when
  Jimmy explicitly authorizes it and the expected wall-clock saving is material.
- Test proportionally: one full baseline at session entry, focused tests for changed
  mechanics, and one full suite before commit. Do not rerun the full suite without an
  intervening code change or a specific verification need.
- Reconcile the dashboard and write the dated handoff once at session closure. A
  mid-session update is warranted only when handing control to another agent.
- Do not create documentation that merely restates an existing authoritative document.

### Paper-conversion triggers

- When W3 readings exist, immediately fill every licensed statistics/results
  placeholder those readings support. Do not wait for G4 to draft clearly marked
  descriptive results.
- When each label wave lands, run its G4 branch and update the corresponding paper
  tables incrementally. Do not wait for all designs when a truthful partial fill is
  licensed.
- Gate verdicts and release claims still require every frozen prerequisite; speed never
  authorizes premature interpretation.

### Session success and effort budget

Every execution session names one primary deliverable that advances the critical path.
Prefer, in order: completed measurement/adjudication stage → validated readings/gate
artifact → paper section populated from that artifact → supporting mechanics or
documentation. A session producing only audits, plans, dashboards, or handoffs is
incomplete unless a genuine STOP condition prevented execution.

Target at least 80% of session effort on critical-path execution and at most 20% on
testing, documentation, dashboard maintenance, and handoff work combined. Every new
handoff must state (a) paper-facing progress, (b) the next paper-conversion trigger,
and (c) any ancillary work performed and why it was blocking.

## Project dashboard (LIVING document — binds ALL agents)
`00-PORTFOLIO/project-dashboard.html` is the rolling project dashboard: plan since genesis,
timeline, gate status, who-owes-what lanes, session forecasts, live status, changelog.
**It is the ONE file exempt from the report-immutability rule** (Jimmy's direction,
2026-07-11) — update it IN PLACE; never fork it into dated copies. Every agent — Anthropic/
Claude, OpenAI/Codex, or any other model — must:
1. **Read it at session start** (alongside this file and the latest dated handoff).
2. **Update it at session end**: refresh the Live-status panel + any section your session
   made stale, bump the "Last updated" line, append a Changelog row (§8 of the page).
3. Revise its session forecasts only on material change.
4. Keep it self-contained (inline CSS, no JS, no external fonts/CDNs — must render offline).
Dated reports/handoffs remain the immutable evidentiary record; the dashboard summarizes
and cites them, never replaces them. The full protocol is in the HTML comment at the top
of the file itself.

## Session convention
Work TDD. End every session with a NEW dated handoff (`00-PORTFOLIO/YYYYMMDD-*-handoff.md`)
summarizing what was done / what remains / file locations / known issues, **plus the
dashboard update above**, then a commit + fast-forward push of WALKWORTHY paths only
(explicit pathspecs). There is no external memory — the handoff IS the persistence (and
the dashboard is the at-a-glance view of it).
