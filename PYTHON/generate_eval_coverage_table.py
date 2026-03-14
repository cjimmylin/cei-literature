#!/usr/bin/env python3
"""Generate eval framework coverage table (TABLE 1: Already Included).

Parses 4 eval framework reports from 2026-03-12 and builds a cross-reference
table showing which papers are already included in EleutherAI, lm-eval,
Inspect, and HELM frameworks.

lighteval and OpenAI Evals are listed as columns but marked '—' (these
reports assess implementability only, not existing coverage).

Usage:
    python PYTHON/generate_eval_coverage_table.py
"""

import re
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
VAULT   = Path(__file__).parent.parent
STATS   = VAULT / "STATISTICS"

ELEUTHERAI_REPORT = STATS / "20260312-eleutherai-eval-harness-integration.md"
HELM_REPORT       = STATS / "20260312-helm-values-alignment-integration-report.md"
LMEVAL_REPORT     = STATS / "20260312-lm-eval-implementability-report.md"
INSPECT_REPORT    = STATS / "20260312-inspect-eval-implementability-report.md"

OUTPUT_REPORT = STATS / "20260313-eval-already-included-comparison.md"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def normalize_key(raw: str) -> str:
    """Strip .md suffix, backticks, and surrounding whitespace."""
    return raw.strip().lstrip("`").rstrip("`").strip().removesuffix(".md").strip()


def build_alias_map(all_keys: set) -> dict:
    """Return {abbreviated_key: canonical_key} for cases where one key is
    a strict prefix of another (e.g. '2022-Parrish-BBQ' vs
    '2022-Parrish-BBQ Bias Benchmark for Question Answering').

    Only merges when the longer key begins with the shorter key followed
    by a space or end-of-string — prevents over-merging.
    """
    sorted_keys = sorted(all_keys, key=len)
    alias_map: dict[str, str] = {}

    for short in sorted_keys:
        for long in sorted_keys:
            if long == short:
                continue
            if not long.startswith(short):
                continue
            rest = long[len(short):]
            # Must be " " or " -" etc. — not just a substring of a word
            if rest and rest[0] not in (' ', '-'):
                continue
            # Map short → long (prefer already-resolved long key if chain)
            canonical = alias_map.get(long, long)
            alias_map[short] = canonical
            break  # take first (shortest extension) match

    return alias_map


def apply_aliases(d: dict, alias_map: dict) -> dict:
    """Re-key a dict through alias_map, keeping the canonical key."""
    out: dict[str, str] = {}
    for k, v in d.items():
        canon = alias_map.get(k, k)
        if canon not in out:          # first-seen wins
            out[canon] = v
    return out


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def parse_eleutherai(path: Path) -> dict:
    """Parse EleutherAI report → {canonical_key: task_id_string}.

    Covers:
    - Table 1 (16 existing papers): | N | Title | Benchmark | `task_id` |
    - Table 2 (6 new papers):       | N | Title | Key | arXiv | ... |
    """
    text = path.read_text()
    results: dict[str, str] = {}

    # --- Table 1 ---
    # Row format: | N | Title | Benchmark | `task1`, `task2` |
    # Stop when we hit Table 2
    in_table1 = False
    for line in text.splitlines():
        if "## Table 1" in line:
            in_table1 = True
            continue
        if in_table1 and line.startswith("## "):
            break
        if not in_table1:
            continue

        # Skip header / separator lines
        if re.match(r"^\|[-\s|]+\|$", line) or "|---|" in line:
            continue

        # Match rows: | N | Title | Benchmark | task_cell |
        m = re.match(
            r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|\s*[^|]+?\s*\|\s*([^|]+?)\s*\|",
            line,
        )
        if not m:
            continue
        title = m.group(1).strip()
        task_cell = m.group(2).strip()
        if title in ("Paper", "#") or not title:
            continue
        key = normalize_key(title)
        # Keep backtick-wrapped task IDs; skip header/separator text
        if "`" in task_cell:
            results[key] = task_cell
        elif task_cell not in ("EleutherAI Task", "---"):
            results[key] = f"`{task_cell}`" if task_cell else "✓"

    # --- Table 2 (new papers — task IDs not listed in table, mark ✓) ---
    in_table2 = False
    for line in text.splitlines():
        if "## Table 2" in line:
            in_table2 = True
            continue
        if in_table2 and line.startswith("## "):
            break
        if not in_table2:
            continue
        if re.match(r"^\|[-\s|]+\|$", line) or "|---|" in line:
            continue

        m = re.match(r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|", line)
        if not m:
            continue
        title = m.group(1).strip()
        if title in ("Paper", "#") or not title:
            continue
        key = normalize_key(title)
        if key and key not in results:
            results[key] = "✓"

    return results


def parse_helm(path: Path) -> dict:
    """Parse HELM report → {canonical_key: benchmark_name}.

    Covers:
    - Phase 1 (16 existing): | N | Benchmark | `filename.md` | Tagged |
    - Phase 2 (3 new):       | File | `papers/filename.md` (...) |
    """
    text = path.read_text()
    results: dict[str, str] = {}

    # --- Phase 1 ---
    in_phase1 = False
    for line in text.splitlines():
        if "## Phase 1" in line:
            in_phase1 = True
            continue
        if in_phase1 and line.startswith("## "):
            break
        if not in_phase1:
            continue
        if re.match(r"^\|[-\s|]+\|$", line) or "|---|" in line:
            continue

        # | N | Benchmark | `filename.md` | Tagged |
        m = re.match(
            r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|\s*`([^`]+\.md)`\s*\|\s*Tagged\s*\|",
            line,
        )
        if m:
            benchmark = m.group(1).strip()
            key = normalize_key(m.group(2))
            results[key] = benchmark

    # --- Phase 2 new papers: | File | `papers/filename.md` (...) | ---
    for m in re.finditer(r"\|\s*File\s*\|\s*`papers/([^`]+\.md)`", text):
        key = normalize_key(m.group(1))
        if key not in results:
            results[key] = "✓"

    return results


def parse_lmeval(path: Path) -> dict:
    """Parse lm-eval report → {canonical_key: task_id}.

    Section 1 table: | Paper | Year | Harness Task | Match Method | Availability |
    """
    text = path.read_text()
    results: dict[str, str] = {}

    in_section1 = False
    for line in text.splitlines():
        if "## 1. Already in lm-eval" in line:
            in_section1 = True
            continue
        if in_section1 and line.startswith("## "):
            break
        if not in_section1:
            continue
        if re.match(r"^\|[-\s|]+\|$", line) or "|---|" in line:
            continue

        # | Paper | Year | `task_id` | match_method | availability |
        m = re.match(
            r"^\|\s*([^|]+?)\s*\|\s*\d{4}\s*\|\s*`([^`]+)`\s*\|",
            line,
        )
        if not m:
            continue
        title = m.group(1).strip()
        task  = m.group(2).strip()
        if title in ("Paper",) or not title:
            continue
        key = normalize_key(title)
        if key and key not in results:
            results[key] = f"`{task}`"

    return results


def parse_inspect(path: Path) -> dict:
    """Parse Inspect report → {canonical_key: eval_id}.

    Section 1 table: | Paper.md | Inspect Eval | Category | Scorer |
    """
    text = path.read_text()
    results: dict[str, str] = {}

    in_section1 = False
    for line in text.splitlines():
        if "## 1. Already in Inspect" in line:
            in_section1 = True
            continue
        if in_section1 and line.startswith("## "):
            break
        if not in_section1:
            continue
        if re.match(r"^\|[-\s|]+\|$", line) or "|---|" in line:
            continue

        # | filename.md | eval_id | Category | Scorer |
        m = re.match(
            r"^\|\s*([^|]+?\.md)\s*\|\s*([^|]+?)\s*\|",
            line,
        )
        if not m:
            continue
        filename = m.group(1).strip()
        eval_id  = m.group(2).strip()
        if filename in ("Paper",) or not filename:
            continue
        key = normalize_key(filename)
        if key and key not in results:
            results[key] = f"`{eval_id}`"

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Parsing source reports…")
    eleutherai_raw = parse_eleutherai(ELEUTHERAI_REPORT)
    helm_raw       = parse_helm(HELM_REPORT)
    lmeval_raw     = parse_lmeval(LMEVAL_REPORT)
    inspect_raw    = parse_inspect(INSPECT_REPORT)

    print(f"  EleutherAI : {len(eleutherai_raw):3d}  (expected ~22)")
    print(f"  HELM       : {len(helm_raw):3d}  (expected ~19)")
    print(f"  lm-eval    : {len(lmeval_raw):3d}  (expected ~65)")
    print(f"  Inspect    : {len(inspect_raw):3d}  (expected ~38)")

    # Resolve cross-report duplicate keys (prefix-based merge)
    all_keys: set[str] = (
        set(eleutherai_raw) | set(helm_raw) | set(lmeval_raw) | set(inspect_raw)
    )
    alias_map = build_alias_map(all_keys)

    if alias_map:
        print(f"\nDuplicate keys merged ({len(alias_map)}):")
        for short, canon in sorted(alias_map.items()):
            print(f"  {short!r}\n    → {canon!r}")

    eleutherai = apply_aliases(eleutherai_raw, alias_map)
    helm       = apply_aliases(helm_raw, alias_map)
    lmeval     = apply_aliases(lmeval_raw, alias_map)
    inspect    = apply_aliases(inspect_raw, alias_map)

    # Union set
    all_papers: set[str] = set(eleutherai) | set(helm) | set(lmeval) | set(inspect)
    print(f"\nTotal unique papers after dedup: {len(all_papers)}")

    # Build rows
    rows = []
    for paper in all_papers:
        m = re.match(r"^(\d{4})", paper)
        year = int(m.group(1)) if m else 0

        e_val = eleutherai.get(paper, "")
        l_val = lmeval.get(paper, "")
        i_val = inspect.get(paper, "")
        h_val = helm.get(paper, "")
        covered = sum(1 for v in [e_val, l_val, i_val, h_val] if v)

        rows.append((paper, year, e_val, l_val, i_val, h_val, covered))

    # Sort: most-covered → year asc → name asc
    rows.sort(key=lambda r: (-r[6], r[1], r[0].lower()))

    # Summary stats
    total = len(rows)
    all4  = sum(1 for r in rows if r[6] == 4)
    e_only = sum(1 for r in rows if r[2] and not r[3] and not r[4] and not r[5])
    l_only = sum(1 for r in rows if r[3] and not r[2] and not r[4] and not r[5])
    i_only = sum(1 for r in rows if r[4] and not r[2] and not r[3] and not r[5])
    h_only = sum(1 for r in rows if r[5] and not r[2] and not r[3] and not r[4])

    # Pairwise overlaps (lower-triangle)
    def ov(fa, fb):
        return sum(1 for r in rows if fa(r) and fb(r))

    e = lambda r: bool(r[2])
    l = lambda r: bool(r[3])
    i = lambda r: bool(r[4])
    h = lambda r: bool(r[5])

    n_e = sum(1 for r in rows if e(r))
    n_l = sum(1 for r in rows if l(r))
    n_i = sum(1 for r in rows if i(r))
    n_h = sum(1 for r in rows if h(r))

    # ---------------------------------------------------------------------------
    # Build output
    # ---------------------------------------------------------------------------
    out_lines = [
        "# Eval Framework Coverage: Already Included (TABLE 1)",
        "",
        "Generated: 2026-03-13",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"- **Total unique papers already included in ≥1 framework:** {total}",
        f"- **Covered by all 4 trackable frameworks:** {all4}",
        f"- **EleutherAI only:** {e_only} &nbsp;|&nbsp; "
        f"**lm-eval only:** {l_only} &nbsp;|&nbsp; "
        f"**Inspect only:** {i_only} &nbsp;|&nbsp; "
        f"**HELM only:** {h_only}",
        "",
        "### Per-Framework Counts",
        "",
        f"| Framework | Papers | Notes |",
        f"|-----------|--------|-------|",
        f"| EleutherAI | {n_e} | Tagged `eleutherai: incorporated` |",
        f"| lm-eval | {n_l} | 'Already in Harness' tier |",
        f"| Inspect | {n_i} | 'Already in Inspect' tier |",
        f"| HELM | {n_h} | Tagged `helm: \"incorporated\"` |",
        f"| lighteval | — | Not tracked (implementability report only) |",
        f"| OpenAI Evals | — | Not tracked (implementability report only) |",
        "",
        "### Pairwise Overlap",
        "",
        "| | EleutherAI | lm-eval | Inspect | HELM |",
        "|---|---|---|---|---|",
        f"| **EleutherAI** ({n_e}) | — | {ov(e,l)} | {ov(e,i)} | {ov(e,h)} |",
        f"| **lm-eval** ({n_l}) | | — | {ov(l,i)} | {ov(l,h)} |",
        f"| **Inspect** ({n_i}) | | | — | {ov(i,h)} |",
        f"| **HELM** ({n_h}) | | | | — |",
        "",
        "---",
        "",
        "## TABLE 1 — Already Included",
        "",
        "Columns show the eval framework's internal task/benchmark ID for papers it already "
        "implements. Blank = not included. `—` = not tracked by that framework's report.",
        "",
        "| Paper | Year | EleutherAI | lm-eval | Inspect | HELM | lighteval | OpenAI Evals |",
        "|-------|------|-----------|---------|---------|------|-----------|--------------|",
    ]

    for paper, year, e_val, l_val, i_val, h_val, covered in rows:
        out_lines.append(
            f"| {paper} | {year} | {e_val} | {l_val} | {i_val} | {h_val} | — | — |"
        )

    out_lines += [
        "",
        "---",
        "",
        "## Notes",
        "",
        "- **Duplicate handling:** Keys where one is a strict prefix of another "
        "(e.g. `2022-Parrish-BBQ` vs `2022-Parrish-BBQ Bias Benchmark for Question Answering`) "
        "are merged under the longer canonical key.",
        "- **YAML tags:** EleutherAI papers carry `eleutherai: incorporated`; "
        'HELM papers carry `helm: "incorporated"` in frontmatter.',
        "- **lighteval / OpenAI Evals:** These reports assess *implementability* only — "
        "no 'already included' tracking exists for these frameworks.",
        "",
        "*Source reports: `20260312-eleutherai-eval-harness-integration.md`, "
        "`20260312-helm-values-alignment-integration-report.md`, "
        "`20260312-lm-eval-implementability-report.md`, "
        "`20260312-inspect-eval-implementability-report.md`*",
        "",
    ]

    OUTPUT_REPORT.write_text("\n".join(out_lines))
    print(f"\nReport written → {OUTPUT_REPORT.relative_to(VAULT.parent)}")

    # Spot-checks
    print("\n--- Spot checks ---")
    for needle in ("Parrish-BBQ", "Lin-TruthfulQA"):
        matches = [p for p in all_papers if needle.lower() in p.lower()]
        print(f"  '{needle}': {matches}")

    # Confirm expected spot-check coverage
    for key in list(all_papers):
        if "lin-truthfulqa" in key.lower() or "truthfulqa" in key.lower():
            r = next(r for r in rows if r[0] == key)
            print(f"  TruthfulQA coverage: E={bool(r[2])} L={bool(r[3])} I={bool(r[4])} H={bool(r[5])}")


if __name__ == "__main__":
    main()
