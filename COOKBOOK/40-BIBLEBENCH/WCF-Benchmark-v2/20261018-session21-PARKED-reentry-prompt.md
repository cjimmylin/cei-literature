# WCF-Benchmark-v2 — PARKED (2026-10-18, session 21) — Re-entry prompt

**Parked 2026-10-18 by owner decision.** Session 21's boot prompt
(`20260806-session21-next-direction-boot-prompt.md` §2) offered six candidate directions. The owner
chose **#4 then #6**: close the T2a/T2b documentation gap in a superseding paper file, then
formally park the project with a dated re-entry pointer. The owner made this choice after reading a
decision brief prepared on 2026-10-18; the brief is not stored in the vault. Its reasoning is
summarized in §3 below. This note follows the vault's parking pattern
(`COOKBOOK/20260706-PARKED-opus-reentry-prompt.md`) and is now the project's entry point, replacing
the session-21 boot prompt. **Nothing is queued.** Re-entry needs a new owner instruction that names
a direction.

What session 21 did: it ran no model calls and spent $0. It wrote the s21 paper revision and its
build script, this note, and the `INDEX.md` status update. It did **not** commit or push: committing
is owner-gated. The four touched paths are listed in §4, step 1.

---

## 1. What is final and quotable

- **Numbers:** `reports/20260731-session19-quotable-results-report.md` is still the project's
  only quotable source. Every report from sessions 1–18 stays EXPLORATORY and must not be cited as
  evidence about any model.
- **Narrative:** `reports/20261018-session21-v1x-paper-draft.md` is the current paper. It supersedes
  `reports/20260731-session20-v1x-paper-draft.md`, the owner-accepted s20 draft, which stays on disk
  unchanged. The s21 revision differs only in the T2a/T2b tier-label correction (see its change
  note). No number, result, or disclosure changed.
- **What the paper establishes:**
  - A completed run of 5 systems under test (SUTs) × 345 items × 3 epochs, giving 5,175 responses.
  - Scoring by the frozen strict-v2 dual-judge instrument (Opus + GPT-5.6-Sol mean-of-2,
    single-packet, ICC(2,1) = 0.985).
  - A three-tier ranking: {gpt-5-mini, minimax-m3, qwen} tied at the top, then haiku, then
    gpt-4o-mini.
  - The 146-item frontier core is 11–21 points harder for every SUT.
  - The judge-gap triage found 90% of sampled high-disagreement cells to be driven by two
    response idioms.
  - Six disclosures, plus the rejected strict-v3 episode, are in the paper's Section 5.
- **Frozen surfaces (unchanged):**
  - Bank v2.5: 345 scored items. The 22 episode items stay out of scope.
  - Instrument strict-v2, sha `c32fee45…e6650`.
  - Single-packet judging only; batch judging prohibited.
  - No cross-instrument comparison.

## 2. Where the artifacts are (paths relative to this folder)

| Artifact | Path |
|---|---|
| Current paper (s21 revision) | `reports/20261018-session21-v1x-paper-draft.md` |
| Accepted s20 draft (superseded, unchanged) | `reports/20260731-session20-v1x-paper-draft.md` |
| PDF build scripts | `reports/20261018-session21-build-pdf.py` (s21) · `reports/20260731-session20-build-pdf.py` (s20) |
| PDFs | **s21 PDF NOT built**: the parking session's environment has pandoc but not the typst CLI. Build it from this folder with `.venv-v2/bin/python reports/20261018-session21-build-pdf.py` once typst is installed. Do not commit the `.master.md` intermediate. The s20 PDF (2026-07-31) is gitignored and disk-only; it is not present in every checkout. |
| Quotable results + analysis | `reports/20260731-session19-quotable-results-report.md` · `analysis/20260731-session19-headline-analysis.json` · `analysis/20260731-session19-judge-gap-triage.md` |
| Full-run data | `logs/20260725-session17-fullrun/` (RUN-MANIFEST, responses, both verdict arms) |
| Bank + composition | `data/wcf_main.jsonl` · `data/BANK-VERSION.json` · `analysis/session20_composition_stats.py` → `analysis/20260731-session20-composition-stats.json` · `vendor/v1-bank-yaml/` |
| Instrument records | `analysis/20260724-session16-instrument-freeze.json` · `analysis/20260725-session17-v3-gate-adjudication.md` |
| Tier definitions (source of the s21 correction) | `../WCF-Benchmark/01-DESIGNS/03-aggravate.md` L24–30 · `07-prooftext.md` L30–36 · `09-wholeheart.md` L25–31 |
| Full-run cost record | `reports/20260725-session16-fullrun-design-memo.md` §1, §3 · `20260726-session18-boot-prompt.md` §0 (SUT spend about $28.20 of the $70 cap; judges $0 via subscription channels) |

## 3. Deliberately left undone, and why

- **#1 Target venue and submission prep: deferred, not ruled out.** Nothing on record names a venue
  or deadline. Venue, DOI, and author list remain owner-only decisions. Reviewers will likely raise
  two points: the roster has only small and mid-tier models, and the top-tier tie is unresolved.
- **#2 Larger SUT roster: not funded.** This requires paid SUT sampling. The 5-SUT run cost about
  $28.20, at $0.0004–0.011 per item. No premium-model price has been estimated. Each added SUT means
  about 2 × 1,035 verdicts: roughly 4 h of Sol at 4 streams plus about 1 h of Opus, at the
  throughputs in the s16 memo §1. It also needs a fresh judge-gap triage before anything is
  quotable. All of this assumes both judge models are still available. Best bundled with #5.
- **#3 MEND-N-018 rubric fix: not done.** It touches one item of 345, and it would unfreeze the bank
  (v2.6). It would also require re-judging that item for every SUT and writing another superseding
  paper. Worth doing only alongside a new run. Do not fold it into a broader rubric review.
- **#5 Model ceiling vs bank ceiling: open.** Answering it needs a new measurement. The cheapest
  discriminating test is #2 with stronger SUTs. If they score clearly above the tied three, the bank
  is not the ceiling at that level.
- **Open disclosure item, not yet in any paper version: judge/vendor overlap.** Opus (Anthropic)
  judged haiku (Anthropic), and GPT-5.6-Sol (OpenAI) judged gpt-4o-mini and gpt-5-mini (OpenAI). In
  the s19 per-judge columns, the two OpenAI SUTs are the only ones where Sol scores higher than Opus
  (opus − Sol = −1.66 and −0.54, against +2.28 to +4.00 for the other three). This is small and
  untested, and the paper does not mention it. Add one sentence in a new superseding paper file
  before any external version.
- **Housekeeping left to the owner or a later session:**
  - The commit and push of the s21 files.
  - The memory checkpoint named in the s21 boot prompt §5.
  - A WCF-Bench-v2 entry in the portfolio register `../ACTIVE-CRITICAL-PATHS.md`. It has none;
    its "WCF" entry describes the older v1 PPP-1 lane. This is outside this folder's scope.

## 4. How to resume

**Paste-ready prompt:**

> You are re-entering WCF-Benchmark-v2 (`CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/`),
> parked 2026-10-18 at session 21. Read `INDEX.md`, then
> `20261018-session21-PARKED-reentry-prompt.md` in full, then nothing else until the owner names a
> direction. Do not default to one of §3's items on your own initiative: being asked to re-open the
> project is not authorization for any particular direction.
>
> 1. **Verify state.** From the `CEI-Lit-WS/` repo root, run
>    `git log -1 -- COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/`. Do not use `git log -1` without the
>    pathspec: sibling projects commit to the same trunk. Run `git status --short` for this folder.
>    If the four s21 files are still uncommitted, raise that with the owner first:
>    `reports/20261018-session21-v1x-paper-draft.md`, `reports/20261018-session21-build-pdf.py`,
>    this note, and `INDEX.md`. Test baseline: `.venv-v2/bin/python -m pytest tests/ -q` gives
>    137 passed plus 1 known env failure (`test_frontier_core_task_size`). Re-check it if you touch
>    `src/` or `analysis/`.
> 2. **Once the owner picks a direction, that is the session's whole scope.**
>    - #1 (submit): write a new superseding paper file with the judge/vendor-overlap sentence plus
>      the venue template and author list the owner supplies. Rebuild the PDF; this needs typst.
>    - #2 or #5 (more SUTs or the ceiling question): write a costed design memo first, in the
>      pattern of `reports/20260725-session16-fullrun-design-memo.md`. The owner sets the SUT spend
>      cap. The judge-gap triage is mandatory before anything is quotable.
>    - #3: scoped to MEND-N-018 alone. It produces bank v2.6, re-judges that item for all SUTs, and
>      needs a superseding paper.
> 3. **Standing rules (unchanged):**
>    - Bank v2.5 is frozen at 345 scored items; the 22 episodes stay out.
>    - No deletions: use `mv` to `RECYCLE-BIN/`.
>    - Report immutability: new dated files only. Never edit an existing dated report or paper.
>    - Single-packet judging only. No cross-instrument comparison.
>    - Commits are owner-gated: explicit pathspecs only, message written to a file and committed
>      with `git commit -F`, then `git log -1 --stat`.
>    - Update `INDEX.md`'s current-state line at close.
