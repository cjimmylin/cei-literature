# Anthropic Overview

## Lab Overview

Anthropic is an AI safety company founded in 2021, dedicated to building reliable, interpretable, and steerable AI systems. The company's mission centers on AI safety research, with a focus on developing techniques to make large language models helpful, harmless, and honest (the "HHH" criteria). Anthropic has pioneered several influential safety techniques including Constitutional AI (CAI), Reinforcement Learning from Human Feedback (RLHF), and Reinforcement Learning from AI Feedback (RLAIF).

Anthropic operates under a Responsible Scaling Policy (RSP) that defines AI Safety Levels (ASL-1 through ASL-4) to categorize models based on their potential risks and required safeguards. This framework guides deployment decisions and ensures appropriate safety measures are in place before releasing increasingly capable models.

---

## Timeline of Claude Models

| Date | Model | Key Milestone |
|------|-------|---------------|
| July 2023 | Claude 2 | First major public release, 100K context window |
| March 2024 | Claude 3 (Haiku, Sonnet, Opus) | Model family launch, vision capabilities, 200K context |
| June 2024 | Claude 3.5 Sonnet | Significant capability improvements |
| October 2024 | Claude 3.5 Sonnet (Updated) | Computer use capability introduced |
| October 2024 | Claude 3.5 Haiku | Cost-effective, faster variant |
| February 2025 | Claude 3.7 Sonnet | First hybrid reasoning model with extended thinking |
| May 2025 | Claude 4 Opus & Sonnet | ASL-3 deployment, enhanced agentic capabilities |
| September 2025 | Claude Sonnet 4.5 | Hybrid reasoning, improved coding |
| November 2025 | Claude Opus 4.5 | State-of-the-art frontier model |

---

## Summary Table of All Models

| Model | Release | Context Window | Key Capabilities | Safety Level |
|-------|---------|----------------|------------------|--------------|
| Claude 2 | July 2023 | 100K tokens | General assistant, coding, analysis | ASL-2 |
| Claude 3 Haiku | March 2024 | 200K tokens | Fast, cost-effective, vision | ASL-2 |
| Claude 3 Sonnet | March 2024 | 200K tokens | Balanced performance, vision | ASL-2 |
| Claude 3 Opus | March 2024 | 200K tokens | Highest capability, vision | ASL-2 |
| Claude 3.5 Haiku | October 2024 | 200K tokens | Improved speed/cost ratio | ASL-2 |
| Claude 3.5 Sonnet | June/Oct 2024 | 200K tokens | Computer use, enhanced reasoning | ASL-2 |
| Claude 3.7 Sonnet | February 2025 | 200K tokens | Extended thinking, hybrid reasoning | ASL-3 |
| Claude 4 Opus | May 2025 | 200K tokens | Advanced reasoning, agentic tasks | ASL-3 |
| Claude 4 Sonnet | May 2025 | 200K tokens | Balanced, agentic capabilities | ASL-3 |
| Claude 4.5 Haiku | 2025 | 200K tokens | Fast, efficient processing | ASL-3 |
| Claude Sonnet 4.5 | September 2025 | 200K tokens | Hybrid reasoning, strong coding | ASL-3 |
| Claude Opus 4.5 | November 2025 | 200K tokens | State-of-the-art, frontier capabilities | ASL-3 |

---

## Detailed Model Information

### Claude 2 (July 2023)

**Key Capabilities:**
- 100,000 token context window
- General-purpose assistant for analysis, writing, and coding
- Improved performance over Claude 1.x

**Safety Features:**
- RLHF training for helpfulness and harmlessness
- Constitutional AI principles
- Red team testing for harmful outputs

---

### Claude 3 Family (March 2024)

The Claude 3 family introduced a tiered approach with three models optimized for different use cases.

#### Claude 3 Haiku
- **Focus:** Speed and cost efficiency
- **Best for:** High-volume, latency-sensitive applications
- **Vision:** Yes (image understanding)

#### Claude 3 Sonnet
- **Focus:** Balanced performance and cost
- **Best for:** Enterprise applications requiring quality and efficiency
- **Vision:** Yes (image understanding)

#### Claude 3 Opus
- **Focus:** Maximum capability
- **Best for:** Complex reasoning, research, creative tasks
- **Vision:** Yes (image understanding)

**Shared Features (Claude 3 Family):**
- 200K token context window
- Multimodal capabilities (text and images)
- Improved instruction following
- Enhanced multilingual support
- Constitutional AI training
- Comprehensive red teaming

---

### Claude 3.5 Sonnet (June 2024, Updated October 2024)

**Key Capabilities:**
- Significant improvements in reasoning and coding
- Computer use capability (October 2024 update)
- Enhanced tool use and function calling
- Improved performance on benchmarks

**Safety Features:**
- Agentic safety evaluations
- Prompt injection resistance testing
- Computer use specific safety measures
- ASL-2 classification

**Notable Characteristics:**
- First model with computer use capability (screenshot, mouse, keyboard control)
- Strong performance on SWE-bench and coding tasks

---

### Claude 3.5 Haiku (October 2024)

**Key Capabilities:**
- Faster inference than Claude 3 Haiku
- Improved reasoning while maintaining speed
- Cost-effective for high-volume applications

**Safety Features:**
- Constitutional AI training
- Red team evaluations
- ASL-2 classification

---

### Claude 3.7 Sonnet (February 2025)

**Key Capabilities:**
- **Extended Thinking Mode:** First hybrid reasoning model that can show its reasoning process
- Improved performance on complex reasoning tasks (GPQA Diamond: 84.8%)
- Strong coding abilities (SWE-bench: 62.3%)
- Tool use and agentic workflows

**Safety Features:**
- **ASL-3 Classification:** First model requiring ASL-3 safeguards
- Enhanced CBRN (Chemical, Biological, Radiological, Nuclear) evaluations
- Agentic safety testing including prompt injection resistance
- Extended thinking safety measures

**Notable Characteristics:**
- Hybrid model: can operate in standard mode or extended thinking mode
- Extended thinking provides transparency into reasoning process
- Thinking tokens are separate from output tokens

---

### Claude 4 Opus & Claude 4 Sonnet (May 2025)

**Key Capabilities:**
- Advanced reasoning and analysis
- Strong agentic task performance
- Enhanced coding and technical capabilities
- Improved instruction following

**Safety Features:**
- **ASL-3 Deployment:** Both models deployed under ASL-3 safeguards
- Comprehensive CBRN evaluations
- Cyber capabilities assessments
- Agentic safety testing
- Enhanced monitoring and deployment controls

**Notable Characteristics:**
- First Claude 4 generation models
- Significant capability improvements across benchmarks
- Designed for autonomous and semi-autonomous workflows

---

### Claude 4.5 Haiku

**Key Capabilities:**
- Fast, efficient processing
- Improved performance over Claude 3.5 Haiku
- Cost-effective for production applications

**Safety Features:**
- ASL-3 safeguards
- Constitutional AI training
- Comprehensive safety evaluations

---

### Claude Sonnet 4.5 (September 2025)

**Key Capabilities:**
- **Hybrid Reasoning:** Extended thinking mode for complex problems
- Strong coding performance
- Enhanced tool use and function calling
- Improved reasoning benchmarks

**Safety Features:**
- **ASL-3 Classification**
- CBRN capability evaluations (pre-mitigation: ASL-2, post-mitigation: ASL-2)
- Cyber capability assessments
- Agentic safety evaluations
- Prompt injection resistance testing

**Notable Characteristics:**
- Balances capability with efficiency
- Extended thinking improves performance on hard reasoning tasks
- Strong performance on SWE-bench and agentic benchmarks

---

### Claude Opus 4.5 (November 2025)

**Key Capabilities:**
- **State-of-the-art frontier model**
- Highest capability in the Claude family
- Superior performance on complex reasoning and analysis
- Advanced coding and technical tasks
- Strong performance on graduate-level reasoning (GPQA)

**Safety Features:**
- **ASL-3 Classification**
- Comprehensive CBRN evaluations
- Enhanced cyber capability assessments
- Agentic safety testing (multi-turn, prompt injection)
- Autonomous replication and adaptation (ARA) testing
- Alignment and deception evaluations

**Notable Characteristics:**
- Most capable Claude model to date
- Designed for the most demanding reasoning and analysis tasks
- Extended context understanding and complex instruction following

---

## Key Research Papers

### A General Language Assistant as a Laboratory for Alignment (December 2021)

**Paper ID:** arXiv:2112.00861

**Key Contributions:**
- Introduced the **HHH criteria** (Helpful, Honest, Harmless) as alignment objectives
- Demonstrated that language models can serve as laboratories for alignment research
- Explored techniques including prompting, RLHF, and Preference Model Pre-training (PMP)
- Introduced context distillation as a training technique

**Technical Details:**
- Preference modeling to rank model outputs
- Context distillation: fine-tuning on outputs produced with helpful context
- Showed alignment techniques can improve both safety and capabilities

**[Source: Anthropic-A_General_Language_Assistant_as_a_Laboratory_for_Alignment_2112.00861.md](../PDF%20Extracts/AI%20Labs/Anthropic-A_General_Language_Assistant_as_a_Laboratory_for_Alignment_2112.00861.md)**

---

### Training a Helpful and Harmless Assistant with RLHF (April 2022)

**Paper ID:** arXiv:2204.05862

**Key Contributions:**
- Detailed methodology for **RLHF training** of language models
- Demonstrated tension between helpfulness and harmlessness
- Introduced techniques for balancing competing objectives
- Showed online training improves over static approaches

**Technical Details:**
- Preference model (PM) training from human comparisons
- Reinforcement learning using PPO with PM as reward
- Weekly retraining of preference models with fresh data
- Rejection sampling for data quality improvement

**Key Findings:**
- Larger models are easier to train for helpfulness and harmlessness
- RLHF training significantly reduces harmful outputs
- Trade-offs exist between being maximally helpful and avoiding all harm

**[Source: Anthropic-Training_a_Helpful_and_Harmless_Assistant_with_RLHF_2204.05862.md](../PDF%20Extracts/AI%20Labs/Anthropic-Training_a_Helpful_and_Harmless_Assistant_with_RLHF_2204.05862.md)**

---

### Constitutional AI: Harmlessness from AI Feedback (December 2022)

**Paper ID:** arXiv:2212.08073

**Key Contributions:**
- Introduced **Constitutional AI (CAI)** methodology
- Developed **RLAIF** (Reinforcement Learning from AI Feedback)
- Demonstrated training harmless AI without human labels for harmlessness
- Showed AI can critique and revise its own outputs

**Technical Details:**
- **Supervised Learning (SL) Stage:** Model generates responses, critiques them against principles, then revises
- **Reinforcement Learning (RL) Stage:** AI evaluates response pairs, feedback used for RLHF
- Constitution: set of principles guiding AI self-critique (e.g., from UN Declaration, Apple ToS)
- Chain-of-thought prompting improves AI feedback quality

**Key Findings:**
- CAI models are both more helpful AND more harmless than RLHF-only models
- RLAIF can replace human labeling for harmlessness
- Transparency: training principles can be made public
- Reduced human exposure to harmful content during training

**[Source: Anthropic-Constitutional_AI_Harmlessness_from_AI_Feedback_2212.08073.md](../PDF%20Extracts/AI%20Labs/Anthropic-Constitutional_AI_Harmlessness_from_AI_Feedback_2212.08073.md)**

---

## Safety Framework: AI Safety Levels (ASL)

Anthropic's Responsible Scaling Policy defines four AI Safety Levels:

| Level | Description | Requirements |
|-------|-------------|--------------|
| ASL-1 | Systems posing no meaningful catastrophic risk | Basic safety measures |
| ASL-2 | Systems where misuse could cause harm but not catastrophic | Standard safeguards, red teaming |
| ASL-3 | Systems substantially increasing risk of catastrophic misuse | Enhanced security, monitoring, deployment controls |
| ASL-4 | Systems requiring currently unknown safety techniques | Future research required |

**Current Status (as of November 2025):**
- Claude 2, 3.x, and 3.5.x models: ASL-2
- Claude 3.7 Sonnet and later: ASL-3 (first models requiring ASL-3 safeguards)

---

## Source Documents

All source PDF extracts are located in `/PDF Extracts/AI Labs/`:

### Model Documentation
- [Claude 2 Model Card](../PDF%20Extracts/AI%20Labs/Anthropic-Claude_2_Model_Card.md)
- [Claude 3 Model Card](../PDF%20Extracts/AI%20Labs/Anthropic-Claude_3_Model_Card.md)
- [Claude 3.5 Haiku Addendum](../PDF%20Extracts/AI%20Labs/Anthropic-Claude_3.5_Haiku_October_Addendum.md)
- [Claude 3.5 Sonnet Addendum](../PDF%20Extracts/AI%20Labs/Anthropic-Claude_3.5_Sonnet_Model_Card_Addendum.md)
- [Claude 3.7 Sonnet System Card](../PDF%20Extracts/AI%20Labs/Anthropic-Claude_3.7_Sonnet_System_Card.md)
- [Claude 4 Opus & Sonnet System Card](../PDF%20Extracts/AI%20Labs/Anthropic-Claude_4_Opus_Sonnet_System_Card.md)
- [Claude 4.5 Haiku System Card](../PDF%20Extracts/AI%20Labs/Anthropic-Claude_Haiku_4.5_System_Card.md)
- [Claude Sonnet 4.5 System Card](../PDF%20Extracts/AI%20Labs/Anthropic-Claude_Sonnet_4.5_System_Card.md)
- [Claude Opus 4.5 System Card](../PDF%20Extracts/AI%20Labs/Anthropic-Claude_Opus_4.5_System_Card.md)

### Research Papers
- [A General Language Assistant as a Laboratory for Alignment](../PDF%20Extracts/AI%20Labs/Anthropic-A_General_Language_Assistant_as_a_Laboratory_for_Alignment_2112.00861.md)
- [Training a Helpful and Harmless Assistant with RLHF](../PDF%20Extracts/AI%20Labs/Anthropic-Training_a_Helpful_and_Harmless_Assistant_with_RLHF_2204.05862.md)
- [Constitutional AI: Harmlessness from AI Feedback](../PDF%20Extracts/AI%20Labs/Anthropic-Constitutional_AI_Harmlessness_from_AI_Feedback_2212.08073.md)

---

*Last updated: January 2026*
