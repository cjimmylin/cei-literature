# NormEval v2.2-preliminary Revision Protocol

**Created:** 2026-04-13 | **Purpose:** Document the path from v2.2-preliminary to v2.3 (or v3.0) when external model runs land.

---

## Current Status

v2.2-preliminary is labeled "preliminary" because:
- 6 of 9 model results (GPT-5, GPT-5-mini, 4 Gemini) were generated via in-context elicitation, not direct API calls
- All cross-vendor findings (F1-F7) are exploratory hypotheses, not empirical measurements
- The PDF carries a "DRAFT -- NOT FOR CITATION" watermark
- All cross-vendor data is marked with `[simulated -- awaits external validation]` inline flags

## What Triggers the Upgrade to v2.3

The upgrade occurs when **real non-Anthropic API results** land from external model administration. Specifically:

1. T6-T15 administered to GPT-5 and GPT-5-mini via OpenAI API
2. T6-T15 administered to Gemini models via Google API
3. Optional: Gemini T>0 temperature sensitivity probe
4. Optional: IRR via multi-rater panel

## What Gets Rewritten in v2.3

| Section | Change |
|---------|--------|
| Abstract | Remove `[simulated]` flags; update model count if different models tested |
| Methods §3.4 | Replace elicitation methodology with real API administration details |
| Results §4.5-4.6 | Replace all cross-vendor numbers with real API results |
| Discussion §5.3 | Reframe profile analysis with real data (2+1 or 3 profiles, as data dictates) |
| Discussion §5.6 | Gemini identity finding: confirm or retract based on real API results |
| Limitations §6.1 | Remove elicitation disclosure paragraph; add whatever new limitations emerge |
| Conclusion | Reframe Contributions 3-4 and Calls 1, 4, 5 based on real results |
| Appendix K | Add real API prompt templates alongside elicitation prompts |
| Figures 6, 7, 8, S5, S6 | Regenerate from real data; remove `[simulated]` caption flags |
| Dashboard v5 | New version with real data replacing simulated; v4 frozen as historical |
| Zenodo | New deposit version; link v2.2-preliminary as superseded |

## What Stays Unchanged in v2.3

| Section | Why |
|---------|-----|
| Claims C1-C5 | Landscape-level, no model dependency |
| Results §4.1-4.4 | Pure benchmark analysis, no model data |
| Introduction | Framework and motivation unchanged |
| Figures 1-5, S1, S2 | Anthropic-only or landscape data |
| T1-T5 trial results | Direct Anthropic API, empirically grounded |

## Retraction Notice Template

If v2.3 substantially changes the cross-vendor findings:

```
RETRACTION/REVISION NOTICE

NormEval v2.2-preliminary (DOI: [pending]) contained cross-vendor 
results generated via in-context elicitation, as disclosed in the 
abstract, Section 6.1, and inline [simulated] flags throughout. 
These results have been replaced with empirical API-administered 
data in v2.3 (DOI: [new]). Readers should cite v2.3 for any 
cross-vendor claims. The landscape-level claims (C1-C5) and 
Anthropic-only findings (T1-T5) are unchanged between versions.
```

## Zenodo Versioning

- v2.2-preliminary deposit: `status: preliminary`, tagged with embargo notice
- v2.3 deposit: new version of the same Zenodo concept DOI
- v2.2-preliminary automatically marked as "superseded" in Zenodo's version chain

---

*This protocol was written during Session 19 (2026-04-13) per the 12-expert council's META-CRIT #1 (research integrity) recommendation.*
