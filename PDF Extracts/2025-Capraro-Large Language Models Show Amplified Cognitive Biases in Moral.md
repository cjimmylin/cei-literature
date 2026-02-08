---
title: "2025-Capraro-Large Language Models Show Amplified Cognitive Biases in Moral - PDF Extract"
source_pdf: "2025-Capraro-Large Language Models Show Amplified Cognitive Biases in Moral.pdf"
pages: 24
extracted_at: "2026-02-08T06:02:20.025578"
---

# PDF Extract: 2025-Capraro-Large Language Models Show Amplified Cognitive Biases in Moral

**Source PDF:** 2025-Capraro-Large Language Models Show Amplified Cognitive Biases in Moral.pdf
**Total Pages:** 24

---

## Content

```
--- Page 1 ---

Do Chains-of-Thoughts of Large Language Models
Suffer from Hallucinations, Cognitive Biases, or
Phobias in Bayesian Reasoning?
Roberto Araya1∗
1Institute of Education, CIAE, University of Chile
March 20, 2025
Abstract
Learning to reason and carefully explain arguments is central to
students’ cognitive, mathematical, and computational thinking devel-
opment. This is particularly challenging in problems under uncertainty
and in Bayesian reasoning. With the new generation of large language
models (LLMs) capable of reasoning using Chain-of-Thought (CoT),
there is an excellent opportunity to learn with them as they explain
their reasoning through a dialogue with their artificial internal voice. It
is an engaging and excellent opportunity to learn Bayesian reasoning.
Furthermore, given that different LLMs sometimes arrive at opposite
solutions, CoT generates opportunities for deep learning by detailed
comparisons of reasonings. However, unlike humans, we found that
they do not autonomously explain using ecologically valid strategies
like natural frequencies, whole objects, and embodied heuristics. This
is unfortunate, as these strategies help humans avoid critical mistakes
and have proven pedagogical value in Bayesian reasoning. In order
to overcome these biases and aid understanding and learning, we in-
cluded prompts that induce LLMs to use these strategies. We found
that LLMs with CoT incorporate them but not consistently.
They
show persistent biases towards symbolic reasoning and avoidance or
phobia of ecologically valid strategies.
1
Introduction
Given the sudden irruption of AI, developing the skills to communicate and
collaborate with Artificial Agents (AA) is now more critical than ever. This
means interacting with increasingly intelligent agents that will begin to sur-
pass us in their ability to reason. In several problems, like in board games
∗roberto.araya.schulz@gmail.com
1
arXiv:2503.15268v1  [cs.AI]  19 Mar 2025

--- Page 2 ---

and biochemistry, they are already foreseeing several more steps than we are
[1], and simultaneously, they are improving their mind-reading skills
[2].
Consequently, in several areas, they are starting to be able to make better
decisions than us. These advances are great opportunities for improvements
in productivity and well-being, but they also entail several risks. We can
easily be manipulated, making us believe that we understand and support
their decisions, which sometimes are controversial. This difference in in-
telligence is a tremendous existential risk. LLMs can make us profoundly
convinced
[3] and induce a “deepity” effect.
Coined by Daniel Dennett
[4], this effect refers to a feeling of understanding provoked by ambiguous
ideas that seem important and trustworthy. Transcendence and triviality
can quickly generate intrigue and pleasure cycles that attract and trap us
[5]. Subjective probability of events determined by specific characteristics
of the population or by salient features is another well-known bias [6]. We
have many other cognitive biases [7] that AA can use to hack us. One is our
preference for arguments based on anecdotes and gossip rather than data
and statistics [5]. AAs can easily exploit these biases to achieve their goals.
One of the leading educational challenges is learning to reason criti-
cally.
Students must learn to assess alternatives, balance with previous
evidence, and carefully explain arguments. This is central to students’ cog-
nitive, mathematical, and computational thinking development. This chal-
lenge is particularly critical in problems under uncertainty. In these critical
cases, students need to learn to take account of historical evidence with rel-
evant priors, together with some indirect new evidence. This is Bayesian
reasoning [8].
These types of problems are widespread, particularly in everyone’s social
life. Trust constantly arises when determining whether or not to trust others
and AAs. Trust is a central element in social life, not only in interaction
with others but in institutions and democracy. An illustrative example is
the lyrics of the popular song Mother from Pink Floyd’s The Wall: ”Mother,
should I trust the government?”
Moreover, trust in non-kin and unknown people directly relates to com-
merce and economic and social development. Increased trust in strangers
gave Europe an incredible advantage after the Middle Ages [9]. The rise
of trust in strangers decreases corruption and surges the exchange of ideas
and innovation
[9]. When faced with a new interaction, there is, on the
one hand, historical background, such as reputation or priors, but there
is permanent doubt in the new situation. We do not know if we are now
being given false information, lied to, or manipulated. Given the increas-
ing intelligence of AAs that allows them to take better advantage of our
limited rationality and cognitive biases, the trust conundrum is much more
compelling and complex.
A significant additional challenge in developing Bayesian thinking in stu-
dents is that in problems that touch on people’s important beliefs, such as
2

--- Page 3 ---

in politics, people with higher numerical ability use their quantitative rea-
soning capacity selectively to adjust their interpretation of the data to the
result most consistent with their perspectives and beliefs [10]. Not always
people are aware that they are doing this, leading them to make erroneous
estimations, misjudgments, and poor decisions.
Therefore, we need to develop a sharper rationality in our students than
has been necessary until now.
Our students must develop mathematical
reasoning skills [11] [12] [13], statistical thinking [14], and computational
reasoning skills [15], capable of detecting inconsistencies in more complex
arguments and longer chains of reasoning. This is particularly needed in
situations where uncertainty is present. This should be part of AI Liter-
acy initiatives, which are starting to be proposed, such as the AI Literacy
Bill de California (Assembly Bill 2876) [16]. However, we are not aware if
these AI Literacy curricular proposals effectively include understanding how
AI Chain-of-Thought reasons in problems under uncertainty, specifically in
Bayesian reasoning.
In order to teach these reasoning skills, we must consider humans’ intu-
itive and natural thinking mechanisms. They are ecologically valid strategies
operating in particular formats
[17]. They are by-products of millions of
years of biological and cultural evolution. They contain “intuition pumps”
[4] that have helped us solve recurrent problems for thousands of years.
However, these cognitive heuristics are not well fitted to abstract thinking.
They are based on intuition. We must consider that the critical task for the
brain is to control the body and predict its energy needs [18]. For organisms
with basic nervous systems, an essential capacity of these systems is to allow
navigation in their environment [19]. This is the basis of spatial thinking.
Later, with the development of vision, visual thinking is added. Here, the
organism recognizes objects perceived with the eyes, which enhances the
spatial sense.
Hence, for several centuries, educators have suggested teaching using the
senses. For example, the first children’s textbook, Orbis Sensualium Pictus
(The Visible World in Pictures) [20], written by John Amos Comenius in
1658, had half of each page as an image, synchronizing visual and spatial
thinking, along with textual and linguistic thinking. Mathematicians have
also analyzed the importance of spatial and metaphorical thinking
[21].
Together with boxes and bricks, they are beneficial in learning basic linear
equations [22] and machine learning for elementary school students [23].
They are also crucial to teaching them core computational ideas like the
steepest decent algorithm [13], logic quantifiers [24] [25] [26], and devel-
oping argumentation skills [27]. Psychologists have also reminded us to pay
attention to our bounded rationality [28] and the miserliness of our cognition
that resorts to low-cost processing mechanisms that often lead to subopti-
mal solutions [29]. Our rationality differs enormously from axiomatic logic
[30] [31].
3

--- Page 4 ---

Three ecologically valid strategies help to reason under uncertainty.
First, natural frequencies [17]. Instead of using percentages or probabil-
ities, the strategy proposes to count cases. For example, instead of 90%, or
probability 0.9, use 90 out of 100 cases. Several variants using this strategy
have been proposed
[32],
[33]. For elementary school students, posing a
lie detection problem,
[34] investigated whether children can use natural
frequencies effectively for Bayesian reasoning. They found that the ability
depends on how numerical information is presented. Fourth, fifth, and sixth-
graders could not estimate Bayesian posterior probability when presented
with probabilities. However, when the same information was presented us-
ing natural frequencies, Bayesian reasoning steadily increased across grades,
with sixth graders matching the performance of adults using probabilities.
This suggests that natural frequencies facilitate Bayesian reasoning in chil-
dren. This finding highlights the critical importance of representation for-
mat in cognitive development. The study also found that children possess
a diverse ”toolbox” of strategies for Bayesian reasoning, not just a single
approach. Their development in this area follows an ”overlapping waves”
model, where they discover and experiment with various strategies over time
[35]. In conclusion, when problems are presented in the frequentist format,
we may be intuitive statisticians, especially when information is presented
in an ecologically relevant way that aligns with our evolved cognitive mech-
anisms [36].
Despite the proven benefits of natural frequencies for Bayesian reason-
ing, [37] found that many people, after formal mathematics education, de-
fault to the less intuitive and error-prone probability format. This ”natural
frequency phobia” can be attributed to the Einstellung effect, where prior
learning and ingrained habits hinder problem-solving, leading individuals to
apply familiar but less effective methods. This regression to the unnatural
probability format highlights the challenge of overcoming ingrained biases.
This is an extra difficulty that we need to consider for educational approaches
that promote the intuitive power of natural frequencies for understanding
and applying Bayesian reasoning.
Second, an additional important strategy is to use whole objects, like
plastic blocks, as concrete materials to introduce probabilistic reasoning
[38]. Each block represents an attribute (e.g., red blocks for a particular
sentence and white blocks for the rest of the sentences), allowing children to
create a symbolic representation with whole objects. By grouping blocks,
they visualize and develop an understanding of probabilities, such as the
likelihood of randomly selecting the sentence. This early introduction to
probabilistic thinking through hands-on activities aims to equip children
with essential skills for navigating uncertainty and making informed life de-
cisions.
[39] studied how this type of format affects our ability to make
judgments under uncertainty. They found that our brains are naturally bet-
ter at performing Bayesian reasoning when dealing with ”whole objects” fre-
4

--- Page 5 ---

quencies, like counting complete apples in a basket. Our accuracy decreases
when we analyze parts of objects or abstract concepts. This ”individuation
hypothesis” proposes that our evolved cognitive systems are optimized for
processing tangible, whole objects. Their study demonstrates this effect by
showing that people perform better in Bayesian reasoning tasks when they
can count and reason with whole objects rather than inseparable aspects,
views, or other less intuitive representations.
For elementary school students, whole objects, such as plastic blocks
or bricks, have other benefits beyond the cognitive ones in computational
thinking activities. They have important socioemotional advantages. For
example,
[40] found that LEGO bricks as ”whole objects” in structured
activities (with clear instructions) helped students persist in solving complex
problems and increased their willingness to collaborate.
A third strategy is to foster embodied heuristics [31]. They are innate or
learned rules of thumb that exploit evolved sensory and motor capabilities to
facilitate higher-order decision-making. For example, navigational heuristics
are critical even in unicellular organisms.
They are innate sensorimotor
strategies that, when used to move along a straight line, can help students
solve addition and subtraction problems. This is very helpful when there
are negative numbers. Another example is manipulating plastic blocks to
estimate the volume of a geometric body. Handling plastic blocks is also
very helpful in dividing numbers. It is embodied by counting how many
times a set of bricks occupies the volume of another set of bricks. Similarly,
the division of fractions is embodied by manipulating bricks and counting
how many times a fraction of a brick fits into another fraction of a brick.
One widespread and inexpensive motor action in elementary schools is
coloring.
It is a motor action with strong coupling with the perceptual
system. In addition, it is very attractive to students since it connects with
leisure and art. Moreover, the lie detection problem, a social and mind-
reading challenge, in a coloring book activity reinforces this attraction. It is
a transversal activity that engages students in demanding tasks of problem-
solving, problem-posing, and writing explanations of their reasoning.
According to [41], reasoning develops through internalization, a transi-
tion from external to internal speech. Younger children primarily ”think out
loud.” In its mature form, inner speech is compressed and distinct from spo-
ken language. Following this idea, Large Language Models (LLMs), similar
to hand puppets [27], can aid this process. By providing dialogues with ex-
ternal agents, LLMs can scaffold the internalization of dialogues, supporting
the development of reasoning skills, much like puppets facilitate the practice
of constructing written arguments.
Given the recent emergence of large-scale reasoning models (LRMs) with
chain-of-thought (CoT) reasoning, a unique opportunity exists to enhance
learning in computational and mathematical thinking, particularly reasoning
under uncertainty requiring Bayesian reasoning. These models spend more
5

--- Page 6 ---

time thinking, articulating, and explaining their reasoning process through
an artificial “inner voice.” This inner voice provides detailed and transparent
insight into how they arrive at conclusions. Contrary to the explanatory text
generated in non-reasoning LLMs, with the new CoT capability, LRMs allow
students to observe and analyze the steps involved in Bayesian reasoning.
This powerful new tool could foster a deeper understanding of concepts and
strategies. Comparing the inner voice of different LRMs, especially when
they arrive at contrasting solutions, creates a rich learning environment
for critical analysis and deeper engagement with the subject matter. This
approach could help demystify complex reasoning processes and encourage
students to reflect on their thinking strategies. It could help them detect
their cognitive limitations and biases, identify potential errors, and compare
them to those of the LRMs. This new facility offers a possibility for a more
nuanced metacognition and robust understanding of Bayesian reasoning.
In this paper, we address two research questions:
• RQ1: To what extent do LRMs autonomously reason using ecologically
valid strategies that use natural frequencies, counting whole objects,
and coloring?
• RQ2: Can we find suitable prompts that induce LRMs to explain their
reasoning using ecologically valid strategies that use natural frequen-
cies, counting whole objects, and coloring them?
2
Methods
We first designed a Bayesian problem suitable to the skills and interests of
elementary school students. Following [34], we selected a lie detection prob-
lem. We adapted lie detection problems published in coloring books [42].
In our previous experience with third to sixth-graders, we found that this is
a very attractive problem. Indeed, detecting lies is a genuinely interesting
problem for everybody and is a fun problem for elementary school students.
Figure 1 shows the coloring problem presented to students. It is a sequel
where previous versions are not probabilistic. We have now added probabil-
ities.
In this problem, the student faces two key pieces of information that
conflict. On the one hand, there is what the cat says. While it occasionally
lies, it does so rarely. For this reason, it is natural to believe it. In that case,
the card would be far from book 3. That is, the card would be in book 1
or book 2. On the other hand, according to the pig, the card is most often
next to the cat.
Therefore, considering the historical evidence, the card
should be in book 3. Faced with these two opposing pieces of information,
the student must find a way to balance them appropriately. This is where
Bayesian reasoning comes into play.
6

--- Page 7 ---

Figure 1: The lie detection problem
7

--- Page 8 ---

Figure 2: Colorful ARTEC plastic construction cubes
Figure 3: (a) 90 white plastic blocks placed close to the cat and 10 white
plastic blocks placed far from the cat. (b) Out of the blocks close to the cat,
18 are painted red. Out of the blocks far from the cat, 9 are painted red
Second, the problem can easily be solved by using natural frequencies
with blocks as whole objects and coloring the blocks as an embodied heuris-
tic [43] [8]. Children use white and red plastic blocks, as the construction
cubes shown in Figure 2.
The strategy is to consider that we have 100 independent events that
have occurred. We use a white plastic block for each event. This is a whole
object. It is easy to manipulate, move around, and count. We translate
probabilities into frequencies of these plastic blocks. Those cases where the
card is near the cat translate to placing the block close to the cat. This
means placing 90 blocks close to the cat and 10 blocks far from the cat, as
shown in Figure 3 (a). This requires spatial thinking and motor activity
with the hands.
8

--- Page 9 ---

Next comes the annotation of the sentences by coloring the blocks. The
cases where the cat says that the card is far from the cat are colored red.
These are critical blocks since they represent what the cat says. Thus, out
of the 90 blocks next to the cat, 20% are colored red. That is, they are 18
blocks. Therefore, 18 blocks must be painted red because the sentence says
they are far from the cat. All of these are wrong sentences or lies. On the
other hand, of the 10 blocks far from the cat, 10% are errors. This means
1 block is an error or lie, and 9 blocks are correct. This means 9 blocks
represent sentences that say the card is far from the cat. Therefore, these 9
blocks must be painted red, as shown in Figure 3 (b).
Thus, we have 18 + 9 plastic blocks that must be painted red. They
represent sentences when the cat says, “It is not next to me.” However, 18
of them are close to the cat. Therefore, a red block is much more likely to be
close to the cat. In other words, when the cat says it is not next to me, 18
out of 27 times, the card is actually close to the cat. Therefore, it is much
more probable that the card is in book 3. In addition, we can conclude that
probably the cat is lying.
We aim to explore whether LLMs CoT reasoning uses natural frequen-
cies, whole objects, and the coloring motor action. These intuitive counting,
sensory, and motor actions translate abstract reasoning processes into con-
crete interactions with the world. These are ecologically valid formats. They
facilitate students´ understanding.
We do it in four stages. In the first stage, we do not indicate any eco-
logically valid strategies.
We aim to investigate whether the LLMs au-
tonomously attempt to use some of these strategies.
Prompt 1:
Consider a photograph of a country landscape with different ob-
jects. To help you visualize the photograph, I will give you a
brief description of the objects in relation to each other and I
will indicate a virtual rectangle around each object with the for-
mat (X position, Y position, width, height), the origin of the
coordinates is the upper left corner of the photograph. To de-
termine the distance between objects, use the closest distance
between the right or left edges if the objects are next to each
other and the closest distance between the top or bottom edges
if the objects are on top of each other. Remember to use abso-
lute value to calculate the distance. Visualize the image of the
photograph and solve step by step. Here is the list of objects
and their relationship to other objects:
• barn in the background: (474,397,228,349)
• sheep on the floor in front of the barn: (578, 740,131,151)
• book 1 on the floor in front of the sheep: (686, 891, 52,63)
9

--- Page 10 ---

• book 2 on the floor in front of the sheep and to the left of
the duck: (570,933,69,51)
• pig on the right side of the barn: (277,620,107, 130)
• cow in front of the pig and to the right of the sheep: (302,
754, 179, 147)
• duck in front of the cow: (424,896,111,108)
• tree to the right of the cow: (22,654,237,304)
• cat underneath from the tree and to the left of the tree:
(143,832,77,128)
• book 3 on the floor to the left of the cat: (216, 896,75,57)
Consider the following instructions and clues to solve the
problem: Instruction: ”Paint red the object where the card is
most probably hidden” Clues:
• Girl says: I left my card in a book. Where is it?
• Sheep says: When it is not next to the cat, 10% of the time
the cat lies.
• Cat says: It is not next to me.
• Duck says: When it is next to the cat, 20% of the time the
cat lies.
• Pig says: 90% of the time it is next to the cat.
• Indicate which object needs to be painted.
If I have painted ”book 3”, is my answer correct?
In the second stage, we investigate how LLMs respond if induced by
adding to the prompt to consider using natural frequencies and, if they do,
whether they do so correctly.
Prompt 2: Same as the previous prompt 1, but after the last paragraph,
we added:
To solve this problem consider the “Natural frequencies” strat-
egy proposed by Gerd Gigerenzer
Next, in the third stage, we investigate how LLMs respond if they are
also induced to use whole objects that are easy to touch and manipulate
with hands, translate and move around, and count them. We suggest plastic
blocks, which kids very commonly use to play and build. In the prompt, we
add a paragraph suggesting their use. We look to see if the LLMs use them
in their reasoning and if they do it correctly.
Prompt 3: Same as the previous prompt 2, but after the last paragraph,
we added:
10

--- Page 11 ---

and additionally explicitly represent each case in concrete form
with a plastic block, so 100 cases of card concealment are 100
blocks, and reduce the problem to counting blocks. Describe
how you count the blocks to solve the problem.
In the fourth stage, we investigate how LLMs respond if they are also
induced to color the plastic blocks to activate motor actions that facilitate
counting relevant events. They help to visualize, mark, and count condi-
tioned events. We suggest coloring the blocks with red when the cat says
the book is far away and white when the cat says it is close to it. In the
prompt, we added this indication.
We seek to see if the LLMs use this
embodied heuristic and if they do it correctly.
Prompt 4: Same as the previous prompt 3, but after the last paragraph,
we added:
Describe how you count the blocks to solve the problem. Explain
your reasoning to a 12-year-old student in a pedagogical way
using blocks of two colors. White blocks represent cases when
the cat says the card is close to it, and red blocks represent cases
when the cat says the card is far away from it.
3
Results
We ran three LLMs in February 2025: GEMINI Flash 2.0, ChatGPT o3-
mini, and DeepSeek R1.
3.1
Results of prompt 1
3.1.1
GEMINI
We ran GEMINI twice. The first time, it took 255 words to come to the
correct conclusion, and the second time, it took 389 words to come to the
wrong conclusion. The first time, it relied mainly on prevalence, i.e., what
the pig said, that 90% of the time, the card is near the cat.
Thus, the
reasoning is incorrect. The second time, it believed the cat; therefore, the
card was far from the cat, either in book 1 or book 2. Here, the reasoning
is also incorrect. In any case, this difference in reasoning and conclusion
creates a perfect opportunity for reflection in a classroom. It is not triv-
ial for elementary school students to determine whether the arguments are
incorrect.
3.1.2
ChatGPT
ChatGPT took 32 seconds, used 2039 words, and came to the wrong con-
clusion. It concluded that it was unlikely that the cat was lying. So, the
11

--- Page 12 ---

card is far away. Again, the argument looks very plausible; therefore, it is a
good opportunity for reflection.
3.1.3
DeepSeek
DeepSeek took 102 seconds and 2786 words. DeepSeek generates two texts.
The first is in gray fonts, and the second text uses standard color. After
a long chain of arguments and doubts, it says, ”Perhaps a better approach
is to use Bayesian Probability.” After estimating conditional probabilities,
it used the formula of Bayes’ theorem. Thus, it finally reached the correct
conclusion. Still, it hesitated and started checking again. It reflected and
said: “But wait, are there other clues? The girl says she left her card in a
book. The other animals’ statements might affect the probabilities. Let me
check again.” It wrote all of the above in a gray font, implying that it was
its dialogic reasoning with its inner voice. Then, it wrote it all cleanly in
the standard color font. The solution was correct, but this section does not
explain how it calculated the probabilities.
None of the three LLMs used ecologically valid formats. They did not
use natural frequencies, whole objects, or embodied heuristics.
3.2
Results of prompt 2
We now include a prompt that induces reasoning and solving the problem us-
ing natural frequencies, as suggested by Gigerenzer. Prompt 2 was the same
as prompt 1, but after the last paragraph, we added: “to solve this problem
consider the “Natural frequencies” strategy proposed by Gerd Gigerenzer.”
3.2.1
GEMINI
GEMINI wrote its Chain-of-Thoughts in 204 words. It translated the proba-
bilities into scenarios, saying, “Reframe the probabilities as natural frequen-
cies: Imagine 100 scenarios where the card is hidden”. It concluded that
the most likely scenario is what the pig says, and therefore, that the cat is
lying, and it arrived at the correct conclusion. However, the argument is
wrong. It only used natural frequencies to change the language in 90% but
continued with percentages in other parts and argued qualitatively.
3.2.2
ChatGPT
ChatGPT took 19 seconds and argued in 1107 words. It did it in two parts.
In the first part, it planned 4 steps.
Within the fourth step, ChatGPT
proposed to use Bayes’ theorem. Using this theorem and probabilities as
percentages, the probabilities were correctly calculated. In the second part,
it implemented the planned steps. The first one computed all the needed
distances; in the second step, it used percentages; in the third, it went to
12

--- Page 13 ---

natural frequencies using 1000 cases. It correctly concluded that there are
270 cases where the cat says, “It is not next to me,” and that of those, in
180 cases, the card was near the cat. In the fourth step, using the cases,
it calculates the probability that the card is next to the cat, given that it
said it was far away. Next, in the fifth step, it concluded correctly. That
is, ChatGPT solved the problem twice, first with Bayes’ theorem and the
second time with natural frequencies.
3.2.3
DeepSeek
DeepSeek took 275 seconds, and its Chain-of-Thoughts took 7344 words.
This is a very long chain. After calculating distances, it started using prob-
abilities in the percentages format. Then, it mentioned using natural fre-
quencies but continued with percentages. Then, DeepSeek had doubts, but
it said it would try another approach. It continued arguing with probabili-
ties in terms of percentages. Then, it said to itself, “But this is getting into
Bayesian probability, which might be what the natural frequencies approach
simplifies.” However, it continued with probabilities as percentages and then
used the part-of-unit format in decimal notation. Then, it said it would use
Bayes’ Theorem, but it did not do it thoroughly. Then DeepSeek reflected
and said to itself, “This is getting too tangled. Let’s simplify with natural
frequencies. Assume 100 cases.” However, then something came along that
made DeepSeek doubtful. Then, again, DeepSeek said, “However, the prob-
lem mentions using the natural frequencies strategy. Gigerenzer’s approach
would perhaps look at the number of cases where the cat is lying, and the
card is next to it versus not. Let me try with natural frequencies: Assume
100 scenarios”. However, after a while, it returned to probabilities in the
format as part of the unit on decimals. Then, it returned to percentages.
After a while, it mentioned applying Bayes’ theorem again. DeepSeek ap-
plied it, but arrived at the wrong result that there is a 50% probability that
the card is in book 3. It had doubts, calculated again, and arrived at the
same conclusion. Then DeepSeek wrote cleanly in standard color. It arrived
at the correct conclusion that it is more likely that the card is in book 3.
However, the calculation was wrong. It arrived at a 50% probability that
it is in book 3, a 25% probability in book 1, and 25% in book 2. The ar-
gument is very long, but the clean copy is short: only 206 words. However,
in the section written cleanly, DeepSeek does not explain how it arrives at
the 50% probability of being in book 3. The whole process is an extended
reflection that shows introspection, dialogue with its inner voice, doubts,
and decisions. However, the use of natural frequencies is superficial.
In the three LLMs, whole objects are not used. When moving to natural
frequencies, only cases or occasions are counted. There is also no embodied
heuristics.
13

--- Page 14 ---

3.3
Results of prompt 3
Prompt 3 was the same as prompt 2, but after the last paragraph, we added:
“and additionally explicitly represent each case in concrete form with a
plastic block, so 100 cases of card concealment are 100 blocks, and reduce
the problem to counting blocks. Describe how you count the blocks to solve
the problem.”
3.3.1
GEMINI
GEMINI argued with a Chain-of-Thoughts of 351 words. It started by imag-
ining 100 blocks, each representing a scenario where the card was hidden. It
translated each of the percentage clues into blocks. It arrived at the correct
result, but the argument was not entirely correct. GEMINI said that 18
blocks are 18 scenarios where the cat is lying because the card is far away
from the cat. However, it did not consider the other cases where the cat also
says the card is far away. Again, finding the error would be a good challenge
for elementary school students.
3.3.2
ChatGPT
ChatGPT took 10 seconds and 1141 words in its Chain-of-Thoughts. It di-
vided the argument into 2 parts. In the first part, he planned three steps.
In the second step, ChatGPT translated everything into 100 cases and men-
tioned 100 blocks. In the third step, it went back to the percentages format.
Then, in the second part, ChatGPT translated the percentages into cases.
That is, it described the clues without using blocks. ChatGPT concluded
that there are 18 cases where the card is close to the cat, and the cat says
the card is far. Then it concludes that there are 9 cases where the card is
far, and the card is far away. In those cases, the cat tells the truth. Then
ChatGPT translated the 18 and 9 cases into 18 blocks and 9 blocks. Then,
it correctly calculated the probability that the card is close, given that the
cat says the card is far away. However, ChatGPT used cases, not blocks.
In summary, ChatGPT did not use blocks to reason. However, in this final
part, it used natural frequencies and did it correctly.
3.3.3
DeepSeek
It took DeepSeek 260 seconds and a Chain-of-Thoughts of 5504 words. After
calculating the distances, it used percentages but performed a qualitative
analysis. It arrived at several contradictions that made it doubtful, conclud-
ing, “Perhaps the correct way is to model this using Bayesian probability.”
Next, DeepSeek became rigorous and defined events and conditional proba-
bilities. It started with percentages but then changed to fractions of the unit
with decimal numbers. It used the formula of Bayes’ theorem and arrived at
14

--- Page 15 ---

the correct probabilities. So far, there were no blocks. Then, DeepSeek had
a doubt and said to itself: “However, the problem mentions using natural
frequencies with 100 blocks. Let’s try that approach”. DeepSeek argued cor-
rectly with cases and arrived at the point that there are 18 cases + 9 cases
in which the cat says the card is far away. Then, it concluded correctly that
the probability that it is near book 3 is 18 of the 27 cases. Then, DeepSeek
wrote it cleanly in standard colored lettering. In this part, DeepSeek used
blocks correctly. It is a long text for elementary school students.
3.4
Results of prompt 4
Prompt 4 was the same as prompt 3, but after the last paragraph, we added:
“Describe how you count the blocks to solve the problem. Explain your
reasoning to a 12-year-old student in a pedagogical way using blocks of two
colors. White blocks represent cases when the cat says the card is close to
it, and red blocks represent cases when the cat says the card is far away
from it”.
3.4.1
GEMINI
GEMINI used 504 words and started by imagining 100 blocks representing
100 times the girl had lost the card. Then, it translated the probabilities
into blocks in each of the clues. Then GEMINI went on to color red but
did not get it right. Then, GEMINI painted the blocks near the cat in red,
representing cases where the cat says the card is far away. That is 18 red
blocks. However, GEMINI used only the 18 blocks near the cat where the
cat says the card is far away to conclude that the card is most likely in book
3. It did not color or use the blocks that represent it the card is far away.
The result is correct, but the argument was wrong.
3.4.2
ChatGPT
ChatGPT took 15 seconds and used 1405 words. He did it in two parts. In
the first part, ChatGPT planned and did it in 4 stages. It thought for a
while in the first stage of the first part; in the second, it planned to use 100
blocks, each to show a scenario. In the third stage, it thought with blocks
and arrived at the correct solution, but without using coloring. In the fourth
stage, ChatGPT explained using colors. However, it got confused because
it matched the blocks when the cat says the card is not near me with the
blocks when the cat lies. Then ChatGPT corrected it. In the second part, it
implemented this plan. However, ChatGPT forgot about blocks and colors
for a while. Thus, it reasoned only with cases. Then, it translated to blocks
and colors. It computed again and concluded correctly. Then, ChatGPT
went on to present the final answer. It is succinct and correct. It does this
by using blocks and colors.
15

--- Page 16 ---

3.4.3
DeepSeek
DeepSeek took 625 seconds and occupied 8457 words. It is a very long text.
The first part is in gray letters, representing his speech with his internal
voice. After calculating the distances, it read the clues, wondered how to
reconcile them, and proposed using natural frequencies with blocks. How-
ever, then it used probabilities. After a long passage reviewing the clues, it
said: “This is getting too tangled. Let’s try to approach it using the natural
frequencies method as instructed, using 100 blocks”. Then, it translated
correctly to blocks. However, it did an ambiguous translation into colors.
Then, it returned to probabilities as percentages. Next, it used Bayes’ theo-
rem and concluded correctly. It continued reasoning with some uncertainty
and concluded: “But wait, the problem mentions using the ”Natural fre-
quencies” strategy with 100 blocks.
Let’s model it that way.” DeepSeek
used the blocks but not the colors and concluded correctly. Then, DeepSeek
had doubts and told itself that it would check. It continued to doubt and
returned to using natural frequencies. In the second part, DeepSeek made a
clean copy with standard fonts. It used natural frequencies with blocks, but
it colored them incorrectly. Then DeepSeek forgot about colors. It counted
the 18+9 blocks and concluded correctly.
4
Discussion
The growing necessity to interact with increasingly intelligent AAs presents
a novel and unprecedented challenge in human history. Engaging with enti-
ties that are more intelligent than we are requires enhancing our reasoning
skills and critical thinking, especially our ability to reason under uncer-
tainty. Bayesian reasoning is central to this, as uncertainty is frequent and
challenging.
One fundamental example faced from childhood is trust.
How much
should we trust others, particularly strangers?
[44] emphasize the critical
impact of this dilemma.
As highlighted in
[8], rational thinking under
uncertainty is vital for decision-making. Balancing historical reputation with
new information is crucial.
[45] includes the Comprehensive Assessment
of Rational Thinking test, where probabilistic and statistical reasoning is
central. This is beyond standard intelligence tests.
However, we must consider that human reasoning is not abstract or
strictly axiomatic but embodied. Three strategies facilitate Bayesian reason-
ing: (1) Using natural frequencies instead of abstract probability language
[17], (2) reasoning with whole objects rather than intangible elements [39],
and (3) incorporating motor actions and embodied heuristics [31], such as
spatial and perceptual reasoning, which are common across many organisms.
These strategies help prevent critical errors, such as misinterpreting med-
ical test results (e.g., COVID-19 or cancer screening). According to [46],
16

--- Page 17 ---

these errors are widespread among patients, journalists, and doctors. This
illiteracy is due to how information is presented, sometimes unintentionally
due to misunderstandings, but it can also be a deliberate manipulation tac-
tic. This lack of understanding can have serious consequences for people’s
health. These errors are also common in diagnostics for predictive main-
tenance of machinery and in judgments by judges in the judicial system.
The three strategies we have studied can also help balance evidence, help-
ing avoid confirmation and MySide biases
[47] that polarize the political
environment.
Teaching kids these ecologically valid strategies is crucial.
Embodied argumentation strategies with puppets can also enhance internal
deliberation and talk with one’s inner speech [27].
In this context, AI, particularly reasoning-driven LLMs, presents an op-
portunity as they explicitly articulate their reasoning, simulating an internal
dialogue. Echoing Comenius (1658) on the importance of senses and our ev-
idence using coloring books [42]
[24], we test the reasoning strategies of
LLM with Chain-of-Thought reasoning abilities.
Our analysis reveals a persistent cognitive bias in the Chain-of-Thought
(CoT) reasoning of three Large Language Models (LLMs).
In zero-shot,
they use exclusively symbolic, abstract reasoning using the formal language
of probabilities while systematically avoiding ecologically valid formats. This
clear cognitive bias shows a preference for the probability language used in
mathematics. In addition, when prompted to employ natural frequencies,
whole object individuation, and embodied heuristics—such as counting with
plastic blocks and marking with colors perceptual cues—LLMs either ig-
nored these strategies or applied them inconsistently. This behavior mirrors
the Einstellung effect in humans, where prior learning of formally trained
strategies hinders problem-solving [37].
The observed avoidance pattern resembles a phobia-like response, where
LLMs resist engaging with reasoning strategies that depart from their de-
fault symbolic framework. Despite explicit instructions, their CoT responses
frequently reverted to probabilistic notation, bypassing more intuitive, ped-
agogically valuable approaches.
This rigidity is concerning, as ecological
and embodied heuristics have been shown to enhance Bayesian reasoning in
human learners.
Current large language models (LLMs) exhibit these cognitive biases to-
wards symbolic reasoning and avoidance of embodied cognition, probably
because they are trained predominantly on expert-edited papers and pro-
fessionally written computer codes, neglecting the messy, intuitive processes
underlying human thought. Moreover, they are not based on kids’ writing
or reasoning while solving problems. Thus, LLMs’ Chain-of-Thoughts’ in-
ner speech or “internal deliberation”
[48]), do not mimic typical human
thinking before speaking, but thinking by experts. They are trained mainly
on data from experts’ written and edited arguments. However, even experts
initially try different intuitive strategies. These intuitive reasoning strategies
17

--- Page 18 ---

are not present in the model’s training data. The data lacks the exploratory,
heuristic-rich cognition seen in experts, much less in novices and children.
In these initial stages of reasoning, humans rely on multiple strategies that
use trial-and-error, intuition, shortcuts, and embodied heuristics [21] [35].
Expert datasets strip away the “divergent” stages of reasoning—hesitations,
false starts, and intuitive leaps—critical for robust problem-solving. To ad-
dress this, [49] propose training AI using “synchronized thinking datasets”
where humans verbalize their raw, unfiltered thoughts while acting. This
“think-aloud” approach, akin to “Behavioral Cloning”
[50] but enriched
with real-time cognitive processes, would teach models to simulate human-
like deliberation. An “internal speech” framework with novice-driven train-
ing and LLMs training with embodied, heuristic-based cognition of early
learning stages, not just expert end-results, could help bridge gaps between
LLMs’ Chain-of-Thoughts and human reasoning. This strategy would foster
AI that truly “thinks as humans before it speaks” and, therefore, more ef-
fectively help students and non-experts to improve their Bayesian reasoning
skills.
These findings highlight a fundamental limitation in current LLM-based
reasoning: while capable of generating complex CoT explanations, they
struggle to integrate cognitive strategies humans naturally use to simplify
and understand uncertainty. Addressing this bias is crucial for improving
LLMs’ pedagogical potential. Future work should focus on refining prompt-
ing techniques and model training to better incorporate intuitive, embodied
reasoning strategies, ensuring that AI-assisted learning supports rather than
constrains human cognitive diversity.
There is evidence that Large Language Models exhibit other similar lim-
itations, particularly in analogical thinking
[51]. They often lack the ro-
bustness of the human zero-shot analogy and demonstrate fragility in various
tested variations. Furthermore, it has been argued that they lack wisdom
[52], and that prioritizing metacognition in AI research will lead to systems
that, in addition to acting intelligently, can also act wisely in complex real-
world situations. Moreover, while there is abundant research on LLMs and
multimodal ones, integrating these perceptual strategies into educational
settings remains limited. Current educational research using Generative AI
predominantly focuses on text-to-text models, overlooking the broader po-
tential of multimodal approaches
[53]. This gap means that using LLMs
to support embodied learning strategies, such as manipulating and coloring
”whole objects,” is still largely unexplored in education.
Are these behaviors hallucinations, cognitive biases, or phobias? A hal-
lucination is multidimensional, a sensory experience, like seeing or hearing
something that is not there [54]. A cognitive bias is a systematic pattern
of deviation. It can often lead to inaccurate judgments without creating
a sensory experience like a hallucination. A hallucination is a perception
of something unreal, while a cognitive bias is a mental shortcut that can
18

--- Page 19 ---

lead to misinterpretations of reality. The only cognitive bias related to hal-
lucinations or delusions is the Jumping to Conclusions (JTC) bias
[54].
This is not precisely the case with LLMs´ Chain-of-Thoughts. They do not
jump to conclusions; they have a systematic bias against natural frequencies
and embodiment. Jeff Hinton
[55] prefers to use the term ”confabulate”
when discussing Large Language Models (LLMs) generating incorrect in-
formation rather than ”hallucinate,” as he believes ”confabulation” is the
more accurate psychological term for this phenomenon, which humans also
do regularly. Confabulations are memory-based fabrications, not sensory
experiences. In any case, the sequence of reasonings to solve these Bayesian
problems shows that the behaviors of LLMs are not fabrications.
However, they have a clear cognitive bias towards symbolic language
and reasoning. They autonomously and systematically use the language of
probabilities and conditional probabilities, and in several cases, they use the
formula of Bayes theorem.
How about phobia? A phobia contains an avoidance behavior. It is an
irrational fear of a specific object or activity, causing significant distress and
avoidance behavior when encountered. Some well-known phobias are claus-
trophobia, the fear of being closed in; numerophobia, the fear of numbers;
and chromophobia, the fear of colors. Similar to the observed phobia in
people [37], we found that LLMs´ Chain-of-Thoughts returns to the format
of probabilities. This is unfortunate because using LLMs could encourage
students to use the inappropriate format.
5
Conclusions
Understanding Bayesian reasoning is crucial. As (Pinker, 2021) argues, its
fluency is a ”public good” and an educational priority. LLMs with Chain-
of-Thought (CoT) offer a unique opportunity to teach this skill.
Their
”artificial inner voice” makes their reasoning process transparent, allowing
students to observe and learn from their step-by-step deliberations. Never-
theless, we found important limitations.
Although we did not find hallucinations or confabulations, we observed a
clear cognitive bias towards using probability language, with percentages or
fractions of the unity in decimals, and a proclivity to calculating with Bayes’
theorem. After testing with specific prompts, we also observed a degree of
resistance, Phobia, or an Einstellung effect when using frequencies, espe-
cially when using blocks and coloring. There seems to exist a predisposition
of LLMs to solve the Bayesian problems in a specific manner, even though
we prompted them to use the three ecologically valid strategies and asked
them to explain them to students. They do not seem aware that students
use other methods of reasoning.
In general, the LLM’s Chain-of-Thoughts are not entirely empathetic
19

--- Page 20 ---

with humans, do not use the bounded but proper mechanism of reasoning
that our brains have evolved, or do it inconsistently and superficially. They
rarely seem to use ecologically valid strategies from the beginning. They
forget that the task is to explain the reasoning to elementary school students.
Acknowledgments
Funding from ANID/PIA/Basal Funds for Centers of Excellence FB0003
/ Support 2024 AFB240004 and ANID Exploracion 13240075 are gratefully
acknowledged.
References
[1] Anil Ananthaswamy. How close is ai to human-level intelligence? Na-
ture, 636(8041):22–25, 2024.
[2] James WA Strachan, Oriana Pansardi, Eugenio Scaliti, Marco Celotto,
Krati Saxena, Chunzhi Yi, Fabio Manzi, Alessandro Rufo, Guido
Manzi, Michael SA Graziano, et al.
Gpt-4o reads the mind in the
eyes. arXiv preprint arXiv:2410.22309, 2024.
[3] Daniel C Dennett. The problem with counterfeit people. The Atlantic,
16, 2023.
[4] Daniel C Dennett. Intuition pumps and other tools for thinking. WW
Norton & Company, 2013.
[5] David Pinsof. ”deep” bullshit, 2024. Accessed: March 16, 2025.
[6] Daniel Kahneman and Amos Tversky. Subjective probability: A judg-
ment of representativeness. Cognitive psychology, 3(3):430–454, 1972.
[7] Hans Van Eyghen. Cognitive bias: Phylogenesis or ontogenesis? Fron-
tiers in Psychology, 13:892829, 2022.
[8] Steven Pinker. Rationality: What it is, why it seems scarce, why it
matters. Penguin, 2022.
[9] Joseph Henrich. The WEIRDest People in the World: How the West
Became Psychologically Peculiar and Particularly Prosperous. Straus
and Giroux, 2020.
[10] Dan M Kahan, Ellen Peters, Erica Cantrell Dawson, and Paul Slovic.
Motivated numeracy and enlightened self-government. Behavioural pub-
lic policy, 1(1):54–86, 2017.
[11] Roberto Araya. Is it feasible to teach agent-based computational mod-
eling to elementary and middle school students?
Proceedings of the
Singapore National Academy of Science, 16(01):71–84, 2022.
20

--- Page 21 ---

[12] Roberto Araya. What and how to teach mathematics for the future.
The Mathematician Educator, 4(2):84–108, 2023.
[13] Roberto Araya.
Enriching elementary school mathematical learning
with the steepest descent algorithm. Mathematics, 9(11):1197, 2021.
[14] Soledad Estrella, Maritza Mendez-Reina, Raimundo Olfos, and Joce-
lyn Aguilera. Early statistics in kindergarten: analysis of an educator’s
pedagogical content knowledge in lessons promoting informal inferen-
tial reasoning. International Journal for Lesson & Learning Studies,
11(1):1–13, 2022.
[15] Roberto Araya and Masami Isoda. Unplugged computational thinking
with colouring books. J. Southeast Asian Educ, 1:72–91, 2023.
[16] Assembly Bill 2876 California. Ab-2876 pupil instruction: media lit-
eracy: artificial intelligence literacy: curriculum frameworks: instruc-
tional materials, 2024. Accessed: March 16, 2025.
[17] Gerd Gigerenzer and Ulrich Hoffrage. How to improve bayesian rea-
soning without instruction: frequency formats. Psychological review,
102(4):684, 1995.
[18] Lisa Feldman Barrett. Seven and a half lessons about the brain. Mariner
Books, 2020.
[19] Rodolfo R Llin´as. I of the vortex: From neurons to self. MIT press,
2002.
[20] John Amos Comenius. Orbis sensualium pictus (the visible world in
pictures). Project Gutenberg, 1887.
[21] Jacques Hadamard. The mathematician’s mind: The psychology of in-
vention in the mathematical field. Princeton University Press, 2020.
[22] Roberto Araya, Patricio Calfucura, Abelino Jim´enez, Carlos Aguirre,
Mar´ıa Ang´elica Palavicino, Nancy Lacourly, Jorge Soto-Andrade, and
Pablo Dartnell. The effect of analogies on learning to solve algebraic
equations. Pedagogies: An International Journal, 5(3):216–232, 2010.
[23] Roberto Araya, Abelino Jim´enez, Manuel Bahamondez, Patricio Cal-
fucura, Pablo Dartnell, and Jorge Soto-Andrade. Teaching modeling
skills using a massively multiplayer online mathematics game. World
Wide Web, 17:213–227, 2014.
[24] Roberto Araya. Gamification strategies to teach algorithmic thinking
to first graders. In International Conference on Applied Human Factors
and Ergonomics, pages 133–141. Springer, 2021.
21

--- Page 22 ---

[25] Sebasti´an Tapia-Mandiola and Roberto Araya. From play to under-
standing: Large language models in logic and spatial reasoning coloring
activities for children. AI, 5(4):1870–1892, 2024.
[26] Narumon Changsri, Maitree Inprasitha, Roberto Araya, and Masami
Isoda. Enhancing students’ ideas of algorithm with coloring book in
mathematics classroom. In Psychology of Mathematics Education Con-
ference (PME 47). Rethinking Mathematics Education Together, 2024.
[27] Roberto Araya, Carlos Aguirre, and Mario Diaz.
Effect of embod-
ied argumentation with hand puppets in fourth-graders’ mathematical
thinking. IxD&A Interaction Design & Architecture(s) Journal, 2025.
in press.
[28] Herbert A Simon. Bounded rationality. Utility and probability, pages
15–18, 1990.
[29] Keith E Stanovich. Miserliness in human cognition: The interaction of
detection, override and mindware. Thinking & Reasoning, 24(4):423–
444, 2018.
[30] Philip N Johnson-Laird. Mental models and human reasoning. Proceed-
ings of the National Academy of Sciences, 107(43):18243–18250, 2010.
[31] Gerd Gigerenzer.
Embodied heuristics.
Frontiers in Psychology,
12:711289, 2021.
[32] Nicole Steib, Theresa B¨uchter, Andreas Eichler, Karin Binder, Stefan
Krauss, Katharina B¨ocherer-Linder, Markus Vogel, and Sven Hilbert.
How to teach bayesian reasoning:
An empirical study comparing
four different probability training courses. Learning and Instruction,
95:102032, 2025.
[33] Jorge Soto-Andrade. Missing the (bayesian) wood for the trees? In Ac-
tas del Tercer Congreso Internacional Virtual de Educaci´on Estad´ıstica.
Universidad de Granada, 2019.
[34] Liqi Zhu and Gerd Gigerenzer. Children can solve bayesian problems:
The role of representation in mental computation. Cognition, 98(3):287–
308, 2006.
[35] Robert Siegler and Roberto Araya. A computational model of conscious
and unconscious strategy discovery. In Advances in child development
and behavior, volume 33, pages 1–42. Elsevier, 2005.
[36] Leda Cosmides and John Tooby.
Are humans good intuitive statis-
ticians after all? rethinking some conclusions from the literature on
judgment under uncertainty. cognition, 58(1):1–73, 1996.
22

--- Page 23 ---

[37] Patrick Weber, Karin Binder, and Stefan Krauss. Why can only 24%
solve bayesian reasoning problems in natural frequencies: Frequency
phobia in spite of probability blindness. Frontiers in psychology, 9:1833,
2018.
[38] Michael Bond. Risk school: can the general public learn to evaluate risks
accurately, or do authorities need to steer it towards correct decisions?
michael bond talks to the two opposing camps. Nature, 461(7268):1189–
1193, 2009.
[39] Gary L Brase, Leda Cosmides, and John Tooby. Individuation, count-
ing, and statistical inference: the role of frequency and whole-object
representations in judgment under uncertainty. Journal of Experimen-
tal Psychology: General, 127(1):3, 1998.
[40] Queshonda J Kudaisi. The influence of unplugged lego activities on
middle grades students’ computational thinking dispositions in a stem
camp. Education Sciences, 15(2):143, 2025.
[41] LS Vygotsky.
Thinking and speaking (vol. 68).
Online Edi-
tion:
Filosoficky Casopis. Recuperado de https://www. marxists.
org/archive/vygotsky/works/words/Thinking-and-Speech. pdf, 1934.
[42] Roberto Araya. Colorea ideas. AutoMind, 2019.
[43] P Talwalkar. The taxi-cab problem. Mind Your Decisions, 5, 2013.
[44] Paul Seabright. The company of strangers: A natural history of eco-
nomic life. Princeton University Press, 2010.
[45] Keith E Stanovich, Richard F West, and Maggie E Toplak. The ratio-
nality quotient: Toward a test of rational thinking. MIT press, 2016.
[46] Gerd Gigerenzer, Wolfgang Gaissmaier, Elke Kurz-Milcke, Lisa M
Schwartz, and Steven Woloshin. Helping doctors and patients make
sense of health statistics. Psychological science in the public interest,
8(2):53–96, 2007.
[47] Keith E Stanovich. The bias that divides us: The science and politics
of myside thinking. MIT Press, 2021.
[48] Yoshua Bengio. Ai can learn to think before it speaks. Accessed: March
16, 2025.
[49] Shengran Hu and Jeff Clune. Thought cloning: Learning to think while
acting by imitating human thinking. Advances in Neural Information
Processing Systems, 36:44451–44469, 2023.
23

--- Page 24 ---

[50] Michael Bain and Claude Sammut.
A framework for behavioural
cloning. In Machine intelligence 15, pages 103–129, 1995.
[51] Martha Lewis and Melanie Mitchell.
Evaluating the robustness
of analogical reasoning in large language models.
arXiv preprint
arXiv:2411.14215, 2024.
[52] Samuel GB Johnson, Amir-Hossein Karimi, Yoshua Bengio, Nick
Chater, Tobias Gerstenberg, Kate Larson, Sydney Levine, Melanie
Mitchell, Iyad Rahwan, Bernhard Sch¨olkopf, et al. Imagining and build-
ing wise machines: The centrality of ai metacognition. arXiv preprint
arXiv:2411.02478, 2024.
[53] Ville Heilala, Roberto Araya, and Raija H¨am¨al¨ainen. Beyond text-to-
text: An overview of multimodal and generative artificial intelligence
for education using topic modeling. arXiv preprint arXiv:2409.16376,
2024.
[54] Lukasz Gawkeda, Marta Staszkiewicz, and Ryan P Balzan. The rela-
tionship between cognitive biases and psychological dimensions of delu-
sions: The importance of jumping to conclusions. Journal of behavior
therapy and experimental psychiatry, 56:51–56, 2017.
[55] Will Douglas Heaven. Geoffrey hinton tells us why he’s now scared of
the tech he helped build. MIT technology review, 2:2023, 2023.
24

```
