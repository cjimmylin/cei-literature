<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# WCF-Bench MVP Exploratory Paper

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

**Status:** Offline paper-only assembly dated 2026-07-14. This directory is an
append-only manuscript artifact assembled from the accepted PPP-1 paper packet,
the existing WCF-Bench pre-draft, and the immutable PPP-1 report and metadata.

**Authority:** $0 paper assembly only. No network, model, API, credential, runner,
bank, manifest, judge, panel, gate, ruling, or release action was authorized or
performed.

## Files

- `manuscript.md` - integrated exploratory manuscript source.
- `wcf-bench-mvp-exploratory-paper.pdf` - offline Pandoc/Typst rendering.
- `traceability.md` - claim-to-source map for every empirical, cost, and runtime
  statement in the manuscript.
- `source-manifest.json` - SHA-256 inventory of every source used and every copied
  asset.
- `figures/` - two unchanged accepted PPP-1 SVG figures.
- `tables/` - unchanged accepted PPP-1 tables 01, 02, and 03 in Markdown and CSV.

## Offline rendering

From this directory:

```bash
ROOT=/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark
PAPER="$ROOT/08-PAPER/20260714-mvp-exploratory-paper"
PPP="$ROOT/08-PAPER/20260713-ppp1-exploratory-preview"
/opt/homebrew/bin/pandoc manuscript.md --from=gfm+footnotes --to=pdf --standalone --pdf-engine=/opt/homebrew/bin/typst --pdf-engine-opt=--root=/ --resource-path="$PAPER:$PPP:$ROOT" --toc --toc-depth=2 -V papersize=us-letter -V margin.top=0.75in -V margin.bottom=0.75in -V margin.left=0.82in -V margin.right=0.82in -V mainfont='Libertinus Serif' -V fontsize=10pt -V linestretch=1.08 -V page-numbering=1 -o wcf-bench-mvp-exploratory-paper.pdf
```

## Source and claim boundaries

The prose uses only the existing paper pre-draft (`08-PAPER/01-abstract-skeleton.md`
through `08-PAPER/10-ethics-release.md`), the accepted immutable packet at
`08-PAPER/20260713-ppp1-exploratory-preview/`, and the controlling immutable PPP-1
report, metadata, and checkpoint custody fields identified in `traceability.md`.
No raw prompt or response text is reproduced.

This paper does not rank models and does not support external quotation, public
release, release readiness, panel consensus, judge-family robustness, gate outcomes,
perturbation claims, cross-family robustness, or T4 completion. PPP-1 does not amend,
replace, or satisfy registered T4.
