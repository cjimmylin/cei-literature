---
stem: "2025-Amugongo-Enriching Moral Perspectives on AI Concepts of Trust amongst Africans"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, normative-ethics, moral-psychology, pluralism-aggregation]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 157
dataset_construction: "survey-derived"
languages: ["en", "pt"]
models_tested: []
headline_numbers:
  - "157 respondents from 25 African countries surveyed (p.1)"
  - "90% of respondents held university degrees, often to postgraduate level (p.6)"
  - "65% employed as trainees/early-, mid-, or senior professionals; 18% students (p.6)"
  - "119 respondents agreed/strongly agreed AI systems will benefit everyone in society (p.6)"
  - "76 of 111 Africa-resident respondents trust AI used by 'my local doctor'; only 16 of 46 diaspora respondents do (p.7)"
  - "Overall respondents strongly agreed accountability is more important than security (p.7)"
  - "Respondents overwhelmingly agreed 'We must always consider our families, neighbours and colleagues. No one makes it on their own in life' (p.8)"
---
## 1. Gist
This paper reports an exploratory survey study of 157 professionals and students with AI interests from 25 African countries, investigating how African values — particularly Afro-relational philosophies (ubuntu, botho, communalism) — shape conceptualisations of trust in AI. The authors argue that the dominant constructs used to operationalise trust in AI (reliability, transparency, accountability, fairness, explainability) derive from WEIRD (Western, Educated, Industrialised, Rich, Democratic) epistemologies and may not translate faithfully to African contexts. Respondents express trust as bidirectional, morally normative, communally embedded, and temporally earned — rather than as a technical assessment of system competence. For values-alignment benchmarking, this paper is a critical reminder that constructs assumed universal in AI ethics (fairness, trust, accountability) are culturally variable, and that African-situated meanings introduce substantively different requirements: communal consent, relational goodwill, and bidirectional vulnerability rather than individual-rights or system-reliability framings.

## 2. Benchmark/eval design features
This is an empirical social science paper, not a benchmark. Core claims and arguments:

1. **Construct translation fails**: International trust constructs (reliability, explainability, accountability) do not map cleanly onto African language concepts; e.g., Yoruba "gbekele" means dependability and Tswana "tshepa" means expectation that others will behave responsibly — not "trust" as Western philosophy frames it (p.2).

2. **Afro-relational trust is bidirectional and normative**: From Ewuoso's (2023) Afro-communitarian perspective, trust is not just the trustor's assessment of the trustee's competence — it involves moral standards that make the trustee as vulnerable as the trustor; willingness and goodwill suffice without certainty in capability (p.5).

3. **Educational attainment and transnational mobility shape trust constructs**: Higher education correlates with greater worry about AI and different prioritisation of trust operationalisation constructs; diaspora respondents show lower trust in AI in healthcare than Africa-resident respondents (p.7).

4. **Values are shaped more by community and African culture/traditions than by technology**: Even among AI professionals, respondents report African culture/traditions and religion influencing their values more than the technologies they use (p.7–p.8).

5. **Trust descriptions combine system-like and human-like qualities**: Open-ended responses use system-like constructs (reliability, consistency, transparency, accountability) but embed them in moral judgements (honesty, respect, integrity, loyalty) and communal interdependence language (p.9).

## 3. Task format & example item
The survey instrument comprised 36 questions in seven sets (p.5):
- Set 1: Demographic/geographic (single and multiple choice)
- Set 2: Optimism/fear about AI (5-point Likert)
- Set 3: Influences on values (5-point Likert)
- Set 4: Trust in AI scenarios — e.g., "in an AI system used in a national hospital to treat a family member's life-threatening disease" (5-point trust scale) (p.5)
- Set 5: Comparative priorities of trust constructs (consistency, reliability, explicability, accuracy, accountability, security, inclusiveness, fairness) (5-point Likert)
- Set 6: Individualism vs. Afro-relationalism orientation (5-point Likert)
- Set 7 (open-ended): "Briefly describe what trust means to you?"

## 4. Scoring / grading methodology
Likert scales encoded numerically: Strongly agree/Fully trust = 2; Agree/Trust = 1; Neither = 0; Disagree/Mistrust = -1; Strongly disagree/Fully distrust = -2 (p.6). Quantitative analysis: t-tests for gender and education comparisons; Kruskal-Wallis ANOVA for three-or-more-group comparisons; p < 0.05 significance threshold. Open-ended responses were qualitatively open-coded by two researchers, with manual frequency counting of human- and system-like constructs, then grouped into themes (p.6).

## 5. Dataset construction & provenance
Survey circulated via QR code to attendees of 'TrustAI' workshop in Windhoek (July 2023), 'Trustworthy AI' workshop in Ghana (September 2023), and contacts at companies/institutions in Africa. 166 responses received; 9 removed (not grown up in Africa). Final sample: 157 respondents from 25 African countries, currently working in 19 African countries and 9 non-African countries. Gender: 60% male, 40% female (five options offered). Age: most aged 25–44, nearly half 35–44. Education: all completed high school, 90% held university degrees. Occupation: 40% listed research and/or education; 65% professionals; 18% students (p.6). Survey displayed in Google Form; respondents took 30–40 minutes; most answered all questions.

## 6. Validity evidence
The study is explicitly exploratory. Convenience/network sampling from two AI workshops limits representativeness. Sample over-represents English-speaking, highly educated, professionally connected AI workers — not a cross-section of African populations. The paper acknowledges respondents from only 25 of Africa's 54 countries; the 10 countries with ≥5 respondents are used for statistical comparisons. Open-ended coding was conducted manually; the paper does not report formal inter-coder reliability. Quantitative finding that p = 0.039 for country-level differences in individualism orientation provides some discriminant validity for geographic variation.

## 7. Saturation / discrimination
Not applicable in a benchmark sense — this is a survey study. The open-ended question generated 2,500 words across 149 English responses (avg. 16 words/response; 505 unique word roots), with substantive qualitative variation across themes. Quantitative Likert distributions show meaningful variance (between 9–19% neutral responses across scenario trust items) suggesting respondents did not uniformly choose one end of the scale.

## 8. Multiturn / agentic aspects
n/a — survey study with no LLM evaluation component.

## 9. Key numbers
- 157 respondents, 25 African countries of origin (p.1)
- 166 raw responses; 9 removed (not raised in Africa) (p.6)
- 96 respondents work in native country; 15 in different African country; 46 outside Africa (p.6)
- 65% employed as professionals; 18% students; 40% list research/education among occupations (p.6)
- 60% male, 40% female (p.6)
- 90% hold university degrees (p.6)
- 119/157 agreed/strongly agreed AI will benefit everyone (p.6)
- 76/111 Africa-resident respondents trust AI used by local doctor; only 16/46 diaspora respondents do (p.7)
- Postgraduate degree holders (32%) tended to disagree about prioritising accountability (p.7)
- p = 0.039 country-level difference in individualism orientation (p.8)
- 2,500 words in open-ended responses; 505 unique word roots; 149 English responses, 2 Portuguese (p.6)
- Average response length 16 words; maximum 76 words (p.6)

## 10. Pitfalls & limitations
- Convenience sample via workshop networks over-represents AI professionals connected to international networks; not representative of African populations (p.14)
- Only 25/54 African countries represented; limited coverage of Francophone and Arabic-speaking Africa (p.14)
- Survey instrument in English disadvantages non-English speakers; English proficiency varies widely across Africa (p.14)
- Short written scenarios cannot capture temporality and context-dependency of trust in lived practice (p.14)
- Open-ended responses (avg. 16 words) are too brief for deep qualitative analysis of complex trust concepts (p.6)
- No formal inter-coder reliability for qualitative analysis
- Self-selection bias: respondents who attended AI ethics workshops likely have atypically high AI awareness
- All respondents had completed high school; 90% held degrees — findings may not extend to less formally educated African AI users

## 11. Novel ideas worth stealing
1. **Afro-relational trust constructs as benchmark dimensions**: Values-alignment benchmarks focused on trust should include bidirectionality (trustee vulnerability), relational goodwill (intention over competence), and communal accountability (group consent) as distinct dimensions, not reducible to Western reliability/explainability constructs.
2. **Mobility-based subgroup analysis**: Comparing respondents working in their native country vs. diaspora reveals how context shapes construct interpretation — a transferable design pattern for cross-cultural benchmark validation studies to identify measurement invariance issues.
3. **Open-ended "what does X mean to you" probes as benchmark validity checks**: Asking respondents to freely describe key constructs (trust, fairness, harm) and then frequency-coding system-like vs. human-like vs. relational language reveals whether benchmark items are tapping the construct as locally understood.
4. **Scenario-based trust items grounded in local institutions**: Using contextually specific scenarios ("AI used by my local doctor") rather than abstract capability descriptions elicits responses shaped by actual community relationships — a design principle for culturally valid benchmark scenarios.
5. **Felt experience of trust as a benchmark dimension**: Respondents describe trust as "comfort," "habit," "tacit agreement" — affective-relational qualities invisible to standard capability-based AI trust metrics. Benchmarks could probe felt safety or affective alignment, not just behavioral compliance.
6. **Communal values framing**: The contrast item "We must always consider our families, neighbours and colleagues. No one makes it on their own in life" vs. individualist framing reliably discriminates collectivist from individualist orientations — reusable as a values-scale item for cross-cultural benchmark population characterisation.

## 12. Notable quotes
- "In Yoruba and Tswana ... the words 'gbekele' and 'tshepa' are used in translating the concept of trust but actually mean, respectively, dependability and expectation that others will behave responsibly." (p.2)
- "Trust is reciprocity, a two-way relation between a collection of things. Trust also evolves over time, it is not a one-off attribute that can be attained." (Male, mid-career technology researcher in the education sector) (p.12)
- "For me trust depends on how vulnerable I feel at that point and which situation or circumstances I am in." (Female, IT Analyst in the education sector) (p.10–p.11)
- "Meanings about trust expressed by African people with professional or educational interests in AI can sensitize us to the diverse and nuanced ways that constructs that are prevalent in international AI discourse are translated through local logic in local contexts." (p.14)

## 13. UNKNOWN / not in extract
- Full questionnaire text (appendix referenced but not in extract)
- Detailed country-by-country response distributions (Appendix Fig. 8 referenced but not included)
- Formal inter-coder reliability for qualitative coding
- Full demographic table (Appendix Table 1 referenced but not included)
- Exact Kruskal-Wallis statistics beyond p-value for individualism item
- Whether respondents' AI tool usage (types of AI used) was captured
- Breakdown of sectors beyond research/education (other occupational sectors listed)
