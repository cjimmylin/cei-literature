---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: G4DI2ZZ7
type: journalArticle
short_title: "Multimodal machine learning for deception"
year: 2025
first_author: "[[Gargi Joshi]]"
last_author: "[[Ketan Kotecha]]"
authors: "Gargi Joshi; Vaibhav Tasgaonkar; Aditya Deshpande; Aditya Desai; Bhavya Shah; Akshay Kushawaha; Aadith Sukumar; Kermi Kotecha; Saumit Kunder; Yoginii Waykole; Harsh Maheshwari; Abhijit Das; Shubhashi Gupta; Akanksha Subudhi; Priyanka Jain; N. K. Jain; Rahee Walambe; Ketan Kotecha"
doi: 10.1038/s41598-025-92399-6
url: "https://www.nature.com/articles/s41598-025-92399-6"
external_pdf: "file:///Users/jimmylin/Zotero/storage/QL55WV8C/Joshi et al. - 2025 - Multimodal machine learning for deception detection using behavioral and physiological data.pdf"
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: 
tags: 
research_topic: "Truthfulness & Factuality"
abstract: "Deception detection is crucial in domains like national security, privacy, judiciary, and courtroom trials. Differentiating truth from lies is inherently challenging due to many complex, diversified behavioural, physiological and cognitive aspects. Traditional lie detector tests (polygraphs) have been widely used but remain controversial due to scientific, ethical, and practical concerns. With advancements in machine learning, deception detection can be automated. However, existing secondary datasets are limited—they are small, unimodal, and predominantly based on non-Indian populations. To address these gaps, we present CogniModal-D, a primary real-world multimodal dataset for deception detection, specifically targeting the Indian population. It spans seven modalities—electroencephalography (EEG), electrocardiography (ECG), electrooculography (EOG), eye-gaze, galvanic skin response (GSR), audio, and video—collected from over 100 subjects."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Hallucination & Truthfulness"
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: Dataset
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "NA"
pdf_extract: "PDF Extracts/2025/2025-Joshi-Multimodal machine learning for deception.md"
local_pdf: "[[PDFs/2025/2025-Joshi-Multimodal machine learning for deception.pdf]]"
---
# Multimodal machine learning for deception detection using behavioral and physiological data

## Metadata

**Authors:** Joshi, Gargi; Tasgaonkar, Vaibhav; Deshpande, Aditya; Desai, Aditya; Shah, Bhavya; Kushawaha, Akshay; Sukumar, Aadith; Kotecha, Kermi; Kunder, Saumit; Waykole, Yoginii; Maheshwari, Harsh; Das, Abhijit; Gupta, Shubhashi; Subudhi, Akanksha; Jain, Priyanka; Jain, N. K.; Walambe, Rahee; Kotecha, Ketan

**Year:** 2025

**Publication:** Scientific Reports

**Type:** journalArticle

**DOI:** [10.1038/s41598-025-92399-6](https://doi.org/10.1038/s41598-025-92399-6)

**Pages:** 8943

**Volume/Issue:** Vol. 15, Issue 1

## Links

- **URL:** https://www.nature.com/articles/s41598-025-92399-6
- **DOI:** https://doi.org/10.1038/s41598-025-92399-6

## Abstract

Deception detection is crucial in domains like national security, privacy, judiciary, and courtroom trials. Differentiating truth from lies is inherently challenging due to many complex, diversified behavioural, physiological and cognitive aspects. Traditional lie detector tests (polygraphs) have been widely used but remain controversial due to scientific, ethical, and practical concerns. With advancements in machine learning, deception detection can be automated. However, existing secondary datasets are limited—they are small, unimodal, and predominantly based on non-Indian populations. To address these gaps, we present CogniModal-D, a primary real-world multimodal dataset for deception detection, specifically targeting the Indian population. It spans seven modalities—electroencephalography (EEG), electrocardiography (ECG), electrooculography (EOG), eye-gaze, galvanic skin response (GSR), audio, and video—collected from over 100 subjects.

## Authors

[[Gargi Joshi]], [[Vaibhav Tasgaonkar]], [[Aditya Deshpande]], [[Aditya Desai]], [[Bhavya Shah]], [[Akshay Kushawaha]], [[Aadith Sukumar]], [[Kermi Kotecha]], [[Saumit Kunder]], [[Yoginii Waykole]], [[Harsh Maheshwari]], [[Abhijit Das]], [[Shubhashi Gupta]], [[Akanksha Subudhi]], [[Priyanka Jain]], [[N. K. Jain]], [[Rahee Walambe]], [[Ketan Kotecha]]

## Detailed Summary

This paper introduces CogniModal-D, a comprehensive multimodal dataset for deception detection specifically targeting the Indian population. The authors address a critical gap in existing deception detection research: most datasets are small, unimodal, and predominantly based on non-Indian (primarily Caucasian) populations, limiting their generalizability across cultural and ethnic groups. Deception detection is crucial for applications in national security, judiciary systems, courtroom trials, and privacy protection, but differentiating truth from lies remains challenging due to the complex interplay of behavioral, physiological, and cognitive factors.

The CogniModal-D dataset spans seven modalities collected from over 100 subjects: electroencephalography (EEG), electrocardiography (ECG), electrooculography (EOG), eye-gaze tracking, galvanic skin response (GSR), audio, and video. Data was collected through two experimental paradigms: a mock crime scenario (where participants were randomly assigned to commit or not commit simulated misbehavior and then answer questions) and a best friend scenario (storytelling about relationships with truth and lie conditions). Participants were balanced across age groups (18-25, 25-40, 40-60) and gender, with equal distribution of male and female subjects.

The study demonstrates that multimodal AI-based score-level fusion significantly outperforms unimodal methods, with performance improvements of up to 15% observed in mock crime and best friend scenarios. Notably, behavioral modalities (audio, video, gaze, GSR) proved more robust than neurophysiological modalities (EEG, ECG, EOG) for deception detection. The authors employed CNN and LSTM architectures for feature extraction and classification, with late fusion combining individual modality predictions. The findings highlight the importance of integrating multiple modalities for robust, scalable deception detection systems.

## Paper Outline

1. Introduction - Importance of deception detection and limitations of existing approaches
2. Related Work - Review of deception detection paradigms and multimodal fusion approaches
3. CogniModal-D Dataset
   - Dataset description (100+ subjects, 7 modalities)
   - Experimental tasks (mock crime, best friend scenarios)
   - Significance of each modality
   - Data acquisition and processing
4. Unimodal and Multimodal Deception Detection
   - Preprocessing and feature extraction for each modality
   - Multimodal fusion methodology
5. Results - Performance evaluation across modalities and fusion approaches
6. Discussion and Conclusions

## Methods Summary

Data collection involved 100+ Indian participants (balanced by age and gender) performing two tasks: mock crime interrogation and best friend storytelling. Seven modalities were simultaneously captured: EEG (28 channels), ECG (2 channels), EOG (2 channels), GSR, eye-gaze (Tobii), audio, and video. For EEG, preprocessing included bad channel interpolation, re-referencing, band-pass filtering (1-48 Hz), and ICA artifact removal; features extracted included Power Spectral Density, Hjorth parameters, and statistical entropy. Audio features included MFCCs, zero crossing rate, and spectral features processed through DNNs. Video used LBP preprocessing and CNN classification. Multimodal fusion employed score-level late fusion combining individual modality predictions. Statistical evaluation used accuracy, F1-score, precision, recall, and AUC metrics.

## Results Summary

Unimodal results varied across modalities, with behavioral modalities generally outperforming neurophysiological ones. Key findings: (1) Multimodal fusion achieved up to 15% improvement over best unimodal approaches in mock crime and best friend scenarios; (2) Behavioral modalities (audio, video, gaze, GSR) showed more robust discrimination than EEG, ECG, and EOG; (3) The best friend scenario showed different patterns than mock crime, reflecting the influence of emotional complexity on deception; (4) Age and gender-balanced sampling revealed no significant demographic biases in detection accuracy; (5) Score-level late fusion proved effective for combining heterogeneous modality predictions while maintaining interpretability of individual modality contributions.

## Conclusions

The study establishes CogniModal-D as a valuable resource for deception detection research, particularly for underrepresented Indian populations. Multimodal fusion significantly outperforms unimodal approaches, supporting the theoretical premise that deception manifests across multiple behavioral and physiological channels. The superior performance of behavioral over neurophysiological modalities suggests that observable cues (facial expressions, voice changes, gaze patterns) may be more reliable deception indicators than internal physiological states in naturalistic settings. The authors recommend multimodal approaches for future deception detection systems and highlight the need for culturally diverse datasets to develop generalizable AI systems.

## Artifact Contributions

- CogniModal-D dataset: 7-modality dataset from 100+ Indian subjects for deception detection
- Experimental paradigms: Mock crime and best friend scenarios for inducing truth/lie conditions

## Data Description

The paper presents CogniModal-D, a primary multimodal dataset for deception detection targeting the Indian population, spanning seven modalities (EEG, ECG, EOG, eye-gaze, GSR, audio, and video) collected from over 100 subjects. Data was gathered through mock crime and best friend scenario tasks. The study uses traditional machine learning models (CNN, LSTM, DNN, SVM) for unimodal and multimodal fusion-based deception detection, not large language models.


## Notes

