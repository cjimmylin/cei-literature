# F2 Judge Ablations — Results (arms 2a + 2b)

**Date:** 2026-07-16 (session 5) · **Authorization:** owner GO
(`20260716-owner-ruling-f1-and-spend-go.md`), spend memo Items 2a/2b (ceilings
$0.80/$0.60). Re-judging of stored pilot responses only — zero SUT calls. Verdicts:
`logs/f2-ablations-20260716/` (gitignored). Tools: `tools/audit/judge_ablation.py` +
`ablation_agreement.py`. Optional arm 2c (d02-anchors-on) NOT run (not in the GO).

## Arm 2a — design-07 anchor ablation: the anchors are NOT the main driver of the 07-vs-02 agreement story

Per-turn cross-judge agreement (judge-A gpt-4.1-nano vs judge-B llama-3.3-70b), same
stored responses, with vs without `_DESIGN07_STATE_ANCHORS`:

| SUT | anchored A/B (pilot) | anchor-less A′/B′ | Δ |
|---|---|---|---|
| deepseek-chat | 0.580 | 0.484 | −0.096 |
| gemini-flash-lite | 0.509 | 0.463 | −0.046 |
| gpt-4.1-mini | 0.512 | 0.497 | −0.015 |
| llama-3.3-70b | 0.487 | 0.451 | −0.036 |
| mistral-small | 0.570 | 0.500 | −0.070 |

- Anchors help cross-judge agreement **consistently but modestly**: −0.015…−0.096 when
  removed (same sign all 5 SUTs; mean ≈ −0.05).
- **Attribution:** even anchor-less, 07 agreement (0.451–0.500) sits far above design
  02 (0.218–0.274) and the v1 07 floor ≈0.22. Of the ~26-point 07-vs-02 gap the pilot
  reported, roughly **5 points are the anchors; the rest is the 07 instrument itself**
  (state taxonomy/rubric), not the anchor block. The pilot's suggestive
  anchors-did-it reading is corrected.
- Judge self-consistency across the ablation: judge-A 0.557–0.759, judge-B 0.813–0.856
  — the anchors move judge-A's verdicts far more than judge-B's (foreshadows arm 2b).
- Caveats: anchored side = the single stored pilot draw; ablated side = a fresh decode
  draw, so decode noise is inside Δ (the consistent sign across SUTs is the robust
  part). Single-judge-pair; 07 remains floor-saturated for arc_pass (R11 unchanged).

## Arm 2b — answer-blind ablation (JV-2): verdicts are strongly anchor-dependent, and the dependence is judge-asymmetric

Same stored 03/06/09 responses re-judged with the keyed anchor (and keyed-derived
references) withheld. Delta = blind − visible.

**Judge-A (gpt-4.1-nano): large, design-directional shifts.**
- Design 06: blind scores **lower** almost everywhere (deltas to −0.52; largest on
  `remainder`, `facts`) — with the key visible the judge awards substantially more
  criterion credit.
- Design 03: blind is **more lenient** — `violating` verdicts collapse (e.g., llama
  34→13, gemini 30→12), `expressed_judgment: yes` inflates (deepseek 9→24),
  keypoints_met mostly +0.06…+0.32.
- Design 09: blind `floor_compliance` **much higher** (+0.10…+0.51) — floor violations
  are largely invisible to an unanchored judge.

**Judge-B (llama-3.3-70b): small shifts throughout** — 03 keypoints ±0.08; 06 mostly
within ±0.13; 09 floor_compliance +0.06…+0.11.

Reading: the keyed anchor is doing heavy lifting in judge-A's verdicts (both directions
— stricter on 03/09 violations, more credit-granting on 06), while judge-B's verdicts
barely move. Implications:
- R6's "PROVISIONAL — judge not G5-neutrality-certified" labels on 06/09 are
  empirically justified; anchor-blind judging is NOT a substitute channel for these
  designs (the blind judge misses floor violations).
- JV-2's parrot risk is real but judge-specific: nano-class judges act as
  anchor-matchers; llama-70b behaves closer to an independent evaluator. The
  adversarial-parrot probe set (false-faithful rate) remains the un-run half of F2.
- The 2-judge mandate (R4) gains a mechanism: A and B disagree partly because they use
  the anchor differently, not merely because they read responses differently.

## Tooling disclosure

The first leniency table emitted this session was WRONG (identical "blind" cells across
all 5 SUTs): `ablation_agreement.py` joined ablation rows by sample_id only, and
sample_ids repeat across SUTs, so one SUT's rows overwrote all others. Found via the
identical-distribution signature, fixed the same hour (log-basename scoping,
`_sut_log_basenames`; per-turn mode also gained a native ablated-A′/B′ column verified
against an independent inline computation). No wrong number left this session's
workspace; tables above are post-fix.

## Spend

2a: 1,630 judge calls (~2.7M in-tokens total); 2b: 1,850 calls (~1.7M in). Estimated
combined ≈ $0.5–0.9 vs ceilings $1.40 — within envelope (OpenRouter dashboard is the
exact source of record).
