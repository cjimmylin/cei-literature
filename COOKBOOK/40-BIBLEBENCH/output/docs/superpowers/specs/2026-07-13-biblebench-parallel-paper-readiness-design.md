# BibleBench Parallel Paper-Readiness Design

**Date:** 2026-07-13  
**Status:** OWNER-APPROVED DECOMPOSITION; written specification awaiting owner review  
**Owner:** Jimmy Lin  
**Implementation worktree:** `codex/biblebench-pilot`

## 1. Objective and authority

This package advances BibleBench while the owner completes theologian-technical
adjudication. It produces paper, judging, runner, analysis, and design-PDF
artifacts that do not require model evidence and do not contaminate the owner's
independent judgments.

The empirical target follows the owner-ratified low-cost MVP ruling PF-002:

- all 48 frozen episodes, 12 per module;
- exactly one preregistered C1 primary plus matched probe per episode;
- exactly three inexpensive general-purpose models;
- one founding theologian-technical judge;
- exploratory, descriptive, non-ranking claims;
- a preflight forecast at or below $3.00 and a $5.00 hard ceiling; and
- separate written authority before credential access, provider calls, or spend.

This package authorizes no live model call, credential access, balance query,
provider mutation, roster approval, or spend. It must remain useful if the owner
later changes the exact three-model manifest.

## 2. Delivery strategy

Four lanes run concurrently after their implementation plans are approved.
They have disjoint primary ownership and communicate only through registered
artifacts.

### 2.1 Paper lane

The paper lane replaces the local-citation scaffold with a source-verified
related-work review and a venue-neutral, submission-shaped methods-and-pilot
draft. The core manuscript remains adaptable to AI-ethics, NLP evaluation, or
religion-and-technology venues without claiming compliance with a venue whose
template has not been selected.

The lane delivers:

- a completed related-work section covering behavioral and agentic evaluation,
  stated versus enacted values, LLM judging and human adjudication, construct
  validity and psychometrics, and relevant biblical/Christian evaluation work;
- a bibliography containing only verified sources with stable DOI, proceedings,
  publisher, or arXiv identifiers;
- an adapted manuscript structure: Abstract, Introduction, Related Work,
  Construct and Theological Frame, Benchmark Design, MVP Protocol, Planned
  Analysis, Ethics, Limitations, Results placeholder, and Discussion scaffold;
- reproducibility, ethics, limitations, and data-card appendices; and
- no novelty, performance, ranking, or consensus claim unsupported by evidence.

Technical evaluation sources must be primary papers or official documentation.
Biblical and theological claims must cite the passage and suitable scholarly or
confessional sources; repository handoffs remain design provenance, not external
scholarship. All citations must be locally resolvable through `references.bib`.

### 2.2 Human-judging lane

The judging lane builds a local, offline HTML interface for the 48-record owner
packet. It reduces navigation and transcription cost while preserving the
single-expert, owner-authored nature of the provisional gold.

The interface:

- runs without a server, network request, external font, analytics, or CDN;
- presents one record at a time with progress, module/role filters, keyboard
  navigation, autosave to browser-local storage, and explicit JSON import/export;
- shows only the already authorized review content and registered rubric;
- never proposes a decision, rationale, confidence level, applicability result,
  theological interpretation, repair, or wording change;
- labels every field as pending until the owner enters it;
- validates required fields, allowed values, applicability/decision coherence,
  confidence/rationale rules, and record completion;
- reports only mechanical warnings such as missing fields or contradictions;
- cannot finalize, overwrite, or mutate the authoritative YAML packet directly;
  and
- exports a judge-authored draft that the existing fail-closed finalizer validates.

The blinded repeat remains a separate later interface generated only from a
frozen pass-one packet. The pass-one interface never reveals repeat membership.

### 2.3 No-spend MVP runner lane

The runner lane implements the narrowed PF-002 geometry rather than the earlier
seven-call C0/C1/C2 schedule. It compiles exactly:

`48 episodes × 3 actors × (1 C1 primary + 1 matched probe) = 288 logical calls`.

The runner delivers:

- a strict MVP manifest schema containing exact model and provider identities,
  C1 surface hashes, request hashes, token caps, decoding parameters, retry rule,
  price evidence date, forecast, $5.00 cap, and authorization state;
- a deterministic compiler that derives all 288 calls from the frozen bank;
- provider-neutral request objects plus offline shape adapters for the three
  proposed provider families, with secrets and live transport absent;
- fail-closed budget accounting using registered maximum tokens and unit prices;
- no fallback and at most one explicitly registered technical retry;
- terminal missingness for unknown delivery or exhausted retry;
- immutable request/response/usage/receipt artifact contracts;
- a deterministic synthetic provider that exercises success, refusal,
  malformed output, truncation, rate limit, and unknown-delivery paths; and
- synthetic dry-run outputs unmistakably labeled `SYNTHETIC_VALIDATION_ONLY`.

The manifest fixture uses synthetic aliases and zero prices. Any real manifest
must remain `PROPOSAL_ONLY` and `authorized: false` until the owner approves the
exact roster, routes, prices, token ceilings, retry rule, expiry, and NTE.

### 2.4 PDF and analysis lane

The PDF lane produces nine stable design-only reports. Every report is marked
`PRE-EMPIRICAL DESIGN REPORT`, contains no model outcomes, and has a machine and
visual QA record.

The exact inventory is:

1. `01-biblebench-consolidated-design-and-methods.pdf`
2. `02-fruitbench-design-report.pdf`
3. `03-corinthlove-design-report.pdf`
4. `04-10cbench-30-design-atlas.pdf`
5. `05-sermonmount-design-report.pdf`
6. `06-shared-episode-protocol-and-custody.pdf`
7. `07-human-adjudication-handbook.pdf`
8. `08-reproducibility-ethics-and-data-card.pdf`
9. `09-analysis-tables-figures-and-claims-boundary.pdf`

The 10CBench atlas includes all 30 registered designs, even though the
consolidated 48-episode MVP uses only the approved 10CBench core families.
The four module reports preserve their passage-specific constructs, exclusions,
failure poles, provenance, and pluralistic evangelical-Protestant boundaries.

The analysis artifacts include final table shells and figure-data contracts for:

- completion and missingness;
- module-native dimension vectors;
- common-life and Christian-facing strata;
- action/probe consistency;
- red-line incidents;
- single-expert adjudication confidence and contestability; and
- descriptive model-by-module patterns.

They exclude p-values, composites, leaderboards, best-model fields, cue effects,
capability-adjusted attribution, and family-level estimates. Pre-run tables use
headers and explicit `PENDING_EMPIRICAL_RUN` bodies rather than fabricated values.

## 3. Data flow and ownership

The frozen episode bank and source-provenance hashes are read-only inputs. The
owner's adjudication packet remains the sole authoritative judgment surface.

```text
frozen bank ──> judge-interface builder ──> owner-authored draft
      │                                      │
      │                                      └─> existing fail-closed finalizer
      │
      ├──> MVP schedule compiler ──> synthetic provider ──> synthetic custody
      │
      └──> paper/PDF builders ──> pre-empirical manuscript and nine PDFs

verified literature ──> references.bib ──> related work and appendices
```

No lane may write to the authoritative owner packet, frozen episode banks,
historical handoffs, or main-workspace living surfaces. Living dashboard and
critical-path updates occur only during final integration after reconciling the
newer concurrent main-workspace state.

## 4. Contamination and privacy controls

The following are prohibited from judge-visible artifacts:

- suggested answers, rationales, labels, confidence, applicability, or repairs;
- previous or repeat decisions;
- model, provider, actor, condition, or run-order identity;
- repeat membership or the private repeat mapping;
- analysis summaries derived from owner decisions; and
- private custody manifests or credentials.

Mechanical validation may identify an empty field, an invalid enum, a required
rationale, or an internal contradiction. It may not state which substantive
value would resolve the warning.

The judge interface stores drafts only in the user's browser and exported local
files. It performs no network operation. A Content Security Policy forbids
connections, remote media, embedding, and form submission.

## 5. Error and stop behavior

- Missing or malformed citation metadata blocks the affected citation and claim,
  not unrelated manuscript drafting.
- A judge draft with any incomplete or contradictory record remains visibly
  `DRAFT_INCOMPLETE` and cannot enter the finalizer.
- The synthetic runner refuses real-looking provider/model identities and any
  nonzero authorization or spend state.
- The real runner path refuses an expired, unapproved, over-budget, fallback-
  enabled, or incompletely hashed manifest before transport construction.
- Unknown delivery is terminal; automatic replay is prohibited.
- PDF generation fails on missing source sections, unresolved placeholders other
  than the registered empirical sentinel, empty pages, missing metadata, or
  non-searchable text.
- Any P0/P1 that could change the narrowed MVP paper claim stops integration.
  P2/P3 polish is disclosed and deferred.

## 6. Verification

### 6.1 Literature and manuscript

- Every manuscript citation key resolves to `references.bib`.
- Every bibliography record has a verified stable identifier or an explicitly
  local design-provenance type.
- No incomplete-literature marker remains in the submission-shaped draft.
- `PENDING_EMPIRICAL_RUN` appears exactly once in Results.
- Claim-registry types and limitations remain consistent with manuscript prose.

### 6.2 Judge interface

- Exactly 48 unique records load.
- No record contains a suggested judgment or repeat membership.
- Import/export round-trips losslessly.
- Reload restores local drafts.
- All invalid field and coherence cases fail mechanically without answer advice.
- A network-attempt test finds no external URL or permitted connection target.

### 6.3 Runner

- Exactly 288 logical calls compile: 144 C1 primaries and 144 probes.
- All calls bind exact bank, surface, request, actor, and primary/probe identities.
- Synthetic runs are byte-reproducible and cannot be mistaken for model evidence.
- Retry, missingness, receipt, custody, and budget-stop paths are tested.
- No credential lookup, socket, HTTP client, or paid provider call occurs.

### 6.4 PDFs and analysis

- Exactly nine named PDFs build deterministically.
- Each PDF has correct title, author, subject, pre-empirical status, searchable
  text, page numbering, and nonempty pages.
- The 10CBench report contains all 30 design identifiers.
- Every page is rendered with Poppler and inspected as a contact sheet plus dense
  representative pages.
- No clipped text, overlap, broken glyph, unresolved citation, empirical value,
  ranking, or composite appears.

## 7. Completion boundary

This package is complete when the verified literature, venue-neutral manuscript,
appendices, 48-record judge interface, PF-002-compliant synthetic runner, table
and figure templates, and nine visually verified design PDFs exist in one clean
commit with no live calls or spend.

The empirical phase remains separate. After the owner completes a scientifically
adequate provisional-gold pass, the project freezes the real three-model
manifest, requests explicit authority, runs once within the approved cap, and
replaces only the registered empirical sentinels with actual descriptive results
or a documented failure account.
