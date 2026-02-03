---
title: "sora world model survey arxiv 2403.05131"
source_pdf: "AI Labs/OpenAI/Sora/sora-world-model-survey-arxiv-2403.05131.pdf"
company: "OpenAI"
pages: 35
extracted_at: "2026-01-31T17:32:37.616283"
type: "ai_lab_paper"
---

# sora world model survey arxiv 2403.05131

**Company/Lab:** OpenAI
**Model:** Sora
**Source PDF:** AI Labs/OpenAI/Sora/sora-world-model-survey-arxiv-2403.05131.pdf
**Total Pages:** 35

---

## Content

```
--- Page 1 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
FACHRINA DEWI PUSPITASARI, University of Electronic Science and Technology of China, China
CHAONING ZHANG∗, University of Electronic Science and Technology of China, China
JOSEPH CHO, Kyung Hee University, South Korea
ADNAN HAIDER, University of Electronic Science and Technology of China, China
NOOR UL EMAN, University of Electronic Science and Technology of China, China
OMER AMIN, University of Electronic Science and Technology of China, China
ALEXIS MANKOWSKI, University of Electronic Science and Technology of China, China
MUHAMMAD UMAIR, University of Electronic Science and Technology of China, China
JINGYAO ZHENG, The Hong Kong Polytechnic University, Hong Kong SAR
SHENG ZHENG, University of Electronic Science and Technology of China, China
LIK-HANG LEE, The Hong Kong Polytechnic University, Hong Kong SAR
CAIYAN QIN, Harbin Institute of Technology Shenzhen, China
TAE-HO KIM, Nota Inc., South Korea
CHOONG SEON HONG, Kyung Hee University, South Korea
YANG YANG, University of Electronic Science and Technology of China, China
HENG TAO SHEN, Tongji University, China
The evolution of video generation from text, from animating MNIST to simulating the world with Sora, has progressed at a breakneck
speed. Here, we systematically discuss how far text-to-video generation technology supports essential requirements in world modeling.
We curate 250+ studies on text-based video synthesis and world modeling. We then observe that recent models increasingly support
spatial, action, and strategic intelligences in world modeling through adherence to completeness, consistency, invention, as well as
human interaction and control. We conclude that text-to-video generation is adept at world modeling, although homework in several
aspects, such as the diversity-consistency trade-offs, remains to be addressed.
CCS Concepts: • Computing methodologies →Computer vision.
Additional Key Words and Phrases: Survey, Text-to-Video Generation, Text-to-Image Generation, Generative AI, World Model,
Scalability in AI, Artificial General Intelligence
∗Correspondence Author: Chaoning Zhang (chaoningzhang1990@gmail.com).
Authors’ addresses: Fachrina Dewi Puspitasari, University of Electronic Science and Technology of China, China, puspitasari-dewi@outlook.com;
Chaoning Zhang∗, University of Electronic Science and Technology of China, China, chaoningzhang1990@gmail.com; Joseph Cho, Kyung Hee University,
South Korea, joyousaf@khu.ac.kr; Adnan Haider, University of Electronic Science and Technology of China, China, adnanhaiderjaferi512@gmail.com;
Noor Ul Eman, University of Electronic Science and Technology of China, China, nooruleman3763@gmail.com; Omer Amin, University of Electronic
Science and Technology of China, China, oaminjr@gmail.com; Alexis Mankowski, University of Electronic Science and Technology of China, China,
alexis@mankowski.fr; Muhammad Umair, University of Electronic Science and Technology of China, China, umair.analyzes@gmail.com; Jingyao Zheng,
The Hong Kong Polytechnic University, Hong Kong SAR, jingyao.zheng@connect.polyu.hk; Sheng Zheng, University of Electronic Science and Technology
of China, China, zszhx2021@gmail.com; Lik-Hang Lee, The Hong Kong Polytechnic University, Hong Kong SAR, lik-hang.lee@polyu.edu.hk; Caiyan Qin,
Harbin Institute of Technology Shenzhen, China, qincaiyan@hit.edu.cn; Tae-Ho Kim, Nota Inc., South Korea, thkim@nota.ai; Choong Seon Hong, Kyung
Hee University, South Korea, cshong@khu.ac.kr; Yang Yang, University of Electronic Science and Technology of China, China, yang.yang@uestc.edu.cn;
Heng Tao Shen, Tongji University, China, shenhengtao@tongji.edu.cn.
1
arXiv:2403.05131v3  [cs.AI]  21 Jan 2026

--- Page 2 ---

2
Puspitasari et al.
1
INTRODUCTION
On February 15th, 2024, OpenAI introduced a new vision foundation model that can generate video from users’ text
prompts. The model named Sora, which people call a video version of ChatGPT, has raised excitement from industries
such as marketing [252], education [25], and filmmaking [245] for promoting democratization and offering a shortcut
to high-quality content creation. OpenAI claimed that Sora, due to being trained on a large-scale dataset of text-video
pairs, has impressive near-real-world generation capability. This includes creating vivid characters, simulating smooth
motion, depicting emotions, and provisioning detailed objects and backgrounds.
Survey Focus. Emerging from text-to-image generation models (denoted as “T2I”), text-to-video generation models
(denoted as “T2V”) expand the technological features of the image counterpart to handle the temporal dimension in video.
Specifically, the generative model learns the approximation of the true input video data distribution with text as the
condition. On the other hand, world model defines a generative artificial intelligence (AI) model that understands general
real-world mechanisms. Naturally, for a T2V to be considered as world model, it requires skills beyond synthesizing
video. These world modeling skills includes, but not limited to, physics understanding, user visual comfort, and the
logic of content composition. Given the above assertions, we are interested in exploring how text-to-video generation
models have come closer to being world models.
Method. Our survey utilizes PRISMA [191] framework. We primarily collect resources from well-recognized publication
venues, including, but not limited to, AAAI, ACL, CVPR, ECCV, ICCV, ICLR, IJCAI, NAACL, NeurIPS, ACM Multimedia,
IEEE Transactions on Multimedia, and arXiv in November 2025. Given that text-to-video synthesis is a fast-growing
study in the research community, we did not restrict the range of publication years. Using the search keywords “text-to-
video AND/OR (world model OR world simulator)”, we initially curated 400+ articles after briefly reviewing the fitness
of the publication title. We further devise several exclusion criteria, as follows:
• articles that discuss video synthesizing not conditioned on text prompt,
• articles that discuss text-video relationship other than the generation task (e.g, retrieval, editing, captioning),
• articles that discuss world modeling unrelated to the generative vision task, and
• survey and review articles.
and apply on the abstract and full article, we finally obtained a final list of 250+ papers.
Contribution. Following the recent surge in video generation, there have been a handful of surveys in T2V and/or
world model. Prior surveys discuss either T2V [128, 158, 228, 237, 277, 297] or world [44] model separately. Another
reviews both [360], but centers the discussion on world modeling. By contrast, we provide a comprehensive review of
T2V technology from world modeling perspective. Specifically, we first identify the critical components required for
world modeling, then explore how the advancement in T2V has achieved them. Our work also complements the existing
survey in the generative AI models for text-to-text [335], text-to-image [336], text-to-3D [131], and text-to-speech [337].
To summarise, our survey contributes the following to the research community:
• through preliminary discussion on world modeling, we identify the substantial components required for a
vision generative model to function as a world model,
• we provide technical discussion underpinning T2V from multiple aspects, including architecture, enabling
technology, and other complementary elements that support its role as a world model.
Structure. We start by reviewing the foundations of world modeling within the perception-action system and how
T2V contributes to it, from which we derive the essential aspects required by T2V to function as a world model (§ 2).

--- Page 3 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
3
We open the discussion on T2V by reviewing the historically important models as well as their core building blocks
(§ 3). With preliminary foundations on the world model and T2V, we then comprehensively discuss T2V from a world
modeling perspective, which includes the discussion on technical enablers (§ 4), control and human-in-the-loop (§ 5),
dataset and evaluation (§ 6), as well as applications (§ 7). Finally, based on these discussions, we summarize insights on
how T2V can be improved in the future to become the true world model (§ 8).
2
PRELIMINARY ON WORLD MODELS
2.1
Definitions of World Model
Imagine a waiter pouring a glass of orange juice:
through experience, he intuitively determines the pre-
cise level to stop, preventing the liquid from overflow-
ing. This judgment arises from his understanding of
factors such as the jug’s tilt angle, the juice level in
the glass, and the experience accumulated through
repeated practice. The waiter’s intuitive sense demon-
strates an internal understanding of how actions lead
to outcomes. Such predictive reasoning illustrates the
principle of a world model.
Fig. 1. World model inside the perception-action system. The world
model is part of the system brain that connects the internal repre-
sentation to the external world (adapted from [123]).
Mathematical Definition. World model conceptualizes the interaction between an agent and its environment [38].
“World” refers to the environment where the agent resides and “model” refers to the vision of the world carried by the
agent [77]. The agent constructs a world model with only a subset of world elements that are relevant to the task at
hand [123]. The idea of world model originates from the concept of mental model in psychology [59], in which internal
and external systems interact with each other. Mathematically, world model 𝑀can be defined as follows [38]:
𝑀= (𝑉,𝑆,𝑠0,𝐴, 𝐹𝐴, 𝐹𝑆)
(1)
where 𝑉, 𝑆, 𝑠0, 𝐴, 𝐹𝐴, and 𝐹𝑆refer to the environment variable, all possible outcome states, initial state, the action taken,
the valuation function of responses variable, and the valuation function of control variables, respectively.
World Model In Intelligent Systems. World model is a substantial component of the agents’ intelligence system,
which is optimized to improve the decision-making skills [238] through interaction with the environment [239]. The
system, referred to as perception-action system (Fig. 1), consists of six interconnected modules (i.e., perceptor, world
model, cost estimator, actor, short-term memory, and configurator) [123]. Perceptor estimates the current state of the
world based on input, and world model thinks about the possible future state. The discrepancies between these two
modules are examined by cost estimator, which then becomes an input for the actor to find an optimal action that
minimizes this cost in the future sequence. Information about the world state, predicted state, and their cost is stored in
the short-term memory that obeys temporal logic [8]. Finally, configurator regulates the information flow in the whole
system.
2.2
Roles of World Model in Perception-Action System
Perception-action system serves as the physical actualization of AGI. The world model is a part of AGI, acting as the
prefrontal cortex and hipopocampus which executes two core functions: prediction and planning, and memory storage.

--- Page 4 ---

4
Puspitasari et al.
In this section, we discuss three core roles of world model in the perception-action system: spatial intelligence, action
intelligence, and strategic intelligence (Fig. 2).
Spatial Intelligence. Spatial intelligence refers to the agent’s ability to see, process, and navigate through various
spatial layouts. For instance, a home robot adapting to a customer’s house layout, or a city ego vehicle that adapts
to rural roads. Given the abundance of spatial layout combinations, it is impossible to pre-define everything during
training. Thus, the role of world modeling is needed to circumvent this combinatorial knowledge problem. Spatial
intelligence is commonly performed as a scene prediction task, where given a single view of the spatial layout, the
world model can generate its prediction on the 360◦view [118]. Spatial intelligence entails four substantial aspects that
must be adhered to by the world model:
• Visual fidelity: ensuring high-quality visual construction [9].
• Temporal consistency: acceleration [350] of all moving objects that determine the occlusion hierarchy [314] and
visual condition [163].
• Structural stability: handling of corner cases and viewpoint responses to unrealistic agent behavior [184, 195].
• Commonsense plausibility: adherence to world law (e.g., traffic signals) [27].
The present-day world model in the perception-action system has considered these crucial aspects to ensure seamless
world modeling. For example, this is achieved by injecting spatial priors (e.g., point cloud and depth map, perspective
map) [176, 303]. Some world models even generate spatial priors (e.g., 3D occupancy map, LiDAR map) [258, 361] to be
utilized as the intermediate stage for the scene generation [163, 165].
Fig. 2. Cases of perception-action system where the world model performs spatial [184], action [144], and strategic [107] intelligences.
Action Intelligence. Action intelligence specifies how agent behaves in task execution. A naive example is an assistant
robot that can mimic human activity, performing behavioral cloning. Action intelligence undergoes an open-ended
objectives problem that may consist of not only what, but also how an activity is performed. Besides, it also suffers from
the scarcity (even more scarce than spatial intelligence) of data for training a generalist agent. World models, with
their strong generative capabilities, offer a promising direction for addressing these challenges [144]. To perform action
intelligence, the world model needs to comply with two fundamental requirements:
• Embodiment: reducing the perception–action gap between visual examples and real-world execution [136, 141].
• Physical plausibility: obeying physics law in real world [231, 313].
Some models depend on high-fidelity generated vision and state transition to learn these key elements [210]. Some
others rely on external data as generation conditions, such as sensorimotor signals (e.g., haptic forces, EMG, body pose,
and gaze tracking) [16, 136], and robot trajectories [287]. Other models decouple action and vision modals [359], rely

--- Page 5 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
5
on a digital twin to transfer the action knowledge into new environments [53], or attach an action adapter to a strong
world model [211] to get the benefit from large-scale action-free data and exclusively curated behavior data. World
model as action intelligence is also utilized as policy in reinforcement learning [142, 247]. It is also further enhanced by
an interim reflection mechanism that validates the generated content before it is translated into robot action [35].
Strategic Intelligence. Strategic intelligence refers to agents’ ability to perform long-horizon reasoning, opponent
modeling, and rule understanding. Strategic intelligence encompasses all elements in the world that the agent lives
in. This includes the environment and all the actors, including non-player characters. Game is an example of where
strategic intelligence is needed. A pleasurable gaming experience needs the integration of four key aspects: task leveling,
game mechanics, players, and randomness [107]. Deriving from this, there are two key requirements for a world model
to perform strategic intelligence:
• Diversity: generating diverse scenarios that fulfill the users’ divergent thinking [19].
• Interaction mechanics: ensuring and sustaining [84] coherence between users’ inputs and the generated con-
tent [307], as well as demonstrating causality from the interaction [115].
Interactive behaviors can be integrated into generated content by learning latent action representations from gameplay
data [19] or through imagination-based training [78]. Decoupling domain modeling from action learning further enables
the synthesis of novel game scenarios while maintaining realistic action control [318, 322]. User interaction is typically
expressed via general atomic control signals, such as keyboard bindings in game-generation settings [28, 318]. Diversity
can be introduced through reinforcement learning frameworks that cultivate agents with diverse skill sets, whose action
trajectories are subsequently used to train generative models [249]. Moreover, several approaches employ learned
dynamics engines to model state transitions explicitly, allowing the system to capture interaction causality [19, 78, 115].
Finally, memory mechanisms are often incorporated to support long-horizon reasoning and planning [115, 290, 307].
2.3
Why Text-to-Video Generation Matters for World Modeling
In perception–action systems, visualization is a core mechanism for interacting with the environment. Vision, in
particular, serves as an efficient medium for information transmission [110]. Given that effective simulation requires
both spatial and temporal understanding [188, 212], most existing systems rely on video for learning, sourced from
real-world recordings [58] or video games [76]. However, collecting video data that sufficiently covers the breadth of real-
world scenarios remains impractical. While video games can simulate diverse environments, they often rely on controlled
scenarios that hinder real-world generalization. Although internet videos are abundant, they are typically noisy and
lack critical properties for effective learning, such as skill development and realistic challenges [186]. T2Vs overcome
these limitations by generating diverse, task-specific environments that serve as agents’ training playground [84].
2.4
Critical Aspects of Text-to-Video for World Modeling
Generated video content from T2V serves as an imagined world, similar to the environments constructed in fiction and
video games. Such worlds are characterized by three core properties: invention, completeness, and consistency [282].
Completeness consists of comprehensiveness and cohesion [214] dimensions that correspond to content alignment and
richness, and scene compatibility, respectively. In perception-action systems, completeness is manifested as both visual
fidelity and interaction mechanics. Consistency measures whether generated content is plausible, non-contradictory, and
adheres to the rules of the world [126]. It includes entity, composition, and world consistency. Entity consistency concerns
the stable appearance of objects across space and time, composition consistency captures coherent spatial relationships

--- Page 6 ---

6
Puspitasari et al.
and interactions, and world consistency enforces physical and semantic plausibility. In the perception-action system,
consistency is translatable as temporal consistency, structural stability, and semantic and physical plausibility. Invention
is creativity constrained by internal consistency [282]. At the same time, invention enables extensibility, supporting
expansion and allowing new scenes, actions, and viewpoints to emerge without contradiction. In a perception–action
system, this extensible yet rule-consistent structure manifests as diversity in generation.
3
TEXT-TO-VIDEO AS WORLD MODELING
Since the emergence of Sora, T2Vs have increasingly been positioned as candidates for visual world modeling. Both
open-source and proprietary models are now competing to produce highly realistic videos while offering flexible and
fine-grained user control. In this section, we identify the current top-performing T2V models based on the public video
generation leaderboards and review their key design choices and enabling technologies. For closed-source models with
limited technical disclosure, we infer their underlying mechanisms from related research outputs and technical reports.
Fig. 3. Milestone of several historically substantial text-to-video generation models. Models in red are proprietary.
3.1
Historical Development of Text-to-Video Generation Models
Much of the technology utilized in the current top-performing T2Vs originates from early T2Vs. Here, we discuss
several historically important models (Fig. 3) that have become the inspiration for present-day world-model-like T2Vs.
Foundational Text-to-Video Generation Models. Video Diffusion Model (VDM) [92] is the first extension of T2I
to T2V. The model inherits the 3D U-Net architecture from T2I to generate videos with a fixed number of frames.
The key innovation of VDM is factorized space-time attention on 1D+2D latents over pseudo-3D convolution that
enables seamless image-video joint training. Stable Video Diffusion [17] (SVD) then improves the training paradigm
into three stages: T2I pretraining, video pretraining, and high-quality video finetuning. Further, to enable denser frame
generation during inference, VDM proposes reconstruction-guided sampling, where the intermediate output is checked
first to see whether it satisfies the input condition. Meanwhile, Imagen Video [89] presents techniques for high-fidelity
video generation over a fixed number of frames. The essential innovation of Imagen Video is a cascaded diffusion
framework, where the base T2V model is empowered by interleaved spatial and temporal video super-resolution.
This model also implements factorized space-time attention as well as progressive distillation for fast training. Finally,
Phenaki [250] pioneers arbitrary-length video generation. The key idea proposed by Phenaki is C-ViViT, which employs
causal attention for autoregressive-like generation. Further, Phenaki utilizes masked bidirectional transformer to
enable efficient sampling for long video generation.

--- Page 7 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
7
Foundational Transformer-based Models. VideoGPT [302] is the first T2V that explores a text-generation model
instead of a diffusion model for video generation. The key finding of VideoGPT is that the potential of transformer-
based architecture that enables world modeling. Meanwhile, MAGVIT [324] proposes 3D VQ-VAE to quantize
video into discrete tokens suitable for text-generation models. The essential innovation of MAGVIT is enabling multi-
task generation with masked token modeling that utilize interior condition as a learnable task router. Further,
MAGVIT-v2 [325] constructs a more powerful video tokenizer with a causal 3D CNN to support the implementation of a
text-generation model for generating video. The study shows that this technical improvement enables the transformer-
based language model to perform better than the U-Net-based diffusion model for video generation.
Early Proprietary Models. Runway Gen-2 [215] pioneers the widely accessible T2V as a video generation tool for
the public. Gen-2 also provides a wide range of controls and input modalities for users to perform various video-
related tasks. Impressively, despite being an early proprietary model, Gen-2 is capable of generating realistic video.
Runway Gen-3 [216] further improves Gen-2 performance in terms of visual fidelity and consistency. Equipped
with the more advanced controls, Gen-3 generates more highly realistic subjects compared to Gen-2. Moreover,
Dream Machine [167] establishes a benchmark for proprietary models in terms of physical realism and motion.
Top-Performing World-Modeling-Aware Models. Runway Gen-4.5 [217] is currently among the highest-ranked
T2Vs and has been adopted by numerous industry leaders. Beginning with Gen-1 in 2023, which was built upon a
latent diffusion backbone, Runway has evolved into its latest version, offering richer control mechanisms and enhanced
in-context generation capabilities. Veo 3 [68] is among the top-performing T2Vs that support native audio generation
alongside video synthesis. Similar to Runway, Veo 3 emphasizes audio-conditioned generation, long video extension,
and improved character consistency. Sora 2 [189] is introduced by OpenAI one year after the release of Sora. The
model is believed to retain Sora’s Diffusion Transformer (DiT) backbone while strengthening physical plausibility.
Minimax Hailuo [5] offers user video generation with complicated physical simulation due to its noise-aware compute
redistribution that allows for highly efficient computation. Seedance [62] optimizes text and vision representation
individually through separated branches to improve multimodal alignment. Lumiere [14] introduce space-time U-Net
where the temporal dimension is generated in a single-stream generation, followed by spatial super-resolution
to prioritize temporal continuity. The hype of T2V also promotes the deployment of other proprietary models, such
as PixVerse [7], Pika 1.5 [6], Dreamina [2], Hailuo [3], and Kling [4]. On the other hand, open-source models also
increasingly improve. HunyuanVideo [120] released by Tencent in 2025 demonstrates competitive performance with
closed-source counterparts in terms of temporal consistency, dynamics, and physical plausibility. CogVideoX [315],
developed by Tsinghua University, is an open-source T2V that achieves performance comparable to leading closed-source
systems. Mochi [244] proposes asymmetric DiT that performs text and vision processing in different streams
and joins them with multimodal self-attention, optimizing each modality and expediting inference speed. Vchitect [51]
also implement conceptually similar architecture to Mochi. Wan [253] offers fast computation and maintains temporal
continuity due to its feature caching of preceding frames. We present the performance of these models across all
evaluation dimensions in Table 2.
3.2
Core Building Blocks
Text Encoders. A text encoder encodes the raw text prompt into embedding representations that become input for the
vision model as a condition. Since its introduction in 2017, text encoders utilized by T2V models have followed the
evolution of text modeling. For instance, recurrent-based text models (e.g., RNN, LSTM, and GRU) are more common in

--- Page 8 ---

8
Puspitasari et al.
early-era T2V models, while transformer-based models (e.g. T5 [204] and BERT [42]) are more prevalent in modern
T2V models. Recent T2V models utilize CLIP [202] text encoder for its remarkable global contextual understanding.
Vision Model. A vision model converts input (e.g., image or noise) and condition (e.g., text embedding) into an output
video. T2V models mainly inherit the main architecture from T2I models. These vision backbones are generally grouped
in four architectures: VAE, GAN, autoregressive transformer, and latent DDPM (Fig. 4).
Fig. 4. Generative vision backbone in text-to-video generation models.
• VAE and GAN. VAE [117] is a probabilistic modeling based on variational inference of𝑞(𝑧| 𝑥) that approximates
the posterior 𝑝(𝑥| 𝑧) by maximizing the Evidence Lower Bound loss.
LVAE = −E𝑞𝜙(𝑧|𝑥) [log𝑝𝜃(𝑥| 𝑧)] + KL

𝑞𝜙(𝑧| 𝑥) ∥𝑝(𝑧)

.
(2)
Meanwhile, GAN [67] works according to the Minmax game principle between generator 𝐺and discriminator
𝐷, where the former generates samples, and the latter tries to distinguish between real and generated samples.
min
𝜃𝑔
max
𝜃𝑑
Ex∼𝑝data

log 𝐷𝜃𝑑(x)

+ Ez∼𝑝(z)
h
log

1 −𝐷𝜃𝑑(𝐺𝜃𝑔(z))
i
.
(3)
This training paradigm encourages GAN to produce diverse high-quality samples, making GAN-based T2V
models often utilized for story visualization (e.g., StoryGAN [135]). Further, VQ-VAE and VQ-GAN allow T2V
models (e.g., GODIVA [283]) to perform generation process in the discrete latent space to solve the prohibitive
computational cost from pixel-space generation.
• Autoregressive Transformer. Learning from how a discrete latent space has effectively facilitated text-vision
joint learning, some modern T2V models (e.g., VideoPoet [119]) synthesize video using a transformer. This idea
is pioneered by Phenaki through its C-ViViT architecture. MAGVIT-v2 later shows that this representation
discretization offers several benefits compared to the diffusion model, such as supporting multiple modes of
communication, speeding up (de)compression, and contextual understanding.
• Latent DDPM. Diffusion model, specifically Stable Diffusion [213], is the most popular vision model utilized by
contemporary T2Vs. Stable diffusion performs generation from input data x in continuous latent space encoded
by VAE. Diffusion model or DDPM [90] offers a better balance between diversity and fidelity compared to
GAN [43]. DDPM working mechanism entails two major processes, forward and backward. Forward process
converts input data z0 into noise z𝑇∼N(0, I) by gradually adding an infinitesimal amount of noise for a 𝑇
timesteps. Meanwhile, the backward process performs generation by iteratively denoising data z𝑡−1 from z𝑡
using a neural network 𝝐𝜃(z𝑡,𝑡) which is optimized through the following objective function:

--- Page 9 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
9
𝐿𝑠𝑖𝑚𝑝𝑙𝑒
𝑡
= E𝑡∼[1,𝑇],x0,𝝐𝑡
h
∥𝝐𝑡−𝝐𝜃(
√︁
𝛼𝑡x0 +
√︁
1 −𝛼𝑡𝝐𝑡,𝑡) ∥2i
Modern DDPM allows users to control the generation process by inserting prompts such as text, audio, and
localization marks. The classifier-free diffusion guidance handles all of these extra inputs. It is trained along
with the DDPM neural network during the reverse denoising process [91].
• Diffusion Transformer. Diffusion Transformers (DiT) [194] serve as the dominant backbone in contemporary
T2Vs. By combining the generative strengths of latent DDPM with the generalizability of transformers, DiT
provides a highly scalable architecture for video generation. This scalability enables the synthesis of longer,
higher-quality videos with improved alignment to user queries. The core architectural innovation of the DiT lies
in replacing the convolutional U-Net in latent DDPMs with a transformer-based backbone (Fig. 5). DiT operates
on a sequence of 𝑁patch tokens obtained by linearly projecting the VAE-encoded latent representation 𝑧0.
In addition to visual tokens, the transformer incorporates conditioning signals such as diffusion timesteps,
class labels, or text embeddings. These conditioning inputs modulate the network through adaptive layer
normalization, where scale-shift (𝛾and 𝛽) parameters are learned directly from the conditioning embeddings.
DiT further introduces residual scaling to stabilize training, with scaling parameters (𝛼) initialized to zero. After
a stack of transformer blocks and a final normalization layer, a linear projection produces the predicted noise
(and optionally covariance), which is used in the reverse denoising process to generate the output image.
Fig. 5. The architecture of Diffusion Transformer, which combines a transformer with latent DDPM (adapted from [194]).
Temporal Handler. Temporal handler complements the vision model by learning the inter-frame visual dynamics.
This function exists in a range of mechanisms: temporal attention, RNN, pseudo-3D convolution and attention, and
LLM (Fig. 6).
• RNN. Recurrent neural networks, such as LSTM [93] and GRU [36] are commonly integrated into GAN-based
vision models (e.g., StoryGAN). RNN takes text representation, noise, and its previous hidden state to produce a
new hidden state, which becomes the input to the generator. To ensure both temporal consistency and content
diversity, auxiliary modules like a hint generator connects inter-frame output [113, 125, 135].
• Temporal Attention. Adding a temporal attention that operates on time dimension is the most straightforward
way of incorporating temporality into T2I models. Temporal layers are commonly found in autoregressive and
VQ-VAE vision models. Several implementations of temporal layers are found in Phenaki with causal attention,

--- Page 10 ---

10
Puspitasari et al.
CogVideo [95] with temporal attention, GODIVA [283] with 3D-sparse attention, and VideoPoet [119] that
utilizes causal attention on regressive language model.
• Pseudo-3D Convolutions. Pseudo network inflation is a familiar technique for incorporating temporal dimen-
sionality into the diffusion model, such as Make-A-Video [227] and the majority of latent DDPM-based T2Vs.
Here, a 1D convolution (temporal) layer is attached after every 2D convolution (spatial) layer. Through the
pseudo-3D convolution layer, the input video of shape 𝑏𝑎𝑡𝑐ℎ× 𝑓𝑟𝑎𝑚𝑒𝑠×𝑐ℎ𝑎𝑛𝑛𝑒𝑙𝑠×ℎ𝑒𝑖𝑔ℎ𝑡×𝑤𝑖𝑑𝑡ℎis processed
by the spatial layer as (𝑏× 𝑓) × 𝑐× ℎ× 𝑤and the temporal layer as 𝑏× 𝑐× 𝑓× ℎ× 𝑤. This separable convolu-
tion [37] technique offers multiple benefits: circumventing expensive computation, preserving the 2D backbone
knowledge while updating the temporal parameter, and sharing knowledge with all of the input elements. In
addition to pseudo-3D convolution, inflating T2I to T2V can also be enriched with noise prior correlation [64].
• Pseudo-3D Attention in DiT. Conceptually similar to pseudo-3D convolutions, pseudo-3D attention layer also
offers cheap temporal integration. Pioneered by VDM, this layer leverages sinusoidal positional embedding to
supply frame indices information. Some examples of practical implementations include Gentron [33] and Open-
sora [356] that utilize lightweight temporal self-attention, Latte [175] and MotionZero [234], which interleave
spatial and temporal attention, and Runway that attaches a temporal extension module in a residual connection
and attention block. To ensure that the latent representations preserve the temporal continuity, CogVideoX
leverages 3D-VAE [356], while another improves it with leading padding to encode temporal causality [325].
Further, to handle temporal inconsistency in fast motion, CogVideoX utilizes 3D full attention [315], while
another supplies motion conditioning [33]. Finally, it is worth noting that these models achieve proper temporal
modeling by treating T2V as the generation of “image as 𝑇frames video” instead of “video as a sequence of 𝑇
images” [177].
Fig. 6. Temporal handler used to align frames in text-to-video generation models.
3.3
Towards World Modeling Backbone
Scalable and Generalizable Learning. Training on an immense number of high-resolution images and videos, while
improving generalizability, is highly prohibitive. To circumvent this issue, MDTv2 [61] and DiffPhy [354] subsequent
works propose masked training, where it learns to predict the score of unmasked patches and reconstruct the masked
patches simultaneously. PIXART-𝛼[31] decouples pixel learning and text-image learning from the standard unified

--- Page 11 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
11
training, making intra- and inter-modal learning less complex and thus more efficient. AnimateLCM [255] decouples
image prior and motion prior to expedite learning. Runway decomposes video generation into content (e.g, appearance)
and structure (e.g., geometry and dynamics) [48]. Structural knowledge can be derived using structural encoders, while
content is derived from CLIP image embedding that is sensitive to semantic properties [138]. Finally, pioneered by VDM,
nearly all current T2Vs (e.g., Gentron [33] and Latte [175]) employ joint image-video training to get the advantage of
high visual quality and high temporal consistency.
Efficient Sampling. The iterative sampling process during the denoising step is one of the bottlenecks of DiT.
Consistency model [229, 230] offers a remedy to this limitation. Specifically, consistency models enable sampling
high-quality data in a single step or n-steps where n is much smaller than the original iteration steps. To date, the
effort to compress the sampling step has developed into various approaches. Some approaches perform modification by
replacing denoising with rectified flow that directly learns the velocity field to transport noise to data [49], replacing
DiT with an interpolant transformer that takes advantages from denoising, rectified flow, and others [173]. Some of
which are utilizing the probability density function of the signal-to-noise ratio to schedule sampling [316] and weighted
caching of representation at each step with error optimization [201]. Other approaches explore the asymmetric sampling,
such as sampling prioritizing areas that have not yet converged [257], adjusting the model shape at each timestep [352],
and treating the sampling step as a mixture-of-depth [226].
4
WORLD-MODELING-ENABLERS IN TEXT-TO-VIDEO GENERATION
T2V as a world model needs to adhere to the specification on world model for perception-action system (Fig. 7). Accord-
ingly, this section reviews the key techniques adopted in recent T2V models to address these additional requirements.
Fig. 7. The relationship between essential components for world model of the perception-action system and substantial components
of text-to-video generation as world model.
4.1
Visual Fidelity
Visual fidelity is a foundational requirement for any vision generation task. As T2V generation builds upon T2I models,
it naturally inherits many image-generation challenges, such as preserving fine-grained textures and handling non-zero
signal-to-noise ratios.

--- Page 12 ---

12
Puspitasari et al.
Texture Modeling. Texture plays a crucial role in perceived image quality, as it conveys fine-grained visual details.
However, texture information is often suppressed when images are compressed into latent representations. Cascaded
generation, as pioneered by Imagen Video, offers an effective solution to this limitation. Specifically, models like
VideoLDM [18], Waver [347], and Show-1 [338] first generate low-resolution frames in pixel space to preserve fine
details, and subsequently enhance them via latent-space super-resolution. In addition, texture information can be
explicitly introduced as a conditioning signal during generation through semantic-texture consistency training [327]. To
alleviate the difficulty of reconstructing good representations, regularization based on distillation of external high-quality
representations can guide model learning [326].
Noise Conditioning. Diffusion models often suffer from reduced visual fidelity due to a mismatch between training
and inference noise schedules. Residual signals at the terminal training timestep hinder generalization to pure Gaussian
noise during sampling. This issue can be mitigated by aligning the two processes, for example, Emu Video [66] scales the
noise schedule to zero at the final timestep. On the other hand, to alleviate train-test discrepancies in noise scheduling,
ART·V [281] performs noise augmentation.
Factorized Learning. Jointly optimizing spatial and temporal dimensions remains a core challenge in T2V generation.
Disentanglement provides an effective remedy by simplifying the learning problem. For example, it can be realized
through spatiotemporal decomposition in prompt level [270], latent space level [106], and architectural level [151].
HiGen [199] implements hierarchical spatiotemporal learning. Similarly, MotionBooth [286] additionally incorporates
subject region loss and video preservation loss. In hierarchical learning approaches, models are typically trained in
a sequential order, such as T2I →T2V or T2V →T2I. However, differences in noise sampling mechanisms between
image and video diffusion often introduce visual inconsistencies. To address this issue, recent works pursue pseudo-
simultaneous learning of spatial and temporal representations. To reduce flickers and generate high visual quality,
DSDN [149] employs dual-stream diffusion and EVS [235] encapsulates T2I with T2V in a T2I−→T2V−→T2I manner. On the
other hand, DCM [170] performs dual-expert consistency modeling and cross-dimensional losses, and MotionShot [157]
learns semantic and morphological motion hierarchically.
4.2
Diversity
A video must exhibit not only temporal consistency but also sufficient visual diversity and progression to convey a story.
However, generating diverse, temporally evolving content from a single text prompt is challenging, as models often fail
to capture fine-grained temporal cues embedded in language. As a result, T2V systems tend to focus on the main clause
while overlooking temporal subclauses. For instance, given the prompt the dog catches the ball and returns it to the man,
the model may generate only the dog catches the ball. This behavior is partly attributable to training objectives that
favor short, temporally consistent clips. To address this limitation, initiated by LVD [140] and other early models like
FlowZero [166], FreeBloom [97], and VideoDrafter [161], T2Vs leverage LLMs to decompose prompts into structured
scene plans. These plans guide story construction by drafting keyframes or event sequences. For instance, EIDT-V [101]
utilizes LLMs to generate frame-wise prompts and to identify the scene switch. Moreover, VideoStudio [162] and
DirectT2V [94] ask LLM to convert prompts into multi-scene scripts. Subsequent event-wise segments can be merged
into a coherent video using techniques such as, noise blending [86] or frame interpolation [11, 148].

--- Page 13 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
13
4.3
Interactivity: Prompt-Generation Alignment
In the perception–action systems, interactivity characterizes how tightly a world model is coupled with the real world.
In T2V systems, text serves as the primary interface enabling this interactivity. However, textual expressiveness and
visual richness arise from different modalities, meaning that improvements in text modeling do not necessarily translate
into better visual generation. As a result, specialized strategies are required to enhance interactivity in T2V models.
Prompt Optimization. Detailed descriptions, rather than merely expressive prompts, are more effective at aligning
generation with visual richness. However, crafting such detailed prompts is often tedious. Leveraging their strong
language understanding, LLMs provide an efficient solution through prompt rewriting. For example, POS [174] proposes
a semantic-preserving rewriter to prevent semantic drift from naïve LLM rewriting. Runway employs coarse-to-
fine progressive refinement instead of passing a long and detailed prompt at once [218]. VideoTetris [246] performs
spatiotemporal hierarchical refinement. MOVAI [193] introduces a compositional scene parser to generate scene graphs
with temporal annotations. InstanceCap [50] performs temporal- and attribute-level decomposition with improved
chain-of-thought prompting [278]. MOVi [205] disentangles the prompt based on the subject. The rewritten results can
further be translated into auxiliary conditioning signals that improve visual control, such as trajectories or layouts [166],
reference images or videos [148], sketches [150], depth maps [295], keypoint poses [21, 348, 351], and 3D skeletons [116].
Given that grounding is a critical component of vision–text alignment, auxiliary non-textual conditions enhance
text–vision grounding by refining cross-modal understanding [98]. Further, VLMs are commonly employed to reason
over the prompt and select appropriate conditioning signals [114, 138].
Visuo-Textual Cross-Attention. To integrate text condition to DiT, a common approach is performed by replacing class
condition embedding with language model embedding [33], and incorporating a visual-text cross-attention layer [31].
CogVideoX improves this technique by integrating modality experts that modulate parameters in the adaptive layer
norm based on the modality being passed [315], allowing modalities to be optimized individually yet learned in a union.
Meanwhile, HunyuanVideo proposes a two-stage alignment [120] where each modality is processed individually before
being processed as one sequence. Similarly, two separate weights can be assigned for the two modalities [49].
4.4
Temporal Consistency: Entity
Entity consistency describes the ability of a model to maintain a stable identity for subjects across frames. Entity
consistency is substantial for preventing visual drift and identity fragmentation over time.
Reference Representation. Identity preservation in T2V refers to maintaining consistent visual characteristics of
subjects (e.g., facial features, clothing, and expressions) across frames and viewpoints. Intuitively, these attributes should
remain as close as possible to the initial appearance. As a result, many methods incorporate reference features during
training to anchor subject identity [94, 138, 150, 246]. ConsistI2V [208] and other models [111, 291] commonly derive
these references from the first frame. Meanwhile, MEVG [187] and other models [41, 85, 187] adopt inversion, where
the noise initialization is taken from previously generated frames rather than sampled from a Gaussian distribution,
thereby reinforcing subject continuity. Alternatively, some approaches jointly condition the generation process on both
the first frame and the last frame to further enhance identity consistency [319].
Single-Subject Learning. Generating a single entity that engages in diverse activities or appears across varying
backgrounds remains a significant challenge. Single-stream generation, which produces all scenes within a single
pass, often lacks visual diversity. In contrast, multi-stream generation synthesizes scenes independently but typically

--- Page 14 ---

14
Puspitasari et al.
struggles to preserve entity consistency. To strike a balance between diversity and consistency, diffusion-based attention
mechanisms have introduced several strategies. ShotAdapter [109] and EIDT-V perform transition-aware attention
masking that regulates shot-specific prompting. MoCA [292] leverages cross-attention on mixtures of hierarchical
temporal representation [60]. ConsisID [329] decomposes subject representation for high and low-frequency learning.
Multi-Subject Learning. To ensure consistent generation of multiple subjects within a single video, subject-specific
representations must be disentangled to avoid interference with other subjects or the background. Current T2Vs
achieve this form of “isolation” through mechanisms like subject-wise attention masking [246, 273]. Additionally,
DisenStudio [29] decomposes text features at the subject level, and TIV-Diffusion [264] integrates subject-specific slot
attention modules.
4.5
Structural Stability: Composition
Composition encompasses all visual elements in a scene, including foreground subjects and the background. With this
perspective, composition consistency is closely related to view consistency. The generated world is expected to preserve
coherent and stable visual structures across different viewpoints and directions. This is analogous to a 360◦panoramic
video, where traversing the scene ultimately leads back to a viewpoint that seamlessly aligns with the original position.
3D Geometric Prior. The 3D geometric representations, such as point clouds, encode rich structural knowledge
about the physical world. From 3D geometry, one can infer static structure, motion dynamics [272], and lighting
directions [355]. Recent studies in T2V have developed several interesting techniques in leveraging 3D prior for
structural stability. GenDef [262] warps a static reference image in a generative deformation field. CineMaster [260]
facilitates users in providing bounding boxes for scene assembly, while GEN3C [209] builds a 3D cache to memorize the
structure of previously generated frames. In addition, Geometry Forcing [285] enforces angular and scale alignment as
auxiliary constraints to align the generated 2D projections with the underlying 3D structure.
2D Structural Layout. Despite its expressiveness, acquiring 3D geometric structure is costly, whether through manual
annotation or learned reconstruction models. To enforce spatial consistency with a more lightweight alternative,
recent approaches introduce dynamic 2D layouts across the generated frame sequence. Common approaches includes
incorporating motion trajectories [159] and spatial displacements [317]. BlobGEN [57] utilizes visual primitive blobs to
ground composition. Dysen-VDM [54] relies on LLM to generate a scene graph. MotionBooth introduces a latent shift
module to control camera movement. Beyond manual specification, models like CAMEO [185] and Direct-A-Video [308]
employ a learnable camera module to learn structural cues. TrajVLM-Gen [304] employs VLM to predict the trajectory of
the next frame. The frequency domain also offers valuable signals for structural consistency. In particular, low-frequency
components preserve semantic content and spatiotemporal correlations, thereby maintaining global consistency,
while high-frequency components capture motion dynamics. Accordingly, ConsistI2V [208] utilizes low-frequency
information from a reference image as layout guidance. ScenarioDiff [346] utilizes a mixed-frequency ControlNet where
high-frequency components are used to initialize noise. ByTheWay [20] proposes Fourier-based motion enhancement
that modulates the high-frequency components of the temporal attention map. Finally, the learning strategy also plays
an important role in structural consistency. For example, incorporating localized visual–text cross-attention [339] or
leveraging shape rigidity losses [206] has been shown to further stabilize compositional structure.

--- Page 15 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
15
4.6
World Consistency: Physical and Commonsense Conformities
World consistency is a fundamental requirement for any model that aims to replicate the real world. It refers to the
adherence to the laws of the world, which typically encompass both commonsense constraints and physical principles.
Learning Physical Law. Physical laws are among the most salient indicators of world adherence. A ball bouncing
upon hitting the ground and water flowing faster than milk illustrate fundamental physical regularities. As a visual
generative model, T2V naturally prioritizes visual fidelity and temporal coherence, often neglecting the incorporation
of physical knowledge. As a result, external mechanisms are required to trigger T2V models to respect the physical
laws of the real world. In general, models acquire physical knowledge through three stages: perception of physical
properties, simulation of dynamics, and visual rendering [153]. Contemporary approaches involve motion cues, such as
3D point trajectories [34] or optical flow [181]. MagicTime [330] utilizes time-lapse video for learning metamorphic
generation. VideoREPA [344] distills physics knowledge from pre-trained large video encoders and learning token
relation. NewtonGen [332] relies on physics-informed neural ordinary differential equation to learn Newtonian motions.
Physics learning can also be performed post-training. For instance, PISA [130] performs fine-tuning by watching
stuff drop, and PhysMaster [104] leverages reinforcement learning to optimize physics encoder. Beyond vision-only
approaches, VLMs and LLMs can further assist T2Vs in learning physical plausibility. VLIPP [310] leverages physics-
aware chain-of-thought [278] reasoning for predicting rough motion. DiffPhy [342] utilizes LLM to derive physical
context from the prompt. Similarly, WISA [256] derives the prompt to enrich qualitative physical categories and
quantitative physical properties. GPT4Motion [169] relies on LLM assistance to generate a script for physical simulators
(e.g., Blender). SGD [82] performs counterfactual prompting to suppress physical implausibility. Moreover, architectural
and training strategies, including mixtures of physical experts [256] and reinforcement learning [259], have been shown
to further strengthen the embedding of physical knowledge into T2Vs.
Commonsense Conformity. Beyond physical dynamics, T2V models must also incorporate world commonsense to
achieve truly world-like generation. These include material properties, causal relationships, and factual adherence [24].
Accurate encoding of material properties is essential for maintaining physical plausibility. For example, a ball landing
on a bed should deform and settle rather than bounce as it would on a rigid floor. Such material-dependent behavior can
be modeled by integrating physics-based simulations with material-aware point cloud representations. PhysCtrl [254]
proposes a spatiotemporal attention block that emulates particle interactions in point cloud. PhysChoreo [340] estimates
the static physical properties of all objects in the image through part-aware physical property reconstruction. In contrast,
causal reasoning can be introduced in several ways. For instance, PhysAnimator [293] introduces customizable energy
strokes and the incorporation of rigging point support, combined with deformable simulation. PhyT2V [301] performs
chain-of-thought and step-back reasoning to learn causality.
5
MULTIMODAL CONTROL AND HUMAN-IN-THE-LOOP OF T2V
5.1
Leveraging Multimodal Control Through Any-to-Any Generation
A world model, by definition, must accommodate a wide range of input signals. In practical scenarios such as gaming,
these signals include multi-user controls, such as keyboard commands, haptic inputs, text instructions, and voice signals.
Moreover, the model is expected to support diverse tasks, including video generation, audio synthesis, and haptic
feedback. Such requirements extend the conventional scope of T2V, which is limited to bimodal input and single-task
output, toward a more general any-to-any generation paradigm.

--- Page 16 ---

16
Puspitasari et al.
General Framework. Exploration of any-to-any generation begins in 2023 with CoDi [243] as one of the pioneering
studies. It emphasizes that the generation capability of the diffusion model is not limited to vision, but to other modalities.
The key enabler is isolated training, where a specific diffusion model is trained for a specific modality. The input
representations from all modalities are projected into the same space before being interpolated for training. To alleviate
the costly all-modal optimization, CoDi utilizes text-any bridging. After isolated training, CoDi performs joint generation
with the assistance of a cross-modal attention layer. Following CoDi, there have been numerous developments for
diffusion-based any-to-any generation. For instance, to alleviate the costly training from scratch, modality-specific
diffusion models are replaced with a unified modular multimodal diffusion with a joint attention layer [133], diffusion
latent aligner [296], or inter-models inter-layer consistency transfer [200].
Multimodal Alignment. The alignment complexity in any-to-any generation increases with the number of modalities
involved. Naïve multimodal binding often results in poor generation results. To tackle this issue, numerous studies
have proposed several remedies, such as ensembling modality-specific models and modulating their contribution with
learnable routers [276], constructing a multimodal Control-Net to generate compound conditions [341], and binding
unified multimodal spaces to an expert single modal space [275]. To address modalities with limited data (e.g., haptics),
OmniBind leverages distillation from data-rich modality to data-scarce ones, enhancing cross-modal alignment [172].
In-Context Understanding From Multimodalities. Real-world deployment of a world model demands contextual
understanding arising from the integration of multiple modalities. For example, text prompts and audio cues in gameplay
may carry implicit instructions that require deep contextual comprehension. Achieving this level of expertise goes
beyond simple multimodal alignment, motivating the use of LLMs to enhance reasoning and understanding across
modalities. NExT-GPT [288], CoDi-2 [242], and Vitron [55] are among the first any-to-any generative models that
leverage LLMs. It projects all modalities into language-like representations and passes them to an LLM that performs
semantic understanding and reasoning. On the output side, multiple strategies exist to enhance the mapping from LLM
outputs to generative models. For instance, UnifiedMLLM [139] and Spider [122] utilize learnable task tokens and a
router, A-Language [32] leverages symbolic representation, and ModaVerse [267] proposes an I/O alignment strategy
where LLM generates meta-responses to instruct the specific generative model. Finally, a step further from employing
LLMs as the alignment engine is to solely utilize autoregressive transformers for multimodal generation [65, 266].
5.2
Human In the Generation Loop
Humans are central to any artificial intelligence system, including T2V. In a perception-action system, the world
model must align closely with the user’s actual experiences and perceptions. This requires human involvement in the
generation loop, either by providing feedback on outputs or by interacting with the system during the process.
Human Feedback. Reinforcement learning with human feedback (RLHF) is a de facto method for incorporating human
feedback into AI models. Aligning AI generation to human preference not only helps in generating hyper-realistic
output but also entails other benefits, such as correcting model reasoning and safeguarding against malicious input
triggers. The customary practice in RLHF is to collect manual human annotation on a small subset of data, which is
then used in direct preference optimization (DPO) [203] or to train a reward model in proximal policy optimization
(PPO) [223]. In T2V, DPO-based RLHF [152, 298, 358] is more commonly employed than PPO-based RLHF [1]. Due to
the prohibitive cost of iterative reward optimization, several studies modify DPO through reusing a pre-trained diffusion
model as a value estimator [306] and recasting the reward optimization as editing task [328]. Besides the common DPO
and PPO, T2Vs also utilize iterative preference optimization (IPO) [251, 271, 311]. IPO is an extension of DPO, which

--- Page 17 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
17
leverages a critic model trained with manually annotated human feedback to optimize the generative model iteratively.
It is worth noting that fine-tuning on feedback data also empowers the alignment in terms of physics consistency [197].
Human-AI Co-Creation. Co-creation with a generative model entails active user participation throughout the
generation process. Rather than limiting user input to the initial text prompt or conditions, co-creation frames T2V
as an iterative mechanism that continuously relies on user involvement. Several works that explore this direction
are InteractiveVideo [345] that alter the predicted noise with new conditions, IGV [321] that leverages four modules
supporting the world modeling through user interaction (i.e., control, memory, dynamics, and intelligence), and
Imagine360 [279] that incorporates users’ speech-based text prompts.
6
DATASETS AND EVALUATION
6.1
Datasets
Datasets evolve following the evolution of T2Vs. For instance, in the early T2V era, simple datasets such as MovingM-
NIST [233] and PororoSV [135] were frequently used for training. As the T2V evolved from multi-image generation to
video generation and to world modeling, the datasets became more complex.
General T2V Datasets. We observe that there are five most commonly utilized datasets for training T2V: WebVid-10M,
HD-VILA-100M, SSV2, MSR-VTT, and LAION-5B. Webvid-10M is the expansion of WebVid-2M [13], which consists of
2.5M pairs of short caption-video from Shutterstock. The open-domain nature of Webvid-10M encourages learning
of diverse visual representations. However, WebVid-10M contains watermarks [266], which challenge the generation
of videos with high visual fidelity. Thus, researchers often supplement WebVid-10M with additional high-quality,
watermark-free video data [75]. HD-VILA-100M [300] consists of 100M pairs of high-resolution videos and long text
captions with diverse categories. Such a characteristic makes HD-VILA-100M suitable for training high-performing
T2Vs. SSV2 [69] is a collection of 100k human-object interaction short videos accompanied by natural language template
captions as class labels. The SSV2 represents physical properties of objects and the world through action. Given the
scarcity of high-quality video-text pair data, supplementing the training dataset with an image-text pair dataset like
LAION-5B has become a common practice. The LAION-5B [221] dataset contains a massive collection of image-text pairs.
LAION-5B is the extension of LAION-400M [222], which curates the data with common crawl and is accompanied by
CLIP [202] filtering. About 50% of LAION-5B data pairs have English captions. While containing only image-text pairs,
training T2V on LAION provides large-scale semantic grounding and compositional priors of visual representations.
Complementary World Modeling Datasets. General T2V models often face challenges when applied to native world-
modeling tasks, such as navigation, autonomous driving, robotics, and gaming. A key limitation is the scarcity of relevant
samples in standard training datasets. To overcome this, researchers typically augment training with domain-specific
data. Several notable representations of these complementary datasets are Room-2-Room, Sekai, nuScene, OpenDV-2K,
Ego-Exo4D, OXE, DROID, Atari Grand Challenge, and Platformers. Room-2-Room [10] is a visual-language navigation
dataset consisting of 90 indoor scenes with 21k navigation instructions. Given that scenes are derived from panoramic
RGB-D data, Room-2-Room is capable of assisting the world model in learning structural consistency. Sekai [137] is an
outdoor navigation (e.g., walking and drone-based) dataset with a total of 5k hours of videos with the corresponding
text descriptions. In the autonomous driving domain, nuScene and OpenDV-2K present proper learning sources for
scene diversification. nuScene [22] comprises of 1k scenes, each with a 360◦field-of-view. The dataset also includes a
comprehensive set of sensors, including cameras, radars, and LiDAR, making it a powerful learning resource for world
models in ego vehicles. Following nuScene, OpenDV-2K [305] proposes an even larger dataset with text description

--- Page 18 ---

18
Puspitasari et al.
and a more diverse road conditions and driving scenarios. Meanwhile, in the robotics domain, datasets that cover
holistic modalities can be represented by Ego-Exo4D, DROID, and OXE. Ego-Exo4D [70] is an ego-exocentric dataset
of human activities, totaling 1k hour-long videos. This multimodal dataset not only includes videos and language
descriptions, but also audio, eye gaze, 3D point clouds, pose, and IMU, making it a perfect complement for training a
world model. Meanwhile, DROID [112] and OXE [190] offer robot activities image-based datasets with 76k and 1M
episodes, respectively. With their broad coverage of tasks, these datasets offer a valuable training ground for world
models in robotics. Moreover, large-scale datasets also exist in the game domain, which is represented by Atari Grand
Challenge, Platformers, Yan, and OGameData. Atari Grand Challenge [121] consists of human interaction on Atari 2600
games, consisting of 2k episodes totaling 45 hours of playtime. Other representative datasets are Platformers [19] with
6.8M gameplay videos curated from various Internet games, Yan [318] with 400M high-resolution videos and actions
from 3D games, and OGameData [28] with 1M text-video pairs of various games. Owing to their scale, these gameplay
datasets encompass diverse scenarios and player expertise, providing an effective training ground for developing
strategic intelligence. Lastly, physical simulation datasets [105] can be incorporated to teach the model about objects’
physical properties.
Table 1. T2V benchmark datasets for various evaluation components.
Dimension
Benchmark datasets
General
FETV [156] || EvalCrafter [155] || VBench [99] || HVEval [289] || T2VEval [196]
Compositional
GenAI-Bench [146] || T2V-CompBench [236]
Temporal
TC-Bench [56] || T2VBench [103] || ChronoMagic-bench [331] || VMBench [147] || VideoVerse [274]
Safety
T2VSafetyBench [179] || VidProM [261] || ViBe [207]
World model
WorldSimBench [198] || PhyGenBench [178] || PAI-Bench [357] || Physics-IQ [183] || Morpheus [334]
Reasoning
Gen-ViRe [154] || MMGR [23] || V-ReasonBench [168] || || TiViBench [30] || VBench-2.0 [353]
Others
VC4VG-Bench [45] || Q-Eval-100K [349] || StoryEval [269]
6.2
Benchmark
Like the datasets, benchmark datasets have also evolved in tandem with advances in T2V models. Early benchmark
datasets focus on task-specific evaluation, such as human appearance [323] and simple motion [96]. Holistic benchmark
datasets began emerging in 2024. They are typically organized into seven assessment categories: general quality,
composition, temporal coherence, safety & hallucination, world modeling, reasoning, and others (Table 1). General
quality remains the most commonly emphasized evaluation criterion. Benchmarks on compositional quality evaluate the
relationships of constituents. Temporal quality benchmarks examine the dynamic quality and consistency. World model
benchmark examines how T2Vs conforms to the world rules, including physics. Meanwhile, reasoning benchmark mea-
sure T2V’s ability to perform visual reasoning. Finally, other benchmarks exist for text alignment (VC4VG-Bench [45]),
human preference (Q-Eval-100K [349]), and story composition (StoryEval [269]).
6.3
Metrics
Besides the benchmark dataset, evaluation on T2V also incorporates numerical metrics. There are three general
categories of metrics: visual quality, text-vision faithfulness, and temporal dynamics. The visual quality metric measures
the visual fidelity of the generation. Several widely used visual metrics are IS, FID, and FVD. Inception Score (IS) [219]
measures the average per-frame KL distance between ground truth label distribution and the generated label distribution

--- Page 19 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
19
Table 2. Top-performing T2Vs on several benchmark dimensions. Blue models are open-sourced.
Dimension
Benchmark
Component
Top-3 Performer (hi −→low)
Performance (𝜇/𝜎)
General
Dynamic smoothness
Sora, Runway Gen-3, Dreamina 1.0
73.67/10.58
T2VEval [196]
Text-video alignment
Sora, Runway Gen-3, Dreamina 1.0
72.03/10.28
(Aug 25)
Overall impression
Sora, Runway Gen-3, Dreamina 1.0
69.13/11.43
Commonsense conformity
Sora, Runway Gen-3, Kling 1.0
65.63/11.78
Composition
Interaction
PixVerse-V3, Kling-1.0, Dreamina 1.2
74.20/6.40
Static attribute
PixVerse-V3, Kling-1.0, Dreamina 1.2
69.68/0.66
T2V-Comp
Action
PixVerse-V3, Runway Gen-3, CogVideoX
68.11/13.52
Bench [236]
Spatial
PixVerse-V3, Dreamina 1.2, Kling 1.0
58.14/1.22
(Jan 25)
Numeracy
PixVerse-V3, Kling-1.0, Dreamina 1.2
49.53/7.87
Motion
PixVerse-V3, Runway Gen-3, CogVideoX
27.60/0.85
Dynamic attribute
Runway Gen-3, PixVerse-V3, Mochi
5.19/1.95
Temporal
Camera control
Veo 3, Minimax Hailuo, Sora 2
74.33/1.70
2D layout
Minimax Hailuo, Veo 3, Sora 2
67.00/0.82
Video
Natural constraint
Veo 3, Sora 2, Minimax Hailuo
61.67/5.56
Verse [274]
Commonsense
Sora 2, Veo 3, Minimax Hailuo
57.33/4.50
(Oct 25)
3D depth
Minimax Hailuo, Veo 3, Sora 2
54.00/0.00
Interaction
Sora 2, Veo 3, Minimax Hailuo
44.00/5.36
Mechanics
Sora 2, Veo 3, Wan 2.2
38.00/4.32
Material properties
Minimax Hailuo, Veo 3, Sora 2
21.33/0.47
World model
Magnetism
Runway Gen-3, Lumiere, VideoPoet
37.67/6.13
Physics-
Thermodynamics
Lumiere, VideoPoet, Runway Gen-3
30.00/2.83
IQ [183]
Solid Mechanics
Lumiere, VideoPoet, Runway Gen-3
17.67/2.06
(Feb 25)
Optics
VideoPoet, Lumiere, Stable Video Diffusion
9.00/2.95
Fluid dynamics
Lumiere, VideoPoet, Stable Video Diffusion
7.50/1.78
Reasoning
Planning
Hailuo 2.3, Sora 2, Veo 3.1
75.60/2.44
Spatiotemporal
Seedance 1.0, Veo 3.1, Sora 2
56.90/3.69
Gen-ViRe [154]
Abstract
Sora 2, Hailuo 2.3, Veo 3.1
51.27/6.82
(Dec 25)
Analogy
Wan 2.5, Sora 2, Hailuo 2.3
45.53/5.16
Logical
Sora 2, Veo 3.1, Wan 2.5
44.47/2.53
Perceptual
Sora 2, Hailuo 2.3, Veo 3.1
43.57/4.58
Storyline
Easy plotting
Kling-1.0, Hailuo, Vchitect 2.0
54.17/8.08
Commonsense adherence
Hailuo, Kling-1.0, Pika 1.5
36.30/6.78
Animal story
Kling-1.0, Hailuo, Vchitect 2.0
34.37/10.58
StoryEval [269]
Human story
Hailuo, Kling 1.5, Vchitect 2.0
32.30/7.65
(Jul 25)
Object story
Kling-1.0, Hailuo, Pika 1.5
28.73/5.99
Creativeness
Kling-1.0, Pika 1.5, Hailuo
24.87/7.94
Hard plotting
Kling-1.0, Hailuo, CogVideoX
10.37/4.68
from Inception [240] network. Fréchet Inception Distance (FID) [88] calculates the average per-frame Fréchet distance
between the ground truth samples distribution and the generated samples distributions from the Inception-v3 [241]
network. Fréchet Video Distance (FVD) [248] measures the maximum mean discrepancy (MMD) [74] between ground
truth distribution and generated distribution after being passed to an inflated 3D Inception-v1 network [26]. For
text-vision faithfulness, some common metrics are CLIP R-Precision and CLIP Score, and some newly proposed scores
like VQA Score and TLT Score. CLIP R-Precision [192] is obtained by querying the CLIP model with the generated
image and automatically checking how much the retrieved caption matches the ground truth caption. CLIP Score [87]
is calculated by taking the average (CLIP SIM) [283] or maximum [81] of cosine similarity between the text and vision
embeddings. VQA Score [127] measures the probability of a yes answer to a confirmation question like Does this figure
show *text*? from VLM. TLT Score [102] measures the embedding distance between evaluation embeddings with the

--- Page 20 ---

20
Puspitasari et al.
curated prompt embeddings of the VLM. Additionally, there are several newly proposed metrics to measure temporal
dynamics, such as Dynamic Score [143], MTScore [331], CHScore [331], and NeuS-V [225].
7
APPLICATIONS
7.1
Metaverse
With the capability to understand and simulate physical worlds, it is reasonable to assume that T2Vs could facilitate
the development of the metaverse, offering a more dynamic, personalized, immersive user experience. The metaverse,
conceived as a collective virtual shared space, merges multiple aspects of digital and augmented realities, including
social networks, online gaming, augmented reality (AR), and virtual reality (VR) [124]. The metaverse thrives on the
continuous creation and expansion of its virtual environments and experiences. T2Vs can potentially contribute to
this aspect by enabling the rapid generation of 3D content to populate virtual worlds, since manually constructing 3D
objects is tedious and resource-intensive. This could include everything from environmental backgrounds and animated
textures [12, 73, 294] to complex narrative sequences, thereby enriching the diversity and dynamism of the metaverse’s
content landscape. Additionally, the potential to rapidly construct virtual 3D objects could open up new possibilities,
making feasible what was once thought impossible in the future. The T2V advancements suggest the potential for
creating digital twins modeled after physical items. Other attributes of these items, like sound and tactile feedback
(haptics), may be enhanced in addition to a series of images, for the sake of realistic copies of the world model. T2Vs
can also unleash the potential of the metaverse, through studying the interaction between virtual entities and human
users. This includes evaluating activities that are difficult to carry out in the actual world, such as user studies that
may raise ethical issues (e.g., racism or dark patterns [263]) and technological constraints (e.g., deploying a movable
100-meter building [40]). Using the future generation of advanced T2Vs, researchers may simulate augmented reality in
virtual environments (i.e., virtual reality) to analyze user behaviors and their response to 3D user interfaces, with the
premise that modern virtual reality headsets can provide high-quality video and seamless experiences.
7.2
Robotics
In robotic applications, T2Vs can be an affordable platform for robots to learn manipulation actions [312]. This facilitates
open-world learning by lowering the cost and effort for data collection on human demonstration, which was initially
performed by video recording of directed choreography with 3D motion capture [72]. Early attempts to leverage
robot learning via video are made by supplying trajectory signals (e.g., flow vectors) to an action image [83]. From
this, trajectory learning is improved by incorporating detailed text description [299] and robot state [284]. Such a
development encourages the works in robot learning to assimilate recent generative AI models such as T2I [108] and
T2V [46], which inherit the power of LLM to act as a policy generator or reward for reinforcement learning [47, 232].
This advancement enables the realization of scalable, unsupervised, and generalizable robot learning.
7.3
Autonomous Driving
Similar to the robotic application, T2Vs for autonomous driving are also mainly utilized as data generators for uncommon
road scenes, such as traffic accidents [52], which are enormously costly to recreate. The availability of such data is
highly beneficial for designing autonomous vehicles’ safety features [39] as it enables learning the trajectory before and
after the accident. Further, video generation for this field can also provide panoramic driving scene data in various road
conditions that were originally limited in supply [134, 280]. Output generated by T2Vs enables autonomous vehicle

--- Page 21 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
21
intelligence systems to learn directly from real-world environments instead of being confined in the game environment,
which was commonly used to simulate the driving scene [132, 265].
7.4
Healthcare
Despite lingering doubts about its trustworthiness, T2V holds the potential to improve the healthcare industry. Current
studies primarily implement these models in healthcare education and medical imaging. In medical education, T2Vs can
help to create training videos for healthcare practitioners whose number is considerably limited since the collection
process involves real medical cases [220]. This is particularly useful in generating educational videos that involve
rare cases. In its function to enhance medical imaging, T2Vs have been explored in various examinations such as
radiology [15], CT scan [80], and endoscopy [129]. T2V also empowers any-to-any generation in the medical domain [180,
333]. Besides, T2V may promote the equal distribution of health services between highly developed areas and rural
areas. One interesting study by Loh and Then [160] envisions the data conversion of echocardiogram video into text to
facilitate a more economical and faster information transmission between urban and rural regions.
8
DISCUSSION AND FUTURE DIRECTION
8.1
Homework on Technical Improvement
Despite the emergence of high-performing commercial T2Vs and the rapid exploration of many core world model
requirements (e.g., consistency and physics), several aspects remain open questions. First, diversity and consistency
remain two distinct dimensions. Generating the whole video at once protects consistency but sacrifices diversity [343];
on the other hand, multi-step generation tends to prioritize diversity and struggle to maintain consistency [101]. Second,
consistency is still costly to afford. As 3D data, video can be modeled by 3D attention, either full or pseudo. 3D full
attention is computationally expensive, while pseudo-3D attention is unstable on scene with large spatial motion [315].
Some recent advances in temporal attention or autoregressive-based generation have improved the temporal consistency
modeling, but still fail to circumvent temporal flickers [164]. Third, long video synthesis remains challenging. Long video
generations still rely on a temporal interpolation mechanism whose quality is capped at the base model capacity [309].
On the cascaded generation framework, temporal interpolation struggles to model complicated motions [100] and is
inferior in multi-scene generation [343]. Further, developing a true long-video synthesizer is challenged by the train-test
data discrepancy, where the model only sees short clips during training but is forced to generalize to long videos at
inference [320]. Moreover, training on long videos is not only costly but also limited by the data availability [320]. Fourth,
limited world understanding. As discussed in § 4, current T2Vs still rely on external supplementary cues to understand
the world rule, which exposes the insufficiency of world understanding in T2Vs. Relying on external supplements,
however, binds the generation quality to the accuracy of the reference [100]. Full-supervision on world modeling data
may be the closest alternative for T2Vs to statistically embed world understanding in the model [145]; however, it
is capped by the availability of world-modeling-specific data for learning [224, 268]. This exhibits the insufficiency
of a proper training sample for world modeling in the current pool of training datasets [105]. Table 2 reflects these
limitations, that even the top-performing modern T2Vs still struggle in physical simulation. Fifth, insufficient exploration
for flexible interaction. Interaction controls remain largely limited to visual and textual forms. In contrast, true world
modeling requires richer modalities (e.g., LiDAR, haptics, and symbolic primitives). Further, research on AI-human
interaction, such as human-in-the-loop generation, remains limited. This highlights the need for further investigation
into human-computer interaction (HCI) within T2V [182].

--- Page 22 ---

22
Puspitasari et al.
8.2
Ethical and Social Implications
The significant advancement in T2V also entails numerous drawbacks, including, but not limited to, misuse, privacy and
copyright, and fairness [79]. Hyper-realistic videos from T2V may be misused for creating counterfactual evidence in
criminal cases. The plaintiff may use the generated content in court trials, exacerbating the pressure on the defendant
side [71]. Indeed, this calls for adaptation of detection and preventive measures from the lawmakers. The web data
used to train T2V may contain personal identifications whose owners may not intend to share. If T2V suffers from a
data memorization issue, it could generate someone’s face in the video, leaking that individual’s privacy. [171]. Privacy
and copyright dilemma is currently faced by WebVid-10M datasets, in which owners of some Shutterstock videos take
down their posts, making the videos gradually disappear and ceasing the usefulness of the dataset. The fairness issue is
another caution on T2V as a world model. For instance, Western culture bias in the training dataset may be inherited
by the model, making it generate Western-like output [63]. While it sounds trivial, this can be a substantial issue in
critical situations, such as robot-assisted surgery or emergency reaction while driving. Thus, it is important to pay
more attention to the research on model debiasing.
9
CONCLUSION
The arrival of Sora, which claims as world model, has surfaced the importance of a profound understanding of the
relationship between text-to-video and world model. Specifically, it is essential to match world model requirements and
the text-to-video generation model’s proposals. Our survey pinpoints that the relationship between the two models
is established through the adherence of elements in spatial, action, and strategic intelligence. Despite moving closer
to being a world model, text-to-video generation models still need to solve several important limitations, both from
technical and ethical perspectives. We hope that future studies arising from inter-disciplinary collaborations can solve
diverse challenges in synthesizing video from text, to foster the realization of the world model.
REFERENCES
[1] Daechul Ahn, Yura Choi, Youngjae Yu, Dongyeop Kang, and Jonghyun Choi. 2024. Tuning large multimodal models for videos using reinforcement
learning from ai feedback. arXiv preprint arXiv:2402.03746 (2024).
[2] Dreamina AI. 2025. Dreamina. https://dreaminai.org/
[3] Hailuo AI. 2025. Hailuo. https://hailuoai.video/
[4] Kling AI. 2025. Kling. https://klingai.com/cn/
[5] MiniMax AI. 2025. MiniMax Hailuo 02, World-Class Quality, Record-Breaking Cost Efficiency. https://www.minimax.io/news/minimax-hailuo-02
[6] Pika AI. 2025. Pika. https://pikalabs.net/pika-1-5/
[7] PixVerse AI. 2025. PixVerse. https://pixversecn.com/
[8] James F Allen and Johannes A Koomen. 1983. Planning using a temporal world model. In Proceedings of the Eighth international joint conference on
Artificial intelligence-Volume 2. 741–747.
[9] Eloi Alonso, Adam Jelley, Vincent Micheli, Anssi Kanervisto, Amos J Storkey, Tim Pearce, and François Fleuret. 2024. Diffusion for world modeling:
Visual details matter in atari. Advances in Neural Information Processing Systems 37 (2024), 58757–58791.
[10] Peter Anderson, Qi Wu, Damien Teney, Jake Bruce, Mark Johnson, Niko Sünderhauf, Ian Reid, Stephen Gould, and Anton Van Den Hengel. 2018.
Vision-and-language navigation: Interpreting visually-grounded navigation instructions in real environments. In Proceedings of the IEEE conference
on computer vision and pattern recognition. 3674–3683.
[11] Vladimir Arkhipkin, Zein Shaheen, Viacheslav Vasilev, Elizaveta Dakhova, Konstantin Sobolev, Andrey Kuznetsov, and Denis Dimitrov. 2024.
Improveyourvideos: Architectural improvements for text-to-video generation pipeline. IEEE Access (2024).
[12] Samaneh Azadi, Akbar Shah, Thomas Hayes, Devi Parikh, and Sonal Gupta. 2023. Make-an-animation: Large-scale text-conditional 3d human
motion generation. In Proceedings of the IEEE/CVF International Conference on Computer Vision. 15039–15048.
[13] Max Bain, Arsha Nagrani, Gül Varol, and Andrew Zisserman. 2021. Frozen in time: A joint video and image encoder for end-to-end retrieval. In
Proceedings of the IEEE/CVF International Conference on Computer Vision. 1728–1738.
[14] Omer Bar-Tal, Hila Chefer, Omer Tov, Charles Herrmann, Roni Paiss, Shiran Zada, Ariel Ephrat, Junhwa Hur, Guanghui Liu, Amit Raj, et al. 2024.
Lumiere: A space-time diffusion model for video generation. In SIGGRAPH Asia 2024 Conference Papers. 1–11.

--- Page 23 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
23
[15] Nathan Benaich, Elliot K Fishman, Steven P Rowe, Linda C Chu, and Elias Lugo-Fagundo. 2023. The Current State of Artificial Intelligence and Its
Intersection With Radiology. Journal of the American College of Radiology (2023).
[16] Johan Bjorck, Fernando Castañeda, Nikita Cherniadev, Xingye Da, Runyu Ding, Linxi Fan, Yu Fang, Dieter Fox, Fengyuan Hu, Spencer Huang,
et al. 2025. Gr00t n1: An open foundation model for generalist humanoid robots. arXiv preprint arXiv:2503.14734 (2025).
[17] Andreas Blattmann, Tim Dockhorn, Sumith Kulal, Daniel Mendelevitch, Maciej Kilian, Dominik Lorenz, Yam Levi, Zion English, Vikram Voleti,
Adam Letts, et al. 2023. Stable video diffusion: Scaling latent video diffusion models to large datasets. arXiv preprint arXiv:2311.15127 (2023).
[18] Andreas Blattmann, Robin Rombach, Huan Ling, Tim Dockhorn, Seung Wook Kim, Sanja Fidler, and Karsten Kreis. 2023. Align your latents:
High-resolution video synthesis with latent diffusion models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition.
22563–22575.
[19] Jake Bruce, Michael D Dennis, Ashley Edwards, Jack Parker-Holder, Yuge Shi, Edward Hughes, Matthew Lai, Aditi Mavalankar, Richie Steigerwald,
Chris Apps, et al. 2024. Genie: Generative interactive environments. In Forty-first International Conference on Machine Learning.
[20] Jiazi Bu, Pengyang Ling, Pan Zhang, Tong Wu, Xiaoyi Dong, Yuhang Zang, Yuhang Cao, Dahua Lin, and Jiaqi Wang. 2025. ByTheWay: Boost
Your Text-to-Video Generation Model to Higher Quality in a Training-free Way. In Proceedings of the Computer Vision and Pattern Recognition
Conference. 12999–13008.
[21] Manh-Hung Bui, Vinh-Tiep Nguyen, Bich-Nga Pham, and Ngan Luu-Thuy Nguyen. 2025. PerSynth: Personalized Character Video Synthesis from
Text Prompts. In 2025 International Conference on Multimedia Analysis and Pattern Recognition (MAPR). IEEE, 1–6.
[22] Holger Caesar, Varun Bankiti, Alex H Lang, Sourabh Vora, Venice Erin Liong, Qiang Xu, Anush Krishnan, Yu Pan, Giancarlo Baldan, and Oscar
Beijbom. 2020. nuscenes: A multimodal dataset for autonomous driving. In Proceedings of the IEEE/CVF conference on computer vision and pattern
recognition. 11621–11631.
[23] Zefan Cai, Haoyi Qiu, Tianyi Ma, Haozhe Zhao, Gengze Zhou, Kung-Hsiang Huang, Parisa Kordjamshidi, Minjia Zhang, Xiao Wen, Jiuxiang Gu,
et al. 2025. MMGR: Multi-Modal Generative Reasoning. arXiv preprint arXiv:2512.14691 (2025).
[24] Natalia Caldera. 2025. VerifyVid: A Causal-Aware Framework for Factually Grounded Text-to-Video Generation with Temporal Consistency.
(2025).
[25] Sirley Carballo. 2024. How openai’s Sora is Transforming Higher Education Video content. https://www.enrollify.org/blog/how-openais-sora-is-
transforming-higher-education-video-content
[26] João Carreira and Andrew Zisserman. 2017. Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset. In 2017 IEEE Conference on
Computer Vision and Pattern Recognition (CVPR). 4724–4733.
[27] Chun-Peng Chang, Chen-Yu Wang, Julian Schmidt, Holger Caesar, and Alain Pagani. 2025. Seeing Clearly, Forgetting Deeply: Revisiting Fine-Tuned
Video Generators for Driving Simulation. arXiv preprint arXiv:2508.16512 (2025).
[28] Haoxuan Che, Xuanhua He, Quande Liu, Cheng Jin, and Hao Chen. 2024. Gamegen-x: Interactive open-world game video generation. arXiv
preprint arXiv:2411.00769 (2024).
[29] Hong Chen, Xin Wang, Yipeng Zhang, Yuwei Zhou, Zeyang Zhang, Siao Tang, and Wenwu Zhu. 2024. Disenstudio: Customized multi-subject
text-to-video generation with disentangled spatial control. In Proceedings of the 32nd ACM International Conference on Multimedia. 3637–3646.
[30] Harold Haodong Chen, Disen Lan, Wen-Jie Shu, Qingyang Liu, Zihan Wang, Sirui Chen, Wenkai Cheng, Kanghao Chen, Hongfei Zhang, Zixin
Zhang, et al. 2025. TiViBench: Benchmarking Think-in-Video Reasoning for Video Generative Models. arXiv preprint arXiv:2511.13704 (2025).
[31] Junsong Chen, Jincheng Yu, Chongjian Ge, Lewei Yao, Enze Xie, Yue Wu, Zhongdao Wang, James Kwok, Ping Luo, Huchuan Lu, et al. 2023.
Pixart-𝛼: Fast training of diffusion transformer for photorealistic text-to-image synthesis. arXiv preprint arXiv:2310.00426 (2023).
[32] Jiaqi Chen, Xiaoye Zhu, Yue Wang, Tianyang Liu, Xinhui Chen, Ying Chen, Chak Tou Leong, Yifei Ke, Joseph Liu, Yiwen Yuan, et al. 2025. Symbolic
Representation for Any-to-Any Generative Tasks. In Proceedings of the Computer Vision and Pattern Recognition Conference. 27816–27826.
[33] Shoufa Chen, Mengmeng Xu, Jiawei Ren, Yuren Cong, Sen He, Yanping Xie, Animesh Sinha, Ping Luo, Tao Xiang, and Juan-Manuel Perez-Rua.
2024. Gentron: Diffusion transformers for image and video generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition. 6441–6451.
[34] Yunuo Chen, Junli Cao, Vidit Goel, Sergei Korolev, Chenfanfu Jiang, Jian Ren, Sergey Tulyakov, and Anil Kag. 2025. Towards physical understanding
in video generation: A 3d point regularization approach. arXiv preprint arXiv:2502.03639 (2025).
[35] Xiaowei Chi, Chun-Kai Fan, Hengyuan Zhang, Xingqun Qi, Rongyu Zhang, Anthony Chen, Chi-Min Chan, Wei Xue, Qifeng Liu, Shanghang
Zhang, et al. 2025. Empowering World Models with Reflection for Embodied Video Prediction. In Forty-second International Conference on Machine
Learning.
[36] Kyunghyun Cho, Bart Van Merriënboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, and Yoshua Bengio. 2014. Learning
phrase representations using RNN encoder-decoder for statistical machine translation. arXiv preprint arXiv:1406.1078 (2014).
[37] François Chollet. 2017. Xception: Deep Learning with Depthwise Separable Convolutions. In 2017 IEEE Conference on Computer Vision and Pattern
Recognition (CVPR). 1800–1807.
[38] Werner Damm and Bernd Finkbeiner. 2011. Does it pay to extend the perimeter of a world model?. In International Symposium on Formal Methods.
Springer, 12–26.
[39] Minh-Son Dao, Muhamad Hilmil Muchtar Aditya Pradana, and Koji Zettsu. 2023. MM-TrafficRisk: A Video-based Fleet Management Application
for Traffic Risk Prediction, Prevention, and Querying. In 2023 IEEE International Conference on Big Data (BigData). IEEE, 1697–1706.

--- Page 24 ---

24
Puspitasari et al.
[40] Jeffrey A. Delmerico, Roi Poranne, Federica Bogo, Helen Oleynikova, Eric Vollenweider, Stelian Coros, Juan Nieto, and Marc Pollefeys. 2022. Spatial
Computing and Intuitive Interaction: Bringing Mixed Reality and Robotics Together. IEEE Robotics & Automation Magazine 29 (2022), 45–57.
[41] Kangle Deng, Tianyi Fei, Xin Huang, and Yuxin Peng. 2019. IRC-GAN: Introspective Recurrent Convolutional GAN for Text-to-video Generation..
In IJCAI. 2216–2222.
[42] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. Bert: Pre-training of deep bidirectional transformers for language
understanding. NAACL (2019).
[43] Prafulla Dhariwal and Alexander Nichol. 2021. Diffusion models beat gans on image synthesis. Advances in neural information processing systems
34 (2021), 8780–8794.
[44] Jingtao Ding, Yunke Zhang, Yu Shang, Yuheng Zhang, Zefang Zong, Jie Feng, Yuan Yuan, Hongyuan Su, Nian Li, Nicholas Sukiennik, et al. 2025.
Understanding world or predicting future? a comprehensive survey of world models. Comput. Surveys 58, 3 (2025), 1–38.
[45] Yang Du, Zhuoran Lin, Kaiqiang Song, Biao Wang, Zhicheng Zheng, Tiezheng Ge, Bo Zheng, and Qin Jin. 2025. VC4VG: Optimizing Video Captions
for Text-to-Video Generation. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing. 1124–1138.
[46] Yilun Du, Mengjiao Yang, Pete Florence, Fei Xia, Ayzaan Wahid, Brian Ichter, Pierre Sermanet, Tianhe Yu, Pieter Abbeel, Joshua B Tenenbaum,
et al. 2023. Video language planning. arXiv preprint arXiv:2310.10625 (2023).
[47] Alejandro Escontrela, Ademi Adeniji, Wilson Yan, Ajay Jain, Xue Bin Peng, Ken Goldberg, Youngwoon Lee, Danijar Hafner, and Pieter Abbeel.
2024. Video prediction models as rewards for reinforcement learning. Advances in Neural Information Processing Systems 36 (2024).
[48] Patrick Esser, Johnathan Chiu, Parmida Atighehchian, Jonathan Granskog, and Anastasis Germanidis. 2023. Structure and content-guided video
synthesis with diffusion models. In Proceedings of the IEEE/CVF international conference on computer vision. 7346–7356.
[49] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel,
et al. 2024. Scaling rectified flow transformers for high-resolution image synthesis. In Forty-first international conference on machine learning.
[50] Tiehan Fan, Kepan Nan, Rui Xie, Penghao Zhou, Zhenheng Yang, Chaoyou Fu, Xiang Li, Jian Yang, and Ying Tai. 2025. Instancecap: Improving text-
to-video generation via instance-aware structured caption. In Proceedings of the Computer Vision and Pattern Recognition Conference. 28974–28983.
[51] Weichen Fan, Chenyang Si, Junhao Song, Zhenyu Yang, Yinan He, Long Zhuo, Ziqi Huang, Ziyue Dong, Jingwen He, Dongwei Pan, et al. 2025.
Vchitect-2.0: Parallel transformer for scaling up video diffusion models. arXiv preprint arXiv:2501.08453 (2025).
[52] Jianwu Fang, Lei-Lei Li, Kuan Yang, Zhedong Zheng, Jianru Xue, and Tat-Seng Chua. 2022. Cognitive accident prediction in driving scenes: A
multimodality benchmark. arXiv preprint arXiv:2212.09381 (2022).
[53] Yu Fang, Yue Yang, Xinghao Zhu, Kaiyuan Zheng, Gedas Bertasius, Daniel Szafir, and Mingyu Ding. 2025. Rebot: Scaling robot learning with
real-to-sim-to-real robotic video synthesis. arXiv preprint arXiv:2503.14526 (2025).
[54] Hao Fei, Shengqiong Wu, Wei Ji, Hanwang Zhang, and Tat-Seng Chua. 2024. Dysen-vdm: Empowering dynamics-aware text-to-video diffusion
with llms. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 7641–7653.
[55] Hao Fei, Shengqiong Wu, Hanwang Zhang, Tat-Seng Chua, and Shuicheng Yan. 2024. Vitron: A unified pixel-level vision llm for understanding,
generating, segmenting, editing. Advances in neural information processing systems 37 (2024), 57207–57239.
[56] Weixi Feng, Jiachen Li, Michael Saxon, Tsu-jui Fu, Wenhu Chen, and William Yang Wang. 2024. Tc-bench: Benchmarking temporal compositionality
in text-to-video and image-to-video generation. arXiv preprint arXiv:2406.08656 (2024).
[57] Weixi Feng, Chao Liu, Sifei Liu, William Yang Wang, Arash Vahdat, and Weili Nie. 2025. Blobgen-vid: Compositional text-to-video generation with
blob video representations. In Proceedings of the Computer Vision and Pattern Recognition Conference. 12989–12998.
[58] Chelsea Finn and Sergey Levine. 2017. Deep visual foresight for planning robot motion. In 2017 IEEE international conference on robotics and
automation (ICRA). IEEE, 2786–2793.
[59] Stephen Fox. 2022. Human–Artificial Intelligence Systems: How Human Survival First Principles Influence Machine Learning World Models.
Systems 10, 6 (2022), 260.
[60] Rinon Gal, Yael Vinker, Yuval Alaluf, Amit Bermano, Daniel Cohen-Or, Ariel Shamir, and Gal Chechik. 2024. Breathing life into sketches using
text-to-video priors. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 4325–4336.
[61] Shanghua Gao, Pan Zhou, Ming-Ming Cheng, and Shuicheng Yan. 2023. Masked diffusion transformer is a strong image synthesizer. In Proceedings
of the IEEE/CVF international conference on computer vision. 23164–23173.
[62] Yu Gao, Haoyuan Guo, Tuyen Hoang, Weilin Huang, Lu Jiang, Fangyuan Kong, Huixia Li, Jiashi Li, Liang Li, Xiaojie Li, et al. 2025. Seedance 1.0:
Exploring the Boundaries of Video Generation Models. arXiv preprint arXiv:2506.09113 (2025).
[63] Sanjana Gautam, Pranav Narayanan Venkit, and Sourojit Ghosh. 2024. From Melting Pots to Misrepresentations: Exploring Harms in Generative
AI. arXiv preprint arXiv:2403.10776 (2024).
[64] Songwei Ge, Seungjun Nah, Guilin Liu, Tyler Poon, Andrew Tao, Bryan Catanzaro, David Jacobs, Jia-Bin Huang, Ming-Yu Liu, and Yogesh Balaji.
2023. Preserve your own correlation: A noise prior for video diffusion models. In Proceedings of the IEEE/CVF International Conference on Computer
Vision. 22930–22941.
[65] Zhiqi Ge, Hongzhe Huang, Mingze Zhou, Juncheng Li, Guoming Wang, Siliang Tang, and Yueting Zhuang. 2024. Worldgpt: Empowering llm as
multimodal world model. In Proceedings of the 32nd ACM International Conference on Multimedia. 7346–7355.
[66] Rohit Girdhar, Mannat Singh, Andrew Brown, Quentin Duval, Samaneh Azadi, Sai Saketh Rambhatla, Akbar Shah, Xi Yin, Devi Parikh, and Ishan
Misra. 2023. Emu video: Factorizing text-to-video generation by explicit image conditioning. arXiv preprint arXiv:2311.10709 (2023).

--- Page 25 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
25
[67] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. 2014.
Generative adversarial nets. Advances in neural information processing systems 27 (2014).
[68] Google. 2025. Veo. https://deepmind.google/models/veo/
[69] Raghav Goyal, Samira Ebrahimi Kahou, Vincent Michalski, Joanna Materzynska, Susanne Westphal, Heuna Kim, Valentin Haenel, Ingo Fruend,
Peter Yianilos, Moritz Mueller-Freitag, et al. 2017. The" something something" video database for learning and evaluating visual common sense. In
Proceedings of the IEEE international conference on computer vision. 5842–5850.
[70] Kristen Grauman, Andrew Westbury, Lorenzo Torresani, Kris Kitani, Jitendra Malik, Triantafyllos Afouras, Kumar Ashutosh, Vijay Baiyya, Siddhant
Bansal, Bikram Boote, et al. 2024. Ego-exo4d: Understanding skilled human activity from first-and third-person perspectives. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition. 19383–19400.
[71] Sam Gregory. 2023. Fortify the truth: How to defend human rights in an age of deepfakes and generative AI. , 702–714 pages.
[72] Liang-Yan Gui, Kevin Zhang, Yu-Xiong Wang, Xiaodan Liang, José MF Moura, and Manuela Veloso. 2018. Teaching robots to predict human
motion. In 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 562–567.
[73] Chuan Guo, Shihao Zou, Xinxin Zuo, Sen Wang, Wei Ji, Xingyu Li, and Li Cheng. 2022. Generating diverse and natural 3d human motions from
text. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 5152–5161.
[74] Meng-Hao Guo, Tian-Xing Xu, Jiang-Jiang Liu, Zheng-Ning Liu, Peng-Tao Jiang, Tai-Jiang Mu, Song-Hai Zhang, Ralph R Martin, Ming-Ming
Cheng, and Shi-Min Hu. 2022. Attention mechanisms in computer vision: A survey. Computational visual media 8, 3 (2022), 331–368.
[75] Xun Guo, Mingwu Zheng, Liang Hou, Yuan Gao, Yufan Deng, Chongyang Ma, Weiming Hu, Zhengjun Zha, Haibin Huang, Pengfei Wan, et al.
2023. I2V-Adapter: A General Image-to-Video Adapter for Video Diffusion Models. arXiv preprint arXiv:2312.16693 (2023).
[76] David Ha and Jürgen Schmidhuber. 2018. Recurrent world models facilitate policy evolution. Advances in neural information processing systems 31
(2018).
[77] David Ha and Jürgen Schmidhuber. 2018. World models. arXiv preprint arXiv:1803.10122 (2018).
[78] Danijar Hafner, Wilson Yan, and Timothy Lillicrap. 2025. Training agents inside of scalable world models. arXiv preprint arXiv:2509.24527 (2025).
[79] Thilo Hagendorff. 2024. Mapping the Ethics of Generative AI: A Comprehensive Scoping Review. arXiv preprint arXiv:2402.08323 (2024).
[80] Ibrahim Ethem Hamamci, Sezgin Er, Enis Simsar, Alperen Tezcan, Ayse Gulnihan Simsek, Furkan Almas, Sevval Nil Esirgun, Hadrien Reynaud,
Sarthak Pati, Christian Bluethgen, et al. 2023. GenerateCT: text-guided 3D chest CT generation. arXiv preprint arXiv:2305.16037 (2023).
[81] Ligong Han, Jian Ren, Hsin-Ying Lee, Francesco Barbieri, Kyle Olszewski, Shervin Minaee, Dimitris Metaxas, and Sergey Tulyakov. 2022. Show me
what and tell me how: Video synthesis via multimodal conditioning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition. 3615–3625.
[82] Yutong Hao, Chen Chen, Ajmal Saeed Mian, Chang Xu, and Daochang Liu. 2025. Enhancing physical plausibility in video generation by reasoning
the implausibility. arXiv preprint arXiv:2509.24702 (2025).
[83] Zekun Hao, Xun Huang, and Serge Belongie. 2018. Controllable video generation with sparse trajectories. In Proceedings of the IEEE Conference on
Computer Vision and Pattern Recognition. 7854–7863.
[84] Haoran He, Yang Zhang, Liang Lin, Zhongwen Xu, and Ling Pan. 2025. Pre-trained video generative models as world simulators. arXiv preprint
arXiv:2502.07825 (2025).
[85] Yingqing He, Menghan Xia, Haoxin Chen, Xiaodong Cun, Yuan Gong, Jinbo Xing, Yong Zhang, Xintao Wang, Chao Weng, Ying Shan, et al. 2024.
Storytelling Video Generation with Retrieval Augmentation and Character Consistency. In European Conference on Computer Vision. Springer,
218–234.
[86] Roberto Henschel, Levon Khachatryan, Hayk Poghosyan, Daniil Hayrapetyan, Vahram Tadevosyan, Zhangyang Wang, Shant Navasardyan, and
Humphrey Shi. 2025. Streamingt2v: Consistent, dynamic, and extendable long video generation from text. In Proceedings of the Computer Vision
and Pattern Recognition Conference. 2568–2577.
[87] Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. 2021. Clipscore: A reference-free evaluation metric for image captioning.
arXiv preprint arXiv:2104.08718 (2021).
[88] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. 2017. Gans trained by a two time-scale update rule
converge to a local nash equilibrium. Advances in neural information processing systems 30 (2017).
[89] Jonathan Ho, William Chan, Chitwan Saharia, Jay Whang, Ruiqi Gao, Alexey Gritsenko, Diederik P Kingma, Ben Poole, Mohammad Norouzi,
David J Fleet, et al. 2022. Imagen video: High definition video generation with diffusion models. arXiv preprint arXiv:2210.02303 (2022).
[90] Jonathan Ho, Ajay Jain, and Pieter Abbeel. 2020. Denoising diffusion probabilistic models. Advances in Neural Information Processing Systems 33
(2020), 6840–6851.
[91] Jonathan Ho and Tim Salimans. 2022. Classifier-free diffusion guidance. arXiv preprint arXiv:2207.12598 (2022).
[92] Jonathan Ho, Tim Salimans, Alexey Gritsenko, William Chan, Mohammad Norouzi, and David J Fleet. 2022. Video diffusion models. arXiv preprint
arXiv:2204.03458 (2022).
[93] Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long short-term memory. Neural computation 9, 8 (1997), 1735–1780.
[94] Susung Hong, Junyoung Seo, Heeseong Shin, Sunghwan Hong, and Seungryong Kim. 2024. Large language models are frame-level directors for
zero-shot text-to-video generation. In First Workshop on Controllable Video Generation@ ICML24.
[95] Wenyi Hong, Ming Ding, Wendi Zheng, Xinghan Liu, and Jie Tang. 2022. Cogvideo: Large-scale pretraining for text-to-video generation via
transformers. arXiv preprint arXiv:2205.15868 (2022).

--- Page 26 ---

26
Puspitasari et al.
[96] Yaosi Hu, Chong Luo, and Zhenzhong Chen. 2023. A benchmark for controllable text-image-to-video generation. IEEE Transactions on Multimedia
26 (2023), 1706–1719.
[97] Hanzhuo Huang, Yufan Feng, Cheng Shi, Lan Xu, Jingyi Yu, and Sibei Yang. 2024. Free-bloom: Zero-shot text-to-video generator with llm director
and ldm animator. Advances in Neural Information Processing Systems 36 (2024).
[98] Hsin-Ping Huang, Yu-Chuan Su, Deqing Sun, Lu Jiang, Xuhui Jia, Yukun Zhu, and Ming-Hsuan Yang. 2025. Fine-grained controllable video
generation via object appearance and context. In 2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV). IEEE, 3698–3708.
[99] Ziqi Huang, Yinan He, Jiashuo Yu, Fan Zhang, Chenyang Si, Yuming Jiang, Yuanhan Zhang, Tianxing Wu, Qingyang Jin, Nattapol Chanpaisit, et al.
2024. Vbench: Comprehensive benchmark suite for video generative models. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition. 21807–21818.
[100] Junhwa Hur, Charles Herrmann, Saurabh Saxena, Janne Kontkanen, Wei-Sheng Lai, Yichang Shih, Michael Rubinstein, David J Fleet, and Deqing
Sun. 2025. High-resolution frame interpolation with patch-based cascaded diffusion. In Proceedings of the AAAI Conference on Artificial Intelligence,
Vol. 39. 3868–3876.
[101] Diljeet Jagpal, Xi Chen, and Vinay P Namboodiri. 2025. EIDT-V: Exploiting Intersections in Diffusion Trajectories for Model-Agnostic, Zero-Shot,
Training-Free Text-to-Video Generation. In Proceedings of the Computer Vision and Pattern Recognition Conference. 18219–18228.
[102] Pengliang Ji and Junchen Liu. 2024. Tltscore: Towards long-tail effects in text-to-visual evaluation with generative foundation models. In Proceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 5302–5313.
[103] Pengliang Ji, Chuyang Xiao, Huilin Tai, and Mingxiao Huo. 2024. T2vbench: Benchmarking temporal dynamics for text-to-video generation. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 5325–5335.
[104] Sihui Ji, Xi Chen, Xin Tao, Pengfei Wan, and Hengshuang Zhao. 2025. PhysMaster: Mastering Physical Representation for Video Generation via
Reinforcement Learning. arXiv preprint arXiv:2510.13809 (2025).
[105] Hanxiao Jiang, Hao-Yu Hsu, Kaifeng Zhang, Hsin-Ni Yu, Shenlong Wang, and Yunzhu Li. 2025. Phystwin: Physics-informed reconstruction and
simulation of deformable objects from videos. arXiv preprint arXiv:2503.17973 (2025).
[106] Yuming Jiang, Shuai Yang, Tong Liang Koh, Wayne Wu, Chen Change Loy, and Ziwei Liu. 2023. Text2performer: Text-driven human video
generation. In Proceedings of the IEEE/CVF International Conference on Computer Vision. 22747–22757.
[107] Anssi Kanervisto, Dave Bignell, Linda Yilin Wen, Martin Grayson, Raluca Georgescu, Sergio Valcarcel Macua, Shan Zheng Tan, Tabish Rashid, Tim
Pearce, Yuhan Cao, et al. 2025. World and human action models towards gameplay ideation. Nature 638, 8051 (2025), 656–663.
[108] Ivan Kapelyukh, Vitalis Vosylius, and Edward Johns. 2023. Dall-e-bot: Introducing web-scale diffusion models to robotics. IEEE Robotics and
Automation Letters (2023).
[109] Ozgur Kara, Krishna Kumar Singh, Feng Liu, Duygu Ceylan, James M Rehg, and Tobias Hinz. 2025. ShotAdapter: Text-to-Multi-Shot Video
Generation with Diffusion Models. In Proceedings of the Computer Vision and Pattern Recognition Conference. 28405–28415.
[110] Gyorgy Kepes. 1995. Language of vision. Courier Corporation.
[111] Levon Khachatryan, Andranik Movsisyan, Vahram Tadevosyan, Roberto Henschel, Zhangyang Wang, Shant Navasardyan, and Humphrey Shi.
2023. Text2video-zero: Text-to-image diffusion models are zero-shot video generators. In Proceedings of the IEEE/CVF International Conference on
Computer Vision. 15954–15964.
[112] Alexander Khazatsky, Karl Pertsch, Suraj Nair, Ashwin Balakrishna, Sudeep Dasari, Siddharth Karamcheti, Soroush Nasiriany, Mohan Kumar Srirama,
Lawrence Yunliang Chen, Kirsty Ellis, et al. 2024. Droid: A large-scale in-the-wild robot manipulation dataset. arXiv preprint arXiv:2403.12945
(2024).
[113] Doyeon Kim, Donggyu Joo, and Junmo Kim. 2020. Tivgan: Text to image to video generation with step-by-step evolutionary generator. IEEE
Access 8 (2020), 153113–153122.
[114] Jaemin Kim, Bryan Sangwoo Kim, and Jong Chul Ye. 2025. Free2Guide: Training-Free Text-to-Video Alignment using Image LVLM. In Proceedings
of the IEEE/CVF International Conference on Computer Vision. 17920–17929.
[115] Seung Wook Kim, Yuhao Zhou, Jonah Philion, Antonio Torralba, and Sanja Fidler. 2020. Learning to simulate dynamic environments with gamegan.
In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 1231–1240.
[116] Taehoon Kim, ChanHee Kang, JaeHyuk Park, Daun Jeong, ChangHee Yang, Suk-Ju Kang, and Kyeongbo Kong. 2024. Human motion aware
text-to-video generation with explicit camera control. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision.
5081–5090.
[117] Diederik P Kingma and Max Welling. 2013. Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114 (2013).
[118] Jing Yu Koh, Honglak Lee, Yinfei Yang, Jason Baldridge, and Peter Anderson. 2021. Pathdreamer: A world model for indoor navigation. In
Proceedings of the IEEE/CVF International Conference on Computer Vision. 14738–14748.
[119] Dan Kondratyuk, Lijun Yu, Xiuye Gu, José Lezama, Jonathan Huang, Rachel Hornung, Hartwig Adam, Hassan Akbari, Yair Alon, Vighnesh
Birodkar, et al. 2023. Videopoet: A large language model for zero-shot video generation. arXiv preprint arXiv:2312.14125 (2023).
[120] Weijie Kong, Qi Tian, Zijian Zhang, Rox Min, Zuozhuo Dai, Jin Zhou, Jiangfeng Xiong, Xin Li, Bo Wu, Jianwei Zhang, et al. 2024. Hunyuanvideo:
A systematic framework for large video generative models. arXiv preprint arXiv:2412.03603 (2024).
[121] Vitaly Kurin, Sebastian Nowozin, Katja Hofmann, Lucas Beyer, and Bastian Leibe. 2017. The atari grand challenge dataset. arXiv preprint
arXiv:1705.10998 (2017).

--- Page 27 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
27
[122] Jinxiang Lai, Jie Zhang, Jun Liu, Jian Li, Xiaocheng Lu, and Song Guo. 2024. Spider: Any-to-many multimodal llm. arXiv preprint arXiv:2411.09439
(2024).
[123] Yann LeCun. 2022. A path towards autonomous machine intelligence version 0.9. 2, 2022-06-27. Open Review 62, 1 (2022), 1–62.
[124] Lik-Hang Lee, Tristan Braud, Pengyuan Zhou, Lin Wang, Dianlei Xu, Zijun Lin, Abhishek Kumar, Carlos Bermejo, and Pan Hui. 2021. All One
Needs to Know about Metaverse: A Complete Survey on Technological Singularity, Virtual Ecosystem, and Research Agenda. ArXiv abs/2110.05352
(2021).
[125] Jie Lei, Liwei Wang, Yelong Shen, Dong Yu, Tamara L Berg, and Mohit Bansal. 2020. Mart: Memory-augmented recurrent transformer for coherent
video paragraph captioning. arXiv preprint arXiv:2005.05402 (2020).
[126] Rodrigo Lessa and João Araújo. 2017. World Consistency. In The Routledge Companion to Imaginary Worlds. Routledge, 90–97.
[127] Baiqi Li, Zhiqiu Lin, Deepak Pathak, Jiayao Li, Yixin Fei, Kewen Wu, Xide Xia, Pengchuan Zhang, Graham Neubig, and Deva Ramanan. 2024.
Evaluating and improving compositional text-to-visual generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition. 5290–5301.
[128] Chengxuan Li, Di Huang, Zeyu Lu, Yang Xiao, Qingqi Pei, and Lei Bai. 2024. A survey on long video generation: Challenges, methods, and
prospects. arXiv preprint arXiv:2403.16407 (2024).
[129] Chenxin Li, Hengyu Liu, Yifan Liu, Brandon Y Feng, Wuyang Li, Xinyu Liu, Zhen Chen, Jing Shao, and Yixuan Yuan. 2024. Endora: Video
generation models as endoscopy simulators. In International conference on medical image computing and computer-assisted intervention. Springer
Nature Switzerland Cham, 230–240.
[130] Chenyu Li, Oscar Michel, Xichen Pan, Sainan Liu, Mike Roberts, and Saining Xie. 2025. PISA experiments: Exploring physics post-training for
video diffusion models by watching stuff drop. arXiv preprint arXiv:2503.09595 (2025).
[131] Chenghao Li, Chaoning Zhang, Atish Waghwase, Lik-Hang Lee, Francois Rameau, Yang Yang, Sung-Ho Bae, and Choong Seon Hong. 2023.
Generative AI meets 3D: A Survey on Text-to-3D in AIGC Era. arXiv preprint arXiv:2305.06131 (2023).
[132] He Li, Ruihua Han, Zirui Zhao, Wei Xu, Qi Hao, Shuai Wang, and Chengzhong Xu. 2024. Seamless Virtual Reality With Integrated Synchronizer
and Synthesizer for Autonomous Driving. IEEE Robotics and Automation Letters (2024).
[133] Shufan Li, Konstantinos Kallidromitis, Akash Gokul, Zichun Liao, Yusuke Kato, Kazuki Kozuka, and Aditya Grover. 2025. Omniflow: Any-to-any
generation with multi-modal rectified flows. In Proceedings of the Computer Vision and Pattern Recognition Conference. 13178–13188.
[134] Xiaofan Li, Yifu Zhang, and Xiaoqing Ye. 2023. DrivingDiffusion: Layout-Guided multi-view driving scene video generation with latent diffusion
model. arXiv preprint arXiv:2310.07771 (2023).
[135] Yitong Li, Zhe Gan, Yelong Shen, Jingjing Liu, Yu Cheng, Yuexin Wu, Lawrence Carin, David Carlson, and Jianfeng Gao. 2019. Storygan: A
sequential conditional gan for story visualization. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 6329–6338.
[136] Yichen Li and Antonio Torralba. 2025. MultiModal Action Conditioned Video Simulation. In Proceedings of the IEEE/CVF International Conference
on Computer Vision. 14173–14183.
[137] Zhen Li, Chuanhao Li, Xiaofeng Mao, Shaoheng Lin, Ming Li, Shitian Zhao, Zhaopan Xu, Xinyue Li, Yukang Feng, Jianwen Sun, et al. 2025. Sekai:
A Video Dataset towards World Exploration. arXiv preprint arXiv:2506.15675 (2025).
[138] Zhaoyang Li, Dongjun Qian, Kai Su, Qishuai Diao, Xiangyang Xia, Chang Liu, Wenfei Yang, Tianzhu Zhang, and Zehuan Yuan. 2025. BindWeave:
Subject-Consistent Video Generation via Cross-Modal Integration. arXiv preprint arXiv:2510.00438 (2025).
[139] Zhaowei Li, Wei Wang, YiQing Cai, Qi Xu, Pengyu Wang, Dong Zhang, Hang Song, Botian Jiang, Zhida Huang, and Tao Wang. 2025. Unifiedmllm:
Enabling unified representation for multi-modal multi-tasks with large language model. In Findings of the Association for Computational Linguistics:
NAACL 2025. 334–344.
[140] Long Lian, Baifeng Shi, Adam Yala, Trevor Darrell, and Boyi Li. 2023. Llm-grounded video diffusion models. arXiv preprint arXiv:2309.17444 (2023).
[141] Junbang Liang, Ruoshi Liu, Ege Ozguroglu, Sruthi Sudhakar, Achal Dave, Pavel Tokmakov, Shuran Song, and Carl Vondrick. 2024. Dreamitate:
Real-world visuomotor policy learning via video generation. arXiv preprint arXiv:2406.16862 (2024).
[142] Junbang Liang, Pavel Tokmakov, Ruoshi Liu, Sruthi Sudhakar, Paarth Shah, Rares Ambrus, and Carl Vondrick. 2025. Video generators are robot
policies. arXiv preprint arXiv:2508.00795 (2025).
[143] Mingxiang Liao, Qixiang Ye, Wangmeng Zuo, Fang Wan, Tianyu Wang, Yuzhong Zhao, Jingdong Wang, Xinyu Zhang, et al. 2024. Evaluation of
text-to-video generation models: A dynamics perspective. Advances in Neural Information Processing Systems 37 (2024), 109790–109816.
[144] Yue Liao, Pengfei Zhou, Siyuan Huang, Donglin Yang, Shengcong Chen, Yuxin Jiang, Yue Hu, Jingbin Cai, Si Liu, Jianlan Luo, et al. 2025. Genie
envisioner: A unified world foundation platform for robotic manipulation. arXiv preprint arXiv:2508.05635 (2025).
[145] Minghui Lin, Xiang Wang, Yishan Wang, Shu Wang, Fengqi Dai, Pengxiang Ding, Cunxiang Wang, Zhengrong Zuo, Nong Sang, Siteng Huang,
et al. 2025. Exploring the evolution of physics cognition in video generation: A survey. arXiv preprint arXiv:2503.21765 (2025).
[146] Zhiqiu Lin, Deepak Pathak, Baiqi Li, Jiayao Li, Xide Xia, Graham Neubig, Pengchuan Zhang, and Deva Ramanan. 2024. Evaluating text-to-visual
generation with image-to-text generation. In European Conference on Computer Vision. Springer Nature Switzerland Cham, 366–384.
[147] Xinran Ling, Chen Zhu, Meiqi Wu, Hangyu Li, Xiaokun Feng, Cundian Yang, Aiming Hao, Jiashu Zhu, Jiahong Wu, and Xiangxiang Chu. 2025.
Vmbench: A benchmark for perception-aligned video motion generation. In Proceedings of the IEEE/CVF International Conference on Computer
Vision. 13087–13098.
[148] Akide Liu, Hanwen Wang, and Mong Yuan Sim. 2024. Personalised Video Generation: Temporal Diffusion Synthesis With Generative Large
Language Model. arXiv preprint (2024).

--- Page 28 ---

28
Puspitasari et al.
[149] Binhui Liu, Xin Liu, Anbo Dai, Zhiyong Zeng, Dan Wang, Zhen Cui, and Jian Yang. 2023. Dual-stream diffusion net for text-to-video generation.
arXiv preprint arXiv:2308.08316 (2023).
[150] Feng-Lin Liu, Hongbo Fu, Xintao Wang, Weicai Ye, Pengfei Wan, Di Zhang, and Lin Gao. 2025. SketchVideo: Sketch-based Video Generation and
Editing. In Proceedings of the Computer Vision and Pattern Recognition Conference. 23379–23390.
[151] Huijie Liu, Jingyun Wang, Shuai Ma, Jie Hu, Xiaoming Wei, and Guoliang Kang. 2025. Separate motion from appearance: Customizing motion via
customizing text-to-video diffusion models. In Proceedings of the 33rd ACM International Conference on Multimedia. 9227–9236.
[152] Jie Liu, Gongye Liu, Jiajun Liang, Ziyang Yuan, Xiaokun Liu, Mingwu Zheng, Xiele Wu, Qiulin Wang, Menghan Xia, Xintao Wang, et al. 2025.
Improving video generation with human feedback. arXiv preprint arXiv:2501.13918 (2025).
[153] Shaowei Liu, Zhongzheng Ren, Saurabh Gupta, and Shenlong Wang. 2024. Physgen: Rigid-body physics-grounded image-to-video generation. In
European Conference on Computer Vision. Springer, 360–378.
[154] Xinxin Liu, Zhaopan Xu, Kai Wang, Yong Jae Lee, and Yuzhang Shang. 2025. Can World Simulators Reason? Gen-ViRe: A Generative Visual
Reasoning Benchmark. arXiv preprint arXiv:2511.13853 (2025).
[155] Yaofang Liu, Xiaodong Cun, Xuebo Liu, Xintao Wang, Yong Zhang, Haoxin Chen, Yang Liu, Tieyong Zeng, Raymond Chan, and Ying Shan. 2024.
Evalcrafter: Benchmarking and evaluating large video generation models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition. 22139–22149.
[156] Yuanxin Liu, Lei Li, Shuhuai Ren, Rundong Gao, Shicheng Li, Sishuo Chen, Xu Sun, and Lu Hou. 2023. Fetv: A benchmark for fine-grained
evaluation of open-domain text-to-video generation. Advances in Neural Information Processing Systems 36 (2023), 62352–62387.
[157] Yanchen Liu, Yanan Sun, Zhening Xing, Junyao Gao, Kai Chen, and Wenjie Pei. 2025. MotionShot: Adaptive Motion Transfer across Arbitrary
Objects for Text-to-Video Generation. In Proceedings of the IEEE/CVF International Conference on Computer Vision. 11861–11871.
[158] Yixin Liu, Kai Zhang, Yuan Li, Zhiling Yan, Chujie Gao, Ruoxi Chen, Zhengqing Yuan, Yue Huang, Hanchi Sun, Jianfeng Gao, et al. 2024. Sora: A
Review on Background, Technology, Limitations, and Opportunities of Large Vision Models. arXiv preprint arXiv:2402.17177 (2024).
[159] Zuhao Liu, Aleksandar Yanev, Ahmad Mahmood, Ivan Nikolov, Saman Motamed, Wei-Shi Zheng, Xi Wang, Luc Van Gool, and Danda Pani Paudel.
2024. InTraGen: Trajectory-controlled video generation for object interactions. arXiv preprint arXiv:2411.16804 (2024).
[160] Brian CS Loh and Patrick HH Then. 2013. Cardiac echo to text conversion: Closing the urban-rural connectivity gap. In 2013 9th International
Conference on Information, Communications & Signal Processing. IEEE, 1–4.
[161] Fuchen Long, Zhaofan Qiu, Ting Yao, and Tao Mei. 2024. VideoDrafter: Content-Consistent Multi-Scene Video Generation with LLM. arXiv
preprint arXiv:2401.01256 (2024).
[162] Fuchen Long, Zhaofan Qiu, Ting Yao, and Tao Mei. 2024. Videostudio: Generating consistent-content and multi-scene videos. In European
Conference on Computer Vision. Springer, 468–485.
[163] Jiachen Lu, Ze Huang, Zeyu Yang, Jiahui Zhang, and Li Zhang. 2024. Wovogen: World volume-aware diffusion for controllable multi-camera
driving scene generation. In European Conference on Computer Vision. Springer, 329–345.
[164] Yu Lu, Yuanzhi Liang, Linchao Zhu, and Yi Yang. 2024. Freelong: Training-free long video generation with spectralblend temporal attention.
Advances in Neural Information Processing Systems 37 (2024), 131434–131455.
[165] Yifan Lu, Xuanchi Ren, Jiawei Yang, Tianchang Shen, Zhangjie Wu, Jun Gao, Yue Wang, Siheng Chen, Mike Chen, Sanja Fidler, et al. 2025.
Infinicube: Unbounded and controllable dynamic 3d driving scene generation with world-guided video models. In Proceedings of the IEEE/CVF
International Conference on Computer Vision. 27272–27283.
[166] Yu Lu, Linchao Zhu, Hehe Fan, and Yi Yang. 2023. FlowZero: Zero-Shot Text-to-Video Synthesis with LLM-Driven Dynamic Scene Syntax. arXiv
preprint arXiv:2311.15813 (2023).
[167] Luma. 2024. Dream Machine. https://lumalabs.ai/dream-machine
[168] Yang Luo, Xuanlei Zhao, Baijiong Lin, Lingting Zhu, Liyao Tang, Yuqi Liu, Ying-Cong Chen, Shengju Qian, Xin Wang, and Yang You. 2025.
V-ReasonBench: Toward Unified Reasoning Benchmark Suite for Video Generation Models. arXiv preprint arXiv:2511.16668 (2025).
[169] Jiaxi Lv, Yi Huang, Mingfu Yan, Jiancheng Huang, Jianzhuang Liu, Yifan Liu, Yafei Wen, Xiaoxin Chen, and Shifeng Chen. 2023. GPT4Motion:
Scripting Physical Motions in Text-to-Video Generation via Blender-Oriented GPT Planning. arXiv preprint arXiv:2311.12631 (2023).
[170] Zhengyao Lv, Chenyang Si, Tianlin Pan, Zhaoxi Chen, Kwan-Yee K Wong, Yu Qiao, and Ziwei Liu. 2025. Dual-Expert Consistency Model for
Efficient and High-Quality Video Generation. In Proceedings of the IEEE/CVF International Conference on Computer Vision. 14983–14993.
[171] Lingjuan Lyu, C Chen, and J Fu. 2023. A pathway towards responsible AI generated content. In Proc. 2nd tnt’I. Joint Conf. Artificial Intelligence.
[172] Yuanhuiyi Lyu, Xu Zheng, Dahun Kim, and Lin Wang. 2024. Omnibind: Teach to build unequal-scale modality interaction for omni-bind of all.
arXiv preprint arXiv:2405.16108 (2024).
[173] Nanye Ma, Mark Goldstein, Michael S Albergo, Nicholas M Boffi, Eric Vanden-Eijnden, and Saining Xie. 2024. Sit: Exploring flow and diffusion-based
generative models with scalable interpolant transformers. In European Conference on Computer Vision. Springer, 23–40.
[174] Shijie Ma, Huayi Xu, Mengjian Li, Weidong Geng, Yaxiong Wang, and Meng Wang. 2023. POS: A prompts optimization suite for augmenting
text-to-video generation. arXiv preprint arXiv:2311.00949 (2023).
[175] Xin Ma, Yaohui Wang, Gengyun Jia, Xinyuan Chen, Ziwei Liu, Yuan-Fang Li, Cunjian Chen, and Yu Qiao. 2024. Latte: Latent diffusion transformer
for video generation. arXiv preprint arXiv:2401.03048 (2024).
[176] Jianbiao Mei, Tao Hu, Xuemeng Yang, Licheng Wen, Yu Yang, Tiantian Wei, Yukai Ma, Min Dou, Botian Shi, and Yong Liu. 2024. Dreamforge:
Motion-aware autoregressive video generation for multi-view driving scenes. arXiv preprint arXiv:2409.04003 (2024).

--- Page 29 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
29
[177] Willi Menapace, Aliaksandr Siarohin, Ivan Skorokhodov, Ekaterina Deyneka, Tsai-Shien Chen, Anil Kag, Yuwei Fang, Aleksei Stoliar, Elisa Ricci,
Jian Ren, et al. 2024. Snap video: Scaled spatiotemporal transformers for text-to-video synthesis. In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition. 7038–7048.
[178] Fanqing Meng, Jiaqi Liao, Xinyu Tan, Wenqi Shao, Quanfeng Lu, Kaipeng Zhang, Yu Cheng, Dianqi Li, Yu Qiao, and Ping Luo. 2024. Towards
world simulator: Crafting physical commonsense-based benchmark for video generation. arXiv preprint arXiv:2410.05363 (2024).
[179] Yibo Miao, Yifan Zhu, Lijia Yu, Jun Zhu, Xiao-Shan Gao, and Yinpeng Dong. 2024. T2vsafetybench: Evaluating the safety of text-to-video generative
models. Advances in Neural Information Processing Systems 37 (2024), 63858–63872.
[180] Daniele Molino, Francesco di Feola, Linlin Shen, Paolo Soda, and Valerio Guarrasi. 2025. Any-to-Any Vision-Language Model for Multimodal
X-ray Imaging and Radiological Report Generation. arXiv preprint arXiv:2505.01091 (2025).
[181] Antonio Montanaro, Luca Savant Aira, Emanuele Aiello, Diego Valsesia, and Enrico Magli. 2024. Motioncraft: Physics-based zero-shot video
generation. Advances in Neural Information Processing Systems 37 (2024), 123155–123181.
[182] Meredith Ringel Morris. 2025. HCI for AGI. Interactions 32, 2 (2025), 26–32.
[183] Saman Motamed, Laura Culp, Kevin Swersky, Priyank Jaini, and Robert Geirhos. 2025. Do generative video models understand physical principles?
arXiv preprint arXiv:2501.09038 (2025).
[184] Arian Mousakhan, Sudhanshu Mittal, Silvio Galesso, Karim Farid, and Thomas Brox. 2025. Orbis: Overcoming challenges of long-horizon prediction
in driving world models. arXiv preprint arXiv:2507.13162 (2025).
[185] Hyelin Nam, Hyojun Go, Byeongjun Park, Byung-Hoon Kim, and Hyungjin Chung. 2025. Generating Human Motion Videos using a Cascaded
Text-to-Video Framework. arXiv preprint arXiv:2510.03909 (2025).
[186] Viknashvaran Narayanasamy, Kok Wai Wong, Chun Che Fung, and Arnold Depickere. 2005. Distinguishing simulation games from simulators by
considering design characteristics. In Second Australasian Conference on Interactive Entertainment. Creativity & Cognition Studios Press.
[187] Haomiao Ni, Bernhard Egger, Suhas Lohit, Anoop Cherian, Ye Wang, Toshiaki Koike-Akino, Sharon X Huang, and Tim K Marks. 2024. Ti2v-zero:
Zero-shot image conditioning for text-to-video diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition.
9015–9025.
[188] Massimiliano Oliveri, Giacomo Koch, and Carlo Caltagirone. 2009. Spatial–temporal interactions in the human brain. Experimental Brain Research
195, 4 (2009), 489–497.
[189] OpenAI. 2025. Sora 2 is here. https://openai.com/index/sora-2/
[190] Abby O’Neill, Abdul Rehman, Abhiram Maddukuri, Abhishek Gupta, Abhishek Padalkar, Abraham Lee, Acorn Pooley, Agrim Gupta, Ajay
Mandlekar, Ajinkya Jain, et al. 2024. Open x-embodiment: Robotic learning datasets and rt-x models: Open x-embodiment collaboration 0. In 2024
IEEE International Conference on Robotics and Automation (ICRA). IEEE, 6892–6903.
[191] Matthew J Page, Joanne E McKenzie, Patrick M Bossuyt, Isabelle Boutron, Tammy C Hoffmann, Cynthia D Mulrow, Larissa Shamseer, Jennifer M
Tetzlaff, Elie A Akl, Sue E Brennan, et al. 2021. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. Bmj 372
(2021).
[192] Dong Huk Park, Samaneh Azadi, Xihui Liu, Trevor Darrell, and Anna Rohrbach. 2021. Benchmark for compositional text-to-image synthesis. In
Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 1).
[193] Piyushkumar Patel. 2025. AI Powered High Quality Text to Video Generation with Enhanced Temporal Consistency. arXiv preprint arXiv:2511.00107
(2025).
[194] William Peebles and Saining Xie. 2023. Scalable diffusion models with transformers. In Proceedings of the IEEE/CVF international conference on
computer vision. 4195–4205.
[195] Ryan Po, Yotam Nitzan, Richard Zhang, Berlin Chen, Tri Dao, Eli Shechtman, Gordon Wetzstein, and Xun Huang. 2025. Long-context state-space
video world models. arXiv preprint arXiv:2505.20171 (2025).
[196] Zelu Qi, Ping Shi, Shuqi Wang, Chaoyang Zhang, Fei Zhao, Zefeng Ying, Da Pan, Xi Yang, Zheqi He, and Teng Dai. 2025. T2VEval: Benchmark
Dataset and Objective Evaluation Method for T2V-generated Videos. arXiv preprint arXiv:2501.08545 (2025).
[197] Wenxu Qian, Chaoyue Wang, Hou Peng, Zhiyu Tan, Hao Li, and Anxiang Zeng. 2025. RDPO: Real Data Preference Optimization for Physics
Consistency Video Generation. arXiv preprint arXiv:2506.18655 (2025).
[198] Yiran Qin, Zhelun Shi, Jiwen Yu, Xijun Wang, Enshen Zhou, Lijun Li, Zhenfei Yin, Xihui Liu, Lu Sheng, Jing Shao, et al. 2024. Worldsimbench:
Towards video generation models as world simulators. arXiv preprint arXiv:2410.18072 (2024).
[199] Zhiwu Qing, Shiwei Zhang, Jiayu Wang, Xiang Wang, Yujie Wei, Yingya Zhang, Changxin Gao, and Nong Sang. 2024. Hierarchical spatio-temporal
decoupling for text-to-video generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 6635–6645.
[200] Junxiang Qiu, Jinda Lu, and Shuo Wang. 2025. Multimodal Generation with Consistency Transferring. In Findings of the Association for Computational
Linguistics: NAACL 2025. 504–513.
[201] Junxiang Qiu, Shuo Wang, Jinda Lu, Lin Liu, Houcheng Jiang, Xingyu Zhu, and Yanbin Hao. 2025. Accelerating diffusion transformer via
error-optimized cache. In Proceedings of the 33rd ACM International Conference on Multimedia. 9588–9597.
[202] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin,
Jack Clark, Gretchen Krueger, and Ilya Sutskever. 2021. Learning Transferable Visual Models From Natural Language Supervision.
https:
//doi.org/10.48550/arXiv.2103.00020 arXiv:2103.00020 [cs.CV]

--- Page 30 ---

30
Puspitasari et al.
[203] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. 2023. Direct preference optimization:
Your language model is secretly a reward model. Advances in Neural Information Processing Systems 36 (2023), 53728–53741.
[204] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. 2020. Exploring
the limits of transfer learning with a unified text-to-text transformer. The Journal of Machine Learning Research 21, 1 (2020), 5485–5551.
[205] Aimon Rahman, Jiang Liu, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Yusheng Su, Vishal M Patel, Zicheng Liu, and Emad Barsoum. 2025.
MOVi: Training-free Text-conditioned Multi-Object Video Generation. arXiv preprint arXiv:2505.22980 (2025).
[206] Gaurav Rai and Ojaswa Sharma. 2024. Enhancing sketch animation: Text-to-video diffusion models with temporal consistency and rigidity
constraints. arXiv preprint arXiv:2411.19381 (2024).
[207] Vipula Rawte, Sarthak Jain, Aarush Sinha, Garv Kaushik, Aman Bansal, Prathiksha Rumale Vishwanath, Samyak Rajesh Jain, Aishwarya Naresh
Reganti, Vinija Jain, Aman Chadha, et al. 2025. Vibe: A text-to-video benchmark for evaluating hallucination in large multimodal models. In
Proceedings of the 5th Workshop on Trustworthy NLP (TrustNLP 2025). 232–246.
[208] Weiming Ren, Huan Yang, Ge Zhang, Cong Wei, Xinrun Du, Wenhao Huang, and Wenhu Chen. 2024. Consisti2v: Enhancing visual consistency for
image-to-video generation. arXiv preprint arXiv:2402.04324 (2024).
[209] Xuanchi Ren, Tianchang Shen, Jiahui Huang, Huan Ling, Yifan Lu, Merlin Nimier-David, Thomas Müller, Alexander Keller, Sanja Fidler, and Jun
Gao. 2025. Gen3c: 3d-informed world-consistent video generation with precise camera control. In Proceedings of the Computer Vision and Pattern
Recognition Conference. 6121–6132.
[210] Zhongwei Ren, Yunchao Wei, Xun Guo, Yao Zhao, Bingyi Kang, Jiashi Feng, and Xiaojie Jin. 2025. Videoworld: Exploring knowledge learning from
unlabeled videos. In Proceedings of the Computer Vision and Pattern Recognition Conference. 29029–29039.
[211] Marc Rigter, Tarun Gupta, Agrin Hilmkil, and Chao Ma. 2024. Avid: Adapting video diffusion models to world models. arXiv preprint arXiv:2410.12822
(2024).
[212] Gustavo Rohenkohl, Ian C Gould, Jéssica Pessoa, and Anna C Nobre. 2014. Combining spatial and temporal expectations to improve visual
perception. Journal of vision 14, 4 (2014), 8–8.
[213] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. 2022. High-resolution image synthesis with latent diffusion
models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 10684–10695.
[214] Seth Rudy. 2014. Introduction: Concepts of Completeness. In Literature and Encyclopedism in Enlightenment Britain: The Pursuit of Complete
Knowledge. Springer, 1–17.
[215] Runway. 2023. Gen-2: Generate novel videos with text, images or video clips. https://runwayml.com/research/gen-2
[216] Runway. 2024. Introducing Gen-3 Alpha: A New Frontier for Video Generation. https://runwayml.com/research/introducing-gen-3-alpha
[217] Runway. 2025. Introducing Runway Gen-4.5. https://runwayml.com/research/introducing-runway-gen-4.5
[218] Ketan Suhaas Saichandran, Xavier Thomas, Prakhar Kaushik, and Deepti Ghadiyaram. 2025. Progressive Prompt Detailing for Improved Alignment
in Text-to-Image Generative Models. arXiv preprint arXiv:2503.17794 (2025).
[219] Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen. 2016. Improved techniques for training gans.
Advances in neural information processing systems 29 (2016).
[220] Malik Sallam, Amwaj Al-Farajat, and Jan Egger. 2024. Envisioning the Future of ChatGPT in Healthcare: Insights and Recommendations from a
Systematic Identification of Influential Research and a Call for Papers. Jordan Medical Journal 58, 1 (2024).
[221] Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton
Mullis, Mitchell Wortsman, et al. 2022. Laion-5b: An open large-scale dataset for training next generation image-text models. Advances in Neural
Information Processing Systems 35 (2022), 25278–25294.
[222] Christoph Schuhmann, Richard Vencu, Romain Beaumont, Robert Kaczmarczyk, Clayton Mullis, Aarush Katta, Theo Coombes, Jenia Jitsev, and
Aran Komatsuzaki. 2021. Laion-400m: Open dataset of clip-filtered 400 million image-text pairs. arXiv preprint arXiv:2111.02114 (2021).
[223] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. 2017. Proximal policy optimization algorithms. arXiv preprint
arXiv:1707.06347 (2017).
[224] Ruizhi Shao, Youxin Pang, Zerong Zheng, Jingxiang Sun, and Yebin Liu. 2024. 360-degree human video generation with 4d diffusion transformer.
ACM Transactions on Graphics (TOG) 43, 6 (2024), 1–13.
[225] SP Sharan, Minkyu Choi, Sahil Shah, Harsh Goel, Mohammad Omama, and Sandeep Chinchali. 2025. Neuro-symbolic evaluation of text-to-video
models using formal verification. In Proceedings of the Computer Vision and Pattern Recognition Conference. 8395–8405.
[226] Mingzhu Shen, Pengtao Chen, Peng Ye, Guoxuan Xia, Tao Chen, Christos-Savvas Bouganis, and Yiren Zhao. 2024. MD-DiT: Step-aware Mixture-
of-Depths for Efficient Diffusion Transformers. In Adaptive Foundation Models: Evolving AI for Personalized and Efficient Learning.
[227] Uriel Singer, Adam Polyak, Thomas Hayes, Xi Yin, Jie An, Songyang Zhang, Qiyuan Hu, Harry Yang, Oron Ashual, Oran Gafni, et al. 2022.
Make-a-video: Text-to-video generation without text-video data. arXiv preprint arXiv:2209.14792 (2022).
[228] Aditi Singh. 2023. A Survey of AI Text-to-Image and AI Text-to-Video Generators. In 2023 4th International Conference on Artificial Intelligence,
Robotics and Control (AIRC). IEEE, 32–36.
[229] Yang Song and Prafulla Dhariwal. 2023. Improved techniques for training consistency models. arXiv preprint arXiv:2310.14189 (2023).
[230] Yang Song, Prafulla Dhariwal, Mark Chen, and Ilya Sutskever. 2023. Consistency models. arXiv preprint arXiv:2303.01469 (2023).
[231] Achint Soni, Sreyas Venkataraman, Abhranil Chandra, Sebastian Fischmeister, Percy Liang, Bo Dai, and Sherry Yang. 2025. VideoAgent: Self-
Improving Video Generation for Embodied Planning. In Workshop on Reinforcement Learning Beyond Rewards@ Reinforcement Learning Conference

--- Page 31 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
31
2025.
[232] Sumedh Sontakke, Jesse Zhang, Séb Arnold, Karl Pertsch, Erdem Bıyık, Dorsa Sadigh, Chelsea Finn, and Laurent Itti. 2024. Roboclip: One
demonstration is enough to learn robot policies. Advances in Neural Information Processing Systems 36 (2024).
[233] Nitish Srivastava, Elman Mansimov, and Ruslan Salakhutdinov. 2015. Unsupervised Learning of Video Representations using LSTMs. CoRR
abs/1502.04681 (2015). arXiv:1502.04681
[234] Sitong Su, Litao Guo, Lianli Gao, Hengtao Shen, and Jingkuan Song. 2023. Motionzero: Exploiting motion priors for zero-shot text-to-video
generation. arXiv preprint arXiv:2311.16635 (2023).
[235] Tongtong Su, Chengyu Wang, Bingyan Liu, Jun Huang, and Dongming Lu. 2025. Encapsulated Composition of Text-to-Image and Text-to-Video
Models for High-Quality Video Synthesis. In Proceedings of the Computer Vision and Pattern Recognition Conference. 18209–18218.
[236] Kaiyue Sun, Kaiyi Huang, Xian Liu, Yue Wu, Zihan Xu, Zhenguo Li, and Xihui Liu. 2025. T2v-compbench: A comprehensive benchmark for
compositional text-to-video generation. In Proceedings of the Computer Vision and Pattern Recognition Conference. 8406–8416.
[237] Rui Sun, Yumin Zhang, Tejal Shah, Jiaohao Sun, Shuoying Zhang, Wenqi Li, Haoran Duan, and Bo Wei. 2024. From Sora What We Can See: A
Survey of Text-to-Video Generation. (2024).
[238] J. Suomala and J. Kauttonen. 2022. Human’s Intuitive Mental Models as a Source of Realistic Artificial Intelligence and Engineering. Frontiers in
Psychology (2022).
[239] Richard S Sutton, Andrew G Barto, et al. 1998. Reinforcement learning: An introduction. Vol. 1. MIT press Cambridge.
[240] Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, and Andrew
Rabinovich. 2015. Going deeper with convolutions. In Proceedings of the IEEE conference on computer vision and pattern recognition. 1–9.
[241] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon Shlens, and Zbigniew Wojna. 2016. Rethinking the inception architecture for computer
vision. In Proceedings of the IEEE conference on computer vision and pattern recognition. 2818–2826.
[242] Zineng Tang, Ziyi Yang, Mahmoud Khademi, Yang Liu, Chenguang Zhu, and Mohit Bansal. 2024. Codi-2: In-context interleaved and interactive
any-to-any generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 27425–27434.
[243] Zineng Tang, Ziyi Yang, Chenguang Zhu, Michael Zeng, and Mohit Bansal. 2024. Any-to-any generation via composable diffusion. Advances in
Neural Information Processing Systems 36 (2024).
[244] Genmo Team. 2024. Mochi 1. https://github.com/genmoai/models
[245] Andy Thomas. 2024. Sora the future of filmmaking. https://techduffer.com/sora-the-future-of-filmmaking/
[246] Ye Tian, Ling Yang, Haotian Yang, Yuan Gao, Yufan Deng, Jingmin Chen, Xintao Wang, Zhaochen Yu, Xin Tao, Pengfei Wan, et al. 2024. Videotetris:
Towards compositional text-to-video generation. Advances in Neural Information Processing Systems 37 (2024), 29489–29513.
[247] Wei-Cheng Tseng, Jinwei Gu, Qinsheng Zhang, Hanzi Mao, Ming-Yu Liu, Florian Shkurti, and Lin Yen-Chen. 2025. Scalable Policy Evaluation with
Video World Models. arXiv preprint arXiv:2511.11520 (2025).
[248] Thomas Unterthiner, Sjoerd van Steenkiste, Karol Kurach, Raphaël Marinier, Marcin Michalski, and Sylvain Gelly. 2018. Towards Accurate Generative
Models of Video: A New Metric & Challenges. Technical Report.
[249] Dani Valevski, Yaniv Leviathan, Moab Arar, and Shlomi Fruchter. 2024. Diffusion models are real-time game engines. arXiv preprint arXiv:2408.14837
(2024).
[250] Ruben Villegas, Mohammad Babaeizadeh, Pieter-Jan Kindermans, Hernan Moraldo, Han Zhang, Mohammad Taghi Saffar, Santiago Castro, Julius
Kunze, and Dumitru Erhan. 2022. Phenaki: Variable length video generation from open domain textual description. arXiv preprint arXiv:2210.02399
(2022).
[251] Dimitri Von Rütte, Elisabetta Fedele, Jonathan Thomm, and Lukas Wolf. 2024. Fabric: Personalizing diffusion models with iterative feedback. In
European Conference on Computer Vision. Springer, 385–400.
[252] Sasha Wallinger. 2024. How openai’s sora impacts the future of Music Marketing. https://www.forbes.com/sites/sashawallinger/2024/02/17/how-
openais-sora-impacts-the-future-of-music-marketing/?sh=28ead1e94831
[253] Team Wan, Ang Wang, Baole Ai, Bin Wen, Chaojie Mao, Chen-Wei Xie, Di Chen, Feiwu Yu, Haiming Zhao, Jianxiao Yang, et al. 2025. Wan: Open
and advanced large-scale video generative models. arXiv preprint arXiv:2503.20314 (2025).
[254] Chen Wang, Chuhao Chen, Yiming Huang, Zhiyang Dou, Yuan Liu, Jiatao Gu, and Lingjie Liu. 2025. Physctrl: Generative physics for controllable
and physics-grounded video generation. arXiv preprint arXiv:2509.20358 (2025).
[255] Fu-Yun Wang, Zhaoyang Huang, Xiaoyu Shi, Weikang Bian, Guanglu Song, Yu Liu, and Hongsheng Li. 2024. AnimateLCM: Accelerating the
Animation of Personalized Diffusion Models and Adapters with Decoupled Consistency Learning. arXiv preprint arXiv:2402.00769 (2024).
[256] Jing Wang, Ao Ma, Ke Cao, Jun Zheng, Zhanjie Zhang, Jiasong Feng, Shanyuan Liu, Yuhang Ma, Bo Cheng, Dawei Leng, et al. 2025. Wisa: World
simulator assistant for physics-aware text-to-video generation. arXiv preprint arXiv:2503.08153 (2025).
[257] Kai Wang, Mingjia Shi, Yukun Zhou, Zekai Li, Zhihang Yuan, Yuzhang Shang, Xiaojiang Peng, Hanwang Zhang, and Yang You. 2025. A closer look
at time steps is worthy of triple speed-up for diffusion model training. In Proceedings of the Computer Vision and Pattern Recognition Conference.
12934–12944.
[258] Lening Wang, Wenzhao Zheng, Yilong Ren, Han Jiang, Zhiyong Cui, Haiyang Yu, and Jiwen Lu. 2024. Occsora: 4d occupancy generation models as
world simulators for autonomous driving. arXiv preprint arXiv:2405.20337 (2024).
[259] Peiyao Wang, Weining Wang, and Qi Li. 2025. PhysCorr: Dual-Reward DPO for Physics-Constrained Text-to-Video Generation with Automated
Preference Selection. arXiv preprint arXiv:2511.03997 (2025).

--- Page 32 ---

32
Puspitasari et al.
[260] Qinghe Wang, Yawen Luo, Xiaoyu Shi, Xu Jia, Huchuan Lu, Tianfan Xue, Xintao Wang, Pengfei Wan, Di Zhang, and Kun Gai. 2025. Cinemaster: A
3d-aware and controllable framework for cinematic text-to-video generation. In Proceedings of the Special Interest Group on Computer Graphics and
Interactive Techniques Conference Conference Papers. 1–10.
[261] Wenhao Wang and Yi Yang. 2024. Vidprom: A million-scale real prompt-gallery dataset for text-to-video diffusion models. Advances in Neural
Information Processing Systems 37 (2024), 65618–65642.
[262] Wen Wang, Kecheng Zheng, Qiuyu Wang, Hao Chen, Zifan Shi, Ceyuan Yang, Yujun Shen, and Chunhua Shen. 2023. Gendef: Learning generative
deformation field for video generation. arXiv preprint arXiv:2312.04561 (2023).
[263] Xian Wang, Lik-Hang Lee, Carlos Bermejo Fernández, and Pan Hui. 2023. The Dark Side of Augmented Reality: Exploring Manipulative Designs in
AR. ArXiv abs/2303.02843 (2023).
[264] Xingrui Wang, Xin Li, Yaosi Hu, Hanxin Zhu, Chen Hou, Cuiling Lan, and Zhibo Chen. 2025. Tiv-diffusion: Towards object-centric movement for
text-driven image to video generation. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 39. 7988–7996.
[265] Xiaofeng Wang, Zheng Zhu, Guan Huang, Xinze Chen, and Jiwen Lu. 2023. Drivedreamer: Towards real-world-driven world models for autonomous
driving. arXiv preprint arXiv:2309.09777 (2023).
[266] Xiaofeng Wang, Zheng Zhu, Guan Huang, Boyuan Wang, Xinze Chen, and Jiwen Lu. 2024. WorldDreamer: Towards General World Models for
Video Generation via Predicting Masked Tokens. arXiv preprint arXiv:2401.09985 (2024).
[267] Xinyu Wang, Bohan Zhuang, and Qi Wu. 2024. Modaverse: Efficiently transforming modalities with llms. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition. 26606–26616.
[268] Yaohui Wang, Xinyuan Chen, Xin Ma, Shangchen Zhou, Ziqi Huang, Yi Wang, Ceyuan Yang, Yinan He, Jiashuo Yu, Peiqing Yang, et al. 2023. Lavie:
High-quality video generation with cascaded latent diffusion models. arXiv preprint arXiv:2309.15103 (2023).
[269] Yiping Wang, Xuehai He, Kuan Wang, Luyao Ma, Jianwei Yang, Shuohang Wang, Simon Shaolei Du, and Yelong Shen. 2025. Is your world simulator
a good story presenter? a consecutive events-based benchmark for future long video generation. In Proceedings of the Computer Vision and Pattern
Recognition Conference. 13629–13638.
[270] Yuji Wang, Moran Li, Xiaobin Hu, Ran Yi, Jiangning Zhang, Han Feng, Weijian Cao, Yabiao Wang, Chengjie Wang, and Lizhuang Ma. 2025.
Identity-preserving text-to-video generation guided by simple yet effective spatial-temporal decoupled representations. In Proceedings of the 33rd
ACM International Conference on Multimedia. 13743–13750.
[271] Yibin Wang, Zhiyu Tan, Junyan Wang, Xiaomeng Yang, Cheng Jin, and Hao Li. 2024. Lift: Leveraging human feedback for text-to-video model
alignment. arXiv preprint arXiv:2412.04814 (2024).
[272] Yuang Wang, Chao Wen, Haoyu Guo, Sida Peng, Minghan Qin, Hujun Bao, Xiaowei Zhou, and Ruizhen Hu. 2025. Precise action-to-video generation
through visual action prompts. In Proceedings of the IEEE/CVF International Conference on Computer Vision. 12713–12724.
[273] Zhao Wang, Aoxue Li, Lingting Zhu, Yong Guo, Qi Dou, and Zhenguo Li. 2024. Customvideo: Customizing text-to-video generation with multiple
subjects. arXiv preprint arXiv:2401.09962 (2024).
[274] Zeqing Wang, Xinyu Wei, Bairui Li, Zhen Guo, Jinrui Zhang, Hongyang Wei, Keze Wang, and Lei Zhang. 2025. VideoVerse: How Far is Your T2V
Generator from a World Model? arXiv preprint arXiv:2510.08398 (2025).
[275] Zehan Wang, Ziang Zhang, Xize Cheng, Rongjie Huang, Luping Liu, Zhenhui Ye, Haifeng Huang, Yang Zhao, Tao Jin, Peng Gao, et al. 2024.
Freebind: Free lunch in unified multimodal space via knowledge fusion. arXiv preprint arXiv:2405.04883 (2024).
[276] Zehan Wang, Ziang Zhang, Hang Zhang, Luping Liu, Rongjie Huang, Xize Cheng, Hengshuang Zhao, and Zhou Zhao. 2024. Omnibind: Large-scale
omni multimodal representation via binding spaces. arXiv preprint arXiv:2407.11895 (2024).
[277] Faraz Waseem and Muhammad Shahzad. 2025. Video is worth a thousand images: Exploring the latest trends in long video generation. Comput.
Surveys 58, 6 (2025), 1–35.
[278] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022. Chain-of-thought prompting
elicits reasoning in large language models. Advances in neural information processing systems 35 (2022), 24824–24837.
[279] Yunge Wen. 2025. “See What I Imagine, Imagine What I See”: Human-AI Co-Creation System for 360◦Panoramic Video Generation in VR. arXiv
preprint arXiv:2501.15456 (2025).
[280] Yuqing Wen, Yucheng Zhao, Yingfei Liu, Fan Jia, Yanhui Wang, Chong Luo, Chi Zhang, Tiancai Wang, Xiaoyan Sun, and Xiangyu Zhang. 2023.
Panacea: Panoramic and Controllable Video Generation for Autonomous Driving. arXiv preprint arXiv:2311.16813 (2023).
[281] Wenming Weng, Ruoyu Feng, Yanhui Wang, Qi Dai, Chunyu Wang, Dacheng Yin, Zhiyuan Zhao, Kai Qiu, Jianmin Bao, Yuhui Yuan, et al. 2024.
Art-v: Auto-regressive text-to-video generation with diffusion models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition. 7395–7405.
[282] Mark JP Wolf. 2014. Building imaginary worlds: The theory and history of subcreation. Routledge.
[283] Chenfei Wu, Lun Huang, Qianxi Zhang, Binyang Li, Lei Ji, Fan Yang, Guillermo Sapiro, and Nan Duan. 2021. Godiva: Generating open-domain
videos from natural descriptions. arXiv preprint arXiv:2104.14806 (2021).
[284] Hongtao Wu, Ya Jing, Chilam Cheang, Guangzeng Chen, Jiafeng Xu, Xinghang Li, Minghuan Liu, Hang Li, and Tao Kong. 2023. Unleashing
Large-Scale Video Generative Pre-training for Visual Robot Manipulation. arXiv preprint arXiv:2312.13139 (2023).
[285] Haoyu Wu, Diankun Wu, Tianyu He, Junliang Guo, Yang Ye, Yueqi Duan, and Jiang Bian. 2025. Geometry forcing: Marrying video diffusion and
3d representation for consistent world modeling. arXiv preprint arXiv:2507.07982 (2025).

--- Page 33 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
33
[286] Jianzong Wu, Xiangtai Li, Yanhong Zeng, Jiangning Zhang, Qianyu Zhou, Yining Li, Yunhai Tong, and Kai Chen. 2024. Motionbooth: Motion-aware
customized text-to-video generation. Advances in Neural Information Processing Systems 37 (2024), 34322–34348.
[287] Jialong Wu, Shaofeng Yin, Ningya Feng, Xu He, Dong Li, Jianye Hao, and Mingsheng Long. 2024. ivideogpt: Interactive videogpts are scalable
world models. Advances in Neural Information Processing Systems 37 (2024), 68082–68119.
[288] Shengqiong Wu, Hao Fei, Leigang Qu, Wei Ji, and Tat-Seng Chua. 2024. Next-gpt: Any-to-any multimodal llm. In Forty-first International Conference
on Machine Learning.
[289] Sijing Wu, Yunhao Li, Huiyu Duan, Yanwei Jiang, Yucheng Zhu, and Guangtao Zhai. 2025. HVEval: Towards Unified Evaluation of Human-Centric
Video Generation and Understanding. In Proceedings of the 33rd ACM International Conference on Multimedia. 13376–13383.
[290] Tong Wu, Shuai Yang, Ryan Po, Yinghao Xu, Ziwei Liu, Dahua Lin, and Gordon Wetzstein. 2025. Video World Models with Long-term Spatial
Memory. arXiv preprint arXiv:2506.05284 (2025).
[291] Tian Xia, Xuweiyi Chen, and Sihan Xu. 2024. Unictrl: Improving the spatiotemporal consistency of text-to-video diffusion models via training-free
unified attention control. arXiv preprint arXiv:2403.02332 (2024).
[292] Qi Xie, Yongjia Ma, Donglin Di, Xuehao Gao, and Xun Yang. 2025. Moca: Identity-preserving text-to-video generation via mixture of cross
attention. arXiv preprint arXiv:2508.03034 (2025).
[293] Tianyi Xie, Yiwei Zhao, Ying Jiang, and Chenfanfu Jiang. 2025. Physanimator: Physics-guided generative cartoon animation. In Proceedings of the
Computer Vision and Pattern Recognition Conference. 10793–10804.
[294] Zhenyu Xie, Yang Wu, Xuehao Gao, Zhongqian Sun, Wei Yang, and Xiaodan Liang. 2024. Towards detailed text-to-motion synthesis via
basic-to-advanced hierarchical diffusion model. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38. 6252–6260.
[295] Jinbo Xing, Menghan Xia, Yuxin Liu, Yuechen Zhang, Yong Zhang, Yingqing He, Hanyuan Liu, Haoxin Chen, Xiaodong Cun, Xintao Wang, et al.
2024. Make-your-video: Customized video generation using textual and structural guidance. IEEE Transactions on Visualization and Computer
Graphics 31, 2 (2024), 1526–1541.
[296] Yazhou Xing, Yingqing He, Zeyue Tian, Xintao Wang, and Qifeng Chen. 2024. Seeing and hearing: Open-domain visual-audio generation with
diffusion latent aligners. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 7151–7161.
[297] Zhen Xing, Qijun Feng, Haoran Chen, Qi Dai, Han Hu, Hang Xu, Zuxuan Wu, and Yu-Gang Jiang. 2024. A survey on video diffusion models.
Comput. Surveys 57, 2 (2024), 1–42.
[298] Jiazheng Xu, Yu Huang, Jiale Cheng, Yuanming Yang, Jiajun Xu, Yuan Wang, Wenbo Duan, Shen Yang, Qunlin Jin, Shurun Li, et al. 2024.
Visionreward: Fine-grained multi-dimensional human preference learning for image and video generation. arXiv preprint arXiv:2412.21059 (2024).
[299] Yucheng Xu, Li Nanbo, Arushi Goel, Zijian Guo, Zonghai Yao, Hamidreza Kasaei, Mohammadreze Kasaei, and Zhibin Li. 2023. Controllable video
generation by learning the underlying dynamical system with neural ode. arXiv preprint arXiv:2303.05323 (2023).
[300] Hongwei Xue, Tiankai Hang, Yanhong Zeng, Yuchong Sun, Bei Liu, Huan Yang, Jianlong Fu, and Baining Guo. 2022. Advancing high-resolution
video-language representation with large-scale video transcriptions. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition. 5036–5045.
[301] Qiyao Xue, Xiangyu Yin, Boyuan Yang, and Wei Gao. 2025. Phyt2v: Llm-guided iterative self-refinement for physics-grounded text-to-video
generation. In Proceedings of the Computer Vision and Pattern Recognition Conference. 18826–18836.
[302] Wilson Yan, Yunzhi Zhang, Pieter Abbeel, and Aravind Srinivas. 2021. Videogpt: Video generation using vq-vae and transformers. arXiv preprint
arXiv:2104.10157 (2021).
[303] Yunzhi Yan, Zhen Xu, Haotong Lin, Haian Jin, Haoyu Guo, Yida Wang, Kun Zhan, Xianpeng Lang, Hujun Bao, Xiaowei Zhou, et al. 2025.
Streetcrafter: Street view synthesis with controllable video diffusion models. In Proceedings of the Computer Vision and Pattern Recognition
Conference. 822–832.
[304] Fan Yang, Zhiyang Chen, Yousong Zhu, Xin Li, and Jinqiao Wang. 2025. From Seeing to Predicting: A Vision-Language Framework for Trajectory
Forecasting and Controlled Video Generation. arXiv preprint arXiv:2510.00806 (2025).
[305] Jiazhi Yang, Shenyuan Gao, Yihang Qiu, Li Chen, Tianyu Li, Bo Dai, Kashyap Chitta, Penghao Wu, Jia Zeng, Ping Luo, et al. 2024. Generalized
predictive model for autonomous driving. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 14662–14672.
[306] Kai Yang, Jian Tao, Jiafei Lyu, Chunjiang Ge, Jiaxin Chen, Weihan Shen, Xiaolong Zhu, and Xiu Li. 2024. Using human feedback to fine-tune
diffusion models without any reward model. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 8941–8951.
[307] Mingyu Yang, Junyou Li, Zhongbin Fang, Sheng Chen, Yangbin Yu, Qiang Fu, Wei Yang, and Deheng Ye. 2024. Playable game generation. arXiv
preprint arXiv:2412.00887 (2024).
[308] Shiyuan Yang, Liang Hou, Haibin Huang, Chongyang Ma, Pengfei Wan, Di Zhang, Xiaodong Chen, and Jing Liao. 2024. Direct-a-video: Customized
video generation with user-directed camera movement and object motion. In ACM SIGGRAPH 2024 Conference Papers. 1–12.
[309] Shuai Yang, Wei Huang, Ruihang Chu, Yicheng Xiao, Yuyang Zhao, Xianbang Wang, Muyang Li, Enze Xie, Yingcong Chen, Yao Lu, et al. 2025.
Longlive: Real-time interactive long video generation. arXiv preprint arXiv:2509.22622 (2025).
[310] Xindi Yang, Baolu Li, Yiming Zhang, Zhenfei Yin, Lei Bai, Liqian Ma, Zhiyong Wang, Jianfei Cai, Tien-Tsin Wong, Huchuan Lu, et al. 2025. VLIPP:
Towards Physically Plausible Video Generation with Vision and Language Informed Physical Prior. arXiv preprint arXiv:2503.23368 (2025).
[311] Xiaomeng Yang, Zhiyu Tan, and Hao Li. 2025. IPO: Iterative preference optimization for text-to-video generation. arXiv preprint arXiv:2502.02088
(2025).

--- Page 34 ---

34
Puspitasari et al.
[312] Yezhou Yang, Yi Li, Cornelia Fermuller, and Yiannis Aloimonos. 2015. Robot learning manipulation action plans by" watching" unconstrained
videos from the world wide web. In Proceedings of the AAAI conference on artificial intelligence, Vol. 29.
[313] Yu Yang, Zhilu Zhang, Xiang Zhang, Yihan Zeng, Hui Li, and Wangmeng Zuo. 2025. PhysWorld: From Real Videos to World Models of Deformable
Objects via Physics-Aware Demonstration Synthesis. arXiv preprint arXiv:2510.21447 (2025).
[314] Zhuoran Yang, Xi Guo, Chenjing Ding, Chiyu Wang, Wei Wu, and Yanyong Zhang. 2025. InstaDrive: Instance-Aware Driving World Models for
Realistic and Consistent Video Generation. In Proceedings of the IEEE/CVF International Conference on Computer Vision. 25410–25420.
[315] Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu Huang, Jiazheng Xu, Yuanming Yang, Wenyi Hong, Xiaohan Zhang, Guanyu Feng,
et al. 2024. Cogvideox: Text-to-video diffusion models with an expert transformer. arXiv preprint arXiv:2408.06072 (2024).
[316] Jingfeng Yao, Cheng Wang, Wenyu Liu, and Xinggang Wang. 2024. Fasterdit: Towards faster diffusion transformers training without architecture
modification. Advances in Neural Information Processing Systems 37 (2024), 56166–56189.
[317] Danah Yatim, Rafail Fridman, Omer Bar-Tal, Yoni Kasten, and Tali Dekel. 2024. Space-time diffusion features for zero-shot text-driven motion
transfer. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 8466–8476.
[318] Deheng Ye, Fangyun Zhou, Jiacheng Lv, Jianqi Ma, Jun Zhang, Junyan Lv, Junyou Li, Minwen Deng, Mingyu Yang, Qiang Fu, et al. 2025. Yan:
Foundational interactive video generation. arXiv preprint arXiv:2508.08601 (2025).
[319] Aoxiong Yin, Xu Tan, Kai Shen, Yichong Leng, Xinyu Zhou, Juncheng Li, and Siliang Tang. 2025. The best of both worlds: Integrating language
models and diffusion models for video generation. In Proceedings of the IEEE/CVF International Conference on Computer Vision. 15604–15615.
[320] Shengming Yin, Chenfei Wu, Huan Yang, Jianfeng Wang, Xiaodong Wang, Minheng Ni, Zhengyuan Yang, Linjie Li, Shuguang Liu, Fan Yang,
et al. 2023. Nuwa-xl: Diffusion over diffusion for extremely long video generation. In Proceedings of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers). 1309–1320.
[321] Jiwen Yu, Yiran Qin, Haoxuan Che, Quande Liu, Xintao Wang, Pengfei Wan, Di Zhang, and Xihui Liu. 2025. Position: Interactive generative video
as next-generation game engine. arXiv preprint arXiv:2503.17359 (2025).
[322] Jiwen Yu, Yiran Qin, Xintao Wang, Pengfei Wan, Di Zhang, and Xihui Liu. 2025. Gamefactory: Creating new games with generative interactive
videos. arXiv preprint arXiv:2501.08325 (2025).
[323] Jianhui Yu, Hao Zhu, Liming Jiang, Chen Change Loy, Weidong Cai, and Wayne Wu. 2023. Celebv-text: A large-scale facial text-video dataset. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 14805–14814.
[324] Lijun Yu, Yong Cheng, Kihyuk Sohn, José Lezama, Han Zhang, Huiwen Chang, Alexander G Hauptmann, Ming-Hsuan Yang, Yuan Hao, Irfan Essa,
et al. 2023. Magvit: Masked generative video transformer. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition.
10459–10469.
[325] Lijun Yu, José Lezama, Nitesh B Gundavarapu, Luca Versari, Kihyuk Sohn, David Minnen, Yong Cheng, Vighnesh Birodkar, Agrim Gupta, Xiuye
Gu, et al. 2023. Language Model Beats Diffusion–Tokenizer is Key to Visual Generation. arXiv preprint arXiv:2310.05737 (2023).
[326] Sihyun Yu, Sangkyung Kwak, Huiwon Jang, Jongheon Jeong, Jonathan Huang, Jinwoo Shin, and Saining Xie. 2024. Representation alignment for
generation: Training diffusion transformers is easier than you think. arXiv preprint arXiv:2410.06940 (2024).
[327] Xian Yu and Jianxun Zhang. 2025. Optimizing Semantic and Texture Consistency in Video Generation. Available at SSRN 5137309 (2025).
[328] Hangjie Yuan, Shiwei Zhang, Xiang Wang, Yujie Wei, Tao Feng, Yining Pan, Yingya Zhang, Ziwei Liu, Samuel Albanie, and Dong Ni. 2024.
Instructvideo: Instructing video diffusion models with human feedback. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition. 6463–6474.
[329] Shenghai Yuan, Jinfa Huang, Xianyi He, Yunyang Ge, Yujun Shi, Liuhan Chen, Jiebo Luo, and Li Yuan. 2025. Identity-preserving text-to-video
generation by frequency decomposition. In Proceedings of the Computer Vision and Pattern Recognition Conference. 12978–12988.
[330] Shenghai Yuan, Jinfa Huang, Yujun Shi, Yongqi Xu, Ruijie Zhu, Bin Lin, Xinhua Cheng, Li Yuan, and Jiebo Luo. 2025. Magictime: Time-lapse video
generation models as metamorphic simulators. IEEE Transactions on Pattern Analysis and Machine Intelligence (2025).
[331] Shenghai Yuan, Jinfa Huang, Yongqi Xu, Yaoyang Liu, Shaofeng Zhang, Yujun Shi, Rui-Jie Zhu, Xinhua Cheng, Jiebo Luo, and Li Yuan. 2024.
Chronomagic-bench: A benchmark for metamorphic evaluation of text-to-time-lapse video generation. Advances in Neural Information Processing
Systems 37 (2024), 21236–21270.
[332] Yu Yuan, Xijun Wang, Tharindu Wickremasinghe, Zeeshan Nadir, Bole Ma, and Stanley H Chan. 2025. NewtonGen: Physics-Consistent and
Controllable Text-to-Video Generation via Neural Newtonian Dynamics. arXiv preprint arXiv:2509.21309 (2025).
[333] Chenlu Zhan, Yu Lin, Gaoang Wang, Hongwei Wang, and Jian Wu. 2024. Medm2g: Unifying medical multi-modal generation via cross-guided
diffusion with visual invariant. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 11502–11512.
[334] Chenyu Zhang, Daniil Cherniavskii, Antonios Tragoudaras, Antonios Vozikis, Thijmen Nijdam, Derck WE Prinzhorn, Mark Bodracska, Nicu Sebe,
Andrii Zadaianchuk, and Efstratios Gavves. 2025. Morpheus: Benchmarking physical reasoning of video generative models with real physical
experiments. arXiv preprint arXiv:2504.02918 (2025).
[335] Chaoning Zhang, Chenshuang Zhang, Chenghao Li, Sheng Zheng, Yu Qiao, Sumit Kumar Dam, Mengchun Zhang, Jung Uk Kim, Seong Tae
Kim, Gyeong-Moon Park, Jinwoo Choi, Sung-Ho Bae, Lik-Hang Lee, Pan Hui, In So Kweon, and Choong Seon Hong. 2023. One Small Step for
Generative AI, One Giant Leap for AGI: A Complete Survey on ChatGPT in AIGC Era. researchgate DOI:10.13140/RG.2.2.24789.70883 (2023).
[336] Chenshuang Zhang, Chaoning Zhang, Mengchun Zhang, and In So Kweon. 2023. Text-to-image Diffusion Models in Generative AI: A Survey.
arXiv preprint arXiv:2303.07909 (2023).

--- Page 35 ---

Sora as a World Model? A Complete Survey on Text-to-Video Generation
35
[337] Chenshuang Zhang, Chaoning Zhang, Sheng Zheng, Mengchun Zhang, Maryam Qamar, Sung-Ho Bae, and In So Kweon. 2023. A Survey on Audio
Diffusion Models: Text To Speech Synthesis and Enhancement in Generative AI. arXiv preprint arXiv:2303.13336 (2023).
[338] David Junhao Zhang, Jay Zhangjie Wu, Jia-Wei Liu, Rui Zhao, Lingmin Ran, Yuchao Gu, Difei Gao, and Mike Zheng Shou. 2025. Show-1: Marrying
pixel and latent diffusion models for text-to-video generation. International Journal of Computer Vision 133, 4 (2025), 1879–1893.
[339] Guofeng Zhang, Angtian Wang, Jacob Zhiyuan Fang, Liming Jiang, Haotian Yang, Bo Liu, Yiding Yang, Guang Chen, Longyin Wen, Alan Yuille,
et al. 2025. TGT: Text-Grounded Trajectories for Locally Controlled Video Generation. arXiv preprint arXiv:2510.15104 (2025).
[340] Haoze Zhang, Tianyu Huang, Zichen Wan, Xiaowei Jin, Hongzhi Zhang, Hui Li, and Wangmeng Zuo. 2025. PhysChoreo: Physics-Controllable
Video Generation with Part-Aware Semantic Grounding. arXiv preprint arXiv:2511.20562 (2025).
[341] Juntao Zhang, Yuehuai Liu, Yu-Wing Tai, and Chi-Keung Tang. 2024. C3net: Compound conditioned controlnet for multimodal content generation.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 26886–26895.
[342] Ke Zhang, Cihan Xiao, Yiqun Mei, Jiacong Xu, and Vishal M Patel. 2025. Think Before You Diffuse: LLMs-Guided Physics-Aware Video Generation.
arXiv preprint arXiv:2505.21653 (2025).
[343] Shiwei Zhang, Jiayu Wang, Yingya Zhang, Kang Zhao, Hangjie Yuan, Zhiwu Qin, Xiang Wang, Deli Zhao, and Jingren Zhou. 2023. I2vgen-xl:
High-quality image-to-video synthesis via cascaded diffusion models. arXiv preprint arXiv:2311.04145 (2023).
[344] Xiangdong Zhang, Jiaqi Liao, Shaofeng Zhang, Fanqing Meng, Xiangpeng Wan, Junchi Yan, and Yu Cheng. 2025. VideoREPA: Learning Physics for
Video Generation through Relational Alignment with Foundation Models. arXiv preprint arXiv:2505.23656 (2025).
[345] Yiyuan Zhang, Yuhao Kang, Zhixin Zhang, Xiaohan Ding, Sanyuan Zhao, and Xiangyu Yue. 2024. Interactivevideo: User-centric controllable video
generation with synergistic multimodal instructions. arXiv preprint arXiv:2402.03040 (2024).
[346] Yipeng Zhang, Xin Wang, Hong Chen, Chenyang Qin, Yibo Hao, Hong Mei, and Wenwu Zhu. 2025. ScenarioDiff: text-to-video generation with
dynamic transformations of scene conditions. International Journal of Computer Vision 133, 7 (2025), 4909–4922.
[347] Yifu Zhang, Hao Yang, Yuqi Zhang, Yifei Hu, Fengda Zhu, Chuang Lin, Xiaofeng Mei, Yi Jiang, Bingyue Peng, and Zehuan Yuan. 2025. Waver:
Wave your way to lifelike video generation. arXiv preprint arXiv:2508.15761 (2025).
[348] Yuhang Zhang, Yuan Zhou, Zeyu Liu, Yuxuan Cai, Qiuyue Wang, Aidong Men, and Huan Yang. 2024. Fleximo: Towards flexible text-to-human
motion video generation. arXiv preprint arXiv:2411.19459 (2024).
[349] Zicheng Zhang, Tengchuan Kou, Shushi Wang, Chunyi Li, Wei Sun, Wei Wang, Xiaoyu Li, Zongyu Wang, Xuezhi Cao, Xiongkuo Min, et al. 2025.
Q-eval-100k: Evaluating visual quality and alignment level for text-to-vision content. In Proceedings of the Computer Vision and Pattern Recognition
Conference. 10621–10631.
[350] Guosheng Zhao, Chaojun Ni, Xiaofeng Wang, Zheng Zhu, Xueyang Zhang, Yida Wang, Guan Huang, Xinze Chen, Boyuan Wang, Youyi Zhang,
et al. 2025. Drivedreamer4d: World models are effective data machines for 4d driving scene representation. In Proceedings of the Computer Vision
and Pattern Recognition Conference. 12015–12026.
[351] Hongxiang Zhao, Xingchen Liu, Mutian Xu, Yiming Hao, Weikai Chen, and Xiaoguang Han. 2025. TASTE-Rob: Advancing video generation
of task-oriented hand-object interaction for generalizable robotic manipulation. In Proceedings of the Computer Vision and Pattern Recognition
Conference. 27683–27693.
[352] Wangbo Zhao, Yizeng Han, Jiasheng Tang, Kai Wang, Yibing Song, Gao Huang, Fan Wang, and Yang You. 2025. Dynamic Diffusion Transformer.
In The Thirteenth International Conference on Learning Representations.
[353] Dian Zheng, Ziqi Huang, Hongbo Liu, Kai Zou, Yinan He, Fan Zhang, Lulu Gu, Yuanhan Zhang, Jingwen He, Wei-Shi Zheng, et al. 2025. Vbench-2.0:
Advancing video generation benchmark suite for intrinsic faithfulness. arXiv preprint arXiv:2503.21755 (2025).
[354] Hongkai Zheng, Weili Nie, Arash Vahdat, and Anima Anandkumar. 2023. Fast training of diffusion models with masked transformers. arXiv
preprint arXiv:2306.09305 (2023).
[355] Sixiao Zheng, Zimian Peng, Yanpeng Zhou, Yi Zhu, Hang Xu, Xiangru Huang, and Yanwei Fu. 2025. Vidcraft3: Camera, object, and lighting control
for image-to-video generation. arXiv preprint arXiv:2502.07531 (2025).
[356] Zangwei Zheng, Xiangyu Peng, Tianji Yang, Chenhui Shen, Shenggui Li, Hongxin Liu, Yukun Zhou, Tianyi Li, and Yang You. 2024. Open-sora:
Democratizing efficient video production for all. arXiv preprint arXiv:2412.20404 (2024).
[357] Fengzhe Zhou, Jiannan Huang, Jialuo Li, Deva Ramanan, and Humphrey Shi. 2025. PAI-Bench: A Comprehensive Benchmark For Physical AI.
arXiv preprint arXiv:2512.01989 (2025).
[358] Bingwen Zhu, Yudong Jiang, Baohan Xu, Siqian Yang, Mingyu Yin, Yidi Wu, Huyang Sun, and Zuxuan Wu. 2025. Aligning Anime Video Generation
with Human Feedback. arXiv preprint arXiv:2504.10044 (2025).
[359] Chuning Zhu, Raymond Yu, Siyuan Feng, Benjamin Burchfiel, Paarth Shah, and Abhishek Gupta. 2025. Unified world models: Coupling video and
action diffusion for pretraining on large robotic datasets. arXiv preprint arXiv:2504.02792 (2025).
[360] Zheng Zhu, Xiaofeng Wang, Wangbo Zhao, Chen Min, Bohan Li, Nianchen Deng, Min Dou, Yuqi Wang, Botian Shi, Kai Wang, et al. 2024. Is sora a
world simulator? a comprehensive survey on general world models and beyond. arXiv preprint arXiv:2405.03520 (2024).
[361] Vlas Zyrianov, Henry Che, Zhijian Liu, and Shenlong Wang. 2025. Lidardm: Generative lidar simulation in a generated world. In 2025 IEEE
International Conference on Robotics and Automation (ICRA). IEEE, 6055–6062.

```
