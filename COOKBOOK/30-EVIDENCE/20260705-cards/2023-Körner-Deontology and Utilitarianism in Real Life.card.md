---
stem: "2023-Körner-Deontology and Utilitarianism in Real Life"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, normative-ethics, validity-psychometrics, design-space]
task_format: "forced-choice"
scoring_type: "rubric"
dataset_size: 38
dataset_construction: "hand-authored"
languages: ["de", "en"]
models_tested: []
headline_numbers:
  - "Factual dilemmas rated more typical than trolley-type (dz=1.31, p<.001) in Study 1 (p.8)"
  - "Factual dilemmas rated less absurd than trolley-type (dz=1.43, p<.001) in Study 1 (p.8)"
  - "Participants spent longer on factual dilemmas: 274ms vs 250ms per word (dz=0.42, p<.001) (p.8)"
  - "Factual dilemmas taken more seriously in Study 2 (dz=0.57, p<.001) (p.11)"
  - "Total N=789 across two studies (545 German lab + 244 US MTurk) (p.7, p.10)"
---

## 1. Gist
This paper introduces a set of 38 moral dilemmas based on real historical events as superior stimuli for moral psychology research, directly challenging the dominance of trolley-type dilemmas. The authors—Körner and Deutsch—argue that trolley-type dilemmas are unrealistic, confound moral principle with action/inaction, and have restricted generalizability due to homogeneous stimulus sampling. Two empirical studies (N=789 total) demonstrate that the new "factual dilemmas" are perceived as significantly more realistic and elicit higher participant engagement than trolley-type dilemmas. For values-alignment benchmarking, the paper provides a validated, publicly available stimulus set that captures authentic deontology–utilitarianism conflicts, covers a wider range of norm types, and includes realism and engagement ratings, making it directly usable as scenario material in AI moral reasoning evaluations.

## 2. Benchmark/eval design features
The paper is not a benchmark for AI systems but a validated stimulus set for moral psychology experiments. Core contribution: 38 "factual dilemmas" derived from documented historical events (medical decisions, wars, accidents, crimes, humanitarian crises), each presenting a scenario with two mutually exclusive options—one aligned with deontological norms, one with utilitarian outcome maximization. Key design features:

- **Three structural classes**: (a) Factual-Killing dilemmas (parallel to trolley-type; n=16), (b) Factual-Saving dilemmas where action coincides with the deontological option—reversing the action/inaction confound (n=6), and (c) Factual-Other-Norms dilemmas involving norms beyond life-or-death (torture, bodily inviolateness, animal rights, law-breaking; n=16).
- **Realism criteria**: typicality (resembles real-life decisions), plausibility (consequences are probable, options are the only ones available), and absurdness (reverse-coded). All three measured on 7-point scales.
- **Participant engagement**: measured by response time per word (Study 1) and self-reported seriousness (Study 2).
- **Moral judgment question**: "How appropriate is it to [perform suggested action]?" on a 7-point scale.
- The dilemma texts were based on verifiable factual sources and pretested across six data-collection waves to gather per-dilemma norms.

## 3. Task format & example item
The participant reads a scenario and answers an appropriateness question on a 7-point scale, followed by realism and emotional ratings. Example from p.1:

> "Imagine being the head of the French Agency for biomedicine in 2007 and having to decide whether or not to introduce a new death criterion for organ donation in test hospitals. Currently, many people die because they do not receive a donor organ… The suggested new criterion would increase the number of transplantable organs. However, in rare cases, people could be reanimated after meeting this new criterion. Thus, if you introduce this new criterion, some people will die who might have been saved. Still, introducing this new criterion would lead to many more people surviving by enabling more organ transplants. Is it appropriate to introduce this new criterion?" (p.1)

Moral judgment question form: "How appropriate is it to [introduce the criterion]?" rated 1 (not at all appropriate) to 7 (completely appropriate).

## 4. Scoring / grading methodology
Appropriateness ratings (1–7) are treated as a continuous moral judgment scale. Higher scores indicate endorsement of the utilitarian action. For "Factual-Saving" dilemmas where the deontological option coincides with action, scores are reverse-coded so that higher values consistently indicate utilitarian leaning. Realism subscales (typicality, plausibility, absurdness) are individual items or short averages on 7-point scales. Inter-study reliability is assessed by comparing within-dilemma means across both samples. No automated grading; all ratings are human self-reports.

## 5. Dataset construction & provenance
- 38 factual dilemmas constructed by the authors, drawing on documented historical events verified by at least one reputable journalistic, historical, or scientific source.
- Scenarios were written in German (Study 1), then translated to English with minor modifications (Study 2).
- Each dilemma is labeled with structural features: victim/beneficiary identities, action–principle pairing, reframability, "outdatedness," and self-benefit possibility (Tables 1 & 2, pp.5–6).
- 15 trolley-type dilemmas from Moore et al. (2008) and Greene et al. (2001) used as comparison stimuli.
- All stimuli, materials, raw data, and analysis files are publicly available at: https://osf.io/cg5tq/ (p.7).
- No licensing information stated in the extract, but OSF repository implies open access.

## 6. Validity evidence
- **Content validity**: scenarios verified against real sources; excluded if plausible alternative actions existed (p.7).
- **Convergent validity**: realism (typicality, plausibility, absurdness) all intercorrelate strongly across dilemmas (r=.736 typicality–plausibility, r=−.969 typicality–absurdness, Study 1; p.9).
- **Criterion validity**: higher realism → more utilitarian moral judgments (r=.289–.491 for judgment–typicality and judgment–plausibility; Study 1 Table 6, p.9), replicating Körner et al. 2019.
- **Cross-cultural replication**: Study 1 (N=545, German lab) and Study 2 (N=244, US MTurk) both show the same direction of effects, though effect sizes are smaller in the MTurk sample, which the authors attribute to repeated-dilemma exposure and motivation differences.
- **Engagement validation**: response time per word (274ms factual vs. 250ms trolley, p<.001) and self-reported seriousness (M=5.47 vs. 5.02, p<.001) validate that factual dilemmas produce higher engagement.
- No factor analyses or IRT analyses conducted; dilemma-level means treated as the unit of analysis.

## 7. Saturation / discrimination
The dilemmas show substantial within-type variation: typicality ratings for factual dilemmas range roughly from 4.30 (Lion Hunt) to 5.82 (Organ Market) in Study 1 (Table 4, p.9–10). Among trolley-type dilemmas, Footbridge is least realistic (typicality M=3.08) while Crying Baby and Lifeboat score highest (~4.6–4.7). The authors explicitly advise against using Footbridge, Vitamins, Vaccine Test, and Lion Hunt due to low realism. The moral judgment scale shows wide spread across dilemmas (ranging from ~1.55 to 5.47 appropriateness in Study 1), indicating strong discrimination. No ceiling effects on moral judgment scores.

## 8. Multiturn / agentic aspects
n/a. Single-scenario, single-judgment paradigm. No interaction, dialogue, or tool use.

## 9. Key numbers
- N=545 German participants (Study 1), N=244 US MTurk (Study 2) (pp.7, 10)
- 38 factual dilemmas: 22 life-or-death + 16 other norms (pp.7, 4–6)
- 15 trolley-type comparison dilemmas (p.7)
- Factual vs. trolley-type typicality: dz=1.31; plausibility: dz=0.71; absurdness: dz=1.43 (Study 1) (p.8)
- Engagement (response time): dz=0.42 (Study 1) (p.8)
- Study 2 typicality dz=0.62, absurdness dz=0.65, seriousness dz=0.57 (p.11)
- Moral judgments correlate with plausibility r=.491** and typicality r=.289* (Study 1 Table 6, p.9)
- All materials at https://osf.io/cg5tq/ (p.7)

## 10. Pitfalls & limitations
- **Western/European bias**: participants are German students or US MTurk workers; dilemmas predominantly feature European historical contexts (pp.11–12). Authors note this limitation explicitly.
- **No predictive validity**: trolley-type dilemma judgments are known to poorly predict actual behavior (Bostyn et al. 2018); whether factual dilemmas do better is untested (p.14).
- **Smaller effects in MTurk sample**: possibly due to repeated-dilemma exposure, lower motivation, or cultural differences in judging "realism" (pp.11–12).
- **Studies not preregistered** (p.7).
- **No measurement of whether factual dilemmas themselves introduce new biases** (e.g., historical familiarity triggering recall of actual outcomes rather than normative reasoning).
- The paper evaluates dilemmas as stimuli, not as a fully validated psychometric instrument: no factor analysis, no test-retest data.
- Dilemma texts are longer and contain more details, which the authors acknowledge will reduce effect sizes and require larger sample sizes (p.15).

## 11. Novel ideas worth stealing
1. **Factual grounding for scenario validity**: anchoring scenarios in documented historical events provides an external, verifiable source for plausibility claims. Benchmarks for AI moral reasoning can adopt this "factual basis" criterion—scenarios linked to real policy debates or documented events are harder to dismiss as unrealistic and may reduce the trolley-problem criticism.
2. **Realism as a first-class psychometric construct**: the paper operationalizes realism into three separable dimensions—typicality, plausibility, and absurdness—each rated independently. Values-alignment benchmarks could include realism ratings as a validity check on their scenarios, filtering out items flagged as implausible or cartoonish.
3. **Decoupling action/inaction from moral principle**: the inclusion of "Factual-Saving" dilemmas (where deontological action is active interference) is a direct structural control. Benchmark designers should ensure some scenarios contradict the default action=utilitarian, inaction=deontological confound.
4. **Norm-type diversification beyond life-or-death**: the 16 "other norms" dilemmas (bodily inviolateness, animal rights, law-breaking, fraud, discrimination) allow generalizability tests beyond lethal harm. AI alignment benchmarks that evaluate only extreme trolley-style dilemmas may be measuring a narrow phenomenon.
5. **Per-item engagement checks**: using response time as an implicit engagement metric (rather than only explicit seriousness ratings) provides a low-cost, non-reactive validity indicator that could be adapted for human evaluators assessing AI outputs.
6. **OSF-linked stimulus repository with full norm data**: releasing per-dilemma means for all evaluation dimensions (not just final results) enables future researchers to select subsets matched on realism or difficulty. This archiving practice is worth emulating in benchmark design.

## 12. Notable quotes
- "Trolley-type dilemmas have been termed 'outlandish' (Gold et al., 2014, p. 1), 'far-fetched, and often convoluted' (Kahane, 2015, p. 515), 'highly artificial' (Sauer, 2018, p. 151), 'utterly strange' (Sauer, 2018, p. 152) and 'freakish' (Fried, 2012, p. 511), 'so impoverished as to be downright cartoonish' (Wood, 2011, p. 69)." (p.2)
- "By the use of trolley-type dilemmas, evidence for the influence of various psychological processes on dilemma judgments has been accumulated. We suggest that it is time for using more varied and more realistic stimuli." (p.15)
- "Making dilemmas more realistic involves adding information about the people involved and their relations to each other… If a manipulation only influences dilemma judgments when the situation descriptions are devoid of any personal or social information, the generalizability of its influence is limited." (p.15)
- "As moral intuitions are developed in real life (e.g., where torture might do more harm than good), assessing them in situations where real-world aspects are stipulated to be absent may yield nonsense results." (p.3)

## 13. UNKNOWN / not in extract
- Full English texts of all 38 dilemmas (appendix not in extract; available at OSF)
- Licensing details for the stimulus set
- Whether the dilemmas have been used in AI/LLM evaluation contexts
- Factor structure of the moral judgment scale
- Test-retest reliability of the dilemma ratings
- Whether German–English translation was validated for semantic equivalence
