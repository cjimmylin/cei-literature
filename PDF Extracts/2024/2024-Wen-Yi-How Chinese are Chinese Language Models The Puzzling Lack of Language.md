---
title: "2024-Wen-Yi-How Chinese are Chinese Language Models The Puzzling Lack of Language - PDF Extract"
source_pdf: "2024-Wen-Yi-How Chinese are Chinese Language Models The Puzzling Lack of Language.pdf"
pages: 10
extracted_at: "2026-03-13T18:35:05.821681"
extractor: PyMuPDF
---

# PDF Extract: 2024-Wen-Yi-How Chinese are Chinese Language Models The Puzzling Lack of Language

**Source PDF:** 2024-Wen-Yi-How Chinese are Chinese Language Models The Puzzling Lack of Language.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

How Chinese are Chinese Language Models? The Puzzling Lack of
Language Policy in China’s LLMs
Andrea W Wen-Yi 1∗
Unso Eun Seo Jo1∗
Lu Jia Lin2
David Mimno1
1 Cornell University
2 Seoul National University
{andreawwenyi@infosci.,unsojo,mimno}@cornell.edu
leuadd0@gmail.com
Abstract
Contemporary language models are increas-
ingly multilingual, but Chinese LLM develop-
ers must navigate complex political and busi-
ness considerations of language diversity. Lan-
guage policy in China aims at influencing the
public discourse and governing a multi-ethnic
society, and has gradually transitioned from
a pluralist to a more assimilationist approach
since 1949. We explore the impact of these
influences on current language technology. We
evaluate six open-source multilingual LLMs
pre-trained by Chinese companies on 18 lan-
guages, spanning a wide range of Chinese,
Asian, and Anglo-European languages. Our ex-
periments show Chinese LLMs performance on
diverse languages is indistinguishable from in-
ternational LLMs. Similarly, the models’ tech-
nical reports also show lack of consideration
for pretraining data language coverage except
for English and Mandarin Chinese. Examin-
ing Chinese AI policy, model experiments, and
technical reports, we find no sign of any con-
sistent policy, either for or against, language
diversity in China’s LLM development. This
leaves a puzzling fact that while China regu-
lates both the languages people use daily as
well as language model development, they do
not seem to have any policy on the languages
in language models.
1
Introduction
For thousands of years, central governments in
China have used language as a tool to manage a
vast multiethnic population that speaks 129 lan-
guages and dialects. Over time, these policies have
changed in level of inclusivity. In 2017, China
announced the ‘New Generation AI Development
Plan,’ a plan to lead China to become a ‘major AI
innovation center’ by 2030. In this ‘New Genera-
tion’ AI era, what is China’s AI language policy
and how does it relate to minority languages?
To answer this question we look at nationally
developed pretrained LLMs. We explore six open-
∗Both authors contributed equally to this work.
source multilingual language models developed
by Chinese companies that have majority Chinese
local ownership (see Table 2). We evaluate their
performance across Mandarin, Northeast Asian lan-
guages (Japanese and Korean), Southeast Asian
languages (Indonesian, Lao, Burmese, Thai, Viet-
namese, Standard Malay), and Chinese ethnic mi-
nority languages (Lhasa Tibetan, Jingpho, Kazakh,
Northern Uzbek) and compare their performance
with European languages (e.g. English, French,
Italian, Spanish, German). We also examine their
technical reports to evaluate their data collection.
Both nationally-developed open-source Chinese
LLMs and well-known international models show
similar performance across dialects and select re-
gional and national languages. They show all of
the same performance caveats on low-resource Chi-
nese dialects, and their technical reports on data
collection also indicate no clear extra effort into
improving dialect performance.
The PRC has shown intention to regulate lan-
guage AI but has not announced requirements
about minority language performance in LLMs.
Their major policy guidelines and requirements
about generative AI have no specific mention of
minority languages despite stated measures about
discrimination and socially influential content. In
2024, we find no evidence of PRC priorities for
minority languages — either for or against — in
open-source LLMs.
Related Work
LLMs have grown increasingly
multilingual over the last few years (Conneau et al.,
2020; Brown et al., 2020; Workshop et al., 2022),
with significant efforts put into promoting the repre-
sentation of low-resource languages (Abadji et al.,
2022; ImaniGooghari et al., 2023). Studies have
shown that linguistic diversity in language technol-
ogy promote access to information (Lee, 2020) and
preservation of low-resource languages (Bird and
Chiang, 2012).
arXiv:2407.09652v1  [cs.CL]  12 Jul 2024

--- Page 2 ---

2
Historical background on China’s
language and AI policy
Language Policy
Language policy has been an
essential political tool for rulers in China to govern
multiple ethnicities and cultures. These policies
vacillated from being pluralist to assimilationist
over the eras. In 221 B.C., after unifying the war-
ring states, the Qin Emperor launched the first of-
ficial program to standardize the Chinese script
to consolidate central state power. Following the
1949 Chinese Communist Revolution, the Chinese
Communist Party (CCP) continued this tradition by
launching extensive linguistic campaigns to unify
the minority population of over 106 million people
who spoke 129 languages among them (Mullaney,
2011). Gradually this transitioned to a more mono-
lingual, assimilationist policy (one nation, one lan-
guage). In 1982, constitutional amendment Article
19 made Mandarin Chinese the official common
spoken “super language” for all indigenous and eth-
nic people. In 2000, the PRC promulgated the Stan-
dard Spoken and Written Chinese Language law to
promote standard spoken and written Mandarin in
public including schools, publications, broadcasts,
and product packaging. While Mandarin Chinese
remains the standard in the public sphere, non-
Mandarin languages exist in common usage but
are not recognized as standard, official languages.
AI Policy
The PRC government has also been
taking steps to regulate generative AI. In July 2023
the Cyberspace Administration of China issued
the Administration of Generative AI Services (the
“Interim AI Measures”), which requires that gen-
erative AI services with “public opinion attributes”
or “social mobilization capabilities” must undergo
rigorous security assessments and file detailed algo-
rithm records with authorities. The Interim AI Mea-
sures require that AI-generated content complies
with five principles such as upholding socialist val-
ues, preventing discriminatory content, and imple-
menting transparency and reliability measures. As
of March 2024, 117 generative AI services had
completed the mandatory government filing pro-
cess to comply with these requires. The Interim
AI Measures define requisites for pretraining AI
models in particular. When training AI models,
providers must use lawfully sourced data and foun-
dational models and avoid infringing on intellectual
property rights. They must also employ measures
to enhance training data quality, truthfulness, accu-
racy, objectivity, and diversity and comply with na-
tional laws 1. While these requirements are vague
and could include minority languages, there is no
explicit mention of them.
3
Model Experiments
Models
Language models vary considerably in
both size and capability. In order to provide the
most fair comparison among models, we restrict
experiments to models roughly at the 8-billion pa-
rameter scale. This scale is sufficient for at-or-near
state of the art performance while limiting computa-
tional complexity. We access these models through
the transformers (Wolf et al., 2020) library.2
We experiment on six open-source multilin-
gual LLMs pretrained from scratch by Chi-
nese entities:
Qwen1.5-7B (Bai et al., 2023),
Yi-6B (Young et al., 2024), DeepSeek-LLM-7B
(DeepSeek-AI, 2024), InternLM2-7B (Cai et al.,
2024), XVERSE-7B (XVERSE Technology, 2023),
and Baichuan2-7B-Base (Yang et al., 2023). We
also evaluate Llama3-8B (AI@Meta, 2024) and
Mistral-7B-v0.3 (Jiang et al., 2023), open LLMs
developed by U.S. and French companies.
Technical Reports
We also examine the mod-
els’ technical reports to investigate the pretrain-
ing data that shaped these LLMs. We find that
Chinese AI companies’ focus on language mod-
els places a heavy emphasis on Mandarin and En-
glish but not on other languages. While the reports
for Qwen, XVERSE and InternLM2 mention multi-
lingual coverage, they do not explicate what lan-
guages they cover except English and Mandarin
(See Table 3 in appendix for further details). Ad-
ditionally, similar to the training of international
models, sources of pretrained data rely heavily on
web pages, with three reports specifically mention-
ing Common Crawl as their primary data source.
Languages and Tasks
We conduct two exper-
iments, measuring different aspects of language
model capabilities on two datasets: the FLORES+
and Belebele benchmarks. Both datasets are devel-
oped based on the FLORES evaluation benchmark
for machine translation (Goyal et al., 2022). We
evaluate 18 languages included in both datasets,
spanning languages spoken in China, Northeast
Asia, Southeast Asia, US/Europe, and by ethnic mi-
1Chinese national Cybersecurity Law, Data Security Law,
and Personal Information Protection
2We will release code.

--- Page 3 ---

Chinese Ethnic Minorities
Southeast Asian
Northeast Asian
US/European
Mandarin Chinese
100
200
300
Mandarin (Traditional)
Mandarin (Simplified)
Spanish
Italian
German
French
English
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
Northern Uzbek
Kazakh
Mean NLL Across Sentences
Languages
Models
Qwen1.5
Yi
DeepSeek
InternLM2
Baichuan2
XVERSE
Llama3
Mistral
Figure 1: NLL averaged across 997 sentences in each
language from Experiment 1. The x-axis is reversed
such that lower, and better, score is on the right. The
y-axis lists languages, ordered within each language
category by the average score across models.
norities in China. For Mandarin Chinese, we test
two writing system variants — Simplified Chinese
characters, used in the PRC, and Traditional Chi-
nese characters, used in Taiwan. We were not able
to evaluate Chinese Han dialects such as Cantonese
or Shanghainese because the benchmarks did not
include them. For the full list of languages, see
Table 1 in appendix.
Experiment 1: Evaluating language model per-
plexity with the FLORES+ dataset
The mod-
els we evaluate are trained on a next-token predic-
tion task. Our first experiment evaluates how well
these language models predict the next token in
sentences from the FLORES+ multilingual dataset.3
997 English sentences 4 are sampled from Wiki
sources then translated into target languages by na-
tive speakers. There are 997 parallel sentences in
all languages we evaluate. See example English
sentences in Appendix A.
Modern language model tokenizers employ data-
driven approaches like byte-pair encoding (BPE) to
break words into sub-word units, often leading to
varying segmentation rates across languages (Rust
et al., 2021; Ali et al., 2023). We also observe such
3https://github.com/openlanguagedata/flores
4we use the dev split of FLORES+.
Chinese Ethnic Minorities
Southeast Asian
Northeast Asian
US/European
Mandarin Chinese
0.25
0.50
0.75
Mandarin (Traditional)
Mandarin (Simplified)
Italian
German
Spanish
French
English
Korean
Japanese
Lao
Burmese
Thai
Vietnamese
Standard Malay
Indonesian
Lhasa Tibetan
Jingpho
Kazakh
Northern Uzbek
Accuracy
Languages
Models
Qwen1.5
Yi
DeepSeek
InternLM2
Baichuan2
XVERSE
Llama3
Mistral
Figure 2: Accuracy of zero-shot MRC from Experiment
2. The y-axis lists languages, ordered within each lan-
guage category by the average score across models. The
dashed vertical line represents the random baseline.
discrepancy in segmentation rate with the language
models we evaluate, see Appendix Figure 4.
Perplexity (PPL) is a common measure to eval-
uate the probability given to a sentence (Gonen
et al., 2023; Xiao et al., 2023). However, perplex-
ity, as a per-token measure, is not directly compa-
rable across languages tokenized at varying rates
(Mielke, 2019). To account for the confounding
influence of tokenization efficiency, we report un-
normalized negative log likelihood, equivalent to
the sum of negative log-likelihood given to each
token in a sentence:
NLL = −loge(PPL) × ntokens
where ntokens refers to the total number of tokens
in the sentence. Lower scores are better as they
represent higher probability.
From Figure 1, we find that NLL is lowest for
Mandarin and US/European languages, followed
by Northeast Asian languages, Southeast Asian
Languages, and with Chinese Ethnic Minorities
languages having the worst. Language models
show similar results among the top-performing
languages, but the performance varies in lower-
resource languages including Lao, Burmese, and
Chinese minority languages. We find no clear dis-
tinctions between Chinese and international models

--- Page 4 ---

across languages, with only slightly better perfor-
mance in Mandarin from the Chinese models.
Experiment 2: Evaluating Zero-shot Reading
Comprehension using Belebele dataset
Per-
plexity is an intrinsic measure of how well a lan-
guage model performs on the task they are trained
to do. But it does not necessarily predict how well
a model does in tasks that require text compre-
hension (Holtzman et al., 2021; Wiegreffe et al.,
2023). To account for this, in the second exper-
iment we evaluate the language models’ perfor-
mance on multiple-choice reading comprehension
(MRC) using the Belebele benchmark dataset (Ban-
darkar et al., 2023). The Belebele becnhmark is
a parallel reading comprehension dataset covering
122 languages. For each language, there are 900
multiple-choice questions. Each question is related
to a passage from the FLORES-200 dataset (NLLB
Team et al., 2022). Each question has four multiple
choice answers with one correct answer. The ques-
tions are fully parallel across 122 languages and
curated and verified by translators fluent in both
English and the target language. We query mod-
els with zero-shot prompts and calculate zero-shot
MRC accuracy of the models’ answers, higher is
better. See example question and prompt in the
appendix.
Figure 2 shows the result of the second experi-
ment. Overall, the performance trend across lan-
guages is similar to Experiment 1. While zero-shot
MRC accuracy is consistently lowest for Burmese,
Lao, and Chinese minority languages, it is more
varied for other languages, especially for higher-
resource ones. Additionally, InternLM2 consis-
tently outperforms other models in all languages,
and XVERSE consistently underperforms, some-
times even lower than a random baseline. Similar
to Experiment 1, there are no clear performance dif-
ferences between Chinese and international models
among the languages we test.
Population and Economy
We find that Chinese
national models show the same pattern of perfor-
mance across languages that international models
do. Both Chinese and international models, like
Llama3 and Mistral, perform best in Mandarin and
Western languages, then Japanese and Korean, and
worst in Chinese minority languages. To test if
the performance variance is a factor of data avail-
ability we use number of speakers and GDP as
proxies (Eberhard et al., 2024). We find that model
Lhasa Tibetan
Mandarin (Simplified)
German
English
French
Indonesian
Italian
Japanese
Jingpho
Kazakh
Korean
Lao
Burmese
Spanish
Thai
Northern Uzbek
Vietnamese
Standard Malay
Lhasa Tibetan
German
English
French
Indonesian
Italian
Japanese
Jingpho
Kazakh
Korean
Lao
Burmese
Spanish
Thai
Northern Uzbek
Vietnamese
Mandarin (Simplified)
Standard Malay
Lhasa Tibetan
Mandarin (Simplified)
German
English
French
Italian
Jingpho
Kazakh
Lao
Burmese
Spanish
Thai
Northern Uzbek
Vietnamese
Standard Malay
Lhasa Tibetan
German
English
French
Indonesian
Italian
Japanese
Jingpho
Kazakh
Korean
Lao
Burmese
Spanish
Thai
Northern Uzbek
Vietnamese
Mandarin (Simplified)
Standard Malay
Chinese Models
International Models
Unnormalized PPL
Zero−shot MC Accuracy
1e+06
1e+07
1e+08
1e+09
1e+06
1e+07
1e+08
1e+09
100
200
300
0.2
0.3
0.4
0.5
0.6
0.7
# of Language Speakers
Mean Metric Across Models
Figure 3: Chinese models’ performance on different
languages correlate positively with the number of speak-
ers. Each point represents the average score of language
models. The top y-axis is NLL (Experiment 1) and the
bottom y-axis is average zero-shot MRC accuracy (Ex-
periment 2).
performance on different languages highly corre-
lates with the number of speakers of the language
(Figure 3), and the trend is almost indistinguish-
able between Chinese and international models.
On average, the logarithm of number of language
speakers highly correlates with NLL, at −0.845
for Chinese LLMs and −0.883 for international
LLMs. Correlations with zero-shot MRC accuracy
are 0.837 for Chinese LLMs and 0.884 for inter-
national LLMs.5 We find the NLL and zero-shot
MRC accuracy performances of national languages
from Asian countries neighboring China (Japan,
Korea, Indonesia, Malaysia, Vietnam, Thai, Myan-
mar, Laos) also highly correlate with the logarithm
of national GDP (see Appendix Table 4 and Figure
5 for details).
4
Discussion and Conclusion
We evaluate the linguistic policy in China’s LLM
development through three venues: AI policy,
model experiments, as well as model technical re-
ports. The PRC has implemented a more assimila-
tionist language policy and shown clear intention to
regulate generative AI training but has no obvious
plans for either limiting or encouraging minority
languages in LLMs. Our experiments and review of
technical reports also verify the lack of consistent
and explicit policy related to language AI, whether
for or against linguistic diversity.
5The population for Standard Malay (zsm) is not provided
in Eberhard et al. (2024), so we use the population for Malay
(msa) instead.

--- Page 5 ---

Limitations
We identify three limitations in this work. First,
due to data availability, we do not evaluate Chi-
nese Han dialects. In addition to ethnic minority
languages, China also has significant populations
speaking 8–10 different Chinese Han dialects, such
as Cantonese, Hokkien, or Shanghainese, in their
day-to-day lives. The difficulty in evaluating Han
dialects is that, except for Cantonese in Hong Kong,
these dialects often do not have standardized writ-
ing forms. Additional data collection efforts are
required in order to evaluate performance on these
dialects. Second, we do not evaluate closed-source
LLMs in this study. It is possible that closed-source
LLMs’ development and capabilities differ from
open-source ones. However, closed-source models
do not give us the level of liberal access we needed
for our experiments. Finally, while we access all
models via HuggingFace, China has their own plat-
form for releasing and accessing AI models called
ModelScope6 (HuggingFace is blocked in China).
In our work, we do not evaluate models on Mod-
elScope but focus on the top-performing Chinese
LLMs on HuggingFace.
Acknowledgements
Left blank for anonymous submission
References
Julien Abadji, Pedro Ortiz Suarez, Laurent Romary, and
Benoît Sagot. 2022. Towards a cleaner document-
oriented multilingual crawled corpus. In Proceedings
of the Thirteenth Language Resources and Evalua-
tion Conference, pages 4344–4355, Marseille, France.
European Language Resources Association.
AI@Meta. 2024. Llama 3 model card.
Mehdi Ali, Michael Fromm, Klaudia Thellmann,
Richard Rutmann,
Max Lübbering,
Johannes
Leveling, Katrin Klug, Jan Ebert, Niclas Doll,
Jasper Schulze Buschhoff, et al. 2023. Tokenizer
choice for llm training: Negligible or crucial? arXiv
preprint arXiv:2310.08754.
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang,
Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin,
Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu,
Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren,
Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong
Tu, Peng Wang, Shijie Wang, Wei Wang, Sheng-
guang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang,
6https://github.com/modelscope/modelscope
Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu,
Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingx-
uan Zhang, Yichang Zhang, Zhenru Zhang, Chang
Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang
Zhu. 2023. Qwen technical report. arXiv preprint
arXiv:2309.16609.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel
Artetxe, Satya Narayan Shukla, Donald Husa, Naman
Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and
Madian Khabsa. 2023. The belebele benchmark: a
parallel reading comprehension dataset in 122 lan-
guage variants. arXiv preprint arXiv:2308.16884.
Steven Bird and David Chiang. 2012. Machine trans-
lation for language preservation. In Proceedings of
COLING 2012: Posters, pages 125–134, Mumbai,
India. The COLING 2012 Organizing Committee.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot
learners. Advances in neural information processing
systems, 33:1877–1901.
Zheng Cai, Maosong Cao, Haojiong Chen, Kai Chen,
Keyu Chen, Xin Chen, Xun Chen, Zehui Chen, Zhi
Chen, Pei Chu, et al. 2024. Internlm2 technical re-
port. arXiv preprint arXiv:2403.17297.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451, Online. Association for Computational Lin-
guistics.
DeepSeek-AI. 2024.
Deepseek llm: Scaling open-
source language models with longtermism. arXiv
preprint arXiv:2401.02954.
David M. Eberhard, Gary F. Simons, and Charles
D. Fennig (eds.). 2024. Ethnologue: Languages of
the world. twenty-seventh edition.
Hila Gonen, Srini Iyer, Terra Blevins, Noah Smith, and
Luke Zettlemoyer. 2023. Demystifying prompts in
language models via perplexity estimation. In Find-
ings of the Association for Computational Linguis-
tics: EMNLP 2023, pages 10136–10148, Singapore.
Association for Computational Linguistics.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary, Peng-
Jen Chen, Guillaume Wenzek, Da Ju, Sanjana Kr-
ishnan, Marc’Aurelio Ranzato, Francisco Guzmán,
and Angela Fan. 2022. The Flores-101 evaluation
benchmark for low-resource and multilingual ma-
chine translation. Transactions of the Association for
Computational Linguistics, 10:522–538.

--- Page 6 ---

Ari Holtzman, Peter West, Vered Shwartz, Yejin Choi,
and Luke Zettlemoyer. 2021.
Surface form com-
petition: Why the highest probability answer isn’t
always right. In Proceedings of the 2021 Conference
on Empirical Methods in Natural Language Process-
ing, pages 7038–7051, Online and Punta Cana, Do-
minican Republic. Association for Computational
Linguistics.
Ayyoob ImaniGooghari, Peiqin Lin, Amir Hossein Kar-
garan, Silvia Severini, Masoud Jalili Sabet, Nora
Kassner, Chunlan Ma, Helmut Schmid, André Mar-
tins, François Yvon, and Hinrich Schütze. 2023.
Glot500: Scaling multilingual corpora and language
models to 500 languages. In Proceedings of the 61st
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 1082–
1117, Toronto, Canada. Association for Computa-
tional Linguistics.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, et al. 2023. Mistral
7b. arXiv preprint arXiv:2310.06825.
Sangmin-Michelle Lee. 2020. The impact of using ma-
chine translation on efl students’ writing. Computer
Assisted Language Learning, 33(3):157–175.
Sabrina J. Mielke. 2019. Can you compare perplexity
across different segmentations?
Thomas Mullaney. 2011. Coming to terms with the
nation: Ethnic classification in modern China, vol-
ume 18. Univ of California Press.
NLLB Team, Marta R. Costa-jussà, James Cross, Onur
Çelebi, Maha Elbayad, Kenneth Heafield, Kevin Hef-
fernan, Elahe Kalbassi, Janice Lam, Daniel Licht,
Jean Maillard, Anna Sun, Skyler Wang, Guillaume
Wenzek, Al Youngblood, Bapi Akula, Loic Bar-
rault, Gabriel Mejia-Gonzalez, Prangthip Hansanti,
John Hoffman, Semarley Jarrett, Kaushik Ram
Sadagopan, Dirk Rowe, Shannon Spruit, Chau
Tran, Pierre Andrews, Necip Fazil Ayan, Shruti
Bhosale, Sergey Edunov, Angela Fan, Cynthia
Gao, Vedanuj Goswami, Francisco Guzmán, Philipp
Koehn, Alexandre Mourachko, Christophe Ropers,
Safiyyah Saleem, Holger Schwenk, and Jeff Wang.
2022.
No language left behind: Scaling human-
centered machine translation. arXiv:1902.01382.
Phillip Rust, Jonas Pfeiffer, Ivan Vuli´c, Sebastian Ruder,
and Iryna Gurevych. 2021. How good is your tok-
enizer? on the monolingual performance of multilin-
gual language models. In Proceedings of the 59th
Annual Meeting of the Association for Computational
Linguistics and the 11th International Joint Confer-
ence on Natural Language Processing (Volume 1:
Long Papers), pages 3118–3135, Online. Association
for Computational Linguistics.
Sarah Wiegreffe, Matthew Finlayson, Oyvind Tafjord,
Peter Clark, and Ashish Sabharwal. 2023. Increasing
probability mass on answer choices does not always
improve accuracy. In Proceedings of the 2023 Con-
ference on Empirical Methods in Natural Language
Processing, pages 8392–8417, Singapore. Associa-
tion for Computational Linguistics.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Remi Louf, Morgan Funtow-
icz, Joe Davison, Sam Shleifer, Patrick von Platen,
Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,
Teven Le Scao, Sylvain Gugger, Mariama Drame,
Quentin Lhoest, and Alexander Rush. 2020. Trans-
formers: State-of-the-art natural language processing.
In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 38–45, Online. Association
for Computational Linguistics.
BigScience Workshop, Teven Le Scao, Angela Fan,
Christopher Akiki, Ellie Pavlick, Suzana Ili´c, Daniel
Hesslow, Roman Castagné, Alexandra Sasha Luc-
cioni, François Yvon, et al. 2022. Bloom: A 176b-
parameter open-access multilingual language model.
arXiv preprint arXiv:2211.05100.
Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song
Han, and Mike Lewis. 2023. Efficient streaming
language models with attention sinks. arXiv.
XVERSE Technology. 2023. Xverse-7b model card.
Aiyuan Yang, Bin Xiao, Bingning Wang, Borong Zhang,
Ce Bian, Chao Yin, Chenxu Lv, Da Pan, Dian Wang,
Dong Yan, et al. 2023. Baichuan 2: Open large-scale
language models. arXiv preprint arXiv:2309.10305.
Alex Young, Bei Chen, Chao Li, Chengen Huang,
Ge Zhang, Guanwei Zhang, Heng Li, Jiangcheng
Zhu, Jianqun Chen, Jing Chang, Kaidong Yu, Peng
Liu, Qiang Liu, Shawn Yue, Senbin Yang, Shiming
Yang, Tao Yu, Wen Xie, Wenhao Huang, Xiaohui
Hu, Xiaoyi Ren, Xinyao Niu, Pengcheng Nie, Yuchi
Xu, Yudong Liu, Yue Wang, Yuxuan Cai, Zhenyu Gu,
Zhiyuan Liu, and Zonghong Dai. 2024. Yi: Open
foundation models by 01.ai.
A
Experiment 1: Sample sentences from
FLORES+ English dataset
On Monday, scientists from the Stan-
ford University School of Medicine an-
nounced the invention of a new diagnos-
tic tool that can sort cells by type: a tiny
printable chip that can be manufactured
using standard inkjet printers for possi-
bly about one U.S. cent each.
“Panama Papers” is an umbrella term
for roughly ten million documents from
Panamanian law firm Mossack Fonseca,
leaked to the press in spring 2016.

--- Page 7 ---

Language
FLORES+ Language Code
Cateogry
Mandarin (Simplified Characters)
cmn_Hans
Mandarin Chinese
Mandarin (Traditional Characters)
cmn_Hant
Mandarin Chinese
Korean
kor_Hang
Northeast Asian
Japanese
jpn_Jpan
Northeast Asian
Indonesian
ind_Latn
Southeast Asian
Lao
lao_Laoo
Southeast Asian
Burmese
mya_Mymr
Southeast Asian
Thai
tha_Thai
Southeast Asian
Vietnamese
vie_Latn
Southeast Asian
Standard Malay
zsm_Latn
Southeast Asian
Lhasa Tibetan
bod_Tibt
Chinese ethnic minorities
Jingpho
kac_Latn
Chinese ethnic minorities
Kazakh
kaz_Cyrl
Chinese ethnic minorities
Northern Uzbek
uzn_Latn
Chinese ethnic minorities
English
eng_Latn
US/European
French
fra_Latn
US/European
Italian
ita_Latn
US/European
Spanish
spa_Latn
US/European
German
deu_Latn
US/European
Table 1: Overview of selected languages and their respective categories. Languages categorized as “Chinese
ethnic minorities” indicate languages that are also spoken by some populations in China that the PRC determine as
“minority ethnic group”.
Model
Developer
Launch
Ownership
Founder
Investors
Qwen1.5
Alibaba Cloud
2023/04/07
Private
Alibaba Group
Alibaba Group
Yi
01-AI
2023/11/06
Private
Kai-Fu Lee, Chair-
man of Sinovation
Ventures
Undisclosed. Reported to include Al-
ibaba Cloud.
Deepseek
Deepseek AI
2023/11/29
Private
Eoghan Mulcahy,
Ciaran
O’Mara,
Niall Mulcahy
Hedge-Fund High-Flyer
InternLM2
Shanghai AI Labo-
ratory
2024/01/17
Private
Shanghai AI Labo-
ratory
Strategic Cooperation with main Uni-
versities in China.
XVERSE
XVERSE Technol-
ogy
2023/08/07
Private
former
Tencent
vice President, Yao
Xing
Tencent, GGV Capital, 5Y Capital,
Hillhouse Capital, Sequoia Capital,
Temasek, and CPE.
Baichuan2
Baichuan
Intelli-
gent Technology
2023/08/31
Private
former
Sogou
CEO,
Wang
Xi-
aochuan
Undisclosed.
Reported that major
Chinese tech companies including Al-
ibaba, Tencent, Xiaomi involved.
Table 2: Information about the developers of Chinese open-source multilingual language models.
Model
Tokenization
Vocabulary Size
Pretrained Data
Size (trillion to-
kens)
Pretrained Data Source
Pretrained Data Languages
Qwen1.5
tiktoken 7
around 152,000
3
Web pages, encyclope-
dia, books, codes, etc.
Multilingual data, with a signifi-
cant portion being in English and
Chinese.
Yi
SentencePiece
(BPE)
64,000
3.1
Common
Crawl
8
(80%),
encyclopedia,
books, papers, codes.
English and Chinese
Deepseek
tokenizers
(BBPE) 9
around 100,000
2
Common Crawl
English and Chinese
InternLM2
tiktoken
around 92,000
-
Common
Crawl,
papers, patents, and
books.
86.46% of data are Chinese and
English web pages
XVERSE
BPE
100,534
2.6
-
More than 40 languages includ-
ing Chinese, English, Russian, and
Spanish
Baichuan2
SentencePiece
(BPE)
125,696
2.6
Web pages, books, re-
search papers, code-
bases, etc.
-
Table 3: Technical details according to technical reports and model cards of the models. Information not reported is
shown as ‘-’.

--- Page 8 ---

B
Experiment 2 prompt
Below is the prompt format we use for experiment
2 with a question from the Belebele dataset. We
construct the prompts following the original paper
(Bandarkar et al., 2023):
Given the following passage ,
query , and answer choices ,
output the letter
corresponding to the correct
answer.
###
Passage:
With the change from the quarter
to the half mile run , speed
becomes of much less
importance and endurance
becomes an absolute necessity.
Of course a first -class half -
miler , a man who can beat two
minutes , must be possessed of
a fair amount of speed , but
endurance must be cultivated
at all hazards. Some cross
country running during the
winter , combined with
gymnasium work for the upper
part of the body , is the best
preparation for the running
season.
###
Query:
According to the passage , which
of the following would be the
most beneficial for a runner
preparing for the upcoming
season?
###
Choices:
(A) Practicing cross country
running in the summer
(B) Focusing on cultivating speed
while training
(C) Beating a three minute time
(D) Utilizing the gym to work out
the upper body
###
Answer:
C
Model and Dataset Information
C.1
Licensing
Both FLORES+ and Belebele dataset are li-
censed under CC-BY-SA-4.0.
The pretrained
models Yi-6B, XVERSE-7B, InternLM2-7B, and
Mistral-7B-v0.3
are
under
Apache-2.0
li-
cense. Baichuan2-7B-Base is under Apache-2.0
and Community License for Baichuan2 Model.
DeepSeek-LLM-7B is under MIT license and
Deepseek License Agreement. Qwen1.5-7B are
licensed “AS IS”. Llama3-8B is released under the
Meta Llama 3 Community License Agreement.
C.2
Runtime
All experiments were run on an NVIDIA RTX
A6000 GPU. On average, it took around 50 hours
to evaluate one model on all languages in both ex-
periments. In total, approximately 400 GPU hours
were used.

--- Page 9 ---

0
1
2
3
fertility
Qwen1.5-7B
Yi-6B
0
1
2
3
fertility
deepseek-llm-7b-base
internlm2-7b
0
1
2
3
fertility
Baichuan2-7B-Base
XVERSE-7B
bod_Tibt
kac_Latn
kaz_Cyrl
uzn_Latn
cmn_Hans
cmn_Hant
jpn_Jpan
kor_Hang
ind_Latn
lao_Laoo
mya_Mymr
tha_Thai
vie_Latn
zsm_Latn
deu_Latn
eng_Latn
fra_Latn
ita_Latn
spa_Latn
lang_code
0
1
2
3
fertility
Meta-Llama-3-8B
bod_Tibt
kac_Latn
kaz_Cyrl
uzn_Latn
cmn_Hans
cmn_Hant
jpn_Jpan
kor_Hang
ind_Latn
lao_Laoo
mya_Mymr
tha_Thai
vie_Latn
zsm_Latn
deu_Latn
eng_Latn
fra_Latn
ita_Latn
spa_Latn
lang_code
Mistral-7B-v0.3
lang_category
Chinese Ethnic Minorities
Mandarin Chinese
Northeast Asian
Southeast Asian
US/European
Figure 4: Tokenization by different models and languages. Fertility on the y-axis is defined as number of tokens
divided by number of characters in a sentence. Therefore, the higher the number means a sentence is more
fragmented by tokenizers. Overall, Lao (lao_Laoo), Burmese (mya_Mymr) and Tibetan (bod_Tibt) are the most
fragmented languages. Baichuan2 and XVERSE produce more balanced tokenization result across languages.
Indonesian
Japanese
Korean
Lao
Burmese
Thai
Vietnamese
Standard Malay
Indonesian
Japanese
Korean
Lao
Burmese
Thai
Vietnamese
Standard Malay
Indonesian Japanese
Korean
Lao
Burmese
Thai
Vietnamese
Standard Malay
Indonesian
Japanese
Korean
Lao
Burmese
Thai
Vietnamese
Standard Malay
Chinese Models
International Models
Unnormalized PPL
Zero−shot MC Accuracy
30
100
300
1000
3000
30
100
300
1000
3000
100
200
300
0.3
0.4
0.5
0.6
0.7
National GDP (billion USD)
Mean Metric Across Models
Figure 5: Looking at the languages spoken by China’s neighboring countries, performance metrics correlates with
national GDP, and the trend of Chinese models and international models are highly similar.

--- Page 10 ---

Model
Correlation with log(national GDP)
Correlation with log(language speakers)
Experiment 1
Experiment 2
Experiment 1
Experiment 2
Qwen1.5
-0.940
0.872
-0.898
0.883
Yi
-0.659
0.890
-0.830
0.855
XVERSE
-0.916
0.942
-0.818
0.719
DeepSeek
-0.887
0.927
-0.874
0.855
InternLM2
-0.843
0.915
-0.858
0.867
Baichuan2
-0.909
0.920
-0.792
0.841
AVG
-0.859
0.911
-0.845
0.837
Llama 3
-0.921
0.871
-0.875
0.894
Mistral
-0.908
0.882
-0.891
0.875
AVG
-0.914
0.877
-0.883
0.884
Table 4: Correlations between performance metrics of experiment 1 and 2 with log(language speakers) for all 18
languages and log(national GDP) for Lao, Burmese, Thai, Malay, Vietnamese, Indonesian, Korean, and Japanese.
Language performance as measured by both experiments metrics are highly correlate with data resources, as
measured by number of speakers and GDP, where increased resources correlates with better performance.

```
