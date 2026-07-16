# BOOT PROMPT — WALKWORTHY v2: F-ledger tops (F9 / F2 / F1) + v1↔v2 cross-harness design

Paste/read this at the start of a fresh session. It is self-contained.

## Mission

Work the top of the post-pilot FIX-later ledger, in order: **F9** (design-05 format
retry — unlocks CSR coverage), **F2** (anchor + answer-blind judge ablations — mostly
offline over existing pilot logs), **F1** (divergence tagging — release-blocking for any
"Christian ethics" headline), then write the **v1↔v2 cross-harness comparison design
memo** the PARALLEL ruling anticipates. Free/offline work executes; **every paid call
waits behind one consolidated owner spend gate** (§Gates below — the 2026-07-16 $7.90
pilot authorization is SPENT AND EXPIRED; nothing rolls over).

## Where everything is

- **V2 (work here):** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`
  — Inspect AI 0.3.246, dedicated `.venv` (`$V2/.venv/bin/{python,inspect}`), package
  `walkworthy_inspect` editable-installed.
- **V1 (READ-ONLY, canonical):** `../Christian-Ethics-Benchmark/`. NEVER modify — note
  for cross-harness work: running v1's harness writes into v1's own runs/ tree, which
  read-only forbids; any v1 execution must redirect outputs into the v2 folder or the
  design memo must flag the conflict for the owner.
- **Books (ground truth):** `../Christian-Ethics-Books/` (15 registry works; L8/L9 rules).
- **Pilot substrate (on disk, gitignored):** `logs/pilot-20260716/<sut>/` — 50 `.eval`
  logs (563 samples × 5 SUTs) + 5 `judgeB-verdicts.jsonl`. This is the raw material for
  F2 and the divergence-split re-reporting; do NOT re-run the pilot.

## Current state (as of 2026-07-16 end of session 4; commits `513924d5c`, `4ea6de875`, `00cec2b28` on CEI-Lit-WS local main, NOT pushed)

- **PARALLEL — RULED, do not re-litigate** (`20260716-owner-ruling-v2-parallel.md`): v2
  is a comparison instrument; v1 stays canonical for release evidence.
- **Five-lens adversarial critique DONE and adjudicated**
  (`REVIEWS/20260716-adjudication-benchmark-critique.md`): M1–M4 code fixes landed;
  R1–R12 reporting rules are STANDING (no rankings; joint companions; stratum-c
  quarantine; recompute-only headlines; refusal cells omitted — owner ratified). Do NOT
  redo the critique, the 510-item copyedit review, or the adjudication.
- **Full 5-SUT pilot EXECUTED** (`20260716-pilot-report.md`): 50/50 success, ≈$3.63
  spent. Headline: **all 9 comparable designs flip SUT ordering under judge-B** →
  2-judge is mandatory in any future v2 measurement; 02/09 most fragile (per-turn A/B
  0.21–0.26 / field 0.36–0.51). Design-07 floor-saturated (arc_pass 0.0, all SUTs, 0
  exclusions). Design-03's say_do_gap collapses to ≈0 under judge-B (judge-carried).
- **Design-05 alloc-spec bug FIXED** (scorers.py + tools/rescore/rescore.py now read
  `keyed.extras.allocation`); true CSR recovered offline
  (`tools/audit/recompute_design05_csr.py`: 0.84–0.94 on decidable items). The LIVE
  residual is format compliance: **46–79% of items per SUT never emit a parseable
  allocation block** — that is what F9 fixes.
- **Design-07 harness anchors AUTHORED** (`scorers._DESIGN07_STATE_ANCHORS`,
  `20260716-design07-reference-anchors-report.md`): first live reading 07 per-turn A/B
  agreement 0.48–0.56 vs anchor-less 02 at 0.21–0.26 — suggestive, unattributed. F2
  provides the clean attribution.
- New tools: `tools/audit/pilot_judge_swap.py` (judge-swap/ordering-flip analysis;
  gotcha: Inspect `Score.value` rejects nested dicts — sanitize `_judge_meta`),
  per-turn 02/07 support in `tools/rescore/rescore.py`, Wilson CIs + per-stratum cells
  in `tools/audit/recompute_metrics.py`.

## Read first (in order, skim)

1. `20260716-pilot-report.md` (esp. §2 judge-sensitivity, §6 instrument diagnostics)
2. `REVIEWS/20260716-adjudication-benchmark-critique.md` (R-rules + F-ledger — the
   authoritative list; F3–F8, F10–F11 are OUT of this session's scope unless owner asks)
3. `20260716-design07-reference-anchors-report.md` (owner gate record + anchors)
4. `AGENTS.md` (402 max-tokens trap, no sampling params to Opus4.7+/Fable, PF-003 $5
   gate, no deletions, v1 read-only)

## Task 1 — F9: design-05 solver-level format retry (code first, then gated micro-check)

The unused `_FORMAT_REMINDER` string exists in the package (CV-5 finding). Implement the
v1-spirit one-retry rule at the SOLVER level for design 05: if the response yields no
parseable allocation block (use the FIXED alloc-spec path), append the format reminder
as a follow-up user turn and regenerate ONCE; record `format_retry_used` (and whether
the retry parsed) in sample metadata/store so coverage accounting can separate
first-pass vs retry compliance. Genuine refusal-to-allocate must remain a signal — a
retry that still fails parses as non-compliant, never as an error. Verify: mock
(design05, mockllm) + offline re-parse unit sanity. THEN STOP: the live micro-check
(design05 × 1–2 SUTs, `--limit` acceptable here since 05 is unpaired; ≈$0.10–0.25) goes
in the consolidated spend memo, not fired on its own.

## Task 2 — F2: judge ablations over EXISTING pilot logs (judge-tokens only)

Two ablations, both re-judging stored responses (no SUT calls — pattern:
`tools/rescore/rescore.py`):

1. **Anchor ablation (design 07):** re-judge the stored 07 per-turn responses WITHOUT
   `_DESIGN07_STATE_ANCHORS` (and optionally design 02 WITH a generically-adapted
   anchor block as the reverse arm), judges A and B. Deliverable: per-turn A/B agreement
   with-vs-without anchors → clean attribution of the 0.48-vs-0.22 story.
2. **Answer-blind ablation (JV-2, designs 03/06/09 sample):** re-judge a fixed sample
   with the keyed anchor REMOVED from the judge prompt; measure the leniency delta
   (anchor-visible vs anchor-blind scores).

Build these as new `tools/audit/` scripts (dated report of results; never overwrite the
pilot report). Estimate judge-token cost per arm in the spend memo (expect low single
dollars total; per-turn 07 = 163 turns × 5 SUTs per judge per arm). STOP before firing.

## Task 3 — F1: divergence tagging (agents, no API spend) + divergence-split re-report

Tag every public runnable item: does the corpus-keyed answer DIVERGE from the modal
secular/RLHF-consensus answer? (`divergence: yes | partial | no` + one-line rationale.)
Method: Claude Code Agent dispatches (vault rule: Agents over API; opus tier for
judgment, explicit `model` on every dispatch), disjoint per-design assignments,
refute-first framing ("assume NO divergence unless the keyed anchor requires something a
well-RLHF'd secular model would not do"). Output: a NEW sidecar file (e.g.
`banks/20260716-divergence-tags.jsonl` or next date) — do NOT edit the ratified bank
item files. Then re-emit the pilot per-design cells split by divergence flag (offline,
free, from `logs/pilot-20260716/`) as a dated addendum report. Expected shape per CV-1:
only 04/05/10 + scattered items elsewhere carry divergence — the split table is what
makes any future "Christian ethics" claim honest. Surface the tag distribution to the
owner before treating it as settled (it is a construct-defining artifact).

## Task 4 — v1↔v2 cross-harness comparison DESIGN MEMO (no execution)

Write `20260716-crossharness-design.md` (or next date): proposed comparison of the same
SUT × item slice run through BOTH harnesses (candidate: MVP-A1 60-item slice, 1–2 SUTs
from the pilot panel), same judge pair; what agreement statistic decides "the harnesses
measure the same thing" (per-item score agreement, per-design cell deltas vs the
judge-swap noise band from the pilot — a cross-harness delta smaller than the judge-swap
band is indistinguishable from judge noise); the v1 read-only execution problem (v1
harness writes runs/ into the v1 folder — propose output redirection or an owner
exception); cost math; claims scope (descriptive; feeds a future canonical-ruling
evidence base but does NOT reopen the PARALLEL ruling). END AT THE GATE.

## Gates (hard)

- **One consolidated spend memo** at the end of the free work: F9 micro-check + F2
  ablation arms + (if owner wants it now) cross-harness run, each with cost math and a
  per-run ceiling. **STOP for explicit owner authorization before ANY paid call** —
  PF-003-style; the pilot's $7.90 authorization is spent and does not roll over.
- F1 tag distribution → owner review before use in any headline.
- Task order is the priority order; if context runs short, ship F9 code + the spend
  memo first.

## Standing constraints (hook-enforced + conventions)

- NO deletions ever (`rm` blocked; deletion-guard scans whole command strings — don't
  even quote such commands) — `mv` to `RECYCLE-BIN/`. Reports immutable: new `YYYYMMDD-`
  files only; supersede, never edit, prior dated reports.
- Shared git trunk: pathspec-commit `COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2`
  only; verify `git status` scope; local main ahead of origin — `git pull --rebase`
  before any push (and don't push unless asked).
- Model tiering: Fable main loop = plan/adjudicate/synthesize; opus = judgment-bearing
  agents; sonnet/haiku = mechanical. Explicit `model` on every Agent dispatch (hook).
- Handoff/session-wrap skills RETIRED (2026-07-15) — no handoff docs unless owner asks.
  Cross-session auto-memory continues (`20260716-walkworthy-v2-critique-and-pilot.md`
  is the latest entry).
- Canary `WALKWORTHY-CANARY-7f3e2026` preserved everywhere; holdout
  (`banks-holdout/`, `datasets/holdout/`) never enters prompts, reports, or git;
  `WALKWORTHY_ALLOW_HOLDOUT` stays unset.
- OpenRouter: ALWAYS explicit max-tokens (402 reservation trap); key via
  `source ~/.codex/secrets/openrouter.env`; availability probe before any paid design run.

## Known open items deliberately OUT of scope (do not pick up unbidden)

F3 cross-family classifier sensitivity · F4 refusal-taxonomy policy (needs an owner
policy call) · F5 G5 neutrality port + judge certification · F6 DSP judge-prompt credit
rule · F7 design-07 prior-turn-context judging · F8 parser recovery-path fix (report-side
derivation covers current use) · F10 seed probe · F11 multiplicity pre-registration ·
design-07 floor-saturation item revisions (v-next bank work — touches the ratified
review, owner call).
