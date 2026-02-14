# Manual Browser Queue Execution Summary

Generated: 2026-02-14T07:42:29
Mode: `dry-run`

- Queue rows: **124**
- Unique papers: **84**
- By tier: **{'P2-Medium': 21, 'P3-Hard': 103}**
- Apply rows attempted: **124**
- Status counts: **{'download_failed': 106, 'missing_paper': 4, 'rejected_verification': 14}**

## Top Download Errors
- http_403: 55
- not_pdf_header: 41
- http_202: 8
- curl_return_6: 2

## Top HTTP Codes (failed downloads)
- 403: 55
- 200: 41
- 202: 8
- : 2

## Produced Artifacts
- playbook_md: `logs/20260214-manual-browser-playbook.md`
- p2_actionable_csv: `logs/20260214-manual-browser-p2-actionable.csv`
- p2_actionable_md: `logs/20260214-manual-browser-p2-actionable.md`
- p2_plan_md: `logs/20260214-manual-browser-p2-execution-plan.md`
- p2_blockers_csv: `logs/20260214-manual-browser-p2-blockers.csv`
- stale_map_csv: `logs/20260214-manual-browser-queue-stale-paper-map.csv`
- dryrun_results_csv: `logs/20260214-manual-queue-clean-dryrun-results.csv`
