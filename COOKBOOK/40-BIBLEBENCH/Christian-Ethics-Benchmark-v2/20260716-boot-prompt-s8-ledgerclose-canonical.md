# BOOT PROMPT — WALKWORTHY v2 session 8: F-ledger close-out + canonical-readiness + v-next scoping

Paste/read this at the start of a fresh session. It is self-contained.

## Mission

Session 7 drained the F-ledger's executable core: the owner ruled the full decision
grid (F11 RATIFIED, F4 closed at B, 02 re-pin ruled for v-next) and both remaining
live arms fired clean (F7: context judging moves design-07 per-turn verdicts 27%/11%
but does NOT close the 0.53 judge gap; F2-2c: anchors buy ~0 for 02 — F2 fully
CLOSED, the 07-vs-02 gap is an instrument property of the state taxonomy/rubric, not
the anchors). What remains is **synthesis and scoping, not experiments**: (1) an
F-ledger close-out report, (2) a canonical-readiness check against the fit memo §4
preconditions, (3) an owner grid on the R11 flag and the v-next package. Free work
executes; the ONLY candidate paid item is F10 (seed probe) IF the owner scopes it in
— nothing fires without a fresh spend memo + GO (the session-7 GO is CLOSED, ~$1.05–
2.01 spent of $5.50; no rollover).

## Where everything is

- **V2 (work here):** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`
  — Inspect AI 0.3.246, dedicated `.venv` (`$V2/.venv/bin/{python,inspect}`), package
  `walkworthy_inspect` editable-installed. pytest NOT in venv — run `tests/` via
  `python -c "import tests.test_X as t; t.run_all()"`.
- **V1 (READ-ONLY, canonical for now):** `../Christian-Ethics-Benchmark/`. NEVER
  write into it (`PYTHONDONTWRITEBYTECODE=1` if executing v1 code).
- **Stored run data (gitignored, do NOT re-run):** `logs/pilot-20260716/<sut>/`,
  `logs/f2-ablations-20260716/` (now incl. 2c `d02-anchors-on-judge{A,B}.jsonl`),
  `logs/f9-microcheck-20260716/`, `logs/crossharness-20260716/`,
  `logs/judge-certify-20260716/`, `logs/f3-classifier-20260716/`, and session-7
  additions: `logs/f7-context/` (context-judge{A,B}.jsonl, 815 verdicts each) and
  `logs/f4-taxonomy-20260716/taxonomy.json` (2,815 rows).
- **Governance now in force:** `20260716-prereg-comparisons-RATIFIED.md` (C1 m=30
  pairwise / C2 m=70 / α=0.05 blunt Bonferroni / n≥20 single-turn floor /
  divergence poles-only / freeze-nano / stratification-multiplier formula / C9
  first-use) + `20260716-owner-rulings-s7-decision-grid.md` (the four s7 rulings) +
  `20260716-design02-classifier-pin-decision.md` (v-next re-pin, memo-only).

## Current state (end of session 7, 2026-07-16; local CEI-Lit-WS main = `1661f61b3`, SEVEN commits ahead of origin AND origin has DIVERGED — sibling WCF commit `227f123e3` is on origin but not local; `git pull --rebase` REQUIRED before any push; don't push unless asked)

- **F-ledger status: F1 RATIFIED · F2 CLOSED (2a+2b+2c) · F3 DONE · F4 CLOSED at B ·
  F5 DONE · F7 DONE · F8 DONE · F9 DONE · F11 RATIFIED.** Open: F6 (dormant,
  design-memo-first, coupled to un-ruled F4-C) and F10 (seed probe, never specified
  in detail — scoping it IS session-8 work if the owner wants it).
- **F7 results** (`20260716-f7-context-judging-results.md`): prior-turn context moves
  per-turn states (judge-A agreement with shipped 0.727 = 27% move; judge-B 0.890 =
  11% move) → descriptively corroborates R11 order-sensitivity; cross-judge gap NOT
  closed (0.531→0.537); arc_pass floor-saturated (1/135→2/135). Instrument evidence,
  C9-labeled. NOTE THE COUNT CORRECTION: design-07 stored data = **163 turns/SUT
  (815/judge)**, not the 109/1,090 an earlier prompt claimed.
- **F2-2c results** (`20260716-f2-2c-results.md`): d02 anchors-on cross-judge
  0.247→0.242 (≈0 effect). With 2a: the 07-vs-02 judge gap is a property of the
  state taxonomy/rubric, NOT the anchor block. nano≫llama anchor-asymmetry
  replicated a third time (2a/2b/2c).
- **F4-B** (`20260716-f4-optionB-engaged-derivation.md`): `_derive_engaged` live in
  `scorers.py`; equivalence proven byte-identical two ways (recompute hashes +
  monkeypatch-to-raise proof that primaries never touch `_refusal_cell`); 17/17
  tests; taxonomy is DESCRIPTIVE-ONLY, 70 rows un-flagged across 17 cells;
  stratum-(c) rows labeled "policy-pending" until F4-C/F6 is ever ruled.
- Tool gotchas (carried + new): Inspect `Score.value` rejects nested dicts
  (turn_states JSON-encoded — decode); sample_ids COLLIDE across SUTs — scope joins
  by (sut, log basename, sample_id, rec_index); judge-free metrics have degenerate
  judge-swap bands; `certify-events.jsonl` is shared across judges — filter by
  `judge_model`; `judge_context_ablation.py`'s batch driver DISCARDS per-call usage
  objects (output spend is estimate-only ~60 tok/call — if a future run needs exact
  spend, log usage first); OpenRouter 402 reservation trap — explicit max-tokens on
  every call.

## Read first (in order, skim)

1. `20260716-f7-context-judging-results.md` (the R11 evidence and its limits)
2. `20260716-f2-2c-results.md` (what closed F2; the instrument-property conclusion)
3. `20260716-prereg-comparisons-RATIFIED.md` (the comparative-claims machinery now live)
4. `20260715-inspect-fit-assessment.md` **§4** (the canonical-ruling preconditions —
   session 8's centerpiece checks against these)
5. `REVIEWS/20260716-adjudication-benchmark-critique.md` (R-rules + original F-ledger)
6. `AGENTS.md` (402 trap, PF-003 $5 gate, no deletions, v1 read-only)

## Task 0 — Decision grid (owner; present FIRST, then continue free work regardless)

1. **R11 flag ruling.** F7 gives direct evidence: design-07 per-turn judging is
   order-SENSITIVE (verdicts move with context) but context does not reconcile the
   judges (gap ~0.53 either way) and the arc-level summary is floor-saturated either
   way. Options: (a) RETAIN the PROVISIONAL flag as-is; (b) CONVERT it to a
   permanent, sharper caveat ("per-turn verdicts are context-dependent; the shipped
   context-free protocol is the pinned instrument; cross-judge disagreement is a
   rubric property") — recommended shape given the evidence; (c) LIFT (not supported
   by the data — gap persists). On ruling: new dated adjudication addendum; the
   REVIEWS file stays immutable.
2. **v-next package scope.** Which items enter v-next scope NOW (scoping ≠ running;
   each carries its own future spend gate): 02 re-pin implementation · design-07
   floor-saturation item revisions (touches the ratified 510-item review; the F2
   conclusion "gap = taxonomy/rubric" argues rubric work accompanies item work) ·
   adversarial-parrot probe set (construct work, owner scopes) · F10 seed probe ·
   F6/F4-C DSP policy (design-memo-first). Owner picks any subset, or defers all.
3. **Canonical-readiness ruling — AFTER Task 2's memo is in front of the owner** (do
   not ask cold; the memo states which §4 preconditions are met/unmet).

## Task 1 — F-ledger close-out report (free)

New dated `YYYYMMDD-f-ledger-closeout.md`: every F1–F11 item, its status, the
artifact(s) that discharged it, what it changed in the instrument or its governance,
and the residual risk it leaves. This is the capstone synthesis — write it so a
reader who has seen nothing else understands what the adjudication cycle bought.
Include the two dormant items (F6, F10) with their activation conditions. Fable
writes/adjudicates this in the main loop; delegate only mechanical fact-pulls
(model: sonnet/haiku, explicit).

## Task 2 — Canonical-readiness check (free)

Read `20260715-inspect-fit-assessment.md` §4 (the preconditions set when v2 was
ruled a PARALLEL EXPERIMENT with v1 canonical). New dated memo: each precondition —
met (cite artifact) / unmet (what's missing) / changed-in-meaning (explain). End
with a recommendation ladder for the owner (rule v2 canonical now / after named
gaps close / keep parallel), but the RULING is the owner's (Task 0.3). Do NOT flip
any canonical designation yourself; no README/status edits until ruled.

## Task 3 — Execute per Task 0 rulings (free)

- R11 ruling → dated adjudication addendum (supersede-by-pointer; REVIEWS immutable).
- v-next scoping → one dated v-next scope memo listing what's IN with per-item
  activation conditions + spend-gate placeholders. If F10 is scoped in: specify the
  probe design (which cells, which seed policy, expected call count, honest cost) —
  spec only, into the spend memo, NO run without GO. If F6 is scoped in: design memo
  only (it edits scoring semantics and couples to the un-ruled F4-C).
- Canonical ruling → if the owner rules a designation change, a dated ruling memo
  records it; implementation (README/status-line edits across v1+v2) only if the
  owner explicitly asks this session.

## Gates (hard)

- **No pre-authorized paid work exists this session.** If and only if F10 (or
  anything else) is scoped in with a spec, ONE consolidated spend memo at the end,
  then STOP for explicit owner GO (PF-003; session-7 GO is CLOSED, no rollover).
- Availability probe (max_tokens=16) before any authorized run (R10).
- Priority if context runs short: Task 0 grid + Task 1 close-out ship first; Task 2
  memo second; Task 3 executions third.

## Standing constraints (hook-enforced + conventions)

- NO deletions ever (`rm` blocked; the guard scans whole command strings — don't
  even quote such commands) — `mv` to `RECYCLE-BIN/`. Reports immutable: new
  `YYYYMMDD-` files only; supersede by pointer, never edit.
- Shared git trunk: pathspec-commit `COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2`
  only; verify origin state at start (`git log --oneline -1 origin/main` — origin
  DIVERGED at `227f123e3`; a sibling may have pushed/rebased since; `git pull
  --rebase` before any push; don't push unless asked).
- Model tiering: Fable main loop = adjudicate/synthesize (Tasks 1–2 are main-loop
  work); opus = judgment-bearing agents; sonnet/haiku = mechanical. Explicit `model`
  on every Agent dispatch (hook checks `tool_input.model`).
- Handoff/session-wrap skills RETIRED — no handoff docs unless the owner asks.
  Auto-memory continues (`20260716d-walkworthy-v2-s7-rulings-f7-f2c.md` is latest).
- Canary `WALKWORTHY-CANARY-7f3e2026` preserved everywhere; holdout
  (`banks-holdout/`, `datasets/holdout/`) never enters prompts, reports, or git;
  `WALKWORTHY_ALLOW_HOLDOUT` stays unset.
- OpenRouter: ALWAYS explicit max-tokens (402 trap); key via
  `source ~/.codex/secrets/openrouter.env`.

## Known open items deliberately OUT of scope (do not pick up unbidden)

IMPLEMENTING anything v-next this session (02 re-pin, item/rubric revisions,
parrot probes — Task 0.2 produces a SCOPE memo, not code or runs) · F6/F4-C coding
in any form (design-memo-first if scoped) · flipping the canonical designation or
editing READMEs before the owner rules · re-running ANY stored logs · using the
divergence split as a headline stratifier beyond what the RATIFIED file allows ·
pushing to origin unbidden (diverged trunk — rebase hazard).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
