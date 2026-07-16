# BOOT PROMPT — WALKWORTHY v2: adversarial critique → improve → 5-LLM pilot prep

Paste/read this at the start of a fresh session. It is self-contained.

## Mission

Adversarially critique and improve the WALKWORTHY normative-ethics benchmark
(Christian ethics, 10 behavioral designs) to prepare for **test deployment in a small
pilot run with 5 LLMs**. Critique first, fix second, pilot design third; the paid
pilot itself fires only after an explicit owner spend authorization in-session.

## Where everything is

- **V2 (work here):** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`
  — WALKWORTHY on Inspect AI 0.3.246. Dedicated `.venv` (Python 3.14):
  `$V2/.venv/bin/{python,inspect}`. Package `walkworthy_inspect` is editable-installed.
- **V1 (READ-ONLY reference, canonical):** `../Christian-Ethics-Benchmark/` — custom
  harness, paper v0.1 thread, G4 human-label gate. Never modify.
- **Books (ground truth):** `../Christian-Ethics-Books/` — 15 registry works; every
  item anchor must be grep-verifiable there (L9); no direct-Scripture anchors (L8);
  Bahnsen contrast-only.

## Current state (as of 2026-07-16, all committed on CEI-Lit-WS local main)

- **Status: PARALLEL — RULED.** Owner ruling 2026-07-16 (`20260716-owner-ruling-v2-parallel.md`):
  v2 stays parallel to v1 indefinitely as a comparison instrument. Do not re-litigate.
- 344 runnable public items (exact v1 O4 parity), 10 designs, admin-level JSONL in
  `datasets/public/` (holdout gitignored + env-guarded `WALKWORTHY_ALLOW_HOLDOUT=1`).
- Item banks (`banks/`) carry a ratified 10-agent adversarial review (510 items,
  105 fixes, 0 kills — `RULINGS-APPLIED.md`; owner ratified 2026-07-15). Do NOT redo
  item-level copyedit review; the next critique targets a HIGHER altitude (below).
- Harness evidence: judge-path replay PARITY vs v1 (73.2% vs 59.2% inter-judge
  baseline, `20260715c-`); 2-judge re-score validated (`20260715d-`); per-turn 02/07
  scoring with v1 formulas, metric audit fixes, native `inspect score` all landed
  (`20260716-polish-items-report.md`). Mock validation 10/10; cumulative live spend ≈$0.09.

## Read first (in order, skim)

1. `20260716-owner-ruling-v2-parallel.md` + `README.md` (status)
2. `20260715-inspect-fit-assessment.md` (esp. §3 friction, §5 open items)
3. `20260716-polish-items-report.md` (what just changed)
4. `AGENTS.md` (ops rules — 402 max_tokens trap, no sampling params to Opus4.7+/Fable,
   spend gates, no-deletion rule)
5. `RULINGS-APPLIED.md` (what the item review already covered — avoid re-treading)

## Phase 1 — Adversarial critique (refute-first, benchmark-level)

Dispatch independent refute-first critics (opus tier; explicit `model` on every Agent
dispatch — global tiering hook enforces; `adversarial-reviewer` agent type is
read-only, give write-needing critics `general-purpose`). Suggested lenses, one critic
each, disjoint memo files in `REVIEWS/` (`20260716-critique-<lens>.md`):

1. **Construct validity** — does each design measure "walk not talk" as claimed, or
   capability/format-compliance/sycophancy confounds? (design-05 prose-noncompliance
   finding is a live example: format gate vs ethics measure.)
2. **Contested-tier fairness** — stratum (b)/(c) handling: does scoring penalize
   defensible non-Christian or rival-Christian positions? Judge-prompt neutrality.
3. **Judge validity & gaming** — single-judge fragility, judge-family bias,
   length/style artifacts, susceptibility to models that verbalize virtue without
   enacting it; shortcut/lexical exploits.
4. **Statistical design for n=5 pilot** — what can/cannot be claimed from 5 SUTs;
   per-design n, admin pairing, multiple comparisons, which headline metrics are
   stable at pilot scale (per-turn 02/07 metrics have small n per item).
5. **Ops readiness** — cost model (per-turn judging multiplies 02/07 judge calls by
   ladder length), provider failure modes, `--limit` pair-splitting, the stale
   Task-header n=0 display artifact, dict-score scalar headline (fit memo §3.1).

Then **adjudicate in the main loop**: classify findings MUST-FIX-before-pilot /
FIX-later / REJECTED (with reasons), as a dated adjudication memo in `REVIEWS/`.
Surface genuine judgment calls to the owner rather than deciding silently.

## Phase 2 — Implement MUST-FIX items

Direct edits or opus implementation agents per the vault's tiering rules. Re-run mock
validation (all 10 tasks, mockllm) + `tools/audit/recompute_metrics.py` after metric
changes. New dated reports only; never overwrite existing ones.

## Phase 3 — Pilot design memo (owner gate)

Write `20260716-pilot-design.md` (or next date): proposed 5 SUTs (prior-art cheap
tier: deepseek-chat, mistral-small-3.2-24b, gemini-2.5-flash-lite,
llama-3.3-70b-instruct, gpt-4.1-mini — adjust per critique), judge pair (cross-family;
gpt-4.1-nano + llama-3.3-70b matches v1 MVP-A1), item scope (60-item MVP subset vs
full 344 — recommend with cost math), per-design worst-case call budget incl. per-turn
02/07 multiplier, total cost estimate, and gates/claims scope (descriptive only; v1
remains canonical for release evidence — pilot claims must say so).
**STOP for explicit owner spend authorization before any paid run** (PF-003-style
gate; prior authorizations do not roll over).

## Phase 4 — (only after authorization) Run pilot + analyze

Inspect eval per design × 5 SUTs via OpenRouter (`source ~/.codex/secrets/openrouter.env`;
ALWAYS explicit `--max-tokens`), logs under `logs/pilot-YYYYMMDD/`, judge-B re-score
via native `inspect score` (registry now supports it) or `tools/rescore/`, disagreement
cells logged, dated pilot report with per-design cells adjacent to any aggregate
(v1 gate-10 spirit: no composite leaderboard without per-design cells).

## Standing constraints (hook-enforced + conventions)

- NO deletions ever (`rm` blocked by hook) — `mv` to `RECYCLE-BIN/`. Report
  immutability: new `YYYYMMDD-` files only. v1 folder read-only.
- Shared git trunk: sibling sessions (e.g. WCF-Benchmark-v2) commit concurrently —
  pathspec-commit `COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2` only; verify
  `git status` scope before committing; local main is ahead of origin — `git pull
  --rebase` before any push.
- Model tiering: Fable main loop = plan/adjudicate/synthesize; opus = critics +
  implementation; sonnet/haiku = mechanical. Explicit `model` on every dispatch.
- Handoff/session-wrap skills are RETIRED (2026-07-15) — do not write handoff docs or
  run session-closure sequences unless the owner explicitly asks.
- Canary `WALKWORTHY-CANARY-7f3e2026` preserved everywhere; holdout never enters
  prompts, reports, or git.

## Known small residuals (fold into Phase 1 lens 5 rather than fixing blind)

Design-07 harness-side matched-quality reference answers; Task-header n=0 display
artifact for dict-valued scores; pair-aware `--limit` helper; G-gates (G1–G10) not
implemented in v2 (offline-analysis territory; pilot is descriptive regardless).
