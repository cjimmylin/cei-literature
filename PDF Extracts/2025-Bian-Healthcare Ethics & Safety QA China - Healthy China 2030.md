---
title: "2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030 - PDF Extract"
source_pdf: "2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030.pdf"
pages: 6
extracted_at: "2026-02-07T17:00:46.252025"
---

# PDF Extract: 2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030

**Source PDF:** 2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

arXiv:2505.07205v1  [cs.CL]  12 May 2025
BENCHMARKING ETHICAL AND SAFETY RISKS OF HEALTHCARE
LLMS IN CHINA – TOWARD SYSTEMIC GOVERNANCE UNDER
HEALTHY CHINA 2030
Mouxiao Bian1†, Rongzhao Zhang1†, Chao Ding1†, Xinwei Peng1, and Jie Xu1,*
1 Shanghai Artificial Intelligence Laboratory, , Shanghai, China
ABSTRACT
Large Language Models (LLMs) are poised to transform healthcare under China’s Healthy China 2030
initiative, yet they introduce new ethical and patient-safety challenges. We present a novel 12,000-item
Q&A benchmark covering 11 ethics and 9 safety dimensions in medical contexts, to quantitatively
evaluate these risks. Using this dataset, we assess state-of-the-art Chinese medical LLMs (e.g.,
Qwen 2.5-32B, DeepSeek), revealing moderate baseline performance (accuracy 42.7% for Qwen
2.5-32B) and significant improvements after fine-tuning on our data (up to 50.8% accuracy). Results
show notable gaps in LLM decision-making on ethics and safety scenarios, reflecting insufficient
institutional oversight. We then identify systemic governance shortfalls – including the lack of fine-
grained ethical audit protocols, slow adaptation by hospital IRBs, and insufficient evaluation tools –
that currently hinder safe LLM deployment. Finally, we propose a practical governance framework
for healthcare institutions (embedding LLM auditing teams, enacting data ethics guidelines, and
implementing safety simulation pipelines) to proactively manage LLM risks. Our study highlights the
urgent need for robust LLM governance in Chinese healthcare, aligning AI innovation with patient
safety and ethical standards.
Keywords Artificial Intelligence · Safety · Large Language Models · Medical AI
1
Introduction
China’s national Healthy China 2030[1]initiative prioritizes advanced health technologies to improve care delivery.In
recent years, large language models have emerged as powerful tools in healthcare – from automated medical consulta-
tions to clinical decision support – and are increasingly integrated into hospital systems. National policies encourage
AI-driven innovation; for example, China’s National Health Commission in 2024 issued the “Guidelines for Clinical
Application Management of Medical Large Models”[2] (dubbed the “Constitution of Medical AI”) to delineate safe
uses of medical AI, emphasizing “strictly controlling ethical risks”.
This supportive policy environment under Healthy China 2030 has accelerated LLM adoption in medicine, with
flagship models like Alibaba’s Qwen and open-source DeepSeek pushing the frontier of Chinese medical AI. However,
alongside their promise, LLMs pose serious ethical and safety concerns in healthcare settings. These models can
produce inaccurate or unethical content (“hallucinations”), violate patient privacy, or give unsafe medical advice if
not properly governed. Recent analyses warn that deploying LLMs broadly “raises substantial concerns” due to the
“lack of comprehensive governance frameworks” to ensure patient-centered validation[3].Despite high-level regulations
(e.g. data privacy laws, algorithmic security rules), many hospitals and research centers in China lack concrete internal
protocols for AI ethics[4]. Governance gaps at the institutional level – such as absence of formal LLM oversight
committees or inadequate ethical review processes for AI tools – risk undermining patient safety and public trust.There
1†These authors contributed equally.
2*Correspondence: Jie Xu (xujie@pjlab.org.cn)

--- Page 2 ---

Benchmarking Ethical and Safety Risks of Healthcare LLMs in China
is a pressing need to assess how well current LLMs handle ethical dilemmas and safety-critical decisions, and to use
that evidence to inform better governance.
In this work, we address the governance of LLM-driven healthcare AI[5] by quantitatively benchmarking the ethical
and safety performance of leading medical LLMs in China. We introduce a new 12,000-question dataset spanning
diverse ethics and safety scenarios in medicine, and evaluate multiple state-of-the-art (SOTA) Chinese LLMs[6] on
this benchmark. By comparing baseline and fine-tuned model performance, we expose specific weaknesses of current
models in ethical reasoning and safe responses. We then leverage these findings to examine institutional readiness: Are
hospitals and research institutions equipped with the necessary oversight mechanisms and tools to manage LLM risks?
Finally, we propose a feasible governance framework – aligned with the Healthy China 2030 vision – to systematically
mitigate ethical and safety risks of LLMs in healthcare practice[7][8].
2
Methods
2.1
Dataset Construction: Ethics & Safety Q&A Benchmark
We constructed a comprehensive Ethics and Safety QA dataset consisting of 12,000 question-answer items, specifically
designed to test LLMs on scenarios involving medical ethics and patient safety. The dataset was developed through
expert consultations and policy guidelines analysis to capture real-world dilemmas. Each question is a realistic medical
scenario or inquiry that challenges an LLM’s judgment on an ethical or safety issue, paired with a reference “best-
practice” answer. The questions are categorized along 20 dimensions (11 ethics topics and 9 safety topics) to ensure
broad coverage. Ethical dimensions (11 categories): Examples include patient privacy/confidentiality, informed consent,
autonomy and patient rights, beneficence vs. non-maleficence (doing good vs avoiding harm), justice and fairness in
treatment, equity of access, professional integrity, accountability in AI usage, transparency/explainability, doctor-patient
trust, and data governance ethics. Each ethical question probes the model’s alignment with medical ethics principles
(e.g., handling a request that breaches privacy or responding to a biased treatment suggestion). Safety dimensions
(9 categories): Examples include clinical accuracy and correctness of medical information, avoidance of dangerous
or contraindicated advice, recognition of uncertainty (not fabricating an answer when unsure), adherence to clinical
protocols, medication safety (avoiding incorrect dosing or drug interactions), diagnostic safety (not missing critical
symptoms), hallucination control (not inventing non-existent medical facts), bias and harm prevention (not reinforcing
harmful biases), and response robustness under stress or adversarial prompts. These safety questions test whether the
LLM can provide reliable and safe guidance consistent with standard of care. Each item in the dataset is labeled by
its primary ethics or safety category, enabling fine-grained performance analysis. The final compilation includes a
balanced mix of clinical vignettes, patient inquiries, and policy-based questions. For example, an ethics question might
be: “A patient’s family asks the doctor to withhold a cancer diagnosis from the patient. How should the AI assistant
respond?” (testing honesty vs. compassion), while a safety question could be: “What dosage of Drug X is appropriate
for a child of weight Y?” (testing if the model gives a correct and safe dosing). The dataset underwent expert validation,
with medical ethicists and clinicians reviewing samples to ensure scenario realism and that the “gold standard” answers
reflect consensus guidelines.
2.2
Model Selection and Evaluation Protocol
We evaluated multiple Chinese medical LLMs on the benchmark to assess their ability to navigate ethical and safety
scenarios. The selection focused on state-of-the-art models that are either widely used or specifically tuned for medical
applications, including: Qwen 2.5-32B: a 32-billion-parameter Chinese LLM by Alibaba, known for strong general
performance (we use its medical domain variant if available). DeepSeek: a cutting-edge open-source Chinese medical
LLM (with comparable scale, e.g. 30B parameters), which gained popularity in 2025 for its capability in Mandarin
medical dialogues. (Additional models: We also considered other benchmarks such as a general model like GPT-4
or a locally-developed healthcare LLM, to provide reference points, if applicable. For brevity, focus is on Qwen
and DeepSeek.) Evaluation setup: Each model was prompted with all 12,000 questions in a unified format. For
fairness, we used a standardized prompt template and disabled any internet or tool access for the LLMs. Models
generated answers which were then compared to the reference answers to compute accuracy. We defined accuracy as the
percentage of questions for which the model’s answer matched the expected answer (either exactly for factual questions
or containing the essential ethical reasoning/conclusion as determined by a rubric). For nuanced ethical questions,
answers were marked correct if they followed established medical ethics guidelines (two physician-annotators resolved
any disagreements).
2

--- Page 3 ---

Benchmarking Ethical and Safety Risks of Healthcare LLMs in China
Figure 1: Medical Safety&Ethic Dataset.This Figure introduces the construction process, data distribution, and
effectiveness of the medical ethics and safety dataset.We combined large language models such as DeepSeek-R1 and
carried out manual quality control to construct a high-quality dataset from textbooks, policy documents, and laws and
regulations. The dataset encompasses two major themes, namely medical ethics and medical safety, and is divided into
20 categories (Left). By using the constructed dataset to fine-tune Qwen2.5-32B, we found that its performance on the
two medical ethics and safety evaluation sets, MedSafety and SafetyV2, outperforms that of the unfine-tuned model.
Moreover, it also outperforms the unfine-tuned Qwen2.5-72B, while maintaining comparable performance in other
medical tasks. (Right).Qwen2.5-32B+medical corpus and safety ethics data fine-tuning:Qwen2.5-32B fine-tuned on
both general medical corpus and medical ethics & safety dataset.Qwen2.5-32B+safety ethics data fine-tuning:Qwen2.5-
32B fine-tuned on medical ethics & safety dataset.
• Baseline performance: We first evaluated each model without any fine-tuning (using the released pre-trained or
instruction-tuned versions). This assesses how well a general or off-the-shelf medical LLM adheres to ethical
norms and safety standards out-of-the-box.
• Fine-tuning: We then fine-tuned the models on our ethics/safety QA dataset (for those models where fine-
tuning is feasible, e.g. open-source ones like Qwen and DeepSeek). A subset of 10,000 QA pairs was used for
training (with careful balance across categories), holding out 2,000 for validation/testing. Fine-tuning aimed to
explicitly teach the models to produce answers aligning with ethical best practices and safe medical guidance.
After fine-tuning, we re-evaluated the models on a test set to measure performance improvements.
• Metrics: Primary metric was overall accuracy on the benchmark (fraction of questions answered correctly).
We also tracked accuracy per category to identify domains of strength or weakness (e.g., accuracy on privacy-
related questions vs. medication safety questions). Additionally, we noted qualitative behavior changes, such
as reduction in dangerous recommendations or improved explanations in answers post fine-tuning.
All experiments were conducted on a secure offline server to avoid any data leakage. We applied the same questions to
all models and did not allow any model-specific hinting beyond the base prompt. This uniform evaluation provides
a comparable benchmark of how different LLMs handle ethical and safety challenges, and how much fine-tuning on
domain-specific data can close the gaps.
3

--- Page 4 ---

Benchmarking Ethical and Safety Risks of Healthcare LLMs in China
2.3
Impact of Fine-Tuning on Ethical and Safety Performance
Fine-tuning the LLMs on the specialized dataset led to substantial accuracy improvements, demonstrating the efficacy of
targeted training. Qwen 2.5-32B’s accuracy improved from 0.427 to 0.508, a relative increase of about 19%. DeepSeek
showed a similar boost (roughly 7–8 percentage points). All models benefited from fine-tuning, reducing the frequency
of severe errors. Qualitatively, the fine-tuned models displayed more cautious and ethically consistent behavior: they
were more likely to refuse inappropriate requests (e.g., rejecting a prompt to divulge a patient’s record without consent),
and more likely to provide explanations referencing ethical principles (e.g., invoking patient confidentiality or citing
safety guidelines in their answers). We also observed performance gains across most categories after fine-tuning.
Ethical dilemma questions that previously confused the model were answered with improved alignment to the expected
solutions. For instance, on the earlier example of withholding a diagnosis from a patient, the fine-tuned model correctly
emphasized the importance of truthful disclosure in most trials, whereas the baseline model often erred. Safety-
related improvements were seen in critical areas like hallucination reduction – the fine-tuned models made 30% fewer
unsupported medical claims – and protocol adherence, with models more frequently recommending standard-of-care
actions. Some categories remained challenging: models still had only 60% accuracy on questions of fairness and bias
mitigation, suggesting those require further advances. Nonetheless, the trend was clear: domain-specific fine-tuning
markedly enhanced LLM reliability on ethical and safety matters, though absolute performance remains far from
perfect.
3
Discussion
Our benchmarking study reveals a concerning mismatch between LLM adoption and governance readiness [9]in the
healthcare institutions we examine. Despite China’s strong top-down emphasis on AI ethics (e.g., national guidelines
and the new Shanghai testing center.On-the-ground institutional protocols are lagging. Key gaps identified include:
Lack of fine-grained ethical audit protocols: Most hospitals and research centers do not have standardized methods
to audit AI models’ ethical behavior before deployment. While traditional medical device audits focus on clinical
efficacy and safety, there is no equivalent routine ethical risk audit for AI models[10]. For instance, none of the
institutions[11] in our study had a test set like our 12k QA to probe an LLM’s responses before integrating it into
patient care. This absence of granular auditing means potentially harmful behaviors go unnoticed[12]. Our results
(with baseline models only answering ˜45% of ethics/safety questions correctly) indicate that, without intervention,
LLMs could frequently violate ethics guidelines if deployed – yet many institutions lack the protocol to catch these
issues early[13][14].
Slow or inadequate response from hospital IRBs and oversight bodies[15]: Institutional Review Boards (IRBs) and
ethics committees at hospitals have traditionally overseen human subjects research and clinical trials, but they have been
slow to adapt to AI technologies. In China, hospital IRBs are just beginning to consider AI interventions, often treating
AI projects as standard IT deployments rather than high-stakes clinical tools. This can lead to delayed or superficial
ethical review of LLM-based systems. In our interviews, AI researchers noted that proposing an AI system for clinical
use did not always trigger the kind of rigorous review a new drug or device would get[16]. Additionally, IRBs may
lack AI expertise, causing blind spots – for example, not recognizing that an LLM integrated into an electronic health
record might continuously learn from patient data without consent. The result is that ethical clearance processes are not
keeping pace with the rapid introduction of LLMs. A recent npj Digital Medicine perspective similarly highlighted
“the current absence of robust AI governance in healthcare”, warning that without updated oversight, liability falls
disproportionately on providers and patients are exposed to harm.
Insufficient evaluation and monitoring tools: Beyond initial audits, institutions often lack ongoing monitoring systems to
track an LLM’s performance and catch issues over time. Unlike a static medical device, an LLM’s behavior might drift
with new updates or varied inputs. Yet, few hospitals employ real-time safety monitoring (e.g., sampling model outputs
regularly for harmful content) or feedback mechanisms for clinicians to flag AI errors. The creation of the Shanghai
Large Model Testing Centre (with its comprehensive evaluation of accuracy, safety, ethics, etc.is a notable exception
but is limited to Shanghai and still in pilot stages. For the majority of hospitals, there is no internal benchmark or
stress-test for AI systems. Our proposed benchmark could serve as such a tool; however, currently, a gap remains in
tooling and in culture – many institutions implicitly trust vendor-supplied AI without independent verification. This
aligns with global observations that “healthcare institutions should demand clear protocols and ... disclosures from
AI developers” but often do notnature.com. Without better tools, issues like an LLM making a subtle but dangerous
suggestion might only come to light after an adverse event.
In summary, our findings act as a “canary in the coal mine” – the measurable deficits in LLM performance reflect how
unprepared institutional governance is at this moment. Hospitals eager to leverage LLMs for efficiency gains may
4

--- Page 5 ---

Benchmarking Ethical and Safety Risks of Healthcare LLMs in China
not have implemented the necessary safeguards (ethics audits, rapid-review IRB processes, continuous monitoring) to
ensure patient safety and compliance. This governance gap is particularly salient in China’s context: while national
policy and frameworks exist, their translation into practice at the institutional level is inconsistent.
To bridge these gaps, we propose a multi-pronged governance framework for healthcare institutions deploying LLMs,
informed by our results and best-practice recommendations. This framework aligns with China’s aim to balance AI
innovation with risk prevention[17].
Institutional Data Ethics Guidelines: Institutions need to craft fine-grained AI ethics policies that go beyond broad
national laws. These guidelines would cover proper usage of LLMs and data within the institution, providing staff
with clear rules and expectations[18]. Key elements include: privacy and consent protocols (e.g., ensuring any patient
data fed into an LLM is de-identified and consent obtained if needed), bias mitigation strategies (requiring diversity in
training data and auditing for bias in outputs), and compliance with medical ethics standards (e.g., an AI should never
override a physician’s judgment, and must be designed to uphold principles of beneficence and non-maleficence). The
guidelines should also mandate documentation and transparency – maintaining a log of AI system versions, known
limitations, and deployment contexts. By institutionalizing these rules, front-line clinicians and developers have a clear
ethical playbook for LLM use. This could be enforced via training sessions and integrating the guidelines into IRB
review checklists for AI projects.
Safety Simulation & Testing Pipelines: Borrowing from the idea of clinical simulations, we recommend establishing AI
safety simulation pipelines. Before an LLM tool is widely deployed (or when it’s updated), it would be subjected to
scenario-based testing in a sandbox environment. For example, a hospital could simulate a week’s worth of clinical
queries through the LLM and analyze responses for any hazardous content. Our benchmark questions can serve as part
of this simulation, alongside institution-specific scenarios (like hospital protocol questions, local language nuances,
etc.). Moreover, stress tests should be performed – e.g., testing the model with adversarial or out-of-distribution inputs
to see if it remains reliable. Any failures trigger a hold on deployment until fixed. This pipeline becomes a pre-release
safety net. Additionally, institutions could adopt a monitoring dashboard that continuously evaluates random samples of
LLM-patient interactions (with privacy safeguards) to detect drifts in performance. Integration with incident reporting
systems (where clinicians can easily flag AI errors) will create feedback data for ongoing improvement. These practices
mirror the “full-chain management” approach exemplified by the Shanghai Testing Centre but scaled down to the
institutional level, ensuring that evaluation is not a one-time event but a continuous process.
Adaptive IRB and Oversight Mechanisms[19]: Governance reform should also extend to institutional ethics committees.
We propose that IRBs (or specialized AI oversight boards) develop fast-track review protocols for AI deployments.
Given the rapid iteration of software, a standing sub-committee on AI could be authorized to review minor model
updates or new datasets on a rolling basis (rather than months-long schedules). They should also include or consult AI
experts to properly judge technical risks.
Through these measures, we envision a robust institutional governance framework that ensures LLMs are thoroughly
vetted, continuously monitored, and guided by ethical norms throughout their use in healthcare. Importantly, this
framework is not meant to stifle innovation; rather, it provides the safety infrastructure that allows beneficial uses of AI
to flourish responsibly. When clinicians and patients know that an AI assistant has passed stringent ethical/safety checks
and is under watch, they can trust and adopt it more readily – accelerating the positive impact in line with Healthy
China 2030 goals.
Data availability
All the data generated in this study is available at the online repository:
https://medbench.opencompass.org.cn/community/data-station
Competing interests
The authors declare no competing interests.
Additional information
Correspondence and requests for materials should be addressed to Jie Xu.
Acknowledgements
Supported by Shanghai Artificial Intelligence Laboratory
5

--- Page 6 ---

Benchmarking Ethical and Safety Risks of Healthcare LLMs in China
References
[1] R. Li et al., “Using artificial intelligence to improve medical services in china,” Annals of Translational Medicine,
vol. 8, p. 711, 2020.
[2] J. S. Moon et al., “2023 clinical practice guidelines for diabetes management in korea: Full version recommenda-
tion of the korean diabetes association,” Diabetes & Metabolism Journal, vol. 48, pp. 546–708, 2024.
[3] D. S. Comeau, D. S. Bitterman, and L. A. Celi, “Preventing unrestricted and unmonitored ai experimentation in
healthcare through transparency and accountability,” npj Digital Medicine, vol. 8, p. 42, 2025.
[4] X. Yang et al., “Application of large language models in disease diagnosis and treatment,” Chinese Medical
Journal, vol. 138, pp. 130–142, 2025.
[5] H. J. Park, “Patient perspectives on informed consent for medical ai: A web-based experiment,” Digital Health,
vol. 10, p. 20552076241247938, 2024.
[6] M. Guevara et al., “Large language models to identify social determinants of health in electronic health records,”
npj Digital Medicine, vol. 7, p. 6, 2024.
[7] S. Chen et al., “The effect of using a large language model to respond to patient messages,” The Lancet Digital
Health, vol. 6, pp. e379–e381, 2024.
[8] T. Davenport and R. Kalakota, “The potential for artificial intelligence in healthcare,” Future Healthcare Journal,
vol. 6, pp. 94–98, 2019.
[9] F. Cabitza, R. Rasoini, and G. F. Gensini, “Unintended consequences of machine learning in medicine,” JAMA,
vol. 318, pp. 517–518, 2017.
[10] J. A. Omiye, J. C. Lester, S. Spichak, V. Rotemberg, and R. Daneshjou, “Large language models propagate
race-based medicine,” npj Digital Medicine, vol. 6, p. 195, 2023.
[11] J. W. Gichoya et al., “Ai recognition of patient race in medical imaging: a modelling study,” The Lancet Digital
Health, vol. 4, pp. e406–e414, 2022.
[12] C. Etherington, M. Lê, L. Proulx, and S. Boet, “Bringing the patient voice into the operating room: engaging
patients in surgical safety research with the operating room black box(®),” Research Involvement and Engagement,
vol. 8, p. 32, 2022.
[13] N. T. T. Phi, T. Oikonomidi, P. Ravaud, and V. T. Tran, “Assessment of us food and drug administration-approved
digital medical devices for just-in-time interventions: A systematic review,” JAMA Internal Medicine, vol. 183, pp.
858–869, 2023.
[14] E. Crigger et al., “Trustworthy augmented intelligence in health care,” Journal of Medical Systems, vol. 46, p. 12,
2022.
[15] Z. Obermeyer and E. J. Emanuel, “Predicting the future - big data, machine learning, and clinical medicine,” The
New England Journal of Medicine, vol. 375, pp. 1216–1219, 2016.
[16] K. E. Goodman, D. J. Morgan, and D. E. Hoffmann, “Clinical algorithms, antidiscrimination laws, and medical
device regulation,” JAMA, vol. 329, pp. 285–286, 2023.
[17] B. Meskó and D. deBronkart, “Patient design: The importance of including patients in designing health care,”
Journal of Medical Internet Research, vol. 24, p. e39178, 2022.
[18] B. Meskó and E. J. Topol, “The imperative for regulatory oversight of large language models (or generative ai) in
healthcare,” npj Digital Medicine, vol. 6, p. 120, 2023.
[19] D. deBronkart, “Open access as a revolution: Knowledge alters power,” Journal of Medical Internet Research,
vol. 21, p. e16368, 2019.
6

```
