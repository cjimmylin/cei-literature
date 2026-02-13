---
title: "2024-Singla-Samayik A Benchmark and Dataset for - PDF Extract"
source_pdf: "2024-Singla-Samayik A Benchmark and Dataset for.pdf"
pages: 7
extracted_at: "2026-02-13T09:15:44.419985"
---

# PDF Extract: 2024-Singla-Samayik A Benchmark and Dataset for

**Source PDF:** 2024-Singla-Samayik A Benchmark and Dataset for.pdf
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

Sāmayik: A Benchmark and Dataset for English-Sanskrit
Translation
Ayush Maheshwari1∗, Ashim Gupta2, Amrith Krishna3, Atul Kumar Singh4,
Ganesh Ramakrishnan4, G. Anil Kumar5, Jitin Singla5
1Vizzhy Inc Bengaluru, 2University of Utah, 3Learno.ai,
4Indian Institute of Technology Bombay, 5Indian Institute of Technology Roorkee
Abstract
We release Sāmayik, a dataset of around 53,000 parallel English-Sanskrit sentences, written in contemporary prose.
Sanskrit is a classical language still in sustenance and has a rich documented heritage. However, due to the lim-
ited availability of digitized content, it still remains a low-resource language. Existing Sanskrit corpora, whether
monolingual or bilingual, have predominantly focused on poetry and offer limited coverage of contemporary writ-
ten materials. Sāmayik is curated from a diverse range of domains, including language instruction material, textual
teaching pedagogy, and online tutorials, among others. It stands out as a unique resource that specifically caters to
the contemporary usage of Sanskrit, with a primary emphasis on prose writing. Translation models trained on our
dataset demonstrate statistically significant improvements when translating out-of-domain contemporary corpora,
outperforming models trained on older classical-era poetry datasets. Finally, we also release benchmark models
by adapting four multilingual pre-trained models, three of them have not been previously exposed to Sanskrit for
translating between English and Sanskrit while one of them is multi-lingual pre-trained translation model including
English and Sanskrit. The dataset and source code is present at https://github.com/ayushbits/saamayik.
1.
Introduction
We release Sāmayik, an English-Sanskrit parallel
dataset, that covers the contemporary usage of
Sanskrit, written in prose. Sāmayik is a Sanskrit
term that translates to the “sayings of the contem-
porary world”. Sāmayik
consists of 52,961 par-
allel sentence pairs, collected from five different
sources. These are spoken content that covers
contemporary world affairs, interpretation of liter-
ary works, pedagogical content, etc.
‘Itihāsa’ currently forms the largest parallel ma-
chine translation corpus in English-Sanskrit (Ara-
likatte et al., 2021). This Sanskrit-English dataset
comprises 93,000 pairs of verses in Sanskrit
along with their corresponding English translations.
These Sanskrit verses belong to Rāmāyaṇa and
Mahābhārata written in the poetry form and belong
to the classical era literature.
Sanskrit is estimated to have around 30 mil-
lion extant manuscripts fit for digitization. More-
over, it has more than two million active speakers
(McCartney, 2019; Chandramouli, 2011). Despite
its rich heritage, Sanskrit remains classified as a
low-resource language with no more than one mil-
lion monolingual sentences available in the digi-
tized form (Hellwig, 2010–2021; Maheshwari et al.,
2022). The available digitized corpora for Sanskrit
are vastly diverse not just in terms of the domains
and chronology they span, but also in terms of
the usage, stylistic features, the underlying syntax
(Hellwig, 2009), and even the typological charac-
*Outcome of research while pursuing PhD at IIT
Bombay.
Correspondence: {ayusham, ganesh}@cse.iitb.ac.in
teristics such as word order (Krishna et al., 2021;
Tubb and Boose, 2007).
Sentence constructions in Sanskrit follow rela-
tively free word order. Here, sentences written in
verse form have to adhere to prescribed meter pat-
terns as per prosody. Hence, word order need not
adhere to a fixed word-order pattern.
However,
sentences written in prose tend to form Subject-
Object-Verb (SOV) ordering.
Ithihāsa and other
monolingual available corpora predominantly rep-
resent content written in poetry form. Content writ-
ten in prose is generally underrepresented in avail-
able digitized corpora in Sanskrit, especially those
written in the contemporary era. To bridge this gap
we release Sāmayik.
Sāmayik is a parallel Sanskrit-English dataset
encompassing multiple contemporary corpora,
providing a comprehensive representation of the
contemporary usage of Sanskrit. In Section 2, we
provide a detailed description of each source in-
cluded in our dataset, and Table 1 presents an
overview of the statistics for each source.
The
latest corpus in our collection contains content as
recent as 2022, from an ongoing podcast series
‘Mann Ki Baat’. The oldest corpus in our collec-
tion is the English-Sanskrit Bible, where the San-
skrit translation was performed in 1851 and it forms
less than 14% of the overall dataset. The Sanskrit
component in the rest of the corpora is composed
either in the latter half of the twentieth century or
in the current century.
In addition to our dataset, we release three
benchmarks by adapting pre-trained models for
neural machine translation in English-Sanskrit and
vice-versa. Here, we adapt four pre-trained multi-

--- Page 2 ---

lingual seq2seq models for the task, namely ByT5
(Xue et al., 2022), mBART (Liu et al., 2020), In-
dicBART (Dabre et al., 2022), and Indictrans (Gala
et al., 2023). Except Indictrans, none of the mod-
els were exposed to Sanskrit during their pretrain-
ing stage where Indictrans is a multi-lingual trans-
lation model including English and Sanskrit.
2.
Sāmayik
Sāmayik is an English-Sanskrit machine transla-
tion dataset, consisting of 52,941 sentences from
five different corpora.
The aim of the dataset
is to include translation pairs containing Sanskrit
prose written in the modern era.
We hired sev-
eral professional English and Sanskrit linguistic ex-
perts for the purpose of translation and alignment
for the development of the dataset. The educa-
tional qualifications of the experts range from a
Master’s degree to a Ph.D. The experience of the
experts ranged from 3-20 years, with the more
experienced ones assigned the job of translation
while junior members were assigned the job of sen-
tence alignment. The experts were paid as per the
norms laid out by the norms set by the Government
of India. Below, we give a brief description of each
of the datasets involved and the steps involved in
processing these sentences.
1. Bible - The New Testament: We release the
New Testament of the Bible aligned with its cor-
responding English version. We use the Sanskrit
version released by Calcutta Baptist Missionaries,
originally published in 18511.
The New Testa-
ment contains 7,838 sentences from 260 chapters.
Each verse is generally indexed by the book name,
and chapter name followed by the verse number.
For the English version of the Bible, we rely on
Christodouloupoulos and Steedman (2015) where
the English sentences also follow the same index-
ing form. Given the one-to-one correspondences
at the sentence level for both English and Sanskrit
sentences, the mapping was straightforward. We
finally obtained a total of 7,838 parallel sentences.
Further, three fluent speakers of both English and
Sanskrit have verified the alignments for of 100
sentences, randomly sampled from the corpus.
2.
Mann ki Baat (MKB)2 - MKB is an ongo-
ing monthly radio podcast hosted by the Prime
Minister of India, which resumed its broadcast in
2014. Each episode is an address to the nation dis-
cussing social, cultural, and contemporary topics
including conversation with individuals. Sanskrit
translations by experts, albeit unoﬀicial, are avail-
1https://www.bible.com/bible/2104/MAT.
1.SAN-DN
2https://pmonradio.nic.in/
able in public domain3. We use these expert trans-
lations and manually align Sanskrit sentences with
oﬀicial English transcripts from 25 episodes. Addi-
tionally, these Sanskrit translations are further ver-
ified by 3 in-house language experts. The MKB
English-Sanskrit corpus Sāmayik release consists
of 4,047 sentences with a total of 47,843 words.
3. Gītā Sopānaṁ - Gītā Sopānaṁ is a book pub-
lished by ‘Samskrita Bharati’ in 2009 for teaching
Sanskrit to beginners. It consists of a total of 6130
sentences. As observable in Table 1, the count
of unique words is just 6465 for these 6130 sen-
tences. Gītā Sopānaṁ is a self-learning book tar-
geted at beginners and enables them to learn San-
skrit through stories. It often contains simple and
small sentences with a focus on learning the gram-
mar instead of expanding vocabulary. We perform
in-house translation of the work to English sen-
tences with the help of 4 language experts well-
versed in both English and Sanskrit.
Given the
expert-level annotations, we only gather one trans-
lation per Sanskrit sentence. In summary, each
expert annotated around 1500 sentences.
4.
Spoken Tutorials4 - Spoken Tutorial project
is a large corpus of video tutorials for training stu-
dents to use open-source software. These tutori-
als are created by domain experts and translated
into several languages by expert translators. We
scraped5 videos and transcripts from their website
for which both English and the corresponding San-
skrit translations are available. We extracted tran-
scripts of 254 videos where each video is an of
average 10 minutes in duration. The transcripts
are manually created and, therefore, do not require
additional sentence segmentation. The alignment
between the English and the corresponding sen-
tences for each transcript was performed manu-
ally with the help of 5 linguistic experts. We ask
experts to align English and Sanskrit sentences
from the transcripts and merge sentences if one-to-
one correspondence is not present. Each expert
aligned around 5,000 sentences. The final corpus
contains 23,835 sentences comprising 237,449
words.
5. NIOS - The National Institute of Open School-
ing (NIOS) is a national-level board of education
in India established in 1989.
NIOS prints self-
instructional study materials for various subjects
up to the senior secondary education level. We
obtained the study materials from the Indian knowl-
edge tradition courses offered by NIOS, which are
3https://sanskritdocuments.org/sites/
manogatam/
4https://spoken-tutorial.org/
5The website content is licensed under CC4.0 li-
cense.

--- Page 3 ---

Dataset
NIOS
Spoken Tutorials
GitaSopanam
Bible
Mann Ki Baat
Total
#sentences
11356
23835
5885
7838
4047
52941
#words
105178
237449
26135
102508
47843
518842
#unique words
30966
38373
6513
38359
20484
122349
% of unique words
29.4
16.2
24.9
37.4
42.8
23.6
Mean word length
9.3
10
4.5
13.1
11.8
9.8
Table 1: Number of sentences, words, unique words and average word length for different corpus in
Sāmayik.
available in both English and Sanskrit6.
Each
course consists of multiple topics accessible in the
form of PDF files. We use PDF parsers to convert
PDF content in text format, without loss of infor-
mation. We hired a team of five English and San-
skrit linguistic experts who aligned the sentences
from the corresponding text files. NIOS contains
11,356 parallel sentences with 105,178 total words
and 30,966 unique words.
3.
Experiments
3.1.
Systems
1.
mBART (Liu et al., 2020):
is a multilin-
gual pretrained seq2seq model trained using sim-
ilar objective as employed in BART (Lewis et al.,
2020). We employ mbart-large-50-many-to-many-
mmt, trained on a large multilingual corpus of 50
languages, for our experiments. The vocabulary
size of the pre-trained model is 250K and maxi-
mum sequence length of 1024 with 610M parame-
ters.
2. IndicBART (Dabre et al., 2022) is a multilingual
pretrained seq2seq model with 244M parameters
trained using the pre-training objective of BART.
IndicBART was trained using corpora from Indic
languages and English. While different Indic lan-
guages use different scripts, these are losslessly
converted to Devanagari before tokenization dur-
ing its pretraining. Hence, we use the Devanagari
script for encoding Sanskrit, and Roman script for
English.
3.
ByT5 (Xue et al., 2022) is a token free pre-
trained seq2seq model following the pre-training
objective of mT5 (Xue et al., 2021). However, here
it is a token-free model that uses a fixed 256-byte
value in Unicode as its vocabulary.
From prior
work (Maheshwari et al., 2022), we observe that
the use of the Devanagari script in Unicode to en-
code content in Sanskrit leads to the best results.
We use a base version of ByT5 in our experiments
which consists of 582M parameters where UTF-8
bytes are directly fed into the model without any
6https://www.nios.ac.in/
online-course-material/
indian-knowledge-tradition.aspx
text pre-processing.
4. IndicTrans (Gala et al., 2023) is a multi-lingual
translation model trained on 22 Indic languages
including Sanskrit.
The multi-lingual model is
trained with the English-Sanskrit bi-text pairs. The
NLLB corpora of 3M sentences were filtered to re-
move noisy sentence pairs. The sentence pairs
were filtered using margin-based scoring that finds
the closest semantic match between the pairs of
source and target sentences. Finally, the model
is trained with a dataset size of 244,367 English-
Sanskrit bi-lingual sentence pairs. The model is
trained with the transformer architecture compris-
ing of 18 encoder and 18 decoder layers with the
feedforward dimension of 8192, and 16 attention
heads.
The model uses sub-word tokenization
with the maximum vocab size of 32K for English-
Sanskrit and 128K for Sanskrit-English models
and parameter count of 1.1B. We fine-tune the
English-Sanskrit and Sanskrit-Eng model with Sā-
mayik corpus.
3.2.
Experimental Setup
Metrics: We evaluate the performance of the mod-
els on both BLEU (Papineni et al., 2002) and
ChrF (Popović, 2015).
BLEU is a word-level n-
gram precision-based metric whereas ChrF is a
character-level n-gram F-score. Here, given that
Sanskrit is a morphologically rich language with
more than 1,400 possible inflected forms (Krishna
et al., 2021), we believe ChrF can be indicative of
capturing morpho-syntactic aspects.
Data: Due to the relatively low availability of the
data, we consider 90% of sentence pairs from
the four corpora NIOS, Spoken Tutorial (ST), Gita
Sopanam (GS), and Bible as our training set and
the rest as our in-domain evaluation set. The eval-
uation set is equally split into development and test
set. To evaluate the performance of our model on
a completely different domain test set, we reserve
Mann Ki Baat(MKB) as an out-of-domain test set,
implying that MKB was not included in the training
data.
Implementation Details:
All models are fine-
tuned from their pre-trained checkpoints using
HuggingFace Transformers (Wolf et al., 2020).
Both source and target sequences are truncated

--- Page 4 ---

En-Sa
Sa-En
Model
BLEU
ChrF
BLEU
ChrF
ByT5
28.7
44.4
31.1
55.7
mBART
27.20
46.61
11.6
27.0
IndicBART
25.45
43.47
29.79
50.14
Indictrans
11.3
46.6
37
58.2
Table 2: Results for different models on the in-
domain test set for En-Sa and Sa-En direction.
En-Sa
Sa-En
Model
BLEU
ChrF
BLEU
ChrF
ByT5
7
21.4
5.4
29
mBART
7.11
22.6
-
-
IndicBART
6.9
22.4
5.3
27.7
Indictrans
0.6
26.7
13.1
37.5
Google Trans
1.9
35
13.9
44.7
NLLB
1.2
27.6
11.5
36.1
Indictrans(Vanilla)
1.2
34
14.5
42.7
Table 3: Results for out-of-domain test set, namely,
Mann Ki Baat (MKB) for En-Sa and Sa-En direc-
tions. We omit mBART due to poor performance
on in-domain test split (refer Table 2).
Perfor-
mance reported on the Google Translate, NLLB
and Indictrans (Vanilla) (below double horizontal
line) refers to the evaluation with pre-trained mod-
els.
at 512 token lengths and set the batch size to
128.
We use the standard cross entropy loss
with label smoothing of 0.1 and AdamW optimizer
(Loshchilov and Hutter). All model are trained for
a maximum of 30 epochs with a batch size of 16,
learning rate of 1e-3, label smoothing factor of 0.1
and weight decay of 1e-4.
For IndicTrans, the
learning rate is set to 1e-4, dropout is 0.2 and max-
imum tokens per batch of 1024 and patience of
early stopping was set to 5.
3.3.
Results
Table 2 shows the performance of all four systems
on the in-domain test set. These systems are fine-
tuned on the in-domain training data. As it can
be observed from the table, different models per-
form the best depending on the direction of the
translation. Here, mBART reports the best results
for English-Sanskrit (En-Sa) translation, whereas
Indictrans performs the best for Sanskrit-English
(Sa-En) translation. Despite being pre-trained on
significant amount of English-Sanskrit parallel cor-
pus, Indictrans reports lower scores for En-Sa di-
rection. However, model reports better scores on
Sa-En direction. We hypothesise this can be at-
tributed to the high morphological characteristics
of the Sanskrit language which prevents fair eval-
uation using existing metrics.
ByT5 reports the
Model
IndicBART
mBART
Dataset
BLEU
ChrF
BLEU
ChrF
Itihasa
4.6
16
4.3
16.7
Sāmayik
6.3
23.2
7.3
22.3
Itihasa + Sāmayik
6.9
22.4
6.8
21.6
Table 4: Comparison between existing dataset Iti-
hasa, Sāmayik and Itihasa + Sāmayik on MKB out-
of-domain testset for English-Sanskrit translation
direction.
The score difference between Itihasa
(1st row) and Sāmayik(2nd row) are statistically
significant at p<0.05.
second best results for En-Sa, though on an aver-
age it requires more than five times the sequence
length than that of the other models. Here, ByT5
reports a sequence length of 156.99, as against
30 for the model with the next longest sequence
length, mBART. The disparity in sequence length
arises out of the tokenizers used in ByT5 which is
at a Unicode byte level against the subword tok-
enizers used in the other models.
We perform a zero-shot evaluation using MKB,
on our out-of-domain test data, not just on the four
systems fine-tuned on Sāmayik, but also on three
publicly available systems, namely Google trans-
late (GT) service7, NLLB-200 1.3B variant8, and
IndicTrans with no fine-tuning. As shown in Table
3, GT outperforms all other systems by a consider-
able margin in the Sa-En direction, though a sig-
nificant drop is observed in the En-Sa direction.
However, for the En-Sa direction, our fine-tuned
version of mBART performs the best in terms of
BLEU and our fine-tuned version of Indictrans in
terms of ChrF.
The considerable drop in performance on the in-
domain dataset may be attributed to the vocabu-
lary diversity generally observed in Sanskrit cor-
pora.
Sanskrit corpora tend to have a long tail
of rare words within the corpus.
Further, owing
to high lexical productivity both with compounding
and derivation, these corpora tend to have a di-
verse vocabulary for one another. Both the long
tail of rare words and rich compounding are chal-
lenging for models, similar to the current NMT mod-
els, that rely on distributional semantics.
‘Contemporyness’ forms a key factor for the cor-
pora in Sāmayik. Table 4 shows the performance
on MKB in En-Sa translation on the mBART and
IndicBART, fine-tuned using an alternate publicly
available dataset ‘Itihasa’. Here, Itihasa has nearly
double the number of training instances than Sā-
mayik.
In spite of it, models fine-tuned on Sā-
7Accessed
via
https://translation.
googleapis.com/language/translate/v2
8Accessed
via
https://huggingface.co/
facebook/nllb-200-distilled-1.3B

--- Page 5 ---

Bible - The New Testament
1. The book of the generation of Jesus Christ, the
son of David, the son of Abraham.
1.
इब्राहࣚमः
सۖानो
दायूद्
तࡺ
सۖानो
यीशुख्री࠿ࡰࡺपू࠘र्पुरुषवंशश्रेणी।
2. And being warned of God in a dream that they
should not return to Herod, they departed into
their own country another way.
2. पࠥाद्हेरोद्राजࡺसमीपंपुनरࣺपगۖुंࡼ݈
ई࠰रेणࣺनࣻषڔाःसۖोऽ۠ेनपथातेࣺनजदेशंप्रࣻत
प्रतऍࡱरे।
Mann Ki Baat
1. My dear countrymen, namaskar!
1. ममࣺप्रयाःदेश-वाऀसनः! नमࡡारः।
2. A while ago, I had a chance to have an indirect
dialogue, with young friends from Karnataka.
2. कࣻतपय-ࣺदनेޟःपूवर्म्अहंकणЄटकࡺबालࣻमत्रैः
सहपरोक्ष-संवादࡺअवसरंलނवान्।
Gita Sopanam
1. Father comes home from oﬀice.
1. ࣺपताकायЄलयात्गृहम्आगՃࣻत।
2. Paternal grandfather came home from library.
2. ࣺपतामहःग्रۗालयात्आगतवान्।
Spoken Tutorials
1. Let’s start today’s tutorial with this image.
1. अनेनࣿचत्रेणवयम्अښतनपाठࡺआरޱंकुमर्ः।
2. Today I will work with this image only to use it
as an example.
2. अښ, केवलम्उदाहरणٌेनउपयोѱुम्अनेनࣿचत्रेण
सहकाय϶ करोࣻम।
NIOS
1. Narrate the context of the Ramayana.
1. रामायणࡺकथांज्ञापࣻयतु޳।
2. understand the qualities of Rama.
2. रामࡺधाࣻमर्कगुणांࠥावगۖुम।
Table 5: Samples from different subsets of the Sāmayik.
mayik outperform that on Itihasa for MKB. Further,
model trained with the combination of Itihasa and
Sāmayik report marginally better scores on En-Sa
than the models trained only using SāmayikȮn the
contrary in Sa-En, Sāmayik reports better results
than the combination of two datasets. We find that
systems trained using our dataset has significantly
higher BLEU and ChrF scores reinforcing the need
for a corpus that follows contemporary content in
Sanskrit.
4.
Conclusion
We release a novel dataset, Sāmayik comprising
of around 53,000 sentences for English-Sanskrit
translation. Unlike existing datasets, Sāmayik em-
phasizes on contemporary prose writing and is cu-
rated from five diverse domains including instruc-
tion material, radio-podcast, etc. We also release
a set of strong baselines built on four multilingual
pre-trained models. We empirically demonstrate
that models trained using our dataset achieve bet-
ter performance than models trained on existing
datasets, as well as pre-trained models incorpo-
rated with a Sanskrit corpus.
Acknowledgements
We would like to thank following translators and re-
viewers towards development of the corpus.
1. Dr. Dinesh Joshi
2. Dr. Vasudev Aital
3. Shruti Sharma
4. Ashwini PN
5. Atmarama Bhat K
Ayush Maheshwari was supported by a fellow-
ship from the Ekal Foundation during his Ph.D. at
IIT Bombay.
Ashim Gupta is supported by the
Bloomberg Data Science Ph.D. Fellowship. This
work is a result of the funding by the IKS Division
of the Ministry of Education (MoE), Government of
India to the IKS Projects (AICTE/IKS/RFP1/2021-
22/05).
Ganesh Ramakrishnan is also grate-
ful to the National Language Translation Mission
(NLTM): Bhashini project by Government of India
and IIT Bombay Institute Chair Professorship for
their support and sponsorship.

--- Page 6 ---

References
Rahul Aralikatte, Miryam de Lhoneux, Anoop
Kunchukuttan, and Anders Søgaard. 2021. Iti-
hasa: A large-scale corpus for Sanskrit to En-
glish translation. In Proceedings of the 8th Work-
shop on Asian Translation (WAT2021), pages
191–197, Online. Association for Computational
Linguistics.
C Chandramouli. 2011. Census of india 2011. Pro-
visional Population Totals. New Delhi: Govern-
ment of India.
Christos Christodouloupoulos and Mark Steed-
man. 2015.
A massively parallel corpus: the
bible in 100 languages.
Language resources
and evaluation, 49:375–395.
Raj Dabre, Himani Shrotriya, Anoop Kunchukut-
tan, Ratish Puduppully, Mitesh Khapra, and
Pratyush Kumar. 2022.
IndicBART: A pre-
trained model for indic natural language gener-
ation. In Findings of the Association for Com-
putational Linguistics: ACL 2022, pages 1849–
1863, Dublin, Ireland. Association for Computa-
tional Linguistics.
Jay Gala,
Pranjal A Chitale,
Raghavan AK,
Sumanth
Doddapaneni,
Varun
Gumma,
Aswanth
Kumar,
Janki
Nawale,
Anupama
Sujatha, Ratish Puduppully, Vivek Raghavan,
et al. 2023. Indictrans2: Towards high-quality
and accessible machine translation models
for all 22 scheduled indian languages.
arXiv
preprint arXiv:2305.16307.
Oliver Hellwig. 2009. Extracting dependency trees
from sanskrit texts. In Sanskrit Computational
Linguistics: Third International Symposium, Hy-
derabad, India, January 15-17, 2009. Proceed-
ings, pages 106–115. Springer.
Oliver Hellwig. 2010–2021. Dcs - the digital corpus
of sanskrit.
Amrith Krishna, Bishal Santra, Ashim Gupta, Pa-
vankumar Satuluri, and Pawan Goyal. 2021. A
Graph-Based Framework for Structured Predic-
tion Tasks in Sanskrit. Computational Linguis-
tics, 46(4):785–845.
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan
Ghazvininejad, Abdelrahman Mohamed, Omer
Levy, Veselin Stoyanov, and Luke Zettlemoyer.
2020. BART: Denoising sequence-to-sequence
pre-training for natural language generation,
translation, and comprehension.
In Proceed-
ings of the 58th Annual Meeting of the Associa-
tion for Computational Linguistics, pages 7871–
7880, Online. Association for Computational Lin-
guistics.
Yinhan Liu, Jiatao Gu, Naman Goyal, Xian Li,
Sergey Edunov, Marjan Ghazvininejad, Mike
Lewis, and Luke Zettlemoyer. 2020. Multilingual
denoising pre-training for neural machine trans-
lation. Transactions of the Association for Com-
putational Linguistics, 8:726–742.
Ilya Loshchilov and Frank Hutter.
Decoupled
weight decay regularization.
In International
Conference on Learning Representations.
Ayush Maheshwari, Nikhil Singh, Amrith Krishna,
and Ganesh Ramakrishnan. 2022.
A bench-
mark and dataset for post-OCR text correction
in Sanskrit.
In Findings of the Association
for Computational Linguistics:
EMNLP 2022,
pages 6258–6265, Abu Dhabi, United Arab Emi-
rates. Association for Computational Linguistics.
Patrick McCartney. 2019.
Sustainably–speaking
yoga: Comparing sanskrit in the 2001 and 2011
indian censuses. In The GLOCAL in Asia 2019.
The GLOCAL Unit, SOAS University of London.
Kishore Papineni, Salim Roukos, Todd Ward, and
Wei-Jing Zhu. 2002. Bleu: a method for auto-
matic evaluation of machine translation. In Pro-
ceedings of the 40th annual meeting of the As-
sociation for Computational Linguistics, pages
311–318.
Maja Popović. 2015.
chrf: character n-gram f-
score for automatic mt evaluation. In Proceed-
ings of the Tenth Workshop on Statistical Ma-
chine Translation, pages 392–395.
Gary A Tubb and Emery R Boose. 2007. Scholas-
tic Sanskrit. American Institute of Buddhist Stud-
ies.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi,
Pierric Cistac, Tim Rault, Rémi Louf, Morgan
Funtowicz, et al. 2020.
Transformers: State-
of-the-art natural language processing. In Pro-
ceedings of the 2020 conference on empirical
methods in natural language processing: sys-
tem demonstrations, pages 38–45.
Linting Xue, Aditya Barua, Noah Constant, Rami
Al-Rfou, Sharan Narang, Mihir Kale, Adam
Roberts, and Colin Raffel. 2022.
ByT5:
To-
wards a token-free future with pre-trained byte-
to-byte models. Transactions of the Association
for Computational Linguistics, 10:291–306.

--- Page 7 ---

Linting Xue, Noah Constant, Adam Roberts, Mi-
hir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya
Barua, and Colin Raffel. 2021.
mt5: A mas-
sively multilingual pre-trained text-to-text trans-
former. In Proceedings of the 2021 Conference
of the North American Chapter of the Associa-
tion for Computational Linguistics: Human Lan-
guage Technologies, pages 483–498.

```
