# WizardLM

## Overview
WizardLM is a family of instruction-following language models developed by Microsoft Research that use "Evol-Instruct" to progressively rewrite instructions into more complex forms, enabling smaller models to follow complex instructions effectively.

## Models
- **WizardLM:** Base instruction-following model
- **WizardCoder:** Specialized for code generation
- **WizardMath:** Specialized for mathematical reasoning

## Technical Approach
The Evol-Instruct method progressively rewrites initial instructions step-by-step into increasingly complex instructions, then uses all generated instruction data to fine-tune base models like LLaMA.

## Performance Highlights
- WizardLM outputs preferred over ChatGPT in human evaluations on high complexity tasks
- WizardLM achieves >90% of ChatGPT's capacity on 17 out of 29 skills (GPT-4 evaluation)
- WizardCoder surpasses Anthropic's Claude and Google's Bard on coding tasks
- WizardMath 70B outperforms GPT-3.5-Turbo, Claude 2, and Gemini Pro on mathematical reasoning

## Papers
| Paper | File | arXiv |
|-------|------|-------|
| WizardLM: Empowering Large Language Models to Follow Complex Instructions | [[WizardLM_Empowering_Complex_Instructions.pdf]] | [2304.12244](https://arxiv.org/abs/2304.12244) |
| WizardCoder: Empowering Code Large Language Models with Evol-Instruct | [[WizardCoder_Evol-Instruct.pdf]] | [2306.08568](https://arxiv.org/abs/2306.08568) |
| WizardMath: Empowering Mathematical Reasoning for LLMs via Reinforced Evol-Instruct | [[WizardMath_Reinforced_Evol-Instruct.pdf]] | [2308.09583](https://arxiv.org/abs/2308.09583) |

## Documentation & Links

### Official Resources
- [Microsoft Research: WizardLM](https://www.microsoft.com/en-us/research/publication/wizardlm-empowering-large-language-models-to-follow-complex-instructions/) - Official publication page
- [GitHub: WizardLM](https://github.com/nlpxucan/WizardLM) - Code and implementation

### Model Weights
- [HuggingFace: WizardLM](https://huggingface.co/WizardLM) - Model hub for all WizardLM variants

### Note
In 2025, the WizardLM team left Microsoft to join Tencent's Hunyuan AI development organization. Future development may occur under Tencent.
