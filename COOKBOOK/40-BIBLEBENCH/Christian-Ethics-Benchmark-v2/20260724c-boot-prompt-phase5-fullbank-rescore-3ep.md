# BOOT PROMPT — WALKWORTHY v2 PHASE 5: ARM 1 full-bank run, 3 epochs (owner-preselected config)

Paste/read this at the start of a fresh session. Self-contained: a session with zero
prior context can execute it. **Intended main-loop model: Opus suffices**
(`/model opus`) — this is a spend memo + a scripted run + a governed report; switch to
Fable only if a genuine claims-adjudication call surfaces (say so when it happens).
Authored 2026-07-24 by the Fable phase-4 session.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

---

## Where things stand (read this, don't re-derive)

- Phase 4 **CLOSED** (commit `3eb6a8388`, pushed): paper-(a) skeleton + source map
  (`$V2/REPORTS/20260724c-paper-skeleton-and-source-map.md`), §3–§4 design-section
  draft v1.1 (adversarially reviewed, SHIP), and the **A′ ruling**
  (`$V2/RULINGS-APPLIED-20260724d.md`): `pushback_rate` is on the reported design-02
  surface as a SECONDARY metric — **per-judge only, never pooled across judges**,
  standing "cross-judge stability untested" caveat — with `break_turn` the sole
  design-02 headline. This run's report MUST follow that surface.
- Bank revision **2026-07-24b** (public 344 items / 344 runnable / 563 admin lines;
  holdout 158/158/260 — holdout stays quarantined, see rails). Tests 33/33 in the
  project venv. No bank or code edits are expected this session.
- **Owner pre-selected the 3-epoch configuration** (2026-07-24, phase-4 session,
  verbatim ask: "write a boot prompt for all 3 epochs for next session").
  Pre-selection covers the CONFIG only, not the SPEND: the final envelope still
  requires an explicit in-session GO (Mission step 3) after live-price pinning.
- **Prior estimate (to be re-pinned, not trusted):** per-epoch all-in ≈ $4.50–5.70;
  3 epochs ≈ **$14–17**, proposed ceiling **~$25** incl. retry headroom. Anchors:
  2026-07-16 pilot $3.63 = full bank (563 lines) × 5 SUTs × 1 epoch, SUT + judge-A;
  2026-07-24 smoke $0.79 / 390 line-runs all-in (incl. judge-B; mix skews expensive);
  judge-B ≈ $0.0007–0.001/verdict (smoke 390 rescores; B02 30 verdicts ≈ $0.02).
- Design-08 note: this will be the FIRST full-bank run under the post-anchor
  design-08 judge rubric (`RULINGS-APPLIED-20260724c.md`). Pre-anchor design-08
  judge verdicts (pilot, smoke judge-A stores) are a separate comparability line.

## Mission (in order)

1. **Availability probes** (authorized as memo prep, ≤$0.01 total): 1 call ×
   max_tokens=16 per slug — the 5 pilot SUTs, judge-A, judge-B, and the pinned
   design-02/07 branch classifier. Take exact slugs from `$V2/tasks/` config and the
   ops section of `$V2/20260716-pilot-report.md` — do NOT reconstruct slugs from
   memory. Credentials: `source ~/.codex/secrets/openrouter.env`. If any slug is
   delisted, STOP and surface it — a substitute model is an owner decision (C6
   forbids silently swapping the classifier; a substitute SUT changes the matrix).
2. **Draft the dated spend memo** (`$V2/YYYYMMDD-spend-memo-fullbank-3ep.md`, NEW
   dated file, canary): exact matrix (per-design admin-line counts × 5 SUTs × 3
   epochs, taken from `$V2/20260724b-conversion-parity-report.md` §1 — note that
   file's internal header says 2026-07-15; its tables ARE the 24b revision), live
   OpenRouter prices per slug, bottom-up cost estimate + ceiling, and the **claims
   envelope**: (a) these are FIRST-EVER numbers on bank rev 2026-07-24b (C9);
   (b) NO comparisons to the 2026-07-16 pilot except with the standing caveats
   (bank changed at 24b; design-08 rubric is its own C9 line); (c) within-run
   comparative claims only per the families in
   `$V2/20260716-prereg-comparisons-RATIFIED.md` and only where they survive R4
   (same direction under both judges) — anything else is descriptive cells with
   intervals, no rankings, no composites; (d) design-02 surface per the A′ ruling;
   (e) public bank only, holdout untouched. Also state what this run buys the
   governance queue: per-judge `pushback_rate` cells = the evidence base for the
   deferred headline re-decision (RULINGS-APPLIED-20260724d condition 3).
3. **Present the envelope via AskUserQuestion** (GO / no-GO / modify). Do NOT call
   any API beyond step 1's probes before an explicit GO. If no-GO, commit the memo
   and stop cleanly.
4. **Execute (on GO):** follow the smoke pattern — **3 independent single-epoch
   runs per SUT** (not epochs×3 in one eval; keeps logs separable and resumable),
   judge-A inline at run time; then a full judge-B pass via the rescore tooling.
   Logs under a NEW dated dir whose path NEVER contains the substring "rescore"
   (e.g. `$V2/logs/fullbank-3ep-YYYYMMDD/`); the recompute/rescore tools glob
   `*.eval` at the TOP level of `--log-dir` — symlink evals into a flat dir to
   scope each pass. Offline aggregation: reuse the pattern (and the
   security-hook-safe accessor idiom) in
   `$V2/logs/changed-items-smoke-20260724/aggregate_epochs.py`.
5. **Report** (NEW dated file, canary): per-design × per-judge cells with
   intervals; design-02 prints `break_turn` (headline) + `pushback_rate`
   (secondary, per-judge, never pooled, with the standing caveat); per-judge
   pushback_rate stability explicitly tabulated (feeds the headline re-decision —
   present it, do not decide it); design-05 CSR judge-free; spend tally from
   eval-log token counts × live prices vs the authorized ceiling. NO SUT
   leaderboard language beyond what the memo's claims envelope licensed. If any
   defect forces a code/bank edit mid-run, STOP — owner ruling first (F11).
6. **Close:** run the 33-test suite (should be untouched), commit + push per the
   shared-trunk discipline below, update auto-memory
   (`20260718-walkworthy-v2-item-assessment.md` addendum + MEMORY.md index line).

## Execution discipline (carried forward — follow it)

- **Tests run in the PROJECT venv** `$V2/.venv/bin/python` (py3.14; the vault .venv
  is py3.9 and cannot).
- **Rescore tooling traps:** `recompute_metrics.py`/`rescore.py` silently skip any
  log path containing the substring "rescore" — never name working dirs that.
  `rescore.py` output jsonl carries BOTH judge_a (stored) and judge_b (fresh) per row.
- **Shared trunk (WCF sibling sessions ACTIVE in this clone):** commit your files
  first, then push; if rejected, `git pull --rebase` — and if that demands stashing,
  stash ONLY the sibling's named tracked file and **only `git stash pop` if your
  stash push actually created an entry** ("No local changes to save" + blind pop =
  you pop a STRANGER's stash). Historical stash entries belong to others — leave them.
- Hard rails: no `rm` (mv to `$V2/RECYCLE-BIN/`); reports immutable (NEW dated
  files only); canary in every artifact; **holdout quarantine — this run is the
  PUBLIC bank only; the holdout is reserved for a future blind first-use run and
  its item IDs live only in gitignored `$V2/logs/`**; v1 sibling read-only;
  `/tmp/jr-*` paths in tools/audit are intentional referee-blindness — don't fix.
- **Security write-hook sharp edges:** it blocks file-writes containing the token
  exec-immediately-followed-by-open-paren and ALSO e-v-a-l-immediately-followed-by-
  open-paren — even in prose. Use an indirect accessor in code and circumlocution
  in prose (working pattern: the smoke's `aggregate_epochs.py`). Rephrase; don't
  fight the hook.
- Governance: instrument changes (rubrics, keys, metrics, reporting surface) need
  an owner ruling first, recorded in a NEW dated `RULINGS-APPLIED-YYYYMMDD[x].md`.
  The reporting surface for this run is ALREADY ruled (A′) — apply it, don't relitigate.
- Spend: tally from eval-log token counts × live OpenRouter prices; report actual
  vs ceiling in the run report.

## Out of scope (do not pick up unbidden)

Holdout runs (quarantined) · new bank/rubric/metric edits · paper §5/§6 drafting and
the related-work sweep (separate arm; skeleton at
`REPORTS/20260724c-paper-skeleton-and-source-map.md` queues them) · judge/referee
re-audit · pushback_rate HEADLINE re-decision (this run only produces its evidence) ·
`WCF-Benchmark-v2/` (separate project, actively worked by sibling sessions) · v1
modifications · editing any existing dated report (successor files only).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
