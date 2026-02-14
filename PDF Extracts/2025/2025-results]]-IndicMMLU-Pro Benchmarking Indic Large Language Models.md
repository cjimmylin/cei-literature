---\ntitle: "2025-results]]-IndicMMLU-Pro Benchmarking Indic Large Language Models - PDF Extract"\nsource_pdf: "2025/2025-results]]-IndicMMLU-Pro Benchmarking Indic Large Language Models.pdf"\npages: 18\nextracted_at: "2026-02-14T02:17:32.116087"\n---\n\n# PDF Extract: 2025-results]]-IndicMMLU-Pro Benchmarking Indic Large Language Models\n\n**Source PDF:** 2025/2025-results]]-IndicMMLU-Pro Benchmarking Indic Large Language Models.pdf\n**Total Pages:** 18\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nIndicMMLU-Pro: Benchmarking Indic Large Language Models on
Multi-Task Language Understanding
Sankalp KJ1, Ashutosh Kumar2, Laxmaan Balaji3,
Nikunj Kotecha3, Vinija Jain4*, Aman Chadha5†, Sreyoshi Bhaduri6‡
1Artificial Intelligence Institute, University of South Carolina
2Rochester Institute of Technology 3Independent Researcher
4Meta AI 5Amazon Gen AI 6Amazon
sjajee@email.sc.edu, ak1825@rit.edu, laxmaanb@gmail.com,
kotecha.nikunj95@gmail.com, hi@vinija.ai, hi@aman.ai, sreyoshibhaduri@gmail.com
Abstract
Known by more than 1.5 billion people in the
Indian subcontinent, Indic languages present
unique challenges and opportunities for natu-
ral language processing (NLP) research due to
their rich cultural heritage, linguistic diversity,
and complex structures. IndicMMLU-Pro is a
comprehensive benchmark designed to evalu-
ate Large Language Models (LLMs) across In-
dic languages, building upon the MMLU Pro
(Massive Multitask Language Understanding)
framework. Covering major languages such
as Hindi, Bengali, Gujarati, Marathi, Kannada,
Punjabi, Tamil, Telugu, and Urdu, our bench-
mark addresses the unique challenges and op-
portunities presented by the linguistic diver-
sity of the Indian subcontinent. This bench-
mark encompasses a wide range of tasks in
language comprehension, reasoning, and gen-
eration, meticulously crafted to capture the in-
tricacies of Indian languages. IndicMMLU-
Pro provides a standardized evaluation frame-
work to push the research boundaries in In-
dic language AI, facilitating the development
of more accurate, efficient, and culturally sen-
sitive models. This paper outlines the bench-
marks’ design principles, task taxonomy, and
data collection methodology, and presents
baseline results from state-of-the-art multilin-
gual models. As a publicly available resource,
IndicMMLU-Pro1 is set to contribute signif-
icantly to advancements in Indic language-
based technologies and serve as a valuable tool
for the NLP community.
1
Introduction
With over 1.5 billion speakers, Indic languages
constitute a substantial component of the world’s
*Work done outside position at Meta
†Work done outside position at Amazon Gen AI.
‡Work done outside position at Amazon.
1https://huggingface.co/datasets/LinguaLift/IndicMMLU-
Pro
linguistic tapestry, showcasing the incredible di-
versity of the Indian subcontinent, where lan-
guages from the Indo-Aryan and Dravidian fam-
ilies have evolved over centuries, shaped by a
shared cultural and historical context. As an in-
tegral part of daily life, these languages facili-
tate communication and accessibility in various
aspects of society, including education, govern-
ment, media, healthcare, and social services. Fur-
ther, by developing language-specific benchmarks
and conducting research on Indic languages, we
can increase the downstream impact on these lan-
guages on inclusion, ultimately leading to better
language support and enhanced accessibility for
the deaf and hard-of-hearing communities across
the region who use Indic sign languages (Anan-
thanarayana et al., 2021b). This, in turn, can en-
able greater social inclusion, improved education
and employment opportunities, and more effective
participation in civic life for sign language users.
The disparity in Natural Language Processing
(NLP) research and resources across languages
is striking with a survey of existing literature
showing how resources and research on Indic
languages lagging (KJ et al., 2024a).
In their
work, (Joshi et al., 2020) revealed a stark imbal-
ance, where a mere 28 percent of languages are
considered "winners," while a staggering 88 per-
cent are "left behind." This disparity is exempli-
fied by the contrast between English and Ben-
gali, languages with comparable speaker popula-
tions (Lane, 2019). Despite this, English domi-
nates Bengali regarding available resources, with
hundreds of times more visibility on platforms like
the Linguistic Data Consortium, Wikipedia, and
academic publication venues of significance.
Thus, Indic languages have historically received
less attention in the field of NLP compared to
more globally dominant languages (Das et al.,
2024).
The disparity in NLP resources for In-
dic languages has been attributed to their remark-
arXiv:2501.15747v2  [cs.CL]  28 Jan 2025

--- Page 2 ---\n\nMMLU-Pro Dataset
(English)
IndicTrans2
IndicMMLU-Pro Dataset
(9 Indic languages)
Final IndicMMLU-Pro Dataset
Translation Quality Check
Back-translated dataset 
(English)
Quality Assurance
Metrics’ Thresholds
chrF++ (>0.5) 
BLEU (>25-30)
METEOR (0.5-0.6) 
TER (<0.4-0.5) 
sacreBLEU (>25-30)
HINDI
BENGALI
TELUGU
MARATHI
TAMIL
GUJARATI
URDU
KANNADA
PUNJABI
Linguistic 
Style
Fluency &
Readability
Semantic
Accuracy
9000 
Sentence Pairs
13
Expert Reviewers
Figure 1: IndicMMLU-Pro Dataset Construction and Evaluation Pipeline. The diagram illustrates the end-to-
end process of creating and validating the IndicMMLU-Pro dataset across nine Indic languages. Starting with
the English MMLU-Pro dataset, content is translated using IndicTrans2 (1B parameters) and undergoes rigorous
quality assurance through back-translation and multiple metric evaluations (chrF++, BLEU, METEOR, TER, and
SacreBLEU). Only translations meeting quality thresholds proceed to the final dataset. The workflow also shows
the comprehensive evaluation process including expert proofreading involving 13 reviewers who assess semantic
accuracy, fluency, and linguistic style. This systematic approach ensures the creation of a high-quality, multilingual
benchmark dataset that maintains the integrity of the original MMLU-Pro while adapting to the linguistic nuances
of Indic languages.
able linguistic diversity, intricate morphology, and
the scarcity of annotated datasets (Kakwani et al.,
2020a; Marreddy et al., 2022).
Nevertheless,
driven by the increasing demand for NLP appli-
cations in Indic languages and the prospect of
groundbreaking technological innovations (Anan-
thanarayana et al., 2021a), there is an urgent need
for rigorous evaluation benchmarks to assess the
performance of AI models in this domain accu-
rately.
To address this gap, we introduce IndicMMLU-
Pro, a benchmark built upon the principles of the
recently released MMLU-Pro (Wang et al., 2024)
by Tiger Labs. IndicMMLU-Pro adapts the robust
multi-task principles to the unique context of Indic
languages, providing a comprehensive evaluation
framework that assesses the linguistic understand-
ing, reasoning abilities, and generative capabilities
of AI models.
This paper makes three key contributions. Pri-
marily, we introduce IndicMMLU-Pro, a novel
benchmark for evaluating AI models across a
wide range of tasks and multiple Indic languages.
Next, the design principles, task taxonomy, and
data collection methodology of IndicMMLU-Pro
are presented in detail, to ensure that the bench-

--- Page 3 ---\n\nmark accurately captures the complex linguistic
and cultural characteristics of Indic languages.
Furthermore, we establish baseline results on
IndicMMLU-Pro using state-of-the-art multilin-
gual models, laying the groundwork for future re-
search and development of Indic languages-based
AI models.
2
Methodology
To create IndicMMLU-Pro, a benchmark for Indic
languages equivalent to MMLU Pro, we adopted a
process similar to the prior work on IndicMMLU,
organizing our approach into two main steps:
dataset creation and baseline benchmarking.
2.1
Dataset Creation
Our goal was to provide MMLU-Pro in nine In-
dic languages: Hindi, Bengali, Telugu, Marathi,
Tamil, Gujarati, Urdu, Kannada and Punjabi.
To achieve this,
we used IndicTrans2 (Gala
et al., 2023), a state-of-the-art machine translation
model specifically designed for Indic languages.
As shown in Figure1, we use IndicTrans2 to
convert the questions and corresponding options
from the original English MMLU Pro dataset into
each of the target languages. This approach al-
lowed us to maintain the structure and content of
the original benchmark while adapting it to the lin-
guistic characteristics of Indic languages.
The experimental settings for IndicTrans2 were
as follows:
• Model Size: 1B parameters
• Quantization: None
• Batch Size: 8
We applied these settings consistently across all
nine language translations to ensure uniformity in
the translation process.
2.2
Quality Assurance
To maintain the integrity and accuracy of the trans-
lated content, we implemented a rigorous quality
assurance process:
• Back-translation: For a subset of the data,
we performed back-translation to English and
compared it with the original text to identify
any significant discrepancies.
• Validation: After back-translation, we veri-
fied the back-translated dataset with the orig-
inal MMLU-Pro on numerous metrics, such
as chrF++ BLEU, METEOR, TER & Sacre-
BLEU to ensure the dataset’s quality and con-
sistency, also described in Section 3. This
multi-metric evaluation provides a compre-
hensive assessment of the translation’s accu-
racy and fluency.
2.3
Dataset Structure
The resulting IndicMMLU-Pro dataset maintains
the same structure as the original MMLU-Pro
dataset, with separate subsets for each of the nine
Indic languages. The dataset retains the original
categories and task types from MMLU Pro, thus
ensuring identical usage and facilitating compre-
hensive evaluation in various domains and cogni-
tive skills.
2.4
Dataset Availability
The IndicMMLU-Pro dataset is publicly available
on the Hugging Face Hub (KJ et al., 2024b). This
allows for easy access and reproducibility of our
results. Researchers and practitioners can directly
use or adapt this dataset for their studies and ap-
plications in the processing of Indic languages.
2.5
Baseline Benchmarking
To establish baseline performance metrics for the
IndicMMLU-Pro benchmark, we evaluated state-
of-the-art multilingual language models: GPT-4o,
GPT-4o-mini, Llama-3.1-8B-Instruct, IndicBERT
(Kakwani et al., 2020a), IndicBART (Dabre et al.,
2021), RemBERT (Chung et al., 2020), MuRIL
(Khanuja et al., 2021), and XLM-RoBERTa (Con-
neau et al., 2020), Navarasa, Airavata (Gala et al.,
2024), OpenHathi, TamilLlama (Balachandran,
2023), and MahaMarathi. These models were cho-
sen due to their demonstrated capabilities in han-
dling multiple languages and their specific design
for the inclusion of Indic languages in their train-
ing data.
The benchmarking process was con-
ducted as follows:
• Model Selection: To provide a benchmark of
performance over the various languages con-
tained in IndicMMLU-Pro, we leverage the
following language models with Indic lan-
guage understanding capabilities.
– IndicBERT and IndicBART: Specifi-
cally designed for Indic languages, of-

--- Page 4 ---\n\nfering robust performance in this do-
main.
– RemBERT: A multilingual model with
strong performance across diverse lan-
guages, suitable for cross-lingual tasks.
– MuRIL: A multilingual model with a
focus on Indian languages, providing
comprehensive coverage of Indic lan-
guages.
– XLM-RoBERTa: A large-scale multi-
lingual model is known for its cross-
lingual performance and ability to han-
dle multiple languages efficiently.
– GPT-4o and GPT-4o-mini: State-of-
the-art models with advanced capabili-
ties in handling multilingual tasks.
– Llama-3.1-8B-Instruct: A model de-
signed for multilingual (Hindi) instruc-
tion tasks.
– Navarasa,
Airavata,
OpenHathi,
TamilLlama,
and
MahaMarathi:
Models specifically designed or fine-
tuned for Indic languages, enhancing
their performance in this domain.
• Data Preparation: We used the test split of
the IndicMMLU-Pro dataset for each of the
nine Indic languages. The data was prepro-
cessed to match the input format required by
each model.
• Evaluation Process: We used accuracy as
the primary metric, calculated as the percent-
age of correct predictions across all tasks in
the benchmark.
We acknowledge the im-
portance of using multiple evaluation met-
rics to garner a comprehensive understand-
ing of text data (Bhaduri et al., 2024a), as
different metrics can capture distinct aspects
of model performance (Bedemariam et al.,
2025).
Nevertheless, for this study, accu-
racy served as a suitable baseline metric. No-
tably, our evaluation was conducted sepa-
rately for each language, enabling language-
specific performance analysis and facilitat-
ing a more nuanced understanding of model
strengths and weaknesses across diverse lin-
guistic contexts.
• Computational Resources:
The bench-
marking was performed on a cluster of
NVIDIA A100 GPUs, with each model eval-
uation taking approximately 24 hours per lan-
guage.
The results of this baseline benchmarking are pre-
sented in Table 1 of the Results section, showing
the accuracy scores for each model across all nine
languages. This benchmarking process provides
a solid foundation for understanding the current
capabilities of multilingual models in Indic lan-
guages and sets a baseline for future research and
improvements in this area.
2.6
Proofreading and Setup
We conducted a proofreading exercise on 9,000
sentence pairs (English and Indic), where 1,000
of these pairs were from the test split of each
of the nine languages in the IndicMMLU-Pro
dataset.
These sentences pairs were stratified
equally across the 14 categories and their respec-
tive 4 sources in each of the nine languages. These
sentence pairs were shuffled randomly across all
Indic languages to eliminate any bias and ensure
there was no preservation for each source and cat-
egory after the selection process. The three criteria
that were defined for proofreading scores were:
• Semantic Accuracy and Correctness: en-
suring the translation conveys the exact
meaning of the original text without errors,
omissions, or additions.
• Fluency and Readability: check if the trans-
lation reads naturally, smoothly, and is easy
to understand in the target language.
• Linguistic and Stylistic Appropriateness:
ensuring the tone, style, and language fit the
purpose, audience, and cultural context of the
text.
A total of 13 experts, representing all 9 Indic
languages, participated in the proofreading exer-
cise. The expert distribution ensured that each lan-
guage had at least one expert, with four languages
having an additional expert to facilitate workload
sharing. Using a standardized evaluation frame-
work, each expert assessed sentence pairs based on
three criteria, assigning scores on a 5-point scale
(1 = lowest, 5 = highest). Comprehensive guide-
lines, accompanied by illustrative samples, were
provided to all experts to ensure consistency in
scoring.

--- Page 5 ---\n\nThe participating experts were native speak-
ers of their respective languages, with fluency
in English and formal education in their na-
tive languages.
To ensure consistency, experts’
scores were systematically recorded in spread-
sheets, which included sentence pairs and evalu-
ations based on the three criteria. We extend our
sincere gratitude to the experts listed below under
Acknowledgements, for generously volunteering
their time and expertise to support this research
endeavor.
3
Results
Table 3 presents the evaluation metrics for the
IndicMMLU-Pro dataset using back-translation
techniques.
The chrF++ (Popovi´c, 2017) and
BLEU (Papineni et al., 2002) scores are provided
for each of the nine Indic languages (Bengali, Gu-
jarati, Hindi, Kannada, Marathi, Punjabi, Tamil,
Telugu, and Urdu). These metrics assess the qual-
ity and accuracy of the translated content in the
IndicMMLU-Pro benchmark, providing insights
into the dataset’s linguistic fidelity across different
Indic languages.
Table 1 and 2 present the accuracy scores
(in percentages) of various pre-trained language
models evaluated on the IndicMMLU-Pro bench-
mark.
The benchmark covers nine major Indic
languages:
Bengali, Gujarati, Hindi, Kannada,
Marathi, Punjabi, Tamil, Telugu, and Urdu. The
scores reflect the models’ ability to handle diverse
linguistic challenges specific to Indic languages.
3.1
Overall Performance
Performance Range: The accuracy scores across
all models and languages now fall within a broader
range of 9.90% to 44.80%. This wider range re-
flects the significant performance differences be-
tween the newer, more advanced models (like
GPT-4o) and the previously evaluated models.
Model Comparison: GPT-4o consistently out-
performs all other models across all languages,
achieving the highest scores ranging from 38.46%
to 44.80%. GPT-4o mini follows as the second-
best performer with scores ranging from 25.75%
to 35.08%. Among the previously evaluated mod-
els, XLM-RoBERTa remains the top performer,
consistently outperforming other models across
most languages with scores ranging from 11.92%
to 13.16%.
Language-Model Variability: There is now a
much more pronounced variability in performance
across different languages and models. This sug-
gests that language-specific characteristics and
model architectures play significant roles in per-
formance outcomes.
3.2
Language-wise Performance
Breaking down the performance for each language
reveals interesting patterns:
• Hindi:
GPT-4o leads with 44.80%, fol-
lowed by GPT-4o mini (32.33%).
Among
other models, Navarasa (12.43%) and XLM-
RoBERTa (12.33%) perform best.
• Bengali:
GPT-4o achieves 44.38%, with
GPT-4o mini at 31.11%.
XLM-RoBERTa
(12.68%) and Navarasa (12.08%) lead among
other models.
• Telugu:
GPT-4o scores 41.34%, GPT-4o
mini 26.78%. XLM-RoBERTa (12.62%) out-
performs Navarasa (11.77%) and TamilL-
lama (11.53%).
• Marathi: GPT-4o reaches 42.20%, GPT-4o
mini 27.13%. RemBERT (12.93%) performs
best among earlier models, with Navarasa at
11.88% and MahaMarathi at 11.60%.
• Tamil:
GPT-4o mini shows strong per-
formance at 35.08%, close to GPT-4o’s
38.46%.
Navarasa (12.38%) slightly out-
performs XLM-RoBERTa (12.34%), with
TamilLlama at 11.54%.
• Gujarati: GPT-4o scores 41.77%, GPT-4o
mini 28.29%.
IndicBART (12.14%) and
RemBERT (12.13%) perform well among
earlier models.
• Urdu:
GPT-4o achieves 44.18%, GPT-4o
mini 31.13%.
XLM-RoBERTa (12.53%)
leads among other models.
• Kannada: GPT-4o scores 38.97%, GPT-4o
mini 25.75%. XLM-RoBERTa significantly
outperforms other models (13.16%) among
earlier models.
• Punjabi: GPT-4o reaches 40.60%, GPT-4o
mini 26.25%. XLM-RoBERTa (12.59%) per-
forms best among other models.

--- Page 6 ---\n\nLanguage
GPT-4o
GPT-4o mini
Llama-3.1-8B
IndicBART
IndicBERT
RemBERT
MuRIL
Hindi
44.80
32.33
18.61
11.21
10.78
11.41
10.87
Bengali
44.38
31.11
N/A
12.52
10.39
12.00
9.90
Punjabi
40.60
26.25
N/A
11.78
10.36
11.06
10.36
Marathi
42.20
27.13
N/A
11.65
10.59
12.93
11.79
Urdu
44.18
31.13
N/A
12.11
11.63
11.32
11.20
Gujarati
41.77
28.29
N/A
12.14
11.06
12.13
10.79
Telugu
41.34
26.78
N/A
12.05
11.36
10.20
9.96
Tamil
38.46
35.08
N/A
11.70
10.96
10.98
11.00
Kannada
38.97
25.75
N/A
11.51
11.71
10.87
10.62
Table 1: Performance comparison of language models on the IndicMMLU-Pro benchmark across nine Indic lan-
guages, including Indo-Aryan (Hindi, Bengali, Punjabi, Marathi, Urdu, and Gujarati) and Dravidian (Telugu,
Tamil, and Kannada) languages. Accuracy scores are shown as percentages. Models compared include GPT-4o,
GPT-4o mini, IndicBART, IndicBERT, RemBERT, MuRIL, and Llama-3.1-8B-Instruct.
Language
XLM-RoBERTa
Navarasa
Airavata
OpenHathi
TamilLlama
MahaMarathi
Hindi
12.33
12.43
11.60
11.65
-
-
Bengali
12.68
12.08
-
-
-
-
Punjabi
12.59
11.95
-
-
-
-
Marathi
12.57
11.88
-
-
-
11.60
Urdu
12.53
10.73
-
-
-
-
Gujarati
11.92
11.53
-
-
-
-
Telugu
12.62
11.77
-
-
11.53
-
Tamil
12.34
12.38
-
-
11.66
-
Kannada
13.16
11.88
-
-
-
-
Table 2: Comparison of language model performance across Indian languages, both Indo-Aryan (i.e., Hindi, Ben-
gali, Punjabi, Marathi, Urdu, and Gujarati) and Dravidan (i.e., Telegu, Tamil, and Kannada). Scores are shown for
Llama 3.1, Navarasa, Airavata, OpenHathi, TamilLlama, and MahaMarathi models where available.
3.2.1
Cross-linguistic Analysis
Indo-Aryan languages (Hindi, Bengali, Punjabi,
Gujarati, Urdu, Marathi) and Dravidian languages
(Kannada, Tamil, Telugu) exhibit distinct perfor-
mance patterns.
• Performance Patterns: GPT-4o and GPT-4o
mini consistently outperform all other models
across both language families.Among other
models, XLM-RoBERTa generally performs
best across both language families. Navarasa
shows competitive performance, particularly
for the Dravidian language
• Language-specific Models:
TamilLlama
and MahaMarathi show promise but fail to
surpass the performance of top multilingual
models like XLM-RoBERTa and Navarasa.
• Consistency:
GPT-4o and GPT-4o mini
demonstrate
relatively
consistent
perfor-
mance across different languages, suggest-
ing robust multilingual capabilities. Navarasa
also shows consistency, particularly among
Dravidian languages.
• Script-based Patterns: Languages using the
Devanagari script (Hindi, Marathi) exhibit
similar performance patterns, while Urdu
(using the Perso-Arabic script) shows more
varied performance.
• Performance Gap:
A significant perfor-
mance gap exists between GPT-4o/GPT-4o
mini and other models, highlighting the ad-
vantages of larger, more advanced models in
handling the complexities of Indic languages.
3.3
Dataset Quality Assessment
In order to heuristically assert the quality of Indic
language datasets, we convert the dataset from the
respective Indic language back to English again by
leveraging IndicTrans2 as in Section 2.1. The En-
glish translations are then scored by the following
metrics:
• chrF++ (Popovi´c, 2017) (threshold > 50%):
A language and token agnostic, character n-
gram F1 score. We use n=6, as it is the stan-
dard set in the chrF++ paper.

--- Page 7 ---\n\nLanguage
chrF++
BLEU
METEOR
TER
SacreBLEU
Hindi
78.06
0.59
0.56
42.27
59.07
Gujarati
77.67
0.58
0.55
43.09
58.28
Tamil
74.32
0.54
0.52
46.41
53.64
Table 3: Back-translation evaluation metrics for the IndicMMLU-Pro dataset for 3 Indic languages.
• BLEU (Papineni et al., 2002) (threshold >
25-30%): A score obtained by measuring the
precision of n-grams of the candidate trans-
lation compared to the reference translation,
with a brevity penalty to penalize short trans-
lations.
• METEOR
(Banerjee
and
Lavie,
2005)
(threshold = 50-60%): A metric that evalu-
ates translation quality by considering preci-
sion and recall, along with a harmonic mean
of unigram matches, with additional features
such as stemming and synonymy matching.
• TER (Snover et al., 2006) (threshold < 40-
50%): A score that measures the number of
edits required to change a system-generated
translation to exactly match a reference trans-
lation.
• SacreBLEU (Post, 2018) (threshold > 25-
30%): A variant of BLEU that ensures stan-
dard reference text processing and tokeniza-
tion.
Table 3 provides insights into the quality of the
IndicMMLU-Pro dataset through back-translation
evaluation metrics for three languages: Hindi, Gu-
jarati, and Tamil.
The metrics include chrF++,
BLEU, METEOR, TER, and SacreBLEU scores.
Hindi shows the highest overall quality with
a chrF++ score of 78.06, BLEU of 0.59, ME-
TEOR of 0.56, TER of 42.27, and SacreBLEU
of 59.07. Gujarati follows closely with very sim-
ilar scores: chrF++ of 77.67, BLEU of 0.58, ME-
TEOR of 0.55, TER of 43.09, and SacreBLEU
of 58.28. Tamil, while still demonstrating good
quality, shows slightly lower scores across all met-
rics: chrF++ of 74.32, BLEU of 0.54, METEOR
of 0.52, TER of 46.41, and SacreBLEU of 53.64.
The high chrF++ scores (above 74) for all three
languages indicate good overall translation qual-
ity and semantic preservation.
The BLEU and
SacreBLEU scores, ranging from 0.54 to 0.59 and
53.64 to 59.07 respectively, suggest reasonably
good translation quality, though there’s room for
improvement. The METEOR scores (0.52-0.56)
also indicate good semantic similarity between the
original and back-translated texts.
The Translation Error Rate (TER) scores, rang-
ing from 42.27 to 46.41, suggest that a moderate
amount of editing is required to match the ref-
erence translation, with Tamil requiring slightly
more editing than Hindi or Gujarati.
It is important to note that data for the other
six languages (Bengali, Punjabi, Kannada, Telugu,
Urdu, and Marathi) is missing from Table 2. This
limitation in the dataset quality assessment makes
it challenging to draw comprehensive conclusions
about the overall quality of the IndicMMLU-Pro
dataset across all nine languages.
In summary, the available metrics indicate good
translation quality for Hindi, Gujarati, and Tamil,
with Hindi showing the highest quality across all
metrics. However, the lack of data for the remain-
ing languages highlights the need for a more com-
prehensive evaluation of the entire dataset.
To better illustrate the meaning of chrF++
scores in practice, let’s examine sample transla-
tions for Hindi (highest score), Gujarati (middle
score), and Tamil (lowest score) as shown in
Figure 2, 3, 4 respectively.
Hindi (chrF++: 78.06): The chrF++ score for
Hindi is the best among the three languages in-
dicating a high structural and semantic similarity
between the original text and the back-translated
text.
Gujarati (chrF++:
77.67):
While slightly
lower, this score still represents a high-quality
translation with minor variations.
Tamil (chrF++: 74.32): This lower score might
reflect slight changes in word choice or structure,
but the core meaning is preserved.
These examples demonstrate that even with the
lowest chrF++ score in our dataset (74.32 for
Tamil), the translations maintain good semantic
fidelity.
The differences in scores often reflect

--- Page 8 ---\n\nOriginal
Hindi
Back-translated
A total of 30 players will play basketball at 
a park. There will be exactly 5 players on 
each team. Which statement correctly 
explains how to find the number of teams 
needed?
एक पाMर्क में कुल 30 Sखिलाड़ी बास्केटबॉल खेलेंगे। 
प्रत्येक टीम में ठीक 5 Sखिलाड़ी होंगे। कौन सा कथन 
सही ढंग से बताता है :कि आवश्यक टीमों की संख्या 
कैसे ज्ञात की जाए?
A total of 30 players will play basketball in 
a park. Each team will have exactly 5 
players. Which statement correctly states 
how to find the number of teams required?
Figure 2: The original text sample, its Hindi translation, and the corresponding back-translated text
Original
Gujarati
Back-translated
Which of the following is the body cavity 
that contains the pituitary gland?
નીચેનામાંથી કઈ શરીરની પોલાણ છે જેમાં કફોત્પાદક 
ગ્રંCથિ હોય છે?
Which of the following is the body cavity 
that contains the pituitary gland?
Figure 3: The original text sample, its Gujarati translation, and the corresponding back-translated text
Original
Tamil
Back-translated
What is the embryological origin of the 
hyoid bone?
Cஹைய்டு எலும்பின் கருப்3பொருள் 
1தோற்றம் என்ன?
What is the thematic appearance of the 
hyoid bone?
Figure 4: The original text sample, its Tamil translation, and the corresponding back-translated text
Language
Questions
Choices
Hindi
0.9109
0.9250
Bengali
0.9172
0.9251
Telugu
0.9193
0.9287
Marathi
0.9126
0.9242
Tamil
0.9194
0.9255
Gujarati
0.9164
0.9320
Urdu
0.9121
0.9302
Kannada
0.9149
0.9238
Punjabi
0.9177
0.9254
Table 4: Cosine similarity scores between LaBSE em-
beddings of IndicMMLU-Pro languages and English
MMLU-Pro for questions and multiple-choice options.
These scores are used as a measure of semantic sim-
ilarity, with higher values suggesting closer meaning
alignment across languages.
nuances in word choice, sentence structure, or
slight variations in conveying the same meaning,
rather than significant errors in translation. This
analysis supports our earlier observation that the
IndicMMLU-Pro dataset maintains good overall
translation quality across the evaluated languages.
Preliminary assessments of the other languages
(Bengali, Punjabi, Kannada, Telugu, Urdu, and
Marathi) suggest similar trends in translation qual-
ity, with chrF++ scores ranging from 73 to 79.
Complete metrics for these languages are being
compiled and will be included in future publica-
tions.
3.4
Cosine Similarity Scores
We evaluated the semantic similarity between In-
dic languages from the IndicMMLU-Pro dataset
and the English MMLU-Pro dataset using the
LaBSE (Language-agnostic BERT Sentence Em-
bedding) model. It loads both datasets and pro-
cesses all the samples from each. For each pair of
corresponding questions, it generates embeddings
for the questions and their multiple-choice options
using the LaBSE model.
The script then calculates cosine similarity be-
tween these embeddings to measure how seman-
tically similar Indic languages and their english
versions are. It computes two main metrics: av-
erage question similarity, and average choice sim-
ilarity. The question and choice similarities indi-
cate how close the meanings are between the two
languages. This analysis helps assess how accu-
rately Indic languages in the IndicMMLU-Pro rep-
resent the original English MMLU-Pro in terms
of meaning and structure, which is crucial for en-
suring the quality and consistency of multilingual
datasets in machine learning and natural language
processing tasks.
4
Related Work
The study of multilingual language models has
been significantly advanced by efforts to create
and utilize datasets that encompass a wide range
of languages. Indic languages, with their diverse
scripts and rich morphological structures, present
unique challenges and opportunities for multilin-
gual NLP research.
Multilingual datasets have been crucial in de-
veloping language models capable of understand-
ing and generating text in multiple languages. The
WikiAnn dataset, for instance, provides a valuable
resource for named entity recognition across many

--- Page 9 ---\n\nlanguages, including several Indic languages (Pan
et al., 2017). The IndicNLP Corpus (Kunchukut-
tan, 2020), developed as part of the IndicNLP Li-
brary, provides extensive monolingual corpora for
various Indic languages.
This dataset has been
instrumental in training and evaluating models
specifically designed for these languages. Indic-
Corp (Joshi et al., 2022), a large-scale dataset of
Indic languages, and the IndicNLPSuite(Kakwani
et al., 2020b), which includes pre-trained models
and linguistic resources, have further enhanced the
development of multilingual NLP models. These
resources have provided a solid foundation for var-
ious NLP tasks such as machine translation, text
classification, etc.
IndicGLUE(Kakwani et al., 2020c) is a compre-
hensive benchmark designed to evaluate the per-
formance of NLP models on a variety of tasks
across multiple Indic languages. It includes tasks
such as sentiment analysis, natural language infer-
ence, and question answering, making it a valuable
resource for assessing the capabilities of multilin-
gual models.
(Ahuja et al., 2023) introduce Megaverse, a
comprehensive benchmark designed to evaluate
large language models across a variety of lan-
guages, modalities, models, and tasks.
This
benchmark aims to provide a holistic assessment
of language models’ performance, emphasizing
their capabilities and limitations in handling di-
verse linguistic and contextual scenarios. Mega-
verse is instrumental in identifying the strengths
and weaknesses of current models and guiding fu-
ture improvements in multilingual and multimodal
language processing.
(Holtermann et al., 2024) developed MultiQ,
a benchmark aimed at evaluating the elementary
multilingual capabilities of large language mod-
els. MultiQ focuses on assessing basic language
understanding and generation tasks across multi-
ple languages, providing insights into the foun-
dational multilingual capabilities of these models.
This benchmark is critical for identifying gaps in
language model training and performance, partic-
ularly for less-represented languages.
(Aggarwal et al., 2022) introduce IndicXNLI,
a benchmark specifically designed to evaluate the
natural language inference capabilities of multi-
lingual models for Indian languages. This bench-
mark includes a diverse set of inference tasks, re-
flecting the linguistic richness and complexity of
Indic languages. IndicXNLI is crucial for advanc-
ing the understanding and processing of Indian
languages in NLP, providing a standard for eval-
uating inference models in this context.
(Kumar et al., 2022) develop the IndicNLG
benchmark, which provides multilingual datasets
for a variety of natural language generation (NLG)
tasks in Indic languages.
This benchmark ad-
dresses the unique challenges posed by the linguis-
tic diversity of Indic languages, offering datasets
for tasks such as machine translation, summariza-
tion, and text generation. IndicNLG is instrumen-
tal in improving the performance and capabilities
of NLG models for Indic languages, fostering ad-
vancements in multilingual NLP.
MMLU (Massively Multilingual Language Un-
derstanding) (Liang et al., 2020; Hu et al., 2020) is
a comprehensive benchmark designed to evaluate
the performance of language models across mul-
tiple languages and a wide range of tasks. This
benchmark has been instrumental in assessing the
capabilities of multilingual models and has pro-
vided insights into their strengths and limitations.
5
Key Findings and Implications of
IndicMMLU-Pro
IndicMMLU-Pro represents a significant step for-
ward in the development and evaluation of AI
models for Indic languages. Through this com-
prehensive benchmark, we have shed light on the
current capabilities and limitations of state-of-the-
art multilingual models in handling the linguistic
diversity and complexity of the Indian subconti-
nent. This section details implications based on
some of our key findings.
5.1
Performance Across Models
5.1.1
GPT-4o Dominance
GPT-4o consistently outperformed all other mod-
els across all languages, with accuracy scores
ranging from 38.46% to 44.80%. This suggests
that large, advanced language models have signif-
icant potential for handling Indic languages.
5.1.2
Performance Tiers
A clear hierarchy emerged among the models:
• Elite Tier: GPT-4o
• Advanced Tier: GPT-4o mini
• Specialized
Tier:
XLM-RoBERTa,
Navarasa, and other specialized models

--- Page 10 ---\n\n• Foundation
Tier:
Earlier
models
like
IndicBERT,
IndicBART,
RemBERT,
and
MuRIL
5.1.3
Specialized vs. General Models
While GPT-4o and GPT-4o mini showed supe-
rior performance, specialized models like XLM-
RoBERTa
and
Navarasa
consistently
outper-
formed other models in the foundation tier. This
highlights the importance of both scale and spe-
cialized training for Indic languages.
5.2
Language-Specific Insights
5.2.1
Performance Variability
Significant variability in model performance was
observed across different Indic languages, empha-
sizing the need for language-specific approaches
in NLP.
5.2.2
Script and Language Family Impact
Languages using similar scripts (e.g., Devanagari
for Hindi and Marathi) showed similar perfor-
mance patterns. Urdu, using a different script, ex-
hibited more varied performance across models.
5.2.3
Indo-Aryan vs. Dravidian Languages
While performance varied across both language
families, some models showed more consistency
in Dravidian languages, suggesting potential dif-
ferences in how models handle these distinct lan-
guage groups.
5.3
Dataset and Evaluation Quality
5.3.1
Translation Quality
Back-translation evaluation metrics for Hindi, Gu-
jarati, and Tamil demonstrated good overall trans-
lation quality and semantic preservation, with
chrF++ scores above 74 for all three languages.
5.3.2
Metric Discrepancies
Differences between chrF++ and BLEU scores
suggest that while meaning is generally preserved,
there may be variations in phrasing and structure
compared to the original English text.
5.3.3
Comprehensive Evaluation Need
The lack of evaluation metrics for six out of nine
languages highlights the need for more thorough
assessment across all included Indic languages.
5.4
Methodological Insights
5.4.1
Benchmark Design
The
adaptation
of
MMLU-Pro
to
create
IndicMMLU-Pro
demonstrates
a
successful
approach to developing comprehensive, multi-
task benchmarks for specific language groups.
5.4.2
Translation Approach
The use of IndicTrans2 for dataset creation, com-
bined with rigorous quality assurance processes,
provides a template for developing high-quality
multilingual datasets.
5.4.3
Evaluation Metrics
The use of multiple metrics (chrF++, BLEU, ME-
TEOR, TER, SacreBLEU) for assessing transla-
tion quality offers a more nuanced understanding
of dataset quality.
These findings and implications highlight the
significant advancements made by IndicMMLU-
Pro in evaluating and understanding the perfor-
mance of language models across Indic languages,
while also pointing to crucial areas for future re-
search and development in multilingual NLP.
5.5
Future Directions
Based on our findings, we propose several key ar-
eas for future research and development:
• Data Collection: There is a pressing need
for more high-quality, diverse datasets across
all Indic languages, particularly for low-
resource languages. This will in turn enable
more robust model training and evaluation.
• Model
Development:
Future
research
should focus on developing models that can
better handle the unique linguistic features
of Indic languages, including their complex
morphology and script diversity. This may
involve innovative architecture designs or
novel pre-training techniques.
• Cross-lingual Transfer:
Exploring tech-
niques to improve knowledge transfer be-
tween related Indic languages will help boost
performance, especially for low-resource lan-
guages.
This could involve leveraging lin-
guistic similarities or developing more effec-
tive multilingual training strategies.
• Task-specific
Fine-tuning:
Developing
strategies for effective fine-tuning of large

--- Page 11 ---\n\nmultilingual models on specific language
tasks lead to significant performance im-
provements (Balne et al., 2024). Thus future
work in this area may include investigating
optimal fine-tuning techniques or developing
Indic-specific pre-training tasks.
• Evaluation Metrics: Further refinement of
evaluation metrics to account for the linguis-
tic and cultural nuances of Indic languages is
necessary for more accurate performance as-
sessment. Existing metrics often overlook the
linguistic and cultural nuances inherent to In-
dic languages.
IndicMMLU-Pro sets a new standard for eval-
uating AI models in the context of Indic lan-
guages.
By providing a comprehensive, multi-
task, and multilingual benchmark, it enables re-
searchers and developers to assess and improve the
capabilities of their models across a wide range of
Indic languages and domains. As the field of NLP
continues to advance, we hope that IndicMMLU-
Pro will catalyze increased research and develop-
ment of technologies based on Indic languages.
This benchmark not only highlights the current
state of the art but also points the way forward
for creating more linguistically diverse, culturally
sensitive, and capable AI systems that can serve
the vast and diverse population of the Indian sub-
continent.
To foster a more comprehensive understand-
ing of Indic language models, it is essential to
intentionally integrate multi-disciplinary perspec-
tives into engineering and science workstreams
(Bhaduri et al., 2024b). Collaborations between
engineers, scientists, and experts from social sci-
ences can provide nuanced insights into the com-
plex interplay between language, culture, and
technology (Mackenzie et al., 2024). By embrac-
ing interdisciplinary approaches and refining eval-
uation metrics, we can work towards a more in-
clusive and accurate assessment of Indic language
models, ultimately driving progress in natural lan-
guage processing for diverse languages and com-
munities.
In conclusion,
while significant challenges
remain in the field of Indic language NLP,
IndicMMLU-Pro provides a robust framework for
measuring progress and guiding future research
efforts. As we continue to push the boundaries
of what’s possible in multilingual AI, benchmarks
like IndicMMLU-Pro will play a crucial role in en-
suring that technological advancements benefit all
language communities, fostering greater inclusiv-
ity and accessibility in the digital age.
6
Acknowledgements
We extend our deepest gratitude to the experts who
volunteered their time and effort to evaluate our
dataset.
Unfortunately, Indic languages are of-
ten neglected in the development and evaluation
of Large Language Models, making initiatives like
ours reliant on the generosity and expertise of indi-
viduals like those listed below. The list of experts
and the language they reviewed are:
• Telugu Experts: Dushyanth Reddy and Sai
Krishna Bolla
• Tamil Expert: Veeramanohar Avudaiappan
• Hindi Expert: Ojasmitha Pedirappagari
• Gujarati Expert: Ashwini Thosar
• Punjabi Expert: Shivan Bhatia
• Marathi
Experts:
Sameer
Jadhav
and
Nityanand Bhadra
• Kannada Expert: Nikhil Ragunath
• Bengali Experts: Sounak Datta and Nirjhar
Barua
• Urdu Experts: Md Mahtab and Risha Fatema
Expert feedback has significantly enhanced the
quality of our dataset, and we are grateful for their
dedication to promoting Indic languages in the
global LLM community.
References
Divyanshu Aggarwal,
Vivek Gupta,
and Anoop
Kunchukuttan. 2022.
Indicxnli: Evaluating mul-
tilingual inference for indian languages.
arXiv
preprint arXiv:2204.08776.
Sanchit Ahuja, Divyanshu Aggarwal, Varun Gumma,
Ishaan Watts, Ashutosh Sathe, Millicent Ochieng,
Rishav Hada, Prachi Jain, Maxamed Axmed, Ka-
lika Bali, et al. 2023. Megaverse: Benchmarking
large language models across languages, modalities,
models and tasks. arXiv preprint arXiv:2311.07463.

--- Page 12 ---\n\nTejaswini Ananthanarayana, Nikunj Kotecha, Priyan-
shu
Srivastava,
Lipisha
Chaudhary,
Nicholas
Wilkins, and Ifeoma Nwogu. 2021a.
Dynamic
cross-feature fusion for american sign language
translation. In 2021 16th IEEE International Con-
ference on Automatic Face and Gesture Recognition
(FG 2021), pages 1–8. IEEE.
Tejaswini Ananthanarayana,
Priyanshu Srivastava,
Akash Chintha, Akhil Santha, Brian Landy, Joseph
Panaro, Andre Webster, Nikunj Kotecha, Shagan
Sah, Thomastine Sarchet, et al. 2021b. Deep learn-
ing methods for sign language translation.
ACM
Transactions on Accessible Computing (TACCESS),
14(4):1–30.
Abhinand Balachandran. 2023. Tamil-llama: A new
tamil language model based on llama 2.
arXiv
preprint arXiv:2311.05845.
Charith Chandra Sai Balne, Sreyoshi Bhaduri, Ta-
moghna Roy, Vinija Jain, and Aman Chadha. 2024.
Parameter efficient fine tuning:
A comprehen-
sive analysis across applications.
arXiv preprint
arXiv:2404.13506.
Satanjeev Banerjee and Alon Lavie. 2005. Meteor: An
automatic metric for mt evaluation with improved
correlation with human judgments. In Proceedings
of the acl workshop on intrinsic and extrinsic evalu-
ation measures for machine translation and/or sum-
marization, pages 65–72.
Rewina Bedemariam, Natalie Perez, Sreyoshi Bhaduri,
Satya Kapoor, Alex Gil, Elizabeth Conjar, Ikkei
Itoku, David Theil, Aman Chadha, and Naumaan
Nayyar. 2025. Potential and perils of large language
models as judges of unstructured textual data. arXiv
preprint arXiv:2501.08167.
Sreyoshi Bhaduri, Satya Kapoor, Alex Gil, Anshul
Mittal, and Rutu Mulkar. 2024a.
Reconciling
methodological paradigms: Employing large lan-
guage models as novice qualitative research assis-
tants in talent management research. arXiv preprint
arXiv:2408.11043.
Sreyoshi Bhaduri, Kenneth Ohnemus, Jess Black-
burn, Anshul Mittal, Yan Dong, Savannah Lafer-
riere, Robert Pulvermacher, Marina Dias, Alex Gil,
Shahriar Sadighi, et al. 2024b. (multi-disciplinary)
teamwork makes the (real) dream work:
Prag-
matic recommendations from industry for engineer-
ing classrooms.
Hyung Won Chung, Thibault Févry, Henry Tsai,
Melvin Johnson, and Sebastian Ruder. 2020.
Re-
thinking embedding coupling in pre-trained lan-
guage models. Preprint, arXiv:2010.12821.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020.
Unsuper-
vised cross-lingual representation learning at scale.
Preprint, arXiv:1911.02116.
Raj Dabre, Himani Shrotriya, Anoop Kunchukuttan,
Ratish Puduppully, Mitesh M. Khapra, and Pratyush
Kumar. 2021.
Indicbart:
A pre-trained model
for natural language generation of indic languages.
Preprint, arXiv:2109.02903.
Dipto Das, Shion Guha, Jed R Brubaker, and Bryan
Semaan. 2024.
The“colonial impulse" of natural
language processing: An audit of bengali sentiment
analysis tools and their identity-based biases.
In
Proceedings of the CHI Conference on Human Fac-
tors in Computing Systems, pages 1–18.
Jay Gala, Pranjal A. Chitale, Raghavan AK, Varun
Gumma, Sumanth Doddapaneni, Aswanth Kumar,
Janki Nawale, Anupama Sujatha, Ratish Pudup-
pully, Vivek Raghavan, Pratyush Kumar, Mitesh M.
Khapra, Raj Dabre, and Anoop Kunchukuttan. 2023.
Indictrans2: Towards high-quality and accessible
machine translation models for all 22 scheduled in-
dian languages. Preprint, arXiv:2305.16307.
Jay Gala, Thanmay Jayakumar, Jaavid Aktar Hu-
sain, Mohammed Safi Ur Rahman Khan, Diptesh
Kanojia, Ratish Puduppully, Mitesh M Khapra, Raj
Dabre, Rudra Murthy, Anoop Kunchukuttan, et al.
2024. Airavata: Introducing hindi instruction-tuned
llm. arXiv preprint arXiv:2401.15006.
Carolin Holtermann, Paul Röttger, Timm Dill, and
Anne Lauscher. 2024.
Evaluating the elementary
multilingual capabilities of large language models
with multiq. arXiv preprint arXiv:2403.03814.
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Gra-
ham Neubig, Orhan Firat, and Melvin Johnson.
2020. Xtreme: A massively multilingual multi-task
benchmark for evaluating cross-lingual generaliza-
tion. arXiv preprint arXiv:2003.11080.
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika
Bali, and Monojit Choudhury. 2020. The state and
fate of linguistic diversity and inclusion in the nlp
world. arXiv preprint arXiv:2004.09095.
Sachin Joshi et al. 2022.
Indiccorp: A large-scale
dataset for indic languages. In Proceedings of the
2022 Conference on Empirical Methods in Natural
Language Processing (EMNLP).
Divyanshu Kakwani, Anoop Kunchukuttan, Satish
Golla, Gokul N.C., Avik Bhattacharyya, Mitesh M.
Khapra, and Pratyush Kumar. 2020a.
IndicNLP-
Suite:
Monolingual Corpora, Evaluation Bench-
marks and Pre-trained Multilingual Language Mod-
els for Indian Languages. In Findings of EMNLP.
Divyanshu Kakwani, Anoop Kunchukuttan, Raj D
Shah, et al. 2020b. Indicnlpsuite: Monolingual cor-
pora, evaluation benchmarks and pre-trained multi-
lingual language models for indian languages. arXiv
preprint arXiv:2004.09095.
Divyanshu Kakwani et al. 2020c. Indicglue: A bench-
mark for evaluating indic language understanding.
arXiv preprint arXiv:2004.09095.

--- Page 13 ---\n\nSimran Khanuja, Diksha Bansal, Sarvesh Mehtani,
Savya
Khosla,
Atreyee
Dey,
Balaji
Gopalan,
Dilip Kumar Margam, Pooja Aggarwal, Rajiv Teja
Nagipogu, Shachi Dave, Shruti Gupta, Subhash
Chandra Bose Gali, Vish Subramanian, and Partha
Talukdar. 2021. Muril: Multilingual representations
for indian languages. Preprint, arXiv:2103.10730.
Sankalp KJ, Vinija Jain, Sreyoshi Bhaduri, Tamoghna
Roy, and Aman Chadha. 2024a. Decoding the di-
versity: A review of the indic ai research landscape.
arXiv preprint arXiv:2406.09559.
Sankalp
KJ,
Ashutosh
Kumar,
Laxmaan
Balaji,
Nikunj Kotecha, Vinija Jain, Aman Chadha, and
Sreyoshi Bhaduri. 2024b.
IndicMMLU-Pro:
A
Comprehensive Benchmark for Evaluating Mul-
tilingual
AI
Models
across
Indic
Languages.
https://huggingface.co/datasets/
LinguaLift/IndicMMLU-Pro.
Accessed:
2024-07-12.
Aman Kumar, Himani Shrotriya, Prachi Sahu, Raj
Dabre, Ratish Puduppully, Anoop Kunchukuttan,
Amogh Mishra, Mitesh M Khapra, and Pratyush
Kumar. 2022.
Indicnlg benchmark: Multilingual
datasets for diverse nlg tasks in indic languages.
arXiv preprint arXiv:2203.05437.
Anoop Kunchukuttan. 2020. The indicnlp library.
James Lane. 2019. The 10 most spoken languages in
the world. Babbel Magazine, 6(09).
Yaobo Liang et al. 2020. Xglue: A new benchmark
dataset for cross-lingual pre-training, understanding
and generation. arXiv preprint arXiv:2004.01401.
Tammy Mackenzie, Leslie Salgado, Sreyoshi Bhaduri,
Victoria Kuketz, Solenne Savoia, and Lilianny Vir-
guez. 2024.
Beyond the algorithm: Empowering
ai practitioners through liberal education. In 2024
ASEE Annual Conference & Exposition.
Mounika
Marreddy,
Subba
Reddy
Oota,
Lak-
shmi Sireesha Vakada, Venkata Charan Chinni, and
Radhika Mamidi. 2022. Am i a resource-poor lan-
guage? data sets, embeddings, models and analysis
for four different nlp tasks in telugu language. ACM
Transactions on Asian and Low-Resource Language
Information Processing, 22(1):1–34.
Xiaoman Pan, Boliang Zhang, Jonathan May, Joel
Nothman, Kevin Knight, and Heng Ji. 2017. Cross-
lingual name tagging and linking for 282 languages.
In Proceedings of the 55th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 1946–1958.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei
jing Zhu. 2002. Bleu: a method for automatic eval-
uation of machine translation.
Maja Popovi´c. 2017. chrF++: words helping charac-
ter n-grams.
In Proceedings of the Second Con-
ference on Machine Translation, pages 612–618,
Copenhagen, Denmark. Association for Computa-
tional Linguistics.
Matt Post. 2018. A call for clarity in reporting bleu
scores. arXiv preprint arXiv:1804.08771.
Matthew Snover, Bonnie Dorr, Richard Schwartz, Lin-
nea Micciulla, and John Makhoul. 2006. A study
of translation edit rate with targeted human annota-
tion. In Proceedings of the 7th Conference of the
Association for Machine Translation in the Ameri-
cas: Technical Papers, pages 223–231.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng
Ni, Abhranil Chandra, Shiguang Guo, Weiming
Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle
Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi
Fan, Xiang Yue, and Wenhu Chen. 2024. Mmlu-
pro:
A more robust and challenging multi-task
language understanding benchmark.
Preprint,
arXiv:2406.01574.
7
Appendix
7.1
Choice of Models
The selection of models for our benchmark eval-
uation was based on their relevance to Indic lan-
guages, their prominence in multilingual NLP re-
search, and their potential to handle the diverse
linguistic features of Indic languages. Here’s a de-
tailed explanation of our choices:
• GPT-4o:
A highly advanced multimodal
model that offers improved speed and cost-
effectiveness compared to GPT-4 Turbo,
while also featuring enhanced vision capa-
bilities. With its 128K context window and
knowledge cutoff in October 2023, GPT-
4o represents the cutting edge in large lan-
guage models, making it an excellent candi-
date for benchmarking across diverse Indic
languages.
• GPT-4o-mini:
Designed as a more cost-
efficient alternative to larger models, GPT-
4o-mini offers a balance between perfor-
mance and resource utilization. Despite its
smaller size, it outperforms GPT-3.5 Turbo
in intelligence while maintaining lower costs.
Its inclusion in our benchmark allows us to
assess the trade-offs between model size, per-
formance, and efficiency in processing Indic
languages.
• IndicBERT: A transformer-based multilin-
gual model specifically pre-trained on 12
major Indian languages.
Developed by

--- Page 14 ---\n\nAI4Bharat, IndicBERT is designed to cap-
ture the nuances of Indic languages through
its training on a large corpus of Indian lan-
guage text. Its inclusion in our benchmark is
crucial for evaluating performance on tasks
that require a deep understanding of Indian
language structures and semantics.
• IndicBART: A sequence-to-sequence model
tailored for Indian languages, IndicBART ex-
tends the capabilities of mBART by incor-
porating additional pre-training on Indic lan-
guage corpora. It excels in generation tasks
such as summarization, translation, and text
completion across multiple Indian languages.
Its inclusion allows us to assess performance
on more complex, generative NLP tasks spe-
cific to Indic languages.
• RemBERT: Developed by Google Research,
RemBERT (Rebalanced Multilingual BERT)
is an advanced multilingual model that ad-
dresses the limitations of previous multilin-
gual models. It uses a novel rebalancing tech-
nique during pre-training to improve perfor-
mance across a wide range of languages, in-
cluding low-resource ones. RemBERT’s in-
clusion in our benchmark provides a strong
baseline for assessing how well general mul-
tilingual models perform on Indic language
tasks compared to Indic-specific models.
• MuRIL: (Multilingual Representations for
Indian Languages): Developed by Google
Research India, MuRIL is specifically de-
signed to address the unique challenges of In-
dian languages. It’s trained on significantly
larger amounts of Indian language data com-
pared to general multilingual models, cov-
ering 17 Indian languages including low-
resource ones. MuRIL’s architecture incor-
porates techniques to handle the linguistic di-
versity and script complexity of Indian lan-
guages, making it a crucial benchmark for
evaluating specialized Indic language perfor-
mance.
• XLM-RoBERTa:
A large-scale multilin-
gual model trained on 100 languages, XLM-
RoBERTa represents a significant advance-
ment in cross-lingual language understand-
ing.
Developed by Facebook AI, it uses a
self-supervised learning approach on a vast
amount of web-crawled data. Its inclusion
in our benchmark allows us to assess how
well a general multilingual model, trained
on a diverse set of languages including In-
dic ones, performs on specific Indic language
tasks compared to models with a more fo-
cused Indic language training.
• OpenHathi: An open-source large language
model focused primarily on Hindi and other
Indian languages. Developed as part of an
initiative to create freely accessible AI re-
sources for Indic languages, OpenHathi is
trained on a diverse corpus of Indian lan-
guage texts, including literature, news, and
web content.
Its inclusion in our bench-
mark allows us to evaluate the performance
of community-driven, open-source efforts in
Indic language modeling, particularly for
Hindi, and compare it with proprietary and
general multilingual models.
• Airavata: Developed by AI4Bharat, Aira-
vata is a specialized large language model fo-
cused on Hindi and other Indian languages.
It represents a significant effort in creating
instruction-tuned models specifically for In-
dic languages. Trained on a diverse corpus
of Hindi text and fine-tuned on carefully cu-
rated instruction datasets, Airavata aims to
understand and generate contextually appro-
priate responses in Hindi. Its inclusion in our
benchmark allows us to evaluate the effec-
tiveness of language-specific instruction tun-
ing for Indic languages, particularly in tasks
requiring a nuanced understanding of cultural
and linguistic contexts unique to Hindi.
• TamilLlama: A pioneering language model
specifically designed for Tamil, one of the
classical languages of India. Developed by
a team of researchers and language enthusi-
asts, TamilLlama is built upon the LLaMA
architecture but fine-tuned extensively on a
large corpus of Tamil text.
It incorporates
unique features to handle the agglutinative
nature of Tamil and its complex morphology.
By including TamilLlama in our benchmark,
we aim to assess the advantages of highly
specialized, language-specific models in cap-
turing the intricacies of individual Indic lan-
guages, particularly for tasks that require a

--- Page 15 ---\n\ndeep understanding of Tamil linguistic struc-
tures and cultural nuances.
7.2
Model Output & Evaluation
• IndicBERT: The IndicBERT model, when
used
with
AutoModelForMultipleChoice,
outputs logits for each option in a multiple-
choice question. These logits represent the
model’s confidence scores for each option.
The model produces logits for each option.
torch.argmax(logits, dim=1) selects the index
of the option with the highest logit (i.e., the
model’s predicted answer).
This index is
converted to a letter (A, B, C, D) using the
index_to_letter dictionary.
The predicted
answer (letter) is directly compared with the
correct answer.
• IndicBART: The IndicBART model is be-
ing loaded with AutoModelForSeq2SeqLM
framework to construct input texts by com-
bining the question with each of its options in
the format: ’Question: <question> Answer:
<option>’. These input texts are encoded into
a format that the model can process.
The
model generates responses for each encoded
input text, effectively simulating an answer
for each option. A scoring heuristic, such as
the length of the generated response, is then
applied to determine the relevance or quality
of each simulated answer. The option with
the highest score is selected as the model’s
predicted answer. This method leverages the
model’s ability to generate coherent and con-
textually appropriate responses, allowing it to
adapt to different questions and options ef-
fectively. It iterates through all questions, ap-
plies this process, and calculates the accuracy
by comparing predicted answers with the cor-
rect ones, thus evaluating the model’s perfor-
mance in handling multiple-choice questions
across various languages.
• MURIL: The MURIL (Multilingual Repre-
sentations for Indian Languages) model is
being used for sequence classification. The
model’s output is a single logit value for
each question-option pair, representing the
model’s confidence or relevance score for
that pair. The evaluation process works as
follows: For each question, the script passes
the question text paired with each option to
the model separately. The model produces a
score for each pair. These scores are collected
for all options of a question. The option with
the highest score is selected as the predicted
answer. This approach assumes that the op-
tion most relevant or coherent with the ques-
tion (as determined by the model’s score) is
likely to be the correct answer. While this
method can work for some types of ques-
tions, it’s not the standard way to use MURIL
for multiple-choice questions. MURIL is pri-
marily designed for tasks like text classifi-
cation, not specifically for multiple-choice
question answering. A more appropriate ap-
proach would be to fine-tune MURIL on a
multiple-choice QA task, or to use a model
specifically designed for this purpose. The
current method might work to some extent
due to MURIL’s pretraining on diverse tasks,
but it may not be as accurate or reliable
as a properly fine-tuned model for multiple-
choice questions.
• RemBERT: The RemBERT model, which
is designed for multiple-choice tasks, is be-
ing used.
The model’s output is a set of
logits, one for each option in the multiple-
choice question. These logits represent the
model’s confidence scores for each option.
The evaluation process works as follows: For
each question, the script encodes the ques-
tion paired with each option and passes this
to the model. The model then outputs log-
its for all options simultaneously. The op-
tion with the highest logit score is selected
as the predicted answer.
This approach is
correct and appropriate for multiple-choice
question-answering tasks, as it allows the
model to consider all options together in con-
text, rather than evaluating them indepen-
dently. The model has been trained to under-
stand the relationship between the question,
the correct answer, and the distractors, mak-
ing it well-suited for this type of task. This
method of using RemBERT for multiple-
choice questions is a standard and effective
approach in natural language processing for
question-answering tasks.
• XLM-RoBERTa:
The
XLM-RoBERTa
model is being used for sequence classi-
fication.
The model’s output is a single
logit value for each question-option pair,

--- Page 16 ---\n\nHindi
Bengali
Telugu
Marathi
Tamil
Gujarati
Urdu
Kannada
Punjabi
Language
9
14
19
24
29
34
39
44
49
54
59
64
69
74
79
84
89
94
99
Accuracy in %
Accuracy of Different Models Across Languages
IndicBART
IndicBERT
RemBERT
MuRIL
XLM-RoBERTa
Navarasa
GPT-4o
GPT-4o mini
Llama-3.1-8B-Instruct
Figure 5: Model Accuracy Across Different Languages
Gujarati
Punjabi
Hindi
Urdu
Telugu
Kannada
Tamil
Marathi
Bengali
0
25
50
75
100
125
150
175
200
Average Count 
152.52
153.47
159.67
157.1
158.09
160.91
169.08
157.87
157
34.5
34.39
36.91
35.59
37.13
38.4
41.83
36.5
36.49
42.28
51.28
51.73
56.34
34.93
33.32
34.83
38.41
40.04
6.46
7.36
7.44
8.24
5.59
5.43
5.6
6
6.14
Dataset Attributes By Language
Avg # Question Tokens
Avg # Option Tokens
Avg # Question Words
Avg # Option Words
Figure 6: Average Question and Option Lengths in #
Words and # Tokens
representing the model’s relevance or com-
patibility score for that pair. The evaluation
process works as follows: For each question,
the script passes the question text paired
with each option to the model separately.
The model produces a score for each pair.
These scores are collected for all options
of a question. The option with the highest
score is selected as the predicted answer.
This approach assumes that the option most
relevant or coherent with the question (as
determined by the model’s score) is likely to
be the correct answer. While this method can
work to some extent, it’s not the optimal way
to use XLM-RoBERTa for multiple-choice
questions.
XLM-RoBERTa is primarily
designed for tasks like text classification or
sequence pair classification, not specifically
for multiple-choice question answering.
A
more appropriate approach would be to fine-
tune XLM-RoBERTa on a multiple-choice
QA task, or to use a model architecture
specifically
designed
for
multiple-choice
tasks, which would consider all options
simultaneously rather than in pairs.
• Airavata We evaluate the performance of
the Airavata language model on the Hindi
subset of the IndicMMLU-Pro dataset.
It
loads a specified model using the Hugging
Face transformers library, and then processes
multiple-choice questions from the dataset.

--- Page 17 ---\n\nFor each question, it creates a prompt in a
chat format, feeds it to the model, and com-
pares the model’s single-token prediction to
the correct answer. The script calculates the
overall accuracy of the model’s predictions
across all questions in the dataset. Finally,
it saves this accuracy score to a text file and
prints it to the console, providing a quanti-
tative measure of the model’s capability in
understanding and answering Hindi multiple-
choice questions.
8
Additional Data Samples
To further illustrate the performance of the ma-
chine translation workflow, we provide examples
of translations and back-translations in three dif-
ferent languages: Hindi, Gujarati, and Tamil. Fig-
ure 2 showcases the original text sample, its trans-
lation into Hindi, and the corresponding back-
translated text, demonstrating the transformation
and consistency of the translation process. For ad-
ditional insights, Figure 7, 8, 9 includes a broader
set of examples across Hindi, Gujarati, and Tamil,
highlighting the system’s ability to handle linguis-
tic diversity and maintain semantic fidelity across
these languages. These examples emphasize the
efficacy and robustness of the translation pipeline
in preserving the original meaning during both for-
ward and reverse translation.

--- Page 18 ---\n\nOriginal
Hindi
Back-translated
Say the pupil of your eye has a diameter of 
5 mm and you have a telescope with an 
aperture of 50 cm. How much more light 
can the telescope gather than your eye?
A refracting telescope consists of two 
converging lenses separated by 100 cm. 
The eye-piece lens has a focal length of 
20 cm. The angular magnification of the 
telescope is
Where do most short-period comets come 
from and how do we know?
मान लीजिए vकि आपकी आंख की पुतली का व्यास 5 
sमिमी है और आपके पास 50 सेमी के छिद्र के साथ 
एक दूरबीन है I दूरबीन आपकी आंख की तुलना में 
vकितना अfधिक प्रकाश एकत्र कर सकती है?
Suppose your pupil is 5 mm in diameter 
and you have a telescope with a 50 cm 
aperture. How much more light can the 
telescope collect than your eye?
A refracting telescope has two 
converging lenses separated by 100 cm. 
The focal length of the I-piece lens is 20 
cm. The angular magnification of the 
telescope is
Where do most short-period comets 
come from and how do we know?
अfधिकांश अल्पका लिक धूमकेतु कहाँ से आते हैं और 
हम कैसे जानते हैं?
एक अपवÓर्तक दूरबीन में दो अÉभिसारी लेंस होते हैं जो 
100 सेमी से अलग होते हैंI आ´ई-पीस लेंस की 
फोकल लंबा´ई 20 सेमी होती हैI दूरबीन का कोणीय 
आवÖर्धन है
Figure 7: Additional examples showcasing the machine translation workflow, including the original text samples,
their Hindi translations, and the corresponding back-translated texts.
Original
Gujarati
Back-translated
Say the pupil of your eye has a diameter of 
5 mm and you have a telescope with an 
aperture of 50 cm. How much more light 
can the telescope gather than your eye?
A refracting telescope consists of two 
converging lenses separated by 100 cm. 
The eye-piece lens has a focal length of 
20 cm. The angular magnification of the 
telescope is
Where do most short-period comets come 
from and how do we know?
ધારો કે તમારી આંખની પાંખડીનો વ્યાસ 5 મીમી છે અને 
તમારી પાસે 50 સે. મી. ની nછિદ્રવાળી દૂરબીન છે. 
ટેnલિસ્કોપ તમારી આંખ કરતાં કેટલો વધુ પ્રકાશ એકnત્રિત 
કરી શકે છે?
Suppose your eyelid is 5 mm in diameter 
and you have a telescope with a 50 cm 
aperture. How much more light can the 
telescope collect than your eye?
A refracting telescope has two 
converging lenses separated by 100 cm. 
The lens of the eyepiece has a focal 
length of 20 cm. The angular 
magnification of the telescope is
Where do most short-period comets 
come from and how do we know?
મોટાભાગના ટૂંકા ગાળાના ધૂમકેતુઓ ક્યાંથી આવે છે અને 
આપણે કેવી રીતે જાણી શકીએ?
રીફ્રેãâક્ટિંગ ટેnલિસ્કોપમાં બે કન્વáÐર્જિંગ લેન્સ હોય છે જે 
100 સે. મી. દ્વારા અલગ પડે છે. આંખના ટુકડાના 
લેન્સની ફોકલ લંબાઈ 20 સે. મી. હોય છે. 
ટેnલિસ્કોપનું કોણીય nવિસ્તૃતીકરણ છે
Figure 8: Additional examples showcasing the machine translation workflow, including the original text samples,
their Gujarati translations, and the corresponding back-translated texts.
Original
Tamil
Back-translated
Say the pupil of your eye has a diameter of 
5 mm and you have a telescope with an 
aperture of 50 cm. How much more light 
can the telescope gather than your eye?
A refracting telescope consists of two 
converging lenses separated by 100 cm. 
The eye-piece lens has a focal length of 
20 cm. The angular magnification of the 
telescope is
Where do most short-period comets come 
from and how do we know?
உங்கள் கண்ணின் புறணி 5 மிமீ 
விட்டம் கொண்டதாகவும், உங்களிடம் 
50 செமீ துxளை கொண்ட 
தொxலைvநோக்கி இருப்பதாகவும் 
xவைத்துக்கொள்vவோம். உங்கள் 
கண்xணை விட தொxலைvநோக்கி 
எவ்வளவு அதிக ஒளிxயை vசேகரிக்க 
முடியும்?
Suppose your eyelid is 5 mm in diameter 
and you have a telescope with a 50 cm 
aperture. How much more light can the 
telescope collect than your eye?
A refractive telescope consists of two 
merging lenses separated by 100 cm. 
The eye-piece lens has a focal length of 
20 cm. The telescope's angular 
magnification is.
Where do most short-period comets 
come from, and how do we know?
பெரும்பாலான குறுகிய கால 
வால்மீன்கள் எங்கிருந்து 
வருகின்றன, நமக்கு எப்படித் 
தெரியும்?
ஒரு ஒளிவிலகல் தொxலைvநோக்கி 
100 செமீ பிரிக்கப்பட்ட இரண்டு 
ஒன்றிxணைக்கும் லென்ஸ்கxளைக் 
கொண்டுள்ளது. கண்-துண்டு 
லென்ஸ் 20 செமீ குவிய நீளம் 
கொண்டது. தொxலைvநோக்கியின் 
vகோண உருப்பெருக்கம்
Figure 9: Additional examples showcasing the machine translation workflow, including the original text samples,
their Tamil translations, and the corresponding back-translated texts.
\n```\n