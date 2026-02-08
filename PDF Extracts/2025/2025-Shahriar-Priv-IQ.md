---
title: "2025-Shahriar-Priv-IQ - PDF Extract"
source_pdf: "2025-Shahriar-Priv-IQ.pdf"
pages: 44
extracted_at: "2026-02-08T11:55:10.224142"
---

# PDF Extract: 2025-Shahriar-Priv-IQ

**Source PDF:** 2025-Shahriar-Priv-IQ.pdf
**Total Pages:** 44

---

## Content

```
--- Page 1 ---

 
 
 
 
AI 2025, 6, 29 
https://doi.org/10.3390/ai6020029 
Article 
Priv-IQ: A Benchmark and Comparative Evaluation of Large 
Multimodal Models on Privacy Competencies 
Sakib Shahriar * and Rozita Dara 
School of Computer Science, University of Guelph, Guelph, ON N1G 2W1, Canada; drozita@uoguelph.ca 
*  Correspondence: shahrias@uoguelph.ca 
Abstract: Large language models (LLMs) and generative artiﬁcial intelligence (AI) have 
demonstrated  notable  capabilities,  achieving  human-level  performance  in  intelligent 
tasks  like  medical  exams.  Despite  the  introduction  of  extensive  LLM  evaluations  and 
benchmarks in disciplines like education, software development, and general intelligence, 
a privacy-centric perspective remains underexplored in the literature. We introduce Priv-
IQ,  a  comprehensive  multimodal  benchmark  designed  to  measure  LLM  performance 
across diverse privacy tasks. Priv-IQ measures privacy intelligence by deﬁning eight com-
petencies, including visual privacy, multilingual capabilities, and knowledge of privacy 
law. We conduct a comparative study evaluating seven prominent LLMs, such as GPT, 
Claude, and Gemini, on the Priv-IQ benchmark. Results indicate that although GPT-4o 
performs relatively well across several competencies with an overall score of 77.7%, there 
is room for signiﬁcant improvements in capabilities like multilingual understanding. Ad-
ditionally, we present an LLM-based evaluator to quantify model performance on Priv-
IQ. Through a case study and statistical analysis, we demonstrate that the evaluator’s per-
formance closely correlates with human scoring. 
Keywords: generative artificial intelligence; large language models; privacy benchmark; 
data risk assessment; privacy evaluation 
 
1. Introduction 
Privacy has long been a vital component of human society, encompassing both per-
sonal and institutional concerns. With the rise in the digital age, the conversation around 
privacy has increasingly focused on information privacy, especially in contexts where 
sensitive data are widely shared and processed. This shift has given rise to data protection 
laws and regulations like the General Data Protection Regulation (GDPR) [1] and Personal 
Information Protection and Electronic Documents Act (PIPEDA) [2], designed to safe-
guard personal information in an era of massive data collection and processing. Although 
traditional privacy-enhancing technologies (PETs) and regulations were adept at mitigat-
ing existing privacy threats, the rise in large language models (LLMs) introduces new 
privacy risks. LLMs trained on publicly available data may inadvertently memorize and 
leak sensitive information [3]. For instance, Google’s Language Model for Dialog Appli-
cations (LaMDA) was trained on a dataset containing over 1.56 trillion publicly available 
words [4]. A model trained on large text corpora might expose private details (like names 
and addresses) through a data extraction attack [5]. In applications like home assistants 
or clinical note summarizers, sensitive user data such as health records or personal be-
haviors may be at risk [6]. 
Academic Editor: Luis Javier Garcia 
Villalba 
Received: 3 December 2024 
Revised: 6 January 2025 
Accepted: 4 February 2025 
Published: 6 February 2025 
Citation: Shahriar, S.; Dara, R.   
Priv-IQ: A Benchmark and   
Comparative Evaluation of Large 
Multimodal Models on Privacy 
Competencies. AI 2025, 6, 29. 
https://doi.org/10.3390/ai6020029 
Copyright: © 2025 by the authors. 
Licensee MDPI, Basel, Switzerland. 
This article is an open access article 
distributed under the terms and 
conditions of the Creative Commons 
Attribution (CC BY) license 
(https://creativecommons.org/license
s/by/4.0/). 

--- Page 2 ---

AI 2025, 6, 29 
2  of  44 
 
Complex artiﬁcial intelligence (AI) models are increasingly integrated into everyday 
technologies in sectors like education [7] and healthcare [8]. Companies like Amazon are 
embedding these models in their products, creating more opportunities for user interac-
tion and more data for models to train on [9]. While this improves AI capabilities, it raises 
serious privacy concerns, particularly when user data could be memorized and exposed. 
Adversaries can exploit vulnerabilities in AI models through attacks such as membership 
inference [10] or training data extraction [5]. Additionally, prompt injection attacks can 
bypass model safeguards, leading to the exposure of conﬁdential information and harm-
ful content ([11,12]). As AI systems become increasingly integrated into everyday life, the 
need for these systems to comprehend and respect privacy principles is critical. If privacy 
risks are not mitigated appropriately, users could face consequences like identity theft and 
data breaches. Poor privacy management can damage the reputation of organizations and 
lead to expensive legal ﬁnes. 
In the past, tasks such as banking and teller services required signiﬁcant human re-
sources and time, often leading to long queues and delays. The introduction of automated 
teller machines (ATMs) alleviated these challenges by providing eﬃcient, user-friendly 
service [13]. Similarly, in more complex scenarios, intelligent automation, such as com-
puter vision algorithms, has surpassed human capabilities in tasks like detecting faulty 
goods  and  improving  quality  control  [14].  With  rising  privacy  concerns  in  the  digital 
sphere, there is potential for AI models to replace the need for human privacy and security 
experts by achieving high levels of intelligence in understanding and managing privacy 
threats. To explore this potential, our research addresses several key questions: What core 
competencies  are  required  for AI  to  demonstrate  privacy  intelligence?  How  can  these 
competencies be systematically measured and benchmarked? How well do current state-
of-the-art multimodal LLMs perform in addressing privacy challenges, and where do they 
fall short? To answer these questions, our work presents the following key contributions: 
 
We deﬁne eight primary privacy competencies targeted to measure the competency 
of large multimodal models in various privacy-related tasks. 
 
We introduce a multimodal benchmark to evaluate the privacy intelligence of large 
language models encompassing the eight competencies. 
 
We conduct a comparative study to assess the current capabilities of leading models. 
 
We present an LLM-based evaluator enabling researchers to score new LLMs on pri-
vacy intelligence. 
The rest of the manuscript is organized as follows. Section 2 provides an overview of 
related works in the literature. Section 3 introduces the Priv-IQ benchmark by deﬁning 
the eight competencies. Section 4 presents the comparative study evaluating state-of-the-
art multimodal models on the Priv-IQ benchmark. Section 5 discusses the main results 
and provides a case study evaluating the proposed LLM-based evaluator against human 
judgment. Finally, Section 6 concludes the study and hints at future research directions. 
2. Related Work 
In this section, we explore related works in the literature focusing on the privacy of 
LLMs, their safety, and benchmarks evaluating their intelligence. 
2.1. LLM Privacy Attacks, Vulnerabilities, and Solutions 
Several studies have explored privacy attacks and defenses in the context of LLMs. 
Jailbreaking, which involves designing speciﬁc prompts to exploit vulnerabilities or loop-
holes in LLMs, has emerged as a growing concern [15]. Given that LLMs are trained on 
vast amounts of internet data, often including private information, such attacks can reveal 
new  privacy  threats,  particularly  in  application-integrated  systems  like  ChatGPT  and 
New Bing [16]. Moreover, the susceptibility of LLM chatbots to advanced jailbreak attacks 

--- Page 3 ---

AI 2025, 6, 29 
3  of  44 
 
(with over 20% success rate) highlights gaps in existing defenses, as these vulnerabilities 
can be exploited to generate sensitive or inappropriate responses [17]. In addition to jail-
breaks, membership inference attacks highlight privacy risks by determining whether a 
speciﬁc data sample was included in a model’s training data. Neighborhood attacks elim-
inate training data dependency by leveraging synthetic neighbor texts, oﬀering a more 
realistic alternative for assessing privacy risks [18]. Concerns about training data contam-
ination in LLMs have also been raised [19]. Recent methods use exchangeable benchmarks 
to detect contamination without access to pretraining data, providing reliable evidence 
for small models and datasets [20]. 
Hallucination in LLM refers to scenarios where models generate false or inaccurate 
information. Fact checking has become increasingly critical as these tools, while capable 
of generating convincing content, are prone to errors that can mislead users or propagate 
misinformation  ([21,22]).  Eﬀorts  to  evaluate  and  mitigate  hallucinations  through  new 
frameworks highlight promising approaches to improve factuality while maintaining re-
producibility and cost eﬃciency [23]. In parallel, memorization in LLMs has raised con-
cerns about privacy and data reuse [24]. Larger models are more prone to memorizing 
training data, especially when exposed to repetitive patterns, making deduplication an 
eﬀective  mitigation  strategy  [25].  Furthermore,  a  model’s  ability  to  answer  fact-based 
questions strongly correlates with the prevalence of relevant information in pretraining 
data,  underscoring  the  importance  of  retrieval  augmentation  for  capturing  long-tail 
knowledge and reducing reliance on memorized content [26]. 
A host of research has been dedicated to preserving the privacy of LLMs while main-
taining performance. Approaches like anonymizing training data and assessing models 
ﬁne-tuned on such data demonstrate promise in reducing privacy risks [27]. However, 
techniques like scrubbing data are often insuﬃcient, as membership inference and recon-
struction attacks can still extract sensitive information, highlighting the need for diﬀeren-
tial privacy [28]. Diﬀerential privacy has shown potential to reduce personally identiﬁable 
information  leakage,  though  limitations  remain,  including  residual  leakage  risks  and 
trade-oﬀs in model utility [29]. Privacy risks can also be addressed directly at the model 
level. For instance, locating and erasing “risky neurons” in trained models enables devel-
opers to mitigate privacy risks without retraining from scratch [30]. Semi-automated pipe-
lines can also uncover indirect leaks through carefully constructed prompts, emphasizing 
the importance of contextual privacy safeguards [31]. Similarly, users can evaluate and 
control the risk of their PII being leaked by LLMs to add transparency and accountability 
in model development [32]. It is also possible to enhance the customization of LLMs with 
private data while providing local diﬀerential privacy guarantees [33]. At the system level, 
frameworks like autonomous edge AI systems leverage federated learning and task-ori-
ented communication to deliver privacy-preserving AI services at the network edge, en-
suring low latency and adaptability to user demands [34]. In operational settings, privacy-
preserving inference frameworks can leverage secure multi-party computing to protect 
sensitive data during inference [35]. Watermarking generated text also oﬀers a practical 
method for embedding privacy-preserving signals into LLM outputs, enabling the detec-
tion of content provenance without compromising text quality [36]. 
2.2. LLM Trustworthiness and Safety 
Besides privacy, the safety and trustworthiness of LLMs are crucial in building public 
trust in these technologies. In this context, safety and trustworthiness entail the ability to 
ensure ethical use, prevent harm, and align with human values [37]. For instance, trust-
worthiness can be evaluated across dimensions such as truthfulness, fairness, and robust-
ness,  revealing  that  proprietary  LLMs  generally  outperform  open-source  counterparts 
while  highlighting  the  tension  between  trustworthiness  and  utility  [38].  Safety  and 

--- Page 4 ---

AI 2025, 6, 29 
4  of  44 
 
alignment are often used interchangeably to denote the potential risks of LLMs going 
against human interests or values. Safety concerns like generating harmful or misleading 
content emphasize the importance of rigorous evaluation. Several benchmarks measure 
alignment to safety and responsibility criteria, addressing issues like instruction attacks, 
cultural biases, and adherence to human values ([39,40]). Similarly, exaggerated safety 
behaviors like refusing safe prompts due to overly cautious calibration can be detected 
but present a delicate balance between helpfulness and harm prevention [41]. 
LLMs deployed in sensitive domains like healthcare further illustrate the importance 
of trustworthiness. For example, privacy-aware approaches can be integrated to improve 
compatibility between Electronic Health Records and clinical trials, ensuring security and 
ethical data use [42]. However, concerns remain about the inability of chatbots to comply 
with regulatory frameworks like the Health Insurance Portability and Accountability Act 
(HIPAA), necessitating novel legal and ethical approaches to mitigate risks in medical ap-
plications [43]. Governance and auditing provide another layer of assurance, as outlined 
in a three-layered framework encompassing governance, model, and application audits. 
This structured approach addresses ethical and social challenges by evaluating LLMs at 
all stages of deployment, oﬀering a practical mechanism for identifying and managing 
risks [44]. Furthermore, studies emphasize the need for transparency in model outputs 
and the underlying technologies, as seen in assessments of ChatGPT’s security, ethics, and 
societal impact [45]. Lastly, public benchmarks enable large-scale evaluations of safety 
across diverse scenarios, facilitating open research and responsible development [46]. 
2.3. Existing LLM Benchmarks 
In the context of LLMs, multimodality refers to the ability to process and generate 
information across multiple modalities, such as text, images, and videos. Several bench-
marks have been established to evaluate these capabilities systematically. MMBench of-
fers  a  bilingual  evaluation  pipeline  that  rigorously  assesses  vision-language  models 
(VLMs) across multiple-choice questions in English and Chinese [47]. Similarly, SEED-
Bench  categorizes  multimodal  capabilities  hierarchically,  providing  a  comprehensive 
benchmark with 24K human-annotated questions that span both text and image genera-
tion [48]. Benchmarks like MM-Vet and its extension MM-Vet v2 focus on integrating core 
vision-language capabilities such as spatial awareness, math, and optical character recog-
nition (OCR), while extending to interleaved image–text sequence understanding for real-
world scenarios ([49,50]). Meanwhile, Mementos emphasizes sequential image reasoning, 
addressing the limitations of benchmarks that focus on static, single-image evaluations; 
key challenges like hallucinations and behavioral misrepresentations in sequential rea-
soning tasks are demonstrated [51]. To assess advanced perception tasks, Blink targets 
core visual perception abilities like depth estimation and forensic detection, which remain 
challenging for multimodal models as human accuracy far exceeds that of leading Multi-
modal Large Language Models (MLLMs) like GPT-4V and Gemini [52]. Similarly, MMT-
Bench evaluates Large Vision-Language Models (LVLMs) across expert-level multimodal 
tasks, covering areas like visual dialog and embodied navigation [53]. LVLM-eHub pro-
vides a holistic evaluation of publicly available large multimodal models; quantitative ca-
pability assessments and user-level evaluations in open-world scenarios reveal limitations 
like object hallucinations and overﬁtting to speciﬁc tasks [54]. Evaluations on capacities 
like scoring and pair comparisons show inconsistencies and biases in judgment tasks [55]. 
In general multimodal understanding, frameworks allow researchers to evaluate models 
on tasks requiring true generalization [56]. 
Other benchmarks have focused on evaluating LLMs on domain specialization, ad-
dressing unique challenges in speciﬁc ﬁelds. The evaluation of process mining tasks high-
lights  both  the  strengths  and  biases  of  LLMs  in  performing  process-speciﬁc  analytics 

--- Page 5 ---

AI 2025, 6, 29 
5  of  44 
 
while identifying areas requiring improvement for smaller edge-device models [57]. Sci-
Assess evaluates LLMs in a scientiﬁc literature analysis, assessing their memorization, 
comprehension, and reasoning capabilities across diverse domains such as biology and 
medicine [58]. In education, evaluating LLM performance on computer science concept 
inventories shows that LLMs often underperform on complex computing tasks like nested 
conditionals and a runtime analysis [59]. In the healthcare domain, the complexities of 
analyzing discharge summaries were addressed to bridge the gap between single-note 
evaluations and real-world clinical inquiries; a high correlation with clinician evaluations 
can improve clinical decision making [60]. Similarly, AgEval assessed multimodal LLMs 
in agricultural tasks like plant stress phenotyping, oﬀering insights into their zero-shot 
and few-shot learning performance for scalable solutions in agriculture [61]. For LLMs 
functioning as agents, CToolEval evaluates their ability to invoke tools across domains 
like travel and shopping; however, challenges of hallucinations in real-world scenarios 
persist  [62].  Meanwhile,  Mobile-Bench  addresses  multi-app  collaboration,  focusing  on 
task complexity and sequential action planning in mobile environments [63]. In program-
ming, Mercury introduces a novel eﬃciency metric for Code LLMs to bridge the gap be-
tween functional correctness and computational eﬃciency [64], while EvoEval evolves 
traditional coding benchmarks to expose overﬁtting in LLMs’ instruction-following abili-
ties [65]. Further, assessing LLMs’ structural understanding of tabular data reveals that 
self-augmentation and structured prompting methods lead to further improvements [66]. 
A framework to evaluate the risks posed by LLM agents in malicious multi-step tasks 
sheds light on their vulnerabilities to jailbreaking and misuse [67]. LLM can also be used 
as a “judge” for scalable and explainable assessments in open-ended conversational tasks 
by aligning LLM performance with human preferences [68]. 
3. Priv-IQ Multimodal Benchmark for Privacy Evaluation 
Traditionally, organizations and individuals responsible for data protection have re-
lied on established methods such as anonymization to mask direct identiﬁers; while eﬀec-
tive to some extent, these methods have limitations in addressing more complex privacy 
concerns. Advanced techniques like diﬀerential privacy oﬀer stronger protections but re-
quire signiﬁcant expertise, making them inaccessible to many. With advancements in ma-
chine intelligence, particularly in LLMs, there is potential to leverage their analytical ca-
pabilities for implementing privacy measures. However, this necessitates the develop-
ment of a framework that deﬁnes key privacy competencies and evaluates LLMs’ ability 
to understand and apply privacy techniques in real-world applications. Despite the grow-
ing importance of such an approach, a comprehensive privacy framework is absent in the 
current literature. Through the Priv-IQ benchmark, we address this gap by introducing a 
Turing Test-like methodology for privacy, which will provide a foundation for research-
ers to develop more specialized privacy-competent models. Figure 1 provides examples 
from the Priv-IQ benchmark across several competencies. 

--- Page 6 ---

AI 2025, 6, 29 
6  of  44 
 
 
 
 
Figure 1. Examples from the Priv-IQ benchmark measuring various privacy competencies. Each 
question (Q) is paired with its corresponding image along with the ground truth (GT) for assessment 
and the privacy competencies required to address each question. 

--- Page 7 ---

AI 2025, 6, 29 
7  of  44 
 
3.1. Privacy Competencies 
We propose a comprehensive multimodal benchmark that requires various core and 
auxiliary competencies reflecting realistic privacy scenarios an AI agent or LLM might en-
counter. Figure 2 illustrates the eight competencies, further grouped into three core compe-
tencies. Throughout this work, competency and capability are used interchangeably. 
. 
Figure 2. Eight privacy competencies evaluated in the Priv-IQ benchmark. 
These privacy competencies can provide a comprehensive evaluation of model per-
formance on privacy understanding, measuring core aspects of privacy, information, and 
model cores: 
1. 
Visual Privacy Recognition (VizPriv): This capability requires models to recognize 
potential privacy risks from images, identify sensitive information and object prop-
erties (e.g., text, multiple objects), and count items if needed to assess visual privacy 
threats. 
2. 
Named Entity Recognition (NER): This task evaluates the model’s ability to identify 
and  label  personal  identiﬁers  or  sensitive  entities, such  as  names,  addresses, and 
phone numbers, especially within multimodal contexts and free-form texts. 
3. 
Privacy Risk Assessment (PrivRisk): This capability focuses on recognizing speciﬁc 
privacy risks posed by various scenarios and identifying how particular elements 
within data can lead to privacy breaches. An example is comprehending how speciﬁc 
identiﬁers or details can be exploited by diﬀerent privacy attacks. 
4. 
Privacy-Enhancing Technologies (PETs): Knowledge of PETs is essential, as models 
must understand diﬀerent technologies that mitigate privacy risks and apply them 
where relevant. 
5. 
Privacy Law and Regulations (Law): Awareness of privacy laws, such as GDPR and 
PIPEDA, is necessary for privacy compliance. This competency ensures understand-
ing of regulatory frameworks and their implications, including recourse and penal-
ties. 
6. 
General Privacy Knowledge (Know): This category evaluates the model’s founda-
tional understanding of privacy principles, allowing it to handle general knowledge 
questions that guide its decisions regarding sensitive data. For instance, the model 
must know the diﬀerence between direct and quasi-identiﬁers to eﬀectively protect 
them. 

--- Page 8 ---

AI 2025, 6, 29 
8  of  44 
 
7. 
Contextual  Privacy  Understanding  (CntxPriv):  Since  privacy  is  often  contextual, 
models must interpret how objects relate spatially and how combinations may reveal 
unintended information, such as when a personal item appears alongside identifying 
details. For instance, a pregnancy test kit in an image alone may be benign but, com-
bined with other information, could risk disclosure. 
8. 
Multilingual Understanding (MultLing): In a multilingual society, privacy protec-
tion must extend across languages. This capability tests the model’s understanding 
of privacy principles in multiple languages and their combinations to ensure con-
sistent  privacy  standards  across  language  barriers  in  the  interconnected  digital 
world. 
The eight competencies introduced in our benchmark are further grouped into three 
core capabilities: a privacy core, information core, and model core. The privacy core in-
cludes visual privacy recognition, named entity recognition, and privacy risk assessment, 
as these require models to apply deep privacy understanding in complex and nuanced 
scenarios  beyond  simple  factual  knowledge.  The  information  core  encompasses 
knowledge of PETs, privacy laws, and general privacy concepts, providing a foundational 
knowledge base for models to address complex privacy issues eﬀectively (including the 
ones in the privacy core). The model core includes contextual understanding and multi-
lingual understanding, reﬂecting the fundamental complexity of the model itself. Simpler 
models often struggle with these tasks; they may not be adept at dealing with multilingual 
understanding or perform worse in tasks requiring high contextual awareness. 
The eight selected competencies in the Priv-IQ benchmark are grounded in ﬁndings 
from the privacy- and LLM-related literature. The importance of visual privacy arises 
from the need to protect sensitive information in images. Gurari et al. [69] explored pri-
vacy risks in visual data and demonstrated the necessity for models to recognize and mit-
igate such risks. Similarly, multimodal NER plays a crucial role in identifying personal 
identiﬁers in diverse contexts, with research highlighting how multimodal interactions 
and uniﬁed transformers enhance recognition accuracy [70]. In addition, privacy risk as-
sessment focuses on understanding how data elements contribute to privacy risks. The 
complexity  of  privacy  vulnerabilities and  the  importance  of  risk assessment are  high-
lighted by quantifying re-identiﬁcation risks using realistic threat models [71]. To ensure 
a comprehensive understanding of privacy, models must exhibit knowledge of general 
privacy facts and concepts, PETs, and regulatory frameworks. PETs are indispensable for 
mitigating privacy threats in distributed and data-driven environments, and understand-
ing their complex taxonomy and application is necessary ([72,73]). Further, existing works 
have  leveraged  automated  tools  like  machine  learning  to  summarize  privacy  policies, 
demonstrating how foundational knowledge of legal frameworks supports eﬀective pri-
vacy management [74,75]. Beyond regulatory knowledge, a general understanding of pri-
vacy principles is essential for handling diverse scenarios. Several frameworks have con-
ceptualized privacy and its correlates, highlighting the interplay of privacy calculus and 
risk calculus in shaping privacy behavior [76,77]. The evolution of LLMs has introduced 
capabilities  that  were  previously  uncommon  in  computational  approaches.  Existing 
works have established the importance of understanding visual contexts and their impli-
cations  for  real-world  applications  and  privacy  [78,79].  Similarly,  multilingual  under-
standing has become a vital competency in a globalized world; existing LLMs struggle 
with multilingual challenges in low-resource languages, emphasizing the need for models 
to achieve consistent privacy standards across languages [80,81]. 
Organizations and individuals dealing with sensitive data must rely on these pri-
mary competencies to navigate privacy challenges eﬀectively. For instance, a social media 
platform must identify sensitive details in images, such as nudity or personal information, 
to  prevent  inappropriate  content  dissemination  (VizPriv).  When  collecting  user  data, 

--- Page 9 ---

AI 2025, 6, 29 
9  of  44 
 
ensuring that personal identiﬁers are properly concealed from public access is essential 
(NER). Additionally, recognizing how seemingly anonymized data can be combined with 
other information to enable linkage attacks and compromise individual privacy is critical 
(PrivRisk). Employing privacy-enhancing technologies like diﬀerential privacy and fed-
erated learning ensures secure data processing (PET). The organization must also adhere 
to legal frameworks, such as notifying users about breaches to avoid penalties (Law) and 
educating employees on best practices like using strong passwords and secure backups 
(Know). Furthermore, understanding the context in which sensitive information appears 
(such as in accompanying text, images, or URLs) is essential for comprehensive privacy 
management (CntxPriv). Finally, in a global platform with multilingual users, appreciat-
ing the nuances of data and private information in various languages is indispensable 
(MultLing). Through Priv-IQ, these key capabilities are tested using structured scenarios 
and multimodal data (text and images), which reﬂect the complex privacy demands en-
countered in real-world AI applications. 
3.2. Data Collection 
In the data collection phase, we relied on annotated data from various sources to 
avoid the need for manual annotation as much as possible. For visual privacy, we relied 
on the VizWiz-Priv [69] and the BIV-Priv datasets [82], which contained non-private and 
private images, respectively. The private media from the VizWiz-Priv dataset were not 
publicly available or blurred; hence, we relied on only using non-private images from this 
dataset. In contrast, the BIV-Priv dataset included images from several private categories 
captured by blind participants. For multimodal named entity recognition, we relied on 
the dataset by Yu et al. [70], which combines the Twitter-2015 [83] and Twitter-2017 [84] 
datasets. However, we recognize the lack of multilingual representations in this dataset. 
Therefore, we manually annotated a few multilingual examples for multimodal named 
entity recognition to extend this benchmark. The annotations in Chinese, Russian, and 
Arabic were validated further using Google Translate. For privacy risk assessment and 
multilingual entity recognition, we also relied on samples from AI4privacy, a dataset of 
personally  identiﬁable  information  on  Hugging  Face  [85].  As  the  examples  from  the 
AI4privacy dataset were available only in text form, we applied the text content to a back-
ground  image  to  obtain  our  image–text  pair.  For  questions  related  to  general  privacy 
knowledge, privacy-enhancing technologies, and information privacy scenarios, we relied 
on various textbooks, course assignment handouts, online articles, and academic papers. 
For questions related to privacy law and regulation, we used the case study and scenarios 
presented by the Oﬃce of the Privacy Commissioner of Canada’s investigations subject to 
PIPEDA [86] as well as other case studies violating GDPR. Following the completion of 
our benchmark, we presented samples from the benchmark to two privacy and cyberse-
curity experts for further validation. 
Each data point in our evaluation is structured as an image–text pair consisting of 
four key components: an image ﬁlename, a question, a ground truth answer, and the ca-
pabilities measured. The image ﬁlename identiﬁes the visual input (e.g., v1_0.png). The 
question poses a privacy-related query about the content of the image, such as, “Does the 
image contain any sensitive information that could be a privacy risk?” The ground truth 
answer provides an annotated response explaining the privacy implications, for example, 
“Yes, this image contains a pregnancy test along with a signed document which could 
lead to identiﬁcation.” Finally, the capabilities measured highlight the speciﬁc skills being 
assessed, such as VizPriv for recognizing sensitive visual elements and CntxPriv for un-
derstanding the contextual implications of combining visual and textual information. This 
structured approach ensures a robust evaluation of the model’s ability to detect and inter-
pret  privacy  risks  in  real-world  scenarios.  In  total,  our  benchmark  consists  of  146 

--- Page 10 ---

AI 2025, 6, 29 
10  of  44 
 
questions spanning the aforementioned eight competencies. Our benchmark comprises a 
total of 146 questions distributed across eight competencies. Figure 3 provides a bar chart 
that visually represents the number of questions associated with each competency. Since 
some questions involve multiple competencies, Table 1 oﬀers a detailed breakdown, high-
lighting individual competencies and their combinations. 
 
Figure 3. The distribution of privacy competencies based on their occurrence in the Priv-IQ bench-
mark. 
Table 1. Detailed breakdown of benchmark questions, showing counts for individual competencies 
and combinations where questions span multiple competencies. 
Capability/Combination 
Count 
Law 
29 
Know 
19 
CntxPriv and VizPriv 
17 
CntxPriv and PET 
14 
VizPriv 
12 
PET 
10 
CntxPriv and Know 
8 
CntxPriv and NER 
6 
Know and PrivRisk 
6 
CntxPriv and MultLing and NER 
5 
NER 
3 
PrivRisk 
3 
Know and PET 
3 
CntxPriv and PrivRisk 
3 
MultLing and VizPriv 
2 
MultLing and NER 
2 
CntxPriv and Law 
2 
Know and Law 
2 
Total 
146 
4. Comparative Study 
Having introduced the benchmark, our next objective was to evaluate the perfor-
mance of state-of-the-art LLMs on privacy competencies. In this section, we outline the 
experimental setup, evaluation approach, and results from our experiments. 

--- Page 11 ---

AI 2025, 6, 29 
11  of  44 
 
4.1. Experimental Setup 
While LLMs have demonstrated notable success in areas such as machine translation, 
problem solving in exams, and image recognition [87], this work represents the ﬁrst sys-
tematic eﬀort to measure the privacy understanding of these models. To this end, we se-
lected seven state-of-the-art models: Claude 3 Opus, Claude 3.5 Sonnet, DeepSeek-VL, 
Gemini 1.5 Flash, Gemini 1.5 Pro, GPT-4o, and GPT-4o Mini. Each model is brieﬂy de-
scribed below based on its oﬃcial documentation. 
 
Claude  3  Opus:  Developed  by  Anthropic,  this  model  (https://www.an-
thropic.com/news/claude-3-family,  accessed  on  24  December  2024)  specializes  in 
handling complex analyses, higher-order tasks such as advanced math and coding, 
and multi-step workﬂows [88]. It is optimized for speed and cost, making it suitable 
for applications requiring quick yet precise outputs. 
 
Claude 3.5 Sonnet: This model (https://www.anthropic.com/news/claude-3-5-sonnet, 
accessed on 24 December 2024) excels in graduate-level reasoning, undergraduate-
level knowledge tasks, and coding proﬁciency. It demonstrates a marked improve-
ment  in  nuanced  understanding  and  content  generation,  combining  high  perfor-
mance with cost eﬃciency, making it ideal for multi-step and context-sensitive tasks 
[89]. 
 
DeepSeek-VL: 
This 
open-source 
vision-language 
model 
(https://arxiv.org/abs/2403.05525, accessed on 24 December 2024) is designed for real-
world applications requiring multimodal understanding. Its capabilities include in-
terpreting diagrams, the scientiﬁc literature, and natural images, along with handling 
embodied intelligence in complex scenarios, positioning it as a versatile tool for both 
visual and textual inputs [90]. In our experiments, we used the DeepSeek‐VL‐1.3B‐chat 
version with a sequence length of 4096. 
 
Gemini 1.5 Flash: Known for its faster response times and reduced hallucinations, 
this  model  (https://ai.google.dev/gemini-api/docs/models/gemini#gemini-1.5-ﬂash, 
accessed on 24 December 2024) oﬀers high-quality reasoning and improved latency. 
It supports longer conversations with a 32K token context window and is well suited 
for tasks requiring eﬃcient yet detailed outputs, such as customer service and rea-
soning-based queries [91]. 
 
Gemini 1.5 Pro: This mid-sized multimodal model (https://deepmind.google/tech-
nologies/gemini/pro/, accessed on 24 December 2024) introduces a breakthrough in 
long-context understanding, with a standard 128K token context window and an ex-
perimental feature supporting up to 1 million tokens [92]. Its Mixture-of-Experts ar-
chitecture  enhances  its  eﬃciency,  making  it  scalable  across  diverse  and  complex 
tasks. 
 
GPT-4o: OpenAI’s GPT-4o (https://openai.com/index/hello-gpt-4o/, accessed on 24 
December 2024) is a multilingual, multimodal transformer that sets benchmarks in 
voice, vision, and language tasks [87]. Supporting over 50 languages and oﬀering 
voice-to-voice capabilities, it is designed for a wide range of applications requiring 
advanced multimodal understanding and context retention with a 128K token limit 
[93]. 
 
GPT-4o Mini: This cost-eﬃcient version of GPT-4o (https://openai.com/index/gpt-
4o-mini-advancing-cost-eﬃcient-intelligence/, accessed on 24 December 2024) pro-
vides robust performance on tasks requiring low latency and aﬀordability. With its 
support for text and vision inputs and outputs, it is useful for applications needing 
real-time interactions, such as customer support and API-based workﬂows [94]. 
To evaluate each method, we leverage their respective Application Programming In-
terfaces (APIs), sending image–text pairs from the Priv-IQ benchmark to the model for 
response generation. The evaluation begins by encoding the image into a base64 format 
and combining it with a textual prompt to create a structured input payload. The payload 
is sent to the model’s API, specifying parameters such as the model’s name, maximum 
token  limit,  and  temperature  settings.  The  model  processes  the  input  and  returns  a 

--- Page 12 ---

AI 2025, 6, 29 
12  of  44 
 
response, which is then compared against the ground truth answer in the Priv-IQ bench-
mark to assess performance across various privacy-related tasks. 
4.2. LLM‐Based Evaluator 
Many existing benchmarks rely on multiple-choice or single-value responses, which 
are relatively straightforward to evaluate. However, our benchmark poses a unique chal-
lenge by including questions that require detailed, qualitative answers. For instance, the 
question “Does the image contain any sensitive information that could be a privacy risk?” 
might have a ground truth response such as, “Yes, the image contains sensitive medical 
information visible on a pill container, revealing the patient’s name and part of the pre-
scription details like dosage.” Evaluating such responses demands assessing the logical 
and contextual correctness of the model’s output, rather than a binary yes/no evaluation. 
To address this challenge, we developed an LLM-based evaluator to automatically assess 
the correctness of model responses by comparing them to the ground truth. This allows 
for faster, more cost-eﬀective, and less subjective evaluations compared to human judg-
ment. The establishment of related LLM-based evaluation has been justiﬁed in the litera-
ture due to their similar or improved ability to assess qualitative answers ([95–97]). Fur-
thermore, we have made the evaluator publicly available to encourage researchers to re-
ﬁne and develop privacy-aware models in the future. 
Our LLM-based evaluator builds on MM-Vet [49] but introduces signiﬁcant enhance-
ments tailored for privacy-speciﬁc evaluation tasks. We chose GPT-4o for its superior per-
formance and cost eﬃciency. To adapt the few-shot learning approach, we expanded the 
context to include ten in-context examples designed for privacy-related questions. These 
examples cover completely correct, partially correct, and incorrect responses, enabling the 
evaluator to assign scores from 0.0 (completely wrong) to 1.0 (totally accurate) based on 
the alignment of model responses with the ground truth. To mathematically model the 
evaluation, let each sample  𝑖  in the dataset have a correctness score  𝑠௜, ranging from 0 
(completely incorrect) to 1 (completely correct). The overall performance of a model across 
𝑁  samples is computed as 
𝑆ൌ
∑
௦೔
ಿ
೔సభ
ே
ൈ100   
(1)
where  𝑆  represents the overall evaluation score as a percentage, and  𝑠௜  is the correctness 
score for the  𝑖-th sample. This ensures that each sample contributes equally to the ﬁnal 
score. For capability-speciﬁc evaluations, consider a subset of the dataset  𝐶  that corre-
sponds to a speciﬁc capability or capability integration. Let  𝑁஼  denote the total number 
of samples in this subset, and  𝑠௜ be the score for each sample in  𝐶. The capability-speciﬁc 
score  𝑆஼ is given by 
𝑆஼ൌ
∑
௦೔
೔∈𝒞
ே಴
ൈ100   
(2)
where  𝑆஼  evaluates the model’s performance on a particular capability. This framework 
allows precise scoring of open-ended responses while capturing the nuanced correctness 
of answers in privacy-aware tasks. The evaluation process is automated using the GPT-4o 
API. Each sample’s question, ground truth, and model-generated response are compared, 
with correctness scores calculated via a consistent scoring rubric. The total evaluation 
score is determined by averaging individual sample scores across the dataset. Addition-
ally, capability-speciﬁc scores are computed by aggregating scores for subsets of samples 
linked to speciﬁc privacy capabilities. Table 2 provides the prompt and examples for few-
shot learning for our evaluator. We further validate the performance of our proposed eval-
uator using a small case study. 

--- Page 13 ---

AI 2025, 6, 29 
13  of  44 
 
Table 2. Few-shot learning of predictions using correctness scores. Prompt: Compare the ground 
truth and prediction from AI models to give a correctness score for the prediction. <AND> in the 
ground truth means that it is totally right only when all elements in the ground truth are present in 
the prediction, and <OR> means that it is totally right when any one element in the ground truth is 
present in the prediction. The correctness score is 0.0 (totally wrong), 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 
0.8, 0.9, or 1.0 (totally right). 
Question 
Ground Truth 
Prediction 
Correctness 
Does the image contain any sensi-
tive information that could be a 
privacy risk? 
Yes, the image contains a braille de-
vice and a mug along with a bank 
card, which reveals the cardholder 
name, card number, and expiration 
date. 
Yes, it contains sensitive infor-
mation of a bank card and a 
braille device. The card reveals 
the cardholder name, card num-
ber, and expiration date, which 
could identify the cardholder and 
could also be used for financial 
fraud. 
1.0 
Does the image contain any sensi-
tive information that could be a 
privacy risk? 
Yes, the image contains a braille de-
vice and a mug along with a bank 
card, which reveals the cardholder 
name, card number, and expiration 
date. 
Yes, this image contains a bank 
card, which reveals the card-
holder name, card number, and 
expiration date. 
0.9 
Does the image contain any sensi-
tive information that could be a 
privacy risk? 
Yes, the image contains a braille de-
vice and a mug along with a bank 
card, which reveals the cardholder 
name, card number, and expiration 
date. 
Yes, the image contains a bank 
card with sensitive/identifying in-
formation. 
0.7 
Does the image contain any sensi-
tive information that could be a 
privacy risk? 
Yes, the image contains a braille de-
vice and a mug along with a bank 
card, which reveals the cardholder 
name, card number, and expiration 
date. 
Yes, this image contains a bank 
card. 
0.5 
Does the image contain any sensi-
tive information that could be a 
privacy risk? 
Yes, the image contains a braille de-
vice and a mug along with a bank 
card, which reveals the cardholder 
name, card number, and expiration 
date. 
Yes. 
0.3 
Does the image contain any sensi-
tive information that could be a 
privacy risk? 
Yes, the image contains a braille de-
vice and a mug along with a bank 
card, which reveals the cardholder 
name, card number, and expiration 
date. 
No. 
0.0 
Can any individuals be identified 
and linked to their diseases using 
the joining of Tables (a) and (b)? 
Provide examples. 
Doug, a male lawyer who is 38 years 
old, is identified as an HIV patient 
by qid = Lawyer, Male, 38 after the 
joining. 
Yes, some individuals can be 
identified after the joining. For 
example, if we join the tables, we 
can identify Doug by attributes of 
sex, job, and age. This would 
identify Doug as an HIV patient 
who is a 38-year-old male and a 
lawyer. 
1.0 
Can any individuals be identified 
and linked to their diseases using 
the joining of Tables (a) and (b)? 
Provide examples. 
Doug, a male lawyer who is 38 years 
old, is identified as an HIV patient 
by qid = Lawyer, Male, 38 after the 
joining. 
Yes, Doug can be identified. 
0.7 

--- Page 14 ---

AI 2025, 6, 29 
14  of  44 
 
Can any individuals be identified 
and linked to their diseases using 
the joining of Tables (a) and (b)? 
Provide examples. 
Doug, a male lawyer who is 38 years 
old, is identified as an HIV patient 
by qid = Lawyer, Male, 38 after the 
joining. 
Yes. 
0.3 
Can any individuals be identified 
and linked to their diseases using 
the joining of Tables (a) and (b)? 
Provide examples. 
Doug, a male lawyer who is 38 years 
old, is identified as an HIV patient 
by qid = Lawyer, Male, 38 after the 
joining. 
No. 
0.0 
4.3. Results 
The result from the comparative study is presented in Table 3. As indicated in Figure 
4, GPT-4o reveals the best average across all categories, with a total score of 77.7. GPT-4o 
emerges as the most robust model overall, leading in ﬁve out of eight competencies, in-
cluding VizPriv (84.5), NER (68.1), Law (84.5), CntxPriv (74.5), and MultLing (55.6). Other 
models demonstrate notable strengths in speciﬁc areas. For example, Claude 3 Opus ex-
cels in PrivRisk with a score of 83.3, showcasing its strong capability in privacy risk as-
sessment. Similarly, GPT-4o Mini achieves the highest scores in PET (74.4) and Know 
(78.9), reﬂecting its proﬁciency in knowledge tasks. However, DeepSeek-VL underper-
forms across most categories, including VizPriv (39.4) and MultLing (26.7), indicating lim-
itations in adapting to privacy-speciﬁc challenges despite being a vision-language model. 
On average, the models show relative strength in visual privacy tasks, with an average of 
69.3. However, multilingual understanding has the lowest average score (43.0), highlight-
ing a consistent challenge across models, as further emphasized in Figure 5. 
The analysis of Table 3 is further contextualized by the three core competencies out-
lined in the framework: the privacy core (blue shading), information core (red shading), 
and model core (green shading). In privacy core competencies, models perform relatively 
well, with an average score of 67.1 for PrivRisk and 69.3 for VizPriv. This reﬂects their 
strength in identifying privacy risks and handling sensitive data. GPT-4o excels in this 
core, leading in both VizPriv (84.5) and NER (68.1), indicating its proﬁciency in under-
standing privacy challenges. Scores in the information core category are more variable; 
although GPT-4o shows a notable grasp of privacy Law (84.5), GPT-4o Mini performs well 
in PET (74.4) and Know (78.9), showcasing its capability in technical knowledge. In terms 
of model core capabilities, the consistent challenge of multilingual capabilities for most 
models is well noted (43.0). GPT-4o again leads with 55.6 in MultLing and 74.5 in Cntx-
Priv, emphasizing its ability to interpret contextual nuances and adapt to diverse linguis-
tic settings. 
Table 3. The performance comparison of state-of-the-art models across privacy competencies. Bold 
values indicate the best performance in each competency. 
 
VizPri
v 
NER PrivRis
k 
PET  Law Know  Cntx-
Priv 
MultLin
g 
Total 
Claude 3 Opus 
61.3 
56.2 
83.3 
57.0  69.1  75.0 
56.4 
42.2 
65.5 
Claude 3.5 Sonnet 
72.3 
64.4 
79.2 
61.1  72.4  71.1 
60.4 
43.3 
69.0 
DeepSeek-VL 
39.4 
41.9 
45.8 
23.3  39.4  50.3 
29.3 
26.7 
38.3 
Gemini 1.5 Flash 
70.6 
55.6 
65.8 
54.1  67.0  65.8 
57.1 
45.6 
63.6 
Gemini 1.5 Pro 
75.2 
59.4 
58.3 
66.7  60.9  70.8 
60.4 
44.4 
66.6 
GPT-4o 
84.5 
68.1 
70.8 
69.6  84.5  78.2 
74.5 
55.6 
77.7 
GPT-4o Mini 
81.6 
57.5 
66.7 
74.4  76.4  78.9 
69.8 
43.3 
74.6 
Average 
69.3 
57.6 
67.1 
58.0  67.1  70.0 
58.3 
43.0 
65.0 

--- Page 15 ---

AI 2025, 6, 29 
15  of  44 
 
 
Figure 4. Performance comparison of LLMs averaged across competencies. 
 
Figure 5. Performance comparison of state-of-the-art models across privacy competencies. 

--- Page 16 ---

AI 2025, 6, 29 
16  of  44 
 
Figure 6 displays radar charts for each model, showcasing their performance across 
the eight competencies. The visual representation highlights distinct strengths and weak-
nesses among the models. For instance, GPT-4o demonstrates balanced performance, ex-
celling in both privacy-related tasks such as PrivRisk and broader competencies like Cntx-
Priv  and  Law.  In  contrast,  DeepSeek-VL  shows  signiﬁcant  limitations,  particularly  in 
MultLing and VizPriv, reﬂecting its challenges in handling multilingual and visual pri-
vacy tasks. While Gemini 1.5 Pro and GPT-4o Mini exhibit notable performance in PET 
and Know, respectively, their lower scores in CntxPriv indicate room for improvement in 
contextual understanding. 
 
 
 
 
 
 

--- Page 17 ---

AI 2025, 6, 29 
17  of  44 
 
 
Figure 6. Radar charts representing the performance of LLMs across privacy competencies. 
The box plot in Figure 7 shows a wide variation in scores across metrics. There is a 
noticeable inconsistency in privacy risk assessment, with the highest median score but a 
signiﬁcant interquartile range. In contrast, multilingual capability has consistently low 
scores with minimal variability, suggesting that it remains a challenge across all models. 
The heatmap in Figure 8 reveals strong correlations between certain metrics; for instance, 
high contextual privacy is associated with high visual privacy, indicating overlapping 
skillsets in contextual understanding and image-based privacy assessments. However, 
high performance in visual privacy does not necessarily translate into strong privacy risk 
assessment  (e.g.,  weaker  correlation  between  VizPriv  and  PrivRisk).  This  discrepancy 
highlights that excelling in one domain does not always imply broader privacy compe-
tency. 
 
Figure 7. Box plots displaying the distribution of scores across metrics for all models. 

--- Page 18 ---

AI 2025, 6, 29 
18  of  44 
 
 
Figure 8. Correlation heatmap showcasing relationships between metrics across models. 
Figure  9  shows  the  hierarchical  clustering  of  models  based  on  their  performance 
across metrics. The Claude, Gemini, and GPT models are clustered, possibly due to shared 
architecture  or  training  data.  For  instance,  Claude  3  Opus  and  Claude  3.5  Sonnet  are 
closely clustered, suggesting that they perform similarly across most metrics. Models that 
excel in contextual privacy (e.g., Claude 3 and GPT-4o) also demonstrate strong perfor-
mance in PET, indicating a potential correlation between these competencies (Figure 8). 
DeepSeek-VL stands out as the least performant model, forming a distinct cluster due to 
its consistently lower scores across metrics. A further analysis is presented in the Appen-
dix A. 
 
Figure 9. Hierarchical clustered heatmap of model performance across competencies. 

--- Page 19 ---

AI 2025, 6, 29 
19  of  44 
 
4.4. Prediction Examples 
We present several samples from our benchmark across various competencies and 
their combinations with prediction examples from the various state-of-the-art LLMs in 
Table 4. We also mention the ground truth and the corresponding score obtained by each 
model answer. Additional examples with a side-by-side comparison of model answers are 
presented in the Appendix A. 
Table 4. Prediction examples. 
Question Image 
Question (Q), Ground Truth (GT), 
and Capabilities 
Model Response and Score 
 
Q: Identify what attributes are quasi-
identifiers and direct identifiers. 
 
GT: SSN is a direct identifier because 
it is unique for individuals, while 
gender, age, and zip code are quasi-
identifiers because they can be 
shared between individuals. 
 
Required capabilities: General Pri-
vacy Knowledge. 
Claude-3-Opus: In the given data, the 
SSN (Social Security Number) is a di-
rect identifier, as it uniquely identifies 
an individual. 
The other attributes—Gender, Age, 
ZIP Code, Hourly Wage, and Political 
Affiliation—are quasi-identifiers. 
While they do not directly identify a 
person on their own, combinations of 
these attributes could potentially be 
used to narrow down or identify spe-
cific individuals, especially with addi-
tional external information. 
 
Claude-3-Opus Score: 1.0. 
 
Q: List any named entities in the im-
age and classify them. 
 
GT: 1. Mueller Sports Medicine: OR-
GANIZATION, 2. Rafael Nadal: 
PERSON, 3. Mueller Pro Team: OR-
GANIZATION. 
 
Required capabilities: Named Entity 
Recognition, Contextual Privacy Un-
derstanding. 
 
Claude-3.5-Sonnet: Here are the 
named entities in the image and their 
classifications: 
1. Mueller Sports Medicine—Organi-
zation (sports medicine company). 
2. @MuellerSportMed—Social media 
handle. 
3. Rafael Nadal—Person (professional 
tennis player). 
4. Mueller Pro Team—Organization 
(sports team or group). 
5. Nike—Brand (visible on the ath-
lete’s headband). 
The image shows a tennis player in ac-
tion, wearing Nike apparel, which cor-
responds to the announcement about 
Rafael Nadal joining the Mueller Pro 
Team. 
 
Claude-3.5-Sonnet Score: 0.8. 
 
 
Q: Analyze the data breach notifica-
tion and implications. 
GT: The statement indicates that 
there has been a data breach involv-
ing unauthorized access to personal 
 
GPT-4o: The data breach notification 
indicates that unauthorized access to 
personal information has occurred, af-
fecting both users and employees. The 
Department is undertaking mitigation 

--- Page 20 ---

AI 2025, 6, 29 
20  of  44 
 
information of users, including em-
ployees. This suggests a potential 
compromise of sensitive data, such 
as names, addresses, and contact in-
formation. 
 
Required capabilities: General Pri-
vacy Knowledge, Privacy Risk As-
sessment. 
measures and notifying affected indi-
viduals to protect their sensitive infor-
mation. Additionally, the incident has 
been reported to Canada’s Office of 
the Privacy Commissioner. The impli-
cations include potential risks to per-
sonal privacy and the necessity for in-
creased security measures and moni-
toring for the affected individuals. 
GPT-4o Score: 0.7. 
 
Q: Identify GDPR violations (if any). 
 
GT: Violation of Article 33 of the 
GDPR, which requires organizations 
to notify the supervisory authority of 
a personal data breach without un-
due delay and, where feasible, within 
72 h of becoming aware of the 
breach. 
 
Required capabilities: Privacy Law 
and Regulations. 
 
GPT-4o Mini: The scenario describes 
a GDPR violation due to the com-
pany’s failure to notify the supervi-
sory authority within the required 72 
h window after experiencing a data 
breach. This breach of the notification 
obligation constitutes a violation of 
Article 33 of the GDPR, which man-
dates timely reporting of personal 
data breaches. 
 
GPT-4o Mini Score: 1.0. 
 
 
Q: What measures are taken to en-
sure user privacy? 
 
GT: The app uses a clear and concise 
consent banner to obtain user per-
mission for collecting GPS location 
and app data. 
 
Required capabilities: General Pri-
vacy Knowledge. 
 
Gemini-1.5-Pro: The question cannot 
be answered from the image alone.   
No specific privacy measures were 
mentioned. 
 
 
 
Gemini-1.5-Pro Score: 0.0. 
 
 
 
 
Q: How does the company obtain 
user consent? 
 
GT: The company obtains user con-
sent through a clear and explicit opt-
in mechanism. Users are required to 
check a box indicating their agree-
ment to the Terms of Service and Pri-
vacy Policy, as well as their consent 
to receive marketing communica-
tions. 
Required capabilities: Privacy Law 
and Regulations, General Privacy 
Knowledge. 
Gemini-1.5-Flash: The company ob-
tains user consent by asking users to 
check a box to indicate that they agree 
to receive commercial electronic infor-
mation and offers. 
 
Gemini-1.5-Flash Score: 0.3. 

--- Page 21 ---

AI 2025, 6, 29 
21  of  44 
 
 
Q: Does the image contain any sensi-
tive information that could be a pri-
vacy risk? 
 
GT: Yes, this image contains a per-
sonal letter revealing identifiable in-
formation like name and address. 
 
Required capabilities: Visual Pri-
vacy, Contextual Privacy Under-
standing. 
Deepseek-VL: The image shows a 
piece of paper with text on it, and at 
the bottom right corner, there is a line 
of text that reads “OPERA LXIX 88 121 
122 123 124 125 126 127 128 129 130.” 
This line of text appears to be a list of 
numbers, which could potentially be 
sensitive information if they are asso-
ciated with personal data or identifi-
ers. However, without additional con-
text or the ability to analyze the con-
tent of the text, it is difficult to deter-
mine if this list of numbers is indeed 
sensitive information that could be a 
privacy risk. The text on the paper it-
self does not provide any direct clues 
about the nature of the information or 
the context in which it is used. The 
rest of the visible text on the paper is 
not legible due to the resolution and 
angle of the photograph. The visual 
clues in the image, such as the list of 
numbers and the surrounding text, do 
not provide enough information to 
conclusively determine if the image 
contains sensitive information that 
could be a privacy risk. To make a 
more informed assessment, one would 
need additional context or the ability 
to read the text clearly. 
 
Deepseek-VL Score: 0.0. 
5. Discussion 
In this section, we present further analyses of the results from our comparative study. 
We also present the evaluation of the proposed LLM-based scoring. 
5.1. Analyzing Combined Competencies 
To better understand how models handle tasks requiring multiple competencies, we 
analyze the detailed breakdown of individual and combined competencies. Questions fo-
cusing on a single competency, such as Law assess the model’s knowledge of privacy laws 
exclusively. In contrast, combined competencies, such as “CntxPriv VizPriv”, evaluate 
tasks requiring both contextual privacy awareness and visual privacy recognition. For in-
stance, these tasks assess the model’s ability to interpret visual elements within a privacy-
sensitive context. The dataset encompasses a total of 146 questions, evenly distributed 
across 18 non-overlapping categories (refer to Table 1 for breakdown). 
We present the scores in Table 5, highlighting the best and second-best performances 
across various combined competencies. While GPT models generally perform the best, 
several notable trends emerge. In tasks requiring named entity recognition with contex-
tual awareness (Ner CntxPriv), GPT models struggled, with Claude 3.5 Sonnet and Gem-
ini 1.5 Pro outperforming them. Similarly, in questions assessing privacy risks that also 
require  general  knowledge  (PrivRisk  Know),  GPT  models  exhibited  relatively  poor 

--- Page 22 ---

AI 2025, 6, 29 
22  of  44 
 
performance, showcasing the limitations of generalized intelligence in niche tasks. Inter-
estingly, except DeepSeek-VL and Gemini 1.5 Flash, all models achieved top performance 
in at least one competency. This highlights the diversity of strengths across models and 
underscores the importance of combining specialized intelligence to develop advanced, 
privacy-focused models. The results emphasize that no single model excels universally, 
pointing to the need for a hybrid or ensemble approach to achieve comprehensive com-
petency in privacy-related assessments. Figure 10 shows the percentage contribution of 
various competencies to the total scores across models. GPT-4o demonstrates the most 
balanced  contribution  across  competencies,  indicating  its  versatility.  In  contrast, 
DeepSeek-VL shows limited contributions in advanced competencies. This distribution 
also highlights the need for models to excel in both individual and combined competen-
cies for robust performance in privacy-related domains. Additional ﬁgures and results are 
presented in the Appendix A. 
Table 5. Breakdown of model performance across individual competencies and their combinations. 
Highest and Second-Highest scores are highlighted. 
Model 
Law 
Know 
CntxPriv VizPriv 
PET CntxPriv 
VizPriv 
PET 
CntxPriv Know 
NER CntxPriv 
PrivRisk Know 
MultLing NER 
CntxPriv
NER 
PrivRisk 
PET Know 
CntxPriv PrivRisk 
MultLing NER 
MultLing VizPriv 
Law   
CntxPriv 
Law Know 
Total 
Claude 3 
Opus 
71.
4 
73.
7 
49.4  55.
0 
83.
3 
52.0  68.8  71.7  88.3  44.0  50.
0 
90.
0 
83.
3 
66.7  50.
0 
30.0 
45.0 
60.
0 
65.
5 
Claude 3.5 
Sonnet 
74.
8 
63.
7 
58.8  51.
4 
95.
0 
64.0  75.0  86.7  80.0  34.0  73.
3 
86.
7 
96.
7 
70.0  60.
0 
50.0 
50.0 
60.
0 
69.
0 
DeepSeek-
VL 
41.
4 
43.
7 
27.6  22.
1 
61.
7 
22.0  48.8  51.7  81.7  26.0  43.
3 
20.
0 
33.
3 
0.0 
50.
0 
5.0 
0.0 
50.
0 
38.
3 
Gemini 1.5 
Flash 
66.
2 
61.
6 
57.1  43.
6 
93.
3 
57.0  71.2  75.0  58.3  38.0  43.
3 
83.
3 
93.
3 
63.3  60.
0 
50.0 
80.0 
65.
0 
63.
6 
Gemini 1.5 
Pro 
61.
4 
73.
2 
64.1  61.
4 
91.
7 
73.0  68.8  86.7  75.0  32.0  56.
7 
83.
3 
70.
0 
0.0 
50.
0 
70.0 
70.0 
45.
0 
66.
6 
GPT-4o 
83.
1 
76.
8 
78.8  70.
0 
98.
3 
61.0  81.2  75.0  61.7  60.0  80.
0 
93.
3 
96.
7 
66.7  50.
0 
50.0 
90.0 
10
0.0 
77.
7 
GPT-4o 
Mini 
74.
8 
78.
9 
79.4  68.
6 
93.
3 
76.0  76.2  63.3  68.3  38.0  70.
0 
66.
7 
96.
7 
63.3  70.
0 
30.0 
80.0 
95.
0 
74.
6 

--- Page 23 ---

AI 2025, 6, 29 
23  of  44 
 
 
Figure 10. Percentage contribution of individual and combined competencies to total score. 
5.2. Evaluating LLM‐Based Scoring 
After developing the LLM-based evaluator to score model performances, we sought 
to validate its eﬀectiveness through a case study involving 15 participants. All participants 
had at least completed an undergraduate degree in the English language to ensure a base-
line competency in understanding and evaluating answers. The case study aimed to com-
pare human evaluations with the LLM-generated scores by presenting participants with 
both  the  ground  truth  answer and  the  model-generated answer.  Participants were in-
structed to score each response on a scale from 0.0 to 1.0. To assess the reliability and 
alignment of the LLM-based scoring system, we measured the level of agreement between 
the human evaluations and the LLM-evaluator scores using a statistical analysis. 
We designed a study using two separate surveys to ensure representation and avoid 
selection bias. Each survey consisted of ten randomly selected answers generated by var-
ious models alongside their corresponding ground truth answers. To maintain diversity 
and fair representation, all models contributed at least one answer in the combined sur-
veys. The two surveys were distributed to 15 participants, with one survey receiving eight 
responses and the other receiving seven. Participants were tasked with scoring the model-
generated answers on a scale from 0.0 to 1.0, where 0 indicated no agreement and 1 indi-
cated complete alignment with the actual answer. The task instructions provided in the 
survey included detailed scoring guidance. For instance, participants were asked to eval-
uate the potential privacy risks in a speciﬁc scenario, where both the ground truth answer 
and the model’s response were presented. Participants were instructed to assess the de-
gree to which the model’s answer aligned with the ground truth based on the logical con-
sistency, completeness, and relevance of the response. To evaluate the agreement between 
human evaluators and the LLM-based scoring system, we employed multiple statistical 
methods and metrics to ensure a comprehensive analysis. These methods include 
 
Intraclass Correlation Coeﬃcient (ICC): ICC measures the reliability or consistency 
between two or more raters (in this case, human evaluators and LLM scores). It eval-
uates how much of the variability in scores is due to diﬀerences between items rather 
than inconsistency between raters. A higher ICC indicates better agreement. Values 

--- Page 24 ---

AI 2025, 6, 29 
24  of  44 
 
above 0.75 are considered good, and between 0.5 and 0.75 is considered moderate, 
while values below 0.5 indicate poor agreement [98]. 
 
Spearman Correlation: This non-parametric measure assesses the strength and direc-
tion of the monotonic relationship between human and LLM scores. It is given by 
𝜌ൌ1 െ
଺∑ௗ೔
మ
௡ሺ௡మିଵሻ   
(3)
where  𝑑௜  is the rank diﬀerence for each item, and  𝑛  is the number of items. A higher 
Spearman Correlation (𝜌 ) indicates stronger agreement. Values range from −1 (perfect 
negative correlation) to +1 (perfect positive correlation) [99]. 
 
Mean  Absolute  Error (MAE): MAE  quantiﬁes  the average  absolute  diﬀerence be-
tween human and LLM scores, providing an intuitive measure of accuracy. Lower 
MAE values are better, indicating closer alignment between LLM and human scores. 
MAE is calculated as 
MAE ൌ1
𝑛෍|Human௜െLLM௜|
௡
௜ୀଵ
 
(4)
 
Agreement Rate: This metric calculates the percentage of scores where the diﬀerence 
between  human  and  LLM  scores  is  within  a  threshold  (±1  in  this  study).  Higher 
Agreement Rates indicate better alignment and consistency between evaluators: 
Agreement Rate ൌ
Number of agreements
Total comparisons
ൈ100   
(5)
In addition to the four statistical metrics, we used two visual methods to analyze the 
agreement between human and LLM scores: a Bland–Altman analysis plot and a violin 
plot. This plot evaluates the agreement by displaying the diﬀerences between human and 
LLM scores on the y-axis against their mean on the x-axis. It helps identify systematic bias 
and the range of variability. Limits of agreement are deﬁned as the mean diﬀerence ±1.96 
standard deviations, providing a visual representation of how closely the scores align. 
Smaller diﬀerences and tighter limits indicate better agreement [100]. 
The results in Table 6 demonstrate a moderate to strong agreement between LLM 
and human scoring, with stronger alignment in Survey 2. The ICC improved from mod-
erate (0.512) in Survey 1 to strong (0.754) in Survey 2, averaging 0.633. Spearman Correla-
tion also increased from 0.693 to 0.831, indicating a higher consistency, with an average of 
0.762. The MAE decreased from 2.1 to 1.25, and the Agreement Rate rose signiﬁcantly 
from 65% to 82.5%, showing improved precision and alignment in Survey 2. The Bland–
Altman analysis revealed reduced bias (−1.2 to −0.45) and narrower limits of agreement, 
highlighting better consistency in the second survey. The results are further supported by 
the Bland–Altman (Figure 11) and violin plots (Figure 12). In Figure 11, Survey 1 shows a 
positive mean diﬀerence (red dashed line), indicating a bias where human evaluators gen-
erally  rated  higher  than  the  LLM.  In  Survey  2,  the  mean  diﬀerence  is  closer  to  zero, 
demonstrating better alignment. The reduced bias in Survey 2 highlights improved agree-
ment, as evidenced by narrower limits of agreement and a smaller Bland–Altman bias. 
The violin plots show that human scores exhibit a narrow interquartile range centered 
around higher values (close to 10), reﬂecting consistency in human scoring. In contrast, 
the LLM scores display a bimodal distribution, with peaks near 0 and 10, highlighting its 
tendency to assign extreme scores. 
 
 

--- Page 25 ---

AI 2025, 6, 29 
25  of  44 
 
Table 6. Statistical evaluation of agreement between human and LLM scoring. 
Metric 
Survey 1 (n = 8) 
Survey 2 (n = 7) 
Average (n = 15) 
Intraclass Correlation Coefficient (ICC) 
0.512 (Moderate agreement) 
0.754 (Strong agreement) 
0.633 
Spearman Correlation 
0.693 (Moderate to strong cor-
relation) 
0.831 (Strong correlation) 
0.762 
Mean Absolute Error (MAE) 
2.1 
1.25 
1.675 
Agreement Rate (±1) 
65% 
82.5% 
73.75% 
Bland–Altman Bias (Mean Difference) 
−1.2 
−0.45 
Not Applicable 
Limits of Agreement (±1.96 SD) 
[−4.6, 2.2] 
[−3.12, 2.22] 
Not Applicable 
 
Figure 11. Bland–Altman plots comparing human and LLM scores. 

--- Page 26 ---

AI 2025, 6, 29 
26  of  44 
 
 
 
Figure 12. Violin plots comparing human and LLM scores. 
6. Conclusions and Outlook 
In this paper, we took the ﬁrst step toward developing a privacy-intelligence frame-
work.  Our  Priv-IQ  benchmark  introduces  eight  key  privacy  competencies  to  measure 
multimodal LLM privacy intelligence. We evaluated seven leading LLMs on this bench-
mark, with GPT-4o emerging as the best performer, scoring 77.7%. However, signiﬁcant 
improvements  are  needed  in  areas  such  as  multilingual  privacy  understanding  and 
named entity recognition. We have made the benchmark publicly available, along with 
an LLM-based evaluator for measuring model performance. Our evaluator was validated 
by a case study, showing strong agreement with human judgment. Based on our ﬁndings, 
future work should explore the development of specialized privacy models that combine 
the strengths of individual models and are ﬁne-tuned on privacy-related knowledge ba-
ses. Additionally, expanding the multilingual component of the benchmark is needed to 
ensure robust evaluations of privacy intelligence across diverse languages and cultural 
contexts. Future eﬀorts should also focus on addressing complex privacy scenarios, such 
as ﬁne-grained privacy attacks and adversarial robustness, by incorporating structured 
datasets and code-based tasks into the benchmark. 
 
 

--- Page 27 ---

AI 2025, 6, 29 
27  of  44 
 
Author Contributions: Conceptualization, S.S. and R.D.; methodology, S.S.; software, S.S.; valida-
tion, S.S. and R.D.; formal analysis, S.S. and R.D.; investigation, S.S.; resources, S.S.; data curation, 
S.S.; writing—original draft preparation, S.S.; writing—review and editing, S.S. and R.D.; visualiza-
tion, S.S.; supervision, R.D.; project administration, R.D.; funding acquisition, R.D. All authors have 
read and agreed to the published version of the manuscript. 
Funding: This research was funded by a Natural Sciences and Engineering Research Council of 
Canada (NSERC) Discovery Grant awarded to R. Dara. 
Institutional Review Board Statement: Not Applicable. 
Informed Consent Statement: Not Applicable. 
Data Availability Statement: The Priv-IQ benchmark and the evaluator were made publicly avail-
able on GitHub (https://github.com/sakibsh/Priv-IQ, accessed on 6 January 2025). 
Acknowledgments: We sincerely thank the privacy and cybersecurity experts for their valuable 
contributions to validating our benchmark. We also appreciate the participants for completing the 
survey, which enabled us to evaluate the performance of our LLM-based evaluator. 
Conﬂicts of Interest: The authors declare no conﬂicts of interest. 
Appendix A 
Table A1. Claude 3 Opus prediction examples. 
Question Image 
Question (Q), Ground Truth (GT), 
and Capabilities 
Model Response and Score 
 
Q: Does the image contain any 
sensitive information that could be a 
privacy risk? 
 
GT: No, the product is food-related, 
containing standard consumer 
information, and does not reveal 
identifying data. 
 
Required capabilities: Visual 
Privacy. 
Claude-3-Opus: No, the image does 
not contain any sensitive information 
that could be a privacy risk. It shows a 
close-up view of a red package or 
container labeled “Ella’s kitchen”, 
which appears to contain strawberry 
and apple baby food or snacks that 
are “super smooth” and “100% 
organic”. No personal or identifying 
information is visible. 
 
Claude-3-Opus Score: 1.0. 
 
Q: How many distinct organizations 
and individuals are mentioned in 
this tweet? 
 
GT: five<OR> 5. 
 
Required capabilities: Named 
Entity Recognition, Contextual 
Privacy Understanding. 
Claude-3-Opus: The tweet mentions 4 
distinct organizations and individu-
als: 
Trio @phronesismusic (a musical 
group). 
Frankfurt Radio Big Band (a musical 
ensemble). 
@JulArgJazz (an individual). 
@EditionRecords (a record label). 
Claude-3-Opus Score: 0.0. 
 
 

--- Page 28 ---

AI 2025, 6, 29 
28  of  44 
 
Table A2. Claude 3.5 Sonnet prediction examples. 
Question Image 
Question (Q), Ground Truth 
(GT), and Capabilities 
Model Response and Score 
 
Q: Does the image contain any 
sensitive information that could 
be a privacy risk? 
 
GT: No, the image shows a 
desk with a keyboard and 
various electronic device 
packages, without any sensitive 
information visible. 
 
Required capabilities: Visual 
Privacy. 
Claude-3.5-Sonnet: The image does not 
appear to contain any sensitive personal 
information that would pose a privacy 
risk. It shows a desk or workspace with 
various electronic devices and 
accessories, including 
A computer monitor or display. 
A wireless keyboard. 
Several product boxes, likely for tablets 
or other devices. 
A black laptop bag or carrying case. 
There are no visible documents, screens 
with readable information, or other 
items that would typically be considered 
sensitive or private. The image appears 
to be a fairly standard view of some 
consumer electronics and accessories. 
 
Claude-3.5-Sonnet Score: 1.0. 
 
Q: Explain the role of the public 
and private keys. 
 
GT: The public key is used to 
encrypt the medical records, 
ensuring that only the 
authorized party with the 
corresponding private key can 
decrypt and access the data. 
This prevents unauthorized 
disclosure of sensitive 
information. 
 
Required capabilities: General 
Privacy Knowledge, Contextual 
Privacy Understanding. 
Claude-3.5-Sonnet: In this image, the 
role of public and private keys is 
illustrated in the context of encrypting 
and sharing medical records: 
Public Key: Used in the “Data uploading 
process”. Represented by a yellow key 
icon. The public key is used to encrypt 
the plain text medical records. This en-
cryption process converts the readable 
patient data into cipher text, which is 
then stored in the cloud. 
Private Key: Used in the “Medical rec-
ord sharing process”. Also represented 
by a yellow key icon. The private key is 
used to decrypt the cipher text stored in 
the cloud. This decryption process con-
verts the encrypted data back into read-
able plain text for authorized parties like 
healthcare services, monitoring authori-
ties, or doctors. The public–private key 
pair works together in an asymmetric 
encryption system: 
The public key can be freely shared and 
is used to encrypt data. 
Only the corresponding private key can 
decrypt the data encrypted with the 
public key. 
This system ensures that even if the en-
crypted data are intercepted during 

--- Page 29 ---

AI 2025, 6, 29 
29  of  44 
 
transmission or storage, it cannot be 
read without the private key. 
This method provides a secure way to 
store sensitive medical information in 
the cloud and share it only with 
authorized parties who possess the 
private key for decryption. 
 
Claude-3.5-Sonnet Score: 1.0. 
Table A3. GPT-4o prediction examples. 
Question Image 
Question (Q), Ground Truth 
(GT), and Capabilities 
Model Response and Score 
 
Q: Does the image contain any 
sensitive information that could be 
a privacy risk? 
 
GT: Yes, the image contains 
sensitive information on a receipt, 
including date, location details, 
and payment information next to 
the lower part of an individual’s 
body. 
 
Required capabilities: Visual 
Privacy, Contextual Privacy 
Understanding. 
GPT-4o: The image contains a Best Buy 
receipt, which includes details such as store 
location, transaction details, and the last 
four digits of a credit card number. While it 
does not show highly sensitive information 
like full credit card numbers or personal 
identifiers, it does have some data that could 
pose a privacy risk if combined with other 
personal information. 
 
GPT-4o: 0.7. 
 
(a) Q: This image poses a privacy 
risk only because it contains a 
phone number that could identify 
an individual. 
 
GT: No, the image also contains 
sex, age, and social insurance 
number, which could be combined 
to identify an individual. 
 
Required capabilities: Visual 
Privacy, Multilingual Privacy 
Understanding. 
GPT-4o: The image contains sensitive 
information, including a phone number and 
partial tax code, and poses a privacy risk. It 
would be best to blur or remove these 
details to protect personal information. 
 
 
GPT-4o Score: 0.3. 

--- Page 30 ---

AI 2025, 6, 29 
30  of  44 
 
(b) Q: List any named entities in 
the image and classify them. 
 
GT: 1. Male: Sex, 2. 44 years: Age, 
3. 5442833110261561: Phone 
number, 4. 646 59 2654: SSN. 
 
Required capabilities: Named 
Entity Recognition, Contextual 
Privacy Understanding. 
GPT-4o:   
Male, 44 years—Entity: Person (Gender and 
Age). 
544283110261561—Entity: Contact Number. 
64659 2654—Entity: Fiscal Code. 
 
 
GPT-4o Score: 0.3. 
Table A4. GPT-4o Mini prediction examples. 
Question Image 
Question (Q), Ground Truth (GT), and 
Capabilities 
Model Response and Score 
 
(a) Q: How many locations are 
mentioned in this tweet, and can you 
specify their names? 
 
GT: 3 locations: Larkin Square, Buffalo, 
NY. 
 
Required capabilities: Named Entity 
Recognition, Contextual Privacy 
Understanding. 
GPT-4o Mini: The tweet 
mentions one location: Larkin 
Square in Buffalo, NY. 
 
 
GPT-4o Mini Score: 0.7. 
(b) Q: Label locations in the text with B-
LOC (Beginning of a Location) and I-LOC 
(Inside a Location) tags. 
 
GT: Larkin: B-LOC, Square: I-LOC, 
Buffalo: B-LOC, NY: B-LOC. 
 
Required capabilities: Named Entity 
Recognition, Contextual Privacy 
Understanding. 
GPT-4o Mini: the labeled text 
with B-LOC and I-LOC tags: 
a lunchtime talk in B-LOC 
Larkin I-LOC Square. (@ B-
LOC Larkin I-LOC Square in 
B-LOC Buffalo, I-LOC NY.) 
 
GPT-4o Mini Score: 1.0. 
Table A5. Gemini 1.5 pro prediction examples. 
Question Image 
Question (Q), Ground Truth (GT), 
and Capabilities 
Model Response and Score 
 
Q: Does the image contain any 
sensitive information that could be a 
privacy risk? 
 
GT: Yes, the image reveals a name 
and license number, which could 
lead to identification. 
 
Required capabilities: Visual 
Privacy. 
Gemini-1.5-Pro: Yes, the image contains a 
license number: 78B5R2MVFAHJ48500. 
Sharing this information publicly could be a 
privacy risk. 
 
 
Gemini-1.5-Pro Score: 0.7. 
 
Q: Analyze the privacy technique 
used in the image. 
 
GT: Pseudonymization is used to 
replace real names with pseudonyms, 
and it helps protect patient privacy 
and prevent direct identification. 
 
Gemini-1.5-Pro: The image shows data 
anonymization/pseudonymization. Here is 
why: 
Replacement: The original patient information 
(Peter Watson, residing in Sunnyvale, CA) 
were replaced with a different set of infor-
mation (John Mayer, residing in Boston, MA). 

--- Page 31 ---

AI 2025, 6, 29 
31  of  44 
 
Required capabilities: Privacy-
Enhancing Technologies. 
Preservation of Structure: The structure of the 
information remains the same (Patient No., 
Name, Address, City, State, Zip). This sug-
gests that the purpose is not to completely dis-
card the data but to replace it with a non-iden-
tifiable version. 
This technique is used to protect the privacy of 
individuals while still allowing the data to be 
used for other purposes (e.g., analysis, 
testing). 
 
Gemini-1.5-Pro Score: 0.9. 
Table A6. Gemini 1.5 ﬂash prediction examples. 
Question Image 
Question (Q), Ground Truth 
(GT), and Capabilities 
Model Response and Score 
 
Q: Explain the data redaction 
techniques illustrated in the 
image. 
 
GT: Full masking replaces the 
entire record, partial masking 
conceals portions of the value, 
RegExp replaces specific patterns 
with a placeholder, and Random 
replaces the value with a random 
string. 
 
Required capabilities: General 
Privacy Knowledge. 
Gemini-1.5-Flash: The image illustrates different data 
redaction techniques. These techniques are used to 
protect sensitive information by replacing it with a less 
specific or completely obscured version. 
Full: The entire data value is replaced with a 
placeholder. This is the most common and simple 
technique, offering the highest level of protection, but 
also the least informative. Example: “10/09/1992” is 
replaced with “01/01/2001.” 
Partial: Only part of the data value is redacted, usually 
the most sensitive part. This offers a balance between 
protection and information. Example: “987-65-4328” is 
replaced with “XXX-XX-4328.” 
RegEx: A regular expression is used to replace specific 
patterns within the data. This technique is useful for 
redacting specific formats, like email addresses. 
Example: “first.last@example.com” is replaced with 
“[hidden]@example.com.” 
Random: The original data are replaced with a random 
value of the same data type. This can offer a high level 
of protection, but it is important to ensure that the 
random values do not reveal any patterns or 
information. Example: “5105105105100” is replaced 
with “5500000000000004.” 
The choice of redaction technique depends on the 
sensitivity of the data and the desired level of 
information disclosure. 
 
Gemini-1.5-Flash Score: 1.0. 
Table A7. Deepseek VL prediction examples. 
Question Image 
Question (Q), Ground 
Truth (GT), and Capabili-
ties 
Model Response and Score 
 
Q: Identify GDPR 
violations (if any). 
 
GT: Violation of GDPR 
Article 44. Lack of 
adequate data protection 
safeguards for 
international transfers. 
 
Required capabilities: 
Privacy Law and 
Regulations. 
Deepseek-VL: The text provided states that a US-based 
company transfers the personal data of EU customers to 
servers located in India without implementing any 
additional data protection safeguards. This statement 
suggests a potential GDPR (General Data Protection 
Regulation) violation. 
The GDPR is a European Union regulation that sets the 
standard for data protection laws in the EU. It requires 
companies to implement appropriate technical and 
organizational measures to ensure the security of personal 
data. The GDPR also stipulates that personal data should 
not be transferred outside the EU unless the recipient 
country ensures an adequate level of protection. 

--- Page 32 ---

AI 2025, 6, 29 
32  of  44 
 
The text implies that the company is transferring data to a 
location (India) where there may not be the same level of 
data protection as in the EU. This could potentially be a 
violation of the GDPR, as it suggests that the company is 
not taking the necessary steps to ensure that the data are 
adequately protected during the transfer. 
It is important to note that the text does not provide 
explicit information about the company’s compliance with 
the GDPR or any other specific regulations. Therefore, the 
identification of a potential violation is based solely on the 
information provided and the general principles of GDPR 
compliance. 
 
Deepseek-VL Score: 0.7. 
Table A8. Comparative Example of Model Responses and Scores. 
Question Image 
Question (Q), Ground Truth 
(GT), and Capabilities 
Model Responses and Scores 
 
Q: Does the image contain any 
sensitive information that could 
be a privacy risk? 
 
GT: No, the image shows an 
UNO playing card, which does 
not reveal identifying data. 
 
Required capabilities: Visual 
Privacy. 
Claude 3 Opus: No, the image does not contain any sensitive 
information that could be a privacy risk. The image shows a 
close-up view of what appears to be a playing card with the 
number “2” printed on it in a stylized font against a blue 
background. 
Score: 1.0. 
 
Clausde 3.5 Sonnet: No, this image does not contain any 
sensitive information that could be a privacy risk. The image 
shows a playing card from the game Uno. It is a blue “2” card. 
The card is lying on what appears to be a wooden surface. 
There is no personal or private information visible in this 
image. 
Score: 1.0. 
 
Deepseek-VL: “The image shows a playing card, specifically a 
two of clubs, from the popular card game “UNO.” The card is 
placed on a wooden surface, and the focus is on the blue and 
white design of the card. There is no sensitive information 
visible on the card itself. The card does not contain any 
personal data, financial information, or any other type of 
information that could be considered private or confidential. 
The design of the card is generic and does not include any 
identifiable marks, logos, or text that could link it to a specific 
individual or entity. The only text visible on the card is the 
number “2” and the word “UNO”, which is the name of the 
game. These are not sensitive in nature and are part of the 
standard design for the game. Therefore, based on the visual 
information present in the image, there is no evidence to 
suggest that the card contains any sensitive information that 
could be a privacy risk. The card is a standard playing card 
and does not contain any identifiable information that could 
compromise privacy.” 
Score: 1.0. 
 
Gemini 1.5 Flash: No, the image does not contain any 
sensitive information. It is just a picture of a playing card. 
Score: 1.0. 
 
Gemini 1.5 Pro: No, the image does not contain any sensitive 
information. It is a picture of a playing card. 
Score: 1.0. 
 
GPT-4o: No, the image does not contain any sensitive 
information that could be a privacy risk. It depicts a playing 
card with the number 2. 
Score: 1.0. 

--- Page 33 ---

AI 2025, 6, 29 
33  of  44 
 
 
GPT-4o mini: The image does not contain any sensitive 
information that could be a privacy risk. It shows a card with 
the number “2” on it. 
Score: 1.0. 
 
Q: How many locations are 
mentioned in this tweet, and 
can you specify their names? 
 
GT: 2 locations: Dubai and 
UAE. 
 
Required capabilities: Named 
Entity Recognition. 
Claude 3 Opus: “The tweet mentions 2 locations: 
Dream Dinner Show Dubai–This appears to be the name of a 
dinner show or restaurant located in Dubai. 
UAE (United Arab Emirates)–The tweet specifies that the 
Dream Dinner Show Dubai is located in UAE, which is a 
country in the Middle East.” 
Score: 1.0. 
 
Clausde 3.5 Sonnet: “Two locations are mentioned in this 
tweet: 
Dubai 
UAE (United Arab Emirates) 
Dubai is specifically mentioned as the location of the Dream 
Dinner Show, and UAE is mentioned as the country where 
Dubai is located.” 
Score: 1.0. 
 
Deepseek-VL: “The tweet mentions one location, which is 
“Dream Dinner Show Dubai, UAE.” This is explicitly stated in 
the text of the tweet. There are no other locations mentioned in 
the visible content of the tweet.” 
Score: 0.5. 
 
Gemini 1.5 Flash: There is one location mentioned in this 
tweet: Dubai, UAE. 
Score: 0.5. 
 
Gemini 1.5 Pro: One location is mentioned in the tweet: 
Dream Dinner Show Dubai, UAE. 
Score: 0.7. 
 
GPT-4o: The tweet mentions one location: Dream Dinner 
Show Dubai, UAE. 
Score: 0.7. 
 
GPT-4o mini: The tweet mentions two locations: “Dream 
Dinner Show” and “Dubai, UAE.” 
Score: 0.5. 
 

--- Page 34 ---

AI 2025, 6, 29 
34  of  44 
 
 
 
Figure A1. Bubble charts depicting total scores vs. standard deviation across the core competencies. 
 
Figure A2. Performance comparison of models across combined competencies. 

--- Page 35 ---

AI 2025, 6, 29 
35  of  44 
 
 
 

--- Page 36 ---

AI 2025, 6, 29 
36  of  44 
 
 
 

--- Page 37 ---

AI 2025, 6, 29 
37  of  44 
 
 
 

--- Page 38 ---

AI 2025, 6, 29 
38  of  44 
 
Figure A3. Comparison across multiple privacy competencies using radar graphs. 
References 
1. 
Voigt, P.; Von Dem Bussche, A. The EU General Data Protection Regulation (GDPR); Springer International Publishing: Cham, 
Switzerland, 2017. https://doi.org/10.1007/978-3-319-57959-7. 
2. 
Privacy Commissioner of Canada. The Personal Information Protection and Electronic Documents Act (PIPEDA). Available 
online:  https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-
documents-act-pipeda/ (accessed on 21 December 2024). 
3. 
Brown, T.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J.D.; Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell, A.; et al. 
Language Models are Few-Shot Learners. In Advances in Neural Information Processing Systems; Curran Associates, Inc.: Red 
Hook, 
NY, 
USA, 
2020; 
pp. 
1877–1901. 
Available 
online: 
https://proceedings.neurips.cc/pa-
per/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html (accessed on 24 October 2024). 
4. 
Cheng, H.-T.; Thoppilan, R. LaMDA: Towards Safe, Grounded, and High-Quality Dialog Models for Everything. Available 
online:  http://research.google/blog/lamda-towards-safe-grounded-and-high-quality-dialog-models-for-everything/  (accessed 
on 24 October 2024). 
5. 
Carlini, N.; Tramèr, F.; Wallace, E.; Jagielski, M.; Herbert-Voss, A.; Lee, K.; Roberts, A.; Brown, T.; Song, D.; Erlingsson, Ú.; et 
al. Extracting Training Data from Large Language Models. In Proceedings of the 30th USENIX Security Symposium (USENIX 
Security  21),  Vancouver,  BC,  Canada,  11–13  August  2021;  pp.  2633–2650.  Available  online:  https://www.proceed-
ings.com/60082.html (accessed on 24 October 2024). 
6. 
Brown, H.; Lee, K.; Mireshghallah, F.; Shokri, R.; Tramèr, F. What Does it Mean for a Language Model to Preserve Privacy? In 
Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency, FAccT ’22, Seoul, Republic of Korea, 
21–24 
June 
2022; 
Association 
for 
Computing 
Machinery: 
New 
York, 
NY, 
USA, 
2022; 
pp. 
2280–2292. 
https://doi.org/10.1145/3531146.3534642. 
 
 

--- Page 39 ---

AI 2025, 6, 29 
39  of  44 
 
7. 
Prakash, K.; Rao, S.; Hamza, R.; Lukich, J.; Chaudhari, V.; Nandi, A. Integrating LLMs into Database Systems Education. In 
Proceedings of the 3rd International Workshop on Data Systems Education: Bridging Education Practice with Education Re-
search, DataEd ’24, Santiago, Chile, 9–15 June 2024; Association for Computing Machinery: New York, NY, USA, 2024; pp. 33–
39. https://doi.org/10.1145/3663649.3664371. 
8. 
Prabhod, K.J. Integrating Large Language Models for Enhanced Clinical Decision Support Systems in Modern Healthcare. J. 
Mach. Learn. Healthc. Decis. Support 2023, 3, 18–62. 
9. 
Goldman, S. How Amazon Blew Alexa’s Shot to Dominate AI, According to More Than a Dozen Employees Who Worked on 
It. Fortune. Available online: https://fortune.com/2024/06/12/amazon-insiders-why-new-alexa-llm-generative-ai-conversational-
chatbot-missing-in-action/ (accessed on 24 October 2024). 
10. 
Salem, A.; Zhang, Y.; Humbert, M.; Berrang, P.; Fritz, M.; Backes, M. ML-Leaks: Model and Data Independent Membership 
Inference 
Attacks 
and 
Defenses 
on 
Machine 
Learning 
Models. 
arXiv 
2018, 
arXiv:1806.01246. 
https://doi.org/10.48550/arXiv.1806.01246. 
11. 
Liu, Y.; Deng, G.; Li, Y.; Wang, K.; Wang, Z.; Wang, X.; Zhang, T.; Liu, Y.; Wang, H.; Zheng, Y.; et al. Prompt Injection attack 
against LLM-integrated Applications. arXiv 2024, arXiv:2306.05499. https://doi.org/10.48550/arXiv.2306.05499. 
12. 
Liu, X.; Yu, Z.; Zhang, Y.; Zhang, N.; Xiao, C. Automatic and Universal Prompt Injection Attacks against Large Language Mod-
els. arXiv 2024, arXiv:2403.04957. https://doi.org/10.48550/arXiv.2403.04957. 
13. 
Violano, M.; Collie, S.-C.V. Retail Banking Technology: Strategies and Resources That Seize the Competitive Advantage; John Wiley & 
Sons: Hoboken, NJ, USA, 1992; ISBN 978-0-471-53174-6. 
14. 
Brosnan, T.; Sun, D.-W. Improving quality inspection of food products by computer vision––A review. J. Food Eng. 2004, 61, 3–
16. https://doi.org/10.1016/S0260-8774(03)00183-3. 
15. 
Shen, X.; Chen, Z.; Backes, M.; Shen, Y.; Zhang, Y. “Do Anything Now”: Characterizing and Evaluating In-The-Wild Jailbreak 
Prompts on Large Language Models. arXiv 2024, arXiv:2308.03825. https://doi.org/10.48550/arXiv.2308.03825. 
16. 
Li, H.; Guo, D.; Fan, W.; Xu, M.; Huang, J.; Meng, F.; Song, Y. Multi-step Jailbreaking Privacy Attacks on ChatGPT. In Findings 
of the Association for Computational Linguistics, Proceedings of the EMNLP 2023, Singapore; Bouamor, H., Pino, J., Bali, K., Eds.; 
Association for Computational Linguistics: Stroudsburg, PA, USA, 2023; pp. 4138–4153. https://doi.org/10.18653/v1/2023.ﬁnd-
ings-emnlp.272 
17. 
Deng, G.; Liu, Y.; Li, Y.; Wang, K.; Zhang, Y.; Li, Z.; Wang, H.; Zhang, T.; Liu, Y. MasterKey: Automated Jailbreak Across 
Multiple Large Language Model Chatbots. arXiv 2023, arXiv:2307.08715. https://doi.org/10.48550/arXiv.2307.08715. 
18. 
Mattern, J.; Mireshghallah, F.; Jin, Z.; Schoelkopf, B.; Sachan, M.; Berg-Kirkpatrick, T. Membership Inference Attacks against 
Language Models via Neighbourhood Comparison. In Findings of the Association for Computational Linguistics: Proceedings of the 
ACL 2023, Toronto, ON, Canada; Rogers, A., Boyd-Graber, J., Okazaki, N., Eds.; Association for Computational Linguistics: New 
York, NY, USA, 2023; pp. 11330–11343. https://doi.org/10.18653/v1/2023.ﬁndings-acl.719 
19. 
Shi, W.; Ajith, A.; Xia, M.; Huang, Y.; Liu, D.; Blevins, T.; Chen, D.; Zettlemoyer, L. Detecting Pretraining Data from Large 
Language Models. In Proceedings of the Twelfth International Conference on Learning Representations, Vienna, Austria, 7–11 
May 2023. Available online: https://openreview.net/forum?id=zWqr3MQuNs (accessed on 21 November 2024). 
20. 
Oren, Y.; Meister, N.; Chatterji, N.; Ladhak, F.; Hashimoto, T.B. Proving Test Set Contamination in Black Box Language Models. 
arXiv 2023, arXiv:2310.17623. https://doi.org/10.48550/arXiv.2310.17623. 
21. 
Semnani, S.; Yao, V.; Zhang, H.; Lam, M. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-
Shot Grounding on Wikipedia. In Findings of the Association for Computational Linguistics, Proceedings of the EMNLP 2023, Singa‐
pore, December 2023; Bouamor, H., Pino, J., Bali, K., Eds., Association for Computational Linguistics: New York, NY, USA, 2023; 
pp. 2387–2413. https://doi.org/10.18653/v1/2023.ﬁndings-emnlp.157. 
22. 
Augenstein, I.; Baldwin, T.; Cha, M.; Chakraborty, T.; Ciampaglia, G.L.; Corney, D.; DiResta, R.; Ferrara, E.; Hale, S.; Halevy, 
A.; et al. Factuality challenges in the era of large language models and opportunities for fact-checking. Nat. Mach. Intell. 2024, 6, 
852–863. https://doi.org/10.1038/s42256-024-00881-z. 
23. 
Wang, J.; Zhou, Y.; Xu, G.; Shi, P.; Zhao, C.; Xu, H.; Ye, Q.; Yan, M.; Zhang, J.; Zhu, J.; et al. Evaluation and Analysis of Halluci-
nation in Large Vision-Language Models. arXiv 2023, arXiv:2308.15126. https://doi.org/10.48550/arXiv.2308.15126. 
24. 
Biderman, S.; Prashanth, U.; Sutawika, L.; Schoelkopf, H.; Anthony, Q.; Purohit, S.; Raﬀ, E. Emergent and Predictable Memori-
zation in Large Language Models. Adv. Neural Inf. Process. Syst. 2023, 36, 28072–28090. 
25. 
Yang, Z.; Zhao, Z.; Wang, C.; Shi, J.; Kim, D.; Han, D.; Lo, D. Unveiling Memorization in Code Models. In Proceedings of the 
IEEE/ACM 46th International Conference on Software Engineering, ICSE ’24, Lisbon, Portugal, 14–20 April 2024; Association 
for Computing Machinery: New York, NY, USA, 2024; pp. 1–13. https://doi.org/10.1145/3597503.3639074. 

--- Page 40 ---

AI 2025, 6, 29 
40  of  44 
 
26. 
Kandpal, N.; Deng, H.; Roberts, A.; Wallace, E.; Raﬀel, C. Large Language Models Struggle to Learn Long-Tail Knowledge. In 
Proceedings of the 40th International Conference on Machine Learning, PMLR, Honolulu, HI, USA, 23–29 July 2023; pp. 15696–
15707. Available online: https://proceedings.mlr.press/v202/kandpal23a.html (accessed on 21 November 2024). 
27. 
Gardiner, S.; Habib, T.; Humphreys, K.; Azizi, M.; Mailhot, F.; Paling, A.; Thomas, P.; Zhang, N. Data Anonymization for Pri-
vacy-Preserving Large Language Model Fine-Tuning on Call Transcripts. In Proceedings of the Workshop on Computational 
Approaches to Language Data Pseudonymization (CALD-pseudo 2024), St. Julian’s, Malta, 17–22 March 2024; Volodina, E., 
Alfter, D., Dobnik, S., Lindström Tiedemann, T., Muñoz Sánchez, R., Szawerna, M.I., Vu, X.-S., Eds.; Association for Computa-
tional Linguistics: New York, NY, USA, 2024; pp. 64–75. Available online: https://aclanthology.org/2024.caldpseudo-1.8 (ac-
cessed on 21 November 2024). 
28. 
Lukas, N.; Salem, A.; Sim, R.; Tople, S.; Wutschitz, L.; Zanella-Béguelin, S. Analyzing Leakage of Personally Identiﬁable Infor-
mation in Language Models. In Proceedings of the 2023 IEEE Symposium on Security and Privacy (SP), San Francisco, CA, 
USA, 21–25 May 2023; pp. 346–363. https://doi.org/10.1109/SP46215.2023.10179300. 
29. 
Carranza, A.; Farahani, R.; Ponomareva, N.; Kurakin, A.; Jagielski, M.; Nasr, M. Synthetic Query Generation for Privacy-Pre-
serving Deep Retrieval Systems using Diﬀerentially Private Language Models. In Proceedings of the 2024 Conference of the 
North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long 
Papers), Mexico City, Mexico, 16–21 June 2024; Duh, K., Gomez, H., Bethard, S., Eds.; Association for Computational Linguistics: 
New York, NY, USA, 2024; pp. 3920–3930. https://doi.org/10.18653/v1/2024.naacl-long.217. 
30. 
Wu, X.; Li, J.; Xu, M.; Dong, W.; Wu, S.; Bian, C.; Xiong, D. DEPN: Detecting and Editing Privacy Neurons in Pretrained Lan-
guage Models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, Singapore, De-
cember 2023, Singapore, 6–10 December 2023; Bouamor, H., Pino, J., Bali, K., Eds.; Association for Computational Linguistics: 
New York, NY, USA, 2023; pp. 2875–2886. https://doi.org/10.18653/v1/2023.emnlp-main.174. 
31. 
Niu, L.; Mirza, S.; Maradni, Z.; Pöpper, C. {CodexLeaks}: Privacy Leaks from Code Generation Language Models in {GitHub} 
Copilot. In Proceedings of the 32nd USENIX Security Symposium (USENIX Security 23), Anaheim, CA, USA, 9–11 August 2023; 
pp.  2133–2150.  Available  online:  https://www.usenix.org/conference/usenixsecurity23/presentation/niu  (accessed  on  21  No-
vember 2024). 
32. 
Kim, S.; Yun, S.; Lee, H.; Gubri, M.; Yoon, S.; Oh, S.J. ProPILE: Probing Privacy Leakage in Large Language Models. Adv. Neural 
Inf. Process. Syst. 2023, 36, 20750–20762. 
33. 
Li, Y.; Tan, Z.; Liu, Y. Privacy-Preserving Prompt Tuning for Large Language Model Services. arXiv 2023, arXiv:2305.06212. 
https://doi.org/10.48550/arXiv.2305.06212. 
34. 
Shen, Y.; Shao, J.; Zhang, X.; Lin, Z.; Pan, H.; Li, D.; Zhang, J.; Letaief, K.B. Large Language Models Empowered Autonomous 
Edge AI for Connected Intelligence. IEEE Commun. Mag. 2024, 62, 140–146. https://doi.org/10.1109/MCOM.001.2300550. 
35. 
Luo, J.; Zhang, Y.; Zhang, Z.; Zhang, J.; Mu, X.; Wang, H.; Yu, Y.; Xu, Z. SecFormer: Towards Fast and Accurate Privacy-Pre-
serving Inference for Large Language Models. arXiv 2024, arXiv:2401.00793. https://doi.org/10.48550/arXiv.2401.00793. 
36. 
Kirchenbauer, J.; Geiping, J.; Wen, Y.; Katz, J.; Miers, I.; Goldstein, T. A Watermark for Large Language Models. In Proceedings 
of the 40th International Conference on Machine Learning, Honolulu, HI, USA, 23–29 July 2023; pp. 17061–17084. Available 
online: https://proceedings.mlr.press/v202/kirchenbauer23a.html (accessed on 21 November 2024). 
37. 
Huang, X.; Ruan, W.; Huang, W.; Jin, G.; Dong, Y.; Wu, C.; Bensalem, S.; Mu, R.; Qi, Y.; Zhao, X.; et al. A survey of safety and 
trustworthiness  of  large  language  models  through  the  lens  of  veriﬁcation  and  validation.  Artif.  Intell.  Rev.  2024,  57,  175. 
https://doi.org/10.1007/s10462-024-10824-0. 
38. 
Huang, Y.; Sun, L.; Wang, H.; Wu, S.; Zhang, Q.; Li, Y.; Gao, C.; Huang, Y.; Lyu, W.; Zhang, Y.; et al. TrustLLM: Trustworthiness 
in Large Language Models. arXiv 2024, arXiv:2401.05561. https://doi.org/10.48550/arXiv.2401.05561. 
39. 
Xu, G.; Liu, J.; Yan, M.; Xu, H.; Si, J.; Zhou, Z.; Yi, P.; Gao, X.; Sang, J.; Zhang, R.; et al. CValues: Measuring the Values of Chinese 
Large Language Models from Safety to Responsibility arXiv 2023, arXiv:2307.09705. https://doi.org/10.48550/arXiv.2307.09705. 
40. 
Zhang, Z.; Lei, L.; Wu, L.; Sun, R.; Huang, Y.; Long, C.; Liu, X.; Lei, X.; Tang, J.; Huang, M. SafetyBench: Evaluating the Safety 
of Large Language Models. arXiv 2024, arXiv:2309.07045. https://doi.org/10.48550/arXiv.2309.07045. 
41. 
Röttger, P.; Kirk, H.; Vidgen, B.; Attanasio, G.; Bianchi, F.; Hovy, D. XSTest: A Test Suite for Identifying Exaggerated Safety 
Behaviours in Large Language Models. In Proceedings of the 2024 Conference of the North American Chapter of the Association 
for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), Mexico City, Mexico, 16–21 June 2024; 
Duh, K., Gomez, H., Bethard, S., Eds.; Association for Computational Linguistics: New York, NY, USA, 2024; pp. 5377–5400. 
https://doi.org/10.18653/v1/2024.naacl-long.301. 

--- Page 41 ---

AI 2025, 6, 29 
41  of  44 
 
42. 
Yuan, J.; Tang, R.; Jiang, X.; Hu, X. LLM for Patient-Trial Matching: Privacy-Aware Data Augmentation Towards Better Perfor-
mance and Generalizability. In Proceedings of the American Medical Informatics Association (AMIA) Annual Symposium, San 
Francisco, CA, USA,  9–13  January  2023.  Available  online:  https://par.nsf.gov/biblio/10448809-llm-patient-trial-matching-pri-
vacy-aware-data-augmentation-towards-better-performance-generalizability (accessed on 21 November 2024). 
43. 
Marks,  M.;  Haupt,  C.E.  AI  Chatbots,  Health  Privacy,  and  Challenges  to  HIPAA  Compliance.  JAMA  2023,  330,  309–310. 
https://doi.org/10.1001/jama.2023.9458. 
44. 
Mökander, J.; Schuett, J.; Kirk, H.R.; Floridi, L. Auditing large language models: A three-layered approach. AI Ethics 2024, 4, 
1085–1115. https://doi.org/10.1007/s43681-023-00289-2. 
45. 
Wu,  X.;  Duan,  R.;  Ni,  J.  Unveiling  security,  privacy,  and  ethical  concerns  of  ChatGPT.  J.  Inf.  Intell.  2024,  2,  102–115. 
https://doi.org/10.1016/j.jiixd.2023.10.007. 
46. 
Sun,  H.;  Zhang,  Z.;  Deng,  J.;  Cheng,  J.;  Huang,  M.  Safety  Assessment  of  Chinese  Large  Language  Models.  arXiv  2023, 
arXiv:2304.10436. https://doi.org/10.48550/arXiv.2304.10436. 
47. 
Liu, Y.; Duan, H.; Zhang, Y.; Li, B.; Zhang, S.; Zhao, W.; Yuan, Y.; Wang, J.; He, C.; Liu, Z.; et al. MMBench: Is Your Multi-modal 
Model an All-Around Player? In Computer Vision—ECCV 2024; Leonardis, A., Ricci, E., Roth, S., Russakovsky, O., Sattler, T., 
Varol, G., Eds.; Springer Nature: Cham, Switzerland, 2025; pp. 216–233. https://doi.org/10.1007/978-3-031-72658-3_13. 
48. 
Li, B.; Ge, Y.; Ge, Y.; Wang, G.; Wang, R.; Zhang, R.; Shan, Y. SEED-Bench: Benchmarking Multimodal Large Language Models. 
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Seattle, WA, USA, 16–22 June 2024; 
pp.  13299–13308.  Available  online:  https://openaccess.thecvf.com/content/CVPR2024/html/Li_SEED-Bench_Benchmark-
ing_Multimodal_Large_Language_Models_CVPR_2024_paper.html (accessed on 22 November 2024). 
49. 
Yu, W.; Yang, Z.; Li, L.; Wang, J.; Lin, K.; Liu, Z.; Wang, X.; Wang, L. MM-Vet: Evaluating Large Multimodal Models for Inte-
grated Capabilities. In Proceedings of the Forty-First International Conference on Machine Learning, Vienna, Austria, 21–27 
June 2024. Available online: https://openreview.net/forum?id=KOTutrSR2y (accessed on 22 November 2024). 
50. 
Yu, W.; Yang, Z.; Ren, L.; Li, L.; Wang, J.; Lin, K.; Lin, C.-C.; Liu, Z.; Wang, L.; Wang, X. MM-Vet v2: A Challenging Benchmark 
to 
Evaluate 
Large 
Multimodal 
Models 
for 
Integrated 
Capabilities. 
arXiv 
2024, 
arXiv:2408.00765. 
https://doi.org/10.48550/arXiv.2408.00765. 
51. 
Wang, X.; Zhou, Y.; Liu, X.; Lu, H.; Xu, Y.; He, F.; Yoon, J.; Lu, T.; Bertasius, G.; Bansal, M.; et al. Mementos: A Comprehensive 
Benchmark  for  Multimodal  Large  Language  Model  Reasoning  over  Image  Sequences.  arXiv  2024,  arXiv:2401.10529. 
https://doi.org/10.48550/arXiv.2401.10529. 
52. 
Fu, X.; Hu, Y.; Li, B.; Feng, Y.; Wang, H.; Lin, X.; Roth, D.; Smith, N.A.; Ma, W.-C.; Krishna, R. BLINK: Multimodal Large 
Language Models Can See but Not Perceive. In Computer Vision—ECCV 2024; Leonardis, A., Ricci, E., Roth, S., Russakovsky, O., 
Sattler, T., Varol, G., Eds.; Springer Nature: Cham, Switzerland, 2025; pp. 148–166. https://doi.org/10.1007/978-3-031-73337-6_9. 
53. 
Ying, K.; Meng, F.; Wang, J.; Li, Z.; Lin, H.; Yang, Y.; Zhang, H.; Zhang, W.; Lin, Y.; Liu, S.; et al. MMT-Bench: A Comprehensive 
Multimodal Benchmark for Evaluating Large Vision-Language Models Towards Multitask AGI. In Proceedings of the Forty-
First  International  Conference  on  Machine  Learning,  Vienna,  Austria,  21–27  June  2024.  Available  online:  https://open-
review.net/forum?id=R4Ng8zYaiz (accessed on 22 November 2024). 
54. 
Xu, P.; Shao, W.; Zhang, K.; Gao, P.; Liu, S.; Meng, F.; Huang, S.; Lei, M.; Luo, P.; Qiao, Y. LVLM-eHub: A Comprehensive 
Evaluation  Benchmark  for  Large  Vision-Language  Models.  December  2023.  Available  online:  https://openreview.net/fo-
rum?id=q1NaqDadKM (accessed on 22 November 2024). 
55. 
Chen, D.; Chen, R.; Zhang, S.; Wang, Y.; Liu, Y.; Zhou, H.; Zhang, Q.; Wan, Y.; Zhou, P.; Sun, L. MLLM-as-a-Judge: Assessing 
Multimodal LLM-as-a-Judge with Vision-Language Benchmark. In Proceedings of the Forty-First International Conference on 
Machine Learning, Vienna, Austria, 21–27 June 2024. Available online: https://openreview.net/forum?id=dbFEFHAD79 (ac-
cessed on 22 November 2024). 
56. 
Kuhnle,  A.;  Copestake,  A.  ShapeWorld—A  new  test  methodology  for  multimodal  language  understanding.  arXiv  2017, 
arXiv:1704.04517. https://doi.org/10.48550/arXiv.1704.04517. 
57. 
Berti, A.; Kourani, H.; Aalst, W.M.P. van der PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining 
Tasks. arXiv 2024, arXiv:2407.13244. https://doi.org/10.48550/arXiv.2407.13244. 
58. 
Cai, H.; Cai, X.; Chang, J.; Li, S.; Yao, L.; Wang, C.; Gao, Z.; Wang, H.; Li, Y.; Lin, M.; et al. SciAssess: Benchmarking LLM 
Proﬁciency in Scientiﬁc Literature Analysis. arXiv 2024, arXiv:2403.01976. https://doi.org/10.48550/arXiv.2403.01976. 
 
 

--- Page 42 ---

AI 2025, 6, 29 
42  of  44 
 
59. 
Ali, M.; Rao, P.; Mai, Y.; Xie, B. Using Benchmarking Infrastructure to Evaluate LLM Performance on CS Concept Inventories: 
Challenges, Opportunities, and Critiques. In Proceedings of the 2024 ACM Conference on International Computing Education 
Research—Volume 1, ICER ’24, Melbourne, Australia, 13–15 August 2024; Association for Computing Machinery: New York, 
NY, USA, 2024; pp. 452–468. https://doi.org/10.1145/3632620.3671097. 
60. 
Kweon, S.; Kim, J.; Kwak, H.; Cha, D.; Yoon, H.; Kim, K.; Yang, J.; Won, S.; Choi, E. EHRNoteQA: An LLM Benchmark for Real-
World Clinical Practice Using Discharge Summaries. In Proceedings of the 38th Conference on Neural Information Processing 
Systems  Datasets  and  Benchmarks  Track,  Vancouver,  BC,  Canada,  9–15  December  2024.  Available  online:  https://ko-
asas.kaist.ac.kr/handle/10203/324596 (accessed on 22 November 2024). 
61. 
Arshad, M.A.; Jubery, T.Z.; Roy, T.; Nassiri, R.; Singh, A.K.; Singh, A.; Hegde, C.; Ganapathysubramanian, B.; Balu, A.; Krish-
namurthy, A.; et al. AgEval: A Benchmark for Zero-Shot and Few-Shot Plant Stress Phenotyping with Multimodal LLMs. CoRR, 
January 2024. Available online: https://openreview.net/forum?id=26e0VpAKue (accessed on 22 November 2024). 
62. 
Guo, Z.; Huang, Y.; Xiong, D. CToolEval: A Chinese Benchmark for LLM-Powered Agent Evaluation in Real-World API Inter-
actions. In Findings of the Association for Computational Linguistics, Proceedings of the ACL 2024, Bangkok, Thailand, August 2024; Ku, 
L.-W., Martins, A., Srikumar, V., Eds.; Association for Computational Linguistics: New York, NY, USA, 2024; pp. 15711–15724. 
https://doi.org/10.18653/v1/2024.ﬁndings-acl.928. 
63. 
Deng, S.; Xu, W.; Sun, H.; Liu, W.; Tan, T.; Liujianfeng, L.; Li, A.; Luan, J.; Wang, B.; Yan, R.; et al. Mobile-Bench: An Evaluation 
Benchmark for LLM-based Mobile Agents. In Proceedings of the 62nd Annual Meeting of the Association for Computational 
Linguistics (Volume 1: Long Papers), Bangkok, Thailand, 11–16 August 2024; Ku, L.-W., Martins, A., Srikumar, V., Eds.; Asso-
ciation for Computational Linguistics: New York, NY, USA, 2024; pp. 8813–8831. https://doi.org/10.18653/v1/2024.acl-long.478. 
64. 
Du, M.; Luu, A.T.; Ji, B.; Liu, Q.; Ng, S.-K. Mercury: A Code Eﬃciency Benchmark for Code Large Language Models. arXiv 2024, 
arXiv:2402.07844. https://doi.org/10.48550/arXiv.2402.07844. 
65. 
Xia, C.S.; Deng, Y.; Zhang, L. Top Leaderboard Ranking = Top Coding Proﬁciency, Always? EvoEval: Evolving Coding Bench-
marks via LLM. arXiv 2024, arXiv:2403.19114. https://doi.org/10.48550/arXiv.2403.19114. 
66. 
Sui, Y.; Zhou, M.; Zhou, M.; Han, S.; Zhang, D. Table Meets LLM: Can Large Language Models Understand Structured Table 
Data? A Benchmark and Empirical Study. In Proceedings of the 17th ACM International Conference on Web Search and Data 
Mining, WSDM ’24, Mérida, Mexico, 4–8 March 2024; Association for Computing Machinery: New York, NY, USA, 2024; pp. 
645–654. https://doi.org/10.1145/3616855.3635752. 
67. 
Andriushchenko, M.; Souly, A.; Dziemian, M.; Duenas, D.; Lin, M.; Wang, J.; Hendrycks, D.; Zou, A.; Kolter, Z.; Fredrikson, M.; 
et  al.  AgentHarm:  A  Benchmark  for  Measuring  Harmfulness  of  LLM  Agents.  arXiv  2024,  arXiv:2410.09024. 
https://doi.org/10.48550/arXiv.2410.09024. 
68. 
Zheng, L.; Chiang, W.-L.; Sheng, Y.; Zhuang, S.; Wu, Z.; Zhuang, Y.; Lin, Z.; Li, Z.; Li, D.; Xing, E.; et al. Judging LLM-as-a-Judge 
with MT-Bench and Chatbot Arena. Adv. Neural Inf. Process. Syst. 2023, 36, 46595–46623. 
69. 
Gurari, D.; Li, Q.; Lin, C.; Zhao, Y.; Guo, A.; Stangl, A.; Bigham, J.P. VizWiz-Priv: A Dataset for Recognizing the Presence and 
Purpose of Private Visual Information in Images Taken by Blind People. In Proceedings of the IEEE/CVF Conference on Com-
puter Vision and Pattern Recognition, Long Beach, CA, USA, 16–20 June 2019; pp. 939–948. Available online: https://openac-
cess.thecvf.com/content_CVPR_2019/html/Gurari_VizWiz-Priv_A_Dataset_for_Recognizing_the_Presence_and_Pur-
pose_of_CVPR_2019_paper.html (accessed on 26 November 2024). 
70. 
Yu, J.; Jiang, J.; Yang, L.; Xia, R. Improving multimodal named entity recognition via entity span detection with uniﬁed multi-
modal transformer. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, Online, 5–10 
July 2020; pp. 3342–3352. https://doi.org/10.18653/v1/2020.acl-main.306. 
71. 
Vatsalan, D.; Rakotoarivelo, T.; Bhaskar, R.; Tyler, P.; Ladjal, D. Privacy risk quantiﬁcation in education data using Markov 
model. Br. J. Educ. Technol. 2022, 53, 804–821. https://doi.org/10.1111/bjet.13223. 
72. 
Kaaniche, N.; Laurent, M.; Belguith, S. Privacy enhancing technologies for solving the privacy-personalization paradox: Taxon-
omy and survey. J. Netw. Comput. Appl. 2020, 171, 102807. https://doi.org/10.1016/j.jnca.2020.102807. 
73. 
Curzon, J.; Kosa, T.A.; Akalu, R.; El-Khatib, K. Privacy and Artiﬁcial Intelligence. IEEE Transactions on Artiﬁcial Intelligence 2021, 
2, 96–108. https://doi.org/10.1109/TAI.2021.3088084. 
74. 
Tesfay, W.B.; Hofmann, P.; Nakamura, T.; Kiyomoto, S.; Serna, J. I Read but Don’t Agree: Privacy Policy Benchmarking using 
Machine Learning and the EU GDPR. In Proceedings of the Companion Proceedings of the Web Conference 2018, WWW ’18, 
April 2018; International World Wide Web Conferences Steering Committee: Geneva, Switzerland, Lyon, France, 23–27 April 
2018; pp. 163–166. https://doi.org/10.1145/3184558.3186969. 

--- Page 43 ---

AI 2025, 6, 29 
43  of  44 
 
75. 
Harkous, H.; Fawaz, K.; Lebret, R.; Schaub, F.; Shin, K.G.; Aberer, K. Polisis: Automated Analysis and Presentation of Privacy 
Policies Using Deep Learning. In Proceedings of the 27th USENIX Security Symposium (USENIX Security 18), Baltimore, MD, 
USA,  15–17  August  2018;  pp.  531–548.  Available  online:  https://www.usenix.org/conference/usenixsecurity18/presenta-
tion/harkous (accessed on 23 December 2024). 
76. 
Dinev, T.; Xu, H.; Smith, J.H.; Hart, P. Information privacy and correlates: an empirical attempt to bridge and distinguish pri-
vacy-related concepts. Eur. J. Inf. Syst. 2013, 22, 295–316. https://doi.org/10.1057/ejis.2012.23. 
77. 
Li, Y. Theories in online information privacy research: A critical review and an integrated framework. Decis. Support Syst. 2012, 
54, 471–481. https://doi.org/10.1016/j.dss.2012.06.010. 
78. 
Zang, Y.; Li, W.; Han, J.; Zhou, K.; Loy, C.C. Contextual Object Detection with Multimodal Large Language Models. Int. J. 
Comput. Vis. 2024, 133, 825–843. https://doi.org/10.1007/s11263-024-02214-4. 
79. 
Yao, Y.; Duan, J.; Xu, K.; Cai, Y.; Sun, Z.; Zhang, Y. A survey on large language model (LLM) security and privacy: The Good, 
The Bad, and The Ugly. High‐Conﬁd. Comput. 2024, 4, 100211. https://doi.org/10.1016/j.hcc.2024.100211. 
80. 
Qiu, P.; Wu, C.; Zhang, X.; Lin, W.; Wang, H.; Zhang, Y.; Wang, Y.; Xie, W. Towards building multilingual language model for 
medicine. Nat. Commun. 2024, 15, 8384. https://doi.org/10.1038/s41467-024-52417-z. 
81. 
Zhang, W.; Aljunied, M.; Gao, C.; Chia, Y.K.; Bing, L. M3Exam: A Multilingual, Multimodal, Multilevel Benchmark for Exam-
ining Large Language Models. Adv. Neural Inf. Process. Syst. 2023, 36, 5484–5505. 
82. 
Sharma, T.; Stangl, A.; Zhang, L.; Tseng, Y.-Y.; Xu, I.; Findlater, L.; Gurari, D.; Wang, Y. Disability-First Design and Creation of 
A Dataset Showing Private Visual Information Collected with People Who Are Blind. In Proceedings of the 2023 CHI Confer-
ence on Human Factors in Computing Systems, CHI ’23, Hamburg, Germany, 23–28 April 2023; Association for Computing 
Machinery: New York, NY, USA, 2023; pp. 1–15. https://doi.org/10.1145/3544548.3580922. 
83. 
Zhang, Q.; Fu, J.; Liu, X.; Huang, X. Adaptive Co-attention Network for Named Entity Recognition in Tweets. In Proceedings 
of  the  AAAI  Conference  on  Artiﬁcial  Intelligence  2018,  New  Orleans,  LA,  USA,  2–7  February  2018;  Volume  32. 
https://doi.org/10.1609/aaai.v32i1.11962. 
84. 
Lu, D.; Neves, L.; Carvalho, V.; Zhang, N.; Ji, H. Visual Attention Model for Name Tagging in Multimodal Social Media. In 
Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Melbourne, 
Australia, 15–20 July 2018; Gurevych, I., Miyao, Y., Eds., Association for Computational Linguistics: New York, NY, USA, 2018; 
pp. 1990–1999. https://doi.org/10.18653/v1/P18-1185. 
85. 
ai4privacy (Ai4Privacy). Available online: https://huggingface.co/ai4privacy (accessed on 26 December 2024). 
86. 
Privacy Commissioner of Canada. Investigations. Available online: https://www.priv.gc.ca/en/opc-actions-and-decisions/inves-
tigations/ (accessed on 26 November 2024). 
87. 
Shahriar, S.; Lund, B.D.; Mannuru, N.R.; Arshad, M.A.; Hayawi, K.; Bevara, R.V.K.; Mannuru, A.; Batool, L. Putting GPT-4o to 
the Sword: A Comprehensive Evaluation of Language, Vision, Speech, and Multimodal Proﬁciency. Appl. Sci. 2024, 14, 7782. 
https://doi.org/10.3390/app14177782. 
88. 
Introducing the Next Generation of Claude\Anthropic. Available online: https://www.anthropic.com/news/claude-3-family 
(accessed on 26 November 2024). 
89. 
Introducing Claude 3.5 Sonnet. Available online: https://www.anthropic.com/news/claude-3-5-sonnet (accessed on 26 Novem-
ber 2024). 
90. 
Lu, H.; Liu, W.; Zhang, B.; Wang, B.; Dong, K.; Liu, B.; Sun, J.; Ren, T.; Li, Z.; Yang, H.; et al. DeepSeek-VL: Towards Real-World 
Vision-Language Understanding. CoRR, 2024. Available online: https://openreview.net/forum?id=pHxj2dX7oS (accessed on 26 
November 2024). 
91. 
Gemini’s  Big  Upgrade:  Faster  Responses  with  1.5  Flash,  Expanded  Access  and  More.  Google.  Available  online: 
https://blog.google/products/gemini/google-gemini-new-features-july-2024/ (accessed on 26 November 2024).. 
92. 
Our Next-Generation Model: Gemini 1.5. Google. Available online: https://blog.google/technology/ai/google-gemini-next-gen-
eration-model-february-2024/ (accessed on 26 November 2024). 
93. 
Conway, A. What Is GPT-4o? Everything you Need to Know About the New OpenAI Model That Everyone Can Use for Free. 
XDA. Available online: https://www.xda-developers.com/gpt-4o/ (accessed on 26 November 2024). 
94. 
GPT-4o Mini: Advancing Cost-Eﬃcient Intelligence. Available online: https://openai.com/index/gpt-4o-mini-advancing-cost-
eﬃcient-intelligence/ (accessed on 26 November 2024). 
 
 

--- Page 44 ---

AI 2025, 6, 29 
44  of  44 
 
95. 
Chiang, C.-H.; Lee, H. Can Large Language Models Be an Alternative to Human Evaluations? In Proceedings of the 61st Annual 
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Toronto, ON, Canada, 9–14 July 2023; Rog-
ers, A., Boyd-Graber, J., Okazaki, N., Eds.; Association for Computational Linguistics: New York, NY, USA, 2023; pp. 15607–
15631. https://doi.org/10.18653/v1/2023.acl-long.870. 
96. 
Liu, Y.; Iter, D.; Xu, Y.; Wang, S.; Xu, R.; Zhu, C. G-Eval: NLG Evaluation using Gpt-4 with Better Human Alignment. In Pro-
ceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, Singapore, 6–10 December 2023; Boua-
mor,  H.,  Pino,  J.,  Bali,  K.,  Eds.;  Association  for  Computational  Linguistics:  New  York,  NY,  USA,  2023;  pp.  2511–2522. 
https://doi.org/10.18653/v1/2023.emnlp-main.153. 
97. 
Fu, J.; Ng, S.-K.; Jiang, Z.; Liu, P. GPTScore: Evaluate as You Desire. In Proceedings of the 2024 Conference of the North Amer-
ican Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), Mex-
ico City, Mexico, 16–21 June 2024; Duh, K., Gomez, H., Bethard, S., Eds., Association for Computational Linguistics: New York, 
NY, USA, 2024; pp. 6556–6576. https://doi.org/10.18653/v1/2024.naacl-long.365. 
98. 
Koo, T.K.; Li, M.Y. A Guideline of Selecting and Reporting Intraclass Correlation Coeﬃcients for Reliability Research. J. Chiropr. 
Med. 2016, 15, 155–163. https://doi.org/10.1016/j.jcm.2016.02.012. 
99. 
Spearman, C. “General Intelligence” Objectively Determined and Measured. In Studies in individual diﬀerences: The search for 
intelligence; Appleton-Century-Crofts: East Norwalk, CT, USA, 1961; p. 73. https://doi.org/10.1037/11491-006. 
100. Bland, J.M.; Altman, D.G. Statistical methods for assessing agreement between two methods of clinical measurement. Lancet 
1986, 1, 307–310. 
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual au-
thor(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to 
people or property resulting from any ideas, methods, instructions or products referred to in the content. 

```
