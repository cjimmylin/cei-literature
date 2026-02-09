# Author-Paper Linking & Last Author Annotation — Status Log

**Date:** 2026-02-08

## Phase Summary

| Phase | Status | Key Result |
|-------|--------|------------|
| 1. Build Map | Done | 846 papers parsed, 4,245 unique authors found, 13/82 "et al." resolved via API |
| 2. Disambiguate | Done | 80.9% match rate (3,436 matched), 809 new authors identified |
| 3. Update Papers | Done | 846 papers got `last_author` field, 13 author lists expanded, 69 flagged `authors_incomplete` |
| 4. Rebuild Profiles | Done | 3,195 profiles updated, 791 stubs created, 2,830 enriched with affiliations |
| 5. Verify | Done | 0 errors, 846/846 YAML valid |

## Final Counts

- **846 papers** — all have both `first_author` and `last_author` YAML fields
- **4,145 author profiles** (up from 3,354 — 791 new stubs)
- **69 papers** still have "et al." in `authors` field (flagged `authors_incomplete: true`)
- **809 disambiguation review queue items** in `logs/20260208-disambiguation_review_queue.json` for optional manual review

## Remaining Known Limitations (warnings, not errors)

- 258 first_author format mismatches — "LastName, FirstName" in `authors` field vs "FirstName LastName" in `first_author` wikilink. These are cosmetic format differences, not data errors.
- 873 author names in paper YAML lack exact-match profiles due to the same format difference. The profiles exist under the normalized name.
- Affiliation enrichment from PDF extracts has some noise (abstract text fragments misidentified as affiliations).
