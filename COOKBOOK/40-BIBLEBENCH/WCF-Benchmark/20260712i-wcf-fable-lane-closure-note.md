<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# WCF-Bench — Fable/Claude Lane CLOSURE NOTE (2026-07-12, end of S25)

**Purpose:** the permanent record of what the Claude (Fable) lane completed and the
exact state it left behind, written at final session closure after Codex began
executing. Future sessions (any model): the live entry points are
`20260712g-codex-standing-boot-prompt-v2.md` (Codex, every session) and
`project-dashboard.html` — NOT this note. This note is history.

## 1. What the Claude lane completed (25 sessions, 2026-07-06 → 2026-07-12)

- **Design + bank:** 10 method-major designs, 230/230-item bank authored, audited,
  frozen (`05-BANK-YAML/`), anchor registry, shared spine, contested-item scoring
  ruling.
- **Harness:** 492-test offline suite; judge qualification (K=8 majority gating, frozen
  manifests), per-keypoint AWARD scoring, transcripts persistence, perturbation
  materialization, checkpoint/resume runner.
- **MVP run:** 816/816 cells, 0 errors, DESCRIPTIVE-only (harness shakedown, not
  measurement).
- **Judgment ledger:** binding rulings **R1–R68**, complete and CLOSED — including the
  parser-artifact forensics (R42/R47), panel of record gemini-flash + grok-4.20 (R43),
  the gated-run pre-registration (R58–R68), and the compute/adjudicate/ratify
  separation (R67.4).
- **Paper:** `08-PAPER/` pre-draft (S24) — master outline with frozen editorial
  decisions E1–E8, 10 sections, results scaffolds keyed to the prereg, independently
  verified (24 MVP figures memo-verbatim; ~40 prereg items zero-deviation).
- **Handover:** standing Codex boot prompt **v2** + Jimmy-ratified execution-plan
  AMENDMENT (paper lane P1–P4) + AGENTS.md/dashboard repointing (S25).

Final Claude-lane commits: `f42151d09` (S24 paper pre-draft), `ad12deb73` (S25 Codex
consolidation), plus this closure commit. All pushed to `origin/main`.

## 2. State at closure (verified 2026-07-12, after Codex started)

- `main` == `origin/main`; no uncommitted Claude-lane files. Codex had **not yet
  committed** at closure time (no commits after `ad12deb73`; PENDING-QUESTIONS.md had
  no new open items).
- Untracked-by-design and deliberately left alone: `screenshots/` (2026-07-11 dashboard
  captures, not this lane's), sibling-project dirty files at repo root, and ALL
  existing branches/worktrees — including `codex/wcfbench-mvp-testable` (merged into
  main at S21, but its worktree still exists and Codex is active; deleting it is not
  this lane's call). No branch, worktree, or file outside this lane was touched.
- Memory system: `wcf-bench-portfolio-state` note **trimmed ~35k → ~1k tokens** (repo
  docs are the history of record; the note now holds only entry-point pointers +
  non-repo-recoverable traps: WCF/-only normative sources per Jimmy, lost session-1 /
  third-family-screen transcripts, the WLC Q1–113 registry gap, OpenRouter gotchas,
  shared-git-index discipline, canary policy). MEMORY.md index line trimmed to match.

## 3. Who owns what now

| Owner | Work |
|-------|------|
| **Codex** (every session: paste boot prompt v2) | T1 → T2 (offline), P1 citations (interleavable); then gate-locked T3–T6 + P3/P4 |
| **Jimmy** | R57 checklist ratification (R58.1); paid-call reauth + $300 NTE budget; G6 raters + G4 co-labeling; R67.4 gate PASS/FAIL adjudication; P4 paper-packet adjudication |
| **Claude** | Nothing scheduled. Re-entry (only if Jimmy directs) = review/escalation per `20260712d-wcf-session23-handoff.md` §4: read the NEWEST handoff + dashboard first; never redo Codex work |

No Fable sessions are planned or required anywhere in this project.

**Canary:** `WCFBENCH-CANARY-c1647-x9k4q` (never re-minted).
