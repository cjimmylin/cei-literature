# WCF-Benchmark-v2 — Session 16 Boot Prompt (Fable · PILOT-READINESS session: freeze instrument → pilot → scale plan)

> Paste as the opening prompt of a fresh **Fable** session. Authored at the s15 close
> (2026-07-24: Phase-4 gate GO 70/80 owner-ratified; bank v2.4 → **v2.5**, 367 items;
> strong panel adopted, cheap panel retired for admissions; tranche CLOSED; commit
> `ac6bee576`). Orient via `INDEX.md`, then read the s15 wave report
> (`reports/20260724-session15-wave-report.md`) FIRST, then the bench + Arm-B files
> (`analysis/20260724-session15-truth-bench.json`,
> `…-armB-opus-verdicts.md`, `…-armB-sol-verdicts-and-aggregation.md`).
> Stop-points are marked; everything else proceeds without asking.

## 0. Session type & tiering (read first)

Fable stays in the main loop: rulings adjudication, bench verdicts, freeze decisions,
pilot design, synthesis. Everything delegable goes down a tier with an explicit
`model` on every dispatch: `vault-searcher` (haiku) find · `Explore`/`stats-runner`
(sonnet) reads + scripts · `general-purpose` (opus) implementation, blind audits,
judge agents · `housekeeper` (sonnet) owner-gated commits. Never read eval
transcripts or SUT responses into the Fable main loop — verdict tables and packet
manifests only. KNOWN AGENT FAILURE MODE (hit in s14, mitigated since): implementers
resting at "waiting on the live run" — after every dispatch verify expected output
files exist on disk; if absent, run the pending step from the main loop (interpreter:
`/opt/homebrew/opt/python@3.14/bin/python3.14`, NOT the vault `.venv`). Judge
channels: opus = Agent dispatches ($0); GPT-5.6-Sol = `codex exec` OAuth ($0,
default model per `~/.codex/config.toml`, recipe: stdin-piped prompt, `--sandbox
read-only`, `--output-last-message`, ~2 min/verdict, 4 parallel background streams
proven). Anti-leakage discipline per the `dispatching-parallel-agents` skill: blind
packets copied outside the repo, one-packet-per-fresh-agent for validation work
(SUT-pure batches of 8 acceptable for production judging), watchlist check on
returns.

## 1. Mission

s15 finished the admission question. s16 begins the PAPER question: freeze the
measurement instrument, run a pilot that produces the three numbers the full run
depends on (throughput, cross-SUT validity, judge stability), and leave a costed,
owner-ratified full-run design. State entering s16:

- **Bank v2.5 FROZEN:** 367 items (main 345 = v1 199 / s6 29 / s7 37 / s12 17 /
  s13 63; episodes 22); frontier `-N-` core 146
  (`analysis/20260724-session13-frontier-core-index.json`); G4-excluded 28
  (cheap-panel-era derivation, policy question below).
- **Instrument (candidate-frozen):** strict-v2 template
  (`src/templates/wcf_grade_template_strict_v2.txt`) + strong panel = mean-of-2
  Claude-Opus + GPT-5.6-Sol. Validated on the 17-cell truth bench: 0 categorical
  errors both judges; residuals OPEN — Sol strict on 2 negative controls (−19,
  half-credits with satisfying quotes and no rationale), opus lenient (+4..+9),
  LIB-N-010 row CONTESTED, single-judge repeat-cell variance ±10–40
  (LIB-N-006 92↔83, WHOLE-N-003 4↔42 on identical packets).
- **Quotability rule:** every number to date is EXPLORATORY / NON-QUOTABLE. Paper
  numbers come ONLY from a fresh full run under the frozen instrument; s6–s15
  becomes methods narrative (instrument development + truth-bench validation),
  never results.

## 2. Phase A — settle and freeze the instrument ($0; proceed without asking, stop-points excepted)

A1. **LIB-N-010 decisive re-audit.** Dispatch a FRESH blind meta-auditor (opus; no
    access to the s14 audit, the bench, or the two strong-judge verdicts) against
    the full SUT response + item key: is the artifact-compactness deduction real
    (band 78–92) or not (band extends to 100)? Fable adjudicates auditor-vs-audit;
    the bench row's CONTESTED status resolves either way. Update
    `analysis/20260724-session15-truth-bench.json` (new dated successor file if the
    band changes — report immutability).

A2. **STOP-POINT 1 — residual doctrine: freeze as-is, or one guard round?**
    Present to owner: (a) FREEZE the instrument now with residuals disclosed
    (default recommendation — s14 proved prompt iterations don't compose; the
    residuals are metric, opposed in direction, and partially cancel in the mean),
    or (b) authorize exactly ONE anti-strictness guard round (require articulated
    rationale for any half-credit) with a mandatory full 17-cell bench re-pass and
    a hard rule: if the re-pass degrades ANY currently-passing cell, revert and
    freeze the s15 template. No further iterations either way. **After this ruling
    the instrument is FROZEN: template + panel + mean-of-2 + packet pipeline. Any
    later edit is a NEW instrument (bank-versioning rule extended to judge-mode)
    and restarts validation.**

A3. **Judge stability measurement** (replaces the caveat with a statistic).
    Stratified 20-cell sample (refusal floors, negative controls, partial-credit
    band cells, high deliveries — reuse bench cells + ~6 non-bench cells from the
    s13 logs) × 3 repeats × both judges = 120 verdicts, $0, blind, fresh context
    per verdict. stats-runner computes per-judge and panel-mean test–retest
    (SD of repeats per cell; ICC(2,1)-style summary acceptable — no human raters,
    LLM-only, per vault directive). This is the paper's instrument-reliability
    number. Deliverable: dated analysis file with the full repeat matrix.

A4. **Freeze manifest.** After A2's ruling and A3's numbers: write
    `analysis/20260724-session16-instrument-freeze.json` — template sha256, panel
    spec, aggregation rule, bench file + pass/fail state, stability numbers,
    residual disclosures. This is the paper's methods anchor.

## 3. Phase B — pilot (SPEND-GATED; design proceeds, execution waits on stop-points)

B1. **STOP-POINT 2 — pilot scope + SUT roster + spend cap.** Present a concrete
    pilot design for ruling: recommended shape = 2–3 SUTs × the 146-item frontier
    core × 1 epoch, temp per s7 harness defaults, fresh SUT sampling via OpenRouter
    (key at `~/.codex/secrets/openrouter.env`; run scripts with `OPENROUTER_API_KEY`
    unset in the calling env — the env-truncation gotcha; cost guards + resumable
    runner mandatory, mirror `analysis/session14_calibration.py` patterns).
    Estimated SUT cost ~$1–3; judges $0. Owner picks: roster (candidates: the s7
    full-bank set incl. minimax-m3; at minimum one frontier + one mid + one weak for
    spread), items (frontier core vs full main bank), epochs, and the cap. **No SUT
    sampling before this ruling.**
- B2. **Pilot execution** (on B1 authorization): sample SUTs → build packets with the
    frozen pipeline (`analysis/session15_gate_packets.py` generalizes; new dated
    script, don't mutate s15's) → judge with the frozen panel (opus Agent fan-out,
    SUT-pure batches ≤8; Sol 4-stream background) → measure ACTUAL throughput
    (verdicts/hour/stream) and cost.

B3. **Cross-SUT validity spot-audit** (folds into B2, $0): blind-audit ~10 pilot
    cells from the NEW SUTs (stratify: refusals, preambled deliveries, substitutes)
    — the bench validated the panel on qwen/haiku idioms only; confirm no new trap
    class (novel refusal styles, new substitute shapes) before scaling. Fable
    adjudicates; any new failure mode is a STOP (back to A2's successor instrument,
    new validation).

B4. **Standing flags that RIDE the full eval — carry into the design, do not drop:**
    the 5-AGG regrade (s11 gold_order char-split fix, `wcf_tasks.py:96`) and the
    fitness re-check (does fit-now rise from 84?) both execute at the full run, not
    the pilot. **STOP-POINT 3 — G4 policy:** the 28 exclusions are cheap-panel-era;
    owner rules keep-frozen-and-disclose (cheap, default) vs re-derive under the
    strong panel (cleaner, costs a saturation pass).

B5. **Full-run design memo** (the session's synthesis deliverable): from pilot
    actuals — SUT roster × 367 (or ruled scope) × epochs (s7 precedent ×3 for
    significance), judge wall-clock plan (the bottleneck: Sol ~2 min/verdict —
    present measured options: more streams / Sol on 1 epoch + opus all / paid API
    judge with cap), SUT + judge cost table, analysis plan per s7/s8 precedent
    (paired significance over epochs, per-mold + frontier-core breakdowns,
    panel-mean with per-judge sensitivity). Ends with **STOP-POINT 4 — full-run
    authorization** (roster, epochs, caps): expected to be ruled in s17, not s16,
    unless the owner rules early.

## 4. Standing flags (carry, do not act without cause)

- Bank v2.5 FROZEN — no item edits of any kind. Episodes (22) default OUT of paper
  scope unless the owner rules them in at B1.
- No cross-instrument score comparison, ever: v2.5-strong-panel scores vs any prior
  set (s6/s7/s12/s13 cheap-panel, s14 strict-v1) — including in paper drafts.
- s12/s13 gate history: two NO-GOs were instrument artifacts (s15 finding) —
  background for the methods section; NOT a license to rescore or reinterpret old
  reports (report immutability).
- Frozen-17 single-run instability (11/17) remains on file; the A3 stability study
  is the constructive answer — do not relitigate the retired gate criterion.
- Paper directives (vault-wide): no pre-registration framing; no human raters
  (LLM-triangulation disclosure pattern); venue-generic v1.x; NON-QUOTABLE lifts
  only via the fresh frozen-instrument full run.
- `data/RECYCLE-BIN/` is gitignored — the superseded v2.4 manifest lives on disk
  only (recoverable from git history); don't re-add.

## 5. Fidelity caveats + safety (HOOK-ENFORCED; apply to subagents)

EXPLORATORY / NON-QUOTABLE until the full run; ranks, not values. No deletions
(`mv` to `RECYCLE-BIN/`). Report immutability (new `YYYYMMDD-` files only). Git:
owner-gated, nested repo `CEI-Lit-WS` main, explicit pathspecs,
`pull --rebase --autostash` → push → `rev-list --count origin/main..HEAD`==0.
Deletion-guard sharp edge: commands merely CONTAINING deletion-command strings are
denied — rephrase. pytest baseline: 137 passed + 1 known env failure
(`test_session7.py::test_frontier_core_task_size`, key-presence, count already
corrected to 146).

## 6. Definition of done (s16)

1. LIB-N-010 resolved; bench fully settled.
2. STOP-POINT 1 ruled; instrument FROZEN; freeze manifest written (template sha,
   panel, aggregation, bench state, A3 stability numbers, residual disclosures).
3. Judge-stability statistic measured and on file (120-verdict repeat matrix).
4. STOP-POINT 2 ruled; pilot executed within cap; actual throughput + cost measured.
5. Cross-SUT spot-audit adjudicated clean (or STOP escalated).
6. STOP-POINT 3 (G4 policy) ruled; 5-AGG regrade + fitness re-check wired into the
   full-run design.
7. Full-run design memo written, ending at STOP-POINT 4 (full-run authorization,
   expected s17).
8. Dated session-16 wave report under `reports/`; memory updated; owner-gated
   commit + push.
