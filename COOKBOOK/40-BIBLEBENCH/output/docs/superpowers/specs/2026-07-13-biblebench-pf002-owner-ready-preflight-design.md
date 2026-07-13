# BibleBench PF-002 Owner-Ready Three-Model Preflight Design

**Date:** 2026-07-13
**Status:** OWNER APPROVED FOR SPECIFICATION; IMPLEMENTATION AWAITS WRITTEN-SPEC REVIEW
**Owner:** Jimmy Lin
**Branch:** `codex/biblebench-pf002-preflight`

## 1. Objective

Prepare the exact zero-spend preflight packet that can be presented for owner
authorization immediately after the founding theologian-technical adjudication
is scientifically adequate. The packet must reconcile the implemented PF-002
runner with the registered three-model, 288-call geometry and remove the stale
four-model/C0-C1-C2 checkpoint from the active authorization surface.

This work is independent of the owner's substantive judgments. It must neither
read nor alter an exported judge draft, provisional-gold decision, rationale,
confidence field, repeat mapping, model response, or final gold packet.

## 2. Authority and non-authority

PF-002 authorizes preparation of a bounded three-model paper-preview proposal:

- all 48 frozen episodes;
- one C1 primary and one matched observable probe per episode;
- exactly three inexpensive general-purpose models;
- 288 logical calls total;
- a forecast at or below $3.00; and
- a hard not-to-exceed ceiling of $5.00.

This design authorizes public-document research and local deterministic
validation only. It authorizes no credential access, balance query, provider
API call, model call, smoke call, account mutation, owner-signature creation,
authorization-state mutation, or spend. Every real-roster artifact remains
`PROPOSAL_ONLY`, `authorized: false`, and `NOT_AUTHORIZED`.

## 3. Candidate roster

The preflight preserves the already implemented cross-family candidate roster
unless current official documentation invalidates an entry:

| Alias | Provider | Candidate model | First-party route family |
|---|---|---|---|
| `actor-alpha` | OpenAI | `gpt-5-nano-2025-08-07` | Responses API |
| `actor-beta` | Google | `gemini-2.5-flash-lite` | Generate Content |
| `actor-gamma` | Anthropic | `claude-haiku-4-5-20251001` | Messages API |

For each entry, the implementation must verify from official first-party
documentation the exact identifier, current standard input and output prices,
context window, maximum supported output, route family, and relevant decoding
parameter support. Search results, aggregators, reseller pages, and cached
repository claims are not sufficient evidence.

If an exact identifier, price, limit, or route cannot be verified, the packet
must remain visibly incomplete and fail closed. The implementation may propose
a documented replacement but may not silently change the three-model roster.

## 4. Deliverables

The session produces four coordinated owner-facing surfaces:

1. **Canonical proposal manifest.** A schema-valid copy of the exact real
   roster proposal under `BIBLEBENCH-PILOT/preflight/`, bound to the frozen
   banks, request/surface registries, runner, adapters, schemas, and analysis
   contracts. It remains unauthorized.
2. **PF-002 cost checkpoint.** Replace the active stale four-model checkpoint
   with the registered 48 × 3 × 2 geometry, exact verified price evidence,
   deterministic worst-case calculation, retry exposure, forecast gate, $5
   NTE, expiry, and stop rules. Historical design records are not rewritten.
3. **Owner authorization request.** A concise Markdown packet listing the exact
   roster, routes, hashes, price evidence, token caps, retry rule, forecast,
   NTE, expiry, unresolved facts, and the precise approval fields still blank.
   It explicitly says that signing is a later owner action.
4. **Verification record.** A machine-readable and human-readable consistency
   report proving the manifest, checkpoint, schemas, runner, and authorization
   request describe one proposal.

## 5. Registered request and cost geometry

The canonical proposal must retain:

- 48 episodes and four passage modules;
- three blinded actor aliases;
- 144 C1 primary calls;
- 144 matched probe calls;
- 288 logical calls;
- no capability twins;
- no C0 or C2 dispatch;
- no fallback;
- at most one retry only for the registered rate-limit class;
- unknown delivery as terminal missingness; and
- maximum input/output token caps of 4,096/700 per logical call unless a
  narrower owner-visible proposal is explicitly documented.

Worst-case cost is recomputed with decimal arithmetic from exact unit prices,
all 288 logical calls, registered maximum tokens, and the permitted retry
exposure. The manifest-provided total is never trusted. The active proposal
must fail if the calculation exceeds the $3.00 forecast gate, if the NTE or hard
cap differs from $5.00, or if any price or token field is missing.

No batch, cache, promotional, or account-specific discount is assumed. Taxes,
billing rounding, and regional/account availability remain disclosed preflight
unknowns unless an official public source resolves them without account access.

## 6. Data flow and custody

```text
official public documentation
        |
        v
verified price/model evidence -----> canonical proposal manifest
                                             |
frozen banks + code/schema hashes ----------+
                                             |
                                             v
                                  deterministic cost recomputation
                                             |
                     +-----------------------+-----------------------+
                     v                                               v
             cost checkpoint                              authorization request
                     \                                               /
                      +------------- consistency report -------------+
```

Owner adjudication data does not enter this flow. The proposal binds only
already frozen public/authorized bank and runtime artifacts. Private repeat
custody, owner rationales, and provisional-gold fields remain outside the
preflight packet.

## 7. Fail-closed behavior

The preflight is invalid if any of the following occurs:

- an official source no longer supports an exact model identifier or route;
- price evidence is unavailable, internally inconsistent, or outside the
  registered freshness/expiry interval;
- bank, registry, runner, adapter, schema, or analysis hashes drift;
- provider, model, route, or adapter-family coherence fails;
- duplicate JSON members or noncanonical values are detected;
- fallback is enabled;
- forecast exceeds $3.00 or the NTE/hard cap differs from $5.00;
- proposal or authorization state implies approval;
- an owner field, nonce, signature/trust record, or consumption receipt is
  fabricated during preparation; or
- any credential, provider, model, or billing surface would be required to
  finish the packet.

Failure produces an explicit `PREFLIGHT_INCOMPLETE` report with the unresolved
fact and no executable authorization artifact.

## 8. Testing and review

Implementation uses test-driven development and adds focused checks that:

- enforce the exact three-model/288-call geometry across every deliverable;
- require all public evidence URLs to be official first-party sources;
- recompute price exposure independently and match all displayed totals;
- reject the stale four-model and 1,344-call language from the active
  checkpoint;
- require `PROPOSAL_ONLY`, `authorized: false`, and `NOT_AUTHORIZED` throughout;
- reject expired, hash-drifted, over-budget, fallback-enabled, malformed, or
  internally inconsistent packets;
- prove no credential lookup, provider SDK, HTTP transport, socket, model call,
  or balance query is reachable from the preflight build command; and
- reproduce all generated preflight artifacts byte-for-byte.

An independent P0/P1 review must confirm that the packet can be safely handed
to the owner without being mistaken for authorization or empirical evidence.
P2/P3 polish is recorded and deferred.

## 9. Completion boundary

This session is complete when the canonical proposal, corrected cost
checkpoint, owner authorization request, and consistency record agree exactly;
focused and integrated tests pass; public-source verification is recorded; the
proposal remains unauthorized; and the portfolio dashboard points to the owner
adjudication and exact paid-manifest approval as the only remaining pre-call
gates.

The next authorized action remains human: complete adjudication, review the
exact packet, and separately approve or reject the roster and spend boundary.
