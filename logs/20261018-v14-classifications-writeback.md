# 20261018 — Write dashboard v14's classifications of the 402 new papers into the vault

**Script:** `PYTHON/apply_v14_classifications.py` (dry run by default; `--apply` to write; safe to re-run)
**Input:** `DASHBOARDS/cei-dashboard-14/build/overlay_v14.json` (provenance: `DASHBOARDS/cei-dashboard-14/build/README.md`)

## Why

Dashboard v14 classified the 402 papers added after v13 (cultures, languages, religion and
moral-psychology scores, missing framework scores, authors, venue, models evaluated) but kept the
values in a build overlay. A dashboard rebuilt from the vault would have lost them, and the
generator's inputs (`logs/*.json`) were gitignored and absent from the repo.

## What changed

391 notes, 6,536 lines: 174 empty lines filled in place (`CONF-CC` 47, `LLM_assessed` 10,
`cultures_nationalities_list` 48, `national_ethnic_cultural` 48, `languages_list` 21) and 6,362
lines added at the end of the frontmatter (`rv_*` 3,290, `mp_*` 1,880, `last_author` 294,
`moral_psychology` 235, `cultures_nationalities_list` 166, `national_ethnic_cultural` 155,
`CONF-CC` 99, `religious_values_list` 60, `LLM_assessed` 51, `first_author` 20, `url` 20,
`languages_list` 12, five framework scores 16 each).

No existing value was changed: 20 fields that already had a value were kept (e.g.
`national_ethnic_cultural: Islamic` was not replaced by the review's `Arabic`). No body text,
no other lines, no deletions.

## Checks

- `validate_all_papers.py`: 2,445 / 2,445 valid, 0 errors.
- Re-running the script changes nothing.
- The dashboard rebuilt from the vault alone (`PYTHON/build_vault_dashboard_14.py`) matches the
  overlay build exactly except one venue name corrected by hand (AraQA → `JAC-ECC 2023`) and one
  author name now shown as a wikilink, and matches published v14 except corrections from the
  2026-10-18 repair (6 venue years, 4 author lists, 1 title, 33 abstracts).

## Not changed (follow-ups)

- 17 papers added on or after 2026-07-09 still have `ethics_overall: Yes/No`, and the 60 other
  alignment papers from 2026-07-09 hold the acquisition script's hard-coded `80`, not a score.
- 40 notes have an `abstract` that is leftover web-search tool output ("I've completed the web
  search…", "Based on the search results…"), not an abstract.
- 13 likely duplicate note pairs (`DASHBOARDS/cei-dashboard-14/build/likely_duplicates.txt`).
