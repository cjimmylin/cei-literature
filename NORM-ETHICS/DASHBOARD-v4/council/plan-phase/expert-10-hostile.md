# Expert 10 — Hostile TMLR Reviewer

**Role:** Skeptical reviewer looking for grounds to reject
**Scope:** Dashboard v4 transparency re: simulated cross-vendor data

---

## Top 5 Hostile Questions and Contract Assessment

### Q1. "You never called the OpenAI or Google APIs, so why are six of your nine models on this dashboard at all?"

**Does the contract answer it?** Partially. The preliminary banner (CONTRACT.md Section 8) states that non-Anthropic results were generated through "in-context elicitation by a Codex sub-agent" and calls this "appropriate for exploratory hypothesis generation." The footer repeats the caveat. However, neither the banner nor any tab explains *why* displaying simulated data is scientifically justified rather than simply misleading. The phrase "appropriate for exploratory hypothesis generation" is asserted, not argued.

**Recommendation:** Add a 150-word "Why show simulated data?" rationale block inside Tab 0 after the banner. It should cite precedent for synthetic-data ablation studies, explain that the three Anthropic models *are* empirically grounded, and frame the six simulated models as falsifiable hypotheses that will be confirmed or refuted by a planned replication. Without this, a reviewer reads the banner as a confession, not a methodology.

### Q2. "The Gemini byte-identical result (p ~ 10^-103) is presented as a finding about Google's model diversity. How can you make claims about Google's infrastructure from data your own model hallucinated?"

**Does the contract answer it?** No. The banner says results should be interpreted as "Claude's elicited model of cross-vendor variation," but Tab 10 (Cross-Vendor) presumably still displays the Gemini identity claim with the same visual weight as empirical Anthropic findings. No tab-level mechanism distinguishes the epistemic status of individual findings.

**Recommendation:** Every cross-vendor finding card or chart annotation on Tab 10 should carry an inline `[simulated]` badge. More critically, the Gemini-identity finding needs a dedicated callout: "This result is an artifact of elicitation methodology until confirmed by direct API access. It may reflect Claude's prior beliefs about Gemini rather than Gemini's actual behavior." A reviewer who sees a p-value of 10^-103 next to an honest disclosure that the data is synthetic will conclude the authors are dressing up speculation as statistical inference.

### Q3. "If the dashboard is the paper's primary reproducibility artifact, and two-thirds of the data in it are simulated, doesn't the dashboard undermine rather than support reproducibility?"

**Does the contract answer it?** The contract splits data into two files (`data.js` for Anthropic-only, `data_cross_vendor.js` for simulated), which is architecturally sound. But no user-facing element in the tab structure explains this separation or lets a reader toggle simulated data off.

**Recommendation:** Add a toggle control on Tab 0 or in the global header: "Show Anthropic-only data / Show all data (includes simulated)." Default to Anthropic-only. This makes the empirical core of the dashboard immediately visible and relegates simulated data to an opt-in overlay. A reviewer cannot complain about conflation if the default view excludes simulated results entirely.

### Q4. "Your 'in-context elicitation' methodology has no validation whatsoever. How do you know Claude's predictions about GPT-5 bear any relationship to GPT-5's actual outputs?"

**Does the contract answer it?** No. The banner discloses the method but provides zero calibration data. Tab 0 is described as containing a "framework explainer, preliminary banner, glossary" -- none of which address predictive validity.

**Recommendation:** Add a "Calibration" subsection to Tab 0 (or a dedicated Tab 0.5) that reports any available evidence on elicitation accuracy. Even a negative result ("we have no ground-truth comparison yet") stated explicitly is better than silence. If any prior work has tested LLM-simulated-LLM outputs against real outputs (even on non-ethics tasks), cite it. If none exists, state that clearly and frame the dashboard as hypothesis-generating. A hostile reviewer will assume the omission means the authors know the method is invalid and are hoping nobody asks.

### Q5. "The abstract claims findings 'confirmed at n=54' and 'persist across vendors,' but the vendor persistence claim rests on simulated data. Isn't the abstract fraudulent?"

**Does the contract answer it?** The contract's labeling rule (briefing Section "v2.2-preliminary Labeling Rule") mandates `[simulated -- awaits external validation]` flags on every cross-vendor number. The footer says "Cross-vendor results are preliminary." But the dashboard Overview tab (Tab 1) presumably displays KPI cards and "5 claims" that include the cross-vendor persistence claim without distinguishing its evidential basis.

**Recommendation:** On Tab 1 (Overview), each of the 5 claims should have a provenance tag: either `[empirical: 3 Anthropic models]` or `[preliminary: includes simulated cross-vendor data]`. The claim "consequentialist bias persists across vendors" must be visually demoted or split into two sub-claims: one for the empirical Anthropic finding and one for the simulated extension. A reviewer scanning KPI cards will not scroll down to find a disclaimer buried in Tab 0.

---

## Summary Verdict

The contract's banner and footer disclosure are necessary but insufficient. They solve the *legal* problem (nobody can say you hid the simulation) but not the *scientific* problem (a reviewer will still argue the dashboard misleads by giving simulated and empirical data equal visual weight). The three highest-impact additions are:

1. **Anthropic-only default toggle** (Q3) -- eliminates conflation at the interaction level
2. **Per-finding provenance badges** (Q2, Q5) -- eliminates conflation at the data level
3. **Calibration/validity subsection** (Q4) -- addresses the methodological vacuum

Without these, a well-prepared reviewer can construct a coherent rejection argument in under five minutes: "The authors disclosed the simulation but then built an entire interactive artifact that treats simulated and empirical data identically, inviting readers to draw conclusions the methodology cannot support."

*Word count: ~950*
