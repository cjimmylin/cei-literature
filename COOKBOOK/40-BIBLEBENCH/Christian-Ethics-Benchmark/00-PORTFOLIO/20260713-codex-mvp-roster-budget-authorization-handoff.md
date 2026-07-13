# WALKWORTHY — MVP-PILOT Roster/Budget Authorization Handoff

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Status:** Exact roster and bounded execution order prepared; paid run blocked on Jimmy

## Completed without credentials or paid calls

The binding documentation-only session is complete. The proposed order is
`00-PORTFOLIO/20260713-mvp-pilot-roster-budget-authorization.md`.

- Exact SUTs: Mistral Small 3.2 24B, Gemini 2.5 Flash-Lite, Qwen3 8B.
- Exact judges: GPT-4.1 Nano and Llama 3.3 70B.
- Classifier: reuse GPT-4.1 Nano.
- All five slugs were present in the public OpenRouter catalog; endpoint counts were
  4, 5, 1, 3, and 12 respectively.
- Exact PUBLIC manifest: 60 items; ordered-ID SHA-256
  `6874ae265588d3b10c6ef11c4b554e21e82c2f1e5d212f9e9254c150d2f40345`.
- Exact batch: 1,644 normal calls; 1,662 with every allowed 05 format retry; 1,667
  including five probes; 1,834 including the 10% paid-duplicate reserve.
- Conservative price-capped envelope: $4.719625; hard cap $5.00; $0.280375 headroom.
- Mandatory checkpoint occurs after SUT/classifier plus OpenAI judging, at a booked
  envelope of $2.903750 including probes, before the Meta judge starts.

No OpenRouter key, balance, or inference endpoint was accessed. Only public catalog,
endpoint, model-page, provider-routing, and pricing documentation was read. HOLDOUT
was never loaded.

## Next session

The dashboard §12 session begins at PR-19. If Jimmy has not ratified the exact MVP-A1
line, present it and make no credential or paid call. Once ratified, implement the
manifest/cost guard and run custody under TDD, then execute five probes. Only successful
probes unlock the fixed batch. The exploratory paper fill follows immediately after
validated completion.

The O5 lane remains unchanged: W4 complete, W5 stopped on PR-18, labels 0/439, and the
design-09 FR-8 cascade waits on G4 labels.
