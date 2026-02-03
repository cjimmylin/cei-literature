---
title: "Steering Risk Preferences in Large Language - PDF Extract"
source_pdf: "2025-Zhu-Steering Risk Preferences in Large Language.pdf"
pages: 15
extracted_at: "2026-01-24T16:38:38.971928"
---

# PDF Extract: Steering Risk Preferences in Large Language

**Source PDF:** 2025-Zhu-Steering Risk Preferences in Large Language.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

arXiv:2505.11615v1  [cs.CL]  16 May 2025
Steering Risk Preferences in Large Language Models
by Aligning Behavioral and Neural Representations
Jian-Qiao Zhu∗
Department of Computer Science
Princeton University
Haijiang Yan∗
Department of Psychology
University of Warwick
Thomas L. Griffiths
Departments of Psychology and Computer Science
Princeton University
Abstract
Changing the behavior of large language models (LLMs) can be as straightforward
as editing the Transformer’s residual streams using appropriately constructed
“steering vectors.” These modifications to internal neural activations, a form of
representation engineering, offer an effective and targeted means of influencing
model behavior without retraining or fine-tuning the model. But how can such
steering vectors be systematically identified? We propose a principled approach
for uncovering steering vectors by aligning latent representations elicited through
behavioral methods (specifically, Markov chain Monte Carlo with LLMs) with their
neural counterparts. To evaluate this approach, we focus on extracting latent risk
preferences from LLMs and steering their risk-related outputs using the aligned
representations as steering vectors. We show that the resulting steering vectors
successfully and reliably modulate LLM outputs in line with the targeted behavior.
1
Introduction
LLMs are increasingly deployed in risk-sensitive domains such as finance [22] and healthcare [1]. In
these high-stakes applications, it is essential to develop reliable methods for aligning the behavior of
LLMs with human values and safety requirements [9, 21]. One solution to this problem is steering, a
term that refers to any targeted intervention (whether through model weights, decoding strategies,
prompts, or internal neural activations) intended to control or shape a model’s outputs. Steering
risk-related behavior in LLMs is one way to ensure alignment with humans in risky domains.
Steering the risk preferences of a pretrained LLM, however, is inherently challenging due to the
opacity of these models. LLMs operate over vast weight spaces, and their outputs are highly context-
dependent [4, 42], making it difficult to isolate or manipulate any specific internal variable that
governs risk preference. Existing steering techniques, such as prompt engineering or supervised fine-
tuning, either lack the granularity needed to target specific latent representation or require extensive
retraining and human supervision [25, 45].
Given the context-dependent and probabilistic nature of LLM outputs, we propose that their un-
derlying risk preferences are best characterized as probabilistic representations. That is, the same
risky decision may yield different completions depending on subtle variations in input phrasing
or prompt structure [42, 4]. This view suggests that an LLM’s underlying risk preferences can
be recovered by sampling its behavior over many such comparisons. To operationalize this idea,
∗Equal contribution. Correspondence to: Jian-Qiao Zhu <jz5204@princeton.edu>
Preprint. Under review.

--- Page 2 ---

we measure the risk preferences of LLMs using a method based on Markov chain Monte Carlo
(MCMC; [28]), using repeated choices by the model to define a Markov chain that converges to a
probability distribution that captures these preferences. This approach has previously been used to
elicit probabilistic representations in other settings from both humans and LLMs [23, 8, 44].
Measuring the risk preferences of LLMs in this way creates the opportunity to build a bridge between
the observed behavior and the activations of nodes in the underlying neural network [30]. We can
align the behavioral representations we find with the neural representations within LLMs and use this
alignment to derive a steering vector that captures underlying risk preferences. When this vector is
injected back into the model at inference time, it enables precise control of the model’s risk-related
behavior. We refer to this approach as self-alignment, since it leverages the model’s own emergent
representations for behavior control.
To evaluate this method, we apply steering vectors derived from the aligned representation across
three domains: risky decision-making, risk perception, and risk-related text generation. Our results
demonstrate that self-alignment yields substantially greater control over model behavior than two
other baselines: (i) the Contrastive Activation approach, which derives steering vectors from prompt
pairs, and (ii) a Certainty Equivalent control condition that uses an alternative behavioral elicitation.
Our results also demonstrate that the modified risk preferences transfer to tasks that are quite far away
from the choices from which the steering vectors were derived.
2
Background
AI safety and value alignment. AI safety research has long emphasized the importance of aligning
artificial systems with human values, though explicitly encoding such values in machines remains a
formidable challenge [27]. The emergence of LLMs presents new opportunities in this regard, as
LLMs have been shown to internalize commonsense knowledge and human norms from large-scale
training data [10, 21, 19]. Consequently, many researchers now argue that, given sufficient data,
LLMs can approximate shared norms [4]. At the same time, however, this capacity introduces
new challenges for interpretability, as it becomes increasingly difficult to discern the underlying
factors that drive LLM behavior. In this work, we propose a novel strategy that leverages emergent
representations in LLMs by eliciting the same latent construct through both behavioral and neural
means. This dual elicitation facilitates self-alignment between behavior and neural activations,
providing an interpretable method for steering LLM outputs.
LLM steering. A range of approaches has been proposed to influence the outputs of pretrained
LLMs, which can broadly be categorized as different forms of intervention. These interventions vary
in where and how they modify the model. Weight-level interventions include techniques such as
supervised fine-tuning [25] and reinforcement learning with human feedback [45], which directly
update model parameters. Alternatively, decoding-level interventions, such as trainable decoding,
modify the output generation process while keeping model weights fixed [6]. Prompt engineering can
be viewed as an intervention on the input space, shaping model behavior through carefully constructed
prompts [40, 39]. Moreover, activation-level interventions, which typically freeze the model weights
and instead search for steering vectors, offer an alternative to behavioral control. These vectors can be
discovered through gradient-based optimization [11] or computed directly from contrastive prompt
pairs [15, 32]. In this work, we propose an alignment-based method for deriving steering vectors by
aligning behavioral and neural representations of latent constructs such as risk preference.
3
Method
The key idea behind our proposed method is to derive a steering vector that optimally aligns the
model’s behavioral and neural representations of risk preference (see Figure 1a). Our method proceeds
in two main steps, described below.
Step 1: Eliciting behavioral representations of risk via MCMC. Risk preference, like many
other mental representations, is inherently unobservable. However, as demonstrated in cognitive
psychology, such latent constructs can be inferred from observed behavior [13, 28, 8]. Drawing
inspiration from recent work on behavioral elicitation in LLMs [41, 44, 5], we incorporate LLMs into
a MCMC sampler to effectively elicit their behavioral representation of risk. A variety of sampling
algorithms can be used for this purpose, including the Metropolis-Hastings algorithm [44, 28] and
2

--- Page 3 ---

risk 
preference
Risky 
behavior
Neural 
activations
Aligned 
representation
Given the following gambles:  
Option A offers a 5% chance to win $100 and 95% 
chance to win $0;  
Option B offers a 100% chance to win $5.  
Please select either option A or option B to play.
Steering vector
Transformer 
residual stream
Layer n
positive 
steer
Option A
negative 
steer
Option B
a
b
Figure 1: Aligned steering vectors. (a) Overview of the proposed method for generating steering
vectors by aligning representations of risk preference derived from behavioral and neural elicitation.
(b) During inference, the steering vector is injected into the residual stream at all token positions to
control LLM outputs. When the steering vector is applied with a positive multiplier (i.e., positive
steering), the LLM is expected to exhibit more risk-seeking behavior. Conversely, applying a negative
multiplier (i.e., negative steering) is expected to induce more risk-averse behavior.
Gibbs sampling [8]. The core intuition is to use the LLM to define the proposal or acceptance
mechanism, such that the resulting sequence of samples produced by the Markov chain converges to
a stationary distribution that reflects the model’s latent representations [44, 23, 8, 14, 38, 28].
Specifically, we adapted the procedure established by [23], which has been successfully used to elicit
human risk preferences, to the LLM setting. In each trial, the LLM is prompted to choose between
two gambles, A and B. In our implementation, all gambles consist of three possible outcomes: $0, $50,
and $100. While the outcome values are fixed, the probabilities associated with each outcome vary
across gambles. After the LLM makes a choice, the selected gamble is retained, and the unchosen
option is replaced with a newly generated gamble. The probabilities for this new gamble are randomly
sampled from a Dirichlet distribution: Dir(1, 1, 1). In the next trial, the retained and newly generated
gambles are presented again (with their order randomized), and the LLM is asked to make another
choice. Importantly, no choice history is provided in the prompt: each decision is made solely based
on the current pair of gambles presented. The sequence of choices made by the LLM forms the
foundation for constructing its behavioral representation of risk. Specifically, within the space of
all possible gambles, represented as a probability triangle2, the LLM’s choices allow us to infer a
probability distribution over gambles reflecting its preferences across risk profiles (see Figure 2).
More formally, MCMC begins at an initial state z (i.e., a specific gamble from the probability triangle).
A proposed next state z′ is drawn from a proposal distribution q(z′|z), and is then evaluated under the
target distribution π (i.e., latent representation of risk) to determine whether it should be accepted as
the new state or rejected in favor of retaining the current state z. To guarantee that the Markov chain
converges to π, it is sufficient to satisfy the condition of detailed balance (along with ergodicity):
π(z)q(z′|z)A(z′, z) = π(z′)q(z|z′)A(z, z′)
(1)
where q(z′|z) is the probability of proposing z′ from state z, and A(z′, z) is the probability of
accepting proposal z′ over z. In our case, we use a symmetric proposal distribution (i.e., q(z′|z) =
q(z|z′)), which simplifies the detailed balance condition to: π(z)A(z′, z) = π(z′)A(z, z′). One way
to satisfy this condition is by using the Barker acceptance function [2]:
A(z′, z) =
π(z′)
π(z) + π(z′)
(2)
This acceptance rule is particularly appropriate for modeling LLM behavior, as it closely resembles
well-known stochastic choice models such as Luce’s choice rule [17] and the Bradley–Terry model
[26], which has been applied in LLM post-training and preference alignment. As a result, by
sequentially presenting pairs of risky choice alternatives to an LLM, the set of selected options can
be interpreted as samples from a probability distribution whose density is proportional to the LLM’s
latent representation of risk [23].
2In the economics literature, this triangle is also known as the Marschak–Machina probability triangle
[20, 18], a method traditionally used to qualitatively differentiate among competing theories of risky choice [37].
Our MCMC approach provides a non-parametric estimation of the LLM’s risk representation within this triangle.
3

--- Page 4 ---

a
Certainty Equivalent
60% $0;  
20% $100;  
20% $50
20% $0;  
80% $100;  
0% $50
Markov chain Monte Carlo
b
Figure 2: Elicited risk preferences from Gemma-2-9B-Instruct using behavioral methods. (a)
Certainty Equivalent method. (b) Markov chain Monte Carlo with LLM. Each triangle represents
the probability simplex over three-outcome gambles ($0, $50, and $100), where the sum of outcome
probabilities equals one. The MCMC-with-LLM elicitation reveals more nuanced and structured
contours of risk preference compared to the Certainty Equivalent method. Higher values indicate a
stronger preference for the gamble by the Gemma model.
Step 2: Aligning behavioral and neural representations to compute steering vectors. Given
the behavioral representations of risk elicited via MCMC with LLM, we next sought to align them
with the model’s internal neural activations. To obtain corresponding neural representations of risk
preference for each gamble, we prompted the same LLM to evaluate the attractiveness of the gamble
when hypothetically offered (see Appendix A.4 for details). We then aligned the two representations
by regressing the behavioral estimates onto the neural activations. Specifically, we treated the neural
activations as independent variables and the behavioral responses as dependent variables, using Lasso
regression with an L1 penalty of 10. The resulting regression coefficients, corresponding to neurons
in the Transformer’s residual stream, are interpreted as reflecting the LLM’s risk preference and are
thus used as the steering vector.
4
Other Methods
Contrastive Activation. Another simple yet effective method for computing steering vectors is to
contrast intermediate neural activations on carefully selected prompt pairs–a technique known as
Contrastive Activation [24, 32]. For example, to steer LLM outputs toward more positive sentiment,
Contrastive Activation compares the model’s internal activations on a contrasting pair of prompts
such as “Love” and “Hate” [32]. The difference between these activations is treated as the steering
vector, which is then added to the model’s residual stream during inference. This shifts the model’s
internal representations along the desired semantic direction (e.g., toward “Love” and away from
“Hate”), resulting in completions that reflect more positive sentiment.
To adapt Contrastive Activation to the task of steering LLM risk preferences, we constructed a list of
words associated with “Risk” and “Safety” (see Appendix A.1 for details). Following the standard
procedure for computing steering vectors in Contrastive Activation, we extracted the residual stream
activations of the LLM for each word across multiple layers. The steering vector was computed as
the average difference in residual activations between the risk-related and safety-related word pairs.
Certainty Equivalent. Finally, we consider an alternative behavioral method for eliciting individuals’
risk preferences that is widely used in economics and psychology: the Certainty Equivalent. The
Certainty Equivalent refers to the sure amount of money a person is willing to accept in place of a
risky gamble [35, 12]. In other words, it represents the value at which an individual is indifferent
between receiving a certain payoff or a probabilistic outcome. This measure serves as a behavioral
4

--- Page 5 ---

proxy for risk preference: individuals are classified as risk-averse if their Certainty Equivalent is
lower than the gamble’s expected value, risk-neutral if it is equal, and risk-seeking if it is higher.
In our task, the Certainty Equivalent serves as a direct control condition for the risk representations
elicited via MCMC. Specifically, we elicited the LLM’s Certainty Equivalent for all gambles previ-
ously used in the MCMC procedure. This produces an alternative behavioral representation of risk,
based on Certainty Equivalents rather than MCMC, while holding the set of gambles constant.
5
Experiments
In this work, we focus on steering the risk preferences of Gemma-2-9B-Instruct [31], which serves as
our primary target LLM. We also replicate the main experiments using the smaller-scale Gemma-2-
2B-Instruct (see Appendix E). The temperature was fixed at 1 for behavioral elicitation.
Behavioral elicitation of risk representations. For both the MCMC with LLM and Certainty
Equivalent methods, we derive steering vectors from behaviorally aligned representations of risk.
That is, these approaches rely on first eliciting the model’s risk preferences through behavioral
methods. To obtain a quantitative characterization of these preferences, we focus on the space of
gambles defined over the probability triangle (see Figure 2).
In the Certainty Equivalent method, we probed Gemma-2-9B-Instruct by densely sampling gambles
across the probability triangle. For each gamble, the model was prompted to report its certainty
equivalent. These responses were then aggregated and normalized across all sampled gambles to
produce the density plot shown in Figure 2a.
Similarly, for the MCMC with LLM method, we embedded the Gemma model within a MCMC
sampler, prompting it to accept or reject newly proposed gambles through binary choices. The space
of gambles was identical to that used in the Certainty Equivalent method (i.e., the probability triangle).
The Markov chain consisted of 3,000 such binary choices. The resulting risk representation elicited
via MCMC (smoothed using a Dirichlet kernel of width 0.09 that preserves probability triangle
boundaries) is shown in Figure 2b. Note that the behavioral representation derived from MCMC
reveals more nuanced gradients in the density plot, highlighting a stark contrast with the coarser
structure observed in the Certainty Equivalent method.
Steering vectors for both the MCMC and Certainty Equivalent methods were computed using Lasso
regression to align behavioral and neural representations (see Appendix B for a comparison). In
contrast, the steering vector for the Contrastive Activation method was derived by computing the
difference in neural activations between pairs of risk-related and safety-related words. Steering
vectors were normalized by division by their Euclidean norm.
Table 1: Gambles used to evaluate the effectiveness of steering LLMs’ risky decision-making. Risky
options are expressed in the format {probability, outcome}; the remaining probability corresponds to
receiving nothing.
Outcome probability
High
Low
Gains
{80%, $4000} vs $3000
{5%, $100} vs $5
Losses
{80%, -$4000} vs -$3000
{5%, -$100} vs -$5
Steering LLM risky choices. Having obtained three steering vectors (derived from MCMC with
LLM, Contrastive Activation, and Certainty Equivalent methods), we now evaluate the effectiveness
of the three steering vectors in controlling LLM’s risky decision-making. Our analysis focuses on a
set of four gambles that have been foundational in the study of the fourfold pattern of risk preferences
[12]. This well-documented pattern describes how human decision-makers tend to be risk-seeking
when the probability of a positive outcome is low and when the probability of a negative outcome is
high; conversely, they tend to be risk-averse when the probability of a positive outcome is high and
when the probability of a negative outcome is low (see Table 1 for examples).
To steer the LLM’s decisions toward greater risk-seeking or risk-aversion, we prompted the Gemma
model with the gambles shown in Table 1, framed as binary choices between options A and B. During
inference, steering vectors (scaled by a predefined multiplier ranging between -900 to +900) were
5

--- Page 6 ---

a
b
Markov chain Monte Carlo
Contrastive Activation
Certainty Equivalent
Steerability
Layers
Layers
Layers
Greater risk-
seeking
Greater risk-
aversion
Unsteered 
baseline
Excessive steered choice 
probabilities of risky option
Steering multipliers
Steering multipliers
Steering multipliers
Steering multipliers
Stronger 
positive steer
Stronger 
negative steer
Stronger 
negative steer
Stronger 
positive steer
Stronger 
positive steer
Stronger 
negative steer
Low Probability (Gains)
High Probability (Gains)
Low Probability (Losses)
High Probability (Losses)
Figure 3: Steering risky decisions of Gemma-2-9B-Instruct. (a) Steerability results using steering
vectors derived from Contrastive Activation (blue), Certainty Equivalent (green), and MCMC (red).
Darker colors indicate larger steering multipliers. The optimal layers for steering, identified by
the highest steerability at the maximum multiplier, are layers 41, 39, and 39 for the three methods,
respectively (marked with stars). (b) Change in choice probabilities for the risky option after steering,
using the best layer for each method. The vertical axis reflects the difference from the unsteered
baseline probabilities across the four gambles.
added to the model’s residual stream at each token position. The model then continued its forward
pass to the output layer, where we extracted the token probabilities for “A” and “B” from the final
logits. These probabilities were normalized and then used to quantify the model’s choice behavior
under different steering conditions.
We first evaluated which Transformer layer contains the most effective residual stream for steering.
To do so, we examined the model’s behavior under extreme steering conditions, using multipliers
of –900 and +900. For each layer, we computed the steered choice probabilities with each steering
multiplier. We then quantified steerability as the average difference in choice probabilities across four
gambles (see Figure 3a), defined as:
Steerability = 1
4
4
X
i=1

ppositive(zi) −pnegative(zi)

(3)
where zi denotes the i-th gamble prompted to the LLM, ppositive(zi) is the model’s probability of
choosing the risky option under positive steering, and pnegative(zi) is the corresponding probability
under negative steering of equal magnitude.
As shown in Figure 3b, we compared the steered choice probabilities for the risky option by subtracting
the baseline (unsteered) choice probabilities. A value of zero therefore indicates no change relative
to the unsteered baseline. We find that the steering vector derived from the Contrastive Activation
method has limited impact on altering the Gemma model’s choice behavior. In contrast, steering
vectors computed by aligning behavioral and neural representations (i.e., both Certainty Equivalent
and MCMC methods) are effective in controlling the Gemma model’s risky decision-making, shifting
it toward greater risk-seeking under positive steering and greater risk aversion under negative steering.
Steering LLM risk perception. While studying abstract gambles provides valuable insights into an
agent’s risk preferences, psychologists have also used more naturalistic stimuli to assess people’s
perception of risk in real-world contexts such as “cheating on an exam” or “forging someone’s
signature” [36, 29]. LLMs, by virtue of their broad training data, are presumably capable of forming
meaningful risk perceptions about such real-world events [21, 32]. Indeed, recent work has shown
that LLM embeddings account for a substantial portion of the variance in human risk perception [3].
Here, we investigate the extent to which an LLM’s risk perception can be steered using the same set
of steering vectors derived in the preceding analyses.
6

--- Page 7 ---

a
b
Markov chain Monte Carlo
Contrastive Activation
Certainty Equivalent
Steerability
Layers
Layers
Layers
Higher ratings
Lower ratings
Unsteered baseline
Excessive ratings 
of risky events
Steering multipliers
Stronger 
positive steer
Stronger 
negative steer
Stronger 
negative steer
Stronger 
positive steer
Stronger 
positive steer
Stronger 
negative steer
Risk Perception
Figure 4: Steering risk perception of Gemma-2-9B-Instruct. (a) Steerability results using steering
vectors derived from Contrastive Activation (blue), Certainty Equivalent (green), and MCMC (red).
Darker colors represent larger steering multipliers. The optimal layers for steering, identified by the
highest steerability at the maximum multiplier, are layers 2, 28, and 8 for the respective methods
(marked with stars). (b) Change in average risk ratings for real-world events after steering, using the
optimal layer for each method. The vertical axis reflects the deviation from the unsteered baseline
rating. Each violin plot displays the distribution of ratings, with the white bar indicating the median
and the black box representing the interquartile range up to the 75th percentile.
We prompted Gemma-2-9B-Instruct to rate real-world risky events using integers from 1 (not risky at
all) to 7 (extremely risky). The full set included 150 risky events curated by [3], spanning a range of
domains: ethical (e.g., “passing off somebody else’s work as your own”), financial (e.g., “betting
at the horse races”), health-related (e.g., “consuming excessive amounts of alcohol”), sports (e.g.,
“bungee jumping”), and social (e.g., “trusting a stranger with your personal information”). As in
previous experiments, we modified the residual stream during inference by injecting the steering
vectors. However, instead of focusing on choices between options A and B, we extracted the model’s
output logits for the integer tokens “1” through “7.” These token probabilities were then normalized
to yield a distribution reflecting the model’s perceived risk level for each event.
Analogous to the steerability metric used for risky decisions, we define steerability for risk perception
as the average difference in risk ratings across all real-world events between positive and negative
steering conditions. However, by comparing the most steerable layers for risky decisions (Figure
3a) and risk perceptions (Figure 4a), we find that risk perceptions are more effectively influenced at
earlier layers, whereas risky decisions are more steerable in later layers closer to the output of the
Gemma model. This finding aligns with psychological evidence suggesting that perceptual processes
occur earlier than decision-making processes in the cognitive hierarchy [34].
To evaluate the influence of steering vectors on model-generated ratings, we conducted two separate
two-way repeated-measures ANOVAs for positive and negative steering conditions. For positive
steering, the analysis revealed a significant main effect of steering method, F(2, 298) = 1717.09, p <
.01, a significant main effect of steering multiplier, F(4, 596) = 2503.30, p < .01, and a significant
interaction between method and multiplier, F(8, 1192) = 1507.64, p < .01. Follow-up paired
t-tests comparing steered ratings showed that the MCMC method significantly outperformed both
the Certainty Equivalent method (t(149) = 2.41, p < .01) and the Contrastive Activation method
(t(149) = 88.95, p < .01). Additionally, the Certainty Equivalent method significantly outperformed
the Contrastive Activation method (t(149) = 38.90, p < .01).
Similarly, for negative steering, the two-way repeated-measures ANOVA revealed significant main
effects of steering method (F(2, 298) = 265.04, p < .01), steering multiplier (F(4, 596) =
832.89, p < .01), and their interaction (F(8, 1192) = 283.95, p < .01). Follow-up paired t-tests
7

--- Page 8 ---

a
b
Contrastive Activation
Certainty Equivalent
c
Markov chain Monte Carlo
Positive steer (risk seeking)
Negative steer (risk averse)
-500
-900
500
900
-500
-900
500
900
-500
-900
500
900
Figure 5: Steering text generation for real-world risky events in Gemma-2-9B-Instruct. Text
outputs generated by injecting steering vectors into the residual stream at the final layer of the
model during inference. Steering vectors are derived from (a) Contrastive Activation, (b) Certainty
Equivalent, and (c) MCMC with LLM methods. Each word cloud represents the frequency distribution
of words used in the model’s completions under different steering conditions. The corresponding
steering multiplier is indicated below each word cloud.
showed that the MCMC method significantly outperformed both the Certainty Equivalent method
(t(149) = 16.07, p < .01) and the Contrastive Activation method (t(149) = 11.40, p < .01). More-
over, the Contrastive Activation method yielded significantly better performance than the Certainty
Equivalent method (t(149) = 16.70, p < .01).
Steering text generation for risky events in LLM. Finally, beyond quantitative evaluations based
on choice probabilities and risk ratings, we also examine whether modifying the final layer’s residual
stream at inference time systematically alters the textual outputs of the Gemma model. Using the
same set of 150 real-world risky events described above [3], we prompted the model with the sentence
“I think {event}”, where {event} is replaced with each risky scenario (e.g., “I think cheating on an
exam ___” or “I think consuming excessive amounts of alcohol ___”). Steering vectors were injected
into the final layer’s residual stream at each subsequent token position during generation.
To give a visual idea of how steering influences model-generated text, we created word clouds that
reflect the frequency of word usage following the application of steering vectors (see Figure 5).
Overall, the Gemma model recognizes the inherent risk in the real-world events presented. However,
when the residual stream at the final layer is positively steered toward risk-seeking behavior using the
vector derived from the MCMC method, we observe a noticeable attenuation in the model’s perceived
risk. For example, completions more frequently include phrases such as “slightly risky” and “a minor
offense” (see Figure 5c). In contrast, applying the same steering vector with a negative multiplier leads
the model to amplify perceived risk, generating more cautionary or morally disapproving language,
such as “wrong,” “never right,” and “not something I would ever do.” Table 2 presents representative
examples of text completions generated by the model under different steering conditions.
6
Discussion
We investigated the use of aligned behavioral and neural representations of risk to steer LLM
behavior across three risk-related domains: risky decision-making, risk perception, and text generation
involving real-world risky events. In all three domains, steering vectors derived from aligned
representations (i.e., the Certainty Equivalent and MCMC methods) consistently outperformed those
generated via Contrastive Activation. These results suggest that self-alignment methods, which align
the same latent construct elicited through both behavior and neural activations, offer a more effective
and principled means of controlling LLM behavior in risk-sensitive contexts.
8

--- Page 9 ---

Table 2: Example steered text completions generated by Gemma-2-9B-Instruct using a steering
multiplier of 900. CA refers to Contrastive Activation, CE to Certainty Equivalent, and MCMC to
Markov chain Monte Carlo with LLM.
Risky event
Steering
method
Negative steer
(risk averse)
Positive steer
(risk seeking)
I think cheating on an exam...
CA
is wrong because
it undermines the
integrity of the educational
system and devalues
the achievements of those
who uphold ethical standards.
is wrong.
CE
is absolutely wrong
and absolutely not
worth the consequences.
is a weak move.
MCMC
is wrong.
is a very bad idea.
I mean, sure, maybe
you might get a slightly
better grade, but in
the long run, it’s
just going to compromise
your learning.
I think stealing an additional
TV cable connection off
the one you pay for...
CA
is unethical.
is stealing.
CE
is not ethical and
could have serious
consequences.
is slightly unethical.
MCMC
is not ethical.
is a slightly more minor
offense compared to some
other types of theft.
I think riding a motorcycle...
CA
is a great way to
experience freedom and
independence, especially for
those who enjoy the outdoors
and the wind in their hair.
However, it’s important
to remember that motorcycling
involves inherent risks.
is about more than just getting
from point A to point B.
It’s about the feeling.
CE
is absolutely amazing.
The open air, the
wind in your hair,
the feeling of freedom
and escape - it’s
truly unique.
is a rewarding but risky
passtime. I enjoy the feeling
of freedom and control
I get while riding,
but I also understand
the dangers involved.
MCMC
is not for everyone.
It’s not just about
physical ability, it’s also
about mental and emotional
preparedness.
is a very exhilarating
experience. I enjoy the
feeling of the wind
in my hair and the freedom
of the open road.
Limitations and future research. While it is intuitive that self-aligned representations can be used
to steer model behavior related to the underlying latent construct, further theoretical and mechanistic
interpretability research is needed to establish a more concrete link between behaviorally elicited
representations and their corresponding neural activations. Moreover, modifying a Transformer’s
residual stream is not uniformly effective across all layers; the success of such interventions is highly
dependent on the layer selected. Identifying optimal layers for steering remains an open question
9

--- Page 10 ---

for future research. Finally, this form of steering is limited in scope for proprietary models where
weights are not accessible, restricting its broader applicability.
Acknowledgments. This work and related results were made possible with the support of the NOMIS
Foundation. HY acknowledges the Chancellor’s International Scholarship from the University of
Warwick for additional support.
References
[1] Mostafa Abdou, Razia S Sahi, Thomas D Hull, Erik C Nook, and Nathaniel D Daw. Leveraging
large language models to estimate clinically relevant psychological constructs in psychotherapy
transcripts. medRxiv, pages 2025–03, 2025.
[2] Anthony Alfred Barker. Monte Carlo calculations of the radial distribution functions for a
proton-electron plasma. Australian Journal of Physics, 18(2):119–134, 1965.
[3] Sudeep Bhatia. Exploring variability in risk taking with large language models. Journal of
Experimental Psychology: General, 153(7):1838, 2024.
[4] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are
few-shot learners. Advances in Neural Information Processing Systems, 33:1877–1901, 2020.
[5] Alexander Capstick, Rahul G Krishnan, and Payam Barnaghi. Using large language models for
expert prior elicitation in predictive modelling. arXiv preprint arXiv:2411.17284, 2024.
[6] Aditya Grover, Jiaming Song, Ashish Kapoor, Kenneth Tran, Alekh Agarwal, Eric J Horvitz, and
Stefano Ermon. Bias correction of learned generative models using likelihood-free importance
weighting. Advances in Neural Information Processing Systems, 32, 2019.
[7] David W Harless. Predictions about indifference curves inside the unit triangle: A test of variants
of expected utility theory. Journal of Economic Behavior & Organization, 18(3):391–414,
1992.
[8] Peter Harrison, Raja Marjieh, Federico Adolfi, Pol van Rijn, Manuel Anglada-Tort, Ofer
Tchernichovski, Pauline Larrouy-Maestri, and Nori Jacoby. Gibbs sampling with people.
Advances in Neural Information Processing Systems, 33:10659–10671, 2020.
[9] Dan Hendrycks. Introduction to AI safety, ethics, and society. Taylor & Francis, 2025.
[10] Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song, and Jacob
Steinhardt. Aligning AI with shared human values. arXiv preprint arXiv:2008.02275, 2020.
[11] Evan Hernandez, Belinda Z Li, and Jacob Andreas. Inspecting and editing knowledge represen-
tations in language models. arXiv preprint arXiv:2304.00740, 2023.
[12] Daniel Kahneman, Amos Tversky, et al. Prospect theory: An analysis of decision under risk.
Econometrica, 47(2):363–391, 1979.
[13] Paul Kay and Richard S Cook. World color survey. In Encyclopedia of Color Science and
Technology, pages 1601–1607. Springer, 2023.
[14] Pablo León-Villagrá, Kay Otsubo, Christopher G Lucas, and Daphna Buchsbaum. Uncovering
category representations with linked mcmc with people. In Proceedings of the Annual Meeting
of the Cognitive Science Society, volume 42, 2020.
[15] Kenneth Li, Oam Patel, Fernanda Viégas, Hanspeter Pfister, and Martin Wattenberg. Inference-
time intervention: Eliciting truthful answers from a language model. Advances in Neural
Information Processing Systems, 36:41451–41530, 2023.
[16] Ryan Liu, Jiayi Geng, Joshua C Peterson, Ilia Sucholutsky, and Thomas L Griffiths. Large
language models assume people are more rational than we really are.
arXiv preprint
arXiv:2406.17055, 2024.
10

--- Page 11 ---

[17] R Duncan Luce et al. Individual choice behavior, volume 4. Wiley New York, 1959.
[18] Mark J Machina. “Expected utility”’ analysis without the independence axiom. Econometrica:
Journal of the Econometric Society, pages 277–323, 1982.
[19] Raja Marjieh, Ilia Sucholutsky, Pol van Rijn, Nori Jacoby, and Thomas L Griffiths. Large
language models predict human sensory judgments across six modalities. Scientific Reports,
14(1):21445, 2024.
[20] Jacob Marschak. Rational behavior, uncertain prospects, and measurable utility. Econometrica,
18(2):111–141, 1950.
[21] Mantas Mazeika, Xuwang Yin, Rishub Tamirisa, Jaehyuk Lim, Bruce W Lee, Richard Ren,
Long Phan, Norman Mu, Adam Khoja, Oliver Zhang, et al. Utility engineering: Analyzing and
controlling emergent value systems in ais. arXiv preprint arXiv:2502.08640, 2025.
[22] Paweł Niszczota and Sami Abbas. Gpt as a financial advisor. Available at SSRN 4384861, 2023.
[23] Takao Noguchi, Adam Sanborn, and Neil Stewart. Non-parametric estimation of the individual’s
utility map. In Proceedings of the Annual Meeting of the Cognitive Science Society, volume 35,
2013.
[24] Nina Panickssery, Nick Gabrieli, Julian Schulz, Meg Tong, Evan Hubinger, and Alexander Matt
Turner. Steering Llama 2 via contrastive activation addition. arXiv preprint arXiv:2312.06681,
2023.
[25] Xiangyu Qi, Yi Zeng, Tinghao Xie, Pin-Yu Chen, Ruoxi Jia, Prateek Mittal, and Peter Henderson.
Fine-tuning aligned language models compromises safety, even when users do not intend to!
arXiv preprint arXiv:2310.03693, 2023.
[26] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and
Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model.
Advances in Neural Information Processing Systems, 36:53728–53741, 2023.
[27] Stuart Russell. Human-Compatible Artificial Intelligence. Viking, 2022.
[28] Adam Sanborn and Thomas Griffiths. Markov chain Monte Carlo with people. Advances in
Neural Information Processing Systems, 20, 2007.
[29] Paul Slovic. Perception of risk. Science, 236(4799):280–285, 1987.
[30] Ilia Sucholutsky, Lukas Muttenthaler, Adrian Weller, Andi Peng, Andreea Bobu, Been Kim,
Bradley C Love, Erin Grant, Iris Groen, Jascha Achterberg, et al. Getting aligned on representa-
tional alignment. arXiv preprint arXiv:2310.13018, 2023.
[31] Gemma Team, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin,
Surya Bhupatiraju, Léonard Hussenot, Thomas Mesnard, Bobak Shahriari, Alexandre Ramé,
et al.
Gemma 2: Improving open language models at a practical size.
arXiv preprint
arXiv:2408.00118, 2024.
[32] Alexander Matt Turner, Lisa Thiergart, Gavin Leech, David Udell, Juan J Vazquez, Ulisse Mini,
and Monte MacDiarmid. Steering language models with activation engineering. arXiv preprint
arXiv:2308.10248, 2023.
[33] Amos Tversky and Daniel Kahneman. Advances in prospect theory: Cumulative representation
of uncertainty. Journal of Risk and Uncertainty, 5:297–323, 1992.
[34] Rufin VanRullen and Simon J Thorpe. The time course of visual processing: from early
perception to decision-making. Journal of Cognitive Neuroscience, 13(4):454–461, 2001.
[35] John von Neumann and Oskar Morgenstern. Theory of Games and Economic Behavior. Prince-
ton University Press, 1947.
11

--- Page 12 ---

[36] Elke U Weber, Ann-Renee Blais, and Nancy E Betz. A domain-specific risk-attitude scale: Mea-
suring risk perceptions and risk behaviors. Journal of Behavioral Decision Making, 15(4):263–
290, 2002.
[37] George Wu and Richard Gonzalez. Common consequence conditions in decision making under
risk. Journal of Risk and Uncertainty, 16:115–139, 1998.
[38] Haijiang Yan, Christian Tsvetkov, Nick Chater, and Adam Sanborn. Quickly recovering
comprehensive individual mental representations of facial affect. OSF, 2024.
[39] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L Griffiths, Yuan Cao, and
Karthik Narasimhan. Tree of thoughts: Deliberate problem solving with large language models.
Advances in Neural Information Processing Systems, 36:11809–11822, 2023.
[40] Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan,
and Jimmy Ba. Steering large language models using ape. In NeurIPS ML Safety Workshop,
2022.
[41] Jian-Qiao Zhu and Thomas L Griffiths. Eliciting the priors of large language models using
iterated in-context learning. arXiv preprint arXiv:2406.01860, 2024.
[42] Jian-Qiao Zhu and Thomas L Griffiths. Incoherent probability judgments in large language
models. arXiv preprint arXiv:2401.16646, 2024.
[43] Jian-Qiao Zhu, Haijiang Yan, and Thomas L Griffiths. Language models trained to do arithmetic
predict human risky and intertemporal choice. arXiv preprint arXiv:2405.19313, 2024.
[44] Jian-Qiao Zhu, Haijiang Yan, and Thomas L Griffiths. Recovering mental representations from
large language models with Markov Chain Monte Carlo. In Proceedings of the Annual Meeting
of the Cognitive Science Society, volume 46, 2024.
[45] Daniel M Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B Brown, Alec Radford, Dario Amodei,
Paul Christiano, and Geoffrey Irving. Fine-tuning language models from human preferences.
arXiv preprint arXiv:1909.08593, 2019.
A
Prompts
A.1
Words for Contrastive Activation
Risk words: ‘risk’, ‘uncertainty’, ‘danger’, ‘volatility’, ‘loss’, ‘gamble’, ‘exposure’, ‘threat’, ‘hazard’,
‘insecurity’, ‘unpredictability’, ‘peril’, ‘chance’, ‘vulnerability’, ‘instability’, ‘jeopardy’, ‘speculation’,
‘probability’, ‘accident’, ‘daring’
Safe words: ‘safety’, ‘certainty’, ‘stability’, ‘gain’, ‘assurance’, ‘protection’, ‘security’, ‘safeguard’,
‘reliability’,‘predictability’, ‘refuge’, ‘guarantee’, ‘resilience’, ‘steadiness’, ‘shelter’, ‘caution’, ‘in-
evitability’, ‘prevention’, ‘prudence’
A.2
Prompts for Certainty Equivalent
Starting with $100 in capital, what is the maximum dollar amount you are willing to pay to participate
in this gamble: the gamble offers a {p1}% chance to win $100, a {p2}% chance to win $50, a {p3}%
chance to win $0. Respond with a single numeric value only. Do not explain your reasoning.
A.3
Prompts for MCMC with LLM
You are participating in a gambling game where you will be shown two options, Gamble A and
Gamble B:
Gamble A offers a {p1}% chance to win $100, a {p2}% chance to win $50, and a {p3}% chance to
win $0.
Gamble B offers a {p′
1}% chance to win $100, a {p′
2}% chance to win $50, and a {p′
3}% chance to
win $0.
12

--- Page 13 ---

Your task is to choose between the two. Do not explain your reasoning, just limit your answer to
either ‘A’ or ‘B’.
A.4
Prompts for Neural Activations
You are offered a gambling game: the gamble offers a {p1}% chance to win $100, a {p2}% chance to
win $50, a {p3}% chance to win $0. Respond with a single word only to express how much does this
gambling appeal to you. Do not explain your reasoning.
A.5
Prompts for Steering Risky Decision-Making
Given the following gambles: Option A offers a 5% chance to win $100 and 95% chance to win $0;
Option B offers a 100% chance to win $5. Please select either option A or option B to participate.
A.6
Prompts for Steering Risk Perception
Please rate how risky this behavior is with a single numeric value ranging from 1 (Not at all) to 7
(Extremely risky): {event}
B
Comparing Steering Vectors
In this section, we compare steering vectors derived from the MCMC and Certainty Equivalent
methods across different layers of the Gemma-2-9B-Instruct model (see Figure 6). The only difference
between the two approaches lies in the behavioral representation of risk used to compute alignment;
the underlying neural representation remains identical. We observe a clear trend: as we move from
earlier to later layers, the similarity between the two steering vectors increases, suggesting greater
convergence in their influence on model behavior at deeper levels of information processing.
0.004
0.002 0.000
0.002
0.015
0.010
0.005
0.000
0.005
0.010
Certainty Equivalent
Layer 1
0.01
0.00
0.01
0.0075
0.0050
0.0025
0.0000
0.0025
0.0050
Layer 10
0.02
0.00
0.03
0.02
0.01
0.00
0.01
Layer 25
0.01
0.00
0.01
0.010
0.005
0.000
0.005
Layer 41
MCMC
Figure 6: Comparison of steering vectors derived from MCMC with LLM (horizontal axis) and
Certainty Equivalent (vertical axis) across selected layers of Gemma-2-9B-Instruct. Pearson correla-
tion coefficients between the two steering vectors at layers 1, 10, 25, and 41 are −0.63 (p < .01),
0.04 (p = 0.02), 0.48 (p < .01), and 0.64 (p < .01), respectively.
C
Details of Representation Engineering
In this section, we describe the procedure for injecting a steering vector, hl
A, into the residual stream
of a Transformer at layer l. At inference time, we first obtain the model’s neural activation at layer l
for a given prompt p∗:
hl ←M.forward(p∗).activations[l]
where M denotes the LLM and hl represents the original activation at layer l. Next, we modify this
activation by injecting the steering vector scaled by a steering multiplier c:
hl
S ←hl + chl
A
where hl
S is the steered activation. The model then resumes its forward computation, beginning from
layer l with the modified activation:
S ←M.continue_forward(hl
S)
where S denotes the final output generated by the steered model.
13

--- Page 14 ---

D
Understanding the Marschak-Machina Triangle
As illustrated in Figure 2, behavioral representations of risk are defined over the Marschak–Machina
triangle [20, 18], a method used to characterize preferences over three-outcome gambles. To provide
additional context, we visualize the theoretical predictions of two influential models of human risky
choice within this triangle. Figure 7a depicts predictions from Expected Utility Theory (EUT),
a normative model of decision-making under risk [35], which assumes that individuals evaluate
gambles based on the weighted sum of utility. Under EUT, indifference curves are always straight and
parallel, reflecting consistent trade-offs between outcomes. In contrast, Cumulative Prospect Theory
(CPT), a descriptive model that accounts for empirical deviations from EUT, generates indifference
curves that exhibit a “fanning out” pattern (see Figure 7b). This curvature reflects increasing risk
aversion as the probability of extreme outcomes changes, leading to steeper indifference curves in
some regions of the triangle [18, 7].
a
Cumulative Prospect Theory
Expected Utility Theory
b
Figure 7: Predicted preferences under classical theories of human risky choice visualized in the
Marschak–Machina probability triangle. (a) Expected utility theory [35]. (b) Cumulative prospect
theory [33] using parameters α = 0.88, γ = 0.52. In both panels, each point within the triangle
represents a three-outcome gamble, and color intensity reflects the model’s predicted preference for
that gamble. Higher values correspond to stronger preferences.
Comparing the theoretical predictions within the probability triangle to the behavioral representation
elicited via MCMC (Figure 2b), we find that neither EUT nor CPT qualitatively captures the risk
preferences exhibited by the Gemma-2-9B-Instruct model. This suggests that existing models of
human risky choice may not be directly transferable to explaining LLM behavior [16, 43]. Future
research should consider developing new descriptive frameworks tailored to characterizing and
predicting the risky choices of LLMs.
E
Replication
We replicated the main experiment using a smaller LLM: Gemma-2-2B-Instruct [31].
Steering risky choices. For the four gambles presented in Table 1, Gemma-2-2B-Instruct exhibited a
ceiling effect, consistently preferring the risky option with 100% choice probability. As a result, all
three steering vectors showed negligible steerability in this condition.
Steering risk perception. Next, we examined the effects of steering vectors on the Gemma-2B
model’s ratings of real-world risky events (see Figure 8). The most steerable layer in the 2B model
occurred at a similar relative depth as in the 9B model.
We conducted two separate two-way repeated-measures ANOVAs to evaluate the effects of steering
method and multiplier on model ratings under positive and negative steering conditions.
14

--- Page 15 ---

a
b
Markov chain Monte Carlo
Contrastive Activation
Certainty Equivalent
Steerability
Layers
Layers
Layers
Higher ratings
Lower ratings
Unsteered baseline
Excessive ratings 
of risky events
Steering multipliers
Stronger 
positive steer
Stronger 
negative steer
Stronger 
negative steer
Stronger 
positive steer
Stronger 
positive steer
Stronger 
negative steer
Risk Perception
Figure 8: Steering risk perception of Gemma-2-2B-Instruct. (a) Steerability results using steering
vectors derived from Contrastive Activation (blue), Certainty Equivalent (green), and MCMC (red).
Darker colors represent larger steering multipliers. The optimal layers for steering, identified by the
highest steerability at the maximum multiplier, are layers 3, 15, and 15 for the respective methods
(marked with stars). (b) Change in average risk ratings for real-world events after steering, using the
optimal layer for each method. The vertical axis reflects the deviation from the unsteered baseline
rating. Each violin plot displays the distribution of ratings, with the white bar indicating the median
and the black box representing the interquartile range up to the 75th percentile.
For positive steering, the analysis revealed significant main effects of steering method, F(2, 298) =
1710.77, p < .01, and steering multiplier, F(4, 596) = 5092.48, p < .01, as well as a significant
interaction between the two factors, F(8, 1192) = 599.96, p < .01. Follow-up paired t-tests
showed that the MCMC method significantly outperformed both the Certainty Equivalent method
(t(149) = 55.63, p < .01) and the Contrastive Activation method (t(149) = 35.35, p < .01).
Additionally, the Contrastive Activation method outperformed the Certainty Equivalent method
(t(149) = 27.22, p < .01).
For negative steering, we again found significant main effects of steering method, F(2, 298) =
5786.59, p < .01, and multiplier, F(4, 596) = 2838.58, p < .01, along with a significant interaction,
F(8, 1192) = 2640.75, p < .01. Paired t-tests indicated that the MCMC method significantly
outperformed the Certainty Equivalent method (t(149) = 100.00, p < .01) and the Contrastive
Activation method (t(149) = 11.47, p < .01), while the Contrastive Activation method again
outperformed the Certainty Equivalent method (t(149) = 89.19, p < .01).
F
Implementation details
Steered model completions were executed on a single A100 GPU, requiring approximately 50 hours
for the 9B model and 40 hours for the 2B model. Computing steering vectors via self-alignment took
an additional 2 hours on a single A100 GPU.
15

```
