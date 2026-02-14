---
title: "2025-Pretrained-Graphic Language Model for Agglutinative Languages Uyghur as Study"
source_pdf: "[[PDFs/2025/2025-Pretrained-Graphic Language Model for Agglutinative Languages Uyghur as Study.pdf]]"
extracted_date: "2026-02-14"
extraction_method: "PyMuPDF"
---

# PDF Extract: 2025-Pretrained-Graphic Language Model for Agglutinative Languages Uyghur as Study

```
## Page 1

Graphic Language Model for Agglutinative
Languages: Uyghur as Study Case
Miliwan Xuehelaiti1,2,3,⋆, Kai Liu2, Wenbin Jiang2, and Tuergen Yibulayin1
1 Xinjiang University Information Science and Technology Institute
Urumqi, Xinjiang 830046, China
mihreban@126.com
2 Institute of Computing Technology, University of Chinese Academy of Sciences
Beijing 100190, China
{liukai,jiangwenbin}@ict.ac.cn
3 Urumqi Administration of Industry and Commerce
Urumqi, Xinjiang 830002, China
Abstract. This paper describes a novel, graphic language modeling
strategy for morphologically rich agglutinative languages. Diﬀerent from
the linear structure in n-gram language models, graphic modeling or-
ganizes the morphemes in a sentence, including stems and aﬃxes, as a
directed graph. The graphic language model is veriﬁed in two typical
application scenarios, morphological analysis and machine translation.
We take Uyghur for example, and experiments show that the graphic
language model achieves signiﬁcant improvement in both morphological
analysis and machine translation.
Keywords: graphic language model, agglutinative language, morpho-
logical analyzing, statistical machine translation.
1
Introduction
Language model is one of the most important models in NLP, it describes proba-
bilities of sentences in natural language. Many NLP tasks can be boiled down to
the modeling of language model, such as transliteration, speech recognition, part
of speech tagging and so on. One of most widely used language model is n-gram
language model[3], which models words in sentences with local context environ-
ment in an linear way. The n-gram language model is simple and eﬀective, and
it have got excellent performance on Chinese, English and other languages with
simple morphological form.
Agglutinative language is one kind of language which is widely used in
North/South Korea, Japan, Mongolian, Turkey and other countries in Middle
East Asia and other areas. Agglutinative languages diﬀer from languages with
simple morphological form (such as English and Chinese) in their sentence and
⋆This work is supported by the National Science Foundation of China (Grant No.
61262060 61262060 ), Key Project of National Natural Science Fund [61032008] and
National Social Science Fund Key Projects [10AYY006].
M. Sun et al. (Eds.): CCL and NLP-NABD 2013, LNAI 8202, pp. 268–279, 2013.
c
⃝Springer-Verlag Berlin Heidelberg 2013

## Page 2

Graphic Language Model for Agglutinative Languages
269
word-formation[2], in which the composition of each word in agglutinative lan-
guage follows diﬀerent word-building rules according to simple observation: each
word of agglutinative language is composed by a word-stem and any number of
aﬃxes, in where constrained relations exist between stem and aﬃxes; and simi-
lar relations exist in stems of diﬀerent words. The former rule lead to the data
sparseness of word of agglutinative language, the latter rule makes it hard to
seize the relation between stems, for there maybe some aﬃxes between stems in
diﬀerent words.
According to the observations above, sentence of agglutinative language with
those relations can not be simply modeled as linear sequence. As a matter of fact,
traditional n-gram language language model which models sentences as linear
sequence can not obtain idea results on agglutinative languages. In this paper,
we propose a novel graphic language model which can depict those relations
more deeply. More speciﬁcally, our graphic language model models the generative
relations between stem and aﬃxes in a word and the relations between stems
in diﬀerent words, which relations can hardly be modeled by traditional linear
language models.
In order to test the novel graphic language model, two language model needed
natural language processing tasks (morphological analyzing and statistical ma-
chine translation(SMT)) are adopted to verify our graphic language model. In
the experiments, both tasks show that graphic language model gets signiﬁcant
improvements compares to n-gram language model. In morphological analyzing,
the accuracy gains 0.8% improvements due to the new style language model,
while in SMT it gains more than 1.1 BLEU improvement. Furthermore, the
graphic language model is simple, and the complexity of it is approximate to the
n-gram language model.
The rest of paper is organized as follows: Section 2 describes the characteristics
of agglutinative languages; Traditional linear language model is described in
Section 3; We propose our graphic language model for agglutinative language
in Section 4; And the methods of utilizing proposed graphic language model in
two NLP tasks are shown in Section 5; Finally, we present the experiments of
the two NLP tasks with graphic language model on Uyghur in Section 6 and
conclude in Section 8.
2
Agglutinative Language
Agglutinative language is a kind of language that its words are made up of dis-
tinct morphemes by a linear sequence way, and each component of meaning is
represented by its own morpheme. Agglutinative languages have many charac-
teristic, more speciﬁcally, we take Uyghur as our study case. Uyghur is one of
typical agglutinative languages, it is a Turkic language which is widely used in
Western China by Uyghur people, and it shares some characteristics with other
agglutinative languages:

```
