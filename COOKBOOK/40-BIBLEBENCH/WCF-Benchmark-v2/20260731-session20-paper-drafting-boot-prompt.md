# WCF-Benchmark-v2 — Session 20 Boot Prompt (paper drafting from the FIRST QUOTABLE results)

> Paste as the opening prompt of a fresh session. Authored 2026-07-31 at the
> close of s19. Orient via `INDEX.md`, then read (in this order):
> `reports/20260731-session19-quotable-results-report.md` (the primary
> source — every number in the paper comes from here or its cited
> artifacts, nowhere else), `analysis/20260731-session19-judge-gap-triage.md`
> (disclosure detail), `analysis/20260725-session17-v3-gate-adjudication.md`
> (the rejected-candidate episode, must be disclosed). No stop-points
> pre-planned; STOP only on a numeric claim you cannot trace to a cited
> artifact, an instrument-validity question, or before git push (owner-gated).

## 0. Verified state entering s20 (2026-07-31)

- **Session 19 CLOSED.** Full run complete (5,175/5,175 both judge arms),
  mandatory judge-gap triage executed (90-cell stratified blind audit, 90%
  idiom rate), first QUOTABLE results report shipped and **committed +
  pushed**: commit `ca698532320b6299ca371ac50621509595370225`, verify with
  `git log -1 --format="%H %ad"` from `CEI-Lit-WS/` root — should show that
  hash. `git status --short` from repo root should be clean (0 lines) unless
  you have new uncommitted work.
- **What is quotable:** ONLY `reports/20260731-session19-quotable-results-report.md`
  and the artifacts it cites (`analysis/20260731-session19-headline-analysis.json`,
  `-judge-gap-triage.md`/`.json`, `-agg-fitness-regrade.json`,
  `20260731-session18-{panel.json,perjudge.csv}`). **Every prior report
  (sessions 1–18, including the s9 readiness reports, the session-10 deck,
  and `INDEX.md`'s own historical framing) is EXPLORATORY / NON-QUOTABLE and
  reflects a stale bank version (v2.4, 287 items) or a pre-triage headline —
  do not pull numbers, leaderboards, or claims from them into the paper.**
  They are reusable for *structure* only (see §2).
- **No paper draft exists yet.** `METHODS/` holds harness/handoff docs, not
  paper prose. The closest prior scaffolding is
  `reports/20260717-session9-0{1..6}-*.md` (benchmark card, evaluation,
  meta-judging, overview, next-steps, messaging/abstract) — all dated s9,
  all stale on numbers and history (stop at s8; miss the v3-gate episode,
  the full run, and the triage entirely). Reuse their section shape, rewrite
  every number and claim against s19.
- **Paper directives (stated, binding):** no pre-registration framing, no
  human raters, **venue-generic v1.x** (do not name a target venue or mint a
  DOI at this stage — matches the vault-wide v1.x convention used elsewhere,
  e.g. `feedback_no_pre_reg_for_v1_manuscripts` /
  `feedback_no_preprint_v1.0_vault_wide_v2_subprojects` in memory, extended
  here to this project by the s19 boot prompt's own §4).
- Portfolio labeling convention (from `PAPER-FIRST-DECISIONS.md` PF-003,
  scoped to WCF-Bench **v1** but sets the house style): exploratory material
  gets stamped `EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE`.
  Nothing in the v2 paper should carry that stamp — v2's dual-judge,
  triaged, 3-epoch design is exactly what earns it the QUOTABLE status s19
  established. If you draft any exploratory appendix/preview material, stamp
  it accordingly; the main paper body should not need to.

## 1. Tiering (unchanged from s19)

Main loop: structure the paper, adjudicate claims against cited artifacts,
adversarial self-check before calling a section done. Everything delegable
(drafting prose from a spec, formatting, figure/table generation) goes
down-tier — `manuscript-drafter` (opus) is the natural fit per
`.claude/agents/` (root vault). Never read raw SUT responses, packets, or
verdict transcripts into the main loop — the s19 report and its cited JSONs
are aggregate/verdict-table artifacts and are fine to read directly. Pass
`model` explicitly on every dispatch.

## 2. Mission: draft the v1.x paper

1. **Reuse structure, not content**, from the s9 reports:
   - Benchmark card (`20260717-session9-01`) → composition/taxonomy section.
     Rewrite: bank is now 345 (v2.5), not 287 (v2.4); molds are AGG/COMP/
     CONT/CROSS/DUTY/LIB/MEND/PROOF/STED/WHOLE; frontier-core is 146 items
     (`analysis/20260724-session13-frontier-core-index.json`), not whatever
     s9 cited.
   - Evaluation section (`20260717-session9-02`) → leaderboard/scoring
     section. Rewrite entirely from `20260731-session19-quotable-results-report.md`
     §1–3 (panel means, per-judge sensitivity, s7 MDD80 pairwise
     significance, frontier-core split, per-mold breakdown).
   - Meta-judging section (`20260717-session9-03`) → judge design/reliability
     section. Rewrite from s19 §4 (judge-gap triage) and §5 (ICC 0.985)
     — this supersedes s9's meta-judging findings, don't blend them.
   - Overview-of-work (`-04`) and next-steps (`-05`) → informal background
     only; do not cite their content as findings.
   - Messaging/abstract draft (`-06`) → framing guardrails may still apply
     (check tone/scope), but the abstract itself must be rewritten from
     scratch against s19 numbers, not edited from the s9 draft.
2. **Every number in the paper must trace to** `20260731-session19-quotable-results-report.md`
   or its cited JSON artifacts. If you want a number not already computed
   there (e.g. a different cut of the data), compute it fresh from
   `analysis/20260731-session18-perjudge.csv` / `-panel.json` with a new,
   named script under `analysis/session20_*.py` — do not eyeball or
   re-derive numbers by hand, and do not re-run any judging.
3. **Disclosures are load-bearing in the paper too**, not just the report —
   carry all 6 items from s19 §8 (v3-rejected-candidate episode, N=345
   correction, opposed-judge residuals + triage results, duplicate-judge
   artifact, batch-mode prohibition, no-cross-instrument-comparison) into
   the paper's limitations/methods-integrity section. Do not soften or drop
   any of them for narrative flow.
4. **The MEND-N-018 rubric self-contradiction** (flagged, not fixed, in the
   triage) should get one sentence in a limitations/future-work note — do
   not attempt to fix the rubric or re-score the item in this session; that
   is explicitly out of scope for a paper-drafting pass.
5. Target format: fpdf2 or Typst if/when a PDF build is wanted (root
   CLAUDE.md's environment constraint — no LaTeX/Pango unless confirmed
   available). Markdown source first; don't jump to PDF build before the
   prose is adjudicated.

## 3. What NOT to do this session

- No new judging, no re-triage, no re-aggregation — s19's data is frozen and
  complete. If a paper-drafting need surfaces a genuine analysis gap (not
  already in the s19 report), flag it as a candidate for a dedicated
  analysis session rather than quietly running it here.
- No cross-instrument comparison anywhere in the draft, including
  informally in prose — v2↔v3 bench deltas are instrument diagnostics only.
- No venue selection, no DOI, no author list, no submission prep — stays
  venue-generic per §0.
- Do not edit or "correct" the s19 report itself; it's the frozen input.
  Supersede via a new dated artifact if something in it needs revision.

## 4. Standing flags + safety (HOOK-ENFORCED; apply to subagents)

Bank v2.5 FROZEN, scored bank 345, episodes (22) OUT. No deletions (`mv` →
`RECYCLE-BIN/`). Report immutability (new `YYYYMMDD-` files). Deletion-guard
scans whole command strings — rephrase, don't fight it. pytest baseline 137
passed + 1 known env failure (`.venv-v2/bin/python -m pytest tests/ -q`) —
re-check if you touch `src/` or `analysis/` for any reason.

## 5. Close-out (after a full draft lands)

Commit is owner-gated — explicit pathspecs (never `git add -A`), write the
commit message to a file, `git commit -F <file>` (never pipe `git commit`),
verify with `git log -1 --stat`, `pull --rebase --autostash` → push →
`git rev-list --count origin/main..HEAD` == 0. Update `INDEX.md`'s
"Current state" line to point at the new draft. Memory: new s20 entry
pointing at [[20260731-wcf-v2-s19-triage-first-quotable-report]] with the
outcome. Do not pre-write a session-21 boot prompt unless the draft actually
lands cleanly.
