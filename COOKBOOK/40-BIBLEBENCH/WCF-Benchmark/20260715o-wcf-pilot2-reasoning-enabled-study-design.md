# WCF-Bench Pilot 2 — Reasoning-Enabled Study Design

**Date:** 2026-07-15
**Status:** OWNER-APPROVED DESIGN · OFFLINE IMPLEMENTATION ONLY
**Authority boundary:** stop after a new zero-paid public-metadata preflight and return
the refreshed amount-specific cap. This document does not authorize credentials, OAuth,
OpenRouter inference, top-up, or a run.

> **EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED OPEN-FIRST SUTS · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Frozen study

Pilot 2 is independent of closed Pilot 1 and the accepted PPP-1 packet. It produces one
response for every bank item from each of five SUTs: MiniMax M3 through MiniMax, GLM 5.2
through StreamLake, DeepSeek V4 Pro through DeepSeek, Qwen3.7 Max through Alibaba, and
Gemma 4 31B through WandB. Meta is excluded because its registered endpoint lacks the
required reasoning control.

Each request uses temperature 0, an 8,192-token completion ceiling, the model-specific
reasoning control, one exact provider, no fallback, required-parameter enforcement,
data-collection denial, and an endpoint price ceiling. Only the final answer reaches the
judge; private reasoning remains private evidence.

The geometry is 1,150 response cells, 1,130 scorable cells, 20 development-only diagnostic
cells, 1,110 scalar-eligible cells, 20 contested outputs, and 1,740 logical judge decisions.
At least 200 of 222 scalar-eligible cells are required for a SUT descriptive aggregate.
Failures are missing, never zero.

## Execution gates

1. Freeze an append-only public-metadata manifest proving the roster, endpoint pins,
   capabilities, prices, prompt ceilings, geometry, retry envelope, and exact cap.
2. Obtain new amount-specific authority.
3. Run the separately authorized 16-record OAuth canary and five synthetic provider
   canaries. Any semantic failure stops the study; only one transport retry is permitted.
4. Validate the first real cell from all five SUTs sequentially, then process the rest in
   three model shards, sequential within each shard.
5. Judge at concurrency one in same-SUT/same-route batches of at most eight, at most
   800,000 serialized bytes per batch and 262,144 per record. Oversized answers remain
   intact but their judge-dependent result is missing.
6. If evidence is sufficient, produce a roster-ordered, permanently non-quotable
   Markdown/HTML/PDF supplement. It may not claim ranking, reasoning effect, release,
   universal scoring, publication readiness, or replacement of the accepted paper.

The planning ceiling is $27.03, subject to refresh. No paid action may begin from this
design alone.
