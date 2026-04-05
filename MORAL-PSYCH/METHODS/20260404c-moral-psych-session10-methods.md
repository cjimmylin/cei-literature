# Methods: File Safety Remediation and Non-Western Framework Score Application

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/MORAL-PSYCH/` (primary), vault-wide papers

## Data and Materials

- **Paper corpus:** 2,368 Markdown files in `CEI-Lit-WS/papers/`, each with YAML frontmatter containing metadata and classification scores
- **Non-Western scoring engine:** `CULTURAL-GLOBAL/SCRIPTS/nonwestern_scoring.py` — keyword-based scorer for 7 non-Western normative ethical frameworks (Confucian, Ubuntu, Islamic ethics, Buddhist, Dharmic, Indigenous relational, Buen Vivir)
- **Scoring orchestrator:** `CULTURAL-GLOBAL/SCRIPTS/score_nonwestern_frameworks.py` — batch processor with YAML write-back capability
- **Git version control:** All files tracked in the CEI-Lit-WS repository; deleted files recoverable via `git checkout`

## Procedure

### File Safety Remediation

A prior session had deleted 10 files using `rm`/`unlink` rather than the mandated `mv`-to-RECYCLE-BIN protocol. Remediation proceeded in three steps:

1. **Identification:** `git diff --name-status HEAD` was used to enumerate all uncommitted deletions (10 files: 5 archive reports, 1 PDF extract, 1 Python utility script, 3 paper files).
2. **Restoration:** All 10 files were restored from git using `git checkout -- <path>`.
3. **Triage and safe disposal:**
   - 7 files (archive reports, utility script, PDF extract) were moved to `RECYCLE-BIN/session9-cleanup/` per the vault's no-deletion safety rule.
   - 3 paper files (FatwaSet, UniMoral, IslamTrust) were identified as legitimate papers with full YAML frontmatter (134–193 lines each) and left restored in `papers/`.

### Non-Western Framework Score Application

The `nw_*` fields (7 fields per paper) had been added to all paper frontmatter with initial value 0 in a prior session. A fully validated scoring pipeline existed but had been run without the `--write-yaml` flag, leaving scores unwritten.

1. **Dry-run verification:** The scoring script was tested on a 5-paper subset to confirm correct execution.
2. **Full scoring run:** `score_nonwestern_frameworks.py --write-yaml` was executed on all 2,368 papers. The script reads each paper's title, abstract, and PDF extract text, applies regex-based keyword matching across three tiers (strong: 15 points, medium: 5 points, false-positive: -10 points) with title bonus (+20), strong-match floors, and co-occurrence boost, clamped to [0, 100].
3. **Validation:** `validate_all_papers.py` was run post-scoring to confirm YAML integrity. Result: 2,360/2,368 valid; 8 errors were pre-existing format issues unrelated to the scoring.

## Analysis

Non-Western framework scores were computed using the established keyword-heuristic pipeline (no LLM). The scoring formula mirrors the Western ethics and moral psychology pipelines:

```
score = strong_matches × 15 + medium_matches × 5 - fp_context × 10 + title_bonus(20)
```

Scores are clamped to [0, 100]. A paper is considered "detected" for a framework when its score >= 50. A strong-match floor ensures that papers with 2+ strong matches or corroborated single strong matches receive a minimum score of 50. A co-occurrence boost ensures multi-tradition papers (2+ frameworks with strong matches) have all matched fields at >= 50.

## Computational Environment

- Python 3.9 via `../.venv/bin/python`
- No external API calls required — all scoring is local regex-based
- Processing time: ~2 minutes for 2,368 papers on Apple Silicon

## Limitations and Decisions

1. **Keyword-based scoring inherently limited:** Philosophical nuance cannot be fully captured by regex patterns. The pipeline prioritizes recall over precision (documented F1 range: 0.29–1.0 across frameworks).
2. **Paper count discrepancy:** The scorer found 2,368 papers versus the expected ~2,043; the additional files may include collection/project entries and should be audited.
3. **Pre-existing validation errors left unfixed:** The 8 EXSR-series papers with "orphaned list item" warnings were not modified, as the issue is a validator limitation with the YAML list format for `authors:`, not a data integrity problem.
