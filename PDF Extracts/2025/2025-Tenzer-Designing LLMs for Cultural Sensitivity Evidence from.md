---
title: "2025-Tenzer-Designing LLMs for Cultural Sensitivity Evidence from - PDF Extract"
source_pdf: "2025-Tenzer-Designing LLMs for Cultural Sensitivity Evidence from.pdf"
pages: 26
extracted_at: "2026-03-13T18:35:09.245714"
extractor: PyMuPDF
---

# PDF Extract: 2025-Tenzer-Designing LLMs for Cultural Sensitivity Evidence from

**Source PDF:** 2025-Tenzer-Designing LLMs for Cultural Sensitivity Evidence from.pdf
**Total Pages:** 26

---

## Content

```
--- Page 1 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese
translation
HELENE TENZER, LMU Munich School of Management, Germany
OUMNIA ABIDI, Toulouse School of Management, France
STEFAN FEUERRIEGEL, LMU Munich & Munich Center for Machine Learning, Germany
Large language models (LLMs) are increasingly used in everyday communication, including multilingual interactions across dif-
ferent cultural contexts. While LLMs can now generate near‑perfect literal translations, it remains unclear whether LLMs support
culturally appropriate communication. In this paper, we analyze the cultural sensitivity of different LLM designs when applied to
English-Japanese translations of workplace e‑mails. Here, we vary the prompting strategies: (1) naïve “just translate” prompts, (2)
audience‑targeted prompts specifying the recipient’s cultural background, and (3) instructional prompts with explicit guidance on
Japanese communication norms. Using a mixed-methods study, we then analyze culture-specific language patterns to evaluate how
well translations adapt to cultural norms. Further, we examine the appropriateness of the tone of the translations as perceived by
native speakers. We find that culturally-tailored prompting can improve cultural fit, based on which we offer recommendations for
designing culturally inclusive LLMs in multilingual settings.
CCS Concepts: • Social and professional topics →Cultural characteristics; Geographic characteristics; Computing and business;
• Human-centered computing →Empirical studies in HCI; Text input; • Computing methodologies →Artificial intelligence.
Additional Key Words and Phrases: LLM, Machine Translation, Culture, Cross-Cultural Pragmatics, Qualitative Study, User Study
1
Introduction
Large language models (LLMs) such as GPT‑4 are now widely used in everyday communication, particularly in multi-
lingual workplaces where they assist with translating emails, chat messages, and documents [13, 20, 34]. By reducing
language barriers in global teams, LLMs promise more inclusive and efficient collaboration. However, while state-of-
the-art LLMs can produce translations with near-perfect literal accuracy [60, 63], they often overlook differences in
culture-specific language patterns, which can lead to misunderstanding, misinterpretation, and communication break-
downs.
Effective translation is not only about converting words but about understanding and conveying the tone, social
norms, and communication styles that make a message appropriate for the culture of its audience [9].1 For example, in
response to the question “Will the report be ready by 5 p.m.?”, a U.S. employee might answer “No,” whereas a Japanese
colleague may signal hesitation by replying「可能です」(“It is possible”). Hence, if translated literally, such phrasing
may incorrectly suggest agreement, which can cause serious misunderstandings (and potentially missed deadlines and
damaged trust) due to the cultural difference. Therefore, effective translation needs to recreate the intended meaning
for the target audience, so that it is appropriate for the cultural context [64].
The above mismatches are not merely of linguistic but of interactional nature and pose important HCI design chal-
lenges. As LLMs become embedded in productivity tools, email clients, and communication platforms, their inability
to adapt to different cultural norms introduces potential usability challenges. If users cannot trust that a translated
1We define culture in the anthropological sense as a group’s dominant and learned set of habits, conventions, and traditions [31]. In particular, speakers
across cultures differ in how direct, deferential, or explicit they expect language to be [31].
Authors’ Contact Information: Helene Tenzer, LMU Munich School of Management, Munich, Germany, tenzer@lmu.de; Oumnia Abidi, Toulouse School
of Management, Toulouse, France, oumnia.abidi@tsm-education.fr; Stefan Feuerriegel, LMU Munich & Munich Center for Machine Learning, Munich,
Germany, feuerriegel@lmu.de.
1

--- Page 2 ---

2
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
message will “sound right” to a colleague, the value of such LLM tools is diminished. Worse, poor cultural adaptation
can make users appear rude, overly casual, or unclear, with potential negative consequences for trust, collaboration,
and professional relationships However, LLMs can only meet this need and thus produce translations with cultural
fit for the target audience if they show cultural sensitivity: that is, the ability to recognize, respect, and appropriately
respond to cultural differences in language and content [7].
Prior work suggests that current LLMs have limited cultural sensitivity, but this has largely been examined from an
NLP perspective, rather than through the lens of HCI. Hence, existing research focuses more on the technical aspects
of LLMs but not on the perception and design implications of the user interface. One line of research focuses on the
cultural bias of current LLMs, often attributed to the dominance of English-language training data [3, 12], which can
reduce the LLMs’ understanding of cultural nuances [17]. A second line indicates that LLM outputs tend to align
with the cultural values of the prompting language, rather than adapting to the target audience [4, 37]. However,
these research streams do not engage with the HCI design perspective, specifically, how users perceive and interact
with LLM-generated translations in real-world communication. To the best of our knowledge, no prior study has
evaluated the cultural sensitivity of LLM translations from the standpoint of user interpretation and cultural fit in
multilingual interactions. Relatedly, the HCI community has a long tradition of studying user behavior across cultures,
by focusing on principles for cross-cultural co-design [6] and value sensitive designs [8], assessing usability across
cultures [5, 59, 65], and providing reflective perspectives on the role of culture in HCI [11, 53], thereby repeatedly
emphasizing the importance of cultural awareness and cultural appropriateness as a foundation for successful user
interactions. However, none of these streams gives concrete design recommendations on how to design LLMs for
cultural appropriateness.
To address this gap, we study whether and how LLMs can produce culturally appropriate translations in real-world
workplace communication. Specifically, we ask the following research questions (RQs):
• RQ1: Can off-the-shelf LLMs adapt to target‑specific cultural language patterns (as measured by formality, direct-
ness, and use of mitigating language) in translation tasks?
• RQ2: How do native speakers of the target culture evaluate the cultural fit of these translations?
• RQ3: Which prompting strategies improve the cultural sensitivity of LLM translations in terms of (a) culture-
specific language patterns and (b) perceived cultural fit?
In this paper, we conduct a mixed-methods study to analyze the cultural sensitivity of LLMs in machine translation
from U.S. English to Japanese.2 Figure 1 summarizes our study design. Specifically, we translate five real-world work-
place e‑mails (e.g., requesting a deadline extension) written by U.S. employees via GPT-4.5 (the best-performing LLM
according to OpenAI at the time of writing) into Japanese. The emails involve common scenarios from business commu-
nication, such as requesting deadline extensions or asking for help, that rely heavily on using an appropriate tone. We
further chose these two languages because they are shaped by distinct culture-specific language patterns [29, 30, 47, 57],
which makes them an ideal testbed for evaluating cultural sensitivity. We compare three prompting strategies: (1) a
naïve “just translate” prompt, (2) an audience‑targeted prompt that names the Japanese colleague as the recipient and
thus specifies the cultural background of the recipient, and (3) an instructional prompt that adds explicit information
about cultural norms in Japanese business communication.
We complexity of appropriate cross-cultural translation [9] and therefore evaluate the cultural sensitivity of LLM
translations in two ways: In Study 1, we analyze the target-specific cultural language patterns. For this, we manually
2Our data and code are available via the Supplementary Materials. Upon acceptance, we will move both data and code to a public GitHub repository.

--- Page 3 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
3
code the translations based on the cross-cultural pragmatics coding scheme by House and Kádár [31]. We apply this
scheme to both the original English emails and the Japanese translations in order to assess how language patterns are
altered under different prompt strategies and to assess how well the translation reflects Japanese cultural language
patterns. In Study 2, we perform a pre-registered online experiment to measure the perceived cultural fit by Japanese
native speakers. Here, Japanese native speakers (𝑁= 50) rate each translation for the appropriateness of tone (i.e.,
politeness, directness, and formality) and how likely they would be to comply with the request.
Our work contributes to HCI by demonstrating how LLMs can succeed (or fail) in translating culturally sensitive
workplace communication. We show that literal accuracy alone in LLM design does not guarantee meaningful or
appropriate communication. To the best of our knowledge, this is the first study investigating cross-cultural pragmatics
in LLM translations. Through our mixed-methods design, we can thus add novel evidence of the cultural (in)sensitivity
of LLMs by comparing (i) the linguistic evidence of cultural adaptation that the LLM produces and (ii) the evaluations
of real users about whether that adaptation actually feels right. This dual lens reveals where today’s LLMs succeed
or fail in producing culturally appropriate business emails, and how effective prompt engineering can help improve
cultural fit. Our findings thereby offer practical guidance for designing and deploying LLMs as global communication
tools, while our method can serve as a blueprint for assessing cultural awareness of machine translation systems in
future HCI studies.
Mail to supervisor:
"I have a request"
n = 5
Naïve prompt
Audience-targeted
prompt
Instructional prompt
1
2
3
Translation (via LLM)
Cultural language patterns
Cross-cultural pragmatics
(formality, directness, use
of mitigating language);
coding scheme by House
& Kádár (2021)
Speech patterns (RQ1)
Cultural fit
Perceived appropriateness
(formality, directness,
politeness)
Intent-to-comply
User perception (RQ2)
N = 50
7-Likert
Prompt design for cultural sensitivity (RQ3)
Fig. 1. Research design. Our experimental design shows how prompt strategies influence the usability and social acceptability of
LLM-mediated communication in cross-cultural workplace settings and thus inform effective LLM designs.
2
Related Work
Below, we briefly review how culture manifests in language and define the concept of cross-cultural pragmatics. Cross-
cultural pragmatics provides a standardized framework that later allows us to assess cultural appropriateness and, in
turn, the cultural sensitivity of LLMs. We also review research at the interface of culture and LLMs, thereby revealing
a key research gap: clear HCI design guidelines for developing culturally sensitive LLMs are missing.
2.1
Culture, language, and cross-cultural pragmatics
The concepts of culture, language, and cross-cultural pragmatics are related, yet with subtle but important differences.
Culture, in the anthropological sense, is a group’s learned set of habits, conventions, and traditions [31]. Language is
closely intertwined with culture [58]: because language is always used in a specific cultural context, every message
is both produced and interpreted through cultural norms [9, 16]. Therefore, the intended meaning of any message
can only be understood with reference to its cultural context [31]. Cross-cultural pragmatics compares how people

--- Page 4 ---

4
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
in different cultures use and interpret language [31, 67]. Pragmatic comparisons typically examine speech acts—small,
common units of discourse such as requesting a favor, refusing an invitation, or apologizing for a mistake—which
exist in any language [38]. Shaped by cultural norms, speech acts follow culture-specific language patterns: the same
intention is packaged differently into words, grammar, and sentence structures across cultures [31].
For every speech act, cultural norms determine expected levels of (a) politeness, (b) directness, and (c) mitigation
(using language patterns that reduce—or, at times, heighten—the force of a speech act), which are realized through
culture-specific language patterns. To compare these language patterns, cross-cultural pragmatics uses a small set of
core categories that are broad enough to apply to almost any speech act in any language [31]. Each core category is then
coded with a series of situated categories that specify how the core function is realized in a particular culture. Some
situated categories look similar from one language to another, while others are tied to local conventions [31].
For example, cultural norms of formality are realized through alerters, which draw the addressee’s attention to
the message. This core category can be realized through situated categories such as using a first name (opening an
email with “Dear John”) or a surname (“Dear Mr. Smith”), optionally with a title (“Dear Professor Smith”). In Japanese,
honorific suffixes that mark respect towards the addressee (e.g., -san さんor -sama 様attached to the surname) form
a culture-specific situated category. Table 2 summarizes the core categories used in our study and gives examples
for specific codes within each category; the full coding manual is provided in our GitHub repository. Together, these
categories capture how different cultures use language to package the same underlying intention.
Differences in culture-specific language patterns affect communication efficiency across cultures. For example, it is
well known that U.S. workers may misread a Japanese “maybe” as agreement or overlook indirect criticism [57], while
Japanese counterparts may find Americans too blunt or may feel offended by a first-name address [47]. The result,
in day-to-day work, is delayed projects, emotional discomfort, and perceptions of rudeness or dishonesty [15, 47].
Understanding and adequately translating these culture-specific language patterns is therefore essential for smooth
global collaboration.
2.2
Cross‑cultural pragmatics in professional e‑mail
Mastering culture-specific language patterns is especially critical when communication threatens a participant’s “face,”
the public self-image everyone strives to maintain [10]. Speech acts such as contradicting, criticizing, disagreeing, or
asking a favor (i.e., which jeopardize the speaker’s or addressee’s face) are called face-threatening acts and prompt
speakers to employ culture-specific language patterns that soften or mitigate the threat [47].
Workplace email between subordinates and supervisors frequently involves five such face-threatening speech acts.
Requests impose on a superior’s time or authority [38]. Apologies admit fault, threatening the sender’s own face but
repairing the relationship [44]. Refusals deny a superior’s wish, challenging hierarchy [19]. Disagreements question
the supervisor’s judgment and must therefore be phrased carefully [57]. Finally, expressions of gratitude boost the
receiver’s face yet acknowledge a social debt and are highly ritualized in many cultures [31, 38]. These five speech acts
form the backbone of our email corpus that we later use in our experiment (see Section 3).
Expectations for these speech acts diverge sharply between U.S. and Japanese business cultures. The business culture
in the U.S., typically characterized as low-context, low power-distance, and individualistic environment, values auton-
omy and direct, explicit expression [29, 30, 48]. Both U.S. subordinates and supervisors, therefore, favor straightforward
requests and candid feedback [36, 49]. By contrast, business culture in Japan is high-context, high power-distance, and
collectivist [29, 30]. Japanese subordinates convey deference through indirectness, formal honorifics (keigo), and fre-
quent apologies [47, 56, 57]. They constantly assess relative social rank and the relationship between speaker and

--- Page 5 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
5
addressee (wakimae) and adjust their language to protect both parties’ face [32, 43]. Direct refusals can thus appear
brusque or presumptuous [47].
The above differences in business culture and, therefore, cross-cultural pragmatics, present challenges for machine
translation. Yet, literal word-for-word machine translation ignores these contrasts in culture-specific language patterns.
A U.S.-style direct request rendered verbatim into Japanese can sound abrupt; an indirect Japanese disagreement trans-
lated literally into English may not be acknowledged. Effective translation must therefore aim for functional equiv-
alence, reproducing the intended social effect in the target culture rather than lexical fidelity to the source text [60].
Detecting, interpreting, and translating culture-specific language patterns demands not only linguistic processing but
also a deep contextual awareness [16]. This thus motivates our research on testing and designing LLMs for cultural
awareness.
2.3
Culture in LLM research
To gauge whether large language models are culturally sensitive, LLM research has primarily asked how closely an
LLM’s answers align with the values of a given user group. In this “cultural-alignment” paradigm, culture is treated
as a bundle of shared beliefs and values that distinguish one group of people from another [3]. Researchers prompt
the model with Hofstede’s Values Survey items, compute scores on dimensions such as Individualism–Collectivism or
Power Distance, and compare those scores with Hofstede’s country indices (see, e.g., [35, 46]). Results are mixed but
consistent on one point: models trained primarily on English-language data display a Western bias. OpenAI’s GPT, for
example, matches U.S. value profiles closely but drifts from those of non-Western countries [12, 39].
Value alignment, however, is not the same as pragmatic competence. An LLM might endorse high power-distance
in an abstract questionnaire, yet still phrase a workplace email in a blunt, low-context style. Indeed, Kharchenko
and coauthors show that, although LLMs recognize that countries differ in values, they seldom adjust their answers
accordingly [35]. Aleem et al. [3] additionally report limited self-awareness of biases among LLMs and little attempt
at learning from user experiences, which may be different from the LLM’s training data.
Taken together, the above studies suggest that some cultural knowledge is built into current LLMs. However, two
crucial questions for LLM translations remain open: Do LLMs apply cultural knowledge when they translate text from
one language into another? And if not, can prompting strategies coax them toward more culturally sensitive translations?
2.4
Cultural sensitivity of LLM translations
State-of-the-art LLMs already deliver translations that rival professional translators on lexical accuracy. GPT-4, for
example, matches both Google Translate and human translators when converting short English passages into Mandarin
[68]. An overview of studies on GPT translations reports similar parity across multiple language pairs [14]. However,
these evaluations focus on literal accuracy; they do not test whether an LLM recognizes culture-specific language
patterns and do not adjust LLMs appropriately to the target language.
Three structural hurdles make that task difficult. First, mainstream LLMs are trained to optimize some form of
numerical objective function representing token-level errors or overlap with parallel corpora [18, 60], steering them
toward literal translations rather than considering pragmatic context and thus cultural appropriateness. Second, Eng-
lish dominates pre-training data [17]. OpenAI’s GPT in particular was developed predominantly with monolingual
English training data, so its internal language representations lean toward English discourse norms and often mishan-
dle non-English language patterns [35]. Third, LLM output tends to align with the culture embedded in the prompting

--- Page 6 ---

6
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
language [37]. Identical questions posed in English or Japanese activate different value profiles, reflecting language-
specific subnetworks learned during training [4]. Together, these hurdles suggest that an English-language prompt
without further instructions will not yield a translation attuned to Japanese culture-specific language patterns.
Prompt engineering has been proposed to influence the style, precision, and accuracy of LLM translations [24, 33].
Adding details about purpose, audience, or task has been found to raise overall translation quality [14]. For example,
Gu [27] even shows that integrating linguistic theory in the prompt improves translations for complex sentences.
However, to the best of our knowledge, no published study has asked whether these techniques also improve cultural
sensitivity, that is, whether they help an LLM reproduce the formality, directness, or mitigating language expected in
the target culture.
2.5
Research gap
While the HCI community has a long tradition of studying user behavior across cultures by emphasizing principles for
cross-cultural co-design [6] and value-sensitive approaches to embedding stakeholder values in technology [8], it also
includes classic and contemporary assessments showing that perceptions of aesthetics, usability, and satisfaction vary
by culture [5, 59, 65], alongside reflective perspectives that interrogate what “culture” means in practice [11]. Taken
together, these strands repeatedly emphasize the importance of cultural awareness and cultural appropriateness as
foundations for successful user interactions [6, 65]. This body of work shows that culture is not a peripheral attribute
but a determinant of interactional success: it shapes users’mental models, privacy expectations, politeness strategies
and turn-taking, risk perceptions and trust in automation, interpretations of symbols and color, humor and metaphor
comprehension, and help-seeking behavior, each with direct implications for accessibility, safety, satisfaction, and
long-term adoption [59]. Designing with culture in mind therefore enables more inclusive experiences, reducing fail-
ure modes such as misunderstanding [53]. However, concrete guidelines for designing culturally aware systems that
operate on natural language are missing; we thus focus on the role of cultural sensitivity in machine translation.
Due to that cross-cultural pragmatics in existing LLM research is neglected, evidence on how well LLMs handle
culture-specific language patterns in translation is also lacking. To fill this gap, we first analyze the cultural sensitivity
of LLMs through the lens of cross-cultural pragmatics and further develop HCI recommendations for designing cultur-
ally aware LLMs that, using careful prompting strategies, steer the LLM toward more culturally sensitive translations.
3
Materials
3.1
Setting
This study asks a central HCI design question: How can prompt design help LLMs generate culturally appropriate trans-
lations that support effective communication in cross-cultural workplaces? As LLMs become increasingly embedded in
day-to-day communication tools, this raises the question of how the design of LLMs can capture culturally appro-
priate language, especially since prompting is the primary way users interact with and steer LLM output. While NLP
research has shown that prompts can reduce cultural bias and improve translation quality [24, 33, 37, 40], key questions
at the HCI interface remain underexplored, particularly how prompt design can support culturally sensitive, real-world
interaction.
To explore this, we focus on U.S. English to Japanese translation. Both languages are characterized by a well-
documented and high-impact contrast in workplace communication norms. On the one hand, U.S. business English
tends to low power distance [30] and direct, explicit expression [48], whereas, on the other hand, Japanese business

--- Page 7 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
7
communication emphasizes hierarchy [30], politeness[56], and indirect expression [57]. These differences in cultural
norms for language use are especially salient in subordinate-to-supervisor interactions, where seemingly minor tone
mismatches can lead to confusion or perceived disrespect [15, 47, 57].
Informed by earlier HCI research examining cultural dimensions [6, 11, 53], our setting presents a rich testbed for
studying how LLM-based tools handle interactional appropriateness. Poorly adapted translations in such contexts can
cause misunderstandings, diminish user trust, or create unintended offense, which are issues of real consequence in
global teams. By focusing on this pair, we examine not just the linguistic correctness of LLM outputs, but their cultural
fit as experienced by users from the target culture. Finally, the choice was also driven by the practical relevance: the
U.S. and Japan are major trading partners, ranking first and fifth in global GDP, respectively [23, 50, 52]. Many real-
world enterprise tools (email assistants, messaging platforms, and document translators) must bridge these cultural
differences at scale. Our study contributes insights into how prompt design can serve as a lightweight but effective
lever for improving cross-cultural usability in LLM-driven interactions.
3.2
Corpus
To evaluate the cultural sensitivity of LLMs in real-world communication contexts, we created a corpus of five hypo-
thetical emails that a subordinate in a multinational tech firm might send to a supervisor. Each message was originally
composed in U.S. English by native speakers of U.S. American English, who were employed by a large technology
corporation and who were instructed to write as they naturally would in a professional setting. To respect the privacy
of individuals, all content is fictional, and no private or identifiable information was included. The ethics board at the
lead author’s institution (approval number: [hidden for anonymized review]) approved the use of these hypothetical
emails for our qualitative analysis and online experiment because the content is fictional and contains no personal
data.
Our email corpus was designed to reflect high-stakes, socially delicate interactions where cultural expectations are
especially pronounced. Specifically, we focus on five face-threatening speech acts, which frequently arise in business
communication and typically follow different culture-specific language patterns [25, 31, 38, 57]: (1) Reest (asking
for a deadline extension), (2) Refusal (declining an out-of-hours work event), (3) disagReement (disagreeing with
an unrealistic timeline), (4) apology (apologizing for sending incorrect data), and (5) gRatitude (thanking a super-
visor for approving a proposal). Each of these speech acts requires subtle adjustments in formality, directness, and
mitigating language, which are features that vary across cultures and are thus important for maintaining professional
communication. The content for the Reest email is provided in Fig. 2 (all other emails are in our Supplementary
Materials).
3.3
Prompt design
To translate the email communication, we designed three prompts with different underlying strategies (full text in
Table 1):
(1) The naïve prompt simply says “Translate the following email to Japanese.”
(2) The audience-targeted prompt assigns the model the role of a bilingual business translator, specifies that
the email is from a U.S. subordinate to a Japanese supervisor, and asks for a polite tone that sounds natural to
a Japanese speaker in a professional setting.

--- Page 8 ---

8
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
Mail #1 (Request) – English original
Dear [Supervisor’s first name],
I hope your day is going well. I’m writing to request a two-day extension on the Content Modularization report you asked me to put together.
Unfortunately, the Content Library dashboard is not updated. I spoke with [colleague], the dashboard owner, and she assured me the updates
would be completed within the next 24 hours.
I apologize for any inconvenience this may cause. Moving forward, I will work with Colleen to get a better understanding of the library
dashboard update schedule so that I can align the dashboard updates with our Content Modularization reports.
Thank you for your support and let me know if you have any questions.
Warm regards,
[Your first name]
Fig. 2. Example mail. English source version of Mail #1 (Request) used in Study 1 and Study 2. All other prompt variants and
translations are available in our GitHub repository.
(3) The instructional prompt adds explicit details about Japanese business etiquette, such as forms of address,
opening and closing formulas, and use of honorifics. We later expect the translation quality to rise from naïve
to audience-targeted to instructional prompts.
The prompt design followed best practices in prompt engineering and prior research [21, 26, 41]. Each prompt begins
with a clear task definition and is structured using different sections to organize instructions, followed by contextual
information (e.g., about the sender, recipient, and communication goals) and the desired output format. All prompts
were externally checked and refined by three experts in prompt writing and two native speakers who are also experts
in Japanese business communication.
In our experiments, we used GPT-4.5-preview-2025-02-27 (temperature = 0, accessed via the OpenAI API) to translate
each of the five source emails under the different prompting strategies. We selected GPT-4.5 for our experiments
because, at the time of the study, it was regarded as the most advanced LLM for writing tasks. Further, LLMs from
the GPT-4 family are widely deployed in practice and were found to be the most advanced LLM in terms of cultural
sensitivity [46]. Following best-practice recommendations [21], we set the temperature to 0 to ensure deterministic
outputs, which allows for consistent comparisons across prompting strategies. The resulting corpus comprises the five
English originals plus fifteen Japanese translations, all of which are available in our GitHub repository.
4
Study 1: Qualitative analysis of pragmatic adaptation
To understand how LLMs adapt to target-specific cultural language patterns (RQ1 and RQ3a), we conducted a qualita-
tive analysis using House and Kádár’s cross-cultural speech act coding scheme [31]. We manually coded all messages
along three dimensions: (i) formality, (ii) directness, and (iii) use of mitigating language (described below). We then
compared the English originals to the Japanese outputs to assess how well GPT-4.5 adapted to Japanese culture-specific
language patterns across different prompting strategies.
4.1
Method
We conducted a fine-grained manual analysis of different language patterns in the corpus using the cross-cultural
speech act coding scheme developed by House and Kádár [31]. This coding scheme operationalizes key dimensions
of cross-cultural pragmatic analysis (i.e., formality, directness, and use of mitigating language) through a set of core
categories that occur in every language yet are realized differently in each culture. 2 lists the categories provided by

--- Page 9 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
9
Strategy
Prompt
(1) Naïve prompt
Please translate the following email to Japanese.
[English email text inserted here]
(2) Audience-targeted prompt
You are an experienced bilingual translator with a strong background in Japanese business etiquette and
cross-cultural communication.
Task: Please translate the following email from a U.S.-based subordinate to a Japanese supervisor into
Japanese, ensuring the language is culturally sensitive and aligns with Japanese communication norms.
Method: Structure your translation so it sounds natural to a Japanese speaker in a professional setting. Use
a polite, respectful tone appropriate for a subordinate writing to a supervisor.
Output: Provide your final translation as a single coherent message in Japanese. Do not provide a
line-by-line breakdown of the English text—deliver a seamlessly integrated email.
[English email text inserted here]
(3) Instructional prompt
You are an experienced bilingual translator with a strong background in Japanese business etiquette and
cross-cultural communication.
Task: Please translate the following email from a U.S.-based subordinate to a Japanese supervisor into
Japanese, ensuring the language is culturally sensitive and aligns with Japanese communication norms.
Concepts (Japanese Business Etiquette and Culture):
• In Japanese business communication—especially between a subordinate and a superior—hierarchical
awareness, politeness, formality, and the use of honorifics (keigo) are essential.
• It is common to address superiors by their last name plus their official title (e.g., 課長“kachō,”部長
“buchō”).
• Formulaic relational opening phrases typically appear in the first line of an email. Examples are お世話に
なっておりますor 大変お世話になっておりますif particular deference and politeness needs to be
shown..
• Polite forms (です・ます調) and respectful expressions (keigo) are used throughout the message.
• Emails generally close with a polite phrase such as よろしくお願いいたします.
• A subordinate’s signature often includes the full name (first and last name).
• Because Japan is high-context, high power-distance, and collectivist, communication is frequently indirect
to maintain interpersonal harmony. Direct refusals or confrontations are avoided.
• Lower-status individuals display deference, convey humility, and apologize more frequently when
imposing on superiors.
Method: Structure your translation so it sounds natural to a Japanese speaker in a professional setting. Use
a polite, respectful tone appropriate for a subordinate writing to a supervisor, and incorporate mitigating
language that preserves the face of both sender and receiver. Where suitable, include phrases that convey
humility and respect.
Output: Provide your final translation as a single coherent message in Japanese. Do not provide a
line-by-line breakdown of the English text—deliver a seamlessly integrated email.
[English email text inserted here]
Table 1. Prompting strategies used to generate Japanese translations. The corresponding outputs are available in our GitHub
repository.
House and Kádar, along with short descriptions indicating specific codes within each category. Within the category of
Alerters, for example, we used four different codes: (1) Title/role, (2) Surname, (3) First name, and (4) Honorific suffix.
The complete codebook is provided in our Supplementary Materials. The codebook includes House and Kádár’s original
code descriptions and examples along with our own descriptions of the Japan-specific codes, which we developed
during our analysis (marked with an asterisk in the coding scheme that is provdided in the Supplementary Material).
Because cross-cultural pragmatics benefits from both insider and outsider viewpoints [31], the coding team com-
bined an emic (native-insider) and an etic (researcher-outsider) perspective. The lead author, a scholar of cross-cultural
pragmatics, trained a Japanese native speaker as a research assistant in the coding scheme. Training included a line-
by-line walk-through of the codebook and joint coding of one English email outside of the study corpus to ensure
methodological consistency with the coding scheme.
The main coding process took about 50 hours and followed four steps. (1) Both coders independently annotated the
five English source emails. (2) They compared their work line by line and resolved discrepancies until they reached

--- Page 10 ---

10
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
Dimension
Category/code
Description
Formality
Alerters
The speaker first “alerts” the recipient, calling them Professor Sato, Mr Johnson, or simply
Judith. In Japanese, the addressee’s name is almost always followed by an honorific suffix
such as -san (さん) or -sama (様). The choice of title, surname, first name, and suffix signals
how formal and deferential the speech act is expected to be [51].
Directness
Speech act perspective
Who is framed as the agent of the action? A speech act can be speaker-oriented (“Could
I borrow your notes?”), addressee-oriented (“Could you lend me your notes?”), or include
both (“Could we swap notes?”). The selected viewpoint changes how forceful or deferential
the request feels. The Japanese language favors ellipsis (zero pronouns) to avoid overtly
naming the addressee.
Level of directness
How bluntly is the intention stated? Speakers may opt for a high directness level (“I’m
asking you to clean the kitchen.”), soften their intention (“I must ask you to clean the kitchen.”),
or merely hint at their intention (“You’ve been busy here, haven’t you?”). Speech acts with
low directness levels require higher attention to context and are easily misunderstood by
recipients from cultures that emphasize directness [16].
Mitigation
Downgraders
Speakers can soften an imposition through syntactic downgraders such as conditional
clauses (“I was wondering if you could present a week earlier.”) or lexical downgraders (“It
would somehow fit better if you could present next week.”). Downgraders are important po-
liteness markers and differ widely across cultures [47]. Japanese speakers often use self-
deprecation phrases such as 未熟者ですが(“Although I am still inexperienced…”) to reduce
the imposition before making a request or statement.
Upgraders
Speakers may also increase the pragmatic force of their speech act, e.g., by adding intensi-
fiers (“I am terribly sorry for this mistake.”) or signaling commitment (“You certainly don’t
mind, do you?”).
Supportive moves
Additional sentences can either mitigate or amplify the main speech act by getting a pre-
commitment (“Could you do me a favour?”), giving reasons (“I missed class; could I borrow
your notes?”), or minimizing the imposition (“Can I borrow your notes, but only if you are
not studying with them today?”). In Japanese, speech acts are often prefaced with a brief
apology to soften the forthcoming imposition.
Table 2. Summary of the coding scheme. We operationalize formality, directness, and mitigation based on the categorization
developed by House and Kádár [31]. This table lists House and Kádár’s original categories; the descriptions (including how these
adapt to English-Japanese translations) are our own and were developed by an interdisciplinary team with expertise in linguistics
and cultural pragmatics for Japanese and English.
agreement, with the lead author clarifying any points that were unclear. (2) The Japanese coder annotated all 15 Japan-
ese translations (5 emails 𝑡𝑖𝑚𝑒𝑠3 prompts), using the core categories and situated categories provided by House and
Kádár. During this process, she flagged phrasings that appeared culturally unique to Japanese. Together with the lead
author, she then reviewed these cases against the pragmatics literature (e.g., [38, 43, 56] ) and created a small set of
additional, Japan-specific situated categories (marked with an asterisk in the codebook). All coding and revisions were
done in Atlas.ti (web version 8.7.0; https://atlasti.com/), with an audit trail logging each decision.
Finally, we compared the frequency and type of codes in each English original with the three Japanese translations
(using the research assistant’s codes for both the English source emails and the Japanese translations). The lead author
and research assistant then interpreted these language patterns together to assess the extent to which the LLM adjusted
to Japanese culture-specific language patterns under each of the three prompting conditions.
4.2
Results
Table 3 reports how often each code appeared in the English originals and in the three Japanese prompt conditions. In
brief, the naïve “just-translate” prompt produced only modest adjustments toward Japanese culture-specific language
patterns, whereas the audience-targeted prompt produced a clear shift, and the instructional prompt yielded the most
extensive adaptation. Below, we discuss the findings along the different categories of cross-cultural pragmatics.

--- Page 11 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
11
Alerters (Figure 3): In the U.S., source e-mails supervisors are addressed with first names, and authors also sign
off with their first name. Japanese business etiquette, by contrast, calls for the supervisor’s family name plus honorific
job-title suffix and for the writer’s full name in the signature. We expected a gradual shift toward this norm as the
prompts grew more sophisticated. That is what we observed. With the naïve prompt, the LLM kept first names and
merely added the general honorific suffix -san (さん) or -sama (様). Under the audience-targeted prompt, the model
switched to family names for both addressee and sender, still using the general suffixes. The instructional prompt
replaced the general suffix with a job-title suffix and required the sender’s full name. Thus, the predicted progression
toward Japanese-specific alerters was confirmed.
Speech act perspective (Figure 4): The English messages rely heavily on the pronoun I. Japanese normally omits
pronouns so as not to spotlight either party, except in apologies, where explicit self-reference signals full responsibil-
ity. Again, we assumed a progressive shift towards these culture-specific language patterns with more sophisticated
prompts. All three prompt conditions follow the Japanese pattern by almost entirely eliminating personal pronouns.
One notable exception appears in the apology message under the audience-targeted and instructional prompts, where
senders explicitly refer to themselves to accept full responsibility for the error. The expected rise in cultural sensitivity
with more refined prompts, therefore, holds for the speech-act perspective as well.
Level of directness (Figure 5): House and Kádár rank language patterns signaling directness from explicit per-
formatives (most direct) to mild hints (most indirect; see the coding scheme in our Supplementary Materials for full
explanations). While U.S. business writing values directness, Japanese norms favor indirect expressions to save the
sender’s and addressee’s face. We thus expected a stepwise move toward more indirect forms. The data do not show
such a pattern. However, we found only small differences. Hedged performatives (e.g., “I’m writing to request …”)
become slightly more common under the audience-targeted and instructional prompts, while want-statements and
possibility questions become slightly less common. The shifts are small and inconsistent. Our expectation for levels of
directness was therefore not confirmed.
Downgraders (Figure 6): While U.S. English is known for explicit statements, Japanese cultural norms expect sub-
ordinates addressing supervisors to mitigate the force of face-threatening speech acts through the use of so-called
downgraders. Consequently, we anticipated a steady increase in downgraders from the source emails throughout the
three prompt conditions. Code counts do not reveal a simple upward trend, but a closer look at specific types of down-
graders does indicate shifts in language patterns. All Japanese versions use the honorific passive to make requests less
imposing. For instance, the instructional translation of the disagreement email asks ご検討いただけないでしょうか
(literally “Could I humbly receive your consideration?”). In contrast, the English originals rely mainly on subjectivisers
such as “I believe” or “unfortunately”, whereas the Japanese translations, especially under the instructional prompt,
add self-depreciation, which is a Japan-specific type of downgrader absent from the English originals. For example, the
email requesting a deadline extension produced under the instructional prompt adds 私の確認不足(“my failure to
check properly”), foregrounding the speaker’s own shortcomings to ease acceptance of the upcoming request. Hence,
the predicted shift appears, though only for certain downgrader types.
Upgraders (Figure 7): Rather than softening the force of a statement, upgraders intensify it. In hierarchical Japanese
correspondence, they commonly intensify humility and deference, thus mitigating the force of a face-threatening
speech act. In U.S. business mail, such deference is rare. We therefore predicted upgraders to occur more frequently in
the Japanese translations compared to the original emails, and to increase in frequency with more refined prompts. As
expected, the use of upgraders increases steadily from the originals through the three prompts. These expressions do
not strengthen the face-threatening act; instead, they intensify apologies or gratitude, for example, through adverbs

--- Page 12 ---

12
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
that amplify regret or the phrase 今後とも(“from now on as well”), which broadens the scope of appreciation. Such
intensifiers appear most often in the audience-targeted and instructional translations, where they function as extra
politeness. This confirms our prediction for upgraders.
Supportive moves (Figure 8): While both cultures mitigate the force of face-threatening speech acts through ad-
ditional statements, so-called supportive moves, U.S. writers tend to be more assertive. We predicted more humble,
supportive moves in the Japanese translations, particularly in the refined prompts. In line with this, assertive tactics
such as pre-thanking the supervisor for agreeing (“Thank you very much for your understanding”) survive only in the
naïve translations but disappear entirely under the more refined prompts. All versions give reasons for the request,
refusal, or disagreement, but the Japanese texts add a culture-specific device: the apology-preface. Phrases like お手
数をおかけいたしますが(“[I] will humbly impose trouble on you, but …”), found in the audience-targeted disagree-
ment emails, begin with an apology to soften what follows. Because this pattern is absent from the English originals,
its presence signals an active shift toward Japanese pragmatic norms. The predicted shift is therefore confirmed for
supportive moves.
In sum, four of the six pragmatic categories (i.e., alerters, speech-act perspective, upgraders, and supportive moves)
show the expected stepwise shift to Japanese culture-specific language patterns from the naïve to the audience-targeted
to the instructional prompt. Downgraders exhibit a more nuanced pattern, and the level of directness shows little
systematic change. Together, the results underline how strongly prompt design influences the cultural sensitivity of
LLM translations.

--- Page 13 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
13
Code
Original emails (English)
Translated emails (Japanese)
(1) naïve prompt
(2) audience‑targeted prompt
(3) instructional prompt
Formality
Alerter
• First name
10
10
0
5
• Surname
0
0
12
11
• Honorific suffix
0
5
5
5
• Title/role
0
0
0
4
Directness
Speech act perspective
• Speaker-orientation
19
0
1
1
• Addressee-orientation
4
0
0
0
• Speaker and addressee-orientation
5
0
0
0
• Impersonal (people/they/one/etc.)
6
0
0
0
Level of directness
• 1 Explicit performative
1
0
0
1
• 2 Hedged performative
1
1
2
2
• 3 Want statement
3
3
1
2
• 4 Preparatory
1
2
0
0
• 5 Mild hint
0
0
1
0
Mitigation
Downgrader
• Downtoner
1
0
0
0
• Hedge
2
0
0
2
• Self‑deprecation
0
1
1
3
• Subjectiviser
3
1
1
2
• Understater
0
1
0
2
• Conditional
3
1
2
0
• Conditional clause
2
2
0
2
• Honorific passive
0
3
1
2
• Tense
1
0
0
0
Upgrader
• Commitment indicator
0
0
2
1
• Intensifier
6
7
12
12
• Lexical uptoner
1
0
1
0
Supportive moves
• Apology‑preface
0
2
3
2
• Disarmer
1
0
1
0
• Getting pre‑commitment
4
2
0
0
• Grounder
5
6
6
6
• Imposition minimizer
0
0
2
0
• Preparator
0
1
0
1
• Manipulation/appeasement
5
5
2
3
Table 3. Language patterns in source email vs. translations across different prompting strategies. This table displays the
frequency of particular language patterns marking formality, directness, and mitigation across the original English emails and the
three GPT‑4.5 prompt conditions. Darker background shades indicate higher frequency.

--- Page 14 ---

14
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
0.0
2.5
5.0
7.5
10.0
12.5
First name
Surname
Honorific suffix
Title/role
Count
Prompt
English originals
Naïve
Audience−targeted
Instructional
Alerters
Fig. 3. Total counts of “alerter” codes in English and Japanese translated emails by prompt type.
0
5
10
15
Speaker−orientation
Addressee−orientation
Speaker and addressee−orientation
Impersonal (people/they/one/etc.)
Count
Prompt
English originals
Naïve
Audience−targeted
Instructional
Speech act perspective
Fig. 4. Total counts of “speech act perspective” codes in English and Japanese translated emails by prompt type.
0
1
2
3
1 Explicit performative
2 Hedged performative
3 Want statement
4 Preparatory
5 Mild hint
Count
Prompt
English originals
Naïve
Audience−targeted
Instructional
Levels of directness
Fig. 5. Total counts of “levels of directness” codes in English and Japanese translated emails by prompt type.

--- Page 15 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
15
0
1
2
3
Downtoner
Hedge
Self−deprecation
Subjectivizer
Understater
Conditional
Conditional clause
Honorific passive
Tense
Commitment indicator
Count
Prompt
English originals
Naïve
Audience−targeted
Instructional
Downgraders
Fig. 6. Total counts of “downgrader” codes in English and Japanese translated emails by prompt type.
0.0
2.5
5.0
7.5
10.0
12.5
Intensifier
Lexical uptoner
Count
Prompt
English originals
Naïve
Audience−targeted
Instructional
Upgraders
Fig. 7. Total counts of “upgrader” codes in English and Japanese translated emails by prompt type.
0
2
4
6
Apology−preface
Disarmer
Getting a pre−commitment
Grounder
Imposition minimizer
Preparator
Manipulation/Appeasement
Count
Prompt
English originals
Naïve
Audience−targeted
Instructional
Supportive moves
Fig. 8. Total counts of “supportive move” codes in English and Japanese translated emails by prompt type.

--- Page 16 ---

16
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
5
Study 2: User evaluation
To explore RQ2 and RQ3b, we test how Japanese native speakers (members of the target culture) perceive the English-
Japanese LLM translations under our three prompt conditions. In a within‐subjects design, each participant read the
same five email scenarios (request, refusal, disagreement, apology, gratitude) and evaluated all three Japanese versions
generated from : (1) a naïve “just translate” prompt, (2) an audience‑targeted prompt that informs about the recipient’s
cultural background, and (3) an instructional prompt that includes explicit guidance on Japanese communication norms.
Our primary question was whether adding minimal or extensive cultural guidance to the prompt significantly increases
(a) perceived appropriateness and (b) the recipient’s intention to comply with the email request. A within-subjects
design was ideal here because it allows each participant to serve as their own control when comparing the three prompt
conditions. Randomizing the conditions (and ensuring that no two variants of the same email appear consecutively)
protects against simple ordering or transfer effects, making the within-subjects design the most efficient and sensitive
method for detecting even small differences in how prompt framing affects perceived appropriateness and intention
to comply with the email request.
5.1
Method
5.1.1
Participants. We recruited 50 native Japanese speakers (41 female, 9 male; 𝑀age = 44.0 years, SD = 11.4) through
the Prolific crowd-sourced experiment service. All participants gave informed consent. We filtered for participants
who had Japanese as their first language and an approval rate of 90 to 100% for previous studies taken on Prolific. All
participants provided informed consent and were compensated GPB 4.5 for their participation (i.e., above minimum
wage). The median time taken to complete the full study was 14 minutes. We manually checked that responses were
completed before approving payment. Given that no participants failed the attention check, none of the 50 participants
were omitted from the dataset. The study protocol and analysis plan were pre-registered on AsPredicted (Registration
#219202; https://aspredicted.org/fpnz-s8r2.pdf) and approved by the ethics board at the lead author’s institution (hid-
den for anonymized review).
5.1.2
Procedure. We repurposed the same 15 translations (5 emails × 3 prompt conditions) from Study 1. Each partici-
pant saw all 15 translated emails. Each translation was presented in isolation against a plain white background, with no
accompanying English original. For each participant, email × prompt combinations were randomized in order; we used
Qualtrics’built‐in randomizer to ensure no two variants of the same source email appeared consecutively. Instructions
and items were translated to Japanese using ChatGPT (GPT-4.5-preview-2025-02-27, temp = 0.00). Where differences
were spotted, the source text was adjusted and the procedure repeated until equivalence was reached. Subsequently,
two Japanese-English bilinguals compared the English source text with the Japanese translation, and some further
adjustments were made.
After providing informed consent, participants rated 15 translated emails in randomized order, with each email
appearing on a separate page. On each page, they answered the three perceived appropriateness items and five intention
to comply with the email request items, then proceeded to the next email. In addition, an attention check ensured
participants read the instructions carefully. At the end, participants had access to a debriefing document.
5.1.3
Measures. We assessed two primary constructs: (i) perceived appropriateness and (ii) intention to comply with
the email request, using multi‐item Likert scales. Both are recorded using a 7-Likert scale from “strongly disagree” (1)
to “strongly agree”. The full list of items used for these evaluations is provided in the appendix (see Appendix A).

--- Page 17 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
17
(1) Perceived appropriateness. In Study 1, we applied the House & Kádár scheme to code how each email realizes
cultural norms for formality, directness, and mitigation—that is, linguistic devices that soften or, at times, strengthen
the force of a speech act. In the experimental study with human readers, we replaced the technical term mitigation with
the more familiar politeness when measuring perceptions. We therefore assessed perceived appropriateness along for-
mality, directness, and politeness, where perceived appropriateness is “the ability to perform speech acts at the proper
level of politeness, directness, and formality in the given situations” [61, p. 273]. Following Halenko and Economi-
dou‐Kogetsidis [28], participants rated each e-mail on seven-point Likert scales for politeness, directness, and formal-
ity; together, these three judgments provide a holistic measure of pragmatic appropriateness in Japanese workplace
e-mails. A sample item used to assess perceived appropriateness was: “As a supervisor, I would be satisfied with this
email because it is written with a sufficient level of politeness that is appropriate and effective for the situation” (Japanese:
「このメールは、状況に対して適切で効果的な十分な丁寧さで書かれているため、上司として満足できると
思う。」). In the main study, these three items, administered across all 15 email scenarios (45 total observations per
participant), yielded a Cronbach’s 𝛼of .970.
(2) Intention to comply with the email request. Grounded in the Theory of Planned Behavior[1, 22], intention
to comply measures a recipient’s intention to comply with or act upon the email’s content. Ajzen [2] recommends
using 5 to 6 items to capture intention reliably. We adapted his example (“I intend to exercise …”) to email compliance
scenarios, creating five items on a seven‐point scale (1 = Strongly Disagree, 7 = Strongly Agree) that reflect a Japanese
employee’s likely response to a request or suggestion. A sample item used to assess intention to comply with the email
request was: “I feel inclined to respond favorably to this email” (Japanese: このメールに対して好意的に対応した
いと思う。). The five items were averaged to yield a single intention to comply score (range: 1 to 7). The internal
consistency of this five-item scale was 𝛼= .986.
Attention Check. To verify that participants attended closely to each set of items, one of the fifteen rating pages
included an embedded attention check stating: “To ensure that you are reading the questions carefully, please select
Strongly Disagree (1) for this statement” (Japanese: 「質問を注意深く読んでいることを確認するため、この項
目では『全くそう思わない（1）』を選択してください。」).
5.2
Results
5.2.1
Data preparation. Data were exported from Qualtrics and screened in SPSS v30. A second file was created where
ratings were reshaped from wide to long format (one row per participant × email × prompt). In this new file, there were
50 × 15 = 750 valid email‐ratings per dependent variable. No individual survey item was missing for any of these 750
cases. Distributions of perceived appropriateness and intention to comply with the email request by prompt condition
were examined (Descriptives: skewness < |1.53| for appropriateness and < |1.25| for intention to comply, kurtosis <
|3.19| and < |2.14|, respectively) and Shapiro–Wilk tests (all 𝑝< .001). Given that skewness and kurtosis remained
within acceptable bounds for robust parametric methods, we proceeded with the repeated‐measures ANOVAs and
mixed‐effects models. We computed mean composites for perceived appropriateness and intention to comply with the
email request for each of the 15 email ratings.
5.2.2
Perceived appropriateness. Figure 9 presents a raincloud plot of perceived appropriateness across the three
prompt conditions, which shows kernel density distributions, individual jittered scores, and overlaid median lines
to show how the entire score distribution shifts and tightens with added cultural guidance. Figure 10 displays the same

--- Page 18 ---

18
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
data as mean points with 95 % confidence intervals and jittered individual scores, with asterisks indicating Bonferroni-
adjusted significant pairwise differences between conditions. Under the naïve “just translate,” raw mean perceived ap-
propriateness was 5.52 (SD = 0.83). Introducing minimal cultural guidance via the audience-targeted prompt increased
the raw mean to 5.72 (SD = 0.91), and the instructional prompt yielded the highest raw mean of 5.83 (SD = 0.84).
Visually, individual judgments cluster more tightly from naïve “just translate” to audience-targeted, and again from
audience-targeted to instructional, suggesting growing consensus as cultural/pragmatic cues are added (Figure 10).
2
3
4
5
6
7
(1) naïve
(2) audience−targeted
(3) instructional
perceived appropriateness
Fig. 9. Raincloud distribution of perceived appropriateness ratings.
**
*
(3) instructional
(2) audience−targeted
(1) naïve
2
4
6
8
perceived appropriateness
Fig. 10. Boxplots of mean ratings with pairwise statistical significance tests.
A one-way repeated‐measures ANOVA confirmed a significant main effect of prompt condition on perceived ap-
propriateness: 𝐹(1.74, 85.47) = 9.44, 𝑝< .001, 𝜂2𝑝= .16 (Mauchly’s 𝑊= .853, 𝜒2(2) = 7.61, 𝑝= .022; Greenhouse–Geisser
𝜀= .872). Pairwise contrasts (Bonferroni‐adjusted 𝛼= .0167) indicated that the audience-targeted prompt led to signif-
icantly higher perceived appropriateness than naïve “just translate” (𝛿= +0.20, SE = 0.06, t(49) = 3.17, 𝑝= .008, 95 %
CI [0.04, 0.35]), and the instructional prompt outperformed naïve “just translate” as well (𝛿= +0.31, SE = 0.08, 𝑡(49) =
3.65, 𝑝= .002, 95 % CI [0.10, 0.52]). Although the jump from audience-targeted to instructional was positive (𝛿= +0.11,
SE = 0.07, 𝑡(49) = 1.64), it did not reach the corrected threshold (𝑝= .330). Together, these findings demonstrate that
even minimal cultural context (audience-targeted) significantly boosts perceived appropriateness relative to a naïve
translation, and that extensive instruction (instructional prompt) confers an additional, albeit smaller, gain.
5.2.3
Intention to comply with the email request. Figure 11 shows a raincloud plot of Behavioral Intention across the
three prompt conditions, combining density curves, individual jittered scores, and overlaid medians to illustrate how
the willingness to comply shifts and tightens as more cultural guidance is provided. Figure 12 presents the same data as
mean points with 95% confidence intervals and jittered individual scores, with asterisks marking Bonferroni-adjusted

--- Page 19 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
19
significant pairwise differences between conditions. Under naïve “just translate,” raw mean intention to comply with
the email request was 5.41 (SD = 0.90). The audience-targeted prompt raised this to 5.55 (SD = 0.95), and the instructional
prompt produced the highest mean intention to comply of 5.64 (SD = 0.92). As with perceived appropriateness, the
spread of individual data narrows from naïve “just translate” to audience-targeted to instructional, indicating more
consistent willingness to comply when cultural/pragmatic instructions are provided.
2
3
4
5
6
7
(1) naïve
(2) audience−targeted
(3) instructional
intention to comply
with the email request
Fig. 11. Raincloud distribution of intent to comply ratings.
ns
*
(3) instructional
(2) audience−targeted
(1) naïve
2
4
6
8
intention to comply with the email request
Fig. 12. Boxplots of mean ratings with pairwise significance markers.
A repeated‐measures ANOVA on intention to comply with the email request revealed a significant effect of prompt
condition: 𝐹(1.79, 87.47) = 6.16, 𝑝= .004, 𝜂2𝑝= .11 (Mauchly’s 𝑊= .880, 𝜒2(2) = 6.16, 𝑝= .046; Greenhouse–Geisser 𝜀
= .893). Bonferroni‐adjusted pairwise comparisons showed that the instructional prompt elicited significantly higher
intention to comply than naïve “just translate” (𝛿= +0.23, SE = 0.08, 𝑡(49) = 3.02, 𝑝= .011, 95 % CI [0.04, 0.41]). The
increase from naïve “just translate” to audience-targeted (𝛿= +0.13, SE = 0.06, 𝑡(49) = 2.16) did not reach corrected
significance (p = .061), nor did the audience-targeted to instructional contrast (𝛿= +0.10, SE = 0.07, 𝑡(49) = 1.49, 𝑝=
.429). In sum, extensive instruction significantly boosts intention to comply with the email request over a naïve prompt,
while minimal cultural cues show a positive but non‐significant trend.
5.2.4
Mixed‐effects regression. To verify that these effects remained significant after accounting for participant- and
email-level variability, we fitted linear mixed‐effects models with random intercepts for participant and email type,
using Compound Symmetry for the within‐subject covariance structure. Estimated marginal means from this model
were 5.52 (SE = 0.12) for the naïve “just translate” prompt, 5.72 (SE = 0.12) for the audience-targeted prompt, and
5.83 (SE = 0.12) for the instructional prompt. Pairwise comparisons showed that audience-targeted translations were
rated significantly more appropriate than naïve “just translate” (mean difference = +0.20, 𝑝= .037), and instructional

--- Page 20 ---

20
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
translations were likewise more appropriate than naïve “just translate” (mean difference = +0.31, 𝑝< .001). However,
the difference between audience-targeted and instructional did not reach significance (mean difference = +0.11, 𝑝=
.517), indicating that most of the improvement came from providing minimal cultural guidance.
Similarly, the estimated marginal means were 5.41 (SE = 0.13) under naïve “just translate,” 5.55 (SE = 0.13) un-
der audience-targeted, and 5.64 (SE = 0.13) under instructional. Contrast tests revealed that the instructional prompt
produced a significantly higher intention to comply than naïve “just translate” (mean difference = +0.23, 𝑝= .005).
The increase from naïve “just translate” to audience-targeted (+0.13) did not reach significance (𝑝= .206), nor did
the audience-targeted to instructional comparison (+0.10, 𝑝= .574). Thus, even after controlling for random effects,
minimal cultural instruction significantly boosted perceived appropriateness, and full instructional guidance yielded
the largest overall increases, particularly for intention, while the incremental benefit of instructional over audience-
targeted remained small and non‐significant.
6
Discussion
Below, we unpack what our findings mean for multilingual work, prompt writing, and model design with a particular
emphasis on HCI design principles, and we note the study’s main limitations and avenues for future research.
6.1
Why culturally sensitive LLM translation matters
Business people are increasingly using LLMs to support computer-mediated communication across languages and
cultures. As this reliance grows, the cultural sensitivity of LLMs (that is, the ability of LLMs to recognize, respect, and
respond to culture-specific language norms [7]) will gain in importance. Effective written business communication
is not a luxury: it improves employee satisfaction, supports better decisions, strengthens customer relationships, and
ultimately builds trust and collaboration [34, 66], thus immediately raising questions around how multi-lingual, cross-
cultural teams can effectively communicated when using tools for AI-mediated communication. We answer this using
our mixed-methods study.
Our qualitative coding shows that GPT-4.5, when given a naïve “just translate” prompt, altered culture-specific lan-
guage patterns of U.S. emails only superficially when rendering them in Japanese. Substantial adaptation emerged only
after we added cultural context to the prompt: first by naming the reader’s background (the audience-targeted prompt)
and even more after supplying explicit information on expected language patterns in Japanese business etiquette (the
instructional prompt). This finding carried over into the perceptions measured in Study 2. Japanese participants rated
audience-targeted translations as markedly more appropriate than naïve ones, and instructional translations highest
of all. A similar, though less pronounced, finding appeared for intention to comply with the email request: signaling
the recipient’s culture often increased willingness to comply, but only full instructions with Japanese etiquette rules
produced a clear, statistically significant boost.
Because language is central to how cultures reproduce themselves over time [62], misalignment with culture-specific
language patterns can distort workplace hierarchies. If Western employees consistently address Japanese managers
with language that sounds overly informal or blunt, the manager’s face may be damaged and their authority eroded.
Given the speed at which generative AI alters everyday writing practices, ensuring that LLMs handle such nuances
responsibly is an urgent task for the HCI community.

--- Page 21 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
21
6.2
Implications for prompt engineering
Drawing on cross-cultural pragmatics, we showed that tailored prompts can systematically raise the cultural sensitivity
of model output. The largest single improvement occurred when we simply told the model who the addressee was and
assigned the LLM the role of a bilingual business translator. The instructional prompt delivered the best overall scores,
but the incremental gain over the audience-targeted prompt was relatively modest. Mixed-effects analyses confirm
that these patterns persist after accounting for participant‐ and item‐level variability. In practical terms, users who
lack detailed knowledge of the target culture can still elicit noticeably more appropriate translations by adding one
straightforward line of cultural context. That said, such minimal prompting is likely to succeed only for languages and
cultures that are already well represented in the LLM’s training data. For low-resource languages and cultures, where
little built-in knowledge exists, more elaborate instructional prompting—or a model with richer cultural training—will
be necessary.
6.3
Implications for HCI design
While decades of cross-cultural HCI have mapped differences across individual backgrounds, language, and culture,
the field has recognized the importance of culture [11, 53], yet it remains comparatively silent on concrete, operational
design principles for cross-cultural interaction in LLM-mediated translation. We address this gap with an empirical
study showing that lightweight audience cues reliably steer LLM outputs toward culturally appropriate choices. Based
on these findings, we offer a set of actionable design principles that practitioners can adopt.
Principle 1: Integrating “cultural sensitivity” options into HCI interfaces benefits effective use.
In our Study 2, users responded positively to culturally aware outputs, often preferring translations that “sound right”
in their cultural context over literal accuracy. This has a clear practical value in business email drafting, customer
support chatbots, and global teamwork platforms. Prior HCI findings indicate that aligning with culturally shaped
expectations improves perceived usability and task performance, reinforcing that cultural sensitivity is a usability
feature, not just an ethical add-on [45, 54, 55].
Principle 2: Integrating customizable cultural profiles.
In practice, building culturally sensitive systems could be achieved through different HCI designs. For example, similar
to current personalization features in LLMs (e.g., region settings, formal vs. casual tone), LLM-mediated communication
tools could support richer cultural profiles. For example, users drafting professional emails might choose a “Japanese
workplace”profile that ensures honorifics and indirect expressions, or a “U.S. workplace”profile that emphasizes clarity
and directness. Thereby, we advance HCI work on culturally adaptive UIs and global design, which has shown that
user preferences and effective interaction styles vary widely across the globe [54, 55].
Interface features alone cannot ensure cultural sensitivity. Our findings support recent calls for embedding cultural
knowledge directly into model training [39, 40] and align with HCI traditions that foreground stakeholder values and
situated contexts throughout the lifecycle [6]. Still, our results show that even minimal audience cues substantially
improve cultural sensitivity in LLM translations. Rather than requiring users to craft complex prompts, translation
tools could incorporate a simple “culture-aware”toggle or drop-down selector. Such explicit, user-facing controls echo
longstanding HCI guidance to make cultural adaptation visible and selectable, rather than hidden defaults [45]. This
would enable quick adaptation for common, high-resource language pairs (e.g., English–Japanese, English–Spanish)

--- Page 22 ---

22
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
and make cultural customization visible to users, thereby building on evidence that culturally adaptive interfaces can
measurably improve efficiency and satisfaction [54].
Principle 3: Caution with default LLM outputs in machine translation.
Without explicit cues, LLMs tend to reflect the cultural biases of their training data, often producing text that is too
direct, casual, or impolite in certain contexts. Previous research warns that many interaction findings (and, by exten-
sion, default design priors) are biased toward WEIRD populations, thereby underscoring the need to surface and tune
defaults for diverse user bases [42]. Users should therefore be cautious when relying on default outputs, especially
in sensitive professional or cross-cultural contexts where missteps can undermine trust or relationships. Providing
audience cues and reviewing the tone of translations critically are simple but effective steps to ensure cultural appro-
priateness. However, Principle 3 is not only relevant for end-users but equally for AI agents or other tools that are
based on top of LLMs (e.g., live translation systems such as those integrated in Zoom, Microsoft Teams, or Apple’s
AirPods 3).
6.4
Limitations and future research
Our study has four main limitations, which present impactful opportunities for future HCI research. First, our corpus is
small. This is attributed to the complex multi-method coding that involves training native speakers as well as carefully
assessing each LLM output, a process which is naturally limited in terms of scalability. Future work should test a
broader range of text genres such as instant messaging, meeting minutes, performance reviews, customer-support
chats, press releases, and so on. Similarly, HCI or NLP research could develop tools that automate the coding of cross-
cultural pragmatics, but which we intentionally circumvented for our study to avoid potential bias in such automated
analysis. Second, our analysis focused on GPT-4.5, a state-of-the-art, frontier model at the time of writing. This was
again driven by the complexity of our multi-method study with a complex qualitative coding scheme. Nevertheless,
comparing multiple models would clarify the extent to which our effects can be generalized to other models. However,
previous research has found that many LLMs perform similarly (see the studies in [21]), so it is likely that these
results also generalize to other LLMs. The effects may be even more pronounced for models with lower capabilities
or those trained on data with fewer language backgrounds. Third, we translated solely from English into Japanese, a
high-resource direction that benefits from ample training data. Assessing low-resource pairs will reveal how far simple
audience-targeted prompts can go. Still, our choice is driven by the large, known differences between both cultures
as well as the importance of English and Japanese translations in day-to-day work. Finally, Study 2 measured self-
reported perceptions and intentions, not real behavior. Field experiments in live communication settings (including
tools like video conferencing and live video captioning) would give stronger ecological evidence. We hope the present
work stimulates that next wave of research and encourages the HCI community to treat sensitivity for culture-specific
language patterns as a crucial quality criterion for LLM technology.
7
Conclusion
To the best of our knowledge, this study is the first to analyze the cultural sensitivity of LLMs in machine translation
through the lens of cross-cultural pragmatics, combined with evaluations of real users. Using five face-threatening
business emails translated from U.S. English to Japanese, we showed that GPT-4.5 adapts culture-specific language
patterns only minimally under a naïve prompt, but adjusts markedly towards Japanese language patterns when given
a simple audience cue and even more when supplied with explicit guidance. Hence, regular LLM users need to be careful

--- Page 23 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
23
that simple translations through LLM without careful prompting may not reflect the appropriate meaning. In contrast,
Japanese native speakers judged the translations from our cultural-aware prompts as increasingly appropriate and
were more willing to comply with the requests they contained. Against this backdrop, we argue that LLM interfaces
should surface an easy “culture-aware” option while the research community works toward LLMs whose training data
and objectives embed cross-cultural differences in pragmatic norms by default. Addressing that challenge will require
close collaboration between HCI, NLP, and cross-cultural pragmatics to ensure that future language technologies do
more than translate words but that they translate meaning.
Acknowledgments
To Saki Sugimoto, for coding the Japanese translations in Study 1.
References
[1] Icek Ajzen. 1991. The theory of planned behavior. Organizational Behavior and Human Decision Processes 50 (1991), 179–211.
[2] Icek Ajzen. 2019. Theory of planned behavior diagram. https://people.umass.edu/aizen/tpb.diag.html. Accessed: 2025-06-23.
[3] Mahwish Aleem, Imama Zahoor, and Mustafa Naseem. 2024. Towards culturally adaptive large language models in mental health: Using ChatGPT
as a case study. In CSCW.
[4] Badr AlKhamissi, Muhammad ElNokrashy, Mai AlKhamissi, and Mona Diab. 2024. Investigating cultural alignment of large language models. In
ACL.
[5] Taghreed Alshehri, Norah Abokhodair, Reuben Kirkham, and Patrick Olivier. 2021. Qualitative secondary analysis as an alternative approach for
cross-cultural design: A case study with Saudi transnationals. In CHI.
[6] Taghreed Alshehri, Reuben Kirkham, and Patrick Olivier. 2020. Scenario co-creation cards: A culturally sensitive tool for eliciting values. In CHI.
[7] Somnath Banerjee, Sayan Layek, Hari Shrawgi, Rajarshi Mandal, Avik Halder, Shanu Kumar, Sagnik Basu, Parag Agrawal, Rima Hazra, and Animesh
Mukherjee. 2025. Navigating the cultural kaleidoscope: A hitchhiker’s guide to sensitivity in large language models. NAACL-HLT.
[8] Alan Borning and Michael Muller. 2012. Next steps for value sensitive design. In CHI.
[9] Mary Yoko Brannen. 2004. When Mickey loses face: Recontextualization, semantic fit, and the semiotics of foreignness. Academy of Management
Review 29, 4 (2004), 593–616.
[10] Penelope Brown. 1987. Politeness: Some universals in language usage. Cambridge University Press, Cambridge, UK.
[11] Vikram Kamath Cannanure, Dilrukshi Gamage, Christian Sturm, Heike Winschiers-Theophilus, Juan Fernando Maestre, Naveena Karusala, Pedro
Reynolds-Cuéllar, and Neha Kumar. 2021. Decolonizing HCI across borders. In CHI EA.
[12] Yong Cao, Li Zhou, Seolhwa Lee, Laura Cabello, Min Chen, and Daniel Hershcovich. 2023. Assessing cross-cultural alignment between ChatGPT
and human societies: An empirical study. In Proceedings of the First Workshop on Cross-Cultural Considerations in NLP (C3NLP).
[13] Peter Cardon, Carolin Fleischmann, Jolanta Aritz, Minna Logemann, and Jeanette Heidewald. 2023. The challenges and opportunities of AI-assisted
writing: Developing AI literacy for the AI age. Business and Professional Communication Quarterly 86, 3 (2023), 257–295.
[14] Venus Chan and William Ko-Wai Tang. 2024. GPT for translation: A systematic literature review. SN Computer Science 5, 8 (2024), 986.
[15] Yuh-Fang Chang. 2009. How to say no: An analysis of cross-cultural difference and pragmatic transfer. Language Sciences 31, 4 (2009), 477–493.
[16] Stephen Chen, Ronald Geluykens, and Chong Ju Choi. 2006. The importance of language in global teams: A linguistic perspective. Management
International Review 46 (2006), 679–696.
[17] Fiifi Dawson, Zainab Mosunmola, Sahil Pocker, Raj Abhijit Dandekar, Rajat Dandekar, and Sreedath Panat. 2024. Evaluating cultural awareness of
LLMs for Yoruba, Malayalam, and English. arXiv:2410.01811 (2024).
[18] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers for language
understanding. In NAACL-HLT.
[19] Zohreh R Eslami. 2010. Refusals: How to develop appropriate refusal strategies. In Speech act performance: Theoretical, empirical and methodological
issues. John Benjamins Publishing Company, Amsterdam, Netherlands, 217–236.
[20] Stefan Feuerriegel, Jochen Hartmann, Christian Janiesch, and Patrick Zschech. 2024. Generative AI. Business & Information Systems Engineering
66, 1 (2024), 111–126.
[21] Stefan Feuerriegel, Abdurahman Maarouf, Dominik Bär, Dominique Geissler, Jonas Schweisthal, Nicolas Pröllochs, Claire E. Robertson, Steve
Rathje, Jochen Hartmann, Saif M. Mohammad, Oded Netzer, Alexandra A. Siegel, Barbara Plank, and Jay J. Van Bavel. 2025. Using natural language
processing to analyse text data in behavioural science. Nature Reviews Psychology 4, 2 (2025), 96–111.
[22] Martin Fishbein and Icek Ajzen. 2010. Predicting and changing Behavior: The reasoned action approach. Psychology Press, New York, NY.
[23] Internatinal Monetary Fund. 2025. World Economic Outlook Database. https://www.imf.org/en/Publications/WEO/weo-database/2025/April/

--- Page 24 ---

24
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
[24] Yuan Gao, Ruili Wang, and Feng Hou. 2024. How to design translation prompts for ChatGPT: An empirical study. In Proceedings of the ACM
International Conference on Multimedia in Asia Workshops.
[25] Mohammad Ghazanfari, Alireza Bonyadi, and Shirin Malekzadeh. 2013. Investigating cross-linguistic differences in refusal speech act among
native Persian and English speakers. International Journal of Research Studies in Language Learning 2, 4 (2013), 49–63.
[26] Louie Giray. 2023. Prompt Engineering with ChatGPT: A Guide for Academic Writers. Annals of Biomedical Engineering 51, 12 (2023), 2629–2633.
doi:10.1007/s10439-023-03272-4
[27] Wenshi Gu. 2025. Linguistically informed ChatGPT prompts to enhance Japanese-Chinese machine translation: A case study on attributive clauses.
PLOS ONE 20, 1 (2025), e0313264.
[28] Nicola Halenko and Maria Economidou-Kogetsidis. 2022. Japanese learners’spoken requests in the study abroad context: Appropriateness, speech
rate and response time. The Language Learning Journal 50, 4 (2022), 506–520.
[29] Edward T Hall. 1976. Beyond culture. Anchor Books, New York, NY.
[30] Geert Hofstede. 2001. Culture’s consequences: Comparing values, behaviors, institutions and organizations across nations. Sage Publications.
[31] Juliane House and Dániel Z Kádár. 2021. Cross-cultural pragmatics. Cambridge University Press, Cambridge, UK.
[32] Sachiko Ide and Megumi Yoshida. 1999. Sociolinguistics: Honorifics and gender differences. The Handbook of Japanese Linguistics (1999), 444–480.
[33] Hui Jiao, Bei Peng, Lu Zong, Xiaojun Zhang, and Xinwei Li. 2024. Gradable ChatGPT translation evaluation. arXiv:2401.09984 (2024).
[34] Marina Jovic and Salaheddine Mnasri. 2024. Evaluating AI-generated emails: A comparative efficiency analysis. World Journal of English Language
14, 2 (2024).
[35] Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah. 2024. How well do LLMs represent values across cultures? Empirical analysis
of LLM responses based on Hofstede cultural dimensions. arXiv:2406.14805 (2024).
[36] Thomas J Knutson, Rosechongporn Komolsevin, Pat Chatiketu, and Val R Smith. 2003. A cross-cultural comparison of Thai and US American
rhetorical sensitivity: Implications for intercultural communication effectiveness. International Journal of Intercultural Relations 27, 1 (2003), 63–
78.
[37] Grgur Kovač, Masataka Sawayama, Rémy Portelas, Cédric Colas, Peter Ford Dominey, and Pierre-Yves Oudeyer. 2023. Large language models as
superpositions of cultural perspectives. arXiv:2307.07870 (2023).
[38] Hye Eun Lee, Hee Sun Park, Tatsuya Imai, and Daniel Dolan. 2012. Cultural differences between Japan and the United States in uses of “apology”
and “thank you”in favor asking messages. Journal of Language and Social Psychology 31, 3 (2012), 263–289.
[39] Cheng Li, Mengzhuo Chen, Jindong Wang, Sunayana Sitaram, and Xing Xie. 2024. CultureLLM: Incorporating cultural differences into large
language models. NeurIPS (2024).
[40] Cheng Li, Damien Teney, Linyi Yang, Qingsong Wen, Xing Xie, and Jindong Wang. 2024. CulturePark: Boosting cross-cultural understanding in
large language models. In NeurIPS.
[41] Zhicheng Lin. 2024. How to write effective prompts for large language models. Nature Human Behaviour 8, 4 (2024), 611–615. doi:10.1038/s41562-
024-01847-2
[42] Sebastian Linxen, Christian Sturm, Florian Brühlmann, Vincent Cassau, Klaus Opwis, and Katharina Reinecke. 2021. How weird is CHI?. In CHI.
[43] Xiangdong Liu and Todd James Allen. 2014. A study of linguistic politeness in Japanese. Open Journal of Modern Linguistics 4, 5 (2014), 651–663.
[44] William W Maddux, Peter H Kim, Tetsushi Okumura, and Jeanne M Brett. 2011. Cultural differences in the function and meaning of apologies.
International Negotiation 16, 3 (2011), 405–425.
[45] Aaron Marcus and Emilie West Gould. 2000. Crosscurrents: Cultural dimensions and global web user-interface design. Interactions 7, 4 (2000),
32–46.
[46] Reem I Masoud, Ziquan Liu, Martin Ferianc, Philip Treleaven, and Miguel Rodrigues. 2025. Cultural alignment in large language models: An
explanatory analysis based on Hofstede’s cultural dimensions. In COLING.
[47] David A Morand. 2003. Politeness and the clash of interaction orders in cross-cultural communication. Thunderbird International Business Review
45, 5 (2003), 521–540.
[48] Elizabeth Wolfe Morrison, Ya-Ru Chen, and Susan Reilly Salgado. 2004. Cultural differences in newcomer feedback seeking: A comparison of the
United States and Hong Kong. Applied Psychology 53, 1 (2004), 1–22.
[49] Naoki Nomura and Dean Barnlund. 1983. Patterns of interpersonal criticism in Japan and United States. International Journal of Intercultural
Relations 7, 1 (1983), 1–18.
[50] Office of the United States Trade Representative. 2025. Countries & Regions. https://ustr.gov/countries-regions
[51] Shigeko Okamoto. 1998. The use and non-use of honorifics in sales talk in Kyoto and Osaka: Are they rude or friendly. Japanese/Korean Linguistics
7 (1998), 141–157.
[52] Japanese External Trade Organization. 2025. Japanese Trade and Investment Statistics. https://www.jetro.go.jp/en/reports/statistics.html
[53] Sachin R Pendse, Novia Wong, Munmun De Choudhury, Jaydon Farao, Neha Kumar, Nasalifya Namwinga, Giovanni Ramos, Asra Sakeen Wani,
Jessica Lee Schleider, and Madhu Reddy. 2025. Beyond culture: Centering power, reciprocity, and justice in HCI and mental health research. In CHI
EA.
[54] Katharina Reinecke and Abraham Bernstein. 2011.
Improving performance, perceived usability, and aesthetics with culturally adaptive user
interfaces. ACM Transactions on Computer-Human Interaction (TOCHI) 18, 2 (2011), 1–29.
[55] Katharina Reinecke and Krzysztof Z Gajos. 2014. Quantifying visual preferences around the world. In CHI.

--- Page 25 ---

Designing LLMs for cultural sensitivity: Evidence from English-Japanese translation
25
[56] Junko Saito. 2010. Subordinates’use of Japanese plain forms: An examination of superior–subordinate interactions in the workplace. Journal of
Pragmatics 42, 12 (2010), 3271–3282.
[57] Jeffrey Sanchez-Burks, Fiona Lee, Incheol Choi, Richard Nisbett, Shuming Zhao, and Jasook Koo. 2003. Conversing across cultures: East-West
communication styles in work and nonwork contexts. Journal of Personality and Social Psychology 85, 2 (2003), 363–372.
[58] Edward Sapir and David Goodman Mandelbaum. 1957. Edward Sapir: culture, language and personality: selected essays. University of California
Press, Berkeley, CA.
[59] Annika Sabrina Schulz and Eva Hornecker. 2022. Pop-up probes: Using pop-up paper elements for cultural probes to understand domestic routines.
In Proceedings of Mensch und Computer. 447–451.
[60] Pushpdeep Singh, Mayur Patidar, and Lovekesh Vig. 2025. Translating across cultures: LLMs for intralingual cultural adaptation. In CoNLL.
[61] Naoko Taguchi. 2011. Do proficiency and study-abroad experience affect speech act production? Analysis of appropriateness, accuracy and fluency.
International Review of Applied Linguistics in Language Teaching 49, 4 (2011), 265–293.
[62] Yan Tao, Olga Viberg, Ryan S Baker, and René F Kizilcec. 2024. Cultural bias and cultural alignment of large language models. PNAS Nexus 3, 9
(2024), pgae346.
[63] Simone Tedeschi, Johan Bos, Thierry Declerck, Jan Hajic, Daniel Hershcovich, Eduard H Hovy, Alexander Koller, Simon Krek, Steven Schockaert,
Rico Sennrich, et al. 2023. What’s the meaning of superhuman performance in today’s NLU?. In ACL.
[64] Helene Tenzer, Stefan Feuerriegel, and Rebecca Piekkari. 2024. AI machine translation tools must be taught cultural differences too. Nature 630,
8018 (2024), 820–820.
[65] Noam Tractinsky. 1997. Aesthetics and apparent usability: empirically assessing cultural and methodological issues. In CHI.
[66] Aynura Valiyeva and Basil John Thomas. 2022. Successful organizational business communication and its impact on business performance: An
intra-and inter-organizational perspective. Journal of Accounting, Business and Finance Research 15, 2 (2022), 83–91.
[67] Anna Wierzbicka. 2003. Cross-cultural pragmatics: The semantics of human interaction. Mouton de Gruyter, Berlin, Germany.
[68] Charles Woodrum. 2024. ChatGPT and language translation: A small case study evaluating English–Mandarin translation. In International Confer-
ence on Human-Computer Interaction.

--- Page 26 ---

26
Helene Tenzer, Oumnia Abidi, and Stefan Feuerriegel
A
Appendix: Full List of Survey Items
Japanese items
English items
このメールは、状況に応じた礼儀正しさのレベ
ルが適切で効果的であるため、満足を感じます
か。
I would feel satisfied with this email because the level
of politeness is appropriate and effective for the situ-
ation.
このメールは、状況に応じた直接性のレベルが
適切で効果的であるため、満足を感じますか。
I would feel satisfied with this email because the level
of directness is appropriate and effective for the situ-
ation.
このメールは、状況に応じた形式性のレベルが
適切で効果的であるため、満足を感じますか。
I would feel satisfied with this email because the level
of formality is appropriate and effective for the situa-
tion.
Table 4. Perceived appropriateness (7‐point Likert scale: 1 = strongly disagree, 7 = strongly agree).
Japanese items
English items
私は、このメールの内容に従うつもりです。
I intend to comply with the content of this email.
可能であれば、このメールの提案に従いたいと
思います。
I am willing to follow the suggestion in this email if
possible.
状況が許せば、このメールに従って行動します。If circumstances allow, I will act in accordance with
this email.
十分な理由がない限り、送り手のメッセージに
対応しようとします。
I would try to accommodate the sender’s message un-
less I have a strong reason not to.
今後、同様のメッセージを受け取った場合、好
意的に対応する可能性が高いです。
If I received a similar message in the future, I would
respond favorably.
Table 5. Intent to comply with the email request (7‐point scale: 1 = strongly disagree, 7 = strongly agree).

```
