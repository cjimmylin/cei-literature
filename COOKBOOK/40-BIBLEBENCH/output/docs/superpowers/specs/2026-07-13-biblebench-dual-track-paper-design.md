# BibleBench Dual-Track Paper and Pilot-Bank Design

**Date:** 2026-07-13  
**Status:** Approved for implementation  
**Owner:** Jimmy Lin  
**Implementation branch:** `codex/biblebench-pilot`

## 1. Decision

BibleBench will proceed on two coordinated tracks:

1. draft a venue-neutral design and methods manuscript immediately; and
2. build the executable 42-family bank and owner gold-review packet in
   parallel, then insert pilot results after the registered live study.

The manuscript must distinguish verified design or engineering evidence from
future empirical evidence. No placeholder, fixture, synthetic organism, or
test-suite result may be presented as evidence about an LLM.

## 2. Owner approval of the 42-family selection

On 2026-07-13, Jimmy Lin reviewed and approved the exact family selection in:

`output/docs/superpowers/specs/2026-07-11-biblebench-42-core-selection.md`

The reviewed file is bound by SHA-256:

`c0de28c064fdb87ae9ac4d38d53190856912b88f645492cc087ff2d0cee346e2`

The approved inventory is:

- FruitBench: F01-F12;
- CORINTHLOVE: L01-L08;
- 10CBench: T01-T12; and
- SermonMount: S01-S10.

This approval fixes the selected families, source provenance, pilot-use
descriptions, primary-evidence descriptions, and stated construct boundaries.
It does **not** constitute episode-level provisional gold, semantic-invariance
approval, permission to spend, or authorization to generate bank outputs.

## 3. Paper track

The first manuscript is a venue-neutral design and methods paper. Its working
artifact set is:

- `BIBLEBENCH-PAPER/manuscript.md`;
- `BIBLEBENCH-PAPER/references.bib`;
- `BIBLEBENCH-PAPER/claims-registry.yaml`;
- `BIBLEBENCH-PAPER/figures/` and `BIBLEBENCH-PAPER/tables/`;
- a reproducible build entry point; and
- a rendered, visually checked PDF.

The manuscript structure is:

1. motivation and contributions;
2. biblical and ethical construct boundaries;
3. related benchmark and measurement work;
4. the four passage-module architecture and approved 42 families;
5. shared-episode, forecast, primary, and probe methodology;
6. lossless observable evidence and module-native lens isolation;
7. human adjudication and single-expert provisional gold;
8. planned cheap-model diagnostic protocol;
9. engineering validation and prerelease limitations;
10. empirical results, added only after the registered pilot; and
11. discussion, ethics, limitations, and future multi-judge validation.

Results surfaces remain explicitly marked `PENDING_EMPIRICAL_RUN` until a
verified run and completed human adjudication exist.

## 4. Claims registry

Every headline statement is classified as exactly one of:

- `DESIGN_CLAIM`: supported by approved specifications or provenance;
- `ENGINEERING_CLAIM`: supported by credential-free tests and artifact checks;
- `PROVISIONAL_THEOLOGICAL_JUDGMENT`: authored or ratified by the owner and
  labeled as single-expert judgment;
- `EMPIRICAL_CLAIM_PENDING`: preregistered but not yet supported by a run; or
- `EMPIRICAL_CLAIM`: supported by frozen run artifacts and adjudication.

The paper may report the first three categories before live execution. It may
describe the fourth only prospectively. The fifth category remains empty until
the registered pilot closes successfully.

## 5. Bank and gold track

The executable development bank contains 48 episodes: 12 per module, with four
target, four null or foil, and four restraint, counterfeit, or overreach roles
per module. It represents every approved family at least once and preserves the
registered 34 common-life / 14 Christian-facing balance.

Each episode record includes:

- core and passage provenance;
- role, stratum, affected parties, and authority boundary;
- shared task body and C0/C1/C2 surfaces;
- observable acceptable-action band and prohibited actions;
- deficient and counterfeit poles;
- red-line classes;
- capability twin where action is primary;
- sandbox or consequential-artifact contract;
- matched observable probe;
- repair or restitution expectations;
- behavioral-attribution status; and
- confidence and contestability fields.

The owner review packet is generated before any model output. Jimmy serves as
the founding theologian-technical judge. Approved labels are stored as
`single_expert_provisional_gold`, never as Christian consensus. A deterministic
stratified 20% repeat sample is prepared for later blinded intra-rater analysis.

## 6. Shared-engine prerelease boundary

The integrated prerelease candidate is based on Git commit
`f49497b8c455e0d912c40481df5f360d013eee98`. It includes deterministic schedule
construction, lossless observable evidence, and authenticated lens packets.

Two limitations are accepted for the paper-first prerelease:

- Task 7's compact privacy parser may reject some ordinary phrases. It is
  reopened only if authored pilot content fails compilation.
- Task 8's runtime privacy firewall is fail-closed, while the static JSON Schema
  does not enumerate every Unicode NFKC compatibility spelling. Runtime
  validation remains authoritative for the pilot.

Neither limitation may be hidden. A content-level failure in a registered
episode is blocking; a schema-only compatibility gap that runtime rejects is a
disclosed limitation.

## 7. Parallel execution and integration

Module authoring is partitioned by benchmark so writers do not edit the same
files. Separate worktrees may draft FruitBench, CORINTHLOVE, 10CBench, and
SermonMount packs concurrently. The coordinating branch owns shared schemas,
cross-module tests, claims, and final integration.

Each module passes, in order:

1. source and ID verification;
2. theological and construct-boundary review;
3. episode-role and stratum checks;
4. compilation through the shared schedule;
5. observable-outcome and capability-control review; and
6. owner provisional-gold review.

An agent may draft but may not silently ratify owner-only gold, contested
interpretations, spend, model selection, or publication claims.

## 8. Spend and empirical execution

All work through manuscript drafting, bank authoring, owner review, offline
fixtures, and cost estimation is credential-free and has a USD 0 budget.

Before any paid call, the owner receives an exact checkpoint containing:

- four currently available general-purpose models across at least three pinned
  providers;
- the fresh catalog and price evidence;
- exact call and token ceilings;
- the non-bank smoke cost;
- the bank-tranche worst-case cost;
- the frozen hashes; and
- the proposed authority expiry and stop rules.

No paid request is authorized by this design document.

## 9. First milestone and acceptance criteria

The first no-spend milestone is complete when:

- the manuscript is drafted through Methods and Planned Evaluation;
- the claims registry contains no unsupported empirical claim;
- all 42 core records and 48 episode records exist and validate;
- the real authored packs compile through the shared schedule;
- Task 7's known false-positive limitation is tested against those packs;
- an owner-reviewable provisional-gold packet exists;
- the prerelease limitations register is complete; and
- an exact spend proposal exists without executing a request.

The empirical-results section, qualified composite, formal CORINTHLOVE
concordance, leaderboard, best-model claim, C3 confirmation, and multi-judge
validation are outside this first milestone.

## 10. Approval record

Jimmy Lin approved the dual-track direction and confirmed the 42-core selection
on 2026-07-13. Implementation may begin after review of this written design.
