# CROSSROADS v3-01 implementation plan

Date: 2026-07-11  
Build root: `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-v3/BANKS/01-crossroads/`  
Status: **offline implementation complete; fresh v6 live run paused by the
2026-07-11 consolidated-benchmark strategy switch**

Closeout evidence: `COOKBOOK/20260711c-corinthlove-consolidation-handoff.md`.
Final verification is 233/233; the controlling live-protocol review is
`CORINTHLOVE-REVIEWS/20260711-crossroads-live-completion-evidence-addendum.md`,
Final disposition revision 2 (GO). Do not resume step 6 from this archival plan
without an approved consolidated architecture.

## Binding interpretation

- D-18 controls scoring: direct key-based C1–C16 choice scores are primary;
  follow-through quality is a separate execution vector. Joint Thurstonian
  estimation is exploratory and must pass synthetic recovery before use.
- C1–C16 labels and operational definitions are copied verbatim from the
  frozen portfolio registry. Method-specific notes may specialize, never
  redefine, them.
- Every emitted episode is enacted through structured tool calls and artifact
  effects. Talk-only output and stalling past the fork window are evasion.
- Every candidate receives a recorded A1/A2 hardness decision. Rejections and
  reasons remain in the log; there are no silent drops.
- P-1…P-3 bind the build: complete cell asserts, matched defeat-class checks
  wherever paired comparisons are used, and a contemporaneous deviation log.

## Frozen construction

Use the duplicated affine-plane 2-(16,4,2) design only as the hidden
clause-assignment layer beneath 40 substantive causal scenario skeletons:

- 16 points map one-to-one to C1–C16;
- 20 GF(4) affine lines contain four clauses each and cover every unordered
  pair once;
- two orientations per line provide 40 clause blocks, each clause in 10 blocks
  and every pair in exactly two;
- each block is assigned to a distinct causal scenario with its own domain,
  roles, artifact, incident, evidence state, deadline, baseline duty, competing
  claims, stable action plans, and branch-specific reaction/repair logic;
- IDs or cross-product coordinates do not establish scenario diversity: build
  assertions require distinct substantive scenario signatures, varied tool and
  substrate sets, and varied 8–20-turn trajectories;
- four executable paths per structure, each honoring two keyed clauses and
  violating two, with every clause plus/minus balanced 2/2 inside a structure.

Visible effects are neutral observable facts. Normative signs, frozen pole
phrases, and rationales stay sidecar-only. A parameter flip changes an
observable environmental fact and can thereby change the hidden evaluation of
a stable underlying action; keys may never be rotated independently of the
causal world. Full-payload and held-out-family lexical decoder audits are
build-blocking.

Counts:

- 600 private episodes = 40 structures × 3 private skins × 5 key-flipping
  parameter states;
- 30 public episodes from disjoint public skins and held-out parameter
  realizations;
- 630 accepted episodes total;
- at least 40 rejected candidates retained as full candidate snapshots with
  mutation, evidence, reason, and content hashes in the hardness log;
- 60 generated stated-pair items, protocol-only and never mixed into enacted
  primary scoring.

Every private clause pair therefore appears in 30 emitted forks, exceeding the
≥25 identification floor. Path order uses a deterministic balanced schedule;
warmth, effort, specificity, length, tool, and ordinal position are crossed
against hidden key signs and audited before scale.

## Build order

### 1. Scaffolding and frozen contracts

Create README, `DECISIONS.md`, `clause_mapping.md`, shared ownership table,
package directories, canonical response/tool schemas, canary registry, and
tests that fail before implementation. Tests freeze counts, exact C1–C16
labels, allowed public keys, and sidecar/judge payload boundaries.

### 2. Deep structures and hardness gate

Implement GF(4) block construction, 40 distinct causal scenario skeletons,
clause-specific competing-claim/action catalogs, four-path key matrices,
evidence-derived A1/A2 gate, full rejected-candidate snapshots, complete
payload split hygiene, surface-orthogonality audit, and semantic cue decoder.
Persist
`deep_structures.yaml`, accepted/rejected logs, coverage tables, and audit
reports only after focused tests pass.

### 3. Scorers and recovery before scale

Implement:

- deterministic tool-log path classifier with at least 40 fixtures, including
  conflicting/multi-tool/late/stall cases;
- evasion detector and fork-window accounting;
- five-point follow-through anchors for all 16 clauses, with pious-language and
  harsh-pole fixtures;
- direct key-based clause aggregation and separate E(C1–C16) vector;
- path-consistency index across the three skins;
- block-information/rank audit;
- exploratory conditional-logit/Thurstonian profile estimator with synthetic
  known-θ recovery and a build-blocking threshold.

No bulk generation occurs until these fixtures and recovery assertions pass.

### 4. Generator and bank artifacts

Generate 600 private +30 public episodes, hidden path keys/parameter states,
hardness log, consistency groups, deterministic authoring-only `JSEED` tokens,
630 deterministic UUIDv4-format `10CB3-01-` canaries, and 60 stated pairs.
Issue random `JCASE-<UUIDv4>` values per scoring occurrence through a private
append-only registry; bind persistent `JUDGE-<UUIDv4>` identities to an
immutable roster containing family, provider, exact model or human class,
prompt/configuration hashes, and role. Public YAML exposes
paths and scripts but no key, clause-sign, reaction-table, or hidden-state
field. Simulant branch logic remains private by CO-3.

### 5. Adversarial, export, and self-check

Run warm-path, stall, template-memorizer, length-tell, tool-position,
pious-language, frozen-phrase, normative-token, and held-out lexical decoder
bots. All monotone bots must fail at least one declared gate, and no lookup
surface may recover hidden signs.
Export the pinned ten-field episode table, frozen C1–C16 coverage map, A3
profile schema, and A4 loadings/calibration notes. Self-check covers every
count, block/pair cell, hardness decision, split boundary, canary, judge ID,
mock label, scope/citation ban, and export row.

### 6. Cheap public qualification

Only after the interim gate is fully green and a fresh adversarial re-review
supersedes the 2026-07-11 FAIL, implement or execute a bank-specific
crash-safe public runner. Reuse CHARITROC's integrity principles, not its
design-specific response or scoring contracts. Start with access and a small
balanced canary on the cheapest authorized models; expand to all 30 public
episodes only after access/canary verification.

Qualification reports path resolution, evasion, path entropy, clause-profile
dispersion, between-model profile distance, consistency where estimable, and
surface-cue decoding. It does not call profile convergence a correctness AUC
and does not authorize private execution, calibration, or freeze.

### 7. Review and handoff

Run the complete offline suite once before live and once at final code freeze
only if code changed after the pre-live run. Obtain a fresh adversarial review,
apply safe conditional fixes, write the dated handoff, update authoritative
status/memory, and advance the one-bank queue.

The 2026-07-11 pre-live review is a blocking FAIL until a later evidence-based
re-review explicitly supersedes it. No catalog/access probe or other paid call
is permitted while that verdict remains current.

## Initial verification commands

```sh
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
$PY -m pytest tests/ -q
$PY generator.py --dry
$PY adversarial/run_adversarial.py
$PY export/export_megamatrix.py
$PY selfcheck.py
```

No commit, stage, push, deletion, frontier call, human-validation simulation,
or frozen-registry edit is authorized.
