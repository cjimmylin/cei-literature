---
title: "2025-Yesil-Yesil o1 Pro - PDF Extract"
source_pdf: "2025-Yesil-Yesil o1 Pro.pdf"
pages: 33
extracted_at: "2026-01-29T13:51:33.699244"
---

# PDF Extract: 2025-Yesil-Yesil o1 Pro

**Source PDF:** 2025-Yesil-Yesil o1 Pro.pdf
**Total Pages:** 33

---

## Content

```
--- Page 1 ---

JMIR Preprints
Yesil et al
Yesil o1 Pro: Evidence-Based AI Model for Health and
Benchmarking in Clinical Decision Support
 Yusuf Yesil
Submitted to: JMIR AI
on: February 14, 2025
Disclaimer: © The authors. All rights reserved. This is a privileged document currently under peer-review/community
review. Authors have provided JMIR Publications with an exclusive license to publish this preprint on it's website for
review purposes only. While the final peer-reviewed paper may be licensed under a CC BY license on publication, at this
stage authors and publisher expressively prohibit redistribution of this draft paper other than for review purposes.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 2 ---

JMIR Preprints
Yesil et al
Table of Contents
Original Manuscript ....................................................................................................................................................................... 5
Supplementary Files ..................................................................................................................................................................... 30
Figures ......................................................................................................................................................................................... 31
Figure 7 ...................................................................................................................................................................................... 32
Figure 8 ...................................................................................................................................................................................... 33
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 3 ---

JMIR Preprints
Yesil et al
Yesil o1 Pro: Evidence-Based AI Model for Health and Benchmarking in
Clinical Decision Support
Yusuf Yesil1 MD, MIS
1 Yesil Health AI Istanbul TR
Corresponding Author:
Yusuf Yesil MD, MIS
Yesil Health AI
Istanbul
Istanbul
TR
Abstract
Background: Integrating evidence-based approaches in healthcare and artificial intelligence (AI) is crucial for enhancing
clinical decision-making and patient safety. Yesil o1 Pro is a specialized large language model (LLM) designed to transform
medical knowledge synthesis by leveraging a comprehensive, curated database of scientific literature, clinical guidelines, and
medical textbooks.
Objective: The system's innovative "AI Hospital" framework employs domain-specific expert agents coordinated by a central
Master Agent, enabling tailored and precise medical responses across multiple disciplines.
Methods: The model's advanced methodology incorporates sophisticated techniques including GraphRAG-based retrieval,
extensive fine-tuning with 1.5 million question-answer pairs, and Chain of Thought (CoT) reasoning. Its robust training dataset
comprises 100.5M words from high-impact journals, 96.8M words from core medical texts, and 74.4M words from international
standards, ensuring a comprehensive and authoritative knowledge base.
Results: Benchmark evaluations demonstrate Yesil o1 Pro's exceptional performance, achieving an overall accuracy of 89.1%
and surpassing leading models like GPT-4o (83.9%) and Claude 3.5 Sonnet (83.0%). Domain-specific accuracies are particularly
impressive, with 96.1% in Mental Health, 94.6% in Epidemiology, and 94.6% in Dentistry, highlighting the model's proficiency
in handling complex, reasoning-intensive medical queries.
Conclusions: The model shows promising applications in clinical decision support, interdisciplinary collaboration, professional
education, and medical research. While challenges remain in real-world integration and maintaining alignment with evolving
medical knowledge, Yesil o1 Pro represents a significant advancement in AI-driven healthcare support.
Future research will focus on validating the model's utility in clinical environments and developing strategies for seamless
healthcare system integration.
(JMIR Preprints 14/02/2025:72646)
DOI: https://doi.org/10.2196/preprints.72646
Preprint Settings
1) Would you like to publish your submitted manuscript as preprint?
Please make my preprint PDF available to anyone at any time (recommended).
Please make my preprint PDF available only to logged-in users; I understand that my title and abstract will remain visible to all users.
Only make the preprint title and abstract visible.
No, I do not wish to publish my submitted manuscript as a preprint.
2) If accepted for publication in a JMIR journal, would you like the PDF to be visible to the public?
Yes, please make my accepted manuscript PDF available to anyone at any time (Recommended). 
Yes, but please make my accepted manuscript PDF available only to logged-in users; I understand that the title and abstract will remain v
Yes, but only make the title and abstract visible (see Important note, above). I understand that if I later pay to participate in  <a href="http
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 4 ---

JMIR Preprints
Yesil et al
No. Please do not make my accepted manuscript PDF available to anyone.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 5 ---

JMIR Preprints
Yesil et al
Original Manuscript
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 6 ---

JMIR Preprints
Yesil et al
Yesil AI: Evidence-Based LLM for Health 
Yusuf Yesil, Yesil Health AI
Abstract
Integrating evidence-based approaches in healthcare and artificial intelligence (AI) is crucial for
enhancing clinical  decision-making and patient  safety. Yesil o1 Pro is  a specialized  large
language model (LLM) designed to transform medical knowledge synthesis by leveraging a
comprehensive,  curated  database  of  scientific  literature,  clinical  guidelines,  and  medical
textbooks. The system's innovative "AI Hospital" framework employs domain-specific expert
agents coordinated by a central Master Agent, enabling tailored and precise medical responses
across multiple disciplines.
The model's advanced methodology incorporates sophisticated techniques including GraphRAG-
based retrieval, extensive fine-tuning with 1.5 million question-answer pairs, and Chain of
Thought (CoT) reasoning. Its robust training dataset comprises 100.5M words from high-impact
journals, 96.8M words from core medical texts, and 74.4M words from international standards,
ensuring a comprehensive and authoritative knowledge base.
Benchmark evaluations demonstrate Yesil o1 Pro's exceptional performance, achieving an overall
accuracy of 89.1% and surpassing leading models like GPT-4o (83.9%) and Claude 3.5 Sonnet
(83.0%). Domain-specific accuracies are particularly impressive, with 96.1% in Mental Health,
94.6% in Epidemiology, and 94.6% in Dentistry, highlighting the model's proficiency in handling
complex, reasoning-intensive medical queries.
The  model  shows  promising  applications  in  clinical  decision  support,  interdisciplinary
collaboration, professional education, and medical research. While challenges remain in real-
world integration and maintaining alignment with evolving medical knowledge, Yesil o1 Pro
represents a significant advancement in AI-driven healthcare support.
Future  research  will  focus  on  validating  the  model's  utility  in  clinical  environments  and
developing strategies for seamless healthcare system integration.
Introduction
Integrating  evidence-based  approaches  is  essential  for  patient  safety  and  effective  clinical
decision-making in the rapidly evolving landscape of health and AI. As medical knowledge
expands  across  multiple  specialties,  healthcare  professionals  face  significant  challenges  in
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 7 ---

JMIR Preprints
Yesil et al
staying up-to-date with the latest research, highlighting the need for robust tools that can synthesize,
analyze, and present the most relevant and timely information.
Large language models (LLMs) typically rely on patterns learned from existing datasets. However,
without direct access to scientific literature and real-time evidence, their responses can lack the
accuracy and relevance required for clinical decision-making. Unlike traditional models, Yesil AI is
designed to go beyond these limitations. It connects directly to a specialized database composed of
scientific literature, clinical guidelines, textbooks, and other authoritative sources, enabling it to
provide evidence-based responses. This capability ensures that the answers generated are grounded
in the latest and most reliable medical knowledge, preventing misinformation and supporting safer,
more effective patient care.
Figure 1: Bridging the Gap: Yesil Al. Illustrates how Yesil Al addresses the limitations of traditional
language models (LLMs) in medicine. By training on a massive database of various specialties with
their knowledge, Yesil Al gains a deeper understanding of each domain. This enhanced knowledge
base allows Yesil Al to provide more accurate and informative responses to queries, bridging the gap
between standard LLMs and specialized medical knowledge.
Advancements in AI have shown immense potential to bridge the gap between vast medical literature
and practical clinical applications. While existing AI systems assist with specific tasks, they often
lack the depth and reasoning required for complex, multi-disciplinary clinical scenarios.  Yesil AI
overcomes this by integrating multiple specialized expert agents, each trained with domain-specific
knowledge, to offer nuanced insights that enhance decision-making and improve patient outcomes.
The intersection of AI and clinical reasoning addresses the unique challenges faced by healthcare
professionals, who must navigate diverse, specialized information sources. 
In Yesil AI, this challenge is met by creating an AI Hospital—a multi-specialty system where each
specialty is dedicated to a specific area of medical expertise. These expert agents are connected to a
unified,  evidence-based  database,  allowing  them  to  generate  contextually  accurate,  up-to-date
responses based on the latest research. This AI Hospital enables healthcare professionals to access
comprehensive, reliable knowledge that supports informed clinical decisions across all specialties.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 8 ---

JMIR Preprints
Yesil et al
Figure  2:  AI  Hospital  -  Specialized  Agent  Network  This  figure  illustrates  the  AI  Hospital
Framework, which utilizes a network of dedicated expert agents specializing in various medical
areas. These agents are trained on extensive scientific literature within their respective domains. A
master agent oversees the system and determines when consultations between specialized agents are
necessary to provide comprehensive patient care.
A comprehensive development approach is necessary to maximize AI's utility in clinical settings.
This includes the creation of specialized  expert agents for each medical specialty, continuous
validation against clinical benchmarks, regular updates  with new evidence, and strong ethical
considerations for AI use. Effective models should not only enhance individual decision-making but
also foster collaboration across different specialties within healthcare teams.
In this paper, we present Yesil AI, an AI Hospital powered by a multi-specialty expert agent system
designed to support clinical decision-making across a wide range of medical fields. Each specialty in
Yesil AI is built using a tailored dataset derived from scientific literature, clinical guidelines, and
relevant medical texts. The system operates through a central Master Agent, which orchestrates the
interaction between the expert agents. When a clinical query is presented, the Master Agent analyzes
the question, identifies which specialties are relevant, and consults the corresponding expert agents.
Each expert agent then generates evidence-based responses grounded in its specialized knowledge.
The  Master  Agent  consolidates  these  responses,  providing  a  final,  informed  decision  that
incorporates multiple perspectives.
Furthermore, Yesil AI can explain its reasoning and decision-making process. For each response, the
system can provide a clear rationale, detailing how it arrived at its conclusion. In addition, the Master
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 9 ---

JMIR Preprints
Yesil et al
Agent can present consultations from other specialties that may be relevant to the clinical question,
providing a more holistic view of the case.
Yesil AI empowers healthcare professionals by providing reliable, up-to-date, and evidence-backed
information across a wide range of medical specialties. By linking specialized knowledge bases and
leveraging the capabilities of expert agents, Yesil AI enhances decision-making, supports accurate
diagnoses, and ultimately improves patient care and clinical outcomes.
Methods
Dataset Development and Curation
The  Yesil  AI’s  foundation  model  is  Yesil  Pro-o1’s  (Yesil  o1  Pro) dataset  was  developed
systematically and rigorously to compile a comprehensive body of medical knowledge across
multiple specialties, derived from diverse, trusted sources. The final dataset comprises millions of
words of specialized medical information, making it one of the most extensive curated collections
across a wide range of medical fields. This dataset integrates information from high-quality, peer-
reviewed  scientific  literature,  clinical  guidelines,  textbooks,  international  standards,  and  other
authoritative resources, ensuring both breadth and depth across multiple medical specialties.
The dataset serves dual purposes: it is utilized for both Graph-RAG  (Graph-Based Retrieval-
Augmented  Generation)  and  fine-tuning  processes.  For  the  fine-tuning  process,  thousands  of
question-answer pairs were meticulously created from this dataset, allowing the Yesil Pro-o1 to learn
and  adapt  to  the  intricacies  of complex  clinical  inquiries  from  a  variety  of  fields,  including
Cardiology, Pediatrics, Endocrinology, Psychiatry, and many others.
The composition of the dataset is as follows:
●
High Impact Journals: 100.5M words
●
Core Medical Textbooks: 96.8M words
●
International Standards: 74.4M words
●
Clinical Guidelines: 60.2M words
●
Specialty References: 56.1M words
●
Clinical Protocols: 55.0M words
●
Meta-analyses: 51.8M words
●
Clinical Trials: 42.7M words
●
Medical Documentation: 38.4M words
●
Quality Control Protocols: 32.7M words
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 10 ---

JMIR Preprints
Yesil et al
Figure 3: A Diverse Knowledge Base: From High-Impact Journals to Quality Control Protocols
GraphRAG for Clinical Applications
We utilize LightRAG (Guo et al., 2024), an advanced framework based on Microsoft’s GraphRAG
(Edge et al., 2024), which enhances graph-based RAG for improved retrieval efficiency. Our
approach customizes GraphRAG with domain-specific modifications tailored to clinical and multi-
specialty medical applications, optimizing its performance for healthcare scenarios (Tsu-Jui et al.,
2019). This allows  Yesil o1 Pro to provide evidence-based, nuanced responses by leveraging
specialized knowledge from diverse medical domains.
Yesil AI leverages a health-specific GraphRAG architecture that excels in text indexing and retrieval
through graph-based structures. Key enhancements include:
●
Specialized Entity Extraction: Focused on extracting terminology and entities specific to
various specialties such as cardiology, oncology, pediatrics, and psychiatry.
●
Recognition of Clinical Parameters: Including biomarkers, clinical parameters, analytical
methods, and diagnostic criteria across specialties.
●
Finding Medical Relationships: Between tests, symptoms, diseases, treatments, and clinical
outcomes, facilitating inter-specialty consultation.
●
Dual-Level Retrieval System: The System efficiently retrieves relevant clinical texts and
research through both local and global searches to support informed decision-making.
●
Context-Aware Search: Prioritizing clinical relevance based on the query’s complexity,
ensuring that responses are clinically accurate and contextually specific.
●
Real-Time Confidence Scoring: For clinical recommendations, enabling the system to
evaluate the relevance and accuracy of responses, enhancing decision-making reliability.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 11 ---

JMIR Preprints
Yesil et al
Figure 4: Workflow for extracting and processing medical knowledge. The diagram illustrates a
multi-step  process  for  converting  raw  medical  knowledge  into  actionable  insights.  It  involves
extracting  relevant  entities  from  medical  text,  mapping  relationships  between  these  entities,
constructing a knowledge graph, selecting the most relevant context, assigning confidence scores to
generated responses, and ultimately providing evidence-based responses. 
To develop a robust and comprehensive knowledge base for  Yesil AI, we conducted an in-depth
analysis of medical specialties by identifying and categorizing entities and their relationships. This
process ensures that the system captures the complexity and interconnectivity of medical knowledge
across diverse fields. Each specialty dataset is structured around two core components:
●
Entities: Specific terms or items, including biomarkers, procedures, or conditions, extracted
from authoritative sources.
●
Relationships: Connections between entities that define how they interact, such as cause-
effect, diagnostic relevance, or treatment pathways.
The entity and relationship counts for each specialty demonstrate the depth and richness of the
knowledge captured. This structured data serves as the foundation for  Yesil AI's multi-specialty
system, enabling:
●
Precise identification of domain-specific terms.
●
The evidence-based reasoning supported by relationships between medical concepts.
●
Seamless integration across specialties to provide holistic, interdisciplinary insights.
The dataset’s balance of depth in established specialties and inclusion of emerging fields ensures that
Yesil o1 Pro remains a comprehensive and adaptive tool for clinical decision-making. Continuous
updates  to  entity  and  relationship  datasets  across  all  specialties  further  enhance  the  system’s
relevance and accuracy in addressing complex medical queries. (Table 1)
Categories
Entities
Relationshi
Categories
Entities
Relationsh
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 12 ---

JMIR Preprints
Yesil et al
p
ip
Allergy
Immunology
42.223
41.403
Neurology
58.899
49.973
Audiology
21.892
17.511
Neuroscience
32.933
20.897
Cardiology
52.423
65.374
Nutrition
25.590
26.691
Critical Care
39.457
36.690
Obstetrics
Gynecology"
55.272
52.051
Dentistry
60.133
51.419
Oncology
87.345
96.609
Dermatology
19.117
16.907
Ophthalmology
11.770
7.385
Elderly Care
53.297
52.945
Orthopedics
64.119
64.184
Emergency
65.049
70.862
Palliative Care
34.050
30.788
Endocrinology
91.886
113.371
Pathology
49.169
45.893
Epidemiology
11.925
9.733
Pediatric Surgery
42.915
36.059
Ethics
7.058
4.689
Pediatrics
103.835
97.591
Fitness Sports
32.545
28.385
Pharmacy
82.718
71.207
Gastroenterology
51.899
52.508
Physical Medicine
and
Rehabilitation
55.416
45.252
General Surgery
61.513
59.723
Preventive
Medicine
54.675
49.929
Genetics
30.082
21.946
Psychiatry
67.921
70.282
Head
 
Neck
Surgery
47.149
44.096
Public Health
20.354
16.522
Health AI
68.979
73.174
Pulmonology
74.857
89.447
Health Economics
22.086
17.335
Radiology
37.110
32.149
Health Education
892
535
Rare Diseases
18.446
6.968
Health
Entrepreneurship
13.682
8.272
Rheumatology
53.365
52.219
Hematology
38.886
38.975
Sleep
14.536
14.359
Hospital
Management
17.028
11.518
Social
 
Media
Addiction
5.153
4.149
Infectious
Diseases
38.352
37.221
Supplements
71.463
66.733
Internal Medicine
83.472
94.368
Vaccination
16.716
14.941
Lab Medicine
78.809
50.264
Wearables
13.208
9.071
Mental Health
27.528
21.012
Wellbeing
16.655
13.213
Microbiology
56.201
39.493
Work Health
10.921
7.736
Table 1: The table provides an overview of the number of entities and relationships identified
within the Yesil AI knowledge base across various medical specialties. 
Unlike traditional methods relying on linear structures, graph-based indexing captures dynamic
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 13 ---

JMIR Preprints
Yesil et al
relationships between entities (Sun et al., 2019), enabling more efficient retrieval of complex clinical
concepts. This interconnected structure helps assess the confidence of retrieved information by
evaluating the quality and relevance of relationships between entities. These adaptations allow for
precise identification of key medical terms and concepts, ensuring that extracted entities are both
accurate and relevant to clinical inquiries. The dual-level retrieval system establishes complex
relationships among symptoms, diseases, treatments, tests, biomarkers, and clinical guidelines.
Figure 5: Knowledge graph visualization of the Endocrinology module.  Illustrates the visual
structure of the GraphRAG knowledge graph, showcasing the extensive data landscape formed by
nodes, edges, and relationships within the system. The full graph view (left) displays the entirety of
the knowledge graph, with densely interconnected nodes that represent various topics and entities in
medicine and related fields. As we zoom in to 100x, individual relationships between nodes become
increasingly visible. These close-up views reveal the detailed linkages and pathways connecting
specific  topics.  The  color-coded  edges  indicate  different  types  of  associations  and  knowledge
pathways, with the line thickness often representing the strength or relevance of the connection
between nodes.
Chain of Thought Reasoning and Explainability
Explainability is a cornerstone of trust in AI-driven healthcare systems. The central Master Agent
employs a Chain of Thought (CoT) reasoning approach to deliver clear, evidence-based responses.
This method systematically breaks down complex queries into logical steps, ensuring accuracy and
transparency. How Yesil AI’s CoT works:
1. The master agent analyzes the query and identifies the relevant medical specialties.
2. It consults the appropriate specialist agents—such as Cardiologist AI, Microbiologist AI,
or Endocrinologist AI—to gather expert insights.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 14 ---

JMIR Preprints
Yesil et al
3. Each specialist agent generates step-by-step responses using its specialized knowledge base.
4. The master agent integrates these insights into a unified, evidence-backed response.
By  coordinating  consultations  between  multiple  Specialist  Agents,  Yesil  AI provides  a
multidisciplinary perspective. The step-by-step reasoning from each specialist, combined into a
comprehensive explanation, makes the decision-making process transparent and easily interpretable
for healthcare professionals.
This combination of CoT reasoning and multi-specialist collaboration ensures that Yesil AI delivers
accurate, explainable, and trustworthy clinical insights.
Figure 6:  Yesil AI's  Consultation  Process.  It begins with Yesil AI analyzing the query and
identifying  relevant  medical  specialties.  These  responses  are  integrated  into  a  comprehensive,
evidence-backed answer. This workflow enhances explainability and trust by leveraging a multi-
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 15 ---

JMIR Preprints
Yesil et al
specialist consultation system to deliver accurate and transparent healthcare insights.
Model Fine-tuning and Optimization
The Yesil AI system is built upon a cutting-edge architecture that integrates fine-tuned LLM models
with a dynamic multi-specialist consultation framework. This architecture builds upon a hybrid
approach, integrating fine-tuning and GraphRAG, with the added functionality of domain-specific
specialist agents to provide tailored responses across medical disciplines. The fine-tuning process for
Yesil o1 Pro employed a carefully curated dataset of 1,562,000 question-answer pairs drawn from
diverse sources, including textbooks, clinical guidelines, peer-reviewed research, and case studies.
The dataset was expanded to incorporate domain-specific complexities, ensuring the model could
address  a wide  array  of medical queries. Key areas  of focus  included  diagnostic strategies,
biomarker interpretation, treatments, clinical guidelines, and interdisciplinary consultation
scenarios. To ensure robustness, fine-tuning followed these optimized specifications:
●
Batch size: 50
●
Learning rate multiplier: 2.0
●
Number of epochs: 2
●
Random seed: 123456
●
Total trained tokens: 1,500,000,000
To enhance performance, Yesil o1 Pro employs a modified RAG framework, dynamically retrieving
context-specific knowledge from a proprietary medical database. This system enables the master
agent to identify relevant specialties for complex queries and engage domain-specific specialist
agents.  These  agents  collaboratively  analyze  the  query,  leveraging  their  expertise  to  generate
cohesive, interdisciplinary responses. Specialist agents provide clear, step-by-step rationales for their
conclusions, enhancing trust and usability in clinical environments. Evaluation using an expanded
benchmark  covering  all  specialties  demonstrated  superior  performance,  with  significant
improvements in accuracy and relevance over single-model systems.
Model Performance
To ensure the robustness and accuracy of Yesil o1 Pro as a multi-specialist consultation system, we
developed  a  comprehensive  benchmarking  dataset  spanning  multiple  medical  disciplines.  This
dataset  evaluates  the  AI's  performance  across  a  diverse  range  of  specialties,  encompassing
foundational knowledge, clinical expertise, and cutting-edge research. While the dataset includes
over 50 specialties such as Dermatology, Cardiology, Pediatrics, Oncology, and Mental Health, the
question count per specialty varies to ensure depth and focus on the most critical areas.
The dataset was crafted using trusted, open-access medical literature and incorporates the latest
advancements across disciplines, ensuring a challenging and informative benchmark. Some questions
were derived from peer-reviewed article abstracts, lending additional credibility to the dataset.
This benchmarking dataset is freely accessible to the public, empowering researchers and developers
to evaluate and benchmark language models in multi-specialist healthcare settings. By sharing this
resource, we aim to enhance the development of AI systems that can assist in multidisciplinary
medical decision-making, ultimately improving patient care and outcomes.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 16 ---

JMIR Preprints
Yesil et al
Performance Analysis
The benchmarking results for Yesil o1 Pro highlight its exceptional performance as a multi-specialist
consultation system, surpassing or matching leading LLMs across various medical domains. The
evaluations  used  a  robust,  domain-specific  dataset,  ensuring  the  results  reflect  real-world
applicability in diverse healthcare settings.
Yesil o1 Pro consistently achieved the highest or near-highest accuracy across key categories. For
example,  the  model  reached  an  outstanding  96.1% in  Mental  Health,  outperforming  GPT-4o
(92.6%)  and  Claude  3.5  Sonnet  (92.6%).  Similarly,  in  Epidemiology,  it  achieved  94.6%,
showcasing  its  strength  in  evidence-based,  data-driven  decision-making  for  public  health
applications. These results underscore the system’s capability to handle reasoning-intensive queries
effectively.
In specialized areas such as  Dentistry (94.6%),  Ethics (93.5%), and  Social Media Addiction
(93.6%), Yesil o1 Pro demonstrated remarkable accuracy, highlighting its adaptability across a broad
spectrum of medical topics. Notably, its performance in Allergy Immunology (91.0%) and Elderly
Care (91.9%) reinforces its utility in fields requiring nuanced, patient-centered insights.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 17 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
Figure 7. Accuracy of Different LLMs Across Medical Specialties
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 18 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
The overall accuracy results underscore  Yesil o1 Pro's exceptional performance compared to
leading LLMs across a wide range of medical specialties. With an impressive 89.1% overall
accuracy, Yesil o1 Pro significantly outperforms its competitors, cementing its position as a
state-of-the-art multi-specialist consultation system for healthcare applications. 
Among the baseline models, GPT-4o achieves a respectable 83.9%, closely followed by GPT-
o1-preview (83.3%), Claude 3.5 Sonnet (83.0%), and Deepseek R1 70B (82.6%). These results
highlight the strong performance of general-purpose LLMs when applied to medical datasets.
The results validate Yesil o1 Pro's hybrid approach of leveraging fine-tuning, RAG, and CoT
reasoning to deliver precise, evidence-based outputs. Its ability to outperform even high-capacity
models like GPT-o1-preview, Claude 3.5, and Deepseek R1 70B illustrates the value of its multi-
specialist framework in bridging the gap between general-purpose AI and real-world healthcare
needs.
Yesil  o1  mini,  designed  for  environments  with  limited  computational  resources,  delivers
remarkable performance considering its streamlined architecture. While optimized for efficiency,
it maintains robust accuracy across specialties, achieving an impressive  accuracy of 85.1%.
Yesil o1 Mini is a testament to delivering top-tier performance efficiently, making it an ideal
choice for users requiring a compact yet powerful solution.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 19 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
Figure 8. The average accuracy of LLMs
Yesil o1 Pro is the premier multi-specialist healthcare consultation system, combining precision,
adaptability, and cutting-edge technology to set a new benchmark for LLM performance in
medicine. Yesil o1 Mini offers an excellent alternative for users prioritizing efficiency without
compromising  accuracy,  maintaining  strong  performance  across  diverse  medical  domains.
Together, these models showcase the transformative potential of AI in healthcare, catering to a
wide range of applications and needs.
Discussion
The comparative analysis of various language models in medical applications highlights the
strengths of Yesil AI as a multi-specialist consultation system. By leveraging a hybrid approach
that integrates fine-tuning, RAG, and CoT reasoning, Yesil AI delivers precise, evidence-based,
and interdisciplinary insights tailored to healthcare professionals' needs.
Yesil AI's unique architecture allows it to serve as a transformative tool in healthcare. The
system's ability to consult specialist agents—such as Cardiologist AI, Infectious Diseases AI, or
Oncology AI—ensures that even complex queries receive integrated and holistic responses. This
approach enhances decision-making in cases that require expertise from multiple domains, such
as managing cardiovascular risks in diabetic patients or evaluating biomarkers for cancer.
In addition to supporting clinical decision-making, Yesil AI excels at staying current with the
latest research. Through its RAG framework, it continuously integrates findings from peer-
reviewed studies, clinical guidelines, and treatment protocols. This  ensures  that healthcare
providers have access to the most up-to-date evidence, reinforcing evidence-based practices and
promoting continuous professional learning.
A notable strength of Yesil AI is its ability to integrate real-time research updates into its
responses,  especially  in  fast-evolving  fields  like  oncology  and  infectious  diseases.  This
functionality addresses the challenge healthcare professionals face in keeping pace with an
expanding body of clinical knowledge, ensuring that clinicians can make informed decisions
based on the latest scientific developments.
Moreover,  Yesil  AI  fosters  interdisciplinary  collaboration  by  delivering  cohesive,  domain-
specific insights that break down silos between specialties. In complex scenarios—such as
managing patients with multiple comorbidities or rare diseases—this integrated approach enables
seamless collaboration across specialties, ultimately improving patient management, reducing
medical errors, and enhancing overall care quality.
Model Size Considerations
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 20 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
Yesil AI, based on GPT-4o, is a high-performance model that outperforms several other leading
models  in  terms  of  accuracy  and effectiveness,  as  demonstrated  by  its  impressive  89.2%
performance. While GPT-4o-based models like Yesil AI are on the larger end of the spectrum,
their size is strategically optimized to deliver superior results in complex healthcare scenarios.
Despite being larger than some other models, such as GPT-o1-preview, Yesil AI's architecture
ensures that the benefits of a larger model, such as the ability to process and integrate vast
amounts of medical data, are fully leveraged.
In comparison to models like GPT-o1-mini and GPT-4o mini, Yesil AI strikes a balance between
performance and efficiency. Models like Llama 3.3 70B, Llama 3.2 90B Vision, and Gemini 2.0
offer competitive results but still fall short of Yesil AI’s precision, which can be attributed to its
specialized training for healthcare applications. The hybrid approach used in Yesil AI further
enhances its ability to deliver domain-specific, evidence-based insights while maintaining model
size optimization.
Possible Applications of Yesil AI
Yesil  AI's  multi-specialist  consultation  framework  offers  transformative  applications  in
healthcare, addressing a wide range of medical domains:
1. Decision
 
Support
Yesil AI provides timely, evidence-based insights that enhance clinical decision-making.
By integrating multidisciplinary perspectives, it empowers professionals to analyze data
efficiently, leading to improved patient outcomes. For instance, its ability to synthesize
insights  from  Cardiologist  AI and  Endocrinologist  AI enables  comprehensive
evaluations in complex cases such as cardiovascular risk assessment in diabetic patients.
2. Staying
 
Up-to-date
 
with
 
Research
By leveraging RAG, Yesil AI integrates the latest findings from scientific literature,
ensuring  that  healthcare  providers  remain  informed  about  emerging  trends  and
breakthroughs. This supports evidence-based practice and fosters continuous professional
development.
3. Interdisciplinary
 
Collaboration
Yesil  AI's  ability  to  consult  specialist  agents  across  domains  enables  seamless
interdisciplinary collaboration. For example, a query involving Infectious Diseases and
Pulmonology can yield cohesive, integrated insights, critical for managing complex
conditions like COVID-19 or multi-system infections.
4. Research
 
and
 
Innovation
Yesil AI's data-driven insights can identify knowledge gaps and suggest new research
directions. For example, analyzing patterns in biomarker performance may lead to the
development of innovative diagnostic tools or therapies.
5. Training
 
and
 
Education
Yesil AI serves as an educational resource, offering interactive scenarios, quizzes, and
case studies for medical students and professionals. Its ability to simulate real-world
clinical challenges prepares users for complex decision-making scenarios.
Limitations
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 21 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
While Yesil AI demonstrates impressive performance, several limitations should be considered:
1. Benchmark Scope: The evaluation metrics used in testing Yesil AI may not fully capture
all aspects of real-world medical practice, particularly in specialized or niche clinical
settings. This could result in overlooked challenges that may arise in dynamic, patient-
facing environments where context, human interaction, and non-textual data play a
significant role in decision-making.
2. Dynamic Nature of Healthcare: The field of healthcare is continuously evolving, with
new research, treatments, and clinical practices emerging regularly. To maintain its
relevance and performance, Yesil AI requires ongoing updates and re-training to ensure it
reflects the latest advancements in medical knowledge and practice. Regular model
updates are essential to keeping the AI aligned with rapidly changing healthcare needs.
3. Clinical Integration: While Yesil AI is designed to provide valuable decision support,
further research is needed to assess its effectiveness and accuracy in real-world clinical
environments. The integration of AI models into existing clinical workflows introduces
unique complexities that could impact performance, such as varying standards of care,
clinician expertise, and access to data.
4. User Feedback and Continuous Improvement: To optimize its clinical relevance, we
encourage collaboration with healthcare professionals, researchers, and clinical experts.
Real-world testing and feedback are crucial in identifying areas for improvement and
refining the model to better address clinical challenges. Their input will help ensure that
Yesil AI evolves to meet the diverse needs of healthcare providers and remains a reliable
tool for evidence-based decision-making.
Our goal is to conduct extensive application testing in clinical settings to gather insights into the
model’s usability, effectiveness, and potential barriers to implementation. This process will
provide valuable guidance for enhancing Yesil AI's practical application in healthcare, ensuring
its continued development and successful integration into clinical workflows.
Future Research Directions
Future research for Yesil AI should focus on several key areas to enhance its applicability and
effectiveness in healthcare settings. First and foremost,  real-world validation is essential.
Conducting studies within clinical environments will allow for the verification of Yesil AI's
performance in practice, ensuring that it delivers reliable, accurate results in dynamic, real-world
scenarios.
Secondly,  there  is  a  need  to develop  frameworks  for integrating Yesil  AI into  existing
healthcare information systems. This will involve creating standardized processes for seamless
deployment  across  diverse  clinical  settings,  ensuring  the  AI  system  can  be  effectively
incorporated into existing workflows without disruption.
Additionally, comprehensive error analyses should be conducted to identify areas where Yesil
AI  may  underperform  or  generate  inaccurate  outputs.  By  understanding  these  limitations,
researchers can refine the model, enhancing its accuracy and reliability over time.
Overall,  these  efforts  underscore  the  potential  of  specialized  AI  models  like  Yesil  AI  in
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 22 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
advancing clinical decision-making. Continued research, development, and validation are crucial
for realizing the full potential of Yesil AI and ensuring its long-term effectiveness in improving
patient  care,  supporting  interdisciplinary  collaboration,  and  keeping  healthcare  providers
informed with the most up-to-date medical knowledge.
Conclusion
The development and evaluation of Yesil AI mark a significant step forward in the integration of
large  language  models  into  health  applications.  By  leveraging  a  hybrid  approach  that
incorporates  fine-tuning,  RAG,  and  CoT  reasoning,  Yesil  AI  outperforms  general-purpose
models,  demonstrating  its  superior  capability  in  providing  precise,  evidence-based,  and
interdisciplinary insights for healthcare professionals. One of the key benefits of Yesil AI is its
multi-specialist  consultation  system,  which  allows  it  to  consult  specialist  agents  ensuring
comprehensive  and  holistic  responses  to  complex  queries.  This  interdisciplinary  approach
enhances clinical decision-making by integrating perspectives from multiple medical domains,
ultimately improving patient outcomes, especially in cases involving comorbidities or requiring
expertise from various specialties.
Our findings highlight the importance of specialized architectures and domain-specific training
in optimizing AI models for healthcare applications. Yesil AI's unique design, combined with its
ongoing updates through RAG and CoT reasoning, ensures that it remains aligned with the latest
research and clinical guidelines, thereby supporting evidence-based practices and fostering
continuous  learning.  The  system's  performance  in  staying  up-to-date  with  recent  medical
developments further underscores its potential to revolutionize healthcare decision support.
However, the path forward requires a balanced approach that considers both technological
innovation and real-world implementation. While  Yesil Pro-o1 shows promising results in
benchmark testing, its integration into clinical environments must be carried out with careful
attention to quality control, safety protocols, and regulatory compliance. Ongoing development
must  prioritize  not  only  performance  metrics  but  also  reliability,  transparency,  and
reproducibility to ensure its trustworthiness and clinical relevance.
As  healthcare  continues  to  evolve,  systems  like  Yesil  AI  have  the  potential  to  become
indispensable tools  for clinicians, assisting  in both routine decision support and complex,
interdisciplinary cases. By maintaining a responsible and evidence-based approach, we can
ensure that AI systems like Yesil AI effectively enhance medical practices, ultimately improving
patient care and outcomes.
Data Availability
The benchmark datasets used for evaluating Yesil AI's performance across various healthcare
domains will be made publicly available through our project repository. These datasets provide a
foundation for researchers to reproduce results and compare Yesil AI's performance with other
models. The dataset is accessible via our project’s Huggingface profile.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 23 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
Note: The training dataset, fine-tuning question-answer pairs, and other proprietary materials
used in the development of Yesil AI will remain confidential and are not included in this public
release.
Code Availability
Yesil AI is currently available on its website. Interested researchers and healthcare providers are
encouraged to try via API contact us (hello@yesilhealth.com) for access to the model. We are
collaborating with research institutions, regulatory bodies, and healthcare providers to validate
Yesil AI and explore safe and effective implementations in clinical settings.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 24 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
References
Younis HA, Eisa TAE, Nasser M, Sahib TM, Noor AA, Alyasiri OM, Salisu S, Hayder IM,
Younis HA. A Systematic Review and Meta-Analysis of Artificial Intelligence Tools in Medicine
and  Healthcare:  Applications,  Considerations,  Limitations,  Motivation  and  Challenges.
Diagnostics  (Basel).  2024  Jan  4;14(1):109.  doi:  10.3390/diagnostics14010109.  PMID:
38201418; PMCID: PMC10802884.
Amin K, Doshi R, Forman HP. Large language models as a source of health information: Are
they patient-centered? A longitudinal analysis. Healthc (Amst). 2024 Mar;12(1):100731. doi:
10.1016/j.hjdsi.2023.100731. Epub 2023 Dec 22. PMID: 38141269.
Sun C, Gong Y, Yuanbin W, et al. (eds). Joint type inference on entities and relations via graph
convolutional networks. In: Proceedings of the 57th Annual Meeting of the Association for
Computational  Linguistics,  2019,  1361–70,  Florence,  Italy.  Association  for  Computational
Linguistics.
Tsu-Jui F, Li P-H, Ma W-Y. Graphrel: Modeling text as relational graphs for joint entity and
relation  extraction.  In:  Proceedings  of  the  57th  Annual  Meeting  of  the  Association  for
Computational  Linguistics,  2019,  1409–18,  Florence,  Italy.  Association  for  Computational
Linguistics
Guo, Z., Xia, L., Yu, Y., Ao, T., & Huang, C. (2024). LightRAG: Simple and Fast Retrieval-
Augmented Generation. arXiv. https://arxiv.org/abs/2410.05779
Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., & Larson, J. (2024).
From Local to Global: A Graph RAG Approach to Query-Focused Summarization. arXiv. https://
arxiv.org/abs/2404.16130
Gemini Team et al. (2024). Gemini 1.5: Unlocking multimodal understanding across millions of
tokens of context. arXiv:2403.05530. Available at: https://arxiv.org/abs/2403.05530
Anthropic (2024). Claude 3.5. Available at: https://www.anthropic.com/news/claude-3-5-sonnet
Meta  (2024).  LLaMA  3.2:  Connect  2024  vision  to  edge  mobile  devices.  Available  at:
https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/
OpenAI et al. (2024). GPT-4 Technical Report. arXiv:2303.08774. Available at: https://arxiv.org/
abs/2303.08774
Yesil
 
Health
 
Benchmark
 
Dataset.
 
Available
 
at:
https://huggingface.co/datasets/yesilhealth/Health_Benchmarks
Yesil
 
Health
 
AI
 
website.
 
Available
 
at:
https://yesilhealth.com
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 25 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
Appendix
Appendix
 
1:
 
Case
 
study
 
-
 
Biomarkers
 
for
 
Diabetes
 
Mellitus
Question: What are the primary biomarkers for diagnosing diabetes mellitus, and how do they differ
from those used in monitoring the condition?
⬇
Sources retrieve and summary:
●Source 1 Summary: This source provides an overview of diabetes mellitus, covering the
American Diabetes Association (ADA) diagnostic criteria, including fasting plasma glucose
(FPG) of 126 mg/dL or higher, casual plasma glucose of 200 mg/dL with symptoms, and
HbA1c of 6.5% or higher. It also describes "prediabetes" and mentions that gestational
diabetes screening is specific to pregnancy with glucose tolerance tests.
●Source 2 Summary: This source discusses devices and techniques for diabetes monitoring,
emphasizing the role of home blood glucose monitors and continuous glucose monitoring
(CGM) systems, including their accuracy, limitations, and how they supplement traditional
glucose tests by providing real-time trends.
⬇
Reasoning:
●Step
 
1:
 Understanding
 
the
 
Key
 
Question
To answer the question, it's necessary to first identify which biomarkers diagnose diabetes and
then differentiate these from the ones used for monitoring. This approach ensures a clear,
comprehensive answer that addresses both diagnosis and ongoing management.
●Step  2:
 Providing  Diagnostic  Biomarkers  in  a  Logical  Sequence
The answer begins with diagnostic biomarkers (FPG, HbA1c, OGTT) in a structured order,
establishing the foundational markers used to confirm diabetes and explaining each marker’s
specific role.
●Step
 
3:
 Explaining
 
Each
 
Diagnostic
 
Biomarker’s
 
Purpose
Each diagnostic biomarker is detailed to show why it’s important for diagnosis. This includes
what each test measures and its threshold for diagnosing diabetes, illustrating the unique role
of each test in confirming the condition.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 26 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
●Step
 
4:
 Introducing
 
Monitoring
 
Biomarkers
After the diagnostic biomarkers, the answer shifts focus to the biomarkers used for monitoring
diabetes. This transition clarifies that monitoring biomarkers serve a different purpose—
managing diabetes over time rather than diagnosing it.
●Step
 
5:
 Describing
 
Each
 
Monitoring
 
Biomarker’s
 
Role
Each monitoring tool (HbA1c, SMBG, CGM) is described to show how it supports ongoing
glucose  management.  The  distinct  roles  of  immediate  feedback,  long-term  trends,  and
continuous monitoring are highlighted, providing insight into daily diabetes management.
●Step  6:  Highlighting  the  Key  Difference  Between  Diagnosis  and  Monitoring
To complete the response, the answer summarizes the primary distinction between diagnostic
and  monitoring  biomarkers.  Diagnostic  tools  identify  diabetes  at  a  single  point,  while
monitoring tools guide treatment over time, concluding with a clear differentiation.
⬇
Answer:
The primary biomarkers for diagnosing diabetes mellitus include fasting plasma glucose (FPG),
hemoglobin A1c (HbA1c), and the oral glucose tolerance test (OGTT), each serving a specific
purpose:
1. Fasting Plasma Glucose (FPG): Measures blood glucose after an 8-hour fast. A level of 126
mg/dL or higher (on two occasions) indicates diabetes, focusing on the body’s fasting glucose
regulation.
2. Hemoglobin A1c (HbA1c): Reflects average glucose over the past 2-3 months. A level of
6.5% or higher (on two occasions) indicates diabetes, providing a long-term glucose overview
instead of a single snapshot.
3. Oral  Glucose  Tolerance  Test  (OGTT):  Used  when  FPG  or  random  glucose  tests  are
inconclusive. Measures blood glucose before and 2 hours after a glucose load (75 g). A 2-hour
level of 200 mg/dL or higher confirms diabetes, testing the body’s glucose processing ability.
In contrast, monitoring biomarkers include:
1. Continued use of HbA1c: Monitors long-term glucose control, with a target usually under
7% for effective management.
2. Self-Monitoring of Blood Glucose (SMBG): Allows patients to track daily fluctuations using
glucometers, adjusting diets and insulin as needed.
3. Continuous Glucose Monitoring (CGM): Provides real-time glucose trends throughout the
day, helping to adjust treatment proactively.
Key Difference: Diagnostic biomarkers (FPG, HbA1c, OGTT) confirm diabetes at a specific point,
while monitoring biomarkers focus on ongoing management and treatment adjustments.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 27 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
Confidence Score: 9
Appendix
 
2:
 Table
 
of
 
example
 
Q&A
 
from
 
fine-tuning
 
dataset
Q: What are the implications of preanalytical variables on laboratory test results?
A: Preanalytical variables refer to factors that can affect laboratory test results before the actual
analysis occurs. These variables can significantly impact the accuracy and reliability of test outcomes,
leading  to  potential  misdiagnosis  or  inappropriate  treatment.  Key implications  of  preanalytical
variables include:
1. Sample Collection: The method of sample collection (e.g., venipuncture, capillary sampling) can
influence test results. Factors such as the site of collection, the use of tourniquets, and the timing of
collection (e.g., fasting vs. non-fasting) can introduce variability.
2. Sample Handling and Transport: Improper handling, storage, or transport of samples can lead to
degradation or contamination. For example, delays in processing or exposure to extreme temperatures
can affect the stability of certain analytes, resulting in inaccurate results.
3.  Patient  Factors:  Individual  patient  characteristics,  such  as  age,  sex,  hydration  status,  and
medications, can influence laboratory results. For instance, certain medications may interfere with
specific tests, leading to false positives or negatives.
4. Timing of Collection: The timing of sample collection about the patient's physiological state (e.g.,
circadian rhythms, postprandial state) can affect the concentration of analytes. For example, hormone
levels may vary throughout the day, necessitating careful timing for accurate assessment.
5. Equipment and Supplies: The quality and type of collection devices, tubes, and reagents used can
impact test results. For instance, using the wrong type of anticoagulant can alter coagulation test
outcomes.
6. Standardization: Lack of standardization in preanalytical processes across different laboratories can
lead to variability in results, making it challenging to compare findings or establish reference ranges.
To  mitigate  the  impact  of  preanalytical  variables,  laboratories  should  implement  standardized
protocols for sample collection, handling, and processing. Training for healthcare providers on proper
sample collection techniques and awareness of factors that can influence results is also essential. By
addressing preanalytical variables, laboratories can enhance the accuracy and reliability of test
results, ultimately improving patient care.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 28 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
Appendix 3: Figure - Example of a mapped entity
●Entity: Alanine Aminotransferase (ALT)
○Description: "Alanine Aminotransferase (ALT) is an enzyme used as an important
indicator for liver health, being a principal biomarker for liver disease."
○Related Data Points:
■
Indication of liver damage or inflammation when elevated.
■
Its levels can indicate liver or pancreatic disease.
■
Measured to assess liver health and function, with specific variability metrics
reported.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 29 ---

JMIR Preprints
Yesil et al
Yesil AI: An Evidence-Based LLM Specialized in Health
Appendix 4: Figure - Confidence Scoring Process for Contextual Answers
Figure: Confidence Scoring Process for Contextual Answers.  The figure depicts a pipeline for
assessing the reliability of AI-generated responses. It starts by retrieving relevant information, then
evaluates its relevance to the query. Next, it calculates a confidence score based on the relevance and
reasoning applied, providing a contextual answer with an associated level of certainty. Finally, it
applies chain-of-thought reasoning to generate a contextual answer.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 30 ---

JMIR Preprints
Yesil et al
Supplementary Files
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 31 ---

JMIR Preprints
Yesil et al
Figures
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 32 ---

JMIR Preprints
Yesil et al
Comparison of LLMs in healthcare applications.
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

--- Page 33 ---

JMIR Preprints
Yesil et al
The average accuracy of LLMs.
Powered by TCPDF (www.tcpdf.org)
https://preprints.jmir.org/preprint/72646
[unpublished, non-peer-reviewed preprint]

```
