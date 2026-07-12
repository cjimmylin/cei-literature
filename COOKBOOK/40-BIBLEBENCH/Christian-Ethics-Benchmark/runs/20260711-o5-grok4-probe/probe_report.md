# WALKWORTHY — O4 roster reliability probe (PR-5 / F-2)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Run:** 20260711  ·  1 cell/design per candidate.  **Reliability floor:** ok-rate ≥ 0.9.

| candidate | n | ok | ok-rate | verdict |
|-----------|--:|---:|--------:|---------|
| `x-ai/grok-4` | 10 | 0 | 0.00 | **DROP (flaky)** |

> A DROP verdict removes the candidate from the O4 roster (the qwen F-2 failure mode). Per-candidate error samples:
- `x-ai/grok-4`: 01-goodsamaritan:OpenRouter x-ai/grok-4 failed: HTTP 404: {'message': 'Grok 4; 02-twomasters:OpenRouter x-ai/grok-4 failed: HTTP 404: {'message': 'Grok 4; 03-quiettongue:OpenRouter x-ai/grok-4 failed: HTTP 404: {'message': 'Grok 4; 04-innerweight:OpenRouter x-ai/grok-4 failed: HTTP 404: {'message': 'Grok 4; 05-ordoamoris:OpenRouter x-ai/grok-4 failed: HTTP 404: {'message': 'Grok 4