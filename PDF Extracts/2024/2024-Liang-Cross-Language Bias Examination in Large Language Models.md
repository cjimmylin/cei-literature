---
title: "2024-Liang-Cross-Language Bias Examination in Large Language Models - PDF Extract"
source_pdf: "2024-Liang-Cross-Language Bias Examination in Large Language Models.pdf"
pages: 10
extracted_at: "2026-02-13T13:13:46.602899"
---

# PDF Extract: 2024-Liang-Cross-Language Bias Examination in Large Language Models

**Source PDF:** 2024-Liang-Cross-Language Bias Examination in Large Language Models.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Cross-Language Bias Examination in Large Language Models
Yuxuan Liang
Georgia Institute of Technology
yliang372@gatech.edu
Marwa Mahmoud
University of Glasgow
marwa.mahmoud@cl.cam.ac.uk
This paper was written while I attended the Cam-
bridge Online Summer Research Program under
the supervision of Professor Marwa Mahmoud.
Abstract
This study introduces an innovative multilin-
gual bias evaluation framework for assessing
bias in Large Language Models, combining ex-
plicit bias assessment through the BBQ bench-
mark with implicit bias measurement using a
prompt-based Implicit Association Test. By
translating the prompts and word list into five
target languages — English, Chinese, Arabic,
French, and Spanish — we were able to di-
rectly compare different types of bias across
languages. The results reveal the fact that there
are huge gaps between biases in different lan-
guages used in LLMs, for example, Arabic and
Spanish show a high level of stereotype con-
sistently. In contrast, Chinese and English ex-
hibit a lower level of bias. We also disclose
the opposite pattern across bias types, for in-
stance, age shows the lowest explicit bias but
the highest implicit bias, which emphasizes the
importance of detecting implicit biases that are
undetectable with a normal, standard bench-
mark. These findings indicate that LLMs vary
significantly across different languages and di-
mensions. This study fills a key research gap by
providing a complete methodology to analyze
bias across languages. Ultimately, our work
establishes a strong foundation for the develop-
ment of equitable, multilingual LLMs, ensuring
that future models are fair and effective across
a diverse range of languages and cultures.
1
Introduction
Introduction In recent years, Large Language Mod-
els (LLMs) have been recognized as a revolution-
ary technology when people are talking about the
field of Natural Language Processing (NLP). These
Large Language Models have shown a strong abil-
ity in text generation, reasoning, translation, and
many other areas. Also, LLMs have become one
of the hottest topics in the world today. Many com-
mercial models, like GPT-4 (OpenAI et al., 2024),
and open source models, like LLaMA (Touvron
et al., 2023) have emerged. Due to the fact that
LLMs model offer strong ability and efficiency,
they have been largely integrated into our day to
day lives, including our education tools, customer
systems, legal systems, healthcare systems, etc. Ad-
ditionally, many people who work with LLMs ex-
pressed that LLMs not just make their work more
efficient, but also more meaningful (Kobiella et al.,
2025). However, with their tremendous impact on
the whole society, significant concerns have been
raised regarding that the LLMs could have social
bias, which could also lead to stereotypes and un-
fairness to the LLM applications.
Most research nowadays focuses on examining
bias in English in LLMs, covering a lot of dimen-
sions like gender, age, race, and religion, by us-
ing many benchmark like Truthful QA (Lin et al.,
2022), BBQ benchmark (Parrish et al., 2022), and
tools like BiasAlert (Fan et al., 2024) which could
detect social bias. Nonetheless, the inevitable trend
of globalization today reveals an even more com-
plex situation is that the LLMs will be served to
people who speak different languages. And it is
critical for us to ask: do LLMs have consistent
bias across all different languages, or biases will
vary between them? Answering this question could
be a key factor in promoting the equity of LLMs
development and deployment.
To answer this question, our study explores the
different degrees of bias of different languages that
exist in LLM by evaluating explicit bias and im-
plicit bias across five languages——English(EN),
Chinese(ZH), Arabic(AR), French(FR), and Span-
ish(ES). The reason why we choose these five lan-
guages is because these five languages are the top
languages spoken in the world (International Cen-
ter for Language Studies, 2024). Moreover, most
of the selected languages represent different lan-
1
arXiv:2512.16029v1  [cs.CY]  17 Dec 2025

--- Page 2 ---

guage families, for example English is classified as
Indo-European, and Mandarin Chinese is classified
as Sino-Tibetan(Ethnologue, 2024). The diversity
of languages could enhance the impact of our ex-
ploration by including most used languages and
many language families.
For explicit bias testing, we translate BBQ
prompts into target languages via DeepL API, care-
fully preserving meaning. We then invoke GPT-4
across languages to obtain responses, from which
we derive accuracy and bias scores. For implicit
bias, we obtain the IAT word list, and translate
them into target languages via DeepL API. The
model is prompted to associate each attribute with
one of two target concepts, enabling calculation
of IAT-style bias scores across categories like race,
gender, religion, and age.
This dual-method approach, integrating explicit
decision-based evaluation with implicit semantic
associations, offers a comprehensive understanding
on how bias surfaces in LLMs across languages.
1.1
Research Questions & Contribution
We seek to answer the following research ques-
tions:
• How does model bias vary across languages
and bias dimensions?
• Are explicit and implicit biases aligned or di-
vergent across languages?
• What linguistic, cultural, or technical factors
explain observed disparities?
Our contributions are:
• Construction of a multilingual experimental
framework for bias evaluation using rigorous
prompt translation and dual-method design.
• Empirical analysis of cross-language bias, re-
porting bias scores and accuracy for five lan-
guages under both explicit (BBQ) and implicit
(IAT) paradigms.
• Discussion of observed trends, causal factors,
and implications for fairness in multilingual
AI systems.
1.2
summary
Ultimately, this work seeks to expand the research
of fairness and bias issues that exist in LLMs and
inspire a broader examination of various issues
in LLMs across linguistic and cultural contexts.
As LLM becomes more and more globalized and
widely used, it is necessary for us to reveal and un-
derstand LLMs’ behaviors, which is an imperative
and indispensable step for LLM development.
2
Related Works
In this section, we will review three core research
areas that have major impacts on our study. Firstly,
we examine explicit bias in LLM, how the previous
work defines bias, and providing work flow to mea-
sure explicit bias. Second, we explore implicit bias.
Even though implicit bias is not a new concept in
LLM. However, the methodology for measuring
implicit bias is innovative. Last but not least, I will
discuss some areas and fields that will be helpful
when we are exploring multilingual LLM.
2.1
Explicit bias measuring in LLM
(English-centric)
A great amount of research on the analysis of ex-
plicit bias(which is bias that is traditionally con-
sidered as bias for LLM), for instance clarifying
definition and notion for bias in LLM (Navigli et al.,
2023; Gallegos et al., 2024), how could the bias
form in the process of training LLM (Navigli et al.,
2023).Additionally, there are many benchmarks
and datasets that are invented and constructed for
the purpose of LLM bias detection and evaluation
(Gallegos et al., 2024; Lin et al., 2022; Parrish
et al., 2022). Most of this research and these bench-
marks are focused on English-centric bias detection.
There is one exception: MBBQ(Multilingual Bias
Benchmark for Question-answering) (Neplenbroek
et al., 2024), which is a dataset that is built for
the purpose of cross-lingual comparison of stereo-
types in generative LLMs based on BBQ dataset
(Parrish et al., 2022). Also, there is one dataset for
detecting explicit bias in Korean, called KBBQ (Jin
et al., 2024). However, this dataset only provides
English, Dutch, Spanish, and Turkish. These lim-
ited language choices constrain the field of impact
and generalizability of the dataset, especially given
that most of its included languages are not among
the most widely spoken worldwide. Despite all
these limitations, these previous works underscore
that explicit bias is measurable, and they have done
great in depth analysis in bias behavior of LLMs.
In addition to providing analysis, many of these pre-
vious works provide a complete and reproducible
work flow that could be very helpful to the future
2

--- Page 3 ---

works.
2.2
Implicit bias measuring in LLM
Due to the fact that many LLMs nowadays have
eliminated explicit bias by several efficient ways,
for example prompt engineering (Kamruzzaman
and Kim, 2024). However, it does not represent that
bias does not exist in LLMs. While explicit bias
metrics capture surface-level stereotyping and bias,
implicit bias evaluates deeper semantic associa-
tions. A recent prompt-based method adapts the Im-
plicit Association Test (IAT) for LLMs: the study
“Measuring Implicit Bias in Explicitly Unbiased
Large Language Models” demonstrates that even
models explicitly free of bias can display covert
associative biases across categories like race and
gender (Bai et al., 2025). This method of testing im-
plicit bias is inspired by a century of psychological
studies on human stereotypes. Methodologically,
explicit bias can be elicited by asking people to
express their opinions. In contrast, implicit bias
measures bypass deliberation and are thus likely to
be free of influence from social desirability. And
one of the method that can measure the implicit
bias is Implicit Association Test(IAT) (Bai et al.,
2025). The method shows strong correlation with
embedding-based bias metrics and is predictive of
LLM decision-making behavior (Bai et al., 2025).
Additional work (“Explicit vs. Implicit: Investigat-
ing Social Bias in Large ...”) provides evidence
that explicit and implicit biases in LLMs often di-
verge, and that explicit debiasing techniques may
not affect implicit associations. These findings re-
veal the complexity and importance of measuring
both explicit and implicit bias in LLMs (Zhao et al.,
2025).
2.3
Multilingual LLM performances
Many LLMs face challenges when they are trained
on multilingual data. There are research and eval-
uation shows that most of the LLMs perform well
in high-resource languages but have a not satisfac-
tory result on low-resource languages since there
are unbalance dataset and uneven training distri-
bution (Gupta et al., 2025).
Also, there is re-
search that attempt to understand how is LLMs han-
dling multilingualism (Zhao et al., 2024), and they
also propose a framework that can improve LLMs
performance on multilingual scenarios. However,
the LLMs still have better performance in high-
resource languages than low-resource languages.
Nonetheless, there is research indicating that multi-
lingual training is already a means that reduces bias
itself (Nie et al., 2024), since multilingual training
provided model with more diverse data from dif-
ferent cultural background. These previous works
directly inspire me to think that multilingual LLMs
could not only face serious performance problems,
but also, they could exhibit bias and stereotypes
disparities.
2.4
summary
Overall, explicit bias evaluation has primarily been
English-focused, while emerging studies such as
MBBQ explore cross-lingual explicit bias. Implicit
bias evaluation by prompt-based IAT reveals la-
tent associative biases even after explicit mitigation.
Multilingual performance research highlights sys-
temic disparities across languages. However, there
is no study combining explicit and implicit bias
measurement across multiple linguistically diverse
languages in a standardized framework, exposing
a critical research gap which our research directly
addresses.
3
Methodology
We designed a reproducible cross-language bias
evaluation workflow with four main steps: First
and foremost, we need to prepare the English
BBQ prompts for the explicit bias test, and the
IAT word list and the prompt template for the im-
plicit bias test. Secondly, All prompts, prompt
templates, and word lists are translated into tar-
get language——English(En), Chinese(ZH), Ara-
bic(AR), Spanish(ES), and French(FR)——using
DeepL. The third step is invocation of LLM, we
choose to use GPT-4 as the LLM in zero-shot mode
to generate all the responses. The last step is cal-
culate the accuracy and bias score on BBQ; and
calculate the D-score based on the responses on
prompt-based IAT.
3.1
Explicit Bias Evaluation: BBQ
benchmark
We use the BBQ dataset (Parrish et al., 2022),
which comprises many dimensions and a huge
amount of different samples on each dimension.
And for this experiment, we choose to examine
five dimensions: age, gender, nationality, race, and
religion. And for each dimension test the first 100
samples from that dimension. After gathering the
prompts, we use DeepL API to carefully translate
the questions and the answers into five target lan-
3

--- Page 4 ---

Figure 1: The complete work flow of the methodology
Figure 2: Example of using BBQ benchmark to evaluate
explicit bias
guages, maintaining their original meaning and
structure.
Each prompt is queried using OpenAI API to
call GPT-4 in zero-shot mode with temperature=0.
We calculate two metrics for each language and
each dimension after we finish the experiments and
get the data: accuracy and bias score. Accuracy
is simply the percentage of correct answers in all
the contexts. And since accuracy is not able to
correctly represent the response pattern in inaccu-
rate response, we follow the BBQ methodology,
calculating the bias score:
Bias score in disambiguated contexts:
sDIS = 2

nbiased_ans
nnon−UNKNOWN_outputs

−1
(1)
Bias score in ambiguous contexts:
sAMB = (1 −accuracy)sDIS
(2)
A bias score of 0 indicates that no model bias has
been measured, while 1 indicates that all answers
align with the targeted social bias, and -1 indicates
that all answers go against the bias (Parrish et al.,
2022).
3.2
Implicit Bias Evaluation: Prompt-Based
IAT
We adopt prompt-based Implicit Association Test
by using the word list in Explicitly unbiased large
language models still form biased associations (Bai
et al., 2025), which allows us to measure the im-
plicit bias of a LLM.
We run 50 tests on every sub-category(racism,
guilt, skintone, weapon, black, hispanic, asian, en-
glish, career, science, sexuality, power, islam, ju-
daism, buddhism, disability, weight, mental, eating,
age). Also, in order to have a clear comparison to
the explicit bias test, we also conclude the data into
four different super-category(race, gender, religion,
and age).
We use a uniform prompt template: "Here is a
list of words. For each word pick one — pair[0]
or pair[1] — ", "and write it after the word. The
words are attributes. ", "Do not include any extra
text. Separate word-label pairs with ’-’ and each
on a new line." (Bai et al., 2025) The next step, we
4

--- Page 5 ---

Figure 3: Example of using IAT to evaluate implicit bias
carefully translate the IAT word list, and the prompt
template into five target languages, maintaining its
original meaning.
Each prompt is queried using OpenAI API to
call GPT-4 in zero-shot mode with temperature=0.
We calculate two metrics for each language and
each dimension after we finish the experiments and
get the data: bias scores. Bias scores for IAT are
calculated as:
bias =
N(sa, Xa)
N(sa, Xa) + N(sa, Xb)
(3)
+
N(sb, Xb)
N(sb, Xa) + N(sb, Xb) −1
LLM Word Association Test prompts consist of
a template instruction t, two sets of tokens Sa and
Sb referring to members of different groups a and
b associated with a social category, and two sets
of response tokens Xa and Xb associated with the
same two groups.
We embed S and X in the prompt template t,
e.g.,
t(S, X) =
“Here is a list of words. For each word,
pick a word—sa or sb—and write it
after the word. The words
are x1, x2, . . . .”
where sa and sb are drawn from Sa and Sb re-
spectively and the xi are a randomly permuted set
of words drawn in equal quantities from Xa and Xb.
For example, if the target category is gender, then
sa and sb might ... (Bai et al., 2025) Bias ranges
from -1 to 1, reflecting the difference in the associ-
ation of attributes with each group. For example, if
Julia is assigned to wedding-related words 7 out of
7 times and Ben is assigned to office-related words
7 out of 7 times (Bai et al., 2025).
3.3
summary
Our methodology combines established and ver-
ified explicit bias benchmark, BBQ benchmark
Figure 4: This Figure presents the bias score of GPT-4’s
responses in ambiguous contexts across five languages
(Arabic, English, Spanish, French, and Chinese) and
five bias dimensions (age, gender, nationality, race, and
religion). Gender exhibits the highest level of explicit
bias across all languages in ambiguous context Also,
Chinese and English shows a relatively low level of
explicit bias in ambiguous context.
and an innovative, inspired by psychology, prompt-
based Implicit Association Test(IAT) across five
languages. This framework supports a transpar-
ent and reproducible bias evaluation, providing a
foundation of equality LLM development.
4
Experiment and Evaluation
In this section, we will exhibit and analyse the
experiment result we have done. Based on the
experiment result, we will have a short discussion
on the possible causation and potential solution.
4.1
BBQ benchmark experiment results
We observe high accuracy in the nationality di-
mension, with every language having an accuracy
above 90%, with Arabic reaching the peak accuracy
of 97%. Also, gender and race dimensions show
a great performance across languages, although
English and Spanish slightly outperform other lan-
guages in gender dimension. Nevertheless, we no-
tice that we have a great drop in accuracy in age and
religion dimension, except for English. Across ev-
ery dimension, only English can either perform the
best or stay in the usable range. This phenomenon
suggests that GPT-4 is more reliable in its reason-
ing when it is tackling English, which is likely due
to its uneven training data distribution. These re-
sults confirm that while the model is capable of
tackling problems with clear context, performance
will vary across dimensions and languages.
When we are analyzing bias scores in ambiguous
contexts, we notice that gender is the most biased
dimension among five dimensions, with Arabic
with the highest bias score(0.22). At the same
time, other languages also show a significant level
5

--- Page 6 ---

Figure 5: This Figure presents the accuracy of GPT-4’s
responses in disambiguated contexts across five lan-
guages (Arabic, English, Spanish, French, and Chinese)
and five bias dimensions (age, gender, nationality, race,
and religion). Nationality exhibits the highest level of
average accuracy, while age shows the lowest level of
accuracy. Also, English have a consistently high level
of bias except for the race dimension.
of stereotypes, for example Chinese and French
have a bias score 0.16. Interestingly, we notice
that the bias score of age of Chinese and Arabic is
negative(-0.02, -0.10), which suggests that Arabic
has an opposite bias to the normal social bias in the
age dimension.
However, when we are checking the disambigu-
ous context scenario, the bias scores increase dra-
matically almost across all dimensions and lan-
guages. Gender bias still remains to be the most
biased dimension among five dimensions, but the
bias score of Arabic has increased to 0.60, and
other languages also show a very high level of bias,
for instance English(0.53), and French(0.51). Ad-
ditionally, nationality also becomes a dimension
that most languages exhibit high levels of stereo-
types, most languages have a bias score greater or
equal than 0.50, only French have a bias score 0.21
which is lower than 0.50. Surprisingly, we notice
that there are more negative bias score when we
are comparing disambiguous context and ambigu-
ous context, for example, religion in English(-0.06)
and age in Spanish(-0.07), indicating that we GPT-
4 is more possible to be anti-stereotype when it is
facing disambiguous context.
Also, we could see that English has a minimal
race bias score(0.04) and even a negative religion
bias score(-0.06), which may reflect the trend in En-
glish training data. Comparing two graphs 6 and 5,
we could see almost the same trend between disam-
biguous context and ambiguous context, with age
dimension being the least severe level of stereotype
and gender being most biased dimension.
Figure 6: This Figure presents the bias score of GPT-4’s
responses in disambiguated contexts across five lan-
guages (Arabic, English, Spanish, French, and Chinese)
and five bias dimensions (age, gender, nationality, race,
and religion). Gender again shows a strong level of bias
across all languages among all dimensions in disam-
biguated context. Notably, data exhibits great discrep-
ancy of bias level in religion dimension.
Also, we notice that both Arabic and Spanish
show a high level of bias in both ambiguous context
and disambiguous context across multiple dimen-
sions. Surprisingly, Chinese and English remain a
relatively low level of stereotype across multiple
dimensions. This discrepancy reveals the fact that
LLM could show different levels of bias and stereo-
type when LLM are facing different languages.
In summary, our evaluation reveals a stereotype
pattern in GPT-4’s explicit bias across both ambigu-
ous and disambiguous context. Gender consistently
exhibits the highest level of bias among all dimen-
sions. And Arabic and Spanish showing the highest
overall bias scores, while Chinese and English still
remain at a relatively low lel of stereotype. Surpris-
ingly, when GPT-4 is facing disambiguous context,
it significantly behaves much more biased than am-
biguous context.
4.2
Implicit Association Test experiment
results
Graph 7 illustrates the conclusionary data of the
Implicit Association Test(IAT) across four super-
category(dimensions) of five target languages.
Among all these different dimensions, age shows
the strongest level of bias, with all languages hav-
ing a bias score above 0.75, and Arabic having the
highest level of stereotype, which almost has a bias
score of 1.00. This suggests that GPT-4 exhibits a
strong implicit bias toward age-related problems
across all the languages. In addition to age, race
dimension also shows a relatively high level of bias
with all the languages receiving a bias score above
6

--- Page 7 ---

Figure 7: This Figure presents the bias score of GPT-4’s
responses of Implicit Association Test(IAT) contexts
across five languages (Arabic, English, Spanish, French,
and Chinese) and four super categories(dimensions)
(age, gender, race, and religion). Age shows a sur-
prisingly high level of implicit bias. French exhibits a
consistently low level of implicit bias. Unexpectedly,
English presents a high level of implicit bias.
0.4. Conversely, gender and religion dimensions
have a relatively low level of implicit bias. Notice-
ably, French exhibits a surprisingly low level of
implicit bias in gender and religion, with both of
the bias scores below 0.1.
This Figure 8 provides a more detailed view
of how GPT-4 performs in every sub-category.
Largely, we can see a similar pattern across all
the languages, for example, high levels of bias in
racism, guilt , and skintone, and relatively no bias
in black, hispanic, and asian. However, when we
are making a more detailed exploration of the data,
we can see some very interesting behavior. For in-
stance, every language has a nearly zero bias score
when they are answering asian related problems,
but Chinese has a negative bias score, which repre-
sents that when we are talking to GPT-4 in Chinese,
GPT-4 could behave anti-stereotypes. That could
be caused by the cultural context in the Chinese
training dataset.
Across these two figures 7 and 8, we could ob-
serve that age and gender show a strong degree of
implicit bias. Interestingly, English exhibits a deep
degree of implicit bias in every dimension, but at
the same time, Chinese and French seem to be not
so implicitly biased.
These implicit bias results indicate that even
when LLMs are prompted neutrally, deep semantic
associations still reflect great societal stereotypes
in a way that varies by both language and category.
Figure 8: This Figure presents the bias score of GPT-4’s
responses of Implicit Association Test(IAT) contexts
across five languages (Arabic, English, Spanish, French,
and Chinese) and sixteen super categories(dimensions)
(racism, guilt, skintone, weapon, black, hispanic, asian,
english, career, science, sexuality, power, islam, ju-
daism, buddhism, age). Even implicit bias level of every
language across every dimension exhibits a largely sim-
ilar trend, there are still gaps between the implicit bias
level across all the languages.
4.3
Comparing the result of explicit bias and
implicit bias
When we are comparing explicit and implicit bias
experiment results, several revealing trends have
emerged. Explicit bias experiments indicate that
gender and nationality are the most biased dimen-
sions. And age is the least biased dimension explic-
itly. However, in the implicit bias experiment, age
shows the greatest level of bias implicitly. More-
over, there are some consistent patterns, for exam-
ple Arabic shows a high level of bias both explicitly
and implicitly. Notably, Chinese and French con-
sistently exhibit low levels of bias in both explicit
bias and implicit bias. Even though English shows
a low level of explicit bias, surprisingly, English
actually exhibits a high level of implicit bias. Over-
all, our results emphasize the existence of different
levels of bias between languages and dimensions
both explicitly and implicitly.
4.4
Discussion
After we quantify the differences in both the ex-
plicit bias and the implicit bias within GPT-4, we
will have a short discussion on why the bias exists,
and some potential solution or means to mitigate
these differences.
7

--- Page 8 ---

4.4.1
Why does bias differ between
languages?
The variance in bias between different languages
could stem from the uneven and unbalanced train-
ing dataset problems (Li et al., 2025). Also, there
is research indicating that high-resource languages,
like English, outperform low-resource languages
in bias (Neplenbroek et al., 2024). Furthermore,
there are research notes that LLM safety and align-
ment behave differently across languages due to
disparities in pretraining data, with low-resource
languages often under-aligned and biased (Shen
et al., 2024). Also, the reason why there is a huge
gap between explicit bias and implicit bias is that
most LLMs have bias elimination strategies. For
instance, there are prompts that can reduce output
bias; for example, there are some prompt-tuning
techniques that could mitigate gender bias (Chisca
et al., 2024; Gallegos et al., 2025), which means
that we can deploy DPO to LLMs that can mitigate
bias (Allam, 2024), and some datasets that can be
used to finetune the model allow the model to rec-
ognize and mitigate bias (Allam, 2024). Explicit
bias has been the area that most researchers focus
on since the explicit bias can directly be seen in the
models’ output. Therefore, it could be a potential
reason that can explain why there is a huge gap
between explicit bias and implicit bias.
4.4.2
Potential solutions and mitigation
methods
To address this bias discrepancy, we propose some
potential solutions.
• Balance cross-lingual dataset. Models that train
on a more balanced, equally-distributed dataset
could efficiently reduce stereotypes and improve
model alignment across languages (Shen et al.,
2024).
• Direct Preference Optimization (DPO). There
is research exploring bias mitigation in English
(Allam, 2024). Extending DPO frameworks to
more languages could help mitigate cross-lingual
bias.
• Prompting technique. Prompt tuning is an ef-
fective, lightweight way to reduce bias without
full retraining. A framework reduces social bias
in encoder-only models (Chisca et al., 2024); in-
spired by this, prompt tuning may also mitigate
cross-language bias in LLMs.
5
Conclusion
5.1
Limitation
While our study provide a completed examination
of bias in different languages in LLM, our study is
still subject to two main limitation:
5.1.1
Language Coverage and Model
Coverage
We only apply our experiments in five languages,
and only in one LLM model. This factor limits
the applicability of our study and findings. Also,
since GPT-4 is a close-source model, it sets up a lot
of difficulties when we try to determine where the
bias problems stem from and what strategy GPT-4
is using to reduce their social bias.
5.1.2
Translation artifact
Even though we are using the very well-known
translation application, DeepL, as our translator,
there are inevitably meaning shifts. Machine learn-
ing translation often struggles with word-sense dis-
ambiguated and cultural nuance. All these factors
could introduce misunderstanding and meaning
shifts in translation. Moreover, structural differ-
ences exist between languages, which could also
lead to unintended artifacts.
6
Summary
In this study, we introduced a novel evaluation
framework combining both explicit bias(BBQ) and
implicit bias(prompt-based IAT) to assess the level
of bias across different languages. We enable di-
rect and intuitive contrast of bias across different
linguistic contexts in LLM. In our experiment re-
sult, we reveal the noticeable gap between biases
of different languages in LLM: Arabic and Spanish
show a significantly higher level of bias than Chi-
nese and English. Surprisingly, we also discover
that the dimension of bias is also distinct between
explicit bias and implicit bias, for example, age has
the least level of explicit bias but has the highest
level of implicit bias.
References
Ahmed Allam. 2024. BiasDPO: Mitigating bias in lan-
guage models through direct preference optimization.
In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 4:
Student Research Workshop), pages 42–50, Bangkok,
Thailand. Association for Computational Linguistics.
8

--- Page 9 ---

Xuechunzi Bai, Angelina Wang, Ilia Sucholutsky, and
Thomas L. Griffiths. 2025.
Explicitly unbiased
large language models still form biased associations.
Proceedings of the National Academy of Sciences,
122(8):e2416228122.
Andrei-Victor Chisca,
Andrei-Cristian Rad,
and
Camelia Lemnaru. 2024. Prompting fairness: Learn-
ing prompts for debiasing large language models. In
Proceedings of the Fourth Workshop on Language
Technology for Equality, Diversity, Inclusion, pages
52–62, St. Julian’s, Malta. Association for Computa-
tional Linguistics.
Ethnologue. 2024.
Largest language families.
Ac-
cessed: 2025-07-24.
Zhiting Fan, Ruizhe Chen, Ruiling Xu, and Zuozhu
Liu. 2024. BiasAlert: A plug-and-play tool for so-
cial bias detection in LLMs. In Proceedings of the
2024 Conference on Empirical Methods in Natural
Language Processing, pages 14778–14790, Miami,
Florida, USA. Association for Computational Lin-
guistics.
Isabel O. Gallegos, Ryan Aponte, Ryan A. Rossi, Joe
Barrow, Mehrab Tanjim, Tong Yu, Hanieh Deilam-
salehy, Ruiyi Zhang, Sungchul Kim, Franck Dernon-
court, Nedim Lipka, Deonna Owens, and Jiuxiang
Gu. 2025. Self-debiasing large language models:
Zero-shot recognition and reduction of stereotypes.
In Proceedings of the 2025 Conference of the Na-
tions of the Americas Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies (Volume 2: Short Papers), pages 873–888,
Albuquerque, New Mexico. Association for Compu-
tational Linguistics.
Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow,
Md Mehrab Tanjim, Sungchul Kim, Franck Dernon-
court, Tong Yu, Ruiyi Zhang, and Nesreen K. Ahmed.
2024. Bias and fairness in large language models:
A survey. Computational Linguistics, 50(3):1097–
1179.
Vansh Gupta, Sankalan Pal Chowdhury, Vilém Zouhar,
Donya Rooein, and Mrinmaya Sachan. 2025. Multi-
lingual performance biases of large language models
in education. Preprint, arXiv:2504.17720.
International Center for Language Studies. 2024. Most
spoken languages in the world. Accessed: 2025-07-
24.
Jiho Jin, Jiseon Kim, Nayeon Lee, Haneul Yoo, Al-
ice Oh, and Hwaran Lee. 2024. KoBBQ: Korean
bias benchmark for question answering. Transac-
tions of the Association for Computational Linguis-
tics, 12:507–524.
Mahammed Kamruzzaman and Gene Louis Kim. 2024.
Prompting techniques for reducing social bias in llms
through system 1 and system 2 cognitive processes.
Preprint, arXiv:2404.17218.
Charlotte Kobiella,
Teodora Mitrevska,
Albrecht
Schmidt, and Fiona Draxler. 2025. When efficiency
meets fulfillment: Understanding long-term llm in-
tegration in knowledge work. In Proceedings of the
4th Annual Symposium on Human-Computer Interac-
tion for Work, CHIWORK ’25, New York, NY, USA.
Association for Computing Machinery.
Miaomiao Li, Hao Chen, Yang Wang, Tingyuan Zhu,
Weijia Zhang, Kaijie Zhu, Kam-Fai Wong, and Jin-
dong Wang. 2025. Understanding and mitigating the
bias inheritance in llm-based data augmentation on
downstream tasks. Preprint, arXiv:2502.04419.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.
TruthfulQA: Measuring how models mimic human
falsehoods. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 3214–3252, Dublin,
Ireland. Association for Computational Linguistics.
Roberto Navigli, Simone Conia, and Björn Ross. 2023.
Biases in large language models: Origins, inventory,
and discussion. J. Data and Information Quality,
15(2).
Vera Neplenbroek, Arianna Bisazza, and Raquel Fer-
nández. 2024. MBBQ: A dataset for cross-lingual
comparison of stereotypes in generative LLMs. In
First Conference on Language Modeling.
Shangrui Nie, Michael Fromm, Charles Welch, Rebekka
Görge, Akbar Karimi, Joan Plepi, Nazia Mowmita,
Nicolas Flores-Herr, Mehdi Ali, and Lucie Flek.
2024. Do multilingual large language models mit-
igate stereotype bias?
In Proceedings of the 2nd
Workshop on Cross-Cultural Considerations in NLP,
pages 65–83, Bangkok, Thailand. Association for
Computational Linguistics.
OpenAI, Josh Achiam, Steven Adler, and etc. 2024.
Gpt-4 technical report. Preprint, arXiv:2303.08774.
Alicia
Parrish,
Angelica
Chen,
Nikita
Nangia,
Vishakh Padmakumar, Jason Phang, Jana Thompson,
Phu Mon Htut, and Samuel Bowman. 2022. BBQ:
A hand-built bias benchmark for question answering.
In Findings of the Association for Computational
Linguistics: ACL 2022, pages 2086–2105, Dublin,
Ireland. Association for Computational Linguistics.
Lingfeng Shen, Weiting Tan, Sihao Chen, Yunmo Chen,
Jingyu Zhang, Haoran Xu, Boyuan Zheng, Philipp
Koehn, and Daniel Khashabi. 2024. The language
barrier: Dissecting safety challenges of LLMs in mul-
tilingual contexts. In Findings of the Association for
Computational Linguistics: ACL 2024, pages 2668–
2680, Bangkok, Thailand. Association for Computa-
tional Linguistics.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard
Grave, and Guillaume Lample. 2023. Llama: Open
and efficient foundation language models. Preprint,
arXiv:2302.13971.
9

--- Page 10 ---

Yachao Zhao, Bo Wang, Yan Wang, Dongming Zhao,
Ruifang He, and Yuexian Hou. 2025.
Explicit
vs. implicit: Investigating social bias in large lan-
guage models through self-reflection.
Preprint,
arXiv:2501.02295.
Yiran Zhao, Wenxuan Zhang, Guizhen Chen, Kenji
Kawaguchi, and Lidong Bing. 2024. How do large
language models handle multilingualism?
In Ad-
vances in Neural Information Processing Systems
(NeurIPS).
10

```
