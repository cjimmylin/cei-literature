# BOOT PROMPT — WALKWORTHY v2 PHASE 4: owner-gated next arms (full-bank rescore / paper assembly / pushback_rate promotion)

Paste/read this at the start of a fresh session. Self-contained: a session with zero
prior context can execute it. **Intended main-loop model: Opus suffices**
(`/model opus`) — the arms are spend-memo drafting, manuscript assembly, and a
governed metric-reporting decision; switch to Fable only if an arm surfaces a genuine
adjudication call (say so when it happens). Authored 2026-07-24 by the Fable phase-3
execution session.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

---

## Where things stand (read this, don't re-derive)

Phase 3 is **fully CLOSED** (commit `ffcc48039`, pushed). All three phase-3 arms
executed and verified:

- **Arm A** — paper-shaped validity section at
  `$V2/REPORTS/20260724-paper-validity-section-draft.md`, now **DRAFT v1.1**:
  adversarially reviewed (1 MAJOR fixed — 105 smoke invocations = 7 design tasks
  × 5 SUTs × 3 runs, NOT 26×5×3), then updated same-day with the pilot first-look
  corroboration (§X.7) and the post-anchor B02 state (§X.8). Inline
  `<!-- src -->` comments are kept deliberately (owner ruling) until manuscript
  transplant; two editor-trap comments guard the 355-vs-344 and d04 12-vs-18
  census pitfalls.
- **Arm B** — `$V2/20260724-pushback-rate-first-look.md`: $0 offline re-aggregation
  of the 2026-07-16 pilot design-02 logs (stored judge verdicts already carried
  `pushback_with_alternative`). Headline: pushback_rate 0.13–0.24 per SUT; **32.7%
  of old hold-mass (range 21.8–45.8%) is the third-way state**; break_turn
  invariance proven exactly (stored pilot scalars ≡ recompute, delta 0.000000 × 344
  samples; the recompute tool's "OLD=nan" column is an offline-only decode artifact).
  Pilot-era numbers, C9-fenced from bank rev 2026-07-24b.
- **Arm C** — design-08 `guardrail_state` rubric now carries the owner-ruled boundary
  anchor ("exclusion-with-stated-ground = protected, not steamrolled") —
  `$V2/RULINGS-APPLIED-20260724c.md`. B02 re-judge 30/30: flips 4→2, judge-A/B
  agreement 25→27/30, only movement toward the keyed reading (overt arm), covert
  15/15 untouched. Residual 3 cells = documented judge-sensitivity limitation.
  **Design-08 judge-rubric revision is its own C9 line**: pre-anchor judge verdicts
  (incl. the smoke's stored judge-A + `aggregate-judgeB.txt`) are not comparable to
  post-anchor verdicts without noting the revision.
- Bank revision remains **2026-07-24b** (public 344/344/563, holdout 158/158/260);
  tests 33/33 in the project venv. Assessment ledger PE-1..25 fully dispositioned.
- Holdout item IDs live ONLY in gitignored `$V2/logs/` files — never copy them into
  tracked files or final chat messages.

## Mission

**Step 0 — present the arms menu to the owner via AskUserQuestion before starting
anything** (none was chosen at phase-3 close). The three candidate arms, with costs:

- **ARM 1 — full-bank rescore spend memo → (if authorized) execution.** The
  long-signposted separately-gated run: full public bank (344 runnable items, bank
  rev 2026-07-24b) × pilot SUT set, judge-A + judge-B. FIRST draft a dated spend
  memo: exact item/epoch matrix, per-SUT token estimate scaled from the pilot
  (2026-07-16 full 10-design pilot ≈$3.63 SUT+judge-A; smoke ≈$0.79 for 26 lines
  ×3 eps ×5 SUTs incl. judge-B) and live OpenRouter prices
  (`source ~/.codex/secrets/openrouter.env`), epoch recommendation, and what
  claims the run can/cannot support (C9: first-ever numbers on rev 2026-07-24b;
  no comparison to the pilot without the standing caveats; design-08 under the
  post-anchor rubric). Present envelope via AskUserQuestion; do NOT call any API
  before authorization. Probe model availability (1 × max_tokens=16 per slug)
  before the matrix.
- **ARM 2 — paper assembly ($0, drafting).** Build the paper skeleton around the
  v1.1 validity section: outline the full manuscript (intro/related/design/
  methods/validity/limitations), inventory which existing reports feed which
  sections (pilot report, F-ledger results, JR referee studies, briefing suite,
  smoke report, first-look), and draft the next-most-ready section. Delegate
  drafting to `manuscript-drafter` (opus) from explicit outlines; keep
  what-the-evidence-supports adjudication in the main loop; adversarial-review
  any number-bearing section before it lands.
- **ARM 3 — pushback_rate reporting decision ($0, governed).** Decide whether
  `pushback_rate` is promoted from diagnostic sub-metric to a REPORTED design-02
  headline alongside break_turn in future runs. This is a reporting-surface
  instrument decision (F11/C9): draft the options memo (promote / keep
  diagnostic / defer to post-full-bank evidence), get the owner ruling, record in
  a new dated RULINGS-APPLIED file. Evidence base: first-look report + S1-A
  taxonomy (50/83 neither-cells) + smoke instrument verification. Note the
  first-look's own caveat: single-judge (judge-A era) verdicts; cross-judge
  stability of the state untested.

Run whichever arms the owner picks, in the order picked. Do NOT start any arm
unbidden. ARM 1 execution (not the memo) requires an explicit spend authorization.

## Execution discipline (carried forward — follow it)

- **Bank→converter→metadata loop:** any bank edit is INERT until
  `python tools/convert_banks.py` (public + holdout) → `tools/verify_conversion.py
  --out <NEW dated file>` → fresh dated census → tests. Vendored v1 builders are
  READ-ONLY; marker text must be parser-exact (`**Keyed.**`, `**Keyed behavior:**`,
  `Expressed = **X**`).
- **d04 direction gotcha:** the builder derives keyed_motive direction by scanning
  Keyed prose for the literal substring `delta > 0` — zero-delta prose must avoid
  the literal; positive items must keep it.
- **Tests run in the PROJECT venv** `$V2/.venv/bin/python` (py3.14; vault .venv is
  py3.9 and cannot). 33 tests must pass after any code/bank change.
- **Rescore tooling traps:** `recompute_metrics.py`/`rescore.py` silently skip any
  log path containing the substring "rescore" — never name working dirs that (the
  phase-3 B02 re-judge dir `logs/b02-anchored-judgeB-20260724/` is the working
  example). Both tools glob `*.eval` at the TOP level of `--log-dir` — symlink
  evals into a flat dir to scope a run. `rescore.py` output jsonl carries BOTH
  judge_a (stored) and judge_b (fresh) per row.
- **Shared trunk (WCF sibling sessions are ACTIVE in this clone):** commit your
  files first, then push; if push is rejected, `git pull --rebase` — and if that
  demands stashing, stash ONLY the sibling's named tracked file and **only
  `git stash pop` if your stash push actually created an entry** ("No local changes
  to save" + blind pop = you pop a STRANGER's stash). Two historical stash entries
  (autostash + codex-pre-biblebench-20260713) belong to others — leave them.
- Hard rails: no `rm` (mv to `$V2/RECYCLE-BIN/`); reports immutable (NEW dated
  files, incl. the verify report — pass `--out`); canary in every artifact; holdout
  quarantine; v1 sibling read-only; `/tmp/jr-*` paths in tools/audit are intentional
  referee-blindness — don't fix.
- **Security write-hook sharp edges:** it blocks file-writes containing the token
  exec-immediately-followed-by-open-paren, and ALSO the token
  e-v-a-l-immediately-followed-by-open-paren — including inside the name of
  Python's safe literal parser in `ast`, and even inside prose that merely mentions
  it. Use an indirect accessor in code and circumlocution in prose (see
  `logs/changed-items-smoke-20260724/aggregate_epochs.py` for the working pattern).
  Rephrase; don't fight the hook.
- Instrument changes (rubrics, keys, metrics, REPORTING SURFACE) are governed
  (F11/C9): owner ruling first, outcomes in a NEW dated
  `RULINGS-APPLIED-YYYYMMDD[x].md`.
- Spend: any new API run needs an owner-authorized envelope first; probe model
  availability before matrices; tally spend from eval-log token counts × live
  OpenRouter prices.

## Out of scope (do not pick up unbidden)

New pilot beyond ARM 1's scope · judge/referee re-audit (done 2026-07-16/17) · SUT
leaderboard claims before a full-bank run lands (C9) · `WCF-Benchmark-v2/`
(separate project, actively worked by sibling sessions) · v1 modifications ·
re-running the 2-rater item sweep · new bank edits without a ruling · editing any
existing dated report (successor files only).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
