# WCF-Bench — Codex Session 27 Handoff

**Date:** 2026-07-12

**Branch:** `main` (explicitly authorized by the standing v2 boot prompt)

**Scope:** T2 / R54–R56 EPISODE registry application only. No paid calls or spend.

On session open: load `project-dashboard.html` (Live-status first).
On session close: update the dashboard per `AGENTS.md §The project dashboard`.

## Completed

### R54 field application

- Applied every exact R54 correction across all 22 EPISODE entries without rephrasing
  the ruled values.
- Corrected seven `forbidden_markers` lists, all 22 `required_report_facts` lists, the
  single `NARROW-C7-010` success metric, and the exact added
  `NARROW-C2-W202` known-limitation sentence.
- Left every unruled entry field unchanged.

### R56 approval transition

- Renamed the reviewed draft to the canonical approved path:
  `04-HARNESS/config/episode-spec-registry.json`.
- Set registry status to `APPROVED`, all 22 `human_review.status` values to `approved`,
  and the approval block exactly to:
  - reviewer: `20260712-fable-episode-registry-review-memo.md (R54, Fable S22)`
  - reviewed at: `2026-07-12`
- Updated `wcfbench/episode_registry.py` so the canonical approved file is the default
  `REGISTRY_PATH`; `load_episode_registry()` now loads it outside review mode.

### R55.4 fixture parity and state surfaces

- Added bidirectional marker fixtures for all seven corrected marker lists: a
  key-literal defection exemplar matches and an authored-path obedient exemplar does
  not.
- Added exact registry-contract coverage for all 22 R54 rows and the R56 approval/path
  contract.
- Checked T2 in `20260712-codex-execution-plan-v2.md` and mirrored it on the dashboard.
- Updated `PENDING-QUESTIONS.md` only to record the authorized R54/R56 resolution; no
  unresolved judgment question was added.

## Verification

- Baseline: 513/513 tests passed before changes.
- TDD red: the focused test module failed collection because the canonical
  `REGISTRY_PATH` did not yet exist.
- Focused green: 23/23 `test_episode_registry.py` cases passed.
- Full suite after implementation: 520/520 tests passed offline.
- Bank status check: no path under `05-BANK-YAML/` was modified.
- No OpenRouter, network, live-run, or paid call was made.
- Pytest emitted a post-run warning while cleaning an unrelated temporary directory;
  no test failed and no WCF repository path was involved.

## Shared-mainline note

- During session close, concurrent commit `aa0477933` advanced `main` and `origin/main`.
  It incorporated the T2 registry, loader, tests, execution-plan checkbox, and
  `PENDING-QUESTIONS.md` updates from the shared worktree together with unrelated
  portfolio changes.
- That commit was not rewritten or amended. The subsequent path-scoped session-close
  commit contains only this WCF handoff and the WCF dashboard update.

## Next

1. Jimmy alone checks and ratifies T1/T2 through the pre-registered R57 checklist
   (T2.5 / R58.1). Codex must not self-ratify or mark MVP testable.
2. While T2.5 waits, P1 citation verification is the next ungated Codex task. Resolve
   the three `[VERIFY-CITATION]` tags in `08-PAPER/03-related-work.md`; escalate rather
   than delete or invent a citation if evidence cannot be obtained.
3. Do not begin T3 or T4 without their explicit Jimmy gates. Paid OpenRouter calls
   remain paused.

## Deliberate non-actions

- No bank YAML, prompt, historical run directory, historical report, binding memo, or
  manifest was modified.
- No R55.1–R55.3 runner build, EPISODE live run, candidate screening, G6 work, paid
  call, T3/T4 execution, or gate adjudication was started.
- Dirty sibling-benchmark files and the WCF `screenshots/` directory were left
  untouched.
