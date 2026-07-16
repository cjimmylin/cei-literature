# Handoff — WALKWORTHY v2 on Inspect AI (2026-07-15)

**Session:** Christian-Ethics-Benchmark-v2 founding build. **Scope:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/` (new folder; first handoff for this sub-project). **Status:** all planned phases (0, A, B, C, D) COMPLETE. v2 is a **parallel experiment**; v1 (`../Christian-Ethics-Benchmark/`) remains canonical and was not modified.

## What Was Done

### Phase 0 — Scaffold
Folder skeleton; dedicated `.venv` (Homebrew Python 3.14; inspect-ai==0.3.246 + openai — the vault `.venv` is Python 3.9, too old for Inspect); copies of all v1 bank/holdout markdown into `banks/` + `banks-holdout/`; `README.md`, `AGENTS.md` (v1 ops gotchas carried over), `.gitignore` (holdout + logs + venv), and the frozen dataset contract `tools/SCHEMA.md`.

### Phase A — Conversion + Inspect package (2 opus agents, parallel)
- `tools/convert_banks.py`: v1 `walkworthy` builders imported directly under Python 3.14 (no vendoring needed); emits one JSONL line per **administration** per SCHEMA.md. `tools/verify_conversion.py`: parity report.
- `walkworthy_inspect/` (8 modules: datasets loader with `WALKWORTHY_ALLOW_HOLDOUT=1` guard, rubrics ported verbatim, design-05 parser, refusal taxonomy, single/multi-turn solvers, per-design scorers, pair-grouped metrics) + `tasks/design01…10_*.py` + `walkworthy_suite.py`.
- First conversion: **344 public runnable items, exact O4-manifest parity**; 563 public + 260 holdout administration lines; 835 unique ids; canary 100%.

### Phase B — Fresh adversarial review pass (10 opus agents, one per design, parallel with A)
510 items reviewed, 105 stamped fixed, **0 killed**; per-design memos in `REVIEWS/20260715-NN-*-v2review.md`; before/after in `REVIEWS/20260715-consolidated-diff.md` (4,689 lines); ledger in `RULINGS-APPLIED.md`. v1 sources untouched; all fixes on v2 copies.

### Phase C — Convergence + live smoke (1 opus agent)
Re-conversion from reviewed banks (parity re-confirmed 344, report `20260715b-conversion-parity-report-postreview.md`); `metadata.keyed` field names reconciled consumer-side (guessed names in scorers were nearly all wrong; designs 06/09 judge prompts had been unanchored — fixed); v1 `ordo_constraints.py` vendored for exact design-05 CSR; mock re-validation 10/10; **live OpenRouter smoke 10/10** (deepseek-chat SUT × gpt-4.1-mini judge, ~2 samples/design, ≈$0.038, zero provider failures). Report: `20260715-live-smoke-report.md`.

### Phase D — Assessment + wrap
`20260715-inspect-fit-assessment.md` — the parallel-experiment deliverable (fit verdict: strong; preconditions for canonical ruling in §4). Memory file + MEMORY.md index updated.

## Scientific / Substantive Findings

- **Inspect AI eliminates v1's worst operational failure class by construction.** Full transcripts (including 17-message design-02 ladders) persist in `.eval` logs automatically — the PR-9 transcript-loss defect that cost a $27 re-execution in v1 cannot recur.
- **Design-05 items contained parser-breaking accented allocation tokens** (`connected_protégé`, `décor`): the strict parser's regex cannot match `é`, so the judge-free CSR metric would have silently mechanically zeroed. Caught by the review pass, fixed to ASCII (item semantics unchanged).
- **The custom-code surface shrank ~4×** (v1: 32 modules + 66 test files → v2: 8 package modules + 11 tasks + 2 tools) while the measurement-defining assets (banks, rubrics, refusal taxonomy, CSR comparator) transferred verbatim.
- **Live design-05 result is real signal, not harness fault:** deepseek-chat answered in prose without the required allocation block → CSR `unscorable` = SUT format-noncompliance, verified via synthetic compliant answers (CSR 0.5/0.8/1.0).

## User Decisions (grilling rounds 1–3, all explicit)

Port + apply review learnings · all 10 designs · single judge with v1 rubrics verbatim (cross-family = later re-score) · MockLLM + tiny live smoke authorized (<$1) · rulings + fresh review pass · holdout ported gitignored+guarded · deepseek SUT + gpt-4.1-mini judge · **parallel experiment first (v1 stays canonical)** · auto-apply review fixes with diff for later review · parallel tracks from the start · task-per-design package. Full table: plan file + `README.md`.

## Remaining Work

- **P1 — Jimmy reviews the review-pass diff.** `REVIEWS/20260715-consolidated-diff.md` + `RULINGS-APPLIED.md`: 105 auto-applied fixes await owner eyes (chosen mode was auto-apply/diff-later). ~30–60 min skim.
- **P2 — Cross-harness comparability slice.** Run the MVP-A1 60-item subset on both harnesses, same SUT + shared judge; confirm score agreement. Precondition #1 for any canonical-path ruling. Est. < $2, one session.
- **P3 — Validate the 2-judge re-score path.** `inspect score` with a judge-B model over the smoke logs + disagreement-cell script (replaces v1's in-band `needs_adjudication`). Precondition #2.
- **P4 — Small fixes.** Parser edge (`reparse_allocation_response` logs `allocation_ok=True/values={}` on block-less answers); design-07 harness-side matched-quality reference answers; design-06 spec-exemplar review_status stamps (cosmetic); dict-score scalar headline; pair-aware `--limit` helper.

## Open Decisions (next session asks Jimmy)

1. Approve/amend the 105 auto-applied review fixes (P1)?
2. Authorize the P2 comparability slice spend (~$2)?
3. After P2/P3: rule on canonical path (v2 replaces v1 harness for future runs)?

## Key Files

| File | Location | Purpose |
|---|---|---|
| Fit assessment | `20260715-inspect-fit-assessment.md` | Parallel-experiment deliverable |
| Smoke report | `20260715-live-smoke-report.md` | 10/10 live results, costs, commands |
| Parity reports | `20260715-conversion-parity-report.md`, `20260715b-…-postreview.md` | 344-item parity, pre/post review |
| Review ledger | `RULINGS-APPLIED.md` + `REVIEWS/` (10 memos + consolidated diff) | What the review pass changed |
| Contract | `tools/SCHEMA.md` | Frozen dataset shape (producer/consumer) |
| Ops rules | `AGENTS.md` | 402 trap, sampling-params, spend gates |
| Runbook | `METHODS/20260715-walkworthy-v2-inspect-operational-methods.md` | Exact commands |

## Known Issues

- **Parallel-session state:** `origin/main` is 57 commits ahead of local HEAD; our footprint is the brand-new v2 directory only → auto-narrowed commit scope to v2 files; intersection with remote-changed files is empty by construction. Out-of-scope uncommitted changes exist elsewhere in the repo (BIBLEBENCH-PILOT modifications/deletions, stale `.lock` files under v1 `runs/20260713-o5-g7-a1/`) — from other sessions, NOT committed here.
- **Not pushed.** Two local commits only (session work, handoff docs). Push deliberately deferred given the 57-commit remote delta; recommend `git pull --rebase` before pushing.
- Inspect prints cosmetic "Unable to convert value to float" warnings for dict-valued category scores (headline scalar defaults 0.0; per-design metrics are correct) — fit memo §3.1.
- No validators discovered under v2 `{PYTHON,scripts,R}/` (they live in `tools/` and were run in-phase); pre-commit validation step logged as skipped-by-convention.
- `banks-holdout/` + `datasets/holdout/` are gitignored by design — holdout content is disk-only, same as v1's HOLDOUT convention.
