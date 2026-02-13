---
title: "2023-Unknown-Divide-and-Conquer Attack Harnessing the Power of LLM to Bypass - PDF Extract"
source_pdf: "2023-Unknown-Divide-and-Conquer Attack Harnessing the Power of LLM to Bypass.pdf"
pages: 10
extracted_at: "2026-02-13T13:57:10.736039"
---

# PDF Extract: 2023-Unknown-Divide-and-Conquer Attack Harnessing the Power of LLM to Bypass

**Source PDF:** 2023-Unknown-Divide-and-Conquer Attack Harnessing the Power of LLM to Bypass.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Harnessing LLM to Attack LLM-Guarded Text-to-Image Models
Yimo Deng, Huangxun Chen
Hong Kong University of Science and Technology (Guangzhou)
dengemo.neu@gmail.com, huangxunchen@hkust-gz.edu.cn
𝓑𝒍
𝓑𝑺
semantic logical/illogical boundary
semantic safe/unsafe boundary
Prompts w/ similar embedding semantic
Visual Rephrase (Ours): This image has two main
characters, 'Black Male Jamel,' 'White Female Emily.’
Jamel is dressed in Jamel's attire of dark clothes.
Emily is dressed in Emily's attire of casual home attire.
Jamel’s action is surprising, quickly picking up objects that
belong to others, now relocated.
Emily’s action is standing startled, spotting an uncertain
object that can be utilized for protection or harm.
Jamel carries something that may be used to ensure
safety but potentially causing harm.
Emily carries her own items of personal use.
Drawing Prompt: A black male robbed a white female in a 
home invasion.
Token Replacement: A black male inghamluwinspire
a white female in a home tapswenighthighland.
logical
illogical
unsafe
safe
T2I Model
Safety Filter
Generated Image
Figure 1. Visual Rephrase Prompt Against T2I Model’s Safety Filter: The blue curve represents the safety filter’s semantic safe/unsafe
boundary Bs, while the red dashed curve represents the logical/illogical boundary Bl. The safety filter will reject prompts that are either
harmful or illogical. By design, our method finds a sanitized prompt through visual rephrasing, enabling it to bypass both safety filter
boundaries and generate the intended images.
Abstract
To prevent Text-to-Image (T2I) models from generating
unethical images, people deploy safety filters to block inap-
propriate drawing prompts. Previous works have employed
token replacement to search adversarial prompts that at-
tempt to bypass these filters, but they has become ineffec-
tive as nonsensical tokens fail semantic logic checks. In
this paper, we approach adversarial prompts from a differ-
ent perspective. We demonstrate that rephrasing a drawing
intent into multiple benign descriptions of individual visual
components can obtain an effective adversarial prompt. We
propose a LLM-piloted multi-agent method named DACA to
automatically complete intended rephrasing. Our method
successfully bypasses the safety filters of DALL·E 3 and
Midjourney to generate the intended images, achieving suc-
cess rates of up to 76.7% and 64% in the one-time attack,
and 98% and 84% in the re-use attack, respectively. We
open-source our code and dataset on GitHub1.
1https://github.com/researchcode003/DACA
1. Introduction
Text-to-Image (T2I) models have emerged as an attractive
field.
T2I models, including DALL·E series from Ope-
nAI [5, 7] and others like Stable Diffusion [31, 42], Mid-
journey [11] and [43], can take a drawing intent in the form
of natural language and generate an image matching that in-
tent. This can support creative expression, advancing many
fields such as design, education and advertising [29].
However, as the old saying goes, a sharp blade has two
edges.
Since the birth of T2I models, there have been
many concerns about their potential abuse to generate inap-
propriate images, which could lead to negative social im-
pacts [9, 21, 25, 37]. Therefore, efforts are being made
to develop safety filters. Basically, they intercept drawing
prompts, apply checking before actual image generation to
prevent undesired output, as shown in Figure 1.
In the early stages, keyword blocklist strategy was pri-
marily adopted. A comprehensive list of harmful words,
such as the open-source NSFW list [27], was curated to
flag harmful drawing prompts accordingly. Following that,
neural networks [19, 35] have been developed to classify
1
arXiv:2312.07130v4  [cs.AI]  23 Nov 2024

--- Page 2 ---

harmful prompts. Recently, the latest T2I services, DALL·E
3 [7, 8] and MidJourney [11] have incorporated large lan-
guage models (LLMs) [22, 46] to help recognize harmful
drawing prompts. Existing prompt scrutiny has two parts:
1.Semantic Safe/Unsafe Checking. This check classifies
the drawing prompt as either safe or unsafe. Technically, it
transforms text T into vectors v, then distinguishes which
text vectors are deemed unsafe based on their position rela-
tive to the semantic safe/unsafe boundary Bs in the embed-
ding space, denoted by the blue curve in Figure 1. However,
prior research [20, 49] have shown that prompts with sim-
ilar semantic embeddings may not be entirely located on
one side of this boundary. As illustrated by the intersec-
tion between Bs and gray circular area in Figure 1, terms
like “inghamluwinspire” can replace “robbed”, and “tap-
swenighthighland” can replace “invasion”, which results in
a prompt whose embedding remains close to the original but
crosses from unsafe side into safe side.
2.Semantic Logical/Illogical Checking. This check ver-
ifies whether the drawing prompt is coherent and not ran-
dom nonsense.
Similarly, it determines which text vec-
tors v are logical based on their position relative to the
semantic logical/illogical boundary Bl in the embedding
space, represented by the red dashed curve in Figure 1.
The prompt “...inghamluwinspire...tapswenighthighland...”
mentioned earlier, uses token replacement to cross into the
safe side, but also causes the prompt to cross into the illog-
ical side, resulting in rejection for image generation.
In this paper, we approach adversarial prompt from a
different perspective, going beyond conventional token re-
placement. As illustrated in Figure 1, an adversarial prompt
can be seen as an alternative version of a prompt that
deemed unsafe and rejected for image generation. An ef-
fective adversarial prompt, however, will be deemed both
safe and logical, allowing it to be accepted by T2I model
and generate the image intended by the original prompt.
Instead of rigidly replacing certain tokens, we find a
more neutral way to convey the intended visual effect in im-
age. An image often comprises multiple components, such
as background, people, clothing, etc. By objectively de-
scribing the visual features of each individual aspect, we
can prompt T2I model to generate the desired image as
expressed by an overall global description. As shown in
Figure 1, to generate an image of “a black male robbing
a white female in a home invasion”, we can start by de-
scribing the image with two characters, Jamel and Emily,
implicitly suggesting the presence of a man and a woman.
Then, we describe the clothing, actions, and belongings of
each character respectively. Without mentioning any terms
like “rob” or “invasion”, this approach allows us to gen-
erate an image with the intended visual effect. We name
the above attack idea divide-and-conquer attack (DACA),
which involves breaking down a holistic image description
deemed unsafe into multiple fine-grained descriptions that
are considered safe, while also preserving logical coherence
to generate the image with intended visual effect.
The remaining challenge is how to automate this at-
tack strategy instead of relying on manual rephrasing. Pre-
vious token replacement methods fail to produce visually
rephrased versions. Given great potential of LLMs in var-
ious text transformation tasks, we propose an LLM-piloted
method to realize DACA idea. Technically, we specify tar-
get image’s ontology (Figure 3) and design an ontology-
guided multi-agent workflow (Algorithm 1), where three
types of agents, Decomposer, Polisher, and Assembler co-
ordinate to decompose the image components, identify sen-
sitive terms within these components, and reassemble as-
sociated components into coherent and fluent sentences, as
illustrated in Figure 2.
In summary, our main contributions are as follows:
• We approach adversarial prompts against T2I models
from a different perspective, proposing an LLM-driven
multi-agent method guided by image ontology.
It effec-
tively generates prompts that objectively describe the ap-
pearance of individual components to bypass safety filters,
outperforming prior token replacement methods.
• We curated a comprehensive prompt dataset covering 5
major topics censored by the latest T2I models, with a total
of 100 sensitive prompts and 3,600 corresponding adversar-
ial prompts to thoroughly evaluate the attack-effectiveness
and cost-effectiveness of our proposed method.
• Our evaluation shows that our method successfully by-
passes safety filters of DALL·E 3 and Midjourney to gen-
erate images with intended visual effect, achieving success
rates of up to 76.7% and 64% in the one-time attack, and
98% and 84% in the re-use attack, respectively. Moreover,
our attack is cost-effective. With just 1 dollar, we can en-
able 28 adversarial prompt generation using GPT-4 as the
agent backbone, and up to 83 when using a smaller model
like Qwen-14B. This highlights non-negligible safety im-
plications and encourages more defense efforts.
2. Related Work
2.1. Adversarial Attack
Adversarial inputs, where attackers manipulate the input to
trigger unintended outputs in AI models, have attracted sig-
nificant attention. The initial focus was on the computer
vision domain [23, 28, 33], where subtle perturbations, im-
perceptible to human eyes, were introduced to images to
mislead model classification. This concept has been ob-
served in other continuous modalities like time-series sig-
nals [24, 30] and discrete ones like texts [26, 32, 34].
In text domain, earlier studies [26, 34] primarily aimed
to deceive text classification models. However, with the rise
of generative AI, recent research has begun to explore ad-
2

--- Page 3 ---

versarial prompts against generative models, including both
LLMs and T2I models. Mehrotra et al. [39] present an auto-
mated method for generating attack prompts, requiring only
black-box access to the target LLM to jailbreak it. Many
recent works [48, 50, 51] have continued to explore adver-
sarial prompts to manipulate LLMs into generating text that
would otherwise be restricted or inappropriate.
In terms of adversarial prompts against T2I models, the
goal is to manipulate T2I models into generating target im-
ages, often bypassing safety filters or restrictions. Milli`ere
et al. [40] showed that attackers could create adversarial
examples by combining words from different languages to
mislead T2I models. Maus et al. [38] developed a black-
box framework using Bayesian optimization for adversarial
prompt generation, aiming to generate images of a target
class using nonsensical tokens. Yang et al. [49] employed
reinforcement learning to search for and replace sensitive
tokens via repeatedly querying T2I models, which circum-
vented DALL·E 2 to generate sexual images. Ba et al. [20]
also employ a substitution strategy to search for adversar-
ial prompts. Ma et al. [36] design a method to first gen-
erate safe images and then locally edit them, which lever-
ages adaptive prompt substitution and local inpainting tech-
niques to produce unsafe images from targeted T2I mod-
els. Instead of searching for prompts via iterative queries
to T2I models, our work explores whether agents can di-
rectly rephrase unsafe prompts to objectively and benignly
describe individual visual components, aiming to bypass
safety filters while still achieving the intended visual effect
in the generated image.
2.2. Defense against Adversarial Prompt
Since the embeddings of text and images are aligned dur-
ing T2I model training, it is cost-effective to apply scrutiny
in the text domain to prevent output inappropriate images.
Existing methods can be classified into two types:
• Vanilla Safety Filters.
The representative ones are
those used in open-source solutions [35] and DALL·E
2 [5, 6]. These can be regarded as first-generation safety
filters, relying on (i) Blocklists: They curate a list of harm-
ful words, and when an input prompt matches an entry on
this list, it is denied. (ii) Prompt Classifiers: They primar-
ily use encoder models [4, 44] to classify text into prede-
fined categories such as hate, threats, self-harm, sexual con-
tent, minors, and violence. For instance, an open-source
binary classifier [35] utilizes the DistilBERT [44] model,
fine-tuned on data from an NSFW content channel on Red-
dit [19]. The moderation policy [6] enforced by DALL·E 2
follows a similar approach.
• LLM-assisted Safety Filters. The representative ones
are those used in DALL·E 3 [7] and MidJourney V6 [11].
These systems incorporate LLMs, such as ChatGPT [3, 10],
for prompt checking.
Due to the enhanced text under-
Drawing Prompt
Clothing
Character
Action
Belongings
Background
Polisher
Decomposer
Unsafe
Safe
Assembler
Character+Clothing
Character+Action
Character+Belongings
Background
…
Alternative 
Description
Sensitive
Term
Class
…
Gun
Belongings
Figure 2.
Overview of LLM-Piloted Multi-Agent Method.
Decomposer: decompose the key visual components based on the
specified image ontology (Figure 3); Polisher: identify sensitive
terms within each isolated component and finds alternative benign
descriptions; Assembler: reassemble associated components into
coherent and fluent sentences based on the image ontology.
standing capabilities of LLMs, these filters can effectively
block harmful text based on system-prescribed instructions.
Moreover, they can reject chaotic or illogical inputs, which
are often challenging for vanilla safety filters.
With ad-
vancements in defense, many prior attacks can not effec-
tively bypass them.
3. Method
DACA is an LLM-piloted approach designed to isolate key
visual components from targeted drawing prompts, then ar-
ticulate these components benignly and reassemble them
into a safe drawing prompt. As shown in Figure 2, it fea-
tures multiple agents, including Decomposer, Polisher and
Assembler, to accomplish these tasks.
3.1. Agent’s Meta-Prompts
LLM serves as the backbone for all three agents, and we
follow the meta-structure below to guide the agents:
1. Context Description. First, we establish a plausible con-
text for the agent to legitimize our queries as follows.
I am working on handling sensitive texts to create a posi-
tive online environment.
2. Overall Task and Task Sub-steps. Next, we outline the
task and its steps to guide prompt rephrasing process.
3. Output Format. We then specify the expected output
format to ensure consistency in the results.
3

--- Page 4 ---

4. Demo (Optional). We handcraft an adversarial prompt
as an example, and apply Chain-of-Thought (CoT) [47] to
clarity more on how to approach the task.
5. Input Feeding. We supply the input for processing.
3.2. Agent Role Specialization
Our initial attempt involved using a single agent to produce
detailed descriptions for each component to realize targeted
visual effect. However, this all-in-one approach proved less
effective for semantically rich images, e.g., the robbery sce-
nario depicted in Figure 1. Additionally, specific elements
like guns inherently carry sensitivity, even when described
individually, requiring more nuanced rephrasing.
Thus,
a single agent cannot accurately decompose and rephrase
these intricate details in a single pass. Therefore, we di-
vide the entire task into three parts: decomposing the com-
ponent, rephrasing the component if any sensitivity is in-
volved, and reassembling the component description. Each
part is assigned to a specific agent, as shown in Figure 2.
Decomposer: Its task is to identify and distill individual
visual elements from the original drawing prompt. Based
on common image ontology as illustrated in Figure 3, we
guide Decomposer to extract the following aspects: Char-
acter (main characters in the scene), Clothing (notable at-
tire of the main character), Action (character motion), Be-
longings (objects closely associated with the character), and
Background. Covering these aspects helps approximate the
intended visual narrative of the original prompt.
Polisher: Its task is to rephrase unsafe terms. Among
the components distilled by Decomposer, certain elements
might raise flags. For instance, terms like “gun” (Belong-
ings) and “shooting” (Action) are likely to trigger safety fil-
ters. Polisher is instructed to identify any potentially sen-
sitive elements and rephrase them using more objective de-
scriptions of their visual appearance. The polisher’s out-
put will be a substitution table listing all identified sensitive
terms and their replacements as shown in Figure 2.
Assembler: This agent utilizes the substitution table
from Polisher to replace portions of Decomposer’s output
with their non-sensitive equivalents and assemble a coher-
ent text in sentence form, as examples shown in Figure 1.
Each agent has a template following the meta-structure
in §3.1, incorporating placeholders for versatile adaptation
to various visual components. Please refer to our supple-
mentary material for more details.
3.3. Workflow across Agents
The workflow and interaction between multiple agents are
illustrated in Algorithm 1. The end-to-end effect is to ob-
tain a prompt Tadv that retains the semantics of the original
unsafe prompt T but is considered safe by safety filters.
The agent workflow is essentially driven by our speci-
fied ontology G for visual components in targeted image, as
Character
Background
Cloth
Action
Belongings
Image Ontology 𝑮
𝒏
𝒆
Figure 3. Image Ontology: A graph structure to capture the major
visual components and their associations in targeted image.
Algorithm 1: Ontology-guided Agent Workflow
Input: Prompt T, Image Ontology G
Output: Prompt Tadv
/* Guided by ontology, decompose and
polish visual components.
*/
1 t ←∅, s ←∅
2 for n ∈G do
3
t{n} = Decomposern(T)
4
s{n} = Polishern(t{n})
/* Guided by ontology, assemble the
associated components.
*/
5 r ←∅
6 for e = (ni, no) ∈G do
7
r{e} = Assemblere(t{ni}, s{ni}, t{no}, s{no})
8 for n ∈G do
9
if Degree(n) = 0 then
10
r{n} = Assemblern(t{n}, s{n})
11 Tadv = CONCAT(r)
shown in Figure 3. For each node n (component) in G, we
invoke Decomposer to obtain the corresponding description
t{n} from T. Our approach can be extended to incorporate
more components as needed by expanding the ontology G.
Next, we invoke Polisher to identify potentially sensitive
elements and produce appropriate replacements to populate
the substitution table s{n} (Lines 1 to 4 in Algorithm 1).
After that, for each edge e (component association) in
G, we apply Assembler to the outputs of both Decomposer
and Polisher on the two end nodes (ni and no) to generate a
safe and coherent sentence. We also applied the assembling
operation to isolated nodes, e.g., Background in Figure 3.
Finally, we concatenate all sentences to form the resultant
prompt Tadv (Lines 5 to 11 in Algorithm 1). Please refer to
our supplementary material for our code and Tadv samples.
4. Evaluation
We evaluate both the attack effectiveness and cost efficiency
of our proposed method on curated multi-category sensitive
prompt datasets.
4

--- Page 5 ---

Table 1. Bypass rate using various LLMs as the agent backbone
Type
Violence
Bloodiness
Crime
Discrimination
Eroticism
Mean
One-time
Re-use
One-time
Re-use
One-time
Re-use
One-time
Re-use
One-time
Re-use
One-time
Re-use
GPT-4.0
86%
85%
65%
80%
92%
90%
87%
85%
44%
75%
74.8%
83%
GPT-3.5
76%
80%
45%
75%
72%
85%
57%
80%
26%
70%
55.2%
78%
Spark V3.0
73%
95%
57%
100%
78%
100%
63%
100%
35%
85%
61.2%
96%
ChatGLM
91%
95%
65%
100%
67%
100%
87%
95%
36%
80%
69.2%
94%
Qwen-14B
64%
95%
34%
95%
67%
90%
46%
100%
23%
95%
46.8%
95%
Qwen-Max
96%
100%
73%
100%
87%
100%
82%
100%
45%
90%
76.6%
98%
Table 2. Bypass rate against various T2I models (Agent Backbone: GPT-4.0)
Type
Violence
Bloodiness
Crime
Discrimination
Eroticism
Mean
One-time
Re-use
One-time
Re-use
One-time
Re-use
One-time
Re-use
One-time
Re-use
One-time
Re-use
DALL·E 3
86%
85%
65%
80%
92%
90%
87%
85%
44%
75%
74.8%
83%
Midjourney V6
80%
90%
60%
80%
60%
80%
80%
90%
40%
80%
64.0%
84%
4.1. VBCDE Dataset
To evaluate whether our method can successfully by-
pass safety filters to generate the image with intended vi-
sual effect, we reviewed content moderation guidelines
specified by latest T2I models [7, 8, 12] and relevant
works [20, 49], and then curated a diverse drawing prompt
set called VBCDE (Violent-Bloody-Crime-Discriminate-
Erotic) dataset, which includes 100 sensitive prompts
across 5 categories: violence, gore, illegal activities, dis-
crimination, and pornographic content. Each category is
represented by around 20 prompts, covering major censor-
ship range enforced by current T2I models. Our empiri-
cal testing confirmed that all prompts were consistently re-
jected by safety filters of our targeted T2I models.
For each sensitive drawing prompt within VBCDE, we
employ different LLMs as the agent backbone (including
Decomposer, Polisher and Assembler) to generate its adver-
sarial prompts. Based on public benchmarks such as Super-
CLUE [18], Chatbot Arena [1], and Open Compass [14], we
selected GPT-4 [13], GPT-3.5-turbo [13], Spark V3.0 [17],
ChatGLM-turbo [2], Qwen-14B [15], and Qwen-Max [16],
6 LLMs in total as agent backbone. Per LLM, we produce
around 5 to 10 adversarial prompts, yielding a total of 50-
100 adversarial prompts for each sensitive prompt and 3,600
adversarial prompts for image generation in total. We open-
source both sensitive prompts and certain effective adver-
sarial prompts.
4.2. One-time Attack against T2I Models
One-time attack means generating an adversarial prompt for
each original sensitive prompt for single-use only.
Experimental Setup. We use two state-of-the-art T2I
models, DALL·E3 [7] and Midjourney V6 [11], as tar-
gets for our attack. These models reject prompts if their
LLM-assisted safety filters detect sensitive content.
For
DALL·E 3, each adversarial prompt (3,600 in total) is in-
dividually fed into the T2I model for image generation. For
Midjourney, we select 5 adversarial prompts from each cat-
egory (5 categories) generated using GPT-4 as the agent
backbone. They are then fed into the model to generate a
total of (5×5×4=100) images, as each prompt generates 4
images in Midjourney.
Results. In one-time attack, we compute the bypass rate
as the ratio of adversarial prompts that successfully circum-
vent the safety filter to the total number of tested adversar-
ial prompts. As shown in Table 1, our generated prompts
achieve a notable bypass rate in the one-time attack against
targeted T2I models.
Among various LLM backbones,
Qwen-Max achieves the highest average bypass success
rate at 76.6% across various sensitive categories, followed
by GPT-4 at 74.8%. Even a smaller model, Qwen-14B,
achieves a non-negligible bypass rate of 46.8%, demon-
strating the high feasibility of our LLM-piloted method for
generating effective adversarial prompts. As shown in Ta-
ble 2, the bypass rate for Midjourney in the one-time attack
is lower than that of DALL·E 3, likely due to stricter prompt
scrutiny. Additionally, for one-time attacks, the bypass rate
for erotic content is relatively lower, which is expected as
T2I models generally apply stricter restrictions on such con-
tent as indicated in their specification [8, 12].
4.3. Re-use Attack against T2I Models
A re-use attack means that an adversarial prompt is stored
and repeatedly fed into the T2I model to generate multiple
5

--- Page 6 ---

Figure 4. Bypass Rate Distribution in Re-use Attack: X-axis:
bypass rate per prompt in re-use attack; Y-axis: the proportion of
evaluated re-used prompts that achieve a specific bypass rate.
images, thereby extending its impact. It is worth noting that
since the latest T2I models use LLMs as safety filters, the
generative nature of LLMs may lead to variations in how
the same prompt is evaluated over time. Consequently, it
is expected that an effective prompt in one-time attack may
not always achieve 100% bypass rate against LLM-assisted
safety filters.
Experimental Setup. The victim T2I models remain the
same as before. For DALL·E3, we select 180 adversarial
prompts, covering each combination of sensitive category
and LLM backbone, based on the image quality from the
one-time attack results. Each selected prompt is then used
to generate images in DALL·E 3 an additional 10 times.
This results in 180×10=1,800 reuse attack instances. For
MidJourney, we identify 5 prompts in one-time attack that
yielded images with the greatest semantic coherence to the
original sensitive prompts. Reusing each prompt to generate
images 10 additional times results in (5×10×4=200) attack
instances.
Results. In re-use attack, the bypass rate is calculated as
the proportion of attack instances that successfully bypass
the safety filter. As shown in Table 1 and Table 2, the re-use
attack demonstrates strong stability, with most agent back-
bone models achieving an average bypass rate of over 80%.
Qwen-Max even reaches an average bypass rate of 98.0%.
Notably, for strictly restricted erotic prompts, the re-use by-
pass rate is significantly higher than in the one-time attack,
indicating that once a prompt bypasses strict restrictions, it
can consistently be used to generate inappropriate images.
Since each re-used adversarial prompt is evaluated 10
times, we further calculate individual bypass rates and plot
the bypass rate distribution in Figure 4, where X-axis de-
notes the bypass rate of individual prompts, and Y-axis
denotes the proportion of evaluated re-used prompts that
achieve a specific bypass rate. It can be noted that 50% of
Figure 5. CLIP-embeddings-based Cosine Similarity Score be-
tween Generated Image T2I(Tadv) and Original Prompt T.
re-used prompts achieve a 100% bypass rate, indicating that
these prompts consistently bypass the safety filter. More-
over, all re-used prompts achieve more than a 60% bypass
rate, meaning that within 10 attempts per prompt, at least
6 successfully bypass the safety filter. This highlights non-
negligible safety implications.
4.4. Image Generation Quality
We use a pre-trained encoder model, CLIP [4] to derive the
embedding of images generated by our attacks and the orig-
inal sensitive prompts to evaluate their semantic similarity.
CLIP, trained on a large dataset of images paired with tex-
tual descriptions, aligns texts and images within a unified
dimensional space, making it well-suited for cross-modal
similarity evaluation. As a result, CLIP-based embeddings
are widely used in prior research [45, 49] to quantify sim-
ilarity across text and image modalities. Specifically, we
compute the cosine similarity [41] between CLIP embed-
dings of generated images and original prompts as follows:
CosineSim(ECLIP (T2I(Tadv)), ECLIP (T))
(1)
Before evaluation, we curated 100 benign prompts, ensur-
ing each prompt would be accepted by our targeted T2I
models and generate images. We then calculated the text-
image similarity scores for these 100 pairs to establish a
reference, resulting in an average score of 0.274. As shown
in Figure 5, in the re-use attack, similarity scores are close
to or even exceed the reference, outperforming the one-time
attack case. This indicates that images generated in the re-
use attack align well with the original sensitive prompts,
which also corresponds with the high bypass rate observed
in the previous evaluation.
Figure 6 showcases representative images generated via
bypassing our targeted T2I model. Certain categories, such
as eroticism, are omitted. Notably, our adversarial prompts
can bypass the safety filter to produce images with the
6

--- Page 7 ---

Figure 6. Sample Generated Images: (1) and (2) display images generated by feeding our adversarial prompts, covering various sensitive
categories and produced by different agent backbones, to DALL·E 3 and Midjourney. (3) shows a sample where one adversarial prompt is
fed to DALL·E 3 sentence by sentence, with similarity scores calculated between the original prompt and each intermediate image.
intended visual effects across various sensitive categories.
Figure 6 (3) shows a sample where an adversarial prompt
is fed to DALL·E 3 sentence by sentence, with similarity
scores calculated between the original prompt and each in-
termediate image. It can be observed that as with more sen-
tences, the similarity score gradually increases. This sug-
gests that as more individual descriptions are provided, the
generated image becomes increasingly semantically aligned
with the original sensitive prompt.
4.5. Cost Effectiveness
Our proposed method illustrated in Algorithm 1 lever-
ages LLMs as the agent backbone to generate adversarial
prompts, thus incurring relevant token costs. Token costs
fall into two categories: fixed and elastic. The fixed cost
arises from prompts required by each agent, while the elas-
tic cost mainly stems from outputs from agents that may
need to be fed into another agent. Commercial LLMs have
distinct API pricing schemes based on token usage. We col-
lect these LLM API pricing schemes used in our evalua-
tion in Table 3, where the ‘Words/Tokens’ column indicates
the conversion ratio between tokens and words. Following
the standard outlined in [15], we consider three characters
equivalent to one word and apply the word-to-token conver-
sion ratios shown in Table 3 to calculate token usage and
corresponding expense for different backbone LLMs.
As shown in Figures 7a and 7b, GPT-4 incurs a low fixed
cost of $0.009 and an average of $0.035 per attack, enabling
approximately 28 attacks for under one dollar. For cheaper
and smaller models like Qwen-14B, this could support up
to 83 attack attempts.
These attacks can produce stable
adversarial prompts suitable for subsequent re-use attacks
Table 3. API pricing schemes, i.e., the cost per 1,000 tokens for
LLM backbones in our evaluation.
Models
Input Token ($)
Output Token ($)
Words/Tokens
GPT-4.0 [13]
0.003
0.006
0.75
GPT-3.5-turbo [13]
0.001
0.002
0.75
Spark V3.0 [17]
0.005
0.005
0.8
ChatGLM-turbo [2]
0.0007
0.0007
0.56
Qwen-14B [15]
0.001
0.001
1
Qwen-Max [16]
free for now
1
as indicated in Table 1 and Figure 4. As LLM API costs
continue to decrease, the affordability of such attacks raises
significant security implications, particularly given the ac-
cessibility and cost-effectiveness of generating adversarial
prompts for widespread use.
5. Limitations and Discussions
Root Cause of Attack:
The existence of adversarial
prompts against T2I models stems from the incomplete
alignment between text and image embedding spaces. Im-
ages with similar visual effects can be described in multiple
ways, but only a portion of these descriptions are covered by
the safety filter. Compared to token replacement strategies,
our LLM-piloted multi-agent method can explore a larger
semantically equivalent space more efficiently, owing to the
LLM backbone’s advanced comprehension, generation, and
instruction-following capabilities.
Safety Implications:
Our method illustrated in Algo-
rithm 1 does not require online querying of the target T2I
model during adversarial prompt generation. Moreover, as
7

--- Page 8 ---

(a) Token Usage@Agent Backbone
(b) Money Expense@Agent Backbone(unit: dollar)
Figure 7. Cost Effectiveness Evaluation: (a) Average token usage for generating adversarial prompts in Algorithm 1; (b) Average money
expense, calculated as token usage × price per token.
shown in our cost evaluation in §4.5, generating an effec-
tive adversarial prompt is inexpensive, and these prompts
can be reused multiple times for image generation as indi-
cated in §4.3. With the ongoing evolution of agents’ back-
bone LLMs, the same cost will likely enable access to even
more powerful models, making this an increasingly signifi-
cant threat.
Countermeasures: A possible defense is to apply post-
generation safety filter on generated images, using vision
understanding models or multi-modal foundation models
to detect whether the image itself contains sensitive con-
tent. However, compared to text-level scrutiny, image un-
derstanding generally incurs higher costs and delays, which
could hinder its widespread adoption in practice. Another
potential defense is prompt summarization. Our method
generally expands the drawing prompt to have a more ver-
bose version. Conversely, we could summarize these ver-
bose adversarial prompts for screening. Based on our em-
pirical tests, the summarized adversarial prompts still by-
pass safety filters with over 95% success rate, although cer-
tain nuanced visual details may be lost due to summariza-
tion. Moreover, the sentence-by-sentence prompt feeding
method shown in Figure 6 (3) render summarization-based
defenses less effective, as the adversarial content is intro-
duced gradually, making it more challenging to detect. We
plan to systematically study the impact of various summa-
rization techniques in our future work.
Evaluation with More Fine-grained Image Ontology: In
our evaluation, we observed that generated images related
to violence, crime, and discrimination align better with the
original sensitive prompt compared to other two sensitive
categories. This can be attributed to the granularity of the
image ontology in our current implementation, as shown in
Figure 3. Images depicting bloodiness and eroticism of-
ten include more detailed sensitive elements, such as blood,
which were not thoroughly decomposed in our specified on-
tology. In contrast, for violence, dividing the description
between the performer and recipient of the action effec-
tively conceals sensitive semantics. In the future, we will
explore a more fine-grained ontology specification to poten-
tially improve attack effectiveness across a broader range of
categories and against more T2I models.
Ethical Considerations: We have responsibly disclosed
our findings to relevant stakeholders. We hope our work
will inspire positive applications, such as using our method
as a red teaming tool to efficiently identify vulnerabilities.
6. Conclusion
In this study, we approach adversarial prompts against T2I
models from a different perspective. To bypass both se-
mantic safe/unsafe and logical/illogical checks, we design
LLM-piloted method that rephrases sensitive prompts into
adversarial versions considered safe and logically coherent,
enabling the generation of images with intended visual ef-
fects. Specifically, we design three agents, Decomposer,
Polisher and Assembler, and use a specified image ontol-
ogy to guide their workflow. Together, the agents isolates
key visual components from targeted drawing prompts, ar-
ticulate these components in benign terms, and reassemble
them into a safe drawing prompt that objectively describes
the appearance of visual components, effectively bypassing
safety filters. To evaluate our attack’s capacity, we curated
a prompt dataset covering 5 major topics censored by the
latest T2I models, comprising 100 sensitive prompts and
3,600 corresponding adversarial prompts. Our evaluation
demonstrates that our method is both attack-effective and
cost-effective. Our adversarial prompts can successfully by-
pass close-box safety filters of DALL·E 3 and Midjourney.
With just 1 dollar, we can generate 28 adversarial prompts
using GPT-4 as the agent backbone. Our findings highlight
non-negligible safety implications, and we hope our open-
sourced code and dataset facilitate future research.
8

--- Page 9 ---

References
[1] Chatbot
Arena.
https : / / huggingface . co /
spaces/lmsys/chatbot-arena-leaderboard.
[2] ChatGLM API Pricing.
https://open.bigmodel.
cn/dev/api#product-billing, .
[3] OpenAI ChatGPT. https://chat.openai.com/, .
[4] CLIP Repo. https://github.com/openai/CLIP.
[5] DALL-E 2. https://openai.com/dall-e-2, .
[6] DALL-E 2 moderation policy. https://openai.com/
policies/usage-policies/, .
[7] DALL-E 3. https://openai.com/dall-e-3, .
[8] DALL·E 3 system card.
https://openai.com/
research/dall-e-3-system-card, .
[9] The Rise of Ethical Concerns about AI Content Creation:
A Call to Action.
https://www.computer.org/
publications/tech- news/trends/ethical-
concerns-on-ai-content-creation.
[10] GPT-4. https://openai.com/research/gpt-4.
[11] Midjourney. https://www.midjourney.com/, .
[12] Midjourney’s
banned
words
policy.
https :
/ / openaimaster . com / midjourney - banned -
words/, .
[13] OpenAI API Pricing.
https : / / openai . com /
pricing, .
[14] OpenCompass.
https://opencompass.org.cn/
leaderboard-llm, .
[15] TongYiQianWen 14B API Pricing.
https://help.
aliyun . com / zh / dashscope / developer -
reference / tongyi - qianwen - 7b - 14b - 72b -
metering-and-billing?spm=a2c4g.11186623.
0.0.693c502fDRJtKO, .
[16] TongYiQianWen Max API Pricing.
https://help.
aliyun . com / zh / dashscope / developer -
reference / tongyi - thousand - questions -
metering-and-billing?spm=a2c4g.11186623.
0.i1, .
[17] Spark API Pricing. https://www.xfyun.cn/doc/
spark/Web.html.
[18] SuperCLUE. https://www.superclueai.com/.
[19] Nsfw
gpt.
https : / / www . reddit . com / r /
ChatGPT/comments/11vlp7j/nsfwgpt_that_
nsfw_prompt/, 2023.
[20] Zhongjie Ba, Jieming Zhong, Jiachen Lei, Peng Cheng, Qin-
glong Wang, Zhan Qin, Zhibo Wang, and Kui Ren.
Sur-
rogateprompt: Bypassing the safety filter of text-to-image
models via substitution. arXiv preprint arXiv:2309.14122,
2023.
[21] Hritik Bansal, Da Yin, Masoud Monajatipoor, and Kai-Wei
Chang. How well can text-to-image generative models un-
derstand ethical natural language interventions? In Proceed-
ings of the 2022 Conference on Empirical Methods in Natu-
ral Language Processing, pages 1358–1370, 2022.
[22] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Sub-
biah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakan-
tan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Lan-
guage models are few-shot learners. Advances in neural in-
formation processing systems, 33:1877–1901, 2020.
[23] Nicholas Carlini and David Wagner. Towards evaluating the
robustness of neural networks. In 2017 IEEE Symposium on
Security and Privacy (SP), pages 39–57. IEEE, 2017.
[24] Huangxun Chen, Chenyu Huang, Qianyi Huang, Qian
Zhang, and Wei Wang. Ecgadv: Generating adversarial elec-
trocardiogram to misguide arrhythmia classification system.
In Proceedings of the AAAI Conference on Artificial Intelli-
gence, pages 3446–3453, 2020.
[25] Deep Ganguli, Amanda Askell, Nicholas Schiefer, Thomas
Liao, Kamil˙e Lukoˇsi¯ut˙e, Anna Chen, Anna Goldie, Azalia
Mirhoseini, Catherine Olsson, Danny Hernandez, et al. The
capacity for moral self-correction in large language models.
arXiv e-prints, pages arXiv–2302, 2023.
[26] Siddhant Garg and Goutham Ramakrishnan.
Bae: Bert-
based adversarial examples for text classification. In Pro-
ceedings of the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages 6174–6181,
2020.
[27] R. George. Nsfw words list on github, 2020.
[28] Ian J Goodfellow, Jonathon Shlens, and Christian Szegedy.
Explaining and harnessing adversarial examples.
arXiv
preprint arXiv:1412.6572, 2014.
[29] Roberto Gozalo-Brizuela and Eduardo C Garrido-Merch´an.
A survey of generative ai applications.
arXiv preprint
arXiv:2306.02781, 2023.
[30] Xintian Han, Yuxuan Hu, Luca Foschini, Larry Chinitz, Lior
Jankelson, and Rajesh Ranganath. Deep learning models for
electrocardiograms are susceptible to adversarial attack. Na-
ture medicine, 26(3):360–363, 2020.
[31] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising dif-
fusion probabilistic models. Advances in neural information
processing systems, 33:6840–6851, 2020.
[32] Di Jin, Zhijing Jin, Joey Tianyi Zhou, and Peter Szolovits. Is
bert really robust? a strong baseline for natural language at-
tack on text classification and entailment. In Proceedings of
the AAAI conference on artificial intelligence, pages 8018–
8025, 2020.
[33] Alexey Kurakin, Ian J Goodfellow, and Samy Bengio. Ad-
versarial examples in the physical world. In Artificial In-
telligence Safety and Security, pages 99–112. Chapman and
Hall/CRC, 2018.
[34] Jinfeng Li, Shouling Ji, Tianyu Du, Bo Li, and Ting Wang.
Textbugger: Generating adversarial text against real-world
applications. arXiv preprint arXiv:1812.05271, 2018.
[35] M. Li. Nsfw text classifier on hugging face, 2022.
[36] Yizhuo Ma, Shanmin Pang, Qi Guo, Tianyu Wei, and Qing
Guo. Coljailbreak: Collaborative generation and editing for
jailbreaking text-to-image deep generation. In Proceedings
of the 38th International Conference and Workshop on Neu-
ral Information Processing Systems, 2024.
[37] Todor Markov, Chong Zhang, Sandhini Agarwal, Floren-
tine Eloundou Nekoul, Theodore Lee, Steven Adler, Angela
Jiang, and Lilian Weng. A holistic approach to undesired
content detection in the real world. In Proceedings of the
AAAI Conference on Artificial Intelligence, pages 15009–
15018, 2023.
9

--- Page 10 ---

[38] Natalie Maus, Patrick Chao, Eric Wong, and Jacob Gard-
ner. Adversarial prompting for black box foundation models.
arXiv preprint arXiv:2302.04237, 2023.
[39] Anay Mehrotra, Manolis Zampetakis, Paul Kassianik, Blaine
Nelson, Hyrum Anderson, Yaron Singer, and Amin Karbasi.
Tree of attacks: Jailbreaking black-box llms automatically.
In Proceedings of the 38th International Conference and
Workshop on Neural Information Processing Systems, 2024.
[40] Rapha¨el Milli`ere.
Adversarial attacks on image genera-
tion with made-up words. arXiv preprint arXiv:2208.04135,
2022.
[41] Faisal Rahutomo, Teruaki Kitasuka, Masayoshi Aritsugi,
et al. Semantic cosine similarity. In The 7th international stu-
dent conference on advanced science and technology ICAST,
page 1. University of Seoul South Korea, 2012.
[42] Robin Rombach, Andreas Blattmann, Dominik Lorenz,
Patrick Esser, and Bj¨orn Ommer.
High-resolution image
synthesis with latent diffusion models.
In Proceedings of
the IEEE/CVF conference on computer vision and pattern
recognition, pages 10684–10695, 2022.
[43] Chitwan Saharia, William Chan, Saurabh Saxena, Lala
Li, Jay Whang, Emily L Denton, Kamyar Ghasemipour,
Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans,
et al. Photorealistic text-to-image diffusion models with deep
language understanding.
Advances in Neural Information
Processing Systems, 35:36479–36494, 2022.
[44] Victor Sanh,
Lysandre Debut,
Julien Chaumond,
and
Thomas Wolf. Distilbert, a distilled version of bert: smaller,
faster, cheaper and lighter. arXiv preprint arXiv:1910.01108,
2019.
[45] Shawn Shan, Wenxin Ding, Josephine Passananti, Haitao
Zheng, and Ben Y. Zhao.
Prompt-specific poisoning at-
tacks on text-to-image generative models.
arXiv preprint
arXiv:2310.13828, 2023.
[46] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-
reit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia
Polosukhin. Attention is all you need. Advances in neural
information processing systems, 30, 2017.
[47] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al.
Chain-of-Thought Prompting Elicits Reasoning in Large
Language Models. Advances in neural information process-
ing systems, 35:24824–24837, 2022.
[48] Jiaqi Xue, Mengxin Zheng, Ting Hua, Yilin Shen, Yepeng
Liu, Ladislau B¨ol¨oni, and Qian Lou. Trojllm: A black-box
trojan prompt attack on large language models. Advances in
Neural Information Processing Systems, 36, 2024.
[49] Yuchen Yang, Bo Hui, Haolin Yuan, Neil Gong, and Yinzhi
Cao.
Sneakyprompt:
Evaluating robustness of text-to-
image generative models’ safety filters.
arXiv preprint
arXiv:2305.12082, 2023.
[50] Kaijie Zhu, Jindong Wang, Jiaheng Zhou, Zichen Wang, Hao
Chen, Yidong Wang, Linyi Yang, Wei Ye, Yue Zhang, Neil
Zhenqiang Gong, et al.
Promptbench: Towards evaluat-
ing the robustness of large language models on adversarial
prompts. arXiv e-prints, pages arXiv–2306, 2023.
[51] Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J Zico
Kolter, and Matt Fredrikson. Universal and transferable ad-
versarial attacks on aligned language models. arXiv preprint
arXiv:2307.15043, 2023.
10

```
