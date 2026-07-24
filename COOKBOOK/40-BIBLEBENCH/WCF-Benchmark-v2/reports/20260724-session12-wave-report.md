# WCF-Benchmark-v2 — Session 12 Wave Report (replacement-authoring tranche; gate NO-GO)

**Executed:** 2026-07-18/19 per `20260718-session12-replacement-authoring-boot-prompt.md`
· **Report written:** 2026-07-24 (after owner ruling) · **Committed:** `f8d640199`
· **Bank:** v2.4 (unchanged — no items admitted) · **Harness:** panel median of
gemini-2.5-flash + deepseek-chat + mistral-small-2603, last-match parser.
**All numbers EXPLORATORY / NON-QUOTABLE; 0–100 rubric conformity, not accuracy.
Scores are panel-median rubric-conformity ranks, not absolute values. No
pre-registration framing (vault v1.x directive).**

## Headline

**The replacement-authoring tranche cleared authoring and the blind kill-loop
(80 items, 0 kills) but FAILED the live gate: 17/80 = 21.2% nonzero |qwen−haiku|,
below the pre-stated ≥⅓.** Diagnosis is ceiling saturation on the qwen–haiku
pair, not a plumbing fault — gpt-4o-mini spreads widely across the same items, so
the instrument has range. Owner ruling (2026-07-24): **SESSION-13 HARDENING PASS**;
partial admission and criterion amendment declined; bank stays v2.4. Gate results:
`analysis/20260718-session12-gate-results.json`.

## Phase 0 — P1 + P4 (owner-acked)

**P1 — char-split fix.** `src/wcf_tasks.py` `render_standard` gained an
`isinstance(list)` guard: the string sentinel `"declines total order"` on 5 AGG
items (AGG-C3-003, AGG-C4-W202, AGG-C7-007, AGG-C5-W304, AGG-C8-W305 — all route
as the contested kind) was being char-split into judge prompts. Regression tests
in `tests/test_session12.py`. The fix is render-side, so future evals are
automatically clean; the regrade of the 5 is **DEFERRED to the next eval** (no
$0 path exists this session).

**P4 — explicit mold + provenance.** All 287 records now carry explicit `mold` +
`provenance` fields via a `MOLD_BY_PREFIX` map in `convert/yaml_to_jsonl.py`
(provenance mirrors `authored`; an unknown prefix raises). Pinned tests updated —
`test_jsonl_counts_and_split` now counts by provenance: **199 v1 / 29 s6 / 37 s7**.
Manifest restamped 2026-07-18; `BANK_VERSION` stays **v2.4**. Full pytest: **87 pass
+ 1 pre-existing environment failure** (`test_frontier_core_task_size` needs
`OPENROUTER_API_KEY`; fails identically on the pre-diff tree).

## Phase 1 — drafting (80 items)

8 opus drafters, 2 per mold × 10 items → **80 items** MEND / LIB / PROOF /
WHOLE-N-001..020 in `data/session12-drafts/D-*.json`. The PROOF batch used the new
**apply-not-quote** design: no ≥8-word verbatim confessional runs in stems; exact
quotes live only in the key's AUTHORITATIVE STANDARDS TEXT (ASTT) block.

Post-draft mechanical validation caught **47 anchorless rubric lines** across 3
batches (D-LIB-b 17, D-MEND-a 14, D-PROOF-a 16) — repaired by the original-batch
repair agents. Drafter self-reports had overclaimed full anchoring; the mechanical
pass is the backstop.

## Phase 2 — blind kill-loop: **0 KILLS, ~45 items repaired**

16 blind adversarial reviewers (2 per batch: lens A form/gradeability, lens B
construct/difficulty/doctrine), **160 verdicts → 0 KILLS**, ~45 items repaired.
Defect classes (all caught cross-batch):

1. **Q147↔Q148 sins-vs-duties anchor confusion** on 10th-commandment lines (4 items;
   found independently by two reviewers).
2. **Missing wrong-verdict GATE blocks** (12 LIB items + later 8 evaluative WHOLE
   items, per the Fable G1 ruling below).
3. **ONE FABRICATED WLC Q105 quote** in PROOF-N-017's ASTT block ("the giving of
   that worship and glory to any other…" — not in Q105); replaced with the verified
   authentic clause.
4. **PROOF-N-007** "needless"→"unnecessary" Q145 wording correction.
5. **Banned "settle" stem token** (PROOF-N-012).
6. **Axis mis-tags and double-barreled criteria** across WHOLE-b.
7. **In-block anchor gaps** — Q113 / WCF 1.9 clauses added to 3 PROOF ASTT blocks.

**LIB-N-005** was ruled a near-duplicate of banked item LIB-C2-W307 → differentiated
(candle element removed; cornerstone + oil kept) → fresh 2-reviewer round → **KEEP**
(lens B confirmed distinct discrimination texture; one split applied).

**Fable adjudication.** The zero-kill outcome vs s6's 14.8% kill ratio is attributed
to the matured briefs / style pack, with the live gate as the objective backstop —
not to laxer review. The reviewers' GATE-scope disagreement was resolved by ruling
**ALL evaluative items carry wrong-verdict GATEs** (uniformity).

**G1.** New `analysis/session12_g1_check.py` (s6 checks + 8-gram contamination scan
vs `../WCF/*.txt` + gold_order-type check): **80 items, 0 violations** after repairs.
One G1 false positive is documented ("review-tied" in MEND-N-017 is legit key text;
the pattern was narrowed). **G3.** $0 mockllm **80/80 samples success**; prompts
render correctly (ANCHOR ask present, ASTT in targets, no GOLD ORDER lines).

## Phase 3 — live gate (2026-07-19): **NO-GO**

3 SUTs via OpenRouter — qwen/qwen3.7-plus (~19 min), anthropic/claude-haiku-4.5
(~3.5 min), openai/gpt-4o-mini (~4 min) — × 80 items, default 3-judge median panel
(gemini-2.5-flash / deepseek-chat / mistral-small-2603), logs at
`logs/20260718-session12-gate-main/`. Spend **~$1.5–2 of the $6 authorization**.
Eval: `analysis/session12_gate_eval.py` (verbatim s6/s7 criterion).

**VERDICT: NO-GO — 17/80 (21.2%) nonzero |qwen−haiku| < pre-stated ≥⅓.** Unscored 0,
missing 0, all-SUT-zero 0. Results: `analysis/20260718-session12-gate-results.json`.

## Phase 3 diagnosis — ceiling saturation (not a plumbing fault)

**69/80 qwen scores = 100; 55 of the 63 zero-gap items tie at 100-100; ZERO items
tie at the GATE cap 40.** Per-mold nonzero-gap counts: MEND 6 / LIB 5 / PROOF 2 /
WHOLE 4.

| SUT | MEND | LIB | PROOF | WHOLE |
|---|---|---|---|---|
| qwen3.7-plus | 97.5 | 99.6 | 97.0 | 96.0 |
| claude-haiku-4.5 | 96.0 | 94.9 | 96.2 | 91.3 |
| gpt-4o-mini | 91.1 | 74.1 | 63.6 | 72.2 |

**gpt-4o-mini spreads widely → the instrument has range; the saturation is
qwen–haiku-pair-specific.** Top gaps: WHOLE-N-010 36 · LIB-N-005 36 · LIB-N-001 33 ·
MEND-N-011 31 · WHOLE-N-009 27 · LIB-N-009 25 · WHOLE-N-001 20 · MEND-N-006 17.

**Opus transcript audit of 6 tied-100s** (MEND-N-004, MEND-N-013, LIB-N-017,
PROOF-N-005, PROOF-N-019, WHOLE-N-014):

- **4 GENUINE-100** — the SUTs really satisfy the rubrics; single-direction molds
  are not frontier-hard for the mid-2026 tier-1 tier.
- **1 modest over-credit** — MEND-N-013 real ~91 (the un-addressed volunteers prong).
- **1 SEVERE over-credit** — LIB-N-017 real ~75: qwen committed the very legalism
  error the double-hazard item exists to catch, and gemini-2.5-flash awarded 100 with
  a factually false justification. **Judges under-enforce the "unbind" half of
  double-hazard rubrics.**

**Conclusion:** item softness dominates; double-hazard / opposite-handling constructs
are the discriminators. The 6-transcript audit sampled qwen only.

## Owner ruling (2026-07-24, STOP-POINT 1)

**SESSION-13 HARDENING PASS.** Rebuild the 63 saturated items toward double-hazard
constructs, keep the 17 discriminators, re-gate within the remaining **~$4**.
Partial admission and criterion amendment **declined**. **No items admitted; bank
stays v2.4.** Boot prompt: `20260724-session13-hardening-boot-prompt.md` (being
authored alongside this report).

## Standing caveats

EXPLORATORY / NON-QUOTABLE. Scores are panel-median rubric conformity — ranks, not
absolute values. Single gate run per SUT (no epochs). The 6-transcript audit sampled
qwen only. Any future v2.5 is a separate instrument — no cross-version comparison
(bank-versioning rule).

## Artifacts

Report: this file. Boot prompts: `20260718-session12-replacement-authoring-boot-prompt.md`,
`20260724-session13-hardening-boot-prompt.md`. Analysis:
`20260718-session12-gate-results.json`, scripts `session12_gate_eval.py`,
`session12_g1_check.py`. Code: `src/wcf_tasks.py` (P1 render guard),
`convert/yaml_to_jsonl.py` (P4 MOLD_BY_PREFIX), `tests/test_session12.py`. Data:
`data/session12-drafts/D-*.json`. Logs: `logs/20260718-session12-gate-main/`.
