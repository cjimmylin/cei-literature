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

## The 17 papers with `ethics_overall: Yes/No` (owner decision)

The 17 alignment papers added on 2026-07-10/11 carried the acquisition templates' `Yes`/`No`.
Converted to the vault's own mapping (`ethics_scoring.parse_ethics_value`: Yes → 80, No → 0),
the same value the 60 alignment papers acquired on 2026-07-09 already hold: 9 → 80, 8 → 0.
Single-line edits; dashboard data unchanged (the generator already read Yes as 80).

The keyword scorer was not used: it misses alignment documents (see the "Constitutional AI /
TruthfulQA Issue" in `_OPERATING-SYSTEM/Standards/classification-logic.md`). It would have scored
Claude's Constitution and OpenAI's Model Spec at 0 and put 47 of the 60 sibling papers below 50.
The five framework fields of these 17 keep their template 0/1 values.

## Not changed (follow-ups)

- The 77 alignment papers from July (60 + the 17 above) have acquisition labels as scores, not
  scorer output. Scoring them properly needs the scorer fix the standard describes (alignment
  keywords such as harmlessness, truthfulness) or a reviewed pin list.
- 57 notes had an `abstract` that is leftover web-search tool output ("I've completed the web
  search…", "Based on the search results…"); 13 fixed from PDF extracts, 44 left: `logs/20261018-junk-abstracts.md`.
- 13 likely duplicate note pairs (`DASHBOARDS/cei-dashboard-14/build/likely_duplicates.txt`).
