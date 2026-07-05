---
stem: "2018-Crone-The Socio-Moral Image Database (SMID)"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, validity-psychometrics, cultural-linguistic, design-space]
task_format: "preference"
scoring_type: "human-rating"
dataset_size: 2941
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: []
headline_numbers:
  - "2,941 photographic images with normative ratings on 8 dimensions (p.1)"
  - "820,525 individual judgments from 2,716 participants (p.1)"
  - "Average of 34.88 ratings per image per dimension (p.8)"
  - "ICC(A,k) achieved 'excellent' reliability (ICC >= .75) on all dimensions (p.11)"
  - "All five moral foundations strongly positively correlated (all rs > .5, all ps < .001) (p.11)"
---
## 1. Gist
The Socio-Moral Image Database (SMID) is the largest standardized moral stimulus set assembled to date, containing 2,941 freely available photographic images spanning morally positive, negative, and neutral content. Images were crowdsourced from Flickr and Wikimedia Commons and validated against eight rating dimensions — valence, arousal, moral wrongness, and relevance to each of the five Moral Foundations Theory (MFT) dimensions (Care, Fairness, Ingroup, Authority, Purity). The SMID addresses critical gaps in moral psychology research: the over-reliance on text-based stimuli, narrow moral content coverage, the false assumption of discrete moral categories, and the neglect of morally positive stimuli. For values-alignment benchmarking, the SMID provides a validated, large-scale, multidimensional ground-truth dataset for testing whether computational systems correctly identify moral dimensions of real-world image content, offering a bridge from text-based moral benchmarks to visual moral perception.

## 2. Benchmark/eval design features
Not primarily a benchmark but a validated stimulus set. Core constructs measured: affective valence (1–5 scale), arousal (1–5 scale), moral wrongness/praiseworthiness (1–5 scale), and five moral foundation relevance scores (1–5, labeled as "not at all" to "very much"). Key design features: (1) bottom-up crowdsourcing to reduce researcher selection bias; (2) all images rated on all dimensions rather than sorting each image into one discrete category; (3) explicit representation of morally positive, negative, and neutral content; (4) Creative Commons licensing allowing broad reuse; (5) uniqueness scores computed for each image on each foundation to identify foundation-specific exemplars. The paper demonstrates that assuming discrete moral categories is empirically wrong—all five foundations are strongly intercorrelated (all rs > .5).

## 3. Task format & example item
No benchmark item format (this is a stimulus set). Rating task example: participants viewed an image and rated it on a 1–5 keyboard scale for each dimension. Sample dimension prompt (p.9, Table 3):

> "This image makes me think about the concept of CARE / HARM — NOT AT ALL (1) … VERY MUCH (5)"

Participants rated all images in an assigned batch (~30–40 images) on one dimension before moving to the next.

## 4. Scoring / grading methodology
Ratings are normalized to 1–5 Likert scales. Normative scores are means across raters, with standard deviations and standard errors reported per image. Inter-rater reliability assessed using ICC(A,1) (single-rating absolute agreement) and ICC(A,k) (averaged-rating reliability). ICC(A,k) achieved "excellent" (≥0.75) on all eight dimensions. A 95% CI width less than 1 scale point was achieved for most images on most dimensions. Uniqueness scores = image's score on a foundation minus its maximum score on any other foundation; positive scores indicate foundation-specific images.

## 5. Dataset construction & provenance
Images sourced via crowdsourcing on Amazon Mechanical Turk (AMT): 476 participants searched Flickr and Wikimedia Commons using 50+ moral concept prompts (e.g., "Care/Harm", "Sanctity/Degradation", "Loyalty/Betrayal"). After deduplication and filtering for minimum resolution (640×480), 4,092 images were obtained, supplemented by 362 researcher-contributed images (4,454 total). Screening by 285 AMT workers excluded famous people, prominent text, watermarks, and non-photographic images, yielding 2,941 images. All images are Creative Commons licensed. Normative rating sample: 1,812 AMT workers (US, ≥90% approval, ≥100 HITs) and 904 Australian undergraduates, with political balance requirements (≥5 liberal, ≥5 conservative, ≥5 moderate raters per image). Data available at https://osf.io/2rqad/.

## 6. Validity evidence
Extensive validity analysis provided: ICC(A,1) ranged from "poor" (foundations) to "fair" (valence, morality) for single ratings, but ICC(A,k) was "excellent" across all dimensions after averaging. A 95% CI of <1 scale point was achieved for most images at ~35 ratings/image. Valence and moral wrongness showed highest inter-rater consensus; MFT foundations showed lower consensus comparable to arousal. Face validity confirmed: high-uniqueness images visually represent their corresponding foundation. Bivariate distributions showed v-shaped relationships between foundation relevance and moral judgments (images with extreme moral ratings had high foundation relevance), confirming construct validity.

## 7. Saturation / discrimination
The dataset spans the full moral spectrum (positive, neutral, negative), unlike most prior sets. Uniqueness score distributions show that purely foundation-specific images are rare (most uniqueness scores cluster around or below zero), but at least 46 morally good and 21 morally bad images with positive uniqueness scores exist per foundation (p.14). Strong intercorrelations among foundations (all rs > .5) limit the ability to isolate single-foundation content, mirroring findings in basic emotion research. Some content domains (Fairness, Ingroup, Authority) are less well represented than Care and Purity due to difficulty of static image portrayal.

## 8. Multiturn / agentic aspects
n/a — single-rating task with no sequential interaction.

## 9. Key numbers
- 2,941 images in final stimulus set (p.8)
- 820,525 total ratings from 2,716 participants (p.1)
- 820,565 ratings obtained [slight discrepancy in text] (p.8)
- Average 34.88 ratings per image per dimension (p.8)
- Target: at least 20 ratings per image per dimension (p.8)
- ICC(A,k) "excellent" (≥.75) on all 8 dimensions (p.11)
- 95% CI <1 scale point for most images on most dimensions (p.11)
- All 5 MFT foundations correlated r > .5, p < .001 at image level (p.11)
- Individual-level Care-Fairness correlation averaged r = .32, negative in 11% of participants (p.13)
- ≥46 morally good and ≥21 morally bad images with positive uniqueness scores per foundation (p.14)
- Halving average CI width would require ~10,000–13,000 raters (p.11)
- 63% of images contain people, 17% animals, 15% landscapes (p.8)

## 10. Pitfalls & limitations
- Rater sample limited to US AMT workers and Australian undergraduates; politically balanced but not demographic-balanced (gender, religiosity, vegetarianism all uncontrolled) (p.20)
- Creative Commons licenses are disproportionately US-issued; content reflects a WEIRD (Western, Educated, Industrialized, Rich, Democratic) photographer bias (p.21)
- Fairness, Ingroup, and Authority foundations underrepresented compared to Care and Purity because abstract social dynamics are difficult to depict in static images (p.20-21)
- Image uniqueness is unusual — most images score on multiple foundations simultaneously, making single-foundation studies hard (p.14)
- ICC(A,1) values for foundations are "poor" (<.40) by clinical guidelines, indicating high individual variability (p.10)
- Photographs are not fully representative of everyday moral life due to "capture bias" (p.21)
- Organized around MFT which is theoretically contested; does not cover Liberty foundation (p.21)

## 11. Novel ideas worth stealing
- **Bottom-up crowdsourced image collection** with concept-based search prompts to reduce researcher bias — transferable to any multimodal moral benchmark.
- **Rating all items on all dimensions** rather than assigning each item to a single category; this directly tests for moral complexity and co-occurrence, an underexplored feature in text-based benchmarks.
- **Uniqueness scores** (item score on target dimension minus max on all other dimensions) as a way to quantify and select pure exemplars of a construct — applicable to any multidimensional values benchmark.
- **Deliberate sampling of the full moral spectrum** (positive, neutral, negative) — most text-based moral benchmarks focus on violations only; adding prosocial and neutral items enables richer discrimination and theory testing.
- **Political balance requirement** in rater composition (at least 5 liberal, 5 conservative, 5 moderate per item) — a simple control for ideological confounds in any crowdsourced moral annotation.
- **Precision-focused item-level reporting** (95% CI widths per item, not just aggregate ICC) — allows dataset users to select subsets meeting specific reliability thresholds.

## 12. Notable quotes
- "A major obstacle for the design of rigorous, reproducible studies in moral psychology is the lack of suitable stimulus sets." (p.1)
- "Whereas the English lexicon is estimated to contain around one million words, a Flickr search for the term 'house' currently returns around 3.5 million unique images." (p.3)
- "All five foundations were strongly positively correlated (all rs > .5, all ps < .001), suggesting that relatively 'pure' instances of individual foundations (i.e., scoring highly on one, but low on all others) may be somewhat rare." (p.11)
- "Rather than reflecting random noise in the ratings, we suggest that rating variability can be meaningfully accounted for by at least three separate substantive sources... ambiguity... ambivalence... divisiveness." (p.15)

## 13. UNKNOWN / not in extract
- Whether the SMID has been used to train or evaluate any computational moral classification models (mentioned as a future application but no results reported)
- Inter-rater reliability statistics for individual demographic subgroups
- Exact number of images with positive uniqueness scores for Liberty foundation (omitted as Liberty was not included)
- Full list of screening statistics (what percentage were excluded for each criterion)
- Detailed comparison statistics between AMT and undergraduate rater populations
