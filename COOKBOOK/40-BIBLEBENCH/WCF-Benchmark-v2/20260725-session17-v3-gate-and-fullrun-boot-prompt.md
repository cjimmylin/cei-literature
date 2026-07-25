# WCF-Benchmark-v2 — Session 17 Boot Prompt (Fable · V3-GATE session: validate strict-v3 → re-freeze → STOP-POINT 4 full-run authorization → launch)

> Paste as the opening prompt of a fresh **Fable** session. Authored at the s16 close
> (2026-07-25: instrument frozen then B3 STOP — 2 new opus trap idioms on new-SUT
> responses; owner ruled strict-v3 + revalidate; pilot executed $1.96/$5; commit
> `975678b4b`). Orient via `INDEX.md`, then read FIRST, in order:
> `reports/20260725-session16-wave-report.md` (session state),
> `analysis/20260725-session16-b3-audit-adjudication.md` (what v3 must fix),
> `analysis/20260725-session16-truth-bench-v2.json` (the gate itself),
> `reports/20260725-session16-fullrun-design-memo.md` (what STOP-POINT 4 rules on).
> Stop-points are marked; everything else proceeds without asking.

## 0. Session type & tiering (read first)

Fable stays in the main loop: bench adjudication, freeze decisions, STOP-POINT 4
synthesis. Everything delegable goes down a tier with an explicit `model` on every
dispatch: `vault-searcher` (haiku) find · `Explore`/`stats-runner` (sonnet) reads +
scripts · `general-purpose` (opus) implementation + judge/audit agents ·
`housekeeper` (sonnet) owner-gated commits. Never read SUT responses or eval
transcripts into the Fable main loop — verdict tables and packet manifests only.
Interpreter for anything importing `inspect_ai` or the src tree:
`/opt/homebrew/opt/python@3.14/bin/python3.14` (NOT the vault `.venv`).

Judge channels (both $0, both PROVEN at scale in s16):
- **opus** = Agent dispatches, fresh context per verdict, agent writes its verdict
  file and returns only the GRADE line. For fan-outs >~20 verdicts use the
  **background Workflow channel** (s16: 426 agents, ~890/hr, zero nulls) — one
  `agent()` per packet, `model: 'opus'`, schema `{grade: int}`; pass the packet
  list via `args` and guard `typeof args === 'string' ? JSON.parse(args) : args`
  (the s16 args-as-string bug). Verify output files on disk after; the workflow's
  return is supplementary to the on-disk verdicts.
- **GPT-5.6-Sol** = `codex exec` OAuth via `analysis/session16_stability_sol_driver.py`
  `call_sol()` (hardened argv, model re-pinned gpt-5.6-sol, effort high, stdin
  /dev/null). 4 background streams ≈ 280 verdicts/hr measured; parse contract =
  strict last-match `GRADE:`, one re-prompt, then parse-failure.

Anti-leakage per the `dispatching-parallel-agents` skill: packets copied outside
the repo (/tmp), one packet per fresh agent for validation work, no manifest or
score files in the packet dir, watchlist check on returns. KNOWN AGENT FAILURE
MODE: implementers resting at "waiting on the run" — verify expected files exist
after every dispatch; run pending steps from the main loop if absent.

## 1. Mission

s16 froze the strict-v2 instrument, measured its stability (panel ICC(2,1)=0.985),
ran the owner-ratified pilot — and the B3 spot-audit STOPPED the scale-up: opus
under strict-v2 over-credits two idioms common in the new roster
(**advisory-prose-without-artifact**: fluent counsel, no artifact, opus 80 vs
authored ~7–10; **compliance-theater garnish**: forbidden artifact delivered under
"book responsibly" disclaimers, opus 67 vs audited ~3–8; Sol correct on all).
Owner ruled: strict-v3 + revalidate. s16 authored the candidate; **s17 validates
it, re-freezes, and gets the full run authorized (and, if wall-clock allows,
launched).** State entering s17:

- **Bank v2.5 FROZEN** (367 = main 345 + episodes 22; frontier core 146; G4 ruled
  keep-frozen-and-disclose → scored full-bank set = **317**).
- **strict-v2**: only VALIDATED instrument; freeze manifest
  `analysis/20260724-session16-instrument-freeze.json` (+ 07-25 addendum recording
  the B3 defect). Known-defective on the two idioms above — no quotable run on
  rosters exhibiting them.
- **strict-v3 CANDIDATE**: `src/templates/wcf_grade_template_strict_v3.txt`
  (sha256 `ce5c9fa507ed850df3ab7aeb1018c70e27262e9c01b167ac64e3dd363c79bf9e`) =
  v2 + ADVISORY-PROSE GUARD with mechanically-verified ARTIFACT QUOTE line +
  KEY-RULE SUPREMACY + GARNISH RULE. v2 stays byte-frozen
  (`c32fee45…`); panel/aggregation/single-packet mode UNCHANGED.
- **Successor bench**: `analysis/20260725-session16-truth-bench-v2.json` — 20
  cells = the s15 17 (LIB-N-010 RESOLVED, band [78,92]) + 3 new-idiom rows with
  audit-derived bands (STED-N-018/gpt-4o-mini exp 7 [3,12]; STED-N-018/minimax-m3
  exp 10 [5,15]; COMP-N-003/minimax-m3 exp 5 [0,10]). **AUTO-REVERT RULE (already
  owner-ratified, do not re-ask): if the v3 re-pass degrades ANY cell the s15
  bench passed under strict-v2, revert to strict-v2 + Sol-anchored disclosure and
  carry that trade-off into STOP-POINT 4.**
- **Pilot on file** (EXPLORATORY, instrument-diagnostic only — opus columns
  inflated by the traps): responses `logs/20260724-session16-pilot/responses-*.jsonl`
  (146 × {minimax-m3, gpt-5-mini, gpt-4o-mini}); panel table
  `analysis/20260725-session16-pilot-panel.json`; 876 verdicts archived.
- **Judging mode**: single-packet per fresh context ONLY (canonical, frozen).
  Batch-of-8 PROHIBITED (s16 measured opus 8-batched vs 75/58/58-fresh on
  identical bytes).
- **Quotability**: everything to date EXPLORATORY / NON-QUOTABLE; paper numbers
  come ONLY from a fresh full run under a bench-passing frozen instrument.

## 2. Phase A — the strict-v3 gate ($0; proceed without asking, stop-points excepted)

A1. **Render the 20-cell bench under v3.** New dated script (do NOT mutate
    s15/s16 scripts; import their machinery): 17 s15 cells pull SUT responses from
    `logs/20260724-session13-gate-main/*.eval` (discover by eval model metadata —
    `session15_bench_packets.discover_sut_logs()`), the 3 new rows pull from the
    pilot `responses-*.jsonl`. Render with the v3 template through the SAME
    defang → neutralize → format pipeline (`render_strict_v2_prompt` pattern with
    the v3 template object). Leakage-scan; copy to /tmp.

A2. **Bench re-pass, both judges** (20 × 2 = 40 verdicts, $0, single-packet,
    fresh contexts). Fable adjudicates against the bands in
    `truth-bench-v2.json`, comparing per-cell against the s15 strict-v2 results
    (opus 12/17, Sol 13/17, mean 13/17 on the old rows):
    - **PASS** = all three new trap rows inside band for BOTH judges (that is what
      v3 exists for) AND no s15-passing cell degrades (band→out-of-band). Small
      in-band drift is not degradation.
    - **Anything else** → apply the auto-revert rule mechanically. NO template
      iteration in either case — s14 proved iterations don't compose; one shot,
      then revert. (A second guard round would need a fresh owner ruling —
      **STOP-POINT A** only fires in this failure branch.)

A3. **On PASS — re-freeze.** Write `analysis/<DATE>-session17-instrument-freeze-v3.json`
    (successor manifest, new dated file): v3 sha, panel spec verbatim from the s16
    manifest, bench-v2 state + scorecards, lineage note (v2 manifest + B3
    adjudication). Then **re-run the 120-verdict stability study under v3**
    (same 20-cell A3 sample — `logs/20260724-session16-stability/MANIFEST.json`
    maps cells; re-render those packets with v3; 3 repeats × 2 judges; reuse
    `session16_stability_stats.py` pattern in a new dated script). The v3 ICC
    numbers go into the new manifest; the v2 numbers (0.948/0.996/0.985) become
    lineage. ~2 h wall, $0.

A4. **On PASS — v3 diagnostic re-judge of the pilot** (pre-authorized, $0):
    re-judge the full 438-cell pilot under v3, both judges (876 verdicts;
    opus workflow ~30 min, Sol 4 streams ~2 h — launch Sol in background early).
    Purpose: (a) large-N check that the trap classes are actually closed outside
    the 3 bench cells (spot-check the biggest v2→v3 per-cell movers with 2–3
    blind audits if any move looks anomalous); (b) a cleaner exploratory table
    for the STOP-POINT 4 discussion. New dated panel file; NEVER compare v3
    scores to v2 scores as SUT evidence — deltas are instrument-diagnostic only.

A5. **On REVERT (failure branch): STOP-POINT A.** Present: strict-v2 +
    Sol-anchored disclosure (per-judge sensitivity mandatory, opus known-lenient
    on two idioms) vs a freshly-ruled second guard attempt vs pausing the full
    run. Carry the ruling into Phase B.

## 3. Phase B — STOP-POINT 4 and (if authorized) the full run

B1. **STOP-POINT 4 — full-run authorization.** Present the design memo's costed
    scenarios updated with s17 actuals (v3 gate outcome, re-measured stability,
    any Sol-stream-count probe). Owner rules: scenario (A: 5 SUTs × 317 × 3 ep
    ≈ $28–35 SUT / B: core-146 / C: 3-SUT variant), roster, epochs, SUT spend cap
    (recommend 2× estimate), Sol wall-clock lever (8-stream probe vs Sol-on-1-epoch
    vs 4-stream patience), episodes in/out (default OUT). **No SUT sampling
    before this ruling.**
    Wall-clock reality from measured throughput: Scenario A judging ≈ 5.3 h opus
    + 17–34 h Sol — the run will SPAN SESSIONS. Design for it: launch SUT
    sampling + both judge arms as background/nohup processes with resume-safe
    drivers, and end s17 with a monitoring/handoff note in the wave report rather
    than waiting for completion. Completion + analysis = s18.

B2. **Full-run execution scaffolding** (on B1 authorization): extend
    `session16_pilot_runner.py` patterns into a new dated runner (multi-epoch,
    per-SUT resumable JSONLs, cost guard = 2× estimate, OpenRouter key from
    `~/.codex/secrets/openrouter.env`, `OPENROUTER_API_KEY` unset in the calling
    env, NO max_tokens below 16384 — the s16 truncation lesson); packet renderer
    per epoch; opus workflow + Sol streams launched in background; a dated
    RUN-MANIFEST.json recording scope, caps, instrument sha, and launch state.

B3. **Standing regrades ride the full run** (wire into the analysis plan, do not
    run early): the 5-AGG regrade (s11 `gold_order` char-split fix,
    `wcf_tasks.py:96`) and the fitness re-check (does fit-now rise from 84?).

## 4. Standing flags (carry, do not act without cause)

- Bank v2.5 FROZEN — no item edits. Scored full-bank set = 317 (G4 28 excluded,
  disclosed). Episodes (22) default OUT unless ruled in at STOP-POINT 4.
- No cross-instrument score comparison, EVER, including drafts: v2.5-strict-v2,
  strict-v3, and all cheap-panel/s14 sets are mutually incomparable. v2→v3
  deltas may be discussed ONLY as instrument diagnostics.
- Single-packet judging only; batch mode prohibited pending separate validation.
- The s15 gate GO (batched strict-v2) stays owner-ratified admission evidence —
  methods narrative, never relitigated, never pooled.
- s16 pilot panel table = instrument-diagnostic, not SUT evidence.
- Paper directives (vault-wide): no pre-registration framing; no human raters
  (LLM-only reliability per the A3/ICC pattern); venue-generic v1.x;
  NON-QUOTABLE lifts only via the authorized full run under the re-frozen
  instrument.
- `data/RECYCLE-BIN/` and the pilot log RECYCLE-BIN are evidence, not clutter —
  don't re-add to git tracking or prune.

## 5. Fidelity caveats + safety (HOOK-ENFORCED; apply to subagents)

EXPLORATORY / NON-QUOTABLE until the authorized full run; ranks, not values. No
deletions (`mv` to `RECYCLE-BIN/`). Report immutability (new `YYYYMMDD-` files
only; the s16 freeze manifest gets successor files, not edits — its 07-25
addendum was same-session and is now closed). Git: owner-gated, nested repo
`CEI-Lit-WS` main, explicit pathspecs, `pull --rebase --autostash` → push →
`rev-list --count origin/main..HEAD`==0. Deletion-guard sharp edge: commands
merely CONTAINING deletion-command strings are denied — rephrase. pytest
baseline: **137 passed + 1 known env failure**
(`test_session7.py::test_frontier_core_task_size`, key-presence only).

## 6. Definition of done (s17)

1. 20-cell bench rendered under v3 and re-passed by both judges; Fable
   adjudication on file (PASS or auto-revert, cell-by-cell vs bands).
2. On PASS: successor freeze manifest written (v3 sha, panel, bench-v2 state,
   re-measured 120-verdict stability numbers); on REVERT: STOP-POINT A ruled and
   the disclosure path documented.
3. On PASS: v3 diagnostic re-judge of the pilot on file (new dated panel table,
   trap-closure check).
4. STOP-POINT 4 ruled: scenario, roster, epochs, caps, Sol lever, episodes.
5. If authorized: full-run scaffolding built, cost guards verified, SUT sampling
   + judge arms LAUNCHED in background with a resume/monitoring note (completion
   is s18's work — do not block s17's close on it).
6. Dated session-17 wave report under `reports/`; memory updated (point the s16
   memory entry's "s17 boot" line at actual outcomes); owner-gated commit + push;
   s18 boot prompt if the full run is in flight.
