---
title: "2025-Nguyen-VietMEAgent Culturally-Aware Few-Shot Multimodal Explanation for - PDF Extract"
source_pdf: "2025-Nguyen-VietMEAgent Culturally-Aware Few-Shot Multimodal Explanation for.pdf"
pages: 7
extracted_at: "2026-02-15T17:54:27.707932"
---

# PDF Extract: 2025-Nguyen-VietMEAgent Culturally-Aware Few-Shot Multimodal Explanation for

**Source PDF:** 2025-Nguyen-VietMEAgent Culturally-Aware Few-Shot Multimodal Explanation for.pdf
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

VietMEAgent: Culturally-Aware Few-Shot Multimodal Explanation for
Vietnamese Visual Question Answering
Hai-Dang Nguyen1, Minh-Anh Dang2, Minh-Tan Le3, Minh-Tuan Le4
1 Faculty Of Information Technology, VNU University of Engineering and Technology, Hanoi, Vietnam
2 IT-BT Convergence Technology Division, Vietnam-Korea Institute of Science and Technology, Hanoi, Vietnam
3 TADI Global Lab, TADI Global Company Limited, Hanoi, Vietnam
4 Faculty of Finance, Banking Academy of Vietnam, Hanoi, Vietnam
ABSTRACT— Contemporary Visual Question Answering (VQA) systems remain constrained when confronted with culturally specific
content, largely because cultural knowledge is under-represented in training corpora and the reasoning process is not rendered
interpretable to end users. This paper introduces VietMEAgent, a multimodal explainable framework engineered for Vietnamese cultural
understanding. The method integrates a cultural object detection backbone with a structured program generation layer, yielding a
pipeline in which answer prediction and explanation are tightly coupled. A curated knowledge base of Vietnamese cultural entities
serves as an explicit source of background information, while a dual-modality explanation module combines attention-based visual
evidence with structured, human-readable textual rationales. We further construct a Vietnamese Cultural VQA dataset sourced from
public repositories and use it to demonstrate the practicality of programming-based methodologies for cultural AI. The resulting
system provides transparent explanations that disclose both the computational rationale and the underlying cultural context, supporting
education and cultural preservation with an emphasis on interpretability and cultural sensitivity.
Keywords— Visual Question Answering, Cultural AI, Explainable AI, Vietnamese Culture, Multimodal Learning.
I. INTRODUCTION
Visual Question Answering (VQA) is a central challenge in artificial intelligence that requires a system to jointly
process visual and linguistic information to answer questions grounded in images [2,3]. Despite steady advances, applying
VQA to culturally situated scenarios remains difficult. In the Vietnamese context, a model must not only recognize
objects, scenes, and relations, but also interpret their cultural meanings, historical connotations, ritual functions, and
regional variants. In practice, current systems are often culturally blind: they misrecognize symbols, conflate distinct
but visually similar artifacts, or fail to connect a visual cue to its cultural semantics. These issues are exacerbated by
a lack of interpretability: black-box predictions obscure the chain of reasoning and hinder verification or correction by
non-experts. Language further compounds the problem, as Vietnamese idioms, polysemy, and culturally bound expressions
are underrepresented in common benchmarks. Finally, the development of dedicated datasets for Vietnamese Cultural
VQA has lagged behind, limiting both modeling and evaluation.
Vietnamese culture spans interlinked domains—from cuisine (e.g., phở, bánh mì, bánh xèo) and architecture (e.g.,
temples, communal houses, colonial heritage) to attire (e.g., áo dài with regional and ceremonial variants), festivals
(e.g., Tết, Mid-Autumn, ancestor worship), and folk arts (e.g., traditional instruments, dances, and games). Modeling this
landscape requires mechanisms that connect perception with knowledge and that communicate inference in ways users
can scrutinize. Recent developments in explainable AI [7,18] and few-shot learning with large language models [6,13]
suggest new directions: visual program induction can decompose complex questions into verifiable sub-steps [8,20], while
open-world recognition expands the space of detectable concepts [16].
We therefore present VietMEAgent, a culturally aware, few-shot multimodal explanation framework. The contributions
are fourfold. First, we introduce a Vietnamese Cultural VQA dataset of 28,484 annotated samples spanning twelve
categories. Second, we propose a multimodal programming approach that couples cultural object detection with structured
program generation. Third, we integrate a curated knowledge base of Vietnamese cultural entities to ground both answers
and explanations. Fourth, we provide transparent explanations that integrate visual evidence with structured textual
reasoning, facilitating educational use and cultural preservation.
II. RELATED WORK
A. Textual Explanation Methodologies for VQA
Foundational research emphasized generating textual justifications to accompany answers in order to render the
model’s reasoning auditable [10,15,18]. Multi-task frameworks that jointly train on VQA and image captioning have been
explored [26], but the decoupling between captions and VQA supervision can yield explanations that are fluent yet not
question-specific. Later work attached answer-related captions to VQA instances [10] or retrieved auxiliary text to enrich
explanations [22]. While text-only rationales are accessible and compact, they often elide the visual grounding central to
VQA, thereby limiting faithfulness.
arXiv:2511.09058v1  [cs.CV]  12 Nov 2025

--- Page 2 ---

VietMEAgent: Culturally-Aware Few-Shot Multimodal Explanation for Vietnamese Visual Question Answering
2
Figure 1: VietMEAgent producing multimodal explanations that align visual evidence (e.g., attention heatmaps and
bounding boxes) with structured textual rationales. The example illustrates identification of HạLong Bay accompanied by
contextual cultural information.
B. Multimodal Explanation Frameworks for VQA
To more closely tie text to perception, multimodal approaches correlate visual attention with explanatory sentences
[18,23] or jointly optimize vision–language objectives to improve consistency [7,24,25]. For instance, [7] maps detected
regions into textual slots, though early systems were confined to limited object vocabularies and used rigid templates
that reduced readability. Variational formulations have been proposed to strengthen causal alignment between answers
and explanations [24]. Nevertheless, most methods presuppose large, domain-matched datasets—an assumption that is
costly in niche cultural settings. As multimodal LLMs (e.g., GPT-4V [1], Gemini-1.5 [19], Qwen-VL [4]) expand visual
reasoning capabilities, lightweight, knowledge-integrated strategies become attractive, especially where cultural precision
is paramount.
C. Few-Shot Explanation Methodologies for VQA
Large language models exhibit strong in-context learning, enabling few-shot rationalization from carefully chosen
exemplars [6,11,13,14]. Prior work has shown that prompting with image captions and question–answer exemplars can
elicit stepwise reasoning [13]. Yet, when cultural content is involved, generic exemplars underperform without explicit
domain knowledge. Our approach departs by combining few-shot program induction with a cultural knowledge base and a
detector tuned to Vietnamese cultural artifacts. In doing so, we aim to retain the flexibility of few-shot prompting while
supplying the precise entities and relations required for culturally faithful explanations.
III. METHODOLOGY
A. System Architecture
VietMEAgent follows a four-stage pipeline that links perception, reasoning, knowledge, and explanation. Given a
Vietnamese question and an image, the system first performs cultural object detection to localize salient entities and
produce region-level evidence. It then invokes a program generator that translates the natural-language question into an
executable, domain-specific program whose functions encode common cultural reasoning patterns. During execution, the
program queries a knowledge base to retrieve definitions, historical context, ceremonial significance, and regional variants
relevant to the detected entities. Finally, a multimodal explanation module synthesizes visual evidence and structured
textual reasoning into a coherent, human-readable account.

--- Page 3 ---

VietMEAgent: Culturally-Aware Few-Shot Multimodal Explanation for Vietnamese Visual Question Answering
3
Figure 2: Overall architecture. Cultural object detection feeds a program generator that compiles questions into executable
steps. Program execution integrates a Vietnamese cultural knowledge base, and an explanation module renders aligned
visual and textual rationales.
B. Cultural Object Detection Framework
The detector is built on YOLOv8 and fine-tuned on a culturally curated corpus covering twelve categories, including
cuisine, architecture, traditional clothing, and festivals. Training data were collected from Vietnamese cultural repositories
and heritage sources, with augmentation strategies that preserve culturally relevant color and texture while improving
robustness. The model outputs tuples of the form (label, confidence, box), for example (’bánh xèo’,
0.92, [x1,y1,x2,y2]), which provide both semantic labels and spatial evidence for subsequent reasoning and
explanation.
C. Program Generation and Execution
We employ Gemini 2.0 Pro alongside sixteen carefully designed few-shot exemplars to transform Vietnamese cultural
questions into structured programs. These programs consist of domain-specific functions such as identify_food,
describe_architecture, explain_cultural_significance, and compare_regional_variations.
The prompts are carefully crafted to reflect Vietnamese linguistic features, including idiomatic expressions and
pragmatic particles. They are designed to elicit disambiguation, especially in cases where cultural questions may have
multiple valid interpretations. During program execution, visual entities detected in the image are mapped to entries in the
cultural knowledge base using both semantic similarity and standardized Vietnamese naming conventions.
This matching mechanism allows the system to retrieve culturally rich information such as definitions, ceremonial
functions, preparation techniques, or historical significance. As a result, both the answer and the explanation are grounded
not only in the visual content but also in validated cultural knowledge.
D. Multimodal Explanation Generation
Explanations are produced by aligning visual and textual channels. On the visual side, attention maps and bounding
boxes mark regions most influential to the prediction, making the evidential basis explicit. On the textual side, explanations
follow a structured template that first identifies the object or scene, then situates it within Vietnamese cultural context,
and finally elaborates on regional variants, historical background, or ceremonial functions as appropriate. A lightweight
consistency checker verifies that referenced entities in text correspond to detected regions, and that claims are supported
by the knowledge base. The result is a concise yet transparent narrative that users can inspect and contest.

--- Page 4 ---

VietMEAgent: Culturally-Aware Few-Shot Multimodal Explanation for Vietnamese Visual Question Answering
4
IV. VIETNAMESE CULTURAL VQA DATASET
A. Construction and Coverage
We assemble a Vietnamese Cultural VQA dataset comprising 28,484 samples across twelve categories representative
of core cultural domains. Images are drawn from public sources such as official tourism portals, museum digitizations,
cultural heritage repositories, and educational platforms, with careful screening for authenticity and research-appropriate
use. Each image is annotated by experts in Vietnamese anthropology, history, or cultural studies. Annotations include
culturally correct Vietnamese labels, multiple questions spanning identification, comparison, description, and explanation,
and answers that incorporate essential cultural context. A second round of expert review ensures consistency and reduces
bias.
The coverage includes everyday and ceremonial cuisine, architectural heritage ranging from religious structures to
colonial-era buildings and traditional dwellings, attire encompassing áo dài and ethnic costumes, national and local
festivals, daily practices and crafts, folk sports and games, traditional transport, handicrafts and decorative arts, musical
instruments, and culturally significant landscapes. This breadth is intended to support both recognition and higher-order
reasoning within a unified benchmark.
Table 1: Dataset Composition by Cultural Category
Cultural Category
Sample Count
Percentage
Complexity Level
Cuisine
2,934
10.3%
Low
Architecture
2,991
10.5%
Medium
Traditional Clothing
2,478
8.7%
Low
Cultural Festivals
2,393
8.4%
Medium
Daily Life Practices
2,336
8.2%
High
Traditional Sports
2,307
8.1%
High
Transportation
2,279
8.0%
High
Handicrafts
2,250
7.9%
Very High
Miscellaneous Categories
12,516
43.9%
Mixed
Total
28,484
100.0%
B. Quality Assessment and Statistics
The dataset contains 28,484 high-resolution images paired with 91,149 questions, yielding an average of approximately
3.2 questions per image. Across the corpus, 156 unique cultural entities are catalogued with expert-validated descriptions
to anchor terminology and reduce ambiguity. Question length averages 12.3 words and answers average 15.7 words,
reflecting an emphasis on concise yet informative phrasing suited to educational settings. Inter-annotator agreement
reaches κ = 0.832, indicating substantial consistency in labeling and reasoning categories, and the overall cultural
accuracy approval rate in expert audits is 94.7%. For research use under appropriate licensing, the dataset is hosted at
https://huggingface.co/datasets/Dangindev/viet-cultural-vqa.
V. EXPERIMENTAL EVALUATION
A. Setup and Metrics
Experiments are conducted on NVIDIA V100 GPUs (32 GB) using PyTorch 1.12. We evaluate language quality with
BLEU-4 [17], complement it with METEOR [5] and ROUGE-L [12], and introduce two domain-oriented criteria: Cultural
Accuracy, which measures correctness against expert-validated cultural facts, and Explanation Quality, which assesses
the coherence and grounding of multimodal rationales. Baselines include BLIP-VQA [9], LXMERT [21], and a strong
large-model variant (PaLM-VQA) representative of instruction-tuned multimodal pipelines.
B. Results and Analysis
Quantitatively, VietMEAgent achieves competitive gains over baselines on all metrics, with the largest margins observed
in Cultural Accuracy and Explanation Quality, reflecting the benefits of knowledge integration and program-structured
reasoning. BLEU-4 scores also improve, suggesting that textual rationales are not only faithful but linguistically fluent.
Nevertheless, complex scenes with fine-grained visual distinctions and subtle regional cues remain challenging, indicating
room for richer perceptual modules and expanded knowledge entries.

--- Page 5 ---

VietMEAgent: Culturally-Aware Few-Shot Multimodal Explanation for Vietnamese Visual Question Answering
5
Figure 3: Performance comparison across BLEU-4, Cultural Accuracy, and Explanation Quality. VietMEAgent improves
both task performance and transparency relative to strong baselines.
Table 2: Quantitative Performance Comparison
Method
BLEU-4
Cultural Accuracy
Explanation Quality
BLIP-VQA
0.325
0.156
0.234
LXMERT
0.312
0.145
0.198
PaLM-VQA
0.356
0.198
0.267
VietMEAgent
0.486
0.723
0.689
C. Ablation Study
An ablation analysis isolates the contribution of each module. Removing the cultural knowledge base leads to the
most pronounced drop in Cultural Accuracy and Explanation Quality, underscoring the centrality of explicit cultural
grounding. Suppressing the visual explanation channel reduces perceived faithfulness even when answers remain correct,
while omitting the programming module degrades both accuracy and coherence, likely because the system loses its ability
to decompose questions into verifiable sub-steps.
Table 3: Ablation Study of VietMEAgent Components
Configuration
BLEU-4
Cultural Accuracy
Explanation Quality
Full Model
0.486
0.723
0.689
w/o Knowledge Base
0.398
0.334
0.445
w/o Visual Explanation
0.456
0.678
0.534
w/o Programming Module
0.423
0.645
0.567
VI. CONCLUSIONS
We have presented VietMEAgent, a few-shot multimodal explanation framework for Vietnamese Cultural VQA that
unifies cultural object detection, program-structured reasoning, and knowledge-grounded explanation. The proposed
dataset and method jointly advance cultural coverage, interpretability, and task performance. Although complex scenes
and subtle regional nuances continue to present difficulties, the results suggest a practical path toward culturally faithful,
transparent AI systems. Future work will expand the knowledge base, refine perception for fine-grained recognition, and
explore deployment in educational tools and heritage documentation platforms.
VII. ACKNOWLEDGMENTS
We thank Vietnamese cultural experts for their careful annotations and validation, and we acknowledge the broader
research community for constructive feedback during early dissemination. All materials are handled with respect for
cultural heritage and ethical guidelines for research.

--- Page 6 ---

VietMEAgent: Culturally-Aware Few-Shot Multimodal Explanation for Vietnamese Visual Question Answering
6
VIII. DATA AVAILABILITY
The Vietnamese Cultural VQA dataset is available for research purposes at https://huggingface.co/
datasets/Dangindev/viet-cultural-vqa under licenses designed to balance accessibility with responsible
use.
References
[1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida,
Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774,
2023.
[2] Peter Anderson, Xiaodong He, Chris Buehler, Damien Teney, Mark Johnson, Stephen Gould, and Lei Zhang.
Bottom-up and top-down attention for image captioning and visual question answering. In Proceedings of the IEEE
conference on computer vision and pattern recognition, pages 6077–6086, 2018.
[3] Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu, Margaret Mitchell, Dhruv Batra, C Lawrence Zitnick, and Devi
Parikh. Vqa: Visual question answering. In Proceedings of the IEEE international conference on computer vision,
pages 2425–2433, 2015.
[4] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren
Zhou. Qwen-vl: A frontier large vision-language model with versatile abilities. arXiv preprint arXiv:2308.12966,
2023.
[5] Satanjeev Banerjee and Alon Lavie. Meteor: An automatic metric for mt evaluation with improved correlation with
human judgments. In Proceedings of the ACL workshop on intrinsic and extrinsic evaluation measures for machine
translation and/or summarization, pages 65–72, 2005.
[6] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan,
Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. Advances in neural
information processing systems, 33:1877–1901, 2020.
[7] Shi Chen and Qi Zhao. Rex: Reasoning-aware and grounded explanation. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages 15586–15595, 2022.
[8] Tanmay Gupta and Aniruddha Kembhavi. Visual programming: Compositional visual reasoning without training. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 14953–14962, 2023.
[9] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. Blip-2: bootstrapping language-image pre-training with
frozen image encoders and large language models. In Proceedings of the 40th International Conference on Machine
Learning, pages 19730–19742, 2023.
[10] Qing Li, Qingyi Tao, Shafiq Joty, Jianfei Cai, and Jiebo Luo. Vqa-e: Explaining, elaborating, and enhancing your
answers for visual questions. In Proceedings of the European Conference on Computer Vision (ECCV), pages
552–567, 2018.
[11] Zhenyu Li, Sunqi Fan, Yu Gu, Xiuxing Li, Zhichao Duan, Bowen Dong, Ning Liu, and Jianyong Wang. Flexkbqa:
A flexible llm-powered framework for few-shot knowledge base question answering. In Proceedings of the AAAI
Conference on Artificial Intelligence, volume 38, pages 18608–18616, 2024.
[12] Chin-Yew Lin. Rouge: A package for automatic evaluation of summaries. In Text summarization branches out, pages
74–81, 2004.
[13] Pan Lu, Swaroop Mishra, Tanglin Xia, Liang Qiu, Kai-Wei Chang, Song-Chun Zhu, Oyvind Tafjord, Peter Clark,
and Ashwin Kalyan. Learn to explain: Multimodal reasoning via thought chains for science question answering. In
Advances in Neural Information Processing Systems, volume 35, pages 2507–2521, 2022.
[14] Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu, and Jianfeng Gao.
Chameleon: Plug-and-play compositional reasoning with large language models. Advances in Neural Information
Processing Systems, 36, 2024.
[15] Ana Maraˇsovi´c, Chandra Bhagavatula, Jae Sung Park, Ronan Le Bras, Noah A Smith, and Yejin Choi. Natural
language rationales with full-stack visual reasoning: From pixels to semantic frames to commonsense graphs. 2020.

--- Page 7 ---

VietMEAgent: Culturally-Aware Few-Shot Multimodal Explanation for Vietnamese Visual Question Answering
7
[16] Matthias Minderer, Alexey Gritsenko, Austin Stone, Maxim Neumann, Dirk Weissenborn, Alexey Dosovitskiy,
Aravindh Mahendran, Anurag Arnab, Mostafa Dehghani, Zhuoran Shen, et al. Simple open-vocabulary object
detection. In European Conference on Computer Vision, pages 728–755. Springer, 2022.
[17] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic evaluation of machine
translation. In Proceedings of the 40th annual meeting of the Association for Computational Linguistics, pages
311–318, 2002.
[18] Dong Huk Park, Lisa Anne Hendricks, Zeynep Akata, Anna Rohrbach, Bernt Schiele, Trevor Darrell, and Marcus
Rohrbach. Multimodal explanations: Justifying decisions and pointing to the evidence. In Proceedings of the IEEE
conference on computer vision and pattern recognition, pages 8779–8788, 2018.
[19] Machel Reid, Nikolay Savinov, Denis Teplyashin, Dmitry Lepikhin, Timothy Lillicrap, Jean-baptiste Alayrac, Radu
Soricut, Angeliki Lazaridou, Orhan Firat, Julian Schrittwieser, et al. Gemini 1.5: Unlocking multimodal understanding
across millions of tokens of context. arXiv preprint arXiv:2403.05530, 2024.
[20] Dídac Surís, Sachit Menon, and Carl Vondrick. Vipergpt: Visual inference via python execution for reasoning. In
Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 11888–11898, 2023.
[21] Hao Tan and Mohit Bansal. Lxmert: Learning cross-modality encoder representations from transformers. In
Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International
Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 5100–5111, 2019.
[22] Zhang Wen and Yuxin Peng. Multi-level knowledge injecting for visual commonsense reasoning. IEEE Transactions
on Circuits and Systems for Video Technology, 31(3):1042–1054, 2020.
[23] Jialin Wu and Raymond Mooney. Faithful multimodal explanation for visual question answering. In Proceedings of
the 2019 ACL Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP, pages 103–112, 2019.
[24] Dizhan Xue, Shengsheng Qian, and Changsheng Xu. Variational causal inference network for explanatory visual
question answering. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 2515–
2525, 2023.
[25] Rowan Zellers, Yonatan Bisk, Ali Farhadi, and Yejin Choi. From recognition to cognition: Visual commonsense
reasoning. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 6720–6731,
2019.
[26] Yiyi Zhou, Rongrong Ji, Jinsong Su, Yongjian Wu, and Yunsheng Wu. More than an answer: Neural pivot network
for visual question answering. In Proceedings of the 25th ACM international conference on Multimedia, pages
681–689, 2017.

```
