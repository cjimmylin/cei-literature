# WCF-Benchmark-v2 — Session 19 Boot Prompt (Fable · judging COMPLETE → judge-gap triage → first QUOTABLE analysis → close-out)

> Paste as the opening prompt of a fresh **Fable** session. Authored 2026-07-31 —
> **SUPERSEDES `20260726-session18-boot-prompt.md`** (written at the start of
> judging; this version reflects the verified post-judging state). Orient via
> `INDEX.md`, then read: `reports/20260725-session17-wave-report.md` (rulings +
> launch), `logs/20260725-session17-fullrun/RUN-MANIFEST.json` (scope,
> instrument, disclosure obligations), `analysis/20260725-session17-v3-gate-adjudication.md`
> (why strict-v2 + Sol-anchored disclosure). No stop-points pre-planned; STOP
> only on instrument anomaly, integrity-gate failure, or before git push
> (owner-gated).

## 0. Verified state entering s19 (2026-07-31)

- **BOTH judging arms COMPLETE at 5,175/5,175.** Sol (GPT-5.6) finished early
  in s18; opus (Claude) finished at the end of s18 after ~10 Workflow chunks,
  several session-limit interruptions, and one monthly-spend-limit interruption
  (owner raised the cap mid-session; work resumed each time from exactly where
  disk left off — no data was ever lost, only delayed).
  Verify before trusting anything below:
  `ls logs/20260725-session17-fullrun/opus-verdicts | grep -cE '__(gpt-4o-mini|gpt-5-mini|haiku|minimax-m3|qwen)__ep[123]\.md$'`
  and the same for `sol-verdicts` (no filter needed there) — both MUST read 5175.
- **Gated aggregation run in STRICT mode (no `--allow-partial`) — all 5
  integrity gates PASS** over the complete 5,175×2 matrix:
  `analysis/session18_aggregation.py --date 20260731` (mirrored copies of
  outputs live in both `analysis/` and `logs/20260725-session17-fullrun/`):
  `20260731-session18-panel.json` + `20260731-session18-perjudge.csv`.
  An earlier partial run under `--date 20260729` also exists on disk — **do
  not cite it**; only the `20260731` strict pass is post-completion-verified.
- **Exploratory (pre-triage, NOT quotable) headline read** from the 20260731
  aggregation, panel_mean = mean(opus, Sol) per cell, n=1035 per SUT:

  | SUT | panel mean | mean opus−Sol gap | \|gap\|≥30 cells |
  |---|---|---|---|
  | gpt-4o-mini | 47.55 | −1.66 | 75 (7.2%) |
  | gpt-5-mini | 72.93 | −0.54 | 38 (3.7%) |
  | haiku | 63.53 | +2.28 | 76 (7.3%) |
  | minimax-m3 | 74.09 | +3.69 | 67 (6.5%) |
  | qwen | 73.09 | +4.00 | 58 (5.6%) |
  | **ALL** | **66.24** | **+1.56** | **314 / 5175 (6.1%)** |

  Near-zero mean gaps mask real per-cell dispersion (6.1% |gap|≥30) — this is
  exactly what the mandatory triage (§1 below) exists to characterize. Do not
  quote this table as-is in any report; it is the *input* to triage, not an
  output.
- **Known benign duplicate-judge artifact**: 4 qwen cells (COMP-N-020/021/024
  ep2-or-3, CONT-N-004 ep2) were independently judged twice by opus during
  overlapping chunk relaunches. A file-safety hook preserved the pre-existing
  verdict as a `*.bak`/`*preexisting*` sidecar before the second write landed
  — no data loss, no double-counting (aggregation only reads the canonical
  `<item>__<sut>__<ep>.md` filename; `.bak` files are invisible to it, gate 4
  confirmed 0 parse anomalies). Two of the four pairs showed real grade
  divergence between the two independent passes (COMP-N-021: 9→5; CONT-N-004:
  68→59) — minor evidence of opus judge-pass noise, worth one disclosure
  sentence in the final report, not a blocker. The stray sidecar files are
  harmless clutter in `opus-verdicts/`; leave them (they're audit trail, not
  reports/logs subject to the immutability rule) — just don't let a naive
  `ls | wc -l` count them as verdicts; always filter to the canonical pattern
  as shown above.
- Instrument: **strict-v2** (sha `c32fee45652008e724c304a3e6df8c1d4ee43b055a7439d826f1ab0048d6e650`),
  opus + GPT-5.6-Sol mean-of-2, **single-packet mode only** (batch prohibited),
  judges $0 (opus via Agent/Workflow; Sol via codex OAuth `call_sol`). Sol-
  anchored disclosure regime: opus known-lenient (+57..+68 single-judge on
  audited cells) on *advisory-prose-without-artifact* and *compliance-theater
  garnish*; per-judge sensitivity columns mandatory in all reporting.
- Scored bank N = **345** (never 317 — s16's "317" was a ratified-corrected
  double-count). Episodes (22) OUT of scope.
- **Git is NOT yet committed** for any of this session's work: responses
  tail, all 15 opus chunks, aggregation outputs, sol-stream logs are all
  modified/untracked (`git status --short` from repo root). Commit is
  owner-gated — do not push without explicit sign-off (§5 close-out).
- `/tmp/wcf-s17-fullrun/packets/` may or may not survive between sessions
  (it did NOT survive the s17→s18 gap). If judging or triage packet reads
  fail with ENOENT, regenerate first:
  `/opt/homebrew/opt/python@3.14/bin/python3.14 analysis/session17_fullrun_packets.py`
  (deterministic, idempotent, expect 5175 rendered).

## 1. Tiering (unchanged)

Fable main loop: adjudication, triage rulings, analysis design, synthesis.
Everything delegable goes down-tier with explicit `model` per dispatch. Never
read SUT responses, packets, or verdict transcripts into the main loop —
verdict tables and aggregate CSVs only. Interpreter:
`/opt/homebrew/opt/python@3.14/bin/python3.14` (NOT the vault .venv). Fan-outs
follow the `dispatching-parallel-agents` skill (anti-leakage snippet verbatim
for any comparison dispatch — the judge-gap triage IS a comparison dispatch:
auditors must not see opus's or Sol's existing scores).

## 2. Judge-gap triage (MANDATORY — STOP-POINT A ruling; do this BEFORE any
   report claims quotable status)

This is the disclosure regime's detection channel for advisory-prose /
compliance-theater garnish idioms at scale. Without it, the headline table in
§0 is not quotable.

1. From `20260731-session18-perjudge.csv`, select the 314 cells with
   `|gap| >= 30` (or recompute the threshold if you have a principled reason
   to change it — document why).
2. **Stratify a sample** across SUT × mold (item family, e.g. AGG/COMP/CONT/
   CROSS/DUTY/LIB/MEND/PROOF/STED/WHOLE) so no single SUT or mold dominates
   the audited set. Aim for a sample large enough to estimate idiom
   prevalence with reasonable precision (s16's B3 pattern used a comparable
   stratified pull — check `analysis/session16_a1_audit_packet.py` for the
   sampling code to reuse/adapt).
3. **Blind audit each sampled cell**: fresh opus agent, ONE packet per agent,
   raw materials only (scenario/question stem + gold key + SUT response) —
   **no rubric-application template, no existing scores, no GATE-mode
   verdict text**. The auditor's job is to characterize *why* opus and Sol
   diverged (garnish idiom present? genuine substantive disagreement?
   ambiguous key? other?), not to re-grade. Tempdir isolation from the repo
   recommended (anti-leakage). This mirrors the s16 B3 audit-packet pattern —
   reuse `session16_a1_audit_packet.py` conventions, don't reinvent.
4. **Fable adjudicates the audited cells cell-by-cell** — do not delegate the
   final characterization. Tally: idiom-driven vs. genuine-disagreement vs.
   other, per SUT, with rate estimates and confidence caveats given the
   sample size.
5. Write the triage result to a new dated file under `analysis/` — this
   becomes a load-bearing input to the report in §3, not an appendix.

## 3. Analysis → the project's FIRST QUOTABLE numbers

1. Per-SUT panel means + per-judge sensitivity columns (both opus and Sol
   shown separately, not just panel mean); paired-epoch significance (s7
   precedent — check `analysis/` for the s7 method if not already documented
   here); per-mold and frontier-core breakdowns; 3-epoch consistency reported
   explicitly (single-epoch verdicts are unreliable — WALKWORTHY lesson,
   [[project_walkworthy_v2]] in memory).
2. Instrument-reliability: quote the s16 A3 numbers (panel ICC(2,1)=0.985 —
   instrument unchanged by the rejected-v3 episode; the v3 gate failure and
   auto-revert are a disclosed methodological episode, not a validity threat
   to the frozen v2 instrument actually used).
3. Standing regrades (deferred from s16/s17, ride this analysis pass):
   - 5-AGG gold_order regrade (`wcf_tasks.py:96` char-split bug fix).
   - Fitness re-check: does fit-now rise from 84 once the fix is applied?
4. Disclosures section (all of these are load-bearing, not boilerplate):
   - strict-v3 rejected-candidate episode (announce-then-ignore blind
     characterization; the auto-revert).
   - N=345 correction (never cite 317).
   - G4 derivation (28 ids already absent from frozen bank, sha-verified).
   - Opposed judge residuals + the two opus idioms (advisory-prose,
     compliance-theater garnish) + this session's triage results.
   - The 4-cell duplicate-judge artifact from §0 (one sentence).
   - Batch-mode prohibition (single-packet only, throughout).
   - **NO cross-instrument comparison anywhere, including drafts** — v2↔v3
     bench deltas are instrument diagnostics only, never SUT evidence.
5. Dated results report under `reports/` — title it clearly as the **first
   QUOTABLE** output of the project; every prior report/artifact (s15-s18)
   stays EXPLORATORY and should not be cited as evidence in papers.

## 4. Standing flags + safety (HOOK-ENFORCED; apply to subagents)

Bank v2.5 FROZEN, scored bank 345, episodes (22) OUT. Judges $0 only (Agent/
Workflow opus; codex OAuth Sol — `call_sol` hardened argv, model
gpt-5.6-sol, stdin /dev/null). No deletions (`mv` → `RECYCLE-BIN/`). Report
immutability (new `YYYYMMDD-` files; `RUN-MANIFEST` status fields are the
designed exception). Deletion-guard scans whole command strings — rephrase,
don't fight it. pytest baseline 137 passed + 1 known env failure. Paper
directives: no pre-registration framing, no human raters, venue-generic v1.x.
`data/RECYCLE-BIN/` and run-log RECYCLE-BINs are evidence — don't prune.

## 5. Close-out (after §3 lands)

Complete-data commit — owner-gated, explicit pathspecs (do NOT `git add -A`):
responses tail + all opus/sol verdicts + aggregation outputs + triage +
reports; `pull --rebase --autostash` → push → `rev-list --count
origin/main..HEAD`==0; **never pipe `git commit`** (write message to a file,
`git commit -F <file>`, verify with `git log -1 --stat`). Wave report under
`reports/`. Memory: point the s18 entry (if one exists) at outcomes; new s19
entry. s20 boot prompt (paper drafting) only if the analysis in §3 actually
lands cleanly — don't pre-write it speculatively.
