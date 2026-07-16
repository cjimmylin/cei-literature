# WCF-Bench Pilot 2 Session-65 quality-custody specification re-review

**Date:** 2026-07-15

**Scope:** only the two named blockers in
`20260715ap-wcf-pilot2-s65-quality-custody-specification-review.md`

**Result:** **PASS**

## Cumulative settlement custody

Settlement state updates and the fsynced cumulative ledger row now occur atomically under
the same process lock. Completed-run validation evaluates settlements in persisted evidence
order and requires each finite, numeric, non-boolean cumulative value to equal the running
sum of response-attributed actual costs. The former `-999.0` cumulative-value bypass now
fails closed. Focused regressions also force concurrent settlement ordering.

## Stable process lease

The lease path now hashes the resolved immutable run-directory identity into one stable
process-global temporary location. Creating a previously absent run parent cannot change
the lease identity; a second process fails closed while the first holds the lease. Live and
analysis entry points share the same nonblocking lease and release it on exit.

## Boundary

The re-review's focused suite passed 12/12. The strict `$28.13` cap, registered retries,
phase order, and within-process three-shard executors remain unchanged. No roster, provider,
reasoning, prompt, scorer, geometry, label, or claim changed. Fresh quality review remains
required before any credential/private-balance access or live task.

No public metadata, credential/private-balance access, OAuth, inference, empirical run
directory, or spend occurred.
