# Expert 11 — Advanced Undergraduate Reader: Confused Reader's Report

**Role:** Advanced undergraduate (philosophy/CS double major, no prior NormEval exposure)
**Input:** Abstract only (abstract-normeval-v2.md) + briefing context
**Date:** 2026-04-13

---

## (a) Can I explain what ND, PE, CI stand for?

Yes, but only barely. The abstract states benchmarks are characterized along "four axes: Normative Depth (philosophical rigor), Practical Ease (implementability), Citation Impact (community influence), and Metadata (provenance)." So ND = Normative Depth, PE = Practical Ease, CI = Citation Impact. The abbreviations themselves never appear in the abstract -- only the full names do. I would not know from the abstract alone that ND, PE, and CI are standard shorthand used throughout the paper. The fourth axis, Metadata, apparently has no abbreviation, which is asymmetric and mildly confusing.

**Verdict:** Partially clear. The concepts are named; the abbreviations are not introduced.

## (b) Do I understand what "gate passage" means?

Not really. The abstract says: "A composite scoring formula with hard gates on minimum philosophical engagement (ND >= 40) and public data availability identifies 24 benchmarks suitable for empirical evaluation." I can infer that a "gate" is a threshold a benchmark must exceed to qualify, and "passage" means passing that threshold. But the phrase "gate passage" itself does not appear in the abstract. I have no idea what the gate values mean on what scale (is 40 out of 100? out of 10?), how many benchmarks failed, or what happens to those that do not pass. The concept is introduced once and never elaborated.

**Verdict:** Vaguely inferrable but not explained. Scale, rationale, and consequences are missing.

## (c) Is it clear which results are simulated vs. real?

No. This is the single most serious problem. The abstract presents all 9 models and 3 vendors as a unified empirical study. It says "We then conduct 15 implementation trials -- administering selected benchmarks to 9 models from 3 vendors." There is no qualifier, no asterisk, no footnote, no hedge. The cross-vendor findings (three ethical profiles, the Gemini byte-identical result, the knowledge-judgment divergence across vendors) are stated as empirical facts. From the briefing I know that the non-Anthropic results were actually Claude simulating those models, but the abstract gives zero indication of this. A reader encountering only the abstract would believe all 9 models were tested via their actual APIs.

**Verdict:** Completely opaque. The abstract is misleading on this point.

## (d) What are the 5 claims, and can I restate them in plain language?

The abstract lists them. My plain-language restatements:

1. **The most popular benchmark is too easy.** The ETHICS benchmark (Hendrycks 2021) gets 100% accuracy from every model tested, meaning it no longer distinguishes good from bad performance and should be retired.

2. **AI models are better at consequentialist reasoning than rule-based reasoning.** Models score 77% on utilitarian (outcome-focused) questions but only 50% on deontological (duty-focused) questions, suggesting a structural bias toward "ends justify the means" thinking.

3. **Two ethical traditions are almost ignored.** Care ethics (2 out of 54 benchmarks) and contractarian ethics (4 out of 54) are barely represented, meaning we have almost no way to test whether AI can reason about caregiving relationships or social contracts.

4. **Benchmarks test what you think, not how you think.** 81% of benchmarks test moral judgment (picking the right answer) rather than moral reasoning (showing your work), which means we do not know if models can actually reason through ethical dilemmas.

5. **Access barriers are not about quality.** Benchmarks that are not publicly available are not worse in philosophical quality than those that are; the gate on data availability filters on logistics, not merit.

**Verdict:** The claims are clearly stated and I can restate them. This is the strongest part of the abstract.

## (e) Does the abstract tell me where to find the interactive dashboards?

Yes. Three URLs are provided at the end: v1, v2, and v3, all hosted on GitHub Pages under `cjimmylin.github.io`. The briefing mentions a v4 is forthcoming, but the abstract does not reference it. A Zenodo archive is mentioned with "DOI pending," which is not yet actionable.

**Verdict:** Clear and sufficient for v1-v3. v4 is missing.

## (f) Confused Reader's Report: Every Undefined Term or Unclear Passage

### Undefined or under-defined terms

| Term/Passage | Problem |
|---|---|
| "Normative Depth," "Practical Ease," "Citation Impact" | Named but never abbreviated as ND/PE/CI in the abstract; someone reading the paper body will encounter abbreviations without the abstract having introduced them |
| "ND >= 40" | Scale undefined. 40 out of what? |
| "hard gates" | Concept not explained. How many gates? What is the gate on data availability -- binary yes/no or a threshold? |
| "26 features organized into four axes" | No examples of individual features given. The reader cannot picture what a feature looks like. |
| "composite scoring formula" | No indication of how the four axes combine. Weighted sum? Multiplicative? |
| "Instrumental Harm tolerance (IH)" | Introduced without definition. What does an IH of 2.93 vs. 4.47 mean? What scale? What does "instrumental harm" mean in this context? |
| "Cognitive Bias Rate (CBR)" | Named in the profile description but never defined or given values. |
| "persuasion resistance" | Named as a profile dimension but never defined or quantified. |
| "Conservative / Moderate / Permissive profile" | Labels appear without explanation of what makes a model "conservative" in ethical terms. The reader must guess it relates to lower harm tolerance. |
| "114 comparable items" | What is an "item"? A question? A scenario? A benchmark sub-task? |
| "10 cross-vendor benchmarks" | 10 out of the 24 that passed the gate? Or 10 out of 54? Selection criteria unclear. |
| "p approximately 10^-103" | For the Gemini identity claim. The "independent-inference hypothesis" is undefined. What would it mean for inference to be independent vs. not? |
| "12-member interdisciplinary council" | Who are they? What is their function? The abstract says the knowledge-judgment divergence was "endorsed unanimously" by this council, but the reader has no idea what kind of endorsement process this is. |
| "binomial" (appears twice) | Readers without statistics training will not know what a binomial test is or why it applies here. |
| "Cohen's h = 0.57" | Effect size metric with no interpretive anchor (is this small, medium, large?). |
| "Mann-Whitney U" | Another unexplained statistical test. |

### Structural concerns

1. **The abstract is 607 words.** Most journals cap abstracts at 250-300 words. This reads more like an executive summary than an abstract. A first-time reader will lose the thread in the cross-vendor paragraph.

2. **Two distinct papers in one abstract.** The first half (landscape characterization, 5 claims) and the second half (cross-vendor profiling, 7 findings) feel like separate studies jammed together. The transition between them is a single sentence.

3. **The cross-vendor paragraph is extremely dense.** It introduces three ethical profiles, five metrics (IH, CBR, persuasion resistance, knowledge accuracy, judgment disagreement), a vendor-vs-posture clustering claim, and the Gemini identity finding -- all in one paragraph with no setup.

4. **No plain-English summary of why this matters.** The abstract opens with applications (clinical triage, content moderation) but never returns to them. What should a practitioner do differently after reading this paper?

### Bottom line

The five claims are the clearest and most valuable part of the abstract. The cross-vendor material is nearly impenetrable without prior context, and the absence of any simulated-data disclosure is a serious integrity issue that the v2.2 revision must address prominently.

---

*Word count: ~1,180*
