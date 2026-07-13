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
- Dispatch boundary: no C0/C2 dispatch; no capability twins; fallback disabled
- Retry exposure: at most 2 attempts per logical call, rate-limit only
- Missingness: unknown delivery is terminal missingness
- Forecast: **$1.6839168**, below the **$3.00** forecast gate
- Hard not-to-exceed ceiling: **$5.00**
- Evidence hash: `bcfb95c07c5b5a41af4f8913be28c96e7c946573d975fde8c372955587354b82`
- Registered adapter controls: temperature `0`; maximum output `700`

### Roster

Prices are standard synchronous text input/output USD per million tokens.

| Alias | Provider | Exact model | Exact first-party route | Input / output price | Token caps |
|---|---|---|---|---:|---:|
| actor-alpha | OpenAI | `gpt-5-nano-2025-08-07` | `openai/first-party/responses` | $0.05 / $0.40 | 4,096 input / 700 output |
| actor-beta | Google | `gemini-2.5-flash-lite` | `google/first-party/generate-content` | $0.10 / $0.40 | 4,096 input / 700 output |
| actor-gamma | Anthropic | `claude-haiku-4-5-20251001` | `anthropic/first-party/messages` | $1.00 / $5.00 | 4,096 input / 700 output |

### Frozen contract hashes

- Runner hash: `5fa4367d82d0e32f19cbf5161e878416562cb0871c1181a170e589e6d144749c`
- Adapter hash: `a60922823281ae98968864588b5926c44f65dad225c3efe2b7fbbcacba07cf8e`
- Proposal schema hash: `95d05168c7b87f8fa5186981f6a63a91649ae212142982b5ae24524db7e3b579`
- Artifact schema hash: `e79b1e07c7563c3d435b9d2352611cb034245f7295c2b0041eb011b5be312334`
- Bank-set hash: `a77be21323f4ce6d6cea74ef66ad31651e1d65bb1e894bc1712176d3dc7c29b5`
- Request-registry-set hash: `6dda345264f797a1cb112901486affe4f0d4104f7e191c060ff19371d7826a0f`
- Surface-registry-set hash: `ade2bc05a49f52f277c50d15a47a36233d1b221e5295f1adddb3317822aa7b1b`
- Analysis-contract hash: `35ffeb29530cbb454c90d60892f8c2b47265c7a9361604d44f22d90e36f1de09`
- Adjudication-contract hash: `e716fa5f7fc19b3b8ca143e10b95af0d66105eb42495a85d88b21de6df136520`

### Unresolved pre-call facts

Unresolved facts are account entitlement, live model availability, account
rate limits, taxes, billing rounding, and regional availability or pricing.
They cannot be verified without entering a credential or provider surface.
They remain explicitly unresolved. Any material change requires a refreshed
proposal and owner review.

### Human-readable consistency statement

The proposal hash, evidence hash, geometry, budget, checkpoint, frozen contract
hashes, and blank owner fields above describe the same `PROPOSAL_ONLY` object.
The machine-readable companion is `pf002-preflight-consistency.json`, whose
checkpoint hash is `7a42de7c1374310174a20ca2e4398076fe69c3699758d684325ac60492f9735c`.

## Owner gate

Approval, if granted, must be a separate hash-bound authorization record for
this exact proposal. Any roster, route, price, geometry, expiry, or budget
change requires a new proposal and a new owner decision. This request cannot
authorize itself.

No credential, provider, model, or billing surface was accessed. Calls: **0**.
Spend: **$0.00**. The pilot remains stopped.
