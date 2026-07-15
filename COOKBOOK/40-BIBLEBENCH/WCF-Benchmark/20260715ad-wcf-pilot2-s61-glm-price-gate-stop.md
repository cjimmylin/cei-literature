# WCF-Bench Pilot 2 — Session 61 GLM price-gate stop

**Date:** 2026-07-15

**Permanent label:** **EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED
OPEN-FIRST SUTS · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL
JUDGE · NON-QUOTABLE**

## Outcome

Jimmy selected the exact Session-60 `PIN CASE FIX`. One TDD regression proved exact
provider-identifier matching, and the minimum implementation changed only the
`minimax/minimax-m3` pin from `MiniMax` to `Minimax`. Independent named-only review passed
with no P1 and no in-scope P2/P3.

The authorized append-only refreshed public preflight then ran once and produced:

`07-PILOTS/20260715-pilot2-public-preflight-v2/`

Its status is **FAILED/NON-EXECUTABLE**. The exact blocker is:

> `pinned provider exceeds frozen price: z-ai/glm-5.2`

The registered StreamLake ceiling is `$0.8533/$2.6818` per million prompt/completion
tokens. The frozen v2 public snapshot returned StreamLake at `$0.9793/$3.0778` per million,
a 14.7662% increase in the conservative per-attempt reservation. Codex did not raise the
ceiling, switch providers, retry the preflight, or infer paid authority.

All other exact model/provider rows, including the corrected `Minimax` pin, passed the
registered validation. Because the five-model validation is incomplete, the failed packet
correctly returns no proposed cap or required balance.

## Conditional offline forecast — not an executable cap

If Jimmy separately authorizes only the current StreamLake price-ceiling refresh and the
same public snapshot otherwise controls, offline arithmetic gives:

| Surface | Conditional amount |
|---|---:|
| 1,150 no-retry SUT calls | `$20.386632567` |
| 1,260-attempt model envelope | `$22.336658291` |
| Five provider canaries, one attempt each | `$0.088637533` |
| Five provider canaries, two attempts each | `$0.177275066` |
| Envelope plus two-attempt canaries | `$22.513933357` |
| 80%-utilization proposed NTE | `$28.15` |

These figures are decision support from the frozen failed snapshot. They are not a
successful preflight result, balance check, cap, or spending authorization. The prior
`$27.03` planning NTE remains superseded as a current forecast but was never approved.

## Custody and cost

- Public calls this session: one model-catalog GET plus five endpoint-metadata GETs.
- Credential or private balance access: none.
- OAuth tasks: none.
- OpenRouter inference calls: none.
- Spend: `$0.00`.
- Empirical progress: `0/1,150` responses, `0/1,130` scorable cells,
  `0/20` diagnostic cells, `0/1,740` judge decisions.
- Earlier failed packet: preserved unchanged at
  `07-PILOTS/20260715-pilot2-public-preflight/`.
- Accepted PPP-1 paper, Pilot 1, frozen bank, prior runs, roster, prompts, scorers, and
  quotability state: unchanged.

## Owner gate

Jimmy must choose one exact disposition:

- **PRICE CEILING REFRESH** — authorize only the frozen StreamLake prompt/completion
  ceiling update to the v2 snapshot's `$0.9793/$3.0778` per million, one exact regression,
  one named-only review, and one append-only public preflight v3. This grants no credential,
  balance, OAuth, inference, or spending authority.
- **DEFER** — retain both failed packets and stop Pilot 2 before empirical execution.

Recommended default: **PRICE CEILING REFRESH**. It retains the exact model and pinned
provider and changes only the public price ceiling. Any later successful preflight must
still return to Jimmy for a separate amount-specific paid ruling.
