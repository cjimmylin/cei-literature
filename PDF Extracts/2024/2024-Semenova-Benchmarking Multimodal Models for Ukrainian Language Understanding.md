---
title: "2024-Semenova-Benchmarking Multimodal Models for Ukrainian Language Understanding - PDF Extract"
source_pdf: "2024-Semenova-Benchmarking Multimodal Models for Ukrainian Language Understanding.pdf"
pages: 16
extracted_at: "2026-02-13T09:50:31.289253"
---

# PDF Extract: 2024-Semenova-Benchmarking Multimodal Models for Ukrainian Language Understanding

**Source PDF:** 2024-Semenova-Benchmarking Multimodal Models for Ukrainian Language Understanding.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

Benchmarking Multimodal Models for Ukrainian Language Understanding
Across Academic and Cultural Domains
Yurii Paniv
Ukrainian Catholic University
paniv@ucu.edu.ua
Artur Kiulian
OpenBabylon
akiulian@gmail.com
Dmytro Chaplynskyi
lang-uk initiative
chaplinsky.dmitry@gmail.com
Mykola Khandoga
OpenBabylon
mkhandoga@gmail.com
Anton Polishko
OpenBabylon
anton.polishko@gmail.com
Tetiana Bas
Minerva University
tetiana@uni.minerva.edu
Guillermo Gabrielli
OpenBabylon
guillermo.gabrielli.fer@gmail.com
Abstract
While the evaluation of multimodal English-
centric models is an active area of research
with numerous benchmarks, there is a pro-
found lack of benchmarks or evaluation suites
for low- and mid-resource languages. We in-
troduce ZNO-Vision, a comprehensive multi-
modal Ukrainian-centric benchmark derived
from standardized university entrance exam-
ination (ZNO). The benchmark consists of over
4,300 expert-crafted questions spanning 12
academic disciplines, including mathematics,
physics, chemistry, and humanities. We evalu-
ated the performance of both open-source mod-
els and API providers, finding that only a hand-
ful of models performed above baseline. Along-
side the new benchmark, we performed the first
evaluation study of multimodal text generation
for the Ukrainian language: we measured cap-
tion generation quality on the Multi30K-UK
dataset, translated the VQA benchmark into
Ukrainian, and measured performance degrada-
tion relative to original English versions. Lastly,
we tested a few models from a cultural per-
spective on knowledge of national cuisine. We
believe our work will advance multimodal gen-
eration capabilities for the Ukrainian language
and our approach could be useful for other low-
resource languages.
1
Introduction
Vision-language models (VLMs) have expanded
LLM capabilities into more domains, allowing for
models to work with plenty of new tasks such as
OCR (Liu et al., 2024), image captioning, visual
question answering and many more.
While numerous benchmarks (Li et al., 2024)
evaluate VLMs performance across a range of
multimodal tasks, these resources primarily serve
English-language models, underscoring a critical
gap for evaluating VLMs in less-resourced lan-
guages. This absence is especially pronounced
for Ukrainian, where multimodal benchmarks are
exceedingly scarce.
Our work addresses this gap by introducing a
suite of Ukrainian-specific benchmarks and pre-
senting benchmarking results for leading propri-
etary and open-source VLMs. To estimate aca-
demic knowledge, we developed a new bench-
mark based on the External Independent Evalua-
tion (ZNO) - national university entrance exam (eie,
2024), which includes a large selection of questions
across various fields, such as chemistry, mathemat-
ics, Ukrainian language and literature, etc. Besides
that, we evaluated all models using Multi30K-UK
(Saichyshyna et al., 2023), one of the few exist-
ing Ukrainian multimodal benchmarks. Also, we
translated the VQA benchmark (Antol et al., 2015)
and measured the performance degradation com-
pared to the English version. Additionaly, for cul-
ture test, we developed a new multimodal bench-
mark, UACUISINE, based on 20 popular Ukrainian
dishes and finetuned Paligemma model on UACUI-
SINE training dataset, improving performance on
UACUISINE benchmark and VQA.
We believe that our effort would advance the de-
velopment of VLMs applications for the Ukrainian
language across academic and business sectors
worldwide, wherever it’s being used.
2
Related Work
Recent years have seen significant development
in multimodal benchmarks for evaluating VLMs.
Existing benchmarks can be broadly categorized
into three groups. General visual understanding
benchmarks include VQA (Antol et al., 2015) (1M+
question-answer pairs), GQA (Ainslie et al., 2023)
(compositional reasoning), and MMMU (Yue et al.,
2024) (broad domain reasoning). Cultural and mul-
tilingual benchmarks are represented by Cultur-
alVQA (Nayak et al., 2024) (11 countries), World-
Cuisines (Winata et al., 2024) (30 languages), and
MaXM (Changpinyo et al., 2023) (7 languages). Vi-
sual reasoning benchmarks feature CLEVR (John-
1
arXiv:2411.14647v1  [cs.CL]  22 Nov 2024

--- Page 2 ---

son et al., 2016) (compositional reasoning), A-
OKVQA (Schwenk et al., 2022) (external knowl-
edge), and Visual7W (Zhu et al., 2016) (semantic
understanding).
While these benchmarks provide comprehen-
sive evaluation frameworks, they predominantly
focus on English language capabilities. Recent
multilingual benchmarks often rely on translations
rather than culturally-grounded content, highlight-
ing a critical gap for evaluating VLMs in under-
represented languages like Ukrainian. Translation-
based benchmarks like xGQA (Pfeiffer et al., 2022)
(9,670 questions in 7 languages) often introduce
artifacts and fail to capture cultural nuances (Park
et al., 2024). Current cultural evaluations are either
too limited in scope (CulturalVQA: 2,378 questions
across 11 countries) or too narrow in focus (World-
Cuisines: food-specific across 30 languages). Ana-
lyzing the WorldCuisines, we found three critical
limitations regarding Ukrainian cuisine: (1) repre-
sentation was restricted solely to location identifi-
cation tasks without deeper cultural assessment, (2)
the selection of dishes failed to capture the breadth
of Ukrainian culinary traditions, and (3) several
dishes were incorrectly categorized as Ukrainian
while featuring Russian-language captions and rep-
resenting Russian cuisine variants.
3
Datasets & Methodology
ZNO multi-choice questions. External Indepen-
dent Evaluation (abbr. "ZNO" in Ukrainian) is
a national Ukrainian test for high school gradu-
ates (eie, 2024). This test is challenging for LLMs
even in text-only setting (Romanyshyn et al., 2024).
We gathered questions from Osvita portal (Osv,
2024), where an image is required for the answer.
Dataset consists of 4306 question-pair in 13 cat-
egories (overview in Appendix B): Math, Geog-
raphy, Ukrainian language and literature, Teach-
ing, History, Spanish, German, French, English,
Chemistry, Physics, Biology and Other (for a small
portion of unclassified questions). From our source
dataset, we filtered out questions with multiple
images, images as answers, and choice-matching
questions to streamline the setting for the bench-
mark, leaving only questions that require a single
letter (e.g., B) as an answer.
Multi30K-UK. We evaluated models for caption
generation task on Multi30K-UK (Saichyshyna
et al., 2023) dataset.
We use Flickr2017 and
Flickr2018 datasets as dev and test subsets respec-
tively.
Visual Question Answering (VQA) 2.0. We trans-
lated portions of an English-language benchmark
VQA 2.0 (Antol et al., 2015) to measure perfor-
mance degradation for translated Ukrainian multi-
modal evaluation. We used the standard evaluation
process for VQA (Agrawal et al., 2015) on a subset
of 1000 questions.
We used GPT-4o for translation due to its quality
(Paniv et al., 2024) and ability to work in long-
context setting. We selected 1,000 question-answer
pairs from VQA 2.0, preserving original associa-
tions and metadata.
UACUISINE Benchmark. In this dataset we ad-
dressed the issues with WorldCuisine dataset men-
tioned in section 2. The UACUISINE benchmark
consists of seven question types across three cate-
gories: (1) dish identification (three variants), (2)
text generation (ingredients and recipe), and (3)
characteristic classification (temperature and taste).
The identification questions were adapted from
WorldCuisines and translated into Ukrainian, while
preparation and classification questions were newly
introduced to assess deeper culinary understanding.
We curated a dataset of 20 most typical Ukrainian
dishes and annotated each with 7 question types in
Ukrainian, generating 140 question-answer pairs.
Evaluation Framework. For ZNO benchmark the
model is given an image and a natural language
question about the image. The expected answer
is a letter, e.g. A/B/C/D. The dataset contains
491/490/3325 (dev/validation/test) samples, each
making up an image, a question and multi-choice
answers encoded as letters.
54% of questions are pure visual questions to test
OCR capabilities for models. We prepend ques-
tions with a single prompt: "дай вiдповiдь на
питання i напиши варiант вiдповiдi в квадра-
тних дужках, наприклад: "[А]""(answer this
question and write the answer in quadratic braces,
in example "[A]"). We extraxt the last match for
quadratic braces using regular expression to repli-
cate the original setting of the test: final answer
could be counted only if it’s strictly in correct box.
For the translated VQA 2.0 benchmark, we mai-
ntained the original evaluation protocols (Agrawal
et al., 2015) to ensure comparability with English-
language results. Specifically, we used the VQA
accuracy metric that takes into account answer
agreement among multiple human annotators.
Evaluation for UACUISINE consists of three
metrics.
For the dish name prediction and
2

--- Page 3 ---

Model
ZNO val
ZNO test
Gemini Pro
0.680
0.675
Claude 3.5 Sonnet
0.651
0.643
Qwen2-VL-72B
0.496
0.512
GPT-4o
0.416
0.470
Qwen2-VL-7B
0.247
0.264
Baseline
0.224
0.219
Llama-3.2-11B
0.116
0.095
LLaVa-v1.6-mistral-7b
0.071
0.067
Paligemma-3b
0.049
0.058
Pixtral-12b
0.000
0.000
Table 1: Accuracy scores on ZNO dataset across di-
fferent models for validation and test subdatasets. More
detailed results could de found in Appendix A.
characteristic classification we use exact match
score (EM). For the ingredients generation, we use
a matching score called the Intersection Match (IM)
(detailed formulas for both of them in Appendix C).
For recipe generation evaluation, we use BERT
score (Zhang et al., 2020) using "bert-base-
multilingual-cased" model (Devlin et al., 2018) to
capture semantic similarity.
For Multi30K-UK, we use SacreBLEU (Post,
2018) and the same BERT score as well.
4
Experimental Setup
For each benchmark evaluation, we used their
specific metrics. For all generations, we used a
temperature equal to 1 and a maximum amount
of tokens equal to 300. We evaluated both propri-
etary and open-source multimodal language models
to provide a comprehensive assessment of current
capabilities on Ukrainian language tasks.
For
baseline evaluation of ZNO we select the first choi-
ce in each question, getting a 22% accuracy score.
We additionally evaluated a fine-tuned Pali-
gemma specifically on our UACUISINE training
dataset to assess the potential of domain adaptation.
Our training data includes 4,615 image-question-
answer triplets from UACUISINE training dataset.
We finetuned Paligemma using AdamW optimizer
with learning rate of 2e-5, batch size 4, gradient
accumulation steps 4.
5
Results & Discussion
In Table 1, Gemini 1.5 Pro (Team et al., 2024) and
Claude 3.5 Sonnet (Anthropic, 2024) demonstrated
the best results on ZNO benchmark, with Qwen2-
VL-72B
(Wang et al., 2024) being the only
Model
BLEU
BERT
Qwen2-VL-
72B
4.46 ± 3.82
0.728 ± 0.043
Paligemma-3b
4.36 ± 3.92
0.706 ± 0.045
Qwen2-VL-7B
3.35 ± 2.71
0.706 ± 0.039
Qwen2-VL-2B
2.08 ± 1.62
0.667 ± 0.050
LLaVa-v1.6-
mistral-7b
1.35 ± 1.24
0.620 ± 0.037
Pixtral-12b
0.39 ± 0.38
0.604 ± 0.032
Table 2: Average scores ± STD in BLEU and BERT on
Multi30k-UA dataset.
open source model to meaningfully beat a baseli-
ne. Surprisingly, GPT-4o (OpenAI et al., 2024)
performed worse than Qwen, and LLaMA 3.2
(Dubey et al., 2024), Paligemma-3B-mix-224
(Beyer et al., 2024) and Pixtral (Agrawal et al.,
2024) failed to even beat a baseline. The detailed
breakdown of models performance per question
category is provided in Appendix A.
As shown in Table 4,
the UACUISINE
benchmark reveals potential benefits of finetuni-
ng, showing that Paligemma can outmatch Qwen
with additional finetuning.
As shown in Table 2, testing caption generation
task on Multi30K-Uk dataset did not provide a
way to make conclusions about model performance.
The target domain is too different (model frequently
used synonyms) or did not follow instructions to
provide an answer in one sentence only.
Performance degradation in Ukrainian. Parallel
benchmarking in English and Ukrainian VQA
datasets provides an insight into language-induced
performance degradation as shown in Table 3. Whi-
le all the models demonstrated a certain degree of
performance degradation in Ukrainian, it varied
substantially. We attribute performance degradati-
on to translation model performance and assumpti-
on that models are more capable of understanding
and reasoning in English rather than in Ukraini-
an. While the former factor is a limitation of our
work, the latter is a manifestation of cultural and
linguistic bias by the models.
Instruction-following Issues. The most prevalent
challenge observed across models was inconsi-
stent instruction following in Ukrainian.
Even
high-performing models like GPT-4o and Gemi-
ni frequently failed to respond in expected format.
We have observed models replying in a much
more verbose way than expected by Multi30K and
3

--- Page 4 ---

Model
VQA-UA
VQA-EN
Qwen2-VL-7b
34.41
83.12
Paligemma-3b FT
34.19
78.71
Pixtral-12b
31.55
46.32
Gemini Pro
32.73
40.15
Paligemma-3b
29.38
79.40
GPT-4o
29.04
40.69
Llama3.2
27.57
42.41
Claude Sonnet
26.73
30.64
Table 3: Accuracy scores for VQA-1000-UA and VQA-
1000-EN datasets, sorted by VQA-UA in descending
order.
VQA, therefore we modified prompts with an extra
instruction to reply with one word for VQA or with
a sentence for Multi30K, but issue persisted.
Code-switching issues.
Besides instruction
following, we’ve observed major issues with code-
switching and language confusion. This behavior
was particularly pronounced in open-ended tasks
like recipe generation and ingredient listing in the
UACUISINE benchmark, where models would be
prompted in Ukrainian but switch to English, Chi-
nese or Russian for response. This suggests that
current VLMs experience the same code-switching
issues that are known to happen in text-only multi-
lingual LLMs (Kiulian et al., 2024).
We have
also observed the same issues of broken grammar
"Куряче супу з лапшой", non-existing words
generation (Хаширо-iтамэ, Курицики, Кулiби-
но)and tokenization artifacts (Рисotto).
Cultural misattribution. A key issue was cultural
appropriation, notably when Ukrainian Borsch
(UNESCO-recognized cultural heritage) was mi-
slabeled as "Russian Red Borscht." This pattern
extended to other Ukrainian dishes, with models
defaulting to English or Russian translations even
when prompted in Ukrainian. The misattributi-
on went beyond labeling - in recipe generation,
models often suggested Russian rather than traditi-
onal Ukrainian preparations. This systematic bias
points to training data issues that risk reinforcing
narratives diminishing Ukrainian cultural identity.
Addressing this requires both improved Ukraini-
an language capabilities and better integration of
accurate cultural knowledge in model training.
Fine-tuning observations. The fine-tuned Pali-
Gemma model demonstrated improvement in
Table 4 on the UACUISINE benchmark compared
to the base model, with exact match increasing
Model
BERT
EM
IM
Qwen2-VL-7B
0.53
0.31
0.25
Pixtral-12b
0.55
0.02
0.00
Llama3.2
0.57
0.01
0.25
Paligemma-3b
0.53
0.03
0.00
Paligemma FT (1 ep)
0.54
0.18
0.30
Paligemma FT (2 ep)
0.55
0.26
0.10
Paligemma FT (4 ep)
0.54
0.34
0.15
Table 4:
UACUISINE Evaluation Metrics Across
Models.
from 3% to 34% and intersection match improvi-
ng from 0% to 15%. This improvement suggests
that even limited domain-specific fine-tuning can
substantially enhance performance on culturally-
focused tasks. Notably, this specialization also
yields improved performance on the translated
Ukrainian VQA benchmark (+5.33%), while mai-
ntaining comparable performance on the English
VQA benchmark (slight -0.52% difference). These
results suggest that targeted fine-tuning on Ukraini-
an cultural content can enhance model performance
on Ukrainian language tasks without compromi-
sing general capabilities in English. We noticed
a clear limitation of the VLMs to perform non-
caption tasks that require more than general world
knowledge, especially things like providing cuisine
recipes, which manifests into low BERT score.
6
Conclusions
In this work, we introduced a suite of benchmarks
to evaluate VLMs in Ukrainian, addressing a cri-
tical gap in resources for low- and mid-resource
languages. ZNO benchmark enables researchers to
objectively estimate model performance for Ukrai-
nian multimodal generation on expert-made questi-
ons. Our paper also reveals stark performance
gaps between Ukrainian and English benchmarks
as measured on VQA, underscoring the challenges
faced by multimodal models in low-resource setti-
ng. We demonstrated the potential of targeted fine-
tuning to improve cultural and linguistic relevance
without sacrificing general capabilities.
Future
research directions should focus on extending
benchmarks to include more diverse, language-
specific tasks, addressing the culture gap. Beyond
Ukrainian, the methodologies introduced here
could serve as a template for advancing multimodal
language modelling in underrepresented languages,
enabling more inclusive access to AI instruments.
4

--- Page 5 ---

7
Limitations
While we believe that our work is a step forward in
evaluating the Ukrainian capabilities of VLMs, it
has a number of limitations.
In particular, the usage of machine translation
in translating the VQA dataset into the Ukraini-
an language might have introduced a bias, parti-
ally responsible for the degradation of performance
comparing to the original VQA benchmank.
Also, we have used the same prompt prefix for
all queries to all the tested models. It is possible
that this prompt might introduce a bias in model
comparison.
ZNO dataset is heavily skewed towards STEM
domains, having more than half of the questions
in these categories. Also, STEM categories have
the most visual-only questions (meaning that the
model has to rely on its OCR capabilities to answer
the question).
Multi30K provides both English and Ukrainian
captions for the same image, which makes it sui-
table for testing multi-modal translation task. We
haven’t performed such testing.
8
Ethical Considerations
Several ethical considerations arise in developing
and deploying multimodal benchmarks for Ukrai-
nian language evaluation.
Most critically, our
work addresses questions of cultural representati-
on and identity preservation, particularly salient
given current geopolitical contexts. The systematic
misattribution of Ukrainian cultural elements
by AI models highlights risks of technologi-
cal erasure of cultural identity.
While our
use of translated benchmarks enables comparati-
ve evaluation, this approach may inadvertently
perpetuate biases and fail to capture uniquely Ukrai-
nian contexts. Additionally, the observed tendency
of models to default to Russian or English translati-
ons, even when prompted in Ukrainian, raises
concerns about digital marginalization of Ukrainian
language users. These considerations underscore
the importance of developing culturally sensitive
evaluation frameworks that can help ensure AI
systems properly represent and serve Ukrainian
language users.
Acknowledgments
This research was made possible through generous
support from several organizations. We thank The
alliance of De Novo and MK-Consulting for
providing computational resources, and ELEKS
for their grant in memory of Oleksiy Skrypnyk.
We also gratefully acknowledge Amazon Web
Services (AWS) for cloud credits that enabled trai-
ning and inference on H200 instances, and Google
Cloud Platform (GCP) for credits supporting
model training and inference.
References
2024.
External independent evaluation.
Accessed:
2024-11-03.
2024. Osvita.ua test portal. Accessed: 2024-11-03.
Aishwarya Agrawal, Dhruv Batra, and Devi Parikh.
2015. Visual question answering (vqa) - evaluati-
on. Accessed: 2024-11-03.
Pravesh Agrawal, Szymon Antoniak, Emma Bou
Hanna, Baptiste Bout, Devendra Chaplot, Jessi-
ca Chudnovsky, Diogo Costa, Baudouin De Moni-
cault, Saurabh Garg, Theophile Gervet, Soham
Ghosh, Amélie Héliou, Paul Jacob, Albert Q. Jiang,
Kartik Khandelwal, Timothée Lacroix, Guillaume
Lample, Diego Las Casas, Thibaut Lavril, Teven Le
Scao, Andy Lo, William Marshall, Louis Martin,
Arthur Mensch, Pavankumar Muddireddy, Valera
Nemychnikova, Marie Pellat, Patrick Von Platen,
Nikhil Raghuraman, Baptiste Rozière, Alexandre
Sablayrolles, Lucile Saulnier, Romain Sauvestre,
Wendy Shang, Roman Soletskyi, Lawrence Stewart,
Pierre Stock, Joachim Studnia, Sandeep Subramani-
an, Sagar Vaze, Thomas Wang, and Sophia Yang.
2024. Pixtral 12b. Preprint, arXiv:2410.07073.
Joshua Ainslie, James Lee-Thorp, Michiel de Jong,
Yury Zemlyanskiy, Federico Lebrón, and Sumit
Sanghai. 2023. Gqa: Training generalized multi-
query transformer models from multi-head checkpoi-
nts. Preprint, arXiv:2305.13245.
Galen Andrew and Jianfeng Gao. 2007. Scalable traini-
ng of L1-regularized log-linear models. In Proceedi-
ngs of the 24th International Conference on Machine
Learning, pages 33–40.
Anthropic. 2024.
Claude 3.5 and claude with code
interpreter. Accessed: 2024-11-21.
Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu,
Margaret Mitchell, Dhruv Batra, C. Lawrence Zi-
tnick, and Devi Parikh. 2015. VQA: visual question
answering. CoRR, abs/1505.00468.
Lucas Beyer, Andreas Steiner, André Susano Pinto,
Alexander Kolesnikov, Xiao Wang, Daniel Salz,
Maxim Neumann, Ibrahim Alabdulmohsin, Michael
Tschannen, Emanuele Bugliarello, Thomas Unterthi-
ner, Daniel Keysers, Skanda Koppula, Fangyu Liu,
Adam Grycner, Alexey Gritsenko, Neil Houlsby,
Manoj Kumar, Keran Rong, Julian Eisenschlos,
Rishabh Kabra, Matthias Bauer, Matko Bošnjak,
5

--- Page 6 ---

Xi Chen, Matthias Minderer, Paul Voigtlaender,
Ioana Bica, Ivana Balazevic, Joan Puigcerver, Pi-
nelopi Papalampidi, Olivier Henaff, Xi Xiong, Radu
Soricut, Jeremiah Harmsen, and Xiaohua Zhai. 2024.
Paligemma: A versatile 3b vlm for transfer. Preprint,
arXiv:2407.07726.
Soravit Changpinyo, Linting Xue, Michal Yarom, Ashi-
sh V. Thapliyal, Idan Szpektor, Julien Amelot,
Xi Chen, and Radu Soricut. 2023. Maxm: Towards
multilingual visual question answering. Preprint,
arXiv:2209.05401.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kri-
stina Toutanova. 2018. BERT: pre-training of deep
bidirectional transformers for language understandi-
ng. CoRR, abs/1810.04805.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, Anirudh Goyal, Anthony Hartshorn, Aobo Yang,
Archi Mitra, Archie Sravankumar, Artem Korenev,
Arthur Hinsvark, Arun Rao, Aston Zhang, Aurelien
Rodriguez, Austen Gregerson, Ava Spataru, Bapti-
ste Roziere, Bethany Biron, Binh Tang, Bobbie
Chern, Charlotte Caucheteux, Chaya Nayak, Chloe
Bi, Chris Marra, Chris McConnell, Christian Keller,
Christophe Touret, Chunyang Wu, Corinne Wong,
Cristian Canton Ferrer, Cyrus Nikolaidis, Dami-
en Allonsius, Daniel Song, Danielle Pintz, Danny
Livshits, David Esiobu, Dhruv Choudhary, Dhruv
Mahajan, Diego Garcia-Olano, Diego Perino, Di-
euwke Hupkes, Egor Lakomkin, Ehab AlBadawy,
Elina Lobanova, Emily Dinan, Eric Michael Smith,
Filip Radenovic, Frank Zhang, Gabriel Synnaeve,
Gabrielle Lee, Georgia Lewis Anderson, Graeme
Nail, Gregoire Mialon, Guan Pang, Guillem Cucurell,
Hailey Nguyen, Hannah Korevaar, Hu Xu, Hugo
Touvron, Iliyan Zarov, Imanol Arrieta Ibarra, Isabel
Kloumann, Ishan Misra, Ivan Evtimov, Jade Copet,
Jaewon Lee, Jan Geffert, Jana Vranes, Jason Park,
Jay Mahadeokar, Jeet Shah, Jelmer van der Li-
nde, Jennifer Billock, Jenny Hong, Jenya Lee,
Jeremy Fu, Jianfeng Chi, Jianyu Huang, Jiawen
Liu, Jie Wang, Jiecao Yu, Joanna Bitton, Joe Spi-
sak, Jongsoo Park, Joseph Rocca, Joshua Johnstun,
Joshua Saxe, Junteng Jia, Kalyan Vasuden Alwala,
Kartikeya Upasani, Kate Plawiak, Ke Li, Kenneth
Heafield, Kevin Stone, Khalid El-Arini, Krithika
Iyer, Kshitiz Malik, Kuenley Chiu, Kunal Bhalla,
Lauren Rantala-Yeary, Laurens van der Maaten,
Lawrence Chen, Liang Tan, Liz Jenkins, Louis
Martin, Lovish Madaan, Lubo Malo, Lukas Blecher,
Lukas Landzaat, Luke de Oliveira, Madeline Muzzi,
Mahesh Pasupuleti, Mannat Singh, Manohar Paluri,
Marcin Kardas, Mathew Oldham, Mathieu Rita,
Maya Pavlova, Melanie Kambadur, Mike Lewis,
Min Si, Mitesh Kumar Singh, Mona Hassan, Naman
Goyal, Narjes Torabi, Nikolay Bashlykov, Nikolay
Bogoychev, Niladri Chatterji, Olivier Duchenne,
Onur Çelebi, Patrick Alrassy, Pengchuan Zhang,
Pengwei Li, Petar Vasic, Peter Weng, Prajjwal
Bhargava, Pratik Dubal, Praveen Krishnan, Punit Si-
ngh Koura, Puxin Xu, Qing He, Qingxiao Dong,
Ragavan Srinivasan, Raj Ganapathy, Ramon Calderer,
Ricardo Silveira Cabral, Robert Stojnic, Roberta Rai-
leanu, Rohit Girdhar, Rohit Patel, Romain Sauvestre,
Ronnie Polidoro, Roshan Sumbaly, Ross Taylor,
Ruan Silva, Rui Hou, Rui Wang, Saghar Hossei-
ni, Sahana Chennabasappa, Sanjay Singh, Sean
Bell, Seohyun Sonia Kim, Sergey Edunov, Shaoli-
ang Nie, Sharan Narang, Sharath Raparthy, Sheng
Shen, Shengye Wan, Shruti Bhosale, Shun Zhang, Si-
mon Vandenhende, Soumya Batra, Spencer Whitman,
Sten Sootla, Stephane Collot, Suchin Gururangan,
Sydney Borodinsky, Tamar Herman, Tara Fowler,
Tarek Sheasha, Thomas Georgiou, Thomas Scialom,
Tobias Speckbacher, Todor Mihaylov, Tong Xiao,
Ujjwal Karn, Vedanuj Goswami, Vibhor Gupta, Vi-
gnesh Ramanathan, Viktor Kerkez, Vincent Gonguet,
Virginie Do, Vish Vogeti, Vladan Petrovic, Wei-
wei Chu, Wenhan Xiong, Wenyin Fu, Whitney
Meers, Xavier Martinet, Xiaodong Wang, Xiaoqi-
ng Ellen Tan, Xinfeng Xie, Xuchao Jia, Xuewei
Wang, Yaelle Goldschlag, Yashesh Gaur, Yasmine
Babaei, Yi Wen, Yiwen Song, Yuchen Zhang, Yue
Li, Yuning Mao, Zacharie Delpierre Coudert, Zheng
Yan, Zhengxing Chen, Zoe Papakipos, Aaditya Si-
ngh, Aaron Grattafiori, Abha Jain, Adam Kelsey,
Adam Shajnfeld, Adithya Gangidi, Adolfo Vi-
ctoria, Ahuva Goldstand, Ajay Menon, Ajay Sharma,
Alex Boesenberg, Alex Vaughan, Alexei Baevski,
Allie Feinstein, Amanda Kallet, Amit Sangani,
Anam Yunus, Andrei Lupu, Andres Alvarado,
Andrew Caples, Andrew Gu, Andrew Ho, Andrew
Poulton, Andrew Ryan, Ankit Ramchandani, Annie
Franco, Aparajita Saraf, Arkabandhu Chowdhury,
Ashley Gabriel, Ashwin Bharambe, Assaf Ei-
senman, Azadeh Yazdan, Beau James, Ben Maurer,
Benjamin Leonhardi, Bernie Huang, Beth Loyd,
Beto De Paola, Bhargavi Paranjape, Bing Liu,
Bo Wu, Boyu Ni, Braden Hancock, Bram Wasti,
Brandon Spence, Brani Stojkovic, Brian Gamido,
Britt Montalvo, Carl Parker, Carly Burton, Catali-
na Mejia, Changhan Wang, Changkyu Kim, Chao
Zhou, Chester Hu, Ching-Hsiang Chu, Chris Cai,
Chris Tindal, Christoph Feichtenhofer, Damon Ci-
vin, Dana Beaty, Daniel Kreymer, Daniel Li, Danny
Wyatt, David Adkins, David Xu, Davide Testuggi-
ne, Delia David, Devi Parikh, Diana Liskovich,
Didem Foss, Dingkang Wang, Duc Le, Dustin
Holland, Edward Dowling, Eissa Jamil, Elaine
Montgomery, Eleonora Presani, Emily Hahn, Emi-
ly Wood, Erik Brinkman, Esteban Arcaute, Evan
Dunbar, Evan Smothers, Fei Sun, Felix Kreuk, Feng
Tian, Firat Ozgenel, Francesco Caggioni, Franci-
sco Guzmán, Frank Kanayet, Frank Seide, Gabri-
ela Medina Florez, Gabriella Schwarz, Gada Badeer,
Georgia Swee, Gil Halpern, Govind Thattai, Grant
Herman, Grigory Sizov, Guangyi, Zhang, Guna
Lakshminarayanan, Hamid Shojanazeri, Han Zou,
Hannah Wang, Hanwen Zha, Haroun Habeeb, Harri-
son Rudolph, Helen Suk, Henry Aspegren, Hunter
Goldman, Ibrahim Damlaj, Igor Molybog, Igor
Tufanov, Irina-Elena Veliche, Itai Gat, Jake Wei-
ssman, James Geboski, James Kohli, Japhet Asher,
Jean-Baptiste Gaya, Jeff Marcus, Jeff Tang, Jenni-
fer Chan, Jenny Zhen, Jeremy Reizenstein, Jeremy
6

--- Page 7 ---

Teboul, Jessica Zhong, Jian Jin, Jingyi Yang, Joe
Cummings, Jon Carvill, Jon Shepard, Jonathan
McPhie, Jonathan Torres, Josh Ginsburg, Junjie
Wang, Kai Wu, Kam Hou U, Karan Saxena, Karthik
Prasad, Kartikay Khandelwal, Katayoun Zand, Kathy
Matosich, Kaushik Veeraraghavan, Kelly Michelena,
Keqian Li, Kun Huang, Kunal Chawla, Kushal
Lakhotia, Kyle Huang, Lailin Chen, Lakshya Garg,
Lavender A, Leandro Silva, Lee Bell, Lei Zhang, Li-
angpeng Guo, Licheng Yu, Liron Moshkovich, Luca
Wehrstedt, Madian Khabsa, Manav Avalani, Manish
Bhatt, Maria Tsimpoukelli, Martynas Mankus, Matan
Hasson, Matthew Lennie, Matthias Reso, Maxim
Groshev, Maxim Naumov, Maya Lathi, Meghan
Keneally, Michael L. Seltzer, Michal Valko, Mi-
chelle Restrepo, Mihir Patel, Mik Vyatskov, Mi-
kayel Samvelyan, Mike Clark, Mike Macey, Mi-
ke Wang, Miquel Jubert Hermoso, Mo Metanat,
Mohammad Rastegari, Munish Bansal, Nandhini
Santhanam, Natascha Parks, Natasha White, Navyata
Bawa, Nayan Singhal, Nick Egebo, Nicolas Usuni-
er, Nikolay Pavlovich Laptev, Ning Dong, Ning
Zhang, Norman Cheng, Oleg Chernoguz, Olivia
Hart, Omkar Salpekar, Ozlem Kalinli, Parkin Kent,
Parth Parekh, Paul Saab, Pavan Balaji, Pedro Rittner,
Philip Bontrager, Pierre Roux, Piotr Dollar, Polina
Zvyagina, Prashant Ratanchandani, Pritish Yuvraj,
Qian Liang, Rachad Alao, Rachel Rodriguez, Rafi
Ayub, Raghotham Murthy, Raghu Nayani, Rahul Mi-
tra, Raymond Li, Rebekkah Hogan, Robin Battey,
Rocky Wang, Rohan Maheswari, Russ Howes, Ruty
Rinott, Sai Jayesh Bondu, Samyak Datta, Sara Chugh,
Sara Hunt, Sargun Dhillon, Sasha Sidorov, Satadru
Pan, Saurabh Verma, Seiji Yamamoto, Sharadh
Ramaswamy, Shaun Lindsay, Shaun Lindsay, Sheng
Feng, Shenghao Lin, Shengxin Cindy Zha, Shiva
Shankar, Shuqiang Zhang, Shuqiang Zhang, Sinong
Wang, Sneha Agarwal, Soji Sajuyigbe, Soumith Chi-
ntala, Stephanie Max, Stephen Chen, Steve Kehoe,
Steve Satterfield, Sudarshan Govindaprasad, Sumit
Gupta, Sungmin Cho, Sunny Virk, Suraj Subramani-
an, Sy Choudhury, Sydney Goldman, Tal Remez,
Tamar Glaser, Tamara Best, Thilo Kohler, Thomas
Robinson, Tianhe Li, Tianjun Zhang, Tim Matthews,
Timothy Chou, Tzook Shaked, Varun Vontimitta, Vi-
ctoria Ajayi, Victoria Montanez, Vijai Mohan, Vi-
nay Satish Kumar, Vishal Mangla, Vítor Albiero,
Vlad Ionescu, Vlad Poenaru, Vlad Tiberiu Mihai-
lescu, Vladimir Ivanov, Wei Li, Wenchen Wang,
Wenwen Jiang, Wes Bouaziz, Will Constable, Xi-
aocheng Tang, Xiaofang Wang, Xiaojian Wu, Xi-
aolan Wang, Xide Xia, Xilun Wu, Xinbo Gao,
Yanjun Chen, Ye Hu, Ye Jia, Ye Qi, Yenda Li, Yi-
lin Zhang, Ying Zhang, Yossi Adi, Youngjin Nam,
Yu, Wang, Yuchen Hao, Yundi Qian, Yuzi He, Zach
Rait, Zachary DeVito, Zef Rosnbrick, Zhaoduo Wen,
Zhenyu Yang, and Zhiwei Zhao. 2024. The llama 3
herd of models. Preprint, arXiv:2407.21783.
Justin Johnson, Bharath Hariharan, Laurens van der
Maaten, Li Fei-Fei, C. Lawrence Zitnick, and
Ross Girshick. 2016. Clevr: A diagnostic dataset
for compositional language and elementary visual
reasoning. Preprint, arXiv:1612.06890.
Artur Kiulian, Anton Polishko, Mykola Khandoga,
Oryna Chubych, Jack Connor, Raghav Ravishankar,
and Adarsh Shirawalmath. 2024.
From bytes
to borsch:
Fine-tuning gemma and mistral for
the ukrainian language representation.
Preprint,
arXiv:2404.09138.
Jian Li, Weiheng Lu, Hao Fei, Meng Luo, Ming
Dai, Min Xia, Yizhang Jin, Zhenye Gan, Ding Qi,
Chaoyou Fu, Ying Tai, Wankou Yang, Yabiao Wang,
and Chengjie Wang. 2024. A survey on benchmarks
of multimodal large language models.
Preprint,
arXiv:2408.08632.
Yuliang Liu, Zhang Li, Mingxin Huang, Biao Yang,
Wenwen Yu, Chunyuan Li, Xucheng Yin, Cheng lin
Liu, Lianwen Jin, and Xiang Bai. 2024. Ocrbench:
On the hidden mystery of ocr in large multimodal
models. Preprint, arXiv:2305.07895.
Shravan Nayak, Kanishk Jain, Rabiul Awal, Siva
Reddy, Sjoerd van Steenkiste, Lisa Anne Hendricks,
Karolina Sta´nczak, and Aishwarya Agrawal. 2024.
Benchmarking vision language models for cultural
understanding. Preprint, arXiv:2407.10920.
OpenAI, :, Aaron Hurst, Adam Lerer, Adam P. Goucher,
Adam Perelman, Aditya Ramesh, Aidan Clark,
AJ Ostrow, Akila Welihinda, Alan Hayes, Alec
Radford, Aleksander M ˛adry, Alex Baker-Whitcomb,
Alex Beutel, Alex Borzunov, Alex Carney, Alex
Chow, Alex Kirillov, Alex Nichol, Alex Paino,
Alex Renzin, Alex Tachard Passos, Alexander Ki-
rillov, Alexi Christakis, Alexis Conneau, Ali Kamali,
Allan Jabri, Allison Moyer, Allison Tam, Amadou
Crookes, Amin Tootoochian, Amin Tootoonchian,
Ananya Kumar, Andrea Vallone, Andrej Karpathy,
Andrew Braunstein, Andrew Cann, Andrew Codi-
spoti, Andrew Galu, Andrew Kondrich, Andrew
Tulloch, Andrey Mishchenko, Angela Baek, Angela
Jiang, Antoine Pelisse, Antonia Woodford, Anuj
Gosalia, Arka Dhar, Ashley Pantuliano, Avi Nayak,
Avital Oliver, Barret Zoph, Behrooz Ghorbani, Ben
Leimberger, Ben Rossen, Ben Sokolowsky, Ben
Wang, Benjamin Zweig, Beth Hoover, Blake Samic,
Bob McGrew, Bobby Spero, Bogo Giertler, Bowen
Cheng, Brad Lightcap, Brandon Walkin, Brendan
Quinn, Brian Guarraci, Brian Hsu, Bright Kellogg,
Brydon Eastman, Camillo Lugaresi, Carroll Wainwri-
ght, Cary Bassin, Cary Hudson, Casey Chu, Chad
Nelson, Chak Li, Chan Jun Shern, Channing Conger,
Charlotte Barette, Chelsea Voss, Chen Ding, Cheng
Lu, Chong Zhang, Chris Beaumont, Chris Hallacy,
Chris Koch, Christian Gibson, Christina Kim, Chri-
stine Choi, Christine McLeavey, Christopher Hesse,
Claudia Fischer, Clemens Winter, Coley Czarnecki,
Colin Jarvis, Colin Wei, Constantin Koumouzelis,
Dane Sherburn, Daniel Kappler, Daniel Levin, Dani-
el Levy, David Carr, David Farhi, David Mely,
David Robinson, David Sasaki, Denny Jin, Dev
Valladares, Dimitris Tsipras, Doug Li, Duc Phong
Nguyen, Duncan Findlay, Edede Oiwoh, Edmund
Wong, Ehsan Asdar, Elizabeth Proehl, Elizabeth
Yang, Eric Antonow, Eric Kramer, Eric Peterson, Eric
Sigler, Eric Wallace, Eugene Brevdo, Evan Mays,
7

--- Page 8 ---

Farzad Khorasani, Felipe Petroski Such, Filippo
Raso, Francis Zhang, Fred von Lohmann, Freddie
Sulit, Gabriel Goh, Gene Oden, Geoff Salmon, Giulio
Starace, Greg Brockman, Hadi Salman, Haiming Bao,
Haitang Hu, Hannah Wong, Haoyu Wang, Heather
Schmidt, Heather Whitney, Heewoo Jun, Hendrik
Kirchner, Henrique Ponde de Oliveira Pinto, Hongyu
Ren, Huiwen Chang, Hyung Won Chung, Ian Ki-
vlichan, Ian O’Connell, Ian O’Connell, Ian Osband,
Ian Silber, Ian Sohl, Ibrahim Okuyucu, Ikai Lan,
Ilya Kostrikov, Ilya Sutskever, Ingmar Kanitschei-
der, Ishaan Gulrajani, Jacob Coxon, Jacob Meni-
ck, Jakub Pachocki, James Aung, James Betker,
James Crooks, James Lennon, Jamie Kiros, Jan Leike,
Jane Park, Jason Kwon, Jason Phang, Jason Tepli-
tz, Jason Wei, Jason Wolfe, Jay Chen, Jeff Harris,
Jenia Varavva, Jessica Gan Lee, Jessica Shieh, Ji Lin,
Jiahui Yu, Jiayi Weng, Jie Tang, Jieqi Yu, Joanne
Jang, Joaquin Quinonero Candela, Joe Beutler, Joe
Landers, Joel Parish, Johannes Heidecke, John
Schulman, Jonathan Lachman, Jonathan McKay,
Jonathan Uesato, Jonathan Ward, Jong Wook Kim,
Joost Huizinga, Jordan Sitkin, Jos Kraaijeveld, Josh
Gross, Josh Kaplan, Josh Snyder, Joshua Achiam,
Joy Jiao, Joyce Lee, Juntang Zhuang, Justyn Harri-
man, Kai Fricke, Kai Hayashi, Karan Singhal, Katy
Shi, Kavin Karthik, Kayla Wood, Kendra Rimbach,
Kenny Hsu, Kenny Nguyen, Keren Gu-Lemberg,
Kevin Button, Kevin Liu, Kiel Howe, Krithika
Muthukumar, Kyle Luther, Lama Ahmad, Larry Kai,
Lauren Itow, Lauren Workman, Leher Pathak, Leo
Chen, Li Jing, Lia Guy, Liam Fedus, Liang Zhou, Li-
en Mamitsuka, Lilian Weng, Lindsay McCallum, Li-
ndsey Held, Long Ouyang, Louis Feuvrier, Lu Zhang,
Lukas Kondraciuk, Lukasz Kaiser, Luke Hewitt,
Luke Metz, Lyric Doshi, Mada Aflak, Maddie Si-
mens, Madelaine Boyd, Madeleine Thompson, Marat
Dukhan, Mark Chen, Mark Gray, Mark Hudnall,
Marvin Zhang, Marwan Aljubeh, Mateusz Litwin,
Matthew Zeng, Max Johnson, Maya Shetty, Mayank
Gupta, Meghan Shah, Mehmet Yatbaz, Meng Jia
Yang, Mengchao Zhong, Mia Glaese, Mianna Chen,
Michael Janner, Michael Lampe, Michael Petrov,
Michael Wu, Michele Wang, Michelle Fradin, Mi-
chelle Pokrass, Miguel Castro, Miguel Oom Temudo
de Castro, Mikhail Pavlov, Miles Brundage, Mi-
les Wang, Minal Khan, Mira Murati, Mo Bavarian,
Molly Lin, Murat Yesildal, Nacho Soto, Natalia Gi-
melshein, Natalie Cone, Natalie Staudacher, Natalie
Summers, Natan LaFontaine, Neil Chowdhury, Nick
Ryder, Nick Stathas, Nick Turley, Nik Tezak, Niko
Felix, Nithanth Kudige, Nitish Keskar, Noah Deutsch,
Noel Bundick, Nora Puckett, Ofir Nachum, Ola
Okelola, Oleg Boiko, Oleg Murk, Oliver Jaffe, Olivia
Watkins, Olivier Godement, Owen Campbell-Moore,
Patrick Chao, Paul McMillan, Pavel Belov, Peng Su,
Peter Bak, Peter Bakkum, Peter Deng, Peter Dolan,
Peter Hoeschele, Peter Welinder, Phil Tillet, Philip
Pronin, Philippe Tillet, Prafulla Dhariwal, Qiming
Yuan, Rachel Dias, Rachel Lim, Rahul Arora, Rajan
Troll, Randall Lin, Rapha Gontijo Lopes, Raul Puri,
Reah Miyara, Reimar Leike, Renaud Gaubert, Reza
Zamani, Ricky Wang, Rob Donnelly, Rob Honsby,
Rocky Smith, Rohan Sahai, Rohit Ramchandani,
Romain Huet, Rory Carmichael, Rowan Zellers, Roy
Chen, Ruby Chen, Ruslan Nigmatullin, Ryan Cheu,
Saachi Jain, Sam Altman, Sam Schoenholz, Sam Toi-
zer, Samuel Miserendino, Sandhini Agarwal, Sara
Culver, Scott Ethersmith, Scott Gray, Sean Grove,
Sean Metzger, Shamez Hermani, Shantanu Jain,
Shengjia Zhao, Sherwin Wu, Shino Jomoto, Shirong
Wu, Shuaiqi, Xia, Sonia Phene, Spencer Papay, Sri-
nivas Narayanan, Steve Coffey, Steve Lee, Stewart
Hall, Suchir Balaji, Tal Broda, Tal Stramer, Tao Xu,
Tarun Gogineni, Taya Christianson, Ted Sanders,
Tejal Patwardhan, Thomas Cunninghman, Thomas
Degry, Thomas Dimson, Thomas Raoux, Thomas
Shadwell, Tianhao Zheng, Todd Underwood, Todor
Markov, Toki Sherbakov, Tom Rubin, Tom Stasi,
Tomer Kaftan, Tristan Heywood, Troy Peterson, Tyce
Walters, Tyna Eloundou, Valerie Qi, Veit Moeller, Vi-
nnie Monaco, Vishal Kuo, Vlad Fomenko, Wayne
Chang, Weiyi Zheng, Wenda Zhou, Wesam Manassra,
Will Sheu, Wojciech Zaremba, Yash Patil, Yilei Qian,
Yongjik Kim, Youlong Cheng, Yu Zhang, Yuchen
He, Yuchen Zhang, Yujia Jin, Yunxing Dai, and
Yury Malkov. 2024. Gpt-4o system card. Prepri-
nt, arXiv:2410.21276.
Yurii Paniv, Dmytro Chaplynskyi, Nikita Trynus, and
Volodymyr Kyrylov. 2024. Setting up the data pri-
nter with improved English to Ukrainian machine
translation. In Proceedings of the Third Ukrainian
Natural Language Processing Workshop (UNLP) @
LREC-COLING 2024, pages 41–50, Torino, Italia.
ELRA and ICCL.
ChaeHun Park, Koanho Lee, Hyesu Lim, Jaeseok Kim,
Junmo Park, Yu-Jung Heo, Du-Seong Chang, and
Jaegul Choo. 2024.
Translation deserves better:
Analyzing translation artifacts in cross-lingual visual
question answering. Preprint, arXiv:2406.02331.
Jonas Pfeiffer, Gregor Geigle, Aishwarya Kamath, Jan-
Martin O. Steitz, Stefan Roth, Ivan Vuli´c, and Iryna
Gurevych. 2022. xgqa: Cross-lingual visual question
answering. Preprint, arXiv:2109.06082.
Matt Post. 2018. A call for clarity in reporting BLEU
scores. In Proceedings of the Third Conference on
Machine Translation: Research Papers, pages 186–
191, Belgium, Brussels. Association for Computati-
onal Linguistics.
Mariana Romanyshyn, Oleksiy Syvokon, and Roman
Kyslyi. 2024.
The UNLP 2024 shared task on
fine-tuning large language models for Ukrainian.
In Proceedings of the Third Ukrainian Natural
Language Processing Workshop (UNLP) @ LREC-
COLING 2024, pages 67–74, Torino, Italia. ELRA
and ICCL.
Nataliia Saichyshyna, Daniil Maksymenko, Oleksii
Turuta, Andriy Yerokhin, Andrii Babii, and Olena
Turuta. 2023.
Extension Multi30K: Multimodal
dataset for integrated vision and language research
in Ukrainian. In Proceedings of the Second Ukraini-
an Natural Language Processing Workshop (UNLP),
pages 54–61, Dubrovnik, Croatia. Association for
Computational Linguistics.
8

--- Page 9 ---

Dustin Schwenk, Apoorv Khandelwal, Christopher
Clark, Kenneth Marino, and Roozbeh Mottaghi. 2022.
A-okvqa: A benchmark for visual question answering
using world knowledge. Preprint, arXiv:2206.01718.
Gemini Team, Petko Georgiev, Ving Ian Lei, Ryan
Burnell, Libin Bai, Anmol Gulati, Garrett Tanzer,
Damien Vincent, Zhufeng Pan, Shibo Wang, Soroosh
Mariooryad, Yifan Ding, Xinyang Geng, Fred
Alcober,
Roy Frostig,
Mark Omernick,
Lexi
Walker, Cosmin Paduraru, Christina Sorokin, Andrea
Tacchetti, Colin Gaffney, Samira Daruki, Olcan
Sercinoglu, Zach Gleicher, Juliette Love, Paul Voi-
gtlaender, Rohan Jain, Gabriela Surita, Kareem
Mohamed, Rory Blevins, Junwhan Ahn, Tao Zhu,
Kornraphop Kawintiranon, Orhan Firat, Yiming Gu,
Yujing Zhang, Matthew Rahtz, Manaal Faruqui,
Natalie Clay, Justin Gilmer, JD Co-Reyes, Ivo
Penchev, Rui Zhu, Nobuyuki Morioka, Kevin Hui,
Krishna Haridasan, Victor Campos, Mahdis Mahdi-
eh, Mandy Guo, Samer Hassan, Kevin Kilgour,
Arpi Vezer, Heng-Tze Cheng, Raoul de Liedekerke,
Siddharth Goyal, Paul Barham, DJ Strouse, Seb
Noury, Jonas Adler, Mukund Sundararajan, Sharad
Vikram, Dmitry Lepikhin, Michela Paganini, Xavier
Garcia, Fan Yang, Dasha Valter, Maja Trebacz, Ki-
ran Vodrahalli, Chulayuth Asawaroengchai, Roman
Ring, Norbert Kalb, Livio Baldini Soares, Si-
ddhartha Brahma, David Steiner, Tianhe Yu, Fabi-
an Mentzer, Antoine He, Lucas Gonzalez, Bibo
Xu, Raphael Lopez Kaufman, Laurent El Shafey,
Junhyuk Oh, Tom Hennigan, George van den Dri-
essche, Seth Odoom, Mario Lucic, Becca Roelofs,
Sid Lall, Amit Marathe, Betty Chan, Santiago
Ontanon, Luheng He, Denis Teplyashin, Jonathan
Lai, Phil Crone, Bogdan Damoc, Lewis Ho, Sebasti-
an Riedel, Karel Lenc, Chih-Kuan Yeh, Aakanksha
Chowdhery, Yang Xu, Mehran Kazemi, Ehsan Amid,
Anastasia Petrushkina, Kevin Swersky, Ali Khodaei,
Gowoon Chen, Chris Larkin, Mario Pinto, Geng Yan,
Adria Puigdomenech Badia, Piyush Patil, Steven
Hansen, Dave Orr, Sebastien M. R. Arnold, Jordan
Grimstad, Andrew Dai, Sholto Douglas, Rishika
Sinha, Vikas Yadav, Xi Chen, Elena Gribovskaya,
Jacob Austin, Jeffrey Zhao, Kaushal Patel, Paul
Komarek, Sophia Austin, Sebastian Borgeaud, Li-
nda Friso, Abhimanyu Goyal, Ben Caine, Kris Cao,
Da-Woon Chung, Matthew Lamm, Gabe Barth-
Maron, Thais Kagohara, Kate Olszewska, Mia Chen,
Kaushik Shivakumar, Rishabh Agarwal, Harshal
Godhia, Ravi Rajwar, Javier Snaider, Xerxes Doti-
walla, Yuan Liu, Aditya Barua, Victor Ungureanu,
Yuan Zhang, Bat-Orgil Batsaikhan, Mateo Wirth,
James Qin, Ivo Danihelka, Tulsee Doshi, Martin
Chadwick, Jilin Chen, Sanil Jain, Quoc Le, Arjun
Kar, Madhu Gurumurthy, Cheng Li, Ruoxin Sang,
Fangyu Liu, Lampros Lamprou, Rich Munoz,
Nathan Lintz, Harsh Mehta, Heidi Howard, Malcolm
Reynolds, Lora Aroyo, Quan Wang, Lorenzo Blanco,
Albin Cassirer, Jordan Griffith, Dipanjan Das,
Stephan Lee, Jakub Sygnowski, Zach Fisher, James
Besley, Richard Powell, Zafarali Ahmed, Dominik
Paulus, David Reitter, Zalan Borsos, Rishabh Joshi,
Aedan Pope, Steven Hand, Vittorio Selo, Vihan Jain,
Nikhil Sethi, Megha Goel, Takaki Makino, Rhys May,
Zhen Yang, Johan Schalkwyk, Christina Butterfi-
eld, Anja Hauth, Alex Goldin, Will Hawkins, Evan
Senter, Sergey Brin, Oliver Woodman, Marvin Ri-
tter, Eric Noland, Minh Giang, Vijay Bolina, Li-
sa Lee, Tim Blyth, Ian Mackinnon, Machel Reid,
Obaid Sarvana, David Silver, Alexander Chen, Li-
ly Wang, Loren Maggiore, Oscar Chang, Nithya
Attaluri, Gregory Thornton, Chung-Cheng Chiu,
Oskar Bunyan, Nir Levine, Timothy Chung, Evgenii
Eltyshev, Xiance Si, Timothy Lillicrap, Demetra
Brady, Vaibhav Aggarwal, Boxi Wu, Yuanzhong Xu,
Ross McIlroy, Kartikeya Badola, Paramjit Sandhu,
Erica Moreira, Wojciech Stokowiec, Ross Hemsley,
Dong Li, Alex Tudor, Pranav Shyam, Elahe Rahi-
mtoroghi, Salem Haykal, Pablo Sprechmann, Xi-
ang Zhou, Diana Mincu, Yujia Li, Ravi Addanki,
Kalpesh Krishna, Xiao Wu, Alexandre Frechette,
Matan Eyal, Allan Dafoe, Dave Lacey, Jay Whang,
Thi Avrahami, Ye Zhang, Emanuel Taropa, Hanzhao
Lin, Daniel Toyama, Eliza Rutherford, Motoki Sano,
HyunJeong Choe, Alex Tomala, Chalence Safranek-
Shrader, Nora Kassner, Mantas Pajarskas, Matt
Harvey, Sean Sechrist, Meire Fortunato, Christina
Lyu, Gamaleldin Elsayed, Chenkai Kuang, James
Lottes, Eric Chu, Chao Jia, Chih-Wei Chen, Peter
Humphreys, Kate Baumli, Connie Tao, Rajkumar
Samuel, Cicero Nogueira dos Santos, Anders
Andreassen, Nemanja Raki´cevi´c, Dominik Grewe,
Aviral Kumar, Stephanie Winkler, Jonathan Caton,
Andrew Brock, Sid Dalmia, Hannah Sheahan, Iain
Barr, Yingjie Miao, Paul Natsev, Jacob Devlin,
Feryal Behbahani, Flavien Prost, Yanhua Sun, Arti-
om Myaskovsky, Thanumalayan Sankaranarayana
Pillai, Dan Hurt, Angeliki Lazaridou, Xi Xiong,
Ce Zheng, Fabio Pardo, Xiaowei Li, Dan Horgan,
Joe Stanton, Moran Ambar, Fei Xia, Alejandro Li-
nce, Mingqiu Wang, Basil Mustafa, Albert Webson,
Hyo Lee, Rohan Anil, Martin Wicke, Timothy Dozat,
Abhishek Sinha, Enrique Piqueras, Elahe Dabir,
Shyam Upadhyay, Anudhyan Boral, Lisa Anne
Hendricks, Corey Fry, Josip Djolonga, Yi Su, Jake
Walker, Jane Labanowski, Ronny Huang, Vedant
Misra, Jeremy Chen, RJ Skerry-Ryan, Avi Singh,
Shruti Rijhwani, Dian Yu, Alex Castro-Ros, Beer
Changpinyo, Romina Datta, Sumit Bagri, Arnar Mar
Hrafnkelsson, Marcello Maggioni, Daniel Zheng,
Yury Sulsky, Shaobo Hou, Tom Le Paine, Antoi-
ne Yang, Jason Riesa, Dominika Rogozinska, Dror
Marcus, Dalia El Badawy, Qiao Zhang, Luyu Wang,
Helen Miller, Jeremy Greer, Lars Lowe Sjos, Azade
Nova, Heiga Zen, Rahma Chaabouni, Mihaela Rosca,
Jiepu Jiang, Charlie Chen, Ruibo Liu, Tara Sai-
nath, Maxim Krikun, Alex Polozov, Jean-Baptiste
Lespiau, Josh Newlan, Zeyncep Cankara, Soo Kwak,
Yunhan Xu, Phil Chen, Andy Coenen, Clemens
Meyer, Katerina Tsihlas, Ada Ma, Juraj Gottweis,
Jinwei Xing, Chenjie Gu, Jin Miao, Christian Frank,
Zeynep Cankara, Sanjay Ganapathy, Ishita Dasgupta,
Steph Hughes-Fitt, Heng Chen, David Reid, Keran
Rong, Hongmin Fan, Joost van Amersfoort, Vincent
Zhuang, Aaron Cohen, Shixiang Shane Gu, Anhad
Mohananey, Anastasija Ilic, Taylor Tobin, John Wi-
eting, Anna Bortsova, Phoebe Thacker, Emma Wang,
9

--- Page 10 ---

Emily Caveness, Justin Chiu, Eren Sezener, Alex
Kaskasoli, Steven Baker, Katie Millican, Mohamed
Elhawaty, Kostas Aisopos, Carl Lebsack, Nathan
Byrd, Hanjun Dai, Wenhao Jia, Matthew Wiethoff,
Elnaz Davoodi, Albert Weston, Lakshman Yagati,
Arun Ahuja, Isabel Gao, Golan Pundak, Susan
Zhang, Michael Azzam, Khe Chai Sim, Sergi Caelles,
James Keeling, Abhanshu Sharma, Andy Swing,
YaGuang Li, Chenxi Liu, Carrie Grimes Bostock,
Yamini Bansal, Zachary Nado, Ankesh Anand, Josh
Lipschultz, Abhijit Karmarkar, Lev Proleev, Abe
Ittycheriah, Soheil Hassas Yeganeh, George Polovets,
Aleksandra Faust, Jiao Sun, Alban Rrustemi, Pen
Li, Rakesh Shivanna, Jeremiah Liu, Chris Welty,
Federico Lebron, Anirudh Baddepudi, Sebastian
Krause, Emilio Parisotto, Radu Soricut, Zheng
Xu, Dawn Bloxwich, Melvin Johnson, Behnam
Neyshabur, Justin Mao-Jones, Renshen Wang, Vinay
Ramasesh, Zaheer Abbas, Arthur Guez, Constant
Segal, Duc Dung Nguyen, James Svensson, Le Hou,
Sarah York, Kieran Milan, Sophie Bridgers, Wiktor
Gworek, Marco Tagliasacchi, James Lee-Thorp, Mi-
chael Chang, Alexey Guseynov, Ale Jakse Hartman,
Michael Kwong, Ruizhe Zhao, Sheleem Kashem, Eli-
zabeth Cole, Antoine Miech, Richard Tanburn, Mary
Phuong, Filip Pavetic, Sebastien Cevey, Ramona
Comanescu, Richard Ives, Sherry Yang, Cosmo Du,
Bo Li, Zizhao Zhang, Mariko Iinuma, Clara Hui-
yi Hu, Aurko Roy, Shaan Bijwadia, Zhenkai Zhu,
Danilo Martins, Rachel Saputro, Anita Gergely,
Steven Zheng, Dawei Jia, Ioannis Antonoglou, Adam
Sadovsky, Shane Gu, Yingying Bi, Alek Andreev,
Sina Samangooei, Mina Khan, Tomas Kocisky,
Angelos Filos, Chintu Kumar, Colton Bishop, Adams
Yu, Sarah Hodkinson, Sid Mittal, Premal Shah,
Alexandre Moufarek, Yong Cheng, Adam Bloniarz,
Jaehoon Lee, Pedram Pejman, Paul Michel, Stephen
Spencer, Vladimir Feinberg, Xuehan Xiong, Nikolay
Savinov, Charlotte Smith, Siamak Shakeri, Dustin
Tran, Mary Chesus, Bernd Bohnet, George Tucker,
Tamara von Glehn, Carrie Muir, Yiran Mao, Hideto
Kazawa, Ambrose Slone, Kedar Soparkar, Disha
Shrivastava, James Cobon-Kerr, Michael Sharman,
Jay Pavagadhi, Carlos Araya, Karolis Misiunas, Ni-
mesh Ghelani, Michael Laskin, David Barker, Qi-
ujia Li, Anton Briukhov, Neil Houlsby, Mia Glaese,
Balaji Lakshminarayanan, Nathan Schucher, Yunhao
Tang, Eli Collins, Hyeontaek Lim, Fangxiaoyu Feng,
Adria Recasens, Guangda Lai, Alberto Magni, Ni-
cola De Cao, Aditya Siddhant, Zoe Ashwood, Jordi
Orbay, Mostafa Dehghani, Jenny Brennan, Yifan He,
Kelvin Xu, Yang Gao, Carl Saroufim, James Molloy,
Xinyi Wu, Seb Arnold, Solomon Chang, Julian
Schrittwieser, Elena Buchatskaya, Soroush Radpour,
Martin Polacek, Skye Giordano, Ankur Bapna, Si-
mon Tokumine, Vincent Hellendoorn, Thibault Sotti-
aux, Sarah Cogan, Aliaksei Severyn, Mohammad
Saleh, Shantanu Thakoor, Laurent Shefey, Siyuan Qi-
ao, Meenu Gaba, Shuo yiin Chang, Craig Swanson,
Biao Zhang, Benjamin Lee, Paul Kishan Rubenstein,
Gan Song, Tom Kwiatkowski, Anna Koop, Ajay
Kannan, David Kao, Parker Schuh, Axel Stjerngren,
Golnaz Ghiasi, Gena Gibson, Luke Vilnis, Ye Yuan,
Felipe Tiengo Ferreira, Aishwarya Kamath, Ted Kli-
menko, Ken Franko, Kefan Xiao, Indro Bhattacharya,
Miteyan Patel, Rui Wang, Alex Morris, Robin
Strudel, Vivek Sharma, Peter Choy, Sayed Hadi
Hashemi, Jessica Landon, Mara Finkelstein, Pri-
ya Jhakra, Justin Frye, Megan Barnes, Matthew
Mauger, Dennis Daun, Khuslen Baatarsukh, Matthew
Tung, Wael Farhan, Henryk Michalewski, Fabio Vi-
ola, Felix de Chaumont Quitry, Charline Le Lan,
Tom Hudson, Qingze Wang, Felix Fischer, Ivy
Zheng, Elspeth White, Anca Dragan, Jean bapti-
ste Alayrac, Eric Ni, Alexander Pritzel, Adam
Iwanicki, Michael Isard, Anna Bulanova, Lukas Zi-
lka, Ethan Dyer, Devendra Sachan, Srivatsan Srini-
vasan, Hannah Muckenhirn, Honglong Cai, Amol
Mandhane, Mukarram Tariq, Jack W. Rae, Gary
Wang, Kareem Ayoub, Nicholas FitzGerald, Yao
Zhao, Woohyun Han, Chris Alberti, Dan Garrette,
Kashyap Krishnakumar, Mai Gimenez, Anselm
Levskaya, Daniel Sohn, Josip Matak, Inaki Iturrate,
Michael B. Chang, Jackie Xiang, Yuan Cao, Ni-
shant Ranka, Geoff Brown, Adrian Hutter, Vahab
Mirrokni, Nanxin Chen, Kaisheng Yao, Zoltan
Egyed, Francois Galilee, Tyler Liechty, Praveen
Kallakuri, Evan Palmer, Sanjay Ghemawat, Jasmine
Liu, David Tao, Chloe Thornton, Tim Green, Mi-
mi Jasarevic, Sharon Lin, Victor Cotruta, Yi-Xuan
Tan, Noah Fiedel, Hongkun Yu, Ed Chi, Alexander
Neitz, Jens Heitkaemper, Anu Sinha, Denny Zhou,
Yi Sun, Charbel Kaed, Brice Hulse, Swaroop Mi-
shra, Maria Georgaki, Sneha Kudugunta, Clement
Farabet, Izhak Shafran, Daniel Vlasic, Anton Tsi-
tsulin, Rajagopal Ananthanarayanan, Alen Carin,
Guolong Su, Pei Sun, Shashank V, Gabriel Carvajal,
Josef Broder, Iulia Comsa, Alena Repina, Willi-
am Wong, Warren Weilun Chen, Peter Hawkins,
Egor Filonov, Lucia Loher, Christoph Hirnschall,
Weiyi Wang, Jingchen Ye, Andrea Burns, Hardie
Cate, Diana Gage Wright, Federico Piccinini, Lei
Zhang, Chu-Cheng Lin, Ionel Gog, Yana Kuli-
zhskaya, Ashwin Sreevatsa, Shuang Song, Luis C.
Cobo, Anand Iyer, Chetan Tekur, Guillermo Garri-
do, Zhuyun Xiao, Rupert Kemp, Huaixiu Steven
Zheng, Hui Li, Ananth Agarwal, Christel Ngani, Kati
Goshvadi, Rebeca Santamaria-Fernandez, Wojci-
ech Fica, Xinyun Chen, Chris Gorgolewski, Sean
Sun, Roopal Garg, Xinyu Ye, S. M. Ali Eslami,
Nan Hua, Jon Simon, Pratik Joshi, Yelin Kim, Ian
Tenney, Sahitya Potluri, Lam Nguyen Thiet, Quan
Yuan, Florian Luisier, Alexandra Chronopoulou,
Salvatore Scellato, Praveen Srinivasan, Minmin
Chen, Vinod Koverkathu, Valentin Dalibard, Yami-
ng Xu, Brennan Saeta, Keith Anderson, Thibault
Sellam, Nick Fernando, Fantine Huot, Junehyuk
Jung, Mani Varadarajan, Michael Quinn, Amit Raul,
Maigo Le, Ruslan Habalov, Jon Clark, Komal
Jalan, Kalesha Bullard, Achintya Singhal, Thang
Luong, Boyu Wang, Sujeevan Rajayogam, Julian
Eisenschlos, Johnson Jia, Daniel Finchelstein, Alex
Yakubovich, Daniel Balle, Michael Fink, Sameer
Agarwal, Jing Li, Dj Dvijotham, Shalini Pal, Kai
Kang, Jaclyn Konzelmann, Jennifer Beattie, Olivi-
er Dousse, Diane Wu, Remi Crocker, Chen Elki-
nd, Siddhartha Reddy Jonnalagadda, Jong Lee,
Dan Holtmann-Rice, Krystal Kallarackal, Rosanne
10

--- Page 11 ---

Liu, Denis Vnukov, Neera Vats, Luca Invernizzi,
Mohsen Jafari, Huanjie Zhou, Lilly Taylor, Jenni-
fer Prendki, Marcus Wu, Tom Eccles, Tianqi Liu,
Kavya Kopparapu, Francoise Beaufays, Christof
Angermueller, Andreea Marzoca, Shourya Sarcar,
Hilal Dib, Jeff Stanway, Frank Perbet, Nejc Trdin,
Rachel Sterneck, Andrey Khorlin, Dinghua Li, Xi-
hui Wu, Sonam Goenka, David Madras, Sasha
Goldshtein, Willi Gierke, Tong Zhou, Yaxin Liu,
Yannie Liang, Anais White, Yunjie Li, Shreya Si-
ngh, Sanaz Bahargam, Mark Epstein, Sujoy Basu,
Li Lao, Adnan Ozturel, Carl Crous, Alex Zhai, Han
Lu, Zora Tung, Neeraj Gaur, Alanna Walton, Lucas
Dixon, Ming Zhang, Amir Globerson, Grant Uy,
Andrew Bolt, Olivia Wiles, Milad Nasr, Ilia Shumai-
lov, Marco Selvi, Francesco Piccinno, Ricardo Agui-
lar, Sara McCarthy, Misha Khalman, Mrinal Shukla,
Vlado Galic, John Carpenter, Kevin Villela, Haibin
Zhang, Harry Richardson, James Martens, Matko
Bosnjak, Shreyas Rammohan Belle, Jeff Seibert,
Mahmoud Alnahlawi, Brian McWilliams, Sankalp
Singh, Annie Louis, Wen Ding, Dan Popovici, Lenin
Simicich, Laura Knight, Pulkit Mehta, Nishesh
Gupta, Chongyang Shi, Saaber Fatehi, Jovana Mi-
trovic, Alex Grills, Joseph Pagadora, Dessie Petrova,
Danielle Eisenbud, Zhishuai Zhang, Damion Yates,
Bhavishya Mittal, Nilesh Tripuraneni, Yannis Assael,
Thomas Brovelli, Prateek Jain, Mihajlo Velimirovic,
Canfer Akbulut, Jiaqi Mu, Wolfgang Macherey,
Ravin Kumar, Jun Xu, Haroon Qureshi, Gheorghe
Comanici, Jeremy Wiesner, Zhitao Gong, Anton
Ruddock, Matthias Bauer, Nick Felt, Anirudh GP,
Anurag Arnab, Dustin Zelle, Jonas Rothfuss, Bi-
ll Rosgen, Ashish Shenoy, Bryan Seybold, Xinji-
an Li, Jayaram Mudigonda, Goker Erdogan, Ji-
awei Xia, Jiri Simsa, Andrea Michi, Yi Yao, Chri-
stopher Yew, Steven Kan, Isaac Caswell, Carey
Radebaugh, Andre Elisseeff, Pedro Valenzuela, Kay
McKinney, Kim Paterson, Albert Cui, Eri Latorre-
Chimoto, Solomon Kim, William Zeng, Ken Durden,
Priya Ponnapalli, Tiberiu Sosea, Christopher A.
Choquette-Choo, James Manyika, Brona Robenek,
Harsha Vashisht, Sebastien Pereira, Hoi Lam, Marko
Velic, Denese Owusu-Afriyie, Katherine Lee, Tolga
Bolukbasi, Alicia Parrish, Shawn Lu, Jane Park,
Balaji Venkatraman, Alice Talbert, Lambert Rosi-
que, Yuchung Cheng, Andrei Sozanschi, Adam
Paszke, Praveen Kumar, Jessica Austin, Lu Li, Khalid
Salama, Wooyeol Kim, Nandita Dukkipati, Anthony
Baryshnikov, Christos Kaplanis, XiangHai Sheng,
Yuri Chervonyi, Caglar Unlu, Diego de Las Casas,
Harry Askham, Kathryn Tunyasuvunakool, Felix
Gimeno, Siim Poder, Chester Kwak, Matt Miecni-
kowski, Vahab Mirrokni, Alek Dimitriev, Aaron Pari-
si, Dangyi Liu, Tomy Tsai, Toby Shevlane, Christi-
na Kouridi, Drew Garmon, Adrian Goedeckemeyer,
Adam R. Brown, Anitha Vijayakumar, Ali Elqursh,
Sadegh Jazayeri, Jin Huang, Sara Mc Carthy, Jay
Hoover, Lucy Kim, Sandeep Kumar, Wei Chen,
Courtney Biles, Garrett Bingham, Evan Rosen,
Lisa Wang, Qijun Tan, David Engel, Francesco
Pongetti, Dario de Cesare, Dongseong Hwang, Lily
Yu, Jennifer Pullman, Srini Narayanan, Kyle Levin,
Siddharth Gopal, Megan Li, Asaf Aharoni, Trieu
Trinh, Jessica Lo, Norman Casagrande, Roopali
Vij, Loic Matthey, Bramandia Ramadhana, Austin
Matthews, CJ Carey, Matthew Johnson, Kremena
Goranova, Rohin Shah, Shereen Ashraf, Kingshuk
Dasgupta, Rasmus Larsen, Yicheng Wang, Mani-
sh Reddy Vuyyuru, Chong Jiang, Joana Ijazi, Kazuki
Osawa, Celine Smith, Ramya Sree Boppana, Taylan
Bilal, Yuma Koizumi, Ying Xu, Yasemin Altun, Nir
Shabat, Ben Bariach, Alex Korchemniy, Kiam Choo,
Olaf Ronneberger, Chimezie Iwuanyanwu, Shubin
Zhao, David Soergel, Cho-Jui Hsieh, Irene Cai,
Shariq Iqbal, Martin Sundermeyer, Zhe Chen, Elie
Bursztein, Chaitanya Malaviya, Fadi Biadsy, Prakash
Shroff, Inderjit Dhillon, Tejasi Latkar, Chris Dyer,
Hannah Forbes, Massimo Nicosia, Vitaly Nikolaev,
Somer Greene, Marin Georgiev, Pidong Wang, Ni-
na Martin, Hanie Sedghi, John Zhang, Praseem
Banzal, Doug Fritz, Vikram Rao, Xuezhi Wang, Ji-
ageng Zhang, Viorica Patraucean, Dayou Du, Igor
Mordatch, Ivan Jurin, Lewis Liu, Ayush Dubey, Abhi
Mohan, Janek Nowakowski, Vlad-Doru Ion, Nan
Wei, Reiko Tojo, Maria Abi Raad, Drew A. Hudson,
Vaishakh Keshava, Shubham Agrawal, Kevin Rami-
rez, Zhichun Wu, Hoang Nguyen, Ji Liu, Madhavi
Sewak, Bryce Petrini, DongHyun Choi, Ivan Philips,
Ziyue Wang, Ioana Bica, Ankush Garg, Jarek Wi-
lkiewicz, Priyanka Agrawal, Xiaowei Li, Danhao
Guo, Emily Xue, Naseer Shaik, Andrew Leach,
Sadh MNM Khan, Julia Wiesinger, Sammy Jerome,
Abhishek Chakladar, Alek Wenjiao Wang, Tina
Ornduff, Folake Abu, Alireza Ghaffarkhah, Marcus
Wainwright, Mario Cortes, Frederick Liu, Joshua
Maynez, Andreas Terzis, Pouya Samangouei, Ri-
ham Mansour, Tomasz K˛epa, François-Xavier Aubet,
Anton Algymr, Dan Banica, Agoston Weisz, Andras
Orban, Alexandre Senges, Ewa Andrejczuk, Mark
Geller, Niccolo Dal Santo, Valentin Anklin, Majd Al
Merey, Martin Baeuml, Trevor Strohman, Junwen
Bai, Slav Petrov, Yonghui Wu, Demis Hassabis,
Koray Kavukcuoglu, Jeffrey Dean, and Oriol Vi-
nyals. 2024. Gemini 1.5: Unlocking multimodal
understanding across millions of tokens of context.
Preprint, arXiv:2403.05530.
Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhi-
hao Fan, Jinze Bai, Keqin Chen, Xuejing Liu,
Jialin Wang, Wenbin Ge, Yang Fan, Kai Dang,
Mengfei Du, Xuancheng Ren, Rui Men, Dayi-
heng Liu, Chang Zhou, Jingren Zhou, and Junyang
Lin. 2024. Qwen2-vl: Enhancing vision-language
model’s perception of the world at any resolution.
Preprint, arXiv:2409.12191.
Genta Indra Winata, Frederikus Hudi, Patrick Amadeus
Irawan, David Anugraha, Rifki Afina Putri, Yutong
Wang, Adam Nohejl, Ubaidillah Ariq Prathama,
Nedjma Ousidhoum, Afifa Amriani, Anar Rzayev,
Anirban Das, Ashmari Pramodya, Aulia Adila,
Bryan Wilie, Candy Olivia Mawalim, Ching Lam
Cheng, Daud Abolade, Emmanuele Chersoni, Enrico
Santus, Fariz Ikhwantri, Garry Kuwanto, Hanyang
Zhao, Haryo Akbarianto Wibowo, Holy Lovenia,
Jan Christian Blaise Cruz, Jan Wira Gotama Putra,
Junho Myung, Lucky Susanto, Maria Angelica Ri-
11

--- Page 12 ---

era Machin, Marina Zhukova, Michael Anugraha,
Muhammad Farid Adilazuarda, Natasha Santosa,
Peerat Limkonchotiwat, Raj Dabre, Rio Alexander
Audino, Samuel Cahyawijaya, Shi-Xiong Zhang,
Stephanie Yulia Salim, Yi Zhou, Yinxuan Gui,
David Ifeoluwa Adelani, En-Shiun Annie Lee, Shogo
Okada, Ayu Purwarianti, Alham Fikri Aji, Taro
Watanabe, Derry Tanti Wijaya, Alice Oh, and Chong-
Wah Ngo. 2024. Worldcuisines: A massive-scale
benchmark for multilingual and multicultural visual
question answering on global cuisines.
Preprint,
arXiv:2410.12705.
Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng,
Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Ji-
ang, Weiming Ren, Yuxuan Sun, Cong Wei, Botao
Yu, Ruibin Yuan, Renliang Sun, Ming Yin, Boyuan
Zheng, Zhenzhu Yang, Yibo Liu, Wenhao Huang,
Huan Sun, Yu Su, and Wenhu Chen. 2024. Mmmu:
A massive multi-discipline multimodal understandi-
ng and reasoning benchmark for expert agi. Preprint,
arXiv:2311.16502.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.
Weinberger, and Yoav Artzi. 2020.
Bertscore:
Evaluating text generation with bert.
Preprint,
arXiv:1904.09675.
Yuke Zhu, Oliver Groth, Michael Bernstein, and Li Fei-
Fei. 2016. Visual7w: Grounded question answering
in images. Preprint, arXiv:1511.03416.
A
Evaluation breakdown by category
12

--- Page 13 ---

Model
Mathematics
Geography
Ukrainian
Other
Kindergarten
History
Spanish
German
French
English
Chemistry
Physics
Biology
Gemini Pro
0.489
0.687
0.800
0.705
0.661
0.722
1.000
0.600
0.900
0.957
0.732
0.612
0.767
Claude 3.5 Sonnet
0.541
0.623
0.722
0.500
0.590
0.643
0.714
0.600
0.931
0.963
0.725
0.510
0.560
Qwen2-VL-72B
0.394
0.553
0.200
0.409
0.575
0.444
0.429
0.600
0.263
0.250
0.700
0.452
0.564
GPT-4o
0.609
0.260
0.100
0.182
0.195
0.167
0.143
0.000
0.100
0.171
0.747
0.550
0.218
Qwen2-VL-7B
0.244
0.260
0.200
0.205
0.247
0.333
0.000
0.000
0.019
0.006
0.389
0.291
0.233
Baseline
0.196
0.260
0.300
0.295
0.213
0.333
0.000
0.000
0.269
0.122
0.228
0.216
0.237
LLama-3.2-90B-Vision-
Instruct
0.0928
0.360
0.388
0.200
0.386
0.324
0.142
0.000
0.281
0.250
0.112
0.113
0.383
Qwen2-VL-2B
0.151
0.050
0.000
0.000
0.006
0.000
0.000
0.000
0.000
0.000
0.247
0.200
0.019
Llama-3.2-11B
0.062
0.150
0.000
0.159
0.124
0.111
0.143
0.000
0.106
0.213
0.061
0.066
0.154
LLaVa-v1.6-mistral-7b
0.061
0.100
0.000
0.068
0.052
0.056
0.000
0.000
0.006
0.037
0.087
0.078
0.049
Paligemma-3b
0.084
0.003
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.114
0.079
0.008
Pixtral-12b
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
Table 5: Performance metrics for ZNO test set, split by subject. The models highlighted are the best API model, Gemini, best open source model, Qwen2-VL-72B and Baseline -
always select first choice. Notably, Claude 3.5 Sonnet demonstrates a similarly strong capabilities as Gemini.
Model
Mathematics
Geography
Ukrainian
Other
Kindergarten
History
Spanish
German
French
English
Chemistry
Physics
Biology
Gemini Pro
0.476
0.649
0.526
0.400
0.711
0.767
1.000
0.833
0.900
0.950
0.804
0.576
0.667
Claude 3.5 Sonnet
0.500
0.675
0.526
0.300
0.666
0.697
1.000
0.666
0.850
0.950
0.754
0.590
0.515
Qwen2-VL-72B
0.366
0.514
0.368
0.200
0.356
0.651
0.429
0.500
0.300
0.100
0.745
0.470
0.606
GPT-4o
0.634
0.162
0.158
0.100
0.244
0.233
0.143
0.167
0.100
0.100
0.735
0.470
0.273
LLama-3.2-90B-Vision-
Instruct
0.134
0.351
0.105
0.100
0.288
0.418
0.428
0.166
0.250
0.400
0.107
0.212
0.575
Baseline
0.232
0.162
0.263
0.000
0.289
0.349
0.143
0.167
0.250
0.150
0.225
0.182
0.212
Llama-3.2-11B
0.049
0.189
0.105
0.100
0.111
0.140
0.000
0.167
0.200
0.250
0.098
0.121
0.121
Qwen2-VL-2B
0.195
0.054
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.206
0.167
0.030
LLaVa-v1.6-mistral-7b
0.061
0.027
0.053
0.000
0.089
0.163
0.000
0.000
0.000
0.050
0.059
0.152
0.000
Paligemma-3b
0.122
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.069
0.106
0.000
Pixtral-12b
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
Table 6: Performance metrics for ZNO validation set, split by subject. The models highlighted are the best API model, Gemini, best open source model, Qwen2-VL-72B and
Baseline - always select first choice. Notably, Claude 3.5 Sonnet demonstrates a similarly strong capabilities as Gemini.
13

--- Page 14 ---

B
ZNO Dataset Overview
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023
2024
Year
0
500
1000
1500
2000
2500
Number of Questions
Number of Questions by Year and Subject
Subject
Accounting and Finance
Administration
Biology
Chemistry
Economics
English Language
French Language
Geography
German Language
History of Ukraine
Law
Math
Physics
Political Science
Psychology
Spanish Language
Ukrainian Language
Ukrainian Literature
Figure 1: Distribution of ZNO questions by year and
subject, showing a skewed yet diverse distribution of
questions.
Category
Total
Visual-Only
Strictly-visual %
Chemistry
1,021
946
92.65%
Mathematics
821
771
93.91%
Physics
661
595
90.02%
History
434
0
0.00%
Geography
374
0
0.00%
Biology
332
0
0.00%
English language
204
0
0.00%
French language
199
0
0.00%
Kindergarten teaching
134
0
0.00%
Ukrainian language and literature
56
0
0.00%
Other
31
0
0.00%
Spanish language
22
20
90.91%
German language
17
0
0.00%
Table 7: Distribution of ZNO questions by category.
As we can see, STEM categories represent more than
a half of a dataset, even having more than 90% of all
visual-only questions (typical question has a text and
image, but in visual-only setting model hast to perform
OCR to answer the question).
14

--- Page 15 ---

Subset
# Questions
Visual-Only
Visual %
Dev
491
235
47.86%
Validation
490
233
47.55%
Test
3,325
1,864
56.06%
Total
4306
2332
54.16%
Table 8: Distribution of ZNO Dataset by subset. Dev
and Validation subset each represent 10% of all data
that can be used during model training.
C
UACUISINE Metrics
For the dish name prediction and characteristic
classification we use exact match score (EM):
EM(y, ˆy) = ⊮(y = ˆy)
(1)
where:
• EM is the exact match score
• y is the ground truth
• ˆy is the model prediction
This score is calculated on the stem level to account
for gender based noun changes in Ukrainian.
For the ingredients generation we use intersecti-
on match score (IM):
IM(y, ˆy) = |W(y) ∩W(ˆy)|
|W(y) ∪W(ˆy)|
(2)
where:
• IM is the intersection match score
• W(·) represents the set of words in a string
15

--- Page 16 ---

D
UACUISINE Questions
Ukrainian Question
English Translation
1. Identification Questions
Q1: Як називається ця страва?
Q1: What is this dish called?
Q2: Яка назва цiєї страви в Українi?
Q2: What is the name of this dish in Ukraine?
Q3: Я обiдаю в українському ресторанi. Зараз
я збираюся їсти цю страву. Як називається ця
страва?
Q3: I’m having lunch at a Ukrainian restaurant. I’m
about to eat this dish. What is this dish called?
2. Generation Questions
Q4: Перелiчи iнгредiєнти необхiднi для приго-
тування зображеної страви
Q4: List the ingredients needed to prepare the shown
dish
Q5: Як приготувати цю страву. Опиши коро-
тко покроковий рецепт.
Q5: How to prepare this dish. Describe briefly the
step-by-step recipe.
3. Binary Classification Questions
Q6: Яка ця страва на смак: солона чи солодка?
Q6: How does this dish taste: salty or sweet?
Q7: Ця страва подається холодна чи гаряча?
Q7: Is this dish served cold or hot?
Table 9: Ukrainian UACUISINE Questions with English
Translations
16

```
