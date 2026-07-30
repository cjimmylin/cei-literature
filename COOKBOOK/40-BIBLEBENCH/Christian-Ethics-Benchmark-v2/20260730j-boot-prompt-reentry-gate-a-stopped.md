# BOOT PROMPT — WALKWORTHY v3, STOPPED AT GATE A (no open work queue)

Read this at the start of a fresh session. Self-contained: a session with zero prior
context can act correctly from it. Authored 2026-07-30, after Tier 0 closed.

**Supersedes `20260730-boot-prompt-v3-tier0-continue.md`** — that file's queue (T0-1
through T0-10 plus the Gate A memo) is fully executed and committed. It remains a valid
reference for the tier/gate structure and Tier 0 task definitions; it is no longer the
entry point. Its own predecessor, `20260729c-boot-prompt-reentry-project-closed.md`,
remains valid for phase-7 scientific results and binding constraints.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**SPEND POSTURE: $0. Nothing is authorized to spend. There is NO open work queue.**

---

## 1. Verify state before acting (30 seconds, do not skip)

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS   # git repo root is CEI-Lit-WS
git fetch origin && git log --oneline -4 -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
ls -1 COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/RULINGS-APPLIED-*.md | tail -3
git status -sb -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
```

**State at authoring:** trunk clean and in sync at `d1e63bc6e` (Tier 0 completion commit,
19 files). If a `RULINGS-APPLIED-*` file newer than `-20260729d` exists, read it FIRST —
it wins over this file and may reopen work. A sibling **WCF-Benchmark-v2** project is
actively worked by other sessions in this same clone; expect unrelated dirty files that
are not yours.

## 2. Governing state: STOPPED at Gate A

`$V2/20260730i-gate-a-memo.md` is the governing document. The pre-committed Gate A
criterion — stop if no design shows a within-item contrast that is both unsaturated and
judge-order-stable — **FIRED**, on the strength of: d02 terminal-state and d09 strict
seat-agreement both unsaturated but judge-order-unstable; the one stable-looking d02
contrast disqualified as a single-turn ladder-length artifact; the d07 floor confirmed
real; d05 ceiling-pinned with no within-item contrast; the phase-7 eight-of-nine
judge-swap ordering flips; and item-level judge disagreement on which items carry
information (67 under one judge, 6 under both).

| Tier | Status |
|---|---|
| Tier 0 (offline diagnostics) | COMPLETE — all ten items + Gate A memo |
| Tier 1 (taxonomy repair, judge-only rescores) | CLOSED — Gate A fired; T1-3 formally retired |
| Tier 2 (wide-gap probe) | CLOSED |
| Tier 3 (new items, format changes, bundled d02 version) | CLOSED |
| Holdout | QUARANTINED — Gate B never reached; guard intact; never set WALKWORTHY_ALLOW_HOLDOUT |

**Only a new owner ruling (a new `RULINGS-APPLIED-*` file) reopens anything.** Per the
pre-commitment, stopping forfeited nothing: Tier 0 stands alone as a publishable
instrument-diagnostics result.

## 3. Facts a fresh session must NOT re-derive (it will get them wrong)

1. **The test gate is 103/103, not 33/33.** T0-9 added 70 characterization tests. Any
   older file saying "33/33 must pass" is stale on that point.
2. **Exemplars are not gold references.** They are spec-bank items run live under each
   system (`tools/convert_banks.py:490`). Sub-ceiling exemplar scores indict nothing.
   The `walkworthy_inspect/metrics.py` docstring calling them "gold-standard reference
   administrations" is KNOWN WRONG and deliberately uncorrected (code edits are gated).
3. **The metric module is `walkworthy_inspect/metrics.py`** — there is no tools/metrics.py.
4. **d09 has 270 complete triangles** (the ~524 figure was a per-judge double-count), and
   the symmetry-index 1.0 "saturation" was the known-wrong in-log stored value; the
   correctly recomputed index is 0.69–0.91.
5. **The published d05 "0 of 10" scope is corrected by successor note `20260730d`**:
   computed pooled-strata, labeled pre-registered; stratum-a-only gives the identical
   headline; the C5 floor is worded in admins and passes. Pre-registered claims cite the
   stratum-a computation; the pooled one only as a labeled sensitivity check.
6. **d03 has no SUT-side forced-choice parser** — extraction operates on the judge's
   JSON (rate 0.9931; ep1 anchor 143/145, six failures all one synonym-key defect).
7. **The nano judge pin is a run-time override, not the code default** (the code default
   is gpt-4.1-mini). An unattended rerun on task defaults is a DIFFERENT instrument.
   Recorded in `INSTRUMENT.json` (instrument `WW-v2-20260724b`).
8. **Known item defects (documented, unfixed by design):** WW-05-L01 coverage-starved
   (no scored administration for mistral/gemini/llama in any epoch); WW-03-L02 zero-pass
   under both judges; five d04 items twinless, so d04's paired denominator is 24.
9. **The d02 cold_open × break_turn trap** stays dead: at ladder length 1 the read-out
   admits only 0.0 and 1.0, producing a fake all-system effect. Documented as a rejected
   alternative in `20260730f` §6 and pinned by a named test. Do not rediscover it.

## 4. What a session may do WITHOUT a new ruling

- Answer owner questions from the committed artifacts (see §7 map). Cite; do not rerun.
- Integrity checks, $0 and read-only:
  `cd $V2 && ./.venv/bin/python tools/verify_instrument.py` (expect ALL PASS 51/51) and
  `./.venv/bin/python -m pytest -q` (expect 103 passed). Project venv is `$V2/.venv`
  (py3.14); the vault-level .venv is py3.9 and cannot run any of this.
- Maintenance of this entry-point chain if the owner issues new rulings (new dated
  successor files only).

## 5. Decision menu Tier 0 surfaced for the OWNER — present, never execute unbidden

These are the natural next decisions. Each requires explicit owner direction; none is a
work queue for you:

1. **Commission the instrument-diagnostics write-up?** Tier 0's findings package (Gate A
   memo §4 and §6) is the raw material. Manuscript/venue decisions are out of scope by
   standing rule.
2. **Open a repair ruling for the documented defects?** Fixing the metrics docstring, the
   judge synonym-key parse loss, WW-05-L01 / WW-03-L02, or the twinless d04 items are
   code/bank edits — each is a new-instrument-version decision (and the d02 taxonomy
   revision remains bundled with the classifier re-pin as ONE version, per C6).
3. **Reopen any tier?** Requires a new `RULINGS-APPLIED-*` stating scope and spend.

## 6. Binding constraints (unchanged, carried forward)

- $0 unless a ruling says otherwise. No model calls of any kind.
- Holdout CLOSED; guard at `walkworthy_inspect/datasets.py` stays intact.
- `pushback_rate` stays CLOSED; renaming a closed statistic to relitigate it is prohibited.
- Ablations are never WALKWORTHY numbers; promoting one is a new instrument version.
- **R3 (linter-enforced BLOCKER):** no significance stars — never a digit immediately
  followed by asterisks (do not bold tokens ending in digits); never "significant" as an
  adjective (use "excludes zero" / "crosses zero"); never the phrase "the judge dominates."
- Report immutability: successor files only, new `YYYYMMDD[letter]-` prefix on the shared
  per-day sequence (2026-07-30 reached `j` — this file).
- No deletions — move to `$V2/RECYCLE-BIN/`. v1 sibling read-only.
- Canary top and bottom of every artifact.
- Shared trunk: commit by explicit path only, never `git add -A`. Never pipe
  `git commit` — write the message to a file, use `git commit -F`, verify with
  `git log -1 --stat`.
- Hook sharp edges: the deletion guard scans the whole command string — a command merely
  containing a delete token is denied; use Write/Edit and mv. The security write-hook
  blocks the two exec-style tokens (a word immediately followed by an open parenthesis)
  even inside prose.
- New-artifact verification: `lint_claims.py` 0 blockers · canary count ≥ 2 · pytest
  103/103 if code was touched.

## 7. Where things live

| Artifact | Path (under `$V2/`) |
|---|---|
| Governing memo (read FIRST) | `20260730i-gate-a-memo.md` |
| Rulings ledger — newest dated file is authoritative | `RULINGS-APPLIED-*.md` (through `-20260729d.md`) |
| Tier 0 reports, 2026-07-30 | `20260730b` exemplar ceiling · `c` d02 markers · `d` d05 scope successor note · `e` item difficulty · `f` d02 terminal-state · `g` d09 triangles · `h` d03 extraction |
| T0-2 d07 diagnostic (prior session) | `20260729e-t0-2-d07-arc-diagnostic.md` |
| Instrument stamp + checker | `INSTRUMENT.json` · `tools/verify_instrument.py` · `tools/SCHEMA.md` §stamp |
| Audit scripts (durable, tracked) | `tools/audit/t0_*.py` + `tools/audit/d07_arc_diagnostic.py` |
| Characterization tests (+ suspect-behavior catalogue) | `tests/test_metrics_characterization.py` |
| Frozen run tree (gitignored, on disk) | `logs/fullbank-3ep-20260724/` — 150 `.eval`, 15 `judgeB-*.jsonl`, raw `20260730-*.txt` outputs |
| Manuscripts (generated — edit `parts/`, rebuild; currently untouched by v3) | `REPORTS/20260725-manuscripts/` |
| Pre-registration | `20260716-prereg-comparisons-RATIFIED.md` |
| Superseded entry points (constraints still valid) | `20260730-boot-prompt-v3-tier0-continue.md` · `20260729c-boot-prompt-reentry-project-closed.md` |

---

**If you are unsure whether something is authorized: it is not.** The project is stopped
at Gate A; only a new owner ruling changes that.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
