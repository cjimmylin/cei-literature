# CHARITROC cheap OpenRouter qualification plan

Date: 2026-07-10

## Outcome

Add an immutable, low-cost OpenRouter qualification path without changing or
relabeling the frozen GPT-5.5 / GPT-5.4 / GPT-5.4-mini calibration panel or its
persisted Codex evidence.

The qualification profile is `cheap-azure-v1` and contains, in fixed order:

1. `openai/gpt-5-nano`
2. `openai/gpt-5.4-nano`
3. `openai/gpt-5-mini`

Each arm uses medium reasoning, strict JSON-schema output, Azure-only routing,
ZDR, no fallback, and exact returned model/provider attestation. The profile is
limited to access qualification and a public-bank smoke measurement; it cannot
authorize calibration gates, private freeze, or private execution.

## Implementation order

1. Add a separately validated cheap-panel manifest with exact identities,
   provider route, price ceilings, catalog snapshot time, profile hash, and
   stage allowlist.
2. Extend stage identity validation by unioning exact cheap-profile tuples;
   derive the expected returned provider from the immutable identity record.
   Keep every existing calibration tuple unchanged.
3. Make the OpenRouter wire request and route attestation select the immutable
   policy for the request identity. Preserve the current calibration policy as
   the default and forbid injected live policies.
4. Add a separate crash-safe qualification runner with commands `access`,
   `smoke`, `verify`, and `analyze`. Bind profile id/hash into metadata,
   journals, artifacts, and reports. Use all 12 public episodes for smoke.
5. Score canonical stage-4 action, stage-3 update accuracy, empirical AUC, and
   cross-model ranges. Label access as non-measurement and smoke as a cheap
   qualification measurement distinct from the flagship calibration panel.
6. Add failing tests first for identity separation, Azure routing, provider
   mismatch, price/profile drift, crash resume, exact 12x3 coverage, forbidden
   commands, verification replay, and analysis recovery.
7. Run offline suites, then one live access arm. Only after it passes, run all
   three access arms and the 12x3 smoke panel. Recheck account spend before and
   after the live run.

## Non-goals

- No mutation of the frozen flagship panel or existing Codex artifacts.
- No OpenRouter private-bank run.
- No fallback, free-router, auto-router, provider substitution, tool use,
  web search, plugins, healing, or context compression.
- No claim that the cheap panel satisfies the later multi-vendor concordance
  requirement. Cross-vendor routing is a separately frozen v2 profile.
