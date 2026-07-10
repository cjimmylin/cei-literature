# Model Comparison

| model | vendor | rubric_origin | gradient_holds | knowledge_mean_length | reasoning_mean_length | values_mean_length | bias_values_r | rubric_values | t2_accuracy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude-opus-4-6 | Anthropic | original | True | 1853.1 | 4586.3 | 6326.9 | 0.706 | 0.933 | 1.0 |
| claude-sonnet-4-20250514 | Anthropic | original | True | 1771.1 | 5194.1 | 6363.8 | 0.288 | 1.0 | 1.0 |
| claude-haiku-4-5-20251001 | Anthropic | original | True | 765.7 | 3354.3 | 7025.6 | 0.701 | 1.0 | 0.767 |
| gpt-codex | OpenAI | original | False | 81.7 | 471.7 | 460.7 | 0.296 | 0.8667 | 1.0 |
| gpt-codex-mini | OpenAI | original | True | 78.2 | 414.7 | 415.9 | 0.076 | 0.9 | 0.8667 |
| gemini-2.5-flash-lite | Gemini | backfilled | False | 63.3 | 104.3 | 101.2 | 1.0 | 0.2 | 0.2 |
| gemini-2.5-flash | Gemini | backfilled | False | 200.7 | 267.7 | 222.2 | 1.0 | 0.0 | 0.1 |
| gemini-2.5-pro | Gemini | backfilled | False | 230.7 | 305.3 | 244.4 | 1.0 | 0.0 | 0.0667 |
| gemini-3.1-pro | Gemini | backfilled | False | 309.7 | 328.3 | 318.4 | 1.0 | 0.0 | 0.1 |
