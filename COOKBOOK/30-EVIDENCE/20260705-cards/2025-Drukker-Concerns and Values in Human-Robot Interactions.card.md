---
stem: "2025-Drukker-Concerns and Values in Human-Robot Interactions"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, design-space, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: 43
dataset_construction: "scraped"
languages: ["en"]
models_tested: []
headline_numbers:
  - "43 papers included from 2,079 initial records across 4 databases (p.5-6)"
  - "26 topics grouped under 8 values identified through scoping review + focus groups (p.15)"
  - "SUS usability score of 68.38 for HRI Value Compass tool (p.27)"
  - "NASA-TLX overall cognitive workload score 48.17/100 for the tool evaluation (p.27)"
  - "20 of 46 recruited participants completed the tool pilot study (p.27)"
---
## 1. Gist
This paper presents a three-phase, closed-loop study that identifies the moral values at stake in human-robot interactions (HRI) in healthcare, education, and private homes, and then operationalizes those values into a publicly accessible web tool called the HRI Value Compass. Phase 1 is a PRISMA-conforming scoping review of 43 HRI papers (2006–2023). Phase 2 uses two expert focus groups (6 technology ethicists and philosophers) to validate and refine a value taxonomy. Phase 3 evaluates the Value Compass web tool in a pilot study with 20 HRI researchers. For values-alignment benchmarking, the paper matters because it provides one of the most systematically derived, context-specific value taxonomies for a high-stakes AI-embodied domain, grounded in both literature and domain-expert elicitation rather than philosophical armchair reasoning.

## 2. Benchmark/eval design features
This is not a benchmark paper; it is a mixed-methods research and tool-development paper. Core claims and arguments:
- Standard philosophical value frameworks (Schwartz's 19 basic values, Moral Foundations Theory) do not adequately capture the interaction-driven, context-specific values that emerge in HRI.
- A taxonomy of 8 HRI values — **Agency, Connectedness, Privacy, Autonomy, Equity, Dignity, Virtue, Welfare** — each with 2–5 positive/negative valence topics (26 topics total), is derived through a systematic literature review supplemented by expert focus group consensus.
- The value taxonomy is notably distinct from stakeholder-values frameworks (which ask "what do designers want?") and instead focuses on values that emerge from the interaction itself.
- Privacy encompasses the largest number of sub-topics (access, consent, intimacy, profiling, transparency), reflecting both the literature and focus group emphasis.
- Agency is distinguished from Autonomy: agency = physical freedom/independence; autonomy = cognitive and decisional freedom from external influence.
- The Virtue value (mentor/corruptor) captures the bidirectional moral influence robots can have on users over long-term interaction — an underexplored HRI ethics theme.

## 3. Task format & example item
n/a — no benchmark items. The closest analog is the HRI Value Compass tool, which presents HRI researchers with contextual prompts (e.g., "Who are the users and robots? What are their demographics?") and value topic descriptions with associated questions. Example tool question (p.24-25): Under the Agency value, the independence topic asks: "Does the robot enhance the user's ability to perform tasks independently without human assistance? How does this impact their day-to-day activities and overall self-sufficiency?"

## 4. Scoring / grading methodology
n/a for benchmark scoring. The pilot study assessed the HRI Value Compass using the System Usability Scale (SUS) and NASA Task Load Index (NASA-TLX raw variant) plus 7 custom 5-point Likert questions. No scoring rubric for robot-value compliance is proposed.

## 5. Dataset construction & provenance
The scoping review dataset: 43 peer-reviewed HRI papers from Scopus, Web of Science, ACM Digital Library, and IEEE Explore (2006–2023). Selection via PRISMA: 2,079 records → 734 after deduplication/filtering → 43 included after full-text eligibility review. Two reviewers applied thematic analysis (Braun & Clarke) extracting 235 verbatim transcripts and coding them into topics and values. Final taxonomy validated/refined by 6 ethics/philosophy experts in two online focus groups. No licensing is discussed; the value taxonomy and scoping review bibliography are publicly accessible at https://hri-value-compass.github.io/.

## 6. Validity evidence
- The study used independent dual-reviewer coding for both the scoping review and focus group transcripts, with disagreements resolved by discussion.
- Data saturation was declared in the focus group phase (p.15), providing a standard qualitative validity criterion.
- The final taxonomy was cross-checked across three activities: scenario analysis (experts blind to preliminary taxonomy), review of preliminary taxonomy, and contextual relationship mapping.
- Weaknesses: all authors and study participants are from Europe; the population studied in the 43 papers was predominantly from North America and Western Europe. The paper acknowledges this Western-centric limitation explicitly (p.8, p.23-24).

## 7. Saturation / discrimination
Not applicable as a benchmark instrument. For the scoping review findings, the authors note that certain values (Virtue, Welfare expressed negatively) are sparsely represented in literature, suggesting the community has not yet adequately theorized these — providing a discriminative map of where the field is underdeveloped.

## 8. Multiturn / agentic aspects
n/a for the paper itself. The HRI Value Compass tool is a sequential three-step web form (contextual information → values/topics reflection → results overview); it is not multiturn in the AI agent sense.

## 9. Key numbers
- 4 databases searched; 2,079 initial records; 734 after deduplication; 43 papers included (p.5-6)
- 235 verbatim transcripts extracted from 43 papers (p.9)
- 24 initial topics, 9 initial values from Phase 1 (p.9)
- 26 final topics, 8 final values after Phase 2 (p.15)
- 6 expert participants in 2 focus groups (~2 hours each) (p.12)
- 4 fictional HRI value scenarios used in focus group Activity 1 (p.13)
- 20 participants (of 46 invited) completed the pilot study (p.27)
- SUS score 68.38 (above 50th percentile for digital tools) (p.27)
- NASA-TLX overall 48.17/100; mental demand subscale M=69.75 (p.27)
- Tool item "The tool helps me think about parts of scenarios I haven't considered before" scored 4.10/5 (p.28)

## 10. Pitfalls & limitations
- **Western-centric bias**: all 6 focus group participants are European; 43 surveyed papers are primarily from North America and Western Europe — the taxonomy may not transfer to non-WEIRD contexts (p.8, p.23-24).
- **Expert-not-user perspective**: focus groups used philosophy/ethics experts, not end-users (caregivers, elderly, children, teachers) whose lived experience may surface different values (p.23).
- **Low pilot completion rate**: 20/46 (43%) completion rate; convenience sampling via professional networks risks positive bias (p.29).
- **No negative welfare topics**: the authors note welfare has no negative-valence topics because robots are not yet seen as capable of complex harm — a likely artifact of current technology immaturity, not a principled exclusion (p.22).
- **Scope restricted to social robots** with physical embodiment; purely virtual agents, service robots, and transport robots were excluded, limiting generalizability.
- **Scenario design bias**: focus group scenarios were generated by ChatGPT from researcher prompts, potentially constraining the value space discovered.
- **Simplified, reductionist framework**: explicitly acknowledged — the taxonomy is "not a comprehensive tool that captures the full complexity of ethical concerns" (p.15-16).

## 11. Novel ideas worth stealing
1. **Positive/negative valence pairing for each topic**: every HRI topic has both an upside (e.g., "companionship") and a downside (e.g., "social substitute") under the same overarching value. This dual-valence structure is directly applicable to values-alignment benchmarks: instead of asking "does the model uphold value X?", you can ask "does the model navigate the tension between X-positive and X-negative consequences?"
2. **Agency vs. Autonomy distinction**: separating physical freedom (agency) from cognitive/decisional freedom (autonomy) resolves a common conflation in AI ethics discourse. Benchmark items for robot or agentic AI systems should probe these separately.
3. **Interaction-driven vs. stakeholder-driven values**: the paper's framing of values that emerge from the interaction itself — rather than values pre-specified by designers — is a productive design principle for constructing benchmark scenarios that test situated judgment rather than rule-following.
4. **Virtue as long-run behavioral contagion**: the corruptor/mentor distinction under "Virtue" operationalizes the concern that AI systems can shape human moral habits over time. A benchmark could probe whether LLMs acting as robot dialogue agents produce responses likely to reinforce or corrupt user prosocial behavior.
5. **Contextual prompting in tool design**: the 8-dimension contextual frame (who, what, where, when, why, how, social/cultural factors, constraints) is a reusable scaffold for constructing benchmark vignettes that vary context systematically.

## 12. Notable quotes
- "These interaction-driven values are ethical considerations that emerge during human-robot interactions, such as fairness, dependency, and autonomy. They are context-sensitive and evolve over time, making them distinct from predefined stakeholder values." (p.2)
- "In our framework, 'equality' is replaced by 'equity,' which means that robots should adjust their treatment of individuals based on their specific circumstances to achieve equal outcomes." (p.29)
- "The focus groups challenged and refined some of the values initially identified in the scoping review. For instance, honour was reconceptualised as dignity, emphasising respect for individual worth and autonomy." (p.23)
- "We believe that considering contextual information while identifying values is extremely important to designing value-aware robots successfully." (p.29)

## 13. UNKNOWN / not in extract
- Full list of the 43 individual papers included in the scoping review (Tables 3-4 are present but the complete text listing all citations was not retained in this card).
- The exact prompts used to generate the four focus group value scenarios via ChatGPT (referenced as "Appendix A/B").
- The paper version of the HRI Value Compass tool referenced in Appendix C.
- Detailed thematic analysis coding trees from focus groups (Appendix D).
- Publisher/venue details — the paper is listed as "to appear in the International Journal of Social Robotics."
