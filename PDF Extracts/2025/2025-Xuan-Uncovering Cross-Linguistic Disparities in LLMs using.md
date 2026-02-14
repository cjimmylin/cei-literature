---\ntitle: "2025-Xuan-Uncovering Cross-Linguistic Disparities in LLMs using - PDF Extract"\nsource_pdf: "2025/2025-Xuan-Uncovering Cross-Linguistic Disparities in LLMs using.pdf"\npages: 14\nextracted_at: "2026-02-14T02:17:34.041651"\n---\n\n# PDF Extract: 2025-Xuan-Uncovering Cross-Linguistic Disparities in LLMs using\n\n**Source PDF:** 2025/2025-Xuan-Uncovering Cross-Linguistic Disparities in LLMs using.pdf\n**Total Pages:** 14\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nUncovering Cross-Linguistic Disparities in LLMs using Sparse
Autoencoders
Richmond Sin Jing Xuan1, Jalil Huseynov 1, Yang Zhang1
1 National University of Singapore
Abstract
Multilingual Large Language Models (LLMs)
exhibit strong cross-linguistic generalization,
yet medium-to-low resource languages un-
derperform in common benchmarks (ARC-C,
MMLU, HellaSwag). We analyze activation
patterns in Gemma-2-2B across all 26 residual
layers and 10 languages: Chinese (zh), Rus-
sian (ru), Spanish (es), Italian (it); medium-to-
low resource languages: Indonesian (id), Cata-
lan (ca), Marathi (mr), Malayalam (ml), Hindi
(hi), with English (en) as the reference—using
Sparse Autoencoders (SAEs), revealing sys-
tematic disparities—medium-to-low resource
languages receive up to 26.27% lower acti-
vations in early layers, persisting at 19.89%
in deeper layers. To address this, we apply
activation-aware fine-tuning via LoRA, leading
to substantial activation gains (e.g., Malayalam
87.69%, Hindi 86.32%) while maintaining En-
glish retention (∼91%).
Post-fine-tuning,
benchmarks show modest but consistent im-
provements, highlighting activation alignment
as a crucial factor in multilingual LLM perfor-
mance.
1
Introduction
Large Language Models (LLMs), such as GPT-4
(OpenAI, 2023), Gemma (DeepMind, 2024), and
LLaMA 3 (AI, 2024), demonstrate strong mul-
tilingual capabilities in zero-shot and few-shot
settings.
These models leverage shared cross-
linguistic representations, enabling them to process
both high- and low-resource languages. However,
multilingual training data remains highly imbal-
anced, with English dominating most pre-training
corpora. OpenAI (2023) reported that 92.65% of
GPT-3’s training tokens were English, while Meta
(2024) disclosed that non-English data makes up
just over 5% of LLaMA 3’s dataset. This raises
concerns about whether LLMs are disproportion-
ately optimized for high-resource languages (Blasi
et al., 2021).
To investigate this multilingual performance gap,
we leverage Sparse Autoencoders (SAEs) (Cun-
ningham et al., 2023)—an interpretability tool de-
signed to analyze internal neuron activations in
LLMs. SAEs have been widely used in mechanis-
tic interpretability research (Bricken et al., 2023;
Templeton et al., 2024; Kissane et al., 2024) to ex-
tract structured, human-interpretable features from
complex activations. Unlike embeddings, which
measure representational similarity, SAEs provide
direct insights into how LLMs process different
languages at the neuron activation level. A key
recent advancement in this space is Gemma Scope
(Lieberum et al., 2024), an open-source framework
that applies SAEs to Gemma-2-2B (Riviere et al.,
2024), allowing for precise layer-wise analysis of
neuron activations linked to linguistic properties.
Building on this framework, we investigate whether
LLMs exhibit systematic activation disparities be-
tween high-resource and medium-to-low resource
languages, despite similar embeddings.
Using
SAEs on Gemma-2-2B, we conduct a layer-wise
activation analysis across multiple languages to as-
sess whether activation differences contribute to
the multilingual performance gap.
Our key contributions are as follows:
1. We analyze embedding similarity across lan-
guages and demonstrate that despite appearing to
capture all languages similarly, LLMs exhibit sig-
nificant performance disparities in real-world tasks,
as evidenced by lower scores for medium-to-low re-
source languages on Okapi’s evaluation framework
(Lai et al., 2023).
2. We conduct a layer-wise SAE activation study,
showing that medium-to-low resource languages
exhibit significantly lower activation values com-
pared to high-resource languages, particularly in
the early layers of processing.
3. We demonstrate that fine-tuning with activa-
tion alignment reduces activation disparities and
yields modest improvements in model performance,
1
arXiv:2507.18918v1  [cs.CL]  25 Jul 2025

--- Page 2 ---\n\nproviding a foundation for future work in improv-
ing multilingual representations in LLMs.
Our findings challenge the assumption that em-
bedding similarity guarantees equal linguistic
understanding and highlight the importance of
activation-based interpretability techniques in mul-
tilingual NLP. By identifying and quantifying cross-
linguistic activation disparities, we contribute to
the broader discourse on multilingual fairness and
propose new strategies for improving LLM perfor-
mance on medium-to-low resource languages.
2
Methodology
In this section, we outline our methodology for
investigating multilingual representation in LLMs.
We first introduce the dataset and preprocessing
pipeline. Next, we assess whether LLMs encode
different languages equally. To evaluate whether
these similarities translate to actual performance,
we conduct multilingual benchmark tests using
Okapi’s framework. Finally, we perform SAE-
based activation analysis to uncover deeper acti-
vation disparities across languages and apply fine-
tuning with activation alignment to mitigate activa-
tion disparities and improve model performance.
2.1
Data Collection and Preprocessing
We use the Neuronpedia (Joseph Bloom and
Chanin, 2024) dataset, which contains 16, 384 in-
terpretable neuron features across all 26 layers of
Gemma-2-2B. Each feature represents a learned lin-
guistic property identified via SAE decomposition.
To construct our dataset, we first apply tokeniza-
tion constraints by segmenting each English phrase
using a ±3 token window around the most activated
token, preserving contextual relevance while ensur-
ing efficient processing.
We then extract top-activated English phrases ex-
ceeding an 80% activation threshold relative to the
highest activation in that feature and translate them
into nine languages (zh, ru, es, it, id, ca, mr, ml,
hi) using Helsinki-NLP models (Tiedemann and
Thottingal, 2020; Tiedemann et al., 2023). This
yields a multilingual dataset of approximately six
million phrases.
2.2
Embedding-Based Activation Analysis
We analyze cross-linguistic representations in
Gemma-2-2B by computing cosine similarity be-
tween residual activations of English phrases and
their translations across nine languages. In our
collected dataset, each phrase is associated with
different feature indices. We use data from fea-
ture indices sampled at intervals of 16, selecting
{16i | i ∈{0, . . . , 999}} from 16, 384 available
indices to balance efficiency and representative-
ness.
To obtain fixed-size activation vectors, we apply
mean pooling over token activations per phrase.
For each layer, we compute the cosine similarity be-
tween activation vectors of translated phrases and
their English counterparts and then average these
values across all phrases. This yields per-layer sim-
ilarity scores that quantify embedding alignment
across languages, further discussed in Section 3.1.
2.3
Multilingual Benchmark Evaluation
Using Okapi’s framework, we evaluate LLMs ac-
curacy on multilingual MMLU (Hendrycks et al.,
2020), HellaSwag (Zellers et al., 2019), and ARC-
Challenge (Clark et al., 2018), comparing high-
resource and medium-to-low resource languages to
assess alignment between embeddings and actual
performance.
2.4
SAE-Based Activation Analysis
To go beyond embeddings, we analyze activation-
level disparities using SAEs trained on Gemma-2-
2B. Given a phrase P in language L, we extract its
activation vector at layer l:
AL
l = SAE(P, l)
For each feature index, multiple phrases contribute
activation values. We compute the mean activa-
tion per index by averaging across all associated
phrases, allowing a direct comparison of activation
magnitudes at each index.
2.5
Cross-Linguistic Activation Disparities
Finally, we quantify activation differences between
high-resource and medium-to-low resource lan-
guages. For each layer l, we compute the percent-
age activation gap between the two groups:
∆Al =
¯Ahigh −¯Amed-low
¯Ahigh
× 100
where ¯Ahigh and ¯Amed-low represent the mean acti-
vation scores for high-resource and medium-to-low
resource languages, respectively. By analyzing
∆Al across all layers, we uncover whether LLMs
activate differently for different language groups,
highlighting potential biases in how features are
learned and processed.
2

--- Page 3 ---\n\n2.6
Fine-Tuning for Improved Model
Performance
To enhance multilingual performance, we apply
LoRA-based fine-tuning (Hu et al., 2021) with an
activation alignment objective. The loss function
is defined as:
f(ul, vl) = |ul −vl| + α · ||ul −uorig,l||2
where ul represents the activation of English at
layer l, vl represents the activation of a correspond-
ing language, and uorig,l is the original English
activation recorded in Neuronpedia. The first term
minimizes activation gaps between English and the
target language, while the second term ensures En-
glish activations remain stable during fine-tuning.
Fine-tuning results are analyzed in Section 3.3.
3
Experiments
We conduct experiments using the Gemma-2-2B
model and analyze cross-linguistic activation pat-
terns with Gemma Scope, an interpretability frame-
work based on Sparse Autoencoders (SAEs).
Section 3.1 examines the gap between embedding
similarity and benchmark performance, highlight-
ing multilingual disparities. Section 3.2 analyzes
activation differences across languages using SAEs.
Section 3.3 evaluates fine-tuning with activation
alignment to reduce activation gaps and enhance
cross-linguistic performance.
3.1
Embedding-Based Performance
Disparities
Embedding similarity is often used as a proxy
for multilingual generalization (Dubossarsky et al.,
2020), but our analysis shows it does not always
correlate with strong benchmark performance.
We compute cosine similarity between English
residual activations and their translations in nine
languages using Gemma-2-2B. As shown in Fig-
ure 1, similarity declines in the initial and final
layers, aligning with their encoding and text gen-
eration roles (Zhang et al., 2024). In intermediate
layers, most languages—except Malayalam and
Marathi—maintain similarity above 0.8, while all
remain above 0.7, aside from slight dips in some
middle layers. However, despite strong embedding
alignment, benchmark results (Figure 2) reveal sub-
stantial performance gaps.
While residual activation similarities remain
high, ARC-Challenge (10-shot) scores drop from
53.67% (English) to 26.16% (Marathi) and
Figure 1: Cross-linguistic embedding similarity be-
tween English and nine languages across all layers.
Figure 2: Performance between high-resource and
medium-to-low resource languages across all bench-
marks.
26.34% (Malayalam), and HellaSwag (10-shot)
shows a 46.79% gap between English and Malay-
alam, indicating surface-level alignment does not
guarantee equitable activation dynamics. Further-
more, medium-to-low resource languages consis-
tently underperform across all benchmarks, partic-
ularly ARC-Challenge and MMLU, where Hindi,
Marathi, and Malayalam score significantly lower
despite high embedding similarity (Robinson et al.,
2023).
3.2
SAE-Based Activation Analysis
To investigate performance disparities, we analyze
cross-linguistic activation patterns using Sparse
Autoencoders (SAEs).
Figure 3 visualizes
activation differences across 26 layers.
These differences lead to three key observations:
1. Peak disparities in early layers. Activation gaps
are largest at layer 6 (26.27%), suggesting weaker
encoding of lower resource languages, consistent
with prior findings on syntactic and semantic fea-
ture activation (Nanda et al., 2024).
2. Reduction but persistence of disparities in deeper
3

--- Page 4 ---\n\nFigure 3:
Differences in activation between high-
resource and medium-to-low resource languages across
layers.
Figure 4: Activation improvements and English reten-
tion compared to the original score across all languages
in layer 20.
layers.
Activation gaps decrease to 19.89% at
layer 25, suggesting that deeper layers rely more
on shared representations rather than language-
specific features (Dufter and Schütze, 2020; Paul
et al., 2024; Pires et al., 2019).
3.
Activation gaps correlate with performance.
Medium-to-low resource languages show consis-
tent 20% lower activations, mirroring weaker com-
mon benchmark results (see Figure 2), aligning
with evidence that activation disparities hinder mul-
tilingual generalization (Conneau et al., 2020). Fig-
ures 9, 10, and 11 show that activation gap is indeed
negatively correlated with benchmark performance.
3.3
Fine-Tuning for Improved Model
Performance
Fine-tuning improves activation alignment across
languages, leading to measurable gains in both ac-
tivation consistency and benchmark performance.
Fine-tuning yields two key outcomes:
1. Activation gains across languages with English
stability. Fine-tuning increased activations across
all ten languages in layer 20 (Figure 4), with the
highest improvements in Marathi (93.87%), Malay-
alam (87.69%), and Hindi (86.32%). Even high-
resource languages like Russian (70.08%) and Chi-
nese (66.93%) saw substantial gains. English ac-
tivations remained stable (≥90% retention), en-
suring fine-tuning did not distort learned represen-
tations. This trend generalizes across layers, as
shown by the reduction of activation gaps in Malay-
alam (see Appendix Figure 5).
2. Improved benchmark performance. Fine-tuning
resulted in a 1.44-point increase in ARC-C (Malay-
alam) accuracy, translating to a 5.47% improve-
ment, demonstrating the positive impact of acti-
vation alignment on downstream tasks (Conneau
et al., 2020; Su et al., 2024). Additional benchmark
results (Malayalam) for other tasks can be found in
Appendix Figure 6.
4
Limitations
Our study has three main limitations. First, while
Helsinki-NLP models enable efficient large-scale
translation, they may introduce errors that mis-
align activation patterns, particularly for medium-
to-low resource languages, introducing bias in
cross-lingual analysis (Agrawal et al., 2024). Sec-
ond, while fine-tuning reduced activation dispar-
ities, benchmark performance improvements re-
mained modest. This suggests that activation align-
ment alone is insufficient, as multilingual LLMs do
not fully converge to shared representations across
languages (Zeng et al., 2024). Third, our findings
are based on Gemma-2-2B, and it remains unclear
whether similar activation disparities exist across
other architectures. Multilingual activation studies
indicate that disparities may vary across models,
warranting further investigation (Liu et al., 2024).
5
Conclusion
This study reveals that LLMs exhibit systematic
activation disparities across languages, despite
embedding similarity. Medium-to-low resource
languages consistently receive lower activations,
which correlate with weaker performance on mul-
tilingual benchmarks. While fine-tuning reduces
activation gaps, its effect on task performance re-
mains limited, highlighting the need for more effec-
tive adaptation strategies. Future work should ex-
plore refining fine-tuning techniques to better trans-
late activation alignment into performance gains
and extend this analysis to other LLMs and multi-
lingual datasets to further improve language equity
in LLMs.
4

--- Page 5 ---\n\nReferences
Ashish Sunil Agrawal, Barah Fazili, and Preethi Jyothi.
2024. Translation errors significantly impact low-
resource languages in cross-lingual learning. In Pro-
ceedings of the 18th Conference of the European
Chapter of the Association for Computational Lin-
guistics (EACL).
Meta AI. 2024. Llama 3: Advances in large-scale mul-
tilingual training. Meta Research.
Evan
Anders,
Clement
Neo,
Jason
Hoelscher-
Obermaier, and Jessica N. Howard. 2024. Sparse
autoencoders find composed features in small toy
models.
Damian Blasi, Antonios Anastasopoulos, and Gra-
ham Neubig. 2021. Systematic inequalities in lan-
guage technology performance across the world’s
languages. arXiv preprint arXiv:2110.06733.
Trenton Bricken, Adly Templeton, Joshua Batson, Brian
Chen, Adam Jermyn, Tom Conerly, Nick Turner,
Cem Anil, Carson Denison, Amanda Askell, et al.
2023. Towards monosemanticity: Decomposing lan-
guage models with dictionary learning. Transformer
Circuits Thread, 2.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018. Think you have solved question an-
swering? try arc, the ai2 reasoning challenge. arXiv
preprint arXiv:1803.05457.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale. arXiv
preprint arXiv:1911.02116.
Hoagy Cunningham, Aidan Ewart, Logan Riggs, Robert
Huben, and Lee Sharkey. 2023. Sparse autoencoders
find highly interpretable features in language models.
arXiv preprint arXiv:2309.08600.
Google DeepMind. 2024. Gemma: Open models based
on gemini research and technology. arXiv preprint
arXiv:2403.08295.
Haim Dubossarsky, Ivan Vuli´c, Roi Reichart, and Anna
Korhonen. 2020. The secret is in the spectra: Predict-
ing cross-lingual task performance with spectral sim-
ilarity measures. arXiv preprint arXiv:2001.11136.
Philipp Dufter and Hinrich Schütze. 2020. Identifying
necessary elements for bert’s multilinguality. arXiv
preprint arXiv:2005.00396.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300.
Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
and Weizhu Chen. 2021.
Lora: Low-rank adap-
tation of large language models.
arXiv preprint
arXiv:2106.09685.
Curt Tigges Joseph Bloom and David Chanin.
2024. Saelens. https://github.com/jbloomAus/
SAELens.
Connor Kissane, Robert Krzyzanowski, Joseph Isaac
Bloom, Arthur Conmy, and Neel Nanda. 2024. In-
terpreting attention layer outputs with sparse autoen-
coders. arXiv preprint arXiv:2406.17759.
Viet Dac Lai, Chien Van Nguyen, Nghia Trung Ngo,
Thuat Nguyen, Franck Dernoncourt, Ryan A. Rossi,
and Thien Huu Nguyen. 2023. Okapi: Instruction-
tuned large language models in multiple languages
with reinforcement learning from human feedback.
arXiv preprint arXiv:2307.16039.
Tom Lieberum, Senthooran Rajamanoharan, Arthur
Conmy, Lewis Smith, Nicolas Sonnerat, Vikrant
Varma, János Kramár, Anca Dragan, Rohin Shah,
and Neel Nanda. 2024. Gemma scope: Open sparse
autoencoders everywhere all at once on gemma 2.
arXiv preprint arXiv:2408.05147.
Weize Liu, Yinlong Xu, Hongxia Xu, Jintai Chen, Xum-
ing Hu, and Jian Wu. 2024. Unraveling babel: Ex-
ploring multilingual activation patterns of llms and
their applications. arXiv preprint arXiv:2402.16367.
Neel Nanda, Robert Krzyzanowski, Connor Kissane,
Joseph Isaac Bloom, and Arthur Conmy. 2024. In-
terpreting attention layer outputs with sparse autoen-
coders. arXiv preprint arXiv:2406.17759.
OpenAI. 2023. Gpt-4 technical report. arXiv preprint
arXiv:2303.08774.
Indraneil Paul, Goran Glavaš, and Iryna Gurevych. 2024.
Ircoder: Intermediate representations make language
models robust multilingual code generators. arXiv
preprint arXiv:2403.03894.
Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.
How multilingual is multilingual bert?
arXiv
preprint arXiv:1906.01502.
Gemma Team: Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupati-
raju, Léonard Hussenot, Thomas Mesnard, Bobak
Shahriari, Alexandre Ramé, Johan Ferret, Peter
Liu, Pouya Tafti, Abe Friesen, Michelle Casbon,
Sabela Ramos, Ravin Kumar, Charline Le Lan,
Sammy Jerome, Anton Tsitsulin, Nino Vieillard,
Piotr Stanczyk, Sertan Girgin, Nikola Momchev,
Matt Hoffman, Shantanu Thakoor, Jean-Bastien Grill,
Behnam Neyshabur, Olivier Bachem, Alanna Wal-
ton, Aliaksei Severyn, Alicia Parrish, Aliya Ah-
mad, Allen Hutchison, Alvin Abdagic, Amanda
Carl, Amy Shen, Andy Brock, Andy Coenen, An-
thony Laforge, Antonia Paterson, Ben Bastian, Bilal
Piot, Bo Wu, Brandon Royal, Charlie Chen, Chintu
5

--- Page 6 ---\n\nKumar, Chris Perry, Chris Welty, Christopher A.
Choquette-Choo, Danila Sinopalnikov, David Wein-
berger, Dimple Vijaykumar, Dominika Rogozi´nska,
Dustin Herbison, Elisa Bandy, Emma Wang, Eric
Noland, Erica Moreira, Evan Senter, Evgenii Elty-
shev, Francesco Visin, Gabriel Rasskin, Gary Wei,
Glenn Cameron, Gus Martins, Hadi Hashemi, Hanna
Klimczak-Pluci´nska, Harleen Batra, Harsh Dhand,
Ivan Nardini, Jacinda Mein, Jack Zhou, James Svens-
son, Jeff Stanway, Jetha Chan, Jin Peng Zhou, Joana
Carrasqueira, Joana Iljazi, Jocelyn Becker, Joe Fer-
nandez, Joost van Amersfoort, Josh Gordon, Josh
Lipschultz, Josh Newlan, Ju yeong Ji, Kareem Mo-
hamed, Kartikeya Badola, Kat Black, Katie Milli-
can, Keelin McDonell, Kelvin Nguyen, Kiranbir Sod-
hia, Kish Greene, Lars Lowe Sjoesund, Lauren Usui,
Laurent Sifre, Lena Heuermann, Leticia Lago, and
Lilly McNealus et al. 2024.
Gemma 2: Improv-
ing open language models at a practical size. arXiv
preprint arXiv:2408.00118.
Nathaniel R. Robinson, Perez Ogayo, David R.
Mortensen, and Graham Neubig. 2023. Chatgpt mt:
Competitive for high- (but not low-) resource lan-
guages. arXiv preprint arXiv:2309.07423.
Tong Su, Xin Peng, Sarubi Thillainathan, David
Guzmán, Surangika Ranathunga, and En-Shiun An-
nie Lee. 2024. Unlocking parameter-efficient fine-
tuning for low-resource language translation. arXiv
preprint arXiv:2412.15726.
Adly Templeton, Tom Conerly, Jonathan Marcus,
Jack Lindsey, Trenton Bricken, Brian Chen, Adam
Pearce, Craig Citro, Emmanuel Ameisen, Andy
Jones, Hoagy Cunningham, Nicholas L. Turner,
Callum McDougall, Monte MacDiarmid, Alex
Tamkin, Esin Durmus, Tristan Hume, Francesco
Mosconi, C. Daniel Freeman, Theodore R. Sumers,
Edward Rees,
Joshua Batson,
Adam Jermyn,
Shan Carter, Chris Olah, and Tom Henighan.
2024. Scaling monosemanticity: Extracting inter-
pretable features from claude 3 sonnet. Available
at:
https://transformer-circuits.pub/2024/
scaling-monosemanticity/ (Accessed on May 21,
2024).
Jörg Tiedemann, Mikko Aulamo, Daria Bakshandaeva,
Michele Boggia, Stig-Arne Grönroos, Tommi Niem-
inen, Alessandro Raganato, Yves Scherrer, Raul
Vazquez, and Sami Virpioja. 2023. Democratizing
neural machine translation with OPUS-MT. Lan-
guage Resources and Evaluation, 58:713–755.
Jörg Tiedemann and Santhosh Thottingal. 2020. OPUS-
MT — Building open translation services for the
World. In Proceedings of the 22nd Annual Confer-
ence of the European Association for Machine Trans-
lation (EAMT), Lisbon, Portugal.
Demian Till. 2024. Do sparse autoencoders find "true
features".
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. Hellaswag: Can a
machine really finish your sentence? arXiv preprint
arXiv:1905.07830.
Hongchuan Zeng, Senyu Han, Lu Chen, and Kai Yu.
2024. Converging to a lingua franca: Evolution of
linguistic regions and semantic alignment in mul-
tilingual large language models.
arXiv preprint
arXiv:2410.11718.
Yang Zhang, Yanfei Dong, and Kenji Kawaguchi. 2024.
Investigating layer importance in large language mod-
els. arXiv preprint arXiv:2409.14381.
6

--- Page 7 ---\n\nA
Appendix
A.1
Related Works
Sparse Autoencoders (SAEs) have been widely
adopted in mechanistic interpretability for decom-
posing neural activations into monosemantic la-
tent features. However, recent studies have raised
concerns about their ability to recover truly inde-
pendent and disentangled features. Till (2024) ar-
gues that ℓ1 regularization, which penalizes activa-
tions to enforce sparsity, may cause neurons to en-
code frequently co-occurring feature combinations
rather than distinct, independent features. As a re-
sult, some rare latent features may not be learned
at all. Furthermore, Anders et al. (2024) demon-
strates that SAEs consistently learn composed fea-
tures rather than the true underlying features, re-
gardless of learning rate or ℓ1 coefficient used in
training. These findings suggest that SAEs may
distort learned representations, potentially limiting
their interpretability.
While these concerns focus on the properties of
SAEs themselves, our study suggests that the ob-
served activation gaps may be a result of the
model struggling to generalize in medium-to-low
resource languages, rather than a fundamental is-
sue with SAE representations. Specifically, we
find that activation vectors appear well-aligned
across languages at the embedding layer, but a sig-
nificant gap emerges at the SAE layer between
high-resource and medium-to-low resource lan-
guages. This aligns with performance disparities
observed in benchmark tasks such as ARC-C, Hel-
laSwag, and MMLU, where model accuracy de-
clines for medium-to-low resource languages. Our
results suggest that the model itself may struggle
to develop robust representations for these lan-
guages, which is reflected in the activation pat-
terns extracted by SAEs. This finding underlines
the broader challenge of ensuring high-quality,
language-agnostic representations in multilingual
models.
A.2
Preprocessing and Data Preparation
A.2.1
Gemma-2-2B and Gemma Scope Local
Deployment
We deploy Gemma-2-2B and Gemma Scope lo-
cally to enable efficient processing and analysis of
neural activations across multiple languages. This
setup provides local inference capabilities, allow-
ing structured analysis of neuron activations with-
out cloud-based constraints.
Layers Processed:
Gemma-2-2B consists of 26
layers, each containing 16, 384 indices, represent-
ing distinct learned features. The layers processed
in this study are:
• layer_0/width_16k/average_l0_105
• layer_1/width_16k/average_l0_102
• layer_2/width_16k/average_l0_141
• layer_3/width_16k/average_l0_59
• layer_4/width_16k/average_l0_124
• layer_5/width_16k/average_l0_68
• layer_6/width_16k/average_l0_70
• layer_7/width_16k/average_l0_69
• layer_8/width_16k/average_l0_71
• layer_9/width_16k/average_l0_73
• layer_10/width_16k/average_l0_77
• layer_11/width_16k/average_l0_80
• layer_12/width_16k/average_l0_82
• layer_13/width_16k/average_l0_84
• layer_14/width_16k/average_l0_84
• layer_15/width_16k/average_l0_78
• layer_16/width_16k/average_l0_78
• layer_17/width_16k/average_l0_77
• layer_18/width_16k/average_l0_74
• layer_19/width_16k/average_l0_73
• layer_20/width_16k/average_l0_71
• layer_21/width_16k/average_l0_70
• layer_22/width_16k/average_l0_72
• layer_23/width_16k/average_l0_75
• layer_24/width_16k/average_l0_73
• layer_25/width_16k/average_l0_116
A.2.2
Data Cleaning and Preprocessing
All data used for fine-tuning and experiments are
identical to the multilingual dataset described in
Section 2.1.
7

--- Page 8 ---\n\nData Extraction:
• Extracted activation data from Neuronpedia
JSON files.
• Converted structured JSON into CSV format.
• Standardized sentence formatting for transla-
tion and activation analysis.
Extracted Features:
• Layer Number – Neural network layer refer-
ence.
• Index Number – Specifies neuron index.
• Sentence_en – Extracted English sentences
(activation threshold ≥0.80 of the max acti-
vation).
• MaxValue_en – Maximum activation score
per sentence.
• phraseWindow_en – A 7-token context win-
dow, consisting of the highest activation score
token along with the 3 preceding and 3 follow-
ing tokens.
• avgMaxValue_en – Average activation score
for English.
A.2.3
Translation Process
Method:
Sentences
from
phraseWindow_en
were translated into nine additional languages us-
ing Helsinki-NLP models.
Language Groups:
• High-Resource Languages:
– phraseWindow_en – English
– phraseWindow_zh – Chinese
– phraseWindow_ru – Russian
– phraseWindow_es – Spanish
– phraseWindow_it – Italian
• Medium-to-Low Resource Languages:
– phraseWindow_id – Indonesian
– phraseWindow_ca – Catalan
– phraseWindow_mr – Marathi
– phraseWindow_ml – Malayalam
– phraseWindow_hi – Hindi
B
Fine-Tuning Setup and Evaluation
B.1
Fine-Tuning Configuration
To assess the impact of activation alignment on mul-
tilingual performance, we fine-tune Gemma-2-2B
using LoRA-based adaptation. The fine-tuning pro-
cess targets activation disparities across multiple
languages, with specific configurations as follows:
All Languages (Targeting Layer 20)
• Data size: 4, 000 samples
• Regularization weight (α): 1.00
• Iterations: 2
• Target layer: 20
• Fine-tuned layers: 0 −20
The target layer refers to the layer at which we aim
to reduce activation disparities between English
and other languages. In this setting, we include
phrases from all nine languages during fine-tuning,
without designating a specific target language. The
objective is to achieve broad alignment across the
multilingual set. The dataset used for fine-tuning
is the same as the one described in Section 2.1.
Layer 20 is specifically selected to allow fine-
tuning of as many layers as possible while avoiding
disruption to the uppermost layers responsible for
text generation.
B.2
Benchmarking with Okapi’s Framework
Fine-tuned models were evaluated on ARC-
Challenge, HellaSwag, and MMLU using Okapi’s
framework, ensuring consistency with Gemma-2-
2B’s technical report evaluation settings.
• ARC-Challenge (10-shot): 2, 497 samples
per language
• HellaSwag (10-shot): 6, 019 samples per lan-
guage
• MMLU (5-shot): 12, 414 samples per lan-
guage
Each dataset was standardized to maintain compa-
rability across languages:
• ARC-Challenge: Common question IDs re-
tained across languages.
• HellaSwag: Preserved identical samples per
language.
8

--- Page 9 ---\n\n• MMLU: Truncated to ensure consistency
across languages.
This setup follows the Hugging Face leaderboard
evaluation protocol for Gemma-2-2B.
C
Experimental Results
C.1
Residual Activation Similarities Across
Languages
All pairwise cosine similarity results are available
in our GitHub repository under the 04 Residual Ac-
tivation Calculations & Analysis directory. While
our paper focuses on similarities between English
and nine other languages, the repository contains
full similarity matrices for all language pairs.
C.2
Activation Disparities Across Layers
To quantify the differences in activation between
high-resource and medium-to-low resource lan-
guages, we measure activation differences across
all 26 layers of Gemma-2-2B. Table 1 presents
these differences, showing a peak gap of 26.27%
at layer 6. Although the gap reduces in deeper lay-
ers, a persistent difference remains, highlighting
structural disparities in multilingual representation
learning.
C.3
Benchmark Performance Across
Languages
Tables 2, 3, and 4 present the accuracy results
for high-resource and medium-to-low resource lan-
guages across different tasks. The results show
that high-resource languages consistently outper-
form medium-to-low resource languages across all
benchmarks, reinforcing that weaker activations in
feature space lead to weaker performance in down-
stream tasks.
C.4
Activation Improvements at Layer 20
Across Languages
Fine-tuning at layer 20 resulted in activation in-
creases across all ten languages. Table 5 presents
the activation improvements for each language post-
fine-tuning, while Table 6 reports the retention of
English activations after fine-tuning.
C.5
Activation Improvements for Malayalam
Across Various Layers
Malayalam, which initially exhibited the largest
activation disparity, demonstrated substantial im-
provements in activation levels across all layers
Layer
Activation Difference (%)
0
18.06
1
21.31
2
21.82
3
23.59
4
24.89
5
25.77
6
26.27
7
25.55
8
24.84
9
23.41
10
23.59
11
22.25
12
21.60
13
20.52
14
20.49
15
22.25
16
21.54
17
21.68
18
22.64
19
23.67
20
23.15
21
22.64
22
23.20
23
22.80
24
20.75
25
19.89
Table 1: Activation differences between high-resource
and medium-to-low resource languages across all layers.
after fine-tuning. As shown in Figure 5, the activa-
tion differences are reduced across the layers that
were randomly selected for the experiment, align-
ing Malayalam more closely with high-resource
languages.
To quantify these improvements, Table 7 presents
the percentage increase in activation values for
Malayalam across different layers. For efficiency,
we randomly selected a subset of layers to serve
as representative checkpoints. This selection en-
sures that improvements are observed across early,
middle, and deep layers without introducing bias
in specific regions of the model.
While fine-tuning successfully increased Malay-
alam’s activation levels, it is also important to as-
sess whether English activations were preserved.
Table 8 reports the retention rates of English acti-
vations across the same layers. Notably, English
activations remained largely stable, with retention
exceeding 80% in all layers and peaking at 95.75%
9

--- Page 10 ---\n\nLanguage
ARC-Challenge (%)
High-Resource Languages
English
53.67
Chinese
42.22
Russian
37.90
Spanish
45.07
Italian
43.91
Medium-to-Low Resource Languages
Indonesian
40.14
Catalan
38.71
Marathi
26.16
Malayalam
26.34
Hindi
30.47
Table 2:
ARC-Challenge benchmark accuracy for
Gemma-2-2B.
Language
HellaSwag (%)
High-Resource Languages
English
76.23
Chinese
54.98
Russian
54.54
Spanish
62.95
Italian
57.72
Medium-to-Low Resource Languages
Indonesian
55.92
Catalan
50.24
Marathi
30.99
Malayalam
29.44
Hindi
39.77
Table 3: HellaSwag benchmark accuracy for Gemma-2-
2B.
in layer 15. This indicates that improvements in
Malayalam did not come at the cost of significant
degradation in English performance.
These results demonstrate that our fine-tuning
approach, guided by the loss function incorporat-
ing activation disparity, successfully reduces the
activation gap for Malayalam across layers while
preserving English activations. The combination
of Figure 5 and Tables 7 and 8 provides a compre-
hensive validation of our loss formulation’s impact
across multiple layers in Gemma-2-2B model.
C.6
Model Performance After Fine-tuning for
Malayalam Across All Benchmarks
While fine-tuning significantly improved activation
levels, its impact on benchmark performance was
inconsistent. As shown in Figure 6, the model
exhibited varying degrees of performance changes
Language
MMLU (%)
High-Resource Languages
English
49.15
Chinese
40.71
Russian
40.22
Spanish
44.57
Italian
43.70
Medium-to-Low Resource Languages
Indonesian
42.30
Catalan
42.16
Marathi
31.54
Malayalam
29.44
Hindi
35.85
Table 4: MMLU benchmark accuracy for Gemma-2-2B.
Language
Activation Improvement (%)
Malayalam
87.69
Hindi
86.32
Marathi
93.87
Catalan
63.22
Indonesian
56.58
Italian
43.48
Spanish
43.71
Russian
70.08
Chinese
66.93
Table 5: Activation improvements across ten languages
after fine-tuning.
across ARC-Challenge (ARC-C), MMLU, and Hel-
laSwag. Table 9 quantifies these results. Notably,
ARC-C showed a performance gain, increasing
1.44% from 26.34% to 27.77% after fine-tuning.
This suggests that the model may have improved in
reasoning-based tasks, potentially benefiting from
better token representations at deeper layers. How-
ever, performance in MMLU and HellaSwag de-
clined post fine-tuning. MMLU, which requires
broad factual knowledge, dropped 3.95% from
29.05% to 25.10%, while HellaSwag, which in-
volves commonsense reasoning, saw a 2.41% de-
crease from 29.44% to 27.03%. This inconsistency
indicates that while fine-tuning aligned activations
for Malayalam, it did not translate uniformly into
downstream improvements across all tasks. The
decline in MMLU suggests a potential trade-off
where fine-tuning optimizes some linguistic repre-
sentations at the cost of factual recall.
These results highlight that activation alignment
does not equally translate into higher benchmark
scores. The observed improvement in ARC-C sug-
10

--- Page 11 ---\n\nLanguage
English Activation Retention (%)
Malayalam
90.40
Hindi
91.90
Marathi
92.81
Catalan
92.96
Indonesian
90.46
Italian
91.82
Spanish
91.02
Russian
90.70
Chinese
93.17
Table 6: English activation retention after fine-tuning.
Figure 5: Activation alignment for Malayalam across
various layers.
gests that fine-tuning enhanced reasoning abilities,
but the decline in MMLU and HellaSwag implies
that certain knowledge-intensive tasks may have
been negatively impacted. Future work could inves-
tigate whether task-specific fine-tuning strategies
or balancing activation alignment across layers can
lead to more consistent performance gains across
all benchmarks.
D
Cross-Linguistic Activation Disparities
From Figure 7, the results show a systematic dispar-
ity, with all languages consistently receiving lower
activations than English. Table 10 confirms that
this disparity persists across all layers. Addition-
ally, we observe variability across languages:
1. Malayalam and Marathi exhibit the largest ac-
tivation gaps, confirming that these languages are
underrepresented in feature space.
2. High-resource languages such as Chinese, Rus-
sian, and Spanish still show activation gaps, though
smaller than medium-to-low resource languages.
These findings reinforce that activation disparities
are a structural phenomenon in multilingual LLMs,
where medium-to-low resource languages system-
atically receive fewer learned representations. This
Layer
Malayalam Activation Improvement (%)
0
68.21
4
71.12
6
74.11
8
83.25
12
77.89
15
86.28
18
87.54
21
88.83
25
87.30
Table 7: Layer-wise activation improvement for Malay-
alam after fine-tuning.
Layer
English Activation Retention (%)
0
81.08
4
90.85
6
90.10
8
80.25
12
83.33
15
95.75
18
87.30
21
87.73
25
86.70
Table 8: Layer-wise English activation retention after
fine-tuning. The selected layers serve as checkpoints to
assess consistency across different depths.
under-representation likely contributes to perfor-
mance degradation on multilingual benchmarks.
From Figure 8, the results highlight a persistent
activation gap, where high-resource languages re-
ceive consistently higher activations than medium-
to-low resource languages across all layers. This
trend suggests systematic differences in how mul-
tilingual models process linguistic features, which
can be examined through the following key obser-
vations:
1. Early layers show the largest gap, reinforcing
that medium-to-low resource languages struggle to
activate neurons encoding foundational linguistic
features.
2. Disparities persist in deeper layers, indicating
that even though later representations are more ab-
stract and shared across languages, medium-to-low
resource languages still do not fully align with high-
resource languages in feature space.
3.
The separation between high-resource and
medium-to-low resource languages remains sta-
ble, suggesting that multilingual models inherently
prioritize high-resource languages at all levels of
11

--- Page 12 ---\n\nFigure 6: Benchmark performance across all tasks for
Malayalam after fine-tuning.
Benchmark
Score Type
Accuracy (%)
ARC-C
Original
26.34
Fine-Tuned
27.77
MMLU
Original
29.05
Fine-Tuned
25.10
HellaSwag
Original
29.44
Fine-Tuned
27.03
Table 9: Performance of Malayalam at layer 20 across
different benchmarks before and after fine-tuning.
representation.
These findings further support the hypothesis that
activation disparities contribute to cross-linguistic
performance gaps, as medium-to-low resource lan-
guages remain underrepresented in the model’s
learned feature space.
Language
Mean
Std
Chinese
0.33
0.32
Russian
0.30
0.31
Spanish
0.57
0.34
Italian
0.56
0.36
Indonesian
0.43
0.36
Catalan
0.35
0.33
Marathi
0.05
0.17
Malayalam
0.10
0.24
Hindi
0.12
0.25
Table 10: Mean and standard deviation of activation ra-
tios with English across all 26 layers for each language.
12

--- Page 13 ---\n\nFigure 7: Activation ratios across all layers and 4000 feature indices, comparing activation values for each language
relative to English.
Figure 8: Comparison of activation differences between high-resource and medium-to-low resource language
groups.
13

--- Page 14 ---\n\nFigure 9: Correlation between activation difference with
English and ARC-C accuracy across languages. Pear-
son’s correlation coefficient: r = −0.95.
Figure 10: Correlation between activation difference
with English and HellaSwag accuracy across languages.
Pearson’s correlation coefficient: r = −0.93.
Figure 11: Correlation between activation difference
with English and MMLU accuracy across languages.
Pearson’s correlation coefficient: r = −0.95.
14
\n```\n