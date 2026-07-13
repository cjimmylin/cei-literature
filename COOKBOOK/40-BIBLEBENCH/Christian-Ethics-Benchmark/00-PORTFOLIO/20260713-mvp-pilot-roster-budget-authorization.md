# WALKWORTHY — MVP-PILOT Roster and Budget Authorization Order

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Owner:** Jimmy Lin
**Prepared by:** Codex
**Status:** PROPOSED — NO CREDENTIAL ACCESS OR PAID CALL AUTHORIZED
**Scope:** Separate exploratory MVP-PILOT paper-preview lane; never O5 evidence

## 1. Recommended exact roster

| Role | Explicit OpenRouter slug | Family | Current input / output price per 1M tokens | Public endpoints |
|---|---|---:|---:|---:|
| SUT 1 | `mistralai/mistral-small-3.2-24b-instruct` | Mistral | $0.075 / $0.20 | 4 |
| SUT 2 | `google/gemini-2.5-flash-lite` | Google | $0.10 / $0.40 | 5 |
| SUT 3 | `qwen/qwen3-8b` | Qwen | $0.117 / $0.455 | 1 |
| Judge 1 | `openai/gpt-4.1-nano` | OpenAI | $0.10 / $0.40 | 3 |
| Judge 2 | `meta-llama/llama-3.3-70b-instruct` | Meta | $0.10 / $0.32 | 12 |
| Branch classifier | reuse `openai/gpt-4.1-nano` | OpenAI | $0.10 / $0.40 | 3 |

The SUTs span three provider families. The judges are cross-family and do not share a
family with any selected SUT. OpenAI Nano is reused as the 02/07 branch classifier so
the order has five unique model slugs, not six. These judges are deliberately cheap
and unvalidated; this is acceptable only because the MVP output is descriptive and
non-release-grade.

### Availability and price evidence

Codex performed public, unauthenticated GET requests on 2026-07-13. All five exact
slugs were present in OpenRouter's model catalog and each exposed at least one current
provider endpoint. No credential, account balance, or inference endpoint was accessed.

- Catalog source: <https://openrouter.ai/api/v1/models>
- Endpoint source pattern: `https://openrouter.ai/api/v1/models/{slug}/endpoints`
- Provider-routing contract: <https://openrouter.ai/docs/guides/routing/provider-selection>
- Billing note: <https://openrouter.ai/pricing> (posted token rates; failed fallback
  attempts are not billed)
- Model pages:
  [Mistral](https://openrouter.ai/mistralai/mistral-small-3.2-24b-instruct/providers),
  [Gemini Flash-Lite](https://openrouter.ai/google/gemini-2.5-flash-lite/providers),
  [Qwen3 8B](https://openrouter.ai/qwen/qwen3-8b/providers),
  [GPT-4.1 Nano](https://openrouter.ai/openai/gpt-4.1-nano-2025-04-14/providers), and
  [Llama 3.3 70B](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct/providers).

The budget uses the catalog/API rate, not cache discounts or an optimistic weighted
average. Every client must use `provider.sort = "price"`,
`provider.require_parameters = true`, `provider.allow_fallbacks = true`, and a
model-specific `provider.max_price` equal to the table rate. If no endpoint satisfies
that ceiling, the probe/call fails and that model thread stops; there is no unapproved
provider-price increase or model substitution.

## 2. Frozen 60-item PUBLIC manifest

Selector: first two runnable `easy` plus first four runnable `hard` items by item ID
within each design, including PUBLIC exemplars only when runnable. The exact selected
IDs are:

| Design | Two easy + four hard IDs |
|---|---|
| 01 | `WW-01-B03`, `WW-01-D04`, `WW-01-A01`, `WW-01-A05`, `WW-01-A05-P`, `WW-01-B01` |
| 02 | `WW-02-B03`, `WW-02-C02`, `WW-02-A02`, `WW-02-A05`, `WW-02-B02`, `WW-02-B04` |
| 03 | `WW-03-B03`, `WW-03-B05`, `WW-03-A01`, `WW-03-A04`, `WW-03-A05`, `WW-03-B01` |
| 04 | `WW-04-D01`, `WW-04-D05`, `WW-04-A03`, `WW-04-A04`, `WW-04-B01`, `WW-04-B04` |
| 05 | `WW-05-A01`, `WW-05-C05`, `WW-05-A03`, `WW-05-B01`, `WW-05-B02`, `WW-05-B06` |
| 06 | `WW-06-A05`, `WW-06-D03`, `WW-06-A01`, `WW-06-A06`, `WW-06-B02`, `WW-06-B04` |
| 07 | `WW-07-A02`, `WW-07-C02`, `WW-07-A03`, `WW-07-B02`, `WW-07-B04`, `WW-07-C01` |
| 08 | `WW-08-B02`, `WW-08-D02`, `WW-08-A02`, `WW-08-A04`, `WW-08-B01`, `WW-08-B04` |
| 09 | `WW-09-A04`, `WW-09-A05`, `WW-09-B01`, `WW-09-B04`, `WW-09-C01`, `WW-09-C04` |
| 10 | `WW-10-A05`, `WW-10-B05`, `WW-10-A01`, `WW-10-A03`, `WW-10-B01`, `WW-10-B04` |

SHA-256 of the newline-delimited ordered ID list (with final newline):
`6874ae265588d3b10c6ef11c4b554e21e82c2f1e5d212f9e9254c150d2f40345`.

The production manifest must fail closed unless it contains these exact 60 IDs in this
order. HOLDOUT and the frozen G7 selector are unrelated and must never be loaded.

## 3. Exact logical call surface

The 180 item×SUT headline expands because paired/multi-turn administrations, branch
classification, per-unit judging, and design-05 allocation parsing each make calls.

| Design | SUT calls per model (normal / all 05 retries) | Classifier calls per model | Judge units per judge per model |
|---|---:|---:|---:|
| 01 | 6 / 6 | 0 | 6 |
| 02 | 52 / 52 | 28 | 46 |
| 03 | 12 / 12 | 0 | 12 |
| 04 | 12 / 12 | 0 | 12 |
| 05 | 12 / 18 | 0 | 6 |
| 06 | 6 / 6 | 0 | 6 |
| 07 | 36 / 36 | 24 | 36 |
| 08 | 12 / 12 | 0 | 12 |
| 09 | 16 / 16 | 0 | 12 |
| 10 | 12 / 12 | 0 | 12 |
| **Per model** | **176 / 182** | **52** | **160** |
| **Three-SUT panel** | **528 / 546** | **156** | **480 per judge** |

- Normal batch: 528 SUT + 156 classifier + 960 judge = **1,644 calls**.
- If all 18 design-05 allocation cells use their one allowed format retry:
  **1,662 calls**.
- One minimal probe for each of five unique slugs: **5 calls**.
- General paid-duplicate reserve: `ceil(10% × 1,662)` = **167 calls**.
- Maximum authorized call envelope: **1,834 calls**. Provider failures/fallbacks are
  not assumed billable; the reserve covers charged empty-success or duplicate work.

## 4. Token and cost envelope

MVP-specific output caps (they do not modify O5): SUT 2,048 tokens; judge 256;
classifier 16; probe 256. The budget uses a conservative 24,000-token input envelope
for every SUT and judge call, 2,048 for classifier calls, and 1,024 for probes.

This 24,000-token envelope was checked against the exact manifest. The largest selected
multi-turn request is conservatively bounded at 20,736 (literal input characters plus
nine prior 2,048-token outputs); the largest fixed judge prompt is 6,403 characters
before the at-most-2,048-token SUT response. The envelope therefore covers the selected
surface without relying on average token use.

| Role | Calls priced | Input / output envelope | Maximum cost |
|---|---:|---:|---:|
| Mistral SUT | 182 | 24,000 / 2,048 | $0.402147 |
| Google SUT | 182 | 24,000 / 2,048 | $0.585894 |
| Qwen SUT | 182 | 24,000 / 2,048 | $0.680651 |
| OpenAI classifier | 156 | 2,048 / 16 | $0.032947 |
| OpenAI judge | 480 | 24,000 / 256 | $1.201152 |
| Meta judge | 480 | 24,000 / 256 | $1.191322 |
| Five probes | 5 | 1,024 / 256 each | $0.000958 |
| **Base worst-case envelope** | **1,667** | — | **$4.095071** |
| 10% paid-duplicate reserve (167 × highest per-call envelope) | **167** | Qwen SUT worst case | **$0.624553** |
| **Authorized planning envelope** | **1,834** | — | **$4.719625** |
| **Headroom below hard cap** | — | — | **$0.280375** |

Actual charges should be much lower than this full-token envelope, but the order does
not depend on that expectation. Before each paid request, the driver must verify that
actual spend plus the next call's role/model envelope is at most $5.00. Otherwise it
stops before the request.

## 5. Run order, checkpoints, and stops

1. **TDD preflight, $0:** build the fixed manifest/hash validator, explicit client
   roster/caps/price ceilings, append-only attempt ledger, and pre-call NTE guard. Run
   focused tests and the full suite before credentials are accessed.
2. **Five probes:** one call per unique slug. Require nonempty output, explicit returned
   model/family, parseable output for judge/classifier roles, and recorded usage/cost.
   Any failed probe stops only that model thread; no substitution is allowed.
3. **SUT phase:** run Mistral, then Google, then Qwen, checkpointing after every model.
   Branch-classifier calls occur inline for designs 02/07. The all-05-retry plus
   classifier phase envelope, including the five probes, is $1.702598.
4. **Judge 1:** run OpenAI Nano across the 480 scoring units. The cumulative envelope
   before the second judge is **$2.903750**, below $3.
5. **Mandatory $3 checkpoint:** persist coverage, errors, actual spend, remaining
   projected envelope, and the 90%-per-design×SUT completeness table before starting
   the Meta judge. Continue only if actual plus all remaining work plus unused reserve
   is at most $5.00.
6. **Judge 2:** run Meta Llama, enforcing the pre-call hard-cap guard. Stop on cap risk,
   reserve exhaustion, or a model-specific reliability failure.
7. **Paper conversion:** after validated merge/summary, immediately fill the exploratory
   MVP table/figure shapes and limitations. Do not extend the panel or do unrelated
   hardening.

Resume is append-only and exact-key validated. No missing cell is inferred. A
design×SUT row below 90% completeness is rendered `INCOMPLETE`, not interpreted.

## 6. Claim boundary

Every result surface must state:

> Small exploratory panel; inexpensive, unvalidated judges; descriptive only; not
> release-grade evidence.

The pilot cannot support rankings, gate PASS/FAIL, release/redesign/kill/demotion
decisions, population/frontier generalization, or any merge with O5 evidence.

## 7. Jimmy authorization requested

Please ratify this exact line before credentials or paid calls:

> Authorize WALKWORTHY MVP-PILOT order MVP-A1: SUTs
> `mistralai/mistral-small-3.2-24b-instruct`,
> `google/gemini-2.5-flash-lite`, and `qwen/qwen3-8b`; judges
> `openai/gpt-4.1-nano` and `meta-llama/llama-3.3-70b-instruct`; classifier
> `openai/gpt-4.1-nano`; exact 60-item PUBLIC manifest hash
> `6874ae265588d3b10c6ef11c4b554e21e82c2f1e5d212f9e9254c150d2f40345`;
> SUT/judge/classifier output caps 2048/256/16; price-sorted capped providers;
> 1,834-call authorized envelope; mandatory pre-$3 checkpoint; $5.00 hard NTE;
> stop on failed probe, reserve exhaustion, or projected cap breach; no substitution;
> descriptive-only paper preview.
