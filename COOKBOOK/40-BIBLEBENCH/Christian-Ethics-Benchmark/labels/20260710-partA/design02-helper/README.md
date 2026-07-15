# WALKWORTHY Design 02 labeling helper

Use modern Chrome. Each HTML page is a standalone `file://` tool: no network or server
is required. Primary and reliability drafts use isolated localStorage. Keep every
returned file private. This packet contains no model, judge, unblinding, or HOLDOUT
content.

## Workflow

1. Jimmy opens `02-primary-labeling.html` directly, completes all 21 turns across 12
   units, reviews the entries, and downloads
   `02-twomasters-partA-primary-completed.csv`.
2. The independent labeler receives **only** `02-reliability-labeling.html` and
   `../02-twomasters-partA-instructions.md`, completes all seven turns across four
   units, reviews the entries, and returns
   `02-twomasters-partA-reliability-completed.csv`. Never send the primary CSV,
   primary page, or primary draft to the independent labeler.
3. Jimmy opens `02-finalization.html`, loads both completed CSVs, supplies distinct
   opaque labeler IDs and ISO-8601 completion timestamps with offsets, adjudicates every
   displayed turn disagreement, and downloads `reliability-declaration.json` and
   `adjudications.jsonl`. When all overlap labels agree, `adjudications.jsonl` may be a
   zero-byte file.
4. Codex verifies and imports the returned files. Humans must not overwrite repository
   CSVs manually.
5. Codex runs the existing PR-29 command below. Downloads are inputs, not G4 or release
   results.

From `harness/` after Codex has verified and imported the inputs:

```bash
../../../../../.venv/bin/python -m walkworthy.judge_validation \
  --labels ../labels/20260710-partA \
  --run-path ../runs/20260711-o4-panel/scored_items.jsonl \
  --reliability-manifest ../labels/20260710-partA/reliability/overlap-manifest.json \
  --reliability-labels ../labels/20260710-partA/reliability \
  --reliability-declaration ../labels/20260710-partA/reliability/reliability-declaration.json \
  --adjudications ../labels/20260710-partA/reliability/adjudications.jsonl \
  --date YYYYMMDD \
  --out ../00-PORTFOLIO/YYYYMMDD-o5-g4-judge-validity.md
```

If any page reports an error, stop and return the exact message to Codex. Do not edit a
CSV manually to bypass it.
