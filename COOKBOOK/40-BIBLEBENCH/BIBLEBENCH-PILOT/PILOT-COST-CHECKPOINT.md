# BibleBench PF-002 Cost Checkpoint

Status: `PROPOSAL_ONLY` — **NOT AUTHORIZED**

Verified from official public documentation on 2026-07-13.
No credential or provider/model endpoint was accessed. Calls: **0**. Spend:
**$0.00**.

## Registered geometry

- 48 executable episodes
- 3 exact general-purpose actors
- C1 primary and matched observable probe
- **288 logical calls**: 144 primary and 144 probe
- Maximum 2 attempts per logical call; rate-limit retry only
- Input cap: 4,096 tokens; output cap: 700 tokens

## Exact worst-case forecast

| Alias | Provider | Model | Two-attempt worst case |
|---|---|---|---:|
| actor-alpha | OpenAI | `gpt-5-nano-2025-08-07` | $0.0930816 |
| actor-beta | Google | `gemini-2.5-flash-lite` | $0.1324032 |
| actor-gamma | Anthropic | `claude-haiku-4-5-20251001` | $1.4584320 |

- Calculated worst case: **$1.6839168**
- Forecast gate: **$3.00**
- Hard not-to-exceed ceiling: **$5.00**
- Proposal hash: `33e1aae176561ecb3c93edf41b9a9682096d088b261cad8297fbed675c63872e`
- Proposal expiry: `2026-07-20`

The forecast charges every logical call at both registered attempts and at both
token caps. Any change to this proposal requires recomputation and separate
owner approval. This checkpoint grants no authority to access credentials,
construct transport, or make calls.
