# BOOT PROMPT — WALKWORTHY v2 RE-ENTRY · PROJECT CLOSED AT PHASE 7

Paste/read this at the start of a fresh session. Self-contained: a session with zero prior
context can act on it. Authored 2026-07-29 by the §2-citation-sweep session, superseding the
phase-6 and phase-7 boot prompts as the current entry point.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**Intended main-loop model: Opus.** Escalate to Fable only if a genuine claims-validity call
surfaces — and say so when it happens.

**This is a ZERO-SPEND, ZERO-QUEUE session by default.** No model calls, no runs, no retrieval
are authorized. If a task appears to need spend, STOP and surface it.

---

## ⚠ READ THIS BEFORE ANYTHING ELSE — this is NOT a work queue

**The project is CLOSED at phase 7** (`RULINGS-APPLIED-20260729b.md`). Every remaining work
item was **deliberately deferred by owner decision on 2026-07-29**. There is no open queue, no
pending phase, and nothing to pick up.

This file exists so that a re-entering session can (a) establish state without re-deriving it
and (b) recognise that the correct default action is **to do nothing and ask**. Arriving with
this file is not authorization to start work.

**Do NOT re-raise any deferred item as though it were open.** The three deferrals are listed in
§5 with what authorizing each would actually require. An informational question about them
("what's left?", "what's next?") requires enumeration, **not execution**.

## 1 Verify state before acting on ANY boot prompt — including this one

The 2026-07-29 sweep session was launched against a boot prompt that had **already been fully
executed two phases earlier**, along with an unlisted successor. Re-running it would have
re-adjudicated settled questions and written a duplicate dated ruling into an append-only
ledger whose convention is *newest dated file wins* — silent corruption, not a loud failure.

**Boot prompts are snapshots of intent, not state.** Cheap 30-second check before you act:

```bash
cd CEI-Lit-WS                                     # the git repo root is CEI-Lit-WS, not the vault root
git fetch origin && git log --oneline -8 -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
ls -1 COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/RULINGS-APPLIED-*.md | tail -5
git status -sb -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
```

If a newer `RULINGS-APPLIED-*` or boot prompt exists than the ones named here, **that file wins
and this one is stale.** A sibling WCF-Benchmark-v2 project is actively worked by other sessions
in this same clone, so the trunk moves under you; expect ~1,800 dirty WCF files that are **not
yours**.

## 2 Where things stand — read, do not re-derive

**Both manuscripts are assembled, adjudicated, and citation-complete.**

| Artifact | State |
|---|---|
| Paper (a) — instrument + validity | **18,686 words**, §1–§10, v0.1 adjudicated draft |
| Paper (b) — *Judging the Judges* | **15,190 words**, §1–§7, v0.1 adjudicated draft |
| §2 citation gaps | **0** — all 8 closed 2026-07-29 (`RULINGS-APPLIED-20260729.md`) |
| Test suite | 33/33 pass |
| Claims linter | 16 files, 0 blockers |
| Holdout | quarantined, **UNSPENT, ruling CLOSED** |
| Total measurement spend to date | ≈$11 ($8.53 metered + estimated judge-B rescore) |

**Both manuscripts are GENERATED FILES.** Edit `REPORTS/20260725-manuscripts/parts/*.md`, then
rebuild. Hand-editing a manuscript is silently discarded at the next build.

```bash
cd $V2
./.venv/bin/python REPORTS/20260725-manuscripts/assemble.py                        # parts -> manuscripts
./.venv/bin/python REPORTS/20260725-manuscripts/lint_claims.py REPORTS/20260725-manuscripts
./.venv/bin/python -m pytest -q                                                    # 33 tests
```

**Tests and builds run in the PROJECT venv** `$V2/.venv/bin/python` (py3.14). The vault `.venv`
is py3.9 and cannot run them.

## 3 The scientific result, in the form that is licensed

**No SUT-vs-SUT comparative claim survives anywhere in the suite.** Two independent legs, both
unaffected by any later re-adjudication:

1. **Ordering flips** — eight of the *nine judged* designs flip system ordering between judge-A
   and judge-B. (Not "nine of ten": design 07 yields no judge-A ordering at all, and design 05
   is judge-free by construction. See `20260725e-run-report-correction-note.md`.)
2. **The judge-free surface** — design 05's mechanically-parsed CSR, the only R4-survivable
   surface, yields **0 of 10** pre-registered contrasts excluding zero.

**The binding suite-wide claim, quoted verbatim from `RULINGS-APPLIED-20260725c.md` RULING 1:**

> *The models differ on most designs. On a minority of designs the judges clearly disagree
> about the ordering; on the rest the systems are too tightly spaced for either judge to
> resolve. Either way, no comparative claim survives the swap.*

Riders that travel with it, and which are easy to over-claim:
- **Never write "the judge dominates."** Judge and system footprints are comparable at the
  median (35.3% vs 35.6%). This prohibition is BLOCKER-enforced by the linter.
- **"Non-zero in 8 of 8" is WITHDRAWN as evidential.** An SS is almost surely non-zero, and
  four of the eight interactions sit at or below the df-proportional line (13.79% for SUT and
  SUT×judge). Variance shares are read against that line, **descriptively — never with
  significance language.**
- **"Large model effect the judges still reorder" = design 01 ALONE.** Designs 06 and 09 are
  re-grounded in graded flip verdicts (d06's epoch-1 flip is a single adjacent transposition,
  τ = +0.80; epochs 2–3 are identical orderings).
- **"Models genuinely differ" is design-specific**, not suite-wide — %SUT sits below the line
  in designs 02, 03 and 08.
- **Flip verdicts: binary (R4) plus Kendall τ alongside.** The 1/120 chance-rate argument is
  **REJECTED on record** — the judges score the same stored transcripts, so a
  uniform-random-permutation null is far too permissive. Do not let it back in.
- **Design 02:** `break_turn` is the sole headline, **permanently**. `pushback_rate` stays
  secondary, per-judge, never pooled, caveat attached. CLOSED — do not relitigate.

## 4 Binding constraints — apply without being asked

- **Claims discipline:** `REPORTS/20260717-briefing/06-messaging.md` §5 items 1–7 verbatim — no
  SUT rankings, no referee-proves-truth claims, no pooled referee agreement without strata, no
  religious-authority claims, v2 is parallel-not-canonical, no cross-classifier pooling (C6),
  no comparative reading of F2-2c/F3.
- **R3:** no significance stars, and **never "significant" as an adjective.** Use "excludes
  zero" / "crosses zero". The linter BLOCKERs on it.
- **Manuscripts stay venue-generic and author-generic.** No venue or authorship decision has
  been made and none is authorized.
- **Report immutability:** never edit an existing dated report or boot prompt. **Successor files
  only**, new `YYYYMMDD[letter]-` prefix, where the letter continues the *shared day sequence*
  across all artifact types (today's a/b/c are `RULINGS-APPLIED-20260729`, `-20260729b`, and
  this file).
- **Search-provenance rule** (`RULINGS-APPLIED-20260729.md` §4): **retrieval does not confer
  provenance.** A source found via search is not citable until its publication apparatus —
  DOI, ISSN, editorial board, peer-review attestation — has been inspected **directly**. A
  search summary will restate an unvetted working paper's claim as established fact; one such
  source was inspected and **REJECTED** this lineage and is recorded as rejected in the paper
  (b) ledger so it is not silently rediscovered. Phase 6's control ("give the drafter no web
  access") does **not** cover a web-enabled main loop.
- **Cite from documents, never from paths.** Five vault citation-metadata defects are on record;
  several vault filenames carry an author token that disagrees with the work's printed byline,
  and at least one record fronts an **empty `pages: 0` extract**. A populated metadata record
  does not imply a readable document.
- **Verify against structured fields, not text scans.** A grep for `402` over run logs
  false-positives on token counts like `47,402`; the U+2212-minus false-negative is the same
  family; and counting a sentence that *describes* a marker convention as an instance of the
  marker is what produced the wrong "10 markers" figure (true count: 8).
- **Hard rails:** no deletions — move to `$V2/RECYCLE-BIN/` · canary in every artifact ·
  **holdout quarantine** · v1 sibling is read-only · `/tmp/jr-*` paths in tools/audit are
  intentional referee-blindness, do not "fix" them.
- **Hook sharp edges:** (a) the deletion guard scans the **whole** command string, so a command
  merely *containing* a delete token — even as prose in a heredoc — is denied; use Write/Edit
  instead. (b) The security write-hook blocks the two exec-style tokens
  (word-immediately-followed-by-open-paren) even inside prose; circumlocute.
- **Shared trunk:** commit **your** files by explicit path, never `git add -A`. Then push; if
  rejected, `git pull --rebase`. **Never pipe `git commit`** through anything — a truncating
  pipe kills it mid-pre-commit-hook and can look like success while committing nothing. Write
  the message to a file, `git commit -F <file>`, then verify with `git log -1 --stat`.

## 5 The three DEFERRALS — on record, NOT open

From `RULINGS-APPLIED-20260729b.md` §"Deferrals recorded". **Do not re-raise these as open
items.** Each needs explicit owner authorization to become work.

1. **Instrument-repair queue — DEFERRED, project stays closed.** On record, unscoped: d02
   taxonomy revision **bundled with the unfired v-next cross-family classifier re-pin as ONE
   instrument version** (C6 forbids pooling across classifier pins) · d08
   `protected→steamrolled` boundary, 113/965 = 11.7%, 25.9% interaction · d07 is floor-saturated
   at this tier and needs **harder SUTs**, not a scoring fix · d03 may be judge-defined (88.8%
   judge level shift with ~no interaction). **Authorizing this means opening a new instrument
   version, not a patch** — and it is the only route to the holdout release condition.
2. **Vault citation-metadata remediation — DEFERRED** (papers-vault scope, needs its own
   authorization). Five recorded defects: four in
   `REPORTS/20260725-manuscripts/20260725-citation-metadata-findings.md` §6, plus the
   Gospel-Coalition empty-extract defect in `RULINGS-APPLIED-20260729.md` §5. The
   cite-from-documents discipline already fences the manuscripts, so this is vault hygiene, not
   a manuscript blocker.
3. **Holdout — CLOSED, quarantine RATIFIED. Do not spend.** Not a deferral to revisit but a
   ruling to cite. Its blind first use is a one-shot asset and would currently be consumed to
   reconfirm a known negative. **Release condition:** the quarantine holds until a repaired
   instrument version demonstrates discrimination on public data — at minimum a judged surface
   that survives R4, or a judge-free surface whose pre-registered contrasts exclude zero.
   Successor sessions cite `RULINGS-APPLIED-20260729b.md`, **not** the old recommendation.

## 6 Genuinely unfinished, and also unauthorized

Listed for completeness so a future session need not rediscover them. **Neither is a queue
item; both need an owner decision to start.**

- **Supplementary material is not assembled** — IVR-1.1 rater protocol, PE-1..25 ledger,
  per-design agreement tables, consolidated defect ledger.
- **No venue and no authorship decision.** Both manuscripts are deliberately generic. Nothing
  about submission, preprinting, or DOI minting is authorized.

## 7 Where everything lives

| Artifact | Path (under `$V2/`) |
|---|---|
| Rulings ledger — **newest dated file is authoritative** | `RULINGS-APPLIED-*.md` (through `-20260729b.md`) |
| Both manuscripts + parts + assembler + linter | `REPORTS/20260725-manuscripts/` (see its `README.md` first) |
| Run report · variance addendum | `20260725-fullbank-3ep-run-report.md` · `20260725b-variance-decomposition-addendum.md` |
| Successor corrections to those immutable reports | `20260725e-run-report-correction-note.md` · `20260725f-variance-decomposition-df-baseline-addendum.md` |
| Citation-metadata defect ledger | `REPORTS/20260725-manuscripts/20260725-citation-metadata-findings.md` |
| Raw run root (gitignored, on disk) | `logs/fullbank-3ep-20260724/` — incl. `kendall_tau.py`, `20260725-kendall-tau.txt` |
| Claims discipline · pre-registered families | `REPORTS/20260717-briefing/06-messaging.md` §5 · `20260716-prereg-comparisons-RATIFIED.md` |
| Superseded entry points (historical, do not execute) | `20260725c-boot-prompt-phase6-*.md` · `20260725d-boot-prompt-phase7-*.md` |

## 8 Out of scope — do not pick up unbidden

Holdout runs (ruled, quarantined) · any new measurement run or spend · bank, rubric, metric or
code edits · firing the v-next classifier re-pin on its own · reopening `pushback_rate` (CLOSED)
or the holdout (CLOSED) · the 1/120 chance-rate argument (REJECTED) · `WCF-Benchmark-v2/`
(separate project, actively worked by sibling sessions in this same clone) · v1 sibling
modifications · editing any existing dated report or boot prompt (successor files only) ·
venue/authorship/preprint decisions.

---

**If you are unsure whether something is authorized: it is not.** Enumerate, recommend, and ask.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
