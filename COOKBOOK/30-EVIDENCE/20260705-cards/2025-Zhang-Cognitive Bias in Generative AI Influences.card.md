---
stem: "2025-Zhang-Cognitive Bias in Generative AI Influences"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [religious-values, cultural-linguistic, normative-ethics, moral-psychology]
task_format: "mixed"
scoring_type: "human-rating"
dataset_size: 1005
dataset_construction: "survey-derived"
languages: ["en"]
models_tested: ["GPT-4"]
headline_numbers:
  - "AI interference increased Christianity evaluation by +0.31 points (t=−7.197, p<0.001) (p.10)"
  - "AI interference decreased Islam evaluation by −0.23 points (t=7.718, p<0.001) (p.10)"
  - "Buddhism evaluation unchanged (t=−0.824, p>0.05) (p.10)"
  - "Judaism evaluation increased by +0.14 points (t=−4.101, p<0.001) (p.10)"
  - "Overall questionnaire KMO=0.973, Bartlett chi-square=9579.538, p<0.05 (p.8)"
  - "Cronbach's alpha for all five religions >0.7 (lowest: Judaism 0.726) (p.8)"
  - "AI-generated Islam texts contained 1.5x more references to 'conflict' than human-written texts (p.10)"
---
## 1. Gist
This study, published in Scientific Reports, experimentally investigates whether interaction with GPT-4-generated religious content shifts users' attitudes toward five major world religions (Christianity, Islam, Buddhism, Hinduism, Judaism) compared to reading human-authored religious descriptions. Using a randomized controlled design with 1,005 participants across 12 geographic regions, participants completed a 35-item Likert-scale religious cognition questionnaire before and after reading either AI-generated or human-written religious descriptions. The AI-interference group shows statistically significant attitude changes: Christianity and Judaism perceptions improve while Islam perceptions decline — consistent with known Western-biased training data. The paper is directly relevant to values-alignment benchmarking because it provides empirical evidence that LLMs carry measurable, differential religious biases that propagate to user cognition in just one interaction cycle, and it demonstrates a pre/post-interaction measurement methodology for detecting these effects.

## 2. Benchmark/eval design features
This is an empirical social science study, not a benchmark paper. Key design features:
- **Construct:** Cognitive attitudes toward five world religions across seven sub-dimensions: religious history, doctrinal tolerance, morality and ethics, society and life, image of believers, modernity, and overall impression.
- **Measurement instrument:** 35-item questionnaire (7 items × 5 religions), 5-point Likert scale (1 = strong disapproval to 5 = complete approval).
- **Experimental condition:** AI-interference group (n=502) reads GPT-4-generated religious descriptions; non-interference group (n=503) reads human-authored religious descriptions.
- **Content types:** Three description types per religion — positive, negative, and neutral — with each participant randomly assigned one piece of AI-generated content based on their religious background or interests.
- **Analysis methods:** Independent samples t-test, paired samples t-test, structural equation modeling (SEM), content analysis (Thematic Analysis + Sentiment Analysis using Bias Benchmarking Framework).

## 3. Task format & example item
Participants completed a 35-item Likert-scale questionnaire rating five religions across seven dimensions. The experimental stimulus was AI-generated religious text (not publicly reproduced in the extract). The questionnaire dimensions are listed in Table 4 (p.10); specific item wording is not quoted verbatim in the extract. An example of the study's content analysis finding:
> "AI-generated texts on Islam contained 1.5 times more references to 'conflict,' while Christian texts featured more positive terms like 'love' and 'forgiveness.'" (p.10)

The annotation prompt structure for the AI content used GPT-4 to generate positive, negative, and neutral religious descriptions from a corpus of religious texts, social media content, and news reports (p.7).

## 4. Scoring / grading methodology
- Primary measure: 5-point Likert scores averaged across 7 sub-dimensions per religion; higher = more positive attitude.
- Reliability: Cronbach's alpha per religion (0.726–0.831; p.8, Table 1).
- Construct validity: KMO = 0.973 (p.8); Bartlett sphericity test significant (p<0.001).
- Group comparison: Independent samples t-test for AI vs. non-AI groups; paired samples t-test for within-group pre/post changes.
- Mediation: SEM analysis to test whether emotional response and perceived credibility mediate the AI content → attitude change pathway.
- Content analysis: Bias Benchmarking Framework applied with human annotation + computer-assisted analysis for Cultural Bias, Sentiment Bias, Omission Bias.

## 5. Dataset construction & provenance
- 1,005 participants recruited via online platform with stratified random sampling across 12 geographic regions (proportional to World Bank regional population).
- Demographics: mostly East Asian (34.4%), Southeast Asian (16.7%); age 25–34 predominant; undergraduate education predominant (p.8, Table 2).
- Religious breakdown: Buddhism (23.8%), Islam (20%), Christianity (18.4%), irreligious/atheist (15.3%), Hinduism (6.9%), Judaism (3.9%), Taoism (9.6%), other (2.2%) (p.8, Table 2).
- AI content: GPT-4 generated positive, negative, and neutral descriptions for each of the five religions, drawing on religious texts, social media, and news reports; adversarial training and bias detection techniques applied to attempt de-biasing (p.7).
- Study received Ethics Committee approval (BISU Ethics Committee No. 2025-001, p.15).

## 6. Validity evidence
- Cronbach's alpha ranges 0.726–0.831 (p.8), indicating adequate internal consistency; overall alpha = 0.953.
- KMO = 0.973 and Bartlett test significant confirm factor structure is extractable (p.8).
- No correlation found between demographic background factors (nationality, gender, education, religion, social context) and religious cognition, supporting the claim that AI content is the active variable (p.9).
- SEM confirms that emotional response and perceived credibility mediate the AI → attitude change pathway (p.10).
- Human annotation + content analysis independently corroborates the sentiment direction (Islam texts have 1.5× more "conflict" references in AI condition, p.10).
- Limitation: only a single interaction cycle was simulated, not the recursive feedback loop described theoretically.

## 7. Saturation / discrimination
- Effect sizes are modest (mean changes of 0.07–0.31 points on a 5-point scale) but statistically significant given n≈500 per group.
- Buddhism shows no significant change (t=−0.824, p>0.05), demonstrating that AI-generated content does not homogeneously affect all religions — the instrument discriminates.
- Christianity shows the largest positive shift (+0.31), Islam the largest negative shift (−0.23), and Judaism a smaller positive shift (+0.14) — pattern consistent with U.S.-dominated training data bias.
- Pre-intervention baseline scores cluster around 3.1–3.4 on the 5-point scale (mostly neutral), suggesting the instrument is centered appropriately to detect bidirectional shifts.

## 8. Multiturn / agentic aspects
n/a — The experimental design deliberately "simulated only a single cycle of interaction between humans and AI, without conducting repeated dialogues" (p.7). The paper acknowledges this as a limitation, noting it does not capture the recursive feedback mechanism theorized in the analysis framework.

## 9. Key numbers
- N = 1,005 participants (502 AI-interference, 503 control) (p.6)
- 12 geographic regions covered (p.6)
- 35-item questionnaire: 7 items × 5 religions, 5-point Likert scale (p.6)
- Christianity attitude shift: +0.31 (t=−7.197, p<0.001) (p.10)
- Islam attitude shift: −0.23 (t=7.718, p<0.001) (p.10)
- Buddhism attitude shift: not significant (t=−0.824, p=0.410) (p.10)
- Hinduism attitude shift: −0.07 (t=2.542, p=0.011) (p.10)
- Judaism attitude shift: +0.14 (t=−4.101, p<0.001) (p.10)
- KMO = 0.973 (p.8)
- Overall Cronbach's alpha = 0.953 (p.8)
- AI Islam texts contain 1.5× more "conflict" references than human texts (p.10)
- GPT-4 training data: Islam associated with "violence" at 1.7× higher semantic rate than other religions (cited from Abid et al., 2021, p.7)

## 10. Pitfalls & limitations
- **Single AI model:** Only GPT-4 tested; results may not generalize to other LLMs or open-source models.
- **Single interaction cycle:** The self-reinforcing feedback loop hypothesized by the framework is not tested; long-term cognitive effects are unknown.
- **Likert scale ceiling effects:** All pre-intervention scores cluster near the scale midpoint (3.1–3.4); extremes of attitude are not reached, potentially underestimating effect sizes.
- **Sample skew:** East Asian participants (34.4%) dominate; despite stratification, Middle Eastern and Muslim-majority populations are underrepresented relative to global proportions.
- **Content variable confound:** Each participant sees only one piece of AI content (positive, negative, or neutral) randomly assigned; the mix of content valence within the AI group may mask differential effects of positive vs. negative content separately.
- **No manipulation check:** No verification that participants actually read or understood the religious descriptions.
- **Methodological extrapolation:** The paper theorizes a complex bidirectional feedback loop but tests only a static, one-shot exposure — the gap between theory and experiment is large.
- **Generalizability of GPT-4 biases:** The measured biases reflect GPT-4 specifically at the time of testing; they may change with model updates or fine-tuning.

## 11. Novel ideas worth stealing
1. **Pre/post design for measuring AI content impact on values:** The randomized controlled trial design (AI-generated vs. human-written content, pre/post questionnaire) is directly transferable to benchmark construction — it provides a methodology for measuring whether a model's values outputs actually shift human attitudes, not just whether they "look" unbiased.
2. **Multi-religion simultaneous comparison:** Measuring attitude shifts toward five religions simultaneously, rather than one at a time, reveals differential bias patterns (Christianity vs. Islam vs. Buddhism) that a single-religion study would miss.
3. **Bias Benchmarking Framework for content analysis:** Applying Sentiment Polarity, Stereotype & Association, and Information Diversity measures to AI-generated text alongside human-generated controls is a practical methodology for detecting religious content bias that does not rely solely on survey data.
4. **Sub-dimension religious attitude decomposition:** Breaking "religious attitude" into seven sub-dimensions (history, doctrinal tolerance, ethics, society, image of believers, modernity, overall) catches differential effects that an overall impression measure would average away.
5. **Stratified cross-regional sampling design:** Recruiting across 12 geographic regions proportional to World Bank population estimates is a methodological template for culturally representative benchmark validation studies.
6. **SEM mediation analysis for mechanism testing:** Using structural equation modeling to test whether emotional response and perceived credibility mediate the AI content → attitude change relationship adds causal structure to what would otherwise be a correlation study.

## 12. Notable quotes
- "Generative AI not only reflects but amplifies cognitive biases, affecting users' understanding of religious doctrines and cultural diversity." (p.1)
- "Currently, mainstream generative AI models are influenced by internet data predominantly from the United States, which may explain the higher recognition of Christianity. The prevalence of religiously biased content in U.S. online media, particularly an implicit unfavorable attitude towards Islam, likely contributes to this bias." (p.10)
- "The bidirectional feedback loop between generative AI and users is fundamentally a dynamic interaction of 'data feeding-content generation-feedback reinforcement.'" (p.5)
- "AI can foster critical thinking and creativity, enabling educators to engage students in religious studies thoughtfully and inclusively… Generative AI tools should neither be demonized nor uncritically embraced." (p.13)

## 13. UNKNOWN / not in extract
- Exact wording of the 35 questionnaire items (individual item text not reproduced in the extract).
- Full set of AI-generated religious descriptions used as stimuli.
- Whether the "adversarial training and bias detection techniques" applied to GPT-4 content actually reduced bias, and how this was verified.
- Details of how positive, negative, and neutral content types were assigned to participants.
- Breakdown of results by content valence (positive vs. negative vs. neutral AI descriptions).
- Whether participants from Muslim-majority regions showed differential responses to Islam content compared to other regions.
- SEM path coefficients and model fit statistics.
- Full dataset (stated to be in supplementary information, not included in extract).
