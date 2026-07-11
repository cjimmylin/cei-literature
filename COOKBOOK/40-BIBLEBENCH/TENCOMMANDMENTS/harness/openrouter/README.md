# Shared OpenRouter foundation

This package contains benchmark-neutral primitives for deterministic,
resumable OpenRouter runs. Benchmark request projections, schedule schemas,
mechanical scorers, and result reports remain outside this package.

## Modules

- `canonical.py`: bounded exact canonical JSON and SHA-256 helpers.
- `budget.py`: exact logical-call preflight and resumable paid-cost custody.
- `checkpoint.py`: canonical, durable, per-stream hash-chained JSONL records.
- `client.py`: exact provider pinning, endpoint catalog verification, sanitized
  usage metadata, and 429-only retry.

## Required call order

1. Construct frozen `ModelRoute` values and call `verify_model_routes`.
2. Build the exact schedule with `CallEstimate` and call `preflight_spend`.
3. Rebuild `SpendLedger` from verified checkpoint spend records on resume.
4. Give the ledger to `OpenRouterChatClient` and provide the scheduled
   `call_id` to every `generate` call.
5. Append benchmark-sanitized terminal or parked payloads with
   `append_checkpoint`; pass the last verified head for optimistic concurrency.

The client sends a single-provider route with fallbacks disabled and parameter
support required. It retries only HTTP 429 responses. HTTP 5xx, timeouts, and
network failures are treated as ambiguous-delivery failures and are never
retried automatically. Ledger authorization atomically reserves the call ID
before transport; only a known uncharged HTTP 429 exhaustion releases it.
Ambiguous failures retain the reservation so another client sharing the ledger
cannot replay the same logical call. A response's cost is recorded before its content,
provider, model, finish reason, or response ID is accepted.

The API credential is used only in request headers. It is rejected if it
appears in model-facing content and is never included in call metadata,
catalog proofs, spend records, or checkpoint helpers.
