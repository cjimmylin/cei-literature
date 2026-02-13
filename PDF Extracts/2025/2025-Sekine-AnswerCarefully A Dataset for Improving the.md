---
title: "2025-Sekine-AnswerCarefully A Dataset for Improving the - PDF Extract"
source_pdf: "2025-Sekine-AnswerCarefully A Dataset for Improving the.pdf"
pages: 10
extracted_at: "2026-02-13T09:15:42.130020"
---

# PDF Extract: 2025-Sekine-AnswerCarefully A Dataset for Improving the

**Source PDF:** 2025-Sekine-AnswerCarefully A Dataset for Improving the.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

arXiv:2506.02372v1  [cs.CL]  3 Jun 2025
AnswerCarefully: A Dataset for Improving the Safety
of Japanese LLM Output
Hisami Suzuki
NII-LLMC
hisamis@nii.ac.jp
Satoru Katsumata
Retrieva, Inc.
satoru.katsumata@retrieva.jp
Takashi Kodama
NII-LLMC
tkodama@nii.ac.jp
Tetsuro Takahashi
Kagoshima University
takahashi@ibe.kagoshima-u.ac.jp
Kouta Nakayama
NII-LLMC
nakayama@nii.ac.jp
Satoshi Sekine
NII-LLMC
sekine@nii.ac.jp
Abstract
In this paper we present AnswerCarefully, a dataset for promoting the safety and
appropriateness of Japanese LLM outputs. The dataset consists of 1,800 pairs of
questions and reference answers, where the questions require special attention in
answering. It covers a wide range of risk categories established in prior English-
language datasets, but the data samples are original in that they are manually created
to reflect the socio-cultural context of LLM usage in Japan. We show that using this
dataset for instruction to fine-tune a Japanese LLM led to improved output safety
without compromising the utility of general responses. We also report the results of
a safety evaluation of 12 Japanese LLMs using this dataset as a benchmark. Finally,
we describe the latest update on the dataset which provides English translations and
annotations of the questions, aimed at facilitating the derivation of similar datasets
in different languages and regions. fc
1
Introduction
Applications of Large Language Models (LLMs) such as ChatGPT have become popular very quickly
in recent years, as they enable highly fluent dialogue and allow conversational access to knowledge
in many languages. At the same time, these models cannot guarantee the accuracy of the information
they provide, causing models to output incorrect information (so-called hallucination), reproduce and
spread social prejudices and biases, false information and other inappropriate information, and can
even be used to assist criminal activities. In addition, LLMs are so fluent in generating language that
we need to be mindful of the risks that humans become over-dependent on them psychologically and
emotionally.
Organizations that develop LLMs take these issues seriously, and devote considerable efforts in
curtailing harmful or inappropriate responses by their models [2, 10, 12, 13], especially as the risks
presented by these models become even more emphasized as the models get larger, more powerful
and more convincing in generating both useful and harmful responses. At this stage, however, it is
difficult to address harmfulness of a model in any principled manner, and consequently the removal
of harmfulness from a model response largely depends on alignment via safety fine-tuning and on the
so-called red-teaming efforts aimed at ensuring that model responses are free of harmful content or
expression via an extensive and focused stress-testing by specialists. Even though these alignment
and red-teaming processes are carried out in English, the resulting models are impressively successful
in suppressing obviously harmful or inappropriate responses to a large extent even in Japanese. That
said, what counts as harmful or inappropriate depends on the cultural context; for example, there are
cultural biases against different groups in different societal conditions, different cultural or religious
Preprint.

--- Page 2 ---

Figure 1: Sample data from AnswerCarefully (with English translation)
taboos exist, and different types of criminal activities are more prevalent in different countries. It
is also known that a foreign language itself can be an attack vector [13], in that models are more
vulnerable to malicious attacks in languages other than English. We have yet to see if the LLMs
trained and aligned mostly with English data are sufficiently safe for public consumption in Japan in
these extended aspects.
AnswerCarefully(AC)1 is a dataset for improving the safety of Japanese LLM output, developed with
the above background in mind. Figure 1 is an example AC data. While there are existing datasets
such as JBBQ [16], TruthfulQA [7] and JSocialFact [9] that target the safety of Japanese LLM, they
are restricted to specific domains: JBBQ focuses solely on bias and prejudice, and TruthfulQA and
JSocialFact deal with factuality only. In contrast, AC adopts a broad range of harmful categories based
on Do-Not-Answer dataset [14] (hereinafter referred to as DNA) which was originally developed for
English, providing one of the most comprehensive safety categories for LLM output. Unlike DNA
which uses GPT-4 to generate the questions in the dataset, we collected our questions manually from
our contracted annotators. This ensures that the questions are natural, realistic and free of usage
restrictions, unlike those in DNA which tend to be templatic, abstract and unnatural and are bound
by the usage terms of GPT-4. Another difference from DNA is that our dataset includes reference
answers paired with the questions so as to serve as an instruction data for fine-tuning LLMs. We used
AC for fine-tuning LLM-jp-13B-v2.0, a Japanese LLM developed by LLM-jp 2, and found that the
harmful answer rate of the model was significantly reduced without compromising the usefulness
of answers to general questions. We also used AC as a benchmark for evaluating 12 LLMs used in
Japan for their safety, and found that there were significant differences in the results of these models.
This paper is organized as follows. We first describe the details of the AC dataset in Section 2. Since
the value of the data is tied to the safety evaluation of LLMs, Section 3 describes the safety evaluation
metrics that we used. Section 4 reports on the safety alignment experiment via fine-tuning using
AC, and Section 5 on the evaluation 12 LLMs in use in Japan using AC as a safety benchmark. We
conclude the paperin Section 6 by describing the recent addition of the annotations to facilitate the
creation of similar data in different languages, as well as our plans for future versions.
2
AnswerCarefully Dataset
AC is a dataset that consists of questions that literally need to be answered carefully along with their
reference answers, created to promote the safety of Japanese LLM output. Table 1 shows the statistics
of the dataset. Given that there was previously no broad-coverage safety dataset in Japanese, we
focused on collecting safety data as quickly and widely as possible. We therefore relied on the safety
taxonomy of DNA, which proposes the most comprehensive classification of LLM safety categories
that we were aware of, and collected questions and reference answers in Japanese from scratch from
contracted annotators. In version 1.0 (ACv1), we used DNA’s three-level hierarchical risk categories
as is, consisting of 5 Level-1 categories (risk areas), 12 Level-2 categories (harm types), and 61
Level-3 categories (specific harms). In version 2.0 (ACv2), we have slightly revised the Level-3
categories to 56 to balance the number of samples collected for Japanese in each category. The 12
Level-2 categories of DNA and AC are shown in the Appendix Table 4 for reference, as compared
1https://llmc.nii.ac.jp/en/answercarefully-dataset/
2https://llm-jp.nii.ac.jp/en/
2

--- Page 3 ---

v
Release Date
#samples (Test)
#samples (Dev)
#samples (All)
1
4/30/2024
183 (x3 per each Level-3 Category)
762
945
2
9/12/2024
336 (x6 per each Level-3 Category)
1,464
1,800
Table 1: Summary of AnswerCarefully dataset
with the corresponding categories in AILuminate v1.0 benchmark by MLCommons 3 which adopts
Llama Guard’s [3] categories 4.
Additional examples from AC are shown in the Appendix Figure 1. Potential safety risks of LLM
include both the risk of answering straightforward questions in a harmful or inappropriate way, as
well as the risk of someone with a level of expertise maliciously using LLM for harmful or illegal
activities. AC currently focuses on the former as an initial attempt to cover everyday LLM safety
concerns in Japanese. As we will see in Section 5, it poses an appropriate level of challenge to various
LLMs in service at the time of the release of the dataset.
The data samples in AC are created by human annotators, ensuring naturalness and quality of the
questions with the LLM usage in Japan in mind.5 This is different from DNA, where the data samples
are automatically generated using GPT-4, which can be unnatural and templatic. We also wanted to
avoid any usage restrictions imposed on the model output, as our goal was to create a dataset that
can be used by anyone for the purpose of improving the safety of Japanese LLM.6 Another unique
aspect of AC as a safety dataset is that it includes reference answers. Creating reference answers
for potentially unsafe or sensitive questions is not an easy task, precisely because they need to be
answered carefully. It is not our goal to offer the right response to these questions; rather, we strive to
offer an initial starting point for use in safety alignment, which can later be modified or enriched for
LLMs serving for specific purposes. We relied on the G7 Hiroshima AI Process7 for guidance, and
within the values of this process (such as saying nothing harmful or unsafe; unequivocally opposing
to illegal activities or discrimination; protecting human rights and democracy), we strive to present
multiple viewpoints and opinions for sensitive topics without taking a particular position. We also do
not overly anthropomorphize the responses, and when necessary ensure that users know the responses
are coming from an AI assistant. As we will discuss in Section 4.2, reference answers are not only
useful for model fine-tuning, but also valuable for improving the accuracy of automatic evaluation
(via LLM-as-a-judge) of LLM output safety.
3
Safety Evaluation
3.1
Evaluation Metrics
There are two ways for evaluating the safety of LLM output. One is to evaluate the harmfulness of
the output separately from its usefulness, as exemplified in such tools as Llama Guard 8. As this
evaluation method does not account for the helpfulness of the output, it requires a separate evaluation
metric for it. The challenge, however, is that when the helpfulness metrics (including accuracy,
factuality, detailedness and fluency) are separately applied to the responses to those questions that
need answering carefully, it is difficult to interpret the overall appropriateness of the response. This is
especially true as AC consists of those questions that can be answered (albeit carefully) rather than
those that cannot be answered at all. If a system simply fails to respond to such questions or responds
3https://ailuminate.mlcommons.org/benchmarks/
4For the definition of the full risk categories of AC including all Level-3 categories, see https://llmc.
nii.ac.jp/wp-content/uploads/2025/02/CategoryDefinitions_ACv2_English.pdf.
5We did not specifically instruct the annotators to include region- or culture-specific content, but 27% of
the collected data ended up including some culture-specific content, suggesting that simply translating English
safety datasets will not suffice. See Section 6 for a related discussion.
6Chinese DNA [15], an updated and extended version of DNA, has a manual process in creating questions
which mitigates there limitations.
7https://www.mofa.go.jp/ecm/ec/page5e_000076.html
8https://www.llama.com/docs/model-cards-and-prompt-formats/llama-guard-4/
3

--- Page 4 ---

Pearson
Spearman
Kendall
Annotator 1 & Annotator 2
0.698
0.619
0.559
Annotator 2 & Annotator 3
0.681
0.64
0.57
Annotator 3 & Annotator 1
0.666
0.654
0.578
Average of 3 annotators & GPT-4 (no reference answer)
0.505
0.557
0.449
Average of 3 annotators & GPT-4 (with reference answer)
0.667
0.679
0.571
Table 2: Correlation between human and automatic evaluation
with irrelevant answers, it can be scored high on the safety scale, but the usefulness will be extremely
low. We would like our metrics to distinguish appropriate refusal from safe but useless responses 9.
Therefore, we have adopted a rating system that evaluates the harmfulness and helpfulness on a single
scale. Specifically, we first rate the responses based on the following five-level evaluation criteria
proposed in Meta’s Llama2-Chat [13]10:
5 : Response includes no safety violation, and is very helpful
4 : No safety violation, but minor issues other than those related to safety
3 : No safety violation, but response not useful at all or has major issues other than safety
2 : Minor or moderate safety violation(s)
1 : Major safety violation(s)
In Llama2-Chat, the percentage of outputs that are given a rating of 1 or 2 is called Violation Rate,
and is used as the rate of harmful responses of a system. In addition, we also define Acceptable
Response Rate, which is the percentage of outputs with a rating of 4 or 5, as an indicator of how well
the system responds to harmful or sensitive questions overall. These two metrics together can capture
the potential trade-off relation between safety and helpfulness in the responses to the questions in AC.
We will therefore use these two metrics in our discussion below11.
3.2
Automatic Evaluation
While manual evaluation is an essential process for continuously improving evaluation criteria, it
is difficult to perform frequently as it is resource intensive. For this reason, LLM-as-a-judge [17],
which uses LLM to evaluate the system output, has attracted a lot of attention in recent years, and we
also make use of this method extensively in AC safety evaluation. In order to verify the reliability
of LLM-as-a-judge in this context, we used the ACv1 evaluation set to investigate the correlation
between the ratings by three human annotators and GPT-4 (gpt-4-0613)12. Table 2 shows the
results.
As can be seen from the table, the correlation coefficients between two human annotators range
from 0.56 to 0.7, indicating a moderate positive correlation. In contrast, the correlation coefficient
between the automatic evaluator and the average scores of the three human annotators is from 0.45
to 0.55 when LLM-as-a-judge has no access to reference answers. Interestingly, the correlation
coefficients improve to the range from 0.57 to 0.68 when LLM-as-a-judge can use reference answers,
almost to the same level of the correlation as between the human annotators. This shows that AC’s
reference answers, though originally created for instruction tuning, are also for improving the quality
9[1] also discusses the downside of separating the datasets for helpfulness and harmfulness for the purpose of
RLHF.
10Since the Meta paper did not provide detailed descriptions of the evaluation criteria, we wrote our own,
extending them to cover the risk areas of Misinformation Harms and Human-Chatbot Interaction Harms that
are not covered in Llama2-Chat. The detailed evaluation criteria for each risk area used in AC are described in
Takahashi et al.[11].
11While we believe that these two metrics together are very informative in evaluating the quality of the
responses to sensitive questions, the average score of the 5-scale rating is not, as the intervals between these
ratings are not uniform. This is why we use the two metrics side by side rather than representing them with a
single average score.
12For more details about his investigation, see Nakayama et al. [8]
4

--- Page 5 ---

Safety (on ACv2-Test)
Usefulness (on MT Bench)
Violation Rate
Acceptable Response Rate
Average evaluation score
Usefulness data only
0.445
0.436
3.64±0.03
+ ACv1 x1
0.357
0.538
3.78±0.03
+ ACv1 x16
0.218
0.63
3.68
+ ACv2 x1
0.274
0.595
3.84±0.10
+ ACv2 x16
0.153
0.719
3.81±0.04
Table 3: Results of safety SFT using AC
of LLM-as-a-judge. Based on these results, we consider that LLM-as-a-judge is sufficiently reliable
in evaluations using AC, and in Section 4 below, we will investigate the effectiveness of safety
fine-tuning using automatic evaluation.
4
Safety Fine-Tuning with AC
As emphasized in preceding sections, AC is unique in that it is a safety dataset that comes with
reference answers. In this section, we describe the experiments where we used AC as an instruction
dataset for supervised fine-tuning (SFT) of a Japanese LLM, and show that it improved the safety of
a Japanese LLM output without compromising the usefulness in general.
The base model we used for this experiment is LLM-jp’s LLM-jp-13B-v2.013. The following
instruction datasets were used simultaneously for SFT14:
• OpenAssistant-1 (19,047 samples each in Japanese and English)
• OpenAssistant-2 (29,431 samples each in Japanese and English)
• Dolly (13,509 samples each in Japanese and English)
• ichikara-004-001-single (8,192 samples in Japanese)
• AnswerCarefully (762 samples in ACv1 development set and 1,464 in ACv2 development
set)
All of these datasets except for AC are instruction datasets for usefulness. Since AC is substantially
smaller in size than these, we also conducted an experiment in which we duplicated the AC data
16 times. For safety evaluation, we used the ACv2 evaluation set (336 samples) and performed
automatic evaluation with GPT-4-as-a-judge as described in the previous section. We also performed
an evaluation of Japanese MT-Bench 15 using GPT-4-as-a-judge (on a scale of 1-10) to check whether
side effects of safety tuning (excessive refusal to safe questions) were present in the general domain
responses.
The results are shown in Table 3. By using AC for SFT, violation rate goes down and acceptable
response rate goes up on the safety evaluation, without causing a negative side effect on the usefulness
evaluation. We also see that copying the safety data 16 times did help improve the safety of the model,
and that ACv2 is more effective than ACv1: there is a statistically significant difference (p < 0.05) in
violation rate comparing these two.
5
Benchmark Evaluation with AC
Many LLMs are currently in common use in Japan, but few systems are believed to have undergone
safety tuning or alignment in Japanese. In addition, there are no publicly available safety evaluations
of the Japanese output of the LLMs in the market. Therefore, we used the AC evaluation data as a
13https://huggingface.co/llm-jp/llm-jp-13b-v2.0
14For details of the comprehensive safety tuning experiment using AC, including the tuning of the latest model
of LLM-jp, LLM-jp-3-172B-instruct3, see Katsumata et al. [4].
15https://github.com/Stability-AI/FastChat/tree/jp-stable/fastchat/llm_judge
5

--- Page 6 ---

Figure 2: Results of human evaluation of 12 LLMs using AC
benchmark and manually evaluated 12 systems16. For evaluating these models, we used Violation
Rate and Acceptable Response Rate from Section 3. We obtained output from 12 LLMs for the 183
questions in ACv1 evaluation set, and asked three annotators to evaluate each output. If the evaluation
scores of the three evaluators differed by 2 or more, or if the scores straddled the boundary between 2
and 3 (i.e., the safety boundary), the person responsible for the evaluation (who wrote the guidelines)
assigned a final score. The results are shown in Figure 217.
What we can see from this table is that effectiveness of the safety measures of the LLMs currently used
in Japan varies greatly, and that the AC evaluation was able to capture this variation. The questions
in the AC evaluation data used in this evaluation are straightforward, and are not Jailbreak-type
questions that are deliberately devised to circumvent the safety measures of LLMs. Nevertheless, the
fact that the differences between systems are so pronounced in this evaluation suggests that the AC
dataset was effective as a benchmark at the time of the evaluation.
6
Concluding Remarks
This paper discussed AnswerCarefully, an instruction dataset aimed at improving the safety of LLMs,
and showed that it has been instrumental in safety fine-tuning of LLM output in Japanese and in
serving as a safety benchmark for the LLMs in Japan. As we have seen, the value of such dataset
is closely tied to the state of the LLMs: as the models become more capable of handling harmful
or sensitive questions, the dataset also needs to evolve to address the risks and challenges that the
models face at that time. In that vein, we are planning future updates and extensions to AC, including
the addition of borderline data (where the questions are similar to harmful or unsafe questions but
can be answered straightforwardly) [15, 5] and the regionally sensitive category (which includes
questions for which an appropriate answer or an official viewpoint differs depending on the country
16The following 12 systems were used for the evaluation experiment which was conducted in August 2024.
a:openai/gpt-35-turbo-1106
b:llm-jp/llm-jp-13b-instruct-full-ac_001_16x-dolly-ichikara_004_001_single-oasst-oasst2-v2.0
c:cyberagent/calm3-22b-chat
d:anthropic/anthropic.claude-3-5-sonnet-20240620-v1:0
e:llm-jp/llm-jp-13b-instruct-full-dolly-ichikara_004_001_single-oasst- oasst2-v2.0
f:tokyotech-llm/Llama-3-Swallow-70B-Instruct-v0.1
g:meta-llama/Meta-Llama-3-8B-Instruct
h:openai/gpt-4-0613
i:elyza/Llama-3-ELYZA-JP-8B
j:tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1
k:Qwen/Qwen2-72B-Instruct
l:google/gemma-2-27b-it
17For a detailed analysis of this human evaluation, see Takahashi et al.[11].
6

--- Page 7 ---

Figure 3: Sample mlmc annotation in ACv2.2
or region) [15]. Furthermore, we have recently added what we call multi-language-multi-culture
(mlmc) annotations to ACv2 as version 2.2, in line with the efforts of AI Safety Institute International
Network 18 promoting the creation of safety data for multiple languages and regions. A sample
annotation is shown in Figure 3: it adds English translation of the questions in AC, along with the
label adaptation-tag indicating whether the question includes any specific references to Japan and
if so, whether regional adaptation is possible by simply swapping entity names. We also added
translation-notes if the question requires explanation (beyond translation) to make sense as a safety
question in Japan. It is our hope that the addition of such information further stimulates the discussion
on LLM safety and creation of more datasets in many regions.
AC presents only an initial step toward promoting LLM safety; there are many challenges ahead of
us before the LLM can become accepted broadly as a safe tool in our society. We plan to continue
creating datasets that will play a part in addressing these challenges.
Acknowledgments
AnswerCarefully is a project of LLM-jp [6], a consortium for promoting cross-organizational col-
laboration on LLM research and development. Version 1 was created in part by RIKEN Center
for Advanced Intellfence Project (RIKEN AIP) 19 with the cooperation of Citadel AI 20. Version 2
was created primarily by Research and Development Center for Large Language Model at National
Institute of Informatics (NII-LLMC) 21.
References
[1] Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma,
Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath,
Jackson Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny
Hernandez, Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine
Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann,
and Jared Kaplan. Training a helpful and harmless assistant with reinforcement learning from
human feedback, 2022. URL https://arxiv.org/abs/2204.05862.
[2] Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones,
Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, Carol Chen, Catherine
Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli, Dustin Li, Eli
Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal
Ndousse, Kamile Lukosuite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer,
Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott Johnston,
18https://www.jstor.org/stable/resrep64561
19https://www.riken.jp/en/research/labs/aip/index.html
20https://citadel-ai.com/
21https://llmc.nii.ac.jp/en/
7

--- Page 8 ---

Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton,
Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben
Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Tom Brown, and Jared Kaplan.
Constitutional AI: Harmlessness from AI Feedback, 2022.
[3] Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi Rungta, Krithika Iyer, Yuning Mao,
Michael Tontchev, Qing Hu, Brian Fuller, Davide Testuggine, and Madian Khabsa. Llama
Guard: LLM-based input-output safeguard for human-AI conversations, 2023. URL https:
//arxiv.org/abs/2312.06674.
[4] Satoru Katsumata, Takashi Kodama, and Yusuke Miyao. Investigating tuning methods for
achieving usefulness and safety for Japanese large language models (in Japanese). In The 31st
Annual Conference of the Association for Natural Language Processing, 2025.
[5] Tomoya Kurosawa, Junya Takayama, Koki Wataoka, Koga Kobayashi, Masayuki Asahara, and
Sae Nishiuchi. Japanese safety boundary test for large language models (in Japanese). In The
31st Annual Conference of the Association for Natural Language Processing, 2025.
[6] LLM-jp, :, Akiko Aizawa, Eiji Aramaki, Bowen Chen, Fei Cheng, Hiroyuki Deguchi, Rintaro
Enomoto, Kazuki Fujii, Kensuke Fukumoto, Takuya Fukushima, Namgi Han, Yuto Harada,
Chikara Hashimoto, Tatsuya Hiraoka, Shohei Hisada, Sosuke Hosokawa, Lu Jie, Keisuke
Kamata, Teruhito Kanazawa, Hiroki Kanezashi, Hiroshi Kataoka, Satoru Katsumata, Daisuke
Kawahara, Seiya Kawano, Atsushi Keyaki, Keisuke Kiryu, Hirokazu Kiyomaru, Takashi
Kodama, Takahiro Kubo, Yohei Kuga, Ryoma Kumon, Shuhei Kurita, Sadao Kurohashi, Con-
glong Li, Taiki Maekawa, Hiroshi Matsuda, Yusuke Miyao, Kentaro Mizuki, Sakae Mizuki,
Yugo Murawaki, Akim Mousterou, Ryo Nakamura, Taishi Nakamura, Kouta Nakayama,
Tomoka Nakazato, Takuro Niitsuma, Jiro Nishitoba, Yusuke Oda, Hayato Ogawa, Takumi
Okamoto, Naoaki Okazaki, Yohei Oseki, Shintaro Ozaki, Koki Ryu, Rafal Rzepka, Keisuke
Sakaguchi, Shota Sasaki, Satoshi Sekine, Kohei Suda, Saku Sugawara, Issa Sugiura, Hiroaki
Sugiyama, Hisami Suzuki, Jun Suzuki, Toyotaro Suzumura, Kensuke Tachibana, Yu Takagi,
Kyosuke Takami, Koichi Takeda, Masashi Takeshita, Masahiro Tanaka, Kenjiro Taura, Ar-
seny Tolmachev, Nobuhiro Ueda, Zhen Wan, Shuntaro Yada, Sakiko Yahata, Yuya Yamamoto,
Yusuke Yamauchi, Hitomi Yanaka, Rio Yokota, and Koichiro Yoshino. LLM-jp: A Cross-
organizational Project for the Research and Development of Fully Open Japanese LLMs, 2024.
URL https://arxiv.org/abs/2407.03963.
[7] Yusuke Nakamura and Daisuke Kawahara. Construction of the Japanese TruthfulQA Dataset (in
Japanese). In The 30th Annual Conference of the Association for Natural Language Processing,
2024.
[8] Kouta Nakayama, Takashi Kodama, Hisami Suzuki, Yusuke Miyao, and Sekine. Satoshi. llm-jp-
judge: Japanese LLM-as-a-Judge evaluation tool (in Japanese). In The 31st Annual Conference
of the Association for Natural Language Processing, 2025.
[9] Tomoka Nakazato, Masaki Onishi, Hisami Suzuki, and Yuya Shibuya. JSocialFact: a misinfor-
mation dataset from social media for benchmarking LLM safety. In 2024 IEEE International
Conference on Big Data (BigData), pages 3017–3025, 2024. doi: 10.1109/BigData62323.2024.
10825770.
[10] OpenAI. GPT-4 technical report, 2024.
[11] Tetsuro Takahashi, Hisami Suzuki, and Satoshi Sekine. Large-scale human evaluation of LLM
safety (in Japanese). In The 31st Annual Conference of the Association for Natural Language
Processing, 2025.
[12] Gemini Team. Gemini: A family of highly capable multimodal models, 2024.
[13] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei,
Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas
Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes,
Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony
Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian
8

--- Page 9 ---

Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut
Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov,
Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta,
Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiao-
qing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng
Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien
Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. Llama 2: Open foundation
and fine-tuned chat models, 2023.
[14] Yuxia Wang, Haonan Li, Xudong Han, Preslav Nakov, and Timothy Baldwin. Do-Not-Answer:
Evaluating safeguards in LLMs. In Yvette Graham and Matthew Purver, editors, Findings of
the Association for Computational Linguistics: EACL 2024, pages 896–911, St. Julian’s, Malta,
March 2024. Association for Computational Linguistics. URL https://aclanthology.org/
2024.findings-eacl.61.
[15] Yuxia Wang, Zenan Zhai, Haonan Li, Xudong Han, Shom Lin, Zhenxuan Zhang, Angela Zhao,
Preslav Nakov, and Timothy Baldwin. A Chinese Dataset for Evaluating the Safeguards in Large
Language Models. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Findings of the
Association for Computational Linguistics: ACL 2024, pages 3106–3119, Bangkok, Thailand,
August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.findings-acl.
184. URL https://aclanthology.org/2024.findings-acl.184/.
[16] Hitomi Yanaka, Namgi Han, Ryoma Kumon, Jie Lu, Masashi Takeshita, Ryo Sekizawa,
Taisei Kato, and Hiromi Arai. Analyzing social biases in Japanese large language models.
arxiv:2406.02050, 2024.
[17] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica.
Judging LLM-as-a-judge with MT-bench and Chatbot Arena. In Advances in Neural Information
Processing Systems, volume 36, 2023.
A
Appendix
9

--- Page 10 ---

DNA/AC Level-1 (risk areas)
DNA/AC
Level-2
(harm
types)
ML Commons AILuminate
v1.0
Discrimination,
Exclusion,
Toxicity, Hateful, Offensive
Adult Content
Sexual Content
Social stereotypes and unfair
discrimination
Toxic language (hate speech)
Defamation, Hate
Human-Chatbot
Interaction
Harms
Mental Health or Overreliance
Crisis
Suicide and Self-Harm
Treat Chatbot as a Human
Information Hazards
Leakage of private informa-
tion (person/individual)
Privacy
Leakage
of
sensitive
information
(organiza-
tion/government)
Intellectual Property
Malicious Uses
Assisting illegal activities
Violent Crimes, Non-Violent
Crimes, Sex-Related Crimes
Child Sexual Exploitation, In-
discriminate Weapons
Nudging or advising users to
perform unethical or unsafe ac-
tions
Reducing the cost of disinfor-
mation campaigns
Misinformation Harms
Causing material harm by dis-
seminating misinformation
Specialized Advice
Disseminating false or mis-
leading information
Table 4: Safety Categories of Do-Not-Answer, AnswerCarefully and AILuminate
Figure 4: Additional samples from AnswerCarefully (translated into English)
10

```
