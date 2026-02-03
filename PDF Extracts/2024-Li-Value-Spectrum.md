---
title: "Value-Spectrum - PDF Extract"
source_pdf: "2024-Li-Value-Spectrum.pdf"
pages: 20
extracted_at: "2026-01-24T17:05:38.355333"
---

# PDF Extract: Value-Spectrum

**Source PDF:** 2024-Li-Value-Spectrum.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

arXiv:2411.11479v3  [cs.CL]  3 Jun 2025
Value-Spectrum: Quantifying Preferences of Vision-Language Models
via Value Decomposition in Social Media Contexts
Jingxuan Li1,*
Yuning Yang1,*
Shengqi Yang2
Linfan Zhang1
Ying Nian Wu1
1University of California, Los Angeles
2Los Alamos National Laboratory
{madili, yuningyang, linfanz}@g.ucla.edu
shengqi@lanl.gov
ywu@stat.ucla.edu
Abstract
The recent progress in Vision-Language Mod-
els (VLMs) has broadened the scope of multi-
modal applications. However, evaluations often
remain limited to functional tasks, neglecting
abstract dimensions such as personality traits
and human values. To address this gap, we in-
troduce Value-Spectrum, a novel Visual Ques-
tion Answering (VQA) benchmark aimed at
assessing VLMs based on Schwartz’s value di-
mensions that capture core human values guid-
ing people’s preferences and actions. We de-
sign a VLM agent pipeline to simulate video
browsing and construct a vector database com-
prising over 50,000 short videos from TikTok,
YouTube Shorts, and Instagram Reels. These
videos span multiple months and cover diverse
topics, including family, health, hobbies, soci-
ety, technology, etc. Benchmarking on Value-
Spectrum highlights notable variations in how
VLMs handle value-oriented content. Beyond
identifying VLMs’ intrinsic preferences, we
also explore the ability of VLM agents to adopt
specific personas when explicitly prompted, re-
vealing insights into the adaptability of the
model in role-playing scenarios. These find-
ings highlight the potential of Value-Spectrum
as a comprehensive evaluation set for track-
ing VLM preferences in value-based tasks and
abilities to simulate diverse personas. The com-
plete code and data are available at https://
github.com/Jeremyyny/Value-Spectrum.
1
Introduction
Vision-Language Models, built upon Large Lan-
guage Models (LLMs) with pre-trained vision en-
coders through cross-modal alignment training,
have shown impressive perceptual and cognitive
capabilities in tasks like VQA and image cap-
tioning (Zhou et al., 2019; Radford et al., 2021;
Zhang et al., 2023; Lu et al., 2024). Recent re-
search has identified that LLMs exhibit distinct
*Equal contribution, alphabetical by first name.
Figure 1: Exploring value-driven role-playing in
VLMs. This study investigates how VLMs adopt as-
signed personas to align value traits and preferences
within social media contexts.
preferences (Li et al., 2024), personalities (Serapio-
García et al., 2023), and values (Ren et al., 2024a).
In addition, some studies have explored the poten-
tial of LLMs as role-playing agents to simulate
various personas (Wang et al., 2023b; Chen et al.,
2024a). Questions thus arise about whether VLMs,
as visual extensions of LLMs, also exhibit inherent
preferences and whether they can be induced to
role-play specific personas.
To address these concerns, our study explores
two key questions: (1) Do VLMs exhibit prefer-
ence traits? (2) Can VLMs adapt their traits to
role-play specific human-designed personas, align-
ing their behaviors and preferences to match prede-
fined roles? To answer these questions, we propose
a framework that systematically evaluates VLM
preference traits through analyzing their values,
i.e., the guiding principles that influence (human)
attitudes, beliefs, and traits (Schwartz, 2012). By
evaluating how VLMs prioritize these values, we
can gain insights into their preference traits and
alignment with human-designed personas.

--- Page 2 ---

Figure 2: Overview of short video contents distribution of Value-Spectrum dataset. We collect an abundance of
short video screenshots relevant to 10 Schwartz values. The area of circles centered at each keyword represents the
amount of relevant videos in the dataset.
In this paper, we introduce Value-Spectrum, a
benchmark designed to evaluate preference traits
in VLMs through visual content from social media.
Our framework utilizes VLM agents embedded
within social media platforms to collect a dataset
of 50, 191 unique short video screenshots span-
ning a wide range of topics, including lifestyle,
technology, health, and more. To enable scalable
evaluation, we construct a vector database using
the CLIP model (Radford et al., 2021), facilitating
keyword-driven retrieval of images aligned with
specific value dimensions. These images repre-
senting each value dimension are then presented to
VLMs alongside designed questionnaires to assess
their preferences.
Our findings reveal models’ shared tendency to
exhibit a strong inclination towards Universalism
and Benevolence, but preferences still vary across
models. CogVLM2 and Gemini 2.0 Flash demon-
strate relatively balanced and high preferences
across all value dimensions, while other models
like GPT-4o and Claude 3.5 Sonnet show distinct
preferences, favoring values like Universalism and
dislikes Stimulation. In contrast, Blip-2 shows low
engagement across most value dimensions, with
the highest standard deviation, indicating a random
preference pattern with inconclusive responses for
reasons of likes and dislikes.
In addition to the static preferences of VLMs, we
evaluate their abilities to adapt inherent preferences
in role-playing specific personas. We propose two
strategies, Simple and Inductive Scoring Question-
naire(ISQ), to assess the effectiveness of different
prompt techniques in inducing VLMs with injected
personas. By evaluating these strategies across mul-
tiple platforms, our experiments show that TikTok
serves as an optimal testing environment for induc-
ing VLM personalities, with models demonstrating
the strongest alignment under the ISQ strategy. No-
tably, Claude 3.5 Sonnet achieved the highest align-
ment with the ISQ strategy, whereas Blip-2 showed
no preference alignment under either strategy, un-
derscoring fundamental differences in model adapt-
ability.
This work makes the following contributions:
• We propose Value-Spectrum, a benchmark
for quantifying VLM value preferences, using
social media-based contents to reveal human-
like traits across different VLMs.
• We present a dataset of over 50k short video
screenshots spanning diverse topics, social
media platforms, and release dates, designed
for our benchmark.
• We embed specific role-play personas into
VLMs using two strategies(Simple and ISQ)
to adjust their value traits, achieving improved
personality alignment in real-world interac-
tions.

--- Page 3 ---

Figure 3: Illustration of our VLM agent interaction with social media videos and screenshot collection pipeline
Our pipeline uses a VLM agent to capture screenshots from social media videos (e.g., Instagram, TikTok, YouTube).
These screenshots are fed to a VLM (e.g., GPT, Gemini, Qwen, Claude), which then indicates its preference
(Yes/No) for the content (e.g., in response to "Do you like this content?"). The agent subsequently acts (e.g.,
continues viewing or scrolls to the next video) based on this VLM feedback, enabling automated assessment of
VLM responses to visual social media content.
2
Related work
2.1
Vision-Language Agents
VLMs take inputs as images and textual descrip-
tions, and they learn to discover the knowledge
from the two modalities.
The recent develop-
ment of large VLMs is rapidly advancing the field
of AI. These models have the potential to revo-
lutionize various industries and tasks, showcas-
ing their power in plot and table identifying (Liu
et al., 2022),VQA (Hu et al., 2024), image caption-
ing (Bianco et al., 2023), and e.t.c. Following Niu
et al. (2024), the environment for VLM agents to
interact with social media can be constructed. We
design an automated control pipeline that guides
the agent to continuously interact with social net-
works.
2.2
Computational Social Science
The intersection of social media and computational
social science has emerged as a dynamic field of
research (Chen et al., 2023). Dialogues and social
interactions, with their vast user base and intricate
networks of connections, offer a large database for
studying human behaviors (Christakis and Fowler,
2013), social relationships (Qiu et al., 2021), and
social networks (Zhang and Amini, 2023). Re-
searchers in computational social science apply
advanced computational techniques, such as ma-
chine learning, natural language processing (NLP),
and network analysis, to analyze massive datasets
extracted from social media platforms. These anal-
yses provide insights into various phenomena, in-
cluding information diffusion (Jiang et al., 2014),
opinion formation (Xiong and Liu, 2014), and col-
lective behavior (Pinheiro et al., 2016).
2.3
Sentiment, Personality, and Value
The community has employed machine learning-
based models to study human sentiment (Malviya
et al., 2020), personality (Stachl et al., 2020), and
values (Qiu et al., 2022; Ye et al., 2024). Building
on this, research has explored AI personalities, in-
cluding those of LLMs (Serapio-García et al., 2023;
Li et al., 2023b; Röttger et al., 2024), and their
alignment with human values (Ren et al., 2024b).
Inspired by recent efforts to reveal AI agent traits
through indirect methods like physiological ex-
ams (Jiang et al., 2024), questionnaires (Huang
et al., 2023), and cultural views (Kovaˇc et al., 2023),
we adopt a novel perspective: examining machine
behavior and inferred personality traits, including
underlying values, to evaluate the performance of
VLMs on mainstream social media platforms. To
ground this examination, we utilize Schwartz’s
value theory (Schwartz, 1992), a comprehensive
and culturally validated classification of human
motivations (Davidov et al., 2008) that predicts at-
titudes and social behavior (Bardi and Schwartz,
2003). While prior computational work like Val-
ueNet (Qiu et al., 2022) and ValueBench (Ren et al.,
2024b) has assessed values in text-based NLP sys-
tems, and recent studies have begun exploring cul-
tural value sensitivity in multimodal models (Ya-
dav et al., 2025), our work specifically extends
this value-based evaluation to VLMs within visual
contexts on social media.
3
Data Collection
Inspired by ScreenAgent (Niu et al., 2024), our
work leverages a VLM-driven graphical user inter-
face (GUI) agent to autonomously navigate popular
social media platforms. This agent conducts ran-

--- Page 4 ---

Figure 4: Schwartz value-based image retrieval pipeline. Our pipeline retrieves video screenshots based on
Schwartz values by associating each value with relevant keywords, such as linking Hedonism to topics like vacation.
These keywords are converted into vector queries, retrieving matching video content using the shortest distance
within our database.
dom walks through social media platforms where
it observes and captures screenshots. The data col-
lected is stored in a vector database (Han et al.,
2023), creating a structured repository optimized
for value decomposition and efficient retrieval. We
aim to analyze VLMs’ behaviors across diverse
social contexts and reveal their preferences. The
automated data collection process (see Figure 3)
efficiently fetches a large volume of diverse con-
tent, granting the analysis with scope and depth
that traditional manual collection methods could
not achieve.
The resulting dataset comprises 50, 191 videos
sourced from Instagram (32%), YouTube (29%),
and TikTok (39%). Each entry includes the video
link, a screenshot, and meta-information such as
platform name and post date, capturing a compre-
hensive snapshot of content ranged between July
31, 2024, and October 31, 2024. By collecting
data proportionally across these platforms, we en-
able balanced analysis and facilitate unbiased value
decomposition across social media content. This
innovative dataset empowers researchers to explore
the behavior of VLMs in a systematic and orga-
nized way, fostering deeper insights into model
interpretation and the dynamics of social media.
To examine the distribution of video themes in
this dataset, we take a screenshot of each video
at the beginning as a representation of the video
content. In Figure 2, we present the distribution
of videos that are relevant to ten Schwartz val-
ues. Specifically, for each Schwartz value, we
curate 10 representative keywords. The area of
the transparent circle is proportional to the num-
ber of videos that lie within a distance of 1.5 to
the corresponding normalized keyword vector. We
find that videos relevant to these Schwartz Value
Dimensions Achievement, Hedonism, and Power
appear most frequently, while videos about Tradi-
tion are relatively rare. We then vectorize the image
and define its relevance to a specific keyword using
cosine distance.
4
Evaluating VLM’s Preferences
Extending the idea of analyzing LLMs’ human
likeness (Shanahan et al., 2023; Kovaˇc et al., 2023)
to VLMs with both visual and textual inputs, we
ask: Do VLMs also exhibit inherent preferences?
To answer this question, we explore a diverse set
of VLMs including GPT-4o (OpenAI, 2023), Gem-
ini 2.0 Flash (Team et al., 2023), Claude 3.5 Son-
net (Anthropic, 2023), DeepSeek-VL2 (Wu et al.,
2024), Qwen2.5-VL-Plus (Bai et al., 2023), In-
ternVL2 (Chen et al., 2024c), CogVLM2 (Hong
et al., 2024), and Blip-2 (Li et al., 2023a) to as-
sess their value preferences. We quantify a VLM’s
preferences by evaluating its attitudes towards the
10 Schwartz values. This approach enables us to
construct a comprehensive profile of each model’s
value preferences and to identify its unique value
traits.
After constructing a vector database (as de-
scribed in Section 3) to retrieve images based on
specific Schwartz values’ keywords, we analyze
and compare the responses and attitudes of each
model toward them. Our analysis reveals the extent
to which each value captures the VLMs’ attention,
uncovering both similarities and differences across
models, and highlighting distinct inclinations and
sentiments within each VLM.
4.1
Preference Retrieval
To evaluate a VLM’s preference for a specific
Schwartz value, we collect each model’s responses
to images associated with several keywords related
to the value (see Figure 4). For instance, we se-
lected the keywords Equality, Globe, and Hand-
shake for the Universalism dimension because they
closely align with its core principles of fairness and
global awareness. For each keyword linked to the
value, each model reviews five images and answers
their attitude towards each image.

--- Page 5 ---

Figure 5: Each VLM’s preference scores towards the
10 Schwartz values. The scores range from 0 to 100,
with higher scores indicating stronger preferences for
the corresponding values.
We retrieve the preference score of each VLM
on the given visual input according to the following
prompts:(1) Do you like the content of this image?
Please include yes or no in your answer, just re-
spond in one word. (2)Why do you like or dislike
this picture? (3) Describe this image in English
briefly.
The answer to the question is processed into
either yes (1) or no (0), and the average score is
calculated in percentage to evaluate the intensity
of the model’s preference for a given value (e.g.,
Universalism).
4.2
Preference Patterns
We evaluate and visualize the preference dimen-
sions, identifying three distinct patterns:
(1) Global Pattern: After summarizing the pref-
erence score across all VLMs, we find most of
them tend to prefer certain values over others. The
results indicate a general preference for Univer-
salism and Benevolence while showing relatively
less liking for Stimulation and Power. The specific
ranking of values is presented in Figure 6.
(2) Range Consistency: As shown in Figure 5,
each model’s preference scores, despite very few
extremes, remain within a narrow band of approx-
imately 15 around a central value. Models dis-
play varying levels of engagement with the content:
some, like InternVL2, are more reserved, occupy-
ing a smaller area on the plot with lower preference
scores, while others, like Gemini 2.0 Flash, show
greater enthusiasm, demonstrating interest across
all inputs with higher preference scores.
(3) Individual Model Variations: When analyzed
individually, some models, such as Gemini 2.0
Figure 6: Average preference scores for 10 Schwartz
values across VLMs. The length of each bar represents
the mean score of all models for a value, with higher
scores indicating a higher overall preference across all
VLMs.
Flash, exhibit consistently high preferences across
all 10 Schwartz values. In contrast, other models,
like Claude 3.5 Sonnet, display more specific pref-
erences as indicated in the standard deviation of
scores across values. (Figure 7).
GPT-4o maintains balanced scores around 80,
except for a notably lower score for Stimulation,
with strong inclinations toward Universalism and
Benevolence. Qwen2.5-VL-Plus covers a broad
range of scores from 40 to 70, maintaining rela-
tive stability with a low standard deviation, yet it
shares an aversion to Stimulation similar to other
models. Deepseek-VL2 is highly balanced, slightly
favoring Benevolence. CogVLM2, with a very low
standard deviation, stands out by marking Power as
its highest, diverging from all other models. Blip-2
ranks low across most values and has the highest
variance, often providing short, inconclusive, or
passive responses when reasoning about its likes or
dislikes, reflecting a lack of ability to express pref-
erences. Claude 3.5 Sonnet has a distinct person-
ality, with the second-highest standard deviation,
favoring Universalism while scoring the lowest in
Power and Stimulation. InternVL2 demonstrates
the lowest engagement, particularly disregarding
Stimulation, while its high standard deviation sug-
gests that, despite overall disinterest, it does show
selective tendencies in certain areas. Finally, Gem-
ini 2.0 Flash has both the lowest standard deviation
and the highest overall scores, maintaining values
above 80 across all dimensions, making it the most
consistent and high-scoring model.

--- Page 6 ---

Model
Open-source Parameters Self-direction Universalism Benevolence Stimulation Power Achievement Hedonism Conformity Tradition Security
GPT-4o
✗
–
78
90
88
56
80
86
76
86
68
78
Deepseek-VL2
✓
27B
66
68
82
68
76
62
72
78
80
64
Claude 3.5 Sonnet
✗
–
70
70
68
34
50
60
66
58
66
58
Gemini 2.0 Flash
✗
–
84
90
86
92
94
92
82
86
92
90
Blip-2
✓
2.7B
72
78
68
48
28
48
52
64
74
40
Qwen2.5-VL-Plus
✓
72B
70
56
70
40
62
58
60
56
70
52
CogVLM2
✓
8B
80
80
80
74
90
72
78
68
78
76
InternVL2
✓
26B
44
54
44
28
32
38
48
54
54
26
Table 1: Comparison of VLMs’ preference scores based on Schwartz’s 10 values. Higher scores indicate
stronger preferences. "Open-source" indicates whether the model is publicly available, and "Parameters" denotes
the model’s size in billions (B).
Figure 7: Average standard deviation for each VLM.
Higher standard deviation indicates stronger preferences
for certain values over others, while lower standard
deviation reflects a more balanced attitude.
5
Inducing VLM’s Preferences
Our initial experiment shows that VLMs have in-
herent inclinations toward different values. We now
explore the dynamic aspects of VLM preferences
beyond these static traits. We use Role-Playing
Language Agents (RPLA) (Chen et al., 2024b) as
a framework to assess VLMs’ ability to adapt dy-
namically and simulate different personas, mak-
ing decisions accordingly. Building on research
showing that LLMs can emulate personas through
RPLA (Serapio-García et al., 2023), we propose
two key questions for VLMs: (1) How well can
VLMs align their traits to role-play personas using
specific prompts? (2) Can strategies enhance accu-
racy and consistency in role-playing performance?
5.1
Experiment
We use social media recommendation systems
to evaluate whether VLMs can exhibit prefer-
ences aligned with the specified embedded persona.
These systems rely on viewing duration as a key
signal for content recommendation(Appendix A).
Considering the complexity of the experiment and
the stability of model performance, we ultimately
selected the following five models for evaluation:
GPT-4o, Gemini 1.5 Pro, Qwen-VL-Plus (Bai et al.,
2023), Claude 3.5 Sonnet, and CogVLM (Wang
et al., 2023a). We assess the VLMs’ role-playing
ability by analyzing how well the recommended
content reflects the imposed preferences. For exam-
ple, adopting a pet owner persona should heighten
the model’s emphasis on Benevolence, valuing
kindness and care, resulting in longer engagement
with pet care videos and increased related recom-
mendations (Liu et al., 2023).
In addition, we improve VLM performance on
social networks by inducing personas through a
questionnaire (Abeysinghe and Circi, 2024), com-
prehensively evaluating traits like emotional en-
gagement, value alignment, curiosity, and prefer-
ence matching to guide structured optimization.
Simple Strategy
In the simple strategy, we assign a specific persona
in the demographic persona dataset from Persona-
Chat (Zhang et al., 2018) to the VLM using the
prompt: You are a person who possesses certain
traits, and the following statements best describe
you: {Personality 1, 2, 3 . . . }. Then, we pose a sim-
ple question: Determine whether you are interested
in the content of the given picture.
The VLM engages with video shorts by respond-
ing either yes or no. A yes response prompts the
VLM agent to remain on the current video, while
a no results in an immediate skip. Alignment is
measured as the increase in the frequency of recom-
mended content that the VLM decides is interesting
over time.
Iavg = 1
N
N
X
t=1
(
Pn
i=1 Y (t)
l
(i) −Pn
i=1 Y (t)
f (i)
Pn
i=1 Y (t)
f (i)
)

--- Page 7 ---

Figure 8: Each VLM’s percentage score of preference alignment changes across TikTok, YouTube, and
Instagram. Positive values indicate an increase in alignment, while negative values represent a decrease.
We define Iavg, the averaged percentage increase
of yes responses, to measure the effectiveness of
the strategy. Yl(i) and Yf(i) are the number of
yes responses until i-th video in the last and first
n = 50 videos, respectively. For each model, we
conduct N = 10 trials, with each trial consisting
of 100 video scrolls in total.
Result Analysis. Results highlight significant dif-
ferences in role-playing effectiveness across plat-
forms and models. TikTok stands out for GPT-
4o and CogVLM, where GPT-4o exhibits "overfit-
ting" behavior, showing highly nuanced responses
to assigned roles that align closely with TikTok’s
recommendation system.
However, this strong
alignment is not consistent across models; for in-
stance, Claude 3.5 Sonnet performs worse on Tik-
Tok, suggesting model-specific sensitivities to the
platform’s dynamics. On YouTube and Instagram,
performance is generally lower, with only modest
gains or even negative alignment observed. These
results indicate that TikTok’s algorithmic design
may amplify certain models’ role-play capabilities,
whereas YouTube and Instagram seem less con-
ducive to capturing role-play nuances, possibly due
to differences in content structure, user interaction
patterns, or recommendation algorithms.
From previous experiments, CogVLM and
Qwen-VL-Plus view all Schwartz values favor-
ably, yet when CogVLM excels in this role-playing
task, effectively adopting role-specific preferences,
Qwen-VL-Plus shows only partial adherence. Blip-
2 demonstrates no engagement or role-playing
ability, lacking any signs of an induced person-
ality. The findings show that even basic prompts
can evoke detectable preferences, with some plat-
forms emerging as particularly well-suited for role-
playing tasks. Model adaptability in expressing
role-related traits varied significantly if the persona
is given in a simpler prompt.
Inductive Scoring Questionnaire Strategy.
Building on insights from the simple questioning
approach, we develop the ISQ strategy to enhance
VLMs’ performance in social media alignment
tasks. ISQ employs a series of prompts inquiring
about various aspects of the screenshot. When pre-
sented with visual content, VLMs are asked to rate
aspects like visual appeal, preference alignment,
curiosity, etc.
Prompts include questions such as On a scale of
1 to 10, how visually appealing is this screenshot to
you based on your persona? and Does this screen-
shot make you want to click and start watching the
video immediately?
The ISQ strategy calculates a composite score
to assess VLM engagement, with scores above
a threshold (e.g. 60) indicating genuine interest,
prompting extended interaction. This layered ap-
proach enhances persona analysis and final pref-
erence evaluation, improving role-specific perfor-
mance on social media platforms.
The score is calculated as:
S% = va + cs + ee + ve + 10pa + 10ad
60
× 100
Each response contributes to the total score: va
for visual appeal, cs for curiosity stimulation, ee
for emotional engagement, ve for value expectation,
pa for preference alignment (yes = 1, no = 0), ad
for action desire (yes = 1, no = 0). The increase is
calculated the same as the simple strategy.

--- Page 8 ---

Figure 9: Value distribution comparison between VLMs and corresponding LLMs. For the same model
(e.g., GPT-4o and GPT-4o_text), different input modes (multi-modal vs. text-only) are compared. Experiments
demonstrate that the choice of multi-modal input significantly influences some models’ value preferences. While
models like GPT-4o show consistency across input modes, others, such as Claude 3.5 Sonnet and Gemini 1.5 Pro,
exhibit notable differences in preferences.
Result Analysis. Compared to the simple strat-
egy, the ISQ strategy performances are elevated
throughout all models and platforms except for
Qwen-VL-Plus. This shows that the strategy could
successfully induce the model’s role-playing ability
in preference indication detectable through social
media on behalf of the persona.
Following the trend in simple strategy, we could
see a strong increase for TikTok, particularly with
Gemini 1.5 Pro, which demonstrates an average
rise of as much as 51.9.
GPT-4o, Gemini 1.5
Pro, and Claude 3.5 Sonnet—all displayed notable
improvements, with consistently positive changes
in performance. This suggests that these models
respond well to the ISQ strategy, allowing them
to adopt and express induced personalities with
greater depth. Among them, Gemini 1.5 Pro and
Claude 3.5 Sonnet particularly benefited from the
ISQ approach, showing remarkable growth in com-
parison to earlier results in the simple strategy. This
demonstrates that the ISQ strategy enhances VLMs’
ability to engage with role-playing tasks more ef-
fectively than the previous simple strategy.
6
Discussion
VLMs vs. Corresponding LLMs. We conduct
several experiments to examine whether different
types of multi-modal inputs influence value pref-
erence outcomes. As shown in Figure 9, we com-
pare value preferences derived directly from VLMs
using images as input with those generated by feed-
ing the corresponding text-based image descrip-
tions created by the same VLM into their paired
LLMs. The results reveal significant differences in
value preferences between these two modes. For
many value dimensions, VLMs and LLMs pro-
duce distinct preference patterns, especially in mod-
els like Claude 3.5 Sonnet and Gemini 1.5 Pro,
where the outputs diverge significantly across in-
put modes. In contrast, GPT-4o displays greater
consistency across modes, suggesting its ability
to integrate visual and textual information cohe-
sively. These findings highlight that the choice of
input mode—visual or text—can significantly af-
fect model outputs, underscoring the importance of
input selection in applications requiring personal-
ized or human-like responses. Detailed evaluation
methods and results are provided in Appendix E.
Single Frame Screenshot Representation. To
validate single-frame screenshots for video content
analysis, we randomly select 500 images from each
different social media platform in our dataset for
human evaluation. Annotators are provided with
the instructions outlined in Appendix D, along with
the images and additional context. Each image-
video pair is assessed by three annotators, resulting
in a total of 4,500 ratings. Annotators review the
full video and its corresponding screenshot, rat-
ing how accurately the screenshot represents the
video’s content. The results indicate that 90.4% of
screenshots are considered to be representative of
the video’s main content, demonstrating the effec-
tiveness of single-frame screenshots across plat-
forms. However, 8.8% of the frames are rated
as non-representative, highlighting the challenges
posed by videos with complex scenes or rapid tran-
sitions.
7
Conclusion
Our study introduces Value-Spectrum, a bench-
mark for evaluating value preferences in VLMs
using a vector database derived from social media
platforms. Through systematic evaluation, we ob-
serve a shared global inclination among models
toward certain mainstream values, such as Univer-
salism, likely influenced by the nature of their train-

--- Page 9 ---

ing data. At the same time, significant differences
emerged across other value dimensions, highlight-
ing disparities in how VLMs align with diverse
human-designed value systems. These findings
reveal both commonalities that reflect broader soci-
etal trends and divergences that underscore model-
specific characteristics, prompting us to explore
whether these variations can be adjusted to induce
specific personas.
Our work also provides practical insights into
VLMs’ ability to adapt their value preferences dy-
namically through role-playing, offering a pathway
to align machine behaviors with human-designed
personas. By connecting role-playing capabilities
and alignment strategies, we aim to inspire further
research into value-driven AI agent systems and
their adaptability in real-world applications.
8
Limitations
The evaluation utilizes Schwartz’s value dimen-
sions as the foundation for understanding person-
ality traits and preferences, highlighting opportu-
nities for future research to incorporate broader
cultural and personality-based perspectives. Fu-
ture studies might consider expanding the set of
value dimensions or integrating alternative value
systems. Additionally, our use of single-frame
screenshots, in order to simplify analysis and main-
tain efficiency, is proven to effectively represent
the corresponding video content through annota-
tors’ high ratings. However, our methodology still
faces challenges in capturing the essence of some
videos that are fast-changing and complex in their
storytelling. This leaves room for future refine-
ment.
9
Ethical Considerations
We eliminate any harmful effects of VLMs by
ensuring that they only observe content without
interacting through comments or likes. This ap-
proach maintains the integrity of the social media
ecosystem and prevents unintended AI-driven con-
sequences. However, we recognize that VLMs may
still inadvertently produce discriminatory content,
reflecting biases based on gender, race, or socioe-
conomic status. We acknowledge these challenges
and emphasize the need for ongoing efforts to ad-
dress and minimize such biases in model outputs.
References
Bhashithe Abeysinghe and Ruhan Circi. 2024. The chal-
lenges of evaluating llm applications: An analysis of
automated, human, and llm-based approaches. arXiv
preprint arXiv:2406.03339.
Anthropic. 2023. Claude 3.5.
Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang,
Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou,
and Jingren Zhou. 2023. Qwen-vl: A frontier large
vision-language model with versatile abilities. arXiv
preprint arXiv:2308.12966.
Anat Bardi and Shalom H Schwartz. 2003. Values and
behavior: Strength and structure of relations. Person-
ality and Social Psychology Bulletin, 29(10):1207–
1220.
Simone Bianco, Luigi Celona, Marco Donzella, and
Paolo Napoletano. 2023. Improving image caption-
ing descriptiveness by ranking and llm-based fusion.
arXiv preprint arXiv:2306.11593.
Jiangjie Chen, Xintao Wang, Rui Xu, Siyu Yuan, Yikai
Zhang, Wei Shi, Jian Xie, Shuang Li, Ruihan Yang,
Tinghui Zhu, Aili Chen, Nianqi Li, Lida Chen, Caiyu
Hu, Siye Wu, Scott Ren, Ziquan Fu, and Yanghua
Xiao. 2024a. From persona to personalization: A
survey on role-playing language agents.
ArXiv,
abs/2404.18231.
Jiangjie Chen, Xintao Wang, Rui Xu, Siyu Yuan, Yikai
Zhang, Wei Shi, Jian Xie, Shuang Li, Ruihan Yang,
Tinghui Zhu, Aili Chen, Nianqi Li, Lida Chen, Caiyu
Hu, Siye Wu, Scott Ren, Ziquan Fu, and Yanghua
Xiao. 2024b. From persona to personalization: A sur-
vey on role-playing language agents. arXiv preprint
arXiv:2404.18231.
Yan
Chen,
Kate
Sherren,
Michael
Smit,
and
Kyung Young Lee. 2023. Using social media im-
ages as data in social science research. New Media
& Society, 25(4):849–871.
Zhe Chen, Weiyun Wang, Hao Tian, Shenglong Ye,
Zhangwei Gao, Erfei Cui, Wenwen Tong, Kongzhi
Hu, Jiapeng Luo, Zheng Ma, Ji Ma, Jiaqi Wang,
Xiao wen Dong, Hang Yan, Hewei Guo, Conghui He,
Zhenjiang Jin, Chaochao Xu, Bin Wang, Xingjian
Wei, Wei Li, Wenjian Zhang, Bo Zhang, Lewei Lu,
Xizhou Zhu, Tong Lu, Dahua Lin, and Yu Qiao.
2024c. How far are we to gpt-4v? closing the gap
to commercial multimodal models with open-source
suites. ArXiv, abs/2404.16821.
Nicholas A Christakis and James H Fowler. 2013. So-
cial contagion theory: examining dynamic social net-
works and human behavior. Statistics in medicine,
32(4):556–577.
Eldad Davidov, Peter Schmidt, and Shalom H Schwartz.
2008. The measurement of values: Testing and im-
proving the theory in a comparative perspective. Eu-
ropean Journal of Social Psychology, 38(6):881–897.

--- Page 10 ---

Yikun Han, Chunjiang Liu, and Pengfei Wang. 2023. A
comprehensive survey on vector database: Storage
and retrieval technique, challenge. arXiv preprint
arXiv:2310.11703.
Wenyi Hong, Weihan Wang, Ming Ding, Wenmeng Yu,
Qingsong Lv, Yan Wang, Yean Cheng, Shiyu Huang,
Junhui Ji, Zhao Xue, Lei Zhao, Zhuoyi Yang, Xiaotao
Gu, Xiaohan Zhang, Guanyu Feng, Da Yin, Zihan
Wang, Ji Qi, Xixuan Song, Peng Zhang, De-Feng
Liu, Bin Xu, Juanzi Li, Yu-Chen Dong, and Jie Tang.
2024. Cogvlm2: Visual language models for image
and video understanding. ArXiv, abs/2408.16500.
Wenbo Hu, Yifan Xu, Yi Li, Weiyue Li, Zeyuan Chen,
and Zhuowen Tu. 2024. Bliva: A simple multimodal
llm for better handling of text-rich visual questions.
In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 38, pages 2256–2264.
Jen-tse Huang, Man Ho Lam, Eric John Li, Shujie Ren,
Wenxuan Wang, Wenxiang Jiao, Zhaopeng Tu, and
Michael R Lyu. 2023. Emotionally numb or empa-
thetic? evaluating how llms feel using emotionbench.
arXiv preprint arXiv:2308.03656.
Chunxiao Jiang, Yan Chen, and KJ Ray Liu. 2014. Evo-
lutionary dynamics of information diffusion over so-
cial networks. IEEE transactions on signal process-
ing, 62(17):4573–4586.
Guangyuan Jiang, Manjie Xu, Song-Chun Zhu, Wen-
juan Han, Chi Zhang, and Yixin Zhu. 2024. Evaluat-
ing and inducing personality in pre-trained language
models. Advances in Neural Information Processing
Systems, 36.
Grgur Kovaˇc, Masataka Sawayama, Rémy Portelas, Cé-
dric Colas, Peter Ford Dominey, and Pierre-Yves
Oudeyer. 2023. Large language models as super-
positions of cultural perspectives. arXiv preprint
arXiv:2307.07870.
Junlong Li, Fan Zhou, Shichao Sun, Yikai Zhang, Hai
Zhao, and Pengfei Liu. 2024. Dissecting human and
llm preferences. ArXiv, abs/2402.11296.
Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi.
2023a. Blip-2: Bootstrapping language-image pre-
training with frozen image encoders and large lan-
guage models. In International conference on ma-
chine learning, pages 19730–19742. PMLR.
Junyi Li, Ninareh Mehrabi, Charith Peris, Palash Goyal,
Kai-Wei Chang, A. G. Galstyan, Richard Zemel, and
Rahul Gupta. 2023b. The steerability of large lan-
guage models toward data-driven personas. ArXiv,
abs/2311.04978.
Fangyu Liu, Julian Martin Eisenschlos, Francesco Pic-
cinno, Syrine Krichene, Chenxi Pang, Kenton Lee,
Mandar Joshi, Wenhu Chen, Nigel Collier, and
Yasemin Altun. 2022. Deplot: One-shot visual lan-
guage reasoning by plot-to-table translation. arXiv
preprint arXiv:2212.10505.
Peng Liu, Lemei Zhang, and Jon Atle Gulla. 2023. Pre-
train, prompt, and recommendation: A comprehen-
sive survey of language modeling paradigm adapta-
tions in recommender systems. Transactions of the
Association for Computational Linguistics, 11:1553–
1571.
Yujie Lu, Dongfu Jiang, Wenhu Chen, William Yang
Wang, Yejin Choi, and Bill Yuchen Lin. 2024.
Wildvision:
Evaluating vision-language models
in the wild with human preferences.
ArXiv,
abs/2406.11069.
Sunil Malviya, Arvind Kumar Tiwari, Rajeev Srivastava,
and Vipin Tiwari. 2020. Machine learning techniques
for sentiment analysis: A review. SAMRIDDHI: A
Journal of Physical Sciences, Engineering and Tech-
nology, 12(02):72–78.
Runliang Niu, Jindong Li, Shiqi Wang, Yali Fu, Xiyu
Hu, Xueyuan Leng, He Kong, Yi Chang, and
Qi Wang. 2024. Screenagent: A vision language
model-driven computer control agent. arXiv preprint
arXiv:2402.07945.
OpenAI. 2023. Gpt-4.
Flávio L Pinheiro, Francisco C Santos, and Jorge M
Pacheco. 2016. Linking individual and collective
behavior in adaptive social networks. Physical review
letters, 116(12):128702.
Liang Qiu, Yuan Liang, Yizhou Zhao, Pan Lu, Baolin
Peng, Zhou Yu, Ying Nian Wu, and Song-Chun Zhu.
2021. Socaog: Incremental graph parsing for so-
cial relation inference in dialogues. arXiv preprint
arXiv:2106.01006.
Liang Qiu, Yizhou Zhao, Jinchao Li, Pan Lu, Baolin
Peng, Jianfeng Gao, and Song-Chun Zhu. 2022. Val-
uenet: A new dataset for human value driven di-
alogue system. In Proceedings of the AAAI Con-
ference on Artificial Intelligence, volume 36, pages
11183–11191.
Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya
Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sas-
try, Amanda Askell, Pamela Mishkin, Jack Clark,
Gretchen Krueger, and Ilya Sutskever. 2021. Learn-
ing transferable visual models from natural language
supervision. In International Conference on Machine
Learning.
Yuanyi Ren, Haoran Ye, Hanjun Fang, Xin Zhang,
and Guojie Song. 2024a.
Valuebench: Towards
comprehensively evaluating value orientations and
understanding of large language models.
ArXiv,
abs/2406.04214.
Yuanyi Ren, Haoran Ye, Hanjun Fang, Xin Zhang, and
Guojie Song. 2024b. Valuebench: Towards compre-
hensively evaluating value orientations and under-
standing of large language models. arXiv preprint
arXiv:2406.04214.

--- Page 11 ---

Paul Röttger, Valentin Hofmann, Valentina Pyatkin,
Musashi Hinck, Hannah Rose Kirk, Hinrich Schutze,
and Dirk Hovy. 2024. Political compass or spin-
ning arrow? towards more meaningful evaluations
for values and opinions in large language models. In
Annual Meeting of the Association for Computational
Linguistics.
Shalom H Schwartz. 1992. Universals in the content
and structure of values: Theoretical advances and
empirical tests in 20 countries. Advances in Experi-
mental Social Psychology, 25:1–65.
Shalom H Schwartz. 2012. An overview of the schwartz
theory of basic values. Online readings in Psychol-
ogy and Culture, 2(1):11.
Greg Serapio-García, Mustafa Safdari, Clément Crepy,
Luning Sun, Stephen Fitz, Peter Romero, Marwa
Abdulhai, Aleksandra Faust, and Maja Matari´c. 2023.
Personality traits in large language models. arXiv
preprint arXiv:2307.00184.
Murray Shanahan, Kyle McDonell, and Laria Reynolds.
2023. Role-play with large language models. arXiv
preprint arXiv:2305.16367.
Clemens Stachl,
Florian Pargent,
Sven Hilbert,
Gabriella M Harari, Ramona Schoedel, Sumer Vaid,
Samuel D Gosling, and Markus Bühner. 2020. Per-
sonality research and assessment in the era of ma-
chine learning. European Journal of Personality,
34(5):613–631.
Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-
Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan
Schalkwyk, Andrew M Dai, Anja Hauth, Katie
Millican, et al. 2023.
Gemini:
a family of
highly capable multimodal models. arXiv preprint
arXiv:2312.11805.
Weihan Wang, Qingsong Lv, Wenmeng Yu, Wenyi
Hong, Ji Qi, Yan Wang, Junhui Ji, Zhuoyi Yang,
Lei Zhao, Xixuan Song, et al. 2023a. Cogvlm: Vi-
sual expert for pretrained language models. arXiv
preprint arXiv:2311.03079.
Xintao Wang, Yunze Xiao, Jen tse Huang, Siyu Yuan,
Rui Xu, Haoran Guo, Quan Tu, Yaying Fei, Ziang
Leng, Wei Wang, Jiangjie Chen, Cheng Li, and
Yanghua Xiao. 2023b. Incharacter: Evaluating per-
sonality fidelity in role-playing agents through psy-
chological interviews. In Annual Meeting of the As-
sociation for Computational Linguistics.
Zhiyu Wu, Xiaokang Chen, Zizheng Pan, Xingchao
Liu, Wen Liu, Damai Dai, Huazuo Gao, Yiyang
Ma, Chengyue Wu, Bing-Li Wang, Zhenda Xie,
Yu Wu, Kai Hu, Jiawei Wang, Yaofeng Sun, Yukun
Li, Yishi Piao, Kang Guan, Aixin Liu, Xin Xie,
Yu mei You, Kaihong Dong, Xingkai Yu, Haowei
Zhang, Liang Zhao, Yisong Wang, and Chong Ruan.
2024.
Deepseek-vl2: Mixture-of-experts vision-
language models for advanced multimodal under-
standing. ArXiv, abs/2412.10302.
Fei Xiong and Yun Liu. 2014. Opinion formation on
social media: an empirical approach. Chaos: An In-
terdisciplinary Journal of Nonlinear Science, 24(1).
Srishti Yadav, Zhi Zhang, Daniel Hershcovich, and Eka-
terina Shutova. 2025.
Beyond words: Exploring
cultural value sensitivity in multimodal models. In
North American Chapter of the Association for Com-
putational Linguistics.
Haoran Ye, Yuhang Xie, Yuanyi Ren, Hanjun Fang, Xin
Zhang, and Guojie Song. 2024. Measuring human
and ai values based on generative psychometrics with
large language models. In AAAI Conference on Arti-
ficial Intelligence.
Jingyi Zhang, Jiaxing Huang, Sheng Jin, and Shijian Lu.
2023. Vision-language models for vision tasks: A
survey. IEEE Transactions on Pattern Analysis and
Machine Intelligence, 46:5625–5644.
Linfan Zhang and Arash A Amini. 2023. Adjusted chi-
square test for degree-corrected block models. The
Annals of Statistics, 51(6):2366–2385.
Saizheng Zhang, Emily Dinan, Jack Urbanek, Arthur
Szlam, Douwe Kiela, and Jason Weston. 2018. Per-
sonalizing dialogue agents: I have a dog, do you have
pets too? arXiv preprint arXiv:1801.07243.
Luowei Zhou, Hamid Palangi, Lei Zhang, Houdong Hu,
Jason J. Corso, and Jianfeng Gao. 2019. Unified
vision-language pre-training for image captioning
and vqa. ArXiv, abs/1909.11059.

--- Page 12 ---

Appendix
A
Industry References
For further information on the signals used for con-
tent recommendation, refer to the following blogs:
• YouTube:https://www.youtube.
com/howyoutubeworks/
product-features/recommendations/
#signals-used-to-recommend-content
Watch history: Our system uses the YouTube
videos you watch to give you better recom-
mendations, remember where you left off,
and more.
• Instagram:https://about.instagram.
com/blog/announcements/
instagram-ranking-explained
View-
ing history: This looks at how often you view
an account’s stories, so we can prioritize the
stories from accounts we think you don’t
want to miss.
• TikTok:https://support.tiktok.com/
en/using-tiktok/exploring-videos/
how-tiktok-recommends-content
User
interactions: Content you like, share, com-
ment on, and watch in full or skip, as well as
accounts of followers that you follow back.
B
Inducing VLM’s Personas
B.1
Experiment Steps
In this section, we detail the steps of our exper-
iments designed to evaluate the effectiveness of
different strategies in identifying persona-related
content on social media platforms. The experiment
comprises three main parts:
Open The Designated Social Media Platform
The second step involves accessing the designated
social media platform. For demonstration, we fo-
cus on TikTok and GPT-4o.
• Open TikTok website(Figure 10).
• Navigate to the ’For You’ page, where a vari-
ety of content is displayed.
Capture Screenshot Image of Playing Short
Video Next, we capture screenshots of the short
videos that are playing.
This captured screen-
shot is then inputted to the VLM. An ex-
ample of a screenshot is shown in Figure11.
Figure 10: Screenshot of the TikTok homepage.
(URL: https://www.tiktok.com/@pugloulou/
video/7342967563321822497).
Responses and Strategy Actions for Models
We design specific questionnaire prompts for dif-
ferent experimental purposes and then collect and
analyze responses from different VLMs. Based on
these responses, we apply various strategic actions.
Simple Strategy: See details in Figure 13.
ISQ Strategy: See details in Figure 14.
C
Single VS. Multi Frames
In both experiments, screenshots were captured
exactly 2 seconds into the video shorts. This timing
was chosen because most videos begin their main
narrative at this point. Multi-frame analysis was
not utilized for two key reasons:
Preference Evaluation: Using a single frame
aligns with CLIP’s capability to filter and retrieve
the most relevant social media screenshots. Multi-
ple frames are unnecessary for this purpose.
Preference Induction: For recommendation
systems to recognize user preferences, the stay-
ing duration for each video is critical. Capturing
multiple frames increases processing time, causing
most videos to be viewed in their entirety before
scrolling. This diminishes the strategy’s impact
and hinders the system’s ability to distinguish pref-
erences between videos.

--- Page 13 ---

Figure 11: Screenshot of playing a short video
Thus, single-frame analysis was deemed more
effective and practical for the experiments.
D
Human Annotators: Single-Frame
Analysis
We refine the survey formats provided to annota-
tors through multiple iterations, conducting pilot
studies on Amazon Mechanical Turk (MTurk) to
continuously adjust the instructions until the qual-
ity of answers by the annotators meets the desired
standard. The instruction examples referenced by
the annotators can be found in Figure 15.
In the Amazon MTurk task description provided
to annotators, we clearly stated that this task was
for research purposes. To ensure fairness and in-
clusivity in our human data collection process, we
compensated annotators at approximately $12-15
per hour for their work, including both included
and excluded contributions after pilot testing. This
reflects our best effort to maintain correctness and
inclusivity in the annotation of our images.
E
Performance Analysis of Multi-Modal
Inputs Across Value Dimensions
To investigate the influence of different input
modalities on value preference outcomes, we con-
duct experiments to compare results derived from
direct visual inputs with those generated using
text-based image descriptions. Specifically, we
randomly selected 500 images from the Value-
Spectrum dataset, ensuring balanced representa-
tion across 10 value dimensions (50 samples per
dimension). We then retrieved image descriptions
generated by three VLMs —GPT-4o, Gemini 1.5
Pro, and Claude 3.5 Sonnet—by prompting these
models with images from the dataset. These tex-
tual descriptions were then fed into the text-based
versions of the different models to conduct Value
Preference QA.
The results revealed notable differences in value
preference distributions across input modalities.
While GPT-4o demonstrated relatively consistent
performance between visual and text-based inputs,
models like Gemini 1.5 Pro and Claude 3.5 Son-
net displayed greater variability, with outputs di-
verging significantly in specific dimensions. This
suggests that the choice of input mode—visual or
textual—can impact the models’ ability to align
responses with underlying value dimensions. The
detailed scores for all models and input settings
are summarized in Table 10, highlighting patterns
across dimensions such as Achievement, Benevo-
lence, and Tradition. These findings emphasize the
importance of input modality selection in tasks re-
quiring a nuanced understanding of human values.
F
Cultural Diversity Analysis of the
Dataset
We also conducted a systematic analysis to quantify
the cultural variety present. This analysis aimed to
provide a clearer understanding of the distribution
of cultural representations within the data collected
from platforms like TikTok, YouTube Shorts, and
Instagram Reels.
F.1
Methodology
We randomly sampled 2,614 images from our
dataset. A two-step pipeline was then applied:
1. Caption Generation: For each sampled im-
age, we utilized GPT-4o to generate a descrip-
tive caption. This step aimed to produce a

--- Page 14 ---

textual representation that more precisely cap-
tures the visual content of the image, facilitat-
ing subsequent cultural analysis.
2. Cultural Signal Extraction: Using the gener-
ated captions, we applied named entity recog-
nition (NER) and keyword matching tech-
niques. This process was designed to identify
mentions of specific cultural elements, includ-
ing but not limited to:
• Locations: e.g., “Seoul,” “Mecca”
• Traditional Clothing: e.g., “sari,” “han-
bok”
• Holidays: e.g., “Diwali,” “Ramadan”
• Scripts/Languages: e.g., “Arabic callig-
raphy”
• Other culturally relevant features and ar-
tifacts.
Based on the extracted signals, we created a culture-
labeled subset where each sample could be associ-
ated with one or more identified cultural categories.
F.2
Results
The aggregated results from the cultural signal ex-
traction process are summarized in Table 2.
Culture
Count
Percentage
Western
2054
78.6%
Japanese
364
13.9%
Korean
61
2.3%
Chinese
49
1.9%
Muslim
37
1.4%
Indian
37
1.4%
Arabic
12
0.5%
Others
183
7.0%
Total
2614
100.0%
Table 2: Distribution of Identified Cultural Categories
in the Sampled Dataset (N=2,614). Percentages are
rounded.
The distribution presented in Table 2 shows a
predominance of Western cultural signals (78.6%).
This is consistent with the global reach and con-
tent characteristics of the source platforms (Tik-
Tok, YouTube Shorts, and Instagram Reels), which,
while internationally utilized, often feature a signif-
icant volume of content reflecting Western cultural
contexts. Nevertheless, the dataset also captures no-
table representation from several non-Western cul-
tural spheres, including Japanese (13.9%), Korean
(2.3%), Chinese (1.9%), Muslim (1.4%), Indian
(1.4%), and Arabic (0.5%) cultural elements.
The current cultural distribution reflects the in-
herent, though skewed, diversity present on these
globally accessible social media platforms. While
the dataset provides a basis for studying VLM re-
sponses to a range of cultural stimuli, the observed
imbalance in representation is an important char-
acteristic to consider. Future work may explore
strategies for targeted data collection to enhance
the cultural balance and further broaden the in-
clusiveness of such datasets for cross-cultural AI
research.
G
Human Validation of Value Alignment
in Screenshots and Videos
To empirically assess the alignment between the
machine-assigned value labels and human percep-
tion, both for the selected screenshots and their
corresponding full video content, we conducted
a dedicated human validation study. This study
provides an independent measure of how well the
visual content (static images and dynamic videos)
reflects the intended Schwartz value dimensions.
G.1
Methodology
The human validation study was structured as fol-
lows:
1. Sample Selection: From our dataset, we
randomly selected 50 screenshot-video pairs
for each of the ten Schwartz value dimen-
sions (e.g., Benevolence, Tradition, Hedo-
nism). This resulted in a total of 500 unique
items for evaluation.
2. Annotation Task and Annotators: Three in-
dependent human annotators, familiar with
Schwartz’s value theory, were recruited. For
each item (a screenshot and its associated
video URL), annotators were tasked with mak-
ing two separate judgments based on the as-
signed value dimension:
• Judgment 1 (Screenshot): “Does this
screenshot reflect the given value of
[Value Name]?”
(Response options:
Yes/No/Not Sure)
• Judgment 2 (Video): “Does this video
(linked) reflect the given value of
[Value Name]?”
(Response options:
Yes/No/Not Sure)

--- Page 15 ---

Annotators were required to view the full
video before making their judgment for the
video content.
3. Survey Design and Order: The annotation
survey was designed to present these judg-
ments sequentially to mitigate order effects.
For each item, annotators first evaluated the
screenshot. Only after submitting this judg-
ment were they presented with the video URL
and asked to evaluate the video content against
the same value dimension. A visual example
of the survey interface is shown in Figure ??.
4. Data Aggregation: With 50 items per value,
10 value dimensions, and 3 annotators, this
process yielded 1,500 individual judgments
for screenshots and another 1,500 for videos.
5. Handling Inaccessible Video Content: In
instances where a video URL was no longer
accessible (e.g., due to content deletion or plat-
form restrictions), annotators were instructed
to mark their response for the video judgment
as “Not Sure.” These instances are accounted
for in the reported results.
G.2
Results
The aggregated human judgments on value align-
ment for both screenshots and their corresponding
videos are presented in Table 9. Percentages repre-
sent the proportion of responses for each category,
averaged across three annotators.
Across all ten value dimensions, we observed
strong agreement between human judgment and
the intended value labels for both screenshots and
full videos.
• On average, screenshot-based value alignment
received a 90.6% “Yes” rate from human an-
notators.
• Video-based value alignment achieved an
87.6% “Yes” rate.
The “Not Sure” responses were minimal for images
(average 1.00%) and slightly higher for videos (av-
erage 5.58%). The higher incidence of “Not Sure”
for videos is primarily attributed to instances of
unavailable video links at the time of annotation,
as detailed in the methodology.
G.3
Discussion
The findings from this human validation study pro-
vide strong empirical support for the value align-
ment of the collected content:
1. Screenshots as Reliable Indicators of Value:
The high average “Yes” rate (90.6%) for
screenshots demonstrates that the static im-
ages selected through our pipeline are gener-
ally perceived by human annotators as reliably
reflecting the intended Schwartz value dimen-
sions.
2. Consistency of Value Perception in Video
Content: Full video evaluations also yielded
a high average “Yes” rate (87.6%), indicat-
ing that the broader dynamic context of the
videos largely aligns with the value percep-
tion derived from the representative screen-
shots. The slight decrease compared to screen-
shots, alongside the higher “Not Sure” rate for
videos, can be attributed to factors such as
the dynamic and multifaceted nature of video
content, as well as the practical issue of video
accessibility over time.
3. Support for Benchmark Methodology: The
close agreement between human judgments
and the assigned value labels, for both image
and video modalities, supports the efficacy of
our content retrieval and labeling approach.
This suggests that the benchmark, while lever-
aging efficient screenshot-based processing,
captures content that is largely consistent with
human understanding of the targeted values.
This human validation ablation study therefore rein-
forces the suitability of the dataset for investigating
VLM responses to visual content associated with
diverse human values.

--- Page 16 ---

H
Inducing VLM’s Persona Detailed
Information
Table 3: Simple Strategy - TikTok
Dimension
GPT-4o
Gemini 1.5 pro
Qwen-VL-Plus
CogVLM
Claude
Related contents(<=50)(%)
7.6
20
6.0
45.2
15.8
Related contents(LAST 50)(%)
11.8
23.2
6.2
51.2
12.4
Change(%)
55.26
16
3.33
13.27
-21.52
Table 4: Questionnaire Strategy - TikTok
Dimension
GPT-4o
Gemini 1.5 pro
Qwen-VL-Plus
CogVLM
Claude
Related contents(<=50)(%)
3.6
10.8
19.6
66.2
12.7
Related contents(LAST 50)(%)
4.0
16.4
19.2
69
16
Change(%)
11.1
51.9
-2.0
4.2
26.3
Table 5: Simple Strategy - YouTube
Dimension
GPT-4o
Gemini 1.5 pro
Qwen-VL-Plus
CogVLM
Claude
Related contents(<=50)(%)
10
25
13.6
61
24.8
Related contents(LAST 50)(%)
9.6
27.2
13.4
64
22.6
Change(%)
-4.0
8.8
-1.47
4.9
-8.9
Table 6: Questionnaire Strategy - YouTube
Dimension
GPT-4o
Gemini 1.5 pro
Qwen-VL-Plus
CogVLM
Claude
Related contents(<=50)(%)
11.4
20.0
42
81
15.6
Related contents(LAST 50)(%)
12.8
23.4
42.8
81
21.2
Change(%)
12.3
17.0
1.9
0
34.9
Table 7: Simple Strategy - Instagram
Dimension
GPT-4o
Gemini 1.5 pro
Qwen-VL-Plus
CogVLM
Claude
Related contents(<=50)(%)
22.4
27.8
11.4
53.6
15.8
Related contents(LAST 50)(%)
20.2
22.8
9.8
49.4
16.8
Change(%)
-9.82
-18
-14
-7.8
6.33
Table 8: Questionnaire Strategy - Instagram
Dimension
GPT-4o
Gemini 1.5 pro
Qwen-VL-Plus
CogVLM
Claude
Related contents(<=50)(%)
13.4
15.8
46.8
56.4
8.6
Related contents(LAST 50)(%)
15.6
16.8
44
56.8
9.4
Change(%)
16.4
6.3
-6
0.7
8.5

--- Page 17 ---

Value
Yes (Image)
Yes (Video)
No (Image)
No (Video)
Not Sure (Image)
Not Sure (Video)
Benevolence
82.67
76.00
16.00
16.67
1.33
7.33
Tradition
94.67
96.00
4.67
1.33
0.67
2.67
Self-Direction
95.33
92.67
2.67
2.67
2.00
4.67
Achievement
88.67
78.00
10.67
11.33
0.67
10.67
Conformity
82.67
80.00
14.67
11.33
2.67
8.67
Hedonism
87.33
83.33
12.67
10.67
0.00
6.00
Security
94.00
92.67
6.00
4.00
0.00
3.33
Stimulation
96.00
97.33
3.33
1.33
0.67
1.33
Power
87.33
82.67
11.33
7.33
1.33
10.00
Universalism
97.33
97.33
1.33
0.67
1.33
2.00
Average
90.60
87.60
8.40
8.30
1.00
5.58
Table 9: Human Annotation Results for Value Alignment of Screenshots and Videos (Percentages).
Figure 12: Two examples of trials evaluating VLM’s preferences. For each trial, a social media short video is used,
and a screenshot is taken at the 2-second timestamp. The user then interacts with the VLM using a question-and-
answer format to assess the model’s attitude toward the screenshot’s content. In these examples, TikTok content and
the GPT-4o model are used for demonstration.

--- Page 18 ---

Figure 13: Example of two scenarios in inducing the VLM’s persona using the Simple strategy: when VLM
determines that the screenshot content aligns with the persona, and the user remains engaged with the content for 45
seconds. Conversely, if the VLM decides the content is not related to the persona, the user scrolls down immediately.

--- Page 19 ---

Figure 14: Example of inducing the VLM’s persona using the ISQ strategy: When the calculated score exceeds 60,
the Vision-Language Model (VLM) chooses to stay engaged with the content for 45 seconds before scrolling down.

--- Page 20 ---

Figure 15: Instructions provided to annotators to evaluate whether a single-frame screenshot accurately represents
the main content of a video. Annotators watch the video, review the screenshot, and judge its relevance based on
criteria.
Setting
Model
Achievement Benevolence Conformity Hedonism Power Security Self-direction Stimulation Tradition Universalism
VLM_answer
GPT-4o
94.0
94.0
96.0
98.0
100.0
90.0
98.0
98.0
92.0
94.0
Gemini 1.5 Pro
44.0
58.0
58.0
60.0
60.0
64.0
52.0
58.0
50.0
46.0
Claude 3.5 Sonnet
80.0
80.0
72.0
82.0
90.0
76.0
72.0
72.0
64.0
66.0
GPT-4o image description + LLMs
GPT-4o_text
94.0
92.0
88.0
82.0
96.0
88.0
94.0
98.0
94.0
88.0
Gemini 1.5 Pro_text
76.0
76.0
80.0
80.0
86.0
72.0
90.0
88.0
82.0
82.0
Claude 3.5 Sonnet_text
94.0
94.0
96.0
92.0
100.0
90.0
98.0
94.0
98.0
96.0
Gemini 1.5 Pro vision image description + LLMs
GPT-4o_text
90.0
94.0
88.0
90.0
90.0
86.0
92.0
94.0
88.0
86.0
Gemini 1.5-Pro_text
98.0
100.0
86.0
94.0
94.0
88.0
92.0
92.0
94.0
88.0
Claude 3.5 Sonnet_text
96.0
98.0
88.0
86.0
90.0
88.0
86.0
84.0
94.0
90.0
Claude 3.5 Sonnet image description + LLMs
GPT-4o_text
100.0
96.0
92.0
92.0
100.0
100.0
96.0
92.0
96.0
94.0
Gemini 1.5 Pro_text
100.0
98.0
100.0
100.0
98.0
100.0
96.0
94.0
100.0
98.0
Claude 3.5 Sonnet_text
100.0
96.0
96.0
98.0
100.0
100.0
98.0
94.0
96.0
100.0
Table 10: Value preference outcomes across different models and input settings on Value-Spectrum. The settings
include direct multi-modal responses from VLMs and combinations of image descriptions generated by different
VLMs with LLMs.

```
