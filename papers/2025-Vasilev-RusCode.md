---



























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: QEE4XHK6
type: document
short_title: RusCode
year: 2025
first_author: "[[Viacheslav Vasilev]]"
last_author: "[[Dimitrov, Denis]]"
authors: "Vasilev, Viacheslav; Agafonova, Julia; Gerasimenko, Nikolai; Kapitanov, Alexander; Mikhailova, Polina; Mironova, Evelina; Dimitrov, Denis"
url: "https://aclanthology.org/2025.findings-naacl.425/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/JFUIN3WV/2025 - RusCode Russian Cultural Code Benchmark for Text-to-Image Generation.pdf"
national_ethnic_cultural: "Russian"
cultures_nationalities_list: "Russian"
languages_list: "English, Russian"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Russian, Social & Cultural Values"
key_contribution: "Proposes the RusCode benchmark, consisting of 1250 text prompts in 19 categories (art, folk traditions, etc.) to evaluate Russian cultural code representation in text-to-image models."
significance: "Mitigates Western/English-speaking cultural bias in generative CV models, ensuring unique cultural characteristics of diverse language groups are accurately represented."
tags: 
abstract: "Text-to-image generation models have gained popularity among users around the world. However, many of these models exhibit a strong bias toward English-speaking cultures, ignoring or misrepresenting the unique characteristics of other language groups, countries, and nationalities. The lack of cultural awareness can reduce the generation quality and lead to undesirable consequences such as unintentional insult, and the spread of prejudice."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "Ernie"
DATA_URL: "https://github.com/ai-forever/RusCode"
pdf_extract: "PDF Extracts/2025/2025-Vasilev-RusCode.md"
local_pdf: "[[PDFs/2025/2025-Vasilev-RusCode.pdf]]"
CONFERENCE: "NAACL 2025"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Social & Cultural Values"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "1250 prompts; 19 categories"
---
# RusCode: Russian Cultural Code Benchmark for Text-to-Image Generation

## Authors

[[Viacheslav Vasilev|Vasilev, Viacheslav]], [[Julia Agafonova|Agafonova, Julia]], [[Nikolai Gerasimenko|Gerasimenko, Nikolai]], [[Alexander Kapitanov|Kapitanov, Alexander]], [[Polina Mikhailova|Mikhailova, Polina]], [[Evelina Mironova|Mironova, Evelina]], [[Denis Dimitrov|Dimitrov, Denis]]

## Links

- **ACL Anthology:** https://aclanthology.org/2025.findings-naacl.425/

## Abstract

This paper introduces **RusCode**, a benchmark specifically designed to evaluate the **Russian Cultural Code** in text-to-image generation models. Current generative models exhibit a strong Anglo-Centric bias, often failing to correctly render concepts specific to Russian history, folklore, and daily life. RusCode consists of 1250 text prompts across 19 categories (e.g., fairytale characters like Baba Yaga, historical architecture, and specific cultural artifacts). The study compares major models (like Midjourney, Kandinsky, and Stable Diffusion), revealing significant gaps in cultural competence.

### Detailed Summary
Visual generative AI often behaves like a "tourist," rendering superficial stereotypes rather than accurate cultural representations. The authors argue that "Cultural Awareness" in Computer Vision is under-explored compared to NLP. They constructed RusCode to test deep cultural knowledge. For instance, testing if a model knows the difference between a generic "cottage" and an "Izba," or between a "pancake" and a "blin." They found that while Russian-developed models (like Kandinsky) perform better, global models often "hallucinate" Western aesthetics onto Russian prompts.

### Paper Outline
1.  **Introduction**: The Anglo-centric bias in T2I models.
2.  **RusCode Benchmark**: Methodology for selecting 19 categories (Art, Folk Traditions, Famous Names, Natural Objects, etc.).
3.  **Data Collection**: Curating 1250 prompts in Russian and English.
4.  **Experiments**: Side-by-side human evaluation of model outputs involving local and global models.
5.  **Results**: Quantitative analysis of "cultural hallucination" and fidelity.
6.  **Conclusion**: The need for culturally specific benchmarks in Vision-Language models.

### Methods Summary
*   **Taxonomy**: 19 cultural categories including "Folk Traditions," "Scientific Achievements," "Famous People," and "Architecture."
*   **Prompting**: 1250 prompts provided in both Russian (native) and English (translated) to test cross-lingual transfer of cultural concepts.
*   **Evaluation**: Human annotators evaluated generated images for cultural accuracy (e.g., "Does this look like a real samovar?").

### Results Summary
1.  **Western Bias**: Global models (e.g., Stable Diffusion) frequently default to Western visual tropes. A prompt for a "Russian wedding" might yield imagery that looks like an American wedding with slight modifications.
2.  **Local Competence**: Models trained explicitly on Russian data (Kandinsky) showed significantly higher fidelity to specific cultural artifacts (e.g., correctly rendering the details of Khokhloma painting).
3.  **Language Sensitivity**: Prompts in Russian yielded better cultural results than prompts in English, suggesting that the "cultural code" is tightly bound to the language embedding space.

### Conclusions
RusCode highlights that "high quality" image generation is not universal. A model can generate a photorealistic image that is culturally nonsensical (a "hallucination" of culture). Benchmarks like RusCode are essential for preserving digital cultural heritage and preventing the homogenization of visual culture by dominant AI models.

### Artifact Contributions
*   **RusCode Benchmark**: 1250 culturally specific text-to-image prompts.
*   **Evaluation Protocol**: A framework for assessing cultural fidelity in generative vision models.

## Data Description

RusCode is a benchmark dataset for evaluating cultural awareness of text-to-image generation models with respect to Russian visual culture. It consists of 1,250 text prompts in Russian and English across 19 cultural categories and 125 subcategories, each paired with reference images. The benchmark was used for human evaluation of four T2I models (Stable Diffusion 3, DALL-E 3, Kandinsky 3.1, YandexART 2), which are image generation models rather than LLMs.


## Notes

