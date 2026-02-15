---
title: "2025-Wen-Yi-Do Chinese models speak Chinese languages - PDF Extract"
source_pdf: "2025-Wen-Yi-Do Chinese models speak Chinese languages.pdf"
pages: 19
extracted_at: "2026-02-15T17:54:28.799762"
---

# PDF Extract: 2025-Wen-Yi-Do Chinese models speak Chinese languages

**Source PDF:** 2025-Wen-Yi-Do Chinese models speak Chinese languages.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

Preprint. Under review.
Do Chinese models speak Chinese languages?
Andrea W Wen-Yi∗
Unso Eun Seo Jo∗
David Mimno
Cornell University
andreawwenyi@infosci.cornell.edu unsojo@cornell.edu mimno@cornell.edu
Abstract
The release of top-performing open-weight LLMs has cemented China’s
role as a leading force in AI development. Do these models support lan-
guages spoken in China? Or do they speak the same languages as Western
models? Comparing multilingual capabilities is important for two reasons.
First, language ability provides insights into pre-training data curation, and
thus into resource allocation and development priorities. Second, China
has a long history of explicit language policy, varying between inclusivity
of minority languages and a Mandarin-first policy. To test whether Chinese
LLMs today reflect an agenda about China’s languages, we test perfor-
mance of Chinese and Western open-source LLMs on Asian regional and
Chinese minority languages. Our experiments on Information Parity and
reading comprehension show Chinese models’ performance across these
languages correlates strongly (r=0.93) with Western models’, with the sole
exception being better Mandarin. Sometimes, Chinese models cannot iden-
tify languages spoken by Chinese minorities such as Kazakh and Uyghur,
even though they are good at French and German. These results provide
a window into current development priorities, suggest options for future
development, and indicate guidance for end users.
1
Introduction
China has become a global leader in open-source AI with a series of high performing LLMs
(Yang et al., 2024; DeepSeek-AI, 2025; Young et al., 2024; Yang et al., 2023; Cai et al., 2024).
In particular, DeepSeek-R1’s open weight release in January 2025 sent shockwaves beyond
the AI community with its efficient training protocol matched with outstanding reasoning
capabilities (Huang, 2025; Goldman, 2025). But these models give insights beyond technical
solutions. As LLMs are increasingly multilingual, their performance across languages
and dialects reveals much about the socio-political factors and decisions underlying their
development (Ramesh et al., 2023; Koenecke et al., 2020; Bender, 2019; Bella et al., 2024).
What about LLMs from China — a country with a complex language policy presiding over
1.4 billion people including dozens of minority groups (Erard, 2009)? In this context, Chinese
AI technology has incentives both for multilingual support and for linguistic homogeneity.
Historically, Chinese rulers used language as a political tool to classify and govern multiple
ethnicities and cultures. These policies have changed in their degree of language inclusivity,
ranging from assimilationist to pluralist over centuries (Mullaney, 2011). Today, modern
China has a complex language environment that is at a middle ground between the U.S.
(one dominant language) and Europe (many competing languages), where the dominant
language is Mandarin Chinese, but hundreds of other languages continue to be used by
Chinese citizens (Eberhard et al., 2024b).1 Linguistic diversity and classification remains a
sensitive and contentious topic in China (Erard, 2009; Bradley, 2005).
AI technologies are the product of an identifiable political, cultural, and regulatory landscape
that underlies their development (Yew et al., 2025; Huang et al., 2024; ˇSabanovi´c, 2010).
∗Equal contribution.
1Yue Chinese (Cantonese) has more than 80 million native speakers, surpassing Korean speakers
(Eberhard et al., 2024a)
1
arXiv:2504.00289v2  [cs.CL]  7 Apr 2025

--- Page 2 ---

Preprint. Under review.
Multilingual language support in LLMs is one way to gauge these influences as it takes
resource commitment. It is also much easier to observe than LLM alignment which requires
clear definitions of moral and cultural value judgments. To understand China’s approach to
showcasing its AI to the world, its domestic linguistic policy, and internal tech demands,
we test mulitilingual performance of LLMs from China.
We identify four hypotheses about Chinese multilingual LLM performance:
• Null Hypothesis: There is no difference in language support between Chinese
and Western models. Performance across languages is highly correlated between
Chinese and Western LLMs, suggesting a similar approach to data collection and
use of datasets.
• Mandarin Hypothesis: Chinese models are better than Western models at Man-
darin but not at other languages. Chinese organizations allocated additional
resources to improve Mandarin performance, incentivized by socio-political context
and ease of access to Mandarin data.
• Pluralist Hypothesis: Chinese models are better than Western models at Man-
darin and other languages spoken in China. While Mandarin is the dominant
language, Chinese companies are responding to the growing popularity for dialects
and non-Mandarin languages on social media and technology platforms (Chu, 2022;
Li et al., 2024; Jing & Anni, 2024).2
• Regional Hypothesis: Chinese models are better than Western models at Man-
darin and other languages spoken in the greater East and Southeast Asian regions
but not at Chinese minority local languages. Historically, China and the greater
Asian region share linguistic and cultural commonalities.3. Chinese firms also have
economic incentive to address languages of larger populations or market power in
greater Asia, such as Korean and Japanese.
To test these hypotheses, we investigate 6 Chinese and 4 western models on 21 language vari-
ants, spanning Mandarin Chinese, Chinese minority languages, Asian regional languages,
and European languages. We evaluate multilingual performance using both task-agnostic
and task-dependent experiments, measuring Information Parity, machine reading compre-
hension, and language identification.
Our experiments yield the strongest evidence for the Mandarin Hypothesis, that Chinese
LLMs are giving more attention to Mandarin but not other Chinese languages. We also find
difficulty to reject the Null Hypothesis, as Chinese LLMs’ performance across languages is
highly correlated with that of Western models. We do not find evidence for the Pluralist
and Regional hypotheses. Beyond the nation-specific level, we see evidence that many
high-performing open models may be trained on similar distributions of language data.
At the same time, accompanying technical reports have become increasingly terse and
unreliable even for open-source models (Achiam et al., 2023). There may be an inadvertent
homogenization effect as public datasets become saturated.
2
Related Works and Historical Context
Multilingual LLMs
LLMs have grown increasingly multilingual over the last few years
(Conneau et al., 2020; Brown et al., 2020; Workshop et al., 2022), with teams spending
significant effort in improving and evaluating low-resource languages in LLMs (Abadji
et al., 2022; ImaniGooghari et al., 2023). Various studies corroborate the socio-cultural
2There is increasing demand for machine translation between Mandarin Chinese and China’s
minority languages, such as Tibetan, Mongolian, and Uyghurs, to foster the “the political, economic,
and cultural exchanges” between China and their minority populations (Zhang et al., 2024b).
3China has historically been a regional “Middle Kingdom” with influence in the greater Asian
regional “tributary states” such as Korea and Vietnam. Also, many modern scientific and social
vocabulary are shared pan-Asia via translation of western concepts. For instance, many Asian
languages adopted Japanese western scientific terms (“wasei-kango”: Japanese-made Chinese words)
such as physics (butsurin/物理) or phone (denwa/電話).
2

--- Page 3 ---

Preprint. Under review.
Category
Language
FLORES+
BELEBELE
MC2
Mandarin Chinese
Mandarin (Simplified)
✓
✓
-
Mandarin (Traditional)
✓
✓
-
Chinese Han Dialects (Other)
Yue (Cantonese)
✓
-
-
Chinese Minority
Jingpho
✓
✓
-
Lhasa Tibetan
✓
✓
✓
Uyghur
✓
-
✓
Mongolian
-
-
✓
Kazakh
-
-
✓
Northeast Asian
Korean
✓
✓
-
Japanese
✓
✓
-
Southeast Asian
Indonesian
✓
✓
-
Lao
✓
✓
-
Burmese
✓
✓
-
Thai
✓
✓
-
Vietnamese
✓
✓
-
Standard Malay
✓
✓
-
European
English
⋆
✓
-
French
✓
✓
-
Italian
✓
✓
-
Spanish
✓
✓
-
German
✓
✓
-
Table 1: Languages evaluated in each experiment. “Chinese minority” category indicates
languages also used by populations in China that the PRC determines as “minority ethnic
group”. We evaluate the Kazakh in Kazakh Arabic script and Mongolian in Traditional
Mongolian script, which are writing systems used in China. ⋆: English is used as the
reference language (Tsvetkov & Kipnis, 2024).
value of multilingual support in tech systems. Linguistic diversity in language technology
promotes access to information for more people (Lee, 2020) and helps preserve low-resource
languages (Bird & Chiang, 2012). For example, New Zealand’s Te Hiku Media and Africa’s
Masakhane are examples of community efforts to preserve under-resourced languages
through language technology (Coffey, 2021; Nekoto et al., 2020; Adelani et al., 2023).
Language Policy in China
For thousands of years, central governments in China have
used language as a tool to manage a vast multiethnic population that speaks over a hundred
languages and dialects. These policies have alternated from being pluralist to assimilationist
over the eras. One of the earliest such mandates, in 221 B.C., was the First Emperor of
Qin’s program to standard the Chinese script as a move to consolidate central state power
after unifying the warring states. More recently, following the 1949 Communist Revolution,
the Chinese Communist Party (CCP) launched extensive linguistic campaigns to unite the
minority population of over 106 million people who spoke 129 languages among them to
build an inclusive Chinese nation (Mullaney, 2011).4
China adopted a more assimilationist approach in the late twentieth century with a monolin-
gual policy (“one nation, one language”) that promoted Mandarin as the “super language”
in a 1982 constitutional amendment.
Yet, digital frontiers have seen grassroots efforts to promote linguistic inclusivity. For exam-
ple, the 2005 convening of the National Conference on the Standardization and Computerization
of Minority Languages and Writing, and publications such as the “Ethnic Language Edition of
the Linux Operating System and Office Suite” and “Advances in China’s Minority Language
Processing” signal these attempts.
AI Policy in China
The PRC government has been taking steps to regulate LLMs and
generative AI. In July 2023, China’s Cyberspace Administration issued the Administration
of Generative AI Services (the “Interim AI Measures”), requiring generative AI services with
4Also known as “Multinational state building”
3

--- Page 4 ---

Preprint. Under review.
Chinese Minorities
Southeast Asian
Northeast Asian
European
Chinese Han Dialects (Other)
Mandarin Chinese
0.2
0.4
0.6
0.8
Mandarin (Traditional)
Mandarin (Simplified)
Yue (Cantonese)
Italian
Spanish
German
French
Korean
Japanese
Burmese
Lao
Thai
Standard Malay
Vietnamese
Indonesian
Jingpho
Lhasa Tibetan
Uyghur
Mean IP Across Sentences
Languages
Model Source
Western
China
(a) Instruction-tuned models
Chinese Minorities
Southeast Asian
Northeast Asian
European
Chinese Han Dialects (Other)
Mandarin Chinese
0.2
0.4
0.6
0.8
Mandarin (Traditional)
Mandarin (Simplified)
Yue (Cantonese)
Italian
Spanish
German
French
Korean
Japanese
Burmese
Lao
Thai
Standard Malay
Vietnamese
Indonesian
Jingpho
Lhasa Tibetan
Uyghur
Mean IP Across Sentences
Languages
Model Source
Western
China
(b) Base models
Figure 1: Information Parity of Chinese models vs. Western models.
“public opinion attributes” or “social mobilization capabilities” undergo rigorous security
assessments.
The Interim AI Measures require that all AI-generated content comply with five principles
such as upholding socialist values, preventing discriminatory content, and implementing
transparency and reliability measures. As of January 2025, 302 generative AI services had
completed the mandatory government filing process to comply with these requirements
(Cyberspace Administration of China, 2025). Indeed, users have reported that models
like Deepseek-R1 refused to engage with certain topics deemed sensitive by the Chinese
government such as Taiwan, Tibet, and Tiananmen Square and instead digress to chat about
math, coding, and logic (Yang, 2024).
Data is central to these regulation efforts. When training AI models, the Interim AI Measures
require providers to use lawfully sourced data and avoid infringing on intellectual property
rights. They must also employ measures to enhance training data quality, truthfulness,
accuracy, objectivity, and diversity and comply with national laws.5 These requirements
are broadly defined and can include minority languages, but there is no explicit mention
of language and cultural inclusivity. In other words, there is no evidence of top-down
pressure for Chinese organizations to commit resources for minority languages. In 2017,
China announced the New Generation AI Development Plan to lead China to become a
‘major AI innovation center’ by 2030. In this ‘New Generation’ AI era, what is China’s AI
language policy and how does it relate to minority languages?
3
Experiments
3.1
Models
We selected our models to optimize for fair comparison while accounting for sufficient
variability. In order to provide the fairest comparison among models, we restrict experiments
to models of 7–9 billion parameters. This scale is sufficient for at-or-near state of the art
performance while limiting computational complexity. We experiment with both base and
instruction-tuned open-source LLMs that we access through the Hugging Face transformers
5Chinese national Cybersecurity Law, Data Security Law, and Personal Information Protection
4

--- Page 5 ---

Preprint. Under review.
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Average IP of Western instruction-tuned models
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Average IP of Chinese instruction-tuned models
Mandarin (Simplified)
Mandarin (Traditional)
Yue (Cantonese)
Correlation (r = 0.925, p value = 0.000)
Language Category
Southeast Asian
European
Northeast Asian
Chinese Minorities
Mandarin Chinese
Chinese Han Dialects (Other)
(a) Information Parity (IP)
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Average MRC accuracy of Western instruction-tuned models
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Average MRC accuracy of Chinese instruction-tuned models
Mandarin (Simplified)
Mandarin (Traditional)
Correlation (r = 0.991, p value = 0.000)
Language Category
Southeast Asian
European
Northeast Asian
Chinese Minorities
Mandarin Chinese
(b) MRC Accuracy
Figure 2: Correlation of IP and MRC Accuracy between Chinese and Western instruction-
tuned models across languages. Across languages, the two model groups have a Pearson
correlation of 0.925 in IP and 0.991 in MRC accuracy.
library(Wolf et al., 2020).6 Mindful of the bias of the primarily Western platform, we selected
top-performing models with significant traction.
We
evaluate
the
following
models
developed
by
Chinese
organizations
(base
models
in
paranthesis):
Qwen2.5-7B-Instruct
(Qwen2.5-7B)
(Yang
et
al.,
2024),
Yi-1.5-9B-Chat (Yi-1.5-9B) (Young et al., 2024), DeepSeek-R1-Distill-Qwen-7B (DeepSeek-
AI, 2025), DeepSeek-R1-Distill-Llama-8B (DeepSeek-AI, 2025), InternLM3-8b-instruct
(InternLM2.5-7B) (Cai et al., 2024), and Baichuan2-7B-Chat (Baichuan2-7B-Base) (Yang
et al., 2023). We also evaluate the following Western models developed in the U.S. or
France: Llama-3-8B-Instruct (Llama3-8B) (AI@Meta, 2024), Mistral-7B-Instruct-v0.3
(Mistral-7B-v0.3) (Jiang et al., 2023), OLMo-2-1124-7B-Instruct (OLMo-2-1124-7B) (OLMo
et al., 2024), and Gemma-2-9b-it (Gemma2-9b) (Gemma Team, 2024).
3.2
Data and Experiments
Datasets that allow comparable evaluations across a range of high- and low-resource lan-
guages are scarce, but we identify three datasets that allow us to quantify model perfor-
mance on multilingual data through three experiments. These experiments include both
task-agnostic and task-dependent evaluations.
Experiment 1: Information Parity
We conduct a task-agnostic evaluation utilizing the
FLORES+ benchmark for multilingual machine translation (Goyal et al., 2022; NLLB Team
et al., 2024). The benchmark has 997 English samples sentences from Wiki sources.7 These
sentences are translated into target languages by native speakers and professional translators.
This high quality dataset includes parallel translations across around 200 language variants,
including many low-resource languages. Example English sentences are in appendix C.
To measure multilingual capabilities, we calculate Information Parity (IP), an index proposed
by Tsvetkov & Kipnis (2024). IP aims to measure the comparative efficiency of representing
the same information in a reference language R to a target language L. Suppose a text input
in the reference language textR is translated to a target language textL, and NLL(text) is the
sum of negative log-likelihood of a text input (refer to Appendix B for formal definition), IP
is defined by:
IP(textL) = NLL(textR)
NLL(textL)
(1)
6We will release code upon acceptance.
7We use the dev split of FLORES+.
5

--- Page 6 ---

Preprint. Under review.
Chinese Minorities
Southeast Asian
Northeast Asian
European
Mandarin Chinese
20
40
60
80
Mandarin (Traditional)
Mandarin (Simplified)
Italian
German
Spanish
French
English
Japanese
Korean
Lao
Burmese
Thai
Standard Malay
Vietnamese
Indonesian
Lhasa Tibetan
Jingpho
MRC Accuracy (%)
Languages
Model Source
Western
China
Models
DeepSeek−R1−Qwen
(a) Instruction-tuned models
Chinese Minorities
Southeast Asian
Northeast Asian
European
Mandarin Chinese
20
40
60
80
Mandarin (Traditional)
Mandarin (Simplified)
German
Italian
Spanish
French
English
Japanese
Korean
Lao
Burmese
Thai
Vietnamese
Standard Malay
Indonesian
Lhasa Tibetan
Jingpho
MRC Accuracy (%)
Languages
Model Source
Western
China
(b) Base models
Figure 3: MRC Accuracy of Chinese vs. Western models. Chinese models have higher
accuracy in reading comprehension questions than Western models in Mandarin. With
base models, Chinese models have higher accuracy than Western models in most languages
except Burmese, Lao, Jingpho, and Tibetan. But both groups are similar on their instruction-
tuned models across all languages. We notice that DeepSeek-R1-Qwen is more competitive
with its custom chat template (See Appendix Figure 7). Since we apply a consistent prompt
across all models for comparability, we exclude DeepSeek-R1-Qwen from the grouped bar
results. Instead, we highlight its performance with the more effective chat template using a
green triangle in (a).
We use English as the reference language for textR because all models have been shown to
be good at it. Higher IP score means higher efficiency in language-agnostic information
representation. In other words, language input textL with higher IP(textL) score means
closer alignment with English reference input textR.
Compared to other popular task-agnostic metrics such as tokenization parity (Petrov et al.,
2023) and fertility (Rust et al., 2021), IP is a better predictor of downstream task performance
(Tsvetkov & Kipnis, 2024). It is also a more robust multilingual measure than perplexity
because it is less affected by tokenizer differences (Wang et al., 2022). We evaluate IP on 18
language variants from FLORES+, spanning languages spoken in China, Northeast Asia,
Southeast Asia, and Europe. See Table 1 for the full list.
Experiment 2: Machine Reading Comprehension
We evaluate the models’ natural lan-
guage understanding (NLU) performance on the Belebele benchmark, a multilingual ma-
chine reading comprehension (MRC) dataset. For each language, there are 900 multiple-
choice questions, each with one passage, four answer choices, and one correct option. The
dataset is fully parallel across 122 high- to low-resource languages. It is curated and verified
by translators fluent in both English and the target language (Bandarkar et al., 2024).
Our experiments follow the setup in the original Belebele paper: we query models with
zero-shot prompts and calculate accuracy of the models’ answers. See an example question
and prompt in Appendix D. Similar to Experiment 1, we evaluate models’ performance on
17 languages spoken in China, Northeast Asia, Southeast Asia, US/Europe (Table 1).
Experiment 3
As Chinese minority languages are under-represented in the previous two
experiments, we conduct an additional experiment on four minority languages: Tibetan,
Mongolian, Kazakh, and Uyghur. We use the Multilingual Corpus of Minority Languages
in China (MC2) by Zhang et al. (2024a), to test the models’ language identification ability.
For each language, we prompt models to identify the language of 101 texts from the MC2
6

--- Page 7 ---

Preprint. Under review.
Chinese Minorities
Southeast Asian
Northeast Asian
European
Chinese Han Dialects (Other)
Mandarin Chinese
0.2
0.4
0.6
0.8
Mandarin (Simplified)
Yue (Cantonese)
French
Japanese
Lao
Vietnamese
Lhasa Tibetan
Mean IP Across Sentences
Languages
Models
Qwen2.5−Instruct
Yi−1.5−Chat
DeepSeek−R1−Llama
DeepSeek−R1−Qwen
InternLM3−Instruct
Baichuan2−Chat
Llama3−Instruct
Mistral−Instruct
Olmo2−Instruct
Gemma2−Instruct
(a) Information Parity (IP)
Chinese Minorities
Southeast Asian
Northeast Asian
European
Mandarin Chinese
20
40
60
80
Mandarin (Simplified)
French
English
Japanese
Lao
Vietnamese
Lhasa Tibetan
MRC Accuracy (%)
Languages
Models
Qwen2.5−Instruct
Yi−1.5−Chat
DeepSeek−R1−Llama
DeepSeek−R1−Qwen
InternLM3−Instruct
Baichuan2−Chat
Llama3−Instruct
Mistral−Instruct
Olmo2−Instruct
Gemma2−Instruct
(b) MRC Accuracy
Figure 4: Average IP (vs. English) and MRC Accuracy of each instruction-tuned model
for select languages. In both figures, Chinese LLMs are represented by circle markers,
and Western LLMs by diamond-plus markers. The vertical line in the MRC figure is the
0.25 random baseline. Chinese LLMs all have higher IP than Western LLMs in Simplified
Mandarin. In MRC accuracy, Gemma2-Instruct is consistently the highest, and DeepSeek
models underperform. The order of models stays similar across languages, except in Tibetan,
where most models are near random.
corpus.8 We adopt a lenient approach and count the output as correct if it contains the
language name. See prompt in Appendix E.
4
Results
4.1
Experiment 1: Information Parity
We show instruction-tuned models’ IP scores averaging across 997 translated sentences on a
selection of languages (Figure 4a). Gemma2 and Qwen2.5 have the highest average IPs in most
languages. In Simplified Mandarin, all Chinese models have higher IP than Western models.
See Appendix Figure 8 for the full model-language results.
The IP distribution of Chinese and Western models on all 18 languages is shown in Figure
1. We exclude DeepSeek-R1-Llama from this figure as it is a US model (Llama) fine-tuned
by a Chinese organization (Deepseek). We observe that Chinese LLMs, both base and
instruction-tuned, have significantly higher IPs than Western models in Mandarin Chinese.
In Cantonese as well, Chinese LLMs have higher IPs and lower variance. Chinese instruction-
tuned models have lower IP variability in Japanese, Korean, Vietnamese, and Malay than
base models and Western instruction-tuned models have higher IPs in European language.
Despite, these performance differences, when it comes to Chinese minority languages, both
Chinese and Western LLMs have low IP and similar variance. See Appendix Figure 9 to see
full results on of instruction-tuned models.
In fact, taking the models’ performance distribution across all languages, Western and
Chinese models show a high correlation. The Pearson correlation of average IP for Chinese
and Western model groups is 0.925 for instruction-tuned models (Figure 2a), and 0.929 for
base models (Appendix Figure 11a).
8Kazakh and Mongolian both have multiple writing systems. MC2 collects the writing system
predominantly used by speakers in China: Kazakh in Arabic script and Mongolian in Traditional
Mongolian script.
7

--- Page 8 ---

Preprint. Under review.
5
0
5
10
15
20
25
30
35
Change in MRC accuracy (%) with instruction-tuning
Qwen2.5
Yi-1.5
InternLM2.5
Baichuan2
Llama3
Mistral
OLMo2
Gemma2
Base Model
Model Source
China
Western
5
0
5
10
15
20
25
30
35
Change in MRC accuracy (%) with instruction-tuned vs. base models
Mandarin (Simplified)
Mandarin (Traditional)
English
French
German
Spanish
Italian
Japanese
Korean
Indonesian
Vietnamese
Standard Malay
Thai
Lao
Burmese
Lhasa Tibetan
Jingpho
Language
Model Source
China
Western
Figure 5: Change in MRC accuracy with instruction-tuned vs. base models. Instruction-
tuned models generally outperform their base versions, especially Llama3.
Western
instruction-tuned models show a larger accuracy gain over their base models across most
languages compared to Chinese models.
4.2
Experiment 2: Machine Reading Comprehension
The MRC accuracy for all models on selected languages shows a wider distribution
than IP (4b ). We see Gemma2-Instruct consistently outperforms other models, whereas
Deepseek-R1-Qwen and Baichuan2-Chat consistently underperform (See Figure 10 for full
language/model breakdown for both instruction-tuned and base models).
We look at China’s models vs. Western models’ MRC accuracies across 17 languages in
Figure 3.9 As in Experiment 1, Chinese LLMs are significantly better in Mandarin Chinese.
MRC accuracies in other languages are similar between Chinese and Western instruction-
tuned models. However with base models, Chinese models are better than Western models
in almost every language except in those with low accuracy, namely Burmese, Lao, Jingpho
and Tibetan (Figure 3b).
We observe that Chinese and Western models exhibit different results when instruction-
tuned. As expected, we find that instruction-tuned models have higher accuracy than their
base counterparts overall (Figure 5). However, this effect is larger in Western models across
most languages except in Burmese, Lao, Jingpho and Tibetan. Notably, the instruction-
tuning effect on Llama3 far exceeds others’ — twice as big as the other base types — with the
median increase of 25% over the base. While we tested various chat templates and system
prompt designs for instuction-tuned models, we do not observe significant differences
except for DeepSeek models. See Appendix Figure 7.
With MRC, the correlation between Chinese and Western models is even stronger than in
Experiment 1. The Pearson correlation is 0.991 for instruction-tuned models (Figure 2b),
and 0.984 for base models (Appendix Figure 11b).
4.3
Experiment 3: Language identification of low-resource minority languages in China
Our language identification experiments on four Chinese minority languages reveals that
overall, models have higher success identifying Tibetan and Mongolian than Uyghur
and Kazakh (Figure 6). All models are bad at identifying Kazakh. Most models can-
not identify Uyghur. And most models can identify at least 75% of Tibetan and Mongolian.
Llama3-Instruct is uniquely good at Uyghur, and is also top-performing in Tibetan and
Mongolian. Baichuan2 is consistently the worst in every language. For results of base
models, see Appendix Figure 12.
9As done in Experiment 1, we exclude DeepSeek-R1-Llama.
8

--- Page 9 ---

Preprint. Under review.
5
Discussion and Conclusion
Kazakh
Mongolian
Tibetan
Uyghur
0
25
50
75
100
Language Identification Accuracy (%)
Languages
Models
Qwen2.5−Instruct
Yi−1.5−Chat
DeepSeek−R1−Llama
DeepSeek−R1−Qwen
InternLM3−Instruct
Baichuan2−Chat
Llama3−Instruct
Mistral−Instruct
Olmo2−Instruct
Gemma2−Instruct
Figure 6: Language identification accuracy
for 4 Chinese minority languages in the MC2
corpus.
From our experiment results we make the
following three observations: First, Chi-
nese models are better at Mandarin than
are Western models. Second, Chinese mod-
els are just as bad at Chinese minority lan-
guages as are Western models. Some Chi-
nese models even fail to identify minor-
ity languages such as Uyghur and Kazakh.
Third, Chinese models’ performance across
languages highly correlates with those of
Western models. Like Western models, Chi-
nese models are better at European lan-
guages such as French and German but un-
derperform at Chinese minority languages.
Our results support the Mandarin Hypoth-
esis — Chinese models are better at Man-
darin than Western models but not at other
languages spoken in China. The de facto
practice for language AI development there-
fore seems to be Mandarin-first. This con-
trasts with China’s mid-twentieth century
linguistic pluralism approach, where the
Chinese government following the Communist revolution invested resources to collect,
categorize, and study minority languages in China (Mullaney, 2011). Our finding suggests
that developers of Chinese open-source models may not have easily accessible resources
for Chinese minority language research, nor the pressure to meet performance standards in
local languages. Instead, a look at the technical reports shows Chinese models are largely
evaluated on Western AI standards (Orr & Kang, 2024). For example, DeepSeek-R1 is evalu-
ated on 10 English benchmarks, compared to 3 in Mandarin Chinese. The reasoning-related
benchmarks that DeepSeek-R1 evaluated on are also in English (DeepSeek-AI, 2025). The
Qwen2.5 family is explicitly evaluated on multiple languages, including Arabic, Japanese,
Korean, and Turkish, but not on Chinese minority languages (Yang et al., 2024). 10
Meanwhile, we cannot reject Null Hypothesis, as we observe a high correlation on mul-
tilingual performance between Western and Chinese models. This suggests Chinese and
Western models may be trained on data with similar multilingual proportions. Coupled
with the Western-centered evaluation strategies, this corroborates that China’s open-source
LLMs maybe motivated more for global display and competition than utility for local users.
For end users of Asian regional languages, Gemma2 and Qwen2.5 generally outperform other
open-source models. For Mandarin-English bilingual use, Chinese models, notably Qwen2.5
and InternLM3 are a better option. One will gain the increased performance of Mandarin
Chinese without losing much in other languages compared to using a Western LLM.11
Direction for future model development
There is both good news and bad news about
our findings. On the one hand, we have shown through a study of multilingual support,
the current space of open-source models is highly homogeneous. The data available for
multilingual open source models may be somewhat saturated. On the other hand, this
means there are unique opportunities for groups with domain-specific or language-specific
data to gain an edge even against open-source models trained by large organizations.
This could be a unique opportunity for Chinese organizations to expand their multilingual
influence. Developers and researchers can tackle the lagging performance of minority
languages by investing in the digitization and evaluation of the 100+ spoken languages in
10We provide additional information on pretraining data collection in Appendix Table 2.
11See Appendix A for Limitations.
9

--- Page 10 ---

Preprint. Under review.
mainland China. In this way, China has a singular advantage in setting new standards and
metrics for its minority languages.
References
Julien Abadji, Pedro Ortiz Suarez, Laurent Romary, and Benoˆıt Sagot. Towards a cleaner
document-oriented multilingual crawled corpus. In Nicoletta Calzolari, Fr´ed´eric B´echet,
Philippe Blache, Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, Hitoshi
Isahara, Bente Maegaard, Joseph Mariani, H´el`ene Mazo, Jan Odijk, and Stelios Piperidis
(eds.), Proceedings of the Thirteenth Language Resources and Evaluation Conference, pp. 4344–
4355, Marseille, France, June 2022. European Language Resources Association. URL
https://aclanthology.org/2022.lrec-1.463.
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni
Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al.
Gpt-4 technical report. arXiv preprint arXiv:2303.08774, 2023.
David Ifeoluwa Adelani, Marek Masiak, Israel Abebe Azime, Jesujoba Alabi, Atnafu Lam-
bebo Tonja, Christine Mwase, Odunayo Ogundepo, Bonaventure F. P. Dossou, Akin-
tunde Oladipo, Doreen Nixdorf, Chris Chinenye Emezue, Sana Al-azzawi, Blessing
Sibanda, Davis David, Lolwethu Ndolela, Jonathan Mukiibi, Tunde Ajayi, Tatiana
Moteu, Brian Odhiambo, Abraham Owodunni, Nnaemeka Obiefuna, Muhidin Mo-
hamed, Shamsuddeen Hassan Muhammad, Teshome Mulugeta Ababu, Saheed Abdullahi
Salahudeen, Mesay Gemeda Yigezu, Tajuddeen Gwadabe, Idris Abdulmumin, Mahlet
Taye, Oluwabusayo Awoyomi, Iyanuoluwa Shode, Tolulope Adelani, Habiba Abdul-
ganiyu, Abdul-Hakeem Omotayo, Adetola Adeeko, Abeeb Afolabi, Anuoluwapo Aremu,
Olanrewaju Samuel, Clemencia Siro, Wangari Kimotho, Onyekachi Ogbu, Chinedu
Mbonu, Chiamaka Chukwuneke, Samuel Fanijo, Jessica Ojo, Oyinkansola Awosan,
Tadesse Kebede, Toadoum Sari Sakayo, Pamela Nyatsine, Freedmore Sidume, Oreen
Yousuf, Mardiyyah Oduwole, Kanda Tshinu, Ussen Kimanuka, Thina Diko, Siyanda
Nxakama, Sinodos Nigusse, Abdulmejid Johar, Shafie Mohamed, Fuad Mire Hassan,
Moges Ahmed Mehamed, Evrard Ngabire, Jules Jules, Ivan Ssenkungu, and Pontus
Stenetorp. MasakhaNEWS: News topic classification for African languages. In Jong C.
Park, Yuki Arase, Baotian Hu, Wei Lu, Derry Wijaya, Ayu Purwarianti, and Adila Alfa
Krisnadhi (eds.), Proceedings of the 13th International Joint Conference on Natural Language
Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computa-
tional Linguistics (Volume 1: Long Papers), pp. 144–159, Nusa Dua, Bali, November 2023.
Association for Computational Linguistics. doi: 10.18653/v1/2023.ijcnlp-main.10. URL
https://aclanthology.org/2023.ijcnlp-main.10/.
AI@Meta. Llama 3 model card, 2024. URL https://github.com/meta-llama/llama3/blob/
main/MODEL CARD.md.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya Narayan Shukla,
Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian
Khabsa. The belebele benchmark: a parallel reading comprehension dataset in 122
language variants. arXiv preprint arXiv:2308.16884, 2023.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya Narayan Shukla,
Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian
Khabsa. The belebele benchmark: a parallel reading comprehension dataset in 122
language variants. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), Proceedings
of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pp. 749–775, Bangkok, Thailand, August 2024. Association for Computational
Linguistics. doi: 10.18653/v1/2024.acl-long.44. URL https://aclanthology.org/2024.
acl-long.44/.
G´abor Bella, Paula Helm, Gertraud Koch, and Fausto Giunchiglia. Tackling language
modelling bias in support of linguistic diversity. In Proceedings of the 2024 ACM Conference
on Fairness, Accountability, and Transparency, FAccT ’24, pp. 562–572, New York, NY, USA,
10

--- Page 11 ---

Preprint. Under review.
2024. Association for Computing Machinery. ISBN 9798400704505. doi: 10.1145/3630106.
3658925. URL https://doi.org/10.1145/3630106.3658925.
Emily
M.
Bender.
The
#benderrule:
On
naming
the
languages
we
study
and
why
it
matters,
2019.
URL
https://thegradient.pub/
the-benderrule-on-naming-the-languages-we-study-and-why-it-matters/.
Last
Accessed:2025-03-26.
Steven Bird and David Chiang.
Machine translation for language preservation.
In
Martin Kay and Christian Boitet (eds.), Proceedings of COLING 2012: Posters, pp. 125–
134, Mumbai, India, December 2012. The COLING 2012 Organizing Committee. URL
https://aclanthology.org/C12-2013.
David Bradley.
Introduction: Language policy and language endangerment in china.
International Journal of the Sociology of Language, 2005(173):1–21, 2005. doi: 10.1515/ijsl.
2005.2005.173.1.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al.
Language models are few-shot learners. Advances in neural information processing systems,
33:1877–1901, 2020.
Zheng Cai, Maosong Cao, Haojiong Chen, Kai Chen, Keyu Chen, Xin Chen, Xun Chen, Zehui
Chen, Zhi Chen, Pei Chu, et al. Internlm2 technical report. arXiv preprint arXiv:2403.17297,
2024.
Siyi
Chu.
Speaking
up:
Can
social
media
save
china’s
di-
alects?,
2022.
URL
https://www.theworldofchinese.com/2022/08/
speaking-up-can-social-media-save-chinas-dialects/.
Last
Accessed:2025-03-
26.
Donavyn Coffey. M¯aori are trying to save their language from big tech, 2021. URL https:
//www.wired.com/story/maori-language-tech/. Accessed: 2025-03-27.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume
Wenzek, Francisco Guzm´an, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin
Stoyanov. Unsupervised cross-lingual representation learning at scale. In Dan Jurafsky,
Joyce Chai, Natalie Schluter, and Joel Tetreault (eds.), Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, pp. 8440–8451, Online, July 2020.
Association for Computational Linguistics. doi: 10.18653/v1/2020.acl-main.747. URL
https://aclanthology.org/2020.acl-main.747.
Cyberspace Administration of China. Announcement of the cyberspace administration
of china on the disclosure of recorded information for generative artificial intelligence
services, 2025. URL https://www.cac.gov.cn/2025-01/08/c 1738034725920930.htm. Ac-
cessed: 2025-03-27.
DeepSeek-AI. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement
learning, 2025. URL https://arxiv.org/abs/2501.12948.
David M. Eberhard, Gary F. Simons, and Charles D. Fennig (eds.). Ethnologue: Languages
of the world. twenty-seventh edition, 2024a. URL http://www.ethnologue.com.
David M. Eberhard, Gary F. Simons, and Charles D. Fennig (eds.). Ethnologue: China, 2024b.
URL https://www.ethnologue.com/country/CN/. Accessed: 2025-03-26.
Michael Erard. How many languages? linguists discover new tongues in china. Science,
324(5925):332–333, 2009. doi: 10.1126/science.324.5925.332a. URL https://www.science.
org/doi/full/10.1126/science.324.5925.332a.
Gemma Team. Gemma. 2024. doi: 10.34740/KAGGLE/M/3301. URL https://www.kaggle.
com/m/3301.
11

--- Page 12 ---

Preprint. Under review.
David Goldman. What is deepseek, the chinese ai startup that shook the tech world?
CNN, 2025.
URL https://www.cnn.com/2025/01/27/tech/deepseek-ai-explainer/
index.html. Accessed: 2025-03-11.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary, Peng-Jen Chen, Guillaume Wenzek, Da Ju,
Sanjana Krishnan, Marc’Aurelio Ranzato, Francisco Guzm´an, and Angela Fan. The
Flores-101 evaluation benchmark for low-resource and multilingual machine translation.
Transactions of the Association for Computational Linguistics, 10:522–538, 2022. doi: 10.1162/
tacl a 00474. URL https://aclanthology.org/2022.tacl-1.30.
Raffaele Huang. Silicon valley is raving about a made-in-china ai model. The Wall Street Jour-
nal, 2025. URL https://www.wsj.com/tech/ai/china-ai-deepseek-chatbot-6ac4ad33.
Accessed: 2025-03-11.
Saffron Huang, Divya Siddarth, Liane Lovitt, Thomas I. Liao, Esin Durmus, Alex Tamkin,
and Deep Ganguli. Collective constitutional ai: Aligning a language model with pub-
lic input.
In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and
Transparency, FAccT ’24, pp. 1395–1417, New York, NY, USA, 2024. Association for
Computing Machinery.
ISBN 9798400704505.
doi: 10.1145/3630106.3658979.
URL
https://doi.org/10.1145/3630106.3658979.
Ayyoob ImaniGooghari, Peiqin Lin, Amir Hossein Kargaran, Silvia Severini, Masoud
Jalili Sabet, Nora Kassner, Chunlan Ma, Helmut Schmid, Andr´e Martins, Franc¸ois
Yvon, and Hinrich Sch¨utze. Glot500: Scaling multilingual corpora and language mod-
els to 500 languages.
In Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki
(eds.), Proceedings of the 61st Annual Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pp. 1082–1117, Toronto, Canada, July 2023. Associa-
tion for Computational Linguistics. doi: 10.18653/v1/2023.acl-long.61. URL https:
//aclanthology.org/2023.acl-long.61.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh
Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, et al. Mistral 7b. arXiv preprint arXiv:2310.06825, 2023.
Chen Jing and Ma Anni. “blossoms” sparks a ”dialect craze”—can you speak in dialect?,
2024.
URL https://news.cctv.com/2024/01/19/ARTIvo9LySHaxW7tpLn3T7Jl240119.
shtml. Last Accessed:2025-03-26.
Allison Koenecke, Andrew Nam, Emily Lake, Joe Nudell, Minnie Quartey, Zion Mengesha,
Connor Toups, John R. Rickford, Dan Jurafsky, and Sharad Goel. Racial disparities in
automated speech recognition. Proceedings of the National Academy of Sciences, 117(14):
7684–7689, 2020. doi: 10.1073/pnas.1915768117. URL https://www.pnas.org/doi/abs/
10.1073/pnas.1915768117.
Sangmin-Michelle Lee. The impact of using machine translation on efl students’ writing.
Computer Assisted Language Learning, 33(3):157–175, 2020. doi: 10.1080/09588221.2018.
1553186. URL https://doi.org/10.1080/09588221.2018.1553186.
Qiang Li, Qianyu Mai, Mandou Wang, and Mingjuan Ma. Chinese dialect speech recognition:
a comprehensive survey. Artificial Intelligence Review, 57(2):25, 2024.
Thomas Mullaney. Coming to terms with the nation: Ethnic classification in modern China,
volume 18. Univ of California Press, 2011.
Wilhelmina Nekoto, Vukosi Marivate, Tshinondiwa Matsila, Timi Fasubaa, Taiwo
Fagbohungbe, Solomon Oluwole Akinola, Shamsuddeen Muhammad, Salomon
Kabongo Kabenamualu, Salomey Osei, Freshia Sackey, Rubungo Andre Niyongabo,
Ricky Macharm, Perez Ogayo, Orevaoghene Ahia, Musie Meressa Berhe, Mofetoluwa
Adeyemi, Masabata Mokgesi-Selinga, Lawrence Okegbemi, Laura Martinus, Kolawole
Tajudeen, Kevin Degila, Kelechi Ogueji, Kathleen Siminyu, Julia Kreutzer, Jason Webster,
Jamiil Toure Ali, Jade Abbott, Iroro Orife, Ignatius Ezeani, Idris Abdulkadir Dangana,
Herman Kamper, Hady Elsahar, Goodness Duru, Ghollah Kioko, Murhabazi Espoir,
12

--- Page 13 ---

Preprint. Under review.
Elan van Biljon, Daniel Whitenack, Christopher Onyefuluchi, Chris Chinenye Emezue,
Bonaventure F. P. Dossou, Blessing Sibanda, Blessing Bassey, Ayodele Olabiyi, Arshath
Ramkilowan, Alp ¨Oktem, Adewale Akinfaderin, and Abdallah Bashir. Participatory
research for low-resourced machine translation: A case study in African languages.
In Trevor Cohn, Yulan He, and Yang Liu (eds.), Findings of the Association for Com-
putational Linguistics: EMNLP 2020, pp. 2144–2160, Online, November 2020. Associa-
tion for Computational Linguistics. doi: 10.18653/v1/2020.findings-emnlp.195. URL
https://aclanthology.org/2020.findings-emnlp.195/.
NLLB Team, Marta R. Costa-juss`a, James Cross, Onur C¸ elebi, Maha Elbayad, Kenneth
Heafield, Kevin Heffernan, Elahe Kalbassi, Janice Lam, Daniel Licht, Jean Maillard,
Anna Sun, Skyler Wang, Guillaume Wenzek, Al Youngblood, Bapi Akula, Loic Bar-
rault, Gabriel Mejia Gonzalez, Prangthip Hansanti, John Hoffman, Semarley Jarrett,
Kaushik Ram Sadagopan, Dirk Rowe, Shannon Spruit, Chau Tran, Pierre Andrews,
Necip Fazil Ayan, Shruti Bhosale, Sergey Edunov, Angela Fan, Cynthia Gao, Vedanuj
Goswami, Francisco Guzm´an, Philipp Koehn, Alexandre Mourachko, Christophe Rop-
ers, Safiyyah Saleem, Holger Schwenk, and Jeff Wang. Scaling neural machine trans-
lation to 200 languages.
Nature, 630(8018):841–846, 2024.
ISSN 1476-4687.
doi:
10.1038/s41586-024-07335-x. URL https://doi.org/10.1038/s41586-024-07335-x.
Team OLMo, Pete Walsh, Luca Soldaini, Dirk Groeneveld, Kyle Lo, Shane Arora, Akshita
Bhagia, Yuling Gu, Shengyi Huang, Matt Jordan, et al. 2 olmo 2 furious. arXiv preprint
arXiv:2501.00656, 2024.
Will Orr and Edward B. Kang.
Ai as a sport: On the competitive epistemologies of
benchmarking. In Proceedings of the 2024 ACM Conference on Fairness, Accountability,
and Transparency, FAccT ’24, pp. 1875–1884, New York, NY, USA, 2024. Association for
Computing Machinery.
ISBN 9798400704505.
doi: 10.1145/3630106.3659012.
URL
https://doi.org/10.1145/3630106.3659012.
Aleksandar Petrov, Emanuele La Malfa, Philip Torr, and Adel Bibi. Language model tok-
enizers introduce unfairness between languages. Advances in neural information processing
systems, 36:36963–36990, 2023.
Krithika Ramesh, Sunayana Sitaram, and Monojit Choudhury. Fairness in language models
beyond English: Gaps and challenges. In Andreas Vlachos and Isabelle Augenstein
(eds.), Findings of the Association for Computational Linguistics: EACL 2023, pp. 2106–2119,
Dubrovnik, Croatia, May 2023. Association for Computational Linguistics. doi: 10.18653/
v1/2023.findings-eacl.157. URL https://aclanthology.org/2023.findings-eacl.157/.
Phillip Rust, Jonas Pfeiffer, Ivan Vuli´c, Sebastian Ruder, and Iryna Gurevych. How good is
your tokenizer? on the monolingual performance of multilingual language models. In
Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli (eds.), Proceedings of the 59th
Annual Meeting of the Association for Computational Linguistics and the 11th International Joint
Conference on Natural Language Processing (Volume 1: Long Papers), pp. 3118–3135, Online,
August 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.acl-long.
243. URL https://aclanthology.org/2021.acl-long.243/.
Selma ˇSabanovi´c. Robots in society, society in robots: Mutual shaping of society and
technology as a framework for social robot design. International Journal of Social Robotics, 2
(4):439–450, 2010.
Alexander Tsvetkov and Alon Kipnis. Information parity: Measuring and predicting the
multilingual capabilities of language models. In Yaser Al-Onaizan, Mohit Bansal, and Yun-
Nung Chen (eds.), Findings of the Association for Computational Linguistics: EMNLP 2024,
pp. 7971–7989, Miami, Florida, USA, November 2024. Association for Computational
Linguistics. doi: 10.18653/v1/2024.findings-emnlp.468. URL https://aclanthology.
org/2024.findings-emnlp.468/.
Yequan Wang, Jiawen Deng, Aixin Sun, and Xuying Meng. Perplexity from plm is unreliable
for evaluating text quality. arXiv preprint arXiv:2210.05892, 2022.
13

--- Page 14 ---

Preprint. Under review.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony
Moi, Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer,
Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao,
Sylvain Gugger, Mariama Drame, Quentin Lhoest, and Alexander Rush. Transformers:
State-of-the-art natural language processing. In Qun Liu and David Schlangen (eds.),
Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing:
System Demonstrations, pp. 38–45, Online, October 2020. Association for Computational
Linguistics. doi: 10.18653/v1/2020.emnlp-demos.6. URL https://aclanthology.org/
2020.emnlp-demos.6.
BigScience Workshop, Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana
Ili´c, Daniel Hesslow, Roman Castagn´e, Alexandra Sasha Luccioni, Franc¸ois Yvon, et al.
Bloom: A 176b-parameter open-access multilingual language model. arXiv preprint
arXiv:2211.05100, 2022.
Aiyuan Yang, Bin Xiao, Bingning Wang, Borong Zhang, Ce Bian, Chao Yin, Chenxu Lv,
Da Pan, Dian Wang, Dong Yan, et al. Baichuan 2: Open large-scale language models.
arXiv preprint arXiv:2309.10305, 2023.
An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li,
Dayiheng Liu, Fei Huang, Haoran Wei, et al. Qwen2. 5 technical report. arXiv preprint
arXiv:2412.15115, 2024.
Zeyi Yang. Here’s how deepseek censorship actually works—and how to get around it,
2024. URL https://www.wired.com/story/deepseek-censorship/. Accessed: 2025-03-27.
Rui-Jie Yew, Lucy Qin, and Suresh Venkatasubramanian. You still see me: How data
protection supports the architecture of ai surveillance. In Proceedings of the 2024 AAAI/ACM
Conference on AI, Ethics, and Society, AIES ’24, pp. 1709–1722. AAAI Press, 2025.
Alex Young, Bei Chen, Chao Li, Chengen Huang, Ge Zhang, Guanwei Zhang, Heng Li,
Jiangcheng Zhu, Jianqun Chen, Jing Chang, Kaidong Yu, Peng Liu, Qiang Liu, Shawn
Yue, Senbin Yang, Shiming Yang, Tao Yu, Wen Xie, Wenhao Huang, Xiaohui Hu, Xiaoyi
Ren, Xinyao Niu, Pengcheng Nie, Yuchi Xu, Yudong Liu, Yue Wang, Yuxuan Cai, Zhenyu
Gu, Zhiyuan Liu, and Zonghong Dai. Yi: Open foundation models by 01.ai, 2024.
Chen Zhang, Mingxu Tao, Quzhe Huang, Jiuheng Lin, Zhibin Chen, and Yansong Feng.
MC2: Towards transparent and culturally-aware NLP for minority languages in China. In
Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), Proceedings of the 62nd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 8832–
8850, Bangkok, Thailand, August 2024a. Association for Computational Linguistics. doi:
10.18653/v1/2024.acl-long.479. URL https://aclanthology.org/2024.acl-long.479/.
Jinyi Zhang, Ke Su, Haowei Li, Jiannan Mao, Ye Tian, Feng Wen, Chong Guo, and Tadahiro
Matsumoto. Neural machine translation for low-resource languages from a chinese-
centric perspective: A survey. 23(6), June 2024b. ISSN 2375-4699. doi: 10.1145/3665244.
URL https://doi.org/10.1145/3665244.
Appendix
A
Limitations
There are several limitations in our experiments that could bias our observations regarding
China’s LLMs. First, the models we evaluate on are open-source, with 7–9 billion parameters,
and released on Hugging Face, a western platform. We note that China has their own
Hugging Face equivalent, such as ModelScope and OpenCSG.1213 It is possible that models
12https://www.modelscope.cn/
13https://opencsg.com/
14

--- Page 15 ---

Preprint. Under review.
20
10
0
10
20
Change in MRC accuracy (%) by using chat template
Baichuan2-Chat
DeepSeek-R1-Llama
DeepSeek-R1-Qwen
Llama3-Instruct
Mistral-Instruct
Olmo2-Instruct
Qwen2.5-Instruct
Yi-1.5-Chat
Gemma2-Instruct
InternLM3-Instruct
Model
20
10
0
10
20
MRC accuracy change by using chat template
Jingpho
Lhasa Tibetan
English
French
German
Italian
Spanish
Mandarin (Simplified)
Mandarin (Traditional)
Japanese
Korean
Burmese
Indonesian
Lao
Standard Malay
Thai
Vietnamese
Language
Figure 7: Change in MRC accuracy by using chat template. Overall, using chat template
and system prompt does not significant influence model performance on MRC, with the
exception for DeepSeek models. We observe that custom chat templates better activate the
“<think>” pattern in DeepSeek models.
released on these platforms may be different from the ones on Hugging Face. However,
at the time of writing, we find that the popular models on these platforms are also on
Hugging Face. We also note that there are other closed-source LLMs developed and widely
used in mainland China (e.g. Baidu’s ERNIE bot) that may have different performance
outputs. However, closed-source models do not give us the level of liberal access we needed
for our experiments. Second, while we evaluate Chinese and other Asian languages, our
experiments only feature benchmarks that have been translated from English. This may
introduce biases by way of cultural representation. However, we note a general lack of
parallel dataset that is translated from Mandarin. Third, the benchmarks we use are open-
source and well-known, possibly exposing them for developers to train or finetune their
models on. Fourth, due to data availability, we do not include most of the Chinese Han
dialects. In addition to minority languages, China also has significant populations speaking
8–10 different Chinese Han dialects, such as Cantonese, Hokkien, or Shanghainese, in their
day-to-day lives. The difficulty in evaluating Han dialects is that, except for Cantonese
in Hong Kong, these dialects often do not have standardized writing forms. We also
note the relative few number of minority languages we evalutae in this study. In general,
data collection efforts are required to evaluate performance on more dialects and minority
languages.
B
Negative Log Likelihood
The sum of negative log likelihood of a given text (t1, t2, ..., tn), where ti is the ith token of
the text, under a language model M, is defined as followed
NLL(text) = NLL(t1, t2, ..., tn) =
n
∑
i=1
−log PM(wi|w1:i−1)
(2)
where PM is the probability assigned by model M.
C
Sample English sentences from FLORES+ dataset
On Monday, scientists from the Stanford University School of Medicine announced
the invention of a new diagnostic tool that can sort cells by type: a tiny printable
chip that can be manufactured using standard inkjet printers for possibly about
one U.S. cent each.
“Panama Papers” is an umbrella term for roughly ten million documents from
Panamanian law firm Mossack Fonseca, leaked to the press in spring 2016.
15

--- Page 16 ---

Preprint. Under review.
Model
Vocabulary
Size
Pretrained
Data Size
(trillion
tokens)
Pretrained Data Source
Pretrained Data
Languages
Qwen2.5
151,643
18
“Our dataset is designed
to meet these
requirements and
includes public web
documents, encyclopedia,
books, codes, etc.
Additionally, our dataset
is multilingual, with a
significant portion of the
data being in English and
Chinese.” (Qwen2)
Multilingual data,
with a significant
portion in English
and Chinese.
(Qwen2)
Yi-1.5
64,000
3.1
Common Crawl 15 (80%),
encyclopedia, books,
papers, codes. (Yi)
English and
Chinese (Yi)
DeepSeek-R1
129,280
14.8
(DeepSeek-
V3)
Unclear
“multilingual
coverage beyond
English and
Chinese”
(DeepSeek-V3)
InternLM3
around
92,000 (In-
ternLM2)
4
“The text data in our
pre-training dataset can
be categorized by source
into web pages, papers,
patents, and books. [...]
Our web page data
mainly comes from
Common Crawl.”
(InternLM2)
“The Chinese and
English data from
web pages account
for 86.46% of the
total, making it the
primary source. ”
(InternLM2)
Baichuan2
125,696
2.6
Web pages, books,
research papers,
codebases, etc.
Unclear
Table 2: Training data details according to technical reports and model cards of the models.
Many models are updates of earlier pretrained models and lack clear details on pretraining
data. In such cases, we refer to the technical reports and model cards of the earlier models.
Notably, DeepSeek models have been very extremely terse about their pretraining data recipe
for both the R1 and V3.
D
Prompt used in Machine Reading Comprehension (Experiment 2)
Below is the prompt format we use for experiment 2 with a question from the Belebele
dataset. We construct the prompts following the original paper (Bandarkar et al., 2023):
Given the
following passage ,
query ,
and answer choices ,
output the
l e t t e r
corresponding
to
the
correct
answer .
###
Passage :
With the change from the
quarter
to
the
half
mile run ,
speed
becomes of much l e s s
importance and endurance becomes an
absolute
necessity .
Of course a
f i r s t −c l a s s
half −miler ,
a man
who can beat two minutes ,
must be possessed
of a
f a i r amount
16

--- Page 17 ---

Preprint. Under review.
Chinese Minorities
Southeast Asian
Northeast Asian
European
Chinese Han Dialects (Other)
Mandarin Chinese
0.2
0.4
0.6
0.8
Mandarin (Traditional)
Mandarin (Simplified)
Yue (Cantonese)
Italian
Spanish
German
French
Korean
Japanese
Lao
Burmese
Thai
Standard Malay
Vietnamese
Indonesian
Jingpho
Lhasa Tibetan
Uyghur
Mean IP Across Sentences
Languages
Models
Qwen2.5−Instruct
Yi−1.5−Chat
DeepSeek−R1−Llama
DeepSeek−R1−Qwen
InternLM3−Instruct
Baichuan2−Chat
Llama3−Instruct
Mistral−Instruct
Olmo2−Instruct
Gemma2−Instruct
(a) Instruction-tuned models
Chinese Minorities
Southeast Asian
Northeast Asian
European
Chinese Han Dialects (Other)
Mandarin Chinese
0.2
0.4
0.6
0.8
Mandarin (Traditional)
Mandarin (Simplified)
Yue (Cantonese)
Italian
Spanish
German
French
Korean
Japanese
Burmese
Lao
Thai
Standard Malay
Vietnamese
Indonesian
Jingpho
Lhasa Tibetan
Uyghur
Mean IP Across Sentences
Languages
Models
Qwen2.5
Yi−1.5
InternLM2.5
Baichuan2
Llama3
Mistral
Olmo2
Gemma2
(b) Base models
Figure 8: Experiment 1 full language and models breakdown.
of speed ,
but endurance must be cultivated
at
a l l
hazards .
Some cross
country running during the winter ,
combined with
gymnasium work for
the upper part
of
the body ,
i s
the
best
preparation
for
the running season .
###
Query :
According to
the passage ,
which of
the
following would be the most
b e n e f i c i a l
for a runner preparing
for
the upcoming season ?
###
Choices :
(A)
Practicing
cross
country running in
the summer
(B)
Focusing on c u l t i v a t i n g
speed while
training
(C)
Beating a three minute time
(D)
Utilizing
the gym to work out the upper body
###
Answer :
E
Prompt used in Minority Language Identification (Experiment 3)
Identify
the language of
the given
t ex t .
Output the
English name
of
the language .
Be concise .
Example :
Text : 地元メディアの報道によると、空港の消防車が中にしたということです。
Language :
Japanese
Text : ᄀ
ᅳᄌ
ᅩᄌ
ᅩ
ᆼᄉ
ᅡᄂ
ᅳ
ᆫᄇ
ᅵᄒ
ᅢ
ᆼᄌ
ᅮ
ᆼᄃ
ᅢᄌ
ᅡ
ᆼᄃ
ᅵ
ᆯᄅ
ᅩᄏ
ᅳᄅ
ᅵᄐ
ᅳᄑ
ᅢᄐ
ᅡᄇ
ᅵᄅ
ᅩᄒ
ᅪ
ᆨᄋ
ᅵ
ᆫᄃ
ᅬᄋ
ᅥ
ᆻᄃ
ᅡ.
Language :
Korean
Text : <input
text >
Language :
17

--- Page 18 ---

Preprint. Under review.
5
0
5
10
15
20
25
30
35
Change in mean IP with instruction-tuning
Qwen2.5
Yi-1.5
InternLM2.5
Baichuan2
Llama3
Mistral
OLMo2
Gemma2
Base Model
Model Source
China
Western
0.100
0.075
0.050
0.025
0.000
0.025
0.050
Change in mean IP with instruction-tuned vs. base models
Mandarin (Simplified)
Mandarin (Traditional)
French
German
Spanish
Italian
Japanese
Korean
Indonesian
Vietnamese
Standard Malay
Thai
Lao
Burmese
Lhasa Tibetan
Jingpho
Language
Model Source
China
Western
Figure 9: Change in average IP with instruction-tuned vs. base models
Chinese Minorities
Southeast Asian
Northeast Asian
European
Mandarin Chinese
20
40
60
80
Mandarin (Traditional)
Mandarin (Simplified)
Italian
Spanish
German
French
English
Japanese
Korean
Lao
Burmese
Thai
Standard Malay
Vietnamese
Indonesian
Lhasa Tibetan
Jingpho
MRC Accuracy (%)
Languages
Models
Qwen2.5−Instruct
Yi−1.5−Chat
DeepSeek−R1−Llama
DeepSeek−R1−Qwen
InternLM3−Instruct
Baichuan2−Chat
Llama3−Instruct
Mistral−Instruct
Olmo2−Instruct
Gemma2−Instruct
(a) Instruction-tuned models
Chinese Minorities
Southeast Asian
Northeast Asian
European
Mandarin Chinese
20
40
60
80
Mandarin (Traditional)
Mandarin (Simplified)
German
Italian
Spanish
French
English
Japanese
Korean
Lao
Burmese
Thai
Vietnamese
Standard Malay
Indonesian
Lhasa Tibetan
Jingpho
MRC Accuracy (%)
Languages
Models
Qwen2.5
Yi−1.5
InternLM2.5
Baichuan2
Llama3
Mistral
Olmo2
Gemma2
(b) Base models
Figure 10: MRC Accuracy of instruction-tuned models (a) and base models (b) on 17
languages. The ranking of model performance are largely consistent across languages,
except for Burmese, Lao, Jingpho, and Tibetan. Gemma2, IntermLM2.5 and Qwen2.5 top the
charts among both instruction-tuned and base models. Gemma2 significantly outperforms
other models in Burmese and Lao. Models perform similarly poor, around random baseline
of 0.25, in Chinese minorities languages.
18

--- Page 19 ---

Preprint. Under review.
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Average IP of Western base models
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Average IP of Chinese base models
Mandarin (Simplified)
Mandarin (Traditional)
Yue (Cantonese)
Correlation (r = 0.929, p value = 0.000)
Language Category
Southeast Asian
European
Northeast Asian
Chinese Minorities
Mandarin Chinese
Chinese Han Dialects (Other)
(a) IP
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Average MRC accuracy of Western base models
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Average MRC accuracy of Chinese base models
Mandarin (Simplified)
Mandarin (Traditional)
Correlation (r = 0.981, p value = 0.000)
Language Category
Southeast Asian
European
Northeast Asian
Chinese Minorities
Mandarin Chinese
(b) MRC Accuracy
Figure 11: Correlation of IP and MRC accuracy between Chinese and Western base models
Kazakh
Mongolian
Tibetan
Uyghur
0
25
50
75
100
Language Identification Accuracy (%)
Languages
Models
Qwen2.5
Yi−1.5
InternLM2.5
Baichuan2
Llama3
Mistral
Olmo2
Gemma2
Figure 12: Language identification accuracy of base models on MC2 data.
19

```
