# WCF-Benchmark-v2 — Session 18 Boot Prompt (Fable · run COMPLETE → finish judging → aggregate → triage → first QUOTABLE analysis)

> Paste as the opening prompt of a fresh **Fable** session. Authored 2026-07-26 —
> **SUPERSEDES `20260725-session18-fullrun-completion-boot-prompt.md`** (written
> mid-launch; this version reflects the verified post-completion state). Orient via
> `INDEX.md`, then read: `reports/20260725-session17-wave-report.md` (rulings +
> launch), `logs/20260725-session17-fullrun/RUN-MANIFEST.json` (scope, instrument,
> disclosure obligations), `analysis/20260725-session17-v3-gate-adjudication.md`
> (why strict-v2 + Sol-anchored disclosure). No stop-points pre-planned; STOP only
> on instrument anomaly, integrity-gate failure, or before git push (owner-gated).

## 0. Verified state entering s18 (2026-07-26)

- **SUT sampling COMPLETE:** 5,175/5,175 responses (5 SUTs × 345 × 3 epochs),
  `RUNNER-DONE` on disk, final cost ~$28.20 of the $70 cap (13 transient failures
  were retried successfully). Scored bank = **345** (the "317" in s16 docs is a
  ratified-corrected double-count — never quote it).
- **Sol arm 5,172/5,175**, 0 parse failures. Missing (all qwen ep3, orphaned by
  the overnight /tmp cleanup): `AGG-C6-008__qwen__ep3`, `CONT-N-043__qwen__ep3`,
  `CROSS-C2-005__qwen__ep3`.
- **Opus arm 345/5,175** — chunk 1 (gpt-4o-mini ep1) complete and disk-verified.
  **~4,830 remain** (Workflow chunks are session-bound; that is THIS session's
  main mechanical load).
- **/tmp packet dir is GONE** (cleared overnight). Packets are deterministic and
  regenerable — regenerate before ANY judging (§2 step 1).
- Committed through the mid-run snapshot (`26d3ba85c`); the post-completion data
  (final responses, Sol tail, opus chunks 2+) is NOT yet committed — final
  complete-data commit closes this session.
- Instrument: **strict-v2** (sha `c32fee45652008e724c304a3e6df8c1d4ee43b055a7439d826f1ab0048d6e650`),
  opus + GPT-5.6-Sol mean-of-2, **single-packet mode only** (batch prohibited),
  judges $0. Sol-anchored disclosure regime: opus known-lenient (+57..+68
  single-judge on audited cells) on *advisory-prose-without-artifact* and
  *compliance-theater garnish*; per-judge sensitivity columns mandatory.

## 1. Tiering (unchanged)

Fable main loop: adjudication, triage rulings, analysis design, synthesis.
Everything delegable goes down-tier with explicit `model` per dispatch. Never
read SUT responses or eval transcripts into the main loop — verdict tables and
aggregate CSVs only. Interpreter: `/opt/homebrew/opt/python@3.14/bin/python3.14`
(NOT the vault .venv). Judge fan-outs follow the `dispatching-parallel-agents`
skill (fresh context per verdict, anti-leakage snippet verbatim, watchlist on
returns).

## 2. Mechanical completion (proceed without asking)

1. **Regenerate packets** (from repo root of the project):
   `/opt/homebrew/opt/python@3.14/bin/python3.14 analysis/session17_fullrun_packets.py`
   → expect 5,175 rendered into `/tmp/wcf-s17-fullrun/packets/`.
2. **Finish the 3 Sol verdicts:** run ONE stream —
   `analysis/session17_fullrun_sol_driver.py --stream 0 --nstreams 1` (it renders,
   sees RUNNER-DONE, judges every unjudged cell, exits) — or judge the 3 named
   packets directly via `session16_stability_sol_driver.call_sol`. Verify
   5,175/5,175 in `sol-verdicts/`.
3. **Opus chunks (~4,830):** background Workflow per SUT-epoch pair (≤950 agents
   per workflow; ~25–30 min per 345). Pattern per chunk (proven s16 + s17 chunk 1):
   - Stage 1 `List` (sonnet, effort low): `ls` the chunk's packets, subtract
     existing `logs/20260725-session17-fullrun/opus-verdicts/` entries, return
     `{names:[…]}` (Workflow scripts have NO filesystem access — the agent does
     the listing).
   - Stage 2 `Judge`: one fresh **opus** agent per packet, schema
     `{grade:int (0–100)}`; agent Reads its ONE packet, writes the full verdict
     (ending `GRADE: <int>`) to `opus-verdicts/<name>.md`, returns the grade;
     anti-leakage snippet verbatim in every prompt.
   - After each chunk: verify on-disk count matches (disk is authoritative, the
     workflow return is supplementary). Run 2–3 chunks concurrently; interleave
     with §3–§5 work. KNOWN FAILURE MODE: agents resting at "waiting" — if a
     chunk returns with missing files, relaunch the List→Judge for the gap.

## 3. Aggregation (new dated script; extend `session16_pilot_stats.py` patterns)

- Parse ALL verdicts (strict last-match `GRADE:`), join per (item, SUT, epoch) →
  panel mean-of-2; per-judge columns retained everywhere.
- **Integrity gates before any analysis:** 5,175 cells × 2 judges, 0 unparsed
  (or an explicit disclosed list); per-file counts vs the responses JSONLs
  (authoritative — RUN-SUMMARY's per-epoch `complete` flags for some ep1 rows
  lag and are cosmetic); empty completions floor as data. Verify unique counts
  by set membership, not arithmetic.
- Output: dated panel JSON + per-judge CSVs under `analysis/` and the run log dir.

## 4. Judge-gap triage (MANDATORY — STOP-POINT A ruling)

Rank cells by |opus − Sol|; blind-audit a stratified sample of the top gaps
(fresh opus auditors, raw-materials packets — stem + key + response, no template,
no scores; /tmp isolation; one packet per agent; the s16 B3 pattern). Purpose:
detect advisory-prose / garnish idiom cells at scale; report idiom prevalence and
a Sol-anchored sensitivity read for affected cells. Fable adjudicates audited
cells cell-by-cell. This is the disclosure regime's detection channel — the
headline table is not quotable without it.

## 5. Analysis → the project's FIRST QUOTABLE numbers

1. Per-SUT panel means + per-judge sensitivity columns; paired-epoch significance
   (s7 precedent); per-mold and frontier-core breakdowns; 3-epoch consistency
   reported explicitly (single-epoch verdicts are unreliable — WALKWORTHY lesson).
2. Instrument-reliability: quote the s16 A3 numbers (panel ICC(2,1)=0.985 —
   instrument unchanged by the rejected-v3 episode).
3. Standing regrades: 5-AGG gold_order regrade (`wcf_tasks.py:96` char-split
   fix); fitness re-check (does fit-now rise from 84?).
4. Disclosures: strict-v3 rejected-candidate episode (announce-then-ignore);
   N=345 correction; G4 derivation; opposed judge residuals + the two opus
   idioms + triage results; batch prohibition; NO cross-instrument comparison
   anywhere, including drafts.
5. Dated results report under `reports/` — clearly marked as the first QUOTABLE
   output; everything prior stays EXPLORATORY.

## 6. Close-out

Complete-data commit (responses tail + all verdicts + aggregation outputs +
reports; owner-gated, explicit pathspecs, `pull --rebase --autostash` → push →
`rev-list --count origin/main..HEAD`==0; never pipe `git commit`). Wave report
under `reports/`. Memory: point the s17 entry at outcomes; new s18 entry. s19
boot prompt (paper drafting) if the analysis lands.

## 7. Standing flags + safety (HOOK-ENFORCED; apply to subagents)

Bank v2.5 FROZEN, scored bank 345, episodes (22) OUT. Judges $0 only (Agent/
Workflow opus; codex OAuth Sol — `call_sol` hardened argv, model gpt-5.6-sol,
stdin /dev/null). No deletions (`mv` → `RECYCLE-BIN/`). Report immutability
(new `YYYYMMDD-` files; RUN-MANIFEST status fields are the designed exception).
Deletion-guard scans whole command strings — rephrase, don't fight. pytest
baseline 137 passed + 1 known env failure. Paper directives: no pre-registration
framing, no human raters, venue-generic v1.x. `data/RECYCLE-BIN/` and run-log
RECYCLE-BINs are evidence — don't prune.
