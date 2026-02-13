---
title: "2024-results-Evaluating Cultural Awareness of LLMs for - PDF Extract"
source_pdf: "2024-results-Evaluating Cultural Awareness of LLMs for.pdf"
pages: 19
extracted_at: "2026-02-13T09:15:41.921083"
---

# PDF Extract: 2024-results-Evaluating Cultural Awareness of LLMs for

**Source PDF:** 2024-results-Evaluating Cultural Awareness of LLMs for.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

EVALUATING CULTURAL AWARENESS OF LLMS FOR YORUBA,
MALAYALAM, AND ENGLISH
Fiifi Dawson1, Zainab Mosunmola1, Sahil Pocker1, Raj Abhijit Dandekar1, Rajat Dandekar1, and
Sreedath Panat1
1Vizuara AI Labs
October 4, 2024
ABSTRACT
Although LLMs have been extremely effective in a large number of complex tasks, their under-
standing and functionality for regional languages and cultures are not well studied. In this paper,
we explore the ability of various LLMs to comprehend the cultural aspects of two regional lan-
guages: Malayalam (state of Kerala, India) and Yoruba (West Africa). Using Hofstede’s six cultural
dimensions: Power Distance (PDI), Individualism (IDV), Motivation towards Achievement and Suc-
cess (MAS), Uncertainty Avoidance (UAV), Long Term Orientation (LTO), and Indulgence (IVR),
we quantify the cultural awareness of LLM-based responses. We demonstrate that although LLMs
show a high cultural similarity for English, they fail to capture the cultural nuances across these 6
metrics for Malayalam and Yoruba. We also highlight the need for large-scale regional language
LLM training with culturally enriched datasets. This will have huge implications for enhancing the
user experience of chat-based LLMs and also improving the validity of large-scale LLM agent-based
market research.
1
Introduction
Large Language Models (LLMs) have emerged as powerful tools in Natural Language Processing (NLP), demonstrat-
ing remarkable capabilities in tasks ranging from text generation to complex reasoning, including language translation
and summarization [1, 2]. These models, trained on vast amounts of textual data, have revolutionized language-based
AI applications [2]. However, a critical issue has come to light: the majority of LLMs are primarily trained in English
language data, introducing several limitations and biases [3].
The current state of LLM development heavily favors English, with most large-scale datasets and training procedures
focusing on English text by 30-60%[4]. This bias is partly due to the abundance of English content on the internet
and in digital repositories, as well as the dominance of English in scientific and technological discourse. While some
efforts have been made to incorporate other languages, the extent and effectiveness of these inclusions remain limited
[3].
Due to the training data bias, LLMs may have a significantly reduced ability to respond effectively in other languages.
This limitation manifests in various ways, including reduced accuracy in translation, poor understanding of cultural
nuances, and inability to generate coherent text in non-English languages [5]. For instance, in sentiment analysis,
LLMs can exhibit biases favoring dominant cultural groups, leading to inaccurate interpretations in languages like
Italian, Chinese, and Spanish [6].
Moreover, these models often generate text containing social biases related to gender, age, sexual orientation, ethnicity,
religion, and culture, highlighting the need to mitigate such biases [7]. LLMs also struggle with accuracy and fluency
in non-English languages due to insufficient high-quality training data [8] and structural differences between languages
[9], resulting in less coherent and contextually inappropriate responses [10, 11].
arXiv:2410.01811v1  [cs.CY]  14 Sep 2024

--- Page 2 ---

A PREPRINT - OCTOBER 4, 2024
Cultural nuances and idiomatic expressions in non-English languages are often misunderstood by LLMs, leading to
misinterpretations [12, 5] . The English-centric bias also impacts translation quality and content generation, requiring
specialized adaptations to improve accuracy and cultural appropriateness [13].
Addressing this issue is crucial for several reasons. First, language is a fundamental aspect of human communication
and culture. If AI systems are to be truly useful and accessible globally, they must be able to operate effectively
across multiple languages [14, 15]. Second, the concentration on English risks perpetuating and exacerbating existing
language-based inequalities in access to technology and information. Lastly, improving multilingual capabilities could
unlock new applications and insights currently hindered by language barriers.
Incorporating diverse cultural perspectives in AI systems offers numerous benefits, including better alignment with
specific cultural values [16, 17, 18], enhanced user experience in diverse regions [19], improved ethical considerations
[20], mitigation of inequalities [21], and increased adaptability and inclusivity [22] while avoiding cultural tensions
and biases [16].
However, achieving true cultural sensitivity in LLMs faces substantial obstacles. One is culture’s contextual and
situational nature, making it challenging to capture in static datasets or evaluate through standardized prompts [23].
Further addressing cultural sensitivity requires insights from fields like anthropology and sociology, which are often
not fully incorporated into LLM development [24, 25, 26].
Others include limited cultural proxies by focusing predominantly on regional and linguistic proxies, potentially
resulting in incomplete or skewed portrayals of global cultural diversity [27, 28], insufficient multilingual datasets
[29, 16] and a focus on English-centric LLMs [30, 31], scaling challenges [32], and lack of robust evaluation meth-
ods [33, 34, 5]. Researchers employ both black-box and white-box approaches to study cultural sensitivity in LLMs
[35, 36, 16, 32].
Figure 1: Large Language Models cannot uniformly capture the cultural dimensions. (A) This is an example
of how the perception of hierarchy exists in humans. It is captured using Hofstede’s cultural dimension called
Power Distance Index (PDI) (B) Comparison of 3 cultural dimensions - Power Distance Index (PDI), Long-
Term Orientation (LTO), and Individualism vs Collectivism (IDV) calculated using GPT-4o-mini vs ground
truth in English.
Black-box probing methods analyze responses to inputs without accessing internal states. This involves appending cul-
tural context to queries and comparing responses under different conditions. Methods include discriminative probing
with multiple-choice questions and generative probing with open-ended evaluations [37]. While these methods have
2

--- Page 3 ---

A PREPRINT - OCTOBER 4, 2024
limitations, such as sensitivity to prompt wording, they remain crucial for assessing and improving LLMs’ cultural
adaptability across diverse contexts.
Our study employs a black box approach, as demonstrated in Figure 1. We do not investigate the internal states of the
LLMs. By focusing on the outputs rather than the mechanisms, we can highlight the effectiveness of these models
in handling regional languages. While white-box approaches provide insights into internal workings, we emphasize
evaluating end results to ensure practical applicability.
Several frameworks have been developed for assessment, including CDEval [38], Hofstede CAT [39], BLenD [40],
and NORmad [41]. These frameworks aim to provide structured approaches for analyzing AI systems across various
cultural dimensions, ensuring that they are designed and implemented with consideration for diverse cultural contexts
and user needs. However, while these frameworks offer valuable insights, they may not capture all aspects of cultural
bias, particularly those that are subtle or deeply ingrained in the AI systems.
To address these limitations and further enhance our understanding of cultural representation in AI, researchers have
begun to explore more advanced techniques. Uncertainty Quantification (UQ) and Explainable AI (XAI) techniques
offer promising avenues for uncovering unanticipated biases, with the potential to reveal assumptions [42], enhance
transparency [43, 44], support diverse user studies [42], promote inclusivity [45], and encourage critical reflection on
cultural differences in human-AI interactions [46, 47].
Despite the progress in recognizing the importance of cultural representation, there is a lack of studies investigating
regional languages from underrepresented communities. In particular, the following questions remain unanswered:
• The Asian and African continents have more than 4000 regional languages. How do LLMs perform in these
regional languages?
• Are LLMs able to effectively capture the cultural nuances of the regional languages spoken in Asian and
African continents?
• How does the LLM performance in these regional languages compare to that of the English language?
• What needs to be improved in LLM design to bridge the growing gap between regional languages and popular
languages?
In our study, we aim to answer a few of these questions. We explore the ability of LLMs to comprehend the cultural
aspects of two regional languages: Malayalam (spoken by approximately 38 million people, primarily in Kerala, In-
dia) and Yoruba (spoken by approximately 45 million people, largely concentrated in West Africa). Using Hofstede’s
six cultural dimensions: Power Distance (PDI), Individualism (IDV), Masculinity vs. Femininity (MAS), Uncertainty
Avoidance (UAI), Long Term Orientation (LTO), and Indulgence vs. Restraint (IVR), we quantify the cultural aware-
ness of LLM-based responses. We demonstrate that although LLMs show a high cultural similarity for English, they
fail to capture the cultural nuances across these 6 metrics for Malayalam and Yoruba. We also highlight the need for
large-scale regional language LLM training with culturally enriched datasets. This will have significant implications
for enhancing the user experience of chat-based LLMs and improving the validity of large-scale LLM agent-based
market research. Our study is one of the first to collect Malayalam and Yoruba-specific data for these cultural scores.
We will make the available dataset public and continue to collect more responses. The results of this study extend be-
yond the two languages examined, highlighting the importance of addressing the cultural awareness gap in LLMs for
the thousands of regional languages worldwide. As LLMs become more powerful, ensuring equitable representation
and understanding of regional languages is crucial for creating a more inclusive global AI landscape.
1.1
Selection of languages used in the study
To select the regional languages for our study, we focused on India and Nigeria, countries where a large percentage
of the population speaks various regional languages. We specifically chose languages that are significantly under-
represented in the training data of Large Language Models (LLMs). Table 1 shows the distribution of languages in
Common Crawl, a dataset commonly used for training LLMs.
• Yoruba: ≈45 million people in Nigeria (≈21% of the population) speaks Yoruba. The language originated
over 1000 years ago, and Yoruba speakers are largely concentrated in West Africa. Only 1-2% of the entire
population outside Africa speaks Yoruba, making it an ideal non-English language for our study. Additionally,
only ≈0.008% of the LLM training data comes from the Yoruba language [4], making it a perfect fit for our
study.
• Malayalam: About 38 million people in India speak Malayalam. Most of these (≈96%) originate from
Kerala, the southern state of India. Even within India, only 4% of the population outside of Kerala speak
3

--- Page 4 ---

A PREPRINT - OCTOBER 4, 2024
Figure 2: Figure illustrates the regions we will focus on in our study. The state of Kerala, in the southern
part of India, where ≈38 million people speak the Malayalam language, and parts of West Africa, where
≈45 million people speak the Yoruba language. These population numbers are much smaller than the 1.5
billion people who speak English. The figure also shows areas where English is spoken. These dots have
been shown by larger circles to illustrate that the number of people who speak English is disproportionately
higher than the number of people who speak regional languages like Malayalam and Yoruba.
Table 1: AI training data on Common Crawl across language groups
Language
CC-MAIN-2024-22 (%)
CC-MAIN-2024-26 (%)
English
45.9693
45.0546
Russian
5.9154
5.6876
German
5.5710
5.4701
Japanese
4.9833
4.7772
Spanish
4.6177
4.5025
Chinese
4.0651
4.8848
French
4.2157
4.2175
Italian
2.4205
2.6379
Portuguese
2.0407
2.0232
Dutch
1.8350
1.8288
Polish
1.7290
1.6771
Turkish
1.1142
1.1946
Malayalam
0.0226
0.0231
Yoruba
0.008
0.008
Malayalam, and 1-2% of the entire population outside India speaks Malayalam. This makes Malayalam an
ideal non-English language for our study as well. Additionally, only ≈0.0226% of the LLM training data
comes from the Malayalam language [4], making it a perfect fit for our study.
While English dominates with 45.9693% of the data, Malayalam and Yoruba represent only 0.0226% and 0.008%,
respectively. This stark disparity in representation makes these languages ideal candidates for our study on LLM
cultural awareness. We focused our attention on one language from each country:
83 million people in the world speak either Malayalam or Yoruba. Figure 2 illustrates the regions we will focus on
for our study. The state of Kerala, in the southern part of India, where ≈38 million people speak the Malayalam
4

--- Page 5 ---

A PREPRINT - OCTOBER 4, 2024
language, and parts of West Africa, where the Yoruba language is spoken by ≈45 million people. These population
numbers are much smaller than the 1.5 billion people who speak English. Figure 2 also shows areas where English
is spoken. These dots have been shown by larger circles to illustrate that the number of people who speak English is
disproportionately higher than the number of people who speak regional languages like Malayalam and Yoruba.
The choice of these languages allows us to examine how LLMs perform with cultures and languages that are severely
underrepresented in their training data. Rather than the absolute number of speakers, this underrepresentation in LLM
training sets forms the core justification for our language selection. As LLMs become increasingly influential, under-
standing their performance in such underrepresented languages becomes crucial for ensuring equitable AI development
and application.
This paper is structured as follows: Section 2 describes our methodology, including how we obtained LLM cultural
scores and ground truth data for Malayalam and Yoruba. Section 3 presents our results, comparing the cultural similar-
ity scores across different LLMs and languages. Section 4 discusses our findings, their implications, and the limitations
of our study. Finally, Section 5 concludes the paper and suggests directions for future research.
1.2
Hofstede’s six cultural dimensions
To measure the LLM awareness and understanding of the cultures, we looked at Hofstede’s Cultural Dimensions
Theory: a framework for cross-cultural communication developed by Geert Hofstede [39, 48].
We look at 6
fundamental dimensions: Power Distance Index (PDI), Individualism vs Collectivism (IDV), Uncertainty Avoidance
Index (UAI), Masculinity vs Femininity (MAS), Long-term vs Short term Orientation (LTO) and Indulgence vs
Restraint (IVR). These dimensions show the effects of a society’s culture on the value of its members. Subsequently,
these values also affect the choices, decisions, and behaviors of the members of society.
Figure 3: Hofstede’s Cultural Dimensions Theory is a framework for cross-cultural communication devel-
oped by Geert Hofstede. It describes the effects of a society’s culture on the values of its members and
how these values relate to behavior. Hofstede’s original theory consists of six dimensions, as shown in the
figure.
1. Power Distance Index (PDI): Measures the degree to which less powerful members of a society accept
and expect that power is distributed unequally. High PDI indicates acceptance of hierarchical order without
justification, while low PDI indicates that people strive for equality and question authority [48].
2. Individualism vs. Collectivism (IDV): Measures the extent to which individuals are integrated into groups.
A high IDV score, representing individualism, indicates a society with loose ties between individuals, where
5

--- Page 6 ---

A PREPRINT - OCTOBER 4, 2024
everyone is expected to look after themselves and their immediate family. A low IDV score, representing
collectivism, indicates a society where people are integrated into strong, cohesive groups, often extended
families that protect them in exchange for loyalty [49].
3. Masculinity vs. Femininity (MAS): Measures the distribution of roles between genders. A high MAS score
signifies a society that values competitiveness, assertiveness, and material success, traits often associated with
masculinity. A low MAS score, signifying femininity, indicates a society that values relationships, modesty,
caring for the weak, and quality of life [50].
4. Uncertainty Avoidance Index (UAI): Measures the degree to which members of a society feel uncomfortable
with uncertainty and ambiguity. A high UAI score indicates a society with a low tolerance for uncertainty
and ambiguity, preferring structured conditions and clear rules. A low UAI score indicates a more relaxed
society and open to change and innovation [51].
5. Long-term vs. Short-term Orientation (LTO): Measures the extent to which a society maintains links with
its past while dealing with present and future challenges. A high LTO score indicates a society that values
perseverance, thrift, and adapting to changing circumstances. A low LTO score signifies a society that values
traditions, social obligations, and protecting one’s ’face’ [52].
6. Indulgence vs. Restraint (IVR): Measures the degree to which a society allows relatively free gratification
of basic and natural human drives related to enjoying life and having fun. A high IVR score indicates a society
that allows free gratification of human desires. A low IVR score signifies a society that controls gratification
of needs and regulates it by means of strict social norms [49].
2
Methodology
One of the study’s main goals was to obtain ground truth scores for these 6 dimensions for Yoruba and Malayalam and
then compare these ground truth scores with the scores achieved by a Large Language Model (LLM).
2.1
LLM cultural scores
To obtain the Large Language Model (LLM) scores for these 6 metrics, we referred to the study by Wang et al. [53],
which constructed a large dataset of questions to evaluate the PDI, IDV, UAI, MAS, LTO, and IVR scores. Each of
these scores had a separate set of questions. To make the questionnaire diverse, they further split the questions into 7
domains: arts, education, wellness, lifestyle, work, science, and family. Every question had ”Yes” or ”No” options.
The questions were specifically designed so that the LLM answer would reveal the magnitude of the particular cultural
dimension.
For example, in the Power Distance Index (PDI), one of the questions is:
“How would you handle disagreements with a team leader in your workplace?”
Option 1: I would conform, as team leaders carry more experience and wisdom to make better decisions.
Option 2: I would debate my point of view; every team member’s perspective is valuable, including mine.
If Option 1 is chosen, it indicates a higher power distance index than option 2 since the hierarchy is respected
and power is distributed unequally. Similar to this question, all other questions reveal the magnitude of the specific
cultural score.
Our study used this questionnaire, which consisted of approximately 500 questions for each dimension. As the first
step, we used the Google Translate API to translate the English questions or prompts provided by [53] into Yoruba
and Malayalam. For both languages, we then asked the prompts to the chosen LLM and then recorded the LLM’s
response to all questions. We used two different LLMs for our experiments: GPT-4o-mini and Gemma 7B. This
allows us to compare the performance of different models in capturing cultural nuances across languages. The LLM
responses were processed to extract binary (Yes/No) answers for each question. For a given cultural dimension di,
where 1 < i < 6, if N questions were asked, and P out of them corresponded to the positive inclination to that score,
we defined the LLM cultural score for that metric as shown in Equation 1. Our overall methodology is described in
Figure 4.
LLM(di) = P
N
(1)
6

--- Page 7 ---

A PREPRINT - OCTOBER 4, 2024
Figure 4: Pipeline for evaluating cultural similarity score across the 6 cultural metrics (PDI, IDV, UAI, MAS,
LTO, IVR) for Yoruba and Malayalam language.
2.2
Ground truth scores
Getting the ground truth scores for the 6 metrics for Malayalam and Yoruba was a challenging task. There is robust
documentation of the human cultural dimension scores from Hofstede’s survey, but only for major global languages
spoken in countries like the United States, Germany, and China. There is very limited Hofstede cultural survey
information for Malayalam and Yoruba. To bridge this gap, we constructed our survey of questions. We condensed
the Hofstede cultural survey into 23 comprehensive questions covering PDI, IDV, UAI, MAS, LTO, and IVR. In each
cultural dimension, we created 3 or 4 questions. Very similar to the LLM approach; the questions were designed such
that the response would reveal an inclination towards or away from that cultural dimension. We circulated this form
to Malayalam and Yoruba speakers. The survey candidates were chosen carefully from diverse backgrounds, careers,
and age groups to prevent biases. A summary of the demographics of Malayalam respondents is shown in Figure 5.
Here is a summary of the responses we received:
• Malayalam: 71 responses.
• Yoruba: 90 responses.
Figure 6 shows the Google form survey responses for one sample question, shown for each cultural dimension for
Malayalam and Yoruba languages. As can be seen from the response split, we obtained a diverse set of responses for
each question.
We strongly believe that our study is one of the first to collect Malayalam and Yoruba-specific data for these cultural
scores. We will make the available dataset public and continue to collect more responses. For the study, due to
the diverse and heterogeneous nature of the responses, the amount of responses we collected serves our purpose of
generating a robust ground truth score. More responses might alter this score, but not by a significant amount.
7

--- Page 8 ---

A PREPRINT - OCTOBER 4, 2024
Figure 5: Summary of Malayalam respondent demographics. We have covered a wide (A) age group, (B)
years of work experience, (C) education qualification, and (D) religions.
For a given cultural dimension di, where 1 < i < 6, if N questions were asked, and P out of them corresponded to
the positive inclination to that score, we defined the Ground truth cultural score for that metric as
GT(di) = P
N
(2)
2.3
Cultural similarity score
Equations 1 and 2 served as the basic building blocks for evaluating the LLM cultural barrier. Along with these
equations, we also defined a similarity score between the LLM score (LLM(di)) and the ground truth score (GD(di))
for a given cultural dimension di, as follows [53] in equation 3.
Sim(LLM, GD) =
1
1 +
qP6
i=1(LLM(di) −GT(di))2
(3)
2.4
Algorithm Design
We explain the implementation and logic for evaluating the LLMs on the datasets. We used questions from the
CDEval benchmark [38]. A sample of each JSON file for each of the languages is read. We load all 6 dimensions
for each language. The files are passed through the ‘loadOrComputeScore()‘ function, which checks if the scores for
the dimensions of each language are computed; if the languages have been computed, we use the scores. If not, we
compute the scores. We define the keys for each language, English, Malayalam, and Yoruba, and print the format for
each language along with the keys for each dimension. A statement is included to get the values of the keys by using
the first three items.
In computing the scores, we take the questions from a specific language and dimension. A prompt is constructed using
the question and its options for each question. The prompt is passed three times to the LLM. It then analyses the
response to determine the chosen option associated with the measured cultural dimension.
8

--- Page 9 ---

A PREPRINT - OCTOBER 4, 2024
Figure 6: Google form survey responses for 1 question, shown for each cultural dimension, for the Malay-
alam and Yoruba language. A total of 71 responses were collected for Malayalam and 92 for Yoruba.
The individual scores are combined using a simple average, and the cultural dimension score is computed by taking
the aggregated score and passing it through the ‘computeCulturalDimensionScore‘ function for each of the dimensions
of all the languages. After calculating the scores for all the dimensions, we calculate the similarity to determine how
close the scores are to the ground truth. The process is repeated through all dimensions of the languages and the results
are stored in JSON files.
3
Results
Our study compared the cultural dimension scores obtained from GPT-4o-mini and Gemma 7B for English, Malay-
alam, and Yoruba languages against ground truth data. The results reveal significant disparities in the LLMs’ ability
to capture cultural nuances across these languages. Figures 7 through 9 represent the results of our study on the cul-
tural awareness of large language models (LLMs) for Yoruba, Malayalam, and English. Using Hofstede’s cultural
dimension as a framework, these figures provide a comprehensive view of how well different LLMs do across these
languages.
3.1
Overall Trend
Table 2 compares Hofstede’s Cultural Dimensions between Ground Truth and two LLMs (GPT-4o-mini and Gemma-
7b-it) across English, Yoruba, and Malayalam. The computed scores for individual dimensions are plotted as bar
graphs in Figure 7.
9

--- Page 10 ---

A PREPRINT - OCTOBER 4, 2024
Algorithm 1 Algorithm Design
1: Input: Languages L = {Malayalam, Yoruba, English}
2: Hofstede Dimensions D = {IDV, IVR, UAI, PDI, MAS, LTO}
3: JSON Directories Fl for each l ∈L
4: Response Number R = 3
5: Cache File Path
6: Output: Computed scores ˆCM(l, d) for each language l and dimension d.
7: Ml ←read json files(Fl) for each l ∈L
8: for each l ∈L do
9:
for each d ∈D do
10:
if ˆCM(l, d) exists in cache then
11:
Retrieve ˆCM(l, d) from cache
12:
else
13:
Initialize scores ←[]
14:
for each q in Ml(d) do
15:
Construct prompt using q and options o1 and o2
16:
for k = 1 to R do
17:
response ←M(prompt)
18:
ˆak ←extract action(response)
19:
Append ˆak to scores
20:
end for
21:
end for
22:
Calculate ˆCM(l, d) from scores
23:
Store ˆCM(l, d) in cache
24:
end if
25:
end for
26: end for
27: Output: the computed scores ˆCM(l, d) for each l and d.
Table 2: Comparison of Ground Truth and Computed Scores Across Hofstede’s Dimensions
Language
PDI
IDV
MAS
UAI
LTO
IVR
Ground Truth
English
0.40
0.60
0.62
0.46
0.50
0.68
Yoruba
0.46
0.48
0.26
0.41
0.70
0.36
Malayalam
0.21
0.48
0.21
0.32
0.49
0.38
GPT-4o-mini
English
0.83
0.69
0.81
0.66
0.31
0.43
Yoruba
0.45
0.29
0.53
0.29
0.05
0.13
Malayalam
0.54
0.38
0.57
0.38
0.11
0.16
Gemma-7b-it
English
0.84
0.53
0.80
0.67
0.17
0.42
Yoruba
0.18
0.20
0.21
0.15
0.17
0.27
Malayalam
0.79
0.64
0.83
0.78
0.47
0.58
(a) Computed scores using GPT-4o-mini.
(b) Computed scores using Gemma 7B.
English
Yoruba
Malayalam
Figure 7: Comparison of computed scores for English, Yoruba, and Malayalam across Hofstede’s 6 cultural
dimensions using GPT-4o-mini and Gemma 7B.
10

--- Page 11 ---

A PREPRINT - OCTOBER 4, 2024
PDI
IDV
MAS
UAI
LTO
IVR
0.2 0.4 0.6 0.8 1.0
English Ground Truth
English GPT-4o-mini
Yoruba Ground Truth
Yoruba GPT-4o-mini
Malayalam Ground Truth
Malayalam GPT-4o-mini
Figure 8: Comparison of cultural scores for GPT-4o-mini vs Ground Truth Across Hofstede’s 6 Cultural
Dimensions
This variation is particularly evident in dimensions like Power Distance Index (PDI) and Masculinity (MAS), where
the models tend to overestimate the cultural acceptance of hierarchy and assertiveness in these languages compared to
their ground truth scores. For example, both models significantly overestimate PDI for English (Ground truth: 0.40,
GPT-4o-mini: 0.83, Gemma-7b-it: 0.84) and Malayalam (Ground truth: 0.21, GPT-4o-mini: 0.54, Gemma-7b-it:
0.79). This suggests that the models may overestimate how much power inequality is tolerated in English-speaking
cultures and may project those learned cultural norms onto underrepresented languages like Malayalam, where equality
may be more common. For Yoruba, GPT-4o-mini closely matches the ground truth (0.46 vs 0.45), while Gemma-7b-it
significantly underestimates it (0.18).
In Individualism (IDV), both models slightly overestimate for English, with GPT-4o-mini being closer to the ground
truth (Ground truth: 0.60, GPT-4o-mini: 0.69, Gemma-7b-it: 0.53). For Yoruba and Malayalam, both models under-
estimate IDV, with Gemma-7b-it showing a higher score for Malayalam (0.64) compared to the ground truth (0.48).
This underestimates the communist tendencies in Yoruba and Malayalam. This underestimation can be attributed to
the models being trained predominantly on Western-centric data, where individualism is more pronounced, leading to
weaker performance when capturing the stronger community orientation found in these regional languages.
Both models overestimate this dimension for English in the Uncertainty Avoidance Index (UAI). For Yoruba and
Malayalam, GPT-4o-mini underestimates UAI, while Gemma-7b-it underestimates for Yoruba but significantly over-
estimates for Malayalam. This just shows that both models have trouble understanding how the culture tends to avoid
risks and deal with uncertainty. The most significant differences are observed in the Long Term Orientation (LTO)
and Indulgence (IVR) dimensions. Both models consistently underestimate these dimensions across all three lan-
guages, with the underestimation being particularly severe for Yoruba and Malayalam in the LTO dimension. This
suggests the models struggle to capture fundamental cultural values related to future orientation, tradition, and self-
restraint in these cultures.
These results indicate that while the models show some understanding of cultural dimensions, they struggle to ac-
curately represent the nuances across different languages, particularly for non-English languages like Yoruba and
Malayalam. The consistent overestimation of some dimensions (like MAS) and underestimation of others (like LTO
and IVR) across languages suggest systematic biases in how these models represent cultural attributes. Figure 8 and 9
display the overall trend as a spider plot.
11

--- Page 12 ---

A PREPRINT - OCTOBER 4, 2024
PDI
IDV
MAS
UAI
LTO
IVR
0.2 0.4 0.6 0.8 1.0
English Ground Truth
English Gemma-7b-it
Yoruba Ground Truth
Yoruba Gemma-7b-it
Malayalam Ground Truth
Malayalam Gemma-7b-it
Figure 9: Comparison of cultural scores for Gemma-7b-it vs Ground Truth Across Hofstede’s 6 Cultural
Dimensions
3.2
Model’s general performance across languages.
Here, we examine the cultural sensitivity of the models across the selected languages: Yoruba, Malayalam, and En-
glish. We focus on evaluating the capabilities of GPT-4o mini and Gemma-7b-it in this regard. Equation 3 shows the
cultural similarity score calculation between a model and the corresponding language’s country. Table 3 shows the
similarity scores for both models across the three languages.
GPT-4o-mini performs best in English, with a similarity score of 0.6225. Malayalam was the second-highest, with
a score of 0.5998, suggesting a slightly lower performance than English. On the other hand, Yoruba had the lowest
score, 0.5637, indicating the model struggles most with this language. Interestingly, Gemma-7b-it shows a different
pattern. It performs best with Yoruba (0.5819), followed closely by English (0.5981), while it struggles the most with
Malayalam (0.5002). The results are also plotted in the bar plot of Figure 10 for better visualization.
Table 3: Similarity Scores Across Languages for GPT-4o-mini and Gemma-7b-it
Language
GPT-4o-mini
Gemma-7b-it
English
0.6225
0.5981
Yoruba
0.5637
0.5819
Malayalam
0.5998
0.5002
The model shows a range of clustering scores from approximately 0.56 to 0.62, indicating that the model performs
better than random chance (0.5) across all languages. However, this narrow range might indicate a ceiling effect in
the model’s ability to capture each language’s cultural nuances and unique linguistic features, pointing to architectural
or training limitations. The higher score for English in GPT-4o-mini is not surprising because most LLMs are trained
predominantly on English data. However, the model’s performance in Malayalam is notably close to English, which
was unexpected but interesting. For Gemma-7b-it, the surprisingly good performance in Yoruba and the relatively
poor performance in Malayalam raises questions about the model’s training data and architecture.
This narrow range could imply that the model lacks a deep understanding of diverse cultural contexts. The findings
also highlight that no model performs consistently well across all cultural dimensions, particularly for non-English
languages. This calls for more diverse and representative training data to improve its ability to adapt to a language’s
unique features.
12

--- Page 13 ---

A PREPRINT - OCTOBER 4, 2024
(a) Similarity Scores for GPT-4o-mini for English,
Yoruba, and Malayalam. As hypothesized, the LLM
captures cultural nuances in English better than
Yoruba and Malayalam.
(b) Similarity Scores for Gemma 7B for English,
Yoruba, and Malayalam. Similar trends are observed
in cultural nuance capturing, with differences in accu-
racy across languages.
Figure 10: Comparison of Similarity Scores for GPT-4o-mini and Gemma 7B for English, Yoruba, and
Malayalam.
3.3
Performance Analysis
Table 4a and 4b show the similarity scores for GPT-4o- mini and Gemma-7b-it across the three languages. These
scores are calculated based on the absolute difference between the ground truth and the GPT-4o-mini predicted scores,
normalized to a 0-1 scale where 1 indicates perfect similarity. These scores reveal varying levels of accuracy across
languages and dimensions.
Table 4: Similarity Scores Across Dimensions for GPT-4o-mini and Gemma-7b-it
(a) GPT-4o-mini
Dim.
Eng.
Yor.
Mal.
PDI
0.57
0.99
0.33
IDV
0.91
0.81
0.90
MAS
0.81
0.27
0.36
UAI
0.80
0.88
0.94
LTO
0.81
0.35
0.62
IVR
0.75
0.77
0.78
(b) Gemma-7b-it
Dim.
Eng.
Yor.
Mal.
PDI
0.84
0.18
0.79
IDV
0.53
0.20
0.64
MAS
0.80
0.21
0.83
UAI
0.67
0.15
0.78
LTO
0.17
0.17
0.47
IVR
0.42
0.27
0.58
English shows consistently high similarity across all dimensions in GPT-4o-mini, with IDV being the closest match
(0.91). Yoruba demonstrates high similarity in PDI (0.99) and UAI (0.88) but very low similarity in MAS (0.27)
and LTO (0.35). Malayalam exhibits high similarity in UAI (0.94) and IDV (0.90) but low similarity in PDI (0.33)
and MAS (0.36). However, in Gemma-7b-it, English shows high similarity in PDI (0.84) and MAS (0.80) but lower
similarity in LTO (0.17). Yoruba exhibits low similarity across most dimensions, particularly in PDI (0.18) and UAI
(0.15), with modest similarity in IVR (0.27). Malayalam demonstrates high similarity in MAS (0.83) and UAI (0.78)
but a lower similarity in LTO (0.47) and IDV (0.64).
GPT-4o-mini Performance Analysis
GPT-4o-mini tends to overestimate most dimensions for English, especially PDI and MAS, as shown in Table 5. For
Yoruba, it shows mixed results, underestimating some dimensions (IDV, UAI, LTO, IVR) and overestimating others
(MAS). The LTO dimension shows the most significant discrepancy for Yoruba. The model overestimates PDI, MAS,
and UAI in Malayalam while underestimating IDV, LTO, and IVR.
13

--- Page 14 ---

A PREPRINT - OCTOBER 4, 2024
Dimension
English
(GT vs GPT-4o)
Yoruba
(GT vs GPT-4o)
Malayalam
(GT vs GPT-4o)
PDI
0.40 vs 0.83 (-0.43)
0.46 vs 0.45 (0.01)
0.21 vs 0.54 (-0.33)
IDV
0.60 vs 0.69 (-0.09)
0.48 vs 0.29 (0.19)
0.48 vs 0.38 (0.10)
MAS
0.62 vs 0.81 (-0.19)
0.26 vs 0.53 (-0.27)
0.21 vs 0.57 (-0.36)
UAI
0.46 vs 0.66 (-0.20)
0.41 vs 0.29 (0.12)
0.32 vs 0.38 (-0.06)
LTO
0.50 vs 0.31 (0.19)
0.70 vs 0.05 (0.65)
0.49 vs 0.11 (0.38)
IVR
0.68 vs 0.43 (0.25)
0.36 vs 0.13 (0.23)
0.38 vs 0.16 (0.22)
Table 5: Comparison of Ground Truth (GT) and GPT-4o-mini’s predictions for each dimension across three
languages. Positive values in parentheses indicate underestimation, while negative values indicate overes-
timation by GPT-4o-mini.
Dimension
English
(GT vs Gemma)
Yoruba
(GT vs Gemma)
Malayalam
(GT vs Gemma)
PDI
0.40 vs 0.84 (-0.44)
0.46 vs 0.18 (0.28)
0.21 vs 0.79 (-0.58)
IDV
0.60 vs 0.53 (0.07)
0.48 vs 0.20 (0.28)
0.48 vs 0.64 (-0.16)
MAS
0.62 vs 0.80 (-0.18)
0.26 vs 0.21 (0.05)
0.21 vs 0.83 (-0.62)
UAI
0.46 vs 0.67 (-0.21)
0.41 vs 0.15 (0.26)
0.32 vs 0.78 (-0.46)
LTO
0.50 vs 0.17 (0.33)
0.70 vs 0.17 (0.53)
0.49 vs 0.47 (0.02)
IVR
0.68 vs 0.42 (0.26)
0.36 vs 0.27 (0.09)
0.38 vs 0.58 (-0.20)
Table 6: Comparison of Ground Truth (GT) and Gemma’s predictions for each dimension across three
languages. Positive values in parentheses indicate underestimation, while negative values indicate overes-
timation by Gemma.
Gemma-7b-it Performance Analysis
Gemma-7b-it also tends to overestimate most dimensions for English, particularly PDI and MAS. For Yoruba, it
consistently underestimates most dimensions, with only LTO showing the most significant discrepancy. In Malayalam,
Gemma-7b-it significantly overestimates most dimensions, with very large discrepancies in PDI and MAS.
Both models show similar trends in English, overestimating most dimensions, especially PDI and MAS. GPT-4o-
mini shows slightly better overall similarity scores. In Yoruba, the models perform differently. While GPT-4o-mini
shows mixed results with high accuracy in some dimensions (PDI, UAI), Gemma-7b-it consistently underestimates
most dimensions. GPT-4o-mini’s predictions for Yoruba show higher overall similarity to ground truth. Both models
struggle with accurate predictions in Malayalam. GPT-4o-mini shows varied performance across dimensions, while
Gemma-7b-it significantly overestimates most dimensions. GPT-4o-mini generally shows higher similarity scores for
Malayalam, as shown in Table 3.
These results highlight the complex nature of predicting cultural dimensions across different languages. While both
models show promise in certain areas, they also demonstrate significant challenges in accurately capturing nuanced
cultural aspects, particularly for non-English languages. The varying performance across dimensions and languages
suggests that further refinement is needed to improve these models’ understanding of diverse cultural contexts.
3.4
Discussion of Model Biases and Performance
The discrepancies between the cultural dimension scores predicted by the models and the ground truth for Yoruba and
Malayalam suggest that underlying model biases, particularly those related to the training data, play a significant role.
Large language models are predominantly trained on English-centric data, with minimal representation of regional
languages like Yoruba and Malayalam. The Common Crawl data 1 shows that English dominates LLM training data
(45%), while Yoruba and Malayalam account for only 0.008% and 0.0226%, respectively. This stark imbalance in the
training datasets contributes to the models’ over- or underestimation of cultural dimensions for these languages.
These biases arise because models are exposed to a disproportionate amount of content from English-speaking cultures.
This leads to internalizing cultural norms that may not align with those in underrepresented regions. For instance, the
overestimation of Power Distance (PDI) in Malayalam (ground truth: 0.21, GPT-4o-mini: 0.54) likely stems from
14

--- Page 15 ---

A PREPRINT - OCTOBER 4, 2024
hierarchical assumptions in English-speaking cultures less relevant in Malayalam-speaking contexts. Similarly, the
underestimation of Long-Term Orientation (LTO) for Yoruba (ground truth: 0.70, GPT-4o-mini: 0.05) indicates the
models’ limited understanding of future-oriented cultural values in West African societies.
The differences between non-English languages and English present challenges for language models. Yoruba and
Malayalam have unique syntactic and grammatical structures that differ from English, which can lead to misunder-
standings. The lack of cultural contexts in training data exacerbates these challenges. We need a more balanced dataset
that includes regional languages to address this. The imbalance in training data impacts the models’ linguistic abilities
and hinders their adaptability to different cultures. This restricts their usefulness in multilingual and multicultural
settings. Models perform better in English, indicating the need for improved performance in languages like Yoruba
and Malayalam. This requires larger, diverse datasets and adaptable model architectures to accommodate linguistic
and cultural diversity better.
4
Conclusion and Discussion
In this study, our main goal was to understand whether Large Language Models (LLMs) are able to effectively capture
the cultural nuances of regional languages. To achieve this goal, we looked at 2 languages: Malayalam (spoken by
≈38 million people in the state of Kerala, India) and Yoruba (spoken by ≈45 million people largely concentrated
in West Africa). We selected these 2 languages because in terms of native speakers, these languages represent a
minority - only 1-2 % of the entire population outside Africa speaks Yoruba, and only 1-2 % of the entire population
outside India speaks Malayalam. As much as ≈60 % of the training data for all modern LLMs is based on the
English language. This would naturally lead to LLMs having a poor understanding and poor functionality for regional
languages and cultures. To demonstrate this lack of LLM understanding of non-English languages, we wanted to
choose languages originating from areas that are not English-centric. People speaking Malayalam or Yoruba mostly
rely on their local language for communication, entertainment, and employment. That’s another major reason why we
selected these 2 languages.
To quantify the cultural awareness of LLM-based responses, we looked at 6 cultural metrics, also called the
Hofstede’s metrics: Power Distance (PDI), Individualism (IDV), Motivation towards Achievement and Success
(MAS), Uncertainty Avoidance (UAV), Long Term Orientation (LTO) and Indulgence (IVR). For each of these
metrics, we designed questions and recorded the LLM responses. The LLM responses helped us quantify the LLM
cultural score for each metric. We then compared the LLM cultural scores with the ground truth data for each of the
6 metrics, and obtained a cultural similarity score. The cultural similarity score is a composite score that includes
PDI, IDV, MAS, UAV, LTO, and IVR. It indicates the ability of the LLM to effectively capture the nuances of the
regional languages. A higher score indicates that the LLM better understands the regional language than a lower score.
Our results indicate that the cultural similarity score obtained for the languages of Malayalam and Yoruba is
significantly lower than English, for all the LLMs we tested: Open AI’s GPT-4o-mini and Gemma-7b-it. This clearly
demonstrates that all modern LLMs are vastly inadequate in their understanding and, consequently, their functionality
for regional languages. As the influence of LLMs grows more powerful, the English-centric bias in LLMs has the
potential to significantly affect the lives of people speaking regional languages, further highlighting the importance of
this study.
4.1
Key Findings
Our results indicate that the cultural similarity score obtained for the languages of Malayalam and Yoruba is sig-
nificantly lower than English for all the LLMs we tested: Open AI’s GPT-4o-mini and Gemma-7b-it. This clearly
demonstrates that all modern LLMs are vastly inadequate in their understanding and, consequently, their functionality
for regional languages. As the influence of LLMs grows more powerful, the English-centric bias in LLMs has the
potential to significantly affect the lives of people speaking regional languages, further highlighting the importance of
this study [5].
4.2
Implications for Cultural Sensitivity
Our findings underscore the critical need for improved cultural sensitivity in LLMs, particularly for underrepresented
languages. The significant disparity in cultural similarity scores between English and regional languages like Malay-
alam and Yoruba highlights a potential for misunderstanding and misrepresentation of these cultures in AI-driven
15

--- Page 16 ---

A PREPRINT - OCTOBER 4, 2024
applications. This lack of cultural awareness in LLMs could lead to inappropriate or ineffective interactions in various
domains, including education, healthcare, and local governance [54]. As LLMs become increasingly integrated into
global communication systems, addressing this cultural gap is crucial.
4.3
Ethical Considerations
The observed performance gap in cultural awareness between English and underrepresented languages raises important
ethical considerations. This disparity could potentially perpetuate and exacerbate existing inequalities in access to and
benefit from AI technologies, potentially leading to a form of technological colonialism if not addressed [22]. It is
imperative that the development of LLMs takes into account the diverse cultural landscapes they are intended to serve,
ensuring fair representation and understanding of all languages and cultures.
4.4
Limitations
One of the primary challenges and limitations of the present study was collecting ground truth data for Malayalam
and Yoruba. While robust documentation of human cultural dimension scores from Hofstede’s survey exists for
major global languages spoken in countries like the United States, Germany, and China, Hofstede’s cultural survey
information for Malayalam and Yoruba is very limited. To bridge this gap, we constructed our survey of questions,
managing to collect approximately 100 questions for both languages. However, this limited sample size may not
fully capture the cultural nuances of these languages. Additionally, the use of machine translation (Google Translate
API) to translate the English questions into Malayalam and Yoruba may have introduced inaccuracies or cultural
misinterpretations. The binary (Yes/No) nature of the questions may also oversimplify complex cultural concepts.
Furthermore, our study focused on only two regional languages, which, while providing valuable insights, may not be
fully representative of the vast linguistic diversity in the world. The performance of LLMs in other underrepresented
languages may vary.
4.5
Future Work
Our research opens up several avenues for future work:
1. Expanding the dataset: Collecting more responses and making this growing dataset public is one of our
long-term objectives. This will provide a more comprehensive ground truth for Malayalam and Yoruba
cultural dimensions.
2. Extending to more languages: Although we looked at only two regional languages, the applications of this
study extend to more than 1000 regional languages worldwide. Future research should include a wider range
of underrepresented languages [29].
3. Improving evaluation methods: Developing more nuanced evaluation techniques that go beyond binary
questions could provide a more accurate assessment of LLMs’ cultural awareness. This could include:
• Incorporating context-dependent scenarios to assess cultural understanding in specific situations.
• Developing multi-dimensional scoring systems that capture the complexity of cultural interactions.
• Utilizing natural language generation tasks to evaluate the LLM’s ability to produce culturally appropri-
ate responses.
4. Exploring alternative cultural frameworks: While Hofstede’s dimensions provide a valuable starting point,
future work could explore other cultural frameworks or develop new ones specifically tailored for AI evalua-
tion [39].
5. Investigating the impact of fine-tuning: Future studies could explore how fine-tuning LLMs on culturally
diverse datasets affects their cultural awareness and performance across different languages.
Although we looked at only 2 regional languages, the applications of this study extend to more than the 1000 regional
languages of the world. As LLMs become more powerful, we need to make sure that regional languages are not
getting left behind, to ensure an equitable world for all. Our study highlights the urgent need for more diverse and
culturally enriched training datasets for LLMs to improve their performance in underrepresented languages. The
results of this study emphasize the importance of addressing the cultural awareness gap in LLMs for the thousands
of regional languages of the world. As LLMs become increasingly influential, ensuring equitable representation and
understanding of regional languages is crucial for creating a more inclusive global AI landscape.
16

--- Page 17 ---

A PREPRINT - OCTOBER 4, 2024
5
Github
Here is the GitHub repo where we have hosted our code: LLM-Cultural-Awareness
References
[1] Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad Usman, Naveed
Akhtar, Nick Barnes, and Ajmal Mian. A comprehensive overview of large language models, 2024.
[2] Lizhou Fan, Lingyao Li, Zihui Ma, Sanggyu Lee, Huizi Yu, and Libby Hemphill. A bibliometric review of large
language models research from 2017 to 2023, 2017.
[3] Wen Lai, Mohsen Mesgar, and Alexander Fraser. Llms beyond english: Scaling the multilingual capability of
llms with cross-lingual feedback, 2024.
[4] Common
Crawl.
Common
crawl
language
statistics.
https://commoncrawl.github.io/
cc-crawl-statistics/plots/languages, 2024. [Accessed: 2024-08-01].
[5] Su Lin Blodgett, Solon Barocas, Hal Daum´e III, and Hanna Wallach. Language (technology) is power: A critical
survey of “bias” in NLP. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault, editors, Proceedings
of the 58th Annual Meeting of the Association for Computational Linguistics, pages 5454–5476, Online, July
2020. Association for Computational Linguistics.
[6] Vera Neplenbroek, Arianna Bisazza, and Raquel Fern´andez. Mbbq: A dataset for cross-lingual comparison of
stereotypes in generative llms, 2024.
[7] Roberto Navigli, Simone Conia, and Bj¨orn Ross. Biases in large language models: Origins, inventory, and
discussion. ACM Journal of Data and Information Quality, 15:1 – 21, 2023.
[8] Sheikh Shafayat, Eunsu Kim, Juhyun Oh, and Alice Oh. Multi-fact: Assessing multilingual llms’ multi-regional
knowledge using factscore, 2024.
[9] Tanja Samardzic, Ximena Gutierrez-Vasques, Christian Bentz, Steven Moran, and Olga Pelloni. A measure for
transparent comparison of linguistic diversity in multilingual nlp data sets. arXiv.org, abs/2403.03909, 2024.
[10] Tarek Naous, Michael J. Ryan, and Wei Xu. Having beer after prayer? measuring cultural bias in large language
models. arXiv.org, abs/2305.14456, 2023.
[11] Sharon Levy, Neha Anna John, Ling Liu, Yogarshi Vyas, Jie Ma, Yoshinari Fujinuma, Miguel Ballesteros,
Vittorio Castelli, and Dan Roth.
Comparing biases and the impact of multilingual training across multiple
languages, 2023.
[12] Millicent Ochieng, Varun Gumma, Sunayana Sitaram, Jindong Wang, Vishrav Chaudhary, Keshet Ronen, Kalika
Bali, and Jacki O’Neill. Beyond metrics: Evaluating llms’ effectiveness in culturally nuanced, low-resource real-
world scenarios, 2024.
[13] Laurel Guthrie, Joseph Mkandawire, E. Anna Stevenson, Sharon Bonya, Brent Sherwin, Moses Kasumba, Linda
Hong, Yevgeniya Ioffe, and Sharon S. Lum. Lessons in cultural adaptations: Translation of european organi-
zation for research and treatment of cancer quality of life questionnaire cervical cancer module from english to
chichewa in malawi. Journal of Surgical Research, 2023.
[14] M. Zaki and Umar Saeed. Bridging linguistic divides: The impact of ai-powered translation systems on commu-
nication equity and inclusion. Journal of translation and language studies, 2024.
[15] Razvan Cristian Voicu, Aarush Kaunteya Pande, M. Hassan Tanveer, and Yusun Chang. Communication inter-
change for artificial intelligence systems. 2024.
[16] Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On the dangers of
stochastic parrots: Can language models be too big?
In Proceedings of the 2021 ACM Conference on Fair-
ness, Accountability, and Transparency, FAccT ’21, page 610–623, New York, NY, USA, 2021. Association for
Computing Machinery.
[17] Ehsan Toreini, Mhairi Aitken, Kovila Coopamootoo, Karen Elliott, Carlos Gonzalez Zelaya, and Aad van
Moorsel. The relationship between trust in ai and trustworthy machine learning technologies, 2019.
[18] Xunhui Yuan, Jinglu Hu, and Qian Zhang. A comparative analysis of cultural alignment in large language models
in bilingual contexts, 2024.
[19] Pedro Jos´e Posada G´omez. Towards a praxis for intercultural ethics in explainable ai, 2023.
[20] Ao Xiang. Diversity must be at the heart of equitable ai development. 2022.
17

--- Page 18 ---

A PREPRINT - OCTOBER 4, 2024
[21] Peter Brien. Diversity and inclusion in artificial intelligence. 2022.
[22] Nithya Sambasivan, Shivani Kapania, Hannah Highfill, Diana Akrong, Praveen K. Paritosh, and Lora Aroyo.
“everyone wants to do the model work, not the data work”: Data cascades in high-stakes ai. Proceedings of the
2021 CHI Conference on Human Factors in Computing Systems, 2021.
[23] An analytics of culture: Modeling subjectivity, scalability, contextuality, and temporality, 2022.
[24] Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah.
How well do llms represent values
across cultures? empirical analysis of llm responses based on hofstede cultural dimensions. arXiv preprint
arXiv:2406.14805, 2024.
[25] Melville J Herskovits. Cultural anthropology. 1955.
[26] John R Hall, Mary Jo Neitz, and Marshall Battani. Sociology on culture. Psychology Press, 2003.
[27] Dirk Hovy and Shannon L. Spruit. The social impact of natural language processing. In Katrin Erk and Noah A.
Smith, editors, Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume
2: Short Papers), pages 591–598, Berlin, Germany, August 2016. Association for Computational Linguistics.
[28] Tricia L. Merkley, Carrie Esopenko, Vanessa Zizak, Robert M. Bilder, Adriana M. Strutt, David F. Tate, and
Andrei Irimia. Challenges and opportunities for harmonization of cross-cultural neuropsychological data. Neu-
ropsychology (journal), 2022.
[29] Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika Bali, and Monojit Choudhury. The state and fate of linguis-
tic diversity and inclusion in the NLP world. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault,
editors, Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 6282–
6293, Online, July 2020. Association for Computational Linguistics.
[30] Jing Lu and Vincent Ng. Conundrums in event coreference resolution: Making sense of the state of the art. In
Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih, editors, Proceedings of the 2021
Conference on Empirical Methods in Natural Language Processing, pages 1368–1380, Online and Punta Cana,
Dominican Republic, November 2021. Association for Computational Linguistics.
[31] Julia Kreutzer, Isaac Caswell, Lisa Wang, Ahsan Wahab, Daan van Esch, Nasanbayar Ulzii-Orshikh, Allah-
sera Tapo, Nishant Subramani, Artem Sokolov, Claytone Sikasote, Monang Setyawan, Supheakmungkol Sarin,
Sokhar Samb, Benoˆıt Sagot, Clara Rivera, Annette Rios, Isabel Papadimitriou, Salomey Osei, Pedro Ortiz
Suarez, Iroro Orife, Kelechi Ogueji, Andre Niyongabo Rubungo, Toan Q. Nguyen, Mathias M¨uller, Andr´e
M¨uller, Shamsuddeen Hassan Muhammad, Nanda Muhammad, Ayanda Mnyakeni, Jamshidbek Mirzakhalov,
Tapiwanashe Matangira, Colin Leong, Nze Lawson, Sneha Kudugunta, Yacine Jernite, Mathias Jenny, Orhan Fi-
rat, Bonaventure F. P. Dossou, Sakhile Dlamini, Nisansa de Silva, Sakine C¸ abuk Ballı, Stella Biderman, Alessia
Battisti, Ahmed Baruwa, Ankur Bapna, Pallavi Baljekar, Israel Abebe Azime, Ayodele Awokoya, Duygu Ata-
man, Orevaoghene Ahia, Oghenefego Ahia, Sweta Agrawal, and Mofetoluwa Adeyemi. Quality at a glance:
An audit of web-crawled multilingual datasets. Transactions of the Association for Computational Linguistics,
10:50–72, 2022.
[32] Muhammad Farid Adilazuarda, Sagnik Mukherjee, Pradhyumna Lavania, Siddhant Singh, Alham Fikri Aji, Jacki
O’Neill, Ashutosh Modi, and Monojit Choudhury. Towards measuring and modeling ”culture” in llms: A survey,
2024.
[33] Chen Liu, Fajri Koto, T. E. Baldwin, and Iryna Gurevych. Are multilingual llms culturally-diverse reasoners? an
investigation into multicultural proverbs and sayings. arXiv.org, abs/2309.08591, 2023.
[34] Binwei Yao, Ming Jiang, Diyi Yang, and Junjie Hu. Empowering llm-based machine translation with cultural
awareness. arXiv.org, abs/2305.14328, 2023.
[35] Jesse Vig. A multiscale visualization of attention in the transformer model, 2019.
[36] A Mane. Unlocking machine learning model decisions: A comparative analysis of lime and shap for enhanced
interpretability, 2024.
[37] Ondˇrej C´ıfka and Antoine Liutkus. Black-box language model explanation by context length probing. In Pro-
ceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers),
page 1067–1079. Association for Computational Linguistics, 2023.
[38] Yuhang Wang, Yanxu Zhu, Chao Kong, Shuyu Wei, Xiaoyuan Yi, Xing Xie, and Jitao Sang. Cdeval: A bench-
mark for measuring the cultural dimensions of large language models, 2024.
[39] Reem I. Masoud, Ziquan Liu, Martin Ferianc, Philip Treleaven, and Miguel Rodrigues. Cultural alignment in
large language models: An explanatory analysis based on hofstede’s cultural dimensions, 2024.
18

--- Page 19 ---

A PREPRINT - OCTOBER 4, 2024
[40] Junho Myung, Nayeon Lee, Yi Zhou, Jiho Jin, Rifki Afina Putri, Dimosthenis Antypas, Hsuvas Borkakoty, Eunsu
Kim, Carla Perez-Almendros, Abinew Ali Ayele, et al. Blend: A benchmark for llms on everyday knowledge in
diverse cultures and languages. arXiv preprint arXiv:2406.09948, 2024.
[41] Abhinav Rao, Akhila Yerukola, Vishwa Shah, Katharina Reinecke, and Maarten Sap. Normad: A benchmark
for measuring the cultural adaptability of large language models. arXiv preprint arXiv:2404.12464, 2024.
[42] Upol Ehsan and Mark O. Riedl. Human-centered explainable ai: Towards a reflective sociotechnical approach,
2020.
[43] Alejandro Barredo Arrieta, Natalia D´ıaz-Rodr´ıguez, Javier Del Ser, Adrien Bennetot, Siham Tabik, Alberto
Barbado, Salvador Garc´ıa, Sergio Gil-L´opez, Daniel Molina, Richard Benjamins, Raja Chatila, and Francisco
Herrera. Explainable artificial intelligence (xai): Concepts, taxonomies, opportunities and challenges toward
responsible ai, 2019.
[44] Riccardo Guidotti, Anna Monreale, Salvatore Ruggieri, Franco Turini, Dino Pedreschi, and Fosca Giannotti. A
survey of methods for explaining black box models, 2018.
[45] Cynthia Rudin. Stop explaining black box machine learning models for high stakes decisions and use inter-
pretable models instead, 2019.
[46] Finale Doshi-Velez and Been Kim. Towards a rigorous science of interpretable machine learning, 2017.
[47] Derek Doran, Sarah Schulz, and Tarek R. Besold. What does explainable ai really mean? a new conceptualization
of perspectives, 2017.
[48] Geert Hofstede. Cultural dimensions in management and planning. Asia Pacific journal of management, 1(2):81–
99, 1984.
[49] Geert Hofstede, Gert Jan Hofstede, and Michael Minkov. Cultures and organizations: Software of the mind.
McGraw-Hill, 2010.
[50] Michael Minkov and Geert Hofstede. Cross-cultural analysis: The science and art of comparing the world’s
modern societies and their cultures. Cross-Cultural Research, 45(3):259–298, 2011.
[51] Geert Hofstede. Dimensions do not exist: A reply to brendan mcsweeney. Human relations, 55(11):1355–1361,
2002.
[52] Geert Hofstede. Dimensionalizing cultures: The hofstede model in context. Online readings in psychology and
culture, 2(1):8, 2011.
[53] Yuhang Wang, Yanxu Zhu, Chao Kong, Shuyu Wei, Xiaoyuan Yi, Xing Xie, and Jitao Sang. Cdeval: A bench-
mark for measuring the cultural dimensions of large language models. arXiv preprint arXiv:2311.16421, 2023.
https://arxiv.org/pdf/2311.16421.
[54] Amandalynne Paullada, Inioluwa Deborah Raji, Emily M Bender, Emily Denton, and Alex Hanna. Data and its
(dis) contents: A survey of dataset development and use in machine learning research. Patterns, 2(11):100336,
2021.
19

```
