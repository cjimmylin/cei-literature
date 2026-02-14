---\ntitle: "2025-results]]-IndicVisionBench Benchmarking Cultural and Multilingual Understanding - PDF Extract"\nsource_pdf: "2025/2025-results]]-IndicVisionBench Benchmarking Cultural and Multilingual Understanding.pdf"\npages: 39\nextracted_at: "2026-02-14T02:17:32.307956"\n---\n\n# PDF Extract: 2025-results]]-IndicVisionBench Benchmarking Cultural and Multilingual Understanding\n\n**Source PDF:** 2025/2025-results]]-IndicVisionBench Benchmarking Cultural and Multilingual Understanding.pdf\n**Total Pages:** 39\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nINDICVISIONBENCH:
BENCHMARKING CULTURAL
AND MULTILINGUAL UNDERSTANDING IN VLMS
Ali Faraz1, Akash2, Shaharukh Khan1, Raja Kolla1, Akshat Patidar1,
Suranjan Goswami2, Abhinav Ravi1, Chandra Khatri1, Shubham Agarwal1
1Krutrim AI, Bangalore, India
2OLA Electric, Bangalore, India
Contact: {ali.faraz, raja.kolla, shubham.agarwal1}@olakrutrim.com,{akash.shyam, suranjan.goswami}@olaelectric.com
ABSTRACT
Vision-language models (VLMs) have demonstrated impressive generalization
across multimodal tasks, yet most evaluation benchmarks remain Western-centric,
leaving open questions about their performance in culturally diverse and multi-
lingual settings. To address this gap, we introduce IndicVisionBench, the first
large-scale benchmark centered on the Indian subcontinent. Covering English and
10 Indian languages, our benchmark spans 3 multimodal tasks, including Opti-
cal Character Recognition (OCR), Multimodal Machine Translation (MMT), and
Visual Question Answering (VQA), covering 6 kinds of question types. Our fi-
nal benchmark consists of a total of 5K images and 37K+ QA pairs across 13
culturally grounded topics. In addition, we release a paired parallel corpus of an-
notations across 10 Indic languages, creating a unique resource for analyzing cul-
tural and linguistic biases in VLMs. We evaluate a broad spectrum of 8 models,
from proprietary closed-source systems to open-weights medium and large-scale
models. Our experiments reveal substantial performance gaps, underscoring the
limitations of current VLMs in culturally diverse contexts. By centering cultural
diversity and multilinguality, IndicVisionBench establishes a reproducible evalu-
ation framework that paves the way for more inclusive multimodal research.
1
INTRODUCTION
Vision-language models (VLMs) (Bai et al., 2023; Chen et al., 2024; Lu et al., 2024; Wang et al.,
2024b; Laurenc¸on et al., 2024; Tong et al., 2024; Xue et al., 2024) have demonstrated strong perfor-
mance across a variety of multimodal tasks. However, existing benchmarks (Antol et al., 2015; Fu
et al., 2023; Goyal et al., 2017) remain heavily Western-centric, limiting our understanding of how
these models generalize to culturally diverse and multilingual settings. India, in particular, represents
one of the most culturally and linguistically diverse regions globally, with 22 official languages and
28 states plus 8 Union Territories1 , each with distinct ethnic, visual, and cultural identities. While
some recent efforts partially cover this diversity (Romero et al., 2024; Nayak et al., 2024; Vayani
et al., 2025), a systematic, large-scale benchmark capturing India-specific cultural concepts across
multiple languages is still lacking.
To address this gap, we introduce IndicVisionBench, a culturally grounded evaluation benchmark
tailored for the Indian subcontinent. To the best of our knowledge, this is the first large-scale bench-
mark explicitly designed to assess VLMs in the context of Indian culture and languages. We use
states as a proxy for cultural groups following prior works (Adilazuarda et al., 2024; Nayak et al.,
2024). IndicVisionBench comprises 5K unique images and 37K+ question-answer pairs spanning 13
cultural topics, covering English and 10 medium-to-low resource Indic languages supporting three
multimodal tracks: Visual Question Answering (VQA), Optical Character Recognition (OCR), and
Multimodal Machine Translation (MMT). Figure 1 illustrates examples reflecting diverse cultural
1https://en.wikipedia.org/wiki/States_and_union_territories_of_India
1
arXiv:2511.04727v1  [cs.CV]  6 Nov 2025

--- Page 2 ---\n\nnuances, including monuments, food, and digitized text. Rigorous human verification and correc-
tion at every stage of data collection ensure the reliability and cultural fidelity of the benchmark,
covering medium-to-low resource languages including Hindi, Bengali, Tamil, Malayalam, Telugu,
Marathi, Kannada, Gujarati, Punjabi, and Oriya.
In this study, we evaluate 8 state-of-the-art (SOTA) VLMs on IndicVisionBench and find that per-
formance drops considerably for low-resource languages and culturally specific content. We also
observe a clear gap between proprietary and open-source models in their ability to capture linguistic
and cultural nuances across multimodal tasks. Analysis across scripts and language groups further
highlight the need for better support and representation of underrepresented regions and cultures.
IndicVisionBench
Image Sources
IVB-VQA-Parallel
IVB-MMT
IVB-VQA-EN
IVB - OCR
876
OCR Quality 
Filter
4117
Correction
3502
Crowd Sourcing
Wikisource
Internet Images
(topics and indian states based)
IVB-VQA-Indic
IVB - VQA
VLM based
generation
LLM based
translation
1113
106
1007
Quality Check
IndicVisionBench-MMT
English
A close-up, top view shows three dark brown, textured ragi mudde, a
traditional Indian dish, on a white plate. Above them, a white bowl filled
with a reddish-brown lentil soup, garnished with green cilantro leaves ...
Telugu
పై నుంండి తీసిన దగ్గరి దృశ్యంంలో తెల్లటి ప్లేట్‌లో మూడు ముదురు గోధుమ
రంగు, గరుకు ఆకృతి గల రాగి ముద్దే, ఒక సాంంప్రదాయ భారతీయ వంటకం
కనిపిస్తుంంది. వాటి పైన, ఆకుపచ్చ కొత్తిమీర ఆకులతో అలంకరించబడిన ...
IndicVisionBench-VQA
Question﻿
Based on the architectural style visible, how would you describe the
cultural significance of this fort in Indian history?
Question﻿
The distinct Mughal architectural style signifies its origin during the
Mughal Empire, representing a significant period of Indian heritage and
imperial power.
IndicVisionBench-OCR
Ground Truth﻿
ਚਰਚਾ ਸੀ ਪਈ ਬਲੋਚ ਸਰਦਾਰ ਹਾਸ਼ਮ ਖਾਂ ਨੇ ਹਜ਼ਾਾਰਾਂ ਰੁਪਏ ਮਕਬਰੇ ਤੇ ਅਤੇ 
ਖਰਾਇਤ ਵਿਚ ਖਰਚੇ। ਫਿਰ ਆਏ ਸਾਲ ਮੇਲਾ ਲਗਦਾ ਰਿਹਾ। ਨੱਜੋ ਦੇ ਖੂਹ 
ਦਾ ਮੇਲਾ। ਅਤੇ ਕਾਫਲੇ ਆਉਂਦੇ ਰਹੇ। ਗੁੱਜਰ ਆਉਂਦੇ ਪਰ ਬਲੋਚ ਕਾਫਲਾ 
ਕਦੀ ਨਾ ਆਇਆ।
Human
Correction
615
Image
Filter
Figure 1: IndicVisionBench (IVB) pipeline and 3 tracks. Top panel illustrates our image col-
lection pipeline for 10 Indian languages, showing the number of images at each step, with human
quality checks applied throughout. We also present sample outputs for the three tracks: VQA (Vi-
sual Question Answering) in English, MMT (Multimodal Machine Translation) in Telugu, and OCR
(Optical Character Recognition) in Punjabi. Further details are provided in Section 3.
Our contributions could thus be summarized as follows:
• We propose IndicVisionBench as the first large-scale, Indian-centric benchmark for evalu-
ating VLMs on culture-specific understanding, involving OCR, recognition, cultural identi-
fication, multi modal translation and semantic understanding involving 5K unique images.
• We conduct a comprehensive evaluation of 8 prominent closed-source as well as open-
weight models supporting Indian languages and contrast their performance across all the 3
tracks. We highlight systematic performance gaps that underscore the limitations of current
general-purpose VLMs in culturally diverse settings.
• We systematically study the regional-language biases, performance across topics and cross-
lingual variation in performance. We will open source this benchmark after acceptance, for
the future research in this direction.
2
RELATED WORK
Vision Language Models and Benchmarks.
Cross-attention models (Alayrac et al., 2022; Singh
et al., 2022) and later visual instruction tuning based auto-regressive models like the LLaVA fam-
2

--- Page 3 ---\n\nily (Liu et al., 2023a; 2024), have advanced multimodal learning, where vision encoders (Radford
et al., 2021; Zhai et al., 2023; Tschannen et al., 2025) are aligned with large language models. This
approach has since influenced a range of VLMs (Lu et al., 2024; Laurenc¸on et al., 2024; Tong et al.,
2024; Xue et al., 2024; Team et al., 2024), which follow similar design principles and achieve strong
results on translation, captioning, and multi-turn vision language benchmarks (Hudson & Manning,
2019; Fu et al., 2023; Yu et al., 2023). In contrast, multimodal models that handle Indic languages
remain relatively underexplored. Most open-source systems provide support only for 2 to 4 medium-
resource Indian languages (Maaz et al., 2024; Alam et al., 2025; Yue et al., 2025), with the notable
exception of Chitrarth (Khan et al., 2025b), which extends coverage to all ten languages, considered
in this work. We include all these models in our benchmark to assess their relative strengths.
Optical Character Recognition (OCR). OCR has progressed from early rule-based engines such
as Tesseract (Smith, 2007) to modern transformer-based approaches like TrOCR (Li et al., 2021) and
docTR (Liao et al., 2023). Recent efforts in document understanding further leverage multimodal
architectures, including the DocOwl series (Hu et al., 2024a;b), DocLLM (Wang et al., 2023), and
Donut (Kim et al., 2022). These systems are typically evaluated on benchmarks such as RVL-
CDIP (Harley et al., 2015), FUNSD (Jaume et al., 2019), and DocVQA (Mathew et al., 2021), to
name a few. Despite this progress, existing OCR benchmarks are largely English-centric, offering
minimal coverage of Indic scripts and multilingual contexts.
Multimodal
Machine
Translation
(MMT).
Recently,
Multimodal
Machine
Translation
(MMT) (Calixto & Liu, 2017; Elliott & K´ad´ar, 2017; Delbrouck & Dupont, 2017; Yao & Wan,
2020) has gained traction, where the translation leverages auxiliary modalities (e.g., images). Prior
works have largely centered on English-European language pairs (Elliott et al., 2016; Specia et al.,
2016), with a subset of medium-resource Indian languages (particularly Hindi, Bengali, Malayalam)
also explored in the shared task series (Nakazawa et al., 2019; 2020; 2021; 2022; 2023) based on
Visual Genome images (Krishna et al., 2017). We support a similar task based on a diverse set of
cultural images avoiding potential data contamination issues (Balloccu et al., 2024).
Cultural VQA.
Several benchmarks have begun probing cultural and multilingual reasoning in
VLMs. GD-VCR (Yin et al., 2021) and Henna (Alwajih et al., 2024) emphasize culturally specific
content but are largely limited to English or Arabic, while WorldCuisines (Winata et al., 2025)
focuses on food and cuisines. Multilingual benchmarks (Liu et al., 2023b; Zhang et al., 2023; Sun
et al., 2024; Das et al., 2024; Wang et al., 2024a; Fu et al., 2024a) expand language coverage but often
lack cultural and task diversity. Datasets like MaRVL (Liu et al., 2021) and xGQA (Pfeiffer et al.,
2021) broaden multilingual reasoning but do not incorporate Indic cultural grounding. Closest to our
work are CVQA (Romero et al., 2024), CulturalVQA (Nayak et al., 2024), and ALM-Bench (Vayani
et al., 2025), which partially touch on India-specific contexts, yet none offers a unified framework
capturing both Indic cultural diversity and multilingual multimodal evaluation.
3
BENCHMARK CREATION
Figure 1 illustrates our curation pipeline across all tracks; additional details are provided below.
3.1
INDICVISIONBENCH-VQA
We constructed the VQA split using two approaches: (i) controlled crowd-sourcing and (ii) large-
scale web crawling. In the first phase, we recruited volunteers (including authors) who contributed
images captured on their personal devices along with corresponding annotations. These images were
further reviewed to determine whether they were culturally specific to India and, if so, mapped to
one of 13 predefined topics and to the relevant State/Union Territory (UT). Irrelevant images were
discarded, resulting in 615 valid samples. As several categories and regions were underrepresented,
we expanded coverage in the second phase, where cultural experts systematically collected Creative
Commons–licensed images2 from Google Search, targeting roughly 100 per State/UT across the
same categories. This yielded 3,502 additional images, bringing the total corpus to 4,117 (3,797
region-specific and 320 pan-India).
2https://creativecommons.org/share-your-work/cclicenses/
3

--- Page 4 ---\n\nRajasthan
Question
संगीतकार द्वाारा पहना जाने वाला पारंपरिक परिधान क्याा है जो भारत में
उसके क्षेत्र को दर्शाता है?
Answer
उन्होंोंनेने एक सफेद कुर्ता और धोती पहनी हुई है, साथ में एक लाल पगड़ीी
और एक प्रिंटेड शॉल भी है, जो राजस्थान में सामान्य पारंपरिक वस्त्र हैं।
Tripura
Question
গলায় মহিলারা সাধারণত কোন ধরনের গহনা পরে থাকেন?
Answer
তারা বড় বড় একাধিক স্তর যুক্ত রুপোর গয়না পরে আছেন,
যেগুলি দেখতে পয়সার মতো চ্যাাপ্টাা চাকতি দিয়ে তৈরী।
Maharashtra
Question
वडापावसोबत सामान्यतः दिली जाणारी, तिच्याा तिखटपणासाठी प्रसिद्ध
असलेली कोणती गोष्ट ताटात दिसत आहे?
Answer
वडापावसोबत दोन चमकदार हिरव्याा मिरच्याा ठेवल्याा आहेत.
Tamilnadu
Question
சந்தைக் கடையில் காணப்படும் பாரம்பரிய இந்திய
கூரை வகை என்ன, இது பொதுவாக கிராமப்புற அல்லது
பாரம்பரிய அமைப்புகளில் காணப்படுகிறது?
Answer
சந்தைக் கடையானது ஓலையால் வேயப்பட்ட
கூரையைக் கொண்டுள்ளது, இது இந்தியாவின் பல
பகுதிகளில், குறிப்பாக சிறிய கடைகள் அல்லது
குடில்களுக்கு, ஒரு பொதுவான பாரம்பரிய மேற்கூரை
பாணியாகும்.
Karnataka
Question
ಹಿನ್ನೆಲೆಯಲ್ಲಿ ಯಾವ ರೀತಿಯ, ಸಾಮಾನ್ಯವಾಗಿ ಸಾರ್ವಜನಿಕ
ಸಾರಿಗೆಯಲ್ಲಿ ಬಳಸಲಾಗುವ ಸಾಂಪ್ರದಾಯಿಕ ಭಾರತೀಯ
ವಾಹನ ಗೋಚರಿಸುತ್ತದೆ?
Answer
ಹಿನ್ನೆಲೆಯಲ್ಲಿ ಹಳದಿ ಆಟೋ ರಿಕ್ಷಾ ಕಾಣಿಸುತ್ತಿದೆ.
Odisha
Question 
ରାସ୍ତାାରେ ଟଣାଯାଉଥିବା ଉଚ୍ଚ ରଥଗୁଡ଼ିକୁ କେଉଁ ରଙ୍ଗ ପ୍ରମୁଖ ଭାବରେ
ସଜାଯାଇଛି ?
Answer
ରଥଗୁଡ଼ିକ ଉଜ୍ଜ୍ୱଳ ନାଲି, ହଳଦିଆ, କଳା ଏବଂ ସବୁଜ ରଙ୍ଗର କପଡ଼ାାରେ ସୁନ୍ଦର
ଭାବରେ ସଜାଯାଇଛି ।
Figure 2: Examples from IndicVisionBench-VQA. Illustrative samples from different regions are
shown on the left. The map on the right depicts the regional distribution of images across India, with
counts per State/UT. Further details are provided in Section D of the Appendix.
Each image was first annotated with concise keywords by humans, expanded into intermediary
synthetic detailed captions using VLMs in English, and then used to generate six QAs per image:
two short-answer, one long-answer, one multiple-choice (single-correct), one True/False, and one
adversarial question. Notably, adversarial questions incorporate false assumptions, requiring models
to explicitly reject them, enabling a systematic probe of cultural knowledge beyond surface-level
recognition. We employed Gemini-1.5-Flash and Gemini-2.5-Flash (Gemini Team, Google, 2025)
for QA generation, informed by a small pilot study and cost considerations (see Appendix; Table 6).
Human reviewers then refined all outputs for factual accuracy and cultural alignment, resulting in a
balanced set of open-ended queries that jointly test recognition, reasoning, and robustness in VLMs.
Guidelines provided to annotators are detailed in Appendix E while Figure 22 shows the annotation
interface which we will open-source after acceptance.
From this pool of 4K+ images and their corresponding 6 QAs, we translated a subset into the dom-
inant regional language using text-only Gemini call, followed by human correction, resulting in
an VQA-Indic version. Additionally, we sampled a disjoint set of 106 images and translated them
into all 10 Indian languages, creating a VQA-Parallel corpus to systematically study cross-lingual
variation in VLMs’ cultural understanding and robustness.
3.2
INDICVISIONBENCH-MMT
The Multimodal Machine Translation (MMT) track extends the 106 images from the VQA-Parallel
corpus, where each English caption was translated into 10 Indic languages with access to the image
context. All translations were manually annotated to preserve meaning and align with cultural nu-
ances, resulting in a multimodal parallel dataset tailored for evaluating vision-grounded multimodal
translation in medium-to-low resource Indic languages.
3.3
INDICVISIONBENCH-OCR
For benchmarking OCR performance, we construct a multilingual corpus from Wikisource (Foun-
dation, 2025), a public-domain repository of digitized literary works. The corpus spans 10 Indic
languages and includes both printed and handwritten styles. To ensure reliability, we restrict collec-
tion to Level-4 verified pages, which have been human-reviewed on the platform. For each page, we
pair high-resolution scans (prppageimage) with their corresponding verified text (pagetext).
Further implementation details are provided in Appendix B.
4

--- Page 5 ---\n\nFigure 3: Data analysis on IndicVisionBench. Distribution of VQA questions by category (a) and
by language excluding English (b); average word counts for questions (c) and answers (d). For MMT
(e) shows caption word counts in Hindi; and for OCR average words per language (f).
4
INDICVISIONBENCH (IVB)
IndicVisionBench provides a diverse evaluation suite across 13 India-centric topics in English and
10 regional languages. Among Indic languages, Hindi dominates with 26.8% of QA pairs (Figure
3). For MMT, Hindi captions average 131 words, while OCR track word counts vary more widely,
with Hindi (329) and Gujarati (247) highest. Figure 5 shows that the dataset spans diverse cultural
categories, with largest shares in Heritage (12.4%), Religion (11.2%), Architecture (11.1%) and
Food (8.6%). More details in Appendix D.
Benchmark Tracks:
IndicVisionBench consists of three evaluation subsets: i). OCR: 876 docu-
ment images across 10 Indic languages. ii). VQA: 4,011 English and 1,007 multilingual culturally
grounded images with 6 QA types each. We also benchmark cross-lingual performance on a disjoint
set of 106 images with 6 paired questions across English and 10 Indic languages. iii). MMT: 106
image–caption pairs translated into 10 Indic languages, enabling multimodal translation.
Models Evaluated.
We evaluate three families of VLMs with varying degrees of Indic language
support: i). Proprietary models: Gemini-2.5 Flash (Gemini Team, Google, 2025), GPT-4o (OpenAI,
2023). ii). Large open-weight VLMs: Gemma-3-27B (Team et al., 2025), LLaMA-4-Maverick-
17B (LLaMA-4 for brevity) (Meta, 2025). iii). Medium-scale open-weight VLMs (7B): Maya
(Nahid Alam et al., 2024), PALO (Maaz et al., 2024), Pangea (Yue et al., 2025), and Chitrarth-1
(Khan et al., 2025b). For the OCR subset, we additionally include closed-source Chitrapathak3, de-
signed specifically for Indian languages as well as Chitranuvad (Khan et al., 2025a), winning entry
of the English-to-lowres4 MMT’ 24 (3 Indian languages) shared task (Parida et al., 2024).
Evaluation Metrics
We assess model performance using a combination of deterministic and
judgment-based metrics, tailored to each task. In the VQA track, Exact Match (refer Table 17)
is used for multiple-choice and True/False questions, while short/long-answer and adversarial ques-
tions are evaluated using LLM-as-a-Judge (GPT-4o, 0–10 scale) following prior works (Vayani et al.,
3https://bit.ly/chitrapathak
4https://www2.statmt.org/wmt24/multimodallowresmt-task.html
5

--- Page 6 ---\n\n2025) to capture contextual and cultural appropriateness (prompts in Appendix F). For the MMT
task, we evaluate performance using BLEU (Papineni et al., 2002) and RIBES (Isozaki et al., 2010)
scores across ten Indic languages, following the setup of prior shared tasks (Parida et al., 2024). For
OCR evaluation, we follow OCRBenchv2 (Fu et al., 2024b) and report Average Normalized Lev-
enshtein Similarity (ANLS) (Biten et al., 2019), along with Word Error Rate (WER) and Character
Error Rate (CER) as standard metrics (Smith, 2007; Neudecker et al., 2021).
Table 1: Model performances on English QAs in IndicVisionBench-VQA. Average scores of
different models for the six question-types. MCQ and True/False are binary (0–1), while Long
Answer, Short Answer-1, Short Answer-2, and Adversarial descriptive questions use a 0–10 scale.
The best score is shown in bold, and the second-best is underlined.
Model
MCQ ↑
True/False ↑
Long-answer ↑
Short-1 ↑
Short-2 ↑
Adversarial ↑
Maya
0.69
0.71
6.98
5.00
5.50
0.16
PALO
0.72
0.43
7.12
5.51
5.81
0.19
Pangea
0.85
0.37
7.01
6.72
6.95
0.67
Chitrarth-1
0.81
0.68
7.53
6.22
6.33
0.03
LLaMA-4
0.87
0.92
8.55
7.98
7.91
2.62
Gemma-3
0.87
0.88
8.56
7.68
7.61
1.50
GPT-4o
0.90
0.91
8.75
8.19
8.02
2.95
Gemini-2.5
0.94
0.95
9.30
8.58
8.49
5.79
5
RESULTS
VQA: Table 1 reports results on English subset of cultural VQA task. Gemini-2.5 achieves the
highest scores across all 6 question types, with GPT-4o and LLaMA-4 as the strongest challengers.
Binary-style questions (True/False, MCQ) yield the highest accuracy, while long-answer questions
also show robust performance. Short-answer types remains harder, reflecting the difficulty of con-
cise factual recall. This pattern highlights how answer format modulates model performance. In
multilingual settings, Gemini-2.5 continues to lead overall, while LLaMA-4 and Gemma-3 exhibit
comparable performance with language-specific strengths. GPT-4o consistently lags behind these
models, followed by the 7B variants. Among the 7B models, Chitrarth-1 generally outperforms
Pangea for short and long answer questions, with the latter holding an edge for MCQ and True/-
False questions. (Figure 4; Table 8 in Appendix on VQA-Indic). Adversarial questions, which
embed false assumptions, remains the most challenging both in English and Indic (Tables 1 and 2).
Though Gemini-2.5 consistently outperforms all models, even its scores are notably lower compared
to other QA types, reflecting the increased difficulty. On these select questions, GPT-4o is a distant
second, while both Gemma-3 and LLaMA-4 struggle across the board.
Figure 4: Model performances on IndicVisionBench-VQA-Parallel. Average scores across lan-
guages for the three open-ended (long and short) questions (on left) and scores across languages for
the structured tasks (True/False and MCQ) on the right.
6

--- Page 7 ---\n\nMMT: Gemini-2.5 also dominates the MMT track, with LLaMA-4 and Gemma-3 performing com-
parable across most languages in Table 3 based on both BLEU and RIBES metrics. LLaMA-4
attains second-best results in Bengali, Kannada, Malayalam, Odia, and Punjabi, while Gemma-3
ranks second in the remaining languages. Malayalam proves most challenging, with the sub-par per-
formance across all models. Chitranuvad, a finetuned version of Chitrarth-1 on Visual Genome (Kr-
ishna et al., 2017) for image grounded translation of English into 3 languages (Hindi, Bengali and
Malayalam), outperforms the base model Chitrarth-1 in Hindi, Kannada, Malayalam, and Telugu
but lags in Bengali despite being specifically fine-tuned for it. Nevertheless, both Chitranuvad and
Chitrarth-1 substantially outperform other 7B baselines (Maya, PALO, Pangea).
OCR: We report ANLS scores in Table 4, median WER/CER in 10. Gemini-2.5 leads across all
languages and metrics, achieving SOTA performance at both the word and character-level. OCR
difficulty remains language-dependent, with higher scores for Malayalam (59.64), Odia (41.7), Tel-
ugu (33.32), and Gujarati (24.09), underscoring persistent challenges in Indic scripts. At the word
level, closed-source Chitrapathak ranks second in nine languages (except Gujarati), followed closely
by LLaMA-4. Surprisingly, GPT-4o performs poorly in OCR with word-level ANLS scores (e.g.,
94.67 in Malayalam, 90.54 in Gujarati) significantly below expectations while 7B open-source mod-
els fall further behind.
Across all evaluation tracks, the closed-source Gemini-2.5 demonstrates clear superiority, while
Gemma-3 and LLaMA-4 show notable strengths with observed disparities across languages and
question types. We show qualitative results and more details in Appendix C.
Table 2: Model performances for Adversarial Questions in IndicVisionBench-VQA. We report
the average scores for only top 4 models since scores of other 7B models approached to 0. Even
proprietary models perform poorly on these kinds of hard and challenging questions.
Model
Bengali ↑
English ↑
Gujarati ↑
Hindi ↑
Kannada ↑
Malayalam ↑
Marathi ↑
Odia ↑
Punjabi ↑
Tamil ↑
Telugu ↑
LLaMA-4
0.38
2.62
0.52
1.18
0.14
0.33
0.81
0.53
1.03
1.14
0.07
Gemma-3
1.07
1.50
0.97
1.66
1.02
0.77
0.68
0.90
2.94
1.85
1.13
GPT-4o
2.23
2.95
3.10
2.25
0.67
2.28
2.89
1.82
4.00
1.70
2.04
Gemini-2.5
5.17
5.79
2.94
4.46
3.17
3.32
4.84
3.92
5.71
5.15
2.73
Table 3: Model performances on IndicVisionBench-MMT. RIBES (R) and BLEU (B) scores
across ten Indic languages, with Gemini-2.5 achieving the highest performance consistently.
Model
Bengali
Gujarati
Hindi
Kannada
Malayalam
Marathi
Odia
Punjabi
Tamil
Telugu
R ↑
B ↑
R ↑
B ↑
R ↑
B ↑
R ↑
B ↑
R ↑
B ↑
R ↑
B ↑
R ↑
B ↑
R ↑
B ↑
R ↑
B ↑
R ↑
B ↑
Maya
0.45
5.48
–
–
0.69
18.09
–
–
–
–
–
–
–
–
–
–
–
–
–
–
PALO
0.41
4.56
–
–
0.58
11.79
–
–
–
–
–
–
–
–
–
–
–
–
–
–
Pangea
0.69
16.84
–
–
0.75
25.29
–
–
–
–
–
–
–
–
–
–
0.43
5.40
0.62
12.52
Chitrarth-1
0.76
21.89
0.72
21.07
0.71
21.93
0.65
12.83
0.59
7.49
0.70
16.25
0.62
11.10
0.50
10.39
0.71
17.59
0.67
15.60
Chitranuvad
0.74
18.13
0.68
18.66
0.74
21.93
0.69
12.93
0.60
7.36
0.69
14.74
0.03
0.86
0.07
1.61
0.67
15.85
0.71
16.56
LLaMA-4
0.82
30.70
0.80
29.84
0.81
33.55
0.76
20.91
0.72
14.96
0.76
20.49
0.72
15.35
0.85
41.01
0.80
25.22
0.78
22.35
Gemma-3
0.81
29.75
0.83
35.76
0.82
34.40
0.72
16.23
0.68
10.29
0.80
26.96
0.65
8.56
0.81
32.48
0.82
29.97
0.82
31.35
GPT-4o
0.80
28.65
0.74
21.99
0.79
33.30
0.67
11.75
0.59
8.08
0.75
23.19
0.65
9.42
0.75
24.72
0.73
16.77
0.71
17.65
Gemini-2.5
0.87
44.51
0.90
53.27
0.83
38.91
0.80
30.08
0.81
28.65
0.88
47.00
0.85
39.08
0.89
52.39
0.88
46.32
0.87
44.85
Table 4: Model performances on IndicVisionBench-OCR: ANLS (Average Normalized Leven-
shtein Similarity) across 10 Indic languages for different models. ANLS-W and ANLS-C denote
word- and character-level scores, respectively. For each language, the highest score is marked in
bold, while the second-highest is underlined. Gemini-2.5 performs the best followed by Chitrap-
athak in most languages.
Model
Bengali
Gujarati
Hindi
Kannada
Malayalam
Marathi
Odia
Punjabi
Tamil
Telugu
Word ↓
Char ↓
Word ↓
Char ↓
Word ↓
Char ↓
Word ↓
Char ↓
Word ↓
Char ↓
Word ↓
Char ↓
Word ↓
Char ↓
Word ↓
Char ↓
Word ↓
Char ↓
Word ↓
Char ↓
Maya
99.42
95.77
-
-
99.70
94.91
-
-
-
-
-
-
-
-
-
-
-
-
-
-
PALO
96.30
91.15
-
-
99.26
91.98
-
-
-
-
-
-
-
-
-
-
-
-
-
-
Pangea
94.66
80.33
-
-
99.53
91.50
-
-
-
-
-
-
-
-
-
-
99.44
84.13
99.95
89.91
Chitrarth-1
96.16
84.65
99.32
86.81
98.56
89.81
99.58
85.29
99.62
94.77
99.66
86.58
99.99
93.21
99.16
90.17
99.10
89.94
99.86
89.02
LLaMA-4
31.52
13.21
40.56
18.38
25.73
11.91
36.90
11.17
75.50
45.75
20.94
8.05
97.51
86.78
29.77
12.68
31.36
10.79
57.07
18.72
Gemma-3
42.15
24.41
60.07
38.49
46.47
29.50
84.22
54.24
92.06
72.64
50.40
31.06
92.67
70.72
70.88
42.65
39.52
16.51
86.76
54.14
Chitrapathak
17.14
7.03
49.99
27.80
25.55
13.74
26.24
8.78
71.97
48.19
15.68
6.09
50.72
31.62
17.70
7.87
19.25
5.81
38.79
11.00
GPT-4o
55.51
32.68
90.54
68.03
54.62
35.54
94.33
69.79
94.67
78.47
63.44
37.93
94.61
73.46
68.88
40.71
74.35
43.39
95.97
70.08
Gemini-2.5
11.30
4.04
24.09
7.61
16.01
5.88
17.18
4.38
59.64
30.60
8.06
1.79
41.70
18.60
14.56
4.98
15.26
3.01
33.32
7.16
7

--- Page 8 ---\n\nTable 5: Are images necessary for IndicVisionBench-VQA-Parallel? Average performance drop
in short-answer questions across languages for Chitrarth-1, Gemma-3, and Gemini-2.5, comparing
with vs. without image input.
Model
Type
Bengali
↑
English
↑
Gujarati
↑
Hindi
↑
Kannada
↑
Malayalam
↑
Marathi
↑
Odia
↑
Punjabi
↑
Tamil
↑
Telugu
↑
Chitrarth-1
w/o img
3.88
4.18
3.76
4.09
4.07
3.99
4.53
4.06
4.52
3.88
4.23
with img
5.90
5.95
5.76
5.97
5.58
4.68
5.61
5.11
5.43
4.93
5.50
Gemma-3
w/o img
4.21
3.25
4.30
4.47
3.90
4.23
4.31
3.54
4.15
4.26
4.44
with img
6.67
6.98
7.08
6.87
6.29
6.41
6.58
5.94
6.80
6.92
6.93
Gemini-2.5
w/o img
4.69
4.14
4.62
4.76
4.29
4.69
4.57
4.80
4.60
4.24
4.66
with img
8.09
8.22
7.90
8.33
7.57
7.89
7.99
7.72
8.15
7.96
7.76
6
DISCUSSION
VLMs without vision: Are images necessary?
We evaluate models on the paired VQA-Parallel
corpus spanning 10 Indic languages plus English, comparing performance with and without visual
input. Removing images leads to a substantial drop in accuracy, most pronounced for short-answer
tasks (see Table 5) where precise, detail-oriented responses are required. Long-answer questions
are comparatively more resilient, though still affected. Across the representative models of each
category: Chitrarth-1, Gemma-3, and Gemini-2.5, the trend is consistent (Table 9 in Appendix),
showcasing that visual grounding is necessary for answering questions in our VQA benchmark.
Do VLMs exhibit cross-lingual variations in performance?
We systematically conducted a
study on the VQA-Parallel corpus to measure the cross-lingual performance across 11 languages
including English. For the long answer, Gemini-2.5 achieves the best overall performance, followed
by Gemma-3, which ranks second in all languages except Odia, where it surpasses even GPT-4o.
On the MCQ type questions, GPT-4o and LLaMA-4 perform comparable across all languages (next
to Gemini-2.5) as in Table 7, while Chitrarth-1 consistently outperforms all other 7B-scale mod-
els. Among the 7B-scale models, Chitrarth-1 again proves strongest, followed by Maya. In the
adversarial question, Gemini remains the best-performing model but shows a considerable drop in
performance compared to its long-form results. Excluding English, Gemma-3 consistently outper-
forms both GPT-4o and LLaMA-4 across all Indian languages, while LLaMA-4 maintains a slight
advantage over Gemma-3 in English. For short-answer questions, LLaMA-4 generally secures the
second rank, but falls behind Gemma-3 in Tamil and Telugu, and performs particularly poorly in
Gujarati and Kannada. Nonetheless, both LLaMA-4 and Gemma-3 outperform GPT-4o across all
languages. In the True/False setting, GPT-4o ranks second in Bengali, Punjabi, Telugu, and English.
By contrast, Gemma-3 shows notable weaknesses in Bengali, Punjabi, and Telugu, even trailing
behind Chitrarth-1 in Punjabi and Bengali.
Do VLMs perform better in some cultural topics in English?
Model performance also varies
by cultural category. As shown in Figure 5, Gemini-2.5 consistently achieves the strongest results
across topics with slight variations, establishing itself as the most reliable model. LLaMA-4 and
Gemma-3 show advantages on certain topics, while GPT-4o retains a slight edge in others over
both. Among 7B models, Chitrarth-1 and Pangea demonstrate moderate and roughly comparable
capabilities, whereas Maya and PALO cluster together at the lower end. These topics-level patterns
suggest that stronger models generalize more evenly across cultural domains, while weaker ones
exhibit sharper inconsistencies.
Do VLMs know more about certain regions or show regional-language biases?
We investigate
whether VLMs exhibit region-specific strengths or biases by comparing performance across cultural
images from different Indian regions (states) and the corresponding multilingual queries. Gemini-
2.5 (Figure 6) generally performs well across regions but consistently struggles with Odia cultural
content, regardless of query language. Across models, English questions yield the best results,
followed by Hindi and Bengali, with no clear alignment between the region depicted in the image
and the language of the query. Among open-weight models (Figure 7 in Appendix), Gemma-3
favors Punjabi, Marathi, and Bengali, while LLaMA-4 performs best on Punjabi and Hindi content.
7B Chitrarth-1 records its lowest scores on Odia and Punjabi and often performs better in English
than in native Indic languages for Hindi-speaking states. Pangea performs strongest in English and
weakest in Tamil, with also a bias toward Tamil-language queries. Maya and PALO remain relatively
stable in English but show weaknesses in Hindi and Bengali, respectively. These results suggest that
8

--- Page 9 ---\n\nFigure 5: Performance across topics in IndicVisionBench-VQA. Distribution of categories of
questions (on left) and model performances averaged over the two short and a long answer open-
ended questions (on right). Gemini-2.5 shows comparable performance across all topics.
Figure 6: Average performance on open-ended question (Long and Short answer types).
Gemini-2.5 (on left), GPT-4o (right) and other models in Figure 7 in Appendix. X-axis displays
query languages and Y-axis displays Indian states grouped by dominant language. Numbers in
parentheses indicate the count of states for dominant language.
9

--- Page 10 ---\n\nwhile certain region–language preferences exist, systematic region-level cultural alignment is largely
absent, with Odia emerging as a consistently difficult case across all models.
How do we evaluate OCR outputs?
Apart from the ANLS metric, we also report average and
median WER/CER metrics (Tables 11 and 12 in the Appendix), based on Levenshtein Distance
(Lcvenshtcin, 1966). Mathematically, this metric is unbounded and can over-penalize models for a
few extreme cases (e.g., inflated scores for LLaMA-4 repetition upto maximum length; see Figure
8). To quantify this effect, we report in Table 13, the proportion of instances exceeding a value of 1.
Notably, LLaMA-4 accounts for only 7% of such cases, yet includes strong outliers with an average
worst-case WER of 25 in Malayalam, while still ranking third best under ANLS which remains
relatively robust to these anomalies. While underexplored for LLMs and VLMs, that often produce
long repetitive outputs (Hiraoka & Inui, 2024), even median-based reporting (Patel et al., 2025)
fails to capture such edge cases. Other statistical alternatives like Word Recognition Rate (WRR)
/ Character Recognition Rate (CRR) (Bhattacharyya et al., 2025) ignore ordering in the outputs, so
we adopt ANLS as the most interpretable metric in our setting.
7
CONCLUSION
We present IndicVisionBench, a large-scale benchmark consisting of 5K unique images, 37K+
questions spanning 13 culturally grounded topics across English and 10 Indic languages. Covering
VQA (6 kind of questions), OCR, and MMT tasks, it combines curated images with linguistically
diverse queries to probe recognition, reasoning, and translation. Experiments with proprietary and
open-weight models reveal substantial performance gaps, especially in low-resource languages and
culturally nuanced settings. By centering cultural and linguistic diversity, our work provides a re-
producible foundation for building more inclusive and globally robust multimodal systems.
ETHICS AND REPRODUCIBILITY STATEMENT
Ethics Statement
This work focuses on the responsible development of an evaluation benchmark
for multimodal cultural understanding in regional Indian contexts and languages, spanning diverse
tasks. We applied careful filtering to reduce harmful or unsafe content, though model outputs remain
beyond our full control. All external datasets and tools are properly cited. Human involvement was
limited to annotation and quality control; no sensitive or personally identifiable information (PII)
was collected. Participants were informed that their contributed images and annotations would be
used in a VLM benchmark and provided prior consent, with instructions to obscure any identifiable
information. Dataset curation was performed by a team of in-house annotators who were fairly com-
pensated according to local market standards. As the study did not involve personal or medical data,
formal IRB approval was not required. Throughout the process, we prioritized preserving cultural
nuance while minimizing bias and harm. Despite careful filtering, dataset bias may remain, reflect-
ing regional, socio-economic, or cultural imbalances. The resulting benchmark aims to support the
development of multilingual and culturally inclusive vision-language models.
Reproducibility Statement
To support reproducibility, we will release all benchmark-related arti-
facts publicly, along with detailed documentation. Our experimental setups and evaluation protocols
are thoroughly recorded to facilitate precise replication of results. For components involving human
annotation or judgment, we include the instructions and guidelines followed, ensuring transparency
and consistency throughout the process.
ACKNOWLEDGMENTS
We express our sincere gratitude to the leadership at Krutrim for their unwavering support through-
out the course of this research. We would also like to thank the AI Research team at Krutrim for
their valuable feedback and insightful discussions during various stages of the project, as well as the
Krutrim team members who contributed to data collection. We further acknowledge the dedicated
efforts of the data collection and annotation teams, including Sanmathi and Aravind, for their work
in building this benchmark. Our experiments were conducted with generous computational support
from Krutrim Cloud using Krutrim credits.
10

--- Page 11 ---\n\nREFERENCES
Muhammad Farid Adilazuarda, Sagnik Mukherjee, Pradhyumna Lavania, Siddhant Singh, Al-
ham Fikri Aji, Jacki O’Neill, Ashutosh Modi, and Monojit Choudhury. Towards measuring and
modeling” culture” in llms: A survey. arXiv preprint arXiv:2403.15412, 2024.
Nahid Alam, Karthik Reddy Kanjula, Surya Guthikonda, Timothy Chung, Bala Krishna S Vegesna,
Abhipsha Das, Anthony Susevski, Ryan Sze-Yin Chan, SM Uddin, Shayekh Bin Islam, et al.
Behind maya: Building a multilingual vision language model. arXiv preprint arXiv:2505.08910,
2025.
Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel
Lenc, Arthur Mensch, Katherine Millican, Malcolm Reynolds, et al. Flamingo: a visual language
model for few-shot learning. Advances in neural information processing systems, 35:23716–
23736, 2022.
Fakhraddin Alwajih, El Moatez Billah Nagoudi, Gagan Bhatia, Abdelrahman Mohamed, and
Muhammad Abdul-Mageed. Peacock: A family of arabic multimodal large language models
and benchmarks. arXiv preprint arXiv:2403.01031, 2024.
Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu, Margaret Mitchell, Dhruv Batra, C Lawrence Zit-
nick, and Devi Parikh. Vqa: Visual question answering. In Proceedings of the IEEE international
conference on computer vision, pp. 2425–2433, 2015.
Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang
Zhou, and Jingren Zhou. Qwen-VL: A versatile vision-language model for understanding, local-
ization, text reading, and beyond. arXiv preprint arXiv:2308.12966, 2023.
Simone Balloccu, Patr´ıcia Schmidtov´a, Mateusz Lango, and Ondˇrej Duˇsek.
Leak, cheat, re-
peat: Data contamination and evaluation malpractices in closed-source llms.
arXiv preprint
arXiv:2402.03927, 2024.
Shaon Bhattacharyya, Souvik Ghosh, Prantik Deb, Ajoy Mondal, and CV Jawahar. Adapting vision-
language models for hindi ocr. In International Conference on Document Analysis and Recogni-
tion, pp. 577–594. Springer, 2025.
Ali Furkan Biten, Ruben Tito, Andres Mafla, Lluis Gomez, Marc¸al Rusinol, Ernest Valveny,
CV Jawahar, and Dimosthenis Karatzas. Scene text visual question answering. In Proceedings of
the IEEE/CVF international conference on computer vision, pp. 4291–4301, 2019.
Iacer Calixto and Qun Liu. Incorporating global visual features into attention-based neural ma-
chine translation.
In Martha Palmer, Rebecca Hwa, and Sebastian Riedel (eds.), Proceed-
ings of the 2017 Conference on Empirical Methods in Natural Language Processing, pp. 992–
1003, Copenhagen, Denmark, September 2017. Association for Computational Linguistics. doi:
10.18653/v1/D17-1105. URL https://aclanthology.org/D17-1105.
Soravit Changpinyo, Linting Xue, Michal Yarom, Ashish Thapliyal, Idan Szpektor, Julien Amelot,
Xi Chen, and Radu Soricut. MaXM: Towards multilingual visual question answering. In Findings
of the Association for Computational Linguistics: EMNLP 2023, pp. 2667–2682, 2023.
Zhe Chen, Weiyun Wang, Hao Tian, Shenglong Ye, Zhangwei Gao, Erfei Cui, Wenwen Tong,
Kongzhi Hu, Jiapeng Luo, Zheng Ma, et al.
How far are we to gpt-4v? closing the gap to
commercial multimodal models with open-source suites. arXiv preprint arXiv:2404.16821, 2024.
Rocktim Jyoti Das, Simeon Emilov Hristov, Haonan Li, Dimitar Iliyanov Dimitrov, Ivan Koychev,
and Preslav Nakov. Exams-v: A multi-discipline multilingual multimodal exam benchmark for
evaluating vision language models. arXiv preprint arXiv:2403.10378, 2024.
Jean-Benoit Delbrouck and St´ephane Dupont. An empirical study on the effectiveness of images in
multimodal neural machine translation. In Martha Palmer, Rebecca Hwa, and Sebastian Riedel
(eds.), Proceedings of the 2017 Conference on Empirical Methods in Natural Language Process-
ing, pp. 910–919, Copenhagen, Denmark, September 2017. Association for Computational Lin-
guistics. doi: 10.18653/v1/D17-1095. URL https://aclanthology.org/D17-1095.
11

--- Page 12 ---\n\nDesmond Elliott and ´Akos K´ad´ar. Imagination improves multimodal translation. In Greg Kondrak
and Taro Watanabe (eds.), Proceedings of the Eighth International Joint Conference on Natural
Language Processing (Volume 1: Long Papers), pp. 130–141, Taipei, Taiwan, November 2017.
Asian Federation of Natural Language Processing. URL https://aclanthology.org/
I17-1014.
Desmond Elliott, Stella Frank, Khalil Sima’an, and Lucia Specia. Multi30k: Multilingual english-
german image descriptions. arXiv preprint arXiv:1605.00459, 2016.
Wikimedia Foundation.
Wikisource: The free library.
https://en.wikisource.org/
wiki/Main_Page, 2025. Accessed: 2025-07-09.
Chaoyou Fu, Peixian Chen, Yunhang Shen, Yulei Qin, Mengdan Zhang, Xu Lin, Jinrui Yang, Xiawu
Zheng, Ke Li, Xing Sun, et al. MME: A comprehensive evaluation benchmark for multimodal
large language models. arXiv preprint arXiv:2306.13394, 2023.
Chaoyou Fu, Peixian Chen, Yunhang Shen, Yulei Qin, Mengdan Zhang, Xu Lin, Jinrui Yang, Xiawu
Zheng, Ke Li, Xing Sun, Yunsheng Wu, and Rongrong Ji. MME: A comprehensive evaluation
benchmark for multimodal large language models, 2024a. URL https://arxiv.org/abs/
2306.13394.
Ling Fu, Zhebin Kuang, Jiajun Song, Mingxin Huang, Biao Yang, Yuzhe Li, Linghao Zhu, Qidi
Luo, Xinyu Wang, Hao Lu, et al. Ocrbench v2: An improved benchmark for evaluating large
multimodal models on visual text localization and reasoning. arXiv preprint arXiv:2501.00321,
2024b.
Gemini Team, Google. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality,
long context, and next generation agentic capabilities, 2025. URL https://arxiv.org/
abs/2507.06261.
Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, and Devi Parikh. Making the v in vqa
matter: Elevating the role of image understanding in visual question answering. In Proceedings
of the IEEE conference on computer vision and pattern recognition, pp. 6904–6913, 2017.
Stig-Arne Gr¨onroos, Benoit Huet, Mikko Kurimo, Jorma Laaksonen, Bernard Merialdo, Phu Pham,
Mats Sj¨oberg, Umut Sulubacak, J¨org Tiedemann, Raphael Troncy, et al. The memad submission
to the wmt18 multimodal translation task. arXiv preprint arXiv:1808.10802, 2018.
Adam W. Harley, Alex Ufkes, and Konstantinos G. Derpanis. Evaluation of deep convolutional
nets for document image classification and retrieval. In International Conference on Document
Analysis and Recognition (ICDAR), 2015.
Tatsuya Hiraoka and Kentaro Inui. Repetition neurons: How do language models produce repeti-
tions? arXiv preprint arXiv:2410.13497, 2024.
Anwen Hu, Haiyang Xu, Jiabo Ye, Ming Yan, Liang Zhang, Bo Zhang, Chen Li, Ji Zhang, Qin
Jin, Fei Huang, and Jingren Zhou. mplug-docowl 1.5: Unified structure learning for ocr-free
document understanding. arXiv preprint arXiv:2403.12895, 2024a.
Anwen Hu, Jiabo Ye, Qinghao Ye, Haiyang Xu, Ming Yan, Yuhao Dan, Qian Qi, Junfeng Tian,
Ji Zhang, and Fei Huang. mplug-docowl2: High-resolution compressing for ocr-free multi-page
document understanding. arXiv preprint arXiv:2409.03420, 2024b. ACL 2025.
Drew A Hudson and Christopher D Manning. GQA: A new dataset for real-world visual reasoning
and compositional question answering. In Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition, pp. 6700–6709, 2019.
Hideki Isozaki, Tsutomu Hirao, Kevin Duh, Katsuhito Sudoh, and Hajime Tsukada. Automatic
evaluation of translation quality for distant language pairs. In Proceedings of the 2010 Conference
on Empirical Methods in Natural Language Processing, pp. 944–952. ACL, 2010.
Guillaume Jaume et al. Funsd: A dataset for form understanding in noisy scanned documents. arXiv
preprint arXiv:1905.13538, 2019.
12

--- Page 13 ---\n\nShaharukh Khan, Ayush Tarun, Ali Faraz, Palash Kamble, Vivek Dahiya, Praveen Pokala, Ashish
Kulkarni, Chandra Khatri, Abhinav Ravi, and Shubham Agarwal. Chitranuvad: Adapting multi-
lingual llms for multimodal translation. arXiv preprint arXiv:2502.20420, 2025a.
Shaharukh Khan, Ayush Tarun, Abhinav Ravi, Ali Faraz, Akshat Patidar, Praveen Kumar Pokala,
Anagha Bhangare, Raja Kolla, Chandra Khatri, and Shubham Agarwal. Chitrarth: Bridging vision
and language for a billion people. https://github.com/ola-krutrim/Chitrarth,
2025b. URL https://arxiv.org/abs/2502.15392.
Geewook Kim, Teakgyu Hong, Moonbin Yim, JeongYeon Nam, Jinyoung Park, Jinyeong Yim,
Wonseok Hwang, Sangdoo Yun, Dongyoon Han, and Seunghyun Park. Ocr-free document un-
derstanding transformer. In European Conference on Computer Vision (ECCV), 2022.
Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin Johnson, Kenji Hata, Joshua Kravitz, Stephanie
Chen, Yannis Kalantidis, Li-Jia Li, David A Shamma, et al. Visual genome: Connecting lan-
guage and vision using crowdsourced dense image annotations. International journal of computer
vision, 123(1):32–73, 2017.
Chiraag Lala, Pranava Swaroop Madhyastha, Carolina Scarton, and Lucia Specia. Sheffield submis-
sions for wmt18 multimodal translation shared task. In Proceedings of the Third Conference on
Machine Translation: Shared Task Papers, pp. 624–631, 2018.
Hugo Laurenc¸on, L´eo Tronchon, Matthieu Cord, and Victor Sanh. What matters when building
vision-language models? arXiv preprint arXiv:2405.02246, 2024.
Hugo Laurenc¸on, L´eo Tronchon, Matthieu Cord, and Victor Sanh. What matters when building
vision-language models?, 2024. URL https://arxiv.org/abs/2405.02246.
VI Lcvenshtcin. Binary coors capable or ‘correcting deletions, insertions, and reversals. In Soviet
physics-doklady, 1966.
Minghao Li, Tengchao Lv, Jingye Chen, Lei Cui, Yijuan Lu, Dinei Florencio, Cha Zhang, Zhou-
jun Li, and Furu Wei. Trocr: Transformer-based optical character recognition with pre-trained
models. arXiv preprint arXiv:2109.10282, 2021.
Haofu Liao, Aruni RoyChowdhury, Weijian Li, Ankan Bansal, Yuting Zhang, Zhuowen Tu,
Ravi Kumar Satzoda, R. Manmatha, and Vijay Mahadevan. Doctr: Document transformer for
structured information extraction in documents. In Proceedings of the IEEE/CVF International
Conference on Computer Vision (ICCV), pp. 19584–19594, 2023.
Fangyu Liu, Emanuele Bugliarello, Edoardo Maria Ponti, Siva Reddy, Nigel Collier, and
Desmond Elliott. Visually grounded reasoning across languages and cultures. arXiv preprint
arXiv:2109.13238, 2021.
Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. Advances
in neural information processing systems, 36, 2023a.
Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction
tuning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recogni-
tion, pp. 26296–26306, 2024.
Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang Zhang, Wangbo Zhao, Yike Yuan,
Jiaqi Wang, Conghui He, Ziwei Liu, et al. Mmbench: Is your multi-modal model an all-around
player? arXiv preprint arXiv:2307.06281, 2023b.
Haoyu Lu, Wen Liu, Bo Zhang, Bingxuan Wang, Kai Dong, Bo Liu, Jingxiang Sun, Tongzheng Ren,
Zhuoshu Li, Yaofeng Sun, et al. Deepseek-vl: towards real-world vision-language understanding.
arXiv preprint arXiv:2403.05525, 2024.
Muhammad Maaz, Hanoona Rasheed, Abdelrahman Shaker, Salman Khan, Hisham Cholakal,
Rao M Anwer, Tim Baldwin, Michael Felsberg, and Fahad S Khan.
Palo: A polyglot large
multimodal model for 5b people. arXiv preprint arXiv:2402.14818, 2024.
13

--- Page 14 ---\n\nMinesh Mathew, Dimosthenis Karatzas, and CV Jawahar. Docvqa: A dataset for vqa on document
images. In Proceedings of the IEEE/CVF winter conference on applications of computer vision,
pp. 2200–2209, 2021.
AI Meta. The llama 4 herd: The beginning of a new era of natively multimodal ai innovation.
https://ai. meta. com/blog/llama-4-multimodal-intelligence/, checked on, 4(7):2025, 2025.
Karthik Reddy Kanjula Nahid Alam et al. Maya: An instruction finetuned multilingual multimodal
model. arXiv preprint arXiv:2412.07112, 2024. doi: 10.48550/arXiv.2412.07112. URL https:
//arxiv.org/abs/2412.07112.
Toshiaki Nakazawa, Chenchen Ding, Raj Dabre, Anoop Kunchukuttan, Nobushige Doi, Yusuke
Oda, Ondˇrej Bojar, Shantipriya Parida, Isao Goto, and Hidaya Mino. Proceedings of the 6th
workshop on asian translation. In Proceedings of the 6th Workshop on Asian Translation, 2019.
Toshiaki Nakazawa, Hideki Nakayama, Chenchen Ding, Raj Dabre, Anoop Kunchukuttan, Win Pa
Pa, Ondˇrej Bojar, Shantipriya Parida, Isao Goto, Hidaya Mino, Hiroshi Manabe, Katsuhito Sudoh,
Sadao Kurohashi, and Pushpak Bhattacharyya (eds.). Proceedings of the 7th Workshop on Asian
Translation, Suzhou, China, December 2020. Association for Computational Linguistics. URL
https://aclanthology.org/2020.wat-1.0.
Toshiaki Nakazawa, Hideki Nakayama, Isao Goto, Hideya Mino, Chenchen Ding, Raj Dabre, Anoop
Kunchukuttan, Shohei Higashiyama, Hiroshi Manabe, Win Pa Pa, Shantipriya Parida, Ondˇrej
Bojar, Chenhui Chu, Akiko Eriguchi, Kaori Abe, Yusuke Oda, Katsuhito Sudoh, Sadao Kuro-
hashi, and Pushpak Bhattacharyya (eds.).
Proceedings of the 8th Workshop on Asian Trans-
lation (WAT2021), Online, August 2021. Association for Computational Linguistics.
URL
https://aclanthology.org/2021.wat-1.0.
Toshiaki Nakazawa, Kazutaka Kinugawa, Hideya Mino, Isao Goto, Raj Dabre, Shohei Higashiyama,
Shantipriya Parida, Makoto Morishita, Ondrej Bojar, Akiko Eriguchi, Yusuke Oda, Akiko
Eriguchi, Chenhui Chu, et al. (eds.). Proceedings of the 9th Workshop on Asian Translation,
Gyeongju, Republic of Korea, October 2022. International Conference on Computational Lin-
guistics. URL https://aclanthology.org/2022.wat-1.0.
Toshiaki Nakazawa, Kazutaka Kinugawa, Hideya Mino, Isao Goto, Raj Dabre, Shohei Higashiyama,
Shantipriya Parida, Makoto Morishita, Ondrej Bojar, Akiko Eriguchi, Yusuke Oda, Akiko
Eriguchi, Chenhui Chu, and Sadao Kurohashi (eds.). Proceedings of the 10th Workshop on Asian
Translation, Macau SAR, China, September 2023. Asia-Pacific Association for Machine Trans-
lation. URL https://aclanthology.org/2023.wat-1.0.
Shravan Nayak, Kanishk Jain, Rabiul Awal, Siva Reddy, Sjoerd van Steenkiste, Lisa Anne Hen-
dricks, Karolina Sta´nczak, and Aishwarya Agrawal. Benchmarking vision language models for
cultural understanding, 2024. URL https://arxiv.org/abs/2407.10920.
Clemens Neudecker, Konstantin Baierer, Mike Gerber, Christian Clausner, Apostolos Antonacopou-
los, and Stefan Pletschacher. A survey of ocr evaluation tools and metrics. In Proceedings of the
6th International Workshop on Historical Document Imaging and Processing, pp. 13–18, 2021.
OpenAI.
Gpt-4v, 2023.
Retrieved from https://cdn.openai.com/papers/GPTV_
System_Card.pdf.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic
evaluation of machine translation. In Proceedings of the 40th Annual Meeting of the Association
for Computational Linguistics, pp. 311–318. ACL, 2002.
Shantipriya Parida, Ondˇrej Bojar, Idris Abdulmumin, Shamsuddeen Hassan Muhammad, and
Ibrahim Sa’id Ahmad. Findings of wmt2024 english-to-low resource multimodal translation task.
In Proceedings of the Ninth Conference on Machine Translation, pp. 677–683, 2024.
Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor
Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. Pytorch: An imperative style, high-
performance deep learning library. Advances in neural information processing systems, 32, 2019.
14

--- Page 15 ---\n\nTanvina Patel, Wiebke Hutiri, Aaron Yi Ding, and Odette Scharenborg. How to evaluate auto-
matic speech recognition: Comparing different performance and bias measures. arXiv preprint
arXiv:2507.05885, 2025.
Jonas Pfeiffer, Gregor Geigle, Aishwarya Kamath, Jan-Martin O Steitz, Stefan Roth, Ivan
Vuli´c, and Iryna Gurevych.
xgqa: Cross-lingual visual question answering.
arXiv preprint
arXiv:2109.06082, 2021.
Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal,
Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual
models from natural language supervision. In International conference on machine learning, pp.
8748–8763. PmLR, 2021.
David Romero, Chenyang Lyu, Haryo Akbarianto Wibowo, Teresa Lynn, Injy Hamed, Aditya Nanda
Kishore, Aishik Mandal, Alina Dragonetti, Artem Abzaliev, Atnafu Lambebo Tonja, et al.
CVQA: Culturally-diverse multilingual visual question answering benchmark. arXiv preprint
arXiv:2406.05967, 2024.
Amanpreet Singh, Ronghang Hu, Vedanuj Goswami, Guillaume Couairon, Wojciech Galuba, Mar-
cus Rohrbach, and Douwe Kiela. Flava: A foundational language and vision alignment model.
In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp.
15638–15650, 2022.
Ray Smith. An overview of the tesseract ocr engine. In Proceedings of the Ninth International Con-
ference on Document Analysis and Recognition (ICDAR), pp. 629–633. IEEE, 2007. doi: 10.1109/
ICDAR.2007.4376991. URL https://ieeexplore.ieee.org/document/4376991.
Lucia Specia, Stella Frank, Khalil Sima’an, and Desmond Elliott. A shared task on multimodal
machine translation and crosslingual image description. In Proceedings of the First Conference
on Machine Translation: Volume 2, Shared Task Papers, pp. 543–553, 2016. URL https:
//www.aclweb.org/anthology/W16-2346/.
Hai-Long Sun, Da-Wei Zhou, Yang Li, Shiyin Lu, Chao Yi, Qing-Guo Chen, Zhao Xu, Weihua Luo,
Kaifu Zhang, De-Chuan Zhan, et al. Parrot: Multilingual visual instruction tuning. arXiv preprint
arXiv:2406.02539, 2024.
Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya
Pathak, Laurent Sifre, Morgane Rivi`ere, Mihir Sanjay Kale, Juliette Love, et al. Gemma: Open
models based on gemini research and technology. arXiv preprint arXiv:2403.08295, 2024.
Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya Pathak, Nino Vieillard, Ramona Merhej,
Sarah Perrin, Tatiana Matejovicova, Alexandre Ram´e, Morgane Rivi`ere, et al. Gemma 3 technical
report. arXiv preprint arXiv:2503.19786, 2025.
Shengbang Tong, Ellis Brown, Penghao Wu, Sanghyun Woo, Manoj Middepogu, Sai Charitha
Akula, Jihan Yang, Shusheng Yang, Adithya Iyer, Xichen Pan, et al. Cambrian-1: A fully open,
vision-centric exploration of multimodal llms. arXiv preprint arXiv:2406.16860, 2024.
Michael Tschannen, Alexey Gritsenko, Xiao Wang, Muhammad Ferjad Naeem, Ibrahim Alabdul-
mohsin, Nikhil Parthasarathy, Talfan Evans, Lucas Beyer, Ye Xia, Basil Mustafa, et al. Siglip 2:
Multilingual vision-language encoders with improved semantic understanding, localization, and
dense features. arXiv preprint arXiv:2502.14786, 2025.
Ashmal Vayani, Dinura Dissanayake, Hasindri Watawana, and et al. All languages matter: Eval-
uating lmms on culturally diverse 100 languages, 2025. URL https://arxiv.org/abs/
2411.16508.
Dongsheng Wang, Natraj Raman, Mathieu Sibue, Zhiqiang Ma, Petr Babkin, Simerjot Kaur, Yulong
Pei, Armineh Nourbakhsh, and Xiaomo Liu. Docllm: A layout-aware generative language model
for multimodal document understanding. arXiv preprint arXiv: 2401.00908, 2023.
Hongyu Wang, Jiayu Xu, Senwei Xie, Ruiping Wang, Jialin Li, Zhaojie Xie, Bin Zhang, Chuyan
Xiong, and Xilin Chen. M4u: Evaluating multilingual understanding and reasoning for large
multimodal models. arXiv preprint arXiv:2405.15638, 2024a.
15

--- Page 16 ---\n\nWeihan Wang, Qingsong Lv, Wenmeng Yu, Wenyi Hong, Ji Qi, Yan Wang, Junhui Ji, Zhuoyi Yang,
Lei Zhao, Xixuan Song, Jiazheng Xu, Bin Xu, Juanzi Li, Yuxiao Dong, Ming Ding, and Jie Tang.
Cogvlm: Visual expert for pretrained language models, 2024b. URL https://arxiv.org/
abs/2311.03079.
Genta Indra Winata, Frederikus Hudi, Patrick Amadeus Irawan, and et al. Worldcuisines: A massive-
scale benchmark for multilingual and multicultural visual question answering on global cuisines,
2025. URL https://arxiv.org/abs/2410.12705.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi,
Pierric Cistac, Tim Rault, R´emi Louf, Morgan Funtowicz, et al. Huggingface’s transformers:
State-of-the-art natural language processing. arXiv preprint arXiv:1910.03771, 2019.
Zhiyong Wu, Lingpeng Kong, Wei Bi, Xiang Li, and Ben Kao. Good for misconceived reasons:
An empirical revisiting on the need for visual context in multimodal machine translation. In
Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli (eds.), ACL, pp. 6153–6166, Online,
August 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.acl-long.480.
URL https://aclanthology.org/2021.acl-long.480.
Le Xue, Manli Shu, Anas Awadalla, Jun Wang, An Yan, Senthil Purushwalkam, Honglu Zhou, Viraj
Prabhu, Yutong Dai, Michael S Ryoo, et al. xgen-mm (blip-3): A family of open large multimodal
models. arXiv preprint arXiv:2408.08872, 2024.
Shaowei Yao and Xiaojun Wan. Multimodal transformer for multimodal machine translation. In
Proceedings of the 58th annual meeting of the association for computational linguistics, pp.
4346–4350, 2020.
Da Yin, Liunian Harold Li, Ziniu Hu, Nanyun Peng, and Kai-Wei Chang. Broaden the vision:
Geo-diverse visual commonsense reasoning. arXiv preprint arXiv:2109.06860, 2021.
Weihao Yu, Zhengyuan Yang, Linjie Li, Jianfeng Wang, Kevin Lin, Zicheng Liu, Xinchao Wang,
and Lijuan Wang. MM-VET: Evaluating large multimodal models for integrated capabilities.
arXiv preprint arXiv:2308.02490, 2023.
Xiang Yue, Yueqi Song, Akari Asai, Seungone Kim, Jean de Dieu Nyandwi, Simran Khanuja, Anjali
Kantharuban, Lintang Sutawika, Sathyanarayanan Ramamoorthy, and Graham Neubig. Pangea:
A fully open multilingual multimodal LLM for 39 languages. In The Thirteenth International
Conference on Learning Representations (ICLR), 2025. URL https://arxiv.org/abs/
2410.16153.
Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, and Lucas Beyer. Sigmoid loss for language
image pre-training. In Proceedings of the IEEE/CVF international conference on computer vision,
pp. 11975–11986, 2023.
Wenxuan Zhang, Mahani Aljunied, Chang Gao, Yew Ken Chia, and Lidong Bing. M3exam: A
multilingual, multimodal, multilevel benchmark for examining large language models. Advances
in Neural Information Processing Systems, 36:5484–5505, 2023.
16

--- Page 17 ---\n\nAPPENDIX
A
LIMITATIONS
IndicVisionBench covers English and ten medium- to low-resource Indic languages across 13 cul-
turally grounded topics, but some limitations remain. Language coverage is still limited for some of
the lowest-resource languages, and topic diversity could be further expanded to cover additional cul-
tural contexts. Human annotations and translations are usually subject to interpretation, especially
for cultural nuances, which may introduce inconsistencies or simplifications. Existing evaluation
metrics and LLM-based scoring may not fully capture cultural grounding or multimodal reasoning,
highlighting opportunities for more nuanced evaluation approaches. Although we systematically
study the impact of visual modality for VQA, we have not yet explored this effect for the MMT
track with prior works (Gr¨onroos et al., 2018; Lala et al., 2018; Wu et al., 2021) showcasing mini-
mal impact of visual modality. We plan to cover this as part of the future work.
B
IMPLEMENTATION
Most of our implementation is based in Python and we use HuggingFace library in PyTorch (Paszke
et al., 2019; Wolf et al., 2019). We evaluate a broad range of frontier and open-source models on
the IndicVisionBench benchmark using their respective APIs as well as HuggingFace pages. For
the OCR-focused subset of our evaluation, we used the implementation of OCRBenchV25 to com-
pute the ANLS metrics. We adapted this script to report both word-level and character-level ANLS
metrics. Beyond OCR, our full benchmark includes additional evaluation dimensions, we also com-
pute metrics such as BLEU6 where we don’t have additional pre-processing step of tokenization,
RIBES7, Exact Match (EM), and employ LLM-as-a-Judge evaluation to capture semantic and task-
level correctness. We use official Batch APIs to get the results from GPT-4o8 for LLM-as-a-judge9
results and Gemini-2.5 for annotations.
OCR benchmark. We began with raw dumps from Wikisource10 for ten Indic languages, obtained
from the official Wikimedia snapshots 11. Each compressed XML dump was parsed to extract page
titles, which were then converted into canonical Wikisource URLs. From the harvested URLs, we
fetched the corresponding Wikisource pages, retained only pages with images and applied filtering
to retain only those marked as proofread by the community (quality level 4), ensuring high-fidelity
ground truth. For every verified page, we used the <prp-page-image> tag to collect the page scans
and the <pagetext> tag to extract the corresponding OCR text, which reflects the latest human-
edited annotation. This pipeline, implemented with custom parsing code and filtering, yielded a
linguistically diverse dataset of high-quality scanned documents paired with verified text, which
forms the foundation of the OCR evaluation track in IndicVisionBench.
Table 6: Cost comparison for Gemini and OpenAI models in OCR and Captioning tasks
(rounded to 2 decimals in $). We provide an approximate cost at the time of submission for a
sample of 1000 images based on the assumptions of input and outputs tokens. Batch APIs are half
the price of Single calls. Here Gemini-2.5-F denotes Gemini-2.5-Flash and Gemini-2.5-P denotes
Gemini-2.5-Pro. Our benchmark further involved a multiple for number of languages and questions.
Task
#Images
Input (M)
Output (M)
Batch (Gemini)
Single (Gemini)
Batch (OpenAI)
Single (OpenAI)
Gemini-2.5-F
Gemini-2.5-P
Gemini-2.5-F
Gemini-2.5-P
GPT-4o
GPT-4o-mini
GPT-4o
GPT-4o-mini
OCR
1,000
0.05
0.30
0.58
2.34
1.15
4.68
2.52
2.01
5.04
4.01
Captioning
1,000
0.05
0.15
0.39
1.59
0.78
3.18
1.77
1.96
3.54
3.92
5https://github.com/Yuliang-Liu/MultimodalOCR/blob/main/OCRBench_v2/
eval_scripts/vqa_metric.py
6https://huggingface.co/spaces/evaluate-metric/sacrebleu/blob/main/
sacrebleu.py
7https://github.com/nttcslab-nlp/RIBES
8https://platform.openai.com/docs/guides/batch
9GPT-4o-2024-08-06 is the model used as LLM-as-a-Judge.
10https://hi.wikisource.org
11https://dumps.wikimedia.org/hiwikisource/latest/
17

--- Page 18 ---\n\nC
ADDITIONAL RESULTS
Figure 7: Model performances on IndicVisionBench-VQA-Parallel. Average scores on the three
open-ended questions (Long and two Short) for six models across different languages (X-axis) and
images corresponding to Indian states grouped by primary language (Y-axis). Left to right, top
row: Gemma-3-27B (left) and LLaMA-4 (right); middle row: Chitrarth-1 (left) and Pangea (right);
bottom row: Maya (left) and PALO (right).
18

--- Page 19 ---\n\nTable 7: Model performances on IndicVisionBench-VQA-Parallel.
Comprehensive scores
across languages, question types, and models for IndicVisionBench-VQA-Parallel.
Q-Type
Model
Bengali
English
Gujarati
Hindi
Kannada
Malayalam
Marathi
Odia
Punjabi
Tamil
Telugu
MCQ
(Exact Match, out of 1, ↑)
Maya
0.462
0.632
-
0.575
-
-
-
-
-
-
-
PALO
0.604
0.802
-
0.660
-
-
-
-
-
-
-
Pangea
0.783
0.840
-
0.849
-
-
-
-
-
0.670
0.764
Chitrarth-1
0.726
0.811
0.755
0.792
0.651
0.726
0.774
0.679
0.726
0.689
0.708
LLaMA-4
0.802
0.858
0.802
0.792
0.840
0.830
0.811
0.774
0.802
0.802
0.783
Gemma-3
0.849
0.877
0.877
0.877
0.868
0.858
0.849
0.830
0.849
0.858
0.840
GPT-4o
0.830
0.896
0.849
0.877
0.830
0.745
0.830
0.708
0.774
0.755
0.821
Gemini
0.925
0.943
0.953
0.953
0.943
0.953
0.943
0.972
0.962
0.925
0.953
True/False
(Exact Match, out of 1, ↑)
Maya
0.600
0.470
-
0.360
-
-
-
-
-
-
-
PALO
0.310
0.570
-
0.620
-
-
-
-
-
-
-
Pangea
0.770
0.470
-
0.850
-
-
-
-
-
0.640
0.790
Chitrarth-1
0.560
0.730
0.630
0.450
0.470
0.420
0.500
0.632
0.604
0.349
0.349
LLaMA-4
0.896
0.877
0.830
0.896
0.896
0.858
0.925
0.868
0.792
0.821
0.792
Gemma-3
0.547
0.868
0.858
0.906
0.783
0.925
0.896
0.425
0.585
0.896
0.557
GPT-4o
0.802
0.915
0.849
0.868
0.821
0.802
0.877
0.632
0.877
0.811
0.792
Gemini
0.972
0.981
0.943
0.943
0.943
0.943
0.953
0.925
0.915
0.953
0.925
Long answer
(LLM-as-Judge, out of 10, ↑)
Maya
3.538
6.915
-
6.217
-
-
-
-
-
-
-
PALO
2.557
7.057
-
5.217
-
-
-
-
-
-
-
Pangea
6.585
7.038
-
7.009
-
-
-
-
-
5.066
5.887
Chitrarth-1
7.443
7.491
7.547
7.311
7.292
7.406
7.472
7.311
6.972
7.142
7.443
LLaMA-4
8.396
8.566
8.217
8.500
8.387
7.934
8.349
7.774
8.292
8.236
8.292
Gemma-3
8.377
8.698
8.358
8.443
8.377
8.104
8.368
7.802
8.330
8.443
8.236
GPT-4o
8.075
8.660
7.868
8.330
7.613
7.557
8.170
6.868
7.642
7.528
7.764
Gemini
9.094
9.453
9.113
9.132
9.113
8.877
9.075
8.764
9.142
8.981
8.981
Short-answer 1
(LLM-as-Judge, out of 10, ↑)
Maya
3.142
4.745
-
3.755
-
-
-
-
-
-
-
PALO
3.066
5.000
-
3.708
-
-
-
-
-
-
-
Pangea
4.557
6.170
-
5.443
-
-
-
-
-
3.066
4.094
Chitrarth-1
5.896
5.953
5.755
5.972
5.575
4.679
5.613
5.114
5.434
4.925
5.500
LLaMA-4
7.198
7.387
7.189
7.415
6.698
6.736
6.868
6.283
6.991
6.302
6.679
Gemma-3
6.670
6.981
7.075
6.868
6.292
6.406
6.575
5.943
6.802
6.915
6.934
GPT-4o
6.726
7.594
6.028
7.075
5.896
5.962
6.519
4.849
6.019
5.538
6.123
Gemini
8.094
8.217
7.896
8.330
7.566
7.887
7.991
7.717
8.151
7.962
7.755
Short-answer 2
(LLM-as-Judge, out of 10, ↑)
Maya
3.462
5.094
-
4.472
-
-
-
-
-
-
-
PALO
2.774
5.472
-
4.028
-
-
-
-
-
-
-
Pangea
5.340
7.255
-
5.783
-
-
-
-
-
3.236
4.396
Chitrarth-1
6.519
6.085
5.792
5.604
5.849
5.330
5.698
5.651
4.953
5.670
6.066
LLaMA-4
7.642
8.236
7.019
7.755
7.179
7.151
7.132
6.651
7.321
6.858
7.085
Gemma-3
7.170
7.547
7.160
7.179
7.217
6.981
7.123
6.443
6.858
6.783
6.962
GPT-4o
6.755
7.934
5.840
6.858
5.915
5.708
6.368
5.075
5.858
5.538
6.075
Gemini
8.434
8.755
8.142
8.368
8.406
8.094
8.236
8.085
8.302
8.151
8.179
Adversarial question
(LLM-as-Judge, out of 10, ↑)
Maya
0.255
0.368
-
0.377
-
-
-
-
-
-
-
PALO
0.123
0.453
-
0.104
-
-
-
-
-
-
-
Pangea
0.066
0.858
-
0.000
-
-
-
-
-
0.000
0.000
Chitrarth-1
0.000
0.094
0.094
0.075
0.000
0.000
0.094
0.000
0.000
0.047
0.047
LLaMA-4
1.123
3.387
0.849
1.500
0.953
1.547
0.821
0.406
0.991
0.849
0.660
Gemma-3
1.566
2.179
1.915
2.349
2.283
2.226
1.915
2.132
2.472
2.085
2.906
GPT-4o
0.642
1.104
0.708
0.745
0.726
0.425
0.642
0.642
0.566
0.623
0.726
Gemini
4.745
6.142
4.962
5.528
4.491
4.991
4.575
4.094
4.660
4.670
5.019
൪൨൪\nധ്രുുവചരിതം\nനൂണില്ലുറക്കമില്ലെന്നല്ലമെല്ലവേ\nനാണിച്ചുുകേണങ്ങൊളിച്ചുുവാണീടുന്നു\nഏണാക്ഷിമാരുടെവക്ത്രങ്ങൾകാൺകയാൽ
\nഏണാങ്കനൊട്ടൊട്ടൊളിച്ചുുനടക്കുന്നു\nകാണാതെജന്മംംകഴിക്കേണമെന്നോർത്തു\nതാണുമേഘങ്ങളിൽനൂണുനടക്കുന്നു\n
മാളികാസൌ
ധംമുകളേറിമേവുന്നു\nകാണിനേരമൊരിടത്തുകാണുന്നീലാ;\nഉത്താനപാദന്റെപത്തനംതന്നില\nങ്ങുത്തമസ്ത്രീീകടെനൃത്തപ്ര
യോഗവും\nമദ്ദളക്കാരുടെഒത്തുംകലാശവും\nകൂത്തിനിണങ്ങുന്നതിത്തിപ്രയോഗവും\nവൃത്തിക്കുചേരുംപ്രവൃത്തിപ്രസംഗവും\nമംഗല
മാകുംമൃദംഗശബ്ദങ്ങളും\nതുംഗങ്ങളായുളളരംഗങ്ങളിൽപുന-\nരംഗനമാരുടെസംഗീതഭംഗിയും\nശൃംഗവരങ്ങളിൽശൃംഗാരലീലയും\nതുംഗ
ഹർമ്മ്യങ്ങളിലംഗജക്രീീഡയും\nകാളംകടുന്തുടിചേങ്കിലയുംനല്ല\nമേളംതകിലുംമുരശുംകലാവിദ്യാാ\nപാഠകന്മാാരുടെപാഠകംനാടകം\nചേടക
ന്മാാരുടെചാടുകടുംപൂജ\nവിദ്വജ്ജനത്തിന്റെഗദ്യങ്ങൾപദ്യങ്ങൾ\nസദ്യോവരുന്നോരുസദ്യോഗസമ്പത്തു\nസദ്യോഗൃഹങ്ങളിലുദ്യാാനലീലക-\n
ളുദ്യോഗമോടുടൻപദ്യാാദിലേഖനം\nമദ്യാാലയങ്ങളിൽമദ്യപാനോത്സവം\nസദ്യഗൃഹങ്ങളിൽവാദ്യപ്രയോഗവും\nഗ്രന്ഥികളോരോരോദിക്കിന്നുവ
ന്നുടൻ\nസന്തതംമന്നവൻമുന്നിലിരുന്നോരോ\nഗ്രന്ഥങ്ങൾനോക്കിവായിച്ചുുപൊരുൾപറ-\nഞ്ഞന്തരംകൂടാതെകാലംകഴിക്കയും\nമാലതീമാധ
വംശാകുന്തളംപിന്നെ\nബാലരാമായണംകർപ്പൂൂരമഞ്ജർ\nമാളവികാഗ്നിിയുംമിത്രാാബുരാശിയും\nമേളംകലർന്നൊരുമുദ്ദിരാരാക്ഷസം...
ഉപഹാരിതം\n\n\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
. . . . . . . .
Ground Truth
Prediction
Figure 8: Observed repetition in OCR outputs. We show an example where LLaMA-4 provided
repetitions upto maximum sequence length in the prediction for an OCR example in Malayalam.
19

--- Page 20 ---\n\nTable 8: Model performances on IndicVisionBench-VQA-Indic. Comprehensive scores across
languages, question types, and models.
Q-Type
Model
Bengali
Gujarati
Hindi
Kannada
Malayalam
Marathi
Odia
Punjabi
Tamil
Telugu
MCQ
(Exact Match, out of 1, ↑)
Maya
0.433
-
0.638
-
-
-
-
-
-
-
PALO
0.467
-
0.576
-
-
-
-
-
-
-
Pangea
0.733
-
0.812
-
-
-
-
-
0.670
0.768
Chitrarth-1
0.717
0.774
0.812
0.633
0.733
0.811
0.605
0.645
0.691
0.681
LLaMA-4
0.700
0.871
0.866
0.878
0.817
0.838
0.816
0.839
0.809
0.899
Gemma-3
0.817
0.839
0.844
0.878
0.783
0.919
0.868
0.710
0.798
0.870
GPT-4o
0.750
0.613
0.839
0.719
0.733
0.838
0.684
0.806
0.713
0.812
Gemini-2.5
0.883
0.871
0.924
0.906
0.833
1.000
0.895
0.935
0.883
0.928
True/False
(Exact Match out of 1, ↑)
Maya
0.483
-
0.333
-
-
-
-
-
-
-
PALO
0.317
-
0.714
-
-
-
-
-
-
-
Pangea
0.717
-
0.746
-
-
-
-
-
0.585
0.725
Chitrarth-1
0.600
0.452
0.415
0.374
0.500
0.514
0.553
0.548
0.277
0.377
LLaMA-4
0.850
0.742
0.891
0.899
0.783
0.892
0.816
0.839
0.862
0.870
Gemma-3
0.867
0.581
0.830
0.827
0.800
0.757
0.711
0.935
0.766
0.812
GPT-4o
0.883
0.742
0.842
0.676
0.850
0.892
0.711
0.968
0.819
0.739
Gemini-2.5
0.917
0.871
0.924
0.878
0.867
0.973
0.868
1.000
0.915
0.928
Long answer
(LLM-as-Judge, out of 10, ↑)
Maya
3.867
-
6.504
-
-
-
-
-
-
-
PALO
3.150
-
5.712
-
-
-
-
-
-
-
Pangea
6.783
-
7.493
-
-
-
-
-
4.787
5.884
Chitrarth-1
7.233
7.484
7.547
7.669
7.433
7.351
7.553
7.290
7.298
7.290
LLaMA-4
8.050
8.290
8.482
8.489
8.267
8.486
7.763
8.452
8.245
8.000
Gemma-3
8.400
8.613
8.498
8.576
8.317
8.541
7.737
8.613
8.489
8.217
GPT-4o
8.283
8.484
8.484
7.000
8.033
8.243
7.868
8.484
7.755
7.913
Gemini-2.5
8.883
9.226
9.087
9.029
8.817
9.243
8.737
8.968
8.904
8.870
Short answer 1
(LLM-as-Judge, out of 10, ↑)
Maya
2.117
-
4.199
-
-
-
-
-
-
-
PALO
2.733
-
3.984
-
-
-
-
-
-
-
Pangea
4.617
-
5.772
-
-
-
-
-
4.160
4.768
Chitrarth-1
5.550
6.129
6.328
5.964
4.483
5.595
6.658
5.129
6.489
5.551
LLaMA-4
7.050
7.677
7.710
7.662
6.933
7.351
6.289
7.516
7.394
7.043
Gemma-3
6.783
8.032
7.578
7.158
6.417
6.676
6.526
7.516
7.266
7.101
GPT-4o
7.550
7.355
8.060
7.309
6.800
6.865
6.158
7.065
7.223
7.580
Gemini-2.5
8.117
8.355
8.540
8.734
7.600
8.486
8.263
8.355
8.245
8.116
Short answer 2
(LLM-as-Judge, out of 10, ↑)
Maya
3.717
-
4.696
-
-
-
-
-
-
-
PALO
2.700
-
4.205
-
-
-
-
-
-
-
Pangea
4.983
-
6.188
-
-
-
-
-
4.213
4.652
Chitrarth-1
5.883
6.613
6.212
6.029
5.567
6.378
6.132
6.032
6.468
6.087
LLaMA-4
6.917
7.581
7.665
7.633
6.917
7.838
6.947
7.742
6.926
7.217
Gemma-3
7.117
7.742
7.344
7.173
6.450
6.811
5.842
7.484
6.883
6.652
GPT-4o
7.300
7.581
7.652
7.338
7.450
7.649
6.579
7.290
7.160
7.261
Gemini-2.5
7.950
8.484
8.268
8.691
8.083
8.730
8.289
8.452
8.117
8.188
Adversarial
(LLM-as-Judge, out of 10, ↑)
Maya
0
-
0.188
-
-
-
-
-
-
-
PALO
0.017
-
0.114
-
-
-
-
-
-
-
Pangea
0
-
0.011
-
-
-
-
-
0
0
Chitrarth-1
0
0
0.011
0.072
0
0.135
0.053
0.161
0.053
0
LLaMA-4
0.383
0.516
1.179
0.144
0.333
0.811
0.526
1.032
1.138
0.072
Gemma-3
1.067
0.968
1.656
1.022
0.767
0.676
0.895
2.935
1.851
1.130
GPT-4o
2.233
3.097
2.248
0.669
2.283
2.892
1.816
4.000
1.702
2.043
Gemini-2.5
5.167
2.935
4.460
3.165
3.317
4.838
3.921
5.710
5.149
2.725
Table 9: VQA with and without image.
Average scores on long-answer type questions of
Chitrarth-1, Gemma-3, and Gemini-2.5 on IVB-VQA-Parallel across 11 languages, evaluated with
and without image input.
Model
Type
Bengali
↑
English
↑
Gujarati
↑
Hindi
↑
Kannada
↑
Malayalam
↑
Marathi
↑
Odia
↑
Punjabi
↑
Tamil
↑
Telugu
↑
Chitrarth-1
w/o img
6.52
6.37
6.72
6.62
6.69
6.67
6.52
6.39
6.09
6.78
6.65
with img
7.44
7.49
7.55
7.31
7.29
7.41
7.47
7.31
6.97
7.14
7.44
Gemma-3
w/o img
7.40
6.43
7.49
7.33
7.53
7.43
7.40
6.53
7.07
7.70
7.29
with img
8.38
8.70
8.36
8.44
8.38
8.10
8.37
7.80
8.33
8.44
8.24
Gemini-2.5
w/o img
8.11
6.58
8.13
8.21
8.15
8.15
8.27
8.06
8.13
8.11
8.21
with img
9.09
9.45
9.11
9.13
9.11
8.88
9.08
8.76
9.14
8.98
8.98
Table 10: Model performances on IndicVisionBench-OCR. Median WER and CER scores across
Indic languages for various models.
Model
Bengali
Gujarati
Hindi
Kannada
Malayalam
Marathi
Odia
Punjabi
Tamil
Telugu
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
Maya
1.00
1.00
-
-
1.00
0.98
-
-
-
-
-
-
-
-
-
-
-
-
-
-
PALO
1.00
0.99
-
-
1.00
0.99
-
-
-
-
-
-
-
-
-
-
-
-
-
-
Pangea
1.00
0.85
-
-
1.00
0.95
-
-
-
-
-
-
-
-
-
-
1.00
0.87
1.00
0.93
Chitrarth-1
1.00
0.96
1.00
0.96
0.99
0.97
1.11
0.95
1.00
0.99
1.00
0.95
1.19
1.00
1.00
0.97
1.00
0.97
1.00
0.96
LLaMA-4
0.38
0.13
0.53
0.16
0.27
0.09
0.65
0.12
0.87
0.45
0.25
0.07
1.00
0.89
0.34
0.11
0.39
0.08
0.69
0.19
Gemma-3
0.49
0.21
0.71
0.40
0.50
0.28
0.91
0.55
0.98
0.76
0.60
0.34
0.97
0.77
0.78
0.43
0.57
0.15
0.93
0.57
GPT-4o
0.65
0.29
1.00
0.77
0.60
0.34
1.09
0.74
1.00
0.80
0.75
0.39
0.97
0.79
0.78
0.39
0.92
0.44
1.17
0.76
Gemini-2.5
0.25
0.03
0.33
0.07
0.23
0.04
0.24
0.04
0.63
0.30
0.23
0.02
0.55
0.20
0.24
0.04
0.39
0.03
0.45
0.05
20

--- Page 21 ---\n\nTable 11: Model performances on IndicVisionBench-OCR. Average WER and CER (± standard
deviation) for Bengali, Gujarati, Hindi, Kannada, and Malayalam.
Model
Bengali
Gujarati
Hindi
Kannada
Malayalam
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
Maya
1.15 ± 0.56
0.99 ± 0.07
-
-
2.32 ± 8.94
1.90 ± 5.78
-
-
-
-
PALO
2.77 ± 3.45
2.06 ± 2.02
-
-
1.58 ± 2.43
1.06 ± 0.50
-
-
-
-
Pangea
1.25 ± 0.90
0.99 ± 0.59
-
-
1.22 ± 1.31
1.07 ± 1.07
-
-
-
-
Chitrarth-1
1.34 ± 0.89
1.07 ± 0.64
1.38 ± 1.05
1.02 ± 0.48
1.09 ± 0.41
0.96 ± 0.22
1.37 ± 0.49
0.95 ± 0.13
2.45 ± 7.82
1.16 ± 0.61
Chitrapathak
0.33 ± 0.13
0.08 ± 0.14
0.55 ± 0.19
0.29 ± 0.25
0.37 ± 0.37
0.15 ± 0.27
0.34 ± 0.14
0.09 ± 0.08
0.76 ± 0.18
0.48 ± 0.32
Gemma-3
0.53 ± 0.19
0.26 ± 0.15
0.71 ± 0.13
0.41 ± 0.13
0.59 ± 0.44
0.35 ± 0.41
0.94 ± 0.16
0.58 ± 0.15
1.72 ± 5.42
0.76 ± 0.15
LLaMA-4
0.40 ± 0.17
0.14 ± 0.11
0.53 ± 0.28
0.20 ± 0.18
0.37 ± 0.36
0.14 ± 0.18
0.66 ± 0.29
0.13 ± 0.12
25.26 ± 217.47
0.48 ± 0.26
GPT-4o
0.71 ± 0.43
0.41 ± 0.50
1.36 ± 0.97
1.40 ± 2.51
0.77 ± 0.78
0.42 ± 0.28
1.43 ± 1.21
0.95 ± 0.72
7.62 ± 39.12
1.12 ± 0.92
Gemini-2.5
0.26 ± 0.08
0.05 ± 0.09
0.33 ± 0.13
0.08 ± 0.11
0.29 ± 0.31
0.07 ± 0.12
0.27 ± 0.19
0.05 ± 0.05
2.26 ± 9.16
0.31 ± 0.26
Table 12: Model performances on IndicVisionBench-OCR. Average WER and CER (± standard
deviation) for Marathi, Odia, Punjabi, Tamil, and Telugu.
Model
Marathi
Odia
Punjabi
Tamil
Telugu
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
WER ↓
CER ↓
Maya
-
-
-
-
-
-
-
-
-
-
PALO
-
-
-
-
-
-
-
-
-
-
Pangea
-
-
-
-
-
-
1.37 ± 1.02
0.97 ± 0.43
1.29 ± 0.67
0.98 ± 0.35
Chitrarth-1
1.15 ± 0.50
0.93 ± 0.21
1.89 ± 1.36
1.52 ± 0.93
1.59 ± 1.20
1.41 ± 1.17
1.53 ± 1.58
1.09 ± 0.56
1.56 ± 1.27
1.05 ± 0.50
Chitrapathak
0.31 ± 0.16
0.07 ± 0.09
0.60 ± 0.20
0.33 ± 0.27
0.27 ± 0.16
0.09 ± 0.15
0.43 ± 0.14
0.07 ± 0.12
0.54 ± 0.21
0.12 ± 0.15
Gemma-3
0.59 ± 0.16
0.32 ± 0.13
0.98 ± 0.14
0.75 ± 0.12
0.78 ± 0.14
0.44 ± 0.13
0.65 ± 0.41
0.18 ± 0.12
1.05 ± 0.68
0.58 ± 0.18
LLaMA-4
0.30 ± 0.22
0.09 ± 0.14
1.68 ± 3.58
1.10 ± 0.65
0.41 ± 0.21
0.13 ± 0.12
0.53 ± 0.50
0.13 ± 0.19
0.77 ± 0.57
0.20 ± 0.11
GPT-4o
0.76 ± 0.26
0.42 ± 0.23
1.26 ± 1.18
0.94 ± 0.75
0.88 ± 0.42
0.57 ± 0.80
1.23 ± 1.97
0.69 ± 1.63
1.41 ± 0.98
0.85 ± 0.35
Gemini-2.5
0.25 ± 0.11
0.03 ± 0.02
0.55 ± 0.25
0.21 ± 0.14
0.25 ± 0.15
0.06 ± 0.11
0.42 ± 0.18
0.05 ± 0.04
0.51 ± 0.29
0.08 ± 0.10
Table 13: IndicVisionBench-OCR WER and CER statistics. Model-wise WER and CER statis-
tics where the scores are more than 1. We present the count as well as percentage of the examples
for each model.
Model
WER > 1
CER > 1
Count
%
Count
%
Maya
22
2.51
15
1.71
PALO
51
5.82
45
5.14
Pangea
77
8.79
34
3.88
Chitrarth-1
302
34.47
169
19.29
Chitrapathak
8
0.91
0
0.00
Gemma-3
79
9.01
10
1.14
LLaMA-4
68
7.76
28
3.19
GPT-4o
286
32.64
115
13.12
Gemini-2.5
15
1.71
0
0.00
21

--- Page 22 ---\n\nGPT
The art depicted on this shawl is characteristic
of Gond tribal art from central India. Gond art
is a traditional form of painting and textile
design practiced by the Gond people, one of the
largest indigenous communities in India. This
art form is known for its vibrant colors,
intricate patterns, and depiction of nature and
animals.....
Gemini
The shawl depicts elements of Gond art, a
traditional tribal art form predominantly
practiced by the Gond and other related tribes
in central India, particularly in the states of
Madhya Pradesh, Chhattisgarh, and parts of
Maharashtra, Andhra Pradesh, and Odisha...
Llama
The shawl in the image showcases a traditional
tribal art form from central India, specifically
the Gond art style. Gond art is a traditional
form of painting practiced by the Gond tribe,
one of the largest tribal communities in India,
primarily residing in the states of Madhya
Pradesh, Chhattisgarh, and parts of
Maharashtra and Andhra Pradesh.....
Pangea
The shawl in the image features a design that is
reminiscent of traditional tribal art from central
India, specifically the region of Madhya
Pradesh. The art style depicted here is often
associated with the local tribal communities
such as the Gond, who are known for their
intricate and symbolic motifs....
Maya
The shawl in the image features traditional
tribal art from central India, which includes
designs depicting various animals such as
elephants, bears, and birds. These animals are
often depicted in black and white patterns,
showcasing the artistic style of the region. The
shawl showcases the cultural heritage and
craftsmanship of the........
Palo
The shawl in the image features traditional
tribal art from central India, specifically from
the region of Gujarat. The artwork showcases
various animals, including elephants, birds, and
people, which are common motifs in the tribal
art of this region.....
Chitrarth
The shawl in the image features a traditional
tribal art form known as Gond painting. This
art form is characterized by intricate patterns
and vibrant colors, often depicting nature,
animals, and human figures. The Gond people,
who are indigenous to central India, are known
for their rich cultural heritage and artistic
expression....
Gemma
Based on the imagery and style visible in the
image, the shawl depicts Pithora painting, a
traditional tribal art form originating from the
Rathwa community in Gujarat and Rajasthan,
but also found and practiced by other tribes in
central India. While the Rathwa are its primary
creators, the influence and similar art forms are
seen in Madhya Pradesh and neighboring
areas.....
Adversarial Answer
The shawl features a traditional textile design from
Nagaland, a state in Northeast India, not central
India.
Adversarial Question
What kind of traditional tribal art from central India is
depicted on this shawl?
Figure 9: Model outputs on IndicVisionBench-VQA. We show an example of an adversarial
question along with the corresponding model outputs.
22

--- Page 23 ---\n\nA group of young Indian boys are enthusiastically playing 
football in a muddy street or field in Kolkata, West Bengal. 
One boy in a bright yellow shirt with a green collar is kicking
 the black and white football, causing a substantial splash 
of mud and water. Another boy in a red sleeveless shirt with 
a Vodafone logo is running nearby, also covered in mud. 
A third boy in a light green t-shirt and shorts, similarly 
covered in mud, is looking towards the camera with a 
slight smile. On the right, a boy in a grey vest and dark 
shorts is running through the mud, creating a large mud splash. 
In the background, other boys are visible, and there are 
buildings with orange walls and windows, along with green 
grass and a metal gate. The overall scene captures the 
vibrant energy of street football during the monsoon season.
English Input
একদল তরুণ ভারতীয় ছেলে কোলকাতা, পশ্চিমবঙ্গের একটি কাদামাটি রাস্তাায় বা মাঠে ফুটবল খেলছে। 
একটি উজ্জ্বল হলুদ শার্টের একটি ছেলে কালো এবং সাদা ফুটবল লাথি মারছে, যার ফলে প্রচুর কাদা 
এবং জলের স্প্ল্যাাশ হয়েছে। একটি লাল স্লিভলেস শার্টের একটি ছেলে কাছাকাছি দৌড়াাচ্ছে, কাদায়ও 
ঢাকা রয়েছে। একটি হালকা সবুজ টি-শার্ট এবং শর্টসের একটি ছেলে ক্যাামেরার দিকে তাকিয়ে 
সামান্য হাসছে। ডানদিকে একটি ছেলে ধূসর রঙের জামা এবং গাঢ় শর্টস নিয়ে কাদামাটি দিয়ে 
দৌড়াাচ্ছে। পিছনে অন্যাান্য ছেলেরা দৃশ্যমান, কমলা দেয়াাল এবং জানালা সহ বিল্ডিংং এবং সবুজ ঘাস 
এবং একটি ধাতব গেট।
Chitranuvad Output
কিছু ভারতীয় ছেলে কলকাতার একটি কাদামাখা রাস্তাা বা মাঠে উচ্ছ্বাাসের সাথে ফুটবল খেলছে। 
একটি উজ্জ্বল হলুদ শার্ট এবং সবুজ কলার পরা ছেলে একটি কালো ও সাদা ফুটবল লাথি মারছে, 
যার ফলে কাদা ও জল ছিটকে যাচ্ছে। ভোডাফোন লোগো সহ একটি লাল হাতকাটা শার্ট পরা 
আরেকটি ছেলে কাছাকাছি দৌড়াাচ্ছে, সেও কাদায় মাখা। হালকা সবুজ টি-শার্ট এবং শর্টস 
পরা তৃতীয় ছেলেটি ক্যাামেরার দিকে তাকিয়ে একটু হাসছে, সেও কাদায় মাখা। ডানদিকে, 
একটি ছাই রঙের ভেস্ট এবং গাঢ় শর্টস পরা একটি ছেলে কাদার মধ্যে দৌড়াাচ্ছে, যার ফলে বড় 
কাদার ছিটা হচ্ছে। পেছনে আরও কয়েকটি ছেলে দেখা যাচ্ছে, এবং কমলা রঙের দেওয়াাল ও 
জানালা সহ ভবন, সবুজ ঘাস এবং একটি ধাতব গেট রয়েছে। এই দৃশ্যটি বর্ষা মৌসুমে স্ট্রিট 
ফুটবলের প্রাণবন্ত শক্তি ধারণ করে।
GPT Output
পশ্চিমবঙ্গের কলকাতার একটি কর্দমাক্ত রাস্তাা বা মাঠে একদল তরুণ ভারতীয় ছেলে উত্সাহের 
সাথে ফুটবল খেলছে। একটি উজ্জ্বল হলুদ শার্ট এবং সবুজ কলার পরা একটি ছেলে কালো-সাদা 
ফুটবলটিতে লাথি মারছে, যার ফলে কাদা এবং জলের একটি বড় ছিটকিনি তৈরি হচ্ছে। 
লাল হাতাবিহীন শার্ট এবং ভোডাফোন লোগো পরা অন্য একটি ছেলে কাছাকাছি দৌড়াাচ্ছে, সেও 
কাদায় ঢাকা। হালকা সবুজ টি-শার্ট এবং শর্টস পরা তৃতীয় একটি ছেলে, একইভাবে কাদায় 
ঢাকা, সামান্য হাসি নিয়ে ক্যাামেরার দিকে তাকিয়ে আছে। ডানদিকে, ধূসর ভেস্ট এবং গাঢ় শর্টস 
পরা একটি ছেলে কাদার মধ্য দিয়ে দৌড়াাচ্ছে, যার ফলে কাদার একটি বড় ছিটকিনি তৈরি হচ্ছে। 
পটভূমিতে, অন্যাান্য ছেলেদের দেখা যাচ্ছে এবং কমলা দেয়াাল ও জানালা সহ ভবন, সবুজ ঘাস 
এবং একটি ধাতব গেট রয়েছে। সামগ্রিক দৃশ্যটি বর্ষাকালে রাস্তাার ফুটবলের প্রাণবন্ত শক্তিকে তুলে ধরে।
Gemini Output
কোলকাতার পশ্চিমবঙ্গের একটি কর্দমাক্ত রাস্তাা বা মাঠে একদল তরুণ ভারতীয় ছেলে উৎসাহের 
সাথে ফুটবল খেলছে। একজন ছেলে উজ্জ্বল হলুদ শার্ট পরে সবুজ কলারের সাথে একটি 
কালো এবং সাদা ফুটবল লাথি মারছে, যার ফলে প্রচুর পরিমাণে কর্দমাক্ত জল এবং জল ছিটকে পড়ছে। 
লাল স্লিভলেস শার্ট পরা আরেকটি ছেলে ভোডাফোনের লোগো নিয়ে কাছাকাছি দৌড়াাচ্ছে, যার গায়েও 
কর্দমাক্ত। তৃতীয় ছেলেটি হালকা সবুজ টি-শার্ট এবং শর্টস পরেছে, যার গায়েও কর্দমাক্ত, সামান্য হাসি 
দিয়ে ক্যাামেরার দিকে তাকিয়ে আছে। ডানদিকে, একটি ধূসর ভেস্ট এবং গাঢ় শর্টস পরা একটি ছেলে 
কর্দমাক্ত জলের মধ্য দিয়ে দৌড়াাচ্ছে, যার ফলে বড় কর্দমাক্ত জলের স্প্ল্যাাশ হচ্ছে। পটভূমিতে, অন্যাান্য 
ছেলেরা দৃশ্যমান, এবং কমলা দেয়াাল এবং জানালা সহ ভবন, সবুজ ঘাস এবং একটি ধাতব গেট রয়েছে। 
এই দৃশ্যটি বর্ষাকালে রাস্তাার ফুটবলের প্রাণবন্ত শক্তিকে ধারণ করে।
Chitrarth Output
কলকাতার পশ্চিমবঙ্গ রাজ্যের একটি কাদা মাখা রাস্তাা বা মাঠে 
একদল অল্পবয়সী ভারতীয় ছেলে ফুটবল খেলছে। উজ্জ্বল হলুদ শার্ট 
এবং সবুজ কলার পরা একটি ছেলে কালো এবং সাদা ফুটবল লাথি মারছে, 
যার ফলে প্রচুর কাদা ও জলের ছিটকে পড়ছে। লাল রঙের স্লিভলেস শার্টে 
ভোডাফোন লোগো দেওয়া অন্য একটি ছেলে কাছাকাছি দৌড়াচ্ছে, তার 
শরীরও কাদায় ঢাকা। হালকা সবুজ টি-শার্ট এবং শর্টস পরা তৃতীয় একটি 
ছেলে ক্যাামেরার দিকে তাকিয়ে সামা  ্
য হাসছে। ডানদিকে, 
ধূসর রঙের ভেস্ট এবং গাঢ় শর্টস পরা একটি ছেলে কাদা দিয়ে ছুটে যাচ্ছে 
এবং বড়Splash তৈরি করছে। পটভূমিতে আরও কিছু ছেলে দেখা যাচ্ছে, 
এছাড়া কমলা রঙের দেওয়াাল এবং জানালাযুক্ত বিল্ডিংং, সবুজ ঘাস 
এবং একটি ধাতব গেটও রয়েছে। সামগ্রিকভাবে দৃশ্যটি বর্ষাকালে রাস্তাার 
ফুটবলের প্রাণবন্ততাকে তুলে ধরে।
Gemma Output
পশ্চিমবঙ্গের কলকাতার একটি কাদা ভরা রাস্তাায় বা মাঠে ভারতীয় একদল যুবক উৎসাহের সাথে ফুটবল খেলছে। 
সবুজ কলার সহ উজ্জ্বল হলুদ শার্ট পরা এক ছেলে কালো এবং সাদা ফুটবলটি লাথি মারছে, যার ফলে কাদা 
এবং জলের যথেষ্ট ছিটে পড়ছে। ভোডাফোন লোগো সহ লাল হাতা ছাড়াা শার্ট পরা আরেকটি ছেলে কাছাকাছি 
দৌড়াাচ্ছে, সেও কাদায় আবৃত। হালকা সবুজ টি-শার্ট এবং শর্টস পরা তৃতীয় একটি ছেলে, একইভাবে 
কাদায় ঢাকা,    ্
যামেরার দিকে সামান্য হাসি দিয়ে তাকিয়ে আছে৷ ডানদিকে, ধূসর রঙের ভেস্ট 
এবং গাঢ় শর্টস পরা একটি ছেলে কাদার মধ্য দিয়ে দৌড়াাচ্ছে, একটি বড় কাদার ছিটা তৈরি করছে। 
পটভূমিতে অন্যাান্য ছেলেরা দেখা যাচ্ছে এবং কমলা দেয়াাল এবং জানালা সহ ভবন রয়েছে, সাথে 
সবুজ ঘাস এবং একটি ধাতব গেট রয়েছে। সামগ্রিক দৃশ্যটি বর্ষাকালে রাস্তাার ফুটবলের প্রাণবন্ত শক্তি ধরে রেখেছে।
Llama Output
একটি দল যুবক ইন্দিয়াান ছেলেরা একটি মটরশিপ রাস্তাা বা মাঠে উত্সাহে ফুটবল খেলছে কলকাতা, পূর্ববঙ্গে। 
একটি উজ্জ্বল হলুদ শার্ট পরিধান করা একটি ছেলে কালো এবং সাদা ফুটবল পাঠাচ্ছে, যা মাটি এবং 
পানি দিয়ে একটি বৃহত্তর মাটি ছড়িয়ে দিচ্ছে। আরেকটি ছেলে, একটি লাল স্লিভলেস শার্ট পরিধান করা, 
যার উপরে একটি ভোডাফোন লোগো রয়েছে, নিকটবর্তীতে দৌড়ছে, এটি মাটিতে আচ্ছাাদিত। 
একটি তৃতীয় ছেলে, একটি হালকা সবুজ টি-শার্ট এবং শর্টস পরিধান করা, এটি মাটিতে আচ্ছাাদিত 
হয়ে দেখাচ্ছে এবং ক্যাামেরা দিকে তাকিয়ে দেখছে একটি সামান্য হাসি দিয়ে। ডান পাশে, একটি ছেলে 
একটি ধূসর ভেস্ট এবং কালো শর্টস পরিধান করে দৌড়ছে, মাটি ছড়িয়ে দিচ্ছে। পশ্চাাদপটে, কিছু 
অন্যাান্য ছেলে দেখা যাচ্ছে, এবং পটভূমিতে কমলা দেওয়াা দেওয়াা দেওয়াা দেওয়াা দেওয়াা দেওয়াা দেওয়াা
 দেওয়াা দেওয়াা দেওয়াা দেওয়াা দেওয়াা দেওয়াা দেওয়াা দেওয়াা দেওয়াা ........ REPEATS
Maya Output
একটি গ্রুপ তরুণ ইন্দিয়াান ছেলেরা একটি কলকাতার মধ্যে একটি 
মটর রাস্তাা বা মাঠে উত্সাহে ফুটবল খেলছে। একজন ছেলে 
একটি উজ্জ্বল হলুদ শার্ট এবং সবুজ কলারের সাথে একটি 
কালো এবং সাদা ফুটবল ছুঁড়ে একটি বড় মটর ছিটকে 
ছিটকে ছিটকে ছিটকে ছিটকে ছিটকে ছিটকে ছিটকে....... REPEATS
PALO Output
ছবিতে দেখা যাচ্ছে, কলকাতার বিশ্বব্যাাপী বিখ্যাাত বাংলাদেশী 
ফুটবল খেলোয়াাড় সাদিক খাদেমের ছেলেরা মাঝে মাঝে 
একটি মাঝে মাঝে মাঝে মাঝে মাঝে মাঝে...... REPEATS
Pangea Output
Figure 10: Model outputs on IndicVisionBench-MMT. Example of an MMT question and the
corresponding responses from multiple models.
Question
ವ್ಯಕ್ತಿ ಧರಿಸಿದ ಪ್ರಮುಖ ಶಿರ ಧಿರಿಸಿನ ಮೇಲೆ ಯಾವ ಸಾಮಾನ್ಯ ಹಿಂಂದೂ ದೇವತೆ ಅಥವಾ ಚಿಹ್ನೆಯನ್ನು ನೋಡಬಹುದಾಗಿದೆ? 
GPT
ನಾನು ಈ ಚಿತ್ರದಲ್ಲಿ ವ್ಯಕ್ತಿಯ ಗಾತ್ರದ ಆಭರಣದ
ಮೇಲೆ ಏನಿದೆ ಎಂದು ಗುರುತಿಸಲು ಸಾಧ್ಯವಿಲ್ಲ.
Chitrarth
ವ್ಯಕ್ತಿಯು ಧರಿಸಿರುವ ಪ್ರಮುಖ ಶಿರೋವಸ್ತ್ರದ ಮೇಲೆ
ನಾಗ ದೇವತೆಯ ಚಿಹ್ನೆಯನ್ನು ಕಾಣಬಹುದು.
Gemma
ಚಿತ್ರದಲ್ಲಿರುವ ಶಿರೋcrestವು ಸಾಮಾನ್ಯವಾಗಿ ಶಿವ
ದೇವರನ್ನು ಸೂಚಿಸುತ್ತದೆ. ಇದು ಶಿವನ
ಜಟಾಮುಖುಟದ ಪ್ರತೀಕವಾಗಿದೆ. 
ಇದಲ್ಲದೆ, ಇದು ಸ್ಥಳೀಯ ದೇವತೆಗಳ ಪೂಜೆಯಲ್ಲಿ
ಸಹ ಬಳಸಲಾಗುತ್ತದೆ.
Gemini
ವ್ಯಕ್ತಿಯ ಶಿರ ಧಿರಿಸಿನ ಮೇಲೆ ಹಾವಿನ ಹೆಡೆ
(ನಾಗ) ಚಿಹ್ನೆಯನ್ನು ನೋಡಬಹುದಾಗಿದೆ. ಇದು
ಹಿಂಂದೂ ಧರ್ಮದಲ್ಲಿ ಪೂಜಿಸಲ್ಪಡುವ ನಾಗ
ದೇವತೆಗಳನ್ನು ಅಥವಾ ನಾಗಗಳನ್ನು
ಪ್ರತಿನಿಧಿಸುತ್ತದೆ.
Llama
ಆತನ ತಲೆಯ ಮೇಲಿರುವ ಚಿತ್ರದಲ್ಲಿ ನಾವು ನಾಗರಹಾವು ಅಥವಾ ಕಾಳಿಂಂಗ ಸರ್ಪದ ಚಿಹ್ನೆಯನ್ನು ನೋಡಬಹುದು. ಇದು ಶಿವನ
ಸಂಕೇತವಾಗಿದೆ.
Answer
ಶಿರಸ್ತ್ರಾಣವು ಐದು ತಲೆಯ ನಾಗರಹಾವಿನ ಬೆಳ್ಳಿಯ ಬಣ್ಣದ ಆಕೃತಿಯನ್ನು ಹೊಂಂದಿದೆ, ಇದು ಸಾಮಾನ್ಯವಾಗಿ ನಾಗ ಅಥವಾ ಸರ್ಪಗಳೊಂಂದಿಗೆ
ಸಂಬಂಧ ಹೊಂಂದಿದೆ, ಇದು ಹಿಂಂದೂ ಪುರಾಣಗಳಲ್ಲಿ ಪ್ರಮುಖ ಸಾಂಕೇತಿಕ ಮೌಲ್ಯವನ್ನು ಹೊಂಂದಿದೆ, ಇದನ್ನು ಹೆಚ್ಚಾಗಿ ಶಿವ ಅಥವಾ
ವಿಷ್ಣುವಿಗೆ ಸಂಬಂಧಿಸಿದೆ.
Figure 11: Model outputs on IndicVisionBench-VQA. We show an example of an VQA output
for corresponding models.
23

--- Page 24 ---\n\nदो बहने
लिखा है, रिसर्च के जिस दुरूह कार्य में नोरद अपने
आपको लगा देना चाहता है, वह भारतवर्ष में सम्भव नहीं
है। इसीलिये उसे अपने जीवन में एक और बड़ाा बलिदान
करना पड़ेगा। ऊर्मि के साथ विवाह सम्बन्ध विच्छिन्न
किए बिना अब चल ही नहीं सकता। एक यूरोपीय महिला
उसके साथ विवाह करके उसके कार्य में आत्मनियोग
करने को तैयार हैं। लेकिन काम तो बही है, भारतवर्ष
में हो तो, और विलायत में हो तो । राजारामबाबू ने
जिस कार्य के लिये धन देना बाहा था, उसका कुछ
हिस्साा वहाँ लगाने में कोई अन्यााय नहीं है। उससे
मृत्त व्यक्ति का सम्माान ही होगा ।
शशांक ने कहा, "जीवित व्यक्ति को कुछ-कुछ देकर
यदि उस दूरदेश में ही जिला रख सको तो बुरा क्याा है ?
क्योंोंकि
 यदि रुपया बंद कर दिया जाय तो भूख की ज्वााला
से अधमरा होकर यहाँ दौड़ाा चला आयगा, यह आशंका
है।"
ऊर्मि ने हँसकर कहा, "यदि तुम्हाारे मन में यह डर
हो तो रुपया तुम्हींीं भेजना, मैं तो एक पैसा भी नहीं देती।"
शशांक बोला, "फिर से मन तो नहीं बदलेगा न ?
मानिनी का अभिमान तो अटल ही बना रहेगा ?"
६७
Gemini
Gemma
दो बहनें-
लिखा है, रिस्वत के जिस दुखद कार्य में नारद अपने आपको लगा
देना चाहता है, वह भारतवर्ष में सम्भव नहीं है | इसीलिये उसे अपने
जीवन में एक और बड़ाा बलिदान करना पड़ेगा | ऊर्मि के साथ
विवाह-सम्बन्ध विच्छिन्न किए बिना अब चल ही नहीं सकता | एक
यूरोपीय महिला उसके साथ विवाह करके उसके कार्य में
आत्मनियोग करने को तैयार है | लेकिन काम तो वही है, भारतवर्ष में
हो तो, और विलायत में हो तो | राजारामबाबू ने जिस कार्य के लिये
धन देना चाहा था, उसका कुछ हिस्साा वहाँ लगाने में कोई अन्यााय
नहीं है | उससे मृत व्यक्ति का सम्माान ही होगा | 
श्रााद्धनिक ने कहा, “औचित्य की कुछ-कुछ देर तक यदि उस दूरदेश
में ही जिला रख सकते तो बुरा क्याा है ? क्योंोंकि
 यदि रुपया खंड कर
दिया जाय तो भूल की ज्वााला से अग्रभारा होकर यहाँ दीदा बदला
आगया, यह आशंका है।”
x
ऊर्मि ने हँसकर कहा, “यदि तुम्हाारे मन में यह डर हो तो क्याा तुम्हें
भेजना, मैं तो एक पैसा भी नहीं देती |”
श्रााद्धनिक बोला, “फिर से मन तो नहीं बदलेगा न ? मानिनी का
अभिमान तो अटल ही बना रहेगा ?”
६१
दो बहनें
लिखा है, रिचर्ड के जिस दुरूह कार्य में नोरद अपने
आपको लगा देना चाहता है, वह भारतवर्ष में सम्भव नहीं
है। इसीलिये उसे अपने जीवन में एक और बड़ाा बलिदान
करना पड़ेगा। ऊर्मि के साथ विवाह सम्बन्ध विच्छिन्न
किए बिना अब चल ही नहीं सकता। एक यूरोपीय महिला
उसके साथ विवाह करके उसके कार्य में आत्मनियोग
करने को तैयार हैं। लेकिन काम तो वही है, भारतवर्ष
में हो तो, और विलायत में हो तो । राजारामबाबू ने
जिस कार्य के लिये धन देना चाहा था, उसका कुछ
हिस्साा वहाँ लगाने में कोई अन्यााय नहीं है। उससे
मृत व्यक्ति का सम्माान ही होगा।
शशांक ने कहा, "जीवित व्यक्ति को कुछ-कुछ देकर
यदि उस दूरदेश में ही मिला रख सको तो बुरा क्याा है?
क्योंोंकि
 यदि रुपया बंद कर दिया जाय तो भूख की ज्वााला
से अधमरा होकर यहाँ दौड़ाा चला आयगा, यह आशंका
है।"
ऊर्मि ने हँसकर कहा, "यदि तुम्हाारे मन में यह डर
हो तो रुपया तुम्हींीं भेजना, मैं तो एक पैसा भी नहीं देती।"
शशांक बोला, "फिर से मन तो नहीं बदलेगा न?
मानिनी का अभिमान तो अटल ही बना रहेगा?"
Chitrapathak
दो बहनें
लिखा है, रिसर्च के जिस तुच्छ कार्य में नोरद अपने आपको लगा देता
चाहता है, वह भारतवर्ष में सम्भव नहीं है। इसलिये उसे अपने जीवन
में एक और बड़ा बलिदान करना पड़ेगा। ऊर्मि के साथ विवाह-
सम्बन्ध विच्छिन्न किए बिना अब चल ही नहीं सकता। एक यूरोपीय
महिला उसके साथ विवाह करके उसके कार्य में आत्मनियोग करने
को तैयार हैं। लेकिन काम तो वही है, भारतवर्ष में हो तो, और
विलायत में हो तो ! राजाराम बाबू ने जिस कार्य के लिये धन देना
चाहा था, उसका कुछ हिस्साा वहाँ लगाने में कोई अन्यााय नहीं है !
उससे मृत व्यक्ति का सम्माान ही होगा।
शाशांक ने कहा, “जीवित व्यक्ति को कुछ-कुछ देकर यदि उस
दूरदेश में ही जिला रख सको तो बुरा क्याा है ? क्योंोंकि
 यदि रुपया
बंद कर दिया जाय तो भूख की दुहाई मचा अधमरा होकर यहाँ दौड़ा
आयेगा, यह आशंका है !”
ऊर्मि ने हँसकर कहा, “यदि तुम्हाारे मन में यह डर हो तो रुपया तुम्हींीं
भेजना, मैं तो एक पैसा भी नहीं देती !” शाशांक बोला, “फिर से मन
तो नहीं बदलेगा न ? मानिनी का अभिमान तो अटल ही बना रहेगा ?”
२७
Llama
दो बहनें
लिखा है, रिश्ते के जिन्द मुद्द््ति मार्ग में नारद अपने 
आपको त्याग देकर समाप्त हुआ है, वह भारतवर्ष में समाप्त नहीं 
है। इसलिए उसे अपने जीवन में एक और बड़ाा बलिदान 
करना पड़ेगा। उर्मी के साथ विवाह-सम्बन्ध विच्छिन्न 
किए बिना भव की नहीं सकता। एक युरोपीय महिल 
उसके साथ विवाह करके उसके कार्य में आत्मसमर्पण 
करने को तैयार हैं। लेकिन बातें तो वही हैं, भारतवर्ष 
में हो तो, और विदेश में हो तो। राजारामबाबू ने 
जिसका ब्यााह करके घर से चुपचाप भेजा था, उसका कुछ 
हिस्साा घर में लौटाने में कोई अत्याय नहीं है। उससे 
मृत व्यक्ति का सम्माान ही होगा। 
शशांक ने कहा, "जीवित व्यक्ति को कुछ-कुछ देकर 
यदि उसे दूरदेश में ही जिलर रखने तो बुरा क्याा है ? 
क्योंोंकि
 यदि गधया बंध कर दिया जाय तो भूख की ख्वााक 
बे अच्छभ होअर यहाँ दौड़ाा चला आयेगा, यह आशंका 
है!"
उर्मी ने हँसकर कहा, "यदि तुम्हाारे मन में यह खत्य 
हो तो कतया तुम्हें भेजना, मैं तो एक पैसा भी नहीं देती।'' 
शशांक बोला, "फिर से मन तो नहीं बदलोगी न? 
माननी का अभिमान तो अचल ही बना रहेगा ?" 
२७
GPT
हिंदी में अनुवाद करें: हिंदी में अनुवाद करें: हिंदी में अनुवाद करें:
हिंदी में अनुवाद करें: हिंदी में अनुवाद करें: हिंदी में अनुवाद करें:
हिंदी में अनुवाद करें: हिंदी में अनुवाद करें: हिंदी में अनुवाद करें:
हिंदी में अनुवाद करें......
Maya
I am sorry, but I am unable to extract the exact text
from the image using OCR.
Palo
The text in the image is in Hindi, and it appears to be a
narrative or a story. The text is too small and dense to
transcribe accurately without the aid of OCR software, which
is not available in this environment. However, if you need the
text translated or transcribed, I can assist with that by using
OCR software or by manually transcribing it if the text is
legible enough. Please note that the quality of the OCR
process can vary depending on the clarity of the text in the
image.<|im_end|>
Pangea
Figure 12: Model outputs on IndicVisionBench-OCR. We show an example of an OCR output
for corresponding models.
24

--- Page 25 ---\n\nD
DATASET ANALYSIS AND BENCHMARK DETAILS
We provide more details about our dataset here. Figure 5 shows that the dataset spans diverse cul-
tural categories, with the largest shares in Heritage (12.4%), Religion (11.2%), Architecture (11.1%),
Food (8.6%), and Lifestyle (8.1%). The numbers of these categories are provided in Figure 3 with
4698 and 4212 questions for Heritage and Religion respectively. Also, Hindi has the largest share of
QA pairs (26.8%) followed by Kannada (11.9%) and Tamil (9.7%) among Indic languages. Inter-
estingly, Adversarial questions have the shortest length (15) while their answers have greater length
(44) than Short-QAs (18 and 21). Meanwhile in IVB-MMT, the caption length in number of words
follows a distribution with mean = 131.30 and std = 43.52 for Hindi. We expect that the distribution
for other languages will also be the same. On the other hand, in the OCR track, the average number
of words for different languages vary significantly with Hindi (329) and Gujarati (247) topping the
table and Tamil (121) and Malayalam (127) being the least. Please refer to Table 14 for details of the
dataset. Moreover, Table 15 shows the State/UT-wise image distribution of the data set. Figure 13
presents word clouds by category, where the word ‘traditional’ emerges as a dominant term across
domains, underscoring the cultural grounding of the benchmark. Alongside, category-specific con-
cepts appear prominently — e.g., sweet and dish in Food, palace and temple in Heritage, dance and
instrument in Music, and buddhist and church in Religion. This distribution confirms that IVB-VQA
emphasizes India’s traditional practices while maintaining diversity across food, heritage, festivals,
lifestyle etc.
Table 14: Summary of IndicVisionBench datasets.
Task
#Images
Languages
Type
OCR
876
10
Image–text pairs
VQA-EN
4117
English
6 QA types
VQA-Indic
1007
10
Indic langs QA
VQA-Parallel
106
English+10
Parallel QA
MMT
106
English+10
Parallel captions
Table 15: State/UT-wise image distribution in IndicVisionBench-VQA.
State/UT
#Images
State/UT
#Images
Andaman & Nicobar
97
Madhya Pradesh
98
Andhra Pradesh
107
Maharashtra
128
Arunachal Pradesh
99
Manipur
100
Assam
101
Meghalaya
75
Bihar
120
Mizoram
78
Chandigarh
100
Nagaland
94
Chhattisgarh
90
Odisha
116
Dadra & Nagar Haveli, Daman & Diu
54
Puducherry
106
Delhi
141
Punjab
108
Goa
101
Rajasthan
131
Gujarat
110
Sikkim
97
Haryana
99
Tamil Nadu
139
Himachal Pradesh
99
Telangana
111
Jammu & Kashmir
105
Tripura
97
Jharkhand
94
Uttar Pradesh
129
Karnataka
242
Uttarakhand
112
Kerala
116
West Bengal
109
Ladakh
99
Pan-India
320
Lakshadweep
101
–
–
25

--- Page 26 ---\n\nD.1
TOPICS COVERED
Topics covered using IndicVisionBench
The categories that we have for the crawled images are as follows:
• Food: Iconic regional cuisines and dishes
• Lifestyle: Traditional attire, daily routines, and modern practices
• Literature: Renowned works, authors, and poets
• Music and Dance: Classical, folk, and traditional performance arts
• Religion: Major faiths, rituals, and festivals
• Customs: Cultural etiquette and greeting practices
• Festivals: National and regional celebrations
• Heritage: Monuments, sites, and landmarks of historical importance
• Economy: Key industries and occupations
• Media: Popular entertainment figures, cinema, and television
• Architecture: Traditional Art and Architecture
• Sports: Indigenous games and traditional sports
• Notable Figures: Influential leaders and historical personalities
Table 16: Comparison of existing VQA evaluation datasets with IndicVisionBench. IndicVi-
sionBench supports 3 multi-lingual tasks compared to existing benchmarks.
Dataset
No. Questions
No. Images
Multilingual?
Task Format
Culturally Diverse Images?
MaXM (Changpinyo et al., 2023)
2,142
335
✓
VQA
No
GDVCR (Yin et al., 2021)
886
328
✗
VQA
Yes
MaRVL (Liu et al., 2021)
5,670
4,914
✓
VQA
Yes
CVQA (Romero et al., 2024)
9,044
4,560
✓
VQA
Yes
CulturalVQA(Romero et al., 2024)
2,378
2,328
✗
VQA
Yes
ALM-Bench(Vayani et al., 2025)
22,763
2,328
✓
VQA
Yes
IndicVisionBench
37,740
4,993
✓
VQA, OCR, MMT
Yes
Table 17: Evaluation metrics used for different tasks in IndicVisionBench highlighting deter-
ministic and non-deterministic measures along with their rationale.
Task
Deterministic
Non-deterministic
Rationale
OCR
ANLS, WER, CER
–
Robustness to script
VQA
Exact Match
LLM-as-a-Judge
QA accuracy + reasoning quality
MMT
BLEU, RIBES
–
Translation quality
26

--- Page 27 ---\n\n(a) Food
(b) Media
(c) Music
(d) Sports
(e) Customs
(f) Economy
(g) Heritage
(h) Religion
(i) Festivals
(j) Lifestyle
(k) Literature
(l) Architecture
Figure 13: Word clouds of different categories in IndicVisionBench-VQA. We omit the words
“India” & “Indian” in the word clouds to show other important topics.
27

--- Page 28 ---\n\nD.2
EXAMPLES OF OUR DATASET
MCQ
घाटों के निर्माण में इस्तेमाल होने वाली प्राथमिक सामग्रीी क्याा है?
 Choices:
 A. गहरे लाल रंग की ईंट
 B. हल्केे भूरे और बेज रंग का पत्थर
 C. ग्रे कंक्रीीट
 D. घुटी हुई सफ़ेेद संगमरमर
Short Q2
नाव में सवार लोगों से जुड़ीी कौन-सी
बात उनके परिवेश के साथ घुलने-
मिलने का संकेत देती है?
Short Q1
घाटों के किनारे बनी इमारतों में कौन-
सी स्थापत्य विशेषताएँ उनकी उम्र और
ऐतिहासिक महत्ता का संकेत देती हैं?
Short A2
नाव में बैठे लोग गहरे रंग के कपड़े पहने हुए हैं, जो नाव के रंग से मेल खाते
हैं, जिससे दृश्य का शांत और कालातीत माहौल और मज़बूत होता है।
Short A1
ये इमारतें जर्जर दिखती हैं, इनमें अनेक खिड़कियां हैं, जिनमें से 
कुछ के शिखर मेहराबदार हैं, तथा जटिल बालकनियाँ हैं, 
जो उनकी ऐतिहासिक प्रकृति का संकेत देती हैं।
True/False
नदी की सतह को तेज़ धाराओं के साथ
अशांत दर्शाया गया है। 
गलत
Long Q
नदी और संरचनाओं के दृश्य तत्वों से परे, छवि में कौन से विशिष्ट
संकेत वाराणसी को ऐतिहासिक रूप से महत्वपूर्ण भारतीय नदी
तटीय शहर के रूप में दर्शाने में योगदान करते हैं, और ये संकेत
भारत के लिए सांस्कृृतिक रूप से प्रासंगिक क्योंों हो सकते हैं?
Long A
इस चित्र के विभिन्न संकेत वाराणसी के ऐतिहासिक महत्व को दर्शाते हैं। धुंधला आकाश और इमारतों का जर्जर स्वरूप प्राचीनता का आभास कराते हैं। घाटों की मौजूदगी, मंदिरों जैसी 
शिखरनुमा संरचनाएँ, और नदी किनारे लोग जो अपने दैनिक कार्यों में लगे हैं, ये सभी सांस्कृृतिक रूप से बेहद महत्वपूर्ण हैं। वाराणसी में घाट हिंदू रीति-रिवाज़ोंों और दैनिक जीवन का अहम हिस्साा हैं, 
जहाँ लोग पवित्र गंगा नदी में स्नाान और अन्य धार्मिक अनुष्ठाान करते हैं। मंदिरों की उपस्थिति इस शहर की धार्मिक महत्ता को और भी स्पष्ट करती है, जो भारत में एक प्रमुख तीर्थस्थल के रूप में जाना 
जाता है। ये सभी तत्व मिलकर एक शाश्वत और आध्याात्मिक वातावरण रचते हैं, जो वाराणसी की प्राचीन विरासत को एक जीवित आस्था और परंपरा के शहर के रूप में दर्शाते हैं।
Adversarial
इस नदी के किनारे बनी इमारतों में किस तरह की पारंपरिक
मणिपुरी वास्तुकला दिखाई देती है?
Adversarial A
तस्वीर में उत्तर प्रदेश के वाराणसी में गंगा नदी के किनारे बने ऐतिहासिक घाट और इमारतें 
दिखाई गई हैं, जिनमें विशिष्ट उत्तर भारतीय स्थापत्य शैली है, न कि मणिपुरी वास्तुकला।
B
Figure 14: Example from IndicVisionBench-VQA. shown in Hindi
Short Q2
ପଟ୍ଟର କେନ୍ଦ୍ରରେ, କୃଷ୍ଣଙ୍କ ଉପରେ ଧରାଯାଇଥିବା
ଛତାର ରଙ୍ଗ କ’ଣ ?
Short Q1
ପଟ୍ଟର କେନ୍ଦ୍ରରେ ଚିତ୍ରିତ ମୁଖ୍ୟ ଆଧ୍ୟାତ୍ମିକ ଚିତ୍ର କିଏ,
ଯିଏ ନିଜର ନୀଳ ତ୍ଵଚା ଏବଂ ବଂଶୀ ଦ୍ୱାାରା ଚିହ୍ନିତ ?
Short A2
ପଟ୍ଟର କେନ୍ଦ୍ରରେ ଥିବା କୃଷ୍ଣଙ୍କ ଉପରେ ଧରାଯାଇଥିବା ଛତାଟି ଲାଲ୍ 
ଏବଂ ନୀଳ ରଙ୍ଗର ଅଟେ ।
Short A1
କୃଷ୍ଣ ହେଉଛନ୍ତି ମୁଖ୍ୟ ଆଧ୍ୟାତ୍ମିକ ଚିତ୍ର, ଯାହାଙ୍କୁ ପଟ୍ଟର କେନ୍ଦ୍ରରେ 
ଦର୍ଶାାଯାଇଛି, ତାଙ୍କର ନୀଳ ଚର୍ମ ଓ ବଂଶୀରୁ ତାଙ୍କୁ ଚିହ୍ନି ହେବ ।
True/False
ପଟ୍ଟର କେନ୍ଦ୍ରରେ ଗୋଟିଏ ମାତ୍ର ମୁଖ୍ୟ ପୌରାଣିକ ଦୃଶ୍ୟ ରହିଛି, ଯେଉଁଥିରେ ଅନ୍ୟ କୌଣସି ଛୋଟବଡ଼ ଚିତ୍ର ନାହିଁ । 
ଭୁଲ୍
Long Q
ଏହି ପଟ୍ଟଚିତ୍ରରେ ଥିବା ପାରମ୍ପରିକ କଳାତ୍ମକ ଉପାଦାନଗୁଡ଼ିକ ଏବଂ
ପ୍ରଯୁକ୍ତିଗୁଡ଼ିକ କ’ଣ, ଯାହା ଭାରତୀୟ ଲୋକକଳାରେ ଏହାର ଉତ୍ପତ୍ତି
ଏବଂ ସାଂସ୍କୃୃତିକ ପୃଷ୍ଠଭୂମିକୁ ସୂଚାଉଛି ? ଚିତ୍ରରେ ଥିବା ନିର୍ଦ୍ଦିଷ୍ଟ
ବିବରଣୀଗୁଡ଼ିକୁ ଉଲ୍ଲେଖ କରନ୍ତୁ ।
Long A
ଏହି ପଟ୍ଟଚିତ୍ର ଭାରତୀୟ ଲୋକକଳାର, ବିଶେଷକରି ଓଡ଼ିଶାର ଅନେକ ପାରମ୍ପରିକ କଳାତ୍ମକ ଉପାଦାନ ପ୍ରଦର୍ଶିତ କରୁଛି । ସାଜସଜ୍ଜାାଯୁକ୍ତ ସୀମାରେଖାରେ ଏବଂ ଦୃଶ୍ୟଗୁଡ଼ିକ ମଧ୍ୟରେ ଲାଲ୍, କଳା, ସବୁଜ, ନୀଳ 
ଓ ହଳଦିଆ ଭଳି ଉଜ୍ଜ୍ୱଳ ଏବଂ ବିପରୀତ ରଙ୍ଗର ବ୍ୟବହାର ସାଧାରଣ ଅଟେ । ଚିତ୍ରଗୁଡ଼ିକ ସ୍ପଷ୍ଟ ଆକୃତି, ସର୍ବନିମ୍ନ ଦୃଷ୍ଟିକୋଣ ଏବଂ ପୋଷାକ ଓ ଅଳଙ୍କାରରେ ଗଭୀର ଜଟିଳତା ସହିତ ଶୈଳୀକୃତ । ବର୍ଣ୍ଣନ ବିଭିନ୍ନ 
ଭିନ୍ନ ପ୍ୟାାନେଲ ମାଧ୍ୟମରେ ଉପସ୍ଥାାପିତ କରାଯାଇଛି—ଏକ ବଡ଼ କେନ୍ଦ୍ରୀୟ ଦୃଶ୍ୟ ଏବଂ ଅନେକ କ୍ଷୁଦ୍ର ଭିନିଏଟ୍‌—ପ୍ରତ୍ୟେକଟି ଭିନ୍ନ ପୌରାଣିକ କାହାଣୀକୁ ଚିତ୍ରଣ କରୁଛି, ଯାହା ଭାରତୀୟ କାହାଣୀ କହିବା କଳାରେ 
ଜଟିଳ ବର୍ଣ୍ଣନାଗୁଡ଼ିକୁ ପରିପ୍ରକାଶ କରିବା ନିମନ୍ତେ ଏକ ସାଧାରଣ ବୈଶିଷ୍ଟ୍ୟ । ହିନ୍ଦୁ ଦେବତା ଓ ପୌରାଣିକ ଘଟଣାଗୁଡ଼ିକର ଉପସ୍ଥିତି ଏକ
 ନିର୍ଦ୍ଦିଷ୍ଟ ସାଂସ୍କୃୃତିକ ଓ ଧାର୍ମିକ ପରିପ୍ରେକ୍ଷୀୀରେ କଳାକୃତିକୁ ଅଧିକ ପ୍ରତିଷ୍ଠିତ କରୁଛି, ଯାହା ଭାରତୀୟ ପାରମ୍ପରିକ ଚିତ୍ରକଳାରେ ସାଧାରଣତଃ ମନ୍ଦିର ବା ଭକ୍ତିମୂଳକ ଉଦ୍ଦେଶ୍ୟରେ ସୃଷ୍ଟି କରାଯାଇଥାଏ ।
Adversarial
କୃଷ୍ଣଙ୍କ ଚିତ୍ରଣ ସହିତ ଏହି ମଧୁବନୀ ଚିତ୍ରକଳା ଦିପାବଳୀ 
ପର୍ବକୁ କିପରି ପାଳନ କରୁଛି ?
Adversarial A
ଏହି ଚିତ୍ରକଳା ଓଡ଼ିଶାର ଏକ "ପଟ୍ଟଚିତ୍ର", ମଧୁବନୀ ଚିତ୍ର ନୁହେଁଁ । ଯଦିଓ ଏଥିରେ ଶ୍ରୀୀକୃଷ୍ଣଙ୍କୁ ଚିତ୍ରିତ କରାଯାଇଛି, ତେବେ ଏହାର ବିଷୟବସ୍ତୁୁ ବିଶେଷ 
ଭାବରେ ଦୀପାବଳି ସହିତ ଜଡ଼ିତ ନୁହେଁଁ । ଦୀପାବଳି ହେଉଛି ଏକ ହିନ୍ଦୁ ପର୍ବ ଯାହା ମୁଖ୍ୟତଃ ଲକ୍ଷ୍ମୀୀ ଓ ଗଣେଶଙ୍କ ପୂଜା ସହିତ ପାଳନ କରାଯାଏ ।
ପଟ୍ଟଚିତ୍ର ପ୍ରାୟତଃ ବିଭିନ୍ନ ହିନ୍ଦୁ ପୌରାଣିକ ବିଷୟବସ୍ତୁୁକୁ ଚିତ୍ରଣ କରିଥାଏ, ଏହା କୌଣସି ଗୋଟିଏ ପର୍ବ ଯେପରିକି ଦୀପାବଳି ସହିତ ବାନ୍ଧିହୋଇ ରହିନଥାଏ ।
MCQ
କେନ୍ଦ୍ରୀୟ ଚିତ୍ରକଳାରେ କୃଷ୍ଣଙ୍କୁ ଚିହ୍ନିବା ପାଇଁ ନିମ୍ନଲିଖିତ କେଉଁ 
ଉପାଦାନଟି ମୁଖ୍ୟତଃ ବ୍ୟବହାର କରାଯାଏ ନାହିଁ ?
 Choices:
 A. ହଳଦିଆ ପୋଷାକ
 B. ନୀଳ ତ୍ଵଚା
 C. ବଂଶୀ
 D. ଗୋପୀଗଣ ଏବଂ ଗୋଟିଏ ଧଳା ଗାଈ ଦ୍ୱାାରା ପରିବେଷ୍ଟିତ
A
Figure 15: Example from IndicVisionBench-VQA. shown in Odia
28

--- Page 29 ---\n\nShort Q2
சேபியா தொனி மற்றும் நடிகரின் உடை
ஆகியவற்றைக் கருத்தில் கொண்டு, இந்த
உருவப்படம் எந்த குறிப்பிட்ட இந்திய கலாச்சார
காலகட்டத்திற்கோ அல்லது திரைப்படத் துறை
சகாப்தத்திற்கோ மிகவும் பொருத்தமானதாகத்
தெரிகிறது?
Short Q1
திருவிழாக் கொண்டாட்டங்களில் அணியப்படும்
பாரம்பரிய ஆடைகளில் காணப்படும், ஆண்களின்
சட்டைப் பிளவுகளின் அலங்காரத்தில் காணப்படும்
குஞ்சங்கள், எந்த பாரம்பரிய இந்திய உடை
அலங்காரத்தின் தனிச்சிறப்பை உணர்த்துகிறது?
Short A2
செபியா தொனியும், வடிவமைக்கப்பட்ட, குஞ்சம் வைத்த சட்டை மற்றும்
கால்சட்டையின் தனித்துவமான ஃபேஷனும், இந்த ஓவியம் இந்திய திரைப்படத்
துறையின் பழங்காலத்தைச் சேர்ந்தது என்பதை வலுவாகக் காட்டுகிறது. இக்காலம்,
இந்தியாவின் சினிமா கலை வளர்ச்சிக்கு குறிப்பிடத்தக்க காலமாக இருந்தது.
Short A1
குஞ்சமானது ஒரு விரிவான அலங்காரக் கூறு என்று
 கருதப்படலாம், இது பழைய, அதிக ஆடம்பரமான பாணிகளை 
நினைவூட்டுகிறது, இது சில சமயங்களில் சாதாரண 
அல்லது பண்டிகைக் கால ஆடைகளில் சேர்க்கப்படுகிறது, 
இது இந்திய பாரம்பரிய உடைகளில் காணப்படும் கம்பீரத்தை சேர்க்கிறது.
True/False
நடிகரின் இடது மணிக்கட்டில் உள்ள கடிகாரத்தில் 
எளிமையான, அலங்காரமற்ற தோல் 
பட்டை உள்ளது, இது நவீன இந்திய 
அணிகலன்களில் பெரும்பாலும் காணப்படும் ஒரு
 குறைந்தபட்ச பாணியைப் பிரதிபலிக்கிறது.   
தவறு
Long Q
தமிழ்நாட்டின் ஒரு முன்னணி நடிகர் என்பதைத் தாண்டி,
சிவாஜி 
கணேசன் போன்ற ஒருவரின் பரந்த கலாச்சார முக்கியத்துவம் 
என்னவாக இருக்கும், குறிப்பாக வரலாற்று ரீதியான ரசிகர்
பட்டாளம் மற்றும் இந்த உருவப் படத்தின் காட்சி நடையை
கருத்தில் கொள்ளும்போது?
Long A
சிவாஜி கணேசன் போன்ற ஒரு உருவம் பெரும் கலாச்சார முக்கியத்துவத்தைக் கொண்டுள்ளது, குறிப்பாக இந்தியாவில். அவருடைய பழங்காலப் புகைப்படம் ஒரு 
வரலாற்றுப் ஃபேஷன் டிரெண்டை வெளிப்படுத்துவதோடு மட்டுமல்லாமல், இந்திய சினிமாவின் பொற்காலத்தையும் குறிக்கிறது, 
அங்கு நடிகர்கள் பெரும்பாலும் கடவுள்களாக போற்றப்பட்டனர் மற்றும் திரையில் அவர்களின் இருப்பு கலாச்சார விவரிப்புகளை வடிவமைத்தது.
 தமிழ்நாட்டின் சூழலில், கணேசன் ஒரு 'நடிகர் திலகம்' ஆவார், அவருடைய வெளிப்படையான நடிப்பு பாணி எதிர்கால தலைமுறை
 நடிகர்களை கணிசமாக பாதித்தது மற்றும் சினிமா நடிப்பிற்கான அளவுகோல்களை அமைத்தது. ஒரு சாதாரண ஸ்டுடியோ ஓவியத்தில் கூட, அவருடைய படம் பரவலாகப் 
பரப்பப்பட்டது மற்றும் போற்றப்பட்டது, அவரை அக்காலத்திய பிரபலமான ஊடகங்களில் ஒரு முக்கிய நபராக மாற்றியது. செபியா 
தொனி, இந்தியாவில் வெகுஜன பொழுதுபோக்கு மற்றும் கலாச்சார பிரதிபலிப்பின் முதன்மை ஆதாரமாக சினிமா இருந்த ஒரு காலகட்டத்திற்கான ஏக்கத்தை 
மேலும் தூண்டுகிறது, அவரை நாட்டின் ஊடக நிலப்பரப்பில் ஒரு காலமற்ற சின்னமாக மாற்றுகிறது.
Adversarial
இந்த நடிகர் எந்த வகையான கிளாசிக்கல் ஒடிசி 
நடன அசைவை வெளிப்படுத்துகிறார்?
Adversarial A
ஒரு துணிச்சலான தோரணையை ஏற்றுக்கொண்டுள்ள, தமிழ்நாட்டைச் 
சேர்ந்த புகழ்பெற்ற இந்திய நடிகரான சிவாஜி கணேசனின் ஸ்டுடியோ
 உருவப்படம் படத்தில் காட்டப்பட்டுள்ளது. அவர் ஒடிசி நடன போஸில் இல்லை.
MCQ
இந்தியாவில் ஜோதிடம் அல்லது பாரம்பரிய மோதிரங்கள் 
பொதுவாக அணியப்படும் வலது கையின் எந்த விரலில் 
நடிகர் மோதிரம் அணிந்திருக்கிறார்?
 Choices:
 A. சுட்டு விரல்
 B. நடுத்தர விரல்
 C. மோதிர விரல்
 D. சுண்டு விரல்
C
Figure 16: Example from IndicVisionBench-VQA. shown in Tamil
Short Q2
ਮੁਰਗੀ ਦਾ ਰੰਗ ਭਾਰਤੀ ਪਕਵਾਨਾਂ ਵਿੱਚ ਇਸਦੀ ਆਮ ਤਿਆਰੀ 
ਸ਼ੈਲੀ ਨੂੰ ਕਿਵੇਂ ਦਰਸਾਉਂਦਾ ਹੈ?
Short Q1
ਚਿੱਤਰ ਵਿੱਚ ਚਿਕਨ ਨੂੰ ਜਿਸ ਤਰੀਕੇ ਨਾਲ ਪੇਸ਼ ਕੀਤਾ ਗਿਆ
ਹੈ, 
ਉਸ ਤੋਂ ਖਾਣਾ ਪਕਾਉਣ ਦਾ ਮੁੱਖ ਤਰੀਕਾ ਕੀ ਸੁਝਾਇਆ ਗਿਆ
ਹੈ?
Short A2
ਮੁਰਗੇ ਦਾ ਲਾਲ-ਸੰਤਰੀ ਰੰਗ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਇਸ ਨੂੰ ਮਸਾਲਿਆਂ 
ਅਤੇ ਦਹੀਂ ਨਾਲ ਮੈਰੀਨੇਟ ਕੀਤਾ ਗਿਆ ਹੈ, ਜੋ ਕਿ ਭਾਰਤੀ ਪਕਵਾਨਾਂ ਵਿੱਚ 
ਤੰਦੂਰੀ ਚਿਕਨ ਲਈ ਇੱਕ ਆਮ ਤਿਆਰੀ ਹੈ।
Short A1
ਚਿਕਨ ਇੱਕ ਸੀਖ ਉੱਤੇ ਟੰਗਿਆ ਹੋਇਆ ਹੈ, ਅਤੇ ਧੂੰਏਂ ਵਾਲਾ ਪਿਛੋਕੜ ਦੱਸਦਾ ਹੈ ਕਿ 
ਇਸਨੂੰ ਗਰਿੱਲ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ ਜਾਂ ਤੰਦੂਰ, ਇੱਕ ਰਵਾਇਤੀ ਭਾਰਤੀ ਮਿੱਟੀ ਦੇ ਓਵਨ 
ਵਿੱਚ ਪਕਾਇਆ ਜਾ ਰਿਹਾ ਹੈ।.
True/False
ਪਿਛੋਕੜ ਵਿੱਚ ਧੁੰਦਲਾ ਵਿਅਕਤੀ ਇੱਕ ਰਵਾਇਤੀ 
ਭਾਰਤੀ ਸ਼ੈੱਫ ਦੀ ਵਰਦੀ ਪਹਿਨਿਆ ਹੋਇਆ ਹੈ,
 ਜੋ ਕਿ ਵਿਲੱਖਣ ਸਿਰ ਦੇ ਪਹਿਰਾਵੇ ਦੁਆਰਾ ਪਛਾਣਨਯੋਗ ਹੈ।  
ਗਲਤ
Long Q
ਚਿਕਨ ਨੂੰ ਗਰਿੱਲ ਕੀਤੇ ਜਾਣ ਦੇ ਦ੍ਰਿਸ਼ਟੀਗਤ ਸਬੂਤ ਤੋਂ ਇਲਾਵਾ, ਡਿਸ਼ 
ਦੀ ਦਿੱਖ ਅਤੇ ਪ੍ਰਦਾਨ ਕੀਤੀ ਗਈ ਜਾਣਕਾਰੀ ਦੁਆਰਾ ਕਿਹੜੇ 
ਸੱਭਿਆਚਾਰਕ ਤੱਤ ਜਾਂ ਖੇਤਰੀ ਸਬੰਧਾਂ ਦਾ ਸੁਝਾਅ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ, ਅਤੇ 
ਇਹ ਤੱਤ ਭਾਰਤ ਵਿੱਚ ਅਜਿਹੇ ਭੋਜਨ ਦੀ ਪ੍ਰਸਿੱਧੀ ਵਿੱਚ ਕਿਵੇਂ ਯੋਗਦਾਨ ਪਾਉਂਦੇ ਹਨ?
Long A
ਇਸ ਦਾ ਲਾਲੀ-ਨਾਰੰਗੀ ਰੰਗ ਅਤੇ ‘ਤੰਦੂਰੀ ਚਿਕਨ’ ਨਾਮ ਸੁਣਾਉਣ ਸਾਰ ਹੀ ਇਸ ਪਕਵਾਨ ਨੂੰ ਉੱਤਰੀ ਭਾਰਤੀ, ਖਾਸ ਕਰਕੇ ਪੰਜਾਬੀ, ਪਕਵਾਨਾਂ ਨਾਲ ਜੋੜ ਦਿੰਦਾ ਹੈ, ਜਿੱਥੇ ਤੰਦੂਰ ਮਿੱਟੀ ਦੇ ਓਵਨ ਦੀ ਬਹੁਤ ਜ਼ਿਆਦਾ 
ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਹ ਤਰੀਕਾ ਇਸ ਨੂੰ ਇੱਕ ਧੂੰਏਂ ਵਾਲਾ ਸੁਆਦ ਅਤੇ ਨਰਮ ਬਣਾਵਟ ਦਿੰਦਾ ਹੈ ਜੋ ਬਹੁਤ ਪਸੰਦ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਦਿਖਾਈ ਦੇਣ ਵਾਲੀ ਸੀਖ ਰਵਾਇਤੀ ਖਾਣਾ ਪਕਾਉਣ ਨੂੰ ਦਰਸਾਉਂਦੀ 
ਹੈ, ਅਤੇ ‘ਪੰਜਾਬ’ ਦਾ ਹਵਾਲਾ ਇਸ ਨੂੰ ਖੇਤਰੀ ਤੌਰ ’ਤੇ ਪ੍ਰਸਿੱਧ ਕਰਦਾ ਹੈ, ਜੋ ਇੱਕ ਸੁਆਦੀ ਨਾਨ-ਵੈਜੀਟੇਰੀਅਨ ਪਕਵਾਨ ਦੇ ਰੂਪ ਵਿੱਚ ਇਸਦੀ ਵਿਆਪਕ ਪ੍ਰਸਿੱਧੀ ਨੂੰ ਉਜਾਗਰ ਕਰਦਾ 
ਹੈ ਜੋ ਅਕਸਰ ਭਾਰਤ ਭਰ ਦੇ ਢਾਬਿਆਂ ਅਤੇ ਰੈਸਟੋਰੈਂਟਾਂ ਵਿੱਚ ਪਰੋਸਿਆ ਜਾਂਦਾ ਹੈ, ਜੋ ਇਸਦੀਆਂ ਸ਼ਾਾਨਦਾਰ ਸੁਆਦਾਂ ਅਤੇ ਵਿਲੱਖਣ ਖਾਣਾ ਪਕਾਉਣ ਦੀ ਤਕਨੀਕ ਲਈ ਪ੍ਰਸ਼ੰਸਾ ਕੀਤੀ ਜਾਂਦੀ ਇੱਕ ਅਮੀਰ 
ਪਕਵਾਨ ਪਰੰਪਰਾ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ।
Adversarial
ਇਹ ਚਿਕਨ ਟਿੱਕਾ ਆਮ ਤੌਰ 'ਤੇ ਹੈਦਰਾਬਾਦੀ ਰੈਸਟੋਰੈਂਟ ਵਿੱਚ ਕਿਵੇਂ ਪਰੋਸਿਆ ਜਾਂਦਾ
ਹੈ?
Adversarial A
ਤਸਵੀਰ ਵਿੱਚ ਤੰਦੂਰੀ ਚਿਕਨ ਦਿਖਾਈ ਦੇ ਰਿਹਾ ਹੈ, ਨਾ ਕਿ ਚਿਕਨ ਟਿੱਕਾ। ਤੰਦੂਰੀ ਚਿਕਨ ਵਿੱਚ ਸਾਬਤ ਜਾਂ ਅੱਧਾ ਚਿਕਨ (ਮੁਰਗਾ) 
ਸ਼ਾਾਮਲ ਹੁੰਦਾ ਹੈ ਜਿਸਨੂੰ ਮੈਰੀਨੇਟ ਕਰਕੇ ਤੰਦੂਰ ਵਿੱਚ ਪਕਾਇਆ ਜਾਂਦਾ ਹੈ, 
ਜਦੋਂ ਕਿ ਚਿਕਨ ਟਿੱਕਾ ਮੁਰਗੇ ਦੇ ਬੋਨਲੈੱਸ ਟੁਕੜਿਆਂ ਨੂੰ ਕਿਹਾ ਜਾਂਦਾ ਹੈ। ਇਹ ਪਕਵਾਨ ਪੰਜਾਬ ਖੇਤਰ ਤੋਂ ਉਤਪੰਨ ਹੋਇਆ ਹੈ, ਨਾ ਕਿ ਖਾਸ ਤੌਰ 'ਤੇ ਹੈਦਰਾਬਾਦ ਤੋਂ।
MCQ
ਦਿੱਤੇ ਗਏ ਵਿਜ਼ੂਅਲ ਸੰਕੇਤਾਂ ਦੇ ਆਧਾਰ 'ਤੇ, ਇਸ ਪਕਵਾਨ ਲਈ ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ ਸੰਭਾਵਿਤ
 ਰਵਾਇਤੀ ਭਾਰਤੀ ਖਾਣਾ ਪਕਾਉਣ ਵਾਲਾ ਉਪਕਰਣ ਕੀ ਹੈ?
 Choices:
 A. ਇੱਕ ਤੰਦੂਰ (ਮਿੱਟੀ ਦਾ ਓਵਨ)
 B. ਇੱਕ ਪ੍ਰੈਸ਼ਰ ਕੂਕਰ
 C. ਇੱਕ ਡੀਪ ਫਰਾਇਰ
 D. ਇੱਕ ਇੰਡਕਸ਼ਨ ਕੁੱਕਟੌਪ
A
Figure 17: Example from IndicVisionBench-VQA. shown in Punjabi
Short Q2
চলচ্চিত্র নির্মাণ ছাড়াাও সত্যজিৎ রায় আর কী কী
অবদান রেখেছিলেন?
Short Q1
সত্যজিৎ রায়ের কাজ বিশ্ব চলচ্চিত্রকে কীভাবে প্রভাবিত করেছিল?
Short A2
একজন কিংংবদন্তি পরিচালক হওয়াার পাশাপাশি, তিনি একজন লেখক, চিত্রকর এবং সঙ্গীত পরিচালকও 
ছিলেন, বিশেষত তিনি ফেলুদা নামে একটি জনপ্রিয় বাংলা গোয়েন্দাা চরিত্র তৈরি করেন এবং তাঁর বহু
 চলচ্চিত্রের জন্য সঙ্গীত রচনা করেন।
Short A1
সত্যজিৎ রায়ের পরিচালিত পথের পাঁচালীর মতো চলচ্চিত্রগুলোতে তাঁর মানবতাবাদী গল্প বলার ধরণ, 
বাস্তবধর্মী চিত্রায়ণ এবং গভীর সাংস্কৃৃতিক প্রেক্ষাপট আন্তর্জাাতিক প্রশংসা অর্জন করেছে এবং আকিরা 
কুরোসাওয়াা ও মার্টিন স্কোরসেসের মতো বিশ্বজুড়ে চলচ্চিত্র নির্মাতাদের অনুপ্রাণিত করেছে।
True/False
সত্যজিৎ রায় চলচ্চিত্রে তাঁর অসামান্য অবদানের জন্য একটি 
সম্মাানসূচক অস্কাার লাভ করেন।   
ঠিক
Long Q
সত্যজিৎ রায়ের চলচ্চিত্র নির্মাণ কীভাবে ভারতের সামাজিক ও সাংস্কৃৃতিক বাস্তবতা 
প্রতিফলিত করেছিল এবং বিশ্ব চলচ্চিত্রের ইতিহাসে তাঁর কাজ কেন গুরুত্বপূর্ণ বলে
বিবেচিত হয়?
Long A
সত্যজিৎ রায়ের চলচ্চিত্র ভারতের সামাজিক ও সাংস্কৃৃতিক বাস্তবতাকে তুলে ধরেছিল। তিনি সাধারণ মানুষের দৈনন্দিন জীবন, সংগ্রাাম এবং অনুভূতিগুলোকে সততা ও সংবেদনশীলতার সঙ্গে ফুটিয়ে তুলতেন।
তাঁর কাজগুলো, বিশেষত 'অপু ট্রিলজি', দারিদ্র্য, পরিবার, ঐতিহ্য এবং পরিবর্তনের মতো বিষয়গুলো নিয়ে তৈরি, যেখানে কোনো রকম বাড়িয়ে বলা বা রোমান্টিকতার আশ্রয় নেওয়া হয়নি তাঁর 
মিনিমালিস্ট স্টাইল, খুঁটিনাটির দিকে নজর রাখা এবং অপেশাদার অভিনেতাদের ব্যবহার ভারতীয় সিনেমায় এক ধরনের নীরব বাস্তবতা নিয়ে এসেছিল, যা সেই সময়ে বিরল ছিল। তাঁর চলচ্চিত্রগুলো পরিচয়, আধুনিকতা 
এবং মানুষের টিকে থাকার ক্ষমতা নিয়েও গভীর প্রশ্ন তুলে ধরেছিল। এই কারণেই তাঁর কাজগুলো একদিকে যেমন স্থাানীয় সংস্কৃৃতির প্রতি বিশ্বস্ত ছিল, তেমনি অন্যদিকে আন্তর্জাাতিক দর্শকদের কাছেও সমানভাবে প্রাসঙ্গিক 
ছিল। সাংস্কৃৃতিক স্বকীয়তা এবং আন্তর্জাাতিক আবেদন—এই দুইয়ের অনন্য মিশ্রণের জন্যই সত্যজিৎ রায়ের কাজ বিশ্ব চলচ্চিত্রে একটি মাইলফলক হিসেবে বিবেচিত হয়।
Adversarial
তামিলনাড়ুুর কোন সাহিত্য পুরস্কাার জেতার জন্য সত্যজিৎ রায় পরিচিত ছিলেন?
Adversarial A
সত্যজিৎ রায় পশ্চিমবঙ্গের একজন প্রভাবশালী ভারতীয় চলচ্চিত্র নির্মাতা এবং লেখক ছিলেন, তামিলনাড়ুুর নয়। তিনি তাঁর কাজের জন্য দাদাসাহেব ফালকে পুরস্কাার এবং ভারতরত্ন (ভারতের সর্বোচ্চ সম্মাান) সহ
 অসংখ্য জাতীয় ও আন্তর্জাাতিক পুরস্কাার পেয়েছেন।
MCQ
নিম্নলিখিতগুলির মধ্যে, সত্যজিৎ রায়ের অপু ট্রিলজিতে বর্ণিত বিষয়বস্তুগুলির মধ্যে কোনটিকে সব চেয়ে 
বেশি প্রতিফলিত করে?
 Choices:
 A. ফ্যাান্টাাসি এবং পৌরাণিক অ্যাাডভেঞ্চাার
 B. নগরীয় ভোগবাদ এবং পুঁজিবাদ
 C. গ্রাামীণ কষ্ট, ব্যক্তিগত বৃদ্ধি এবং মানবিক অবস্থাা
 D. রাজনৈতিক ব্যঙ্গ এবং ঐতিহাসিক কল্পকাহিনী
C
Figure 18: Example from IndicVisionBench-VQA. shown in Bengali
29

--- Page 30 ---\n\nShort Q2
किल्ल्‍याच्याा भिंतीपलीकडे आणि बोटींच्याा
पलीकडे, जमीन पाण्यााशी जोडण्याासाठी
वापरण्याात येणारी, कमानदार रचना असलेली
पारंपरिक किनारी वास्तू ओळखा.
Short Q1
खाडीमध्ये पर्यटकांसाठी स्थानिक वाहतुकीचे
किंंवा गतिविधीचे कोणते सामान्य साधन हिरव्या
छतखुणांवरून ओळखता येते?
Short A2
कमानीदार मोकळ्याा जागा असलेला एक काँक्रीीटचा धक्काा पाण्याात दूरवर
पसरलेला आहे आणि तो एका दूरच्याा भूभागाला जोडलेला आहे, जे
ऐतिहासिक भारतीय किनारी भागांतील चढाई किंंवा किनारी संरक्षणासाठी
एक वैशिष्ट्यपूर्ण रचना आहे.
Short A1
हिरव्या छत असलेल्याा अनेक पर्यटन बोटी खाडीत उभ्याा आहेत, जे 
पर्यटकांसाठी बोटिंग किंंवा प्रेक्षणीय स्थळे पाहण्याासारख्याा सामान्य
 क्रियाकलापांची नोंद करतात.
True/False
प्रतिमेत दाखवलेली किल्ल्यााची भिंत आधुनिक बांधकाम आहे का, जी पारंपरिक भारतीय किल्ल्यााच्याा 
स्थापत्यशास्त्रााच्याा विरुद्ध आहे?
चूक
Long Q
कॅप्शन आणि दृश्यातील तपशीलांचा संदर्भ देत, या दृश्यातील कोणत्या बाबी 
‘अर्थव्यवस्थे’ च्याा श्रेणीत योगदान देतात, विशेषतः समृद्ध सांस्कृृतिक वारसा 
आणि पर्यटन यासाठी ओळखल्याा जाणाऱ्या भारतीय संदर्भात?
Long A
हे दृश्य पर्यटन आणि संबंधित क्रियाकलापांच्याा स्पष्ट चित्रणामुळे 'अर्थव्यवस्था' श्रेणीमध्ये योगदान देते. हिरव्या छत असलेल्याा अनेक पर्यटन नौकांची उपस्थिती सक्रिय सागरी पर्यटन दर्शवते, कदाचित आनंददायी प्रवासासाठी,
 किल्ल्यांांना भेट देण्याासाठी किंंवा स्थानिक वाहतुकीसाठी, ज्याामुळे नौका चालक आणि संबंधित सेवांसाठी थेट उत्पन्न मिळते. ऐतिहासिक दगडी किल्ल्यााची भिंत स्वतःच एक वारसा आकर्षण आहे, जे अभ्याागतांना आकर्षित करते
 आणि निवास, भोजन आणि स्मृतिचिन्हांांच्याा खरेदीवर खर्च करून स्थानिक अर्थव्यवस्थेला अप्रत्यक्षपणे चालना देते. वाळूच्याा किनाऱ्यावर विखुरलेले लोक आणि नौका पर्यटकांची उपस्थिती आणि स्थानिक वातावरणाशी त्यांचा 
सहभाग आणखी स्पष्ट करतात, ज्याामुळे महाराष्ट्राातील एक पर्यटन स्थळ म्हणून प्रसिद्ध असलेल्याा ‘मालवण’ या विशिष्ट किनारपट्टीीच्याा प्रदेशाच्याा विश्रााम आणि शोध यावर केंद्रित आर्थिक क्रियाकलाप दिसून येतात.
Adversarial
या गजबजलेल्याा मासेमारी बंदरामुळे स्थानिक अर्थव्यवस्थेत लक्षणीय आणि पारंपारिक योगदान 
कसे दिले जाते, विशेषतः या प्रदेशासाठी माशांच्याा निर्यातीचे महत्त्व कसे अधोरेखित होते?
Adversarial A
हे चित्र पाण्यााजवळून बोटी आणि किल्लाा दर्शवते, ज्याामुळे सागरी क्रियाकलाप सूचित होतात, परंतु ते विशेषतः गजबजलेले 
मासेमारी बंदर किंंवा माशांची निर्यात ही प्राथमिक आर्थिक देणगी आहे असे दर्शवत नाही. बोटी हिरव्या छत असलेल्याा पर्यटन
 बोटी असल्यााचे दिसते, मासेमारीच्याा नौका नाहीत, हे सूचित करते की स्थानिक अर्थव्यवस्थेला ऐतिहासिक 
किल्लाा आणि किनारपट्टीीच्याा सौंदर्याशी संबंधित पर्यटन आणि मनोरंजक क्रियाकलापांमुळे जास्त फायदा होतो.
MCQ
भारतातील ऐतिहासिक सागरी किल्ल्यांांमध्ये सामान्यतः वापरल्याा 
जाणाऱ्या कोणत्या प्रकारच्याा सामग्रीीने किल्ल्यााची भिंत बांधलेली आहे?
 Choices:
 A. लाल वालुकाश्म आणि संगमरवर
 B. गुळगुळीत, एकसमान काँक्रीीट ब्लॉॉक्स
 C. मोठे, अनियमित राखाडी आणि तपकिरी दगड
 D. लाकडी खांब आणि मातीच्याा विटा
C
Figure 19: Example from IndicVisionBench-VQA. shown in Marathi
Bengali
Hindi
প্রথম অঙ্ক
৯
ও আমার বৃদ্ধ মাতার জন্য দুইটি conductor order দি, কিন্তু, 
যাহাদের বিজ্ঞাানের চর্চ্চাা বা উন্নতি করবার কিঞ্চিৎ মাত্রও ইচ্ছাা বা উ
পায় নাই তাদের জীবন দুরারোহ পর্ব্বতের ন্যাায় থাকা না থাকা দুই স
মান।
গৌরহরি। ছিঃঃ মাখন! বাব ও সকল ত্যাাগ কর, তোমার ও রকম ব্যব
হার দেখ্‌লে লোকে তোমায় পাগল বলবে। আর আমায়—
মাখন। Hush! আপনি আমার বয়োজ্যেষ্ঠ ও পিতা, তাই আপনার 
ন্যাায় বিজ্ঞাান-অন্ধ লোকের সহিত আমি এখনও কথা কহিতেছি। 
প্রাচীন ইতিহাসের একটা ছায়াা মাত্র আজ আপনার নিকট উন্মুক্ত করি 
শুনুন—যে ইংরাজজাতী সামান্য Telegraphএর প্রথম প্রচলনের সময় 
তারে জুতা বাঁধিয়াা বিদেস্থ পুত্রকে পাঠাইয়াাছি ভাবিয়াা স্থির হইত, 
বিজ্ঞাানের চর্চ্চাা করে, সেই ইংরাজ আজি সু-দূর হিমালয় হ’তে 
কুমারিকা পর্য্যন্ত ইঙ্গিতে শাসন কর্চ্চে। আর আমরা যে Nasty nation 
তাইই রহিলাম, not a whit superior, সেই বিজ্ঞাানে M. A. পাশ দিয়ে, 
আমি কি Dumb inert, as Egyptian mummy হয়ে থাক্‌ব। আপনি 
দেখবেন আমি by sheer science আপনার হিমালয়কে গরম করব, 
তাকে মানুষের ন্যাায় কথা কওয়াাব, ocean কে Shahara তে পরিণত ক
র্‌ব।
শীতল। মাখন বাবু! এ বড় আশ্চর্য্যের বিষয়। এ যদি
निवेदन
इस पुस्तक में मेरी अन्तर्यात्राा में पड़नेवाले कुछ प्रदेश हैं। यात्राा के लिए निक
लती रही है बुद्धि, पर हृदय को भी साथ लेकर। अपना रास्ता निकालती हुई 
बुद्धि जहाँ कहीं मार्मिक या भावाकर्षक स्थलों पर पहुँचती है वहाँ हृदय थोड़ाा-
बहुत रमता और अपनी प्रवृत्ति के अनुसार कुछ कहता गया है। इस प्रकार 
यात्राा के श्रम का परिहार होता रहा है। बुद्धिपथ पर हृदय भी अपने लिए कुछ 
न कुछ पाता रहा है।
बस, इतना ही निवेदन करके इस बात का निर्णय मैं विज्ञ पाठकों पर ही 
छोड़ता हूँ कि ये निबन्ध विषय-प्रधान है या व्यक्ति प्रधान।
काशी
}
रामचंद्र शुक्ल
२-२-१९१९
தேர் கொடுத்தவர்
முத்து, பவளம், மணி இழைத்த
தேரைப் பாரடி-அதில்
மிடுக்கு டனே செல்லும் அந்த
மனிதர் யாரடி?
எத்தி சையும் புகழ் மணக்கும்
பாரி தானடி-அவர்
இல்லை யென்றே சொல்லி டாத
வள்ள லாமடி.
சாலை ஓரம் அந்தத் தேரும்
நிற்ப தேனடி?-அங்கே
சட்டென் றவரும் கீழிறங்கிப்
பார்ப்ப தென்னடி?
மாலைக் காற்றில் ஆடி அசையும்
முல்லைக் கொடியடி- அதை
வழியில் கண்டே வேகமாக
இறங்கி னாரடி.
உற்றே அந்தக் கொடியை அவரும்
பார்ப்ப தேனடி?-அவர்
உள்ளம் நொந்து முகமும் வாடி
நிற்ப தேனடி?
115
వానాకాలపు పల్లీజీవితము.
శ్రావణనీలమేఘముల చల్లనినీడలఁ బెంంపు నొంంది, క్రొంం
దావుల: జల్లుచుంం బొలముదాపునఁ బూచెను గేతకంబు; లే
తావులనైన యౌవనముఁ దాల్చె వసుంంధర పైరుపచ్చలన్ ;
ఆవులు కండపెట్టెఁఁ దనివారఁగఁ బచ్చిక మేసి బీరులన్ .
కాఱుమెయిళ్ళపైన హరికార్ముక రేఖలు స్వర్గపట్టణ
ద్వారపుఁ దోరణంబు సరిదాఁక, బలాకలు మాలగట్టి యా
దారినె సంచరింప, నిశితత్వముఁ బాసిన సూర్యరశ్మి లేఁ
బైరుల సేవఁజేయఁ గనుపండువుఁ గొల్చు దినంబు లియ్యెడన్.
ప్రకృతి లీలావిలాస కావ్యంంబునందు
రసవదధ్యాయమేమొ వర్షంంపు ఋతువు!
కానిచోఁఁ దదధ్యేతలౌ కర్షకులకు
నెటులఁ బరనిర్వృృతిం గూర్చి యింపెలర్చు ?
పనిపాటుల్ ముగిసెంం గదా,యిఁకను లేఁబ్రాాయంపు టిల్లాలితో
దనపైఁ బ్రక్కలఁ ద్రొక్కిమూఁఁగు పసిసంతానంబుతో వర్షపున్
దినముల్ తిన్నగఁ బుచ్చవచ్చునను నుద్దేశమ్మునం గాఁఁపు గ
న్గొనుచుంండుం దన పైరుచేల శ్రమకున్ జోడైన సంతృప్తితోఁ .
Tamil
Telugu
Figure 20: Examples of IndicVisionBench-OCR. We show corresponding documents and the
Ground Truth (GT) texts in Bengali, Hindi, Tamil and Telugu.
30

--- Page 31 ---\n\nগোঁঁফ ও দাড়িওয়াালা একজন পুরুষ কৃষক, একটি কমলা
রঙের ফুলহাতা শার্ট, ধূসর প্যাান্ট এবং একটি লাল ও সাদা
চেকের পাগড়ি পরা অবস্থাায় একটি বিশাল সোনালী গমের
ক্ষেতে পরিষ্কাার আকাশের নিচে বসে আছেন। তিনি তার
হাতে একটি রূপালী কাস্তে ধরে আছেন, যা তার হাঁটুর উপর
রাখা আছে এবং সরাসরি ক্যাামেরার দিকে তাকিয়ে আছেন।
তার পাশে মাটিতে কাটা গমের আঁটি দেখা যাচ্ছে এবং
পটভূমিতে আরও গমের শীষ আছে। ফ্রেমের বাম দিকে
অন্য একজন ব্যক্তির লাল শার্ট আংশিকভাবে দৃশ্যমান।
மீசையும் தாடியும் கொண்ட ஒரு ஆண் விவசாயி,
ஆரஞ்சு நிற முழுக்கை சட்டை, சாம்பல் நிற கால்சட்டை
மற்றும் சிவப்பு வெள்ளை நிற கட்டம்போட்ட
தலைப்பாகை அணிந்து, தெளிவான வானத்தின் கீழ்
ஒரு பெரிய பொன்னிற கோதுமை வயலில் குதிகாலிட்டு
அமர்ந்திருக்கிறார். அவர், தனது கைகளில் ஒரு வெள்ளி
நிற அரிவாளை வைத்திருக்கிறார். அது அவரது
முழங்கால்களின் மேல் வைக்கப்பட்டிருக்கிறது. மேலும்,
அவர் நேரடியாக கேமராவைப் பார்க்கிறார்.
வெட்டப்பட்ட கோதுமை தண்டுகளின் கட்டுகள்
அவருக்கு அடுத்த தரையில் காணப்படுகின்றன,
மேலும், பின்னணியில் விளைந்து நிற்கும் கோதுமை
பயிர்கள் நிரம்பியுள்ளன. சட்டகத்தின் இடது பக்கத்தில்
மற்றொரு நபரின் சிவப்பு சட்டை ஓரளவு தெரிகிறது.
एक मूंछ और दाढ़ीी वाला पुरुष किसान, नारंगी रंग की पूरी
आस्तीीन वाली कमीज, ग्रे पैंट और लाल और सफेद चेक वाली
पगड़ीी पहने, साफ आसमान के नीचे एक बड़े सुनहरे गेहूं के खेत
में बैठा है। उसके हाथों में एक चांदी की हंसिया है, जो उसके
घुटनों पर टिकी हुई है, और वह सीधे कैमरे की ओर देख रहा है।
उसके बगल में जमीन पर कटे हुए गेहूं के डंठलों के बंडल दिखाई
दे रहे हैं, और पृष्ठभूमि में और भी खड़े गेहूं के डंठल भरे हुए हैं।
फ्रेेम के बाईं ओर एक अन्य व्यक्ति की लाल कमीज आंशिक रूप
से दिखाई दे रही है।
A male farmer, with a mustache and beard, wearing
an orange full-sleeved shirt, grey pants, and a red and
white checkered turban, squats in a large golden
wheat field under a clear sky. He holds a silver sickle
in his hands, which are resting on his knees, and
looks directly at the camera. Bundles of cut wheat
stalks are visible on the ground next to him, with
more standing wheat stalks filling the background.
Another person's red shirt is partially visible on the
left side of the frame.
മീശയും താടിയുമുള്ള ഒരു പുരുഷ
കർഷകൻ ഓറഞ്ച് നിറത്തിലുള്ള ഫുൾ
സ്ലീീവ് ഷർട്ടുംും ചാരനിറത്തിലുള്ള പാന്റ്സും
ചുവപ്പുംും വെളുപ്പുംും കലർന്ന കള്ളി തലക്കെട്ട്
ധരിച്ച് തെളിഞ്ഞ ആകാശത്തിന് കീഴെ
സ്വർണ്ണനിറമുള്ള വലിയ ഗോതമ്പ് പാടത്ത്
കുത്തിയിരിക്കുുന്നു. അയാൾ തന്റെ
കാൽമുട്ടിിൽ വെച്ചിരിക്കുുന്ന കൈകളിൽ
ഒരു വെള്ളി അരിവാൾ പിടിച്ച്
ക്യാാമറയിലേക്ക് നോക്കുുന്നു. മുറിച്ച
ഗോതമ്പ് കറ്റകൾക്ക് സമീപത്ത് കാണാം.
കൂടുതൽ ഗോതമ്പ് കറ്റകൾ
പശ്ചാാത്തലത്തിൽ നിറഞ്ഞുനിൽക്കുുന്നു.
ഫ്രെയിമിന്റെ ഇടതുവശത്ത് മറ്റൊരാളുടെ
ചുവന്ന ഷർട്ട് ഭാഗികമായി കാണാം.
మీసాలు, గడ్డంంతో, నారింజ రంగు ఫుల్ స్లీవ్స్ షర్ట్,
బూడిద రంగు ప్యాంంటు, ఎరుపు, తెలుపు గీతాలున్న
తలపాగా ధరించిన ఒక పురుష రైతు, స్పష్టమైన ఆకాశం
కింంద పెద్ద బంగారు గోధుమ పొలంలో కూర్చున్నాడు.
అతను తన చేతుల్లో ఇనుప కొడవలిని పట్టుకుని
ఉన్నాడు, అతని చేతులు మోకాళ్లపై ఆని ఉన్నాయి,
మరియు నేరుగా కెమెరా వైపు చూస్తున్నాడు. అతని
పక్కన నేలపై కోసిన గోధుమ కాడల కట్టలు
కనిపిస్తున్నాయి, నేపథ్యంంలో మరిన్ని గోధుమ మొక్కలు
ఉన్నాయి. ఫ్రేమ్ ఎడమ వైపున మరొక వ్యక్తి యొక్క
ఎరుపు చొక్కా పాక్షికంగా కనిపిస్తుంంది.
ନିଶ ଓ ଦାଢ଼ି ରଖିଥିବା ଜଣେ ପୁରୁଷ ଚାଷୀ, କମଳା ରଙ୍ଗର ଫୁଲ୍-ସ୍ଲିଭ୍
ସାର୍ଟ, ଧୂସର ପ୍ୟାାଣ୍ଟ ଏବଂ ଲାଲ୍ ଓ ଧଳା ଚେକ୍ଡ୍ ପଗଡ଼ି ପିନ୍ଧି ଏକ
ବିରାଟ ସୁନେଲି ଗହମ କ୍ଷେତରେ ସ୍ୱଚ୍ଛ ଆକାଶ ତଳେ ବସିଛନ୍ତି । ସେ
ତାଙ୍କ ହାତରେ ଏକ ଲୁହା ଦାଆ ଧରିଛନ୍ତି, ଯାହା ତାଙ୍କ ଆଣ୍ଠୁ ଉପରେ
ରଖାଯାଇଛି ଏବଂ ସିଧା କ୍ୟାାମେରାକୁ ଚାହିଁଛନ୍ତି । ତାଙ୍କ ପାଖରେ କଟା
ଯାଇଥିବା ଗହମ ନଡ଼ାାର ବିଡ଼ା ଦେଖାଯାଉଛି ଏବଂ ପୃଷ୍ଠଭୂମିରେ ଅଧିକ
ଠିଆ ହୋଇଥିବା ଗହମ ଗଛ ଭରି ରହିଛି । ଫ୍ରେମର ବାମ ପାର୍ଶ୍ୱରେ
ଅନ୍ୟ ଜଣେ ବ୍ୟକ୍ତିଙ୍କ ଲାଲ୍ ସାର୍ଟ ଆଂଶିକ ଭାବରେ ଦୃଶ୍ୟମାନ ହେଉଛି
।
ਮੁੱਛਾਂ ਅਤੇ ਦਾੜ੍ਹੀੀ ਵਾਲਾ ਇੱਕ ਪੁਰਸ਼ ਕਿਸਾਨ, ਜਿਸਨੇ ਸੰਤਰੀ ਰੰਗ ਦੀ
ਪੂਰੀ ਬਾਹਾਂ ਵਾਲੀ ਕਮੀਜ਼, ਸਲੇਟੀ ਪੈਂਟ ਅਤੇ ਲਾਲ ਤੇ ਚਿੱਟੇ ਰੰਗ ਦੀ
ਚੈੱਕਦਾਰ ਪੱਗ ਬੰਨ੍ਹੀੀ ਹੋਈ ਹੈ, ਇੱਕ ਵੱਡੇ ਸੁਨਹਿਰੀ ਕਣਕ ਦੇ ਖੇਤ ਵਿੱਚ
ਸਾਫ਼ ਅਸਮਾਨ ਹੇਠਾਂ ਬੈਠਾ ਹੈ। ਉਸਨੇ ਆਪਣੇ ਹੱਥਾਂ ਵਿੱਚ ਇੱਕ ਚਾਂਦੀ
ਰੰਗੀ ਦਾਤਰੀ ਫੜਿਆ ਹੋਇਆ ਹੈ, ਜੋ ਉਸਦੇ ਗੋਡਿਆਂ 'ਤੇ ਟਿਕੇ ਹੋਏ ਹਨ,
ਅਤੇ ਉਹ ਸਿੱਧਾ ਕੈਮਰੇ ਵੱਲ ਦੇਖ ਰਿਹਾ ਹੈ। ਉਸਦੇ ਕੋਲ ਜ਼ਮੀਨ 'ਤੇ
ਕਣਕ ਦੀ ਫ਼ਸਲ ਦੇ ਗੱਠੇ ਦਿਖਾਈ ਦੇ ਰਹੇ ਹਨ, ਜਦੋਂ ਕਿ ਪਿਛੋਕੜ ਵਿੱਚ
ਹੋਰ ਖੜੀ ਕਣਕ ਦੀ ਫ਼ਸਲ ਹੈ । ਫਰੇਮ ਦੇ ਖੱਬੇ ਪਾਸੇ ਇੱਕ ਹੋਰ ਵਿਅਕਤੀ
ਦੀ ਲਾਲ ਕਮੀਜ਼ ਅੰਸ਼ਕ ਤੌਰ 'ਤੇ ਦਿਖਾਈ ਦੇ ਰਹੀ ਹੈ।
Bengali
English
Malayalam
Tamil
Telugu
Hindi
Punjabi
Odia
Figure 21: IndicVisionBench-MMT benchmark sample image and corresponding translations in
8 languages.
31

--- Page 32 ---\n\nFigure 22: Image QA pairs’ correction tool. Interface of the QA pairs’ correction tool provided to
the human annotators.
32

--- Page 33 ---\n\nE
HUMAN ANNOTATIONS
Annotation guidelines for the IndicVisionBench Cultural QA Dataset
The task involves enriching image–caption pairs with culturally grounded question–answer
(QA) annotations. The focus is on determining whether an image depicts Indian culture and, if
so, generating diverse QA pairs that capture cultural specificity.
Scope
Annotators assess cultural relevance (e.g., attire, festivals, rituals, food, architecture) and
generate QA pairs to support training and evaluation of multimodal models.
Captions
Each image is provided with human-annotated keywords and an auto-generated caption.
Keywords are fixed; captions may be edited for accuracy. Both should be used as context when
forming QA pairs.
Annotation Process
• If an image does not depict Indian culture:
– Set depicts indian culture = False
– Set state specific culture = no
– Leave other fields unchanged.
• If an image does depict Indian culture:
– Update caption if necessary.
– Provide the following QA annotations:
* Short Answer QAs: Two concise cultural QA pairs.
* MCQ: One multiple-choice question with one correct option and three plausible
distractors (exact string match required between answer and option).
* True/False: One fact-based cultural question with answer True or False.
* Long Answer: One descriptive QA pair (4–6 lines).
State-Specific Culture
If the image reflects a specific Indian state, record the state name; otherwise enter no.
Adversarial Question
Each culturally relevant image requires one adversarial question designed to include a plausible
but incorrect cultural assumption.
• Dos: Specific, confident, culturally relevant, and misleading but realistic.
• Don’ts: Speculative (“Is this...?” ), vague, hedged, or trivial.
• Examples: Mistaking Aipan art for Bikaneri art, Pongal for Eid, etc.
Bad or Irrelevant Images
Low-quality, generic, or culturally irrelevant images are marked as:
• depicts indian culture = False
• state specific culture = no
Checklist
• Verify cultural relevance.
• Mark depicts indian culture and state specific culture appropriately.
• If relevant, complete all QA fields.
• Do not leave fields empty.
Note. Annotations must remain brief, factual, and faithful to Indian culture. Careful, consistent
labeling ensures the dataset’s reliability for benchmarking multimodal models.
33

--- Page 34 ---\n\nIndicVisionBench Image Collection Guidelines
The goal is to curate culturally relevant, open-license images across Indian states for the In-
dicVisionBench vision-language benchmark. Each state–category pair must contain at least 10
high-quality images that satisfy the following requirements:
1. Cultural Authenticity
Images should accurately reflect Indian cultural elements tied to the specified state.
2. Category Relevance
Each image must belong to one of the predefined categories (e.g., food, literature, festivals).
3. Geographic Specificity
Content should be clearly associated with a specific Indian state.
4. Open Licensing
Only images under Creative Commons licenses permitting commercial use are eligible.
Collection Process
1. Formulate search queries in the format: “<category>in <state>” (e.g., Music in Nagaland,
Traditional sports in Kerala).
2. Apply Creative Commons usage rights filters.
3. Manually inspect results for authenticity and verify license details.
4. Select as many images per category–state pair as possible, organize them into subfolders,
and record metadata (filename, source URL, category, license).
Exclusions
• Low-quality, blurry, watermarked, or stereotypical content.
• Images not clearly tied to culture or state.
• Content with unclear or invalid licensing.
Target Categories
Food, Lifestyle, Literature, Music & Dance, Religion, Customs, Festivals, Heritage, Economy,
Media & Entertainment, Architecture, Sports, Notable Figures.
Submission
Each state folder is expected to contain at least 100 images across categories, with a metadata
file. For states with limited available material, collect as many culturally relevant images as
possible. All submissions are uploaded to the shared repository.
34

--- Page 35 ---\n\nF
PROMPTS USED
Instructional Prompts for Each Question Category
Long Question:
{Question} Answer the question in detail in {target language} language.
Short Question:
{Question} Please provide brief, clear responses in {target language} language.
Adversarial:
{Question} Answer the question in detail in {target language}language.
Multiple Choice (MCQ):
Strict Instruction: Respond with only one choice in the format <A>, <B>, <C>, or <D>.
Do not include any explanation, reasoning, or extra text.
{Question} Your question here
Choices:
A. Option 1
B. Option 2
C. Option 3
D. Option 4
True/False:
Strict Instruction: Respond with only {lang true} or {lang false}.
{Question} Your question here
Choices: {lang true} or {lang false}
OCR:
Extract the exact text from this image using OCR. Respond with only the text.
Multimodal Translation:
{Question} Answer the question in detail in {target language} language.
We release all prompts used in our study. These include one prompt for generating four QA types
(Long, Short, MCQ, and True/False), and a separate dedicated prompt for adversarial QAs. We
design adversarial prompts independently because these questions are more challenging and require
detailed instructions. We also include prompts used for evaluation via the LLM-as-a-judge frame-
work, where responses are scored on a 0–10 scale. Furthermore, we provide the prompts we use for
each type of question during response generation from different models being evaluated.
Prompt for judging short answer questions via LLM-as-a-judge:
You are a judge evaluating how well a Vision-Language Model answers short-answer type
questions.
Evaluate the model’s response based on accuracy and correctness with respect to the Ground
Truth answer. Assign a high score when the model’s response matches closely with the ground
truth and a low score when the response lacks knowledge or is unrelated to the ground truth.
Question: {question}
Ground Truth: {ground truth}
Model response: {predicted answer}
Provide a single overall score from 0 to 10 based on the given criteria. Strictly return only the
numeric score, without any additional commentary.
35

--- Page 36 ---\n\nCategory classification prompt for crowdsourced images:
You are a cultural content classifier. Given the image and the caption, classify it into one or
more of the following **top-level categories**. Use the definitions to guide your classification,
but **only return one category name** (e.g., ”Food”, ”Lifestyle”) that the image can be best
classified into in your answer — no subcategories or descriptions.
• Food: Iconic regional cuisines and dishes
• Lifestyle: Traditional attire, daily routines, and modern practices
• Literature: Renowned works, authors, and poets
• Music and Dance: Classical, folk, and traditional performance arts
• Religion: Major faiths, rituals, and festivals
• Customs: Cultural etiquette and greeting practices
• Festivals: National and regional celebrations
• Heritage: Monuments, sites, and landmarks of historical importance
• Economy: Key industries and occupations
• Media: Popular entertainment figures, cinema, and television
• Architecture: Traditional Art and Architecture
• Sports: Indigenous games and traditional sports
• Notable Figures: Influential leaders and historical personalities
Take help from the detailed caption of this image in this task of categorization.
Caption:
{caption}
**Respond only with the name of the most relevant category from the list above i.e., Food,
Lifestyle, Literature, Music, Religion, Customs, Festivals, Heritage, Economy, Media, Archi-
tecture, Sports, Notable Figures**. **Do not give any other response and do not provide any
explanation or any unnecessary text**.
36

--- Page 37 ---\n\nQA pairs creation prompt:
Here is an India-specific image and the image filename, caption, and category of the image I
have on hand.
The image filename is this: {image filename}
The caption is this: {caption}
The category is this: {category}
I’d like you to generate two short questions and answers, one multiple-choice question and
answer, one true/false question and answer, and one long question and answer. Refer to the
image filename, category, and caption for context and hints. Take into account the cultural
diversity of the category that this image falls under with respect to India.
Follow these rules while designing questions and answers:
1. The question must be answerable only by looking at the image.
2. Ensure that the questions are culturally relevant to India and specific to the image.
3. Make the questions in such a way that someone who is not well aware of Indian culture will
find them difficult to answer.
4. Provide answers that are concise, accurate, and directly related to the question.
5. For MCQs, provide 1 correct option and 3 incorrect (but relevant) distractors.
6. For MCQs, the question must be answerable even without the choices.
Example of an invalid question: “What song is not performed by this musician” – not
answerable if you don’t know the choices.
7. Write all questions fluently in English.
8. Be mindful of cultural sensitivities and avoid stereotyping or misrepresentation.
9. Ensure variety: include identity questions (“What is this?”, “Where is this?”), reasoning,
referencing, and commonsense knowledge.
10. Generate only in English.
11. For short-answer questions, keep answers brief (1–2 sentences).
12. Make all questions distinct and unique.
Give the answers in the following JSON format and output only valid JSON:
{{
“short questions”: [ { “question”: <question>, ”answer”: <answer>} ],
“multiple choice questions”: [ { “question”: <question>, “answer”: <answer>, “options”:
[<option1>, <option2>, <option3>, <option4>] } ],
“true false question”: { “question”: <question>, “answer”: <answer>},
“long question”: { “question”: <question>, “answer”: <answer>}
}}
37

--- Page 38 ---\n\nAdversarial QA pairs creation prompt:
You are given an image from India along with its caption and the category it belongs to.
Your task is to create an adversarial question for the image — one that makes a confident but
subtly incorrect cultural assumption about what is shown, especially with respect to India’s di-
verse regional traditions, foods, festivals, clothing, rituals, and art forms.
Here is the image’s caption: {caption}
The category it belongs to is: {category}
Generate:
Adversarial Question: A misleading or culturally incorrect question that confidently makes a
specific, wrong assumption which is plausibly close to the truth (e.g., mixing up similar Indian
art styles, dishes, festivals, or traditions). The question must not reveal that it is making an
assumption — just ask the question normally, as if the incorrect assumption is true.
Avoid yes/no or speculative questions.
Examples:
– How was this Bikaneri folk painting prepared on canvas? (image shows Kumaoni Aipan)
– What are the main ingredients in this chicken tandoori dish? (image shows paneer tikka)
– Which Sikh gurdwara is being shown here? (image shows a Hindu temple)
– How is this Eid offering typically presented in Tamil Nadu? (image shows a Pongal celebra-
tion)
Non-examples:
– Is this a Bikaneri art piece?
– Are these Modaks made of coconut?
– Considering this is a South Indian Onam celebration...
The adversarial question should be close enough to the actual content that it forces a model to
distinguish finely between culturally similar options and reject the incorrect assumption. You
also need to generate the answer for the question that you generate.
Do not include introductions or explanations. Output only the following two fields in exactly
this format:
Adversarial Question: <your question here>
Answer: <your answer here>
38

--- Page 39 ---\n\nPrompt for judging adversarial questions via LLM-as-a-judge:
You are a judge evaluating how well a Vision-Language Model (VLM) answers adversarial
questions. In adversarial questions, the question contains a false assumption about the image.
You are given:
– Question: {question}
– Correct Answer (Gold reference): {ground truth}
– VLM Answer: {predicted answer}
Your task:
Evaluate the VLM’s answer according to this rubric:
1. Identifying the false assumption (0 or 5 points):
• Award 5 points if the VLM explicitly identifies that the question contains a wrong assump-
tion OR expresses uncertainty/difficulty in confirming the assumption.
• Award 0 points if the VLM ignores the wrong assumption and answers as if the question
were correct.
2. Identifying what the image is actually about (0–5 points):
• Award 0–5 points depending on how well the VLM correctly identifies the real content of
the image.
0 = completely wrong or no attempt.
1–2 = vague or partially correct.
3–4 = mostly correct but incomplete.
5 = fully correct identification.
Final Score = Assumption Score (0 or 5) + Identification Score (0–5) →0 to 10.
Instructions:
– Only output the final score as a number between 0 and 10.
– Do not explain reasoning or repeat answers.
– Always respond with the final score. Do not return a blank response.
– Be fair but consistent: partial credit is encouraged for partial identification.
Now, provide the score.
39
\n```\n