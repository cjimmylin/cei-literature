# v1↔v2 Cross-Harness Comparison — DESIGN MEMO (no execution)

**Date:** 2026-07-16 (session 5) · **Status:** DESIGN ONLY — ends at the consolidated
spend gate (`20260716-spend-memo-f9-f2-crossharness.md`). Nothing here has been run.

**Scope guard (verbatim intent of the PARALLEL ruling,
`20260716-owner-ruling-v2-parallel.md`):** this comparison is *descriptive* instrument
work. It feeds a future canonical-ruling evidence base but does **not** reopen the
PARALLEL ruling; v1 remains canonical for release evidence regardless of the outcome.

---

## 1. What we found that changes the design (new, this session)

**The v1 side of the comparison already exists on disk.**
`../Christian-Ethics-Benchmark/runs/20260713-mvp-a1/` holds a completed, owner-authorized
(2026-07-13, $5.00 NTE) v1 run of the **MVP-A1 slice**: the SHA-pinned 60-item public
subset (6 items/design: 2 easy + 4 hard; `harness/walkworthy/mvp_pilot.py::MVP_ITEM_IDS`,
manifest SHA `6874ae26…`), 3 SUTs × 60 items with per-item `scalar_by_judge`,
`judge_report`, and `scored_items.jsonl`, judged by **the same judge pair as the v2
pilot** (judge-A gpt-4.1-nano, judge-B llama-3.3-70b).

Verified joinability (this session, offline):
- All 60 MVP-A1 item_ids exist in v2 `datasets/public/` and all are runnable (0 missing,
  0 non-runnable). They map to exactly **100 v2 admin lines** (pairs/ladders included).
- Two of the three MVP-A1 SUTs are also in the v2 pilot panel:
  `mistralai/mistral-small-3.2-24b-instruct` and `google/gemini-2.5-flash-lite`
  (the third, qwen3-8b, is v1-only — excluded).

## 2. Proposed comparison (Option A — primary)

Run **only the v2 side**: the 60-item MVP-A1 slice through the v2 Inspect harness for
the 2 overlapping SUTs, judge-A live, judge-B via `tools/rescore/rescore.py` (free-ish
judge-token pass). Compare against the stored v1 MVP-A1 outputs. **No v1 execution at
all** — the v1 read-only constraint is satisfied trivially (reading `runs/` is allowed).

- Item scoping: `-T item_ids=<60 ids>` per design (R10: never `--limit` on paired
  designs; 05 is unpaired but item_ids scoping is uniform and safer).
- Same ops rules as the pilot: `--max-tokens 4096 --max-connections 4`, availability
  probe first, per-SUT spend tally, headlines only from `recompute_metrics.py`.
- Prerequisite ordering: **F9 micro-check before (or within) this run** — v2's design-05
  live format retry (landed this session) now matches v1's `run_with_format_retry`
  semantics; comparing 05 across harnesses without it would confound format-gating.
  Ideally also **F2 design-07 anchor ablation first** (see §4 confound c1).

## 3. Decision statistic — "do the harnesses measure the same thing?"

Three layers, all descriptive, no rankings (R1), judge-B companions everywhere (R4):

1. **Per-item agreement** (same SUT, same judge, same item): v1 `judge_report`
   categories vs v2 `Score.value` categories where category spaces align; exact
   agreement fraction + κ for categorical fields; paired differences for numeric
   scalars. Report per design.
2. **Per-design cell deltas vs the judge-swap noise band** — the pre-registered
   decision rule: for each design and SUT, compute Δharness = |cell_v2 − cell_v1| under
   judge-A, and compare to Δjudge = |cell_A − cell_B| within v2 (already computed by
   `tools/audit/pilot_judge_swap.py` at pilot scale; recompute on the 60-item slice for
   n-matched bands). **A cross-harness delta smaller than the judge-swap band is
   indistinguishable from judge noise** → verdict "no detectable harness effect at this
   n". Δharness > Δjudge on any design → flagged harness effect; investigate before any
   canonical-ruling use.
3. **Judge-sensitivity reproduction** (structural, not ordinal): designs whose cells
   are judge-sensitive in v2 (all 9 comparable, per the pilot) should show the same
   instability in v1's two-judge records. Reported as a property table, never as
   SUT ordering.

Power honesty: at n=6 items/design the per-design cells are all under the R2 n≥10
floor — every per-design cell is reported "insufficient n" and the headline statistic
is the **pooled per-item agreement** (n=60 per SUT per judge, n=120 pooled across SUTs)
plus the direction/magnitude of the 10 per-design deltas as a pattern, not 10 separate
claims.

## 4. Pre-registered confounds (must appear in the results report)

- **c1 — design-07 anchors:** v2 judges 07 with `_DESIGN07_STATE_ANCHORS` (2026-07-16);
  v1 MVP-A1 judged without harness anchors. A 07 cross-harness delta is therefore
  anchors+harness, not harness alone. The F2 anchor-off ablation (if authorized) gives
  the anchor-only delta and cleanly decomposes this — hence the recommended sequencing
  F2-07 → cross-harness.
- **c2 — 02/07 branch routing:** v1's ladder branching used its heuristic/judge-call
  classifier; v2 uses a classifier model with lexical fallback. Different routing can
  administer *different stimuli* on the same item. 02/07 comparisons are therefore
  descriptive-only; the primary equivalence read lives on the single-turn designs
  (01/03/04/05/06/08/09/10).
- **c3 — time + decode noise:** v1 MVP-A1 ran 2026-07-13; the v2 slice would run now.
  Single-run stochastic decode (R11; F10 seed probe still open) plus possible OpenRouter
  endpoint drift is inside Δharness. The judge-swap band comparison partially absorbs
  this; the residual is disclosed, not modeled.
- **c4 — score-shape mismatch:** v1 emits per-item scalars + judge_report; v2 emits
  category dicts + recomputed design metrics. The mapping layer (which fields are
  declared comparable per design) must be written down in the results report BEFORE
  numbers are read (R3 spirit: pre-commit the reportable cells).

## 5. The v1 read-only problem (and Option B)

Option A requires **zero v1 writes**. If the owner ever wants fresh paired same-day runs
(Option B — controls c3 at ~$3–4 extra), v1 execution is possible without violating
read-only:

- v1's output dir is natively configurable: `run.py:352` —
  `out = Path(args.out) if args.out else root / "runs" / panel`. Invoke with
  `--out <v2>/logs/crossharness-YYYYMMDD/v1side/` so all artifacts land in the v2 tree.
- Set `PYTHONDONTWRITEBYTECODE=1`: executing v1 code otherwise writes `__pycache__/`
  into the v1 tree — a real (if benign) write that the read-only ruling forbids.
- Residual risk: any un-audited absolute-path write inside v1 (caches, logs). A mock
  dry-run with the redirect, followed by `find v1 -newer <stamp>`, verifies zero v1-tree
  writes before the paid run. If any residual write is found → **owner exception
  required**, not a workaround.

## 6. Cost math (Option A)

Anchors: v2 pilot = 563 admins/SUT ≈ $0.55/SUT (SUT + judge-A + classifier, log-exact);
judge-B ≈ $0.90 / 2,815 admins ≈ $0.00032/admin.

| Component | Volume | Estimate |
|---|---|---|
| v2 SUT+judge-A, 2 SUTs × 100 admins | 200 admins (~17.8% of a pilot SUT ×2) | ≈ $0.20 |
| judge-B rescore (rescore.py) | 200 admins | ≈ $0.07 |
| F9 retry overhead on the 05 slice | ≤ 12 extra generations | ≈ $0.02 |
| v1 side | stored — reuse | $0.00 |
| **Total (Option A)** | | **≈ $0.29, ceiling $0.75 NTE** |

Option B (fresh v1 side, 2 SUTs × 60 items × 2 judges): ≈ $2.50, ceiling $4.00 NTE —
not recommended until Option A shows a harness effect worth isolating from c3.

## 7. Claims scope

Results are descriptive instrument-equivalence evidence. Permissible claim shapes:
"per-item agreement X [CI] pooled across the slice; per-design deltas sit within/outside
the judge-swap band on k/10 designs." No SUT rankings, no "v2 validates v1" (or
converse), no reopening of PARALLEL. If deltas sit within the judge-swap band across
designs, the honest summary is: *any harness effect is smaller than the judge effect we
already know we have* — which is the strongest statement this design can support.

---

**GATE:** Execution (≈$0.29, ceiling $0.75) is item 3 of the consolidated spend memo.
This memo ends here per the session boot prompt.
