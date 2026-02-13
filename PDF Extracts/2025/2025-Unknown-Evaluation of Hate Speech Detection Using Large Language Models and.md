---
title: "2025-Unknown-Evaluation of Hate Speech Detection Using Large Language Models and - PDF Extract"
source_pdf: "2025-Unknown-Evaluation of Hate Speech Detection Using Large Language Models and.pdf"
pages: 6
extracted_at: "2026-02-13T09:50:32.279514"
---

# PDF Extract: 2025-Unknown-Evaluation of Hate Speech Detection Using Large Language Models and

**Source PDF:** 2025-Unknown-Evaluation of Hate Speech Detection Using Large Language Models and.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

Evaluation of Hate Speech Detection using Large
Language Models and Geographical
Contextualization
Anwar Hossain
Department of Computer Science
Iowa State University
Iowa, USA
ahzahid@iastate.edu
Monoshi Roy
Department of Computer Science
Iowa State University
Iowa, USA
monoshi@iastate.edu
Swarna Das
Department of Computer Science
Iowa State University
Iowa, USA
swarna@iastate.edu
Abstract—The proliferation of hate speech on social media
is one of the serious issues that is bringing huge impacts to
society: an escalation of violence, discrimination, and social
fragmentation. The problem of detecting hate speech is intrin-
sically multifaceted due to cultural, linguistic, and contextual
complexities and adversarial manipulations. In this study, we
systematically investigate the performance of LLMs on detecting
hate speech across multilingual datasets and diverse geographic
contexts. Our work presents a new evaluation framework in three
dimensions: binary classification of hate speech, geography-aware
contextual detection, and robustness to adversarially generated
text. Using a dataset of 1,000 comments from five diverse
regions, we evaluate three state-of-the-art LLMs: Llama2 (13b),
Codellama (7b), and DeepSeekCoder (6.7b). Codellama had the
best binary classification recall with 70.6% and an F1-score of
52.18%, whereas DeepSeekCoder had the best performance in
geographic sensitivity, correctly detecting 63 out of 265 locations.
The tests for adversarial robustness also showed significant
weaknesses; Llama2 misclassified 62.5% of manipulated samples.
These results bring to light the trade-offs between accuracy,
contextual understanding, and robustness in the current versions
of LLMs. This work has thus set the stage for developing
contextually aware, multilingual hate speech detection systems
by underlining key strengths and limitations, therefore offering
actionable insights for future research and real-world applica-
tions.
Index Terms—Hate Speech, Contextual Awareness, Large Lan-
guage Models
I. INTRODUCTION
Hate speech on social media has emerged as a pervasive
and harmful phenomenon, with far-reaching societal impli-
cations. Defined as language that degrades, intimidates, or
dehumanizes individuals or groups based on their identity,
race, gender, disability, sexual orientation, or other character-
istics, hate speech contributes to the escalation of violence,
discrimination, and societal polarization [1], [2]. Social media
platforms have become major vehicles for spreading harmful
ideologies, despite their utilities in fostering global connec-
tivity. Recent studies show alarming trends: the European
Commission reported a 20% increase in hate speech on major
platforms between 2020 and 2023, while in the United States,
the Anti-Defamation League found a 21% year-over-year
increase in online hate incidents. The subcontinent has been
especially susceptible to the aftereffects of online hate speech.
In India, online propaganda has led to numerous communal
riots, killing more than 1600 people between 2004 and 2017
[1]. In Bangladesh, hate speech took its course during the
Durga Puja riots in 2021, killing seven and injuring over 150
people [2]. These tragedies further pinpoint the dire need
for scalable, reliable, and context-sensitive mechanisms for
detecting hate speech.
Detecting hate speech is intrinsically a very challenging
task. While existing Machine Learning based methods work
relatively well for explicit hate speech detection, most fail in
the case of subtle or implicit hate speech manifestations as
reported in related works [3]. In particular, sarcastic or coded
languages mostly bypass traditional systems. Additionally, the
linguistic and cultural diversity in regions like South Asia
exacerbates the challenge, as hate speech varies significantly
across languages, dialects, and social contexts [4]. To com-
pound the issue, adversarial attacks, where hateful intent is
disguised through paraphrasing or obfuscation, expose the
fragility of current detection frameworks [5]. These limitations
necessitate innovative approaches that integrate contextual un-
derstanding, multilingual adaptability, and robustness against
adversarial manipulation.
LLMs like GPT-4 and Codellama provide a promising
avenue to solve these challenges. Trained on large multilingual
datasets, LLMs possess state-of-the-art contextual understand-
ing, semantic analysis, and transfer learning capabilities [6].
Initial studies have shown their potential in a wide variety of
tasks ranging from sentiment analysis to text classification.
However, their performance on hate speech detection, specif-
ically on multilingual and geographically diverse datasets, is
still relatively unexplored [7]. Our research fills this gap by rig-
orously evaluating the performance of state-of-the-art LLMs in
hate speech detection under three key dimensions. Firstly, we
assess the accuracy, precision, recall, and F1-score of LLMs
in the binary classification of hate speech in five languages,
namely Arabic, Bengali, Hindi, Chinese, and Russian. We also
probe into the ability of the models to inculcate geographical
arXiv:2502.19612v1  [cs.CL]  26 Feb 2025

--- Page 2 ---

and cultural contexts into their classification decisions. At last,
we test resilience against adversarially generated text designed
to obscure hateful intent. These are achieved by collecting a
dataset of 10,000 multilingual comments from publicly avail-
able sources such as Kaggle, Hatebase, and community-driven
datasets [8], [9]. Each comment was annotated for hate speech
content and geographical origin. Non-English comments were
translated into English using Google Translate and LLM-based
translation techniques, ensuring sentiment preservation. The
dataset is uniquely suited for comprehensive evaluation due to
the diversity of cultural and linguistic nuances.
Our approach uses prompt engineering to enhance the
performance of LLMs. For hate speech detection, we designed
structured prompts with in-context examples, which helped
the models understand nuanced text. In adversarial robustness
tests, we used GPT-4 to generate synthetic adversarial samples
by paraphrasing or injecting noise into original comments.
These adversarial samples were used to evaluate the con-
sistency and resilience of LLM predictions. Three advanced
LLMs were evaluated: Llama2 (13b), Codellama (7b), and
DeepSeekCoder (6.7b). Codellama had the best recall (70.6%)
and F1-score (52.18%) for hate speech detection but only
correctly predicted 10.5% of locations. DeepSeekCoder was
more geographic-sensitive but with a lower classification per-
formance. Adversarial testing showed significant vulnerabili-
ties; Llama2 misclassified 62.5% of adversarial samples. These
results indicate the trade-offs in the current state of LLMs
on accuracy, sensitivity, and robustness. Our contributions are
threefold:
• Showing the importance of geographically contextualized
datasets for hate speech detection.
• Performing an end-to-end evaluation framework to eval-
uate LLMs across multilingual, adversarial, and geo-
graphic dimensions.
• Discussing the limitations and suggesting ways of fine-
tuning LLMs for improved contextual understanding and
robustness.
The rest of the paper is organized as follows: Section II
reviews the related work on hate speech detection and LLM
applications. Section III describes the dataset and experimental
setup. In Sect. IV, it presents the technical approach involving
prompt engineering and adversarial sample generation. Section
V presents the results of the evaluation and Sect. VI discusses
those. Finally, Sect. VII outlines the threats to validity, and
Sect. VIII concludes the paper with directions for future
research.
II. RELATED WORK
In recent years, NLP and large language models have im-
proved hate speech detection. LLMs have been contributing to
enhancing both performance and interpretability in hate speech
detection. Models employ different techniques like rationale
extraction to identify and highlight elements, i.e., derogatory
words or contextual reasoning behind classifications [10].
Different
prompting
strategies,
e.g.,
general
prompts,
definition-based prompts, few-shot learning, and chain-of-
thought (CoT) were explored for detecting hate speech. Study
shows prompting strategy played a critical role in reasoning
and significantly improved contextual understanding and clas-
sification accuracy [11]. With these strategies, LLMs can ef-
fectively use their extensive pre-trained knowledge, even when
fine-tuning is not possible. CoT reasoning, in particular, has
been shown to enhance the model’s ability to detect implicit
hate speech by breaking down complex tasks into logical steps
[12]. Zero-shot learning approaches using instruction-tuned
LLMs have demonstrated equal or better performance com-
pared to the fine-tuned models in low-resource settings. [13]
It suggests the careful selection of verbalizers and prompts
helps the models to work with a wide range of datasets and
languages when the labeled data is scarce. [12] emphasize
the importance of explainability techniques in the context
of LLM-based hate speech detection. CoT reasoning offers
detailed, step-by-step rationales for predictions. By combining
explanations generated by machines with annotations made by
humans, models are able to achieve better alignment with the
requirements that are uniquely associated with the dataset. This
hybrid approach shows improved classification accuracy and
interpretability. [14]
Recently, researchers have focused on fine-tuning LLMs
with smaller parameters, which shows promising results on the
English hate speech dataset [15]. Vision-based models have
also been used to detect hate speech from images and their
captions, keeping the cultural context in mind [16]. However,
though the current research provides significant insights into
hate speech detection, minimal attention has been given to
the evaluation of LLMs on hate speech detection, keeping
the geographical context in mind. Our study aims to bridge
the gap in LLM’s hate speech evaluation while incorporating
geographical information in our evaluation process. This focus
will ensure the future directions and challenges in addressing
hate speech detection with LLMs across multiple languages
and regions.
III. TECHNICAL APPROACH
As we wanted to evaluate the capabilities of LLMs in
Hate Speech Detection, the first problem we faced was that
most of the LLMs were not trained on the multi-lingual
corpus. We aimed to evaluate hate speech across multiple
languages like Arabic, Bengali, Hindi, etc. Hence, we decided
to translate all the sample comments into English and prompt
the LLMs based on the translated English comments. For the
language translation process, we used Google’s translation
API [17]. However, the quality of Google translation may not
be consistent across all the languages, and our work might
be substantially dependent on the quality of the translation
process. So, we decided to adopt LLM translation and
prompted the models to keep the sentiment of the original
text intact. Pre-trained models might not be a good approach
for language translation; fine-tuning can be a better approach
for this application. However, we haven’t used any fine-tuning
on the models for this project to improve the sentiment-based
translation task. We have used two different prompts for the

--- Page 3 ---

hate speech detection evaluation and translating the language
with LLM. For hate speech evaluation, we used the prompt
structure in Fig.1, where we used three different language
comments for in-context examples. We used specific tags like
[ANSWER] [/ANSWER] to dictate the LLMs to give the
prediction in particular tags so that we could quickly parse
the responses of the LLMs by just extracting the prediction
inside these tags. For translation, we used the prompt in Fig.
2. In this case, we used two in-context examples.
We also analyzed the robustness of LLMs responses by
promoting the models with some adversarial examples. For
this task, we selected 50 English language hate-speech and
non-hate speech samples and prompted LLM (GPT-4) to create
adversarial samples of those samples to flip the labels for the
LLM predictions. Then we prompted (fig. 3) the LLMs with
both original and adversarial samples and analyzed how the
models predict with the adversarial samples.
Task Description
You will be given a translated comment from one of
the following regions: Arab, Bangladesh, India, China,
or Russia/Ukraine. Based on the given translated com-
ment, you need to predict whether it contains hate
speech or not.
If the comment contains hate speech or not, pro-
vide your prediction inside [ANSWER][/ANSWER]
tags. Additionally, identify the geographical region
of the comment and provide your prediction in
[LOCATION][/LOCATION] tags.
Below are some examples:
In-context Examples
[TRANSLATED COMMENT] Comment [/TRANS-
LATED COMMENT]
[QUESTION] Does this comment contain hate speech?
And which region is the comment from? [/QUES-
TION]
[ANSWER] Yes/No [/ANSWER]
[LOCATION] Label Location [/LOCATION]
Example Query
[TRANSLATED COMMENT] comment [/TRANS-
LATED COMMENT]
[QUESTION] Does this comment contain hate speech?
And which region is the comment from? [/QUES-
TION]
Fig. 1: Prompt Structure for Hate Speech Evaluation.
Task Description
You will be given a Bengali Comment, and your task is
to translate the Bengali Comment to English Comment
without changing the Sentiment of the original lan-
guage. Give the English Translation inside [TRANS-
LATION] [/TRANSLATION] tags, don’t print any
extra information. Here are some examples:
In-context Examples
[BENGALI COMMENT]
Comment
[/BEN-
GALI COMMENT]
Translate
the
Bengali
comment
to
sentiment-
preserving English Comment.
[TRANSLATION] [/TRANSLATION]
Example Query
[BENGALI COMMENT]
comment
[/BEN-
GALI COMMENT]
Translate
the
Bengali
comment
to
sentiment-
preserving English Comment.
Fig. 2: Prompt Structure for Language Translation.
IV. EVALUATION
We can divide our evaluation into some subsections, at first
we evaluated three LLMs (llama2 [18], codellama [19] and
deepseekcoder [20]), on our dataset for hate speech detection
as a binary classification. After that, we evaluated the capa-
bilities of the models to predict the correct geography of the
hate speech, given it predicted the hate speech correctly. Then,
we studied how these three models work with the synthetic
adversarial examples. And finally, we added the case studies
for how LLM translated comments perform and examples of
how using adversarial samples misclassify the prediction.
A. Hate Speech Evaluation
TABLE I shows the result of hate speech evaluation on
LLMs. Pre-trained LLMs are not performing significantly
well on hate speech detection tasks. Codellama performs
well on our three evaluated models in all metrics, substan-
tially surpassing the other two. Codellama correctly predicted
the hate speech comments 71%(Recall: 70.60) of the time.
However, as the overall accuracy of Codellama seems to be
pretty poor, we can deduce that for most of the comments,
Codellama’s predictions are biased toward hate speech class.
Deepseekcoder ranks second among the three models, with
an accuracy of 26.40% and a recall value of 53%. Llama2’s
comparative performance was lower than the other two models

--- Page 4 ---

Task Description
You will be given a comment of English Language.
Based on the given comment, you need to predict
whether it contains hate speech or not. If the comment
contains hate speech, provide your prediction inside
[ANSWER][/ANSWER] tags. Below are some exam-
ples:
In-context Examples
[COMMENT] Comment [/COMMENT]
[QUESTION]
Does
this
comment
contain
hate
speech?[/QUESTION]
[ANSWER] Yes/No [/ANSWER]
Example Query
[COMMENT] Comment [/COMMENT]
[QUESTION]
Does
this
comment
contain
hate
speech?[/QUESTION]
Fig. 3: Prompt Structure for Language Translation.
in terms of all metrics. Fig. 4. shows the comparative bar-chart
of the performance metrics across all three models.
TABLE I: Performance comparison of models on key metrics.
Model
Accuracy (%)
Precision
Recall
F1 Score
Llama2 (13b)
16.04
23.74
33.10
27.65
Codellama (7b)
35.30
41.38
70.60
52.18
DeepSeek (6.7b)
26.50
34.64
53.00
41.90
Fig. 4: Model Performance on Hate Speech Detection.
B. Geography Detection Capabilities of the Models
We also analyzed the capabilities of the LLM models on
geographic location. For this, we are only interested in the
comments predicted as hate speech by the models. We also
analyzed that model’s location prediction if any comment is
predicted as hate speech. TABLE II shows the geographic
prediction capabilities of the models. Interestingly, we observe
that, although, Codellama was performing well in hate speech
detection, its ability to detect hate speech location is very poor.
In total, deepseek correctly predicted 63 locations out of 265
correct predictions; however, in terms of percentage, llama2 is
outperforming the other two (37 out of 94). Fig.5 shows the
comparative bar chart of this analysis.
TABLE II: Model Performance Comparison for Correct Hate
Speech Prediction and Correct Location
Model
Correct HateSpeech Prediction
Correct Location
Llama2 (13b)
94
37
Codellama (7b)
353
37
deepseek6.7
265
63
Fig. 5: Model Performance on Hate Speech Location.
C. Evaluation on Adversarial Synthetic Dataset
We evaluated three LLM models on the synthetic dataset
we developed using GPT 4. In this experiment, we focused
on whether our synthetic samples can change the label of the
predictions of the original samples. Table III depicts the results
of this experiment; in the Correct Prediction column, we are
showing out of 50 original samples how many samples were
correctly predicted by the models. Deepseekcoder outperforms
the other two models in predicting the correct English hate
speech or benign comments. Half of the comments were
predicted correctly by deepseekcoder; on the other hand, llama
and codellama correctly predicted 24 and 22 samples. The
third column, Adversarial Misclassify, denotes how many of
the correctly predicted samples were incorrectly predicted by

--- Page 5 ---

the models when we introduced the adversarial examples. Our
result shows that deepseek6.7 and codellama are robust against
this simple adversarial attack. However, llama showed the least
robustness against this attack for 15 samples (out of 24 correct
predictions); the model flipped the prediction label when the
adversarial examples were introduced.
TABLE III: Model Performance Comparison on Correct Pre-
diction and Misclassification using Adversarial Samples
Model
Correct Predictions
Adversarial Misclassify
deepseek6.7
25/50
1/25
llama
24/50
15/24
codellama
22/50
2/22
D. Case Studies
1) Google Translator vs LLM Translators on Evaluation:
We assume that the hate speech prediction results are not up
to the mark because of the quality of the Google Translator
[17]. Google Translator API doesn’t work well, preserving
the sentiment of the actual language while translating to
English. Hence, we decided to run a pilot study, if the
LLMs can be used for the translation task effectively. We
have prompted (Fig. 2) two LLMs for this task. First one is
GPT 3.5-turbo [21], and the other one is codellama-34b [22].
After the translation, we ran only the best-performing model
(codellama-7b) from Table I for the hate speech detection task.
For the translation part also, we select only one language,
Bengali, with 200 comments. In TABLE IV, we have shown
the comparative analysis of different translation techniques
regarding different metrics. We expected better results when
translating the language using LLMs. However, the table result
doesn’t show any improvement using LLMs over Google
Translate. Our pre-trained LLMs translation capabilities are
not there yet. We could have also tried different prompting
strategies on the pre-trained models. However, that is beyond
our current study.
TABLE IV: Performance Metrics for Different Translation
Techniques on Codellama-7b Model
Translator
Accuracy
Precision
Recall
F1 Score
Google Translator
33.00
38.65
66.00
47.90
GPT-3.5
31.00
38.27
62.00
47.33
Codellama (34b)
31.50
39.75
66.00
49.62
2) Adversarial Misclassification Example: As, we have
mentioned in TABLE III that llama is working poorly on our
synthetic adversarial dataset. Here we will be presenting a
motivating example.
In Fig. 6, we present a comment from the original dataset
labeled as hate speech and Llama also predicted the comment
as hate speech. After generating adversarial comments, the
prediction of Llama has been flipped, as shown in Fig. 7.
V. DISCUSSION
The evaluation result section demonstrates the capabilities
and limitations of pre-trained LLMs in Hate Speech Detection.
Original Comment
”RT @psjohnson23: The problem with retard liberals
is they think Supply & Demand means “Supply me
with everything I Demand.” #VotingMatters”
Label: Hate Speech
Llama Prediction: Hate Speech
Fig. 6: Example of an Original Comment Detected as Hate
Speech
Adversarial Comment
”RT @psjohnson23: The issue with clueless thinkers
is they assume “Supply me with whatever I want” is
the rule. #VotingMatters”
Label: Hate Speech
Llama Prediction: Non Hate Speech
Fig. 7: Example of an Adversarial Comment Misclassified as
Non Hate Speech
Our result reveals significant differences in binary hate speech
detection on different LLMs. Codellama-7b achieved better re-
sults than Llama-2 and deepseekcoder in all metrics, especially
in recall accuracy. However, the accuracy of codellama-7b was
still suboptimal compared to its higher recall, suggesting the
tendency of the model to be biased towards the hate speech
class.
The limitation of codellama-7b is also evident in the case
of correct geographic prediction. Although codellama-7b
achieved the highest accuracy for predicting hate speech, the
percentage of predicting correct geography is notably poor.
Deekseekcoder achieved the highest number of correct geo-
graphic predictions, and Llama-2 achieved the best percentage
in predicting the correct location, indicating promising aspects
of further targeted fine-tuning.
We also analyzed the adversarial robustness of the three LLM
models. Our study shows Llama-2 is highly susceptible to
adversarial attacks, flipping more than half correct predictions
during the attack. Codellama-7b and deepseekcoder demon-
strate substantial robustness against our adversarial attack.
We conducted a pilot study to find out the effectiveness of
LLM as a translator vs Google Translator. Our analysis shows
using LLM to translate the original language doesn’t help to
improve the hate speech prediction performance. However, a
detailed study on this may be required to determine the actual
reason.
VI. THREATS TO VALIDITY
Our original dataset had a total of 10k samples. Out of those,
we selected 1k samples for evaluation randomly. We haven’t
used any other systematic filtering or heuristics to choose the
”better” samples for evaluation. We didn’t find many LLMs

--- Page 6 ---

working on Multilingual data, so we had to translate the origi-
nal hate speech comment into English. So, our work is heavily
dependent on the quality of the translation. Our synthetic
adversarial dataset contains only 50 samples, which is small
set of evaluation. Additionally, While adversarial examples
were used to test robustness, these synthetic samples might not
reflect real-world adversarial behaviors, potentially limiting the
applicability of the findings to real-world scenarios. Lastly, our
work is fully evaluated on pre-trained models, which might not
be good enough for this specialized task.
VII. CONCLUSION AND FUTURE WORK
In this study, we focused on analyzing the capabilities of the
LLMs on multilingual hate speech detection and finding out
the geographic context of the hate speech. We translated the
original language comment to English and demonstrated the
feasibility of leveraging LLMs in a multilingual hate speech
dataset. We have curated 10k samples across five languages
and evaluated three LLMs on 1k randomly selected samples.
Our approach heavily relies on the quality of the translation,
which is a major dependency of our study. Despite the
challenges, our work will contribute to researching advanced
multilingual hate speech detection and translation quality.
In the future, we would like to work on targeted fine-tuned
LLMs. The 10k samples we curated will not be enough to
fine-tune LLMs, so we must curate more labeled data from
various public sources. It would also be great to see how
the new LLMs will perform on our multilingual dataset; we
couldn’t run more than three models for this study due to
resource constraints.
DATA AVAILABILITY
Our dataset and codes are available here.
ACKNOWLEDGMENT
We want to express our gratitude to Professor Amit Kumar
Sikder for his valuable feedback and guidance on this project.
REFERENCES
[1] N.
News,
“India
communal
riots
data:
2004-
2017,”
NDTV,
2017,
accessed:
2024-12-20.
[Online].
Available:
https://www.ndtv.com/india-news/
over-1600-deaths-reported-in-communal-violence-in-india-between-2004-and-2017-1766344
[2] T. Guardian, “Bangladesh riots during durga puja leave 7 dead
and
150
injured,”
The
Guardian,
2021,
accessed:
2024-12-20.
[Online].
Available:
https://www.theguardian.com/world/2021/oct/19/
bangladesh-riots-over-hindu-religious-festival
[3] Z. Waseem and D. Hovy, “Hateful symbols or hateful people?
predictive features for hate speech detection on twitter,” Proceedings
of the NAACL-HLT, 2016, accessed: 2024-12-20. [Online]. Available:
https://arxiv.org/abs/1603.08983
[4] T. Davidson, D. Warmsley, M. Macy, and I. Weber, “Automated
hate
speech
detection
and
the
problem
of
offensive
language,”
Proceedings
of
ICWSM,
2017,
accessed:
2024-12-20.
[Online].
Available: https://ojs.aaai.org/index.php/ICWSM/article/view/14955
[5] S. Eger, L. Bojic, and A. Mehler, “Data augmentation for hate
speech detection: A study on the impact of synonym replacement and
backtranslation,” Proceedings of NAACL, 2019, accessed: 2024-12-20.
[Online]. Available: https://aclanthology.org/N19-2011
[6] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal,
A. Neelakantan et al., “Language models are few-shot learners,”
Advances in Neural Information Processing Systems (NeurIPS), vol. 33,
pp. 1877–1901, 2020, accessed: 2024-12-20. [Online]. Available:
https://arxiv.org/abs/2005.14165
[7] B. Vidgen, A. Botelho, D. Broniatowski, H. Margetts, D. Nguyen, and
R. Tromble, “Detecting east asian hate speech with large language
models,” Proceedings of the ACM Web Conference (WWW), 2023,
accessed: 2024-12-20. [Online]. Available: https://dl.acm.org/doi/10.
1145/3543873.3587588
[8] Kaggle,
“Hate
speech
dataset,”
https://www.kaggle.com/datasets/
mrmorj/hate-speech-and-offensive-language-dataset,
2024,
accessed:
2024-12-19.
[9] Hatebase, “Global hate speech database,” https://hatebase.org/, 2024,
accessed: 2024-12-19.
[10] A. Nirmal, A. Bhattacharjee, P. Sheth, and H. Liu, “Towards inter-
pretable hate speech detection using large language model-extracted
rationales,” arXiv preprint arXiv:2403.12403, 2024.
[11] K. Guo, A. Hu, J. Mu, Z. Shi, Z. Zhao, N. Vishwamitra, and H. Hu,
“An investigation of large language models for real-world hate speech
detection,” in 2023 International Conference on Machine Learning and
Applications (ICMLA).
IEEE, 2023, pp. 1568–1573.
[12] Y. Yang, J. Kim, Y. Kim, N. Ho, J. Thorne, and S.-y. Yun, “Hare:
Explainable hate speech detection with step-by-step reasoning,” arXiv
preprint arXiv:2311.00321, 2023.
[13] F. M. Plaza-del Arco, D. Nozza, D. Hovy et al., “Respectful or toxic?
using zero-shot learning with language models to detect hate speech,” in
The 7th Workshop on Online Abuse and Harms (WOAH).
Association
for Computational Linguistics, 2023.
[14] S. Roy, A. Harshavardhan, A. Mukherjee, and P. Saha, “Probing llms
for hate speech detection: strengths and vulnerabilities,” arXiv preprint
arXiv:2310.12860, 2023.
[15] T. Sen, A. Das, and M. Sen, “Hatetinyllm : Hate speech detection
using
tiny
large
language
models,”
2024.
[Online].
Available:
https://arxiv.org/abs/2405.01577
[16] M. D. Bui, K. von der Wense, and A. Lauscher, “Multi3hate:
Multimodal, multilingual, and multicultural hate speech detection
with
vision-language
models,”
2024.
[Online].
Available:
https:
//arxiv.org/abs/2411.03888
[17] G. Cloud, “Cloud translation api,” https://cloud.google.com/translate,
2024, accessed: 2024-12-19.
[18] Meta,
“Llama
2
13b
model,”
https://huggingface.co/meta-llama/
Llama-2-13b, 2024, accessed: 2024-12-19.
[19] ——,
“Codellama
7b
model,”
https://huggingface.co/codellama/
CodeLlama-7b-hf, 2024, accessed: 2024-12-19.
[20] D. AI, “Deepseek coder 6.7b instruct model,” https://huggingface.co/
deepseek-ai/deepseek-coder-6.7b-instruct, 2024, accessed: 2024-12-19.
[21] OpenAI, “Gpt-3.5 turbo,” https://platform.openai.com/docs/models/gp#
gpt-3-5-turbo, 2024, accessed: 2024-12-19.
[22] Meta,
“Codellama
34b
model,”
https://huggingface.co/codellama/
CodeLlama-34b-hf, 2024, accessed: 2024-12-19.

```
