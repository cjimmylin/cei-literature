---
title: "2023-Shmidman-Introducing DictaLM - A Large Generative Language Model for Modern - PDF Extract"
source_pdf: "2023-Shmidman-Introducing DictaLM - A Large Generative Language Model for Modern.pdf"
pages: 6
extracted_at: "2026-02-13T09:50:27.927248"
---

# PDF Extract: 2023-Shmidman-Introducing DictaLM - A Large Generative Language Model for Modern

**Source PDF:** 2023-Shmidman-Introducing DictaLM - A Large Generative Language Model for Modern.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

Introducing DictaLM - A Large Generative Language Model for Modern
Hebrew
Shaltiel Shmidman1,†, Avi Shmidman1,2,‡, Amir David Nissan Cohen2,†, Moshe Koppel1,2,†
1DICTA / Jerusalem, Israel
2Bar Ilan University / Ramat Gan, Israel
†{shaltieltzion,moishk,amirdnc}@gmail.com
‡avi.shmidman@biu.ac.il
Abstract
We present DictaLM, a large-scale language
model tailored for Modern Hebrew. Boasting
7B parameters, this model is predominantly
trained on Hebrew-centric data. As a com-
mitment to promoting research and develop-
ment in the Hebrew language, we release both
the foundation model and the instruct-tuned
model under a Creative Commons license1.
Concurrently, we introduce DictaLM-Rab,
another foundation model geared towards Rab-
binic/Historical Hebrew.
These foundation
models serve as ideal starting points for fine-
tuning various Hebrew-specific tasks, such as
instruction, Q&A (Cohen et al., 2023), senti-
ment analysis (Amram et al., 2018), and more
(Bareket and Tsarfaty, 2021). This release rep-
resents a preliminary step, offering an initial
Hebrew LLM model for the Hebrew NLP com-
munity to experiment with.
1
Introduction
Language models have revolutionized the realm
of natural language processing, facilitating signifi-
cant advancements in tasks ranging from sentiment
analysis to machine translation. As the breadth
and depth of these models expand, so does the
aspiration for linguistic diversity. Yet, while the
majority of state-of-the-art models cater predomi-
nantly to widely spoken languages, there exists a
vast landscape of languages and dialects that are
underrepresented in currently existing large-scale
language models. Hebrew is one such language.
In this paper, we make strides to bridge this
gap by introducing DictaLM - the first large-scale
language model crafted for Modern Hebrew. By
leveraging a dataset dominated by Hebrew-centric
content, our endeavor was not only to construct a
model adept at understanding and generating Mod-
ern Hebrew but also to lay down a foundation that
1For
specifics
on
the
license,
visit
https://
creativecommons.org/licenses/by-sa/4.0/
facilitates further advancements in the field. As part
of this initiative, we also present DictaLM-Rab,
a parallel model pretrained for Rabbinic/Historical
Hebrew, thereby encompassing the vast chronolog-
ical spectrum of the Hebrew language. This release
serves as a preliminary step, providing an initial ten-
tative version to the Hebrew NLP community as a
foundation for further refinements, adaptations, and
collaborative enhancements. Figure 1 demonstrates
example output from the instruct-tuned model.
Figure 1: We present two instances of DictaLM utiliza-
tion: in the first instance, the model exhibits common
sense reasoning, while in the second, it displays worldly
knowledge.
2
Datasets
In this section, we elucidate the datasets employed
for training and fine-tuning DictaLM. The assem-
blage of data, amassing a total of 7.5 billion tokens,
originates from a mixture of authentic sources; no
synthetic data was added. The pre-training phase
is followed by a fine-tuning stage through instruct
datasets derived from Hebrew Question-Answering
datasets and a translated version of the MPT In-
struct Dataset.
2.1
Pre-training Data
The dataset is built up of several different compo-
nents:
C4 [80%]. We start with the HeDC4 corpus
released by (Shalumov and Haskey, 2023), and
1
arXiv:2309.14568v1  [cs.CL]  25 Sep 2023

--- Page 2 ---

continue further cleaning it. We removed approxi-
mately 15% of the corpus using various techniques
including histograms, gibberish detectors, as well
as removing sentences that had a very high perplex-
ity when running through a Modern Hebrew BERT
model. In addition, we limited our training corpus
to contain only words in English and Hebrew, and
all other languages were reduced to a designated
<foreign> token to avoid cluttering the tokenizer
with non-Hebrew tokens. The resulting corpus con-
tains approximately 6B byte-pair tokens.
Other sources [20%]. We collected data from
various other sources including news sites, blogs,
tv and movie subtitles, novels, and more. This data
was also run through a similar cleaning process to
the C4 corpus, as described above, and resulted in
an additional 1.5B byte-pair tokens.
2.1.1
Instruct Data
Our instruct-tuning data contains a mixture of 2
different datasets, each processed and modified in
order to teach the model to follow as many different
instructions as possible.
QA Datasets. We take the HeQ (Cohen et al.,
2023) and ParaShoot (Keren and Levy, 2021) train-
ing datasets and format them as instructions. The
prompt contains the context paragraph followed by
the question, with a system instruction. The sys-
tem instruction starts with a general instruction (in
Hebrew) stating "Please read the following para-
graph and answer the question that comes after",
and 60% of the time also instructs the system to
format a specific type of response (e.g., "Short and
to the point", "Please cite the sentence to support
your answer", and more). We list a few examples
in Appendix A.
Translated MPT Instruct. We took the MPT In-
struct Dataset from huggingface2 and ran it through
a translation API. We then reformatted the prompt
to remove the constant structure, and left the ques-
tion only. We then added in each question three
times: Once with no system prompt, and twice with
two different prompts chosen based on the length
of the response, asking the model to be concise,
expand, answer in X sentences, etc. We list a few
examples in Appendix B.
2https://huggingface.co/datasets/
mosaicml/dolly_hhrlhf
3
Model architecture
3.1
Tokenizer
A major problem we encountered when attempting
to use other multilingual LLMs for Hebrew was
the tokenization. When the corpus contains a very
small percentage of a language, then the number
of tokens representing that language in the vocab-
ulary is significantly reduced. In addition, due to
the nature of UTF-8 encoding, byte-pair tokeniza-
tion methods result in even scarcer representation
of Hebrew in the vocabulary. As can be seen in
OpenAI’s GPT-3 tokenizer3, if one inserts a few
paragraphs of Hebrew text, the tokenizer will aver-
age 1.1 tokens per character.
We train our tokenizer using the byte-pair en-
coding (BPE) algorithm (Sennrich et al., 2015) on
our cleaned corpus with a vocabulary size of 56000.
The resulting tokenizer had a ratio of approximately
1.3 tokens per word.
3.2
Architecture
In this section, we detail the architectural frame-
work of DictaLM. Following recent work on large
language models, our network is based on the trans-
former architecture (Vaswani et al., 2017). Our
architecture encompasses several enhancements
aimed at boosting training stability and overall per-
formance:
Normalization. To improve training stability
and balance the input, we normalize the input of
each transformer layer before and after the attention
calculation. We use the LayerNorm1P normaliza-
tion with ϵ = 1e −5, which is a slightly modified
version of the FastLayerNorm normalization of-
fered by NVIDIA’s APEX library4.
GeLU Activation. As reported by (Hendrycks
and Gimpel, 2023), we use the GeLU activation
function.5
Rotary Embeddings. Shown to be effective
for extending the sequence length without a perfor-
mance trase-off, we use rotary positional embed-
ding (RoPE) with a 0.5% dimension percentage,
introduced by (Su et al., 2022), at each layer of the
network.
Separate embedding and output weights. As
shown by (Welch et al., 2020), separating the em-
beddings and the output weights leads to better
3https://platform.openai.com/tokenizer
4https://github.com/NVIDIA/apex
5We considered using other activations (such as SwiGLU
(Shazeer, 2020)), but in the end we went with GeLU
2

--- Page 3 ---

performance.
3.3
Training Details and Hyperparameters
We trained our model using the NeMo framework6
which is highly optimized for training compute-
heavy machine learning models on NVIDIA hard-
ware. We pre-trained the model on 8 H100 GPUs
with tensor parallel size of 2 for a total of 150
hours completing 2.5 epochs (∼18.5B tokens), and
then fine-tuning for instructions for 8 hours. The
training was done in a combination of bf16 and
fp8 precision using NVIDIA’s transformer engine7.
The training was done with a global batch size of
128. We used the FusedAdam optimizer, with an
initial learning rate of 0.00016, betas of 0.9, 0.95
and the Cosine-Annealing schedule with a warmup
of 750 steps and a minimum learning rate of 1e−5.
The details for the model size are listed in Table 1.
Max Sequence Length
2048
Num Layers
32
Hidden Size
4096
Intermediate Size
10880
Attention Heads
32
Table 1: Model size
3.4
DictaLM-Rab Model
In addition to the model we described above, we
also trained a model DictaLM-Rab for use with
Rabbinic Hebrew tasks. We used the same ap-
proach as above, adjusting the input corpus to con-
tain a large sampling of Rabbinic Hebrew data.
Specifically, we added a corpus of 1.2B tokens of
Rabbinic Hebrew texts taken from various sources
(e.g. Sefaria8, Dicta9). We combined this corpus
together with the modern Hebrew corpus that we
described above, sampling the data such that fifty
percent of the training sequences would be from
the Rabbinic Hebrew corpus (with oversampling).
The model uses the same tokenizer as DictaLM,
and was trained for a total of 1.5 iterations (∼12.5B
tokens).
We are pleased to also release this foundation
model, tailored to benefit researchers working on
Rabbinic Hebrew. This model can be used as a base
model for fine-tuning on specific tasks relevant to
6https://github.com/NVIDIA/NeMo
7https://github.com/NVIDIA/
TransformerEngine
8https://www.sefaria.org.il/
9https://library.dicta.org.il/
the Rabbinic Hebrew domain. Our internal exper-
iments reveal encouraging results with Rabbinic
texts, details of which will be shared in forthcom-
ing publications.
4
Drawbacks
Our model was trained on the full dataset without
any censorship for offensive or biased material,
and therefore it may generate sentences that are
offensive to some users.
Also, we would like to highlight that this project
is in its alpha phase.
While we are releasing
DictaLM to facilitate research endeavors, and
while we believe that it can serve as a useful foun-
dation for specific fine-tuned tasks in the realm of
Hebrew NLP, we acknowledge that the quality of
the model does not yet match industry standards.
5
Conclusion
We are pleased to present the three models de-
scribed within this paper: the two foundational
models (suitable as base models for further fine-
tuning for tasks concerning both Modern and Rab-
binic Hebrew), and the instruct model, fine-tuned
to address instruction prompts in Modern Hebrew.
The public release of these models aims to con-
tribute to the advancement of research and develop-
ment within the Hebrew NLP domain. The models
can be accessed via the following links:
• Foundation
model
DictaLM:
https:
//huggingface.co/dicta-il/
dictalm-7b
• Instruct
model
DictaLM-Instruct:
https://huggingface.co/
dicta-il/dictalm-7b-instruct
• Foundation
model
for
Rabbinic
He-
brew
DictaLM-Rab:
https:
//huggingface.co/dicta-il/
dictalm-rab-7b
References
Adam Amram, Anat Ben David, and Reut Tsarfaty.
2018.
Representations and architectures in neu-
ral sentiment analysis for morphologically rich lan-
guages: A case study from Modern Hebrew. In Pro-
ceedings of the 27th International Conference on
Computational Linguistics, pages 2242–2252, Santa
Fe, New Mexico, USA. Association for Computa-
tional Linguistics.
3

--- Page 4 ---

Dan Bareket and Reut Tsarfaty. 2021. Neural Model-
ing for Named Entities and Morphology (NEMO2).
Transactions of the Association for Computational
Linguistics, 9:909–928.
Amir DN Cohen, Hilla Merhav Fine, Yoav Goldberg,
and Reut Tsarfaty. 2023. Heq: a large and diverse
hebrew reading comprehension benchmark.
Dan Hendrycks and Kevin Gimpel. 2023. Gaussian
error linear units (gelus).
Omri Keren and Omer Levy. 2021. Parashoot: A he-
brew question answering dataset. In Proceedings of
the 3rd Workshop on Machine Reading for Question
Answering, pages 106–112.
Rico Sennrich, Barry Haddow, and Alexandra Birch.
2015. Neural machine translation of rare words with
subword units. CoRR, abs/1508.07909.
Vitaly Shalumov and Harel Haskey. 2023.
Hero:
Roberta and longformer hebrew language models.
arXiv:2304.11077.
Noam Shazeer. 2020. Glu variants improve transformer.
Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha,
Bo Wen, and Yunfeng Liu. 2022. Roformer: En-
hanced transformer with rotary position embedding.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. CoRR, abs/1706.03762.
Charles Welch, Rada Mihalcea, and Jonathan K. Kum-
merfeld. 2020. Improving low compute language
modeling with in-domain embedding initialisation.
4

--- Page 5 ---

A
Appendix: Instruct Examples from QA Datasets
 :פרומפט
 
האריזה אשר נחשפה באתר הוויאטנמי
 netnews 
 מעידה לכאורה על מספר פיצ'רים מעניינים שאפשר לצפות
להם מהמכשיר הבא של סמסונג: ראשית, נראה כי סמסונג בכל זאת עשויה שלא לאמץ מערך צילום כפול קלאסי 
כמו שראינו בשנים האחרונות אצל רוב היצרניות, אלא לאמץ מודל של 
מצלמה אחת משוכללת, בדומה לפיקסל 
2 שעושה
 
שימוש בטכנולוגיית 
 Machine Learning 
 .(ומרווחים בין פיקסלים בכדי ליצור אפקט "בוקה" )טשטוש
בנוסף לכך, נראה שלמצלמה של סמסונג תהיה טכנולוגייה מעניינת המאפשרת לה לעבור בין שני מצבי צמצם 
קיצוניים יחסית
 :F1.5 ו-F2.4. בכך המ
צלמה תוכל להתאים את עצמה לצילום בתנאי תאורה חלשים, ולעבור 
לצילום בתנאי תאורה בהירים וחזקים בכדי לתפוס את התמונות בצורה אופטימלית.
 
 ?על פי הפסקה הזאת, חוץ מתנאי תאורה חלשים, באילו תנאי תאורה תוכל המצלמה לצלם
 
 
 :תגובה
 
  התשובה לשאלה היא בהירים וחזקים. הסקתי את
התשובה הזאת מהמשפט: ולעבור לצילום בתנאי תאורה 
בהירים וחזקים בכדי לתפוס את התמונות בצורה אופטימלית
 
 
 
 :פרומפט
 
.קרא את הסעיף וענה על השאלה שמייד אחרי. אל תתאר, רק נתן תשובה קצרה וממוקדת
 
עוד במהלך שירותו בשם האימפריה העות
'
מאנית, ניהל בחשאי מגעים עם אויביה: רפובליקת רגוזה, הרפובליקה 
של ונציה, לסלו החמישי, מלך הונגריה, ואלפונסו החמישי, מלך אראגון. ב -
28
 
 בנובמבר1443
 , תוך כדי קרב בניש
נגד ההונגרים )בפיקודו של יאנוש הוניאדי(, פתח סקנדרבג במרד. הוא ערק לצד ההונגרי יחד עם 300
 אלבנ
ים 
ששירתו בצבא העו
ת'
מאני. לאחר מסע ארוך לאלבניה כבש את קרויה )לאחר שזייף מכתב מן הסולטאן אשר 
סייע לו להיכנס לעיר(. אחרי שכבש את טירת קרויה התנער מנאמנותו לנביא מוחמד ולסולטאן הטורקי, והכריז 
כי הוא נוקם בשם משפחתו ועמו. על התורן תלה דגל, שיהפוך אחר-
 כך לדגל
אלבניה ועל פי הדיווחים קרא: 
"
זה 
לא היה אני שהביא לכם את החופש, מצאתי אותו פה, ביניכם
"
. סקנדרבג יצר ברית עם לאומן אלבני אחר, גיירגי 
אריאניטה )Gjergj Arianit Komneni
) (, ונישא לבתו, ארדרוניקהMarina Donika Arianiti
 (. משלב זה ואילך
לחם בראש כוח לא גדול )כ-
20,000
 לוחמים( נגד העות
'
מאנים, כשהוא משתמש בעיקר בשיטות גרילה. 
 
 ?מה השם של מלך אראגון
 
 
 :תגובה
 
אלפונסו החמיש
י 
 
 
 :פרומפט
 
 בתחומי השגרירות ניסו המצרים להרדים את לוק באמצעות שתיית תה עם סם הרדמה אך הוא הערים עליהם
והצליח להקיא את המשקה. לאחר מכן הכניסו אותו למזוודה בצורת ארגז גדול. ב
 -
18
 
 בנובמבר1964
 
 הובילו
המצרים את המזוודה לנמל התעופה לאונרדו דה וינצ'י ברומא, לשם שליחתה לקהיר 
בטיסה מס' 784
 
 של חברת
התעופה  "יונייטד  ערב  איירליינס",  כ"מזוודה  דיפלומטית"  )Valise Diplomatique
  
-
  
 ,(במינוח  הבינלאומי
המיועדת  למשלוח  למשרד  החוץ  המצרי  בקהיר.  מחמת  חסינותה  הדיפלומטית,  עברה  המזוודה  את  המכס 
האיטלקי ללא בדיקה וחיפוש. כאשר הייתה המזוודה בדרכה אל ה
מטוס, שמע לפתע הסבל האיטלקי שהוביל 
אותה קולות חנוקים הבוקעים מן המזוודה וקוראים באיטלקית: "!Salvatemi! Aiutatemi
 " )"עזרו לי! הצילו
אותי!"(. הסבל העיד לאחר מכן: "...לפתע חשבתי, אלוהים, זהו איטלקי והערבים האלה חוטפים אותו - 
 ברנש
פוליטי או משהו כזה. מי יודע מ
ה הם יעשו לו שם בקהיר".
 
?באיזה משקה שמו ללוק סם הרדמה
 
.השתמש בציטוט מהפסקה כחלק מהתמיכה בתשובה שלך
 
 
 :תגובה
 
 על פי המשפט 'בתחומי השגרירות ניסו המצרים להרדים את לוק באמצעות שתיית תה עם סם הרדמה אך הוא
הערים עליהם והצליח להקיא את המשקה' אפשר להסיק 
שהתשובה היא תה. 
 
5

--- Page 6 ---

B
Appendix: Instruct Examples from Translated MPT-Instruct
 :פרומפט
 
.תן לי רשימה של דברים שאני יכול לעשות עם הרבה כסף נוסף
 
 .אנא הקדש מעט זמן וכתוב תשובה מפורטת במספר משפטים
 
 
 :תגובה
 
הנה מה שאתה יכול לעשות עם כסף נוסף: השקיעו בבורסה. לדוגמה, התשואה השנתית הממוצעת של S&P 
500
 מ-
1928
 
 עד2021
 
 היא11.82%
 . השקיעו בעצמכם על ידי רכישת שיעורים. אתה יכול גם לחקור תחביבים
חדשים להנאתך. כמה דוגמאות הן סקי, ציור או נגינה בגיטרה. לטייל ברחבי העולם כ
די לצבור חוויות חדשות 
ולחוות תרבויות חדשות. השקיעו בשוק הנדל"ן.
 
 
 
 :פרומפט
 
.תענה בבקשה קצר וקולע
 
 אמור לי אם אלה נהרות או אוקיינוסים: הנילוס, האמזונס, הגנגס, הדסון, הריין
 
 
 :תגובה
 
 .אלו נהרות
 
 
 
 :פרומפט
 
איך להשיג אימון אירובי יעיל ולשפר את המהירות שלך ולהרוו
יח יתרונות בריאותיים אחרים? 
 
 
 :תגובה
 
 בעידן  הזה,  שבהם  רבים  עסוקים  בעבודה,  במשפחה,  בגאדג'טים  אלקטרוניים,  במדיה  החברתית,  זה  הופך
למאתגר יותר ויותר למצוא את הזמן להתאמן. שמירה על בריאות תאפשר לכם ליהנות מהסחות הדעת הללו 
זמן רב יותר, אבל בדיחות בצד זה יגרמו לכם להרגיש מלאי אנרגיה, מוטיבציה ולהוציא
 
מכם את המיטב. כאשר 
תגליות חדשות באזורי נוף מיושמים בצורה נכונה, אינך צריך לבלות מספר שעות בחדר הכושר, אינך צריך לגווע 
ברעב כדי להשיג את המטרות שלך, הרעיון הזה היה מאוד מפתה אותי כאשר למדתי לראשונה על הספרינט 8 
תוכנית בחדר הכושר המקומי שלי. החלטתי לנסות את
 
זה! ספרינט 8 - 
 זה שגרה של20
 
 דקות, שבה אתה מבלה
את  30
  
  השניות הראשונות באימון ברמת האינטנסיביות הגבוהה ביותר )לצאת הכל( ואחריה90
  
 שניות של
התאוששות פעילה, חזור על זה 8 
 פעמים.. אתה יכול להשתמש באופניים, הליכון , אליפטי מה שמתאים לסגנון
שלך. בכל החיים שלי בה
יותי פעיל למדי, לספרינט 8 
 יש את האימון הקשה ביותר, אבל במשך שנה יכולתי לראות
תוצאות משמעותיות. הצלחתי לרוץ מהר יותר, להוריד לחץ דם, להוריד אחוזי שומן ולשפר את מסת השריר. 
המבדיל העיקרי בתוכנית זו הוא שהיא מערבת את כל שלושת סוגי סיבי השריר ומשחררת הורמוני גד
ילה 
הנגרמת על ידי פעילות גופנית כדי לעזור לגוף שלך להיות חזק יותר, רזה ובריא יותר. יתרון נוסף הוא שתוכנית 
זו באמת מפחיתה כל שינוי בפציעה שאדם עלול להתמודד איתו בריצה, הרמת משקל כבד וכו', ולכן מאפשרת 
לך לקיים את תוכנית האימונים במשך שנים רבות. נסה זאת והשיג
 
את היתרונות של פעילות גופנית יעילה. 
 
 
6

```
