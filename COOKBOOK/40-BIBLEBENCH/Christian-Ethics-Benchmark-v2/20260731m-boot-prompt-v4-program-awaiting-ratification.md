# BOOT PROMPT — WALKWORTHY v4 program (probe CLOSED; spec v0.4 twice-reviewed; AWAITING owner ratification of §8)

Read this at the start of a fresh session. Self-contained: a session with zero prior
context can act correctly from it. Authored 2026-07-31, end of the v4-opening session.

**Supersedes `20260731f-boot-prompt-reentry-post-repair.md` as the entry point.**
Nothing in it is retracted — its v3 facts, constraints, and run-machinery recipe all
remain valid and are incorporated by reference below. What changed: the owner OPENED
the v4 program (a NEW program; the v3 Gate A STOP is unchanged and un-relitigated).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**SPEND POSTURE: $0. NO open work queue.** The `-g`/`-h` probe authorization
($60.00) was executed, tallied at $48.806, and is CLOSED. It does not carry forward.
Every v4 execution phase (§7 of the spec) requires its own future ruling.

---

## 1. Verify state before acting (30 seconds, do not skip)

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS
git fetch origin && git log --oneline -8 -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
ls -1 COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/RULINGS-APPLIED-*.md | tail -3
git status -sb -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
```

**State at authoring:** trunk clean and in sync at `c908fc1f0`; newest rulings are
`RULINGS-APPLIED-20260731g` (v4 direction + probe) and `-20260731h` (ceiling
amendment). **If a `RULINGS-APPLIED-*` newer than `-20260731h` exists, read it FIRST
— it wins over this file.** In particular, the spec-ratification ruling is expected
to be the next one; it defines the queue. Sibling WCF-Benchmark-v2 is worked by
other sessions in this clone; expect unrelated dirty files.

$0 integrity checks (all should pass; instrument `WW-v2-20260731b` was NOT modified
by the probe):

```bash
cd COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2
./.venv/bin/python -m pytest -q                    # 115 passed
./.venv/bin/python tools/verify_instrument.py      # ALL PASS 51/51 (WW-v2-20260731b)
./.venv/bin/python tools/audit/analyze_widegap_probe.py   # $0 re-print of probe P1-P4 from stored logs
```

## 2. Governing state

| Thing | Status |
|---|---|
| v3 (Gate A STOP, tiers closed, published record = claims about WW-v2-20260724b) | UNCHANGED — everything in `20260731f` §2/§4 still binds |
| v4 program | OPENED by `-g` Ruling 1 (owner, 2026-07-31): keep frame + new designs; frontier target; two-tier gate; probe-first |
| Wide-gap probe (`-g`/`-h`, $60 ceiling) | EXECUTED + CLOSED — $48.806; report `20260731i` (as corrected by `20260731k` §2.3) |
| v4 design spec | `20260731j` at **v0.4**, SELF-CONTAINED, twice adversarially reviewed (adjudications `20260731k` v0.1→v0.2, `20260731l` v0.3→v0.4) |
| Profiling re-target | Owner directive 2026-07-31, recorded in spec lineage; ratified only when the §8 ruling lands |
| **The one open door** | **Owner ratification of spec v0.4 §8 (9 questions)** → next `RULINGS-APPLIED-*` defines the queue (likely v4-C first, ~$20–30 ceiling) |

## 3. What a session may do WITHOUT a new ruling

- Answer owner questions from the committed artifacts (map in §6). Cite; do not rerun.
- The §1 $0 checks. The probe analysis script also runs on the mid-tier tree
  (`--log-root logs/fullbank-3ep-20260724`), $0.
- Maintain the entry-point chain (new dated successor files only; never edit dated
  files; the spec `20260731j` is the exception — a living file under version banners).
- If the owner ratifies (even informally in chat): write the ratification as the next
  `RULINGS-APPLIED-*` (letter after the newest), then execute ONLY what it authorizes.
- Do NOT: start any §7 phase unbidden; re-litigate the `20260731k`/`20260731l`
  adjudications; author items; touch the instrument; open holdout paths.

## 4. Facts this session established at real cost (do NOT re-derive)

Probe facts:
1. Probe: 100 items, 4 frontier SUTs (gpt-5, claude-sonnet-4.5, gemini-2.5-pro,
   deepseek-r1) + gpt-4.1-mini anchor, 3 epochs, dual judge, $48.806. Tree
   `logs/widegap-probe-20260731/` (gitignored) incl. `item_manifest.json`,
   `run_matrix.sh`, `analysis_results.json`, 15 `judgeB-*.jsonl`.
2. **"Mid-tier had zero" is RETRACTED** (`20260731k` §2.3 is the standing correction
   to `20260731i` §5.1): identical P1 test on the mid-tier tree yields 10/60
   survivors (8.3 pct confirmatory ≈ the ~6.9 pct permutation null); frontier
   12/36 (19.4 pct ≈ 3× null). Frontier strengthens discrimination, did not create it.
3. d05: 4 pairs exclude zero but 3 are deepseek-r1-vs-rest (r1 collapses to 0.483
   CSR); top-three gap +0.061; anchor (0.859) NOT separated; 9 of 11 v3
   ceiling-pinned items released, H01/M01 still pinned.
4. gpt-5 profile: leads d05 (0.941) and d03-judge-A (0.906; judge-B REVERSES:
   claude45 1.000 > gpt5 0.880), trails everyone on d04 (0.033; deficit vs claude45
   confirmatory). ALL probe crossing evidence localizes to gpt-5 × d04.
5. d02 cross-judge ordering τ-b = −0.913 (worst in record) → absolute scoring
   retired, Davidson-BT protocol designed. d07: judge-A 0.000/26 vs judge-B 0.526 of
   19 scored (worst-case 0.385) → HOLD pending stored-arc re-score.
6. Judge-B complete-case retention vs judge-A-scored (the operative denominator, NOT
   the unparseable rate): d01 86.1 / d03 77.4 / d04 85.5 / d05 100 / d07 67.9 pct.
   Rule: < 85 pct voids the judge-swap check. Parse hardening = named v4-A code
   deliverable. X-2 is conditional on d03 clearing this at B2.
7. Run-machinery additions to the `20260731f` §4.13 recipe: calibrate cost with a
   ~$0.30 micro-run BEFORE projecting (gpt-5 ≈ 3.4k completion tokens/call, ~2.6k
   reasoning; caps 8192 reasoning / 4096 other); `tools/rescore/rescore.py` is
   sequential per cell — at probe scale run the 15 cells as PARALLEL processes
   (sequential ≈ 15 h, parallel ≈ 1 h); rescore cells are independent (own eval
   reads, own JSONL out).

Fable rulings (in `20260731l` §2 — binding on the spec, do not relitigate):
8. Crossing evidence TIERS attach to the pinned instrument scales; only the SIGN is
   monotone-invariant (v0.3's stronger invariance claim was demonstrated false).
9. The norm/shape frame is DESCRIPTIVE reporting only: LOO standardization, frame
   recomputed inside every bootstrap draw, leave-one-out sensitivity published,
   COMMON-ITEM cross-version linking (anchor-rerun linking is unidentified).
10. Structural labels are GRADED: multi-axis report / two-axis structure
    demonstrated (v4.0 target) / multidimensional profile. A reflected single factor
    also crosses; distinctness screening is two-sided (|τ-b|).
11. Named claims: X-1 = gpt5/deepseekr1 between P-ALLOCATION and P-MOTIVE
    (re-named for power; d05 leg +0.458 already interval-excluding) and X-2 =
    gpt5/gemini25pro between P-FAITHFULNESS and P-MOTIVE (conditional, fact 6).
    Crossing p = max(leg p) (intersection-union); Holm across {X-1, X-2} only —
    never across legs. d04 REBUILD is power-sized n = 40; d03 n ≥ 16.
12. Ship rule requires ≥ 1 CONFIRMATORY crossing — an explicit AMENDMENT of `-g`
    Ruling 1.3's descriptive-sufficient provision at instrument level (per-dimension
    claims keep the descriptive tier). §8 item 5 ratifies this knowingly.
13. B1+B2 ≈ $180–230 (≈ 4× the largest prior ceiling) — its own §8 question; never
    treat as pre-approved.

Artifact discipline:
14. Spec v0.4 is SELF-CONTAINED; v0.2/v0.3 texts exist ONLY at git `d249122d0` /
    `ee3a441ff` — never cite "v0.2 §x" as normative.
15. R3 lint sharp edge (cost two blockers twice): a bold span must never END on a
    digit (`…n ≥ 12**` reads as significance stars). Also: no "significant" as
    adjective; "excludes zero"/"crosses zero"; never "the judge dominates".
16. Axis-candidate availability at mid-tier band: d06 7, d08 6, d10 8 items (ten do
    not exist); d08's SUT variance share is 9.1 pct — below the 13.79 pct df-null
    line, weakest candidate. Axis probes screen variance/degeneracy ONLY.

## 5. Binding constraints (carried forward unchanged)

All of `20260731f` §5 applies verbatim: $0 unless ruled; holdout CLOSED (never set
WALKWORTHY_ALLOW_HOLDOUT; converter `--no-holdout`); pushback_rate CLOSED; ablations
never WALKWORTHY numbers; any bank/scorer/pin change = new instrument version with
superseded stamps preserved; R3 linter rules; report immutability (successor files;
manuscripts/specs live-edit under version banners); no deletions (RECYCLE-BIN);
explicit-path commits, message via `git commit -F`, verify `git log -1 --stat`;
canary top+bottom of every artifact; deletion-guard and exec-token hook sharp edges;
new-artifact gates (lint 0 blockers · canary ≥ 2 · pytest 115 if code touched ·
verify_instrument if pinned components touched, which needs a ruling first).
Probe numbers are DIAGNOSTICS ONLY — never quoted as WALKWORTHY numbers or
comparative system claims.

## 6. Where things live

| Artifact | Path (under `$V2/`) |
|---|---|
| Rulings ledger (newest wins) | `RULINGS-APPLIED-*.md` through `-20260731h.md` |
| 2026-07-31 v4 chain, reading order | `RULINGS-APPLIED-20260731g` → `-h` → `20260731i` (probe report) → `20260731k` (1st adjudication + §2.3 correction) → `20260731j` (spec, **v0.4**) → `20260731l` (2nd adjudication, Fable rulings) → this file |
| Probe analysis ($0 rerun) | `tools/audit/analyze_widegap_probe.py` |
| Probe run tree (gitignored) | `logs/widegap-probe-20260731/` |
| v3 record entry point (still valid for v3 facts) | `20260731f-boot-prompt-reentry-post-repair.md` |
| Instrument stamp + checker | `INSTRUMENT.json` (WW-v2-20260731b) · `tools/verify_instrument.py` |
| Mid-tier frozen tree (for $0 comparisons) | `logs/fullbank-3ep-20260724/` |

---

**If you are unsure whether something is authorized: it is not.** The v4 program has
exactly one open door — the owner ratifying spec v0.4 §8 (nine questions; the answer
becomes the next `RULINGS-APPLIED-*` and defines the queue, with v4-C at $20–30 the
recommended first phase). Until that ruling exists, this is a $0 session: verify,
cite, answer, and wait.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
