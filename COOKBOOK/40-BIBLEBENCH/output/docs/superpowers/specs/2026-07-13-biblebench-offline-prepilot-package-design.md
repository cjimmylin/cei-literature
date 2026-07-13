# BibleBench Offline Pre-Pilot Package Design

**Status:** Owner-approved for execution by Jimmy Lin on 2026-07-13.

## 1. Purpose and paper boundary

This package completes the offline work that can proceed while Jimmy performs
the founding theologian-technical adjudication. It prepares the first cheap
general-purpose-model pilot without making a model call, accessing a credential,
or authorizing spend.

The package enables five paper-facing outputs:

1. a judge-safe blinded-repeat workflow for the registered 10-record repeat;
2. an authenticated C0/C1/C2 primary-probe-to-evidence custody manifest;
3. synthetic-only analysis, table, and figure scaffolds;
4. an exact cheap-model roster and cost checkpoint for later owner approval; and
5. a visually verified methods PDF whose results remain explicitly pending.

It does not alter the 48 authored episodes, Jimmy's active pass-one packet, the
registered roll-up, or the claim that pass one and repeat must freeze before any
pilot call or model-output exposure.

## 2. Alternatives considered

### A. Minimal documentation only

Document the remaining procedures without executable tooling. This is fastest,
but it leaves blinding, custody, and analysis reproducibility dependent on
manual steps. It does not close the cue-custody P1.

### B. Offline executable pre-pilot package (selected)

Build small deterministic modules with schemas, synthetic fixtures, immutable
outputs, and explicit manifests. This closes the genuine P1 while keeping live
execution outside scope.

### C. Full live-run platform

Add provider adapters, retries, billing, and operational deployment controls.
This exceeds the paper-first timebox and would recreate the hardening drift the
portfolio policy forbids.

## 3. Architecture and file ownership

The work is divided into four independent implementation lanes. Agents may work
concurrently only within these disjoint paths.

### 3.1 Blinded repeat lane

`repeat.py` consumes a completed adjudicated packet plus the custodian-only
mapping already produced by `adjudication.py`. It emits a judge packet with
only opaque `RPT-NNN` identifiers and an allowlisted, hash-bound review surface.
It excludes original episode IDs, original decisions, rationales, ordering,
source-bank paths, and the repeat mapping. A separate finalizer validates all 10
fresh judgments and writes immutable repeat results plus a custody manifest.

### 3.2 Cue/evidence custody lane

`custody.py` consumes a frozen schedule and an exact inventory of evidence
bundle artifacts. It creates one private row per C0/C1/C2 primary call and its
matched probe, binding module, episode, actor, cue, logical-call IDs, request
hashes, bundle ID, and exact evidence-bundle hash. It rejects missing,
duplicate, cross-bundle, cross-cue, or tampered relationships. No private
manifest is model-visible or judge-visible.

### 3.3 Synthetic analysis lane

`analysis.py` accepts typed synthetic observation rows and produces deterministic
JSON/CSV tables for missingness, module-native vector summaries, strata, red-line
incidents, action-probe consistency, cue contrasts, and repeat agreement. It
must refuse cue contrasts without a verified custody manifest and must label
all fixture outputs `SYNTHETIC_VALIDATION_ONLY`. It produces no composite score,
ranking, best-model claim, p-value, or empirical manuscript result.

### 3.4 Paper and cost lane

The cost checkpoint records a current, source-cited shortlist of inexpensive
general-purpose models, exact planned call geometry, unit prices, worst-case
cost formulas, hard stop conditions, and a zero-call status. It is a proposal,
not authorization. The methods PDF is rendered from the existing manuscript,
retains `PENDING_EMPIRICAL_RUN`, and is visually checked page by page.

## 4. Data and custody rules

- Pass-one and repeat files are immutable after finalization.
- The repeat mapping is custodian-only and never copied into judge artifacts.
- Repeat judging finishes before any pilot call or output exposure.
- Cue custody uses exact SHA-256 bindings for requests and evidence bundles.
- Synthetic fixtures never contain or imitate real provider responses.
- Roster research may use public documentation but no provider API or key.
- No cost proposal is authority to spend.
- Existing active adjudication files are read-only during this work.

## 5. Error handling

Every executable lane fails closed on schema failure, hash mismatch, duplicate
identity, missing row, wrong relationship, an existing immutable output, or a
scope-forbidden field. Errors name the invalid relationship without exposing
private mapping contents or model identity to judge-visible surfaces.

## 6. Testing and sufficiency gate

Each new behavior follows test-first RED-GREEN-REFACTOR development. The offline
package is sufficient when:

- repeat packet tests prove no original ID, decision, rationale, or mapping is
  visible and immutable finalization works;
- custody tests prove complete 3-cue primary/probe coverage and reject tamper or
  cross-linking;
- analysis tests prove deterministic synthetic tables, cue-gate enforcement,
  vector-only reporting, and no ranking/composite leakage;
- the cost checkpoint has live source citations, explicit assumptions, and a
  hard zero-call/zero-spend statement;
- the PDF renders without clipping, overlap, broken glyphs, placeholder result
  claims, or unreadable references; and
- the full credential-free suite and an independent integrated P0/P1 review pass.

P2/P3 deployment hardening remains deferred unless it can change the registered
pilot conclusion.

## 7. Closing artifacts

- judge-safe repeat schema, packet builder, finalizer, and tests;
- private cue-custody schema, builder, verifier, synthetic fixture, and tests;
- synthetic analysis module, exports, empty paper tables/figures, and tests;
- cited cheap-model roster and cost checkpoint with no calls made;
- methods PDF plus rendered-page QA evidence;
- updated manuscript, claims/limitations surfaces if required; and
- updated portfolio dashboard and active critical path.
