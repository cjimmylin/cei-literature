# WALKWORTHY OPEN6-SOL1 — freeze/preflight order

**Date:** 2026-07-14

**Mode:** documentation-only preflight; no credential access and no live call

**Owner authorization:** `20260714-jimmy-open6-sol1-authorization.md`

## Paper-facing purpose

Produce a standalone private descriptive supplement covering the full runnable PUBLIC
bank with one trajectory from each of six current open-weight model families and one
blinded Sol reading per logical scoring unit. This is a bounded exploratory extension,
not a substitute for human labels, G4, O5, or the release-grade paper path.

## Frozen surface and derived geometry

The preflight must call
`load_public_split(include_exemplars=True, runnable_only=True)`, sort canonically by
design and item ID, and fail closed unless it finds the registered surface:

| Quantity | Registered value | Mechanical derivation |
|---|---:|---|
| Runnable PUBLIC items | 344 | normalized loader output |
| Item × SUT records | 2,064 | 344 × 6 |
| SUT content calls | 5,694 | 949 structural calls/model × 6 |
| Design-05 allocation calls | 192 | 32 PUBLIC items × 6 |
| OpenRouter nominal calls | 5,886 | 5,694 + 192 |
| 02/07 classifier turns | 1,722 | (178 + 109) branch turns/model × 6 |
| Sol judge units | 5,370 | 895 scoring units/model × 6 |
| Category cells | 10,008 | 1,668 cells/model × 6 |
| Same-design Sol batches | 227 | sum of per-design `ceil(6 × units-per-model / 24)` |

The item count, ordered-item SHA-256, every per-design structural count, and each total
must be materialized in the canonical manifest. A surface or geometry change is a hard
preflight stop, not permission to revise a denominator.

## Exact model and price snapshot

Prices are the OpenRouter catalog observations reviewed on 2026-07-14, stated as
USD per million input/output tokens. The provider ceiling for each side is exactly
110% of the observed price.

| Exact SUT slug | Input | Output | Input ceiling | Output ceiling |
|---|---:|---:|---:|---:|
| `minimax/minimax-m3` | $0.30 | $1.20 | $0.33 | $1.32 |
| `z-ai/glm-5.2` | $0.903 | $2.838 | $0.9933 | $3.1218 |
| `deepseek/deepseek-v4-pro` | $0.435 | $0.87 | $0.4785 | $0.957 |
| `qwen/qwen3.5-397b-a17b` | $0.385 | $2.45 | $0.4235 | $2.695 |
| `google/gemma-4-31b-it` | $0.12 | $0.35 | $0.132 | $0.385 |
| `meta-llama/llama-4-maverick` | $0.20 | $0.80 | $0.22 | $0.88 |

Use the neutral term **open-weight**; the roster is not uniformly OSI-open-source.
No optional cross-provider reasoning parameter is sent to the SUTs. The exact model,
output cap, provider policy, request payload, returned model, usage, and cost must be
captured for every later attempt.

## Cost, time, and hard stops

- Expected OpenRouter spend: approximately **$11.10** from the prior MVP token ledger
  scaled to the full six-model surface.
- Conservative planning envelope: approximately **$21–23**, including price variation
  and the registered replay reserve.
- Hard OpenRouter NTE: **$25.00**; reserve 295 calls above the 5,886 nominal calls;
  hard call cap 6,181.
- Sol OAuth: no OpenRouter cost and no predictable incremental cash charge while
  included ChatGPT capacity suffices. Do not buy credits; pause on quota exhaustion.
- Expected implementation/preflight work: 6–10 active hours. Expected production
  wall time: 8–18 hours for OpenRouter plus 8–24 hours for Sol, followed by 4–6 active
  hours for analysis and the supplement. Plan for 2–4 calendar days with sufficient
  OAuth capacity, longer if usage limits require pauses.

Stop on surface/hash drift, failed offline tests, failed canary, missing exact-model or
reported-cost custody, unavailable registered model, second defect for a logical key,
projected NTE breach, call/turn-cap exhaustion, OAuth quota exhaustion, HOLDOUT contact,
or any unregistered behavior. No substitution, fallback model, automatic concurrency
increase, automatic scale-up, or denominator repair is authorized.

## Freeze/preflight implementation order

1. Add a narrow `walkworthy.open6_sol1` module with no credential/live-backend import.
2. Derive and assert the item, call, classifier, judge-unit, category-cell, and batching
   geometry from current item structures and registered scoring specs.
3. Build canonical JSON containing the complete ordered item list, exact roster and
   prices, provider ceilings, execution caps, Sol contract, and claims boundary.
4. Expose only a `preflight` CLI phase. It may create a new manifest or byte-validate
   the same manifest; it must refuse to overwrite divergent existing bytes.
5. Run focused tests without credentials. Live canary and production mechanics are a
   later implementation phase and must not be smuggled into this preflight layer.

## Claims boundary and closing artifact

The final supplement may report per-design and per-model descriptive metrics, hard-tier
readings, category distributions, refusal behavior, and explicit missingness. It must
state that one stochastic trajectory and one unvalidated judge do not support stability,
reliability, gate, release, or universal-ranking claims. It must not edit the frozen MVP
v0.1 manuscript/PDF or any frozen O5 document.

The closing execution session must deliver the validated standalone supplement/PDF,
one claims-conformance checklist, a dated handoff, and one dashboard update. Ancillary
engineering is permitted only where it directly unlocks those paper-facing outputs.
