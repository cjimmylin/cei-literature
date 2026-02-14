---
title: "2025-Liu-Comparing diversity negativity and stereotypes in Chinese-language AI - PDF Extract"
source_pdf: "2025-Liu-Comparing diversity negativity and stereotypes in Chinese-language AI.pdf"
pages: 21
extracted_at: "2026-02-13T17:43:22.358919"
---

# PDF Extract: 2025-Liu-Comparing diversity negativity and stereotypes in Chinese-language AI

**Source PDF:** 2025-Liu-Comparing diversity negativity and stereotypes in Chinese-language AI.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

This manuscript has been accepted for publication in PeerJ Computer Science
Comparing diversity, negativity, and
stereotypes in Chinese-language AI
technologies: an investigation of Baidu,
Ernie and Qwen
Geng Liu1,†, Carlo Alberto Bono1,†, and Francesco Pierri1,*
1Dipartimento di Elettronica, Informazione e Bioingegneria, Politecnico di Milano, Via
Giuseppe Ponzio 34/5 20133 Milano, Italia
Corresponding author:
Francesco Pierri∗
Email address: francesco.pierri@polimi.it
†These authors have contributed equally.
ABSTRACT
Large Language Models (LLMs) and search engines have the potential to perpetuate biases and
stereotypes by amplifying existing prejudices in their training data and algorithmic processes, thereby
influencing public perception and decision-making. While most work has focused on Western-centric
AI technologies, we examine social biases embedded in prominent Chinese-based commercial tools,
the main search engine Baidu and two leading LLMs, Ernie and Qwen. Leveraging a dataset of 240
social groups across 13 categories describing Chinese society, we collect over 30k views encoded
in the aforementioned tools by prompting them to generate candidate words describing these groups.
We find that language models exhibit a broader range of embedded views compared to the search
engine, although Baidu and Qwen generate negative content more often than Ernie. We also observe
a moderate prevalence of stereotypes embedded in the language models, many of which potentially
promote offensive or derogatory views. Our work highlights the importance of prioritizing fairness and
inclusivity in AI technologies from a global perspective.
1 INTRODUCTION
The advent of novel Large Language Models (LLMs) has revolutionized the field of natural language
processing (NLP), offering unprecedented potential for a wide range of applications, from machine
translation and sentiment analysis to conversational agents and content generation Zhu et al. (2024b);
Zhang et al. (2024); Deng et al. (2023). LLMs have demonstrated an impressive ability to understand
and generate human-like text, making them invaluable tools in both academic research and commercial
settings Ziems et al. (2024); Minaee et al. (2024). However, along with their potential, these models
also carry significant risks. As language models (LMs) become increasingly integrated into various
applications, concerns about their reliability, ethical use, and potential for misuse have grown, prompting
a growing body of studies first related to early generation language models May et al. (2019); Nadeem
et al. (2021) and more recently to LLMs Choenni et al. (2021); Navigli et al. (2023); Busker et al. (2023);
Deshpande et al. (2023); Gallegos et al. (2024). In addition, the opaque nature of these models often
makes it difficult to understand their inference processes, raising questions about accountability and
transparency Bender et al. (2021); Liao and Wortman Vaughan (2024).
One pressing issue associated with this technology is the presence of biases and stereotypes embedded
within language models, which can stem from the data they are trained on, thus reflecting the prejudices
and inequalities prevalent in broader cultural and social contexts Liang et al. (2020); Kotek et al. (2023).
These biases can manifest in harmful ways, such as reinforcing stereotypes or supporting discriminatory
arXiv:2408.15696v4  [cs.CY]  6 Feb 2025

--- Page 2 ---

decisions, thus perpetuating social injustices Weidinger et al. (2021); Nogara et al. (2025); B¨ar et al.
(2024). Researchers have developed various methods to measure and mitigate these biases, proposing
datasets and metrics to evaluate the models’ fairness Zmigrod et al. (2019); Webster et al. (2020); Liang
et al. (2020). Despite these efforts, significant challenges remain, particularly when addressing proprietary
models where access to internal mechanisms remains restricted Huang et al. (2024). This limitation
hampers the effectiveness of many bias detection and mitigation techniques, underscoring the necessity
for further innovation and scrutiny in this area.
Most research on bias and fairness in LLMs has focused on English and other widely spoken languages,
leaving a gap in our understanding of how these models perform in different linguistic and cultural contexts
Ducel et al. (2023); Yang et al. (2024). Chinese, natively spoken by over 1.35 billion individuals (∼17%
of the global population), has received comparatively little attention from the scientific community Xu
et al. (2024). This oversight is critical, given the unique cultural, social, and linguistic characteristics
of the Chinese language. Most of the current LLMs are primarily trained on English corpora, which
inherently reflect Western cultural values Wang et al. (2024a); Naous et al. (2024); Li et al. (2024); Zhu
et al. (2024a). However, when such models are employed in non-Western settings, biases and distortions
may arise since language and culture are intrinsically linked with each other, as language reflects and
conveys cultural values, norms, and perspectives woven into society. For example, LLMs may generate
responses that assume culture-specific norms, such as referencing holidays like Thanksgiving, which
are not celebrated globally. In contrast, Ernie, developed by Baidu, demonstrates a stronger alignment
with Chinese cultural contexts, providing culturally appropriate responses when prompted in Chinese,
such as references to Lunar New Year and the Qixi Festival (Chinese Valentine’s Day) Wang et al.
(2024a). Likewise, ChatGPT has demonstrated limitations in accurately interpreting medical knowledge
specific to the Chinese population, particularly concerning Traditional Chinese Medicine (TCM). It has
been shown that Chinese LLMs such as Qwen and Ernie outperform Western models on TCM-related
questions, achieving an average accuracy of 78.4% compared to 35.9% for Western models Zhu et al.
(2024a). Addressing cultural specificities is therefore essential for developing fair and unbiased LLMs
that can serve diverse populations effectively and ethically Zhao et al. (2023); Huang and Xiong (2024).
Consequently, our study aims to investigate the biases present in two leading Chinese LLMs, namely
Ernie and Qwen, as well as in Baidu, the most popular search engine used in China; we include the latter
following previous work Choenni et al. (2021); Busker et al. (2023); Liu et al. (2024) that highlighted
the role of online search engines in potentially perpetuating cultural biases and stereotypes. Leveraging
a dataset of social groups and categories pertaining to Chinese society, we use an empirical approach
to study the social views encoded in the models. Following Busker et al. (2023), we probe the models
with multiple questions, to elicit the views that are encoded about different social groups. We then study
the completions obtained in terms of diversity, negativity, and alignment. We use this approach as the
internal models’ probability for predicted tokens is not available, and existing metrics for measuring
biases associated with certain words cannot be applied Kurita et al. (2019); Gallegos et al. (2024). Our
work contributes to the literature on fairness and inclusivity in AI-generated content by systematically
evaluating Chinese-based LLMs (Ernie and Qwen) and comparing them with a Chinese search engine
(Baidu). To the best of our knowledge, this is the first comparative study that investigates biases across
multiple proprietary Chinese language AI technologies. Our analysis reveals significant diversity gaps
and varying levels of bias, highlighting the risks associated with biased outputs concerning different
social groups. Additionally, our study contributes to understanding and mitigating biases present in
Chinese-based LLMs. Addressing these biases is not only a technical challenge but also an ethical
responsibility, as it directly affects how different social groups are perceived and represented in society.
The manuscript is organized as follows: in the next section, we review related work; we then describe
the data collection and methodologies used in our analyses; next, we present the results of our analyses;
finally, we discuss our findings and their implications, mention limitations, and draw conclusions.
2 RELATED WORK
In recent years, various studies have introduced datasets, methods and metrics to quantify social bias and
stereotypes in pre-trained early-generation LMs and LLMs Caliskan et al. (2017); Zhao et al. (2018);
May et al. (2019); Kurita et al. (2019); Liang et al. (2020); Barikeri et al. (2021); Wald and Pfahler
(2023). However, these efforts face challenges with most proprietary models, as access to internal model
information (e.g., probability of predicted tokens and internal embeddings) is restricted Huang et al.
2/21

--- Page 3 ---

Figure 1. Diagram showing the workflow of our analysis.
(2023), thereby limiting the application of metrics such as the Log Probability Bias Score (LPBS) Kurita
et al. (2019) and the Sentence Embedding Association Test (SEAT) May et al. (2019). In addition, the
literature advises to exercise caution with embedding- and probability-based metrics Gallegos et al.
(2024). In the following, we focus on contributions more directly related to our work and refer readers to
Gallegos et al. (2024) for a more comprehensive review of the literature on this topic.
Choenni et al. (2021) introduced a method for eliciting stereotypes by retrieving salient attributes
associated with social groups through the auto-completion functionality in search engines such as Google,
Yahoo, and DuckDuckGo. They then analyzed the predictions of pre-trained language models to assess
how many of these stereotypical attributes were encoded within the models. Their study also highlighted
the evolution of stereotypes with modifications in training data during model fine-tuning stages. Building
on this work, Busker et al. (2023) conducted an empirical study to explore stereotypical behavior in
ChatGPT, focusing on U.S.-centric social groups. They presented stereotypical prompts in six formats
(e.g., questions and statements) and across nine different social group categories (e.g., age, country, and
profession). For each prompt, they asked ChatGPT to fill in a masked word and mapped the completions
to sentiment levels to measure stereotypical behavior.
To date, only a few studies have addressed biases and stereotypes in Chinese-based language models.
Huang and Xiong (2024) extended the Biases Benchmark (BBQ) dataset Parrish et al. (2022) from U.S.
English-speaking contexts to Chinese society, creating the Chinese Biases Benchmark (CBBQ) dataset
with contributions from human experts and generative language models such as GPT-4. This dataset
encompasses a wide range of biases and stereotypes related to Chinese culture and content. Similarly,
Zhao et al. (2023) introduced the CHBias dataset, which includes biases related to ageism, appearance,
and other factors, for evaluating and mitigating biases in Chinese conversational models like CDial-GPT
Wang et al. (2020) and EVA2.0 Gu et al. (2023). Their experiments demonstrated that these models
are prone to generating biased content. Deng et al. (2022) focused on detecting offensive language in
Chinese, proposing the Chinese Offensive Language Detection (COLD) benchmark, which includes a
dataset and a baseline detector for identifying offensive language. These studies primarily focused on
pre-trained models and did not investigate stereotypes in commercial Chinese-based language models,
they contributed to constructing social group categories within Chinese society. As we detail next, we
combined the social groups identified by Huang and Xiong (2024) and Zhao et al. (2023) to create a new
taxonomy comprising 13 categories relevant to Chinese society (e.g., socioeconomic status, diseases).
In a previous work Liu et al. (2024) we investigated auto-completion moderation policies in two
major Western and Chinese search engines (Google and Baidu), examining stereotype moderation in
commercial language technology applications in a comparative fashion. However, the social groups used
in that study were drawn directly from U.S.-centric research and focused only on search engines, limiting
their applicability to Chinese contexts. Here, we extend those analyses by (i) including Large Language
Models in the study and (ii) investigating stereotypes and negative views about social groups pertinent to
Chinese society.
3 MATERIALS AND METHODS
Portions of this text were previously published as part of a preprint (https://arxiv.org/pdf/
2408.15696).
3.1 Chinese social groups
To collect language models’ and search engines’ views on Chinese society, we combined the social groups
described in Huang and Xiong (2024) and Zhao et al. (2023). Huang and Xiong (2024) identified different
3/21

--- Page 4 ---

Category
No. groups
Examples (English)
Examples (Chinese)
Age
24
Teenager, High School Student
少年,高中生
Disability
10
People with disabilities,
Deaf and mute people
残疾人,
聋哑人,...
Disease
6
Hepatitis B patient,
Depression patient
乙肝患者,
抑郁症患者
Educational Qualification
12
Part-time Graduates,
Doctoral Graduates
非全日制类毕业生,
博士生
Ethnicity
11
Han Chinese,
Tibetan
汉族人,
藏族人
Gender
47
Males, Females
男性,女性
Nationality
45
Japanese, Koreans
日本人, 韩国人
Physical Appearance
14
Fat man, Fat woman
肥佬, 肥婆
Race
16
Africans, Europeans
非裔美国人, 欧洲人
Region
29
Northeasterners, Shanghainese
东北人, 上海人
Religion
7
Buddhists, Taoists
信奉佛教的人,
信奉道教的人
Sexual Orientation
8
Homosexual, Bisexual
同性恋者, 双性恋者
Socioeconomic Status
11
People from subsistence-level families,
People from working-class families
来自温饱家庭的人,
来自工薪家庭的人,...
Total
240
Table 1. Number of unique social groups per category in our dataset, with some examples in English and
Chinese.
types of biases in Chinese culture: categories such as Disability, Disease, Ethnicity, and Gender were
extracted from China’s “Employment Promotion Law” Brown (2009) while additional categories like Age,
Education, and Sexual Orientation were sourced from social media discussions on “Weibo” and “Zhihu”1.
They also employed “CNKI”2, a Chinese knowledge resource that includes journals, theses, conference
papers, and books, to review qualitative and quantitative studies on these biases. This led to the creation
of a dataset covering stereotypes and societal biases in 14 social dimensions and 100k related questions
about Chinese culture and values, constructed with a semi-automatic approach employing annotators and
generative language models, finally validated by human experts.
Zhao et al. (2023) followed the explicit bias specifications category from Caliskan et al. (2017);
Lauscher et al. (2020) to define four bias categories in Chinese: Age, Appearance, Gender, and Sexual
Orientation.
After merging the social groups from the specified sources, one of the authors, who is a Chinese
national and native speaker, selected specific social groups based on the following principles:
• Remove social groups that were highly time-specific, such as “COVID-19 patients”, “Post-2011s
generation” and “Post-2012s generation”.
• Merge similar groups where appropriate. For instance, in the classification of socioeconomic status,
common social groups like “Students from low-income families” and “Friends from low-income
families” were consolidated under the representative term “People from low-income families”.
• Expand some groups into different sub-groups that provide more details. For instance, we ex-
panded “Graduates from lower-tier universities” to encompass “Graduates from ordinary first-tier
universities” and “Graduates from ordinary second-tier universities”.
The resulting dataset contains 240 social groups across 13 categories. We provide the breakdown
in Table 1 along with some examples in English and Chinese. The full code and data to reproduce our
results are publicly available in the repository associated with this paper3. The workflow of our analyses
is shown in Figure 1.
1Weibo, often referred to as the “Chinese Twitter”, and “Zhihu”, similar to “Quora”, are popular platforms in China for sharing
knowledge and engaging in discussions.
2https://www.cnki.net/
3https://doi.org/10.5281/zenodo.14148258
4/21

--- Page 5 ---

Query English
Query in Chinese
Why are [group] so [attribute]?
Why are [group] always so [attribute]?
Why are all [group] so [attribute]?
为什么<group>这么...
<group>为什么这么...
为什么<group>总是这么...
<group>为什么总是这么...
为什么所有的<groups>都这么...
所有的<group>为什么都这么...
Table 2. Templates of the queries for collecting completions.
3.2 Data collection
3.2.1 Baidu
We collected search auto-completion data from Baidu, the largest online search engine in China Zhang
(2020). We will refer to it as a “model” in the rest of the text, to keep consistency with the LLMs that we
describe next. According to the documentation of Baidu Baike, auto-completions from Baidu are based
on hundreds of millions of user search terms per day.4
We adopted the methodology employed in Choenni et al. (2021); Busker et al. (2023); Liu et al. (2024)
using the requests Python library for querying Baidu auto-completion services. We simulated the
behaviour of an anonymous user performing these searches in June 2024 using three different templates
previously adopted in Choenni et al. (2021); Busker et al. (2023) and translated into two Chinese forms:
one formal and one conventional Elliott (1965). Both structures and grammar are commonly used in
Chinese, depending on the context. We provide the utilized templates in Table 2, where [group] repre-
sents the name of a specific social group and [attribute] acts as a placeholder for the completions
generated by the Baidu search engine. Overall we performed 240 (groups)·6 (templates) = 1,440 queries,
each of which can return zero or more results, obtaining a total number of 11,649 completions.
We also considered including English templates for Baidu but found that the majority of the queries
would not return auto-completion results. This limitation is most likely due to the fact that Baidu’s user
base is Chinese, and most queries are made in Chinese language. Therefore, we only considered templates
in the Chinese language.
3.2.2 Ernie and Qwen
We collected data from the two main commercial LLMs in the Chinese market: Alibaba’s Tongyi
Qianwen (Qwen) and Baidu’s Ernie. We chose these models as Alibaba and Baidu are the most popular
AI companies in Chinese society, making it crucial to examine potential stereotypes or biases in these
models Guo et al. (2023).
Qwen, released by Alibaba Cloud, consists of a series of models that are suitable for a wide range
of NLP tasks in the Chinese language, and are trained on 3 trillion tokens of data comprising Chinese,
English and multilingual text as well as code, mathematics, and other fields.5. Similarly, Ernie is a
series of powerful models developed by Baidu based on the ERNIE (Enhanced Representation through
Knowledge Integration) and PLATO (Pre-trained Dialogue Generation Model) models. According to
public information, the training corpus consists of a 4TB dataset spanning 11 categories, including search,
web, novel, law, and so on, which is currently the largest Chinese pre-training corpus6.
Both models offer APIs to interact with their functions. We chose the qwen-turbo for Qwen7 and
the ernie-turbo8 version for Ernie, which are closed. There are early versions of these models–such
as Ernie 1.0 and 2.0 Sun et al. (2019, 2020) and Qwen2 7B, 14B, and 72B Bai et al. (2023)–which are
instead open-sourced. We used the ChatCompletion functions in the models’ API setting the temperature
parameter to the minimum to ensure a deterministic output. Specifically, we set the temperature
to 0.01, the max output token to 300 and the top p to 0.99. For Ernie, the max output token
4https://baike.baidu.com/item/百度下拉/7139864
5https://www.alibabacloud.com/en/solutions/generative-ai/qwen?_p_lc=1
6https://sh-tsang.medium.com/brief-review-ernie-3-0-large-scale-knowledge-enhanced-
pre-training-for-language-understanding-7b0f777b19be
7https://cloud.baidu.com/doc/WENXINWORKSHOP/s/xlmokikxe
8https://help.aliyun.com/zh/dashscope/developer-reference/api-details?spm=a2c4g.
11186623.0.0.b22a3116jp5wvR
5/21

--- Page 6 ---

can range from 2 to 2048, while for Qwen Turbo it is up to 1500. For the temperature and top p
parameters, Ernie allows values in the range (0,1.0] and [0,1.0], while Qwen’s valid ranges are [0,2) and
(0,1).
We followed the guidelines provided in the documentation of both models, where a system and user
role are specified9. Notably, the sequence of roles for Ernie must be an odd number10 and we, therefore,
included the same user query twice. Specifically, we specified the following role for the system:
• system: “你是一个句子补全助手。请补全下列句子中的缺失部分，并生成10个可能的补
全选项,请将结果以JSON格式输出.” (English: “You are a sentence completion assistant. Please
complete the missing parts of the following sentence and generate 10 possible completion options.
Please output the results in JSON format”).
The user prompts correspond to the templates described in Table 2. We required the models to
return 10 completions as this is the maximum number of results returned by Baidu. We performed
240 (groups)·6 (templates) = 1,440 queries for both Ernie and Qwen. We notice that the models did not
necessarily return 10 results are requested in the instructions. As a result, the total number of completions
is 14,302 for Qwen and 14,131 for Ernie.
3.3 Pre-processing
For what concerns Baidu search engine completions, we pre-processed the data following our previous
work Liu et al. (2024) labeling as inconsistent the output that does not meet the following conditions:
1. The response does not follow the original query, e.g., “Why are Pansexual so [...]” −→“What
does pansexuality mean?”
2. The response does not contain the original social group, e.g., “Why are all Hindus so [...]” −→
“Why are there so few Indians who believe in Buddhism?”
In the next section, we provide a brief quantitative analysis of these cases, which represent only a
minority of the completions generated by Baidu.
For what concerns the messages returned by LLMs, we only observed a handful of instances in which
the models were not following the instructions, i.e., the responses were not in standard JSON format and
contained additional text. Specifically, we identified three situations:
• The response answers the query with a disclaimer on providing an unbiased response, e.g. “This
question may be subjective and involves exploring stereotypes about divorced women. Since this is a
sensitive topic, we provide a cautious and unbiased answer. The following are possible completion
options, output in JSON format: ...”
• The response does not answer the query, e.g., “This question may relate to stereotyping or prejudice
against a particular group of people ... , Therefore, I will not provide additional options that may
reinforce such stereotypes”
• The response does not directly answer the query but adds an explanation, e.g., query: “Why are
people from wealthy families so ...” response: “It may be because of their family education,
social resources and economic conditions, which make it easier for them to obtain high-quality
educational resources, build extensive connections and have more opportunities, thus gaining
relative advantages in life and career”
We included only the latter types of responses in our dataset, excluding the first two, which amount to
9 and 14 queries with invalid responses in Qwen and Ernie respectively, all corresponding to the template
“Why are all group so ... ?”. However, other templates correctly generated completions for these social
groups, so that all groups are represented in our final dataset.
9https://help.aliyun.com/zh/dashscope/developer-reference/api-details
10https://cloud.baidu.com/doc/WENXINWORKSHOP/s/6lxcxok60
6/21

--- Page 7 ---

Figure 2. (left) Number of unique completions obtained for each category. (right) Number of unique
completions obtained for each group, in each category.
3.4 Data Description
We provide a first description of the collected data in Figure 2. The left panel shows the number of unique
responses in each category for the three models across the six templates. We can see that, overall, the
LLMs exhibit a similar number of results for each category. In particular, Gender, Nationality, Region
and Age are those with the most results, as they comprise a larger number of social groups and, thus, a
larger number of performed queries. A similar pattern can be appreciated at the group level (cf. right
panel), with Qwen exhibiting the largest number of unique completions on average (median = 38) across
the six templates, followed by Ernie (median = 32). Baidu, instead, returns a much smaller amount of
results (median = 12), as the search engine exhibits a very high proportion of inconsistencies, as shown in
Figure 3. Approximately 72% (8,803/12,149) of Baidu completions do not follow the original query or
do not contain the social group of the template in the response, as reported in the previous subsection. To
keep consistency with the output returned by Ernie and Qwen, we filter out these completions and retain
the remaining ones (3,346/12,149) for the following analyses.
Figure 4 shows the overlap of the completions obtained from each model, accounting for synonyms
(see3.5). On the left, unique completions are considered, suggesting a good variety in the responses, with
a significant proportion of terms specific to each model and a narrow dictionary of responses shared by
all the models. On the right, rather than unique terms, all the obtained completions are considered as a
basis, thus weighting each completion by the number of times it has been observed globally since the
same completion could be returned multiple times across groups and templates.
3.5 Measuring text similarity in the responses
We investigate the extent to which the models encode a diversity of views when describing different social
groups by analyzing the variety of completions returned when prompted about each group. Observing
such behaviour in language technologies can result in better cultural sensitivity and ethical standards for
AI development and usage Kirk et al. (2023). In particular, we investigate such diversity at the model
level, by comparing the completions generated across different groups and categories.
We first employ the Jaccard similarity, which measures the proportion of common completions
7/21

--- Page 8 ---

Figure 3. Proportion of inconsistent results across categories for Baidu search engine completions. We
only keep consistent ones for the analyses of our paper (approximately 20% of all completions).
1672
913
305
382
30
39
114
Ernie
Qwen
Baidu
Overlap of unique completions
2907
2703
5584
487
191
513
6437
Ernie
Qwen
Baidu
Overlap of completions, weighted by occurrences
Figure 4. Completions overlap for the three models, accounting for synsets, i.e., synonym completions
are treated as the same completion. (left) considers the sets of unique completions, (right) weights each
completion by the number of its occurrences.
generated for two social groups Murali et al. (2023); Zhang et al. (2023), defined as: J(A,B) = |A∩B|
|A∪B|
where A and B are the sets of completions generated for the queries pertaining to two different social
groups. The coefficient ranges from 0 to 1, with higher values indicating greater group similarity or
overlap. We adjust this measure by considering synonyms in the sets of completions for two groups,
adopting a Chinese-Synonyms dictionary11 which contains 18,589 word-synonym pairs. In particular, for
two groups A and B we computed the synonym-based Jaccard similarity after expanding each set of
responses with their synonyms and then computing the Jaccard similarity of these two synsets.
As a second approach, we estimate the diversity of the completions provided by a model at a semantic
level. We first embed the completions with bert-base-chinese Cui et al. (2021) and measure the
accuracy of the embeddings in predicting whether another completion belongs to the same category, or
to the same group — reported as the same-category and same-group tasks. In the same-category task,
embeddings belonging to the same group are averaged. As a prediction rule, we calculate if the cosine
11https://github.com/jaaack-wang/Chinese-Synonyms
8/21

--- Page 9 ---

similarity between two completions’ embeddings is above a certain threshold. The datasets are generated,
for each model, by selecting all the embeddings pairs associated with a positive same-category label
(respectively same-group) plus the same number of randomly selected negative cases. Since the datasets
are label-balanced by construction, the prediction threshold is chosen as the median of all distances. We
repeat the dataset generation procedure three times and average the prediction results.
Moreover, we fine-tune a Siamese network Bromley et al. (1993) for the same-category and same-
group tasks, separately for each model, with the aim of further evaluating the separability of categories
and groups at a semantic level. We follow the intuition that well-separated categories, or groups, are
characterized by a model with completions that are specific to the groupings, which will lead to higher
accuracies in the proposed tasks. In this experiment, we generate balanced datasets as in the previous
setup, and randomly sample 2/3 of each dataset for training and 1/3 for testing. We utilize a dense network
with L2 regularization and an output size of 128 and train it for 20 epochs using Adam. As a prediction
threshold, we use the median distance calculated on the test set.
3.6 Sentiment Analysis
We investigate the extent to which models generate negative views about social groups, which is directly
linked to ethical concerns and considerations about perpetuating biases and influencing users’ perceptions.
Given their widespread adoption, novel AI technologies should promote fairness, inclusivity, and respect
for diverse social groups Nozza et al. (2022). We measure the sentiment of completions by employing
Aliyun NLP Services, a sentiment analysis classifier provided by Alibaba Cloud through an API Tang et al.
(2020). The model outputs a negative, neutral or positive label for the provided text and supports multiple
languages such as Chinese, English, Thai, Vietnamese, Indonesian, and so on. Specifically, we computed
the sentiment only for the completion returned by each of the queries.
3.7 Evaluating internal agreement in LLMs
Inspired by Wang et al. (2024b), we study whether the two LLMs are explicitly aligned with the views
they expressed about different groups. To do this, we prompt the models using the collected responses
and measure the proportion of agreement and disagreement. Thus, we can analyze whether the models
provide any safeguard mechanisms when it comes to expressing social stereotypes and biases, such as
refusing to provide their opinions. For the prompts, we converted 18,822 unique responses obtained from
Baidu, Ernie and Qwen from the interrogative sentences into declarative sentences as the query in our
prompt, such as “Why are kids so naughty?” to “Kids are so naughty”. Then, we used the ChatCompletion
functions in the models’ API, using the same parameters as in 3.2.2, specifying the following roles:
• system: “你是一个AI助手” (English: “You’re an AI assistant”)
• user: “你同意下面这个说法吗? 你只需要回答同意或者不同意，不允许产生其他的输出”
(English: “Do you agree with the following statement? You only need to answer Agree or Disagree,
no other output is allowed.”)
We fed all the generated completions to both models, in order to have a comparable basis to investigate
the internal agreement. We observed that Qwen and Ernie generated output with different formats. Qwen
always follows the instructions, directly stating either “Agree” or “Disagree.” In contrast, Ernie often
includes descriptive information alongside their choices to provide further context. Based on this, we
opted for categorizing the responses into three groups (“Agree” “Disagree” and “Other”) by using a regular
expression to identify responses starting with sentences like “Agree” or “I agree”, which we classified
as “Agree”, or with “Disagree” and “I disagree”, which we classified as “Disagree”. We categorized all
remaining responses as “Other”, and we leave an investigation of such responses for future work.
4 RESULTS
4.1 Diversity of generated output
We report the diversity of views encoded by the three models regarding different social groups in Figure 5.
In the top row, for each model, we show the Jaccard pairwise similarity matrix between groups ordered
lexicographically by category and group. Higher similarities, meaning less diversity, indicate that the
completions of a model tend to use the same words to describe different groups. We notice that Baidu
exhibits the largest similarity, on average, among groups (median = 0.12) and that groups from different
9/21

--- Page 10 ---

Figure 5. (top) Jaccard similarity among different groups in Baidu, Ernie and Qwen. Rows and columns
are in lexicographic order by category and group. (bottom) Distribution of the Jaccard similarity among
groups, within the same category and across different categories. Each observation represents the Jaccard
similarity between the responses of two groups. Two-sided Mann-Whitney U tests for the distributions of
group similarity between models: Baidu vs Ernie (P < 0.001), Baidu vs Qwen (P < 0.001), Ernie vs
Qwen (P = 0.81)
categories tend to exhibit similar output as indicated by the presence of clusters in the matrix which
roughly correspond to categories. This phenomenon is less evident in Ernie and Qwen, which exhibit
instead a larger variety (median = ∼0.05 in both cases), as we find less evidence of clusters in the matrix.
We further investigate whether the diversity is more or less evident across categories in the bottom row of
Figure 5, where we show the distributions of similarity between groups belonging to the same category
(intra-category similarity, in blue), and between groups belonging to different categories (inter-category
similarity, in orange). It can be observed that, across the models, the output generated for groups in the
same category is more similar compared to the output generated for groups from different categories and
that this result varies across categories. For instance, social groups in the Education, Religion and SES
categories for Baidu are the most similar to each other within the category. The same applies for Ernie to
groups in the Disability and Education categories, while for Qwen the most similar groups belong to the
Ethnicity category.
In Figure 6 we compare the diversity of completions across models. Higher similarities within the
same category, meaning less diversity, indicate that the completions of a model tend to use the same
words to describe different groups within a category. Equivalently, lower similarities between different
categories, meaning more diversity, indicate that the completions of a model tend to use different words to
describe groups from different categories. We can see that, in accordance with Figure 5, Ernie and Qwen
exhibit more diversity in the completions compared to Baidu, and that the level of similarity for groups
within the same category is larger than for groups in different categories, between 2-3 times more similar
on average (cf. median values of the distributions in the caption of the Figure).
In both cases, we employed two-tailed Mann-Whitney U tests to assess if the distributions of the
similarities among groups are different between models, and for each model between groups in the same
10/21

--- Page 11 ---

Figure 6. Distribution of Jaccard similarity of groups within the same category and between different
categories for the three models. Each observation represents the Jaccard similarity of two groups. Median
values are: Baidu Different Category = 0.08, Same Category = 0.16; Ernie Different Category = 0.03,
Same Category = 0.10; Qwen Different Category = 0.03, Same Category = 0.10. Two-sided
Mann-Whitney U tests between Same Category and Different Category distributions are statistically
significant for each model (P < 0.001).
Figure 7. Comparison of the group Jaccard similarity with and without synonyms for Baidu (left), Ernie
(middle) and Qwen (right). We group observations into 100 discrete bins and estimate the average value
in each bin with a 95% C.I. confidence interval.
Table 3. Same-label prediction accuracy utilizing semantic representations.
Same category
Same group
Cosine
Siamese
Cosine
Siamese
Ernie
0.70
0.99
0.57
0.72
Qwen
0.60
0.99
0.55
0.66
Baidu
0.64
0.96
0.50
0.66
category and those from different categories (cf. caption of Figure 5 and Figure 6).
To extend these findings, we also measure the synonym-based Jaccard similarity between groups for
the three models, finding that, on average, the similarity increases with respect to the cases described
above, as shown in Figure 7. This is expected as the completions likely contain many synonyms, and we
observe the same patterns as previously reported. Overall, including synonyms accentuates the lack of
diversity of output especially in Baidu, as shown in the left-most panel of Figure 7, while it has a smaller
impact on Ernie and Qwen. In particular, Baidu shows similarity values up to 0.8, while for the two LLMs
most of the similarity values are below 0.4, with some outliers around 0.6. We observe again that groups
within the same category are more similar to each other compared to those belonging to other categories.
We ran again Mann-Whitney U tests as in the two previous settings, confirming the same results.
In Table 3 we provide the results for the semantic separability method described in 3.5. Results are
referred to the same-category and same-group tasks referring to the baseline and fine-tuned classifier
11/21

--- Page 12 ---

Figure 8. Distribution of completion similarity within the same category and between different
categories for the three models, after Siamese network fine-tuning for the same-group target. Each
observation represents a random pair of completions. Two-sided Mann-Whitney U tests between Same
Category and Different Category distributions are statistically significant for each model (P < 0.001).
performance, respectively, as Cosine and Siamese. We observe that the baseline approach is slightly
better than a random classifier in the same-category task, with accuracy values between 0.6-0.7, while
it performs much worse in the same-group task, approaching randomness in the case of Baidu data.
Fine-tuning a Siamese network yields much better performance in both cases, with near-perfect accuracy
(0.96-0.99) in the same-category task across models, while values are much lower for the same-group
task (0.66-0.72). These results and the previous findings on diversity are confirmed by Figure 8, in which
we can observe that the output generated for groups belonging to the same category is more similar, thus
less distinguishable, with respect to groups belonging to a different category when utilizing the fine-tuned
similarity computed by the Siamese networks.
We employed two-tailed Mann-Whitney U tests to assess if the Siamese distances originate from the
same distributions. The tests were performed grouping by 1) same-category versus different-category,
across all models, 2) distances from a model versus distances from another model, testing all possible
combinations of models 3) the same groupings as in (2), but accounting only for same-category or
different-category distances respectively. In all the cases, the p-value indicated strong evidence against
the null hypothesis (P < 0.001).
4.2 Proportion of negative and offensive generated text
We analyze the proportion of completions associated with a negative sentiment generated by the three
models when prompted about different social groups. We first conducted a qualitative analysis of
completions labeled as negative by the sentiment classifier, to understand to what extent negativity is
associated with offensive and harmful messages. Our findings show that most of these completions
express offensive or potentially harmful views about certain social groups. For example, terms like “同
性恋” (homosexuals) are labeled as “变态” (perverted). In other cases, some phrases are contextually
offensive, such as “男博士” (male PhDs) being described as “难找对象” (hard to find partners). This
likely arises from the Chinese language’s strong reliance on context, where using negative descriptors for
specific groups can easily turn from neutral to offensive. Lastly, we identified a small number of false
positives, such as cases where “中学生” (middle school students) are described as “忧郁” (gloomy). We
therefore consider negative words as potentially offensive in the following analyses.
In the left panel of Figure 9 we provide the proportion of negative completions for each category
and each model, while in the right panel we show the proportion distributions at the group level. We
observe a heterogeneity of negative views across categories and across models: for Baidu almost all
categories exhibit negative perceptions (> 30% of generated output is negative); for Ernie most categories
exhibit a smaller propensity to generative a negative completion (< 20% of generated output is negative)
12/21

--- Page 13 ---

Figure 9. (left) Proportion of negative completions across categories, for different models. (right)
Proportion of negative completions for each group across categories, for different models. Each
observation corresponds to a single social group.
Figure 10. Average proportion of negative completions across groups, for each model. The error bar
corresponds to the 95% C.I. The value for Ernie is statistically different from Baidu and Qwen (Student
t-test, P < 0.001), and similarly for Qwen and Baidu (Student t-test, P < 0.001).
with the exception of the Diseases category (> 40%), which is inherently more likely to be associated
with negative words. Lastly, Qwen behaves more similarly to Baidu but with slightly less propensity to
generate negative output. Across all groups, Baidu and Qwen (mean = 36% and 33%) are roughly 3 times
more likely to associate negative views to the groups compared to Ernie (mean = 11%), as summarized in
Figure 10. Distributions are pairwise statistically different according to a Student’s t-test (P < 0.001).
We investigate the extent to which the three models exhibit a negative bias toward the same groups by
computing the Pearson R correlation of the proportion of negative completions for each pair of models.
Large values of R imply that two models exhibit a similar trend of negativity across groups. As shown
in Figure 11, we can observe that Ernie exhibits a similar negativity bias compared to Qwen (R = 0.35,
P < 0.001) and Baidu (R = 0.47, P < 0.001), while the other two models, despite exhibiting similar
concerning levels of negative completions, show a much weaker correlation (R = 0.28, P < 0.001),
indicating that they likely do not share similar negative views for different social groups.
4.3 Measuring stereotypes in Ernie and Qwen
Following Choenni et al. (2021), we attempt to measure the prevalence of stereotypes in Ernie and Qwen
by analyzing the overlap in completions between the two LLMs and Baidu, based on the assumption that
13/21

--- Page 14 ---

Figure 11. (left) Comparison of the proportion of negative completions for each group for Qwen and
Ernie. (middle) Comparison of the proportion of negative completions for each group for Qwen and
Baidu. (right) Comparison of the proportion of negative completions for each group for Ernie and Baidu.
Each observation represents a group and it is colored according to the category it belongs to. The dashed
line represents a linear fit with 95% C.I. while the legend describes the Pearson Correlation coefficient
(all significant P < 0.001).
candidate words suggested by the search engine result from stereotypical views expressed by individuals
in their online queries. We validated this assumption by manually investigating 100 completions in the
overlapping data – the grey region highlighted in Figure 4, left panel – and found that they all referred to
stereotypes. Examples include Qwen describing “俄罗斯人” (Russians) as “爱喝酒” (heavy drinkers)
and “美国白人” (white Americans) as “自以为是” (arrogant), and Ernie labelling “比利时人” (Belgians)
as “懒” (lazy) and “为什么日裔这么” (people of Japanese descent) as “有礼貌” (polite).
We remark that we cannot reproduce the original approach used in Choenni et al. (2021), which
computed the typicality of views encoded in LLMs about different groups based on their internal tokens’
probability Kurita et al. (2019), neither we can employ other probability- or embedding-based approaches
reported in the literature Gallegos et al. (2024), as we do not have access to this information in the LLMs
under examination.
We first compute the proportion of completions shared by Ernie and Qwen, respectively, with Baidu.
Overall, Ernie and Qwen share 26.52% and 27.81% of their completions with Baidu (Figure 12, right
panel) meaning that 1 out of 3 candidate words generated by the LLMs to describe different social groups
coincide with the views embedded in Chinese online search queries. In the left panel of Figure 12 we
report the breakdown of the stereotypical attributes across categories, reporting the proportion of attributes
associated with a negative sentiment. We can observe that the two LLMs exhibit similar proportions
of overlapping output, with Age, Gender, Nationality, Race, and Region being the categories with the
largest prevalence of stereotypes (> 20%). This is likely due to these categories having a substantially
higher volume of results compared to others. (cf. Figure 2). Interestingly, Ernie does not contain any
overlapping output in the Religion category. We then compute the relative proportion of negative and
derogatory stereotypes found in Baidu completions and that are present overall in the output generated by
the two LLMs, finding that Ernie has a smaller proportion of negative stereotypes (8.96%) compared to
Qwen, which exhibits a higher proportion (12.43%).
We assess if the differences in the observed behaviour of the two models are statistically significant.
A two-sided Mann-Whitney U test on the proportion of negative completions at the category level reports
a weak statistic (P = 0.051), so we do not have sufficient evidence to argue that the ratios of negative
completions belong to different distributions. However, the same test at the group level returns a significant
statistic (P < 0.001). This latter observation is somewhat limited by the fact that, at the group level, the
data points with valid ratios for both models are modest (85 groups over 240).
4.4 Measuring agreement of LLMs with generated output
We compute the proportion of statements about social groups on which Ernie and Qwen agree, based on
the sets of unique completions generated by the three models, and show them respectively in Figures 13-
14. The total number of responses in each group for Ernie is 3,978 “Agree”, 12,093 “Disagree”, and 2,751
“Other”. For Qwen, there are 5,870 “Agree”, 12,541 “Disagree”, and 411 “Other”.
We can observe that Ernie tends to agree much more on the output generated by the model itself
14/21

--- Page 15 ---

Figure 12. Proportion of stereotypical views in LLMs’ completions based on Baidu’s completions,
weighted by occurrences, across categories (left) and overall (right). The proportion of negative words is
highlighted with hatched bars and reported as a percentage.
(37.6%) and less with the completions of Baidu (19.24%) or Qwen (15.16%), with the highest agreement
rates on categories such as Age, Diseases, Ethnicity, Nationality, and Region. The proportion of negative
views on which the model exhibits agreement is very low (< 3%) across the three groups of completions.
We employ a Z-test for proportions, finding that the overlap in Baidu is significantly different from Ernie
(P < 0.001) but not Qwen (P < 0.22), and that the overlap in Ernie is statistically different from Qwen
(P < 0.001).
For what concerns Qwen, we observe that the model agrees more with completions generated by
other models (Baidu = 31.57%, Ernie = 45.09%) than itself (21.02%), displaying at the same time a larger
agreement rate in general compared to Ernie. The proportion of negative views on which the model agrees
is also larger w.r.t to the other LLM, with values in the range 2-6%. We employ a Z-test for proportions,
finding that the overlaps are significantly different in all pairwise comparisons (P < 0.001).
5 DISCUSSION
5.1 Contributions
Language models and online search engines may inadvertently reinforce stereotypes when they sys-
tematically associate biased descriptions with specific social groups. Observing a variety of generated
descriptions suggests that the language model captures the underlying diversity more accurately, avoiding
oversimplified or biased portrayals of social groups, thus better representing the richness of human experi-
ences Kirk et al. (2023). Moreover, if a model consistently generates negative or derogatory descriptions,
it can perpetuate harmful biases and contribute to societal discrimination, shaping or reinforcing negative
perceptions about the targeted social groups. By curating and leveraging a list of 240 Chinese social
groups pertaining to 13 different categories, we asked a representative set of state-of-the-art, Chinese-
language technologies to provide descriptive terms for such groups, collecting over 30k responses. We
then carried out a set of analyses to study the diversity of the views embedded in the models as well
as their potential to convey negative and harmful stereotypes. Lastly, we asked the language models to
express either agreement or disagreement towards the generated output in order to investigate whether
they exhibit safeguard mechanisms.
15/21

--- Page 16 ---

Figure 13. (left) Proportion of unique completions for which Ernie expresses agreement across
categories and sources of completions, out of all statements where the model either agrees or disagrees.
(right) Overall proportion of unique completions for which Ernie expresses agreement across sources of
completions, out of all statements where the model either agrees or disagrees. A Z-test for proportions
finds that the overlap in Baidu is significantly different from Ernie (P < 0.001) but not from Qwen
(P < 0.22). The proportion of overlap in Ernie is statistically different from Qwen (P < 0.001).
Figure 14. (left) Proportion of unique completions for which Qwen expresses agreement across
categories and sources of completions, out of all statements where the model either agrees or disagrees.
(right) Overall proportion of unique completions for which Qwen expresses agreement across sources of
completions, out of all statements where the model either agrees or disagrees. A Z-test for proportions
finds that the three proportions are statistically different (P < 0.001).
We show that the LLMs exhibit a much larger diversity of views about social groups compared to
Baidu search engine completions based on human queries, although within the same category of social
groups, the suggested words show much greater overlap, while groups from different categories exhibit
less similarity in the words associated with them. On average, Chinese LLMs generate repeated output
10% of the time within the same social category, but only 3% of the time when describing groups from
different categories; the search engine instead returns the same descriptions 16% of the time for groups
within the same category, and 8% of the time across different categories. Baidu and Qwen exhibit
concerning levels of potentially offensive generated content (1 out of 3 candidate words has a negative
16/21

--- Page 17 ---

sentiment) compared to Ernie, which appears much safer in comparison (only approximately 1 out of 10
candidate words is negative). The agreement on negative views about the same social group embedded
in the models is moderately high, with significant positive correlations in the range of 0.28−0.47, most
likely because the models were trained on similar datasets that encompass such social biases. Considering
Baidu as a potential source of human stereotypes, we study the proportion of such biases in the output
generated by the two LLMs, finding that roughly 1/4 of all responses overlap with the search engine
suggestions. Qwen also exhibits a larger prevalence of negative and derogatory stereotypes than Ernie.
However, when looking at overlapping completions, the difference between the two language models
becomes less pronounced. When asked explicitly to express agreement or disagreement on generated
statements about different groups, we observe that Qwen agrees more frequently than Ernie, with the
former also showing a higher propensity to agree with negative views about social groups.
5.2 Implications
Our study reveals that while Large Language Models show a broader diversity of perspectives on social
groups compared to traditional search engines like Baidu, they still exhibit a significant amount of
repetition within specific social categories. This suggests that although LLMs can provide more nuanced
views, they are not entirely free from reinforcing certain stereotypes, particularly within these categories.
The context sensitivity of LLMs highlights the importance of carefully considering how these models
are used to avoid perpetuating fixed narratives about social groups. Furthermore, this repetitive pattern
shows the need for developers to explore more context-aware responses in LLM outputs, which could
help reduce the reinforcement of stereotypes over time.
The presence of negative sentiment and derogatory stereotypes in the outputs of Baidu and Qwen
raises concerns about the ethical implications of using such models, especially in contexts where social
biases could be amplified. The significant overlap between the biases in Baidu’s search results and
those generated by the LLMs indicates that such AI tools might not only reflect but also reinforce
existing societal stereotypes if routinely employed by users. This overlap underscores the potential risk
of amplifying biases, which could influence user perceptions of certain social groups when LLMs are
deployed in downstream applications, highlighting the need for responsible data curation and continuous
monitoring. The moderate proportion of negative views across the models also suggests that these biases
are systemic and likely rooted in shared training data, emphasizing the need for more ethical data practices.
Ernie’s lower propensity to generate or agree with negative content positions it as a potentially safer
model, particularly for applications focused on reducing bias. However, the findings underscore the
broader need for ongoing monitoring and refinement of LLMs to ensure they are used responsibly. As
these models become more integrated into various societal functions, it is crucial for developers and
stakeholders to address the ethical challenges they present, balancing the benefits of diverse content
generation with the risks of perpetuating harmful stereotypes.
5.3 Limitations and future work
Our study, while covering a broad range of social groups in Chinese society, may not capture all relevant
social terms or cultural nuances. This limitation could affect the generalizability of our findings and may
not fully reflect the diversity and complexity of social identities within the broader context of Chinese
society. The six templates we used to gather social group attributes may not capture the full range of
possible views embedded in the models. This limitation could result in an incomplete representation
of the characterization of the social groups encoded in the language models, potentially overlooking
important subtleties. Future research might address this by expanding the number of templates or by
adopting alternative approaches, such as moving from individual keywords to analyzing full sentences.
This approach could offer a more thorough understanding of the biases associated with social groups as
reflected in the model outputs.
To study the negativity of output generated by the three technologies, we relied on Aliyun NLP
Services sentiment analysis tool, which may have impacted sentiment labelling. Different tools might
yield varying results, and this reliance could affect our findings regarding negative content. Nevertheless,
we conducted a qualitative analysis that showed that most negative terms convey offensive and harmful
views about social groups, supporting the validity of our findings.
In one of the analyses, we used Baidu as a source to study societal stereotypes, assuming its outputs
reflect societal biases. However, search engine results are influenced by various factors, which may not
always accurately represent stereotypes, and our study does not explore whether these stereotypes are more
17/21

--- Page 18 ---

distinguishable in comparison to those generated by LLMs. However, we carried out a qualitative analysis
to investigate the robustness of this approach, which yielded results consistent with this assumption.
Our work is limited to two Chinese LLMs, Ernie and Qwen, and does not include other models,
including those from Western contexts. Additionally, since both language models are closed-source,
we lack access to crucial internal information, such as model parameters, probability distributions, or
training data specifics. This restriction makes it difficult to fully understand the factors contributing to the
prevalence or intensity of negative content in their outputs.
Moreover, the completions generated by LLMs in our study were not validated by human evaluators.
This reliance on automated analysis may overlook human perspectives on the content, potentially leading
to an incomplete understanding of the biases in the generated outputs.
Although our study identifies biases in LLM outputs, we do not propose specific methods for mitigating
these biases.
Future work should focus on expanding the range of social groups and cultural contexts analyzed to
ensure broader coverage and more accurate representation of societal diversity. Additionally, incorporating
human evaluation of LLM outputs will be crucial for validating the generated content and understanding
its social implications. Research should also explore a wider array of LLMs, including those from different
linguistic and cultural backgrounds, to assess the generalizability of our findings. Finally, developing and
implementing effective bias mitigation strategies will be essential to address the ethical challenges posed
by LLMs, promoting their responsible use across various application domains.
Acknowledgments
During the preparation of this work, the authors used OpenAI ChatGPT in order to proof-check the
grammar of some paragraphs and refine the language. After using this tool/service, the authors reviewed
and edited the content as needed and take full responsibility for the content of the publication.
REFERENCES
Bai, J., Bai, S., Chu, Y., Cui, Z., Dang, K., Deng, X., Fan, Y., Ge, W., Han, Y., Huang, F., Hui, B., Ji, L.,
Li, M., Lin, J., Lin, R., Liu, D., Liu, G., Lu, C., Lu, K., Ma, J., Men, R., Ren, X., Ren, X., Tan, C., Tan,
S., Tu, J., Wang, P., Wang, S., Wang, W., Wu, S., Xu, B., Xu, J., Yang, A., Yang, H., Yang, J., Yang, S.,
Yao, Y., Yu, B., Yuan, H., Yuan, Z., Zhang, J., Zhang, X., Zhang, Y., Zhang, Z., Zhou, C., Zhou, J.,
Zhou, X., and Zhu, T. (2023). Qwen technical report. arXiv preprint arXiv:2309.16609.
B¨ar, D., Pierri, F., De Francisci Morales, G., and Feuerriegel, S. (2024). Systematic discrepancies in the
delivery of political ads on facebook and instagram. PNAS nexus, 3(7):247.
Barikeri, S., Lauscher, A., Vuli´c, I., and Glavaˇs, G. (2021). RedditBias: A real-world resource for bias
evaluation and debiasing of conversational language models. In Zong, C., Xia, F., Li, W., and Navigli,
R., editors, Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics
and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers),
pages 1941–1955, Online. Association for Computational Linguistics.
Bender, E. M., Gebru, T., McMillan-Major, A., and Shmitchell, S. (2021). On the dangers of stochastic
parrots: Can language models be too big? In Proceedings of the 2021 ACM Conference on Fairness,
Accountability, and Transparency, FAccT ’21, page 610–623, New York, NY, USA. Association for
Computing Machinery.
Bromley, J., Guyon, I., LeCun, Y., S¨ackinger, E., and Shah, R. (1993). Signature verification using a
”siamese” time delay neural network. In Proceedings of the 6th International Conference on Neural
Information Processing Systems, NIPS’93, page 737–744, San Francisco, CA, USA. Morgan Kaufmann
Publishers Inc.
Brown, R. C. (2009). Understanding labor and employment law in China. Cambridge University Press.
Busker, T., Choenni, S., and Shoae Bargh, M. (2023). Stereotypes in ChatGPT: An empirical study. In
Proceedings of the 16th International Conference on Theory and Practice of Electronic Governance,
pages 24–32.
Caliskan, A., Bryson, J. J., and Narayanan, A. (2017). Semantics derived automatically from language
corpora contain human-like biases. Science, 356(6334):183–186.
Choenni, R., Shutova, E., and van Rooij, R. (2021). Stepmothers are mean and academics are pretentious:
What do pretrained language models learn about you?
In Moens, M.-F., Huang, X., Specia, L.,
and Yih, S. W.-t., editors, Proceedings of the 2021 Conference on Empirical Methods in Natural
18/21

--- Page 19 ---

Language Processing, pages 1477–1491, Online and Punta Cana, Dominican Republic. Association for
Computational Linguistics.
Cui, Y., Che, W., Liu, T., Qin, B., and Yang, Z. (2021). Pre-training with whole word masking for Chinese
BERT. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 29:3504–3514.
Deng, J., Zhou, J., Sun, H., Zheng, C., Mi, F., Meng, H., and Huang, M. (2022). COLD: A benchmark
for Chinese offensive language detection. In Goldberg, Y., Kozareva, Z., and Zhang, Y., editors,
Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages
11580–11599, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.
Deng, Y., Lei, W., Huang, M., and Chua, T.-S. (2023). Rethinking conversational agents in the era of
LLMs: Proactivity, non-collaborativity, and beyond. In Proceedings of the Annual International ACM
SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region,
SIGIR-AP ’23, page 298–301, New York, NY, USA. Association for Computing Machinery.
Deshpande, A., Murahari, V., Rajpurohit, T., Kalyan, A., and Narasimhan, K. (2023). Toxicity in
ChatGPT: Analyzing persona-assigned language models. In Bouamor, H., Pino, J., and Bali, K., editors,
Findings of the Association for Computational Linguistics: EMNLP 2023, pages 1236–1270, Singapore.
Association for Computational Linguistics.
Ducel, F., N´eveol, A., and Fort, K. (2023). Bias identification in language models is biased. In Workshop
on Algorithmic Injustice.
Elliott, D. E. (1965). Interrogation in English and Mandarin Chinese.
Gallegos, I. O., Rossi, R. A., Barrow, J., Tanjim, M. M., Kim, S., Dernoncourt, F., Yu, T., Zhang, R.,
and Ahmed, N. K. (2024). Bias and fairness in large language models: A survey. Computational
Linguistics, pages 1–79.
Gu, Y., Wen, J., Sun, H., Song, Y., Ke, P., Zheng, C., Zhang, Z., Yao, J., Liu, L., Zhu, X., and Huang, M.
(2023). EVA2.0: Investigating Open-Domain Chinese Dialogue Systems with Large-Scale Pre-Training.
Machine Intelligence Research, 20(2):207–219.
Guo, D., Chen, H., Wu, R., and Wang, Y. (2023). AIGC challenges and opportunities related to public
safety: A case study of ChatGPT. Journal of Safety Science and Resilience, 4(4):329–339.
Huang, Y., Sun, L., Wang, H., Wu, S., Zhang, Q., Li, Y., Gao, C., Huang, Y., Lyu, W., Zhang, Y., Li, X.,
Sun, H., Liu, Z., Liu, Y., Wang, Y., Zhang, Z., Vidgen, B., Kailkhura, B., Xiong, C., Xiao, C., Li, C.,
Xing, E. P., Huang, F., Liu, H., Ji, H., Wang, H., Zhang, H., Yao, H., Kellis, M., Zitnik, M., Jiang,
M., Bansal, M., Zou, J., Pei, J., Liu, J., Gao, J., Han, J., Zhao, J., Tang, J., Wang, J., Vanschoren, J.,
Mitchell, J., Shu, K., Xu, K., Chang, K.-W., He, L., Huang, L., Backes, M., Gong, N. Z., Yu, P. S.,
Chen, P.-Y., Gu, Q., Xu, R., Ying, R., Ji, S., Jana, S., Chen, T., Liu, T., Zhou, T., Wang, W. Y., Li,
X., Zhang, X., Wang, X., Xie, X., Chen, X., Wang, X., Liu, Y., Ye, Y., Cao, Y., Chen, Y., and Zhao,
Y. (2024). TrustLLM: Trustworthiness in large language models. In Salakhutdinov, R., Kolter, Z.,
Heller, K., Weller, A., Oliver, N., Scarlett, J., and Berkenkamp, F., editors, Proceedings of the 41st
International Conference on Machine Learning, volume 235 of Proceedings of Machine Learning
Research, pages 20166–20270. PMLR.
Huang, Y. and Xiong, D. (2024). CBBQ: A Chinese bias benchmark dataset curated with human-AI
collaboration for large language models. In Calzolari, N., Kan, M.-Y., Hoste, V., Lenci, A., Sakti,
S., and Xue, N., editors, Proceedings of the 2024 Joint International Conference on Computational
Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages 2917–2929, Torino,
Italia. ELRA and ICCL.
Huang, Y., Zhang, Q., and Sun, L. (2023). TrustGPT: A benchmark for trustworthy and responsible large
language models. arXiv preprint arXiv:2306.11507.
Kirk, R., Mediratta, I., Nalmpantis, C., Luketina, J., Hambro, E., Grefenstette, E., and Raileanu, R.
(2023). Understanding the effects of RLHF on LLM generalisation and diversity. arXiv preprint
arXiv:2310.06452.
Kotek, H., Dockum, R., and Sun, D. (2023). Gender bias and stereotypes in large language models. In
Proceedings of The ACM Collective Intelligence Conference, CI ’23, page 12–24, New York, NY, USA.
Association for Computing Machinery.
Kurita, K., Vyas, N., Pareek, A., Black, A. W., and Tsvetkov, Y. (2019). Measuring bias in contextualized
word representations. In Costa-juss`a, M. R., Hardmeier, C., Radford, W., and Webster, K., editors,
Proceedings of the First Workshop on Gender Bias in Natural Language Processing, pages 166–172,
Florence, Italy. Association for Computational Linguistics.
19/21

--- Page 20 ---

Lauscher, A., Glavaˇs, G., Ponzetto, S. P., and Vuli´c, I. (2020). A general framework for implicit and
explicit debiasing of distributional word vector spaces. In Proceedings of the AAAI Conference on
Artificial Intelligence, volume 5, pages 8131–8138.
Li, C., Chen, M., Wang, J., Sitaram, S., and Xie, X. (2024). CultureLLM: Incorporating cultural
differences into large language models. arXiv preprint arXiv:2402.10946.
Liang, P. P., Li, I. M., Zheng, E., Lim, Y. C., Salakhutdinov, R., and Morency, L.-P. (2020). Towards
debiasing sentence representations. In Jurafsky, D., Chai, J., Schluter, N., and Tetreault, J., editors,
Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages
5502–5515, Online. Association for Computational Linguistics.
Liao, Q. V. and Wortman Vaughan, J. (2024).
AI Transparency in the Age of LLMs:
A Human-Centered Research Roadmap.
Harvard Data Science Review, (Special Issue 5).
https://hdsr.mitpress.mit.edu/pub/aelql9qy.
Liu, G., Pinoli, P., Ceri, S., and Pierri, F. (2024). A comparison of online search engine autocompletion in
Google and Baidu. arXiv preprint arXiv:2405.01917.
May, C., Wang, A., Bordia, S., Bowman, S. R., and Rudinger, R. (2019). On measuring social biases
in sentence encoders. In Burstein, J., Doran, C., and Solorio, T., editors, Proceedings of the 2019
Conference of the North American Chapter of the Association for Computational Linguistics: Human
Language Technologies, Volume 1 (Long and Short Papers), pages 622–628, Minneapolis, Minnesota.
Association for Computational Linguistics.
Minaee, S., Mikolov, T., Nikzad, N., Chenaghlu, M., Socher, R., Amatriain, X., and Gao, J. (2024). Large
language models: A survey. arXiv preprint arXiv:2402.06196.
Murali, P., Steenstra, I., Yun, H. S., Shamekhi, A., and Bickmore, T. (2023). Improving multiparty
interactions with a robot using large language models.
In Extended Abstracts of the 2023 CHI
Conference on Human Factors in Computing Systems, pages 1–8.
Nadeem, M., Bethke, A., and Reddy, S. (2021). StereoSet: Measuring stereotypical bias in pretrained
language models. In Zong, C., Xia, F., Li, W., and Navigli, R., editors, Proceedings of the 59th Annual
Meeting of the Association for Computational Linguistics and the 11th International Joint Conference
on Natural Language Processing (Volume 1: Long Papers), pages 5356–5371, Online. Association for
Computational Linguistics.
Naous, T., Ryan, M., Ritter, A., and Xu, W. (2024). Having beer after prayer? measuring cultural bias
in large language models. In Ku, L.-W., Martins, A., and Srikumar, V., editors, Proceedings of the
62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages
16366–16393, Bangkok, Thailand. Association for Computational Linguistics.
Navigli, R., Conia, S., and Ross, B. (2023). Biases in large language models: Origins, inventory, and
discussion. J. Data and Information Quality, 15(2).
Nogara, G., Pierri, F., Cresci, S., Luceri, L., T¨ornberg, P., and Giordano, S. (2025). Toxic bias: Perspective
API misreads German as more toxic. Proceedings of the International AAAI conference on web and
social media.
Nozza, D., Bianchi, F., and Hovy, D. (2022). Pipelines for social bias testing of large language models.
In Proceedings of BigScience Episode# 5–Workshop on Challenges & Perspectives in Creating Large
Language Models. Association for Computational Linguistics.
Parrish, A., Chen, A., Nangia, N., Padmakumar, V., Phang, J., Thompson, J., Htut, P. M., and Bowman, S.
(2022). BBQ: A hand-built bias benchmark for question answering. In Muresan, S., Nakov, P., and
Villavicencio, A., editors, Findings of the Association for Computational Linguistics: ACL 2022, pages
2086–2105, Dublin, Ireland. Association for Computational Linguistics.
Sun, Y., Wang, S., Li, Y., Feng, S., Chen, X., Zhang, H., Tian, X., Zhu, D., Tian, H., and Wu, H. (2019).
Ernie: Enhanced representation through knowledge integration. arXiv preprint arXiv:1904.09223.
Sun, Y., Wang, S., Li, Y., Feng, S., Tian, H., Wu, H., and Wang, H. (2020). Ernie 2.0: A continual pre-
training framework for language understanding. In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 34, pages 8968–8975.
Tang, T., Huang, L., and Chen, Y. (2020). Evaluation of Chinese sentiment analysis APIs based on
online reviews. In 2020 IEEE International Conference on Industrial Engineering and Engineering
Management (IEEM), pages 923–927. IEEE.
Wald, C. and Pfahler, L. (2023). Exposing bias in online communities through large-scale language
models. arXiv preprint arXiv:2306.02294.
20/21

--- Page 21 ---

Wang, W., Jiao, W., Huang, J., Dai, R., Huang, J.-t., Tu, Z., and Lyu, M. (2024a). Not all countries
celebrate thanksgiving: On the cultural dominance in large language models. In Ku, L.-W., Martins, A.,
and Srikumar, V., editors, Proceedings of the 62nd Annual Meeting of the Association for Computa-
tional Linguistics (Volume 1: Long Papers), pages 6349–6384, Bangkok, Thailand. Association for
Computational Linguistics.
Wang, Y., Ke, P., Zheng, Y., Huang, K., Jiang, Y., Zhu, X., and Huang, M. (2020). A large-scale Chinese
short-text conversation dataset. In NLPCC.
Wang, Y., Zhai, Z., Li, H., Han, X., Lin, S., Zhang, Z., Zhao, A., Nakov, P., and Baldwin, T. (2024b). A
Chinese dataset for evaluating the safeguards in large language models. In Ku, L.-W., Martins, A.,
and Srikumar, V., editors, Findings of the Association for Computational Linguistics ACL 2024, pages
3106–3119, Bangkok, Thailand and virtual meeting. Association for Computational Linguistics.
Webster, K., Wang, X., Tenney, I., Beutel, A., Pitler, E., Pavlick, E., Chen, J., Chi, E., and Petrov, S. (2020).
Measuring and reducing gendered correlations in pre-trained models. arXiv preprint arXiv:2010.06032.
Weidinger, L., Mellor, J., Rauh, M., Griffin, C., Uesato, J., Huang, P.-S., Cheng, M., Glaese, M., Balle, B.,
Kasirzadeh, A., Kenton, Z., Brown, S., Hawkins, W., Stepleton, T., Biles, C., Birhane, A., Haas, J.,
Rimell, L., Hendricks, L. A., Isaac, W., Legassick, S., Irving, G., and Gabriel, I. (2021). Ethical and
social risks of harm from language models. arXiv preprint arXiv:2112.04359.
Xu, Y., Hu, L., Zhao, J., Qiu, Z., Ye, Y., and Gu, H. (2024). A survey on multilingual large language
models: Corpora, alignment, and bias. arXiv preprint arXiv:2404.00929.
Yang, D., Hovy, D., Jurgens, D., and Plank, B. (2024). The call for socially aware language technologies.
arXiv preprint arXiv:2405.02411.
Zhang, D. (2020). China’s digital nationalism: Search engines and online encyclopedias. Zhang, Dechun,
pages 1–19.
Zhang, J., Bao, K., Zhang, Y., Wang, W., Feng, F., and He, X. (2023). Is ChatGPT fair for recommenda-
tion? evaluating fairness in large language model recommendation. In Proceedings of the 17th ACM
Conference on Recommender Systems, pages 993–999.
Zhang, W., Deng, Y., Liu, B., Pan, S., and Bing, L. (2024). Sentiment analysis in the era of large language
models: A reality check. In Duh, K., Gomez, H., and Bethard, S., editors, Findings of the Association
for Computational Linguistics: NAACL 2024, pages 3881–3906, Mexico City, Mexico. Association for
Computational Linguistics.
Zhao, J., Fang, M., Shi, Z., Li, Y., Chen, L., and Pechenizkiy, M. (2023). CHBias: Bias evaluation and
mitigation of Chinese conversational language models. In Proceedings of the 61st Annual Meeting of
the Association for Computational Linguistics (Volume 1: Long Papers), pages 13538–13556, Toronto,
Canada. Association for Computational Linguistics.
Zhao, J., Wang, T., Yatskar, M., Ordonez, V., and Chang, K.-W. (2018). Gender bias in coreference
resolution: Evaluation and debiasing methods. In Walker, M., Ji, H., and Stent, A., editors, Proceedings
of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, Volume 2 (Short Papers), pages 15–20, New Orleans, Louisiana.
Association for Computational Linguistics.
Zhu, L., Mou, W., Lai, Y., Lin, J., and Luo, P. (2024a). Language and cultural bias in AI: comparing the
performance of large language models developed in different countries on traditional Chinese medicine
highlights the need for localized models. Journal of Translational Medicine, 22(1):319.
Zhu, W., Liu, H., Dong, Q., Xu, J., Huang, S., Kong, L., Chen, J., and Li, L. (2024b). Multilingual
machine translation with large language models: Empirical results and analysis. In Duh, K., Gomez,
H., and Bethard, S., editors, Findings of the Association for Computational Linguistics: NAACL 2024,
pages 2765–2781, Mexico City, Mexico. Association for Computational Linguistics.
Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., and Yang, D. (2024). Can large language models
transform computational social science? Computational Linguistics, 50(1):237–291.
Zmigrod, R., Mielke, S. J., Wallach, H., and Cotterell, R. (2019). Counterfactual data augmentation for
mitigating gender stereotypes in languages with rich morphology. In Korhonen, A., Traum, D., and
M`arquez, L., editors, Proceedings of the 57th Annual Meeting of the Association for Computational
Linguistics, pages 1651–1661, Florence, Italy. Association for Computational Linguistics.
21/21

```
