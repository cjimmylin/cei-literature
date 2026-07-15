# Jimmy authorization — WALKWORTHY OPEN6-SOL1

**Date:** 2026-07-14

**Owner:** Jimmy Lin

**Status:** AUTHORIZED in direct chat after review of the complete pilot plan and its
OpenRouter cost estimate

## Authorized order

Jimmy authorizes implementation and execution of `WALKWORTHY-OPEN6-SOL1` within the
following exact boundary:

- evaluate every one of the 344 runnable **PUBLIC** WALKWORTHY items once for each of
  these exact OpenRouter SUTs: `minimax/minimax-m3`, `z-ai/glm-5.2`,
  `deepseek/deepseek-v4-pro`, `qwen/qwen3.5-397b-a17b`,
  `google/gemma-4-31b-it`, and `meta-llama/llama-4-maverick`;
- use OpenRouter for SUT calls only, with price-sorted same-model providers, the
  frozen 110% provider ceilings, a 2,048-token output cap, no model substitution,
  and no free aliases;
- use exact `gpt-5.6-sol` through the existing Codex ChatGPT OAuth session, at medium
  reasoning, for adaptive 02/07 routing and the single descriptive judge;
- make one trajectory per item-model pair and one Sol judgment per logical scoring
  unit, with same-design/schema judge batches of at most 24 units;
- permit one byte-identical replay only after a transport, empty-output, malformed
  required-output, or custody defect; retain the first defect, never rerun valid
  substantive output, and leave a key unresolved after its second failure;
- enforce 5,886 nominal OpenRouter calls, a 295-call replay reserve, and a 6,181-call
  hard cap; enforce 1,949 nominal Sol turns, a 98-turn replay reserve, and a
  2,047-turn hard cap;
- stop before OpenRouter spend can exceed **$25.00 hard NTE**; do not purchase OAuth
  credits automatically and pause on OAuth quota exhaustion;
- retain full request/response, returned-model, token, cost, defect, and hash custody;
- never load HOLDOUT, substitute or add a model, change an item/key/denominator,
  increase concurrency beyond two, or scale automatically.

The expected OpenRouter spend reviewed by Jimmy was approximately **$11.10**. The
authorized $25.00 NTE is the conservative ceiling for provider variation and the
registered defect-replay reserve, not a target.

## Claims and paper boundary

The resulting evidence is a **descriptive single-judge MVP** only. It does not
authorize an O5 verdict, G4 validation, release determination, judge-reliability
claim, repeated-run stability claim, universal best-model claim, or cross-design
composite. Results belong in a new standalone supplement; the hash-frozen private
MVP v0.1 manuscript and PDF remain byte-unchanged.

This authorization is Jimmy's explicit owner exception to the earlier labels-only
critical path and new-model/scale-up deferral. Human labels → G4 → O5 verdict assembly
remain the release-grade critical path. The exception permits this one bounded
descriptive pilot; it does not reopen general model expansion.

## Execution condition

The first implementation stage is documentation-only freeze/preflight with no
credential access or live call. Production execution must use the byte-frozen
manifest produced by that preflight and pass the registered offline and canary
checks. Any unregistered behavior stops the affected thread; it does not begin a
new serial specification chain or authorize an improvised workaround.
