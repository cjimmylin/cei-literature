<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY descriptive MVP v0.1 release-candidate manifest

**Frozen:** 2026-07-14
**Prepared by:** Codex
**Status:** technically verified release candidate; Jimmy circulation/authorship sign-off pending

## 1. Canonical candidate

| Artifact | Size | SHA-256 |
|---|---:|---|
| `PAPER/walkworthy-mvp-manuscript.md` | 20,516 words | `dcf329166a4cb064adf779e8aa3e0e4429a120a9305cd8e0c7c6d5f537f9e214` |
| `PAPER/walkworthy-mvp-manuscript.pdf` | 36 US-letter pages | `1b678a5317581db38801964632992973572d2f4519be7cc871f6ffafaeba0a4e` |

These paths and hashes define candidate v0.1. Any later edit creates a new candidate
hash and requires a new dated manifest; this file is never rewritten.

## 2. Claim boundary

This candidate is a complete descriptive artifact paper. It licenses claims about:

- the declared-corpus construct and ten-design benchmark architecture;
- public artifact counts, governance, pre-registration, and execution custody;
- provisional O5 checkpoint readings with their registered limitations;
- the complete 60-item, three-SUT exploratory MVP-A1 execution and its descriptive
  compatibility/coverage results.

It does **not** license a model ranking, a released WALKWORTHY design, judge validity,
MVP cheap-judge accuracy, a G7 flip rate, or a claim that any model is ethical,
Christian, or aligned with Christianity. O5 and MVP-A1 remain separate evidence
surfaces.

## 3. Release audit

| Check | Result |
|---|---|
| Numerical/claim conformance | PASS; the prior reviewed values and PR-22 MVP/O5 correction remain intact |
| Citations | PASS; 53 in-text citation atoms match bibliography entries |
| Tables and figure | PASS; Tables 6.1–6.5 and Figure 1 are present, labeled, and unclipped |
| Paper structure | PASS after adding §11 Conclusion |
| Reproducibility surface | PASS after replacing future-tense command promises with this manifest |
| PDF | PASS; tagged, 36 US-letter pages, unencrypted, no JavaScript |
| Visual inspection | PASS; every page rendered at 110 dpi, contact-sheet reviewed, and critical pages inspected at full resolution |
| Offline harness | PASS; 549/549 tests in 99.38 seconds |
| Placeholder/internal-token scan | PASS |
| HOLDOUT boundary | PASS; no HOLDOUT content was loaded or quoted |

No P0/P1 paper defect remains in the candidate. Venue-specific citation formatting and
final author/affiliation metadata are owner/venue surfaces, not scientific blockers.

## 4. Exact offline reproduction commands

Run the mock-first regression suite from the benchmark directory:

```bash
cd harness
../../../../../.venv/bin/python -m pytest tests/ -q
```

Regenerate the PDF on the verified macOS toolchain:

```bash
cd PAPER
/opt/homebrew/bin/pandoc walkworthy-mvp-manuscript.md \
  --from markdown \
  --pdf-engine=/opt/homebrew/bin/typst \
  --resource-path=. \
  --pdf-engine-opt=--root=/ \
  --toc --toc-depth=2 \
  -V papersize=us-letter \
  -V fontsize=9pt \
  -V page-numbering=1 \
  -o walkworthy-mvp-manuscript.pdf
```

Verify the frozen artifacts:

```bash
shasum -a 256 \
  PAPER/walkworthy-mvp-manuscript.md \
  PAPER/walkworthy-mvp-manuscript.pdf
pdfinfo PAPER/walkworthy-mvp-manuscript.pdf
pdftotext -layout PAPER/walkworthy-mvp-manuscript.pdf -
```

No live smoke or scored-panel command is part of this descriptive release. Live model
execution remains subject to separate credential, roster, and spending authorization.

## 5. Outstanding owner decision — bundled once

The manuscript currently uses the byline `Anonymous manuscript`. Codex cannot choose
authorship or authorize public circulation. The recommended immediate disposition is
private scholarly circulation of the exact candidate while human labels proceed.

Jimmy can close both owner-only questions with this exact one-liner:

> Ratify WALKWORTHY descriptive MVP v0.1 at manuscript SHA-256
> `dcf329166a4cb064adf779e8aa3e0e4429a120a9305cd8e0c7c6d5f537f9e214` and PDF
> SHA-256 `1b678a5317581db38801964632992973572d2f4519be7cc871f6ffafaeba0a4e`
> for private circulation under the `Anonymous manuscript` byline; descriptive claims
> only, with no public release, O5 verdict, paid call, or scale-up authorized.

Public preprint release requires one later bundled owner instruction containing the
exact author/affiliation line and public-release approval. It does not require more
benchmark engineering.

## 6. Upgrade path

Human labels are an independent release-grade upgrade lane. When one complete PUBLIC
design and its registered reliability input exist, run G4, available Part B,
recomputation/status, and the paper update in one session. The descriptive v0.1
candidate need not wait for that work.
