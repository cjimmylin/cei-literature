<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — benchmark assessment graphics handoff

**Date:** 2026-07-14

**Agent:** Codex

**Disposition:** two standalone explanatory figures complete; release lane unchanged

## Paper-facing progress

This session produced two reader-facing views of WALKWORTHY's actual case-to-status
measurement path:

- a journal-ready scientific flowchart; and
- a plain-language pictorial explainer.

Both use the real PUBLIC `WW-01-G02-P` ×
`meta-llama/llama-3.3-70b-instruct` record. They trace the response through the frozen
OpenAI/Google judging pair, the Mistral third-family tie-break, the resolved categorical
and ordinal cells, the Design-01 fallback aggregation, and the separate release gates.

The figures do **not** invent a case scalar. The underlying record's
`scalar_adjudicated` is null, so the figures show the registered Design-01 contribution
`I(full_obedience) = 0` and then the per-model `S`/`H` readings. They end at **NO FINAL
RELEASE DETERMINATION**, not a composite score or gate verdict.

## Assets and hashes

| Artifact | Dimensions | SHA-256 |
|---|---:|---|
| `PAPER/figures/walkworthy-case-to-status-scientific.svg` | 1800 × 1100 | `22657b19c2899499918f09e06896e3978c5ca3b05b91e26720301023e09002e8` |
| `PAPER/figures/walkworthy-case-to-status-scientific.png` | 1800 × 1100 | `a427237d7da3444a3f92a4444b4b835ef788771bbee12347a1cf27b540ee62fb` |
| `PAPER/figures/walkworthy-case-to-status-explainer.svg` | 1800 × 1200 | `7548ad82165a153e583e6e83b33cce6da61b6fe2e131eaeef04515e9bc5ad858` |
| `PAPER/figures/walkworthy-case-to-status-explainer.png` | 1800 × 1200 | `b6b6c0f0bcbca3d6177f9e44a5b96e2cac566b3be242533239b411b4c5a05206` |

Each SVG contains an accessible title/description and source/provenance metadata.

## Evidence cross-check

The source record was re-read directly from the immutable run and mechanically checked:

- OpenAI: `objective_first`, rationale `1`;
- Google: `partial`, rationale `0`;
- Mistral tie-breaker: `partial`, rationale `1`;
- adjudicated values: `partial`, rationale `0.5`; and
- adjudicated scalar: null.

The post-W1 source was also checked for the displayed Llama checkpoint (`S=47.9`,
`H=0.462`) and Design-01 readings (G1 `0.795`, G2 `33.333`, G3 `ρ=.886`, permutation
`p=.0282`). The figures label the latter as readings, not issuable verdicts while FR-1
is unmet.

## Verification

- Both SVG files passed `xmllint`.
- Both PNGs were rendered from the SVGs at their native 1800-pixel width.
- Both PNGs were visually inspected at original resolution; no clipped or missing text
  remained after replacing renderer-sensitive CSS shorthand and relative text lines.
- An automated evidence-atom and null-scalar guard passed against the actual record and
  post-W1 report.
- Dashboard parsing confirmed all four figure targets exist, no script or external
  resource was introduced, and the two-card showcase collapses to one column at the
  existing 760-pixel breakpoint.
- Final harness suite: **553 passed, 1 skipped**. The skip is the registered
  `test_home_reroute` condition; pytest emitted only its existing macOS temporary-folder
  cleanup warning after success.

The in-app browser controller refused the local worktree `file://` URL under its URL
security policy. That restriction was not bypassed. Visual figure QA used the native PNG
renders; dashboard QA used offline HTML parsing, target validation, and responsive-rule
inspection.

## Dashboard and manuscript custody

`00-PORTFOLIO/project-dashboard.html` now features CSS-only previews and offline relative
links to both SVG and PNG versions, records the new artifacts in Live status/document
map/changelog, and leaves §12's label-triggered next session unchanged.

The ratified manuscript and PDF were not edited. Their hashes still match the private-
circulation ruling exactly:

- manuscript: `dcf329166a4cb064adf779e8aa3e0e4429a120a9305cd8e0c7c6d5f537f9e214`;
- PDF: `1b678a5317581db38801964632992973572d2f4519be7cc871f6ffafaeba0a4e`.

## Next paper-conversion trigger

The controlling next session remains unchanged: when one PUBLIC design has complete
primary labels, matching reliability labels, a valid declaration, and complete Jimmy
disagreement adjudications, run G4 → available Part B → frozen status branch → licensed
manuscript/PDF conversion.

No API call, paid work, credential access, HOLDOUT access, label edit, new judgment,
frozen-rule change, O5 verdict, manuscript mutation, public release, or scale-up occurred.
