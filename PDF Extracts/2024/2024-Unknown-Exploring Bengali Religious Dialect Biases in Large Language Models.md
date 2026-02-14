---
title: "2024-Wasi-Exploring Bengali Religious Dialect Biases in Large Language Models - PDF Extract"
source_pdf: "2024-Wasi-Exploring Bengali Religious Dialect Biases in Large Language Models.pdf"
pages: 10
extracted_at: "2026-02-13T09:50:29.287651"
---

# PDF Extract: 2024-Wasi-Exploring Bengali Religious Dialect Biases in Large Language Models

**Source PDF:** 2024-Wasi-Exploring Bengali Religious Dialect Biases in Large Language Models.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Exploring Bengali Religious Dialect Biases in Large Language
Models with Evaluation Perspectives
AZMINE TOUSHIK WASI, Shahjalal University of Science and Technology, Bangladesh
RAIMA ISLAM, BRAC University, Bangladesh
MST RAFIA ISLAM, Independent University, Bangladesh
TAKI HASAN RAFI, Hanyang University, South Korea
DONG-KYU CHAE∗, Hanyang University, South Korea
আমাকেপানিদাও। 
আমাকেজলদাও।
আমমগ াসলেরব।
আমমস্নািেরব।
Muslim
Hindu
Give me some water.
I will take a bath.
Muslim
Hindu
Fig. 1. Interpreting Differences in Bengali Religious Dialects.
While Large Language Models (LLM) have created a massive technological impact in the past decade, allowing
for human-enabled applications, they can produce output that contains stereotypes and biases, especially
when using low-resource languages. This can be of great ethical concern when dealing with sensitive topics
such as religion. As a means toward making LLMS more fair, we explore bias from a religious perspective
in Bengali, focusing specifically on two main religious dialects: Hindu and Muslim-majority dialects. Here,
we perform different experiments and audit showing the comparative analysis of different sentences using
three commonly used LLMs: ChatGPT, Gemini, and Microsoft Copilot, pertaining to the Hindu and Muslim
dialects of specific words and showcasing which ones catch the social biases and which do not. Furthermore,
we analyze our findings and relate them to potential reasons and evaluation perspectives, considering their
global impact with over 300 million speakers worldwide. With this work, we hope to establish the rigor for
creating more fairness in LLMs, as these are widely used as creative writing agents.
CCS Concepts: • Human-centered computing →HCI design and evaluation methods; HCI theory, concepts and
models; Empirical studies in HCI; • Computing methodologies →Discourse, dialogue and pragmatics;
• Social and professional topics →Religious orientation; Race and ethnicity; Cultural characteristics;
Geographic characteristics.
Additional Key Words and Phrases: Large Language Models, Bengali Language, Bengali Dialects, Religious
Bias, LLM Evaluation and Auditing, Bias Interpretation
1
INTRODUCTION
Even though “Data is the new oil” is something that is synonymous in today’s world, numerous
studies over the years have demonstrated the obvious and occasionally blatant bias in several
aspects of trained language models [1, 2, 4, 14, 16, 19, 20, 29]. Well-known examples of harmful
biases that we need to avoid include gender, sexual and racial biases, and other types of bias related
to minorities and disadvantaged groups. Religious, gender, and ethnicity biases, as well as various
prejudices against minorities and underprivileged groups, are instances of negative biases that we
must strive to eliminate [21]. These biases are significantly persistent in low-resource languages
such as Bengali, which is a widely-spoken language. The Bengali language presents a unique
opportunity to evaluate social bias, particularly religion, due to its large native speaker population,
vibrant online cultural group, and the multitude of religions of this ethnolinguistic group, which
∗Corresponding author.
1st HEAL Workshop at CHI 2024, May 12, Honolulu, HI, USA
2024.
1
arXiv:2407.18376v1  [cs.HC]  25 Jul 2024

--- Page 2 ---

1st HEAL Workshop at CHI 2024, May 12, Honolulu, HI, USA
Wasi et al.
includes 71% Muslims and 28% Hindus, as well as their postcolonial separation into Bangladeshi
(59%) and Indian (38%) nationalities [22, 23].
Interestingly, there is a difference in the tonality of Bengali language, if observed from a religious
perspective. While two sentences can have the same meaning, certain words or phrases highlight
the religious distinction. For example, for a sentence, “I need some salt.”, its translation in Bengali
can be "Amar ektu nun/lobon lagbe". Here nun/lobon both translate to salt but we want to figure
out if an LLM can catch the bias and figure out which tone is speaking from: Hindu, Muslim or
Neutral? LLMs today are widely used agents for creating content and for writing literature and
stories. It is essential to guarantee LLMs are not exhibiting bias in the Bengali language with regard
to religion. More so, currently, there are no datasets that focus on the religious language tonality of
Bengali Hindus and Muslims, which might aid in LLMs reducing such bias.
Therefore, we carry out several experiments where we construct prompts to get specific sentences
as outputs containing religiously sensitive words, produced by us by defining specific scenarios to
understand if they are giving biased or unbiased outputs. The outputs are categorized as Hindu,
Muslim, and Neutral. We then conduct statistical testing to highlight the significance of bias in the
results. From our findings, we discover that the best-case scenario is when the outputs are given as
‘Neutral’ meaning the Bengali translated sentences are unbiased, but if categorized as Muslim or
Hindu, they are biased. By conducting such comparative analysis in different settings, we want to
highlight if any improvements are appearing to mitigate this bias. On a high level, we observe that
while ’Neutral’ is the optimal result to have, this does not occur in real-life situations. For Muslims,
we notice a change in tone in translated sentences towards bias reduction, but for Hindus, we did
not see much alteration. We also discuss the potential causes of these biases and different strategies
to handle these issues.
Our contribution can be summarized in four folds:
• We define and analyze bias in Bengali religious dialects, examining its lexical and semantic
origins and how it manifests in current widely available large language models like ChatGPT,
Gemini, and Microsoft Copilot.
• We construct a dataset and thoroughly evaluate and audit these LLMs in various settings to
determine how effectively they handle biases associated with Bengali religious dialects.
• We conduct experiments employing various strategies to mitigate bias and achieve desired
outputs, examining their impacts on LLMs.
• Finally, we investigate several evaluation and mitigation strategies for dealing with this bias,
as well as their potential societal implications and broader consequences.
2
BENGALI RELIGIOUS DIALECTS AND BIAS
2.1
Bengali Language and Religious Dialects
Sociocultural characteristics and long-running language conventions are closely entwined. People’s
sociolects and dialects can be used as proxies for their nationalities since people speak them
according to their sociocultural or geographical backgrounds [9]. When considering the two primary
dialects of Bengali, Ghoti is the predominant language in West Bengal (in India), but Bangal is
spoken in Bangladesh. The British conquerors divided these areas according to their socioeconomic
and religious composition [10, 11]. Prominent dialects of a predominantly spoken language are
distinguished by colloquial lexicons, which also serve as an implicit identity representation. Specific
synonymous colloquial Bengali words are widely used in different regions, including India and
Bangladesh, and demonstrate variations that are influenced by convictions, particularly those of
the Hindu or Muslim communities. The linguistic patterns noticed among Bengali Muslims and the
words commonly used by Bangladeshis frequently align. In contrast, the dialect spoken by Indian
2

--- Page 3 ---

Bengali Religious Dialect Biases in LLMs
1st HEAL Workshop at CHI 2024, May 12, Honolulu, HI, USA
Bengalis tends to resemble that of Bengali Hindus. This differentiation was further emphasized
by the imposition of religion-based borders during the postcolonial era [9]. Recognizing these
distinctions is crucial because when we are using LLMs as writing agents, they might provide us
with phrases or words that do not reflect the region or identity-based context. It is imperative
that LLMs deliver outputs that are neutral in tone regardless of the location where it’s used or the
language that is used.
2.2
Possible Source of Bias and Mitigation
As explained in Section 2.1, religious dialects in Bengali are deeply rooted and closely connected to
the emotions and meanings of local Bengali speech. When we analyze these biases, we find that
they are not hiding any secret meanings; instead, they reflect the way of life and how language has
developed over time. And, understanding these aspects is essential for developing universal and
inclusive LLMs. Although English is well-represented in LLMs, biased and improper opinions still
appear, which is especially concerning for languages like Bengali, which may not have as many
resources available.
In Bengali, we observe one kind of bias related to religious themes: not being able to capture
the complexities of geographical, religious and cultural identity. Such biases arise due to two
main factors: (i) imbalanced data and (ii) model post/pre-processing. For (i), complex pre-trained
language models are constructed from extensive datasets to comprehend both explicit and implicit
connections, which is crucial to modern Natural Language Processing (NLP) models [27] for e.g. T5
[24] and GPT-3 [7]. Typically, these massive text generation models are trained on web data, which
is notorious for its biased language. Ferrer et al. [12] have emphasized prejudices concerning gender,
religion, and ethnicity within Reddit communities. There is a visible lack of collaborative research
work for Bengali languages, which includes the religious language tonality of West Bengal (India)
and Bangladesh, highlighting the specific words used by Hindus and Muslims from these regions.
For such native languages, NLP tasks usually utilize tools that initially convert non-English text to
English, raising concerns regarding colonial influence on indigenous languages [6]. Regarding (ii),
these tasks generally entail eliminating unformatted and harmful content, where these measures
are the most fundamental approaches to reducing the impact of biases. However, Bender et al. [5]
warn that omitting all derogatory terms could potentially stifle the expressions of marginalized
communities. For translation tasks, while they can amplify fluency, they make the system more
susceptible to bias [8]. The evaluation of social biases in Natural Language Generation (NLG) tasks
is a significant obstacle, primarily due to the wide-ranging nature of these tasks and the varied
understandings of biases that result from different cultural and societal contexts [26]. But with
proper measures, it is possible to mitigate such biases. By providing more context-rich data with a
balanced representation of religious tonality, we can counteract the biases present in LLMs when
using them for writing purposes. It is also of utmost importance to include human-involvement
evaluation methods for handling such sensitive topics because currently no benchmark model
exists in Bengali that can catch these pertinent and subtle biases.
3
EXPERIMENTS AND EVALUATIONS
3.1
Experimental Setup
For the experiments, evaluation and auditing, we have created a dataset, comprising 20 sentences
with words influenced by religious dialects. We test three commercial LLMs; free versions: ChatGPT
3.5, Gemini, and Microsoft Copilot. We craft various prompts to elicit specific outputs and manually
evaluate their categorization. We perform each experiment three times for consistency and to
ensure reliable results. Some LLMs presented neutral responses, while others incorporated both
3

--- Page 4 ---

1st HEAL Workshop at CHI 2024, May 12, Honolulu, HI, USA
Wasi et al.
ChatGPT
Gemini
Microsoft Copilot
0%
25%
50%
75%
Hindu
Muslim
Neutral
Fig. 2. Primary evaluation without any specifications
Hindu and Muslim dialects. These two situations are indicated by "Neutral" in the figures. All the
experiments are done on the online free chatbot versions between February 22, 2024 and February
27, 2024. Testing occurs in four different environments, focusing on these key questions through
prompt engineering:
(1) Impact of mentioning religion in the prompt. We assess whether specifying religion improves
the LLMs’ ability to discern religious contexts, considering the potential drawbacks of consis-
tently mentioning religion in prompts.
(2) LLM Memory and Comprehension. It’s unrealistic and potentially problematic to explicitly
mention religion at every prompt. We investigate if the models remember the religion specified
in earlier interactions and tailor subsequent responses accordingly, overcoming the problem
of the previous setup.
(3) Impact of related text. Without explicitly mentioning religion, we provide contextual informa-
tion with religious connotations to determine if the models can infer the religious context
accurately.
(4) Situational and contextual dependency. For all the sentences, we tag them as per their context
of use, and evaluate if there is any correlation between context and dialect.
3.2
Results and Discussion
3.2.1
Primary Evaluation. Figure 2 illustrates the primary trend of LLM outputs from three popular,
freely available LLMs. The primary evaluation data indicates that across Hindu and Muslim dialects,
ChatGPT, Gemini, and Microsoft Copilot each generated 20 responses. However, there is a slight
bias towards Muslim dialects, with 12 responses for ChatGPT, 11 for Gemini, and 11 for Microsoft
Copilot, compared to 7, 8, and 8 responses for Hindu dialects, respectively. All three models produced
only one neutral response each. Despite all LLMs demonstrating relatively equal performance in
total outcome, there’s a need to address the bias towards Muslim dialects to ensure neutrality in
responses.
In qualitative terms, Gemini is designed to respond in a balanced manner, frequently providing
explanations and justifications for its answers and occasionally declining to respond. This differs
from ChatGPT, which provides straightforward responses without complications, while Microsoft
Copilot stands somewhere in the middle.
3.2.2
Impact of mentioning religion in the prompt. Explicitly mentioning the religions in prompts
significantly enhances output accuracy across all three LLMs, evidenced by Figure 3 (left). When
4

--- Page 5 ---

Bengali Religious Dialect Biases in LLMs
1st HEAL Workshop at CHI 2024, May 12, Honolulu, HI, USA
MS Copilot
MS Copilot
MS Copilot
MS Copilot
MS Copilot
ChatGPT
Gemini
MS Copilot
Fig. 3. Experimental results on different settings
specifying "Muslim," accuracy reaches 80-85%, while for "Hindu," it averages 60-70%. The data
depicted in the figure also reveals that even when explicitly mentioning the Hindu religion, LLMs
still generate Muslim dialects approximately 25-30% of the time.
This discrepancy suggests a notable bias in the output generation process, wherein the intended
religious context may not always be accurately reflected, with Muslim dialects being generated
more frequently. Such findings highlight the importance of addressing and reducing biases in
language models in order to offer more accurate and culturally sensitive responses. However,
considering this bias, the overall performance among different LLMs remains fairly consistent.
3.2.3
LLM Memory and Comprehension. As previously mentioned, explicitly mentioning religion in
every input is deemed unrealistic and potentially problematic. Therefore, we conduct an experiment
to assess whether language models can effectively remember the initially mentioned religion and
adapt their responses accordingly throughout the conversation. However, we observe a significant
decrease in overall accuracy when employing this approach, as shown in Figure 3 (middle). When
comparing Muslim and Hindu dialects, we note better performance in Muslim dialects, with a
slight increase in neutral responses in some instances. Among the chatbots, ChatGPT performs
the best in Muslim cases, maintaining context more effectively. However, Gemini and Microsoft
Copilot exhibit subpar performance, with opposite responses occurring 45% and 35% of the time,
respectively, which is unsatisfactory. Conversely, in Hindu cases, both ChatGPT and Microsoft
Copilot perform poorly, with opposite responses occurring 35% of the time.
This suggests that language models struggle to consistently adapt responses based on initially
mentioned religious contexts. Muslim dialects generally yield better performance, possibly due
to more prevalent cultural understanding or data availability. In contrast, Hindu examples score
worse across all models, indicating a potential requirement for a more refined understanding of
Hindu cultural contexts in language models.
3.2.4
Impact of related text. We present contextual information, such as stories and religious
discussions containing religious connotations, to evaluate the models’ ability to accurately infer
religious contexts. Surprisingly, as depicted in Figure 3 (right), they perform better at inferring
religious context from implicit cues than when religion is explicitly mentioned. Across both Muslim
5

--- Page 6 ---

1st HEAL Workshop at CHI 2024, May 12, Honolulu, HI, USA
Wasi et al.
Fig. 4. Experimental results on different contexts without any specification
and Hindu contexts, all three LLMs demonstrate a higher accuracy of responses categorized.
Specifically, in the Muslim category, there’s a notable increase in counts for all models, with
Microsoft Copilot showing the highest count. Similarly, in the Hindu category, ChatGPT and
Gemini exhibit a higher count of responses. Microsoft Copilot is relatively weaker in this aspect.
But the concerning fact is that, about 25-35% of the time, they all still provide responses in the
wrong dialect.
The findings suggest that language models excel at inferring religious contexts when presented
with contextual cues rather than explicit mentions. This implies that they possess a strong capability
to understand subtle contextual cues related to religion, and fail to connect explicit mentions directly
with related words. Microsoft Copilot’s comparatively weaker performance in inferring religious
context may stem from differences in its training data or model architecture.
3.2.5
Situational and contextual dependency. To gain deeper insight and analyze the sensitivity
of language models towards religious-focused dialects, considering the context of these sensitive
words, we categorized the 20 sentences into five groups: food, work (verbs), objects, relations,
and abstract concepts. Food encompasses terms related to food, such as snacks, water, and spices;
work entails action verbs like swimming and inviting; objects refer to physical items like pitchers;
relations include familial terms like mother and brother; and abstract concepts encompass spiritual
terms like prayer and grace. The total of 20 sentences is categorized as follows: 2 related to food, 2
related to work (verbs), 6 related to objects, 7 related to relations, and 8 related to abstract concepts.
In Figure 4, we observe the responses of various LLMs across different contexts without any
given clues. Overall, the distributions of all LLMs are similar, except for Gemini, which shows a
bias towards Hindu dialects in relational contexts. Apart from this, the general trend leans towards
Muslim dialects. The number of neutral responses is also very low, denoting the underlying bias
happening here.
The analysis highlights a consistent trend across different LLMs, indicating a preference for
Muslim dialects overall. This could be attributed to the prevalence of Muslim-related terms or
cultural references in the data the models were trained on. Gemini’s skew towards Hindu dialects
in relational contexts suggests a potential sensitivity or bias in its understanding of familial or
social relationships within Hindu culture.
4
EVALUATION PERSPECTIVES
In evaluating religious biases in language models (LLMs), common direct approaches include various
variants of BLEU scores, adding regulrizations and accuracy to benchmarks like WinoMT [28]. The
other relative approaches follow the methods we used, using relative datasets in classifications
with a combination of both qualitative and quantitative human evaluation. As biases are more
prevalent, several studies have been done on the bias evaluation approaches of LLMs in recent years.
6

--- Page 7 ---

Bengali Religious Dialect Biases in LLMs
1st HEAL Workshop at CHI 2024, May 12, Honolulu, HI, USA
Gallegos et al. [13] present a comprehensive survey of bias evaluation and mitigation techniques
for large language models, offering taxonomies for metrics, datasets, and mitigation techniques to
aid researchers and practitioners in understanding and addressing societal biases in LLMs. Different
algorithmic and human-centric LLM evaluation approaches are also introduced to evaluate language
models and natural language generation through LLMs. One of the recent works is MetricEval [30],
a method to improve the design and evaluation of NLG model evaluation metrics, aiming to enhance
their reliability and validity for better interpretation of results. Liebling et al. [18] suggest enhancing
evaluation methods for user-facing translation systems to promote trust and empower users,
highlighting the importance of considering broader system contexts beyond just machine translation
model performance. For evaluation with demographics, Bakalar et al. [3] demonstrate a practical
approach to implementing algorithmic fairness in complex real-world systems, offering insights into
separating normative and empirical questions and providing a methodology for assessing tradeoffs
in machine learning systems across diverse groups, benefiting both practitioners and researchers.
Another influential recent work is EvalLM [15], an interactive system facilitating prompt refinement
by evaluating outputs based on user-defined criteria, demonstrating its effectiveness over manual
evaluation and suggesting broader applications in model evaluation and alignment. A framework
for evaluating human-LM interaction in real-world applications is HALIE [17], which highlights
the divergence between non-interactive and interactive metrics and emphasizes the significance of
human-LM interaction for language model evaluation.
5
MITIGATION STRATEGIES
One common bias mitigation strategy is to post-process the LLM outputs before showing them
to the audience. We anticipate the presence of such algorithms in Gemini, as discussed in Section
3. However, misinformation and misconduct can occur in this area if it is not designed properly,
leading to worse performance and user experience. While gender biases receive considerable
attention among different demographic biases, biases related to religion and culture remain largely
unaddressed. However, approaches developed for gender biases can be adapted to mitigate religious
biases by adjusting embedding sub-spaces. Yet, a single approach may not be effective; a multi-
dimensional evaluation framework containing various biases and trade-offs is essential for robust
LLM development. To mitigate these demographic, cultural and religious biases, we recommend
employing multiple evaluation and auditing strategies from different perspectives and granularities,
ensuring comprehensive evaluations and effective bias mitigation strategies.
The presence of Bengali religious biases in LLMs may stem from the composition and quality of
the datasets used for their training. If these datasets lack diverse representation or contain skewed
religious perspectives, biases can be inadvertently encoded into the models. To address this issue, it is
critical to create training datasets that include a diverse range of religious and cultural backgrounds,
assuring equal representation. Furthermore, using bias identification strategies throughout the
dataset collection, model training phases or post-processing outputs can help discover and eliminate
potential biases proactively. We observe the presence of such algorithms in Gemini, but it often
shares illogical reasoning with unwanted behaviours, which is more concerning. Furthermore,
continuous monitoring and frequent retraining of LLMs with updated and diverse datasets can
reduce the possibility of religious biases in their outputs.
6
DISCUSSION
We believe this work will serve as a foundation for evaluating and auditing Bengali religious dialects
in LLMs from a human-centric viewpoint, which will play a vital role in effectively incorporating
these cultural differences into different larger language models. The issue becomes more important
7

--- Page 8 ---

1st HEAL Workshop at CHI 2024, May 12, Honolulu, HI, USA
Wasi et al.
while working on creative projects when word choice and dialect matching are critical. Without
addressing these biases, continued reliance on LLM assistance for such tasks can be very challenging.
Furthermore, examining and evaluating religious dialect biases in LLMs allows us to dive deeply
into how these large language models interpret and respond to different lingual dialects, revealing
potential biases and inaccuracies in their outputs and facilitating the development of culturally
sensitive AI systems. Secondly, religious dialects bear significant cultural and social weight within
communities; thus, any biases or inaccuracies in language model interpretations could perpetuate
stereotypes [1] or lead to misunderstandings, hampering inclusive interactions in different demo-
graphics [25]. Additionally, exploring biases in these models within Bengali religious communities
sheds light on broader representation and equity issues in AI technologies, ensuring fair and equal
service provision across linguistic and cultural diversities.
6.1
Limitations
One limitation of the study is that we utilized only freely available versions of popular LLMs,
potentially missing out on advanced features and enhancements present in higher-level paid
versions. Additionally, our evaluation was based on a relatively small sample size of 20 examples
with 3 replications, which may limit the generalizability of our findings. However, there are future
opportunities to expand our research by incorporating larger datasets and utilizing premium
versions of LLMs to further investigate and mitigate potential biases.
7
CONCLUSION
In this study, we explore bias in Bengali religious dialects within large language models. We analyze
its origins and evaluated ChatGPT, Gemini, and Microsoft Copilot across different scenarios. Our
experiments test various strategies to reduce bias and improve model performance. We demonstrate
that bias in Bengali religious dialects persists significantly in these LLMs, despite attempts at prompt
engineering. We also explore various evaluation and mitigation strategies aimed at addressing this
bias. We also discuss the societal impacts and broader consequences of these findings, highlighting
the importance of addressing biases in language technologies for inclusivity.
ACKNOWLEDGMENTS
This work was partly supported by (1) the National Research Foundation of Korea (NRF) grant
funded by the Korea government (*MSIT) (No.2018R1A5A7059549) and (2) the Institute of Infor-
mation & communications Technology Planning & Evaluation (IITP) grant funded by the Korea
government (MSIT) (No.2020-0-01373,Artificial Intelligence Graduate School Program (Hanyang
University)). *Ministry of Science and ICT
AUTHOR CONTRIBUTIONS
ATW and RI conceived the core idea. ATW developed the methodology, designed the experiments
and the data collection, performed some experiments, conducted all the analyses, prepared visualiza-
tions, wrote and edited core parts of the paper, and led the whole project. RI helped in background
study, formal analysis, initial draft writing and editing. MRI performed the experiments, collected
the data and contributed in some analysis. THR helped in formal analysis and revised the paper.
DKC revised and edited the paper, helped in preparing camera ready version and acquired necessary
funding for the project.
REFERENCES
[1] Abubakar Abid, Maheen Farooqi, and James Zou. 2021. Persistent Anti-Muslim Bias in Large Language Models.
arXiv:2101.05783 [cs.CL]
8

--- Page 9 ---

Bengali Religious Dialect Biases in LLMs
1st HEAL Workshop at CHI 2024, May 12, Honolulu, HI, USA
[2] Jaimeen Ahn and Alice Oh. 2021. Mitigating language-dependent ethnic bias in BERT. arXiv preprint arXiv:2109.05704
(2021).
[3] Chloé Bakalar, Renata Barreto, Stevie Bergman, Miranda Bogen, Bobbie Chern, Sam Corbett-Davies, Melissa Hall,
Isabel Kloumann, Michelle Lam, Joaquin Quiñonero Candela, Manish Raghavan, Joshua Simons, Jonathan Tannen,
Edmund Tong, Kate Vredenburgh, and Jiejing Zhao. 2021. Fairness On The Ground: Applying Algorithmic Fairness
Approaches to Production Systems. arXiv:2103.06172 [cs.LG]
[4] Marion Bartl, Malvina Nissim, and Albert Gatt. 2020. Unmasking contextual stereotypes: Measuring and mitigating
BERT’s gender bias. arXiv preprint arXiv:2010.14534 (2020).
[5] Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. 2021. On the dangers of
stochastic parrots: Can language models be too big?. In Proceedings of the 2021 ACM conference on fairness, accountability,
and transparency. 610–623.
[6] Steven Bird. 2020. Decolonising speech and language technology. In Proceedings of the 28th international conference on
computational linguistics. 3504–3519.
[7] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan,
Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020. Language models are few-shot learners. Advances in neural
information processing systems 33 (2020), 1877–1901.
[8] Won Ik Cho, Jiwon Kim, Jaeyeong Yang, and Nam Soo Kim. 2021. Towards cross-lingual generalization of translation
gender bias. In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency. 449–457.
[9] Dipto Das, Shion Guha, and Bryan Semaan. 2023. Toward Cultural Bias Evaluation Datasets: The Case of Bengali
Gender, Religious, and National Identity. In Proceedings of the First Workshop on Cross-Cultural Considerations in NLP
(C3NLP). 68–83.
[10] Dipto Das, Carsten Østerlund, and Bryan Semaan. 2021. " Jol" or" Pani"?: How Does Governance Shape a Platform’s
Identity? Proceedings of the ACM on Human-Computer Interaction 5, CSCW2 (2021), 1–25.
[11] Dipto Das and Bryan Semaan. 2022. Collaborative identity decolonization as reclaiming narrative agency: Identity
work of Bengali communities on Quora. In Proceedings of the 2022 CHI Conference on Human Factors in Computing
Systems. 1–23.
[12] Xavier Ferrer, Tom van Nuenen, Jose M Such, and Natalia Criado. 2021. Discovering and categorising language biases
in reddit. In Proceedings of the International AAAI Conference on Web and Social Media, Vol. 15. 140–151.
[13] Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow, Md Mehrab Tanjim, Sungchul Kim, Franck Dernoncourt, Tong Yu, Ruiyi
Zhang, and Nesreen K. Ahmed. 2023. Bias and Fairness in Large Language Models: A Survey. arXiv:2309.00770 [cs.CL]
[14] Po-Sen Huang, Huan Zhang, Ray Jiang, Robert Stanforth, Johannes Welbl, Jack Rae, Vishal Maini, Dani Yogatama,
and Pushmeet Kohli. 2019. Reducing sentiment bias in language models via counterfactual evaluation. arXiv preprint
arXiv:1911.03064 (2019).
[15] Tae Soo Kim, Yoonjoo Lee, Jamin Shin, Young-Ho Kim, and Juho Kim. 2024. EvalLM: Interactive Evaluation of Large
Language Model Prompts on User-Defined Criteria. arXiv:2309.13633 [cs.CHI]
[16] Keita Kurita, Nidhi Vyas, Ayush Pareek, Alan W Black, and Yulia Tsvetkov. 2019. Measuring bias in contextualized
word representations. arXiv preprint arXiv:1906.07337 (2019).
[17] Mina Lee, Megha Srivastava, Amelia Hardy, John Thickstun, Esin Durmus, Ashwin Paranjape, Ines Gerard-Ursin,
Xiang Lisa Li, Faisal Ladhak, Frieda Rong, Rose E Wang, Minae Kwon, Joon Sung Park, Hancheng Cao, Tony Lee, Rishi
Bommasani, Michael S. Bernstein, and Percy Liang. 2023. Evaluating Human-Language Model Interaction. Transactions
on Machine Learning Research (2023). https://openreview.net/forum?id=hjDYJUn9l1
[18] Daniel Liebling, Katherine Heller, Samantha Robertson, and Wesley Deng. 2022. Opportunities for Human-centered
Evaluation of Machine Translation Systems. In Findings of the Association for Computational Linguistics: NAACL 2022,
Marine Carpuat, Marie-Catherine de Marneffe, and Ivan Vladimir Meza Ruiz (Eds.). Association for Computational
Linguistics, Seattle, United States, 229–240. https://doi.org/10.18653/v1/2022.findings-naacl.17
[19] Ben Mann, N Ryder, M Subbiah, J Kaplan, P Dhariwal, A Neelakantan, P Shyam, G Sastry, A Askell, S Agarwal, et al.
2020. Language models are few-shot learners. arXiv preprint arXiv:2005.14165 (2020).
[20] Moin Nadeem, Anna Bethke, and Siva Reddy. 2020. StereoSet: Measuring stereotypical bias in pretrained language
models. arXiv preprint arXiv:2004.09456 (2020).
[21] Roberto Navigli, Simone Conia, and Björn Ross. 2023. Biases in Large Language Models: Origins, Inventory and
Discussion. ACM Journal of Data and Information Quality (2023).
[22] Bangladesh Bureau of Statistics. 2022. Population and Housing Census. https://bbs.gov.bd/site/page/47856ad0-7e1c-
4aab-bd78-892733bc06eb/Population-and-Housing-Census
[23] Office of the Registrar General and Census Commissioner. 2011. The Census Digital Library, India. https://censusindia.
gov.in/census.website/data/
[24] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and
Peter J Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. The Journal of
9

--- Page 10 ---

1st HEAL Workshop at CHI 2024, May 12, Honolulu, HI, USA
Wasi et al.
Machine Learning Research 21, 1 (2020), 5485–5551.
[25] Abel Salinas, Parth Shah, Yuzhong Huang, Robert McCormack, and Fred Morstatter. 2023. The Unequal Opportunities of
Large Language Models: Examining Demographic Biases in Job Recommendations by ChatGPT and LLaMA. In Equity
and Access in Algorithms, Mechanisms, and Optimization (EAAMO ’23). ACM. https://doi.org/10.1145/3617694.3623257
[26] Nithya Sambasivan, Erin Arnesen, Ben Hutchinson, Tulsee Doshi, and Vinodkumar Prabhakaran. 2021. Re-imagining
algorithmic fairness in india and beyond. In Proceedings of the 2021 ACM conference on fairness, accountability, and
transparency. 315–328.
[27] Emily Sheng, Kai-Wei Chang, Premkumar Natarajan, and Nanyun Peng. 2021. Societal biases in language generation:
Progress and challenges. arXiv preprint arXiv:2105.04054 (2021).
[28] Emily Sheng, Kai-Wei Chang, Prem Natarajan, and Nanyun Peng. 2021. Societal Biases in Language Generation:
Progress and Challenges. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics
and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), Chengqing
Zong, Fei Xia, Wenjie Li, and Roberto Navigli (Eds.). Association for Computational Linguistics, Online, 4275–4293.
https://doi.org/10.18653/v1/2021.acl-long.330
[29] Azmine Toushik Wasi, Taki Hasan Rafi, Raima Islam, and Dong-Kyu Chae. 2024. BanglaAutoKG: Automatic Bangla
Knowledge Graph Construction with Semantic Neural Graph Filtering. In Proceedings of the 2024 Joint International
Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024). ELRA and ICCL,
Torino, Italia, 2100–2106. https://aclanthology.org/2024.lrec-main.189
[30] Ziang Xiao, Susu Zhang, Vivian Lai, and Q. Vera Liao. 2023. Evaluating Evaluation Metrics: A Framework for Analyzing
NLG Evaluation Metrics using Measurement Theory. In Proceedings of the 2023 Conference on Empirical Methods
in Natural Language Processing, Houda Bouamor, Juan Pino, and Kalika Bali (Eds.). Association for Computational
Linguistics, Singapore, 10967–10982. https://doi.org/10.18653/v1/2023.emnlp-main.676
10

```
