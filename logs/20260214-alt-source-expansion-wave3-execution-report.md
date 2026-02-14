# Wave3 Alt-Source Expansion Execution Report

- Date: 2026-02-14
- Scope: exhaustive rerun of unresolved PDF discovery with additional source methods + strict apply waves.

## Script Enhancements
- Updated `CEI-Lit-WS/PYTHON/discover_alt_pdf_sources.py`.
- Added methods:
  - `semantic_scholar_doi` / `semantic_scholar_title`
  - `core`
  - `openaire_doi`
  - `host_transform` expansions for publisher PDF URL patterns
- Added retry/backoff for API calls (`429/5xx`) and richer HTML URL extraction.

## Discovery Run (Exhaustive)
- Input unresolved (post-p2-metadata-fix): 224
- Candidate rows generated: 871
- Papers with candidates: 202
- Papers with best direct PDF: 37
- Papers with best direct PDF confidence >=70: 37
- Outputs:
  - `CEI-Lit-WS/logs/20260214-alt-method-source-candidates.csv`
  - `CEI-Lit-WS/logs/20260214-alt-method-priority-shortlist.csv`
  - `CEI-Lit-WS/logs/20260214-alt-method-summary.json`

## Apply Waves
1. Wave3 shortlist apply (`37` rows)
- Dry-run: accepted `13`, already_has_pdf `6`, download_failed `7`, rejected `11`
- Full apply: accepted `13`

2. EuropePMC fallback salvage (`7` rows, from PMC PoW interstitial failures)
- Dry-run: accepted `6`, rejected `1`
- Full apply: accepted `6`
- Preserved logs:
  - `CEI-Lit-WS/logs/20260214-alt-method-direct-apply-summary-wave3-europepmc-fallback-dryrun.json`
  - `CEI-Lit-WS/logs/20260214-alt-method-direct-apply-summary-wave3-europepmc-fallback-apply.json`

3. Additional direct-candidate wave from full table (`20` rows)
- Dry-run: accepted `1`, download_failed `1`, rejected `18`
- Single apply of accepted row: `2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata.md`
- Preserved logs:
  - `CEI-Lit-WS/logs/20260214-alt-method-direct-apply-summary-wave4-kajiwara-apply.json`

## Net State
- Initial unresolved (post-p2-metadata-fix): `224`
- Final unresolved: `196`
- Net resolved since initial: `29`
- Newly unresolved since initial: `1`
  - `2024-Unknown-LIEA-BERT A Linguistically Enriched Framework for.md`

## Final Tracking Artifacts
- Final unresolved snapshot:
  - `CEI-Lit-WS/logs/20260214-unresolved-after-wave3-plus-europepmc-plus-wave4.csv`
  - `CEI-Lit-WS/logs/20260214-unresolved-after-wave3-plus-europepmc-plus-wave4-summary.json`
- Final resolved snapshot:
  - `CEI-Lit-WS/logs/20260214-unresolved-now-resolved-after-wave3-plus-europepmc-plus-wave4.csv`
- Final manual queue:
  - `CEI-Lit-WS/logs/20260214-browser-fetch-manual-plan-after-wave3-plus-europepmc-plus-wave4.csv`
  - `CEI-Lit-WS/logs/20260214-browser-fetch-manual-plan-after-wave3-plus-europepmc-plus-wave4.md`
- Final action summary:
  - `CEI-Lit-WS/logs/20260214-unresolved-pdf-action-list-after-wave3-plus-europepmc-plus-wave4.md`
