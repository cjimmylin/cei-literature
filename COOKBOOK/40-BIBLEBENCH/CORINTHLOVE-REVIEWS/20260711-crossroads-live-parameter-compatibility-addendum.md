# CROSSROADS parameter-compatibility addendum

Date: 2026-07-11  
Reviewer: fresh independent Codex subagent  
Scope: profile-v4 removal of unsupported `parallel_tool_calls` only  
Verdict: **GO — fresh v4 cheap public qualification root authorized**

This addendum leaves the construct GO, endpoint/ZDR review, and direct-response
attestation review unchanged. I loaded no credential and made no network,
paid, or model call.

## Finding

The preserved v3 root closes offline at `valid=true` with 7 artifacts, 8
journal entries, and only the access phase complete. All four access artifacts
succeeded with exact returned provider `Azure`, their frozen snapshots, and a
512-token access budget. Its first nano canary artifact records HTTP 404 before
any model output. The current runtime rejects the root with `qualification
manifest version differs`, so it cannot be resumed under v4.

The compatibility diagnosis is coherent: every exact eligible Azure/ZDR
catalog row omits `parallel_tool_calls`, while the v3 fork transmitted it under
`require_parameters: true`. Profile v4 removes that one optional field. Fork,
follow-through, and closeout still transmit only catalog-required parameters;
the final OpenRouter transport now independently rejects any undeclared model
parameter before `urlopen`. Routing remains exactly lowercase `azure`, ZDR
required, data collection denied, fallbacks forbidden, and exact Azure/direct
provider and snapshot attestation required.

The scoring consequence is bounded. Distinct complete fork actions remain
ambiguous and select the evasion reaction branch; repeated calls to the same
exact fork path remain intentionally idempotent under the unchanged path
classifier. Multiple repair or closeout calls remain mechanically unresolved,
and any incomplete call fails before classification. Thus the removed flag is
not needed to determine path identity or staged completion. The README and
decision-log phrase “multiple complete actions” should be read as **distinct**
fork actions; this wording nuance is non-blocking because the frozen classifier
and tests are unambiguous.

## Independent delta and verification

In-memory reversal reproduced every v3-bound source hash exactly:

- reinserting `parallel_tool_calls: false` and reverting staged request v3→v2
  reproduced executor `3dbd1c33...9b7f2b`;
- removing the new parameter preflight reproduced transport
  `b6971056...9f4f62`;
- reverting manifest v4→v3 reproduced runner `7be24ab6...ad1d06`;
- reverting only profile identity v4→v3 and its catalog timestamp refresh
  reproduced contracts `71fc999b...f17272` and canonical profile
  `6026830e...b57a3`.

The bank, public episodes, staged tool contracts, payload contract, and both
scorers remain at their v3 hashes, including bank
`d0bb7f69...f3f4e3`, path classifier `914c4d18...78c21`, and follow-through
scorer `2880a745...8167`. Completion budgets remain 512 for access and
2,048/1,024/1,024 for fork/follow-through/closeout.

```text
PYTHONDONTWRITEBYTECODE=1 $PY -m pytest tests/test_pilot_*.py -q -p no:cacheprovider
  -> 71 passed in 8.88s

PYTHONDONTWRITEBYTECODE=1 $PY -m pytest tests/ -q -p no:cacheprovider
  -> 228 passed

verify_evidence_root(v3)
  -> valid=true; artifacts=7; journal_entries=8; phases_complete=[access]

current verify_run(v3)
  -> rejected: qualification manifest version differs
```

## Authorization boundary

**GO.** Create only
`pilot/runs/20260711-openrouter-cheap-azure-v4-live-v1` and run the same four
cheap aliases. Proceed access → six-item canary → smoke only after each prior
phase succeeds and verifies offline. Preserve v3 without retry or mutation and
stop on any new catalog, routing, transport, provider, snapshot, usage, cost,
finish-reason, or semantic-replay failure.

This remains public path-only qualification, not a measurement. It does not
authorize private episodes, calibration, model ranking, canonical E(C1–C16),
live judges, expert key validation, frontier filtering, or bank freeze.
