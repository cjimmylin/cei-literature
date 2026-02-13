---
title: "2026-Alam-Quran-MD A Fine-Grained Multilingual Multimodal Dataset - PDF Extract"
source_pdf: "2026-Alam-Quran-MD A Fine-Grained Multilingual Multimodal Dataset.pdf"
pages: 6
extracted_at: "2026-02-13T09:15:45.213590"
---

# PDF Extract: 2026-Alam-Quran-MD A Fine-Grained Multilingual Multimodal Dataset

**Source PDF:** 2026-Alam-Quran-MD A Fine-Grained Multilingual Multimodal Dataset.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

QURAN-MD: A Fine-Grained Multilingual
Multimodal Dataset of the Quran
Muhammad Umar Salman
MBZUAI
Abu Dhabi, UAE
umar.salman@mbzuai.ac.ae
Mohammad Areeb Qazi
MBZUAI
Abu Dhabi, UAE
mohammad.qazi@mbzuai.ac.ae
Mohammed Talha Alam
MBZUAI
Abu Dhabi, UAE
mohammed.alam@mbzuai.ac.ae
Abstract
We present QURAN-MD, a comprehensive multimodal dataset of the Qur’an that
integrates textual, linguistic, and audio dimensions at the verse and word levels. For
each verse (ayah), the dataset provides its original Arabic text, English translation,
and phonetic transliteration. To capture the rich oral tradition of Qur’anic recitation,
we include verse-level audio from 32 distinct reciters, reflecting diverse recitation
styles and dialectical nuances. At the word level, each token is paired with its
corresponding Arabic script, English translation, transliteration, and an aligned
audio recording, allowing fine-grained analysis of pronunciation, phonology, and
semantic context. This dataset supports various applications, including natural lan-
guage processing, speech recognition, text-to-speech synthesis, linguistic analysis,
and digital Islamic studies. Bridging text and audio modalities across multiple re-
citers, this dataset provides a unique resource to advance computational approaches
to Qur’anic recitation and study. Beyond enabling tasks such as ASR, tajweed
detection, and Qur’anic TTS, it lays the foundation for multimodal embeddings,
semantic retrieval, style transfer, and personalized tutoring systems that can sup-
port both research and community applications. The dataset is available at https:
//huggingface.co/datasets/Buraaq/quran-audio-text-dataset
1
Introduction
The Qur’an, the holy book of Islam, occupies a central role in the spiritual, intellectual, and cultural
lives of nearly two billion Muslims worldwide. Revealed in Classical Arabic (Fusha), it is not only
revered as sacred scripture but also preserved through its oral tradition of recitation. Mastery of
recitation is guided by tajweed which is a set of phonological and prosodic rules that ensure the
Qur’an is read with precision, beauty, and correctness. For Muslims, engaging with the Qur’an
involves more than simply reading the text but is an act of devotion that requires both accurate
pronunciation and a deep understanding of its meaning.
Despite its origins in Arabic, the Qur’an is recited and studied across every corner of the globe,
including by millions of non-Arabic speakers from diverse linguistic and cultural backgrounds. This
global engagement highlights the challenges faced by learners who must navigate not only the Arabic
script but also its sounds, phonology, and interpretive meanings. While Islamic scholars, including
Ulama (religious scholars), Fuqaha (jurists), and researchers, have made significant contributions
to Qur’anic studies, the integration of modern computational approaches, particularly artificial
39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: MusIML
arXiv:2601.17880v1  [cs.CV]  25 Jan 2026

--- Page 2 ---

Table 1: Feature comparison across prominent Quranic datasets. The proposed QUR’AN-MD is the
first to holistically integrate all listed modalities across multiple reciters at both verse and word levels,
filling a critical gap in the available resources.
Dataset
Feature
Quranic Arabic
Corpus [1]
Tanzil
Project [4]
Tarteel [5]
QDAT [6]
QUR’AN-MD
(Ours)
Text (Arabic)
✓
✓
✓
✓
✓
Morpho-syntactic Data
✓
✗
✗
✗
✓
Multi-Language Translation
✗
✓
✗
✗
✓
Word-level Audio
✗
✗
✗
✓
✓
Verse-level Audio
✗
✗
✓
✓
✓
Multiple Reciters
✗
✗
✓
✗
✓
intelligence, remains very limited compared to the rapid advances in AI. AI has the potential to
illuminate linguistic patterns, aid recitation training, and support both Arabic and non-Arabic learners
in mastering tajweed and understanding the Qur’an’s message.
Existing resources, however, often fall short of capturing the Qur’an’s full multimodal nature. Some
datasets provide the Arabic text alone, others include translations or transliterations, and a few extend
to audio recordings at either the verse or word level. Rarely are these modalities combined in a way
that allows fine-grained analysis of both the written and spoken Qur’an. This fragmentation restricts
their utility for advancing AI-driven research in areas such as natural language processing, speech
recognition, and text-to-speech synthesis. Table 1 summarizes key features of prior Qur’anic datasets,
where QUR’AN-MD offers the most comprehensive multimodal coverage.
In this work, we curate and harmonize resources from three data sources to construct QUR’AN-MD, a
comprehensive multimodal dataset of the Qur’an. Our dataset unifies Arabic text, English translation,
and phonetic transliteration at both the verse and word levels, while pairing each word with an aligned
audio recording of its pronunciation. We provide high-quality recitations from 30 distinct reciters
at the verse level, representing diverse styles and dialectical nuances (see Table 2 in the Appendix).
Through careful validation and consistency checks, we ensure the reliability of the textual and audio
components. By making this dataset available on Hugging Face, we aim to provide scholars, linguists,
and AI researchers with a standardized resource that bridges textual, phonological, and semantic
dimensions. This contribution supports the study of Qur’anic language and recitation traditions. It
enables and promotes future work in cutting-edge computational applications at the intersection of
speech, language, and Quranic studies.
2
Related Work
There has been growing interest in developing resources for Qur’anic text and recitation, yet existing
efforts typically focus on either textual analysis or audio recordings, rather than providing a fully
integrated multimodal resource. Early structured corpora, such as the Quranic Arabic Corpus [1],
provide full text with detailed morphological and syntactic annotations, supporting parsing, part-of-
speech tagging, and grammatical analysis. More recent contributions, including the MASAQ corpus
[2] and the corpus introduced by [3], expand these annotations and incorporate orthographic variants
(Uthmani and Imlaai scripts), Buckwalter and phonetic transliterations, as well as English translations
at the verse level. Similarly, the Tanzil project [4] offers the Qur’an aligned with translations in
more than 40 languages, supporting multilingual NLP research, though without detailed linguistic or
recitational information.
Parallel to these textual resources, several initiatives have sought to capture Qur’anic recitation across
multiple readers. Large-scale audio collections, such as Tarteel AI EveryAyah[5] and the Quran-
Recitations Dataset [7], provide verse-level recordings across numerous reciters, while the Quranic
Audio Dataset [8] and RetaSy [9] focus on non-native reciters with labeled correctness annotations.
The OpenSLR Quran Speech-to-Text corpus [10] offers complete verse coverage for multiple reciters,
and smaller targeted collections, such as QDAT [11] and its extensions [12], provide labeled data
for Tajweed error detection using deep neural models. Recent Kaggle contributions, including the
Quran Ayat Speech-to-Text dataset [13], Quran Reciters dataset [14], Quran.com Audio dataset [15],
Quran Recitations for Audio Classification dataset [16], and the Comprehensive Quranic Dataset v1
2

--- Page 3 ---

(CQDV1) [17], offer large-scale verse-level audio recordings from dozens of reciters, but generally
provide only Arabic text and audio without consistent transliteration or translation.
Taken together, these resources demonstrate substantial progress in both linguistic annotation and
audio collection, yet they remain fragmented: either focusing on text or audio, verse- or word-level
data. None combine verse and word-level text, transliteration, English translation, and audio across
multiple reciters with consistent cross-modal alignment. QUR’AN-MD addresses these gaps by
integrating verse and word-level text, English translation, transliteration, word-level audio, and verse
audio from 30 reciters, providing a unified multimodal resource that supports research across natural
language processing, speech technologies, linguistic analysis, and digital Islamic studies.
3
Dataset (QUR’AN-MD)
The dataset was constructed by aggregating and harmonizing three publicly available sources of
Qur’anic data: (1) a Kaggle dataset of verse-level speech-to-text recordings by 30 reciters [18], (2)
the quranwbw repository containing aligned word-by-word Arabic text, English translations, and
transliterations [19], and (3) the Internet Archive collection of word-by-word Qur’an audio recordings
[20]. To unify these heterogeneous resources, we designed a hierarchical JSON template. At the top
level, each surah (chapter) is represented by its numerical index (e.g., "112" for the 114 surah’s) and
annotated with its Arabic name, English translation, transliteration, and total verse count. Each surah
contains a nested set of verses (ayahs), where each verse entry includes the Arabic text, its English
translation, phonetic transliteration, paths to reciter-specific verse-level audio, and a list of word-level
objects. Word objects store the word Arabic script, English translation, transliteration, and the
corresponding aligned audio file. This structure allows seamless integration of textual, transliterated,
and auditory modalities across both verse- and word-level granularities.
The preparation pipeline proceeded in four main steps. First, surah-level metadata (surah number,
names, and verse counts) was populated into the template. Second, from the Kaggle dataset, verse-
level recitations by 30 reciters were aligned with their corresponding verse texts and added under the
audio_ayah_path field. Third, word-level Arabic text, translations, and transliterations from the
quranwbw repository were inserted into the template. Fourth, word-level audio files from the Internet
Archive collection were matched to individual tokens and linked under the audio_word_path field.
After populating all layers, automated validation scripts were applied to ensure correctness, checking
that every word and verse was paired with its corresponding audio, and identifying and correcting
missing or misaligned entries. This pipeline resulted in a complete, consistent, and multimodal
representation of the Qur’an, ready for release as a standardized dataset.
Dataset Format: The dataset is organized in a hierarchical JSON structure, where each surah (chapter)
of the Qur’an is represented as a nested object. This design ensures that verse-level and word-level
information is consistently accessible and easily parsable for downstream applications. An example
of Surah 112 (Al-Ikhlas) is shown in Figure 1 (Appendix), highlighting metadata and audio/text
linkage. This structure enables researchers to work seamlessly at both the verse level (for example,
analyzing prosody between reciters) and the word level (for example, studying phoneme-grapheme
alignment).
4
Future Work
QUR’AN-MD opens multiple avenues for future research at the intersection of speech processing,
natural language processing, and digital Islamic studies. We outline three directions: (A) Speech-only
tasks, (B) Multimodal approaches integrating speech and text, and (C) Tools and applications that
can support both research and community engagement.
Speech-only Research: A major direction lies in automatic speech recognition (ASR) for Qur’anic
recitation, both at the verse and word level. The audio and verse-level transcripts aligned in the dataset
with 30 reciters provide a unique testbed to develop end-to-end ASR models adapted to classical
Arabic with the unique prosody and melodic contours in recitations. Evaluations can measure word
error rate and segmentation accuracy across reciters, while challenges include modeling tajweed-
driven prosody (madd, pauses, emphatics) and script-pronunciation mismatches.
3

--- Page 4 ---

Multimodal Speech-Text Research: The full potential emerges when the modalities are combined.
The dataset can drive progress in forced alignment and phoneme-level segmentation, producing
high-quality timestamps for words and phonemes that benefit pronunciation modeling. It enables
pronunciation tutoring systems tailored to Qur’anic recitation, which automatically detect tajweed
issues and mispronounced words, providing corrective audio feedback and guidance on proper
melodic and rhythmic patterns.
Another promising direction is Qur’anic TTS that respects tajweed rules and recitation styles. Lever-
aging parallel recordings from 32 reciters, the dataset enables the development of personalized
TTS systems that provide corrective feedback for tajweed and Qur’anic melody in a user’s own
voice, facilitating accurate imitation and learning. In addition, style transfer approaches can allow
users to reproduce the prosody and melodic patterns of renowned reciters while preserving tajweed
correctness, supporting both educational applications and expressive recitation synthesis.
Tools, Applications, and Community Resources: QUR’AN-MD also enables the development
of advanced tools and applications that bridge research and community engagement. Multimodal
embeddings of Qur’anic text and audio can support semantic retrieval of specific verses, style-
aware search, and clustering of reciters, while facilitating the creation of robust tutoring systems for
pronunciation and tajweed. Beyond machine learning applications, the dataset can be integrated into
retrieval platforms, APIs, and interactive visualization tools for scholars, educators, and students,
providing aligned verse- and word-level corpora that support linguistic, phonological, and prosodical
research. Such resources can foster broader accessibility and engagement with the Qur’an and its
studies.
5
Conclusion
We curated QUR’AN-MD, a comprehensive multimodal dataset of the Qur’an from three different
sources that integrates textual and audio information with linguistic annotations at the verse- and
word-level, encompassing 30 distinct reciters to capture the rich diversity of Qur’anic recitation. By
aligning Arabic text, English translations, phonetic transliterations, and fine-grained audio recordings
at both verse- and word-levels, the dataset enables a wide range of research applications, including
automatic speech recognition, tajweed detection, pronunciation tutoring, personalized Qur’anic TTS,
style transfer, and prosody modeling. Furthermore, it supports the development of multimodal
embeddings for semantic retrieval, style-aware search, and reciter clustering, as well as interactive
tools for scholars, educators, and learners. This resource bridges text and audio modalities at
scale, providing a unique platform to advance computational modeling and applications in Qur’anic
research.
4

--- Page 5 ---

6
Appendix
Beyond ASR, the dataset can enable automatic tajweed detection and error classification, an area
currently limited to small corpora like QDAT. In addition, it provides an opportunity to investigate
the explainability of tajweed errors or mispronounced words, allowing models to highlight specific
phonological or tajweed-related deviations and provide interpretable feedback for learners and
researchers. Leveraging recitation at a word level, models could detect rules such as ghunnah,
idgham, or madd, with precision/recall measured against expert annotations. Similarly, the dataset
supports reciter identification and style analysis, using embeddings to group readers by dialect or
melodic tendencies, and prosody modeling, which quantifies melodic contours and pause structures
for downstream use in Qur’anic TTS.
Example: Surah 112 (Al-Ikhlas): Figure 1 shows a simplified representation of the dataset format
for the 112th surah (Al-Ikhlas). This example illustrates how each surah contains its metadata, how
verses are indexed, and how both verse- and word-level audio/textual information are linked.
{
"112":
{
"surah_name_ar": "اﻹﺧﻼص",
"surah_name_en": "Sincerity",
"surah_name_tr": "Al-Ikhlaas",
"ayah_count": 4,
"ayahs": {
"001": {
"ayah_ar": "ﻗُلْ ھُوَ  ا.ﱠُ أَﺣَدٌ",
"ayah_en": "Say, \"He is Allah, [who is] One,\"",
"ayah_tr": "qul huwa l-lahu aḥadun",
"audio_ayah_path": {
"alafasy": "audio/ayahs/alafasy/112001.mp3",
"husary": "audio/ayahs/husary/112001.mp3",
"...": "... (32 reciters in total)"
},
"words": [
{
"id": "001",
"word_ar": "ﻗُلْ",
"word_en": "Say",
"word_tr": "qul",
"audio_word_path": "audio/words/112_001_001.mp3"
},
{
"id": "002",
"word_ar": "ھُوَ",
"word_en": "He",
"word_tr": "huwa",
"audio_word_path": "audio/words/112_001_002.mp3"
}
// ... (rest of the words in this ayah)
]
},
"002": {
"ayah_ar": "ا.ﱠُ اﻟﺻﱠﻣَدُ",
"ayah_en": "Allah, the Eternal Refuge.",
"ayah_tr": "allahu ṣ-ṣamad",
"audio_ayah_path": {
"alafasy": "audio/ayahs/alafasy/112002.mp3",
"husary": "audio/ayahs/husary/112002.mp3",
"...": "... (32 reciters in total)"
},
"words": [
// ... (words for this ayah will come here)
]
// ... (rest of the ayahs in this surah)
}
}
}
}
Figure 1: Example of format of Surah 112 (Al-Ikhlas) in the Dataset.
Table 2: Overview of the QUR’AN-MD dataset.
Category
Attribute
Statistics / Details
Corpus Size
Surahs
114
Ayahs
6,236
Words
∼77.8k
Audio
Reciters
30 (diverse styles)
Verse-level Audio
∼665 hours
Word-level Audio
∼22 hours
Modalities
Text
Arabic, English, Transliteration
Audio
Verse- and Word-level recordings
5

--- Page 6 ---

References
[1] A. Dukhovny and E. Atwell. The quranic arabic corpus: An annotated linguistic resource for
the holy quran. In Proceedings of the 7th International Conference on Language Resources and
Evaluation (LREC), 2009.
[2] Majdi Sawalha, Fahad Alshammari, Salam Khalifa, and Nizar Habash. Masaq: Morphologically-
analyzed and syntactically-annotated quran corpus. Language Resources and Evaluation, 2024.
[3] A. Nashir and colleagues. Quranic corpus with orthographic, morphological, and syntactic
layers. Mendeley Data, V1, 2025.
[4] Z. Zarrabi-Zadeh. Tanzil: Verified quran text and translations. https://tanzil.net, 2008.
[5] Taha Khan et al. Tarteel: Crowdsourcing a large dataset of quran recitations for speech
recognition. In Proceedings of Interspeech, 2021.
[6] Hanaa Mohammed Osman, Ban Sharief Mustafa, and Yusra Faisal. Qdat: A data set for reciting
the quran. International Journal on Islamic Applications in Computer Science And Technology,
9(1), 2021. Provides audio annotated for Tajweed rules (Al Mad, Ghunnah, Ikhfaa).
[7] MohamedRashad. Quran-recitations dataset. Hugging Face Dataset, 2024. Verse-level audio +
fully diacritized Arabic text, multiple reciters.
[8] Raghad Salameh, Mohamad Al Mdfaa, Nursultan Askarbekuly, and Manuel Mazzara. Quranic
audio dataset: Crowdsourced and labeled recitation from non-arabic speakers. In arXiv preprint,
2024. Crowdsourced labeling of correct/incorrect recitations from non-native reciters.
[9] Ahmad Salameh and colleagues. Retasy: A crowdsourced quran recitation dataset from non-
arabic speakers. In Proceedings of the 12th Language Resources and Evaluation Conference
(LREC), 2024.
[10] OpenSLR. Quran speech-to-text (slr132). https://www.openslr.org/132, 2017.
[11] A. Osman and colleagues. Qdat: Quranic dataset for automatic tajweed error detection. In
Proceedings of the IEEE International Conference on Arabic Language Processing (ICALP),
2021.
[12] Dim Shaiakhmetov, Gulnaz Gimaletdinova, Selcuk Cankurt, and Kadyrmamat Momunov.
Evaluation of the pronunciation of tajweed rules based on dnn as a step towards interactive
recitation learning. 2025. Uses QDAT dataset for classifying Tajweed rules: Al-Mad, Ghunnah,
Ikhfaa.
[13] BigGuyUbuntu. Quran ayat speech-to-text dataset. Kaggle, https://www.kaggle.com/
datasets/bigguyubuntu/quran-ayat-speech-to-text, 2023.
[14] Omar Tariq.
Quran reciters dataset.
Kaggle, https://www.kaggle.com/datasets/
omartariq612/quran-reciters, 2025.
[15] Abdo3id.
Quran.com audio dataset.
Kaggle, https://www.kaggle.com/datasets/
abdo3id/quran-com-audio-files, 2022.
[16] Mohammed
Alrajeh.
Quran
recitations
for
audio
classification.
Kaggle,
https://www.kaggle.com/datasets/mohammedalrajeh/
quran-recitations-for-audio-classification, 2021.
[17] QuranicDataset. Comprehensive quranic dataset v1 (cqdv1). Kaggle, https://www.kaggle.
com/datasets/quranicdataset/quranic-dataset-v1, 2024.
[18] Bigguyubuntu. Qur’an ayat speech-to-text dataset. https://www.kaggle.com/datasets/
bigguyubuntu/quran-ayat-speech-to-text, 2021. Accessed: 2025-09-14.
[19] Qazasaz. Quran word-by-word repository. https://github.com/qazasaz/quranwbw, 2018.
Accessed: 2025-09-14.
[20] Internet Archive. Qur’an word-by-word audio collection. https://archive.org/details/
quran-wordbyword, 2017. Accessed: 2025-09-14.
6

```
