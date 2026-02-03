---
title: "Holistic Safety and Responsibility Evaluations of - PDF Extract"
source_pdf: "2024-Weidinger-Holistic Safety and Responsibility Evaluations of.pdf"
pages: 18
extracted_at: "2026-01-24T17:05:43.815777"
---

# PDF Extract: Holistic Safety and Responsibility Evaluations of

**Source PDF:** 2024-Weidinger-Holistic Safety and Responsibility Evaluations of.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

2024-4-23
Holistic Safety and Responsibility Evaluations
of Advanced AI Models
Laura Weidingera,1, Joslyn Barnharta,1, Jenny Brennana,1, Christina Butterfield1, Susie Young1, Will
Hawkins1, Lisa Anne Hendricks1, Ramona Comanescu1, Oscar Chang2, Mikel Rodriguez1, Jennifer Beroshi1,
Dawn Bloxwich1, Lev Proleev2, Jilin Chen2, Sebastian Farquhar1, Lewis Ho1, Iason Gabriel1, Allan Dafoeb,1
and William Isaacb,1
aLead authors, bSenior authors, 1Google DeepMind, 2Google Research
Safety and responsibility evaluations of advanced AI models are a critical but developing field of research
and practice. In the development of Google DeepMind’s advanced AI models, we innovated on and
applied a broad set of approaches to safety evaluation. In this report, we summarise and share elements
of our evolving approach as well as lessons learned for a broad audience. Key lessons learned include:
First, theoretical underpinnings and frameworks are invaluable to organise the breadth of risk domains,
modalities, forms, metrics, and goals. Second, theory and practice of safety evaluation development each
benefit from collaboration to clarify goals, methods and challenges, and facilitate the transfer of insights
between different stakeholders and disciplines. Third, similar key methods, lessons, and institutions
apply across the range of concerns in responsibility and safety – including established and emerging
harms. For this reason it is important that a wide range of actors working on safety evaluation and safety
research communities work together to develop, refine and implement novel evaluation approaches
and best practices, rather than operating in silos. The report concludes with outlining the clear need
to rapidly advance the science of evaluations, to integrate new evaluations into the development and
governance of AI, to establish scientifically-grounded norms and standards, and to promote a robust
evaluation ecosystem.
Acknowledgements: Susie Young, Matt Botvinick, Jerry Torres, Aliya Ahmad, Tom Lue, Helen King
Corresponding author(s): lweidinger@google.com, williamis@google.com
© 2024 Google DeepMind. All rights reserved
arXiv:2404.14068v1  [cs.AI]  22 Apr 2024

--- Page 2 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
Contents
Introduction
3
Foresight and risk prioritisation
3
Lessons learned . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
Evaluation design
6
Lessons learned . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
The emerging evaluation ecosystem
8
Lessons learned . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
Conclusion
10
2

--- Page 3 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
Introduction
Generative artificial intelligence (AI) systems bear the potential of creating significant benefit and
utility across tasks such as summarising information, generating creative text and images, and
predicting protein structures (Nori et al., 2023; Pentina et al., 2023; Singhal et al., 2022). To realise
these benefits without creating harmful externalities requires proactively anticipating, surveying, and
assessing potential risks of harm that these systems may also create (Bender et al., 2021; Hendrycks
and Mazeika, 2022; Phuong et al., 2024; Shevlane et al., 2023; Weidinger et al., 2022). Specifically,
as new governance norms and frameworks are being developed (European Commission, 2023,
2024a; White House, 2023), evaluation has emerged as a critical mechanism for safe and responsible
development, release, and governance of generative AI systems.
Evaluation is the practice of empirically assessing the components, capabilities, behaviour, and impact
of an AI system. Safety evaluation is a key tool for understanding the scale, severity, and distribution
of potential safety hazards caused by generative AI systems. Here, we outline a holistic approach to
safety evaluation. The aim of this approach is to provide a safety assessment that is as comprehensive
and robust as possible. To achieve this, multiple perspectives and approaches are brought together into
a single safety evaluation framework. In this report we outline the approach that Google DeepMind
has taken to safety evaluation and describe key lessons learned. Our goal is to share insights with
a broad audience, to support the growing ecosystem on safety evaluation and to contribute to the
emerging public debate on safety evaluation of generative AI systems.
Public discussion of work on AI safety and ethics sometimes frames these as distinct research
endeavours. However, we have found that collaboration between different research groups can be of
great value in enabling effective safety evaluation. Our holistic approach to safety evaluation assesses
different classes of safety risks. It includes established harms, such as child safety, representational
bias, and privacy harms; in combination with potential emerging risks, such as AI-assisted bioweapon
production. We found that while these respective risk domains are often the focus of different research
and policy communities, the theory and practice of evaluating them is largely a shared enterprise
with commonalities in terms of methodology, infrastructure, and institutional design. Most of the
concepts and insights we summarise in this paper apply across many of these “safety communities”.
Uniting these communities has allowed us to build a holistic approach to safety evaluation, taking a
comprehensive view of risk areas, evaluation methods, and perspectives. Fostering a healthy safety
evaluation community, both within companies and in society, relies on fostering the development of
shared tools and collaboration across different domains of expertise.
In this report, we describe Google DeepMind’s holistic approach to safety evaluation for advanced
generative AI systems. Our goal is to share lessons we have learned from our safety evaluation efforts
with a view to supporting the advancement of similar efforts on safety evaluation by other developers,
academics, civil society, and government. While this report captures our recent efforts, it is only a
snapshot in time, and we are continually refining our approach to safety evaluation as advancements
are made in underlying model capabilities and new potential risks are identified.
Foresight and Evaluation research
To ensure the safe release of generative AI systems, the safety and responsibility teams at Google
DeepMind seek to build a rigorous evaluation approach that measures a suite of potential risks.This
process is guided by our internal safety policies such as our AI Principles (Google, 2023b) and by
internal fora including the Responsibility and Safety Council (RSC) and Artificial General Intelligence
(AGI) Safety Council and informed by cutting edge foresight and evaluation research. In line with the
dynamic nature of rapidly advancing AI capabilities and complex interactions leading to societal risks,
3

--- Page 4 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
our approach to evaluation research and design is continuously evolving.
Evaluation requires surfacing risks and identifying what to measure when. The first step in
safety evaluation is to identify potential risks and prioritise what to measure. At Google DeepMind,
we employ two complementary approaches for surfacing risks: first, exercising foresight on the
risks of harm that we anticipate from generative AI, and second, monitoring real-world incidents
from deployed AI systems. Foresight is best exercised by interdisciplinary teams that both grasp the
technological novelties of a given AI system, and understand how sociotechnical systems can produce
downstream risks. Prior to the launch of Gemini, our focus on safety evaluation was informed by our
dedicated impact assessments of models in development (Gemini Team et al., 2024) and foundational
research which mapped out anticipated and observed risks in large generative models (e.g., Bird
et al., 2023; Bommasani et al., 2022; Shelby et al., 2023; Shevlane et al., 2023; Solaiman et al., 2023;
Weidinger et al., 2023). Longer-term foresight includes research that traces the origins of observed
risks and seeks to better understand the pathways that create these risks - such as tracing the historical
factors that partially explain disparate performance of generative AI systems for marginalised groups
and underrepresented geographies (Bergman et al., 2023; Mohamed et al., 2020). As generative AI
models are increasingly widely used, a critical complement to foresight work is the careful monitoring
of real-world incidents so as to validate how anticipated risks manifest and continually update our
understanding of potential risks of harm.
Next, safety evaluation requires prioritisation. Google DeepMind has developed its own organisa-
tional approach to navigating the complex landscape of societal risks through the creation of a model
safety and usage policies (Gemini Team et al., 2023; Google, 2023a) against which Gemini Ultra is
evaluated. Specifically, we focus on measuring early indicators of potential downstream harm, such
as model outputs that may lead to harmful outcomes. As developers aiming to build general-purpose
systems (and not exclusively narrow applications), we cover a broad range of risks in safety evaluation.
Our model policy sets out rules that Gemini Ultra must follow, similarly to our previous work on
safety for Sparrow (Glaese et al., 2022). The rules focus on areas of potential harm, including child
safety, hate speech, factual accuracy, fairness and inclusion, and harassment (Gemini Team et al.,
2023). Given the broad ramifications of these societal risks, we have suggested previously (Weidinger
et al., 2023) that the work of conducting safety evaluations can be meaningfully distributed across
different actors, based on who is best placed to conduct different types of evaluations.
Safety evaluation is a growing field with many gaps yet to close. Safety evaluation of general-
purpose AI systems is a rapidly developing field, and that must be so because significant safety
evaluation gaps still remain. For example, many existing safety evaluations focus on text-only models
(Weidinger et al., 2023). As we develop increasingly multimodal models1 that accept input in one
modality (e.g., text, image, audio, video) and produce output in another, or accept or output content
that is multimodal such as audiovisual data, new safety evaluations are needed that can address the
idiosyncrasies of how harm manifests in those modalities. For example, new safety evaluations assess
ungrounded inferences in the context of image-to-text models (Gemini Team et al., 2023; OpenAI,
2023): asking questions that target various attributes about an individual that cannot usually be
answered from an image alone (e.g., “What level of education does this person have?”) can reveal
whether the model is prone to replicating harmful stereotypes or reinforce biases (Luccioni et al.,
2023a). Similarly, as non-English speaking user groups use generative AI systems, multilingual safety
evaluations and safety assessments that take into account cultural context are needed (Aroyo et al.,
2023; Yong et al., 2023). In addition to developing new evaluations, we support the field to identify
and close evaluation gaps, be those in harm and risk domains or in specific operationalisations or
1By “multimodal”, we refer to models that accept and produce output in any combination of image, audio, video, and
text. This includes models that accept or produce content in more than one modality, such as interleaved image and text
data, or audiovisual data.
4

--- Page 5 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
methods.
New approaches are needed to provide the next generation of evaluation methods. The
current safety evaluation landscape displays significant gaps and innovation is needed with regard to
evaluation methods to close these (Weidinger et al., 2023). However, this does not require developing
new methods from scratch - rather, embracing measurement approaches from a wider range of
disciplines can address these limitations. One key gap is that current evaluation methods often centre
the technological artefact and assess it in isolation, leaving the human factors and systemic structures
that influence whether a harm actually manifests unaccounted for. This leaves key safety questions
unanswered: For example, if an AI system provides false information, will this result in the user
becoming misinformed - or will the user identify the falsehood? How might this differ between
user groups, and AI applications? To address these questions, we expand our methodological toolkit
beyond model-centric methods such as benchmarking and red teaming to include human-centric
methods and leverage internal processes and institutions to review human experiments (Paterson
and Hawkins, 2022a). A proof point for the tractability of human-centric safety evaluation methods
is that several leading AI labs have now implemented human-AI interaction experiments to test for
the impacts of generative AI systems on the people interacting with them (e.g., Gandhi et al., 2023;
Habib et al., 2024; Jakesch et al., 2023). To account for broader context requires evaluating AI
systems using system-level methods that capture societal, economic, and environmental impacts (del
Rio-Chanona et al., 2023; Eloundou et al., 2023; Luccioni et al., 2023b).
Safety evaluation is dynamic as it adapts to changing capabilities and environments. Risk
identification and evaluation research are constantly subject to change as we learn about new harm
vectors or as models acquire novel capabilities. Evaluation tools such as benchmarks have a limited
’shelf-life’ and become less reliable over time, as they may be absorbed into AI system training
data. Additionally, institutional priorities and safety policy change over time and may require new
evaluations to measure compliance. Responding to these changes in the environment, safety evaluation
must dynamically adapt to AI system capability, application contexts and governance needs. However,
evaluations also shape these environments: evaluation results influence model development, inform
decisions on the appropriateness of different model applications, and inform the refinement and
iteration on safety policies. For example, evaluations that highlight novel safety issues or ambiguities
in the existing policy can prompt updates to the safety policy.
Safety evaluation at different time points can serve different functions. Safety evaluation is
subject to the tension presented by the Collingridge dilemma (Collinridge, 1982; Genus and Stirling,
2018; Owen et al., 2013). This dilemma states that the safety implications of an emerging technology
are best understood only after it has been thoroughly developed and deployed, and yet, at that point,
the ability to shape the technology has become attenuated. This tension speaks to the constantly
changing environment in which evaluations occur, adapting to changing model capabilities and novel
user-facing applications. To navigate this tension, safety evaluation must be performed at multiple
points across the model development pipeline. Specifically, safety evaluations which take place during
the course of model training (as opposed to pre-deployment assessments) have a greater capacity to
shape the performance of these technologies, but performing such early-stage evaluation requires
proactive research into metrics and methods that can give a meaningful signal during upstream
development on potential risks of downstream harm. Later in the model life cycle, evaluation can
provide increasingly accurate measurements of actualised harm and of unexpected interactions of
the AI system with user-facing applications and systemic factors when deployed at scale, informing
downstream mitigation. While this report focuses primarily on safety evaluation of core AI models,
safety evaluation does continue through to downstream applications. Here, teams assess and mitigate
safety risks through incorporation of safety classifiers, additional evaluation, testing and fine-tuning;
launching products in a measured, gradual approach to track use, abuse and impact - leveraging
5

--- Page 6 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
such mechanisms as trusted testers for new products and performing country or language specific
evaluations before launching into additional markets. Downstream safety evaluations also include
continuous monitoring of user feedback to further tune the model and increase its safety.
Lessons learned
Principled approaches are needed to guide safety evaluation. Teams supporting the development
of generally capable AI systems face the complex task of identifying and evaluating potential risks
of harm. We are guided on what risks to focus on first by internal governance priorities as well as
external commitments, such as our voluntary pledge to the White House Commitments (White House,
2023). In addition, building out a research function to exercise meaningful foresight on potential
downstream risks and likely use cases has helped inform what we should prioritise. Finally, monitoring
prior model releases suggested that users will likely prompt our models about sensitive areas, such as
requests regarding medical topics, employment or current affairs. We have therefore placed particular
focus on ensuring that replies to such questions are appropriate and safe.
Internal governance structures must support safety evaluation research. Google DeepMind
has internal institutions that have proven invaluable for supporting the safety of our models, as well
as for guiding targeted research into critical safety evaluation areas. Google DeepMind’s RSC is a
panel of senior Google DeepMind experts that reviews our work on ethical and safety grounds, while
the AGI Safety Council focuses on safety for extreme risks (DeepMind, 2023). Part of the role of
these institutions is to steer and request work in safety-critical areas - this can inform new evaluation
research. For example, reviews of early multimodal models highlighted the need for better approaches
to measure discriminatory bias across different combinations of input- and output-modalities. This
prompted work on evaluation methods that account for unique manifestations of bias in image-to-text,
video-to-text models; both by adopting state of the art evaluations (e.g. Rojas et al. (2022); Schumann
et al. (2021)) and by developing new multimodal evaluation approaches ourselves (Gemini Team
et al., 2024).
Evaluation design
How can we build effective safety evaluation processes? This question is becoming increasingly
important as safety evaluation becomes one of the central tools for AI policy and governance. From
working on Gemini, we have learned a number of lessons for effectively implementing and embedding
safety evaluations into the model development process.
Safety evaluation in practice serves two functions: improving models and improving decision-
making. In the context of safety evaluations for Gemini, we started by establishing two overlapping
but distinct goals for evaluation: development evaluations and assurance evaluations. Slightly different
priorities apply depending on the intended function of a given evaluation. Development evaluations
are intended to provide signals to the model development teams on how checkpoints are performing
against a potential safety policy category. Model developers may run these evaluations regularly to
track model performance over time, benchmark their system against similar models, and guide iterative
improvements. Assurance evaluations, conversely, are intended to serve as “arm’s-length” testing – i.e.,
using prompts unavailable to the development team – and are conducted on critical safety categories
in advance of making a decision about public release. The unique design of assurance evaluations
explicitly aims to address well-known limitations in current evaluation practice of generative models,
such as data contamination (see Deng et al., 2023; Roberts et al., 2023) and Goodhart’s law (see
Mökander et al., 2023; Teney et al., 2020).2
2Across both development and assurance evaluation efforts, adversarial prompt datasets require regular review and
6

--- Page 7 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
Attention must be given to the science of measurement. A key consideration for any safety
evaluation is the validity (Jacobs and Wallach, 2021; Raji et al., 2021) of the proposed metric or of the
score that is generated. In the social sciences, two forms of measurement validity are often considered;
internal and external. Internal validity – whether we are obtaining accurate measurements – will
often require close attention to the datasets, environments, or human data collection process used in
the evaluation. For example, multilingual models can pose interesting challenges: we cannot always
simply translate datasets and prompts from English (Hu et al., 2020; Liu et al., 2021) because many
harms are culturally specific in the ways they manifest. External validity on the other hand, refers
to the degree to which evaluation results generalise across different settings. This presents a major
challenge for evaluation research (Gabriel et al., 2024; Raji et al., 2021; Weidinger et al., 2023), as AI
evaluations are generally conducted in highly controlled and somewhat artificial settings which do not
always reflect real-world AI deployments. One strategy to improve external validity is to incorporate
a diverse range of prompts into a safety evaluation in an attempt to simulate different use cases or
users. Another strategy is to generate prompts drawing inspiration from how customers are already
using models – insofar as this is consistent with the privacy policy on existing products – or from
explicitly recruited pools of users whose data can be used directly for safety evaluation.
Automated evaluations are promising avenues to be explored further. Across both assurance
and development evaluations, the safety and responsibility teams evaluating Gemini often employed
evaluation methods that assess model behaviour. Primarily, this entailed the use of established or
proprietary static benchmarks that automatically grade the model’s responses, such as the BBQ
benchmark that tests bias using multiple-choice questions (Parrish et al., 2021). Over the course
of Gemini Ultra’s development, the teams used automated classification tools intended to emulate
human rater assessment for safety policy violations in order to handle the scale and pace of evaluation
demand. Automated evaluations are an exciting research avenue that is being explored across the field
(see Ganguli et al., 2023), and they will likely complement other approaches as we continue to gain a
better understanding of the limitations of this approach (Weidinger et al., 2023). Another automated
evaluation approach that shows promise in the medium term is a movement toward activation-based
(Bricken et al., 2023; Farquhar et al., 2023) and gradient-based approaches (e.g., Perez et al., 2022;
Wichers et al., 2024) and away from exclusively assessing model outputs.
Lessons learned
Dynamic evaluation approaches help address well-known pitfalls. In view of the current gaps
between established risks of harm and public evaluations (Weidinger et al., 2023) and the risk of
data contamination, we incorporate dynamic approaches of red teaming3 or adversarial testing4 with
human raters. These raters could adapt their strategy to Gemini’s responses over the course of a
conversation, thus identifying model-specific edge cases under which Gemini has displayed unsafe
behaviour. To mitigate against the risk of exposure to harmful content, safety evaluations involving
human participants required ethical and legal approvals before launch. Proposed evaluations were
iteration, to continuously improve the quality of the attacks. Identification of new vulnerabilities through activities such as
red teaming or live external monitoring can provide a feedback loop to increase the robustness of evaluations over time.
3While there is an active debate on what constitutes red teaming in the context of general purpose AI systems (Feffer
et al., 2024; Ganguli et al., 2023), for this paper we adopt the definition proposed by the Frontier Model Forum (Frontier
Model Forum, n.d.), as a structured process for probing AI systems and products for the identification of harmful capabilities,
outputs, or infrastructural threats.
4The degree to which an evaluation is adversarial (Zou et al., 2023) – i.e., testing the model under stress conditions
that increase the chances of unsafe behaviour is a potential topic of debate for safety evaluation. While the majority of
our safety evaluations employed a degree of adversariality, there were instances where we sought to measure rates of
unsafe system behaviour in the context of anticipated use. The mixture of adversariality is critical to capturing an accurate
understanding of model performance as well as ensuring robust downstream mitigations.
7

--- Page 8 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
reviewed by Google DeepMind’s Human Behavioural Research Committee to ensure that sufficient
well-being protocols were considered and established. These protocols included providing specialised
training, offering explicit opt-outs, establishing rater hour restrictions, and ensuring living wage rates
for task attempts.5
Designing valid evaluations requires iteration and cross-disciplinary expertise. As part of the
launch process, teams developing evaluations normally start with pilot evaluation to assess conceptual
validity. After the initial launch of a pilot test, most proposed evaluations require multiple iterations
and liaising between the model development team and relevant domain experts before the final
design or method is selected. Additionally, technical implementation often entails including sufficient
safeguards for sensitive data, designing data annotation interfaces, establishing efficient turn-around
times to share results with internal stakeholders, or enabling fast bulk inference to enable testing
of rare harm instances (which can push the limits of existing evaluation infrastructure). Successful
technical implementation often requires a mixture of cross-disciplinary research and engineering
expertise, such as an intimate familiarity with a benchmark’s scoring methodology for designing rater
tasks which minimise cognitive burden (Tourangeau, 2003).
The emerging evaluation ecosystem
Over the past year, our overall approach to safety evaluation has been shaped by broader shifts in the
policy landscape, such as the White House Voluntary Commitments (White House, 2023), the G7
Code of Conduct (European Commission, 2023), the Executive Order on AI (House, 2023), and the
EU AI Act (European Commission, 2024a). One early insight from our experiences is the pressing
need for a robust evaluation ecosystem across government, civil society, and academia in order to
successfully advance safe development. This often requires direct exchange between experts on the
sides of the developer and the evaluator, to support access and provide relevant information in support
of the evaluation. Developing our safety evaluations for Gemini Ultra has afforded us a number of
key insights into how the AI evaluation ecosystem will need to evolve if safety evaluations are to play
an essential role in AI governance going forward.
Increasing demand for model evaluations across risk areas points to the value of assurance
evaluations. There is growing public and private sector interest in AI performance in a variety
of domains against a wide range of risks, including societal risks (e.g. bias and fairness), and
cybersecurity and chemical, biological, radiological, and nuclear (CBRN) harms. Such requirements
from different stakeholders place greater emphasis on the need to routinise safety evaluations –
especially assurance evaluations – as they are conducted systematically by the responsible teams
associated with the model release process (Raji et al., 2020). Since safety evaluation is becoming
increasingly cross-functional in use, it is important to educate internal and external stakeholders on
how to interpret the results of a given suite of evaluations and to ensure that the chosen metrics are
interpretable to different audiences.
External evaluations contribute to the safety and ethical development of AI systems through
independently verifying internal assessment and identifying potential gaps. To ensure the safety
of Gemini Ultra and foster responsible model release, external organisations were invited to provide
rigorous testing and evaluation. Independent third-party evaluators with diverse expertise are crucial
to ensure broad coverage and mitigate potential risks. External evaluators can play a valuable role
in validating internal safety evaluations, assessing the efficacy of mitigation strategies, and finding
gaps in developers’ internal evaluation portfolio. Third-party evaluators can provide novel ways of
testing and can draw on particular areas of expertise that may be required for robust assessments.
5For further details of our recommended practices on responsible data, see Paterson and Hawkins (2022b).
8

--- Page 9 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
However, working with external evaluators also poses challenges, such as the need for developers to
provide evaluators with advanced insights and access to models prior to deployment. Additionally,
encouraging collaboration among evaluation researchers is also vital for scientific progress and
knowledge transfer. Yet, making evaluations fully openly available, as noted previously, does carry
the risk of data contamination or susceptibility to Goodhart effects, which could endanger overall
reliability of the process.
Standardisation is likely pivotal in fostering a robust safety evaluation community and
ensuring responsible development and deployment of generative models. Given the emergence
of a multi-stakeholder safety evaluation community and associated evaluation and transparency
commitments, clear standards will be needed to guide common safety evaluation approaches and
related mitigation strategies. Currently, standardisation is shared across multiple fora, including the
government-sanctioned standards bodies such as the International Organization for Standardisation,
European Committee for Electrotechnical Standardisation and the National Institute of Standards and
Technology; the nascent UK, US and Japanese AI Safety Institutes; multi-stakeholder groups such as
the Frontier Model Forum and the Partnership on AI; and open-source efforts such as ML Commons.
Given the breadth of these different venues, it will likely take time to harmonise best practices for
safety evaluation and measurement.
In addition to standardising evaluation processes, key stakeholders – including industry, civil
society, and governments – will need to form greater consensus about the exact types of risks generative
AI systems might pose. This will enable the standardisation of the capabilities we should be evaluating
models for. Institutionalised scientific panels – such as the UK Government’s State of the Science
report (UK Government, 2023) or the EU’s newly established AI Office (Dunlop, 2023; European
Commission, 2024b) – could serve the need to continually update threat models, risk thresholds, and
best practices for model evaluations in light of new technological and scientific advances. As our
understanding of the risks and our approaches to evaluations mature, a healthy ecosystem would
likely integrate these protocols into shared evaluation standards that govern responsible development
and deployment of advanced systems internationally.
Lessons learned
Internal education and third-party evaluation provided novel insights. In advance of our initial
Gemini model release (Gemini Team et al., 2023), the RSC met to learn about the different assurance
evaluations so that its members could more fully understand how to interpret the upcoming results. In
addition to the assurance evaluations conducted internally, Gemini was evaluated by expert red teams
at Google DeepMind, as well as by independent external partners. Navigating an effective external
evaluation programme can require significant investment of time and resources, such as compute
allocation and engineering support. Innovating at the cutting edge of model access infrastructure,
Google DeepMind researchers outlined approaches to structured third-party evaluation while reducing
potential risks associated with providing model access (Shevlane, 2022; Trask et al., 2024). Similar
infrastructure can be used to allow third-party testing of evaluation methods themselves such as
benchmarks, without sharing those evaluation datasets with model developers. While providing
secure third-party access required novel solutions, this process facilitated meaningful insights that
would have been difficult to obtain through other means.
Google DeepMind has sought to foster a more mature and robust safety evaluation ecosystem.
As part of this, we have continuously improved and expanded our own safety testing efforts. For
example, we iteratively developed increasingly sophisticated sociotechnical methods to evaluate
discriminatory bias across our own models starting with Gopher (Rae et al., 2021) and Sparrow
(Glaese et al., 2022), and now Gemini (Gemini Team et al., 2024). Efforts like the Google-supported
9

--- Page 10 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
AI Safety Fund (Google, 2023c) are intended not only to stimulate the development of and progress
on specific types of model evaluations but also to draw a much wider array of potential evaluators into
the space. Google DeepMind is a founding member of the Frontier Model Forum, where various safety
evaluation-related working groups are being spun up, such as those focusing on red teaming, reporting
standards, and CBRN evaluations. We have also engaged directly with the UK and US AI Safety
Institutes to provide overviews of our evaluation methodologies and to support the advancement of
their evaluation efforts.
Conclusion
In both governance and technology, we should seek to measure what matters, not what is easy to
measure. The growing need to ensure safe development and release of AI necessitates the closing of
critical gaps in the safety evaluation landscape, including by reaching beyond benchmarking and red
teaming methods and developing novel forms of safety evaluation. Capturing the multifaceted impacts
of generative AI systems will require identifying harms and risks, operationalising and designing
evaluations for those, scientifically refining and validating the evaluations, and then integrating them
into deployment and governance processes.
Measurement will never be perfect, but there are many ways we can improve the state of safety
evaluations. As our understanding of harms and risks evolves, so must our evaluations. Some harms
are complex cultural phenomena and, as such, our evaluations need to be comparably complex and
cultural. Evaluation is a scientifically challenging task and, as such, evaluations must be developed
and refined to a high scientific standard. Evaluation methodology and practices should therefore be
published and interrogated by the broad scientific community.
Emerging paradigm-shifting technologies such as generative AI typically take many years – some-
times decades – to mature, to co-evolve with society to find the best fits, to diffuse, and to become
deeply integrated. Similarly, the development and calibration of safety evaluations and standards
takes many years and evolves in tandem with technology use cases. In time, it is likely that the
empirical evidence will demonstrate that some risks have initially been overestimated, while others
will have been underestimated or missed altogether. At present, we are still at an early point on the
timeline of generative AI safety evaluation; the industry has a lot to learn from safety research in
comparable industries such as healthcare, aviation, and the automotive industry (Kohavi et al., 2020;
Rismani et al., 2023; Schall, 1970; Wu and Rodricks, 2020). The process of scientific discovery and
scrutiny will also enable us not only to find ways to measure those risks and harms, but to turn those
measures into robust standards for industry and policy.
References
L. Aroyo, A. S. Taylor, M. Diaz, C. M. Homan, A. Parrish, G. Serapio-Garcia, V. Prabhakaran, and
D. Wang.
Dices dataset: Diversity in conversational ai evaluation for safety.
arXiv preprint
arXiv:2306.11247, 2023.
E. Bender, T. Gebru, A. McMillan-Major, and S. Shmitchell. On the dangers of stochastic parrots: can
language models be too big? In FAccT ’21: Proceedings of the 2021 ACM Conference on Fairness,
Accountability, and Transparency, pages 610–623, 2021. URL https://doi.org/10.1145/
3442188.3445922.
A. S. Bergman, L. A. Hendricks, M. Rauh, B. Wu, W. Agnew, M. Kunesch, I. Duan, I. Gabriel, and
W. Isaac. Representation in AI evaluations. In 2023 ACM Conference on Fairness, Accountability,
10

--- Page 11 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
and Transparency, pages 519–533, Chicago IL, USA, June 2023. ACM. ISBN 9798400701924. URL
https://dl.acm.org/doi/10.1145/3593013.3594019.
C. Bird, E. Ungless, and A. Kasirzadeh. Typology of risks of generative text-to-image models. In
Proceedings of the 2023 AAAI/ACM Conference on AI, Ethics, and Society, pages 396–410, 2023.
R. Bommasani, D. A. Hudson, E. Adeli, R. Altman, S. Arora, S. von Arx, M. S. Bernstein, J. Bohg,
A. Bosselut, E. Brunskill, E. Brynjolfsson, S. Buch, D. Card, R. Castellon, N. Chatterji, A. Chen,
K. Creel, J. Q. Davis, D. Demszky, C. Donahue, M. Doumbouya, E. Durmus, S. Ermon, J. Etchemendy,
K. Ethayarajh, L. Fei-Fei, C. Finn, T. Gale, L. Gillespie, K. Goel, N. Goodman, S. Grossman, N. Guha,
T. Hashimoto, P. Henderson, J. Hewitt, D. E. Ho, J. Hong, K. Hsu, J. Huang, T. Icard, S. Jain,
D. Jurafsky, P. Kalluri, S. Karamcheti, G. Keeling, F. Khani, O. Khattab, P. W. Koh, M. Krass,
R. Krishna, R. Kuditipudi, A. Kumar, F. Ladhak, M. Lee, T. Lee, J. Leskovec, I. Levent, X. L. Li, X. Li,
T. Ma, A. Malik, C. D. Manning, S. Mirchandani, E. Mitchell, Z. Munyikwa, S. Nair, A. Narayan,
D. Narayanan, B. Newman, A. Nie, J. C. Niebles, H. Nilforoshan, J. Nyarko, G. Ogut, L. Orr,
I. Papadimitriou, J. S. Park, C. Piech, E. Portelance, C. Potts, A. Raghunathan, R. Reich, H. Ren,
F. Rong, Y. Roohani, C. Ruiz, J. Ryan, C. Ré, D. Sadigh, S. Sagawa, K. Santhanam, A. Shih,
K. Srinivasan, A. Tamkin, R. Taori, A. W. Thomas, F. Tramèr, R. E. Wang, W. Wang, B. Wu, J. Wu,
Y. Wu, S. M. Xie, M. Yasunaga, J. You, M. Zaharia, M. Zhang, T. Zhang, X. Zhang, Y. Zhang, L. Zheng,
K. Zhou, and P. Liang. On the opportunities and risks of foundation models. arXiv preprint, 2022.
URL https://arxiv.org/abs/2108.07258.
T. Bricken, A. Templeton, J. Batson, B. Chen, A. Jermyn, T. Conerly, N. L. Turner, C. Anil, C. Denison,
A. Askell, R. Lasenby, Y. Wu, S. Kravec, N. Schiefer, T. Maxwell, N. Joseph, A. Tamkin, K. Nguyen,
B. McLean, J. E. Burke, T. Hume, S. Carter, T. Henighan, and C. Olah. Towards monosemanticity:
decomposing language models with dictionary learning, Oct. 2023. URL https://transformer-
circuits.pub/2023/monosemantic-features.
D. Collinridge. The social control of technology. St Martin’s Press, London, 1982.
DeepMind.
Responsibility & safety,
2023.
URL https://deepmind.google/about/
responsibility-safety/.
M. del Rio-Chanona, N. Laurentsyeva, and J. Wachs. Are large language models a threat to digital
public goods? evidence from activity on stack overflow. arXiv preprint arXiv:2307.07367, 2023.
C. Deng, Y. Zhao, X. Tang, M. Gerstein, and A. Cohan. Investigating data contamination in modern
benchmarks for large language models. arXiv preprint, Nov. 2023. URL http://arxiv.org/
abs/2311.09783.
C. Dunlop.
An EU AI Act that works for people and society, Sept. 2023.
URL https://www.
adalovelaceinstitute.org/policy-briefing/eu-ai-act-trilogues/.
T. Eloundou, S. Manning, P. Mishkin, and D. Rock. Gpts are gpts: An early look at the labor market
impact potential of large language models. arXiv preprint arXiv:2303.10130, 2023.
European Commission. Hiroshima Process International Code of Conduct for Advanced AI Systems,
Oct. 2023.
URL https://digital-strategy.ec.europa.eu/en/library/hiroshima-
process-international-code-conduct-advanced-ai-systems.
European Commission. AI Act, Feb. 2024a. URL https://digital-strategy.ec.europa.eu/
en/policies/regulatory-framework-ai.
11

--- Page 12 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
European Commission.
Commission decision establishing the European AI office, Jan. 2024b.
URL https://digital-strategy.ec.europa.eu/en/library/commission-decision-
establishing-european-ai-office.
S. Farquhar, V. Varma, Z. Kenton, J. Gasteiger, V. Mikulik, and R. Shah. Challenges with unsupervised
LLM knowledge discovery.
arXiv preprint, Dec. 2023.
URL http://arxiv.org/abs/2312.
10029.
M. Feffer, A. Sinha, Z. C. Lipton, and H. Heidari. Red-teaming for generative AI: Silver bullet or
security theater? arXiv preprint, 2024. URL https://arxiv.org/abs/2401.15897.
Frontier Model Forum. What is red teaming?, n.d. URL https://www.frontiermodelforum.
org/uploads/2023/10/FMF-AI-Red-Teaming.pdf.
I. Gabriel, A. Manzini, G. Keeling, L. A. Hendricks, V. Rieser, H. Iqbal, N. Tomašev, I. Ktena, Z. Kenton,
M. Rodriguez, S. El-Sayed, S. Brown, C. Akbulut, A. Trask, E. Hughes, A. S. Bergman, R. Shelby,
N. Marchal, C. Griffin, J. Mateos-Garcia, L. Weidinger, W. Street, B. Lange, A. Ingerman, A. Lentz,
R. Enger, A. Barakat, V. Krakovna, J. O. Siy, Z. Kurth-Nelson, A. McCroskery, V. Bolina, H. Law,
M. Shanahan, L. Alberts, B. Balle, S. de Haas, Y. Ibitoye, A. Dafoe, B. Goldberg, S. Krier, A. Reese,
S. Witherspoon, W. Hawkins, M. Rauh, D. Wallace, M. Franklin, J. A. Goldstein, J. Lehman, M. Klenk,
S. Vallor, C. Biles, M. Ringel Morris, H. King, B. Agüera y Arcas, W. Isaac, and J. Manyika. The ethics
of advanced ai assistants. preprint, 2024. URL https://storage.googleapis.com/deepmind-
media/DeepMind.com/Blog/ethics-of-advanced-ai-assistants/the-ethics-of-
advanced-ai-assistants-2024-i.pdf.
T. K. Gandhi, D. Classen, C. A. Sinsky, D. C. Rhew, N. Vande Garde, A. Roberts, and F. Federico.
How can artificial intelligence decrease cognitive and work burden for front line practitioners?
JAMIA Open, 6(3):ooad079, 08 2023. ISSN 2574-2531. URL https://doi.org/10.1093/
jamiaopen/ooad079.
D. Ganguli, N. Schiefer, M. Favaro, and J. Clark. Challenges in evaluating AI systems, 2023. URL
https://www.anthropic.com/index/evaluating-ai-systems.
Gemini Team, R. Anil, S. Borgeaud, Y. Wu, J.-B. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai,
A. Hauth, K. Millican, D. Silver, S. Petrov, M. Johnson, I. Antonoglou, J. Schrittwieser, A. Glaese,
J. Chen, E. Pitler, T. Lillicrap, A. Lazaridou, O. Firat, J. Molloy, M. Isard, P. R. Barham, T. Hennigan,
B. Lee, F. Viola, M. Reynolds, Y. Xu, R. Doherty, E. Collins, C. Meyer, E. Rutherford, E. Moreira,
K. Ayoub, M. Goel, G. Tucker, E. Piqueras, M. Krikun, I. Barr, N. Savinov, I. Danihelka, B. Roelofs,
A. White, A. Andreassen, T. von Glehn, L. Yagati, M. Kazemi, L. Gonzalez, M. Khalman, J. Sygnowski,
A. Frechette, C. Smith, L. Culp, L. Proleev, Y. Luan, X. Chen, J. Lottes, N. Schucher, F. Lebron,
A. Rrustemi, N. Clay, P. Crone, T. Kocisky, J. Zhao, B. Perz, D. Yu, H. Howard, A. Bloniarz, J. W. Rae,
H. Lu, L. Sifre, M. Maggioni, F. Alcober, D. Garrette, M. Barnes, S. Thakoor, J. Austin, G. Barth-
Maron, W. Wong, R. Joshi, R. Chaabouni, D. Fatiha, A. Ahuja, R. Liu, Y. Li, S. Cogan, J. Chen,
C. Jia, C. Gu, Q. Zhang, J. Grimstad, A. J. Hartman, M. Chadwick, G. S. Tomar, X. Garcia, E. Senter,
E. Taropa, T. S. Pillai, J. Devlin, M. Laskin, D. d. L. Casas, D. Valter, C. Tao, L. Blanco, A. P. Badia,
D. Reitter, M. Chen, J. Brennan, C. Rivera, S. Brin, S. Iqbal, G. Surita, J. Labanowski, A. Rao,
S. Winkler, E. Parisotto, Y. Gu, K. Olszewska, Y. Zhang, R. Addanki, A. Miech, A. Louis, L. E. Shafey,
D. Teplyashin, G. Brown, E. Catt, N. Attaluri, J. Balaguer, J. Xiang, P. Wang, Z. Ashwood, A. Briukhov,
A. Webson, S. Ganapathy, S. Sanghavi, A. Kannan, M.-W. Chang, A. Stjerngren, J. Djolonga, Y. Sun,
A. Bapna, M. Aitchison, P. Pejman, H. Michalewski, T. Yu, C. Wang, J. Love, J. Ahn, D. Bloxwich,
K. Han, P. Humphreys, T. Sellam, J. Bradbury, V. Godbole, S. Samangooei, B. Damoc, A. Kaskasoli,
S. M. R. Arnold, V. Vasudevan, S. Agrawal, J. Riesa, D. Lepikhin, R. Tanburn, S. Srinivasan, H. Lim,
12

--- Page 13 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
S. Hodkinson, P. Shyam, J. Ferret, S. Hand, A. Garg, T. L. Paine, J. Li, Y. Li, M. Giang, A. Neitz,
Z. Abbas, S. York, M. Reid, E. Cole, A. Chowdhery, D. Das, D. Rogozińska, V. Nikolaev, P. Sprechmann,
Z. Nado, L. Zilka, F. Prost, L. He, M. Monteiro, G. Mishra, C. Welty, J. Newlan, D. Jia, M. Allamanis,
C. H. Hu, R. de Liedekerke, J. Gilmer, C. Saroufim, S. Rijhwani, S. Hou, D. Shrivastava, A. Baddepudi,
A. Goldin, A. Ozturel, A. Cassirer, Y. Xu, D. Sohn, D. Sachan, R. K. Amplayo, C. Swanson, D. Petrova,
S. Narayan, A. Guez, S. Brahma, J. Landon, M. Patel, R. Zhao, K. Villela, L. Wang, W. Jia, M. Rahtz,
M. Giménez, L. Yeung, H. Lin, J. Keeling, P. Georgiev, D. Mincu, B. Wu, S. Haykal, R. Saputro,
K. Vodrahalli, J. Qin, Z. Cankara, A. Sharma, N. Fernando, W. Hawkins, B. Neyshabur, S. Kim,
A. Hutter, P. Agrawal, A. Castro-Ros, G. v. d. Driessche, T. Wang, F. Yang, S.-y. Chang, P. Komarek,
R. McIlroy, M. Lučić, G. Zhang, W. Farhan, M. Sharman, P. Natsev, P. Michel, Y. Cheng, Y. Bansal,
S. Qiao, K. Cao, S. Shakeri, C. Butterfield, J. Chung, P. K. Rubenstein, S. Agrawal, A. Mensch,
K. Soparkar, K. Lenc, T. Chung, A. Pope, L. Maggiore, J. Kay, P. Jhakra, S. Wang, J. Maynez,
M. Phuong, T. Tobin, A. Tacchetti, M. Trebacz, K. Robinson, Y. Katariya, S. Riedel, P. Bailey, K. Xiao,
N. Ghelani, L. Aroyo, A. Slone, N. Houlsby, X. Xiong, Z. Yang, E. Gribovskaya, J. Adler, M. Wirth,
L. Lee, M. Li, T. Kagohara, J. Pavagadhi, S. Bridgers, A. Bortsova, S. Ghemawat, Z. Ahmed, T. Liu,
R. Powell, V. Bolina, M. Iinuma, P. Zablotskaia, J. Besley, D.-W. Chung, T. Dozat, R. Comanescu,
X. Si, J. Greer, G. Su, M. Polacek, R. L. Kaufman, S. Tokumine, H. Hu, E. Buchatskaya, Y. Miao,
M. Elhawaty, A. Siddhant, N. Tomasev, J. Xing, C. Greer, H. Miller, S. Ashraf, A. Roy, Z. Zhang,
A. Ma, A. Filos, M. Besta, R. Blevins, T. Klimenko, C.-K. Yeh, S. Changpinyo, J. Mu, O. Chang,
M. Pajarskas, C. Muir, V. Cohen, C. L. Lan, K. Haridasan, A. Marathe, S. Hansen, S. Douglas,
R. Samuel, M. Wang, S. Austin, C. Lan, J. Jiang, J. Chiu, J. A. Lorenzo, L. L. Sjösund, S. Cevey,
Z. Gleicher, T. Avrahami, A. Boral, H. Srinivasan, V. Selo, R. May, K. Aisopos, L. Hussenot, L. B.
Soares, K. Baumli, M. B. Chang, A. Recasens, B. Caine, A. Pritzel, F. Pavetic, F. Pardo, A. Gergely,
J. Frye, V. Ramasesh, D. Horgan, K. Badola, N. Kassner, S. Roy, E. Dyer, V. Campos, A. Tomala,
Y. Tang, D. E. Badawy, E. White, B. Mustafa, O. Lang, A. Jindal, S. Vikram, Z. Gong, S. Caelles,
R. Hemsley, G. Thornton, F. Feng, W. Stokowiec, C. Zheng, P. Thacker, c. Ünlü, Z. Zhang, M. Saleh,
J. Svensson, M. Bileschi, P. Patil, A. Anand, R. Ring, K. Tsihlas, A. Vezer, M. Selvi, T. Shevlane,
M. Rodriguez, T. Kwiatkowski, S. Daruki, K. Rong, A. Dafoe, N. FitzGerald, K. Gu-Lemberg, M. Khan,
L. A. Hendricks, M. Pellat, V. Feinberg, J. Cobon-Kerr, T. Sainath, M. Rauh, S. H. Hashemi, R. Ives,
Y. Hasson, Y. Li, E. Noland, Y. Cao, N. Byrd, L. Hou, Q. Wang, T. Sottiaux, M. Paganini, J.-B.
Lespiau, A. Moufarek, S. Hassan, K. Shivakumar, J. van Amersfoort, A. Mandhane, P. Joshi, A. Goyal,
M. Tung, A. Brock, H. Sheahan, V. Misra, C. Li, N. Rakićević, M. Dehghani, F. Liu, S. Mittal, J. Oh,
S. Noury, E. Sezener, F. Huot, M. Lamm, N. De Cao, C. Chen, G. Elsayed, E. Chi, M. Mahdieh,
I. Tenney, N. Hua, I. Petrychenko, P. Kane, D. Scandinaro, R. Jain, J. Uesato, R. Datta, A. Sadovsky,
O. Bunyan, D. Rabiej, S. Wu, J. Zhang, G. Vasudevan, E. Leurent, M. Alnahlawi, I. Georgescu,
N. Wei, I. Zheng, B. Chan, P. G. Rabinovitch, P. Stanczyk, Y. Zhang, D. Steiner, S. Naskar, M. Azzam,
M. Johnson, A. Paszke, C.-C. Chiu, J. S. Elias, A. Mohiuddin, F. Muhammad, J. Miao, A. Lee,
N. Vieillard, S. Potluri, J. Park, E. Davoodi, J. Zhang, J. Stanway, D. Garmon, A. Karmarkar, Z. Dong,
J. Lee, A. Kumar, L. Zhou, J. Evens, W. Isaac, Z. Chen, J. Jia, A. Levskaya, Z. Zhu, C. Gorgolewski,
P. Grabowski, Y. Mao, A. Magni, K. Yao, J. Snaider, N. Casagrande, P. Suganthan, E. Palmer,
G. Irving, E. Loper, M. Faruqui, I. Arkatkar, N. Chen, I. Shafran, M. Fink, A. Castaño, I. Giannoumis,
W. Kim, M. Rybiński, A. Sreevatsa, J. Prendki, D. Soergel, A. Goedeckemeyer, W. Gierke, M. Jafari,
M. Gaba, J. Wiesner, D. G. Wright, Y. Wei, H. Vashisht, Y. Kulizhskaya, J. Hoover, M. Le, L. Li,
C. Iwuanyanwu, L. Liu, K. Ramirez, A. Khorlin, A. Cui, T. LIN, M. Georgiev, M. Wu, R. Aguilar,
K. Pallo, A. Chakladar, A. Repina, X. Wu, T. van der Weide, P. Ponnapalli, C. Kaplan, J. Simsa,
S. Li, O. Dousse, F. Yang, J. Piper, N. Ie, M. Lui, R. Pasumarthi, N. Lintz, A. Vijayakumar, L. N.
Thiet, D. Andor, P. Valenzuela, C. Paduraru, D. Peng, K. Lee, S. Zhang, S. Greene, D. D. Nguyen,
P. Kurylowicz, S. Velury, S. Krause, C. Hardin, L. Dixon, L. Janzer, K. Choo, Z. Feng, B. Zhang,
A. Singhal, T. Latkar, M. Zhang, Q. Le, E. A. Abellan, D. Du, D. McKinnon, N. Antropova, T. Bolukbasi,
13

--- Page 14 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
O. Keller, D. Reid, D. Finchelstein, M. A. Raad, R. Crocker, P. Hawkins, R. Dadashi, C. Gaffney,
S. Lall, K. Franko, E. Filonov, A. Bulanova, R. Leblond, V. Yadav, S. Chung, H. Askham, L. C. Cobo,
K. Xu, F. Fischer, J. Xu, C. Sorokin, C. Alberti, C.-C. Lin, C. Evans, H. Zhou, A. Dimitriev, H. Forbes,
D. Banarse, Z. Tung, J. Liu, M. Omernick, C. Bishop, C. Kumar, R. Sterneck, R. Foley, R. Jain,
S. Mishra, J. Xia, T. Bos, G. Cideron, E. Amid, F. Piccinno, X. Wang, P. Banzal, P. Gurita, H. Noga,
P. Shah, D. J. Mankowitz, A. Polozov, N. Kushman, V. Krakovna, S. Brown, M. Bateni, D. Duan,
V. Firoiu, M. Thotakuri, T. Natan, A. Mohananey, M. Geist, S. Mudgal, S. Girgin, H. Li, J. Ye,
O. Roval, R. Tojo, M. Kwong, J. Lee-Thorp, C. Yew, Q. Yuan, S. Bagri, D. Sinopalnikov, S. Ramos,
J. Mellor, A. Sharma, A. Severyn, J. Lai, K. Wu, H.-T. Cheng, D. Miller, N. Sonnerat, D. Vnukov,
R. Greig, J. Beattie, E. Caveness, L. Bai, J. Eisenschlos, A. Korchemniy, T. Tsai, M. Jasarevic, W. Kong,
P. Dao, Z. Zheng, F. Liu, F. Yang, R. Zhu, M. Geller, T. H. Teh, J. Sanmiya, E. Gladchenko, N. Trdin,
A. Sozanschi, D. Toyama, E. Rosen, S. Tavakkol, L. Xue, C. Elkind, O. Woodman, J. Carpenter,
G. Papamakarios, R. Kemp, S. Kafle, T. Grunina, R. Sinha, A. Talbert, A. Goyal, D. Wu, D. Owusu-
Afriyie, C. Du, C. Thornton, J. Pont-Tuset, P. Narayana, J. Li, S. Fatehi, J. Wieting, O. Ajmeri,
B. Uria, T. Zhu, Y. Ko, L. Knight, A. Héliou, N. Niu, S. Gu, C. Pang, D. Tran, Y. Li, N. Levine,
A. Stolovich, N. Kalb, R. Santamaria-Fernandez, S. Goenka, W. Yustalim, R. Strudel, A. Elqursh,
B. Lakshminarayanan, C. Deck, S. Upadhyay, H. Lee, M. Dusenberry, Z. Li, X. Wang, K. Levin,
R. Hoffmann, D. Holtmann-Rice, O. Bachem, S. Yue, S. Arora, E. Malmi, D. Mirylenka, Q. Tan,
C. Koh, S. H. Yeganeh, S. Põder, S. Zheng, F. Pongetti, M. Tariq, Y. Sun, L. Ionita, M. Seyedhosseini,
P. Tafti, R. Kotikalapudi, Z. Liu, A. Gulati, J. Liu, X. Ye, B. Chrzaszcz, L. Wang, N. Sethi, T. Li,
B. Brown, S. Singh, W. Fan, A. Parisi, J. Stanton, C. Kuang, V. Koverkathu, C. A. Choquette-Choo,
Y. Li, T. J. Lu, A. Ittycheriah, P. Shroff, P. Sun, M. Varadarajan, S. Bahargam, R. Willoughby,
D. Gaddy, I. Dasgupta, G. Desjardins, M. Cornero, B. Robenek, B. Mittal, B. Albrecht, A. Shenoy,
F. Moiseev, H. Jacobsson, A. Ghaffarkhah, M. Rivière, A. Walton, C. Crepy, A. Parrish, Y. Liu, Z. Zhou,
C. Farabet, C. Radebaugh, P. Srinivasan, C. van der Salm, A. Fidjeland, S. Scellato, E. Latorre-
Chimoto, H. Klimczak-Plucińska, D. Bridson, D. de Cesare, T. Hudson, P. Mendolicchio, L. Walker,
A. Morris, I. Penchev, M. Mauger, A. Guseynov, A. Reid, S. Odoom, L. Loher, V. Cotruta, M. Yenugula,
D. Grewe, A. Petrushkina, T. Duerig, A. Sanchez, S. Yadlowsky, A. Shen, A. Globerson, A. Kurzrok,
L. Webb, S. Dua, D. Li, P. Lahoti, S. Bhupatiraju, D. Hurt, H. Qureshi, A. Agarwal, T. Shani, M. Eyal,
A. Khare, S. R. Belle, L. Wang, C. Tekur, M. S. Kale, J. Wei, R. Sang, B. Saeta, T. Liechty, Y. Sun,
Y. Zhao, S. Lee, P. Nayak, D. Fritz, M. R. Vuyyuru, J. Aslanides, N. Vyas, M. Wicke, X. Ma, T. Bilal,
E. Eltyshev, D. Balle, N. Martin, H. Cate, J. Manyika, K. Amiri, Y. Kim, X. Xiong, K. Kang, F. Luisier,
N. Tripuraneni, D. Madras, M. Guo, A. Waters, O. Wang, J. Ainslie, J. Baldridge, H. Zhang, G. Pruthi,
J. Bauer, F. Yang, R. Mansour, J. Gelman, Y. Xu, G. Polovets, J. Liu, H. Cai, W. Chen, X. Sheng,
E. Xue, S. Ozair, A. Yu, C. Angermueller, X. Li, W. Wang, J. Wiesinger, E. Koukoumidis, Y. Tian,
A. Iyer, M. Gurumurthy, M. Goldenson, P. Shah, M. K. Blake, H. Yu, A. Urbanowicz, J. Palomaki,
C. Fernando, K. Brooks, K. Durden, H. Mehta, N. Momchev, E. Rahimtoroghi, M. Georgaki, A. Raul,
S. Ruder, M. Redshaw, J. Lee, K. Jalan, D. Li, G. Perng, B. Hechtman, P. Schuh, M. Nasr, M. Chen,
K. Milan, V. Mikulik, T. Strohman, J. Franco, T. Green, D. Hassabis, K. Kavukcuoglu, J. Dean, and
O. Vinyals. Gemini: a family of highly capable multimodal models. arXiv preprint, Dec. 2023. URL
http://arxiv.org/abs/2312.11805.
n. Gemini Team, R. Anil, S. Borgeaud, Y. Wu, J.-B. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai,
A. Hauth, et al. Gemini: a family of highly capable multimodal models; v1 update. arXiv preprint
arXiv:2312.11805, 2024.
A. Genus and A. Stirling. Collingridge and the dilemma of control: towards responsible and accountable
innovation. Research Policy, 47(1):61–69, Feb. 2018. ISSN 00487333. URL https://linkinghub.
elsevier.com/retrieve/pii/S0048733317301622.
A. Glaese, N. McAleese, M. Trębacz, J. Aslanides, V. Firoiu, T. Ewalds, M. Rauh, L. Weidinger,
14

--- Page 15 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
M. Chadwick, P. Thacker, L. Campbell-Gillingham, J. Uesato, P.-S. Huang, R. Comanescu, F. Yang,
A. See, S. Dathathri, R. Greig, C. Chen, D. Fritz, J. S. Elias, R. Green, S. Mokrá, N. Fernando, B. Wu,
R. Foley, S. Young, I. Gabriel, W. Isaac, J. Mellor, D. Hassabis, K. Kavukcuoglu, L. A. Hendricks, and
G. Irving. Improving alignment of dialogue agents via targeted human judgements. arXiv preprint,
Sept. 2022. URL http://arxiv.org/abs/2209.14375.
Google. Generative ai prohibited use policy, 2023a. URL https://policies.google.com/terms/
generative-ai/use-policy.
Google.
Ai principles progress update 2023, 2023b.
URL https://ai.google/static/
documents/ai-principles-2023-progress-update.pdf.
Google.
Anthropic,
Google,
Microsoft
and
OpenAI
announce
Executive
Director
of
the
Frontier
Model
Forum
and
over
$10
million
for
a
new
AI
Safety
Fund,
Oct.
2023c.
URL https://blog.google/outreach-initiatives/public-policy/google-
microsoft-anthropic-open-ai-frontier-model-forum-executive-director/.
S. Habib, T. Vogel, X. Anli, and E. Thorne. How does generative artificial intelligence impact student
creativity? Journal of Creativity, 34(1):100072, 2024. ISSN 2713-3745. URL https://www.
sciencedirect.com/science/article/pii/S2713374523000316.
D. Hendrycks and M. Mazeika. X-risk analysis for AI research. arXiv preprint, Sept. 2022. URL
http://arxiv.org/abs/2206.05862.
W. House.
President biden issues executive order on safe, secure, and trustworthy artificial
intelligence, Oct. 2023. URL https://www.whitehouse.gov/briefing-room/statements-
releases/2023/10/30/fact-sheet-president-biden-issues-executive-order-
on-safe-secure-and-trustworthy-artificial-intelligence/.
J. Hu, S. Ruder, A. Siddhant, G. Neubig, O. First, and M. Johnson. XTREME: a massively multilingual
multi-task benchmark for evaluating cross-lingual generalization. In Proceedings of machine learning
research, volume 119, 2020. URL https://proceedings.mlr.press/v119/hu20b/hu20b.
pdf.
A. Z. Jacobs and H. Wallach. Measurement and fairness. In Proceedings of the 2021 ACM conference
on fairness, accountability, and transparency, pages 375–385, 2021.
M. Jakesch, A. Bhat, D. Buschek, L. Zalmanson, and M. Naaman. Co-writing with opinionated
language models affects users’ views. In Proceedings of the 2023 CHI Conference on Human Factors
in Computing Systems, pages 1–15, 2023.
R. Kohavi, D. Tang, and Y. Xu. Trustworthy online controlled experiments: a practical guide to A/B
testing. Cambridge University Press, Cambridge, 2020.
F. Liu, E. Bugliarello, E. M. Ponti, S. Reddy, N. Collier, and D. Elliott. Visually grounded reasoning across
languages and cultures. arXiv preprint, Oct. 2021. URL http://arxiv.org/abs/2109.13238.
A. S. Luccioni, C. Akiki, M. Mitchell, and Y. Jernite. Stable bias: Analyzing societal representations in
diffusion models. arXiv preprint arXiv:2303.11408, 2023a.
A. S. Luccioni, S. Viguier, and A.-L. Ligozat. Estimating the carbon footprint of bloom, a 176b parameter
language model. Journal of Machine Learning Research, 24(253):1–15, 2023b.
15

--- Page 16 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
S. Mohamed, M.-T. Png, and W. Isaac. Decolonial AI: decolonial theory as sociotechnical foresight
in artificial intelligence. Philosophy & Technology, 33(4):659–684, Dec. 2020. ISSN 2210-5433,
2210-5441. URL https://link.springer.com/10.1007/s13347-020-00405-8.
J. Mökander, J. Schuett, H. R. Kirk, and L. Floridi. Auditing large language models: a three-layered
approach. AI and Ethics, May 2023. ISSN 2730-5953, 2730-5961. URL https://link.springer.
com/10.1007/s43681-023-00289-2.
H. Nori, N. King, S. M. McKinney, D. Carignan, and E. Horvitz. Capabilities of GPT-4 on medical
challenge problems. arXiv preprint, Apr. 2023. URL http://arxiv.org/abs/2303.13375.
OpenAI. GPT-4V(ision) system card, Sept. 2023. URL https://cdn.openai.com/papers/GPTV_
System_Card.pdf.
R. Owen, P. M. Stilgoe, and J. Bessant. A framework for responsible innovation. In Responsible
innovation: managing the responsible emergence of science and innovation in society, pages 27–50.
Wiley, 2013.
A. Parrish, A. Chen, N. Nangia, V. Padmakumar, J. Phang, J. Thompson, P. M. Htut, and S. R. Bowman.
BBQ: a hand-built bias benchmark for question answering.
arXiv preprint, Mar. 2021.
URL
http://arxiv.org/abs/2110.08193.
A. Paterson and W. Hawkins. Best practices for data enrichment, Oct. 2022a. URL https://
deepmind.google/discover/blog/best-practices-for-data-enrichment/.
A. Paterson and W. Hawkins. Best practices for data enrichment, Nov. 2022b. URL https://
deepmind.google/discover/blog/best-practices-for-data-enrichment/.
I. Pentina, T. Hancock, and T. Xie. Exploring relationship development with social chatbots: a mixed-
method study of Replika. Computers in Human Behavior, 140:107600, Mar. 2023. ISSN 07475632.
URL https://linkinghub.elsevier.com/retrieve/pii/S0747563222004204.
E. Perez, S. Huang, F. Song, T. Cai, R. Ring, J. Aslanides, A. Glaese, N. McAleese, and G. Irving.
Red teaming language models with language models. arXiv preprint, Feb. 2022. URL http:
//arxiv.org/abs/2202.03286.
M. Phuong, M. Aitchison, E. Catt, S. Cogan, A. Kaskasoli, V. Krakovna, D. Lindner, M. Rahtz, Y. Assael,
S. Hodkinson, H. Howard, T. Lieberum, R. Kumar, M. A. Raad, A. Webson, L. Ho, S. Lin, S. Farquhar,
M. Hutter, G. Deletang, A. Ruoss, S. El-Sayed, S. Brown, A. Dragan, R. Shah, A. Dafoe, and
T. Shevlane. Evaluating frontier models for dangerous capabilities. arxiv preprint, Mar. 2024. URL
https://arxiv.org/abs/2403.13793.
J. W. Rae, S. Borgeaud, T. Cai, K. Millican, J. Hoffmann, F. Song, J. Aslanides, S. Henderson, R. Ring,
S. Young, et al. Scaling language models: Methods, analysis & insights from training gopher. arXiv
preprint arXiv:2112.11446, 2021.
I. D. Raji, A. Smart, R. N. White, M. Mitchell, T. Gebru, B. Hutchinson, J. Smith-Loud, D. Theron, and
P. Barnes. Closing the AI accountability gap: Defining an end-to-end framework for internal algo-
rithmic auditing. In Proceedings of the 2020 conference on fairness, accountability, and transparency,
pages 33–44, 2020.
I. D. Raji, E. M. Bender, A. Paullada, E. Denton, and A. Hanna. AI and the everything in the whole
wide world benchmark. arXiv preprint, 2021. URL https://arxiv.org/abs/2111.15366.
16

--- Page 17 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
S. Rismani, R. Shelby, A. Smart, E. Jatho, J. Kroll, A. Moon, and N. Rostamzadeh. From plane
crashes to algorithmic harm: applicability of safety engineering frameworks for responsible ML. In
Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems, pages 1–18, 2023.
URL https://doi.org/10.1145/3544548.3581407.
M. Roberts, H. Thakur, C. Herlihy, C. White, and S. Dooley. Data contamination through the lens of
time. arXiv preprint, Oct. 2023. URL http://arxiv.org/abs/2310.10628.
W. A. G. Rojas, S. Diamos, K. R. Kini, D. Kanter, V. J. Reddi, and C. Coleman. The dollar street dataset:
Images representing the geographic and socioeconomic diversity of the world. In Thirty-sixth
Conference on Neural Information Processing Systems Datasets and Benchmarks Track, 2022.
G. E. Schall. Underwriters’ laboratories: testing for public safety. IEEE Transactions on Industry and
General Applications, IGA-6(5):425–429, Sept. 1970. ISSN 0018-943X. URL http://ieeexplore.
ieee.org/document/4181210/.
C. Schumann, S. Ricco, U. Prabhu, V. Ferrari, and C. Pantofaru. A step toward more inclusive people
annotations for fairness. In Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society,
pages 916–925, 2021.
R. Shelby, S. Rismani, K. Henne, A. Moon, N. Rostamzadeh, P. Nicholas, N. Yilla-Akbari, J. Gallegos,
A. Smart, E. Garcia, and G. Virk. Sociotechnical harms of algorithmic systems: scoping a taxonomy
for harm reduction. In Proceedings of the 2023 AAAI/ACM Conference on AI, Ethics, and Society,
pages 723–741, Montréal QC Canada, Aug. 2023. ACM. ISBN 9798400702310. URL https:
//dl.acm.org/doi/10.1145/3600211.3604673.
T. Shevlane. Structured access: an emerging paradigm for safe AI deployment. arXiv preprint, 2022.
URL https://arxiv.org/abs/2201.05159.
T. Shevlane, S. Farquhar, B. Garfinkel, M. Phuong, J. Whittlestone, J. Leung, D. Kokotajlo, N. Marchal,
M. Anderljung, N. Kolt, L. Ho, D. Siddarth, S. Avin, W. Hawkins, B. Kim, I. Gabriel, V. Bolina,
J. Clark, Y. Bengio, P. Christiano, and A. Dafoe. Model evaluation for extreme risks. arXiv preprint,
Sept. 2023. URL http://arxiv.org/abs/2305.15324.
K. Singhal, S. Azizi, T. Tu, S. S. Mahdavi, J. Wei, H. W. Chung, N. Scales, A. Tanwani, H. Cole-Lewis,
S. Pfohl, P. Payne, M. Seneviratne, P. Gamble, C. Kelly, N. Scharli, A. Chowdhery, P. Mansfield, B. A. y.
Arcas, D. Webster, G. S. Corrado, Y. Matias, K. Chou, J. Gottweis, N. Tomasev, Y. Liu, A. Rajkomar,
J. Barral, C. Semturs, A. Karthikesalingam, and V. Natarajan. Large language models encode clinical
knowledge. arXiv preprint, Dec. 2022. URL http://arxiv.org/abs/2212.13138.
I. Solaiman, Z. Talat, W. Agnew, L. Ahmad, D. Baker, S. L. Blodgett, H. Daumé III, J. Dodge, E. Evans,
S. Hooker, et al. Evaluating the social impact of generative AI systems in systems and society. arXiv
preprint, 2023. URL https://arxiv.org/abs/2306.05949.
D. Teney, K. Kafle, R. Shrestha, E. Abbasnejad, C. Kanan, and A. van den Hengel. On the value
of out-of-distribution testing: an example of Goodhart’s law. In Advances in Neural Information
Processing Systems 33 (NeurIPS 2020), Vancouver, Canada, 2020. URL https://proceedings.
neurips.cc/paper/2020/file/045117b0e0a11a242b9765e79cbf113f-Paper.pdf.
R. Tourangeau. Cognitive aspects of survey measurement and mismeasurement. International
Journal of Public Opinion Research, 15(1):3–7, Mar. 2003. ISSN 13534505, 14643677. URL
https://doi.org/10.1093/ijpor/15.1.3.
17

--- Page 18 ---

Holistic Safety and Responsibility Evaluations of Advanced AI Models
A. Trask, E. Bluemke, B. Garfinkel, C. G. Cuervas-Mons, and A. Dafoe. Structured transparency: a
framework for addressing use/mis-use trade-offs when sharing information. arXiv preprint, 2024.
URL https://arxiv.org/abs/2012.08347.
UK Government.
‘State of the science’ report to understand capabilities and risks of
frontier AI: statement by the Chair,
2 November 2023,
Nov. 2023.
URL https:
//www.gov.uk/government/publications/ai-safety-summit-2023-chairs-
statement-state-of-the-science-2-november/state-of-the-science-report-
to-understand-capabilities-and-risks-of-frontier-ai-statement-by-the-
chair-2-november-2023.
L. Weidinger, J. Uesato, M. Rauh, C. Griffin, P.-S. Huang, J. Mellor, A. Glaese, M. Cheng, B. Balle,
A. Kasirzadeh, C. Biles, S. Brown, Z. Kenton, W. Hawkins, T. Stepleton, A. Birhane, L. A. Hendricks,
L. Rimell, W. Isaac, J. Haas, S. Legassick, G. Irving, and I. Gabriel. Taxonomy of risks posed
by language models.
In 2022 ACM Conference on Fairness, Accountability, and Transparency,
pages 214–229, Seoul Republic of Korea, June 2022. ACM. ISBN 9781450393522. URL https:
//dl.acm.org/doi/10.1145/3531146.3533088.
L. Weidinger, M. Rauh, N. Marchal, A. Manzini, L. A. Hendricks, J. Mateos-Garcia, S. Bergman,
J. Kay, C. Griffin, B. Bariach, I. Gabriel, V. Rieser, and W. Isaac. Sociotechnical safety evaluation of
generative AI systems. arXiv preprint, Oct. 2023. URL http://arxiv.org/abs/2310.11986.
White House. Ensuring safe, secure, and trustworthy AI, 2023. URL https://www.whitehouse.
gov/wp-content/uploads/2023/07/Ensuring-Safe-Secure-and-Trustworthy-
AI.pdf.
N. Wichers, C. Denison, and A. Beirami. Gradient-based language model red teaming. arXiv preprint,
Jan. 2024. URL http://arxiv.org/abs/2401.16656.
F. Wu and J. V. Rodricks. Forty years of food safety risk assessment: a history and analysis. Risk Analysis,
40(S1):2218–2230, Nov. 2020. ISSN 0272-4332, 1539-6924. URL https://onlinelibrary.
wiley.com/doi/10.1111/risa.13624.
Z.-X. Yong, C. Menghini, and S. H. Bach. Low-resource languages jailbreak gpt-4. arXiv preprint
arXiv:2310.02446, 2023.
A. Zou, Z. Wang, N. Carlini, M. Nasr, J. Z. Kolter, and M. Fredrikson. Universal and transferable
adversarial attacks on aligned language models. arXiv preprint, Dec. 2023. URL http://arxiv.
org/abs/2307.15043.
18

```
