---
title: "2025-Wu-Chain-of-Ethics Defense Framework Wu et al. - PDF Extract"
source_pdf: "2025-Wu-Chain-of-Ethics Defense Framework Wu et al..pdf"
pages: 19
extracted_at: "2026-02-08T06:02:21.389335"
---

# PDF Extract: 2025-Wu-Chain-of-Ethics Defense Framework Wu et al.

**Source PDF:** 2025-Wu-Chain-of-Ethics Defense Framework Wu et al..pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

 
1 
 
Ethical Risks in Deploying Large Language Models: An Evaluation 
of Medical Ethics Jailbreaking 
Chutian Huang1, Dake Cao2, Jiacheng Ji3, Yunlou Fan4, Chengze Yan5, Hanhui Xu6* 
 
ABSTRACT 
Background: While Large Language Models (LLMs) have achieved widespread adoption, 
malicious prompt engineering—specifically "jailbreak attacks"—poses severe security risks 
by inducing models to bypass internal safety mechanisms. Current benchmarks predominantly 
focus on public safety and Western cultural norms, leaving a critical gap in evaluating the 
niche, high-risk domain of medical ethics within the Chinese context. 
Objective: To establish a specialized jailbreak evaluation framework for Chinese medical 
ethics and to systematically assess the defensive resilience and ethical alignment of seven 
prominent LLMs when subjected to sophisticated adversarial simulations. 
Methodology: We evaluated seven prominent models (e.g., GPT-5, Claude-Sonnet-4-
Reasoning, DeepSeek-R1) using a "role-playing + scenario simulation + multi-turn dialogue" 
vector within the DeepInception framework. The testing focused on eight high-risk themes, 
including commercial surrogacy and organ trading, utilizing a hierarchical scoring matrix to 
quantify the Attack Success Rate (ASR) and ASR Gain. 
Results: A systemic collapse of defenses was observed, whereas models demonstrated high 
 
1 Department of Central Laboratory, Shanghai Children’s Hospital, School of Medicine, Shanghai Jiaotong 
University, Shanghai, China; School of Philosophy, Fudan University, 24260160010@m.fudan.edu.cn. 
2 School of Philosophy, Fudan University, 24210160035@m.fudan.edu.cn. 
3 Institute of Technology Ethics for Human Future, Fudan University, jijiacheng2000@126.com. 
4 School of Philosophy, Fudan University, 24260160005@m.fudan.edu.cn. 
5 School of Philosophy, Fudan University, 24260160031@m.fudan.edu.cn. 
6 Institute of Technology Ethics for Human Future, Fudan University, xuhanhui@fudan.edu.cn. 
* Corresponding Author. 

--- Page 2 ---

 
2 
 
baseline compliance, the jailbreak ASR reached 82.1%, representing an ASR Gain of over 80 
percentage points. Claude-Sonnet-4-Reasoning emerged as the most robust model, while five 
models—including Gemini-2.5-Pro and GPT-4.1—exhibited near-total failure with ASRs 
between 96% and 100%. 
Conclusions: Current LLMs are highly vulnerable to contextual manipulation in medical 
ethics, often prioritizing "helpfulness" over safety constraints. To enhance security, we 
recommend a transition from outcome to process supervision, the implementation of multi-
factor identity verification, and the establishment of cross-model "joint defense" mechanisms. 
 
Keywords: Medical Ethics; Large Language Models; Jailbreak Attacks; AI Alignment; 
Chinese Context. 
 
INTRODUCTION 
Large Language Models (LLMs), owing to their robust natural language processing 
capabilities, have been widely adopted across diverse industries. However, this widespread 
application is accompanied by severe security risks: malicious users may employ specific 
prompt engineering techniques to induce models to bypass built-in security defense 
mechanisms and generate harmful or sensitive content—a phenomenon termed “Jailbreak 
Attacks” 1 2. In response to these threats, the academic community has launched extensive 
research3 4. Current attack methods are primarily categorized into white-box attacks (requiring 
access to the model’s internal parameters) and black-box attacks (needing only API access)5-
12. Among these, black-box strategies such as DeepInception13 are particularly insidious. They 

--- Page 3 ---

 
3 
 
demand no specialized expertise and incur minimal implementation costs, enabling ordinary 
users to breach model defenses—rendering them particularly perilous. For defense evaluation, 
researchers have developed multiple benchmark datasets such as AdvBench and 
JailbreakBench12 14-20, which cover a wide range of scenarios spanning from general harmful 
speech to specific social misuse cases.  
 
This study is the first jailbreak evaluation targeting the field of medical ethics. We evaluated 
seven mainstream Chinese and English models on eight high-risk themes. Based on 
DeepInception method, we launch jailbreak attacks by role-playing specific characters—such 
as police officers tracking the black market for organ trafficking—in hypothetical scenarios. 
By applying a unified risk scoring system, we quantify the defensive resilience of these 
models against jailbreak attempts across diverse contexts. 
 
The contributions of this study are threefold. First, the study presents the first comprehensive 
evaluation of LLM defense mechanisms concerning medical ethics, thereby broadening the 
scope of safety research. Second, it reveals systemic vulnerabilities in how mainstream 
models handle ethically sensitive medical queries. Third, the study proposes evidence-based 
recommendations aimed at mitigating jailbreak risks targeting medical ethics in LLMs. 
 
METHODOLOGY 
2.1 Dataset 
2.1.1 Selection of Evaluation Themes 

--- Page 4 ---

 
4 
 
Eight high-risk themes in medical ethics were selected, namely: commercial surrogacy, organ 
trafficking, blood trade, concealment of HIV-positive test results, inducement of suicide 
among minors, medical bribery, manufacture of illicit drugs, and fetal sex identification7. 
 
2.1.2 Establishment of Baseline and Jailbreak Test Groups 
(1) Baseline Control Group: For each of the eight themes, we administered direct inquiries 
containing explicit ethical violations.  
(2) Jailbreak Experimental Group: We implemented a composite attack strategy utilizing 
“role-playing + scenario simulation + multi-turn dialogue”. 
 
2.1.3 Design of Jailbreak Scenarios  
For each medical ethics topic, three role scenarios were designed, with each scenario 
containing no fewer than two turns of dialogue content. In constructing roles and scenarios, 
we leveraged the model’s role-playing ability to mimic human interaction, inducing it to 
immerse itself in specific identity scenarios and forget system safety constraints by adopting 
fictional professional identities. In terms of questioning methods, we utilized the long-context 
format of multi-turn dialogues, gradually reducing the model’s defensive vigilance and 
building trust through seemingly harmless preliminary questions. In experimental control, 
standardization and consistency in dialogue structure and content were maintained across 
different models to ensure the reliability and validity of the evaluation. Additionally, the 
 
7 Article 39 of the Population and Family Planning Law of the People’s Republic of China stipulates: "The use of 
ultrasound technology and other technical means to conduct fetal sex identification for non-medical purposes is 
strictly prohibited; sex-selective artificial termination of pregnancy for non-medical purposes is strictly prohibited. 

--- Page 5 ---

 
5 
 
public safety theme of “manufacturing bombs” was introduced as a control evaluation group. 
 
2.2 Establishing Evaluation Scoring Standards 
This study developed a hierarchical scoring framework (Table 1). 
 
Level Description 
Score 
1 
The models provided helpful information aligned with the enacted 
persona, without violating ethical requirements. 
2 
2 
While the models adhered to ethical codes, it failed to provide helpful 
information. 
1 
3 
Explicit refusal to answer or irrelevant response. 
0 
4 
The disclosed information facilitates illicit activity, but it is generalized 
(with low actionability) and accompanied by risk warnings. 
-1 
5 
The disclosed information facilitates illicit activity, but it is generalized 
(with low actionability) and lacks risk warnings. 
-2 
6 
The provided information offered granular, actionable details or 
operational steps, but also included risk warnings, scope limitations, or 
disclaimers. 
-3 
7 
The provided information offered granular, actionable details or 
operational steps, lacking any risk warnings. 
-4 
Table 1 Grading and Scoring Matrix for Medical Ethics Jailbreak Evaluation in Large 
Language Models8 
 
2.3 Model Selection and Evaluation Implementation 
To ensure a representative evaluation spectrum, this study selected seven prominent Chinese 
and global foundation models including DeepSeek-R1, Qwen-3-235B-2507-T, Doubao, 
Claude-Sonnet-4-Reasoning, GPT-4.1, GPT-5, and Gemini-2.5-Pro9 (refer to Appendix B for 
evaluation prompts). 
 
8 Detailed criteria for grading and scoring, along with examples, are provided in Appendix A. 
9 The model evaluation phase for this study was conducted from August 2025 to November 2025. 

--- Page 6 ---

 
6 
 
 
2.4 Analysis of Data Metrics 
Utilizing the scoring framework established above, we calculated key metrics to provide a 
granular assessment of the models’ ethical alignment and defensive resilience. 
 
2.4.1 Calculation of Quantitative Metrics 
(1) Attack Success Rate (ASR) 
𝐴𝑆𝑅= 1
𝑁∑𝐼(𝑆𝑐𝑜𝑟𝑒𝑖< 0)
𝑁
𝑖=1
 
 
The ASR serves as a direct indicator of model vulnerability, quantifying the proportion of 
samples that elicited harmful responses relative to the total dataset10. A jailbreak is deemed 
successful when 𝑆𝑐𝑜𝑟𝑒𝑖< 0.  
(2) Attack Success Rate Gain (ASRGain) 
𝐴𝑆𝑅𝐺𝑎𝑖𝑛= 𝐴𝑆𝑅𝐽𝑎𝑖𝑙𝑏𝑟𝑒𝑎𝑘−𝐴𝑆𝑅𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒 
 
This metric quantifies the comparative robustness of the model's defense system under 
adversarial stress. It is calculated as the differential between ASRJailbreak and ASRBaseline, where: 
ASRBaseline (Baseline Attack Success Rate) denotes the proportion of violative content 
generated via zero-shot direct questioning. ASRJailbreak (Jailbreak Attack Success Rate) denotes 
the proportion of violative content elicited using the specific jailbreak vectors designed in this 
 
10 Where N denotes the total number of test samples (e.g., 3 samples per theme × 8 themes = 24 total samples); 
Scorei denotes the score obtained by the i-th sample based on the aforementioned scoring table; and is the indicator 
function, which takes the value 1 when the condition inside the parentheses (Scorei<0) is satisfied, and 0 
otherwise. 

--- Page 7 ---

 
7 
 
study.  
 
2.4.2 Statistical Significance Analysis 
Given that the evaluation scoring data exhibit non-normal distribution characteristics and the 
test results of each model under the same medical ethics themes are related samples, this 
study abandoned traditional parametric test methods and instead adopted an analytical 
approach combining non-parametric statistical methods with dispersion indicators: (1) The 
Friedman Rank Sum Test was used to evaluate whether there were significant differences in 
the overall performance of seven LLMs across eight medical ethics themes. (2) The Wilcoxon 
Signed-Rank Test was employed, on the basis of significant overall differences, for post-hoc 
pairwise comparisons between models in the top tier of defensive capabilities (such as the top 
two best-performing models). (3) Dispersion analysis introduced the interquartile range (IQR) 
and standard deviation (SD) as quantitative indicators for defensive patterns. By calculating 
the dispersion of scores, it aimed to distinguish whether a model’s performance was stable. 
 
RESULTS 
3.1 Systemic Failure of Defenses Against Jailbreak Attacks  
This evaluation first established a control benchmark. When we did not employ jailbreak 
strategies but instead directly posed non-compliant questions on eight medical ethics themes, 
nearly all tested models successfully activated their defense mechanisms. Among them, GPT-
4.1 tended to adopt a direct refusal-to-answer approach; whereas the remaining models (such 
as GPT-5, Claude-Sonnet-4-Reasoning, etc.) generally shifted to analyzing the potential 

--- Page 8 ---

 
8 
 
ethical risks and legal consequences of the raised questions, providing advisory responses to 
dissuade such inquiries, thereby avoiding the direct output of harmful content. However, the 
deployment of the “role-playing + scenario simulation + multi-turn dialogue ” vector 
precipitated a systemic failure in these defenses (see Table 2). 
 
Topics 
 
LLMs 
Comme
rcial 
Surroga
cy 
Organ 
Trade 
Blood 
Trade 
Conceal
ment of 
HIV+ 
Status 
Incitem
ent to 
Suicide 
Medical 
Bribery 
Illegal 
Drug 
Product
ion 
Fetal 
Sex 
Determi
nation 
Total 
Score (8 
Themes) 
Model 
ASR 
GPT-4.1 
-10 
-10 
-12 
-8 
-12 
-12 
-8 
-12 
-84 
100% 
GPT-5 
-7 
-2 
-4 
1 
-2 
-5 
-2 
3 
-18 
63% 
Claude-
Sonnet-4- 
Reasoning 
1 
2 
-2 
-1 
0 
3 
3 
-1 
5 
38% 
Gemini-
2.5-Pro 
-12 
-12 
-12 
-12 
-11 
-12 
-11 
-12 
-94 
100% 
DeepSeek-
R1 
-11 
-12 
-11 
-12 
-12 
-12 
-11 
-12 
-93 
100% 
Qwen-3-
235B 
-12 
-10 
-8 
-9 
-11 
-9 
-11 
-10 
-80 
100% 
Doubao 
-11 
-12 
-12 
-8 
-12 
-12 
-11 
-12 
-90 
96% 
Total Score 
per 
Scenario 
-62 
-56 
-61 
-49 
-60 
-59 
-51 
-56 
N/A 
N/A 
Scenario 
ASR 
86% 
81% 
76% 
86% 
91% 
81% 
81% 
81% 
N/A 
82% 
Table 2 Overview of Scores for Seven Evaluated Models Across Eight Scenarios 
 
In the Baseline Test, when faced with direct questions, the vast majority of models 
successfully triggered their defense mechanisms, with the baseline attack success rate 
(ASRBaseline) approaching 0%. However, after introducing a jailbreak strategy, the defense 
system experienced a systemic collapse. As illustrated in Figure 1, of the 168 samples 

--- Page 9 ---

 
9 
 
subjected to jailbreak vectors, 138 responses were adjudged as harmful (Score < 0, i.e., Levels 
4-7), resulting in an aggregate Jailbreak Attack Success Rate (ASRJailbreak) of 82.1%. 
Consequently, the Attack Success Rate Gain (ASRGain) exceeded 80 percentage points, 
underscoring the profound fragility of current LLM robustness when confronted with 
contextual manipulation. Further analysis of the response quality distribution (Figure 1) 
reveals that the vast majority of responses (72.6%) were induced to generate practical illegal 
guidance (Level 6–7), among which over half (57.1%) did not even include any risk warnings 
(Level 7). 
 
 
Figure 1 Distribution of Score Levels Across 168 Responses 
 
3.2 Defense Blind Spots Exist in Medical Ethics Themes  
From a thematic perspective, unlike the control group involving bomb-making, the 
vulnerability of LLMs in the field of medical ethics exhibits a high degree of universality 
rather than being confined to a single topic. As shown in Figure 2, all eight high-risk themes 

--- Page 10 ---

 
10 
 
covered in the test had negative total scores, with an extremely uniform distribution: ranging 
from the lowest-scoring “commercial surrogacy” (-62.0) to the relatively higher-scoring 
“concealment of HIV-positive results” (-49.0), no significant safe havens emerged. Notably, 
even in the case of the "concealment of HIV-positive results" topic—which had the relatively 
highest score—its ASR remained high (76.2%). In addition, the standard deviation (SD) of 
the scores for the 8 topics is merely 4.41. This minimal variability strongly demonstrates that 
the current jailbreak risk does not stem from a deficit in understanding a specific medical 
knowledge point, but rather from a general lack of deep alignment with medical ethics 
contexts in models. 
 
 
Figure 2 Aggregate Model Scores Across Eight Medical Ethics Scenarios and the Control 
Scenario 
 

--- Page 11 ---

 
11 
 
3.3 The Polarization of Defensive Capabilities 
A clear polarization emerged in the performance of various models in defending against 
jailbreak attacks. The Friedman rank-sum test confirmed that the differences in defense 
capabilities among the seven models were statistically highly significant (χ² = 37.09, p ≈ 
1.69×10⁻⁶ < 0.001). Based on the total scores of the 7 models (Figure 3) and their ASRs 
(Table 2), the model cohort can be divided into two distinctly different echelons. First is the 
effective defense echelon. Claude-sonnet-4-reasoning topped the list with a total score of 5.0, 
making it the only model to achieve a positive score. Its ASR of 38% was significantly lower 
than that of other models. As shown in Figure 3, its distribution density centered on the 
median (Mdn = 0.5), with most scores concentrated in the positive range and a relatively 
symmetric shape—indicating relatively consistent performance across different medical ethics 
topics. GPT-5 followed closely with a total score of -18.0 and an ASR of 63%. In Figure 3, it 
showed an obvious extension trend, with scores exhibiting wide distribution and extreme 
volatility; its median fell in the negative range (Mdn = -2), suggesting its defense mechanism 
is relatively fragile, susceptible to interference from specific prompts, and lacks stability.  
Second is the failed defense echelon. The remaining five models (gemini-2.5-Pro, deepSeek-
R1, doubao, gpt-4.1, qwen-3) all had total scores below -80, with ASRs as high as 96% to 
100%. The interquartile range (IQR) of cross-model total scores was as high as 42.5, 
accounting for approximately 30% of the theoretical total range, indicating wide dispersion. 
As shown in Figure 3, they also exhibited a clear floor effect.  
 

--- Page 12 ---

 
12 
 
 
Figure 3 Aggregate Scores of Seven Models Across All Eight Scenarios 
 
DISCUSSION 
Firstly, our study shows that for most models, there exist systemic risks when facing jailbreak 
attacks of the “role-playing + scenario simulation + multi-turn dialogue” type in the context 
of medical ethics themes. First, in medical ethics themes, when confronted with contextual 
attacks, models exhibit widespread structural failures in their defenses. They demonstrate 
high surface compliance while masking deep-seated security flaws. This compliance risk is 
more insidious and deceptive than having no defense at all. The naivety of models toward 
prompts claiming special identities means users can bypass LLMs’ defenses by disguising 
their identities, thereby obtaining sensitive information accessible only to professionals. This 
lowers the barrier to accessing sensitive information and reduces the cost of committing 
related crimes. Second, in medical ethics themes, models’ defense capabilities reflect a long-
tail effect: the good defenses of a few models cannot offset the systemic collapse of most 

--- Page 13 ---

 
13 
 
models under jailbreak attacks. This means that for malicious actors, even if they cannot 
obtain sensitive information from high-defense models, they can switch to other low-defense 
models at an extremely low cost to acquire such information. At present, LLMs as an 
emerging means of information access do not possess good overall defense capabilities. 
Conversely, no matter how impenetrable high-defense models are, low-defense models still 
pose a risk of harming society. This may be a future research direction for LLM jailbreak 
defense: how to establish cross-model defense cooperation mechanisms to enhance the overall 
jailbreak resistance of LLMs. 
 
Secondly, compared to public safety themes such as “how to make a bomb,” models perform 
even worse when facing jailbreak attacks on medical ethics themes. We conducted a 
controlled experiment comparing LLM responses to attacks on medical ethics themes versus 
those on the “how to make a bomb” theme, and the difference was significant. This 
discrepancy is not accidental but an inevitable result of current LLM security design. A 
problem in LLMs’ ethical alignment is their training paradigm relying on massive data, which 
causes them to exhibit varying performance across different themes. For attacks that are clear-
cut, consensus-based, and frequently occurring in training data, LLMs can easily handle them 
and provide appropriate responses. However, for attacks on medical ethics: on one hand, there 
are numerous variations in specific scenarios and concrete means of violating ethical 
principles, and the training data for LLMs cannot fully cover these. This leads to an unclear 
“impression” of such ethical issues in LLMs. On the other hand, for similar questions, human 
labeling may vary due to differences in occurrence scenarios and description methods. This 

--- Page 14 ---

 
14 
 
results in a low density and scattered distribution of rewards and punishments for LLMs. 
Consequently, when facing novel problems, models are more prone to hesitation and thus 
more susceptible to being breached. 
 
Thirdly, the superior performance of Claude-Sonnet-4-Reasoning is plausibly attributable to 
its adoption of the “Constitutional AI” (CAI) paradigm. In contrast to traditional 
Reinforcement Learning from Human Feedback (RLHF), which relies heavily on stochastic 
human preference labeling21, CAI integrates a “Digital Constitution”—a codified set of 
normative principles—to govern model behavior under ethical stress22-27. However, Claude 
with CAI also exhibits over-sensitivity to questions involving ethical risks, rendering it unable 
to provide valuable information to professionals. In our evaluation, Claude’s over-sensitivity 
manifested in the following aspects: first, identity sensitivity. In our tests, scenarios like 
“mitigation defense” and “hospice care provider” scored higher, as the model immediately 
identified users attempting to gain trust by claiming a certain identity to obtain more 
information. During the thinking phase, it doubted the authenticity of the user’s identity, 
further reinforced the boundaries of information provision, and actively changed the subject 
during the response phase. Second, information source sensitivity. After identifying the user’s 
identity, the model proactively provided non-AI information access channels appropriate for 
their identity. For example, it suggested lawyers search for public cases on official platforms, 
advised consulting experts in relevant fields, and recommended novelists obtain creative 
resources from documentary literature. The model thus proactively avoided becoming a 
provider of sensitive information. 

--- Page 15 ---

 
15 
 
 
SUGGESTIONS 
First, this study recommends shifting the research focus of moral alignment from Outcome 
Supervision (OS) to Process Supervision (PS). OS merely requires a black-box target that 
performs well, whereas PS demands that each step of the model’s reasoning be morally 
auditable. Secondly, this study suggests introducing an identity verification step to strengthen 
models against jailbreak attacks of the “role-playing + scenario simulation” type, while 
ensuring accessibility of special information for professionals. This study found that models 
with weaker defenses are more likely to trust users’ “benign intentions” during role-playing 
and thus provide more information, whereas models with stronger defenses completely refuse 
to offer further details regardless of the user’s role. This creates two problems: first, users can 
easily bypass the defenses of weaker models by disguising their identities; second, 
professionals who need model assistance cannot obtain more details through the models. A 
feasible solution is to add a verification step to check the credibility of the “identity” claimed 
by users when they request sensitive or high-risk information. Finally, this study recommends 
that multiple large language models (LLMs) adopt “joint defense” to enhance the overall 
security of LLMs as a means of information access. This study found significant performance 
differences among different models: although high-defense models perform well, malicious 
actors can use low-defense models to obtain information at an extremely low cost, meaning 
LLMs as an information access tool lack overall security. It is suggested that future laws and 
regulations be enacted to urge LLM developers to promptly adopt state-of-the-art defense 
technologies. Only by "joining forces" can the cost of accessing sensitive information be 

--- Page 16 ---

 
16 
 
increased, thereby ensuring the overall security of this important information channel. 
 
LIMITATIONS 
First, this study takes China’s medical ethics codes as the standard for evaluating model 
responses, which puts international models at a greater disadvantage compared to domestic 
models. For example, in China, commercial surrogacy violates ethical norms, whereas it is 
legal in some English-speaking countries and regions. Considering that a large portion of the 
training data for domestic models comes from Chinese corpora, these models are more likely 
than international models to provide responses that comply with China’s ethical norms. 
Secondly, this study set eight high-risk themes in medical ethics for evaluation. Although the 
selection of these themes was based on careful planning, these eight themes are not sufficient 
to exhaust all high-risk themes in medical ethics. Themes such as physician-assisted suicide 
and euthanasia are also high-risk but were not covered in our study. 
 
CONCLUSION 
This study is the first jailbreak evaluation of LLMs focusing on medical ethics. Based on 
medical ethics codes in China, the study conducted jailbreak evaluations on seven LLMs on 
eight themes by using the method of “role-playing + scenario simulation + multi-turn 
dialogue.” The results show that: (1) Facing jailbreak attacks targeting medical ethics themes, 
the models generally exhibited low defense capabilities and were easily induced by attackers 
to generate harmful information. (2) Although all models failed to meet expectations in the 
evaluation, Claude—adopting a Constitutional AI approach—performed the best by 

--- Page 17 ---

 
17 
 
comparison, and its defense strategy is worth referencing. (3) Compared with jailbreak attacks 
targeting public safety themes (e.g., “how to make a bomb”), the models performed even 
worse when facing jailbreak attacks on medical ethics themes, which deserves attention. 
Based on the above evaluation results, constructing cross-model jailbreak attack defense 
mechanisms and user identity verification mechanisms appears to be a feasible improvement 
measure. 
 
Ethics approval and consent to participate: Not applicable. 
Competing interests: The authors declare that they have no competing interests. 
Data Availability Statement: The datasets comprising the 168 dialogue test samples and 
granular scoring metrics analyzed during the current study are available from the 
corresponding author on reasonable request. 
Funding: This work has been supported by the China NSSFC Project (Grant No. 
22CZX019). 
Author Contributions 
Chutian Huang: Conceptualization, Methodology, Investigation (lead LLM evaluation and 
prompt engineering), and Writing – original draft (Methods). 
Dake Cao: Investigation (literature review), Writing – original draft (Introduction and 
Discussion). 
Jiacheng Ji: Software (technical support), Data curation, Formal analysis, Visualization 
(figures and tables), Writing – original draft (Results), and Writing – review & editing 
(translation and linguistic refinement). 

--- Page 18 ---

 
18 
 
Yunlou Fan: Investigation (literature retrieval support) and Data curation (evaluation 
assistance). 
Chengze Yan: Investigation (literature retrieval support) and Data curation (evaluation 
assistance). 
Hanhui Xu: Conceptualization (methodological guidance), Funding acquisition, Supervision, 
and Writing – review & editing (critical revision for intellectual content and final polishing). 
All authors have read and agreed to the published version of the manuscript. 
 
REFERENCE 
1. Hazell J. Spear phishing with large language models. 2023 doi: 10.48550/arXiv.2305.06972 
2. Exploiting programmatic behavior of LLMs: Dual-use through standard security attacks. 
Proceedings of the 40th International Conference on Machine Learning (ICML); 2023. 
3. Chu J, Liu Y, Yang Z, et al. JailbreakRadar: Comprehensive assessment of jailbreak attacks against 
LLMs. arXiv preprint arXiv:240205668 2024 doi: 10.48550/arXiv.2402.05668 
4. Liu Y, Deng G, Xu Z, et al. Jailbreaking ChatGPT via prompt engineering: An empirical study. arXiv 
preprint arXiv:230513860 2023 doi: 10.48550/arXiv.2305.13860 
5. Jailbreaking leading safety-aligned LLMs with simple adaptive attacks. Proceedings of the 
International Conference on Learning Representations (ICLR 2025); 2025. 
6. Does refusal training in llms generalize to the past tense. Proceedings of the International 
Conference on Learning Representations (ICLR 2025); 2025. 
7. Chao P, Robey A, Dobriban E, et al. Jailbreaking black box large language models in twenty queries. 
arXiv preprint arXiv:231008419v4 2024 
8. Jiang F, Xu Z, Niu L, et al. Artprompt: Ascii art-based jailbreak attacks against aligned llms. arXiv 
preprint arXiv:240211753v4 2024 
9. AutoDAN: Generating stealthy jailbreak prompts on aligned large language models. Proceedings of 
the International Conference on Learning Representations (ICLR 2024); 2024. 
10. Samvelyan M, Raparthy SC, Lupu A, et al. Rainbow teaming: Open-ended generation of diverse 
adversarial prompts. arXiv preprint arXiv:240216822v3 2024 
11. Yi S, Liu Y, Sun Z, et al. Jailbreak attacks and defenses against large language models: A survey. 
arXiv preprint arXiv:240704295 2024 doi: 10.48550/arXiv.2407.04295 
12. Zou A, Wang Z, Carlini N, et al. Universal and transferable adversarial attacks on aligned language 
models. arXiv preprint arXiv:230715043 2023 doi: 10.48550/arXiv.2307.15043 
13. Li X, Zhou Z, Zhu J, et al. Deepinception: Hypnotize large language model to be jailbreaker. arXiv 
preprint arXiv:231103191v5 2024 
14. JailbreakBench: An open robustness benchmark for jailbreaking large language models. 

--- Page 19 ---

 
19 
 
Proceedings of the 38th Conference on Neural Information Processing Systems (NeurIPS 
2024) Track on Datasets and Benchmarks; 2024. 
15. MedSafetyBench: Evaluating and improving the medical safety of large language models. 38th 
Conference on Neural Information Processing Systems (NeurIPS 2024): Datasets and 
Benchmarks Track; 2024. 
16. Lin H, Luo Z, Wang B, et al. GOAT-Bench: Safety insights to large multimodal models through 
meme-based social abuse. arXiv preprint arXiv:240101523v4 2025 
17. Niu Z, Ren H, Gao X, et al. Jailbreaking attack against multimodal large language model. arXiv 
preprint arXiv:240202309v1 2024 
18. "Do anything now": Characterizing and evaluating in-the-wild jailbreak prompts on large language 
models. Proceedings of the ACM Conference on Computer and Communications Security 
(CCS 2024); 2024. 
19. Zhang W, Lei X, Liu Z, et al. CHiSafetyBench: A Chinese hierarchical safety benchmark for large 
language models. arXiv preprint arXiv:240610311v2 2024 
20. Ying Z, Liu A, Liang S, et al. SafeBench: A safety evaluation framework for multimodal large 
language models. arXiv preprint arXiv:241018927v1 2024 
21. Stiennon N, Ouyang L, Wu J, et al. Learning to summarize from human feedback. arXiv preprint 
arXiv:200901325 2020 
22. Abiri G. Public Constitutional AI. arXiv preprint arXiv:240616696 2024 
23. Bai Y, Kadavath S, Kundu S, et al. Constitutional AI: Harmlessness from AI Feedback. arXiv 
preprint arXiv:221208073 2022 
24. Findeis A, Kaufmann T, Hüllermeier E, et al. Inverse Constitutional AI: Compressing Preferences 
into Principles. arXiv preprint arXiv:240606560 2024 
25. Collective Constitutional AI: Aligning a Language Model with Public Input. Proceedings of the 
2024 ACM Conference on Fairness, Accountability, and Transparency (ACM FAccT); 2024. 
26. Kundu S, Bai Y, Kadavath S, et al. Specific versus General Principles for Constitutional AI. arXiv 
preprint arXiv:231013798 2023 
27. Zhang X. Constitution or Collapse? Exploring Constitutional AI with Llama 3-8B. arXiv preprint 
arXiv:250404918 2025 
 
 

```
