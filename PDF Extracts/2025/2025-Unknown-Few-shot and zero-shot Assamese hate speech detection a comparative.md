---
title: "2025-Nath-Few-shot and zero-shot Assamese hate speech detection a comparative - PDF Extract"
source_pdf: "2025-Nath-Few-shot and zero-shot Assamese hate speech detection a comparative.pdf"
pages: 13
extracted_at: "2026-02-13T10:43:55.438685"
---

# PDF Extract: 2025-Nath-Few-shot and zero-shot Assamese hate speech detection a comparative

**Source PDF:** 2025-Nath-Few-shot and zero-shot Assamese hate speech detection a comparative.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

ORIGINAL ARTICLE
Social Network Analysis and Mining           (2026) 16:14 
https://doi.org/10.1007/s13278-025-01531-x
1  Introduction
Social media hate speech presents serious issues to the har­
mony of society, especially in multicultural and multilingual 
communities like Assam, India. As online communication 
increases rapidly, hate speech or other offensive material 
spreads widely in a short period, leading to violence and 
further social polarisation. Automatic detection and mod­
eration of such content are key to creating safer online 
spaces (Schmidt and Wiegand 2017; MacAvaney et  al. 
2019). Although there has been some progress in the detec­
tion of hate speech in high-resource languages, Assamese, 
as a low-resource Indo-Aryan language, has not yet been 
fully explored (Joshi et al. 2020; Ghosh and Senapati 2025). 
Automated detection is further complicated by the paucity 
of annotated datasets, the diversity of dialects (Kamrupi 
and Eastern variations), and the prevalence of code-switch­
ing with English, Hindi, and Bengali (Kumar et al. 2022). 
Furthermore, traditional supervised methods require vast 
amounts of labelled data and intensive fine-tuning, which 
is not always viable in the case of regional languages 
	
 Krishna Kant Pandey
krishna.pandey@jaipur.manipal.edu
	
 Vinod Yadav
vinod.yadav@jaipur.manipal.edu
Basab Nath
basabnath@gmail.com
Phaneendra Varma Chintalapati
chpvarmacse@svecw.edu.in
1	
School of Computer Science Engineering and Technology, 
Bennett University, TechZone II, Greater Noida, 
Uttar Pradesh 201310, India
2	
Department of Mechatronics Engineering, Manipal 
University Jaipur, Dehmi Kalan, Jaipur, Rajasthan 
303007, India
3	
Department of Mechanical Engineering, Manipal University 
Jaipur, Dehmi Kalan, Jaipur, Rajasthan 303007, India
4	
Department of Computer Science and Engineering, Shri 
Vishnu Engineering College for Women (Autonomous), 
Bhimavaram, Andhra Pradesh, India
Abstract
Hate speech detection remains a critical challenge for natural language processing (NLP), particularly in low-resource 
languages such as Assamese. Although supervised models have shown promise, their performance is often constrained by 
the scarcity of annotated data and complex linguistic phenomena, such as code-mixing. In this study, we systematically 
benchmark large language models (LLMs), including GPT-4, GPT-3.5, and the open-source Mistral-7B, in prompt-based 
zero-shot and few-shot configurations, alongside fine-tuned multilingual transformers such as IndicBERT and mBERT, for 
Assamese hate speech detection. We evaluate these models on an extended Assamese hate speech dataset that combines 
a publicly available Kaggle corpus with additional code-mixed and transliterated examples. Our results show that GPT-4 
achieves a macro-F1 score of 0.870 (few-shot, k = 5), significantly outperforming previous best-reported models, such as 
fine-tuned mBERT (0.72 F1). GPT-3.5 and Mistral-7B also demonstrate strong performance (0.807 and 0.801 macro-F1, 
respectively), with Mistral offering a competitive open-source alternative that supports efficient local deployment. Nota­
bly, GPT-4 maintains robust performance across challenging code-mixed and Roman-script text, highlighting its superior 
cross-lingual adaptability. Error analysis reveals challenges in cultural nuance and subtle sarcasm, while statistical signifi­
cance tests confirm consistent improvements.
Keywords  Zero-shot learning · Few-shot learning · GPT-4 · Transformers
Received: 24 July 2025 / Revised: 10 September 2025 / Accepted: 11 September 2025
© The Author(s) 2025
Few-shot and zero-shot Assamese hate speech detection: a 
comparative benchmark of large language models
Basab Nath1 · Krishna Kant Pandey2 · Vinod Yadav3 · Phaneendra Varma Chintalapati4
1 3

--- Page 2 ---

Social Network Analysis and Mining           (2026) 16:14 
(Zhang et al. 2018; Rani et al. 2022).he abilities of large 
language models (LLMs), e.g. GPT-4, GPT-3.5, and open-
source models such as Mistral-7B, alongside multilingual 
transformers (e.g. mBERT, IndicBERT), have recently been 
shown to excel in cross-lingual comprehension and zero-
shot reasoning skills (Brown et al. 2020; Devlin et al. 2019; 
Khanuja et al. 2021; Jiang et al. 2023). One possible solu­
tion for low-resource cases is that these models can accom­
plish a wide variety of downstream tasks without requiring 
task-specific training (Chowdhery et  al. 2023). However, 
fine-tuned transformers have been primarily used in detect­
ing hate speech in Assamese and other Indian languages so 
far, even in approaches based on classical supervised learn­
ing (Mandl et al. 2023; Ghosh and Senapati 2025). These 
methods can provide quite acceptable accuracy but are 
constrained by the available data and generally cannot gen­
eralise to code-mixed or dialectal data. To the best of our 
knowledge, no publicly available systems have methodi­
cally studied Assamese hate speech detection benchmarks 
using either zero- or few-shot configurations of LLMs. 
In this study, we provide a novel comparative benchmark 
of LLMs for Assamese hate speech detection in zero-shot 
and few-shot configurations. Our main contributions are 
summarized as follows:
	
●
We benchmark multiple LLMs, including GPT-4, GPT-
3.5, and Mistral-7B, as well as transformer baselines 
(IndicBERT, mBERT), using prompt-based and fine-
tuning strategies for Assamese hate speech detection.
	
●
We extend an existing Assamese hate speech dataset 
with code-mixed and Romanised examples to better 
simulate real-world usage scenarios. 
	
●
We provide an in-depth error analysis of model perfor­
mance on code-mixed and Romanised samples, high­
lighting persistent challenges in low-resource contexts.
	
●
We offer practical insights for deploying scalable and 
adaptable LLM-based hate speech moderation systems 
in Assamese and other underrepresented languages.
The rest of the paper is organised as follows: Sect. 2 will 
review existing related literature to the work on hate speech 
detection and multilingual NLP. In Sect. 3 we describe our 
methodology: the preparation of the data, the models to be 
used and the process of evaluation. The results and detailed 
analyses of experiments are reported in Sect. 4, and then 
Section. In the last part, Sect. 5 wraps up the paper with 
major findings and future course of investigation.
2  Literature review
The problem of hate speech identification has become a 
popular area of interest over the past few years, especially 
in high-resource languages like English, in which super­
vised data and pre-trained models can achieve good per­
formance (Schmidt and Wiegand 2017; MacAvaney et al. 
2019; Anjum and Katarya 2024). Nonetheless, in the case of 
Indian languages, research is still in its early stage due to the 
limited availability of data and the more complex aspects of 
linguistics (Joshi et al. 2020). Works like HASOC (Mandl 
et al. 2023) have studied hate and offensive speech detec­
tion in Indo-Aryan languages; however, their approaches 
tend to use supervised learning and transformer-based mod­
els (BERT, mBERT, or IndicBERT) and thus require much 
fine-tuning and record labelling. According to recent works, 
hate speech detection has been explored in Assamese using 
supervised methods and datasets composed of social media 
comments (Ghosh and Senapati 2025). Narayan et al. (2023) 
conducted a comparative analysis across five low-resource 
languages, including Assamese, as part of the HASOC 2023 
shared task, reporting that Bert Base Multilingual Cased 
achieved an F1-score of 0.705 for Assamese. Gutha et al. 
(2023) presented approaches that combine LSTM, CNN, 
and pre-trained IndicBERT and MuRIL models, achieving 
up to 69.7% F1-score for Assamese, and discussed chal­
lenges related to code-mixing and literal meaning shifts 
in Indic languages. Neog et al. (2024) proposed a hybrid 
BiLSTM-CNN model with a new dataset for Assamese 
toxic comment classification, emphasizing improvements 
over traditional approaches. Although these models perform 
decently on in-domain data, they struggle to generalise to 
code-mixed and Romanised forms that are frequent in the 
online discourse of Assamese (Kumar et al. 2022). Further­
more, previous research has not systematically explored 
the potential of large language models (LLMs) in zero-shot 
and few-shot contexts for hate speech processing in low-
resource languages. The progress in the field of general-pur­
pose and multilingual LLMs, such as GPT-4, GPT-3.5, and 
MuRIL, demonstrated the potential of developing cross-lin­
gual understanding in a way that does not explicitly involve 
fine-tuning on a specific task (Brown et al. 2020; Khanuja 
et al. 2021). Nevertheless, their scope is further unexplored 
about the detection of Assamese hate speech. Our work fills 
this gap by introducing a novel comparative baseline of 
several LLMs in zero-shot and few-shot configurations and 
assessing their potential on augmented datasets of Assamese 
hate speech code-mixed examples.
In short, compared to other studies in the Assamese lan­
guage that mainly rely on supervised transformer-based 
models and fully annotated data on hate speech detection, 
our work is the first to benchmark large language models 
1 3
   14 
 
Page 2 of 13

--- Page 3 ---

Social Network Analysis and Mining           (2026) 16:14 
(LLMs) like GPT-4 and GPT-3.5 in zero-shot and low-shot 
settings. Our strategy addresses key gaps identified in recent 
HASOC and FIRE workshops, providing a concrete assess­
ment of LLM performance on challenging examples of 
code-mixed and transliterated text and offering an original 
understanding and real-world resolutions in a low-resource 
multilingual framework.
3  Methodology
This paper used a comparative evaluation approach to 
determine the efficacy of large language models (LLMs) 
and multilingual transformers in detecting Assamese hate 
speech on zero-shot (Chowdhery et al. 2023) and few-shot 
(Brown et al. 2020) tasks. Our study was inspired by the 
following questions:
	
●
What is the performance of state-of-the-art LLMs on 
Assamese hate speech detection without any task-spe­
cific fine-tuning?
	
●
How does a few-shot approach compare to a zero-shot 
one?
	
●
What is the impact of code-mixing and script vari­
ance on the accuracy of various model architectures of 
detection?
We used a three-step protocol in our experiments: (1) prepa­
ration of data and its augmentation with code-mixed and 
transliterated examples, (2) model performance assessment 
based on prompt-based approaches to LLMs (GPT-4, GPT-
3.5, and the open-source Mistral-7B) as well as fine-tuning 
of transformer baselines (mBERT and IndicBERT), and (3) 
overall performance analysis in macro-F1 scores, precision, 
and recall values. The proposed work enabled a compari­
son between traditional fine-tuned approaches and modern 
prompt-based methods under resource-constrained scenar­
ios typical of low-resource languages. The overall detailed 
architecture, including internal submodules of both trans­
former-based and LLM-based paths, is illustrated in Fig. 1.
3.1  Dataset description
For this study, we utilised and systematically enhanced an 
Assamese hate speech dataset derived from the publicly 
available Kaggle Assamese multi-class hate speech col­
lection (Dutta 2023). The original dataset comprised 5,044 
social media comments sourced from Facebook, Twitter, 
and YouTube, collected during 2020–2022. Comments were 
harvested using platform-specific APIs and keyword-based 
filtering guided by Assamese hate speech indicators curated 
with input from native speakers and domain experts. Fol­
lowing a structured augmentation process (Section 3.1.4), 
the dataset was expanded to 7200 comments, of which 2156 
(20.6%) are synthetic additions designed to improve code-
mixing coverage, script diversity, and class balance.
3.1.1  Annotation framework and quality assurance
The dataset was annotated using a dual-level annotation 
scheme. The primary classification task was performed 
using a binary label column (0 = Non-hate, 1 = Hate). 
Additionally, a secondary fine-grained class column was 
introduced to capture more specific categories, including 
religion-based (REG), political (POL), gender-based (GEN), 
caste-based (CAS), and general offensive (OFF) instances. 
The annotation was conducted by two native Assamese 
speakers with a linguistics background, following a detailed 
15-page guideline that defined category boundaries, cultural 
nuances, and code-mixing scenarios. The inter-annotator 
agreement was strong, achieving a Fleiss’ κ of 0.78 for the 
binary labels and 0.71 for the fine-grained categories. To 
further ensure robustness, 20% of the samples were dou­
ble-annotated, with adjudication sessions held in cases of 
disagreement. Fine-grained category labels were provided 
for approximately 50% of the dataset (n = 2,522), enabling 
more detailed downstream analyses.
3.1.2  Dataset statistics and distribution
Table  1 summarises the label distribution in the original 
dataset, highlighting the prevalence of non-hate content. 
Additionally, fine-grained class distribution is presented in 
Table 2.
Fig. 1  Architecture illustrating internal components in the transformer 
and LLM paths for Assamese hate speech detection
 
1 3
Page 3 of 13 
   14 

--- Page 4 ---

Social Network Analysis and Mining           (2026) 16:14 
constituted less than 10% of the training set and were delib­
erately diversified and validated to minimise structural bias. 
Overall, augmentation expanded the training set from 5,044 
to 7,200 samples, of which 20.6% were synthetic.
To validate augmentation quality, two native Assamese 
annotators independently reviewed a random subset of 240 
augmented samples (60 code-mixed, 60 transliterated, 60 
paraphrased, and 60 template-based). Inter-annotator agree­
ment on label preservation was Cohen’s κ = 0.83, while the 
average naturalness score on a 1–5 scale was 4.3 (SD = 0.5). 
These results confirm that the augmented samples were both 
fluent and label-consistent. Importantly, our ablation study 
(Sect.  4.1) showed that augmentation improved baseline 
transformer performance only modestly (+0.024 macro-F1 
for IndicBERT, +0.021 for mBERT), far smaller than the 
margin between LLMs and baselines. This confirms that the 
observed improvements primarily stem from model capa­
bilities rather than synthetic bias. Table 3 provides the post-
augmentation distribution.
3.1.5  Preprocessing and normalization
The preprocessing pipeline included URL and mention nor­
malisation, punctuation standardisation, whitespace nor­
malisation, and Unicode encoding standardisation (UTF-8). 
We also implemented script and language detection to verify 
text integrity, achieving 97.5% language detection accuracy, 
manually confirmed on a 500-sample random subset.
The final dataset was split into 70% training (5,040 sam­
ples), 15% validation (1080 samples), and 15% test (1080 
samples), as summarised in Table 4. Augmentation added 
2156 synthetic samples (20.6% of the training set), increas­
ing code-mixing, script diversity, and category balance. 
Importantly, augmentation was applied exclusively to the 
training partition, while the validation and test sets consist 
only of authentic (non-augmented) samples to ensure unbi­
ased evaluation. Splits were stratified to preserve label bal­
ance, code-mixing ratios, and fine-grained categories where 
3.1.3  Linguistic characteristics analysis
A detailed linguistic analysis of the original dataset revealed 
that 67.8% of the comments were purely monolingual Assa­
mese, while 32.2% exhibited code-mixing with English, 
Hindi, or Bengali fragments. Specifically, Assamese-Eng­
lish code-mixing accounted for 17.7%, Assamese-Hindi for 
9.0%, and Assamese-Bengali for 5.5%. Comment lengths 
ranged from 3 to 127 tokens, with a median of 17 tokens and 
95th percentile length of 52 tokens.
After augmentation, the proportion of code-mixed com­
ments increased to 45.1%, distributed as Assamese-English 
(18.1%), Assamese-Hindi (11.8%), and Assamese-Bengali 
(6.7%). In addition, 12.0% of the dataset comprised Roman­
ized Assamese comments and 3.0% Devanagari script vari­
ants, enhancing script-level diversity. These adjustments 
ensure broader linguistic and orthographic coverage for 
evaluating model robustness.
3.1.4  Data augmentation strategy
To effectively capture the dynamism of multilingual online 
discourse, we introduced a systematic augmentation pipe­
line, with all synthetic samples used exclusively in the 
training split. The first phase increased the proportion of 
code-mixed comments from 32.2% to 42.5% by inserting 
short tokens from English (38%), Hindi (34%), and Bengali 
(28%) into Assamese sentences. The second phase intro­
duced script variability by generating Romanized Assamese 
(9.0%) and Devanagari script variants (6.5%), combining 
automated transliteration with manual correction. Finally, to 
balance underrepresented fine-grained classes (e.g., caste-
based, gender-based), we generated 650 additional hate 
speech examples through controlled template filling and 
paraphrasing of authentic comments. The use of template-
based augmentation was motivated by the extreme spar­
sity of such categories in the real dataset; these examples 
Table 1  Original Kaggle Assamese hate speech dataset distribution
Label type
Count
Percentage
Avg. length
Std Dev
Hate (1)
2156
42.7%
18.4
12.3
Non-hate (0)
2888
57.3%
22.1
15.7
Total
5044
100%
20.6
14.2
Table 2  Fine-grained category distribution (n = 2522)
Category
Count
Percentage
Description
REG
658
26.1%
Religion-based hate speech
POL
512
20.3%
Political hate and inflam­
matory content
GEN
387
15.4%
Gender-based discrimina­
tory language
CAS
234
9.3%
Caste-based hate speech
OFF
731
29.0%
General offensive language
Table 3  Post-augmentation distribution of the Assamese hate speech 
dataset
Sample type
Original 
count
Augmented 
count
Total 
%
Standard assamese
3421
3421
47.5
Code-mixed (Eng)
892
1334
18.5
Code-mixed (Hindi)
456
860
12.0
Code-mixed (Bengali)
275
650
9.0
Transliterated (Roman)
0
650
9.0
Transliterated (Devanagari)
0
485
6.5
Total
5044
7200
100.0
Synthetic samples were used exclusively in the training split, with 
template-based additions forming a small proportion for balancing 
underrepresented categories
1 3
   14 
 
Page 4 of 13

--- Page 5 ---

Social Network Analysis and Mining           (2026) 16:14 
observed here are unlikely to result from direct memorisa­
tion. Nevertheless,
Table 5 illustrates example comments and their linguistic 
features, and Table 6 summarises dataset quality metrics.
3.2  Model configurations
We tested five benchmark models for Assamese hate speech 
detection: three large language models (LLMs) and two 
multilingual transformer baselines. This design permitted a 
thorough comparison of prompt-based inference and super­
vised fine-tuning approaches within a low-resource context.
The large language models included GPT-4 (gpt-4-0613), 
estimated at about 1.76 trillion parameters, and GPT-3.5-
Turbo (gpt-3.5-turbo-0613), with approximately 175 billion 
parameters (Brown et al. 2020). GPT-4 has been associated 
with superior cross-lingual reasoning capabilities, whereas 
GPT-3.5-Turbo is more computationally economical, pri­
oritising efficiency in chat-oriented applications. To provide 
a representative open-source alternative, we also evaluated 
Mistral-7B-Instruct (Jiang et al. 2023), a 7-billion param­
eter instruction-tuned model optimised for general-pur­
pose reasoning and multilinguality. All LLMs were tested 
in zero-shot and few-shot setups using culturally-aware 
prompts, without task-specific fine-tuning. We used deter­
ministic generation parameters (temperature = 0.0), and 
outputs were constrained to strict “Hate” or “Non-hate” 
labels. Few-shot configurations incorporated k examples, 
with k ∈{1, 3, 5, 10}, and outputs were normalised for 
consistency.
For transformer baselines, we selected Multilingual 
BERT (mBERT) (Devlin et al. 2019) and IndicBERT (Kak­
wani et  al. 2020), both 12-layer transformers with 110 
million parameters. While mBERT is pre-trained on 104 
languages with limited Assamese coverage, IndicBERT 
available. Additionally, we employed 5-fold stratified cross-
validation for hyperparameter tuning, and temporal and 
script-based splits to assess generalisation across different 
timeframes and orthographic styles.
3.1.6  Ethical considerations and limitations
We took strict measures to anonymise user information and 
filter out extremely graphic content. Dataset usage adhered 
to the platform’s terms of service and was released under 
a CC BY-NC 4.0 license for academic research. Annotator 
and sampling biases were examined through demographic 
and regional representation analysis, achieving a conserva­
tive interpretation of fine-grained annotations due to partial 
coverage (50%).
We acknowledge that the dataset remains limited to con­
tent from 2020–2022, is biased towards Central Assamese 
dialects, and overrepresents Facebook (approximately 60% 
of samples). Although augmentation introduced greater 
script and code-mixing variability, it cannot fully substi­
tute for genuine cross-platform and longitudinal data. Thus, 
while the augmented corpus improves robustness, future 
expansions will target broader temporal coverage, dialectal 
balance, and additional platforms (e.g., Instagram, YouTube, 
WhatsApp) to further enhance generalisability. A broader 
methodological concern in LLM evaluation is the potential 
overlap between public benchmark datasets and the large-
scale pretraining corpora of proprietary models. While this 
risk cannot be fully ruled out, the relatively small size and 
niche linguistic scope of our dataset, coupled with the per­
sistence of systematic model errors (e.g., sarcasm, cultural 
nuance, transliteration), suggest that the performance gains 
Table 4  Final dataset split configuration and statistics
Split
Samples
Percentage
Notes
Training
5040
70%
Includes 2156 aug­
mented samples (20.6%); 
used for model fitting
Validation
1080
15%
Authentic samples only; 
hyperparameter tuning
Test
1080
15%
Authentic samples only; 
final evaluation
Total
7200
100%
5044 authentic + 2156 
augmented; stratified 
by labels, code-mix, 
categories
Table 5  Example Assamese comments from the dataset showing different types
e
p
y
T
l
e
b
a
L
t
x
e
T
e
l
p
m
a
S
D
I
1
Hate
Standard
2
This comment is total nonsense,
Hate
Code-mixed
3
Non-hate
Standard
4
politics
big joke
Hate
Code-mixed
Table 6  Dataset quality metrics overview
Metric
Value
Benchmark
Status
Inter-annotator agree­
ment (κ)
0.78
>0.70
✓ Acceptable
Language detection 
accuracy
97.3%
>95%
✓ High quality
Duplicate rate
0.8%
< 2%
✓ Minimal
Missing value rate
0.2%
< 1%
✓ Complete
Code-mixing coverage
45%
30–50%
✓ Representative
1 3
Page 5 of 13 
   14 

--- Page 6 ---

Social Network Analysis and Mining           (2026) 16:14 
3.3  Prompt design and experimental setup
For the large language models (GPT-4-0613, GPT-3.5-
turbo-0613, and Mistral-7B-Instruct), we developed a com­
prehensive prompt engineering framework covering both 
zero-shot and few-shot configurations. Our design adhered 
to established best practices for multilingual hate speech 
classification while integrating domain-specific consider­
ations tailored to Assamese and code-mixed social media 
discourse. In the zero-shot configuration (k = 0), each 
prompt consisted of a structured template containing a sys­
tem instruction defining the task, explicit output constraints, 
and context-awareness instructions for handling code-mixed 
content. The general template included:
“Task: Classify the following Assamese comment as 
either ’Hate’ or ’Non-hate’. Context: You are analysing 
social media comments in Assamese that may contain code-
mixed text fragments from English, Hindi, or Bengali. Out­
put: Respond with exactly one word: ’Hate’ or ’Non-hate’. 
Comment: [TARGET_COMMENT] Classification:”
For few-shot configurations, we included k ∈{1, 3, 5, 10} 
labelled examples preceding the target comment to guide 
the model through in-context learning. The choice of these 
k values followed common practice in prior LLM evalua­
tion studies (Brown et al. 2020; Chowdhery et al. 2023), 
balancing representative coverage with the input length 
constraints of current APIs. Higher k values were avoided 
due to latency and cost considerations, as well as the risk of 
diminishing returns.
To ensure reproducibility and eliminate any risk of data 
leakage, few-shot examples were sampled exclusively from 
the training split and were temporally distinct from valida­
tion and test data (i.e., drawn from earlier time periods). 
The selection process followed a four-step algorithm: (1) 
partition the training split by primary class label (hate vs. 
non-hate), (2) further group by linguistic type (monolingual 
Assamese, English-Assamese, Hindi-Assamese, Bengali-
Assamese, and transliterated), (3) randomly sample pro­
portionate examples from each subgroup while enforcing 
diversity in comment length (5–50 tokens) and fine-grained 
category (religion-based, political, gender-based, caste-
based, offensive), and (4) fix the selected examples across 
all runs for comparability. This ensured that no few-shot 
examples overlapped with, or were contemporaneous to, 
is pre-trained specifically on 12 Indian languages, includ­
ing Assamese, and thus offers stronger vocabulary cover­
age for Indic scripts. Both models were fine-tuned on our 
augmented dataset using a gradual unfreezing strategy 
and regularisation enhancements (dropout rate = 0.1, label 
smoothing α = 0.1). The hyperparameters were optimised 
via grid search with macro-F1 on the validation set as the 
criterion. The final configuration included a learning rate of 
2e–5, batch size of 16 (effective 32 with gradient accumu­
lation), sequence length of 128, maximum 5 epochs with 
early stopping (patience = 2), and weight decay of 0.01. 
The sequence length of 128 tokens was chosen based on the 
observed dataset distribution (maximum comment length = 
127 tokens, 95th percentile = 52), ensuring no truncation of 
samples while remaining consistent with standard practice 
for short-text classification in BERT-based models. Warmup 
steps were set to 10% of total training iterations.
Transformer experiments were executed on an NVIDIA 
Tesla V100 (32 GB VRAM) using PyTorch 1.12.0 and 
Transformers 4.21.0 in mixed precision (FP16). This setup 
was also used for evaluating the open-source LLM (Mistral-
7B), while GPT-3.5 and GPT-4 were accessed through API 
endpoints with reliability safeguards including retry logic 
and timeout handling. Multiple random seeds (42, 123, 456, 
789, 1024) were fixed for reproducibility, McNemar’s test 
(p < 0.05) was used for statistical significance, and 95% 
confidence intervals were estimated via bootstrap sampling 
(n = 1000). Table 7 summarises the evaluated models and 
their key characteristics. Table 8 describes the hyperparam­
eters used in the proposed work.
Table 7  Comparative summary of evaluated models, including parameter size, training setup, and inference efficiency
Model
Params
Architecture
Training
Evaluation
Inference speed
GPT-4
∼1.76T
Proprietary transformer
Pre-trained only
Prompt-based (0/few-shot)
∼2.4 s / sample (API)
GPT-3.5
∼175B
Proprietary transformer
Pre-trained only
Prompt-based (0/few-shot)
∼0.9 s / sample (API)
Mistral-7B
7B
Decoder-only transformer
Pre-trained only
Prompt-based (0/few-shot)
∼0.6 s / sample (V100)
mBERT
110 M
12-layer BERT
Fine-tuned
Supervised classification
∼80 ms / sample (V100)
IndicBERT
110 M
12-layer BERT (Indic)
Fine-tuned
Supervised classification
∼70 ms / sample (V100)
Table 8  Hyperparameters for transformer fine-tuning
Parameter
Value
Selection
Learning rate
2e–5
Grid search
Batch size
16 (effective: 32)
Resource optimization
Epochs
Max 5
Early stopping
Optimizer
AdamW
Standard practice
Dropout
0.1
Regularization
Sequence length
128
Distribution analysis
Warmup ratio
0.1
Linear schedule
Weight decay
0.01
L2 regularization
1 3
   14 
 
Page 6 of 13

--- Page 7 ---

Social Network Analysis and Mining           (2026) 16:14 
authenticity, with inter-validator agreement κ = 0.87 for lin­
guistic accuracy and κ = 0.84 for cultural appropriateness, 
demonstrating strong consensus. Furthermore, all experi­
mental data handling complied with ethical AI guidelines, 
including the removal of personal identifiers, encrypted API 
communication, no external data retention, and oversight 
for manual annotations.
Table 9 shows an example few-shot prompt with k = 3 
for GPT-based models, and Table 10 summarises the overall 
prompt configurations.
3.4  Evaluation metrics
To comprehensively assess model performance, we 
employed standard metrics commonly used in hate speech 
and text classification tasks, namely precision, recall, and 
macro-averaged F1 score (Zhang et al. 2018; Fortuna and 
Nunes 2018). Precision (P) measures the proportion of pre­
dicted positive (hateful) samples that are actually positive, 
defined as:
P =
TP
TP + FP
where TP and FP represent true positives and false positives, 
respectively.
Recall (R) evaluates the proportion of actual positive 
samples that were correctly identified:
R =
TP
TP + FN
where FN denotes false negatives.
The macro-averaged F1 score (F1) combines precision 
and recall and is particularly useful for imbalanced datasets 
since it gives equal weight to each class:
evaluation data, thereby mimicking real-world deployment 
where models are trained on past discourse and evaluated 
on future content.
All LLM evaluations used deterministic generation 
parameters (temperature = 0.0, max tokens = 10, top-p = 1.0) 
and applied stop sequences to enforce concise responses. 
We explicitly constrained outputs to case-insensitive “Hate” 
or “Non-hate” to standardise downstream evaluation. Post-
processing included response extraction after the “Clas­
sification:” marker, normalisation, and automated error 
detection. Non-conforming responses, comprising less than 
2% of total predictions, were manually reviewed and conser­
vatively labeled. LLM evaluations were performed through 
the OpenAI API (GPT-4, GPT-3.5) and a local runtime on 
NVIDIA Tesla V100 (Mistral-7B), incorporating reliability 
measures such as rate limiting, exponential backoff retry 
logic, and strict timeout handling. For transformer baselines 
(mBERT and IndicBERT), we adopted the fine-tuning con­
figurations outlined in Sect.  3.2. Models were fine-tuned 
using a learning rate of 2e–5, a batch size of 16 with gradi­
ent accumulation, and a maximum sequence length of 128 
tokens. Training ran for up to 5 epochs with early stopping 
based on validation macro-F1 score (patience = 2). Regu­
larisation strategies included dropout (0.1), weight decay 
(0.01), and the AdamW optimiser with linear warmup (10% 
of steps). The best-performing checkpoint on the valida­
tion set was selected for final evaluation. To ensure repro­
ducibility, each configuration was evaluated across five 
independent runs using fixed random seeds (42, 123, 456, 
789, 1024). Confidence intervals (95%) were estimated via 
bootstrap sampling with n = 1000. Statistical significance 
between model pairs was assessed using McNemar’s test 
with a threshold of p < 0.05.
All prompts underwent a rigorous cultural and linguistic 
validation process by a panel of native Assamese speakers 
with computational linguistics expertise. Validation focused 
on linguistic accuracy, cultural sensitivity, and code-mixed 
Table 9  Example few-shot prompt (k = 3) designed for GPT-based models
Prompt Content
Example 1:
Hate
Example 2:
Non-hate
Example 3: This comment is total nonsense,
Hate
Target:
politics
big joke
?
Table 10  Summary of prompt configurations used in LLM evaluations
k-value
Description
Example selection
Parameters
0
Zero-shot: Task instruction only
N/A
temp=0.0, max=10
1
Few-shot: One balanced example
Stratified sampling
temp=0.0, max=10
3
Few-shot: Three diverse examples
Diversity-based selection
temp=0.0, max=10
5
Few-shot: Five balanced examples
Class-balanced sampling
temp=0.0, max=10
10
Few-shot: Ten comprehensive examples
Max. diversity coverage
temp=0.0, max=10
1 3
Page 7 of 13 
   14 

--- Page 8 ---

Social Network Analysis and Mining           (2026) 16:14 
The superiority of GPT-4 was statistically significant (p < 
0.001, McNemar’s test), as confirmed in pairwise compari­
sons summarized in Table 16.
Few-shot configurations generally provided significant 
performance boosts for all three LLMs. GPT-4 demon­
strated rapid gains from k = 0 to k = 3, with performance 
plateauing at k = 5 and slightly declining at k = 10. This 
pattern suggests diminishing returns beyond moderate 
example counts, likely due to overfitting or prompt interfer­
ence. In contrast, GPT-3.5 displayed more gradual improve­
ments, peaking at k = 5 and declining at k = 10, reflecting 
higher sensitivity to prompt composition and example qual­
ity. Mistral-7B also followed a similar trajectory, achieving 
its best performance at k = 5 (macro-F1 = 0.801), which 
positions it between GPT-3.5 and the fine-tuned IndicBERT 
baseline. This highlights the potential of open-source LLMs 
to provide competitive accuracy with the added advantage 
of local deployment.
To further verify that few-shot improvements were not 
artifacts of the specific example selection strategy, we con­
ducted a sensitivity analysis comparing stratified versus 
random sampling of few-shot examples. Across all LLMs, 
macro-F1 differences remained consistently below 1.5%. 
For instance, GPT-4 (k = 5) achieved 0.870 with strati­
fied selection versus 0.864 with random selection, GPT-3.5 
(k = 5) differed by 0.9 percentage points (0.807 vs. 0.798), 
and Mistral-7B (k = 5) differed by 0.6 points (0.801 vs. 
0.795). These small variations confirm the robustness of 
our reported few-shot results. Table  12 summarises this 
comparison. As shown in Fig.  2, all LLMs demonstrate 
performance improvements with increasing few-shot exam­
ples, although performance saturates or declines slightly at 
F1 = 2 × P × R
P + R
We used macro-averaging to ensure fair evaluation across 
both "Hate" and "Non-hate" classes, irrespective of class 
distribution (Mohammad et  al. 2021; Schmidt and Wie­
gand 2017). For the transformer baselines (mBERT and 
IndicBERT), we evaluated on a held-out test set with fixed 
hyperparameters, selecting the best checkpoint based on 
validation F1 score. For LLM-based evaluations (GPT-4 
and GPT-3.5), model predictions were directly mapped to 
"Hate" or "Non-hate" using prompt outputs without addi­
tional calibration. All metrics were computed using the 
scikit-learn library (Pedregosa et al. 2011), ensuring 
reproducibility and standardized comparison.
4  Results
Table 11 presents the detailed performance metrics for all 
evaluated models and configurations, including precision, 
recall, macro-F1 score, and overall accuracy. Addition­
ally, we report 95% confidence intervals for each macro-
F1 score, estimated using bootstrap sampling (n = 1000), to 
illustrate the statistical robustness of the results. The con­
sistent narrow intervals observed, particularly for GPT-4, 
indicate stable and reproducible performance across runs. 
GPT-4 consistently outperformed all other models across 
every metric, achieving a maximum macro-F1 score of 
0.870 in the k = 5 few-shot configuration. This represents 
a substantial improvement over the best fine-tuned baseline 
(IndicBERT), which attained a macro-F1 score of 0.780. 
Table 11  Main results: model performance on Assamese hate speech detection
Model
Config
Prec.
Recall
F1
Acc.
95% CI (F1)
GPT-4
Zero-shot
0.847
0.823
0.835
0.851
[0.821, 0.849]
k = 1
0.863
0.841
0.852
0.867
[0.838, 0.866]
k = 3
0.879
0.856
0.867
0.882
[0.854, 0.880]
k = 5
0.881
0.859
0.870
0.885
[0.857, 0.883]
k = 10
0.878
0.854
0.866
0.881
[0.853, 0.879]
GPT-3.5
Zero-shot
0.782
0.756
0.769
0.791
[0.752, 0.786]
k = 1
0.801
0.778
0.789
0.812
[0.772, 0.806]
k = 3
0.824
0.798
0.811
0.831
[0.794, 0.828]
k = 5
0.819
0.795
0.807
0.827
[0.790, 0.824]
k = 10
0.813
0.789
0.801
0.821
[0.784, 0.818]
Mistral-7B
Zero-shot
0.764
0.752
0.758
0.774
[0.742, 0.774]
k = 1
0.782
0.767
0.774
0.789
[0.759, 0.789]
k = 3
0.805
0.793
0.799
0.814
[0.784, 0.814]
k = 5
0.811
0.792
0.801
0.818
[0.786, 0.816]
k = 10
0.807
0.785
0.796
0.812
[0.780, 0.812]
mBERT
Fine-tuned
0.756
0.731
0.743
0.768
[0.726, 0.760]
IndicBERT
Fine-tuned
0.792
0.768
0.780
0.803
[0.763, 0.797]
Best F1 scores are highlighted in bold
1 3
   14 
 
Page 8 of 13

--- Page 9 ---

Social Network Analysis and Mining           (2026) 16:14 
illustrating the superior performance of GPT-4 (k = 5) 
compared to GPT-3.5, Mistral-7B, IndicBERT, and mBERT.
4.1  Ablation study
To ensure that the reported gains were not artificially driven 
by our augmentation strategy, we performed an ablation 
study on the transformer baselines with and without aug­
mented training data (validation and test sets remained 
strictly authentic). Each condition was repeated across five 
random seeds. Results are shown in Table 13.
Augmentation 
contributed 
modest 
but 
consistent 
improvements (+0.022 for IndicBERT, +0.019 for mBERT). 
These gains confirm that augmentation enhanced baseline 
robustness, particularly for code-mixed and transliterated 
patterns, but they are far smaller than the margin between 
GPT-4 (k = 5, 0.870 F1) and the best fine-tuned trans­
former. Since LLMs were never trained on augmented 
samples, their superior performance cannot be attributed to 
augmentation.
4.2  Fine-grained performance analysis
A category-wise breakdown of GPT-4 (k = 5) results, pre­
sented in Table 14, reveals that religion-based and general 
offensive categories achieved the highest macro-F1 scores 
(0.877 and 0.893, respectively). These results indicate the 
presence of strong linguistic markers and explicit termi­
nology in these categories, which facilitate detection. In 
contrast, caste-based hate speech exhibited the lowest per­
formance (macro-F1: 0.782), likely due to subtle cultural 
references and limited representation in the training data. 
For comparison, Mistral-7B (k = 5) achieved competitive 
performance across most categories (macro-F1 ≈ 0.79-−
0.80) , outperforming IndicBERT and mBERT but remain­
ing slightly below GPT-3.5 and GPT-4.
higher k-values (k = 10), suggesting diminishing returns or 
potential overfitting.
Among transformer baselines, IndicBERT outperformed 
mBERT (macro-F1 0.780 vs 0.743), underscoring the 
advantage of Indic-specific pre-training for low-resource 
languages such as Assamese. These results validate our 
hypothesis regarding the importance of cultural and linguistic 
alignment in pre-trained transformer models. Figure 3 com­
pares the macro-F1 scores of all evaluated models, clearly 
Table 12  Sensitivity analysis of few-shot example selection (k = 5). 
Macro-F1 values under stratified vs. random sampling
Model
Stratified
Random
Difference
GPT-4 (k = 5)
0.870
0.864
0.006
GPT-3.5 (k = 5)
0.807
0.798
0.009
Mistral-7B (k = 5)
0.801
0.795
0.006
Differences remain below 1.5%, confirming robustness
Table 13  Ablation results: effect of augmentation on transformer base­
lines (macro-F1)
Model (fine-tuned)
Without Aug.
With Aug.
IndicBERT
0.758 [0.736, 0.778]
0.780 [0.763, 0.797]
mBERT
0.724 [0.702, 0.745]
0.743 [0.726, 0.760]
Table 14  Performance breakdown by fine-grained categories (GPT-4, 
k = 5)
Category
Prec.
Recall
F1
Support
Religion-based
0.891
0.864
0.877
132
Political
0.856
0.835
0.845
103
Gender-based
0.823
0.795
0.809
78
Caste-based
0.798
0.766
0.782
47
Offensive
0.903
0.884
0.893
147
Best values are highlighted in bold
Fig. 3  Macro F1 scores of all evaluated models
 
Fig. 2  Few-shot performance improvement for GPT-4, GPT-3.5, and 
Mistral-7B. All three models improve with increasing k, with perfor­
mance saturating or slightly declining at k = 10. Mistral-7B consis­
tently outperforms IndicBERT and mBERT baselines but remains 
below GPT-3.5 and GPT-4
 
1 3
Page 9 of 13 
   14 

--- Page 10 ---

Social Network Analysis and Mining           (2026) 16:14 
k = 5), clearly highlighting correct classifications (true 
positives and true negatives) and incorrect classifications 
(false positives and false negatives).
We observed five dominant error categories across 
models. Cultural context failures were the most frequent, 
4.3  Code-mixing and script analysis
Table  15 illustrates model performance across text types. 
All models performed best on standard Assamese text, with 
performance degrading in code-mixed and transliterated 
samples. GPT-4 showed the highest resilience, maintain­
ing an F1-score above 0.83 even on transliterated inputs, 
while Mistral-7B also proved competitive with stable per­
formance across scripts, outperforming IndicBERT and 
mBERT in most categories. By contrast, mBERT exhibited 
the steepest decline.
4.4  Statistical significance and learning curves
Table  16 presents pairwise statistical significance results 
using McNemar’s test. The performance difference between 
GPT-4 and all other models was highly significant (p < 
0.001), with large effect sizes (Cohen’s d >0.7). Comparisons 
also revealed that Mistral-7B significantly outperformed 
both IndicBERT and mBERT, but remained statistically 
below GPT-4 and slightly below GPT-3.5. Learning curves 
demonstrated rapid gains up to k = 5, beyond which perfor­
mance gains plateaued or slightly declined.
4.5  Comparison with existing work
To contextualize our contributions, we compare our results 
with the best-known Assamese hate speech detection system 
reported by Ranasinghe et al. (2023) as part of the HASOC 
2023 shared task. Their approach, which fine-tuned XLM-R 
on Assamese hate speech data, achieved a macro-F1 score 
of 0.7346, requiring extensive task-specific annotated data 
and supervised fine-tuning. In contrast, our best-performing 
model (GPT-4 with k = 5 few-shot configuration) achieved 
a significantly higher macro-F1 score of 0.870, represent­
ing a +13.5% absolute improvement. Mistral-7B also pro­
vided a strong open-source alternative (macro-F1 = 0.801), 
outperforming IndicBERT and mBERT while offering the 
advantage of local inference without API costs. Table  17 
summarizes this comparison.
4.6  Error analysis
To better understand model limitations and qualitative 
behaviour, we conducted a comprehensive error analysis 
on 450 misclassified samples from the test set. Our analysis 
revealed five primary error categories with distinct linguis­
tic and cultural characteristics. Table 18 presents the quan­
titative distribution of these error types across all evaluated 
models.
To further contextualise these errors, Fig. 4 presents a 
confusion matrix for our best-performing model (GPT-4, 
Table 15  Performance on different text types
Text Type
GPT-4 
(k = 5)
GPT-
3.5 
(k = 5)
Mis­
tral-
7B 
(k = 5)
IndicBERT
mBERT
Standard Assamese 0.884
0.821
0.808
0.798
0.761
Assamese-English
0.867
0.804
0.791
0.772
0.731
Assamese-Hindi
0.852
0.789
0.782
0.756
0.709
Assamese-Bengali
0.859
0.795
0.787
0.763
0.724
Transliterated
0.831
0.763
0.774
0.691
0.652
Best results per row are highlighted in bold
Table 16  Statistical significance tests (McNemar’s test)
Model Pair
p-value
Significance
Effect Size
GPT-4 vs GPT-3.5
< 0.001
***
0.73
GPT-4 vs Mistral-7B
< 0.001
***
0.82
GPT-4 vs IndicBERT
< 0.001
***
0.89
GPT-4 vs mBERT
< 0.001
***
1.12
GPT-3.5 vs Mistral-7B
0.041
*
0.27
GPT-3.5 vs IndicBERT
0.023
*
0.31
GPT-3.5 vs mBERT
< 0.001
***
0.58
Mistral-7B vs IndicBERT
0.017
*
0.29
Mistral-7B vs mBERT
< 0.001
***
0.54
IndicBERT vs mBERT
0.009
**
0.37
Best effect sizes are highlighted in bold
Table 17  Comparison with the existing Assamese hate speech detec­
tion benchmark
Method
F1-Score
Data 
requirement
Approach
HASOC 2023 (Ranas­
inghe et al.)
0.735
High (fully 
labeled)
Fine-tuned 
XLM-R
IndicBERT (this study)
0.780
Medium
Fine-tuned 
transformer
Mistral-7B (k = 5) (this 
study)
0.801
Low 
(few-shot)
Open-source 
prompt-
based LLM
GPT-3.5 (k = 5) (this 
study)
0.807
Low 
(few-shot)
Prompt-
based LLM
GPT-4 (k = 5) (this 
study)
0.870
Very Low 
(few-shot)
Prompt-
based LLM
Table 18  Distribution of error types across models (% of total errors)
Error Type
GPT-4 
(k=5)
GPT-
3.5 
(k=5)
Mis­
tral-7B 
(k=5)
IndicBERT
mBERT
Cultural context
28.3
34.7
32.1
41.2
47.8
Script mixing
24.1
29.8
27.5
35.6
38.9
Sarcasm/Irony
19.5
26.4
23.4
28.3
31.7
Keyword bias
14.2
18.9
16.8
22.4
26.1
Temporal context
13.9
17.6
15.2
20.5
23.4
1 3
   14 
 
Page 10 of 13

--- Page 11 ---

Social Network Analysis and Mining           (2026) 16:14 
events or time-sensitive discourse (e.g., festival tensions or 
election remarks), where models lacked updated or event-
specific knowledge. These patterns underline the need for 
culturally adaptive modelling and enhanced context-aware­
ness mechanisms in future Assamese hate speech detec­
tion systems  . Table 19 shows the error examples from the 
GPT-4 model.
4.7  Discussions
We can confirm our results that LLMs, and especially GPT-4, 
have a high potential to fill in the low-resource gap in Assa­
mese hate speech detection. Their flexibility and advanced 
cross-lingual transfer, as well as their ability to deal with 
code-mixed and transcribed text options on social media, 
affirm their capacity to become established in the confus­
ing multi-linguistic social media configurations. Few-shot 
paradigm has deployment benefits since it allows reduc­
ing the annotated data requirement, which is an important 
issue in high-resource languages. The open-source Mistral-
7B model also delivered competitive results (macro-F1 ≈
0.80), positioning itself between GPT-3.5 and IndicBERT, 
and highlighting the growing promise of community-driven 
LLMs that can be deployed locally without recurring API 
costs. Nevertheless, the existent computational expense 
and latency of LLMs are considerable hindrances to real-
time applications. Additionally, cultural nuances and fast 
changing linguistic patterns are long term issues (Behzadi 
et  al. 2021). The development of hybrid structures that 
simplify the LLM functionality into local models that are 
lightweight, the incorporation of continuous learning sys­
tems that will reduce temporal drift and the exploration of 
culturally-adaptive prompt-engineering approaches are all 
areas that should be explored in the future.
involving misclassification of culturally specific insults or 
idiomatic expressions, which require deep socio-linguistic 
understanding; GPT-4 showed the lowest error rate in this 
category, while mBERT struggled significantly. Mistral-
7B followed GPT-3.5 closely, reducing errors compared to 
IndicBERT but still falling short of GPT-4 in nuanced cases 
such as sarcasm and cultural references. Script mixing and 
transliteration challenges also posed substantial difficulties, 
especially when transitions between Assamese and Eng­
lish occurred mid-sentence or when Bengali numerals and 
Roman script slang were used; even GPT-4 exhibited errors 
when scripts were combined in non-standard ways. Sarcasm 
and implicit hate detection errors were common, highlight­
ing limitations in pragmatic and discourse-level understand­
ing; rhetorical questions and exaggerated praise often went 
undetected as hateful. Additionally, we observed keyword 
bias and surface-level triggers, where models over-relied 
on specific politically or religiously loaded terms, resulting 
in false positives in otherwise neutral contexts. Finally, tem­
poral context errors arose in comments referencing recent 
Table 19  Illustrative error examples
Text Sample
True Label GPT-4 Pred.
Error Type
Analysis
real
joker,
politics
Hate
Non-hate
Cultural Context Missed sarcastic politi-
cal insult
support
Non-hate
Hate
Keyword Bias
Misclassified
due
to
Neta (leader) term
pol-
itics
Hate
Non-hate
Script Mixing
Transliterated
phrase
missed
com-
ment
Non-hate
Non-hate
Correct
Correctly identified pos-
itive sentiment
Fig. 4  Confusion matrix illustrating GPT-4 (k = 5) classification out­
comes, highlighting correct and incorrect classifications
 
1 3
Page 11 of 13 
   14 

--- Page 12 ---

Social Network Analysis and Mining           (2026) 16:14 
which permits any non-commercial use, sharing, distribution and 
reproduction in any medium or format, as long as you give appropri­
ate credit to the original author(s) and the source, provide a link to the 
Creative Commons licence, and indicate if you modified the licensed 
material. You do not have permission under this licence to share 
adapted material derived from this article or parts of it. The images or 
other third party material in this article are included in the article’s Cre­
ative Commons licence, unless indicated otherwise in a credit line to 
the material. If material is not included in the article’s Creative Com­
mons licence and your intended use is not permitted by statutory regu­
lation or exceeds the permitted use, you will need to obtain permission 
directly from the copyright holder. To view a copy of this licence, visit ​
h​t​t​p​:​/​/​c​r​e​a​t​i​v​e​c​o​m​m​o​n​s​.​o​r​g​/​l​i​c​e​n​s​e​s​/​b​y​-​n​c​-​n​d​/​4​.​0​/.
References
Anjum A, Katarya R (2024) Hate speech, toxicity detection in online 
social media: a recent survey of state of the art and opportunities. 
Int J Inform Sec 23:577–608. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​2​0​7​-​0​2​
3​-​0​0​7​5​5​-​2
Behzadi M, Harris IG, Derakhshan A (2021) Rapid cyber-bullying 
detection method using compact bert models. In: Proceedings of 
the 2021 IEEE 15th international conference on semantic com­
puting (ICSC), pp 199–202. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​I​C​S​C​5​0​6​3​1​
.​2​0​2​1​.​0​0​0​4​2
Brown TB, Mann B, Ryder N, Subbiah M, Kaplan J, Dhariwal P 
(2020) Language models are few-shot learners. Adv Neural Inf 
Process Syst 33:1877–1901
Chowdhery A, Narang S (2023) Palm: scaling language modeling with 
pathways. J Mach Learn Res 24(1):1–113
Devlin J, Chang M-W, Lee K, Toutanova K (2019) Bert: Pre-training 
of deep bidirectional transformers for language understanding. 
In: Proceedings of NAACL-HLT
Dutta A (2023) Assamese multi-class hate speech tagged data. ​h​t​t​p​s​:​/​/​
w​w​w​.​k​a​g​g​l​e​.​c​o​m​/​d​a​t​a​s​e​t​s​/​a​s​h​i​s​d​t​a​/​a​s​s​a​m​e​s​e​-​m​u​l​t​i​-​c​l​a​s​s​-​h​a​t​e​-​s​p​
e​e​c​h​-​t​a​g​g​e​d​-​d​a​t​a. Accessed: 2025-06-30
Fortuna P, Nunes S (2018) A survey on automatic detection of hate 
speech in text. ACM Comput Surv (CSUR) 51(4):1–30
Ghosh D, Senapati S (2025) Hate speech detection in low-resourced 
indian languages: an analysis of Assamese and Bodo. Nat Lang 
Process J
Gutha AR (2023) Multilingual hate speech and offensive language 
identification using deep learning. In: Forum for information 
retrieval evaluation (FIRE), HASOC Track. ​h​t​t​p​s​:​/​/​c​e​u​r​-​w​s​.​o​r​g​/​
V​o​l​-​3​6​8​1​/​T​6​-​1​2​.​p​d​f
Jiang AQ, Sablayrolles A, Mensch A, Bamford C, Chaplot DS, 
Las  Casas D, Bressand F, Lengyel G, Lample G, Saulnier L, 
Lavaud LR, Lachaux M-A, Stock P, Scao TL, Lavril T, Wang 
T, Lacroix T, Sayed WE (2023) Mistral 7B. arXiv preprint 
arXiv:2310.06825. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​3​1​0​.​0​6​8​2​5
Joshi P, Santy S, Budhiraja A, Bali K, Choudhury M (2020) The state 
and fate of linguistic diversity and inclusion in the nlp world. In: 
Proceedings of ACL
Kakwani D, Gupta A, Siddhant A, Ramesh S, Dandapat S, Golla V, 
Bhattacharyya P, Kumar R, Bali K, Choudhury M (2020) Indic­
nlpsuite: Monolingual corpora, evaluation benchmarks and pre-
trained multilingual language models for Indian languages. In: 
Findings of EMNLP
Khanuja S, Doddapaneni S, Kumar V et al (2021) Muril: multilingual 
representations for indian Languages. Findings of ACL
Kumar R, Bhat RA, Sharma DM (2022) Code-mixed nlp: a survey of 
tasks and techniques. ACM Trans Asian Low-Res Lang Inform 
Process
5  Conclusion
This paper introduced a novel benchmark of multilingual 
transformers and large language models (LLM) against hate 
speech detection in Assamese in a zero-shot and few-shot 
scenario. We showed the potential of LLMs to perform 
remarkably well without the need for task-specific fine-tun­
ing by using GPT-4 and GPT-3.5 in prompt-based set-ups 
compared to fine-tuned IndicBERT and mBERT baselines. 
It is important to note that GPT-4 reached a macro-F1 score 
of 0.870 in few-shot (k = 5) with an extremely high mar­
gin over previously reported Assamese benchmarks. We 
were able to test the robustness of these models in a sce­
nario that most resembled that of a social media scenario 
due to our augmented dataset with code-mixed and trans­
literated samples. It shows that LLM-based methods to 
moderate hate speech high-potential in low-resource, mul­
tilingual configurations, such as Assamese. Nevertheless, to 
scale the solution, the cost of computation and the risk of 
cultural misinterpretation indicate that a balanced middle-
ground solution of hybrid strategies (i.e., integration of the 
strengths of LLMs with local lightweight models) might 
be preferable. For future work we aim to explore continual 
learning techniques to adapt to evolving online discourse, 
develop more culturally sensitive prompts, and investigate 
multimodal signals (such as images and emojis) to further 
enhance detection accuracy. Additionally, we recommend 
evaluations on newly collected or temporally shifted datas­
ets to minimise any residual risk of overlap with LLM pre­
training corpora and to ensure long-term generalisability. 
We hope this work serves as a foundation and catalyst for 
further research in low-resource language safety and con­
tent moderation.
Author contributions  BN: Data collection, Data analysis, Writing ini­
tial draft; KKP: Conceptualisation, Review and Editing; VY: Concep­
tualisation, Visualisation, Supervision; PVC: Supervision, Data analy­
sis, Review and Editing.
Funding  Open access funding provided by Manipal University Jaipur. 
The authors received no specific funding for this study.
Data availability  The datasets used and/or analysed during the current 
study are available within the manuscript.
Declarations
Conflict of interest  The authors declare no Conflict of interest.
Ethics approval and consent to participate  Not applicable.
Consent for publication  Not applicable.
Open Access   This article is licensed under a Creative Commons 
Attribution-NonCommercial-NoDerivatives 4.0 International License, 
1 3
   14 
 
Page 12 of 13

--- Page 13 ---

Social Network Analysis and Mining           (2026) 16:14 
Ranasinghe T, Ghosh K, Pal AS, Senapati A, Dmonte AE, Zampieri 
M, Modha S, Satapara S (2023) Overview of the hasoc subtracks 
at fire 2023: hate speech and offensive content identification in 
Assamese, Bengali, Bodo, Gujarati and Sinhala. In: Proceedings 
of the forum for information retrieval evaluation (FIRE), pp 1–3. ​
h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​4​5​/​3​6​3​2​7​5​4​.​3​6​3​3​2​7​8
Rani S, Kumari P, Singh SK (2022) A survey of recent advances in hate 
speech detection. Int J Inform Manag Data Insights 2(2):100074
Schmidt A, Wiegand M (2017) A survey on hate speech detection 
using natural language processing. In: Proceedings of the fifth 
international workshop on natural language processing for social 
media, 1–10
Zhang Z, Robinson D, Tepper M (2018) Detecting hate speech on 
social media: a survey. ACM SIGKDD Explor Newsl 20(2):80–94
Zhang L, Wang S, Liu B (2018) Deep learning for sentiment analysis: 
a survey. Wiley Interdisc Rev Data Min Knowl Disc 8(4):1253
Publisher's Note  Springer Nature remains neutral with regard to juris­
dictional claims in published maps and institutional affiliations.
MacAvaney S, Yao H, Yang E, Russell K, Goharian N (2019) 
Hate speech detection: challenges and solutions. PLoS ONE 
14(8):0221152
Mandl T, Modha S, Mandlia C, Patel J (2023) Overview of the hasoc 
track at fire 2023: hate speech and offensive content identification 
in English and Indo-Aryan languages. Working Notes of FIRE
Mohammad SM, Rozovskaya A, Glass J et al (2021) A survey of 
hateful and offensive language detection in nlp. arXiv preprint 
arXiv:2102.00796
Narayan N, Biswal M, Goyal P, Panigrahi A (2023) Hate speech and 
offensive content detection in indo-aryan languages: a battle of 
lstm and transformers. In: Forum for information retrieval evalu­
ation (FIRE), HASOC Track. arxiv:2312.05671
Neog M (2024) A hybrid deep learning approach for assamese toxic 
comment classification. Proc Comput Sci 232:3122–3131. ​h​t​t​p​s​:​/​
/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​p​r​o​c​s​.​2​0​2​4​.​0​4​.​2​1​8
Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B, Grisel 
O, Blondel M, Prettenhofer P, Weiss R, Dubourg V, Vanderplas 
J, Passos A, Cournapeau D, Brucher M, Perrot M, Duchesnay É 
(2011) Scikit-learn: machine learning in python. J Mach Learn 
Res 12:2825–2830
1 3
Page 13 of 13 
   14 

```
