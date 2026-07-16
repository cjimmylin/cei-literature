# BOOT PROMPT — WALKWORTHY v2 session 7: owner-decision execution + F7 (design-07 context judging)

Paste/read this at the start of a fresh session. It is self-contained.

## Mission

Session 6 converted the open ledger into **owner decisions**: F11 ratification (5
marked points), the F4 refusal-policy pick (A/B/C ladder), and a NEW decision F3
surfaced (the design-02 classifier pin). This session (1) presents that decision grid
FIRST and executes whatever the owner rules, and (2) runs **F7** — the design-07
prior-turn-context judging experiment (JV-8) — which F3's cross-family result just
unblocked AND narrowed: 07's stimulus base is cross-family stable (alt-agree
0.77–0.97), so a context-judging effect there is attributable to JUDGING, not to
stimulus instability. Free/offline work executes; **every paid call waits behind one
consolidated spend memo** (§Gates — the session-6 GO is SPENT ~$0.30 of $1.15; it
does not roll over; F2-2c remains un-fired and opt-in).

## Where everything is

- **V2 (work here):** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`
  — Inspect AI 0.3.246, dedicated `.venv` (`$V2/.venv/bin/{python,inspect}`), package
  `walkworthy_inspect` editable-installed. NOTE: pytest is NOT in the venv — run
  `tests/` via `python -c "import tests.test_X as t; ..."` or install pytest first.
- **V1 (READ-ONLY, canonical):** `../Christian-Ethics-Benchmark/`. NEVER write into it
  (set `PYTHONDONTWRITEBYTECODE=1` if executing v1 code).
- **Stored run data (gitignored, do NOT re-run):** `logs/pilot-20260716/<sut>/` (50
  `.eval` + judgeB verdicts), `logs/f2-ablations-20260716/`, `logs/f9-microcheck-20260716/`,
  `logs/crossharness-20260716/`, and session-6 additions:
  `logs/judge-certify-20260716/` (124 certify events + summary, 3 judges) and
  `logs/f3-classifier-20260716/` (2× 1,435 alt-classification JSONLs).
- **Ratified divergence tags:** `banks/20260716-divergence-tags.jsonl` (29/129/186) —
  usable WITH the calibration caveat; headline usage governed by the F11 draft.

## Current state (end of session 6, 2026-07-16; local CEI-Lit-WS main = `8a3425f8d`, FOUR commits ahead of origin — d61273d9b/5b24ace3e/fc2075ced/8a3425f8d NOT pushed; verify origin at start, siblings push-cascade this trunk)

- **F8 DONE:** vacuous-ok parser defect fixed at source (`ok` requires non-empty token
  spec); recompute byte-identical to shipped pilot + F9 reports; 8 regression tests.
- **F5 DONE + EXECUTED:** `tools/audit/judge_certify.py` (40/40 prompt-hash-identical
  to v1's frozen 20260713 run). **ALL THREE judges G5-certified on both designs** —
  nano (1 cleared initial violation), llama-3.3-70b (clean), gpt-4.1-mini (1 cleared).
  KEY NUANCE: anchor-hungry (F2) ≠ conclusion-penalizing (G5) — certification lifts
  R6's PROVISIONAL labels (future reports cite
  `20260716-f5-certification-results.md`); anchor-dependence remains real and is still
  mitigated by R4's 2-judge rule. Replacement-judge line 1d never fired (MOOT).
- **F3 DONE (both halves):** offline heuristic-replay divergence 24–56% (02) / 83–91%
  (07); cross-family arm: **alt-alt agreement 0.902 ≫ alt-vs-nano ~0.70; on 24.4% of
  turns both alt families agree AGAINST nano** — nano is the outlier classifier,
  epicenter design 02 `refused→complied` (nano over-calls "refused"). 07 cross-family
  is moderate-good (0.77–0.97) → the heuristic, not the models, was the outlier there.
  **Consequence already encoded: F11 C6 = pinned classifier, NO cross-classifier
  pooling ever.** Reports: `20260716-f3-classifier-sensitivity-report.md` +
  `20260716-f3-crossfamily-classifier-results.md`.
- **F11 DRAFT shipped** (`20260716-prereg-comparisons-draft.md`) — NOT ratified; R1/R3
  stand (no comparative claims) until the owner rules on its 5 marked points.
- **F4 options memo shipped** (`20260716-f4-refusal-taxonomy-options.md`) — decision
  ladder A (stand pat) → B (derive `engaged`, descriptive table) → B+C (settle the
  DSP both-poles-decline policy; sequence C after F6).
- Tool gotchas (carried + new): Inspect `Score.value` rejects nested dicts
  (turn_states is JSON-encoded — decode it); ablation/verdict JSONLs span SUTs whose
  sample_ids COLLIDE — always scope joins by log basename / (sut, log, sample_id,
  rec_index) tuples; judge-free metrics have a degenerate judge-swap band (Δjudge=0) —
  never read "outside band" there as an effect; `judge_certify.py` events for ALL
  judges share one `certify-events.jsonl` — filter by `judge_model` before any tally;
  `classifier_sensitivity.py --alt-classifier` buffers all rows in memory and writes
  the JSONL only at completion (no partial file = still running, not failed).

## Read first (in order, skim)

1. `20260716-f5-certification-results.md` (what certification did and did NOT validate)
2. `20260716-f3-crossfamily-classifier-results.md` (the nano-outlier evidence; C6)
3. `20260716-prereg-comparisons-draft.md` (the 5 ratification points the owner rules on)
4. `20260716-f4-refusal-taxonomy-options.md` (the A/B/C ladder)
5. `REVIEWS/20260716-adjudication-benchmark-critique.md` (R-rules + F-ledger — still
   the authoritative list; F5/F8 now DONE, F3 DONE, F2 core DONE, F1 RATIFIED)
6. `AGENTS.md` (402 max-tokens trap, PF-003 $5 gate, no deletions, v1 read-only)

## Task 0 — Decision grid (owner; present FIRST, then continue with free work regardless)

Present compactly and ask for rulings; do not block offline F7 work while waiting:

1. **F11 ratification** — the draft's §4: (a) C1 family shape (30 pairwise vs
   omnibus+post-hoc), (b) C5 single-turn floor (proposed n≥20), (c) C3 partial-stratum
   restriction, (d) C6 classifier-pin policy when judge-A changes, (e) α (default
   0.05). On ratification: write a NEW dated ratified file citing the draft (draft
   stays immutable), and note R1/R3 remain in force for all existing data (C9
   first-use rule).
2. **F4 pick** — A / B / B+C. If B: implement (Task 2). If C in any form: DESIGN memo
   only this session (C couples to F6 and edits scoring semantics — do not code it
   unbidden).
3. **Design-02 classifier pin** (new, from F3): keep nano / switch / consensus route —
   each option is a NEW instrument version under C6. Decision memo only; NO
   implementation or re-runs this session (any new 02 run under a new pin is v-next
   work with its own spend gate).

## Task 1 — F7: design-07 prior-turn-context judging (offline assembly free; live arm gated)

R11 flags design-07 per-turn judging as order-blind for order-dependent states; JV-8
is the experiment. F3 cleared its sequencing gate and improved its interpretability
(07 stimuli are cross-family stable).

1. Build `tools/audit/judge_context_ablation.py` mirroring
   `tools/audit/judge_ablation.py`'s monkeypatch-and-restore philosophy: re-judge the
   stored 07 per-turn responses from `logs/pilot-20260716` with the prompt augmented
   by PRIOR-TURN CONTEXT (the administered user turns + SUT responses up to turn
   i−1, read from store `ww_turns`), versus the shipped context-free verdicts as
   baseline. Assembly must reuse `assemble_rubric_prompt` (patch the response/unit
   surface, do not fork the assembler). No SUT calls; judge calls only.
2. Metrics (offline once verdicts exist, pattern = `ablation_agreement.py` with
   log-basename-scoped joins): per-turn state agreement context-vs-blind per judge;
   cross-judge agreement under context (does context close any of the 07 judge gap?);
   arc_pass_rate movement (R11's PROVISIONAL flag is the target of this evidence).
3. Dry-run cost with BOTH certified judges (A nano + B llama; 109 turns × 5 SUTs ×
   2 judges = 1,090 calls; prior-turn context makes prompts materially longer than
   F2's — expect several × 0.5M input tokens; estimate honestly with chars/4). THEN
   STOP — the live arm goes in the spend memo.

## Task 2 — Execute F4 Option B IF the owner picks it (free, equivalence-gated)

Derive `engaged` from already-judged categories (fix the `scorers.py:331`
`engaged=False` hardcode), report the 4-way taxonomy as a descriptive adjacent table
only. HARD GATE: primaries must be provably unchanged — re-run
`tools/audit/recompute_metrics.py` + `recompute_design05_csr.py` over the stored logs
and byte-compare to shipped numbers (drift = STOP); mock all affected tasks. New dated
note documenting the derivation rule. If the owner picks A: record A as standing
policy in a dated note, close F4 in the ledger, done.

## Task 3 — F11 finalization IF ratified (free)

New dated `YYYYMMDD-prereg-comparisons-RATIFIED.md`: the draft text with the owner's
five rulings filled in, m computed and frozen per family, C9 first-use rule restated.
The DRAFT file is immutable; the ratified file supersedes by pointer (F1-addendum
pattern).

## Gates (hard)

- **One consolidated spend memo** at the end of the free work: the F7 live arm
  (per-judge ceilings; both certified judges) + (only if owner asks) F2-2c
  (~$1.50, still un-fired). **STOP for explicit owner authorization before ANY paid
  call** — PF-003-style; the session-6 GO is CLOSED (~$0.30 spent of $1.15; no
  rollover).
- Availability probe (max_tokens=16) before any authorized run (R10).
- Priority if context runs short: Task 0 decisions + their free executions (Tasks
  2/3) ship first; F7 offline assembly second; the spend memo last-but-required.

## Standing constraints (hook-enforced + conventions)

- NO deletions ever (`rm` blocked; guard scans whole command strings — don't even
  quote such commands) — `mv` to `RECYCLE-BIN/`. Reports immutable: new `YYYYMMDD-`
  files only; supersede, never edit.
- Shared git trunk: pathspec-commit `COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2`
  only; verify `git status` scope AND origin state at start (four local commits are
  unpushed — a sibling session may have pushed them incidentally; check
  `git merge-base --is-ancestor 8a3425f8d origin/main`); `git pull --rebase` before
  any push; don't push unless asked.
- Model tiering: Fable main loop = plan/adjudicate/synthesize; opus = judgment-bearing
  agents; sonnet/haiku = mechanical. Explicit `model` on every Agent dispatch (hook).
- Handoff/session-wrap skills RETIRED — no handoff docs unless owner asks. Auto-memory
  continues (`20260716c-walkworthy-v2-s6-f8-f5-f3-memos.md` is the latest entry).
- Canary `WALKWORTHY-CANARY-7f3e2026` preserved everywhere; holdout (`banks-holdout/`,
  `datasets/holdout/`) never enters prompts, reports, or git; `WALKWORTHY_ALLOW_HOLDOUT`
  stays unset.
- OpenRouter: ALWAYS explicit max-tokens (402 reservation trap); key via
  `source ~/.codex/secrets/openrouter.env`.

## Known open items deliberately OUT of scope (do not pick up unbidden)

F6 DSP judge-prompt credit rule (activates only if the owner's F4 ruling reaches
toward C — and then design-memo first) · F10 seed probe · design-07 floor-saturation
item revisions (v-next bank work, touches the ratified 510-item review) · the
adversarial-parrot probe set (needs authored probe items = construct work, owner
scopes it) · IMPLEMENTING any design-02 classifier change (Task 0.3 is a decision
memo; a new pin = new instrument version = v-next with its own gate) · any use of the
divergence split as a HEADLINE stratifier beyond what F11 proposes · F2-2c unless the
owner names it.
