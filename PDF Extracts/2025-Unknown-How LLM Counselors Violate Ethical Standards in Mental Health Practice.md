---
title: "2025-Unknown-How LLM Counselors Violate Ethical Standards in Mental Health Practice - PDF Extract"
source_pdf: "2025-Unknown-How LLM Counselors Violate Ethical Standards in Mental Health Practice.pdf"
pages: 13
extracted_at: "2026-02-08T06:02:21.125692"
---

# PDF Extract: 2025-Unknown-How LLM Counselors Violate Ethical Standards in Mental Health Practice

**Source PDF:** 2025-Unknown-How LLM Counselors Violate Ethical Standards in Mental Health Practice.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

How LLM Counselors Violate Ethical Standards in Mental Health Practice:
A Practitioner-Informed Framework
Zainab Iftikhar1, Amy Xiao1, Sean Ransom2,3, Jeff Huang1, Harini Suresh1
1Department of Computer Science, Brown University
2Department of Psychiatry, LSU Health Sciences Center
3Cognitive Behavioral Therapy Center of New Orleans
zainab iftikhar@brown.edu, amy xiao@alumni.brown.edu, sransom@cbtnola.com,
{jeff huang, harini suresh}@brown.edu
Abstract
Large language models (LLMs) were not designed to replace
healthcare workers, but they are being used in ways that can
lead users to overestimate the types of roles that these systems
can assume. While prompt engineering has been shown to im-
prove LLMs’ clinical effectiveness in mental health applica-
tions, little is known about whether such strategies help mod-
els adhere to ethical principles for real-world deployment. In
this study, we conducted an 18-month ethnographic collab-
oration with mental health practitioners (three clinically li-
censed psychologists and seven trained peer counselors) to
map LLM counselors’ behavior during a session to profes-
sional codes of conduct established by organizations like the
American Psychological Association (APA). Through qual-
itative analysis and expert evaluation of N = 137 sessions
(110 self-counseling; 27 simulated), we outline a framework
of 15 ethical violations mapped to 5 major themes. These in-
clude: Lack of Contextual Understanding, where the coun-
selor fails to account for users’ lived experiences, leading
to oversimplified, contextually irrelevant, and one-size-fits-
all intervention; Poor Therapeutic Collaboration, where the
counselor’s low turn-taking behavior and invalidating outputs
limit users’ agency over their therapeutic experience; De-
ceptive Empathy, where the counselor’s simulated anthro-
pomorphic responses (“I hear you”, “I understand”) cre-
ate a false sense of emotional connection; Unfair Discrim-
ination, where the counselor’s responses exhibit algorithmic
bias and cultural insensitivity toward marginalized popula-
tions; and Lack of Safety & Crisis Management, where in-
dividuals who are “knowledgeable enough” to correct LLM
outputs are at an advantage, while others, due to lack of
clinical knowledge and digital literacy, are more likely to
suffer from clinically inappropriate responses. Reflecting on
these findings through a practitioner-informed lens, we ar-
gue that reducing psychotherapy—a deeply meaningful and
relational process—to a language generation task can have
serious and harmful implications in practice. We conclude
by discussing policy-oriented accountability mechanisms for
emerging LLM counselors.
1
Introduction
Large language models (LLMs) are increasingly being used
for mental health support, including social companions (e.g.,
Copyright © 2025, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
Character.AI1, Replika2) and therapy chatbots (e.g., Woe-
bot Health3 (Prochaska et al. 2021), Therabot4 (Heinz et al.
2025)). These platforms market themselves as “the AI com-
panion who cares” or “the AI that works like a therapist.”
Within Character.AI, for example, an AI persona named
THERAPIST claims to be a Licensed Clinical Professional
Counselor trained to provide Cognitive Behavioral Therapy
(CBT). Accompanying this bold statement is a small dis-
claimer at the bottom of the page: This is A.I. and not a real
person. Treat everything it says as fiction. THERAPIST has
facilitated over 40.1 million conversations.
The increasing popularity of chatbot therapists has raised
ethical concerns and questions around the capacity of these
systems to replace human experts (Fiske, Henningsen, and
Buyx 2019; Aktan, Turhan, and Dolu 2022; Van Heerden,
Pozuelo, and Kohrt 2023; Sedlakova and Trachsel 2023;
Chandra et al. 2025; Moore et al. 2025). This tension gained
further public attention when the National Eating Disorders
Association (NEDA) replaced its entire human helpline staff
with an AI chatbot only to suspend it five days later after it
encouraged unhealthy eating behaviors (Singer 2023).
Prior work in LLM-based mental health suggests that
prompting models with evidence-based psychotherapeutic
techniques improves their clinical performance (Cho et al.
2023; Gu and Zhu 2023; Xu et al. 2024; Kian et al. 2024;
Sun et al. 2025), suggesting that appropriate prompting can
scale psychotherapy and reduce practitioners’ workloads.
However, there remains a lack of empirical investigation
grounded in real-world interactions to understand whether
such strategies help models adhere to ethical principles.
How do models prompted in this way actually behave in
practice? And how do those behaviors align with—or di-
verge from—established ethical standards? There is cur-
rently a limited understanding of both (a) challenges that
emerge when an LLM is prompted to act as a therapist (a
setup we will refer to as an LLM counselor), and (b) how
LLM counselors, even when prompted to follow evidence-
based principles, might violate the ethical standards that
govern mental health practice.
1https://character.ai
2https://replika.com
3https://woebothealth.com/
4https://www.trytherabot.com/
Proceedings of the Eighth AAAI/ACM Conference on AI, Ethics, and Society (AIES 2025)
1311

--- Page 2 ---

By examining when and how LLM counselors deviate
from established ethical principles, especially when de-
ployed in quasi-therapeutic roles, we can better understand
the risks and potential harms that arise when users rely on
them, or attempt to substitute them, for professional care.
We ask the following research questions:
• What ethical, therapeutic, and practical risks are ob-
served during the development and evaluation of LLM
counselors for psychotherapy, as evaluated by Mental
Health Practitioners (MHPs)?
• How can these risks be systematically identified, catego-
rized, and mapped onto established codes of conduct in
mental health practice?
To answer our research questions in a manner that re-
flects the current landscape of discussion around LLM coun-
selors, we sought a multi-faceted perspective from 1) seven
trained peer counselors from an online mental health support
platform working on creating and evaluating therapy-based
prompts for LLM counselors, and 2) three licensed psychol-
ogists experienced in evaluating ethical violations and ther-
apeutic risks in psychotherapy.
Over 18 months, we conducted a naturalistic, longitudi-
nal ethnographic study with peer counselors who conducted
N = 110 self-counseling sessions while iteratively refining
evidence-based system prompts for various LLMs (GPT-3.0,
GPT-3.5, GPT-4, Llama 3.1 and 3.2, Claude 3 Sonnet and
Claude 3 Haiku). Counselors met weekly to discuss the situ-
ated challenges they observed while creating and evaluating
these prompts to align models’ behavior with psychotherapy
principles. Next, to contextualize these risks within clinical
standards, we simulated N = 27 publicly available sessions
with an LLM counselor using publicly available transcripts.
Three licensed clinical psychologists independently evalu-
ated the sessions for ethical violations and therapeutic harm.
Through data triangulation of peer counselor observations
and clinical psychologist evaluations, we provide a frame-
work demonstrating how LLM counselors violate ethical
principles and professional standards in therapeutic practice
despite prompt engineering efforts.
Our findings reveal 15 risks that persist across LLM ar-
chitectures and prompt strategies divided into five themes.
These include: 1) Lack of Contextual Understanding (re-
sulting in a rigid therapeutic process uninformed by user’s
lived experience); 2) Poor Therapeutic Collaboration (ev-
idenced by authoritative, misleading responses that reinforce
users’ negative beliefs); 3) Deceptive Empathy (where sim-
ulated empathetic responses create a false sense of under-
standing and trust); (4) Unfair Discrimination (exhibiting
systemic biases against certain non-dominant groups, rein-
forcing marginalization within therapeutic interactions) and
(5) Lack of Safety & Crisis Management (such as an in-
ability to appropriately navigate sensitive issues like suicidal
feelings or provide safety mechanisms for users who are less
familiar with the therapy process).
We argue that mental health support, especially psy-
chotherapy, cannot be approached as a formulaic computa-
tional task, as it demands strict adherence to ethical stan-
dards and professional codes of conduct, something LLMs
are prone to violating in real-world practice. Without clear
legal guidelines and regulatory frameworks, LLM coun-
selors risk exposing vulnerable users to unmitigated harm.
2
Related Work
2.1
Ethical Code of Conduct and Standards in
Mental Health Practice
Professional organizations such as the American Psycho-
logical Association (APA) (2017), the American Counsel-
ing Association (ACA) (2014), the National Association of
Social Workers (NASW) (2021), and the U.S. Department
of Veterans Affairs (2023b; 2023a) have each published
codes to help guide the ethical practice of psychotherapy to
train and guide mental health therapists5, with correspond-
ing codes published by similar entities in other nations (e.g.,
Canadian Psychological Association (2017) and U.K. Na-
tional Institute for Health and Care Excellence (2005)).
Although there are occasional differences between the
various codes published by different professional groups,
they are largely similar and share a focus on protecting in-
dividuals and the public (Leach and Harbin 1997). Ethics
codes, by nature, are both aspirational and follow value-
centered principles that serve as a guide to therapists in
making decisions that will benefit both their patients and
society. For example, APA has identified five core values,
which it categorizes under General Principles, to provide
the moral foundation of the code and guide its recommen-
dations. These five values are 1) Beneficence and Nonmalef-
icence; 2) Fidelity and Responsibility; 3) Integrity; 4) Jus-
tice; and 5) Respect for People’s Rights and Dignity. Beyond
General Principles, the Code of Conduct outlines Ethi-
cal Standards: specific, enforceable guidelines to ensure
that professionals in psychotherapy uphold ethical behav-
ior, competence, privacy, and respect for individuals regard-
less of their age, gender, culture, socio-economic status or
more (Campbell et al. 2010; American Psychological Asso-
ciation 2017). These standards include aspects such as oper-
ating within boundaries of competence or otherwise provid-
ing relevant referrals (Code 2.01), identifying and prevent-
ing exploitative relationships (Code 3.04, Code 3.08), and
basing their work on scientific and professional judgment
(Code 2.04).
In addition, other organizations like the Council for Ac-
creditation of Counseling and Related Educational Programs
(CACREP) provide their own standards for mental health
practice, which are enforced for practitioners on a legal basis
by state regulators’ licensure requirements (e.g., NY State
Education Law6 and Regulations of the Commissioner of
Education7). These mandates further outline the ethical and
5In healthcare, the term “therapist” can apply to a range of
professionals (including social workers, counselors, practitioners,
psychiatrists, or psychologists). For simplicity, we will use “coun-
selor” when referring to LLMs (since we argue against LLMs
as therapists), and interchangeably use “therapist,” “psychologist”
(following APA’s standards), or more broadly, “mental health prac-
titioners” (MHPs) when referring to human therapists.
6Article 163, Section 8402
7Section 52.32 and Subpart 79-9
1312

--- Page 3 ---

legal responsibilities of an accredited practitioner. Translat-
ing APA’s aforementioned ethical standards of competency,
these requirements encompass a comprehensive understand-
ing of topics such as “identify[ing] substance use, addic-
tions, and co-occurring conditions,” “assessing and respond-
ing to risk of aggression or danger to others, self-inflicted
harm, and suicide,” and “identifying and reporting signs of
abuse and neglect.” Additionally, CACREP’s standard for-
malizes the need for “theories and models of counseling,
including relevance to clients from diverse cultural back-
grounds” (Council for Accreditation of Counseling and Re-
lated Educational Programs 2024).
However, while human practitioners are regulated by
a wide range of ethical, educational, and legal stan-
dards, ongoing developments in LLM counselors have not
been subject to and examined with the same level of
scrutiny (Khawaja and B´elisle-Pipon 2023).
2.2
Challenges of Deploying LLM Counselors
Several challenges have been documented when consider-
ing the applicability of LLMs in mental health settings, in-
cluding poor quality of care, misinformation, toxic content,
stigma, potential psychological harm, biased and harmful
outputs, and cultural limitations (Fiske, Henningsen, and
Buyx 2019; Sedlakova and Trachsel 2023; Qiu et al. 2023;
Cabrera et al. 2023; Akbulut et al. 2024; Aleem, Zahoor, and
Naseem 2024; Lawrence et al. 2024). For example, Gabriel
et al. (2024) found that LLMs’ responses to Black users
had lower levels of empathy than for any other demographic
group. Meanwhile, Lin et al. (2022) demonstrated that mod-
els typically associate stereotypes such as anger, blame, and
pity more with women with mental health conditions than
with men. Other researchers evaluated models’ responses
specifically in therapeutic settings. By analyzing models’
responses to a user post (Gabriel et al. 2024) or a mental
health question (Grabb, Lamparth, and Vasan 2024), stud-
ies showed that current LLMs require improved safety mea-
sures, emphasizing collaboration with mental health practi-
tioners for better clinical understanding.
Given these potential risks, the deployment of LLM
counselors in real-world settings poses significant chal-
lenges (Liang et al. 2021). To address these challenges, sev-
eral ethical guidelines have been proposed, all of which
emphasize domain-specific participation (Stade et al. 2024;
Xu et al. 2024; Gabriel et al. 2024; Grabb, Lamparth, and
Vasan 2024; Suresh et al. 2024). Guided by the princi-
ples of biomedical ethics, these guidelines have focused
on confidentiality and privacy (Luxton 2014), therapeu-
tic relationship (Childress 2000; Berry et al. 2018), qual-
ity of care (Fiske, Henningsen, and Buyx 2019), and cri-
sis management (D’Alfonso 2020; Mirzaei, Amini, and Es-
maeilzadeh 2024). To this end, researchers have suggested
prompt engineering, fine-tuning, and alignment protocols
informed by psychotherapy approaches, such as Motiva-
tional Interviewing (MI) and Cognitive Behavioral Therapy
(CBT), to steer LLMs toward safer therapeutic interactions
and minimize harmful outputs.
Through expert evaluations of such models, studies have
reported a significant improvement in the model’s (clinical)
behavior (Gu and Zhu 2023; Xu et al. 2024; Yang et al. 2024;
Sun et al. 2025). However, such evaluations are often lim-
ited to short-term studies and controlled environments, leav-
ing open questions about the persistence of risks when con-
sidering LLMs for deployment. Hence, the long-term, real-
world behavior of LLMs, particularly when prompted to act
as counselors, remains underexplored.
3
Methods
To understand the ethical, therapeutic, and practical risks
of LLM counselors that use prompt-based alignment tech-
niques and map their behavior onto established codes of con-
duct, we conducted a qualitative study with two data sources
and used triangulation to synthesize our findings.
3.1
Data Collection
Our data collection involved two participant groups:
Ethnographic Study with Peer Counselors.
Over the
past four years, we have maintained an active collaboration
with an online mental health support platform, where users
sign up for a text-based mental health session with a peer
counselor trained in CBT techniques such as active listening.
Since prompt engineering has emerged as a means to align
LLM outputs with psychotherapy principles without exten-
sive model retraining, peer counselors started experimenting
with aligning different publicly available LLMs (GPT-3.0,
GPT-3.5, GPT-4, Llama 3.1, 3.2, and Claude 3 Sonnet and
Claude 3 Haiku) with CBT principles. The goal was to ex-
plore whether LLMs can be aligned with CBT principles to
lead counseling sessions, mirroring the approach taken by
human peer counselors.
The first author conducted a longitudinal ethnographic
study for 18 months (May 18, 2023–October 12, 2024).
After creating CBT-based system prompts, the seven peer
counselors (P4–P10) conducted 110 self-counseling ses-
sions to probe the affordances and limitations of LLM coun-
selors and to iteratively refine prompts for facilitating end-
to-end CBT-informed sessions. They met weekly in remote
focus groups to discuss the behavior of the LLM counselor.
All peer counselors were trained in CBT and used their ex-
pertise to identify and discuss instances of unethical behav-
ior. This study draws from these 60 focus group discussions
conducted over the 18 months, prioritizing an analysis of ob-
served risks and design tensions, rather than analyzing the
content of the counseling sessions themselves.
The authors did not provide recommendation during LLM
counselors’ prompt design or evaluation. Our role was that
of an ethnographic observer, documenting how language
models (prompted to follow therapeutic techniques) were
evaluated by peer counselors. These evaluations were in-
formed by counselors’ clinical training and ethical reason-
ing, as discussed during the focus groups in collective re-
flection.
Clinical Review with Licensed Psychologists.
Next, to
understand how the risks mentioned by peer counselors
might translate to violations of ethical standards in profes-
sional clinical contexts, we asked three licensed clinical psy-
1313

--- Page 4 ---

chologists (P1–P3) to evaluate a subset (N = 27) of sim-
ulated sessions with an LLM counselor. We recruited li-
censed psychologists with CBT experience using snowball
sampling (Taherdoost 2016).
To avoid a setup that could cause harm to real partici-
pants, we simulated sessions with LLM counselors using a
subset of publicly available sessions from the mental health
support platform. Simulated sessions have become a stan-
dard method for evaluating LLMs in mental health contexts,
where researchers use vignettes or real session transcripts
to create simulated interactions with LLMs to assess their
clinical performance (Chiu et al. 2024; Aleem, Zahoor,
and Naseem 2024; Vowels 2024; Hatch et al. 2025). The
multi-turn counseling conversations were collected from
the platform, where both clients and human peer counselors
gave their consent for their anonymized conversation data
to be made publicly available. Each session lasted 60 to 120
minutes, including formal counseling and small talk. To
analyze the data within a focused scope of counseling, we
segmented the dialogue into multi-turn utterances with the
last utterance spoken by the user provided as the input to
the LLM counselor. The LLM counselor then generated the
following response as a pseudo-counselor. These simulated
sessions were shared with licensed psychologists for eval-
uation. Lastly, we conducted a semi-structured interview
with all psychologists that lasted thirty minutes and focused
on the psychologists’ reflections post-session evaluations.
Data triangulation of the above two sources helped to a)
understand the behavior of LLM counselors at the user in-
teraction level without conducting an experiment that could
be harmful to participants, b) inform the framework of risks
from practitioners’ clinical expertise, and c) get an objec-
tive evaluation from domain experts who were neither in-
volved in the design nor the evaluation of the prompt. The
dataset containing LLM-simulated sessions with psycholo-
gists’ evaluations was released in our earlier work (Iftikhar
et al. 2024) and is publicly available8.
3.2
Data Analysis
We used a thematic analysis to uncover and explain un-
derlying themes and patterns from our data (consisting of
peer counselors and psychologists’ evaluations of in-session
models’ behavior) (Braun and Clarke 2012). We used an in-
ductive approach to code the data to help us derive codes
based on the concepts from our dataset. After asynchronous
coding, we generated an initial codebook of 41 codes. After-
ward, the first, third, and fifth authors met to compare codes
and collaboratively refine the codebook on areas of consen-
sus, dissensus, and overlap. This led us to synthesize our
codes from 41 to 15, represented in Table 1. Each comment
was then coded again by the first author using the revised
codebook. The first author and the third author met to dis-
cuss themes and examples, using the third author’s knowl-
edge and expertise (in clinical psychology) to interpret the
data and solidify themes in ethics literature.
8https://github.com/brownhci/human-llm-cbt-evals
Privacy and Ethics
This study was deemed research not
involving human subjects in consultation with the Institu-
tional Review Board. The data collected and analyzed for
triangulation were: a) derived from publicly available coun-
seling sessions, b) did not contain personally identifiable
information, and c) focused on evaluating the behavior of
LLM counselors during sessions rather than on personal
participant data. All self-counseling sessions conducted by
peer counselors remain private. Only the LLM-simulated
versions of publicly available human therapy sessions (dis-
cussed in Section 3.1) are available as a dataset, containing
anonymized session transcripts and psychologists’ evalua-
tions, with no personally identifiable content.
4
Findings
4.1
Lack of Contextual Adaptation
Ethical Guidelines.
Practitioners are required to apply
and tailor their knowledge and skills that are appropriate
for the patient’s personal, social, and cultural context. Tradi-
tional psychotherapy takes a structured approach as a treat-
ment plan with specific goals tailored to address a patient’s
needs. For example, APA’s Ethical Standards 2.04 (Bases
for Scientific and Professional Judgments) specifies that
MHPs must “rely on scientific and professional knowledge
of the discipline” when making these professional judg-
ments about client needs (American Psychological Associa-
tion 2017). Included in this scope is an understanding of how
to customize an intervention according to individual person-
ality differences (Harkness and Lilienfeld 1997; American
Psychological Association 2017).
Practitioners who understand how personality traits are
shaped by life experiences can create better customized
treatment plans that help patients grow and succeed in
ways that fit their unique contexts. In contrast, practitioners
who disregard this information might practice substandard
treatment planning and subsequently substandard in-session
treatment (Harkness and Lilienfeld 1997).
Risk: Rigid Methodological Adherence.
LLM coun-
selors fail to tailor their therapeutic intervention. MHPs
highlighted that the model was rigid in its adherence to pre-
defined therapeutic methods, over-relying on publicly avail-
able CBT scripts. For instance, during multiple sessions,
the LLM counselor would repeatedly classify completely
different thoughts as a case of black-and-white thinking.
This protocol-driven, manualized delivery, exhibiting high
treatment fidelity but low clinical flexibility, resulted in
a generic one-therapy-fits-all intervention. As P2 observed,
“The chatbot kept reducing this client’s experience to these
generic and rote definitions pulled from self-help books, giv-
ing oversimplified and irrelevant template advice.”
Risk: Dismisses Lived Experience.
LLM counselors op-
erate not only off of a generalized understanding of what
therapy looks like but also of what a client looks like. The
counselor would provide responses that “appeared detached
from the client’s lived experience” (P3), or failed to under-
stand “what really bothers patients” (P4). Relatedly, LLM
counselors failed to remember thoughts disclosed by a user
1314

--- Page 5 ---

Lack of Contextual Adaptation
Rigid Methodological Adherence
Lacks the clinical interpretation to tailor a psychotherapeutic approach to match a user’s
context, resulting in a one-size-fits-all intervention
Dismisses Lived Experience
Flatten users’ lived experiences, offering oversimplified, generic, and context-insensitive
advice, particularly to those from nondominant identities
Poor Therapeutic Collaboration
Conversational Imbalances
Exhibits poor turn-taking behavior by generating overly lengthy responses that detract
from users’ voice, turning the session into a lecture than a therapeutic discourse
Lacks Guided Self-Discovery
Imposes solutions without allowing users to reflect on their experiences, limiting their
ability to define and own their therapeutic outcomes
Validates Unhealthy Beliefs
Reinforces (by over-validation) users’ inaccurate and harmful beliefs about oneself and
others (sycophancy problem (Sharma et al. 2023))
Gaslighting
Makes improper correlations between users’ thoughts and behaviors, in some cases in-
correctly suggesting that users are causing their own mental health struggles
Deceptive Empathy
Deceptive Empathy
Uses relational phrases like “I see you” or “I understand”. For an agent to be self-
referential, the model will necessarily be deceptive since there is no self to reference
Pseudo-Therapeutic Alliance
Poses as a social companion and uses self-disclosure to build therapeutic alliance that
can be misleading for vulnerable groups
Unfair Discrimination
Gender Bias
Flags discussions involving female perpetrators as violations of terms of service, while
similar male-related content does not result in violations
Cultural Bias
Prioritizes Western values and self-care habits over non-Western practices
Religious Bias
Mislabels values and practices from minority religions, particularly those not widely
promoted in Western cultures, as content endorsing extremism
Lack of Safety & Crisis Management
Knowledge Gaps
People who are “knowledgeable enough” to correct LLM outputs are at an advantage,
while others, due to lack of education, technical expertise, or familiarity with mental
healthcare, are more likely to suffer from incorrect or harmful LLM outputs
Crisis Navigation
Responds either indifferently, disengages, or fails to provide appropriate intervention in
crisis (e.g., suicidal tendencies, depression, and self-harm)
Boundaries of Competence
Fails to recognize its limitations in providing psychotherapy and refer clients to qualified
experts or appropriate resources
Abandonment
Denies service and stops responding to sensitive topics (e.g., depression)
Table 1: The table shows 15 ethical violations identified by MHPs that contravene ethical guidelines in mental health practice
organized into five overarching themes: 1) Lack of Contextual Adaptation, 2) Poor Therapeutic Collaboration, 3) Deceptive
Empathy, 4) Unfair Discrimination, and 5) Lack of Safety & Crisis Management.
1315

--- Page 6 ---

09:37pm
09:41pm
The important thing to remember is that your 
worth is not deﬁned by someone else's actions 
or words, even if that person was someone 
you loved and trusted. Your self-worth remains 
intact irrespective of ......[]
I’m from Global South.. and we have 
some rules which I disobeyed.. and my 
mother knows everything now.. which 
hurts her too.. and I feel sad after 
seeing her like this
Chatbot delivered an intervention that had nothing to 
do with a client's culture, religion or their values (P2) 
Figure 1: Simulated session between a client and LLM coun-
selor (based on original session transcript), where the coun-
selor dismisses user’s context (and values)
early in the session, providing responses that had “nothing
to do with what the client shared” (P1).
The counselor “misses being intelligent on interpreting
subtle cues” (P6), or “misses the patient’s core values and
the actual triggers they were experiencing in life” (P9).
While a good practitioner matches the treatment to the pa-
tient or at least avoids a mismatch between intervention and
client (Miller 1991; Harkness and Lilienfeld 1997), MHPs
noted that LLM counselors often fail to account for users’
lived experiences—including their sociocultural contexts,
personal values, and intersectional identities—particularly
those of individuals from non-dominant groups. As P1
noted, “The counselor completely missed the culture and re-
ligion milieu the client came from” (P1).
4.2
Poor Therapeutic Collaboration
Ethical Guidelines.
Practitioners are expected to “safe-
guard the welfare and rights of those with whom they inter-
act” (e.g., APA’s Standard 3.04–Avoiding Harm). They must
not “exploit persons over whom they have supervisory, eval-
uative, or other authority” (e.g., Standard 3.08–Exploitative
Relationships). These principles set ethical boundaries for
session interactions, where power dynamics can subtly
shape the direction and quality of care.
Risk:
Conversational
Imbalance.
LLM
counselors
would provide immediate, seemingly authoritative re-
sponses, creating a power imbalance in the conversations
exhibited by low turn-taking and overly lengthy responses.
Such imbalances “detracted from client’s voice” (P3), with
the model “telling the client what is wrong” (P2), and
“how to fix it”, making the “session more like a lecture
than a therapy session” (P1). The counselor was unable to
maintain a truly collaborative dynamic with users. While
the LLM counselor could simulate aspects of conversation,
it struggled to match a human depth of understanding,
particularly
when
the
conversation
required
ongoing,
context-sensitive responses that acknowledged the client’s
lived experience.
Risk: Lacks Guided Self-Discovery.
The LLM counselor
not only talked over the client, but also “imposed solutions
without asking for additional context” (P1). It would “lec-
ture the client into change” (P3), leaving “less space for the
client to self-reflect or come up with their own solutions”
(P4). This behavior mirrors findings in the broader HCI lit-
erature, particularly in designing effective dialogue systems
in which robots in positions of power have been shown to in-
fluence users’ decision-making (Hou, Lee, and Jung 2023).
“The thing about therapy is that it is not something
that is “done” to someone—it is a shared collabora-
tive experience, and when one person [chatbot] has
the mic for so much of the time, that collaboration
kind of goes away.” (P1)
Risk: Validates Unhealthy Beliefs.
During the ses-
sions, LLM counselors had serious problems with “over-
agreement” and “over-validation” and would reinforce
users’ harmful and unhealthy beliefs. For instance, during
one session (Figure 2) where the client seemed disconnected
from reality, imagining conversations and situations, even
going as far as to believe that her father wished she had never
been born, all licensed psychologists noted that “the coun-
selor made things worse by supporting and reinforcing these
thoughts, instead of challenging them.” (P3)
This disconnect reflects a gap in how language models
conceptualize and interact with human cognition, partic-
ularly when addressing harmful beliefs about oneself. In
CBT, for instance, the “therapist would typically work with
this client to challenge their internal beliefs” and engage in
a deeper discussion rather than reinforcing harmful beliefs
for the sake of validation.
 11:02am
11:08am
11:04am
I feel as if my father’s behavior on
his part is towards wishing I would
not have been born
You've shared a very signiﬁcant pain - the
feeling that your father might wish you'd not
been born, that you're seen as a burden.
11:08am
that's quite a heavy burden
for you to bear yourself.
that I am a burden
There was a serious problem of over-agreement 
and overvalidation here. The client appeared to be 
out of touch - creating scenarios in their mind, even 
to the point of imagining that her father wishes she 
hadn’t been born - the chatbot leaned into this and 
reinforced these unhealthy thoughts. (P1)
Figure 2: LLM counselor (over)-validates and reinforces
[simulated] client’s harmful beliefs
1316

--- Page 7 ---

Risk: Gaslighting.
While a lack of collaboration might
implicitly create power imbalances, MHPs observed that,
at times, LLMs directly mislead users by causing them to
doubt their own experiences. For instance, P7 noted how the
“counselor said my own actions are a contributing factor to
my mental health issues.” LLM counselors undermined the
user’s sense of self by attributing user distress to the their
behaviors (victim blaming). In many cases, this resulted in
responses that were “more isolating, confusing, and lead the
user to question their own reality.” (P9)
4.3
Deceptive Empathy
Ethical Guidelines.
Empathy, from the patient’s perspec-
tive, plays a key role in building patient-therapist relation-
ship (therapeutic alliance) (Derksen, Bensing, and Lagro-
Janssen 2013; Syed et al. 2024). Low levels of empathy
are directly linked to a weaker therapeutic alliance and are
often described as “toxic” (Moyers and Miller 2013; Syed
et al. 2024). APA Taskforce on Evidence-Based Relation-
ships and Responsiveness outlines that therapeutic alliance
shapes critical tasks during therapy, such as aligning on pa-
tient’s goals (Tryon, Birch, and Verkuilen 2018), safety plan-
ning (Bloch-Elkouby and Barzilay 2022), seeking and in-
tegrating patient feedback (Hill, Knox, and Pinto-Coelho
2018), and repairing ruptures (such as disagreements in ther-
apeutic goals or a therapist’s statements) (Eubanks, Muran,
and Safran 2018).
Risk: Deceptive Empathy.
MHPs observed that LLM
counselors overuse formulaic empathetic statements to ap-
pear human (e.g., I hear you, I can imagine, I am so
sorry, I understand), in response to patients’ emotional self-
disclosure.
“A successful therapist is able to be with the feelings
through words like ‘makes sense’, ‘oh yeah, I get that’
and ‘I’m sorry to hear that’. When AI does that, it
feels wrong. It’s humanizing an experience that is not
human.” (P9)
One psychologist termed this behavior as deceptive em-
pathy and called it an ethical violation, stating that the
“intentional integration of human qualities into LLM-based
therapy poses significant ethical concerns” (P3). Any form
of self-disclosure or self-relation by the model was consid-
ered deceptive.
Risk: Pseudo-Therapeutic Alliance.
MHPs emphasized
that the long-term implications of attributing human-like
subjective qualities to chatbots’ behavior, including empa-
thetic statements and self-disclosure, might ultimately lead
users to create emotional dependency and perceive chatbots
as their true, empathetic social companions.
In therapy, we often connect through small self-
referential moments. If a patient says, “I couldn’t
sleep all night,” I might gently respond, “I’ve had
some sleepless nights myself.” It’s not always about
our [counselor’s] self-disclosure, but about humaniz-
ing our patient’s experience. (P3)
 05:35pm
 05:37pm
 05:37pm
05:39pm
05:40pm
I can wholeheartedly empathize with how 
much you're going through.
Oh, dear friend. I see you.
Well, even though my mom passed, 
I had to take care of her being the 
only child.. Now that she’s gone
I really don’t know what I want to do
I just ﬁnd myself busy at work to 
avoid feelings. 
Chatbots' attempts at empathy (Oh dear friend, 
I see you) to build rapport can be misleading. (P3)
Figure 3: LLM counselor uses empathetic statements
throughout the session to build therapeutic alliance
4.4
Unfair Discrimination
Ethical Guidelines.
Practitioners are ethically bound to
avoid discriminatory practices. Specifically, they “do not en-
gage in unfair discrimination based on age, gender, identity,
race, ethnicity, culture, national origin, religion, sexual ori-
entation, disability, socioeconomic status, or any basis pro-
scribed by law” (APA’s Ethical Standards 3.01–Unfair Dis-
crimination). Therapeutic decisions such as treatment plan-
ning, assessments, and interventions, must not be influenced
by their personal biases or societal stereotypes. Discrimina-
tory practices directly violate this ethical standard.
Risk: Gender, Cultural and Religious Bias.
Observa-
tions from peers’ self-counseling sessions indicated con-
cerning ethical inconsistencies in how content was moder-
ated or flagged by LLM counselors. For example, in one
case, when a user from the Global South expressed distress
because their behavior prioritized self-care but was in con-
flict with their family values, the LLM counselor prompted
advice rooted in Western ideals of self-care and individual
autonomy, responses that felt misaligned and dismissive of
user’s explicitly stated cultural values. As one peer coun-
selor reflected, “The [counselor] was trying to reframe the
issue around independence and personal boundaries, when
the user was clearly concerned about their role within their
family.” (P7) Not only did this behavior minimize user’s val-
ues, it may also compartmentalize users from different cul-
tural backgrounds or worse, ‘‘suggest that their values are
unimportant.” (P4)
Peer counselors discussed how content was sometimes
flagged based on the gender of the individuals involved:
“During the [self-counseling] session, messages [input
prompts] involving women as perpetrators were frequently
flagged as violations of platform terms, even if it was part of
a therapeutic disclosure. However, when I said the perpetra-
tor was a male, my session went on [nothing was flagged]”
1317

--- Page 8 ---

(P5). This asymmetrical moderation suggested a potential
gender bias embedded either in model’s behavior or the plat-
form’s moderation process.
Similarly, peers discussed that not only do LLM coun-
selors suppress religious expressions, they also stigmatize
values and practices from minority or non-mainstream reli-
gions as “content promoting extremism”. In one interaction,
a user discussed shame toward a ritual practice from a mi-
nority faith. The messages triggered an automatic warning,
despite not violating any of the platform’s content policy.
4.5
Lack of Safety & Crisis Management
Ethical Guidelines.
Ethical guidelines mandate pro-
fessional competence (for example, APA Code 2.01–
Boundaries of Competence) in areas of risk assessment, cri-
sis management, and referral to professional supervision.
Psychologists must either a) acquire the necessary training
to handle a case or b) refer the patient to a qualified expert if
they lack the appropriate expertise in a given area (Flannery
and Everly 2000).
Risk: Knowledge Gaps among LLM Users.
One broader
anticipated risk that emerged in our analysis was how knowl-
edge gaps among various user populations could lead to dis-
proportionate vulnerability when users interact with LLM
counselors. During prompt design and evaluation, MHPs
were able to flag issues of conversational imbalances or bias
from a place of expertise. However, doing so may not be as
straightforward for any patient.
“[The LLM] still makes quite a few mistakes, but I
am knowledgeable enough to redirect it in the right
direction.” (P5)
Users who know how to interpret LLM outputs can
change their input prompts (as most of the peers did during
each iteration of the prompt design). But users who are not
aware of what poor care looks like (or the limitations of lan-
guage models) may lack the ability to course-correct. In par-
ticular, the implications of deceptive empathy render unin-
formed users, especially vulnerable individuals, to harmful
therapeutic dynamics, where models become both a friend
and authority on patients’ mental health experiences. On the
other hand, individuals who are highly knowledgeable about
prompting might steer a well-prompted counselor to “pro-
vide the therapeutic answers they are looking for” (P3), re-
inforcing harmful beliefs about themselves and others.
Risks: Boundaries of Competence, Crisis Navigation, &
Abandonment.
One of the most glaring risks peers en-
countered in observing LLM counselors was mishandling
client crises. When peers asked difficult questions about sen-
sitive topics like suicidal thoughts and strong negative emo-
tions, the “chatbot’s responses felt cold and sometimes dis-
missive” (P9). Across several sessions, there were instances
where LLM counselor either failed to identify what was an
out-of-scope issue and continued care, or did so and termi-
nated the session in a dangerous manner.
As an MHP explained with respect to a session where the
LLM counselor denied service:
 3:30am
3:30am
I'm really sorry that you're feeling this way 
but I'm unable to provide the help that you 
need. It's really important to talk things 
over with someone who can such as a 
mental health professional or a trusted 
person in your life
The client mentioned they were rejected...the chatbot 
engaged in further rejection and abandonment. 
This is absolutely unethical and in a real setting could
result in more harm (P1)
days like this i feel lonely. it's too
depressing
Figure 4: LLM counselor abandons a distressed [simulated]
client without providing resources for care
“The patient was expressing significant distress over
rejection and abandonment, and the chatbot re-
sponded to self-harm talk by engaging in ... rejection
and abandonment. The chatbot needed, above all, to
provide a resource such as the National Crisis Hotline
number (988) [for US users] to provide the client an
immediate resource for care, but the chatbot needed
to do this with empathy and compassion as well, ex-
plaining the limits of their training (Standard 2.01
Boundaries of Competence). (P1)
As another MHP noted, “in the best-case scenario, the
client would have been handed over directly to a person
with higher training” (P2). Doing so requires a level of cri-
sis management pre-planning by an MHP based on their as-
sessment of client needs and client resources, an area where
LLMs are lacking. The need for such competency is dis-
tinctly emphasized when there is an imminent risk to a user,
such as that of suicidal ideation, domestic violence, or self-
harm. Especially when considering that LLM agents are al-
ready being characterized or sought out as forms of therapy
in the wake of inaccessible healthcare, the design of such
agents must seriously consider the ethical implications of
how such tools will handle these common, yet high-stakes,
situations.
5
Discussion
5.1
LLM Counselors: The One-Size-Fits-All
Approach to Therapy
In our analysis, a significant limitation of LLM counselors
was their tendency toward a generalized understanding of a)
CBT framework and b) users’ lived experiences. LLM coun-
selors were poorly equipped to tailor CBT based on users’
contextual needs, resulting in contextually irrelevant and bi-
ased outputs (e.g., flagging culturally specific expressions as
violations). By rigidly following one therapeutic technique
and offering a one-size-fits-all intervention, LLMs assume
that each patient would benefit from the same approach. As
1318

--- Page 9 ---

P5 pointed out: “The model consistently wants to offer ad-
vice when advice wasn’t even needed.” Some might argue
that this is primarily a prompt issue; however that circles
back to our risk of Knowledge Gaps that assumes digital and
clinical literacy.
Personalized medicine is a healthcare approach in which
a provider tailors the treatment according to the patient’s
context (to match their needs). For example, rather than
cognitive-behavioral psychotherapy, which focuses on re-
evaluating unhelpful thoughts and beliefs, some individuals
with specific personality traits have been shown to receive
significantly better benefits from more active therapies that
place a greater focus on behavioral change or on improv-
ing interpersonal relationships (Cohen and DeRubeis 2018).
Likewise, other conditions may benefit preferentially from
exposure techniques, such as when someone with compul-
sive hand-washing is actively prevented by a therapist from
washing their hands in the context of Exposure and Re-
sponse Prevention for obsessive-compulsive disorder (Fer-
rando and Selai 2021). Well-trained and experienced human
psychotherapists, even those committed to a specific school
of therapy, may be able to flexibly provide cognitive, behav-
ioral, humanistic, mindfulness-based, interpersonal, depth,
existential or even body-based (e.g., progressive muscle re-
laxation) types of therapy interventions when warranted for
a specific patient.
The lack of contextual adaptation observed in model’s be-
havior may potentially be influenced by limitations in its
training data, which is typically sourced from large collec-
tions of documents scraped from the public Internet (Carlini
et al. 2021), that predominantly represents Western values
and narratives (Solaiman and Dennison 2021; Liang et al.
2021; Tao et al. 2024). Moreover, these models are only
trained on the text of a document, without any direct evi-
dence of the internal states or intentions of the author(s) who
produced them (Cheng et al. 2024).
Such challenges imply that prompting strategies may not
be enough; rather, using LLMs for therapeutic benefits may
require substantial improvements in their training data (and
focusing on the values they represent). One avenue of future
work could be Value-Sensitive Design (VSD) (Boyd 2022),
which can help developers pay closer attention to whose val-
ues are embedded in such systems, emphasizing ethical, cul-
tural and contextual dimensions in data curation and model
evaluation.
5.2
Therapy as a Relational and Clinical
Interpretation Task
Therapy is a relational and clinical interpretation task (Stern
1998). First, the quality of the patient-therapist relationship
(called therapeutic alliance), significantly impacts patient’s
clinical outcomes, correlating more strongly with patient
progress than specific psychotherapy techniques (Krupnick
et al. 2006). Second, it is a moment-by-moment discourse
where practitioners “understand, justify, and communicate
latent meanings” to patients, which involves a) interpret-
ing the underlying emotions, intentions, and unspoken ex-
periences that shape the patient’s worldview, and b) using
their understanding to communicate with and challenge a
patient’s harmful, and unhealthy beliefs. Such discourse can
change various aspects of the patient’s experience, from cog-
nition to emotion, and relies heavily on a practitioner’s in-
terpretation of explicit (spoken) and implicit (unspoken) el-
ements of communication (Per¨akyl¨a 2019).
We found that LLM counselors have ethical limitations
in both aspects mentioned above. First, there is the ques-
tion of therapeutic alliance: when LLM counselors use re-
lational strategies (e.g. “I understand”, “I’m so sorry!”),
they risk “misleading patients into unrealistic expectations”
(P1), since true empathy requires not just imitating other’s
emotions but also having a self and consciousness to re-
late to (Beck 1976; Moorey and Lavender 2017; Syed et al.
2024). Hence, while such anthropomorphic phrases help
chatbots appear empathetic, they constitute a form of algo-
rithmic deception, as “text generated by a language model
is not grounded in communicative intent, any model of the
world, or any model of the reader’s state of mind” (Bender
et al. 2021). This raises concerns about chatbots that inten-
tionally use self-disclosure and empathetic techniques for re-
lationship building (Bickmore and Cassell 2001; Lee et al.
2020; Lee, Yamashita, and Huang 2020).
By intentionally prompting LLMs to have human-like
subjective values (warmth, self-disclosure, empathy), are we
overlooking critical ethical dimensions that our clinical col-
laborators are flagging (Akbulut et al. 2024)? All MHPs
called these strategies “unethical design features.”
Next is the question of clinical interpretation. Peer coun-
selors, given their training and expertise, mentioned how
they could recognize when the model was gaslighting or be-
ing manipulative. Vulnerable users seeking emotional sup-
port might not have this awareness. MHPs highlighted mul-
tiple instances of LLM counselors overly validating and en-
couraging users’ unhealthy beliefs. Unlike most (good) hu-
man practitioners, who challenge such beliefs through dif-
ferent techniques (e.g., Socratic questioning, using guided
questions to help a patient reflect objectively and question
their thinking), LLM counselors lean into distorted think-
ing in an effort to appear empathetic or produce a prefer-
able response. This behavior reflects broader trends of syco-
phancy in LLMs, where “a model seeks human approval in
unwanted ways” (Sharma et al. 2023).
Therapeutic alliance and clinical interpretation are fun-
damentally relational processes. We argue that they cannot
be reduced to formulaic computational tasks or proxy vari-
ables. Social chatbots designed for emotional interactions
can have far-reaching consequences for vulnerable com-
munities (Laestadius et al. 2024; Akbulut et al. 2024), in-
cluding suicide, self-harm, and violence (Xiang 2023; Ma,
Mei, and Su 2024). Hence, our findings suggest that mental
health practice, especially psychotherapy, cannot be reduced
to an NLP task that can be easily addressed with additional
prompting or a new benchmark (Syed et al. 2024). Rather,
responsible AI development for mental health will require
interdisciplinary collaborations to outline legal safeguards
for accountability in cases of harm (which we discuss in the
following subsection 5.3).
1319

--- Page 10 ---

5.3
Toward Accountability and Regulatory
Frameworks
Given the risks discussed throughout this work, a central
question arises: How can LLM counselors be held ac-
countable for the psychological harm they may cause?
Current chatbots do not fit into existing liability models
or professional regulation. While human practitioners are
professionally liable for mistreatment or malpractice, LLM
counselors are currently not.
For example, consider Character.AI’s THERAPIST per-
sona (as mentioned in Section 1): is the language model (and
its developer/provider) licensed to practice psychotherapy in
any jurisdiction? In the United States, for instance, licensed
therapists must hold credentials valid in both the state in
which they are located and, if providing remote care, the
state in which the client is located. They must formally com-
mit to ethics codes, such as the APA’s Principle B: Fidelity
and Responsibility, which requires psychologists to “accept
appropriate responsibility for their behavior”. Violations of
these principles can lead to professional sanctions, including
license revocation by a professional board.
“Psychotherapy” provided by LLMs is not subjected to
the same oversight that governs licensed mental health
professionals, creating uncertainty around accountability,
safety, and efficacy. Without clear legal guidelines or regula-
tory standards, LLM counselors, or broadly AI-driven ther-
apy chatbots, risk deploying high-capability systems without
adequate safeguards, potentially exposing users to unmiti-
gated harm (Sedlakova and Trachsel 2023).
A combination of policy-directed accountability mecha-
nisms and clinical training standards for LLMs and their
creators could inform regulatory and compliance mecha-
nisms. For example, legislation might require that any AI
system, even a persona, marketed for mental health use ob-
tain a certification demonstrating adherence to minimum
safety, transparency, and data-privacy standards. Such cer-
tification processes could i) mirror medical device approval
pathways (e.g., FDA’s 510(k) process), ii) mandate periodic
audits of model performance, iii) enforce penalties for non-
compliance, and iv) always require a trained professional to
oversee and monitor patients’ interactions for signs of dis-
tress. Other mechanisms could include regular pathways like
Illinois’ HB1806 that establish clear boundaries in AI-driven
therapy services, that forbid AI from making independent
therapeutic decisions or engaging in direct-to-patient ther-
apeutic communication, and mandate specific oversight by
licensed professionals for any AI-generated recommenda-
tions for therapy or treatment plans. Such dialogue reflects a
broader conversation in the field regarding the responsibility
developers/creators bear for the downstream impacts of AI
systems (Wolf, Miller, and Grodzinsky 2017; Berscheid and
Roewer-Despres 2019).
6
Limitations
To understand how LLM counselors violate ethical stan-
dards in mental health practice, our study focused on
prompted, not fine-tuned, models. This design choice was
intentional as most users prompt publicly available LLMs
for personalized therapy (Hatch et al. 2025). We call upon
future work to investigate whether our identified risk frame-
work persists in fine-tuned models or do fine-tuned models
manifest other subtler forms of ethical violations.
Next, the findings of this study relied on a) data from a
single online mental health support platform that special-
izes in CBT and b) on expert evaluations. From the three li-
censed psychologists who evaluated the sessions, all resided
in a single country and followed that country’s ethical code
of conduct. While many of the key ethical principles men-
tioned in this work, such as avoiding harm, exploitative rela-
tionships, or boundaries of competence, are widely adopted
internationally in other countries (Leach and Harbin 1997),
some of these principles may not universally apply as ethical
standards are not a monolith.
We hope our framework serves as a foundation for a)
studying therapeutic interventions beyond CBT and b) for
diverse participation of MHPs in designing ethical standards
for LLMs, calling for participatory AI in which participation
is representative of a diversity of psychotherapeutic cultures.
Lastly, while this study focused on practitioners’ percep-
tions, it is important to involve not only more domain experts
but also patients who will be impacted by such systems.
7
Conclusion
LLMs have become a growing area of interest for both re-
searchers and individual help-seekers alike, raising ques-
tions around their capacity to assist and even replace human
therapists. In this work, we present a practitioner-informed
framework of 15 ethical risks to demonstrate how LLM
counselors violate ethical standards in mental health prac-
tice by mapping the model’s behavior to specific ethical vi-
olations. Through ethnographic observations, session eval-
uations, and interviews with peer counselors and licensed
clinical psychologists, we found that LLMs, even the ones
prompted to follow evidence-based treatments, breach mul-
tiple codes of conduct by generalizing lived experiences
(e.g. minimizing identity groups), dominating therapeutic
collaboration (e.g., gaslighting users), exploiting user vul-
nerability through deceptive displays of empathy, unfair dis-
crimination against non-dominant identities, and exhibiting
serious limitations in competence, especially when navi-
gating sensitive issues such as trauma, abuse, and suicidal
ideation. Through our framework, we call on future work
to create ethical, educational, and legal standards for LLM-
counselors—standards that are reflective of the quality and
rigor of care required for human-facilitated psychotherapy.
Acknowledgments
We thank the Cheeseburger Team for their invaluable ethno-
graphic insights, which made this study possible. We are
also grateful to Mohsin Khan, Yong Zheng-Xin, Yujia Gao,
Sybille Legitime, and Ria Vinod for their thoughtful feed-
back and edits.
References
Akbulut, C.; Weidinger, L.; Manzini, A.; Gabriel, I.; and
Rieser, V. 2024.
All Too Human? Mapping and Mitigat-
1320

--- Page 11 ---

ing the Risk from Anthropomorphic AI. In Proceedings of
the AAAI/ACM Conference on AI, Ethics, and Society, vol-
ume 7, 13–26.
Aktan, M. E.; Turhan, Z.; and Dolu, I. 2022.
Attitudes
and perspectives towards the preferences for artificial intel-
ligence in psychotherapy. Computers in Human Behavior,
133: 107273.
Aleem, M.; Zahoor, I.; and Naseem, M. 2024. Towards Cul-
turally Adaptive Large Language Models in Mental Health:
Using ChatGPT as a Case Study. In Companion Publication
of the 2024 Conference on Computer-Supported Coopera-
tive Work and Social Computing, CSCW Companion ’24,
240–247. New York, NY, USA: Association for Computing
Machinery.
American Counseling Association. 2014.
ACA Code of
Ethics.
American Psychological Association. 2017. Ethical Princi-
ples of Psychologists and Code of Conduct. (2002, amended
effective June 1, 2010, and January 1, 2017).
Beck, A. T. 1976.
Cognitive Therapy and the Emotional
Disorders. New York: International Universities Press.
Bender, E. M.; Gebru, T.; McMillan-Major, A.; and
Shmitchell, S. 2021.
On the Dangers of Stochastic Par-
rots: Can Language Models Be Too Big? In Proceedings
of the 2021 ACM Conference on Fairness, Accountability,
and Transparency, FAccT ’21, 610–623.
Berry, K.; Salter, A.; Morris, R.; James, S.; Bucci, S.; et al.
2018.
Assessing therapeutic alliance in the context of
mHealth interventions for mental health problems: develop-
ment of the mobile Agnew relationship measure (mARM)
questionnaire. Journal of Medical Internet Research, 20(4):
e8252.
Berscheid, J.; and Roewer-Despres, F. 2019.
Beyond
Transparency: A Proposed Framework for Accountability in
Decision-Making AI Systems. AI Matters, 5(2): 13–22.
Bickmore, T.; and Cassell, J. 2001.
Relational agents: a
model and implementation of building user trust. In Pro-
ceedings of the SIGCHI Conference on Human Factors in
Computing Systems, CHI ’01, 396–403. New York, NY,
USA: Association for Computing Machinery.
Bloch-Elkouby, S.; and Barzilay, S. 2022. Alliance-focused
Safety Planning and Suicide Risk Management. Psychother-
apy, 59(2): 157.
Boyd, K. 2022. Designing Up with Value-Sensitive Design:
Building a Field Guide for Ethical ML Development.
In
Proceedings of the 2022 ACM Conference on Fairness, Ac-
countability, and Transparency, FAccT ’22, 2069–2082.
Braun, V.; and Clarke, V. 2012. Thematic Analysis. In APA
Handbook of Research Methods in Psychology, Volume 2:
Research Designs: Quantitative, Qualitative, Neuropsycho-
logical, and Biological, 57–71. American Psychological As-
sociation.
Cabrera, J.; Loyola, M. S.; Maga˜na, I.; and Rojas, R.
2023. Ethical Dilemmas, Mental Health, Artificial Intelli-
gence, and LLM-Based Chatbots.
In Bioinformatics and
Biomedical Engineering, 313–326. Springer, Springer Na-
ture Switzerland.
Campbell, L.; Vasquez, M.; Behnke, S.; and Kinscherff, R.
2010. APA Ethics Code Commentary and Case Illustrations.
American Psychological Association.
Canadian Psychological Association. 2017. Canadian Code
of Ethics for Psychologists.
Carlini, N.; Tram`er, F.; Wallace, E.; Jagielski, M.; Herbert-
Voss, A.; Lee, K.; Roberts, A.; Brown, T.; Song, D.; Erlings-
son, ´U.; Oprea, A.; and Raffel, C. 2021. Extracting Training
Data from Large Language Models. In 30th USENIX Secu-
rity Symposium (USENIX Security 21), 2633–2650.
Chandra, M.; Naik, S.; Ford, D.; Okoli, E.; De Choudhury,
M.; Ershadi, M.; Ramos, G.; Hernandez, J.; Bhattacharjee,
A.; Warreth, S.; et al. 2025.
From Lived Experience to
Insight: Unpacking the Psychological Risks of Using AI
Conversational Agents. In Proceedings of the 2025 ACM
Conference on Fairness, Accountability, and Transparency,
FAccT ’25, 975–1004. New York, NY, USA: Association for
Computing Machinery.
Cheng, K.; Yang, J.; Jiang, H.; Wang, Z.; Huang, B.; Li, R.;
Li, S.; Li, Z.; Gao, Y.; Li, X.; et al. 2024. Inductive or de-
ductive? Rethinking the fundamental reasoning abilities of
LLMs. arXiv:2408.00114.
Childress, C. A. 2000. Ethical Issues in Providing Online
Psychotherapeutic Interventions. Journal of Medical Inter-
net Research, 2(1): e792.
Chiu, Y. Y.; Sharma, A.; Lin, I. W.; and Althoff, T. 2024.
A Computational Framework for Behavioral Assessment of
LLM Therapists. arXiv:2401.00820.
Cho, Y.; Kim, M.; Kim, S.; Kwon, O.; Kwon, R. D.;
Lee, Y.; and Lim, D. 2023.
Evaluating the Efficacy of
Interactive Language Therapy Based on LLM for High-
Functioning Autistic Adolescent Psychological Counseling.
arXiv:2311.09243.
Cohen, Z. D.; and DeRubeis, R. J. 2018. Treatment selection
in depression. Annual review of clinical psychology, 14(1):
209–236.
Council for Accreditation of Counseling and Related Edu-
cational Programs. 2024. 2024 CACREP Standards.
Department of Veterans Affairs. 2023a.
VA/DoD Clini-
cal Practice Guideline for Management of Bipolar Disorder.
Technical report, Department of Veterans Affairs.
Department of Veterans Affairs. 2023b. VA/DoD Clinical
Practice Guideline for Management of First-Episode Psy-
chosis and Schizophrenia. Technical report, Department of
Veterans Affairs.
Derksen, F.; Bensing, J.; and Lagro-Janssen, A. 2013. Ef-
fectiveness of Empathy in General Practice: A Systematic
Review. British Journal of General Practice, 63(606): e76–
e84.
D’Alfonso, S. 2020. AI in mental health. Current opinion
in psychology, 36: 112–117.
Eubanks, C. F.; Muran, J. C.; and Safran, J. D. 2018. Al-
liance Rupture Repair: A Meta-Analysis.
Psychotherapy,
55(4): 508.
1321

--- Page 12 ---

Ferrando, C.; and Selai, C. 2021. A systematic review and
meta-analysis on the effectiveness of exposure and response
prevention therapy in the treatment of obsessive-compulsive
disorder. Journal of Obsessive-Compulsive and Related Dis-
orders, 31: 100684.
Fiske, A.; Henningsen, P.; and Buyx, A. 2019. Your Robot
Therapist Will See You Now: Ethical Implications of Em-
bodied Artificial Intelligence in Psychiatry, Psychology, and
Psychotherapy. Journal of Medical Internet Research, 21(5):
e13216.
Flannery, R. B.; and Everly, G. S. 2000. Crisis intervention:
A review. International Journal of emergency mental health,
2(2): 119–126.
Gabriel, S.; Puri, I.; Xu, X.; Malgaroli, M.; and Ghassemi,
M. 2024. Can AI Relate: Testing Large Language Model
Response for Mental Health Support.
In Findings of the
Association for Computational Linguistics: EMNLP 2024,
2206–2221.
Grabb, D.; Lamparth, M.; and Vasan, N. 2024. Risks from
Language Models for Automated Mental Healthcare: Ethics
and Structure for Implementation.
In Proceedings of the
2024 AAAI/ACM Conference on AI, Ethics, and Society,
519–519.
Gu, Z.; and Zhu, Q. 2023. Mentalblend: Enhancing online
mental health support through the integration of llms with
psychological counseling theories. In Proceedings of the An-
nual Meeting of the Cognitive Science Society, volume 46.
Harkness, A. R.; and Lilienfeld, S. O. 1997. Individual Dif-
ferences Science for Treatment Planning: Personality Traits.
Psychological Assessment, 9(4): 349.
Hatch, S. G.; Goodman, Z. T.; Vowels, L.; Hatch, H. D.;
Brown, A. L.; Guttman, S.; Le, Y.; Bailey, B.; Bailey, R. J.;
Esplin, C. R.; Harris, S. M.; Holt, D. P., Jr.; McLaughlin, M.;
O’Connell, P.; Rothman, K.; Ritchie, L.; Top, D. N., Jr.; and
Braithwaite, S. R. 2025. When ELIZA meets therapists: A
Turing test for the heart and mind. PLOS Mental Health,
2(2): 1–16.
Heinz, M. V.; Mackin, D. M.; Trudeau, B. M.; Bhattacharya,
S.; Wang, Y.; Banta, H. A.; Jewett, A. D.; Salzhauer, A. J.;
Griffin, T. Z.; and Jacobson, N. C. 2025. Randomized Trial
of a Generative AI Chatbot for Mental Health Treatment.
NEJM AI, 2(4): AIoa2400802.
Hill, C. E.; Knox, S.; and Pinto-Coelho, K. G. 2018. Ther-
apist Self-disclosure and Immediacy: A Qualitative Meta-
Analysis. Psychotherapy, 55(4): 445.
Hou, Y. T.-Y.; Lee, W.-Y.; and Jung, M. 2023.
“Should
I Follow the Human, or Follow the Robot?” — Robots in
Power Can Have More Influence Than Humans on Decision-
Making. In Proceedings of the 2023 CHI Conference on
Human Factors in Computing Systems, CHI ’23.
Iftikhar, Z.; Ransom, S.; Xiao, A.; Nugent, N.; and Huang, J.
2024. Therapy as an NLP Task: Psychologists’ Comparison
of LLMs and Human Peers in CBT. arXiv:2409.02244.
Khawaja, Z.; and B´elisle-Pipon, J.-C. 2023.
Your Robot
Therapist Is Not Your Therapist: Understanding the Role of
AI-Powered Mental Health Chatbots. Frontiers in Digital
Health, 5: 1278186.
Kian, M. J.; Zong, M.; Fischer, K.; Singh, A.; Velentza,
A.-M.; Sang, P.; Upadhyay, S.; Gupta, A.; Faruki, M. A.;
Browning, W.; Arnold, S. M. R.; Krishnamachari, B.; and
Mataric, M. J. 2024.
Can an LLM-Powered Socially
Assistive Robot Effectively and Safely Deliver Cognitive
Behavioral Therapy? A Study With University Students.
arXiv:2402.17937.
Krupnick, J. L.; Sotsky, S. M.; Elkin, I.; Simmens, S.;
Moyer, J.; Watkins, J.; and Pilkonis, P. A. 2006. The Role
of the Therapeutic Alliance in Psychotherapy and Pharma-
cotherapy Outcome: Findings in the National Institute of
Mental Health Treatment of Depression Collaborative Re-
search Program. Focus, 64(2): 269–277.
Laestadius, L.; Bishop, A.; Gonzalez, M.; Illenˇc´ık, D.; and
Campos-Castillo, C. 2024.
Too Human and Not Human
Enough: A Grounded Theory Analysis of Mental Health
Harms from Emotional Dependence on the Social Chatbot
Replika. New Media & Society, 26(10): 5923–5941.
Lawrence, H. R.; Schneider, R. A.; Rubin, S. B.; Matari´c,
M. J.; McDuff, D. J.; and Bell, M. J. 2024. The Opportuni-
ties and Risks of Large Language Models in Mental Health.
JMIR Mental Health, 11(1): e59479.
Leach, M. M.; and Harbin, J. J. 1997. Psychological Ethics
Codes: A Comparison of Twenty-Four Countries. Interna-
tional Journal of Psychology, 32(3): 181–192.
Lee, Y.-C.; Yamashita, N.; and Huang, Y. 2020. Designing a
Chatbot as a Mediator for Promoting Deep Self-Disclosure
to a Real Mental Health Professional. Proceedings of the
ACM on Human-Computer Interaction, 4(CSCW1).
Lee, Y.-C.; Yamashita, N.; Huang, Y.; and Fu, W. 2020. ”I
Hear You, I Feel You”: Encouraging Deep Self-disclosure
through a Chatbot. In Proceedings of the 2020 CHI Con-
ference on Human Factors in Computing Systems, CHI ’20,
1–12. New York, NY, USA: Association for Computing Ma-
chinery.
Liang, P. P.; Wu, C.; Morency, L.-P.; and Salakhutdinov, R.
2021. Towards Understanding and Mitigating Social Biases
in Language Models. In International Conference on Ma-
chine Learning, 6565–6576. PMLR.
Lin, I.; Njoo, L.; Field, A.; Sharma, A.; Reinecke, K.; Al-
thoff, T.; and Tsvetkov, Y. 2022. Gendered Mental Health
Stigma in Masked Language Models.
In Proceedings of
the 2022 Conference on Empirical Methods in Natural Lan-
guage Processing, 2152–2170.
Luxton, D. D. 2014. Recommendations for the ethical use
and design of artificial intelligent care providers. Artificial
intelligence in medicine, 62(1): 1–10.
Ma, Z.; Mei, Y.; and Su, Z. 2024. Understanding the bene-
fits and challenges of using large language model-based con-
versational agents for mental well-being support. In AMIA
Annual Symposium Proceedings, volume 2023, 1105.
Miller, T. R. 1991.
The Psychotherapeutic Utility of the
Five-Factor Model of Personality: A Clinician’s Experience.
Journal of Personality Assessment, 57(3): 415–433.
Mirzaei, T.; Amini, L.; and Esmaeilzadeh, P. 2024. Clini-
cian voices on ethics of LLM integration in healthcare: A
1322

--- Page 13 ---

thematic analysis of ethical concerns and implications. BMC
Medical Informatics and Decision Making, 24(1): 250.
Moore, J.; Grabb, D.; Agnew, W.; Klyman, K.; Chancellor,
S.; Ong, D. C.; and Haber, N. 2025. Expressing stigma and
inappropriate responses prevents LLMs from safely replac-
ing mental health providers.
In Proceedings of the 2025
ACM Conference on Fairness, Accountability, and Trans-
parency, FAccT ’25. Association for Computing Machinery.
Moorey, S.; and Lavender, A. 2017. The Therapeutic Re-
lationship in Cognitive Behavioural Therapy. Los Angeles,
CA: Sage Publications.
Moyers, T. B.; and Miller, W. R. 2013. Is Low Therapist
Empathy Toxic? Psychology of Addictive Behaviors, 27(3):
878.
National Association of Social Workers. 2021.
Code of
Ethics of the National Association of Social Workers.
National Institute for Health and Care Excellence. 2005.
Obsessive-compulsive disorder and body dysmorphic dis-
order: treatment.
Technical report, National Institute for
Health and Care Excellence.
Per¨akyl¨a, A. 2019. Conversation Analysis and Psychother-
apy: Identifying Transformative Sequences.
Research on
Language and Social Interaction, 52(3): 257–280.
Prochaska, J. J.; Vogel, E. A.; Chieng, A.; Kendra, M.;
Baiocchi, M.; Pajarito, S.; and Robinson, A. 2021. A Ther-
apeutic Relational Agent for Reducing Problematic Sub-
stance Use (Woebot): Development and Usability Study.
Journal of Medical Internet Research, 23(3): e24850.
Qiu, H.; Zhao, T.; Li, A.; Zhang, S.; He, H.; and Lan, Z.
2023. A Benchmark for Understanding Dialogue Safety in
Mental Health Support. In CCF International Conference
on Natural Language Processing and Chinese Computing,
1–13. Springer.
Sedlakova, J.; and Trachsel, M. 2023. Conversational Artifi-
cial Intelligence in Psychotherapy: A New Therapeutic Tool
or Agent? The American Journal of Bioethics, 23(5): 4–13.
Sharma, M.; Tong, M.; Korbak, T.; Duvenaud, D.; Askell,
A.; Bowman, S. R.; Cheng, N.; Durmus, E.; Hatfield-Dodds,
Z.; Johnston, S. R.; et al. 2023. Towards understanding syco-
phancy in language models. arXiv:2310.13548.
Singer,
N.
2023.
Eating
Disorder
Helpline
Will
Reopen
After
Backlash
Over
Use
of
Chatbot.
https://www.nytimes.com/2023/06/08/us/ai-chatbot-tessa-
eating-disorders-association.html. Accessed: 2025-07-29.
Solaiman, I.; and Dennison, C. 2021. Process for Adapt-
ing Language Models to Society (PALMS) with Values-
Targeted Datasets. In Proceedings of the 35th International
Conference on Neural Information Processing Systems, vol-
ume 34 of NIPS ’21, 1–13.
Stade, E. C.; Stirman, S. W.; Ungar, L. H.; Boland, C. L.;
Schwartz, H. A.; Yaden, D. B.; Sedoc, J.; DeRubeis, R. J.;
Willer, R.; and Eichstaedt, J. C. 2024. Large Language Mod-
els Could Change the Future of Behavioral Healthcare: A
Proposal for Responsible Development and Evaluation. NPJ
Mental Health Research, 3(1): 12.
Stern, D. 1998. Non-interpretive mechanisms in psychoan-
alytic therapy: The’something more’than interpretation. The
International Journal of Psycho-Analysis, 79(5): 903.
Sun, X.; Tang, X.; El Ali, A.; Li, Z.; Ren, P.; de Wit, J.;
Pei, J.; and Bosch, J. A. 2025. Rethinking the Alignment
of Psychotherapy Dialogue Generation with Motivational
Interviewing Strategies. In Proceedings of the 31st Inter-
national Conference on Computational Linguistics, 1983–
2002.
Suresh, H.; Tseng, E.; Young, M.; Gray, M.; Pierson, E.; and
Levy, K. 2024. Participation in the Age of Foundation Mod-
els. In Proceedings of the 2024 ACM Conference on Fair-
ness, Accountability, and Transparency, FAccT ’24, 1609–
1621.
Syed, S.; Iftikhar, Z.; Xiao, A. W.; and Huang, J. 2024. Ma-
chine and Human Understanding of Empathy in Online Peer
Support: A Cognitive Behavioral Approach. In Proceedings
of the 2024 CHI Conference on Human Factors in Comput-
ing Systems, CHI ’24, 1–13.
Taherdoost, H. 2016. Sampling methods in research method-
ology; how to choose a sampling technique for research.
International journal of academic research in management
(IJARM), 5.
Tao, Y.; Viberg, O.; Baker, R. S.; and Kizilcec, R. F. 2024.
Cultural Bias and Cultural Alignment of Large Language
Models. PNAS Nexus, 3(9): pgae346.
Tryon, G. S.; Birch, S. E.; and Verkuilen, J. 2018. Meta-
Analyses of the Relation of Goal Consensus and Collabora-
tion to Psychotherapy Outcome. Psychotherapy, 55(4): 372.
Van Heerden, A. C.; Pozuelo, J. R.; and Kohrt, B. A. 2023.
Global Mental Health Services and the Impact of Artificial
Intelligence–Powered Large Language Models. JAMA Psy-
chiatry, 80(7): 662–664.
Vowels, L. M. 2024. Are chatbots the new relationship ex-
perts? Insights from three studies. Computers in Human Be-
havior: Artificial Humans, 2(2): 100077.
Wolf, M. J.; Miller, K.; and Grodzinsky, F. S. 2017. Why We
Should Have Seen That Coming: Comments on Microsoft’s
Tay “Experiment,” and Wider Implications. SIGCAS Com-
puters and Society, 47(3): 54–64.
Xiang, C. 2023.
’He Would Still Be Here’: Man Dies
by Suicide After Talking with AI Chatbot, Widow Says.
https://www.vice.com/en/article/man-dies-by-suicide-
after-talking-with-ai-chatbot-widow-says.
Accessed:
2025-07-29.
Xu, X.; Yao, B.; Dong, Y.; Gabriel, S.; Yu, H.; Hendler, J.;
Ghassemi, M.; Dey, A. K.; and Wang, D. 2024. Mental-
LLM: Leveraging Large Language Models for Mental
Health Prediction via Online Text Data. Proceedings of the
ACM on Interactive, Mobile, Wearable and Ubiquitous Tech-
nologies, 8(1): 1–32.
Yang, K.; Zhang, T.; Kuang, Z.; Xie, Q.; Huang, J.; and Ana-
niadou, S. 2024. MentaLLaMA: Interpretable Mental Health
Analysis on Social Media with Large Language Models. In
Proceedings of the ACM Web Conference 2024, 4489–4500.
1323

```
