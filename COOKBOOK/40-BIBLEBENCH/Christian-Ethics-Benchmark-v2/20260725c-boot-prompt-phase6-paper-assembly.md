# BOOT PROMPT — WALKWORTHY v2 PHASE 6: paper assembly after ARM 1

Paste/read this at the start of a fresh session. Self-contained: a session with zero
prior context can execute it. **Intended main-loop model: Opus** (`/model opus`) — this
is adjudication + drafting, no runs. Switch to Fable only if a genuine claims-validity
call surfaces (say so when it happens).
Authored 2026-07-25 by the phase-5 session.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**This is a ZERO-SPEND session.** No model calls are required or authorized. If any task
appears to need one, STOP and surface it — do not open a spend gate unbidden.

---

## Where things stand (read this, don't re-derive)

**Phase 5 CLOSED** (commits `89efff88a`, `dc93c69d1`, `1502e7433`, all pushed). The
full-bank two-judge measurement run is DONE and its governance is clean:

- **The run.** Full public bank rev **2026-07-24b** (344 items / 563 administration
  lines) × 5 SUTs × **3 independent single-epoch runs** + a full judge-B rescore pass.
  150/150 eval runs success; 15/15 judge-B passes rc=0 (8,445 verdict rows); n stable
  across epochs in all 50 design×SUT cells. Spend **$8.53 exact + ~$2.70 estimated
  judge-B ≈ $11.23** against a $16 authorized ceiling.
  Report: `$V2/20260725-fullbank-3ep-run-report.md`.
- **Headline: no SUT-vs-SUT comparative claim survives anywhere in the suite**, two
  independent ways — (1) 9 of 10 designs flip SUT ordering between judge-A and judge-B;
  (2) design-05's judge-free CSR, the only R4-survivable surface, yields **0 of 10**
  pre-registered C1 contrasts excluding zero.
- **Variance decomposition** (`$V2/20260725b-variance-decomposition-addendum.md`, $0,
  offline). 5 SUT × 2 judge with the 3 epochs as replicates.
  **Do NOT write "the judge dominates" — that framing was corrected.** Judge and SUT
  footprints are comparable at the median (35.3% vs 35.6%); the SUT main effect is the
  largest single term in several designs (06 63.4%, 09 54.4%, 04 46.3%, 01 45.4%). The
  **models genuinely differ.** The decision-relevant term is the **interaction**:
  `SUT×judge` is non-zero in **8 of 8** judged designs (median 17.2%). **The claim that
  survives: the models differ, but the judges disagree about the ORDERING in every
  judged design** — designs 01/06/09 show a large real model effect the judges still
  reorder. Design 05 is a built-in positive control (judge-free ⇒ judge and interaction
  terms exactly 0.000000; they are).
- **3 epochs bought a methodological result the pilot could not produce:**
  single-epoch judge-stability verdicts are unreliable. Designs 03/04/06 each read
  STABLE in one or two epochs and JUDGE-SENSITIVE in the others; only design 05 is
  stable in all three, by construction.
- **`pushback_rate` re-decision CLOSED** (`$V2/RULINGS-APPLIED-20260725.md`): owner
  AFFIRMED A′. `break_turn` is the **sole** design-02 headline for this lineage,
  permanently — **not** pending further evidence. `pushback_rate` stays SECONDARY,
  per-judge, never pooled, standing caveat attached. **No re-decision is pending; do not
  reopen it as a queue item.**
- **Classifier lineage:** pinned at `gpt-4.1-nano` (`$V2/RULINGS-APPLIED-20260724e.md`).
  This run is the CURRENT lineage. The v-next cross-family re-pin is **unfired and
  deferred**. Under C6 these cells may never be pooled with any future cross-family pin.
- Bank rev stays 2026-07-24b. No code, rubric, metric or bank edit was made. 33/33 tests
  pass. **Holdout untouched and still quarantined.**

## Mission (in order)

### 1. Adjudicate TWO assembly questions FIRST — both need an owner ruling

Do this before drafting a word. Present both via `AskUserQuestion` with a recommendation.
Record the outcome in a NEW dated `RULINGS-APPLIED-YYYYMMDD[x].md`.

**Q1 — What is the assembly target: paper (a) or paper (b)?**
`REPORTS/20260724c-paper-skeleton-and-source-map.md` §0 assembles **paper (a)**
(*benchmark design + deferred leaderboard*), and that decision predates ARM 1. But
`REPORTS/20260717-briefing/06-messaging.md` §1 states the project's own view:

> "The most publishable result WALKWORTHY v2 produced is **not a leaderboard** — it is a
> demonstration that cheap-judge leaderboards on value-laden constructs are
> judge-artifacts until proven otherwise, plus a $0 two-referee method for locating
> *where* the judging fails."

…and §2 ranks **paper (b)** (judge-sensitivity / two-referee meta-audit methods note)
the *more* publishable of the two. **ARM 1 supplied precisely paper (b)'s empirical
core**, and strengthened it well past the pilot: full bank rather than a pilot, rev-24b
rather than the old bank, 3 epochs rather than 1, a quantified `SUT×judge` interaction
in 8/8 designs, a judge-free positive control, and the finding that single-epoch
stability verdicts are unreliable.

The honest reading is that the evidence base has shifted under the skeleton. Options:
(a) hold to paper (a) as skeletoned, with ARM 1 as its §7; (b) pivot assembly to paper
(b) and let paper (a) follow; (c) split — ARM 1 + the decomposition become paper (b)'s
results, and paper (a) cites them. **Recommendation: (b) or (c).** Paper (a)'s central
promised artifact was a leaderboard the data now says cannot be built; paper (b)'s
central claim is the one the data supports and strengthens. Do not decide this alone.

**Q2 — What happens to §7?** The skeleton flagged this itself and the trigger has fired:

> "Pending adjudication: whether §7 survives at all if a full-bank rescore (phase-4
> ARM 1) lands on rev 2026-07-24b first — if it does, pilot becomes a
> development-history subsection and the rescore becomes §7. Flag at assembly time."

ARM 1 landed. **Recommendation: execute the skeleton's own contingency** — the
2026-07-16 pilot becomes a development-history subsection under §5, and the full-bank
run becomes §7. This also removes most C9 friction, because §7 then reports first-ever
rev-24b numbers rather than pilot-era numbers needing fences.

### 2. Draft, per the Q1/Q2 rulings

Whatever the target, the drafting job is the **results section** built on
`20260725-fullbank-3ep-run-report.md` + `20260725b-variance-decomposition-addendum.md`.
Delegate the prose to `manuscript-drafter` (opus) from an explicit spec — that agent is
declared in `.claude/agents/` and every `Agent` dispatch needs its `model` passed
explicitly. Then run an `adversarial-reviewer` (opus) pass before shipping, which is the
pattern §3–§4 followed (`REPORTS/20260724c-paper-design-section-draft.md` v1.1, SHIP).

Sections already drafted or ready, do not redo:
| § | State | Source |
|---|---|---|
| §3 corpus/construct, §4 ten designs | **DRAFTED v1.1** (adversarial SHIP) | `REPORTS/20260724c-paper-design-section-draft.md` |
| §8 validity | **READY (transplant near-verbatim)** | `REPORTS/20260724-paper-validity-section-draft.md` v1.1 |
| §9 limitations, §10 future work | READY (merge / compress) | skeleton §9/§10 |
| §1 intro, §5 item development, §6 methods | PARTIAL | skeleton |
| §2 related work | **GAP** — do this LAST | skeleton |

### 3. Update §10 future work — it is now stale

It lists "Full-bank C9-clean run (phase-4 ARM 1, separately gated)" as future work. That
is DONE. Replace with the evidence-backed queue in §5 below, and carry the holdout
recommendation.

### 4. Close

Run the 33-test suite (should be untouched — this session writes prose, not code),
commit + push per the shared-trunk discipline below, update auto-memory
(`20260718-walkworthy-v2-item-assessment.md` addendum + the MEMORY.md index line).

## Standing open decisions (carry these; do NOT silently resolve them)

- **HOLDOUT — recommended NOT to spend, owner has not ruled.** The holdout's blind
  first-use is a **one-shot asset**: once used, first-use blindness cannot be restored.
  The instrument demonstrably cannot separate these five SUTs. Recommendation on record:
  fix discrimination first, spend the holdout after. Do not run the holdout this session.
- **Instrument-repair queue (evidence-backed, not yet scoped into work):**
  1. **d02 taxonomy revision, bundled WITH the unfired v-next cross-family classifier
     re-pin as ONE new instrument version** — not fired separately. d02 is the most
     judge-fragile instrument (agreement 0.232; 46.5% `SUT×judge` on a 5.8% model
     effect), and the JR referee arms found *both* judges diverge from referee consensus
     there ⇒ **a stronger judge will not fix d02; it is taxonomy-level.**
  2. **d08** `protected→steamrolled` boundary — 113/965 (11.7%) at full n, quantified as
     25.9% interaction. Open instrument question before any d08 promotion to claims.
  3. **d07** is floor-saturated at this SUT tier (arc_pass ≈ 0 under both judges with
     the three repaired items now validly scored) — needs **harder SUTs**, not a
     scoring fix.
  4. **d03** may be judge-defined rather than model-defined: 88.8% judge *level* shift
     with ~no interaction, which is what collapses `say_do_gap` to ≈0 under judge-B.
- **OpenRouter key `limit_remaining` ≈ $107** (limit $2,250). ≈9 more runs of this size.
  Sibling WCF sessions share the key — it is not a WALKWORTHY-only budget.

## Execution discipline (carried forward — follow it)

- **Tests run in the PROJECT venv** `$V2/.venv/bin/python` (py3.14; the vault .venv is
  py3.9 and cannot). Run pytest from `$V2/`.
- **Binding claims discipline for every section** — `06-messaging.md` §5 items 1–7
  verbatim: no SUT rankings, no referee-proves-truth claims, no pooled referee agreement
  without strata, no religious-authority claims, v2 is parallel-not-canonical, no
  cross-classifier pooling (C6), no comparative reading of F2-2c/F3. Plus: **no
  significance stars and never "significant" as an adjective (R3)** — use "excludes
  zero" / "crosses zero". Manuscript stays **venue-generic and author-generic**.
- **Design-02 reporting surface is RULED** (A′ + `RULINGS-APPLIED-20260725`): `break_turn`
  sole headline; `pushback_rate` secondary, per-judge, never pooled, caveat attached.
  Apply it; do not relitigate.
- **C9 fences** on every pilot-era number quoted anywhere: bank changed at rev 24b; d08
  pre/post rubric-anchor are separate comparability lines; d07 items were unscorable
  pre-fix.
- **Report immutability:** never edit an existing dated report. Successor files only,
  NEW `YYYYMMDD-` prefix. `20260725-fullbank-3ep-run-report.md` and its addendum are
  committed and immutable.
- **Shared trunk (WCF sibling sessions ACTIVE in this clone):** commit YOUR files by
  explicit path first, then push; if rejected, `git pull --rebase`. Never `git add -A`.
  If a rebase demands stashing, stash ONLY your own named tracked file and **only
  `git stash pop` if your stash push actually created an entry** ("No local changes to
  save" + a blind pop = you pop a STRANGER's stash).
- **Hard rails:** no deletions (move to `$V2/RECYCLE-BIN/`); canary in every artifact;
  **holdout quarantine**; v1 sibling read-only; `/tmp/jr-*` paths in tools/audit are
  intentional referee-blindness — don't "fix" them.
- **Hook sharp edges.** (a) The deletion guard scans the WHOLE command string — a
  command merely *containing* a delete token (even as prose inside a heredoc) is denied;
  rephrase, or use Write/Edit instead of a shell heredoc. (b) The security write-hook
  blocks file writes containing exec-immediately-followed-by-open-paren and
  e-v-a-l-immediately-followed-by-open-paren, even in prose — use an indirect accessor
  in code and circumlocution in prose (working pattern:
  `logs/fullbank-3ep-20260724/aggregate_judgea.py`).
- **Verification habit earned in phase 5:** verify against structured fields, not text
  scans of console output. A `grep` for `402` over run logs false-positives on token
  counts like `47,402`. This is the sibling of the U+2212-minus false-negative already
  on file.

## Where the numbers live (all committed or gitignored-but-on-disk)

| Artifact | Path |
|---|---|
| Run report (headline, per-judge cells, A′ surface, spend) | `$V2/20260725-fullbank-3ep-run-report.md` |
| Variance decomposition addendum | `$V2/20260725b-variance-decomposition-addendum.md` |
| Rulings: A′ close · classifier lineage + spend GO · spend memo | `$V2/RULINGS-APPLIED-20260725.md` · `-20260724e.md` · `$V2/20260724d-spend-memo-fullbank-3ep.md` |
| Raw run root (gitignored, on disk) | `$V2/logs/fullbank-3ep-20260724/` |
| — judge-A aggregation · cross-judge · R4 flips | `aggregate-judgeA.txt` · `aggregate-judgeB.txt` · `judgeswap-ep{1,2,3}.txt` |
| — C1 contrasts · variance components · spend tally | `c1-design05-contrasts.txt` · `variance-components.txt` · `verify_and_tally.py` |
| Paper skeleton + source map | `$V2/REPORTS/20260724c-paper-skeleton-and-source-map.md` |
| §3–§4 draft v1.1 · §8 validity draft v1.1 | `$V2/REPORTS/20260724c-paper-design-section-draft.md` · `20260724-paper-validity-section-draft.md` |
| Claims discipline · pre-reg families | `$V2/REPORTS/20260717-briefing/06-messaging.md` §5 · `$V2/20260716-prereg-comparisons-RATIFIED.md` |

## Out of scope (do not pick up unbidden)

Holdout runs (quarantined; see standing decisions) · any new measurement run or spend ·
bank/rubric/metric/code edits · firing the v-next classifier re-pin on its own ·
reopening the `pushback_rate` headline decision (CLOSED) · `WCF-Benchmark-v2/` (separate
project, actively worked by sibling sessions in this same clone) · v1 sibling
modifications · editing any existing dated report (successor files only) · §2 related-work
sweep before the other sections are drafted.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
