# BOOT PROMPT — WALKWORTHY v2 PHASE 7: adjudicate the escalated claims, then repair

Paste/read this at the start of a fresh session. Self-contained: a session with zero prior
context can execute it. **Intended main-loop model: Opus** (`/model opus`). This is
adjudication + a $0 offline computation + prose repair. No measurement runs.
Authored 2026-07-25 by the phase-6 session.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**This is a ZERO-SPEND session.** Everything below runs offline on data already on disk.
If any task appears to need a model call or a run, STOP and surface it — do not open a
spend gate unbidden. (The one exception you may *propose*, not take, is §5's citation-gap
sweep, which needs web search.)

---

## Where things stand (read this, don't re-derive)

**Phase 6 CLOSED** (commit `e05322b4f`, pushed). Both manuscripts exist; both were
adversarially reviewed; 35 verified factual fixes were applied. What remains is **not**
drafting — it is two owner adjudications and the repair work they gate.

- **RULING (`RULINGS-APPLIED-20260725b.md`):** Q1 = **(c) SPLIT, both papers live**
  (evidence-division table + cross-citation rule inside). Q2 = **execute the skeleton's
  contingency** — pilot → development history under §5, ARM 1 → §7.
- **The manuscripts** live in `$V2/REPORTS/20260725-manuscripts/`:
  | File | Words | Review verdict |
  |---|---:|---|
  | `20260725-paper-a-walkworthy-benchmark-v0.1.md` | 18,094 | SHIP-WITH-FIXES (applied) |
  | `20260725-paper-b-judging-the-judges-v0.1.md` | 13,317 | **DO-NOT-SHIP → DO-NOT-CIRCULATE** |
- **BOTH MANUSCRIPTS ARE GENERATED FILES.** Never hand-edit them. Edit `parts/*.md`, then
  `./.venv/bin/python REPORTS/20260725-manuscripts/assemble.py`. See that directory's
  `README.md` for the section→source map.
- **Three claims-validity questions were escalated, not resolved**
  (`$V2/REPORTS/20260725-manuscripts/20260725-ESCALATION-claims-validity.md`). Read that
  memo before touching anything. One is already corrected; two are OPEN and gate paper (b).
- **What is NOT in question.** Two independent reviewers recomputed the variance
  decomposition, all C1 intervals, every median and footprint, the run shape, spend, bank
  census and transplant fidelity — and conceded all of them. **No arithmetic error exists.**
  Every open issue is *interpretive*.

### The three escalated findings, in one table

| # | Finding (all independently verified) | State |
|---|---|---|
| Q1 | **Design 07 has no judge-A ordering at all** — 0.0000 on all five systems in ep1 and ep2. Its recorded "flip" is a stable-sort tie-break artefact. | **CORRECTED** in both papers to *eight of the nine judged designs*. Immutable run report still says "nine of ten" → needs a successor note (§3 below). |
| Q2 | **The flip criterion is exact five-way permutation equality** on unrounded point estimates, stable-sort tie-break, no interval. A single adjacent transposition counts as a full flip. | Criterion now **disclosed** in §4.1. Its **calibration is OPEN** → RULING 2 below. |
| Q3 | **Variance shares carry no df-proportional no-effect baseline.** Against E[share] = 13.79%, **four of eight interactions sit at or below chance (03, 04, 06, 09)** — and 06/09 are two of the three headline exemplars. | **OPEN → RULING 1 below.** This is the one that decides whether paper (b) is a light revision or a re-framing. |

## Mission (in order)

### 1. Get TWO owner rulings BEFORE editing prose

Present both via `AskUserQuestion` with the recommendation stated. Record the outcome in a
NEW dated `RULINGS-APPLIED-20260726[x].md` (or whatever today's date is).

---

**RULING 1 — Do variance shares get a df-proportional no-effect baseline?**

The layout is `SS_total (df 29) = SS_SUT (4) + SS_judge (1) + SS_SUT×judge (4) + SS_error (20)`.
Sums of squares are non-negative and, under a null of no effect, have expectation
proportional to df:

| Term | df | E[share] under no effect |
|---|---:|---:|
| SUT | 4 | **13.79%** |
| judge | 1 | 3.45% |
| SUT × judge | 4 | **13.79%** |
| error | 20 | 68.97% |

Against that line, the reported interactions are:

| design | SUT×judge | vs 13.79% | SUT | note |
|---|---:|---|---:|---|
| 02 | 46.5% | above | 5.8% | strongest genuine case |
| 08 | 25.9% | above | 9.1% | |
| 10 | 25.8% | above | 25.8% | |
| 01 | 23.0% | above | 45.4% | the only surviving "large effect, still reordered" exemplar |
| 06 | 11.4% | **BELOW** | 63.4% | **currently cited as a headline exemplar** |
| 09 | 9.9% | **BELOW** | 54.4% | **currently cited as a headline exemplar** |
| 04 | 4.9% | **BELOW** | 46.3% | |
| 03 | 1.4% | **BELOW** | 6.6% | |

**The genuine tension.** Rule R3 forbids significance testing and significance language. A
df-proportional expectation is arguably *descriptive* — no null hypothesis is rejected, no
p-value, no decision rule — in which case R3 permits it. But it is inferential in spirit,
and a reviewer could fairly say the project cannot both refuse significance testing and
lean on a null comparison.

**Recommendation: ADOPT it, as a descriptive reference line, with no significance language.**
Reason: withholding it is the *less* honest option. Raw shares invite a reader to treat a
9.9% interaction as evidence when it is below what pure epoch noise produces. Adopting it
costs two sentences and a table column.

**If adopted, these consequences follow and must be applied:**
- Drop **"non-zero in 8 of 8"** as an evidential claim everywhere (an SS on a continuous
  metric is almost surely non-zero; the claim carries no information).
- Restrict the *"large model effect, judges still reorder it"* narrative to **design 01**
  alone — it is the only exemplar clearly above the line.
- Re-ground designs 06 and 09 in the flip result rather than the interaction term — **but
  see RULING 2 first**, because design 06's flip is a single adjacent transposition.
- Note that %SUT is also below 13.79% in designs 02, 03 and 08, so **"the models genuinely
  differ" is design-specific, not suite-wide.**

**What survives either way — do not lose this.** The operational conclusion is robust and
rests on two independent legs that Q3 does not touch: (1) the ordering flips, and (2) the
judge-free surface yields 0 of 10 contrasts excluding zero. **No SUT-vs-SUT claim is
licensed.** What Q3 threatens is only the *mechanistic story* that judge-ordering
disagreement is what causes it *in every judged design*. The target claim after adoption:

> *The models differ on most designs. On a minority of designs the judges clearly disagree
> about the ordering; on the rest the systems are too tightly spaced for either judge to
> resolve. Either way, no comparative claim survives the swap.*

---

**RULING 2 — Do we replace the binary flip verdict with a graded one?**

The criterion counts any permutation as a flip. Design 06 epoch 1 is a **single adjacent
transposition** (A: `gemini 0.9180 > deepseek 0.8810 > …`; B: `deepseek 0.9630 >
gemini 0.9392 > …`; positions 3–5 identical), and that lone swap is what makes design 06 a
"flip" and a headline exemplar. Ties are broken arbitrarily in roughly 10 of 27 judged
design-epoch cells, including design 09 epoch 3.

**Recommendation: compute Kendall's τ per design × epoch between the two judges' orderings.
It is $0, fully offline, from cells already in `logs/fullbank-3ep-20260724/judgeswap-ep{1,2,3}.txt`.**
With five systems, τ is exactly the graded scale needed:

| discordant pairs (of 10) | τ |
|---:|---:|
| 0 (identical) | +1.00 |
| 1 (one adjacent swap) | **+0.80** |
| 2 | +0.60 |

Report τ **alongside** the binary verdict, not instead of it — the binary verdict is what
rule R4 is written in terms of. Also flag the tie-affected cells explicitly.

**Do NOT adopt** the reviewer's *"P(preserved) = 1/120 under pure noise, so the test has no
power"* argument. The phase-6 session examined and **rejected** it: the two judges score the
same stored transcripts, so their orderings are correlated by construction and a
uniform-random-permutation null is far too permissive. Directionally the reviewer is right
that the test is uncalibrated; the specific 1/120 figure should not enter any artifact.

### 2. Execute the graded-flip computation (only if RULING 2 says yes)

Write `logs/fullbank-3ep-20260724/kendall_tau.py` (new file; the run root is gitignored but
on disk) reading the same cells the swap tool reads. Emit τ per design × epoch, plus the
count of discordant pairs and a tie flag. **Delegate to `stats-runner` (sonnet), passing
`model` explicitly.** Then hand-check two cells against the tables above before using it.

### 3. Write successor correction notes for the IMMUTABLE artifacts

**Report immutability is absolute: never edit a dated report. Successor files only.**

| Artifact | What it still says | Successor needed |
|---|---|---|
| `20260725-fullbank-3ep-run-report.md` §0, §3 | "Nine of ten designs flip" | correction note: design 07 has no judge-A ordering (0.0000 × 5 in ep1/ep2); the count is **eight of nine judged** |
| `20260725b-variance-decomposition-addendum.md` §3 | "non-zero in 8 of 8"; 06/09 as exemplars | addendum adding the df baseline and re-scoping the exemplars (**only if RULING 1 adopts**) |
| `RULINGS-APPLIED-20260725b.md` §"Framing correction" | restates "non-zero in 8 of 8" | a **new dated ruling** supersedes it — never amend a ruling silently |

### 4. Apply the rulings to the manuscripts

Edit `parts/*.md`, never the assembled files. Then rebuild and lint:
```
./.venv/bin/python REPORTS/20260725-manuscripts/assemble.py
./.venv/bin/python REPORTS/20260725-manuscripts/lint_claims.py REPORTS/20260725-manuscripts
```

- **Paper (b):** abstract, §1 ("Third"), §5.3, §5.4 carry the affected claims. Clear the
  **DO-NOT-CIRCULATE banner in `parts/pb-00-frontmatter.md`** only when both rulings are
  recorded and applied.
- **Paper (a):** one sentence in §9 cites the 8-of-8 interaction — adjust with RULING 1.
  Nothing else in paper (a) is blocked.
- **Free corroboration worth adding to paper (b) §5.5** (verified, $0): design 05 is
  judge-free, so its two judge levels are exact duplicates and the layout collapses to
  5 SUT × 3 epochs, giving E[%SUT] = 4/14 = **28.6%**. Observed **%SUT = 27.4%**. **The
  positive control's own system main effect sits at its null expectation** — independent
  corroboration that the judge-free surface genuinely does not separate these systems, and
  a direct strengthening of the "no concealed ranking" argument.
- After ANY corrected phrase, **re-grep it across all ten part files.** Phase 6's regression
  check caught "nine of ten" recurring in six further sentences beyond the abstract.

### 5. Propose (do not execute) the citation-gap sweep

10 `[CITATION NEEDED]` markers remain — 3 in paper (a) §2, 7 in paper (b) §2. They are
**honest gaps, not omissions**: the drafting agents had no web access by design, so §2 cites
only works verifiable in the vault. Closing them needs external search. **Surface this as a
proposal with a scope and a channel; do not open it unbidden.**

Binding if it is ever authorized: every citation must resolve to a document actually read.
See `20260725-citation-metadata-findings.md` — two vault extracts contain documents that are
**not** the work their filename names, so a filename-derived citation would be fabricated.

### 6. Close

Run the 33-test suite (should be untouched — this session writes prose and one offline
script). Commit + push per the shared-trunk discipline below. Update auto-memory
(`20260725b-walkworthy-v2-phase6-assembly.md` addendum + the `MEMORY.md` index line).

## Standing open decisions (carry these; do NOT silently resolve them)

- **HOLDOUT — recommended NOT to spend, owner has not ruled.** Blind first-use is a
  **one-shot asset**; once used it cannot be restored. The instrument demonstrably cannot
  separate these five systems. Recommendation on record: fix discrimination first, spend
  after. **Phase 6's findings strengthen this, not weaken it.** Do not run the holdout.
- **Instrument-repair queue** (unchanged, evidence-backed, not yet scoped into work):
  1. **d02 taxonomy revision bundled WITH the unfired cross-family classifier re-pin as ONE
     instrument version** — never fired separately (C6). d02 is the most judge-fragile
     instrument (agreement 0.232; 46.5% interaction on a 5.8% model effect) and both judges
     diverge from referee consensus there ⇒ **a stronger judge will not fix d02.**
     *New from phase 6:* the pinned classifier and judge-A are the **same model instance**,
     so "judge-A character" on d07 is confounded with classifier character by construction.
  2. **d08** `protected→steamrolled` — 113/965 (11.7%) at full n. Open before any promotion.
  3. **d07** floor-saturated at this tier — needs **harder SUTs**, not a scoring fix.
  4. **d03** may be judge-defined: 88.8% judge *level* shift with ~no interaction.
- **`pushback_rate` is CLOSED** (A′ affirmed, `RULINGS-APPLIED-20260725`). `break_turn` is
  the sole d02 headline permanently. **Do not reopen it as a queue item.**
- **Vault citation-metadata remediation** — four verified defects recorded in
  `20260725-citation-metadata-findings.md` §6. Touches the papers vault, which is a
  **different project scope**. Needs its own authorization; do not pick it up here.
- **OpenRouter key `limit_remaining` ≈ $107.** Sibling WCF sessions share it.

## Execution discipline (carried forward — follow it)

- **Tests run in the PROJECT venv** `$V2/.venv/bin/python` (py3.14; the vault .venv is py3.9
  and cannot). Run pytest from `$V2/`.
- **Binding claims discipline** — `06-messaging.md` §5 items 1–7 verbatim: no SUT rankings,
  no referee-proves-truth claims, no pooled referee agreement without strata, no
  religious-authority claims, v2 is parallel-not-canonical, no cross-classifier pooling (C6),
  no comparative reading of F2-2c/F3. Plus **R3: no significance stars, never "significant"
  as an adjective** — use "excludes zero" / "crosses zero". Venue- and author-generic.
- **Never write "the judge dominates."** Judge and SUT footprints are comparable at the
  median (35.3% vs 35.6%). The models genuinely differ — subject to RULING 1's narrowing.
- **`lint_claims.py` is a gate, but validate it before trusting a PASS.** Phase 6's reviewer
  correctly found its allowance window so permissive it hid real defects. It is now
  sentence-scoped and was re-validated against probe files of deliberate violations.
  **If you change a rule, re-validate the same way** — a linter never shown to catch
  anything proves nothing.
- **Patch scripts must assert exactly one match** before writing. A silent no-op from prose
  drift otherwise leaves the defect in place.
- **Transplants:** paper (a) §3/§4/§8 come from immutable feeder drafts. Post-transplant
  fixes go in the documented `TRANSPLANT_PATCHES` table in `assemble.py`, each asserting a
  single match — never hand-edit the feeder or the generated file.
- **Shared trunk (WCF sibling sessions ACTIVE in this clone):** commit YOUR files by explicit
  path, then push; if rejected, `git pull --rebase`. **Never `git add -A`.** If a rebase
  demands stashing, stash ONLY your own named file and **only pop if your stash push
  actually created an entry** ("No local changes to save" + a blind pop = you pop a
  stranger's stash).
- **Hard rails:** no deletions (move to `$V2/RECYCLE-BIN/`); canary in every artifact;
  **holdout quarantine**; v1 sibling read-only; `/tmp/jr-*` paths are intentional
  referee-blindness — don't "fix" them.
- **Hook sharp edges.** (a) The deletion guard scans the WHOLE command string — a command
  merely *containing* a delete token, even as prose in a heredoc, is denied. **Write commit
  messages to a file and use `git commit -F`**; that keeps the prose out of the command
  string entirely. (b) The security write-hook blocks files containing
  exec-immediately-followed-by-open-paren and e-v-a-l-immediately-followed-by-open-paren,
  even in prose — circumlocute.
- **Verify against structured fields, not text scans.** A grep for `402` over run logs
  false-positives on token counts like `47,402`; the U+2212-minus false-negative is the
  sibling trap already on file.

## Where things live

| Artifact | Path (under `$V2/`) |
|---|---|
| **Escalation memo — READ FIRST** | `REPORTS/20260725-manuscripts/20260725-ESCALATION-claims-validity.md` |
| Fixes already applied (phase 6) | `REPORTS/20260725-manuscripts/20260725-review-fixes-applied.md` |
| Assembly map + rebuild instructions | `REPORTS/20260725-manuscripts/README.md` |
| Builder · claims linter | `REPORTS/20260725-manuscripts/assemble.py` · `lint_claims.py` |
| Part files (EDIT THESE) | `REPORTS/20260725-manuscripts/parts/*.md` |
| Governing rulings | `RULINGS-APPLIED-20260725b.md` (assembly) · `-20260725.md` (A′) · `-20260724e.md` (classifier pin) |
| Run report · decomposition addendum (both IMMUTABLE) | `20260725-fullbank-3ep-run-report.md` · `20260725b-variance-decomposition-addendum.md` |
| Flip-test raw cells (gitignored, on disk) | `logs/fullbank-3ep-20260724/judgeswap-ep{1,2,3}.txt` |
| The flip tool itself | `tools/audit/pilot_judge_swap.py` (~line 181) |
| Claims discipline · pre-reg families | `REPORTS/20260717-briefing/06-messaging.md` §5 · `20260716-prereg-comparisons-RATIFIED.md` |
| Vault citation defects | `REPORTS/20260725-manuscripts/20260725-citation-metadata-findings.md` |

## Out of scope (do not pick up unbidden)

Holdout runs (quarantined) · any new measurement run or spend · bank/rubric/metric/code edits
· firing the v-next classifier re-pin on its own · reopening `pushback_rate` (CLOSED) ·
editing ANY existing dated report (successor files only) · hand-editing either assembled
manuscript (edit parts + rebuild) · the vault citation-metadata remediation (different
project scope) · the §2 citation-gap sweep without authorization ·
`WCF-Benchmark-v2/` (separate project, actively worked by sibling sessions in this clone) ·
v1 sibling modifications.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
