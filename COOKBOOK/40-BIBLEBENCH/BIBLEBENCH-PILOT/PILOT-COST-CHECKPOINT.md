# BibleBench Cheap General-Purpose Model Pilot Cost Checkpoint

**Status:** `PROPOSAL_ONLY`<br>
**Authorized:** no<br>
**Calls made:** 0<br>
**Spend:** $0.00<br>
**Price evidence checked:** 2026-07-13<br>
**Proposal expires:** 2026-07-20 23:59:59 UTC

This document prepares an owner checkpoint. It does not authorize a credential,
provider call, model output, or spend.

## Proposed four-model panel

| Provider | Exact model ID | Input / 1M | Output / 1M | Context | Route worst case |
|---|---|---:|---:|---:|---:|
| OpenAI | `gpt-5-nano-2025-08-07` | $0.05 | $0.40 | 400,000 | $0.12697 |
| Google | `gemini-2.5-flash-lite` | $0.10 | $0.40 | 1,048,576 | $0.19594 |
| Mistral | `mistral-small-2603` | $0.15 | $0.60 | 256,000 | $0.29390 |
| Anthropic | `claude-haiku-4-5-20251001` | $1.00 | $5.00 | 200,000 | $2.10437 |

The panel contains four currently documented general-purpose text models across
four first-party provider families. Exact routes are proposed to eliminate
hidden third-party fallback. This is a diagnostic panel, not the registered
eight-model formal concordance panel and not a basis for a leaderboard.

Official evidence:

- OpenAI documents GPT-5 nano's pinned snapshot, $0.05/$0.40 token prices,
  400,000-token context, and 128,000-token maximum output at
  <https://developers.openai.com/api/docs/models/gpt-5-nano>.
- Google documents the stable `gemini-2.5-flash-lite` ID, 1,048,576-token input
  and 65,536-token output limits at
  <https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite>, and
  $0.10/$0.40 standard pricing at
  <https://ai.google.dev/gemini-api/docs/pricing>.
- Mistral documents `mistral-small-2603`, its general instruct/reasoning/coding
  role, 256,000-token context, and $0.15/$0.60 prices at
  <https://docs.mistral.ai/models/model-cards/mistral-small-4-0-26-03>.
- Anthropic documents the pinned `claude-haiku-4-5-20251001` ID, $1/$5 prices,
  200,000-token context, and 64,000-token maximum output at
  <https://platform.claude.com/docs/en/about-claude/models/overview>.

## Registered call geometry

Each model occupies one blinded actor position across all 48 episodes:

- 48 condition-blind forecasts;
- 144 primary calls: 48 episodes times C0/C1/C2;
- 144 matched observable probes; and
- 336 pilot calls per model, 1,344 across four models.

The checkpoint adds three harmless non-bank smoke calls per route, for 12 smoke
calls and a maximum of 1,356 total calls. There is no automatic retry and no
provider fallback.

## Conservative token and cost ceiling

Per model, the estimate assumes at most 4,096 input tokens on every call:
1,376,256 pilot input tokens. Output ceilings are 128 tokens per forecast,
the episode-registered primary ceilings (101,232 tokens across the 144 primary
calls), and 256 tokens per probe, totaling 144,240 pilot output tokens. The
three smoke calls reserve another 3,072 input and 768 output tokens.

At the official standard synchronous prices, the four-route worst case is
$2.72117760. A 20% contingency yields $3.26541312. The proposed hard not-to-
exceed ceiling is **$4.00**, with a dispatch stop at $3.60 to reserve $0.40 for
delayed usage reconciliation. Batch and cache discounts are not assumed.

## Mandatory stop rules

1. Do not access credentials or call a provider until Jimmy approves the exact
   roster, routes, ceilings, expiry, and $4.00 NTE in writing.
2. Pass one and the blinded repeat must both be frozen before any pilot call or
   model-output exposure.
3. Cue custody must verify before any cue-contrast-eligible run.
4. Reverify exact IDs, prices, limits, provider routes, decoding parameters, and
   response-contract support immediately before authorization. Expiry or any
   changed fact voids this proposal.
5. Run only the three harmless smoke calls per model. Stop the route unless
   identity, fallback-disabled behavior, decoding, usage, and receipt checks all
   pass.
6. Unknown delivery status is terminal evidence. Never silently replay it.
7. Stop before the next dispatch at $3.60 provider-reported cumulative spend,
   at 1,356 total calls, or on any registered integrity failure.
8. Never exceed $4.00. This document itself authorizes $0.00.

## Preflight unknowns

The cited Mistral model card does not state a maximum output-token value; that
limit must be verified before approval. Account-specific rate limits, regional
availability, billing rounding/tax, and exact parameter support also remain
preflight facts. Any unresolved value is a stop, not an invitation to assume.
