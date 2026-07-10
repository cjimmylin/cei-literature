# ZEROSUM P1 authoring + OpenRouter diagnostic handoff

**Date:** 2026-07-10  
**Design:** `10-zerosum` / `10CB-ZEROSUM-P1`  
**Release boundary:** first 10CBench bank-build session only  
**Authoring status:** DONE  
**Official empirical status:** BLOCKED / NOT RUN

## What is complete

- The deterministic ZEROSUM P1 bank is implemented and reproducible: 40 cores,
  160 open primaries, 80 forced anchors, 160 comprehension twins, 160
  recognition twins, 32 monitoring twins, and 40 no-frame twins (632 records).
- Public/private schemas, payoff certificates, human annotation/calibration,
  shared synthetic/live request scheduling, forced/open scoring, slope and core
  bootstrap analysis, X2 leakage checks, and fail-closed reporting are runnable.
- The credential-free release chain was rerun on 2026-07-10. The complete test
  suite passed **343/343** in 313.52 seconds.
- A bounded OpenRouter diagnostic ran the requested GPT-5.5 / GPT-5.4 /
  GPT-5.4-mini panel over every forced anchor under the separately frozen R2
  transport repair.

This does **not** mean the ten-design program is fully bank-built. ZEROSUM is
the completed first bank-build release; the remaining designs continue from
`TENCOMMANDMENTS-REVIEWS/20260706-PARKED-opus-reentry-prompt.md` and its
ordered governing stack.

## Frozen bank and release validation

| Artifact/check | Result |
|---|---|
| Bank | 632 rows; SHA-256 `e0f656218a69e38aa94ec549f331c7555b237402ea5f74244a74f4512ebfe074` |
| Private gold | 632 rows; SHA-256 `5a751f936a6ea54d4ed77c9b0e386078b8386ba9d8fd78426de9cc7b73aa193b` |
| Bank manifest | SHA-256 `8fe3cf267cc37f1ed1db80a4a0eed795133c5cab1aba187114f439cec52ad5ff` |
| Schema audit | PASS; 0 hard / 0 soft findings |
| Leakage audit | PASS; 0 hard / 0 soft findings |
| Matched-surface audit | PASS; 0 hard / 0 soft findings |
| X2 normalized-style baseline | PASS; 0.2500 accuracy vs registered maximum 0.35 |
| X2 length-only baseline | 0.2500 accuracy (diagnostic) |
| X2 raw bag of words | 0.40625 accuracy (diagnostic only) |
| Fine-tune gate | `NOT_RUN_LLM`; classical surrogate 0.25 is plumbing only |
| Full tests | 343 passed |

The disclosed synthetic run regenerated 5,560 responses (five profiles ×
1,112 scheduled responses). Its status is `HARNESS_VALIDATION_ONLY`, with
`eligible_for_empirical_decision=false`, classifier `NOT_RUN_HUMAN`, live
pilot `BLOCKED_PRECONDITIONS`, and fine-tune gate `NOT_RUN_LLM`. The synthetic
validation result SHA-256 is
`c8addba21aa0416597734e2d35b66f1706c0d99029f9021c652aa98365be35ed`;
the generated authoring report SHA-256 is
`c890e708ad9e578afd11059184ed29e567693dc9c2261c6affc21b08679c700f`.

## OpenRouter protocol history

### v1: preserved technical failure

The original frozen config remains byte-for-byte unchanged at SHA-256
`a22920456868293d51d92814f2daebc9f6de06e6948149c7427097b6291f9f41`.
Its first smoke exposed dated canonical response IDs, which the fail-closed
adapter initially rejected. After canonical attribution was repaired, the v1
smoke passed. The v1 full run was then interrupted after GPT-5.5 showed repeated
null-content `max_output_tokens` truncation. Its append-only checkpoint is
preserved at `pilots/20260710-openrouter-forced-full/` and must not be resumed,
overwritten, or interpreted as benchmark data.

A controlled technical probe showed the same failing request exhausted all
512 output tokens as reasoning and returned null content. With
`reasoning_effort=minimal`, it stopped normally and returned a valid letter.
This was a transport diagnosis, not a score observation.

### R2: frozen repair and live execution

Before any R2 benchmark call, a new config and technical memo froze the repair:

- R2 config SHA-256:
  `b2eeb8f436e172bccebb98529e58de21298081ec69fc5846e40339fe5a61f14c`
- run ID: `10CB-ZEROSUM-P1-OPENROUTER-FORCED-20260710-R2`
- unchanged: seed, roster, 80 anchors/model, scoring, eligibility, blockers,
  and all inferential thresholds
- changed transport only: `max_tokens=1024`,
  `reasoning_effort=minimal`

Two independent offline reviews approved the R2 repair; each reran 113 focused
tests. Cross-protocol smoke proofs fail before catalog or client calls, and the
result/report/manifest bind the exact R2 revision and effective reasoning
effort.

The fresh R2 smoke passed all three models on their first attempts. The full
run then completed 240/240 unique model-item pairs with zero parked items. It
recorded 241 audit attempts: 240 valid choices and one sanitized GPT-5.4
adapter error that succeeded on the one allowed neutral repair.

Actual returned canonical model IDs were:

- `openai/gpt-5.5-20260423`
- `openai/gpt-5.4-20260305`
- `openai/gpt-5.4-mini-20260317`

All 240 valid responses had `finish_reason=stop`. Total observed usage was
144,132 tokens and `$0.714126`; cost metadata was present for every successful
attempt. The failed adapter attempt had no billable usage metadata.

## Frozen saturation/discrimination result

| Model | Valid | Parked | Mechanical accuracy | Endpoint delta | `ZS_design_100` |
|---|---:|---:|---:|---:|---:|
| GPT-5.5 | 80/80 | 0 | 98.75% | 0.00 | 50.0 |
| GPT-5.4 | 80/80 | 0 | 93.75% | 0.05 | 52.5 |
| GPT-5.4-mini | 80/80 | 0 | 88.75% | 0.00 | 50.0 |

Registered descriptive checks:

- valid-response prerequisite: **PASS** (all models 100%, threshold 95%)
- panel ceiling saturation: **NO** (mini 88.75%, threshold 90% for every model)
- accuracy discrimination: **PASS AT THE BOUNDARY** (10.00-point spread,
  threshold 10 points)
- structural discrimination: **NO** (2.50-point ZS spread, threshold 20)
- machine classification: `WITHIN_OPENAI_DESCRIPTIVE_DISCRIMINATION`

The integrity checks independently reproduced `result.json`, the generated
Markdown, all model/item coverage, the audit hash chain, and every manifest
artifact hash. The actual OpenRouter credential had zero exact-value hits in
the smoke or full output trees.

R2 artifact hashes:

| Artifact | Smoke SHA-256 | Full SHA-256 |
|---|---|---|
| attempts JSONL | `c9426442e8fe8a4b820c189af2c7664b2d2e7838323b1d32a0083c0779d037e6` | `e2315e06ff8c8c42206dea0b037886a439b2c7a4b7d79510c1174698d4f365fc` |
| result JSON | `83712285596c468f84a1249efc4d0725d52dca9aca1ef0e20592de00afe559ab` | `b3a589b4717e8c09e3d607b4a13c9ac46e18f22c462be17f857e76e3cd579681` |
| report Markdown | `4963fe8326287a4431657ef49081099088303d6e5ed13113ef6f2daadc8576c7` | `ab19ddeedd62d0848004c973b85138fad546ff989d1a12113ba56595dd38ffcf` |
| manifest JSON | `5c8586620ebdaed73b7856b0d5ffa32f8e70601e8fd7121b9fe61157b61f6bae` | `9c6ee47a12e817e28e735e6023d7de02d2eeb13a369bf70fa8e7a829ed11f02b` |

## Exploratory scale audit (not registered evidence)

The 10-point accuracy result is a boundary pass, not broad evidence that the
forced bank is uniformly discriminating. Without disclosing item keys:

- 69/80 anchors were correct for all three models; 11 were missed by at least
  one model.
- The bank contains 68 welfare-optimal and only 12 sufficiency-keyed anchors.
- Across models, the welfare-optimal stratum was 202/204 correct (99.02%);
  the sufficiency stratum was 23/36 correct (63.89%).
- Sufficiency accuracy was 91.67% for GPT-5.5, 75% for GPT-5.4, and 25% for
  GPT-5.4-mini.
- Thirteen of the 15 total error events were welfare-optimal selections where
  the private key required sufficiency; the other two were positional
  selections against welfare-optimal keys.
- Only 2/240 choices were positional. The endpoint structural signal is
  therefore effectively floor-saturated in this forced-choice panel.

Scale-up should preserve R2 unchanged for replication while expanding and
balancing hard anchor types, especially beyond the sufficiency/welfare
boundary. Use three seeds and a multi-vendor roster before interpreting
stability. Do not replace the open-response instrument with forced anchors:
the primary advice slope, frame-by-rho effect, recovery, refusal, spite, and
sufficiency constructs were not run here.

## Official gates still blocked

1. **Human classifier — `NOT_RUN_HUMAN`.** Collect at least 200 unique open
   responses, code each independently by two blinded humans, adjudicate
   disagreements, and meet every preregistered kappa/F1 threshold.
2. **Official model gate — `SINGLE_MODEL_VENDOR`.** The requested panel has
   three models but one vendor. The official run requires at least three models
   from at least two vendors and exactly three frozen seeds.
3. **Open-response construct — not run live.** No OpenRouter diagnostic in this
   release classifies open advice or invokes a judge.
4. **X2 fine-tune gate — `NOT_RUN_LLM`.** The classical surrogate validates
   split/statistic plumbing only; a real mid-tier LLM probe remains required.

No synthetic or single-vendor result may be used to fill any of these gates.

## Reproduction and next actions

Run commands from `COOKBOOK/40-BIBLEBENCH` with:

```bash
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
```

The exact credential-free commands are in
`TENCOMMANDMENTS-v2/DESIGNS/10-zerosum/README.md`. The R2 paid smoke/full
commands are also documented there and require new empty output directories.

Human annotation packet:

```bash
$PY TENCOMMANDMENTS-v2/DESIGNS/10-zerosum/calibration/export_annotation_packet.py \
  --input private-open-responses.jsonl \
  --coding blinded-coding-packet.jsonl \
  --linkage private/annotation-linkage.jsonl \
  --manifest annotation-packet-manifest.json \
  --sample-size 200 \
  --seed 20260709
```

Program continuation order must be taken from the parked re-entry prompt and
governing documents rather than inferred from this single-design release.
