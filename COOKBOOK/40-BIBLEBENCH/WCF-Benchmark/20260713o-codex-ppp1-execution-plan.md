# PPP-1 Execution and Manuscript Packet Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Execute the owner-authorized frozen PPP-1 scope once under a strict pre-call
`$23.56` cap and immediately produce its labeled exploratory manuscript packet.

**Architecture:** Add one narrow `ppp1_run.py` entrypoint that composes the existing
MVP, EPISODE, evidence-capture, retry, and accounting seams. It consumes the frozen
preflight manifest and corrected qualification manifest, permits only the frozen single
Gemini preview judge, uses the existing scorer prompts unchanged, and writes only a new
dated immutable run directory. A separate offline analysis step converts that immutable
record into a new dated preview packet without editing release-labeled manuscript files.

**Tech Stack:** Python stdlib, existing `wcfbench` harness, pytest, Markdown/JSON/CSV/SVG.

---

## Global acceptance ceiling

- Exact roster and 226-item scope; 678 total cells.
- SUT output cap 2,048; judge output cap 512.
- Strict reservation-aware pre-call cap `$23.56`; no new call begins if its conservative
  ceiling would cross the cap.
- Exactly one authorized paid execution; retry/error survival only, no rerun.
- Existing scorer/prompt text and frozen bank remain byte-identical.
- Every output carries the exact exploratory/single-judge/non-quotable label.
- After evidence exists, stop engineering and build the paper packet immediately.

## Task 1 — Minimal PPP-1 runner seam

**Files:**

- Create: `04-HARNESS/ppp1_run.py`
- Create: `04-HARNESS/tests/test_ppp1_run.py`
- Reuse unchanged: `04-HARNESS/wcfbench/mvp.py`, `04-HARNESS/episode_run.py`,
  `04-HARNESS/format_bridge_requal.py`, `04-HARNESS/wcfbench/judge_panel.py`

- [x] Write focused failing tests first for exact identity/roster/caps, 204 normal + 22
  EPISODE selection, single-Gemini manifest eligibility, strict reservation before every
  mocked call, append-only checkpoint/raw evidence, retry/error survival, `--go` safety,
  immutable destination validation, and complete/partial metadata labels.
- [x] Run
  `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/test_ppp1_run.py -q`
  from `04-HARNESS/` and observe the required tests fail because the seam is absent.
- [x] Implement only the tested entrypoint. Reuse the exact existing scoring functions and
  prompts; do not modify production panel semantics. The preview adapter may relax only the
  judge-count aggregation for this explicitly single-judge artifact while still consuming
  the frozen manifest's per-surface eligibility.
- [x] Run the focused tests green, then the full offline suite.
- [x] Receive one specification review and one code-quality review. Fix only findings that
  threaten validity, the strict cap, immutability, blindness, reproducibility, or an owner
  ruling. A second-cycle new finding returns to Jimmy.

**Gate status 2026-07-13:** specification re-review PASS after the first bounded P1 fix
cycle. The subsequent general quality review found a new interruption-custody P1. Per the
binding second-cycle rule, Task 1 is paused for Jimmy's fix/disclose/narrow/defer choice;
no paid attempt has started.

**Gate update 2026-07-13:** Jimmy authorized only the interruption-custody fix. Commit
`5056df116` plus one regression closed that named blocker; named-blocker-only quality
re-review PASS, focused 25/25 and full 725/725. The authorized command then failed closed
during zero-paid catalog preflight before output-directory creation or inference because
the live four-row catalog hash changed. Task 2 remains unchecked; `$0` was spent and the
one-run authority is unconsumed pending Jimmy's catalog-refresh ruling.

**Done when:** the mocked end-to-end plan records all 678 cells as scored-or-error, every
attempt is evidence-accounted, no call can start beyond the strict reservation cap, and
the full offline suite is green.

**Do not:** refactor shared modules, add models/judges, modify prompts, add perturbations,
touch T4, edit bank files, or build convenience tooling.

## Task 2 — One authorized paid execution

**Output:** new `07-PILOTS/20260713-ppp1-exploratory-preview/` only.

- [ ] Before inference, perform the runner's R40.1 auth and catalog checks, validate the
  four exact slugs/prices and at least `$23.56` remaining balance, then freeze run identity.
- [ ] Start the one authorized run with `--go`, judge cap 512, SUT cap 2,048, budget 23.56,
  exact new output directory, and no substitutions.
- [ ] Allow only registered retries. Persist isolated cell failures as errors and continue;
  never debug or rerun them.
- [ ] Reconcile response-attributed run cost and contextual shared-key delta; do not assign
  concurrent shared-account spend to PPP-1 without evidence.

**Done when:** all 678 cells are scored-or-error-recorded, or the strict cap stops the run
with every completed attempt persisted. The authorization is consumed either way.

## Task 3 — Immediate exploratory manuscript packet

**Files:** create only under `08-PAPER/20260713-ppp1-exploratory-preview/`.

- [ ] Parse the immutable run record offline and create traceable per-design, per-SUT, and
  aggregate CSV/Markdown tables with denominators and error/ungraded counts.
- [ ] Create the minimum useful self-contained SVG figures directly from those tables.
- [ ] Draft preview Results, evidence-supported Discussion, conspicuous limitations box,
  and an assembled manuscript preview. Preserve uncertainty and do not make rankings,
  gate, release, family-level, consensus, or quotable claims.
- [ ] Include a provenance map from every displayed value to immutable run fields.
- [ ] Receive one specification review and one quality review, fixing only P0/P1 blockers.

**Done when:** Jimmy can review one assembled, labeled, paper-shaped packet containing the
required tables, figures, Results, Discussion, limitations, and traceability map.

## Task 4 — Close and hand off

- [ ] Resolve the PPP-1 authorization question in `PENDING-QUESTIONS.md` without rewriting
  historical text; append the execution outcome or blocker.
- [ ] Update only authorized WCF/portfolio live surfaces whose WCF contract materially
  changed; preserve unrelated dirty changes.
- [ ] Run fresh focused and full verification plus artifact/secret/bank/run immutability
  checks.
- [ ] Write a new dated session handoff, update `project-dashboard.html`, commit and push
  explicit WCF paths, reload the dashboard in the browser, visually verify it, and leave it
  open for Jimmy.

**Stop condition:** deliver the exploratory packet and ask Jimmy for manuscript review.
Do not proceed to T4 or any additional paid activity.
