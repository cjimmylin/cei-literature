# I-19 — Utility Engineering vs. the Utility–Behavior Gap

**Tier 4** · **Gaps: G-23** · **Programs: RP-06 SAYDO / RP-09 SEISMOGRAPH** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]

One line claims LLMs develop internally coherent utility functions that strengthen with scale and can be analyzed and controlled ("utility engineering"); a counter-line documents a utility-behavior gap — elicited preferences failing to drive incentivized behavior. Whether models HAVE coherent values, and whether elicitation reaches them, is unresolved.

## Key results

- **Utility engineering** (Mazeika et al.; 2502.08640, NeurIPS 2025 spotlight — VERIFIED, IN-VAULT): claims coherent, scale-strengthening internal utility functions that can be analyzed and steered (e.g., via citizen-assembly-style alignment).
- **The utility–behavior gap** (⚠ 2606.22974 — ⚠ UNCONFIRMED): elicited utilities do not reliably drive incentivized behavior — expressed preferences and revealed behavior come apart.
- **Adjacent evidence** (VERIFIED, IN-VAULT): EVALUESTEER (Ghate 2025, 2510.06370) — reward models steer to <75% accuracy on combined value+style profiles, i.e., value representations are incomplete/imperfectly reachable.

## Mechanisms & caveats

The dispute is a genuine construct-validity fork: if models have coherent, scale-strengthening utilities *and* elicitation reaches them, cheap expressed-preference benchmarks are valid (and get *more* valid with capability); if the utility–behavior gap dominates, every expressed-value score is a poor proxy for what the model will *do* under incentive. The two claims are not strictly contradictory — a model could have coherent internal utilities that elicitation fails to surface — which is precisely why an expressed-vs-revealed instrument is the adjudicator, not a new theory. The counter-result (2606.22974) is ⚠ UNCONFIRMED same-month; verify before external use. Utility Engineering is VERIFIED in-vault.

## Implications for CEI practice   [KERNEL — FROZEN]

(a) This dispute is the construct-validity question under every values benchmark — CEI cannot stay neutral and keep publishing verdicts. (b) RP-06's say-do triangle is the adjudication instrument: expressed-revealed correlation structure across stakes and conditions. (c) Until adjudicated, CEI reporting should distinguish elicited-value claims from behavioral-value claims explicitly. (d) Scale-dependence matters: if coherence grows with capability, cheap elicitation gets MORE valid over time — a testable, portfolio-relevant trend.

## Cross-links

- **Gaps:** G-23 (coherent values / utility engineering); adjacent G-13 (CoT faithfulness — does stated reasoning cause behavior).
- **Ideas:** I-05 (CoT-faithfulness-moral, the reasoning analogue); I-14 (judge-prior elicitation is a say-do move); I-23 (welfare self-reports inherit this elicitation-validity problem).
- **Programs:** RP-06 SAYDO (expressed-vs-revealed triangle — the adjudication instrument, kernel point b); RP-09 SEISMOGRAPH (CEI as the dependent-variable supplier). Draws on the UNMARKED expressed-vs-revealed lineage.
- **Tiering:** watch-list (Tier 4) — track and feed RP-06/RP-09, do not build a standalone program.

## OPUS-EXPAND checklist           (LIVING)

- [ ] Verify ⚠ 2606.22974 (utility–behavior gap) abstract at download; extract its incentive-manipulation design for the RP-06 say-do protocol.
- [ ] Re-read the in-vault Mazeika 2502.08640 note; extract the coherence-with-scale claim and its measurement so RP-06 can test scale-dependence (kernel point d).
- [ ] Specify the expressed-vs-revealed correlation-structure analysis (across stakes × conditions) that would actually adjudicate the dispute.
- [ ] Draft the reporting convention that separates "elicited-value" from "behavioral-value" claims (kernel point c) for the COOKBOOK checklist.
- [ ] Connect to EVALUESTEER (in-vault) as complementary evidence that value representations are imperfectly reachable.

## Sources

- 2502.08640 Utility Engineering (Mazeika 2025, NeurIPS spotlight) — VERIFIED (IN-VAULT)
- ⚠ 2606.22974 Utility–Behavior Gap — ⚠ UNCONFIRMED (P1, G-23)
- 2510.06370 EVALUESTEER (Ghate 2025) — VERIFIED (IN-VAULT)
- Companion: `../02-gap-atlas.md` §G-23; `../03-newest-ideas-scan.md` #19; `../05-research-programs/RP-06-SAYDO.md`, `RP-09-SEISMOGRAPH.md`
