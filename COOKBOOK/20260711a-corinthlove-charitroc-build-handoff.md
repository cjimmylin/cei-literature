# CORINTHLOVE CHARITROC build and cheap-qualification handoff

Date: 2026-07-11 (America/Los_Angeles)  
Bank: `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE/BANKS/07-charitroc/`  
Outcome: **GO for cheap-model qualification scale-readiness**

## 1. What is complete

CHARITROC is generator-built and scale-ready for the currently authorized
cheap OpenRouter workflow. The bank contains 684 four-stage episodes:

- 576 private episodes in 288 matched benign/malicious pairs;
- 96 calibration episodes in 48 pairs;
- 12 public episodes, balanced 6/6 by hidden type and three per cue variant.

Every declared private, calibration, and signal cell is fail-loud asserted.
All 288 private pairs match defeat class: 144 valid-premise/coherent-inference,
72 false-premise/coherent-inference, and 72 no-claim pairs. No non-sequitur
invalid arm remains.

Targeted cue counterbalancing and judge-ID hardening are complete. All 684
judge IDs are unique opaque lowercase UUIDv4 tokens; evaluated-model and judge
payload builders exclude canonical item IDs, canaries, split/family labels, and
hidden truth. Static public observable decoders remain at or below 0.5833 AUC
(pointer suffix 0.525); private visible-token AUC is 0.5417 overall and at most
0.625 in a family. No cue or judge-ID redesign is justified before scale.

## 2. Live cheap-model qualification

All runs were public-only, Azure-pinned, ZDR, no fallback, exact-snapshot
attested, and labeled `live OpenRouter qualification measurement`. They do not
authorize calibration, private execution, freeze, final ranking, or
family-level inference.

### Existing three-model root

Root:
`pilot/runs/20260711-openrouter-cheap-azure-v1-live-v2`

Profile: `cheap-azure-v1`  
Profile SHA-256:
`7ae0aedf01874a22e6ef1b26e6c99422cb2377cae87d0b82f9e80a71da6b4f5a`

Exact snapshots:

- `openai/gpt-5-nano-2025-08-07`
- `openai/gpt-5.4-nano-20260317`
- `openai/gpt-5-mini-2025-08-07`

Qualification report SHA-256:
`25029c4558ef4ffb6e77dbd6e53da29fe2fb6de0e207e01118d3576a36e03f6b`

Fresh final verifier output:

```json
{"profile_id":"cheap-azure-v1","purpose":"qualification-only","scopes":{"access":{"model_count":3,"profile_id":"cheap-azure-v1","scope":"access","valid":true},"canary":{"model_episode_count":12,"profile_id":"cheap-azure-v1","scope":"canary","valid":true},"qualification":{"model_count":3,"profile_id":"cheap-azure-v1","scope":"qualification","valid":true},"smoke":{"model_episode_count":36,"profile_id":"cheap-azure-v1","scope":"smoke","valid":true}},"valid":true}
```

### Exact GPT-5.4-mini correction

Root:
`pilot/runs/20260711-gpt54-mini-azure-v1-live-v1`

Profile: `gpt54-mini-azure-v1`  
Profile SHA-256:
`cc92bedbe4eda1e428373af76036bc803d2961e41a7714da838fe4af9480a359`  
Alias: `openai/gpt-5.4-mini`  
Exact Azure snapshot: `openai/gpt-5.4-mini-20260317`  
Frozen price ceilings: $0.75/M input and $4.50/M output

The dedicated wrapper permits only access, canary, smoke, report, and verify.
An independent review found that a lower-level qualification API could accept
the generic flagship profile. A RED/GREEN fix now rejects non-qualification
profiles at all four public/core episode/probe boundaries; the general flagship
path remains unchanged. The fix was independently re-reviewed PASS.

Mini run counts:

- access: 1/1, first attempt;
- canary: 4/4 model-episodes, first attempt;
- smoke: 12/12 model-episodes, reusing the four canaries;
- accepted stages: 48/48;
- retries/failure artifacts: 0/0;
- input/output tokens including access: 26,988 / 11,270;
- reconstructed provider cost: `$0.070956`.

Qualification report SHA-256:
`905ae96234cd2c88ff1c3699eea564462725cbc33019504a5642fa450b055959`

Fresh final verifier output:

```json
{"profile_id":"gpt54-mini-azure-v1","purpose":"qualification-only","scopes":{"access":{"model_count":1,"profile_id":"gpt54-mini-azure-v1","scope":"access","valid":true},"canary":{"model_episode_count":4,"profile_id":"gpt54-mini-azure-v1","scope":"canary","valid":true},"qualification":{"model_count":1,"profile_id":"gpt54-mini-azure-v1","scope":"qualification","valid":true},"smoke":{"model_episode_count":12,"profile_id":"gpt54-mini-azure-v1","scope":"smoke","valid":true}},"valid":true}
```

## 3. Saturation, discrimination, and stage-3 diagnosis

| Model | Public AUC | S3 belief | S3 action | S3 joint | Stage-4 mean benign / malicious |
|---|---:|---:|---:|---:|---:|
| GPT-5 nano | 0.4444 | 0.5000 | 0.5000 | 0.4167 | 2.3333 / 2.3333 |
| GPT-5.4 nano | 0.6389 | 0.7500 | 0.4167 | 0.3333 | 1.6667 / 0.6667 |
| GPT-5 mini | 0.6528 | 0.5000 | 0.5000 | 0.2500 | 1.5000 / 0.5000 |
| GPT-5.4 mini | 0.7361 | 0.5833 | 0.7500 | 0.4167 | 2.3333 / 0.8333 |

The four-model AUC range is 0.2917. The bank is not saturated and provides
useful coarse discrimination across the authorized cheap panel. These N=12
public results do not establish final ordering or family effects.

The exact GPT-5.4-mini stage-4 distribution is 4 refuse, 3 restrict, 2 verify,
0 conditional, and 3 grant, so its AUC is not produced by a single fixed
operating point. Its weakest localized cell is adversarial-cue belief updating
(1/3 belief correct; 0/3 joint). This is insufficient for an item rewrite:
invalid-case evidence does not prove malicious motive, and three public cases
cannot distinguish construct ambiguity from item difficulty. Belief, action,
and joint channels therefore remain separate, and the balanced cue/judge bank
remains frozen pending replicated localized evidence.

Final diagnostic reports:

- `reports/20260711-openrouter-cheap-qualification-diagnostics-v2.json`
  (SHA-256 `af179c2a0d8aed9b8ced9bf88c96828ca1e805c9a2e3f324cf63b53d92f2bfd3`);
- `reports/20260711-openrouter-gpt54-mini-qualification-diagnostics-v1.json`
  (SHA-256 `246f348ad67ca194eaccde9726b8984e23532b863ca80170a44a02e73ce132b9`).

The earlier non-v2 cheap diagnostic is preserved as superseded provenance.

## 4. Final verification evidence

All commands used
`/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python`.

- Full stable-tree suite: `1009 passed in 2100.65s (0:35:00)`.
- Generator dry-run: 576 private + 96 calibration + 12 public = 684;
  288 private, 96 calibration, and 72 signal cells complete; no writes.
- Matching audit: 288 pairs, zero failures, zero undeclared twins, zero
  manipulated-stage character-budget delta.
- Static adversarial filter: PASS; every scripted policy caught; 684 → 684;
  lexical/metadata leakage gates passed. Every synthetic number retains
  `harness validation, NOT a measurement`.
- Megamatrix export: 1,152 rows = 2 mock models × 576 private episodes; all
  288 cells; 108 calibration/public exclusions; pinned ten-field schema.
- Self-check: all 15 checks PASS, including payload boundary, 684 opaque judge
  IDs, registry, split hygiene, export, mock honesty, and scope/citation scan.
- Exact current OpenRouter secret matches in the bank: 0.
- `git diff --check`: clean.

The interrupted pre-fix suite (`116 passed` before deliberate cancellation) is
not counted as verification; it was stopped because the profile-scope fix
changed code underneath it. Only the later clean 1009/1009 run is authoritative.

## 5. Review and standing conditions

Fresh review memo:
`CORINTHLOVE-REVIEWS/20260711-charitroc-bank-review.md`

Verdict: **GO — scale-ready for cheap-model qualification.** No bank fix is
required. The review was performed by a fresh isolated Codex subagent, not
Opus: the current authorization forbids buying frontier/flagship OpenRouter
calls, and the available subagent interface cannot pin Opus. This deviation is
explicit rather than misrepresented.

Rubric B5's frontier-model filter is the sole standing **pre-calibration**
condition. The static filter passes, but no frontier pass was run. Human/dual
judge calibration and private execution also remain Phase-B activities. None
of these standing conditions blocks cheap public qualification or the next
bank build.

## 6. Operator documentation and next action

Authoritative active-state files now exist:

- `CORINTHLOVE/AGENTS.md` — precedence, WIP=1, cheap-only and exit discipline;
- `CORINTHLOVE/STATUS.md` — one active bank/blocker/next action;
- `CORINTHLOVE/RUNBOOK.md` — exact profile commands, retry rules, and failure
  taxonomy.

The stale dated continuation prompt now points to those files rather than
restarting CHARITROC from an obsolete queue.

Next bank: **CO-8 ③ CROSSROADS (v3-01)**. Its build must add the v3 98 guide,
§7 interim hardness gate, frozen C1–C16 clause tags, and `10CB3-` canaries.
OpenRouter remains cheap-only until the user changes that authorization.

No commit, stage, push, deletion, or sibling-benchmark edit was performed.
