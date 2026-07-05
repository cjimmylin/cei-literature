---
stem: "2025-Osei Mensah-Where are the missing values an exploration of the need to"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, pluralism-aggregation, normative-ethics]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: ["Africa contributes 3.8% of global carbon emissions yet is most vulnerable continent to climate change (p.1)", "Single GPT-3 training run emitted 942,330 kg CO2 in South Africa (p.2)", "AI could contribute up to $1.5 trillion to the African economy or 6% of GDP (p.7)", "83% of Africans depend on the environment for livelihood (p.9)"]
---
## 1. Gist
This paper argues that African AI policies fail to incorporate Ubuntu philosophy's communitarian values — especially Ukama (human-environment relatedness) — and instead replicate Eurocentric ethical frameworks. Through content analysis of five African AI governance documents (AUDA-NEPAD White Paper, AU Continental AI Strategy, Mauritius, Rwanda, and Benin national strategies), the paper finds that all fail to establish robust environmental regulations addressing the specific harms Africa bears from AI's life-cycle (carbon emissions from training in Africa, illegal mineral extraction, e-waste dumping). The paper is relevant to values-alignment benchmarking because it makes a concrete, evaluable claim: that values encoded in global AI governance documents systematically exclude African communitarian values, and proposes Ubuntu as a normative framework that could remediate this omission.

## 2. Benchmark/eval design features
Not a benchmark. The analytical framework is a content analysis rubric with two evaluation criteria applied to each of five policy documents:
1. Whether policies establish robust AI regulations (not merely aspirational statements).
2. Whether the environment is treated as having intrinsic value (Ubuntu/Ukama perspective) vs. only instrumental value (Eurocentric).

Summary tables (Tables 1–3) present a yes/no matrix of four features for each document: environmental sustainability via AI adoption (yes/no), mention of environmental risks from AI life cycle (yes/no), Ubuntu principles mentioned as a guide (yes/no), and robust ethical regulations (yes/no). All five documents score yes on feature 1 (leveraging environment for economic development) and yes on some Ubuntu mentions, but all score no on robust ethical regulations.

## 3. Task format & example item
n/a — normative and policy analysis paper.

## 4. Scoring / grading methodology
Content analysis with a binary yes/no rubric applied by the authors. No inter-rater reliability reported. The evaluation criteria are normatively grounded in Ubuntu philosophy rather than a pre-existing coding scheme.

## 5. Dataset construction & provenance
Policy documents analyzed: AUDA-NEPAD White Paper (April 2024), AU Continental Artificial Intelligence Strategy (July 2024), Mauritius AI Strategy (2018), Rwanda AI Strategy (2023), Benin National AI Strategy (2023). All publicly available.

## 6. Validity evidence
No statistical validity testing. The authors acknowledge using content analysis and note that the study relies on foundational textual evidence. Positioning is explicit: the authors are from University of Ghana and University of Bonn and explicitly adopt a decolonial perspective informed by Ubuntu philosophy.

## 7. Saturation / discrimination
The binary rubric produces a clear discriminant result: all five policy documents fail on "robust ethical regulations," including Rwanda which was previously identified by Ayana et al. (2024) as the only African country meeting "decolonization responsive" criteria (p.8). The paper argues this represents a systematic pattern, not individual failure.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- Africa contributes 3.8% of global carbon emissions but is "most vulnerable continent to climate change" (p.1, citing IPCC 2023)
- Single GPT-3 training run: 942,330 kg CO2 emitted in South Africa, 858,360 kg in India (p.2, citing Crowls et al. 2021)
- AI could contribute up to $1.5 trillion to African economy or 6% of GDP (p.7)
- 83% of Africans depend on environment for livelihood per AUCCRDSAP (p.9)
- Mauritius ranked 1st in African AI readiness (57th globally); Rwanda 2nd in Africa (p.8)

## 10. Pitfalls & limitations
- Binary yes/no rubric may oversimplify the nuanced treatment of environment in each policy document.
- No inter-rater reliability assessment.
- Ubuntu is used as a general proxy for African communitarianism despite acknowledged diversity among sub-Saharan cultures (p.4).
- The "dreaming" framework (Laenui 2000) is aspirational; the paper does not generate a fully specified Ubuntu AI policy.
- Focuses exclusively on Sub-Saharan Africa; North African or non-Ubuntu contexts are excluded.
- Paper does not address whether Ubuntu frameworks could themselves have gaps (e.g., treatment of minorities within communities).

## 11. Novel ideas worth stealing
- **Values-as-policy-audit methodology**: The binary rubric (does document address environmental risks? does it treat environment as intrinsic vs. instrumental?) is directly replicable for auditing AI governance documents for any specified set of values. A benchmark could apply this to evaluate LLMs' ability to identify such gaps.
- **Pluriversal value framing**: The paper's call for "pluriversal" approaches (multiple worldviews on environmental sustainability) maps directly to a benchmark design challenge: how to aggregate or represent plural value systems without homogenizing them.
- **Ubuntu as normative benchmark baseline**: Ubuntu's solidarity, reciprocity, Ukama (human-nature relatedness) provide non-WEIRD ethical constructs that could be tested against LLM responses to environmental harm scenarios.
- **Eurocentric default as testable alignment property**: The claim that African institutions adopt Eurocentric values is analogous to Okamoto et al.'s principlist default claim — LLMs trained predominantly on Western texts may exhibit a systematic Eurocentric ethical bias detectable via policy-audit prompts.
- **Intrinsic vs. instrumental value of nature as discriminating dimension**: A benchmark item could present an environmental scenario and ask whether a model treats the environment as a means to human ends or as having intrinsic worth. This would discriminate between Western utilitarian and Indigenous relational frameworks.

## 12. Notable quotes
- "The lack of attention to African voices has ultimately left African policy on AI governance sorely lacking to consider the unique African context." (p.1)
- "The adaptation of Eurocentric ethics, values and policies by African socio-political schemes and institutions is a form of neo-colonialism." (p.2)
- "Ubuntu philosophy introduces three things to the focus of African AI ethical regulations. First, it places moral responsibility on anyone associated with AI to adopt sustainable methods by respecting nature and the environment." (p.5)
- "Where are the missing values?" (p.9)

## 13. UNKNOWN / not in extract
- Specific quotes or passages from the five policy documents analyzed (only summaries are provided).
- Whether co-author Aimee Van Wynsberghe's "sustainable AI" framework is directly embedded in the Ubuntu analysis or treated as background.
- Whether the AU AI Strategy was drafted with any Ubuntu input from African scholars.
- Details of how the content analysis coding was conducted (solo, dual-coded, disputed cases).
