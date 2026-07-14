# WALKWORTHY — O5 W5/G7 Production Paid-Run Preflight

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Prepared by:** Codex
**Status:** DOCUMENTATION COMPLETE; NO CREDENTIAL ACCESS OR PAID CALL AUTHORIZED
**Scope:** O5 W5/G7 PUBLIC perturbation batteries only; no HOLDOUT, labels, item/key
edits, metric changes, gate verdict, or paper claim

## 1. Entry custody is complete

Jimmy's PR-23 and PR-24 ratifications are recorded verbatim in
`20260713i-jimmy-pr23-pr24-ruling.md`. The resulting no-call production surface is:

| Custody object | Exact binding |
|---|---|
| A2 PUBLIC production manifest | 73 items; 6 fixed O5 SUTs; 438 item×model cells per battery; 876 perturbed cells total; SHA-256 `616d2e93491adcb8da9fc00664693cd8c4685a95fc36b6fc09816c32414edf0e` |
| PR-23 role manifest | 73 item declarations; 108 personal given-name roles; 304 exact model-visible occurrences; 5 explicit zero-role items; file SHA-256 `013600bd2f1c34b7353319e98395aa8b1b5b921796d73a840e5ddc2138027480` |
| L7 inventory binding | version `2026-07-12-rj13-v1`; SHA-256 `73711dd6ae89989ae0dfdad67a7a9516b84518eff0366e30fa061c70496b70b0` |
| Per-design exclusion binding | SHA-256 `a6ebbe8f81f236033779c9d6113923ba7419de16e2d142ca622bc37c98fa0366` |
| Design-05 category | frozen judge-free allocation CSR: `all_constraints_met` iff CSR=1; otherwise `one_or_more_constraints_violated`; malformed/uncomputable remains unresolved |

The five fixed-denominator zero-role items are `WW-01-A01`, `WW-01-B02`,
`WW-03-B01`, `WW-04-B05`, and `WW-10-A01`. They are no-op name-swap cells, not
replacement candidates and not denominator exclusions.

The final original-response source is
`runs/20260713-o5-home-reroute/scored_items.jsonl`; all 438 selected item×model keys are
present. No original SUT response is rerun for G7. Under the PR-24 reducer, 316 original
outcomes resolve and 122 remain pending, including 6/42 design-05 cells. The existing
original surface therefore already implies at least 215 human Part-B rubric entries.
Paid perturbation execution alone cannot make G7 final: E3 keeps the fixed denominator
PENDING until all original and perturbed cells complete the frozen P1/Part-B path.

## 2. Exact model roster and current public prices

Public OpenRouter model/provider pages were checked without credentials on 2026-07-13.
Each exact slug was listed with a provider route. Rates below are dollars per million
input/output tokens and are the proposed `provider.max_price` ceilings; a route above
the ceiling fails closed.

| Role | Exact slug | Input / output rate |
|---|---|---:|
| SUT | `openai/gpt-4.1` | $2.00 / $8.00 |
| SUT | `google/gemini-2.5-pro` | $1.25 / $10.00 |
| SUT | `anthropic/claude-sonnet-4` | $3.00 / $15.00 |
| SUT | `deepseek/deepseek-chat` | $0.2002 / $0.8001 |
| SUT / paraphrase author / tie-breaker | `mistralai/mistral-large-2512` | $0.50 / $1.50 |
| SUT | `meta-llama/llama-3.3-70b-instruct` | $0.10 / $0.32 |
| Frozen judge 1 | `openai/gpt-4.1-mini` | $0.40 / $1.60 |
| Frozen judge 2 | `google/gemini-2.5-flash` | $0.30 / $2.50 |
| State classifier | `openai/gpt-5.6-terra` | $2.50 / $15.00 |

Primary public sources:

- model/provider pages: [GPT-4.1](https://openrouter.ai/openai/gpt-4.1/providers),
  [Gemini 2.5 Pro](https://openrouter.ai/google/gemini-2.5-pro/providers),
  [Claude Sonnet 4](https://openrouter.ai/anthropic/claude-sonnet-4/providers),
  [DeepSeek Chat](https://openrouter.ai/deepseek/deepseek-chat/providers),
  [Mistral Large 2512](https://openrouter.ai/mistralai/mistral-large-2512/providers), and
  [Llama 3.3 70B](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct/providers);
- judge/classifier pages: [GPT-4.1 Mini](https://openrouter.ai/openai/gpt-4.1-mini/providers),
  [Gemini 2.5 Flash](https://openrouter.ai/google/gemini-2.5-flash/providers), and
  [GPT-5.6 Terra](https://openrouter.ai/openai/gpt-5.6-terra/providers);
- routing contract: [OpenRouter provider selection](https://openrouter.ai/docs/guides/routing/provider-selection).

No inference endpoint, account balance, credential, or paid availability probe was
accessed. Runtime availability remains unverified until a separately authorized run.

## 3. Corrected maximum logical-call geometry

The earlier 10,031 estimate double-counted design-05 judging and included the judged
`rationale_honesty` secondary that PR-24 forbids. The corrected maximum is **9,709
logical calls**:

| Component | Maximum logical calls | Derivation |
|---|---:|---|
| Perturbed SUT administrations | 2,460 | per battery/model: 198 non-05 + 7 initial design-05 calls; × 2 batteries × 6 SUTs |
| 02/07 state classifier | 768 | 64 per battery/model × 2 × 6 |
| Frozen two-judge scoring, excluding 05 | 4,464 | 186 scoring units per battery/model × 2 judges × 2 × 6 |
| Registered design-05 format retries | 84 | at most one retry for each of 42 design-05 cells in each battery |
| Mistral paraphrase author | 73 | one authored item template per sampled item |
| Conditional Mistral tie-breakers | 1,860 | at most 186 units × 5 non-Mistral SUTs × 2 batteries |
| **Maximum** | **9,709** | no original-response rerun |

The Mistral-SUT own-family direct Part-B ceiling is 372 scoring units. If every
non-Mistral disagreement also remains unresolved after its tie-breaker, the absolute
perturbed Part-B ceiling is 2,232 scoring units. These are workload ceilings, not
forecasts and not permission to infer missing labels.

## 4. Proposed token, cost, and attempt envelope

The following caps preserve the existing O5 response cap and narrow structured roles:

| Role | Input-envelope / output cap | Maximum booked cost for one missing-cost response |
|---|---:|---:|
| GPT-4.1 SUT | 24,000 / 32,768 | $0.310144000 |
| Gemini 2.5 Pro SUT | 24,000 / 32,768 | $0.357680000 |
| Claude Sonnet 4 SUT | 24,000 / 32,768 | $0.563520000 |
| DeepSeek Chat SUT | 24,000 / 32,768 | $0.031022477 |
| Mistral Large SUT | 24,000 / 32,768 | $0.061152000 |
| Llama 3.3 70B SUT | 24,000 / 32,768 | $0.012885760 |
| GPT-4.1 Mini judge | 24,000 / 256 | $0.010009600 |
| Gemini 2.5 Flash judge | 24,000 / 256 | $0.007840000 |
| GPT-5.6 Terra classifier | 2,048 / 16 | $0.005360000 |
| Mistral paraphrase author | 24,000 / 4,096 | $0.018144000 |
| Mistral tie-breaker | 24,000 / 256 | $0.012384000 |

The current final-source 438-cell original analogue used 4,028 calls and
$10.11216799. Two comparable perturbation surfaces, the full author envelope, and the
historical W1 mean tie-breaker cost project **$22.500013**. A stress forecast using
125% of the final-source analogue plus the author envelope and the historical W1 p95
tie-breaker cost is **$28.669439**. These are planning analogues, not worst-case token
guarantees.

Recommended budget controls:

1. hard NTE **$30.00**; this is a pre-request stop, not a completion guarantee;
2. concurrency at most 2;
3. checkpoint after paraphrase authoring + battery 1 (about $11 forecast), mandatory
   before booked spend reaches $20, and again before any tie-breakers;
4. before each POST, require `actual_cost + reserved_max_on_missing_cost + all
   in_flight_max + next_request_max <= $30.00`;
5. require exact returned model and `usage.cost`; a missing cost books the role/model
   maximum above;
6. externalize retries and retain every attempt: 9,709 planned logical requests plus a
   10% reserve of 971 exact-payload replays = **10,680 client POST attempts maximum**;
7. allow at most one byte-identical same-model/same-cap/same-price-ceiling replay per
   failed, empty, malformed, or missing-cost key; the second failure stops that thread;
8. no model substitution, denominator change, item replacement, or automatic scale-up.

The first scheduled retained production request for each slug is its canary. There is
no separate premium-model test/probe call; this preserves Jimmy's cheap-models-only
testing constraint while keeping the frozen O5 production roster unchanged.

## 5. Stop pending owner order

The prices, attempt reserve, retry externalization, custody rules, $30 NTE, and paid
execution are not covered by PR-18/23/24. They are therefore parked as PR-25. Do not
source credentials, modify retry behavior, or make a live call until Jimmy ratifies an
exact paid-run order. No G7 status or paper claim is licensed by this preflight.
