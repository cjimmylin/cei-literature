---
title: "A Benchmark for Large Language Models on Northern - PDF Extract"
source_pdf: "2025-Kaewkasi-A Benchmark for Large Language Models on Northern.pdf"
pages: 10
extracted_at: "2026-01-24T16:38:28.187430"
---

# PDF Extract: A Benchmark for Large Language Models on Northern

**Source PDF:** 2025-Kaewkasi-A Benchmark for Large Language Models on Northern.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Assessing Thai Dialect Performance in LLMs with Automatic Benchmarks
and Human Evaluation
Peerat Limkonchotiwat1,4,*, Kanruethai Masuk,2,*, Surapon Nonesung3,*,
Chalermpun Mai-On2,*, Sarana Nutanong2, Wuttikorn Ponwitayarat2,*,
Potsawee Manakul3,*,
1AI Singapore, 2Vidyasirimedhi Institute of Science and Technology,
3SCB10X, 4National University of Singapore,
Correspondence: peerat@aisingapore.org
Abstract
Large language models show promising results
in various NLP tasks. Despite these successes,
the robustness and consistency of LLMs in un-
derrepresented languages remain largely unex-
plored, especially concerning local dialects. Ex-
isting benchmarks also focus on main dialects,
neglecting LLMs’ ability on local dialect texts.
In this paper, we introduce a Thai local dialect
benchmark covering Northern (Lanna), North-
eastern (Isan), and Southern (Dambro) Thai,
evaluating LLMs on five NLP tasks: summa-
rization, question answering, translation, con-
versation, and food-related tasks. Furthermore,
we propose a human evaluation guideline and
metric for Thai local dialects to assess gen-
eration fluency and dialect-specific accuracy.
Results show that LLM performance declines
significantly in local Thai dialects compared
to standard Thai, with only proprietary models
like GPT-4o and Gemini2 demonstrating some
fluency1.
1
Introduction
Large language models (LLMs) play a crucial role
in natural language processing (NLP) by signifi-
cantly enhancing downstream performance across
diverse tasks and languages. Studies have shown
that LLMs surpass traditional multilingual mod-
els (Devlin et al., 2019; Conneau et al., 2020) in
tasks such as question answering and summariza-
tion (Touvron et al., 2023; Pipatanakul et al., 2023).
One key reason is that LLMs have significantly
larger parameter counts and training datasets, of-
ten exceeding traditional models by a factor of 26,
from 0.3 billion to 8 billion parameters. As a re-
sult, LLMs demonstrate greater robustness than
traditional models across most scenarios, particu-
larly in low-resource languages such as Thai (Peng-
pun et al., 2024; Phatthiyaphaibun et al., 2024),
*Equal contributions
1Data and Evaluation Tool: https://github.com/mrpee
rat/Thai_local_benchmark
Indonesian (Cahyawijaya et al., 2024, 2023), and
Tagalog (Montalan et al., 2024; Gamboa and Lee,
2025).
Researchers are increasingly evaluating LLMs
in underrepresented languages, particularly Thai,
to assess their robustness and consistency in low-
resource languages. Thai-H6 (Kim et al., 2025)
introduces an evaluation benchmark for assessing
LLMs’ understanding of Thai cultural knowledge.
SEACrowd (Lovenia et al., 2024) introduces a
Southeast Asian benchmark for evaluating LLMs
on local and cross-lingual texts, audios, and im-
ages, focusing on natural language generation and
understanding. The Thai LLM benchmark2 extends
SEACrowd by incorporating LLM-as-a-Judge and
Thai Exam datasets for a Thai language evalua-
tion. However, these benchmarks primarily focus
on the Central Thai dialect. Therefore, challenges
observed in the Central dialect may also reflect
underlying issues in local dialects.
Although there are 69 million Thai speakers,
only about 20 million have Central Thai as their
first language. The rest primarily grow up speaking
other dialects, including approximately 15.2 mil-
lion who speak Northeastern Thai (Isan), 6 million
who speak Northern Thai (Lanna), and 4.5 million
who speak Southern Thai (Dambro) or other local
varieties. As shown in Figure 1a, a distinct fea-
ture of Thai local dialects is the blending of words
between Central Thai and local dialects, as well
as among different local dialects. Moreover, each
local dialect has distinct words, some unique to
that dialect and others shared with other dialects
but not found in others. Recent studies examine
the evaluation of fluency and understanding in lo-
cal dialects of Indonesian (Syarfina et al., 2022;
Cahyawijaya et al., 2023; Veria Septianingtias and
Ariyani, 2024) and Filipino (Tabajunda, 2018; Gue-
2https://huggingface.co/spaces/ThaiLLM-Leade
rboard/leaderboard
arXiv:2504.05898v1  [cs.CL]  8 Apr 2025

--- Page 2 ---

[หมู่เฮา]ตอนเที่ยง
มี[ไผ]อยากไปกิน[ตำบักหุ่ง]
ร้านครัวคุณกร[บ่?]
Identify local dialect units
Generation
= 0.5
[หมู่เฮา] 
[ไผ]
[บ่?]
[ตำบักหุ่ง]
Fluency 
= 1.0
[บ่อ]มี[ไผ]อยาก
[บ่อ]
[ไผ]
(We)
(Who)
(No/Or Not)
(No/Or Not)
(Who)
(Papaya Salad)
หมู่เฮาตอนเที่ยงมีไผอยากไปกินตำบักหุ่งร้านครัวคุณกรบ่?
พวกเราตอนเที่ยงมีใครสนใจไปกินส้มตำไก่ย่างที่ร้านครัวคุณกรไหม?
Anyone interested in joining us for papaya salad and grilled chicken at
Khun Korn’s Kitchen for lunch?
Central Thai:
English:
หมู่เฮาตอนเที่ยงมีไผสนใจไปกินส้มตำไก่ย่างตี๋ร้านครัวคุณกรก่อ?
Northern:
โบ๋เราตอนเที่ยงยังใครที่อาดไปกินส้มตำไก่ย่างที่ร้านครัวคุณกรมั้งม่าย?
Southern:
Eastern:
1. Shared tokens between local dialects (underline)
2. Some Dialects has specific tokens that not appear in other dialects (square)
3. Wh- question that used in 
different dialects (circle)
(a)
(b)
[Translation]:
Guys, do anyone want papaya salad 
at Korn's restuarnt for lunch?
[Translation]: No one
want to go.
Figure 1: (a) We showed some unique characteristics of Thai local dialects compared to Central Thai: 1. shared
tokens in local dialects; 2. unique words for each local dialect; and 3. WH- question tokens that are different in each
local dialect. (b) Illustration of our local dialect evaluation metric. The example demonstrates the assessment of
generation and fluency, highlighting variations in spelling and pronunciation among different Thai dialects.
vara et al., 2024). Evaluating the fluency and un-
derstanding of LLMs in Thai local dialects remains
underexplored.
In this paper, we introduce a benchmark for
evaluating local Thai dialects–Isan, Lanna, and
Dambro–to assess LLMs’ understanding of these
dialects. Specifically, we evaluate LLMs on five
tasks – summarization, question answering, trans-
lation, conversation, and food – using instructions,
inputs, and labels written in local dialects. Addi-
tionally, we introduce human evaluation alongside
a new Thai local dialect guideline and metric to
assess LLMs’ capabilities in understanding and
generating local dialects. The new metric evaluates
the generation and fluency of local dialects, reward-
ing or penalizing the model for fluency in a manner
consistent with human speakers. Our experimental
results show that LLM performance significantly
declines on summarization and translation tasks
when inputs are written in local dialects, compared
to inputs in Central Thai. Furthermore, only pro-
prietary models–GPT and Gemini–are capable of
speaking local Thai dialects, as shown by both hu-
man evaluation and our new metric.
Our contributions are as follows: We introduce a
benchmark for evaluating three Thai local dialects.
We also propose a guideline and metric to assess
the generation and fluency of LLMs in Thai local
dialects. Lastly, we are the first to investigate Thai
local dialects in the context of LLMs, presenting
comprehensive evaluations using both traditional
evaluation metrics and human assessment.
2
Benchmark and Metric
2.1
Benchmark Formulation
Data Selection. We create a new benchmark for
evaluating three Thai local dialects–Isan, Lanna,
and Dambro–drawing on examples from the Thai
LLM leaderboard to assess model performance.
We select generation tasks—Question Answering
(QA), summarization, and translation—because
they are more complex and better suited for assess-
ing model knowledge than more straightforward
multiple-choice QA tasks. We randomly selected
20 samples for each task, resulting in 80 samples
per dialect, where the translation task was both
English to local dialects and vice versa. In addi-
tion, we include 10 topics on food (i.e., asking
for a food recipe of [FOOD_NAME]) and conver-
sations between two individuals discussing Thai
traditional and cultural topics (i.e., talking bout
[TOPIC_NAME]). The full topics can be found in
Appendix A.7.
Gold Standard. Our dataset uses the gold standard
provided by the original Central Thai examples.
Note that we do not create labels for the food and
conversation topics, as these tasks are open-ended
and lack a definitive correct answer. Instead, we
rely on human evaluation to assess these tasks. The
number of samples is 100, all written in Central
Thai.
Translation. We enlisted native speakers of each
local dialect to translate the 100 samples from Cen-
tral Thai into their respective dialects. This in-
cludes translating the input, context (for QA and
summarization tasks), prompts, and labels, except
for those related to food and conversation sam-
ples. Furthermore, all annotators are asked to re-
view translations completed by their peers within
the same region to ensure quality and consistency.
Therefore, the total number of samples is 400, com-
parable to previous LLM-as-a-Judge and Human
evaluation benchmarks (Zheng et al., 2023; Qin
et al., 2024). For the full information of data statis-
tics, prompts, topics, annotator demographics, and
guidelines, see Appendix A.

--- Page 3 ---

Model
Dialect
QA
∆Diff
Summarization
∆Diff
Translation (E-L)
∆Diff
Translation (L-E)
∆Diff
Llama-3.1-8b
Central
60.74
-
20.07
-
11.41
-
44.61
-
Typhoon1.5-8b
Central
33.36
-
11.52
-
5.14
-
47.35
-
Llama-3.1-70b
Central
56.44
-
23.03
-
18.11
-
51.07
-
Typhoon1.5-70b
Central
46.99
-
10.83
-
8.46
-
50.54
-
GPT-4o
Central
56.03
-
14.67
-
21.926
-
62.82
-
Gemini2
Central
53.73
-
17.70
-
20.76
-
58.10
-
Llama-3.1-8b
Isan
58.84
1.90
16.47
3.60
3.17
8.24
6.59
38.02
Typhoon1.5-8b
Isan
28.48
4.88
8.54
2.98
0.83
4.31
31.6
15.75
Llama-3.1-70b
Isan
57.59
↑1.15
18.77
4.26
8.98
9.13
33.74
17.33
Typhoon1.5-70b
Isan
45.32
1.67
10.87
↑0.04
2.82
5.64
41.81
8.73
GPT-4o
Isan
44.21
11.82
10.39
4.28
14.29
7.63
55.26
7.56
Gemini2
Isan
40.58
13.15
12.68
5.02
13.31
7.45
51.74
6.36
Llama-3.1-8b
Lanna
55.66
5.08
18.05
2.02
2.46
8.95
7.27
37.34
Typhoon1.5-8b
Lanna
24.39
8.97
7.28
4.24
0.49
4.65
18.48
28.87
Llama-3.1-70b
Lanna
50.97
5.47
17.41
5.62
3.73
14.38
15.92
35.15
Typhoon1.5-70b
Lanna
44.74
2.25
10.17
0.66
4.76
3.70
39.01
11.53
GPT-4o
Lanna
45.73
10.30
9.78
4.89
12.02
9.90
54.83
7.99
Gemini2
Lanna
40.86
12.87
11.70
6.0
7.68
13.08
47.28
10.82
Llama-3.1-8b
Dambro
61.38
↑0.64
16.91
3.16
7.22
4.19
24.02
20.59
Typhoon1.5-8b
Dambro
31.34
2.02
9.18
2.34
4.20
0.94
27.81
19.54
Llama-3.1-70b
Dambro
66.96
↑10.52
17.2
5.83
7.66
10.45
27.10
23.97
Typhoon1.5-70b
Dambro
52.10
↑5.11
9.74
1.09
0.78
7.68
39.19
11.35
GPT-4o
Dambro
49.28
6.75
12.87
1.80
12.95
8.97
45.32
17.50
Gemini2
Dambro
47.91
5.82
12.07
5.63
9.13
11.63
23.46
34.64
Table 1: The main results of our benchmark. We calculate the ∆Diff by comparing Central and local dialects at the
same model. In addition, E equals to English and L equals to local dialects.
2.2
Human Evaluation for Local Dialects
Traditional evaluation metrics, such as BLEU (Pa-
pineni et al., 2002) and ROUGE-L (Lin, 2004),
struggle to assess dialectal text accurately. A key
challenge is their reliance on tokenization, which
fails when dialect words are missing from standard
dictionaries, resulting in inaccurate segmentation.
Furthermore, the absence of a standardized writ-
ing system leads to multiple valid spellings for the
same word. Therefore, these traditional metrics
that compare generated text to a fixed reference fail
to account for such variations, often misclassify-
ing correct responses as errors. These limitations
underscore the urgency of developing more flex-
ible evaluation methods that reflect the linguistic
diversity of dialects.
To bridge these gaps, we conduct our local di-
alect evaluation metric as follows.
1 Annotators evaluate whether the generated out-
put includes accurate local units, covering all
forms of writing: nouns, phrases, and sentences.
2 Different dialect spellings are allowed if they
share the same pronunciation. We ensure this
by transliterating the word and comparing its
phonetic transcriptions.
3 We divide our assessment into two categories:
language Generation (similar to recall) and lan-
guage Fluency (similar to precision). First, an-
notators (native local dialect speakers) evaluate
language Generation by assigning a score of 0
(no local dialect generated), 0.5 (partially gen-
erated), or 1 (fully generated). Next, annotators
assess the correctness and naturalness (Fluency)
of the generated dialectal words using the same
scoring system as Generation: 0 (completely
incorrect), 0.5 (partially correct), and 1 (fully
correct and natural). The final score is calculated
by the average over two annotators.
Figure 1(b) illustrates an example of our evalua-
tion using the proposed metrics. Some extracted
units have the same meaning but are written differ-
ently. Both writings are considered correct because
they share the same pronunciation. In addition, the
averages of annotator agreements (Appendix A.4)
from three dialects are 0.7969 and 0.7449 for Gen-
eration and Fluency, respectively. We discussed
the possibility of replacing humans with LLMs in
Appendix B.
3
Experimental Setups and Results
3.1
Setup
To evaluate Thai local dialects, we use well-known
Thai and multilingual LLMs for 8 and 70 billion
parameters, namely Typhoon1.5 3 and Llama3.1 4.
We also evaluate proprietary LLMs, such as GPT-
4o and Gemini2, in our benchmark. We use BLEU
for translation and ROUGE-L for QA and summa-
rization according to the original benchmark (Love-
nia et al., 2024), including the generation setting for
a fair comparison with previous benchmark works.
3https://huggingface.co/collections/scb10x/ty
phoon-15x-6648d7b07ab33d141d6648b6
4https://huggingface.co/collections/meta-lla
ma/llama-31-669fc079a0c406a149a5738f

--- Page 4 ---

A vs B
Isan
Lanna
Dambro
A
B
Both
None
A
B
Both
None
A
B
Both
None
Typhoon1.5-8b vs Llama3.1-8b
1
-
-
19
-
-
-
20
1
-
-
19
Typhoon1.5-70b vs Llama3.1-70b
-
1
-
19
2
-
-
18
4
-
-
16
Gemini2 vs Typhoon1.5-70b
20
-
-
-
19
-
-
1
16
2
1
1
Gemini2 vs GPT-4o
4
3
13
-
18
-
2
-
16
2
2
-
Table 2: Human fluency preference on conversation and food topics. The full details are described in Section 3.3.
3.2
Traditional Metric Results
Table 1 shows a significant decline in translation
performance for both 8B and 70B models, with the
largest drop observed in Lanna. Results in Isan and
Dambro were more mixed. In particular, QA per-
formance improved in both Dambro and Isan. One
possible explanation is that ROUGE-L measures
only text overlap, assessing correctness based on
matching words rather than fluency. Appendix C
provides LLMs’ outputs, revealing that ROUGE-L
assigned high scores even when Llama-3.1-70B
failed to produce local dialects. In particular, none
of the models produced responses in Thai local di-
alects, even when explicitly prompted to do so. If
reference labels are not written in local dialects,
models may still achieve high scores despite failing
to generate dialectal text, as shown in Table A.2 that
QA and summarization exhibit higher word over-
lap in Central and local dialects than translation.
This highlights the need for alternative evaluation
techniques that assess fluency rather than relying
solely on exact match metrics.
3.3
Human Evaluation
To verify that existing models do not generate Thai
local dialects and the traditional metric problem in
Thai local dialects, we conduct a human evaluation
focused on fluency in food and conversation topics.
We also recruit three native speakers per dialect to
assess the fluency of LLM outputs, selecting one
of four options: (A) for Prefer A, (B) for Prefer B,
(Both) for liking both models equally, or (None)
for disliking without any preference. In addition,
we average the answer from three annotators to
formulate the final answer. The annotator guideline
can be found in Appendix A.6.
Table 2 confirms that all open-source models fail
to generate Thai local dialects, as expected. Ty-
phoon and Llama received the highest number of
both are the worst ratings from annotators. For
the Dambro dialect, Typhoon demonstrates some
ability to generate local dialects, aligning with Ta-
ble 1, where it showed improvement in Dambro
texts. Gemini generates local dialects more flu-
ently and outperforms other models in nearly every
comparison. However, these results reflect only a
preference-based evaluation, while the actual flu-
ency of LLMs in local dialects remains unmeasured.
This underscores the need for an alternative metric
to assess dialect fluency beyond exact match scores
or subjective human ratings.
3.4
Our Local Dialect Metric
To better assess LLMs’ fluency and generative abil-
ity in local dialects, we evaluate them using our pro-
posed metric. As described in Section 2.2, two na-
tive speakers evaluate Typhoon1.5-70B and Gem-
ini2 for QA, summarization, and translation.
Table 3 shows that when we focus only on eval-
uating the generation and fluency performance in
Thai local dialects, only Gemini2 speaks Thai lo-
cal dialects.
Although Typhoon1.5-70b outper-
formed Gemini2 in the traditional metric perfor-
mance in Table 1, we found a significant gap
between these models.
Gemini2 achieves over
∼92.58 points in the Lanna dialect and ∼84.49
points in Dambro, while Typhoon achieves less
than 31 points and 12 points in Dambro and Lanna,
respectively. Moreover, the results of our experi-
ment also conform with Table 2 that Gemini2 is
better than Typhoon1.5 with more deep analysis
results, the Generation and Fluency score. This
emphasizes the robustness of our metric, which
can measure the ability to speak the local dialect
fluently, unlike the traditional metrics (Table 1) and
human preference (Table 2).
Model
Isan
Lanna
Dambro
G.
F.
Avg.
G.
F.
Avg.
G.
F.
Avg.
Typhoon
10.34 15.74 13.04 10.71 13.22 11.97 30.50 30.00 30.25
Gemini2
86.57 82.41 84.49 91.33 93.99 92.58 75.50 68.50 71.83
Table 3: The results from our propose metric. Note that
G. is Generation and F. is Fluency.
4
Conclusion
Our study highlights the significant performance
gap in LLMs when processing Thai local dialects.
While proprietary models like GPT-4 and Gemini
demonstrate some capability in understanding and
generating local dialects, most LLMs struggle with
fluency and accuracy. Our proposed benchmark,
human evaluation, and a new guideline and met-

--- Page 5 ---

rics provide valuable insights into these limitations,
paving the way for future improvements in multi-
lingual and dialect-aware LLMs.
Limitation
• We select only the main local dialects in Thai-
land since some dialects do not have a writing
system, only speaking.
• We experiment only with top-performance
Thai LLMs, such as Typhoon1.5, Llama3.1,
Gemini2, and GPT-4o. We acknowledge other
Thai LLMs, such as WangchanLION and
OpenThaiGPT. However, we found that only
the typhoon model has 8 and 70 billion model
parameters, covering all experiments in our
paper.
• Extending the proposed metric to other lan-
guages. We acknowledge that our paper does
not explain extending our metric to other lan-
guages. Our proposed metric can extend to
other languages when human annotators who
can speak local dialects are available. We will
study this in our future work.
• Limited number of annotators. We use only
five annotators for each local dialect. How-
ever, the agreement score demonstrated a high
agreement in the annotation part.
Ethical Statement
All annotators are volunteers.
In addition, we
demonstrate the annotator details in Appendix A.3.
Moreover, we will release our Thai local dialect
and human evaluation results, for both the training
and our human evaluation methods, to the public
with the original license of each dataset, such as
XL-SUM (Hasan et al., 2021) and iAPP (Viriyayud-
hakorn and Polpanumas, 2021). In addition, we
have the dataset that was created by hand, and we
will release it with license CC-BY-SA, similar to
previous works.
Acknowledgement
This research is supported by the National Re-
search Foundation, Singapore under its National
Large Language Models Funding Initiative. Any
opinions, findings and conclusions or recommen-
dations expressed in this material are those of the
author(s) and do not reflect the views of National
Research Foundation, Singapore. We also would
like to thank all the annotators in this work for their
volunteer work.
References
Samuel Cahyawijaya, Holy Lovenia, Alham Fikri Aji,
Genta Winata, Bryan Wilie, Fajri Koto, Rahmad
Mahendra, Christian Wibisono, Ade Romadhony,
Karissa Vincentio, Jennifer Santoso, David Moel-
jadi, Cahya Wirawan, Frederikus Hudi, Muham-
mad Satrio Wicaksono, Ivan Parmonangan, Ika Al-
fina, Ilham Firdausi Putra, Samsul Rahmadani, Yu-
lianti Oenang, Ali Septiandri, James Jaya, Kaustubh
Dhole, Arie Suryani, Rifki Afina Putri, Dan Su, Keith
Stevens, Made Nindyatama Nityasya, Muhammad
Adilazuarda, Ryan Hadiwijaya, Ryandito Diandaru,
Tiezheng Yu, Vito Ghifari, Wenliang Dai, Yan Xu,
Dyah Damapuspita, Haryo Wibowo, Cuk Tho, Ich-
wanul Karo Karo, Tirana Fatyanosa, Ziwei Ji, Gra-
ham Neubig, Timothy Baldwin, Sebastian Ruder, Pas-
cale Fung, Herry Sujaini, Sakriani Sakti, and Ayu Pur-
warianti. 2023. NusaCrowd: Open source initiative
for Indonesian NLP resources. In Findings of the As-
sociation for Computational Linguistics: ACL 2023,
pages 13745–13818, Toronto, Canada. Association
for Computational Linguistics.
Samuel Cahyawijaya, Holy Lovenia, Fajri Koto, Rifki
Putri, Wawan Cenggoro, Jhonson Lee, Salsabil Ak-
bar, Emmanuel Dave, Nuurshadieq Nuurshadieq,
Muhammad Mahendra, Rr Putri, Bryan Wilie, Genta
Winata, Alham Aji, Ayu Purwarianti, and Pascale
Fung. 2024. Cendol: Open instruction-tuned genera-
tive large language models for Indonesian languages.
In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1:
Long Papers), pages 14899–14914, Bangkok, Thai-
land. Association for Computational Linguistics.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451, Online. Association for Computational Lin-
guistics.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Lance Calvin Lim Gamboa and Mark Lee. 2025. Fil-
ipino benchmarks for measuring sexist and homo-
phobic bias in multilingual language models from
Southeast Asia. In Proceedings of the First Workshop

--- Page 6 ---

on Language Models for Low-Resource Languages,
pages 123–134, Abu Dhabi, United Arab Emirates.
Association for Computational Linguistics.
Rowena Cristina L. Guevara, Rhandley D. Cajote,
Michael Gringo Angelo R. Bayona, and Crisron
Rudolf G. Lucas. 2024.
Philippine languages
database: A multilingual speech corpora for devel-
oping systems for low-resource languages. In Pro-
ceedings of the 3rd Annual Meeting of the Special
Interest Group on Under-resourced Languages @
LREC-COLING 2024, pages 264–271, Torino, Italia.
ELRA and ICCL.
Tahmid Hasan, Abhik Bhattacharjee, Md. Saiful Is-
lam, Kazi Mubasshir, Yuan-Fang Li, Yong-Bin Kang,
M. Sohel Rahman, and Rifat Shahriyar. 2021. XL-
sum: Large-scale multilingual abstractive summariza-
tion for 44 languages. In Findings of the Association
for Computational Linguistics: ACL-IJCNLP 2021,
pages 4693–4703, Online. Association for Computa-
tional Linguistics.
Dahyun Kim, Sukyung Lee, Yungi Kim, Attapol Ruther-
ford, and Chanjun Park. 2025.
Representing the
under-represented:
Cultural and core capability
benchmarks for developing Thai large language mod-
els. In Proceedings of the 31st International Con-
ference on Computational Linguistics, pages 4114–
4129, Abu Dhabi, UAE. Association for Computa-
tional Linguistics.
Chin-Yew Lin. 2004. ROUGE: A package for auto-
matic evaluation of summaries. In Text Summariza-
tion Branches Out, pages 74–81, Barcelona, Spain.
Association for Computational Linguistics.
Holy Lovenia, Rahmad Mahendra, Salsabil Maulana
Akbar, Lester James Validad Miranda, Jennifer
Santoso, Elyanah Aco, Akhdan Fadhilah, Jonibek
Mansurov, Joseph Marvin Imperial, Onno P. Kamp-
man, Joel Ruben Antony Moniz, Muhammad
Ravi Shulthan Habibi, Frederikus Hudi, Jann Rai-
ley Montalan, Ryan Ignatius Hadiwijaya, Joan-
ito Agili Lopo, William Nixon, Börje F. Karls-
son, James Jaya, Ryandito Diandaru, Yuze Gao,
Patrick Amadeus Irawan, Bin Wang, Jan Chris-
tian Blaise Cruz, Chenxi Whitehouse, Ivan Halim
Parmonangan, Maria Khelli, Wenyu Zhang, Lucky
Susanto, Reynard Adha Ryanda, Sonny Lazuardi Her-
mawan, Dan John Velasco, Muhammad Dehan Al
Kautsar, Willy Fitra Hendria, Yasmin Moslem, Noah
Flynn, Muhammad Farid Adilazuarda, Haochen Li,
Johanes Lee, R. Damanhuri, Shuo Sun, Muham-
mad Reza Qorib, Amirbek Djanibekov, Wei Qi
Leong, Quyet V. Do, Niklas Muennighoff, Tan-
rada Pansuwan, Ilham Firdausi Putra, Yan Xu,
Tai Ngee Chia, Ayu Purwarianti, Sebastian Ruder,
William Chandra Tjhi, Peerat Limkonchotiwat, Al-
ham Fikri Aji, Sedrick Keh, Genta Indra Winata,
Ruochen Zhang, Fajri Koto, Zheng Xin Yong, and
Samuel Cahyawijaya. 2024. SEACrowd: A multi-
lingual multimodal data hub and benchmark suite
for Southeast Asian languages. In Proceedings of
the 2024 Conference on Empirical Methods in Natu-
ral Language Processing, pages 5155–5203, Miami,
Florida, USA. Association for Computational Lin-
guistics.
Jann Railey Montalan, Jian Gang Ngui, Wei Qi Leong,
Yosephine Susanto, Hamsawardhini Rengarajan, Al-
ham Fikri Aji, and William Chandra Tjhi. 2024.
Kalahi: A handcrafted, grassroots cultural llm evalu-
ation suite for filipino. Preprint, arXiv:2409.15380.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic evalu-
ation of machine translation. In Proceedings of the
40th Annual Meeting of the Association for Compu-
tational Linguistics, pages 311–318, Philadelphia,
Pennsylvania, USA. Association for Computational
Linguistics.
Parinthapat Pengpun, Can Udomcharoenchaikit, Weer-
ayut Buaphet, and Peerat Limkonchotiwat. 2024.
Seed-free synthetic data generation framework for
instruction-tuning llms: A case study in thai. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics, ACL 2024 -
Student Research Workshop, Bangkok, Thailand, Au-
gust 11-16, 2024, pages 438–457. Association for
Computational Linguistics.
Wannaphong Phatthiyaphaibun, Surapon Nonesung,
Peerat Limkonchotiwat, Can Udomcharoenchaikit,
Jitkapat Sawatphol, Ekapol Chuangsuwanich, and
Sarana Nutanong. 2024. CHIE: Generative MRC
evaluation for in-context QA with correctness, help-
fulness, irrelevancy, and extraneousness aspects. In
Proceedings of the 2nd GenBench Workshop on Gen-
eralisation (Benchmarking) in NLP, pages 154–164,
Miami, Florida, USA. Association for Computational
Linguistics.
Kunat Pipatanakul, Phatrasek Jirabovonvisut, Potsawee
Manakul, Sittipong Sripaisarnmongkol, Ruangsak
Patomwong, Pathomporn Chokchainant, and Kasima
Tharnpipitchai. 2023. Typhoon: Thai large language
models. Preprint, arXiv:2312.13951.
Yiwei Qin, Kaiqiang Song, Yebowen Hu, Wenlin Yao,
Sangwoo Cho, Xiaoyang Wang, Xuansheng Wu, Fei
Liu, Pengfei Liu, and Dong Yu. 2024. InFoBench:
Evaluating instruction following ability in large lan-
guage models. In Findings of the Association for
Computational Linguistics: ACL 2024, pages 13025–
13048, Bangkok, Thailand. Association for Compu-
tational Linguistics.
Tengku Syarfina, Satwiko Budiono, and Denny Adrian
Nurhuda. 2022. Language variations in jayapura city:
A study of dialectology. EAI.
Dastin Tabajunda. 2018.
Linguistic schoolscape as
public communication: A study of announcements
and signages in de la salle university – dasmariñas.
In Proceedings of the 32nd Pacific Asia Conference
on Language, Information and Computation, Hong
Kong. Association for Computational Linguistics.

--- Page 7 ---

Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard
Grave, and Guillaume Lample. 2023. Llama: Open
and efficient foundation language models. Preprint,
arXiv:2302.13971.
Tajudin Nur Veria Septianingtias, Wahya and Farida
Ariyani. 2024.
Lexical variation in the lampung
language, indonesia.
Cogent Arts & Humanities,
11(1):2309740.
Kobkrit Viriyayudhakorn and Charin Polpanumas. 2021.
iapp_wiki_qa_squad.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang,
Joseph E. Gonzalez, and Ion Stoica. 2023. Judging
LLM-as-a-judge with MT-bench and chatbot arena.
In Thirty-seventh Conference on Neural Information
Processing Systems Datasets and Benchmarks Track.
A
Data Statistics and Annotators
A.1
Data Statistics
As shown in Table 4, we have a total of 100 samples
for each local dialect. We use summarization, QA,
and translation for the traditional metric, BLEU,
and ROUGE-L. In contrast, we use conversation
and food topics for human evaluation since these
topics do not have the perfect answer, as in pre-
vious tasks. In addition, the topics of food and
conversation are culturally relevant, such as local
food in Southern or Northern Thailand, and the
conversation topic is events and culture in each
part of Thailand. In addition, we have 40 sam-
ples for translation since it is forward and back-
ward translation. Moreover, the QA samples are
from iAPP
(Viriyayudhakorn and Polpanumas,
2021), the summarization samples are from XL-
SUM (Hasan et al., 2021), and the translation, food,
and conversation samples are formulated by anno-
tators.
Dialects
#Sample of
Summarization
#Sample
of QA
#Sample
of Transaltion
#Sample
of Conversation
#Sample
of Food
Isan
20
20
40
10
10
Lanna
20
20
40
10
10
Dambro
20
20
40
10
10
Table 4: Data Statistical: Number of Samples
A.2
Word Overlap
As shown in Table 5, we observe that the transla-
tion had the least overlap compared to other tasks.
This conforms with the results in Table 1 that the
least word overlap yields the lowest penalty, di-
rectly affecting the downstream task performance.
However, the word-overlap score still cannot ex-
plain the fluency performance of LLMs in speaking
Thai local dialects.
Dialects Summarization
QA
Translation
Isan
0.9628
0.9167
0.9067
Lanna
0.9767
0.93318
0.9072
Dambro
0.9598
0.9008
0.9036
Table 5: Data Statistical: Word Overlap
A.3
Annotators
We list the author’s biographic as follows. For
Lanna, we have two women and three men, and an-
notators are between 25 and 30 years old. For Isan,
we have three women and two men; the annotators
are between 25 and 30 years old and 31 and 35
years old. For Dambro, we have three women and
two men, and annotators are between 25 and 30
years old. All annotators are born in non-Central
Thailand and speak local and Central dialects.
A.4
Annotator Agreement
In this study, we calculate the annotator agreement
of our proposed metric using Cohen’s Kappa score.
We use two annotators in this experiment, and both
of them need to annotate the same sample (100%
sample overlap). As shown in Table 6, we found
that Isan and Dambro have a similar agreement
score, 0.7 points, with a substantial agreement.
Moreover, we found almost perfect agreement on
Lanna. This is because the model can speak Lanna
better than other dialects. When the annotators
assign the score, it is easier for them to judge it.
Agreement
Lanna
Isan
Dambro
Generation Fluency Generation Fluency Generation Fluency
Cohen_kappa
0.9315
0.7319
0.7078
0.7077
0.7514
0.7951
Table 6: Data Statistical: Annotator agreement of our
proposed metric.
A.5
Example Code
Since we use all the generation setup from Lovenia
et al. (2024), we can run all the experiments with
one line code, similar to SEACrowd. For example:
1 #!/bin/bash
2 MODEL_NAME=’meta -llama/Llama -3.1 -8B-
Instruct ’
3 python evaluation/
main_local_prompt_batch.py south ${
MODEL_NAME} 0 1
4 python evaluation/
main_local_prompt_batch.py north ${
MODEL_NAME} 0 1
Listing 1: Example Code

--- Page 8 ---

In addition, the output will be in the CSV format,
including scores according to tasks. The bench-
mark can be run on a single A100 or H100 (800
GB) within < 1 hour.
A.6
Guideline for Annotators
Translation. From Section 3.2, we translate from
Central Thai to Thai local dialects using the follow-
ing guideline:
Translation Task
In this task, we need your help to revise
the translation of the prompt and its re-
sponse from English to your native lan-
guage.
Comparing Original and translated texts
and then editing the translation to be
more human (write your revision in the
edit column)
The goal is to make the translation results
look more like human writing
Note that the edit columns can’t be null.
You need to edit all the translations.
Do not remove or edit emojis, hashtags,
or special characters If the text represents
gender (she/he), please change it to the
general context (I, you, they, them)
All texts should be edited since it is not
100% natural. There is no empty field in
the revision column.
Model Comparison Guideline. From Section 3.3,
we ask three annotators to compare model A vs. B
where we mean the answer to get the final answer
of each sample. Annotators are blinded to model
identities for all examples. In addition, we aver-
age the answer from three annotators into the final
answer.
Guidelines for Evaluating Model A and
Model B
Evaluation Objective: Assess the perfor-
mance of Model A compared to Model
B in responding to provided questions/in-
structions/prompts.
Evaluate based on the following two as-
pects: 1. Accuracy of local dialect/lan-
guage usage 2. Accuracy of the response
Evaluation Options: You must choose
only one option for each criterion:
(i) A is better than B: Model A performs
better than Model B in the given aspect
(ii) B is better than A: Model B performs
better than Model A in the given aspect
(iii) A and B are equally good: Both mod-
els perform equally well in the given as-
pect
(iv) A and B are equally poor: Both mod-
els perform equally poorly in the given
aspect
Evaluation Justification: Provide a short
reason explaining why you chose that
score (repeating reasons is allowed if the
outputs are similar).
A.7
Food and Conversation Topics
We provide the full food and conversation topics in
Figure 2.
A.8
Prompts
We demonstrate the prompt we used in our experi-
ment in Figure 3. Note that all prompts are written
in local dialects, and we also added instructions for
performing in local dialects.
B
LLM-as-a-judge
We acknowledge that the limitation of our proposed
metric is relying on human 100%. We use native
speakers to judge the fluency and generation score
for LLMs’ output. However, we tried to use LLM-
as-a-judge to solve this problem and found that
LLMs (i.e., Gemini2 and GPT4o) are not good
enough to understand Thai local dialects fluency,
resulting in inaccurate judgment compared to na-
tive speakers. Although Gemini2 achieves a high
score in Table 3, when it acts like a judge, it fails
to give a similar fluency score to the human, where
the preliminary results show that the correlation
between Geimini2 and Humans on Lanna is only
53.6 points (Spearman’s correlation). Therefore,
we omit the LLM-as-a-judge from our work.
C
Output Examples
In this study, we show the incorrect and correct
examples when we focus on the local dialect out-
put. We divided it into two categories: (i) answer
correctly with no local dialects, and (ii) answer
correctly with local dialects to make it easier to
understand local Thai dialects. Note that we use
the output from Typhoon1.5-70b and Gemini2.

--- Page 9 ---

Food
Conversation
Isan
Lanna
Dambro
แจ่วบักเขือ
ลาบเหนือ
แก๋งพุงปลา
ประเพณีท้องถิ่น
อ่อมน้องวัว
ขนมจีนน้ำเงี้ยว
แกงส้ม
อาชีพ
ตำบักหุ่ง
แกงฮังเล
ลอกอผัดไข่
การคมนาคม
หมกหน่อไม้
น้ำพริกหนุ่ม
ข้าวผั๊ดเคย
ครอบครัว
ซอยจุ๊
น้ำพริกอ่อง
แกงส้มปล๊าพงยอดพร๊าว
กลับบ้านช่วงเทศกาล
แกงขี้เหล็ก
แกงหัวปลี
ข้าวผั๊ดเคย
การเมืองท้องถิ่น
น้ำตกคอหมูย่าง
แกงหยวก
ปล่าซายท๋อดขี้มิ้น
สภาพอากาศ
ปลาส้ม
ไส้อั๋ว
ผั๊ดผั๊กเหลี๊ยง
อาหารท้องถิ่น
แจ่วฮ้อน
แคบหมู
แก๋งเลียง
เครื่องแต่งกายท้องถิ่น
ตับหวาน
แกงกระด้าง
ผั๊ดหลูกต๋อ
การศึกษาท้องถิ่น
Figure 2: Food and Conversation topics. Note that these food names are very local in each part of Thailand.
Dialect
Summarization
Translation
QA
Food
Conversation
Central
จงสรุปข้อความด้านล่าง\n
ข้อความ: [INPUT]\nสรุป:
แปลข้อความต่อไปนี้จาก [SOURCE] เป็น [TARGET]
ให้คุณแปลโดยตรงโดยไม่ต้องมีข้อมูลเพิ่มเติมใดๆ\n
ข้อความ: [INPUT]\nคำแปล:
โปรดอ้างอิงถึงข้อความด้านล่างนี้และตอบคำถามต่อไปนี้
ให้ตอบโดยใช้แค่ข้อความที่อยู่ในบทความ:\n
ข้อความ: [CONTEXT]\nคำถาม: [QUESTION]\nคำตอบ:
จงเขียนวิธีทำ [INPUT]
จงสร้างบทสนทนาของคนภาคกลาง
โดยพูดคุยเกี่ยวกับ [INPUT] บทสนทนาไม่ควรเกิน 5 turns
Isan
หื้อสรุปข้อความตางล่างหือเป็นภาษาเหนือ\n
ข้อความ: [INPUT]\nสรุป:
แปลข้อความต่อไปนี้จาก [SOURCE] เป๋น [TARGET]
หื้อตั๋วแปลโดยตรงโดยตี้บะต้องมีข้อมูลเพิ่มเติมใดๆ\n
ข้อความ: [INPUT]\nคำแปล:
โปรดอ้างอิงถึงข้อความตางล่างนี้และตอบคำถามต่อไปนี้หื้อเป็นภาษาเหนือ
หื้อตอบโดยใช้ก่าข้อความตี้อยู่ในบทความ:\n
ข้อความ: [CONTEXT]\nคำถาม: [QUESTION]\nคำตอบ:
หื้อเขียนวิธียะ [INPUT]
หื้อเป๋นภาษาเหนือ
หื้อเขียนกำอู้ของคนเหนือ
โดยอู้เกี่ยวกับ [INPUT] บทสนทนาบะควรเกิน 5 turns
North
จงสรุปข้อความทางลุ่ม\n
ข้อความ: [INPUT]\nสรุป:
แปลข้อความต่อไปนี้จาก [SOURCE] เป็น [TARGET]
ให้เจ้าแปลโดยตรงโดยบ่ต้องมีข้อมูลเพิ่มเติมใดๆ\n
ข้อความ: [INPUT]\nคำแปล:
โปรดอ้างอิงถึงข้อความทางลุมพี้และตอบคำถามต่อไปนี้เป็นภาษาอีสาน
ให้ตอบโดยใช้แค่ข้อความที่อยู่ในบทความ:\n
ข้อความ:[CONTEXT]:\nคำถาม: [QUESTION]\nคำตอบ:
จงเขียนวิธีเฮ็ด [INPUT]
จงเขียนบทเว่าของคนภาคอีสาน
โดยเว่าเกี่ยวกับ [INPUT] บทสนทนาบ่ควรเกิน 5 turns
South
ให้สรุปข้อความข้างล่างเป็นภาษาใต้\n
ข้อความ:[INPUT]\nสรุปว่า:
แปลข้อความต่อจากนี้ [SOURCE] เป็น [TARGET]
ให้การแปลของเติ้ลแปลตรงตัวเลย
ไม่ต้องไสข้อมูลเพิ่มเติมไหร\nข้อความ: [INPUT]\nคำแปล:
ช่วยใช้ข้อความข้างล่างนี้ตอบคำถามเป็นภาษาใต้
โดยตอบแค่คำตอบที่มีอยู๋ในบทความ:\n
ข้อความ: [CONTEXT]\nคำถาม: [QUESTION]\nคำตอบ:
ให้เขียนวิธีทำ [INPUT] เป็นภาษาใต้
ให้เขียนบทพูดของคนใต้
โดยแหลงเกี่ยวกับ [INPUT] บทพูดไม่ควรเกิน 5 ตา
Dialect
Summarization
Translation
QA
Food
Conversation
Central
Please summarize the follow text\n
Text: [INPUT]\nSummay:
Translate this text from [SOURCE] to [TARGET]
Please translate it without any additional information\n
ข้อความ: [INPUT]\nคำแปล:
Please reference to the provide context and answer the question
Please answer only the sentence that appear in the context:\n
Context: [CONTEXT]\nQuestion: [QUESTION]\nAnswer:
How to make a food [INPUT]
Please create the conversation
Where the conversation topic is [INPUT] the conversation should not exceed 5 turns
Thai version
English version
Figure 3: The Thai prompts that we used in our experiments with the translation version.
แปลข้อความต่อจากนี้ ภาษาอังกฤษ เป็น ภาษาใต้ ให้การแปลของเติ้ลแปลตรงตัวเลย ไม่ต้องไส
ข้อมูลเพิ่มเติมไหร
ข้อความ: I woke up very early today to go watch the buffalo race. 
The weather was so hot that when I got back home, I had to take a rest because I had a headache.
คำแปล:
ผมถูกตื่นเช้ามากวันนี้เพื่อไปดูการแข่งควาย 
อากาศร้อนมากจนเมื่อผมกลับบ้าน ผมต้องพักเพราะผมมีหัวใจ
The translation is almost correct. 
However, there is no local dialects at all in the response
เอ้อ ตื่นแต่เช้าเหอวันนี้ หวังไปแหลงควายชน 
อากาศร้อนฉิบหาย พอเห้อกลับถึงบ้าน ต้องแหลงพัก 
เพราะว่าปวดหัวเติบเลย
Instruction
Typhoon1.5
Comment
Annotators
prefer
แปลข้อความต่อจากนี้ ภาษาอังกฤษ เป็น ภาษาใต้ ให้การแปลของเติ้ลแปลตรงตัวเลย ไม่ต้องไส
ข้อมูลเพิ่มเติมไหร
ข้อความ: Why do I have to do this work again? I’ve revised it so many times, but it’s never
finished. The person who keeps asking for revisions doesn’t even know what they’re doing. I’m so
exhausted.
คำแปล:
ทำไมฉันต้องทำงานนี้อีก? ฉันแก้ไขมันหลายครั้งแล้ว 
แต่มันไม่เคยเสร็จสิ้น คนที่ขอให้แก้ไขไม่รู้ว่าเขาทำอะไร ฉันเหนื่อยมาก
The translation is almost correct. 
However, there is no local dialects at all in the response
เอ้อ เหอ ไซร กูต้องมาทำไหม่ตะงานนี้หวา? 
กูแก้มาตั้งหลายรอบแล้วเห้อ มันก็ไม่แล้วสักที 
ไอ้คนสั่งแก้ก็ไม่รู้เรื่องอีท่าไหน กูเหนื่อยฉิบหายเลยหว่ะ.
แปลข้อความต่อไปนี้จาก ภาษาอังกฤษ เป๋น ภาษาเหนือ หื้อตั๋วแปลโดยตรงโดยตี้บะต้องมีข้อมูลเพิ่ม
เติมใดๆ
ข้อความ: I never knew before that Beer was so good at rock climbing. It’s impressive, and I’ll use
him as an example of discipline and consistency in exercise.
คำแปล:
ผมไม่เคยรู้มาก่อนว่าเบียร์เก่งในการปีนเขาขนาดนี้ 
มันน่าประทับใจ และผมจะใช้เขาเป็นตัวอย่างของความมีวินัย
และความสม่ำเสมอในการออกกำลังกาย
The translation is almost correct. 
However, there is no local dialects at all in the response
เมื่อก่อนบ่เกยฮู้เลยว่าเบียร์เก่งปีนผาขนาดนี้ 
น่าทึ่งแต้ๆ แล้วจะเอาเปิ้นไปเป็นตัวอย่างเรื่องมีวินัย
และสม่ำเสมอในการออกกำลังกาย
แปลข้อความต่อไปนี้จาก ภาษาอังกฤษ เป๋น ภาษาเหนือ หื้อตั๋วแปลโดยตรงโดยตี้บะต้องมีข้อมูลเพิ่ม
เติมใดๆ
ข้อความ: On rainy days, you have to take an umbrella, but today, Gam forgot hers. So, she stayed
home and relaxed.
คำแปล:
ในวันฝนตก, สูต้องเอาจ้อง (ร่ม), แต่ว่าวันนี้, 
แก๋มลืมของสู. ดังนั้น, สูเลยอยู่บ้านแล้วก็พักผ่อน.
The translation is almost correct with local dialects.
-
แปลข้อความต่อไปนี้จาก ภาษาอังกฤษ เป๋น ภาษาเหนือ หื้อตั๋วแปลโดยตรงโดยตี้บะต้องมีข้อมูลเพิ่ม
เติมใดๆ
ข้อความ: People who like to tease others are no-good. If you want to be a good person, don’t tease
others. But Korn often gets teased, which makes him shout, "What the heck is your problem?"
คำแปล:
คนตี้ชอบล้อเลียนคนอื่น บะดี ถ้าอยากเป๋นคนดี 
อย่าล้อเลียนคนอื่น แต่ก่อนมักจะโดนล้อเลียน 
ทำให้เปิ้นฮ้องว่า "อะหยังนักหนาของสู?"
The translation is almost correct with local dialects.
-
Figure 4: Example from the translation task.
As shown in Figure 4, we notice that while Ty-
phoon can translate the text correctly, there are no
local dialects in this case. In contrast, Gemini2
(anotator prefer) can translate from English to local
dialect correctly. Moreover, we also observe Fig-
ure that both models code-switch between Central
and local dialects, as underscored in Figure 1. This
suggests that the gap in making LLMs speak Thai

--- Page 10 ---

local dialects is significantly broad and needs more
attention.

```
