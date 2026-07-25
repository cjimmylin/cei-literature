# WCF-Benchmark-v2 — Session 18 Boot Prompt (Fable · FULL-RUN COMPLETION: finish opus arm → aggregate → analyze → paper numbers)

> Paste as the opening prompt of a fresh **Fable** session. Authored at the s17
> close (2026-07-25: strict-v3 gate FAILED both grounds → auto-revert ratified;
> STOP-POINT 4 ruled Scenario A; scored-set N corrected 317→**345**; run
> LAUNCHED — SUT sampling + 8-stream Sol arm + opus chunk 1 all in flight at
> close). Orient via `INDEX.md`, then read FIRST, in order:
> `reports/20260725-session17-wave-report.md` (session state + rulings),
> `logs/20260725-session17-fullrun/RUN-MANIFEST.json` (scope, caps, instrument,
> disclosure obligations), `analysis/20260725-session17-v3-gate-adjudication.md`
> (why strict-v2 + Sol-anchored disclosure), then check live run state (§1).
> No stop-points are pre-planned; STOP only on cap breach, instrument anomaly, or
> before git push (owner-gated).

## 0. Session type & tiering

Fable main loop: run-state adjudication, judge-gap triage rulings, analysis
design, final synthesis. Delegate down-tier with explicit `model` on every
dispatch. Never read SUT responses or eval transcripts into the main loop —
verdict tables, manifests, and aggregate CSVs only. Interpreter for anything
importing `inspect_ai` or src/: `/opt/homebrew/opt/python@3.14/bin/python3.14`.
Anti-leakage per the `dispatching-parallel-agents` skill for ALL judge fan-outs
(fresh context, one packet per agent, /tmp packets, watchlist on returns).

## 1. First act — assess the overnight run

```
cd CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/logs/20260725-session17-fullrun
cat RUN-SUMMARY.json          # per-(SUT,epoch) counts/costs; cap_hit must be false
ls RUNNER-DONE 2>/dev/null    # present iff sampling complete (5,175 = 345×5×3)
ls sol-verdicts/*.md | wc -l  # target 5,175; *.FAILED marks exhausted retries
tail sol-stream-*.log         # streams self-terminate when done
ls opus-verdicts/*.md | wc -l # 345 expected from s17 chunk 1 (gpt-4o-mini ep1)
```

Recovery (all resume-safe, same commands as s17):
- Runner incomplete/dead → relaunch `nohup python3.14
  analysis/session17_fullrun_runner.py --expect-count 345 > …/runner.log &`.
- Sol stream dead → relaunch that `--stream N --nstreams 8`. If sol-verdicts has
  gaps after streams exited, re-launch all 8 (they skip done work and exit).
- Packets are /tmp-resident and REGENERABLE: `python3.14
  analysis/session17_fullrun_packets.py` re-renders any missing (deterministic,
  sha-gated strict-v2).
- `.FAILED` markers: retry by removing nothing — mv the marker to RECYCLE-BIN and
  let a Sol stream retry, or judge those cells via a small dedicated dispatch.

## 2. Opus arm — finish the ~4,830 remaining verdicts

Workflow chunks are session-bound; s17 completed chunk 1 (gpt-4o-mini ep1, 345).
Pattern (PROVEN s16 ~890/hr, s17 chunk 1): background Workflow, List stage (one
sonnet agent: `ls` packets for the chunk minus existing `opus-verdicts/` entries)
→ Judge stage (one fresh opus agent per packet, `model: 'opus'`, schema
`{grade:int}`, single-packet, the anti-leakage snippet verbatim, agent writes
verdict to `logs/20260725-session17-fullrun/opus-verdicts/<name>.md` and returns
the grade). Script reference: the s17 chunk-1 workflow in the session-17
transcript workflows dir; ~14 chunks of one SUT-epoch each (345 ≤ 950 cap) or
pair them (690/chunk, 7-8 workflows). ~25-30 min per 345-agent chunk; run 2-3
sequentially per sitting, verify on-disk verdict counts after each (workflow
return is supplementary to disk). Total ~5-6 h of Workflow wall — plan the
session accordingly; chunks can interleave with §3-§4 work.

## 3. Aggregation (new dated script, extend `session16_pilot_stats.py` patterns)

- Parse ALL verdicts (strict last-match `GRADE:`), join opus + Sol per
  (item, SUT, epoch) cell → panel mean-of-2; per-judge columns retained.
- Integrity gates before ANY analysis: 5,175 cells × 2 judges, 0 unparsed (or an
  explicit disclosed list); per-file counts match RUN-SUMMARY; empty-completion
  cells floor as data, not errors. Verify unique counts against source data (the
  s16 "317" double-count is the standing cautionary tale — N=345, never 317).
- Output: dated panel JSON + per-judge CSVs under `analysis/` +
  `logs/20260725-session17-fullrun/`.

## 4. Analysis plan (paper numbers — this lifts NON-QUOTABLE, per design memo §4)

1. Headline: per-SUT panel means with per-judge sensitivity columns; paired-epoch
   significance (s7 precedent); per-mold + frontier-core breakdowns.
2. **Judge-gap triage (MANDATORY, from STOP-POINT A):** rank cells by
   |opus − Sol|; blind-audit a stratified sample of the top gaps (fresh opus
   auditors, raw-materials packets, /tmp isolation — the B3 pattern) to detect
   advisory-prose / garnish idiom cells; report idiom prevalence and a
   Sol-anchored sensitivity read for affected cells. Opus is known-lenient
   (+57..+68 single-judge on audited cells) on these two idioms.
3. Instrument-reliability: quote the s16 A3 numbers (panel ICC(2,1)=0.985 —
   instrument unchanged by the v3 episode).
4. Standing regrades: 5-AGG gold_order regrade (`wcf_tasks.py:96` char-split
   fix); fitness re-check (does fit-now rise from 84?).
5. Epoch stability: WALKWORTHY lesson — single-epoch verdicts unreliable; report
   3-epoch consistency explicitly.
6. Disclosures: strict-v3 rejected-candidate episode (announce-then-ignore
   diagnosis); G4 derivation + N=345 correction; opposed judge residuals; batch
   prohibition; per-judge columns everywhere. NO cross-instrument comparison
   anywhere, including drafts.

## 5. Standing flags (carry)

- Bank v2.5 FROZEN; scored bank = **345** (28 G4 already absent from the bank;
  "317" is a corrected error — do not quote it); episodes (22) OUT.
- strict-v2 sha `c32fee45…` is THE instrument; strict-v3 is REJECTED-CANDIDATE
  (never pooled, never compared as SUT evidence). Freeze manifest + A3 stability
  stand unchanged.
- Single-packet judging only; batch prohibited. Judge channels $0 only (Agent /
  Workflow for opus; codex OAuth for Sol) — no API-key judge pipelines.
- $70 SUT hard cap governs the runner; judges $0.
- Paper directives: no pre-registration framing; no human raters; venue-generic
  v1.x; ranks-not-values until the analysis under the frozen instrument is done.
- `data/RECYCLE-BIN/` + pilot/fullrun RECYCLE-BINs are evidence — don't prune.

## 6. Safety (HOOK-ENFORCED; applies to subagents)

No deletions (`mv` to `RECYCLE-BIN/`). Report immutability (new `YYYYMMDD-`
files; RUN-MANIFEST.json launch/status fields are the designed exception).
Git owner-gated: nested repo `CEI-Lit-WS`, explicit pathspecs,
`pull --rebase --autostash` → push → `rev-list --count origin/main..HEAD`==0.
Deletion-guard sharp edge: commands merely containing deletion-command strings
are denied — rephrase. pytest baseline: 137 passed + 1 known env failure.

## 7. Definition of done (s18)

1. Run complete: 5,175 responses + 10,350 verdicts on disk (or gaps explicitly
   adjudicated and disclosed); costs vs cap recorded.
2. Aggregation with integrity gates; dated panel table.
3. Judge-gap triage executed and adjudicated (Fable rules on audited cells).
4. Analysis per §4; dated results report under `reports/` — the first QUOTABLE
   numbers of the project, clearly marked as such.
5. Wave report; memory updated (s17 entry → outcomes); owner-gated commit+push;
   s19 boot prompt (paper drafting) if warranted.
