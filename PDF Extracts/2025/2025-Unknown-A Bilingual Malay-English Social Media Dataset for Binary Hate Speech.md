---
title: "2025-Unknown-A Bilingual Malay-English Social Media Dataset for Binary Hate Speech - PDF Extract"
source_pdf: "2025-Unknown-A Bilingual Malay-English Social Media Dataset for Binary Hate Speech.pdf"
pages: 8
extracted_at: "2026-02-13T21:21:01.530626"
---

# PDF Extract: 2025-Unknown-A Bilingual Malay-English Social Media Dataset for Binary Hate Speech

**Source PDF:** 2025-Unknown-A Bilingual Malay-English Social Media Dataset for Binary Hate Speech.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Data in Brief 63 (2025) 112153 
Contents lists available at ScienceDirect 
Data in Brief 
journal homepage: www.elsevier.com/locate/dib 
Data Article 
A bilingual Malay-English social media dataset 
for binary hate speech detection 
Jun-Chen Tan, Lee-Yeng Ong ∗, Meng-Chew Leow 
Faculty of Information Science and Technology, Multimedia University, Melaka, 75450 Malaysia 
a r t i c l e 
i n f o 
Article history: 
Received 19 June 2025 
Revised 30 September 2025 
Accepted 2 October 2025 
Available online 8 October 2025 
Dataset link: A Bilingual Malay-English 
Social Media Dataset for Binary Hate 
Speech Detection (Original data) 
Keywords: 
Hate speech detection 
Malay-English bilingual data 
Pseudo-labelling 
Low-resource languages 
a b s t r a c t 
In recent years, online hate speech has posed a growing 
threat to user safety, social harmony, and community cohe- 
sion especially on social media platforms. However, most ex- 
isting hate speech datasets are monolingual and resource- 
rich, which leave Southeast Asia languages such as Malay un- 
derrepresented in natural language processing research. The 
aim of this dataset is to handle this gap by providing a bal- 
anced and quality-controlled resource that supports machine 
learning applications in multilingual settings. Binary classi- 
ﬁcation is selected as a foundation task because it simpli- 
ﬁes practical deployment in real-world and early-stage de- 
tection systems. It is beneﬁcial in low-resource languages 
where detailed or multi-label annotations are always unavail- 
able or inconsistent. This dataset presents 26,985 bilingual 
Malay-English social media texts curated from ﬁve public 
sources for binary hate speech detection. It combines human- 
annotated and ﬁltered through controlled pseudo-labelling 
to retain only high-conﬁdence, quality-controlled texts. The 
dataset is provided in UTF-8 encoded CSV format with 13,609 
English and 13,376 Malay-language texts. Each entry includes 
the social media post, binary label (0 = non-hate, 1 = hate), 
language identiﬁer (en or ms), and data source information. 
The dataset meets clear practical demands, including train- 
ing multilingual transformer-based classiﬁers, benchmark- 
ing cross-lingual NLP models, and developing effective hate 
∗Corresponding author. 
E-mail address: lyong@mmu.edu.my (L.-Y. Ong). 
https://doi.org/10.1016/j.dib.2025.112153 
2352-3409/© 2025 The Author(s). Published by Elsevier Inc. This is an open access article under the CC BY-NC license 
( http://creativecommons.org/licenses/by-nc/4.0/ ) 

--- Page 2 ---

2 
J.-C. Tan, L.-Y. Ong and M.-C. Leow / Data in Brief 63 (2025) 112153 
speech detection systems and educational NLP resources for 
English and Malay-speaking communities. 
© 2025 The Author(s). Published by Elsevier Inc. 
This is an open access article under the CC BY-NC license 
( http://creativecommons.org/licenses/by-nc/4.0/ ) 
Speciﬁcations Table 
Subject 
Computer Sciences 
Speciﬁc subject area 
Bilingual hate speech detection using low-resource Malay-English social media 
data. 
Data Format 
CSV ﬁle 
Type of data 
Processed text data 
Data collection 
The dataset is constructed by combining ﬁve publicly available sources. 
Annotated texts from HateXplain [ 1 ], HateM [ 2 ], and Toxicity-Small are 
ﬁltered for label relevance and quality before inclusion. In contrast, 
Snapshot-Twitter-2022 and Supervised_sentiment datasets initially 
unlabelled are pseudo-labelled using Mesolitica’s NanoT5-based sentiment 
and emotion classiﬁcation models [ 3 ]. Only non-hate pseudo-labels texts 
are retained to prevent noise from weak supervision. This design choice 
handle class imbalance, as the Malay datasets, HateM and Toxicity-Small 
predominantly contribute hate-labelled texts; expanding only the non-hate 
class helps achieve a more balanced distribution across both labels and 
languages. 
Data source location 
The raw data is collected from the following available sources: 
• [ 1 ] https://github.com/hate-alert/HateXplain 
• [ 2 ] https://github.com/MaityKrishanu/Hate_Malay 
• [ 4 ] https://github.com/asrafulsyifaa/Malay-Dataset/tree/master/corpus/ 
toxicity-small 
• [ 5 ] https://huggingface.co/datasets/malaysia-ai/snapshot-twitter 
–2022–09–03 
• [ 6 ] https://github.com/mesolitica/malaysian-dataset/tree/master/ 
sentiment/supervised-twitter 
In addition, two types of dictionaries collection are applied for slang 
normalisation, translation, and pseudo-labelling process. First, custom 
dictionaries of Malay-language slang and hate speech keywords that collected 
from online sources such as Reddit or Blog. Second, two available dictionaries, 
like Eng-Malay keyword and English slang from GitHub, as shown below: 
• [ 13 ] https://github.com/asrafulsyifaa/Malay-Dataset/blob/master/ 
dictionary/200k- english- malay 
• [ 7 ] https://github.com/cbaziotis/ekphrasis/blob/master/ekphrasis/dicts/ 
noslang/slangdict.py 
Licensing terms of each source dataset are summarised in Appendix A for 
transparency and compliance. 
Data accessibility 
Repository name: Mendeley Data 
Data identiﬁcation number: 10.17632/mgv2n2vcb9.3 
Direct URL to data: [ 8 ] https://data.mendeley.com/datasets/mgv2n2vcb9/3 
Related research article 
none. 
1. Value of the Data 
• The dataset provides one of the few bilingual Malay-English resources available for hate 
speech detection and handles the lack of annotated data for Southeast Asia languages. 
• The dataset supports the development and evaluation of machine learning models for binary 
classiﬁcation of hate and non-hate speech especially in multilingual or code-switched social 
media settings. 
• Researchers in natural language processing (NLP), low-resource language modelling, or South- 
east Asia language studies may reuse the dataset for benchmarking multilingual and cross- 
lingual classiﬁcation systems. 

--- Page 3 ---

J.-C. Tan, L.-Y. Ong and M.-C. Leow / Data in Brief 63 (2025) 112153
3 
• The dataset combines annotated English and Malay texts with pseudo-labelled Malay- 
language texts, which allows reproducible research in hybrid supervised and semi-supervised 
learning approaches. 
• Language-speciﬁc preprocessing and custom dictionaries are applied to clean and normalise 
noisy texts, making the dataset valuable for further research on social media text normalisa- 
tion. 
• The dataset can be reused in hate speech detection systems, social media content moderation 
systems, and education NLP applications focusing on English and Malay-language content. It 
also supports cross-lingual transfer learning, platform-level content moderation across mul- 
tiple languages, and comparative studies of cultural and linguistic differences in hate speech 
expression. 
2. Background 
The dataset is collected in response to the growing need for high-quality, language-diverse re- 
sources for hate speech detection. Although English datasets such as HateXplain ( ∼20,0 0 0 texts 
annotated as hate, offensive, or normal) are abundant, Malay-language resources remain lim- 
ited. Existing Malay-language datasets include ( ∼80 0 0 texts) and Toxicity-Small ( ∼50 0 0 texts), 
contain manually labelled hate and non-hate texts but suffer from class imbalance with non- 
hate underrepresented, and from noisy forum-derived texts. Since high-quality Malay-language 
non-hate texts are fewer than English coverage, additional unlabelled Malay-language sources 
include Snapshot and Supervised_sentiment, are used to enhance the non-hate class through 
controlled pseudo-labelling. Label scheme inconsistencies across datasets, such as multi-class 
annotations in HateXplain versus binary labels in HateM and Toxicity-Small, also affect direct 
integration and reinforce English bias. It has limited model transferability to Malay-language or 
code-switched contexts. Therefore, ﬁve publicly available datasets are consolidated, selected for 
complementary coverage across language, domain, and annotation style. All labels are standard- 
ised into a binary format (hate = 1, non-hate = 0). Language-speciﬁc preprocessing pipelines are 
applied (Ekphrasis for English; Malaya NLP, slang normalisation, and dictionary-based correction 
for Malay-language). The resulting balanced, language-tagged dataset supports bilingual bench- 
marking, cross-lingual transfer, and research on low-resource NLP, and semi-supervised learning 
[ 9 ]. 
3. Data Description 
The dataset is provided as a single CSV ﬁle named bilingual_hatespeech_ms_en.csv, which 
contains 26,985 social media posts annotated for binary hate speech detection. In each row, a 
single cleaned and pre-processed text instance is provided in either English or Malay-language. 
The dataset combines annotated and pseudo-labelled content from ﬁve available sources: HateX- 
plain [ 1 ], HateM [ 2 ], Toxicity-Small, Snapshot-Twitter-2022, and Supervised_sentiment. Table 1 
shows the columns included in the CSV ﬁle that uses UTF-8 encoding: 
The dataset is evenly distributed across both languages and labels for balanced training and 
evaluation. Table 2 shows the summary statistics of how the dataset is organised. It is important 
Table 1 
Column in the dataset with its description. 
Column 
Description 
Text 
Cleaned and normalized social media post content. 
label 
Binary label (0 = non-hate, 1 = hate) 
lang 
Language code (en for English, ms for Malay) 
source 
Original dataset source (e.g., HateXplain, HateM) 

--- Page 4 ---

4 
J.-C. Tan, L.-Y. Ong and M.-C. Leow / Data in Brief 63 (2025) 112153 
Table 2 
Label and language distribution. 
Language 
Hate (1) 
Non-Hate (0) 
Total 
English 
6129 
7480 
13,609 
Malay 
6214 
7162 
13,376 
Total 
12,343 
14,642 
26,985 
Table 3 
Cross-tabulated distribution. 
Language 
Source 
Hate (1) 
Non-Hate (0) 
Total 
English 
HateXplain 
6129 
7480 
13,609 
Malay 
HateM 
1397 
2187 
3584 
Malay 
Toxicity-Small 
4817 
435 
5252 
Malay 
Snapshot 
–
4 4 49 
4 4 49 
Malay 
Supervised_sentiment 
–
91 
91 
Total 
–
12,343 
14,642 
26,985 
Table 4 
Sample data texts. 
Text 
label 
source 
language 
so that white powder must have been sodium percarbonate 
0 
HateXplain 
en 
< user > aduh pergi la mengandung sendiri … yang laki pun 
bodoh bebal kimi lincou gi mampos 
1 
HateM 
ms 
baru tadi lalu dekat fyp saya . terkejut yang komen semua 
perempuan 
0 
Supervised_sentiment 
ms 
because a balanced dataset ensures fair training for machine learning models and equal language 
representation support multilingual or cross-lingual NLP research. 
In addition to the overall distribution, a cross-tabulated view of texts by language, source 
dataset, and binary label is provided in Table 3 . This breakdown shows the portion of each 
dataset in each language. Among these, HateXplain, HateM, and Toxicity-Small are fully human- 
annotated (22,445 texts, 83.2 %), while Snapshot and Supervised_sentiment contribute pseudo- 
labelled non-hate texts only (4540 texts, 16.8 %). The inclusion of pseudo-labelled texts is moti- 
vated by class imbalance. Both HateM and Toxicity-Small primarily supply Malay-language hate 
texts, by leaving the non-hate class underrepresented. Controlled pseudo-labelling therefore tar- 
get only non-hate expansion to restore balance without introducing noisy hate labels. To validate 
these pseudo-labels, manual checking of 200 randomly sampled texts is applied. 
In Table 4 , several examples of actual dataset rows from the CSV ﬁle are shown to help re- 
viewers understand what the data looks like. Each row in the dataset has a cleaned text (text), 
a label (0 or 1), source (which dataset it came from), and a language code (en or ms). 
Moreover, two types of dictionaries are used during data preprocessing to support slang nor- 
malization, translation, and pseudo-labelling. A collected dictionary is developed with common 
Malay-language social media slang collected. It does not contain copyrighted or proprietary con- 
tent and are derived from accessible, anonymised social media platforms such as Reddit and 
personal blog. It standardises informal expressions to improve data quality. External dictionaries 
also be used to support English-Malay translation and slang correction. Table 5 shows represen- 
tative from each dictionary used during the data preprocessing and labelling process. 
4. Experimental Design, Materials and Methods 
The dataset is combined through a structured pipeline involving data acquisition, language- 
speciﬁc preprocessing, controlled pseudo-labelling, and dataset balancing. Five datasets are 

--- Page 5 ---

J.-C. Tan, L.-Y. Ong and M.-C. Leow / Data in Brief 63 (2025) 112153
5 
Table 5 
Sample entries from the dictionaries used in data preprocessing. 
Dictionary Type 
Slang/Keyword 
Normalised/Translation 
Malay Slang (custom) 
dkt 
Dekat 
English-to-Malay (public) 
propagative 
propagatif 
English Slang (public) 
aiight 
all right 
constructed to create the ﬁnal dataset: HateXplain (English, labelled) [ 1 ], HateM (Malay, la- 
belled) [ 2 ], Toxicity-Small (Malay, labelled), Snapshot-Twitter-2022 (Malay, unlabelled, and Su- 
pervised_sentiment (Malay, unlabelled). 
1. Data Acquisition: All ﬁve source datasets are retrieved from public repositories in CSV or 
JSON format. The English dataset includes expert-labelled posts for hate/offensive/normal la- 
bels, which are binarised as hate (1) and non-hate (0). For Malay data, labelled datasets are 
included without modiﬁcation, while unlabelled Malay-language datasets underwent con- 
trolled pseudo-labelling with language-speciﬁc models. 
2. Pseudo-Labelling Technique: Pseudo-labels are applied for the unlabelled Malay-language 
sources with a controlled two-stage process that combined rule-based toxic-keyword safe- 
guards with a model-based conﬁdence thresholds technique. Mesolitica’s pre-trained NanoT5 
sentiment and emotion models [ 3 ] are used to compute conﬁdence scores for each sam- 
ple. Since existing Malay datasets (HateM and Toxicity-Small) primarily supply hate-labelled 
texts, the non-hate class is underrepresented. Controlled pseudo-labelling therefore focused 
exclusively on expanding the Malay non-hate class, while avoiding the inclusion of high-risk 
pseudo-labelled hate texts. 
a. Malaya NLP Sentiment and Emotion Models: Each text is processed using Mesolitica’s pre- 
trained NanoT5 sentiment and emotion models [ 3 ]. Following previous practice in semi- 
supervised learning [ 10 , 11 ] and low-resource automatic labelling [ 3 ], strict cutoffs are ap- 
plied. 
• Conﬁdence score ≥0.85 for negative sentiment or anger emotion is labelled as hate 
(1) but not retained in the ﬁnal dataset. 
• Conﬁdence score ≤0.30 is labelled as non-hate (0). 
• 0.30 < score < 0.85 is excluded to control uncertainty. 
b. Although both thresholds are calibrated, only the ≤0.30 non-hate labels are retained in 
the ﬁnal dataset. The choice of 0.30 as the non-hate cutoff is motivated by the need to re- 
tain only extremely low-conﬁdence negative/anger predictions, which empirical validation 
showed to align with human judgement, while excluding the majority of borderline and 
potentially noisy cases. The 0.85 hate cutoff is reported for completeness but deliberately 
excluded to avoid uncontrolled label noise. 
c. Keyword ﬁltering and manual validation: A custom toxic-keyword lexicon of Malay- 
language ( ∼150 abusive terms) is used to prevent false non-hate assignments. Any non- 
hate text ( ≤0.30) containing lexicon terms is automatically excluded or ﬂagged for man- 
ual review. After this ﬁltering, a random sample of 200 retained texts is manually vali- 
dated, with 0/200 errors observed. This corresponds to a conservative 95 % binomial con- 
ﬁdence interval upper bound of ≤1.9 % potential mislabelling. 
Through this controlled pseudo-labelling technique by combining strict thresholding, 
toxic-lexicon ﬁltering, and empirical validation, a total of 4540 non-hate pseudo-labelled 
texts are retained. These represent 16.8 % of the ﬁnal dataset. The ≥0.85 hate boundary 
is reported for transparency but is not used for inclusion. 
3. Language-Aware Preprocessing: Text preprocessing is applied separately for English and 
Malay-language. Deduplication is applied after cleaning to ensure only unique and high- 
quality texts are included. 
a. Malay-language: Malay-texts are processed using the Malaya NLP toolkit (version 5.1) for 
spelling correction, normalisation, and tokenisation. A custom dictionary which compiled 

--- Page 6 ---

6 
J.-C. Tan, L.-Y. Ong and M.-C. Leow / Data in Brief 63 (2025) 112153 
Table 6 
Hyperparameters of benchmark models. 
Model 
Sequence Length 
Tokeniser 
Optimiser 
LR 
XLM-R 
128 
SentencePiece 
AdamW 
2e-5 
InfoXLM 
128 
SentencePiece 
AdamW 
2e-5 
DistilBERT 
128 
WordPiece 
AdamW 
3e-5 
mBERT 
128 
WordPiece 
AdamW 
1e-5 
Table 7 
Binary classiﬁcation performance. 
Model 
Accuracy 
Macro F1 
Precision 
(Hate) 
Recall 
(Hate) 
F1 (Hate) 
EN F1 
(Hate) 
MS F1 
(Hate) 
Inference 
Time (s) 
XLM-R 
0.8572 
0.8568 
0.8170 
0.8831 
0.8488 
0.8368 
0.8609 
0.0022 
InfoXLM 
0.8660 
0.8649 
0.8421 
0.8639 
0.8531 
0.8482 
0.8580 
0.0021 
DistilBERT 
0.8585 
0.8572 
0.8457 
0.8415 
0.8436 
0.8324 
0.8548 
0.0016 
mBERT 
0.8669 
0.8660 
0.8428 
0.8685 
0.8555 
0.8491 
0.8618 
0.0021 
from Reddit, blogs, and Malaysian Twitter is used to map informal tokens to canonical 
forms (e.g. dkt to dekat). A 200k English-Malay bilingual dictionary is used to translate 
embedded English terms to Malay base forms where appropriate. Probabilistic spelling 
correction from Malaya is applied conservatively to avoid over-normalisation. Regex rules 
remove non-ASCII characters, repeated punctuation, and placeholder spam. Quality ﬁlters 
remove samples with fewer than three words, more than 280 characters, only placehold- 
ers or emojis, or excessive placeholder tokens. 
b. English: English texts are cleaned using the Ekphrasis toolkit [ 7 ] with additional custom 
regular expressions. Ekphrasis’ SocialTokenizer is used to segment hashtags, contractions, 
and emoticons. Custom regex rules remove non-ASCII noise, compress repeated char- 
acters, and normalise common social-media abbreviations using the noslang dictionary 
( ∼5400 texts). Placeholders are standardised to < user > and ⟨ url ⟩ . Low-value texts (fewer 
than three words, emoji-only content, or excessive placeholders) are ﬁltered. 
4. Dataset Construction and Balancing: To ensure equal class distribution and reduce sampling 
bias, the number of hate and non-hate texts are matched to the English dataset, which has 
approximately (14,642 non-hate and 12,343 hate-labelled texts. Priority is given to labelled 
texts for both classes. When needed, conﬁdent pseudo-labelled texts are sampled to reach 
the target size. Samples are selected with the use of stratiﬁed random sampling and merged 
into a ﬁnal dataset. 
The ﬁnal dataset is saved in CSV format with UTF-8 encoding, which includes four columns: 
text, label, lang, and source. 26,985 texts are included, with balanced class labels and nearly 
equal distribution across English and Malay languages. All codes for preprocessing, labelling, 
and sampling are written in Python 3.11 with the libraries like pandas, re, tqdm, Malaya, 
ekphrasis, and scikit-learn. The dataset is suitable for bilingual binary hate speech detection, 
domain adaptation research, and low-resource language benchmarking. 
5. To evaluate the effectiveness of the dataset, four multilingual transformer models including 
mBERT, XLM-R, InfoXLM, and DistilBERT are ﬁne-tuned for binary hate speech detection. All 
models are implemented using the HuggingFace Transformers library with a PyTorch back- 
end. Training is conducted on an NVIDIA GeForce GTX 3060 GPU, with random seeds ﬁxed. 
For model evaluation, the dataset is divided into training, validation, and test sets using strat- 
iﬁed sampling by label. Speciﬁcally, 20 % of the data is held out as a ﬁxed test set, while the 
remaining 80 % is split into 71 % training and 9 % validation. This corresponds to an approxi- 
mate 70/10/20 train/validation/test split. Early stopping with patience of 3 epochs is applied, 
and hyperparameters applied are summarised in Table 6 . 
6. As shown in Table 7 , mBERT achieves the best overall performance with an accuracy of 
0.8669 and a macro F1-score of 0.8660. It indicates well-balanced classiﬁcation between hate 

--- Page 7 ---

J.-C. Tan, L.-Y. Ong and M.-C. Leow / Data in Brief 63 (2025) 112153
7 
and non-hate texts. It also generalises across both languages, with F1-scores of 0.8491 for 
English and 0.8618 for Malay language. This conﬁrms its suitability for handling bilingual 
and code-switched content. InfoXLM and XLM-R achieve comparable results, while Distil- 
BERT provides the fastest inference speed by having 0.0016 s per sample with slightly lower 
recall. These results provide baseline benchmarks, which demonstrates that the dataset sup- 
ports the development of effective bilingual hate speech detection models. These results are 
consistent with prior ﬁndings on Malay-language benchmarks [ 12 ]. 
Limitations 
Several limitations are acknowledged in constructing this bilingual hate speech dataset. First, 
while the dataset includes annotated samples from HateXplain [ 1 ], HateM [ 2 ], and Toxicity- 
Small provide manually annotated texts, additional Malay-language texts are obtained through 
controlled pseudo-labelled of unlabelled sources like Snapshot and Supervised_sentiment using 
sentiment and emotion models. This process may still introduce bias or inaccuracies even un- 
der strict thresholds. To reduce label noise, only non-hate pseudo-labelled texts are retained. 
However, this design means that some hate expression from unlabelled sources may remain un- 
represented. Second, although slang is compiled from online sources and prior research, some of 
the full diversity of context-speciﬁc slangs used in Malaysian social media may not be captured, 
which can affect coverage. Third, the dataset is limited to text-based social media posts and does 
not include multimedia content. This exclusion is a deliberate design choice to control scope and 
reduce potential confounding from multimodal signals for ensuring the pseudo-labelling frame- 
work remain consistent. Although effort s are made to balance language and label distributions, 
the dataset may still reﬂect domain-speciﬁc in the original sources, such as overrepresentation 
of certain topics, groups, or platforms. 
Ethics Statement 
In this work, data collected from available social media datasets and repositories are in- 
cluded. All datasets used are annotated and shared under open licenses or hosted on platforms 
like GitHub and Hugging Face. All social media texts have been fully anonymised during the 
preprocessing process with identiﬁable information such as usernames, URLs, and numerical 
identiﬁers replaced with placeholders. No attempt is made to re-identify users. The data col- 
lection and redistribution strictly comply with the terms of use and data redistribution poli- 
cies of the respective platforms. No private or restricted-access data has been included in this 
dataset. 
CRediT Author Statement 
Jun-Chen Tan: Conceptualisation, Data curation, Methodology, Validation, Writing – original 
draft. Lee-Yeng Ong: Supervision, Writing – review and editing, resources. Meng-Chew Leow: 
Writing – review and editing, project administration, funding acquisition. 
Data Availability 
A Bilingual Malay-English Social Media Dataset for Binary Hate Speech Detection (Original 
data) (Mendeley Data) 

--- Page 8 ---

8 
J.-C. Tan, L.-Y. Ong and M.-C. Leow / Data in Brief 63 (2025) 112153 
Acknowledgements 
This work is 233 funded by Telekom Malaysia Research and Development under grant 
RDTC/241125 (MMUE/2400 6 6) . 
Declaration of Competing Interest 
The authors declare that they have no known competing ﬁnancial interests or personal rela- 
tionships that could have appeared to inﬂuence the work reported in this paper. 
Supplementary Materials 
Supplementary material associated with this article can be found, in the online version, at 
doi:10.1016/j.dib.2025.112153 . 
References 
[1] B. Mathew, P. Saha, S.M. Yimam, C. Biemann, P. Goyal, A. Mukherjee, Hatexplain: a benchmark dataset for explain- 
able hate speech detection, in: Proceedings of the AAAI Conference on Artiﬁcial Intelligence, 35, 2021, pp. 14867–
14875, doi: 10.1609/aaai.v35i17.17745 . 
[2] K. Maity, S. Bhattacharya, S. Saha, M. Seera, A deep learning framework for the detection of Malay hate speech, IEEE 
Access 11 (2023) 79542–79552, doi: 10.1109/access.2023.3298808 . 
[3] R. Maskat, M. Faizzuddin Zainal, N. Ismail, N. Ardi, A. Ahmad, N. Daud, Automatic labelling of malay cyberbullying 
twitter corpus using combinations of sentiment, emotion and toxicity polarities, in: Proceedings of the 2020 3rd 
International Conference on Algorithms, Computing and Artiﬁcial Intelligence, December, 2020, pp. 1–6, doi: 10.1145/ 
3446132.3446412 . 
[4] Toxicity Small, GitHub. https://github.com/mesolitica/malaysian-dataset/tree/master/corpus/toxicity-small , 2020. 
(accessed 11 June 2025). 
[5] Snapshot Twitter, Hugging Face. https://huggingface.co/datasets/malaysia- ai/snapshot- twitter- 2022- 09- 03 , 2022. 
(accessed 11 June 2025). 
[6] Supervised sentiment for Bahasa Twitter, GitHub. https://github.com/mesolitica/malaysian-dataset/tree/master/ 
sentiment/supervised-twitter , 2022. (accessed 11 June 2025). 
[7] C. Baziotis, N. Pelekis, C. Doulkeridis, Datastories at semeval-2017 task 4: deep lstm with attention for message- 
level and topic-based sentiment analysis, in: Proceedings of the 11th international workshop on semantic evaluation 
(SemEval-2017), 2017, pp. 747–754, doi: 10.18653/v1/S17-2126 . 
[8] J.C. Tan, A bilingual Malay-English social Media dataset for binary hate speech detection, Mendel. Data 1 (2025), 
doi: 10.17632/mgv2n2vcb9.3 . 
[9] I. Bigoulaeva , V. Hangya , A. Fraser , Cross-lingual transfer learning for hate speech detection, in: Proceedings of the 
ﬁrst workshop on language technology for equality, diversity and inclusion, April, 2021, pp. 15–25 . 
[10] D.H. Lee , Pseudo-label: the simple and eﬃcient semi-supervised learning method for deep neural networks, in: 
Workshop on challenges in representation learning, June, 3, ICML, 2013, p. 896 . 
[11] K. Sohn, D. Berthelot, C.-L. Li, Z. Zhang, N. Carlini, E.D. Cubuk, A. Kurakin, H. Zhang, C. Raffel, FixMatch: simplifying 
semi-supervised learning with consistency and conﬁdence, ArXiv.org (2020), doi: 10.4 8550/arXiv.2001.076 85 . 
[12] J.C. Tan , L.Y. Ong , M.C. Leow , A multi-stage cyberbullying detection framework with hate speech classiﬁcation on 
Malaysian social Media, J. Informat. Web Eng. (2025) . 
[13] 200k 
English 
Malay, 
GitHub. 
https://github.com/asrafulsyifaa/Malay-Dataset/tree/master/dictionary/200k- 
english-malay , 2020. (accessed 11 June 2025). 

```
