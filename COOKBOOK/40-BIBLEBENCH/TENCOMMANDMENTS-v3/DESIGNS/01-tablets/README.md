# TABLETS P1 executable contract

This directory freezes the credential-free Phase 1 contract for TABLETS: a
pairwise forced-action tournament over all 45 pairs of the ten named norms. It
contains a deterministic public bank, a separate private authoring projection,
a runtime request manifest, canonical hashes, and a mechanical scorer.

The evaluated schedule contains **636 records**. Its 342 neutral primaries use
T1/T4 endpoints for every pair and add T2/T3 for the 12 priority pairs. The
remaining records are 135 penalty-threat twins, 45 comprehension controls, 45
recognition controls, and 69 additive monitored counterparts. Threat and
monitoring twins never share a parent.

All casuistic expert-panel, human-baseline, and professional evidence is
`NOT_RUN`. Candidate bands in the private projection are authoring hypotheses,
not certified gold. They must not be used for official conformance, empirical,
publication, or scale-promotion claims unless the independent panel passes the
preregistered agreement gate. The scorer therefore returns the executed duty,
paralysis, control accuracy, and analysis eligibility, but official
conformance is always null in this artifact version. Any future panel evidence
requires a new versioned private schema and artifact set; this version remains
fail-closed even if evidence is supplied ad hoc.

The binding TABLETS/CRUX boundary is machine-linked in
`crux-coregistration-linkage.json`: TABLETS owns two named norms acting on one
actor with casuistic-precedence provenance; CRUX owns stakeholder/value
conflicts with lay-consensus gold. Scenario seeds and triads must not be shared.

## Frozen files

- `itembank/bank/p1-public.jsonl` — public prompts, action contracts, pairing,
  and analysis roles; no private band or answer fields.
- `itembank/gold/p1-private.gold.jsonl` — choice coding, provisional authoring
  bands, controls, eligibility, and explicit `NOT_RUN` evidence fields.
- `itembank/runtime/p1-runtime-manifest.jsonl` — provider-neutral request rows
  bound to public-row hashes.
- `itembank/manifest.json` — byte hashes and exact counts.
- `scoring/mechanical.py` — fail-closed record scoring, per-tier/per-frame
  observed pair majorities, and direct observed-triad cycle counting.

## Rebuild and verify

From `COOKBOOK/40-BIBLEBENCH`:

```bash
python TENCOMMANDMENTS-v3/DESIGNS/01-tablets/itembank/build_bank.py
python TENCOMMANDMENTS-v3/DESIGNS/01-tablets/itembank/build_bank.py --check
python -m pytest TENCOMMANDMENTS-v3/DESIGNS/01-tablets/tests -q
```

These commands create or verify bank bytes only. They do not run models,
panels, human studies, a Bradley–Terry fit, or the permutation null.
