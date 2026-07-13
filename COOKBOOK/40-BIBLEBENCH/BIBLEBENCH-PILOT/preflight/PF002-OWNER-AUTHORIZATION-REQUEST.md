# PF-002 Owner Authorization Request

Status: `NOT_AUTHORIZED`

Owner: _blank_

Approval reference: _blank_

Authorization nonce: _blank_

Run ID: _blank_

## Exact proposal presented for separate owner decision

- Proposal ID: `pf002-three-model-proposal-20260713`
- Proposal hash: `33e1aae176561ecb3c93edf41b9a9682096d088b261cad8297fbed675c63872e`
- Expiry: `2026-07-20`
- Geometry: 48 episodes × 3 actors × C1 primary plus matched probe = **288 logical calls**
- Retry exposure: at most 2 attempts per logical call, rate-limit only
- Forecast: **$1.6839168**, below the **$3.00** forecast gate
- Hard not-to-exceed ceiling: **$5.00**
- Evidence hash: `b07c2ad71bc01f84c8dbbdf95106bda09f8b808e7fcab88c45219ccc075272e9`

### Roster

- `actor-alpha`: OpenAI `gpt-5-nano-2025-08-07` via `responses`
- `actor-beta`: Google `gemini-2.5-flash-lite` via `generate_content`
- `actor-gamma`: Anthropic `claude-haiku-4-5-20251001` via `messages`

## Owner gate

Approval, if granted, must be a separate hash-bound authorization record for
this exact proposal. Any roster, route, price, geometry, expiry, or budget
change requires a new proposal and a new owner decision. This request cannot
authorize itself.

No credential, provider, model, or billing surface was accessed. Calls: **0**.
Spend: **$0.00**. The pilot remains stopped.
