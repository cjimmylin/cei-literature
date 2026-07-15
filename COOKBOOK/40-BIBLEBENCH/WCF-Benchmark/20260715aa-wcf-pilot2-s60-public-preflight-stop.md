# WCF-Bench Pilot 2 — Session 60 public-preflight stop

**Date:** 2026-07-15
**Permanent label:** **EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED
OPEN-FIRST SUTS · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL
JUDGE · NON-QUOTABLE**

## Outcome

Jimmy selected the exact Session-59 `QUALITY FIX`. Eight TDD regressions now cover the
four named custody/authorization defects. The named-only independent quality re-review
passed all four blockers with no new P1 and no P2/P3 finding within scope:

1. settled provider-canary interruption recovery does not reissue transport and additive
   settlement replay reconstructs exact spend;
2. terminal shard failure prevents later peer-cell transport and in-cell retries;
3. ambiguous post-submit transport failure is terminal and never asserted free, while
   retry remains limited to an explicit definitely-not-submitted failure; and
4. full-run OAuth judging requires an exact paid-authorized Pilot-2 manifest plus the
   registered persisted 16-record OAuth-canary PASS before judge construction.

The authorized public-catalog-only preflight then ran once and produced the append-only
packet:

`07-PILOTS/20260715-pilot2-public-preflight/`

Its status is **FAILED/NON-EXECUTABLE**. The exact blocker is:

> `exact pinned provider is unavailable: minimax/minimax-m3`

The frozen protocol pins provider string `MiniMax`. The public endpoint snapshot returned
the same model, price (`$0.30/$1.20` per million), and reasoning-capable vendor endpoint
under provider string `Minimax`. Because the pin is exact and case-sensitive in the
registered manifest builder, Codex did not reinterpret this as a pass, change the pin,
substitute another endpoint, or run a second preflight.

The other four exact SUT/provider rows passed validation. Because the five-model roster is
incomplete, the failed packet correctly returns no proposed cap or required balance.

## Custody and cost

- Public calls: one model-catalog GET plus five endpoint-metadata GETs.
- Credential or private balance access: none.
- OAuth tasks: none.
- OpenRouter inference calls: none.
- Spend: `$0.00`.
- Empirical progress: `0/1,150` responses, `0/1,130` scorable cells,
  `0/20` diagnostic cells, `0/1,740` judge decisions.
- Accepted PPP-1 paper, Pilot 1, frozen bank, prior runs, roster, prompts, scorers, and
  quotability state: unchanged.

## Owner gate

Jimmy must choose one exact disposition:

- **PIN CASE FIX** — authorize only the frozen provider identifier correction
  `MiniMax` → `Minimax`, one regression proving exact public-catalog matching, a
  named-only review, and one append-only refreshed public preflight. This is not authority
  for credentials, balance access, OAuth, inference, or spend.
- **DEFER** — retain the failed packet and stop Pilot 2 before empirical execution.

Recommended default: **PIN CASE FIX**, because the snapshot shows the same frozen model,
same vendor endpoint, same price, and required reasoning parameters; the observed blocker
is the registered provider identifier's capitalization. Codex assigns no ruling and will
not apply the change without Jimmy's written choice.
