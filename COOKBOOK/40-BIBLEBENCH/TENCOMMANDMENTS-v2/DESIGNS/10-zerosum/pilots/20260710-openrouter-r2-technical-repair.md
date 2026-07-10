# OpenRouter forced diagnostic R2 technical transport repair

Date: 2026-07-10

R2 is a separately frozen transport protocol. It does not reinterpret or
overwrite the v1 diagnostic, and it does not change any inferential threshold,
model roster, item schedule, seed, blocker, scoring rule, or eligibility rule.

The repair is motivated by a transport-level truncation observed under v1. A
failing forced item returned `finish_reason=length`, native finish reason
`max_output_tokens`, null content, 512 completion tokens, and 512 reasoning
tokens. A minimal technical probe of that same request with
`reasoning_effort=minimal` returned stopped content using 195 completion tokens,
including 188 reasoning tokens. These observations diagnose output-budget
exhaustion; they are not benchmark score data and no score outcome is recorded
here.

R2 therefore freezes `max_tokens=1024` and `reasoning_effort=minimal`. The
original v1 config remains byte-for-byte frozen at SHA-256
`a22920456868293d51d92814f2daebc9f6de06e6948149c7427097b6291f9f41`.
R2 must use new smoke and full output directories, and only an R2 smoke proof
may authorize an R2 full run.
