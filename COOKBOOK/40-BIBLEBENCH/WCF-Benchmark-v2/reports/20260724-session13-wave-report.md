# WCF-Benchmark-v2 — Session 13 Wave Report (hardening pass; re-gate NO-GO)

**Executed:** 2026-07-24 per `20260724-session13-hardening-boot-prompt.md`
· **Bank:** v2.4 (unchanged — no items admitted) · **Harness:** panel median of
gemini-2.5-flash + deepseek-chat + mistral-small-2603, last-match parser.
**All numbers EXPLORATORY / NON-QUOTABLE; 0–100 rubric conformity, not accuracy.
Scores are panel-median rubric-conformity ranks, not absolute values. No
pre-registration framing (vault v1.x directive).**

## Headline

**The hardening pass (63-item double-hazard rebuild) cleared authoring and the blind
kill-loop (80 items, 0 kills) but again FAILED the live re-gate: 25/80 = 31.2%
nonzero |qwen−haiku|, below the pre-stated ≥⅓ (needs ≥27 of 80) — 2 items short.**
Unscored 0, missing 0, no all-SUT-zero items. This is the **second consecutive
NO-GO** → owner STOP-POINT engaged; no third run authorized; bank stays v2.4; no
items admitted. Gate results: `analysis/20260724-session13-gate-results.json`.

## Mission (owner-ruled 2026-07-24)

Freeze the 17 s12 discriminators, rebuild the other 63 to the double-hazard template
(two co-present errors requiring opposite handling; GATE cap-40 naming BOTH
directions), and re-gate all 80 under the **unchanged criterion** within the ≤$4
remainder. Boot prompt: `20260724-session13-hardening-boot-prompt.md`.

## Phase 1 — rebuild (63 items, $0 Agent channel)

8 opus rebuilders (2 per mold), **63 items rebuilt in place keeping ids**:
14 MEND / 15 LIB / 18 PROOF / 16 WHOLE. Most scenario seeds were kept with a grafted
opposite-handling flank; **6 seeds replaced** (MEND-N-005/010, LIB-N-004 (recast) /
LIB-N-010 (recast), WHOLE-N-003/005/007/008 — the WHOLE-a batch replaced 4).

Two structural mechanisms emerged during the rebuild: **Track-A drafting artifacts**
(clauses that themselves need opposite handling) and **matched-pair verdicts**
(acquit-the-innocent-looking-guilty / convict-the-guilty-looking-gracious).

**Provenance.** Rebuilt items carry `authored: session-13`, batches
`R-<MOLD>-<a|b>`; the frozen 17 keep `session-12`.

## Phase 2 — blind kill-loop: **0 KILLS, 4 major + ~20 minor repairs**

16 blind adversarial opus reviewers (lens A form/gradeability, lens B
construct/difficulty/doctrine; anti-leakage constraints enforced; **no reviewer
opened a sibling file**). Result: **0 KILLS, 4 major + ~20 minor repairs**, all
Fable-adjudicated. The 4 majors are all the same defect class the hardening
targets — a cartoon or duplicated flank collapsing an item to single-direction:

1. **LIB-N-002** — legalism flank near-duped FROZEN LIB-N-009/012 → rebuilt off the
   covenant seed to a business operating agreement.
2. **LIB-N-006** — cartoon fraud flank carried the heaviest criterion → subtilized +
   rebalanced.
3. **PROOF-N-009** — "tear up every mortgage" → seductive debt-free-piety over-bind.
4. **PROOF-N-015** — "printed verse = idolatry" → defensible all-illustration
   scruple; de-duped from PROOF-N-019.

The 4 majors got a fresh 2-reviewer round: **4/4 KEEP**. One adjudicated reviewer
conflict: **WHOLE-N-020's `end` axis tag retained** (lens B + exemplar convention
overrule lens A). One author-facing **"NOTE ON SEED" leak stripped** from LIB-N-002's
key post-review.

**G1.** `analysis/session13_g1_check.py` (extends the s12 checks + a new
two-direction GATE heuristic): **80 items, 0 violations, 2 flags** (MEND-N-005/007)
ruled **checker-vocabulary false positives** — the GATEs are structurally
two-directional; the checker's trigger lists simply lacked "canceling / forgiving /
shutting down." This is the s12 "review-tied" precedent.

**G3.** `$0` mockllm (mock SUT + mock grader, strictly $0): **80/80 success**, no GOLD
ORDER leaks, ASTT present in all PROOF targets, per-line `[anchor:]` rendering in all
80; **two soft length warnings** (WHOLE-N-002/008 grading standards 6,677 / 6,856
chars > 6,000) — non-blocking. Merged dataset `data/session13_new_items.json`
(63 + 17); `data/wcf_s12_new_main.jsonl` regenerated (task name retained as the
tranche runner).

## Phase 3 — live re-gate (2026-07-24): **NO-GO**

3 SUTs via OpenRouter — qwen/qwen3.7-plus (~23 min), anthropic/claude-haiku-4.5
(~6 min), openai/gpt-4o-mini (~5 min) — × 80 items, default 3-judge median panel
(gemini-2.5-flash / deepseek-chat / mistral-small-2603), `--max-connections 8`, logs
`logs/20260724-session13-gate-main/`. Run shape identical to s12 (whose spend was
~$1.5–2); within the ≤$4 remainder. Eval: `analysis/session13_gate_eval.py` (4-line
diff from s12; criterion verbatim).

**VERDICT: NO-GO — 25/80 (31.2%) nonzero |qwen−haiku| < pre-stated ≥⅓
(needs ≥27 of 80; 2 items short).** Unscored 0, missing 0, all-SUT-zero 0. Results:
`analysis/20260724-session13-gate-results.json`.

## Phase 3 decomposition — a test-retest finding about the criterion

25/80 (31.2%) nonzero — up from s12's 17/80 (21.2%), still below the 26.67 required.
Split by provenance:

- **FROZEN 17 → only 11/17 re-discriminated.** Dropped: LIB-N-012, MEND-N-001,
  MEND-N-008, PROOF-N-008, PROOF-N-011, WHOLE-N-016.
- **REBUILT 63 → 14/63 (22.2%) discriminated:** LIB-N-002, MEND-N-015, MEND-N-018,
  PROOF-N-002/004/006/013/015/017/018, WHOLE-N-005/011/012/015.

**The frozen-asset drop is a test-retest reliability finding about the criterion
itself:** 6 items admitted as discriminators produced *zero* gap on re-measurement
under identical conditions. The per-item nonzero-gap binary is substantially
run-noise.

**Per-mold nonzero (frozen contribution in parens):** MEND 6/20 (4) · LIB 5/20 (4) ·
PROOF 7/20 (0 — all seven rebuilt; PROOF went from worst mold in s12, 2/20, to best)
· WHOLE 7/20 (3).

**Saturation.** qwen=100 on **68/80** (s12: 69/80 — essentially unchanged);
haiku=100 on 57/80. The gap gain came almost entirely from **haiku dropping, not qwen
falling.** Tied 100-100: 53 (s12: 55). GATE cap engaged **exactly once**
(LIB-N-002, gap 75.0).

| SUT | MEND | LIB | PROOF | WHOLE |
|---|---|---|---|---|
| qwen3.7-plus | 96.6 | 99.0 | 95.8 | 98.7 |
| claude-haiku-4.5 | 98.8 | 91.2 | 94.8 | 94.7 |
| gpt-4o-mini | 90.0 | 58.1 | 55.6 | 51.0 |

**gpt-4o-mini spreads hugely → the instrument has range; saturation remains
qwen-haiku-pair-specific.** Top gaps: LIB-N-002 75 · LIB-N-001 33 · WHOLE-N-001 32 ·
LIB-N-005 30 · WHOLE-N-010 27 · PROOF-N-015 25 · MEND-N-015 25 · LIB-N-009 25.

## Tied-100 meta-audit — the hardened GATEs held

Opus, $0, qwen transcripts, 6-item sample weighted to major-repaired items that still
tied (`analysis/20260724-session13-tied100-meta-audit.md`): **the hardened GATEs held
6/6** — qwen genuinely handled BOTH halves of every sampled double hazard; the s12
defect (judges under-enforcing the unbind half of a committed GATE error) **did NOT
recur.**

- **4/6 GENUINE-100.**
- **2/6 over-credits on NON-gated rubric lines:** LIB-N-006 real ~83 (no restitution
  to past victims — deepseek + mistral showed the s12 false-justification tell
  "demands restitution" while gemini scored 83 correctly); PROOF-N-009 real ~83–91
  (outline vs delivered script; mistral defensibly stricter at 75).

**Diagnosis:** remaining ceiling is (a) genuine qwen excellence on rubric-conformity
plus (b) **median-of-3 panel leniency washing out correct stricter dissents** — an
instrument property, not an item-construct failure.

## Owner STOP-POINT (engaged, 2026-07-24)

**Second consecutive NO-GO.** Per the boot prompt: **stop; no third run authorized;
bank stays v2.4; no items admitted.** Decision points for the owner (Fable
synthesis — NOT decided here):

- **(a)** Close the tranche as NO-GO and retain v2.4.
- **(b)** Revisit the criterion (previously declined). The frozen-17 instability and
  the 2-item shortfall both bear on whether a single-run nonzero-gap binary is the
  right admission evidence — epochs, gap-magnitude thresholds, or 3-SUT spread are
  the obvious variants.
- **(c)** Admission on different evidence: gpt-4o-mini's spread shows the items
  discriminate within-tier-2.
- **(d)** A session-14 aimed at the **judge panel** (leniency median) rather than the
  items — the meta-audit locates the residual defect judge-side.

## Standing caveats

EXPLORATORY / NON-QUOTABLE. Scores are panel-median rubric conformity — ranks, not
absolute values. Single gate run per SUT (no epochs). The meta-audit sampled qwen
only, 6 items. Any future v2.5 is a separate instrument — no cross-version comparison
(bank-versioning rule).

## Artifacts

Report: this file. Boot prompt: `20260724-session13-hardening-boot-prompt.md`.
Drafts: `data/session13-drafts/` (8 `R-*` batches + `reviews/`). Data:
`data/session13_new_items.json` (63 + 17), regenerated `data/wcf_s12_new_main.jsonl`.
Analysis: `session13_g1_check.py`, `session13_gate_eval.py`,
`20260724-session13-gate-results.json`, `20260724-session13-tied100-meta-audit.md`.
Logs: `logs/20260724-session13-g3-mockllm/`, `logs/20260724-session13-gate-main/`.
