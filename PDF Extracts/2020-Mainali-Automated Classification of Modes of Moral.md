---
title: "Automated Classification of Modes of Moral - PDF Extract"
source_pdf: "2020-Mainali-Automated Classification of Modes of Moral.pdf"
pages: 15
extracted_at: "2026-01-24T17:05:07.861332"
---

# PDF Extract: Automated Classification of Modes of Moral

**Source PDF:** 2020-Mainali-Automated Classification of Modes of Moral.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

HAL Id: hal-04163443
https://hal.science/hal-04163443v1
Preprint submitted on 17 Jul 2023
HAL is a multi-disciplinary open access
archive for the deposit and dissemination of sci-
entific research documents, whether they are pub-
lished or not.
The documents may come from
teaching and research institutions in France or
abroad, or from public or private research centers.
L’archive ouverte pluridisciplinaire HAL, est
destinée au dépôt et à la diffusion de documents
scientifiques de niveau recherche, publiés ou non,
émanant des établissements d’enseignement et de
recherche français ou étrangers, des laboratoires
publics ou privés.
Automated Classification of Modes of Moral Reasoning
in Judicial Decisions
Nischal Mainali, Liam Meier, Elliott Ash, Daniel L. Chen
To cite this version:
Nischal Mainali, Liam Meier, Elliott Ash, Daniel L. Chen. Automated Classification of Modes of
Moral Reasoning in Judicial Decisions. 2023. ￿hal-04163443￿

--- Page 2 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
Automated Classiﬁcation of Modes of Moral
Reasoning in Judicial Decisions
Nischal Mainali∗
NYU Abu Dhabi
nischal.mainali@nyu.edu
Liam Meier*
NYU Abu Dhabi
liam.meier@nyu.edu
Elliott Ash
University of Warwick
e.ash@warwick.ac.uk
Daniel Chen
Toulouse School of Economics
daniel.chen@iast.fr
Abstract
What modes of moral reasoning do judges employ? We construct a linear SVM
classiﬁer for moral reasoning mode trained on applied ethics articles written by
consequentialists and deontologists. The model can classify a paragraph of text
in held out data with over 90 percent accuracy. We then apply this classiﬁer to a
corpus of circuit court opinions. We show that the use of consequentialist reasoning
has increased over time. We report rankings of relative use of reasoning modes by
legal topic, by judge, and by judge law school.
1
Introduction
What is the role of moral reasoning in judge decision-making? To get at this question empirically
one must ﬁrst try to identify and measure the use of different modes of moral reasoning in judicial
decisions. The goal of this project is to use computational techniques to automatically classify legal
arguments by the type of moral reasoning used, if any.
The two broad moral frameworks most often used by philosophers are consequentialism and deontol-
ogy. For a consequentialist, what one ought to do is whatever brings about the best consequences. The
most famous form of consequentialism is utilitarianism, according to which agents are obligated to
do whatever brings about the most utility. For hedonist utilitarians like J.S. Mill and Jeremy Bentham,
pain is bad and pleasure is good. While philosophers have debated about how to measure utility, the
idea is broadly in line with preferring happiness over unhappiness [1].
In a deontological framework, an act is right if it conforms to a moral norm. For Kant, this is the
categorical imperative, the ﬁrst formulation of which holds that one should act only according to
a maxim which they can will to be a universal law [2]. The idea is that morality is decided by the
choice, rather than by the consequences.
Applied ethicists argue about the morality of various issues from these positions. Take the permis-
sibility of lying, for example. A consequentialist might argue that it would be permissible to lie if
∗These authors contributed equally.
.
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 3 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
the consequences of telling the lie would be better than not telling the lie. In contrast, typically a
deontologist would argue that it’s always immoral to lie because one could not will the acting of lying
to be a universal law.
Law commonly operates in correspondence with morality. Some actions are made illegal not because
of practical considerations, but because a society believes that the action is morally wrong. For
example, laws against sex work are often justiﬁed on moral grounds.
In the legal system, we can observe when judges reason according to either of these moral frameworks.
In the case of a contract, a deontological judge may hold that breach is always illegal, since it is
a break of a promise. A consequentialist judge may reason that certain breaches of contract are
acceptable, if, for example, a breach of contract would lead to a better outcome for the relevant parties.
This is known in law and economics as "efﬁcient breach."
In this paper we build a classiﬁer using tools from natural languagae processing and machine learning
to identify modes of moral reasoning. To train our classiﬁer, we use a corpus of articles in the applied
ethics literature. In these articles, philosophers argue about issues such as abortion, vegetarianism,
and war. The articles are annotated as taking a consequentialist or deontological stance. We ﬁnd that
the trained classiﬁer can accurately assign segments of these articles to the proper class.
We then apply the classiﬁer to circuit court opinions, where judges outline their reasoning for the
decision on a case. We use these opinions (dating back to 1883) to analyze trends in moral reasoning
in the U.S. legal system. We look at rates of consequentialist vs deontological reasoning over time,
according to where the individual was born, where the individual attended school, their sex, and the
party of the president under which they were nominated.
2
Automated Classiﬁcation of Moral Reasoning Modes
2.1
Training Data
The training corpus comprises all articles from the philosophy paper database PhilPapers.org tagged
with “Applied Consequentialism” or “Applied Deontology”. We ﬁltered out papers written in
languages other than English, papers that had both consequentialism and deontology tags, and papers
that obviously didn not belong. The resulting training corpus consists of 14 Consequentialist papers
and 11 Deontology papers. These were converted to plain text and artifacts that were not the text of
the paper were also expunged when possible.
Our data set is composed of a few large texts. But most text classiﬁcation techniques perform better
with larger corpora. Accordingly, we separated each of our Consequentialist and Deontology corpa
into 100 equally sized chunks. This introduces risk of overﬁtting, which is handled by tweaking the
random seed for proper separation of the data set into training and validation set.
Next we featurize the text. We have varied approaches such as bag of words, n-gram, tf-idf and so
on for featurizing the text. After some experimentation, we chose tf-idf with n-gram featurization.
In essence, we take phrases of up to 3-words-length and adjust them by their document frequency
to create a list of tf-idf n-grams. Each document is represented as a sparse vector representing the
frequency distribution over these n-grams.
2.2
Model Training
The preprocessing step leaves us with a vector assigned to each of the texts to use for training the
Machine Learning model. A natural choice for classiﬁcation problems such as ours is Linear Support
2
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 4 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
Vector Machine (SVM) or Naive Bayes. Initial performance of Naive Bayes was very poor, so we
focused our efforts on implementation of the SVM, which has been shown to be effective at text
classiﬁcation [3].
In broad terms, Linear-SVM tries to ﬁnd a hyperplane that neatly separates the vectors with ’Deontol-
ogy’ labelling and ’Consequentialist’ labelling. On one side of the hyperplane we ﬁnd consequentialist
text and on the other side we ﬁnd deontological texts. The prediction is made by locating the vector
of the test text according the the hyperplane.
During the initial steps in the training, we separate our data sets into training and validation sets.
After each training, the model predicts on the validation set and we tweak the training parameters to
increase accuracy and get sensible features. The major tuning component in training the model was
frequency threshold and stop words.
Our model very quickly approached a 100% prediction accuracy in the validation set, so the main
hyperparamenter tuning step was ﬁnding junk features in the prediction function and removing them.
For example: “New York University”, because some of the PDFs were downloaded on an NYU
license, which appears on each page of text in some of the documents, other overﬁtting type terms
(e.g. “fetus”), and high frequency junk phrases such as ’x-86’.
We did this by examining the prediction function. Linear-SVM predicts by assigning weights
(coefﬁcients) to the n-grams. So, we looked at the top 50 predictors for both Consequentialist
reasoning and Deontological reasoning and weeded out obviously irrelevant n-grams.
We also experimented with n-grams by adjusting the number of words per phrase. N=3 gave a good
result and increasing it further helped very little, if any, at the risk of creating overﬁtted features.
2.3
Feature Importance
The end product of the training is a weight assigned to each n-gram in the feature set. We rank the
n-grams by their weights. An n-gram with a positive weight means that it tends to occur in deontology
articles, while a negative weight signals that the text is consequentialist.
The set of most predictive n-grams for each category are visualized in Figure 1’s word clouds. Some
of the features are somewhat intuitive. For example, "pleasure" is a consequentialist value, while
"duty" is a deontological value.
3
Application to U.S. Circuit Courts
The application corpus is the univers of U.S. Circuit Court Opinions or the years 1883 through 2013.
Besides the text of the opinions, we have some relevant metadata, such as biographical details of the
judges writing the opinions.
3.1
Prominent Paragraphs
We would like to understand how our classiﬁer works in the judicial corpus. We ranked the paragraphs
in the corpus by the mode of moral reasoning used. We list some of those paragraphs here. We can
read these paragraphs and see how our classiﬁer works in the new context.
Strongly Deontological Prediction.
The following paragraphs are considered deontological by
the prediction model with high conﬁdence:
3
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 5 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
Figure 1: Most Predictive N-grams For Identifying Modes of Moral Reasoning
Consequentialist Word Cloud
Deontological Word Cloud
1.
Second, after determining that Congress intended "special dumping
duties" to be treated differently than normal customs duties,
Commerce compared 201 safeguard duties to both normal customs duties
and antidumping duties in order to determine how Congress would
have intended 201 duties to be treated in achieving the purposes
of the antidumping objectives.
Commerce found several significant
similarities between 201 safeguard duties and antidumping duties and
determined that 201 duties are "special dumping duties" because they
are "more like AD [antidumping duties] in purpose and function than
they are like ordinary customs duties." Id.
2.
[I]f an insurer who refuses to defend were estopped from asserting
the lack of coverage as a defense in a subsequent action, then the
insurer’s duty to indemnify would be coextensive with its duty to
4
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 6 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
defend.
[The Maine Law Court], however, ha[s] repeatedly stated
that an insurer’s duty to indemnify is independent from its duty
to defend and that its duty to defend is broader than its duty to
indemnify.
3.
By reason of its nature as a public institution St.
Elizabeths
Hospital owes a duty to the public in carrying out its difficult
responsibilities.
We have no occasion now to decide, however,
whether its public duty included an entirely separate duty to
Mrs.
Morgan.
There was a particular duty to the Court of General
Sessions, and in the circumstances of this case it was intertwined
with a duty to her.
See infra, note 12.
Strongly Consequentialist Prediction.
The following paragraphs are considered Consequentialist
by the predication function with high conﬁdence:
1.
No rule of bankruptcy practice and procedure is designed to
be considered in isolation.
Each rule is to be considered in
conjunction with every other rule.
What the entire body of rules
makes available to the practitioner and the bankruptcy judge is a
gestalt designed to constitute a functional whole.
The rules are
not a melange of independent parts.
The Advisory Committee alluded
to this in its preface to the rules:
"The proposed rules are not
divided into chapters related to the different types of debtor
relief chapters in the Code.
These rules apply in all chapter
cases except as a particular rule otherwise provides." Preface to
Rules and Forms, 11 U.S.C. XXI. One of the trustee’s most vigorous
arguments, therefore, is explicitly contradicted by the Preface to
the Rules.
He argues that Rule 1019(4) does not apply to Chapter
7 cases.
This is the rule that specifies that claims filed in the
superseded case shall be deemed filed in the Chapter 7 case.
The
Advisory Committee’s preface clearly reveals that the rules apply in
all chapter cases "except as a particular rule provides otherwise."
Rule 3002(a), requiring the filing of a claim in a Chapter 7 case,
does not "provide[ ] otherwise." So construed, there is but one
proper resolution of this case.
2.
Besides the nonrestrictive nature of the ordinary meaning of the
claim term "code," the doctrine of claim differentiation provides a
powerful argument against construing the term "code" restrictively,
to mean "spreading [**1615] code." Independent claim 1 of the ’966
patent uses the term "code," and dependent claim 5 recites, in
full, "The subscriber unit of claim 1 wherein the same code is a
spreading code." The clear implication of narrowing the term "code"
in dependent claim 5 by limiting the claim scope to cases in which
the claimed code "is a spreading code" is that the term "code" in
the independent claim is not limited to a spreading code.
5
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 7 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
Figure 2: Consequentialist Reasoning in the Circuit Courts, 1891-2013
3.
However, the evidence submitted by Clark does not stand alone.
Critically, Jerlene Bush and Mildred Bobo, both within job code 1433,
testified that at the time of the RIF, they trained two employees,
Carolyn Muse and James Russell Hunter, who then replaced them in
their positions.
See Appellants’ App.
at 496-98.
Yet Hunter was
placed in job code 1432, see id.
at 171, and Muse in 1402, see id.
at 170.10 Muse’s placement in another job code generally raises
questions about the claimed functional differences between job
codes.
But Hunter was placed into the very job code that plaintiffs
argue was pretextually separated from their own code for purposes of
discrimination.
On the basis of personal observation, two witnesses
from job code 1433 testified that they trained someone to perform
their jobs and that the person they trained was placed in job code
1432.
That is sufficient for a reasonable jury to find Seagate’s
differentiation of the two codes pretextual.
First, we see that the statements considered deontological all contain the word "duty," which is
intuitive. The statements categorized consequentialist include phrases like "Each rule is to be
considered in conjunction with every other rule", clearly emblemattic of consequential reasoning.
3.2
Time Series for Consequentialist Reasoning
Next we examine trends in consequentialist versus deontological reasoning over time. The plot is in
Figure 2. We see there is a discrete jump in consequentialism in the 1930s, indicating a major switch
in thought at the time.
6
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 8 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
Table 1: Top 10 Deontological Judges
1. TRIEBER, JACOB 21.2%
2. VAN DEVANTER, WILLIS 21.9%
3. COTTERALL, JOHN H. 24.4%
4. REED, HENRY THOMAS 24.6%
5. KENYON, WILLIAM 25.3%
6. MCDOWELL, HENRY CLAY 25.8%
7. HAWLEY, THOMAS PORTER 26.6%
8. BOOTH, WILBUR F. 27.5%
9. PHILIPS, JOHN FINIS 27.6%
10. PRITCHARD, JETER C. 28.1%
Table 2: Top 10 Consequentialist Judges
1. GORSUCH, NEIL M. 92.4%
2. MOORE, KIMBERLY ANN 91.3%
3. MARTIN, BEVERLY B. 90.2%
4. TATEL, DAVID STEPHEN 88.8%
5. MADDEN, JOSEPH 88.1%
6. CLEVENGER, RAYMOND CHARLES, III 87.9%
7. WILKEY, MALCOLM R. 87.8%
8. RICH, GILES SUTHERLAND 87.6%
9. STARR, KENNETH W. 87.5%
10. PATTERSON, ROBERT P. 87.3%
11. CHAMBERS, RICHARD H. 87.0%
There could be many factors driving this change. One possibility is that the hardships of the depression
brought disenchantment with prevailing norms; so moral attitudes shifted toward a focus on better
outcomes, rather than strict adherence to laws regardless of outcomes. Another potential factor is the
legal realism movement of the 1920s and 30s, which viewed law as a mean towards an end, rather
than an end in itself [4].
In the appendix, we report rankings of legal topics by moral reasoning. Estate law and family law
have a deontological bent. Administrative law tends to have a consequentialist bent. These are likely
driven by differences in popularity of legal areas over time.
3.3
Judge Rankings
It might also be illuminating to learn which judges are most consequentialist or most deontological.
For example, we might expected pragmatist judges such as Richard Posner to be consequentialist.
To ensure a large enough sample size, we ﬁlter out all judges that have less than 50 opinions in our
dataset.
Table 2 has the most deontological judges. Table 3 has the most consequentialist judges. We can see
that this appears to be driven by judge cohorts and time effects. Interestingly, the most consequentialist
judge, Neil Gorsuch, was recently promoted to the U.S. Supreme Court.
7
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 9 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
Figure 3: Consequentialist reasoning by Gender
3.4
Moral Reasoning and Judge Characteristics
Here we look at what biographical characteristics of judges are associated with the use of more
consequentialist versus deontological language.
First, we show in Figure 3 that there seems to be very little difference across gender in moral reasoning.
While, it appears that females are more likely to reason consequentially, the difference is too small to
be a reliable signal. This is also likely due to more female judges being in ofﬁce in later years, after
the upward shift.
Next, we ask in Figure 4 whether political party afﬁliations matter for modes of reasoning. There
appears to be almost no difference in consequentialist reasoning across party afﬁliations of the
President who appointed the judge.
Another factor determining differences across judges in the mode of reasoning is their legal training.
Are there differences between judges that come from different law schools? To answer this question
we took the average use of consequentialism for the judges for each law school. We then ranked
them. This ranking is reported in Table 1, along with the percentage difference of that school from
the global average. There are large differences by law school attended.
Perhaps moral reasoning style is determined by where one grew up as well as where one attended
law school. In Figure 5, we look at differences by birth state. We ﬁnd that judges from coastal states
seem to have a relatively deontological leaning.
4
Conclusion
This paper has demonstrated the use of computational linguistics and machine learning techniques
for the problem of classifying modes of moral reasoning in written texts. We show that even a small
corpus of training articles works for this purpose. We then apply the classiﬁer to the law to understand
how moral reasoning is used by judges.
8
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 10 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
Figure 4: Consequentialist reasoning by Political afﬁliation
Figure 5: Consequentialist reasoning by State
Red
corresponds to highly consequentialist states, blue corresponds to highly deontologial states.
9
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 11 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
Table 3: Ranking of Judge Consequentalism by Law School Attended
1. ’Washington and Lee University School of Law’, -19.6%
2. ’University of North Carolina School of Law’, -9.9%
3. ’University of Wisconsin Law School’, -9.5%
4. ’University of Oxford’, -3.5%
5. ’University of Nebraska College of Law’, 0.5%
6. ’St. Louis University School of Law’, 1.2%
7. ’University of California, Berkeley’, 1.7%
8. ’New York University School of Law’, 2.3%
9. ’Columbia Law School’, 2.8%
10. ’Cornell Law School’, 3.1%
11. ’Syracuse University College of Law’, 3.6%
12. ’Fordham University School of Law’, 4.0%
13. ’University of Arkansas School of Law’, 4.3%
14. ’University of Alabama School of Law’, 4.5%
15. ’Harvard Law School’, 5.9%
16. ’George Washington University Law School’, 5.9%
17. ’Notre Dame Law School’, 6.0%
18. ’Northwestern University School of Law’, 6.1%
19. ’University of Utah College of Law’, 7.2%
20. ’University of Washington School of Law’, 7.4%
21. ’University of Southern California Law School’, 7.6%
22. ’University of Virginia School of Law’, 7.8%
23. ’Louisiana State University Law School’, 8.4%
24. ’Yale Law School’, 8.4%
25. ’University of Minnesota Law School’, 8.5%
26. ’University of Chicago Law School’, 9.6%
27. ’Tulane University Law School’, 9.6%
28. ’University of Texas School of Law’, 11.1%
29. ’University of Mississippi School of Law’, 11.4%
30. ’University of Montana School of Law’, 11.7%
31. ’Stanford Law School’, 12.1%
32. ’Georgetown University Law Center’, 17.2%
Rankings of judge schools by consequentialism. Only includes law schools where at least 1000
opinions by attendees are included in the data set.
10
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 12 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
Future work should expand the training data to get a more comprehensive view of moral reasoning
language. We could also look at other moral frameworks, such as virtue ethics. We could also look at
peer effects in the judiciary, and whether sitting with judges of different moral style has an impact on
subsequent reasoning modes or decisions.
11
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 13 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
References
[1] Sinnott-Armstrong, Walter. "Consequentialism", The Stanford Encyclopedia of Philosophy (Winter 2015
Edition), Edward N. Zalta (ed.), URL = <https://plato.stanford.edu/archives/win2015/entries/consequentialism/>.
[2]Alexander, Larry and Moore, Michael. "Deontological Ethics", The Stanford Encyclopedia of Philosophy
(Winter 2016 Edition), Edward N. Zalta (ed.), URL = <https://plato.stanford.edu/archives/win2016/entries/ethics-
deontological/>.
[3] Joachims, Thorsten. Text categorization with Support Vector Machines: Learning with many relevant features.
In: Nédellec C., Rouveirol C. (eds) Machine Learning: ECML-98. ECML 1998. Lecture Notes in Computer
Science (Lecture Notes in Artiﬁcial Intelligence), vol 1398. Springer, Berlin, Heidelberg
[4] Posner, Richard A. "Legal Formalism, Legal Realism, and the Interpretation of Statutes and the Constitution,"
Case Western Reserve Law Review vol. 37, no. 2 (1986-1987): p. 179-217.
5
Appendix
5.1
Topics with Consquentialism Score
We can rank different legal topics by the percentage of opinions written within the topic that are labelled
consequentialist:
1. ’Wills, Trusts Estates’, 44.7%
2. ’Negotiable Instruments’, 50.2%
3. ’Family Law’, 52.6%
4. ’Torts’, 52.6%
5. ’Real Property’, 54.0%
6. ’Admiralty Maritime’, 54.9%
7. ’Native Peoples’, 56.7%
8. ’Judicial Ethics Conduct’, 57.1%
9. ’Natural Resources’, 57.7%
10. ’Mortgages Liens’, 58.0%
11. ’Real Estate Investment Trusts’, 58.6%
12. ’Damages Remedies’, 58.8%
13. ’Landlord Tenant’, 59.1%
14. ’Debtor Creditor’, 60.1%
15. ’Bankruptcy Law’, 60.4%
16. ’Alcohol Beverage’, 61.2 %
17. ’Motor Vehicles Trafﬁc Law’, 61.5%
18. ’Legal Malpractice’, 61.9%
19. ’Personal Property’, 62.3%
20. ’Eminent Domain’, 62.6%
21. ’Corporate Law’, 62.7%
22. ’Entertainment Law’, 63.3%
23. ’Contracts’, 63.8%
24. ’Professional Responsibility’, 64.9%
12
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 14 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
25. ’Civil Procedure’, 66.1%
26. ’Civil Rights’, 66.3%
27. ’Medical Malpractice’, 66.6%
28. ’Agency’, 66.7 %
29. ’Criminal Law’, 66.8%
30. ’Mergers Acquisitions’, 67.1%
31. ’Class Actions’, 67.6%
32. ’Transportation Law’, 68.5%
33. ’International Trade Law’, 68.5%
34. ’International Law’, 68.8%
35. ’Art Law’, 68.9%
36. ’Appellate Procedure’, 69.0%
37. ’Government’, 69.5%
38. ’Constitutional Law’, 69.7%
39. "Prisoners’ Rights", 69.9%
40. ’Partnerships Non-Corporate Business Entities’, 70.1%
41. ’Insurance Law’, 70.5%
42. ’Employee Beneﬁts’, 70.6%
43. ’Postal Service Law’, 71.6%
44. ’Alternative Dispute Resolution’, 72.0%
45. ’Habeas Corpus’, 72.8%
46. ’Gambling Lotteries Law’, 72.9%
47. "Workers’ Compensation", 73.2%
48. ’Elections Politics’, 73.7%
49. ’Securities Law’, 74.1%
50. ’Employment Law’, 74.5%
51. ’Franchise Law’, 74.5 %
52. ’Banking Finance’, 74.6,%
53. ’Land Use Planning Zoning’, 74.8%
54. ’Uniform Commercial Code’, 75.2%
55. ’Evidence’, 75.2%
56. ’Environmental Law’, 75.7%
57. ’Products Liability’, 75.7%
58. ’Agricultural Law’, 75.9%
59. ’Government Employees’, 76.0%
60. ’Copyright Law’, 76.1%
61. ’Military Law’, 76.2%
62. ’Consumer Law’, 76.5%
63. ’Patent Law’, 76.7%
64. ’Education Law’, 76.8%
13
 Electronic copy available at: https://ssrn.com/abstract=3205286 

--- Page 15 ---

 Electronic copy available at: https://ssrn.com/abstract=3205286 
65. ’Construction Law’, 77.0%
66. ’Tax Accounting’, 77.5%
67. ’Professional Corporations’, 77.8%
68. ’Antitrust Trade’, 77.8%
69. ’Immigration Naturalization’, 77.9%
70. ’Trade Secrets’, 78.6%
71. ’Trademark Law’, 78.8%
72. ’Intellectual Property Treaties Conventions’, 79.2 %
73. ’Conﬂict of Laws’, 79.2
74. ’Executive Compensation’, 80.0%
75. ’Communications Media’, 80.3%
76. ’Religious Non-Proﬁt Organizations’, 80.9%
77. ’Hazardous Material Law’, 81.3%
78. ’Health Law’, 81.7%
79. ’Government Contracts’, 81.9%
80. ’Privacy Information Law’, 82.1%
81. ’Sports Law’, 82.6%
82. ’Homeland Security’, 83.3%
83. ’Social Security’, 83.4%
84. ’Administrative Law’, 84.6%
85. ’Labor Law’, 84.6%
86. ’Energy Law’, 92.3%
87. ’Technology Law’, 93.9%
14
 Electronic copy available at: https://ssrn.com/abstract=3205286 

```
