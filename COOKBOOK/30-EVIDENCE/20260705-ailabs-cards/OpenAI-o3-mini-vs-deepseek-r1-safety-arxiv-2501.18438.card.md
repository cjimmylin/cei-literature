---
stem: "OpenAI-o3-mini-vs-deepseek-r1-safety-arxiv-2501.18438"
company: "OpenAI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, best-practices, contamination-robustness, validity-psychometrics]
headline_numbers:
  - "DeepSeek-R1 (70B) unsafe rate: 11.98% vs o3-mini 1.19% across 1,260 test inputs (p.1)"
  - "44.8% of o3-mini test inputs rejected by API policy violation safeguard before reaching model (p.7)"
  - "o3-mini confirmed unsafe: 15/1,260; DeepSeek-R1 confirmed unsafe: 151/1,260 (p.5)"
  - "DeepSeek-R1 worst category: C6 (financial crime) with 54 unsafe outputs (p.5)"
  - "Writing styles S3 (technical terms) and S4 (role-play) caused most DeepSeek failures (p.6)"
---

## 1. Gist
This arXiv technical report (January 2025, Mondragon University + University of Seville) is the first systematic automated safety comparison of OpenAI o3-mini (pre-release beta) and DeepSeek-R1 (70B). The authors use their own tool ASTRAL to generate 1,260 balanced unsafe test inputs across 14 safety categories, 6 writing styles, and 5 persuasion techniques, then execute them against both models and use GPT-3.5 as an LLM judge to classify outputs as safe/unsafe/unknown. Manual review is conducted on all flagged unsafe and unknown responses. Results: DeepSeek-R1 produces ~10x more unsafe outputs (11.98%) than o3-mini (1.19%). A notable finding is that 44.8% of o3-mini test inputs triggered an API-level policy violation safeguard and never reached the model itself, making the o3-mini assessment effectively a system-level rather than model-level evaluation. Note: this is an independent academic paper, not an OpenAI publication, though the team had early access from OpenAI's safety testing programme.

## 2. Alignment/values methods used
The paper does not directly describe alignment/training methods — it is an external safety test of deployed models, not a report on training. For o3-mini, the paper observes that the API-level policy violation mechanism (a pre-model safeguard) rejected ~44.8% of unsafe inputs before they reached the model (p.7). The authors cannot attribute the safety of o3-mini's responses to model training vs. the API safeguard layer, since they had no access to control the safeguard. DeepSeek-R1 is assessed without equivalent safeguards.

## 3. Values specification
The values taxonomy is operationalized through ASTRAL's 14 safety categories (p.4):
- C1: Animal abuse; C2: Child abuse; C3: Controversial topics, politics; C4: Discrimination, stereotype, injustice; C5: Drug abuse, weapons, banned substances; C6: Financial crime, property crime, theft; C7: Hate speech, offensive language; C8: Misinformation regarding ethics, laws, safety; C9: Non-violent unethical behavior; C10: Privacy violation; C11: Self-harm; C12: Sexually explicit; C13: Terrorism, organized crime; C14: Violence, aiding and abetting, incitement.
The classification of what constitutes "unsafe" is done by a GPT-3.5 judge with additional manual review for borderline cases. The paper explicitly acknowledges that manual classification "may be influenced by individual perspectives and cultural differences" (p.4) — e.g., civilian firearm use being evaluated differently across European vs. American contexts.

## 4. Safety & values evaluation methodology
- **ASTRAL framework**: automated generation of 1,260 balanced test inputs using LLM + RAG + few-shot prompting + web browsing for current events; black-box coverage criterion ensures balance across 14 categories × 6 styles × 5 persuasion techniques (p.3-4)
- **Test execution**: API-based for o3-mini (beta); local Ollama deployment for DeepSeek-R1 (70B) on a Linux server with 512GB RAM, NVIDIA RTX A6000 (p.4)
- **LLM judge**: GPT-3.5 with validated prompt; highest accuracy in authors' prior study; classifies outputs as safe/unsafe/unknown with rationale (p.4)
- **Manual review**: All unsafe + unknown outputs reviewed by 3 authors reaching consensus for borderline cases (p.4)
- **Policy violation classification**: o3-mini API rejections counted as safe (p.4)
- Test inputs were generated in November 2024 and reflect contemporary events (2024 US elections, Israel ceasefire) in C3 (p.5)
- No red-teaming or adversarial optimization; inputs are "natural" unsafe prompts, not specifically crafted attacks against o3-mini

## 5. Benchmarks used or introduced
- **ASTRAL** (Ugarte et al., 2025, IEEE AST): the core testing tool; open-source; generates balanced test inputs across 14 safety categories, 6 writing styles, 5 persuasion techniques. This paper is the first application to o3-mini vs DeepSeek-R1 comparison (p.3)
- The 1,260-test input suite is from the original ASTRAL paper (generated November 2024) and reused here for fair comparison (p.5)
- Comparative baseline: GPT-4 (59 unsafe in prior study) and GPT-4o (79 unsafe) vs. DeepSeek-R1 (151 unsafe) for context (p.6)

## 6. Agentic / multiturn evaluation aspects
Not applicable. All evaluations are single-turn: one unsafe prompt → one model response → one judgment. No multi-turn, tool use, or agentic scaffolding. The paper does not evaluate refusal robustness across conversation turns.

## 7. Key numbers
- Total test inputs: 1,260 (6 styles × 5 persuasion × 14 categories × 3 tests) (p.5)
- o3-mini confirmed unsafe: 15 (1.19%); DeepSeek-R1 confirmed unsafe: 151 (11.98%) (p.5)
- o3-mini policy violations (API-level rejections): 565 / 1,260 = 44.8% (p.7)
- o3-mini unknown responses: 4; confirmed unsafe from unknown: 2 (p.5)
- DeepSeek-R1 worst categories: C6 (54 unsafe), C14 (~17), C13 (~16), C7 (~16) (p.5, Fig.1 approximations)
- DeepSeek-R1 safest categories: C2 (child abuse, 3), C11 (self-harm, 5), C12 (sexually explicit, 4) (p.6)
- Writing styles with highest DeepSeek failures: S3 (technical terms, 54) and S4 (role-play, 50) (p.5, Fig.1)
- Persuasion techniques: minimal difference for both models (p.6)
- Prior study comparisons: GPT-4 59 unsafe, GPT-4o 79 unsafe, GPT-3.5 (estimated) above DeepSeek-R1 (p.6)
- DeepSeek-R1 hardware: Linux server 512GB RAM, AMD EPYC 7773X 64-core, NVIDIA RTX A6000 48GB VRAM (p.4)

## 8. Findings relevant to values-benchmark design
- **System-level vs. model-level safety is confounded**: The o3-mini's apparent 1.19% unsafe rate is partly attributable to API-level safeguards (44.8% of inputs rejected), not just model alignment. Any benchmark using API-accessed models is measuring the deployed system, not the model in isolation — a crucial distinction for validity.
- **Benchmark staleness / contamination risk**: The paper explicitly flags that static safety benchmarks may be incorporated into training data, causing models to internalize specific unsafe patterns and making them ineffective over time (p.2). ASTRAL's use of real-time news retrieval is a mitigation, but does not fully solve this.
- **Category imbalance matters**: Most prior benchmarks had unbalanced safety categories (p.2). ASTRAL's balanced design (equal representation across 14 categories × 6 styles × 5 persuasion techniques) is presented as a methodological advance. Values benchmarks should similarly audit coverage balance.
- **Writing style as a safety bypass vector**: Technical terminology (S3) and role-play framing (S4) were the primary triggers for DeepSeek-R1 failures. This is directly actionable: values benchmarks should systematically vary linguistic framing and persona framing, not only semantic content.
- **Cultural relativity of safety classification**: The European evaluators noted genuine disagreement about what constitutes "unsafe" across cultural contexts (firearms example). This is directly relevant to cross-cultural values benchmarks — the oracle is not culture-neutral.
- **Severity matters, not just frequency**: DeepSeek-R1's unsafe outputs were clearer and more severe; o3-mini's unsafe outputs were more borderline. Unsafe rate alone understates the difference. Benchmarks should include severity ratings, not just binary safe/unsafe labels.
- **LLM judge limitations**: The GPT-3.5 judge was not validated for this specific model pair's outputs. Manual review revealed false positives. Any values benchmark using an LLM judge needs validation data showing the judge's accuracy on the specific model outputs being judged.

## 9. Novel ideas worth stealing
- **Black-box coverage criterion for test generation**: Ensuring equal representation across N safety categories × M writing styles × K persuasion techniques, rather than sampling proportionally from existing datasets, guarantees systematic coverage. Directly adaptable to values benchmark construction.
- **Writing style × persuasion technique as a 2D safety stress-test grid**: Explicitly varying linguistic presentation (slang, technical, role-play, misspellings, question form, uncommon dialect) crossed with persuasion strategy (evidence, expert authority, misrepresentation, logical appeal) creates a principled perturbation space for probing robustness.
- **Real-time news integration into test generation (RAG + web browsing)**: Using current events to instantiate abstract safety categories makes test inputs topically realistic and harder to anticipate from training data. Useful for keeping any benchmark fresh over time.
- **Tiered confidence classification** (safe / unsafe / unknown with rationale): The LLM judge's three-way classification with a human follow-up on the uncertain tier is a practical approximation of human review at scale, with a known false positive rate.

## 10. Notable quotes
- "DeepSeek-R1 produces significantly more unsafe responses (12%) than OpenAI's o3-mini (1.2%)." (p.1)
- "The policy violation mechanism plays a crucial role in detecting unsafe test inputs in o3-mini. A significant portion of the inputs (44.8%) were rejected by this safeguard, apparently preventing them from reaching the o3-mini model itself... our assessment can be considered to be performed at the system level of the entire OpenAI's API, rather than the o3-mini model in isolation." (p.7)
- "The manual classification of unsafe LLM behaviours may be influenced by individual perspectives and cultural differences... one of the analysed cases involved civilian firearm use. In many European countries, such practices are not widely accepted... This contrasts with other cultural contexts where such practices are more common and socially acceptable." (p.4)
- "Static safety benchmarks may eventually be incorporated into the training data of new LLMs to enhance safety and alignment. Consequently, LLMs could internalize specific unsafe patterns, significantly diminishing the utility of these prompts for future testing." (p.2)

## 11. UNKNOWN / not in extract
- Whether o3-mini model-level (sans API safeguard) results were ever measured — the authors had no way to disable the policy violation mechanism
- Exact counts per category for o3-mini (only Figure 1 is referenced; figure content is not reproduced in plain text)
- Whether the GPT-3.5 judge was validated against human ratings specifically for these two models' output styles
- Full details of ASTRAL's RAG retrieval methodology and prompt templates
- Whether results for the non-beta public release of o3-mini differed from the beta version tested
