# vendor/ — external inputs vendored for self-containment

## `v1-bank-yaml/`

A frozen copy of the **WCF-Benchmark v1 item-bank YAML**, vendored so this project can
regenerate its datasets without depending on a sibling folder.

- **Copied from:** `../WCF-Benchmark/05-BANK-YAML/` (v1 predecessor project)
- **Copied on:** 2026-07-17
- **Contents:** 40 `*.yaml` exemplar/expansion files + 3 `*.md` spec/audit docs (1.2 MB)
- **Status:** read-only source of truth for `convert/yaml_to_jsonl.py`. Treat as frozen —
  never edit the vendored copy; if the v1 bank is ever revised upstream, re-copy the whole
  directory and note the new date here.

### Why vendored
`convert/yaml_to_jsonl.py` previously read the bank from `../WCF-Benchmark/05-BANK-YAML/`
at run time — the project's one runtime dependency on a folder outside itself. Vendoring a
frozen copy severs that coupling so `WCF-Benchmark-v2/` is fully self-contained and portable
(the whole folder can be moved, archived, or handed off as a single unit and the conversion
pipeline still re-runs). The upstream v1 copy is left untouched and remains canonical.
