---
title: "MedHallTune - PDF Extract"
source_pdf: "2025-Zhang-MedHallTune.pdf"
pages: 11
extracted_at: "2026-01-24T16:38:38.484710"
---

# PDF Extract: MedHallTune

**Source PDF:** 2025-Zhang-MedHallTune.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

MedHallTune: An Instruction-Tuning Benchmark
for Mitigating Medical Hallucination in
Vision-Language Models
Qiao Yan1, Yuchen Yuan1, Xiaowei Hu3, Yihan Wang1, Jiaqi Xu1, Jinpeng
Li1*, Chi-Wing Fu1,2, and Pheng-Ann Heng1,2
1 Dept. of Computer Science and Engineering, The Chinese University of Hong
Kong, Hong Kong, China
2 Institute of Medical Intelligence and XR, The Chinese University of Hong Kong,
Hong Kong, China
3 Shanghai Artificial Intelligence Laboratory, China
jpli21@cse.cuhk.edu.hk
Abstract. The increasing use of vision-language models (VLMs) in health-
care applications presents great challenges related to hallucinations, in
which the models may generate seemingly plausible results that are in
fact incorrect. Such hallucinations can jeopardize clinical decision mak-
ing, potentially harming the diagnosis and treatments. In this work, we
propose MedHallTune, a large-scale benchmark designed specifically to
evaluate and mitigate hallucinations in medical VLMs. Comprising over
100,000 images and 1,000,000 instruction pairs, MedHallTune includes
both hallucination and non-hallucination samples, each with ground-
truth annotations. We conduct a comprehensive evaluation of current
medical and general VLMs using MedHallTune, assessing their perfor-
mance across key metrics, including clinical accuracy, relevance, detail
level, and risk level. The experimental results show that fine-tuning with
MedHallTune successfully improves the ability of several existing mod-
els to manage hallucinations and boost their zero-shot performance on
downstream visual-question-answering (VQA) tasks, making them more
reliable for practical medical applications. Our work contributes to the
development of more trustworthy VLMs. Codes and dataset will be avail-
able at MedHallTune.
Keywords: Medical hallucination · Hallucination mitigation · Large
vision-language models.
1
Introduction
The demand for advanced technologies that can support healthcare professionals
in decision making is rapidly growing [26]. The ability to analyze medical images,
interpret clinical data, and provide accurate insights is essential for improving pa-
tient diagnoses. Vision-language models (VLMs) have emerged as powerful tools
to meet the goal [21,13], combining the strengths of natural language processing
arXiv:2502.20780v1  [cs.AI]  28 Feb 2025

--- Page 2 ---

2
Y. Qiao et al.
Fig. 1. Examples of the medical hallucination in VLMs. The user queries about non-
existent objects in orbit of the brain or incorrect medical knowledge of trauma to the
abdomen. LLaVA-Med [13] generates a plausible response but is incorrect, as shown
in red. In contrast, after fine-tuned on MedHallTune, it provides the correct answer,
effectively countering the hallucination, as highlighted in green.
and visual data interpretation. While these models demonstrate great potential
in various applications such as medical image analysis, automated diagnosis,
and clinical decision support, one significant challenge remains, i.e., hallucina-
tions. Hallucination refers to instances that VLM models generate outputs that
are seemingly plausible but fundamentally incorrect [17]. As Fig. 1 illustrates, in
medical contexts, such inaccuracies can easily lead to misdiagnoses and improper
treatment decisions, posing serious risks to patient treatment [19].
Despite growing attention to hallucinations in VLMs, there is a significant
gap in research focusing on this issue in the medical domain [7]. Existing medical
VLMs rely heavily on benchmarks that fall short of capturing the complexities of
medical hallucinations. Traditional metrics like BLEU and METEOR focus on
surface similarities rather than factual accuracy, while sentence-level assessments
in [3] can be subjective and biased, with an overly intuitive hierarchical defini-
tion that classifies hallucinations as catastrophic, critical, or minor. Although
studies like CARES [22] analyze trustworthiness in over-confidence and absten-
tion rate by toxic prompting and several works [23,7] evaluate hallucinations in
knowledge and objects, they do not specifically address hallucinations and fall
short in evaluating the long-form VLM outputs under clinical settings. This gap
in mitigating and evaluating medical hallucinations hinders the development of
reliable medical AI systems. Therefore, there is a pressing need for methods to
evaluate hallucinations and improve the model robustness in healthcare.
To address these issues, we formulate a medical hallucination tuning dataset,
namely MedHallTune, designed specifically to enhance and evaluate the ability of
VLMs to handle hallucinations in medical contexts. MedHallTune contains over
100,000 images and more than 1,000,000 visual instructions, including pairs of
hallucination and non-hallucination samples as positive and negative instruction
pairs. Negative instructions include hallucinations such as nonexistent medical
objects and attributes and clinical knowledge distortion, while positive instruc-
tions cover tasks like medical image captioning and disease activity recognition to
prevent bias towards negative responses. To comprehensively evaluate responses
in the clinical context, we present a set of new metrics based on (i) clinical pre-
cision, (ii) clinical relevance, (iii) detail level, and (iv) risk level. Our approach
goes beyond traditional hallucination detection metrics, aiming to improve the

--- Page 3 ---

MedHallTune
3
Fig. 2. Overview of the pipeline, demonstrating the process of mitigation and evalua-
tion of medical hallucinations in VLMs via instruction tuning on MedHallTune.
reliability and trustworthiness of VLMs in real-world healthcare applications. To
sum up, our contributions are three-fold:
– We construct MedHallTune, a large-scale dataset comprising over 100,000
images and 1,000,000 instruction pairs, featuring both hallucination and non-
hallucination samples specifically tailored for medical applications.
– We propose a set of new metrics to comprehensively evaluate VLMs, as-
sessing their performance against medical hallucinations in terms of clinical
precision, clinical relevance, detail level, and risk level.
– We demonstrate that fine-tuning with MedHallTune largely enables both
medical and general VLMs to effectively mitigate medical hallucinations,
while also enhancing their zero-shot performance on downstream VQA tasks.
2
MedHallTune
In this section, we present MedHallTune, designed to mitigate and evaluate
hallucinations in VLMs within the medical domain. The overall pipeline is il-
lustrated in Fig. 2. We begin by sampling over 100,000 image-text pairs from
well-annotated datasets [13,4] sourced from the PubMed4 database. In the first
phase, we employ GPT-4o [11] to generate instruction-following data that in-
cludes both hallucination and non-hallucination examples, enhancing dataset
richness through diverse language styles. Next, we implement a self-checking
mechanism, detailed in Sec. 2.2, to filter out incorrect interpretations effectively.
Unlike prior works that assess hallucinations mainly at the object or knowledge
level [23,7] or rely on subjective classifications [3], MedHallTune introduces new
evaluation metrics tailored for healthcare scenarios.
MedHallTune is used to fine-tune existing VLMs, enhancing their ability to
manage hallucinations. As shown in Fig. 1 and Fig. 2b, when users query about
4 https://pubmed.ncbi.nlm.nih.gov/

--- Page 4 ---

4
Y. Qiao et al.
Table 1. Comparison of datasets in medical hallucination. MedHallTune stands out
in data size and includes hallucinatory objects, attributes and knowledge. We propose
new metrics for evaluation, showing that fine-tuning on MedHallTune enables VLMs to
manage medical hallucinations effectively and improve downstream task performance.
Dataset
Multimodal Data Size Object/Knowledge Tuning/Eval Downstream
Med-Halu [1]
✗
2k
✓/ ✓
✗/ ✓
✗
Med-Halt [20]
✗
18k
✓/ ✗
✗/ ✓
✗
MedVH [7]
✓
2k
✓/ ✗
✗/ ✓
✗
MedHallMark [3]
✓
7k
✓/ ✓
✓/ ✓
✗
Med-HVL [23]
✓
1.2k
✓/ ✗
✗/ ✓
✗
CARES [22]
✓
18k
✓/ ✗
✗/ ✓
✗
MedHallTune (Ours)
✓
100k
✓/ ✓
✓/ ✓
✓
non-existent objects or incorrect attributes and knowledge, unrefined models
may produce plausible but incorrect responses misaligned with the image con-
tent. After fine-tuned with MedHallTune, models demonstrate performance im-
provements on both hallucination datasets and downstream tasks, providing
accurate answers consistent with the image.
2.1
Data Construction
Hallucination Instruction Generation. Inspired by [16], we classify negative
instructions into three categories: (i) Nonexistent Medical Object Introduction,
the creation of fictitious entities or instances in medical descriptions; (ii) Exis-
tent Medical Object Manipulation, involving misrepresenting real entities in the
medical input, such as by attributing incorrect characteristics to actual objects
or suggesting unsupported relationships between them; (iii) Clinical Knowledge
Distortion, consisting of altering or misrepresenting factual medical knowledge,
such as misinterpreting the significance of information in medical imaging or
providing contradictory information that contradicts established medical knowl-
edge or facts. By generating these types of hallucination instructions, we seek
to identify and mitigate the vulnerabilities of VLMs in medical contexts. Non-
hallucination Instruction Generation. To consolidate medical knowledge
and eliminate bias towards negative answers, we include non-hallucination in-
structions. Generated using GPT-4o, these instructions cover a range of tasks,
such as medical image captioning, and medical image sentiment analysis.
2.2
Quality Control
To prevent the introduction of contradictory descriptive information that may
arise from the visual inputs during the data construction, we implement an ad-
ditional round of self-checking. The instruction-following data pairs are initially
generated by prompting GPT-4o with the image and annotations, then we pro-
vide GPT-4o with only the ground truth annotations (excluding the images)

--- Page 5 ---

MedHallTune
5
Fig. 3. Examples of (a) hallucination and (b) non-hallucination instruction data. In
the hallucination instructions, user questions are designed to inquire about non-existing
medical objects, incorrect attributes of medical objects, and erroneous clinical knowl-
edge. The answers are formulated to address these hallucinations by providing accurate
responses. (c) Quality control by filtering out incorrect instructions.
and request it to evaluate whether the generated data aligns with these annota-
tions, filtering out any inconsistent pairs, as illustrated in Fig. 3(c). This rigorous
two-step process ensures the integrity of our dataset, thereby enhancing the reli-
ability of VLMs in medical applications, and minimizing the risk of incorporating
erroneous data that could mislead models during training and evaluation.
2.3
Data Statistics
We sample over 100,000 annotated images from existing datasets [13,4] sourced
from PubMed, representing a wide range of medical domains, as illustrated in
Fig. 2(a). These images span critical organs such as the brain, chest, eyes, and
various cellular structures. After a rigorous quality control process, we filter
out 7.3% of incorrect instructions, creating over 509,000 non-hallucination and
518,000 hallucination instruction-following pairs. For the testing split, we ran-
domly select 200 images, which include 1,143 hallucination instructions as neg-
ative samples and 1,127 non-hallucination instructions as positive samples. The
remaining data are allocated to the training split of MedHallTune.
2.4
Evaluation Metrics
In this study, we design a robust evaluation to systematically assess the per-
formance of models in responding to user inquiries based on medical content.

--- Page 6 ---

6
Y. Qiao et al.
Fig. 4. Evaluation procedures and detailed scoring criteria.
This evaluation comprises four critical metrics as detailed in Fig. 4: Clinical Ac-
curacy, Clinical Relevance, Detail Level, and Risk Level, each rated on a scale
from 1 to 10, where a higher score indicates better performance. Clinical Accu-
racy evaluates the correctness of the model’s responses relative to established
medical knowledge. Clinical Relevance measures the extent to which these re-
sponses address the user’s specific inquiries. Detail Level assesses the richness
of information provided, ensuring that responses are not only accurate but also
comprehensive. Finally, Risk Level emphasizes patient safety by evaluating the
potential clinical consequences of the model’s output. To maintain consistency
across different VLMs, we first establish baseline scores by evaluating the out-
puts of LLaVA-Med [13]. Subsequently, by utilizing in-context learning ability of
GPT-4o as an evaluator, we prompt GPT-4o with the outputs of other VLMs,
along with these baseline scores and reference answers. This approach minimizes
bias in the evaluation process, ensuring that comparisons between different mod-
els are fair and objective. As illustrated in Fig. 2b, we evaluate the outputs of
various models based on our proposed metrics. For example, in response to the
incorrect answer "Yes, the mass appears to be smooth and well-defined ... ",
GPT-4o assigns scores (1, 1, 3, 1) with accompanying explanations: "The AI as-
sistant’s response is clinically inaccurate... This fundamental error compromises
the clinical accuracy of the answer... The incorrect information could lead to
severe clinical consequences if decisions are made based on it, such as ..."
3
Experiments
We conduct comprehensive evaluation of state-of-the-art VLVMs, including both
those trained on general images and those specifically designed for medical appli-
cations. The models evaluated in this study include: (1) GPT-4o, (2) MiniGPT-4
[27], (3) Janus-Pro-7b [5], (4) mPLUG-Owl2-7b [24], (5) InternVL-v1.5-4b [6],
(6) Qwen-VL-Chat [2]; and medical VLVMs: (7) Med-Flamingo [18], (8) RadFM

--- Page 7 ---

MedHallTune
7
Table 2. Evaluation of VLMs on MedHallTune. P: non-hallucination samples; N: hal-
lucination samples. The best scores are bold and the second best scores are underlined.
⊕MedHallTune indicates that models are finetuned on the training set of MedHallTune.
Method
Cli. Acc.
Cli. Rel.
Detail Level Risk Level
B. Score
M. Score
P&N ↑
P&N ↑
P&N ↑
P&N ↑
P&N ↑
P&N ↑
GPT-4o
6.51&5.37
7.08&6.04
6.43&5.88
7.56&5.67
0.88&0.87
0.33&0.27
MiniGPT-4
4.44&2.98
4.70&3.26
4.70&4.09
5.90&4.15
0.85&0.85
0.22&0.22
Janus-Pro
6.16&4.11
6.72&4.50
5.53&4.60
7.42&5.21
0.91&0.88
0.38&0.21
mPLUG-Owl2
5.97&3.83
6.43&4.18
5.72&4.64
7.16&4.88
0.89&0.88
0.35&0.24
Qwen-VL-Chat
5.93&4.21
6.42&4.57
5.52&4.59
7.15&5.41
0.90&0.88
0.34&0.19
⊕MedHallTune
6.54&4.68
7.10&5.10
5.53&4.91
7.69&5.85
0.93&0.89
0.44&0.24
InternVL-v1.5
6.01&4.24
6.56&4.67
5.27&4.55
7.26&5.31
0.89&0.87
0.29&0.20
⊕MedHallTune
6.01 &4.99
6.56&5.31
5.27&5.27
7.26&5.76
0.89&0.89
0.29& 0.18
Med-Flamingo
4.69& 3.00
4.79&3.12
3.91&3.23
6.00&4.07
0.84&0.83
0.19&0.15
RadFM
3.81&4.41
4.17&4.91
3.69&4.03
5.12&5.64
0.85&0.80
0.10&0.04
HealthGPT-M3
6.55&4.49
7.08&4.88
6.14&5.10
7.69&5.67
0.90&0.88
0.37&0.25
HuatuoGPT-V
6.50&5.04
7.04&5.55
6.75&5.74
7.67&6.32
0.88&0.87
0.34&0.26
LLaVA-Med-v1.5
6.27&5.03
6.77&5.39
5.47&4.84
7.38&5.89
0.91&0.88
0.38&0.21
⊕MedHallTune
6.67&5.91 7.24&6.56
5.92&5.87
7.79&7.22 0.92&0.90 0.44&0.31
[21], (9) HuatuoGPT-Vision-7b [4], (10) HealthGPT-M3 [14], and (11) LLaVA-
Med-v1.5-7b [13]. Each model is trained on its respective dataset and evaluated
on the testing split of the MedHallTune. Furthermore, we select three of these
models for fine-tuning on the training set: InternVL-v1.5-4b, Qwen-VL-Chat and
LLaVA-Med-v1.5-7b with 3 epochs on 8×NVIDIA A100 GPUs using LoRA [9].
Evaluation. To assess the performance of various models on MedHallTune,
we report both clinical metrics and traditional text evaluation metrics. Clinical
metrics include our proposed clinical accuracy (Cli. Acc.), clinical relevance (Cli.
Rel.), detail level, and risk level. In addition, we report traditional text evalu-
ation metrics, including Bert Score (B. Score), METEOR Score (M. Score). As
shown in Table 2, the clinical accuracy, clinical relevance, detail level, and risk
level metrics demonstrate that models trained with MedHallTune exhibit en-
hanced performance in generating clinically accurate responses. Furthermore,
the MedHallTune tuned model achieves the highest Bert Score (0.93&0.90) and
METEOR Score (0.44&0.31), indicating superior text quality and coherence.
These results underscore the efficacy of MedHallTune in improving medical VQA,
making them more applicable and reliable in clinical applications.
Zero-shot Analysis. We evaluate three selected VLMs on several biomedi-
cal VQA datasets without further training, including VQA-RAD [12], Path VQA
[8], SLAKE [15], PMC-VQA [25], and OmniMedVQA [10]. We follow the evalu-
ation criteria in [13], reporting both closed-set and open-set questions and only
the English set of SLAKE. As shown in Table 3, the overall performance of the
models fine-tuned on MedHallTune shows improvement, indicating that Med-
HallTune effectively addresses the issue of hallucination while simultaneously
enhancing the zero-shot capabilities of VLMs on downstream tasks.

--- Page 8 ---

8
Y. Qiao et al.
Table 3. Zero-shot performance of different methods on medical VQA datasets.
Method
VQA-RAD
Path VQA
SLAKE
PMC-VQA OmniMedVQA
open closed open
close
open closed
LLaVA-Med-v1.5 36.04 58.75
7.96
64.02 43.86 58.41
32.35
49.81
⊕MedHallTune
38.47 82.49 13.52 65.90 44.21 66.58
39.15
52.31
InternVL-v1.5
38.26 76.26 11.11 57.49 43.31 59.13
31.55
49.49
⊕MedHallTune
39.45 76.87 11.53 63.14 43.20 63.94
36.55
56.45
Qwen-VL-Chat
22.42 62.64
6.86
60.92 39.44 68.90
34.25
47.66
⊕MedHallTune
32.42 78.21 12.77 62.40 41.98 68.99
36.45
50.82
Fig. 5. Ablation study comparing model performance across training sets: positive
(non-hallucination), negative (hallucination), and MedHallTune with and without (w.o)
quality control, as well as training on 25%, 50%, 75%, and 100% of data.
Ablation Study. In Fig. 5(a), we investigate the impact of different training
sets on the model performance, comprising positive samples (non-hallucination),
negative samples (hallucination), and variations of MedHallTune with and with-
out quality control (w.o). The results indicate that model trained on the complete
MedHallTune dataset outperforms those trained solely on positive or negative
samples. This highlights the importance of incorporating both types of samples
in the training process to enhance the model’s ability. Furthermore, the model
trained on MedHallTune with rigorous quality control, demonstrates marked
improvements compared to models trained without such data verification.
Fig. 5(b)(c)(d)(e) illustrate the increasing performance gains achieved by
training on 25%, 50%, 75%, and 100% of the MedHallTune dataset. Overall,
the findings from our ablation study highlight the effectiveness of using the full
MedHallTune dataset and emphasize the importance of quality control in data
construction for enhancing model performance in medical VQA applications.
4
Conclusion
In this study, we introduce MedHallTune, a comprehensive dataset specifically
designed to address hallucinations of vision-language models within the med-
ical domain. By providing over 100k images and 1,000k instruction pairs, our
dataset enables robust evaluation and fine-tuning of VLMs, enhancing their

--- Page 9 ---

MedHallTune
9
ability to manage medical hallucinations effectively. We also propose new evalua-
tion metrics focused on clinical accuracy, clinical relevance, detail level, and risk
level, moving beyond traditional assessment methods. Our findings demonstrate
that fine-tuning with MedHallTune significantly improves model performance,
making VLMs more reliable for real-world medical applications. This work con-
tributes to the development of trustworthy AI systems that can support clinical
decision-making and ultimately enhance patient safety.
References
1. Agarwal, V., Jin, Y., Chandra, M., Choudhury, M.D., Kumar, S., Sastry, N.R.:
Medhalu: Hallucinations in responses to healthcare queries by large language
models. ArXiv abs/2409.19492 (2024), https://api.semanticscholar.org/
CorpusID:272987286
2. Bai, J., Bai, S., Yang, S., Wang, S., Tan, S., Wang, P., Lin, J., Zhou, C., Zhou, J.:
Qwen-vl: A versatile vision-language model for understanding, localization, text
reading, and beyond. arXiv preprint arXiv:2308.12966 (2023)
3. Chen, J., Yang, D., Wu, T., Jiang, Y., Hou, X., Li, M., Wang, S., Xiao, D., Li,
K., Zhang, L.: Detecting and evaluating medical hallucinations in large vision lan-
guage models. ArXiv abs/2406.10185 (2024), https://api.semanticscholar.
org/CorpusID:270521409
4. Chen, J., Gui, C., Ouyang, R., Gao, A., Chen, S., Chen, G., Wang, X., Cai, Z., Ji,
K., Wan, X., et al.: Towards injecting medical visual knowledge into multimodal
llms at scale. In: Proceedings of the 2024 Conference on Empirical Methods in
Natural Language Processing. pp. 7346–7370 (2024)
5. Chen, X., Wu, Z., Liu, X., Pan, Z., Liu, W., Xie, Z., Yu, X., Ruan, C.: Janus-pro:
Unified multimodal understanding and generation with data and model scaling
(2025), https://api.semanticscholar.org/CorpusID:275954151
6. Chen, Z., Wu, J., Wang, W., Su, W., Chen, G., Xing, S., Zhong, M., Zhang, Q.,
Zhu, X., Lu, L., et al.: Internvl: Scaling up vision foundation models and aligning
for generic visual-linguistic tasks. In: Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition. pp. 24185–24198 (2024)
7. Gu, Z., Yin, C., Liu, F., Zhang, P.: Medvh: Towards systematic evalua-
tion of hallucination for large vision language models in the medical context.
ArXiv abs/2407.02730 (2024), https://api.semanticscholar.org/CorpusID:
270924059
8. He, X., Zhang, Y., Mou, L., Xing, E., Xie, P.: Pathvqa: 30000+ questions for
medical visual question answering. arXiv preprint arXiv:2003.10286 (2020)
9. Hu, J.E., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Chen, W.: Lora:
Low-rank adaptation of large language models. ArXiv abs/2106.09685 (2021),
https://api.semanticscholar.org/CorpusID:235458009
10. Hu, Y., Li, T., Lu, Q., Shao, W., He, J., Qiao, Y., Luo, P.: Omnimedvqa: A new
large-scale comprehensive evaluation benchmark for medical lvlm. In: Proceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp.
22170–22183 (2024)
11. Hurst, A., Lerer, A., Goucher, A.P., Perelman, A., Ramesh, A., Clark, A., Os-
trow, A., Welihinda, A., Hayes, A., Radford, A., et al.: Gpt-4o system card. arXiv
preprint arXiv:2410.21276 (2024)

--- Page 10 ---

10
Y. Qiao et al.
12. Lau, J.J., Gayen, S., Ben Abacha, A., Demner-Fushman, D.: A dataset of clinically
generated visual questions and answers about radiology images. Scientific data
5(1), 1–10 (2018)
13. Li, C., Wong, C., Zhang, S., Usuyama, N., Liu, H., Yang, J., Naumann, T.,
Poon, H., Gao, J.: Llava-med: Training a large language-and-vision assistant for
biomedicine in one day. Advances in Neural Information Processing Systems 36
(2024)
14. Lin, T., Zhang, W., Li, S., Yuan, Y., Yu, B., Li, H., He, W., Jiang, H., Li, M.,
Song, X., Tang, S., Xiao, J., Lin, H., Zhuang, Y., Ooi, B.C.: Healthgpt: A medical
large vision-language model for unifying comprehension and generation via hetero-
geneous knowledge adaptation (2025), https://arxiv.org/abs/2502.09838
15. Liu, B., Zhan, L.M., Xu, L., Ma, L., Yang, Y.F., Wu, X.M.: Slake: A semantically-
labeled knowledge-enhanced dataset for medical visual question answering. 2021
IEEE 18th International Symposium on Biomedical Imaging (ISBI) pp. 1650–1654
(2021), https://api.semanticscholar.org/CorpusID:231951663
16. Liu, F., Lin, K., Li, L., Wang, J., Yacoob, Y., Wang, L.: Mitigating hallucination
in large multi-modal models via robust instruction tuning. In: International Con-
ference on Learning Representations (2023), https://api.semanticscholar.org/
CorpusID:259251834
17. Liu, H., Xue, W., Chen, Y., Chen, D., Zhao, X., Wang, K., Hou, L., Li,
R.Z., Peng, W.: A survey on hallucination in large vision-language models.
ArXiv abs/2402.00253 (2024), https://api.semanticscholar.org/CorpusID:
267365472
18. Moor, M., Huang, Q., Wu, S., Yasunaga, M., Dalmia, Y., Leskovec, J., Zakka, C.,
Reis, E.P., Rajpurkar, P.: Med-flamingo: a multimodal medical few-shot learner.
In: Machine Learning for Health (ML4H). pp. 353–367. PMLR (2023)
19. Thirunavukarasu, A.J., Ting, D.S.J., Elangovan, K., Gutierrez, L., Tan, T.F., Ting,
D.S.W.: Large language models in medicine. Nature medicine 29(8), 1930–1940
(2023)
20. Umapathi, L.K., Pal, A., Sankarasubbu, M.: Med-halt: Medical domain hallucina-
tion test for large language models. In: Conference on Computational Natural Lan-
guage Learning (2023), https://api.semanticscholar.org/CorpusID:260316324
21. Wu, C., Zhang, X., Zhang, Y., Wang, Y., Xie, W.: Towards generalist foun-
dation model for radiology. ArXiv abs/2308.02463 (2023), https://api.
semanticscholar.org/CorpusID:260611504
22. Xia, P., Chen, Z., Tian, J., Gong, Y., Hou, R., Xu, Y., Wu, Z., Fan, Z., Zhou, Y.,
Zhu, K., et al.: Cares: A comprehensive benchmark of trustworthiness in medical
vision language models. arXiv preprint arXiv:2406.06007 (2024)
23. Yan, Q., He, X., Wang, X.E.: Med-HVL: Automatic medical domain hallucina-
tion evaluation for large vision-language models. In: AAAI 2024 Spring Sympo-
sium on Clinical Foundation Models (2024), https://openreview.net/forum?id=
rxx8leoPy0
24. Ye, Q., Xu, H., Xu, G., Ye, J., Yan, M., Zhou, Y., Wang, J., Hu, A., Shi, P.,
Shi, Y., et al.: mplug-owl: Modularization empowers large language models with
multimodality. arXiv preprint arXiv:2304.14178 (2023)
25. Zhang, X., Wu, C., Zhao, Z., Lin, W., Zhang, Y., Wang, Y., Xie, W.: Pmc-vqa:
Visual instruction tuning for medical visual question answering. arXiv preprint
arXiv:2305.10415 (2023)
26. Zhou, H., Liu, F., Gu, B., Zou, X., Huang, J., Wu, J., Li, Y., Chen, S.S., Zhou, P.,
Liu, J., et al.: A survey of large language models in medicine: Progress, application,
and challenge. arXiv preprint arXiv:2311.05112 (2023)

--- Page 11 ---

MedHallTune
11
27. Zhu,
D., Chen,
J., Shen,
X., Li, X.,
Elhoseiny, M.:
Minigpt-4: Enhanc-
ing
vision-language
understanding
with
advanced
large
language
models.
ArXiv abs/2304.10592 (2023), https://api.semanticscholar.org/CorpusID:
258291930

```
