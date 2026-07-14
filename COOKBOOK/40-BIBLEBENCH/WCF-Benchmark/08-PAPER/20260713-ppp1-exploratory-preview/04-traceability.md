# PPP-1 Traceability

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

Every empirical value in the packet is derived from `checkpoint.jsonl` through `02-normalized-cells.csv`. `scores.fraction` supplies ORDINAL, ANCHOR, and OPEN headline values; `judge.score` supplies EPISODE values; contested fields remain separate. `03-traceability.csv` enumerates each summary field and its contributing cell keys. Every normalized row also records its sequential raw-ledger line span, exact line/span hashes, paid-call count, actual-first cell cost, and judge-text hashes. Where parsed checkpoint judge text exists its hashes are reconciled to the raw ledger; error cells without persisted parsed judge text are labeled not-applicable rather than silently treated as a match. No raw prompt or response text is copied. Errors are retained without imputation.
