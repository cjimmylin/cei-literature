# LLM Assessment & Data Availability Report

> **Generated:** 2026-02-16 | **Papers scanned:** 2002

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [LLM Model Landscape](#2-llm-model-landscape)
   - 2.1 Model Frequency Table
   - 2.2 Model Family Grouping
   - 2.3 Proprietary vs Open-Source Breakdown
   - 2.4 Models Per Paper Distribution
   - 2.5 Model Co-Occurrence Matrix
3. [Data Availability Analysis](#3-data-availability-analysis)
   - 3.1 URL Presence Statistics
   - 3.2 Hosting Platform Breakdown
   - 3.3 Overlap: LLM Models AND Data URLs
4. [Gap Analysis](#4-gap-analysis)
   - 4.1 Papers with LLM Models but No Public Data URL
   - 4.2 Papers with Data URLs but No LLM Models Identified
   - 4.3 Underrepresented Model Families
- [Appendix A: Model Family Normalization Table](#appendix-a-model-family-normalization-table)
- [Appendix B: Methodology Notes](#appendix-b-methodology-notes)

---

## 1. Executive Summary

This report analyzes **2002 papers** in the CEI Literature Vault for LLM model assessment
coverage and public data/benchmark availability.

| Metric | Count | % of Total |
|--------|------:|:----------:|
| Papers with LLM models identified | 1578 | 78.8% |
| Papers with no LLM models (NA) | 424 | 21.2% |
| Papers with public data URL | 1196 | 59.7% |
| Papers with no data URL (NA) | 806 | 40.3% |
| Papers with **both** models + URL | 1075 | 53.7% |
| Papers with **neither** | 303 | 15.1% |

- **1399 unique model names** across **14 model families** detected
- Average models per paper (among assessed papers): **6.1** (max: 53)

---

## 2. LLM Model Landscape

### 2.1 Model Frequency Table

All unique models ranked by number of papers mentioning them:

| Rank | Model | Papers | Family |
|-----:|-------|-------:|--------|
| 1 | GPT-4 | 682 | OpenAI |
| 2 | BERT | 497 | Pre-LLM / Encoder |
| 3 | Llama | 366 | Meta |
| 4 | Llama-3 | 346 | Meta |
| 5 | Qwen | 310 | Alibaba |
| 6 | ChatGPT | 305 | OpenAI |
| 7 | GPT-3.5 | 296 | OpenAI |
| 8 | Claude | 294 | Anthropic |
| 9 | GPT-4o | 270 | OpenAI |
| 10 | Mistral | 261 | Mistral AI |
| 11 | Gemma | 240 | Google |
| 12 | GPT-3 | 229 | OpenAI |
| 13 | Llama-2 | 218 | Meta |
| 14 | RoBERTa | 194 | Pre-LLM / Encoder |
| 15 | DeepSeek | 169 | DeepSeek |
| 16 | Gemini | 139 | Google |
| 17 | ALBERT | 85 | Pre-LLM / Encoder |
| 18 | Mistral-7B | 85 | Other/Unknown |
| 19 | Qwen2.5 | 85 | Other/Unknown |
| 20 | Llama-3.1 | 83 | Other/Unknown |
| 21 | Vicuna | 79 | Open-source (misc) |
| 22 | Mixtral | 74 | Mistral AI |
| 23 | GPT-2 | 70 | OpenAI |
| 24 | T5 | 66 | Google |
| 25 | Alpaca | 66 | Open-source (misc) |
| 26 | BLOOM | 60 | Open-source (misc) |
| 27 | Qwen2 | 59 | Other/Unknown |
| 28 | GPT-4o-mini | 54 | Other/Unknown |
| 29 | Gemma-2 | 53 | Google |
| 30 | Llama 3 | 48 | Other/Unknown |
| 31 | Llama 3.1 | 43 | Other/Unknown |
| 32 | Qwen3 | 42 | Other/Unknown |
| 33 | DeepSeek-V3 | 40 | Other/Unknown |
| 34 | DeepSeek-R1 | 39 | Other/Unknown |
| 35 | llama 3 | 35 | Other/Unknown |
| 36 | Qwen 2.5 | 35 | Other/Unknown |
| 37 | Llama3 | 34 | Other/Unknown |
| 38 | Mistral 7B | 34 | Other/Unknown |
| 39 | Phi | 33 | Microsoft |
| 40 | Word2Vec | 32 | Embeddings |
| 41 | GloVe | 32 | Embeddings |
| 42 | GPT-3.5-turbo | 32 | Other/Unknown |
| 43 | Gemma 2 | 32 | Other/Unknown |
| 44 | Qwen-2.5 | 32 | Other/Unknown |
| 45 | Llama2 | 31 | Other/Unknown |
| 46 | Grok | 30 | xAI |
| 47 | Falcon | 29 | Open-source (misc) |
| 48 | BLOOMZ | 28 | Other/Unknown |
| 49 | Llama 2 | 28 | Other/Unknown |
| 50 | GPT4 | 28 | Other/Unknown |
| 51 | Gemma2 | 27 | Other/Unknown |
| 52 | Claude 3.5 Sonnet | 26 | Other/Unknown |
| 53 | PaLM-2 | 25 | Google |
| 54 | GPT-3.5-Turbo | 25 | Other/Unknown |
| 55 | Llama-3.2 | 25 | Other/Unknown |
| 56 | BART | 24 | Pre-LLM / Encoder |
| 57 | DeBERTa | 24 | Pre-LLM / Encoder |
| 58 | InstructGPT | 24 | OpenAI |
| 59 | GPT-3.5 Turbo | 24 | Other/Unknown |
| 60 | Gemma-3 | 24 | Other/Unknown |
| 61 | PaLM | 22 | Google |
| 62 | Claude 3.5 | 22 | Other/Unknown |
| 63 | DistilBERT | 21 | Pre-LLM / Encoder |
| 64 | ELECTRA | 21 | Pre-LLM / Encoder |
| 65 | GPT-4o mini | 21 | OpenAI |
| 66 | LLaMA-3.1 | 21 | Other/Unknown |
| 67 | DeepSeek-AI | 21 | Other/Unknown |
| 68 | gpt-3.5-turbo | 20 | Other/Unknown |
| 69 | Llama3.1 | 20 | Other/Unknown |
| 70 | Claude-3.5-Sonnet | 19 | Other/Unknown |
| 71 | Llama-3.3 | 19 | Other/Unknown |
| 72 | Claude Sonnet | 18 | Other/Unknown |
| 73 | o3 | 18 | OpenAI |
| 74 | XLNet | 17 | Pre-LLM / Encoder |
| 75 | Qwen-7B | 17 | Other/Unknown |
| 76 | Bloom | 16 | Open-source (misc) |
| 77 | Llama 3.2 | 16 | Other/Unknown |
| 78 | XLM-RoBERTa | 15 | Other/Unknown |
| 79 | mBERT | 15 | Other/Unknown |
| 80 | Flan-T5 | 15 | Google |
| 81 | LLaMA2 | 15 | Other/Unknown |
| 82 | Qwen1.5 | 15 | Other/Unknown |
| 83 | Claude-3 | 15 | Anthropic |
| 84 | Mixtral-8x7B | 15 | Other/Unknown |
| 85 | o1 | 15 | OpenAI |
| 86 | GPT3 | 14 | Other/Unknown |
| 87 | GPT-4 Turbo | 14 | OpenAI |
| 88 | Baichuan2 | 14 | Other/Unknown |
| 89 | Llama Guard | 14 | Other/Unknown |
| 90 | Llama-3.1-8B | 14 | Other/Unknown |
| 91 | claude-3 | 13 | Anthropic |
| 92 | GPT-4-Turbo | 13 | Other/Unknown |
| 93 | Claude-3-Opus | 13 | Other/Unknown |
| 94 | Command-R | 13 | Cohere |
| 95 | Phi-3 | 13 | Microsoft |
| 96 | Llama 3.3 | 13 | Other/Unknown |
| 97 | gemma-2 | 13 | Google |
| 98 | ELMo | 12 | Pre-LLM / Encoder |
| 99 | GPT2 | 12 | Other/Unknown |
| 100 | OPT | 12 | Meta |
| 101 | LLaMA 3.1 | 12 | Other/Unknown |
| 102 | Mistral 7b | 12 | Other/Unknown |
| 103 | Qwen-14B | 12 | Other/Unknown |
| 104 | Dolly | 12 | Open-source (misc) |
| 105 | Llama-4 | 12 | Other/Unknown |
| 106 | Gemma 3 | 12 | Other/Unknown |
| 107 | word2vec | 11 | Embeddings |
| 108 | ChatGLM | 11 | Open-source (misc) |
| 109 | GPT 3 | 11 | Other/Unknown |
| 110 | Phi-4 | 11 | Other/Unknown |
| 111 | Qwen 2 | 11 | Other/Unknown |
| 112 | LlamaGuard | 11 | Other/Unknown |
| 113 | GPT4o | 11 | Other/Unknown |
| 114 | Claude-3.5 | 11 | Other/Unknown |
| 115 | Gemma3 | 11 | Other/Unknown |
| 116 | Llama-3.1-70B | 11 | Other/Unknown |
| 117 | LLaMA 3 | 11 | Other/Unknown |
| 118 | Mistral-Small | 11 | Other/Unknown |
| 119 | gpt-4o-mini | 10 | Other/Unknown |
| 120 | LLaMA3 | 10 | Other/Unknown |
| 121 | Llama-3-8B | 10 | Other/Unknown |
| 122 | Qwen-3 | 10 | Other/Unknown |
| 123 | DeepSeek V3 | 10 | Other/Unknown |
| 124 | Codex | 9 | OpenAI |
| 125 | text-davinci | 9 | OpenAI |
| 126 | Baichuan | 9 | Open-source (misc) |
| 127 | Mistral-Nemo | 9 | Other/Unknown |
| 128 | Barth | 9 | Other/Unknown |
| 129 | Claude 3.5 Haiku | 9 | Other/Unknown |
| 130 | PaLM 2 | 8 | Other/Unknown |
| 131 | GPT 3.5 | 8 | Other/Unknown |
| 132 | Claude. | 8 | Other/Unknown |
| 133 | llama3 | 8 | Other/Unknown |
| 134 | Qwen-1.5 | 8 | Alibaba |
| 135 | GPT 4 | 8 | Other/Unknown |
| 136 | InternLM | 8 | Open-source (misc) |
| 137 | GPT-4-turbo | 8 | Other/Unknown |
| 138 | Mistral-Large | 8 | Other/Unknown |
| 139 | Llama3.3 | 8 | Other/Unknown |
| 140 | Claude 3.7 Sonnet | 8 | Other/Unknown |
| 141 | Qwen2.5-72B | 8 | Other/Unknown |
| 142 | DeepSeek R1 | 8 | Other/Unknown |
| 143 | Qwen 3 | 8 | Other/Unknown |
| 144 | Palm | 7 | Google |
| 145 | llama. | 7 | Other/Unknown |
| 146 | LLaMA 2 | 7 | Other/Unknown |
| 147 | Claude-Sonnet | 7 | Other/Unknown |
| 148 | mistralai | 7 | Other/Unknown |
| 149 | LLaMA3.1 | 7 | Other/Unknown |
| 150 | Claude 3 | 7 | Other/Unknown |
| 151 | Claude-3.7-Sonnet | 7 | Other/Unknown |
| 152 | LaMDA | 6 | Google |
| 153 | Bartolo | 6 | Other/Unknown |
| 154 | CamemBERT | 6 | Other/Unknown |
| 155 | LLAMA2 | 6 | Other/Unknown |
| 156 | WizardLM | 6 | Open-source (misc) |
| 157 | GPT3.5 | 6 | Other/Unknown |
| 158 | Llama. | 6 | Other/Unknown |
| 159 | Claude-3-Sonnet | 6 | Other/Unknown |
| 160 | Claude-2 | 6 | Anthropic |
| 161 | Yi-34B | 6 | Other/Unknown |
| 162 | CommandR | 6 | Other/Unknown |
| 163 | Llama-3. | 6 | Other/Unknown |
| 164 | Claude 3 Opus | 6 | Other/Unknown |
| 165 | GPT 4o | 6 | Other/Unknown |
| 166 | MistralAI | 6 | Other/Unknown |
| 167 | LLaMA 3.2 | 6 | Other/Unknown |
| 168 | Llama3.2 | 6 | Other/Unknown |
| 169 | LLama-3.1 | 6 | Other/Unknown |
| 170 | Mistral Large | 6 | Other/Unknown |
| 171 | Llama 4 | 6 | Other/Unknown |
| 172 | Grok-3 | 6 | Other/Unknown |
| 173 | Glove | 5 | Embeddings |
| 174 | LLaMA. | 5 | Other/Unknown |
| 175 | ChatGLM-6B | 5 | Other/Unknown |
| 176 | CodeLlama | 5 | Meta |
| 177 | PaLM2 | 5 | Other/Unknown |
| 178 | Claude-3-Haiku | 5 | Other/Unknown |
| 179 | Qwen-72B | 5 | Other/Unknown |
| 180 | Bloom-1b7 | 5 | Other/Unknown |
| 181 | Mixtral-8x22B | 5 | Other/Unknown |
| 182 | Falcon 7B | 5 | Other/Unknown |
| 183 | Claude Opus | 5 | Other/Unknown |
| 184 | LLaMA-3.2 | 5 | Other/Unknown |
| 185 | mistral.ai | 5 | Other/Unknown |
| 186 | Mixtral 8x7B | 5 | Other/Unknown |
| 187 | qwenlm | 5 | Other/Unknown |
| 188 | Qwen-2.5-7B | 5 | Other/Unknown |
| 189 | InternLM2 | 5 | Other/Unknown |
| 190 | Mistral Small | 5 | Other/Unknown |
| 191 | Llama-3.3-70B | 5 | Other/Unknown |
| 192 | LLaMA 4 | 5 | Other/Unknown |
| 193 | Qwen-32B | 5 | Other/Unknown |
| 194 | gemma-3 | 5 | Other/Unknown |
| 195 | Llama-Guard | 5 | Other/Unknown |
| 196 | Qwen2.5-7B | 5 | Other/Unknown |
| 197 | T5-based | 4 | Other/Unknown |
| 198 | DeBERTa-v3 | 4 | Other/Unknown |
| 199 | Bart | 4 | Pre-LLM / Encoder |
| 200 | Claude 2 | 4 | Other/Unknown |
| 201 | Claude-2. | 4 | Other/Unknown |
| 202 | LLaMa-2 | 4 | Meta |
| 203 | ChatGLM2 | 4 | Other/Unknown |
| 204 | Bartl | 4 | Other/Unknown |
| 205 | T5-Large | 4 | Other/Unknown |
| 206 | Qwen-2 | 4 | Alibaba |
| 207 | Zephyr | 4 | Open-source (misc) |
| 208 | Gemini-Pro | 4 | Other/Unknown |
| 209 | Claude-3.5-sonnet | 4 | Other/Unknown |
| 210 | mistral-7b | 4 | Other/Unknown |
| 211 | Claude 3 Haiku | 4 | Other/Unknown |
| 212 | BloomZ | 4 | Other/Unknown |
| 213 | Llama3. | 4 | Other/Unknown |
| 214 | Phi-3-medium | 4 | Other/Unknown |
| 215 | Mixtral 8x22B | 4 | Other/Unknown |
| 216 | Gemma-1.1 | 4 | Other/Unknown |
| 217 | GPT 3.5 Turbo | 4 | Other/Unknown |
| 218 | Bloom-7b1 | 4 | Other/Unknown |
| 219 | ChatGLM3 | 4 | Other/Unknown |
| 220 | claude-sonnet | 4 | Other/Unknown |
| 221 | LLAMA-3.1 | 4 | Other/Unknown |
| 222 | llama3.1 | 4 | Other/Unknown |
| 223 | gemma | 4 | Google |
| 224 | Falcon3 | 4 | Other/Unknown |
| 225 | Gemini-1.5-Pro | 4 | Other/Unknown |
| 226 | LLaMA 3.3 | 4 | Other/Unknown |
| 227 | Gemini-2.0-Flash | 4 | Other/Unknown |
| 228 | GPT-4.1 | 4 | Other/Unknown |
| 229 | Mistral- 7B | 4 | Other/Unknown |
| 230 | LLAMA-3.2 | 4 | Other/Unknown |
| 231 | LLaMA 3. | 4 | Other/Unknown |
| 232 | GPT-5 | 4 | OpenAI |
| 233 | Grok 3 | 4 | Other/Unknown |
| 234 | Debertav3 | 3 | Other/Unknown |
| 235 | UmBERTo | 3 | Other/Unknown |
| 236 | XLM-R | 3 | Other/Unknown |
| 237 | Qwen-Max | 3 | Other/Unknown |
| 238 | AceGPT | 3 | Other/Unknown |
| 239 | Jais | 3 | Other/Unknown |
| 240 | phi-1 | 3 | Other/Unknown |
| 241 | Electra | 3 | Pre-LLM / Encoder |
| 242 | BLOOM-7B | 3 | Other/Unknown |
| 243 | Flan-T5-Large | 3 | Other/Unknown |
| 244 | T5-XXL | 3 | Other/Unknown |
| 245 | mGPT | 3 | Other/Unknown |
| 246 | XGLM | 3 | Other/Unknown |
| 247 | Bloom-7B | 3 | Other/Unknown |
| 248 | gpt-4-turbo | 3 | Other/Unknown |
| 249 | Yi-6B | 3 | Other/Unknown |
| 250 | Llama-2-7B | 3 | Other/Unknown |
| 251 | GPT-4-TURBO | 3 | Other/Unknown |
| 252 | Phi-3-mini | 3 | Other/Unknown |
| 253 | Llama 3.2. | 3 | Other/Unknown |
| 254 | CroissantLLM | 3 | Other/Unknown |
| 255 | Falcon-7B | 3 | Other/Unknown |
| 256 | Mistral-7b | 3 | Other/Unknown |
| 257 | Mistral-v0 | 3 | Other/Unknown |
| 258 | Claude-3-opus | 3 | Other/Unknown |
| 259 | llama2 | 3 | Other/Unknown |
| 260 | Qwen technical | 3 | Other/Unknown |
| 261 | Qwen 7B | 3 | Other/Unknown |
| 262 | alpaca | 3 | Open-source (misc) |
| 263 | Deberta | 3 | Pre-LLM / Encoder |
| 264 | Claude 3 Sonnet | 3 | Other/Unknown |
| 265 | Llama-3-70B | 3 | Other/Unknown |
| 266 | Llama2-Chat | 3 | Other/Unknown |
| 267 | llama-3. | 3 | Other/Unknown |
| 268 | LLaMA2. | 3 | Other/Unknown |
| 269 | Bloomz | 3 | Other/Unknown |
| 270 | Mixtral-8x7b | 3 | Other/Unknown |
| 271 | Qwen-Audio | 3 | Other/Unknown |
| 272 | Mistral-NeMo | 3 | Other/Unknown |
| 273 | command-r | 3 | Cohere |
| 274 | Qwen-VL | 3 | Other/Unknown |
| 275 | Claude-3.5-Haiku | 3 | Other/Unknown |
| 276 | Gemma-2-9B | 3 | Other/Unknown |
| 277 | LLAMA-3.3 | 3 | Other/Unknown |
| 278 | Claude-3.5 Sonnet | 3 | Other/Unknown |
| 279 | Aya-Expanse | 3 | Other/Unknown |
| 280 | LLaMA-4 | 3 | Other/Unknown |
| 281 | Llama-4-Maverick | 3 | Other/Unknown |
| 282 | Llama 2-Chat | 3 | Other/Unknown |
| 283 | Claude 3.7 | 3 | Other/Unknown |
| 284 | Grok-4 | 3 | Other/Unknown |
| 285 | LLaMA-3.3 | 3 | Other/Unknown |
| 286 | Grok 4 | 3 | Other/Unknown |
| 287 | Qwen2.5-VL-7B | 3 | Other/Unknown |
| 288 | Llama-4-Scout | 3 | Other/Unknown |
| 289 | Qwen2.5-14B | 3 | Other/Unknown |
| 290 | Qwen-1.5B | 3 | Other/Unknown |
| 291 | Barto | 2 | Other/Unknown |
| 292 | grok | 2 | xAI |
| 293 | FinBERT | 2 | Other/Unknown |
| 294 | FlauBERT | 2 | Other/Unknown |
| 295 | IndicBERT | 2 | Other/Unknown |
| 296 | MuRIL | 2 | Other/Unknown |
| 297 | AlBERTo | 2 | Other/Unknown |
| 298 | BERT-Italian | 2 | Other/Unknown |
| 299 | LLAMA 2 | 2 | Other/Unknown |
| 300 | LLaMA 1 | 2 | Other/Unknown |
| 301 | electra | 2 | Pre-LLM / Encoder |
| 302 | Llama2. | 2 | Other/Unknown |
| 303 | AlephBERT | 2 | Other/Unknown |
| 304 | GPT | 2 | Other/Unknown |
| 305 | Bloomberg | 2 | Other/Unknown |
| 306 | Baichuan-7B | 2 | Other/Unknown |
| 307 | Falcon-40B | 2 | Other/Unknown |
| 308 | Claude-2.1 | 2 | Other/Unknown |
| 309 | LLaMA-2-chat | 2 | Other/Unknown |
| 310 | NB-BERT | 2 | Other/Unknown |
| 311 | GPT-3.5 turbo | 2 | Other/Unknown |
| 312 | BLOOM-7 | 2 | Other/Unknown |
| 313 | OPT-66B | 2 | Other/Unknown |
| 314 | text-davinci-003 | 2 | OpenAI |
| 315 | BERTje | 2 | Other/Unknown |
| 316 | RobBERT | 2 | Other/Unknown |
| 317 | Baichuan-2 | 2 | Other/Unknown |
| 318 | InternLM-XComposer2 | 2 | Other/Unknown |
| 319 | GPT3.5-TURBO | 2 | Other/Unknown |
| 320 | baichuan-inc | 2 | Other/Unknown |
| 321 | LLama 2 | 2 | Other/Unknown |
| 322 | Taiwan-LLM-13B | 2 | Other/Unknown |
| 323 | Taiwan-LLM-7B | 2 | Other/Unknown |
| 324 | Llama-2-13B | 2 | Other/Unknown |
| 325 | Gemma-7B | 2 | Other/Unknown |
| 326 | CLAUDE-3 | 2 | Anthropic |
| 327 | bloom-1b1 | 2 | Other/Unknown |
| 328 | Phi-3 Mini | 2 | Other/Unknown |
| 329 | LLama3 | 2 | Other/Unknown |
| 330 | LLama3.1 | 2 | Other/Unknown |
| 331 | Aya | 2 | Cohere |
| 332 | deepseek r1 | 2 | Other/Unknown |
| 333 | GloVE | 2 | Embeddings |
| 334 | Command R+ | 2 | Cohere |
| 335 | DeBERTaV3 | 2 | Other/Unknown |
| 336 | claude-instant | 2 | Other/Unknown |
| 337 | LLaMA2-chat | 2 | Other/Unknown |
| 338 | Qwen-72b | 2 | Other/Unknown |
| 339 | claude 3 | 2 | Other/Unknown |
| 340 | LLaMA-3. | 2 | Other/Unknown |
| 341 | LLama 3 | 2 | Other/Unknown |
| 342 | Bartlett | 2 | Other/Unknown |
| 343 | Claude3.5 | 2 | Other/Unknown |
| 344 | Qwen 1 | 2 | Other/Unknown |
| 345 | Aya-101 | 2 | Other/Unknown |
| 346 | Mistral Nemo | 2 | Other/Unknown |
| 347 | T5-base | 2 | Other/Unknown |
| 348 | LLaMa3 | 2 | Other/Unknown |
| 349 | AYA | 2 | Cohere |
| 350 | GPT-4-Vision | 2 | Other/Unknown |
| 351 | Gpt4 | 2 | Other/Unknown |
| 352 | gpt-35-turbo | 2 | Other/Unknown |
| 353 | LLaVA | 2 | Other/Unknown |
| 354 | Llama-2. | 2 | Other/Unknown |
| 355 | HyperCLOVA X | 2 | Other/Unknown |
| 356 | MyanmarGPT | 2 | Other/Unknown |
| 357 | gpt2 | 2 | Other/Unknown |
| 358 | phi-1_5 | 2 | Other/Unknown |
| 359 | Mistral Medium | 2 | Other/Unknown |
| 360 | GPT-4o Mini | 2 | OpenAI |
| 361 | Command R | 2 | Other/Unknown |
| 362 | Phi 3 | 2 | Other/Unknown |
| 363 | Qwen-2-72B | 2 | Other/Unknown |
| 364 | Swallow-70B | 2 | Other/Unknown |
| 365 | Baichuan-13B | 2 | Other/Unknown |
| 366 | Claude-3 Opus | 2 | Anthropic |
| 367 | llama 2 | 2 | Other/Unknown |
| 368 | llama 2. | 2 | Other/Unknown |
| 369 | QWEN-72B | 2 | Other/Unknown |
| 370 | GPT4-Turbo | 2 | Other/Unknown |
| 371 | Mistral-AI | 2 | Other/Unknown |
| 372 | Qwen 1.5 | 2 | Other/Unknown |
| 373 | GPT 2 | 2 | Other/Unknown |
| 374 | Mistral 8B | 2 | Other/Unknown |
| 375 | Mistral v0 | 2 | Other/Unknown |
| 376 | DeepSeekMath | 2 | Other/Unknown |
| 377 | Mixtral 8 | 2 | Other/Unknown |
| 378 | Kandinsky 3.1 | 2 | Other/Unknown |
| 379 | DALL-E 3 | 2 | Other/Unknown |
| 380 | LLaMA-2-Chat | 2 | Other/Unknown |
| 381 | claude. | 2 | Other/Unknown |
| 382 | Qwen-Chat | 2 | Other/Unknown |
| 383 | Qwen-chat | 2 | Other/Unknown |
| 384 | BLOOMz | 2 | Other/Unknown |
| 385 | Llama-3.1-8B-Instruct | 2 | Other/Unknown |
| 386 | Qwen-2.5-7B-Instruct | 2 | Other/Unknown |
| 387 | bart-base | 2 | Other/Unknown |
| 388 | Claude-4 | 2 | Other/Unknown |
| 389 | Claude-4-Sonnet | 2 | Other/Unknown |
| 390 | LLaMa 3.1 | 2 | Other/Unknown |
| 391 | GPT 4o Mini | 2 | Other/Unknown |
| 392 | Qwen 1.5B | 2 | Other/Unknown |
| 393 | Mixtral 7B | 2 | Other/Unknown |
| 394 | ALLaM | 2 | Other/Unknown |
| 395 | Qwen-2.5-1.5B | 2 | Other/Unknown |
| 396 | DeepSeek v3 | 2 | Other/Unknown |
| 397 | Phi3 | 2 | Other/Unknown |
| 398 | GEMMA-2 | 2 | Google |
| 399 | QWEN2.5 | 2 | Other/Unknown |
| 400 | InternLM-2 | 2 | Other/Unknown |
| 401 | Qwen 72B | 2 | Other/Unknown |
| 402 | mixtral-8x22b | 2 | Other/Unknown |
| 403 | GEMMA | 2 | Google |
| 404 | LLAMA 3 | 2 | Other/Unknown |
| 405 | GLM-4 | 2 | Other/Unknown |
| 406 | GPT-4-mini | 2 | Other/Unknown |
| 407 | Yi-1.5 | 2 | Other/Unknown |
| 408 | Gemini-1.5-Flash | 2 | Other/Unknown |
| 409 | Llama-3.1-405B | 2 | Other/Unknown |
| 410 | Command-R-Plus | 2 | Other/Unknown |
| 411 | Claude 4. | 2 | Other/Unknown |
| 412 | Mistral-Medium | 2 | Other/Unknown |
| 413 | DeepSeek 1 | 2 | Other/Unknown |
| 414 | qwen-2.5 | 2 | Other/Unknown |
| 415 | DeepSeekCoder | 2 | Other/Unknown |
| 416 | T5-style | 2 | Other/Unknown |
| 417 | LLaMA3. | 2 | Other/Unknown |
| 418 | Grok-2 | 2 | Other/Unknown |
| 419 | phi-4 | 2 | Other/Unknown |
| 420 | DeepSeek-Chat | 2 | Other/Unknown |
| 421 | DeepSeek-v3 | 2 | Other/Unknown |
| 422 | Baichuan2-13B | 2 | Other/Unknown |
| 423 | Claude-Opus-4 | 2 | Other/Unknown |
| 424 | Gemini-2.5-Flash | 2 | Other/Unknown |
| 425 | GLM-4-Plus | 2 | Other/Unknown |
| 426 | Kimi-K2 | 2 | Other/Unknown |
| 427 | PALM | 2 | Google |
| 428 | Mistral Instruct | 2 | Other/Unknown |
| 429 | Gemini-2.5-Pro | 2 | Other/Unknown |
| 430 | Gemini 2.5 Pro | 2 | Other/Unknown |
| 431 | LLAMA-3. | 2 | Other/Unknown |
| 432 | QWEN3 | 2 | Other/Unknown |
| 433 | gemma3 | 2 | Other/Unknown |
| 434 | Claude 3.5-Sonnet | 2 | Other/Unknown |
| 435 | Phi-4-multimodal | 2 | Other/Unknown |
| 436 | Gemini 2.5 Flash | 2 | Other/Unknown |
| 437 | Qwen-2.5-72B | 2 | Other/Unknown |
| 438 | LLaMA Guard | 2 | Other/Unknown |
| 439 | Llama- Guard | 2 | Other/Unknown |
| 440 | dolly | 2 | Open-source (misc) |
| 441 | Baichuan 2 | 2 | Other/Unknown |
| 442 | DeepSeek Chat | 2 | Other/Unknown |
| 443 | Qwen2-VL-7B | 2 | Other/Unknown |
| 444 | Qwen2-VL-72B | 2 | Other/Unknown |
| 445 | Phi-3-Vision | 2 | Other/Unknown |
| 446 | Phi4 | 2 | Other/Unknown |
| 447 | Claude-Haiku | 2 | Other/Unknown |
| 448 | Llama4 | 2 | Other/Unknown |
| 449 | Mistral 3.1 | 2 | Other/Unknown |
| 450 | Deepseek-R1 | 2 | Other/Unknown |
| 451 | BLOOM-1 | 2 | Other/Unknown |
| 452 | Claude 4 | 2 | Other/Unknown |
| 453 | Falcon-7b | 2 | Other/Unknown |
| 454 | claude-4 | 2 | Other/Unknown |
| 455 | Qwen3-8B | 2 | Other/Unknown |
| 456 | DeepSeek-R1-Distill-Llama-8B | 2 | Other/Unknown |
| 457 | claude-3.5-sonnet | 2 | Other/Unknown |
| 458 | GPT4O | 2 | Other/Unknown |
| 459 | o4-mini | 2 | Other/Unknown |
| 460 | Qwen2.5-VL-72B | 2 | Other/Unknown |
| 461 | DeepSeek-Coder | 2 | DeepSeek |
| 462 | Qwen2.5-32B | 2 | Other/Unknown |
| 463 | BERTimbau | 2 | Other/Unknown |
| 464 | mistral-large | 2 | Other/Unknown |
| 465 | Claude-Opus | 2 | Other/Unknown |
| 466 | LLaMa-3.1 | 2 | Other/Unknown |
| 467 | Claude 3. | 2 | Other/Unknown |
| 468 | Gemini-2.0-Pro | 2 | Other/Unknown |
| 469 | gemma2 | 2 | Other/Unknown |
| 470 | multiple LLMs | 2 | Other/Unknown |
| 471 | GPT-OSS-20B | 2 | Other/Unknown |
| 472 | Claude-3.7 | 2 | Other/Unknown |
| 473 | Qwen-SEA | 2 | Other/Unknown |
| 474 | Claude Opus 4.5 | 2 | Other/Unknown |
| 475 | Claude Sonnet 4.5 | 2 | Other/Unknown |
| 476 | Phi-4-Mini | 2 | Other/Unknown |
| 477 | Qwen3Guard | 2 | Other/Unknown |
| 478 | Bloom P | 1 | Other/Unknown |
| 479 | BiLSTM | 1 | Other/Unknown |
| 480 | word2Vec | 1 | Embeddings |
| 481 | BART-based | 1 | Other/Unknown |
| 482 | gloVe | 1 | Embeddings |
| 483 | T5-11B | 1 | Other/Unknown |
| 484 | Word2vec | 1 | Embeddings |
| 485 | codex | 1 | OpenAI |
| 486 | elmo | 1 | Pre-LLM / Encoder |
| 487 | BioBERT | 1 | Other/Unknown |
| 488 | PubMedBERT | 1 | Other/Unknown |
| 489 | BARThez | 1 | Other/Unknown |
| 490 | PAGnol | 1 | Other/Unknown |
| 491 | GPT-J | 1 | Other/Unknown |
| 492 | GPT-NeoX | 1 | Other/Unknown |
| 493 | FrALBERT | 1 | Other/Unknown |
| 494 | XLM-T | 1 | Other/Unknown |
| 495 | BERTeus | 1 | Other/Unknown |
| 496 | mT5 | 1 | Other/Unknown |
| 497 | GilBERTo | 1 | Other/Unknown |
| 498 | LLaMA 1. | 1 | Other/Unknown |
| 499 | VICUNA | 1 | Open-source (misc) |
| 500 | DeBERTa re | 1 | Other/Unknown |
| 501 | DeBERTa-v3large | 1 | Other/Unknown |
| 502 | T5 and | 1 | Other/Unknown |
| 503 | T511B | 1 | Other/Unknown |
| 504 | Claude 1 | 1 | Other/Unknown |
| 505 | text-davinci-002 | 1 | OpenAI |
| 506 | AlephBERTGimel | 1 | Other/Unknown |
| 507 | ChatGLM-turbo | 1 | Other/Unknown |
| 508 | PoliBERT | 1 | Other/Unknown |
| 509 | bert-base-italian-xxl-uncased | 1 | Other/Unknown |
| 510 | CLIP ViT-B/32 | 1 | Other/Unknown |
| 511 | ViT-B/16 | 1 | Other/Unknown |
| 512 | Faster R-CNN ResNet-50-FPN | 1 | Other/Unknown |
| 513 | Mask R-CNN ResNet-50-FPN | 1 | Other/Unknown |
| 514 | CodeX | 1 | OpenAI |
| 515 | Taiwan-LLaMa | 1 | Other/Unknown |
| 516 | Model 7-C | 1 | Other/Unknown |
| 517 | Vigogne (LLaMa-based) | 1 | Other/Unknown |
| 518 | BLOOM perform | 1 | Other/Unknown |
| 519 | BloombergGPT | 1 | Other/Unknown |
| 520 | T5 LLM | 1 | Other/Unknown |
| 521 | phi-1 using | 1 | Other/Unknown |
| 522 | LlaMA2 | 1 | Other/Unknown |
| 523 | Bartels | 1 | Other/Unknown |
| 524 | LLaMA 36.4 | 1 | Other/Unknown |
| 525 | TAIWAN-LLM | 1 | Other/Unknown |
| 526 | ELMO | 1 | Pre-LLM / Encoder |
| 527 | deberta using | 1 | Other/Unknown |
| 528 | Falconer | 1 | Other/Unknown |
| 529 | DistilBert | 1 | Pre-LLM / Encoder |
| 530 | KB-BERT | 1 | Other/Unknown |
| 531 | DFM-encoder | 1 | Other/Unknown |
| 532 | RemBERT | 1 | Other/Unknown |
| 533 | mDeBERTaV3 | 1 | Other/Unknown |
| 534 | Scandinavian BERT variants | 1 | Other/Unknown |
| 535 | NorBERT3 | 1 | Other/Unknown |
| 536 | NorT5 | 1 | Other/Unknown |
| 537 | ScandiBERT | 1 | Other/Unknown |
| 538 | OPT-6 | 1 | Other/Unknown |
| 539 | FLAN-T5 | 1 | Google |
| 540 | DictaLM | 1 | Other/Unknown |
| 541 | CroSloEngual BERT | 1 | Other/Unknown |
| 542 | FLAN-T5-XXL | 1 | Other/Unknown |
| 543 | Flan-T5-Base | 1 | Other/Unknown |
| 544 | Flan-T5-Small | 1 | Other/Unknown |
| 545 | Flan-T5-XL | 1 | Other/Unknown |
| 546 | T5-Base | 1 | Other/Unknown |
| 547 | T5-Small | 1 | Other/Unknown |
| 548 | T5-XL | 1 | Other/Unknown |
| 549 | BLOOM 0 | 1 | Other/Unknown |
| 550 | BLOOM 3 | 1 | Other/Unknown |
| 551 | OPT 3 | 1 | Other/Unknown |
| 552 | LLaMA-2 | 1 | Meta |
| 553 | LLaMA-3 | 1 | Meta |
| 554 | Claude.ai | 1 | Other/Unknown |
| 555 | PALM-2 | 1 | Google |
| 556 | Llama8 | 1 | Other/Unknown |
| 557 | Llama8. | 1 | Other/Unknown |
| 558 | BanglaBERT | 1 | Other/Unknown |
| 559 | InternLM-XC2 | 1 | Other/Unknown |
| 560 | FALCON 40B | 1 | Other/Unknown |
| 561 | LLAMA 1 | 1 | Other/Unknown |
| 562 | LLAMA 1. | 1 | Other/Unknown |
| 563 | LLAMA-2-CHAT | 1 | Other/Unknown |
| 564 | Mixtral 8X7B | 1 | Other/Unknown |
| 565 | LLaMa | 1 | Meta |
| 566 | ChatGLM_Turbo | 1 | Other/Unknown |
| 567 | Bloom-560m | 1 | Other/Unknown |
| 568 | Gpt2 | 1 | Other/Unknown |
| 569 | OPT-125m | 1 | Other/Unknown |
| 570 | Claude-Instant | 1 | Other/Unknown |
| 571 | Qwen-0.5B | 1 | Other/Unknown |
| 572 | Breeze-7B | 1 | Other/Unknown |
| 573 | CLAUDE-3-OPUS | 1 | Other/Unknown |
| 574 | MIXTRAL-8X22B | 1 | Other/Unknown |
| 575 | Bloom 1 | 1 | Other/Unknown |
| 576 | Bloom-1b111 | 1 | Other/Unknown |
| 577 | bloom-1 | 1 | Other/Unknown |
| 578 | BLOOM-7B1 | 1 | Other/Unknown |
| 579 | GPT3.5-turbo | 1 | Other/Unknown |
| 580 | QWEN1.5 | 1 | Other/Unknown |
| 581 | Qwen.5 | 1 | Other/Unknown |
| 582 | Zephyr 7B | 1 | Other/Unknown |
| 583 | E5-multilingual | 1 | Other/Unknown |
| 584 | Sentence-T5 | 1 | Other/Unknown |
| 585 | LaBSE | 1 | Other/Unknown |
| 586 | multilingual-e5 | 1 | Other/Unknown |
| 587 | Scandinavian sentence encoders | 1 | Other/Unknown |
| 588 | Latxa (LLaMa-based) | 1 | Other/Unknown |
| 589 | Irati | 1 | Other/Unknown |
| 590 | Mistral7B | 1 | Other/Unknown |
| 591 | Mistral-NEMO | 1 | Other/Unknown |
| 592 | Phi-3 49 | 1 | Other/Unknown |
| 593 | InternLM CSMPT | 1 | Other/Unknown |
| 594 | Llama.1 | 1 | Other/Unknown |
| 595 | Mistral 2411 123B | 1 | Other/Unknown |
| 596 | Mistral 8x22B | 1 | Other/Unknown |
| 597 | Phi 3 Mini | 1 | Other/Unknown |
| 598 | llama3.1 chat | 1 | Other/Unknown |
| 599 | Command | 1 | Other/Unknown |
| 600 | and 32 additional LLMs (39 total) | 1 | Other/Unknown |
| 601 | BLOOM model | 1 | Other/Unknown |
| 602 | XVERSE-13B | 1 | Other/Unknown |
| 603 | XVERSE-7B | 1 | Other/Unknown |
| 604 | PersianMind | 1 | Other/Unknown |
| 605 | mT0XL | 1 | Other/Unknown |
| 606 | German BERT variants | 1 | Other/Unknown |
| 607 | LeoLM | 1 | Other/Unknown |
| 608 | gelectra-large | 1 | Other/Unknown |
| 609 | Bartolo59 | 1 | Other/Unknown |
| 610 | Palm 2 | 1 | Other/Unknown |
| 611 | palm | 1 | Google |
| 612 | GPT-4 Vision | 1 | Other/Unknown |
| 613 | Mixtral-8 | 1 | Other/Unknown |
| 614 | WizardLM L2Chat | 1 | Other/Unknown |
| 615 | Bard | 1 | Google |
| 616 | Gemini Pro | 1 | Google |
| 617 | and other Danish LLMs | 1 | Other/Unknown |
| 618 | Mistral Nemo25 | 1 | Other/Unknown |
| 619 | Qwen 2.526 | 1 | Other/Unknown |
| 620 | DeBERTa-Base | 1 | Other/Unknown |
| 621 | KcBERT | 1 | Other/Unknown |
| 622 | claude-2.0 | 1 | Other/Unknown |
| 623 | T5 ROUGE | 1 | Other/Unknown |
| 624 | T5 T6 | 1 | Other/Unknown |
| 625 | Claude-23 | 1 | Other/Unknown |
| 626 | NLLB | 1 | Other/Unknown |
| 627 | Indic-BART | 1 | Other/Unknown |
| 628 | Claude2 | 1 | Other/Unknown |
| 629 | Falcon40B | 1 | Other/Unknown |
| 630 | llama-2 chat | 1 | Other/Unknown |
| 631 | Claude-3-sonnet | 1 | Other/Unknown |
| 632 | Gemma7 | 1 | Other/Unknown |
| 633 | Mistral-based | 1 | Other/Unknown |
| 634 | MistralFT | 1 | Other/Unknown |
| 635 | LLaMA3.1-chat | 1 | Other/Unknown |
| 636 | Llama-2 chat | 1 | Other/Unknown |
| 637 | Mistral-nemo | 1 | Other/Unknown |
| 638 | Claude3.5-sonnet | 1 | Other/Unknown |
| 639 | Gemini1.5-pro | 1 | Other/Unknown |
| 640 | O3 | 1 | OpenAI |
| 641 | Bloom 3B | 1 | Other/Unknown |
| 642 | Bloom 7B | 1 | Other/Unknown |
| 643 | LlaMa2 | 1 | Other/Unknown |
| 644 | LlaMa3 | 1 | Other/Unknown |
| 645 | Qwen Llama2 | 1 | Other/Unknown |
| 646 | Qwen 13B | 1 | Other/Unknown |
| 647 | InternLM Team | 1 | Other/Unknown |
| 648 | InternLM-Chat | 1 | Other/Unknown |
| 649 | Qwen Qwen | 1 | Other/Unknown |
| 650 | Qwen Table | 1 | Other/Unknown |
| 651 | Yi 16 | 1 | Other/Unknown |
| 652 | mGPT-1.3B | 1 | Other/Unknown |
| 653 | BLOOM-1.7B | 1 | Other/Unknown |
| 654 | BLOOM-7.1B | 1 | Other/Unknown |
| 655 | Llama2-7B | 1 | Other/Unknown |
| 656 | Llama3-8B | 1 | Other/Unknown |
| 657 | Aya-23-8B | 1 | Other/Unknown |
| 658 | mT0 | 1 | Other/Unknown |
| 659 | NorGPT-369M | 1 | Other/Unknown |
| 660 | NorGPT-3B | 1 | Other/Unknown |
| 661 | NorGPT-23B | 1 | Other/Unknown |
| 662 | NorLlama-3B | 1 | Other/Unknown |
| 663 | NB-GPT-J-6B | 1 | Other/Unknown |
| 664 | MariTalk | 1 | Other/Unknown |
| 665 | Falcon 0 | 1 | Other/Unknown |
| 666 | Llama39 | 1 | Other/Unknown |
| 667 | Mistral 0.159 Llama3 | 1 | Other/Unknown |
| 668 | flan-t5-xl | 1 | Other/Unknown |
| 669 | t5-xl | 1 | Other/Unknown |
| 670 | BART-large | 1 | Other/Unknown |
| 671 | RoGPT-2 | 1 | Other/Unknown |
| 672 | YandexGPT-2 | 1 | Other/Unknown |
| 673 | YandexGPT-3 | 1 | Other/Unknown |
| 674 | GPT4-Vision | 1 | Other/Unknown |
| 675 | Llama2 chat | 1 | Other/Unknown |
| 676 | Mistral-v1 | 1 | Other/Unknown |
| 677 | Lamda | 1 | Google |
| 678 | InternVL | 1 | Other/Unknown |
| 679 | LLaMa 2 | 1 | Other/Unknown |
| 680 | Mistral-0.2-Instruct | 1 | Other/Unknown |
| 681 | Distilbert | 1 | Pre-LLM / Encoder |
| 682 | Llama-2-Chat | 1 | Other/Unknown |
| 683 | Mixtral-8X7B | 1 | Other/Unknown |
| 684 | Phi-1 | 1 | Other/Unknown |
| 685 | Pegasus | 1 | Other/Unknown |
| 686 | LLäMmlein-120M | 1 | Other/Unknown |
| 687 | LLäMmlein-1B | 1 | Other/Unknown |
| 688 | bert-base-german-cased | 1 | Other/Unknown |
| 689 | 10 German-pretrained models | 1 | Other/Unknown |
| 690 | phi-2 | 1 | Microsoft |
| 691 | Mistral large | 1 | Other/Unknown |
| 692 | Qwen-1.5-72B | 1 | Other/Unknown |
| 693 | DeepSeek-67B | 1 | Other/Unknown |
| 694 | Aquila-2-34B | 1 | Other/Unknown |
| 695 | Qwen-1.5-32B-Chat | 1 | Other/Unknown |
| 696 | Mistral-7B-Instruct-v0.2 | 1 | Other/Unknown |
| 697 | Gemma-1.1-7B-it | 1 | Other/Unknown |
| 698 | Llama-3-8B-Instruct | 1 | Other/Unknown |
| 699 | distilbert | 1 | Pre-LLM / Encoder |
| 700 | MistralOrca | 1 | Other/Unknown |
| 701 | Juhaina-9.24B | 1 | Other/Unknown |
| 702 | Silma-9B | 1 | Other/Unknown |
| 703 | Gemma-2-SimPO-9B | 1 | Other/Unknown |
| 704 | SauerkrautLM-Gemma-9B | 1 | Other/Unknown |
| 705 | Gemma-2-SPPO-9B | 1 | Other/Unknown |
| 706 | and other multilingual LLMs | 1 | Other/Unknown |
| 707 | CyberAgentLM2-7B | 1 | Other/Unknown |
| 708 | Swallow-7B | 1 | Other/Unknown |
| 709 | Swallow-13B | 1 | Other/Unknown |
| 710 | Sarashina2-7B | 1 | Other/Unknown |
| 711 | Sarashina2-13B | 1 | Other/Unknown |
| 712 | Phi-3-small | 1 | Other/Unknown |
| 713 | GreekLegalRoBERTa | 1 | Other/Unknown |
| 714 | GreekLegalBERT | 1 | Other/Unknown |
| 715 | GreekLegalBERT-v2 | 1 | Other/Unknown |
| 716 | GreekBERT | 1 | Other/Unknown |
| 717 | Gemini Ultra | 1 | Google |
| 718 | Alpaca2 | 1 | Other/Unknown |
| 719 | Claude-3 Haiku | 1 | Anthropic |
| 720 | Claude-3 Sonnet | 1 | Anthropic |
| 721 | GPT 4-Turbo | 1 | Other/Unknown |
| 722 | LLama-3.2 | 1 | Other/Unknown |
| 723 | Llama-2-70B | 1 | Other/Unknown |
| 724 | Mistral AI | 1 | Other/Unknown |
| 725 | Dolly-200 | 1 | Other/Unknown |
| 726 | GPT-3.5 TURBO | 1 | Other/Unknown |
| 727 | GPT-3.5-TURBO | 1 | Other/Unknown |
| 728 | QWEN-14B | 1 | Other/Unknown |
| 729 | QWEN-7B | 1 | Other/Unknown |
| 730 | Claude models | 1 | Other/Unknown |
| 731 | various LLM-as-a-Judge and reward models | 1 | Other/Unknown |
| 732 | Mixtral-8x22bB | 1 | Other/Unknown |
| 733 | ChatGLM 2 | 1 | Other/Unknown |
| 734 | Chatglm2 | 1 | Other/Unknown |
| 735 | Vicuna 1.5 | 1 | Other/Unknown |
| 736 | Flan-PaLM | 1 | Other/Unknown |
| 737 | gpt-4vision | 1 | Other/Unknown |
| 738 | GPT3.5 turbo | 1 | Other/Unknown |
| 739 | Yi-34B-Chat | 1 | Other/Unknown |
| 740 | Qwen-1.5-14B-Chat | 1 | Other/Unknown |
| 741 | Claude-1.3 | 1 | Other/Unknown |
| 742 | Yi-9B | 1 | Other/Unknown |
| 743 | Qwen-1.8B | 1 | Other/Unknown |
| 744 | Breeze-7B-Instruct-v1.0 | 1 | Other/Unknown |
| 745 | ChatGLM3-6B | 1 | Other/Unknown |
| 746 | gemma 6.51 | 1 | Other/Unknown |
| 747 | internlm | 1 | Open-source (misc) |
| 748 | internlm2 | 1 | Other/Unknown |
| 749 | Qwen-based | 1 | Other/Unknown |
| 750 | llama-31 | 1 | Other/Unknown |
| 751 | qwen2vl | 1 | Other/Unknown |
| 752 | Barth4 | 1 | Other/Unknown |
| 753 | Vicuna-13 | 1 | Other/Unknown |
| 754 | Kandinsky 2.2 | 1 | Other/Unknown |
| 755 | Midjourney | 1 | Other/Unknown |
| 756 | Stable Diffusion XL | 1 | Other/Unknown |
| 757 | YandexART | 1 | Other/Unknown |
| 758 | Meltemi-7B | 1 | Other/Unknown |
| 759 | LlaMA3 | 1 | Other/Unknown |
| 760 | Phi-2 | 1 | Microsoft |
| 761 | Claude-3. | 1 | Other/Unknown |
| 762 | PaLM-22 | 1 | Other/Unknown |
| 763 | Vicuna4 | 1 | Other/Unknown |
| 764 | GPT3.5-Turbo | 1 | Other/Unknown |
| 765 | bloom | 1 | Open-source (misc) |
| 766 | Qwen-Chat9 | 1 | Other/Unknown |
| 767 | Qwen-max | 1 | Other/Unknown |
| 768 | Mistral-v2 | 1 | Other/Unknown |
| 769 | Mistral-v3 | 1 | Other/Unknown |
| 770 | Llama 0.4852 | 1 | Other/Unknown |
| 771 | LlaMa-3.1 | 1 | Other/Unknown |
| 772 | LlaMa-Guard | 1 | Other/Unknown |
| 773 | LLaMA1 | 1 | Other/Unknown |
| 774 | Mistral. 6 | 1 | Other/Unknown |
| 775 | Zephyr-7B | 1 | Other/Unknown |
| 776 | Command-R+ | 1 | Other/Unknown |
| 777 | SOLAR | 1 | Other/Unknown |
| 778 | Polyglot-ko | 1 | Other/Unknown |
| 779 | Qwen-14b | 1 | Other/Unknown |
| 780 | ChatGLM series | 1 | Other/Unknown |
| 781 | Qwen and | 1 | Other/Unknown |
| 782 | Qwen se | 1 | Other/Unknown |
| 783 | Qwen series | 1 | Other/Unknown |
| 784 | Qwen-110B | 1 | Other/Unknown |
| 785 | DeepseekV2 | 1 | Other/Unknown |
| 786 | llama-3.1 | 1 | Other/Unknown |
| 787 | SnakModel (Llama2-7B-based) | 1 | Other/Unknown |
| 788 | other Llama2-7B-based Danish models | 1 | Other/Unknown |
| 789 | LLAMA3.1 | 1 | Other/Unknown |
| 790 | EthioLLM-small | 1 | Other/Unknown |
| 791 | EthioLLM-base | 1 | Other/Unknown |
| 792 | EthioLLM-large | 1 | Other/Unknown |
| 793 | AfroXLMR | 1 | Other/Unknown |
| 794 | AfroLM | 1 | Other/Unknown |
| 795 | EthioMT5 | 1 | Other/Unknown |
| 796 | DOLLY | 1 | Open-source (misc) |
| 797 | MIXTRAL-8X7B | 1 | Other/Unknown |
| 798 | MahaMarathi-7B | 1 | Other/Unknown |
| 799 | internlm-chat | 1 | Other/Unknown |
| 800 | AraBERT | 1 | Other/Unknown |
| 801 | YandexGPT | 1 | Other/Unknown |
| 802 | GigaChat | 1 | Other/Unknown |
| 803 | T5-model | 1 | Other/Unknown |
| 804 | Bloom 1B | 1 | Other/Unknown |
| 805 | Bloom-7B1 | 1 | Other/Unknown |
| 806 | QWEN-2.5 | 1 | Other/Unknown |
| 807 | Qwen_1_5B_instruct | 1 | Other/Unknown |
| 808 | Qwen_500M_instruct | 1 | Other/Unknown |
| 809 | Qwen_7B_instruct | 1 | Other/Unknown |
| 810 | Sabia-3 | 1 | Other/Unknown |
| 811 | Sabiazinho-3 | 1 | Other/Unknown |
| 812 | Qwen-2.5-3B | 1 | Other/Unknown |
| 813 | Qwen-2.5-14B | 1 | Other/Unknown |
| 814 | Llama-1-7B | 1 | Other/Unknown |
| 815 | Sabia-7B | 1 | Other/Unknown |
| 816 | Tucano-1B | 1 | Other/Unknown |
| 817 | Tucano-2B | 1 | Other/Unknown |
| 818 | Tucano-7B | 1 | Other/Unknown |
| 819 | TinyLlama-1.1B | 1 | Other/Unknown |
| 820 | Curio-7B | 1 | Other/Unknown |
| 821 | SILMA-9B-Instruct | 1 | Other/Unknown |
| 822 | Deepseek 0 | 1 | Other/Unknown |
| 823 | Deepseek 79 | 1 | Other/Unknown |
| 824 | LLama 3.3 | 1 | Other/Unknown |
| 825 | Llama 0.072 | 1 | Other/Unknown |
| 826 | Llama 64.5 | 1 | Other/Unknown |
| 827 | T5TokenizerFast | 1 | Other/Unknown |
| 828 | Flan-T5-based | 1 | Other/Unknown |
| 829 | GPT4o-mini | 1 | Other/Unknown |
| 830 | opt125M_portuguese | 1 | Other/Unknown |
| 831 | Gemma-2-27B | 1 | Other/Unknown |
| 832 | Claude 312 | 1 | Other/Unknown |
| 833 | LLaMA 3.116 | 1 | Other/Unknown |
| 834 | Qwen-14B14 | 1 | Other/Unknown |
| 835 | claude-3-haiku | 1 | Other/Unknown |
| 836 | Llama2Chat | 1 | Other/Unknown |
| 837 | Llama3-Chat | 1 | Other/Unknown |
| 838 | EuroLLM | 1 | Other/Unknown |
| 839 | Teuken-7B | 1 | Other/Unknown |
| 840 | Salamandra | 1 | Other/Unknown |
| 841 | transformer-based models | 1 | Other/Unknown |
| 842 | BLOOMZ-7B | 1 | Other/Unknown |
| 843 | Lucie | 1 | Other/Unknown |
| 844 | Llama-3.1. | 1 | Other/Unknown |
| 845 | GEMMA 2 | 1 | Other/Unknown |
| 846 | GPT-4o-Mini | 1 | Other/Unknown |
| 847 | LlamA-3.2 | 1 | Other/Unknown |
| 848 | Llama-3-Taiwan | 1 | Other/Unknown |
| 849 | Meta-Llama-3 | 1 | Other/Unknown |
| 850 | Vicuna-1.5 | 1 | Other/Unknown |
| 851 | Mistral-3-24B | 1 | Other/Unknown |
| 852 | Claude1 | 1 | Other/Unknown |
| 853 | BLOOM-560 | 1 | Other/Unknown |
| 854 | DistilCamemBERT | 1 | Other/Unknown |
| 855 | DeHateBERT | 1 | Other/Unknown |
| 856 | Text-Davinci-003 | 1 | OpenAI |
| 857 | Vicuna-80 | 1 | Other/Unknown |
| 858 | GEMINI-Flash | 1 | Other/Unknown |
| 859 | LLaMA 50.0 | 1 | Other/Unknown |
| 860 | LLaMA 50.1 | 1 | Other/Unknown |
| 861 | LLaMA 67.2 | 1 | Other/Unknown |
| 862 | QwenScorer | 1 | Other/Unknown |
| 863 | Gemini 1.5 Flash | 1 | Other/Unknown |
| 864 | Gemini 1.5 Pro | 1 | Other/Unknown |
| 865 | SenseChat | 1 | Other/Unknown |
| 866 | Aya-23 | 1 | Other/Unknown |
| 867 | LLaMA3.2 | 1 | Other/Unknown |
| 868 | Llama-3.7 | 1 | Other/Unknown |
| 869 | LLama-4 | 1 | Other/Unknown |
| 870 | LLaMA 8 | 1 | Other/Unknown |
| 871 | claude-4. | 1 | Other/Unknown |
| 872 | baichuan-ai | 1 | Other/Unknown |
| 873 | InternLM-7B | 1 | Other/Unknown |
| 874 | LLAMA-2-Chat | 1 | Other/Unknown |
| 875 | Qwen3-4B | 1 | Other/Unknown |
| 876 | Gemini-2.5 | 1 | Other/Unknown |
| 877 | T5-like | 1 | Other/Unknown |
| 878 | llama-3.3 | 1 | Other/Unknown |
| 879 | llama3.2 | 1 | Other/Unknown |
| 880 | qwen2.5 | 1 | Other/Unknown |
| 881 | GPT-OSS-120B | 1 | Other/Unknown |
| 882 | Sailor2 | 1 | Other/Unknown |
| 883 | SeaLLM-v3 | 1 | Other/Unknown |
| 884 | Gemma-9B | 1 | Other/Unknown |
| 885 | Dicta-LM-2.0 | 1 | Other/Unknown |
| 886 | LongHero | 1 | Other/Unknown |
| 887 | T5 17 | 1 | Other/Unknown |
| 888 | Bartz | 1 | Other/Unknown |
| 889 | LLaMA-4. | 1 | Other/Unknown |
| 890 | MISTRAL LARGE | 1 | Other/Unknown |
| 891 | Gemma-2B | 1 | Other/Unknown |
| 892 | Gemma-4B | 1 | Other/Unknown |
| 893 | MISTRAL-X | 1 | Other/Unknown |
| 894 | BERTu | 1 | Other/Unknown |
| 895 | mBERTu | 1 | Other/Unknown |
| 896 | Phi-4 56 | 1 | Other/Unknown |
| 897 | gemini-1.5-flash | 1 | Other/Unknown |
| 898 | T5-large | 1 | Other/Unknown |
| 899 | Falcon 3 | 1 | Other/Unknown |
| 900 | Llama 1 | 1 | Other/Unknown |
| 901 | Qwen 1.8B | 1 | Other/Unknown |
| 902 | Deepseek Reasoner | 1 | Other/Unknown |
| 903 | DeepseekR | 1 | Other/Unknown |
| 904 | DeepseekRa | 1 | Other/Unknown |
| 905 | DeepseekRi | 1 | Other/Unknown |
| 906 | DeepseekRin_grok2a_blindi | 1 | Other/Unknown |
| 907 | DeepseekRin_o3 | 1 | Other/Unknown |
| 908 | DeepseekRn_mistrala_blindi | 1 | Other/Unknown |
| 909 | DeepseekRn_o3 | 1 | Other/Unknown |
| 910 | Grok 2 | 1 | Other/Unknown |
| 911 | Grok2 | 1 | Other/Unknown |
| 912 | Mistral 0.80 0 | 1 | Other/Unknown |
| 913 | Mistrala | 1 | Other/Unknown |
| 914 | Mistrali | 1 | Other/Unknown |
| 915 | mistraln_DeepseekRa_LLMi | 1 | Other/Unknown |
| 916 | mistraln_DeepseekRa_blindi | 1 | Other/Unknown |
| 917 | mistraln_DeepseekRa_person | 1 | Other/Unknown |
| 918 | mistraln_DeepseekRa_personi | 1 | Other/Unknown |
| 919 | mistraln_grok2a_blindi | 1 | Other/Unknown |
| 920 | mistraln_mistrala_DeepseekRi | 1 | Other/Unknown |
| 921 | mistraln_mistrala_blindi | 1 | Other/Unknown |
| 922 | mistraln_mistrala_grok2i | 1 | Other/Unknown |
| 923 | mistraln_mistrala_mistrali | 1 | Other/Unknown |
| 924 | mistraln_mistrala_o3 | 1 | Other/Unknown |
| 925 | Mistral 44.5 58 | 1 | Other/Unknown |
| 926 | Mistral-Saba | 1 | Other/Unknown |
| 927 | Claude3-Opus | 1 | Other/Unknown |
| 928 | Claude3-Sonnet | 1 | Other/Unknown |
| 929 | LLaMA2Chat | 1 | Other/Unknown |
| 930 | Yi-Large | 1 | Other/Unknown |
| 931 | Minimax-01 | 1 | Other/Unknown |
| 932 | HKGAI-V1 | 1 | Other/Unknown |
| 933 | DeepSeek-V2-Lite | 1 | Other/Unknown |
| 934 | Ernie-4.5 | 1 | Other/Unknown |
| 935 | Kimi-1.5 | 1 | Other/Unknown |
| 936 | Qwen3-235B | 1 | Other/Unknown |
| 937 | Falcon-H1 | 1 | Other/Unknown |
| 938 | Mistral 31.65 80 | 1 | Other/Unknown |
| 939 | Mistral 368.0 5 | 1 | Other/Unknown |
| 940 | Phi-2 33 | 1 | Other/Unknown |
| 941 | Phi-4 14B | 1 | Other/Unknown |
| 942 | Command-r | 1 | Cohere |
| 943 | Claude-3.5-haiku | 1 | Other/Unknown |
| 944 | Llama 2 chat | 1 | Other/Unknown |
| 945 | Mistral- Large | 1 | Other/Unknown |
| 946 | phi-1 1 | 1 | Other/Unknown |
| 947 | T5 Base | 1 | Other/Unknown |
| 948 | T5-styled | 1 | Other/Unknown |
| 949 | Claude-3-haiku | 1 | Other/Unknown |
| 950 | DEEPSEEK-V3 | 1 | Other/Unknown |
| 951 | GROK 4 | 1 | Other/Unknown |
| 952 | QWEN-PLUS | 1 | Other/Unknown |
| 953 | grok-4 | 1 | Other/Unknown |
| 954 | DeepSeekV3 | 1 | Other/Unknown |
| 955 | Claude-haiku | 1 | Other/Unknown |
| 956 | Mistral L2 | 1 | Other/Unknown |
| 957 | BART 0 | 1 | Other/Unknown |
| 958 | DeBERTa 0 | 1 | Other/Unknown |
| 959 | T5 0 | 1 | Other/Unknown |
| 960 | Mistral- large | 1 | Other/Unknown |
| 961 | Lt-Llama-2 | 1 | Other/Unknown |
| 962 | Claude 131 | 1 | Other/Unknown |
| 963 | GPT 4 Turbo | 1 | Other/Unknown |
| 964 | Llama 3. | 1 | Other/Unknown |
| 965 | Bllossom-8B | 1 | Other/Unknown |
| 966 | Qwen-1.5-7B | 1 | Other/Unknown |
| 967 | Rakuten-7B | 1 | Other/Unknown |
| 968 | HyperCLOVA-X | 1 | Other/Unknown |
| 969 | EXAONE-3.0-7.8B | 1 | Other/Unknown |
| 970 | KULLM-v3 | 1 | Other/Unknown |
| 971 | Bloomsbury | 1 | Other/Unknown |
| 972 | Qwen-1.5-14B | 1 | Other/Unknown |
| 973 | Solar-10.7B | 1 | Other/Unknown |
| 974 | T3Q-ko-solar | 1 | Other/Unknown |
| 975 | EuroLLM-9B | 1 | Other/Unknown |
| 976 | Mistral-Nemo-12B | 1 | Other/Unknown |
| 977 | Sherkala-Chat-8B | 1 | Other/Unknown |
| 978 | Grok3 | 1 | Other/Unknown |
| 979 | LLaMA3.3 | 1 | Other/Unknown |
| 980 | LLamaGuard | 1 | Other/Unknown |
| 981 | gpt4 | 1 | Other/Unknown |
| 982 | BLOOM 251 | 1 | Other/Unknown |
| 983 | BLOOM 35 | 1 | Other/Unknown |
| 984 | BLOOM 48 | 1 | Other/Unknown |
| 985 | BLOOM 83 | 1 | Other/Unknown |
| 986 | LLaMA 23.26 | 1 | Other/Unknown |
| 987 | LLaMA 32 | 1 | Other/Unknown |
| 988 | LLaMA 38.10 | 1 | Other/Unknown |
| 989 | LLaMA 45.65 | 1 | Other/Unknown |
| 990 | LLaMA 5.38 | 1 | Other/Unknown |
| 991 | LLaMA 50.00 | 1 | Other/Unknown |
| 992 | LLaMA 6.26 | 1 | Other/Unknown |
| 993 | LLaMA 7.09 | 1 | Other/Unknown |
| 994 | LLaMA 76.6 | 1 | Other/Unknown |
| 995 | T5-LM | 1 | Other/Unknown |
| 996 | bloom-7b1 | 1 | Other/Unknown |
| 997 | Claude 3.74 | 1 | Other/Unknown |
| 998 | Falcon 23 | 1 | Other/Unknown |
| 999 | Falcon 24 | 1 | Other/Unknown |
| 1000 | Falcon 27 | 1 | Other/Unknown |
| 1001 | Falcon-3 | 1 | Other/Unknown |
| 1002 | Gemma 24.87 | 1 | Other/Unknown |
| 1003 | Gemma 29.26 | 1 | Other/Unknown |
| 1004 | Gemma 41.94 | 1 | Other/Unknown |
| 1005 | Qwen 26.63 | 1 | Other/Unknown |
| 1006 | Qwen 39.64 | 1 | Other/Unknown |
| 1007 | Qwen 40.58 | 1 | Other/Unknown |
| 1008 | Internlm2 | 1 | Other/Unknown |
| 1009 | LLaMA-31 | 1 | Other/Unknown |
| 1010 | internlm25 | 1 | Other/Unknown |
| 1011 | DeepSeek Reasoner | 1 | Other/Unknown |
| 1012 | Phi-4 and | 1 | Other/Unknown |
| 1013 | o1-preview | 1 | OpenAI |
| 1014 | LLama-Guard | 1 | Other/Unknown |
| 1015 | Ernie-Bot-4 | 1 | Other/Unknown |
| 1016 | Claude 1.00 | 1 | Other/Unknown |
| 1017 | Claude 11.5 | 1 | Other/Unknown |
| 1018 | Claude 42.7 | 1 | Other/Unknown |
| 1019 | DeepSeek 0 | 1 | Other/Unknown |
| 1020 | Grok 0 | 1 | Other/Unknown |
| 1021 | Qwen 28.6 | 1 | Other/Unknown |
| 1022 | Qwen 37.1 | 1 | Other/Unknown |
| 1023 | WizardLM 0 | 1 | Other/Unknown |
| 1024 | bloomz | 1 | Other/Unknown |
| 1025 | GLM-4-Air | 1 | Other/Unknown |
| 1026 | Doubao-1.5-Pro | 1 | Other/Unknown |
| 1027 | Qwen 0.60 | 1 | Other/Unknown |
| 1028 | Llama-3.2-3B | 1 | Other/Unknown |
| 1029 | Llama-3.2-1B | 1 | Other/Unknown |
| 1030 | Mistral-v0.3-7B | 1 | Other/Unknown |
| 1031 | Qwen-2.5-0.5B | 1 | Other/Unknown |
| 1032 | LLaVA-1.5-7B | 1 | Other/Unknown |
| 1033 | LLaVA-1.5-13B | 1 | Other/Unknown |
| 1034 | LLaVA-Next-7B | 1 | Other/Unknown |
| 1035 | LLaVA-OneVision-0.5B | 1 | Other/Unknown |
| 1036 | LLaVA-OneVision-7B | 1 | Other/Unknown |
| 1037 | InternVL2-2B | 1 | Other/Unknown |
| 1038 | InternVL2-8B | 1 | Other/Unknown |
| 1039 | Llama-3.2-11B | 1 | Other/Unknown |
| 1040 | Qwen25 | 1 | Other/Unknown |
| 1041 | Qwen-7B5 | 1 | Other/Unknown |
| 1042 | Qwen-Plus | 1 | Other/Unknown |
| 1043 | Mistral among | 1 | Other/Unknown |
| 1044 | Mistral- 7b | 1 | Other/Unknown |
| 1045 | Taiwan-LLM | 1 | Other/Unknown |
| 1046 | Llama-3.2-1B-Instruct | 1 | Other/Unknown |
| 1047 | Claude 4.5 | 1 | Other/Unknown |
| 1048 | Claude- Haiku | 1 | Other/Unknown |
| 1049 | Claude-4.5 | 1 | Other/Unknown |
| 1050 | Claude-4.5. | 1 | Other/Unknown |
| 1051 | DeepSeek-3 | 1 | Other/Unknown |
| 1052 | Grok4 | 1 | Other/Unknown |
| 1053 | Mistral3.1-24B | 1 | Other/Unknown |
| 1054 | Mistral- 3 | 1 | Other/Unknown |
| 1055 | Mistral-24B | 1 | Other/Unknown |
| 1056 | Mistral-3.1-24B | 1 | Other/Unknown |
| 1057 | Phi3-medium | 1 | Other/Unknown |
| 1058 | gpt3 | 1 | Other/Unknown |
| 1059 | GPT-3.5; GPT-4; Llama-2 | 1 | Other/Unknown |
| 1060 | Mistral small | 1 | Other/Unknown |
| 1061 | Mistral. 2025 | 1 | Other/Unknown |
| 1062 | Qwen-2.5-3B; Jais-adapted-7B; ALLaM-7B; Llama-3.1-8B; Aya-Expanse-8B; AceGPT-v2-8B; AceGPT-v1.5-13B; Jais-13B; Jais-adapted-13B; Jais-family-13B | 1 | Other/Unknown |
| 1063 | Claude4 | 1 | Other/Unknown |
| 1064 | LLaMa 3 | 1 | Other/Unknown |
| 1065 | Mistral 3 | 1 | Other/Unknown |
| 1066 | Qwen 3B | 1 | Other/Unknown |
| 1067 | GPT-2-Medium; GPT-2-Large; OPT-125M; OPT-350M; BLOOM-560M; BLOOMZ-560M; Qwen-0.5B | 1 | Other/Unknown |
| 1068 | Claude-3-Haiku; Claude-3-Sonnet; Claude-3.5-Sonnet; Claude-3-Opus; GPT-4o-Mini; GPT-4o; Gemini-1.5-Flash; Gemini-1.5-Pro; LLaMA-3.2-1B; LLaMA-3.2-3B; LLaMA-3.1-8B; LLaMA-3.1-70B; LLaMA-3.1-405B; Gemma-2-2B; Gemma-2-9B; Gemma-2-27B; Aya-23-8B; Command-R-Plus; Mistral-7B; Mistral-Nemo; Mixtral-8x22B; Qwen-2.5-72B; PersianMind-v1.0; Dorna-LLaMA3-8B | 1 | Other/Unknown |
| 1069 | Mistral-7B; Zephyr-7B; BLOOM-7B; Llama-2-7B; Grok; ChatGPT | 1 | Other/Unknown |
| 1070 | Claude 96.5 | 1 | Other/Unknown |
| 1071 | claude-3-opus | 1 | Other/Unknown |
| 1072 | t5 4 | 1 | Other/Unknown |
| 1073 | Llama-3.3-70B; Qwen-2.5-72B; Aya-Expanse-32B; Gemma-3-27B | 1 | Other/Unknown |
| 1074 | Llama-3.3-70B; Aya-23-8B; Qwen-2.5-7B; AceGPT-v1.5-7B; AceGPT-v2-7B; JAIS-13B; XLM-R; ARBERT; MARBERT; CAMeLBERT; AraBERT | 1 | Other/Unknown |
| 1075 | distilBERT | 1 | Pre-LLM / Encoder |
| 1076 | Flux-1.0-dev; Stable-Diffusion-3.5-Large; Imagen3; GPT-Image | 1 | Other/Unknown |
| 1077 | Mistral 0.3 Instruct | 1 | Other/Unknown |
| 1078 | Mistral 0.3 57 | 1 | Other/Unknown |
| 1079 | Mistral 0.3 68 | 1 | Other/Unknown |
| 1080 | Qwen 494M | 1 | Other/Unknown |
| 1081 | Deepseek 4o | 1 | Other/Unknown |
| 1082 | Deepseek R1 | 1 | Other/Unknown |
| 1083 | BLIP-VQA; LXMERT; PaLM-VQA; Gemini-2.0-Pro | 1 | Other/Unknown |
| 1084 | LLama1 | 1 | Other/Unknown |
| 1085 | LLama2 | 1 | Other/Unknown |
| 1086 | Llama-2-CHAT | 1 | Other/Unknown |
| 1087 | mistral 30 35 | 1 | Other/Unknown |
| 1088 | LLaVA-1.5; MOLMO; LLaVA-NeXT; Phi-3-Vision; Idefics2; Mantis-Idefics2; LLaVA-OneVision; Qwen2-VL; InternLM-XComposer-2.5; mPLUG-Owl3; GPT-4o | 1 | Other/Unknown |
| 1089 | Claude-3.5-Sonnet; Claude-3.5-Haiku; GPT-4o; GPT-4o-Mini; Gemini-1.5-Pro; Gemini-1.5-Flash; Llama-3.1-405B; Llama-3.3-70B; Gemma-2-2B; Gemma-2-9B; Llama-3.2-1B; Llama-3.2-3B; Llama-3.1-8B; Phi-3.5-Mini; Phi-3-Medium; Qwen-2.5-0.5B; Qwen-2.5-1.5B; Qwen-2.5-3B; Qwen-2.5-7B; Qwen-2.5-14B; Qwen-2.5-32B | 1 | Other/Unknown |
| 1090 | LLaMA 93.99 | 1 | Other/Unknown |
| 1091 | LLaMA3.1. | 1 | Other/Unknown |
| 1092 | Claude 4 Opus | 1 | Other/Unknown |
| 1093 | LLama-3.3 | 1 | Other/Unknown |
| 1094 | QWEN 3 | 1 | Other/Unknown |
| 1095 | Llama 11 | 1 | Other/Unknown |
| 1096 | Llama 8 | 1 | Other/Unknown |
| 1097 | Mistral 2410 4 | 1 | Other/Unknown |
| 1098 | Mistral 24B | 1 | Other/Unknown |
| 1099 | Mistral 2501 5 | 1 | Other/Unknown |
| 1100 | Mistral- 2410 | 1 | Other/Unknown |
| 1101 | Mistral-2501 24B | 1 | Other/Unknown |
| 1102 | Llama-70B | 1 | Other/Unknown |
| 1103 | EXAONE | 1 | Other/Unknown |
| 1104 | Plutus-8B | 1 | Other/Unknown |
| 1105 | Qwen2-7B | 1 | Other/Unknown |
| 1106 | Qwen2-72B | 1 | Other/Unknown |
| 1107 | OLMo-7B | 1 | Other/Unknown |
| 1108 | CLAUDE 3.5 SONNET | 1 | Other/Unknown |
| 1109 | CLAUDE-3 HAIKU | 1 | Anthropic |
| 1110 | CLAUDE-3-HAIKU | 1 | Other/Unknown |
| 1111 | Claude 3.5-sonnet | 1 | Other/Unknown |
| 1112 | Claude Haiku | 1 | Other/Unknown |
| 1113 | Claude-sonnet | 1 | Other/Unknown |
| 1114 | MISTRAL-7B | 1 | Other/Unknown |
| 1115 | QWEN-32B | 1 | Other/Unknown |
| 1116 | Llama 32.20 | 1 | Other/Unknown |
| 1117 | Llama 34.80 | 1 | Other/Unknown |
| 1118 | Llama 4.40 | 1 | Other/Unknown |
| 1119 | Llama 4.98 | 1 | Other/Unknown |
| 1120 | Llama 69.19 | 1 | Other/Unknown |
| 1121 | Llama 69.7 | 1 | Other/Unknown |
| 1122 | Llama 72.7 | 1 | Other/Unknown |
| 1123 | Llama 77.13 | 1 | Other/Unknown |
| 1124 | BART Counterfactual | 1 | Other/Unknown |
| 1125 | BART-base | 1 | Other/Unknown |
| 1126 | DeBERTa NLI | 1 | Other/Unknown |
| 1127 | Falcon Instruct | 1 | Other/Unknown |
| 1128 | Flan-T5 NLI | 1 | Other/Unknown |
| 1129 | LLaMA 2 Chat | 1 | Other/Unknown |
| 1130 | LLaMa2 | 1 | Other/Unknown |
| 1131 | OPT6 | 1 | Other/Unknown |
| 1132 | Phi-3-3 | 1 | Other/Unknown |
| 1133 | T5 Answer | 1 | Other/Unknown |
| 1134 | T5 NLI | 1 | Other/Unknown |
| 1135 | T5 Word | 1 | Other/Unknown |
| 1136 | T5-small | 1 | Other/Unknown |
| 1137 | InternVL2.5-4B | 1 | Other/Unknown |
| 1138 | InternVL2.5-8B | 1 | Other/Unknown |
| 1139 | InternVL2.5-38B | 1 | Other/Unknown |
| 1140 | Qwen2.5-VL-3B | 1 | Other/Unknown |
| 1141 | Qwen2.5-VL-32B | 1 | Other/Unknown |
| 1142 | T500 | 1 | Other/Unknown |
| 1143 | llama2.70 | 1 | Other/Unknown |
| 1144 | llama2.70. chat | 1 | Other/Unknown |
| 1145 | mixtral 8x7b | 1 | Other/Unknown |
| 1146 | Minerva-3B | 1 | Other/Unknown |
| 1147 | Zefiro | 1 | Other/Unknown |
| 1148 | Llama-Krikri-8B | 1 | Other/Unknown |
| 1149 | Meltemi | 1 | Other/Unknown |
| 1150 | Barton | 1 | Other/Unknown |
| 1151 | Jais-13B | 1 | Other/Unknown |
| 1152 | Jais-v3-30B | 1 | Other/Unknown |
| 1153 | AceGPT-v2 | 1 | Other/Unknown |
| 1154 | SILMA | 1 | Other/Unknown |
| 1155 | Fanar | 1 | Other/Unknown |
| 1156 | ALLAM | 1 | Other/Unknown |
| 1157 | Claude haiku | 1 | Other/Unknown |
| 1158 | claude3. | 1 | Other/Unknown |
| 1159 | Mistral 7BInstruct | 1 | Other/Unknown |
| 1160 | Falcon-Arabic | 1 | Other/Unknown |
| 1161 | DistilBERTimbau | 1 | Other/Unknown |
| 1162 | PTT5 | 1 | Other/Unknown |
| 1163 | GigaChat-Max | 1 | Other/Unknown |
| 1164 | deepseek-coder | 1 | DeepSeek |
| 1165 | deepseek-v2 | 1 | DeepSeek |
| 1166 | Claude- Sonnet | 1 | Other/Unknown |
| 1167 | Claude-4.1-Opus | 1 | Other/Unknown |
| 1168 | Whisper | 1 | Other/Unknown |
| 1169 | LLaMa-3.3 | 1 | Other/Unknown |
| 1170 | Mistral12b | 1 | Other/Unknown |
| 1171 | Dolly24 | 1 | Other/Unknown |
| 1172 | Mistral 0.74 2 | 1 | Other/Unknown |
| 1173 | Mistral 11.47 69 | 1 | Other/Unknown |
| 1174 | Qwen 0.12 | 1 | Other/Unknown |
| 1175 | Qwen 0.90 | 1 | Other/Unknown |
| 1176 | Gemini 2.0 flash | 1 | Other/Unknown |
| 1177 | LlaMA 2 | 1 | Other/Unknown |
| 1178 | Qwen et | 1 | Other/Unknown |
| 1179 | chatglm-6b | 1 | Other/Unknown |
| 1180 | falcon-40b | 1 | Other/Unknown |
| 1181 | t5-3b | 1 | Other/Unknown |
| 1182 | vicuna | 1 | Open-source (misc) |
| 1183 | Llama-3.2-90B-Vision | 1 | Other/Unknown |
| 1184 | InternVL2 | 1 | Other/Unknown |
| 1185 | Gemma-3-27B | 1 | Other/Unknown |
| 1186 | Breeze2 | 1 | Other/Unknown |
| 1187 | deepseek-vl2 | 1 | Other/Unknown |
| 1188 | mistral-nemo | 1 | Other/Unknown |
| 1189 | qwen-3 | 1 | Other/Unknown |
| 1190 | Gemma-2. | 1 | Other/Unknown |
| 1191 | Aya-Vision-32B | 1 | Other/Unknown |
| 1192 | Aya-Vision-8B | 1 | Other/Unknown |
| 1193 | LLaMA 3.2. | 1 | Other/Unknown |
| 1194 | DeBERTa-based | 1 | Other/Unknown |
| 1195 | WizardLM-2 | 1 | Other/Unknown |
| 1196 | DeepSeek 67B | 1 | Other/Unknown |
| 1197 | qwen2 | 1 | Other/Unknown |
| 1198 | Stable Diffusion 3 | 1 | Other/Unknown |
| 1199 | YandexART 2 | 1 | Other/Unknown |
| 1200 | Midjourney v6 | 1 | Other/Unknown |
| 1201 | Ernie | 1 | Open-source (misc) |
| 1202 | GPT-4O-MINI | 1 | Other/Unknown |
| 1203 | LLAMA3 | 1 | Other/Unknown |
| 1204 | Claude-Sonnet-3.7 | 1 | Other/Unknown |
| 1205 | Claude-Sonnet-4 | 1 | Other/Unknown |
| 1206 | Qwen-3-235B | 1 | Other/Unknown |
| 1207 | InternLM3 | 1 | Other/Unknown |
| 1208 | CogVLM2 | 1 | Other/Unknown |
| 1209 | InternVL-Chat-V1.5 | 1 | Other/Unknown |
| 1210 | MiniCPM-V2.5 | 1 | Other/Unknown |
| 1211 | QwenVL-Chat | 1 | Other/Unknown |
| 1212 | InternLM-XComposer2-VL | 1 | Other/Unknown |
| 1213 | DeepSeek-VL | 1 | Other/Unknown |
| 1214 | Monkey-Chat | 1 | Other/Unknown |
| 1215 | ShareGPT4V | 1 | Other/Unknown |
| 1216 | LLaVA-v1.5 | 1 | Other/Unknown |
| 1217 | Yi-VL | 1 | Other/Unknown |
| 1218 | InstructBLIP | 1 | Other/Unknown |
| 1219 | InternVL2-Llama3 | 1 | Other/Unknown |
| 1220 | Qwen2-VL | 1 | Other/Unknown |
| 1221 | gemma-1.1 | 1 | Other/Unknown |
| 1222 | Claude 2. | 1 | Other/Unknown |
| 1223 | LLaMA-2 Chat | 1 | Other/Unknown |
| 1224 | Qwen-family | 1 | Other/Unknown |
| 1225 | Phi4 0 | 1 | Other/Unknown |
| 1226 | Phi4-14B | 1 | Other/Unknown |
| 1227 | DeepSeek-70B | 1 | Other/Unknown |
| 1228 | BARTL | 1 | Other/Unknown |
| 1229 | Swallow-8B | 1 | Other/Unknown |
| 1230 | LLaMA2-Chat | 1 | Other/Unknown |
| 1231 | mixtral-8x7b | 1 | Other/Unknown |
| 1232 | CodeLLaMA | 1 | Meta |
| 1233 | o1-mini | 1 | OpenAI |
| 1234 | Qwen2.5-Omni-7B | 1 | Other/Unknown |
| 1235 | Qwen2.5-Omni-3B | 1 | Other/Unknown |
| 1236 | Baichuan-Omni-1.5 | 1 | Other/Unknown |
| 1237 | Llama-3.2-11B-Vision | 1 | Other/Unknown |
| 1238 | UI-TARS-1.5-7B | 1 | Other/Unknown |
| 1239 | Idefics2-8b | 1 | Other/Unknown |
| 1240 | PaliGemma-2 | 1 | Other/Unknown |
| 1241 | Qwen MMMLU | 1 | Other/Unknown |
| 1242 | LLAMA 4 | 1 | Other/Unknown |
| 1243 | Phi-4-mini | 1 | Other/Unknown |
| 1244 | DictaLM2.0 | 1 | Other/Unknown |
| 1245 | Alpaca-2 | 1 | Other/Unknown |
| 1246 | GPT 4O | 1 | Other/Unknown |
| 1247 | LlaMA 3.1 | 1 | Other/Unknown |
| 1248 | LlaMA-3.1 | 1 | Other/Unknown |
| 1249 | Qwen 3.5 | 1 | Other/Unknown |
| 1250 | codellama 22 | 1 | Other/Unknown |
| 1251 | deepseek6 | 1 | Other/Unknown |
| 1252 | llama 24 | 1 | Other/Unknown |
| 1253 | ChatGLM-4 | 1 | Other/Unknown |
| 1254 | Baichuan-4 | 1 | Other/Unknown |
| 1255 | Qwen-Turbo | 1 | Other/Unknown |
| 1256 | qwen-13b | 1 | Other/Unknown |
| 1257 | qwen-7b | 1 | Other/Unknown |
| 1258 | ChatGPT-4o-Latest | 1 | Other/Unknown |
| 1259 | Qwen2.5-0.5B | 1 | Other/Unknown |
| 1260 | Qwen2.5-3B | 1 | Other/Unknown |
| 1261 | Mistral-7B-v0.3 | 1 | Other/Unknown |
| 1262 | Gemma2-27B-it | 1 | Other/Unknown |
| 1263 | DeepSeek-GRM | 1 | Other/Unknown |
| 1264 | Qwen-Instruct | 1 | Other/Unknown |
| 1265 | Claude-4-sonnet | 1 | Other/Unknown |
| 1266 | DeepSeek 29 | 1 | Other/Unknown |
| 1267 | llama-guard | 1 | Other/Unknown |
| 1268 | llamaguard | 1 | Other/Unknown |
| 1269 | phi-3 | 1 | Microsoft |
| 1270 | DeepSeek-R1-Distill-Qwen-1.5B | 1 | Other/Unknown |
| 1271 | DeepSeek-R1-Distill-Qwen-7B | 1 | Other/Unknown |
| 1272 | DeepSeek-R1-Distill-Qwen-14B | 1 | Other/Unknown |
| 1273 | DeepSeek-R1-Distill-Qwen-32B | 1 | Other/Unknown |
| 1274 | DeepSeek-R1-Distill-Llama-70B | 1 | Other/Unknown |
| 1275 | Doubao-pro-256k | 1 | Other/Unknown |
| 1276 | Yi-Lightning | 1 | Other/Unknown |
| 1277 | MiniMax-01 | 1 | Other/Unknown |
| 1278 | Moonshot-v1-128k | 1 | Other/Unknown |
| 1279 | Spark-4.0-Ultra | 1 | Other/Unknown |
| 1280 | ERNIE-4.0-Turbo-128K | 1 | Other/Unknown |
| 1281 | Step-2-16K | 1 | Other/Unknown |
| 1282 | Hunyuan-Turbo | 1 | Other/Unknown |
| 1283 | Deepseek-V3 | 1 | Other/Unknown |
| 1284 | DeBERTa V2 | 1 | Other/Unknown |
| 1285 | DeBERTa-base | 1 | Other/Unknown |
| 1286 | Poro-34B | 1 | Other/Unknown |
| 1287 | multilingual and Basque-adapted LLMs | 1 | Other/Unknown |
| 1288 | Cohere-Aya | 1 | Other/Unknown |
| 1289 | claude-3.5 | 1 | Other/Unknown |
| 1290 | claude-3.5 Sonnet | 1 | Other/Unknown |
| 1291 | llama 70. | 1 | Other/Unknown |
| 1292 | llama3.3 | 1 | Other/Unknown |
| 1293 | OLMo | 1 | Other/Unknown |
| 1294 | BLOOM72 | 1 | Other/Unknown |
| 1295 | Claude 3.5 sonnet | 1 | Other/Unknown |
| 1296 | DeepSeek-R126 | 1 | Other/Unknown |
| 1297 | DeepSeek-V327 | 1 | Other/Unknown |
| 1298 | DeepSeek-based | 1 | Other/Unknown |
| 1299 | Deepseek-r1 | 1 | Other/Unknown |
| 1300 | Deepseek-v3 | 1 | Other/Unknown |
| 1301 | LLaMA-224 | 1 | Other/Unknown |
| 1302 | LLaMA23 | 1 | Other/Unknown |
| 1303 | Qwen Family28 | 1 | Other/Unknown |
| 1304 | Qwen2.530 | 1 | Other/Unknown |
| 1305 | phi-3 47 | 1 | Other/Unknown |
| 1306 | phi-4 18 | 1 | Other/Unknown |
| 1307 | Sarvam | 1 | Other/Unknown |
| 1308 | Indic-Gemma | 1 | Other/Unknown |
| 1309 | Airavata | 1 | Other/Unknown |
| 1310 | o3-pro | 1 | Other/Unknown |
| 1311 | Gemma 35.15 | 1 | Other/Unknown |
| 1312 | Gemma 35.31 | 1 | Other/Unknown |
| 1313 | Gemma 69.37 | 1 | Other/Unknown |
| 1314 | Phi-4-14B | 1 | Other/Unknown |
| 1315 | llama3. | 1 | Other/Unknown |
| 1316 | Dolly 7. | 1 | Other/Unknown |
| 1317 | deepseek-ai | 1 | Other/Unknown |
| 1318 | Mistral-medium | 1 | Other/Unknown |
| 1319 | Mistral-small | 1 | Other/Unknown |
| 1320 | Deepseek-3 | 1 | Other/Unknown |
| 1321 | Qwen-3.1 | 1 | Other/Unknown |
| 1322 | VC-LLM | 1 | Other/Unknown |
| 1323 | GLM-4-9B | 1 | Other/Unknown |
| 1324 | Yi-1.5-34B | 1 | Other/Unknown |
| 1325 | InternLM2.5-20B | 1 | Other/Unknown |
| 1326 | TigerBot-70B | 1 | Other/Unknown |
| 1327 | Ziya-LLaMA-13B | 1 | Other/Unknown |
| 1328 | Qwen2.5-32B-Instruct | 1 | Other/Unknown |
| 1329 | Qwen-MT | 1 | Other/Unknown |
| 1330 | claude 3.7 sonnet | 1 | Other/Unknown |
| 1331 | deepseek llama3 | 1 | Other/Unknown |
| 1332 | deepseek chat | 1 | Other/Unknown |
| 1333 | qwen 2.5 | 1 | Other/Unknown |
| 1334 | Qwen-SEA_LION | 1 | Other/Unknown |
| 1335 | H3FUSION | 1 | Other/Unknown |
| 1336 | TRINITYX | 1 | Other/Unknown |
| 1337 | Phi-3-14B | 1 | Other/Unknown |
| 1338 | DeepSeek-7B | 1 | Other/Unknown |
| 1339 | Gemma-2-9B-it | 1 | Other/Unknown |
| 1340 | Qwen3-30B-A3B | 1 | Other/Unknown |
| 1341 | Mistral-7B-Instruct-v0.3 | 1 | Other/Unknown |
| 1342 | GPT-5.2 | 1 | Other/Unknown |
| 1343 | Gemini 3 Pro | 1 | Other/Unknown |
| 1344 | Gemini 2.0 Flash | 1 | Other/Unknown |
| 1345 | Llama 3.3 70B | 1 | Other/Unknown |
| 1346 | Mistral Large 3 | 1 | Other/Unknown |
| 1347 | Qwen3 Max | 1 | Other/Unknown |
| 1348 | Qwen 2.5 72B | 1 | Other/Unknown |
| 1349 | Kimi K2.5 | 1 | Other/Unknown |
| 1350 | MiniMax M2 | 1 | Other/Unknown |
| 1351 | GPT-OSS | 1 | Other/Unknown |
| 1352 | GPT-5.1 | 1 | Other/Unknown |
| 1353 | DeepSeek-V3.2 | 1 | Other/Unknown |
| 1354 | Qwen3-Max | 1 | Other/Unknown |
| 1355 | Lingguang | 1 | Other/Unknown |
| 1356 | Doubao | 1 | Other/Unknown |
| 1357 | Wenxin Yiyan 5.0-Preview | 1 | Other/Unknown |
| 1358 | Llama-3.1-Swallow-8B | 1 | Other/Unknown |
| 1359 | llm-jp-3.1-13b | 1 | Other/Unknown |
| 1360 | gpt-oss-20b | 1 | Other/Unknown |
| 1361 | LLama 4 | 1 | Other/Unknown |
| 1362 | Claude 3.7 sonnet | 1 | Other/Unknown |
| 1363 | LLaMa-3.1. | 1 | Other/Unknown |
| 1364 | LLama 3.1 | 1 | Other/Unknown |
| 1365 | Mistral- 24 | 1 | Other/Unknown |
| 1366 | Mistral-24.07 | 1 | Other/Unknown |
| 1367 | Gemini 2.5 Flash Lite | 1 | Other/Unknown |
| 1368 | EXAONE 3.5 | 1 | Other/Unknown |
| 1369 | Qwen-3B | 1 | Other/Unknown |
| 1370 | 80+ open- and closed-source LLMs | 1 | Other/Unknown |
| 1371 | Qwen3-0.6B | 1 | Other/Unknown |
| 1372 | Qwen3-1.7B | 1 | Other/Unknown |
| 1373 | MiniCPM4-0.5B | 1 | Other/Unknown |
| 1374 | MiniCPM4-8B | 1 | Other/Unknown |
| 1375 | Hunyuan-0.5B | 1 | Other/Unknown |
| 1376 | Hunyuan-1.8B | 1 | Other/Unknown |
| 1377 | Hunyuan-7B | 1 | Other/Unknown |
| 1378 | openPangu-Embedded-1B | 1 | Other/Unknown |
| 1379 | openPangu-Embedded-7B | 1 | Other/Unknown |
| 1380 | Falcon-h1 | 1 | Other/Unknown |
| 1381 | Qwen R1 | 1 | Other/Unknown |
| 1382 | Gemini 3 Flash Preview (thinking) | 1 | Other/Unknown |
| 1383 | Gemini 2.5 Pro (thinking) | 1 | Other/Unknown |
| 1384 | DeepSeek Chat v3.1 (thinking) | 1 | Other/Unknown |
| 1385 | Gemini 2.5 Flash (thinking) | 1 | Other/Unknown |
| 1386 | Gemini 3 Flash Preview | 1 | Other/Unknown |
| 1387 | GPT-5 Chat | 1 | Other/Unknown |
| 1388 | DeepSeek Chat v3.1 | 1 | Other/Unknown |
| 1389 | Claude Haiku 4.5 | 1 | Other/Unknown |
| 1390 | Qwen3-235B-A22B | 1 | Other/Unknown |
| 1391 | Llama 3.3 70B Instruct | 1 | Other/Unknown |
| 1392 | Llama 4 Maverick | 1 | Other/Unknown |
| 1393 | Llama 3.1 8B Instruct | 1 | Other/Unknown |
| 1394 | Qwen3-4B Instruct | 1 | Other/Unknown |
| 1395 | InternLM3-8B Instruct | 1 | Other/Unknown |
| 1396 | Qwen2.5-7B Instruct | 1 | Other/Unknown |
| 1397 | Aya Expanse 8B | 1 | Other/Unknown |
| 1398 | Llama 3.2 3B Instruct | 1 | Other/Unknown |
| 1399 | Aya 23 8B | 1 | Other/Unknown |

### 2.2 Model Family Grouping

Papers per model family (a paper is counted once per family even if it uses multiple models from that family):

| Rank | Family | Papers | % of Assessed |
|-----:|--------|-------:|--------------:|
| 1 | OpenAI | 1027 | 65.1% |
| 2 | Meta | 717 | 45.4% |
| 3 | Other/Unknown | 678 | 43.0% |
| 4 | Pre-LLM / Encoder | 549 | 34.8% |
| 5 | Google | 480 | 30.4% |
| 6 | Alibaba | 319 | 20.2% |
| 7 | Anthropic | 308 | 19.5% |
| 8 | Mistral AI | 296 | 18.8% |
| 9 | Open-source (misc) | 236 | 15.0% |
| 10 | DeepSeek | 170 | 10.8% |
| 11 | Embeddings | 62 | 3.9% |
| 12 | Microsoft | 49 | 3.1% |
| 13 | xAI | 32 | 2.0% |
| 14 | Cohere | 23 | 1.5% |

### 2.3 Proprietary vs Open-Source Breakdown

**By model mention count** (each model×paper counts once):

| Category | Mentions | % |
|----------|--------:|---------:|
| Proprietary (closed-source) | 2490 | 25.7% |
| Open-source / open-weight | 7193 | 74.3% |
| **Total** | **9683** | **100%** |

**By paper count** (papers using at least one model of that type):

| Category | Papers |
|----------|-------:|
| Uses at least one proprietary model | 1028 |
| Uses at least one open-source model | 1448 |

### 2.4 Models Per Paper Distribution

Among the 1578 papers with LLM models identified:

| Models per paper | Papers | % |
|:----------------:|-------:|------:|
| 1 | 257 | 16.3% |
| 2-3 | 372 | 23.6% |
| 4-6 | 430 | 27.2% |
| 7+ | 519 | 32.9% |

### 2.5 Model Co-Occurrence Matrix (Top 12)

How often the top 12 models appear together in the same paper:

| | GPT-4 | BERT | Llama | Llama-3 | Qwen | ChatGPT | GPT-3.5 | Claude | GPT-4o | Mistral | Gemma | GPT-3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **GPT-4** | — | 139 | 234 | 226 | 191 | 186 | 246 | 230 | 141 | 162 | 138 | 154 |
| **BERT** | 139 | — | 138 | 50 | 45 | 99 | 68 | 45 | 77 | 45 | 61 | 100 |
| **Llama** | 234 | 138 | — | 100 | 114 | 134 | 88 | 101 | 130 | 90 | 114 | 115 |
| **Llama-3** | 226 | 50 | 100 | — | 173 | 54 | 95 | 118 | 84 | 149 | 117 | 38 |
| **Qwen** | 191 | 45 | 114 | 173 | — | 47 | 71 | 120 | 89 | 114 | 111 | 35 |
| **ChatGPT** | 186 | 99 | 134 | 54 | 47 | — | 82 | 69 | 57 | 43 | 40 | 106 |
| **GPT-3.5** | 246 | 68 | 88 | 95 | 71 | 82 | — | 84 | 45 | 72 | 42 | 126 |
| **Claude** | 230 | 45 | 101 | 118 | 120 | 69 | 84 | — | 82 | 83 | 58 | 41 |
| **GPT-4o** | 141 | 77 | 130 | 84 | 89 | 57 | 45 | 82 | — | 42 | 68 | 58 |
| **Mistral** | 162 | 45 | 90 | 149 | 114 | 43 | 72 | 83 | 42 | — | 91 | 25 |
| **Gemma** | 138 | 61 | 114 | 117 | 111 | 40 | 42 | 58 | 68 | 91 | — | 34 |
| **GPT-3** | 154 | 100 | 115 | 38 | 35 | 106 | 126 | 41 | 58 | 25 | 34 | — |

---

## 3. Data Availability Analysis

### 3.1 URL Presence Statistics

| Status | Papers | % |
|--------|-------:|------:|
| Has public data URL | 1196 | 59.7% |
| No data URL (NA) | 806 | 40.3% |

### 3.2 Hosting Platform Breakdown

Among papers with data URLs, classified by hosting platform:

| Platform | Papers | % of URLs |
|----------|-------:|----------:|
| GitHub | 794 | 66.4% |
| HuggingFace | 238 | 19.9% |
| Other | 106 | 8.9% |
| OSF | 21 | 1.8% |
| Zenodo | 14 | 1.2% |
| Kaggle | 9 | 0.8% |
| Anonymous (review) | 8 | 0.7% |
| GitLab | 6 | 0.5% |
| Mendeley Data | 6 | 0.5% |
| DOI/Repository | 3 | 0.3% |
| Papers With Code | 2 | 0.2% |
| Google Drive | 1 | 0.1% |

### 3.3 Overlap: LLM Models AND Data URLs

| Combination | Papers | % |
|-------------|-------:|------:|
| LLM models + data URL | 1075 | 53.7% |
| LLM models only (no URL) | 503 | 25.1% |
| Data URL only (no models) | 121 | 6.0% |
| Neither | 303 | 15.1% |

---

## 4. Gap Analysis

### 4.1 Papers with LLM Models but No Public Data URL

**503 papers** assess LLM models but have no publicly available data URL.

<details>
<summary>Click to expand (503 papers)</summary>

| # | Paper | Models |
|--:|-------|--------|
| 1 | [[2016-Bolukbasi-Man is to Computer Programmer as Woman is to]] | Word2Vec, GloVe |
| 2 | [[2018-Santana-Is there Gender Bias and Stereotype in Portuguese Word Embeddings]] | Word2Vec |
| 3 | [[2019-He-Unlearn Dataset Bias in Natural Language]] | BERT |
| 4 | [[2019-Kreutz-GermEval 2019 Task 2]] | BERT |
| 5 | [[2019-Struß-Overview of GermEval Task 2, 2019 Shared Task on]] | BERT |
| 6 | [[2019-University of São Paulo-Moral Stance Recognition and Polarity]] | Word2Vec |
| 7 | [[2020-Forbes-Social Chemistry 101]] | GPT-2, T5, BART |
| 8 | [[2020-Gabriel-Artificial Intelligence Values and Alignment]] | Barto |
| 9 | [[2020-Hossu-UIC-NLP at SemEval-2020 Task 10]] | ELMo, GloVe, Word2Vec |
| 10 | [[2020-Kurpicz-Briki-Cultural Differences in Bias Origin and Gender Bias in Pre-Trained]] | GloVe, word2vec |
| 11 | [[2020-Rybak-KLEJ Comprehensive Benchmark for Polish Language Understanding]] | BERT, ELMo |
| 12 | [[2021-Chakravarthi-Findings of the Sentiment Analysis of]] | BERT, DistilBERT, RoBERTa, Word2Vec |
| 13 | [[2021-Clark-All That's 'Human' Is Not Gold]] | GPT-2, GPT-3 |
| 14 | [[2021-Kurpicz-Briki-A World Full of Stereotypes Further Investigation on Origin and]] | word2vec |
| 15 | [[2021-Mohapatra-Automatic Hate Speech Detection in English-Odia Code Mixed Social]] | Glove, Word2Vec |
| 16 | [[2021-Munshi-Towards an Automated Islamic Fatwa System]] | BERT |
| 17 | [[2021-Perifanos-Multimodal Hate Speech Detection in Greek Social Media]] | BERT |
| 18 | [[2021-Plaza-del-Arco-Overview of MeOffendEs at IberLEF 2021 Offensive Language Detection]] | BERT, RoBERTa, gloVe, word2vec |
| 19 | [[2021-Prabhumoye-Case Study]] | BERT |
| 20 | [[2021-Risch-GermEval 2021 Shared Task on the Identification of Toxic Engaging and]] | BERT |
| 21 | [[2021-Wang-MedAI at SemEval-2021 Task 5]] | RoBERTa |
| 22 | [[2021-Weidinger-Ethical and social risks of harm from Language]] | BERT, GPT-2, GPT-3, GPT2, RoBERTa, T5, T5-11B, XLNet |
| 23 | [[2021-Zou-Persistent Anti-Muslim Bias in Large Language]] | GPT-3 |
| 24 | [[2022-Abbasi-Deep Learning for Religious and Continent-Based]] | GloVe, Word2vec |
| 25 | [[2022-Beyhan-A Turkish Hate Speech Dataset and Detection System]] | BERT |
| 26 | [[2022-Caron-Identifying and Manipulating the Personality]] | BERT, GPT-2 |
| 27 | [[2022-Hendrycks-X-Risk Analysis for AI Research]] | GPT-2 |
| 28 | [[2022-Li-Evaluating Psychological Safety of Large Language]] | GPT-3, InstructGPT, GPT-3.5, GPT-4, Llama-2 |
| 29 | [[2022-Litvak-Offensive language detection in Hebrew can other languages help]] | BERT |
| 30 | [[2022-Rodríguez-Sánchez-Overview of EXIST 2022 sEXism Identification in Social neTworks]] | BERT, RoBERTa |
| 31 | [[2022-Trager-The Moral Foundations Reddit Corpus]] | Llama-3, BERT |
| 32 | [[2022-Unknown-HOTTEST Hate and Offensive Content Identification]] | BERT, XLM-RoBERTa, IndicBERT, MuRIL |
| 33 | [[2022-Zagar-Slovene SuperGLUE Benchmark Translation and Evaluation]] | BERT, RoBERTa |
| 34 | [[2023-Alsalka-Is GPT-4 a Good Islamic Expert]] | GPT-4 |
| 35 | [[2023-Arora-Probing PLMs for Cross-Cultural Values C3NLP Workshop]] | BERT |
| 36 | [[2023-Avetisyan-Large Language Models and Low-Resource Languages An Examination of]] | BERT, RoBERTa |
| 37 | [[2023-Badawi-KurdiSent A Corpus for Kurdish Sentiment Analysis]] | XLM-R |
| 38 | [[2023-Bang-Towards Answering Open-ended Ethical Quandary]] | BERT |
| 39 | [[2023-Benkler-Assessing LLMs for Moral Value Pluralism]] | RoBERTa |
| 40 | [[2023-Catapang-EMoTES-3K]] | RoBERTa, Flan-T5 |
| 41 | [[2023-Chang-niceNLP at SemEval-2023 Task 10]] | DeBERTa, RoBERTa, BERT |
| 42 | [[2023-Chen-Case Law Grounding]] | GPT-4 |
| 43 | [[2023-DN-HeQ a Large and Diverse Hebrew Reading Comprehension Benchmark]] | ChatGPT, mBERT, AlephBERT, AlephBERTGimel |
| 44 | [[2023-Davis-Benchmarks for Automated Commonsense Reasoning]] | BERT, ChatGPT, GPT-3 |
| 45 | [[2023-Dehghani-Persian Offensive Language Detection Dehghani et al.]] | BERT, ELMo, GPT3, GloVe, RoBERTa, Word2Vec |
| 46 | [[2023-Deng-Probing the Moral Development of Large Language]] | GPT-3, GPT-3.5, GPT-4, ChatGPT, PaLM-2, Llama-2 |
| 47 | [[2023-Elrod-Nothing New Under the Sun The]] | GPT |
| 48 | [[2023-Ghosh-ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores]] | ChatGPT, BERT |
| 49 | [[2023-Hartmann-The political ideology of conversational AI]] | ChatGPT |
| 50 | [[2023-Hämmerl-Speaking Multiple Languages Affects the Moral Bias of Language Models]] | BERT, RoBERTa |
| 51 | [[2023-Karra-Estimating the Personality of White-Box Language]] | GPT-2, GPT-3, GPT-3.5, Llama, XLNet |
| 52 | [[2023-Li-On the steerability of large language models]] | Falcon |
| 53 | [[2023-Lima-A Call for a Research Agenda on Fair NLP for Portuguese]] | word2vec |
| 54 | [[2023-Mager-Neural Machine Translation for the Indigenous Languages of the]] | BART, BERT, ELMO, Gemma |
| 55 | [[2023-Morris-Levels of AGI]] | ALBERT, GPT-4, Llama 2 |
| 56 | [[2023-Munn-The Five Tests Designing and Evaluating]] | Falconer |
| 57 | [[2023-Nguyen-Abusive Span Detection for Vietnamese Narrative Texts]] | BERT, RoBERTa |
| 58 | [[2023-Nguyen-RMDM A Multilabel Fakenews Dataset for Vietnamese Evidence]] | BERT, ChatGPT, GPT 3, GPT 3.5, GPT-3, GPT-3.5, GPT-4 |
| 59 | [[2023-Nguyen-VinaLLaMA LLaMA-based Vietnamese Foundation Model]] | BLOOM, BLOOM-7B, BLOOMZ, ChatGPT, GPT-3, GPT-3.5, GPT-4, ... |
| 60 | [[2023-Park-AI Deception]] | ChatGPT, GPT-3, GPT-3.5, GPT-4 |
| 61 | [[2023-Plaza-del-Arco-MarIA and BETO are Sexist Evaluating Gender Bias in Large Language]] | ALBERT, BERT, Bartl, ELECTRA, RoBERTa |
| 62 | [[2023-Qian-Understanding Chinese Moral Stories with Further]] | BERT, RoBERTa, T5 |
| 63 | [[2023-Rao-Ethical Reasoning over Moral Alignment]] | GPT-4, GPT-3.5, GPT-3 |
| 64 | [[2023-Rystrøm-Apolitical Intelligence]] | ChatGPT, GPT-3, GPT-4 |
| 65 | [[2023-Rytting-Towards Coding Social Science Datasets with]] | GPT-3 |
| 66 | [[2023-Sabane-Breaking Language Barriers A Question-Answering Dataset]] | BERT, RoBERTa |
| 67 | [[2023-Schulhoff-HackAPrompt]] | GPT-3, ChatGPT, Flan-T5 |
| 68 | [[2023-Shalumov-HeRo RoBERTa and Longformer Hebrew Language Models]] | BERT, RoBERTa |
| 69 | [[2023-Shmidman-Introducing DictaLM - A Large Generative Language Model for Modern]] | DictaLM |
| 70 | [[2023-Sukhamsri-Toxicity Posts and Hateful Comments Detection]] | BERT |
| 71 | [[2023-Trepczynski-Religion Theology and Philosophical Skills of]] | ChatGPT, Codex, Llama2, Llama2. |
| 72 | [[2023-University-Harmful Communication Detection of Toxic Language and Threats on]] | CroSloEngual BERT |
| 73 | [[2023-Varshney-Muslim-Violence Bias Persists in Debiased GPT]] | ChatGPT, GPT-3, InstructGPT |
| 74 | [[2023-Vida-Values, Ethics, Morals]] | BERT |
| 75 | [[2023-Zhang-Heterogeneous Value Alignment Evaluation for]] | GPT-4, GPT-3.5, ChatGPT, Claude, Llama, Alpaca, Vicuna |
| 76 | [[2023-Zhao-GPTBIAS A Comprehensive Framework for Evaluating]] | BLOOM, BLOOM 0, BLOOM 3, BLOOMZ, ChatGPT, GPT-3, GPT-4, L... |
| 77 | [[2024-Adelani-IrokoBench - A Benchmark for African Languages in the Age of LLMs]] | GPT-4, GPT-3.5, Gemma, Claude, Llama-3, BLOOM |
| 78 | [[2024-Adelani-Uhura A Benchmark for Evaluating Scientific]] | Alpaca, Claude, Claude Sonnet, Claude 3.5, Claude 3.5 Son... |
| 79 | [[2024-Agarwal-Ethical Reasoning Depends on Language]] | GPT-4, ChatGPT, Llama-2 |
| 80 | [[2024-Aksoy-Whose Morality Do They Speak]] | GPT-3.5, GPT-4, Llama-3, Mistral |
| 81 | [[2024-Altenburger-Examining the Role of Relationship Alignment in]] | Llama-3 |
| 82 | [[2024-Aly-Hate speech detection with ADHAR a multi-dialectal hate speech corpus]] | BERT, RoBERTa |
| 83 | [[2024-Amano-Exploring Similarity Measures and Intertextuality in]] | BERT, Word2Vec |
| 84 | [[2024-Aydin-Improving LLM Reliability with RAG in]] | ChatGPT, DeepSeek, Gemma, Llama, Mistral, Qwen |
| 85 | [[2024-Bang-Measuring Political Bias in LLMs What Is Said and How It Is Said]] | Llama-2, Vicuna, Falcon, Mistral |
| 86 | [[2024-Bean-Measuring What Matters - Construct Validity in LLM Benchmarks]] | GPT-4, GPT-4o mini |
| 87 | [[2024-Biedma-Beyond Human Norms]] | GPT-4, GPT-3.5, Llama-2, Mistral, Vicuna |
| 88 | [[2024-Bignotti-Legal Minds, Algorithmic Decisions]] | GPT-4 |
| 89 | [[2024-Cahyawijaya-High-Dimension Human Value Representation in]] | ChatGPT, Llama-2, Llama-3, Mistral, Mixtral, BLOOM |
| 90 | [[2024-Cao-The Moral Foundations Weibo Corpus]] | GPT-4, Llama-3, Qwen |
| 91 | [[2024-Caputo-Rules, Cases, and Reasoning]] | Claude |
| 92 | [[2024-Chakravarthi-Findings of the Shared Task on]] | BERT, RoBERTa |
| 93 | [[2024-Charfi-A Web-Based Hate Speech Detection System for Dialectal Arabic]] | BERT, RoBERTa |
| 94 | [[2024-Chen-EmotionQueen A Benchmark for Evaluating Empathy of Large Language]] | GPT-4, GPT-3.5, Claude, Llama-2, BLOOM, Falcon, Vicuna |
| 95 | [[2024-Chua-AI Safety in Generative AI Large Language Models]] | BERT, BLOOM, Bart, ChatGPT, GPT-4, Llama, Zephyr |
| 96 | [[2024-Das-The 'Colonial Impulse' of Natural Language Processing An Audit of]] | T5 |
| 97 | [[2024-Dawson-Evaluating Cultural Awareness of LLMs for]] | GPT-4o, GPT-4o mini, GPT-4o-mini, Gemma |
| 98 | [[2024-Dognin-Contextual Moral Value Alignment Through]] | Llama-2 |
| 99 | [[2024-Faisal-Dialectal Toxicity Detection Evaluating LLM-as-a-Judge Consistency]] | Mistral-NEMO, Phi-3, Phi-3 49, Phi-3 Mini, Phi-3-mini |
| 100 | [[2024-Fetahi-AI-Based Hate Speech Detection in Albanian Social Media New Dataset]] | mBERT, XLM-RoBERTa |
| 101 | [[2024-Fitzgerald-Some Issues in Predictive Ethics Modeling]] | RoBERTa |
| 102 | [[2024-Freire-Uncovering Latent Human Wellbeing in Language]] | GPT-3, DeBERTa, BERT |
| 103 | [[2024-Garcia-The Moral Turing Test]] | GPT-3.5 |
| 104 | [[2024-Ghahroodi-Khayyam Challenge PersianMMLU Is Your LLM Truly Wise to The Persian]] | GPT-4, GPT-3.5, Claude-3-Haiku, Aya, XVERSE-13B, XVERSE-7... |
| 105 | [[2024-Grigoreva-RuBia A Russian Language Bias Detection Dataset]] | BERT, ChatGPT, GPT-3, GPT-3.5-turbo, RoBERTa |
| 106 | [[2024-Gupta-Improving Model Evaluation using SMART Filtering]] | Qwen, Llama-3, Gemma, Phi, Mixtral |
| 107 | [[2024-Gómez-Adorno-Overview of HOMO-MEX at IberLEF 2024 Hate Speech Detection Towards]] | BERT, GPT2, GloVE, RoBERTa |
| 108 | [[2024-Hadar-Shoval-Assessing the Alignment of Large Language Models With Human Values]] | GPT-4, GPT-3.5, Claude-2, Bard |
| 109 | [[2024-Hendrycks-Introduction to AI Safety, Ethics, and Society]] | BERT, ChatGPT, GPT-4, Llama-2 |
| 110 | [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]] | ALBERT, GPT-4, GPT-4o, Llama, Llama3, Mistral-7b, BERT |
| 111 | [[2024-Huang-Collective Constitutional AI Aligning a Language Model with Public]] | Claude |
| 112 | [[2024-Isbarov-Open foundation models for Azerbaijani language]] | BERT, DeBERTa-Base, RoBERTa |
| 113 | [[2024-J. K. Lee-Detecting Bias in Large Language Models Fine-tuned KcBERT]] | KcBERT |
| 114 | [[2024-Jadhav-On Limitations of LLM as Annotator for Low Resource Languages Marathi]] | ALBERT, BERT, ChatGPT, GPT-3, GPT-4, GPT-4 Turbo, GPT-4o,... |
| 115 | [[2024-Jain-Norm Inconsistency in LLM Decision-Making]] | GPT-4, Claude |
| 116 | [[2024-Jothi Prakash-A Novel Socio-pragmatic Framework for Sentiment]] | XLM-RoBERTa |
| 117 | [[2024-Jue-MalayMMLU A Multitask Benchmark for the Low-Resource Malay Language]] | Baichuan, Baichuan-2, GPT-3, GPT-3.5, GPT-4, GPT-4o, Gemm... |
| 118 | [[2024-Kader-The Emergence of Strategic Reasoning of Large Language Models]] | GPT-4, Claude |
| 119 | [[2024-Kajiwara-A comprehensive framework for multi-modal hate speech detection in]] | BERT, RoBERTa, T5, Word2Vec |
| 120 | [[2024-Kajiwara-A curated dataset for hate speech detection on social media text - PMC]] | BERT, Word2Vec |
| 121 | [[2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata]] | BERT |
| 122 | [[2024-Keller-HOCON34k A Corpus of Hate Speech in Online Comments from German]] | BERT |
| 123 | [[2024-Khamassi-Strong and weak alignment of large language models]] | ChatGPT |
| 124 | [[2024-Khandelwal-Do Moral Judgment and Reasoning Capability of]] | GPT-4, ChatGPT, Llama-2 |
| 125 | [[2024-Khandelwal-Multilingual Defining Issues Test]] | GPT-4, ChatGPT, Llama-2 |
| 126 | [[2024-Khanduja-Telugu Language Hate Speech Detection Using]] | mBERT, DistilBERT, IndicBERT, NLLB, MuRIL, XLM-RoBERTa, I... |
| 127 | [[2024-Kishore-Evaluating Telugu Proficiency in Large Language]] | ChatGPT |
| 128 | [[2024-Koto-IndoCulture Exploring Geographically-Influenced Cultural Commonsense]] | BART, BLOOMZ, ChatGPT, GPT-3, GPT-3.5, GPT-4, Llama, Llam... |
| 129 | [[2024-Kyriacou-Artificial Moral Intelligence Aristotelian]] | Bloom, ChatGPT, GPT-4 |
| 130 | [[2024-Lazar-Frontier AI Ethics]] | ChatGPT, GPT-4 |
| 131 | [[2024-Lee-Exploring Inherent Biases in LLMs within Korean Social Context A]] | ChatGPT, GPT-4 |
| 132 | [[2024-Liang-Cross-Language Bias Examination in Large Language Models]] | GPT-4 |
| 133 | [[2024-Liu-Detecting Anti-Semitic Hate Speech Using Transformer-Based]] | BERT, DistilBERT, GloVe, Llama-2, Llama2, RoBERTa, Word2Vec |
| 134 | [[2024-Locatelli-Examining the Behavior of LLM Architectures Within the Framework of]] | GPT-3.5, GPT-4, MariTalk |
| 135 | [[2024-Luong-Realistic Evaluation of Toxicity in Large]] | ChatGPT, Llama-2, Mistral, Mixtral |
| 136 | [[2024-Lyu-Large language model LLM comparison between GPT-3 and PaLM-2 to]] | GPT-3, PaLM-2 |
| 137 | [[2024-Masood-1 Natural Language Processing for Dialects of a Language A Survey]] | BERT, GPT-4, RoBERTa, T5 |
| 138 | [[2024-Masood-Bias in Large Language Models Origin Evaluation and Mitigation]] | ALBERT, BERT, ChatGPT, GPT-4, Llama, Llama Guard |
| 139 | [[2024-McGee-How Ethical Is Utilitarian Ethics]] | ChatGPT |
| 140 | [[2024-Meadows-LocalValueBench]] | GPT-4, Claude |
| 141 | [[2024-Meijer-LLMs as mirrors of societal moral standards reflection of cultural]] | GPT-2, OPT, BLOOM |
| 142 | [[2024-Nahian-The Goofus & Gallant Story Corpus for Practical]] | GPT-4, BERT |
| 143 | [[2024-Network-Harnessing the Power of Artificial Intelligence to Vitalize]] | BERT |
| 144 | [[2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding]] | GPT-4, Claude |
| 145 | [[2024-Nwaiwu-LIEA-BERT A Linguistically Enriched Framework for]] | BERT |
| 146 | [[2024-Nyachhyon-Consolidating and Developing Benchmarking Datasets for]] | BERT, DeBERTa, DeBERTa-v3, Distilbert, GPT-4o-mini, RoBERTa |
| 147 | [[2024-Ober-Lyceum Project AI Ethics Aristotle]] | GPT-4, ChatGPT, Gemini, Llama |
| 148 | [[2024-Oliech-SwaQuAD-24]] | BERT, RoBERTa |
| 149 | [[2024-Onose-Can LLMs Help Create Grammar Automating Grammar Creation for]] | GPT-4, BERT, gpt-4o-mini |
| 150 | [[2024-Paraschiv-Offensive Text Span Detection in Romanian Comments Using Large]] | BERT, GPT-3.5, GPT-4 |
| 151 | [[2024-Paul-Towards a More Inclusive AI Progress and Perspectives in Large]] | BLOOM, Pegasus |
| 152 | [[2024-Pires-Sabiá-2 A New Generation of Portuguese Large Language Models]] | Claude 3 Sonnet, Claude 3, Claude 3 Opus, GPT-3, GPT-3.5,... |
| 153 | [[2024-Pisano-Moral High Ground]] | Flan-T5, Falcon, Llama-2 |
| 154 | [[2024-Potter-Hidden Persuaders LLMs' Political Leaning and Their Influence on]] | GPT-4, GPT-3.5, Claude, Llama-3, Llama-2, Mixtral, Alpaca... |
| 155 | [[2024-Prabhakar-Cultural Fidelity in Large-Language Models An]] | ChatGPT, GPT-3, GPT-3.5, GPT-4, GPT-4 Turbo, GPT-4-turbo,... |
| 156 | [[2024-Published in Sadhana journal-Transformer-based Pouranic Topic Classification in Indian]] | BERT, RoBERTa, DistilBERT |
| 157 | [[2024-Qamar-A Benchmark Dataset with Larger Context for]] | T5, BART |
| 158 | [[2024-Rane-Concept Alignment]] | ChatGPT |
| 159 | [[2024-Ranjan-A Comprehensive Survey of Bias in LLMs]] | BERT, GPT-2, GPT-3, GPT-4, LLaMA 2 |
| 160 | [[2024-Religions-The Use of Large Language Models]] | ChatGPT, GPT3 |
| 161 | [[2024-Ren-Safetywashing]] | Mixtral, Llama-3, Llama-2, Mistral, Falcon, Gemma, Qwen |
| 162 | [[2024-Semenova-Benchmarking Multimodal Models for Ukrainian Language Understanding]] | BERT, Claude 3.5, Claude 3.5 Sonnet, Claude Sonnet, GPT-4... |
| 163 | [[2024-Senthilkumar-Fine-Tuning Language Models for Ethical Ambiguity]] | GPT-4, Llama-3, Mistral |
| 164 | [[2024-Seror-The Moral Mind(s) of Large Language Models]] | GPT-4, Claude, Llama-3, Qwen, Mixtral, Mistral |
| 165 | [[2024-Seth-DOSA A Dataset of Social Artifacts from Different Indian Geographical]] | GPT-4, Llama-2, PaLM-2, Falcon |
| 166 | [[2024-Simpson-Parity Benchmark for Measuring Bias in]] | ALBERT, BERT, Claude, Claude 3.5, Claude 3.5 Sonnet, GPT-... |
| 167 | [[2024-Song-Multilingual Blending LLM Safety Alignment Evaluation with Language]] | ALBERT, ChatGPT, GPT-3, GPT-3.5, GPT-4, GPT-4o, GPT4-Turb... |
| 168 | [[2024-Songyuan Liu-Measuring Spiritual Values and Bias of]] | ChatGLM, ChatGLM 2, Chatglm2, CodeLlama, GPT-2, GPT-4, GP... |
| 169 | [[2024-Sorensen-A Roadmap to Pluralistic Alignment]] | Alpaca, GPT-3, GPT3, Gemma, Llama, LLaMA2, LLaMA2., gpt-3... |
| 170 | [[2024-Sorin-Ethical Alignment of LLMs in Healthcare]] | GPT-4, GPT-3.5, Llama-3, Gemma, Phi, Qwen |
| 171 | [[2024-Stenseke-Computational Complexity of Ethics]] | GPT-3 |
| 172 | [[2024-Street-LLMs achieve adult human performance on]] | GPT-3.5, GPT-4, LaMDA, PaLM, Flan-PaLM |
| 173 | [[2024-Suliman-The interconnectedness between Ubuntu principles]] | ChatGPT |
| 174 | [[2024-Tahir-Benchmarking Pre-trained Large Language Models Potential]] | BERT, BLOOM, Bloomz, ChatGPT, GPT 3, GPT 3.5, GPT 2, GPT ... |
| 175 | [[2024-Takemoto-The moral machine experiment on large language]] | GPT-3.5, GPT-4, PaLM-2, Llama-2 |
| 176 | [[2024-University-Monitoring the Evolution of Antisemitic Discourse]] | BERT |
| 177 | [[2024-Vallor-The AI Mirror]] | ChatGPT, Gemini, Llama |
| 178 | [[2024-Vasilev-CRAFT Cultural Russian-Oriented Dataset Adaptation for Focused]] | Kandinsky 3.1, Kandinsky 2.2, DALL-E 3, Midjourney, Stabl... |
| 179 | [[2024-Veitsman-Recent Advancements and Challenges of Turkic]] | BERT, GPT-4, Llama-2, RoBERTa |
| 180 | [[2024-Wang-A Comprehensive Survey of LLM Alignment Techniques]] | Alpaca, BERT, ChatGPT, Claude, Claude-3, GPT-2, GPT-3, GP... |
| 181 | [[2024-Wang-Possibilities and challenges in the moral growth of LLMs]] | GPT-2, GPT-3, ChatGPT |
| 182 | [[2024-Wasi-Exploring Bengali Religious Dialect Biases in Large Language Models]] | BERT, ChatGPT |
| 183 | [[2024-Weidinger-Holistic Safety and Responsibility Evaluations of]] | bloom |
| 184 | [[2024-Wijanarko-Monitoring Hate Speech in Indonesia An NLP-based Classification of]] | BERT, ChatGPT, GPT-4o mini, GPT-4, RoBERTa, GPT-3, GPT-3.... |
| 185 | [[2024-Yang-Benchmarking LLM Guardrails in Handling Multilingual Toxicity]] | ChatGPT, GPT-4, Llama, Llama-3, LlaMa-3.1, LlaMa-Guard, M... |
| 186 | [[2024-Yang-Large Language Models Meet Text-Centric Multimodal Sentiment Analysis]] | BERT, ChatGPT, Claude, Llama, LLaMA1, Qwen-VL |
| 187 | [[2024-Yao-CLAVE ValEval]] | GPT-4, GPT-2, Phi, Mistral, Llama-2, Alpaca |
| 188 | [[2024-Yao-Self-Alignment Improving Alignment of Cultural Values in LLMs via]] | BLOOMz, CommandR, Llama-3, Llama3, Mistral, Mistral. 6, c... |
| 189 | [[2024-Yoo-HyperCLOVA X Technical Report]] | HyperCLOVA X, GPT-4, GPT-3.5, Llama-2, Falcon, SOLAR, Pol... |
| 190 | [[2024-Yuan-Cultural Palette Pluralising Culture Alignment via Multi-agent Palette]] | Llama-3.1-8B-Instruct, Qwen-2.5-7B-Instruct, GPT-4o |
| 191 | [[2024-Zangari-A survey on moral foundation theory and pre-trained language models]] | BERT, GPT-3, GPT-3.5, GloVE, Llama, RoBERTa |
| 192 | [[2024-Zhi-Xuan-Beyond Preferences in AI Alignment]] | GPT-4, ChatGPT |
| 193 | [[2024-Zhou-Rethinking Machine Ethics Can LLMs Perform Moral Reasoning]] | Llama-2, GPT-4 |
| 194 | [[2024-team-VLegal-Bench Cognitively Grounded Benchmark for Vietnamese Legal]] | Bloom, Claude Sonnet, GPT-4, GPT-4o, GPT-4o-mini, Llama, ... |
| 195 | [[2024-Šekrst-AI Ethics by Design]] | ChatGPT, Claude, Llama, Mixtral |
| 196 | [[2025-2025-Pretrained Models Against Traditional Machine Learning]] | AraBERT |
| 197 | [[2025-A.-Operationalizing Cultural Values in Language Models A Comparative]] | GPT-4o, YandexGPT, GigaChat, Claude Sonnet, Gemini |
| 198 | [[2025-Abdaljalil-HalluVerse25]] | GPT-4, Phi, Mistral, Qwen, Gemma, Llama-3, PaLM-2 |
| 199 | [[2025-Abdelhalim-Full article Artificial intelligence tools and literary translation a]] | ChatGPT |
| 200 | [[2025-Abdullah-KurdSTS The Kurdish Semantic Textual Similarity]] | BERT |
| 201 | [[2025-Adelani-AfriMTEB and AfriE5 Benchmarking and Adapting]] | BERT, Gemma, Mistral, Mistral-7B, Qwen2, Qwen3, RoBERTa |
| 202 | [[2025-Agarwal-Fluent but Foreign - Even Regional LLMs Lack Cultural Alignment]] | GPT-4, Llama-2, Llama-3, Mistral, Gemma |
| 203 | [[2025-Aggarwal-Letta Leaderboard]] | Claude, GPT-4 |
| 204 | [[2025-Akata-Playing Repeated Games with Large Language Models]] | GPT-4, Claude, Llama-2 |
| 205 | [[2025-Al-SEADialogues A Multilingual Culturally Grounded Multi-turn]] | GPT-4, GPT-4o mini, Llama, Llama-3.1, Qwen-14B |
| 206 | [[2025-Al-SHADES A New Multilingual Benchmark for Stereotypes Bias in Large]] | BERT, BLOOM, Bloom-1b7, Bloom-7b1, BloomZ, Llama-3, Llama... |
| 207 | [[2025-Al-SHADES Towards a Multilingual Assessment of Stereotypes in Large]] | BERT, BLOOM, Bloom-1b7, Bloom-7b1, BloomZ, Llama-3, Llama... |
| 208 | [[2025-Al-Towards a Multilingual Assessment of Stereotypes in Large ...]] | BERT, BLOOM, Bloom-1b7, Bloom-7b1, BloomZ, Llama-3, Llama... |
| 209 | [[2025-Alharbi-LLMs and Islamic Fiqh A Reliability]] | GPT-4o, ALLaM |
| 210 | [[2025-Alhassoun-Saudi-Alignment Benchmark - Assessing LLMs Alignment with Saudi]] | GPT-4, GPT-3.5, Llama-3, Llama-2 |
| 211 | [[2025-Ali-Data Curation for Pluralistic Alignment]] | GPT-4o |
| 212 | [[2025-Almheiri-Cross-Cultural Transfer of Commonsense Reasoning in LLMs Evidence]] | Qwen-2.5-7B-Instruct, Gemma-2, ALLaM, SILMA-9B-Instruct |
| 213 | [[2025-Alvisi-Mapping the Italian Telegram Ecosystem Communities Toxicity and Hate]] | ChatGPT, Mixtral |
| 214 | [[2025-Aly-ArGAN Arabic Gender Ability and Nationality Dataset for ...]] | DeepSeek v3, Deepseek 0, Deepseek 79, GPT-4o, LLama 3.3, ... |
| 215 | [[2025-Aly-On Evaluating and Mitigating Gender Biases in Multilingual ...]] | BERT, RoBERTa |
| 216 | [[2025-Anonymous-BEATS]] | GPT-4, Claude, Mistral, Llama-3 |
| 217 | [[2025-Antar-Do Your Guardrails Even Guard Evaluating Moderation Guardrails for]] | ChatGPT, Claude, GPT-4, GPT-4o, Llama, Llama Guard, PaLM, T5 |
| 218 | [[2025-Arike-A Framework for Analyzing and Measuring Goal]] | Claude, GPT-4 |
| 219 | [[2025-Arnardottir-WikiQA-IS Assisted Benchmark Generation and Automated Evaluation of]] | GPT-4, GPT-4o |
| 220 | [[2025-Azmi-IndoSafety Culturally Grounded Safety for LLMs in Indonesian Languages]] | Claude, Claude 312, GPT-4o, Gemma, Gemma2, LLaMA 3.116, L... |
| 221 | [[2025-Bali-How Deep Is Representational Bias in]] | ChatGPT, GPT-4, GPT-4 Turbo, GPT4-Turbo |
| 222 | [[2025-Banar-MTEB-NL and E5-NL Embedding Benchmark and Models for Dutch]] | BERT, ChatGPT, Qwen, Qwen3, Mistral |
| 223 | [[2025-Barman-RLHF Whose Culture Whose Values]] | GPT-3, GPT-4, InstructGPT |
| 224 | [[2025-Basem-Two-Stage Quranic QA via Ensemble Retrieval]] | BERT, DeepSeek, ELECTRA |
| 225 | [[2025-Basile-NepX-Hate A Nepali Hate Speech Corpus]] | BERT, GPT-4o-mini, GPT-4, RoBERTa |
| 226 | [[2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities]] | Claude, Llama, Qwen |
| 227 | [[2025-Bhowmik-Evaluating LLMs' Multilingual Capabilities for Bengali Benchmark]] | Alpaca, DeepSeek, DeepSeek-R1, Dolly, GPT-4o-mini, Llama,... |
| 228 | [[2025-Bidgoli-FARSIQA Faithful and Advanced RAG System]] | Llama 3, Llama 4, Llama-4 |
| 229 | [[2025-Bokaei-Culture Matters in Toxic Language Detection in Persian]] | BERT, ChatGPT, GEMMA, GEMMA 2, GPT 2, GPT 3, GPT 3.5 Turb... |
| 230 | [[2025-Bravansky-Rethinking AI Cultural Alignment]] | GPT-4o, GPT-4 |
| 231 | [[2025-Brito-ToxSyn Reducing Bias in Hate Speech Detection via Synthetic Minority]] | GPT-4, BERT |
| 232 | [[2025-Brophy-Wide Reflective Equilibrium LLM Alignment]] | ChatGPT, Claude, Claude Opus, DeepSeek |
| 233 | [[2025-Bui-Large Language Models Discriminate Against Speakers of German Dialects]] | Llama-3.1-70B, Llama-3.1-8B, Llama-3-70B, Llama-3-8B, Mis... |
| 234 | [[2025-Canaverde-LegalBench.PT A Benchmark for Portuguese Law]] | ALBERT, Claude, Claude-3, Claude-3-Opus, Claude-3.5, Clau... |
| 235 | [[2025-Carballo-Evaluating Compact LLMs for Zero-Shot Iberian Language Tasks on]] | DeepSeek-R1, GPT-4, Gemma, Gemma 2, Gemma-2, Llama, Llama... |
| 236 | [[2025-Chakraborty-Structured Moral Reasoning]] | Llama-3, Llama-2, Mistral, Qwen, Phi |
| 237 | [[2025-Chakravarthi-Detecting Caste and Migration Hate Speech]] | BERT, BLOOM, BLOOM-560, RoBERTa, Word2Vec |
| 238 | [[2025-Chared-AI-driven detection of hate speech on social media a case study in]] | CamemBERT, DistilCamemBERT, DeHateBERT |
| 239 | [[2025-Chen-Leveraging large language models to assist]] | GPT-4 |
| 240 | [[2025-Chhikara-Through the Prism of Culture Evaluating LLMs' Understanding of Indian]] | GPT-4o, GPT-4o-mini, Llama-3.3-70B, Mixtral-8x7B, Gemini-... |
| 241 | [[2025-Chua-Between a Rock and a Hard Place TRIAL]] | Llama-3, Mistral |
| 242 | [[2025-Cocu-A Cross-Lingual Analysis of Bias in Large Language Models Using]] | DeepSeek, LLama-4, Llama, gemma |
| 243 | [[2025-Cognitive-Evolution of Meta’s LLaMA Models and Parameter-Efficient Fine-Tuning]] | Alpaca, ChatGPT, GPT-3, GPT-4, Llama, LLaMA 1, LLaMA 2, L... |
| 244 | [[2025-Cognitive-T-LLaMA a Tibetan large language model based on LLaMA2 Complex &]] | ALBERT, BERT, Baichuan2, ChatGPT, Llama, LLaMA 8, LLaMA.,... |
| 245 | [[2025-Dang-VMMU A Vietnamese Multitask Multimodal Understanding and Reasoning]] | Claude 4., GPT-4, Gemma, Gemma-3, Llama-4, Mistral Small,... |
| 246 | [[2025-Davies-Exploring the occupational biases and stereotypes of Chinese large]] | Baichuan, ChatGLM, ChatGLM2, ChatGPT, GPT-3, baichuan-ai,... |
| 247 | [[2025-Davies-F2Bench An Open-ended Fairness Evaluation Benchmark ...]] | ChatGPT, DeepSeek, DeepSeek 1, DeepSeek-V3, GPT-4, Gemma,... |
| 248 | [[2025-De Montis-Morality in AI]] | BERT |
| 249 | [[2025-Demidova-John vs. Ahmed Debate-Induced Bias in Multilingual LLMs]] | GPT-3, GPT-3.5, GPT-4 |
| 250 | [[2025-Dickerson-Who Gets the Kidney]] | GPT-4, Claude, Gemma, Llama-3, DeepSeek |
| 251 | [[2025-Do-ViToSA Audio-Based Toxic Spans Detection on Vietnamese Speech]] | BERT, DistilBERT |
| 252 | [[2025-Duan-AdAEM Adaptively and Automated Extensible Measurement for Value]] | GPT-4, GPT-3.5, Claude, Llama-3, Mistral, Qwen, DeepSeek |
| 253 | [[2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation]] | GPT-4 |
| 254 | [[2025-Edeh-Language Diversity Evaluating Language Usage and]] | Llama 3.3 |
| 255 | [[2025-Elkins-Syntactic Framing Fragility SFF Robustness Evaluation of LLM Ethical]] | Claude, Grok, DeepSeek, Llama-3, Phi, Gemma, Qwen |
| 256 | [[2025-Enguix-Overview of HOMO-LAT at IberLEF 2025 Human-Centric Polarity Detection]] | BERT, Falcon-7B, Gemma, Mistral-7B, ChatGPT |
| 257 | [[2025-Eriksson-Can We Trust AI Benchmarks An Interdisciplinary Review]] | Bartz, Claude 3 Opus, GPT-4, GPT4 |
| 258 | [[2025-Fanous-SycEval Evaluating LLM Sycophancy]] | ChatGPT, Claude, Llama-3 |
| 259 | [[2025-Farsi-MELAC Massive Evaluation of Large Language Models with Alignment of]] | BERT, ChatGPT, GPT-4, Gemma, GPT-4o, Llama, Llama 3.2, Ll... |
| 260 | [[2025-Farsi-PBBQ A Persian Bias Benchmark Dataset Curated with Human-AI]] | ALBERT, BERT, Claude, GPT-4o, Llama, Llama-3, LLaMA-3.1, ... |
| 261 | [[2025-Fasching-Inconsistencies in Hate Speech Detection Across]] | ChatGPT, Claude, Claude 3.5, GPT-4o, MISTRAL LARGE, Mistral |
| 262 | [[2025-Fatehkia-FanarGuard A Culturally-Aware Moderation Filter for Arabic Language]] | Gemma-2B, Gemma-4B |
| 263 | [[2025-Fenech-Borg-The Cultural Gene of Large Language Models]] | GPT-4 |
| 264 | [[2025-Feng-ERPO]] | Llama-3, Qwen, DeepSeek, GPT-4 |
| 265 | [[2025-Fillies-A novel German TikTok hate speech dataset far-right comments against]] | BERT |
| 266 | [[2025-Flek-AmericasNLI Machine translation and natural language inference]] | BERT, T5, T5-style |
| 267 | [[2025-Flores-BenchMoral]] | ChatGPT, Llama-3, DeepSeek |
| 268 | [[2025-Gabriel-AI Alignment as Fair Treatment of Claims]] | Claude, GPT-4 |
| 269 | [[2025-Gamboa-Filipino Benchmarks for Measuring Sexist and Homophobic Bias in]] | BERT, BLOOM, GPT-4, Mistral, RoBERTa, llama3 |
| 270 | [[2025-Gao-How Large Language Models Enhance Low-Resource Mongolian-Chinese]] | BERT, Gemma, Gemma2, LLaMA-3.1, LLaMA3.1, Llama, Qwen2, Q... |
| 271 | [[2025-Gao-MIST Moral Inference through Storytelling with Text and Images]] | GPT-4, Llama-3, Claude, Qwen |
| 272 | [[2025-Gerdes-Exploring LLM Chatbots as Potential Guides to]] | ChatGPT, DeepSeek |
| 273 | [[2025-Giachino-An Empirical Investigation of Gender Stereotype Representation in]] | GPT-4o-mini |
| 274 | [[2025-Goethals-One world one opinion The superstar effect in LLM responses]] | GPT-4, Claude-3-Opus, Llama-3.1-70B |
| 275 | [[2025-Gromenko-Cultural Evaluation of LLMs in Russian Catchphrases and Cultural Types]] | ChatGPT, Claude 3.5, Claude 3.5 Sonnet, GPT-3, GPT-3.5, G... |
| 276 | [[2025-Gu-Linguistically informed ChatGPT prompts to enhance Japanese-Chinese]] | ChatGPT |
| 277 | [[2025-Guey-Mapping Geopolitical Bias in 11 Large Language Models A Bilingual]] | GPT-4o, GPT-4o-mini, Claude-3.7-Sonnet, Grok-2, Gemini, M... |
| 278 | [[2025-Gupta-EnDive A Cross-Dialect Benchmark for Fairness and Performance in]] | Claude, Claude 3.5 Sonnet, DeepSeek-v3, GPT-4o, GPT-4o mi... |
| 279 | [[2025-Hamed-A Survey of Code-switched Arabic NLP]] | ChatGPT, Llama-3 |
| 280 | [[2025-Han-HKGAI-V1 Towards Regional Sovereign Large Language Model for Hong Kong]] | HKGAI-V1 |
| 281 | [[2025-Hasan-LLM-Based Multi-Task Bangla Hate Speech Detection Type Severity and]] | BERT, Claude, Claude-3.5 Sonnet, GPT-4, Llama, Llama-3.2,... |
| 282 | [[2025-Haslett-Made-in China Thinking in America U.S. Values Persist in Chinese LLMs]] | Baichuan2-13B, Claude-3.5-Sonnet, Claude-3.7-Sonnet, Clau... |
| 283 | [[2025-Havaldar-Culturally-Aware Conversations A Framework Benchmark for]] | GPT-4, Claude, Gemini |
| 284 | [[2025-Heierli-Evaluating LLM Capabilities in Low-Resource Contexts A Case Study of]] | GPT-4o, Gemini, Llama, DeepSeek |
| 285 | [[2025-Heredia-Conditioning LLMs to Generate Code-Switched Text]] | BLOOM, BERT, GPT-4o, Llama, Llama3, Llama3.3, Mistral 31.... |
| 286 | [[2025-Hew-MyCulture Exploring Malaysia's Diverse Culture under Low-Resource]] | DeepSeek, DeepSeek-V3, GPT-4o, GPT-4o mini, GPT-4, Llama,... |
| 287 | [[2025-Hilliard-Measuring AI Alignment with Human Flourishing]] | GPT-4, ChatGPT, Claude, Grok |
| 288 | [[2025-Hofman-MAPS A Multilingual Benchmark for Global Agent Performance and]] | GPT-4, GPT-4o, Qwen 2, Qwen 7B, Qwen-2, Qwen2, ChatGPT |
| 289 | [[2025-Hong-NormGenesis Multicultural Dialogue Generation Dataset]] | GPT-4, Llama-3, Qwen |
| 290 | [[2025-Hong-PrinciplismQA Towards Assessing Medical Ethics from Knowledge to]] | GPT-4, Claude, Gemma, Llama-3, Qwen, DeepSeek |
| 291 | [[2025-Hossain-Beyond Neutrality A Comprehensive Approach of Religious Bias]] | ChatGPT, GPT-2, GPT-3, GPT-3.5, GPT-4, GPT-4-Turbo, GPT-4... |
| 292 | [[2025-Hosseinbeigi-Matina A Culturally-Aligned Persian Language Model Using Multiple]] | Llama-3.1-8B |
| 293 | [[2025-Huang-Analysis of LLM Bias Chinese Propaganda & Anti-US Sentiment in]] | ChatGPT, DeepSeek, DeepSeek-R1, GPT-3, GPT-3.5, GPT-4, GP... |
| 294 | [[2025-Huang-Understanding Asian Stereotyping and Bias in LLMs Flora Huang]] | BERT, Llama, Mistral |
| 295 | [[2025-Hui-Decoding Moral Responses in AI]] | GPT-3, GPT-3.5, GPT-4, GPT-4.1, Claude-3.7-Sonnet, Grok-3... |
| 296 | [[2025-Hussain-From RAG to Agentic Validating Islamic-Medicine]] | Claude, Claude-4, GPT4, Llama-3, Mistral 7b, Mistral- 7B,... |
| 297 | [[2025-Hähnel-A Companion to Applied Philosophy of AI]] | ChatGPT, Claude, LaMDA |
| 298 | [[2025-Institute-2025 AI Safety Index]] | DeepSeek |
| 299 | [[2025-Jafarinejad-PerGOLD Identification of Offensive Language in Persian Tweets]] | BERT, RoBERTa |
| 300 | [[2025-Jamshidi-MoCoP]] | GPT-4, DeepSeek |
| 301 | [[2025-Jin-Social Bias Benchmark for Generation A Comparison of Generation and]] | Claude, Claude-3-haiku, Claude-3.5-sonnet, GPT-3, GPT-3.5... |
| 302 | [[2025-Kabir-BLUCK A Benchmark Dataset for Bengali Linguistic Understanding and]] | Claude 3.5, Claude 3.5-Sonnet, Claude-3.5, Claude-3.5-Hai... |
| 303 | [[2025-Kanepajs-LAG-MMLU Benchmarking Frontier LLM Understanding in]] | BERT, Claude 3.5, Claude 3.5 Sonnet, DeepSeek-R1, DeepSee... |
| 304 | [[2025-Kapociute-Dzikiene-Localizing AI Evaluating Open-Weight Language Models for Languages of]] | Llama-3, Llama-3.1, Llama-3.2, Gemma-2, Phi-3, GPT-3.5-Tu... |
| 305 | [[2025-Khan-Mitigating Social Bias in English and]] | BERT, GPT-3, GPT-3.5, GPT-3.5-turbo, GPT-4, GPT-4o-mini, ... |
| 306 | [[2025-Kharchenko-How Well Do LLMs Represent Values Across Cultures]] | ChatGPT, Command-R, GPT-4, GPT-4o, GPT4, GPT4o, Gemma, LL... |
| 307 | [[2025-Kilov-Discerning What Matters]] | Llama-3, GPT-4, DeepSeek, Claude |
| 308 | [[2025-Koo-Evaluating Large Language Models on Understanding Korean Indirect]] | GPT-3.5-Turbo, GPT-4-Turbo, Claude-3-Haiku, Claude-3-Sonn... |
| 309 | [[2025-Kostiuk-The Velnias is in the Details Evaluating LLM Judgment on Latvian and]] | Qwen-2.5-72B, Qwen-2.5-7B, Llama-3.1-70B, Llama-3.1-8B, E... |
| 310 | [[2025-Kranti-MATA mata Mindful Assessment of the]] | Claude, Claude Sonnet, Claude-Sonnet, GPT-4, GPT-4o, Gemm... |
| 311 | [[2025-Krishna-D-REX A Benchmark for Detecting Deceptive Reasoning in Large Language]] | Claude, DeepSeek, Qwen, Grok |
| 312 | [[2025-Krzanowski-Phronesis for AI Systems]] | ChatGPT, GPT-4 |
| 313 | [[2025-Kumar-TeSent A Benchmark Dataset for Fairness-aware]] | BERT, RoBERTa |
| 314 | [[2025-LLMs-A Leaderboard to Benchmark Ethical Biases in LLMs]] | ChatGPT, GPT4, Llama-2 |
| 315 | [[2025-LaCroix-Metaethical perspectives on ‘benchmarking’ AI]] | BERT, GPT-3 |
| 316 | [[2025-Lan-McBE A Multi-task Chinese Bias Evaluation Benchmark for Large]] | ALBERT, Baichuan 2, Baichuan2, ChatGLM, DeepSeek, DeepSee... |
| 317 | [[2025-Lan-McBE]] | Qwen, Llama-2, Mistral, ChatGPT |
| 318 | [[2025-Lee-When Prompting Fails to Sway]] | Claude, GPT-4, GPT-3.5, Llama-3 |
| 319 | [[2025-Li-AI Development and Innovation A Comparison of Large Language Models]] | GPT-4-Turbo, Ernie-Bot-4 |
| 320 | [[2025-Li-Analyzing Cognitive Differences Among Large]] | GPT-4o, Qwen, Llama-3, Gemma, DeepSeek, Phi |
| 321 | [[2025-Li-Untangling Input Language from Reasoning Language A Diagnostic]] | ALBERT, Claude, Claude 1.00, Claude 11.5, Claude 42.7, Cl... |
| 322 | [[2025-Lindstrom-Helpful Harmless Honest Sociotechnical Limits]] | ChatGPT, Claude, Llama |
| 323 | [[2025-Liu-Cross-cultural value alignment frameworks]] | GPT-4o, GPT-3.5, Claude, Llama-3, Llama-2, Mistral, Mixtr... |
| 324 | [[2025-Liu-Cultural Learning-Based Culture Adaptation of Language Models]] | Llama-3.1-8B, Llama-3.1-70B, Llama-3.2-3B, Llama-3.2-1B, ... |
| 325 | [[2025-Liu-Diagnosing Moral Reasoning Acquisition in]] | Mistral, Llama-3, BERT |
| 326 | [[2025-Liu-On the Convergence of Moral Self-Correction in LLMs]] | Mistral, GPT-4 |
| 327 | [[2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences]] | GPT-4 |
| 328 | [[2025-Maatta-Language Models for Code-switch Detection of te reo Māori and English]] | BERT |
| 329 | [[2025-Maatta-LinCE Benchmark]] | BERT, ELMo |
| 330 | [[2025-Machlovi-Towards Safer AI Moderation Evaluating LLM Moderators Through a]] | Alpaca, BERT, Gemma, Gemma2, Llama, Llama Guard, LlamaGua... |
| 331 | [[2025-Maheshwari-ParamBench A Graduate-Level Benchmark for Evaluating]] | Claude, GPT-4, Gemma, Gemma-3, Gemma2, Gemma3, Llama, Lla... |
| 332 | [[2025-Masood-A survey of multilingual large language models - PMC]] | BLOOM, BLOOM-1, ChatGPT, GPT-3, GPT-3.5, GPT-3.5-turbo, G... |
| 333 | [[2025-Masood-Beyond MCQ An Open-Ended Arabic Cultural QA Benchmark with Dialect]] | Falcon3, GPT-4, Palm, Qwen, Qwen2, Qwen2.5, BERT |
| 334 | [[2025-Masood-From Words to Proverbs Evaluating LLMs’ Linguistic and Cultural]] | ChatGPT, GPT-4, GPT-4o, Llama, Llama-3, Mistral, Mistral ... |
| 335 | [[2025-Mazeika-Utility Engineering]] | GPT-4, GPT-3.5, Llama-2, Llama-3, Gemma, Qwen |
| 336 | [[2025-Mc-Irish-BLiMP A Linguistic Benchmark for Evaluating Human and Language]] | Gemma, Gemma 3, Llama 2, Llama-2, Llama-4, Mistral, Mistr... |
| 337 | [[2025-Mekky-HALF Harm-Aware LLM Fairness Evaluation Aligned with Deployment]] | Claude, Claude 4, Claude 4., Claude4, DeepSeek, DeepSeek ... |
| 338 | [[2025-Metinov-KyrgyzBERT A Compact Efficient Language Model for Kyrgyz NLP]] | BERT, RoBERTa |
| 339 | [[2025-Mikhailov-NorEval A Norwegian Language Understanding and Generation Evaluation]] | Claude 3.7 Sonnet, GPT-4o, Llama, Llama-3, Llama-3.3, Lla... |
| 340 | [[2025-Mining)-Enhancing social media hate speech detection in low-resource]] | XLM-RoBERTa |
| 341 | [[2025-Mohammadi-Do Large Language Models Understand Morality Across Cultures]] | GPT-2-Medium; GPT-2-Large; OPT-125M; OPT-350M; BLOOM-560M... |
| 342 | [[2025-Mohammadi-EvalMORAAL]] | GPT-4, GPT-3.5, Claude, PaLM-2, Llama-3, Qwen, Mistral, D... |
| 343 | [[2025-Mohammadi-Identifying Gender Stereotypes and Biases in Automated Translation]] | GloVe, Word2Vec |
| 344 | [[2025-Mohammed-Aftina]] | Gemma |
| 345 | [[2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human]] | GPT-4, Mistral, Llama-3, Qwen |
| 346 | [[2025-Mukherjee-DECASTE Unveiling Caste Stereotypes in Large]] | ChatGPT, GPT-3, GPT-3.5, GPT-3.5-turbo, GPT-4, GPT-4o, Ll... |
| 347 | [[2025-Mushtaq-WorldView-Bench]] | GPT-4, Claude, Llama-3, Mistral, DeepSeek |
| 348 | [[2025-Nadeem-Ethical Decision-Making in Humans and Large]] | GPT-4, DeepSeek |
| 349 | [[2025-Naous-Camellia Benchmarking Cultural Biases in LLMs for Asian Languages]] | Llama-3.3-70B; Qwen-2.5-72B; Aya-Expanse-32B; Gemma-3-27B |
| 350 | [[2025-Narnaware-SB-Bench]] | GPT-4, Llama-3, Gemma, Qwen, Phi |
| 351 | [[2025-Narula-A comprehensive review on detection of hate speech for multi-lingual]] | BERT, GPT-3, GloVe, RoBERTa, Word2Vec, XLNet, distilBERT |
| 352 | [[2025-Nath-Few-shot and zero-shot Assamese hate speech detection a comparative]] | BERT, GPT-3, GPT-3.5, GPT-3.5-Turbo, GPT-4, Mistral- 7B, ... |
| 353 | [[2025-Nemkova-Cross-Lingual Stability and Bias in Instruction-Tuned]] | ALBERT, Claude, Claude Sonnet, Claude-Sonnet, DeepSeek, D... |
| 354 | [[2025-Neuman-Analyzing the Ethical Logic of Six Large Language Models]] | GPT-4, Llama, Claude, Mistral |
| 355 | [[2025-Neuman-Auditing the Ethical Logic of Generative AI Models]] | GPT-4, Llama, Claude, Mistral, DeepSeek |
| 356 | [[2025-Neuman-PRIME Framework Convergent Ethics]] | GPT-4, Llama, Claude, Mistral |
| 357 | [[2025-Ngui-SEA-SafeguardBench Evaluating AI Safety in SEA]] | GPT-4, GPT-4o, Gemma, Gemma-2, Gemma-3, Gemma3, LLaMA-3.1... |
| 358 | [[2025-Ni-A Survey on Large Language Model Benchmarks]] | ALBERT, BART, BERT, Bloom, ChatGPT, Claude, DeepSeek-V3, ... |
| 359 | [[2025-Nikandrou-CROPE Evaluating In-Context Adaptation of Vision and Language Models]] | LLaVA-1.5; MOLMO; LLaVA-NeXT; Phi-3-Vision; Idefics2; Man... |
| 360 | [[2025-Niklaus-SwiLTra-Bench The Swiss Legal Translation Benchmark]] | Claude-3.5-Sonnet; Claude-3.5-Haiku; GPT-4o; GPT-4o-Mini;... |
| 361 | [[2025-Nuha-Exploring NLP Benchmarks in an Extremely Low-Resource Setting]] | BERT, DistilBERT, GPT-3, GPT-3.5-turbo, GPT-4, GPT-4o, Ll... |
| 362 | [[2025-Oh-Robustness of Large Language Models in Moral Judgements]] | GPT-3.5 |
| 363 | [[2025-Ohlhorst-Virtues for AI]] | ChatGPT |
| 364 | [[2025-Okamoto-AI-based medical ethics education]] | ChatGPT |
| 365 | [[2025-Open-A Comprehensive Dataset for Enhancing Safety in LLM- ...]] | Claude 3 Haiku, Claude 3 Opus, Claude 3 Sonnet, GPT-3, GP... |
| 366 | [[2025-Open-Safety and Security Analysis of Large Language Models Risk Profile]] | BERT, ChatGPT, Claude, Claude 4, Claude 4 Opus, Claude Op... |
| 367 | [[2025-Osmani-Investigating Retrieval-Augmented Generation in Quranic Studies]] | GPT-4, Gemma, Gemma 2, Gemma2, Llama, Llama 3, Llama 3.1,... |
| 368 | [[2025-Palta-Speaking the Right Language]] | GPT-4 |
| 369 | [[2025-Pan-Banzhida Advancing Large Language Models for Tibetan with Curated]] | Qwen2.5-7B, Qwen3-8B, Llama-3.1-8B, DeepSeek-R1-Distill-L... |
| 370 | [[2025-Park-Deontological Keyword Bias]] | GPT-4, Llama-3, Gemma, Qwen |
| 371 | [[2025-Piot-Bridging Gaps in Hate Speech Detection Meta-Collections and]] | BERT, Gemma, Llama, Llama 3.1, Mistral 7B, RoBERTa, llama 3 |
| 372 | [[2025-Poole-Dayan-OvertonScore Benchmarking Overton Pluralism in LLMs]] | GPT-4, Gemma, DeepSeek, Llama-3, Claude |
| 373 | [[2025-Pramodya-SinhalaMMLU A Comprehensive Benchmark for Evaluating Multitask]] | CLAUDE 3.5 SONNET, CLAUDE-3, CLAUDE-3 HAIKU, CLAUDE-3-HAI... |
| 374 | [[2025-Pranav-Rice-VL Evaluating Vision-Language Models for Cultural Understanding]] | Claude, Claude-3, Claude-3-Opus, GPT-4, GPT-4o, LLaMA 3.2... |
| 375 | [[2025-Pranida-Culturally-Nuanced Story Generation for Reasoning in Low-Resource]] | BERT, Claude, Claude-3 Opus, GPT-4, GPT-4o, Gemma 2, Gemm... |
| 376 | [[2025-Prasannan-Counter-Speech Generation for Homophobic and Transphobic]] | ChatGPT, GPT-2, GPT-3, GPT-4, GPT-4o |
| 377 | [[2025-Pretrained-Evaluating Uighur literary translation A comparative study of ChatGPT]] | BERT, ChatGPT, DeepSeek, GPT-4o, Llama |
| 378 | [[2025-Pudasaini-NepaliGPT A Generative Language Model for]] | GPT-2 |
| 379 | [[2025-Qadir-Can LLMs Write Faithfully An Agent-Based]] | BERT, ChatGPT, Claude, GPT-4, GPT-4o |
| 380 | [[2025-Qi-A Cross-Cultural Comparison of LLM-based Public Opinion Simulation]] | DeepSeek-R1, DeepSeek-V3, Qwen2.5-72B, GPT-4o, Llama-3.3-70B |
| 381 | [[2025-Qiu-Multimodal Cultural Safety Evaluation Framework and Alignment]] | GPT-4o, Gemini-2.5-Pro, Gemini-2.5-Flash, o1, o4-mini, In... |
| 382 | [[2025-Raihan-A Multilingual Benchmark to Evaluate Large Language]] | BERT, Claude, Claude3.5, DeepSeek-Coder, GPT-3, GPT-3.5, ... |
| 383 | [[2025-Rashed-Advancing NLP Equity A Secondary Benchmark Evaluation of Multilingual]] | BERT, RoBERTa |
| 384 | [[2025-Research-IndQA An Indic QA Benchmark for]] | Llama, llama 2, Llama-2, llama2.70, llama2.70. chat, mixt... |
| 385 | [[2025-Rodemann-A Statistical Case Against Empirical Human-AI]] | GPT2 |
| 386 | [[2025-Rosenbaum-MTQE.en-he Machine Translation Quality Estimation for English-Hebrew]] | ChatGPT, Claude |
| 387 | [[2025-Rozen-Do LLMs Have Consistent Values]] | GPT-4, Llama-3, Gemma |
| 388 | [[2025-Russo-The Pluralistic Moral Gap]] | GPT-4, ChatGPT, Claude, Mistral, Llama-3, Qwen |
| 389 | [[2025-Rystrøm-Multilingual Multicultural Evaluating Gaps Between Multilingual]] | GPT-3, GPT-4, Gemma, Llama, gpt-3.5-turbo |
| 390 | [[2025-SOCIETY-How Much of a Pluralist is]] | ChatGPT, Claude, Claude 3.5, Claude 3.5 Sonnet, DeepSeek |
| 391 | [[2025-Sah-FairEval Evaluating Fairness in LLM-Based ...]] | BERT, ChatGPT, Claude, DeepSeek, GPT-3, GPT-3.5, GPT-4o, ... |
| 392 | [[2025-Salles-HateBRXplain A Benchmark Dataset with Human-Annotated Rationales for]] | mBERT, BERTimbau, DistilBERTimbau, PTT5 |
| 393 | [[2025-Salve-Bilingual Code-Switching Using XLM-RoBERTa]] | XLM-RoBERTa |
| 394 | [[2025-Sameer-Insights into Moral Reasoning of AI]] | ChatGPT, GPT-4 |
| 395 | [[2025-Satheesh-Dutch CrowS-Pairs Adapting a Challenge Dataset for Measuring Social]] | BERTje, RobBERT, mBERT, Mistral-7B, BERT, RoBERTa, FlauBE... |
| 396 | [[2025-Sefat-BengaliFig A Low-Resource Challenge for Figurative and Culturally]] | Claude, Claude Opus, Claude Sonnet, Claude- Sonnet, Claud... |
| 397 | [[2025-Sehar-Benchmarking Whisper for Low-Resource Speech Recognition An N-Shot]] | Whisper |
| 398 | [[2025-Sel-Backtracking for Safety]] | Gemma, Llama-3 |
| 399 | [[2025-Sermsri-Debiasing Large Language Models in Thai]] | ChatGPT, GPT-3, GPT-3.5, GPT-4, Llama, Llama-3 |
| 400 | [[2025-Shah-LLM Rationalis Measuring Bargaining Capabilities of AI Negotiators]] | GPT-4, ChatGPT |
| 401 | [[2025-Shan-SGToxicGuard Toxicity Red-Teaming Benchmarking LLM Safety]] | BERT, GPT-4, GPT-4o, GPT-4o mini, GPT-4o-mini, Llama, LLa... |
| 402 | [[2025-Sheth-Beyond Monolingual Assumptions A Survey of Code-Switched NLP in the]] | BERT, ChatGPT, GPT-2, GPT-4, GPT-4o, GloVe, Llama, RoBERT... |
| 403 | [[2025-Shi-A Systematic Study of Position Bias in LLM-as-a-Judge]] | Claude, Claude-3, Claude-3-Haiku, Claude-3-Opus, Claude-3... |
| 404 | [[2025-Simões-IberoBench A Benchmark for LLM Evaluation in Iberian Languages]] | BERT, BLOOM, BLOOM-1, BLOOM-7, Falcon-7B, Gemma, Llama, L... |
| 405 | [[2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J.]] | ChatGPT, DeepSeek, GPT-4 |
| 406 | [[2025-Snoswell-Beyond Verdicts LLM Moral Competence]] | ChatGPT, DeepSeek, GPT-4 |
| 407 | [[2025-Society-Generating Hate Anti-Jewish and Anti-Israel Bias in Leading Large]] | GPT, Claude, Gemini, Llama |
| 408 | [[2025-Solidjonov-Investigating linguistic errors in large language]] | GPT-5, Gemini-2.0-Pro, Llama-4 |
| 409 | [[2025-Song-Evaluation of Social Bias Classification Performance of LLMs Using]] | BERT, GPT-3, GPT-3.5, GPT-3.5 Turbo, GPT-4, GPT-4o |
| 410 | [[2025-Sorensen-Value Profiles for Encoding Human Variation]] | Gemma |
| 411 | [[2025-Su-Understanding How Value Neurons Shape the]] | Llama-3, Qwen, Gemma |
| 412 | [[2025-Suh-SENSE-7 Taxonomy and Dataset for Measuring User Perceptions of]] | GPT-4, GPT-3.5, Llama-2 |
| 413 | [[2025-Sukiennik-An Evaluation of Cultural Value Alignment in LLM]] | GPT-3.5, GPT-4, Llama-3, DeepSeek, Qwen |
| 414 | [[2025-Sun-Evaluating ChatGPT's Performance in Creative Text ...]] | ChatGPT, GPT-3, GPT-3.5, GPT-4 |
| 415 | [[2025-Sun-Evaluating the Translation Accuracy of ChatGPT and DeepL Through the]] | ChatGPT |
| 416 | [[2025-Sun-Full article ChatGPT translation vs. human translation an examination]] | ChatGPT |
| 417 | [[2025-Talat-On the Challenges of Bias Evaluation Under Multilingual ...]] | BERT |
| 418 | [[2025-Tereshchenko-A Comparative Analysis of Ethical and Safety Gaps]] | GPT-4, GPT-3.5, DeepSeek |
| 419 | [[2025-Terziyan-Towards ethical evolution]] | GPT-4, Gemini |
| 420 | [[2025-Tewabe-The State of Large Language Models for African Languages Progress and]] | BART, BERT, BLOOM, T5 |
| 421 | [[2025-Togmanov-KazMMLU Evaluating Language Models on Kazakh]] | ALBERT, BLOOM, BLOOMZ, DeepSeek, DeepSeek V3, DeepSeek-AI... |
| 422 | [[2025-Tomar-BharatBBQ A Multilingual Bias Benchmark for]] | BERT, Bloomz, GPT-2, Gemma, Gemma-2, Llama, Llama-3.1, Phi-3 |
| 423 | [[2025-Trepczynski-AI as a Rational Theologian A]] | Bloom, ChatGPT, Codex, GPT-3, GPT-3.5, GPT-4, GPT-4o, Lla... |
| 424 | [[2025-Tsvetkov-Democracy-in-Silico Institutional Design as Alignment]] | GPT-4, DeepSeek |
| 425 | [[2025-Umer-Sacred or Secular Religious Bias in]] | ChatGPT |
| 426 | [[2025-Unknown-IndQA A Culture-Aware Benchmark for Indian Languages]] | GPT-5 |
| 427 | [[2025-Unknown-Is ChatGPT A Good Translator A Preliminary Study]] | ChatGPT |
| 428 | [[2025-Unknown-Sentiment analysis in multilingual context Comparative analysis of]] | BERT, word2vec |
| 429 | [[2025-Unknown-The Need for Robust and Inclusive Benchmarks in Evaluating LLMs on]] | BERT, BLOOM, ChatGPT, CommandR, GPT-3, GPT-3.5, GPT-3.5 T... |
| 430 | [[2025-Usmana-A Large Language Model-Based Approach for Multilingual Hate Speech]] | ALBERT, BERT, DeepSeek 67B, ELECTRA, GPT 3, GPT 3.5 Turbo... |
| 431 | [[2025-Varsha-From Phonemes to Meaning Evaluating Large]] | ChatGPT, Claude, Claude Sonnet, Claude., DeepSeek V3, Dee... |
| 432 | [[2025-Vo-CURE Cultural Understanding and Reasoning Evaluation - A Framework]] | GPT-4o, GPT-4.1, Claude-Sonnet-3.7, Claude-Sonnet-4, Clau... |
| 433 | [[2025-Wang-Diverse Human Value Alignment for LLMs via Ethical Reasoning]] | GPT-4, Llama-3, DeepSeek, Qwen |
| 434 | [[2025-Wang-Large and Small models for collaborative cross-lingual data]] | BERT, ChatGPT, GPT-4o |
| 435 | [[2025-Wang-Measuring Desired Group Discrimination in LLMs]] | GPT-4, Claude, Llama-3, Mistral, Gemma |
| 436 | [[2025-Wang-Multimodal Understanding of Human Values in Videos]] | Mistral, RoBERTa, DeBERTa |
| 437 | [[2025-Weber-Digital Guardians Can GPT-4 Perspective API and Moderation API]] | GPT-4o |
| 438 | [[2025-Wen-Yi-Do Chinese models speak Chinese languages]] | Qwen2.5, Yi-1.5, DeepSeek-R1, InternLM3, Baichuan2, Llama... |
| 439 | [[2025-Winata-The Decades Progress on Code-Switching Research in NLP]] | ALBERT, BERT |
| 440 | [[2025-Wu-Chain-of-Ethics Defense Framework Wu et al.]] | GPT-4, GPT-4o, Claude, DeepSeek, Qwen |
| 441 | [[2025-Wu-The Bitter Lesson Learned from 2000+ Multilingual Benchmarks]] | DeepSeek-AI, GPT-4, Gemma, Qwen, Qwen1.5, Qwen2.5, ChatGP... |
| 442 | [[2025-Xia-Evaluating Modern Large Language Models on Low-Resource and]] | ChatGPT, Claude, Claude 3.5, Claude 2., Claude 3.5 Sonnet... |
| 443 | [[2025-Xie-Enhancing Multilingual Language Models for Code-Switched Input Data]] | BERT, RoBERTa |
| 444 | [[2025-Xie-SwitchLingua The First Large-Scale Multilingual and Multi-Ethnic]] | GPT-4o, GPT-4, Qwen2 |
| 445 | [[2025-Xu-AncientBench Towards Comprehensive Evaluation on Excavated]] | Baichuan2, Llama-3, Llama3, Qwen, Qwen-14B, Qwen-7B, Qwen... |
| 446 | [[2025-Xu-Nlp Fairness ConceptNet blog]] | GPT-2 |
| 447 | [[2025-Xuan-LaoBench A Large-Scale Multidimensional Lao Benchmark]] | Claude, Claude-Opus, Claude-Sonnet, DeepSeek-V3, Qwen-fam... |
| 448 | [[2025-Xuan-Uncovering Cross-Linguistic Disparities in LLMs using]] | GPT-4, Gemma, Gemma-2 |
| 449 | [[2025-Yanaka-Gender Bias in Natural Language Processing and Computer Vision A]] | ALBERT, BARTL, BERT, Bart, ELMo, GPT-2, GloVe, RoBERTa, X... |
| 450 | [[2025-Yanaka-Intersectional Bias in Japanese Large Language Models from a]] | GPT-4o, Swallow-8B, Swallow-70B |
| 451 | [[2025-Yang-CodeMixBench Evaluating Large Language Models on Code Generation with]] | BERT, CodeLLaMA, Codex, DeepSeek, DeepSeek-Coder, DeepSee... |
| 452 | [[2025-Yao-CUGE A Chinese Language Understanding and Generation Evaluation]] | BERT |
| 453 | [[2025-Yoo-Adaptive Ensemble Techniques Leveraging BERT-based Models for]] | BART, BERT, DistilBERT, RoBERTa |
| 454 | [[2025-Yoo-Moral Judgment of LLM Using Korean Datasets and Eastern Ethical]] | GPT-4, GPT-3.5 |
| 455 | [[2025-Yu-A Structured Framework for Evaluating and Enhancing Interpretive]] | Claude, LLaMA-4, Llama, Llama-3.1, Qwen, Qwen-2.5, Qwen-VL |
| 456 | [[2025-Yu-Sentiment analysis of classical Chinese literature An unsupervised]] | BERT, ChatGLM-6B, ChatGPT, DeepSeek R1, LLaMA 2 |
| 457 | [[2025-Zahid-Evaluation of Hate Speech Detection Using Large Language Models and]] | CodeLlama, DeepSeek, DeepSeekCoder, GPT 4, GPT-3, GPT-3.5... |
| 458 | [[2025-Zaki-Benchmarking the Legal Reasoning of LLMs]] | Falcon3, GPT-4o, Llama 4, Llama4, Llama |
| 459 | [[2025-Zgliczynski-Cuber-AI Ethical Resonance Hypothesis]] | GPT-4 |
| 460 | [[2025-Zhang-Beyond Single-Sentence Prompts Upgrading Value Alignment Benchmarks]] | GPT-3.5, GPT-4, ChatGLM-6B, ChatGLM-4, Claude 3.5, Baichu... |
| 461 | [[2025-Zhang-Cognitive Bias in Generative AI Influences]] | ChatGPT, GPT-4 |
| 462 | [[2025-Zhang-MedHallTune]] | GPT-4, Qwen, Vicuna, Llama-2, Flan-T5 |
| 463 | [[2025-Zhang-PoliCon]] | GPT-4, Qwen, Llama-3, DeepSeek |
| 464 | [[2025-Zhang-Safety Evaluation of DeepSeek Models in Chinese Contexts]] | DeepSeek-R1, DeepSeek-V3, GLM-4-Plus, Doubao-pro-256k, Qw... |
| 465 | [[2025-Zheng-Evaluating Code-Switching Translation with Large ...]] | BLOOMZ, ChatGPT, GPT-3, GPT-3.5, GPT-4, Llama, Llama-2, P... |
| 466 | [[2025-Zhou-Bias Beyond English Evaluating Social Bias and Debiasing Methods in a]] | BERT, Gemma, Gemma 3, Llama, LLaMA 3, LLaMA 3., Qwen, Qwe... |
| 467 | [[2025-Zhu-EAVIT]] | GPT-4, Llama-2, BERT |
| 468 | [[2025-Zhu-Steering Risk Preferences in Large Language]] | Gemma |
| 469 | [[2025-Zhuang-Enhancing Cross-Lingual Transfer through Reversible Transliteration A]] | Llama2, Qwen2, Qwen2.5, Llama |
| 470 | [[2025-Zubitski-KazBench-KK A Cultural-Knowledge Benchmark for Kazakh]] | DeepSeek, Gemma-3, LLama-3.1, Llama, Llama-3, Llama-3.3, ... |
| 471 | [[2025-approach-A Language model-based approach to sentiment classification of]] | BERT |
| 472 | [[2025-collaboration-Improving Methodologies for LLM Evaluations Across Global Languages]] | GPT4o, Gemma 2, Llama, Mistral Large |
| 473 | [[2025-community-Setting Standards in Turkish NLP TR-MMLU]] | BERT, Claude, ELECTRA, GPT-4, Gemma, Llama, claude-3.5, c... |
| 474 | [[2025-funded-Analysis of Indic Language Capabilities in]] | BERT, BLOOM, BLOOMZ, ChatGPT, Claude, Claude 3.5 Sonnet, ... |
| 475 | [[2025-search-DweshVaani An LLM for Detecting Religious]] | Gemma-2, Llama, GPT-4o, Sarvam, Indic-Gemma, Airavata |
| 476 | [[2025-team-Incorporating Diverse Perspectives in Cultural Alignment]] | ChatGPT, Mistral-7B |
| 477 | [[2025-team-ViMUL A Culturally-diverse Multilingual Multimodal Video]] | ALBERT, ChatGPT, DeepSeek-R1, GPT-4, GPT-4o, GPT-4o-mini,... |
| 478 | [[2026-Ali-UrduLM A Resource-Efficient Monolingual Urdu Language]] | GPT-3, GPT-4, Gemma, Gemma 2, GloVe, Llama, LLaMA 3.2, Ll... |
| 479 | [[2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit]] | BERT, GPT-3, GPT-3.5, GPT-4, GPT-4o, Mistral, Mistral Med... |
| 480 | [[2026-Elkins-Negation Sensitivity Index NSI]] | GPT-4, Claude, Grok, DeepSeek, Qwen, Llama, Gemma, Phi |
| 481 | [[2026-Gupta-Language Caste and Context Demographic Disparities in AI-Generated]] | GPT-4o, GPT-4o-mini, Qwen2.5-32B-Instruct, GPT-OSS-20B |
| 482 | [[2026-Hu-The Straight and Narrow Do LLMs Possess an Internal Moral Path]] | Claude-3.5, Claude-3.5-Sonnet, Llama-3, Llama-3.1, claude-3 |
| 483 | [[2026-Huang-Knowing But Not Doing Convergent Morality and Divergent Action in]] | GPT-4, Claude, Grok, Llama, Qwen, DeepSeek |
| 484 | [[2026-Kabir-XCR-Bench A Multi-Task Benchmark for Evaluating Cultural Reasoning in]] | BERT, Claude, Claude 3.7, Claude-3.7, Claude-3.7-Sonnet, ... |
| 485 | [[2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks]] | GPT-4 |
| 486 | [[2026-Kashyap-MisAlign-Profile Can Large Language Models Make Everyone Happy]] | H3FUSION, TRINITYX, Phi-3-14B, DeepSeek-7B, Gemma-2-9B-it... |
| 487 | [[2026-Kim-VALUEFLOW Toward Pluralistic and Steerable Value-based Alignment in]] | GPT-4, Claude, Grok, Qwen, Mistral, Phi, Gemma |
| 488 | [[2026-Klakow-AmharicStoryQA A Multicultural Story Question Answering]] | Gemma, Gemma 3, Gemma-3, GPT-4, Llama, Llama 3.1, Llama 3... |
| 489 | [[2026-Ko-Bilingual Bias in Large Language Models A Taiwan Sovereignty]] | GPT-5.2, GPT-4o, GPT-4o Mini, Claude Opus 4.5, Claude Son... |
| 490 | [[2026-Kolt-Legal Alignment for Safe and Ethical AI]] | GPT-4, Llama, Llama Guard |
| 491 | [[2026-Liu-JMedEthicBench]] | GPT-4, Claude, DeepSeek, Qwen, Llama-3, Grok |
| 492 | [[2026-Liu-The performances of the Chinese and U.S. Large Language Models on the]] | GPT-5.1, Claude Sonnet 4.5, Gemini 2.5 Pro, Grok 4, DeepS... |
| 493 | [[2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs]] | GPT-4, Claude, DeepSeek, Qwen, Llama-3 |
| 494 | [[2026-Madhusudan-Common to Whom Regional Cultural Commonsense]] | Claude, Claude Sonnet, DeepSeek, DeepSeek V3, DeepSeek-AI... |
| 495 | [[2026-Nadeem-Bias Beyond Borders]] | Mistral, DeepSeek |
| 496 | [[2026-Nadies-TF3-RO Training Compact Romanian Language Models on Synthetic Moral]] | ALBERT, BERT, DeepSeek, GPT-4, Gemma 2, Llama, Llama-3 |
| 497 | [[2026-Panda-IndRegBias A Dataset for Studying Indian]] | BERT, DeepSeek, DeepSeek-R1, GPT-4o, Gemma, Gemma-1.1, GP... |
| 498 | [[2026-Permadi-No Shortcuts to Culture Indonesian Multi-hop Question Answering for]] | Claude, Claude 3.7 sonnet, Claude-3.7, Claude-3.7-Sonnet,... |
| 499 | [[2026-Reaj-Cross-Lingual Probing and Community-Grounded Analysis of Gender Bias]] | BERT, ChatGPT, GPT-3, GPT-3.5-Turbo |
| 500 | [[2026-Seo-Toward Culturally Aligned LLMs through Ontology-Guided Multi-Agent]] | GPT-4o-mini, Gemini 2.5 Flash Lite, Qwen 2.5, EXAONE 3.5 |
| 501 | [[2026-Smirnov-The Language You Ask In Language-Conditioned Ideological Divergence]] | ChatGPT, Claude |
| 502 | [[2026-Tagarelli-Culturally Grounded Personas in Large Language Models]] | GPT-OSS-20B |
| 503 | [[2026-[[Unknown]]-UrduBench An Urdu Reasoning Benchmark using]] | Barth, ChatGPT, DeepSeek, DeepSeek-AI, DeepSeek-R1, Falco... |

</details>

### 4.2 Papers with Data URLs but No LLM Models Identified

**121 papers** have public data URLs but no LLM model assessment.

<details>
<summary>Click to expand (121 papers)</summary>

| # | Paper | Data URL |
|--:|-------|----------|
| 1 | [[0000-collections-JainGPT AI-Powered Chatbot for Jain Literature]] | https://jainknowledge.com / https://jaingpt.org/ |
| 2 | [[0000-project-Vedanta Datasets]] | https://github.com/atmabodha/Vedanta_Datasets |
| 3 | [[0000-projects-BaniDB Shabad OS Digital Gurbani Database]] | https://github.com/KhalisFoundation/banidb-api / https://github.com... |
| 4 | [[2010-Project-GurbaniDB]] | https://github.com/sikher/gurbanidb |
| 5 | [[2016-Fonseca-ASSIN Avaliação de Similaridade Semântica e INferência textual]] | https://huggingface.co/datasets/nilc-nlp/assin2 |
| 6 | [[2016-Purzycki-Cross-cultural dataset for the evolution of]] | https://doi.org/10.7910/DVN/ERKCLS |
| 7 | [[2018-Amram-Representations and Architectures in Neural Sentiment Analysis for]] | https://github.com/omilab/Neural-Sentiment-Analyzer-for-Modern-Hebrew |
| 8 | [[2018-Awad-The Moral Machine experiment]] | https://goo.gl/JXRrBP |
| 9 | [[2018-Behzadan-TrolleyMod v1.0]] | https://github.com/zminton/TrolleyMod/wiki |
| 10 | [[2018-Bohra-Hindi-English Code-Mixed Social Media Text for]] | https://github.com/deepanshu1995/HateSpeech-Hindi-English-Code-Mixe... |
| 11 | [[2018-Dixon-Measuring and Mitigating Unintended Bias in Text]] | https://github.com/conversationai/unintended-ml-bias-analysis |
| 12 | [[2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred]] | http://saifmohammad.com/WebPages/Biases-SA.html |
| 13 | [[2018-Ljubesic-Datasets of Slovene and Croatian Moderated News Comments]] | http://hdl.handle.net/11356/1201 |
| 14 | [[2018-Mishra-Are They Our Brothers Analysis and]] | https://github.com/nuhaalbadi/Arabic_hatespeech |
| 15 | [[2018-Nguyen-UIT-VSFC Vietnamese Students' Feedback Corpus for Sentiment Analysis]] | https://github.com/kietnv/uit-vsfc |
| 16 | [[2018-Wiegand-GermEval 2018 Shared Task on the Identification of Offensive Language]] | https://projects.cai.fbi.h-da.de/iggsa/ |
| 17 | [[2018-Zhao-Gender Bias in Coreference Resolution]] | https://github.com/rudinger/winogender-schemas |
| 18 | [[2019-De-Arteaga-Bias in Bios]] | http://aka.ms/biasbios |
| 19 | [[2019-Fortuna-A Hierarchically-Labeled Portuguese Hate Speech Dataset]] | https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset |
| 20 | [[2019-Ibrohim-Multi-label Hate Speech and Abusive Language]] | https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusi... |
| 21 | [[2019-Stanovsky-Evaluating Gender Bias in Machine Translation WinoMT]] | https://github.com/gabrielStanworthy/mt_gender |
| 22 | [[2019-Usbeck-Benchmarking question answering systems]] | https://github.com/AKSW/gerbil/tree/QuestionAnswering |
| 23 | [[2019-collaboration-help_dicrah A ML-based hate speech detection tool on Twitter in French]] | https://github.com/Mik3M4n/help_dicrah |
| 24 | [[2020-Awad-Crowdsourcing moral machines]] | https://moralmachine.mit.edu |
| 25 | [[2020-Awad-Universals and variations in moral decisions made]] | https://moralmachine.mit.edu |
| 26 | [[2020-Hoover-Moral Foundations Twitter Corpus]] | https://osf.io/ezn37/ |
| 27 | [[2020-Souza-BERTimbau Pretrained BERT Models for Brazilian Portuguese]] | https://huggingface.co/neuralmind/bert-base-portuguese-cased |
| 28 | [[2020-Sälevä-A Multi-Orthography Parallel Corpus of Yiddish Nouns]] | http://www.jonnesaleva.com/yi-lrec |
| 29 | [[2020-Whaanga-Indigenous Protocol and Artificial Intelligence Position]] | https://www.indigenous-ai.net/position-paper/ |
| 30 | [[2021-Azada-Fake News Detection in Low-Resourced Languages Kurdish Language Using]] | https://www.kaggle.com/raniaazad/kurdish-fake-news-dataset |
| 31 | [[2021-Cao-Toward Gender-Inclusive Coreference Resolution]] | https://github.com/TristaCao/into_inclusivecoref |
| 32 | [[2021-Croce-RobustBench]] | https://github.com/RobustBench/robustbench |
| 33 | [[2021-Hansson-The Swedish Winogender Dataset SweWinogender]] | https://spraakbanken.gu.se/en/resources/swewinogender |
| 34 | [[2021-Pronoza-Detecting Ethnicity-Targeted Hate Speech in Russian Social Media Texts]] | https://github.com/hse-scila/ethnohate-project |
| 35 | [[2021-Sogaard-Itihasa A Large-Scale Corpus for Sanskrit]] | https://github.com/rahular/itihasa |
| 36 | [[2021-Team-Slovenian Twitter Hate Speech Dataset IMSyPP-sl]] | https://www.clarin.si/repository/xmlui/handle/11356/1398 |
| 37 | [[2021-collaborators-Optimisation of the Largest Annotated Tibetan]] | https://zenodo.org/records/3951503 |
| 38 | [[2022-Atwell-Challenging the Transformer-based Models with a]] | https://github.com/ShathaTm/Quran_Hadith_Datasets |
| 39 | [[2022-Chakravarthi-DravidianCodeMix Sentiment Analysis and Offensive Language]] | https://github.com/bharathichezhiyan/DravidianCodeMix-Dataset |
| 40 | [[2022-Multiple Data in Brief-Sanadset 650K Data on Hadith Narrators]] | https://data.mendeley.com/datasets/5xth87zwb5/4 |
| 41 | [[2022-Network-How can NLP Help Revitalize Endangered Languages]] | https://github.com/ZhangShiyue/RevitalizeCherokee |
| 42 | [[2022-Pollak-Embeddings Models for Buddhist Sanskrit]] | https://figshare.com/articles/code/Gitlab_repository_of_Embeddings_... |
| 43 | [[2022-Romim-BD-SHS A Benchmark Dataset for Learning to Detect Online Bangla Hate]] | https://github.com/naurosromim/hate-speech-dataset-for-Bengali-soci... |
| 44 | [[2022-Saeed-Hate Speech Detection in Social Media for the Kurdish Language]] | https://data.mendeley.com/datasets/x6628zzpdx/1 |
| 45 | [[2022-Yang-CINO A Chinese Minority Pre-trained Language Model]] | http://cino.hfl-rc.com |
| 46 | [[2023-Alyemny-A Data-Driven Exploration of a New Islamic Fatwas]] | https://github.com/ohoud/Fatwaset.git |
| 47 | [[2023-Alyemny-FatwaSet]] | https://github.com/ohoud/Fatwaset.git |
| 48 | [[2023-Aroyo-DICES Dataset]] | https://github.com/google-research-datasets/dices-dataset |
| 49 | [[2023-Ji-Safety Gymnasium]] | https://sites.google.com/view/safety-gymnasium |
| 50 | [[2023-Lee-VisAlign]] | https://github.com/jiyounglee-0523/VisAlign |
| 51 | [[2023-Miah-Islam QA]] | https://www.kaggle.com/datasets/abdullahalmamunn/islam-qa-dataset |
| 52 | [[2023-Standards-NIST AI Risk Management Framework]] | https://doi.org/10.6028/NIST.AI.100-1 |
| 53 | [[2023-Takeshita-JCommonsenseMorality Japanese Dataset for Evaluating Commonsense]] | https://github.com/Language-Media-Lab/commonsense-moral-ja |
| 54 | [[2023-Thapa-NEHATE Large-Scale Annotated Data Shedding Light]] | https://github.com/shucoll/NEHate |
| 55 | [[2023-TheDevastator-HelpSteer A-i Alignment Dataset]] | https://huggingface.co/datasets/nvidia/HelpSteer |
| 56 | [[2023-TheDevastator-OpenAssistant Conversations (OASST1)]] | https://huggingface.co/datasets/OpenAssistant/oasst1 |
| 57 | [[2023-University-Antisemitism on Twitter A Dataset for]] | https://zenodo.org/records/7932888 |
| 58 | [[2024-Akhunzada-Multi-IsnadSet MIS for Sahih Muslim Hadith]] | https://data.mendeley.com/datasets/gzprcr93zn/2 |
| 59 | [[2024-Azerbaijan-Azerbaijani Toxicity Classifier]] | https://huggingface.co/LocalDoc/azerbaijani_toxicity_classifier |
| 60 | [[2024-Defrance-ABCFair]] | https://github.com/aida-ugent/abcfair |
| 61 | [[2024-Gaikwad-MoralBench A Multi-Faceted Benchmark for Ethical and Safety Alignment]] | https://github.com/krimler/moralbench |
| 62 | [[2024-Garcia-Open Portuguese LLM Leaderboard]] | https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard |
| 63 | [[2024-Gordic-Serbian LLM Evaluation Dataset]] | https://github.com/gordicaleksa/serbian-llm-eval |
| 64 | [[2024-Hadi-The Dark Side of Instagram A Large Dataset for Identifying Persian]] | https://github.com/davardoust/PHICAD |
| 65 | [[2024-Hellwig-The Vedic Compound Dataset]] | https://github.com/SvenSellmer/VedicCompoundDataset |
| 66 | [[2024-Kajiwara-Hate Speech and Offensive Language Dataset]] | https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-la... |
| 67 | [[2024-LLM-Beetle-Azerbaijani LLM Leaderboard]] | https://huggingface.co/spaces/LLM-Beetle/azerbaijani-llm-leaderboard |
| 68 | [[2024-Lab-AfroBench Multi-task Benchmark for Evaluating LLMs in African]] | https://mcgill-nlp.github.io/AfroBench/ |
| 69 | [[2024-Laszkiewicz-Benchmarking Fairness in Image Upsampling]] | https://github.com/MikeLasz/Benchmarking-Fairness-ImageUpsampling |
| 70 | [[2024-Levine-Religious Affiliation and Conceptions of the]] | https://github.com/sydneylevine/moral-domain |
| 71 | [[2024-Miðeind-IcelandicEval Utilities to generate Icelandic evaluation data sets]] | https://github.com/mideind/IcelandicEval |
| 72 | [[2024-Multiple Data in Brief-MASAQ Morphologically-Analyzed and Syntactically-Annotated Quran Dataset]] | https://data.mendeley.com/datasets/9yvrzxktmr |
| 73 | [[2024-Murtala-A multilingual dataset for offensive language]] | https://github.com/bharathichezhiyan/DravidianCodeMix-Dataset |
| 74 | [[2024-Nayak-CulturalVQA Evaluating VLMs' Geo-Diverse Cultural Understanding]] | https://huggingface.co/datasets/mair-lab/CulturalVQA |
| 75 | [[2024-Nom-KhmerST A Low-Resource Khmer Scene Text]] | https://gitlab.com/vannkinhnom123/khmerst |
| 76 | [[2024-Organizers-DIALECT-COPA Choice of Plausible Alternatives Datasets in South]] | https://www.clarin.si/repository/xmlui/handle/11356/1766 |
| 77 | [[2024-Overfit-GM-Turkish Overfit-GM Toxic Language Dataset]] | https://huggingface.co/datasets/Overfit-GM/turkish-toxic-language |
| 78 | [[2024-Quang-Vietnamese Law and Ethics Multiple-Choice Questions VLEMCQ]] | https://huggingface.co/datasets/nqdhocai/vietnamese-legal-qa |
| 79 | [[2024-Sagyndyk-Kazakh Dastur-MC Multiple Choice Benchmark]] | https://huggingface.co/datasets/kz-transformers/kazakh-dastur-mc |
| 80 | [[2024-Satar-Seeing Culture Benchmark Evaluating VLMs on Culturally Rich Images]] | https://huggingface.co/datasets/Multimedia-SMU/seeingculture-benchmark |
| 81 | [[2024-Schmeisser-Nieto-Overview of DETESTS-Dis at IberLEF 2024 DETEction and Classification]] | https://detests-dis.github.io/ |
| 82 | [[2024-Tennant-Dynamics of Moral Behavior in Heterogeneous Populations]] | https://github.com/Liza-Tennant/moral_MARL |
| 83 | [[2024-Thu-MixCuBe When Tom Eats Kimchi - Evaluating Cultural Awareness of]] | https://huggingface.co/datasets/kyawyethu/MixCuBe |
| 84 | [[2024-Toygar-Turkish Offensive Language Detection Dataset]] | https://huggingface.co/datasets/Toygar/turkish-offensive-language-d... |
| 85 | [[2024-Trajano-OLID-BR Offensive Language Identification Dataset for Brazilian]] | https://github.com/DougTrajano/olid-br |
| 86 | [[2024-Vladimirova-FairJob]] | https://huggingface.co/datasets/criteo/FairJob |
| 87 | [[2024-Wang-XSafety Multilingual Safety Benchmark]] | https://github.com/Jarviswang94/Multilingual_safety_benchmark |
| 88 | [[2024-community-Open Leaderboard for Hebrew LLMs]] | https://huggingface.co/spaces/hebrew-llm-leaderboard/leaderboard |
| 89 | [[2024-group-ITA-Bench Towards a More Comprehensive Evaluation for Italian LLMs]] | https://github.com/SapienzaNLP/ita-bench |
| 90 | [[2024-project-DharmicData Comprehensive Open-Source Collection of Hindu]] | https://github.com/bhavykhatri/DharmicData |
| 91 | [[2024-team-Indic-Bias A Comprehensive Benchmark for Fairness]] | https://huggingface.co/datasets/ai4bharat/Indic-Bias |
| 92 | [[2024-team-Indic-Bias A Comprehensive Benchmark to Evaluate]] | https://github.com/AI4Bharat/indic-bias |
| 93 | [[2024-Ògúnrẹ̀mí-ÌròyìnSpeech A Multi-purpose Yorùbá Speech Corpus]] | https://github.com/Niger-Volta-LTI/yoruba-voice |
| 94 | [[2025-ADL Center for Technology and Society Daniel Kelley-Generating Hate Anti-Jewish and Anti-Israel Bias]] | https://www.adl.org/resources/report/generating-hate-anti-jewish-an... |
| 95 | [[2025-Akpobi-Yankari Monolingual Yoruba Dataset]] | https://huggingface.co/datasets/acflp/YANKARI |
| 96 | [[2025-Borenstein-Investigating Human Values in Online Communities]] | https://github.com/copenlu/HumanValues |
| 97 | [[2025-Center-Personal Consultations Case Study Database]] | https://www.ncbcenter.org/case-study-database |
| 98 | [[2025-Cognitive-Cognitive LLMs Toward Human-Like Artificial Intelligence by]] | https://github.com/SiyuWu528/LLM-ACTR |
| 99 | [[2025-Consortium-The Vals Legal AI Report (VLAIR)]] | https://www.vals.ai/vlair |
| 100 | [[2025-Dementieva-TextDetox Multilingual Toxicity Dataset]] | https://huggingface.co/datasets/textdetox/multilingual_toxicity_dat... |
| 101 | [[2025-Dey-Beyond the Rubric Cultural Misalignment in LLM Benchmarks for Sexual]] | https://github.com/Sumon/healthbench-srh-eval/ |
| 102 | [[2025-Durmus-Subjective Values]] | https://llmglobalvalues.anthropic.com/ |
| 103 | [[2025-Emezue-NaijaVoices]] | https://naijavoices.com/ |
| 104 | [[2025-Group-AILuminate LLM v1.1 Adding French Language Capabilities to]] | https://github.com/mlcommons/ailuminate |
| 105 | [[2025-Hsieh-TaiwanVQA A Benchmark for Visual Question Answering for Taiwanese]] | https://huggingface.co/datasets/hhhuang/TaiwanVQA |
| 106 | [[2025-IDB-The Performance of Artificial Intelligence in the Use of Indigenous]] | https://publications.iadb.org/publications/english/document/The-Per... |
| 107 | [[2025-Jigsaw-Jigsaw Multilingual Toxic Comment Classification]] | https://www.kaggle.com/competitions/jigsaw-multilingual-toxic-comme... |
| 108 | [[2025-Lahmar-IslamTrust A Benchmark for LLMs Alignment]] | https://github.com/aii-lab-dot-org/IslamTrust |
| 109 | [[2025-Ligeti-Nagy-HuGME A Benchmark System for Evaluating Hungarian Generative Model]] | https://hugme.nytud.hu/ |
| 110 | [[2025-Mayor-Rocher-Spanish Is Not Just One A Dataset of Spanish Dialect Recognition for]] | https://zenodo.org/records/15101403 |
| 111 | [[2025-Moosa-Multi-lingual HateSpeech Dataset]] | https://www.kaggle.com/datasets/wajidhassanmoosa/multilingual-hates... |
| 112 | [[2025-Ning-seeBias]] | https://github.com/nliulab/seeBias |
| 113 | [[2025-Unknown-MIZAN A Persian LLM Leaderboard]] | https://huggingface.co/spaces/MCINext/mizan-llm-leaderboard |
| 114 | [[2025-Wenzek-CC100-Mongolian dataset - NLP Database]] | https://autonlp.ai/datasets/cc100-mongolian |
| 115 | [[2025-Xiangfeng-A dataset of Mongolian Tibetan and Uyghur speech fragments based on]] | https://www.scidb.cn/en/detail?dataSetId=743522838262054912 |
| 116 | [[2025-Xiong-BuddhismEval A Bilingual Benchmark for Buddhist]] | https://huggingface.co/datasets/Nethmi14/BuddhismEval |
| 117 | [[2025-initiative-CatholicBench]] | https://www.catholicbench.com/ |
| 118 | [[2025-initiative-FaithBench AI Benchmark for Christian Theology]] | https://faithbench.com/ |
| 119 | [[2025-onejune2018-Awesome-LLM-Eval Repository Meta-Resource]] | https://github.com/onejune2018/Awesome-LLM-Eval |
| 120 | [[2026-Alam-Quran-MD A Fine-Grained Multilingual Multimodal Dataset]] | https://huggingface.co/datasets/Buraaq/quran-audio-text-dataset |
| 121 | [[2026-Guey-BiasLab Multilingual Dual-Framing Framework]] | https://github.com/williamguey/LLMbiaslab |

</details>

### 4.3 Underrepresented Model Families (< 5 papers)

All model families appear in 5 or more papers.

---

## Appendix A: Model Family Normalization Table

Canonical mapping used to group model names into families:

| Family | Models |
|--------|--------|
| OpenAI | GPT-4, GPT-4o, GPT-4o mini, GPT-4 Turbo, GPT-3.5, GPT-3, GPT-2, ChatGPT, o1, o1-mini, o1-preview, o3, o3-mini, text-davinci, text-davinci-002, text-davinci-003, InstructGPT, CODEX, GPT-5 |
| Anthropic | Claude, Claude-2, Claude-3, Claude-3 Opus, Claude-3 Sonnet, Claude-3 Haiku, Claude Instant |
| Meta | Llama-3, Llama-2, Llama, LLaMA, CodeLlama, OPT, OPT-175B |
| Google | Gemini, Gemini Pro, Gemini Ultra, Gemini Flash, Gemma, Gemma-2, PaLM-2, PaLM, Flan-T5, Flan-UL2, LaMDA, T5, BARD |
| Mistral AI | Mistral, Mixtral |
| Alibaba | Qwen, Qwen-2, Qwen-1.5 |
| DeepSeek | DeepSeek, DeepSeek-V2, DeepSeek-Coder |
| Microsoft | Phi, Phi-2, Phi-3 |
| xAI | Grok |
| Cohere | Cohere, Command-R, Command R+, Aya |
| AI21 | Jurassic, Jurassic-2, J2 |
| Open-source (misc) | Vicuna, Alpaca, Falcon, BLOOM, Yi, Dolly, Zephyr, WizardLM, InternLM, Baichuan, ChatGLM, GLM, StableLM, MPT, DialoGPT, Delphi, ERNIE |
| Pre-LLM / Encoder | BERT, RoBERTa, ALBERT, DeBERTa, DistilBERT, XLNet, ELECTRA, ELMo, BART |
| Embeddings | Word2Vec, GloVe, FastText |

## Appendix B: Methodology Notes

1. **Data source:** YAML frontmatter fields `LLM_assessed` and `DATA_URL` from all 846 papers in `papers/`
2. **Model extraction:** The `LLM_assessed` field contains comma-separated canonical model names assigned during
   the 40-agent deep-read enrichment pipeline (2026-02-12). Values are pre-canonicalized — this report
   performs no additional NLP extraction.
3. **Family grouping:** Models are mapped to families via a static lookup table (Appendix A). Models not
   found in the table are assigned to "Other/Unknown".
4. **Proprietary vs open-source:** Classification is based on model licensing at time of release.
   Some models (e.g., Llama) have evolving licenses; we classify based on the predominant usage pattern.
5. **URL classification:** DATA_URL values may contain multiple comma-separated URLs. Each paper is counted
   once per platform (even if multiple URLs point to the same platform).
6. **Co-occurrence matrix:** Counts how many papers test both Model A and Model B. Only the top 12 models
   by frequency are included to keep the matrix readable.
