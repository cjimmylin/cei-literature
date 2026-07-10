# WCF-Bench — Floor Re-run (manifest-driven panel, post settled-core fix)

Canary: `WCFBENCH-CANARY-c1647-x9k4q`  ·  Run: 2026-07-10T13:23:27  ·  manifest: 07-PILOTS/20260710-third-family-screen

DESCRIPTIVE / pre-gate. Confirms the R31 settled-core floor holds after the session-11 settled-core prompt fix, with a JudgePanel that consumes a frozen qualification manifest (R35.4 — no probe re-run at construction).

## Settled-core floor

- **2/3** contested cells credit the settled core (fraction > 0).
- Verdict: CHECK — see rows

| SUT | item | settled_core_fraction |
|---|---|---|
| meta-llama/llama-3.1-8b-instruct | AGG-C3-W302 | 1.0 |
| meta-llama/llama-3.1-8b-instruct | AGG-C5-W304 | 0.5 |
| meta-llama/llama-3.1-8b-instruct | AGG-C8-W305 | 0.0 |

## Cross-family coverage per scored surface (R34.4)

- DISCLOSURE-valid families: ['google', 'x-ai'] (>=2 → cross-judge pair)
- OPEN-award-valid families: ['google'] (<2 → SINGLE-FAMILY (numbers not a measurement))

Active judges + eligibility: gpt4omini=['coherence', 'settled_core']; gemini-flash=['coherence', 'disclosure', 'open_award', 'settled_core']; grok-4.20=['coherence', 'disclosure', 'settled_core']

