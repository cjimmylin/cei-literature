# Moral Psychology Reclassification — Agent Instructions

**Date:** 2026-03-12
**Task:** Classify each paper's engagement with moral psychology theories

---

## Your Task

For each paper in your assigned batch JSON:

1. Read the paper's abstract from its YAML frontmatter (`abstract:` field or `## Abstract` body section)
2. If `has_extract` is true, read the PDF extract (first ~4000 words) from the path given in `pdf_extract_path`
3. Classify the paper's engagement with moral psychology using the categories below
4. Write your results to the output JSON file

---

## Classification Categories

You must classify each paper into one or more of these 8 categories, or "N/A" if the paper does not substantively engage with any moral psychology theory.

### 1. Moral Foundations Theory
**Theorists:** Jonathan Haidt, Jesse Graham, Craig Joseph
**Core idea:** Morality is built on 5-6 innate psychological foundations: Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation, (Liberty/Oppression)
**Instruments:** Moral Foundations Questionnaire (MFQ), Moral Foundations Dictionary (MFD), Moral Foundations Twitter Corpus (MFTC), Moral Foundations Vignettes (MFV)
**Qualifies if:** Paper explicitly references Moral Foundations Theory, uses MFQ/MFD/MFTC, discusses the specific 5-6 foundations framework, or cites Haidt/Graham in the context of moral foundations

### 2. Dual Process Theory (Moral Cognition)
**Theorists:** Joshua Greene
**Core idea:** Moral judgments arise from two competing systems — fast/automatic emotional responses (favoring deontological conclusions) vs. slow/deliberate cognitive reasoning (favoring utilitarian/consequentialist conclusions)
**Qualifies if:** Paper discusses the dual-process model specifically in moral judgment contexts, references Greene's work on moral cognition, or studies the emotional/rational tension in moral decision-making
**Does NOT qualify:** General dual-process theory (Kahneman) without moral judgment application

### 3. Dyadic Morality
**Theorists:** Kurt Gray, Chelsea Schein
**Core idea:** All moral judgment reduces to perceived harm in an agent-patient dyad (someone intentionally harms someone)
**Key concepts:** Moral typecasting, Theory of Dyadic Morality (TDM), moral agent vs. moral patient
**Qualifies if:** Paper explicitly discusses dyadic morality, moral typecasting, or Gray/Schein's framework

### 4. Social Intuitionist Model
**Theorists:** Jonathan Haidt
**Core idea:** Moral judgments are primarily intuitive (gut feelings), and moral reasoning is post-hoc rationalization — "the emotional dog and its rational tail"
**Key concepts:** Moral dumbfounding, moral intuition primacy, social persuasion in moral judgment
**Qualifies if:** Paper discusses the primacy of moral intuitions over reasoning, moral dumbfounding, or Haidt's intuitionist model specifically
**Note:** Haidt's MFT work is category 1; his intuitionist model is this category. Papers may reference both.

### 5. Moral Identity
**Theorists:** Karl Aquino, Dan Reed
**Core idea:** The degree to which being a moral person is central to one's self-concept predicts moral behavior
**Key concepts:** Moral self-concept, moral identity internalization/symbolization, self-importance of moral identity
**Qualifies if:** Paper discusses moral identity as a psychological construct, references Aquino/Reed's framework, or studies how self-concept relates to moral behavior

### 6. Cognitive Developmental
**Theorists:** Lawrence Kohlberg, Jean Piaget, James Rest
**Core idea:** Moral reasoning develops through invariant stages from pre-conventional (self-interest) through conventional (social norms) to post-conventional (universal principles)
**Instruments:** Defining Issues Test (DIT), Heinz dilemma, Moral Judgment Interview (MJI)
**Qualifies if:** Paper references Kohlberg's stages, Piaget's moral development, Rest's neo-Kohlbergian model, or uses DIT

### 7. Value Pluralism / Schwartz
**Theorists:** Shalom Schwartz
**Core idea:** 10 basic human values (Universalism, Benevolence, Conformity, Tradition, Security, Power, Achievement, Hedonism, Stimulation, Self-Direction) form a motivational circumplex with predictable conflicts and compatibilities
**Instruments:** Schwartz Value Survey (SVS), Portrait Values Questionnaire (PVQ)

**⚠️ CRITICAL GUARDRAIL — READ CAREFULLY:**
Generic mentions of "values", "tradition", "power", "security", "achievement", "conformity", etc. do **NOT** qualify for this category. These are common English words used in thousands of papers about AI ethics, cultural values, power dynamics, etc.

**ONLY qualifies if the paper:**
- Explicitly names Schwartz's theory/framework/circumplex/model
- Uses SVS or PVQ instruments
- Discusses the 10-value circumplex structure with its conflict/compatibility axes
- Cites Schwartz's original work in the context of value theory

**Does NOT qualify:**
- Papers discussing "human values" generically
- Papers about "cultural values" without referencing Schwartz specifically
- Papers mentioning "tradition" or "power" as general concepts
- Papers about value alignment in AI that don't reference Schwartz's specific framework

### 8. Trolley / Dilemmas (Psych)
**Core idea:** Using moral dilemmas (trolley problem, footbridge, Moral Machine) as a **psychological research methodology** to study how people make moral judgments
**Key instruments:** Trolley problem variants, Moral Machine experiment, sacrificial dilemmas
**Qualifies if:** Paper uses trolley-type dilemmas as a methodology for studying moral psychology, references the Moral Machine experiment, or uses sacrificial dilemmas to study moral cognition
**Does NOT qualify:** Philosophical discussion of trolley problems as thought experiments (that's normative ethics, not moral psychology)

---

## Critical Distinction: Normative Ethics vs. Moral Psychology

**Normative ethics** asks "What SHOULD we do?" — prescriptive philosophical frameworks:
- Utilitarianism, deontology, virtue ethics, care ethics, contractualism
- These are NOT moral psychology

**Moral psychology** asks "How DO humans actually make moral judgments?" — descriptive empirical frameworks:
- The 8 categories above are moral psychology
- They study the psychological mechanisms, developmental stages, and cognitive processes of moral reasoning

**A paper about deontology is NOT moral psychology** unless it empirically studies deontological reasoning using one of the above frameworks (e.g., Greene's dual-process theory studying utilitarian vs. deontological processing).

---

## Output Format

For each paper, produce a JSON object:
```json
{
  "filename": "2023-Smith-AI Ethics.md",
  "moral_psychology": "Theory1, Theory2",
  "confidence": "high",
  "reasoning": "1-2 sentences explaining classification"
}
```

**Rules:**
- `moral_psychology`: Comma-separated category names (exactly as listed above), or `"N/A"` if no engagement
- `confidence`: `"high"` (clear/explicit engagement), `"medium"` (implicit/partial engagement), `"low"` (borderline/uncertain)
- `reasoning`: Brief justification — what evidence led to this classification
- Most papers (~85-90%) will be `"N/A"` — moral psychology theories are specialized and only a minority of AI ethics papers engage with them substantively
- Multi-category assignments are valid but should be justified (e.g., a paper using MFT + trolley methodology)

---

## Procedure

1. Read your batch file: `logs/YYYYMMDD-moral_psych_batch_NN.json`
2. For each entry:
   a. Read the paper file from `papers/{filename}`
   b. Extract the abstract from YAML `abstract:` field or `## Abstract` section
   c. If `has_extract` is true, read `{pdf_extract_path}` (use first ~4000 words)
   d. Classify based on abstract + extract content
   e. Record your classification
3. Write all results to: `logs/YYYYMMDD-moral_psych_agent_NN.json`

**Important:** Base classification on actual content, not the paper's `current_moral_psychology` field (which is the old keyword-based classification being replaced).
