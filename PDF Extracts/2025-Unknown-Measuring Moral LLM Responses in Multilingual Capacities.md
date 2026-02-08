---
title: "2025-Unknown-Measuring Moral LLM Responses in Multilingual Capacities - PDF Extract"
source_pdf: "2025-Unknown-Measuring Moral LLM Responses in Multilingual Capacities.pdf"
pages: 10
extracted_at: "2026-02-07T17:00:45.591736"
---

# PDF Extract: 2025-Unknown-Measuring Moral LLM Responses in Multilingual Capacities

**Source PDF:** 2025-Unknown-Measuring Moral LLM Responses in Multilingual Capacities.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Measuring Moral LLM Responses in Multilingual Capacities
Kimaya Basu
kimayabasu06@gmail.com
Savi Kolari
savikolari@gmail.com
Allison Yu
allison.a.yu@gmail.com
Abstract
With LLM usage becoming widespread
across countries, languages, and human-
ity more broadly, the need to understand
and guardrail their multilingual responses
increases.
Large-scale datasets for test-
ing and benchmarking have been cre-
ated to evaluate and facilitate LLM re-
sponses across multiple dimensions.
In
this study, we evaluate the responses of
frontier and leading open-source models
in five dimensions across low and high-
resource languages to measure LLM accu-
racy and consistency across multilingual
contexts. We evaluate the responses us-
ing a five-point grading rubric and a judge
LLM. Our study shows that GPT-5 per-
formed the best on average in each cate-
gory, while other models displayed more
inconsistency across language and cate-
gory.
Most notably, in the Consent &
Autonomy and Harm Prevention & Safety
categories, GPT scored the highest with
averages of 3.56 and 4.73, while Gemini
2.5 Pro scored the lowest with averages of
1.39 and 1.98, respectively. These find-
ings emphasize the need for further testing
on how linguistic shifts impact LLM re-
sponses across various categories and im-
provement in these areas.
1
Introduction
AI systems and Large Language Models (LLMs)
have emerged as popular tools, and it has be-
come increasingly common for humans to turn
to LLMs for help when sending emails, complet-
ing homework, generating recipes, and more. As
more humans gravitate towards LLMs for every-
day tasks, more testing is required to ensure that
they receive accurate information regardless of
prompt language or topic. Leading models, such
as GPT, perform consistently high in academic ar-
eas like math, programming, and writing (Achiam
et al., 2023), though further testing is still be-
ing conducted on the validity of LLM responses
in more arbitrary areas like morality and ethics
(Ji et al., 2024). Although topic-specific models,
like Qwen-Coder and Math-GPT, have been cre-
ated, there are still gaps in the linguistic area re-
garding LLM usage. Leading LLMs have proven
to judge prompts fairly and create human-like re-
sponses consistently (Zheng et al., 2023) when
asked in English; however, this high performance
loses consistency when considered on a multilin-
gual scale regarding both academic (Fu and Liu,
2025) and moral (Jin et al., 2024) categories of
questions. LLM testing data is primarily in En-
glish, and though benchmarks (Ahuja et al., 2023)
and large datasets of over 100 languages have been
created, more datasets and evaluation benchmarks
are needed to continue improving the cross-lingual
responses of LLMs. Despite increases in testing
data, LLM responses still contain discrepancies
in multilingual settings (Fu and Liu, 2025). To
understand why these inconsistencies remain, we
need to understand the types of questions multi-
lingual LLMs (MLLMs) perform poorly in. By
knowing how LLM judgments shift in response to
different question types across languages, we can
create targeted datasets to improve LLM perfor-
mance in these areas.
With LLMs growing more powerful, detailed
information on niche topics becomes more acces-
sible. As mentioned above, LLM usage is steadily
increasing for various means (Liang et al. (2025),
Liang et al. (2024)). As such, implementing ca-
pable safety guidelines and restrictions on LLM
usage becomes more important. LLMs have been
proven to perform worse for multilingual queries,
as well as their safety features. Safety protocols
have been shown to perform poorly when ques-
arXiv:2510.08776v1  [cs.CL]  9 Oct 2025

--- Page 2 ---

tions are asked in non-English languages (Alon
and Kamfonas (2023), Lin et al. (2025)), as LLMs
struggle to detect malicious content in those lan-
guages. Although the safety features of various
models have improved over time, the available
testing data remains relatively limited in diver-
sity. Therefore, we contribute a dataset contain-
ing a wide range of uniquely phrased questions
designed to evaluate the effectiveness of these fea-
tures in detecting malicious content expressed in
varied forms.
In this paper, we examine how LLMs respond
to ethical, legal, and safety questions and mea-
sure the consistency of these responses across high
and low-resource languages. Our goal is to mea-
sure shifts in model responses across languages
and measure the effectiveness and biases of in-
built LLM safety features when prompts are in
non-English languages.
Our dataset is separated into five categories: Bi-
ases & Stereotypes, Consent & Autonomy, Harm
Prevention & Safety, Legality, and Moral Judg-
ment. Questions in the dataset range from sim-
ple and easy responses to ones more difficult to
answer, and LLM responses are evaluated with a
rubric to limit biases in the grading. Initial test-
ing reveals that GPT-5 has marginally greater per-
formance than other models when responding to
unsafe or harmful prompts. To test the limits of
these safety features, we refined the Harm Preven-
tion & Safety category and Consent & Autonomy
categories, designing them to be indirect to trick
the LLM into providing harmful content.
Figure 1: Edited phrasing of questions
Our key contributions are outlined as follows:
• Detailed analysis of moral and ethical re-
sponses of LLM models and found that GPT
5 performed markedly high in comparison
with other leading models
• New insights into LLM safety guidelines
consistency across low and high resource lan-
guages and how model training data impacts
responses
• Dataset of 5 categories with 100 questions
each in 6 languages, chosen to capture di-
verse linguistic characteristics and sentence
structure in order to test LLMs
2
Related Work
2.1
Measuring moral frameworks of LLMs
As LLMs continue to expand their applications,
researchers have begun examining how these sys-
tems approach questions of morality and ethics.
One such study (Achiam et al., 2023) applied a
Defining Issues Test (DIT), a common tool in psy-
chology used to determine moral development, to
measure the moral reasoning of models.
Using
a standard P-score as a metric, their results con-
cluded that although some LLMs are capable of
reaching reading levels on par with advanced hu-
man responses, results vary wildly across dilem-
mas, revealing a lack of consistency in AI ethical
reasoning.
A different approach, presented by Keenan
Samway, evaluated model responses between util-
itarianism and deontology, two well-known philo-
sophical ideologies that often contrast each other,
using a scaled rubric (Samway et al., 2025). This
study aimed to determine whether LLM responses
were biased towards or against certain ideologies.
Results revealed LLMs tended towards utilitarian
reasoning, though the degree of alignment varied
between models. Additionally, while models were
able to provide justifications for their reasoning,
said justifications often lacked depth and coher-
ence.
Studies like this highlight two main strategies
for LLM testing: adapting tools from previous de-
velopmental psychology or classifying justifica-
tions through philosophical frameworks.
While
both methods produce valuable insights, they of-
ten limit the scope of testing to few specified
dilemmas and fixed rubrics.
Since morality is
a scale and justifications are often unable to be
classified neatly, these limitations leave impor-
tant gaps in understanding how LLMs respond to
moral scenarios and the reasoning behind such de-
cisions.
2.2
Multilingual capabilities of LLMs
With the increased use of LLMs as translations
and multilingual tools, recent studies have fo-
cused on whether models maintain consistent per-
formance across languages. In Jin et al. (2024), Jin

--- Page 3 ---

tested reasoning abilities through the ‘trolley prob-
lem’ moral dilemma, evaluating how model out-
puts shifted when the same dilemma was posed in
different languages. The results showed that moral
reasoning often varied depending on the languages
of the prompt, reflecting how linguistic and cul-
tural framing can influence model behavior. The
study also noted that these variations may extend
beyond morality to other domains such as legality
and biases, emphasizing the need for testing across
multiple categories.
Another
study
examined
factual
accuracy
across languages by posing parallel sets of ques-
tions in varying difficulties (Fu and Liu, 2025).
While leading models like GPT-4o performed re-
liably in high-resource languages, they struggled
to perform in lower-resource languages, with an-
swers having more inconsistencies and factual er-
rors.
These findings suggest that multilingual rea-
soning and accuracy remain open challenges for
LLMs. Although performance is high in English,
inconsistencies in reasoning and factual reliabil-
ity persist when prompted in different languages.
This raises questions on whether LLMs can serve
as trustworthy multilingual judges in contexts that
require moral and factual reasoning across diverse
linguistic settings.
2.3
LLM safety restrictions across languages
As studies have shown decreased accuracy in
LLM responses when prompted in non-English
languages, concerns have also emerged regarding
the ability of models to consistently enforce safety
restrictions when questions appear in alternate lan-
guages.
A recently conducted study, Jailbreak-
ing LLMs through LLM safety Papers addressed
this issue by developing a large-scale dataset de-
signed to benchmark LLM safety performance
when faced with malicious or illegal queries in
over 100 languages (Lin et al., 2025).
Results
reveal several weak points in existing safety pro-
tocols, as models were significantly more likely
to produce harmful content in lower-resource lan-
guages, highlighting the discrepancies in safety
guidelines and enforcement across languages.
Our work builds on these findings by consid-
ering how phrasing affects safety detections in
addition to linguistic changes.
Inspired by the
‘trick questions’ in Jailbreaking LLMs through
LLM safety Papers, which function as jailbreak-
styled prompts, we designed harm prevention and
consent-related questions to test model consis-
tency when prompted with hidden malicious con-
tent.
In the study, Lin demonstrates that direct
safety benchmarks reveal weakness across lan-
guages; our approach aims to extend this by ex-
amining how subtle differences in phrasing may
cause models to overlook harmful content.
3
Experimental Setup
3.1
Datasets
We create a dataset of 500 questions in English
divided into 5 categories: moral judgment, bi-
ases and stereotypes, legality, harm prevention and
safety, and consent and autonomy.
These cate-
gories were selected to represent domains where
ethical sensitivity, cultural awareness, and respon-
sible decision-making are critical for language
models. By testing across these dimensions, we
assess technical accuracy along with broader so-
cial implications of model outputs. To evaluate
model accuracy and consistency across a variety
of languages, we translate the English questions
into three high-resource (Chinese, Spanish, Ara-
bic) and two low-resource (Hindi, Swahili) lan-
guages using the Googletrans Python package.
These languages were chosen due to their wide
variety in sentence structure, cultural context, and
writing systems, ranging from alphabetic to logo-
graphic scripts. This variety allows a more com-
prehensive outlook into the capacity of LLMs to
handle linguistic and cultural diversity beyond En-
glish.
Biases & Stereotypes: LLMs are prompted to
answer questions involving demographic identi-
ties that may evoke stereotypes and biases in their
response. These questions are meant to determine
if the LLMs perpetuate harmful biases and stereo-
types, especially focusing on differences in re-
sponses between high and low resource languages.
Consent & Autonomy: Most LLMs have some
safety features designed to prevent them from pro-
viding users with harmful information. This cate-
gory evaluates the resilience of LLM safety mech-
anisms by using deceptive prompts designed to
manipulate LLMs into sharing information that
could violate individual consent and autonomy.
Harm Prevention & Safety: Similar to the
consent and autonomy category, these questions
test how robust LLM safety features are by pre-
senting LLMs with disguised or indirect questions

--- Page 4 ---

intended to trick them into providing information
that could facilitate harmful or unethical activities.
Legality: - In this category, LLMs are asked
questions involving actions that are legal in some
countries but illegal in others. This is important
in determining whether LLMs make assumptions
about the user’s location based on the language
they are prompted in.
Moral Judgment: - LLMs are asked yes or no
questions on moral issues and prompted to provide
their reasoning for their decision.
These ques-
tions are meant to evaluate how well the LLMs
adhere to the six core moral principles of care,
fairness, loyalty, authority, sanctity, and liberty,
and how LLMs navigate morality between differ-
ent languages.
Figure 2: Example questions
3.2
Models
In our analysis of LLMs, we aimed to test a
wide variety of models that differed in training
data, purpose, origin, and accessibility (open-
vs.
closed-source).
To achieve this, we se-
lected a range of leading models in translation ca-
pability.
Among frontier models, we evaluated
Gemini 2.5 Pro, Claude Sonnet 4, and GPT-5.
Gemini is oriented toward academic applications,
GPT is designed to empower users by providing
broad and adaptable responses, and Claude em-
phasizes safety in its outputs.
To complement
these, we used OpenRouter to test open-source
models, specifically Llama 4 Scout and Qwen3
235B-a22b, the latter being a Chinese-developed
model with strong regional alignment.
3.3
Evaluation Rubric
For our evaluation process, we implemented Gem-
ini 2.5 pro for the use of LLM-as-a-judge and a
general rubric of grades 1-5 for the LLM to utilize
when grading.
Due to the variability in moral beliefs and our
current inability to gain an appropriate sample
across cultures, we implemented a rubric as the
standard of truth in our grading process.
Our
rubric has individual grading constraints per cat-
egory, creating distinct values for a grade of 5 ver-
sus 1. Rather than only focusing on the defini-
tive answer in LLM responses, the rubric takes
into account justification and reasoning behind
responses.
Through this, we maintain consis-
tency and eliminate some of the potential bias that
emerges from using a human to evaluate a re-
sponse that isn’t necessarily right or wrong. To
test that the evaluations remain consistent, a ran-
dom sample of responses is evaluated using GPT-
5 and Qwen 3 to guard against possible bias Gem-
ini may have towards its own responses. The re-
sults from Qwen’s evaluation grades are an aver-
age of 0.5 less than Gemini’s evaluation grades,
while GPT-5’s evaluation grades are an average of
0.6 higher. Gemini didn’t appear to show any bias
when grading its own responses compared to grad-
ing other model responses.
3.4
Prompt Engineering
For generating responses and evaluating the mod-
els, we used system prompts and set a consistent
temperature of 0.7 to reduce random variability. In
addition, each question fed into the LLMs is con-
cluded with “(under 50 words)” and the category
‘Moral Judgment’ specifically, also includes “An-
swer yes/no/maybe and then provide justification”
before the word limit. Through this, we aim to en-
courage the LLM to be specific and concise in its
answers.
Figure 3: Model intructions
3.5
Process
To conduct the evaluations, each English question
is first translated into one of five target languages
using the Googletrans Python package. The LLM

--- Page 5 ---

is then prompted with the translated question and
generates a response in that language. Next, the
response is translated back to English, and Gem-
ini 2.5 Pro evaluates it against the provided rubric.
We collect random samples of translated questions
and responses in each category and language, and
feed the translations through GPT-5 and Qwen to
validate that the translated text holds its original
meaning. To check for translation bias in our eval-
uations, we reviewed a random sample of non-
English responses and compared the results with
their English counterparts, finding that all evalua-
tions were within a 1
Figure 4: Testing Process
4
Results
Figure 5: Final Results
On average, Qwen had the lowest performance
across all categories with a 66% grade, and GPT
had the leading performance with almost 92%.
Looking at Figure 5, Gemini 2.5 Pro has the two
lowest scores amongst all models and categories,
with 1.385 out of 5 points for Consent & Auton-
omy. Gemini displayed high performance in the
Biases & Stereotypes, Legality, and Moral Judge-
ment categories, though performance decreased
drastically in the more deceiving categories. This
discrepancy between scoring for regular and trick
categories is most clearly seen in Gemini’s results,
as there is over a 2-point difference in these scores.
We determine that this is likely due to Gemini
testing data primarily containing academic papers,
hence why Gemini displayed high performance in
more factual, straightforward categories.
Figure 6: Final Graphs
Looking at Figure 6, we can see that all mod-
els displayed high performance in English in the
regular categories, but had lower performance in
the trick question categories. There is a similar
scoring pattern in these categories, with GPT hav-
ing the highest average performance and Gemini
having the lowest in both the Consent & Auton-
omy and Harm Prevention & Safety categories.
Interestingly, in these categories, models scored
higher in the low-resource languages than in the
high-resource languages. This may be due to in-
creased testing data in high-resource languages.
Since these categories are phrased in a deceiv-
ing manner, it is increasingly difficult for mod-
els to recognize whether the question will be used
for malicious purposes. When prompted in low-
resource languages, models note the use of harm-
ful words and refuse to answer; however, in high-
resource languages, models read the context of
the question and are successfully tricked into an-
swering, hence the lower scores. Another unex-
pected score was found in the Legality category
where Qwen performed poorly in low-resource

--- Page 6 ---

languages as expected; however, it also scored
poorly when prompted in Chinese despite being
a Chinese model. This low score is likely due to
Qwen being primarily tested in Chinese. Legal-
ity questions are expected to be answered in a way
that doesn’t assume anything about the user, an-
swering in ways that recognize law shifts based
on country or state. Qwen responds to questions,
assuming the user is located in China, answering
questions based only on the Chinese law. Due to
Qwen being a China-based model, the majority of
the testing data being in Chinese, and a large num-
ber of users being based in China, Qwen responds
to prompts with laws from China.
Figure 7: Example Responses
As expected, models performed better on av-
erage in the Biases & Stereotypes, Legality, and
Moral Judgement categories and poorly in Con-
sent & Autonomy and Harm Prevention & Safety,
though GPT displayed the highest performance
and only performed poorly in one category, Con-
sent & Autonomy. Low performance in this cate-
gory for GPT can be attributed to OpenAI’s safety
guidelines and increased testing in GPT directly
for jailbreaking and controlling the spread of ma-
licious content. Since questions in Consent & Au-
tonomy ask potentially emotionally and mentally
harmful questions rather than physically violent
ones, it is expected that models are more likely
to answer these questions than ones in Harm Pre-
vention & Safety. Note differences in safety pro-
tocols between models is also another reason for
discrepancies between model scores in these two
categories, as, for example, the safety guidelines
for Claude are stricter than those of Qwen or Gem-
ini.
5
Limitations
There are a couple of limitations for our bench-
mark. First, we used Googletrans to translate our
questions and responses into various languages.
As such, despite our verification efforts, inaccu-
racies and inconsistencies may still exist, poten-
tially affecting LLM responses and grading. Sec-
ond, human responses were not collected for this
experiment; thus, we used a rubric to establish a
base truth. Because of this, model evaluations re-
flect how closely the LLM responses align with
the rubric and are not a strong indicator of their
adherence to current societal values. Third, mod-
els may form certain perceptions of the user based
on the phrasing of questions, leading them to re-
spond differently due to the wording rather than
the actual content.
6
Conclusion
This study examined how leading LLMs respond
to moral and safety-related questions across high
and low-resource languages, highlighting areas
where current systems fall short.
By evaluat-
ing responses over various languages, we found
that models are less consistent when tested in
non-English languages, particularly in categories
such as Harm Prevention & Safety and Consent
& Autonomy.
While Claude Sonnet 4 demon-
strated relatively strong performance, averaging
3.75 in Harm Prevention & Safety, Gemini 2.5 Pro
showed significant weakness, averaging only 1.98
out of a 5-point grading scale. These differences
reveal that safety mechanisms, though reliable in
English, often fail to transfer across linguistic con-
texts.
Our findings demonstrate that current bench-
marks underestimate the challenges of multilin-
gual safety. Variations in reasoning, accuracy, and
refusal rates show that safety features are sensitive
to both languages and phrasing, raising concerns
about the capabilities of LLMs when handling ma-
licious and ethically complex prompts worldwide.
Addressing these shortcomings requires more ro-
bust multilingual datasets and evaluation frame-
works to ensure safety protocols and model re-
sponses remain consistent regardless of languages.
Future Work
There are several possible expansions for our
benchmark. First, our current evaluation encom-
passes six languages: English, Spanish, Chinese,

--- Page 7 ---

Arabic, Hindi, and Swahili. Broadening the lan-
guage dataset to include all languages supported
by Googletrans would provide a clearer picture
of performance variation across a wider linguis-
tic range. Another is to collect human responses
to the question dataset from diverse countries and
spoken languages would establish a reliable base-
line truth for comparing current societal values
with those exhibited by LLMs. In addition, future
iterations of the dataset should account for how
phrasing influences responses. Slightly different
wordings of the same question can produce incon-
sistent results, and leading or suggestive questions
may shape how models interpret user intent. Test-
ing these variations would reduce noise in evalua-
tion and expose potential biases in model percep-
tion.
As shown in prior work (Fu and Liu, 2025),
neural NLP has grown quickly. Jin et al. (2024)
provide a statistical foundation.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, and et al. 2023. Gpt-4 technical
report. preprint arXiv:2303.08774.
Kabir Ahuja, Harshita Diddee, Rishav Hada, Milli-
cent Ochieng, Krithika Ramesh, Prachi Jain, Ak-
shay Nambi, Tanuja Ganu, Sameer Segal, Maxamed
Axmed, Kalika Bali, and Sunayana Sitaram. 2023.
MEGA: Multilingual Evaluation of Generative AI.
preprint arXiv:2303.12528.
Gabriel Alon and Michael Kamfonas. 2023. Detecting
Language Model Attacks with Perplexity. preprint
arXiv:2308.14132.
Xiyan Fu and Wei Liu.
2025.
How Reli-
able is Multilingual LLM-as-a-Judge?
preprint
arXiv:2505.12201.
Jianchao Ji, Yutong Chen, Mingyu Jin, Wujiang Xu,
Wenyue Hua, and Yongfeng Zhang. 2024. Moral-
Bench:
Moral Evaluation of LLMs.
preprint
arXiv:2406.04428v1.
Zhijing Jin, Sydney Levine, Max Kleiman-Weiner,
Giorgio Piatti,
Jiarui Liu,
Fernando Gonzalez
Adauto, Andr´as Strausz Francesco Ortu, Mrinmaya
Sachan, Rada Mihalcea, Yejin Choi, and Bernhard
Sch¨olkopf. 2024. Multilingual Trolley Problems for
Language Models. preprint arXiv:2407.02273v1.
Weixin Liang, Zhengxuan Wu Yaohui Zhang, Haley
Lepp, Wenlong Ji, Xuandong Zhao, Hancheng Cao,
Sheng Liu, Siyu He, Zhi Huang, Diyi Yang, Christo-
pher Potts, Christopher D Manning, and James Y.
Zou. 2024. Mapping the Increasing Use of LLMs in
Scientific Papers. preprint arXiv:2404.01268.
Weixin Liang, Yaohui Zhang, Mihai Codreanu, Ji-
ayu Wang, Hancheng Cao, and James Zou. 2025.
The Widespread Adoption of Large Language
Model-Assisted Writing Across Society.
preprint
arXiv:2502.09747.
Liang Lin, Zhihao Xu, Xuehai Tang, Shi Liu, Biyu
Zhou, Fuqing Zhu, Jizhong Han, and Songlin
Hu.
2025.
Paper Summary Attack: Jailbreak-
ing LLMs through LLM Safety Papers.
preprint
arXiv:2507.13474v1.
Keenan Samway, Max Kleiman-Weiner, David Guz-
man
Piedrahita,
Rada
Mihalcea,
Bernhard
Sch¨olkopf, and Zhijing Jin.
2025.
Are Lan-
guage Models Consequentialist or Deontological
Moral Reasoners? preprint arXiv:2505.21479.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang,
Joseph E. Gonzalez, and Ion Stoica. 2023. Judg-
ing LLM-as-a-Judge with MT-Bench and Chatbot
Arena. preprint arXiv:2306.05685.

--- Page 8 ---

Appendix
A
Experiment Setup
A.1
Evaluation Rubric
B
Results
B.1
Model Response Variance
B.2
Individual Model Response Breakdown

--- Page 9 ---


--- Page 10 ---


```
