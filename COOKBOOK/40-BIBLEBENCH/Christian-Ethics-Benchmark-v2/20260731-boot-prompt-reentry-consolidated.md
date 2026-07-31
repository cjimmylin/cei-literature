# BOOT PROMPT — WALKWORTHY v3, consolidated re-entry (STOPPED at Gate A; paper-c shipped)

Read this at the start of a fresh session. Self-contained: a session with zero prior
context can act correctly from it. Authored 2026-07-31.

**Supersedes, by consolidation, `20260730j-boot-prompt-reentry-gate-a-stopped.md` and its
addendum `20260730m-entrypoint-addendum-paper-c.md`** — nothing in either is retracted;
this file merges them and adds the paper-c completion so re-entry is a one-file read.
Earlier entry points (`20260730-boot-prompt-v3-tier0-continue.md`,
`20260729c-boot-prompt-reentry-project-closed.md`) remain valid constraint references.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**SPEND POSTURE: $0. Nothing is authorized to spend. There is NO open work queue.**

---

## 1. Verify state before acting (30 seconds, do not skip)

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS   # git repo root is CEI-Lit-WS
git fetch origin && git log --oneline -5 -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
ls -1 COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/RULINGS-APPLIED-*.md | tail -3
git status -sb -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
```

**State at authoring:** trunk clean and in sync at `0068d7128`. If a `RULINGS-APPLIED-*`
newer than `-20260729d` exists, read it FIRST — it wins over this file and may reopen
work. A sibling **WCF-Benchmark-v2** project is actively worked by other sessions in this
same clone (including on 2026-07-31); expect unrelated dirty files that are not yours.

## 2. Governing state

**STOPPED at Gate A.** `$V2/20260730i-gate-a-memo.md` is the governing synthesis, read
together with `$V2/20260730l-paper-c-adversarial-review-adjudication.md`, which corrects
two of its figures (see §4 items 10–11). The pre-committed stop criterion — no design
shows a within-item contrast that is both unsaturated and judge-order-stable — fired on
the Tier 0 evidence.

| Thing | Status |
|---|---|
| Tier 0 (offline diagnostics, ten items + Gate A memo) | COMPLETE (`d1e63bc6e`) |
| Tiers 1 / 2 / 3 | CLOSED — only a new `RULINGS-APPLIED-*` reopens |
| Holdout | QUARANTINED — Gate B never reached; never set WALKWORTHY_ALLOW_HOLDOUT |
| Paper-c (instrument-diagnostics manuscript, decision-menu item 1) | COMPLETE through adversarial review — v0.2 at `e6958d649` |
| Decision-menu items 2 (defect-repair ruling) and 3 (reopen a tier) | OPEN, owner's alone |

**Paper-c detail:** owner-commissioned; drafted from the Tier 0 artifacts; refute-first
review returned 4 blocker / 7 major / 12 minor findings; all 23 adjudicated ACCEPTED and
applied. Manuscript:
`REPORTS/20260730k-diagnostics-manuscript/20260730k-paper-c-instrument-diagnostics-v0.1.md`
(filename keeps v0.1 per paper-a practice; the internal banner is v0.2). Nothing further
is pending on it.

## 3. What a session may do WITHOUT a new ruling

- Answer owner questions from the committed artifacts (map in §7). Cite; do not rerun.
- Integrity checks, $0 and read-only:
  `cd $V2 && ./.venv/bin/python tools/verify_instrument.py` (expect ALL PASS 51/51) and
  `./.venv/bin/python -m pytest -q` (expect 103 passed). Project venv is `$V2/.venv`
  (py3.14); the vault-level .venv is py3.9 and cannot run any of this.
- Maintain this entry-point chain if the owner issues new rulings (new dated successor
  files only; never edit dated files).
- If the owner opens decision-menu item 2 or 3, the ruling defines the queue; until then
  do not draft, probe, fix, or "prepare" anything for those items.

## 4. Facts a fresh session must NOT re-derive (it will get them wrong)

1. **The test gate is 103/103, not 33/33** (70 characterization tests added by T0-9).
2. **Exemplars are not gold references** — spec-bank items run live per system
   (`tools/convert_banks.py:490`). The `walkworthy_inspect/metrics.py` docstring calling
   them "gold-standard" is KNOWN WRONG and deliberately uncorrected (code edits gated).
3. **The metric module is `walkworthy_inspect/metrics.py`** — there is no tools/metrics.py.
4. **d09 has 270 complete triangles** (~524 was a per-judge double-count); the
   symmetry-index 1.0 "saturation" was the known-wrong in-log stored value; the
   recomputed index is 0.69–0.91.
5. **The published d05 "0 of 10" scope is corrected by `20260730d`**: computed
   pooled-strata, labeled pre-registered; stratum-a-only gives the identical headline;
   the C5 floor is worded in admins and passes (19 bank items, 54–55 admins per cell).
6. **d03 has no SUT-side forced-choice parser** — extraction operates on the judge's
   JSON (0.9931 non-exemplar; ep1 anchor 143/145; six failures, one synonym-key cause).
7. **The nano judge pin is a run-time override; the code default is gpt-4.1-mini** — an
   unattended default rerun is a DIFFERENT instrument. Machine-checked via
   `INSTRUMENT.json` + `tools/verify_instrument.py` (instrument `WW-v2-20260724b`).
8. **Known item defects, documented and deliberately unfixed:** WW-05-L01
   coverage-starved (no scored administration for three systems in any epoch);
   WW-03-L02 zero-pass under both judges; five twinless d04 items (paired
   denominator 24).
9. **The d02 cold_open × break_turn trap stays dead** (single-turn arm admits only 0.0
   and 1.0; documented as a rejected alternative in `20260730f` §6, pinned by a test).
10. **The d02 break-position "premium" was NEVER judge-order-stable on committed data**:
    Spearman 0.00 / Kendall −0.20. The Gate A memo's "rho ≈ +0.7" was a planning-era
    figure, unreproducible from the run — corrected in `20260730l`. Its second
    correction: d05 ceiling count is 12 of 28 non-exemplar items, not 12 of 32. Neither
    changes the Gate A decision.
11. **Tables are authoritative over prose in the Tier 0 reports** (established case:
    `20260729e` prose says judge-B d07 labels sit "flat 76–85%"; its own table's range
    is 68.1–85.5, minimum at turn 3). And only six of the ten audit items had true G0
    reproduce-a-published-number gates (the recompute items) — never claim all ten.
12. **The d02 measure substitution is not a prereg deviation**: terminal-state replacing
    break_turn was pre-committed in `RULINGS-APPLIED-20260729d` (lines 81–86) before any
    Tier 0 execution, and is outcome-irrelevant.

## 5. Binding constraints (unchanged, carried forward)

- $0 unless a ruling says otherwise. No model calls of any kind.
- Holdout CLOSED; guard in `walkworthy_inspect/datasets.py` stays intact.
- `pushback_rate` stays CLOSED; renaming a closed statistic to relitigate it is
  prohibited. C6: the d02 taxonomy revision ships bundled with the classifier re-pin as
  ONE instrument version.
- Ablations are never WALKWORTHY numbers; promoting any alternative read-out is a new
  instrument version.
- **R3 (linter-enforced BLOCKER):** no significance stars — never a digit immediately
  followed by asterisks (do not bold tokens ending in digits); never "significant" as an
  adjective (use "excludes zero" / "crosses zero"); never the phrase "the judge
  dominates."
- Report immutability: successor files only, new `YYYYMMDD[letter]-` prefix on the
  shared per-day sequence (2026-07-30 reached `m`; this file opens 2026-07-31).
  Manuscripts are the exception by house practice: living files edited under version
  banners.
- No deletions — move to `$V2/RECYCLE-BIN/`. v1 sibling read-only.
- Canary top and bottom of every artifact.
- Shared trunk: commit by explicit path only, never `git add -A`. Never pipe
  `git commit` — message to a file, `git commit -F`, verify `git log -1 --stat`.
- Hook sharp edges: the deletion guard scans the whole command string (a command merely
  containing a delete token is denied — use Write/Edit and mv); the security write-hook
  blocks the two exec-style tokens (a word immediately followed by an open parenthesis)
  even inside prose.
- New-artifact verification: `lint_claims.py` 0 blockers · canary count ≥ 2 · pytest
  103/103 if code was touched.

## 6. Verification commands

```bash
cd $V2
./.venv/bin/python -m pytest -q                                             # 103 passed
./.venv/bin/python tools/verify_instrument.py                               # ALL PASS 51/51
./.venv/bin/python REPORTS/20260725-manuscripts/lint_claims.py <new-file>   # 0 blockers
grep -c "WALKWORTHY-CANARY-7f3e2026" <new-file>                             # >= 2
```

## 7. Where things live

| Artifact | Path (under `$V2/`) |
|---|---|
| Governing memo + its corrections (read BOTH first) | `20260730i-gate-a-memo.md` · `20260730l-paper-c-adversarial-review-adjudication.md` |
| Rulings ledger — newest dated file is authoritative | `RULINGS-APPLIED-*.md` (through `-20260729d.md`) |
| Paper-c manuscript (v0.2 banner) | `REPORTS/20260730k-diagnostics-manuscript/20260730k-paper-c-instrument-diagnostics-v0.1.md` |
| Tier 0 reports, 2026-07-30 | `20260730b` exemplar ceiling · `c` d02 markers · `d` d05 scope note · `e` item difficulty · `f` d02 terminal-state · `g` d09 triangles · `h` d03 extraction |
| T0-2 d07 diagnostic | `20260729e-t0-2-d07-arc-diagnostic.md` |
| Instrument stamp + checker | `INSTRUMENT.json` · `tools/verify_instrument.py` · `tools/SCHEMA.md` §stamp |
| Audit scripts (durable, tracked) | `tools/audit/t0_*.py` · `tools/audit/d07_arc_diagnostic.py` |
| Characterization tests + suspect-behavior catalogue | `tests/test_metrics_characterization.py` |
| Frozen run tree (gitignored, on disk) | `logs/fullbank-3ep-20260724/` — 150 `.eval`, 15 `judgeB-*.jsonl`, raw `20260730-*.txt` |
| Prior manuscripts (paper-a, paper-b) | `REPORTS/20260725-manuscripts/` |
| Pre-registration | `20260716-prereg-comparisons-RATIFIED.md` |
| Superseded entry points (constraints still valid) | `20260730j` · `20260730m` · `20260730-boot-prompt-v3-tier0-continue.md` · `20260729c-…-project-closed.md` |

---

**If you are unsure whether something is authorized: it is not.** The project is stopped
at Gate A; paper-c is complete; only a new owner ruling (decision-menu item 2 or 3, as a
new `RULINGS-APPLIED-*`) changes that.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
