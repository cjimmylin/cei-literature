---
title: "Llama Guard 3 1B INT4 2411.17713"
source_pdf: "AI Labs/Meta AI/Papers/Llama_Guard_3_1B_INT4_2411.17713.pdf"
company: "Meta AI"
pages: 9
extracted_at: "2026-01-31T17:32:33.541349"
type: "ai_lab_paper"
---

# Llama Guard 3 1B INT4 2411.17713

**Company/Lab:** Meta AI
**Source PDF:** AI Labs/Meta AI/Papers/Llama_Guard_3_1B_INT4_2411.17713.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

Llama Guard 3-1B-INT4: Compact and Efficient
Safeguard for Human-AI Conversations
Igor Fedorov1,∗, Kate Plawiak1,∗, Lemeng Wu1,∗, Tarek Elgamal1,∗, Naveen Suda1,∗, Eric Smith∗,
Hongyuan Zhan∗, Jianfeng Chi∗, Yuriy Hulovatyy∗, Kimish Patel∗, Zechun Liu∗, Changsheng Zhao∗,
Yangyang Shi∗, Tijmen Blankenvoort∗, Mahesh Pasupuleti∗, Bilge Soran∗, Zacharie Delpierre Coudert∗,
Rachad Alao∗, Raghuraman Krishnamoorthi∗, Vikas Chandra∗
1Core contributors
∗Meta
This paper presents Llama Guard 3-1B-INT4, a compact and efficient Llama Guard model, which has
been open-sourced to the community during Meta Connect 2024. We demonstrate that Llama Guard
3-1B-INT4 can be deployed on resource-constrained devices, achieving a throughput of at least 30
tokens per second and a time-to-first-token of 2.5 seconds or less on a commodity Android mobile
CPU. Notably, our experiments show that Llama Guard 3-1B-INT4 attains comparable or superior
safety moderation scores to its larger counterpart, Llama Guard 3-1B, despite being approximately 7
times smaller in size (440MB).
Date: November 28, 2024
Correspondence: Kate Plawiak at kplawiak@meta.com
Code: https://github.com/meta-llama/llama-recipes/tree/main/recipes/responsible_ai/llama_guard
Blogpost: https://www.llama.com/trust-and-safety/#safeguard-model
1
Introduction
Safety is a major concern for products powered by Generative AI. It is essential to have robust safeguards in
place to protect against the generation of high-risk or policy-violating content (Inan et al., 2023). To address
this issue, large language models (LLMs) are often paired with a guard model that checks both user input
and model output for unsafe content. The guard model can be an LLM itself, but does not need to share the
same architecture or weights as the generative LLM it is paired with.
Another important consideration in deploying LLMs is the inference cost, especially when targeting resource
constrained hardware systems like a mobile device. For many such devices, the model’s memory usage becomes
the primary deployment bottleneck since mobile systems have limited DRAM and allocating large chunks of
memory can cause runtime issues due to operating system throttling.
Recently, much work has gone into compressing LLMs to make them significantly smaller. Nvidia’s Minitron
models (Muralidharan et al., 2024) and Google’s Gemma models (Team et al., 2024) extensively use pruning
and distillation to achieve smaller versions of their larger parent models. This paper further adds to the
discourse and evidence of the efficacy of these methods. On top of pruning and distillation, we also include
quantization in the compression process and show that several compression techniques can work well together.
As part of the Llama 3.2 1B release at Meta Connect 2024, we delivered Llama Guard 3-1B-INT4 (Llama Team,
2024), a lightweight Llama Guard model which:
• Consumes only ∼440MB, 7× less than Llama Guard 3-1B (Llama Team, 2024)
• Leverages 4-bit per-channel groupwise weight quantization and 8-bit per token dynamic activation
quantization for model compression
• Is compatible with the ExecuTorch runtime (Pytorch Team, 2024a) and XNNPACK backend delegation
(Pytorch Team, 2024b), which accelerate the quantization schema we used via specialized ARM CPU
kernels, achieving ≥30 token/s on a commodity Android mobile device CPU
1
arXiv:2411.17713v1  [cs.DC]  18 Nov 2024

--- Page 2 ---

Figure 1 Llama Guard output classification example.
• Achieves better F1 and false positive rate (FPR) than Llama Guard 3-1B for Enlish and 5 of 8 non-English
languages.
In this paper, we review the techniques we used to compress Llama Guard 3-1B-INT4 without sacrificing safety.
Some of the components used are well understood compression techniques from the literature (Muralidharan
et al., 2024; Krishnamoorthi, 2018; Liu et al., 2023) and our work represents further empirical validation
for such techniques in real-world LLM safety systems. Other techniques like unembedding layer pruning are
unique to the model and target task.
Our approach can be broken down into the following components:
• Decoder block and MLP dimension pruning. We reduce the number of decoder blocks and MLP width of
Llama Guard 3-1B-INT4 using a block-level and neuron-level sensitivity analysis, respectively
• Quantization. We use quantization aware training (QAT) to reduce the weight bitwidth to 4 and the
activation bitwidth to 8, such that the model size is cut down by 4× (relative to a 16 bit baseline) and
the model can be efficiently run via ExecuTorch’s XNNPACK backend.
• Output unembedding pruning. Llama 3 models have a large vocabulary size (128k), such that the
embedding and unembedding layers consume a substantial 35% of total model parameters. We make
use of the fact that Llama Guard models only require a limited output vocabulary and reduce the
unembedding layer output shape from 128k to 20.
• Distillation. We fine-tune the model with distillation (Hinton, 2015) from a Llama Guard 2-8B (Llama
Team, 2024b) teacher to recover any lost model quality resulting from the compression steps.
2
Llama Guard Models
Llama Guard consists of a series of high-performance moderation models designed to support developers
to detect various common types of violating content. The input to the Llama Guard model can consist of
only user input (prompt classification) or both user input and generative model output (prompt + response
2

--- Page 3 ---

Figure 2 Exporting and lowering quantized model for ExecuTorch runtime.
classification). Fig. 1 shows an example of Llama Guard output classification. Llama guard models are
trained as LLMs – they generate text indicating whether a given prompt or (prompt, response) pair is safe or
unsafe, and if unsafe, which content categories are violated.
2.1
Training and evaluation
Training for Llama Guard models consists of taking a pretrained LLM and conducting finetuning on content
safety classification data. The finetuning stage consists of minimizing the next-token prediction (cross-entropy)
loss over tokens corresponding to the target model outputs (shown in red in Fig. 1). Both Llama Guard 3-1B
and Llama Guard 3-1B-INT4 start from the Llama 3.2 1B pre-trained model (lla, 2024), but Llama Guard
3-1B-INT4 proceeds through a series of model compression steps before / during the finetuning stage (see Sec.
3).
We finetune Llama Guard 3-1B-INT4 using the English data used by Llama Guard (Inan et al., 2023), which
are obtained by labelling Llama 2 and Llama 3 generations on prompts from the hh-rlhf dataset (Bai et al.,
2022). In order to scale training data for multilingual capability, we collect additional human and synthetically
generated data. Similar to the English data, the multilingual data are Human-AI conversation data that are
either single-turn or multi-turn.
We evaluate the performance of Llama Guard 3-1B-INT4 on our internal test dataset based on MLCommons
(2024) hazard taxonomy and compare it across languages with Llama Guard 3-1B, Llama Guard 3-8B and
GPT4 (with zero-shot prompting).
2.2
Running the model on a mobile device
We employ ExecuTorch to demonstrate viability of running Llama Guard 3-1B-INT4 on widely available mobile
devices. ExecuTorch is a PyTorch native runtime framework for running PyTorch models on edge devices,
including smart phones. The ExecuTorch stack also enables leveraging neural network accelerators available on
modern mobile/edge devices, although we did not take advantage of this capability for running Llama Guard
3-1B-INT4. This enables efficient on-device execution of floating point and quantized models. Furthermore,
the lightweight nature of the runtime results in very small runtime memory footprint, significantly reducing
runtime overhead. ExecuTorch also provides LLM specific extensions and optimizations, including optimized
scaled dot product attention (SDPA) and KV-cache quantization.
Figure 2 shows the steps involved in exporting models to ExecuTorch, starting from QAT PyTorch model. As
shown, we leverage export_llama to apply LLM specific optimizations like SDPA, followed by torch.export to
capture the computation graph. The graph then gets further transformed to leverage the XNNPACK delegate
and we finally generate an artifact that the ExecuTorch runtime can run.
We leveraged a demo app for Android (Executorch Team, 2024a) (also available for iOS (Executorch Team,
3

--- Page 4 ---

2024b)), which leverages the ExecuTorch runtime to demonstrate Llama Guard 3-1B-INT4 capabilities for
response classification on an Android mobile CPU.
3
Model compression
We began with a pre-trained Llama 3.2 1B model (lla, 2024) and applied several techniques to achieve our
compression goals. Note that Llama 3.2 1B has about 1.2B parameters and uses embedding / unembedding
(i.e. output layer) weight sharing. ExecuTorch’s XNNPACK delegate does not support weight sharing with
embedding layer and as a result Llama 3.2 1B effectively has 1.5B parameters from an on-device deployment
point of view. Assuming bf16 weights for the original Llama 3.2 1B, which occupies ∼2.8GB, we achieved ∼7×
compression by applying our compression pipeline to yield a 440MB model. In the following, we describe the
techniques we used to achieve our compression goal. Fig. 3 provides a high level overview of the compression
pipeline, alongside the model sizes at each step.
Figure 3 Visualization of the compression pipeline.
3.1
Pruning
To reduce the number of model parameters, we prune the model along two dimensions: The number of
decoder blocks and the MLP hidden dimension. The methodology is similar to Muralidharan et al. (2024)
and proceeds in 3 stages: 1) pruning metric calibration; 2) model pruning; 3) fine-tuning the pruned model.
In the pruning metric calibration step, we calculate importance scores for the decoder blocks and neurons to
determine what to prune. For decoder block pruning, we employ the following importance metric from Men
et al. (2024):
ED

⟨xin, xout⟩
∥xin∥2 ∥xout∥2

(1)
where
• ⟨·, ·⟩is the inner product
• xin and xout refer to the decoder block (Llama Team, 2024a) input and output vectors, respectively, for
a particular input token position
• ED[·] is the expectation over the training data distribution D
The metric in (1) calculates the cosine similarity between the input and output of a decoder block. Blocks
which have low cosine similarity between input and output make a relatively small update to the residual
stream (Elhage et al., 2023) and can therefore be cut from the network.
For the MLP neurons, we estimate
ED
h
(hk)2i
∀1 ≤k ≤K
(2)
where hk denotes the k’th neuron feeding into the output linear layer inside the Llama 3.2 MLP and K is
the MLP hidden dimension. Both (1) and (2) are estimated using Monte-Carlo approximation over a few
thousand batches, where each batch contains 32 (GPUs) x 8 (per-GPU batch size) elements.
After calibrating the pruning metrics, we prune the model to 12 layers (from 16) and 6400 MLP hidden
dimension (from 8192), such that the pruned model has 1123 million parameters.
4

--- Page 5 ---

3.2
Quantization
Next, we quantized the model using quantization-aware training (QAT) (Krishnamoorthi, 2018; Nagel et al.,
2021; Liu et al., 2023), where the network is fine-tuned for accuracy with quantization operations in-the-
loop. QAT was implemented using the torchao (torchao maintainers and contributors, 2024) and torchtune
(torchtune maintainers and contributors, 2024) libraries. The weights of all the linear layers are quantized to
INT4, symmetrically with the range [-8, 7], and then de-quantized to enable backpropagation through the
quantization operation:
Q(θg) = sθ × clip

round
θg
sθ

, −8, 7

, sθ = 1
7.5 max|θg|
(3)
where θg refers to a group of weights for a particular output neuron and sθ is the corresponding scaling
factor. In order to backpropagate through (4), we use the straight-through estimator for the round(·) operator
(Bengio et al., 2013). Our quantization scheme uses a group-size of 256 values per-channel, meaning for a
linear layer with weight shape [Mout, Min], there are corresponding [Mout, Min//256] scaling factors. The
inputs to each linear layer are quantized to INT8, with asymmetric dynamic quantization with a scaling factor
for each token:
Q(xin) = sx × clip

round
xin −z
sx

, 0, 255

+ z, sx =
1
255 (max xin −min xin) , z = min xin
(4)
where xin is an activation vector corresponding to a particular token index. Dynamic quantization means
the tensor is quantized using the per-token min/max right before executing the matrix-multiply operation.
Apart from the inputs to each linear layer, and the linear weights, the rest of the network is executed in BF16.
Quantizing the linear layers to 4 bits per weight, we are able to reduce the model size from 2.1GB to 0.9GB
(Fig. 3).
The embedding layer in our pruned model contains a surprisingly large percentage of the total model weights:
23%. Therefore, quantizing the embedding layer weights to 4 bits represents a huge compression opportunity:
the model size goes from 0.9GB to 0.5GB. We observed that the model accuracy is largely unaffected by
simply rounding the embedding layer weights to their closest 4-bit values, so we did not apply QAT for the
embedding quantization. The embeddings were quantized with a group-size of 32.
3.3
Unembedding layer pruning
Llama Guard 3-1B-INT4 is trained to generate 128k output tokens, out of which only 20 tokens are used:
• Moderation tokens: ’safe’, ’unsafe’
• Unsafe categories: ’1’, ’2’, ’3’, ’4’, ’5’, ’6’, ’7’, ’8’, ’9’, ’10’, ’11’, ’12’, ’13’, ’14’
• Extras: ’\n’, ’S’, ’,’, ’<|eot_id|>’
By keeping only the model connections corresponding to those 20 tokens in the unembedding linear layer,
we can reduce the output layer size significantly without impacting the model. Using this unembedding
layer pruning, we reduced the output layer size from 262.6M parameters (2048 × 128k) to 40.96k parameters
(2048 × 20), giving us a total savings of 131.3MB, assuming 4-bit weight quantization, and a final model size
of 0.4GB. Although the pruned output layer only generates 20 tokens, they are expanded back to produce the
original 128k outputs in the model such that the model interface does not change from the developer’s point
of view.
3.4
Distillation
We employ Llama Guard 3-8B(Llama Team, 2024a) as a teacher to distill Llama Guard 3-1B-INT4 (Hinton,
2015):
min
θ
ED [Lcross-entropy (ys, yt)]
(5)
5

--- Page 6 ---

Table 1 Quantitative comparison between models
Model
F1/FPR
English
French
German
Italian
Spanish
Portugese
Hindi
Vietnamese
Indonesian
# param (B)
Model size (GB)
Llama Guard 3-8B
0.939/0.040
0.943/0.036
0.877/0.032
0.873/0.038
0.875/0.023
0.860/0.060
0.871/0.050
0.890/0.034
0.915/0.048
8
14.9
Llama Guard 3-1B
0.899/0.090
0.939/0.012
0.851/0.06
0.897/0.111
0.84/0.084
0.798/0.108
0.815/0.088
0.819/0.099
0.875/0.083
1.5
2.8
Llama Guard 3-1B -INT4
0.904/0.084
0.873/0.072
0.847/0.135
0.897/0.111
0.855/0.084
0.844/0.112
0.782/0.104
0.825/0.130
0.833/0.121
1.1
0.4
GPT4
0.805/0.152
0.795/0.157
0.691/0.123
0.753/0.20
0.711/0.169
0.738/0.207
0.709/0.206
0.741/0.148
0.787/0.169
?
?
where θ represents the Llama Guard 3-1B-INT4 weights, and ys and yt are the student (Llama Guard
3-1B-INT4) and teacher (Llama Guard 3-8B) logits, respectively, for a particular token index. We observe that
distillation significantly enhances the model’s ability to learn safe and unsafe patterns, as well as the posterior
distribution over unsafe categories. We observed a 1.3 percent (absolute) improvement in F1-score on internal
test data when using distillation to train Llama Guard 3-1B-INT4 compared to standard finetuning.
4
Results
As described in 2.1, we evaluate models using an internal dataset based on MLCommons (2024) hazard
taxonomy. Table 1 provides a quantitative comparison between our Llama Guard 3-1B-INT4, Llama Guard
3-1B, the much larger Llama Guard 3-8B, and GPT4. The metrics used in the table are F1 and FPR, which
stand for F1 score and False Positive Rate. F1 is a harmonic mean of precision and recall, which means
it balances the importance of both metrics and FPR measures the proportion of false positives among all
negative instances. For all models other than Llama Guard 3-1B-INT4, we assume the bf16 data format when
calculating the model size. Llama Guard 3-1B-INT4 achieves better F1/FPR scores for English relative to
Llama Guard 3-1B despite having 7× smaller model size. In addition, Llama Guard 3-1B-INT4 achieves on par
or higher F1 score than Llama Guard 3-1B on 5 out of 8 non-English languages. Compared to GPT4, Llama
Guard 3-1B-INT4 achieves considerably better F1/FPR for English as well as 7/8 non-English languages. Note
that GPT4 was tested in a zero-shot manner (using an internal dataset without any additional fine-tuning or
adaptation).
To validate that Llama Guard 3-1B-INT4 can be run on a commodity mobile device, we deployed the model
to a Moto-Razor phone and observed >= 30 token/s and <=2.5s time-to-first-token.
5
Limitations
There are some limitations associated with Llama Guard 3-1B-INT4. First, Llama Guard 3-1B-INT4 itself
is an LLM fine-tuned from Llama 3.2. Thus, its performance (e.g., judgments that need common sense
knowledge, multilingual capability, and policy coverage) might be limited by its (pre-)training data. Llama
Guard performance varies across model size and languages. When possible, developers should consider Llama
Guard 3-8B which may provide better safety classification performance but comes at a higher deployment
cost. Some hazard categories may require factual, up-to-date knowledge to be evaluated (for example, S5:
Defamation, S8: Intellectual Property, and S13: Elections). We believe more complex systems should be
deployed to accurately moderate these categories for use cases highly sensitive to these types of hazards, but
Llama Guard 3-1B-INT4 provides a good baseline for generic use cases. Lastly, as an LLM, Llama Guard
3-1B-INT4 may be susceptible to adversarial attacks or prompt injection attacks that could bypass or alter its
intended use. Please report vulnerabilities and we will look to incorporate improvements in future versions of
Llama Guard.
6
Summary
In conclusion, the pruned and quantized Llama Guard 3-1B-INT4 model is a significant improvement over its
predecessors in terms of both safety and efficiency. Additionally, the model’s small size and low latency make
it well-suited for deployment on mobile devices.
6

--- Page 7 ---

References
Llama 3.2: Revolutionizing edge ai and vision with open, customizable models, 2024. https://ai.meta.com/blog/
llama-3-2-connect-2024-vision-edge-mobile-devices/.
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort,
Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson Kernion, Tom Conerly, Sheer El-Showk,
Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez, Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt,
Neel Nanda, Catherine Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann,
and Jared Kaplan. Training a helpful and harmless assistant with reinforcement learning from human feedback,
2022. https://arxiv.org/abs/2204.05862.
Yoshua Bengio, Nicholas Léonard, and Aaron Courville. Estimating or propagating gradients through stochastic
neurons for conditional computation. arXiv preprint arXiv:1308.3432, 2013.
Nelson Elhage, Roberb Lasenby, and Christopher Olah. Privileged bases in the transformer residual stream, 2023.
https://transformer-circuits.pub/2023/privileged-basis/index.html.
Executorch Team.
Executorch llama android demo app.
https://github.com/pytorch/executorch/tree/main/
examples/demo-apps/android/LlamaDemo, 2024a.
Executorch Team. Executorch llama ios demo app. https://github.com/pytorch/executorch/tree/main/examples/
demo-apps/apple_ios/LLaMA, 2024b.
Geoffrey Hinton. Distilling the knowledge in a neural network. arXiv preprint arXiv:1503.02531, 2015.
Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi Rungta, Krithika Iyer, Yuning Mao, Michael Tontchev, Qing
Hu, Brian Fuller, Davide Testuggine, and Madian Khabsa. Llama guard: Llm-based input-output safeguard for
human-ai conversations, 2023. https://arxiv.org/abs/2312.06674.
Raghuraman Krishnamoorthi. Quantizing deep convolutional networks for efficient inference: A whitepaper. arXiv
preprint arXiv:1806.08342, 2018.
Zechun Liu, Barlas Oguz, Changsheng Zhao, Ernie Chang, Pierre Stock, Yashar Mehdad, Yangyang Shi, Raghuraman
Krishnamoorthi, and Vikas Chandra. Llm-qat: Data-free quantization aware training for large language models.
arXiv preprint arXiv:2305.17888, 2023.
Llama Team. The llama 3 herd of models, 2024a. https://arxiv.org/abs/2407.21783.
Llama Team.
Meta llama guard 2.
https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard2/
MODEL_CARD.md, 2024b.
AI @ Meta Llama Team. The llama 3 family of models. https://github.com/meta-llama/PurpleLlama/blob/main/
Llama-Guard3/1B/MODEL_CARD.md, 2024.
Xin Men, Mingyu Xu, Qingyu Zhang, Bingning Wang, Hongyu Lin, Yaojie Lu, Xianpei Han, and Weipeng Chen.
Shortgpt: Layers in large language models are more redundant than you expect, 2024. https://arxiv.org/abs/2403.
03853.
MLCommons.
Announcing mlcommons ai safety v0.5 proof of concept.
https://mlcommons.org/2024/04/
mlc-aisafety-v0-5-poc/, 2024.
Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad
Shoeybi, Bryan Catanzaro, Jan Kautz, and Pavlo Molchanov. Compact language models via pruning and knowledge
distillation, 2024. https://arxiv.org/abs/2407.14679.
Markus Nagel, Marios Fournarakis, Rana Ali Amjad, Yelysei Bondarenko, Mart Van Baalen, and Tijmen Blankevoort.
A white paper on neural network quantization. arXiv preprint arXiv:2106.08295, 2021.
Pytorch Team. Executorch runtime overview. https://pytorch.org/executorch/stable/runtime-overview.html, 2024a.
Pytorch
Team.
Executorch
xnnpack
delegate.
https://pytorch.org/executorch/stable/
native-delegates-executorch-xnnpack-delegate.html, 2024b.
Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya Pathak, Laurent Sifre,
Morgane Rivière, Mihir Sanjay Kale, Juliette Love, et al. Gemma: Open models based on gemini research and
technology. arXiv preprint arXiv:2403.08295, 2024.
7

--- Page 8 ---

torchao maintainers and contributors. torchao: Pytorch native quantization and sparsity for training and inference,
October 2024. https//github.com/pytorch/torchao.
torchtune maintainers and contributors. torchtune: Pytorch’s finetuning library, April 2024. https//github.com/
pytorch/torchtune.
8

--- Page 9 ---

Appendix
A
Acknowledgements
This work was made possible by a large group of contributors. We extend our gratitude to the following
people: Jacob Szwejbka, Jack Khuu, Chester Hu, Riandy Riandy, Chirag Modi, Beto de Paola, Jana Vranes,
Botao Chen, Kartikeya Upasani, Ujjwal Karn, Madian Khabsa, Varun Vontimitta, Vincent Gonguet, Joe
Spisak.
9

```
