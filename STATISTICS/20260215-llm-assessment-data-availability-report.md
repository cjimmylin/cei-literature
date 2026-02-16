# LLM Assessment & Data Availability Report

> **Generated:** 2026-02-15 | **Papers scanned:** 2008

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

This report analyzes **2008 papers** in the CEI Literature Vault for LLM model assessment
coverage and public data/benchmark availability.

| Metric | Count | % of Total |
|--------|------:|:----------:|
| Papers with LLM models identified | 1428 | 71.1% |
| Papers with no LLM models (NA) | 580 | 28.9% |
| Papers with public data URL | 1205 | 60.0% |
| Papers with no data URL (NA) | 803 | 40.0% |
| Papers with **both** models + URL | 994 | 49.5% |
| Papers with **neither** | 369 | 18.4% |

- **1053 unique model names** across **14 model families** detected
- Average models per paper (among assessed papers): **6.2** (max: 53)

---

## 2. LLM Model Landscape

### 2.1 Model Frequency Table

All unique models ranked by number of papers mentioning them:

| Rank | Model | Papers | Family |
|-----:|-------|-------:|--------|
| 1 | GPT-4 | 655 | OpenAI |
| 2 | BERT | 494 | Pre-LLM / Encoder |
| 3 | Llama | 362 | Meta |
| 4 | Llama-3 | 339 | Meta |
| 5 | Qwen | 309 | Alibaba |
| 6 | ChatGPT | 299 | OpenAI |
| 7 | Claude | 290 | Anthropic |
| 8 | GPT-3.5 | 279 | OpenAI |
| 9 | Mistral | 253 | Mistral AI |
| 10 | Gemma | 239 | Google |
| 11 | GPT-4o | 229 | OpenAI |
| 12 | GPT-3 | 225 | OpenAI |
| 13 | Llama-2 | 211 | Meta |
| 14 | RoBERTa | 193 | Pre-LLM / Encoder |
| 15 | DeepSeek | 168 | DeepSeek |
| 16 | Gemini | 126 | Google |
| 17 | ALBERT | 85 | Pre-LLM / Encoder |
| 18 | Qwen2.5 | 83 | Other/Unknown |
| 19 | Vicuna | 79 | Open-source (misc) |
| 20 | Mistral-7B | 78 | Other/Unknown |
| 21 | Mixtral | 74 | Mistral AI |
| 22 | Llama-3.1 | 74 | Other/Unknown |
| 23 | GPT-2 | 66 | OpenAI |
| 24 | T5 | 66 | Google |
| 25 | Alpaca | 66 | Open-source (misc) |
| 26 | Qwen2 | 59 | Other/Unknown |
| 27 | BLOOM | 58 | Open-source (misc) |
| 28 | Llama 3 | 48 | Other/Unknown |
| 29 | Llama 3.1 | 43 | Other/Unknown |
| 30 | Gemma-2 | 42 | Google |
| 31 | Qwen3 | 42 | Other/Unknown |
| 32 | GPT-4o-mini | 41 | Other/Unknown |
| 33 | llama 3 | 35 | Other/Unknown |
| 34 | Llama3 | 34 | Other/Unknown |
| 35 | Mistral 7B | 34 | Other/Unknown |
| 36 | Qwen 2.5 | 34 | Other/Unknown |
| 37 | Phi | 33 | Microsoft |
| 38 | Word2Vec | 32 | Embeddings |
| 39 | GloVe | 32 | Embeddings |
| 40 | Gemma 2 | 32 | Other/Unknown |
| 41 | DeepSeek-R1 | 32 | Other/Unknown |
| 42 | DeepSeek-V3 | 32 | Other/Unknown |
| 43 | Llama2 | 31 | Other/Unknown |
| 44 | GPT-3.5-turbo | 31 | Other/Unknown |
| 45 | Grok | 30 | xAI |
| 46 | Llama 2 | 28 | Other/Unknown |
| 47 | GPT4 | 28 | Other/Unknown |
| 48 | Qwen-2.5 | 28 | Other/Unknown |
| 49 | BLOOMZ | 27 | Other/Unknown |
| 50 | Gemma2 | 27 | Other/Unknown |
| 51 | Falcon | 26 | Open-source (misc) |
| 52 | BART | 24 | Pre-LLM / Encoder |
| 53 | DeBERTa | 24 | Pre-LLM / Encoder |
| 54 | InstructGPT | 24 | OpenAI |
| 55 | Claude 3.5 Sonnet | 24 | Other/Unknown |
| 56 | GPT-3.5 Turbo | 24 | Other/Unknown |
| 57 | Gemma-3 | 24 | Other/Unknown |
| 58 | PaLM-2 | 23 | Google |
| 59 | Llama-3.2 | 23 | Other/Unknown |
| 60 | PaLM | 22 | Google |
| 61 | ELECTRA | 21 | Pre-LLM / Encoder |
| 62 | GPT-3.5-Turbo | 21 | Other/Unknown |
| 63 | Claude 3.5 | 21 | Other/Unknown |
| 64 | LLaMA-3.1 | 21 | Other/Unknown |
| 65 | DeepSeek-AI | 21 | Other/Unknown |
| 66 | gpt-3.5-turbo | 20 | Other/Unknown |
| 67 | GPT-4o mini | 20 | OpenAI |
| 68 | Llama3.1 | 20 | Other/Unknown |
| 69 | DistilBERT | 19 | Pre-LLM / Encoder |
| 70 | Llama-3.3 | 19 | Other/Unknown |
| 71 | o3 | 18 | OpenAI |
| 72 | XLNet | 17 | Pre-LLM / Encoder |
| 73 | Claude Sonnet | 17 | Other/Unknown |
| 74 | Bloom | 16 | Open-source (misc) |
| 75 | Llama 3.2 | 16 | Other/Unknown |
| 76 | Flan-T5 | 15 | Google |
| 77 | LLaMA2 | 15 | Other/Unknown |
| 78 | Qwen1.5 | 15 | Other/Unknown |
| 79 | Qwen-7B | 15 | Other/Unknown |
| 80 | GPT3 | 14 | Other/Unknown |
| 81 | Claude-3 | 14 | Anthropic |
| 82 | GPT-4 Turbo | 14 | OpenAI |
| 83 | Llama Guard | 14 | Other/Unknown |
| 84 | Claude-3.5-Sonnet | 14 | Other/Unknown |
| 85 | o1 | 14 | OpenAI |
| 86 | claude-3 | 13 | Anthropic |
| 87 | Baichuan2 | 13 | Other/Unknown |
| 88 | Llama 3.3 | 13 | Other/Unknown |
| 89 | gemma-2 | 13 | Google |
| 90 | ELMo | 12 | Pre-LLM / Encoder |
| 91 | GPT2 | 12 | Other/Unknown |
| 92 | LLaMA 3.1 | 12 | Other/Unknown |
| 93 | Mistral 7b | 12 | Other/Unknown |
| 94 | Dolly | 12 | Open-source (misc) |
| 95 | Gemma 3 | 12 | Other/Unknown |
| 96 | word2vec | 11 | Embeddings |
| 97 | XLM-RoBERTa | 11 | Other/Unknown |
| 98 | OPT | 11 | Meta |
| 99 | ChatGLM | 11 | Open-source (misc) |
| 100 | GPT 3 | 11 | Other/Unknown |
| 101 | GPT-4-Turbo | 11 | Other/Unknown |
| 102 | Command-R | 11 | Cohere |
| 103 | Phi-3 | 11 | Microsoft |
| 104 | Phi-4 | 11 | Other/Unknown |
| 105 | Qwen 2 | 11 | Other/Unknown |
| 106 | LlamaGuard | 11 | Other/Unknown |
| 107 | GPT4o | 11 | Other/Unknown |
| 108 | Mixtral-8x7B | 11 | Other/Unknown |
| 109 | Gemma3 | 11 | Other/Unknown |
| 110 | Llama-4 | 11 | Other/Unknown |
| 111 | LLaMA 3 | 11 | Other/Unknown |
| 112 | mBERT | 10 | Other/Unknown |
| 113 | Qwen-14B | 10 | Other/Unknown |
| 114 | gpt-4o-mini | 10 | Other/Unknown |
| 115 | LLaMA3 | 10 | Other/Unknown |
| 116 | Claude-3.5 | 10 | Other/Unknown |
| 117 | Mistral-Small | 10 | Other/Unknown |
| 118 | DeepSeek V3 | 10 | Other/Unknown |
| 119 | Codex | 9 | OpenAI |
| 120 | text-davinci | 9 | OpenAI |
| 121 | Baichuan | 9 | Open-source (misc) |
| 122 | Mistral-Nemo | 9 | Other/Unknown |
| 123 | Barth | 9 | Other/Unknown |
| 124 | Claude 3.5 Haiku | 9 | Other/Unknown |
| 125 | Qwen-3 | 9 | Other/Unknown |
| 126 | PaLM 2 | 8 | Other/Unknown |
| 127 | GPT 3.5 | 8 | Other/Unknown |
| 128 | Claude. | 8 | Other/Unknown |
| 129 | llama3 | 8 | Other/Unknown |
| 130 | Claude-3-Opus | 8 | Other/Unknown |
| 131 | GPT 4 | 8 | Other/Unknown |
| 132 | InternLM | 8 | Open-source (misc) |
| 133 | Llama3.3 | 8 | Other/Unknown |
| 134 | Qwen 3 | 8 | Other/Unknown |
| 135 | Palm | 7 | Google |
| 136 | llama. | 7 | Other/Unknown |
| 137 | Qwen-1.5 | 7 | Alibaba |
| 138 | LLaMA 2 | 7 | Other/Unknown |
| 139 | Claude-Sonnet | 7 | Other/Unknown |
| 140 | mistralai | 7 | Other/Unknown |
| 141 | LLaMA3.1 | 7 | Other/Unknown |
| 142 | GPT-4-turbo | 7 | Other/Unknown |
| 143 | Claude 3 | 7 | Other/Unknown |
| 144 | LaMDA | 6 | Google |
| 145 | Bartolo | 6 | Other/Unknown |
| 146 | CamemBERT | 6 | Other/Unknown |
| 147 | LLAMA2 | 6 | Other/Unknown |
| 148 | GPT3.5 | 6 | Other/Unknown |
| 149 | Llama. | 6 | Other/Unknown |
| 150 | CommandR | 6 | Other/Unknown |
| 151 | Llama-3. | 6 | Other/Unknown |
| 152 | Claude 3 Opus | 6 | Other/Unknown |
| 153 | GPT 4o | 6 | Other/Unknown |
| 154 | MistralAI | 6 | Other/Unknown |
| 155 | LLaMA 3.2 | 6 | Other/Unknown |
| 156 | Llama3.2 | 6 | Other/Unknown |
| 157 | Mistral-Large | 6 | Other/Unknown |
| 158 | LLama-3.1 | 6 | Other/Unknown |
| 159 | Mistral Large | 6 | Other/Unknown |
| 160 | Llama 4 | 6 | Other/Unknown |
| 161 | DeepSeek R1 | 6 | Other/Unknown |
| 162 | Claude 3.7 Sonnet | 6 | Other/Unknown |
| 163 | Glove | 5 | Embeddings |
| 164 | LLaMA. | 5 | Other/Unknown |
| 165 | WizardLM | 5 | Open-source (misc) |
| 166 | CodeLlama | 5 | Meta |
| 167 | PaLM2 | 5 | Other/Unknown |
| 168 | Bloom-1b7 | 5 | Other/Unknown |
| 169 | Mixtral-8x22B | 5 | Other/Unknown |
| 170 | Falcon 7B | 5 | Other/Unknown |
| 171 | Claude Opus | 5 | Other/Unknown |
| 172 | LLaMA-3.2 | 5 | Other/Unknown |
| 173 | mistral.ai | 5 | Other/Unknown |
| 174 | Mixtral 8x7B | 5 | Other/Unknown |
| 175 | qwenlm | 5 | Other/Unknown |
| 176 | InternLM2 | 5 | Other/Unknown |
| 177 | Mistral Small | 5 | Other/Unknown |
| 178 | Grok-3 | 5 | Other/Unknown |
| 179 | LLaMA 4 | 5 | Other/Unknown |
| 180 | Qwen-32B | 5 | Other/Unknown |
| 181 | gemma-3 | 5 | Other/Unknown |
| 182 | Llama-Guard | 5 | Other/Unknown |
| 183 | T5-based | 4 | Other/Unknown |
| 184 | DeBERTa-v3 | 4 | Other/Unknown |
| 185 | Bart | 4 | Pre-LLM / Encoder |
| 186 | Claude 2 | 4 | Other/Unknown |
| 187 | Claude-2. | 4 | Other/Unknown |
| 188 | LLaMa-2 | 4 | Meta |
| 189 | ChatGLM-6B | 4 | Other/Unknown |
| 190 | ChatGLM2 | 4 | Other/Unknown |
| 191 | Bartl | 4 | Other/Unknown |
| 192 | T5-Large | 4 | Other/Unknown |
| 193 | Claude-3-Sonnet | 4 | Other/Unknown |
| 194 | Qwen-72B | 4 | Other/Unknown |
| 195 | Claude-3.5-sonnet | 4 | Other/Unknown |
| 196 | mistral-7b | 4 | Other/Unknown |
| 197 | Claude 3 Haiku | 4 | Other/Unknown |
| 198 | BloomZ | 4 | Other/Unknown |
| 199 | Llama3. | 4 | Other/Unknown |
| 200 | Mixtral 8x22B | 4 | Other/Unknown |
| 201 | Gemma-1.1 | 4 | Other/Unknown |
| 202 | GPT 3.5 Turbo | 4 | Other/Unknown |
| 203 | Bloom-7b1 | 4 | Other/Unknown |
| 204 | ChatGLM3 | 4 | Other/Unknown |
| 205 | claude-sonnet | 4 | Other/Unknown |
| 206 | LLAMA-3.1 | 4 | Other/Unknown |
| 207 | Llama-3.1-8B | 4 | Other/Unknown |
| 208 | llama3.1 | 4 | Other/Unknown |
| 209 | gemma | 4 | Google |
| 210 | Falcon3 | 4 | Other/Unknown |
| 211 | LLaMA 3.3 | 4 | Other/Unknown |
| 212 | Mistral- 7B | 4 | Other/Unknown |
| 213 | LLAMA-3.2 | 4 | Other/Unknown |
| 214 | LLaMA 3. | 4 | Other/Unknown |
| 215 | Claude-3.7-Sonnet | 4 | Other/Unknown |
| 216 | Debertav3 | 3 | Other/Unknown |
| 217 | UmBERTo | 3 | Other/Unknown |
| 218 | phi-1 | 3 | Other/Unknown |
| 219 | Electra | 3 | Pre-LLM / Encoder |
| 220 | Flan-T5-Large | 3 | Other/Unknown |
| 221 | T5-XXL | 3 | Other/Unknown |
| 222 | Claude-3-Haiku | 3 | Other/Unknown |
| 223 | Zephyr | 3 | Open-source (misc) |
| 224 | Bloom-7B | 3 | Other/Unknown |
| 225 | gpt-4-turbo | 3 | Other/Unknown |
| 226 | GPT-4-TURBO | 3 | Other/Unknown |
| 227 | Phi-3-mini | 3 | Other/Unknown |
| 228 | Llama 3.2. | 3 | Other/Unknown |
| 229 | CroissantLLM | 3 | Other/Unknown |
| 230 | Claude-2 | 3 | Anthropic |
| 231 | Falcon-7B | 3 | Other/Unknown |
| 232 | Mistral-7b | 3 | Other/Unknown |
| 233 | Mistral-v0 | 3 | Other/Unknown |
| 234 | Claude-3-opus | 3 | Other/Unknown |
| 235 | llama2 | 3 | Other/Unknown |
| 236 | Qwen technical | 3 | Other/Unknown |
| 237 | Qwen 7B | 3 | Other/Unknown |
| 238 | alpaca | 3 | Open-source (misc) |
| 239 | Deberta | 3 | Pre-LLM / Encoder |
| 240 | Claude 3 Sonnet | 3 | Other/Unknown |
| 241 | Llama2-Chat | 3 | Other/Unknown |
| 242 | llama-3. | 3 | Other/Unknown |
| 243 | LLaMA2. | 3 | Other/Unknown |
| 244 | Bloomz | 3 | Other/Unknown |
| 245 | Mixtral-8x7b | 3 | Other/Unknown |
| 246 | Qwen-Audio | 3 | Other/Unknown |
| 247 | Mistral-NeMo | 3 | Other/Unknown |
| 248 | Phi-3-medium | 3 | Other/Unknown |
| 249 | command-r | 3 | Cohere |
| 250 | Qwen-VL | 3 | Other/Unknown |
| 251 | LLAMA-3.3 | 3 | Other/Unknown |
| 252 | LLaMA-4 | 3 | Other/Unknown |
| 253 | Llama 2-Chat | 3 | Other/Unknown |
| 254 | Claude 3.7 | 3 | Other/Unknown |
| 255 | Grok-4 | 3 | Other/Unknown |
| 256 | Grok 3 | 3 | Other/Unknown |
| 257 | LLaMA-3.3 | 3 | Other/Unknown |
| 258 | Qwen-1.5B | 3 | Other/Unknown |
| 259 | Barto | 2 | Other/Unknown |
| 260 | grok | 2 | xAI |
| 261 | FinBERT | 2 | Other/Unknown |
| 262 | FlauBERT | 2 | Other/Unknown |
| 263 | AlBERTo | 2 | Other/Unknown |
| 264 | BERT-Italian | 2 | Other/Unknown |
| 265 | LLAMA 2 | 2 | Other/Unknown |
| 266 | LLaMA 1 | 2 | Other/Unknown |
| 267 | electra | 2 | Pre-LLM / Encoder |
| 268 | Llama2. | 2 | Other/Unknown |
| 269 | Qwen-Max | 2 | Other/Unknown |
| 270 | Bloomberg | 2 | Other/Unknown |
| 271 | Baichuan-7B | 2 | Other/Unknown |
| 272 | Falcon-40B | 2 | Other/Unknown |
| 273 | BLOOM-7B | 2 | Other/Unknown |
| 274 | LLaMA-2-chat | 2 | Other/Unknown |
| 275 | NB-BERT | 2 | Other/Unknown |
| 276 | GPT-3.5 turbo | 2 | Other/Unknown |
| 277 | BLOOM-7 | 2 | Other/Unknown |
| 278 | OPT-66B | 2 | Other/Unknown |
| 279 | text-davinci-003 | 2 | OpenAI |
| 280 | BERTje | 2 | Other/Unknown |
| 281 | RobBERT | 2 | Other/Unknown |
| 282 | Baichuan-2 | 2 | Other/Unknown |
| 283 | InternLM-XComposer2 | 2 | Other/Unknown |
| 284 | GPT3.5-TURBO | 2 | Other/Unknown |
| 285 | baichuan-inc | 2 | Other/Unknown |
| 286 | LLama 2 | 2 | Other/Unknown |
| 287 | CLAUDE-3 | 2 | Anthropic |
| 288 | bloom-1b1 | 2 | Other/Unknown |
| 289 | Phi-3 Mini | 2 | Other/Unknown |
| 290 | LLama3 | 2 | Other/Unknown |
| 291 | LLama3.1 | 2 | Other/Unknown |
| 292 | deepseek r1 | 2 | Other/Unknown |
| 293 | GloVE | 2 | Embeddings |
| 294 | Command R+ | 2 | Cohere |
| 295 | DeBERTaV3 | 2 | Other/Unknown |
| 296 | claude-instant | 2 | Other/Unknown |
| 297 | Qwen-2 | 2 | Alibaba |
| 298 | LLaMA2-chat | 2 | Other/Unknown |
| 299 | Qwen-72b | 2 | Other/Unknown |
| 300 | claude 3 | 2 | Other/Unknown |
| 301 | LLaMA-3. | 2 | Other/Unknown |
| 302 | LLama 3 | 2 | Other/Unknown |
| 303 | Bartlett | 2 | Other/Unknown |
| 304 | Claude3.5 | 2 | Other/Unknown |
| 305 | Qwen 1 | 2 | Other/Unknown |
| 306 | Yi-34B | 2 | Other/Unknown |
| 307 | T5-base | 2 | Other/Unknown |
| 308 | LLaMa3 | 2 | Other/Unknown |
| 309 | GPT-4-Vision | 2 | Other/Unknown |
| 310 | Gpt4 | 2 | Other/Unknown |
| 311 | gpt-35-turbo | 2 | Other/Unknown |
| 312 | Llama-2. | 2 | Other/Unknown |
| 313 | gpt2 | 2 | Other/Unknown |
| 314 | phi-1_5 | 2 | Other/Unknown |
| 315 | Mistral Medium | 2 | Other/Unknown |
| 316 | Command R | 2 | Other/Unknown |
| 317 | Phi 3 | 2 | Other/Unknown |
| 318 | Baichuan-13B | 2 | Other/Unknown |
| 319 | Claude-3 Opus | 2 | Anthropic |
| 320 | llama 2 | 2 | Other/Unknown |
| 321 | llama 2. | 2 | Other/Unknown |
| 322 | QWEN-72B | 2 | Other/Unknown |
| 323 | GPT4-Turbo | 2 | Other/Unknown |
| 324 | Mistral-AI | 2 | Other/Unknown |
| 325 | Qwen 1.5 | 2 | Other/Unknown |
| 326 | GPT 2 | 2 | Other/Unknown |
| 327 | Mistral 8B | 2 | Other/Unknown |
| 328 | Mistral v0 | 2 | Other/Unknown |
| 329 | DeepSeekMath | 2 | Other/Unknown |
| 330 | Mixtral 8 | 2 | Other/Unknown |
| 331 | LLaMA-2-Chat | 2 | Other/Unknown |
| 332 | claude. | 2 | Other/Unknown |
| 333 | Qwen-Chat | 2 | Other/Unknown |
| 334 | Qwen-chat | 2 | Other/Unknown |
| 335 | BLOOMz | 2 | Other/Unknown |
| 336 | bart-base | 2 | Other/Unknown |
| 337 | Claude-4 | 2 | Other/Unknown |
| 338 | Claude-4-Sonnet | 2 | Other/Unknown |
| 339 | LLaMa 3.1 | 2 | Other/Unknown |
| 340 | Qwen 1.5B | 2 | Other/Unknown |
| 341 | Mixtral 7B | 2 | Other/Unknown |
| 342 | DeepSeek v3 | 2 | Other/Unknown |
| 343 | Phi3 | 2 | Other/Unknown |
| 344 | GEMMA-2 | 2 | Google |
| 345 | QWEN2.5 | 2 | Other/Unknown |
| 346 | InternLM-2 | 2 | Other/Unknown |
| 347 | Qwen 72B | 2 | Other/Unknown |
| 348 | mixtral-8x22b | 2 | Other/Unknown |
| 349 | GEMMA | 2 | Google |
| 350 | LLAMA 3 | 2 | Other/Unknown |
| 351 | Llama-3.1-70B | 2 | Other/Unknown |
| 352 | Claude-3.5 Sonnet | 2 | Other/Unknown |
| 353 | Command-R-Plus | 2 | Other/Unknown |
| 354 | Claude 4. | 2 | Other/Unknown |
| 355 | DeepSeek 1 | 2 | Other/Unknown |
| 356 | qwen-2.5 | 2 | Other/Unknown |
| 357 | DeepSeekCoder | 2 | Other/Unknown |
| 358 | T5-style | 2 | Other/Unknown |
| 359 | LLaMA3. | 2 | Other/Unknown |
| 360 | phi-4 | 2 | Other/Unknown |
| 361 | DeepSeek-v3 | 2 | Other/Unknown |
| 362 | PALM | 2 | Google |
| 363 | Mistral Instruct | 2 | Other/Unknown |
| 364 | Claude-3.5-Haiku | 2 | Other/Unknown |
| 365 | LLAMA-3. | 2 | Other/Unknown |
| 366 | QWEN3 | 2 | Other/Unknown |
| 367 | gemma3 | 2 | Other/Unknown |
| 368 | Claude 3.5-Sonnet | 2 | Other/Unknown |
| 369 | Phi-4-multimodal | 2 | Other/Unknown |
| 370 | LLaMA Guard | 2 | Other/Unknown |
| 371 | Llama- Guard | 2 | Other/Unknown |
| 372 | dolly | 2 | Open-source (misc) |
| 373 | Baichuan 2 | 2 | Other/Unknown |
| 374 | GPT-5 | 2 | OpenAI |
| 375 | Phi4 | 2 | Other/Unknown |
| 376 | Claude-Haiku | 2 | Other/Unknown |
| 377 | Llama4 | 2 | Other/Unknown |
| 378 | Mistral 3.1 | 2 | Other/Unknown |
| 379 | Deepseek-R1 | 2 | Other/Unknown |
| 380 | BLOOM-1 | 2 | Other/Unknown |
| 381 | Claude 4 | 2 | Other/Unknown |
| 382 | Falcon-7b | 2 | Other/Unknown |
| 383 | Gemini-Pro | 2 | Other/Unknown |
| 384 | Grok 4 | 2 | Other/Unknown |
| 385 | claude-4 | 2 | Other/Unknown |
| 386 | Aya-Expanse | 2 | Other/Unknown |
| 387 | claude-3.5-sonnet | 2 | Other/Unknown |
| 388 | GPT4O | 2 | Other/Unknown |
| 389 | DeepSeek-Coder | 2 | DeepSeek |
| 390 | mistral-large | 2 | Other/Unknown |
| 391 | Claude-Opus | 2 | Other/Unknown |
| 392 | LLaMa-3.1 | 2 | Other/Unknown |
| 393 | Claude 3. | 2 | Other/Unknown |
| 394 | GPT 4o Mini | 2 | Other/Unknown |
| 395 | gemma2 | 2 | Other/Unknown |
| 396 | multiple LLMs | 2 | Other/Unknown |
| 397 | Claude-3.7 | 2 | Other/Unknown |
| 398 | Qwen-SEA | 2 | Other/Unknown |
| 399 | Phi-4-Mini | 2 | Other/Unknown |
| 400 | Qwen3Guard | 2 | Other/Unknown |
| 401 | Bloom P | 1 | Other/Unknown |
| 402 | BiLSTM | 1 | Other/Unknown |
| 403 | word2Vec | 1 | Embeddings |
| 404 | BART-based | 1 | Other/Unknown |
| 405 | gloVe | 1 | Embeddings |
| 406 | T5-11B | 1 | Other/Unknown |
| 407 | Word2vec | 1 | Embeddings |
| 408 | codex | 1 | OpenAI |
| 409 | elmo | 1 | Pre-LLM / Encoder |
| 410 | BioBERT | 1 | Other/Unknown |
| 411 | PubMedBERT | 1 | Other/Unknown |
| 412 | BARThez | 1 | Other/Unknown |
| 413 | PAGnol | 1 | Other/Unknown |
| 414 | GPT-J | 1 | Other/Unknown |
| 415 | GPT-NeoX | 1 | Other/Unknown |
| 416 | FrALBERT | 1 | Other/Unknown |
| 417 | BERTeus | 1 | Other/Unknown |
| 418 | mT5 | 1 | Other/Unknown |
| 419 | GilBERTo | 1 | Other/Unknown |
| 420 | LLaMA 1. | 1 | Other/Unknown |
| 421 | VICUNA | 1 | Open-source (misc) |
| 422 | DeBERTa re | 1 | Other/Unknown |
| 423 | DeBERTa-v3large | 1 | Other/Unknown |
| 424 | T5 and | 1 | Other/Unknown |
| 425 | T511B | 1 | Other/Unknown |
| 426 | Claude 1 | 1 | Other/Unknown |
| 427 | text-davinci-002 | 1 | OpenAI |
| 428 | ChatGLM-turbo | 1 | Other/Unknown |
| 429 | PoliBERT | 1 | Other/Unknown |
| 430 | bert-base-italian-xxl-uncased | 1 | Other/Unknown |
| 431 | CodeX | 1 | OpenAI |
| 432 | Vigogne (LLaMa-based) | 1 | Other/Unknown |
| 433 | BLOOM perform | 1 | Other/Unknown |
| 434 | BloombergGPT | 1 | Other/Unknown |
| 435 | T5 LLM | 1 | Other/Unknown |
| 436 | phi-1 using | 1 | Other/Unknown |
| 437 | LlaMA2 | 1 | Other/Unknown |
| 438 | Bartels | 1 | Other/Unknown |
| 439 | LLaMA 36.4 | 1 | Other/Unknown |
| 440 | ELMO | 1 | Pre-LLM / Encoder |
| 441 | deberta using | 1 | Other/Unknown |
| 442 | Falconer | 1 | Other/Unknown |
| 443 | DistilBert | 1 | Pre-LLM / Encoder |
| 444 | KB-BERT | 1 | Other/Unknown |
| 445 | DFM-encoder | 1 | Other/Unknown |
| 446 | RemBERT | 1 | Other/Unknown |
| 447 | mDeBERTaV3 | 1 | Other/Unknown |
| 448 | Scandinavian BERT variants | 1 | Other/Unknown |
| 449 | NorBERT3 | 1 | Other/Unknown |
| 450 | NorT5 | 1 | Other/Unknown |
| 451 | ScandiBERT | 1 | Other/Unknown |
| 452 | OPT-6 | 1 | Other/Unknown |
| 453 | FLAN-T5 | 1 | Google |
| 454 | CroSloEngual BERT | 1 | Other/Unknown |
| 455 | FLAN-T5-XXL | 1 | Other/Unknown |
| 456 | Flan-T5-Base | 1 | Other/Unknown |
| 457 | Flan-T5-Small | 1 | Other/Unknown |
| 458 | Flan-T5-XL | 1 | Other/Unknown |
| 459 | T5-Base | 1 | Other/Unknown |
| 460 | T5-Small | 1 | Other/Unknown |
| 461 | T5-XL | 1 | Other/Unknown |
| 462 | BLOOM 0 | 1 | Other/Unknown |
| 463 | BLOOM 3 | 1 | Other/Unknown |
| 464 | OPT 3 | 1 | Other/Unknown |
| 465 | Claude.ai | 1 | Other/Unknown |
| 466 | PALM-2 | 1 | Google |
| 467 | Llama8 | 1 | Other/Unknown |
| 468 | Llama8. | 1 | Other/Unknown |
| 469 | InternLM-XC2 | 1 | Other/Unknown |
| 470 | FALCON 40B | 1 | Other/Unknown |
| 471 | LLAMA 1 | 1 | Other/Unknown |
| 472 | LLAMA 1. | 1 | Other/Unknown |
| 473 | LLAMA-2-CHAT | 1 | Other/Unknown |
| 474 | Mixtral 8X7B | 1 | Other/Unknown |
| 475 | XGLM | 1 | Other/Unknown |
| 476 | LLaMa | 1 | Meta |
| 477 | ChatGLM_Turbo | 1 | Other/Unknown |
| 478 | Bloom-560m | 1 | Other/Unknown |
| 479 | Gpt2 | 1 | Other/Unknown |
| 480 | OPT-125m | 1 | Other/Unknown |
| 481 | CLAUDE-3-OPUS | 1 | Other/Unknown |
| 482 | MIXTRAL-8X22B | 1 | Other/Unknown |
| 483 | Bloom 1 | 1 | Other/Unknown |
| 484 | Bloom-1b111 | 1 | Other/Unknown |
| 485 | bloom-1 | 1 | Other/Unknown |
| 486 | BLOOM-7B1 | 1 | Other/Unknown |
| 487 | GPT3.5-turbo | 1 | Other/Unknown |
| 488 | QWEN1.5 | 1 | Other/Unknown |
| 489 | Qwen.5 | 1 | Other/Unknown |
| 490 | Zephyr 7B | 1 | Other/Unknown |
| 491 | E5-multilingual | 1 | Other/Unknown |
| 492 | Sentence-T5 | 1 | Other/Unknown |
| 493 | LaBSE | 1 | Other/Unknown |
| 494 | multilingual-e5 | 1 | Other/Unknown |
| 495 | Scandinavian sentence encoders | 1 | Other/Unknown |
| 496 | Latxa (LLaMa-based) | 1 | Other/Unknown |
| 497 | Irati | 1 | Other/Unknown |
| 498 | Mistral7B | 1 | Other/Unknown |
| 499 | Mistral-NEMO | 1 | Other/Unknown |
| 500 | Phi-3 49 | 1 | Other/Unknown |
| 501 | InternLM CSMPT | 1 | Other/Unknown |
| 502 | Llama.1 | 1 | Other/Unknown |
| 503 | Mistral 2411 123B | 1 | Other/Unknown |
| 504 | Mistral 8x22B | 1 | Other/Unknown |
| 505 | Phi 3 Mini | 1 | Other/Unknown |
| 506 | llama3.1 chat | 1 | Other/Unknown |
| 507 | Command | 1 | Other/Unknown |
| 508 | and 32 additional LLMs (39 total) | 1 | Other/Unknown |
| 509 | BLOOM model | 1 | Other/Unknown |
| 510 | mGPT | 1 | Other/Unknown |
| 511 | German BERT variants | 1 | Other/Unknown |
| 512 | LeoLM | 1 | Other/Unknown |
| 513 | gelectra-large | 1 | Other/Unknown |
| 514 | Bartolo59 | 1 | Other/Unknown |
| 515 | Palm 2 | 1 | Other/Unknown |
| 516 | palm | 1 | Google |
| 517 | GPT-4 Vision | 1 | Other/Unknown |
| 518 | Mixtral-8 | 1 | Other/Unknown |
| 519 | WizardLM L2Chat | 1 | Other/Unknown |
| 520 | Gemini Pro | 1 | Google |
| 521 | and other Danish LLMs | 1 | Other/Unknown |
| 522 | Mistral Nemo25 | 1 | Other/Unknown |
| 523 | Qwen 2.526 | 1 | Other/Unknown |
| 524 | DeBERTa-Base | 1 | Other/Unknown |
| 525 | claude-2.0 | 1 | Other/Unknown |
| 526 | T5 ROUGE | 1 | Other/Unknown |
| 527 | T5 T6 | 1 | Other/Unknown |
| 528 | Claude-23 | 1 | Other/Unknown |
| 529 | Claude2 | 1 | Other/Unknown |
| 530 | Falcon40B | 1 | Other/Unknown |
| 531 | llama-2 chat | 1 | Other/Unknown |
| 532 | Claude-3-sonnet | 1 | Other/Unknown |
| 533 | Gemma7 | 1 | Other/Unknown |
| 534 | Mistral-based | 1 | Other/Unknown |
| 535 | MistralFT | 1 | Other/Unknown |
| 536 | LLaMA3.1-chat | 1 | Other/Unknown |
| 537 | Llama-2 chat | 1 | Other/Unknown |
| 538 | Mistral-nemo | 1 | Other/Unknown |
| 539 | Claude3.5-sonnet | 1 | Other/Unknown |
| 540 | Gemini1.5-pro | 1 | Other/Unknown |
| 541 | O3 | 1 | OpenAI |
| 542 | Bloom 3B | 1 | Other/Unknown |
| 543 | Bloom 7B | 1 | Other/Unknown |
| 544 | LlaMa2 | 1 | Other/Unknown |
| 545 | LlaMa3 | 1 | Other/Unknown |
| 546 | Qwen Llama2 | 1 | Other/Unknown |
| 547 | Qwen 13B | 1 | Other/Unknown |
| 548 | InternLM Team | 1 | Other/Unknown |
| 549 | InternLM-Chat | 1 | Other/Unknown |
| 550 | Qwen Qwen | 1 | Other/Unknown |
| 551 | Qwen Table | 1 | Other/Unknown |
| 552 | Yi 16 | 1 | Other/Unknown |
| 553 | mGPT-1.3B | 1 | Other/Unknown |
| 554 | BLOOM-1.7B | 1 | Other/Unknown |
| 555 | BLOOM-7.1B | 1 | Other/Unknown |
| 556 | Llama2-7B | 1 | Other/Unknown |
| 557 | Llama3-8B | 1 | Other/Unknown |
| 558 | Aya-23-8B | 1 | Other/Unknown |
| 559 | NorGPT-369M | 1 | Other/Unknown |
| 560 | NorGPT-3B | 1 | Other/Unknown |
| 561 | NorGPT-23B | 1 | Other/Unknown |
| 562 | NorLlama-3B | 1 | Other/Unknown |
| 563 | NB-GPT-J-6B | 1 | Other/Unknown |
| 564 | Mistral Nemo | 1 | Other/Unknown |
| 565 | Falcon 0 | 1 | Other/Unknown |
| 566 | Llama39 | 1 | Other/Unknown |
| 567 | Mistral 0.159 Llama3 | 1 | Other/Unknown |
| 568 | flan-t5-xl | 1 | Other/Unknown |
| 569 | t5-xl | 1 | Other/Unknown |
| 570 | BART-large | 1 | Other/Unknown |
| 571 | RoGPT-2 | 1 | Other/Unknown |
| 572 | GPT4-Vision | 1 | Other/Unknown |
| 573 | Llama2 chat | 1 | Other/Unknown |
| 574 | Mistral-v1 | 1 | Other/Unknown |
| 575 | Lamda | 1 | Google |
| 576 | LLaMa 2 | 1 | Other/Unknown |
| 577 | Mistral-0.2-Instruct | 1 | Other/Unknown |
| 578 | Distilbert | 1 | Pre-LLM / Encoder |
| 579 | Llama-2-Chat | 1 | Other/Unknown |
| 580 | Mixtral-8X7B | 1 | Other/Unknown |
| 581 | Phi-1 | 1 | Other/Unknown |
| 582 | LLäMmlein-120M | 1 | Other/Unknown |
| 583 | LLäMmlein-1B | 1 | Other/Unknown |
| 584 | bert-base-german-cased | 1 | Other/Unknown |
| 585 | 10 German-pretrained models | 1 | Other/Unknown |
| 586 | phi-2 | 1 | Microsoft |
| 587 | Mistral large | 1 | Other/Unknown |
| 588 | GPT-4o Mini | 1 | OpenAI |
| 589 | distilbert | 1 | Pre-LLM / Encoder |
| 590 | MistralOrca | 1 | Other/Unknown |
| 591 | and other multilingual LLMs | 1 | Other/Unknown |
| 592 | GreekLegalRoBERTa | 1 | Other/Unknown |
| 593 | GreekLegalBERT | 1 | Other/Unknown |
| 594 | GreekLegalBERT-v2 | 1 | Other/Unknown |
| 595 | GreekBERT | 1 | Other/Unknown |
| 596 | Gemini Ultra | 1 | Google |
| 597 | Alpaca2 | 1 | Other/Unknown |
| 598 | Claude-3 Haiku | 1 | Anthropic |
| 599 | Claude-3 Sonnet | 1 | Anthropic |
| 600 | GPT 4-Turbo | 1 | Other/Unknown |
| 601 | LLama-3.2 | 1 | Other/Unknown |
| 602 | Mistral AI | 1 | Other/Unknown |
| 603 | Dolly-200 | 1 | Other/Unknown |
| 604 | GPT-3.5 TURBO | 1 | Other/Unknown |
| 605 | GPT-3.5-TURBO | 1 | Other/Unknown |
| 606 | QWEN-14B | 1 | Other/Unknown |
| 607 | QWEN-7B | 1 | Other/Unknown |
| 608 | Claude models | 1 | Other/Unknown |
| 609 | various LLM-as-a-Judge and reward models | 1 | Other/Unknown |
| 610 | Mixtral-8x22bB | 1 | Other/Unknown |
| 611 | ChatGLM 2 | 1 | Other/Unknown |
| 612 | Chatglm2 | 1 | Other/Unknown |
| 613 | Vicuna 1.5 | 1 | Other/Unknown |
| 614 | Flan-PaLM | 1 | Other/Unknown |
| 615 | gpt-4vision | 1 | Other/Unknown |
| 616 | GPT3.5 turbo | 1 | Other/Unknown |
| 617 | gemma 6.51 | 1 | Other/Unknown |
| 618 | internlm | 1 | Open-source (misc) |
| 619 | internlm2 | 1 | Other/Unknown |
| 620 | Qwen-based | 1 | Other/Unknown |
| 621 | llama-31 | 1 | Other/Unknown |
| 622 | qwen2vl | 1 | Other/Unknown |
| 623 | Barth4 | 1 | Other/Unknown |
| 624 | Vicuna-13 | 1 | Other/Unknown |
| 625 | Meltemi-7B | 1 | Other/Unknown |
| 626 | LlaMA3 | 1 | Other/Unknown |
| 627 | Phi-2 | 1 | Microsoft |
| 628 | Claude-3. | 1 | Other/Unknown |
| 629 | PaLM-22 | 1 | Other/Unknown |
| 630 | Vicuna4 | 1 | Other/Unknown |
| 631 | GPT3.5-Turbo | 1 | Other/Unknown |
| 632 | bloom | 1 | Open-source (misc) |
| 633 | Qwen-Chat9 | 1 | Other/Unknown |
| 634 | Qwen-max | 1 | Other/Unknown |
| 635 | Mistral-v2 | 1 | Other/Unknown |
| 636 | Mistral-v3 | 1 | Other/Unknown |
| 637 | Llama 0.4852 | 1 | Other/Unknown |
| 638 | LlaMa-3.1 | 1 | Other/Unknown |
| 639 | LlaMa-Guard | 1 | Other/Unknown |
| 640 | LLaMA1 | 1 | Other/Unknown |
| 641 | Mistral. 6 | 1 | Other/Unknown |
| 642 | Qwen-14b | 1 | Other/Unknown |
| 643 | ChatGLM series | 1 | Other/Unknown |
| 644 | Qwen and | 1 | Other/Unknown |
| 645 | Qwen se | 1 | Other/Unknown |
| 646 | Qwen series | 1 | Other/Unknown |
| 647 | Qwen-110B | 1 | Other/Unknown |
| 648 | Yi-6B | 1 | Other/Unknown |
| 649 | DeepseekV2 | 1 | Other/Unknown |
| 650 | llama-3.1 | 1 | Other/Unknown |
| 651 | SnakModel (Llama2-7B-based) | 1 | Other/Unknown |
| 652 | other Llama2-7B-based Danish models | 1 | Other/Unknown |
| 653 | LLAMA3.1 | 1 | Other/Unknown |
| 654 | DOLLY | 1 | Open-source (misc) |
| 655 | MIXTRAL-8X7B | 1 | Other/Unknown |
| 656 | internlm-chat | 1 | Other/Unknown |
| 657 | T5-model | 1 | Other/Unknown |
| 658 | Bloom 1B | 1 | Other/Unknown |
| 659 | Bloom-7B1 | 1 | Other/Unknown |
| 660 | QWEN-2.5 | 1 | Other/Unknown |
| 661 | Qwen_1_5B_instruct | 1 | Other/Unknown |
| 662 | Qwen_500M_instruct | 1 | Other/Unknown |
| 663 | Qwen_7B_instruct | 1 | Other/Unknown |
| 664 | Claude-2.1 | 1 | Other/Unknown |
| 665 | Deepseek 0 | 1 | Other/Unknown |
| 666 | Deepseek 79 | 1 | Other/Unknown |
| 667 | LLama 3.3 | 1 | Other/Unknown |
| 668 | Llama 0.072 | 1 | Other/Unknown |
| 669 | Llama 64.5 | 1 | Other/Unknown |
| 670 | Flan-T5-based | 1 | Other/Unknown |
| 671 | GPT4o-mini | 1 | Other/Unknown |
| 672 | opt125M_portuguese | 1 | Other/Unknown |
| 673 | Claude 312 | 1 | Other/Unknown |
| 674 | LLaMA 3.116 | 1 | Other/Unknown |
| 675 | Qwen-14B14 | 1 | Other/Unknown |
| 676 | claude-3-haiku | 1 | Other/Unknown |
| 677 | Llama2Chat | 1 | Other/Unknown |
| 678 | Llama3-Chat | 1 | Other/Unknown |
| 679 | EuroLLM | 1 | Other/Unknown |
| 680 | Teuken-7B | 1 | Other/Unknown |
| 681 | Salamandra | 1 | Other/Unknown |
| 682 | transformer-based models | 1 | Other/Unknown |
| 683 | BLOOMZ-7B | 1 | Other/Unknown |
| 684 | Lucie | 1 | Other/Unknown |
| 685 | Llama-3.1. | 1 | Other/Unknown |
| 686 | GEMMA 2 | 1 | Other/Unknown |
| 687 | Llama-3-70B | 1 | Other/Unknown |
| 688 | Llama-3-8B | 1 | Other/Unknown |
| 689 | Gemma-7B | 1 | Other/Unknown |
| 690 | GPT-4o-Mini | 1 | Other/Unknown |
| 691 | LlamA-3.2 | 1 | Other/Unknown |
| 692 | Mistral-3-24B | 1 | Other/Unknown |
| 693 | Claude1 | 1 | Other/Unknown |
| 694 | BLOOM-560 | 1 | Other/Unknown |
| 695 | DistilCamemBERT | 1 | Other/Unknown |
| 696 | DeHateBERT | 1 | Other/Unknown |
| 697 | Text-Davinci-003 | 1 | OpenAI |
| 698 | Vicuna-80 | 1 | Other/Unknown |
| 699 | GEMINI-Flash | 1 | Other/Unknown |
| 700 | LLaMA 50.0 | 1 | Other/Unknown |
| 701 | LLaMA 50.1 | 1 | Other/Unknown |
| 702 | LLaMA 67.2 | 1 | Other/Unknown |
| 703 | QwenScorer | 1 | Other/Unknown |
| 704 | LLaMA3.2 | 1 | Other/Unknown |
| 705 | Gemini-1.5-Pro | 1 | Other/Unknown |
| 706 | Llama-3.1-405B | 1 | Other/Unknown |
| 707 | Qwen2.5-72B | 1 | Other/Unknown |
| 708 | LLama-4 | 1 | Other/Unknown |
| 709 | LLaMA 8 | 1 | Other/Unknown |
| 710 | Mistral-Medium | 1 | Other/Unknown |
| 711 | claude-4. | 1 | Other/Unknown |
| 712 | baichuan-ai | 1 | Other/Unknown |
| 713 | InternLM-7B | 1 | Other/Unknown |
| 714 | LLAMA-2-Chat | 1 | Other/Unknown |
| 715 | Qwen3-4B | 1 | Other/Unknown |
| 716 | Gemini-2.5 | 1 | Other/Unknown |
| 717 | T5-like | 1 | Other/Unknown |
| 718 | llama-3.3 | 1 | Other/Unknown |
| 719 | llama3.2 | 1 | Other/Unknown |
| 720 | qwen2.5 | 1 | Other/Unknown |
| 721 | T5 17 | 1 | Other/Unknown |
| 722 | Bartz | 1 | Other/Unknown |
| 723 | LLaMA-4. | 1 | Other/Unknown |
| 724 | MISTRAL LARGE | 1 | Other/Unknown |
| 725 | MISTRAL-X | 1 | Other/Unknown |
| 726 | BERTu | 1 | Other/Unknown |
| 727 | mBERTu | 1 | Other/Unknown |
| 728 | Phi-4 56 | 1 | Other/Unknown |
| 729 | gemini-1.5-flash | 1 | Other/Unknown |
| 730 | T5-large | 1 | Other/Unknown |
| 731 | Falcon 3 | 1 | Other/Unknown |
| 732 | Llama 1 | 1 | Other/Unknown |
| 733 | Qwen 1.8B | 1 | Other/Unknown |
| 734 | Deepseek Reasoner | 1 | Other/Unknown |
| 735 | DeepseekR | 1 | Other/Unknown |
| 736 | DeepseekRa | 1 | Other/Unknown |
| 737 | DeepseekRi | 1 | Other/Unknown |
| 738 | DeepseekRin_grok2a_blindi | 1 | Other/Unknown |
| 739 | DeepseekRin_o3 | 1 | Other/Unknown |
| 740 | DeepseekRn_mistrala_blindi | 1 | Other/Unknown |
| 741 | DeepseekRn_o3 | 1 | Other/Unknown |
| 742 | Grok 2 | 1 | Other/Unknown |
| 743 | Grok-2 | 1 | Other/Unknown |
| 744 | Grok2 | 1 | Other/Unknown |
| 745 | Mistral 0.80 0 | 1 | Other/Unknown |
| 746 | Mistrala | 1 | Other/Unknown |
| 747 | Mistrali | 1 | Other/Unknown |
| 748 | mistraln_DeepseekRa_LLMi | 1 | Other/Unknown |
| 749 | mistraln_DeepseekRa_blindi | 1 | Other/Unknown |
| 750 | mistraln_DeepseekRa_person | 1 | Other/Unknown |
| 751 | mistraln_DeepseekRa_personi | 1 | Other/Unknown |
| 752 | mistraln_grok2a_blindi | 1 | Other/Unknown |
| 753 | mistraln_mistrala_DeepseekRi | 1 | Other/Unknown |
| 754 | mistraln_mistrala_blindi | 1 | Other/Unknown |
| 755 | mistraln_mistrala_grok2i | 1 | Other/Unknown |
| 756 | mistraln_mistrala_mistrali | 1 | Other/Unknown |
| 757 | mistraln_mistrala_o3 | 1 | Other/Unknown |
| 758 | Mistral 44.5 58 | 1 | Other/Unknown |
| 759 | Mistral-Saba | 1 | Other/Unknown |
| 760 | Claude3-Opus | 1 | Other/Unknown |
| 761 | Claude3-Sonnet | 1 | Other/Unknown |
| 762 | LLaMA2Chat | 1 | Other/Unknown |
| 763 | Falcon-H1 | 1 | Other/Unknown |
| 764 | Mistral 31.65 80 | 1 | Other/Unknown |
| 765 | Mistral 368.0 5 | 1 | Other/Unknown |
| 766 | Phi-2 33 | 1 | Other/Unknown |
| 767 | Phi-4 14B | 1 | Other/Unknown |
| 768 | Command-r | 1 | Cohere |
| 769 | Claude-3.5-haiku | 1 | Other/Unknown |
| 770 | Llama 2 chat | 1 | Other/Unknown |
| 771 | Mistral- Large | 1 | Other/Unknown |
| 772 | phi-1 1 | 1 | Other/Unknown |
| 773 | T5 Base | 1 | Other/Unknown |
| 774 | T5-styled | 1 | Other/Unknown |
| 775 | Claude-3-haiku | 1 | Other/Unknown |
| 776 | DEEPSEEK-V3 | 1 | Other/Unknown |
| 777 | GROK 4 | 1 | Other/Unknown |
| 778 | QWEN-PLUS | 1 | Other/Unknown |
| 779 | grok-4 | 1 | Other/Unknown |
| 780 | DeepSeekV3 | 1 | Other/Unknown |
| 781 | Claude-haiku | 1 | Other/Unknown |
| 782 | Mistral L2 | 1 | Other/Unknown |
| 783 | BART 0 | 1 | Other/Unknown |
| 784 | DeBERTa 0 | 1 | Other/Unknown |
| 785 | T5 0 | 1 | Other/Unknown |
| 786 | Mistral- large | 1 | Other/Unknown |
| 787 | Claude 131 | 1 | Other/Unknown |
| 788 | GPT 4 Turbo | 1 | Other/Unknown |
| 789 | Llama 3. | 1 | Other/Unknown |
| 790 | Bloomsbury | 1 | Other/Unknown |
| 791 | Gemini 2.5 Flash | 1 | Other/Unknown |
| 792 | Grok3 | 1 | Other/Unknown |
| 793 | LLaMA3.3 | 1 | Other/Unknown |
| 794 | LLamaGuard | 1 | Other/Unknown |
| 795 | gpt4 | 1 | Other/Unknown |
| 796 | Gemini-2.0-Flash | 1 | Other/Unknown |
| 797 | BLOOM 251 | 1 | Other/Unknown |
| 798 | BLOOM 35 | 1 | Other/Unknown |
| 799 | BLOOM 48 | 1 | Other/Unknown |
| 800 | BLOOM 83 | 1 | Other/Unknown |
| 801 | LLaMA 23.26 | 1 | Other/Unknown |
| 802 | LLaMA 32 | 1 | Other/Unknown |
| 803 | LLaMA 38.10 | 1 | Other/Unknown |
| 804 | LLaMA 45.65 | 1 | Other/Unknown |
| 805 | LLaMA 5.38 | 1 | Other/Unknown |
| 806 | LLaMA 50.00 | 1 | Other/Unknown |
| 807 | LLaMA 6.26 | 1 | Other/Unknown |
| 808 | LLaMA 7.09 | 1 | Other/Unknown |
| 809 | LLaMA 76.6 | 1 | Other/Unknown |
| 810 | T5-LM | 1 | Other/Unknown |
| 811 | bloom-7b1 | 1 | Other/Unknown |
| 812 | Claude 3.74 | 1 | Other/Unknown |
| 813 | Falcon 23 | 1 | Other/Unknown |
| 814 | Falcon 24 | 1 | Other/Unknown |
| 815 | Falcon 27 | 1 | Other/Unknown |
| 816 | Falcon-3 | 1 | Other/Unknown |
| 817 | Gemma 24.87 | 1 | Other/Unknown |
| 818 | Gemma 29.26 | 1 | Other/Unknown |
| 819 | Gemma 41.94 | 1 | Other/Unknown |
| 820 | Qwen 26.63 | 1 | Other/Unknown |
| 821 | Qwen 39.64 | 1 | Other/Unknown |
| 822 | Qwen 40.58 | 1 | Other/Unknown |
| 823 | Internlm2 | 1 | Other/Unknown |
| 824 | LLaMA-31 | 1 | Other/Unknown |
| 825 | internlm25 | 1 | Other/Unknown |
| 826 | DeepSeek Chat | 1 | Other/Unknown |
| 827 | DeepSeek Reasoner | 1 | Other/Unknown |
| 828 | Phi-4 and | 1 | Other/Unknown |
| 829 | o1-preview | 1 | OpenAI |
| 830 | LLama-Guard | 1 | Other/Unknown |
| 831 | Claude 1.00 | 1 | Other/Unknown |
| 832 | Claude 11.5 | 1 | Other/Unknown |
| 833 | Claude 42.7 | 1 | Other/Unknown |
| 834 | DeepSeek 0 | 1 | Other/Unknown |
| 835 | Grok 0 | 1 | Other/Unknown |
| 836 | Qwen 28.6 | 1 | Other/Unknown |
| 837 | Qwen 37.1 | 1 | Other/Unknown |
| 838 | WizardLM 0 | 1 | Other/Unknown |
| 839 | bloomz | 1 | Other/Unknown |
| 840 | Qwen 0.60 | 1 | Other/Unknown |
| 841 | Qwen25 | 1 | Other/Unknown |
| 842 | Qwen-7B5 | 1 | Other/Unknown |
| 843 | Qwen-Plus | 1 | Other/Unknown |
| 844 | Mistral among | 1 | Other/Unknown |
| 845 | Mistral- 7b | 1 | Other/Unknown |
| 846 | Claude 4.5 | 1 | Other/Unknown |
| 847 | Claude- Haiku | 1 | Other/Unknown |
| 848 | Claude-4.5 | 1 | Other/Unknown |
| 849 | Claude-4.5. | 1 | Other/Unknown |
| 850 | DeepSeek-3 | 1 | Other/Unknown |
| 851 | Grok4 | 1 | Other/Unknown |
| 852 | Mistral3.1-24B | 1 | Other/Unknown |
| 853 | Mistral- 3 | 1 | Other/Unknown |
| 854 | Mistral-24B | 1 | Other/Unknown |
| 855 | Mistral-3.1-24B | 1 | Other/Unknown |
| 856 | Phi3-medium | 1 | Other/Unknown |
| 857 | gpt3 | 1 | Other/Unknown |
| 858 | Mistral small | 1 | Other/Unknown |
| 859 | Mistral. 2025 | 1 | Other/Unknown |
| 860 | Claude4 | 1 | Other/Unknown |
| 861 | GPT-4-mini | 1 | Other/Unknown |
| 862 | Aya | 1 | Cohere |
| 863 | LLaMa 3 | 1 | Other/Unknown |
| 864 | Mistral 3 | 1 | Other/Unknown |
| 865 | Qwen 3B | 1 | Other/Unknown |
| 866 | Claude 96.5 | 1 | Other/Unknown |
| 867 | claude-3-opus | 1 | Other/Unknown |
| 868 | t5 4 | 1 | Other/Unknown |
| 869 | distilBERT | 1 | Pre-LLM / Encoder |
| 870 | Mistral 0.3 Instruct | 1 | Other/Unknown |
| 871 | Mistral 0.3 57 | 1 | Other/Unknown |
| 872 | Mistral 0.3 68 | 1 | Other/Unknown |
| 873 | Qwen 494M | 1 | Other/Unknown |
| 874 | Deepseek 4o | 1 | Other/Unknown |
| 875 | Deepseek R1 | 1 | Other/Unknown |
| 876 | LLama1 | 1 | Other/Unknown |
| 877 | LLama2 | 1 | Other/Unknown |
| 878 | Llama-2-CHAT | 1 | Other/Unknown |
| 879 | mistral 30 35 | 1 | Other/Unknown |
| 880 | LLaMA 93.99 | 1 | Other/Unknown |
| 881 | LLaMA3.1. | 1 | Other/Unknown |
| 882 | Claude 4 Opus | 1 | Other/Unknown |
| 883 | LLama-3.3 | 1 | Other/Unknown |
| 884 | QWEN 3 | 1 | Other/Unknown |
| 885 | Llama 11 | 1 | Other/Unknown |
| 886 | Llama 8 | 1 | Other/Unknown |
| 887 | Mistral 2410 4 | 1 | Other/Unknown |
| 888 | Mistral 24B | 1 | Other/Unknown |
| 889 | Mistral 2501 5 | 1 | Other/Unknown |
| 890 | Mistral- 2410 | 1 | Other/Unknown |
| 891 | Mistral-2501 24B | 1 | Other/Unknown |
| 892 | Llama-70B | 1 | Other/Unknown |
| 893 | GLM-4 | 1 | Other/Unknown |
| 894 | EXAONE | 1 | Other/Unknown |
| 895 | Plutus-8B | 1 | Other/Unknown |
| 896 | CLAUDE 3.5 SONNET | 1 | Other/Unknown |
| 897 | CLAUDE-3 HAIKU | 1 | Anthropic |
| 898 | CLAUDE-3-HAIKU | 1 | Other/Unknown |
| 899 | Claude 3.5-sonnet | 1 | Other/Unknown |
| 900 | Claude Haiku | 1 | Other/Unknown |
| 901 | Claude-sonnet | 1 | Other/Unknown |
| 902 | MISTRAL-7B | 1 | Other/Unknown |
| 903 | QWEN-32B | 1 | Other/Unknown |
| 904 | Llama 32.20 | 1 | Other/Unknown |
| 905 | Llama 34.80 | 1 | Other/Unknown |
| 906 | Llama 4.40 | 1 | Other/Unknown |
| 907 | Llama 4.98 | 1 | Other/Unknown |
| 908 | Llama 69.19 | 1 | Other/Unknown |
| 909 | Llama 69.7 | 1 | Other/Unknown |
| 910 | Llama 72.7 | 1 | Other/Unknown |
| 911 | Llama 77.13 | 1 | Other/Unknown |
| 912 | BART Counterfactual | 1 | Other/Unknown |
| 913 | BART-base | 1 | Other/Unknown |
| 914 | DeBERTa NLI | 1 | Other/Unknown |
| 915 | Falcon Instruct | 1 | Other/Unknown |
| 916 | Flan-T5 NLI | 1 | Other/Unknown |
| 917 | LLaMA 2 Chat | 1 | Other/Unknown |
| 918 | LLaMa2 | 1 | Other/Unknown |
| 919 | OPT6 | 1 | Other/Unknown |
| 920 | Phi-3-3 | 1 | Other/Unknown |
| 921 | T5 Answer | 1 | Other/Unknown |
| 922 | T5 NLI | 1 | Other/Unknown |
| 923 | T5 Word | 1 | Other/Unknown |
| 924 | T5-small | 1 | Other/Unknown |
| 925 | T500 | 1 | Other/Unknown |
| 926 | llama2.70 | 1 | Other/Unknown |
| 927 | llama2.70. chat | 1 | Other/Unknown |
| 928 | mixtral 8x7b | 1 | Other/Unknown |
| 929 | Minerva-3B | 1 | Other/Unknown |
| 930 | Zefiro | 1 | Other/Unknown |
| 931 | Llama-Krikri-8B | 1 | Other/Unknown |
| 932 | Meltemi | 1 | Other/Unknown |
| 933 | Barton | 1 | Other/Unknown |
| 934 | Claude haiku | 1 | Other/Unknown |
| 935 | claude3. | 1 | Other/Unknown |
| 936 | Mistral 7BInstruct | 1 | Other/Unknown |
| 937 | Falcon-Arabic | 1 | Other/Unknown |
| 938 | deepseek-coder | 1 | DeepSeek |
| 939 | deepseek-v2 | 1 | DeepSeek |
| 940 | Claude- Sonnet | 1 | Other/Unknown |
| 941 | Claude-4.1-Opus | 1 | Other/Unknown |
| 942 | DeepSeek-Chat | 1 | Other/Unknown |
| 943 | LLaMa-3.3 | 1 | Other/Unknown |
| 944 | Mistral12b | 1 | Other/Unknown |
| 945 | Dolly24 | 1 | Other/Unknown |
| 946 | Mistral 0.74 2 | 1 | Other/Unknown |
| 947 | Mistral 11.47 69 | 1 | Other/Unknown |
| 948 | Qwen 0.12 | 1 | Other/Unknown |
| 949 | Qwen 0.90 | 1 | Other/Unknown |
| 950 | Gemini 2.0 flash | 1 | Other/Unknown |
| 951 | LlaMA 2 | 1 | Other/Unknown |
| 952 | Qwen et | 1 | Other/Unknown |
| 953 | chatglm-6b | 1 | Other/Unknown |
| 954 | falcon-40b | 1 | Other/Unknown |
| 955 | t5-3b | 1 | Other/Unknown |
| 956 | vicuna | 1 | Open-source (misc) |
| 957 | deepseek-vl2 | 1 | Other/Unknown |
| 958 | mistral-nemo | 1 | Other/Unknown |
| 959 | qwen-3 | 1 | Other/Unknown |
| 960 | Gemma-2. | 1 | Other/Unknown |
| 961 | LLaMA 3.2. | 1 | Other/Unknown |
| 962 | DeBERTa-based | 1 | Other/Unknown |
| 963 | T5TokenizerFast | 1 | Other/Unknown |
| 964 | WizardLM-2 | 1 | Other/Unknown |
| 965 | DeepSeek 67B | 1 | Other/Unknown |
| 966 | qwen2 | 1 | Other/Unknown |
| 967 | Ernie | 1 | Open-source (misc) |
| 968 | GPT-4O-MINI | 1 | Other/Unknown |
| 969 | LLAMA3 | 1 | Other/Unknown |
| 970 | gemma-1.1 | 1 | Other/Unknown |
| 971 | Claude 2. | 1 | Other/Unknown |
| 972 | LLaMA-2 Chat | 1 | Other/Unknown |
| 973 | Qwen-family | 1 | Other/Unknown |
| 974 | Phi4 0 | 1 | Other/Unknown |
| 975 | Phi4-14B | 1 | Other/Unknown |
| 976 | DeepSeek-70B | 1 | Other/Unknown |
| 977 | BARTL | 1 | Other/Unknown |
| 978 | LLaMA2-Chat | 1 | Other/Unknown |
| 979 | mixtral-8x7b | 1 | Other/Unknown |
| 980 | CodeLLaMA | 1 | Meta |
| 981 | Qwen MMMLU | 1 | Other/Unknown |
| 982 | LLAMA 4 | 1 | Other/Unknown |
| 983 | Phi-4-mini | 1 | Other/Unknown |
| 984 | Alpaca-2 | 1 | Other/Unknown |
| 985 | GPT 4O | 1 | Other/Unknown |
| 986 | LlaMA 3.1 | 1 | Other/Unknown |
| 987 | LlaMA-3.1 | 1 | Other/Unknown |
| 988 | Qwen 3.5 | 1 | Other/Unknown |
| 989 | codellama 22 | 1 | Other/Unknown |
| 990 | deepseek6 | 1 | Other/Unknown |
| 991 | llama 24 | 1 | Other/Unknown |
| 992 | qwen-13b | 1 | Other/Unknown |
| 993 | qwen-7b | 1 | Other/Unknown |
| 994 | DeepSeek-GRM | 1 | Other/Unknown |
| 995 | Qwen-Instruct | 1 | Other/Unknown |
| 996 | Claude-4-sonnet | 1 | Other/Unknown |
| 997 | DeepSeek 29 | 1 | Other/Unknown |
| 998 | llama-guard | 1 | Other/Unknown |
| 999 | llamaguard | 1 | Other/Unknown |
| 1000 | phi-3 | 1 | Microsoft |
| 1001 | Deepseek-V3 | 1 | Other/Unknown |
| 1002 | DeBERTa V2 | 1 | Other/Unknown |
| 1003 | DeBERTa-base | 1 | Other/Unknown |
| 1004 | Poro-34B | 1 | Other/Unknown |
| 1005 | multilingual and Basque-adapted LLMs | 1 | Other/Unknown |
| 1006 | Cohere-Aya | 1 | Other/Unknown |
| 1007 | claude-3.5 | 1 | Other/Unknown |
| 1008 | claude-3.5 Sonnet | 1 | Other/Unknown |
| 1009 | llama 70. | 1 | Other/Unknown |
| 1010 | llama3.3 | 1 | Other/Unknown |
| 1011 | OLMo | 1 | Other/Unknown |
| 1012 | BLOOM72 | 1 | Other/Unknown |
| 1013 | Claude 3.5 sonnet | 1 | Other/Unknown |
| 1014 | DeepSeek-R126 | 1 | Other/Unknown |
| 1015 | DeepSeek-V327 | 1 | Other/Unknown |
| 1016 | DeepSeek-based | 1 | Other/Unknown |
| 1017 | Deepseek-r1 | 1 | Other/Unknown |
| 1018 | Deepseek-v3 | 1 | Other/Unknown |
| 1019 | LLaMA-224 | 1 | Other/Unknown |
| 1020 | LLaMA23 | 1 | Other/Unknown |
| 1021 | Qwen Family28 | 1 | Other/Unknown |
| 1022 | Qwen2.530 | 1 | Other/Unknown |
| 1023 | phi-3 47 | 1 | Other/Unknown |
| 1024 | phi-4 18 | 1 | Other/Unknown |
| 1025 | o3-pro | 1 | Other/Unknown |
| 1026 | Gemma 35.15 | 1 | Other/Unknown |
| 1027 | Gemma 35.31 | 1 | Other/Unknown |
| 1028 | Gemma 69.37 | 1 | Other/Unknown |
| 1029 | Phi-4-14B | 1 | Other/Unknown |
| 1030 | llama3. | 1 | Other/Unknown |
| 1031 | Dolly 7. | 1 | Other/Unknown |
| 1032 | deepseek-ai | 1 | Other/Unknown |
| 1033 | Mistral-medium | 1 | Other/Unknown |
| 1034 | Mistral-small | 1 | Other/Unknown |
| 1035 | Deepseek-3 | 1 | Other/Unknown |
| 1036 | Qwen-3.1 | 1 | Other/Unknown |
| 1037 | Qwen-MT | 1 | Other/Unknown |
| 1038 | claude 3.7 sonnet | 1 | Other/Unknown |
| 1039 | deepseek llama3 | 1 | Other/Unknown |
| 1040 | deepseek chat | 1 | Other/Unknown |
| 1041 | qwen 2.5 | 1 | Other/Unknown |
| 1042 | Qwen-SEA_LION | 1 | Other/Unknown |
| 1043 | GPT-OSS | 1 | Other/Unknown |
| 1044 | LLama 4 | 1 | Other/Unknown |
| 1045 | Claude 3.7 sonnet | 1 | Other/Unknown |
| 1046 | LLaMa-3.1. | 1 | Other/Unknown |
| 1047 | LLama 3.1 | 1 | Other/Unknown |
| 1048 | Mistral- 24 | 1 | Other/Unknown |
| 1049 | Mistral-24.07 | 1 | Other/Unknown |
| 1050 | Qwen-3B | 1 | Other/Unknown |
| 1051 | 80+ open- and closed-source LLMs | 1 | Other/Unknown |
| 1052 | Falcon-h1 | 1 | Other/Unknown |
| 1053 | Qwen R1 | 1 | Other/Unknown |

### 2.2 Model Family Grouping

Papers per model family (a paper is counted once per family even if it uses multiple models from that family):

| Rank | Family | Papers | % of Assessed |
|-----:|--------|-------:|--------------:|
| 1 | OpenAI | 946 | 66.2% |
| 2 | Meta | 697 | 48.8% |
| 3 | Other/Unknown | 552 | 38.7% |
| 4 | Pre-LLM / Encoder | 545 | 38.2% |
| 5 | Google | 454 | 31.8% |
| 6 | Alibaba | 315 | 22.1% |
| 7 | Anthropic | 300 | 21.0% |
| 8 | Mistral AI | 288 | 20.2% |
| 9 | Open-source (misc) | 231 | 16.2% |
| 10 | DeepSeek | 169 | 11.8% |
| 11 | Embeddings | 62 | 4.3% |
| 12 | Microsoft | 47 | 3.3% |
| 13 | xAI | 32 | 2.2% |
| 14 | Cohere | 18 | 1.3% |

### 2.3 Proprietary vs Open-Source Breakdown

**By model mention count** (each model×paper counts once):

| Category | Mentions | % |
|----------|--------:|---------:|
| Proprietary (closed-source) | 2363 | 26.6% |
| Open-source / open-weight | 6521 | 73.4% |
| **Total** | **8884** | **100%** |

**By paper count** (papers using at least one model of that type):

| Category | Papers |
|----------|-------:|
| Uses at least one proprietary model | 947 |
| Uses at least one open-source model | 1312 |

### 2.4 Models Per Paper Distribution

Among the 1428 papers with LLM models identified:

| Models per paper | Papers | % |
|:----------------:|-------:|------:|
| 1 | 216 | 15.1% |
| 2-3 | 348 | 24.4% |
| 4-6 | 390 | 27.3% |
| 7+ | 474 | 33.2% |

### 2.5 Model Co-Occurrence Matrix (Top 12)

How often the top 12 models appear together in the same paper:

| | GPT-4 | BERT | Llama | Llama-3 | Qwen | ChatGPT | Claude | GPT-3.5 | Mistral | Gemma | GPT-4o | GPT-3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **GPT-4** | — | 139 | 234 | 225 | 191 | 186 | 229 | 231 | 161 | 138 | 138 | 152 |
| **BERT** | 139 | — | 138 | 50 | 45 | 99 | 45 | 68 | 45 | 61 | 77 | 99 |
| **Llama** | 234 | 138 | — | 100 | 114 | 134 | 100 | 88 | 90 | 114 | 128 | 115 |
| **Llama-3** | 225 | 50 | 100 | — | 172 | 54 | 118 | 94 | 146 | 117 | 81 | 38 |
| **Qwen** | 191 | 45 | 114 | 172 | — | 47 | 120 | 71 | 114 | 111 | 89 | 35 |
| **ChatGPT** | 186 | 99 | 134 | 54 | 47 | — | 69 | 82 | 43 | 40 | 57 | 106 |
| **Claude** | 229 | 45 | 100 | 118 | 120 | 69 | — | 84 | 83 | 58 | 80 | 41 |
| **GPT-3.5** | 231 | 68 | 88 | 94 | 71 | 82 | 84 | — | 70 | 42 | 44 | 124 |
| **Mistral** | 161 | 45 | 90 | 146 | 114 | 43 | 83 | 70 | — | 90 | 39 | 25 |
| **Gemma** | 138 | 61 | 114 | 117 | 111 | 40 | 58 | 42 | 90 | — | 68 | 34 |
| **GPT-4o** | 138 | 77 | 128 | 81 | 89 | 57 | 80 | 44 | 39 | 68 | — | 58 |
| **GPT-3** | 152 | 99 | 115 | 38 | 35 | 106 | 41 | 124 | 25 | 34 | 58 | — |

---

## 3. Data Availability Analysis

### 3.1 URL Presence Statistics

| Status | Papers | % |
|--------|-------:|------:|
| Has public data URL | 1205 | 60.0% |
| No data URL (NA) | 803 | 40.0% |

### 3.2 Hosting Platform Breakdown

Among papers with data URLs, classified by hosting platform:

| Platform | Papers | % of URLs |
|----------|-------:|----------:|
| GitHub | 796 | 66.1% |
| HuggingFace | 240 | 19.9% |
| Other | 109 | 9.0% |
| OSF | 23 | 1.9% |
| Zenodo | 15 | 1.2% |
| Kaggle | 13 | 1.1% |
| Anonymous (review) | 8 | 0.7% |
| Mendeley Data | 6 | 0.5% |
| GitLab | 5 | 0.4% |
| DOI/Repository | 2 | 0.2% |
| Papers With Code | 2 | 0.2% |

### 3.3 Overlap: LLM Models AND Data URLs

| Combination | Papers | % |
|-------------|-------:|------:|
| LLM models + data URL | 994 | 49.5% |
| LLM models only (no URL) | 434 | 21.6% |
| Data URL only (no models) | 211 | 10.5% |
| Neither | 369 | 18.4% |

---

## 4. Gap Analysis

### 4.1 Papers with LLM Models but No Public Data URL

**434 papers** assess LLM models but have no publicly available data URL.

<details>
<summary>Click to expand (434 papers)</summary>

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
| 32 | [[2022-Zagar-Slovene SuperGLUE Benchmark Translation and Evaluation]] | BERT, RoBERTa |
| 33 | [[2023-Arora-Probing PLMs for Cross-Cultural Values C3NLP Workshop]] | BERT |
| 34 | [[2023-Avetisyan-Large Language Models and Low-Resource Languages An Examination of]] | BERT, RoBERTa |
| 35 | [[2023-Bang-Towards Answering Open-ended Ethical Quandary]] | BERT |
| 36 | [[2023-Benkler-Assessing LLMs for Moral Value Pluralism]] | RoBERTa |
| 37 | [[2023-Catapang-EMoTES-3K]] | RoBERTa, Flan-T5 |
| 38 | [[2023-Chang-niceNLP at SemEval-2023 Task 10]] | DeBERTa, RoBERTa, BERT |
| 39 | [[2023-Chen-Case Law Grounding]] | GPT-4 |
| 40 | [[2023-Davis-Benchmarks for Automated Commonsense Reasoning]] | BERT, ChatGPT, GPT-3 |
| 41 | [[2023-Dehghani-Persian Offensive Language Detection Dehghani et al.]] | BERT, ELMo, GPT3, GloVe, RoBERTa, Word2Vec |
| 42 | [[2023-Deng-Probing the Moral Development of Large Language]] | GPT-3, GPT-3.5, GPT-4, ChatGPT, PaLM-2, Llama-2 |
| 43 | [[2023-Ghosh-ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores]] | ChatGPT, BERT |
| 44 | [[2023-Hartmann-The political ideology of conversational AI]] | ChatGPT |
| 45 | [[2023-Hämmerl-Speaking Multiple Languages Affects the Moral Bias of Language Models]] | BERT, RoBERTa |
| 46 | [[2023-Karra-Estimating the Personality of White-Box Language]] | GPT-2, GPT-3, GPT-3.5, Llama, XLNet |
| 47 | [[2023-Li-On the steerability of large language models]] | Falcon |
| 48 | [[2023-Lima-A Call for a Research Agenda on Fair NLP for Portuguese]] | word2vec |
| 49 | [[2023-Mager-Neural Machine Translation for the Indigenous Languages of the]] | BART, BERT, ELMO, Gemma |
| 50 | [[2023-Morris-Levels of AGI]] | ALBERT, GPT-4, Llama 2 |
| 51 | [[2023-Munn-The Five Tests Designing and Evaluating]] | Falconer |
| 52 | [[2023-Nguyen-Abusive Span Detection for Vietnamese Narrative Texts]] | BERT, RoBERTa |
| 53 | [[2023-Nguyen-RMDM A Multilabel Fakenews Dataset for Vietnamese Evidence]] | BERT, ChatGPT, GPT 3, GPT 3.5, GPT-3, GPT-3.5, GPT-4 |
| 54 | [[2023-Nguyen-VinaLLaMA LLaMA-based Vietnamese Foundation Model]] | BLOOM, BLOOM-7B, BLOOMZ, ChatGPT, GPT-3, GPT-3.5, GPT-4, ... |
| 55 | [[2023-Park-AI Deception]] | ChatGPT, GPT-3, GPT-3.5, GPT-4 |
| 56 | [[2023-Plaza-del-Arco-MarIA and BETO are Sexist Evaluating Gender Bias in Large Language]] | ALBERT, BERT, Bartl, ELECTRA, RoBERTa |
| 57 | [[2023-Qian-Understanding Chinese Moral Stories with Further]] | BERT, RoBERTa, T5 |
| 58 | [[2023-Rao-Ethical Reasoning over Moral Alignment]] | GPT-4, GPT-3.5, GPT-3 |
| 59 | [[2023-Rystrøm-Apolitical Intelligence]] | ChatGPT, GPT-3, GPT-4 |
| 60 | [[2023-Rytting-Towards Coding Social Science Datasets with]] | GPT-3 |
| 61 | [[2023-Sabane-Breaking Language Barriers A Question-Answering Dataset]] | BERT, RoBERTa |
| 62 | [[2023-Schulhoff-HackAPrompt]] | GPT-3, ChatGPT, Flan-T5 |
| 63 | [[2023-Shalumov-HeRo RoBERTa and Longformer Hebrew Language Models]] | BERT, RoBERTa |
| 64 | [[2023-Trepczynski-Religion Theology and Philosophical Skills of]] | ChatGPT, Codex, Llama2, Llama2. |
| 65 | [[2023-University-Harmful Communication Detection of Toxic Language and Threats on]] | CroSloEngual BERT |
| 66 | [[2023-Unknown-Toxicity Posts and Hateful Comments Detection]] | BERT |
| 67 | [[2023-Varshney-Muslim-Violence Bias Persists in Debiased GPT]] | ChatGPT, GPT-3, InstructGPT |
| 68 | [[2023-Vida-Values, Ethics, Morals]] | BERT |
| 69 | [[2023-Zhang-Heterogeneous Value Alignment Evaluation for]] | GPT-4, GPT-3.5, ChatGPT, Claude, Llama, Alpaca, Vicuna |
| 70 | [[2023-Zhao-GPTBIAS A Comprehensive Framework for Evaluating]] | BLOOM, BLOOM 0, BLOOM 3, BLOOMZ, ChatGPT, GPT-3, GPT-4, L... |
| 71 | [[2024-Adelani-IrokoBench - A Benchmark for African Languages in the Age of LLMs]] | GPT-4, GPT-3.5, Gemma, Claude, Llama-3, BLOOM |
| 72 | [[2024-Adelani-Uhura A Benchmark for Evaluating Scientific]] | Alpaca, Claude, Claude Sonnet, Claude 3.5, Claude 3.5 Son... |
| 73 | [[2024-Agarwal-Ethical Reasoning Depends on Language]] | GPT-4, ChatGPT, Llama-2 |
| 74 | [[2024-Aksoy-Whose Morality Do They Speak]] | GPT-3.5, GPT-4, Llama-3, Mistral |
| 75 | [[2024-Altenburger-Examining the Role of Relationship Alignment in]] | Llama-3 |
| 76 | [[2024-Aly-Hate speech detection with ADHAR a multi-dialectal hate speech corpus]] | BERT, RoBERTa |
| 77 | [[2024-Amano-Exploring Similarity Measures and Intertextuality in]] | BERT, Word2Vec |
| 78 | [[2024-Aydin-Improving LLM Reliability with RAG in]] | ChatGPT, DeepSeek, Gemma, Llama, Mistral, Qwen |
| 79 | [[2024-Bang-Measuring Political Bias in LLMs What Is Said and How It Is Said]] | Llama-2, Vicuna, Falcon, Mistral |
| 80 | [[2024-Bean-Measuring What Matters - Construct Validity in LLM Benchmarks]] | GPT-4, GPT-4o mini |
| 81 | [[2024-Biedma-Beyond Human Norms]] | GPT-4, GPT-3.5, Llama-2, Mistral, Vicuna |
| 82 | [[2024-Bignotti-Legal Minds, Algorithmic Decisions]] | GPT-4 |
| 83 | [[2024-Cahyawijaya-High-Dimension Human Value Representation in]] | ChatGPT, Llama-2, Llama-3, Mistral, Mixtral, BLOOM |
| 84 | [[2024-Cao-The Moral Foundations Weibo Corpus]] | GPT-4, Llama-3, Qwen |
| 85 | [[2024-Caputo-Rules, Cases, and Reasoning]] | Claude |
| 86 | [[2024-Chakravarthi-Findings of the Shared Task on]] | BERT, RoBERTa |
| 87 | [[2024-Charfi-A Web-Based Hate Speech Detection System for Dialectal Arabic]] | BERT, RoBERTa |
| 88 | [[2024-Chen-EmotionQueen A Benchmark for Evaluating Empathy of Large Language]] | GPT-4, GPT-3.5, Claude, Llama-2, BLOOM, Falcon, Vicuna |
| 89 | [[2024-Chua-AI Safety in Generative AI Large Language Models]] | BERT, BLOOM, Bart, ChatGPT, GPT-4, Llama, Zephyr |
| 90 | [[2024-Das-The 'Colonial Impulse' of Natural Language Processing An Audit of]] | T5 |
| 91 | [[2024-Dawson-Evaluating Cultural Awareness of LLMs for]] | GPT-4o, GPT-4o mini, GPT-4o-mini, Gemma |
| 92 | [[2024-Dognin-Contextual Moral Value Alignment Through]] | Llama-2 |
| 93 | [[2024-Faisal-Dialectal Toxicity Detection Evaluating LLM-as-a-Judge Consistency]] | Mistral-NEMO, Phi-3, Phi-3 49, Phi-3 Mini, Phi-3-mini |
| 94 | [[2024-Fetahi-AI-Based Hate Speech Detection in Albanian Social Media New Dataset]] | mBERT, XLM-RoBERTa |
| 95 | [[2024-Fitzgerald-Some Issues in Predictive Ethics Modeling]] | RoBERTa |
| 96 | [[2024-Freire-Uncovering Latent Human Wellbeing in Language]] | GPT-3, DeBERTa, BERT |
| 97 | [[2024-Garcia-The Moral Turing Test]] | GPT-3.5 |
| 98 | [[2024-Grigoreva-RuBia A Russian Language Bias Detection Dataset]] | BERT, ChatGPT, GPT-3, GPT-3.5-turbo, RoBERTa |
| 99 | [[2024-Gupta-Improving Model Evaluation using SMART Filtering]] | Qwen, Llama-3, Gemma, Phi, Mixtral |
| 100 | [[2024-Gómez-Adorno-Overview of HOMO-MEX at IberLEF 2024 Hate Speech Detection Towards]] | BERT, GPT2, GloVE, RoBERTa |
| 101 | [[2024-Hendrycks-Introduction to AI Safety, Ethics, and Society]] | BERT, ChatGPT, GPT-4, Llama-2 |
| 102 | [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]] | ALBERT, GPT-4, GPT-4o, Llama, Llama3, Mistral-7b, BERT |
| 103 | [[2024-Huang-Collective Constitutional AI Aligning a Language Model with Public]] | Claude |
| 104 | [[2024-Isbarov-Open foundation models for Azerbaijani language]] | BERT, DeBERTa-Base, RoBERTa |
| 105 | [[2024-Jadhav-On Limitations of LLM as Annotator for Low Resource Languages Marathi]] | ALBERT, BERT, ChatGPT, GPT-3, GPT-4, GPT-4 Turbo, GPT-4o,... |
| 106 | [[2024-Jain-Norm Inconsistency in LLM Decision-Making]] | GPT-4, Claude |
| 107 | [[2024-Jue-MalayMMLU A Multitask Benchmark for the Low-Resource Malay Language]] | Baichuan, Baichuan-2, GPT-3, GPT-3.5, GPT-4, GPT-4o, Gemm... |
| 108 | [[2024-Kader-The Emergence of Strategic Reasoning of Large Language Models]] | GPT-4, Claude |
| 109 | [[2024-Kajiwara-A comprehensive framework for multi-modal hate speech detection in]] | BERT, RoBERTa, T5, Word2Vec |
| 110 | [[2024-Kajiwara-A curated dataset for hate speech detection on social media text - PMC]] | BERT, Word2Vec |
| 111 | [[2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata]] | BERT |
| 112 | [[2024-Keller-HOCON34k A Corpus of Hate Speech in Online Comments from German]] | BERT |
| 113 | [[2024-Khamassi-Strong and weak alignment of large language models]] | ChatGPT |
| 114 | [[2024-Khandelwal-Do Moral Judgment and Reasoning Capability of]] | GPT-4, ChatGPT, Llama-2 |
| 115 | [[2024-Khandelwal-Multilingual Defining Issues Test]] | GPT-4, ChatGPT, Llama-2 |
| 116 | [[2024-Kishore-Evaluating Telugu Proficiency in Large Language]] | ChatGPT |
| 117 | [[2024-Koto-IndoCulture Exploring Geographically-Influenced Cultural Commonsense]] | BART, BLOOMZ, ChatGPT, GPT-3, GPT-3.5, GPT-4, Llama, Llam... |
| 118 | [[2024-Kyriacou-Artificial Moral Intelligence Aristotelian]] | Bloom, ChatGPT, GPT-4 |
| 119 | [[2024-Lazar-Frontier AI Ethics]] | ChatGPT, GPT-4 |
| 120 | [[2024-Lee-Exploring Inherent Biases in LLMs within Korean Social Context A]] | ChatGPT, GPT-4 |
| 121 | [[2024-Liang-Cross-Language Bias Examination in Large Language Models]] | GPT-4 |
| 122 | [[2024-Liu-Detecting Anti-Semitic Hate Speech Using Transformer-Based]] | BERT, DistilBERT, GloVe, Llama-2, Llama2, RoBERTa, Word2Vec |
| 123 | [[2024-Luong-Realistic Evaluation of Toxicity in Large]] | ChatGPT, Llama-2, Mistral, Mixtral |
| 124 | [[2024-Masood-1 Natural Language Processing for Dialects of a Language A Survey]] | BERT, GPT-4, RoBERTa, T5 |
| 125 | [[2024-Masood-Bias in Large Language Models Origin Evaluation and Mitigation]] | ALBERT, BERT, ChatGPT, GPT-4, Llama, Llama Guard |
| 126 | [[2024-McGee-How Ethical Is Utilitarian Ethics]] | ChatGPT |
| 127 | [[2024-Meadows-LocalValueBench]] | GPT-4, Claude |
| 128 | [[2024-Nahian-The Goofus & Gallant Story Corpus for Practical]] | GPT-4, BERT |
| 129 | [[2024-Network-Harnessing the Power of Artificial Intelligence to Vitalize]] | BERT |
| 130 | [[2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding]] | GPT-4, Claude |
| 131 | [[2024-Nyachhyon-Consolidating and Developing Benchmarking Datasets for]] | BERT, DeBERTa, DeBERTa-v3, Distilbert, GPT-4o-mini, RoBERTa |
| 132 | [[2024-Ober-Lyceum Project AI Ethics Aristotle]] | GPT-4, ChatGPT, Gemini, Llama |
| 133 | [[2024-Oliech-SwaQuAD-24]] | BERT, RoBERTa |
| 134 | [[2024-Onose-Can LLMs Help Create Grammar Automating Grammar Creation for]] | GPT-4, BERT, gpt-4o-mini |
| 135 | [[2024-Paraschiv-Offensive Text Span Detection in Romanian Comments Using Large]] | BERT, GPT-3.5, GPT-4 |
| 136 | [[2024-Pires-Sabiá-2 A New Generation of Portuguese Large Language Models]] | Claude 3 Sonnet, Claude 3, Claude 3 Opus, GPT-3, GPT-3.5,... |
| 137 | [[2024-Pisano-Moral High Ground]] | Flan-T5, Falcon, Llama-2 |
| 138 | [[2024-Potter-Hidden Persuaders LLMs' Political Leaning and Their Influence on]] | GPT-4, GPT-3.5, Claude, Llama-3, Llama-2, Mixtral, Alpaca... |
| 139 | [[2024-Prabhakar-Cultural Fidelity in Large-Language Models An]] | ChatGPT, GPT-3, GPT-3.5, GPT-4, GPT-4 Turbo, GPT-4-turbo,... |
| 140 | [[2024-Qamar-A Benchmark Dataset with Larger Context for]] | T5, BART |
| 141 | [[2024-Rane-Concept Alignment]] | ChatGPT |
| 142 | [[2024-Ranjan-A Comprehensive Survey of Bias in LLMs]] | BERT, GPT-2, GPT-3, GPT-4, LLaMA 2 |
| 143 | [[2024-Religions-The Use of Large Language Models]] | ChatGPT, GPT3 |
| 144 | [[2024-Ren-Safetywashing]] | Mixtral, Llama-3, Llama-2, Mistral, Falcon, Gemma, Qwen |
| 145 | [[2024-Semenova-Benchmarking Multimodal Models for Ukrainian Language Understanding]] | BERT, Claude 3.5, Claude 3.5 Sonnet, Claude Sonnet, GPT-4... |
| 146 | [[2024-Senthilkumar-Fine-Tuning Language Models for Ethical Ambiguity]] | GPT-4, Llama-3, Mistral |
| 147 | [[2024-Seror-The Moral Mind(s) of Large Language Models]] | GPT-4, Claude, Llama-3, Qwen, Mixtral, Mistral |
| 148 | [[2024-Simpson-Parity Benchmark for Measuring Bias in]] | ALBERT, BERT, Claude, Claude 3.5, Claude 3.5 Sonnet, GPT-... |
| 149 | [[2024-Song-Multilingual Blending LLM Safety Alignment Evaluation with Language]] | ALBERT, ChatGPT, GPT-3, GPT-3.5, GPT-4, GPT-4o, GPT4-Turb... |
| 150 | [[2024-Songyuan Liu-Measuring Spiritual Values and Bias of]] | ChatGLM, ChatGLM 2, Chatglm2, CodeLlama, GPT-2, GPT-4, GP... |
| 151 | [[2024-Sorensen-A Roadmap to Pluralistic Alignment]] | Alpaca, GPT-3, GPT3, Gemma, Llama, LLaMA2, LLaMA2., gpt-3... |
| 152 | [[2024-Sorin-Ethical Alignment of LLMs in Healthcare]] | GPT-4, GPT-3.5, Llama-3, Gemma, Phi, Qwen |
| 153 | [[2024-Stenseke-Computational Complexity of Ethics]] | GPT-3 |
| 154 | [[2024-Street-LLMs achieve adult human performance on]] | GPT-3.5, GPT-4, LaMDA, PaLM, Flan-PaLM |
| 155 | [[2024-Suliman-The interconnectedness between Ubuntu principles]] | ChatGPT |
| 156 | [[2024-Tahir-Benchmarking Pre-trained Large Language Models Potential]] | BERT, BLOOM, Bloomz, ChatGPT, GPT 3, GPT 3.5, GPT 2, GPT ... |
| 157 | [[2024-Takemoto-The moral machine experiment on large language]] | GPT-3.5, GPT-4, PaLM-2, Llama-2 |
| 158 | [[2024-University-Monitoring the Evolution of Antisemitic Discourse]] | BERT |
| 159 | [[2024-Unknown-LIEA-BERT A Linguistically Enriched Framework for]] | BERT |
| 160 | [[2024-Vallor-The AI Mirror]] | ChatGPT, Gemini, Llama |
| 161 | [[2024-Veitsman-Recent Advancements and Challenges of Turkic]] | BERT, GPT-4, Llama-2, RoBERTa |
| 162 | [[2024-Wang-A Comprehensive Survey of LLM Alignment Techniques]] | Alpaca, BERT, ChatGPT, Claude, Claude-3, GPT-2, GPT-3, GP... |
| 163 | [[2024-Wang-Possibilities and challenges in the moral growth of LLMs]] | GPT-2, GPT-3, ChatGPT |
| 164 | [[2024-Wasi-Exploring Bengali Religious Dialect Biases in Large Language Models]] | BERT, ChatGPT |
| 165 | [[2024-Weidinger-Holistic Safety and Responsibility Evaluations of]] | bloom |
| 166 | [[2024-Wijanarko-Monitoring Hate Speech in Indonesia An NLP-based Classification of]] | BERT, ChatGPT, GPT-4o mini, GPT-4, RoBERTa, GPT-3, GPT-3.... |
| 167 | [[2024-Yang-Benchmarking LLM Guardrails in Handling Multilingual Toxicity]] | ChatGPT, GPT-4, Llama, Llama-3, LlaMa-3.1, LlaMa-Guard, M... |
| 168 | [[2024-Yang-Large Language Models Meet Text-Centric Multimodal Sentiment Analysis]] | BERT, ChatGPT, Claude, Llama, LLaMA1, Qwen-VL |
| 169 | [[2024-Yao-CLAVE ValEval]] | GPT-4, GPT-2, Phi, Mistral, Llama-2, Alpaca |
| 170 | [[2024-Yao-Self-Alignment Improving Alignment of Cultural Values in LLMs via]] | BLOOMz, CommandR, Llama-3, Llama3, Mistral, Mistral. 6, c... |
| 171 | [[2024-Zangari-A survey on moral foundation theory and pre-trained language models]] | BERT, GPT-3, GPT-3.5, GloVE, Llama, RoBERTa |
| 172 | [[2024-Zhi-Xuan-Beyond Preferences in AI Alignment]] | GPT-4, ChatGPT |
| 173 | [[2024-Zhou-Rethinking Machine Ethics Can LLMs Perform Moral Reasoning]] | Llama-2, GPT-4 |
| 174 | [[2024-team-VLegal-Bench Cognitively Grounded Benchmark for Vietnamese Legal]] | Bloom, Claude Sonnet, GPT-4, GPT-4o, GPT-4o-mini, Llama, ... |
| 175 | [[2024-Šekrst-AI Ethics by Design]] | ChatGPT, Claude, Llama, Mixtral |
| 176 | [[2025-Abdaljalil-HalluVerse25]] | GPT-4, Phi, Mistral, Qwen, Gemma, Llama-3, PaLM-2 |
| 177 | [[2025-Abdullah-KurdSTS The Kurdish Semantic Textual Similarity]] | BERT |
| 178 | [[2025-Adelani-AfriMTEB and AfriE5 Benchmarking and Adapting]] | BERT, Gemma, Mistral, Mistral-7B, Qwen2, Qwen3, RoBERTa |
| 179 | [[2025-Agarwal-Fluent but Foreign - Even Regional LLMs Lack Cultural Alignment]] | GPT-4, Llama-2, Llama-3, Mistral, Gemma |
| 180 | [[2025-Aggarwal-Letta Leaderboard]] | Claude, GPT-4 |
| 181 | [[2025-Akata-Playing Repeated Games with Large Language Models]] | GPT-4, Claude, Llama-2 |
| 182 | [[2025-Al-SEADialogues A Multilingual Culturally Grounded Multi-turn]] | GPT-4, GPT-4o mini, Llama, Llama-3.1, Qwen-14B |
| 183 | [[2025-Al-SHADES A New Multilingual Benchmark for Stereotypes Bias in Large]] | BERT, BLOOM, Bloom-1b7, Bloom-7b1, BloomZ, Llama-3, Llama... |
| 184 | [[2025-Al-SHADES Towards a Multilingual Assessment of Stereotypes in Large]] | BERT, BLOOM, Bloom-1b7, Bloom-7b1, BloomZ, Llama-3, Llama... |
| 185 | [[2025-Al-Towards a Multilingual Assessment of Stereotypes in Large ...]] | BERT, BLOOM, Bloom-1b7, Bloom-7b1, BloomZ, Llama-3, Llama... |
| 186 | [[2025-Alhassoun-Saudi-Alignment Benchmark - Assessing LLMs Alignment with Saudi]] | GPT-4, GPT-3.5, Llama-3, Llama-2 |
| 187 | [[2025-Ali-Data Curation for Pluralistic Alignment]] | GPT-4o |
| 188 | [[2025-Alvisi-Mapping the Italian Telegram Ecosystem Communities Toxicity and Hate]] | ChatGPT, Mixtral |
| 189 | [[2025-Aly-ArGAN Arabic Gender Ability and Nationality Dataset for ...]] | DeepSeek v3, Deepseek 0, Deepseek 79, GPT-4o, LLama 3.3, ... |
| 190 | [[2025-Aly-On Evaluating and Mitigating Gender Biases in Multilingual ...]] | BERT, RoBERTa |
| 191 | [[2025-Anonymous-BEATS]] | GPT-4, Claude, Mistral, Llama-3 |
| 192 | [[2025-Antar-Do Your Guardrails Even Guard Evaluating Moderation Guardrails for]] | ChatGPT, Claude, GPT-4, GPT-4o, Llama, Llama Guard, PaLM, T5 |
| 193 | [[2025-Arike-A Framework for Analyzing and Measuring Goal]] | Claude, GPT-4 |
| 194 | [[2025-Arnardottir-WikiQA-IS Assisted Benchmark Generation and Automated Evaluation of]] | GPT-4, GPT-4o |
| 195 | [[2025-Azmi-IndoSafety Culturally Grounded Safety for LLMs in Indonesian Languages]] | Claude, Claude 312, GPT-4o, Gemma, Gemma2, LLaMA 3.116, L... |
| 196 | [[2025-Bali-How Deep Is Representational Bias in]] | ChatGPT, GPT-4, GPT-4 Turbo, GPT4-Turbo |
| 197 | [[2025-Banar-MTEB-NL and E5-NL Embedding Benchmark and Models for Dutch]] | BERT, ChatGPT, Qwen, Qwen3, Mistral |
| 198 | [[2025-Barman-RLHF Whose Culture Whose Values]] | GPT-3, GPT-4, InstructGPT |
| 199 | [[2025-Basem-Two-Stage Quranic QA via Ensemble Retrieval]] | BERT, DeepSeek, ELECTRA |
| 200 | [[2025-Basile-NepX-Hate A Nepali Hate Speech Corpus]] | BERT, GPT-4o-mini, GPT-4, RoBERTa |
| 201 | [[2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities]] | Claude, Llama, Qwen |
| 202 | [[2025-Bhowmik-Evaluating LLMs' Multilingual Capabilities for Bengali Benchmark]] | Alpaca, DeepSeek, DeepSeek-R1, Dolly, GPT-4o-mini, Llama,... |
| 203 | [[2025-Bidgoli-FARSIQA Faithful and Advanced RAG System]] | Llama 3, Llama 4, Llama-4 |
| 204 | [[2025-Bokaei-Culture Matters in Toxic Language Detection in Persian]] | BERT, ChatGPT, GEMMA, GEMMA 2, GPT 2, GPT 3, GPT 3.5 Turb... |
| 205 | [[2025-Brito-ToxSyn Reducing Bias in Hate Speech Detection via Synthetic Minority]] | GPT-4, BERT |
| 206 | [[2025-Brophy-Wide Reflective Equilibrium LLM Alignment]] | ChatGPT, Claude, Claude Opus, DeepSeek |
| 207 | [[2025-Bui-Large Language Models Discriminate Against Speakers of German Dialects]] | Llama-3.1-70B, Llama-3.1-8B, Llama-3-70B, Llama-3-8B, Mis... |
| 208 | [[2025-Canaverde-LegalBench.PT A Benchmark for Portuguese Law]] | ALBERT, Claude, Claude-3, Claude-3-Opus, Claude-3.5, Clau... |
| 209 | [[2025-Carballo-Evaluating Compact LLMs for Zero-Shot Iberian Language Tasks on]] | DeepSeek-R1, GPT-4, Gemma, Gemma 2, Gemma-2, Llama, Llama... |
| 210 | [[2025-Chakraborty-Structured Moral Reasoning]] | Llama-3, Llama-2, Mistral, Qwen, Phi |
| 211 | [[2025-Chakravarthi-Detecting Caste and Migration Hate Speech]] | BERT, BLOOM, BLOOM-560, RoBERTa, Word2Vec |
| 212 | [[2025-Chared-AI-driven detection of hate speech on social media a case study in]] | CamemBERT, DistilCamemBERT, DeHateBERT |
| 213 | [[2025-Chen-Leveraging large language models to assist]] | GPT-4 |
| 214 | [[2025-Chua-Between a Rock and a Hard Place TRIAL]] | Llama-3, Mistral |
| 215 | [[2025-Cocu-A Cross-Lingual Analysis of Bias in Large Language Models Using]] | DeepSeek, LLama-4, Llama, gemma |
| 216 | [[2025-Cognitive-Evolution of Meta’s LLaMA Models and Parameter-Efficient Fine-Tuning]] | Alpaca, ChatGPT, GPT-3, GPT-4, Llama, LLaMA 1, LLaMA 2, L... |
| 217 | [[2025-Cognitive-T-LLaMA a Tibetan large language model based on LLaMA2 Complex &]] | ALBERT, BERT, Baichuan2, ChatGPT, Llama, LLaMA 8, LLaMA.,... |
| 218 | [[2025-Dang-VMMU A Vietnamese Multitask Multimodal Understanding and Reasoning]] | Claude 4., GPT-4, Gemma, Gemma-3, Llama-4, Mistral Small,... |
| 219 | [[2025-Davies-Exploring the occupational biases and stereotypes of Chinese large]] | Baichuan, ChatGLM, ChatGLM2, ChatGPT, GPT-3, baichuan-ai,... |
| 220 | [[2025-Davies-F2Bench An Open-ended Fairness Evaluation Benchmark ...]] | ChatGPT, DeepSeek, DeepSeek 1, DeepSeek-V3, GPT-4, Gemma,... |
| 221 | [[2025-De Montis-Morality in AI]] | BERT |
| 222 | [[2025-Demidova-John vs. Ahmed Debate-Induced Bias in Multilingual LLMs]] | GPT-3, GPT-3.5, GPT-4 |
| 223 | [[2025-Dickerson-Who Gets the Kidney]] | GPT-4, Claude, Gemma, Llama-3, DeepSeek |
| 224 | [[2025-Do-ViToSA Audio-Based Toxic Spans Detection on Vietnamese Speech]] | BERT, DistilBERT |
| 225 | [[2025-Duan-AdAEM Adaptively and Automated Extensible Measurement for Value]] | GPT-4, GPT-3.5, Claude, Llama-3, Mistral, Qwen, DeepSeek |
| 226 | [[2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation]] | GPT-4 |
| 227 | [[2025-Edeh-Language Diversity Evaluating Language Usage and]] | Llama 3.3 |
| 228 | [[2025-Elkins-Syntactic Framing Fragility SFF Robustness Evaluation of LLM Ethical]] | Claude, Grok, DeepSeek, Llama-3, Phi, Gemma, Qwen |
| 229 | [[2025-Enguix-Overview of HOMO-LAT at IberLEF 2025 Human-Centric Polarity Detection]] | BERT, Falcon-7B, Gemma, Mistral-7B, ChatGPT |
| 230 | [[2025-Eriksson-Can We Trust AI Benchmarks An Interdisciplinary Review]] | Bartz, Claude 3 Opus, GPT-4, GPT4 |
| 231 | [[2025-Fanous-SycEval Evaluating LLM Sycophancy]] | ChatGPT, Claude, Llama-3 |
| 232 | [[2025-Farsi-MELAC Massive Evaluation of Large Language Models with Alignment of]] | BERT, ChatGPT, GPT-4, Gemma, GPT-4o, Llama, Llama 3.2, Ll... |
| 233 | [[2025-Farsi-PBBQ A Persian Bias Benchmark Dataset Curated with Human-AI]] | ALBERT, BERT, Claude, GPT-4o, Llama, Llama-3, LLaMA-3.1, ... |
| 234 | [[2025-Fasching-Inconsistencies in Hate Speech Detection Across]] | ChatGPT, Claude, Claude 3.5, GPT-4o, MISTRAL LARGE, Mistral |
| 235 | [[2025-Fenech-Borg-The Cultural Gene of Large Language Models]] | GPT-4 |
| 236 | [[2025-Feng-ERPO]] | Llama-3, Qwen, DeepSeek, GPT-4 |
| 237 | [[2025-Fillies-A novel German TikTok hate speech dataset far-right comments against]] | BERT |
| 238 | [[2025-Flek-AmericasNLI Machine translation and natural language inference]] | BERT, T5, T5-style |
| 239 | [[2025-Flores-BenchMoral]] | ChatGPT, Llama-3, DeepSeek |
| 240 | [[2025-Gabriel-AI Alignment as Fair Treatment of Claims]] | Claude, GPT-4 |
| 241 | [[2025-Gamboa-Filipino Benchmarks for Measuring Sexist and Homophobic Bias in]] | BERT, BLOOM, GPT-4, Mistral, RoBERTa, llama3 |
| 242 | [[2025-Gao-How Large Language Models Enhance Low-Resource Mongolian-Chinese]] | BERT, Gemma, Gemma2, LLaMA-3.1, LLaMA3.1, Llama, Qwen2, Q... |
| 243 | [[2025-Gao-MIST Moral Inference through Storytelling with Text and Images]] | GPT-4, Llama-3, Claude, Qwen |
| 244 | [[2025-Gerdes-Exploring LLM Chatbots as Potential Guides to]] | ChatGPT, DeepSeek |
| 245 | [[2025-Giachino-An Empirical Investigation of Gender Stereotype Representation in]] | GPT-4o-mini |
| 246 | [[2025-Gromenko-Cultural Evaluation of LLMs in Russian Catchphrases and Cultural Types]] | ChatGPT, Claude 3.5, Claude 3.5 Sonnet, GPT-3, GPT-3.5, G... |
| 247 | [[2025-Gu-Linguistically informed ChatGPT prompts to enhance Japanese-Chinese]] | ChatGPT |
| 248 | [[2025-Gupta-EnDive A Cross-Dialect Benchmark for Fairness and Performance in]] | Claude, Claude 3.5 Sonnet, DeepSeek-v3, GPT-4o, GPT-4o mi... |
| 249 | [[2025-Hamed-A Survey of Code-switched Arabic NLP]] | ChatGPT, Llama-3 |
| 250 | [[2025-Hasan-LLM-Based Multi-Task Bangla Hate Speech Detection Type Severity and]] | BERT, Claude, Claude-3.5 Sonnet, GPT-4, Llama, Llama-3.2,... |
| 251 | [[2025-Havaldar-Culturally-Aware Conversations A Framework Benchmark for]] | GPT-4, Claude, Gemini |
| 252 | [[2025-Heredia-Conditioning LLMs to Generate Code-Switched Text]] | BLOOM, BERT, GPT-4o, Llama, Llama3, Llama3.3, Mistral 31.... |
| 253 | [[2025-Hew-MyCulture Exploring Malaysia's Diverse Culture under Low-Resource]] | DeepSeek, DeepSeek-V3, GPT-4o, GPT-4o mini, GPT-4, Llama,... |
| 254 | [[2025-Hilliard-Measuring AI Alignment with Human Flourishing]] | GPT-4, ChatGPT, Claude, Grok |
| 255 | [[2025-Hofman-MAPS A Multilingual Benchmark for Global Agent Performance and]] | GPT-4, GPT-4o, Qwen 2, Qwen 7B, Qwen-2, Qwen2, ChatGPT |
| 256 | [[2025-Hong-NormGenesis Multicultural Dialogue Generation Dataset]] | GPT-4, Llama-3, Qwen |
| 257 | [[2025-Hong-PrinciplismQA Towards Assessing Medical Ethics from Knowledge to]] | GPT-4, Claude, Gemma, Llama-3, Qwen, DeepSeek |
| 258 | [[2025-Huang-Analysis of LLM Bias Chinese Propaganda & Anti-US Sentiment in]] | ChatGPT, DeepSeek, DeepSeek-R1, GPT-3, GPT-3.5, GPT-4, GP... |
| 259 | [[2025-Hussain-From RAG to Agentic Validating Islamic-Medicine]] | Claude, Claude-4, GPT4, Llama-3, Mistral 7b, Mistral- 7B,... |
| 260 | [[2025-Hähnel-A Companion to Applied Philosophy of AI]] | ChatGPT, Claude, LaMDA |
| 261 | [[2025-Institute-2025 AI Safety Index]] | DeepSeek |
| 262 | [[2025-Jafarinejad-PerGOLD Identification of Offensive Language in Persian Tweets]] | BERT, RoBERTa |
| 263 | [[2025-Jamshidi-MoCoP]] | GPT-4, DeepSeek |
| 264 | [[2025-Jin-Social Bias Benchmark for Generation A Comparison of Generation and]] | Claude, Claude-3-haiku, Claude-3.5-sonnet, GPT-3, GPT-3.5... |
| 265 | [[2025-Kabir-BLUCK A Benchmark Dataset for Bengali Linguistic Understanding and]] | Claude 3.5, Claude 3.5-Sonnet, Claude-3.5, Claude-3.5-Hai... |
| 266 | [[2025-Kanepajs-LAG-MMLU Benchmarking Frontier LLM Understanding in]] | BERT, Claude 3.5, Claude 3.5 Sonnet, DeepSeek-R1, DeepSee... |
| 267 | [[2025-Kharchenko-How Well Do LLMs Represent Values Across Cultures]] | ChatGPT, Command-R, GPT-4, GPT-4o, GPT4, GPT4o, Gemma, LL... |
| 268 | [[2025-Kilov-Discerning What Matters]] | Llama-3, GPT-4, DeepSeek, Claude |
| 269 | [[2025-Kranti-MATA mata Mindful Assessment of the]] | Claude, Claude Sonnet, Claude-Sonnet, GPT-4, GPT-4o, Gemm... |
| 270 | [[2025-Krishna-D-REX A Benchmark for Detecting Deceptive Reasoning in Large Language]] | Claude, DeepSeek, Qwen, Grok |
| 271 | [[2025-Krzanowski-Phronesis for AI Systems]] | ChatGPT, GPT-4 |
| 272 | [[2025-Kumar-TeSent A Benchmark Dataset for Fairness-aware]] | BERT, RoBERTa |
| 273 | [[2025-LLMs-A Leaderboard to Benchmark Ethical Biases in LLMs]] | ChatGPT, GPT4, Llama-2 |
| 274 | [[2025-LaCroix-Metaethical perspectives on ‘benchmarking’ AI]] | BERT, GPT-3 |
| 275 | [[2025-Lan-McBE A Multi-task Chinese Bias Evaluation Benchmark for Large]] | ALBERT, Baichuan 2, Baichuan2, ChatGLM, DeepSeek, DeepSee... |
| 276 | [[2025-Lan-McBE]] | Qwen, Llama-2, Mistral, ChatGPT |
| 277 | [[2025-Lee-When Prompting Fails to Sway]] | Claude, GPT-4, GPT-3.5, Llama-3 |
| 278 | [[2025-Li-Analyzing Cognitive Differences Among Large]] | GPT-4o, Qwen, Llama-3, Gemma, DeepSeek, Phi |
| 279 | [[2025-Li-Untangling Input Language from Reasoning Language A Diagnostic]] | ALBERT, Claude, Claude 1.00, Claude 11.5, Claude 42.7, Cl... |
| 280 | [[2025-Lindstrom-Helpful Harmless Honest Sociotechnical Limits]] | ChatGPT, Claude, Llama |
| 281 | [[2025-Liu-Cross-cultural value alignment frameworks]] | GPT-4o, GPT-3.5, Claude, Llama-3, Llama-2, Mistral, Mixtr... |
| 282 | [[2025-Liu-Diagnosing Moral Reasoning Acquisition in]] | Mistral, Llama-3, BERT |
| 283 | [[2025-Liu-On the Convergence of Moral Self-Correction in LLMs]] | Mistral, GPT-4 |
| 284 | [[2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences]] | GPT-4 |
| 285 | [[2025-Maatta-Language Models for Code-switch Detection of te reo Māori and English]] | BERT |
| 286 | [[2025-Maatta-LinCE Benchmark]] | BERT, ELMo |
| 287 | [[2025-Machlovi-Towards Safer AI Moderation Evaluating LLM Moderators Through a]] | Alpaca, BERT, Gemma, Gemma2, Llama, Llama Guard, LlamaGua... |
| 288 | [[2025-Maheshwari-ParamBench A Graduate-Level Benchmark for Evaluating]] | Claude, GPT-4, Gemma, Gemma-3, Gemma2, Gemma3, Llama, Lla... |
| 289 | [[2025-Masood-A survey of multilingual large language models - PMC]] | BLOOM, BLOOM-1, ChatGPT, GPT-3, GPT-3.5, GPT-3.5-turbo, G... |
| 290 | [[2025-Masood-Beyond MCQ An Open-Ended Arabic Cultural QA Benchmark with Dialect]] | Falcon3, GPT-4, Palm, Qwen, Qwen2, Qwen2.5, BERT |
| 291 | [[2025-Masood-From Words to Proverbs Evaluating LLMs’ Linguistic and Cultural]] | ChatGPT, GPT-4, GPT-4o, Llama, Llama-3, Mistral, Mistral ... |
| 292 | [[2025-Mazeika-Utility Engineering]] | GPT-4, GPT-3.5, Llama-2, Llama-3, Gemma, Qwen |
| 293 | [[2025-Mc-Irish-BLiMP A Linguistic Benchmark for Evaluating Human and Language]] | Gemma, Gemma 3, Llama 2, Llama-2, Llama-4, Mistral, Mistr... |
| 294 | [[2025-Mekky-HALF Harm-Aware LLM Fairness Evaluation Aligned with Deployment]] | Claude, Claude 4, Claude 4., Claude4, DeepSeek, DeepSeek ... |
| 295 | [[2025-Metinov-KyrgyzBERT A Compact Efficient Language Model for Kyrgyz NLP]] | BERT, RoBERTa |
| 296 | [[2025-Mikhailov-NorEval A Norwegian Language Understanding and Generation Evaluation]] | Claude 3.7 Sonnet, GPT-4o, Llama, Llama-3, Llama-3.3, Lla... |
| 297 | [[2025-Mining)-Enhancing social media hate speech detection in low-resource]] | XLM-RoBERTa |
| 298 | [[2025-Mohammadi-EvalMORAAL]] | GPT-4, GPT-3.5, Claude, PaLM-2, Llama-3, Qwen, Mistral, D... |
| 299 | [[2025-Mohammadi-Identifying Gender Stereotypes and Biases in Automated Translation]] | GloVe, Word2Vec |
| 300 | [[2025-Mohammed-Aftina]] | Gemma |
| 301 | [[2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human]] | GPT-4, Mistral, Llama-3, Qwen |
| 302 | [[2025-Mukherjee-DECASTE Unveiling Caste Stereotypes in Large]] | ChatGPT, GPT-3, GPT-3.5, GPT-3.5-turbo, GPT-4, GPT-4o, Ll... |
| 303 | [[2025-Mushtaq-WorldView-Bench]] | GPT-4, Claude, Llama-3, Mistral, DeepSeek |
| 304 | [[2025-Nadeem-Ethical Decision-Making in Humans and Large]] | GPT-4, DeepSeek |
| 305 | [[2025-Narnaware-SB-Bench]] | GPT-4, Llama-3, Gemma, Qwen, Phi |
| 306 | [[2025-Narula-A comprehensive review on detection of hate speech for multi-lingual]] | BERT, GPT-3, GloVe, RoBERTa, Word2Vec, XLNet, distilBERT |
| 307 | [[2025-Nath-Few-shot and zero-shot Assamese hate speech detection a comparative]] | BERT, GPT-3, GPT-3.5, GPT-3.5-Turbo, GPT-4, Mistral- 7B, ... |
| 308 | [[2025-Nemkova-Cross-Lingual Stability and Bias in Instruction-Tuned]] | ALBERT, Claude, Claude Sonnet, Claude-Sonnet, DeepSeek, D... |
| 309 | [[2025-Neuman-Analyzing the Ethical Logic of Six Large Language Models]] | GPT-4, Llama, Claude, Mistral |
| 310 | [[2025-Neuman-Auditing the Ethical Logic of Generative AI Models]] | GPT-4, Llama, Claude, Mistral, DeepSeek |
| 311 | [[2025-Neuman-PRIME Framework Convergent Ethics]] | GPT-4, Llama, Claude, Mistral |
| 312 | [[2025-Ngui-SEA-SafeguardBench Evaluating AI Safety in SEA]] | GPT-4, GPT-4o, Gemma, Gemma-2, Gemma-3, Gemma3, LLaMA-3.1... |
| 313 | [[2025-Ni-A Survey on Large Language Model Benchmarks]] | ALBERT, BART, BERT, Bloom, ChatGPT, Claude, DeepSeek-V3, ... |
| 314 | [[2025-Nuha-Exploring NLP Benchmarks in an Extremely Low-Resource Setting]] | BERT, DistilBERT, GPT-3, GPT-3.5-turbo, GPT-4, GPT-4o, Ll... |
| 315 | [[2025-Oh-Robustness of Large Language Models in Moral Judgements]] | GPT-3.5 |
| 316 | [[2025-Ohlhorst-Virtues for AI]] | ChatGPT |
| 317 | [[2025-Okamoto-AI-based medical ethics education]] | ChatGPT |
| 318 | [[2025-Open-A Comprehensive Dataset for Enhancing Safety in LLM- ...]] | Claude 3 Haiku, Claude 3 Opus, Claude 3 Sonnet, GPT-3, GP... |
| 319 | [[2025-Open-Safety and Security Analysis of Large Language Models Risk Profile]] | BERT, ChatGPT, Claude, Claude 4, Claude 4 Opus, Claude Op... |
| 320 | [[2025-Osmani-Investigating Retrieval-Augmented Generation in Quranic Studies]] | GPT-4, Gemma, Gemma 2, Gemma2, Llama, Llama 3, Llama 3.1,... |
| 321 | [[2025-Palta-Speaking the Right Language]] | GPT-4 |
| 322 | [[2025-Park-Deontological Keyword Bias]] | GPT-4, Llama-3, Gemma, Qwen |
| 323 | [[2025-Piot-Bridging Gaps in Hate Speech Detection Meta-Collections and]] | BERT, Gemma, Llama, Llama 3.1, Mistral 7B, RoBERTa, llama 3 |
| 324 | [[2025-Poole-Dayan-OvertonScore Benchmarking Overton Pluralism in LLMs]] | GPT-4, Gemma, DeepSeek, Llama-3, Claude |
| 325 | [[2025-Pramodya-SinhalaMMLU A Comprehensive Benchmark for Evaluating Multitask]] | CLAUDE 3.5 SONNET, CLAUDE-3, CLAUDE-3 HAIKU, CLAUDE-3-HAI... |
| 326 | [[2025-Pranav-Rice-VL Evaluating Vision-Language Models for Cultural Understanding]] | Claude, Claude-3, Claude-3-Opus, GPT-4, GPT-4o, LLaMA 3.2... |
| 327 | [[2025-Pranida-Culturally-Nuanced Story Generation for Reasoning in Low-Resource]] | BERT, Claude, Claude-3 Opus, GPT-4, GPT-4o, Gemma 2, Gemm... |
| 328 | [[2025-Prasannan-Counter-Speech Generation for Homophobic and Transphobic]] | ChatGPT, GPT-2, GPT-3, GPT-4, GPT-4o |
| 329 | [[2025-Pretrained-Evaluating Uighur literary translation A comparative study of ChatGPT]] | BERT, ChatGPT, DeepSeek, GPT-4o, Llama |
| 330 | [[2025-Pudasaini-NepaliGPT A Generative Language Model for]] | GPT-2 |
| 331 | [[2025-Qadir-Can LLMs Write Faithfully An Agent-Based]] | BERT, ChatGPT, Claude, GPT-4, GPT-4o |
| 332 | [[2025-Raihan-A Multilingual Benchmark to Evaluate Large Language]] | BERT, Claude, Claude3.5, DeepSeek-Coder, GPT-3, GPT-3.5, ... |
| 333 | [[2025-Rashed-Advancing NLP Equity A Secondary Benchmark Evaluation of Multilingual]] | BERT, RoBERTa |
| 334 | [[2025-Research-IndQA An Indic QA Benchmark for]] | Llama, llama 2, Llama-2, llama2.70, llama2.70. chat, mixt... |
| 335 | [[2025-Rodemann-A Statistical Case Against Empirical Human-AI]] | GPT2 |
| 336 | [[2025-Rosenbaum-MTQE.en-he Machine Translation Quality Estimation for English-Hebrew]] | ChatGPT, Claude |
| 337 | [[2025-Rozen-Do LLMs Have Consistent Values]] | GPT-4, Llama-3, Gemma |
| 338 | [[2025-Russo-The Pluralistic Moral Gap]] | GPT-4, ChatGPT, Claude, Mistral, Llama-3, Qwen |
| 339 | [[2025-Rystrøm-Multilingual Multicultural Evaluating Gaps Between Multilingual]] | GPT-3, GPT-4, Gemma, Llama, gpt-3.5-turbo |
| 340 | [[2025-SOCIETY-How Much of a Pluralist is]] | ChatGPT, Claude, Claude 3.5, Claude 3.5 Sonnet, DeepSeek |
| 341 | [[2025-Sah-FairEval Evaluating Fairness in LLM-Based ...]] | BERT, ChatGPT, Claude, DeepSeek, GPT-3, GPT-3.5, GPT-4o, ... |
| 342 | [[2025-Sameer-Insights into Moral Reasoning of AI]] | ChatGPT, GPT-4 |
| 343 | [[2025-Satheesh-Dutch CrowS-Pairs Adapting a Challenge Dataset for Measuring Social]] | BERTje, RobBERT, mBERT, Mistral-7B, BERT, RoBERTa, FlauBE... |
| 344 | [[2025-Sefat-BengaliFig A Low-Resource Challenge for Figurative and Culturally]] | Claude, Claude Opus, Claude Sonnet, Claude- Sonnet, Claud... |
| 345 | [[2025-Sel-Backtracking for Safety]] | Gemma, Llama-3 |
| 346 | [[2025-Sermsri-Debiasing Large Language Models in Thai]] | ChatGPT, GPT-3, GPT-3.5, GPT-4, Llama, Llama-3 |
| 347 | [[2025-Shah-LLM Rationalis Measuring Bargaining Capabilities of AI Negotiators]] | GPT-4, ChatGPT |
| 348 | [[2025-Shan-SGToxicGuard Toxicity Red-Teaming Benchmarking LLM Safety]] | BERT, GPT-4, GPT-4o, GPT-4o mini, GPT-4o-mini, Llama, LLa... |
| 349 | [[2025-Sheth-Beyond Monolingual Assumptions A Survey of Code-Switched NLP in the]] | BERT, ChatGPT, GPT-2, GPT-4, GPT-4o, GloVe, Llama, RoBERT... |
| 350 | [[2025-Shi-A Systematic Study of Position Bias in LLM-as-a-Judge]] | Claude, Claude-3, Claude-3-Haiku, Claude-3-Opus, Claude-3... |
| 351 | [[2025-Simões-IberoBench A Benchmark for LLM Evaluation in Iberian Languages]] | BERT, BLOOM, BLOOM-1, BLOOM-7, Falcon-7B, Gemma, Llama, L... |
| 352 | [[2025-Snoswell-Beyond Verdicts LLM Moral Competence]] | ChatGPT, DeepSeek, GPT-4 |
| 353 | [[2025-Sorensen-Value Profiles for Encoding Human Variation]] | Gemma |
| 354 | [[2025-Su-Understanding How Value Neurons Shape the]] | Llama-3, Qwen, Gemma |
| 355 | [[2025-Suh-SENSE-7 Taxonomy and Dataset for Measuring User Perceptions of]] | GPT-4, GPT-3.5, Llama-2 |
| 356 | [[2025-Sukiennik-An Evaluation of Cultural Value Alignment in LLM]] | GPT-3.5, GPT-4, Llama-3, DeepSeek, Qwen |
| 357 | [[2025-Sun-Evaluating ChatGPT's Performance in Creative Text ...]] | ChatGPT, GPT-3, GPT-3.5, GPT-4 |
| 358 | [[2025-Tereshchenko-A Comparative Analysis of Ethical and Safety Gaps]] | GPT-4, GPT-3.5, DeepSeek |
| 359 | [[2025-Terziyan-Towards ethical evolution]] | GPT-4, Gemini |
| 360 | [[2025-Tewabe-The State of Large Language Models for African Languages Progress and]] | BART, BERT, BLOOM, T5 |
| 361 | [[2025-Togmanov-KazMMLU Evaluating Language Models on Kazakh]] | ALBERT, BLOOM, BLOOMZ, DeepSeek, DeepSeek V3, DeepSeek-AI... |
| 362 | [[2025-Tomar-BharatBBQ A Multilingual Bias Benchmark for]] | BERT, Bloomz, GPT-2, Gemma, Gemma-2, Llama, Llama-3.1, Phi-3 |
| 363 | [[2025-Trepczynski-AI as a Rational Theologian A]] | Bloom, ChatGPT, Codex, GPT-3, GPT-3.5, GPT-4, GPT-4o, Lla... |
| 364 | [[2025-Tsvetkov-Democracy-in-Silico Institutional Design as Alignment]] | GPT-4, DeepSeek |
| 365 | [[2025-Umer-Sacred or Secular Religious Bias in]] | ChatGPT |
| 366 | [[2025-Unknown-Beyond Neutrality A Comprehensive Approach of Religious Bias]] | ChatGPT, GPT-2, GPT-3, GPT-3.5, GPT-4, GPT-4-Turbo, GPT-4... |
| 367 | [[2025-Unknown-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J.]] | ChatGPT, DeepSeek, GPT-4 |
| 368 | [[2025-Unknown-Evaluation of Social Bias Classification Performance of LLMs Using]] | BERT, GPT-3, GPT-3.5, GPT-3.5 Turbo, GPT-4, GPT-4o |
| 369 | [[2025-Unknown-Moral Judgment of LLM Using Korean Datasets and Eastern Ethical]] | GPT-4, GPT-3.5 |
| 370 | [[2025-Unknown-On the Challenges of Bias Evaluation Under Multilingual ...]] | BERT |
| 371 | [[2025-Unknown-Sentiment analysis in multilingual context Comparative analysis of]] | BERT, word2vec |
| 372 | [[2025-Unknown-The Need for Robust and Inclusive Benchmarks in Evaluating LLMs on]] | BERT, BLOOM, ChatGPT, CommandR, GPT-3, GPT-3.5, GPT-3.5 T... |
| 373 | [[2025-Unknown-Understanding Asian Stereotyping and Bias in LLMs Flora Huang]] | BERT, Llama, Mistral |
| 374 | [[2025-Usmana-A Large Language Model-Based Approach for Multilingual Hate Speech]] | ALBERT, BERT, DeepSeek 67B, ELECTRA, GPT 3, GPT 3.5 Turbo... |
| 375 | [[2025-Varsha-From Phonemes to Meaning Evaluating Large]] | ChatGPT, Claude, Claude Sonnet, Claude., DeepSeek V3, Dee... |
| 376 | [[2025-Wang-Diverse Human Value Alignment for LLMs via Ethical Reasoning]] | GPT-4, Llama-3, DeepSeek, Qwen |
| 377 | [[2025-Wang-Large and Small models for collaborative cross-lingual data]] | BERT, ChatGPT, GPT-4o |
| 378 | [[2025-Wang-Measuring Desired Group Discrimination in LLMs]] | GPT-4, Claude, Llama-3, Mistral, Gemma |
| 379 | [[2025-Wang-Multimodal Understanding of Human Values in Videos]] | Mistral, RoBERTa, DeBERTa |
| 380 | [[2025-Weber-Digital Guardians Can GPT-4 Perspective API and Moderation API]] | GPT-4o |
| 381 | [[2025-Winata-The Decades Progress on Code-Switching Research in NLP]] | ALBERT, BERT |
| 382 | [[2025-Wu-Chain-of-Ethics Defense Framework Wu et al.]] | GPT-4, GPT-4o, Claude, DeepSeek, Qwen |
| 383 | [[2025-Wu-The Bitter Lesson Learned from 2000+ Multilingual Benchmarks]] | DeepSeek-AI, GPT-4, Gemma, Qwen, Qwen1.5, Qwen2.5, ChatGP... |
| 384 | [[2025-Xia-Evaluating Modern Large Language Models on Low-Resource and]] | ChatGPT, Claude, Claude 3.5, Claude 2., Claude 3.5 Sonnet... |
| 385 | [[2025-Xie-Enhancing Multilingual Language Models for Code-Switched Input Data]] | BERT, RoBERTa |
| 386 | [[2025-Xie-SwitchLingua The First Large-Scale Multilingual and Multi-Ethnic]] | GPT-4o, GPT-4, Qwen2 |
| 387 | [[2025-Xu-AncientBench Towards Comprehensive Evaluation on Excavated]] | Baichuan2, Llama-3, Llama3, Qwen, Qwen-14B, Qwen-7B, Qwen... |
| 388 | [[2025-Xuan-LaoBench A Large-Scale Multidimensional Lao Benchmark]] | Claude, Claude-Opus, Claude-Sonnet, DeepSeek-V3, Qwen-fam... |
| 389 | [[2025-Xuan-Uncovering Cross-Linguistic Disparities in LLMs using]] | GPT-4, Gemma, Gemma-2 |
| 390 | [[2025-Yanaka-Gender Bias in Natural Language Processing and Computer Vision A]] | ALBERT, BARTL, BERT, Bart, ELMo, GPT-2, GloVe, RoBERTa, X... |
| 391 | [[2025-Yang-CodeMixBench Evaluating Large Language Models on Code Generation with]] | BERT, CodeLLaMA, Codex, DeepSeek, DeepSeek-Coder, DeepSee... |
| 392 | [[2025-Yao-CUGE A Chinese Language Understanding and Generation Evaluation]] | BERT |
| 393 | [[2025-Yoo-Adaptive Ensemble Techniques Leveraging BERT-based Models for]] | BART, BERT, DistilBERT, RoBERTa |
| 394 | [[2025-Yu-A Structured Framework for Evaluating and Enhancing Interpretive]] | Claude, LLaMA-4, Llama, Llama-3.1, Qwen, Qwen-2.5, Qwen-VL |
| 395 | [[2025-Yu-Sentiment analysis of classical Chinese literature An unsupervised]] | BERT, ChatGLM-6B, ChatGPT, DeepSeek R1, LLaMA 2 |
| 396 | [[2025-Zahid-Evaluation of Hate Speech Detection Using Large Language Models and]] | CodeLlama, DeepSeek, DeepSeekCoder, GPT 4, GPT-3, GPT-3.5... |
| 397 | [[2025-Zaki-Benchmarking the Legal Reasoning of LLMs]] | Falcon3, GPT-4o, Llama 4, Llama4, Llama |
| 398 | [[2025-Zgliczynski-Cuber-AI Ethical Resonance Hypothesis]] | GPT-4 |
| 399 | [[2025-Zhang-Cognitive Bias in Generative AI Influences]] | ChatGPT, GPT-4 |
| 400 | [[2025-Zhang-MedHallTune]] | GPT-4, Qwen, Vicuna, Llama-2, Flan-T5 |
| 401 | [[2025-Zhang-PoliCon]] | GPT-4, Qwen, Llama-3, DeepSeek |
| 402 | [[2025-Zheng-Evaluating Code-Switching Translation with Large ...]] | BLOOMZ, ChatGPT, GPT-3, GPT-3.5, GPT-4, Llama, Llama-2, P... |
| 403 | [[2025-Zhou-Bias Beyond English Evaluating Social Bias and Debiasing Methods in a]] | BERT, Gemma, Gemma 3, Llama, LLaMA 3, LLaMA 3., Qwen, Qwe... |
| 404 | [[2025-Zhu-EAVIT]] | GPT-4, Llama-2, BERT |
| 405 | [[2025-Zhu-Steering Risk Preferences in Large Language]] | Gemma |
| 406 | [[2025-Zhuang-Enhancing Cross-Lingual Transfer through Reversible Transliteration A]] | Llama2, Qwen2, Qwen2.5, Llama |
| 407 | [[2025-Zubitski-KazBench-KK A Cultural-Knowledge Benchmark for Kazakh]] | DeepSeek, Gemma-3, LLama-3.1, Llama, Llama-3, Llama-3.3, ... |
| 408 | [[2025-[[Unknown]]-Mitigating Social Bias in English and]] | BERT, GPT-3, GPT-3.5, GPT-3.5-turbo, GPT-4, GPT-4o-mini, ... |
| 409 | [[2025-approach-A Language model-based approach to sentiment classification of]] | BERT |
| 410 | [[2025-collaboration-Improving Methodologies for LLM Evaluations Across Global Languages]] | GPT4o, Gemma 2, Llama, Mistral Large |
| 411 | [[2025-community-Setting Standards in Turkish NLP TR-MMLU]] | BERT, Claude, ELECTRA, GPT-4, Gemma, Llama, claude-3.5, c... |
| 412 | [[2025-funded-Analysis of Indic Language Capabilities in]] | BERT, BLOOM, BLOOMZ, ChatGPT, Claude, Claude 3.5 Sonnet, ... |
| 413 | [[2025-team-Incorporating Diverse Perspectives in Cultural Alignment]] | ChatGPT, Mistral-7B |
| 414 | [[2025-team-ViMUL A Culturally-diverse Multilingual Multimodal Video]] | ALBERT, ChatGPT, DeepSeek-R1, GPT-4, GPT-4o, GPT-4o-mini,... |
| 415 | [[2026-Ali-UrduLM A Resource-Efficient Monolingual Urdu Language]] | GPT-3, GPT-4, Gemma, Gemma 2, GloVe, Llama, LLaMA 3.2, Ll... |
| 416 | [[2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit]] | BERT, GPT-3, GPT-3.5, GPT-4, GPT-4o, Mistral, Mistral Med... |
| 417 | [[2026-Elkins-Negation Sensitivity Index NSI]] | GPT-4, Claude, Grok, DeepSeek, Qwen, Llama, Gemma, Phi |
| 418 | [[2026-Hu-The Straight and Narrow Do LLMs Possess an Internal Moral Path]] | Claude-3.5, Claude-3.5-Sonnet, Llama-3, Llama-3.1, claude-3 |
| 419 | [[2026-Huang-Knowing But Not Doing Convergent Morality and Divergent Action in]] | GPT-4, Claude, Grok, Llama, Qwen, DeepSeek |
| 420 | [[2026-Kabir-XCR-Bench A Multi-Task Benchmark for Evaluating Cultural Reasoning in]] | BERT, Claude, Claude 3.7, Claude-3.7, Claude-3.7-Sonnet, ... |
| 421 | [[2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks]] | GPT-4 |
| 422 | [[2026-Kim-VALUEFLOW Toward Pluralistic and Steerable Value-based Alignment in]] | GPT-4, Claude, Grok, Qwen, Mistral, Phi, Gemma |
| 423 | [[2026-Klakow-AmharicStoryQA A Multicultural Story Question Answering]] | Gemma, Gemma 3, Gemma-3, GPT-4, Llama, Llama 3.1, Llama 3... |
| 424 | [[2026-Kolt-Legal Alignment for Safe and Ethical AI]] | GPT-4, Llama, Llama Guard |
| 425 | [[2026-Liu-JMedEthicBench]] | GPT-4, Claude, DeepSeek, Qwen, Llama-3, Grok |
| 426 | [[2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs]] | GPT-4, Claude, DeepSeek, Qwen, Llama-3 |
| 427 | [[2026-Madhusudan-Common to Whom Regional Cultural Commonsense]] | Claude, Claude Sonnet, DeepSeek, DeepSeek V3, DeepSeek-AI... |
| 428 | [[2026-Nadeem-Bias Beyond Borders]] | Mistral, DeepSeek |
| 429 | [[2026-Nadies-TF3-RO Training Compact Romanian Language Models on Synthetic Moral]] | ALBERT, BERT, DeepSeek, GPT-4, Gemma 2, Llama, Llama-3 |
| 430 | [[2026-Panda-IndRegBias A Dataset for Studying Indian]] | BERT, DeepSeek, DeepSeek-R1, GPT-4o, Gemma, Gemma-1.1, GP... |
| 431 | [[2026-Permadi-No Shortcuts to Culture Indonesian Multi-hop Question Answering for]] | Claude, Claude 3.7 sonnet, Claude-3.7, Claude-3.7-Sonnet,... |
| 432 | [[2026-Reaj-Cross-Lingual Probing and Community-Grounded Analysis of Gender Bias]] | BERT, ChatGPT, GPT-3, GPT-3.5-Turbo |
| 433 | [[2026-Smirnov-The Language You Ask In Language-Conditioned Ideological Divergence]] | ChatGPT, Claude |
| 434 | [[2026-[[Unknown]]-UrduBench An Urdu Reasoning Benchmark using]] | Barth, ChatGPT, DeepSeek, DeepSeek-AI, DeepSeek-R1, Falco... |

</details>

### 4.2 Papers with Data URLs but No LLM Models Identified

**211 papers** have public data URLs but no LLM model assessment.

<details>
<summary>Click to expand (211 papers)</summary>

| # | Paper | Data URL |
|--:|-------|----------|
| 1 | [[0000-collections-JainGPT AI-Powered Chatbot for Jain Literature]] | https://jainknowledge.com / https://jaingpt.org/ |
| 2 | [[0000-project-Vedanta Datasets]] | https://github.com/atmabodha/Vedanta_Datasets |
| 3 | [[0000-projects-BaniDB Shabad OS Digital Gurbani Database]] | https://github.com/KhalisFoundation/banidb-api / https://github.com... |
| 4 | [[2010-Project-GurbaniDB]] | https://github.com/sikher/gurbanidb |
| 5 | [[2016-Fonseca-ASSIN Avaliação de Similaridade Semântica e INferência textual]] | https://huggingface.co/datasets/nilc-nlp/assin2 |
| 6 | [[2016-Purzycki-Cross-cultural dataset for the evolution of]] | https://doi.org/10.7910/DVN/ERKCLS |
| 7 | [[2016-Purzycki-Religious Belief and the Moral Circle]] | https://github.com/FilipeMaia/owl |
| 8 | [[2018-Amram-Representations and Architectures in Neural Sentiment Analysis for]] | https://github.com/omilab/Neural-Sentiment-Analyzer-for-Modern-Hebrew |
| 9 | [[2018-Awad-The Moral Machine experiment]] | https://goo.gl/JXRrBP |
| 10 | [[2018-Behzadan-TrolleyMod v1.0]] | https://github.com/zminton/TrolleyMod/wiki |
| 11 | [[2018-Bohra-Hindi-English Code-Mixed Social Media Text for]] | https://github.com/deepanshu1995/HateSpeech-Hindi-English-Code-Mixe... |
| 12 | [[2018-Dixon-Measuring and Mitigating Unintended Bias in Text]] | https://github.com/conversationai/unintended-ml-bias-analysis |
| 13 | [[2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred]] | http://saifmohammad.com/WebPages/Biases-SA.html |
| 14 | [[2018-Ljubesic-Datasets of Slovene and Croatian Moderated News Comments]] | http://hdl.handle.net/11356/1201 |
| 15 | [[2018-Mishra-Are They Our Brothers Analysis and]] | https://github.com/nuhaalbadi/Arabic_hatespeech |
| 16 | [[2018-Nguyen-UIT-VSFC Vietnamese Students' Feedback Corpus for Sentiment Analysis]] | https://github.com/kietnv/uit-vsfc |
| 17 | [[2018-Wiegand-GermEval 2018 Shared Task on the Identification of Offensive Language]] | https://projects.cai.fbi.h-da.de/iggsa/ |
| 18 | [[2018-Zhao-Gender Bias in Coreference Resolution]] | https://github.com/rudinger/winogender-schemas |
| 19 | [[2019-Basile-SemEval-2019 Task 5 Multilingual Detection of Hate Speech Against]] | https://github.com/jaredks/tweetokenize |
| 20 | [[2019-De-Arteaga-Bias in Bios]] | http://aka.ms/biasbios |
| 21 | [[2019-Fortuna-A Hierarchically-Labeled Portuguese Hate Speech Dataset]] | https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset |
| 22 | [[2019-Ibrohim-Multi-label Hate Speech and Abusive Language]] | https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusi... |
| 23 | [[2019-Jikeli-Annotating Antisemitic Online Content Towards an]] | http://github.com/zeerakw/hatespeech |
| 24 | [[2019-Ljubesic-The FRENK Datasets of Socially Unacceptable Discourse in Slovene and]] | https://github.com/UCSM-DUE/IWG_hatespeech_public |
| 25 | [[2019-Ptaszynski-Results of the PolEval 2019 Shared Task 6 First Dataset and Open]] | https://github.com/ptaszynski/cyberbullying-Polish |
| 26 | [[2019-Stanovsky-Evaluating Gender Bias in Machine Translation WinoMT]] | https://github.com/gabrielStanworthy/mt_gender |
| 27 | [[2019-Usbeck-Benchmarking question answering systems]] | https://github.com/AKSW/NLIWOD |
| 28 | [[2019-collaboration-help_dicrah A ML-based hate speech detection tool on Twitter in French]] | https://github.com/Mik3M4n/help_dicrah |
| 29 | [[2020-Awad-Universals and variations in moral decisions made]] | https://bit.ly/2Y7Brr9 |
| 30 | [[2020-Hoover-Moral Foundations Twitter Corpus]] | https://github.com/limteng-rpi/moral_annotation_tool |
| 31 | [[2020-Schramowski-The Moral Choice Machine]] | https://github.com/ml-research/moral-choice-machine-v2 |
| 32 | [[2020-Souza-BERTimbau Pretrained BERT Models for Brazilian Portuguese]] | https://huggingface.co/neuralmind/bert-base-portuguese-cased |
| 33 | [[2020-Srivastava-A Multi-Dimensional View of Aggression when]] | https://github.com/arjitsrivastava/MultidimensionalViewOpinionMining |
| 34 | [[2020-Sälevä-A Multi-Orthography Parallel Corpus of Yiddish Nouns]] | https://github.com/sequitur-g2p/sequitur-g2p |
| 35 | [[2020-Whaanga-Indigenous Protocol and Artificial Intelligence Position]] | https://www.indigenous-ai.net/position-paper/ |
| 36 | [[2020-Yasseri-Detecting Weak and Strong Islamophobic Hate]] | https://github.com/bvidgen/Weak_strong_Islamophobia |
| 37 | [[2021-Azada-Fake News Detection in Low-Resourced Languages Kurdish Language Using]] | https://www.kaggle.com/raniaazad/kurdish-fake-news-dataset |
| 38 | [[2021-Cao-Toward Gender-Inclusive Coreference Resolution]] | https://github.com/TristaCao/into_inclusivecoref |
| 39 | [[2021-Croce-RobustBench]] | https://github.com/RobustBench/robustbench |
| 40 | [[2021-Hansson-The Swedish Winogender Dataset SweWinogender]] | https://spraakbanken.gu.se/en/resources/swewinogender |
| 41 | [[2021-Pronoza-Detecting Ethnicity-Targeted Hate Speech in Russian Social Media Texts]] | https://github.com/hse-scila/ethnohate-project |
| 42 | [[2021-Sogaard-Itihasa A Large-Scale Corpus for Sanskrit]] | https://github.com/rahular/itihasa |
| 43 | [[2021-collaborators-Optimisation of the Largest Annotated Tibetan]] | https://zenodo.org/records/3951503 ; https://github.com/lothelanor/... |
| 44 | [[2022-Atwell-Challenging the Transformer-based Models with a]] | https://github.com/ShathaTm/Quran_Hadith_Datasets |
| 45 | [[2022-Bago-Situational factors shape moral judgments in the]] | https://github.com/marton-balazs-kovacs/trolleyMultilabReplication |
| 46 | [[2022-Chakravarthi-DravidianCodeMix Sentiment Analysis and Offensive Language]] | https://github.com/bharathichezhiyan/DravidianCodeMix-Dataset, http... |
| 47 | [[2022-Multiple Data in Brief-Sanadset 650K Data on Hadith Narrators]] | https://data.mendeley.com/datasets/5xth87zwb5/4 |
| 48 | [[2022-Network-How can NLP Help Revitalize Endangered Languages]] | https://github.com/ZhangShiyue/RevitalizeCherokee |
| 49 | [[2022-Nkemelu-Tackling Hate Speech in Low-resource Languages]] | https://github.com/TID-Lab/myanmarhsc |
| 50 | [[2022-Pollak-Embeddings Models for Buddhist Sanskrit]] | https://figshare.com/articles/code/Gitlab_repository_of_Embeddings_... |
| 51 | [[2022-Romim-BD-SHS A Benchmark Dataset for Learning to Detect Online Bangla Hate]] | https://github.com/naurosromim/hate-speech-dataset-for-Bengali-soci... |
| 52 | [[2022-Saeed-Hate Speech Detection in Social Media for the Kurdish Language]] | https://data.mendeley.com/datasets/x6628zzpdx/1 |
| 53 | [[2022-Trye-Harnessing Indigenous Tweets]] | https://github.com/TeHikuMedia/nga-kupu |
| 54 | [[2023-2023-Hadiths Classification Using a Novel Author-Based]] | Papers with Code listing |
| 55 | [[2023-Alsalka-HAQA and QUQA Constructing Two Arabic]] | http://github.com/scsaln/HAQA-and-QUQA |
| 56 | [[2023-Alsalka-Is GPT-4 a Good Islamic Expert]] | QUQA dataset (available via thesis/ACL) |
| 57 | [[2023-Alyemny-A Data-Driven Exploration of a New Islamic Fatwas]] | https://github.com/ohoud/Fatwaset.git |
| 58 | [[2023-Alyemny-FatwaSet]] | https://github.com/ohoud/Fatwaset.git |
| 59 | [[2023-Aroyo-DICES Dataset]] | https://github.com/google-research-datasets/dices-dataset/ |
| 60 | [[2023-Astobiza-MoralNet]] | https://osf.io/dbyw7 |
| 61 | [[2023-Bakrola-SAHAAYAK 2023 The Multi-Domain Bilingual Parallel]] | https://rb.gy/hf6bp |
| 62 | [[2023-DN-HeQ a Large and Diverse Hebrew Reading Comprehension Benchmark]] | https://github.com/NNLP-IL/Hebrew-Question-Answering-Dataset |
| 63 | [[2023-Das-Toward Cultural Bias Evaluation Datasets The Case of Bengali Gender]] | https://zenodo.org/record/7775521 |
| 64 | [[2023-Feng-Case Repositories]] | https://github.com/social-futures-lab/case-law-ai-policy |
| 65 | [[2023-Gustafson-FACET]] | https://facet.metademolab.com |
| 66 | [[2023-Huang-AceGPT Localizing Large Language Models in Arabic]] | https://github.com/FreedomIntelligence/AceGPT |
| 67 | [[2023-Ji-Safety Gymnasium]] | https://sites.google.com/view/safety-gymnasium |
| 68 | [[2023-Keutzer-MITRA-zh An Efficient Open Machine Translation]] | Open-source (Dharmamitra project) |
| 69 | [[2023-Khan-The Tarteel Dataset Crowd-Sourced and Labeled]] | Tarteel.ai / Quranic Universal Library |
| 70 | [[2023-Lee-VisAlign]] | https://github.com/jiyounglee-0523/VisAlign |
| 71 | [[2023-Lin-Taiwan LLM Bridging the Linguistic Divide with a Culturally Aligned]] | https://github.com/MiuLab/Taiwan-LLM |
| 72 | [[2023-Lu-The Chai Platform's AI Safety Framework]] | https://huggingface.co/hakurei/lit-6B |
| 73 | [[2023-Miah-Islam QA]] | https://www.kaggle.com/datasets/mamun18/islam-qa-dataset |
| 74 | [[2023-Muhammad-AfriSenti]] | https://github.com/afrisenti-semeval/afrisent-semeval-2023 |
| 75 | [[2023-Ramezani-Knowledge of Cultural Moral Norms in Large Language Models]] | https://github.com/AidaRamezani/cultural_inference |
| 76 | [[2023-Shmidman-Introducing DictaLM - A Large Generative Language Model for Modern]] | https://huggingface.co/dicta-il/dictalm-7b |
| 77 | [[2023-Takeshita-JCommonsenseMorality Japanese Dataset for Evaluating Commonsense]] | https://github.com/Language-Media-Lab/commonsense-moral-ja |
| 78 | [[2023-TheDevastator-HelpSteer A-i Alignment Dataset]] | https://www.kaggle.com/datasets/thedevastator/helpsteer-ai-alignmen... |
| 79 | [[2023-TheDevastator-OpenAssistant Conversations (OASST1)]] | https://www.kaggle.com/datasets/thedevastator/multilingual-conversa... |
| 80 | [[2023-University-Antisemitism on Twitter A Dataset for]] | https://zenodo.org/records/7932888 |
| 81 | [[2023-[[Unknown]]-NEHATE Large-Scale Annotated Data Shedding Light]] | https://github.com/shucoll/NEHate |
| 82 | [[2024-Acikgoz-Bridging the Bosphorus Advancing Turkish Large Language Models]] | https://emrecanacikgoz.github.io/Bridging-the-Bosphorus/ |
| 83 | [[2024-Akhunzada-Multi-IsnadSet MIS for Sahih Muslim Hadith]] | https://data.mendeley.com/datasets/gzprcr93zn/2 |
| 84 | [[2024-Azerbaijan-Azerbaijani Toxicity Classifier]] | https://huggingface.co/LocalDoc/azerbaijani_toxicity_classifier |
| 85 | [[2024-Chen-Measuring Taiwanese Mandarin Language Understanding TMLU]] | https://github.com/MiuLab/TMLU |
| 86 | [[2024-Clarke-GuyLingo The Republic of Guyana Creole Corpora]] | https://github.com/chrisisking/caribbean-creole-languages-translation |
| 87 | [[2024-Crepelle-Tribes and AI Possibilities for Tribal Sovereignty]] | https://scholarship.law.duke.edu/cgi/viewcontent.cgi?article=1389&c... |
| 88 | [[2024-Defrance-ABCFair]] | https://github.com/aida-ugent/abcfair |
| 89 | [[2024-Enkhbold-A new dataset for mongolian online handwritten recognition]] | https://www.kaggle.com/fandaoerji/molhw-ooo |
| 90 | [[2024-Farina-AI and Society Virtue Ethics Approach]] | https://github.com/git/git |
| 91 | [[2024-Gaikwad-MoralBench A Multi-Faceted Benchmark for Ethical and Safety Alignment]] | https://github.com/krimler/moralbench |
| 92 | [[2024-Garcia-Open Portuguese LLM Leaderboard]] | https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard |
| 93 | [[2024-Gordic-Serbian LLM Evaluation Dataset]] | https://github.com/gordicaleksa/serbian-llm-eval |
| 94 | [[2024-Hadi-The Dark Side of Instagram A Large Dataset for Identifying Persian]] | https://github.com/davardoust/PHICAD |
| 95 | [[2024-Hall-Towards Geographic Inclusion in the Evaluation of Text-to-Image Models]] | https://github.com/facebookresearch/DIG-In |
| 96 | [[2024-Hasan-NativQA Multilingual Culturally-Aligned Natural Query for LLMs]] | https://huggingface.co/datasets/QCRI/MultiNativQA |
| 97 | [[2024-Hellwig-The Vedic Compound Dataset]] | https://github.com/SvenSellmer/VedicCompoundDataset |
| 98 | [[2024-Jones-Fit for Our Purpose Not Yours]] | https://papareo.nz/ |
| 99 | [[2024-Kajiwara-Hate Speech and Offensive Language Dataset]] | https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-la... |
| 100 | [[2024-LLM-Beetle-Azerbaijani LLM Leaderboard]] | https://huggingface.co/spaces/LLM-Beetle/azerbaijani-llm-leaderboard |
| 101 | [[2024-Lab-AfroBench Multi-task Benchmark for Evaluating LLMs in African]] | https://mcgill-nlp.github.io/AfroBench/ |
| 102 | [[2024-Laszkiewicz-Benchmarking Fairness in Image Upsampling]] | https://github.com/MikeLasz/Benchmarking-Fairness-ImageUpsampling |
| 103 | [[2024-Lee-KorNAT]] | https://huggingface.co/datasets/jiyounglee0523/KorNAT |
| 104 | [[2024-Levine-Religious Affiliation and Conceptions of the]] | https://github.com/sydneylevine/moral-domain |
| 105 | [[2024-Li-CulturePark Boosting Cross-cultural Understanding in Large Language]] | https://github.com/Scarelette/CulturePark |
| 106 | [[2024-Masood-Hadith QA Pairs Dataset]] | https://www.kaggle.com/datasets/rwmasood/hadith-qa-pairs |
| 107 | [[2024-Maxutov-Do LLMs Speak Kazakh A Pilot Evaluation of Seven Models]] | https://github.com/akylbekmaxutov/LLM-eval-using-Kazakh |
| 108 | [[2024-Mazzara-Quranic Audio Dataset Crowdsourced and Labeled]] | https://huggingface.co/datasets/RetaSy/quranic_audio_dataset |
| 109 | [[2024-Miðeind-IcelandicEval Utilities to generate Icelandic evaluation data sets]] | https://github.com/mideind/IcelandicEval |
| 110 | [[2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs]] | https://huggingface.co/datasets/QCRI/AraDiCE |
| 111 | [[2024-Multiple Data in Brief-MASAQ Morphologically-Analyzed and Syntactically-Annotated Quran Dataset]] | https://data.mendeley.com/datasets/9yvrzxktmr |
| 112 | [[2024-Murtala-A multilingual dataset for offensive language]] | https://github.com/bharathichezhiyan/DravidianCodeMix-Dataset, http... |
| 113 | [[2024-Myers-People Expect Artificial Moral Advisors]] | https://osf.io/m3v48/ |
| 114 | [[2024-Nayak-Benchmarking Vision Language Models for Cultural Understanding]] | https://culturalvqa.org/ |
| 115 | [[2024-Neplenbroek-MBBQ A Dataset for Cross-Lingual Comparison of Stereotypes in]] | https://github.com/Veranep/MBBQ |
| 116 | [[2024-Nom-KhmerST A Low-Resource Khmer Scene Text]] | https://gitlab.com/vannkinhnom123/khmerst |
| 117 | [[2024-Olatunji-AfriMed-QA A Pan-African Multi-Specialty Medical Question-Answering]] | https://afrimedqa.com/ |
| 118 | [[2024-Overfit-GM-Turkish Overfit-GM Toxic Language Dataset]] | https://huggingface.co/datasets/Overfit-GM/turkish-toxic-language |
| 119 | [[2024-Park-Understanding LLM Development Through Longitudinal Study Insights]] | https://github.com/tatsu-lab/alpaca_eval |
| 120 | [[2024-Phyo-Development and Evaluation of Myanmar GPT]] | https://huggingface.co/jojo-ai-mst/MyanmarGPT |
| 121 | [[2024-Pistilli-CIVICS Building a Dataset for Examining Culturally-Informed Values in]] | https://huggingface.co/datasets/llm-values/CIVICS |
| 122 | [[2024-Qian-CamelEval Advancing Culturally Aligned Arabic Language Models and]] | https://huggingface.co/elmrc |
| 123 | [[2024-Quang-Vietnamese Law and Ethics Multiple-Choice Questions VLEMCQ]] | https://huggingface.co/datasets/nqdhocai/vietnamese-legal-qa |
| 124 | [[2024-Sagyndyk-Kazakh Dastur-MC Multiple Choice Benchmark]] | https://huggingface.co/datasets/kz-transformers/kazakh-dastur-mc |
| 125 | [[2024-Seth-DOSA A Dataset of Social Artifacts from Different Indian Geographical]] | https://github.com/microsoft/DOSA |
| 126 | [[2024-Shi-CultureBank An Online Community-Driven Knowledge Base Towards]] | https://huggingface.co/datasets/SALT-NLP/CultureBank |
| 127 | [[2024-So-How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas]] | https://github.com/famous-blue-raincoat/AI_Ethics_Discourse |
| 128 | [[2024-Tam-An Improved Traditional Chinese Evaluation Suite for Foundation Model]] | https://huggingface.co/datasets/ikala/tmmluplus |
| 129 | [[2024-Tennant-Dynamics of Moral Behavior in Heterogeneous Populations]] | https://github.com/Liza-Tennant/moral_MARL |
| 130 | [[2024-Thu-Development and Evaluation of Myanmar GPT A Language Model for]] | https://huggingface.co/jojo-ai-mst/MyanmarGPT |
| 131 | [[2024-Thu-MixCuBe When Tom Eats Kimchi - Evaluating Cultural Awareness of]] | https://huggingface.co/datasets/kyawyethu/MixCuBe |
| 132 | [[2024-Toygar-Turkish Offensive Language Detection Dataset]] | https://huggingface.co/datasets/Toygar/turkish-offensive-language-d... |
| 133 | [[2024-Trajano-OLID-BR Offensive Language Identification Dataset for Brazilian]] | https://github.com/DougTrajano/olid-br |
| 134 | [[2024-Unknown-CulturalVQA Evaluating VLMs' Geo-Diverse Cultural Understanding]] | https://huggingface.co/datasets/mair-lab/CulturalVQA |
| 135 | [[2024-Unknown-Seeing Culture Benchmark Evaluating VLMs on Culturally Rich Images]] | https://huggingface.co/datasets/Multimedia-SMU/seeingculture-benchmark |
| 136 | [[2024-Unknown-WoNBias A Complete Bengali Gender Bias Dataset]] | https://huggingface.co/datasets/gender-bias-bengali/wonbias-complet... |
| 137 | [[2024-Varshney-Decolonial AI Alignment - Openness Visesa-Dharma and Including]] | https://huggingface.co/Jacaranda/UlizaLlama |
| 138 | [[2024-Vladimirova-FairJob]] | https://huggingface.co/datasets/criteo/FairJob |
| 139 | [[2024-Wang-XSafety Multilingual Safety Benchmark]] | https://github.com/Jarviswang94/Multilingual_safety_benchmark |
| 140 | [[2024-Wong-The Humanistic Buddhism Corpus (HBC)]] | https://www.fgstranslation.org/hbc |
| 141 | [[2024-Sagyndyk-Kazakh Dastur-MC Multiple Choice Benchmark]] | https://huggingface.co/datasets/kz-transformers/kazakh-dastur-mc |
| 142 | [[2024-Yin-SafeWorld Geo-Diverse Safety Alignment]] | https://github.com/PlusLabNLP/SafeWorld |
| 143 | [[2024-Yolgoermez-Abundant Intelligences Placing AI Within Indigenous]] | https://www.indigenous-ai.net/ ; https://abundant-intelligences.net/ |
| 144 | [[2024-Yu-The Unseen Targets of Hate – A Systematic Review of Hateful]] | https://github.com/uzeui/HateComm_Review.git |
| 145 | [[2024-community-Open Leaderboard for Hebrew LLMs]] | https://huggingface.co/blog/leaderboard-hebrew |
| 146 | [[2024-group-ITA-Bench Towards a More Comprehensive Evaluation for Italian LLMs]] | https://github.com/SapienzaNLP/ita-bench |
| 147 | [[2024-project-DharmicData Comprehensive Open-Source Collection of Hindu]] | https://github.com/bhavykhatri/DharmicData (ODbL license) |
| 148 | [[2024-team-Indic-Bias A Comprehensive Benchmark for Fairness]] | https://huggingface.co/datasets/ai4bharat/Indic-Bias |
| 149 | [[2024-team-Indic-Bias A Comprehensive Benchmark to Evaluate]] | https://github.com/AI4Bharat/indic-bias |
| 150 | [[2024-team-MahaMarathi-7B Marathi Large Language Model]] | https://huggingface.co/marathi-llm/MahaMarathi-7B-v24.01-Base |
| 151 | [[2024-Ògúnrẹ̀mí-ÌròyìnSpeech A Multi-purpose Yorùbá Speech Corpus]] | https://github.com/Niger-Volta-LTI/yoruba-voice |
| 152 | [[2025-ADL Center for Technology and Society Daniel Kelley-Generating Hate Anti-Jewish and Anti-Israel Bias]] | https://www.adl.org/resources/report/generating-hate-anti-jewish-an... |
| 153 | [[2025-Akpobi-Yankari Monolingual Yoruba Dataset]] | https://huggingface.co/datasets/acflp/YANKARI |
| 154 | [[2025-Almeida-BRoverbs - Measuring how much LLMs understand Portuguese proverbs]] | https://huggingface.co/datasets/Tropic-AI/BRoverbs |
| 155 | [[2025-Bar-DharmaBench Evaluating Language Models on Buddhist]] | Publicly released under CC-BY-4 License (code under Apache-2.0) |
| 156 | [[2025-Benavoli-AI Safety Uncertainty Incomplete Preferences]] | https://github.com/benavoli/prefGP |
| 157 | [[2025-Center-Personal Consultations Case Study Database]] | https://www.ncbcenter.org/case-study-database |
| 158 | [[2025-Choi-No Language Data Left Behind A Comparative Study of CJK Language]] | https://songys.github.io/Korean-HF-datasets-catalog/, https://songy... |
| 159 | [[2025-Coalition-The Gospel Coalition AI Christian Benchmark]] | https://www.thegospelcoalition.org/ai-christian-benchmark/ |
| 160 | [[2025-Cognitive-Cognitive LLMs Toward Human-Like Artificial Intelligence by]] | https://github.com/SiyuWu528/LLM-ACTR |
| 161 | [[2025-Dementieva-TextDetox Multilingual Toxicity Dataset]] | https://huggingface.co/datasets/textdetox/multilingual_toxicity_dat... |
| 162 | [[2025-Devane-BhashaBench V1 A Comprehensive Benchmark for the Quadrant of Indic]] | https://huggingface.co/datasets/bharatgenai/BhashaBench-Legal |
| 163 | [[2025-Dou-Sailor2 Sailing in South-East Asia with Inclusive Multilingual LLMs]] | https://github.com/sail-sg/sailor2 |
| 164 | [[2025-Emezue-NaijaVoices]] | https://naijavoices.com/ |
| 165 | [[2025-Group-AILuminate LLM v1.1 Adding French Language Capabilities to]] | https://github.com/mlcommons/ailuminate |
| 166 | [[2025-Halgamuge-Indigenous Peoples and Artificial Intelligence A]] | https://osf.io/6hrqj/download |
| 167 | [[2025-Hsieh-TaiwanVQA A Benchmark for Visual Question Answering for Taiwanese]] | https://huggingface.co/datasets/hhhuang/TaiwanVQA |
| 168 | [[2025-IDB-The Performance of Artificial Intelligence in the Use of Indigenous]] | https://publications.iadb.org/publications/english/document/The-Per... |
| 169 | [[2025-Jigsaw-Jigsaw Multilingual Toxic Comment Classification]] | https://www.kaggle.com/competitions/jigsaw-multilingual-toxic-comme... |
| 170 | [[2025-Kim-A Dual-Layered Evaluation of Geopolitical and Cultural Bias in LLMs]] | https://github.com/seank021/LLM-Bias-Evaluation |
| 171 | [[2025-Koto-Sherkala-Chat Building a State-of-the-Art LLM for Kazakh in a]] | https://huggingface.co/inceptionai/Llama-3.1-Sherkala-8B-Chat |
| 172 | [[2025-Lee-Knowing the Words Missing the Meaning Evaluating LLMs' Cultural]] | https://github.com/es133lolo/Knowing-the-Words-Missing-the-Meaning |
| 173 | [[2025-Liu-CultureVLM Characterizing and Improving Cultural Understanding of]] | https://culturevlm.github.io/ |
| 174 | [[2025-Liu-JailBench A Comprehensive Chinese Security Assessment Benchmark for]] | https://github.com/STAIR-BUPT/JailBench |
| 175 | [[2025-Lyu-Characterizing Bias Benchmarking Large Language Models in Simplified]] | https://github.com/brucelyu17/SC-TC-Bench |
| 176 | [[2025-Ma-Algorithmic Fidelity of Large Language Models in Generating Synthetic]] | https://github.com/soda-lmu/llm-opinion-german |
| 177 | [[2025-Masood-Neural Machine Translation for Low-Resource Languages from a]] | https://github.com/joshua-decoder/indian-parallel- |
| 178 | [[2025-Masoud-Cultural Alignment in Large Language Models An Explanatory Analysis]] | https://github.com/reemim/Hofstedes_CAT |
| 179 | [[2025-Mayor-Rocher-Spanish Is Not Just One A Dataset of Spanish Dialect Recognition for]] | https://zenodo.org/records/15101403 |
| 180 | [[2025-Mekki-NileChat Towards Linguistically Diverse and Culturally Aware LLMs for]] | https://github.com/UBC-NLP/nilechat |
| 181 | [[2025-Monazzah-PerCul A Story-Driven Cultural Evaluation of LLMs in Persian]] | https://huggingface.co/datasets/teias-ai/percul |
| 182 | [[2025-Naous-Camellia Benchmarking Cultural Biases in LLMs for Asian Languages]] | https://github.com/tareknaous/camellia |
| 183 | [[2025-Naous-On The Origin of Cultural Biases in Language Models From Pre-training]] | https://github.com/tareknaous/camel2 |
| 184 | [[2025-Nguyen-VietMEAgent Culturally-Aware Few-Shot Multimodal Explanation for]] | https://huggingface.co/datasets/Dangindev/viet-cultural-vqa |
| 185 | [[2025-Niklaus-SwiLTra-Bench The Swiss Legal Translation Benchmark]] | https://github.com/JoelNiklaus/SwissLegalTranslations |
| 186 | [[2025-Ning-seeBias]] | https://github.com/nliulab/seeBias |
| 187 | [[2025-Ofli-Multimodal Social Media Data Analysis in]] | http://crisisnlp.qcri.org/ |
| 188 | [[2025-Krutrim-BharatBench Comprehensive Multilingual Multimodal Evaluations of]] | https://github.com/ola-krutrim/BharatBench |
| 189 | [[2025-Qiu-Evaluating Cultural and Social Awareness of LLM Web Agents]] | https://github.com/SalesforceAIResearch/CASA |
| 190 | [[2025-Salnikov-Geopolitical biases in LLMs what are the 'good' and the 'bad']] | https://airi-institute.github.io/geopolitical_llm_bias/ |
| 191 | [[2025-Schacht-Mapping Moral Reasoning Circuits]] | https://github.com/coairesearch/mapping_moral_reasoning.git |
| 192 | [[2025-Team-Annotated Slovak Datasets for Toxicity Hate Speech and Sentiment]] | https://huggingface.co/datasets/TUKE-KEMT/toxic-sk, https://hugging... |
| 193 | [[2025-Topal-How do LLMs perform on Turkish A multi-faceted multi-prompt evaluation]] | https://huggingface.co/collections/Holmeister/turkish-llm-multi-pro... |
| 194 | [[2025-Unknown-Generative Artificial Intelligence and Indigenous Knowledge Systems]] | https://lettersinhighenergyphysics.com/index.php/LHEP/article/downl... |
| 195 | [[2025-Unknown-HuGME A Benchmark System for Evaluating Hungarian Generative Model]] | https://hugme.nytud.hu/ |
| 196 | [[2025-Unknown-IslamTrust A Benchmark for LLMs Alignment]] | https://github.com/aii-lab-dot-org/IslamTrust and https://huggingfa... |
| 197 | [[2025-Unknown-LLM Ethics Benchmark A Three-Dimensional Assessment System for]] | https://github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark |
| 198 | [[2025-Unknown-MIZAN A Persian LLM Leaderboard]] | https://huggingface.co/spaces/MCINext/mizan-llm-leaderboard |
| 199 | [[2025-Unknown-Multi-lingual HateSpeech Dataset]] | https://www.kaggle.com/datasets/wajidhassanmoosa/multilingual-hates... |
| 200 | [[2025-Wu-AlignMMBench Evaluating Chinese Multimodal Alignment in Large]] | https://github.com/THUDM/AlignMMBench |
| 201 | [[2025-Xiong-BuddhismEval A Bilingual Benchmark for Buddhist]] | https://huggingface.co/datasets/Nethmi14/BuddhismEval |
| 202 | [[2025-Xiong-BuddhismEval Bilingual Evaluation Benchmark for Buddhist]] | https://huggingface.co/datasets/Nethmi14/BuddhismEval |
| 203 | [[2025-Yang-OpenHuEval Evaluating Large Language Model on Hungarian Specifics]] | https://github.com/opendatalab/OpenHuEval |
| 204 | [[2025-initiative-CatholicBench]] | https://www.catholicbench.com/ |
| 205 | [[2025-initiative-Faith Respect and Moral Compass in]] | In development (collaborating with BYU, Notre Dame, Baylor, Yeshiva) |
| 206 | [[2025-initiative-FaithBench AI Benchmark for Christian Theology]] | https://faithbench.com/ |
| 207 | [[2025-onejune2018-Awesome-LLM-Eval Repository Meta-Resource]] | https://github.com/AthenaCore/AwesomeResponsibleAI |
| 208 | [[2025-project-Kaku-Ora Zen Wisdom Diffused -- An]] | GitHub (code available); HuggingFace Spaces (model hosted) |
| 209 | [[2026-Alam-Quran-MD A Fine-Grained Multilingual Multimodal Dataset]] | https://huggingface.co/datasets/Buraaq/quran-audio-text-dataset |
| 210 | [[2026-Guey-BiasLab Multilingual Dual-Framing Framework]] | https://github.com/williamguey/LLMbiaslab |
| 211 | [[2026-Vargas-Self-Explaining Hate Speech Detection with Moral Rationales]] | https://github.com/franciellevargas/SMRA |

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
