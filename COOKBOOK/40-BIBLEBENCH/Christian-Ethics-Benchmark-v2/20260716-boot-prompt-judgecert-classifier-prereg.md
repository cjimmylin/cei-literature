# BOOT PROMPT — WALKWORTHY v2: judge certification (F5) + classifier sensitivity (F3) + F8 + pre-reg memos (F11/F4)

Paste/read this at the start of a fresh session. It is self-contained.

## Mission

Post-ratification instrument hardening, in order: **F8** (parsers.py recovery-path fix
— free code), **F5** (port v1's G5 judge-neutrality certification; the 2026-07-16 F2
ablations proved judge-A is anchor-dependent, so certification is no longer optional
hygiene), **F3** (02/07 branch-classifier sensitivity — the cross-harness run showed
only ~50% of design-07 turns get identical stimuli across harnesses; the classifier IS
the stimulus generator), then two free owner-decision memos: **F11** multiplicity
pre-registration draft and **F4** refusal-taxonomy policy options. Free/offline work
executes; **every paid call waits behind one consolidated spend memo** (§Gates — the
2026-07-16 session-5 GO is SPENT; its $2.45 ceiling package does not roll over).

## Where everything is

- **V2 (work here):** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`
  — Inspect AI 0.3.246, dedicated `.venv` (`$V2/.venv/bin/{python,inspect}`), package
  `walkworthy_inspect` editable-installed.
- **V1 (READ-ONLY, canonical):** `../Christian-Ethics-Benchmark/`. NEVER write into it
  (even `__pycache__`: set `PYTHONDONTWRITEBYTECODE=1` if executing v1 code). G5 source:
  `harness/walkworthy/` (search "G5" / neutrality); the 20260713 G5 run is at
  `runs/20260713-o5-g5-neutrality/` — read for the certification protocol + thresholds.
- **Pilot substrate (gitignored, do NOT re-run):** `logs/pilot-20260716/<sut>/` — 50
  `.eval` logs + 5 `judgeB-verdicts.jsonl`. Session-5 additions: `logs/f2-ablations-20260716/`
  (anchor-off + answer-blind verdicts, both judges), `logs/f9-microcheck-20260716/`,
  `logs/crossharness-20260716/` (60-item slice × 2 SUTs, judges A+B).
- **Ratified divergence tags:** `banks/20260716-divergence-tags.jsonl` (344 items,
  29 yes / 129 partial / 186 no) — RATIFIED 2026-07-16; usable in headlines WITH the
  calibration caveat (per-design "partial" thresholds vary by tagger: 04=29/33 vs 06=3/31).

## Current state (end of session 5, 2026-07-16; commits `39062ea4a`, `5b24ace3e` on CEI-Lit-WS main — verify origin state at session start, sibling sessions push-cascade this trunk)

- **F9 DONE + LIVE-VALIDATED:** design-05 solver retry drives final non-compliance
  79%/46% → 0/28 on deepseek/mistral; first-pass compliance tracked separately
  (`format_retry_used`); CSR stable on widened coverage (0.907/0.914). Instrument now
  matches v1's one-retry semantics.
- **F2 core DONE** (`20260716-f2-ablations-report.md`): (a) design-07 anchors account
  for only ~5 pts of the 07-vs-02 agreement gap (0.49–0.58 anchored → 0.45–0.50
  without; 02 = 0.22–0.27) — the instrument, not the anchors, drives agreement;
  (b) **anchor-dependence is judge-asymmetric**: answer-blind deltas are large and
  design-directional for judge-A gpt-4.1-nano (design-09 blind floor_compliance
  +0.10…+0.51 — an unanchored nano judge misses floor violations) but small (±0.13)
  for judge-B llama-3.3-70b. This is the empirical driver for F5.
- **F1 DONE + RATIFIED** (`20260716-owner-ruling-f1-and-spend-go.md`): tags +
  divergence-split addendum shipped; the addendum's PROVISIONAL banner is superseded
  by the ruling — the addendum FILE stays immutable, the ruling is the pointer.
- **Cross-harness Option A DONE** (`20260716-crossharness-results.md`): pooled
  per-item agreement A 0.56/0.59, B 0.66/0.66; no consistent harness effect beyond the
  judge-swap band on comparable designs (n=6 cells, insufficient-n); judge-sensitivity
  reproduces across harnesses; **c2 quantified: only 17–19/36 design-07 turn positions
  (and 35–39/46 on 02) received byte-identical stimuli across harnesses** — that
  divergence is the classifier/branch-routing, which is F3's subject. PARALLEL ruling
  unaffected; v1 canonical.
- Optional F2 arm **2c (d02-anchors-on, ~$1.50)** built but UN-FIRED — needs its own GO.
- Tool gotchas (bite anyone extending the audit tools): Inspect `Score.value` rejects
  nested dicts (turn_states is a JSON-encoded string — decode it); ablation/verdict
  JSONLs span SUTs whose sample_ids COLLIDE — always scope joins by log basename
  (`ablation_agreement._sut_log_basenames` is the pattern; a sample_id-only join
  produced identical-cells-across-SUTs garbage on 2026-07-16 before being fixed);
  judge-free metrics have a degenerate judge-swap band (Δjudge=0) — never read
  "outside band" there as a harness/judge effect.

## Read first (in order, skim)

1. `20260716-f2-ablations-report.md` (the judge-asymmetry evidence F5 rests on)
2. `20260716-crossharness-results.md` §"Quantified confounds" (c2 numbers F3 rests on)
3. `REVIEWS/20260716-adjudication-benchmark-critique.md` (R-rules + F-ledger verbatim —
   the authoritative list)
4. `AGENTS.md` (402 max-tokens trap, PF-003 $5 gate, no deletions, v1 read-only)

## Task 1 — F8: parsers.py recovery-path fix (free, small)

The adjudication's F8: the report-side derivation currently covers the recovery-path
defect. Locate the flagged path in `walkworthy_inspect/parsers.py` (see the F8 entry
and CV-5 cluster in the adjudication for the exact defect), fix it at the source,
and prove equivalence: re-run `tools/audit/recompute_design05_csr.py` on
`logs/pilot-20260716` AND `logs/f9-microcheck-20260716` — numbers must be identical to
the shipped reports (any drift = STOP and investigate, do not rationalize). Mock
design05 run as regression. Free.

## Task 2 — F5: G5 neutrality port + judge certification (code free; certification arm gated)

1. Read v1's G5 protocol (source + `runs/20260713-o5-g5-neutrality/`): what it probes
   (matched-quality cross-grounding reference answers; a judge fails certification if
   it penalizes an attested position for its conclusion), thresholds, and which judge
   it disqualified on design 09.
2. Port the certification harness as `tools/audit/judge_certify.py` (offline assembly,
   same monkeypatch-for-ablation philosophy as `tools/audit/judge_ablation.py`; probe
   items must come from v1's G5 set or be design-level constructs — do NOT author new
   bank-adjacent item content, that reopens the ratified 510-item review).
3. Dry-run cost per judge (expect low single dollars; candidates: certify judge-A
   gpt-4.1-nano, judge-B llama-3.3-70b, and 1–2 alternative judge-A candidates, e.g.
   gpt-4.1-mini — note R5 same-family caveat vs the gpt-4.1-mini SUT). THEN STOP —
   certification runs go in the spend memo. The F2 answer-blind evidence predicts
   judge-A fails or barely passes; if so, the memo should include a
   "replacement judge-A certification" line item so one GO covers both.

## Task 3 — F3: 02/07 classifier sensitivity (offline analysis first; small gated live arm)

The branch classifier picks which user turn each SUT receives (M3 recorded
`branch_source` per turn in the pilot logs — classifier vs heuristic). Offline, free:
mine `logs/pilot-20260716` 02/07 ladders for (a) branch_source distribution,
(b) how often the lexical-heuristic fallback fired, (c) re-classify stored prior-turn
responses with the OTHER route (the v1-ported `_heuristic_branch` in
`walkworthy_inspect/solvers.py`) and report the would-have-diverged rate per design ×
SUT — that is the stimulus-instability number the cross-harness c2 finding predicts.
Gated (spend memo): re-classify the same stored responses with 1–2 alternative
classifier MODELS (classifier-tokens only, no SUT re-runs; pattern =
`tools/rescore/rescore.py`) to get cross-family classifier agreement. Deliverable:
dated report; if would-have-diverged > ~15% on 02/07, flag that any future multi-turn
measurement needs a pinned-classifier pre-registration line in F11.

## Task 4 — F11 draft + F4 options memo (both free, owner-decision documents)

1. **F11:** draft `YYYYMMDD-prereg-comparisons-draft.md`: the pre-registered comparison
   list + multiplicity handling for any future comparative v2 claim (which cells, which
   corrections, divergence-split as ratified stratifier, 2-judge rule, pinned classifier
   per Task 3, minimum-n floors per R2). Mark DRAFT — owner ratifies.
2. **F4:** a one-page options memo for the refusal-taxonomy policy call (the 4-way
   cells are unreported per R12; lay out 2–3 concrete policy options with what each
   would unblock, no recommendation-as-decision — this is the owner's call).

## Gates (hard)

- **One consolidated spend memo** at the end of the free work: F5 certification runs
  (per judge, with per-run ceilings) + F3 cross-family classifier arm + (only if owner
  asks) F2-2c. **STOP for explicit owner authorization before ANY paid call** —
  PF-003-style; the session-5 GO ($2.45 ceiling package, ~$0.9–1.5 spent) is closed.
- Availability probe (max_tokens=16) before any authorized run (R10).
- Task order is priority order; if context runs short, F8 + the two memos (Task 4)
  ship first — they are free and unblock owner decisions.

## Standing constraints (hook-enforced + conventions)

- NO deletions ever (`rm` blocked; guard scans whole command strings — don't even
  quote such commands) — `mv` to `RECYCLE-BIN/`. Reports immutable: new `YYYYMMDD-`
  files only; supersede, never edit.
- Shared git trunk: pathspec-commit `COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2`
  only; verify `git status` scope AND origin state at start (siblings push-cascade);
  `git pull --rebase` before any push; don't push unless asked.
- Model tiering: Fable main loop = plan/adjudicate/synthesize; opus = judgment-bearing
  agents; sonnet/haiku = mechanical. Explicit `model` on every Agent dispatch (hook).
- Handoff/session-wrap skills RETIRED — no handoff docs unless owner asks. Auto-memory
  continues (`20260716b-walkworthy-v2-s5-fledger-crossharness.md` is the latest entry).
- Canary `WALKWORTHY-CANARY-7f3e2026` preserved everywhere; holdout (`banks-holdout/`,
  `datasets/holdout/`) never enters prompts, reports, or git; `WALKWORTHY_ALLOW_HOLDOUT`
  stays unset.
- OpenRouter: ALWAYS explicit max-tokens (402 reservation trap); key via
  `source ~/.codex/secrets/openrouter.env`.

## Known open items deliberately OUT of scope (do not pick up unbidden)

F6 DSP judge-prompt credit rule · F7 design-07 prior-turn-context judging (couples to
F3's outcome — sequence after) · F10 seed probe · design-07 floor-saturation item
revisions (v-next bank work, owner call — touches the ratified review) · the
adversarial-parrot probe set (F2's other half; needs authored probe items = construct
work, owner should scope it) · any use of the divergence split as a HEADLINE stratifier
beyond what F11's draft proposes (the ratification allows use; F11 governs how).
