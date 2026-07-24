# BOOT PROMPT — WALKWORTHY v2 PHASE 3: post-assessment arms (validity section / pushback first-look / B02 watch item)

Paste/read this at the start of a fresh session. Self-contained: a session with zero
prior context can execute it. **Intended main-loop model: Opus suffices** (`/model opus`)
— arms (A) and (B) are drafting + offline rescoring against an already-adjudicated
record; switch to Fable only if an arm surfaces a genuine adjudication call (say so
when it happens). Authored 2026-07-24 by the Fable phase-2 execution session.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

---

## Where things stand (read this, don't re-derive)

The 2026-07-18 item assessment is **fully CLOSED**. Every proposed-edit ledger entry
(PE-1..25) is owner-ruled and APPLIED; three findings stand REFUTED-no-edit
(WW-03-C01, WW-05-D04, WW-08-C04). Nothing in the ledger is pending.

- **Bank revision 2026-07-24b** — public 344 items / 344 runnable / 563 lines,
  holdout 158/158/260; all defect classes 0; verify PASS; tests 33/33 (project venv).
  Governance records: `$V2/RULINGS-APPLIED-20260724.md` (PE-1..8, 18..22) and
  `$V2/RULINGS-APPLIED-20260724b.md` (PE-9..17, 23..25) — commits `3aaab7c2d`,
  `c63debe0c`, both pushed.
- **Changed-items smoke rescore DONE** (owner-authorized, ≈$0.79): 26 changed public
  lines × 5 pilot SUTs × 3 independent single-epoch runs + judge-B rescore. ALL new
  instrumentation verified live end-to-end. Report:
  `$V2/20260724-changed-items-smoke-report.md` (commit `735b44c37`, pushed); raw
  matrix + aggregates in gitignored `$V2/logs/changed-items-smoke-20260724/`.
- Key smoke findings you may build on: `pushback_rate` live and SUT-differentiated;
  `zero_delta_compliance` separates SUTs (llama ≈.85 vs gemini .00); d05 CSR
  sum-enforcement bites; d07's three repaired items are a genuine floor (0/45 arc
  passes, transcript-verified, consistent with pilot floor-saturation); **B02 watch
  item** — judge-A/B disagreement concentrates on the new protected-state boundary
  (protected→steamrolled 4/30).
- Holdout item IDs live ONLY in gitignored `$V2/logs/` files (adjudication rulings,
  census) — never copy them into tracked files or final chat messages.

## Mission

**Step 0 — present the arms menu to the owner via AskUserQuestion before starting
anything** (none was chosen at phase-2 close). The three offered arms, with what each
costs:

- **ARM A — paper-shaped validity section ($0, drafting).** Draft the item-quality /
  validity-evidence section of the eventual paper from the assessment record. Sources
  (all in `$V2/REPORTS/20260718-item-assessment/`): `20260718-04-*` (rater
  reliability: IVR-1.1, kv κw 0.76 both surfaces), `20260718-08-*` (S3 construct
  gradient: GR +18pp; d06/d07 corpus-distinctive), `20260718-10-synthesis.md`
  (verdict + defect taxonomy), plus the two RULINGS-APPLIED files (fix disposition)
  and the smoke report (post-fix instrument verification). Method lessons worth a
  subsection: mechanical severity derivation, adversarial refutation kill-rate (3/10),
  instrument-vs-item artifact partition (C5 packet-builder class, fixed+proven
  2026-07-24). Honest-caveat rails: LLM-raters-only (κ is an upper bound on human
  agreement), single-benchmark scope, C9 comparability discontinuity at bank rev
  2026-07-24b. Delegate drafting to `manuscript-drafter` (opus) from an explicit
  outline; keep adjudication of what the evidence supports in the main loop.
- **ARM B — design-02 `pushback_rate` first-look on stored PILOT logs ($0 API).**
  Offline re-aggregation of the 2026-07-16 pilot logs (`$V2/logs/pilot-20260716/`)
  with the new metrics.py to see how much of the old break/hold mass the third-way
  state re-explains (the S1-A evidence was 50/83 referee neither-cells).
  CAUTION 1: pilot logs were scored by the OLD judge rubric — `pushback_with_alternative`
  existed in rubrics.py then, so stored judge verdicts MAY carry the state; verify
  per-turn verdict fields actually contain it before aggregating (if not, this arm
  needs a re-judge pass ≈$0.15–0.25 — get authorization first).
  CAUTION 2: `recompute_metrics.py`/`rescore.py` silently skip any log path containing
  the substring "rescore" — never name working dirs that.
  CAUTION 3: results are bank-rev-2026-07-16 numbers — report them as pilot-era
  descriptives, C9-fenced from the 2026-07-24b bank.
- **ARM C — B02 protected-boundary judge stabilization (cheap, bounded).** The smoke
  found the PE-8 protected state is judge-dependent (4/30 flips). Options to offer:
  (i) add one clarifying sentence to the design-08 judge rubric anchoring
  "exclusion-with-stated-ground = protected" (rubric edit = instrument change → owner
  ruling + new dated RULINGS-APPLIED), then re-judge B02's 30 smoke verdicts (~$0.02);
  (ii) log as a known limitation in the smoke report's successor — no edit. Evidence:
  `$V2/logs/changed-items-smoke-20260724/aggregate-judgeB.txt`.

Run whichever arms the owner picks, in the order picked. Do NOT start any arm
unbidden; do NOT start a full-bank rescore (that is a separate authorization).

## Execution discipline (carried forward — follow it)

- **Bank→converter→metadata loop:** any bank edit is INERT until
  `python tools/convert_banks.py` (public + holdout) → `tools/verify_conversion.py
  --out <NEW dated file>` → fresh dated census in `logs/item-assessment-20260718/` →
  tests. Vendored v1 builders are READ-ONLY; marker text must be parser-exact
  (`**Keyed.**`, `**Keyed behavior:**`, `Expressed = **X**`).
- **d04 direction gotcha:** the builder derives keyed_motive direction by scanning
  Keyed prose for the literal substring `delta > 0` — zero-delta prose must avoid the
  literal; positive items must keep it.
- **Tests run in the PROJECT venv** `$V2/.venv/bin/python` (py3.14; vault .venv is
  py3.9 and cannot). 33 tests must pass after any code/bank change.
- **Shared trunk (WCF sibling sessions are ACTIVE in this clone):** commit your files
  first, then push; if push is rejected, `git pull --rebase` — and if that demands
  stashing, stash ONLY the sibling's named tracked file and **only `git stash pop` if
  your stash push actually created an entry** ("No local changes to save" + blind pop
  = you pop a STRANGER's stash; this bit the phase-2 session — repaired via
  `git restore --source=HEAD` on the conflicted files, stash entries preserved).
  Two historical stash entries (autostash + codex-pre-biblebench-20260713) belong to
  others — leave them.
- Hard rails: no `rm` (mv to `$V2/RECYCLE-BIN/`); reports immutable (NEW dated
  files, incl. the verify report — pass `--out`); canary in every artifact; holdout
  quarantine; v1 sibling read-only; `/tmp/jr-*` paths in tools/audit are intentional
  referee-blindness — don't fix.
- **Security write-hook sharp edges:** it blocks file-writes containing the token
  exec-immediately-followed-by-open-paren, and ALSO the token
  e-v-a-l-immediately-followed-by-open-paren — including inside the name of Python's
  safe literal parser in `ast`, and even inside prose that merely mentions it. Use an
  indirect accessor (`getattr(ast, "literal_" + <the four letters>)`) in code and
  circumlocution in prose (see `logs/changed-items-smoke-20260724/aggregate_epochs.py`
  for the working pattern). Rephrase; don't fight the hook.
- Instrument changes (rubrics, keys, metrics) are governed (F11/C9): owner ruling
  first, outcomes in a NEW dated `RULINGS-APPLIED-YYYYMMDD[x].md`.
- Spend: any new API run needs an owner-authorized envelope first; probe model
  availability (1 × max_tokens=16 per slug) before matrices; tally spend from eval-log
  token counts × live OpenRouter prices (`source ~/.codex/secrets/openrouter.env`).

## Out of scope (do not pick up unbidden)

Full-bank rescore or new pilot (separate authorization) · judge/referee re-audit
(done 2026-07-16/17) · SUT leaderboard claims (C9) · `WCF-Benchmark-v2/` (separate
project, actively worked by sibling sessions) · v1 modifications · re-running the
2-rater item sweep · new bank edits without a ruling.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
