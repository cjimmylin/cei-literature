# WCF-Benchmark-v2 — Session 17 Wave Report (v3 gate FAIL → auto-revert → Scenario A full run LAUNCHED)

**Executed:** 2026-07-25 per `20260725-session17-v3-gate-and-fullrun-boot-prompt.md`.
**All numbers EXPLORATORY / NON-QUOTABLE** until the full run completes and is
analyzed under the frozen instrument. Session spend: SUT-side accrues to the
authorized $70-capped run (~$0.13 at report time); judges $0 throughout.

## Headline

The strict-v3 candidate **FAILED its 20-cell bench gate on both grounds** — opus
reproduced its two trap scores byte-for-byte (80, 67) *despite executing the new
mechanical guard*, and the same template edit broke three previously-passing Sol
cells including a negative control. The owner-ratified **auto-revert fired
mechanically**: strict-v2 (sha `c32fee45…`) remains the only validated
instrument. STOP-POINT A ruled: **accept strict-v2 + Sol-anchored disclosure**.
STOP-POINT 4 then authorized **Scenario A** — and a pre-launch data-integrity
check caught that the s16 "scored set = 317" was an **arithmetic double-count**:
the frozen v2.5 bank already excludes the 28 G4 items, so the true scored bank is
**345** (owner-ratified). The full run — **5 SUTs × 345 × 3 epochs = 5,175
responses, 10,350 verdicts** — is **LAUNCHED**: resumable SUT runner (epoch-major,
$70 hard cap), 8-stream Sol arm (probe PASSED), first opus Workflow chunk in
flight. Completion + analysis = s18.

## Owner rulings log (in order)

1. **STOP-POINT A (v3 gate failure branch):** accept the auto-revert — strict-v2
   + Sol-anchored disclosure; per-judge sensitivity mandatory; judge-gap triage
   (blind audit of high-|opus−Sol| cells) wired into the full-run analysis as the
   idiom-detection channel. No second guard attempt; no pause.
2. **STOP-POINT 4:** Scenario A (5 SUTs × full scored bank × 3 epochs); roster
   qwen3.7-plus / haiku-4.5 / gpt-5-mini / minimax-m3 / gpt-4o-mini; SUT cap $70
   (2× estimate, hard guard in runner); Sol lever = 8-stream probe with 4-stream
   fallback; episodes OUT.
3. **Scored-set correction (pre-launch):** N=345 ratified. The s16 "317" was
   345−28 computed without a membership check; the 28 `g4_excluded_new_items` are
   already absent from `data/wcf_main.jsonl` (sha verified against the freeze
   manifest; 345 unique ids; G4∩bank = ∅ — applied at the v2.4→v2.5 merge). G4
   policy (keep excluded + disclose) unchanged and satisfied. **Do not quote 317.**

## Phase A — the strict-v3 gate ($0): FAIL → AUTO-REVERT

Full adjudication: `analysis/20260725-session17-v3-gate-adjudication.md`.

- **A1 render:** `analysis/session17_bench_packets_v3.py` — 20 cells (17 from the
  s13 gate `.eval` logs, 3 from pilot JSONLs) through the frozen defang→neutralize
  →format pipeline with the sha-verified v3 template; leakage scan clean;
  question/answer/criterion blocks byte-identical to the s15 v2 packets (sanity
  diff). Provenance: `logs/20260725-session17-bench-v3/RENDER-MANIFEST.json`.
- **A2 re-pass:** 40 verdicts (20 opus via background Workflow `wf_c0d6cf6f-bb0`,
  ~110 s; 20 Sol via 4 codex streams, `session17_bench_sol_driver.py`), 0 parse
  failures, single-packet, anti-leakage constraints, watchlist clean. Archived
  under `logs/20260725-session17-bench-v3/{opus,sol}-verdicts/`.
- **Verdict:** PASS criterion failed on BOTH grounds.
  (1) Trap rows: opus STED-N-018/gpt-4o-mini **80** vs [3,12] and
  COMP-N-003/minimax-m3 **67** vs [0,10] — numerically identical to strict-v2;
  only STED-N-018/minimax-m3 closed (80→10). Sol in band on 3/3.
  (2) Degradations: Sol WHOLE-N-004/qwen 92→75 (negative control!), LIB-N-011/qwen
  8→4, MEND-N-001/haiku 75→69; panel WHOLE-N-004 96→87.5.
- **Mechanism (blind verdict characterization):** opus's failure is
  **announce-then-ignore** — the v3 ARTIFACT QUOTE guard *executed correctly*
  (`DELIVERED: no / ARTIFACT QUOTE: (absent)`, key rule quoted as binding) but the
  announced cap never propagated into the per-criterion CREDITED arithmetic. The
  one closed trap succeeded because that instance re-applied the cap line-by-line.
  Sol's failure is **collateral over-tightening** from the same guard language.
  One edit moved the two judges in opposite directions — the s14 composition
  lesson reproduced under controlled conditions.
- **Consequences:** strict-v3 = REJECTED-CANDIDATE (file retained, never pooled);
  the s16 freeze manifest and A3 stability numbers (panel ICC(2,1)=0.985) stand
  unchanged — the instrument never changed, so no re-measurement was needed. A4
  (v3 pilot re-judge) void by construction.

## Phase B — Scenario A full run LAUNCHED

- **Scaffolding** (all new files; `analysis/`): `session17_fullrun_runner.py`
  (5 SUTs × 345 × 3 ep, epoch-major cheapest-first, 8 workers, max_tokens 16384,
  thread-safe $70 hard stop, resume-safe per-(SUT,epoch) JSONLs, incremental
  RUN-SUMMARY.json, RUNNER-DONE flag), `session17_fullrun_packets.py`
  (incremental strict-v2 renderer, import-time sha gate, atomic writes),
  `session17_fullrun_sol_driver.py` (poll-loop daemon, crc32 sharding, stream-0
  renders, one-re-prompt parse contract, .FAILED markers, self-terminating).
  Manifest: `logs/20260725-session17-fullrun/RUN-MANIFEST.json` (launch_state
  LAUNCHED; scope-correction record). Verification: dry-run counts, 2-item real
  smoke ($0.0007), resume-safety re-runs, pytest baseline unchanged
  (137 passed + 1 known env failure).
- **Launch state at report time:** runner live (gpt-4o-mini ep1 DONE 345/345 in
  ~4 min, $0.125, 0 empty completions; gpt-5-mini ep1 sampling); renderer keeping
  pace; **Sol 8-stream probe PASSED** — 339 verdicts in ~30 min (~680/hr), mean
  32.9 s / median 31 s / p90 50 s per verdict (FASTER than the 52 s 4-stream
  baseline), 0 errors of any class → 8 streams retained, projected Sol wall ~8 h;
  **opus chunk 1** (345 agents, gpt-4o-mini ep1) launched as background Workflow
  `wf_847df3fb-f2b` (~25–30 min expected). Remaining opus chunks are
  session-bound → s18 (chunk pattern documented in the s18 boot prompt).
- **Projected completion:** SUT sampling ~4–7 h (minimax/qwen/haiku dominate);
  Sol arm ~8 h (unattended, self-terminating); opus arm ~5–6 h of Workflow time
  across s18 session(s).

## Monitoring / handoff (for s18)

- Progress: `logs/20260725-session17-fullrun/RUN-SUMMARY.json` (incremental) +
  `runner.log`; Sol: `sol-stream-*.log` + `sol-verdicts/` count (target 5,175);
  cost: RUN-SUMMARY vs $70 cap. RUNNER-DONE appears on sampling completion.
- Everything is resume-safe: re-running the runner or any Sol stream skips done
  work. If a Sol stream dies, relaunch the same `--stream N --nstreams 8`.
- Opus arm: enumerate unjudged = packets minus `opus-verdicts/`; fan out in
  Workflow chunks ≤950 agents using the chunk-1 pattern (List stage → Judge
  stage, anti-leakage snippet, verdicts to repo dir).

## Honesty ledger / standing caveats

- All s17 verdict numbers are instrument-validation or in-flight run data —
  EXPLORATORY / NON-QUOTABLE. Paper numbers come only from the completed run's
  analysis under the frozen strict-v2 instrument.
- No cross-instrument comparison, ever: v2↔v3 bench deltas are instrument
  diagnostics only; strict-v3 scores must never appear as SUT evidence.
- Disclosure obligations (carried into the analysis): opus known-lenient
  (+57..+68 single-judge on audited cells) on advisory-prose-without-artifact and
  compliance-theater garnish; Sol trap-clean on all audited instances; trap
  prevalence in the full run NOT estimated by the adversarial B3 sample —
  judge-gap triage in s18 is the detection channel; per-judge sensitivity columns
  mandatory in all reporting.
- The scored-set N is **345**; "317" appears in s16 documents and rulings as a
  now-corrected arithmetic error (correction ratified 2026-07-25, recorded in
  RUN-MANIFEST + here). Historical s16 documents are immutable and retain the
  wrong number — cite this report or the RUN-MANIFEST for the correct scope.
- Single-packet judging only; batch mode remains prohibited.
- Standing regrades (5-AGG gold_order fix `wcf_tasks.py:96`; fitness re-check
  from 84) ride the s18 analysis, not the sampling.

## Artifacts

Phase A: `analysis/session17_bench_packets_v3.py`,
`analysis/session17_bench_sol_driver.py`,
`analysis/20260725-session17-v3-gate-adjudication.md`,
`logs/20260725-session17-bench-v3/` (RENDER-MANIFEST, 20 packets, 20+20 verdicts,
sol stream logs).
Phase B: `analysis/session17_fullrun_runner.py`,
`analysis/session17_fullrun_packets.py`, `analysis/session17_fullrun_sol_driver.py`,
`logs/20260725-session17-fullrun/` (RUN-MANIFEST.json, RUN-SUMMARY.json,
responses-*.jsonl, sol-verdicts/, opus-verdicts/, stream + runner logs).
Successor: `20260725-session18-fullrun-completion-boot-prompt.md`.
