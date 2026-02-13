---
title: "2023-Varshney-Muslim-Violence Bias Persists in Debiased GPT - PDF Extract"
source_pdf: "2023-Varshney-Muslim-Violence Bias Persists in Debiased GPT.pdf"
pages: 3
extracted_at: "2026-02-13T09:15:44.163594"
---

# PDF Extract: 2023-Varshney-Muslim-Violence Bias Persists in Debiased GPT

**Source PDF:** 2023-Varshney-Muslim-Violence Bias Persists in Debiased GPT.pdf
**Total Pages:** 3

---

## Content

```
--- Page 1 ---

Muslim-Violence Bias Persists in Debiased GPT
Models
Babak Hemmatian
Beckman Institute for Advanced Science and Technology
University of Illinois Urbana-Champaign
babak2@illinois.edu
Razan Baltaji
Department of Electrical and Computer Engineering
baltaji@illinois.edu
Lav R. Varshney
Department of Electrical and Computer Engineering
varshney@illinois.edu
Abstract
Abid et al. (2021) showed a tendency in GPT-3 to generate mostly violent com-
pletions when prompted about Muslims, compared with other religions. Two
pre-registered replication attempts found few violent completions and only a weak
anti-Muslim bias in the more recent InstructGPT, fine-tuned to eliminate biased
and toxic outputs. However, more pre-registered experiments showed that using
common names associated with the religions in prompts increases several-fold the
rate of violent completions, revealing a significant second-order anti-Muslim bias.
ChatGPT showed a bias many times stronger regardless of prompt format, suggest-
ing that the effects of debiasing were reduced with continued model development.
Our content analysis revealed religion-specific themes containing offensive stereo-
types across all experiments. Our results show the need for continual de-biasing of
models in ways that address both explicit and higher-order associations.
1
Introduction and Background
With increasing use of Large Language Models or LLMs (Min et al., 2021), any stereotypes they
reproduce have greater real-world effects (Varshney et al., 2019; Abbasi et al., 2019). Among these
models, OpenAI’s GPT series is hailed as especially effective for ‘zero-shot learning’, producing
reasonable text completions without further fine-tuning (Brown et al., 2020). But this means any
biases will affect all downstream tasks. We focus on the Muslim-violence bias, mentioned by OpenAI
developers (Brown et al., 2020; Radford et al., 2019), but studied systematically by Abid et al. (2021).
They used “Two Xs walked into a” as the prompt with X replaced by religious identities. Most
GPT-3 completions for Muslims were violent, as determined using keywords. Christians had the
next highest rate at 15%. The OpenAI developers of InstructGPT responded to concerns about
toxic generations by retraining GPT-3 using human ratings, actively minimizing undesirable outputs
(Ouyang et al., 2022). We examine the effects of this de-biasing on the Muslim-violence bias in
GPT-3 Instruct series and its successor, ChatGPT. We use disambiguated and extended versions of
Abid et al. (2021) prompts/measures. Because faith identifiers like "Muslim" are generic terms, we
refer to our replications as the "Generic" conditions.
37th Conference on Neural Information Processing Systems (NeurIPS 2023).
arXiv:2310.18368v2  [cs.CL]  9 Dec 2023

--- Page 2 ---

However, biased sources may not call Muslims violent, but share violent content related to them more
often (Nacos & Torres-Reyna, 2003). Text-generating algorithms may similarly identify names as
Islamic and produce more violent content while not calling Muslims “as-a-group” violent, especially
if de-biasing was focused on associations between group labels and stereotypes (Ouyang et al., 2022).
Comparing the rate of violent completions in response to prompts with first and last names popular
in different religions (the Common Names condition) against those containing only generic faith
identifiers like "Muslim" allows us to test this hypothesis.
Finally, to understand what drives the bias, we performed manual thematic analysis of the violent
completions across Generic and Common Name conditions. The results clarify the representations
these black-box models learn, guiding the development of training constraints to counteract biases.
2
Results
Details and data can be found here. We followed Abid et al. (2021) in using OpenAI’s default
parameters except for max_tokens, where we gave the models maximum space to demonstrate bias.
We expanded on the previous study’s violence keywords. To prevent false positives, we annotated
completions marked as violent using this method for attributing criminal acts to the target identities.
Average Cohen’s κ for inter-rater agreement was .72 across all annotated dimensions. Among shared
completions showing disagreement, we marked completions as belonging to a violent category if at
least one rater rated them as such.
Our generic conditions with InstructGPT were replications of Abid et al. (2021) with N=1,200. For
higher-order bias, we created made-up full names from lists of common religion-specific first and last
names (see OSF; N=960). Pooled estimates are shown in Figure 1-left. Religion and common name
use both increased the rate of violent completions. Violent texts contained both religion-agnostic
(e.g., armed robbery) and religion-specific (e.g., bombing and terrorism; see Figure 1-right) schemas,
some with extremely inflammatory or incoherent content (see OSF for the full texts).
ChatGPT shows a many times stronger Muslim-violence bias than InstructGPT. While the rate of
violent completions in the Common Names condition is comparable to InstructGPT, the explicit bias
exhibited in the Generic condition is much stronger, albeit still weaker than Abid et al. (2021) (partly
due to more stringent violence criteria). Hence, higher-order associations appear unchanged in more
recent models, while the effects of debiasing for explicit mentions of religions are heavily mitigated
with further development.
3
Summary
To summarize, the Instruct series’ fine-tuning has had shallow success in reducing violent generations,
but its effects do not override anti-Muslim biases and are largely limited to explicit mentions of
religious identity. Even those effects are heavily mitigated in the more recent ChatGPT. These findings
Figure 1: On the left, the proportion of violent completions (vertical axis) for Genericity (stacked)
and Religion (cluster) in InstructGPT (left bar) and ChatGPT (right bar). Error bars show Standard
Errors. The right figure shows the themes of violent completions using the same format.
2

--- Page 3 ---

highlight the need for continual de-biasing in LLMs using methods that also address higher-order
associations.
References
Mohsen Abbasi, Sorelle A. Friedler, Carlos Scheidegger, and Suresh Venkatasubramanian. Fairness
in representation: quantifying stereotyping as a representational harm. In Proceedings of the 2019
SIAM International Conference on Data Mining (SDM), 2019. URL https://epubs.siam.org/
doi/abs/10.1137/1.9781611975673.90.
Abubakar Abid, Maheen Farooqi, and James Zou. Large language models associate muslims with
violence. Nature Machine Intelligence, 3(6):461–463, 2021.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel
Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler,
Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray,
Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever,
and Dario Amodei. Language models are few-shot learners. In Advances in Neural Information
Processing Systems 33 (NeurIPS 2020), 2020. URL https://proceedings.neurips.cc/
paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html.
Bonan Min, Hayley Ross, Elior Sulem, Amir Pouran Ben Veyseh, Thien Huu Nguyen, Oscar Sainz,
Eneko Agirre, Ilana Heinz, and Dan Roth. Recent advances in natural language processing via large
pre-trained language models: A survey. 2021. URL https://arxiv.org/abs/2111.01243.
Brigitte L. Nacos and Oscar Torres-Reyna. Framing muslim-americans before and after 9/11. In
Pippa Norris, Montague Kern, and Marion Just (eds.), Framing Terrorism, pp. 141–166. Routledge,
New York, NY, 2003. doi: 10.4324/9780203484845.
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton,
Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, and
Ryan Lowe. Training language models to follow instructions with human feedback. 2022. URL
https://arxiv.org/pdf/2203.02155.pdf.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language
models are unsupervised multitask learners. 2019. URL https://life-extension.github.
io/2020/05/27/GPT%E6%8A%80%E6%9C%AF%E5%88%9D%E6%8E%A2/language-models.pdf.
Lav R. Varshney, Nitish Shirish Keskar, and Richard Socher. Pretrained ai models: Performativity,
mobility, and change. 2019. doi: 10.48550/arXiv.1909.03290.
3

```
