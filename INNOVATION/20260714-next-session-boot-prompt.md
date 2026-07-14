# INNOVATION — Next Session Boot Prompt (P3 draft-v1 build)

**Written:** 2026-07-14 (post-window, at Jimmy's request; state verified unchanged since the
2026-07-11 P3-gate session — PR-02/PR-03 still open, no keys). **Use with:** a fresh **Opus**
session (`/model opus`, `/clear` first) in `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/`.
Paste the block below verbatim. The same prompt is mirrored in `INNOVATION/project-dashboard.html`
§12 (kept in sync per `AGENTS.md §The project dashboard`).

---

This is an Opus session, single lane: `CEI-Lit-WS/INNOVATION/`. EXECUTION mode — produce files,
not plans. The Fable window is closed: escalations go to PENDING-RULINGS (Jimmy decides), never
self-approve. Tiering still applies: delegate mechanical work (searches, formatting, batch edits)
to Sonnet agents with explicit `model=`; keep drafting judgment in the main loop.

**Step 0 — state sync:** read `INNOVATION/project-dashboard.html` (Live status + §12 first), then
`INNOVATION/AGENTS.md`, then the latest handoff `INNOVATION/20260711-p3-gate-session-handoff.md`.
Branch: **if PR-03 has been signed** in `PENDING-RULINGS.md`, add a Sonnet agent to apply the §6
patch from `20260710-stage4-vocab-reconciliation-proposal.md` mechanically (+ validator, tick 3.5).
**If API keys have landed** (Jimmy gate #1), log it in the handoff and dashboard but do NOT expand
this session's scope — Cycle 2 gets its own session; draft-v1 comes first. Neither PR may be
self-approved.

## Mission — build P3 draft-v1 per the BINDING work order

Read `INNOVATION/20260711-fable-p3-presubmission-review.md` IN FULL first — its §5 is the work
order and every item is REQUIRED unless marked optional. Inputs (read-only):
`40-BUILDS/p3-position-paper/20260709-draft-v0.md` (FROZEN — never edit),
`20260711-ledger-v2.md` (current ledger: 61 VERIFIED / 3 SEARCH-CONFIRMED / 0 ⚠),
both `20260711-review-*.md` files.

**Output:** `40-BUILDS/p3-position-paper/20260714-draft-v1.md` (NEW dated file; use the actual
session date) + a one-page change map keyed to work-order item codes
(A-1…A-9 correctness · B-1…B-5 repositioning · C-1…C-4 evidence hygiene). Add no new claims
without ledger rows; kill nothing the work order doesn't name.

**The three verification side-tasks (work order §C, do before finalizing the affected sections):**
- **C-1:** S1/S10 (OpenAI web artifacts) — Playwright-render + prose-verify per the Lane-B
  manual-ingest precedent (upgrades them to VERIFIED as web-artifact records; new ledger rev =
  new dated file, ledger-v2 stays frozen), OR keep explicit web-citation hedging with URL +
  access date. S11 (paywalled Springer): cite with DOI + "not independently verified"; do NOT scrape.
- **C-2:** verify §6's utility-engineering characterization ("coherent, scale-strengthening value
  systems") against the on-disk extract `PDF Extracts/2025/2025-Mazeika-Utility Engineering.md`
  before draft-v1 ships it; the "NeurIPS 2025 spotlight" venue token stays struck unless evidenced.
- **C-3:** check Berriaud & Wattenhofer (AAMAS 2026, clone-robust benchmark aggregation) —
  verify identity before any download (arXiv API / abs page; never guess IDs) — and adjust
  contribution 4a's originality claim if it preempts.

## Hard rules (non-negotiable)

- **Lane isolation:** only touch files created in THIS session's lane (+ the living files:
  dashboard, AGENTS.md, 04-decision-log, 07-opus-handoff, PENDING-RULINGS, memory).
- **Git:** stage only your own named files; verify `git diff --cached --name-only` against your
  list; plain `git commit`; NEVER `git add -A`, NEVER pathspec commits (DL-22); `git log -1`
  before committing (shared worktree).
- Report immutability (new dated files only; draft-v0, ledger-v1, ledger-v2 frozen) · evidence-class
  tags travel with every citation; nothing ⚠/SC enters prose as unhedged fact · `tags: ` empty
  scalar on any new paper record · **grep the WHOLE vault by arXiv ID before acquiring anything
  (DL-26)** · run `validate_all_papers.py` ONCE if records were created · no `rm` ever (RECYCLE-BIN).

## Close the books

Queue draft-v1 + change map for the **light re-gate** (Opus memo → Jimmy, per
`20260711-fable-gate-protocols-memo.md` §1 pattern; the re-review checks the change map against
the work order only — it does not reopen settled findings; external use remains Jimmy's decision
regardless). Then: dated handoff `INNOVATION/20260714-<x>-session-handoff.md`; DL entries in
`00-CHARTER/04-decision-log.md`; update the `innovation-portfolio-state` memory; **update the
dashboard per `AGENTS.md §The project dashboard`** — Live status, changelog row, and REWRITE §12
to the re-gate session's prompt; commit (staged-only) + push.

---

**Why this prompt exists:** the P3 double gate is executed (CONDITIONAL-GO, 2026-07-11) and the
lane's only remaining session-executable work is the revision pass it ordered. After draft-v1 +
re-gate, everything left in the lane is Jimmy-gated (PR-02, PR-03, keys → Cycle 2).
