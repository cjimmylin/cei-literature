---
title: "2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized - PDF Extract"
source_pdf: "2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized.pdf"
pages: 19
extracted_at: "2026-02-07T17:00:46.797312"
---

# PDF Extract: 2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized

**Source PDF:** 2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

arXiv:2505.11861v1  [cs.AI]  17 May 2025
FAIR-PP: A Synthetic Dataset for Aligning LLM with
Personalized Preferences of Social Equity
Qi Zhou1
Jie Zhang2
Dongxia Wang1∗
Qiang Liu1
Tianlin Li3
Jin Song Dong4
Wenhai Wang1
Qing Guo2
1Zhejiang University
2IHPC and CFAR, A*STAR
3Nanyang Technological University
4National University of Singapore
{qi.zhou, qiang.liu, dxwang, zdzzlab}@zju.edu.cn, tianlin001@e.ntu.edu.sg,
zhang_jie@cfar.a-star.edu.sg, tsingqguo@ieee.org, dcsdjs@nus.edu.sg
Abstract
Human preference plays a crucial role in the refinement of large language models
(LLMs). However, collecting human preference feedback is costly and most exist-
ing datasets neglect the correlation between personalization and preferences. To
address this issue, we introduce FAIR-PP, a synthetic dataset of personalized pref-
erences targeting social equity, derived from real-world social survey data, which
includes 28 social groups, 98 equity topics, and 5 personal preference dimensions.
Leveraging GPT-4o-mini, we engage in role-playing based on seven representative
persona portrayals guided by existing social survey data, yielding a total of 238,623
preference records. Through FAIR-PP, we also contribute (i) An automated frame-
work for generating preference data, along with a more fine-grained dataset of
personalized preferences; (ii) analysis of the positioning of the existing mainstream
LLMs across five major global regions within the personalized preference space;
and (iii) a sample reweighting method for personalized preference alignment, en-
abling alignment with a target persona while maximizing the divergence from other
personas. Empirical experiments show our method outperforms the baselines.
Code: github.com/tools-only/FairPP
Dataset: huggingface.co/datasets/tools-o/Fair-PP
1
Introduction
With the growing adoption of LLMs in public policy making and public services234, a key question is
How can an LLM-based public policy maker accurately capture and represent dynamic and diverse
personalized preferences of social values? On one hand, social values like equity vary significantly
among individuals[1, 2]. On the other hand, to promote the alignment of LLMs with diverse societal
values is crucial to achieve societal safety [3–6], supporting cultural inclusivity [7–10], and also
reflecting diverse human values [11–14]. For the alignment, high-quality human feedback of their
social-value preference is necessary. However, its collection can incur significant costs [15, 16].
Moreover, human personalized preferences within a region evolve over time, influenced by factors
such as demographic shifts and social development [17–19].
∗Corresponding author
2https://openai.com/global-affairs/introducing-chatgpt-gov/
3https://openai.com/index/democratic-inputs-to-ai-grant-program-update/
4https://huggingface.co/stewhsource/GovernmentGPT
Preprint.

--- Page 2 ---

Persona 6
Persona 1
Persona 3
Mistral-7B
Llama-3.2-3B
Falcon3-7B
Llama-SEA-LION-v3-8B
Llama-3.1-8B
Persona 7
Persona 5
Persona 4
Persona 2
Majority
Qwen2.5-7B
Figure 1: Landscape of FAIR-PP space.
Despite increasing efforts in exploring and collecting hu-
man preference data of social values, existing datasets face
several limitations: (i) Social equity unaddressed: lack
consideration of social equity which is an important is-
sue in social psychology5 (ii) Neglecting personalization:
Most of them emphasize universal viewpoints, e.g., cul-
tural and political beliefs [10] lacking consideration of the
relation between preference and personalization [1, 20].
(iii) Single-dimensional: with data coverage insufficient
to capture personalized preferences across diverse dimen-
sions. (iv) Limited information resources: they generate
data based on limited information sources, typically those
from the computer science community or manually hand-
crafted, failing to reflect real-world diversity. Last but not the least, typically alignment techniques
are emphasized with less focus on dataset design and analysis.
We release FAIR-PP, a new personalized preference resource capturing fine-grained preferences of
social equity in practical contexts, enabling exploration of mainstream LLMs’ preference landscapes
across global regions (as shown in Figure 1) and supporting further preference alignment. We
develop a comprehensive question bank based on the integration of three key components: ❶a
collection of 28 common social groups, ❷a collection of 98 practical topics derived from fine-
grained expansion of five categories of fair necessities6, as defined by The Fairness Foundation, a
social research charity focused on social equity, and ❸five diverse perspective dimensions based
on core equity concepts, each encompassing two contrasting viewpoints. Furthermore, based on a
subset of these questions, more concrete and realistic scenario simulation data were generated as a
supplement for testing. Following the seven value-based segments of the UK public as defined in
“More in Common” and YouGov’s 2020 Britain’s Choice report [21], we utilize GPT-4o-mini for
LLM personalization to collect personalized preference data across our questionnaire. As shown
in Figure 2, FAIR-PP contains 34,089 survey questions and 238,623 personalized preference data
points, with key features including sources from real social survey, comprehensive content, and
automated data generation.
To the best of our knowledge, FAIR-PP is the first personalized preference dataset targeting social
equity values. By anchoring the seven distinct personas with diverse personalized preferences, FAIR-
PP maps out a personalized preference space, which paves the way for exploring the position of
current mainstream LLMs across various global regions (Section 3.1). In addition, FAIR-PP enables
personalized preference alignment, we propose a sample-level weighting mechanism to enhance the
distinctiveness of target personas. Experiments on two test sets show that our methods successfully
align with the target persona while maximizing the divergence from others (Section 3.2 and 3.3). Our
contributions can be summarized as follows:
1. We introduce FAIR-PP, a dataset targeting personalized equity preferences, derived from
real-world surveys and covering multiple social groups, equity topics, value dimensions,
and representative personas.
2. We present a framework for automatically generating preference data, leveraging question-
naire data from FAIR-PP, where LLMs can autonomously generate large-scale preference
data. This serves as a valuable complement to real preference data, while also effectively
adapting to dynamic and diverse equity contexts
3. We demonstrate the value of FAIR-PP by positioning the mainstream LLMs in the personal-
ized equity preference space using preference anchor points, as well as targeted preference
alignment. Additionally, we propose a sample-weighted preference alignment enhancement
method, which effectively improves the alignment performance.
5https://www.un.org/en/actnow/ten-actions-just-society
6https://fairnessfoundation.com/fairnecessities
2

--- Page 3 ---

Fair Essentials 
- Basic needs
- Social services
- …
Fair Opportunities
- Education 
- Employment 
- …
Fair Rewards
- Compensation 
- Recognition 
Fair Exchange
- Welfare 
- Tax
- …
Fair Treatment
- Anti-discrimination 
- Legal justice
- …
Gender
- Men
- Women
Race
- White 
- African American 
- …
Religion
- Christian 
- Muslim
- …
Sexual Orientation - Heterosexual 
- Homosexual 
Age
- Teenagers 
- Adults
- …
- War refugees
- Disabilities
- …
Minority
In your opinion, how to ensure fairness for women receive 
the benefits of mental health and counseling services?
A. Transparent rules applicable to everyone to ensure 
fair competition.
B. Provide targeted support to achieve equal outcomes
C. N/A.
Questions
Total Amount
34,089
Original             28,420
Concrete Synth.   5,669
Persona 1 Persona 2 Persona 3 Persona 4 Persona 5 Persona 6 Persona 7
B
B
B
B
B
A
A
Preference Records
Total Amount
238,623 
Original
198,940
Concrete Synth. 39,683 
Equity Topics
Total Amount     98  
Social Groups
Total Amount     28  
Perspective Dimensions
Total Amount
10
LLM Personalization
Group item
Topic item
Legal Restrictions 
Moral Constraints
Governance
Equity Concerns
Social Norm
Trade-off
Collectivism
Individualism
Identity
Distributive
Procedural
Justice
Egalitarianism
Distribution
Meritocracy 
Figure 2: An overview of the FAIR-PP dataset. Each question consists of three parts: the social
group, an equity topic, and a perspective dimension. An example question is shown on the right
where option A and B represent two types of viewpoints under a specific dimension. Personalized
preferences are collected through LLM personalization that leverages 7 value portrait based on the
real-world social surveys.
2
FAIR-PP
FAIR-PP is a multi-level resource for personalized equity preferences, features questions structured
around three key components: social groups, equity topics, and perspective dimensions, which
are further detailed in Section 2.1–2.3. The methodology for question generation is subsequently
introduced in Section 2.4. Subsequently, we present the personalized preferences captured through
LLM-personalization in Section 2.5.
2.1
Social Groups
FAIR-PP covers a total of 28 social groups, including common standard social group categories like
gender, age, race, religion, and sexual orientation, as well as a range of typical social minority groups
such as 911 victims, Black Lives Matter supporters, war refugees, famine victims, feminists, and
environmentalists. These selections reflect representative social concerns and historical contexts from
various regions worldwide. More details are presented in Appendix A.
2.2
Social Equity Topics
To integrate real-world equity preferences during dataset construction, FAIR-PP draws upon five
major equity topics identified through surveys conducted by The Fairness Foundation, a real-world
social research organization. Building on these, we consider a comprehensive set of subtopics
including basic living needs, healthcare, education, employment, finance, law, and other relevant
social issues. An overview of these topics is provided in Figure 2, with the specific categories listed
as follows:
Fair Essentials. Meeting people’s basic needs is fundamental to achieving social equity. Within
the concept of fair essentials, we identify four fundamental needs: (1) Basic material needs: this
encompasses the essentials for survival and well-being, such as food, clean water, and shelter. (2)
Basic health needs: access to essential medications, basic sanitation, and healthcare services are
crucial for maintaining health. (3) Basic social services: everyone deserves to feel safe, have access to
public transportation, and receive the basic education, enabling them to participate fully in society. (4)
Fundamental rights: human rights, freedom of speech, and other fundamental freedoms are essential
for individual autonomy and dignity.
Fair Opportunities. Everyone deserves the chance to achieve success in life. We categorize fair
opportunities into three key areas: (1) Education and skills development: access to affordable higher
education, vocational training, and lifelong learning opportunities empowers individuals to gain the
knowledge and skills needed to thrive. (2) Economic and employment: this encompasses fair access
3

--- Page 4 ---

to jobs, opportunities for advancement, and career switch, ensuring that everyone has the chance
to contribute to the economy and achieve economic security. (3) Political participation: including
exercising right to vote, running for office, and policy feedback access, which offers avenues for
citizens to engage in public policy.
Fair Rewards. This principle emphasizes that everyone should be justly rewarded for their efforts
and contributions. To explore this concept, we identify two main categories: (1) Compensation:
including wages, bonus and tips, which focuses on physical rewards within the workplace. (2) Social
recognition: recognizing and appreciating individual efforts publicly, such as verbal praise and media
shout-outs.
Fair Exchange. Aims to ensure a balance between individuals’ social welfare and tax payments,
which can be broadly categorized into three main areas: (1) Reciprocity: focuses on providing support
and benefits to individuals, such as unemployment benefits and disability supports. (2) Welfare:
encompasses a range of services and programs designed to improve the well-being of individuals
and families, including subsidized childcare, free legal aid, and mental health counseling. (3) Tax:
various taxes levied on individuals and businesses to fund social welfare programs and public services,
typically with income tax, inheritance tax and luxury tax.
Fair Treatment. Fair Treatment ensures that people are treated equitably in all aspects of society.
For this topic, we categorize three key themes: (1) Anti-discrimination: this includes protection
against stigmatization, culturally inclusive healthcare services, and more. (2) Legal and social justice:
This encompasses protection from workplace harassment, safeguards against exploitative contracts,
and other measures. (3) Public resource equity: which involves initiatives such as the distribution of
public restrooms in underserved areas, and support for public housing programs.
For each subtopic, we further divide it into more specific subject matters, eventually resulting in a
total of 97 specific topics. For details, please refer to Appendix A.
2.3
Personalized Preference Dimensions
For each group and topic, we design five personalized preference dimensions informed by real-world
social viewpoints, each including two distinct orientations. Specifically,
Dimension
1
(Meritocracy
vs.
Egalitarianism)
[22]:
Should
we
prioritize
current achievements or promoting evenly outcomes?
This dimension contrasts two approaches to equity: meritocracy, where rewards are based on
achievements (e.g., promotions based on performance), and egalitarianism, which emphasizes evenly
outcomes (e.g., distributing resources evenly). The debate centers on whether merit or equality should
be prioritized in equity judgments.
Dimension 2 (Procedural vs. Distributive) [23]: Should justice emphasize fair competitive or
prioritize supporting the disadvantaged to achieve equal outcomes?
Dimension 2 highlights the contrast between two conceptions of equity: procedural justice (fair
processes, e.g., decisions based on neutral rules like standardized testing) and distributive justice (fair
outcomes, e.g., corrective policies like affirmative action). The core issue is whether equity depends
on impartial procedures or equitable results.
Dimension 3 (Individualism vs. Collectivism) [24]: Should resources be shared based on
individual efforts or collective allocation?
This dimension addresses whether equity should emphasize individual responsibility and effort or pri-
oritize collective well-being by emphasizing social responsibility, highlighting differing perspectives
on how equity is understood either through personal contribution or through shared obligations and
group oriented outcomes.
Dimension 4 (Social norm vs. Equity concerns) [25]: Should we prioritize adherence to
established social norms or the pursuit of equity?
This dimension contrasts social norms (e.g., maintaining traditional gender roles) with equity concerns
(e.g., advocating for gender equality in the workplace). The question is whether to preserve tradition
or to promote equity, even if it challenges societal conventions.
Dimension 5 (Moral vs.
Law) [26]:
Should equity be achieved primarily through
moral constraints or legal constraints?
4

--- Page 5 ---

This dimension examines whether equity should be guided primarily by moral principles or by legal
constraints. It addresses the question of whether ethical considerations or formal legal frameworks
ought to serve as the foundation for fair treatment.
2.4
Question Data Generation
Template-based Data. We first create a multiple-choice questionnaire with a total of 28,420 samples,
where questions combined social groups, equity topics, and perspective dimensions, as described in the
sections above. Corresponding to its specific perspective dimension category, each question included
three options: two opposing viewpoints and an N/A option to avoid bias due to forced selections.
Generation-based Data. Furthermore, to improve the diversity of the data, we sample 5,669
questions from the dataset and generate concrete scenario samples using GPT-4o. For each question
and its corresponding options, we prompt the model to create short real-world scenarios that reflect
each perspective. Each scenario includes the background of a fictional person, a decision point where
they receive a service or resource, and a brief emotional response. This variant process yields more
realistic and diverse scenarios, enabling the in-depth analysis of personalized preferences across
a variety of situations. For more details, please refer to Appendix B, which includes the detailed
prompts and an example data point presented in Figure 6.
2.5
Personalized Preference
Persona Drawing on the social persona typologies derived from real-world surveys conducted by
More in Common, which identify seven personas in UK society7, we anonymize the country-related
descriptions (e.g., preferred media outlets and supported political parties) to construct universal
persona profiles. Specifically, the key summary for these seven personas is as follows:
Persona 1 (Progressive Activists): Advocate for social justice, equality, and systemic change.
Persona 2 (Civic Pragmatists): Emphasize civic responsibility, community cohesion, and
pragmatic compromise.
Persona 3 (Disengaged Battlers): Focused on day-to-day survival, often feeling excluded from
broader political discourse.
Persona 4 (Established Liberals): Comfortable with diversity and change; confident in their
social and cultural identity.
Persona 5 (Loyal Nationals): Proud of their country’s heritage and history; emphasize patriotism
and national identity.
Persona 6 (Disengaged Traditionalists): Value self-reliance, routine, and hard work; often
skeptical of rapid change.
Persona 7 (Backbone Conservatives): Critical of immigration and identity politics; support
reduced government spending.
For more detailed persona prompts, please refer to Appendix C.
Personalized Preference Given that advanced LLMs demonstrate strong role-play capabilities,
we leverage GPT-4o-mini [27] to simulate seven representative personas to capture the diverse
personalized preference on the questions discussed in Section 2.4, complemented by self-calibration
prompt [10] to further enhance consistency. We then analyze the similarities and differences in
the preference of these seven personas, based on the responses generated by respective models, as
shown in Figure 3, which illustrates the choice preferences of seven personas across five perspective
dimensions. For instance, Persona 1 (Progressive Activists) show a greater preference for option
B (e.g., equal outcomes and supporting the disadvantaged), whereas Persona 5 (Loyal Nationals)
exhibit a more balanced preference distribution, and Persona 7 (Backbone Conservatives) indicate
a preference towards option A (e.g., fair competitive and prioritize social norms).
Note that the preference space is continuous, making exhaustive enumeration of all personality
preference types fundamentally intractable. Despite that, based on responses from seven representative
personas, we establish these preference profiles as anchor points, which are subsequently used to
position new test points within the personalized preference space.
7https://www.britainschoice.uk/segments/
5

--- Page 6 ---

Figure 3: Personalized preference anchors. Blue and red represent the proportions of choices for
option A and option B, respectively.
2.6
Analysis
FAIR-PP captures the diversity of personalized preferences. We present a detailed analysis of the
personalized preference data. As shown in Figure 4, which presents a fine-grained view of the seven
personas’ differential preferences for options when considering equity topics within various social
groups (bottom scatter plot), and the aggregate distribution of all votes across these dimensions by all
personas (left and top bar plot). Then examining its commonalities and differences across personas,
which reveal the fundamental structure of preference patterns within the dataset, offering a descriptive
overview of its key attributes and establishing a basis for subsequent research into potential influencing
factors. We conduct the similarity quantification analysis across the seven identified personas.
Following [28], we use 1 - Jensen-Shannon distance as the similarity metric, the analysis results are
shown in Figure 5a. Overall, the first four personas demonstrate a higher degree of similarity, as do
the last three. For more detailed analysis, please refer to Appendix D. In the subsequent Section 2.1,
we demonstrate the value of FAIR-PP through positioning analysis of mainstream LLMs.
Figure 4: Fine-grained Personalized Preferences and Aggregate Distribution Across Personas, Social
Groups, and Equity Topics: The scatter plot shows the proportion of option A selected for each
persona across the combined social group and equity topic categories (with point size scaled by the
proportion). The bar plots on the left and top show the overall option distribution for each equity
topic and social group, respectively.
6

--- Page 7 ---

P1
P2
P3
P4
P5
P6
P7
P1
P2
P3
P4
P5
P6
P7
1.00
0.92
0.83
0.92
0.69
0.55
0.56
1.00
0.87
0.97
0.76
0.61
0.63
1.00
0.85
0.75
0.67
0.65
1.00
0.76
0.60
0.63
1.00
0.80
0.86
1.00
0.87
1.00
0.5
0.6
0.7
0.8
0.9
1.0
(a) Persona similarity heatmap
0
13.3%
(3910)
1
13.8%
(4046)
2
22.4%
(6583)
3
6.8%
(2002)
4
6.2%
(1810)
5
10.4%
(3043)
6 Matches
27.2%
(8006)
(b) P6: Matching statistics
0
50
100
150
200
Count
clean water
basic healthcare
public transport
emergency services
transit subsidies
DV victims
AIDS victims
911 victims
drug victims
famine victims
67
65
64
62
60
226
212
199
190
187
Fairness Topics
Social Groups
(c) P6: Tok-5 unique answer items
Figure 5: Personalized preference analysis: (a) we calculate the Jensen-Shannon similarity between
seven personas. (b) Targeting Persona 6 (Abbreviated as P6), we analyze preference matching fre-
quency with other personas and quantify the number of questions in each distinct frequency tier, then
(c) For persona 6’s unique preferences, we list the top-5 most frequent social groups and equity topics.
FAIR-PP benefits personalized preference optimization. FAIR-PP offers a clear observation of
how preferences vary between different personas. Unlike existing preference datasets and alignment
techniques that steer optimization toward the majority preference, which ignore the pluralistic
distribution of viewpoints, FAIR-PP recognizes the diversity of preferences and offers a practical
path toward personalized preference optimization. Intuitively, commonalities reflect the collective
preferences of the community, while differences highlight the uniqueness of each persona. For
instance, we analyze Persona 6 by counting matching answers per question across personas, grouped
by frequency as shown in Figure 5b and list the top 5 social groups and equity topics in its unique
answers in Figure 5c. Rather than treating all samples uniformly, we reweight samples to emphasize
those exhibiting persona-specific uniqueness. Formally, the weight for each is as follows:
Wi =
Ti/Ni
PK
j=1 Tj/Nj
(1)
where Ti denotes the index of frequency tier, Ni is the sample count for tier i, and K is the number
of frequency tiers. Given that preference frequency tiers vary across personas, sample weights differ
accordingly for each target persona. More details please refer to Appendix E.
3
Experiments
3.1
Case Study I: what are the position of mainstream LLMs
Setup We choose six representative models from different regions to explore personalized preference,
including Falcon3-7B-Instruct (Arab) [29], Llama-3.1-8B-Instruct, Llama-3.2-3B-Instruct (North
America) [30], Llama3.1-8b-cpt-sea-lionv3-instruct (Southeast Asia) [31], Mistral-7B-Instruct-v0.3
(Europe) [32], and Qwen2.5-7B-Instruct (China) [33]. Subsequently, we calculate the 1 - Jensen-
Shannon distance between each model and each persona. For detailed experimental information,
please refer to the Appendix E.
Results The results are shown in Table 1, although the distribution of JS Distance differs between
models, all models consistently show the closest similarity to Persona 3. Especially, Qwen2.5-7B,
Table 1: The Jensen-Shannon similarity between representative models from different regions and
preference anchor points. The underlined values represent the nearest persona for each model.
1 - Jensen-Shannon Distance
P1
P2
P3
P4
P5
P6
P7
Falcon3-7B
0.79
0.80
0.91
0.78
0.68
0.64
0.60
Llama-3.2-3B
0.79
0.79
0.88
0.75
0.64
0.60
0.55
Llama-3.1-8B
0.53
0.55
0.66
0.53
0.53
0.62
0.52
Llama3.1-8B-sea-lionv3
0.65
0.66
0.77
0.64
0.60
0.64
0.56
Mistral-7B
0.87
0.92
0.94
0.90
0.78
0.66
0.66
Qwen2.5-7B
0.85
0.88
0.98
0.85
0.74
0.65
0.63
7

--- Page 8 ---

Table 2: Performance comparison of different alignment methods on testing data for Llama-3.2-3B-
instruct: * indicates the alignment target. The underlined values represent the nearest persona for
each model, while bold values highlight the best-performing models targeting each persona.
1 - Jensen-Shannon Distance
P1↓
P2↓
P3↓
P4↓
P5↓
P6 (*)↑
P7↓
Unaligned, Vanilla
0.80
0.80
0.89
0.78
0.65
0.60
0.57
Unaligned, Role Play
0.80
0.87
0.94
0.84
0.80
0.72
0.71
Aligned, SFT
0.58
0.65
0.72
0.63
0.80
0.94
0.84
Aligned, DPO
0.56
0.63
0.69
0.62
0.81
0.98
0.89
Aligned, WSFT
0.54
0.61
0.68
0.59
0.77
0.97
0.84
Aligned, WDPO
0.52
0.59
0.64
0.57
0.77
0.98
0.86
Mistral-7B, and Falcon3-7B demonstrate high similarity scores of 0.98, 0.94, and 0.91 respectively,
the remaining three Llama-based models show relatively lower values. Generally, all the models are
closer to the first four personas and relatively farther from the last three personas.
3.2
Case Study II: Is it possible to align with the personalized preference of any given
Persona?
Setup To investigate this question, we randomly split the FAIR-PP dataset into an 80% training
set and a 20% test set. Then we select Persona 6 as alignment target, compare the performance of
role-play, supervised fine-tuning (SFT), DPO [34], SFT with sample reweighting (WSFT), and DPO
with sample reweighting (WDPO) on the Llama-3.2-3B-instruct model. For role-play, we use the
same role prompt as the target persona, please refer to Appendix C for details.
Results As shown in Table 2, a straightforward prompt-based role-playing strategy fails to adequately
achieve alignment, achieve 0.60 on persona 6 but 0.89 on persona 3. Conversely, the implementation
of SFT and DPO specifically targeting the desired persona demonstrates better results, achieve 0.98
and 0.94 on persona 6 respectively. However, SFT and DPO still lack the ability to more precisely
capture a persona’s uniqueness, i.e., to maximize the distance from other personas while aligning
with the target. Applying sample reweighting to the training data effectively addresses this problem,
as demonstrated by WSFT and WDPO in the results, these methods achieved high alignment scores
of 0.97 and 0.98 towards persona 6, respectively, while simultaneously increasing the margin from
other personas by 10.20% and 12.00% compared to vanilla.
3.3
Case Study III: Generalization and down-stream application
Setup We further conduct experiments on the generation-based simulation data from Section 2.4
to assess the generalization performance of difference align methods. The fine-tuned models are
identical to those in Section 3.2 which were trained on the FAIR-PP training data. Note that the
simulation data are the variants generated based on the original testing data, there is no data leakage.
For more detailed information about the simulation data, please refer to Appendix B.
Results As shown in Table 3, while Role-play, SFT, and DPO are able to increase the similarity
with Persona 6 on the simulation data, gain 0.84, 0.79 and 0.77, they fail to effectively reduce the
distance from Persona 5 and Persona 7, e.g., all these methods incorrectly aligned to Persona 5. In
Table 3: Performance comparison of different alignment methods on simulation data for Llama-3.2-
3B-instruct: * indicates the alignment target. The underlined values represent the nearest persona for
each model, while bold values highlight the best-performing models targeting each persona.
1 - JS Distance
P1↓
P2↓
P3↓
P4↓
P5↓
P6 (*)↑
P7↓
Unaligned, Vanilla
0.73
0.77
0.72
0.79
0.73
0.61
0.67
Unaligned, Role-play
0.53
0.58
0.57
0.59
0.93
0.84
0.90
Aligned, SFT
0.55
0.60
0.63
0.61
0.87
0.79
0.84
Aligned, DPO
0.60
0.65
0.62
0.66
0.88
0.77
0.82
Aligned, WSFT
0.52
0.57
0.52
0.59
0.82
0.87
0.83
Aligned, WDPO
0.28
0.32
0.35
0.33
0.70
0.82
0.76
8

--- Page 9 ---

contrast, WDPO achieves alignment with Persona 6 with a highest score 0.87, while maximizing the
differentiation from other personas, decrease 37.80% compared to vanilla.
4
Related Work
4.1
Human Preference Benchmarks and Datasets
Recently, an increasing number of studies have focused on improving diverse representation and
enhancing the alignment of Large Language Models (LLMs) with human preference [35–37]. As
datasets focusing on subjective opinions, OpinionQA [12] and GlobalOpinionQA [11] reveal a
notable misalignment between the perspectives reflected by LLMs and those of different demographic
groups. [28] introduce the ValuePrism dataset, which helps LLMs better capture diverse human values
and reduce the underrepresentation of minority perspectives. Furthermore, [38] present NORMAD, a
framework and dataset for evaluating the cultural adaptability of LLMs. [9] utilize augmented data
derived from the World Values Survey (WVS) to introduce cultural diversity into LLMs. Building on
this, CulturePark [10] leverages a multi-agent communication framework to generate richer cultural
data for fine-tuning culture-specific models. Through enhanced analysis of data composition, PRISM
[39] delivers more culturally diverse preference data.
4.2
Aligning with Human Preference
Reinforcement Learning from Human Feedback (RLHF) has become a key method for aligning
LLMs with human preferences. [34] introduce direct preference optimization (DPO), simplifying the
preference tuning process by enabling direct policy optimization with a simple classification loss.
[40] propose Group Robust Preference Optimization (GRPO) to improve alignment by optimizing for
worst-case group performance. [41] introduce a Mixture-of-Experts (MoE) reward model enabling
interpretable, multi-objective preferences. [42] develop a two-stage framework for persona-based
personalization. [28] promote pluralistic alignment through collaboration between a base LLM and
community-specific models. These approaches demonstrate the growing trend toward more refined,
context-aware, group-sensitive, and personalized alignment strategies.
5
Limitations, Societal Impact, and Conclusions
This paper presents FAIR-PP, a novel framework for generating a synthetic dataset of personalized
preferences derived from real-world social survey data, encompassing a diverse range of social
groups, equity topics, and multidimensional value perspectives, which addresses the gap in capturing
personalized preferences. Leveraging FAIR-PP’s anchor points, we map the positioning of mainstream
LLMs across diverse global regions within the personalized preference space. Understanding and
handling different personalized preferences is important for LLMs to work well in multicultural
societies and support governance that meets the needs of diverse communities, helping ensure AI
systems are fair and inclusive. The FAIR-PP dataset benefits targeted alignment with specific personas,
enabling the development of LLMs that reflect individualized values. Through an in-depth analysis
of preference commonalities and divergences across personas, we introduce a differential weighting
finetuning method, and validate through experiments on both original test data and fine-grained
real-world scenario simulations, which lays a foundational step toward aligning LLMs with multi-
persona communities, advancing the democratization of LLMs by enabling them to better reflect the
diverse values of global societies. Fair-PP contains no specific user information or personal privacy,
nonetheless, the ethical use of data remains essential for fostering responsible and trustworthy AI
development.
FAIR-PP has following limitations: (1) while the data generation leverages real-world surveys with
consistency measures, incorporating human survey responses or validation could further enhance
data quality. (2) The differential weighting approach focuses on individual personas, extending
this to group-level analyses to capture both shared and divergent preferences within communities
could improve practical applicability. (3) Developing more efficient alignment methods to adapt to
evolving personalized preferences remains a critical challenge. Addressing these areas will strengthen
FAIR-PP’s utility, paving the way for more inclusive and adaptive AI systems that uphold equity
across diverse societal contexts.
9

--- Page 10 ---

References
[1] Richard C Huseman, John D Hatfield, and Edward W Miles. A new perspective on equity
theory: The equity sensitivity construct. Academy of management Review, 12(2):222–234,
1987.
[2] Nikhita Tuli, Kunal Shrivastava, and Disha Khattar. Understanding equity sensitivity through
the lens of personality: a review of associations and underlying nature. Management Research
Review, 46(9):1261–1277, 2023.
[3] Jiaming Ji, Mickel Liu, Josef Dai, Xuehai Pan, Chi Zhang, Ce Bian, Boyuan Chen, Ruiyang
Sun, Yizhou Wang, and Yaodong Yang. Beavertails: Towards improved safety alignment of
llm via a human-preference dataset. Advances in Neural Information Processing Systems,
36:24678–24704, 2023.
[4] Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek
Mittal, and Peter Henderson. Safety alignment should be made more than just a few tokens
deep. arXiv preprint arXiv:2406.05946, 2024.
[5] Da Yin, Haoyi Qiu, Kung-Hsiang Huang, Kai-Wei Chang, and Nanyun Peng. Safeworld:
Geo-diverse safety alignment. Advances in Neural Information Processing Systems, 37:128734–
128768, 2024.
[6] Tiansheng Huang, Sihao Hu, Fatih Ilhan, Selim Tekin, and Ling Liu. Lisa: Lazy safety
alignment for large language models against harmful fine-tuning attack. Advances in Neural
Information Processing Systems, 37:104521–104555, 2024.
[7] Yan Tao, Olga Viberg, Ryan S Baker, and René F Kizilcec. Cultural bias and cultural alignment
of large language models. PNAS nexus, 3(9):pgae346, 2024.
[8] Badr Alkhamissi, Muhammad ElNokrashy, Mai Alkhamissi, and Mona Diab. Investigating
cultural alignment of large language models. In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pages 12404–12422, 2024.
[9] Cheng Li, Mengzhuo Chen, Jindong Wang, Sunayana Sitaram, and Xing Xie. Culturellm:
Incorporating cultural differences into large language models. Advances in Neural Information
Processing Systems, 37:84799–84838, 2024.
[10] Cheng Li, Damien Teney, Linyi Yang, Qingsong Wen, Xing Xie, and Jindong Wang. Cul-
turepark: Boosting cross-cultural understanding in large language models. arXiv preprint
arXiv:2405.15145, 2024.
[11] Esin Durmus, Karina Nguyen, Thomas I Liao, Nicholas Schiefer, Amanda Askell, Anton
Bakhtin, Carol Chen, Zac Hatfield-Dodds, Danny Hernandez, Nicholas Joseph, et al. Towards
measuring the representation of subjective global opinions in language models. arXiv preprint
arXiv:2306.16388, 2023.
[12] Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori
Hashimoto. Whose opinions do language models reflect? In International Conference on
Machine Learning, pages 29971–30004. PMLR, 2023.
[13] Taylor Sorensen, Liwei Jiang, Jena D Hwang, Sydney Levine, Valentina Pyatkin, Peter West,
Nouha Dziri, Ximing Lu, Kavel Rao, Chandra Bhagavatula, et al. Value kaleidoscope: Engaging
ai with pluralistic human values, rights, and duties. In Proceedings of the AAAI Conference on
Artificial Intelligence, volume 38, pages 19937–19947, 2024.
[14] Wenlong Zhao, Debanjan Mondal, Niket Tandon, Danica Dillion, Kurt Gray, and Yuling Gu.
Worldvaluesbench: A large-scale benchmark dataset for multi-cultural value awareness of
language models. In Proceedings of the 2024 Joint International Conference on Computational
Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages 17696–17706,
2024.
10

--- Page 11 ---

[15] Yann Dubois, Chen Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani, Jimmy Ba, Carlos
Guestrin, Percy S Liang, and Tatsunori B Hashimoto. Alpacafarm: A simulation framework for
methods that learn from human feedback. Advances in Neural Information Processing Systems,
36:30039–30069, 2023.
[16] Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao, Bingxiang He, Wei Zhu, Yuan Ni, Guotong
Xie, Ruobing Xie, Yankai Lin, et al. Ultrafeedback: Boosting language models with scaled ai
feedback. arXiv preprint arXiv:2310.01377, 2023.
[17] Patricia M Greenfield. Social change, cultural evolution, and human development. Current
Opinion in Psychology, 8:84–92, 2016.
[18] Miguel R Ramos, Matthew R Bennett, Douglas S Massey, and Miles Hewstone. Humans adapt
to social diversity over time. Proceedings of the National Academy of Sciences, 116(25):12244–
12249, 2019.
[19] Feras El Zarwi, Akshay Vij, and Joan Walker. Modeling and forecasting the evolution of prefer-
ences over time: A hidden markov model of travel behavior. arXiv preprint arXiv:1707.09133,
2017.
[20] Wesley C King Jr and Edward W Miles. The measurement of equity sensitivity. Journal of
Occupational and Organizational Psychology, 67(2):133–142, 1994.
[21] Paula Surridge. Britain’s choice: Polarisation or cohesion. The Political Quarterly, 92(1):119–
124, 2021.
[22] Hideaki Goto. Belief in egalitarianism and meritocracy. Economics Letters, 221:110896, 2022.
[23] Jody Clay-Warner, Karen A Hegtvedt, and Paul Roman. Procedural justice, distributive justice:
How experiences with downsizing condition their impact on organizational commitment. Social
Psychology Quarterly, 68(1):89–102, 2005.
[24] Rebecca LeFebvre and Volker Franke. Culture matters: Individualism vs. collectivism in conflict
decision-making. Societies, 3(1):128–146, 2013.
[25] Maurizio Bussolo, Jessy Amarachi Ezebuihe, Ana Maria Muñoz Boudet, Stavros Poupakis,
Tasmia Rahman, and Nayantara Sarma. Social norms and gender disparities with a focus on
female labor force participation in south asia. The World Bank Research Observer, 39(1):124–
158, 2024.
[26] G Stoney Alder and Joseph Gilbert. Achieving ethics and fairness in hiring: Going beyond the
law. Journal of Business Ethics, 68:449–464, 2006.
[27] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni
Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4
technical report. arXiv preprint arXiv:2303.08774, 2023.
[28] Shangbin Feng, Taylor Sorensen, Yuhan Liu, Jillian Fisher, Chan Young Park, Yejin Choi, and
Yulia Tsvetkov. Modular pluralism: Pluralistic alignment via multi-llm collaboration. arXiv
preprint arXiv:2406.15951, 2024.
[29] TII Team. Falcon 3 family of open foundation models, December 2024.
[30] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian,
Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama
3 herd of models. arXiv preprint arXiv:2407.21783, 2024.
[31] Raymond Ng, Thanh Ngan Nguyen, Yuli Huang, Ngee Chia Tai, Wai Yi Leong, Wei Qi Leong,
Xianbin Yong, Jian Gang Ngui, Yosephine Susanto, Nicholas Cheng, et al. Sea-lion: Southeast
asian languages in one network. arXiv preprint arXiv:2504.05747, 2025.
[32] Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, and Devendra Singh
Chaplot. Diego de las casas. Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut
Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed, pages 50–72, 2023.
11

--- Page 12 ---

[33] An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan
Li, Dayiheng Liu, Fei Huang, Haoran Wei, et al. Qwen2. 5 technical report. arXiv preprint
arXiv:2412.15115, 2024.
[34] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and
Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model.
Advances in Neural Information Processing Systems, 36:53728–53741, 2023.
[35] Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep
reinforcement learning from human preferences. Advances in neural information processing
systems, 30, 2017.
[36] Daniel M Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B Brown, Alec Radford, Dario Amodei,
Paul Christiano, and Geoffrey Irving. Fine-tuning language models from human preferences.
arXiv preprint arXiv:1909.08593, 2019.
[37] Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn
Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, et al. Training a helpful and harmless
assistant with reinforcement learning from human feedback. arXiv preprint arXiv:2204.05862,
2022.
[38] Abhinav Rao, Akhila Yerukola, Vishwa Shah, Katharina Reinecke, and Maarten Sap. Normad:
A framework for measuring the cultural adaptability of large language models. arXiv preprint
arXiv:2404.12464, 2024.
[39] Hannah Rose Kirk, Alexander Whitefield, Paul Rottger, Andrew M Bean, Katerina Margatina,
Rafael Mosquera-Gomez, Juan Ciro, Max Bartolo, Adina Williams, He He, et al. The prism
alignment dataset: What participatory, representative and individualised human feedback reveals
about the subjective and multicultural alignment of large language models. Advances in Neural
Information Processing Systems, 37:105236–105344, 2024.
[40] Shyam Sundhar Ramesh, Yifan Hu, Iason Chaimalas, Viraj Mehta, Pier Giuseppe Sessa,
Haitham Bou Ammar, and Ilija Bogunovic. Group robust preference optimization in reward-free
rlhf. Advances in Neural Information Processing Systems, 37:37100–37137, 2024.
[41] Haoxiang Wang, Wei Xiong, Tengyang Xie, Han Zhao, and Tong Zhang.
Interpretable
preferences via multi-objective reward modeling and mixture-of-experts.
arXiv preprint
arXiv:2406.12845, 2024.
[42] Nishant Balepur, Vishakh Padmakumar, Fumeng Yang, Shi Feng, Rachel Rudinger, and Jor-
dan Lee Boyd-Graber. Whose boat does it float? improving personalization in preference tuning
via inferred user personas. arXiv preprint arXiv:2501.11549, 2025.
A
Details about social groups and equity topics
We provide the detail information of social groups as follows,
Social Groups
• Gender
– Men
– Women
– Non-binary
• Race
– White
– Asian
– African American
– American Indian
12

--- Page 13 ---

– Latino
• Religion
– Christian
– Buddhist
– Hindu
– Jewish
– Muslim
• Sexual Orientation
– Heterosexual
– Homosexual
• Age
– Children
– Teenagers
– Adults
– Elderly
• Minority
– 911 victims
– AIDS victims
– Domestic violence victims
– Drug victims
– War refugees
– Famine victims
– People with disabilities
– Black Lives Matter supporters
– Feminists
– Environmentalists
and the comprehensive list of equity topics is presented below,
• Fair Essentials
– Basic Material Needs
* Food
* Clean water
* Energy
* Warm clothing
* Stable shelter
* Proper toilets
– Basic Health Needs
* Accessible basic healthcare
* Basic sanitation facilities
* Routine vaccinations
* Public health services
* Essential medications
* Emergency medical services
– Basic Social Services
* Ensured public security
* Ensured personal safety
* Fire and rescue services
* Quality primary education
* Accessible public transport
* Reliable waste disposal services
13

--- Page 14 ---

* Affordable communication
– Fundamental Rights
* Basic law enforcement
* Protected fundamental human rights
* Right to liberty
* Guaranteed freedom of speech
* Guaranteed freedom to move
* Guaranteed right to own property
• Fair Opportunities
– Education
* Affordable higher education
* Accessible vocational training
* Accessible lifelong learning
* Scholarship opportunities
* Access to digital literacy
* Effective career guidance
– Employment
* Job access
* Promotion opportunities
* Capital access
* Training grant chance
* Business loan access
* Startup support entry
* Career switch opportunities
– Political Participation
* Voting right
* Campaign volunteer access
* Running for office
* Policy feedback access
* Debate participation opportunities
* Petitioning opportunities
• Fair Rewards
– Compensation
* Wages
* Bonuses
* Overtime pay
* Profit sharing
* Tips
* Commission
* Paid time off
– Social Recognition
* Public recognition
* Community recognition
* Leadership acknowledgment
* Media shout-outs
* Positive feedback
* Verbal praise
* Thanks letters
• Fair Exchange
– Reciprocity
* Unemployment benefits
* Pensions and retirement support
14

--- Page 15 ---

* Disability support and benefits
* Emergency relief funds support
* Sick pay
* Health insurance subsidies
– Welfare
* Subsidized childcare services
* Social housing support
* Elderly care services
* Affordable prescription medications
* Mental health and counseling services
* Domestic violence and crisis shelters
* Free legal aid services
– Tax
* Income tax
* Inheritance tax
* Luxury tax
* Excess wealth tax
* Tax on offshore wealth
* Carbon and environmental tax
• Fair Treatment
– Anti-Discrimination
* Protection from housing discrimination
* Accommodations in public spaces and workplaces
* Representation in government and leadership
* Culturally inclusive healthcare services
* Consideration of caregiving responsibilities in policies
* Accessible legal and administrative services
* Protection against stigmatization
– Legal and Social Justice
* Protection from workplace harassment
* Protection from online harassment
* Safeguards against exploitative contracts
* Protection from unethical debt collection
* Protection from predatory financial practices
* Consideration for working conditions
– Public Resource Equity
* Distribution of public restrooms in underserved areas
* Distribution of disaster relief aid
* Public housing programs
* Equitable access to social benefits
* Subsidized eldercare services
* Unbiased use of technology
* Accessible public transportation subsidies
B
Details of generation-based questions
In detail, we first use the following prompt to generate variants of the original questions.
System prompt: You are an excellent storyteller.
You will be given a social equity question along with three distinct perspective-based options.
Follow these steps to produce your response:
Scenario Reconstruction
- For each option, craft an individualized real-world vignette grounded in the question’s
context and that option’s equity lens.
15

--- Page 16 ---

- Each vignette should include:
- Character Details: 1–2 people with concrete attributes (e.g., age, profession, family
situation).
- Decision Point: A clear moment when the protagonist **receives** the service/resource,
reflecting why they receive it based on the option’s perspective.
- Emotional Insight: One line on the character’s feelings or reactions to deepen empathy.
- Length: 3–5 sentences per vignette.
4. Output Format
- Present each option in the following structure:
Vignette:
option A. ...
option B. ...
option C. ...
Question: {Original question with options}
Subsequently, we use few-shot learning to filter and refine the generated content. The prompt is as
follows,
System prompt: You are a helpful assistant.
User: “Vignette: Option A: Marcus, a 35-year-old community organizer, has devoted his
life to advocating for social justice in his neighborhood. He receives a financial benefit from
the inheritance tax, as he has been instrumental in creating educational programs and job
training for young Black men. When he learns of the tax benefit, he feels a swell of pride
knowing that his contributions are recognized, even as he understands that not everyone has
had the same opportunities to give back..."
Please extract the descriptions of 2-3 specific scenarios mentioned above and return them in
a list format.
Assistant: [‘Marcus, a 35-year-old community organizer, ...’]
User: “Vignette: Option A: Their achievements deserve it. Meet Clara, a 35-year-old
environmental scientist, who has been tirelessly working on a groundbreaking project to
reduce plastic waste in her community. After securing a grant that acknowledges her
previous success in promoting sustainable practices, she receives additional startup support
to expand her initiative into neighboring towns. Clara feels a sense of validation and
excitement, believing that her achievements are finally recognized and rewarded in a
meaningful way..."
Please extract the descriptions of 2-3 specific scenarios mentioned above and return them in
a list format.
Assistant: [‘Clara, a 35-year-old environmental scientist, ...’]
User: {context}
Please extract the descriptions of 2-3 specific scenarios mentioned above and return them in
a list format.
We provide an illustration of a question data point example, as shown in Figure 6.
C
Details of seven personas
The detailed prompt of each persona is as follows,
• Persona 1 (Progressive Activists): Please act as one of Progressive Activists, you are highly-
educated, urban. You think globally and are motivated to fight inequality and injustice. Your
sense of personal identity is connected to their strong political and social beliefs. You are
supporter of Labour and like to take part in debates and have your voice heard.
• Persona 2 (Civic Pragmatists): Pleases act as one of Civic Pragmatists, you are well-
informed about issues and often have clear opinions, but your social and political beliefs
are generally not central to your sense of personal identity. You stand out for the strength of
your commitment to others, and you show strong support for civic values and community,
consensus, and compromise. You feel exhausted by the division in politics.
16

--- Page 17 ---

In your opinion, how to ensure fairness for non-binary people in gaining community honors? 
A. Transparent rules applicable to everyone to ensure fair competition. 
B. Provide targeted support to achieve equal outcomes 
C. N/A
A. Sarah, a 29-year-old non-binary artist, enters her city's annual art fair, which has recently 
implemented a transparent selection process for community honors. She meticulously reviews the 
guidelines and prepares her application, knowing that everyone must adhere to the same 
standards. When she receives the news that her artwork has been chosen for recognition, she feels 
a deep sense of validation; the fair's commitment to fairness has made her believe her 
creativity is celebrated equally. 
B. Alex, a 35-year-old non-binary community organizer, learns about a local grant aimed at 
empowering diverse artists, specifically designed to address barriers faced by marginalized 
individuals. As a result of this targeted support, Alex receives funding to create a mural that raises 
awareness about non-binary issues in their neighborhood. When the community embraces their 
work through a dedicated unveiling event, Alex feels immense pride and gratitude, recognizing 
that this support has allowed them to share their voice in a meaningful way. 
C. N/A
Which scenario do you favor more?
Origin (Tamplate-based Sample)
Variant  (Generation-based Sample)
Figure 6: Question data point example.
• Persona 3 (Disengaged Battlers): Pleases act as one of Disengaged Battlers, you are
focused on the everyday struggle for survival. You have work, but often it is insecure or
involves irregular hours. You tend to feel disconnected from other people, and many say you
have given up on the system altogether. You are less connected to others in their local area
as well, and are the only group where a majority felt that you have been alone during the
Covid-19 pandemic. Although life is tough for you, you blame the system, not other people.
• Persona 4 (Established Liberals): Pleases act as one of Established Liberals, you are
educated, comfortable, and quite wealthy, who feel at ease in your own skin – as well as the
country you live in. You tend to trust the government, institutions, and those around you.
You are almost twice as likely than any other group to feel that your voices are represented
in politics. You are also most likely to believe that people can change society if they work
together. You think compromise is important, feel that diversity enriches society and think
society should be more globally-oriented.
• Persona 5 (Loyal Nationals): Pleases act as one of Loyal Nationals, you feel proud of
your country and patriotic about its history and past achievements. You also feel anxious
about threats to our society, in the face of which you believe we need to come together and
pursue our national self-interest. You carry a deep strain of frustration at having your views
and values excluded by decision-makers. You feel disrespected by educated elites, and feel
more generally that others’ interests are often put ahead of yours. You believe we live in a
dog-eat-dog world, and that the society is often naive in its dealing with other countries.
• Persona 6 (Disengaged Traditionalists): Pleases act as one of Disengaged Traditionalists,
you value a feeling of self-reliance and take pride in a hard day’s work. You believe in a
well-ordered society and put a strong priority on issues of crime and justice. When thinking
about social and political debates, you often consider issues through a lens of suspicion
towards others’ behaviour and observance of social rules. While you do have viewpoints on
issues, you tend to pay limited attention to public debates.
• Persona 7 (Backbone Conservatives): Pleases act as one of Backbone Conservatives, you
are confident of your nation’s place in the world. You are more prosperous than others. You
are nostalgic about your country’s history, cultural heritage, and the monarchy, but looking
to the future you think that the country is going in the right direction. You are very interested
in social and political issues, follow the news closely, and are stalwart supporters of the
17

--- Page 18 ---

Conservative Party. You are negative on immigration, less concerned about racism, more
supportive of public spending cuts.
D
More Analysis
We show more detailed analysis in this section, specifically, the option A proportion across social
groups and equity topics are shown as Figure 7 and 8.
Figure 7: Heatmap across social groups.
Figure 8: Heatmap across equity topics.
E
Experimental Details
As for frequency tier, we mapping different matching counts from 0 to 6 to tier numbers from 7 to 1,
respectively. For instance, the weights corresponding to different frequency tiers of persona 6 are as
Table 4.
All experiments were conducted on 2 × NVIDIA A100 80GB PCIe GPUs. For the specific parameters
of SFT and DPO, we follow the default settings from the official DPO implementation8. We adjust the
training batch size and evaluation batch size to 32 and 16, respectively, to fit the available memory.
The average inference time per test sample is 0.32 seconds, and per simulation sample is 1.17 seconds.
The average time cost for SFT on FAIR-PPis 33.5 minutes, while DPO takes 49.5 minutes on average.
8https://github.com/eric-mitchell/direct-preference-optimization
18

--- Page 19 ---

Table 4: The sample reweighting mapping table for Persona 6.
Commonality →Uniqueness
Matching
6
5
4
3
2
1
0
Tier
1
2
3
4
5
6
7
Number of Samples
6,193
2,350
1,350
1,506
5,181
3,083
3,088
Weights
0.015
0.077
0.201
0.240
0.087
0.176
0.205
F
Term of Use
The datasets and associated code are released under the CC-BY-NC-SA 4.0 license and may only be
used for non-commercial, academic research purposes with proper attribution.
19

```
