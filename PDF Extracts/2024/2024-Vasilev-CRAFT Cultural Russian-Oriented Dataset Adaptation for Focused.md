---
title: "2024-Vasilev-CRAFT Cultural Russian-Oriented Dataset Adaptation for Focused - PDF Extract"
source_pdf: "2024-Vasilev-CRAFT Cultural Russian-Oriented Dataset Adaptation for Focused.pdf"
pages: 14
extracted_at: "2026-02-15T17:51:57.930144"
---

# PDF Extract: 2024-Vasilev-CRAFT Cultural Russian-Oriented Dataset Adaptation for Focused

**Source PDF:** 2024-Vasilev-CRAFT Cultural Russian-Oriented Dataset Adaptation for Focused.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

CRAFT: CULTURAL RUSSIAN-ORIENTED DATASET
ADAPTATION FOR FOCUSED TEXT-TO-IMAGE GENERATION
Viacheslav Vasilev1,2,∗,
Vladimir Arkhipkin1,
Julia Agafonova1,3,
Tatiana Nikulina1,
Evelina Mironova1,
Alisa Shichanina1,
Nikolai Gerasimenko1,
Mikhail Shoytov1,
Denis Dimitrov1,4
1 Sber AI, Moscow, Russia
2 Moscow Institute of Physics and Technology (MIPT), Moscow, Russia
3 Information Technologies, Mechanics and Optics University (ITMO University),
Saint-Petersburg, Russia
4Artificial Intelligence Research Institute (AIRI), Moscow, Russia
Corresponding author: vasilev.va@phystech.edu
ABSTRACT
Despite the fact that popular text-to-image generation models cope well with international and general
cultural queries, they have a significant knowledge gap regarding individual cultures. This is due
to the content of existing large training datasets collected on the Internet, which are predominantly
based on Western European or American popular culture. Meanwhile, the lack of cultural adaptation
of the model can lead to incorrect results, a decrease in the generation quality, and the spread of
stereotypes and offensive content. In an effort to address this issue, we examine the concept of
cultural code and recognize the critical importance of its understanding by modern image generation
models, an issue that has not been sufficiently addressed in the research community to date. We
propose the methodology for collecting and processing the data necessary to form a dataset based
on the cultural code, in particular the Russian one. We explore how the collected data affects the
quality of generations in the national domain and analyze the effectiveness of our approach using the
Kandinsky 3.1 text-to-image model. Human evaluation results demonstrate an increase in the level of
awareness of Russian culture in the model.
Keywords:
Cultural Code, Russian Culture, Dataset Adaptation, Text-to-Image Generation, Fine-tuning, Captioning,
Diffusion models, Data Engineering
1
Introduction
The use of image generation models for various purposes through online applications and web editors has become the
norm in modern daily life [1, 2, 3, 4, 5, 6, 7]. This increase in popularity and generation quality was made possible
by training models on data from the Internet and large open datasets of text-image pairs, such as LAION-5B [8], MS
COCO [9], etc. Much of this data allows models to learn a lot about international concepts, objects and events, and
some elements of those national cultures that are most represented in modern mass media [10]. This raises the problem
of a significant bias towards this data, often ignoring information that is represented in a smaller number of training
examples. Such data domains can be the cultural characteristics of certain social groups, peoples and residents of
different regions and states [11, 12]. As a result, such generative models do not take into account the cultural code of
arXiv:2505.04851v1  [cs.AI]  7 May 2025

--- Page 2 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
Figure 1: Comparison of Russian cultural code generations for popular text-to-image models. Reference is an
example of a real image with a specific entity. The cultural adaptation procedure we propose helps improve the quality
of cultural awareness for the Kandinsky 3.1 model, both in comparison with the previous version Kandinsky 2.2, and
for other models.
these groups well enough. Erroneous and incorrect generations in this case can lead to, at a minimum, an unsatisfactory
result, limited applicability of the model and partial loss of interest among users, and, at a maximum, to unintentional
insult, and the spread of stereotypes and social biases.
At the same time, it remains not entirely clear how to resolve the problem of cultural adaptation, since the concept of a
cultural code is rather vague. To the best of our knowledge, there is currently no significant research in the field of visual
content generation that would focus on working with the culture of a particular country or large enough community. The
goal of this work is to analyze the problem of cultural awareness lack in text-to-image models and propose a solution
that would move the field forward. We analyze the concept of a cultural code and describe a procedure for collecting
a dataset that would allow us to adapt a generation model to better understand the concepts of Russian, Soviet and
post-Soviet culture. We propose a CRAFT methodology (Cultural Russian-Oriented Dataset Adaptation for Focused
Text-to-Image Generation), emphasizing the general versatility of our approach.
Therefore, the contribution of this article is as follows:
• We expose the cultural awareness issues that current text-to-image generation models have. We discuss the
concept of cultural code and identify domains of visual data that we believe should be taken into account for
cultural adaptation of the model (Section 3).
• We propose and describe a methodology for collecting and processing a cultural-aware dataset, in particular
for Russian culture (Section 4).
• We analyze the effectiveness of our approach and explore how the collected data affects the quality of Russian
cultural data generation for the Kandinsky 3.1 model [6, 7]. We report human evaluation results where we
achieve higher quality compared to models lacking sufficient knowledge of Russian culture (Section 5).
2

--- Page 3 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
Figure 2: 17 main data categories for creating a dataset of the Russian cultural code. Examples for each category
are generated by the Kandinsky 3.1 model. For each category, we collect a set of visual entities from which we form
our dataset. As a result of additional training, the model increases its level of cultural awareness.
2
Related works
2.1. Generative Models Finetuning
Generative learning models in both natural language processing and computer vision are often pretrained on large
datasets, allowing them to have extensive general knowledge about texts or images in the real world. Various finetuning
methods, that is, additional training on a small dataset, can help expand the specific capabilities of the original models,
both in terms of improving the generation quality and solving new types of problems [13, 14, 15]. The key role here is
not even the quantity of additional data, but its quality and detailed description. For example, the work [16] shows that
finetuning, even on a small set of high-quality text-image data, can significantly improve the visual generation quality.
Also, finetuning a small number of parameters with a relatively small number of images with detailed descriptions
can significantly improve the quality of caption generation in visual-language models [17]. Additionally, finetuning a
model on additional data is also a key element for model enhancement approaches such as domain adaptation [18],
when the model is applied to data on which it was not pretrained, and AI alignment [19], when a certain behavior and
understanding are expected from the model. In this work, we focus on preparing a high-quality dataset that would
expand the text-to-image model’s generation capabilities beyond the international visual domain and at the same
time improve the visual quality of the generation of those national concepts that were already included in it at the
pretraining stage. We also expect the model to expand its understanding of complex, culture-specific concepts, mak-
ing it more relevant to the user who comes from a particular culture. In this sense, our work inherits the mentioned works.
2.2. Cultural Adaptation
By cultural awareness of a generation model we mean their ability to correctly resolve user requests and tasks that
reflect certain features inherent in a particular culture. Cultural adaptation refers to techniques that allow models
to achieve such results. Closely related to adaptation is the achievement of understanding linguistic and semantic
3

--- Page 4 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
Figure 3: General pipeline of our CRAFT method for cultural adaptation. We create a list of categories and entities
from Russian cultural code based on our own cultural analysis, collect and process data manually, including captioning
process. The resulting dataset is used for additional training of the text-to-image model Kandinsky 3.1 [6] to increase
its level of cultural awareness.
features [20], and the semantic matching of entities from different cultures [21], which has received attention in the
adaptive translation [22], offensive language detection [23, 24, 25], and cross-cultural natural language processing [26].
Metaphor understanding and cultural awareness are also important for dialogue agents who interact directly with users
[27]. The recent rise in the quality of multimodal architectures is driving interest in increasing cultural awareness for
visual-language models (VLM) in question answering [28], image-text retrieval and grounding [29]. Our work is one of
the first to extend cultural awareness for text-based visual content generation.
2.3. Ethics and Social Biases
Lack of cultural awareness for visual generation models can lead to the spread of social bias and offensive content
and pose risks comparable to those of using large language models (LLM) [30]. Many works have been devoted to
increasing the models’ knowledge of distribution by race, skin color, gender, and geography, as well as analyzing
and mitigating the social biases that were built into the model during pretraining stage [31, 32, 33, 34, 35]. Typically,
such studies view cultural stereotypes as undesirable artifacts and negative phenomena, aiming for a higher level of
globalization [36, 37]. Although we agree with previous work on this point, we argue that avoiding culture-specific
features may lead to even greater risks. In our work, on the contrary, we strive for cultural adaptation and enrichment of
knowledge about cultural characteristics in order to reduce the excessive influence of globalization or Western-culture
orientation, while maintaining correct behavior in terms of ethics and display of international concepts.
3
Preliminaries
3.1. Lack of Cultural Awareness of Text-to-Image Models
The lack of cultural awareness and biases towards international or Western culture in generative models, resulting
from the use of large datasets, has been noted previously [29, 32, 36, 37]. In this work, we focus on the performance
of text-to-image models in the context of generating entities that have a close connection with Russian culture. To
estimate the current level of Russian culture understanding by modern popular text-to-image models, we used relatively
simple prompts that reflect the most popular concepts of mass culture, widely known in the post-Soviet states. We
examine the performance of the DALL-E 3 [1], Midjourney V5.2 [2], Stable Diffusion XL [3], YandexART [4] and
Kandinsky 2.2 [5] models. Figure 1 demonstrates that these models often fail to correctly generate the expected
entities. It is worth noting that it is nevertheless impossible to talk about a complete lack of cultural awareness. Models
more often generate examples of generalized concepts consisting of individual recognizable elements, but do not
reflect the essence exactly as in the reference. We believe that even imprecise generation based on known elements
is not a satisfactory representation of the desired entity, since such examples may also lead to critical reactions from users.
3.2. What is the Cultural Code?
The cultural code is a complex concept at the intersection of cultural studies, sociology, philosophy, semiotics,
communication theory and other sciences. A cultural code of a particular group of people is shaped by symbolic systems
such as language, art, and tradition, as well as by the norms, values, social practices, and historical context. Media and
visual types of information also play a significant role in the formation of the cultural code [38]. We believe that in
order for generative models to interpret or create culturally relevant content, they must be trained to understand these
4

--- Page 5 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
Figure 4: The effect of filtering and custom captioning on the generation quality in Russian culture domain.
Reference image is a real image from the dataset that displays a specific entity. Our experiments showed that without
additional data processing the model generates unsatisfactory results.
codes. This will significantly improve the visual quality of generation for certain prompts, develop the interpretive and
communicative abilities of models, and allow the creation of systems that respect cultural differences, thereby avoiding
biases and promoting more ethical views.
In this paper we consider a special case of the Russian cultural code. Following previous works in this field [39, 40, 41,
42], we consider language, literature, art, religion, philosophy, folk traditions and history as fundamental factors in the
formation of Russian culture. Since the features of a particular culture are reflected in language [43], it is critical that the
model understands metaphors, proverbs, and figurative expressions from everyday, colloquial speech. From the point of
view of visual concepts, visual elements of modern popular culture, including cinema and television, and geographical
and natural features are also important to us. In order to select data based on the results of our own cultural analysis, we
created a list of 17 categories in which, we believe, the correct display of the visual cultural code is especially important.
See Figure 2 for the list of selected categories.
4
Cultural Dataset Adaptation
In this section, we describe the procedure for collecting and processing the dataset necessary for the cultural adaptation
of the text-to-image model Kandinsky 3.1 [6] in the context of the Russian cultural code. Figure 3 shows the general
scheme of the cultural adaptation process, each component of which we discuss in detail below.
4.1. Entities Determination & Data Collection
In this work, by “entity” we mean a specific concept or object belonging to the category of cultural code. For example,
the entities in the category “trees” are “spruce”, “birch”, “pine”, “oak”, etc. Categories such as “literature”
and “art” include the titles of books, paintings, literary characters, as well as the names of famous writers, poets,
artists, composers, and the like. For each category of Russian culture from the list we have defined, we have compiled a
table of the most popular entities.
Since we collected data from open sources on the Internet, for each entity we also defined a set of web queries in
Russian, which we automatically searched for relevant and correct data related to each entity. Thus, we manually
selected about 8 thousand entities. Examples of entities from our Russian cultural code dataset and a set of web queries
to them, translated into English, can be seen in Table 1.
4.2. Data Processing
We found that training the model on data collected from the Internet according to our entity lists produces unsatisfactory
results (Figure 4). This is explained by the fact that a large number of entities correspond to a small number of examples,
which, moreover, have low visual quality. Such examples include characters from old cartoons, movies, as well as
5

--- Page 6 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
Table 1: Examples of entities from different categories with corresponding web queries.
Entity
Web queries
Famous personalities
Yuri Gagarin
Yuri Alekseyevich Gagarin, cosmonaut Gagarin,
Gagarin in a helmet with the inscription USSR, Gagarin in an orange spacesuit
Movies and TV
Baron Munchausen
Baron Munchausen from “The Very Same Munchhausen”,
Baron Karl Friedrich Hieronymus von Münchhausen,
actor Oleg Ivanovich Yankovsky, film “The Very Same Munchhausen”
Literature
Maxim Gorky
Alexei Maximovich Peshkov, Maxim Gorky,
Alexei Maximovich Gorky, Jehudiel Khlamida
Holidays
Christmas
Nativity of Christ January 7 Orthodox holiday
National cuisine
Pirozhok
pirozhok with cabbage, pirozhok with meat, pirozhok with apples
Utensils
Samovar
Samovar, Russian samovar, ancient samovar, samovar-egg, samovar-flame,
samovar-jug, samovar-ball, samovar-rooster, samovar-barrel, samovar-jar,
samovar-vase, samovar-dula, samovar-pear, samovar-glass,
acorn samovar, store samovar, travel samovar
Technic
VAZ-2101
VAZ-2101, “Zhiguli”, “Zhiga”, “Zhigul”, “Kopeyka”, “Yedinichka”, “Odnerka”
Trees and plants
Birch
Birch, Betula pubescens, downy birch, Betula platyphylla,
Asian white birch, Betula raddeana, weeping birch, warty birch, Betula utilis
old photographs, illustrations, some paintings and portraits. In order to solve this problem, we manually filtered the
collected data, paying attention to the visual aesthetic of the images and their belonging to the Russian cultural code.
The key points in the instructions for filtering by culture code are as follows:
• If the images include elements of the cultures of other nations and nationalities from post-Soviet countries,
then such data is acceptable;
• If the images contain something modern or partly not belonging to Russian culture, but is present along with
elements of the Russian cultural code, then such data is acceptable;
• If the frame is from a film or TV series of non-Russian production, but it contains elements of Soviet and
Russian culture, then such data is acceptable;
• If the general appearance of the scene does not give clues as to whether there are actually elements of Russian
cultural code there, then such a scene is not acceptable.
Key points for quality filtering:
• Poor quality images (blurry, overexposed, low sharpness, or homemade) are not accepted. At the same time,
examples when good quality data does not exist for a particular entity should be processed separately;
• Images must not contain watermarks;
• Entities must not be distorted.
Each estimator got acquainted with negative and positive examples of which data should be selected. Examples of such
images are shown in Figure 5.
4.3. Captioning
Automatic captioning. After the initial filtering, we ran automatic captioning for the collected data using the LLaVa-
NeXT model [44]. To obtain the high quality captions, we varied the following hyperparameters:
• Maximum number of output tokens: from 100 to 1024. Setting a small value resulted in a truncated description,
or significant elements of the image were not revealed. We chose 512 tokens empirically.
6

--- Page 7 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
Table 2: Comparison of captions created by LLaVa-Next 34B [44] or people. The model quite often makes factual
mistakes and does not know the titles and proper names.
Image
LLaVa-Next 34B
Human
Cartoon character that looks like a pig.
The pig
is drawn in a simplistic, child-friendly style, with
bright outlines and flat colors.
She has a large
round head with two small black eyes and a small
triangular nose.
The pig’s mouth is open in a smile,
showing one tooth, he has two small ears and a tuft
of hair on the top of his head, the pig is wearing
a brown collared shirt, the background is a solid
color, bright green, the overall style is cheerful
and cartoonish, likely aimed at a younger audience.
A still from the cartoon “Orange
Cow”:
Bo the calf in an orange dress
with a dark border and Zo the calf
in an orange-brown overalls look in
surprise at the piglet.
The pig is
drawn in a simplified style:
it has a
large round head with two small black
eyes, a small round nose and a cute
smile.
The pig is wearing a brown
suit.
The background is bright green
with light-colored curls, large yellow
stars and small pink ones.
The scene is teeming with life, with numerous
figures and vehicles populating the street.
In
the foreground, a woman is seated in a car, her
back to the viewer, adding a sense of depth and
perspective to the composition.
The car is a
prominent feature, its details rendered with a
certain level of precision, contrasting with the more
abstract background.The background is a flurry of
activity, with buildings, cars, and people filling
the canvas.
The buildings, painted in warm hues,
tower over the scene, their details softened by the
artist’s brushstrokes.
The cars, rendered in cooler
tones, add a dynamic element to the composition,
their movement suggested through the artist’s use of
color and line.
The color palette is dominated by
warm tones, with the buildings and vehicles bathed
in a soft, diffused light.
The artist has used
a variety of brushstrokes, from loose and fluid
to more defined and structured, creating a sense
of movement and energy.Overall, the painting is
a beautiful representation of an urban landscape,
capturing the essence of city life through the lens
of impressionism.
The artist’s use of color, light,
and brushwork brings the scene to life, creating a
sense of movement and energy that is both captivating
and engaging.
Painting by Soviet artist Yuri Pimenov
“New Moscow”, which depicts a girl
with short hair, wearing blue clothes
with a white collar with long sleeves,
sitting behind the wheel, which she
holds with both hands, in an open-top
car, back to her shoulders; a narrow
windshield in a dark frame; a distant
view mirror is attached to the right
side of the glass.
To the left of
the car is a gray road; in the upper
left corner you can see a four-story
yellow building, as well as blue cars
and people crossing the road.
In
the upper right corner there are two
four-story yellow buildings, next
to which there are blue cars and
red-yellow buses, and people are
walking along the sidewalk on the
right.
The image depicts a person seated in a room with
a large window in the background, through which a
blurred view of trees can be seen.
The individual
is wearing a costume that appears to be inspired by
historical or fantasy attire.
The costume includes
a headpiece with intricate patterns and what seems
to be a beaded or embroidered veil that covers
the head and neck.
The person’s face is visible,
and they are looking directly at the camera with
a neutral expression.The costume consists of a
green, long-sleeved garment with a high collar and a
patterned chest area that includes what looks like
a heart or a floral motif.
The person is holding
a small, round object in their right hand, which
could be a fruit or a decorative item.The room has a
rustic feel, with a wooden floor and a zebra print
sofa or bench on which the person is seated.
The
table in front of the person holds a bowl with a
floral pattern, suggesting a setting for a meal or
a tea.
The overall style of the image is a blend
of historical fashion photography with a touch of
fantasy or costume drama.
The lighting is soft and
natural, enhancing the textures of the costume and
the room’s ambiance.
Photo of Uldus Bakhtiozina in an
outfit of his own design.
The girl
is wearing a light green silk dress,
on the front of which there is a
yellow insert with hearts on the
chest.
On the girl’s head is a large
golden kokoshnik with light patterns,
decorated with pearls.
The girl sits
on a black and white striped sofa,
behind which there is a large wooden
window, holding a knife in her right
hand, a potato in her left, and in
front of her there is a green saucepan
on a stool.
7

--- Page 8 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
Figure 5: Examples of images from the instructions that people followed when data filtering. The task was to select
only those images that contain Russian and post-Soviet visual features.
• Temperature. When the temperature was set to high (0.7-1), the model hallucinated and described objects that
were not in the image, or concentrated on insignificant elements.
• Instructional prompt.
We used 3 options: short (“Describe this image shortly in 1-2 short
sentences”),
medium
(“Please provide a caption for this image.
Speak confidently
and describe everything clearly.
Do not lie and describe only what you can see”)
and long (“Describe this image and its style in a very detailed manner”). A short prompt
did not allow generating meaningful captions, and a long one described non-existent objects. Thus, we chose
the middle option.
The generated captions were cleaned using regular expressions from service phrases and repeated initial sentences.
However, we have found that such captions often contain factual errors and do a poor job of understanding the Russian
cultural code. See Table 2 for examples. We conducted time measurements that showed that people spend an average of
4.52 minutes to create their own captions, and 5.23 minutes on editing a synthetic caption. Therefore, we have decided
to use only human-created captions.
Manual captioning. Empirically, we decided to create detailed captions from 2 to 10 sentences in length and according
to the following instructions:
• The greatest attention should be paid to the main entity;
• It is necessary to add the name of the character, the title of the book, movie, etc;
• Captions should be varied and not stick to one template;
• Phrases that suggest viewing an image should be avoided. For example, “we see in this photo”, “this
image shows”, etc;
• It is allowed to use phrases that characterize the features of the image. For example, “black and white
photo”, “still from a Soviet cartoon”, etc;
• Do not create descriptions that contain guesses about what this object in the image can be used for;
• Do not use imprecise language. For example, “the people in the image are probably young”;
• It is necessary to skip collage images and images that contain text.
All created captions were reviewed by another group of people according to the same instructions. In this way, we
collected about 200 thousand text-image pairs. To train the model, all captions were translated into English.
4.4. Data Duplication & Model Finetuning
At the final stage, we duplicated the dataset 50 times to expand those domains and entities for which there are only a
small number of high-quality training examples. Kandinsky 3.1 [6] finetuning took place in two stages. The first is in
768 × 768 resolution with batchsize = 4, and the second is in a mixed resolution of 7682 ≤W × H ≤10242 with a
batchsize = 1. The total number of steps is 500 thousand on 416 A100 GPU.
8

--- Page 9 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
Figure 6: Human evaluation results.
Figure 7: Examples of incorrect generation for some entities. Problems arise due to entities imbalance and translation
difficulties.
5
Evaluation
Since there are no benchmarks and automatic metrics for the task of Russian cultural adaptation of text-to-image
generation, we focused on conducting side-by-side human evaluation and collected our own set of 120 prompts,
reflecting the features of the Russian cultural code. 12 people took part in the comparisons and each chose the best
image according to the correspondence of the image content to the text prompt (text alignment) and the visual quality
of the image.
The results are presented in the Figure 6. As can be seen, Kandinsky 3.1 significantly outperforms the previous version
Kandinsky 2.2 [5], Midjourney 5.2 [2], SDXL [3] and Russian model YaART [4]. In comparison with the DALL-E 3
model [1], we demonstrate competitive results, the difference in which is small and can fluctuate depending on test
prompts and categories. The results of model generation before and after finetuning in Russian culture domain are
presented in Appendix.
9

--- Page 10 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
6
Limitations
Currently, the generation in the domain of cultural code has problems for those entities that are represented by a small
number of samples. For example, almost all available data on the appearance of characters in old films or cartoons are
low-quality frames. Almost all data on the Internet related to these entities are copies of these frames.
The second problem is translation difficulties. For example, due to the fact that the Russian word “cosmonaut” is often
translated into English as “astronaut”, most of the photographs of cosmonauts in the dataset are represented with the
American flag. The same applies to examples like “pirozhki-pies”, and other (Figure 7).
7
Conclusion
In this work, we are one of the first to propose an approach to enhance the cultural awareness of the text-to-image
generation model. We collected a dataset of Russian cultural code and used it to improve the generation quality in
this domain for our Kandinsky 3.1 model. Human evaluation of generation quality demonstrated the advantage of the
described methodology.
We believe that our approach deserves further development. First of all, we strive to conduct an even deeper cultural
analysis in order to expand the number of entities and data, including the semantic complexity of the test dataset. Our
next priorities include applying advanced augmentation and entity balancing techniques for the dataset, using RAG
[45, 46] for cultural adaptation, and extending our approach to text-to-video generation [47, 48]. We also pay close
attention to the ethical side of cross-cultural awareness and plan to develop advanced approaches to limit incorrect
queries while still leaving a sufficient level of freedom for users.
8
Later update
This research continues in our next paper, where we propose a benchmark for evaluating the level of Russian cultural
code understanding for text-to-image generation models [49]. For more details, please refer to the publication.
Acknowledgments
The authors express special gratitude to Igor Pavlov and Anastasia Lysenko, without whom this work would not have
been done. We also thank Sergey Markov, his team from SberDevices, and the prompt-engineering and markup team:
Anastasia Alyaskina, Nadezhda Martynova, Marina Yakushenko, Margarita Geberlein, Denis Kondratev, Stefaniya
Kozlova, Mikhail Kornilin, and Alexandra Averina.
References
[1] James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long Ouyang, Juntang Zhuang, Joyce
Lee, Yufei Guo, Wesam Manassra, Prafulla Dhariwa, Casey Chu, Yunxin Jiao, and Aditya Ramesh. Improving
image generation with better captions, 2023.
[2] Midjourney. Midjourney. https://www.midjourney.com/.
[3] Dustin Podell, Zion English, Kyle Lacey, Andreas Blattmann, Tim Dockhorn, Jonas Müller, Joe Penna, and Robin
Rombach. Sdxl: Improving latent diffusion models for high-resolution image synthesis, 2023.
[4] Sergey Kastryulin, Artem Konev, Alexander Shishenya, Eugene Lyapustin, Artem Khurshudov, Alexander
Tselousov, Nikita Vinokurov, Denis Kuznedelev, Alexander Markovich, Grigoriy Livshits, Alexey Kirillov,
Anastasiia Tabisheva, Liubov Chubarova, Marina Kaminskaia, Alexander Ustyuzhanin, Artemii Shvetsov, Daniil
Shlenskii, Valerii Startsev, Dmitrii Kornilov, Mikhail Romanov, Artem Babenko, Sergei Ovcharenko, and Valentin
Khrulkov. Yaart: Yet another art rendering technology, 2024.
[5] Anton Razzhigaev, Arseniy Shakhmatov, Anastasia Maltseva, Vladimir Arkhipkin, Igor Pavlov, Ilya Ryabov,
Angelina Kuts, Alexander Panchenko, Andrey Kuznetsov, and Denis Dimitrov. Kandinsky: an improved text-to-
image synthesis with image prior and latent diffusion, 2023.
[6] Vladimir Arkhipkin, Andrei Filatov, Viacheslav Vasilev, Anastasia Maltseva, Said Azizov, Igor Pavlov, Julia
Agafonova, Andrey Kuznetsov, and Denis Dimitrov. Kandinsky 3.0 technical report, 2024.
[7] Arkhipkin Vladimir, Viacheslav Vasilev, Andrei Filatov, Igor Pavlov, Julia Agafonova, Nikolai Gerasimenko,
Anna Averchenkova, Evelina Mironova, Bukashkin Anton, Konstantin Kulikov, Andrey Kuznetsov, and Denis
10

--- Page 11 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
Dimitrov. Kandinsky 3: Text-to-image synthesis for multifunctional generative framework. In Delia Irazu
Hernandez Farias, Tom Hope, and Manling Li, editors, Proceedings of the 2024 Conference on Empirical Methods
in Natural Language Processing: System Demonstrations, pages 475–485, Miami, Florida, USA, November 2024.
Association for Computational Linguistics.
[8] Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo
Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, Patrick Schramowski, Srivatsa Kundurthy, Katherine
Crowson, Ludwig Schmidt, Robert Kaczmarczyk, and Jenia Jitsev. Laion-5b: An open large-scale dataset for
training next generation image-text models. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and
A. Oh, editors, Advances in Neural Information Processing Systems, volume 35, pages 25278–25294. Curran
Associates, Inc., 2022.
[9] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and
C. Lawrence Zitnick. Microsoft coco: Common objects in context. In David Fleet, Tomas Pajdla, Bernt Schiele,
and Tinne Tuytelaars, editors, Computer Vision – ECCV 2014, pages 740–755, Cham, 2014. Springer International
Publishing.
[10] Shreya Shankar, Yoni Halpern, Eric Breck, James Atwood, Jimbo Wilson, and D. Sculley. No classification
without representation: Assessing geodiversity issues in open data sets for the developing world, 2017.
[11] Terrance DeVries, Ishan Misra, Changhan Wang, and Laurens van der Maaten. Does object recognition work for
everyone?, 2019.
[12] Laura Gustafson, Megan Richards, Melissa Hall, Caner Hazirbas, Diane Bouchacourt, and Mark Ibrahim.
Pinpointing why object recognition performance degrades across income levels and geographies, 2023.
[13] Alec Radford and Karthik Narasimhan. Improving language understanding by generative pre-training, 2018.
[14] Tero Karras, Miika Aittala, Janne Hellsten, Samuli Laine, Jaakko Lehtinen, and Timo Aila. Training generative
adversarial networks with limited data, 2020.
[15] Alex Nichol, Prafulla Dhariwal, Aditya Ramesh, Pranav Shyam, Pamela Mishkin, Bob McGrew, Ilya Sutskever,
and Mark Chen. Glide: Towards photorealistic image generation and editing with text-guided diffusion models,
2022.
[16] Xiaoliang Dai, Ji Hou, Chih-Yao Ma, Sam Tsai, Jialiang Wang, Rui Wang, Peizhao Zhang, Simon Vandenhende,
Xiaofang Wang, Abhimanyu Dubey, Matthew Yu, Abhishek Kadian, Filip Radenovic, Dhruv Mahajan, Kunpeng
Li, Yue Zhao, Vladan Petrovic, Mitesh Kumar Singh, Simran Motwani, Yi Wen, Yiwen Song, Roshan Sumbaly,
Vignesh Ramanathan, Zijian He, Peter Vajda, and Devi Parikh. Emu: Enhancing image generation models using
photogenic needles in a haystack, 2023.
[17] Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny. Minigpt-4: Enhancing vision-language
understanding with advanced large language models, 2023.
[18] Peeyush Singhal, Rahee Walambe, Sheela Ramanna, and Ketan Kotecha. Domain adaptation: Challenges,
methods, datasets, and applications. IEEE Access, 11:6973–7020, 2023.
[19] Jiaming Ji, Tianyi Qiu, Boyuan Chen, Borong Zhang, Hantao Lou, Kaile Wang, Yawen Duan, Zhonghao He, Jiayi
Zhou, Zhaowei Zhang, Fanzhi Zeng, Kwan Yee Ng, Juntao Dai, Xuehai Pan, Aidan O’Gara, Yingshan Lei, Hua
Xu, Brian Tse, Jie Fu, Stephen McAleer, Yaodong Yang, Yizhou Wang, Song-Chun Zhu, Yike Guo, and Wen Gao.
Ai alignment: A comprehensive survey, 2024.
[20] Haryo Akbarianto Wibowo, Erland Hilman Fuadi, Made Nindyatama Nityasya, Radityo Eko Prasojo, and
Alham Fikri Aji. Copal-id: Indonesian language reasoning with local culture and nuances. arXiv preprint
arXiv:2311.01012, 2023.
[21] Yong Cao, Yova Kementchedjhieva, Ruixiang Cui, Antonia Karamolegkou, Li Zhou, Megan Dare, Lucia Donatelli,
and Daniel Hershcovich. Cultural Adaptation of Recipes. Transactions of the Association for Computational
Linguistics, 12:80–99, 01 2024.
[22] Denis Peskov, Viktor Hangya, Jordan Boyd-Graber, and Alexander Fraser. Adapting entities across languages and
cultures. In Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih, editors, Findings
of the Association for Computational Linguistics: EMNLP 2021, pages 3725–3750, Punta Cana, Dominican
Republic, November 2021. Association for Computational Linguistics.
[23] Li Zhou, Laura Cabello, Yong Cao, and Daniel Hershcovich. Cross-cultural transfer learning for Chinese offensive
language detection. In Sunipa Dev, Vinodkumar Prabhakaran, David Adelani, Dirk Hovy, and Luciana Benotti,
editors, Proceedings of the First Workshop on Cross-Cultural Considerations in NLP (C3NLP), pages 8–15,
Dubrovnik, Croatia, May 2023. Association for Computational Linguistics.
11

--- Page 12 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
[24] Li Zhou, Antonia Karamolegkou, Wenyu Chen, and Daniel Hershcovich. Cultural compass: Predicting transfer
learning success in offensive language detection with cultural features. In Houda Bouamor, Juan Pino, and Kalika
Bali, editors, Findings of the Association for Computational Linguistics: EMNLP 2023, pages 12684–12702,
Singapore, December 2023. Association for Computational Linguistics.
[25] Md Rabiul Awal, Roy Ka-Wei Lee, Eshaan Tanwar, Tanmay Garg, and Tanmoy Chakraborty. Model-agnostic
meta-learning for multilingual hate speech detection. IEEE Transactions on Computational Social Systems,
11(1):1086–1095, 2024.
[26] Daniel Hershcovich, Stella Frank, Heather Lent, Miryam de Lhoneux, Mostafa Abdou, Stephanie Brandl,
Emanuele Bugliarello, Laura Cabello Piqueras, Ilias Chalkidis, Ruixiang Cui, Constanza Fierro, Katerina Mar-
gatina, Phillip Rust, and Anders Søgaard. Challenges and strategies in cross-cultural NLP. In Smaranda Muresan,
Preslav Nakov, and Aline Villavicencio, editors, Proceedings of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), pages 6997–7013, Dublin, Ireland, May 2022. Association
for Computational Linguistics.
[27] Yong Cao, Min Chen, and Daniel Hershcovich. Bridging cultural nuances in dialogue agents through cultural value
surveys. In Yvette Graham and Matthew Purver, editors, Findings of the Association for Computational Linguistics:
EACL 2024, pages 929–945, St. Julian’s, Malta, March 2024. Association for Computational Linguistics.
[28] Federico Becattini, Pietro Bongini, Luana Bulla, Alberto Del Bimbo, Ludovica Marinucci, Misael Mongiovì, and
Valentina Presutti. Viscounth: A large-scale multilingual visual question answering dataset for cultural heritage.
ACM Trans. Multimedia Comput. Commun. Appl., 19(6), jul 2023.
[29] Mehar Bhatia, Sahithya Ravi, Aditya Chinchure, Eunjeong Hwang, and Vered Shwartz. From local concepts to
universals: Evaluating the multicultural understanding of vision-language models, 2024.
[30] Amelia Katirai, Noa Garcia, Kazuki Ide, Yuta Nakashima, and Atsuo Kishimoto. Situating the social issues of
image generation models in the model life cycle: a sociotechnical approach. AI and Ethics, July 2024.
[31] Nassim Dehouche. Implicit stereotypes in pre-trained classifiers. IEEE Access, 9:167936–167947, 2021.
[32] Ranjita Naik and Besmira Nushi. Social biases through the text-to-image generation lens. In Proceedings of the
2023 AAAI/ACM Conference on AI, Ethics, and Society, AIES ’23, page 786–808, New York, NY, USA, 2023.
Association for Computing Machinery.
[33] Yue Yu, Yuchen Zhuang, Jieyu Zhang, Yu Meng, Alexander J Ratner, Ranjay Krishna, Jiaming Shen, and Chao
Zhang. Large language model as attributed training data generator: A tale of diversity and bias. In A. Oh,
T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, Advances in Neural Information
Processing Systems, volume 36, pages 55734–55784. Curran Associates, Inc., 2023.
[34] Abeba Birhane, Sepehr Dehdashtian, Vinay Prabhu, and Vishnu Boddeti. The dark side of dataset scaling:
Evaluating racial classification in multimodal models. In Proceedings of the 2024 ACM Conference on Fairness,
Accountability, and Transparency, FAccT ’24, page 1229–1244, New York, NY, USA, 2024. Association for
Computing Machinery.
[35] Colton Clemmer, Junhua Ding, and Yunhe Feng. Precisedebias: An automatic prompt engineering approach
for generative ai to mitigate image demographic biases. In Proceedings of the IEEE/CVF Winter Conference on
Applications of Computer Vision (WACV), pages 8596–8605, January 2024.
[36] Hugo Berg, Siobhan Hall, Yash Bhalgat, Hannah Kirk, Aleksandar Shtedritski, and Max Bain. A prompt array
keeps the bias away: Debiasing vision-language models with adversarial learning. In Yulan He, Heng Ji, Sujian
Li, Yang Liu, and Chua-Hui Chang, editors, Proceedings of the 2nd Conference of the Asia-Pacific Chapter of
the Association for Computational Linguistics and the 12th International Joint Conference on Natural Language
Processing (Volume 1: Long Papers), pages 806–822, Online only, November 2022. Association for Computational
Linguistics.
[37] Lukas Struppek, Dom Hintersdorf, Felix Friedrich, Manuel br, Patrick Schramowski, and Kristian Kersting.
Exploiting cultural biases via homoglyphs in text-to-image synthesis. J. Artif. Int. Res., 78, jan 2024.
[38] John Corner. Codes and cultural analysis. Media, Culture & Society, 2(1), 1980.
[39] Mikhail Goloubkov. Literature and the russian cultural code at the beginning of the 21st century. Journal of
Eurasian Studies, 4(1):107–113, 2013. 20 Years of the Collapse of the Fomer Soviet Union.
[40] James Billington. The icon and axe: An interpretative history of Russian culture. Vintage, 2010.
[41] Orlando Figes. Natasha’s dance: A cultural history of Russia. Macmillan, 2002.
[42] Richard Stites. Russian popular culture: Entertainment and society since 1900. Cambridge University Press,
1992.
12

--- Page 13 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
[43] Anna Wierzbicka. Russian cultural scripts: The theory of cultural scripts and its applications. Ethos, 30(4):401–
432, 2002.
[44] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning, 2023.
[45] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich
Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, and Douwe Kiela. Retrieval-augmented
generation for knowledge-intensive nlp tasks. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin,
editors, Advances in Neural Information Processing Systems, volume 33, pages 9459–9474. Curran Associates,
Inc., 2020.
[46] Penghao Zhao, Hailin Zhang, Qinhan Yu, Zhengren Wang, Yunteng Geng, Fangcheng Fu, Ling Yang, Wentao
Zhang, Jie Jiang, and Bin Cui. Retrieval-augmented generation for ai-generated content: A survey, 2024.
[47] Vladimir Arkhipkin, Zein Shaheen, Viacheslav Vasilev, Elizaveta Dakhova, Andrey Kuznetsov, and Denis Dimitrov.
Fusionframes: Efficient architectural aspects for text-to-video generation pipeline, 2023.
[48] Vladimir Arkhipkin, Zein Shaheen, Viacheslav Vasilev, Elizaveta Dakhova, Konstantin Sobolev, Andrey Kuznetsov,
and Denis Dimitrov. Improveyourvideos: Architectural improvements for text-to-video generation pipeline. IEEE
Access, 13:1986–2003, 2025.
[49] Viacheslav Vasilev, Julia Agafonova, Nikolai Gerasimenko, Alexander Kapitanov, Polina Mikhailova, Evelina
Mironova, and Denis Dimitrov. RusCode: Russian cultural code benchmark for text-to-image generation. In Luis
Chiruzzo, Alan Ritter, and Lu Wang, editors, Findings of the Association for Computational Linguistics: NAACL
2025, pages 7641–7657, Albuquerque, New Mexico, April 2025. Association for Computational Linguistics.
Appendix
Figure 8: An example of generations by the Kandinsky 3.1 model in the Russian culture domain before and after
cultural adaptation via finetuning.
Figure 9: An example of generations by the Kandinsky 3.1 model in the Russian culture domain before and after
cultural adaptation via finetuning.
13

--- Page 14 ---

CRAFT: Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation
Figure 10: An example of generations by the Kandinsky 3.1 model in the Russian culture domain before and after
cultural adaptation via finetuning.
Figure 11: An example of generations by the Kandinsky 3.1 model in the Russian culture domain before and after
cultural adaptation via finetuning.
Figure 12: An example of generations by the Kandinsky 3.1 model in the Russian culture domain before and after
cultural adaptation via finetuning.
14

```
