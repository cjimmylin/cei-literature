# BOOT PROMPT — WALKWORTHY v3, post-repair re-entry (STOPPED at Gate A; WW-v2-20260731b repaired + validation-run complete)

Read this at the start of a fresh session. Self-contained: a session with zero prior
context can act correctly from it. Authored 2026-07-31, end of the repair session.

**Supersedes, by consolidation, `20260731-boot-prompt-reentry-consolidated.md`** —
nothing in it is retracted; this file carries its content forward plus the 2026-07-31
repair ruling, the bundled instrument version, and the validation run. Earlier entry
points (`20260730j`, `20260730m`, `20260730-boot-prompt-v3-tier0-continue.md`,
`20260729c-…-project-closed.md`) remain valid constraint references only.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**SPEND POSTURE: $0. Nothing is authorized to spend. There is NO open work queue.**
(The $3.00 ceiling of `RULINGS-APPLIED-20260731d` was for its validation run only —
executed, tallied at ~$0.085, and CLOSED. It does not carry forward.)

---

## 1. Verify state before acting (30 seconds, do not skip)

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS   # git repo root is CEI-Lit-WS
git fetch origin && git log --oneline -6 -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
ls -1 COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/RULINGS-APPLIED-*.md | tail -3
git status -sb -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
```

**State at authoring:** trunk clean and in sync at `d876ed05d`; newest ruling is
`RULINGS-APPLIED-20260731d`. If a `RULINGS-APPLIED-*` newer than `-20260731d` exists,
read it FIRST — it wins over this file and may reopen work. Sibling **WCF-Benchmark-v2**
is actively worked by other sessions in this same clone; expect unrelated dirty files
that are not yours.

## 2. Governing state

**STOPPED at Gate A — unchanged.** The pre-committed stop criterion (no design shows a
within-item contrast that is both unsaturated and judge-order-stable) fired on the
Tier 0 evidence and has not been revisited. `$V2/20260730i-gate-a-memo.md` +
`$V2/20260730l-paper-c-adversarial-review-adjudication.md` remain the governing
synthesis. What changed on 2026-07-31 is instrument-repair state, not project state:

| Thing | Status |
|---|---|
| Tier 0 + Gate A memo + paper-c (v0.2, review-complete) | COMPLETE, unchanged |
| Tiers 1 / 2 / 3 | CLOSED — only a new `RULINGS-APPLIED-*` reopens |
| Holdout | QUARANTINED — never set WALKWORTHY_ALLOW_HOLDOUT |
| Instrument on disk | **`WW-v2-20260731b`** (bundled repair version per `RULINGS-APPLIED-20260731b`; predecessor stamp preserved at `INSTRUMENT-WW-v2-20260724b-superseded.json`) |
| Repair validation (`RULINGS-APPLIED-20260731d`, $3.00 ceiling, ~$0.085 spent) | EXECUTED + CLOSED — **6 of 7 items VALIDATED; WW-03-L02 NOT VALIDATED** (`20260731e` report) |
| Decision-menu items still open (owner's alone) | item 2 (C6 d02 taxonomy + classifier bundle — offered twice, NOT taken) · item 3 (reopen a tier) · any further item repair (WW-03-L02, WW-04-I02 cue) |

## 3. What a session may do WITHOUT a new ruling

- Answer owner questions from the committed artifacts (map in §7). Cite; do not rerun.
- Integrity checks, $0 and read-only, with the UPDATED expectations:
  `cd $V2 && ./.venv/bin/python tools/verify_instrument.py` → ALL PASS **51/51 vs
  WW-v2-20260731b**; `./.venv/bin/python -m pytest -q` → **115 passed** (not 103);
  `./.venv/bin/python tools/audit/validate_repairs_20260731d.py` → re-prints the
  validation verdicts from the stored run tree, $0. Project venv is `$V2/.venv`
  (py3.14); the vault-level .venv is py3.9 and cannot run any of this.
- Maintain this entry-point chain if the owner issues new rulings (new dated successor
  files only; never edit dated files).
- If the owner opens a decision-menu door, the ruling defines the queue; until then do
  not draft, probe, fix, or "prepare" anything for those items.

## 4. Facts a fresh session must NOT re-derive (it will get them wrong)

Published-record facts (unchanged):
1. **Every published number — Tier 0 reports, paper-c — is a claim about
   `WW-v2-20260724b`**, not about the repaired instrument. Never recompute a headline
   under `WW-v2-20260731b`; under the repaired parser the frozen d03 logs would read
   870/870, but the shipped 864/870 (0.9931) is the correct published figure.
2. The d02 break-position "premium" was NEVER judge-order-stable on committed data
   (Spearman 0.00 / Kendall −0.20; the memo's "rho ≈ +0.7" was planning-era, corrected
   in `20260730l`). d05 ceiling count is 12 of 28 non-exemplar items, not 12 of 32.
3. Tables are authoritative over prose in the Tier 0 reports (`20260729e` d07 case);
   only six of the ten audit items had true G0 reproduce-a-published-number gates.
4. The d02 measure substitution (terminal-state for break_turn) was pre-committed in
   `RULINGS-APPLIED-20260729d` lines 81–86 — not a prereg deviation.
5. Exemplars are spec-bank items run live per system, NOT gold references
   (`tools/convert_banks.py`; the metrics.py docstring saying otherwise was FIXED in
   this repair version — do not "restore" it).
6. d09 has 270 complete triangles (~524 was a per-judge double-count); recomputed
   symmetry index 0.69–0.91, not the stored 1.0.
7. The nano judge pin is a run-time override (`-T judge_model=openrouter/openai/gpt-4.1-nano`);
   the code default is gpt-4.1-mini — an unattended default rerun is a DIFFERENT
   instrument. Machine-checked via `INSTRUMENT.json` + `tools/verify_instrument.py`.

Repair-session facts (new, expensively established):
8. **The test gate is 115/115, not 103** (12 synonym-fallback tests added).
9. **WW-03-L02's zero-faithful floor is model behavior, not item artifact**: it
   survived removal of the explicit omission instruction AND a reduced faithful bar
   (`20260731e` §3). The item stays UNVALIDATED; its SAY arm now lands keyed-"no" only
   7–8 of 15 (was near-uniform) — a keying question for any future revision. Do not
   re-edit it without a new ruling.
10. **WW-05-L01 is fixed and VALIDATED** (CSR decidable 15/15, spread 0.0/0.5/1.0).
    Root cause was: prose constraints without a comparator symbol are SILENTLY dropped
    by `ordo_constraints`, and its only parseable constraint was remedy-escaped, so
    jury < 2 collapsed the denominator. An item author must always include at least
    one hard (non-escaped) numeric floor.
11. **The five d04 conversions are VALIDATED** (complete α/β pairs 15/15, harshness
    15/15); WW-04-I02's β cue is flagged too subtle (judge-A mean delta −0.096, β ≥ α
    in 11/15 cells) — a future-revision flag, not a defect ruling. d04's paired
    denominator is 29 under WW-v2-20260731b but was 24 in everything published.
12. **Pair-vs-single in design 04 is decided ONLY by the presence of `Shared` /
    `α cue` / `β cue` bold fields in the bank markdown** (Greek letters; v1 builder);
    keyed direction comes from the literal substring "delta > 0" in the keyed text;
    header "(pair)"/"(4b, single)" is cosmetic.
13. **Run machinery** (recon-established, use as-is): subset runs use `-T item_ids=`
    (matches `metadata.item_id`, auto-includes all admins of an item), NOT
    `--sample-id`; epochs = 3 independent single-epoch `inspect eval` invocations into
    `ep1/ep2/ep3` dirs (rescore tooling is not epoch-aware); judge-B via
    `tools/rescore/rescore.py --log-dir … --judge-b openrouter/meta-llama/llama-3.3-70b-instruct`
    (it records NO token usage — bound its spend by the nano volume at llama prices);
    credentials via `source ~/.codex/secrets/openrouter.env` (nothing auto-loads);
    log roots must never contain the substring "rescore"; designs 03/04/05 make zero
    branch-classifier calls. Working template: `logs/repair-validation-20260731d/run_matrix.sh`.
14. **The bank's `validation_status` YAML markers were deliberately NOT updated after
    validation** (bank edit = new hashes = new instrument version). `20260731e` is the
    authoritative validation record; reconciling the markers is bookkeeping for the
    NEXT instrument version, not a standalone task.

## 5. Binding constraints (unchanged, carried forward)

- $0 unless a ruling says otherwise. No model calls of any kind.
- Holdout CLOSED; guard in `walkworthy_inspect/datasets.py` stays intact; the
  converter is only ever run with `--no-holdout` outside a holdout-authorized ruling.
- `pushback_rate` CLOSED; renaming a closed statistic to relitigate it is prohibited.
  C6: the d02 taxonomy revision ships bundled with the classifier re-pin as ONE
  instrument version — still NOT taken.
- Ablations are never WALKWORTHY numbers; promoting any alternative read-out is a new
  instrument version. Any bank/scorer/pin change → new instrument version, superseded
  stamps preserved (`tools/SCHEMA.md` re-stamp rule).
- **R3 (linter-enforced BLOCKER):** no significance stars — never a digit immediately
  followed by asterisks (do not bold tokens ending in digits); never "significant" as
  an adjective (use "excludes zero" / "crosses zero"); never the phrase "the judge
  dominates."
- Report immutability: successor files only, new `YYYYMMDD[letter]-` prefix on the
  shared per-day sequence (2026-07-31 reached `f` — this file). Manuscripts are the
  exception by house practice: living files edited under version banners.
- No deletions — move to `$V2/RECYCLE-BIN/`. v1 sibling read-only (the run harness
  imports its builders — never edit them).
- Canary top and bottom of every artifact; every public bank line carries it.
- Shared trunk: commit by explicit path only, never `git add -A`. Never pipe
  `git commit` — message to a file, `git commit -F`, verify `git log -1 --stat`.
- Hook sharp edges: the deletion guard scans the whole command string (a command
  merely containing a delete token is denied — use Write/Edit and mv); the security
  write-hook blocks the two exec-style tokens (a word immediately followed by an open
  parenthesis) even inside prose.
- New-artifact verification: `lint_claims.py` 0 blockers · canary count ≥ 2 · pytest
  115/115 if code was touched · `verify_instrument.py` ALL PASS if any pinned
  component was touched (which requires a ruling first).

## 6. Verification commands

```bash
cd $V2
./.venv/bin/python -m pytest -q                                             # 115 passed
./.venv/bin/python tools/verify_instrument.py                               # ALL PASS 51/51 (WW-v2-20260731b)
./.venv/bin/python tools/audit/validate_repairs_20260731d.py                # reprints validation verdicts, $0
./.venv/bin/python REPORTS/20260725-manuscripts/lint_claims.py <new-file>   # 0 blockers
grep -c "WALKWORTHY-CANARY-7f3e2026" <new-file>                             # >= 2
```

## 7. Where things live

| Artifact | Path (under `$V2/`) |
|---|---|
| Rulings ledger — newest dated file is authoritative | `RULINGS-APPLIED-*.md` (through `-20260731d.md`) |
| Governing memo + corrections (read BOTH first) | `20260730i-gate-a-memo.md` · `20260730l-paper-c-adversarial-review-adjudication.md` |
| 2026-07-31 repair chain, in order | `RULINGS-APPLIED-20260731b.md` (repair ruling) → `20260731c-instrument-repair-report-ww-v2-20260731b.md` → `RULINGS-APPLIED-20260731d.md` (validation ruling) → `20260731e-repair-validation-report.md` |
| Instrument stamp + checker + superseded stamp | `INSTRUMENT.json` (WW-v2-20260731b) · `tools/verify_instrument.py` · `INSTRUMENT-WW-v2-20260724b-superseded.json` · `tools/SCHEMA.md` §stamp |
| Validation analysis (tracked, $0 rerun) | `tools/audit/validate_repairs_20260731d.py` |
| Validation run tree (gitignored, on disk) | `logs/repair-validation-20260731d/` — 45 `.eval`, 15 `judgeB-*.jsonl`, `run_matrix.sh`, `verify_and_tally_subset.py` |
| Paper-c manuscript (v0.2 banner) | `REPORTS/20260730k-diagnostics-manuscript/20260730k-paper-c-instrument-diagnostics-v0.1.md` |
| Tier 0 reports, 2026-07-30 | `20260730b` exemplar ceiling · `c` d02 markers · `d` d05 scope · `e` item difficulty · `f` d02 terminal-state · `g` d09 triangles · `h` d03 extraction |
| T0-2 d07 diagnostic | `20260729e-t0-2-d07-arc-diagnostic.md` |
| Repaired bank sources | `banks/03-quiettongue-seeds.md` (WW-03-L02) · `banks/04-innerweight-seeds.md` (5 conversions) · `banks/05-ordoamoris-seeds.md` (WW-05-L01) |
| Synonym-fallback tests | `tests/test_scorers_synonym_fallback.py` |
| Frozen published run tree (gitignored) | `logs/fullbank-3ep-20260724/` |
| Pre-registration | `20260716-prereg-comparisons-RATIFIED.md` |
| Superseded entry points (constraints still valid) | `20260731-boot-prompt-reentry-consolidated.md` · `20260730j` · `20260730m` · `20260730-…-tier0-continue.md` · `20260729c-…-project-closed.md` |

---

**If you are unsure whether something is authorized: it is not.** The project is
stopped at Gate A; the instrument is repaired and its validation run is closed; the
open doors — the C6 d02 bundle, reopening a tier, further repair of WW-03-L02 or the
WW-04-I02 cue — are the owner's alone, opened only by a new `RULINGS-APPLIED-*`.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
