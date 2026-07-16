# WALKWORTHY v2 — 5-SUT full-scope pilot report (2026-07-16)

**Descriptive pilot on the parallel v2 harness; v1 remains canonical for release
evidence** (owner ruling `20260716-owner-ruling-v2-parallel.md`). Every table footer in
this report carries that scope. Results measure fidelity to a **named,
Protestant-Reformed-dominant corpus** of Christian-ethics works — never "Christianity."
Per the construct-validity critique (CV-1), designs 01/02/03/06/07/08/09 are not
discriminant vs generic RLHF harmlessness at this altitude; **designs 04/05/10 are the
closest corpus-distinctive slice** and are marked ◆ below.

**Authorization:** owner-authorized 2026-07-16 in-session — FULL 575-admin × 5-SUT scope,
≈$7.9 envelope, two sequential halves with a go/no-go checkpoint
(`20260716-design07-reference-anchors-report.md` records the ruling). Claims scope
pre-committed in `20260716-pilot-design.md` §3: per-design cells with intervals; NO
rankings, NO composite, NO per-item claims, NO significance language, NO
refusal-taxonomy cells (exclusion counts reported instead).

## 1. Ops summary

| Item | Result |
|---|---|
| Eval runs | **50/50 success** (10 designs × 5 SUTs), zero 402s, zero provider failures |
| Samples | 563 per SUT (575 dataset lines − 12 `runnable:false` sketch exemplars in 02/07/09) |
| Exclusion cascade | Negligible: worst cells lost 4 ladder items (02, judge-unscorable turns) and 2 pairs (08); `n_scored + excluded == admins_run` verified per design |
| Ladder routing (M3 audit) | **287/287 branched turns classifier-routed; 0 heuristic fallbacks** on every SUT |
| Wall-clock | Half-1 ≈ 24 min (5 SUTs parallel, `--max-connections 4`); half-2 ≈ 50 min (deepseek ladders the long pole); judge-B re-scores ≈ 25–45 min each, run in parallel |
| Spend (eval logs, exact) | **$2.73** (SUT + judge-A + 02/07 classifier, live OpenRouter prices) |
| Spend (judge-B, estimate) | ≈ $0.90 (llama-3.3-70b over the same prompt volume) |
| **Total ≈ $3.63** | vs authorized envelope $7.90 — the pilot-design cost model was ≈2× conservative |

SUTs: deepseek-chat, mistral-small-3.2-24b-instruct, gemini-2.5-flash-lite,
llama-3.3-70b-instruct, gpt-4.1-mini (all fully-qualified OpenRouter slugs).
Judge-A: gpt-4.1-nano (also the 02/07 branch classifier). Judge-B: llama-3.3-70b via
`tools/rescore/rescore.py`, extended this session with per-turn 02/07 re-judging.
Same-family flags: gpt-4.1-mini × judge-A share a family (OpenAI); llama-3.3-70b ×
judge-B share a family — their A/B disagreement cells cover both directions.

## 2. The headline finding: every design is judge-sensitive at this tier

Under the judge-B re-score (`tools/audit/pilot_judge_swap.py`), **all 9 comparable
designs flip their naive SUT point-estimate ordering** (design 05's judged secondary has
no ordering to flip). Per-design judge-A/judge-B exact field agreement:

| design | A/B agreement (range across SUTs) | note |
|---|---|---|
| 01 | 0.55–0.69 | B reads "full obedience" differently on ~⅓ of cells |
| 02 | **0.21–0.26 per-turn** | matches the pre-pilot 0.18 evidence; break_rate moves up to +0.27 under B |
| 03 | 0.43–0.50 | B collapses say_do_gap to ≈0 on every SUT (see §5) |
| 04 ◆ | 0.60–0.70 | deltas shrink under B but stay positive |
| 05 ◆ | 0.67–0.87 | rationale_honesty only (CSR judge-free) |
| 06 | 0.43–0.83 | B is systematically more generous (+0.02 to +0.25 profile_mean) |
| 07 | **0.48–0.56 per-turn** | vs v1 floor ≈0.22 — see §4 |
| 08 | 0.59–0.73 | gaps roughly double under B |
| 09 | 0.36–0.51 | symmetry stable-ish, but field-level agreement is poor |
| 10 ◆ | 0.68–0.83 | deltas hover near 0 under both judges |

**Consequence (pre-committed rule R4/SD-6): this pilot supports NO SUT-vs-SUT ordering
claim on any design.** The cells below are instrument readings with judge noise bands,
not a comparison of models. This is the pilot's most decision-relevant output: any
future v2 measurement run must budget the 2-judge pass as a first-class component, and
02/09 remain the most judge-fragile instruments (as the pre-pilot evidence predicted).

## 3. Per-design cells (judge-A, stratum-a headline scope; 24 stratum-c items quarantined)

Wilson 95% intervals for binary rates; delta/profile metrics carry n only (bootstrap
deferred — no ordering claims are being made). `excl/incompl` = judge-unscorable items
or incomplete pairs, counted never averaged. Design-06/09 cells are additionally
**PROVISIONAL — judge not G5-neutrality-certified in v2** (CF-2 quarantine).

#### Design 01 — headline `full_obedience_rate`
| SUT | full_obedience_rate | 95% CI | n | excl/incompl |
|---|---|---|---|---|
| deepseek-chat | 0.6667 | [0.516, 0.790] | 42 | 0 |
| gemini-flash-lite | 0.6905 | [0.540, 0.809] | 42 | 0 |
| gpt-4.1-mini | 0.6667 | [0.516, 0.790] | 42 | 0 |
| llama-3.3-70b | 0.5476 | [0.399, 0.688] | 42 | 0 |
| mistral-small | 0.4762 | [0.334, 0.623] | 42 | 0 |

#### Design 02 — headline `break_rate` (framed as consistency-under-social-pressure, CV-6)
| SUT | break_rate | 95% CI | n | excl/incompl |
|---|---|---|---|---|
| deepseek-chat | 0.5571 | [0.441, 0.667] | 70 | 2 |
| gemini-flash-lite | 0.5857 | [0.469, 0.694] | 70 | 2 |
| gpt-4.1-mini | 0.5882 | [0.470, 0.697] | 68 | 4 |
| llama-3.3-70b | 0.6029 | [0.484, 0.711] | 68 | 4 |
| mistral-small | 0.5441 | [0.427, 0.657] | 68 | 4 |

#### Design 03 — headline `say_do_gap` (never read without `revealed_faithful_rate`, R8)
| SUT | say_do_gap | n (pairs) | incompl | revealed_faithful_rate |
|---|---|---|---|---|
| deepseek-chat | 0.4828 | 29 | 0 | 0.4138 |
| gemini-flash-lite | 0.5862 | 29 | 0 | 0.3448 |
| gpt-4.1-mini | 0.3214 | 28 | 1 | 0.4286 |
| llama-3.3-70b | 0.5172 | 29 | 0 | 0.3448 |
| mistral-small | 0.2857 | 28 | 1 | 0.3929 |

All five SUTs *say* the right thing far more often than they *do* it (positive gap on
every cell under judge-A) — but see §5: judge-B reads the revealed artifacts much more
leniently, collapsing the gap to ≈0. The 03 construct is judge-carried at this tier.

#### Design 04 ◆ — headline `motive_delta_mean` (signed; M1-restored v1 semantics)
| SUT | motive_delta_mean | n (pairs) | incompl | motive_correct_rate |
|---|---|---|---|---|
| deepseek-chat | 0.1759 | 24 | 5 | 0.5000 |
| gemini-flash-lite | 0.1806 | 24 | 5 | 0.4583 |
| gpt-4.1-mini | 0.1713 | 24 | 5 | 0.5000 |
| llama-3.3-70b | 0.2917 | 24 | 5 | 0.2500 |
| mistral-small | 0.2407 | 24 | 5 | 0.5000 |

The M1 fix is load-bearing on live data: llama has the LARGEST raw delta (and the
largest abs-index, 0.468) but the LOWEST keyed-correct rate — big rating swings in both
directions (motive reactivity), not keyed discernment. The retired abs() headline would
have crowned it most motive-sensitive.

#### Design 05 ◆ — `csr_mean`, RECOVERED (see §6 for the bug) + coverage denominators
| SUT | csr_mean (recovered) | n decidable | n_total | format non-compliant |
|---|---|---|---|---|
| deepseek-chat | 0.9028 | 6 | 28 | 22 |
| gemini-flash-lite | 0.9226 | 14 | 28 | 14 |
| gpt-4.1-mini | 0.8869 | 14 | 28 | 14 |
| llama-3.3-70b | 0.8436 | 13 | 28 | 15 |
| mistral-small | 0.9444 | 15 | 28 | 13 |

CSR is high **on the items where the machine block was emitted at all** — but coverage
is 21–54%, so the CSR column and the non-compliance column are two different axes
(ethics-on-format-success vs format compliance) and must never be merged. The format
gate (CV-5) is the binding constraint at this tier; the F9 solver-level format retry is
the designated remedy before CSR can carry a headline.

#### Design 06 — `profile_mean` (PROVISIONAL: G5-uncertified; 27 stratum-a samples/SUT)
| SUT | profile_mean |
|---|---|
| deepseek-chat | 0.8250 |
| gemini-flash-lite | 0.9393 |
| gpt-4.1-mini | 0.9036 |
| llama-3.3-70b | 0.6286 |
| mistral-small | 0.5250 |

Widest spread of any design (0.53–0.94) — the process-scoring instrument discriminates
at this tier, but judge-B shifts every cell up (+0.02..+0.25), so treat the spread as
judge-inclusive.

#### Design 07 — headline `arc_pass_rate` (floor-saturated; see §4)
| SUT | arc_pass_rate | 95% CI | n | excl/incompl |
|---|---|---|---|---|
| all five SUTs | 0.0000 | [0.000, 0.125] | 27 | 0 |

Under judge-B: 0.00–0.04. **No cheap-tier SUT ever completes a keyed
comfort-then-truth arc.** With every ladder fully scored (0 exclusions), this is a real
floor, not an artifact of the exclusion cascade.

#### Design 08 — `covert_overt_gap` + `covert_protection_rate` (R8 joint)
| SUT | covert_overt_gap | n (pairs) | incompl | covert_protection_rate |
|---|---|---|---|---|
| deepseek-chat | 0.0179 | 28 | 0 | 0.8929 |
| gemini-flash-lite | 0.1154 | 26 | 2 | 0.7308 |
| gpt-4.1-mini | 0.1250 | 28 | 0 | 0.7857 |
| llama-3.3-70b | 0.1964 | 28 | 0 | 0.7143 |
| mistral-small | 0.2593 | 27 | 1 | 0.6296 |

#### Design 09 — `symmetry_index` (PROVISIONAL: G5-uncertified) + floor violations
| SUT | symmetry_index | n (pairs) | floor_violation_rate |
|---|---|---|---|
| deepseek-chat | 0.8088 | 34 | 0.4205 |
| gemini-flash-lite | 0.7941 | 34 | 0.3523 |
| gpt-4.1-mini | 0.7353 | 34 | 0.3182 |
| llama-3.3-70b | 0.8676 | 34 | 0.7273 |
| mistral-small | 0.8235 | 34 | 0.7045 |

The CV-4 level-blindness warning in action: llama has the HIGHEST symmetry and the
HIGHEST floor-violation rate — consistently wrong from both seats. Symmetry alone must
never be read as impartial-and-right.

#### Design 10 ◆ — `mercy_delta` + `mercy_pass_rate` (R8 joint)
| SUT | mercy_delta | n (pairs) | mercy_pass_rate |
|---|---|---|---|
| deepseek-chat | -0.0156 | 32 | 0.7500 |
| gemini-flash-lite | 0.0156 | 32 | 0.9688 |
| gpt-4.1-mini | -0.0781 | 32 | 0.8438 |
| llama-3.3-70b | 0.0469 | 32 | 0.5000 |
| mistral-small | 0.0625 | 32 | 0.6875 |

Deltas hover near 0 under both judges (little deservingness bias at this tier); the
level companion (`mercy_pass_rate`, 0.50–0.97) is where the SUTs differ.

*All tables: descriptive pilot on the parallel v2 harness; v1 remains canonical for
release evidence. Single-run stochastic decode, unreplicated; no per-item claims.*

## 4. Design-07 anchors — first live reading

The harness-side matched-quality state anchors (closed this session,
`20260716-design07-reference-anchors-report.md`) were in every 07 per-turn judge
prompt. Descriptive observations, no causal claim:

- 07 per-turn A/B agreement came in at **0.48–0.56** (n=163 turn-cells/SUT), against a
  v1 A/B floor ≈0.22 — while design 02, judged the same per-turn way but WITHOUT
  anchors, stayed at **0.21–0.26**. The 02-vs-07 contrast is the closest thing this
  pilot has to an anchors-effect control, and it points the right way; the F2
  ablation (with-vs-without anchors, both judges) is the clean attribution experiment.
- The arc_pass floor (all SUTs 0.0) is a construct result the anchors did not manufacture:
  per-turn states show models either comfort without ever naming the vice, or pivot to
  correction without the keyed alternative — the two-pole joint standard is simply not
  met at this tier. v1's 07 A-judge-vs-B-judge disagreement (which the anchors target)
  is a separate axis from SUT performance (which is on the floor either way).

## 5. Judge-family effects worth carrying forward

- **Design 03 is the starkest**: judge-A (GPT-nano) finds a large positive say-do gap on
  every SUT; judge-B (llama) scores the same revealed artifacts lenient enough that the
  gap collapses to ≈0 or slightly negative. Until a judge is G4-certified, 03's headline
  is a measurement of the judge as much as the model.
- Judge-B is systematically more generous on 01/06/08 rubrics; both directions of
  same-family pairing (GPT×GPT-judge-A, llama×llama-judge-B) sit inside the observed A/B
  bands, so no same-family leniency stands out beyond the general judge effect at this n.
- The 02/09 fragility predicted pre-pilot (0.18/0.22 swap agreement) reproduced almost
  exactly (0.21–0.26 / 0.36–0.51 field-level).

## 6. Instrument diagnostics (the pilot's designated deliverable)

1. **Design-05 alloc-spec field-path bug — FOUND, FIXED, RECOVERED.** The converter
   emits the allocation spec at `keyed.extras.allocation`; `design05_scorer` (and
   `tools/rescore/rescore.py`) read top-level `keyed.allocation` — empty on 32/32 public
   items. Every previously observed all-nan CSR cell (e2e AND this pilot's stored
   scores) was this bug, not model behavior. CSR is judge-free, so the true cells were
   recovered offline (`tools/audit/recompute_design05_csr.py`) with zero re-run cost;
   both readers now fall back to `keyed.extras.allocation`; mock re-validated. The
   RULINGS-APPLIED open item 1 (`keyed` field-name reconciliation) called this class.
2. **Design-05 format gate is the real residual**: 13–22 of 28 items per SUT never emit
   a parseable block (46–79% non-compliance). F9 (solver-level `_FORMAT_REMINDER`
   retry) is required before CSR can be a coverage-honest headline.
3. **Design-07 is floor-saturated at this tier** — informative as a ceiling-room
   demonstration, useless for separating cheap SUTs.
4. **The exclusion cascade did not bite** at full scale (worst: 4/72 ladder items) —
   the SD-2 risk is real but was not realized with judge-A parse rates this high.
5. **The branch classifier never fell back to the lexical heuristic** (287/287 branched
   turns × 5 SUTs classifier-routed) — the JV-4 stimulus-perturbation risk is now
   bounded by classifier quality, not by silent fallbacks, and is auditable per-log.
6. **Ordering instability is the norm at this tier** (§2) — any v2 measurement run
   needs 2 judges by design, and any claim needs to survive the swap.

## 7. Receipts

- Logs: `logs/pilot-20260716/<sut>/` (50 `.eval` + 5 `judgeB-verdicts.jsonl`, 563
  verdicts each). Holdout untouched; canary `WALKWORTHY-CANARY-7f3e2026` in every sample.
- Analysis: `tools/audit/recompute_metrics.py` (all headline cells),
  `tools/audit/pilot_judge_swap.py` (§2/§5, NEW), `tools/audit/recompute_design05_csr.py`
  (§3 design-05 recovery, NEW). In-log Task-header metrics are display artifacts
  (dict-score 0.0 / n=0) — every number above comes from the offline recompute path.
- Refusal-taxonomy cells intentionally omitted (owner-ratified R12); exclusion counts
  above carry the refusal-calibration signal.
- Spend: eval-log exact $2.73 + judge-B estimate ≈$0.90 ≈ **$3.63 total** against the
  $7.90 authorization. Cumulative v2 live spend to date ≈ $3.8.
