---
title: "2024-Onose-Can LLMs Help Create Grammar Automating Grammar Creation for - PDF Extract"
source_pdf: "2024-Onose-Can LLMs Help Create Grammar Automating Grammar Creation for.pdf"
pages: 10
extracted_at: "2026-02-13T13:57:11.856723"
---

# PDF Extract: 2024-Onose-Can LLMs Help Create Grammar Automating Grammar Creation for

**Source PDF:** 2024-Onose-Can LLMs Help Create Grammar Automating Grammar Creation for.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Can LLMs Help Create Grammar?: Automating Grammar Creation for
Endangered Languages with In-Context Learning
Piyapath T Spencer1,2 and Nanthipat Kongborrirak1
1Language and Information Technology Programme, Faculty of Arts, CU, Thailand
2Center for Information and Language Processing (CIS), LMU Munich, Germany
linguistics@piyapath.uk
prompt.k10@gmail.com
Abstract
Yes! In the present-day documenting and pre-
serving endangered languages, the application
of Large Language Models (LLMs) presents a
promising approach. This paper explores how
LLMs, particularly through in-context learning,
can assist in generating grammatical informa-
tion for low-resource languages with limited
amount of data. We takes Moklen as a case
study to evaluate the efficacy of LLMs in pro-
ducing coherent grammatical rules and lexical
entries using only bilingual dictionaries and
parallel sentences of the unknown language
without building the model from scratch. Our
methodology involves organising the existing
linguistic data and prompting to efficiently en-
able to generate formal XLE grammar. Our
results demonstrate that LLMs can successfully
capture key grammatical structures and lexi-
cal information, although challenges such as
the potential for English grammatical biases
remain. This study highlights the potential of
LLMs to enhance language documentation ef-
forts, providing a cost-effective solution for
generating linguistic data and contributing to
the preservation of endangered languages.
1
Introduction
In linguisitics, the quest for universality (Chomsky
and Berwick, 2016), despite its criticism, motivates
the comparison of languages to identify common
patterns and structures. Many linguists investigate
how different languages handle concepts like tense,
number, or syntactic structure to identify universal
features or constraints.
Within
this
broader
discourse,
Lexical-
Functional Grammar (LFG) offers a model
for understanding the complexities of different
information within and across languages. In its
different structures, it assumes both variability
and universality. For instance, the analysis of a
language with a free word order sequence is valid
within the LFG framework (Simpson, 1991).
 
  
    
  
  
 
    
    
   
      
   
 
  
    
   
  
   
   
   
   
  
 
    
    
  
[
 
 
 
 
 
 
 PRED         
ʻlove〈she, I〉ʼ           
 SUBJ         
 [PRED
ʻsheʼ
case
   NOM]        
 OBJ             
[PRED
ʻIʼ  
case 
ACC]          
ADJUNCT  
{[PRED
ʻNEGʼ]}    
TNS-ASP   
[mood
indicative
tense 
past          ]]
 
 
 
 
 
 
 
 
Figure 1: The ϕ mapping (Dalrymple, 2023) from dif-
ferent c(onstituent)-structures of Moklen and English to
the same f(unctional)-structure
According to Butt et al. (1999), "a common set
of linguistic principles and a commonly agreed
upon set of grammatical analyses and features"
unify linguistic insights across languages whilst ac-
knowledge the uniqueness of individual languages.
The XLE (Xerox Linguistic Environment), de-
veloped on the basis of LFG (Maxwell and Ka-
plan; Crouch et al., 2011), serves as a powerful tool
for the computational implementation of multilin-
gual grammars (grammars across a wide range of
languages). However, the ’grammars’ are usually
manually constructed since it requires the under-
standing of nuances within a language, which is ex-
pensive and time-consuming to produce. This fact
makes it difficult to start developing deep grammar
for low-resource languages, especially endangered
languages.
The recent development of large language mod-
els (LLM) has shown notable capabilities for ’adap-
tation’ (Brown et al., 2020; Wei et al., 2022) to
various tasks and understanding natural language
instructions through in-context learning and un-
derstanding natural language instructions with in-
context learning (Brown et al., 2020; OpenAI,
2024; Team, 2024). Their linguistic performances
1
arXiv:2412.10960v1  [cs.CL]  14 Dec 2024

--- Page 2 ---

and metalinguistic abilities have also been recog-
nised (Beguš et al., 2023). This presents an op-
portunity to use their capabilities in generating
grammar and linguistic information for endangered
languages, potentially overcoming the need for ex-
haustive resources and the limitations of manual
grammar construction.
This paper proposes a novel approach that ex-
ploits LLMs’ linguistic competences in English lan-
guage to generate such coherent formal language as
XLE grammar for natural languages that have not
been encountered during the model’s pre-training.
This approach relies solely on bilingual dictionaries
and few pairs of parallel sentences, which reflect
the amount of data linguists typically has at hand
during the process of documenting endangered lan-
guages (Spencer, 2024).
2
Background and Related Work
Despite the significant advancements, most exist-
ing studies focus on high-resource languages, with
limited exploration of how LLMs can be effectively
applied to lower-resource or truly low-resource lan-
guages. This gap is particularly concerning given
the vast number of languages spoken worldwide,
many of which lack sufficient digital representation
and the risk of extinction.
On Large Multilingual Grammar Development
Large multilingual grammar development has seen
significant advancements through theoretical gram-
mar models such as Head-Driven Phrase Structure
Grammar (HPSG) and Lexical-Functional Gram-
mar (LFG). Such projects include LinGO (Oepen
et al., 2002), Matrix (Zamaraeva et al., 2022), and
DELPH-IN (Copestake, 2002) for HPSG, and the
ParGram project (Butt et al., 2002) for LFG. These
frameworks often rely on rule-based systems to
capture the syntactic and semantic nuances of mul-
tiple languages.
Their common objective is to
create comprehensive grammatical analyses that
can be applied across diverse linguistic contexts.
However, the manual construction of these gram-
mars demands extensive linguistic expertise and
resources, which can be considered as a barrier for
low-resource languages.
On ’Low-Resource’
In the fields of artificial intelligence (AI), natural
language processing (NLP), and LLMs, the term
"low-resource" is surprisingly is a broad. This clas-
sification even includes languages like German, Fil-
ipino, and some institutional languages that have
their own pretrained models, machine translation
(MT) systems, and various NLP applications. This
disparity arises from the uneven distribution of lin-
guistic resources, with only 14 languages compris-
ing over 90% of internet content, and English alone
accounting for half of all data (W3Techs). In con-
trast, there are over 7,000 known languages, with
approximately half classified as endangered accord-
ing to Ethnologue. Many of these endangered lan-
guages are likely to disappear by the end of this
century.
When considering endangered languages along-
side the NLP concept of low-resource languages,
it becomes evident that many of these languages
even lacks native speakers in their own society, not
to mentioned its minimal or no digital presence.
Often, they are primarily spoken languages without
a writing system, meaning there may be no written
documentation or corpus available. Despite these
challenges, linguists have made efforts to document
these sorts of languages by, firstly, collecting vo-
cabulary, creating grammar books and dictionaries
to preserve their existence of language in the world.
On Competence and Performance
Psycholinguistically, a distinction exists between
linguistic competence and performance (Pritchett,
1992). Competence refers to the innate ability to
control all aspects of a language’s structure, rang-
ing from the intricate array of grammatical rules
to pragmatic nuances of usage. Performance, on
the other hand, pertains to the actual production of
language in real-world contexts. This distinction
differentiates a critical difference between human
linguistic abilities and those of AI, as LLMs pos-
sess extensive knowledge of a language due to their
rigorous pretraining on large datasets.
When discussing generative AI, the focus is of-
ten on how language is created or generated, as
suggested by the term itself. Generative AI, in-
cluding LLMs, thus simulates human linguistic
performance (Miranda-Saavedra, 2024). In the
context of linguistics, this raises questions about
how language is produced and understood. Over
time, benchmarks for LLMs have shown saturation,
indicating that models are becoming increasingly
powerful and capable of performing complex tasks,
as exemplified by models like GPT-4. This leads
to comparisons between AI capabilities and hu-
man language abilities, prompting inquiries into
whether LLMs truly understand language.
Generally, the performance of LLMs is largely
determined by both quality and, but much more
2

--- Page 3 ---

important, quantity of the data on which they are
trained. Whilst LLMs may demonstrate impressive
capabilities across various languages, this does not
necessarily guarantee a true understanding of those
languages. This distinction is particularly evident
in the case of English, where LLMs benefit from
extensive training on vast and diverse datasets. As
a result, their performance in English is often more
robust and nuanced compared to their performance
in lower-resource languages, which may not have
the same level of data availability and linguistic
representation.
On In-Context Learning
Recent advancements in LLMs have improved their
performance not by training from scratch or re-
quiring extensive datasets, but through prompt en-
gineering that enables in-context learning. This
approach allows models to adopt information pre-
sented within the context of specific inputs to gen-
erate relevant and coherent responses. Various
techniques, such as zero-shot, few-shot, and chain-
of-thought prompting, have emerged as effective
strategies for enhancing LLM capabilities.
In the context of low-resource languages, in-
context learning has been employed to refine LLM
performance, particularly in machine translation.
For instance, Tanzer et al. (2024) utilised dictio-
naries and grammar books to translate endangered
languages with LLMs, establishing benchmarks for
evaluation. Zhang et al. (2024), whose work this
paper aims to build upon, extended this approach
to cover multiple NLP tasks, evaluating their LIN-
GOLLM methodology across different endangered
languages. In contrast to these studies, we seek to
advance the application of LLMs in a more radi-
cal linguistic task: analysing the grammar of lan-
guages under extremely limited conditions where
prior data is not applicable.
3
Language under Study: Moklen
Language
Moklen (ISO 639-3: mkm) is an endangered lan-
guage estimated to be spoken by fewer than 1,000
people, which constitutes only one-fourth of the to-
tal population, most of whom are over 50 years
old.
The speakers are predominantly scattered
across Phang Nga and Phuket in Southern Thai-
land. Moklen has been influenced by Malay and
Thai, the latter being the national language of Thai-
land. It is classified as one of the Austronesian
languages.
Despite attempts by the community to use the
Thai alphabet to record and teach Moklen to chil-
dren, the language remains primarily oral, with no
formal written tradition or administrative use. Con-
sequently, there is little to no evidence of the lan-
guage being used on the internet. Moklen is anal-
ysed to have a subject-verb-object (SVO) word or-
der and a nominative-accusative alignment. While
this word order is prominent, Moklen also features
topicalisation to emphasise certain parts of an ut-
terance. Additionally, it lacks inflectional morphol-
ogy, meaning that words can be combined in vari-
ous ways to convey meaning. Grammatical features
such as tense, aspect, and number are expressed
through content words.
Thorough documentation of the language began
in late 2017, leading to the development of a pilot
version of a dictionary (Pittayaporn et al., 2022),
following the establishment of a Thai-based or-
thography system (Pittayaporn and Choemprayong,
Forthcoming). Nevertheless, there are only a few
samples of Moklen sentences, primarily derived
from field notes, and limited work has been done
on the language.
Considering all these aspects, Moklen is well-
suited for the current study. Firstly, it meets the
requirements of the paper’s approach, which neces-
sitates bitext and a dictionary with the source lan-
guage (Moklen) and the target language (English).
Secondly, the dictionary is relatively comprehen-
sive, containing words that can be used to express
a wide range of concepts. Finally, the isolating
nature of Moklen syntax allows for the application
of LLMs without the complications of inflectional
morphology and complex tokenisation.
4
Methodology
Our methodology reflects the approach linguists
take when analysing grammar and the cognitive
aspects of human language. The process comprises
five major steps, as shown in Figure 2:
(1) Given the bitext, a dictionary-based tokeniser
is used to segment the Moklen text into individual
words.
(2) For every word in a sentence, we search for
the closest match from the dictionary to map the
English meaning to the corresponding words in the
source language.
(3) We concatenate the meanings of each word in
each sentence and pair them side-by-side with the
original sentences.
3

--- Page 4 ---

Figure 2: The approach requires each pair of sentences from bitext going through the process of tokenisation, sense
mapping, and sentence concatenation prior to include into the prompt to do the task
(4) We prompt a large language model (LLM) with
the mapped, tokenised bitext and materials related
to creating grammar in XLE format.
(5) We then use the generated grammar rules to
guide the LLM in generating lexical entries based
on the words from the dictionary.
The primary data sources for this study include
bilingual dictionaries and parallel sentences that
pair Moklen with English. The dictionary in this pa-
per developed from (Pittayaporn et al., 2022) serves
as a foundational resource, containing approxi-
mately 1,000 basic vocabulary items in Moklen
along with their English translations. Additionally,
a collection of parallel sentences, derived from field
notes and existing documentation, will be used to
provide contextual examples of grammatical struc-
tures in both languages.
4.1
Tokenisation
In this step, we create a dictionary-based tokeniser
to segment the Moklen text into individual words.
This approach is feasible since all words in the
Moklen sentences from the bitext exist in the dictio-
nary. However, tokenising Moklen presents unique
challenges due to its high frequency of compound
words. To address this, a longest-match strategy
is employed where the tokeniser first looks for
the closest and largest item in the dictionary be-
fore considering smaller units. This prevents over-
tokenisation and ensures that the true meaning of
each sentence is accurately represented.
For example, the Moklen word maklaw, meaning
’to speak’, is a compound form derived from the
root word klaw. If tokenised incorrectly, it could
be split into two different words: ma (meaning
’horse’) and klaw (meaning ’to speak’). This mis-
interpretation could lead to a sentence being incor-
rectly understood as "The horse is speaking." Ac-
cordingly, the tokeniser will recognise maklaw as a
single unit, thereby preserving the correct meaning
and enhancing the overall accuracy of the analysis.
4.2
Sense Mapping
Once the text is tokenised, we perform sense map-
ping by searching for the corresponding meaning
of each token in the Moklen sentences. This step is
crucial for ensuring that the LLM does not attempt
to match each token independently, which often
results in inaccuracies. Instead, we aim to provide
the LLM with contextually relevant mappings.
Each word in Moklen may have multiple mean-
ings, and it is essential for the LLM to select the
appropriate meaning based on the context provided.
This process assumes that the LLM can consider
the various meanings of words and choose the one
that best fits the context of the sentence. For in-
stance, in the sentence tichum boh pong, which
translates to ’The bird is building the nest’, the
word pong has two different senses: ’nest’ and ’fa-
ther’. The LLM should correctly interpret the sen-
tence as ’The bird is building the nest’ rather than
’The bird is building/making the father’, demon-
strating its ability to disambiguate based on con-
text.
4

--- Page 5 ---

4.3
Generation of Grammar
After mapping the meanings, we concatenate the
meanings of each word and prepare the data for
input into the LLM. The underlying idea is that
even though the LLM may have no prior knowl-
edge of Moklen, it can employ its logical reasoning
capabilities to analyse the provided data. By com-
paring the shared structures of Moklen and English,
the LLM can induce grammatical rules from the
context and information given.
For the model generation, there are two ap-
proaches to creating the grammar of Moklen. The
first approach involves describing the language us-
ing natural language, detailing information such as
word order, grammatical features, and functions.
The second approach is to generate the grammar
in a formal language, specifically XLE, by creat-
ing rules and lexical entries using a specific tem-
plate and syntax1. Whilst we favour the second
approach as the end product of this paper, the natu-
ral language description can be a good indicator to
understand how the LLM interprets and analyses
the language data.
5
Experiment
5.1
Experimental Setup
We ran all experiments on OpenAI’s API-based
model gpt-4o-mini-2024-07-18 and keep a
rather low temperature at 0.1 across tasks. The
benchmark data, code, and model generations can
be found in the supplementary material.
Despite being a single task, we also perform the
task under different experimental settings, varying
the kind of retrieved context that are provided in
the prompt. See ?? for full details. The types of
context include:
No context (-): Apart from Moklen sentences, the
model is told only that Moklen is a language spoken
around Southern Thailand and given no reference
material. This measures the base model’s zero-shot
capabilities and validates that they have effectively
learned zero Moklen during pretraining.
Bitext Context (B): For each sentence, we provide
an English translation into the prompt.
Tokenised Context (T): We experiment with two
different ways. First, for each sentence, we provide
tokens (T 0). Second, for each word in each Moklen
sentence, we map them with the English definition
1Henceforth, grammar refers to formal rules and lexical
entries in XLE.
no matter how many senses they are into the prompt
(T D).
Concatenated Sentence Context (C): For each
sentence, we take the translation of each word to
concatenate as one string, though they may be non-
sensical or ungrammatical (since we need the incor-
rect ones on purpose!). It is assumed that this type
of string will reflect how word order in Moklen
works as opposed to English.
Example Context (E): The model is provided with
an example of how the English language is imple-
mented with XLE.
Self-Explanation Context (S): Prior to the genera-
tion, the model is given the relevant data to analyse
and describe in natural language, and take it as a
guideline when generating the grammar.
For all contexts,
the model is retrieval-
augmented by providing with the XLE documenta-
tion that describes how to create a grammar and a
Moklen dictionary except for no context condition,
storing in a separate datastore (Asai et al., 2024).
5.2
Evaluation Measures
Evaluating the quality of generated grammars is
inherently an complex task, as there is no single
correct approach to grammar construction. Conse-
quently, the evaluation must consider both quanti-
tative and qualitative aspects of the model’s perfor-
mance and the output.
Translation. We follow Tanzer et al. (2024) and
Zhang et al. (2024) in that translation performance
is used as an indirect indicator of the model’s un-
derstanding of linguistic structures, albeit not ex-
plicitly. Thus, this task is the starting point to se-
lecting the best combination of contexts to proceed
to the more sophisticated step. We will evaluate the
model’s performance on Moklen-to-English trans-
lation tasks, using an additional set of 40 parallel
sentences. The quality of translations will be as-
sessed using several metrics including a traditional
BLEU (Papineni et al., 2002), ROUGE (Ganesan,
2018), METEOR (Banerjee and Lavie, 2005), chrF
(Popovi´c, 2015), and BERTScore (Zhang et al.,
2020). This very task will serve as an experimental
ablation to determine the most effective context
settings for further steps. Apart from this, English-
to-Moklen translation will be conducted both be-
fore and after generating the grammar to determine
the impact of the generated grammar on translation
performance.
Grammar Rule Accuracy.
Never before had
Moklen been developed its grammar using XLE.
5

--- Page 6 ---

Hence, there is no XLE grammar for Moklen; we
attempt to create one based on Spencer (2022)
and served as a gold standard. The model will
be prompted to generate the generated grammar
rules which will be qualitatively evaluated. Ide-
ally, the rules must demonstrate the capacity to
accurately model all possible sentence structures in
Moklen, including the full range of parts-of-speech
categories. Specifically, the grammar should cover
syntactic constructions, word order, and morpho-
logical agreement, ensuring that all core grammati-
cal elements of Moklen are represented.
Lexical Entry and Schemata Accuracy.
The
model will generate lexical entries for 100 words
from the Moklen dictionary that do not appear in
the bitext, primarily based on the grammar rules
produced by the model and the information pro-
vided in the dictionary. For each lexical entry, there
are differences between how different element dif-
ferently exhibits their functional schemata. This
accuracy is also assumed to be resulted by the ac-
curacy of the grammar rules, as well as the under-
standing of both grammar of the language and XLE
architecture. We will manually assess the accuracy
of these lexical entries by comparing them to ex-
isting dictionary definitions and evaluating their
coherence across the generation. we will consider
the completeness of the entries, examining whether
the model captures various meanings and usages of
each word. Ultimately, these lexical entries will be
integrated into the XLE system.
6
Results
6.1
Translation
Ablation.
We explored 48 possible context
combinations (see ??) and identified 10 partic-
ularly noteworthy ones based on representative-
ness, not necessarily the best performance. These
combinations are:
-, B, T0, B+T0+S, B+TD,
B+TD+C, TD+C+S, B+TD+C+E, TD+C+E+S,
and B+TD+C+E+S. Further translation tasks were
conducted on these combinations.
Surprisingly, the combination with all contexts
did not yield the best performance. Instead, the
TD context alone achieved the highest score, with
a BERTScore F1 of 0.4904, only slightly better
than the second-best. This suggests that TD is
more effective when combined with other contexts,
outperforming T0 in all scenarios. The impact of
contexts E and S is relatively equal when combined
with other contexts.
-(with dictionary)
T
B
T +B
T +B
T +B+C
T +C+S
T +B+C+E
T +C+E+S
T +B+C+E+S
Conditions
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
BERTScore (F1)
Before
After
Figure 3: When instructing with grammar, the model
performs better across various combinations of context
English-to-Moklen with Grammar. When incor-
porating the XLE gold standard grammar into the
prompt across all models, we observed an overall
improvement in translation performance. This sug-
gests that the inclusion of grammar plays a crucial
role in enhancing model output quality.
This finding is consistent with our previous ob-
servations. Specifically, the context combination
TD+C+S emerged as the most effective, achieving
the highest score in nearly all benchmarks with
an estimated BERTScore F1 of 0.7110. This result
highlights that certain combinations of contexts can
significantly enhance translation accuracy.
English-to-Moklen with Grammar. Interestingly,
translating from Moklen to English demonstrated
better performance compared to the reverse trans-
lation (English-to-Moklen). This suggests that the
model’s ability to generate English sentences from
Moklen inputs is more refined or effective than
generating Moklen sentences from English. The
implication behind this will be discussed later in
the next section.
T
B
T +B
T +B
T +B+C
T +C+S
T +B+C+E
T +C+E+S
T +B+C+E+S
Conditions
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
BERTScore (F1)
Moklen to English
English to Moklen
Figure 4: The improvement in scores across contexts
leading to the suspicion of the reliability of the metric
6

--- Page 7 ---

6.2
Grammar Rules: Accuracy and
Completeness
To assess the completeness of the grammar rules,
we evaluated whether they could accurately capture
all parts of speech in Moklen without overly relying
on English examples.
Using the context TD+C+S, the model effec-
tively identified common parts of speech such as
nouns, verbs, adjectives, and adverbs. However,
some unique English parts of speech, particularly
determiners, were incorrectly applied to Moklen
grammar. Despite this, the XLE implementation
accurately captures most grammatical structures
in the language. This discrepancy raises questions
that will be explored in the following discussion.
6.3
Lexical Entries: Accuracy and Coherence
We generated lexical entries for 100 Moklen words
not present in the bitext and assessed their accuracy
by comparing them to existing dictionary defini-
tions. Out of these, 86 entries were deemed ac-
curate and coherent. However, some incomplete
lexical entries captured only the more prominent
senses of words. For example, the word data was
defined as a preposition meaning ‘on’ and a noun
meaning ‘the top’, but the latter sense was not cap-
tured by the model.
7
Analysis & Discussion
There are several critical aspects emerging from the
experimental results worth for further discussion.
Dictionary Integration. The inclusion of a dic-
tionary in the prompt significantly impacts model
performance, even without further contextual mod-
ifications. This simple integration yields results
that are comparable to or better than combining the
dictionary with other contexts. Specifically, the dic-
tionary enhances the model’s lexical understanding
by grounding it in a structured reference, which is
essential when working with languages with mini-
mal resources. For Moklen, a language that lacks
morphological inflections and instead uses con-
tent words to express grammatical relations (e.g.,
tense or aspect), dictionary-based lexical grounding
proves effective. The performance improvements
can be seen in the BERTscores, where the model
achieved translation quality approaching that of
more morphologically complex languages, despite
Moklen’s isolating structure. This supports the idea
that even minimal data, when correctly utilised, can
provide significant gains in language processing
tasks.
Without Dictionary
With Dictionary
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
BERTScore (F1)
Figure 5: The clear improvement after intergrating dic-
tionary into the prompt in Moklen-to-English translation
tasks
Evaluation of Translation Metrics. A key chal-
lenge with existing translation metrics like BLEU,
ROUGE-L, METEOR, and chrF is their heavy
reliance on word forms and syntactic similarity,
which aligns poorly with Moklen’s structural char-
acteristics. For instance, these metrics work effec-
tively in English, where grammatical markers such
as tense are explicitly coded into verb forms. How-
ever, Moklen’s lack of grammatical tense markers
presents a problem, as a single word can express
multiple temporal aspects. This reduces the valid-
ity of word-form-based metrics for this language,
leading to discrepancies between numerical scores
and actual translation quality. As an alternative,
BERTScore, which prioritizes semantic similarity
over word forms, emerges as a better choice for
evaluating translations of languages like Moklen.
However, even BERTScore falls short in fully cap-
turing the subtleties of Moklen’s grammar. To ad-
dress this, future work should explore the devel-
opment of a new evaluation metric tailored to lan-
guages with similar grammatical features, focusing
on meaning representation rather than form.
Model Size Considerations. One critical design
decision in this study was the intentional use of a
small model. The choice to work with a smaller
model was made to demonstrate the potential for
generating usable grammar and lexical information
with limited computational resources. The success
of the small model implies that larger models could
yield even better performance, especially in cap-
turing more subtle linguistic nuances or handling
rare linguistic phenomena. Given the scalability of
LLMs, this opens a pathway for applying similar
7

--- Page 8 ---

methods to larger models for endangered languages
with more complex syntactic structures or larger
datasets.
Hallucinations and Model Inaccuracies. In low-
resource settings, model hallucinations, particu-
larly in zero-shot translation tasks, were evident.
Hallucinations primarily arose when the model was
forced to translate or generate sentences with little
or no exposure to similar data during training. This
was especially pronounced with Moklen, where the
use of the Thai script caused confusion. Due to
overlap in the lexicons of Thai and Moklen, the
model occasionally produced hybridized transla-
tions, mistaking Thai words for Moklen ones. Al-
though these inaccuracies were rare, they under-
score the importance of refining training data and
prompt construction to mitigate such issues. Mov-
ing forward, the inclusion of more diverse Moklen
data or deliberate disambiguation in the training
process may reduce hallucinations and improve
model robustness.
However, while these deviations can be prob-
lematic, they can also offer unexpected insights
for linguists. In some cases, the model’s introduc-
tion of ’non-Moklen’ parts of speech or grammar
elements not traditionally associated with the lan-
guage might suggest an overlooked pattern or nu-
ance. These hallucinations, though initially appear-
ing as errors, can prompt linguists to reconsider
their assumptions and explore whether the model
has captured subtle relationships or features that
were not immediately apparent from a human per-
spective. For instance, the model’s introduction
of categories that do not exist formally in Moklen
may highlight potential areas of linguistic overlap
or underlying structures that deserve further inves-
tigation. This kind of speculative output, while
not always accurate, provides a thought-provoking
dimension to the analysis, encouraging a holistic
re-examination of linguistic data.
Potential for XLE Parsing and Beyond. this ap-
proach should not be overlooked. XLE’s highly
sophisticated nature for parsing natural language
makes it an ideal framework for documenting en-
dangered languages. However, given the success
of this methodology, it is reasonable to assume
that the generated grammar could be adapted to
other formal frameworks, such as HPSG or de-
pendency grammars, making it widely applicable
across different linguistic projects. This flexibility
suggests that LLMs, when properly guided, can not
only assist in XLE parsing but also contribute to
the broader field of computational linguistics by
providing insights into the underlying structure of
under-documented languages.
8
Conclusion
It is evident that an LLM, if sufficient informa-
tion is provided, can assist linguists in generating
linguistic data for such complex and, moreover, te-
dious tasks. This methodology with careful prompt-
ing techniques offers a cost- and time-effective
means of obtaining grammatical information for
the endangered Moklen language by means of min-
imal linguistic resources and analogy from English
language. By using as less as only bilingual dic-
tionaries and in-context learning, we successfully
extracted coherent grammatical rules and lexical
entries, thereby contributing to the documentation
and preservation of Moklen or, at least, isolating
languages in general.
Limitation
While this study demonstrates promising results,
it is important to acknowledge the limitations of
this study. We experimented with only a single
language, Moklen, which is an isolating language
without grammatical inflections. This typological
characteristic may have made it easier for the LLM
to decipher the language from a negligible amount
of information compared to other languages in the
world. We plan to extend this methodology to in-
clusively experiment with various languages from
different typologies and morphologies to assess
its broader applicability. Additionally, the poten-
tial for English grammatical biases in the model’s
outputs suggests that further research is needed to
develop techniques for minimising cross-linguistic
interference in low-resource language modelling.
References
Akari Asai, Zexuan Zhong, Danqi Chen, Pang Wei
Koh, Luke Zettlemoyer, Hannaneh Hajishirzi, and
Wen tau Yih. 2024.
Reliable, adaptable, and at-
tributable language models with retrieval. Preprint,
arXiv:2403.03187.
Satanjeev Banerjee and Alon Lavie. 2005.
ME-
TEOR: An automatic metric for MT evaluation
with improved correlation with human judgments.
In Proceedings of the ACL Workshop on Intrinsic
and Extrinsic Evaluation Measures for Machine
Translation and/or Summarization, pages 65–72,
Ann Arbor, Michigan. Association for Computational
Linguistics.
8

--- Page 9 ---

Gašper Beguš, Maksymilian D ˛abkowski, and Ryan
Rhodes. 2023.
Large linguistic models: Analyz-
ing theoretical linguistic abilities of llms. Preprint,
arXiv:2305.00948.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen,
Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin
Chess, Jack Clark, Christopher Berner, Sam Mc-
Candlish, Alec Radford, Ilya Sutskever, and Dario
Amodei. 2020. Language models are few-shot learn-
ers. Preprint, arXiv:2005.14165.
Miriam Butt, Helge Dyvik, Tracy Holloway King, Hi-
roshi Masuichi, and Christian Rohrer. 2002. The
parallel grammar project. In COLING-02: Grammar
Engineering and Evaluation.
Miriam Butt, Tracy Holloway King, Maria-Eugenia
Niño, and Frederique Segond. 1999. A Grammar
Writer’s Cookbook. Stanford University Press.
Noam Chomsky and Robert Berwick. 2016. Why Only
Us. MIT Press.
Ann Copestake. 2002. Definitions of typed feature struc-
tures. In Stephan Oepen, Dan Flickinger, Jun-ichi
Tsujii, and Hans Uszkoreit, editors, Collaborative
Language Engineering, pages 227–230. CSLI Publi-
cations, Stanford, CA.
Richard Crouch, Mary Dalrymple, Ronald M. Kaplan,
Tracy Holloway King, John T. III Maxwell, and
Paula S. Newman. 2011. XLE Documentation.
Mary Dalrymple, editor. 2023. Handbook of Lexical
Functional Grammar. Number 13 in Empirically Ori-
ented Theoretical Morphology and Syntax. Language
Science Press, Berlin.
Ethnologue. 2024. How many languages are endan-
gered?
Kavita Ganesan. 2018. Rouge 2.0: Updated and im-
proved measures for evaluation of summarization
tasks. Preprint, arXiv:1803.01937.
John T. Maxwell, III and Ronald M. Kaplan. The in-
terface between phrasal and functional constraints.
Computational Linguistics.
Diego Miranda-Saavedra. 2024. Generative ai models
and the quest for human-level artificial intelligence.
Real World Data Science.
Stephan Oepen, Kristina Toutanova, Stuart Shieber,
Christopher Manning, Dan Flickinger, and Thorsten
Brants. 2002.
The LinGO redwoods treebank:
Motivation and preliminary applications.
In
COLING 2002: The 17th International Conference
on Computational Linguistics: Project Notes.
OpenAI. 2024.
Gpt-4 technical report.
Preprint,
arXiv:2303.08774.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002.
Bleu: a method for automatic
evaluation of machine translation. In Proceedings
of the 40th Annual Meeting of the Association for
Computational Linguistics, pages 311–318, Philadel-
phia, Pennsylvania, USA. Association for Computa-
tional Linguistics.
Pittayawat Pittayaporn and Songphan Choempray-
ong. Forthcoming.
A proposal for a thai-based
moklen orthography. Language Documentation and
Conservation.
Pittayawat Pittayaporn, Warunsiri Pornpottanamas,
Daniel Loss, Songphan Choemprayong, Chengnan
Zhang, Piyangkoon Thaweepol, Pongporn Pray-
ongsap, Pornsuda Nawarak, Peerasak Sirisawasdi,
and Leena Maluleem. 2022. Moklen-Thai-English
Dictionary: A Pilot Version.
Maja Popovi´c. 2015. chrF: character n-gram F-score
for automatic MT evaluation. In Proceedings of the
Tenth Workshop on Statistical Machine Translation,
pages 392–395, Lisbon, Portugal. Association for
Computational Linguistics.
Bradley L. Pritchett. 1992. Grammatical Competence
and Parsing Performance. The University of Chicago
Press.
Jane Simpson. 1991.
Warlpiri Morpho-Syntax: A
Lexicalist Approach. Kluwer Academic Publisher.
Piyapath Spencer. 2024. Documenting endangered lan-
guages with LangDoc: A wordlist-based system and
a case study on Moklen. In Proceedings of the 3rd
Workshop on NLP Applications to Field Linguistics
(Field Matters 2024), pages 28–36, Bangkok, Thai-
land. Association for Computational Linguistics.
Piyapath T Spencer. 2022.
Grammatical sketch of
moklen verb phrase. Unpublished Manuscipt.
Garrett Tanzer, Mirac Suzgun, Eline Visser, Dan Juraf-
sky, and Luke Melas-Kyriazi. 2024. A benchmark
for learning to translate a new language from one
grammar book.
Gemini Team. 2024. Gemini 1.5: Unlocking multi-
modal understanding across millions of tokens of
context. Preprint, arXiv:2403.05530.
W3Techs. 2024. Usage statistics of content languages
for websites.
Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin
Guu, Adams Wei Yu, Brian Lester, Nan Du, An-
drew M. Dai, and Quoc V. Le. 2022.
Finetuned
language models are zero-shot learners. Preprint,
arXiv:2109.01652.
9

--- Page 10 ---

Olga Zamaraeva, Chris Curtis, Guy Emerson, Antske
Fokkens, Michael Goodman, Kristen Howell, T.J.
Trimble, and Emily M. Bender. 2022. 20 years of
the grammar matrix: cross-linguistic hypothesis test-
ing of increasingly complex interactions. Journal of
Language Modelling, 10(1):49–137.
Kexun Zhang, Yee Choi, Zhenqiao Song, Taiqi He,
William Yang Wang, and Lei Li. 2024. Hire a lin-
guist!: Learning endangered languages in LLMs with
in-context linguistic descriptions.
In Findings of
the Association for Computational Linguistics ACL
2024, pages 15654–15669, Bangkok, Thailand and
virtual meeting. Association for Computational Lin-
guistics.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.
Weinberger, and Yoav Artzi. 2020.
Bertscore:
Evaluating text generation with bert.
Preprint,
arXiv:1904.09675.
10

```
